# Is the NKE short too crowded to pitch?

Written 2026-10-14. Stock $35.35 (NKE close 2026-10-12; Yahoo chart, OPENED). Submission Nov 1, finals Nov 19, Investor Day Nov 16 to 17.

Tags: OPENED = we read the source or API response ourselves; SNIPPET = search summary only; REPO = earlier work in this repo (branch `origin/claude/wonderful-franklin-u31n4e`, `research_notes/17_insider_and_institutional_flows.md` and `data/flows/`); DERIVED = our arithmetic on opened data. Data and scripts: `data/hunt/risk_short_interest/`.

## 1. Verdict

**Crowding is a weak argument against the SHORT. It does not flip the call. Strength of this conclusion: moderate.**

- **The number is a record for Nike, but it is not a crowded short by the usual measures.** 99.2M shares short is 8.24% of the Class B float, the highest in the FINRA series back to Dec 2017 and about 4x to 8x Nike's 2018 to 2024 normal of 0.6% to 2.4%. But days to cover is only 2.6 to 3.1, borrow costs 0.41% a year with 10M+ shares free to borrow at Interactive Brokers, and among 30 US consumer large caps above $20B only Kimberly-Clark is more shorted, and that is merger arbitrage.
- **History says record short interest in consumer stocks did not mark the bottom.** Across 27 US consumer names, 2021 to 2026, a record short interest print (at least 4% of shares) was followed by a median return vs SPY of -0.4% after 13 trading days, -4.3% after 3 months, -10.6% after 6 months and -9.3% after 12 months. Shorts won 53%, 58%, 68% and 63% of the time at those horizons. The losses came from a fat right tail: 10% to 18% of cases ran more than 25% above SPY at 3 to 12 months.
- **For the Nov 1 to Nov 19 window it is a coin flip with event risk.** At 13 trading days (about the length of the pitch window; Nov 2 to Nov 19 is 14 sessions), only 7 of 165 record prints (4%) beat SPY by more than 15%, and the biggest ones were earnings-day gaps (Burlington Nov 2022, Lululemon Dec 2024). Nike has no earnings in the window, but Investor Day on Nov 16 to 17 plays the same role. The Nov 20 options straddle prices a 9.5% move (REPO, Oct 13).
- **Nike's own last record is the warning and the reassurance.** After the April 2025 record (50.4M), NKE beat SPY by 22% over the next 3 months (June 2025 earnings rally), then lagged it by 51% over 12 months.

**How to use it in the pitch:** keep the SHORT, but (1) say the short is a record and show why it is not a squeeze setup (low days to cover, cheap borrow, no takeover tail); (2) express it with puts or a defined-risk structure through Investor Day, because skew is flat (REPO) and the event gap is the only real squeeze mechanism; (3) treat a falling short interest print with a flat or rising price (Oct 15 and Oct 31 prints, published about Oct 24 and Nov 10) as the warning sign.

## 2. Short interest history (FINRA)

Source: FINRA consolidated short interest API, symbol NKE, 211 twice-monthly prints from 2017-12-29 to 2026-09-30 (api.finra.org, fetched 2026-10-14, OPENED). Class B and Class A counts are 10-K and 10-Q cover values in `data/nike_filing_facts.csv` (REPO from SEC filings). File: `data/hunt/risk_short_interest/nke_short_interest_2017_2026.csv`.

**Which denominator.** Class A (281.4M shares) cannot trade and 78.8% of it sits with Swoosh, LLC (REPO, note 17). The traded float is Class B: 1,203,921,077 shares (Q1 FY27 10-Q cover, filed 2026-10-02, REPO). Yahoo's float field is 1,178,458,878 (Yahoo quoteSummary, 2026-10-14, OPENED), which strips out about 25M insider-held Class B shares.

