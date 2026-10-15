"""G3 smoking-gun hunt: unit volumes, ASP and factory base. Builds the CSVs in
research_notes/Smoking gun hunt/ (prefix G3_). Run: python3 -I scripts/hunt_g3_build.py

Hard-coded inputs below were read from the cited 10-K / Impact Report pages (see the 'src' columns);
file-based inputs come from the repo (Yue Yuen, US HS6 imports, Nike map snapshot) and from the
FY21 third-party copy of the Nike Manufacturing Map saved next to the outputs."""
import csv, collections, itertools, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "research_notes", "Smoking gun hunt")

def w(name, rows, cols):
    with open(os.path.join(OUT, name), "w", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=cols); wr.writeheader()
        for r in rows: wr.writerow({c: r.get(c, "") for c in cols})

# ---------------------------------------------------------------- 1. annual units / ASP (10-K MD&A, NIKE Brand)
# fy: (units_pct, asp_pts, cn_growth_pct, revenue_usd_m, reported_growth_pct, src)
FW = {
 2015: (9, 8, 17, 18318, 13, "FY16 10-K p. 24 (units, ASP); p. 23 (revenue, growth)"),
 2016: (9, 6, 15, 19871, 8, "FY16 10-K p. 24; p. 23"),
 2017: (7, 1, 8, 21081, 6, "FY17 10-K p. 24; p. 23"),
 2018: (2, 2, 4, 22268, 6, "FY18 10-K p. 23; p. 22"),
 2019: (8, 4, 12, 24222, 9, "FY19 10-K p. 28; p. 27"),
 2020: (-8, 6, -2, 23305, -4, "FY20 10-K p. 32; p. 31"),
 2021: (11, 7, 18, 28021, 20, "FY21 10-K p. 33; p. 32"),
 2022: (-3, 7, 4, 29143, 4, "FY22 10-K p. 33; p. 32"),
 2023: (13, 7, 20, 33135, 14, "FY23 10-K p. 33; p. 32"),
 2024: (-2, 3, 1, 33427, 1, "FY24 10-K p. 35; p. 34"),
 2025: (-8, -3, -11, 29510, -12, "FY25 10-K p. 34; p. 33"),
 2026: (-1, -1, -2, 29525, 0, "FY26 10-K p. 33; p. 32"),
}
AP = {
 2015: (8, 2, 10, 8637, 7, "FY16 10-K p. 24; p. 23"),
 2016: (7, 4, 11, 9067, 5, "FY16 10-K p. 24 (units); ASP DERIVED as cn growth minus units; p. 23"),
 2017: (6, 3, 9, 9654, 6, "FY17 10-K p. 24; p. 23"),
 2018: (4, 5, 9, 10733, 11, "FY18 10-K p. 23; p. 22"),
 2019: (6, 5, 11, 11550, 8, "FY19 10-K p. 28; p. 27"),
 2020: (-8, 5, -3, 10953, -5, "FY20 10-K p. 32; p. 31"),
 2021: (14, 1, 15, 12865, 17, "FY21 10-K p. 33; p. 32"),
 2022: (0, 6, 6, 13567, 5, "FY22 10-K p. 33; p. 32"),
 2023: (4, 4, 8, 13843, 2, "FY23 10-K p. 33; p. 32"),
 2024: (-9, 9, 0, 13775, 0, "FY24 10-K p. 35; p. 34"),
 2025: (-5, 0, -5, 12965, -6, "FY25 10-K p. 34; p. 33"),
 2026: (1, 1, 2, 13449, 4, "FY26 10-K p. 33; p. 32"),
}

def chain(d, key_idx, base_fy, delta=0.0):
    """index (base_fy = 100) from growth rates; delta shifts every year's growth by +/-delta pts (rounding band)."""
    idx = {base_fy: 100.0}
    for fy in sorted(d):
        if fy > base_fy:
            idx[fy] = idx[fy - 1] * (1 + (d[fy][key_idx] + delta) / 100.0)
    for fy in sorted(d, reverse=True):
        if fy <= base_fy and fy > min(d):
            pass
    return idx

