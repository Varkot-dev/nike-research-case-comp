# Q_VALUATION: what the market expects for Nike (NKE)

Prepared 2026-10-13. Reference price $35.35 (NKE close 2026-10-12). Shares 1,485,308,829 (Q1 FY2027 10-Q cover). Cash plus short-term investments $8,368M and financial debt $7,893M at 2026-08-31 (PitchBook quarterly export: Total Debt 11,072M less capital/operating lease obligations 3,179M = 7,893M, matches). Nike FY ends May 31; FY2027 = June 2026 to May 2027.

All downloaded data treated as untrusted data. Raw files: `scratchpad/valuation/dl/`. Scripts: `scratchpad/valuation/scripts/`.

Source keys used below:
- YQS = https://query2.finance.yahoo.com/v10/finance/quoteSummary/NKE?modules=earningsTrend,financialData,defaultKeyStatistics,recommendationTrend,calendarEvents,upgradeDowngradeHistory,summaryDetail,price,earningsHistory,majorHoldersBreakdown (fetched 2026-10-13 ~19:07 UTC, file dl/qs_NKE.json)
- YOPT = https://query2.finance.yahoo.com/v7/finance/options/NKE (date=1797552000 for 2026-12-18, date=1813190400 for 2027-06-17; fetched 2026-10-13)
- YCH = https://query1.finance.yahoo.com/v8/finance/chart/NKE?period1=1420070400&period2=1791936000&interval=1d&events=div,split (fetched 2026-10-13; close is split-adjusted, not dividend-adjusted)
- NDQ = https://api.nasdaq.com/api/analyst/NKE/earnings-forecast (fetched 2026-10-13; Zacks-sourced, asOf field null)
- SA = https://stockanalysis.com/stocks/nke/forecast/ (WebFetch 2026-10-13; page says forecast data updated Oct 13, 2026; FY2028+ behind paywall)
- MB = https://www.marketbeat.com/stocks/NYSE/NKE/forecast/ (WebFetch 2026-10-13; dateModified 2026-10-09)
- PBA = local PitchBook export scratchpad/pb/b.xlsx (annual, downloaded 13-Oct-2026); PBQ = scratchpad/pb/a.xlsx (quarterly, downloaded 13-Oct-2026)
- Peers: https://query2.finance.yahoo.com/v10/finance/quoteSummary/{TICKER}?modules=financialData,defaultKeyStatistics,summaryDetail,earningsTrend,price (fetched 2026-10-13); FX from https://query1.finance.yahoo.com/v8/finance/chart/{PAIR}?range=5d&interval=1d; 10y Treasury from https://query1.finance.yahoo.com/v8/finance/chart/%5ETNX?range=5d&interval=1d

## (A) Data points (CSV)

