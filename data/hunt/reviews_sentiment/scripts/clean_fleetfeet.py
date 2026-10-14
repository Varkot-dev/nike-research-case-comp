"""Tidy Fleet Feet product snapshot -> fleetfeet_products_2026-10-14.csv and brand summary."""
import json, sys, pandas as pd, numpy as np
d = pd.DataFrame(json.load(open(sys.argv[1])))
keep = {"product.brand": "brand", "product.title": "title", "product.slug": "slug", "product.gender": "gender", "product.surface": "surface",
        "product.shoeStyle": "shoe_style", "product.postDate": "post_ts", "computed.product.reviewCount": "review_count", "computed.product.averageRating": "avg_rating",
        "computed.product.averageFitRating": "avg_fit", "computed.product.trendScore": "trend_score", "product.views7": "views7", "product.views30": "views30",
        "product.views60": "views60", "product.inventory": "inventory_units", "product.minPrice": "min_price", "product.maxPrice": "max_price", "product.actualPrice": "list_price",
        "computed.discounted": "sku_discounted", "computed.colorCount": "color_count", "product.inStock": "in_stock"}
t = d[[k for k in keep if k in d.columns]].rename(columns=keep)
t["collection"] = t.brand.apply(lambda v: v[1] if isinstance(v, list) and len(v) > 1 else "")
t["brand"] = t.brand.apply(lambda v: v[0] if isinstance(v, list) else v)
for c in ["gender", "surface", "shoe_style"]:
    t[c] = t[c].apply(lambda v: "|".join(map(str, v)) if isinstance(v, list) else v)
t["post_date"] = pd.to_datetime(t.post_ts, unit="s", errors="coerce").dt.date
t["views_prior30"] = t.views60 - t.views30
t.insert(0, "snapshot_date", "2026-10-14")
t.drop(columns=["post_ts"]).to_csv(sys.argv[2], index=False)
print(len(t))
