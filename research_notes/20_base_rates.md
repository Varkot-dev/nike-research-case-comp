# AE_BASERATES: what happened after large consumer and brand stocks fell 75% to 80%+

Prepared 2026-10-13. Question: when large, well-known consumer or brand companies fell 70% to 85%+ from their peak, what did the stock do over the next 1, 2 and 3 years, and what separated recoveries from value traps? Where does Nike ($35.35 close on 2026-10-12, 80.1% below the $177.51 close on 2021-11-05) sit?

Source labels used below:
- **market data**: Yahoo Finance chart API, daily `close` (split-adjusted) and `adjclose` (dividends reinvested), `https://query2.finance.yahoo.com/v8/finance/chart/{TICKER}?period1=473385600&period2=1792022400&interval=1d&events=div,split`, fetched 2026-10-13, data used through 2026-10-12. Benchmark: S&P 500 total return index (`^SP500TR`, from 1988); S&P 500 price index (`^GSPC`) for the market-regime test.
- **SEC XBRL**: `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json`, fetched 2026-10-13 for 103 US filers.
- **repo**: `research_notes/thesis_tests/consensus_and_valuation.md` (Nike EV/sales 1.13x and EV/EBITDA 11.2x TTM ex leases at $35.35; cash and short-term investments $8,368M vs financial debt $7,893M at 2026-08-31).
- **my arithmetic**: computed in the scripts listed in Section G.
- **KNOWLEDGE, unverified**: CEO change, founder/family control and activist flags (manual_features.csv). These were coded from my background knowledge, not from opened pages, and are treated as indicative only.

All returns are total returns (dividends reinvested). "Excess" is the simple difference between the stock's total return and the S&P 500 total return over the same dates. All figures are historical frequencies, not forecasts.

## (A) Plain-English summary

1. **Sample (rule-based, not outcome-picked):** 113 consumer, retail, apparel, food, beauty, leisure and branded-hardware tickers produced 143 episodes with a drawdown of 70% or more from an all-time high (peak 1990 or later). After requiring a peak market value of at least about $3bn and a 75% crossing, 95 non-Nike episodes remain. 39 of them happened while the S&P 500 was within 15% of its own high ("idiosyncratic", Nike's situation; the S&P 500 was 1.0% below its high on Nike's 2026-10-02 trough, market data). The other 56 happened during market crashes (2000 to 2002, 2008 to 2009, March 2020).
2. **Raw base rates look very good but are mostly crash rebounds.** Buying all 93 episodes with a year of data at the 75% crossing (E75) returned a median +72% over 1 year and +100% over 3 years (82% and 79% positive). For the 56 crash-era episodes alone: +83% and +114%. Crash-era episodes got back to within 25% of the peak 62% of the time (33 of 53), against 37% (10 of 27) for idiosyncratic ones (Fisher p = 0.037).
3. **For Nike-like idiosyncratic declines, buying at the 80% crossing (where Nike is now) returned** a median +52% at 1 year (interquartile range -15% to +98%, 67% positive, n = 30), +65% at 2 years (-29% to +116%, n = 24) and +69% at 3 years (-20% to +145%, 71% positive, n = 24). Against the S&P 500 the median 3-year excess return was only +10%, with 54% of episodes ahead. Since 2009 it is -17%, with 44% ahead (n = 18).
4. **Full recoveries are rare when the decline is company-specific.** Of 27 idiosyncratic episodes with a complete outcome, 10 recovered (got back to 75% of the peak within 5 years), 12 were partial (made money but did not get back) and 5 were value traps (lost money over 3 years). The median best price within 5 years was 62% of the old peak. For Nike, 75% of the peak is $133, or +277% from $35.35 (my arithmetic).
5. **The strongest separator observable at entry was valuation, and Nike is on the wrong side of it.** Among idiosyncratic episodes, 6 of 11 with EV/sales at or below 1.0x at E75 recovered, against 0 of 9 above 1.0x (p = 0.014). By EV/EBITDA it was 5 of 10 at or below 8x against 0 of 5 above 8x (p = 0.10). Nike is at 1.13x sales and 11.2x EBITDA (repo). That is the median EV/sales of the whole sample at E75 (1.10x), and 63% of the episodes were cheaper on EV/EBITDA (median 5.9x). Nike is cheap against its own history, but not against other busted brands.
6. **Balance sheet also separated outcomes.** Idiosyncratic episodes with net cash at entry recovered 5 of 8 times, against 1 of 12 with net debt (p = 0.018). Nike is about neutral: net cash of about $0.5bn ex leases at 2026-08-31 (repo) and net debt of $0.4bn at 2026-05-31 (SEC XBRL, my arithmetic).
7. **Several popular "turnaround" signals did not separate outcomes in this sample:** positive free cash flow (48% vs 50% recovered), a CEO change in the prior 24 months (38% vs 39%, manual flag) and founder or family control (33% vs 40%, manual flag). The founder-controlled idiosyncratic group had a median 3-year return of only +17%, against +100% for the rest (n = 12 vs 14). A dividend cut before entry went with fewer full recoveries (3 of 13 vs 18 of 31, p = 0.049), but no value traps and a positive 3-year return in all 13 cases.
8. **Applied to Nike (historical frequency, entry at the 80% crossing):** the broad idiosyncratic base rate is a median of about +50% to +70% over 1 to 3 years, with roughly 1 in 3 episodes negative, and a coin flip against the S&P 500. In the Nike-like valuation subset (idiosyncratic, EV/sales above 0.8x, n = 11 to 13), medians were +44%, +59% and +65% at 1, 2 and 3 years, but only 45% beat the S&P 500 over 3 years (median -34%). In that subset, 0 of 10 episodes with a complete outcome got back to within 25% of the peak. Survivorship bias pushes all of these numbers up: adding just 5 failures at -90% cuts the idiosyncratic 3-year median from +87% to +40%.

## (B) Sample definition and episode table

**Universe (fixed before looking at outcomes).** 113 tickers (108 returned Yahoo data) listed in `scripts/universe.py`: apparel, footwear and luxury (24, including adidas, Puma, Kering, Burberry, Hugo Boss, ASICS); specialty, mass and online retail (27); food, beverage and restaurants (23); household and durables (9); beauty and personal care (6); branded consumer tech, media and autos (17); travel and leisure (5); and non-consumer controls (Boeing, GE). Five names the brief would include returned no Yahoo data because they are delisted: Hanesbrands, Nordstrom, Walgreens, Foot Locker and Tupperware (market data: HTTP 404). They are missing from the price study (see Section F).