```csv
item,period,value,unit,source,url,as_of
NKE close,2026-10-12,35.35,USD,Yahoo chart,YCH,2026-10-12
NKE intraday price,2026-10-13,35.615,USD,Yahoo quoteSummary price,YQS,2026-10-13 19:07 UTC
Consensus EPS mean,FY2027,1.28806,USD,Yahoo earningsTrend 0y,YQS,2026-10-13
Consensus EPS low,FY2027,1.01,USD,Yahoo earningsTrend 0y,YQS,2026-10-13
Consensus EPS high,FY2027,1.69,USD,Yahoo earningsTrend 0y,YQS,2026-10-13
Consensus EPS analysts,FY2027,35,count,Yahoo earningsTrend 0y,YQS,2026-10-13
Consensus EPS mean 7 days ago,FY2027,1.35606,USD,Yahoo epsTrend,YQS,2026-10-13
Consensus EPS mean 30 days ago,FY2027,1.7122,USD,Yahoo epsTrend,YQS,2026-10-13
Consensus EPS mean 60 days ago,FY2027,1.72383,USD,Yahoo epsTrend,YQS,2026-10-13
Consensus EPS mean 90 days ago,FY2027,1.73093,USD,Yahoo epsTrend,YQS,2026-10-13
EPS revisions up last 30 days,FY2027,1,count,Yahoo epsRevisions,YQS,2026-10-13
EPS revisions down last 30 days,FY2027,12,count,Yahoo epsRevisions,YQS,2026-10-13
EPS revisions down last 7 days,FY2027,24,count,Yahoo epsRevisions (exceeds 30-day count as published),YQS,2026-10-13
Consensus revenue mean,FY2027,43151.56,USD m,Yahoo earningsTrend 0y,YQS,2026-10-13
Consensus revenue low,FY2027,42133.43,USD m,Yahoo earningsTrend 0y,YQS,2026-10-13
Consensus revenue high,FY2027,45712.00,USD m,Yahoo earningsTrend 0y,YQS,2026-10-13
Consensus revenue analysts,FY2027,39,count,Yahoo earningsTrend 0y,YQS,2026-10-13
Consensus revenue growth,FY2027,-7.0,% y/y,Yahoo earningsTrend 0y (vs FY2026 46398),YQS,2026-10-13
Consensus EPS mean,FY2028,1.64603,USD,Yahoo earningsTrend +1y,YQS,2026-10-13
Consensus EPS low,FY2028,1.10,USD,Yahoo earningsTrend +1y,YQS,2026-10-13
Consensus EPS high,FY2028,3.22,USD,Yahoo earningsTrend +1y,YQS,2026-10-13
Consensus EPS analysts,FY2028,39,count,Yahoo earningsTrend +1y,YQS,2026-10-13
Consensus EPS mean 30 days ago,FY2028,2.22078,USD,Yahoo epsTrend,YQS,2026-10-13
Consensus EPS mean 90 days ago,FY2028,2.26662,USD,Yahoo epsTrend,YQS,2026-10-13
EPS revisions down last 30 days,FY2028,23,count,Yahoo epsRevisions,YQS,2026-10-13
EPS revisions up last 30 days,FY2028,0,count,Yahoo epsRevisions,YQS,2026-10-13
Consensus revenue mean,FY2028,43645.04,USD m,Yahoo earningsTrend +1y,YQS,2026-10-13
Consensus revenue low,FY2028,40341.78,USD m,Yahoo earningsTrend +1y,YQS,2026-10-13
Consensus revenue high,FY2028,48103.00,USD m,Yahoo earningsTrend +1y,YQS,2026-10-13
Consensus revenue analysts,FY2028,40,count,Yahoo earningsTrend +1y,YQS,2026-10-13
Consensus revenue growth,FY2028,1.1,% y/y,Yahoo earningsTrend +1y,YQS,2026-10-13
Consensus EPS mean Q2 FY27,quarter to 2026-11-30,0.38074,USD,Yahoo earningsTrend 0q (26 analysts; 30 days ago 0.52265),YQS,2026-10-13
Consensus revenue mean Q2 FY27,quarter to 2026-11-30,11176.23,USD m,Yahoo earningsTrend 0q (28 analysts; -10.1% y/y),YQS,2026-10-13
Consensus EPS mean Q3 FY27,quarter to 2027-02-28,0.26497,USD,Yahoo earningsTrend +1q (26 analysts),YQS,2026-10-13
Next earnings date (estimated),Q2 FY27,2026-12-17,date,Yahoo calendarEvents (isEarningsDateEstimate true),YQS,2026-10-13
Consensus EPS mean,FY2027,1.26,USD,Nasdaq/Zacks yearly (11 est; high 1.69 low 1.13; 10 down 0 up in 4 wks),NDQ,2026-10-13
Consensus EPS mean,FY2028,1.78,USD,Nasdaq/Zacks yearly (14 est; high 3.22 low 1.23; 10 down),NDQ,2026-10-13
Consensus EPS mean,FY2029,2.31,USD,Nasdaq/Zacks yearly (6 est; high 3.86 low 1.61),NDQ,2026-10-13
Consensus EPS mean,FY2030,4.51,USD,Nasdaq/Zacks yearly (1 est; not meaningful),NDQ,2026-10-13
Consensus EPS mean,FY2027,1.32,USD,StockAnalysis (low 1.01 high 1.69),SA,2026-10-13
Consensus revenue mean,FY2027,43200,USD m,StockAnalysis (low 42100 high 45700; 39 analysts),SA,2026-10-13
Company guidance adjusted EPS low,FY2027,1.15,USD,Nike guidance (excludes about 0.15 Pace restructuring),task brief,2026-10-01
Company guidance adjusted EPS high,FY2027,1.35,USD,Nike guidance,task brief,2026-10-01
Company guidance revenue,FY2027,down high-single digits,text,Nike guidance,task brief,2026-10-01
MarketBeat cited pre-guidance consensus EPS,FY2027,1.66,USD,MarketBeat text (stale),MB,2026-10-09
Analyst price target mean,12m,38.04167,USD,Yahoo financialData (36 opinions),YQS,2026-10-13
Analyst price target median,12m,34.40,USD,Yahoo financialData,YQS,2026-10-13
Analyst price target high,12m,94.00,USD,Yahoo financialData,YQS,2026-10-13
Analyst price target low,12m,19.00,USD,Yahoo financialData,YQS,2026-10-13
Analyst price target mean,12m,41.07,USD,MarketBeat (39 ratings; high 75 low 19),MB,2026-10-09
Recommendation mean,current,2.81,1=strong buy 5=strong sell,Yahoo financialData (key hold),YQS,2026-10-13
Ratings strong buy/buy/hold/sell/strong sell,0m,1/9/25/4/3,count,Yahoo recommendationTrend,YQS,2026-10-13
Ratings strong buy/buy/hold/sell/strong sell,-3m,1/11/25/1/1,count,Yahoo recommendationTrend,YQS,2026-10-13
Ratings strong buy/buy/hold/sell/strong sell,Oct 2026,9/1/25/3/4,count,StockAnalysis (S&P Global; looks transposed vs Yahoo),SA,2026-10-13
Ratings sell/hold/buy/strong buy,current,10/21/7/1,count,MarketBeat consensus Reduce,MB,2026-10-09
Price target changes after Q1 FY27 print,2026-10-02 to 2026-10-05,19 of 21 lowered,count,Yahoo upgradeDowngradeHistory,YQS,2026-10-13
Shares short,2026-09-30,99243778,shares,Yahoo defaultKeyStatistics,YQS,2026-10-13
Shares short prior month,2026-08-31,75594334,shares,Yahoo defaultKeyStatistics,YQS,2026-10-13
Short interest % of shares outstanding,2026-09-30,6.68,%,Yahoo sharesPercentSharesOut,YQS,2026-10-13
Short interest % of float,2026-09-30,10.38,%,Yahoo shortPercentOfFloat (float 1178.5m appears Class B basis),YQS,2026-10-13
Days to cover,2026-09-30,3.03,days,Yahoo shortRatio,YQS,2026-10-13
Institutional ownership % of shares,current,82.74,%,Yahoo majorHoldersBreakdown,YQS,2026-10-13
Institutional ownership % of float,current,84.39,%,Yahoo majorHoldersBreakdown,YQS,2026-10-13
Institutions count,current,2388,count,Yahoo majorHoldersBreakdown,YQS,2026-10-13
Insider ownership,current,1.95,%,Yahoo majorHoldersBreakdown,YQS,2026-10-13
Beta,current,1.099,x,Yahoo defaultKeyStatistics,YQS,2026-10-13
Implied vol ATM 35 call,exp 2026-12-18,38.7,%,Yahoo options (spans Dec 17 earnings),YOPT,2026-10-13
Implied vol ATM 35 put,exp 2026-12-18,40.8,%,Yahoo options,YOPT,2026-10-13
ATM 35 straddle mid,exp 2026-12-18,4.72,USD (13.3% of 35.35),Yahoo options bid/ask mids,YOPT,2026-10-13
Implied vol ATM 35 call,exp 2027-06-17,40.5,%,Yahoo options,YOPT,2026-10-13
Implied vol ATM 35 put,exp 2027-06-17,38.6,%,Yahoo options,YOPT,2026-10-13
Implied vol ATM 35 call,exp 2026-10-16,32.8,%,Yahoo options,YOPT,2026-10-13
Dividend rate,annual,1.64,USD (yield 4.64%),Yahoo summaryDetail,YQS,2026-10-13
52-week low/high,to 2026-10-13,31.97/70.44,USD,Yahoo summaryDetail,YQS,2026-10-13
52-week change,to 2026-10-13,-47.7,%,Yahoo defaultKeyStatistics (S&P 500 +17.5%),YQS,2026-10-13
10y US Treasury yield,2026-10-12,5.24,%,Yahoo ^TNX chart,https://query1.finance.yahoo.com/v8/finance/chart/%5ETNX?range=5d&interval=1d,2026-10-12
Market cap at 35.35,2026-10-12,52506,USD m,computed 35.35 x 1485308829,10-Q cover + YCH,2026-10-12
Enterprise value ex leases,2026-10-12,52031,USD m,computed 52506 + 7893 - 8368,PBQ + task brief,2026-08-31 BS
Enterprise value incl leases (Yahoo debt basis),2026-10-12,55263,USD m,computed 52506 + 11125 - 8368,YQS,2026-10-13
Revenue TTM,Q2 FY26 to Q1 FY27,45891,USD m,PitchBook quarterly sum,PBQ,2026-08-31
EBITDA TTM,Q2 FY26 to Q1 FY27,4654,USD m,PitchBook quarterly sum,PBQ,2026-08-31
EBIT (operating profit) TTM,Q2 FY26 to Q1 FY27,3758,USD m,PitchBook quarterly sum (8.2% margin),PBQ,2026-08-31
Diluted EPS TTM,Q2 FY26 to Q1 FY27,2.08,USD,PitchBook quarterly sum (Yahoo trailingEps 2.08),PBQ,2026-08-31
Trailing P/E,today,17.0,x,computed 35.35 / 2.08,PBQ + YCH,2026-10-12
Forward P/E FY2027,today,27.4,x,computed 35.35 / 1.288,YQS,2026-10-13
Forward P/E FY2028,today,21.5,x,computed 35.35 / 1.646,YQS,2026-10-13
Forward P/E FY2029,today,15.3,x,computed 35.35 / 2.31,NDQ,2026-10-13
P/E on FY2027 guidance midpoint 1.25,today,28.3,x,computed,task brief,2026-10-12
EV/Sales TTM,today,1.13,x,computed ex leases,PBQ,2026-10-12
EV/EBITDA TTM,today,11.2,x,computed ex leases,PBQ,2026-10-12
EV/Sales 10y mean,FY2017-FY2026,3.06,x,computed,PBA + YCH,2026-05-29
EV/EBITDA 10y mean,FY2017-FY2026,22.3,x,computed,PBA + YCH,2026-05-29
Trailing P/E (GAAP) 10y median,FY2017-FY2026,31.4,x,computed (mean 35.3 distorted by FY18 tax and FY20 Covid),PBA + YCH,2026-05-29
Forward P/E 10y mean,FY2017-FY2026,33.1,x,computed (perfect-foresight proxy),PBA + YCH,2026-05-29
EBIT margin 10y mean,FY2017-FY2026,11.8,%,computed PitchBook EBIT / revenue,PBA,2026-05-31
Revenue,FY2026,46398,USD m,PitchBook annual,PBA,2026-05-31
EBIT,FY2026,3850,USD m,PitchBook annual (8.3%),PBA,2026-05-31
Diluted EPS GAAP,FY2026,2.10,USD,PitchBook annual,PBA,2026-05-31
EPS analyst-normalized,FY2026,1.57,USD,PitchBook annual (vs GAAP 2.10),PBA,2026-05-31
Implied consensus EBIT margin,FY2027,5.7,%,derived from EPS 1.288 x 1487m sh / (1-22.5% tax),YQS,2026-10-13
Implied consensus EBIT margin,FY2028,7.2,%,derived from EPS 1.646,YQS,2026-10-13
Reverse DCF implied steady-state EBIT margin (base: WACC 10% g 2.5% rev CAGR 3%),FY2031+,13.8,%,computed (avg of g 2% 14.1 and g 3% 13.4),reverse_dcf.csv,2026-10-12
```

