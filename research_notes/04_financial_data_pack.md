# Nike financial data pack (rebuilt from SEC filings, Oct 12, 2026)

**How this was built.** Every Nike 10-K for FY2019 to FY2026, every 10-Q from Q1 FY2024 to Q1 FY2027, every quarterly
earnings 8-K (Exhibit 99.1) from Q4 FY2019 to Q1 FY2027, the 2026 proxy (DEF 14A) and the 2024 to 2026 leadership and
restructuring 8-Ks were downloaded from sec.gov and read in full. Each number below was extracted with a verbatim quote
and then machine-checked: the value had to appear on the cited page of the cited filing. The complete cell-level record
(filing, printed page, URL, quote) is `data/nike_filing_facts.csv`; this file is generated from it by
`scripts/build_data_pack.py`, so the two cannot drift apart.

**Conventions.** USD millions unless noted. Fiscal year ends May 31. Page numbers are the printed page numbers in the
filing (10-K, 10-Q, proxy). Earnings releases have no printed page numbers, so their pages are counted from the first page
of the Exhibit 99.1 press release. Each table row is drawn from the filing that first reported that period (10-K for the
year, 10-Q for Q1 to Q3, the Q4 earnings release for Q4), so values are as originally reported. Where Nike later
reclassified a figure, the CSV notes the count of sources that agree. "n/a" means the filing does not report it.

## 1. Annual income statement

### Revenue, margin, earnings

| Period | Revenue | Gross profit | Gross margin % | Demand creation | Operating overhead | EBIT | Tax rate % | Net income | Diluted EPS ($) | Diluted shares (m) | Source (filing, printed page) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FY2019 | 39,117 | 17,474 | 44.7 | 3,753 | 8,949 | 4,850 | 16.1 | 4,029 | 2.49 | 1618.4 | FY2019 10-K p. 22, 26, 31, 50 |
| FY2020 | 37,403 | 16,241 | 43.4 | 3,592 | 9,534 | 2,976 | 12.1 | 2,539 | 1.60 | 1591.6 | FY2020 10-K p. 25, 30, 35 |
| FY2021 | 44,538 | 19,962 | 44.8 | 3,114 | 9,911 | 6,923 | 14.0 | 5,727 | 3.56 | 1609.4 | FY2021 10-K p. 31, 36, 57 |
| FY2022 | 46,710 | 21,479 | 46.0 | 3,850 | 10,954 | 6,856 | 9.1 | 6,046 | 3.75 | 1610.8 | FY2022 10-K p. 31, 36, 56 |
| FY2023 | 51,217 | 22,292 | 43.5 | 4,060 | 12,317 | 6,195 | 18.2 | 5,070 | 3.23 | 1569.8 | FY2023 10-K p. 31, 55; Q4 FY2023 release p. 6 |
| FY2024 | 51,362 | 22,887 | 44.6 | 4,285 | 12,291 | 6,539 | 14.9 | 5,700 | 3.73 | 1529.7 | FY2024 10-K p. 31, 33, 57 |
| FY2025 | 46,309 | 19,790 | 42.7 | 4,689 | 11,399 | 3,778 | 17.1 | 3,219 | 2.16 | 1487.6 | FY2025 10-K p. 32, 56; Q4 FY2025 release p. 6 |
| FY2026 | 46,398 | 19,911 | 42.9 | 4,754 | 11,360 | 3,850 | 20.3 | 3,108 | 2.10 | 1481.0 | FY2026 10-K p. 31, 32, 55 |

## 2. Annual revenue by segment, channel and product

### Operating segments (reported revenues)

