"""Tests on the cleaned attention data. Run: python3 -I analyze_tests.py <hunt_dir>
Writes test_*.csv tables into <hunt_dir> and prints the numbers used in the README.
"""
import os, sys
import numpy as np
import pandas as pd

H = sys.argv[1] if len(sys.argv) > 1 else ".."
P = lambda f: os.path.join(H, f)

# ------------------------------------------------------------------ Wikipedia
d = pd.read_csv(P("wiki_pageviews_daily_long.csv"), parse_dates=["date"])
# merge old and new titles of moved pages (views are per title; after a move, history stays under old title)
d["brand"] = d["label"].str.replace("_oldtitle", "", regex=False)
daily = d.groupby(["brand", "date"]).views.sum().unstack(0).fillna(0)
daily = daily[daily.index <= "2026-10-12"]

NIKE = ["nike_inc", "air_jordan"]
RIVALS = [c for c in ["adidas", "new_balance", "asics", "puma", "skechers", "hoka", "on_running", "brooks", "saucony",
                      "lululemon", "salomon", "under_armour", "deckers", "crocs"] if c in daily.columns]
RUN_RIVALS = [c for c in ["hoka", "on_running", "asics", "brooks", "saucony"] if c in daily.columns]
LIFE_N = [c for c in ["nike_dunk", "air_force_1", "air_max", "air_jordan"] if c in daily.columns]
LIFE_R = [c for c in ["adidas_samba", "adidas_gazelle"] if c in daily.columns]

wk = daily.resample("W-SUN").sum()
wk = wk[wk.index <= "2026-10-11"]
share = pd.DataFrame({
    "nike_share_vs_all_rivals_pct": 100 * wk[NIKE].sum(axis=1) / (wk[NIKE].sum(axis=1) + wk[RIVALS].sum(axis=1)),
    "nike_inc_vs_adidas_ratio": wk["nike_inc"] / wk["adidas"],
    "nike_inc_vs_run_rivals_ratio": wk["nike_inc"] / wk[RUN_RIVALS].sum(axis=1),
    "nike_lifestyle_vs_samba_gazelle_ratio": wk[LIFE_N].sum(axis=1) / wk[LIFE_R].sum(axis=1).replace(0, np.nan),
    "nike_family_views": wk[NIKE].sum(axis=1), "rivals_views": wk[RIVALS].sum(axis=1),
})
share.to_csv(P("test_wiki_weekly_nike_share.csv"))

m = daily.resample("MS").sum()
m = m[m.index <= "2026-09-01"]
ms = 100 * m[NIKE].sum(axis=1) / (m[NIKE].sum(axis=1) + m[RIVALS].sum(axis=1))
q = daily.resample("QS-DEC").sum()  # Nike fiscal quarters: Dec-Feb, Mar-May, Jun-Aug, Sep-Nov
qs = 100 * q[NIKE].sum(axis=1) / (q[NIKE].sum(axis=1) + q[RIVALS].sum(axis=1))
print("\n== Wikipedia (en) Nike family share of brand-article views, by month ==")
tab = pd.DataFrame({"share_pct": ms.round(2), "yoy_pp": (ms - ms.shift(12)).round(2)})
print(tab.loc["2024-01":].to_string())
tab.to_csv(P("test_wiki_monthly_nike_share.csv"))

# Pre-registered window: Jun 1 to Oct 11 2026 vs same days 2025
def window(a, b):
    x = daily.loc[a:b]
    n, r = x[NIKE].sum().sum(), x[RIVALS].sum().sum()
    return 100 * n / (n + r), x
s26, x26 = window("2026-06-01", "2026-10-11")
s25, x25 = window("2025-06-01", "2025-10-11")
s24, x24 = window("2024-06-01", "2024-10-11")
print(f"\nWindow Jun 1 to Oct 11: Nike share 2024 {s24:.2f}%  2025 {s25:.2f}%  2026 {s26:.2f}%  (YoY {s26 - s25:+.2f} pp)")
print("YoY change in views by brand, Jun 1 to Oct 11, 2026 vs 2025:")
yoy = (x26.sum() / x25.sum() - 1) * 100
print(yoy.reindex(NIKE + RIVALS + LIFE_N + LIFE_R + ["converse"]).round(1).to_string())
yoy.to_csv(P("test_wiki_window_yoy_by_article.csv"), header=["yoy_pct_jun1_oct11_2026_vs_2025"])