## (B) Tables

### B1. Consensus estimates (as of 2026-10-13)

| Metric | FY2027 (May-27) | FY2028 (May-28) | FY2029 (May-29) |
|---|---|---|---|
| EPS mean, Yahoo | 1.288 (35 analysts; 1.01 to 1.69) | 1.646 (39; 1.10 to 3.22) | n/a |
| EPS mean, Nasdaq/Zacks | 1.26 (11; 1.13 to 1.69) | 1.78 (14; 1.23 to 3.22) | 2.31 (6; 1.61 to 3.86) |
| EPS mean, StockAnalysis | 1.32 (1.01 to 1.69) | paywalled | paywalled |
| Company guidance (adj.) | 1.15 to 1.35 (mid 1.25), excl. about 0.15 Pace restructuring | none | none |
| EPS growth y/y (Yahoo vs 2.10 FY26 GAAP) | -38.7% | +27.8% | +40% (Zacks vs Yahoo FY28) |
| Revenue mean, Yahoo ($m) | 43,152 (39; 42,133 to 45,712) | 43,645 (40; 40,342 to 48,103) | n/a |
| Revenue growth y/y | -7.0% (guide: down high-single digits) | +1.1% | n/a |
| Revenue, StockAnalysis ($m) | 43,200 (42,100 to 45,700) | paywalled | paywalled |

