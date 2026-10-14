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
