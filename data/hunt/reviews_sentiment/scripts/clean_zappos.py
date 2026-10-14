"""Tidy Zappos review dates/stars and listing snapshot. Usage: python3 -I clean_zappos.py <raw/zappos>"""
import sys, os, json, gzip, glob, pandas as pd
raw = sys.argv[1]
L = pd.DataFrame([json.loads(l) for l in gzip.open(os.path.join(raw, "zappos_listings.jsonl.gz"), "rt")])
L = L.drop_duplicates("productId")
L["gender"] = L.txAttrFacet_Gender.apply(lambda v: "|".join(v) if isinstance(v, list) else v)
cols = ["productId", "brandName", "productName", "gender", "reviewCount", "productRating", "price", "originalPrice", "onSale", "percentOff", "isNew", "productUrl"]
L[cols].assign(snapshot_date="2026-10-14").to_csv("zappos_listing_snapshot_2026-10-14.csv", index=False)
rows = []
for f in glob.glob(os.path.join(raw, "zappos_reviews_*.jsonl.gz")):
    try:
        for l in gzip.open(f, "rt"): rows.append(json.loads(l))
    except EOFError: pass
R = pd.DataFrame(rows)
R["date"] = pd.to_datetime(R.reviewDate.astype("int64"), unit="ms"); R["rating"] = pd.to_numeric(R.overallRating, errors="coerce")
R = R.drop_duplicates(["pid", "reviewDate", "rating"])
R = R.merge(L[["productId", "brandName", "productName", "gender"]], left_on="pid", right_on="productId", how="left")
R[["pid", "brandName", "productName", "gender", "date", "rating", "shoeSize"]].to_csv("zappos_reviews_tidy.csv", index=False)
print(len(R)); print(R.groupby(["brandName", "productName"]).agg(n=("date", "size"), first=("date", "min"), last=("date", "max"), rating=("rating", "mean")).to_string())