Revisions (Yahoo epsTrend): FY2027 EPS fell from 1.731 (90 days ago) and 1.712 (30 days ago) to 1.356 (7 days ago) and 1.288 now, a 25% cut, almost all after the Q1 FY27 report and guidance (call 2026-10-01). FY2028 fell 26% from 2.221 to 1.646 in 30 days (23 down, 0 up). Q2 FY27 EPS fell from 0.523 to 0.381. After the print, 19 of the 21 broker actions dated 2026-10-02 to 2026-10-05 cut targets (for example JPM 40 to 33 UW, GS 38 to 30 N, BofA 30 to 24 U/P, MS 31 to 27 UW, BNP 23 to 19 U/P, Guggenheim 60 to 50 Buy, Barclays 48 to 37 OW). Downgrades over the prior 10 weeks: JPM to UW (08-04), Truist to Hold (08-26), Baird to Neutral (09-14), BofA to U/P (09-25); BMO initiated U/P (09-09). Sell plus strong sell counts rose from 2 to 7 over three months (Yahoo recommendationTrend).

Discrepancies between sources:
- FY2027 EPS: Yahoo 1.288, Zacks 1.26, StockAnalysis 1.32; MarketBeat still quotes a 1.66 consensus (pre-guidance, stale). Consensus now sits slightly above the 1.25 guidance midpoint.
- FY2028 EPS: Yahoo 1.646 vs Zacks 1.78. Zacks has fewer estimates (14) and may not have updated fully.
- Yahoo `forwardEps` is 1.69088, which does not match its own FY2028 mean (1.646); Yahoo's displayed forward P/E of 21.06 uses that figure and the intraday price.
- Ratings: Yahoo 1 strong buy and 9 buy; StockAnalysis (S&P Global) shows 9 strong buy and 1 buy for the same 42 analysts, which looks transposed. MarketBeat (39) shows 10 sell, 21 hold, 8 buy ("Reduce").
- Price target mean: Yahoo/S&P 38.04 (median 34.40, high 94 is probably a stale target) vs MarketBeat 41.07 (high 75).
- Yahoo `sharesOutstanding` 1,203.9m is Class B only; `impliedSharesOutstanding` 1,485.3m matches the 10-Q cover. Short % of float (10.38%) uses a 1,178m float, so it overstates short interest against the total share count (6.68%).
- Yahoo totalDebt 11,125m includes operating leases (PitchBook 11,072m incl. leases; 7,893m excl.). Yahoo TTM EBITDA 4,893m vs PitchBook quarterly sum 4,654m.

