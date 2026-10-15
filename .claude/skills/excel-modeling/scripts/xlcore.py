"""Core helpers for surgical .xlsx work: package I/O, reference math, recalculation.

Why this exists: openpyxl rewrites the whole workbook on save. It drops sparklines,
dynamic-array metadata and every cached formula value, and rewrites charts. LibreOffice
re-saves change styles and break structured references. Editing the sheet XML in place
touches only the cells you change, so everything else in the file survives byte for byte.

Everything here is pure Python plus lxml (which keeps namespace prefixes intact; the
stdlib ElementTree renames them to ns0:, which breaks mc:Ignorable and makes Excel
"repair" the file).
"""
import os
import re
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

from lxml import etree
from openpyxl.formula.tokenizer import Tokenizer
from openpyxl.formula.translate import Translator
from openpyxl.utils import column_index_from_string as col2i, get_column_letter as i2col

NS = {
    "m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "pr": "http://schemas.openxmlformats.org/package/2006/relationships",
    "ct": "http://schemas.openxmlformats.org/package/2006/content-types",
    "c": "http://schemas.openxmlformats.org/drawingml/2006/chart",
    "xdr": "http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing",
    "xm": "http://schemas.microsoft.com/office/excel/2006/main",
}
M = "{%s}" % NS["m"]

CELL_RE = re.compile(r"^(\$?)([A-Z]{1,3})(\$?)(\d+)$")
COL_RE = re.compile(r"^(\$?)([A-Z]{1,3})$")
ROW_RE = re.compile(r"^(\$?)(\d+)$")


# ----------------------------------------------------------------------------- package

