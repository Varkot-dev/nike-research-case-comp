# Nike US inbound shipments hunt (key: nike_shipments)

Pulled 2026-10-14. Question: can Nike's US inbound shipment volume, by month for 2019 to Oct 2026 (especially Jul to Oct 2026), be rebuilt from free data even though Nike's consignee name is masked on US manifests? This folder extends `../trade_imports/` (reused, not redone: its ImportInfo monthly counts, US/EU/Indonesia trade series and Feng Tay revenue panel are read directly by `scripts/build_panel.py`).

No login, no account, no API key, and no personal details were sent in any request. Rate limits: 4 to 6 s between requests to ImportInfo and ImportGenius; scraping stopped where a site challenged.

## Headline

1. **A Nike-brand US inbound volume series cannot be built from free data for any month outside Feb 2021 to Nov 2022.** New finding: Nike's consignee name was masked before the 2021-22 window too. ImportGenius counts for "Nike USA, Inc." are 0 (2019), 1 (2020), 41,370 (2021), 96,160 (2022), 0 (2023), 0 (2024); ImportInfo shows the same shape. Panjiva's public page lists 159,052 Nike USA shipments, last one 2022-11-16. The 21 visible months look like a lapse in the 19 CFR 103.31 confidentiality certificate (which must be renewed every two years), not a normal state. Nike's factories disappear as shippers at exactly the same dates (Feng Tay, Chang Shin, Pratama, TK Industrial, Lotus all go from hundreds or thousands a year in 2022 to 0 in 2023), so Nike masks shipper names too.
2. **What leaks since 2024 is a small, provider-specific sample.** Factory names re-appear with a blank consignee (and notify party "Expeditors International", 2508 N Marine Dr, Portland, Nike's broker), at roughly 1% to 3% of the 2022 visible rate, and the two providers disagree (2026 YTD: PT Chang Shin Indonesia 14 on ImportGenius vs about 150 on ImportInfo). These counts move when a carrier spells a name differently, so they are visibility series, not volume.
3. **Converse is the one clean, Nike-owned, never-masked US series** (consignee "CONVERSE INC", 2012 to Oct 2026, BOL text gives pairs and containers). Jul-Sep arrivals: 278 (2024), 214 (2025), 154 (2026): -28% YoY, -45% vs 2024; Jan-Sep -53% YoY. This matches Converse's reported collapse (FY23 $2,427M to FY26 $1,174M; Q1 FY27 -$103M).
4. **Nike Canada (named, routed via Tacoma/Seattle)**: Jul-Sep 955 vs 495 (+93%), Oct 1 to about 9 already 216 vs 111 for all of Oct 2025, but Jan-Sep only +0.5%: a timing or routing shift into holiday, not more annual volume.
5. Market: US footwear imports Jul-Aug 2026 -1.4% YoY (Aug estimated), -7.6% vs 2024. Clean visible peer consignees (adidas, ASICS, Brooks, New Balance, On, Vans) Jul-Sep median -19% YoY, -2% vs 2024.

Verdict on this crux: **INCONCLUSIVE** (weak lean LONG on holiday timing from visible proxies; Converse SHORT-consistent; Nike-brand volume not observable). See `research_notes/Long or short cruxes/nike_shipments.md`.

## Tidy files

| File | What it is |
|---|---|
| `bol_monthly_by_entity.csv` | ImportInfo monthly BOL counts 2019-01 to 2026-10 (October partial, data to about Oct 9-12) for 32 entities: slug, month, bols, group (converse, nike_canada, nike_mexico, nike_usa_leak, factory_strict, factory_broad, forwarder_apl, peer, peer_broken), party_role, note |
| `nike_linked_panel_monthly.csv` | Monthly group totals plus US footwear imports (USD m, HS 64 World, Comtrade/Census; Aug 2026 estimated, flagged), Nike-sourcing-mix imports and Feng Tay USD revenue (from `../trade_imports/nike_vs_industry_monthly.csv`), 2019-01 to 2026-10 |
| `test_holiday_window.csv` | Every entity, group and market series: Jul-Sep 2024/2025/2026 totals, YoY, vs 2024, YTD YoY, holiday loading ratio (Jul-Sep monthly avg / Jan-Jun monthly avg), visibility-break flag (12-month rolling total hits 0 or moves more than 3x within 2024-12 to 2026-09) |
| `test_results.csv` | Pre-registered tests T1 to T3 with rule and result |
| `importgenius_annual_counts.csv` | ImportGenius annual shipment counts per page (Nike entities, Converse, factories), 2006 to 2026 YTD |
| `importgenius_recent_shipments.csv` | The 10 most recent shipments per ImportGenius page (shipper, consignee, quantity, kg, origin, description) |

## Scripts

- `scripts/pull_importinfo_monthly.py` ImportInfo `/<slug>?monthly_chart` JSON (company HTML pages return HTTP 401 bot challenge; the chart JSON still answered).
- `scripts/pull_importgenius.py` public ImportGenius company pages (robots.txt allows all but /search).
- `scripts/ig_extract.js` reads the server-rendered `window.__NUXT__` data block of each saved page in a sandboxed `vm` with a 2 s timeout (annual datapoints, top partners, recent shipments). Run: `node scripts/ig_extract.js raw/importgenius/ig_us_extract.json raw/importgenius/us/*.html raw/importgenius/ig_feng-tay-enterprises-co-ltd.html`.
- `scripts/build_panel.py` builds all CSVs and runs the tests (`python3 -I scripts/build_panel.py`).

## Raw (all files under 20 MB)

`raw/importinfo/` (new chart JSON: Converse, peers, Tae Kwang Vina, Dona Pacific, Samyang), `raw/importgenius/us/` and `raw/importgenius/intl/` (saved pages), `raw/importgenius/vn_buyers_nike-global-trading-bv-singapore-branch.html`, `raw/importgenius/sitemaps/` (sitemap indexes), `raw/oec/` (OEC Nike company page data, Oregon and Tennessee state pages, cube list), `raw/datausa/cubes.json` (attempt record).

## Every attempt (worked / partial / blocked)

### 1. Shipper side (Nike factories and trading entities)

| Source / target | Status | Result |
|---|---|---|
| ImportInfo chart JSON: Feng Tay (TW, ID), Chang Shin (VN, ID), Pratama, Nikomas, Freetrend, Pou Yuen VN, Lotus, TK Industrial (from trade_imports) | PARTIAL | Visible 2021-07 to 2022-11 only at scale; leaks since 2024 (see Headline 2) |
| ImportInfo: Tae Kwang Vina | WORKED, no signal | Visible Jun 2021 to Apr 2022 only; 0 every month since 2023 |
| ImportInfo: Dona Pacific Vietnam (Feng Tay group) | WORKED, no signal | 0 to 33 a month, 0 since Oct 2025 |
| ImportInfo: Samyang Tongsang | WORKED, no signal | 0 to 8 a month; 0 in 2025-26 |
| ImportInfo slugs for Changshin Vietnam variant, Shoetown, Pou Yuen Vietnam Enterprise, Nike Global Trading BV, Nike Retail Services | BLOCKED | HTTP 401 (bot challenge, likely on non-existent slugs); not pursued further |
| ImportInfo: Ching Luh Vietnam, Nike Trading Company | BLOCKED | 404 |
| ImportGenius US supplier pages: Feng Tay, PT Feng Tay, Pouyuen VN, PT Chang Shin, PT TK, PT Pratama, PT Nikomas, Lotus | WORKED (annual only) | Annual counts and 10 recent BOLs; monthly chart data is paywalled. Feng Tay 2026 YTD 507 vs 342 in 2025, but 1,435 in 2022 |
| ImportGenius slugs for Chang Shin VN, Tae Kwang Vina, Shoetown, Ching Luh, Samyang, Freetrend, APL Logistics VN, Nike Trading Company, Nike Vietnam LLC, PT Nike Indonesia | BLOCKED | Not found (site returns its generic page) |
| ImportGenius Vietnam export data (buyers "Nike Global Trading BV Singapore Branch", "Nike Global Trading B.V") | PARTIAL | Exists but stops in 2021-2024 (674 shipments 2019, 117 in 2020, 18 in 2021, 0 after); no 2025-26 |
| ImportGenius India pages (Lotus Footwear, Nike Global Trading) | BLOCKED | No company page (generic listing returned) |
| Seair (`seair.co.in` Nike / Feng Tay pages) | BLOCKED | Cloudflare 403 |
| Volza, ExportGenius, ImportYeti, Eximpedia | BLOCKED | Cloudflare 403 |
| Panjiva public pages | PARTIAL | Public page confirms 159,052 Nike USA shipments, last 2022-11-16; detail and charts need login |
| Trademo, Tendata, 52wmb, Datamyne, Tradeint | BLOCKED | Home pages load, company data needs login (not attempted) |

### 2. Alias / notify party / product text

| Target | Status | Result |
|---|---|---|
| Converse Inc (ImportInfo chart + ImportGenius page) | WORKED | Clean monthly series 2012 to Oct 2026 (Headline 3). Shippers Vinh Long Footwear, Nice Elite / Adora, PT Glostar, PT Yih Quan; BOL text gives pairs (for example 26,124 pairs, 4 x 40 ft) |
| Nike Canada Corp, Nike de Mexico (named consignees routed through US ports) | WORKED | Monthly series; shippers include Kuehne+Nagel, notify Expeditors Canada; BOL text "OCM-CTP, FOOTWEAR DIVISION OF GOODS" |
| Nike USA Inc, NIKE Inc | PARTIAL | Residual leaks only (Port Everglades apparel "PLANT CODE", Newark via APL/CEVA); 13 to 81 a month in 2026 |
| Nike Retail Services Inc (DC operator, WARN filer) | BLOCKED | No US import records under that name (ImportGenius 0) |
| Notify party "Expeditors International" Portland, "CEVA", APL Logistics VN ("NIKE APPAREL GOODS" in text) | PARTIAL | Visible as notify/shipper on leaked masked BOLs; APL Logistics VN series jumps from about 36 to 557 a month in Sep 2025 (visibility break), multi-client; cannot be filtered to Nike without the paywalled search |
| Product-text search ("NIKE", style codes, "FOOTWEAR DIVISION OF GOODS", "OCM-CTP") across all BOLs | BLOCKED | Needs ImportInfo /search or /manifest (robots.txt disallows), ImportGenius /search (disallowed) or a paid account. Fingerprints recorded for future paid use: "FOOTWEAR DIVISION OF GOODS", "APPAREL DIVISION OF GOODS", "OCM-CTP", "SHIPPER LOAD AND COUNT", notify "EXPEDITOR S INTERNATIONAL, 2508 NORTH MARINE DR, PORTLAND" |
| OEC company profile "Nike" (BOL-based, public page variables) | PARTIAL | 1,373 shipments 2026 YTD; Aug 2026 266 vs Aug 2025 33; top shipper "Other" (1,021, masked); top destination Washington (Nike Canada). Monthly data API (`bill_of_lading_explorer` cube) returns "needs authorization" |
| JOC Top 100 importers (PIERS estimates of Nike TEU) | BLOCKED | Paywalled; AJOT lists (Descartes/Datamyne BOLs) give Nike about 45,076 TEU (2021 list) and about 110,000 TEU (2023 list), both from the visible window only |

### 3. Other countries' data

| Source | Status | Result |
|---|---|---|
| ImportGenius Vietnam customs data | PARTIAL | Ends by early 2024 |
| Indonesia exports (Comtrade) | WORKED (in trade_imports) | Reused, not re-pulled |
| Vietnam monthly exports to Comtrade | BLOCKED | Not reported after Dec 2023 (trade_imports) |
| Mexico pedimento aggregators, Indian export data sites | BLOCKED | Seair/Volza/ExportGenius 403; no free company-level source found |
| EU/UK company-level import data | BLOCKED | Not published by company; EU aggregates already in trade_imports |

### 4. Government aggregates by place

| Source | Status | Result |
|---|---|---|
| Census API (`api.census.gov/.../intltrade/imports/porths` and `/hs`) without key | BLOCKED | 302 to missing_key.html; a key needs an email registration, so not used |
| OEC subnational cubes (`trade_s_usa_port_m_hs`, `trade_s_usa_district_m_hs`, `trade_s_usa_state_m_hs`) | BLOCKED | Cubes exist, API returns "The requested resource needs authorization" |
| OEC state profile pages (Tennessee, Oregon) | PARTIAL | Public variables give only total state imports for the latest month (Tennessee Jul 2026 imports $10.87B, +4.0% YoY; top origin Vietnam $1.38B). No footwear-by-state series |
| Census state data pages, USA Trade Online, USITC DataWeb | BLOCKED | State/port by HS only through USA Trade Online or DataWeb (login) |
| Data USA API | BLOCKED | No trade-by-port cubes (only FAF annual) |
| FT-900, Comtrade national series | WORKED (in trade_imports) | Reused |
| Port of LA / Long Beach monthly TEU | NOT PULLED | All-commodity; national HS 64 value is the better market comparator and is already in trade_imports |

### 5. Logistics proxies

| Source | Status | Result |
|---|---|---|
| WARN notices (`../hiring/warn_notices_warntracker.csv`) | WORKED | NIKE Retail Services: 583 in Shelby County TN (Memphis, 3100 New Frayser Blvd and 5151 Shelby Dr) and 193 in Byhalia MS, filed Jan 26-27, 2026, effective Apr 3, 2026; Converse Ontario CA 77 (Sep 2024). Nike said it is consolidating domestic DC operations and adding automation (FreightWaves, Bloomberg Jan 26, 2026). Structural, says nothing on Q3 throughput |
| Press: JOC, FreightWaves, Supply Chain Dive, Sourcing Journal on Nike volumes in 2026 | PARTIAL | No 2026 article with Nike shipment counts found; only the DC consolidation story |
| Memphis rail/intermodal volumes | BLOCKED | No free monthly Memphis-specific series found |
| Nike Q1 FY27 10-Q (repo notes) | WORKED (repo) | NA inventory $3,491M at Aug 31, 2026, -0.9% YoY; total inventory $7,846M, -3.3% |

### 6. Non-US Nike entities

| Source | Status | Result |
|---|---|---|
| Nike Canada Corp (US-port BOLs) | WORKED | See Headline 4 |
| Nike de Mexico (US-port BOLs) | WORKED, tiny | Jul-Sep 23 vs 12; YTD -34% |
| Nike Europe (Laakdal), Nike Japan, Nike China imports | BLOCKED | No free company-level import data |

## Pre-registered tests (written in this README before computing)

Window: Jul-Sep arrivals (October is partial). Compare 2026 with 2025 and 2024.

- **T1 Converse** BOL YoY Jul-Sep vs median of clean visible peers (adidas, ASICS, Brooks, New Balance, On, Vans; Skechers, Deckers, Crocs, Puma, Under Armour excluded by the visibility-break flag). More than 10 pts below = SHORT; within 10 = NEUTRAL; above = LONG.
- **T2 Nike brand visible proxies** (Nike Canada consignee; Nike-dedicated factory leaks): LONG if both rise YoY, beat US footwear imports YoY, and the rise is spread across at least 3 of the 6 strict factory names without relying on names with a visibility break. SHORT if both fall more than the market. Otherwise INCONCLUSIVE.
- **T3 Holiday loading** (Jul-Sep monthly avg / Jan-Jun monthly avg): LONG if Nike-linked ratios rise in 2026 while peers fall; SHORT if they fall.

## Results (`test_results.csv`)

| Test | Nike-linked | Benchmark | Result |
|---|---|---|---|
| T1 Converse Jul-Sep YoY | -28.0% | clean peer median -19.0% (gap -9.0 pts) | NEUTRAL (just inside the 10-pt band) |
| T1b Converse vs 2024 | -44.6% | peer median -2.0% | SHORT (supplementary) |
| T2a Nike Canada Jul-Sep YoY | +92.9% | US footwear imports Jul-Aug -1.4% | rises, beats market |
| T2b strict factory leaks (no-break names: PT Feng Tay, PT Chang Shin, Pratama) | +18.3% (115 to 136 BOLs) | -1.4% | breadth fails: 2 of 3 clean names rise (4 of 6 incl. break names); Feng Tay Taiwan, the purest Nike name, -33% (95 to 64). INCONCLUSIVE |
| T3 loading 2025 to 2026 | Nike Canada 0.58 to 1.50; strict factories 1.29 to 1.24; Converse 0.81 to 1.59 | clean peers 1.09 to 0.94; US footwear imports 1.09 to 1.11 | LONG-leaning, weak |

## Caveats

- BOL counts are not containers or pairs; carriers split or merge bills. Converse BOLs rose 26% in calendar 2024 while Converse revenue fell in FY24, so even clean counts are noisy.
- ImportInfo and ImportGenius use different name matching and disagree on leak counts; both are shown.
- Nike Canada counts only Canadian cargo landed at US ports; a routing switch from Vancouver/Prince Rupert to Tacoma would produce the same jump. Jan-Sep is flat (+0.5%), which fits a timing or routing change better than a volume rebuild.
- US footwear imports Aug 2026 is an estimate (+1.8% YoY, from the earlier hunt); Census Exhibit 15 SITC 85 shows Aug 2026 $2,483M and Jul $2,295M.