### B2. NKE valuation history (fiscal year ends, May 31)

Method: price = last Yahoo close on or before May 31. Market cap uses period-end shares outstanding (PitchBook TSO). EV = market cap + financial debt (PitchBook Total Debt less lease obligations) less cash and short-term investments. EBITDA and EBIT are PitchBook unadjusted. Trailing P/E uses GAAP diluted EPS; "norm." uses PitchBook analyst-normalized EPS. Forward P/E is a perfect-foresight proxy: price divided by the next FY's actual normalized EPS (historical consensus was not available). It therefore reads high in years before an earnings fall (FY2019, FY2024, FY2025). For FY2026 end it uses the FY2027 consensus 90 days before 2026-10-13 (1.731, around mid-July 2026). Today: TTM to Q1 FY27, EV ex leases, forward = FY2027 Yahoo consensus 1.288. CSV: `valuation/nke_multiples_history.csv`.

| Period | Price date | Price | EV ($m) | Trailing P/E (GAAP) | Trailing P/E (norm.) | Fwd P/E | EV/Sales | EV/EBITDA | EBIT margin |
|---|---|---|---|---|---|---|---|---|---|
| FY2016 end | 2016-05-31 | 55.22 | 89,461 | 25.6 | 25.6 | 23.1 | 2.76 | 16.9 | 14.3% |
| FY2017 end | 2017-05-31 | 52.99 | 84,686 | 21.1 | 22.2 | 22.1 | 2.47 | 15.0 | 14.4% |
| FY2018 end | 2018-05-31 | 71.80 | 113,517 | 61.4 | 29.9 | 28.8 | 3.12 | 22.0 | 12.0% |
| FY2019 end | 2019-05-31 | 77.14 | 119,772 | 31.0 | 31.0 | 42.2 | 3.06 | 21.5 | 12.4% |
| FY2020 end | 2020-05-29 | 98.58 | 154,165 | 61.6 | 53.9 | 27.7 | 4.12 | 37.6 | 8.0% |
| FY2021 end | 2021-05-28 | 136.46 | 211,273 | 38.3 | 38.3 | 36.3 | 4.74 | 27.4 | 15.5% |
| FY2022 end | 2022-05-31 | 118.85 | 183,146 | 31.7 | 31.6 | 36.8 | 3.92 | 23.8 | 14.7% |
| FY2023 end | 2023-05-31 | 105.26 | 159,516 | 32.6 | 32.6 | 26.6 | 3.11 | 22.6 | 12.1% |
| FY2024 end | 2024-05-31 | 95.05 | 140,187 | 25.5 | 24.0 | 45.3 | 2.73 | 19.0 | 12.7% |
| FY2025 end | 2025-05-30 | 60.59 | 88,240 | 28.1 | 28.9 | 38.6 | 1.91 | 19.2 | 8.2% |
| FY2026 end | 2026-05-29 | 46.23 | 67,376 | 22.0 | 29.4 | 26.7 | 1.45 | 14.5 | 8.3% |
| Today (TTM to Q1 FY27) | 2026-10-12 | 35.35 | 52,031 | 17.0 | n/a | 27.4 (FY28: 21.5) | 1.13 | 11.2 | 8.2% |

