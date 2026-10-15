# Hiring and workforce data hunt (key: `hiring`)

Pulled 2026-10-14 (UTC). No logins, no personal data in any request. All scripts are in `scripts/` and re-runnable from this folder.

## Tidy outputs (this folder)

| File | What it is | Rows / period |
|---|---|---|
| `live_postings_workday_2026-10-14.csv` | Census of every live Nike posting (Workday sites `nke` global and `nke2` US stores) plus Deckers, with req id, posting start date, country, legal entity, category | 1,303 Nike + 400 Deckers, snapshot |
| `nike_open_postings_series.csv` | Total open Nike postings shown on the careers site, read from archived pages | 61 points, Oct 2019 to Oct 2026 |
| `req_frontier_points.csv`, `req_velocity_monthly.csv` | Highest Workday requisition number seen at each date and implied requisitions opened per month and trailing 12 months | Sep 2023 to Oct 2026 |
| `cc_listing_counts.csv` | Every archived listing page fetched: URL, filter, total | 1,130 pages |
| `cc_job_objects.csv`, `cc_job_objects_bucketed.csv` | Job records embedded in archived listing pages (req id, country, family, category, legal entity), with function bucket | 22,160 rows |
| `composition_by_period.csv` | Function and geography mix of open postings by half-year, plus the live census and the 2026-10-13 careers corporate census from the repo | 2019H2 to Oct 2026 |
| `h1b_lca_rows.csv`, `h1b_lca_clean.csv` | H-1B Labor Condition Applications (DOL disclosure data as republished by h1bdata.info) for Nike entities and 10 peers, deduplicated, with role group | 3,600+ rows, Sep 2019 to Jun 2026 |
| `h1b_lca_quarterly_by_firm.csv`, `h1b_lca_quarterly_nike_by_role.csv` | Quarterly LCA counts | 2019Q3 to 2026Q2 |
| `qcew_washington_county_or.csv` | BLS QCEW, Washington County OR (Nike World HQ), private NAICS 551114 corporate offices plus comparison industries | 2018Q1 to 2026Q1 |
| `warn_notices_warntracker.csv` | WARN notices for Nike, Converse and peers from warntracker.com company pages | 2009 to 2026 |
| `peer_live_snapshot_2026-10-14.csv` | Live posting totals and facets for adidas, On, Deckers, Nike | snapshot |
| `cc_adidas_listing_counts.csv`, `adidas_open_postings_series.csv` | adidas careers totals from archived pages | 2022 to Oct 2026, noisy |

## Sources and methods

1. **Nike Workday public job API** (`https://nike.wd1.myworkdayjobs.com/wday/cxs/nike/nke/jobs` and `/nke2/jobs`, POST JSON, no auth). Found by reading `careers.nike.com/jobs` links. Paged 20 at a time, then one GET per posting for start date, country and hiring entity. Categories attached by re-querying with each `jobFamilyGroup` facet. Scripts: `pull_workday.py`, `tag_workday_categories.py`, `build_live_tidy.py`. Same method for Deckers (`deckers.wd5`, site `Deckers`) and a facet-only pull for VF (`vfc.wd5`, 1,254 postings, not used in tests).
2. **Common Crawl archives of jobs.nike.com and careers.nike.com** (the Wayback Machine was blocked, see below). The Common Crawl index server was also resetting connections, so `cc_cluster_lookup.py` binary-searches each crawl's `cluster.idx` on `data.commoncrawl.org` with HTTP Range requests and fetches only the matching compressed index blocks (72 crawls, Jan 2019 to Sep 2026, status-200 captures only, in `raw/commoncrawl/cdx_*.jsonl.gz`). `cc_extract_listings.py` then range-fetches up to 30 listing pages per crawl and parses (a) the total count (`"pagination":{...,"count":N}` on the old site, `window.__PRELOAD_STATE__.jobSearch.totalJob` on the new site) and (b) the embedded job records.
3. **Requisition velocity** (`build_req_velocity.py`). Nike's Workday requisition IDs (R-xxxxx) are issued in sequence from mid-2023 (before that a different ID system). The highest 5-digit ID seen in each crawl, dated by its capture, gives a frontier; the slope is requisitions opened. A separate 6-digit pool (R-7833xx to R-7840xx, 274 IDs, all US seasonal store roles, first seen March 2026) is excluded; it would add at most about 700 requisitions to Mar to Sep 2026.
4. **H-1B LCAs**: `https://h1bdata.info/index.php?em=<employer>&year=<yyyy>`, 2019 to 2026, for search terms nike, nike inc, nike usa, nike retail services, nike ihm, converse inc, adidas, deckers, lululemon, under armour, on running, vf corporation, skechers, new balance athletics, foot locker (`pull_h1bdata.py`, `build_h1b_tidy.py`). Role groups are assigned from job title keywords.
5. **BLS QCEW open data**: `https://data.bls.gov/cew/data/api/<yyyy>/<q>/area/41067.csv` (`pull_qcew.py`). 2026Q2 onward not yet published.
6. **WARN**: warntracker.com company pages (`pull_warntracker.py`); Oregon HECC list searched for "nike" (`raw/warn_states/or_nike.html`); California EDD WARN reports FY2019-20 to FY2025-26 plus current xlsx (PDFs grepped for brand names, then deleted; the matching lines are in `raw/warn_states/ca_warn_brand_lines.txt`); Tennessee WARN page (`raw/warn_states/tn_reports.html`).
7. **Peers live**: adidas `careers.adidas-group.com/jobs?team=<team>` counter; On Eightfold API `jobs.on.com/api/pcsx/search?domain=on.com`; Deckers Workday (`pull_peers_live.py`). adidas archived totals: `cc_extract_adidas.py`.

