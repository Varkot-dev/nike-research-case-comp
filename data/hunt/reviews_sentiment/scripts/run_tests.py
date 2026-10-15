"""Run the pre-registered tests on the tidy files in this folder; writes test_*.csv. Usage: python3 -I scripts/run_tests.py"""
import pandas as pd, numpy as np, math
out = {}
# ---------- T1: nike.com organic US review volume, Jun-Sep, main style codes (perf running vs lifestyle vs entry running)
r = pd.read_csv("nike_reviews_tidy.csv.gz", parse_dates=["date"])
cnt = r.groupby(["model", "gender", "style"]).size().rename("n").reset_index()
main = cnt.sort_values("n").groupby(["model", "gender"]).tail(1)[["style"]].assign(main=True)
r = r.merge(main, on="style", how="left"); r["main"] = r["main"].fillna(False).astype(bool)
RUN = ["Pegasus", "Vomero", "Structure", "Invincible", "Pegasus Plus", "Vomero Plus", "Vomero Premium", "Pegasus Premium", "InfinityRN"]
LIFE = ["Air Force 1", "Dunk Low", "Air Jordan 1", "Air Max 90", "Cortez", "Zoom Vomero 5"]
ENTRY = ["Revolution", "Downshifter", "Winflo", "Journey Run", "Quest"]
r["grp"] = np.select([r.family.isin(RUN), r.family.isin(LIFE), r.family.isin(ENTRY)], ["perf_run", "lifestyle", "entry_run"], "other")
rm = r[r["main"] & ~r.model.str.contains(r"\(|SE$|GORE|EasyOn", regex=True)].copy()
rm["org_us"] = rm.us & ~rm.incentivized
rows = []
for y in range(2021, 2027):
    w = rm[(rm.date >= f"{y}-06-01") & (rm.date <= f"{y}-09-30")]
    for gname, g in w.groupby("grp"):
        rows.append(dict(window=f"{y} Jun-Sep", grp=gname, reviews=len(g), organic_us=int(g.org_us.sum()), avg_rating=g.rating.mean(),
                         organic_rating=g[~g.incentivized].rating.mean(), share_1_2=(g.rating <= 2).mean(), incentivized_share=g.incentivized.mean()))
t1 = pd.DataFrame(rows).sort_values(["grp", "window"])
t1["organic_us_yoy"] = t1.groupby("grp").organic_us.pct_change()
t1.to_csv("test1_nikecom_jun_sep_by_group.csv", index=False)
# ---------- T2: Dick's-sourced reviews (via Foot Locker BV syndication) by brand, Jun-Jul 2026 vs Jun-Jul 2025
f = pd.read_csv("fl_bv_reviews_tidy.csv.gz", parse_dates=["submitted"])
d = f[f.syn == "dickssportinggoods.com"].copy()
rows = []
for b, g in d.groupby("brand_t"):
    for lab, a, z in [("JunJul2025", "2025-06-01", "2025-07-31"), ("JunJul2026", "2026-06-01", "2026-07-31"), ("FebMay2026", "2026-02-01", "2026-05-31"), ("FebMay2025", "2025-02-01", "2025-05-31")]:
        w = g[(g.submitted >= a) & (g.submitted <= z + " 23:59")]
        rows.append(dict(brand=b, window=lab, reviews=len(w), avg_rating=w.rating.mean(), share_1_2=(w.rating <= 2).mean()))
t2 = pd.DataFrame(rows).pivot_table(index="brand", columns="window", values=["reviews", "avg_rating", "share_1_2"])
t2.columns = [f"{a}_{b}" for a, b in t2.columns]
t2["yoy_JunJul"] = t2.reviews_JunJul2026 / t2.reviews_JunJul2025 - 1
t2["yoy_FebMay"] = t2.reviews_FebMay2026 / t2.reviews_FebMay2025 - 1
t2.to_csv("test2_dicks_reviews_by_brand.csv")
# ---------- T3: same-platform launch cohorts on Zappos and Dick's: rating and early volume, successor vs predecessor
z = pd.read_csv("zappos_launch_cohorts.csv"); z.to_csv("test3_zappos_cohorts.csv", index=False)
dd = d.copy(); dd["low"] = dd.rating <= 2
c = dd[dd.submitted >= "2024-01-01"].groupby(["brand_t", "family", "gen"]).agg(n=("review_id", "size"), rating=("rating", "mean"), share_1_2=("low", "mean"), first=("submitted", "min")).reset_index()
c[c.n >= 30].to_csv("test3_dicks_rating_by_generation.csv", index=False)
# ---------- T4: Reddit r/RunningShoeGeeks deal intensity
m = pd.read_csv("reddit_monthly_mentions.csv"); b = m[(m.kind == "brand") & (m.subreddit == "RunningShoeGeeks")].copy()
b["fq"] = pd.PeriodIndex(b.month, freq="M").asfreq("Q-MAY").astype(str)
g = b.groupby(["fq", "tag"])[["mentions", "deal_posts", "review_posts"]].sum().reset_index()
tot = g.groupby("fq")[["mentions", "deal_posts", "review_posts"]].sum()
n = g[g.tag == "Nike"].set_index("fq")
t4 = pd.DataFrame({"nike_mentions": n.mentions, "all_brand_mentions": tot.mentions, "nike_deal_posts": n.deal_posts, "all_deal_posts": tot.deal_posts,
                   "nike_review_posts": n.review_posts, "all_review_posts": tot.review_posts})
t4["nike_mention_share"] = t4.nike_mentions / t4.all_brand_mentions; t4["nike_deal_share"] = t4.nike_deal_posts / t4.all_deal_posts
t4["deal_intensity_index"] = t4.nike_deal_share / t4.nike_mention_share; t4["nike_review_share"] = t4.nike_review_posts / t4.all_review_posts
t4.to_csv("test4_reddit_rsg_deal_intensity.csv")
def ztest(x1, n1, x2, n2):
    p = (x1 + x2) / (n1 + n2); se = math.sqrt(p * (1 - p) * (1 / n1 + 1 / n2)); zz = (x1 / n1 - x2 / n2) / se
    return zz, math.erfc(abs(zz) / math.sqrt(2))
a, bq = t4.loc["2027Q1"], t4.loc["2026Q1"]
print("T4 z-test Nike deal share FY27Q1 vs FY26Q1:", ztest(a.nike_deal_posts, a.all_deal_posts, bq.nike_deal_posts, bq.all_deal_posts))
print(t1.round(3).to_string()); print(t2.round(3).to_string()); print(t4.round(3).loc["2023Q1":].to_string())
