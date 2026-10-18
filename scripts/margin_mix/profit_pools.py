"""Revenue mix and profit pools for NIKE, Inc. by region, channel, product and Jordan (FY2024, FY2026).
Every input is from data/nike_filing_facts.csv or data/nike_region_profitability.csv; outputs are DERIVED."""
import pandas as pd

d = pd.read_csv("data/nike_filing_facts.csv")
r = pd.read_csv("data/nike_region_profitability.csv")
ch = pd.read_csv("data/margin_mix/channel_gm_decomposition.csv")
def v(m, p):
    s = d[(d.metric == m) & (d.period == p)].value
    return float(s.iloc[0]) if len(s) else None

out = []
# 1. Regions: revenue and EBIT share of the five operating segments (segment EBIT before GBD and Corporate)
for fy in ["FY2024", "FY2026"]:
    x = r[r.period == fy].copy()
    x["rev_share"] = x.revenue_usd_m / x.revenue_usd_m.sum()
    x["ebit_share"] = x.ebit_usd_m / x.ebit_usd_m.sum()
    for _, row in x.iterrows():
        out.append(dict(period=fy, cut="region", item=row.segment, revenue_usd_m=row.revenue_usd_m,
                        rev_share=round(row.rev_share, 4), margin_pct=row.ebit_margin_pct, margin_type="segment EBIT",
                        profit_share=round(row.ebit_share, 4), basis="reported; shares DERIVED"))
    if fy == "FY2026":  # with-tariffs view: remove $965M (NA) and $21M (Converse) IEEPA recovery, FY26 10-K p. 30
        adj = {"north_america": 965, "converse": 21}
        x["ebit_ex"] = x.apply(lambda q: q.ebit_usd_m - adj.get(q.segment, 0), axis=1)
        for _, row in x.iterrows():
            out.append(dict(period="FY2026 ex tariff recovery", cut="region", item=row.segment,
                            revenue_usd_m=row.revenue_usd_m, rev_share=round(row.rev_share, 4),
                            margin_pct=round(100 * row.ebit_ex / row.revenue_usd_m, 1), margin_type="segment EBIT",
                            profit_share=round(row.ebit_ex / x.ebit_ex.sum(), 4), basis="DERIVED"))

# 2. Products: revenue share of NIKE Brand product revenue; GP share under Puma-style margin gaps
PUMA_GAP = {"apparel": 1.7, "equipment": 1.2}  # pts above footwear, Puma 2025 (and 2024 restated); range 1.2 to 2.4 in 2021-25
for fy, bgm in [("FY2024", None), ("FY2026", None)]:
    rev = {k: v(f"revenue_{k}", fy) for k in ["footwear", "apparel", "equipment"]}
    tot = sum(rev.values())
    brand_gm = ch[ch.period == fy].brand_gm.iloc[0] * 100 if fy in set(ch.period) else 42.94
    for gap_mult in (0, 1, 3):  # 0 = same margin, 1 = Puma gap, 3 = triple the Puma gap (stress)
        gaps = {"footwear": 0, "apparel": PUMA_GAP["apparel"] * gap_mult, "equipment": PUMA_GAP["equipment"] * gap_mult}
        f = brand_gm - sum(rev[k] / tot * gaps[k] for k in rev)
        gp = {k: rev[k] * (f + gaps[k]) / 100 for k in rev}
        for k in rev:
            out.append(dict(period=fy, cut=f"product (gap x{gap_mult})", item=k, revenue_usd_m=rev[k],
                            rev_share=round(rev[k] / tot, 4), margin_pct=round(f + gaps[k], 1),
                            margin_type="gross (ESTIMATE)", profit_share=round(gp[k] / sum(gp.values()), 4),
                            basis="revenue reported; margins ASSUMED from Puma gaps, calibrated to NIKE Brand GM"))

# 3. Jordan Direct share from reported vs wholesale-equivalent revenue (FY2023, FY2024)
for fy, rep, we in [("FY2023", v("revenue_jordan_reported_basis", "FY2023"), v("revenue_jordan_brand_wholesale_equivalent", "FY2023")),
                    ("FY2024", v("revenue_jordan_recast", "FY2024"), v("revenue_jordan", "FY2024"))]:
    c = ch[ch.period == fy].iloc[0]
    rdj = (rep - we) / (1 - 1 / c.markup_direct_over_w)
    sh = rdj / rep
    gm = sh * c.direct_gm + (1 - sh) * c.wholesale_gm
    out.append(dict(period=fy, cut="jordan", item="jordan_direct_share_est", revenue_usd_m=rep, rev_share=round(sh, 4),
                    margin_pct=round(100 * gm, 1), margin_type="gross, channel-mix only (ESTIMATE)",
                    profit_share=None, basis=f"DERIVED: (reported {rep:.0f} - WE {we:.0f}) / (1 - 1/{c.markup_direct_over_w}); brand Direct share {c.direct_share_rev:.3f}"))

o = pd.DataFrame(out)
o.to_csv("data/margin_mix/profit_pools.csv", index=False)
pd.set_option("display.width", 250)
print(o.drop(columns="basis").to_string())

# 4. Mix effects on gross margin, FY2024 to FY2026, holding FY2024 margins constant (DERIVED; effects overlap)
c24 = ch[ch.period == "FY2024"].iloc[0]
e26 = pd.read_csv("data/margin_mix/channel_gm_fy25_fy26_assumed.csv")
e26 = e26[(e26.period == "FY2026") & (e26.assumed_markup == 1.65)].iloc[0]
chan = (e26.direct_share_rev - c24.direct_share_rev) * (c24.direct_gm - c24.wholesale_gm) * 1e4
rg = r[r.period.isin(["FY2024", "FY2026"])].pivot(index="segment", columns="period", values="revenue_usd_m")
sh = rg / rg.sum()
gm24 = r[r.period == "FY2024"].set_index("segment").gross_margin_pct
reg = ((sh.FY2026 - sh.FY2024) * gm24).sum() * 100
p = {fy: {k: v(f"revenue_{k}", fy) for k in ["footwear", "apparel", "equipment"]} for fy in ["FY2024", "FY2026"]}
ps = {fy: {k: p[fy][k] / sum(p[fy].values()) for k in p[fy]} for fy in p}
prod = sum((ps["FY2026"][k] - ps["FY2024"][k]) * {"footwear": 0, "apparel": 1.7, "equipment": 1.2}[k] for k in ps["FY2026"]) * 100
print(f"\nFY24 to FY26 mix effects on gross margin (bps): channel {chan:.0f}, region {reg:.0f}, product (Puma gaps) {prod:.0f}")
print(f"NIKE Brand GM FY24 {c24.brand_gm:.4f} to FY26 {e26.brand_gm:.4f}: {(e26.brand_gm - c24.brand_gm) * 1e4:.0f} bps")
print(f"FY26 within-channel GMs at 1.65 markup: wholesale {e26.wholesale_gm:.4f} (FY24 {c24.wholesale_gm:.4f}), Direct {e26.direct_gm:.4f} (FY24 {c24.direct_gm:.4f})")
