"""FINRA Reg SHO daily short sale volume (consolidated CNMS file) for chosen symbols.
Source: https://cdn.finra.org/equity/regsho/daily/CNMSshvolYYYYMMDD.txt (free). Note: this is short SALE volume
(includes market-maker and hedging shorts that are covered intraday), not short interest.
Writes daily_short_volume.csv."""
import subprocess, sys, csv, pathlib, datetime as dt
from concurrent.futures import ThreadPoolExecutor
H = pathlib.Path(__file__).resolve().parent.parent
SYMS = set(sys.argv[1:] or ["NKE"])
start, end = dt.date(2025, 10, 1), dt.date(2026, 10, 13)
days = [start + dt.timedelta(d) for d in range((end - start).days + 1)]
days = [d for d in days if d.weekday() < 5]
def get(d):
    u = f"https://cdn.finra.org/equity/regsho/daily/CNMSshvol{d:%Y%m%d}.txt"
    r = subprocess.run(["curl", "-sS", "-f", u], capture_output=True, text=True)
    return [l.split("|") for l in r.stdout.splitlines() if l.split("|")[1:2] and l.split("|")[1] in SYMS] if r.returncode == 0 else []
with ThreadPoolExecutor(8) as ex: res = list(ex.map(get, days))
rows = [x for L in res for x in L]
with open(H / "daily_short_volume.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["date", "symbol", "short_volume", "short_exempt_volume", "total_volume_finra_venues", "markets"])
    for x in rows: w.writerow([x[0], x[1], round(float(x[2])), round(float(x[3])), round(float(x[4])), x[5]])
print(len(rows))
