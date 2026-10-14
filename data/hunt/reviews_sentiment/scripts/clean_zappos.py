"""Tidy Zappos review dates/stars and listing snapshot. Usage: python3 -I clean_zappos.py <raw/zappos>"""
import sys, os, json, gzip, glob, pandas as pd
raw = sys.argv[1]
L = pd.DataFrame([json.loads(l) for l in gzip.open(os.path.join(raw, "zappos_listings.jsonl.gz"), "rt")])
L = L.drop_duplicates("productId")
L["gender"] = L.txAttrFacet_Gender.apply(lambda v: "|".join(v) if isinstance(v, list) else v)
cols = ["productId", "brandName", "productName", "gender", "reviewCount", "productRating", "price", "originalPrice", "onSale", "percentOff", "isNew", "productUrl"]
L[cols].assign(snapshot_date="2026-10-14").to_csv("zappos_listing_snapshot_2026-10-14.csv", index=False)
rows = []
for f in glob.glob(os.path.join(raw, "zappos_reviews_*.jsonl.gz")):  # v2 files (v1 kept in raw/zappos/v1, not read)
    try:
        for l in gzip.open(f, "rt"): rows.append(json.loads(l))
    except EOFError: pass
R = pd.DataFrame(rows)
R["date"] = pd.to_datetime(R.reviewDate.astype("int64"), unit="ms"); R["rating"] = pd.to_numeric(R.overallRating, errors="coerce")
R = R.drop_duplicates(["pid", "reviewDate", "rating"])
R["source"] = R.get("source", pd.Series(index=R.index, dtype=object)).replace("null", None).fillna("zappos native")
for c in ["incentivizedReview", "customerRewardReview"]:
    R[c] = R.get(c, pd.Series(index=R.index, dtype=object)).astype(str).eq("true")
R = R.merge(L[["productId", "brandName", "productName", "gender"]], left_on="pid", right_on="productId", how="left")
R[["pid", "brandName", "productName", "gender", "date", "rating", "shoeSize", "source", "incentivizedReview", "customerRewardReview"]].to_csv("zappos_reviews_tidy.csv", index=False)
print(len(R)); print(R.groupby(["brandName", "productName"]).agg(n=("date", "size"), first=("date", "min"), last=("date", "max"), rating=("rating", "mean")).to_string())

import numpy as np
R["model"] = R.productName.str.replace("&#174;", "").str.replace("Air Zoom ", "").str.replace("GEL-", "").str.strip()
out = []
for (m, nat), g in list(R.groupby(["model", R.source.eq("zappos native")])) + [((m, "all"), g) for m, g in R.groupby("model")]:
    t0 = g.date.quantile(0.01); age = (pd.Timestamp("2026-10-13") - t0).days
    row = dict(model=m, brand=g.brandName.iloc[0], subset={True: "native", False: "syndicated", "all": "all"}[nat], launch=t0.date(), age=age, total=len(g), rating_all=g.rating.mean(),
               incent_share=g.incentivizedReview.mean())
    for D in (90, 180, 365):
        w = g[g.date < t0 + pd.Timedelta(days=D)]
        row[f"n{D}"] = len(w) if age >= D else np.nan; row[f"r{D}"] = w.rating.mean() if age >= D else np.nan
        row[f"low{D}"] = (w.rating <= 2).mean() if age >= D else np.nan
    row["n_jul15_oct13_2026"] = int((g.date >= "2026-07-15").sum()); row["rating_jul15_oct13_2026"] = g[g.date >= "2026-07-15"].rating.mean()
    out.append(row)
pd.DataFrame(out).sort_values(["subset", "brand", "model"]).to_csv("zappos_launch_cohorts.csv", index=False)
