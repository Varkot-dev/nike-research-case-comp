"""Declarative builder for NEW financial models (xlsxwriter), consistent by construction.

A model is a list of keyed rows. Each row has ONE formula template that is written into
every period column, so the 'one formula per row, consistent across columns' rule cannot
be broken by accident. Rows are anchored by defined names (k_<Sheet>_<key>) so later
edits (xl.py patch with {"key": ...}) find them even after someone inserts rows in Excel.

Template tokens (resolved per period column):
    {key}            same sheet, same period column            -> D7
    {key[-1]}        previous period column                    -> C7
    {Sheet.key}      another sheet; scalar -> $C$5, row -> same column
    {key@FY2031E}    one fixed period, absolute                -> $H$7
    {key@all}        the whole period range, absolute          -> $D$7:$H$7
    {col} {period} {idx}   column letter, period label, 1-based period number

    from model_builder import Model
    m = Model("x.xlsx", "Jordan Brand valuation", periods=["FY2027E", ...])
    inp = m.list_sheet("Inputs")
    inp.switch("case", "Active scenario", ["Bear", "Base", "Bull"], "Base")
    inp.scalar("tax", "Tax rate", 0.225, "%", source="consensus_and_valuation.md Section C")
    val.calc("ev", "Enterprise value", "$m", "={pv_fcf}+{pv_tv}")
    ts = m.timeline_sheet("Model")
    ts.scenario_rows("growth", "Revenue growth", "%", {"Bear": [...], "Base": [...], "Bull": [...]})
    ts.row("rev", "Revenue", "$m", "={rev[-1]}*(1+{growth})", first="={Inputs.j26}*(1+{growth})")
    m.check("Revenue positive", "=MIN({Model.rev@all})>0")  (TRUE/1 = pass; or a difference ~ 0)
    m.save()   # writes, recalculates with LibreOffice, caches values, reports errors
"""
import re
import sys
from pathlib import Path

import xlsxwriter
from xlsxwriter.utility import xl_col_to_name, xl_rowcol_to_cell

sys.path.insert(0, str(Path(__file__).resolve().parent))

FMT = {   # unit -> number format. Negatives in parentheses, zero as a dash, units live in column B.
    "$m": '#,##0_);(#,##0);"-"_)',
    "$m.1": '#,##0.0_);(#,##0.0);"-"_)',
    "$": '$#,##0.00_);($#,##0.00);"-"_)',
    "%": '0.0%_);(0.0%);"-"_)',
    "x": '0.0"x"',
    "yrs": '0.00',
    "#": '#,##0_);(#,##0);"-"_)',
    "flag": '0',
    "date": 'yyyy-mm-dd',
    "text": '@',
    "": 'General',
}
TOKEN = re.compile(r"\{([A-Za-z_][\w ]*\.)?([A-Za-z_]\w*)(\[[+-]?\d+\]|@[\w.+-]+)?\}|\{(col|period|idx)\}")
BLUE, GREEN, BLACK = "#0000FF", "#008000", "#000000"
FONT = "Arial"


def safe(name):
    return re.sub(r"\W", "_", name)


def qs(sheet):
    return sheet if re.fullmatch(r"[A-Za-z_]\w*", sheet) else "'" + sheet.replace("'", "''") + "'"


