# Discount vs rivals hunt (key: discount_vs_rivals)

Pulled 2026-10-14 (UTC). Rescues two failed tests from earlier hunts: (a) the BLS PPI shoe-store retail margin index (series PCU448210448210) is at a 24-year low, but nobody could say whether that is Nike or the whole sector; (b) adidas.com US is blocked (403), so "is Nike's discounting worse than rivals" rested on two crawls. Standing rule (CLAUDE.md): no "inconclusive" without at least five different routes, every route logged below.

Decision rule stated before the work: Nike discount depth rising faster than adidas, Hoka, On, ASICS on the same shelves, with retailer margins at lows during Nike's wholesale surge, points SHORT. Nike improving relative to rivals points LONG.

All Python was run with `python3 -I`. No logins, no accounts, no personal data in any request. 1.5 to 6 s sleeps between live requests. robots.txt was read before each live site (Zappos: directory URLs allowed, `/search?term=` disallowed so not used; Foot Locker: `currentPage=` and `sort=` disallowed so first page only; JD Sports UK: sort and search parameters disallowed). Raw files are under 20 MB each; `raw/sec/*.json.gz` are SEC XBRL company-facts API files.

## Route log (every route, with result)

| # | Route | Result | Notes |
|---|---|---|---|
| 4a | Decompose BLS PPI retail margin indexes (FRED) | WORKED | 10 series; shoe-store margin is footwear-specific. `ppi_decomposition_summary.csv`, `ppi_margin_indexes_monthly.csv` |
| 4b | PPI shoe-store index vs Nike wholesale by fiscal quarter | WORKED (weak test, 9 quarters) | `ppi_by_nike_fiscal_quarter.csv` |
| 4c | Retailer gross margins by quarter from SEC XBRL (Dick's, Foot Locker, Academy, Genesco, Caleres, Shoe Carnival / Shoe Station) | WORKED, confounded by tariff refunds | `retailer_gross_margin_quarterly.csv`, `retailer_gross_margin_yoy_bps.csv`. Hibbett: acquired by JD, no usable 2025-26 filings. |
| 4d | Retailer and brand commentary (Dick's call, Shoe Station, Nike, adidas, On, Deckers) | WORKED (some SNIPPET only) | quotes are in the note |
| 1/2a | Zappos live listings, 12 brands, same shelf, same day | WORKED | `zappos_live_listings_20261014.csv`, `zappos_brand_discount_summary_20261014.csv`, `zappos_running_discount_summary_20261014.csv`, `zappos_tidy_deduped_20261014.csv` |
| 1/2b | Foot Locker live brand pages (page 1 only, 48 items each) | WORKED, small samples | `footlocker_live_listings_20261014.csv`, `footlocker_brand_discount_summary_20261014.csv` |
| 1/2c | Extended Shopify partner-store panel (10 new stores added to the 16 earlier ones, 25 stores with usable compare-at prices) | WORKED | `shopify_new_stores_20261014.csv.gz`, `shopify_extended_*.csv` |
| 1a | adidas.de vs nike.com/de from Common Crawl, same crawls, Aug and Sep 2025 and 2026 | WORKED | `cc_intl_de_panel.csv`, `intl_de_discount_by_crawl.csv`. 2024 adidas.de pages carry no price (332 of 332 "noprice"), same as US. |
| 1b | adidas.co.uk, adidas.co.jp, adidas.ca, adidas.com.au live | BLOCKED | 403 (UK, AU) or no connection (JP, CA). Common Crawl index for adidas.co.uk: reset on 8 of 8 tries. Not retried further. |
| 1c | JD Sports UK live (adidas and Nike brand pages) | PARTIAL | Product JSON has price and wasPrice, but 403 after the first few requests. 200 rows, no adidas. `jduk_live_listings_20261014.csv` (not used in the verdict) |
| 1d | Zappos pages in Common Crawl (monthly panel 2024 to 2026) | PARTIAL, too thin | only 7 Nike, 5 adidas, 1 Hoka, 1 On product pages in the 2026-34 crawl; stopped. `cc_zappos_panel.csv` kept as evidence |
| 1e | Wayback Machine for adidas.com or Nike history | BLOCKED | web.archive.org connection error (CDX and replay); archive.org availability API 429 |
| 3a | Off-price (TJX, Ross, Burlington, Nordstrom Rack, Saks Off 5th) listings | BLOCKED / SNIPPET | Nordstrom Rack serves a JavaScript bot challenge (no product data); Ross and Burlington home pages only; TJX/Ross/Burlington commentary on Nike not found in searches (2026) |
| 3b | eBay new-with-tags Nike supply | BLOCKED | eBay search 403 |
| 3c | Nike factory-store / clearance intensity | NOT MEASURABLE | no public price feed; only nike.com sale-wall data exist (`pricing_catalog`) and US outlet commentary is generic (ShopBack, Groupon, Slickdeals, SNIPPET) |
| 5 | Published discount trackers (Lyst, Edited, Numerator, Salesforce, Adobe, Centric, Vertical Knowledge) | PARTIAL | only the Vertical Knowledge / Reuters figure (Feb 2024, via Complex, OPENED); no 2026 brand-level tracker is free |
| 6 | Keepa / camelcamelcamel / Amazon price histories | BLOCKED | Keepa API needs a key (account); camelcamelcamel 403; Amazon search returns no product markup |
| 1f | Dick's, Finish Line, Hibbett, JD Sports US, Famous Footwear, Academy, REI, Kohl's, Macy's, Running Warehouse, Scheels | BLOCKED | 403, 406 or captcha challenge |
| 1g | DSW brand pages | PARTIAL | HTML loads but shows one price per tile (no list price in server markup); not used |

## Files

| File | What |
|---|---|
| `ppi_margin_indexes_monthly.csv` | 10 FRED PPI series (shoe stores 448210, shoe stores total 4482, clothing stores 4481, sporting goods stores 451110 and 4511, hobby 451120, jewelry 448310, auto dealers 441110, grocery 445110, footwear manufacturing 316210) |
| `ppi_decomposition_summary.csv` | Jun to Aug 2026 vs 2025 and 2024, percentile, historical SD of YoY |
| `ppi_by_nike_fiscal_quarter.csv` | the indexes averaged by Nike fiscal quarter next to Nike total wholesale growth |
| `retailer_gross_margin_quarterly.csv`, `retailer_gross_margin_yoy_bps.csv` | gross profit / revenue by quarter from SEC XBRL (accession and filing date per row) |
| `zappos_*` | live Zappos listing pulls and summaries (Nike, adidas, HOKA, On, ASICS, New Balance, Brooks, Saucony, Puma, Under Armour, Skechers, Reebok) |
| `footlocker_*` | live Foot Locker brand pages |
| `shopify_new_stores_20261014.csv.gz`, `shopify_extended_lpm_brand_effects.csv`, `shopify_extended_markdown_by_brand.csv`, `shopify_extended_md10_by_store_brand.csv` | Shopify partner-store panel |
| `cc_intl_de_panel.csv`, `intl_de_discount_by_crawl.csv` | Germany panel |
| `scripts/` | every script used; `raw/` holds logs, FRED CSVs, SEC XBRL (gzipped), live HTML samples, Common Crawl index files |

## Re-run

```
python3 -I scripts/ppi_decomp.py; python3 -I scripts/ppi_vs_nike_wholesale.py
python3 -I scripts/retailer_gm.py
python3 -I scripts/zappos_pull.py; python3 -I scripts/zappos_analysis.py
python3 -I scripts/footlocker_pull.py; python3 -I scripts/footlocker_analysis.py
python3 -I ../pricing_catalog/scripts/shopify_pull.py raw/shopify shopify_new_stores_YYYYMMDD.csv <hosts>; python3 -I scripts/shopify_extended_analysis.py
python3 -I scripts/cc_intl_panel.py 400 CC-MAIN-2026-34 CC-MAIN-2025-33 CC-MAIN-2024-33 CC-MAIN-2026-39 CC-MAIN-2025-38 CC-MAIN-2024-38; python3 -I scripts/intl_de_analysis.py
```

## Caveats (also in the note)

1. Zappos and Foot Locker are single-day snapshots, not time series. Only the Germany panel and the earlier US nike.com / adidas.com crawls give changes over time.
2. Zappos listing order is by relevance and each query is capped at 3 pages of 100; samples are not random draws of the catalog. Foot Locker is page 1 of relevance sort only (48 items per page).
3. Nike controls retail pricing through account terms ("PROMOS_EXCLUDED" flags on nike.com, `isDiscountsExcluded` at Foot Locker), so a low third-party markdown incidence for Nike can coexist with heavy discounting on nike.com and in Nike's own wholesale terms (rebates, markdown allowances, returns) that never show on a shelf price.
4. Common Crawl is not a random sample; crawl policy can change the mix. The Germany panel has four matched crawls (Aug and Sep of 2025 and 2026), which is too few for crawl-clustered intervals; the intervals shown resample pages within crawls and so understate uncertainty.
5. Reported retailer margins for the quarter ended Aug 1, 2026 include IEEPA tariff refunds (Dick's $38.1M; Caleres, Genesco and Academy show large GAAP jumps against smaller adjusted ones), so they are not clean markdown measures.