| Summary, FY2017 to FY2026 (10 FY ends) | Mean | Median | Min | Max | Today |
|---|---|---|---|---|---|
| Trailing P/E (GAAP) | 35.3 | 31.4 | 21.1 (FY17) | 61.6 (FY20) | 17.0 |
| Trailing P/E (normalized) | 32.2 | 30.5 | 22.2 (FY17) | 53.9 (FY20) | n/a |
| Forward P/E (proxy) | 33.1 | 32.6 | 22.1 (FY17) | 45.3 (FY24) | 27.4 FY27 / 21.5 FY28 |
| EV/Sales | 3.06 | 3.08 | 1.45 (FY26) | 4.74 (FY21) | 1.13 |
| EV/EBITDA | 22.3 | 21.8 | 14.5 (FY26) | 37.6 (FY20) | 11.2 |
| EBIT margin | 11.8% | 12.3% | 8.0% (FY20) | 15.5% (FY21) | 8.2% |

Including FY2016 (11 FY ends): EV/Sales mean 3.04 (range 1.45 to 4.74), EV/EBITDA mean 21.8 (14.5 to 37.6), trailing GAAP P/E mean 34.4 (21.1 to 61.6), forward proxy mean 32.2 (22.1 to 45.3). Today NKE trades at its lowest EV/Sales and EV/EBITDA in the series: about 37% of its 10-year average EV/Sales and about 50% of its average EV/EBITDA. The P/E on depressed FY2027 earnings (27.4x) is below the 10-year forward proxy average (33.1x) but not far from it. In other words, the market is valuing the franchise at low multiples of sales and EBITDA, while near-term earnings are cyclically or structurally depressed.

### B3. Peer multiples (prices = 2026-10-12 close; consensus as of 2026-10-13)

Method: all rows use Yahoo data on the same basis. EV = price x implied shares (converted into reporting currency) + Yahoo totalDebt (generally includes leases) less totalCash. EV/EBITDA and EV/Sales use Yahoo TTM EBITDA and revenue. P/E FY1 and FY2 = price / Yahoo consensus EPS for the current and next fiscal year. NTM blends FY1 and FY2 by the fraction of FY1 remaining. FX at 2026-10-13: HKD to CNY 0.8527 (Anta), CHF to USD 1.20119 (On, priced in USD, reports in CHF). Yahoo's own EV/EBITDA, EV/Sales and forward P/E for On and Anta mix currencies, so they were recomputed. NKE here is on the Yahoo (lease-inclusive) basis, so EV/EBITDA is 11.3 vs 11.2 in B2. Skechers is not listed (taken private by 3G Capital in 2025; Yahoo SKX returns 404). Puma shows no market cap on Yahoo, so its shares were implied from EV less debt plus cash. ASICS FY1 revenue growth is omitted because Yahoo's year-ago revenue figure for it is corrupt. CSV: `valuation/peer_multiples.csv`.