## Blocked or empty (do not retry blindly)

- web.archive.org (CDX and pages): connection reset through the proxy all session; WebFetch also refused. archive.org/wayback/available returned 429. arquivo.pt CDX 403. archive.ph reset.
- index.commoncrawl.org: worked for one query, then reset (worked around via cluster.idx, method 2).
- Glassdoor, Indeed, Comparably live pages: 403 or 401. Common Crawl has essentially no Glassdoor captures for Nike (1 capture in 2023-50; 0 in 12 crawls from Oct 2025 to Sep 2026 across 9 Glassdoor country domains). So no employee rating or CEO approval series.
- LinkedIn: not attempted live (login wall); no usable archive.
- USCIS H-1B Employer Data Hub CSVs: 403.
- Big Local News WARN repo (github biglocalnews/warn-github-flow): no data committed.
- lululemon, Under Armour (SuccessFactors), Skechers, New Balance, Puma, Columbia: no public JSON job endpoint found quickly.

## Caveats

- Open postings are a stock, not a flow. Seasonal store hiring drives most swings (Oct peaks).
- The careers site moved from jobs.nike.com (old) to careers.nike.com (new) around Feb 2025; YoY changes that straddle the move are less reliable. From Feb 2025 on, both years are on the new site.
- Old-site embedded job records come from the first page of results and from filtered searches, so the old-site function mix (2019 to 2024 in `composition_by_period.csv`) is NOT representative. Only the new-site rows (2025H1 onward) and the two censuses should be used for mix.
- Archived listing samples (new site) are random result pages, not a census. The two censuses (live Workday Oct 14, careers corporate Oct 13) use slightly different taxonomies; the Oct 13 census uses the same job-family field as the archived new-site samples.
- Requisition IDs count all requisitions (global, corporate and stores). Frontier dates use capture time, which lags creation by a few days to weeks.
- QCEW NAICS 551114 in Washington County is mostly Nike WHQ but includes other head offices (for example Columbia Sportswear).
- H-1B LCAs include extensions and transfers, not only new hires, and 2026Q2 data ends 2026-06-19.
- adidas archived totals come from 1 to 4 pages per crawl, some apparently from language sub-sites (values like 13 or 17 and a constant 404 placeholder were dropped or should be ignored).

## Key numbers (for the tests in the summary)

