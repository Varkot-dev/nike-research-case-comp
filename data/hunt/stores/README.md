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

## Checker review

Reviewed 2026-10-14 by an independent checker. I re-pulled samples from the original sources (generic User-Agent, no personal details, 1 to 2 s sleeps), re-ran `scripts/run_tests.py` and checked the cleaning. Small re-pulled files are in `raw/checker_2026-10-14/`.

### Re-pulls (what matched)

| Dataset | Re-pulled points | Result |
|---|---|---|
| Nike static locator JSON | Full file (fileCreatedTime 10/13/2026 10:01:56 PM), 4 sample rows | Same 4,368 ids as the CSV; facility type, opening date and coordinates match. US Nike-owned: 183 factory + 29 clearance + 40 in-line. China partner doors 1,430 + 1,008 = 2,438. |
| ATP Nike geojson | Runs 2025-07-05, 2026-07-18, 2026-07-25 | US owned: 184/29/80, 183/29/73, 183/29/40. Exactly matches `nike_locator_weekly_counts.csv`. The 33 refs that vanished are the 33 in `closure_verification.csv`. |
| Nike store API | 3 of the 33 ids (Pasadena, Southlake, Ridgedale) | Each returns `closingDate` 2026-07-13 with empty hours. Closures are real, not delistings. |
| ATP Foot Locker geojson | Runs 2025-04-19, 2025-05-10, 2026-10-03 | US 1,461 / 1,356 / 1,292, matching the CSV. See the issue below. |
| SEC XBRL NumberOfStores | Academy, Genesco, DKS | 298/322/327, 1,278/1,236/1,186 and 723 all match. |
| HKEX | Pou Sheng 2026 interim, Topsports Q1 FY26/27 update, Topsports 2025 interim, ANTA 2026 interim, Li Ning Q2 2026 update | 3,310 to 3,110 (-200); area -2.9% QoQ and -11.2% YoY; 4,688; ANTA 7,122 (7,203 at Dec 2025); Li Ning 6,063. All match. |

The test script re-runs and its output is byte-identical to `test_output.txt`. There are no duplicate keys in the store events, weekly counts or partner panels. In the locator CSV, 16 `storeNumber` values are duplicated but `id` is unique; this is harmless because the tests key on `id` or ref.

### What holds

1. **The US in-line cut is real and correctly dated.** 73 to 40 between the 2026-07-18 and 2026-07-25 crawls, all Well Collective stores, and Nike's own API gives a closing date of 2026-07-13. The locator-to-10-K validation also checks out against `data/execution/store_counts_by_year.csv` (non-US owned 543+61=604 in FY2025 and 537+50=587 in FY2026).
2. **The China partner contraction is specific to Nike's channel.** Pou Sheng lost 6.0% of its doors in H1 2026, against -1.1% for the ANTA brand and -0.5% for Li Ning core POS over the same half.
3. **The Nike locator is stale for China partner doors.** It reads 2,438 every week from Sep 2025, which I confirmed in the fresh pull.

### What does not hold, or needs rewording

1. **The Pou Sheng "acceleration" mixes period lengths.** In `pousheng_store_counts.csv`, the `net_change_in_period` value at each Dec row is a full-year change (for example 2025-12-31 is -138, which is 3,448 to 3,310), while each Jun row is a half-year change. The half-on-half series is -40 (H1 2025), -98 (H2 2025) and -200 (H1 2026). It still accelerates, but the column should be relabelled, and the summary's "-40, -138, -200" should read "-40, -98, -200 per half".
2. **The Topsports "re-widening" is selective.** Selling area YoY ran -14.1% (Aug 2025), -13.4% (Nov 2025), -9.7% (Feb 2026) and -11.2% (May 2026), and QoQ ran -3.3, -1.3, -4.2 and -2.9. That is steady double-digit shrinkage with no clear trend, not an acceleration. Store count is also falling faster than area (-13.1% against -9.7% YoY at Feb 2026), which fits a strategy of consolidating into bigger stores. Shelf space is shrinking less than door counts suggest.
3. **The domestic control leaves out ANTA KIDS.** ANTA KIDS fell from 2,652 to 2,560 (-3.5%) in H1 2026, and ANTA plus ANTA KIDS fell 1.8% in the half. There is some China-wide softness. The gap to Pou Sheng (-6.0%) still holds, but it is narrower than "about -1%" implies.
4. **The Foot Locker ATP decline of -11.6% is overstated by a locator clean-up.** ATP lost 116 US Foot Locker ids in three weeks (2025-04-19 to 2025-05-10), including all 5 Lady Foot Locker records, which were already defunct. Yet the filings show Foot Locker North America down only 55 doors (1,665 to 1,610) for the whole year to Jan 2026. Measured from the stable window (Jul 2025: 1,323 to Oct 2026: 1,292), ATP shows -2.3%. Use the filings (-8.0%, 1,665 to 1,531, Feb 2025 to Aug 2026) and drop the ATP -11.6% figure.
5. **Genesco is not a US athletic partner series.** Its total includes Schuh (UK and Ireland) and Johnston & Murphy. Without Genesco, the FL NA + DICK'S + Academy door base goes from 2,686 to 2,581 (-3.9%), and the decline is all Foot Locker. DICK'S and Academy are flat to up, and DICK'S square footage rose. That makes T2 weaker: it is a Foot Locker story, and DICK'S now owns Foot Locker and is closing weak mall doors while opening larger House of Sport stores.
6. **The China 2027 pipeline is not all clearance.** The locator lists 10 future-dated China Nike-owned stores: 5 FACTORY, 4 BEACON (full price) and 1 pop-up. Some future-dated opening dates in the feed are obvious entry errors (2922 and 2033), so treat these as plans, not facts.
7. **The framing of the US in-line cut is too strong for a SHORT signal.** US in-line doors were 29 in FY2021 and 85 in FY2024, mostly small Nike Live and Well Collective formats. The cut takes the fleet back toward its pre-2022 size. A LONG pitch can equally call it the cost-cutting and wholesale pivot management promised. The fact is strong, but its read-through to revenue is small, so as a direction signal it is weak SHORT, not moderate.

### Re-rated tests

- T1 (US in-line cut): the fact is confirmed. As a thesis signal: SHORT, weak.
- T2 (partner shelf): SHORT, weak to moderate. It is driven by Foot Locker, and the ATP -11.6% should not be used.
- T3 (China floor): SHORT, moderate rather than strong. Pou Sheng's half-on-half closures did accelerate, and the gap to domestic brands is real. But the Topsports area decline is steady, not accelerating, and the domestic control is softer once ANTA KIDS is included. The Topsports results for H1 FY26/27, due about 2026-10-22, could upgrade this.
- T3b (locator China): inconclusive, as the hunter said.
