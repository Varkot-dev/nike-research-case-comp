# Nike financial data pack (as of 2026-10-12)

IMPORTANT LIMITS. WebFetch could not resolve sec.gov, nike.com, businesswire, q4cdn (DNS/proxy blocked), so NO filing was opened directly. All figures come from WebSearch result summaries that cited the sources listed, plus model memory where noted.
Status key:
- verified_search = figure stated in a search summary that cited the listed SEC/Nike URL (still re-check against the filing before publishing)
- secondary = third-party aggregator or news; sources conflicted or unconfirmed
- approximate_memory = from model memory, NOT verified this session; confirm in 10-K before use
- derived = computed from other figures
Blank = not found. USD millions unless noted. FY ends May 31.

## 1. Annual results
```csv
fiscal_year,revenue_usd_m,gross_margin_pct,diluted_eps,net_income_usd_m,status,source_url
FY2019,39117,44.7,2.49,4029,approximate_memory,https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000320187&type=10-K
FY2020,37403,43.4,1.62,2539,approximate_memory,same as above
FY2021,44538,44.8,3.56,5727,approximate_memory,same as above
FY2022,46710,46.0,3.75,6046,approximate_memory,same as above
FY2023,51217,43.5,3.23,5070,approximate_memory,same as above
FY2024,51362,44.6,3.73,5700,approximate_memory (GM 44.6 verified_search),https://www.sec.gov/Archives/edgar/data/320187/000032018725000047/nke-20250531.htm
FY2025,46309,42.7,2.16,3219,verified_search,https://www.sec.gov/Archives/edgar/data/320187/000032018725000047/nke-20250531.htm
FY2026,46398,42.9,2.10,3108,verified_search,https://www.sec.gov/Archives/edgar/data/0000320187/000130817926000376/nke015577-ars.pdf
```
Note: FY2026 Q4 includes about $986M expected IEEPA tariff recovery (about 900 bps of Q4 GM). A third-party summary says FY26 EPS ex-benefit is about $1.58 (unverified).

## 2. Quarterly results
```csv
quarter,period_end,revenue_usd_m,gross_margin_pct,diluted_eps,status,source_url
Q1 FY2024,2023-08-31,12939,44.2,0.94,approximate_memory,
Q2 FY2024,2023-11-30,13388,44.6,1.07,approximate_memory,
Q3 FY2024,2024-02-29,12429,44.8,0.99,approximate_memory,
Q4 FY2024,2024-05-31,12606,44.7,0.98,approximate_memory,
Q1 FY2025,2024-08-31,11589,44.7,0.70,approximate_memory,
Q2 FY2025,2024-11-30,12354,43.6,0.78,approximate_memory,
Q3 FY2025,2025-02-28,11269,41.5,0.54,verified_search (rev $11.3B),https://www.sec.gov/Archives/edgar/data/320187/000032018725000011/q3fy25exhibit991er.htm
Q4 FY2025,2025-05-31,11097,40.3,0.14,verified_search (rev $11.1B),https://www.sec.gov/Archives/edgar/data/320187/000032018725000034/q4fy25exhibit991er.htm
Q1 FY2026,2025-08-31,11700,42.2,0.49,verified_search (rev $11.7B rounded),https://www.sec.gov/Archives/edgar/data/0000320187/000130817926000376/nke015577-ars.pdf
Q2 FY2026,2025-11-30,12400,40.6,0.53,verified_search (rev $12.4B rounded),https://investors.nike.com/news-events/press-releases/detail/559/nike-inc-reports-fiscal-2026-second-quarter-results
Q3 FY2026,2026-02-28,11300,40.2,0.35,verified_search (rev $11.3B rounded),https://www.sec.gov/Archives/edgar/data/320187/000032018726000026/q3fy26exhibit991er.htm
Q4 FY2026,2026-05-31,10970,49.2,0.72,verified_search (net income about 1.07B),https://www.sec.gov/Archives/edgar/data/0000320187/000032018726000076/q4fy26exhibit991er.htm
Q1 FY2027,2026-08-31,11210,42.8,0.48,verified_search (net income 712M),https://www.stocktitan.net/sec-filings/NKE/10-q-nike-inc-quarterly-earnings-report-4dd57181e629.html
```
Q1 FY27 reported revenue -4% (-5% currency neutral), GM +60 bps. FY26 quarterly EPS sums to 2.09 vs reported 2.10 (rounding).

