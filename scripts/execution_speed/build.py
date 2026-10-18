"""Execution-speed tables: how fast is Nike implementing its plan, from free alternative data already in the repo.

Run from the repo root: python3 scripts/execution_speed/build.py
Reads only files already committed under data/ (pulled by earlier sessions; each source folder has a README with
routes and caveats). Writes one CSV per table to data/execution_speed/ and one workbook
data/execution_speed/nike_execution_speed.xlsx (Summary sheet plus one sheet per table). All derived columns are
my arithmetic. Status labels follow the fixed rule written next to each indicator in SUMMARY_RULES.
"""
import os
import pandas as pd

OUT = "data/execution_speed"
os.makedirs(OUT, exist_ok=True)
tables, summary = {}, []

def half(dates):
    d = pd.to_datetime(dates)
    return d.dt.year.astype(str) + "H" + ((d.dt.month > 6) + 1).astype(str)

def qtrs_between(a, b):
    return (pd.Timestamp(b) - pd.Timestamp(a)).days / 91.31

def add_summary(pillar, indicator, unit, base_date, base, last_date, last, good_if, source, note=""):
    chg = last - base
    pace = chg / qtrs_between(base_date, last_date) if qtrs_between(base_date, last_date) > 0 else None
    on_plan = (chg < 0) if good_if == "down" else (chg > 0)
    status = "Moving with plan" if on_plan else "Against plan"
    if abs(chg) < 0.05 * max(abs(base), 1e-9):
        status = "Little change"
    summary.append(dict(pillar=pillar, indicator=indicator, unit=unit, baseline_date=str(base_date)[:10],
                        baseline=round(base, 2), latest_date=str(last_date)[:10], latest=round(last, 2),
                        change=round(chg, 2), change_pct=round(100 * chg / base, 1) if base else None,
                        pace_per_quarter=round(pace, 2) if pace is not None else None,
                        plan_direction=good_if, status=status, source=source, note=note))

# T01 Classics wind-down: nike.com franchise wall product counts (Common Crawl captures of the "N results" counter)
w = pd.read_csv("data/hunt/pricing_catalog/cc_category_walls.csv")
w["date"] = pd.to_datetime(w.ts.astype(str).str[:8])
w["half"] = half(w.date)
walls = {"air-force-1-shoes-5sj3yzy7ok": "air_force_1", "dunk-shoes-90aohzy7ok": "dunk",
         "jordan-1-shoes-4fokyzy7ok": "air_jordan_1", "air-max-shoes-a6d8hzy7ok": "air_max",
         "mens-shoes-nik1zy7ok": "all_mens_shoes", "womens-shoes-5e1x6zy7ok": "all_womens_shoes"}
t1 = (w[w.wall.isin(walls)].assign(wall=lambda x: x.wall.map(walls))
      .pivot_table(index="half", columns="wall", values="count", aggfunc="median").round(0))
t1 = t1[[c for c in walls.values() if c in t1.columns]]
t1["captures"] = w[w.wall.isin(walls)].groupby("half").size()
t1["af1_index_2023H1_100"] = (100 * t1.air_force_1 / t1.air_force_1.iloc[0]).round(1)
t1["dunk_index_2023H1_100"] = (100 * t1.dunk / t1.dunk.iloc[0]).round(1)
t1["af1_share_of_all_shoes_pct"] = (100 * t1.air_force_1 / (t1.all_mens_shoes + t1.all_womens_shoes)).round(1)
tables["T01_classics_walls"] = t1.reset_index()
add_summary("Classics wind-down", "Air Force 1 products listed on nike.com (half-year median)", "products",
            "2023-06-30", t1.air_force_1["2023H1"], "2026-06-30", t1.air_force_1["2026H1"], "down",
            "data/hunt/pricing_catalog/cc_category_walls.csv")
add_summary("Classics wind-down", "Dunk products listed on nike.com (half-year median)", "products",
            "2023-06-30", t1.dunk["2023H1"], "2026-10-01", t1.dunk.dropna().iloc[-1], "down",
            "data/hunt/pricing_catalog/cc_category_walls.csv", "latest is 2026H2 to date")
add_summary("Classics wind-down", "Air Jordan 1 products listed on nike.com (half-year median)", "products",
            "2023-06-30", t1.air_jordan_1["2023H1"], "2026-06-30", t1.air_jordan_1["2026H1"], "down",
            "data/hunt/pricing_catalog/cc_category_walls.csv", "fell to 46 in 2025H1, rebounded to 118 in 2026H1")

