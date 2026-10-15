# running_sellthrough: sell-through evidence for Nike running by routes other than SNKRDUNK and Tranco

Pulled 2026-10-14 (UTC). Question: is Nike's running recovery real full-price share gain or discount-driven (scoreboard crux 6)? Failed tests being rescued: (a) SNKRDUNK has no Pegasus trades; (b) Tranco rank for nike.com was inconclusive because retail controls moved the same way.

Rule stated in advance: Nike running review or sales proxies growing faster than Hoka, ASICS and Brooks at healthy prices points LONG; growth only with deep discounts or stock piling up points SHORT.

Verdict and numbers are in `research_notes/Long or short cruxes/running_sellthrough.md`. `evidence_summary.csv` has one row per measured result with its file. No logins, no accounts, no personal data in any request; generic browser user agent; sleeps between requests. Scripts are in `scripts/` (run from this folder with `python3 -I scripts/<name>.py`). Raw pulls are in `raw/` (all files far below 20 MB).

## Route log (every route, worked / partial / blocked)

| # | Route | What was tried | Result | Output |
|---|---|---|---|---|
| 1a | Amazon US Best Sellers, running (men's node 679286011, women's 679360011) | Public zgbs pages, 2 pages each, rank, ASIN, title, rating count | WORKED (one snapshot, top 80 ranks, 60 parsed per list). No Pegasus or Vomero in either list. | `amazon_bestsellers_running_2026-10-14.csv`, `amazon_bestsellers_brand_summary.csv`, `raw/html_snapshots/` |
| 1b | Amazon search pages and per-week review counts | `/s?k=` returned a bot-verification page (Akamai bm-verify). Product page `/dp/` loads but shows only the 8 top reviews, no "bought in past month" and no rank. All-reviews pages need login. | BLOCKED for weekly review counts and "bought in past month". PARTIAL via the rank lists. | none |
| 1c | Archived Amazon pages (Common Crawl index, Wayback) | Common Crawl index queried for 8 URL patterns over 10 crawls from 2024-06 to 2026-08; web.archive.org snapshots reset, CDX "Blocked by egress policy", archive.ph reset | BLOCKED. Common Crawl holds almost no captures of these retailers (48 queries completed, 1 capture found: one Zappos Hoka Clifton page, 2024-26). | `raw/cc_idx/all_logs.txt`, `raw/cc_probe2.tsv` |
| 2a | Fleet Feet UPC-level stock (size-run depth) | Public Typesense index (search-only key read from the fleetfeet.com page at run time, not stored). 32 current models, 11,300 colour x size rows: units per UPC, out-of-stock share, core-size cover. | WORKED, one day (2026-10-14). No archived baseline for the Pegasus 41 launch. | `raw/fleetfeet_upc_2026-10-14.csv.gz`, `fleetfeet_sizerun_depth.csv`, `fleetfeet_sizerun_by_brand.csv`, `fleetfeet_markdown_by_model.csv` |
| 2b | Fleet Feet product views (7, 30, 60 days) | Existing snapshot in `../reviews_sentiment/`, re-analysed by brand: views share, 30d vs prior 30d, stock per view | WORKED | `fleetfeet_brand_views.csv`, `fleetfeet_nike_models.csv`, `fleetfeet_top25_by_views.csv` |
| 2c | Zappos best-seller sort | `recentSalesStyle` sort parameter is silently ignored (server redirects to its semantic search; "sorted" and default pages are identical) | BLOCKED as a sales ranking. Default order is a relevance order, not sales. | `raw/zappos_bestsellers_2026-10-14.jsonl.gz` (kept only to show it) |
| 2d | Running Warehouse | Category pages are JS-rendered (no product list in HTML). Product pages load but carry 0 to 19 reviews per model. Sizes not in HTML. | BLOCKED for rank and stock, PARTIAL for reviews (too few) | `raw/html_snapshots/` |
| 2e | Road Runner Sports, JackRabbit, REI, Dick's, Hoka, ASICS, Brooks sites | RRS reachable but PowerReviews key not found (earlier note); JackRabbit 301; REI no connection; Dick's, Hoka, ASICS, Brooks 403 (earlier notes) | BLOCKED | none |
| 2f | nike.com live catalog discount by running model | Existing live catalog (32,225 rows, 2026-10-14) re-cut by model | WORKED | `nikecom_live_running_markdown_2026-10-14.csv` |
| 3a | Review velocity at Dick's (via Foot Locker Bazaarvoice syndication) | Dick's-sourced reviews by brand, family, generation, matched windows | WORKED, but Dick's syndication stepped up in Jun 2025 for every brand and lags at the end of the feed, so only matched windows inside the regime are used | `dicks_monthly_brand.csv`, `dicks_window_yoy.csv`, `dicks_nike_family_yoy.csv`, `dicks_gen_cohorts.csv` |
| 3b | Generation-over-generation first-90-day reviews | Dick's and Zappos | PARTIAL: Dick's launch dates before Jun 2025 are artefacts; Zappos samples are 30 to 330 reviews | `gen_over_gen_n90.csv` |
| 3c | Review velocity at REI, Amazon, Running Warehouse | See 1b, 2d. REI unreachable. | BLOCKED | none |
| 4a | Strava gear data | T3 articles on the Strava Mid-Year (2025-08-28) and Year in Sport (2025-12-03) reports opened. Strava's own 2026 mid-year report was not found. | PARTIAL (2025 only, before Nike's running recovery showed up in revenue) | `raw/html_snapshots/` |
| 4b | Marathon finisher shoe surveys (Marathon Investigation, Chicago, Berlin, NYC 2024 to 2026) | Search found a Chicago 2025 podium brand count only (Nike 2, adidas 2, Hoka 1, ASICS 1, six athletes). A search snippet quoting finisher shares (Nike 27.4 percent) was not on the opened page and is not used. | BLOCKED for finisher shares | none |
| 5a | Google Trends for model names | pytrends, two batches | BLOCKED (HTTP 429, as before) | `scripts/gtrends_try.py` |
| 5b | Reddit model mentions (r/RunningShoeGeeks) | Existing tagged posts, matched windows, shares | WORKED (shares only; archive sample drops from Oct 2025) | `reddit_rsg_brand_model_windows.csv` |
| 5c | YouTube review volume per model | Public search pages, 21 queries x 2 filters | PARTIAL: `estimatedResults` is unstable (Vomero Plus last year 121k vs Pegasus 42 3.5k), so not usable as volume. Median views of top results only. | `youtube_model_review_search.csv` |
| 6 | Circana, Running USA, SGB, Running Insight, Runstyle, Confluence Running press quotes | Opened: SGB 2026-08-17, Endurance Sports Wire 2026-08-14, Running Insight 2025-11-26, Runstyle 2025-11-21, Confluence Running (sheet dated 2026-02-18), Footwear Magazine 2026-04-08, Nike Q1 FY27 call (repo transcript) | WORKED for category and peer growth rates and run-specialty share; no brand-level Circana sell-through for Nike (paywalled) | `evidence_summary.csv` rows 18 to 20 |
| 7a | Cloudflare Radar domain ranking | radar.cloudflare.com 403 (earlier note) | BLOCKED | none |
| 7b | CrUX origin rank buckets | Existing monthly top-list buckets (GitHub mirror). BigQuery needs a GCP project. | PARTIAL: nike.com sits in the top 1,000 in every month since 2021, so it cannot move | `../apps_digital/crux_rank_buckets_long.csv` |
| 7c | Semrush modelled visits Apr to Sep 2026, nike.com vs run brands and retail controls | Existing snapshot re-cut | WORKED but brand-wide, 6 months, modelled | `semrush_visits_running_brands_vs_controls.csv` |

## Caveats you must carry

- Review counts are a unit proxy, not units. Dick's feed levels are driven by syndication and review programmes. Only shares and matched windows are used.
- Fleet Feet is one channel and one day. Nike only started its nationwide Fleet Feet rollout on 2026-04-09, so Nike's low stock may be a small allocation and not demand.
- Low Nike stock fits both "selling through" and "Nike deliberately cut supply" (management says it is reducing supply). The data here cannot separate them.
- No archived baseline for the Pegasus 41 launch exists in any reachable source. A true generation-over-generation size-run or rank comparison was not possible.
- To build a trend before Nov 19, run `scripts/run_daily_snapshots.sh` each day (Amazon rank lists and Fleet Feet UPC stock).