## 3. Revenue by geography, channel, Converse
```csv
period,north_america,emea,greater_china,apla,converse,nike_direct,wholesale,status,source_url
FY2023,21608,13418,7248,6431,2427,,,approximate_memory,
FY2024,21369,13695,7547,6543,2082,~21500,~27400,approximate_memory,
FY2025,19572,12257,6586,6251,1692,18800,,verified_search (geo + Converse via SEC XBRL; Direct $18.8B),https://www.sec.gov/Archives/edgar/data/320187/000032018725000047/nke-20250531.htm
FY2026,~20500,~12600,~5850,~6200,~1200,17700,,secondary (aggregators; Direct $17.7B from release),https://www.statista.com/statistics/241692/nikes-sales-by-region-since-2007/
Q4 FY2026,4830,,1300,,244,4100,6600,secondary (GC decline cited as -12% and -17% by different sources),https://www.cnbc.com/2026/06/30/nike-nke-q4-2026-earnings.html
Q1 FY2027,~5100,~3200,~1200,~1500,263,4100,6800,secondary (NA +2%, EMEA -5%, GC -22% reported/-26% CN, APLA flat vs -2% conflict; Converse -28%; Direct -8%; Wholesale -1%),https://vanderbiltreport.com/nike-q1-fiscal-2027-earnings/
```
Other: NIKE Brand revenue FY26 $45.2B vs $44.7B FY25. Q1 FY27 Pace plan: reorganize into 3 geographies, about $2.5B savings (secondary, WWD / Benzinga transcript).

## 4. Stock price (NKE, USD)
```csv
item,date,price,status,source_url
All-time high (intraday),2021-11-05,179.10,secondary (StockScan; close was roughly 175, not verified),https://stockscan.io/stocks/NKE/price-history
All-time high close, dividend-adjusted,2021-11-05,161.91,secondary (Macrotrends adjusted basis; not comparable to raw),https://www.macrotrends.net/stocks/charts/NKE/nike/stock-price-history
Year-end close,2019-12-31,101.31,approximate_memory,
Year-end close,2020-12-31,141.47,approximate_memory,
Year-end close,2021-12-31,166.66,approximate_memory,
Year-end close,2022-12-30,117.01,approximate_memory (StockScan page also shows 117.01),https://stockscan.io/stocks/NKE/price-history
Year-end close,2023-12-29,108.57,approximate_memory,
Year-end close,2024-12-31,75.67,approximate_memory,
Year-end close,2025-12-31,~63.6,derived (34.36 on 2026-10-07 stated as -46% YTD),https://www.bloomberglinea.com/quote/nke:UN/
Recent close,2026-10-02,33.10,secondary,https://stockanalysis.com/stocks/nke/history/
Recent close,2026-10-07,~34.36,secondary,https://www.bloomberglinea.com/quote/nke:UN/
Recent close,2026-10-09,34.71,secondary (Macrotrends; 2026-10-11 was a Sunday so last close is 10-09),https://www.macrotrends.net/stocks/charts/NKE/nike/stock-price-history
52-week low (as of 2026-10-07),,31.98,secondary,https://www.bloomberglinea.com/quote/nke:UN/
```

## 5. Dividends, shares, inventory, cash, debt
```csv
item,period,value,status,source_url
Quarterly dividend per share,Nov 2025 raise,0.40 to 0.41 (24th straight yearly increase),secondary,https://finance.yahoo.com/markets/stocks/articles/nike-inc-declares-0-41-210000583.html
Quarterly dividend declared,payable 2026-10-01,0.41,verified_search,https://www.marketscreener.com/news/nike-inc-declares-quarterly-cash-dividend-payable-on-october-1-2026-ce7f50d2dd8fff25
Annual dividends per share,FY2019,0.86,approximate_memory,
Annual dividends per share,FY2020,0.98,approximate_memory,
Annual dividends per share,FY2021,1.10,approximate_memory,
Annual dividends per share,FY2022,1.22,approximate_memory,
Annual dividends per share,FY2023,,not found,
Annual dividends per share,FY2024,,not found,
Annual dividends per share,FY2025,,not found,
Annual dividends per share,FY2026,~1.62,derived (0.40+0.40+0.41+0.41, assumes Nov 2025 raise timing),
Dividends paid total,FY2026,~2400 (returned about 2500 incl buybacks),verified_search,https://about.nike.com/newsroom/releases/nike-inc-reports-fiscal-2026-fourth-quarter-and-full-year-results
Shares outstanding,latest,,not found (roughly 1.48B in 2025 per memory; unverified),
Inventories,2026-05-31,~7500,secondary,https://www.sec.gov/Archives/edgar/data/0000320187/000032018726000088/nke-20260531.htm
Inventories,2026-08-31,~7800 (-3% YoY; +5% vs 2026-05-31),verified_search,https://www.sec.gov/Archives/edgar/data/0000320187/000032018726000193/nke-20260831.htm
Cash and equivalents,2026-08-31,6903,verified_search,https://www.marketscreener.com/news/nike-q1fy27-financial-schedules-key-financial-metrics-ce785ddadb80f123
Short-term investments,2026-08-31,1465,verified_search,same as above
Long-term debt (non-current),2026-08-31,5893,verified_search,same as above
Current portion of long-term debt,2026-08-31,2000,verified_search,same as above
Notes payable,2026-08-31,,not found,
Shareholders equity,2026-08-31,15220,verified_search,same as above
Cash plus short-term investments,2026-05-31,9000,verified_search,https://about.nike.com/newsroom/releases/nike-inc-reports-fiscal-2026-fourth-quarter-and-full-year-results
```