class Package:
    """An .xlsx opened as a zip of XML parts. Parts are parsed lazily and written back
    only if marked dirty, so untouched parts keep their exact original bytes."""

    def __init__(self, path):
        self.path = Path(path)
        with zipfile.ZipFile(self.path) as z:
            self.infos = z.infolist()
            self.raw = {i.filename: z.read(i.filename) for i in self.infos}
        self.trees, self.dirty, self.removed = {}, set(), set()
        self._sheets = None

    def names(self):
        return [n for n in self.raw if n not in self.removed]

    def xml(self, part):
        if part not in self.trees:
            parser = etree.XMLParser(remove_blank_text=False, huge_tree=True)
            self.trees[part] = etree.fromstring(self.raw[part], parser)
        return self.trees[part]

    def touch(self, part):
        self.dirty.add(part)

    def remove(self, part):
        self.removed.add(part)

    def rels_path(self, part):
        d, b = os.path.split(part)
        return f"{d}/_rels/{b}.rels"

    def rels(self, part):
        """{rId: (type_suffix, absolute_target)} for a part."""
        rp = self.rels_path(part)
        if rp not in self.raw or rp in self.removed:
            return {}
        out = {}
        base = os.path.dirname(part)
        for rel in self.xml(rp).findall("pr:Relationship", NS):
            tgt = rel.get("Target")
            if rel.get("TargetMode") == "External":
                full = tgt
            elif tgt.startswith("/"):
                full = tgt.lstrip("/")
            else:
                full = os.path.normpath(os.path.join(base, tgt)).replace("\\", "/")
            out[rel.get("Id")] = (rel.get("Type").rsplit("/", 1)[-1], full)
        return out

    def sheets(self):
        """Ordered list of (sheet_name, part_path, state)."""
        if self._sheets is None:
            wb = self.xml("xl/workbook.xml")
            rels = self.rels("xl/workbook.xml")
            self._sheets = []
            for s in wb.find("m:sheets", NS):
                rid = s.get("{%s}id" % NS["r"])
                self._sheets.append((s.get("name"), rels[rid][1], s.get("state", "visible")))
        return self._sheets

    def sheet_part(self, name):
        for n, p, _ in self.sheets():
            if n == name:
                return p
        raise KeyError(f"no sheet named {name!r}; sheets are {[s[0] for s in self.sheets()]}")

    def save(self, out=None):
        out = Path(out or self.path)
        tmp = out.with_suffix(out.suffix + ".tmp")
        with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
            for info in self.infos:
                n = info.filename
                if n in self.removed:
                    continue
                if n in self.dirty:
                    data = etree.tostring(self.trees[n], xml_declaration=True, encoding="UTF-8", standalone=True)
                else:
                    data = self.raw[n]
                zi = zipfile.ZipInfo(n, date_time=info.date_time)
                zi.compress_type = zipfile.ZIP_DEFLATED
                zi.external_attr = info.external_attr
                z.writestr(zi, data)
        os.replace(tmp, out)
        return out

    # -- workbook-level housekeeping needed after any formula edit

    def drop_calc_chain(self):
        """calcChain.xml lists formula cells in calc order. A stale chain (a formula
        added, removed or moved) makes Excel report 'unreadable content' and repair the
        file. Excel rebuilds the chain silently when it is absent, so remove it."""
        part = "xl/calcChain.xml"
        if part not in self.raw or part in self.removed:
            return False
        self.remove(part)
        ct = self.xml("[Content_Types].xml")
        for o in ct.findall("ct:Override", NS):
            if o.get("PartName") == "/" + part:
                ct.remove(o)
        self.touch("[Content_Types].xml")
        rp = "xl/_rels/workbook.xml.rels"
        rr = self.xml(rp)
        for rel in rr.findall("pr:Relationship", NS):
            if rel.get("Target", "").endswith("calcChain.xml"):
                rr.remove(rel)
        self.touch(rp)
        return True

    def force_full_calc(self, iterate=None):
        """Set fullCalcOnLoad so Excel recalculates every formula on open (stale cached
        values never reach the reader). Optionally switch iterative calc on/off."""
        wb = self.xml("xl/workbook.xml")
        cp = wb.find("m:calcPr", NS)
        if cp is None:
            cp = etree.SubElement(wb, M + "calcPr")
            # calcPr must come after definedNames / before oleSize etc.; move it right after
            # definedNames or sheets to respect the schema order.
            anchor = wb.find("m:definedNames", NS)
            if anchor is None:
                anchor = wb.find("m:sheets", NS)
            anchor.addnext(cp)
        cp.set("fullCalcOnLoad", "1")
        if iterate is not None:
            cp.set("iterate", "1" if iterate else "0")
            if iterate:
                cp.set("iterateCount", cp.get("iterateCount", "100"))
                cp.set("iterateDelta", cp.get("iterateDelta", "0.001"))
        self.touch("xl/workbook.xml")


# ----------------------------------------------------------------------------- cells in sheet XML

def split_cell(ref):
    m = CELL_RE.match(ref)
    if not m:
        raise ValueError(f"not a cell reference: {ref}")
    return col2i(m.group(2)), int(m.group(4))


def sheet_data(root):
    return root.find("m:sheetData", NS)


def find_row(root, r, create=False):
    sd = sheet_data(root)
    prev = None
    for row in sd.findall("m:row", NS):
        rr = int(row.get("r"))
        if rr == r:
            return row
        if rr > r:
            break
        prev = row
    if not create:
        return None
    new = etree.Element(M + "row")
    new.set("r", str(r))
    if prev is None:
        sd.insert(0, new)
    else:
        prev.addnext(new)
    return new


def find_cell(root, ref, create=False):
    c, r = split_cell(ref)
    row = find_row(root, r, create)
    if row is None:
        return None
    prev = None
    for cell in row.findall("m:c", NS):
        cc, _ = split_cell(cell.get("r"))
        if cc == c:
            return cell
        if cc > c:
            break
        prev = cell
    if not create:
        return None
    new = etree.Element(M + "c")
    new.set("r", ref)
    if prev is None:
        row.insert(0, new)
    else:
        prev.addnext(new)
    # keep the row's spans hint valid (it is optional; dropping it is always legal)
    row.attrib.pop("spans", None)
    return new