def level_series(d, base_fy):
    """units, cn revenue and reported revenue indices over all fiscal years, base_fy=100 (FY15 is first level)."""
    fys = sorted(d)
    first = fys[0]
    u = {first: 1.0}; c = {first: 1.0}
    for fy in fys[1:]:
        u[fy] = u[fy - 1] * (1 + d[fy][0] / 100.0)
        c[fy] = c[fy - 1] * (1 + d[fy][2] / 100.0)
    b_u, b_c = u[base_fy], c[base_fy]
    return ({fy: 100 * u[fy] / b_u for fy in fys}, {fy: 100 * c[fy] / b_c for fy in fys})

def band(d, a, b):
    """cumulative units change a->b with worst-case +/-0.5 pt rounding on every year (lo, hi)."""
    lo = hi = 1.0; mid = 1.0
    for fy in range(a + 1, b + 1):
        u = d[fy][0]
        mid *= 1 + u / 100; lo *= 1 + (u - 0.5) / 100; hi *= 1 + (u + 0.5) / 100
    return (lo - 1) * 100, (mid - 1) * 100, (hi - 1) * 100

PRIOR = {"Footwear": 16208, "Apparel": 8109}  # FY14 NIKE Brand revenue, FY16 10-K p. 23
rows = []
for prod, d in (("Footwear", FW), ("Apparel", AP)):
    u19, c19 = level_series(d, 2019); u23, c23 = level_series(d, 2023)
    for fy in sorted(d):
        u, asp, cn, rev, rep, src = d[fy]
        first = fy == 2015
        rows.append({
          "product": prod, "fiscal_year": f"FY{fy}", "units_yoy_pct": u, "asp_contrib_pts": asp,
          "cn_revenue_growth_pct": cn, "check_units_plus_asp_minus_cn": (u + asp - cn),
          "nike_brand_revenue_usd_m": rev,
          "reported_revenue_growth_pct": round(100 * (rev / (d[fy - 1][3] if fy - 1 in d else PRIOR[prod]) - 1), 1),
          "units_index_FY19_100": round(u19[fy], 1), "cn_revenue_index_FY19_100": round(c19[fy], 1),
          "reported_revenue_index_FY19_100": round(100 * rev / d[2019][3], 1),
          "asp_cn_index_FY19_100": round(100 * c19[fy] / u19[fy], 1),
          "reported_rev_per_unit_index_FY19_100": round((100 * rev / d[2019][3]) / (u19[fy] / 100), 1),
          "units_index_FY23_100": round(u23[fy], 1),
          "reported_revenue_index_FY23_100": round(100 * rev / d[2023][3], 1),
          "reported_rev_per_unit_index_FY23_100": round((100 * rev / d[2023][3]) / (u23[fy] / 100), 1),
          "src": src, "tag": "OPENED (growth %, revenue); DERIVED (indices)",
        })
cols = list(rows[0].keys())
w("G3_nike_units_asp_annual.csv", rows, cols)

# windows
win = []
for prod, d in (("Footwear", FW), ("Apparel", AP)):
    for a, b in ((2019, 2023), (2023, 2026), (2019, 2026), (2024, 2026), (2025, 2026), (2015, 2026), (2021, 2026), (2019, 2024)):
        lo, mid, hi = band(d, a, b)
        rev = 100 * (d[b][3] / d[a][3] - 1)
        cnv = 1.0
        for fy in range(a + 1, b + 1): cnv *= 1 + d[fy][2] / 100
        uv = 1 + mid / 100
        win.append({"product": prod, "window": f"FY{a} to FY{b}", "units_change_pct_low": round(lo, 1), "units_change_pct": round(mid, 1),
                    "units_change_pct_high": round(hi, 1), "reported_revenue_change_pct": round(rev, 1),
                    "cn_revenue_change_pct": round((cnv - 1) * 100, 1),
                    "reported_rev_per_unit_change_pct": round(((1 + rev / 100) / uv - 1) * 100, 1),
                    "cn_asp_change_pct": round((cnv / uv - 1) * 100, 1),
                    "verdict": (lambda apc, um: ("units " + ("down" if um < -1 else "up" if um > 1 else "flat") + "; revenue per unit " +
                                ("up" if apc > 2 else "down" if apc < -2 else "about flat")))(((1 + rev / 100) / uv - 1) * 100, mid),
                    "tag": "DERIVED from G3_nike_units_asp_annual.csv; units band = +/-0.5 pt rounding per year"})
