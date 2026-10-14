# apps_digital: Nike apps and web traffic data hunt

Pulled 2026-10-14 (UTC). Question served: is NIKE Digital engagement still falling (NIKE Brand Digital -13% in Q1 FY27) or stabilising? Feeds crux questions 1 (NA sell-through), 5 (lifestyle bottom) and 7 (expectations).

No logins, no personal data in any request. Sleeps between requests in every script.

## Tidy files

| File | What it is | Rows / period |
|---|---|---|
| play_reviews_monthly.csv | Google Play written reviews per month per app and language (count, avg stars, 1 and 5 star share, versions) | 19 app-locales, Jan 2019 to Oct 13 2026 (Oct partial, flagged) |
| play_reviews_fq.csv | Same, summed to Nike fiscal quarters (Q1 = Jun-Aug), with YoY | FY2019Q3 to FY2027Q1 |
| nike_digital_growth_quarterly.csv | Reported NIKE Brand Digital YoY, FY20Q3 to FY27Q1 (calibration target) | 27 quarters |
| test_play_calibration.csv | Review YoY vs reported NIKE Digital YoY by quarter, peer pool, adidas, Nike DE/FR/JP | 27 quarters |
| test_play_latest.csv | Same-window YoY per app for Q4 FY26, Q1 FY27, Q2 FY27 to date (Sep 1 to Oct 12), Jul-Sep, Sep | 19 x 5 |
| web_semrush_history.csv | Semrush free overview: monthly visits (desktop, mobile), organic and paid search traffic, referring domains | 30 domains, Mar or Apr to Sep 2026 |
| web_semrush_country_raw.csv | Semrush traffic by country (Sep 2026) | 125 |
| web_hypestat_snapshot.csv | HypeStat monthly visits, MoM, uniques, bounce | 30 domains, snapshot |
| web_similarweb_snapshot_2026-10-14.csv | Similarweb Sep 2026 MoM change and ranks (read via WebFetch summary, not raw HTML) | 9 domains |
| test_web_traffic_cross_section.csv | Nike vs peer brand median change in visits and organic search | 6 windows |
| appstore_charts_brand_ranks_2026-10-14.csv | Every brand app found in Apple top-100 charts (free and grossing; Shopping, Health and Fitness, Lifestyle, Sports, All) | 40 storefronts, snapshot |
| appstore_shopping_topfree_best_rank_by_brand_2026-10-14.csv | Best Shopping top-free rank by brand and storefront | 40 storefronts |
| app_meta_snapshot_2026-10-14.csv | Google Play realInstalls (exact), ratings, written reviews; App Store rating counts and star histograms in 13 storefronts | snapshot |
| ios_rating_velocity_us.csv | New US App Store ratings between the repo snapshot (committed 2026-10-13 20:22 UTC) and lookup pulls on 2026-10-14 | 11 apps |
| snkrs_products_tidy.csv | Nike SNKRS public launch feed: every product in the feed, launch method (LEO/DAN draw vs FLOW), price, discount, availability, size-level stock (HIGH/MEDIUM/LOW/OOS) | US, GB, JP; feed reaches back to about Dec 2023 (API anchor cap 1000 threads) |
| snkrs_cohort_monthly.csv, snkrs_cohort_quarterly_age14plus.csv | SNKRS launch cohorts: count, still available, deep stock, discounted, draw share | by market and month or quarter |
| crux_rank_buckets_long.csv | Chrome UX Report top-list rank buckets (1k, 5k, 10k, 50k...) for footwear and retail origins | global Feb 2021 to Sep 2026; US and GB Jan 2025 to Sep 2026 |

## Sources and methods