# T02 Full-price NIKE Digital: share of nike.com men's shoes on the sale wall (Wayback, quarterly) and share of
# product pages showing a discount (Common Crawl product-page panel, monthly, aggregated to quarter by count)
s = pd.read_csv("data/marketplace/nike_sale_share_quarterly.csv")
p = pd.read_csv("data/hunt/pricing_catalog/pdp_nike_monthly.csv")
p["quarter"] = pd.PeriodIndex(pd.to_datetime(p.ym), freq="Q").astype(str)
p["disc_n"] = p.n * p.share
pq = p.groupby("quarter").agg(pdp_pages=("n", "sum"), disc=("disc_n", "sum")).reset_index()
pq["pdp_share_discounted_pct"] = (100 * pq.disc / pq.pdp_pages).round(1)
t2 = s[["quarter", "mens_sale_shoes_count", "mens_shoes_count", "mens_sale_share_pct", "all_sale_count",
        "sale_wall_fp_avg_discount_discounted_pct"]].merge(pq.drop(columns="disc"), on="quarter", how="outer")
t2 = t2.rename(columns={"quarter": "calendar_quarter", "all_sale_count": "nikecom_sale_wall_products",
                        "sale_wall_fp_avg_discount_discounted_pct": "sale_wall_first_page_avg_discount_pct"})
tables["T02_fullprice_digital"] = t2
add_summary("Full-price NIKE Digital", "Men's shoes on nike.com sale wall, % of men's shoes", "%",
            "2024-10-08", 42.6, "2026-10-13", 44.0, "down", "data/marketplace/nike_sale_share_quarterly.csv",
            "baseline 2024Q4 = Hill's first quarter; 2024Q1 to Q3 ran 48% to 50%")
pb = pq.set_index("quarter").pdp_share_discounted_pct
add_summary("Full-price NIKE Digital", "nike.com product pages showing a discount (quarter, Common Crawl)", "%",
            "2024-09-30", pb["2024Q3"], "2026-09-30", pb["2026Q3"], "down",
            "data/hunt/pricing_catalog/pdp_nike_monthly.csv",
            f"same calendar quarter to remove seasonality; 2025Q3 = {pb['2025Q3']}%")

# T03 Inventory clean-up: Nike and Jordan share of Foot Locker sale items (Wayback); nike.com sale wall size
f = pd.read_csv("data/marketplace/footlocker_sale_brand_history.csv")
f = f[f.page == "sale_all"].pivot_table(index="snapshot_date", columns="brand", values="share_of_sale_pct")
cols = [c for c in ["Nike", "Jordan", "adidas", "New Balance", "On", "ASICS"] if c in f.columns]
t3 = f[cols].copy()
t3["nike_plus_jordan_pct"] = t3.Nike + t3.Jordan
t3 = t3.reset_index().rename(columns={"snapshot_date": "date"})
tables["T03_footlocker_sale_share"] = t3
b, l = t3[t3.date == "2024-11-23"].iloc[0], t3.iloc[-1]
add_summary("Inventory clean-up", "Nike + Jordan share of Foot Locker sale items", "% of sale items",
            b.date, b.nike_plus_jordan_pct, l.date, l.nike_plus_jordan_pct, "down",
            "data/marketplace/footlocker_sale_brand_history.csv", "Wayback snapshots of footlocker.com/sale")
add_summary("Inventory clean-up", "Products on nike.com sale wall (all categories)", "products",
            "2024-10-08", 3927, "2026-10-13", 4831, "down", "data/marketplace/nike_sale_share_quarterly.csv")

# T04 Wholesale reinvestment: Nike share of products on partner sites, Aug to Oct window each year (Common Crawl)
o = pd.read_csv("data/hunt/offprice_census/cc_brand_share_aug_oct_by_year.csv")
t4 = o[["host", "window", "total_unique", "nike_pct", "jordan_pct", "adidas_pct", "nike_over_adidas"]].copy()
t4["year"] = t4.window.str[:4].astype(int)
tables["T04_partner_site_nike_share"] = t4
ac = t4[t4.host == "academy"].set_index("year")
add_summary("Wholesale reinvestment", "Nike share of products on academy.com (Aug to Oct)", "% of products",
            "2025-10-01", ac.nike_pct[2025], "2026-10-01", ac.nike_pct[2026], "up",
            "data/hunt/offprice_census/cc_brand_share_aug_oct_by_year.csv",
            "2024 Common Crawl sample (430 products) found no Nike pages, but Academy's full sitemap shows 8.9% Nike "
            "(N6_offprice_census.md), so 2024 is a sampling gap and the baseline is 2025; samples 1,475 and 1,097")