| Period | North America | EMEA | Greater China | APLA | Global Brand Div. | NIKE Brand | Converse | Corporate | Source (filing, printed page) |
|---|---|---|---|---|---|---|---|---|---|
| FY2019 | 15,902 | 9,812 | 6,208 | 5,254 | 42 | 37,218 | 1,906 | -7 | FY2019 10-K p. 27, 30 |
| FY2020 | 14,484 | 9,347 | 6,679 | 5,028 | 30 | 35,568 | 1,846 | -11 | FY2020 10-K p. 31, 35 |
| FY2021 | 17,179 | 11,456 | 8,290 | 5,343 | 25 | 42,293 | 2,205 | 40 | FY2021 10-K p. 36 |
| FY2022 | 18,353 | 12,479 | 7,547 | 5,955 | 102 | 44,436 | 2,346 | -72 | FY2022 10-K p. 36 |
| FY2023 | 21,608 | 13,418 | 7,248 | 6,431 | 58 | 48,763 | 2,427 | 27 | Q4 FY2023 release p. 4; FY2023 10-K p. 32, 36 |
| FY2024 | 21,396 | 13,607 | 7,545 | 6,729 | 45 | 49,322 | 2,082 | -42 | FY2024 10-K p. 38 |
| FY2025 | 19,572 | 12,257 | 6,586 | 6,251 | 48 | 44,714 | 1,692 | -97 | Q4 FY2025 release p. 4; FY2025 10-K p. 33, 37 |
| FY2026 | 20,511 | 12,572 | 5,847 | 6,243 | 49 | 45,222 | 1,174 | 2 | FY2026 10-K p. 32, 36 |

### NIKE Brand channel and product

| Period | NIKE Direct | Wholesale | Footwear | Apparel | Equipment | Jordan Brand | Source (filing, printed page) |
|---|---|---|---|---|---|---|---|
| FY2019 | 11,753 | 25,423 | 24,222 | 11,550 | 1,404 | 3,138 | FY2019 10-K p. 27 |
| FY2020 | 12,382 | 23,156 | 23,305 | 10,953 | 1,280 | 3,609 | FY2020 10-K p. 31 |
| FY2021 | 16,370 | 25,898 | 28,021 | 12,865 | 1,382 | 4,780 | FY2021 10-K p. 32; FY2023 10-K p. 32 |
| FY2022 | 18,726 | 25,608 | 29,143 | 13,567 | 1,624 | 5,122 | FY2022 10-K p. 32 |
| FY2023 | 21,308 | 27,397 | 33,135 | 13,843 | 1,727 | 6,589 | FY2023 10-K p. 32 |
| FY2024 | 21,519 | 27,758 | 33,427 | 13,775 | 2,075 | 6,988 | FY2024 10-K p. 34 |
| FY2025 | 18,783 | 25,883 | 29,510 | 12,965 | 2,191 | 7,270 | FY2025 10-K p. 33 |
| FY2026 | 17,720 | 27,453 | 29,525 | 13,449 | 2,199 | 7,034 | FY2026 10-K p. 32 |

Jordan Brand revenue is shown as reported in each year's 10-K. Later filings restate some product and Jordan splits (for example, FY2023 and FY2024 Jordan figures differ between the FY2024 and FY2025 10-Ks); use one year's 10-K for any trend.

### Segment EBIT

| Period | North America | EMEA | Greater China | APLA | Converse | Global Brand Div. | Corporate | Source (filing, printed page) |
|---|---|---|---|---|---|---|---|---|
| FY2019 | 3,925 | 1,995 | 2,376 | 1,323 | 303 | -3,262 | -1,810 | FY2019 10-K p. 31 |
| FY2020 | 2,899 | 1,541 | 2,490 | 1,184 | 297 | -3,468 | -1,967 | FY2020 10-K p. 35 |
| FY2021 | 5,089 | 2,435 | 3,243 | 1,530 | 543 | -3,656 | -2,261 | FY2021 10-K p. 36 |
| FY2022 | 5,114 | 3,293 | 2,365 | 1,896 | 669 | -4,262 | -2,219 | FY2022 10-K p. 36 |
| FY2023 | 5,454 | 3,531 | 2,283 | 1,932 | 676 | -4,841 | -2,840 | FY2023 10-K p. 36; Q4 FY2023 release p. 6 |
| FY2024 | 5,822 | 3,388 | 2,309 | 1,885 | 474 | -4,720 | -2,619 | FY2024 10-K p. 38 |
| FY2025 | 4,735 | 2,575 | 1,602 | 1,527 | 240 | -4,699 | -2,202 | FY2025 10-K p. 37; Q4 FY2025 release p. 6 |
| FY2026 | 5,376 | 2,417 | 1,278 | 1,387 | 18 | -4,603 | -2,023 | FY2026 10-K p. 36 |

## 3. Balance sheet at fiscal year end

### May 31 balances