w("G3_nike_units_windows.csv", win, list(win[0].keys()))

# ---------------------------------------------------------------- 2. quarterly footwear units (10-Q MD&A, 3-month)
Q = [  # quarter, units, asp_pts, cn_rev_growth, 10-Q printed page
 ("Q1 FY23", 3, 9, 12, "Q1 FY23 10-Q (Aug 31 2022) p. 24"),
 ("Q2 FY23", 28, 8, 36, "Q2 FY23 10-Q (Nov 30 2022) p. 27"),
 ("Q3 FY23", 19, 6, 25, "Q3 FY23 10-Q (Feb 28 2023) p. 28"),
 ("Q1 FY24", -1, 5, 4, "Q1 FY24 10-Q (Aug 31 2023) p. 24"),
 ("Q2 FY24", -6, 6, 0, "Q2 FY24 10-Q (Nov 30 2023) p. 27"),
 ("Q3 FY24", 2, 1, 3, "Q3 FY24 10-Q (Feb 29 2024) p. 28"),
 ("Q1 FY25", -10, 0, -10, "Q1 FY25 10-Q (Aug 31 2024) p. 22"),
 ("Q2 FY25", -7, -5, -12, "Q2 FY25 10-Q (Nov 30 2024) p. 25"),
 ("Q3 FY25", -8, -1, -9, "Q3 FY25 10-Q (Feb 28 2025) p. 27"),
 ("Q1 FY26", 2, -4, -2, "Q1 FY26 10-Q (Aug 31 2025) p. 22"),
 ("Q2 FY26", 0, -1, -1, "Q2 FY26 10-Q (Nov 30 2025) p. 26"),
 ("Q3 FY26", -2, 1, -1, "Q3 FY26 10-Q (Feb 28 2026) p. 29"),
 ("Q1 FY27", -5, -1, -6, "Q1 FY27 10-Q (Aug 31 2026) p. 23"),
]
w("G3_nike_footwear_units_quarterly.csv",
  [{"quarter": q, "units_yoy_pct": u, "asp_contrib_pts": a, "nike_brand_footwear_cn_growth_pct": g, "src": s,
    "note": "Q4 quarters are not in any 10-Q; a Q4 split would have to be derived from FY minus 9M percentages and is not reliable at integer rounding",
    "tag": "OPENED"} for q, u, a, g, s in Q],
  ["quarter", "units_yoy_pct", "asp_contrib_pts", "nike_brand_footwear_cn_growth_pct", "src", "note", "tag"])

# ---------------------------------------------------------------- 3. workers by region, factory counts
W = {  # FY: Americas, EMEA, N Asia, S Asia, SE Asia  (source base FY15-FY20; Tier 1 from FY21)
 "FY15": (87234, 17197, 236142, 287862, 386293, "source base (Tier 1 + related)", "FY19 Impact Report p. 28 table"),
 "FY16": (71904, 18674, 233561, 304932, 436970, "source base", "FY19 Impact Report p. 28; FY16/17 SBR"),
 "FY17": (77833, 18396, 198877, 296984, 444907, "source base", "FY19 Impact Report p. 28; FY16/17 SBR"),
 "FY18": (72986, 19114, 170724, 286938, 473258, "source base", "FY19 Impact Report p. 28; FY18 Impact Report"),
 "FY19": (70835, 22128, 153645, 292481, 513023, "source base", "FY19 Impact Report p. 28"),
 "FY20": (67626, 32782, 166730, 322704, 563357, "source base", "FY20 Impact Report p. 29"),
 "FY21": (63115, 25948, 115416, 269240, 507010, "Tier 1", "FY21 Impact Report p. 150 (PDF)"),
 "FY22": (59722, 32428, 113272, 380730, 541811, "Tier 1", "FY22 Impact Report p. 83 (PDF)"),
 "FY23": (56985, 35240, 107104, 391285, 542660, "Tier 1", "FY23 Impact Report p. 68 (PDF)"),
 "FY24": (54906, 34065, 102621, 364662, 539465, "Tier 1", "FY24 Sustainability Data p. 7"),
 "FY25": (59725, 33751, 100278, 391823, 520836, "Tier 1", "FY25 Sustainability Data p. 7"),
}
wr = []
for fy, (a, e, n, s, se, basis, src) in W.items():
    wr.append({"fiscal_year": fy, "basis": basis, "americas": a, "emea": e, "n_asia": n, "s_asia": s, "se_asia": se,
               "total": a + e + n + s + se, "src": src, "tag": "OPENED (total DERIVED as sum)"})
