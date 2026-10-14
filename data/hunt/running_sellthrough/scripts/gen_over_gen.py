"""Same-age (first 90 days) review counts, new generation vs previous generation, Dick's feed and Zappos (all sources). Output gen_over_gen_n90.csv"""
import pandas as pd
d = pd.read_csv("dicks_gen_cohorts.csv"); z = pd.read_csv("../reviews_sentiment/zappos_launch_cohorts.csv"); z = z[z["subset"] == "all"]
pairs = [("Nike", "Pegasus", 41, 42, "Pegasus 41", "Pegasus 42"), ("Nike", "Vomero", None, None, "Vomero 18", None), ("HOKA", "Clifton", 10, 11, "Clifton 10", "Clifton 11"), ("Brooks", "Ghost", 17, 18, "Ghost 17", "Ghost 18"),
         ("Brooks", "Glycerin", 22, 23, None, None), ("Brooks", "Adrenaline", 24, 25, None, None), ("ASICS", "Nimbus", 27, 28, "Nimbus 27", "Nimbus 28"), ("ASICS", "Novablast", 5, 6, "Novablast 5", "Novablast 6"), ("On", "Cloudmonster", None, None, "Cloudmonster 2", "Cloudmonster 3")]
rows = []
for b, f, g0, g1, zm0, zm1 in pairs:
    r = {"brand": b, "family": f, "old_gen": g0, "new_gen": g1}
    if g0 and g1:
        a = d[(d.brand == b) & (d.family == f) & (d.gen == g0)]; n = d[(d.brand == b) & (d.family == f) & (d.gen == g1)]
        if len(a) and len(n): r.update(dicks_old_launch=a.launch_proxy.iloc[0], dicks_new_launch=n.launch_proxy.iloc[0], dicks_old_n90=a.n90.iloc[0], dicks_new_n90=n.n90.iloc[0], dicks_ratio=n.n90.iloc[0] / a.n90.iloc[0])
    if zm0 and zm1:
        a = z[(z.model == zm0)]; n = z[(z.model == zm1)]
        if len(a) and len(n): r.update(zappos_old_n90=a.n90.iloc[0], zappos_new_n90=n.n90.iloc[0], zappos_ratio=n.n90.iloc[0] / a.n90.iloc[0], zappos_new_age_days=n.age.iloc[0])
    rows.append(r)
o = pd.DataFrame(rows); o.to_csv("gen_over_gen_n90.csv", index=False); pd.set_option("display.width", 250); print(o.round(2).to_string())
