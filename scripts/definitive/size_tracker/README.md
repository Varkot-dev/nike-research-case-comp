# Size-run tracker (Test 3: size runs left after launch)

Records, per retailer and per size, whether a style code is in stock and at what price.
Broken size runs (only fringe sizes left) = sold through. Full runs at full price weeks after
release = oversupply.

## Files
- `size_tracker.py`: live tracker (nike.com feed, Foot Locker, Champs; Finish Line/JD probe).
- `fl_history.py`: Foot Locker Wayback captures at about 30 and 90 days after release.
- `README.md`: this file.

## Re-run (for example on holiday 2026 releases)
1. Make an input CSV with header `style_code,name,release_date,retail_usd,gender,group`
   (gender `men` or `women`; release_date ISO; retail in USD).
2. Run, from any directory, with an isolated interpreter:
   ```
   python3 -I size_tracker.py --input holiday26.csv --out out/2026-12-26 --asof 2026-12-26
   ```
   Options: `--retailers nike,footlocker,champs,finishline`, `--delay 2.5` (seconds between requests
   to the same host; keep at least 2.5), `--raw DIR` (raw pages, untrusted data).
3. Re-run 14 and 28 days after each release, into a new `--out` folder or the same one (files are
   appended with `asof`, so one folder becomes a time series).
4. History: `python3 -I fl_history.py --input retros.csv --out out/fl_history` (7 s between Wayback calls).

## Outputs
- `size_rows.csv`: retailer x style x size: in_stock, nike_level (HIGH/MEDIUM/LOW/OOS), price, url.
- `size_summary.csv`: retailer x style, DERIVED metrics:
  - `share_grid_in_stock_DERIVED`: men's US 7 to 13 in half sizes (13 sizes); women's US 6 to 11 (11 sizes).
  - `core_all_available_DERIVED`: men's 9, 9.5, 10, 10.5, 11 all in stock (women's 7.5 to 9).
  - `price_vs_retail_DERIVED`: lowest in-stock price / retail - 1.
  - `days_since_release_DERIVED`: asof - release_date (or Nike commerceStartDate if no date given).
  - `nike_merch_status`, `nike_commerce_start`.
- `fetch_log.jsonl`: every request with URL, HTTP status, UTC time and raw file.

## Source rules learned on 2026-10-13
- nike.com: `https://api.nike.com/product_feed/threads/v3/?filter=marketplace(US)&filter=language(en)&filter=channelId(d9a5bc42-4b9c-4976-858a-f159cf99c647)&filter=productInfo.merchProduct.styleColor(<CODE>)`.
  `availableGtins[].level` gives stock per gtin; `skus[]` maps gtin to size. Count a size only when
  `merchProduct.status == ACTIVE` and `commerceStartDate` has passed: INACTIVE/HOLD products return 404 on
  the product page even with HIGH gtin levels, and a future start date shows "Coming Soon".
  The product page's own `sizes[].status` is SKU status, not stock (always ACTIVE), so Wayback captures
  of nike.com pages cannot measure size runs.
- Foot Locker / Champs: `https://www.footlocker.com/product/~/<sku>.html` where sku = style code without the
  dash and without its first character (IQ5495-005 -> Q5495005). The page embeds `"sizes":[...]` with
  `inventory.inventoryAvailable`, `active` and `price.salePrice/listPrice`. Python `requests` gets 403; curl works.
  A style the retailer does not carry gives a page without that sizes array (recorded as not listed).
- Finish Line / JD Sports US: HTTP 403 "Your Access Has Been Denied" (bot wall) to curl, and a headless
  browser timed out, on 2026-10-13. The tracker probes once per run and stops after a refusal.
- No personal email or login is used in any request.