w("G3_workers_by_region_year.csv", wr, ["fiscal_year", "basis", "americas", "emea", "n_asia", "s_asia", "se_asia", "total", "src", "tag"])

FC = {  # fy: footwear, fw_countries, apparel, ap_countries, 10-K page
 2016: (142, 15, 394, 39, "FY16 10-K p. 3"), 2017: (127, 15, 363, 37, "FY17 10-K p. 3"), 2018: (124, 13, 328, 37, "FY18 10-K p. 3"),
 2019: (112, 12, 334, 36, "FY19 10-K p. 4"), 2020: (122, 12, 329, 38, "FY20 10-K p. 3"), 2021: (191, 14, 344, 33, "FY21 10-K p. 3 (older definition)"),
 2022: (120, 11, 279, 33, "FY22 10-K p. 4 (finished goods contract factories)"), 2023: (123, 11, 291, 31, "FY23 10-K p. 3"),
 2024: (96, 11, 285, 33, "FY24 10-K p. 3"), 2025: (97, 11, 303, 34, "FY25 10-K p. 3"), 2026: (95, 11, 321, 34, "FY26 10-K p. 3"),
}
fu19, _ = level_series(FW, 2019)
fr = []
for fy, (f, fc, a, ac, src) in FC.items():
    fr.append({"fiscal_year": f"FY{fy}", "footwear_factories": f, "footwear_countries": fc, "apparel_factories": a, "apparel_countries": ac,
               "footwear_units_index_FY19_100": round(fu19[fy], 1) if fy in fu19 else "",
               "footwear_units_per_factory_index_FY19_100": round(fu19[fy] / (f / FC[2019][0]), 1) if fy in fu19 else "",
               "src": src, "tag": "OPENED (counts); DERIVED (indices)"})
w("G3_factory_counts_10k.csv", fr, list(fr[0].keys()))

# Tier 1 supplier counts and Nike-reported contract factory counts in Impact Reports
IR = [("FY15", "contract factories", 692, "FY14/15 SBR p. 54 (PDF): 692 contract factories, 42 countries, over 1 million workers"),
      ("FY18", "contract factories", 542, "FY18 Impact Report p. 30 (PDF)"),
      ("FY19", "contract factories", 525, "FY19 Impact Report p. 27 (PDF)"),
      ("FY20", "contract factories", 518, "FY20 Impact Report p. 28 (PDF)"),
      ("FY23", "Tier 1 suppliers (SASB)", 454, "FY23 Impact Report SASB index CG-AA-000.A"),
      ("FY24", "Tier 1 suppliers (SASB)", 454, "FY24 Sustainability Data p. 51 (CG-AA-000.A)"),
      ("FY25", "Tier 1 suppliers (SASB)", 482, "FY25 Sustainability Data p. 50 (CG-AA-000.A); 184 Tier 2 in scope of target"),
      ("Oct 2026", "Tier 1 facilities on Manufacturing Map", 506, "data/hunt/trade_imports/nike_factory_map_2026-10-14.csv (Tier 1/ATL)")]
w("G3_factory_counts_impact_reports.csv", [{"period": p, "measure": m, "count": c, "src": s, "tag": "OPENED"} for p, m, c, s in IR],
  ["period", "measure", "count", "src", "tag"])

# ---------------------------------------------------------------- 4. map snapshots: FY21 third-party copy vs Oct 2026
def n(x):
    try: return int(str(x).replace(",", ""))
    except Exception: return 0
snap21 = list(csv.DictReader(open(os.path.join(OUT, "G3_map_snapshot_FY21_thirdparty_copy.csv"))))
snap26 = list(csv.DictReader(open(os.path.join(ROOT, "data/hunt/trade_imports/nike_factory_map_2026-10-14.csv"))))
agg = collections.defaultdict(lambda: {"n21": 0, "w21": 0, "n26": 0, "w26": 0})
for x in snap21:
    if x["Factory Type"] == "MATERIALS": continue  # Tier 2 materials carry no worker counts in the 2021 copy
    k = (x["Country/Region"], x["Product Type"].title()); agg[k]["n21"] += 1; agg[k]["w21"] += n(x["Total Workers"])
