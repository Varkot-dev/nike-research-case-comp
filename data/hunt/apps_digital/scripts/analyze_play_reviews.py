"""Clean Play review pulls into monthly and Nike-fiscal-quarter panels, and run the calibration and trend tests.
Outputs: play_reviews_monthly.csv, play_reviews_fq.csv, test_play_calibration.csv, test_play_latest.csv
"""
import glob, pandas as pd, numpy as np
BASE = "/home/user/nike-research-case-comp/data/hunt/apps_digital"
rows = []
for f in sorted(glob.glob(f"{BASE}/raw/play_reviews/*.csv.gz")):
    app, loc = f.split("/")[-1][:-7].split("__")
    d = pd.read_csv(f, parse_dates=["at"])
    d = d[d["at"] >= "2019-01-01"]
    g = d.groupby(d["at"].dt.to_period("M")).agg(n_reviews=("score", "size"), avg_stars=("score", "mean"),
                                                 share_1star=("score", lambda s: (s == 1).mean()), share_5star=("score", lambda s: (s == 5).mean()),
                                                 n_versions=("app_version", "nunique"))
    g = g.reset_index().rename(columns={"at": "month"}); g["app"] = app; g["locale"] = loc
    rows.append(g)
m = pd.concat(rows); m["month"] = m["month"].astype(str)
# partial current month: scale October 2026 (data to Oct 14) is flagged, not scaled
m["partial_month"] = m["month"] == "2026-10"
m.to_csv(f"{BASE}/play_reviews_monthly.csv", index=False)

def fq(ym):
    y, mo = map(int, ym.split("-"))
    fy = y + 1 if mo >= 6 else y
    q = {6: 1, 7: 1, 8: 1, 9: 2, 10: 2, 11: 2, 12: 3, 1: 3, 2: 3, 3: 4, 4: 4, 5: 4}[mo]
    return f"FY{fy}Q{q}"
m = m[~m.partial_month].copy(); m["fq"] = m.month.map(fq)
q = m.groupby(["app", "locale", "fq"]).agg(n_reviews=("n_reviews", "sum"), months=("month", "nunique")).reset_index()
q = q[q.months == 3]
q["fy"] = q.fq.str[2:6].astype(int); q["qn"] = q.fq.str[-1].astype(int)
q = q.sort_values(["app", "locale", "fy", "qn"])
q["prev_fq"] = "FY" + (q.fy - 1).astype(str) + "Q" + q.qn.astype(str)
q = q.merge(q[["app", "locale", "fq", "n_reviews"]].rename(columns={"fq": "prev_fq", "n_reviews": "n_prev"}), on=["app", "locale", "prev_fq"], how="left")
q["yoy_pct"] = (q.n_reviews / q.n_prev - 1) * 100
q.to_csv(f"{BASE}/play_reviews_fq.csv", index=False)

dig = pd.read_csv(f"{BASE}/nike_digital_growth_quarterly.csv").rename(columns={"fiscal_quarter": "fq"})
dig["fq"] = dig.fq.str.replace("FY20", "FY20", regex=False)
peers_us = ["adidas_app", "stockx", "goat", "footlocker", "dicks", "zappos", "champs"]
nk = q[(q.app == "nike_app") & (q.locale == "en_us")][["fq", "n_reviews", "yoy_pct"]].rename(columns={"yoy_pct": "nike_app_us_yoy"})
pe = q[(q.app.isin(peers_us)) & (q.locale == "en_us")].groupby("fq").agg(peer_n=("n_reviews", "sum"), peer_prev=("n_prev", "sum")).reset_index()
pe["peer_pool_yoy"] = (pe.peer_n / pe.peer_prev - 1) * 100
ad = q[(q.app == "adidas_app") & (q.locale == "en_us")][["fq", "yoy_pct"]].rename(columns={"yoy_pct": "adidas_app_us_yoy"})
intl = q[(q.app == "nike_app") & (q.locale != "en_us")].groupby("fq").agg(n=("n_reviews", "sum"), p=("n_prev", "sum")).reset_index()
intl["nike_app_de_fr_jp_yoy"] = (intl.n / intl.p - 1) * 100
alln = q[(q.app == "nike_app")].groupby("fq").agg(n=("n_reviews", "sum"), p=("n_prev", "sum")).reset_index()
alln["nike_app_all4_yoy"] = (alln.n / alln.p - 1) * 100
cal = dig.merge(nk, on="fq", how="left").merge(pe[["fq", "peer_pool_yoy"]], on="fq", how="left").merge(ad, on="fq", how="left") \
    .merge(intl[["fq", "nike_app_de_fr_jp_yoy"]], on="fq", how="left").merge(alln[["fq", "nike_app_all4_yoy"]], on="fq", how="left")
cal = cal.replace([np.inf, -np.inf], np.nan)
cal["nike_minus_peers_pp"] = cal.nike_app_us_yoy - cal.peer_pool_yoy
cal.to_csv(f"{BASE}/test_play_calibration.csv", index=False)
print(cal.drop(columns=["source", "basis"]).round(1).to_string())
c = cal.dropna(subset=["nike_app_us_yoy"])
for col in ["nike_app_us_yoy", "nike_minus_peers_pp", "nike_app_all4_yoy"]:
    cc = c.dropna(subset=[col])
    r = cc.nike_brand_digital_yoy_pct.corr(cc[col]); rs = cc.nike_brand_digital_yoy_pct.rank().corr(cc[col].rank())
    dd = cc[["nike_brand_digital_yoy_pct", col]].diff().dropna(); rd = dd.iloc[:, 0].corr(dd.iloc[:, 1])
    same = (np.sign(dd.iloc[:, 0]) == np.sign(dd.iloc[:, 1])).mean()
    post = cc[cc.fq >= "FY2023Q1"]; rp = post.nike_brand_digital_yoy_pct.corr(post[col])
    print(col, "n=", len(cc), "pearson r=", round(r, 2), "spearman=", round(rs, 2), "r(diffs)=", round(rd, 2), "same-direction share=", round(same, 2), "r FY23+=", round(rp, 2), "n FY23+=", len(post))
