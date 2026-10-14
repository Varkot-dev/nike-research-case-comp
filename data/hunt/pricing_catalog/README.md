# Pricing and catalog hunt (key: pricing_catalog)

Pulled 2026-10-14 (UTC). Purpose: push the "discount trend" crux (Q4), and the category cruxes on lifestyle classics (Q5) and running quality (Q6), from moderate toward strong or weak, using free price data that earlier work in this repo did not have: a long, month-by-month product-page panel (2023 to Sep 2026) split by category, a category-level nike.com wall history, a full live nike.com catalog by category, and a 16-store US retailer catalog panel with product age.

All Python was run with `python3 -I`. No logins, no personal data in any request. Sleeps of 1 to 2 s between live requests. nike.com robots.txt allows /w/ walls with up to four "z" filters; all walls used comply.

## 1. Datasets (tidy files in this folder)

| File | Rows | What it is | Period |
|---|---|---|---|
| `cc_pdp_panel_nike.csv` + `cc_pdp_panel_nike_part2.csv` | 16,971 + 2,772 (about 18,900 parsed "ok") | Random sample of nike.com product pages (www.nike.com/t/*) captured by Common Crawl, one row per page: list price, current price, style code, parse method, release date (2023 to mid-2024 pages only) | 37 crawls, Mar 2023 to Sep 2026 |
| `cc_pdp_panel_adidas.csv` | 3,067 | Same for adidas.com/us product pages (schema `standard_price` / `sale_price`) | Aug 2025 to Sep 2026 (2024 adidas pages carry no price) |
| `pdp_panel_tidy.csv.gz` | about 21,900 | Both panels merged, with category (running, basketball, Jordan, lifestyle classics, lifestyle other, training, soccer, fan gear, other), footwear flag, style prefix, window labels | 2023 to 2026 |
| `pdp_share_by_crawl.csv`, `pdp_nike_monthly.csv`, `pdp_nike_month_yoy.csv`, `pdp_share_by_half.csv`, `pdp_share_by_window.csv`, `pdp_nike_window_by_category.csv`, `pdp_adidas_window_by_category.csv`, `pdp_nike_share_by_half_category.csv` | small | Derived tables (share of pages discounted, mean depth) | |
| `cc_category_walls.csv` | 354 | Every Common Crawl capture (latest per crawl) of 44 target nike.com category and franchise walls (running, basketball, Jordan, lifestyle, AF1, Dunk, Air Max, Jordan 1, Pegasus, and their sale walls): reported item count plus first-page prices | Jan 2023 to Sep 2026 |
| `live_category_walls_20261014.csv` | 44 | Same 44 walls fetched live and parsed with the same parser | 2026-10-14 |
| `live_nikecom_wall_summary_20261014.csv` | 22 | Live nike.com product-wall API pulls, one row per wall: groupings, colourways, share discounted, depth, best-seller discount share, fan-gear share | 2026-10-14 |
| `live_nikecom_union_catalog_20261014.csv.gz` | 32,225 colourways | Union of all live API pulls (de-duplicated by style code) with list price, current price, employee price, badge, featured attributes, isNewUntil | 2026-10-14 |
| `shopify_products_20261014.csv.gz` | 120,518 products | Public `/products.json` catalogs of 16 US sneaker and running retailers (DTLR, Shoe Palace, Sneaker Politics, Social Status, Extra Butter, Kith, Undefeated, Feature, BDGA, APB, Lapstone and Hammer, Notre, Concepts, Pacers Running, Playmakers, Sneakersnstuff): vendor, type, created and published dates, price, compare-at price, availability | 2026-10-14 snapshot, products created 2019 to 2026 |
| `shopify_tidy_brand_products_20261014.csv.gz` | 45,685 | Brand rows only (Nike, Jordan, adidas, New Balance, ASICS, HOKA, On, Puma, Saucony, Salomon, Brooks, Converse, Vans, Reebok) with markdown flags and product age | |
| `shopify_lpm_markdown10_brand_effects.csv`, `shopify_fresh_markdown_by_store_brand.csv`, `shopify_running_markdown_by_brand.csv`, `shopify_pacers_running_markdown_by_brand.csv` | small | Regression and table outputs | |
| `matched_sku_then_vs_now.csv`, `matched_sku_rows.csv.gz` | 5 / about 4,600 | Style codes seen on archived nike.com pages matched to today's live price list (list-price change, current discount status) | 2024 to 2026 |
| `cc_dtlr_pdp_panel.csv` | 2,142 | Common Crawl captures of DTLR product pages (vendor, price, compare-at) | Sep to Oct 2025, Aug to Sep 2026 |

Raw pulls are in `raw/`: live API pages (`raw/api_live_20261014/*.csv.gz`), Shopify JSON (slimmed, `raw/shopify/*.json.gz`), Common Crawl index listings (`raw/cc_index`, `raw/cc_pdp_idx`, `raw/cc_retail_idx`, gzipped), logs and analysis printouts (`raw/*_output.txt`). Every Common Crawl row keeps its WARC file name and byte offset (in the index files or in `cc_category_walls.csv`), so any page can be re-read from data.commoncrawl.org.

## 2. Sources and methods

| Source | URL / endpoint | Method |
|---|---|---|
| nike.com product-wall API (the JSON the site itself calls) | `https://api.nike.com/discover/product_wall/v1/marketplace/US/language/en/consumerChannelId/d9a5bc42-4b9c-4976-858a-f159cf99c647?path=/w/<slug>&attributeIds=<ids>&queryType=PRODUCTS&anchor=N&count=100` | `scripts/api_pull.py`. Walls over 10,000 items pulled sorted by price ascending and descending, then de-duplicated. |
| nike.com wall pages | `https://www.nike.com/w/<slug>` | `scripts/live_target_walls.py`, `scripts/live_walls.py` (reads `totalResources` and card prices) |
| Common Crawl index | `https://index.commoncrawl.org/CC-MAIN-YYYY-WW-index?url=...` | `scripts/cc_list.py` (all /w/ walls per crawl), `scripts/cc_pdp_idx.py` and `cc_pdp_idx_generic.py` (product pages), `scripts/cc_retail_idx.py` (DTLR) |
| Common Crawl WARC records | `https://data.commoncrawl.org/<warc>` with HTTP Range | `scripts/cc_wall_fetch.py`, `scripts/pdp_fetch.py`, `scripts/pdp_fetch_adidas.py`, `scripts/retail_pdp_fetch.py` |
| Shopify storefront catalogs | `https://<store>/products.json?limit=250&page=N` (robots.txt checked: allowed) | `scripts/shopify_pull.py`, 1.5 s between pages, capped at 80 pages (20,000 products) per store |
| Analysis | | `scripts/pdp_analysis.py`, `scripts/shopify_analysis.py`, `scripts/matched_sku.py`, `scripts/live_summary.py`; shared helpers `scripts/classify.py`, `scripts/wallparse.py` |

Sampling: product pages are a random sample (fixed seed) of all status-200 nike.com/t/ captures in each crawl, up to 1,300 per crawl (most crawls hold 300 to 1,300, so the sample is close to the whole pool). adidas: up to 1,500 per crawl from pools of 400 to 700 parseable PDPs.

Price parsing on nike.com product pages: 2024-08 onward pages use `currentPrice-container` / `initialPrice-container`; 2023 to mid-2024 pages use the embedded per-colourway JSON (styleColor, seoProductReleaseDate, fullPrice, currentPrice), matched to the style code in the URL, with the rendered `data-test="product-price"` markup as fallback. An earlier version took the first JSON price on the page; hand checks showed it sometimes read a different colourway, so those rows were dropped and re-fetched.

## 3. Known gaps and caveats

1. **Common Crawl is not a random sample of the catalog.** The crawler decides which pages to (re)visit. A change in crawl policy could move the panel's discount share without any change at Nike. The same-calendar-month comparisons reduce, but do not remove, this risk. The skeptic in `discount_trend.md` already noted that this panel and the sale-wall series disagree on 2024 vs 2025 direction; that remains unresolved.
2. **Small crawls:** Jan and Feb 2026 (CC-MAIN-2026-04, -08) hold only 108 and 160 Nike pages; treat those months as noise.
3. **Breadth, not units.** All measures count listed items or pages, not units sold at a discount.
4. **Wall definitions change.** Several walls changed scope in 2026 (for example womens-jordan-shoes jumped from about 60 to about 300 items in Mar 2026; lifestyle-13jrm doubled). Counts across that break are not comparable; ratios of a sale wall to its own parent wall in the same month are safer.
5. **Running wall now includes NFL product.** Live running-shoes wall: 29 of 213 groupings are "Men's NFL Road Running Shoes"; part of the 2026 running assortment growth is licensed fan product.
6. **API pagination trap (fixed):** the product-wall API ignores `path` after page 1 unless `attributeIds` is passed. A first pull without it returned the generic catalog for every wall; it was deleted and re-pulled. Earlier repo pulls that used `scripts/definitive/discount_trend/wall.py` passed attributes explicitly, so they are not affected.
7. **Shopify compare-at prices.** Some stores never use compare-at (Kith, Concepts, APB, Lapstone and Hammer, Social Status show 0% to 10% markdowns), so only within-store comparisons are meaningful (store fixed effects are used). Several stores keep sold-out archive listings at deep markdowns, so tests use available products only. DTLR, Extra Butter, Kith and Feature hit the 20,000-product cap (newest first), so their oldest listings are missing.
8. **DTLR Common Crawl panel is too thin for a time series** (119 and 223 product captures in the two 2026 crawls, and availability flags in archived pages are unreliable). Kept as raw; not used in tests.
9. **adidas.com live is blocked** (WAF 403), so adidas comes only from Common Crawl product pages and from retailers.
10. **Style-code age:** release dates exist only in 2023 to mid-2024 pages. For 2025 to 2026, "fresh" means the two-letter style prefix first appeared in the panel within the past 12 months; this is approximate.

## 4. Sources tried and blocked or unusable

- web.archive.org (CDX and replay): egress policy 403 or connection reset all session; wayback.archive.org and web-beta.archive.org: reset. archive.org availability API works (gives timestamps only, no content).
- archive.ph: reset; timetravel.mementoweb.org: 502; arquivo.pt CDX: 403; wayback.archive-it.org: rate-limited.
- adidas.com/us and adidas.com/api/plp: 403 (bot protection). Not retried.
- milled.com (brand email archive) and retailmenot.com: Cloudflare challenge 403.
- Slickdeals search RSS: works, but robots.txt disallows `/newsearch.php?*rss=*`, so not used.
- Retailers without a public catalog feed or blocked: Hibbett (410), Finish Line (403), JD Sports (403), Snipes (410), SSENSE (403), END (302 to block), Sport Chek (403), Zappos, Jackrabbit, Holabird, Fleet Feet, Atmos (404), Big Peach Running (403), Running Warehouse (reset), Villa (TLS name mismatch), Rogan's (530), Jimmy Jazz (502), Marathon Sports and Philadelphia Runner (no products returned).
- Shoe Palace has no Common Crawl product captures under shoepalace.com.
- Common Crawl index: frequent connection resets and 504s; every listing was retried until it succeeded or logged "giveup".

## 5. How to re-run

```
python3 -I scripts/api_pull.py raw/api_live_YYYYMMDD /w/running-shoes-37v7jzy7ok ...      # live nike.com walls
python3 -I scripts/live_target_walls.py scripts/target_walls.txt live_category_walls_YYYYMMDD.csv
python3 -I scripts/shopify_pull.py raw/shopify shopify_products_YYYYMMDD.csv www.dtlr.com shoepalace.com ...
python3 -I scripts/cc_list.py raw/cc_index CC-MAIN-2026-39 ...                           # wall captures
python3 -I scripts/cc_wall_fetch.py raw/cc_index scripts/target_walls.txt cc_category_walls.csv
python3 -I scripts/cc_pdp_idx.py raw/cc_pdp_idx CC-MAIN-2026-39 ...                      # product-page captures
python3 -I scripts/pdp_fetch.py raw/cc_pdp_idx 1300 cc_pdp_panel_nike.csv CC-MAIN-2026-39 ...
python3 -I scripts/pdp_analysis.py; python3 -I scripts/shopify_analysis.py; python3 -I scripts/matched_sku.py; python3 -I scripts/live_summary.py
```
Index listings are stored gzipped; gunzip them (or re-list) before re-running the fetchers.

## 6. Test results (pre-registered rules, numbers from the files above)

**T1. Is nike.com discounting falling, same calendar months, 2026 vs 2025?** (Q4)
Rule set in advance: LONG if the share of product pages discounted is at least 3 pts lower YoY with a 95% interval excluding zero, overall and in footwear. SHORT if flat or higher.
Result (`pdp_panel_tidy.csv.gz`, Nike pages): Mar to Sep 2025 30.5% (n 4,292) vs Mar to Sep 2026 31.0% (n 6,257): +0.5 pts, 95% CI -1.3 to +2.3. Footwear 30.4% vs 27.8%: -2.6 pts, CI -5.2 to 0.0. Split: Mar to Jun 2026 was lower (-3.4 pts, CI -5.9 to -0.9; footwear -8.4 pts), Jul to Sep 2026 was higher (+5.0 pts, CI +2.4 to +7.5; footwear +3.8). Depth of discount flat at 22% to 26%. For reference, Aug to Sep 2024 was 22.6% (n 1,053), Aug to Sep 2025 32.3% (n 1,761), Aug to Sep 2026 36.9% (n 2,159).
Reading: no improvement over 12 months, with a fresh rise in Jul to Sep 2026 (the quarter where Nike itself reported "increased discounts"). LONG rule fails. "Discounting has stalled" is now strong; "discounting is accelerating" stays weak (it rests on one quarter).

**T2. Is it Nike-specific? Nike vs adidas.com, Aug to Sep 2025 to Aug to Sep 2026** (Q4, alternative A7)
Rule: SHORT if Nike's rise is larger than adidas's; LONG if Nike improves relative to adidas.
Result: Nike +4.6 pts (32.3% to 36.9%), adidas +12.7 pts (55.5% to 68.3%, depth down from 36.4% to 30.3%). Difference in differences -8.2 pts (bootstrap 95% CI -13.3 to -3.3); footwear -10.5 (CI -20.1 to -1.0). adidas.com widened promotions more than Nike did. Points NEUTRAL: the 2026 widening is at least partly market-wide (or adidas-specific), not a Nike-only problem.

**T3. By category on nike.com: which categories are getting better or worse?** (Q5, Q6)
Rule: for each of running, basketball, Jordan, lifestyle classics, LONG if discount share falls 3+ pts YoY; SHORT if it rises 3+ pts.
Result, Mar to Sep 2025 vs 2026: running 26.5% to 27.5% (n 445 / 786), basketball 38.5% to 31.8%, Jordan 21.2% to 21.6%, lifestyle classics (Dunk, AF1, Air Max, Blazer, Cortez, P-6000 and similar) 39.7% to 39.1%, training 24.9% to 32.5%. Aug to Sep only: running 27.6% to 22.6%, Jordan 18.0% to 24.0%, lifestyle classics 41.1% to 46.6%, basketball 29.2% to 33.6%.
Live Oct 14, 2026 colourway shares discounted (API): running shoes 37.9% (best sellers 32.1%), basketball shoes 51.0%, Jordan shoes 37.6%, lifestyle shoes 44.9%, men's shoes 38.4%, women's shoes 43.0%.
Assortment (wall counts, `cc_category_walls.csv` plus live): Air Force 1 shoes 179 (Feb 2023), 126 (Nov 2024), 60 to 68 (mid to late 2025), 50 to 56 (Apr to May 2026), 70 (Oct 2026). Dunk shoes 69 (Mar 2023), 73 (Nov 2024), 46 (Oct 2025), 31 (Sep to Oct 2026). Jordan 1 shoes 46 to 56 (mid 2025), 118 (May 2026), 133 (Oct 2026). Running shoes 146 (Apr 2026), 187 (Aug 2026), 251 (Oct 2026), part of it NFL-licensed product.
Reading: no category shows a clear improvement over the full Mar to Sep window. Dunk and AF1 assortments have been cut by more than half, which fits "close to a bottom" for those two, but the discount share in lifestyle classics is unchanged at about 40%. Jordan 1 assortment has more than doubled since mid 2025, which cuts against the "Jordan retro cut" story on nike.com (it could be SE and kids colourways). NEUTRAL by the rule, with a mild SHORT tilt for Jordan and lifestyle in Aug to Sep and a mild LONG tilt for running in Aug to Sep.

**T4. At wholesale partners, does Nike need more markdowns than peers on product of the same age?** (Q1, Q4, Q6)
Rule: LONG if Nike's markdown rate (10%+ off, available footwear) is at or below adidas and the peer median after store and age controls; SHORT if Nike is more than 5 pts above adidas.
Result (16 stores, 13,634 available footwear products): linear probability model with store and age-bucket fixed effects, Nike +9.7 pts vs adidas (store-clustered SE 7.9, not significant); Jordan +17.8 (SE 11.3); New Balance +11.7; ASICS +13.0; HOKA +1.5; On -10.1. Products 0 to 3 months old: Nike 18.1% (n 990), Jordan 15.5% (548), adidas 5.0% (464), New Balance 8.7%, On 1.1%, HOKA 13.5%, ASICS 28.4%, Saucony 26.0%. Running shoes only (`shopify_running_markdown_by_brand.csv`): Nike 35.0% (n 954) vs On 9.8%, adidas 11.2%, HOKA 23.0%, New Balance 28.6%, ASICS 29.7%, Brooks 35.7%, Saucony 42.0%; at Pacers Running (specialist) Nike 11.8% vs HOKA 21.8%, ASICS 30.1%, Brooks 36.2%.
Reading: Nike is above adidas, On and HOKA (the share gainers) on fresh product, and sits with ASICS, Brooks and Saucony. The direction is SHORT but the controlled estimate is not statistically significant: SHORT, weak to moderate.

**Descriptive (matched SKUs, `matched_sku_then_vs_now.csv`):** of style codes seen at full price on nike.com in Aug to Sep 2026 and still listed, 39.1% were discounted by Oct 14, 2026. Of codes seen in Aug to Sep 2025 and still listed today (16% survive), 48% now carry a higher list price than in 2025 (running: 61% raised, median +3.6%), so part of the 2026 discounting sits on top of higher list prices.