# Robustness: drop each rival in turn; and use medians of weekly shares
rob = {}
for r in RIVALS:
    rr = [c for c in RIVALS if c != r]
    f = lambda x: 100 * x[NIKE].sum().sum() / (x[NIKE].sum().sum() + x[rr].sum().sum())
    rob[r] = f(x26) - f(x25)
print("YoY pp when dropping one rival at a time: min %.2f max %.2f" % (min(rob.values()), max(rob.values())))
w26 = share.loc["2026-06-07":"2026-10-11", "nike_share_vs_all_rivals_pct"]
w25 = share.loc["2025-06-08":"2025-10-12", "nike_share_vs_all_rivals_pct"]
print(f"Weekly share medians: 2025 {w25.median():.2f}  2026 {w26.median():.2f}; weeks 2026 above 2025 median: {(w26 > w25.median()).sum()}/{len(w26)}")

# Other language editions
for lang, n, r in [("zh", "zh_nike", ["zh_adidas", "zh_anta", "zh_li_ning"]), ("de", "de_nike", ["de_adidas", "de_on", "de_hoka"]),
                   ("ja", "ja_nike", ["ja_adidas", "ja_asics"])]:
    cols = [c for c in [n] + r if c in daily.columns]
    if n not in daily.columns or len(cols) < 2:
        continue
    a = daily.loc["2026-06-01":"2026-10-11", cols].sum()
    b = daily.loc["2025-06-01":"2025-10-11", cols].sum()
    sa, sb = 100 * a[n] / a.sum(), 100 * b[n] / b.sum()
    print(f"{lang}.wikipedia Nike share vs {cols[1:]}: 2025 {sb:.1f}%  2026 {sa:.1f}%  ({sa - sb:+.1f} pp); Nike views YoY {100 * (a[n] / b[n] - 1):+.1f}%")

# Validation: does the Wikipedia share track Nike revenue? fiscal quarter YoY
ff = pd.read_csv(os.path.join(H, "raw", "repo_ref", "nike_filing_facts.csv"))
rev = ff[ff.metric == "revenues"].drop_duplicates("period").set_index("period").value
rev = rev[rev.index.str.match(r"^Q\dFY\d{4}$")]
def fq_start(p):
    qn, fy = int(p[1]), int(p[4:])
    start_month = {1: 6, 2: 9, 3: 12, 4: 3}[qn]
    year = fy - 1 if qn in (1, 2, 3) else fy
    return pd.Timestamp(year, start_month, 1)
rv = pd.Series({fq_start(p): v for p, v in rev.items()}).sort_index()
rv_yoy = (rv / rv.shift(4) - 1) * 100
qv = q[NIKE].sum(axis=1)
qshare = qs
val = pd.DataFrame({"rev_yoy_pct": rv_yoy, "wiki_share_yoy_pp": qshare - qshare.shift(4),
                    "wiki_nike_views_yoy_pct": (qv / qv.shift(4) - 1) * 100}).dropna()
val = val[val.index >= "2020-06-01"]
val.round(2).to_csv(P("test_wiki_vs_revenue_quarterly.csv"))
excl = val[(val.index < "2020-03-01") | (val.index > "2021-08-31")]  # drop COVID base effects
print("\nValidation, quarters since FY21Q1 excluding COVID base quarters through Aug 2021, n=%d" % len(excl))
print("corr(rev YoY, wiki share YoY pp) = %.2f; corr(rev YoY, wiki views YoY) = %.2f" % (
    excl.rev_yoy_pct.corr(excl.wiki_share_yoy_pp), excl.rev_yoy_pct.corr(excl.wiki_nike_views_yoy_pct)))
print(val.round(1).tail(10).to_string())

# ------------------------------------------------------------------ Lifestyle vs running (Wikipedia)
print("\n== Lifestyle and brand articles: YoY % over matched windows (same calendar days) ==")
WINS = [("FQ1 Jun-Aug", "06-01", "08-31"), ("Sep 1-Oct 11", "09-01", "10-11"), ("Dec-Feb", "12-01", "02-28"), ("Mar-May", "03-01", "05-31")]
cols = LIFE_N + LIFE_R + ["converse", "nike_inc", "adidas", "new_balance", "asics", "hoka", "on_running"]
cols = [c for c in cols if c in daily.columns]
rows = []
for y in (2024, 2025, 2026):
    for name, a, b in WINS:
        ya, yb = (y - 1, y) if name == "Dec-Feb" else (y, y)
        cur = daily.loc[f"{ya}-{a}":f"{yb}-{b}", cols].sum()
        prv = daily.loc[f"{ya - 1}-{a}":f"{yb - 1}-{b}", cols].sum()
        if pd.Timestamp(f"{yb}-{b}") > daily.index.max():
            continue
        rows.append(pd.Series((cur / prv - 1) * 100, name=f"{y} {name}"))
