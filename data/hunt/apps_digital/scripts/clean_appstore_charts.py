"""Tidy brand ranks out of the full App Store chart snapshot, plus a Nike vs adidas head-to-head by storefront."""
import pandas as pd, glob
BASE = "/home/user/nike-research-case-comp/data/hunt/apps_digital"
f = sorted(glob.glob(f"{BASE}/raw/appstore_charts_all_*.csv.gz"))[-1]
d = pd.read_csv(f, dtype={"app_id": str})
dev = d.developer.fillna("")
key = pd.Series(None, index=d.index, dtype=object)
rules = [("Nike, Inc|NIKE|耐克", "nike"), ("adidas|Adidas", "adidas"), ("On AG", "on"), ("StockX", "stockx"), ("GOAT", "goat"), ("Shizhuang|POIZON|得物", "dewu_poizon"),
         ("lululemon", "lululemon"), ("PUMA", "puma"), ("Dick's", "dicks"), ("Foot Locker", "footlocker"), ("JD Sports", "jdsports"), ("ASICS", "asics"), ("Strava", "strava"), ("Skechers", "skechers"), ("Hoka|Deckers", "hoka")]
for pat, k in rules:
    key = key.where(key.notna(), pd.Series(k, index=d.index).where(dev.str.contains(pat, case=False, regex=True)))
d["brand"] = key
t = d[d.brand.notna()].copy()
t.to_csv(f"{BASE}/appstore_charts_brand_ranks_2026-10-14.csv", index=False)
s = t[(t.chart == "topfreeapplications") & (t.genre == "Shopping")]
best = s.groupby(["country", "brand"])["rank"].min().unstack()
cols = [c for c in ["nike", "adidas", "on", "stockx", "dewu_poizon", "lululemon", "puma", "dicks", "jdsports", "footlocker", "goat"] if c in best]
print(best[cols].to_string())
h2h = best[["nike", "adidas"]].copy()
h2h["nike_ahead"] = h2h.nike.fillna(101) < h2h.adidas.fillna(101)
both_absent = h2h.nike.isna() & h2h.adidas.isna()
print("storefronts:", len(h2h), "Nike ahead of adidas in Shopping top-free:", int(h2h.nike_ahead[~both_absent].sum()), "of", int((~both_absent).sum()))
print("Nike in top100 shopping:", int(h2h.nike.notna().sum()), " adidas:", int(h2h.adidas.notna().sum()))
hf = t[(t.chart == "topfreeapplications") & (t.genre == "Health & Fitness")].groupby(["country", "brand"])["rank"].min().unstack()
print(hf.to_string())
best.to_csv(f"{BASE}/appstore_shopping_topfree_best_rank_by_brand_2026-10-14.csv")