def iter_cells(root):
    sd = sheet_data(root)
    for row in sd.findall("m:row", NS):
        for cell in row.findall("m:c", NS):
            yield cell


def clear_cell_content(cell):
    for tag in ("f", "v", "is"):
        for el in cell.findall("m:" + tag, NS):
            cell.remove(el)
    cell.attrib.pop("t", None)
    cell.attrib.pop("cm", None)   # dynamic-array cell metadata pointer
    cell.attrib.pop("vm", None)


def set_cell(cell, value=None, formula=None):
    """Write a literal or a formula into a <c> element, keeping its style (s)."""
    clear_cell_content(cell)
    if formula is not None:
        f = etree.SubElement(cell, M + "f")
        f.text = formula[1:] if formula.startswith("=") else formula
        return
    if value is None:
        return
    if isinstance(value, bool):
        cell.set("t", "b")
        etree.SubElement(cell, M + "v").text = "1" if value else "0"
    elif isinstance(value, (int, float)):
        etree.SubElement(cell, M + "v").text = repr(float(value)) if isinstance(value, float) else str(value)
    else:
        # inline strings avoid touching sharedStrings.xml (and its count/uniqueCount)
        cell.set("t", "inlineStr")
        is_ = etree.SubElement(cell, M + "is")
        t = etree.SubElement(is_, M + "t")
        t.text = str(value)
        if str(value) != str(value).strip():
            t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")


def expand_shared_formulas(root, only_si=None):
    """Replace shared formulas (<f t="shared" si=".." ref="..">) by explicit per-cell
    formulas. Required before editing a shared master cell or shifting rows, otherwise
    the dependents silently follow the edited master or point at the wrong rows."""
    masters = {}
    for cell in iter_cells(root):
        f = cell.find("m:f", NS)
        if f is not None and f.get("t") == "shared" and f.get("ref") and f.text:
            masters[f.get("si")] = (cell.get("r"), "=" + f.text)
    n = 0
    for cell in iter_cells(root):
        f = cell.find("m:f", NS)
        if f is None or f.get("t") != "shared":
            continue
        si = f.get("si")
        if only_si is not None and si != only_si:
            continue
        origin, text = masters[si]
        f.text = Translator(text, origin=origin).translate_formula(cell.get("r"))[1:]
        for a in ("t", "si", "ref"):
            f.attrib.pop(a, None)
        n += 1
    return n


# ----------------------------------------------------------------------------- reference parsing

def split_sheet(operand):
    """'Model Calc'!B2:F2 -> ("Model Calc", "B2:F2"); B2 -> (None, "B2")."""
    if "!" not in operand:
        return None, operand
    i = operand.rfind("!")
    sh, addr = operand[:i], operand[i + 1:]
    if sh.startswith("'") and sh.endswith("'"):
        sh = sh[1:-1].replace("''", "'")
    return sh, addr


def quote_sheet(name):
    if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_.]*", name) and not CELL_RE.match(name.upper()):
        return name
    return "'" + name.replace("'", "''") + "'"


def iter_formula_refs(formula):
    """Yield (sheet_or_None, address) for every range operand in a formula."""
    if not formula or not formula.startswith("="):
        return
    try:
        toks = Tokenizer(formula).items
    except Exception:
        return
    for t in toks:
        if t.type == "OPERAND" and t.subtype == "RANGE":
            yield split_sheet(t.value)