- Open postings, YoY: Jan to Jun 2026 ran 17% to 24% below 2025; Jul +3%, Aug +20%, Sep +9%; live Oct 14 2026 1,303 vs 1,307 on Oct 8 2025 (flat).
- Requisitions opened: trailing 12 months 35.8k (Jul 2025 peak), 22.1k (Jul 2026 trough), 23.9k now (-24% YoY). Jun to Sep 2026 9.3k vs 8.0k a year earlier (+16%). Dec 2025 to May 2026 about 1.6k per month vs 2.3k to 3.8k a year earlier.
- Corporate mix (careers taxonomy): product and design 15.4% (2025H2) to 19.4% (2026H1) to 25.2% (2026Q3) to 36.2% (Oct 13 census, 138 of 381). Sales and merchandising 23.3% to 20.9% to 16.0% to 10.2%. 72% to 81% of tech postings are in India.
- H-1B LCAs, Jan 1 to Jun 15: Nike 203 (2025) to 136 (2026), -33%; tech/data 141 to 64; product/design/innovation 20 to 38; commercial 7 to 10.
- QCEW Washington County corporate offices: 17,855 (Jun 2023) to 16,066 (Mar 2026); YoY -6.6% (Q1 2025) easing to -1.1% (Q1 2026). Excludes the Apr 2026 tech cuts.
- China: share of all postings 11.7% (2025H2), 7.2% (2026H1), 9.9% (2026Q3), 9.3% (Oct 14). China share of store postings 5.4%, 5.7%, 4.5%, 3.9%. China share of corporate postings 21.6%, 9.6%, 18.6%, 23.1% (88 of 381, mostly product development and design at Nike Sports (China)).
- WARN: last Nike notices Jan 2026 (Memphis 583, Byhalia MS 193, distribution automation) and Oct 2025 (New York 87). No Oregon notice for 2025 or 2026 despite the Apr 2026 tech cut. Pace role decisions start 2027.
- Peers: adidas archived totals Aug to Oct 2026 about +23% to +25% YoY (noisy); live adidas 1,194, Deckers 400, On 57.

## Checker review

Reviewed 2026-10-14 by a second agent. Recomputations are in `scripts/checker_recompute.py`.

### Re-pulls from the original sources (all matched)

- Workday API (POST `/wday/cxs/nike/{nke,nke2}/jobs`): nke 835 + nke2 478 = 1,313 later on Oct 14. The file has 1,303 (pulled earlier the same day). The newest IDs are R-95612, R-95601 and R-95597, above the file's frontier of 95,567, which fits the frontier still advancing. careers.nike.com/jobs `totalJob` also read 1,313. So the archived `totalJob` counts and the Workday totals measure the same thing.
- Common Crawl WARC range re-fetch: careers.nike.com/ko/jobs on 2025-10-11 gave `totalJob` 1396, and /jobs/page/23 on 2026-08-08 gave 1076. Both equal `cc_listing_counts.csv`.
- QCEW API, area 41067, NAICS 551114 private: 2026Q1 16,111 / 16,026 / 16,066 (OTY -1.1%), 2025Q1 16,200 / 16,228 / 16,241 (-6.6%), 2023Q2 month 3 17,855. All match.
- h1bdata.info, `em=nike inc`: rows for "Director, Energy White Space Product Design" (5/29/2026), "Director, Global Basketball and Kobe Concept Design" (3/11/2026) and "Senior Director, Applied Footwear Research" (4/15/2026) match on salary and dates. Data end 2026-06-19.
- warntracker.com/company/nike: shows Byhalia MS 193 (2026-01-26), Memphis 583, NY 87 and OR 740 (2024). It still reads "15 notices, Apr 2009 to Apr 2026". Matches.

### Cleaning checks

- Live census: no duplicate req IDs. nke and nke2 do not overlap.
- `cc_job_objects.csv` has 22,160 rows, but 15,668 of them repeat the same requisition within a crawl because the same job appears on several language sub-sites. `cc_job_objects_bucketed.csv` is correctly de-duplicated to 5,635 rows with 0 repeats within a crawl. The summary's row count of 22,160 for the bucketed file is wrong; the real count is 5,635.
- Periods in the composition table pool crawls, so a requisition open across several crawls counts more than once. That makes the shares averages of the stock of open postings, not counts of new postings. Long-open, hard-to-fill roles (senior design jobs, for example) are over-weighted.
- H-1B dedup across overlapping search terms is fine. The rules give 203 to 136 (Nike, Jan 1 to Jun 15) exactly as reported.
- Requisition frontier, survivorship and splice: the pre-Feb-2025 old-site points rest on only 13 to 25 IDs per crawl, so those frontiers are understated. That inflates the Dec 2024 to Feb 2025 flows (3.7k to 3.8k a month) that the summary uses as the "year earlier" base. The monthly series also joins lagged Common Crawl points (dated at last capture) to an unlagged live endpoint on Oct 14, which inflates Sep 2026 (3,264). Using only the dense crawls (500 or more IDs each), the conclusions still hold:
  - Late Mar to late May: 2,547 a month (2025) vs 1,565 (2026), -39%.
  - Feb to Sep: 2,355 a month vs 1,821, -23%.
  - Jun to Sep: 1,805 a month vs 2,057, +14%. Both windows end before the late-September seasonal batch, so seasonal timing does not drive this.