1. Google Play reviews: google-play-scraper 1.2.x (`reviews`, Sort.NEWEST, 200 per call, 0.6 s sleep), stopping at 2019-01-01 or 150k rows (US English) or 40k (DE, JP, FR). Raw: raw/play_reviews/*.csv.gz holds only timestamp, stars, thumbs, app version and a reply flag. No text and no user names kept. Script: scripts/pull_play_reviews.py. Note the language filter is a language, not a country: en_us means English-language reviews worldwide, mostly US.
2. Google Play app metadata: google-play-scraper `app()`. Script: scripts/pull_app_meta_snapshot.py.
3. Apple App Store pages: https://apps.apple.com/{cc}/app/id{id} (ratingCount, ratingAverage, ratingCounts histogram embedded in page JSON). Same script.
4. Apple top charts: legacy public iTunes RSS https://itunes.apple.com/{cc}/rss/{topfreeapplications|topgrossingapplications}/limit=200/genre={6024,6013,6012,6004}/json (returns top 100). Raw JSON (gzipped after the pull) in raw/appstore_charts/2026-10-14/; full chart table raw/appstore_charts_all_2026-10-14.csv.gz. Scripts: pull_appstore_charts.py, clean_appstore_charts.py.
5. iTunes lookup API: https://itunes.apple.com/lookup?id=...&country=us. Prior snapshot from branch claude/wonderful-franklin-u31n4e data/altdata/appstore_ratings_snapshot_2026-10-13.csv. Script: ios_rating_velocity.py.
6. Semrush free overview pages https://www.semrush.com/website/{domain}/overview/ (data in astro-island props). HypeStat https://hypestat.com/info/{domain}. Raw HTML gzipped in raw/web_traffic/2026-10-14/. Script: pull_web_traffic.py.
7. Similarweb https://www.similarweb.com/website/{domain}/ read with WebFetch (curl gets a 202 bot challenge). Numbers are from a model summary of the page, so treat them as approximate; the "visits" label on the page is ambiguous.
8. Nike SNKRS feed: https://api.nike.com/product_feed/threads/v3/?anchor=..&count=50&filter=marketplace(US)&filter=language(en)&filter=channelId(010794e5-35fe-4e32-aaff-cd2c74f89d61)&filter=exclusiveAccess(true,false). Public JSON behind nike.com/launch. Raw pages in raw/snkrs/{US,GB,JP}/. Scripts: pull_snkrs_feed.py, clean_snkrs.py.
9. CrUX top lists: https://raw.githubusercontent.com/zakird/crux-top-lists/main/data/{global|country/xx}/YYYYMM.csv.gz (monthly, built from Google's CrUX BigQuery). Only matching brand origins kept (raw/crux/). Script: pull_crux_toplists.sh. Country pull stopped after US and GB (DE partial, dropped) because the buckets are too coarse to move for nike.com.
10. NIKE Digital growth: data/nike_filing_facts.csv (repo) plus Q4 FY24 and Q4 FY25 8-K Ex. 99.1 (SEC, opened 2026-10-14).

## Blocked or not usable (2026-10-14)

- web.archive.org and archive.org (CDX and availability API): connection reset by the proxy relay / HTTP 429. So no archived App Store pages, Play pages, Similarweb pages or old RSS charts. This is why chart ranks and installs are snapshots only.
- index.commoncrawl.org: connection reset (data.commoncrawl.org reachable, not used).
- Google Trends via pytrends (app terms "snkrs", "nike app", "nike run club", "adidas app"): HTTP 429 on every attempt; script kept (pull_gtrends_apps.py) for a later re-run.
- BigQuery (CrUX, HTTP Archive): no credentials. Used the GitHub mirror instead.
- GitHub API for zakird/crux-top-lists: not enabled for this session; git clone and raw.githubusercontent.com work.
- data.similarweb.com API 403; similarweb.com via curl 202 challenge (WebFetch worked); appbrain.com 403; socialblade.com 403; radar.cloudflare.com 403; androidrank.org redirect; Sensor Tower app pages need login.
- Apple amp-api reviews (no public token found in page bundle); Apple customer-review RSS pages beyond page 1 return empty feeds.

## Caveats

- Review counts are an engagement proxy, not users. App developers can change review prompts. Checks: Nike app average stars and 5-star share rose in 2026 (4.33 avg, 76% five-star vs 4.18 and 72% in 2025), which is what keeps prompting looks like, so the volume drop is not explained by Nike turning prompts off. SNKRS jumped in Q3 2026 with a jump in stars (1.5 to 3.4), which does look like a new prompt, so SNKRS volume is excluded from conclusions. Dick's jumped about 10x from Q4 2025 (prompt change); it is excluded from the peer pool.
- Calibration (FY23Q1 to FY26Q4): review YoY tracks the level of NIKE Digital growth (r = 0.83) but not quarter-to-quarter turns (direction agrees 52% of the time). Use it for regime, not for one quarter's beat or miss.
- Semrush and HypeStat histories cover only about 6 months, so they are cross-sectional (Nike vs peers over the same months), not YoY.
- SNKRS feed: survivorship is possible (old threads may leave the feed), and availability is measured today, so older cohorts had longer to sell out. Launch method (draw vs FLOW) is set at launch and does not have that age bias.
- CrUX buckets are coarse: nike.com sits in the global and US/GB top 1,000 in every month, so it cannot show a decline of the size Nike reports.
