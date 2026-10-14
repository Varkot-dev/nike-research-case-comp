# Crux: Is Nike's discounting getting better or worse right now?

Prepared 2026-10-14. Labels: OPENED = fetched and read in this session. OPENED (repo) = fetched by an earlier researcher and stored in this repo with archive URL, not re-fetched. SNIPPET = search-result summary only. [my arithmetic] = computed by me.

## 0. Pre-registered decision rules (written 2026-10-14 before any new data was gathered)

Primary measures: (a) share of Nike items on sale, (b) average depth of discount on sale items, measured at the same calendar point YoY (to cancel seasonality), on nike.com and at third-party retailers, with adidas and Hoka as controls.

Points LONG (discounting normalising, margin recovery coming):
- L1. nike.com sale-wall item count and sale share of catalog in Aug to Oct 2026 are BELOW the same months of 2025 and trending toward the 2021 level (sale share about 23% to 30%).
- L2. Average discount depth on nike.com sale items in 2026 is flat or shallower than 2025.
- L3. At third-party retailers (Foot Locker, Dick's, Zappos, Running Warehouse) Nike's share of items on sale falls YoY, and falls relative to adidas and Hoka (so it is Nike-specific, not market-wide).
- L4. Nike's own Q1 FY27 commentary and gross margin bridge show discounts as a shrinking headwind, consistent with the web data.

Points SHORT (discounting flat or rising):
- S1. nike.com sale count and share of catalog in Aug to Oct 2026 are AT or ABOVE the same months of 2025.
- S2. Depth of discount is deeper in 2026 than 2025 (more 30%+ off, extra-% promo codes).
- S3. Nike's share of retailer sale assortment rises YoY or stays well above its share of the total assortment, and above adidas and Hoka.
- S4. Nike's own commentary names higher discounts or liquidation as a continuing margin headwind in FY27.

Neutral: web measures move in opposite directions, or Nike moves in line with controls (market-wide promotion, not Nike-specific).

## 1. Verdict

**Points SHORT (strength: strong, not decisive).** Right now (May to Oct 2026), discounting at Nike is getting **wider, not narrower**. It bottomed in mid-to-late 2025 and has risen again through 2026, on nike.com and at a running specialist where the controls (Hoka, adidas, Brooks, ASICS) did not rise. Nike's own Q1 FY27 call (Oct 1, 2026) confirms "increased discounts" in Jun to Aug 2026. Depth of discount is flat (about 25% to 30% off on discounted items), so the change is breadth (more items on sale), not deeper cuts.

Pre-registered scorecard:
- L1 (nike.com sale share below 2025, falling): **FAILED.** Sep 2026 28.4% vs Sep 2025 18.3%; Oct 2026 26.6% to 27.7% vs Oct 2025 22.0%; sale-wall item count up 52% to 101% YoY in Jun to Oct.
- L2 (depth flat or shallower): **HELD.** Depth is flat.
- L3 (retailer Nike sale share falling vs controls): **FAILED** at Running Warehouse; Foot Locker ambiguous.
- L4 (Nike says discounts shrinking): **FAILED.**
- S1 **HELD**, S2 **NOT MET** (depth not deeper), S3 **HELD** at Running Warehouse (ambiguous at Foot Locker), S4 **HELD**.

Important nuance for the pitch (do not overstate): the **level** is not extreme. nike.com sale share of about 27% today is below the 2024 level (29% to 36% in Jul to Oct 2024), far below the 2022 glut (32% to 42%), and inside the pre-2023 range (2021: 23% to 30%; Aug 2019: about 37%). The SHORT reading rests on **direction** (re-widening after the 2025 clean-up was supposed to be done) plus Nike's own words, not on discounting being at a record.

Why "strong" and not "decisive":
1. nike.com counts measure breadth of the sale assortment, not units sold at a discount or realized price.
2. adidas.com (control) also shows high and partly rising discount incidence in the same crawls, so part of the 2026 move may be market-wide. The Nike-specific evidence is Running Warehouse (Nike up, Hoka and adidas down) and Nike's own statements.
3. Wayback Machine was unreachable from this session all day (connection reset on every request), so 2025 comparison points come from the repo's earlier Wayback pulls (OPENED (repo)) and from Common Crawl captures fetched today (OPENED).

## 2. New primary data gathered in this session

### T1. Live nike.com, full catalog and full sale wall (Nike product-wall API, fetched 2026-10-14, OPENED)

Method: paged `api.nike.com/discover/product_wall/v1/...` (the API nike.com's own wall pages call), 100 groupings a page. Catalog capped at anchor 10,000, so pulled sorted by price ascending and by price descending and de-duplicated: 17,661 of 18,347 groupings covered (96%), 33,630 colourways. Sale wall: all 5,079 groupings, 11,686 colourways. Raw: `data/definitive/discount_trend/live_nikecom_catalog_20261014.csv.gz`, `live_nikecom_sale_wall_20261014.csv.gz`. Script: `scripts/definitive/discount_trend/wall.py`.

| Measure (Oct 14, 2026) | Value |
|---|---|
| Sale wall groupings / all groupings (nike.com/w/sale-3yaep vs nike.com/w, embedded totalResources) | 5,079 / 18,347 = **27.7%** |
| Colourways discounted, whole catalog | **31.4%** |
| Footwear colourways discounted | **43.1%** (6,336 colourways), depth 29.1% |
| Apparel colourways discounted | 28.4% (25,141), depth 26.0% |
| Equipment colourways discounted | 31.9% (2,134), depth 20.6% |
| Mean discount on discounted colourways | 26.5% (median 25%) |
| List-price-weighted discount on discounted colourways (sale wall) | 28.9% |
| List-price-weighted discount across the whole catalog | 8.5% |
| Depth bands of discounted sale-wall colourways | 1 to 19%: 27.6%; 20 to 29%: 36.2%; 30 to 39%: 26.4%; 40 to 49%: 9.7%; 50%+: 0.1% |
| Sale-wall colourways showing 0% (mostly "See Price in Bag" promotion flags) | 1,135 of 11,686 (9.7%) |
| Men's shoes on sale (men's sale shoes wall / men's shoes wall) | 342 / 754 = **45.4%** |
| Sitewide promo code banner on sale wall | none found |

Cross-check: the repo's Oct 13 footwear-only count (3,762 colourways, 43.8% discounted, `data/discount/nikecom_discount_by_franchise_20261013.csv`, OPENED (repo)) matches today's 43.1% footwear figure.

### T2. nike.com sale share of catalog, same month across years (the core time series)

Sources: WB = repo Wayback pulls (`data/altdata/wayback_nike_us_sale_vs_total_catalog.csv`, archive URLs in file, OPENED (repo)). CC = Common Crawl captures fetched today by WARC byte range from data.commoncrawl.org (OPENED; every capture's WARC file and offset is in `data/definitive/discount_trend/cc_nikecom_wall_sources.csv`, parsed counts in `cc_nikecom_wall_counts.csv`; count read from the page's `wall-header__item_count` or `totalResources`). LIVE = T1. Share = sale count / catalog count [my arithmetic]; where the two pages were captured on different days, both dates are shown.

| Month | 2024 | 2025 | 2026 | 2026 vs 2025 |
|---|---|---|---|---|
| May | 3,849 / 13,673 = 28.2% (CC May 23 / May 18) | 2,112 / 10,854 = 19.5% (CC May 21 / May 17) | 3,887 / 14,056 = 27.7% (WB May 24 / May 1) | +8.2 pts |
| Jun | 3,524 sale (WB Jun 1); catalog 11,209 (CC Jun 13) = 31.4% | 2,163 / 10,899 = 19.8% (WB Jun 17 / Jun 3) | 3,425 sale (WB Jun 9); no catalog capture | sale count +58% |
| Jul | 4,207 / 11,778 = 35.7% (WB Jul 1) | 2,876 / 12,265 = 23.4% (WB Jul 13 / CC Jul 10) | 4,129 / 14,525 to 15,073 = 27.4% to 28.4% (WB Jul 11 / CC Jul 10 and 12) | +4 to +5 pts |
| Aug | 3,769 / 12,062 to 12,115 = 31.1% to 31.2% (CC Aug 8 / Aug 3 and 5); WB Aug 1: 32.4% | 3,290 / 13,198 = 24.9% (WB Aug 6 / CC Aug 3) | 4,168 / 16,835 = 24.8% (CC Aug 11 / Aug 7); WB Aug 20: 5,131 sale = 30.5% | flat (CC) to +5.6 pts (WB) |
| Sep | 3,740 / 12,971 = 28.8% (WB Sep 1 / CC Sep 12) | **2,368 / 12,959 = 18.3%** (sale count identical in CC and WB on Sep 9; catalog CC Sep 7) | **4,764 / 16,801 = 28.4%** (CC Sep 9 / Sep 4); WB Sep 2: 4,889 | **+10.1 pts; count +101%** |
| Oct | 4,100 / 13,835 to 13,931 = 29.4% to 29.6% (WB Oct 1 / CC Oct 5, WB Oct 1) | 3,175 / 14,436 = 22.0% (WB Oct 1); CC catalog Oct 9 and 14: 14,265 to 14,554 | 4,831 / 18,170 = 26.6% (WB Oct 1 / Oct 3); **LIVE Oct 14: 5,079 / 18,347 = 27.7%** | **+4.6 to +5.7 pts; count +52% to +60%** |
| Nov | 3,921 sale (CC Nov 2) | 2,981 / 14,200 = 21.0% (WB Nov 7 / CC Nov 8) | n/a | |
| Dec | 4,557 / 11,471 = 39.7% (CC Dec 1 / Dec 9) | 3,588 / 14,195 = 25.3% (WB Dec 8 / CC Dec 5) | n/a | |
| Mar | n/a | 2,982 / 10,593 = 28.2% (CC Mar 25 / Mar 18) | 3,142 / 11,864 to 12,049 = 26.1% to 26.5% (CC Mar 13 / Mar 5 and 7) | -2 pts |

Pre-2023 benchmarks (WB, OPENED (repo)): Jul 2021 27.6%, Aug 2021 30.1%, Sep 2021 23.3%, Oct 2021 24.1%; Aug 2022 (count only) 3,857, Sep 2022 31.8%, Oct 2022 41.6%; Aug 2019 2,253 sale vs about 5,738 to 6,108 catalog = about 37% to 39%.

Reading [my arithmetic and opinion]: the series troughed in May to Nov 2025 (18% to 25%), the period right after Nike cut North America digital promotional days "from over 30 to zero" (Jan to Feb 2025, repo investigations/04). From March 2026 it climbed back to 26% to 28% and has stayed there; every same-month comparison from May to Oct 2026 is above 2025 except the CC August reading (flat). It is still below 2024 for Jul, Aug and Oct.

### T3. Men's shoes on nike.com (repo quarterly table, OPENED (repo), plus LIVE)

Men's sale shoes / men's shoes: 2022 to 2023: 26% to 39%; 2024Q1 to 2025Q1: 43% to 53%; Aug 2025: 37.9%; Nov 2025: 42.7%; Feb 2026: 44.0%; May 2026: 43.3%; Oct 2026: 44.0%; **live Oct 14: 45.4%** (`data/marketplace/nike_sale_share_quarterly.csv`). Footwear follows the same shape: trough in Aug 2025, up about 7 pts since, below the 2024 peak.

### T4. Common Crawl PDP panel: random nike.com and adidas.com product pages (OPENED, fetched 2026-10-14)

Method: for each crawl, list every captured nike.com/t/* and adidas.com/us/*/{code}.html page (status 200), draw 150 at random (seed 42), read current and list price from the page (Nike: currentPrice and initialPrice containers; adidas: schema.org Offer and standard_price / sale_price, verified by hand on 6 pages). Raw: `data/definitive/discount_trend/cc_pdp_panel_nike_adidas.csv`. Script: `scripts/definitive/discount_trend/pdp_panel.py`. 95% interval on share about plus or minus 7 to 8 pts.

| Crawl | Nike n | Nike share discounted | Nike depth (discounted) | adidas n | adidas share discounted | adidas depth |
|---|---|---|---|---|---|---|
| Aug 2024 (2024-33) | 148 | 27.7% | 25.2% | n/a | 2024 adidas captures have no price data | |
| Sep 2024 (2024-38) | 149 | 18.8% | 26.7% | n/a | | |
| Oct 2024 (2024-42) | 114 | 19.3% | 28.3% | n/a | | |
| Aug 2025 (2025-33) | 149 | 28.2% | 18.6% | 150 | 51.3% | 36.7% |
| Sep 2025 (2025-38) | 149 | 38.9% | 24.4% | 150 | 60.0% | 37.3% |
| Oct 2025 (2025-43) | 150 | 37.3% | 28.6% | 150 | 63.3% | 35.7% |
| Aug 2026 (2026-34) | 148 | 35.8% | 23.3% | 150 | 72.0% | 29.5% |
| Sep 2026 (2026-39) | 150 | 36.7% | 25.2% | 150 | 64.0% | 29.9% |

Reading: this panel is weaker than T2 because the crawler chooses which pages to revisit (old, aged pages are more likely to be marked down). It says Nike PDP discount incidence stepped up from about 19% in Sep to Oct 2024 to about 37% to 39% from Sep 2025 and has **not fallen** since (Sep 2026 36.7% vs Sep 2025 38.9%, inside the error band). Depth is flat at 23% to 29%. adidas.com discounts far more items (51% to 72%) but at a shallower and falling depth; adidas incidence also rose Aug 2025 to Aug 2026. So on this measure, the 2026 Nike level is "not improving", and part of the environment is market-wide.

### T5. Retailer controls

**Running Warehouse, men's road running** (repo `data/marketplace/runningwarehouse_history.csv`, Wayback and live, OPENED (repo)). Share of colourways on sale:

| Date | Nike | Hoka | adidas | Brooks | ASICS |
|---|---|---|---|---|---|
| 2025-02-05 | 61.5% | 25.9% | 34.2% | 43.6% | 14.9% |
| 2025-09-11 | 25.4% | 21.1% | 22.7% | 11.7% | 8.8% |
| 2025-10-16 | 33.3% | 12.8% | 25.0% | 23.2% | 5.7% |
| 2026-04-26 | 35.7% | 15.9% | 10.6% | 32.2% | 11.5% |
| 2026-10-13 | **49.0%** | **9.5%** | 22.1% | 32.9% | 19.0% |

Oct 2026 vs Oct 2025: Nike +15.7 pts; Hoka -3.3; adidas -2.9; Brooks +9.7; ASICS +13.3 [my arithmetic]. Nike rose most. Current models are on sale, not just run-outs: on Oct 13, 2026, 6 of 15 Pegasus 42 colourways and 9 of 14 Vomero 18 colourways were discounted (`runningwarehouse_items.csv`, OPENED (repo)). This matters because Running is the category Nike says is growing double digits (Q1 FY27 call).

**Foot Locker** (repo `footlocker_sale_brand_history.csv`, `footlocker_brand_sale_mix.csv`, OPENED (repo)): Nike Inc. (Nike plus Jordan plus Converse) share of the sale-shoes wall 38.6% (Jan 2025), 40.7% (Jun 2025), 49.9% (Oct 13, 2026). But Nike Inc.'s share of the total shoe assortment also rose (42.0% of all shoes on Oct 13, 2026), and the site's whole sale wall shrank from 4,000 to 7,000 items in 2024 to 2,648 after the DICK'S takeover. Over-index (share of sale / share of assortment) about 1.19 on Oct 13, 2026. **Not usable as a trend**: the base changed. Neutral.

**Zappos** (live, fetched 2026-10-14, OPENED): sneakers and athletic shoes, styles on sale / all styles by brand facet: Nike 179 / 289 = 62%; adidas 301 / 508 = 59%; HOKA 30 / 78 = 38%; New Balance 213 / 431 = 49%; ASICS 107 / 159 = 67%; PUMA 188 / 243 = 77%; Brooks 20 / 60 = 33%; Saucony 48 / 121 = 40%. Level only (Zappos discounts nearly everything); no history because Wayback was unreachable and Common Crawl has no Zappos captures for these pages. Neutral, except that Nike is above Hoka and Brooks.

**Live adidas.com and hoka.com**: adidas.com timed out (bot protection) and hoka.com returned HTTP 406 from this session; Common Crawl has no hoka.com/en/us/ sale captures. Hoka control therefore comes only from Running Warehouse and Foot Locker.

### T6. Nike's own words (the company's measure of realized price)

- Q1 FY27 call, Oct 1, 2026 (official transcript PDF, s1.q4cdn.com/806093406/files/doc_financials/2027/q1/NIKE-Inc-Q1FY27-OFFICIAL-Transcript_-FINAL.pdf, OPENED): "Gross margin was 42.8%, up 60 basis points ... benefits from our supply chain cost management efforts and FX tailwinds, partially offset by **increased discounts** as well as channel mix."
- Same call, CFO Dave Denton (OPENED): "we are taking discounts and resetting the marketplace, which is dampening gross margins over time"; FY27 EBIT to fall faster than revenue, "continued pressure on gross margin".
- Same call (OPENED): "some aged, higher volume, sportswear footwear sold through below expectations ... that has impacted our future order books as we proactively work with our wholesale partners to work through excess inventory."
- Q1 FY27 10-Q p. 20 (repo, OPENED (repo)): Sportswear and Jordan actions now "extend beyond fiscal 2027", reflecting "higher levels of discounting and broader marketplace pressure"; p. 23 ASP margin line -30 bps "primarily due to higher discounts and channel mix, partially offset by strategic pricing."
- Sales-related reserve as a share of quarterly wholesale revenue: 14% to 18% (FY23 to FY24), peak 27.9% (May 2025), 21.4% (Aug 2026) (repo note 15, OPENED (repo)). Still above normal, falling slowly.
- Needham (Tom Nikic), Sep 24, 2026: lowered estimates citing weak demand, high inventory and "intense promotional activity" (optionfinance.fr, SNIPPET; page returned 403).

## 3. Alternative explanations for "nike.com sale share rose in 2026", and tests

| # | Alternative | Test | Result |
|---|---|---|---|
| A1 | Catalog got bigger, so more items on sale is mechanical | Use share, not count | **Ruled out.** Catalog +26% (Oct 14,436 to 18,347); sale +52% to +60%; share up 4.6 to 5.7 pts in Oct and 10.1 pts in Sep |
| A2 | Seasonality or event timing (Labor Day, back-to-school) | Same calendar day YoY | **Ruled out for Sep** (Sep 9 vs Sep 9: 2,368 vs 4,764) and Oct (Oct 1 vs Oct 1: 3,175 vs 4,831). Aug is ambiguous (flat on CC Aug 11, up on WB Aug 20) |
| A3 | "Sale" wall now includes items that are not marked down (member pricing, "See Price in Bag") | Count 0%-discount items on today's wall | **Mostly ruled out.** 9.7% of sale-wall colourways show 0%; removing them still leaves about 25% share today vs 22% (Oct 2025, which also included such items). The 2025 composition could not be checked (Wayback unreachable), so a small part remains open |
| A4 | Depth got shallower, so wider sale means little margin cost | Depth series | **Partly true.** Depth flat at 25% to 30% (T1, T4, repo first-page depth 26% to 34%). Breadth is up, depth is not deeper: the margin cost rises with breadth |
| A5 | List-price increases (tariff pricing from Fall 2025) then marked back down: realized price unchanged | Nike's ASP and margin lines | **Ruled out as full explanation.** Nike itself says discounts increased in Q1 FY27 and NA footwear ASP fell on more pairs (Q1 FY27 10-Q pp. 23, 26). Cannot separate the exact size |
| A6 | World Cup apparel clearance (temporary) | Footwear alone | **Partly ruled out.** Footwear is 43% discounted; men's shoes on sale rose from 37.9% (Aug 2025) to 45.4% (Oct 2026). Some apparel clearance may be in the Aug to Oct number |
| A7 | Market-wide promotion, not a Nike problem | adidas, Hoka, Brooks, ASICS controls | **Not fully ruled out.** Running Warehouse: Nike +15.7 pts YoY vs Hoka -3.3, adidas -2.9 (Nike-specific). adidas.com PDP incidence also rose Aug 2025 to Aug 2026 (51% to 72%), and Brooks and ASICS rose at Running Warehouse. Some of the environment is market-wide; Nike's move is the largest where measured |
| A8 | Nike chose to liquidate on nike.com instead of through off-price and wholesale (channel choice, could be margin-neutral) | Nike statements; reserve | **Open.** Nike says it is working "with our wholesale partners to work through excess inventory", and the reserve is still 21% of wholesale. Liquidation seems to be happening in both channels. Even if channel choice, it contradicts the "full-price platform" plan for Digital |
| A9 | Counting method change on nike.com (grouping of colourways) | Same counter (totalResources / item_count) on both pages; ratio cancels a common change | **Mostly ruled out** for the share; count levels could shift if grouping rules changed |

## 4. What is still unknown, and what would settle it

- Unit-weighted discount penetration (what share of Nike units sell below full price). Only Nike or a POS panel (Circana) has this.
- The 2025 composition of the nike.com sale wall (how many 0% "price in bag" items). Settled by Wayback captures of the Nike API JSON for Sep and Oct 2025 once web.archive.org is reachable.
- Hoka.com and adidas.com sale-wall counts over 2025 to 2026. Settled by Wayback captures (Common Crawl does not hold them).
- **Next decisive data:** (1) nike.com sale share across Black Friday to Cyber Monday 2026 vs 2025 (Nov 27 to Dec 1; 2025 Dec 5 to 8 benchmark 25.3%); (2) Nike's Q2 FY27 gross margin bridge (mid to late December 2026): if the ASP line is still "higher discounts", SHORT is confirmed; if it flips to "lower discounts" in North America, LONG; (3) any full-price-realization target at the Nov 16 to 17 Investor Day; (4) the sales-related reserve ratio in the Q2 FY27 10-Q (below 18% would point LONG).

## 5. Sources (all accessed 2026-10-14 unless marked)

| Source | Date of data | Status |
|---|---|---|
| nike.com product-wall API, catalog and sale walls (api.nike.com/discover/product_wall/v1/marketplace/US/...) | 2026-10-14 | OPENED |
| nike.com/w, /w/sale-3yaep, /w/mens-shoes-nik1zy7ok, /w/mens-sale-shoes-3yaepznik1zy7ok (embedded totalResources) | 2026-10-14 | OPENED |
| Common Crawl index (index.commoncrawl.org) and WARC records (data.commoncrawl.org), crawls CC-MAIN-2024-22 to CC-MAIN-2026-39; record list in `cc_nikecom_wall_sources.csv` | captures May 2024 to Sep 2026 | OPENED |
| Common Crawl PDP panel (nike.com/t/*, adidas.com/us/*.html), 2,400 pages sampled, 1,942 with a readable price (the 450 adidas 2024 pages had no price data) | Aug 2024 to Sep 2026 | OPENED |
| Zappos sneakers-athletic-shoes and on-sale filter pages (brand facets) | 2026-10-14 | OPENED |
| adidas.com/us/sale (timeout), hoka.com/en/us/sale/ (HTTP 406), web.archive.org (connection reset all session) | 2026-10-14 | not reachable |
| Nike Q1 FY27 official transcript PDF (s1.q4cdn.com) | 2026-10-01 | OPENED |
| Nike Q1 FY27 10-Q pp. 20, 23, 26 to 28; FY23 to FY26 10-Ks (reserve) | 2026 | OPENED (repo) |
| Repo Wayback nike.com series `data/altdata/wayback_nike_us_sale_vs_total_catalog.csv`, `data/marketplace/nike_sale_share_quarterly.csv` (archive URLs in files) | 2019 to Oct 2026 | OPENED (repo) |
| Repo Running Warehouse `runningwarehouse_history.csv`, `runningwarehouse_items.csv` | Feb 2025 to Oct 2026 | OPENED (repo) |
| Repo Foot Locker `footlocker_sale_brand_history.csv`, `footlocker_brand_sale_mix.csv`, `footlocker_wayback_brand_facets.csv` | 2022 to Oct 2026 | OPENED (repo) |
| optionfinance.fr, "Nike revient vers des planchers de 12 ans", Needham comments | 2026-09-24 | SNIPPET (403) |
| Repo investigations/04 (promo days 30 to 0, Jan to Feb 2025) and research note 15 (reserve ratios) | 2025 to 2026 | OPENED (repo) |

Scripts: `scripts/definitive/discount_trend/` (wall.py live API pager; cc.py Common Crawl wall fetcher; ccparse.py count and card parser; pdp_panel.py and pdpsum.py PDP panel). All Python run with `python3 -I`.
