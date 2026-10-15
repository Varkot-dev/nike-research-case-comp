# N6: Off-price and value channel census (Nike vs adidas, New Balance, Hoka, On, ASICS)

Prepared 2026-10-15. Question: is Nike product leaking into off-price and value channels more or less in 2026 than in 2024 and 2025 (SHORT if rising, i.e. the "marketplace cleanup" is not working; LONG if falling)? Tags: OPENED = fetched and read this session; SNIPPET = search-result summary only; DERIVED = my arithmetic from files in `data/hunt/offprice_census/`. Scripts and raw index files are in that folder (3.0 MB of Common Crawl index lines; sitemaps themselves are not stored, only the script and the counts).

## 1. Verdict

**No evidence that Nike's off-price and value-channel presence is falling in 2026. Where measurable it is flat (Nordstrom Rack, DSW) or higher than 2023 to 2024 (Famous Footwear, 6pm). Smoking gun: NO. Strength: weak to moderate (the Common Crawl series is a sample, 15 usable host-windows, and TJX, Marshalls, Ross, Burlington and Saks Off 5th could not be measured).** This does not contradict Nike's statement of a more than 50% cut in off-price volume on Nike Digital, because that statement concerns Nike's own sales channel and these retailers also buy Nike at full wholesale; the filings and the crawls cannot separate Nike-direct closeouts from regular wholesale or third-party diversion (see section 6).

## 2. Stated in advance

- SHORT-leaning if Nike's share of product pages at off-price and value retailers is higher in Aug to Oct 2026 than in Aug to Oct 2024/2025 and not falling relative to adidas.
- LONG-leaning if it falls by more than sampling noise at several retailers.
- Not met in either direction at 95% confidence except two cells (below).

## 3. Today's snapshot from retailer sitemaps (OPENED, 2026-10-15; `sitemap_snapshot_20261015.csv`)

Brand identified from the product URL slug prefix. Unique products (DSW de-duplicated by product id, colour variants excluded). "Footwear" = slug contains shoe/sneaker/boot/cleat/slide/runner etc. (a text filter, imperfect).

| Retailer | Unique product pages | Nike (n, share all / share footwear-slug) | Jordan | adidas | New Balance | Hoka | On | ASICS |
|---|---|---|---|---|---|---|---|---|
| Nordstrom Rack (12 product sitemaps) | 119,327 | 844, 0.71% / 2.18% | 88 | 1,195, 1.00% / 4.03% | 327, 0.27% / 1.70% | 0 | 10 | 11 |
| DSW (cs_product0 to 2) | 25,124 | 450, 1.79% / 2.18% | 0 (Jordan not in slug) | 908, 3.61% / 4.02% | 132 | 0 | 0 | 37 |
| Academy Sports (product sitemaps 1 to 5; full-price, shown as a comparator) | 136,814 | 12,220, 8.93% / 8.12% | 894 | 3,198, 2.34% / 7.89% | 145 | 0 | 0 | 117 |
| Shoe Carnival (live brand pages, nbHits in page JSON, `shoecarnival_live_counts_20261015.csv`) | n/a | 936 | 156 | 728 | 197 | no brand page (302) | no brand page (302) | 51 |

DERIVED: Nike footwear-slug share is 2.18% at both Rack and DSW against adidas 4.03% and 4.02%, so adidas has about 1.85 times Nike's footprint on off-price shelves while the two are roughly equal on the Nike-owned sales base. Hoka is 0 of 119,327 products at Rack and 0 of 25,124 at DSW, and On is 10 of 119,327 (all apparel/accessory slugs "on-running-..."): the two share gainers keep off-price shelves almost clean, Nike does not. At Shoe Carnival, Nike pages 936 vs adidas 728 vs New Balance 197 vs ASICS 51.

Burlington's sitemap (455 KB, OPENED) lists 2,623 store pages and no product pages; Burlington has no brand pages (`/vendors/nike` returns 404). Ross has no e-commerce. TJ Maxx and Marshalls sitemaps and robots.txt return 403 (bot protection, not bypassed).

## 4. Time series from Common Crawl (OPENED index, `cc_brand_share_aug_oct_by_year.csv`, `cc_brand_share_by_crawl.csv`)