def shift_address(addr, axis, at, n):
    """Shift one address part (A1, A1:B9, A:A, 3:7) for an insertion of n rows/cols
    before index `at`. Returns new string (unchanged if not affected)."""
    parts = addr.split(":")
    if len(parts) > 2:
        return addr
    out = []
    for p in parts:
        m = CELL_RE.match(p)
        if m:
            d1, col, d2, row = m.groups()
            ci, ri = col2i(col), int(row)
            if axis == "row" and ri >= at:
                ri += n
            if axis == "col" and ci >= at:
                ci += n
            out.append(f"{d1}{i2col(ci)}{d2}{ri}")
            continue
        m = ROW_RE.match(p)
        if m and axis == "row":
            ri = int(m.group(2))
            out.append(f"{m.group(1)}{ri + n if ri >= at else ri}")
            continue
        m = COL_RE.match(p)
        if m and axis == "col":
            ci = col2i(m.group(2))
            out.append(f"{m.group(1)}{i2col(ci + n if ci >= at else ci)}")
            continue
        out.append(p)
    return ":".join(out)


def shift_formula(formula, home_sheet, target_sheet, axis, at, n):
    """Rewrite every reference into target_sheet inside formula (which lives on
    home_sheet) for an insertion. Text literals and names are untouched."""
    if not formula:
        return formula
    lead = formula.startswith("=")
    f = formula if lead else "=" + formula
    try:
        tok = Tokenizer(f)
    except Exception:
        return formula
    changed = False
    for t in tok.items:
        if t.type == "OPERAND" and t.subtype == "RANGE":
            sh, addr = split_sheet(t.value)
            if "[" in (sh or "") or "[" in addr:
                continue   # external workbook refs and structured refs are left alone
            if (sh or home_sheet) != target_sheet:
                continue
            new = shift_address(addr, axis, at, n)
            if new != addr:
                prefix = t.value[: len(t.value) - len(addr)]
                t.value = prefix + new
                changed = True
    if not changed:
        return formula
    out = tok.render()
    return out if lead else out[1:]


def shift_sqref(sqref, axis, at, n, extend_adjacent=False):
    """Shift a space-separated list of ranges. extend_adjacent mimics Excel's
    'format same as left/above': a formatting range (conditional format, validation)
    that ends right before the insertion point grows into the new lines."""
    out = []
    for a in sqref.split():
        new = shift_address(a, axis, at, n)
        if extend_adjacent and new == a and ":" in a:
            first, last = a.split(":")
            m = CELL_RE.match(last)
            if m:
                d1, col, d2, row = m.groups()
                if axis == "row" and int(row) == at - 1:
                    new = f"{first}:{d1}{col}{d2}{int(row) + n}"
                if axis == "col" and col2i(col) == at - 1:
                    new = f"{first}:{d1}{i2col(col2i(col) + n)}{d2}{row}"
        out.append(new)
    return " ".join(out)


def relative_form(formula, origin):
    """Normalise a formula to an R1C1-like string relative to its own cell, so formulas
    that are 'the same' across a row compare equal. Used by the consistency audit."""
    oc, orow = split_cell(origin)
    try:
        tok = Tokenizer(formula)
    except Exception:
        return formula
    parts = []
    for t in tok.items:
        if t.type == "OPERAND" and t.subtype == "RANGE":
            sh, addr = split_sheet(t.value)
            segs = []
            for p in addr.split(":"):
                m = CELL_RE.match(p)
                if m:
                    d1, col, d2, row = m.groups()
                    cpart = f"C{col2i(col)}" if d1 else f"C[{col2i(col) - oc}]"
                    rpart = f"R{row}" if d2 else f"R[{int(row) - orow}]"
                    segs.append(rpart + cpart)
                else:
                    segs.append(p)
            parts.append((f"{sh}!" if sh else "") + ":".join(segs))
        else:
            parts.append(t.value)
    return "".join(parts)


# ----------------------------------------------------------------------------- recalculation

RECALC_XCU = """<?xml version="1.0" encoding="UTF-8"?>
<oor:items xmlns:oor="http://openoffice.org/2001/registry" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<item oor:path="/org.openoffice.Office.Calc/Formula/Load"><prop oor:name="OOXMLRecalcMode" oor:op="fuse"><value>0</value></prop></item>
<item oor:path="/org.openoffice.Office.Calc/Formula/Load"><prop oor:name="ODFRecalcMode" oor:op="fuse"><value>0</value></prop></item>
</oor:items>
"""


