"""Compare xl.py insert_rows/insert_cols against LibreOffice's own insert on ANY workbook.
    python3 tests/oracle_compare.py book.xlsx "Sheet name" row 12 [n]
Prints formula/name/CF/DV/chart differences and recalculated value differences."""
import os, sys, subprocess, tempfile, warnings
warnings.filterwarnings("ignore")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "scripts")); sys.path.insert(0, HERE)
import xl
from test_xl_lib import formulas, chart_refs, values

src, sheet, axis, at = sys.argv[1:5]
n = int(sys.argv[5]) if len(sys.argv) > 5 else 1
at = int(at) if at.isdigit() else at
W = tempfile.mkdtemp(prefix="oracle_")
mine, oracle = os.path.join(W, "mine.xlsx"), os.path.join(W, "oracle.xlsx")
p = xl.Patcher(src); p.apply([{"op": f"insert_{axis}s", "sheet": sheet, "at": at, "n": n}]); p.pkg.save(mine)
from openpyxl.utils import column_index_from_string
subprocess.run([sys.executable, os.path.join(HERE, "lo_oracle.py"), src, oracle, sheet, axis,
                str(at if isinstance(at, int) else column_index_from_string(at)), str(n)], check=True, timeout=300)
fm, fo = formulas(mine), formulas(oracle)
d = [(k, fm.get(k), fo.get(k)) for k in sorted(set(fm) | set(fo)) if fm.get(k) != fo.get(k)]
print(f"formula-level cells compared: {len(fo)}; differences: {len(d)}")
for row in d[:25]:
    print("  ", row)
print("charts equal:", chart_refs(mine) == chart_refs(oracle))
vm, vo = values(mine), values(oracle)
bad = [(k, vm.get(k), vo[k]) for k in vo if isinstance(vo[k], (int, float)) and not xl._close(vm.get(k), vo[k])]
print(f"numeric values compared: {sum(isinstance(v,(int,float)) for v in vo.values())}; differences: {len(bad)}", bad[:10])