**Episode rule (`scripts/find_episodes.py`).**
- **Drawdown basis:** Yahoo `close` (split-adjusted, not dividend-adjusted), the same basis as "NKE is 80% below its $177.51 record close."
- **Episode:** the close falls at least 70% below its running all-time high, with the peak on or after 1990-01-01.
- **Trough:** the lowest close before the stock regains the old peak, or before 2026-10-12.
- **Next episode:** may start only after a new high.
- **Entry points:** E75 and E80 are the first closes at least 75% and 80% below the peak. The trough is also reported.
- **Forward returns:** total return over +252, +504 and +756 trading days.

**Core-sample filters (`scripts/analyze.py`).**
- **Excluded:** PARA (the Yahoo symbol now belongs to Banzai International), GE (spin-off-adjusted history, non-consumer) and Boeing (control).
- **Size:** episodes with an approximate peak market value below $3bn are dropped. The value is peak close x SEC weighted diluted shares nearest the peak. For pre-2007 peaks it uses the earliest XBRL share count, so it is approximate. Non-SEC filers are kept as national blue-chip index names (my inference, size not computed).
- **Depth:** episodes that never reached the 75% crossing are dropped.

Result: 143 raw episodes, 47 excluded (listed below), 96 core episodes including Nike.

**Regime.** An episode is "idiosyncratic" if the S&P 500 price index was within 15% of its prior high on the E75 date, and "market-wide" otherwise. I used a 15% threshold rather than 20% so that early-COVID entries (for example NCLH on 2020-03-11, with the S&P 500 19% down) count as market-wide.

**Outcome (based on E75).**
- **Recovered:** the highest close within 5 years of E75 reaches at least 75% of the peak close.
- **Value trap:** not recovered, and the 3-year total return from E75 is zero or negative.
- **Partial:** everything else.
- **Too recent:** the window is still open.

**Valuation columns.** EV/S and EV/EBITDA at E75 come from SEC XBRL plus market data (my arithmetic).
- **Market cap:** actual price x latest weighted diluted shares.
- **EV:** market cap plus debt, minus cash and short-term investments (debt excludes operating leases).
- **Denominators:** the latest fiscal-year revenue, and operating income plus D&A, from a period ending at least 75 days before the date. These are not TTM.
- **Missing values:** "n/a" means the company is not an SEC XBRL filer, the date is pre-XBRL, or the tag is missing. Nike does not tag operating income, so its EV/EBITDA comes from the repo (11.2x TTM).

Episodes excluded by the filters:
- max drawdown 70-75%: never reached 75% entry (22): ADS.DE 1998 (-71%), ADS.DE 2021 (-72%), PUM.DE 2007 (-71%), CROX 2021 (-74%), GIL 2019 (-75%), 7936.T 2007 (-74%), URBN 2018 (-74%), BBY 2000 (-74%), DKS 2007 (-73%), DKS 2016 (-73%), WSM 1999 (-73%), DG 2022 (-74%), CMG 2007 (-75%), MCD 1999 (-74%), TAP 2016 (-71%), BUD 2016 (-74%), CPB 2016 (-72%), WHR 2015 (-70%), EPC 2007 (-74%), TSLA 2021 (-74%), CCL 2004 (-74%), EXPE 2017 (-71%)
- peak market cap below $3bn (approx) (21): PVH 1994 (-86%), DECK 1993 (-94%), FOSL 1994 (-77%), WWW 1998 (-72%), SHOO 1993 (-77%), SHOO 2000 (-71%), AEO 1994 (-81%), AEO 1999 (-79%), AEO 2001 (-75%), URBN 1999 (-77%), BBY 1994 (-81%), ULTA 2007 (-88%), ETSY 2015 (-79%), DPZ 2007 (-92%), SAM 1995 (-79%), HAIN 2000 (-72%), CELH 2007 (-100%), ELF 2016 (-77%), NUS 1997 (-86%), NFLX 2002 (-71%), NFLX 2004 (-77%)
- Yahoo ticker PARA now maps to Banzai International (reassigned symbol); not Paramount (1): PARA 2023 (-100%)
- non-consumer control (2): BA 2007 (-73%), BA 2019 (-78%)
- non-consumer; Yahoo history affected by 2023-2024 spin-offs; control only (1): GE 2000 (-90%)

Core episodes (sorted: idiosyncratic first, then market-wide; by E75 date). Source: market data and SEC XBRL, my arithmetic.

