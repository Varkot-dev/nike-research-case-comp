"""Solve NIKE Brand wholesale and Direct gross margin from the wholesale equivalent disclosure.

Identity (my derivation, labelled DERIVED in the note):
  NIKE Brand gross profit GP = g_w * R_w + (R_d - W * (1 - g_w))
  where R_w = wholesale revenue, R_d = NIKE Direct revenue, W = sales from wholesale operations to
  NIKE Direct at wholesale price (the "internal" line), g_w = gross margin earned at wholesale price.
  => g_w = (GP + W - R_d) / (R_w + W);  Direct GM = 1 - W * (1 - g_w) / R_d
Assumes product sold through Direct carries the same cost-to-wholesale-price ratio as product sold to
wholesale customers. Direct-only costs booked in cost of sales (e-commerce shipping) land in Direct GM.
"""
import pandas as pd

d = pd.read_csv("data/nike_filing_facts.csv")
def v(metric, fy):
    s = d[(d.metric == metric) & (d.period == fy)].value
    return float(s.iloc[0]) if len(s) else None

rows = []
for fy in ["FY2019", "FY2020", "FY2021", "FY2022", "FY2023", "FY2024"]:
    for conv_gm in (0.50, 0.54):  # Converse GM not disclosed before FY2023: bracket it
        cg = v("gross_margin_converse_pct", fy)
        cgm = cg / 100 if cg else conv_gm
        gp = v("gross_profit", fy) - v("revenue_converse", fy) * cgm
        rw, rd = v("revenue_wholesale", fy), v("revenue_nike_direct", fy)
        w = v("revenue_wholesale_to_nike_direct_internal", fy)
        we = rw + w
        gw = (gp + w - rd) / we
        gd = 1 - w * (1 - gw) / rd
        rows.append(dict(period=fy, converse_gm_used=round(cgm, 3), brand_gp=round(gp), wholesale_rev=rw,
                         direct_rev=rd, internal_w=w, markup_direct_over_w=round(rd / w, 3),
                         brand_gm=round(gp / (rw + rd), 4), wholesale_gm=round(gw, 4), direct_gm=round(gd, 4),
                         direct_share_rev=round(rd / (rw + rd), 4),
                         direct_share_gp=round(rd * gd / gp, 4)))
        if cg: break
out = pd.DataFrame(rows)
out.to_csv("data/margin_mix/channel_gm_decomposition.csv", index=False)
print(out.to_string())

# FY2025 and FY2026: Nike stopped disclosing the internal line, so W is ASSUMED from the FY2019 to FY2024
# Direct-over-wholesale-price markup range (1.649 to 1.776; 1.65 to 1.67 outside the FY2022 full-price peak).
ext = []
for fy in ["FY2025", "FY2026"]:
    gp = v("gross_profit", fy) - v("revenue_converse", fy) * v("gross_margin_converse_pct", fy) / 100
    rw, rd = v("revenue_wholesale", fy), v("revenue_nike_direct", fy)
    for mk in (1.60, 1.65, 1.70):
        w = rd / mk
        gw = (gp + w - rd) / (rw + w)
        gd = 1 - w * (1 - gw) / rd
        ext.append(dict(period=fy, assumed_markup=mk, brand_gp=round(gp), wholesale_rev=rw, direct_rev=rd,
                        brand_gm=round(gp / (rw + rd), 4), wholesale_gm=round(gw, 4), direct_gm=round(gd, 4),
                        direct_share_rev=round(rd / (rw + rd), 4), direct_share_gp=round(rd * gd / gp, 4)))
ext = pd.DataFrame(ext)
ext.to_csv("data/margin_mix/channel_gm_fy25_fy26_assumed.csv", index=False)
print(ext.to_string())
