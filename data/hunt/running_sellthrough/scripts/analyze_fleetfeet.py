"""Fleet Feet public search index snapshot (2026-10-14): views 30d vs prior 30d by brand and Nike model; discount and stock depth.
Input ../reviews_sentiment/fleetfeet_products_2026-10-14.csv. Output fleetfeet_brand_views.csv, fleetfeet_nike_models.csv"""
import pandas as pd, numpy as np
d = pd.read_csv("../reviews_sentiment/fleetfeet_products_2026-10-14.csv")
d["views_prior30"] = d["views60"] - d["views30"]
d["disc"] = (d["list_price"] - d["min_price"]) / d["list_price"]
d["model"] = d["title"].str.replace(r"^(Men's|Women's|Unisex)\s*\|\s*", "", regex=True)
g = d.groupby("brand").agg(products=("slug", "size"), views30=("views30", "sum"), views_prior30=("views_prior30", "sum"),
    views7=("views7", "sum"), inventory_units=("inventory_units", "sum"), reviews=("review_count", "sum"),
    med_disc=("disc", "median"), share_sku_discounted=("sku_discounted", "mean")).reset_index()
g["views30_share"] = g.views30 / g.views30.sum(); g["views_prior30_share"] = g.views_prior30 / g.views_prior30.sum()
g["views_chg_30v30"] = g.views30 / g.views_prior30 - 1
g["views_per_inv_unit"] = g.views30 / g.inventory_units
g.sort_values("views30", ascending=False).to_csv("fleetfeet_brand_views.csv", index=False)
print(g.sort_values("views30", ascending=False).round(3).to_string())
n = d[d.brand == "Nike"].copy()
n["views_chg"] = n.views30 / n.views_prior30 - 1
cols = ["model", "gender", "post_date", "views7", "views30", "views_prior30", "views_chg", "inventory_units", "review_count", "avg_rating", "min_price", "list_price", "disc", "sku_discounted"]
n.sort_values("views30", ascending=False)[cols].to_csv("fleetfeet_nike_models.csv", index=False)
print(n.sort_values("views30", ascending=False)[cols].head(14).round(3).to_string())
# top-20 by views among all brands: who is there
t = d.sort_values("views30", ascending=False).head(25)[["brand", "model", "gender", "views30", "views_prior30", "inventory_units", "disc"]]
t.to_csv("fleetfeet_top25_by_views.csv", index=False); print(t.round(3).to_string())