ff = t4[t4.host == "famousfootwear"].set_index("year")
add_summary("Wholesale reinvestment", "Nike share of products on famousfootwear.com (Aug to Oct)", "% of products",
            "2024-10-01", ff.nike_pct[2024], "2026-10-01", ff.nike_pct[2026], "up",
            "data/hunt/offprice_census/cc_brand_share_aug_oct_by_year.csv", "2024 sample only 385 products")

# T05 Wholesale partners' view: Nike mentions and tone on DICK'S (DKS) and Academy (ASO) earnings calls
t5 = pd.read_csv("data/hunt/earnings_calls/peers/peer_calls_summary.csv").drop(columns="source_url")
tables["T05_retailer_call_mentions"] = t5
for tk in ["DKS", "ASO"]:
    x = t5[t5.ticker == tk]
    add_summary("Wholesale partners' view", f"{tk} earnings call: net positive Nike sentences (positive minus negative)",
                "sentences", x.call_date.iloc[0], x.nike_net_tone.iloc[0], x.call_date.iloc[-1], x.nike_net_tone.iloc[-1], "up",
                "data/hunt/earnings_calls/peers/peer_calls_summary.csv",
                f"negative Nike sentences across all {len(x)} calls: {int(x.nike_negative.sum())}")

# T06 Store fleet: 10-K store counts (annual) and Nike store locator (monthly, last weekly run each month)
k = pd.read_csv("data/execution/store_counts_by_year.csv").drop(columns=["doc"])
tables["T06a_store_counts_10k"] = k
loc = pd.read_csv("data/hunt/stores/nike_locator_weekly_counts.csv")
loc = loc[(loc["owner:type"] == "NIKE_OWNED_STORE") & (loc.run_date >= "2025-02-22")]  # consistent crawl from Feb 2025
loc["month"] = loc.run_date.str[:7]
last = loc.groupby("month").run_date.max()
lm = loc[loc.run_date.isin(last)]
t6 = lm.pivot_table(index=["month", "run_date"], columns="brand", values="n", aggfunc="sum")
t6["us_owned_total"] = lm[lm.bucket == "US"].groupby(["month", "run_date"]).n.sum()
t6["china_owned_total"] = lm[lm.bucket == "China mainland"].groupby(["month", "run_date"]).n.sum()
t6["all_owned_total"] = lm.groupby(["month", "run_date"]).n.sum()
t6 = t6.rename(columns={"Nike": "nike_inline_and_brand_stores"}).reset_index()
tables["T06b_owned_stores_locator"] = t6
a, z = t6.iloc[0], t6.iloc[-1]
add_summary("Store fleet", "Nike-owned in-line (full-price) stores worldwide, store locator", "stores",
            a.run_date, a.nike_inline_and_brand_stores, z.run_date, z.nike_inline_and_brand_stores, "down",
            "data/hunt/stores/nike_locator_weekly_counts.csv", "10-K in-line count: 146 (FY25) to 125 (FY26)")
add_summary("Store fleet", "Nike-owned stores in the US, store locator", "stores",
            a.run_date, a.us_owned_total, z.run_date, z.us_owned_total, "down",
            "data/hunt/stores/nike_locator_weekly_counts.csv")

# T07 Sport offense (running): Nike share of full-price road-running colorways at Running Warehouse; Nike share of
# new running-shoe reviews at RunRepeat (half-year)
r = pd.read_csv("data/marketplace/runningwarehouse_history.csv")
t7 = r[r.page == "mens_road"].pivot_table(index="snapshot_date", columns="brand", values="colorway_share_pct")
t7 = t7[[c for c in ["Nike", "Hoka", "ASICS", "Brooks", "Saucony", "New Balance", "On Running"] if c in t7.columns]]
tables["T07a_runningwarehouse_road_share"] = t7.reset_index()
tables["T07b_runrepeat_nike_share"] = pd.read_csv("data/hunt/w8_launch_newness/w8_runrepeat_nike_share_by_halfyear.csv")
add_summary("Sport offense (running)", "Nike share of men's road-running colorways, Running Warehouse", "% of colorways",
            t7.index[0], t7.Nike.iloc[0], t7.index[-1], t7.Nike.iloc[-1], "up",
            "data/marketplace/runningwarehouse_history.csv")

