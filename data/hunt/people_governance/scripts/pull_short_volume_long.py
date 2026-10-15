"""FINRA Reg SHO daily short SALE volume (CNMS consolidated file), 2019-01-02 to 2025-09-30, to extend
data/hunt/risk_short_interest/daily_short_volume.csv (which covers 2025-10-01 to 2026-10-13).
Source: https://cdn.finra.org/equity/regsho/daily/CNMSshvolYYYYMMDD.txt. Usage: python3 -I pull_short_volume_long.py OUTDIR"""
import sys, csv, time, datetime as dt, urllib.request
from concurrent.futures import ThreadPoolExecutor
OUT = sys.argv[1]; SYMS = {'NKE', 'DECK', 'LULU', 'ONON', 'UAA', 'SPY', 'CROX', 'BIRK'}
s, e = dt.date(2019, 1, 2), dt.date(2025, 9, 30)
days = [s + dt.timedelta(i) for i in range((e - s).days + 1)]; days = [d for d in days if d.weekday() < 5]
def get(d):
    u = f"https://cdn.finra.org/equity/regsho/daily/CNMSshvol{d:%Y%m%d}.txt"
    for a in range(3):
        try:
            t = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0 (academic research script)'}), timeout=60).read().decode()
            return [l.split('|') for l in t.splitlines() if l.split('|')[1:2] and l.split('|')[1] in SYMS]
        except urllib.error.HTTPError as x:
            if x.code in (403, 404): return []
        except Exception: time.sleep(3)
    return []
with ThreadPoolExecutor(6) as ex: res = list(ex.map(get, days))
with open(f'{OUT}/raw/finra_short_volume_2019_2025.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['date', 'symbol', 'short_volume', 'short_exempt_volume', 'total_volume_finra_venues', 'markets'])
    n = 0
    for L in res:
        for x in L: w.writerow([x[0], x[1], round(float(x[2])), round(float(x[3])), round(float(x[4])), x[5]]); n += 1
print(n)
