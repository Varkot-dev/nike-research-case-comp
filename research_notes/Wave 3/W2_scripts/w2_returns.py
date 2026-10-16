"""W2: event returns for CFO Denton events vs S&P 500. Yahoo chart API adjclose, no email in request.
Usage: python3 -I w2_returns.py OUT.csv   (needs network)
Day 0 = first session that could reflect the news. Cumulative close-to-close from prior close. Abnormal = raw minus S&P 500 (no beta)."""
import json, sys, urllib.request, datetime as dt, csv, bisect
UA = {"User-Agent": "Mozilla/5.0"}
def px(sym):
    t1 = int(dt.datetime(2026, 10, 16).timestamp()); t0 = int(dt.datetime(2009, 1, 1).timestamp())
    u = f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}?period1={t0}&period2={t1}&interval=1d&events=div%2Csplit"
    d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60))["chart"]["result"][0]
    ts = d["timestamp"]; ac = d["indicators"]["adjclose"][0]["adjclose"]
    out = {}
    for t, a in zip(ts, ac):
        if a is not None:
            out[dt.datetime.utcfromtimestamp(t + d["meta"].get("gmtoffset", 0)).date().isoformat()] = a
    return out
# id, ticker, date (day 0), label
EV = [l.split("|") for l in open(sys.argv[2]).read().strip().splitlines()] if len(sys.argv) > 2 else []
def run(events, outp):
    cache = {}; spx = px("^GSPC"); sd = sorted(spx)
    rows = []
    for eid, tk, d0, *rest in events:
        if tk not in cache: cache[tk] = px(tk)
        p = cache[tk]; ds = sorted(p)
        i = bisect.bisect_left(ds, d0)
        if i >= len(ds) or ds[i] != d0: print("WARN day0 not a session", eid, d0, ds[i] if i < len(ds) else None)
        r = {"event_id": eid, "ticker": tk, "day0": ds[i], "prior_close_date": ds[i - 1]}
        j = bisect.bisect_left(sd, ds[i])
        for h in (0, 1, 3, 5, 20):
            if i + h < len(ds) and sd[j + h] == ds[i + h]:
                raw = p[ds[i + h]] / p[ds[i - 1]] - 1; b = spx[sd[j + h]] / spx[sd[j - 1]] - 1
                r[f"raw_d{h}_pct"] = round(raw * 100, 2); r[f"sp_d{h}_pct"] = round(b * 100, 2); r[f"vs_sp_d{h}_pct"] = round((raw - b) * 100, 2)
            else:
                r[f"raw_d{h}_pct"] = r[f"sp_d{h}_pct"] = r[f"vs_sp_d{h}_pct"] = ""
        rows.append(r)
    with open(outp, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    for r in rows: print(r["event_id"], r["day0"], r["vs_sp_d0_pct"], r["vs_sp_d1_pct"], r["vs_sp_d5_pct"], r["vs_sp_d20_pct"])
if __name__ == "__main__": run(EV, sys.argv[1])