| Ticker | Company | Price | P/E FY1 | P/E FY2 | P/E NTM | EV/EBITDA TTM | EV/Sales TTM | Rev growth last qtr y/y | Rev growth FY1 | Rev growth FY2 | EBITDA margin TTM | FY1 end | Analysts FY1 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NKE | Nike | 35.35 USD | 27.4 | 21.5 | 24.9 | 11.3 | 1.20 | -4.3% | -7.0% | 1.1% | 10.7% | 2027-05-31 | 35 |
| ADS.DE | adidas | 149.60 EUR | 16.4 | 12.9 | 13.5 | 11.5 | 1.18 | 13.3% | 9.3% | 6.5% | 10.2% | 2026-12-31 | 25 |
| PUM.DE | Puma | 23.18 EUR | NM | 87.2 | NM | NM | 0.81 | -9.7% | -5.3% | 5.3% | -0.2% | 2026-12-31 | 15 |
| DECK | Deckers | 84.27 USD | 11.2 | 10.1 | 10.6 | 7.8 | 1.87 | 5.7% | 7.5% | 7.3% | 24.0% | 2027-03-31 | 22 |
| ONON | On Holding | 35.35 USD | 20.6 | 17.2 | 17.9 | 18.7 | 2.84 | 13.5% | 16.6% | 19.0% | 15.2% | 2026-12-31 | 23 |
| LULU | Lululemon | 94.66 USD | 9.8 | 11.0 | 10.6 | 4.9 | 1.06 | -4.3% | -5.8% | -1.2% | 21.5% | 2027-01-31 | 23 |
| UAA | Under Armour (A) | 4.93 USD | 45.5 | 25.5 | 32.0 | 17.9 | 0.63 | -3.2% | -4.8% | 2.2% | 3.5% | 2027-03-31 | 25 |
| 7936.T | ASICS | 4,474 JPY | 24.7 | 21.3 | 22.0 | 14.7 | 3.32 | 35.9% | n/a | 11.3% | 22.5% | 2026-12-31 | 13 |
| 2020.HK | Anta Sports | 71.10 HKD | 11.7 | 10.7 | 10.9 | 6.9 | 1.82 | 12.9% | 10.0% | 8.7% | 26.2% | 2026-12-31 | 22 |
| VFC | VF Corp | 15.79 USD | 14.5 | 11.8 | 12.9 | 11.7 | 1.10 | -5.2% | -1.2% | 3.1% | 9.4% | 2027-03-31 | 23 |
| Peer median (ex NKE) | | | 15.5 | 12.9 | 13.2 | 11.6 | 1.18 | | 3.2% | 6.5% | | | |

Reading: on EV/Sales (1.20 vs 1.18) and EV/EBITDA (11.3 vs 11.6), NKE sits at the peer median. On earnings it carries a clear premium: 24.9x NTM vs 13.2x, and 21.5x FY2028 vs 12.9x. Its revenue growth is the weakest of the group apart from Lululemon and Puma. The market is therefore pricing NKE's sales roughly like an average peer's, while paying up for depressed margins on the assumption that they recover. The P/E premium is the margin-recovery bet.

## (C) Reverse DCF

Question: what long-run EBIT margin and revenue growth justify an EV of $52,031M (market cap 52,506 + debt 7,893 less cash 8,368; leases excluded because EBIT is after rent)? CSV with the full grid: `valuation/reverse_dcf.csv`. Script: `valuation/scripts/rdcf.py`.

Assumptions:
- Valuation date 2026-10-12. FY2027 cash flow is pro-rated by 0.63 (the share of the year remaining); mid-period discounting.
- FY2027 and FY2028 are pinned to consensus. Revenue is 43,152 and 43,645. EBIT is backed out of EPS 1.288 and 1.646 with 1,487m diluted shares, about zero net interest and the stated tax rate, giving margins of 5.7% and 7.2%.
- FY2029 to FY2036: revenue grows at a constant CAGR. The EBIT margin ramps linearly from 7.2% (FY2028) to the steady-state margin by FY2031 and stays there.
- Reinvestment = revenue increase / 2.5 sales-to-capital (FY2026 invested capital is about $16.8B against $46.4B of revenue, which is about 2.8x). No credit is taken for working-capital release in down years.
- Terminal value at FY2036: NOPAT x (1 - g/ROIC) / (WACC - g), with terminal ROIC 20%.
- Tax 22.5% base (20% and 25% shown). Terminal growth 2% to 3%.
- WACC: the 10y UST is 5.24% (2026-10-12) and beta is 1.10 (Yahoo). A 5% ERP gives a cost of equity of about 10.7%. After-tax cost of debt is about 4.7% at a 13% debt weight, so WACC is about 10.0%. The grid runs 8% to 11%.

