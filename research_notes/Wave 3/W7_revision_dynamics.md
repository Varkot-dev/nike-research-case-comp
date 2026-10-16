# W7: FY28 consensus revision dynamics (how big, how fast, is it over)

Prepared 2026-10-16. Figures are pulled 2026-10-16 ~16:38 to 16:45 UTC unless a timestamp says otherwise. Data files in this folder: `W7_snapshots.csv` (Yahoo earningsTrend for NKE, ADS.DE, ADDYY, ONON, DECK, LULU, UAA, PUM.DE, every period), `W7_nke_consensus_path.csv` (FY27 and FY28 consensus at each date available), `W7_broker_actions.csv` (every broker action since Jan 1 2026, 93 from Yahoo plus 19 from MarketBeat and TipRanks), `W7_broker_fy28_news.csv` (news-reported broker EPS), `W7_base_rate_universe.csv` (249-ticker epsTrend panel, pulled 2026-10-16 16:45 UTC), `W7_scripts/`.

Tags: OPENED = page or API read directly (WebFetch results are a small model's summary of the page, so quotes are as returned). SNIPPET = search summary only. DERIVED = my arithmetic.

## 1. Answer first

1. **FY28 consensus EPS is $1.617 (Yahoo, 39 analysts, Oct 16, OPENED), down 26.6% from $2.202 thirty days ago (Sep 16) and 28.7% from $2.267 ninety days ago (Jul 15)** (DERIVED from Yahoo epsTrend). In dollars, $0.585 of EPS (about $869M of net income at 1,485M shares) came off in one month. Nothing moved before the print: Jul 15 to Sep 16 the mean fell only 2.9% ($2.267 to $2.202), even though BofA, Needham and Stifel cut in September. The cut is one gap after the Oct 1 release, not a drift.
2. **The cut has slowed sharply but is not finished.** DERIVED from the dated Yahoo points: Sep 13 to Oct 6 -19.8%; Oct 6 to Oct 9 -7.2%; Oct 9 to Oct 13 -0.4%; Oct 13 to Oct 16 -1.8%. The last 7 days (Oct 9 to 16) were -2.2%, which is 8% of the 30-day cut. Yahoo shows 0 upward and 28 downward FY28 revisions (28 of 39 analysts, 72%) in both the 7-day and 30-day windows. The identical 7d and 30d counts mean the counts are ingestion-window counts and cannot be mapped to the dated broker notes (most dated notes were Oct 2); treat them as direction only.
3. **FY27 moved the same way: $1.703 to $1.276 (-25.1%)**, now 2.1% above the guide midpoint ($1.25; guide $1.15 to $1.35, Oct 1 8-K per D1). The FY27 to FY28 step shrank less than the levels: from +$0.498 (+29.3%) before the print to +$0.340 (+26.7%) now (DERIVED). Analysts moved both years down in near-parallel and kept a recovery step of 26.7%. That step is the number D1 attacks.
4. **Against D1 (OPENED repo note): consensus $1.617 is $0.057 (3.6%) above D1 case A ($1.56), $0.157 (10.7%) above case B ($1.46), and $0.447 (38.2%) above the base case ($1.17)** (DERIVED). At the Oct 14 consensus ($1.646) the same gaps were $0.086, $0.186 and $0.476, so the street has closed $0.029 toward D1 in two days. To reach D1 case A needs another -3.5%, case B -9.7%, base -27.6%.
5. **N8 base-rate margin.** Implied FY28 EBIT margin at $1.617 is about 7.2% (DERIVED: the D1 tax and interest convention, 24.4% tax backed out of D1's $1.646 / $3,179M / $43,645M, $55M net interest, 1,485M shares, applied to Yahoo's Oct 16 FY28 revenue of $43,459M). N8 expects a FY31 margin of 9.4% from FY26's 8.3%. Consensus FY28 is therefore 1.1 points below FY26 and 2.2 points below N8's FY31 expectation. Consensus FY28 is not above N8's base-rate path; the disagreement is with D1's 5.4% base, not with N8.
6. **Smoking gun: NO.** The data show a fast, large, broad and not-yet-finished FY28 cut, but nothing here proves further cuts. Free base rates say the next 30 days after a 15%+ cut are small (median about -0.1%, worst -5%), so the expected drift to the Nov 16 to 17 Investor Day is about 0% to -3%, not a second 25%.

## 2. NKE snapshot, Yahoo earningsTrend (OPENED, 2026-10-16 16:38 UTC)

| Fiscal year | Current | 7d ago (Oct 9) | 30d ago (Sep 16) | 60d ago (Aug 17) | 90d ago (Jul 18) | Low | High | Analysts | Revenue mean |
|---|---|---|---|---|---|---|---|---|---|
| FY27 EPS | 1.276 | 1.289 | 1.703 | 1.724 | 1.726 | 1.01 | 1.69 | 36 | $43,020M |
| FY28 EPS | 1.617 | 1.653 | 2.202 | 2.238 | 2.239 | 1.10 | 3.22 | 39 | $43,459M |

Yahoo revision counts: FY27 0 up / 28 down (7d), 0 up / 27 down (30d). FY28 0 up / 28 down (7d), 0 up / 28 down (30d). Next quarters: Q2 FY27 $0.381 (30d ago $0.523, -27%); Q3 FY27 $0.265 (30d ago $0.432, -39%). Earlier same-source pulls, kept as the time series in `W7_nke_consensus_path.csv`: Oct 13 FY28 $1.646 (7d ago $1.780, 30d $2.221, 90d $2.267; REPO `consensus_and_valuation.md`, OPENED file), Oct 14 identical.

Other aggregators the same day, which do not agree with Yahoo:

| Source | FY28 EPS mean | Low / high | n | Time | Tag |
|---|---|---|---|---|---|
| Yahoo | 1.617 | 1.10 / 3.22 | 39 | Oct 16 16:38 UTC | OPENED |
| Nasdaq/Zacks yearly API | 1.76 (Oct 13: 1.78) | 1.23 / 3.22 | 14 (10 down, 0 up in 4 weeks) | Oct 16 ~16:30 UTC | OPENED |
| WallStreetZen FAQ | 1.53 | 1.08 / 2.23 | not stated | page date not shown | OPENED |
| StockAnalysis | behind paywall (FY27 1.31, 38 analysts, page updated Oct 14) | | | Oct 16 | OPENED |
| MarketScreener | login wall (D1 saw 1.634 on Oct 14) | | | | blocked |

The spread across free aggregators is $1.53 to $1.76, 15% of the lowest. Zacks has only 14 estimates and 4 of them are not in the 4-week revision count, which is how stale numbers sit in a mean.

**Dispersion.** Yahoo gives only mean, low and high, no median or standard deviation. The $3.22 high is also the Zacks high and is almost certainly one stale estimate (the Oct 2 print makes a $3.22 FY28 inconsistent with the $1.15 to $1.35 FY27 guide: it needs +$1.87 of EPS in one year). Sensitivity (DERIVED): dropping a single $3.22 from 39 estimates lowers the mean from $1.617 to $1.575. The median is below the mean for any right-skewed set; I cannot compute it. See section 7.

## 3. Price target and rating moves (OPENED: Yahoo upgradeDowngradeHistory, MarketBeat, TipRanks; 2026-10-16)

- 93 Yahoo-listed actions since Jan 1 2026; 20 on Oct 2 alone. Of the Yahoo actions from Oct 2 to Oct 5, 18 lowered targets with a median cut of 18.1% (mean 18.3%) (DERIVED from `W7_broker_actions.csv`). Since Jun 30, 43 target cuts by 23 firms.
- Rating changes since Jan 2026 in the Yahoo list: 15 downgrades (Needham Jan 8; BofA and JPM Apr 1; Goldman Apr 2; Piper Apr 10; HSBC Apr 13; Wells May 8; RBC Jun 10; Evercore Jun 23; KeyBanc Jun 26; JPM Aug 4; Truist Aug 26; Baird Sep 14; BofA to Underperform Sep 25), 2 upgrades (Barclays Mar 11; Freedom Broker Oct 2), 2 initiations (BMO Underperform Sep 9, StoneX Hold Sep 22). MarketBeat adds Berenberg Hold to Sell (Oct 6, target $27.50 from $49), DZ Bank Strong-Buy to Strong Sell and Williams Trading Strong-Buy to Hold (both Oct 2), Zacks Research to Strong Sell (Oct 1).
- Targets: Yahoo financialData mean $37.67, median $34, high $94, low $19, 36 opinions (Oct 16). Nasdaq/Zacks mean target $36.41 on Oct 1 (from $74.20 on Oct 1 2025 and $62.18 Mar 1 2026), buy/hold/sell 8/17/6 in October versus 17/9/0 a year earlier. Yahoo recommendationTrend (0m): 1 strong buy, 9 buy, 25 hold, 4 sell, 3 strong sell, versus 1/11/25/1/1 three months ago.
- Last printed result: Q1 FY27 EPS $0.48 against $0.437 consensus (+9.9%); the stock-level reaction is not this note's subject.

## 4. News-reported broker FY28 numbers (see `W7_broker_fy28_news.csv` for the quoted sentences)

| Date | Firm | FY28 EPS | Source | Tag |
|---|---|---|---|---|
| Apr 1 | BofA | $2.00 (from $3.26) | sgbonline | OPENED |
| Apr 1 | Needham | $2.02 (from $2.07) | sgbonline | OPENED |
| Aug 4 | JPMorgan | $1.72, "about 20% below the Street" | Yahoo article | OPENED |
| Sep 25 | Needham | $1.80 (from $2.00) | tradingpedia | OPENED; conflicts with the Apr 1 level for the same firm |
| Sep 25 | BofA | cut 12%; level $1.87 | stocktwits/The Fly; level from one snippet | OPENED / SNIPPET; $1.87 does not reconcile with $2.00 x 0.88 = $1.76 |
| Oct 2 | BofA | cut a further 22% (FY27 -21%) | stocktwits | OPENED; level DERIVED $1.37 to $1.46 |
| Oct 6 | Berenberg | FY27 $1.08; FY28 cut 46% | parameter.io, Teleborsa | OPENED; FY28 level not published free |

Opinion, not explanation: JPMorgan's Aug 4 note called FY28 "stabilization, not recovery" (headline of the TechTimes article, SNIPPET). Only Needham and the BofA derivation give a level near or below $1.6, and they are 2 of 39 analysts. I could not find a post-print FY28 EPS level for Goldman, Citi, Evercore, Telsey, Jefferies, Bernstein or Wells (the Wells "about 25% cut to Street EPS" is a SNIPPET with no year).

## 5. Peers, same source and time (OPENED; `W7_snapshots.csv`)

Change in next-fiscal-year (+1y) EPS consensus, current versus 30 days ago and versus 90 days ago (DERIVED):

| Ticker | +1y year end | Now | vs 30d | vs 90d | Down / up revisions, 30d |
|---|---|---|---|---|---|
| NKE | May 2028 | 1.617 | -26.6% | -27.8% | 28 / 0 |
| ADS.DE (adidas) | Dec 2027 | 11.62 | -0.6% | -0.8% | 5 / 1 |
| ONON | Dec 2027 | 1.71 | +2.6% | -1.5% | 2 / 11 |
| DECK | Mar 2028 | 8.37 | +0.2% | +0.2% | 1 / 17 |
| LULU | Jan 2028 | 8.65 | -1.1% | -24.6% | 20 / 0 |
| UAA | Mar 2028 | 0.194 | -1.4% | -17.2% | 14 / 3 |
| PUM.DE | Dec 2027 | 0.272 | -12.6% | -21.0% | 6 / 1 |

Reading: NKE is the only peer with a cut of this size inside 30 days; adidas, On and Deckers are flat to rising, so the FY28 cut is company-specific, not a sector re-rating (consistent with the REPO note `competitor_benchmarks.md`, about two thirds company-specific). Lululemon and Under Armour are the useful analogs for the "what happens after" question (section 6). ADDYY (3 analysts) is a thin line and not used.

## 6. Base rates: how far does consensus keep falling after a large cut?

**Literature (OPENED abstract).** Chan, Jegadeesh and Lakonishok (1996, Journal of Finance 51(5), 1681 to 1713, RePEc abstract opened today): "Security analysts' earnings forecasts also respond sluggishly to past news, especially in the case of stocks with the worst past performance." Revisions are one of their three earnings-news measures, and "past return and past earnings surprise each predict large drifts in future returns" with "little evidence of subsequent reversals". A search summary of a follow-up says analysts keep revising down for past losers for up to 12 months (SNIPPET, source not opened). I could not open Gleason and Lee (2003) or a numeric revision-persistence table (search returned no result for Gleason and Lee; the CFA Digest copy of CJL has no numbers). So the literature gives the direction (continuation, strongest for the worst performers, which Nike is) but not a free, openable magnitude.

**Own test (DERIVED, `W7_base_rate_universe.csv`, `W7_scripts/univ.py`).** Yahoo epsTrend gives five dated points per estimate, so the test is: condition on a cut in one window, measure the next window. Panel: 249 tickers (consumer, retail, apparel, autos, plus a large-cap mix), 453 usable ticker-year observations, pulled Oct 16 2026.

| Test | Condition | n obs (distinct tickers) | Next-window result |
|---|---|---|---|
| A | cut of 15%+ from 60d to 30d ago; outcome 30d ago to now | 5 (4: COTY, OXM, LULU, DKS) | median -0.1%, mean -1.3%, none worse than -10% (worst COTY -5.2%) |
| A2 | same, threshold 10% | 10 (7) | median -0.6%, mean -1.3%, 7 of 10 negative, worst -5.2% |
| B | cut of 10%+ from 90d to 60d; outcome 60d ago to now | 12 (9) | median -1.4%, mean -1.7%, 8 of 12 negative; two of 12 at -9.4% (ACI) and -11.1% (NCLH) |
| C | cut of 15%+ from 30d to 7d ago; outcome last 7 days | 4 (3: AAL, NKE, THO) | median -1.6%, mean -2.3%, all 4 negative; NKE -2.2% |
| D | cut of 15%+ from 90d to 30d ago; outcome 30d ago to now | 13 (9) | median -1.1%, mean -2.0%, worst -9.7% (NCLH) |

Closest analogs: Lululemon cut its next-year consensus 23.7% (60d to 30d) then moved -1.1% in the next 30 days; Under Armour -13.8% then -1.4%; Coty -31.8% then -5.2%; Dick's -20.1% (current year) then -0.1%.

**What this says for NKE (DERIVED, with the sample's limits).** Following a 15% to 30% cut, the typical next-30-day move is 0% to -2%, with a rare tail of -5% to -11% (when a second event hit: NCLH, ACI). Applied to $1.617, a typical drift gives $1.58 to $1.62 by mid-November, and a tail gives $1.45 to $1.54. A move to D1 case A ($1.56) needs -3.5% (larger than the median outcome in every test, but smaller than the worst: -5.2% in tests A and A2); case B ($1.46) needs -9.7% (the tail: only 2 of 12 in test B and 1 of 13 in test D fell 9% or more); the base case ($1.17) needs -27.6%, which no observation in the panel reached after the initial cut. Caveats: n is tiny; 0y and +1y for one ticker are not independent; Yahoo's 30d window is anchored to the pull date; all events share the same market window; the panel is built from names I chose, not a random universe; and Nike's Investor Day on Nov 16 to 17 is a scheduled event that the base rates do not know about. Failing the sample test is not evidence of a cap: it only says continuation after the gap has been small on average here.

## 7. Alternatives considered and what ruled them out

| Question | Explanation tested | Result |
|---|---|---|
| Why did FY28 fall 26.6%? | (a) Pass-through of the FY27 guide cut: FY27 fell 25.1% to a level 2.1% above the guide midpoint, FY28 fell 26.6%. Survives as the main driver: parallel shift. | Survives |
| | (b) Nike-specific FY28 information (China exit, no gross margin guide): cannot be separated from (a) without a revenue-versus-margin split of the cut | Not ruled out |
| | (c) Sector-wide: adidas -0.6%, On +2.6%, Deckers +0.2% over 30 days | Ruled out |
| | (d) Pre-print drift: Jul 15 to Sep 16 only -2.9% | Ruled out as the main cause |
| | (e) Single-analyst or stale-estimate artifact: 28 of 39 analysts revised down, no up | Ruled out for the move; a $3.22 stale high affects the mean by about $0.04 |
| Split into revenue vs margin | Yahoo gives a revenue mean but no revenue history; FY28 revenue was $43,645M on Oct 13 and $43,459M on Oct 16 (-0.4%) | Cannot split the 30-day cut; the last 3 days are roughly -0.4% revenue against -1.8% EPS, i.e. the late cut is mostly margin or below-the-line |
| Is the cut still moving? | 7-day change -2.2%, 3-day -1.8%, 0 up revisions | Yes but slowing: 8% of the 30-day cut came in the last 7 days |

## 8. Routes tried and results

| # | Route | Result |
|---|---|---|
| 1 | Yahoo quoteSummary earningsTrend, earningsHistory, upgradeDowngradeHistory, financialData, recommendationTrend (crumb flow, no email in any request) for 8 tickers | Worked (current, 7, 30, 60, 90 day only; no history beyond that) |
| 2 | Yahoo epsTrend panel on 249 tickers | Worked |
| 3 | Nasdaq analyst API (earnings-forecast, targetprice, estimate-momentum, ratings) | Worked; price-target history monthly |
| 4 | MarketBeat price-target page | Worked (actions to Oct 9) |
| 5 | TipRanks forecast page | Worked partial (actions to Oct 14, no FY28 EPS) |
| 6 | WallStreetZen forecast page | Worked partial (undated mean/high/low, per-analyst rows locked) |
| 7 | StockAnalysis forecast page | Partial (FY28 paywalled) |
| 8 | MarketScreener | Blocked (login wall) |
| 9 | Zacks detailed estimates | Blocked (bot interstitial); Nasdaq/Zacks API used instead |
| 10 | Investing.com earnings page | Empty (forecast fields blank) |
| 11 | Wayback Machine for Yahoo analysis page (availability API) | No snapshots; CDX endpoint unreachable |
| 12 | CNBC Oct 2 and StreetInsider articles | HTTP 403 |
| 13 | Stocktwits Citi article | HTTP 405 |
| 14 | News search for FY28 broker EPS (8 queries) | Worked partial: 7 firm numbers (section 4) |
| 15 | I/B/E/S, FactSet, Visible Alpha | Not available (paid) |

**Inconclusive items, with at least five different routes each:** (i) FY28 median and standard deviation: routes 1, 3, 6, 7, 8, 9 failed, because no free page publishes them. Needed: any I/B/E/S, FactSet or Visible Alpha detail download (per-analyst FY28 EPS), or the Refinitiv pull list item 1. (ii) FY28 consensus history before Jul 15 and daily path Oct 1 to Oct 16: routes 1, 3, 11, 14 failed. Needed: I/B/E/S estimate history (Refinitiv pull list priority 1). Workaround for the future: re-run `W7_scripts/pull.py` daily to build the daily series from today. (iii) Per-analyst post-print FY28 levels: routes 4, 5, 6, 12, 13, 14 gave 3 percentages and 3 levels only.

## 9. Method and verification notes

- Yahoo `7daysAgo` and `30daysAgo` are offsets from the pull time, so the 7d and 30d values in the Oct 13 and Oct 16 pulls refer to different calendar dates; `W7_nke_consensus_path.csv` labels each by its implied date (approximate to one day).
- Peer percentages in section 5 are DERIVED from `W7_snapshots.csv` (e.g., NKE 1.617/2.202 - 1 = -26.6%).
- Yahoo `price` on Oct 16 was $37.435; forward P/E on FY28 is 23.2x at $1.617 (DERIVED), against 21.5x at $35.35 and $1.646 in the REPO note.