| # | Ticker | Peak | Trough | Max DD | E75 date | Regime | EV/S E75 | EV/EBITDA E75 | EV/S trough | E75 +1y | E75 +2y | E75 +3y | E75 +3y vs S&P | E80 +1y | E80 +3y | Outcome |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | AAPL | 1991-04-02 | 1997-12-23 | -82% | 1996-07-11 | idio | n/a | n/a | n/a | -26% | +79% | +205% | +77% | +101% | +664% | recovered |
| 2 | MAT | 1998-03-13 | 2000-03-10 | -80% | 2000-01-24 | idio | n/a | n/a | n/a | +39% | +69% | +87% | +123% | +99% | +138% | partial |
| 3 | ANF | 1999-04-12 | 2000-05-24 | -84% | 2000-04-13 | idio | n/a | n/a | n/a | +151% | +159% | +163% | +197% | +237% | +201% | recovered |
| 4 | BB | 2000-03-02 | 2002-10-07 | -95% | 2000-04-14 | idio | n/a | n/a | n/a | -21% | -46% | -56% | -27% | +30% | -38% | recovered |
| 5 | AMZN | 1999-12-10 | 2001-09-28 | -94% | 2000-10-12 | idio | n/a | n/a | n/a | -66% | -24% | +137% | +155% | -51% | +168% | partial |
| 6 | AAPL | 2000-03-22 | 2003-04-17 | -82% | 2000-11-29 | idio | n/a | n/a | n/a | +35% | -17% | +19% | +36% | +50% | +46% | recovered |
| 7 | HAS | 1999-05-03 | 2000-12-07 | -75% | 2000-12-07 | idio | n/a | n/a | n/a | +86% | +32% | +125% | +142% |  |  | partial |
| 8 | GME | 2007-12-24 | 2020-04-03 | -96% | 2012-07-24 | idio | 0.19 | 2.4 | 0.02 | +204% | +214% | +219% | +152% | -8% | +1581% | recovered |
| 9 | DECK | 2011-10-28 | 2012-10-31 | -76% | 2012-10-31 | idio | 0.70 | 3.1 | 0.70 | +140% | +205% | +96% | +38% |  |  | recovered |
| 10 | BBY | 2006-04-06 | 2012-12-28 | -81% | 2012-11-05 | idio | 0.13 | 3.3 | 0.11 | +214% | +153% | +165% | +107% | +249% | +191% | recovered |
| 11 | NUS | 2013-12-23 | 2026-09-30 | -97% | 2015-10-07 | idio | 0.78 | 5.0 | 0.16 | +97% | +93% | +138% | +85% | +97% | +72% | partial |
| 12 | GPRO | 2014-10-07 | 2025-04-10 | -99% | 2015-11-12 | idio | 2.07 | 14.1 | 0.08 | -56% | -64% | -77% | -118% | -46% | -71% | value trap |
| 13 | FOSL | 2012-04-09 | 2024-04-17 | -99% | 2015-11-13 | idio | 0.58 | 3.1 | 0.09 | +4% | -78% | -42% | -84% | -52% | -51% | value trap |
| 14 | RH | 2015-11-02 | 2017-02-07 | -76% | 2016-06-13 | idio | 0.35 | 3.2 | 0.32 | +103% | +503% | +334% | +286% |  |  | recovered |
| 15 | UAA | 2015-09-17 | 2025-11-20 | -92% | 2017-10-31 | idio | 1.28 | 11.0 | 0.50 | +77% | +69% | +16% | -21% | +141% | -14% | partial |
| 16 | M | 2015-07-16 | 2020-04-01 | -94% | 2017-11-06 | idio | 0.43 | 4.7 | 0.20 | +114% | +0% | -57% | -100% | -50% | +45% | value trap |
| 17 | COTY | 2015-07-01 | 2026-06-04 | -94% | 2018-11-13 | idio | 1.41 | 14.8 | 0.77 | +57% | -37% | +44% | -38% | +85% | +65% | partial |
| 18 | MAT | 2013-12-30 | 2020-03-23 | -85% | 2018-12-14 | idio | 1.43 | n/a | 1.05 | +10% | +46% | +75% | -15% | +44% | +113% | partial |
| 19 | HAIN | 2015-08-05 | 2026-07-29 | -99% | 2018-12-17 | idio | 0.98 | 14.5 | 0.45 | +48% | +129% | +147% | +54% | -45% | -95% | partial |
| 20 | NWL | 2016-08-15 | 2025-11-06 | -94% | 2019-04-25 | idio | 1.50 | n/a | 0.81 | +0% | +118% | +97% | +43% | +151% | +26% | partial |
| 21 | EPC | 2015-05-22 | 2025-12-08 | -85% | 2019-06-26 | idio | 1.13 | n/a | 0.85 | +12% | +69% | +35% | -6% | +81% | +98% | partial |
| 22 | TPR | 2012-03-26 | 2020-03-23 | -87% | 2019-08-15 | idio | 1.03 | 6.4 | 0.56 | -14% | +135% | +105% | +46% | +197% | +191% | partial |
| 23 | CPRI | 2014-02-25 | 2020-03-18 | -92% | 2020-02-26 | idio | 1.08 | 6.1 | 0.58 | +88% | +167% | +102% | +68% | +188% | +118% | partial |
| 24 | GME | 2021-01-27 | 2024-04-22 | -88% | 2021-02-04 | idio | 0.52 | n/a | 0.36 | +85% | +78% | +5% | -30% | +85% | +5% | recovered |
| 25 | PTON | 2021-01-13 | 2024-08-14 | -98% | 2021-12-07 | idio | 3.03 | n/a | 0.66 | -72% | -86% | -77% | -112% | -72% | -73% | value trap |
| 26 | W | 2021-03-22 | 2025-04-08 | -93% | 2022-04-22 | idio | 0.69 | 41.7 | 0.40 | -58% | -40% | -63% | -100% | -41% | -41% | value trap |
| 27 | CHWY | 2021-02-12 | 2024-04-30 | -87% | 2022-04-29 | idio | 1.30 | n/a | 0.48 | +7% | -45% | +31% | -11% | +43% | +76% | partial window open |
| 28 | SONO | 2021-04-15 | 2025-04-16 | -82% | 2023-10-13 | idio | 0.65 | 8.9 | 0.45 | +10% | +50% |  |  | +54% |  | too recent |
| 29 | EL | 2022-01-04 | 2025-04-08 | -87% | 2024-08-05 | idio | 2.31 | 16.3 | 1.49 | +1% | -2% |  |  | +37% |  | too recent |
| 30 | BRBY.L | 2023-04-25 | 2024-09-10 | -78% | 2024-09-03 | idio | n/a | n/a | n/a | +93% | +64% |  |  |  |  | too recent |
| 31 | CELH | 2024-03-13 | 2025-02-12 | -78% | 2025-02-03 | idio | 3.53 | 17.2 | 3.09 | +107% |  |  |  |  |  | too recent |
| 32 | PUM.DE | 2021-11-19 | 2025-11-18 | -87% | 2025-02-07 | idio | n/a | n/a | n/a | -18% |  |  |  | -3% |  | too recent |
| 33 | KER.PA | 2021-08-12 | 2025-04-09 | -80% | 2025-03-31 | idio | n/a | n/a | n/a | +36% |  |  |  | +81% |  | too recent |
| 34 | RH | 2021-08-12 | 2026-04-01 | -85% | 2025-04-03 | idio | 1.83 | 11.4 | 1.44 | -23% |  |  |  | -18% |  | too recent |
| 35 | FIVE | 2021-08-25 | 2025-04-08 | -76% | 2025-04-03 | idio | 0.76 | 5.3 | 0.71 | +285% |  |  |  |  |  | recovered |
| 36 | CRI | 2018-02-26 | 2025-08-01 | -81% | 2025-06-02 | idio | 0.44 | 4.0 | 0.36 | +33% |  |  |  | +70% |  | too recent |
| 37 | AEO | 2021-04-23 | 2025-06-13 | -75% | 2025-06-13 | idio | 0.28 | 2.3 | 0.28 | +95% |  |  |  |  |  | too recent |
| 38 | WHR | 2021-05-07 | 2026-10-09 | -89% | 2026-03-03 | idio | 0.56 | 19.5 | 0.50 |  |  |  |  |  |  | too recent |
| 39 | NKE | 2021-11-05 | 2026-10-02 | -81% | 2026-04-02 | idio | 1.44 | n/a | 1.09 |  |  |  |  |  |  | too recent |
| 40 | LULU | 2023-12-29 | 2026-10-07 | -82% | 2026-05-11 | idio | 1.19 | 4.9 | 0.83 |  |  |  |  |  |  | too recent |
| 41 | EBAY | 2000-03-24 | 2000-12-20 | -77% | 2000-12-20 | market | n/a | n/a | n/a | +137% | +140% | +359% | +367% |  |  | recovered |
| 42 | NOK | 2000-06-19 | 2012-07-17 | -97% | 2001-08-30 | market | n/a | n/a | n/a | -8% | +15% | -13% | -17% | +49% | +48% | value trap |
| 43 | HPQ | 2000-04-07 | 2002-10-09 | -86% | 2001-09-04 | market | n/a | n/a | n/a | -24% | +9% | +1% | -3% | -15% | +28% | partial |
| 44 | GAP | 2000-02-03 | 2020-04-02 | -90% | 2001-09-17 | market | n/a | n/a | 0.10 | -0% | +48% | +63% | +49% | +75% | +75% | partial |
| 45 | SONY | 2000-02-29 | 2012-12-04 | -94% | 2001-09-17 | market | n/a | n/a | n/a | +17% | +2% | -5% | -19% | +37% | +68% | value trap |
| 46 | RCL | 1999-11-16 | 2009-03-02 | -90% | 2001-09-17 | market | n/a | n/a | n/a | +22% | +156% | +274% | +260% | +32% | +322% | recovered |
| 47 | INTC | 2000-08-31 | 2009-02-23 | -84% | 2002-06-25 | market | n/a | n/a | 1.60 | +10% | +53% | +45% | +16% | +92% | +68% | partial |
| 48 | BOSS.DE | 2001-06-11 | 2002-09-25 | -77% | 2002-09-17 | market | n/a | n/a | n/a | +98% | +137% | +269% | +221% |  |  | recovered |
| 49 | KER.PA | 2000-01-03 | 2008-11-21 | -88% | 2002-09-30 | market | n/a | n/a | n/a | +25% | +21% | +52% | -5% | +72% | +112% | partial |
| 50 | F | 1999-05-03 | 2008-11-19 | -97% | 2002-10-03 | market | n/a | n/a | n/a | +30% | +66% | +18% | -38% | +71% | +39% | partial |
| 51 | CROX | 2007-10-31 | 2008-11-20 | -99% | 2008-03-10 | market | n/a | n/a | n/a | -93% | -58% | +7% | -4% | -81% | +84% | partial |
| 52 | GRMN | 2007-10-29 | 2009-02-20 | -88% | 2008-10-03 | market | 1.75 | 5.9 | 0.77 | +31% | +17% | +30% | +20% | +60% | +54% | partial |
| 53 | M | 2007-03-23 | 2008-11-19 | -88% | 2008-10-09 | market | n/a | n/a | n/a | +72% | +126% | +154% | +114% | +139% | +256% | recovered |
| 54 | NWL | 1998-07-17 | 2009-03-09 | -92% | 2008-10-09 | market | n/a | n/a | n/a | +23% | +50% | +5% | -35% | +40% | +51% | partial |
| 55 | BOSS.DE | 2007-05-17 | 2009-03-06 | -83% | 2008-10-10 | market | n/a | n/a | n/a | +107% | +252% | +535% | +497% | +118% | +710% | recovered |
| 56 | LULU | 2007-10-22 | 2009-03-09 | -92% | 2008-10-15 | market | n/a | n/a | n/a | +85% | +227% | +670% | +626% | +129% | +874% | recovered |
| 57 | WSM | 2006-01-11 | 2008-11-20 | -90% | 2008-10-22 | market | n/a | n/a | n/a | +103% | +212% | +275% | +227% | +152% | +418% | recovered |
| 58 | SBUX | 2006-05-05 | 2008-11-20 | -82% | 2008-10-24 | market | 0.72 | 4.4 | 0.66 | +107% | +198% | +337% | +287% | +199% | +498% | recovered |
| 59 | EBAY | 2004-12-30 | 2009-03-09 | -83% | 2008-10-27 | market | 2.03 | 12.8 | 1.30 | +59% | +102% | +114% | +57% | +98% | +155% | recovered |
| 60 | HOG | 2006-11-22 | 2009-03-05 | -89% | 2008-10-27 | market | n/a | n/a | n/a | +45% | +73% | +117% | +61% | +101% | +183% | recovered |
| 61 | EXPE | 2007-10-05 | 2008-11-20 | -83% | 2008-11-05 | market | n/a | n/a | n/a | +178% | +224% | +240% | +200% | +266% | +318% | recovered |
| 62 | TSN | 1998-11-05 | 2008-11-20 | -83% | 2008-11-11 | market | n/a | n/a | n/a | +160% | +202% | +290% | +243% | +175% | +322% | recovered |
| 63 | ANF | 2007-10-10 | 2020-04-02 | -91% | 2008-11-12 | market | n/a | n/a | 0.01 | +81% | +130% | +188% | +130% | +176% | +232% | recovered |
| 64 | AEO | 2007-01-16 | 2020-04-22 | -80% | 2008-11-17 | market | n/a | n/a | 0.17 | +86% | +97% | +85% | +30% | +345% | +113% | partial |
| 65 | BRBY.L | 2007-04-20 | 2008-11-21 | -78% | 2008-11-18 | market | n/a | n/a | n/a | +240% | +474% | +670% | +614% |  |  | recovered |
| 66 | PVH | 2007-06-04 | 2008-11-20 | -78% | 2008-11-19 | market | n/a | n/a | n/a | +188% | +330% | +343% | +282% |  |  | recovered |
| 67 | BBWI | 2006-11-10 | 2009-03-06 | -80% | 2008-11-19 | market | n/a | n/a | n/a | +147% | +394% | +602% | +541% | +277% | +849% | recovered |
| 68 | MAR | 2007-04-18 | 2008-11-20 | -76% | 2008-11-20 | market | n/a | n/a | n/a | +114% | +222% | +151% | +82% |  |  | recovered |
| 69 | GIL | 2007-10-30 | 2009-03-05 | -87% | 2008-12-11 | market | n/a | n/a | n/a | +137% | +228% | +113% | +62% | +155% | +118% | recovered |
| 70 | BB | 2008-06-19 | 2024-08-07 | -99% | 2008-12-15 | market | n/a | n/a | 1.42 | +74% | +61% | -59% | -108% | -62% | -65% | value trap |
| 71 | FOSL | 2007-12-10 | 2009-02-11 | -75% | 2009-02-03 | market | n/a | n/a | n/a | +195% | +543% | +761% | +692% |  |  | recovered |
| 72 | UAA | 2007-08-09 | 2009-03-06 | -82% | 2009-02-10 | market | n/a | n/a | n/a | +49% | +304% | +404% | +329% | +110% | +623% | recovered |
| 73 | LOGI | 2007-12-28 | 2013-04-26 | -83% | 2009-02-17 | market | n/a | n/a | 0.29 | +75% | +110% | -6% | -88% | +5% | +124% | value trap |
| 74 | WHR | 2007-06-19 | 2009-03-09 | -83% | 2009-02-18 | market | n/a | n/a | n/a | +204% | +206% | +167% | +84% | +297% | +268% | recovered |
| 75 | TPR | 2007-04-20 | 2009-03-09 | -78% | 2009-02-23 | market | 1.27 | 3.2 | 1.10 | +176% | +330% | +475% | +381% |  |  | recovered |
| 76 | DECK | 2007-12-26 | 2009-03-02 | -77% | 2009-03-02 | market | n/a | n/a | n/a | +232% | +566% | +495% | +387% |  |  | recovered |
| 77 | HLF | 2008-04-08 | 2009-03-09 | -75% | 2009-03-09 | market | n/a | n/a | n/a | +260% | +558% | +1031% | +918% |  |  | recovered |
| 78 | NFLX | 2011-07-13 | 2012-09-25 | -82% | 2011-11-21 | market | 1.69 | 11.3 | 0.73 | +11% | +367% | +379% | +294% | +328% | +1270% | recovered |
| 79 | BBWI | 2015-11-04 | 2020-03-23 | -91% | 2018-12-21 | market | 0.99 | 5.5 | 0.50 | -22% | +64% | +268% | +163% | +41% | +174% | recovered |
| 80 | KHC | 2017-02-17 | 2020-03-12 | -79% | 2020-03-09 | market | 2.14 | n/a | 2.06 | +72% | +77% | +83% | +33% |  |  | partial |
| 81 | NCLH | 2015-11-02 | 2020-03-18 | -88% | 2020-03-11 | market | 1.62 | 5.5 | 1.27 | +101% | +18% | -10% | -58% | +218% | +38% | value trap |
| 82 | BOSS.DE | 2015-04-10 | 2020-03-19 | -84% | 2020-03-12 | market | n/a | n/a | n/a | +17% | +57% | +136% | +68% | +56% | +188% | partial |
| 83 | 7936.T | 2015-08-17 | 2020-03-19 | -81% | 2020-03-12 | market | n/a | n/a | n/a | +99% | +145% | +324% | +248% | +147% | +457% | recovered |
| 84 | W | 2019-03-12 | 2020-03-19 | -86% | 2020-03-12 | market | 0.58 | n/a | 0.33 | +858% | +247% | -6% | -72% | +858% | -6% | recovered |
| 85 | CCL | 2018-01-29 | 2022-10-10 | -91% | 2020-03-12 | market | 1.03 | 3.9 | 20.27 | +90% | +15% | -39% | -105% | +128% | -33% | value trap |
| 86 | RCL | 2020-01-17 | 2020-03-18 | -83% | 2020-03-12 | market | 1.81 | 5.9 | 1.41 | +198% | +126% | +113% | +47% | +296% | +175% | recovered |
| 87 | PVH | 2018-06-08 | 2020-03-23 | -83% | 2020-03-16 | market | 0.58 | 4.6 | 0.46 | +160% | +84% | +80% | +6% | +217% | +119% | recovered |
| 88 | KSS | 2018-09-04 | 2025-04-16 | -93% | 2020-03-16 | market | 0.22 | 1.9 | 0.12 | +223% | +191% | +34% | -40% | +288% | +61% | recovered |
| 89 | BYND | 2019-07-26 | 2026-10-12 | -100% | 2020-03-18 | market | 6.84 | n/a | 19.18 | +148% | -13% | -72% | -145% | -60% | -93% | recovered |
| 90 | NFLX | 2021-11-17 | 2022-05-11 | -76% | 2022-05-11 | market | 3.06 | 14.2 | 3.06 | +104% | +269% | +616% | +558% |  |  | recovered |
| 91 | ETSY | 2021-11-24 | 2025-04-08 | -86% | 2022-05-24 | market | 4.98 | 21.5 | 2.36 | +23% | -13% | -21% | -78% | -24% |  | value trap |
| 92 | SAM | 2021-04-20 | 2026-06-04 | -88% | 2022-05-24 | market | 1.90 | 48.8 | 0.81 | -2% | -20% | -29% | -86% | -11% |  | value trap |
| 93 | WWW | 2021-05-07 | 2023-10-13 | -84% | 2022-11-17 | market | 0.89 | 11.4 | 0.56 | -16% | +125% | +60% | -18% | +50% | +146% | partial window open |
| 94 | HLF | 2019-02-04 | 2025-02-12 | -92% | 2022-12-06 | market | 0.77 | 5.3 | 0.48 | +9% | -39% | +8% | -74% | -11% | -2% | partial window open |
| 95 | VFC | 2020-01-02 | 2025-04-08 | -90% | 2023-02-23 | market | 1.30 | 8.1 | 0.83 | -34% | +7% | -16% | -95% | -32% | -1% | value trap |
| 96 | ELF | 2024-06-27 | 2026-06-05 | -77% | 2025-04-07 | market | 3.25 | 17.9 | 2.69 | +19% |  |  |  |  |  | too recent |

