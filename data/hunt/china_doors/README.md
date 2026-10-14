# China Nike-selling doors, 2023 to Oct 2026 (key: `china_doors`)

Pulled 2026-10-14. Free public sources, no logins, generic research User-Agent, no personal details sent. Question: what is the true trend in the number of doors that sell Nike in China, given that Nike's own store-locator feed is frozen for partner doors (2,438 in every crawl since Sep 2025)?

**Answer in one line.** No source gives a Nike-only door count by half-year. The best series is the door count of Nike's two largest partners (Topsports plus Pou Sheng, HKEX filings), which fell 26% in three years and about 10% in the last year, against about -1% to -2% for ANTA, Li Ning and Xtep Adult (but -10% for 361). Verdict and caveats are in `research_notes/Long or short cruxes/china_doors.md`.

## Tidy outputs

| File | What it is |
|---|---|
| `partner_doors_halfyear.csv` | Pou Sheng and Topsports directly operated doors by half-year, 2022H1 to 2026H1, with change and combined total. 2026H1 Topsports is an ESTIMATE from May 2026 selling area (Aug 2026 results are due 2026-10-28). |
| `domestic_doors_halfyear.csv` | Same half-year grid for ANTA, ANTA KIDS, Li Ning core, Xtep Adult, Xtep Kids, 361 core, 361 Kids, plus the two partners. Each row names its HKEX document. |
| `rate_comparison.csv` | Door change over 3-year, 1-year and last-half windows for every brand. |
| `partner_open_close_and_nike_proxies.csv` | Topsports annual openings and closures, selling-area changes, largest-supplier share of purchases (Nike by inference) for Topsports and Pou Sheng, Nike online share of revenue. |
| `nike_owned_china_doors.csv` | Nike-owned China mainland doors per locator crawl, with a column removing pre-listed future-dated stores. Nike-owned records are maintained, partner records are not. |
| `nike_owned_cn_dropped_api_check.csv` | 17 Nike-owned China records that dropped off the locator, with closing dates from Nike's per-store API. |
| `nike_api_cn_sample.csv` | 400 random China records (170 mono-brand partner, 140 franchisee partner, 90 Nike-owned) read from Nike's public per-store API: status, closing date, creation and modification dates. Proves the partner freeze. |
| `osm_ohsome_city_counts_quarterly.csv`, `osm_ohsome_totals_24cities.csv` | OpenStreetMap history via the ohsome API: Nike, adidas, ANTA and Li Ning shop features in 24 city boxes, quarterly 2022 to 2026-07. Mapping coverage only, not a store trend. |
| `raw/hkex_reports/` | Text of 19 full annual and interim reports of Topsports and Pou Sheng (pdftotext). `raw/peers/store_count_extracts.txt` has the Xtep and 361 lines. `raw/ohsome_run.log`, `raw/nike_api_*` are run logs and the first API sample. |
| `scripts/` | `fetch_hkex_reports.sh`, `build_panels.py` (all CSVs except API and OSM), `nike_api_cn_sample.py`, `ohsome_nike.py`. Run from this folder with `python3 -I scripts/<name>.py`. Set `PDFDIR` for the shell script. |

Existing pulls reused from `data/hunt/stores/` (HKEX announcements for Topsports, Pou Sheng, ANTA, Li Ning, and the locator panels). Pou Sheng, Topsports, ANTA and Li Ning numbers were re-checked against the raw text there; ANTA 2022 and Xtep and 361 are new here.

## Routes tried (the CLAUDE.md rule: at least five different routes, log all)

| # | Route | Result | What it gave |
|---|---|---|---|
| 1 | HKEX results, interim and annual reports, Topsports (6110) and Pou Sheng (3813) | WORKED for total doors, PARTIAL for Nike | Total directly operated doors every half-year, Topsports openings and closures by year, selling area. Neither company discloses Nike doors, Nike share of doors, or doors by banner: Topsports groups "principal brands" (Nike plus adidas) in revenue only, and Pou Sheng's reports never name Nike (0 mentions in 10 reports). Largest-supplier share of purchases is disclosed (Nike by inference). |
| 2 | Domestic brands: ANTA, Li Ning, Xtep, 361 | WORKED | Door counts to Jun 2026 for all four (Xtep from irasia interim and annual reports, 361 from HKEX results). |
| 3 | Nike 10-K, 10-Q, calls | PARTIAL | 10-K gives non-US owned stores (641 in FY2026) but no Greater China split. Calls give management's rounded mono-brand door counts: "6,000" (Jun 2023, Mar 2024), "over 5,000" (30 Sep 2025, Q1 FY26 call). Nike-owned China doors from the locator: 237 (Apr 2025) to 226 operating (Oct 2026). |
| 4 | Map and POI data: OSM Overpass, Geofabrik, Amap, Baidu | PARTIAL / BLOCKED | Overpass, Geofabrik and Baidu: connection blocked. Amap: needs an API key (INVALID_USER_KEY), not used. The ohsome API (OSM history) worked, but OSM has only 51 to 117 Nike shops in 24 big cities and rises every quarter for every brand (adidas 74 to 136, ANTA 13 to 50), which is mapping growth. Cannot detect closures. |
| 5 | Nike store locator, Nike app API, archived copies | WORKED to prove staleness, BLOCKED for history | Per-store API shows 310 of 310 sampled partner records OPEN with no closing date and last modified 2024-01 to 2025-10-15; 87 of 90 Nike-owned records modified in 2026. So partner records froze on 2025-10-15. nike.com.cn/retail returns 404; nike.com/retail is the same feed. web.archive.org and Common Crawl index: blocked or 429. |
| 6 | Chinese and English press | PARTIAL | Confirms 16 retail partners, "thousands" of Nike partner stores, Topsports operates "over half" of Nike's physical stores (press claim, SNIPPET), Nike-owned "more than 200" China stores (SNIPPET), offline doors keep trading after the 2027-01-01 online cut. No exact partner closure count by Nike. |
| 7 | Dewu, Tmall, JD authorized-store counts | BLOCKED / not informative | Pages are JS or login-gated. Press says "thousands" of online distributors are cut from 2027-01-01 and only Nike.com.cn, the app and one flagship each on Tmall, JD, Douyin remain. That is online, not doors. |
| 8 | Topsports Q2 FY26/27 update (Jun to Aug 2026) | NOT YET PUBLISHED | Board meeting notice (2026-10-12) sets interim results for 2026-10-28. Latest is Q1 (to 31 May 2026): selling area -2.9% QoQ, -11.2% YoY. Pou Sheng interim to Jun 2026 is out (3,110 doors). 361 Q3 2026 update (2026-10-14) has sales growth only. |
| 9 | Press-independent cross-check (derived) | WORKED | Management's door anchors against the partner index (see note). |

## Caveats

- Partner door totals include adidas, PUMA and other brands sold in the same stores, so they overstate the Nike-specific decline if Nike doors were closed less than average, and understate it if Nike mono-brand doors were closed more.
- Topsports and Pou Sheng report on different calendars (Aug and Feb, Jun and Dec). The half-year label pairs Pou Sheng June with Topsports August.
- The 2026H1 Topsports number is a labelled estimate: 4,360 doors at 28 Feb 2026 times (1 minus 3.4%), where -3.4% is the midpoint of -2.9% (area per store flat) and -3.9% (area per store up 1% in the quarter). Replace it with the actual Aug 2026 figure after 2026-10-28.
