"""Review velocity at Dick's (via Foot Locker Bazaarvoice syndication) by brand, model family and generation.
Input ../reviews_sentiment/fl_bv_reviews_tidy.csv.gz. Outputs dicks_monthly_brand.csv, dicks_window_yoy.csv, dicks_gen_cohorts.csv"""
import pandas as pd, numpy as np
d = pd.read_csv("../reviews_sentiment/fl_bv_reviews_tidy.csv.gz")
d["submitted"] = pd.to_datetime(d["submitted"]); d["month"] = d["submitted"].dt.to_period("M").astype(str)
k = d[d.syn == "dickssportinggoods.com"].copy()
B4 = ["Nike", "Brooks", "HOKA", "ASICS"]
m = k.groupby(["month", "brand_t"]).size().unstack(fill_value=0)[B4]
m["total4"] = m.sum(axis=1)
for b in B4: m[b + "_share"] = m[b] / m.total4
m.to_csv("dicks_monthly_brand.csv")
def win(a, b): return k[(k.month >= a) & (k.month <= b)].groupby("brand_t").size().reindex(B4).fillna(0)
rows = []
for name, (a1, b1, a2, b2) in {"Jun-Jul": ("2025-06", "2025-07", "2026-06", "2026-07"), "Jun-Jul(wide Mar-Jul)": ("2025-03", "2025-07", "2026-03", "2026-07"), "Jan-May": ("2025-01", "2025-05", "2026-01", "2026-05"), "Jun-Aug": ("2025-06", "2025-08", "2026-06", "2026-08")}.items():
    x, y = win(a1, b1), win(a2, b2)
    for b in B4: rows.append({"window": name, "brand": b, "n_2025": x[b], "n_2026": y[b], "yoy": y[b] / x[b] - 1 if x[b] else np.nan,
                              "share_2025": x[b] / x.sum(), "share_2026": y[b] / y.sum()})
w = pd.DataFrame(rows); w.to_csv("dicks_window_yoy.csv", index=False); print(w.round(3).to_string())
# Nike by family, Jun-Jul and Mar-Jul
nf = k[k.brand_t == "Nike"]
fam = []
for a1, b1, a2, b2, nm in [("2025-06", "2025-07", "2026-06", "2026-07", "Jun-Jul"), ("2025-03", "2025-07", "2026-03", "2026-07", "Mar-Jul")]:
    for f, g in nf.groupby("family"):
        x = ((g.month >= a1) & (g.month <= b1)).sum(); y = ((g.month >= a2) & (g.month <= b2)).sum()
        fam.append({"window": nm, "family": f, "n_2025": x, "n_2026": y, "yoy": y / x - 1 if x else np.nan})
pd.DataFrame(fam).to_csv("dicks_nike_family_yoy.csv", index=False); print(pd.DataFrame(fam).round(2).to_string())
# generation cohorts: first review date (2nd percentile) and reviews in first 90 / 180 days, Dick's source only
out = []
for (b, f, g), x in k.groupby(["brand_t", "family", "gen"]):
    if len(x) < 15: continue
    t0 = x.submitted.quantile(0.02).normalize()
    age = (x.submitted - t0).dt.days
    out.append({"brand": b, "family": f, "gen": g, "launch_proxy": t0.date(), "total": len(x), "n90": int((age <= 90).sum()), "n180": int((age <= 180).sum()),
                "n365": int((age <= 365).sum()), "avg_rating": round(x.rating.mean(), 2), "last_review": x.submitted.max().date()})
c = pd.DataFrame(out).sort_values(["brand", "family", "gen"]); c.to_csv("dicks_gen_cohorts.csv", index=False)
print(c[c.family.isin(["Pegasus", "Vomero", "Clifton", "Bondi", "Ghost", "Nimbus", "Novablast", "Structure", "Invincible", "Triumph", "Adrenaline", "Glycerin", "Kayano"])].to_string())