**Nike check from the brief:** Nike's worst drawdown before 2021 was -64.9% (close $9.47 on 1997-02-13 to $3.32 on 2000-02-25, split-adjusted; market data, my arithmetic). Nike 2000 to 2001 therefore does not qualify under the 70% rule. adidas 2021 to 2022 (-72%), Crocs 2021 to 2022 (-74%) and Tesla 2021 to 2023 (-74%) also never reached the 75% entry. Under Armour 2015 to 2025 (-92%), VF 2020 to 2025 (-90%), Estee Lauder 2022 to 2025 (-87%), Kraft Heinz 2017 to 2020 (-79%), Puma 2021 to 2025 (-87%), Kering 2021 to 2025 (-80%) and Lululemon 2023 to 2026 (-82%) all qualify.

## (C) Forward return statistics

Total return from the entry close. Percentages are medians, with interquartile range in brackets. "Hit" means the share of episodes with a positive return. Source: market data, my arithmetic (`out/forward_return_stats.csv`).

| Group | Entry | n (1y/2y/3y) | 1y | 2y | 3y | Hit 1y / 3y | 3y excess vs S&P 500 TR (hit) |
|---|---|---|---|---|---|---|---|
| All core | E75 | 93/85/82 | +72% [+10%, +114%] | +84% [+17%, +202%] | +100% [+7%, +261%] | 82% / 79% | +48% (62%) |
| All core | E80 | 74/68/66 | +78% [+11%, +152%] | +89% [+11%, +222%] | +112% [+38%, +198%] | 76% / 80% | +45% (68%) |
| Market-wide (S&P 500 down 15%+) | E75 | 56/55/55 | +83% [+21%, +147%] | +126% [+49%, +225%] | +114% [+8%, +330%] | 86% / 80% | +61% (65%) |
| Market-wide | E80 | 44/44/42 | +100% [+39%, +182%] | +147% [+42%, +258%] | +121% [+52%, +306%] | 82% / 86% | +67% (76%) |
| **Idiosyncratic (Nike's regime)** | E75 | 37/30/27 | +36% [0%, +95%] | +66% [-22%, +126%] | +87% [+10%, +138%] | 76% / 78% | +38% (56%) |
| **Idiosyncratic** | **E80** | 30/24/24 | **+52% [-15%, +98%]** | **+65% [-29%, +116%]** | **+69% [-20%, +145%]** | 67% / 71% | **+10% (54%)** |
| Idiosyncratic, entry after mid-2009 | E75 | 30/23/20 | +42% [+2%, +96%] | +69% [-19%, +132%] | +60% [-7%, +113%] | 80% / 75% | -8% (45%) |
| Idiosyncratic, entry after mid-2009 | E80 | 24/18/18 | +49% [-23%, +88%] | +65% [-30%, +93%] | +55% [-35%, +109%] | 62% / 67% | -17% (44%) |

Buying at the exact trough is not realistic, but for reference: from the trough, the median 1-year return was +195% (all core, n = 82) and +167% (idiosyncratic, n = 29). The gap between that and the E75 or E80 numbers is how much timing explains.

**Outcome counts (E75, decided episodes).** All core: 43 recovered, 23 partial, 14 value traps (15 still open). Market-wide: 33 / 11 / 9. Idiosyncratic: 10 / 12 / 5. Among the 27 decided idiosyncratic episodes, the median best close within 5 years was 62% of the peak (quartiles 51% and 106%). Among the 53 market-wide ones it was 97%.

**The 2021 to 2025 consumer cohort (idiosyncratic, mostly too recent for 3-year data):**
- **1 year from E75:** Puma -18%, Kering +36%, Burberry +93%, Carter's +33%, American Eagle +95%, RH -23%, Celsius +107%, Estee Lauder +1%, Five Below +285%, Sonos +10%.
- **Spread:** median +35% (my arithmetic on these 10). The dispersion is wide, and the cohort shares Nike's macro backdrop.

## (D) Features that separated recoveries from value traps

Test: the recovery rate (to within 25% of the peak within 5 years) by feature at the E75 date, decided episodes only, with a two-sided Fisher exact test. Fundamentals are point-in-time: a fiscal period counts only if it ended at least 75 days before entry. Fundamentals exist only for SEC XBRL filers (mostly entries from 2008 on), so n is much smaller than the full sample. Source: `out/feature_tests_fisher.csv` and `out/feature_splits.csv`.

| Feature at entry | Group | Recovered if TRUE | Recovered if FALSE | Fisher p | 3y median TRUE vs FALSE | Reading |
|---|---|---|---|---|---|---|
| S&P 500 down 15%+ (market-wide) | all | 33/53 (62%) | 10/27 (37%) | 0.037 | +117% vs +92% | Crash rebounds recover; company-specific falls mostly do not |
| EV/sales at or below 1.0x | all | 11/16 (69%) | 6/22 (27%) | 0.020 | +96% vs +40% | Cheapness on sales mattered |
| EV/sales at or below 1.0x | idiosyncratic | 6/11 (55%) | 0/9 (0%) | 0.014 | +117% vs +44% | Strongest single separator; still 4/9 excluding GameStop's two meme-era episodes |
| EV/EBITDA at or below 8x | idiosyncratic | 5/10 (50%) | 0/5 (0%) | 0.10 | +105% vs +16% | Same direction, smaller n |
| Net cash (cash above debt ex leases) | idiosyncratic | 5/8 (62%) | 1/12 (8%) | 0.018 | +96% vs +60% | Leverage blocked full recoveries |
| Net cash | all | 11/17 (65%) | 10/26 (38%) | 0.12 | +105% vs +78% | Same direction |
| Revenue growth above 0 (latest FY) | all | 13/26 (50%) | 1/8 (12%) | 0.10 | +44% vs +55% | Falling sales rarely fully recovered, but 3y returns were similar |
| Gross margin up y/y | all | 9/16 (56%) | 5/17 (29%) | 0.17 | +80% vs +35% | Directionally helpful, not significant |
| Positive free cash flow | all | 15/31 (48%) | 6/12 (50%) | 1.00 | +100% vs +30% | No separation on recovery |
| Dividend cut before entry (payers) | all | 3/13 (23%) | 18/31 (58%) | 0.049 | +63% vs +125% | Cutters seldom regained the peak, but all 13 were positive at 3y |
| Peak to E75 within 2 years | all | 32/51 (63%) | 11/29 (38%) | 0.038 | +113% vs +100% | Slow-burn declines recovered less often |
| Peak to E75 within 2 years | idiosyncratic | 6/13 (46%) | 4/14 (29%) | 0.44 | +87% vs +97% | Not significant |
| CEO change in prior 24 months [manual] | idiosyncratic | 3/8 (38%) | 7/18 (39%) | 1.00 | +75% vs +92% | No separation |
| Founder, family or sponsor control [manual] | idiosyncratic | 4/12 (33%) | 6/15 (40%) | 1.00 | +17% vs +100% | No separation on recovery; worse median and more traps (4 of 12 vs 1 of 15) |
| Activist stake by entry + 12 months [manual] | idiosyncratic | 1/5 (20%) | 9/22 (41%) | 0.62 | +5% vs +96% | n too small |

**What distinguished the value traps (5 idiosyncratic: GoPro 2015, Fossil 2015, Macy's 2017, Wayfair 2022, Peloton 2021).**
- **What they shared:**
  - **Revenue at entry:** three were still growing in their latest FY (GoPro +41%, Fossil +8%, Peloton +120%; SEC XBRL), so trailing revenue growth did not protect them.
  - **Next 3 years:** revenue then fell. In all five, revenue in the third fiscal year after entry was below the last fiscal year before entry (SEC XBRL).
  - **Valuation or leverage:** two had EV/sales above 2x at entry (GoPro 2.07x, Peloton 3.03x), and Macy's and Wayfair carried net debt ($5.5bn and $0.65bn; SEC XBRL, my arithmetic).
  - **Control:** four of the five were founder- or family-controlled (manual flag).
- **What the recoveries shared (Deckers 2012, Best Buy 2012, RH 2016, GameStop 2012, Five Below 2025):** EV/sales of 0.13x to 0.76x and EV/EBITDA of 2.4x to 5.3x at entry (SEC XBRL, my arithmetic).

**Alternatives tested and ruled out as the main separator:**
- **Sector:** apparel recovered 62% of the time, but mostly in crash-era episodes. The idiosyncratic apparel subset (n = 5 with 3y data) is too small to read.
- **Era:** idiosyncratic results after 2009 are weaker on excess returns (-8% median, 3y), but recovery rates show the same valuation split.
- **FCF and CEO change:** no separation (table above).

The remaining candidates are valuation at entry and net cash. The two overlap: cheap, unlevered companies were mostly low-margin retailers. This sample cannot separate "cheap" from "retailer with operating leverage to a sales rebound." Deciding that would need a larger sample of high-gross-margin brand companies trading below 1x sales, and those barely exist here.

## (E) Where Nike sits and the implied base-rate distribution

| Feature | Nike now | Source | Bucket and base rate (idiosyncratic unless noted) |
|---|---|---|---|
| Regime | S&P 500 1.0% below its high at Nike's 2026-10-02 trough | market data | Idiosyncratic: 37% full recoveries (10 of 27) |
| Drawdown and entry | -80.1% at $35.35; crossed 75% on 2026-04-02 and 80% on 2026-09-30 | market data | Use the E80 rows |
| EV/sales | 1.13x TTM ex leases | repo | Above 1.0x: 0 of 9 recovered. Nike is at the sample median of 1.10x at E75 |
| EV/EBITDA | 11.2x TTM ex leases | repo | Above 8x: 0 of 5 recovered. 63% of entries were cheaper (median 5.9x) |
| Revenue growth | FY2026 +0.2% reported (consensus FY2027 -7.0%, repo) | SEC XBRL; repo | Borderline. Falling revenue went with 1 of 8 recoveries (all core) |
| Gross margin | FY2026 +18 bps y/y (42.9% vs 42.7%) | SEC XBRL, my arithmetic | Borderline. May include the tariff-recovery effect discussed in valuation_vs_business.md |
| Net cash or debt | About $0.5bn net cash at 2026-08-31 ex leases | repo | Roughly neutral. Net cash: 5 of 8 recovered; net debt: 1 of 12 |
| Free cash flow | FY2026 CFO less capex $2.18bn | SEC XBRL, my arithmetic | No separation |
| Dividend | Not cut (TTM $1.62 vs $1.48 before) | market data | No cut: 18 of 31 recovered (all core) |
| Speed of decline | 4.4 years from peak to E75 | market data | Slow decline: 38% recovered (all core) |
| CEO change | Elliott Hill CEO since 2024-10-14 | repo 01_ceo_and_board.md | No separation |
| Founder control | Knight family Class A elects about three-quarters of the board | KNOWLEDGE, unverified (repo also flags it) | Founder-controlled: 3y median +17%, 4 of 12 traps |

**Implied distribution for an entry around today's price (historical frequency, not a forecast).** Source: `out/forward_return_stats.csv` and `out/nike_like_subsets.csv`.

| Reference class (entry at the 80% crossing) | n (1y/2y/3y) | 1y median [IQR] | 2y median [IQR] | 3y median [IQR] | Hit 1y / 2y / 3y | 3y excess median (hit) | Full recovery within 5y |
|---|---|---|---|---|---|---|---|
| A. All idiosyncratic | 30/24/24 | +52% [-15%, +98%] | +65% [-29%, +116%] | +69% [-20%, +145%] | 67% / 71% / 71% | +10% (54%) | 10 of 27 (E75 basis) |
| B. Idiosyncratic, EV/sales above 0.8x at E75 | 13/11/11 | +44% [-18%, +141%] | +59% [-42%, +107%] | +65% [-43%, +105%] | 69% / 64% / 64% | -34% (45%) | 0 of 10 decided |
| C. Idiosyncratic, EV/EBITDA above 8x at E75 | 8/5/5 | +10% [-42%, +62%] | +1% [-55%, +11%] | -41% [-71%, -14%] | 50% / 60% / 20% | -89% (0%) | 0 of 5 decided |
| D. Idiosyncratic, entry after mid-2009 | 24/18/18 | +49% [-23%, +88%] | +65% [-30%, +93%] | +55% [-35%, +109%] | 62% / 67% / 67% | -17% (44%) | |

Members:
- **Class B:** Under Armour 2017, Tapestry 2019, Capri 2020, Hain 2018, Newell 2019, Mattel 2018, Coty 2018, Edgewell 2019, GoPro 2015, Peloton 2021, Chewy 2022, plus Lululemon, RH 2025, Celsius and Estee Lauder (too recent).
- **Class C:** Under Armour 2017, Wayfair 2022, Hain 2018, Coty 2018, GoPro 2015 (complete), plus RH, Celsius, Whirlpool, Estee Lauder and Sonos (too recent).
- **Caveat:** C has n = 5 at 3 years and should be read as a warning, not a distribution.

**Reading for the pitch.**
- **Absolute returns:** the historical frequency supports "more likely than not to be higher in 1 to 3 years". In the broad idiosyncratic class, about two-thirds of episodes made money at every horizon, with a median of +50% to +70%.
- **Relative returns:** it does not support "likely to beat the market". The 3-year excess hit rate is 45% to 54% across classes A, B and D.
- **Full recovery:** it argues against a full-recovery thesis. No episode with Nike's valuation features (above 1x sales, above 8x EBITDA) got back to 75% of its peak within 5 years.
- **Bull case:** it has to rest on Nike-specific evidence (margin recovery, from the repo's other notes), not on the base rate.
- **Bear case:** the realistic version from base rates is a "partial" outcome (Under Armour 2017, Coty 2018, Newell 2019 pattern). In that pattern the stock bounces 50% to 100% at some point but trails the S&P 500 over 3 years. It is not a collapse.

## (F) Limits

- **Survivorship bias, the biggest limit.** Yahoo returns no data for delisted names, so Hanesbrands, Nordstrom, Walgreens, Foot Locker and Tupperware are missing. So are other well-known consumer failures that a broader universe would include, for example Bed Bath & Beyond, J.C. Penney, Sears, Rite Aid, Revlon, Avon, RadioShack, Circuit City and Toys R Us (names from my knowledge; their outcomes are not priced or verified here). Several ended in bankruptcy or low takeout prices. Sensitivity on the idiosyncratic E75 3-year distribution (n = 27, median +87%, 78% positive): adding 5 failures at -90% gives a median of +40% and 66% positive; 10 gives +19% and 57%; 15 gives -19% and 50% (my arithmetic, `out/nike_compare_log.txt`). Treat every number above as an upper bound.
- **Hindsight in the universe.** The tickers are names that are well known today. That favours survivors and companies that later became famous (Amazon, Apple, Netflix). Rule-based episode selection inside the universe does not remove this.
- **Small n for the conditional cells.** The key Nike-like cells have 5 to 13 episodes. With Fisher p-values of 0.01 to 0.10 on 15 to 20 decided episodes, a single reclassification can move a rate by 10 to 20 points. Episodes also cluster in time (2008 to 2009, 2020, 2021 to 2022), so they are not independent draws.
- **Overlapping companies.** Some companies appear twice (for example GameStop 2012 and 2021, RH 2016 and 2025, Mattel 2000 and 2018). GameStop 2021 counts as "recovered" because of the meme-stock spike, which is rule-consistent but not a fundamental recovery.
- **Valuation data.** EV uses the latest fiscal-year revenue and operating income plus D&A, not TTM. Debt is approximated from XBRL tags (the largest valid combination), excludes leases and may miss some instruments. Share counts are weighted diluted counts, with a correction for filings that tagged shares x1000. Pre-2008 entries and foreign companies have no fundamentals, so the feature tests rest on about 30 to 50 episodes. Nike's own EV/EBITDA comes from the repo because Nike does not tag operating income.
- **Currencies.** Returns for adidas, Puma, Kering, Burberry, Hugo Boss and ASICS are in local currency, but they are compared with the S&P 500 in USD.
- **Manual flags.** CEO change, founder control and activist flags are KNOWLEDGE, unverified, so they should not support any claim on their own.
- **Outcome thresholds.** The "recovered" (75% of peak) and "value trap" (3-year return of zero or less) cut-offs are my choices. Changing them changes the counts but not the ranking of features.
- **Not a forecast.** These are historical frequencies of what happened to other companies. They say nothing about Nike's specific drivers, which the repo's other notes cover.

## (G) Files

Scripts (`scripts/baserates/`), all run with `python3 -I`:
- `universe.py`: the fixed ticker list.
- `fetch_prices.py`: Yahoo chart API, browser User-Agent, 1.5 to 2.5 s spacing.
- `fetch_sec.py`: SEC companyfacts, sent only to data.sec.gov with the contact the user provided.
- `find_episodes.py`: drawdown rule, entries, forward returns, dividend TTM.
- `features.py`: point-in-time XBRL fundamentals and EV multiples.
- `analyze.py`: core sample, regimes, outcomes, statistics, feature splits.
- `nike_compare.py`: Fisher tests, Nike-like subsets, survivorship sensitivity.
- `make_tables.py`: markdown tables.

Manual input: `data/baserates/manual_features.csv` (KNOWLEDGE flags with notes).

Outputs (`data/baserates/`):
- `episodes_raw.csv`: 143 rule-matched episodes.
- `episodes_features.csv`: plus XBRL features.
- `episodes_all.csv`: plus exclusion, regime, outcome and dividend flags.
- `episodes_core.csv`: the 96 core episodes.
- `forward_return_stats.csv`, `feature_splits.csv`, `feature_tests_fisher.csv`, `nike_like_subsets.csv`.
- `table_core.md`, `table_excluded.md`.
- Logs: `analysis_log.txt`, `analyze_stdout.txt`, `nike_compare_log.txt`, `nike_compare_stdout.txt`, `fetch_log.txt`, `sec_fetch_log.txt`.

Raw downloads (untrusted, parsed as JSON only): Yahoo prices (108 tickers plus `^GSPC`, `SPY` and `^SP500TR`) and 103 SEC companyfacts files; about 430 MB, not committed, re-fetched by the scripts.