| Period | Cash | ST investments | Inventories | Total assets | Current LTD | Notes payable | Long-term debt | Equity | Source (filing, printed page) |
|---|---|---|---|---|---|---|---|---|---|
| 2019-05-31 | 4,466 | 197 | 5,622 | 23,717 | 6 | 9 | 3,464 | 9,040 | FY2019 10-K p. 52 |
| 2020-05-31 | 8,348 | 439 | 7,367 | 31,342 | 3 | 248 | 9,406 | 8,055 | FY2020 10-K p. 58 |
| 2021-05-31 | 9,889 | 3,587 | 6,854 | 37,740 | n/a | 2 | 9,413 | 12,767 | FY2021 10-K p. 59 |
| 2022-05-31 | 8,574 | 4,423 | 8,420 | 40,321 | 500 | 10 | 8,920 | 15,281 | FY2022 10-K p. 58 |
| 2023-05-31 | 7,441 | 3,234 | 8,454 | 37,531 | n/a | 6 | 8,927 | 14,004 | FY2023 10-K p. 57 |
| 2024-05-31 | 9,860 | 1,722 | 7,519 | 38,110 | 1,000 | 6 | 7,903 | 14,430 | FY2024 10-K p. 59 |
| 2025-05-31 | 7,464 | 1,687 | 7,489 | 36,579 | 0 | 5 | 7,961 | 13,213 | FY2025 10-K p. 58; Q4 FY2025 release p. 3 |
| 2026-05-31 | 7,563 | 1,464 | 7,501 | 38,410 | 2,000 | n/a | 5,942 | 14,865 | FY2026 10-K p. 57 |

## 4. Cash flow, dividends, buybacks, people

### Cash flow and shareholder returns

| Period | Cash from operations | Capex (PP&E additions) | Dividends paid | Share repurchases | Dividends declared / share ($) | Source (filing, printed page) |
|---|---|---|---|---|---|---|
| FY2019 | 5,903 | 1,119 | 1,332 | 4,286 | 0.860 | FY2019 10-K p. 22, 53 |
| FY2020 | 2,485 | 1,086 | 1,452 | 3,067 | 0.955 | FY2020 10-K p. 25, 59 |
| FY2021 | 6,657 | 695 | 1,638 | 608 | 1.070 | FY2021 10-K p. 60, 61 |
| FY2022 | 5,188 | 758 | 1,837 | 4,014 | 1.190 | FY2022 10-K p. 59, 60 |
| FY2023 | 5,841 | 969 | 2,012 | 5,480 | 1.325 | FY2023 10-K p. 58; FY2024 10-K p. 60; Q4 FY2023 release p. 2 |
| FY2024 | 7,429 | 812 | 2,169 | 4,250 | 1.450 | FY2024 10-K p. 60, 61 |
| FY2025 | 3,698 | 430 | 2,300 | 2,985 | 1.570 | FY2025 10-K p. 59; FY2026 10-K p. 58; Q4 FY2025 release p. 2 |
| FY2026 | 2,868 | 684 | 2,407 | 146 | 1.630 | FY2026 10-K p. 58, 59 |

Operating cash flow minus capex is not a Nike-reported measure; compute it from these columns if needed.

### Employees

| Period | Employees (approx.) | Source (filing, printed page) |
|---|---|---|
| 2019-05-31 | 76,700 | FY2019 10-K p. 6 |
| 2020-05-31 | 75,400 | FY2020 10-K p. 6 |
| 2021-05-31 | 73,300 | FY2021 10-K p. 6 |
| 2022-05-31 | 79,100 | FY2022 10-K p. 6 |
| 2023-05-31 | 83,700 | FY2023 10-K p. 6 |
| 2024-05-31 | 79,400 | FY2024 10-K p. 6 |
| 2025-05-31 | 77,800 | FY2025 10-K p. 6 |
| 2026-05-31 | 73,000 | FY2026 10-K p. 6 |

## 5. Quarterly results (Q1 FY2024 to Q1 FY2027)

### Quarterly income statement