### Tests re-run

1. **Hiring growth or cutting.** Holds, with one correction: the October reading is not "flat". The 2025-43 crawl spans Oct 5 to 12, during which the 2025 seasonal batch lifted the total from 1,050 to 1,396. The crawl median (1,306.5, dated Oct 8) is a mid-batch value. On matching dates, Oct 11 to 12, 2025 read about 1,385 against 1,303 to 1,313 on Oct 14, 2026, which is **about -5% to -6% YoY**. Also, the summary says 2026 seasonal postings came "2 to 3 weeks later". The data show the opposite: 2026 US store postings arrived in the week of Sep 21 (208 of 474 live US store postings), while the 2025 jump came on Oct 7 to 10. The 2026 batch was about 2 weeks earlier, and the Sep-to-mid-Oct rise was smaller: about +220 in 2026 vs about +390 in 2025. Jan to Jun -17% to -24% and Aug +20% are confirmed. Sep +9% is confirmed (Sep 9, before both batches; the 835 reading on Sep 11 is an outlier that the median correctly drops). QCEW is confirmed. Verdict: NEUTRAL, moderate. Flow (requisitions) has turned up about +14%, but the stock of open postings is still slightly below last year in October.
2. **Mix shift to product.** Direction holds, but the headline overstates it. The rise from 15% to 36% mixes in geography: China product roles went from 4% to 21% of archived product postings, and offshored tech moves the denominator. On a like-for-like basis:
   - US only, product share: 32.2% (2025H2), 34.4% (2026H1), 45.0% (2026Q3), 43.6% (Oct 13 census).
   - Excluding China, product share: 18.9%, 19.7%, 24.5%, 29.0%.
   - US sales and merchandising share: 16.6%, 22.2%, 10.8%, 7.3%.

   The H-1B result gets stronger. Product LCAs with an Oct 1 start (cap-season new-hire petitions, not amendments or extensions) were 11 in 2024, 11 in 2025 and 31 in 2026 (Jan 1 to Jun 15). So the +90% is not a re-titling artefact from the reorg, even though "Energy" titles appear. Caveat: cap petitions often convert existing OPT staff, so this is not all net new headcount. The fall in tech LCAs (141 to 64) sits in non-cap filings and fits tech moving offshore. Verdict: LONG for the long-run product engine, moderate. The US-only rise is about 11 to 12 points, not a doubling.
3. **China floor.** Recomputed shares match: China share of store postings 3.9% (35), China share of corporate postings 23.1% (88 of 381, of which 53 are product roles). Verdict: SHORT, weak, as stated. Store postings are a small and noisy sample.
4. **Peers.** The H-1B peer comparisons rest on tiny counts (Jan 1 to Jun 15):
   - adidas 7 to 9 (the "+29%")
   - Deckers 14 to 16
   - Skechers 4 to 12
   - lululemon 20 to 13

   Nike's -33% matches lululemon's -35%, so part of the drop is likely industry-wide H-1B policy (the 2025 fee proclamation) and not Nike-specific. The adidas archived totals come from one page per crawl and swing between 649 and 1,228 from month to month. Verdict: uninformative, weaker than "weak SHORT".

### Bottom line

Every source re-pulled cleanly and matches the files. The core finding holds: requisition flow cut about 23% to 39% YoY through spring 2026, then turned up about 14% in Jun to Sep. Three corrections:
- October open postings are about -5% YoY, not flat.
- The 2026 seasonal batch came earlier than in 2025, not later.
- The product-share jump is about half geography mix. The US-only rise is 32% to 44%, and the H-1B cap-season evidence for product hiring is stronger than reported.
