"""Tidy summaries for Part 2 snapshot data (Amazon Best Sellers, Foot Locker listings and ratings, BV product stats)."""
import sys, os, pandas as pd, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brandmatch import FOCUS, group_of
D = sys.argv[1]
# Amazon Best Sellers
a = pd.read_csv(f"{D}/amazon_bestsellers_ratings.csv"); a = a[a["rank"].notna() & (a["rank"] <= 30)]
a["group"] = a.brand.map(group_of)
rows = []
for (d, c), x in a.groupby(["snapshot_date", "category"]):
    n = x[x.group == "Nike Inc"]; o = x[(x.group != "Nike Inc") & (x.brand != "Other")]
    rows.append(dict(snapshot_date=d, category=c, items=len(x), nike_inc_items_top30=len(n), nike_inc_share_top30_pct=round(100 * len(n) / len(x), 1),
                     nike_inc_best_rank=n["rank"].min() if len(n) else None, nike_inc_avg_stars=n.stars.mean(), peer_brands_avg_stars=o.stars.mean(),
                     nike_inc_median_rating_count=n.rating_count.median(), peer_median_rating_count=o.rating_count.median(),
                     hoka_on_items_top30=int(x.brand.isin(["HOKA", "On"]).sum()), adidas_items_top30=int((x.brand == "adidas").sum())))
S = pd.DataFrame(rows); S.to_csv(f"{D}/amazon_bestsellers_snapshot_summary.csv", index=False, float_format="%.3f")
S["period"] = pd.to_datetime(S.snapshot_date).dt.year.astype(str) + "H" + np.where(pd.to_datetime(S.snapshot_date).dt.month <= 6, "1", "2")
P = S.groupby("period").agg(snapshots=("items", "size"), nike_inc_share_top30_pct=("nike_inc_share_top30_pct", "mean"),
                            nike_inc_avg_stars=("nike_inc_avg_stars", "mean"), peer_avg_stars=("peer_brands_avg_stars", "mean"),
                            hoka_on_items=("hoka_on_items_top30", "mean")).reset_index()
P.to_csv(f"{D}/amazon_bestsellers_by_halfyear.csv", index=False, float_format="%.3f")
# Foot Locker listing counts (women's + men's shoes brand facets) over time
f = pd.concat([pd.read_csv(f"{D}/footlocker_wayback_brand_facets.csv"), pd.read_csv(f"{D}/footlocker_live_brand_facets.csv")])
f["brand"] = f.brand.str.replace("®", "", regex=False).str.strip().replace({"HOKA ONE ONE": "HOKA", "Asics": "ASICS", "Hoka": "HOKA", "ON": "On"})
f = f.groupby(["snapshot_date", "source", "gender", "brand"], as_index=False).listing_count.sum()
f = f.drop_duplicates(["snapshot_date", "gender", "brand"])
f = f[~f.brand.str.contains(r"\$|^Under \$|^Size|^\d", regex=True)]
FB = FOCUS + ["Saucony"]
tot = f[f.brand.isin(FB)].groupby(["snapshot_date", "gender"]).listing_count.sum().rename("all_brand_facet_sum")  # sum over the focus brands only (facet lists vary by snapshot)
f = f.join(tot, on=["snapshot_date", "gender"]); f["share_pct"] = 100 * f.listing_count / f.all_brand_facet_sum
fk = f[f.brand.isin(FOCUS + ["Saucony"])].copy()
fk.to_csv(f"{D}/footlocker_listing_counts_by_brand.csv", index=False, float_format="%.2f")
ni = f[f.brand.isin(["Nike", "Jordan", "Converse"])].groupby(["snapshot_date", "gender"]).agg(nike_inc_listings=("listing_count", "sum"), all_brands=("all_brand_facet_sum", "first")).reset_index()
ni["nike_inc_share_pct"] = 100 * ni.nike_inc_listings / ni.all_brands
ni.to_csv(f"{D}/footlocker_nike_inc_listing_share.csv", index=False, float_format="%.2f"); print(ni.to_string())
print(fk.pivot_table(index=["gender", "snapshot_date"], columns="brand", values="listing_count").to_string())
# Foot Locker live ratings by brand (top-200 by relevance per brand and gender)
i = pd.read_csv(f"{D}/footlocker_live_items.csv").drop_duplicates(["gender", "sku"])
i = i[i.brand == i.query_brand.replace({"ASICS®": "ASICS"})]
g = i.groupby(["query_brand", "gender"]).apply(lambda x: pd.Series(dict(products=len(x), share_with_reviews=(x.reviews > 0).mean(),
        total_reviews=x.reviews.sum(), median_reviews=x.reviews.median(), review_weighted_rating=np.average(x.rating[x.reviews > 0], weights=x.reviews[x.reviews > 0]) if (x.reviews > 0).any() else np.nan,
        share_on_sale=(x.price < x.list_price).mean())), include_groups=False).reset_index()
g.to_csv(f"{D}/footlocker_live_ratings_by_brand.csv", index=False, float_format="%.3f")
# Bazaarvoice product-level stats (Foot Locker catalog, top products by review count)
try:
    b = pd.read_csv(f"{D}/footlocker_bv_products.csv")
    bb = b.groupby("brand").apply(lambda x: pd.Series(dict(products=len(x), total_reviews=x.total_reviews.sum(),
           review_weighted_avg_rating=np.average(x.avg_rating, weights=x.total_reviews))), include_groups=False).reset_index()
    bb.to_csv(f"{D}/footlocker_bv_brand_stats.csv", index=False, float_format="%.3f"); print(bb)
except FileNotFoundError: pass
print(P.to_string()); print(g.to_string())