| Period | Revenue | Gross margin % | Net income | Diluted EPS ($) | Reported growth % | Currency-neutral growth % | Source (filing, printed page) |
|---|---|---|---|---|---|---|---|
| Q1 FY2024 | 12,939 | 44.2 | 1,450 | 0.94 | 2 | 2 | Q1 FY2024 10-Q p. 1, 23; Q1 FY2024 release p. 1 |
| Q2 FY2024 | 13,388 | 44.6 | 1,578 | 1.03 | 1 | -1 | Q2 FY2024 10-Q p. 1, 26; Q2 FY2024 release p. 1 |
| Q3 FY2024 | 12,429 | 44.8 | 1,172 | 0.77 | 0 | n/a | Q3 FY2024 10-Q p. 1, 27; Q3 FY2024 release p. 1 |
| Q4 FY2024 | 12,606 | 44.7 | 1,500 | 0.99 | -2 | 0 | Q4 FY2024 release p. 1, 2 |
| Q1 FY2025 | 11,589 | 45.4 | 1,051 | 0.70 | -10 | -9 | Q1 FY2025 10-Q p. 1, 21; Q1 FY2025 release p. 1 |
| Q2 FY2025 | 12,354 | 43.6 | 1,163 | 0.78 | -8 | -9 | Q2 FY2025 10-Q p. 1, 24; Q2 FY2025 release p. 1 |
| Q3 FY2025 | 11,269 | 41.5 | 794 | 0.54 | -9 | -7 | Q3 FY2025 10-Q p. 1, 26; Q3 FY2025 release p. 1 |
| Q4 FY2025 | 11,097 | 40.3 | 211 | 0.14 | -12 | -11 | Q4 FY2025 release p. 1, 2 |
| Q1 FY2026 | 11,720 | 42.2 | 727 | 0.49 | 1 | -1 | Q1 FY2026 10-Q p. 1, 21; Q1 FY2026 release p. 1 |
| Q2 FY2026 | 12,427 | 40.6 | 792 | 0.53 | 1 | 0 | Q2 FY2026 10-Q p. 1, 27; Q2 FY2026 release p. 1 |
| Q3 FY2026 | 11,279 | 40.2 | 520 | 0.35 | 0 | -3 | Q3 FY2026 10-Q p. 1, 30; Q3 FY2026 release p. 1 |
| Q4 FY2026 | 10,972 | 49.2 | 1,069 | 0.72 | -1 | -4 | Q4 FY2026 release p. 1, 2 |
| Q1 FY2027 | 11,213 | 42.8 | 712 | 0.48 | -4 | -5 | Q1 FY2027 10-Q p. 1, 22; Q1 FY2027 release p. 1 |

### Quarterly segments and channels

| Period | North America | EMEA | Greater China | APLA | Converse | NIKE Direct | Wholesale | Source (filing, printed page) |
|---|---|---|---|---|---|---|---|---|
| Q1 FY2024 | 5,423 | 3,610 | 1,735 | 1,572 | 588 | 5,357 | 6,983 | Q1 FY2024 10-Q p. 19, 23 |
| Q2 FY2024 | 5,625 | 3,567 | 1,863 | 1,805 | 519 | 5,742 | 7,118 | Q2 FY2024 10-Q p. 21, 26 |
| Q3 FY2024 | 5,070 | 3,138 | 2,084 | 1,647 | 495 | 5,351 | 6,588 | Q3 FY2024 10-Q p. 22, 27 |
| Q4 FY2024 | 5,278 | 3,292 | 1,863 | 1,705 | 480 | 5 | 7 | Q4 FY2024 release p. 1, 4 |
| Q1 FY2025 | 4,826 | 3,143 | 1,666 | 1,462 | 501 | 4,687 | 6,410 | Q1 FY2025 10-Q p. 17, 21 |
| Q2 FY2025 | 5,179 | 3,303 | 1,711 | 1,744 | 429 | 5,017 | 6,920 | Q2 FY2025 10-Q p. 20, 24 |
| Q3 FY2025 | 4,864 | 2,811 | 1,733 | 1,470 | 405 | 4,723 | 6,155 | Q3 FY2025 10-Q p. 21, 27 |
| Q4 FY2025 | 4,703 | 3,000 | 1,476 | 1,575 | 357 | 4 | 6 | Q4 FY2025 release p. 1, 4 |
| Q1 FY2026 | 5,020 | 3,331 | 1,512 | 1,490 | 366 | 4,514 | 6,839 | Q1 FY2026 release p. 4; Q1 FY2026 10-Q p. 21 |
| Q2 FY2026 | 5,633 | 3,392 | 1,423 | 1,667 | 300 | 4,616 | 7,499 | Q2 FY2026 10-Q p. 25, 29 |
| Q3 FY2026 | 5,026 | 2,874 | 1,615 | 1,490 | 264 | 4,539 | 6,466 | Q3 FY2026 10-Q p. 28, 32 |
| Q4 FY2026 | 4,832 | 2,975 | 1,297 | 1,596 | 244 | 4 | 7 | Q4 FY2026 release p. 1, 4 |
| Q1 FY2027 | 5,127 | 3,176 | 1,180 | 1,463 | 263 | 4,142 | 6,804 | Q1 FY2027 10-Q p. 22, 25 |