def lo_recalc_copy(src, out_dir=None, timeout=120):
    """Recalculate a COPY of src with headless LibreOffice and return the copy's path.
    The source file is never modified: LibreOffice re-saves restyle the workbook, so its
    output is used for reading values only, never delivered."""
    src = Path(src).resolve()
    work = Path(tempfile.mkdtemp(prefix="xlrecalc_"))
    prof = work / "profile"
    (prof / "user").mkdir(parents=True)
    (prof / "user" / "registrymodifications.xcu").write_text(RECALC_XCU)
    inp = work / ("in_" + src.name)
    shutil.copy(src, inp)
    outd = Path(out_dir) if out_dir else work / "out"
    outd.mkdir(parents=True, exist_ok=True)
    cmd = ["soffice", f"-env:UserInstallation={prof.as_uri()}", "--headless", "--norestore",
           "--convert-to", "xlsx:Calc MS Excel 2007 XML", "--outdir", str(outd), str(inp)]
    subprocess.run(cmd, capture_output=True, timeout=timeout, check=False)
    out = outd / inp.name
    if not out.exists():
        raise RuntimeError("LibreOffice did not produce a recalculated copy")
    return out


# ----------------------------------------------------------------------------- live LibreOffice session (UNO)

class LOSession:
    """Drive a hidden LibreOffice instance over UNO: open a workbook once, then set inputs,
    recalculate and read outputs many times (sensitivity grids, goal seek checks, and the
    insert-rows oracle used by the tests). Never store the document over the original."""

    def __init__(self, path):
        self.path = os.path.abspath(path)

    def __enter__(self):
        import time
        import uno  # system python3 ships LibreOffice's UNO bridge
        from com.sun.star.beans import PropertyValue
        self._uno, self._PV = uno, PropertyValue
        self.prof = tempfile.mkdtemp(prefix="lo_uno_")
        port = 2100 + os.getpid() % 2000
        self.proc = subprocess.Popen(
            ["soffice", f"-env:UserInstallation=file://{self.prof}", "--headless", "--norestore",
             f"--accept=socket,host=localhost,port={port};urp;"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        local = uno.getComponentContext()
        res = local.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local)
        ctx = None
        for _ in range(80):
            try:
                ctx = res.resolve(f"uno:socket,host=localhost,port={port};urp;StarOffice.ComponentContext")
                break
            except Exception:
                time.sleep(0.25)
        if ctx is None:
            self.proc.kill()
            raise RuntimeError("could not connect to LibreOffice")
        desk = ctx.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
        self.doc = desk.loadComponentFromURL(uno.systemPathToFileUrl(self.path), "_blank", 0, (self._prop("Hidden", True),))
        self.doc.calculateAll()
        return self

    def _prop(self, n, v):
        p = self._PV()
        p.Name, p.Value = n, v
        return p

    def _cell(self, spec):
        sh, addr = split_sheet(spec)
        c, r = split_cell(addr.replace("$", ""))
        return self.doc.Sheets.getByName(sh).getCellByPosition(c - 1, r - 1)

    def get(self, spec):
        cell = self._cell(spec)
        if cell.getError():
            return f"#ERR{cell.getError()}"
        t = cell.getType().value
        return cell.getString() if t == "TEXT" else cell.getValue()

    def set(self, spec, value):
        cell = self._cell(spec)
        if isinstance(value, str) and value.startswith("="):
            cell.setFormula(value)
        elif isinstance(value, str):
            cell.setString(value)
        else:
            cell.setValue(float(value))

    def recalc(self):
        self.doc.calculateAll()

    def __exit__(self, *exc):
        try:
            self.doc.close(True)
        finally:
            self.proc.terminate()
            self.proc.wait()
            shutil.rmtree(self.prof, ignore_errors=True)
