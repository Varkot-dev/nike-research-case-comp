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

## Checker review

Reviewed 2026-10-14 by a second hunter. Re-pulls are in raw/checker/ (FRED CSVs, BEA DSHURC/DSHURX/DSHURG 2022 to 2026 grep of NipaDataM.txt, StatCan 20-10-0056 zip, ONS IDOG, three NBS Chinese releases, one Eurostat API call). All scripts were re-run on a scratch copy; every output CSV came back byte-identical.

### Re-pulled data points (all match)

| Dataset | Points checked | Result |
|---|---|---|
| FRED PCU448210448210 shoe-store margin | Jun, Jul, Aug 2026 = 93.347, 94.055, 91.202; Jun to Aug 2025 | Match. YoY -38.0, -36.9, -42.0, avg -39.0. Prior low 99.3 (2002-08). Record low holds |
| FRED PCU451110451110, PCU44814481, CUUR0000SEAE, PCU316210316210 | Jun to Aug 2026 | Match: +0.2, +2.1, +3.7, +3.3 avg YoY |
| FRED MRTSSM4482USN shoe stores | Apr to Jul 2026 | Match |
| BEA DSHURC/DSHURX/DSHURG | 168 monthly values 2022 to 2026 | 0 mismatches vs raw subset. FY (Jun to May) nominal +2.5, +2.4, +6.3 (FY24 to FY26), real +2.0, +2.4, +4.6. Q1 FY27 nominal +5.95, real +2.15 |
| StatCan 20-10-0056 | 4581, 4582, 459A Jan to Jul and Jun to Jul 2026 | Match (unadjusted): +5.1/-1.7/+4.8 and +6.0/-0.4/+3.4. SA gives shoe retailers Jun to Jul -1.6 |
| ONS IDOG | Jan to Aug 2026 | Match: avg 3.75, Jun to Aug 3.07 |
| NBS China releases (Aug, Jun, Mar 2026) | sports and recreation and clothes/shoes rows | Match: e.g. Aug sports 134 / -4.8 / YTD 1132 / -3.7; clothes/shoes Aug -0.5, YTD +5.1 |
| Eurostat sts_trtu_m EU27 G47 VOL_SLS SCA | Jun to Aug 2026 | Match: 105.4, 104.9, 105.0 |
| Circana H1 2026 press release | reopened | Confirms +1% dollars, units down, performance +6%, running +13% dollars and units, sport lifestyle declined, fashion flat, 2026 outlook flat |
| Nike regional revenue (repo facts) | Q1 FY25 to Q1 FY27 NA, EMEA, Greater China | Arithmetic matches (-22.0, -4.7, +2.1 YoY) |

Cleaning: no full-row duplicates in any tidy file; no key duplicates in the NBS file; NBS YTD values equal the sum of monthly values within rounding (1132 vs 1130 summed); Nike fiscal quarter mapping (Q1 = Jun to Aug) is correct; partial-quarter guard correctly blanks Q1 FY27 Census shoe stores (August not yet out). Currency: NBS is CNY, Nike Greater China is USD; see below.

### What does not hold or needs correcting

1. **China clothes/shoes "first negative months in the 2023 to 2026 sample" is false.** The file itself shows clothes, shoes, hats and textiles negative in Apr 2024 (-2.0), Jun 2024 (-1.9), Jul 2024 (-5.2), Aug 2024 (-1.6), Sep 2024 (-0.4), Nov 2024 (-4.5) and Dec 2024 (-0.3). July and August 2026 are the first negatives since December 2024, not of the sample.
2. **China "no category floor" is overstated for the category that matters most.** Clothes/shoes YTD Jan to Aug 2026 is +5.1%, better than 2025 (+2.9%) and 2024 (+0.3%). Its two-year stack for Jun to Aug 2026 is +3.1%, better than Jun to Aug 2025 (-0.7%). The collapse is in "sports and recreational articles", which includes toys and games, and the 2025 boom (+25% YTD) fits the collectible-toy wave. The clothes/shoes category is slowing (+4.8 to +0.8 Mar-May to Jun-Aug) but not breaking down. The implication runs the other way for Nike: against clothes/shoes (+0.8% Jun to Aug) Nike Greater China (-22% USD, -26% currency-neutral per the 10-Q) lags by 23 to 27 points, so the Nike-specific share-loss reading gets stronger while the "macro floor is gone" reading gets weaker.
3. **Currency for China.** The 16-point gap compares USD Nike with CNY NBS. Nike's currency-neutral figure is -26%, so the like-for-like gap is about 20 points (wider, not narrower).
4. **EMEA "worse in constant currency because the euro was stronger" is not supported.** The Q1 FY27 10-Q row in repo facts reads "3,176 | 3,331 | -5 | -5": reported and currency-neutral are both -5%.
5. **"FY26 bounce (units +6% to +14% a quarter)"**: quarterly NA footwear units were +5, +14, +4 (Q1 to Q3); the FY figure is +6. Say "+4% to +14%".
6. **Script prints a meaningless cumulative.** test1_us_category_vs_nike.py chains 13 overlapping quarterly YoY rates (prints -25.4 vs +63.5). That output was not used in the summary (the summary's -10.5 vs +11.6 is correctly built from fiscal-year rates), but it should be deleted to stop reuse.

### What holds, with nuance

- **Q1 NA share loss (FY24 to FY26 cumulative): holds.** Nike NA footwear approx -10.5% (FY -2, -13, +5 from 10-K units plus ASP) vs PCE shoes +11.5% nominal. But the share loss is concentrated in FY24 to FY25. In the last four reported quarters Nike NA footwear units ran at or ahead of PCE real (gaps 0.0, +9.2, -1.1, -0.2 points in Q1 FY26, Q2 FY26, Q3 FY26, Q1 FY27; FY26 units +6 vs PCE real +4.6). The current gap is in price (ASP gap vs PCE price -5.6, -5.4, +0.5, -4.7) not volume. So "still losing share in volume today" is not shown; "losing on price and mix" is.
- **Channel fill reading: plausible but rests on Circana units only.** Circana says industry units fell in Q4 2025, Q1 2026 and H1 2026 (Q4 2025 dollars +2% with ASP +8% implies units about -6%) while Nike shipped +14% units in Sep to Nov 2025. BEA real PCE shoes, however, grew +4.6% in FY26. The two disagree because BEA's footwear deflator (+0.4% to +1.5% YoY through Q3 FY26) is far below Circana's ASP (+8%). Which unit measure is right decides the test; Circana is athletic-weighted and point-of-sale, so it is the better read, but only press-release figures exist (no raw unit counts). Strength: moderate to strong, not unconditional strong.
- **Q3 China: SHORT holds as Nike-specific, macro part weaker** (see points 1 to 3). Sports and recreation numbers, two-year stacks (18.4 to 6.7) and Jun to Aug averages (-5.9 vs +13.4) all reproduce exactly.
- **Q4 PPI shoe-store margin: INCONCLUSIVE/weak holds.** Numbers reproduce; agree it is unconfirmed by Caleres and Genesco (both still SNIPPET-tagged, not opened).
- **Outside US/China: moderate SHORT holds.** UK and Canada numbers reproduce. Canada 459A also includes hobby, music and books, and specialist shoe retailers are negative in Canada (SA Jun to Jul -1.6), so footwear specifically is soft. Eurostat data reproduces but is not used in any test.
