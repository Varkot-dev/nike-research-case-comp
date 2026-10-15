"""Checker recomputations (2026-10-14). Run from data/hunt/hiring: python3 scripts/checker_recompute.py
1) same-date open postings Oct 2025 vs Oct 2026, 2) req flow using dense Common Crawl points only,
3) product/sales share US-only and ex-China, 4) H-1B LCAs split by Oct 1 (cap) start date."""
import pandas as pd, re
d = pd.read_csv("cc_listing_counts.csv"); d = d[(d.site == "new") & (d.is_unfiltered == 1)].dropna(subset=["total"])
d["day"] = pd.to_datetime(d.timestamp.astype(str).str[:8]); g = d.groupby("day").total.median()
print("Oct 2025 daily totals:", g["2025-10-05":"2025-10-31"].to_dict())
f = pd.read_csv("req_frontier_points.csv", parse_dates=["date"]); cc = f[(f.source == "commoncrawl") & (f.n_ids >= 500)].set_index("crawl")
def rate(a, b): return (cc.loc[b].frontier_req - cc.loc[a].frontier_req) / (cc.loc[b].date - cc.loc[a].date).days * 30.4
for a, b, a2, b2 in [("CC-MAIN-2025-26", "CC-MAIN-2025-38", "CC-MAIN-2026-25", "CC-MAIN-2026-39"),
                     ("CC-MAIN-2025-13", "CC-MAIN-2025-21", "CC-MAIN-2026-12", "CC-MAIN-2026-21"),
                     ("CC-MAIN-2025-08", "CC-MAIN-2025-38", "CC-MAIN-2026-08", "CC-MAIN-2026-39")]:
    r1, r2 = rate(a, b), rate(a2, b2); print(f"{a}->{b} {r1:.0f}/mo vs {a2}->{b2} {r2:.0f}/mo YoY {100*(r2/r1-1):+.0f}%")
src = open("scripts/build_composition.py").read(); exec(src[src.index("def bucket_new"):src.index("def bucket_old")])
j = pd.read_csv("cc_job_objects_bucketed.csv"); j = j[(j.site == "new") & (~j.bucket.isin(["retail_store", "internship"]))]
s = pd.read_csv("raw/repo_careers_corporate_2026-10-13.csv"); s["bucket"] = [bucket_new(x, "Corporate") for x in s.job_family]
s["country_std"] = s.country.replace({"Mainland China": "China"}); s["period"] = "census_2026-10-13"
for per, g2 in list(j.groupby("period")) + [("census_2026-10-13", s)]:
    if per not in ("2025H2", "2026H1", "2026Q3", "census_2026-10-13"): continue
    us = g2[g2.country_std == "United States"]; ex = g2[g2.country_std != "China"]
    print(per, "US prod %.1f US sales %.1f | exChina prod %.1f sales %.1f" % (100*(us.bucket=="product_design").mean(), 100*(us.bucket=="sales_merch").mean(), 100*(ex.bucket=="product_design").mean(), 100*(ex.bucket=="sales_merch").mean()))
h = pd.read_csv("h1b_lca_clean.csv", parse_dates=["submit"]); h["start"] = pd.to_datetime(h.start_date, errors="coerce")
n = h[h.firm == "Nike"]
for y in (2024, 2025, 2026):
    w = n[(n.submit >= f"{y}-01-01") & (n.submit <= f"{y}-06-15")]
    cap = w[w.start == pd.Timestamp(f"{y}-10-01")]
    print(y, "all", w.role_group.value_counts().to_dict(), "| Oct-1 start", cap.role_group.value_counts().to_dict())
