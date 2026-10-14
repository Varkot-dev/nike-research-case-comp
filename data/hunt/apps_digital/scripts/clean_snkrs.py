"""Rebuild tidy SNKRS product table from raw feed pages (all marketplaces pulled).
Per product: launch date (launchView.startEntryDate, else merchProduct.commerceStartDate, else thread viewStartDate),
price, discount flag, availability, size-level stock (availableGtins levels HIGH/MEDIUM/LOW/OOS).
Out: snkrs_products_tidy.csv, snkrs_cohort_monthly.csv
"""
import json, gzip, glob, os, csv
import pandas as pd
BASE = "/home/user/nike-research-case-comp/data/hunt/apps_digital"
rows = []
for m in sorted(os.listdir(f"{BASE}/raw/snkrs")):
    for f in sorted(glob.glob(f"{BASE}/raw/snkrs/{m}/page_*.json.gz")):
        d = json.load(gzip.open(f))
        for o in d.get("objects", []):
            pc = o.get("publishedContent", {}) or {}
            for p in o.get("productInfo", []) or []:
                mp = p.get("merchProduct", {}) or {}; pr = p.get("merchPrice", {}) or {}; lv = p.get("launchView") or {}
                g = p.get("availableGtins") or []
                lev = [x.get("level") for x in g]
                pcn = p.get("productContent", {}) or {}
                rows.append(dict(marketplace=m, thread_id=o.get("id"), view_start=pc.get("viewStartDate"), style_color=mp.get("styleColor"),
                    product_type=mp.get("productType"), merch_status=mp.get("status"), commerce_start=mp.get("commerceStartDate"),
                    publish_type=mp.get("publishType"), exclusive_access=mp.get("exclusiveAccess"), launch_method=lv.get("method"),
                    launch_start=lv.get("startEntryDate"), full_price=pr.get("fullPrice"), current_price=pr.get("currentPrice"),
                    discounted=pr.get("discounted"), currency=pr.get("currency"), available=(p.get("availability") or {}).get("available"),
                    n_skus=len(p.get("skus") or []), n_gtins_listed=len(g), n_high=lev.count("HIGH"), n_medium=lev.count("MEDIUM"),
                    n_low=lev.count("LOW"), n_oos=lev.count("OOS"), title=pcn.get("fullTitle") or pcn.get("title"), colorway=pcn.get("colorDescription")))
df = pd.DataFrame(rows)
for c in ["view_start", "commerce_start", "launch_start"]:
    df[c] = pd.to_datetime(df[c], errors="coerce", utc=True)
df["release_date"] = df.launch_start.fillna(df.commerce_start).fillna(df.view_start)
df = df.sort_values("view_start").drop_duplicates(["marketplace", "style_color"], keep="last")
df["release_month"] = df.release_date.dt.strftime("%Y-%m")
df["in_stock_sizes"] = df.n_high + df.n_medium + df.n_low
df["share_sizes_in_stock"] = df.in_stock_sizes / (df.in_stock_sizes + df.n_oos).where(lambda s: s > 0)
df["deep_stock"] = (df.n_high + df.n_medium) > 0
df["disc_pct"] = 1 - df.current_price / df.full_price
df.to_csv(f"{BASE}/snkrs_products_tidy.csv", index=False)
fw = df[df.product_type == "FOOTWEAR"]
g = fw.groupby(["marketplace", "release_month"]).agg(n_products=("style_color", "size"), share_available=("available", "mean"),
      share_discounted=("discounted", "mean"), avg_disc_pct=("disc_pct", "mean"), share_deep_stock=("deep_stock", "mean"),
      avg_share_sizes_in_stock=("share_sizes_in_stock", "mean"), share_draw_LEO_DAN=("launch_method", lambda s: s.isin(["LEO", "DAN"]).mean()),
      avg_full_price=("full_price", "mean")).reset_index()
g.to_csv(f"{BASE}/snkrs_cohort_monthly.csv", index=False)
print(len(df), len(fw)); print(g.to_string())
