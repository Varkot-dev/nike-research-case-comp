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

from test_xl_lib import norm, formulas, chart_refs, values

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

# audit: every planted defect is caught by the right rule, and nothing fires on the clean fixture's formulas
import audit
bad = os.path.join(W, "bad.xlsx")
p = xl.Patcher(FX)
p.apply([
    {"op": "set", "sheet": "Model", "cell": {"row": "SG&A", "col": "FY2027"}, "value": -300},      # pasted-over formula
    {"op": "set", "sheet": "Model", "cell": "E3", "formula": "=-E2*0.55"},                         # literal + inconsistent
    {"op": "set", "sheet": "Checks", "cell": "B3", "formula": "=XLOOKUP(1,Model!B1:F1,Model!B2:F2)"},  # bare new function
    {"op": "set", "sheet": "Checks", "cell": "B4", "formula": "=Model!B2/Model!B12"},              # #DIV/0! via blank
    {"op": "set", "sheet": "Checks", "cell": "B5", "formula": "=SUM(Model!B2:B3)+Model!B3"},       # double count
    {"op": "set", "sheet": "Checks", "cell": "B6", "formula": "=VLOOKUP(1,Model!B1:F2,2)"},        # approximate lookup
    {"op": "set", "sheet": "Checks", "cell": "B7", "formula": "=SUM(Inputs!B3:B4)"},               # stops short of like input B5
    {"op": "set", "sheet": "Inputs", "cell": "B8", "value": 7},                                    # unused input
    {"op": "style", "sheet": "Inputs", "range": "B8", "like": "B2"},
])
p.pkg.save(bad)
ids = {(f["id"], f["sheet"], f["cell"]) for f in audit.Auditor(bad).run()}
want = [("FORMULA_INTERRUPTED_BY_DATA", "Model", "D5"), ("INCONSISTENT_FORMULA", "Model", "E3"),
        ("LITERAL_IN_FORMULA", "Model", "E3"), ("NEEDS_XLFN_PREFIX", "Checks", "B3"),
        ("LIVE_ERROR_ROOT", "Checks", "B4"), ("REF_TO_BLANK", "Checks", "B4"), ("DOUBLE_COUNT", "Checks", "B5"),
        ("APPROXIMATE_LOOKUP", "Checks", "B6"), ("RANGE_STOPS_SHORT", "Checks", "B7"), ("UNUSED_INPUT", "Inputs", "B8")]
for w in want:
    check(w in ids, f"audit catches {w}")
clean = [f for f in audit.Auditor(FX).run() if f["id"] not in ("MISSING_SOURCE",)]
check(not clean, f"clean fixture has no formula findings ({[(f['id'], f['cell']) for f in clean][:5]})")
v = xl.verify(bad)
check(any("xlookup" in u for u in v["libreoffice_could_not_parse"]), "verify flags formulas LibreOffice could not parse")

# scenarios / sensitivity / tornado / crosscheck on the fixture
sc = xl.scenarios(FX, "Inputs!B3", [0.0, 0.05, 0.10], ["Model!F9"])
check(sc[0]["Model!F9"] < sc[1]["Model!F9"] < sc[2]["Model!F9"], "scenarios: net income rises with growth")
g = xl.sensitivity(FX, "Model!F9", "Inputs!B3", [0.0, 0.05, 0.1], "Inputs!B4", [0.5, 0.55, 0.6])
ga = xl.grid_assertions(g)
check(ga["pass"] and abs(g["grid"][0][0] - (1000 * (1 - 0.5 - 0.3) - 10) * 0.79) < 1e-6,
      f"sensitivity grid matches closed form and passes assertions ({g['grid'][0][0]}, {ga})")
t = xl.tornado(FX, "Model!F9", [("Inputs!B4", 0.5, 0.6), ("Inputs!B6", 0.2, 0.22)])
check(t["ranked"][0]["input"] == "Inputs!B4", "tornado ranks COGS above tax for net income")
cc = xl.crosscheck(FX)
check(cc["status"] in ("agree", "skipped"), f"second engine agrees with LibreOffice ({cc.get('status')}, {cc.get('compared')})")

print(f"\n{len(fails)} failure(s); work dir {W}")
sys.exit(1 if fails else 0)
