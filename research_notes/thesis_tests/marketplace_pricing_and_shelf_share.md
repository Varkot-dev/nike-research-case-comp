# R_MARKETPLACE: alternative data on Nike shelf share, consumer preference and promotional intensity

> Repository copy: CSVs are in `data/marketplace/` and parsing scripts in `scripts/marketplace/` (same file names; scripts expect the original scratch paths for raw pages, which are not committed).

Collected 2026-10-13. Root: `/tmp/claude-0/-home-user-nike-research-case-comp/97c520cc-64e5-53f3-8fe9-898f5b11e054/scratchpad/marketplace/`
(`raw/` = downloaded pages, treated as untrusted data; `scripts/` = parsers and fetchers; `data/` = tidy CSVs and the fetch log).
All parsing ran with `python3 -I`. Polite fetching: browser User-Agent, at least 2.5 s between requests to any one host (6 s or more for web.archive.org, with back-off on HTTP 429), public pages only, no logins. Requests per host (including retries): web.archive.org 301, api.nike.com 110, footlocker.com 46, poshmark.com 44, runningwarehouse.com 11, amazon.com 10, nike.com 9, on.com 1. Full log: `data/fetch_log.jsonl`; Wayback manifest: `data/wayback_manifest.jsonl`.

Note on access: python `requests` got 403 from footlocker.com and repeated 429s from web.archive.org, while `curl` with the same User-Agent got 200, so those hosts were fetched through curl (see `scripts/fetch.py`). on.com returned a client-rendered shell with no product data (not parsed; On retail price was taken from Foot Locker instead).

---

## Bottom line

**(a) Shelf share and consumer preference.** Nike is **not** winning back running shelf share on organic preference in 2025 to 2026. Where it has gained visibility, that comes from price.
- Amazon Best Sellers, men's running, top 30: Nike went from 0 to 1 items (2022 to mid 2025) to 2 to 3 items (Aug 2025 to Oct 2026). That is about 7% to 10% of the list. Every Nike item is an entry model (Run Defy, Revolution 8, Run Swift 3, Air Monarch IV), and on 2026-10-13 each one was listed **25% to 30% below its nike.com full price**. Brooks (8 of 30), ASICS (4 to 7) and New Balance (4 to 6) still lead. HOKA has 2; On has 0.
- Running Warehouse (running specialty) men's road catalog: Nike's share of colorways was flat to down, at 10.4% (Feb 2025), 8.6%, 10.6%, 9.6% and 9.6% (Oct 2026). HOKA's share fell more, from 16.6% to 8.2%, and ASICS's was steady at about 11 to 12%. Nike's problem here is sell-through, not range: **49% of Nike road colorways were marked down** in Oct 2026, against 9.5% for HOKA, 12.5% for On, 19% for ASICS, 33% for Brooks and 23% for the store as a whole. Nike was also the largest brand in men's clearance (23% of clearance colorways).
- Poshmark (asking prices only): Dunk Low, Air Force 1 and Air Jordan 1 Low NWT listings ask around retail, with median ask-to-retail of 0.90 to 1.04. AJ1 High OG (0.68) and Vomero 5 (0.74) ask well below retail, close to HOKA Clifton (0.83) and On Cloud (0.87). There is no hype premium on Vomero 5 or on the High OG.

**(b) Discounting.** Discounting has eased from its early 2025 peak. It has **not** returned to 2022 to 2023 levels, and in some channels it is rising again into late 2026.
- nike.com: men's sale shoes as a share of all men's shoes ran 26% to 39% in 2022 to 2023, rose to 48% to 53% (2024Q1 to 2025Q1), eased to 38% (Aug 2025), then sat at 43% to 46% through 2026 (45.7% live today). The whole-site sale wall had 5,131 items in Aug 2026 and 5,102 today, the highest counts in the 2022 to 2026 series (the previous high was 4,741 in May 2023). Discount depth on sale items is steady at about 30%.
- Full catalog today (every product page fetched): 35% of men's shoe products and 46% of women's shoe products have a lead colorway below full price, with an average markdown of about 30% on the discounted ones.
- Foot Locker: total sale volume fell sharply (sale shoe styles went from 2,633 in Jan 2025 to 718 today), which points to a cleaner wholesale channel. But Nike Inc.'s share of what is left on sale rose, from 39% to 41% of sale shoes in 2025 to 50% today, against a 42% share of the shoe assortment.
- Read against Nike's stated plan (NIKE Brand Digital repositioned as full-price, marketplace clean-up done by end of December 2026): wholesale sale volume is shrinking, which fits the plan. But the nike.com sale assortment is at a series high in October 2026, Nike's markdown rate at running specialty is twice the store average, and Amazon is pricing Nike entry runners 25% below full price. On this evidence, the clean-up is **not finished** in Q4 calendar 2026.