class Model:
    def __init__(self, path, title, periods, description="", period_label="Fiscal year"):
        self.path, self.title, self.periods = str(path), title, list(periods)
        self.description, self.period_label = description, period_label
        self.wb = xlsxwriter.Workbook(self.path)
        self.wb.set_calc_mode("auto")
        self.sheets, self.order = {}, []
        self.checks = []
        self._fmt_cache = {}
        self.cover = self.wb.add_worksheet("Cover")

    # ---- formats
    def fmt(self, unit="", color=BLACK, bold=False, fill=None, italic=False, border=False):
        key = (unit, color, bold, fill, italic, border)
        if key not in self._fmt_cache:
            d = {"font_name": FONT, "font_size": 10, "font_color": color, "bold": bold, "italic": italic,
                 "num_format": FMT.get(unit, unit)}
            if fill:
                d["bg_color"] = fill
            if border:
                d["top"] = 1
            self._fmt_cache[key] = self.wb.add_format(d)
        return self._fmt_cache[key]

    def list_sheet(self, name):
        s = ListSheet(self, name)
        self.sheets[name] = s
        self.order.append(s)
        return s

    def timeline_sheet(self, name):
        s = TimelineSheet(self, name)
        self.sheets[name] = s
        self.order.append(s)
        return s

    def chart_sheet(self, name):
        s = ChartSheet(self, name)
        self.sheets[name] = s
        self.order.append(s)
        return s

    def check(self, label, formula, tol=0.001):
        """Two kinds, picked from the formula: a comparison (contains < > =) must be TRUE;
        anything else is a difference that must be within tol of zero. Kept separate on
        purpose: LibreOffice has no boolean type (TRUE is 1, ISLOGICAL is FALSE), so one
        formula that tries to handle both behaves differently in Excel and LibreOffice."""
        kind = "true" if re.search(r"[<>=]", formula[1:]) else "zero"
        self.checks.append((label, formula, tol, kind))

    # ---- check templates (three-statement, DCF and LBO integrity; feed the master check)
    def check_rows_equal(self, label, a, b, tol=0.5):
        """Every period of row a equals row b (balance sheet balances, CF cash = BS cash,
        segments sum to total). a and b are tokens like 'Model.assets'."""
        self.check(label, f"=SUMPRODUCT(ABS({{{a}@all}}-{{{b}@all}}))", tol)

    def check_rows_nonneg(self, label, row):
        """No negative balances (debt tranches, cash, inventory)."""
        self.check(label, f"=MIN({{{row}@all}})>=0")

    def check_between(self, label, expr, lo, hi):
        """A scalar inside a sanity band, e.g. terminal-value share of EV, tax rate."""
        e = expr if expr.startswith("{") or expr.startswith("(") else "(" + expr + ")"
        self.check(label, f"=AND({e}>={lo},{e}<={hi})")

    def check_less(self, label, a, b):
        """a < b, e.g. terminal growth below WACC."""
        self.check(label, f"={a}<{b}")

    # ---- token resolution shared by both sheet kinds
    def ref(self, home, sheetname, key, mod, col):
        sh = self.sheets[sheetname]
        if key not in sh.keys:
            raise KeyError(f"unknown key {key!r} on sheet {sheetname!r} (referenced from {home.name})")
        r, kind = sh.keys[key]
        prefix = "" if sh is home else qs(sh.name) + "!"
        if kind == "scalar":
            return prefix + xl_rowcol_to_cell(r, sh.value_col, True, True)
        c0 = sh.first_col
        if mod is None:
            if col is None:
                raise ValueError(f"{{{key}}} is a timeline row; from a scalar use {{{key}@PERIOD}} or {{{key}@all}}")
            return prefix + xl_rowcol_to_cell(r, col)
        if mod.startswith("["):
            off = int(mod[1:-1])
            if col + off < c0:
                raise ValueError(f"{key}{mod} reaches before the first period; use first=")
            return prefix + xl_rowcol_to_cell(r, col + off)
        p = mod[1:]
        if p == "all":
            return prefix + xl_rowcol_to_cell(r, c0, True, True) + ":" + xl_rowcol_to_cell(r, c0 + len(self.periods) - 1, True, True)
        if p not in self.periods:
            raise KeyError(f"unknown period {p}")
        return prefix + xl_rowcol_to_cell(r, c0 + self.periods.index(p), True, True)

    def render(self, home, template, col=None):
        def sub(m):
            if m.group(4):
                if col is None:
                    raise ValueError("{col}/{period}/{idx} only exist on timeline rows")
                i = col - home.first_col
                return {"col": xl_col_to_name(col), "period": self.periods[i], "idx": str(i + 1)}[m.group(4)]
            sheet = (m.group(1) or "").rstrip(".") or home.name
            return self.ref(home, sheet, m.group(2), m.group(3), col)
        return TOKEN.sub(sub, template)

    # ---- output
    def save(self, recalc=True):
        for s in self.order:
            s.write()
        for ws in self.wb.worksheets():
            # print-ready: landscape, one page wide, header rows repeated, footer with sheet and page
            ws.set_landscape(); ws.fit_to_pages(1, 0); ws.set_paper(1)
            ws.set_footer("&L&A&R&P of &N")
            if ws.name != "Cover" and not isinstance(self.sheets.get(ws.name), ChartSheet):
                ws.repeat_rows(0, 2)
        self._write_checks()
        self._write_cover()
        self.wb.close()
        report = {"path": self.path}
        if recalc:
            import xl
            v = xl.verify(self.path)
            report["verify"] = {k: v[k] for k in ("formulas", "errors", "status")}
            report["cached_values_written"] = xl.refresh_cache(self.path, v["recalculated_copy"])
        return report

    def _write_checks(self):
        if not self.checks:
            return
        ws = self.wb.add_worksheet("Checks")
        ws.hide_gridlines(2)
        ws.set_column(0, 0, 48); ws.set_column(1, 3, 14)
        ws.write_row(0, 0, ["Check", "Value", "Tolerance", "Pass (1/0)"], self.fmt(bold=True))
        home = type("Home", (), {"name": "Checks", "keys": {}, "first_col": None})()
        for i, (label, formula, tol, kind) in enumerate(self.checks, start=1):
            ws.write(i, 0, label, self.fmt())
            v, t = xl_rowcol_to_cell(i, 1), xl_rowcol_to_cell(i, 2)
            if kind == "true":
                ws.write_formula(i, 1, f"=IF({self.render(home, formula)[1:]},1,0)", self.fmt("flag"))
                ws.write(i, 2, "must be 1", self.fmt(italic=True))
                ws.write_formula(i, 3, f"={v}", self.fmt("flag"))
            else:
                ws.write_formula(i, 1, self.render(home, formula), self.fmt("#,##0.000000"))
                ws.write(i, 2, tol, self.fmt("0.000000", BLUE))
                ws.write_comment(i, 2, "Source: model convention (check tolerance; must exceed float and iteration noise)")
                ws.write_formula(i, 3, f"=IF(ABS({v})<={t},1,0)", self.fmt("flag"))
        n = len(self.checks)
        ws.write(n + 2, 0, "Master check (1 = all pass)", self.fmt(bold=True))
        ws.write_formula(n + 2, 3, f"=IF(SUM(D2:D{n + 1})=COUNT(D2:D{n + 1}),1,0)", self.fmt("flag", bold=True))
        self.wb.define_name("MasterCheck", f"=Checks!$D${n + 3}")

    def _write_cover(self):
        ws = self.cover
        ws.hide_gridlines(2)
        ws.set_column(0, 0, 30); ws.set_column(1, 1, 80)
        ws.write(0, 0, self.title, self.fmt(bold=True))
        if self.description:
            ws.write(1, 0, self.description, self.fmt(italic=True))
        ws.write(3, 0, "Master check", self.fmt(bold=True))
        if self.checks:
            ws.write_formula(3, 1, '=IF(MasterCheck=1,"OK: all checks pass","ERROR: see Checks sheet")', self.fmt(bold=True))
        legend = [("Blue text", "hard-coded input (change these)", BLUE), ("Black text", "formula", BLACK),
                  ("Green text", "link from another sheet", GREEN), ("Yellow fill", "scenario switch", BLACK)]
        ws.write(5, 0, "Colour key", self.fmt(bold=True))
        for i, (k, v, c) in enumerate(legend, start=6):
            ws.write(i, 0, k, self.fmt(color=c, fill="#FFFF00" if "Yellow" in k else None))
            ws.write(i, 1, v, self.fmt())
        ws.write(11, 0, "Sheets", self.fmt(bold=True))
        for i, s in enumerate(self.order, start=12):
            ws.write(i, 0, s.name, self.fmt())
            ws.write(i, 1, s.purpose, self.fmt())


