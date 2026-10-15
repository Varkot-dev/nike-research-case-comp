"""Correlate Nike Inc AbnormalTone (Amazon, Nike fiscal quarters) with Nike revenue growth and NIKE Direct growth.
Reads repo data read-only: data/nike_filing_facts.csv (metric revenues, growth_nike_direct_reported_pct, revenue_nike_direct).
Usage: python3 -I fundamentals_test.py <reviews_data_dir> <repo_data_dir>"""
import sys, numpy as np, pandas as pd
from scipy import stats
D, REPO = sys.argv[1:3]
ff = pd.read_csv(f"{REPO}/nike_filing_facts.csv")
def series(metric):
    x = ff[(ff.metric == metric) & ff.period.str.match(r"^Q[1-4]FY\d{4}$")].drop_duplicates("period")
    return pd.Series(x.value.values, index=x.period.values)
rev = series("revenues"); dg = series("growth_nike_direct_reported_pct"); dr = series("revenue_nike_direct")
def key(p): return int(p[4:8]) * 10 + int(p[1])
def lab(k): return f"Q{k % 10}FY{k // 10}"
def shift(k, n):
    y, q = divmod(k, 10); q += n
    while q > 4: q -= 4; y += 1
    while q < 1: q += 4; y -= 1
    return y * 10 + q
R = {key(p): v for p, v in rev.items()}
fund = []
for k in sorted(R):
    prev = [R.get(shift(k, -j)) for j in range(1, 5)]
    yoy = R[k] / R[shift(k, -4)] - 1 if shift(k, -4) in R else np.nan
    abn = (R[k] - np.mean(prev)) / np.mean(prev) if all(v is not None for v in prev) else np.nan
    d = dg.get(lab(k), np.nan)
    if np.isnan(d) and lab(k) in dr and lab(shift(k, -4)) in dr and dr[lab(k)] > 100 and dr[lab(shift(k, -4))] > 100:
        d = 100 * (dr[lab(k)] / dr[lab(shift(k, -4))] - 1)
    fund.append(dict(qsort=k, quarter=lab(k), revenue=R[k], rev_yoy=yoy, abnormal_sales=abn, direct_yoy=d / 100 if not np.isnan(d) else np.nan))
fund = pd.DataFrame(fund).set_index("qsort")
a = pd.read_csv(f"{D}/amazon_quarterly_nike_fiscal.csv")
# last complete Nike fiscal quarter in the Amazon data is Q1FY2024 (Jun-Aug 2023); Q2FY2024 has only September 2023 and is dropped
a = a[a.qsort <= 20241]
firm = a[a.level == "firm"].pivot(index="qsort", columns="unit", values="AbnormalTone")
comp = [c for c in firm.columns if c != "Nike Inc"]
nike = a[(a.level == "firm") & (a.unit == "Nike Inc")].set_index("qsort")
X = pd.DataFrame({"AbnormalTone": nike.AbnormalTone, "Negative_AbnormalTone": nike.Negative_AbnormalTone,
                  "AbnormalTone_vader": nike.AbnormalTone_vader, "AbnormalTone_big": nike.AbnormalTone_big,
                  "AbnormalRating": nike.AbnormalRating, "AbnormalReviewCnt": nike.AbnormalReviewCnt,
                  "RelAbnormalTone": nike.AbnormalTone - firm[comp].mean(axis=1), "review_cnt": nike.review_cnt})
X.index = X.index.astype(int)
rows = []
for k in X.index:
    nxt = shift(k, 1)
    r = dict(qsort=k, quarter=lab(k), **X.loc[k].to_dict())
    for c in ("rev_yoy", "abnormal_sales", "direct_yoy"):
        r[c + "_q"] = fund[c].get(k, np.nan); r[c + "_q+1"] = fund[c].get(nxt, np.nan)
    rows.append(r)
P = pd.DataFrame(rows); P = P[P.qsort >= 20161]
P.to_csv(f"{D}/nike_tone_vs_fundamentals.csv", index=False, float_format="%.4f")
COVID = {20204, 20211, 20214}  # Q4FY2020 lockdown collapse and the base-effect rebound quarters
out = []
for x in ("AbnormalTone", "Negative_AbnormalTone", "RelAbnormalTone", "AbnormalTone_vader", "AbnormalTone_big", "AbnormalRating"):
    for y in ("rev_yoy_q+1", "abnormal_sales_q+1", "direct_yoy_q+1", "rev_yoy_q", "abnormal_sales_q", "direct_yoy_q"):
        for excl, end in ((False, 20241), (True, 20241), (False, 20233)):
            s = P[[x, y, "qsort"]].dropna(); s = s[s.qsort <= end]
            if excl: s = s[~s.qsort.isin(COVID) & ~s.qsort.isin({shift(c, -1) for c in COVID})]
            if len(s) < 5: continue
            pr = stats.pearsonr(s[x], s[y]); sr = stats.spearmanr(s[x], s[y])
            out.append(dict(x=x, y=y, excl_covid=excl, sample_end=lab(end), n=len(s), first=lab(int(s.qsort.min())), last=lab(int(s.qsort.max())),
                            pearson_r=pr[0], pearson_p=pr[1], spearman_rho=sr[0], spearman_p=sr[1]))
O = pd.DataFrame(out); O.to_csv(f"{D}/nike_tone_correlations.csv", index=False, float_format="%.4f")
print(O[O.x.isin(["AbnormalTone", "Negative_AbnormalTone", "RelAbnormalTone"])].to_string())
# multivariate in the spirit of Eq. (1), next-quarter abnormal sales, OLS with classic t-stats
s = P[["AbnormalTone", "AbnormalRating", "AbnormalReviewCnt", "abnormal_sales_q+1", "qsort"]].dropna()
Xm = np.column_stack([np.ones(len(s)), s[["AbnormalTone", "AbnormalRating", "AbnormalReviewCnt"]].values]); yv = s["abnormal_sales_q+1"].values
b, *_ = np.linalg.lstsq(Xm, yv, rcond=None); e = yv - Xm @ b; sig2 = e @ e / (len(s) - Xm.shape[1])
se = np.sqrt(np.diag(sig2 * np.linalg.inv(Xm.T @ Xm)))
pd.DataFrame(dict(term=["const", "AbnormalTone", "AbnormalRating", "AbnormalReviewCnt"], coef=b, t=b / se, n=len(s))).to_csv(f"{D}/nike_tone_ols_eq1_style.csv", index=False, float_format="%.4f")
print(pd.read_csv(f"{D}/nike_tone_ols_eq1_style.csv"))