Method: for each retailer, the Common Crawl CDX index lists captured product URLs per crawl (e.g. `nordstromrack.com/s/*`, `dsw.com/product/*`, `famousfootwear.com/product/*`, `6pm.com/p/*`, `academy.com/p/*`); brand from the slug prefix; unique (slug, product id) counted once; Aug to Oct crawls (weeks 33 to 44) pooled per year so the same season is compared. Share = brand's share of captured product pages. This measures assortment presence in the crawl, not units sold.

| Retailer | Nike share Aug-Oct 2023 / 2024 / 2025 / 2026 (n unique products) | Nike over adidas ratio | Reading |
|---|---|---|---|
| Nordstrom Rack | 1.52% (591) / 0.89% (2,590) / no usable crawl / 0.66% (8,238) | 1.13 / 1.05 / n.a. / 0.92 | Falling slightly, but 2024 to 2026 difference -0.23 pts has z about -1.1 (not significant); adidas fell in step (1.35 / 0.85 / 0.72%) |
| DSW | n.a. / 1.46% (683) / 0.00% (955, bad crawl: 96 adidas, 0 Nike, treated as unusable) / 1.45% (2,203) | 0.59 / n.a. / 0.78 | Flat |
| Famous Footwear | 2.23% (3,729) / 1.56% (385, thin) / 3.19% (2,508) / 2.94% (4,054) | 0.51 / 0.75 / 0.95 / 0.94 | Up vs 2023: +0.71 pts, z about 2.0 (borderline); flat 2025 to 2026 (-0.25 pts, not significant); adidas 4.40 to 3.13% so Nike gained relative to adidas |
| 6pm (Amazon-owned off-price site) | n.a. / 0.11% (3,678) / n.a. / 1.20% (8,985) | 0.13 / n.a. / 0.69 | Up, z far above 3, but 2024 captures are 301 redirect pages and a different slice of the site; treat the size as unreliable, the sign as probable |
| Academy (full-price comparator) | n.a. / 0.0% (430, thin) / 28.3% (1,475) / 16.3% (1,097) | n.a. / 2.5 / 4.2 | Crawl dominated by Nike apparel pages in some crawls; not interpretable as a trend |
| Saks Off 5th | one crawl set in 2026: 72 products, 0 Nike or adidas | | too thin |
| TJ Maxx / Marshalls | product URLs carry product names without brand ("Gel-Moisturizer"); one Marshalls crawl captured | | brand cannot be read from URL |

Hoka and On: Hoka appears in 6pm captures at 0.33% (2024) falling to 0.07% (2026) and at 0.05% of Rack in 2026; On is 0 in every crawl at every retailer; ASICS 0.04 to 0.35% everywhere. (DERIVED from the same file.)

Reading: against a null of "cleanup cut Nike product at off-price", Nike's share is not lower in 2026 than in 2024 at DSW (1.46 to 1.45%), is lower but not significantly at Rack (z about -1.1), and is higher at Famous Footwear and 6pm. Equivalent adidas shares moved down at Rack, Famous Footwear and DSW, so Nike's relative standing is flat to up. I cannot show a decline.

## 5. Earnings calls and press (route 3)

- TJX Q2 FY27 call, Aug 19 2026 (OPENED, webull transcript and earningswhispers.com transcript): Herrman: "Product availability continues to be off the charts across all categories and from a wide range of brands." "there continues to be more availability in the marketplace than we could ever buy." No mention of Nike, athletic or footwear anywhere in the transcript body. Opinion, labelled as such; it says supply is abundant but not whose.
- TJX Q4 FY26 call, early Mar 2026 (SNIPPET via Retail Brew, 2026-03-10): "We are going after brands in a more aggressive manner than we also have ever had before"; an off-price consultant says brand restrictions are loosening. Third-party opinion.
- Ross Q2 2026 call (Aug 20 2026) and Burlington Q2 call (Aug 27 2026): pages opened had no brand-level or Nike text (bullfincher and marketbeat pages returned navigation only); Burlington summary (SNIPPET) cites $55M tariff refunds to be reinvested in price and 11% sales growth. No Nike statement found.
- Shoe Carnival Q2 FY2026 (Sep 10 2026, marketbeat highlights, OPENED): no Nike text on the page. SNIPPET from the search: net sales -7.2% to $284.3M, comp -7.1%, guidance cut, interim CEO. Designer Brands Q1/Q2 2026: transcripts behind login or truncated; no Nike statement obtained. Genesco: nothing on Nike.