class _Sheet:
    def __init__(self, model, name):
        self.m, self.name, self.keys, self.items, self.purpose = model, name, {}, [], ""
        self.next_row = 3

    def describe(self, text):
        self.purpose = text
        return self

    def section(self, title):
        self.items.append(("section", self.next_row, title))
        self.next_row += 1

    def blank(self):
        self.next_row += 1

    def _claim(self, key, kind):
        if key in self.keys:
            raise KeyError(f"duplicate key {key} on {self.name}")
        self.keys[key] = (self.next_row, kind)
        r = self.next_row
        self.next_row += 1
        return r

    def _name(self, key, r):
        self.m.wb.define_name(f"k_{safe(self.name)}_{key}", f"={qs(self.name)}!$A${r + 1}")


class ListSheet(_Sheet):
    """Vertical list of scalars: A label, B unit, C value (live), D.. scenario cases, then source."""
    value_col = 2

    def __init__(self, model, name):
        super().__init__(model, name)
        self.cases = None
        self.ws = model.wb.add_worksheet(name)

    def switch(self, key, label, options, default):
        self.cases = list(options)
        r = self._claim(key, "scalar")
        self.items.append(("switch", r, key, label, options, default))
        ri = self._claim(key + "_idx", "scalar")
        self.items.append(("scalar", ri, key + "_idx", label + " (index)", "#",
                           f"=MATCH({xl_rowcol_to_cell(r, 2, True, True)},{{{','.join(chr(34) + o + chr(34) for o in options)}}},0)",
                           "derived from the switch above", False))
        self.switch_cell = xl_rowcol_to_cell(ri, 2, True, True)
        self.switch_ref = f"{qs(self.name)}!{self.switch_cell}"

    def scalar(self, key, label, value, unit="", source="", formula=False):
        """A hard-coded input (blue). Use calc() for formulas."""
        if unit and unit not in FMT and not any(ch in unit for ch in "#0"):
            raise ValueError(f"scalar {key}: unknown unit {unit!r}; arguments are (key, label, value, unit, source)")
        r = self._claim(key, "scalar")
        self.items.append(("scalar", r, key, label, unit, value, source, formula))

    def calc(self, key, label, unit, formula, note=""):
        """A formula scalar (outputs, derived values). Same template tokens as rows."""
        if not str(formula).startswith("="):
            raise ValueError(f"calc {key}: formula must start with '='")
        self.scalar(key, label, formula, unit, note)

    def scenario(self, key, label, unit, values, source=""):
        """One input per case in columns D.., live value in C picked by the switch."""
        if not self.cases:
            raise ValueError("call switch() before scenario()")
        r = self._claim(key, "scalar")
        self.items.append(("scenario", r, key, label, unit, values, source))

    def write(self):
        m, ws = self.m, self.ws
        ws.hide_gridlines(2)
        ws.set_column(0, 0, 44); ws.set_column(1, 1, 8); ws.set_column(2, 2, 12)
        ncase = len(self.cases or [])
        ws.set_column(3, 3 + ncase, 12); ws.set_column(3 + ncase, 3 + ncase, 70)
        ws.write(0, 0, self.name, m.fmt(bold=True))
        hdr = ["Item", "Unit", "Live"] + (self.cases or []) + ["Source / note"]
        ws.write_row(2, 0, hdr, m.fmt(bold=True, border=True))
        ws.freeze_panes(3, 1)
        src_col = 3 + ncase
        for it in self.items:
            kind, r = it[0], it[1]
            if kind == "section":
                ws.write(r, 0, it[2], m.fmt(bold=True, fill="#DDEBF7"))
                continue
            if kind == "switch":
                _, r, key, label, options, default = it
                ws.write(r, 0, label, m.fmt(bold=True))
                ws.write(r, 2, default, m.fmt("text", BLUE, bold=True, fill="#FFFF00"))
                ws.data_validation(r, 2, r, 2, {"validate": "list", "source": list(options)})
                ws.write(r, src_col, "Pick a case; every scenario row follows it", m.fmt(italic=True))
            elif kind == "scalar":
                _, r, key, label, unit, value, source, is_formula = it
                ws.write(r, 0, label, m.fmt()); ws.write(r, 1, unit, m.fmt())
                if isinstance(value, str) and value.startswith("="):
                    f = m.render(self, value)
                    color = GREEN if re.fullmatch(r"=('[^']+'|\w+)!\$?[A-Z]+\$?\d+", f) else BLACK
                    ws.write_formula(r, 2, f, m.fmt(unit, color))
                else:
                    ws.write(r, 2, value, m.fmt(unit, BLUE))
                    if source:   # the source travels with the cell, even if the note column is cut
                        ws.write_comment(r, 2, f"Source: {source}", {"x_scale": 2})
                if source:
                    ws.write(r, src_col, source, m.fmt(italic=True))
            elif kind == "scenario":
                _, r, key, label, unit, values, source = it
                ws.write(r, 0, label, m.fmt()); ws.write(r, 1, unit, m.fmt())
                for j, case in enumerate(self.cases):
                    ws.write(r, 3 + j, values[case], m.fmt(unit, BLUE))
                if source:
                    ws.write_comment(r, 3, f"Source: {source}", {"x_scale": 2})
                choices = ",".join(xl_rowcol_to_cell(r, 3 + j) for j in range(ncase))
                ws.write_formula(r, 2, f"=CHOOSE({self.switch_cell},{choices})", m.fmt(unit, BLACK))
                if source:
                    ws.write(r, src_col, source, m.fmt(italic=True))
            self._name(it[2], r)