lt = pd.DataFrame(rows).round(1)
print(lt.to_string())
lt.to_csv(P("test_wiki_matched_window_yoy.csv"))

# ------------------------------------------------------------------ Tranco
t = pd.read_csv(P("tranco_rank_semimonthly_long.csv"), parse_dates=["date"])
pv = t.pivot_table(index="date", columns="domain", values="rank")
peers = [c for c in ["adidas.com", "newbalance.com", "asics.com", "lululemon.com", "puma.com", "skechers.com",
                     "underarmour.com"] if c in pv.columns]
lr = np.log(pv["nike.com"]) - np.log(pv[peers]).mean(axis=1)
tt = pd.DataFrame({"nike_rank": pv["nike.com"], "peer_geomean_rank": np.exp(np.log(pv[peers]).mean(axis=1)),
                   "log_rank_gap": lr, "hoka_rank": pv.get("hoka.com"), "on_rank": pv.get("on.com")})
tt.to_csv(P("test_tranco_nike_vs_peers.csv"))
yr = tt.groupby(tt.index.year)[["nike_rank", "peer_geomean_rank", "log_rank_gap"]].median()
print("\n== Tranco: Nike rank vs peer geometric mean rank (lower rank = more traffic; more negative gap = Nike further ahead) ==")
print(yr.round(3).to_string())
print(tt.loc["2025-06-01":].round(3).to_string())

# ------------------------------------------------------------------ Reddit mention shares
r = pd.read_csv(P("reddit_title_mentions_monthly_sample.csv"))
r["month"] = pd.to_datetime(r["month"])
def period(mo):
    if mo < pd.Timestamp("2023-01-01"):
        return f"{mo.year}"
    if mo < pd.Timestamp("2025-01-01"):
        return f"{mo.year}"
    return f"{mo.year}H{1 if mo.month <= 6 else 2}"
r["period"] = r["month"].map(period)
SETS = {
    "RunningShoeGeeks": (["nike", "nike_run_any"], ["hoka", "asics", "on", "saucony", "brooks", "adidas", "adizero", "new_balance", "puma"]),
    "Sneakers": (["nike", "jordan", "dunk", "af1", "air_max"], ["adidas", "samba", "gazelle", "new_balance", "asics", "onitsuka", "salomon", "puma", "converse"]),
}
out = []
for sub, (nk, rv) in SETS.items():
    x = r[r.subreddit == sub]
    if x.empty:
        continue
    piv = x.pivot_table(index=["period", "month"], columns="term", values="posts_mentioning", aggfunc="sum")
    tot = x.groupby(["period", "month"]).posts_total.first()
    # Nike side: posts counted per term may double count (e.g. 'nike pegasus' hits nike and nike_run_any); use max as a floor
    nike_m = piv[nk].max(axis=1)
    riv_m = piv[rv].sum(axis=1)
    g = pd.DataFrame({"nike": nike_m, "rivals": riv_m, "posts": tot}).groupby(level=0).sum()
    g["nike_share_of_brand_mentions_pct"] = 100 * g.nike / (g.nike + g.rivals)
    nn = g.nike + g.rivals
    p_ = g.nike / nn
    g["ci95_pp"] = 100 * 1.96 * np.sqrt(p_ * (1 - p_) / nn)
    g["nike_posts_per_100_titles"] = 100 * g.nike / g.posts
    g["subreddit"] = sub
    out.append(g.reset_index())
    print(f"\n== Reddit r/{sub}: Nike share of brand mentions in post titles (first 7 days of sampled months) ==")
    print(g.round(2).to_string())
    # Running models split
    if sub == "RunningShoeGeeks":
        mm = x.pivot_table(index="period", columns="term", values="posts_mentioning", aggfunc="sum")
        tt_ = x.groupby("period").apply(lambda z: z.groupby("month").posts_total.first().sum())
        print("Model mentions per 1,000 titles:")
        print((1000 * mm[["pegasus", "vomero", "vaporfly", "alphafly", "hoka", "asics", "on", "saucony", "adizero"]].div(tt_, axis=0)).round(1).to_string())
if out:
    pd.concat(out).to_csv(P("test_reddit_nike_mention_share.csv"), index=False)
