"""Requisition-number velocity: Nike's Workday requisition IDs (R-xxxxx, 5 digits) are issued sequentially.
The highest ID visible at a date is a 'frontier'; its slope = requisitions opened per day (all functions, global, incl. retail).
Sources: Common Crawl captures of Nike job-detail URLs (raw/commoncrawl/cdx_*.jsonl.gz) and the live Workday pull.
Usage: python3 build_req_velocity.py (from data/hunt/hiring)"""
import gzip, json, glob, re, pandas as pd, numpy as np
pts = []
for fn in sorted(glob.glob("raw/commoncrawl/cdx_*.jsonl.gz")):
    crawl = fn.split("cdx_")[1][:-9]
    best = []
    for l in gzip.open(fn, "rt"):
        r = json.loads(l); m = re.search(r"/job/R-(\d{5})(?!\d)", r["url"])
        if m: best.append((int(m.group(1)), r["timestamp"]))
    if len(best) < 5: continue
    best.sort()
    num, ts = best[-1]
    # frontier must be dated by the latest capture timestamp among the top 1% (a req seen later is still <= frontier then)
    top = best[-max(1, len(best) // 100):]
    pts.append({"source": "commoncrawl", "crawl": crawl, "date": pd.to_datetime(max(t for _, t in top)[:8]), "frontier_req": num, "n_ids": len(set(b[0] for b in best))})
live = pd.read_csv("live_postings_workday_2026-10-14.csv")
live = live[(live.company == "Nike") & live.req_id.str.match(r"^R-\d{5}$", na=False)].copy()
live["sd"] = pd.to_datetime(live.start_date, errors="coerce")
pts.append({"source": "live_workday", "crawl": "live", "date": pd.Timestamp("2026-10-14"), "frontier_req": int(live.req_id.str[2:].astype(int).max()), "n_ids": len(live)})
# live frontier by posting week (max req among postings first posted that week; lower bound because later-closed postings are gone)
lw = live.dropna(subset=["sd"]).groupby(live.sd.dt.to_period("W").dt.end_time.dt.normalize()).apply(lambda g: g.req_id.str[2:].astype(int).max())
for d, v in lw.items():
    if d >= pd.Timestamp("2026-06-01"): pts.append({"source": "live_workday_by_post_week", "crawl": "", "date": d, "frontier_req": int(v), "n_ids": None})
df = pd.DataFrame(pts).sort_values("date")
df.to_csv("req_frontier_points.csv", index=False)
cc = df[df.source.isin(["commoncrawl", "live_workday"])].copy()
cc = cc[cc.frontier_req.cummax() == cc.frontier_req]  # drop points below an earlier frontier (sparse crawls)
s = cc.set_index("date").frontier_req
m = s.resample("D").interpolate().resample("MS").first().dropna()
monthly = pd.DataFrame({"frontier_req_start_of_month": m})
monthly["reqs_opened_in_month"] = monthly.frontier_req_start_of_month.shift(-1) - monthly.frontier_req_start_of_month
monthly["reqs_trailing_12m"] = monthly.frontier_req_start_of_month - monthly.frontier_req_start_of_month.shift(12)
monthly.to_csv("req_velocity_monthly.csv")
print(cc.to_string()); print(monthly.to_string())