class TimelineSheet(_Sheet):
    """A label, B unit, periods from column C. One template per row."""
    first_col = 2

    def __init__(self, model, name):
        super().__init__(model, name)
        self.ws = model.wb.add_worksheet(name)

    def row(self, key, label, unit, formula=None, first=None, values=None, bold=False, note=""):
        r = self._claim(key, "row")
        self.items.append(("row", r, key, label, unit, formula, first, values, bold, note))

    def scenario_rows(self, key, label, unit, values_by_case, switch=None, list_sheet="Inputs", source=""):
        """One blue input row per case plus a live row = CHOOSE(switch, cases...)."""
        ls = self.m.sheets[list_sheet]
        sw = switch or ls.switch_ref
        case_keys = []
        for case in ls.cases:
            k = f"{key}_{safe(case).lower()}"
            self.row(k, f"{label}: {case}", unit, values=values_by_case[case], note=source)
            case_keys.append(k)
        self.row(key, f"{label} (live)", unit, "=CHOOSE(" + sw + "," + ",".join("{" + k + "}" for k in case_keys) + ")", bold=True)

    def write(self):
        m, ws = self.m, self.ws
        ws.hide_gridlines(2)
        n = len(m.periods)
        ws.set_column(0, 0, 40); ws.set_column(1, 1, 7); ws.set_column(2, 2 + n - 1, 11)
        ws.set_column(2 + n, 2 + n, 50)
        ws.write(0, 0, self.name, m.fmt(bold=True))
        ws.write(2, 0, m.period_label, m.fmt(bold=True, border=True))
        ws.write(2, 1, "Unit", m.fmt(bold=True, border=True))
        for j, p in enumerate(m.periods):
            ws.write_string(2, 2 + j, p, m.fmt("text", bold=True, border=True))
        ws.freeze_panes(3, 2)
        for it in self.items:
            if it[0] == "section":
                ws.write(it[1], 0, it[2], m.fmt(bold=True, fill="#DDEBF7"))
                continue
            _, r, key, label, unit, formula, first, values, bold, note = it
            ws.write(r, 0, label, m.fmt(bold=bold)); ws.write(r, 1, unit, m.fmt())
            for j in range(n):
                col = 2 + j
                if values is not None:
                    ws.write(r, col, values[j], m.fmt(unit, BLUE, bold))
                    if j == 0 and note:
                        ws.write_comment(r, col, f"Source: {note}", {"x_scale": 2})
                    continue
                tpl = first if (j == 0 and first) else formula
                f = m.render(self, tpl, col)
                color = GREEN if re.fullmatch(r"=('[^']+'|\w+)!\$?[A-Z]+\$?\d+", f) else BLACK
                ws.write_formula(r, col, f, m.fmt(unit, color, bold))
            if note:
                ws.write(r, 2 + n, note, m.fmt(italic=True))
            self._name(key, r)