Net: no earnings call found that mentions Nike by name for off-price supply, so the calls neither confirm nor contradict the cleanup. They do establish that off-price buyers report ample supply of branded goods overall in 2026, which is consistent with, but does not prove, product leaking in.

## 6. Alternatives ruled out and what the data cannot separate

| Alternative explanation of a share change | Test | Result |
|---|---|---|
| Site redesign changed URL patterns | Each host's slug pattern was checked in 2023, 2025 and 2026 captures (brand-first slug unchanged); pattern match counts non-zero in every kept crawl | Ruled out for Rack, DSW, Famous Footwear, 6pm; not testable for Academy |
| Crawl depth changed (total pages per crawl) | Totals range 64 to 8,985 per host-crawl; crawls under 400 products dropped from interpretation; pooled Aug to Oct only | Not ruled out: Rack 2026 total (8,238) is 3 times 2024 (2,590); shares, not counts, are used |
| Brand naming (Jordan, Converse, "NIKE x") | Jordan and Converse reported separately; 6pm and Rack have Jordan under "jordan-" and "air-jordan-" slugs | Ruled out for Nike core; DSW Jordan is not in slugs |
| Hoka and On absent because slugs are different | Rack sitemap searched for "on-running" (10) and "hoka" (0); DSW brands sitemap not used | On/Hoka genuinely near zero on these shelves; brand slug could still be e.g. "on-cloud" (checked: none) |
| Nike Digital cleanup vs Nike full wholesale | Famous Footwear, DSW, Academy, Shoe Carnival are authorised Nike wholesale accounts; Rack and 6pm are mixed | Cannot separate. What would decide: price per product (markdown depth) and quantity by vendor from retailer data, or a TJX/Marshalls item count for Nike-labelled closeouts. TJX/Marshalls are the channel most likely to show diverted product and are blocked |

Related existing work reused, not redone: the nike.com sale assortment is 31.6% of colourways at a discount (`data/hunt/pricing_catalog/live_nikecom_wall_summary_20261014.csv`, row "w"); off-price site blocking and the Foot Locker / Zappos / Shopify panels are in `research_notes/Long or short cruxes/discount_vs_rivals.md`.

## 7. Route log

| # | Route | Result |
|---|---|---|
| 1 | Common Crawl CDX index, prefix queries per retailer, 2023-06 to 2026-39 | PARTIAL. Server resets connections under load; 57 host-crawl index files obtained (Rack 10, Famous Footwear 10, DSW 7, 6pm 6, Academy 3, Saks 13, Marshalls 1); target was 36 crawls per host. Rack 2025, DSW 2025 (one crawl is a bad sample), Academy 2024 and TJ Maxx not obtained |
| 2 | Retailer sitemaps | WORKED for Nordstrom Rack (12 product sitemaps), DSW, Academy, Shoe Carnival (category/brand pages only); BLOCKED 403 for Famous Footwear, TJ Maxx, Marshalls; Burlington has no product pages; Ross sitemap 301; 6pm sitemap 404; Saks Off 5th robots 302. No historical sitemaps (Wayback unreachable from this container) |
| 3 | Earnings calls | PARTIAL: TJX Q2 FY27 transcript read; others summaries or empty; no Nike statements |
| 4 | Nike factory / sale assortment reuse | Reused existing CSV |
| 5 | Retailer search/brand-page counts today | WORKED only for Shoe Carnival (nbHits in page JSON); Rack brand page is a JavaScript bot challenge, DSW and Academy brand pages render client-side or redirect, 6pm redirects |
| 6 | Nordstrom Rack / TJX / Marshalls product names for brand | Ruled out for TJX/Marshalls (slug has no brand) |

Not done because blocked: Wayback historical sitemaps (connection error), Famous Footwear sitemap (403), TJX and Marshalls (403). Data that would settle the open question: a vendor-level unit or dollar count for Nike at TJX/Marshalls/Ross (not public), or repeated monthly sitemap snapshots of Rack/DSW (this note provides the first, 2026-10-15; re-run `sitemap_snapshot.py` monthly to build the series).

## 8. Files

`data/hunt/offprice_census/`: `sitemap_snapshot_20261015.csv`, `shoecarnival_live_counts_20261015.csv`, `cc_brand_share_by_crawl.csv`, `cc_brand_share_aug_oct_by_year.csv`, `raw_cc_index/` (57 gz index files), scripts `harvest.py`, `cc_census.py`, `cc_yearly.py`, `sitemap_snapshot.py`.