for x in snap26:
    if not x["factory_tier"].startswith("Tier 1"): continue
    k = (x["country/region"], x["product_type"]); agg[k]["n26"] += 1; agg[k]["w26"] += n(x["workers"])
rows = []
for (c, p), v in sorted(agg.items(), key=lambda kv: -(kv[1]["w26"] + kv[1]["w21"])):
    rows.append({"country": c, "product_type": p, "factories_FY21": v["n21"], "workers_FY21": v["w21"], "factories_Oct2026": v["n26"],
                 "workers_Oct2026": v["w26"], "workers_change": v["w26"] - v["w21"],
                 "workers_change_pct": round(100 * (v["w26"] / v["w21"] - 1), 1) if v["w21"] else ""})
w("G3_map_by_country_product_FY21_vs_Oct2026.csv", rows, list(rows[0].keys()))
prod = collections.defaultdict(lambda: [0, 0, 0, 0])
for r in rows:
    p = prod[r["product_type"]]; p[0] += r["factories_FY21"]; p[1] += r["workers_FY21"]; p[2] += r["factories_Oct2026"]; p[3] += r["workers_Oct2026"]
pr = [{"product_type": k, "factories_FY21": v[0], "workers_FY21": v[1], "factories_Oct2026": v[2], "workers_Oct2026": v[3],
       "workers_change_pct": round(100 * (v[3] / v[1] - 1), 1)} for k, v in prod.items()]
w("G3_map_by_product_FY21_vs_Oct2026.csv", pr, list(pr[0].keys()))

# ---------------------------------------------------------------- 5. Impact Report physical proxies FY20-FY25 (metric tons)
P = {
 "fw_mfg_waste_total_t": [110733, 102553, 109144, 118411, 115489, 115182],
 "rubber_use_t": [76141, 78896, 94494, 98169, 111358, 84456],
 "eva_foam_use_t": [61053, 53055, 44523, 38493, 37588, 33953],
 "leather_use_t": [51646, 60502, 65870, 66468, 70832, 62546],
 "polyester_use_t": [195490, 166343, 180645, 172412, 183619, 176172],
 "cotton_use_t": [113615, 115543, 142113, 116913, 125286, 120457],
 "tier1_fw_scope3_tco2e_focus": [1388826, 1411754, 1469481, 1397345, 1034093, 755426],
 "waste_per_unit_g": [292.4, 274.6, 269.4, 268.5, 260.1, 262],
 "textile_dyeing_freshwater_ML": [20609, 19338, 21233, 18569, 18021, 17853],
}
yrs = ["FY20", "FY21", "FY22", "FY23", "FY24", "FY25"]
unit_fw = {"FY21": 11, "FY22": -3, "FY23": 13, "FY24": -2, "FY25": -8}
pr = []
for k, v in P.items():
    for i, y in enumerate(yrs):
        yoy = round(100 * (v[i] / v[i - 1] - 1), 1) if i else ""
        pr.append({"metric": k, "fiscal_year": y, "value": v[i], "yoy_pct": yoy,
                   "nike_footwear_units_yoy_pct_10k": unit_fw.get(y, ""),
                   "src": "FY25 Sustainability Data (FY20-FY25 columns); waste p. 29, materials p. 11, Scope 3 p. 22, waste/unit p. 6; FY25 waste/unit printed as 262 (rounded)",
                   "tag": "OPENED"})
w("G3_impact_report_physical_proxies.csv", pr, ["metric", "fiscal_year", "value", "yoy_pct", "nike_footwear_units_yoy_pct_10k", "src", "tag"])
# correlation of each proxy yoy with 10-K footwear units yoy, FY21-FY25
def corr(a, b):
    n_ = len(a); ma = sum(a) / n_; mb = sum(b) / n_
    sa = sum((x - ma) ** 2 for x in a) ** .5; sb = sum((x - mb) ** 2 for x in b) ** .5
    return sum((x - ma) * (y - mb) for x, y in zip(a, b)) / (sa * sb)
