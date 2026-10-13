"""Model audit: structured findings with severity, confidence and detection mode.

Rules combine this skill's own checks with prior art, each verified on its source page:
- PerfectXL Risk Finder inspections (https://www.perfectxl.com/learning-center/risk-finder-library/):
  hardcoded numbers with their exclusion list, approximate lookups, double count, formula
  interrupted by other formula/data/blank (<=20% of the run), complexity thresholds (length
  200, 8+ operations, 5+ nested functions, 10+ references), hidden and invisible content.
- Microsoft Inquire items via O'Beirne, EuSpRIG 2013 (arXiv 1401.7586): unused inputs,
  formulas referencing hidden cells or text, numbers stored as text.
- ExceLint (arXiv 1901.11100): references compared as relative vectors, so a lone cell whose
  shape differs from matching neighbours on both sides (row or column) is flagged.
- spreadsheet-auditor (github.com/petehottelet/spreadsheet-auditor): finding labels
  (deterministic/heuristic, Defect/Likely/Review/Info), annotated copy, fail-on exit codes.
- anthropics/financial-services audit-xls: summary rating Clean / Minor Issues / Major Issues.

Values come from a LibreOffice recalc of a copy, formulas from the file itself. Nothing
here edits the workbook; --annotate writes a separate REVIEW copy.
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import xlcore as X  # noqa: E402
from openpyxl import load_workbook  # noqa: E402
from openpyxl.utils import get_column_letter as i2col  # noqa: E402
from openpyxl.utils.cell import range_boundaries  # noqa: E402

ERRORS = ("#REF!", "#NAME?", "#VALUE!", "#DIV/0!", "#N/A", "#NUM!", "#NULL!", "#SPILL!", "#CALC!")
VOLATILE = ("OFFSET", "INDIRECT", "TODAY", "NOW", "RAND", "RANDBETWEEN", "CELL", "INFO")
NEEDS_PREFIX = ("XLOOKUP", "XMATCH", "FILTER", "SORT", "SORTBY", "UNIQUE", "SEQUENCE", "LET", "LAMBDA",
                "TEXTJOIN", "CONCAT", "IFS", "SWITCH", "MAXIFS", "MINIFS", "VSTACK", "HSTACK", "TAKE",
                "DROP", "CHOOSECOLS", "CHOOSEROWS", "TEXTSPLIT")
# PerfectXL exclusions: frequent numbers anywhere; common factors inside * and /.
ALLOW_ANY = {0.0, 1.0, 0.1, 0.25, 0.5, 0.75}
ALLOW_FACTOR = {0.5, 2, 10, 100, 1000, 4, 7, 12, 24, 30, 31, 52, 53, 60, 365, 366, 365.25, 3600, 1e6}
ARG_EXEMPT = {"ROUND", "ROUNDUP", "ROUNDDOWN", "MROUND", "INDEX", "MATCH", "VLOOKUP", "HLOOKUP", "CHOOSE", "OFFSET",
              "LEFT", "RIGHT", "MID", "TEXT", "DATE", "EDATE", "EOMONTH", "LARGE", "SMALL", "PERCENTILE", "QUARTILE",
              "RANK", "WEEKDAY", "SUBTOTAL", "AGGREGATE", "_XLFN.XLOOKUP", "_XLFN.XMATCH", "YEARFRAC", "DATEDIF"}
YEARLIKE = re.compile(r"^(FY|CY)?'?\d{2,4}[AEBF]?$|^(Q[1-4]|H[12])\s?(FY)?'?\d{2,4}[AEBF]?$", re.I)

# id: (severity, confidence, mode, fix)
RULES = {
    "LIVE_ERROR_ROOT": ("high", "Defect", "det", "Fix this cell; the errors downstream of it follow from it"),
    "LIVE_ERROR_PROPAGATED": ("info", "Info", "det", "Clears when the root error is fixed"),
    "REF_ERROR_IN_FORMULA": ("high", "Defect", "det", "A deleted range left #REF! in the formula text; rebuild the reference"),
    "NAME_WITH_REF_ERROR": ("medium", "Defect", "det", "Delete or repoint the defined name"),
    "CIRCULAR_REFERENCE": ("high", "Likely defect", "det", "Break the loop (opening balances) or add a circuit breaker; see modeling_standards.md section 6"),
    "INCONSISTENT_FORMULA": ("high", "Likely defect", "heur", "Copy the row's formula across, or document the exception"),
    "FORMULA_INTERRUPTED_BY_DATA": ("high", "Likely defect", "heur", "A typed number sits inside a formula row (pasted-over formula); restore the formula or move the input"),
    "FORMULA_INTERRUPTED_BY_BLANK": ("medium", "Review", "heur", "A gap inside a formula row; fill it or confirm it is intended"),
    "RANGE_STOPS_SHORT": ("high", "Likely defect", "heur", "Extend the range to include the adjacent line item"),
    "DOUBLE_COUNT": ("high", "Likely defect", "det", "The same cell is counted twice in one formula"),
    "SUBTOTAL_IN_TOTAL": ("high", "Likely defect", "heur", "The total adds a subtotal and its own components"),
    "APPROXIMATE_LOOKUP": ("medium", "Review", "det", "Use exact match: VLOOKUP/HLOOKUP 4th argument FALSE, MATCH 3rd argument 0"),
    "LITERAL_IN_FORMULA": ("medium", "Review", "det", "Move the number into a labelled input cell and reference it"),
    "REF_TO_BLANK": ("medium", "Review", "det", "The formula reads an empty cell; point it at the right input or fill the input"),
    "REF_TO_TEXT": ("medium", "Likely defect", "det", "Arithmetic on a text cell; check the reference"),
    "NUMBER_STORED_AS_TEXT": ("high", "Likely defect", "det", "SUM skips text; convert the cell to a number"),
    "NEEDS_XLFN_PREFIX": ("high", "Defect", "det", "Write the stored name (_xlfn.) or use a portable function (formulas.md)"),
    "VOLATILE_FUNCTION": ("low", "Review", "det", "Replace OFFSET/INDIRECT with INDEX; avoid TODAY/NOW in calculations"),
    "WHOLE_COLUMN_REF": ("low", "Review", "det", "Use a bounded range"),
    "IFERROR_MASK": ("low", "Review", "det", "Guard the specific error (IF(d=0,...)) rather than masking all errors"),
    "EXTERNAL_LINK": ("medium", "Review", "det", "External links break silently; import the value with a source note"),
    "COMPLEX_FORMULA": ("low", "Review", "heur", "Split into helper rows (FAST 3.03-01)"),
    "NESTED_IF": ("low", "Review", "det", "Use INDEX/CHOOSE or a lookup table (FAST 3.03-07)"),
    "DOUBLE_OPERATOR": ("low", "Review", "det", "Check the sign; --x is fine only as a deliberate boolean coercion"),
    "UNUSED_INPUT": ("low", "Review", "heur", "An input nothing reads; remove it or wire it in"),
    "HIDDEN_SHEET": ("medium", "Review", "det", "Unhide; nothing in a model should be hidden (FAST 2.01-08)"),
    "HIDDEN_CELL_REFERENCED": ("medium", "Review", "det", "A formula reads a hidden row or column"),
    "INVISIBLE_VALUE": ("medium", "Review", "det", "Font matches fill or format is ;;; so the value cannot be seen"),
    "CALC_MANUAL": ("high", "Defect", "det", "Set calculation to automatic"),
    "ITERATIVE_CALC_ON": ("info", "Info", "det", "Circularity is intended; confirm a circuit breaker exists"),
    "DATE_1904": ("medium", "Review", "det", "Date serials differ by 1,462 days from the 1900 system"),
    "FORMULA_COLORED_AS_INPUT": ("low", "Review", "det", "Blue means hard-coded input; recolour the formula black"),
    "INPUT_NOT_BLUE": ("low", "Review", "det", "Colour hard-coded inputs blue so readers can find them"),
    "LINK_NOT_GREEN": ("info", "Info", "det", "Colour cross-sheet links green"),
    "MISSING_SOURCE": ("medium", "Review", "heur", "Every hard-coded input needs a source (comment or note column)"),
    "PERCENT_AS_WHOLE_NUMBER": ("high", "Likely defect", "heur", "Percentages are fractions: 5% is 0.05"),
}
SEV_RANK = {"high": 3, "medium": 2, "low": 1, "info": 0}


def is_formula(v):
    return isinstance(v, str) and v.startswith("=")


def font_rgb(cell):
    try:
        c = cell.font.color
        if c is not None and c.type == "rgb" and isinstance(c.rgb, str):
            return c.rgb[-6:].upper()
    except Exception:
        pass
    return None


def fill_rgb(cell):
    try:
        f = cell.fill
        if f is not None and f.fill_type == "solid" and f.fgColor.type == "rgb":
            return f.fgColor.rgb[-6:].upper()
    except Exception:
        pass
    return None


def tokens(f):
    try:
        return X.Tokenizer(f).items
    except Exception:
        return []


def expand(addr, maxcells=20000):
    try:
        c1, r1, c2, r2 = range_boundaries(addr.replace("$", ""))
    except Exception:
        return []
    if None in (c1, r1, c2, r2) or (c2 - c1 + 1) * (r2 - r1 + 1) > maxcells:
        return []
    return [f"{i2col(c)}{r}" for r in range(r1, r2 + 1) for c in range(c1, c2 + 1)]


def label_of(ws, r):
    for c in range(1, 4):
        v = ws.cell(r, c).value
        if isinstance(v, str) and v.strip() and not v.startswith("="):
            return v.strip()
    return ""


def header_rows(ws, scan=15):
    out = []
    for r in range(1, min(ws.max_row, scan) + 1):
        hits = 0
        for c in range(1, ws.max_column + 1):
            v = ws.cell(r, c).value
            if isinstance(v, (int, float)) and not isinstance(v, bool) and 1990 <= v <= 2100 and float(v).is_integer():
                hits += 1
            elif isinstance(v, str) and YEARLIKE.match(v.strip()):
                hits += 1
        if hits >= 3:
            out.append(r)
    return out


class Auditor:
    def __init__(self, path, values_path=None):
        self.path = path
        self.wf = load_workbook(path)
        self.wv = load_workbook(values_path or X.lo_recalc_copy(path), data_only=True)
        self.findings = []
        self.names = {n: d.attr_text for n, d in self.wf.defined_names.items()}

    def add(self, rid, sheet, cell, msg):
        key = (rid, sheet, cell, msg)
        if key in getattr(self, "_seen", set()):
            return
        self._seen = getattr(self, "_seen", set()) | {key}
        sev, conf, mode, fix = RULES[rid]
        self.findings.append({"id": rid, "sheet": sheet, "cell": cell, "severity": sev, "confidence": conf,
                              "mode": mode, "issue": msg, "fix": fix})

    # ---------------------------------------------------------------- graph
    def build_graph(self):
        self.prec, self.dep = {}, defaultdict(set)
        for ws in self.wf.worksheets:
            for row in ws.iter_rows():
                for c in row:
                    if not is_formula(c.value):
                        continue
                    key = f"{ws.title}!{c.coordinate}"
                    deps = []
                    for sh, addr in X.iter_formula_refs(c.value):
                        if addr in self.names and not sh:
                            sh, addr = X.split_sheet(self.names[addr])
                        for cell in expand(addr):
                            deps.append(f"{sh or ws.title}!{cell}")
                    self.prec[key] = deps
                    for d in deps:
                        self.dep[d].add(key)

    def value(self, key):
        sh, a = key.split("!", 1)
        try:
            return self.wv[sh][a].value
        except Exception:
            return None

    # ---------------------------------------------------------------- checks
    def workbook_checks(self):
        calc = self.wf.calculation
        if getattr(calc, "calcMode", None) == "manual":
            self.add("CALC_MANUAL", "", "", "Workbook calculation mode is manual")
        if getattr(calc, "iterate", False):
            self.add("ITERATIVE_CALC_ON", "", "", f"iterate on, count {calc.iterateCount or 100}, delta {calc.iterateDelta or 0.001}"
                     + (" (schema defaults)" if not calc.iterateCount else ""))
        if getattr(self.wf, "epoch", None) is not None and self.wf.epoch.year == 1904:
            self.add("DATE_1904", "", "", "Workbook uses the 1904 date system")
        for n, t in self.names.items():
            if t and "#REF!" in t:
                self.add("NAME_WITH_REF_ERROR", "", n, f"Defined name {n} = {t}")
        for ws in self.wf.worksheets:
            if ws.sheet_state != "visible":
                self.add("HIDDEN_SHEET", ws.title, "", f"Sheet state {ws.sheet_state}")

    def error_checks(self):
        errs = {}
        for ws in self.wf.worksheets:
            for row in ws.iter_rows():
                for c in row:
                    v = self.wv[ws.title][c.coordinate].value
                    if isinstance(v, str) and v in ERRORS:
                        errs[f"{ws.title}!{c.coordinate}"] = v
                    if is_formula(c.value) and "#REF!" in c.value:
                        self.add("REF_ERROR_IN_FORMULA", ws.title, c.coordinate, c.value[:90])
        for key, v in errs.items():
            upstream = [p for p in self.prec.get(key, []) if p in errs]
            sh, a = key.split("!", 1)
            if upstream:
                self.add("LIVE_ERROR_PROPAGATED", sh, a, f"{v} inherited from {upstream[0]}")
            else:
                n = self._downstream_count(key, errs)
                self.add("LIVE_ERROR_ROOT", sh, a, f"{v} ({label_of(self.wf[sh], self.wf[sh][a].row)}); {n} downstream error cells")

    def _downstream_count(self, key, errs):
        seen, stack = set(), [key]
        while stack:
            u = stack.pop()
            for v in self.dep.get(u, ()):
                if v not in seen and v in errs:
                    seen.add(v)
                    stack.append(v)
        return len(seen)

    def formula_checks(self):
        for ws in self.wf.worksheets:
            hidden_rows = {r for r, d in ws.row_dimensions.items() if d.hidden}
            hidden_cols = {k for k, d in ws.column_dimensions.items() if d.hidden}
            for row in ws.iter_rows():
                for c in row:
                    f = c.value
                    if not is_formula(f):
                        continue
                    where = (ws.title, c.coordinate)
                    up = f.upper()
                    toks = tokens(f)
                    self._literals(where, f, toks)
                    self._lookups(where, toks)
                    for fn in VOLATILE:
                        if re.search(rf"\b{fn}\(", up):
                            self.add("VOLATILE_FUNCTION", *where, fn)
                    for fn in NEEDS_PREFIX:
                        if re.search(rf"(?<![._A-Z]){fn}\(", up):
                            self.add("NEEDS_XLFN_PREFIX", *where, f"{fn} written without _xlfn.")
                    if re.search(r"(?<![A-Z$])\$?[A-Z]{1,3}:\$?[A-Z]{1,3}(?![0-9(])", up):
                        self.add("WHOLE_COLUMN_REF", *where, f[:80])
                    if "IFERROR(" in up:
                        self.add("IFERROR_MASK", *where, f[:80])
                    if re.search(r"\[\d+\]", f):
                        self.add("EXTERNAL_LINK", *where, f[:80])
                    if re.search(r"(--|\+-|-\+|\+\+)", f.replace('"', "'")) and "SUMPRODUCT" not in up:
                        self.add("DOUBLE_OPERATOR", *where, f[:80])
                    self._complexity(where, f, toks)
                    self._double_count(ws, where, f)
                    self._refs(ws, where, f, hidden_rows, hidden_cols)

    def _literals(self, where, f, toks):
        stack, prev = [], None
        for i, t in enumerate(toks):
            if t.type == "FUNC" and t.subtype == "OPEN":
                stack.append(t.value[:-1].upper())
            elif t.type == "FUNC" and t.subtype == "CLOSE":
                stack and stack.pop()
            elif t.type == "OPERAND" and t.subtype == "NUMBER":
                if stack and stack[-1] in ARG_EXEMPT:
                    continue
                try:
                    v = float(t.value)
                except ValueError:
                    continue
                nxt = toks[i + 1].value if i + 1 < len(toks) else ""
                pv = prev.value if prev is not None else ""
                in_factor = pv in ("*", "/") or nxt in ("*", "/") or pv == "^" or nxt == "%"
                if v in ALLOW_ANY or (in_factor and v in ALLOW_FACTOR) or (pv == "^"):
                    continue
                self.add("LITERAL_IN_FORMULA", *where, f"{t.value} in {f[:80]}")
                return
            if t.type != "WHITE-SPACE":
                prev = t

    def _lookups(self, where, toks):
        # walk function calls and count top-level arguments
        stack, arr = [], 0
        for t in toks:
            if t.type == "ARRAY":   # commas inside {a,b,c} constants are not argument separators
                arr += 1 if t.subtype == "OPEN" else -1
                if stack:
                    stack[-1][1][-1] += t.value
                continue
            if t.type == "FUNC" and t.subtype == "OPEN":
                stack.append([t.value[:-1].upper(), [""]])
            elif t.type == "SEP" and t.subtype == "ARG" and stack and arr == 0:
                stack[-1][1].append("")
            elif t.type == "FUNC" and t.subtype == "CLOSE" and stack:
                name, args = stack.pop()
                args = [a.strip().upper() for a in args]
                if name in ("VLOOKUP", "HLOOKUP") and (len(args) < 4 or args[3] not in ("FALSE", "0", "FALSE()")):
                    self.add("APPROXIMATE_LOOKUP", *where, f"{name} without exact-match FALSE")
                elif name == "MATCH" and (len(args) < 3 or args[2] != "0"):
                    self.add("APPROXIMATE_LOOKUP", *where, "MATCH without match_type 0")
                elif name == "LOOKUP":
                    self.add("APPROXIMATE_LOOKUP", *where, "LOOKUP always matches approximately")
                if stack:
                    stack[-1][1][-1] += name + "()"
            elif stack:
                stack[-1][1][-1] += t.value

    def _complexity(self, where, f, toks):
        funcs = [t.value[:-1].upper() for t in toks if t.type == "FUNC" and t.subtype == "OPEN"]
        ops = {t.value for t in toks if t.type.startswith("OPERATOR")}
        refs = [t for t in toks if t.type == "OPERAND" and t.subtype == "RANGE"]
        depth = mx = 0
        for t in toks:
            if t.type == "FUNC" and t.subtype == "OPEN":
                depth += 1; mx = max(mx, depth)
            elif t.type == "FUNC" and t.subtype == "CLOSE":
                depth -= 1
        reasons = []
        if len(f) >= 200:
            reasons.append(f"{len(f)} characters")
        if len(set(funcs) | ops) >= 8:
            reasons.append(f"{len(set(funcs) | ops)} distinct functions/operators")
        if mx >= 5:
            reasons.append(f"nesting depth {mx}")
        if len(refs) >= 10:
            reasons.append(f"{len(refs)} references")
        if reasons:
            self.add("COMPLEX_FORMULA", *where, ", ".join(reasons))
        if funcs.count("IF") >= 3:
            self.add("NESTED_IF", *where, f"{funcs.count('IF')} IFs")

    def _double_count(self, ws, where, f):
        # only purely additive formulas (refs joined by + or inside SUM), where a repeat is a real double count
        toks = [t for t in tokens(f) if t.type != "WHITE-SPACE"]
        additive = toks and all(
            (t.type == "OPERAND" and t.subtype == "RANGE") or (t.type == "OPERATOR-INFIX" and t.value == "+")
            or (t.type == "FUNC" and t.value.upper() in ("SUM(", ")")) or (t.type == "SEP" and t.subtype == "ARG")
            for t in toks)
        if not additive:
            return
        seen = Counter()
        for sh, addr in X.iter_formula_refs(f):
            for cell in expand(addr, 5000):
                seen[f"{sh or ws.title}!{cell}"] += 1
        dup = [k for k, n in seen.items() if n > 1]
        if dup:
            self.add("DOUBLE_COUNT", *where, f"{dup[0]} counted {seen[dup[0]]} times")
        # subtotal inside the same total: a summed cell that itself SUMs other cells of this range
        members = set(seen)
        for m in members:
            sh, a = m.split("!", 1)
            try:
                inner = self.wf[sh][a].value
            except Exception:
                continue
            if is_formula(inner) and "SUM(" in inner.upper():
                inner_cells = {f"{s2 or sh}!{x}" for s2, ad in X.iter_formula_refs(inner) for x in expand(ad, 5000)}
                if len(inner_cells & members) >= 2:
                    self.add("SUBTOTAL_IN_TOTAL", *where, f"{m} is a subtotal of cells this formula also adds")
                    break

    def _refs(self, ws, where, f, hidden_rows, hidden_cols):
        toks = [t for t in tokens(f) if t.type != "WHITE-SPACE"]
        arith_refs = set()
        for i, t in enumerate(toks):
            if t.type == "OPERAND" and t.subtype == "RANGE":
                nb = [toks[j].value for j in (i - 1, i + 1) if 0 <= j < len(toks)]
                if any(v in ("+", "-", "*", "/", "^") for v in nb):
                    arith_refs.add(t.value)
        for sh, addr in X.iter_formula_refs(f):
            raw = (X.quote_sheet(sh) + "!" if sh else "") + addr
            arith = raw in arith_refs or addr in arith_refs or any(r.endswith("!" + addr) and sh for r in arith_refs)
            if addr in self.names or "[" in addr or "[" in (sh or ""):
                continue
            tws = self.wf[sh] if sh in self.wf.sheetnames else (ws if not sh else None)
            if tws is None:
                continue
            cells = expand(addr, 400)
            if len(cells) == 1:
                tc = tws[cells[0]]
                if tc.value is None:
                    self.add("REF_TO_BLANK", *where, f"-> {(sh + '!') if sh else ''}{cells[0]}")
                elif isinstance(tc.value, str) and not is_formula(tc.value) and arith:
                    try:
                        float(tc.value.replace(",", "").replace("%", ""))
                        self.add("NUMBER_STORED_AS_TEXT", tws.title, cells[0], f"'{tc.value}' read by {where[0]}!{where[1]}")
                    except ValueError:
                        self.add("REF_TO_TEXT", *where, f"-> {cells[0]} = '{tc.value[:30]}'")
            if tws is ws:
                for cell in cells:
                    cc, rr = X.split_cell(cell)
                    if rr in hidden_rows or i2col(cc) in hidden_cols:
                        self.add("HIDDEN_CELL_REFERENCED", *where, f"reads hidden {cell}")
                        break
            if len(cells) > 1:
                self._stops_short(tws, where, addr)

    def _stops_short(self, tws, where, addr):
        try:
            c1, r1, c2, r2 = range_boundaries(addr.replace("$", ""))
        except Exception:
            return
        if None in (c1, r1, c2, r2):
            return
        cands = []
        if c1 == c2 and r2 > r1:
            cands = [(c1, r2 + 1, c1, r2), (c1, r1 - 1, c1, r1)]
        elif r1 == r2 and c2 > c1:
            cands = [(c2 + 1, r1, c2, r1), (c1 - 1, r1, c1, r1)]
        fc, fr = X.split_cell(where[1])
        for nc, nr, ec, er in cands:
            if nc < 1 or nr < 1 or (tws.title == where[0] and (nc, nr) == (fc, fr)):
                continue
            nb, edge = tws.cell(nr, nc), tws.cell(er, ec)
            if nb.value is None or edge.value is None:
                continue
            if isinstance(nb.value, str) and not is_formula(nb.value):
                continue
            same_type = (is_formula(nb.value) == is_formula(edge.value))
            if is_formula(nb.value) and same_type:
                same_type = X.relative_form(nb.value, nb.coordinate) == X.relative_form(edge.value, edge.coordinate)
            if same_type and nb.number_format == edge.number_format and font_rgb(nb) == font_rgb(edge) \
                    and not label_of(tws, nr).lower().startswith(("total", "sum", "net", "ebit", "gross")):
                self.add("RANGE_STOPS_SHORT", *where, f"{addr} excludes adjacent like cell {nb.coordinate}")

    def layout_checks(self):
        """Lone-cell inconsistency (ExceLint style) along rows and columns, and runs
        interrupted by data or blanks (PerfectXL, <=20% of the run)."""
        for ws in self.wf.worksheets:
            maxr, maxc = ws.max_row, ws.max_column
            rel = {}
            for row in ws.iter_rows():
                for c in row:
                    if is_formula(c.value):
                        rel[(c.row, c.column)] = X.relative_form(c.value, c.coordinate)
            flagged = set()
            for (r, col), shape in rel.items():
                for (a, b) in (((r, col - 1), (r, col + 1)), ((r - 1, col), (r + 1, col))):
                    if a in rel and b in rel and rel[a] == rel[b] and rel[a] != shape:
                        # skip aggregates over their own neighbours (a SUM next to its inputs)
                        if (r, col) not in flagged:
                            flagged.add((r, col))
                            self.add("INCONSISTENT_FORMULA", ws.title, f"{i2col(col)}{r}",
                                     f"'{label_of(ws, r)}': differs from both neighbours, which agree "
                                     f"({ws.cell(*a).coordinate}: {ws.cell(*a).value[:50]})")
            # runs along rows (time axis): dominant shape and interruptions
            hdr = header_rows(ws)
            for r in range(1, maxr + 1):
                cells = [(col, rel.get((r, col))) for col in range(1, maxc + 1)]
                shapes = Counter(s for _, s in cells if s)
                if not shapes:
                    continue
                main, n = shapes.most_common(1)[0]
                if n < 3:
                    continue
                cols = [col for col, s in cells if s == main]
                span = range(cols[0], cols[-1] + 1)
                odd = []
                for col in span:
                    v = ws.cell(r, col).value
                    if rel.get((r, col)) == main:
                        continue
                    odd.append((col, v))
                if not odd or len(odd) > 0.2 * len(span):
                    continue
                for col, v in odd:
                    ref = f"{i2col(col)}{r}"
                    if v is None:
                        self.add("FORMULA_INTERRUPTED_BY_BLANK", ws.title, ref, f"gap in '{label_of(ws, r)}'")
                    elif not is_formula(v) and isinstance(v, (int, float)):
                        self.add("FORMULA_INTERRUPTED_BY_DATA", ws.title, ref, f"typed {v!r} in '{label_of(ws, r)}'")
                    elif is_formula(v) and (r, col) not in flagged:
                        self.add("INCONSISTENT_FORMULA", ws.title, ref, f"'{label_of(ws, r)}': {v[:60]} vs row pattern")

    def input_checks(self):
        convention = any(isinstance(c.value, (int, float)) and font_rgb(c) == "0000FF"
                         for ws in self.wf.worksheets for row in ws.iter_rows() for c in row)
        for ws in self.wf.worksheets:
            hdr = set(header_rows(ws))
            for row in ws.iter_rows():
                for c in row:
                    v = c.value
                    key = f"{ws.title}!{c.coordinate}"
                    fmt = c.number_format or ""
                    if v is not None and (fmt.strip() == ";;;" or (font_rgb(c) and font_rgb(c) == fill_rgb(c))):
                        self.add("INVISIBLE_VALUE", ws.title, c.coordinate, f"value {str(v)[:30]!r} not visible")
                    if is_formula(v):
                        if convention:
                            col = font_rgb(c)
                            if col == "0000FF":
                                self.add("FORMULA_COLORED_AS_INPUT", ws.title, c.coordinate, v[:60])
                            elif col not in ("008000", "00B050") and self._only_link(v) and \
                                    any(sh and sh != ws.title for sh, _ in X.iter_formula_refs(v)):
                                self.add("LINK_NOT_GREEN", ws.title, c.coordinate, v[:60])
                        continue
                    if not isinstance(v, (int, float)) or isinstance(v, bool) or c.row in hdr or c.column == 1:
                        continue
                    if "%" in fmt and 1.5 < abs(v) <= 100 and round(v, 2) == v:
                        self.add("PERCENT_AS_WHOLE_NUMBER", ws.title, c.coordinate, f"{v} formatted as %")
                    if convention and font_rgb(c) != "0000FF":
                        self.add("INPUT_NOT_BLUE", ws.title, c.coordinate, f"typed {v!r}")
                    is_input_cell = (font_rgb(c) == "0000FF") if convention else \
                        bool(re.search(r"input|assumption|driver", ws.title, re.I))
                    if key not in self.dep and is_input_cell:
                        self.add("UNUSED_INPUT", ws.title, c.coordinate, f"{v!r} ('{label_of(ws, c.row)}') is read by no formula")
                    elif convention and font_rgb(c) == "0000FF" and not self._has_source(ws, c):
                        self.add("MISSING_SOURCE", ws.title, c.coordinate, f"'{label_of(ws, c.row)}' = {v!r}")

    @staticmethod
    def _only_link(f):
        toks = [t for t in tokens(f) if t.type != "WHITE-SPACE"]
        return len(toks) == 1 and toks[0].subtype == "RANGE"

    @staticmethod
    def _has_source(ws, c):
        if c.comment is not None and c.comment.text.strip():
            return True
        for col in range(c.column + 1, ws.max_column + 1):
            v = ws.cell(c.row, col).value
            if isinstance(v, str) and not is_formula(v) and len(v.strip()) > 3:
                return True
        # a time-series input row is sourced once, on its first cell or its row note
        for col in range(2, c.column):
            cc = ws.cell(c.row, col)
            if cc.comment is not None and cc.comment.text.strip():
                return True
        return False

    def circularity(self):
        color, cycles = {}, []
        sys.setrecursionlimit(100000)

        def dfs(u, stack):
            color[u] = 1
            stack.append(u)
            for v in self.prec.get(u, ()):
                if color.get(v) == 1:
                    cycles.append(stack[stack.index(v):] + [v])
                elif color.get(v) is None and v in self.prec:
                    dfs(v, stack)
            stack.pop()
            color[u] = 2

        for u in list(self.prec):
            if color.get(u) is None:
                dfs(u, [])
        for cyc in cycles[:10]:
            sh, a = cyc[0].split("!", 1)
            self.add("CIRCULAR_REFERENCE", sh, a, " -> ".join(cyc)[:300])

    # ---------------------------------------------------------------- run / report
    def run(self, suppress=None):
        self.build_graph()
        self.workbook_checks()
        self.error_checks()
        self.formula_checks()
        self.layout_checks()
        self.input_checks()
        self.circularity()
        sup = set()
        for s in suppress or []:
            sup.add((s["id"], s.get("sheet", ""), s.get("cell", "")))
        self.suppressed = [f for f in self.findings if (f["id"], f["sheet"], f["cell"]) in sup]
        self.findings = [f for f in self.findings if (f["id"], f["sheet"], f["cell"]) not in sup]
        self.findings.sort(key=lambda f: (-SEV_RANK[f["severity"]], f["id"], f["sheet"], f["cell"]))
        return self.findings

    def summary(self):
        by_sev = Counter(f["severity"] for f in self.findings)
        rating = "Major Issues" if by_sev["high"] else "Minor Issues" if by_sev["medium"] else "Clean"
        return {"rating": rating, "by_severity": dict(by_sev), "by_rule": dict(Counter(f["id"] for f in self.findings)),
                "suppressed": len(getattr(self, "suppressed", []))}

    def markdown(self, limit_per_rule=8):
        s = self.summary()
        lines = [f"# Audit: {Path(self.path).name}", "",
                 f"**{s['rating']}**: " + ", ".join(f"{k} {v}" for k, v in sorted(s["by_severity"].items(), key=lambda kv: -SEV_RANK[kv[0]])), "",
                 "| # | Sheet | Cell | Severity | Rule | Issue | Fix |", "|---|---|---|---|---|---|---|"]
        shown = Counter()
        i = 0
        for f in self.findings:
            shown[f["id"]] += 1
            if shown[f["id"]] > limit_per_rule:
                continue
            i += 1
            issue = f["issue"].replace("|", "/")
            lines.append(f"| {i} | {f['sheet']} | {f['cell']} | {f['severity']} | {f['id']} ({f['confidence']}, {f['mode']}) | {issue} | {f['fix']} |")
        more = {k: n - limit_per_rule for k, n in shown.items() if n > limit_per_rule}
        if more:
            lines += ["", "Not listed (over the per-rule limit): " + ", ".join(f"{k} +{n}" for k, n in more.items())]
        return "\n".join(lines)

    def annotate(self, out):
        """REVIEW copy: comment + amber fill on every finding cell. Written with openpyxl,
        so it is for reading only; never deliver it as the model."""
        from openpyxl.comments import Comment
        from openpyxl.styles import PatternFill
        wb = load_workbook(self.path)
        fill = {"high": "F8CBAD", "medium": "FFE699", "low": "DDEBF7", "info": "EDEDED"}
        notes = defaultdict(list)
        for f in self.findings:
            if f["sheet"] and f["cell"] and f["sheet"] in wb.sheetnames:
                notes[(f["sheet"], f["cell"])].append(f)
        for (sh, cell), fs in notes.items():
            c = wb[sh][cell]
            top = max(fs, key=lambda f: SEV_RANK[f["severity"]])
            c.fill = PatternFill("solid", fgColor=fill[top["severity"]])
            c.comment = Comment("\n".join(f"[{f['severity']}] {f['id']}: {f['issue']}. Fix: {f['fix']}" for f in fs)[:2000], "xl audit")
        ws = wb.create_sheet("AUDIT", 0)
        ws.append(["REVIEW COPY written by xl.py audit; not the model. Rating:", self.summary()["rating"]])
        ws.append(["Sheet", "Cell", "Severity", "Rule", "Confidence", "Mode", "Issue", "Fix"])
        for f in self.findings:
            ws.append([f["sheet"], f["cell"], f["severity"], f["id"], f["confidence"], f["mode"], f["issue"], f["fix"]])
        wb.save(out)
        return out


def main(a):
    sup = json.loads(Path(a.suppress).read_text()) if getattr(a, "suppress", None) else None
    au = Auditor(a.file)
    au.run(sup)
    if getattr(a, "sheet", None):
        au.findings = [f for f in au.findings if f["sheet"] in (a.sheet, "")]
    if a.format == "md":
        print(au.markdown())
    else:
        print(json.dumps({"file": a.file, "summary": au.summary(), "findings": au.findings[: a.limit]}, indent=1, default=str))
    if getattr(a, "annotate", None):
        print(f"annotated review copy: {au.annotate(a.annotate)}", file=sys.stderr)
    if a.fail_on:
        if any(SEV_RANK[f["severity"]] >= SEV_RANK[a.fail_on] for f in au.findings):
            sys.exit(2)