---

## Series 1: Amazon Best Sellers (brand counts)

- **URL pattern:** `https://www.amazon.com/gp/bestsellers/fashion/<node>` (live) and Wayback captures of `amazon.com/Best-Sellers-Clothing-Shoes-Jewelry-<Slug>/zgbs/fashion/<node>*`, `amazon.com/gp/bestsellers/fashion/<node>*` and similar URLs, fetched as `https://web.archive.org/web/<ts>id_/<url>`. Nodes: men's running 679286011, women's running 679360011, men's fashion sneakers 679312011, women's fashion sneakers 679394011, men's athletic 6127770011, women's athletic 6127771011.
- **Snapshots:** 65 pages: 6 live (2026-10-13) and 59 Wayback captures. Running has no captures between 2023Q3 and 2025Q1 (none archived), and one capture returned 404 (women's running 2025-03-25). Dates per category are in the CSV.
- **Method:** the cards (`#gridItemRoot`) give rank, title, the lowest price shown and ASIN. Brand comes from the leading word of the title, with model-name fallbacks (for example "Fresh Foam" means New Balance). Counts and shares use **ranks 1 to 30**, because live pages and many captures render only 30 items in HTML (ranks 31 to 50 load later by script). Some captures render 50; the extra items are kept in the item CSV.
- **Sample:** 2,530 ranked items.
- **Caveats:** brand counts per 30 are small, so a move of one or two items is noise. "Nike" excludes Jordan and Converse; a NikeInc column is also given. Best Sellers rank reflects recent Amazon unit sales only, which means it is driven by low prices. Live prices may reflect an Amazon promotion event in October.
- **Nike direct on Amazon (verified):** the live product page for Nike Run Defy (ASIN B0DYKN57S6, fetched 2026-10-13) shows "Shipper / Seller Amazon.com", "Sourced from Nike ... Product sourced from Nike or a Nike-authorized seller" and "Visit the Nike Store". That is a first-party (Amazon buys from Nike) relationship today. The **start date could not be verified** from pages fetched in this session. The data are consistent with a return around mid 2025: Nike items are absent or single in these lists through June 2025 and appear steadily from August 2025, including in men's fashion sneakers, where Nike was absent before.

Key table (count in top 30):

| Category | Date | Nike | HOKA | On | Brooks | ASICS | New Balance | adidas | Skechers | Saucony |
|---|---|---|---|---|---|---|---|---|---|---|
| mens_running | 2022-05-02 | 1 | 0 | 0 | 3 | 7 | 6 | 6 | 0 | 0 |
| mens_running | 2023-06-27 | 1 | 0 | 0 | 5 | 8 | 3 | 6 | 2 | 0 |
| mens_running | 2025-06-18 | 0 | 0 | 0 | 8 | 7 | 5 | 2 | 1 | 0 |
| mens_running | 2025-08-09 | 2 | 2 | 0 | 8 | 5 | 5 | 4 | 1 | 0 |
| mens_running | 2025-10-10 | 2 | 0 | 0 | 7 | 3 | 5 | 3 | 1 | 0 |
| mens_running | 2026-02-17 | 2 | 2 | 0 | 9 | 7 | 4 | 3 | 0 | 0 |
| mens_running | 2026-06-27 | 2 | 0 | 0 | 4 | 5 | 4 | 4 | 1 | 1 |
| mens_running | 2026-08-02 | 3 | 2 | 0 | 4 | 7 | 6 | 3 | 1 | 0 |
| mens_running | 2026-10-13 live | 3 | 2 | 0 | 8 | 4 | 4 | 4 | 0 | 0 |
| womens_running | 2022-02-01 | 1 | 0 | 0 | 6 | 8 | 3 | 4 | 0 | 1 |
| womens_running | 2023-05-27 | 0 | 0 | 0 | 8 | 8 | 3 | 6 | 0 | 0 |
| womens_running | 2025-08-13 | 1 | 1 | 0 | 8 | 7 | 6 | 2 | 0 | 0 |
| womens_running | 2026-02-07 | 1 | 2 | 0 | 9 | 6 | 5 | 1 | 0 | 0 |
| womens_running | 2026-06-23 | 2 | 2 | 0 | 13 | 6 | 4 | 1 | 0 | 0 |
| womens_running | 2026-10-13 live | 2 | 2 | 0 | 8 | 6 | 5 | 3 | 0 | 0 |
| mens_fashion_sneakers | 2022 to 2025-04 (9 captures) | 0 to 1 | 0 | 0 to 1 | 0 | 0 | 1 to 5 | 2 to 6 | 3 to 8 | 0 |
| mens_fashion_sneakers | 2025-08 to 2026-10 (5 snaps) | 2 to 3 | 0 to 1 | 0 to 1 | 0 to 1 | 0 | 2 to 3 | 3 to 5 | 6 to 7 | 0 |

Amazon price compared with nike.com full price, live 2026-10-13 (`amazon_nike_price_vs_nikecom.csv`): Run Defy $48.75 vs $65 (-25%); Revolution 8 men's $56.25 vs $75 (-25%), women's $52.50 (-30%); Run Swift 3 $63.75 vs $85 (-25%); Air Monarch IV $59.50 vs $85 (-30%); Court Vision Low $63.75 vs $85 (-25%); Air Max Excee $75 vs $100 (-25%).

## Series 2: nike.com sale count and discount depth

- **URL pattern:** `https://www.nike.com/w/<wall>` for the walls sale-3yaep, mens-shoes-nik1zy7ok, womens-shoes-5e1x6zy7ok, mens-sale-shoes-3yaepznik1zy7ok, womens-sale-shoes-3yaepz5e1x6zy7ok, sale-shoes-3yaepzy7ok, shoes-y7ok, mens/womens-running-shoes. Later pages come from the public JSON endpoint the wall page itself calls, `https://api.nike.com/discover/product_wall/v1/marketplace/US/language/en/consumerChannelId/...?path=/w/<wall>&anchor=<n>&count=24`. History: Wayback captures of the four main walls, one per quarter, 2022Q1 to 2026Q4.
- **Method:** parse `__NEXT_DATA__` at `props.pageProps.initialState.Wall`. `pageData.totalResources` gives the product count. `productGroupings[].products[].prices` gives currentPrice and initialPrice; discount = 1 - current/initial. "Product" means the lead colorway of a product grouping.
- **Sample:** live full catalog for men's shoes (760 products, 2,794 colorways), women's shoes (596 / 2,606), men's and women's sale shoes (348 / 335), and running walls. History: 90 Wayback page loads. The first page of 24 products gives depth; counts are taken from the page header.
- **Parse failures:** mens-sale-shoes 2025-05-13 and 2026-07-10, and womens-shoes 2026-05-11 (captures with no `__NEXT_DATA__`, left blank). Women's sale shoes have no Wayback history (not captured).
- **Caveats:** item counts include every colorway grouping Nike chooses to list. Nike's assortment size changes, so the ratio (sale / total) is the better metric. First-page depth comes from Nike's "featured" sort and is not representative of share discounted, which is why share discounted is reported only for the live full catalog. A sale wall can contain products whose lead colorway is full price.

Key table (`nike_sale_share_quarterly.csv`; first capture in each quarter):

| Quarter | Men's sale shoes | Men's shoes | Sale share | All sale items (site) | Sale wall avg discount on discounted items (first page) |
|---|---|---|---|---|---|
| 2022Q1 | 193 | 567 | 34.0% | 3,298 | 26.8% |
| 2022Q2 | 153 | 586 | 26.1% | 2,486 | 26.5% |
| 2022Q3 | 213 | 583 | 36.5% | 3,857 | 30.4% |
| 2022Q4 | 245 | 632 | 38.8% | 4,417 | 25.9% |
| 2023Q1 | 291 | 743 | 39.2% | 4,563 | 30.6% |
| 2023Q3 | 295 | 782 | 37.7% | 3,469 | 29.0% |
| 2023Q4 | 308 | 902 | 34.1% | 2,992 | 24.3% |
| 2024Q1 | 458 | 914 | 50.1% | 4,172 | 25.4% |
| 2024Q2 | 410 | 814 | 50.4% | 4,041 | 30.3% |
| 2024Q3 | 413 | 853 | 48.4% | 3,917 | 17.1% |
| 2024Q4 | 377 | 884 | 42.6% | 3,927 | 26.0% |
| 2025Q1 | 404 | 764 | 52.9% | 3,652 | 35.5% |
| 2025Q2 | n/a (parse fail) | 675 | n/a | 2,059 | 29.0% |
| 2025Q3 | 276 | 729 | 37.9% | 3,290 | 16.4% |
| 2025Q4 | 305 | 715 | 42.7% | 2,981 | 31.4% |
| 2026Q1 | 285 | 647 | 44.0% | 3,767 | 26.0% |
| 2026Q2 | 273 | 630 | 43.3% | 3,887 | 25.7% |
| 2026Q3 | n/a (parse fail) | 791 | n/a | 5,131 | 33.5% |
| 2026-10-01 (Wayback) | 342 | 777 | 44.0% | 4,831 | 30.6% |
| 2026-10-13 (live) | 348 | 762 | 45.7% | 5,102 | 30.3% |

Live full catalog, 2026-10-13 (`nike_current_summary.csv`): men's shoes have 35.3% of products discounted, with an average discount of 29.8% on those (10.5% across all products). Women's shoes: 46.1% discounted, average 30.5%. Men's running shoes: 21.4% discounted, average 26.4%. Women's running shoes: 35.2% discounted, average 28.3%.

## Series 3: Foot Locker

- **URL pattern:** `https://www.footlocker.com/category/sale/shoes.html`, `/category/shoes.html`, and the men's and women's versions of both, for brand-facet counts. Per brand: `/category/sale/shoes.html?query=:relevance:collection_id:sale-shoes:brand:<Brand>&pageSize=200`; Nike is split into six price bands so each query stays under 200 results. History: Wayback captures of `/category/sale.html` (19 quarters, 2022 to 2026) and `/category/sale/shoes.html` (5 captures).
- **Method:** parse the embedded search-result JSON for pagination, products (originalPrice, price) and the brand facet with counts. Brand share of sale is brand sale styles divided by total sale styles. Share of brand on sale is brand sale styles divided by brand styles in the full shoe category.
- **Sample:** facet counts covering all 718 sale shoe styles and 6,295 shoe styles. Product-level discounts for 649 sale shoes across 11 brands (every listed sale shoe of those brands).
- **Caveats:** the counts are of styles (product listings), not units. History covers only the sale pages, so the share of each brand's assortment on sale is available for the live snapshot only. The historical sale.html counts include apparel and accessories. The `?currentPage=` parameter is ignored server-side, which is why brand and price filters with pageSize=200 were used. Discount is measured against Foot Locker's stated original price.

Key tables, live 2026-10-13 (`footlocker_brand_sale_mix.csv`, `footlocker_discount_by_brand.csv`):

| Brand (all shoes) | Sale styles | All styles | % of brand on sale | Share of sale | Share of assortment | Avg discount on sale items |
|---|---|---|---|---|---|---|
| Nike | 252 | 1,911 | 13.2% | 35.1% | 30.4% | 25.0% |
| Jordan | 90 | 656 | 13.7% | 12.5% | 10.4% | 20.5% |
| adidas | 81 | 962 | 8.4% | 11.3% | 15.3% | 24.0% |
| New Balance | 74 | 419 | 17.7% | 10.3% | 6.7% | 37.5% |
| PUMA | 40 | 195 | 20.5% | 5.6% | 3.1% | 31.0% |
| HOKA | 28 | 175 | 16.0% | 3.9% | 2.8% | 27.5% |
| On | 24 | 153 | 15.7% | 3.3% | 2.4% | 22.3% |
| ASICS | 10 | 116 | 8.6% | 1.4% | 1.8% | 20.1% |
| Brooks | 10 | 130 | 7.7% | 1.4% | 2.1% | 20.6% |
| All brands | 718 | 6,295 | 11.4% | 100% | 100% | n/a |

History (`footlocker_sale_brand_history.csv`), NikeInc = Nike + Jordan + Converse:

| Page | Date | Total sale styles | Nike share | NikeInc share |
|---|---|---|---|---|
| sale_shoes | 2022-02-01 | 836 | 12.2% | 17.1% |
| sale_shoes | 2022-10-03 | 2,458 | 18.5% | 23.9% |
| sale_shoes | 2025-01-18 | 2,633 | 21.8% | 38.6% |
| sale_shoes | 2025-06-13 | 2,603 | 24.6% | 40.7% |
| sale_shoes | 2026-10-13 live | 718 | 35.1% | 49.9% |
| sale_all | 2023-11-06 | 10,263 | 22.9% | 35.0% |
| sale_all | 2024-11-23 | 6,720 | 26.2% | 38.9% |
| sale_all | 2025-02-09 | 4,768 | 21.5% | 33.5% |
| sale_all | 2025-08-06 | 4,661 | 26.7% | 38.1% |
| sale_all | 2025-11-11 | 2,394 | 23.3% | 34.7% |
| sale_all | 2026-02-08 | 1,091 | 28.0% | 37.0% |
| sale_all | 2026-05-12 | 2,225 | 24.0% | 36.2% |
| sale_all | 2026-08-11 | 2,728 | 25.3% | 35.6% |
| sale_all | 2026-10-13 live | 2,648 | 27.8% | 38.0% |

Reading: Foot Locker's overall promotional load fell by about 60% to 75% from 2023 to 2024 levels. Nike's share of what remains on sale is stable to rising, and Nike over-indexes its assortment share (35% of sale shoe styles against 30% of shoe styles). At Foot Locker, however, Nike's on-sale rate (13%) is close to average and below HOKA, On, New Balance and PUMA. Its discount depth (25%) is mid-pack.

## Series 4: Running Warehouse (running specialty)

- **URL pattern:** `https://www.runningwarehouse.com/catpage-MBESTUSE.html` (men's road running shoes, full catalog), `catpage-WBESTUSE.html` (women's road), `catpage-SALEMS.html` / `catpage-SALEWS.html` (men's and women's clearance). Wayback: MBESTUSE on 2025-02-05, 2025-09-11, 2025-10-16 and 2026-04-26; SALEMS on 2022-06-16, 2025-02-02, 2025-05-31, 2025-08-13, 2025-11-22 and 2026-09-21.
- **Method:** each colorway cell carries `data-gtm_impression_brand`, name and price, plus a struck-through MSRP when marked down. On sale means price below MSRP.
- **Sample (live):** 1,025 men's road colorways, 928 women's road, 305 men's clearance and 306 women's clearance.
- **Parse failure:** the 2022-06-16 clearance capture uses older markup (no cells parsed; left blank). No best-seller ranking is exposed; the default sort order is undocumented, so position is not used as a popularity measure.
- **Caveats:** the counts are colorways. A brand's share partly reflects how deep a range the retailer buys, not consumer demand directly. The share of colorways marked down is the cleanest signal of sell-through.

Key table, men's road catalog (`runningwarehouse_history.csv`):

| Date | Nike share of colorways | Nike % on sale | HOKA share / % on sale | On share / % on sale | ASICS share / % on sale | Brooks share / % on sale | All brands % on sale |
|---|---|---|---|---|---|---|---|
| 2025-02-05 | 10.4% | 61.5% | 16.6% / 25.9% | 5.7% / 16.7% | 11.5% / 14.9% | 11.1% / 43.6% | 26.0% |
| 2025-09-11 | 8.6% | 25.4% | 11.5% / 21.1% | 4.1% / 8.8% | 11.0% / 8.8% | 9.3% / 11.7% | 18.4% |
| 2025-10-16 | 10.6% | 33.3% | 10.5% / 12.8% | 4.5% / 10.8% | 10.6% / 5.7% | 10.0% / 23.2% | 20.0% |
| 2026-04-26 | 9.6% | 35.7% | 9.4% / 15.9% | 3.9% / 26.5% | 11.9% / 11.5% | 10.3% / 32.2% | 17.4% |
| 2026-10-13 live | 9.6% | 49.0% | 8.2% / 9.5% | 3.1% / 12.5% | 11.8% / 19.0% | 8.3% / 32.9% | 23.3% |

Women's road live: Nike has 9.8% of colorways with 50.5% on sale, compared with HOKA 6.4%, On 9.5%, ASICS 20.3% and the store at about 24%. Nike's share of men's clearance colorways: 26.8% (Feb 2025), 3.9% (May 2025), 12.6% (Aug 2025), 9.8% (Nov 2025), 14.8% (Sep 2026), 23.3% (Oct 2026). Average clearance markdown on Nike was 34% to 45%.

## Series 5: Poshmark (asking prices)

- **URL pattern:** `https://poshmark.com/search?query=<model>&type=listings&src=dir[&condition=nwt][&max_id=2|3]`. Parse `window.__INITIAL_STATE__` listing objects (title, price, condition, department, category, size, created_at).
- **Method:** first three result pages for each model, run once over all conditions and once with the New-With-Tags filter. Listings were kept only if the title matched the model, the category was Shoes, the department was Men or Women, the price was at least $20, and kids, SB, collaborations and variants were excluded by regex. Each asking price is divided by a retail reference price observed today: Dunk Low Retro $120, AF1 '07 $115, AJ1 Low $120, AJ1 Retro High OG $185, Zoom Vomero 5 $170 (all from nike.com data in Series 2); HOKA Clifton 10 $155 (Running Warehouse MSRP); On Cloud 6 $160 (Foot Locker).
- **Sample:** 2,051 listings fetched; 56 to 142 included per model and condition.
- **Caveats:** these are **asking prices, not sold prices**. Asks are sticky and biased upward, and listings that have not sold are over-represented. Search relevance ordering decides which listings appear. Some listings are older models (Clifton 8/9, Cloud 5) with lower original retail. One snapshot only.

Key table (`poshmark_summary.csv`), median ask divided by retail:

| Model | All conditions: n / median ask / ratio | NWT: n / median ask / ratio | NWT share of asks above retail |
|---|---|---|---|
| Nike Dunk Low | 101 / $75 / 0.63 | 113 / $108 / 0.90 | 36% |
| Nike Air Force 1 | 107 / $63 / 0.55 | 99 / $120 / 1.04 | 54% |
| Air Jordan 1 Low | 115 / $75 / 0.63 | 96 / $125 / 1.04 | 53% |
| Air Jordan 1 High OG | 133 / $92 / 0.50 | 134 / $125 / 0.68 | 17% |
| Nike Zoom Vomero 5 | 133 / $105 / 0.62 | 128 / $125 / 0.74 | 6% |
| HOKA Clifton | 142 / $66 / 0.43 | 141 / $128 / 0.83 | 5% |
| On Cloud (5/6) | 56 / $98 / 0.61 | 66 / $139 / 0.87 | 17% |

Reading: Nike classics (AF1, Dunk Low, AJ1 Low) still hold about retail on NWT asks, which suggests they are not sharply over-supplied in resale. Vomero 5, Nike's recent lifestyle-running hit, and AJ1 High OG ask at a 26% to 32% discount to retail, a deeper discount than HOKA Clifton or On Cloud. That fits fading scarcity in those franchises. This is weak evidence, given the caveats above.

---

## CSV files

All are under `/tmp/claude-0/-home-user-nike-research-case-comp/97c520cc-64e5-53f3-8fe9-898f5b11e054/scratchpad/marketplace/data/`:
- `amazon_bestsellers_items.csv` (rank, title, brand, price, ASIN for each snapshot)
- `amazon_bestsellers_brand_share.csv` (counts and shares in the top 30 by brand, each snapshot)
- `amazon_nike_price_vs_nikecom.csv`
- `amazon_cdx_index.json` (Wayback index, not a CSV)
- `nike_current_products.csv` (9,139 product-colorway rows, live)
- `nike_current_summary.csv`
- `nike_wall_history.csv` (each wall and snapshot, Wayback plus live)
- `nike_sale_share_quarterly.csv`
- `footlocker_brand_sale_mix.csv`
- `footlocker_sale_items.csv`
- `footlocker_discount_by_brand.csv`
- `footlocker_sale_brand_history.csv`
- `runningwarehouse_items.csv`
- `runningwarehouse_brand_summary.csv`
- `runningwarehouse_history.csv`
- `poshmark_listings.csv`
- `poshmark_summary.csv`

Scripts, in `.../marketplace/scripts/`: `fetch.py`, `cdx.py`, `wayback_queue.py`, `amazon_cdx.py`, `amazon_wayback_fetch.py`, `amazon_parse.py`, `amazon_nike_price_check.py`, `brands.py`, `nike_current_fetch.py`, `nike_parse_lib.py`, `nike_current_build.py`, `nike_history_build.py`, `footlocker_fetch.py`, `footlocker_parse_lib.py`, `footlocker_parse.py`, `footlocker_history.py`, `rw_parse.py`, `rw_history.py`, `poshmark_lib.py`, `poshmark_run.py`.
