"""r/RunningShoeGeeks post-title mentions by brand and running model (from reviews_sentiment/reddit_posts_tagged.csv.gz).
Windows are matched calendar windows; shares are robust to the Oct 2025 archive sample break. Outputs reddit_rsg_brand_model_windows.csv"""
import pandas as pd, numpy as np
r = pd.read_csv("../reviews_sentiment/reddit_posts_tagged.csv.gz", low_memory=False)
r = r[r.subreddit == "RunningShoeGeeks"].copy()
brands = ["Nike", "HOKA", "ASICS", "Brooks", "On", "Saucony", "New Balance", "adidas"]
models = {"Pegasus": "Nike", "Vomero": "Nike", "Invincible": "Nike", "Clifton": "HOKA", "Bondi": "HOKA", "Mach": "HOKA", "Novablast": "ASICS", "Superblast": "ASICS", "Nimbus": "ASICS", "Ghost": "Brooks", "Cloudmonster": "On", "Endorphin": "Saucony"}
wins = {"Jun-Sep": ("06", "09"), "Jul-Sep": ("07", "09"), "Mar-May": ("03", "05"), "Jan-Feb": ("01", "02")}
rows = []
for wn, (a, b) in wins.items():
    for y in (2024, 2025, 2026):
        w = r[(r.month >= f"{y}-{a}") & (r.month <= f"{y}-{b}")]
        tot = sum(w["b_" + x].sum() for x in brands)
        for x in brands: rows.append({"window": wn, "year": y, "kind": "brand", "name": x, "posts_mentioning": int(w["b_" + x].sum()), "share_of_brand_mentions": w["b_" + x].sum() / tot, "all_posts": len(w)})
        mt = sum(w["m_" + m].sum() for m in models)
        for m in models: rows.append({"window": wn, "year": y, "kind": "model", "name": m, "posts_mentioning": int(w["m_" + m].sum()), "share_of_brand_mentions": w["m_" + m].sum() / mt, "all_posts": len(w)})
o = pd.DataFrame(rows); o.to_csv("reddit_rsg_brand_model_windows.csv", index=False)
pv = o[(o.window == "Jun-Sep")].pivot_table(index=["kind", "name"], columns="year", values=["posts_mentioning", "share_of_brand_mentions"])
pd.set_option("display.width", 250); print(pv.round(3).to_string())
