# Resale and secondary market data hunt (key: resale_secondary)

Pulled 2026-10-14 (UTC). Every pull was public: no login, no email or personal details in any request, robots.txt checked, and requests spaced 0.6 s apart for each worker.

## What is new here

Before this pull, the repo's resale evidence was US/StockX snapshots and Wayback captures, mostly for Jordan. This folder adds three things:

1. **SNKRDUNK (Japan's largest sneaker resale marketplace).** Its public JSON gives a **full daily price history of new-condition trades** for every product from listing to today: 4,626 products, 32 model lines, Nike, Jordan, adidas, New Balance, ASICS, Onitsuka Tiger, On, Hoka, Salomon and Puma, Dec 2019 to Oct 13, 2026. It also gives each product's Japan release date and Japan retail price (yen). This is the first cross-brand resale time series in the repo.
2. **Laced (UK resale).** The public product API carries a `sold_in_last_28_days` count. Cross-section only: 2,733 products in 32 collections.
3. **SneakerPing brand table (US, StockX, GOAT and eBay sales, Aug 2026) and a StockX brand facts table.** Both are small tables compiled from opened pages.

## Files

| File | Rows | What it is |
|---|---|---|
| `snkrdunk_products.csv` | 4,626 | One row per product: code, name, brand group, model line, collab flag, JP release date, JP retail (JPY), trade days, last-20-trade velocity |
| `snkrdunk_product_month.csv` | 54,037 | Product x month: median of daily new-condition trade prices (JPY), trade days (days with at least 1 new trade), premium vs current JP retail |
| `laced_products_sold28d.csv` | 2,733 | Laced UK: product, brand, collection, release year, units sold in last 28 days, lowest ask (GBP) |
| `sneakerping_brand_below_retail_aug2026.csv` | 12 | Share of Aug 2024 to Aug 2026 releases whose last sale was below retail, by brand (US marketplaces) |
| `stockx_public_brand_facts.csv` | 14 | StockX brand ranks and growth from press coverage, 2024 to H1 2026 |
| `usdjpy_monthly_ecb.csv` | 46 | USD/JPY monthly average (ECB reference rates via api.frankfurter.app), used for the FX control |
| `test_A_same_product_yoy_price_by_brand.csv` | | Monthly median same-product YoY resale price change, by brand |
| `test_A2_q3_yoy_by_line_brand.csv` | | Q3 (Jul to Sep) same-product YoY change by model line and brand, 2024, 2025, 2026 |
| `test_B_trade_days_by_brand_month.csv`, `test_B2_trade_days_fixed_cohort.csv`, `test_B3_trade_days_jan_sep_yoy_by_brand.csv` | | Resale activity (trade days) by brand |
| `test_C_launch_premium_products.csv`, `test_C_launch_premium_by_brand_half.csv` | | Resale premium vs JP retail in months 1 to 3 after release, by release half-year |
| `test_D_laced_units_by_brand_cohort.csv` | | Laced UK 28-day units by brand and release-year cohort |
| `raw/` | | Raw pulls: SNKRDUNK search pages (JSON), universe, history (4 gzip JSONL shards, each under 1 MB), Laced collections and products (JSONL), SneakerPing HTML, FX JSON |

## Sources and methods

| Source | URL pattern | Method | Status |
|---|---|---|---|
| SNKRDUNK search | `https://snkrdunk.com/en/v2/search?keyword=<kw>&categoryIds=1&perPage=50&page=1..3` | 32 keywords, up to 150 products each, relevance order | OPENED |
| SNKRDUNK product | `https://snkrdunk.com/v2/products/<style code>?type=sneaker` (`?type=sneaker` is required; without it the API returns "invalid id") | JP id, `releasedAtJP`, `regularPriceJP` | OPENED |
| SNKRDUNK trade history | `https://snkrdunk.com/v3/products/<jp id>/trading-history?range=all&condition_code=new_unused` | Daily chart points (one per day with a trade) plus the last 20 trades | OPENED |
| Laced collection pages | `https://www.laced.com/<brand>/<collection>` (`__NEXT_DATA__`) | Top 100 listed products per collection | OPENED |
| Laced product API | `https://www.laced.com/api/v1/products/<slug>` | `sold_in_last_28_days`, `release_year` | OPENED |
| SneakerPing report | `https://www.sneakerping.com/sneaker-resale-market-report` (18 Aug 2026) | Brand table copied | OPENED |
| StockX facts | FashionUnited and Fashion Dive articles (URLs in the CSV) | Transcribed | OPENED or SNIPPET as marked |
| FX | `https://api.frankfurter.app/2023-01-01..2026-10-13?from=USD&to=JPY` | Daily ECB rates averaged by month | OPENED |

Re-run the pulls and tests with:
```
python3 -I scripts/snkrdunk_pull.py OUTDIR 3 <shard> 4    # run shards 0..3 in parallel
python3 -I scripts/snkrdunk_clean.py OUTDIR
python3 -I scripts/laced_pull.py OUTDIR
python3 -I scripts/laced_clean_test.py OUTDIR
python3 -I scripts/tests.py OUTDIR
python3 -I scripts/robustness.py OUTDIR
```

## Definitions

- **Trade day:** a day on which the product had at least one new-condition trade on SNKRDUNK. The chart has one point per day, so trade days are a volume proxy capped at 1 per product per day. Only 4% to 8% of product-months hit the cap (27 or more days) in 2026, so the cap rarely binds. Where it does bind, it is mostly on Nike and Jordan items such as the Panda Dunk and white AF1, so it understates Nike, not rivals.
- **Same-product YoY:** log change of a product's monthly median price versus the same month a year earlier. It requires at least 3 trade days in both months, excludes collabs, and excludes products released less than 6 months before the base month, which removes launch decay. The median is taken across products.
- **Launch premium:** median price in months 1 to 3 after the JP release month, divided by JP regular retail, minus 1. Collabs are excluded.

## Known gaps and caveats

- **SNKRDUNK is Japan.** Japan is part of Nike's APLA segment, not North America. It is a read on global sneaker-culture demand and on supply discipline, not on US sell-through.
- **Prices are in yen.** The yen weakened about 6% from Sep 2025 (147.9 per USD) to Sep 2026 (156.4). That lifts every brand's yen resale prices by roughly the same amount, so the brand comparisons hold but the absolute YoY figures are flattered by about 6 points.
- **Retail price is today's JP regular price.** If Nike raised JP retail during 2025 and 2026, that would lower measured premiums for recent Nike releases, which biases against a Nike improvement.
- **The universe is set by today's search relevance.** Products de-listed from SNKRDUNK search are missing, and the brand mix (about 150 products per model line) is my choice. Use within-brand changes and the Nike vs rival comparisons, not share levels.
- **Laced counts are small.** The 2,733 products sold 724 pairs in 28 days, and the data is a single snapshot with no history.
- **Resale volume is not retail demand.** adidas, New Balance, ASICS and On sell mainly at retail, so their resale activity is thin by nature.
- **Performance running barely trades on resale.** Pegasus: 149 products, zero trades in the Q3 test sample. On and Hoka have very few trades. Resale cannot test running quality.

## Sources tried and blocked (2026-10-14)

- StockX product pages and API: HTTP 403 (Cloudflare).
- GOAT web-api (`buy_bar_data`, search): HTTP 403. It worked on 2026-10-13 for another session.
- GOAT Constructor.io search API (`ac.cnstrc.com`): "Access restricted".
- eBay sold listings: HTTP 403.
- Flight Club, KicksCrew, Grailed, Depop, Mercari US: HTTP 403.
- Mercari JP API: HTTP 403.
- Restocks, Campless: connection failed.
- KREAM (Korea): HTTP 500.
- web.archive.org (snapshots and CDX): connection reset, or HTTP 403 on http. Only the `archive.org/wayback/available` lookup works, and it returns timestamps, not content.
- archive.ph, timetravel.mementoweb.org: connection failed.
- Common Crawl index: tunnel closed.
- Soldout (Korea): robots.txt disallows ClaudeBot and other AI crawlers, so not used.
- Yahoo! Auctions JP closed search: robots.txt disallows `/closedsearch`, so not used.
- SneakerPing `/api/`: robots.txt disallows it for generic agents, so not used (the public report page was used).
- Dewu (web): no product pages; the app-only API needs signed requests.
- Poizon (web): empty response to scripted requests, and robots.txt disallows `/search`.
- Hypeboost: no product links in server HTML.
- Reddit JSON: HTTP 403.
- FRED CSV: connection failed (ECB rates via frankfurter were used instead).
- Wikipedia pageviews API: worked, but was rate limited for some articles. It is not used here because it is outside the resale scope.

## Checker review

Reviewed 2026-10-14 by a second session. Scripts added: `scripts/checker_deep_pull.py` (pulls search page 4, ranks 151 to 200, for 8 lines), `scripts/checker_deep_test.py` (writes `checker_deep_rank_compare.csv`). New raw files: `raw/checker_deep_*.jsonl.gz` (401 products, of which 49 overlap the original universe and are ignored).

### Re-pulls (does the raw data match the source?)

- **SNKRDUNK product records (3/3 match).** Panda Dunk DD1391-100 (id 22264, JP release 2021-07-01, retail 15,400), AJ1 High Patent Bred 555088-063 (id 5958, 2022-01-15, 19,250), Samba OG B75806 (id 33168, 2023-10-16, 15,950). All match `snkrdunk_products.csv`.
- **SNKRDUNK trade histories (12/12 product-months match).** For the same 3 products, trade days and median daily price for Jul and Sep 2025 and Jul and Sep 2026 match `snkrdunk_product_month.csv` exactly (for example Panda Sep 2025 30 days at 9,758 and Sep 2026 25 days at 11,298; Samba Sep 2026 22 days at 13,344). The chart has one point per day, no duplicate dates, and no downsampling of older years (Panda has 365 points in each of 2021 to 2024).
- **Search order is stable.** Page 1 for "nike dunk low" and "adidas samba" re-pulled: same 50 products in the same order.
- **Laced (3/3 match).** `sold_in_last_28_days` for Black Cat AJ4 2025 (51), its GS version (21) and Kayano 14 Metropolis (17) match. No duplicate slugs.
- **SneakerPing (match).** The page (now redirects to sneakerping.com without www) shows Jordan 605 / 70.7% / -20.0%, Nike 1,591 / 61.6% / -12.4%, New Balance 382 / 61.0% / -13.8%, adidas 378 / 59.8% / -10.7%, ASICS 133 / 42.9% / +4.8%. Note: last sales were observed only between 4 July and 18 August 2026, so this is one snapshot, not a trend.
- **FX (match).** USD/JPY Sep 2025 147.93, Sep 2026 156.39, Jul 2026 162.51 re-pulled from frankfurter (the API now 301-redirects; follow redirects).
- **Rebuild.** Running `snkrdunk_clean.py`, `tests.py` and `robustness.py` on the raw shards reproduces both tidy CSVs byte for byte and every headline number in the summary.

### Cleaning issues found

1. **The universe is a heavily truncated, popularity-ranked sample, and the truncation differs by brand.** 31 of 32 keywords hit the 150 cap. SNKRDUNK reports far more matches: Dunk Low 1,965, AF1 4,003, AJ1 High 952, AJ1 Low 1,350, Samba 1,003, but Kayano 14 only 159, Gel-NYC 200, Gel-1130 179. So Nike lines are sampled at 4% to 16% of their catalog and several rival lines at 75% to 100%. Within the sample, the 2025 to 2026 trade-day change falls steeply with search rank (Nike+Jordan: ranks 1 to 50 +9.4%, 51 to 100 -12.9%, 101 to 150 -22.4%; rivals -16.7%, -32.8%, -43.7%). Relevance is clearly correlated with current trading. The README's caveat mentions search relevance but not that this selects on the outcome.
2. **The deeper-rank test clears the main worry for Test B.** I pulled ranks 151 to 200 for Dunk Low, AJ1 High, AF1, AJ4, Samba, Gazelle, 2002R and Mexico 66. Jan to Sep trade days: Nike+Jordan -4.6% (ranks 151 to 200) vs -2.7% (top 150); rivals -61.2% vs -31.5%. The deeper sample makes rivals look worse, not Nike. The relative result holds.
3. **The "-2.4%" level for Nike+Jordan is flattered by new releases.** On a fixed cohort (products released before 2025), trade days are Nike+Jordan -22.3% and rivals -44.7%; for products released before 2024, -18.2% vs -34.1%. Nike's resale activity is shrinking in absolute terms; it is shrinking about half as fast as rivals'.
4. **The daily cap matters more than the README says.** Only 5.7% (Nike+Jordan) and 2.6% (rivals) of 2026 product-months are at 27 or more days, but those months hold 29% and 24% of 2025 trade days. The cap compresses changes in both directions; it does not only understate Nike. I checked: excluding every product that was capped in any 2025 month gives Nike+Jordan -0.2% vs rivals -22.1%, so the cap does not drive the result.
5. **FX effect is about 8 points, not 6, for the Q3 test.** Q3 average USD/JPY was 149.12 (2024), 147.51 (2025), 159.23 (2026), so +7.9% in Q3 2026. In USD terms the same-product YoY is Nike+Jordan -12.3% (Q3 2025) to -9.5% (Q3 2026) and rivals -10.1% to -5.5%. In dollars, Nike resale prices are still falling, just more slowly. Whether to deflate a domestic yen market by USD/JPY is debatable (Japanese buyers pay yen), so the yen number and the USD number bracket the truth.
6. **Retail price direction is stated backwards.** `regularPriceJP` looks like the latest restock price, not the launch price: the Panda Dunk (2021 release) carries 15,400, above its 2021 Japan price. If Nike raised JP retail after a 2025 release, that release's premium is understated, which flatters the 2026H1 vs 2025 improvement. The README says the bias runs against a Nike improvement; it can run in its favour. The size cannot be measured from this data.
7. Minor: 2 products are miscoded to brand groups "asics" and "newbalance" (typo names: "Asiccs", "New Blance"); they drop out of `tests.py` but are counted as rivals in `robustness.py`. Immaterial.

### Re-run of the tests

- **Test A (same-product YoY price).** Reproduced: Nike+Jordan -13.2% (n=461) to -2.3% (n=567); rivals -11.1% to +2.0%; Dunk Low -12.7% to +3.8%; AF1 -4.2% to +7.3%; AJ1 High -15.4% to -14.7%; AJ4 -14.0% to -4.7%. Not sensitive to search rank (Nike+Jordan Q3 2026: ranks 1 to 50 -4.5%, 51 to 100 -0.6%, 101 to 150 +2.6%; ranks 151 to 200 from the new pull +9.8%). **Holds**, with the FX correction above. Verdict NEUTRAL, moderate, stands; in USD terms it leans slightly SHORT because rivals improved more.
- **Test B (trade days by brand).** Reproduced: Nike+Jordan 54,055 to 52,757 (-2.4%), rivals 23,383 to 18,082 (-22.7%), share 69.8% to 74.5%. Robust to the cap, to fixed cohorts and to deeper ranks. **Holds as a relative finding (LONG, moderate)**, but the absolute picture is a shrinking resale market for Nike too (-18% to -22% on fixed cohorts). Resale volume is still not retail demand.
- **Test C (launch premium DiD).** Reproduced: +22.8 points, CI (+5.7, +30.4). It does not survive simple checks:
  - Men's sizes only (drop names with GS, women's, WMNS, TD, PS, kids): Nike+Jordan 2026H1 median **-7.7%** (n=29) vs -12.7% in 2025 (n=58), rivals 0.0% vs +4.3%; DiD **+9.3 points, CI (-2.6, +22.7)**. The headline +2.5% for 2026H1 depends on kids' and women's releases (18 of 47 Nike+Jordan 2026H1 releases vs 13 of 71 in 2025).
  - Releases with at least 5 trade days in months 1 to 3: DiD +16.1, CI (-1.5, +31.1).
  - 2026H1 vs 2025H2 only: +16.4, CI (-0.9, +31.0).
  - Placebo on earlier cohorts: 2024 vs 2023 gives -12.4 points with a CI that excludes zero, so half-year cohort DiDs of plus or minus 12 points occur without any regime change.
  - Rivals excluding adidas: +21.1 (it is not only adidas fading).
  - Verdict: **downgrade from LONG moderate to LONG weak.** New Nike+Jordan men's launches still resell below retail in 2026H1; they are less bad than in 2025, and the remaining edge over rivals is not statistically clear.
- **Test D (Laced).** Reproduced: 724 pairs, Nike 21.5% and Jordan 55.5% (77% together) vs 52% of listed products. Ex the top 10 products the Nike+Jordan share is still 75%. Single snapshot, so it supports the level, not a trend.
- **Running and SneakerPing.** Numbers match the sources. Verdicts (INCONCLUSIVE weak; NEUTRAL moderate) stand.

### Net

What holds: the data are faithfully pulled and cleaned, and the tests reproduce exactly. Nike and Jordan are losing resale activity much more slowly than rivals, and this survives deeper ranks, fixed cohorts and the cap check. Dunk and AF1 resale prices stopped falling in yen terms; AJ1 High has not. What does not hold: "the resale price decline has stopped" is largely a weak-yen effect (about 8 points, not 6; in USD Nike+Jordan is still about -9.5% YoY), the -2.4% Nike volume figure hides a -18% to -22% decline on fixed cohorts, and the launch-premium LONG signal mostly comes from kids' and women's sizes and fails significance on men's sizes. Overall the resale folder supports a weak to moderate LONG on relative brand position versus rivals, not on absolute recovery.
