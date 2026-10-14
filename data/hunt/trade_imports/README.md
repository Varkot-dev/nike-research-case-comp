# Trade and shipments data hunt (key: trade_imports)

Pulled 2026-10-14. Purpose: test whether Nike-specific shipments into the US are rising or falling into holiday 2026, and whether they diverge from total US footwear imports. All sources are free and need no login. No personal details were sent in any request.

## Tidy files in this folder

| File | What it is | Rows / period |
|---|---|---|
| `us_imports_footwear_apparel_monthly.csv` | US monthly imports by origin (World, Vietnam, China, Indonesia, Cambodia, India, Bangladesh, Brazil, Italy, Mexico), HS 64, 6402, 6403, 6404, 6405, 61, 62. Value in USD, quantity (pairs, qty_unit_code 6) for footwear headings | 6,355 rows, 2019-01 to 2026-07 |
| `us_imports_hs6_athletic_monthly.csv` | Same, HS6 detail 640411, 640419, 640219, 640299, 640391, 640399 for World, VN, CN, ID. 640411 and 640219 are the 'sports footwear' lines | 1,032 rows, 2023-01 to 2026-07 |
| `indonesia_exports_footwear_monthly.csv` | Indonesia exports (reporter 360) to World and US, HS 64/6402/6403/6404/61/62 | 1,092 rows, 2019-01 to 2026-07 |
| `vietnam_exports_footwear_monthly_2019_2023.csv` | Vietnam exports (reporter 704) to World and US; Vietnam stops reporting monthly to Comtrade after Dec 2023 | 2019-01 to 2023-12 |
| `eu_imports_footwear_monthly.csv` | EU27 monthly imports of HS 64, 6402, 6403, 6404 from VN, ID, CN, KH, IN, BD, value in EUR | 2019-01 to 2026-07 |
| `importinfo_monthly_bols.csv` | Bill-of-lading counts per month for 31 company pages (Nike consignee entities, Nike factories as shippers, Nike forwarder APL Logistics, peer consignees adidas, New Balance, Puma, Under Armour, Vans, Crocs) | 3,808 rows, 2012 to 2026-10 |
| `importinfo_company_summary.csv` | Totals, first/last shipment, last 30/90 days, past year per page | 23 pages |
| `importinfo_recent_bols.csv` | The few most recent BOLs printed on each page (port, cartons, kg, shipper, consignee, commodity text) | sample only |
| `nike_factory_map_2026-10-14.csv` | Nike manufacturing map: 712 facilities with tier, product type, supplier group, country, total workers | snapshot |
| `nike_vs_industry_monthly.csv` | Built panel: Feng Tay, Lai Yih, Fulgent Sun, Pou Chen revenue in USD; US footwear imports (World and Nike-sourcing-mix weighted VN 52 / ID 27 / CN 16); EU imports from VN+ID+CN; YoY and gaps | 2019-01 to 2026-09 |
| `test_industry_yoy.csv` | YoY by origin and HS, windows Jan-Jul, May-Jul, Jul | |
| `test_bol_holiday.csv` | Jul-Sep BOL counts 2023 to 2026 by group, YoY and seasonal loading ratios | |
| `test_hs6_athletic_yoy.csv` | Sports vs other footwear imports YoY by origin | |
| `test_two_year_share.csv` | Feng Tay vs 7 industry pipeline series, H1 2026 vs H1 2024 and H1 2025 | |
| `indonesia_vs_fengtay_monthly.csv` | Indonesia footwear exports vs Feng Tay YoY | |
| `test_holiday_gap_history.csv` | Rolling 3-month Feng Tay USD YoY minus US footwear imports YoY (lead 1 month), history | 2020 to 2026 |

## Sources, URLs and methods

1. **UN Comtrade public preview API** (no key): `https://comtradeapi.un.org/public/v1/preview/C/M/HS?reporterCode=842&period=YYYYMM&partnerCode=...&cmdCode=...&flowCode=M`. One period per call, max 500 rows. Script `scripts/pull_comtrade.py`, flattening `scripts/clean_comtrade.py`. Raw JSON in `raw/comtrade/`. US figures are the US Census data as reported to the UN.
2. **US Census FT-900, August 2026 release** (released Oct 2026): `https://www.census.gov/foreign-trade/Press-Release/current_press_release/ft900xlsx.zip` and `exh8.xlsx`, `exh15.xlsx`. Exhibit 15 (NSA, principal SITC commodities) gives footwear imports Aug 2026 $2,483M, Jul 2026 $2,295M, YTD Aug 2026 $17,760M vs $18,115M (-2.0%). Exhibit 8 (SA end-use) footwear Aug $1,588M vs Jul $1,419M. Raw in `raw/census_ft900/`.
3. **Eurostat Comext API** (no key): `https://ec.europa.eu/eurostat/api/comext/dissemination/statistics/1.0/data/DS-045409?format=JSON&freq=M&reporter=EU&partner=VN&flow=1&product=64&indicators=VALUE_IN_EUROS&sinceTimePeriod=2019-01`. Script `scripts/pull_eurostat.py`.
4. **ImportInfo.com public company pages** (US CBP vessel manifests): e.g. `https://www.importinfo.com/nike-usa-inc` and the JSON behind its chart, `https://www.importinfo.com/nike-usa-inc?monthly_chart`. robots.txt allows these pages (it disallows /search and /manifest, which were not touched). Script `scripts/pull_importinfo.py` (3 s sleep), parser `scripts/clean_importinfo.py`. After about 60 requests the site began returning a bot challenge (HTTP 401); scraping stopped there and was not worked around.
5. **Nike manufacturing map** `https://manufacturingmap.nikeinc.com/`: the facility list is embedded as JSON in the site bundle `static/js/main.b8203d9b.js` (saved in `raw/nike_map/`). Parser `scripts/parse_nike_map.py`.
6. **FinMind** mirror of Taiwan MOPS monthly revenue: `https://api.finmindtrade.com/api/v4/data?dataset=TaiwanStockMonthRevenue&data_id=9910` (also 6890, 9802, 9904). Converted to USD with the repo's monthly TWD/USD file (`data/definitive/suppliers/fx_twd_per_usd_monthly_avg.csv`, copied to `raw/repo_fx_twd.csv`).
7. **ImportGenius public Nike USA page** (`raw/misc/`) used only to confirm when Nike's consignee name disappears from manifests.