Q4 NIKE Direct and wholesale appear in the Q4 releases only rounded to $ billions (for example 4.1 = $4.1 billion).

### Greater China growth by quarter (%)

| Period | Reported | Currency-neutral | Source (filing, printed page) |
|---|---|---|---|
| Q1 FY2023 | -16 | -13 | Q1 FY2023 release p. 4 |
| Q2 FY2023 | -3 | 6 | Q2 FY2023 release p. 4 |
| Q3 FY2023 | -8 | 1 | Q3 FY2023 release p. 4 |
| Q4 FY2023 | 16 | 25 | Q4 FY2023 release p. 4 |
| Q1 FY2024 | 5 | 12 | Q1 FY2024 10-Q p. 26 |
| Q2 FY2024 | 4 | 8 | Q2 FY2024 10-Q p. 30 |
| Q3 FY2024 | 5 | 6 | Q3 FY2024 10-Q p. 32 |
| Q4 FY2024 | 3 | 7 | Q4 FY2024 release p. 4 |
| Q1 FY2025 | -4 | -3 | Q1 FY2025 10-Q p. 24 |
| Q2 FY2025 | -8 | -11 | Q2 FY2025 10-Q p. 28 |
| Q3 FY2025 | -17 | -15 | Q3 FY2025 10-Q p. 31 |
| Q4 FY2025 | -21 | -20 | Q4 FY2025 release p. 4 |
| Q1 FY2026 | -9 | -10 | Q1 FY2026 10-Q p. 24 |
| Q2 FY2026 | -17 | -16 | Q2 FY2026 10-Q p. 29 |
| Q3 FY2026 | -7 | -10 | Q3 FY2026 10-Q p. 32 |
| Q4 FY2026 | -12 | -17 | Q4 FY2026 release p. 4 |
| Q1 FY2027 | -22 | -26 | Q1 FY2027 10-Q p. 25 |

### Quarter-end balances

| Period | Cash | ST investments | Inventories | Current LTD | Long-term debt | Equity | Source (filing, printed page) |
|---|---|---|---|---|---|---|---|
| 2023-08-31 | 6,178 | 2,612 | 8,698 | 0 | 8,929 | 13,971 | Q1 FY2024 10-Q p. 3; Q1 FY2024 release p. 3 |
| 2023-11-30 | 7,919 | 2,008 | 7,979 | 0 | 8,930 | 14,146 | Q2 FY2024 10-Q p. 3; Q2 FY2024 release p. 3 |
| 2024-02-29 | 8,960 | 1,613 | 7,726 | n/a | 8,930 | 14,226 | Q3 FY2024 10-Q p. 3 |
| 2024-05-31 | 9,860 | 1,722 | 7,519 | 1,000 | 7,903 | 14,430 | FY2024 10-K p. 59 |
| 2024-08-31 | 8,485 | 1,809 | 8,253 | 1,000 | 7,998 | 13,944 | Q1 FY2025 10-Q p. 3 |
| 2024-11-30 | 7,979 | 1,782 | 7,981 | 1,000 | 7,973 | 14,037 | Q2 FY2025 10-Q p. 3 |
| 2025-02-28 | 8,601 | 1,792 | 7,539 | 1,000 | 7,956 | 14,007 | Q3 FY2025 10-Q p. 3 |
| 2025-05-31 | 7,464 | 1,687 | 7,489 | 0 | 7,961 | 13,213 | FY2025 10-K p. 58; Q4 FY2025 release p. 3 |
| 2025-08-31 | 7,024 | 1,551 | 8,114 | 0 | 7,996 | 13,468 | Q1 FY2026 10-Q p. 3; Q1 FY2026 release p. 3 |
| 2025-11-30 | 6,974 | 1,371 | 7,726 | 999 | 7,016 | 14,085 | Q2 FY2026 10-Q p. 3 |
| 2026-02-28 | 6,660 | 1,397 | 7,487 | 999 | 7,030 | 14,090 | Q3 FY2026 10-Q p. 3 |
| 2026-05-31 | 7,563 | 1,464 | 7,501 | 2,000 | 5,942 | 14,865 | FY2026 10-K p. 57 |
| 2026-08-31 | 6,903 | 1,465 | 7,846 | 2,000 | 5,893 | 15,220 | Q1 FY2027 10-Q p. 3 |

