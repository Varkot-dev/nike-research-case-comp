"""For named peers: date of the all-series maximum short interest (FINRA, 2017-12 to 2026-09) and the stock's excess
return vs SPY after the publication date (settle + 10 days), plus where the stock's 2-year low sits relative to the SI peak."""
import csv, bisect, collections, datetime as dt, pathlib
H = pathlib.Path(__file__).resolve().parent.parent
si = collections.defaultdict(list)
for r in csv.DictReader(open(H / "si_all.csv")): si[r["ticker"]].append((r["settlement_date"], int(r["short_shares"]), r["finra_days_to_cover"]))
px = collections.defaultdict(lambda: ([], []))
for r in csv.DictReader(open(H / "prices_all.csv")): px[r["ticker"]][0].append(r["date"]); px[r["ticker"]][1].append(float(r["adj_close"]))
SD, SA = px["SPY"]
print("ticker,si_peak_date,si_peak_m,dtc,close_adj_at_entry,xs_13,xs_63,xs_126,xs_252,days_from_si_peak_to_price_low_within_pm1y")
for t in ["NKE", "LULU", "VFC", "UAA", "TGT", "EL", "SBUX", "DECK", "CROX", "KSS"]:
    L = si[t]; d, s, dtc = max(L, key=lambda x: x[1])
    D, A = px[t]; e = (dt.date.fromisoformat(d) + dt.timedelta(days=10)).isoformat(); i = bisect.bisect_left(D, e); j = bisect.bisect_left(SD, D[i])
    xs = [round(100 * (A[i + h] / A[i] - SA[j + h] / SA[j]), 1) if i + h < len(D) else "" for h in (13, 63, 126, 252)]
    lo, hi = max(0, i - 252), min(len(A), i + 253); k = lo + min(range(hi - lo), key=lambda q: A[lo + q])
    print(f"{t},{d},{s/1e6:.1f},{dtc},{A[i]:.2f}," + ",".join(map(str, xs)) + f",{k - i}")