cr = []
ux = [unit_fw[y] for y in yrs[1:]]
for k, v in P.items():
    yo = [100 * (v[i] / v[i - 1] - 1) for i in range(1, 6)]
    cr.append({"proxy": k, "n_years": 5, "corr_yoy_vs_10k_footwear_units_yoy": round(corr(yo, ux), 2),
               "same_sign_years_of_5": sum(1 for a, b in zip(yo, ux) if (a > 0) == (b > 0)), "tag": "DERIVED"})
w("G3_proxy_vs_10k_units_correlation.csv", cr, list(cr[0].keys()))

# ---------------------------------------------------------------- 6. supplier and official-statistics cross-checks
yy = {r["period_label"]: r for r in csv.DictReader(open(os.path.join(ROOT, "data/definitive/suppliers/yueyuen_pairs_asp_cumulative.csv")))}
def yyv(lbl): return float(yy[lbl]["pairs_m"])
def yy_nikefy(fy):  # 12 months ending June of calendar year fy: FY(t-1) + 6M(t) - 6M(t-1)
    return yyv(f"FY{fy-1}") + yyv(f"6M{fy}") - yyv(f"6M{fy-1}")
rows = []
for fy in range(2016, 2027):
    try: rows.append((fy, yy_nikefy(fy)))
    except KeyError: pass
yyd = dict(rows)
cc = []
for fy in sorted(yyd):
    if fy - 1 in yyd and fy in FW:
        cc.append({"nike_fy": f"FY{fy}", "yue_yuen_pairs_m_12m_to_June_all_brands": round(yyd[fy], 1),
                   "yue_yuen_pairs_yoy_pct": round(100 * (yyd[fy] / yyd[fy - 1] - 1), 1),
                   "nike_brand_footwear_units_yoy_pct_10k": FW[fy][0],
                   "gap_pts_yy_minus_nike": round(100 * (yyd[fy] / yyd[fy - 1] - 1) - FW[fy][0], 1),
                   "src": "data/definitive/suppliers/yueyuen_pairs_asp_cumulative.csv (HKEX results, VERIFIED quotes) and Nike 10-K MD&A",
                   "tag": "DERIVED; Yue Yuen definition changed from 'produced' to 'shipped' in 2019 and covers all brands (Nike is one of five named)"})
w("G3_yueyuen_vs_nike_units.csv", cc, list(cc[0].keys()))

hs = list(csv.DictReader(open(os.path.join(ROOT, "data/hunt/trade_imports/us_imports_hs6_athletic_monthly.csv"))))
def nfy(m):
    y, mo = int(m[:4]), int(m[5:7]); return y + 1 if mo >= 6 else y
ag = collections.defaultdict(lambda: [0.0, 0.0, set()])
for x in hs:
    if x["hs"] in ("640411", "640219"):
        k = (x["partner"], nfy(x["month"])); ag[k][0] += float(x["value_usd"] or 0); ag[k][1] += float(x["qty"] or 0); ag[k][2].add(x["month"])
us = []
for p in ("World", "Vietnam", "Indonesia", "China"):
    for fy in (2024, 2025, 2026):
        v = ag[(p, fy)]
        if len(v[2]) == 12:
            prev = ag.get((p, fy - 1));
            us.append({"origin": p, "nike_fy_window_jun_may": f"FY{fy}", "us_sports_footwear_pairs_m_640411_plus_640219": round(v[1] / 1e6, 1),
                       "value_usd_m": round(v[0] / 1e6, 0), "unit_value_usd_per_pair": round(v[0] / v[1], 2),
                       "pairs_yoy_pct": round(100 * (v[1] / prev[1] - 1), 1) if prev and len(prev[2]) == 12 else "",
                       "src": "data/hunt/trade_imports/us_imports_hs6_athletic_monthly.csv (UN Comtrade, US Census data), all brands, US only",
                       "tag": "DERIVED"})
w("G3_us_sports_footwear_import_pairs.csv", us, list(us[0].keys()))

SH = {2019: (49, 21, 23), 2020: (50, 24, 22), 2021: (51, 24, 21), 2022: (44, 30, 20), 2023: (50, 27, 18),
      2024: (50, 27, 18), 2025: (51, 28, 17), 2026: (52, 27, 16)}
