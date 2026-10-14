# Store footprint hunt (key: `stores`)

Pulled 2026-10-14. All sources are free and public, and none needed a login. Requests used a generic research User-Agent, with no personal details. Scripts are in `scripts/` and can be re-run.

## Tidy outputs

| File | Rows | What it is |
|---|---|---|
| `nike_locator_2026-10-14.csv` | 4,368 | One row per Nike-branded door in Nike's own store-locator feed. Fields: facility type (Nike-owned, franchisee partner, mono-brand partner), operator company (TopSports, PouSheng, Nike, ...), concept (BEACON, FACTORY, RISE, Well Collective, LIVE, ...), country, coordinates and opening date. |
| `nike_locator_weekly_counts.csv` | 2,429 | Door counts by region bucket, owner type and banner for each All The Places (ATP) crawl of the Nike locator. 88 crawls from 2023-01 to 2026-10. They are weekly from 2025-04. |
| `nike_locator_store_events.csv` | 4,784 | Each store id with the first and last crawl it appeared in. Use it to date openings and closures. |
| `partner_doors_weekly_atp.csv` | 468 | Partner door counts (all countries and US only) from ATP crawls of the locators of Foot Locker, DICK'S, Academy, JD Sports US, Hibbett, DSW, adidas, Skechers and Puma. Mostly 2025-01 to 2026-10, plus quarterly snapshots back to 2019. |
| `partner_doors_filings.csv` | 51 | Store counts from 10-K, 10-Q and XBRL filings: Foot Locker (total and North America, FY2018 to Aug 2026, plus Nike share of purchases), DICK'S, Academy, Genesco, Hibbett, Kohl's and Big 5. |
| `topsports_store_counts.csv` | 12 | Topsports (6110.HK) directly operated stores, Feb 2020 to Feb 2026, semiannual. |
| `topsports_quarterly_updates.csv` | 19 | Topsports quarterly gross selling area (QoQ and YoY %) and the sales band, Nov 2021 to May 2026. |
| `pousheng_store_counts.csv` | 16 | Pou Sheng (3813.HK) directly operated stores and sub-distributor stores, plus the net change in each half, Dec 2018 to Jun 2026. |
| `anta_store_counts.csv` | 6 | ANTA brand and ANTA KIDS store counts. This is a domestic-brand control series. |
| `lining_pos_counts.csv` | 22 | Li Ning core-brand POS count in China, quarterly from Mar 2021 to Jun 2026. This is a second control series. |

## Sources and method

- **Nike locator feed.** `https://nslp-directory.nike.com/store-locations-static.json` is the static JSON behind nike.com/retail. I fetched it directly on 2026-10-14; the gzipped raw file is in `raw/`. `scripts/flatten_nike_locator.py` flattens it.
- **All The Places (ATP).** This project crawls more than 5,000 store locators every week and keeps every run. Run list: `https://data.alltheplaces.xyz/runs/history.json`. Per-spider counts: `.../runs/<id>/stats/_results.json`, which runs from 2022 and is pulled by `scripts/atp_stats_series.py` into `raw/atp_spider_counts_long.csv`. Per-store data comes in three formats, depending on the date:
  - 2025 onward: a per-spider geojson at `.../runs/<id>/output/<spider>.geojson`, pulled by `scripts/atp_weekly_geojson.py`.
  - 2022-11 to 2024: members of a multi-GB `output.zip`, read with HTTP Range requests so the whole archive never downloads (`scripts/remote_zip.py`).
  - 2019 to 2022: `output.tar.gz`.

  `scripts/atp_spider_snapshots.py` takes the 2019 to 2024 data quarterly. `scripts/build_weekly_panel.py` turns the raw pulls into the tidy panels.
