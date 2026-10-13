"""Build markdown tables for U_REVIEWS.md from the tidy CSVs. Usage: python3 -I make_tables.py <data_dir> <out.md>"""
import sys, pandas as pd, numpy as np
D, OUT = sys.argv[1:3]; L = []
def md(df, fmt=None):
    df = df.copy()
    cols = list(df.columns); s = "| " + " | ".join(map(str, cols)) + " |\n|" + "|".join(["---"] * len(cols)) + "|\n"
    for _, r in df.iterrows():
        s += "| " + " | ".join("" if (isinstance(v, float) and np.isnan(v)) else (f"{v:,.3f}" if isinstance(v, float) and abs(v) < 10 else (f"{v:,.0f}" if isinstance(v, (float, int, np.integer)) else str(v))) for v in r.values) + " |\n"
    return s
a = pd.read_csv(f"{D}/amazon_quarterly_nike_fiscal.csv")
n = a[(a.level == "firm") & (a.unit == "Nike Inc") & (a.qsort >= 20191) & (a.qsort <= 20241)]
peers = a[(a.level == "firm") & (a.unit != "Nike Inc") & (a.qsort >= 20191) & (a.qsort <= 20241)]
pm = peers.groupby("quarter").agg(peer_reviews=("review_cnt", "sum"), peer_stars=("avg_rating", "mean"), peer_tone=("avg_tone_nb", "mean"), peer_AbnTone=("AbnormalTone", "mean"))
t = n.set_index("quarter")[["listings_proxy", "review_cnt", "avg_rating", "share_1_2_star", "avg_tone_nb", "avg_tone_vader", "AbnormalTone", "Negative_AbnormalTone", "AbnormalRating", "AbnormalReviewCnt"]].join(pm)
t = t.rename(columns={"listings_proxy": "Nike Inc products reviewed", "review_cnt": "reviews", "avg_rating": "stars", "share_1_2_star": "1-2 star share",
                      "avg_tone_nb": "tone NB", "avg_tone_vader": "tone VADER", "AbnormalTone": "AbnTone", "Negative_AbnormalTone": "Neg_AbnTone",
                      "AbnormalRating": "AbnRating", "AbnormalReviewCnt": "AbnReviewCnt (100s)", "peer_stars": "peer avg stars", "peer_tone": "peer avg tone", "peer_AbnTone": "peer avg AbnTone", "peer_reviews": "peer reviews"})
L.append("### C1. Amazon (2023 dataset), Nike Inc by Nike fiscal quarter, with the 9-competitor average\n\n" + md(t.reset_index()))
for tag, metric, lab in (("C2a", "AbnormalTone", "AbnormalTone"), ("C2b", "avg_rating", "average stars"), ("C2c", "listings_proxy", "distinct products reviewed (listing proxy)")):
    p = a[(a.level == "firm") & (a.qsort >= 20201) & (a.qsort <= 20241)].pivot(index="quarter", columns="unit", values=metric)
    p = p.reindex(n[n.qsort >= 20201].quarter)
    L.append(f"### {tag}. Amazon {lab} by firm and Nike fiscal quarter\n\n" + md(p.reset_index()))
c = a[(a.level == "firm") & a.quarter.str.match(r"^20(1[7-9]|2[0-3])Q")] if False else None
cal = pd.read_csv(f"{D}/amazon_quarterly_calendar.csv"); cal = cal[(cal.level == "firm") & (cal.quarter >= "2019Q1") & (cal.quarter <= "2023Q3")]
L.append("### C3. Amazon by calendar quarter: AbnormalTone for Nike Inc, adidas, HOKA, On, New Balance\n\n" + md(
    cal[cal.unit.isin(["Nike Inc", "adidas", "HOKA", "On", "New Balance"])].pivot(index="quarter", columns="unit", values="AbnormalTone").round(3).reset_index()))
th = pd.read_csv(f"{D}/amazon_complaint_themes_by_fy.csv")
for c_ in ("fake", "quality"):
    L.append(f"### C4. Share of Amazon reviews mentioning '{c_}' themes, percent, by Nike fiscal year\n\n" + md((100 * th.pivot(index="fy", columns="firm", values=c_)).round(2).reset_index()))
r = pd.read_csv(f"{D}/recent_reviews_quarterly_fiscal.csv"); r = r[(r.qsort >= 20221) & (r.qsort <= 20271)]
for u in ["Nike (nike.com) [non-incentivized only]", "Nike (nike.com)"]:
    x = r[r.unit == u][["fis_q", "review_cnt", "products", "avg_rating", "share_1_2_star", "share_incentivized", "avg_tone_nb", "avg_tone_vader", "AbnormalTone", "Negative_AbnormalTone", "AbnormalRating"]]
    L.append(f"### C5. {u}: reviews of currently listed shoe styles, by Nike fiscal quarter\n\n" + md(x))
fl = r[r.unit.str.startswith("FL: ") & ~r.unit.str.contains("native")]
if len(fl):
    for v, lab in (("avg_rating", "average stars"), ("avg_tone_nb", "tone NB"), ("AbnormalTone", "AbnormalTone"), ("share_1_2_star", "1-2 star share")):
        L.append(f"### C6. Foot Locker (Bazaarvoice) reviews, {lab}, by brand and Nike fiscal quarter\n\n" + md(fl.pivot(index="fis_q", columns="unit", values=v).reindex(sorted(fl.fis_q.unique(), key=lambda q: int(q[4:]) * 10 + int(q[1]))).reset_index()))
    L.append("### C6b. Foot Locker review counts by brand and quarter (top 25 products per brand, capped at 1,000 newest reviews per product)\n\n" + md(fl.pivot(index="fis_q", columns="unit", values="review_cnt").reindex(sorted(fl.fis_q.unique(), key=lambda q: int(q[4:]) * 10 + int(q[1]))).reset_index()))
fs = pd.read_csv(f"{D}/footlocker_nike_inc_listing_share.csv")
lc = pd.read_csv(f"{D}/footlocker_listing_counts_by_brand.csv")
for g in ("mens", "womens"):
    p = lc[lc.gender == g].pivot_table(index="snapshot_date", columns="brand", values="listing_count")
    p = p.join(fs[fs.gender == g].set_index("snapshot_date")[["nike_inc_share_pct"]])
    L.append(f"### C7. Foot Locker {g} shoes: listing counts by brand (brand filter counts) and Nike Inc share of focus-brand listings\n\n" + md(p.reset_index()))
s = pd.read_csv(f"{D}/amazon_bestsellers_by_halfyear.csv")
L.append("### C8. Amazon Best Sellers (top 30, six shoe lists), averages by half-year\n\n" + md(s))
try:
    b = pd.read_csv(f"{D}/footlocker_bv_brand_stats.csv"); L.append("### C9. Foot Locker catalog (Bazaarvoice), top products by review count: lifetime average rating\n\n" + md(b))
except FileNotFoundError: pass
g = pd.read_csv(f"{D}/footlocker_live_ratings_by_brand.csv")
L.append("### C10. Foot Locker live listing pages today (2026-10-13), top 200 by relevance per brand (ratings shown rounded to whole stars)\n\n" + md(g))
w = pd.read_csv(f"{D}/../../marketplace/data/nike_wall_history.csv") if False else None
open(OUT, "w").write("\n".join(L)); print("ok", len(L))