| Measure (2026-09-30 print) | Value | Source |
|---|---|---|
| Short shares | 99,243,778 | FINRA, OPENED |
| % of all shares (A + B, 1,485.3M) | 6.68% | DERIVED |
| % of Class B (1,203.9M) | 8.24% | DERIVED |
| % of Yahoo float (1,178.5M) | 8.42% | DERIVED |
| Yahoo "short % of float" field | 10.38% (implies a 956M float; we cannot reproduce it) | Yahoo quoteSummary, 2026-10-14, OPENED |
| Days to cover, FINRA's ADV (38.3M) | 2.59 | FINRA, OPENED |
| Days to cover, Yahoo 20-day ADV to Sep 30 (33.8M) | 2.94 | DERIVED from Yahoo volume |
| Days to cover, Yahoo 63-day ADV to Sep 30 (26.4M) | 3.76 | DERIVED |
| Days to cover, 20-day ADV to Oct 13 (48.0M, includes results days) | 2.07 | DERIVED |
| Short value | $3.51B at $35.40 | DERIVED |

Third-party estimates, which use their own methods: S3 Partners 87M shares, "all-time high", SI % of float "from below 3% to above 7%", shorts "persistently added exposure as NKE shares declined", $1.4B mark-to-market gains in 2026 (s3partners.com, 2026-09-29, OPENED). Ortex 94.7M, 8.0% of free float, cost to borrow 0.53%, availability "tightened from 621% to 546%" (ortex.news, 2026-09-28, OPENED). MarketBeat 6.76% "of float" on 1,485.31M shares (marketbeat.com, Oct 2026, OPENED). The 6.7% figure in the scoreboard uses all shares; the right float figure is about 8.2% to 8.4%.

**The path, % of Class B (yearly range, DERIVED):**

| Year | Low | High | Median days to cover (Yahoo 20d) |
|---|---|---|---|
| 2018 | 0.79% | 2.26% | 2.2 |
| 2019 | 0.58% | 0.86% | 1.4 |
| 2020 | 0.70% | 1.13% | 1.6 |
| 2021 | 0.62% | 1.14% | 1.8 |
| 2022 | 0.64% | 1.43% | 1.7 |
| 2023 | 0.84% | 1.53% | 1.9 |
| 2024 | 1.13% | 2.36% | 1.9 |
| 2025 | 2.45% | 4.28% | 2.7 |
| 2026 (to Sep 30) | 3.29% | 8.24% | 2.8 |

Recent prints: 57.4M (Jul 31) to 68.8M (Aug 14), 75.6M (Aug 31), 85.7M (Sep 15), 99.2M (Sep 30), five rises in a row and +73% in two months (FINRA, OPENED; DERIVED). Days to cover never exceeded 4.88 (FINRA, 2025-08-15) or 4.12 on our 20-day measure (2025-08-29). Volume has grown with the short, so days to cover has stayed flat while the share count went up 7x.

**The Sep 30 print is pre-results.** Nike reported on Oct 1. Volume on Oct 1 and Oct 2 was 112.4M and 142.7M shares, 2.6x the whole short position (Yahoo chart, OPENED). The stock went $35.40 (Sep 30) to $33.87 (Oct 2) and back to $35.35 (Oct 12). No squeeze, and no big win for shorts either. The Oct 15 print (published about Oct 24) is the first look at what shorts did after results.

**FINRA daily short sale volume** (Reg SHO CNMS files, cdn.finra.org, Oct 2025 to Oct 13, 2026, OPENED; `daily_short_volume.csv`). Short sale volume ran 39% to 50% of FINRA-reported volume each month, with Oct 1 at 61.9% and Oct 2 at 54.3%. Treat this with care: it counts every short sale, including market makers that cover the same day. A 40% to 50% ratio is normal for liquid large caps. It does not show positions and adds little here.

## 3. Cost and squeeze mechanics

