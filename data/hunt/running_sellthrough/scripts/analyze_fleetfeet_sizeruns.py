"""Size-run depth at Fleet Feet from UPC docs. Output fleetfeet_sizerun_depth.csv (by product) and fleetfeet_sizerun_by_brand.csv"""
import pandas as pd, numpy as np
u = pd.read_csv("raw/fleetfeet_upc_2026-10-14.csv.gz")
u["size"] = pd.to_numeric(u["size"], errors="coerce")
u["gender"] = np.where(u.slug.str.startswith("womens"), "W", "M")
u["core"] = np.where(u.gender == "M", u["size"].between(8, 12), u["size"].between(6, 10))
u["in_stock"] = u.upc_inventory > 0
# the doc universe is every colour x size x width the brand lists; restrict to colours (skus) with any stock to measure size-run holes
sk = u.groupby(["slug", "sku"]).agg(sku_units=("upc_inventory", "sum")).reset_index()
u = u.merge(sk, on=["slug", "sku"]); u["live_sku"] = u.sku_units > 0
l = u[u.live_sku]
def agg(g, l_):
    return pd.Series({"upc_docs": len(g), "units": g.upc_inventory.sum(), "colours": g.sku.nunique(), "live_colours": l_.sku.nunique(),
        "live_colour_share": l_.sku.nunique() / g.sku.nunique(), "units_per_live_colour": l_.upc_inventory.sum() / max(l_.sku.nunique(), 1),
        "core_size_in_stock_share_live_colours": l_[l_.core].in_stock.mean(), "thin_share_live_colours": ((l_.upc_inventory > 0) & (l_.upc_inventory <= 2)).sum() / max(len(l_), 1),
        "oos_share_live_colours": 1 - l_.in_stock.mean(), "mean_price": g.price.mean(), "mean_orig": g.orig.replace(0, np.nan).mean()})
p = pd.DataFrame({s: agg(g, l[l.slug == s]) for s, g in u.groupby("slug")}).T
p.to_csv("fleetfeet_sizerun_depth.csv")
snap = pd.read_csv("../reviews_sentiment/fleetfeet_products_2026-10-14.csv")[["slug", "views30", "views7", "min_price", "list_price"]]
p = p.reset_index().rename(columns={"index": "slug"}).merge(snap, on="slug")
BR = {"nike": "Nike", "hoka": "HOKA", "brooks": "Brooks", "asics": "ASICS", "saucony": "Saucony", "new-balance": "New Balance", "on": "On", "adidas": "adidas"}
p.insert(0, "brand", p.slug.str.replace(r"^(mens|womens)-", "", regex=True).map(lambda x: next(v for k, v in BR.items() if x.startswith(k + "-"))))
p["units_per_view30"] = p.units / p.views30
p.to_csv("fleetfeet_sizerun_depth.csv", index=False)
b = p.groupby("brand").agg(models=("slug", "size"), units=("units", "sum"), views30=("views30", "sum"), live_colour_share=("live_colour_share", "mean"),
    core_size_in_stock=("core_size_in_stock_share_live_colours", "mean"), oos_share=("oos_share_live_colours", "mean"), thin_share=("thin_share_live_colours", "mean")).reset_index()
b["units_per_view30"] = b.units / b.views30; b.to_csv("fleetfeet_sizerun_by_brand.csv", index=False)
pd.set_option("display.width", 250)
print(p[["slug", "upc_docs", "units", "live_colours", "live_colour_share", "core_size_in_stock_share_live_colours", "oos_share_live_colours", "thin_share_live_colours", "views30", "units_per_view30", "min_price", "list_price"]].round(2).to_string())
print(b.round(3).to_string())