CS = {2019: "FY19 10-K p. 3", 2020: "FY20 10-K p. 3", 2021: "FY21 10-K p. 3", 2022: "FY22 10-K p. 3", 2023: "FY23 10-K p. 3",
      2024: "FY24 10-K p. 3", 2025: "FY25 10-K p. 3", 2026: "FY26 10-K p. 3"}
cp = []
for fy, (vn, idn, cn_) in SH.items():
    u = fu19[fy]
    cp.append({"fiscal_year": f"FY{fy}", "vietnam_share_pct": vn, "indonesia_share_pct": idn, "china_share_pct": cn_,
               "other_share_pct_DERIVED": 100 - vn - idn - cn_, "footwear_units_index_FY19_100": round(u, 1),
               "vietnam_pairs_index": round(u * vn / 100, 1), "indonesia_pairs_index": round(u * idn / 100, 1),
               "china_pairs_index": round(u * cn_ / 100, 1), "other_pairs_index": round(u * (100 - vn - idn - cn_) / 100, 1),
               "src": CS[fy], "tag": "OPENED (shares, rounded to 1 pt); DERIVED (index = share x units index, FY19 total = 100)"})
w("G3_footwear_pairs_index_by_country.csv", cp, list(cp[0].keys()))

# ---------------------------------------------------------------- 7. footwear units by region (10-K MD&A, NIKE Brand regions)
REG_REV = {  # fy: NA, EMEA, GC, APLA footwear revenue $m (sum = NIKE Brand footwear)
 2023: (14897, 8260, 5435, 4543), 2024: (14537, 8473, 5552, 4865), 2025: (12684, 7569, 4805, 4452), 2026: (13317, 7643, 4188, 4377)}
REG_U = {  # fy: units %, ASP pts for NA, EMEA, GC, APLA
 2024: ((-7, 5), (-4, 5), (8, -2), (6, 1)), 2025: ((-10, -3), (-8, -2), (-11, -2), (-2, -2)), 2026: ((6, -1), (-2, -3), (-14, -1), (-3, 0))}
REG_SRC = {2024: "FY24 10-K pp. 38-42", 2025: "FY25 10-K pp. 37-41", 2026: "FY26 10-K pp. 37-40"}
names = ("North America", "EMEA", "Greater China", "APLA")
rr = []
cum = {nm: 1.0 for nm in names}
for fy in (2024, 2025, 2026):
    prev = REG_REV[fy - 1]; tot = sum(prev)
    contrib_total = 0.0
    for i, nm in enumerate(names):
        u, a = REG_U[fy][i]
        cum[nm] *= 1 + u / 100
        c = u * prev[i] / tot; contrib_total += c
        rr.append({"fiscal_year": f"FY{fy}", "region": nm, "units_yoy_pct": u, "asp_contrib_pts": a, "cn_growth_check_pct": u + a,
                   "prior_year_footwear_rev_usd_m": prev[i], "prior_year_rev_weight_pct": round(100 * prev[i] / tot, 1),
                   "contribution_to_total_units_pts_DERIVED": round(c, 2), "cum_units_index_FY23_100": round(100 * cum[nm], 1),
                   "src": REG_SRC[fy], "tag": "OPENED (units, ASP, revenue); DERIVED (weights = prior-year revenue share, an approximation because ASP differs by region)"})
    rr.append({"fiscal_year": f"FY{fy}", "region": "Total NIKE Brand (weighted sum)", "units_yoy_pct": FW[fy][0], "contribution_to_total_units_pts_DERIVED": round(contrib_total, 2),
               "src": REG_SRC[fy], "tag": "weighted sum vs reported total units %; difference is weighting and rounding error"})
w("G3_footwear_units_by_region.csv", rr, ["fiscal_year", "region", "units_yoy_pct", "asp_contrib_pts", "cn_growth_check_pct", "prior_year_footwear_rev_usd_m",
  "prior_year_rev_weight_pct", "contribution_to_total_units_pts_DERIVED", "cum_units_index_FY23_100", "src", "tag"])
yo = [r["yue_yuen_pairs_yoy_pct"] for r in cc]; nu = [r["nike_brand_footwear_units_yoy_pct_10k"] for r in cc]
print("YY vs Nike units corr", round(corr(yo, nu), 2), "n", len(yo))
print("ok")