| Item | Value | Source |
|---|---|---|
| Borrow fee (Interactive Brokers) | 0.41% a year; 0.28% to 0.41% since Oct 3 | ChartExchange borrow page (IBKR feed), 2026-10-14, OPENED (`raw/chartexchange_borrow_NKE_2026-10-14.html`) |
| Shares available to borrow at IBKR | 10,000,000 (the feed's cap) on most updates; low of 4.3M on Oct 3 after results | same, OPENED |
| IBKR rebate on short proceeds | 3.47% | same, OPENED |
| Ortex cost to borrow | 0.53% (Sep 28) | ortex.news, OPENED |
| iborrowdesk, Fintel | iborrowdesk returned an empty page; Fintel returned HTTP 403 | tried 2026-10-14 |
| Utilization | not available from a free source; Ortex "availability 546%" implies lendable supply about 5x the short | ortex.news, OPENED |
| Dividend | $0.41 a quarter, $1.64 a year, 4.64% yield | Yahoo summaryDetail, 2026-10-14, OPENED; ex-dates about Dec 1, Mar 1, Jun 1, Sep 1 (REPO) |
| Options skew, 90% put vs 110% call IV | +0.4 pts (Nov 20), +1.3 (Dec 18): flat | REPO, Yahoo chain 2026-10-13 |
| Nov 20 straddle (covers Investor Day) | 9.54% of spot; 1-sd range $31.53 to $40.11; risk-neutral P(>$45) 2.2% | REPO |
| Put/call open interest, all expiries | 0.67 (inflated by stale far out-of-the-money calls) | REPO |

What it means:
- **Borrow is general collateral.** 0.41% is the standard rate for easy-to-borrow large caps. Squeezes need borrow to get scarce (fees in double digits, utilization near 100%). There is no sign of that.
- **The dividend matters for the 12-month case, not the pitch window.** No ex-date falls between Nov 1 and Nov 19, so a short held over the competition pays nothing. Over 12 months a short pays 4.64% in dividends plus 0.41% in borrow, about 5.05% gross. Against that, an institutional short earns interest on the cash proceeds (IBKR's rebate is 3.47%), so the net carry is about 1.6% a year (DERIVED). The adjusted prices in our event study already charge shorts the dividends.
- **The dividend declaration in mid-November is a two-way catalyst.** Option prices imply dividends about 45% to 60% below the $0.41 rate (REPO, put-call parity, partly model bias). A cut would hurt longs and lower the carry for shorts. Holding the dividend could be read as confidence and set off covering.
- **How fast shorts could cover.** At 32M shares a day (Yahoo 63-day ADV to Oct 13) and shorts taking 25% of volume, covering all 99.2M takes about 12 trading days (DERIVED). That is real buying pressure over a two-week window, but it is the same size as the window, not several times it. In the classic squeezes in our sample (Kohl's, Advance Auto, Gap), short interest was 11% to 31% of shares.
- **No takeover tail.** Swoosh, LLC controls the Class A vote that elects most of the board (REPO, note 17; 2026 proxy: Class A elects 8 directors, Class B elects 3, `nike_filing_facts.csv`). The takeover-premium squeezes that hurt shorts elsewhere cannot happen at Nike without the Knight family.
- **No convertible bonds.** So there is no convertible arbitrage short, which can unwind all at once. Part of the short is market makers hedging options; the 13F put total was 77.7M underlying at Jun 30, 2026, held mainly by Susquehanna, Citadel and Jane Street (REPO). The data cannot separate hedges from outright short bets.

**Cross-section, short % of shares (Yahoo quoteSummary, 2026-10-14, OPENED; DERIVED; `yahoo_keystats_2026-10-14.csv`).** Across 56 other US consumer names the median is 5.25%. 17 are above Nike's 8.24% (Kohl's 27.4%, Wendy's 25.6%, Advance Auto 18.5%, Kimberly-Clark 16.0%, Under Armour A 15.2%, Etsy 14.3%, Lululemon 13.3%, Macy's 12.7%, among others). Among the 30 above $20B market cap the median is 3.0%, and only Kimberly-Clark (16.0%, Kenvue deal arbitrage) is above Nike. Median Yahoo days to cover is 3.95; Nike's is 3.03. Note that Yahoo uses each company's own share basis, so the comparison is approximate. **Conclusion: high for a mega-cap, ordinary for a fallen consumer brand, and low on days to cover.**

## 4. Evidence from history

### 4a. Event study: what happened after record short interest

Method (`scripts/event_study.py`). FINRA short interest for 63 US consumer tickers (2017-12 to 2026-09, OPENED), daily adjusted closes from the Yahoo chart API (OPENED; dividends included, so shorts are charged the dividend). An event is a print where short shares exceed every earlier print since Dec 2017, with at least three years of history before it (so events start in 2021), and short interest is at least 4% of shares outstanding (SEC XBRL cover-page counts, OPENED; Yahoo current counts for multi-class issuers). We adjust for the CMG, DECK, WMT and TSCO stock splits. Entry is the first close at least 10 days after settlement, roughly FINRA's publication date, so there is no look-ahead. Returns are measured against SPY. An "episode" is the first record print after at least 126 trading days without one.

**Results (DERIVED, `summary_min4.txt`; negative = short wins):**

| Set | n | 13 days | 3 months | 6 months | 12 months |
|---|---|---|---|---|---|
| All record prints, SI at least 4% | 174 (27 names) | median -0.4%, shorts win 87/165 | -4.3%, 90/154 | -10.6%, 81/119 | -9.3%, 57/90 |
| Episode starts only | 37 | +0.1%, 18/36 | -4.1%, 22/36 | -11.6%, 22/32 | -27.4%, 18/25 |
| Episode starts, stock at least 40% below 3-year high | 22 | +0.7%, 10/22 | -5.6%, 13/22 | -10.9%, 14/20 | -26.9%, 11/15 |
| Nike-like: record, at least 40% below high, days to cover under 4 | 56 (15 names) | -1.1%, 30/52 | -3.5%, 27/49 | -6.0%, 27/38 | -5.5%, 16/30 |
| No minimum SI level | 249 (36 names) | -1.1%, 138/238 | -4.6%, 139/224 | -10.6%, 127/183 | -16.2%, 103/140 |

Tails, all record prints at 4% or more: more than 15% above SPY in 7/165 cases at 13 days, 30/154 at 3 months, 18/119 at 6 months and 16/90 at 12 months; more than 25% above in 2, 16, 14 and 16 cases. Mean returns are close to zero at 13 days to 3 months even though medians are negative: most outcomes favor shorts, and a few large squeezes cancel them out.

Which names produced the big squeezes: at 12 months, Advance Auto, Kohl's, Dollar General, Gap, Tapestry and VF. Most had short interest well above Nike's (Kohl's 31%, Advance Auto 11% to 22%, Gap 11%, VF 9.5% to 12.9%, Tapestry 9.8% of shares); Dollar General (4.1%) is the exception, a turnaround that took hold. At 13 days: Burlington (+20.5% on 2022-11-22, its earnings day), Lululemon (+15.9% on 2024-12-06, the day after earnings), VF (+14.0% on 2023-10-17), Advance Auto, Etsy, Gap and Conagra (Yahoo chart, OPENED; DERIVED).

**Caveats.** (1) Survivorship: Yahoo has no prices for Skechers, Foot Locker, Walgreens and Hanesbrands, whose FINRA series stop in 2025 (FINRA, OPENED); all four were heavily shorted and taken over. Leaving them out flatters shorts, but takeovers are not possible at Nike, so for Nike the bias matters less. (2) Events cluster in the 2022 to 2023 retail bear market and the 2025 to 2026 consumer slump. (3) 27 names is a small sample, and repeated prints from one stock are not independent.

### 4b. Named cases (DERIVED from FINRA and Yahoo, OPENED)

| Stock | Record print (settle) | SI % of shares | 13 days | 3 months | 6 months | 12 months | What happened |
|---|---|---|---|---|---|---|---|
| **Nike** | 2025-02-14 (33.5M) | 2.8% | -1.4% | -22.1% | -8.5% | -36.6% | Shorts won |
| **Nike** | 2025-04-15 (50.4M) | 4.3% | +0.4% | **+22.4%** | -2.3% | -50.6% | Squeeze on Jun 2025 results, then shorts won big |
| **Nike** | 2026-04-15 (56.1M) | 4.7% | -11.5% | -7.6% | n/a | n/a | Shorts winning so far |
| Lululemon | 2024-11-15 | 5.5% | **+18.8%** | +12.1% | -2.3% | -59.4% | Earnings squeeze, then -59% |
| Lululemon | 2025-02-28 to 03-31 | 5.8% to 6.4% | -15% to +1% | -30% to -36% | -60% to -67% | -68% to -73% | Shorts won |
| VF Corp | 2022-05-31 to 2023-02-15 | 4.1% to 6.1% | -11% to +6% | -12% to -36% | -31% to -40% | -59% to -73% | Shorts kept winning for two years |
| VF Corp | 2024-04-15 to 05-31 | 9.5% to 12.9% | -2% to +9% | +22% to +39% | +17% to +55% | -17% to +7% | The final peak marked the bottom |
| Estee Lauder | 2025-06-30 | 5.8% | -2.3% | -3.5% | +9.8% | -31.6% | Mixed, then shorts won |

Target, Starbucks and Under Armour had no record print after 2021: their highest short interest came in 2018 (Target Jan 2018 47.0M, Starbucks Oct 2018 87.3M, Under Armour A Mar 2018 67.7M at 12.8 days to cover). Over the following 12 months Target was -2.5% vs SPY, Starbucks +30.0% and Under Armour +12.3% (`peak_cases.csv`, DERIVED).

### 4c. Records versus the final peak

The pattern that reconciles "record short interest marks bottoms" with the numbers above: **the last, highest print often did mark the bottom** (after their series-high prints, Starbucks Oct 2018, Under Armour Mar 2018, Kohl's May 2025 and Crocs Sep 2018 beat SPY over both the next 6 and 12 months, and VF May 2024 beat it by 49% over 6 months before fading to -16% at 12 months; `peak_cases.csv`). But **you only know which print was the last one afterwards.** Judged at the time, a new record was more often followed by further losses (63% to 68% short win rate at 6 to 12 months). The thing to watch is short interest turning down while the price holds. For Nike that means the Oct 15 and Oct 31 prints.

## 5. Who is short, who is buying

**Short side (no named short seller found).**
- No 13F or fund letter naming a large NKE short was found. 13F filings do not report shorts; the 13F put holders are market makers (Susquehanna 17.4M, Citadel 14.4M, Jane Street 14.0M underlying), then Marshall Wace 3.3M, Millennium 3.3M and D. E. Shaw 3.1M (13F, Jun 30, 2026, REPO). The search "Nike short seller fund letter 2026" returned only data-vendor coverage (WebSearch, 2026-10-14, SNIPPET).
- S3 Partners: shorts "persistently added exposure as NKE shares declined" (2026-09-29, OPENED). Yahoo Finance's Brian Sozzi, "Nike stock has never been more hated by the market" (2026-09-29, OPENED).
- Sell side after the Oct 1 results: Berenberg cut to sell, target $27.50 from $49 (MarketBeat, 2026-10-07, OPENED, citing Barron's); DZ Bank strong-buy to strong sell (Oct 2); Goldman neutral, $30 from $38; UBS neutral, $34 from $42; HSBC hold, $40 from $48 (Sep 28) (all MarketBeat, OPENED). Consensus: 1 strong buy, 7 buy, 21 hold, 10 sell, average target $41.19, "Reduce" (MarketBeat, OPENED). Citi $32, JPMorgan $33, Deutsche $33 (WebSearch, SNIPPET). Ten sell ratings on a mega-cap means the bear case is now the consensus view.

**Long side.**
- Capital Group (three 13F filers) went from 40.2M shares (Dec 2024) to 84.9M (Jun 2026), 7.05% of Class B, nearly the size of the whole short position. New in Q2 2026: Sixth Street 12.4M, Jupiter Topco 5.0M, Marshfield 4.3M, Cable Car 2.3M; Harris/Oakmark 14.4M since Q2 2025 (13F, REPO). Q3 13Fs are due Nov 16, the day Investor Day starts.
- Insiders: 10 discretionary open-market buys plus one plan buy from 2024 to 2026, $9.11M in total, all now under water (Form 4, REPO). No Form 4 purchase has been filed since the Oct 1 results: the latest Nike filing on EDGAR is a 2026-10-05 Form 144 by former CFO Matthew Friend to sell (EDGAR submissions JSON, fetched 2026-10-14, OPENED).

The holder base is passing from growth and quality funds to value funds, and the short has grown alongside it. Both sides are big. The longs are long-horizon funds that do not need to sell on bad news. The shorts can cover cheaply and quickly.

## 6. Catalysts that could force covering

| Date (2026) | Event | Squeeze risk |
|---|---|---|
| About Oct 24 | FINRA Oct 15 print (first after results) | A big drop with the price holding = shorts leaving; less fuel, but a sign the bottom may be in |
| About Nov 10 | FINRA Oct 31 print | Same |
| About Nov 10 | Feng Tay October sales | A turn up would be the first fundamental reason to cover |
| Mid-Nov | Dividend declaration (ex-date about Dec 1) | Holding $0.41 = confidence signal; a cut = bear signal |
| Nov 16 | Q3 13F deadline | Shows whether Capital Group and Sixth Street added below $40 |
| **Nov 16 to 17** | **Investor Day** | The main gap risk inside the pitch window. Nov 20 straddle 9.5%. A FY28 frame at or above consensus ($1.65 EPS) with a margin target above about 9% is the squeeze trigger |
| About Dec 17 | Q2 FY27 results | After the finals |

## 7. Answer to the question

| Question | Answer | Points to | Strength |
|---|---|---|---|
| Is crowding a real threat to a SHORT over Nov 1 to Nov 19? | Only through an event gap at Investor Day. Mechanically there is no squeeze setup: 2.6 to 3.1 days to cover, 0.41% borrow, plentiful lendable supply, no dividend ex-date in the window, no takeover route. History: 13-day outcomes after record prints are a coin flip (median -0.4%), with a gain of more than 15% in about 4% of cases. | NEUTRAL for the window | Moderate |
| Over 6 to 12 months? | Record short interest in consumer names was followed more often by further losses (median -10.6% at 6 months, -9.3% at 12 months vs SPY; shorts win 63% to 68%), but about 1 in 6 ended up more than 25% above SPY at 12 months, mostly names with far higher short interest (about 10% to 31% of shares). | Slightly SHORT (base rates), with a fat right tail | Moderate |
| Is 8.2% of float normal for a large cap? | No: it is a Nike record and the highest among consumer names above $20B except merger arbitrage. But days to cover is below the peer median, and against fallen consumer brands it is middle of the pack. | Not a LONG argument on its own | Moderate |

**Net:** crowding should be presented as a known risk and managed through position structure, not as a reason to go LONG. If the Oct 15 or Oct 31 print shows short interest falling while the stock holds or rises, upgrade this risk, because that is how the final peak (the bottom) looked for VF, Starbucks and Under Armour.

## 8. Files

`data/hunt/risk_short_interest/`
- `scripts/pull_finra_si.py` (FINRA short interest API), `scripts/pull_prices.py` (Yahoo chart), `scripts/pull_shares.py` (SEC XBRL cover counts), `scripts/pull_yahoo_stats.py` (Yahoo key stats), `scripts/pull_daily_short_volume.py` (FINRA Reg SHO daily files), `scripts/nke_si_history.py`, `scripts/event_study.py [min_pct]`, `scripts/peak_cases.py`, `scripts/options_snapshot.py` (Yahoo returned empty IV and open interest before the open on Oct 14; we used the REPO Oct 13 chain instead)
- `si_all.csv` (63 tickers, FINRA), `prices_all.csv`, `shares_all.csv`, `yahoo_keystats_2026-10-14.csv`, `daily_short_volume.csv` (NKE, LULU), `nke_short_interest_2017_2026.csv`
- `events_min{0,4,6}.csv`, `episodes_min{0,4,6}.csv`, `summary_min{0,4,6}.txt`, `peak_cases.csv`
- `raw/` (API responses, about 23 MB; not needed to rerun the analysis once the CSVs exist)