## 6. Key disclosures quoted from the filings

| Topic | What the filing says | Source |
|---|---|---|
| IEEPA tariff recovery | Q4 FY2026 gross margin "increased 890 basis points to 49.2 percent ... The expected recovery of the IEEPA tariffs of $986 million increased gross margin by approximately 900 basis points." Q4 diluted EPS of $0.72 included "a $0.52 benefit related to the expected recovery of the IEEPA tariffs." $965M was booked in North America and $21M in Converse. | Q4 FY2026 release p. 1 and divisional revenues footnote; FY2026 10-K |
| IEEPA cash | FY2026 cash from operations "includes approximately $0.3 billion of cash received from IEEPA tariff recoveries." | Q4 FY2026 release p. 1 |
| FY2027 outlook | "Revenues are expected to decline high-single digits in fiscal 2027." Effective tax rate "expected to be in the mid-20 percent range." "Adjusted Diluted earnings per share is expected to be in the range of $1.15 to $1.35, which excludes approximately $0.15 of restructuring expenses related to Pace." | Q1 FY2027 release p. 1 |
| Pace program | "approximately $2.5 billion in cumulative savings through fiscal 2031, with approximately $1.0 billion of pre-tax charges, primarily consisting of employee-related costs, through fiscal 2031, in addition to approximately $0.3 billion of severance costs recognized in fiscal 2026." Includes "a new campus in India." Builds on "the previous cost realignment plan announced in March 2026." | Q1 FY2027 release p. 1; 8-K filed Oct 1, 2026 (Item 2.05) p. 2 |
| Geography change | "NIKE plans to organize into three geographies in fiscal 2028." | Q1 FY2027 10-Q |
| March 2026 plan | About $300M of pre-tax charges, primarily severance, substantially all in Q3 FY2026; no headcount stated. | 8-K filed Mar 5, 2026 (Item 2.05) p. 2 |
| FY2024 restructuring | $443M of restructuring charges in FY2024 ($392M severance); no savings target or headcount stated. | FY2024 10-K |
| FY2020 charges | $200M to $250M employee termination costs; $405M impairment on moving Brazil, Argentina, Chile and Uruguay to distributors. | FY2020 10-K |
| Q1 FY2027 margin | Gross margin rose 60 bps to 42.8%; lower warehousing and logistics costs added about 90 bps. | Q1 FY2027 10-Q p. 19 |
| Dividend | Quarterly dividend raised to $0.41 from $0.40 in Q2 FY2026; $0.41 declared in Q1 FY2027. | Q2 FY2026 10-Q; Q1 FY2027 10-Q p. 5 |
| Tariff cost estimate | "As a result of new tariffs, we expect a gross incremental cost of approximately $1.5 billion on an annualized basis." Not repeated in the Q3 FY2026 or Q1 FY2027 10-Qs. | Q1 FY2026 10-Q p. 19; Q2 FY2026 10-Q p. 23 |
| IEEPA before Q4 | As of April 1, 2026, "Total IEEPA tariffs paid ... is approximately $1.0 billion" and recovery was judged "not probable"; the receivable was collected in Q1 FY2027 (amount not stated in the 10-Q). | Q3 FY2026 10-Q p. 26; Q1 FY2027 10-Q |
| China and Converse outlook | "The actions related to Converse are expected to continue throughout fiscal 2027 and for Greater China to extend beyond fiscal 2027." | Q1 FY2027 10-Q p. 20 |
| Campion separation | "one-time cash compensation amount of $2,750,000 under a Separation and Release Agreement." | Q2 FY2024 10-Q p. 47 |
| Shares outstanding | 1,483,498,703 (281,387,752 Class A and 1,202,110,951 Class B) at July 8, 2026; 1,485,308,829 on the Q1 FY2027 10-Q cover. | FY2026 10-K cover; 2026 proxy p. 76; Q1 FY2027 10-Q cover |

