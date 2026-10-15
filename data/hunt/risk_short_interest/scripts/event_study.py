"""Event study: what happens to US consumer large caps after short interest (shares) hits a record?
Inputs: si_all.csv (FINRA), prices_all.csv (Yahoo adj close, includes dividends, so a short's dividend cost is in the return),
shares_all.csv (SEC XBRL cover-page counts, single-class issuers), yahoo_keystats_2026-10-14.csv (fallback shares).
Event = settlement date where short shares exceed every prior FINRA print since 2017-12-29, with at least 3 years of prior data
(so events start 2021-01), and short interest >= MINPCT of shares outstanding.
Episode = first record print after >= 126 trading days with no record (non-overlapping starts).
Entry = first close on or after settlement + 10 calendar days (about FINRA's publication date), so no look-ahead.
Excess return = stock adj-close return minus SPY adj-close return. A short wins when excess < 0.
Outputs: events.csv, episodes.csv, summary printed."""
import csv, pathlib, bisect, datetime as dt, statistics as st, collections, sys
H = pathlib.Path(__file__).resolve().parent.parent
MINPCT = float(sys.argv[1]) if len(sys.argv) > 1 else 4.0
# Forward stock splits in the window (split-adjust earlier SI and share counts to post-split units)
SPLITS = {"CMG": ("2024-06-26", 50), "DECK": ("2024-09-17", 6), "WMT": ("2024-02-26", 3), "TSCO": ("2024-12-20", 5)}
adj = lambda t, d, x: x * SPLITS[t][1] if t in SPLITS and d < SPLITS[t][0] else x
si = collections.defaultdict(list)
for r in csv.DictReader(open(H / "si_all.csv")):
    t = "GAP" if r["ticker"] == "GPS" else r["ticker"]
    si[t].append((r["settlement_date"], adj(t, r["settlement_date"], int(r["short_shares"])), float(r["finra_days_to_cover"] or 0)))
px = collections.defaultdict(lambda: ([], []))
for r in csv.DictReader(open(H / "prices_all.csv")):
    d, a = px[r["ticker"]]; d.append(r["date"]); a.append(float(r["adj_close"]))
sh = collections.defaultdict(list)
for r in csv.DictReader(open(H / "shares_all.csv")):
    if r["n_classes"] == "1": sh[r["ticker"]].append((r["date"], adj(r["ticker"], r["date"], int(r["shares_total"]))))
# Nike: Class B counts from data/nike_filing_facts.csv (10-K / 10-Q covers)
for r in csv.DictReader(open(H.parent.parent / "nike_filing_facts.csv")):
    if r["metric"] == "class_b_shares_outstanding": sh["NKE"].append((r["period"], int(float(r["value"]))))
sh["NKE"] = sorted(x for x in sh["NKE"] if x[0] >= "2018")
if sh["NKE"]: sh["NKE"].insert(0, ("2017-01-01", 1272000000))  # FY18 balance sheet 1,272M (FY19 10-K p. 52)
ys = {r["ticker"]: float(r["sharesOutstanding"]) for r in csv.DictReader(open(H / "yahoo_keystats_2026-10-14.csv")) if r["sharesOutstanding"]}
def shares(t, d):
    L = sorted(sh.get(t, []))
    if len(L) >= 4:
        i = bisect.bisect_right([x[0] for x in L], d) - 1
        return L[max(i, 0)][1]
    return ys.get(t)
def idx(t, d):
    D = px[t][0]; return bisect.bisect_left(D, d)
H_ = [13, 21, 63, 126, 252]
spyD, spyA = px["SPY"]
events = []
for t, L in si.items():
    if t not in px or not px[t][0]: continue
    D, A = px[t]
    L.sort(); runmax = 0
    for k, (d, s, dtc) in enumerate(L):
        rec = s > runmax and d >= "2021-01-01"
        runmax = max(runmax, s)
        if not rec: continue
        so = shares(t, d)
        pct = 100 * s / so if so else None
        if pct is None or pct < MINPCT: continue
        e = (dt.date.fromisoformat(d) + dt.timedelta(days=10)).isoformat()
        i = idx(t, e); j = bisect.bisect_left(spyD, D[i]) if i < len(D) else None
        if i >= len(D): continue
        # drawdown from 3-year high at entry
        lo = bisect.bisect_left(D, (dt.date.fromisoformat(D[i]) - dt.timedelta(days=1095)).isoformat())
        dd = A[i] / max(A[lo:i + 1]) - 1
        row = dict(ticker=t, settle=d, entry=D[i], short_m=round(s / 1e6, 2), pct_shares=round(pct, 2), dtc=dtc, dd_3y=round(100 * dd, 1))
        for h in H_:
            if i + h < len(D) and j + h < len(spyD):
                r = A[i + h] / A[i] - 1; m = spyA[j + h] / spyA[j] - 1
                row[f"ret_{h}"] = round(100 * r, 2); row[f"xs_{h}"] = round(100 * (r - m), 2)
        events.append(row)
events.sort(key=lambda r: (r["ticker"], r["settle"]))
# episodes
eps = []; last = {}
for r in events:
    t = r["ticker"]; i = idx(t, r["entry"])
    if t in last and i - last[t] < 126: last[t] = i; continue
    last[t] = i; eps.append(r)
cols = list(events[0].keys()) + [c for h in H_ for c in (f"ret_{h}", f"xs_{h}") if c not in events[0]]
for name, rows in (("events", events), ("episodes", eps)):
    with open(H / f"{name}_min{int(MINPCT)}.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)
def summ(label, rows):
    print(f"\n{label}: n={len(rows)} tickers={len(set(r['ticker'] for r in rows))}")
    for h in H_:
        x = [r[f"xs_{h}"] for r in rows if f"xs_{h}" in r]
        if not x: continue
        print(f"  {h:>3}d excess vs SPY: median {st.median(x):6.1f}%  mean {st.mean(x):6.1f}%  short wins {sum(v < 0 for v in x)}/{len(x)}  squeeze(>+15%) {sum(v > 15 for v in x)}  (>+25%) {sum(v > 25 for v in x)}")
summ(f"All record prints, SI>={MINPCT}% of shares", events)
summ("Episode starts", eps)
summ("Episode starts with stock >=40% below 3y high", [r for r in eps if r["dd_3y"] <= -40])
summ("All record prints with stock >=40% below 3y high", [r for r in events if r["dd_3y"] <= -40])
summ("All record prints, days to cover < 4", [r for r in events if r["dtc"] < 4])
summ("All record prints, dd<=-40 and dtc<4 (Nike-like)", [r for r in events if r["dd_3y"] <= -40 and r["dtc"] < 4])