Implied steady-state EBIT margin (tax 22.5%), by revenue CAGR FY2028 to FY2036:

| WACC | Terminal g | CAGR 1% | CAGR 3% | CAGR 5% |
|---|---|---|---|---|
| 8% | 2% | 11.2% | 10.3% | 9.4% |
| 8% | 3% | 10.3% | 9.4% | 8.6% |
| 9% | 2% | 13.3% | 12.2% | 11.2% |
| 9% | 3% | 12.5% | 11.4% | 10.4% |
| 10% | 2% | 15.4% | 14.1% | 13.0% |
| 10% | 3% | 14.7% | 13.4% | 12.3% |
| 11% | 2% | 17.6% | 16.1% | 14.8% |
| 11% | 3% | 17.0% | 15.5% | 14.3% |

Tax sensitivity (WACC 10%, g 2%, CAGR 3%): 13.7% at 20% tax, 14.1% at 22.5%, 14.6% at 25%.

Implied revenue CAGR FY2028 to FY2036 for a fixed steady-state EBIT margin (tax 22.5%):

| WACC / g | 8% margin | 10% margin | 12% margin | 14% margin |
|---|---|---|---|---|
| 8% / 2% | 9.0% | 3.6% | -0.3% | -2.5% |
| 9% / 2.5% (avg of 2% and 3%) | 12.9% | 6.8% | 2.6% | -0.5% |
| 10% / 2% | 19.0% | 11.8% | 6.9% | 3.2% |
| 10% / 3% | 17.0% | 10.3% | 5.6% | 2.1% |
| 11% / 2% | 24.4% | 15.9% | 10.4% | 6.4% |

Cross-check, per share: a 12.5% margin, 4% CAGR and 2.5% terminal growth give $39.06 at a 9% WACC, $33.55 at 10% and $29.36 at 11%. At g = 2.5%: an 8% margin gives $20.25 to $21.34 (10% WACC, 1% to 3% CAGR), a 10% margin $24.52 to $26.19, and a 15% margin $35.17 to $38.29 ($40.55 to $44.47 at 9%).

## (D) What is priced in

- At $35.35 and a market-implied WACC near 10% (with a 5.2% 10-year yield), the price roughly needs Nike to get back to about 12% to 14% EBIT margins by FY2031 on low-single-digit growth (3% CAGR implies 13.4% to 14.1%). That is about the FY2023 to FY2024 level (12.1% to 12.7%) and the 10-year average (11.8%). It is well below the FY2016, FY2017 and FY2021 peaks (14.3% to 15.5%). At a 9% WACC the bar falls to about 11% to 12%; at 8% it falls to about 9% to 10%, close to today's 8.2%.
- The market is not paying for a growth franchise. EV/Sales of 1.13x is the lowest in at least 11 years (10-year average 3.06x) and in line with peers (1.18x). The multiple compression since FY2021 (4.74x) far exceeds the fall in margins.
- The sell side has capitulated. FY2027 and FY2028 EPS were cut about 25% in the last 30 days. Price targets cluster at 27 to 40, with a median of 34.40, below the price. Sell ratings went from 2 to 7, and short interest rose 31% in a month to 99m shares (6.7% of shares out, 3 days to cover). Options imply about a 13% move through the Dec 17 print (Dec ATM IV about 39% to 41%).
- Consensus for FY2027 (1.29) sits at the top half of guidance (1.15 to 1.35). Implied margins of 5.7% for FY2027 and 7.2% for FY2028 leave a large earnings gap to the 12% to 14% that the DCF needs by FY2031. Zacks' FY2029 EPS of 2.31 (6 estimates; 15.3x) is the only published bridge.
- A differentiated thesis therefore has to argue one of two things. Either margins recover faster or further than the 12% to 14% priced in (for example toward 14% to 15% by FY2029), or Nike's cost of capital is lower than 10%: at a 9% WACC, today's price already discounts only about 11% to 12% margins. The bear case has to argue that margins stay near 8% to 10%, where the model gives $20 to $26 per share at a 10% WACC ($23 to $30 at 9%), with 1% to 3% growth and 2.5% terminal growth. A sustained 15% margin gives $35 to $38 at 10% and $41 to $44 at 9%.
