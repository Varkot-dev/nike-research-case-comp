"""Tidy Foot Locker Bazaarvoice running-model reviews (Nike worker + rival worker files).
Dedupes syndicated copies (same source review on several FL product ids) by (original product name, submitted time, rating),
tags brand / family / generation from the product name, writes fl_bv_reviews_tidy.csv.gz and fl_bv_monthly_family.csv.
Usage: python3 -I clean_footlocker_bv.py <raw/footlocker_bv>"""
import sys, os, re, gzip, io, pandas as pd, numpy as np
raw = sys.argv[1]
def read_partial(p):
    with gzip.open(p, "rb") as f:
        buf = b""
        try:
            while True:
                c = f.read(1 << 20)
                if not c: break
                buf += c
        except EOFError: pass
    txt = buf.decode("utf-8", "ignore"); txt = txt[: txt.rfind("\n") + 1]
    return pd.read_csv(io.StringIO(txt))
fr = [read_partial(os.path.join(raw, f)) for f in ["fl_bv_model_reviews.csv.gz", "fl_bv_rival_reviews.csv.gz"] if os.path.exists(os.path.join(raw, f))]
r = pd.concat(fr); prods = pd.read_csv(os.path.join(raw, "fl_bv_model_products.csv")).drop_duplicates("product_id")
r = r.merge(prods[["product_id", "name", "brand"]].astype({"product_id": str}), left_on=r.product_id.astype(str), right_on="product_id", how="left", suffixes=("", "_p"))
r["submitted"] = pd.to_datetime(r.submitted, utc=True, errors="coerce").dt.tz_localize(None)
r["src_name"] = r.original_product_name.fillna(r.name)
n0 = len(r); r = r.drop_duplicates(["src_name", "submitted", "rating"]); r = r.drop_duplicates("review_id")
FAM = [("Nike", r"pegasus plus|pegasus premium|pegasus trail|pegasus|vomero plus|vomero premium|vomero|structure|invincible|infinity ?rn|winflo"),
       ("HOKA", r"clifton|bondi|arahi"), ("ASICS", r"novablast|nimbus|kayano|cumulus"), ("Brooks", r"ghost max|ghost|adrenaline|glycerin"),
       ("On", r"cloudmonster|cloudsurfer|cloudrunner"), ("Saucony", r"\bride\b|triumph"), ("New Balance", r"\b880\b")]
def tag(n):
    s = str(n).lower()
    if "kid" in s or "grade school" in s or "toddler" in s or "preschool" in s or "boys'" in s or "girls'" in s: return (None, None, None)
    for b, rx in FAM:
        m = re.search(rx, s)
        if m:
            if b == "Nike" and "nike" not in s and "zoom" not in s: pass
            fam = m.group(0).replace(" ", "")
            g = re.search(re.escape(m.group(0)) + r"\s*(?:gts\s*)?(\d{1,2})\b", s)
            return (b, fam.title(), g.group(1) if g else None)
    return (None, None, None)
t = r.src_name.map(tag); r["brand_t"] = [x[0] for x in t]; r["family"] = [x[1] for x in t]; r["gen"] = [x[2] for x in t]
r = r[r.brand_t.notna()]
r["month"] = r.submitted.dt.to_period("M").astype(str)
r["syn"] = r.syndication_source.fillna("footlocker native")
r[["review_id", "product_id", "src_name", "brand_t", "family", "gen", "submitted", "month", "rating", "is_syndicated", "syn", "incentivized", "recommended"]].to_csv("fl_bv_reviews_tidy.csv.gz", index=False, compression="gzip")
m = r.groupby(["brand_t", "family", "gen", "month"], dropna=False).agg(reviews=("review_id", "size"), avg_rating=("rating", "mean")).reset_index()
m.to_csv("fl_bv_monthly_family.csv", index=False)
print(n0, "rows ->", len(r), "deduped tagged reviews"); print(r.groupby("brand_t").size()); print(r.syn.value_counts().head(12))
