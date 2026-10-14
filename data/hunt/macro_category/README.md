# Macro and category data hunt (key: macro_category)

Pulled 2026-10-14. Question: is the footwear and sportswear category growing (so Nike weakness is share loss) or shrinking, in the US, China and elsewhere?

## Tidy files

| File | What | Period |
|---|---|---|
| us_category_monthly_long.csv | 34 FRED series (Census retail, CPI, PPI incl. retail margin indexes, CES jobs) plus 13 BEA PCE monthly series (shoes and other footwear, clothing, sporting equipment) | 2015-01 to 2026-08 (Census MRTS detail to 2026-07) |
| china_nbs_retail_categories_monthly.csv | NBS monthly retail sales: total, above-size goods, clothes/shoes/hats/textiles, sports and recreational articles, cosmetics, gold; month and YTD value and YoY | 2023-02 to 2026-08 (2022 releases parsed but table layout differs; few rows) |
| europe_retail_hicp_monthly_long.csv | Eurostat sts_trtu_m retail volume and turnover (G47, G47_NF_CLTH, G476, G4791) and HICP footwear CP0321 | 2018-01 to 2026-08 (HICP to 2025-12) |
| canada_retail_by_naics_monthly.csv | StatCan table 20-10-0056, Canada level, shoe retailers 4582, clothing 4581, sporting goods 459A, total | 2017-01 to 2026-07 |
| uk_ons_retail_monthly.csv | ONS retail sales index CSVs incl. IDOG (textile, clothing and footwear stores, volume SA, YoY) | to 2026-08 |
| us_footwear_circana_press.csv | Circana US footwear figures as published in press (no raw Circana data is free) | CY2024 to H1 2026 |
| shoe_retailer_margin_crosscheck.csv | Caleres and Genesco Q2 2026 margins, to cross-check the PPI shoe-store margin index | Q2 2026 |
| test1_us_category_vs_nike_na_quarterly.csv | Category YoY by Nike fiscal quarter vs Nike NA footwear units, ASP, revenue | FY2019 to Q1 FY2027 |
| test2_china_category_monthly.csv | China category YoY, two-year stacks, sports minus total | 2023 to 2026-08 |
| test3_us_retail_margin_ppi_monthly.csv | PPI retail margin indexes (shoe, sporting goods, clothing stores), CPI and PPI footwear | 2018 to 2026-08 |
| tests_2_to_4_results.csv | Summary numbers for tests 2 to 4 | |

## Sources and methods

- FRED: `https://fred.stlouisfed.org/graph/fredgraph.csv?id=<SERIES>` (no key). FRED search pages refused connections; series IDs were probed directly.
- BEA: `https://apps.bea.gov/national/Release/TXT/NipaDataM.txt` (37 MB flat file, no key; subset kept in raw/bea_nipa_monthly_subset.txt) and `SeriesRegister.txt`. DSHURC = PCE shoes and other footwear (NIPA U20405 line 112).
- NBS China: English list `https://www.stats.gov.cn/english/PressRelease/index_N.html` and Chinese list `https://www.stats.gov.cn/sj/zxfb/index_N.html`; each monthly retail release table parsed (scripts/parse_nbs.py). The data.stats.gov.cn query API returned 403 (WAF).
- Eurostat: `https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/sts_trtu_m?...` and prc_hicp_midx.
- StatCan: `https://www150.statcan.gc.ca/n1/tbl/csv/20100056-eng.zip` (full table, filtered to Canada).
- ONS: `https://www.ons.gov.uk/generator?format=csv&uri=/businessindustryandtrade/retailindustry/timeseries/<cdid>/drsi`.
- Circana: press release pages on circana.com (opened) and MR Magazine / SGI Europe write-ups.
- Nike figures are copied from repo files (raw/repo_nike_units_asp_tidy.csv from branch claude/wonderful-franklin-u31n4e data/definitive, raw/repo_nike_filing_facts.csv from data/).

Scripts: scripts/pull_all.sh (FRED, BEA, Eurostat, StatCan, ONS), scripts/pull_nbs_cn.sh (NBS Chinese releases), scripts/parse_nbs.py, scripts/build_tidy.py, scripts/test1_us_category_vs_nike.py, scripts/tests_2_to_4.py. Run Python with `python3 -I`.

## Blocked or unusable

- BLS API v1 (daily threshold reached on the shared IP) and download.bls.gov flat files (403). So CPI men's and women's footwear sub-indexes (SEAE01 to SEAE03) are missing; FRED does not carry them.
- data.stats.gov.cn easyquery API (403 WAF).
- FRED search HTML (connection reset).
- ONS after about 25 requests (Cloudflare 1015 rate limit).
- Eurostat footwear store detail (G4772) has no values; G47_NF_CLTH stops in 2022 to 2023 for FR, IT, ES, DE missing. Europe category is therefore UK plus a few small countries only.
- ABS (Australia) API returned 406; Japan e-Stat needs an app ID (not used); Circana and NPD raw data are paid.

## Caveats

- BLS did not publish October 2025 CPI (government shutdown), so CPI quarter averages for Q2 FY2026 are blank.
- PCE shoes is built partly from Census retail sales and includes all footwear (not only athletic). Circana is the better athletic read but only press figures exist.
- NBS "sports and recreational articles" covers enterprises above designated size and includes toys and games, so the 2025 boom and 2026 fade may partly reflect collectible toys (for example Labubu), not sportswear. NBS month values are not comparable across years (panel changes); only the published YoY rates are used.
- The PPI shoe-store retail margin index (PCU448210448210) is a margin per unit of trade service, not a gross margin percent, and it is volatile. Its 2026 collapse is not confirmed by Caleres or Genesco reported margins; treat it as weak.
- Nike NA footwear revenue growth is approximated as units % plus ASP percentage points (as Nike reports them).
