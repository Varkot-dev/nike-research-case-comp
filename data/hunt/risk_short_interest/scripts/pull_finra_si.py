"""Pull FINRA consolidated short interest (twice-monthly) for a list of tickers.
Source: https://api.finra.org/data/group/otcMarket/name/consolidatedShortInterest (free, no key).
Writes raw/si_<TICKER>.json and si_all.csv (ticker, settlement_date, short_shares, adv, dtc).
"""
import json, subprocess, sys, csv, pathlib
HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"; RAW.mkdir(exist_ok=True)
TICKERS = sys.argv[1:] or ["NKE"]
URL = "https://api.finra.org/data/group/otcMarket/name/consolidatedShortInterest"
rows = []
for t in TICKERS:
    out = RAW / f"si_{t}.json"
    if not out.exists():
        body = json.dumps({"limit": 5000, "compareFilters": [{"compareType": "equal", "fieldName": "symbolCode", "fieldValue": t}]})
        subprocess.run(["curl", "-sS", "-X", "POST", URL, "-H", "Content-Type: application/json", "-H", "Accept: application/json", "-d", body, "-o", str(out)], check=True)
    try:
        d = json.load(open(out))
    except Exception:
        print("fail", t); continue
    seen = {}
    for r in d:
        if r.get("symbolCode") != t: continue
        seen[r["settlementDate"]] = r  # last revision wins
    for k in sorted(seen):
        r = seen[k]
        rows.append([t, k, r["currentShortPositionQuantity"], r["averageDailyVolumeQuantity"], r["daysToCoverQuantity"]])
    print(t, len(seen), min(seen) if seen else None, max(seen) if seen else None)
mode = "a" if (HERE / "si_all.csv").exists() else "w"
with open(HERE / "si_all.csv", mode, newline="") as f:
    w = csv.writer(f)
    if mode == "w": w.writerow(["ticker", "settlement_date", "short_shares", "finra_adv", "finra_days_to_cover"])
    w.writerows(rows)