class ChartSheet:
    """Presentation charts that stay live: a small formula table plus a chart drawn from it.
    Built from stacked bars/columns with an invisible base series, which renders the same in
    Excel, LibreOffice and Google Sheets (Excel 2016's native waterfall type does not)."""
    value_col = 1

    def __init__(self, model, name):
        self.m, self.name, self.keys, self.purpose, self.first_col = model, name, {}, "", None
        self.ws = model.wb.add_worksheet(name)
        self.blocks, self.next_row = [], 2

    def describe(self, text):
        self.purpose = text
        return self

    def _val(self, ws, r, c, v, unit, color=BLACK):
        if isinstance(v, str) and v.startswith("="):
            ws.write_formula(r, c, self.m.render(self, v), self.m.fmt(unit, color))
        else:
            ws.write(r, c, v, self.m.fmt(unit, BLUE))

    def football_field(self, title, rows, unit="$", marker=None, note=""):
        """rows: [(label, low, high, source)]; low/high are numbers (inputs) or templates.
        marker: (label, template), e.g. ("Current NKE price", "={Inputs.price}"), shown in the axis title."""
        self.blocks.append(("ff", self.next_row, title, rows, unit, marker, note))
        self.next_row += len(rows) + 6 + 22      # table, then the chart underneath it

    def waterfall(self, title, start, steps, unit="$m", note=""):
        """start: (label, template); steps: [(label, template)]. Ends with the running total.
        Adds a check that the bars reconcile: start + sum(steps) = end."""
        self.blocks.append(("wf", self.next_row, title, start, steps, unit, note))
        self.next_row += len(steps) + 8 + 20

    def write(self):
        m, ws = self.m, self.ws
        ws.hide_gridlines(2)
        ws.set_column(0, 0, 38); ws.set_column(1, 6, 12); ws.set_column(7, 7, 60)
        ws.write(0, 0, self.name, m.fmt(bold=True))
        ws.set_h_pagebreaks([b[1] - 1 for b in self.blocks[1:]])   # one chart block per printed page
        for b in self.blocks:
            if b[0] == "ff":
                self._write_ff(*b[1:])
            else:
                self._write_wf(*b[1:])

    def _write_ff(self, r0, title, rows, unit, marker, note):
        m, ws = self.m, self.ws
        ws.write(r0, 0, title, m.fmt(bold=True))
        ws.write_row(r0 + 1, 0, ["Method", "Low", "High", "Range", "Source"], m.fmt(bold=True, border=True))
        for i, (label, lo, hi, src) in enumerate(rows):
            r = r0 + 2 + i
            ws.write(r, 0, label, m.fmt())
            self._val(ws, r, 1, lo, unit); self._val(ws, r, 2, hi, unit)
            ws.write_formula(r, 3, f"={xl_rowcol_to_cell(r, 2)}-{xl_rowcol_to_cell(r, 1)}", m.fmt(unit))
            ws.write(r, 4, src, m.fmt(italic=True))
        last = r0 + 1 + len(rows)
        points = [None] * len(rows)
        if marker:
            # the marker is its own bar: a thin sliver at the live value, coloured differently
            last += 1
            ws.write(last, 0, marker[0], m.fmt(bold=True))
            ws.write_formula(last, 5, m.render(self, marker[1]), m.fmt(unit, GREEN))
            ws.write(last, 4, "live marker (column F), drawn as a sliver of width set in column G", m.fmt(italic=True))
            ws.write(last, 6, 0.005, m.fmt("0.0%", BLUE))
            ws.write_comment(last, 6, "Source: presentation convention (marker bar width as a share of the value)")
            v, wd = xl_rowcol_to_cell(last, 5), xl_rowcol_to_cell(last, 6)
            ws.write_formula(last, 1, f"={v}-ABS({v})*{wd}", m.fmt(unit))
            ws.write_formula(last, 2, f"={v}+ABS({v})*{wd}", m.fmt(unit))
            ws.write_formula(last, 3, f"={xl_rowcol_to_cell(last, 2)}-{xl_rowcol_to_cell(last, 1)}", m.fmt(unit))
            points.append({"fill": {"color": "#C00000"}})
        ch = m.wb.add_chart({"type": "bar", "subtype": "stacked"})
        cats = [self.name, r0 + 2, 0, last, 0]
        ch.add_series({"name": "Low", "categories": cats, "values": [self.name, r0 + 2, 1, last, 1],
                       "fill": {"none": True}, "border": {"none": True}})
        ch.add_series({"name": "Range", "categories": cats, "values": [self.name, r0 + 2, 3, last, 3],
                       "fill": {"color": "#1F4E79"}, "gap": 60, "points": points})
        ch.set_title({"name": title, "name_font": {"size": 11, "name": FONT}})
        ch.set_legend({"none": True})
        ch.set_y_axis({"reverse": True})
        ch.set_x_axis({"num_format": FMT.get(unit, unit), "major_gridlines": {"visible": True, "line": {"color": "#D9D9D9"}}})
        ch.set_size({"width": 720, "height": 110 + 45 * (last - r0 - 1)})
        ws.insert_chart(last + 3, 0, ch)
        if note:
            ws.write(last + 2, 0, note, m.fmt(italic=True))

    def _write_wf(self, r0, title, start, steps, unit, note):
        m, ws = self.m, self.ws
        ws.write(r0, 0, title, m.fmt(bold=True))
        ws.write_row(r0 + 1, 0, ["Step", "Value", "Running total", "Base", "Increase", "Decrease", "Total"],
                     m.fmt(bold=True, border=True))
        c = lambda r, k: xl_rowcol_to_cell(r, k)
        r = r0 + 2
        ws.write(r, 0, start[0], m.fmt(bold=True)); self._val(ws, r, 1, start[1], unit, GREEN)
        ws.write_formula(r, 2, f"={c(r, 1)}", m.fmt(unit))
        ws.write_blank(r, 3, None, m.fmt(unit)); ws.write_blank(r, 4, None, m.fmt(unit)); ws.write_blank(r, 5, None, m.fmt(unit))
        ws.write_formula(r, 6, f"={c(r, 1)}", m.fmt(unit))
        for label, tpl in steps:
            r += 1
            ws.write(r, 0, label, m.fmt()); self._val(ws, r, 1, tpl, unit, GREEN)
            ws.write_formula(r, 2, f"={c(r - 1, 2)}+{c(r, 1)}", m.fmt(unit))
            ws.write_formula(r, 3, f"=MIN({c(r - 1, 2)},{c(r, 2)})", m.fmt(unit))
            ws.write_formula(r, 4, f"=MAX({c(r, 1)},0)", m.fmt(unit))
            ws.write_formula(r, 5, f"=MAX(-{c(r, 1)},0)", m.fmt(unit))
            ws.write_blank(r, 6, None, m.fmt(unit))
        r += 1
        ws.write(r, 0, "End", m.fmt(bold=True))
        ws.write_formula(r, 2, f"={c(r - 1, 2)}", m.fmt(unit))
        ws.write_blank(r, 3, None, m.fmt(unit)); ws.write_blank(r, 4, None, m.fmt(unit)); ws.write_blank(r, 5, None, m.fmt(unit))
        ws.write_formula(r, 6, f"={c(r, 2)}", m.fmt(unit, bold=True))
        ch = m.wb.add_chart({"type": "column", "subtype": "stacked"})
        cats = [self.name, r0 + 2, 0, r, 0]
        for k, name, fill in ((3, "Base", None), (6, "Total", "#1F4E79"), (4, "Increase", "#548235"), (5, "Decrease", "#C00000")):
            ser = {"name": name, "categories": cats, "values": [self.name, r0 + 2, k, r, k], "gap": 50}
            ser.update({"fill": {"none": True}, "border": {"none": True}} if fill is None else {"fill": {"color": fill}})
            ch.add_series(ser)
        ch.set_title({"name": title, "name_font": {"size": 11, "name": FONT}})
        ch.set_legend({"none": True})
        ch.set_y_axis({"num_format": FMT.get(unit, unit), "major_gridlines": {"visible": True, "line": {"color": "#D9D9D9"}}})
        ch.set_size({"width": 720, "height": 300})
        ws.insert_chart(r + 3, 0, ch)
        if note:
            ws.write(r + 1, 0, note, m.fmt(italic=True))
        # reconciliation check: the bars must add up to the end value
        ref = lambda rr, k: f"{qs(self.name)}!{xl_rowcol_to_cell(rr, k, True, True)}"
        m.checks.append((f"{title}: bars reconcile", f"={ref(r, 6)}-{ref(r0 + 2, 1)}-SUM({ref(r0 + 3, 1)}:{ref(r - 1, 1)})",
                         0.001, "zero"))