## 7. Items checked against the full text of every filing

Confirmed in filings (previously unverified):
- Dec 2023 plan: Nike was "identifying opportunities to deliver up to $2 billion in cumulative cost savings over the next three years" and expected "pre-tax restructuring charges of approximately $400 million to $450 million primarily associated with employee severance" (8-K filed Dec 21, 2023, Item 2.05, p. 2; Q2 FY2024 10-Q p. 22).
- Tariffs: "we expect a gross incremental cost of approximately $1.5 billion on an annualized basis" (Q1 FY2026 10-Q p. 19; Q2 FY2026 10-Q p. 23).
- Geography change: Nike's "four Geographies" (Dec 2025 leadership announcement, 8-K Ex. 99.1 filed Dec 2, 2025) become "three geographies in fiscal 2028" (Q1 FY2027 10-Q; Oct 1, 2026 8-K).

Not in any filing (a text search of all 102 documents found nothing), so the report sources them to opened Nike, WARN or news pages or drops them:
- Layoff headcounts (Feb 2024 "more than 1,500", Jan 2026 "around 775", Apr 2026 "about 1,400"). Filings describe "a net reduction in the Company's global workforce" and the charges, never a count.
- The Q2 FY2027 "400 bps Cyber Week" headwind (likely from the earnings call; dropped).
- "Bengaluru" (filings say "a new campus in India"; Nike's Oct 1, 2026 employee memo names Bengaluru).
- Stock prices, index membership and analyst targets are market data, not filing data; see `data/nke_daily_prices.csv` (Yahoo Finance) and the report's labelling.

## 8. Filing URLs

- FY2019 Form 10-K (filed 2019-07-23): https://www.sec.gov/Archives/edgar/data/320187/000032018719000051/nke-531201910k.htm
- FY2020 Form 10-K (filed 2020-07-24): https://www.sec.gov/Archives/edgar/data/320187/000032018720000047/nke-531202010k.htm
- FY2021 Form 10-K (filed 2021-07-20): https://www.sec.gov/Archives/edgar/data/320187/000032018721000028/nke-20210531.htm
- FY2022 Form 10-K (filed 2022-07-21): https://www.sec.gov/Archives/edgar/data/320187/000032018722000038/nke-20220531.htm
- FY2023 Form 10-K (filed 2023-07-20): https://www.sec.gov/Archives/edgar/data/320187/000032018723000039/nke-20230531.htm
- Q4 FY2023 earnings release, 8-K Ex. 99.1 (filed 2023-06-29): https://www.sec.gov/Archives/edgar/data/320187/000032018723000026/q4fy23exhibit991er.htm
- FY2024 Form 10-K (filed 2024-07-25): https://www.sec.gov/Archives/edgar/data/320187/000032018724000044/nke-20240531.htm
- FY2025 Form 10-K (filed 2025-07-17): https://www.sec.gov/Archives/edgar/data/320187/000032018725000047/nke-20250531.htm
- Q4 FY2025 earnings release, 8-K Ex. 99.1 (filed 2025-06-26): https://www.sec.gov/Archives/edgar/data/320187/000032018725000034/q4fy25exhibit991er.htm
- FY2026 Form 10-K (filed 2026-07-15): https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm
- Q1 FY2024 Form 10-Q (filed 2023-10-06): https://www.sec.gov/Archives/edgar/data/320187/000032018723000052/nke-20230831.htm
- Q1 FY2024 earnings release, 8-K Ex. 99.1 (filed 2023-09-28): https://www.sec.gov/Archives/edgar/data/320187/000032018723000048/q1fy24exhibit991er.htm
- Q2 FY2024 Form 10-Q (filed 2024-01-05): https://www.sec.gov/Archives/edgar/data/320187/000032018724000004/nke-20231130.htm
- Q2 FY2024 earnings release, 8-K Ex. 99.1 (filed 2023-12-21): https://www.sec.gov/Archives/edgar/data/320187/000032018723000054/q2fy24exhibit991er.htm
- Q3 FY2024 Form 10-Q (filed 2024-04-04): https://www.sec.gov/Archives/edgar/data/320187/000032018724000019/nke-20240229.htm
- Q3 FY2024 earnings release, 8-K Ex. 99.1 (filed 2024-03-21): https://www.sec.gov/Archives/edgar/data/320187/000032018724000013/q3fy24exhibit991er.htm
- Q4 FY2024 earnings release, 8-K Ex. 99.1 (filed 2024-06-27): https://www.sec.gov/Archives/edgar/data/320187/000032018724000028/q4fy24exhibit991er.htm
- Q1 FY2025 Form 10-Q (filed 2024-10-07): https://www.sec.gov/Archives/edgar/data/320187/000032018724000065/nke-20240831.htm
- Q1 FY2025 earnings release, 8-K Ex. 99.1 (filed 2024-10-01): https://www.sec.gov/Archives/edgar/data/320187/000032018724000062/q1fy25exhibit991er.htm
- Q2 FY2025 Form 10-Q (filed 2025-01-03): https://www.sec.gov/Archives/edgar/data/320187/000032018725000004/nke-20241130.htm
- Q2 FY2025 earnings release, 8-K Ex. 99.1 (filed 2024-12-19): https://www.sec.gov/Archives/edgar/data/320187/000032018724000069/q2fy25exhibit991er.htm
- Q3 FY2025 Form 10-Q (filed 2025-04-03): https://www.sec.gov/Archives/edgar/data/320187/000032018725000016/nke-20250228.htm
- Q3 FY2025 earnings release, 8-K Ex. 99.1 (filed 2025-03-20): https://www.sec.gov/Archives/edgar/data/320187/000032018725000011/q3fy25exhibit991er.htm
- Q1 FY2026 Form 10-Q (filed 2025-10-01): https://www.sec.gov/Archives/edgar/data/320187/000032018725000097/nke-20250831.htm
- Q1 FY2026 earnings release, 8-K Ex. 99.1 (filed 2025-09-30): https://www.sec.gov/Archives/edgar/data/320187/000032018725000091/q1fy26exhibit991er.htm
- Q2 FY2026 Form 10-Q (filed 2025-12-30): https://www.sec.gov/Archives/edgar/data/320187/000032018725000151/nke-20251130.htm
- Q2 FY2026 earnings release, 8-K Ex. 99.1 (filed 2025-12-18): https://www.sec.gov/Archives/edgar/data/320187/000032018725000138/q2fy26exhibit991er.htm
- Q3 FY2026 Form 10-Q (filed 2026-04-01): https://www.sec.gov/Archives/edgar/data/320187/000032018726000037/nke-20260228.htm
- Q3 FY2026 earnings release, 8-K Ex. 99.1 (filed 2026-03-31): https://www.sec.gov/Archives/edgar/data/320187/000032018726000026/q3fy26exhibit991er.htm
- Q4 FY2026 earnings release, 8-K Ex. 99.1 (filed 2026-06-30): https://www.sec.gov/Archives/edgar/data/320187/000032018726000076/q4fy26exhibit991er.htm
- Q1 FY2027 Form 10-Q (filed 2026-10-02): https://www.sec.gov/Archives/edgar/data/320187/000032018726000193/nke-20260831.htm
- Q1 FY2027 earnings release, 8-K Ex. 99.1 (filed 2026-10-01): https://www.sec.gov/Archives/edgar/data/320187/000032018726000184/q1fy27exhibit991er.htm
- Q1 FY2023 earnings release, 8-K Ex. 99.1 (filed 2022-09-29): https://www.sec.gov/Archives/edgar/data/320187/000032018722000054/q1fy23exhibit991er.htm
- Q2 FY2023 earnings release, 8-K Ex. 99.1 (filed 2022-12-20): https://www.sec.gov/Archives/edgar/data/320187/000032018722000061/q2fy23exhibit991er.htm
- Q3 FY2023 earnings release, 8-K Ex. 99.1 (filed 2023-03-21): https://www.sec.gov/Archives/edgar/data/320187/000032018723000009/q3fy23exhibit991er.htm