# T08 China reset: Nike's two largest China partners (Topsports, Pou Sheng) door counts and Topsports selling area
t8 = pd.read_csv("data/hunt/china_doors/partner_doors_halfyear.csv").drop(columns="hkex_docs")
tables["T08a_china_partner_doors"] = t8
tables["T08b_topsports_quarterly"] = pd.read_csv("data/hunt/stores/topsports_quarterly_updates.csv")[
    ["as_at", "selling_area_qoq_pct", "selling_area_yoy_pct", "retail_wholesale_sales_yoy_band", "hkex_doc"]]
c0, c1 = t8[t8.period == "2024H2"].iloc[0], t8.iloc[-1]
add_summary("China reset", "Topsports + Pou Sheng doors (Nike's two largest China partners)", "doors",
            "2024-12-31", c0.combined_doors, "2026-06-30", c1.combined_doors, "down",
            "data/hunt/china_doors/partner_doors_halfyear.csv",
            "plan direction 'down' = door clean-up; Nike gives no door target, so this measures pace, not success")

# T09 Reorganisation: open postings (Common Crawl of the careers site), corporate mix by function, WARN notices
po = pd.read_csv("data/hunt/hiring/nike_open_postings_series.csv")
tables["T09a_open_postings"] = po[["date", "total_open_postings", "site", "yoy_pct"]]
cm = pd.read_csv("data/hunt/hiring/composition_by_period.csv")
cm = cm[cm.source == "new"]
tables["T09b_corporate_postings_mix"] = cm
wn = pd.read_csv("data/hunt/hiring/warn_notices_warntracker.csv")
tables["T09c_warn_notices"] = wn[wn.notice_date >= "2023-01-01"].sort_values("notice_date")
m = cm.set_index("period")
add_summary("Reorganisation", "Sales and merchandising share of corporate job postings", "% of corporate postings",
            "2025-06-30", m.corp_sales_merch_pct["2025H1"], "2026-09-30", m.corp_sales_merch_pct["2026Q3"], "up",
            "data/hunt/hiring/composition_by_period.csv", "peak 23.3% in 2025H2; 2025H1 sample only 126 postings")

# T10 Promise ledger: dated management commitments and outcomes (from Nike's own earnings call transcripts)
pt = pd.read_csv("data/hunt/earnings_calls/promise_tracker.csv")
tables["T10a_promise_ledger"] = pt[["promise_id", "era", "topic", "target", "made_in", "times_reaffirmed",
                                    "times_pushed", "times_cut", "outcome", "score"]]
sc = pt.groupby(["era", "score"]).size().unstack(fill_value=0)
tables["T10b_promise_scores_by_era"] = sc.reset_index()
hill = pt[pt.era == "Hill"]
resolved = hill[~hill.score.str.startswith("pending")]
kept = resolved.score.isin(["kept", "beat"]).sum()
summary.append(dict(pillar="Dated commitments", indicator="Hill-era promises kept or beaten, of those resolved",
                    unit="count", baseline_date="", baseline=None, latest_date="2026-10-01", latest=kept,
                    change=None, change_pct=round(100 * kept / len(resolved), 1), pace_per_quarter=None,
                    plan_direction="up", status=f"{kept} of {len(resolved)} resolved; "
                    f"{(hill.score.str.startswith('pending')).sum()} pending, of which "
                    f"{(hill.score == 'pending_at_risk').sum()} at risk",
                    source="data/hunt/earnings_calls/promise_tracker.csv",
                    note="Donahoe era: 2 of 13 resolved kept or beaten (D01, D09), 1 kept late"))

# Write
sm = pd.DataFrame(summary)
tables = {"Summary": sm, **tables}
for name, df in tables.items():
    df.to_csv(f"{OUT}/{name}.csv", index=False)
with pd.ExcelWriter(f"{OUT}/nike_execution_speed.xlsx", engine="openpyxl") as xw:
    for name, df in tables.items():
        df.to_excel(xw, sheet_name=name[:31], index=False)
        ws = xw.sheets[name[:31]]
        ws.freeze_panes = "A2"
        for col in ws.columns:
            width = max(len(str(c.value)) if c.value is not None else 0 for c in col[:60])
            ws.column_dimensions[col[0].column_letter].width = min(max(10, width + 2), 60)
pd.set_option("display.width", 250)
pd.set_option("display.max_colwidth", 60)
print(sm.drop(columns=["source", "note"]).to_string())
