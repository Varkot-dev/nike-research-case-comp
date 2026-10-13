"""Markdown tables for AE_BASERATES.md. Usage: python3 -I make_tables.py OUTDIR"""
import sys, os, csv
OUT = sys.argv[1]
rows = list(csv.DictReader(open(os.path.join(OUT, "episodes_core.csv"))))
allr = list(csv.DictReader(open(os.path.join(OUT, "episodes_all.csv"))))
def f(x):
    try: return float(x)
    except Exception: return None
def pct(x): v = f(x); return "" if v is None else "%+.0f%%" % (100 * v)
def mult(x, d=2):
    v = f(x)
    if v is None or v <= 0 or v > 100: return "n/a"
    return ("%." + str(d) + "f") % v
o = []
o.append("| # | Ticker | Peak | Trough | Max DD | E75 date | Regime | EV/S E75 | EV/EBITDA E75 | EV/S trough | E75 +1y | E75 +2y | E75 +3y | E75 +3y vs S&P | E80 +1y | E80 +3y | Outcome |")
o.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
rows.sort(key=lambda r: (r["regime"] != "idiosyncratic", r["e75_date"]))
for i, r in enumerate(rows, 1):
    o.append("| %d | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
        i, r["ticker"], r["peak_date"], r["trough_date"], pct(r["max_drawdown"]), r["e75_date"],
        "idio" if r["regime"] == "idiosyncratic" else "market", mult(r.get("e75_ev_sales")), mult(r.get("e75_ev_ebitda"), 1),
        mult(r.get("trough_ev_sales")), pct(r["e75_fwd1y"]), pct(r["e75_fwd2y"]), pct(r["e75_fwd3y"]), pct(r["e75_xs3y"]),
        pct(r["e80_fwd1y"]), pct(r["e80_fwd3y"]), r["outcome_e75"].replace("_", " ")))
open(os.path.join(OUT, "table_core.md"), "w").write("\n".join(o))
ex = {}
for r in allr:
    if r["exclusion"]:
        ex.setdefault(r["exclusion"], []).append(f'{r["ticker"]} {r["peak_date"][:4]} ({pct(r["max_drawdown"])})')
e = []
for k, v in ex.items():
    e.append(f"- {k} ({len(v)}): " + ", ".join(v))
open(os.path.join(OUT, "table_excluded.md"), "w").write("\n".join(e))
print(len(rows), "core rows;", sum(len(v) for v in ex.values()), "excluded")