- **HKEX filings.** The filing lists come from `https://www1.hkexnews.hk/search/titleSearchServlet.do`, using stockId 1000010460 (Topsports), 23491 (Pou Sheng), 7647 (Li Ning) and 16111 (Anta). PDFs were converted with `pdftotext -layout` (`scripts/hkex_results.py`) and parsed by `scripts/parse_topsports.py` and `scripts/parse_lining.py`. The Pou Sheng and Anta figures were read from those texts by hand, and each row names its HKEX document id.
- **SEC data.** XBRL companyfacts come from `data.sec.gov` (`scripts/sec_store_counts.py` writes `raw/sec_store_facts_all.csv`). The Foot Locker 10-K store tables (filed 2020-03-27, 2022-03-24, 2023-03-27 and 2025-03-27), the DKS 10-Q filed 2026-09-03, the DKS 10-K filed 2026-03-27, the ASO 10-Q filed 2026-09-09 and the NKE 10-Q filed 2026-10-02 were read through WebFetch.

## Validation

The Nike locator matches the 10-K store counts closely. The 10-K counts are from Nike's 10-K data, already in the repo at `data/execution/store_counts_by_year.csv`.

| Locator crawl | 10-K date | US factory and clearance (locator / 10-K) | US in-line (locator / 10-K) | Non-US owned (locator / 10-K) |
|---|---|---|---|---|
| 2025-07-05 | 2025-05-31 | 213 / 213 | 80 / 85 | 608 / 604 |
| 2026-07-04 | 2026-05-31 | 213 / 212 | 73 / 75 | 595 / 587 |

## Known gaps and caveats

1. **The Nike locator is stale for China partner doors.** China partner doors read exactly 2,438 in every crawl from Sep 2025 to Jul 2026. Almost no new partner store ids appear after Aug 2025, and almost none drop out. Over the same period Topsports and Pou Sheng closed hundreds of stores. My reading is that Nike stopped maintaining the China partner records, so do not use the locator to count China partner doors. The opening-date collapse in the locator (China partner openings of 89 in 2024H2, 48 in 2025H1, 3 in 2025H2 and 0 in 2026H1) is probably partly this staleness, not a real collapse. The US, Canada, Europe, Middle East and Africa, and Asia Pacific and Latin America records do update every week.
2. **ATP spider definitions change over time.** The Nike spider's total jumps between 1,241 and 4,001 as its source changed. Only the 2025-04 to 2026-10 window comes from one consistent source (Nike's static JSON), and the tests use that window. The 2023 and 2024 snapshots are kept for reference only.
3. **A store dropping off the locator does not prove it closed.** The 33 US doors that dropped out in the week of 2026-07-18 to 2026-07-25 are not listed under new ids: only 8 new US owned ids appeared after 2025-04-17, and none after July. Press reports confirm closures of Nike Live and Well Collective stores, but they give at least 15 (Retail Dive) or 24 (Maquina do Esporte). Some of the 33 may have been delisted while still trading. **Resolved 2026-10-14:** Nike's own store records (`api.nike.com/store/store_locations/v1/<id>`, saved in `raw/nike_api_closures_2026-10-14/`) give all 33 a closing date of 2026-07-13 (one 2026-07-14) with no hours, and all 33 were Well Collective doors. None was reclassified. See `closure_verification.csv` (built by `scripts/build_closure_verification.py`) and `research_notes/Long or short cruxes/store_closure_verification.md`.
4. **Earlier filings blocked.** www.sec.gov/Archives returns 403 to scripted requests without a contact email, and I did not use the user's email. As a result, the Foot Locker and DICK'S quarterly 8-K tables before 2024 were not bulk-pulled. The data.sec.gov API and WebFetch did work.
5. **Approximate or adjusted counts.** Hibbett XBRL counts are rounded ("approximately 1,100"). JD Sports US door growth on ATP comes mostly from rebannering Finish Line and Hibbett stores, not from net new doors.
6. **Not yet published.** The Topsports results for the half to Aug 2026 (and its Q2 FY26/27 update) are due around 2026-10-22.

## Blocked or unusable sources

- web.archive.org: the CDX API and snapshots were blocked by egress policy (connection reset or "Blocked by egress policy"), so the archived locator pages and archived Nike JSON were not available.
- www.sec.gov/Archives via curl: 403 without a contact User-Agent.
- ATP `output.parquet`: 404 (not published for the runs I tried).
- ATP per-spider geojson before 2025: 404 (only available inside the zip or tar archives).
- The ATP `dicks_sporting_goods` and `hibbett_sports` spiders returned errors in some 2026 runs, which leaves gaps in the weekly series.