Tests: `scripts/test_industry.py`, `scripts/test_nike_vs_industry.py`, `scripts/test_holiday.py`, `scripts/test_bol.py`, `scripts/test_hs6_indonesia.py`.

## Known gaps and caveats

- **Nike USA as a named consignee is not observable after November 2022.** ImportInfo shows 43,576 Nike USA BOLs in 2021 and 95,363 in 2022, then 13 in 2023 and 353 in the past year. ImportGenius's Nike USA page stops at 2022-11-16. Nike filed for manifest confidentiality (19 CFR 103.31). So "Nike shipment counts by month" for the US cannot be built from free BOL data for 2023 to 2026.
- **Shipper-side BOL counts are visibility series, not volume series.** Nike factories (Feng Tay, Chang Shin, Freetrend, Pratama, Nikomas) and APL Logistics Vietnam show step changes (for example APL Logistics Vietnam jumps from about 36 a month to 557 in September 2025). Peer consignees show the same breaks (Puma 4 BOLs in all of 2024, Under Armour 0 in 2024). Treat YoY on these as unreliable.
- **Nike Canada Corp** (consignee name still visible) counts only Canadian-bound cargo routed through US ports (for example Tacoma). Routing changes move this series.
- Comtrade July 2026 US quantity (pairs) is incomplete for 6403 to 6405 and for World; use value for July. Vietnam reports to Comtrade only to Dec 2023 (monthly), so Vietnam is covered via US and EU mirror imports. China's 2026 exports were not yet in Comtrade.
- Census API (`api.census.gov`) now requires a key (redirects to missing_key.html); a key requires registering an email, so it was not used. USITC DataWeb requires login.
- Aug 2026 US footwear YoY (+1.8%) is an estimate: SITC 85 Aug 2026 vs an Aug 2025 value backed out from the official YTD and Comtrade monthly shares.
- Feng Tay revenue covers all destinations, not only the US; about 10% to 12% is non-Nike (Salomon).
- EU values are in EUR; EUR/USD moves affect YoY.

## Blocked or unusable sources

ImportYeti (Cloudflare 403, also no Wayback copy), web.archive.org (connection reset through proxy), api.census.gov (key required), Volza (Cloudflare 403), Trademo (Azure WAF 403), Seair (Cloudflare 403), Panjiva (login), ImportInfo BOL list pages and later company pages (bot challenge 401 after about 60 requests), Comtrade Vietnam and China 2024-2026 monthly (not reported yet).

## Test results (run 2026-10-14)

1. **Holiday 2026, one-year view** (`test_holiday.py`). Pre-registered: LONG if Feng Tay USD Jul-Sep is at or above US footwear imports Jul-Aug; SHORT if 5+ points below and in the bottom quartile of its own history. Result: Feng Tay -8.4% vs US footwear imports -1.3% (Jul -4.6%, Aug about +1.8%); gap -7.1 pts, 25th percentile of 2023-2025 3-month gaps, 36th percentile of 2019-2025. Two-year stack (vs 2024): Feng Tay -5.9%, US footwear imports -7.6%, Lai Yih -5.7%, Pou Chen -7.1%. Verdict: most of the one-year gap is a base effect from Nike's strong H2 2025; not a Nike-specific collapse into holiday. NEUTRAL.
2. **Two-year share of the athletic supply pipeline** (`test_two_year_share.py`). Pre-registered: SHORT if Feng Tay H1 2026 vs H1 2024 trails the industry pipeline by 10+ points on most benchmarks; LONG if in line or ahead. Result: Feng Tay -6.9%; US footwear imports +1.5%; Nike-sourcing-mix US imports +9.4%; US sports footwear imports +18.8% value, +12.5% pairs; EU 6404 imports from VN+ID+CN +26.1% (EUR); Indonesia footwear exports +19.2%. Gap -8 to -33 pts on all seven benchmarks. SHORT.
3. **Gap swing (channel fill)** (`test_nike_vs_industry.py`). H2 2025: Feng Tay +0.7% while US footwear imports -11.3% and Nike-mix imports -7.6% (gap +12 to +17 pts monthly). 2026: gap -2 to -7. Consistent with Nike shipping into the channel in H2 2025 while other brands cut after tariff front-loading, then unwinding now. Alternative: other brands front-loaded in H1 2025 ahead of tariffs, which mechanically depresses their H2 2025. Historical gap noise is large (sd about 26 pts), so moderate at best.
4. **Bills of lading** (`test_bol.py`). Nike USA consignee is masked since Nov 2022, so no US Nike shipment count exists in free data. Nike Canada (still named) Jul-Sep 2026 955 BOLs vs 495 (+93%); seasonal loading ratio 1.50 vs 0.58 in 2025; peers adidas -22%, New Balance -25%, Vans -2%. Routing through US ports and BOL splitting can move this series; treat as weak.
