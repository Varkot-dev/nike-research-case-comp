"""End-to-end tests for scripts/xl.py. Run: python3 tests/test_xl.py  (needs LibreOffice)

1. insert_rows / insert_cols: every formula, defined name, chart series, CF and DV range
   must match what LibreOffice's own insert produces (the oracle), on several sheets/positions.
2. patch: editing a shared-formula master keeps its dependents' formulas.
3. fidelity: sparkline, chart, DV, CF, comment survive a patch byte-for-byte where untouched.
4. refresh-cache: pandas reads the recalculated numbers without opening Excel.
"""
import json, os, re, shutil, subprocess, sys, tempfile, warnings, zipfile
warnings.filterwarnings("ignore")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "scripts"))
import xl, xlcore as X
from make_fixture import build
from openpyxl import load_workbook

W = tempfile.mkdtemp(prefix="xltest_")
FX = os.path.join(W, "fixture.xlsx")
build(FX)
fails = []

def check(cond, msg):
    print(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        fails.append(msg)

def norm(f):
    return re.sub(r"\s+", "", str(f)).upper() if f is not None else None

def formulas(path):
    wb = load_workbook(path)
    out = {}
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str) and c.value.startswith("="):
                    out[f"{ws.title}!{c.coordinate}"] = norm(c.value)
        for cf in ws.conditional_formatting:
            out[f"{ws.title}!CF"] = str(cf.sqref)
        for dv in ws.data_validations.dataValidation:
            out[f"{ws.title}!DV"] = str(dv.sqref)
    for n, d in wb.defined_names.items():
        out[f"name:{n}"] = norm(d.attr_text)
    return out

def chart_refs(path):
    z = zipfile.ZipFile(path)
    return sorted(norm(m) for n in z.namelist() if n.startswith("xl/charts/chart")
                  for m in re.findall(r"<c:f>([^<]+)</c:f>", z.read(n).decode())
                  if not m.startswith("&quot;"))  # LibreOffice writes series names as literal "<c:f>"name"

def values(path):
    rc = X.lo_recalc_copy(path)
    wb = load_workbook(rc, data_only=True)
    return {f"{ws.title}!{c.coordinate}": c.value for ws in wb.worksheets for row in ws.iter_rows() for c in row if c.value is not None}

cases = [("Model", "row", 6, 1), ("Model", "row", 7, 2), ("Model", "row", 2, 1), ("Model", "col", 3, 1),
         ("Inputs", "row", 3, 1), ("Model", "col", 7, 1)]
for sheet, axis, at, n in cases:
    tag = f"{sheet}-{axis}{at}x{n}"
    mine, oracle = os.path.join(W, f"mine_{tag}.xlsx"), os.path.join(W, f"oracle_{tag}.xlsx")
    p = xl.Patcher(FX)
    p.apply([{"op": "insert_rows" if axis == "row" else "insert_cols", "sheet": sheet, "at": at, "n": n}])
    p.pkg.save(mine)
    subprocess.run([sys.executable, os.path.join(HERE, "lo_oracle.py"), FX, oracle, sheet, axis, str(at), str(n)], check=True, timeout=180)
    fm, fo = formulas(mine), formulas(oracle)
    diff = {k: (fm.get(k), fo.get(k)) for k in set(fm) | set(fo) if fm.get(k) != fo.get(k)}
    check(not diff, f"{tag}: formulas/names/CF/DV match LibreOffice insert" + (f" DIFF {list(diff.items())[:4]}" if diff else ""))
    cm, co = chart_refs(mine), chart_refs(oracle)
    check(cm == co, f"{tag}: chart series refs match ({cm} vs {co})" if cm != co else f"{tag}: chart series refs match")
    vm, vo = values(mine), values(oracle)
    bad = [k for k in vo if isinstance(vo[k], (int, float)) and not xl._close(vm.get(k), vo[k])]
    check(not bad, f"{tag}: recalculated values match" + (f" {bad[:4]}" if bad else ""))

# shared-formula master edit
out = os.path.join(W, "shared.xlsx")
p = xl.Patcher(FX); p.apply([{"op": "set", "sheet": "Model", "cell": "C4", "formula": "=C2+C3"}]); p.pkg.save(out)
f = formulas(out)
check(f["Model!D4"] == "=D2+D3" and f["Model!F4"] == "=F2+F3", "editing a shared master keeps dependents (D4, F4)")

# fidelity: untouched parts byte-identical, features present
out = os.path.join(W, "fid.xlsx")
p = xl.Patcher(FX); p.apply([{"op": "set", "sheet": "Inputs", "cell": "B3", "value": 0.08}]); p.pkg.save(out)
za, zb = zipfile.ZipFile(FX), zipfile.ZipFile(out)
same = [n for n in za.namelist() if n in zb.namelist() and za.read(n) == zb.read(n)]
changed = sorted(set(za.namelist()) - set(same))
check(set(changed) <= {"xl/worksheets/sheet1.xml", "xl/workbook.xml"}, f"only the edited sheet and workbook.xml changed: {changed}")
check(b"sparklineGroup" in zb.read("xl/worksheets/sheet2.xml"), "sparkline survives patch")
v = values(out)
check(abs(v["Model!F2"] - 1000 * 1.08 ** 4) < 1e-6, f"growth input flows to FY2029 revenue ({v['Model!F2']})")

# refresh-cache
r = xl.verify(out)
xl.refresh_cache(out, r["recalculated_copy"])
import pandas as pd
df = pd.read_excel(out, sheet_name="Model", header=None)
check(abs(df.iloc[1, 5] - 1000 * 1.08 ** 4) < 1e-6, f"pandas reads refreshed cached value ({df.iloc[1, 5]})")

# fill
out = os.path.join(W, "fill.xlsx")
p = xl.Patcher(FX)
p.apply([{"op": "set", "sheet": "Model", "cell": "B12", "value": "Margin"},
         {"op": "set", "sheet": "Model", "cell": "B13", "formula": "=IF(B2=0,0,B7/B2)"},
         {"op": "fill", "sheet": "Model", "src": "B13", "range": "C13:F13"}])
p.pkg.save(out)
f = formulas(out)
check(f["Model!F13"] == "=IF(F2=0,0,F7/F2)", f"fill translates relative refs ({f['Model!F13']})")

print(f"\n{len(fails)} failure(s); work dir {W}")
sys.exit(1 if fails else 0)
