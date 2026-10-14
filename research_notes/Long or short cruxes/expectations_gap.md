# Crux: Are Wall Street expectations for Nike still too high, or now too low?

Prepared 2026-10-14. Reference price $35.35 (close 2026-10-12); Yahoo showed $35.33 on the 2026-10-14 fetch.

Labels:
- OPENED: fetched and read in this session.
- REPO: taken from this repo, not re-fetched. The file is named.
- SNIPPET: a search-result summary only; the page was not opened.
- [arith]: my own simple arithmetic.

Raw downloads are in the session scratchpad under `expgap/dl` and `expgap/sec`; they are not committed.

## 0. Pre-registered decision rules (written before any new data was gathered)

**Points SHORT (consensus above what the evidence supports):**
- S1. The Q2 FY27 revenue consensus is less negative than a bottom-up build from Nike's own Q1 run rate and the 400 bps Q2 headwind.
- S2. FY27 consensus EPS sits in the upper half of the $1.15 to $1.35 guide, or FY27 revenue sits at the shallow end of "high single digit decline".
- S3. FY28 consensus assumes a revenue recovery or margin rebound that contradicts management's own timing (pressure "into fiscal '28"; Pace savings mostly in FY29 to FY30).
- S4. Revisions are still falling one to two weeks after the print, so the published mean has not caught up.
- S5. At past Nike resets, the stock kept falling after the first cut, because the first guide was too high.

**Points LONG (consensus already below the evidence):**
- L1. The Q2 consensus is more negative than the bottom-up build.
- L2. FY27 consensus EPS is at or below the guide midpoint, and the new CFO has a record of setting initial guides low and then beating.
- L3. FY28 consensus already assumes little or no revenue recovery.
- L4. The stock shrugged off the cut, meaning the price was already set below sell-side numbers.
- L5. Past investor days, or first-guide resets by this CFO, were followed by positive drift.

**Neutral:** the evidence scores both ways, or the gap is small relative to normal estimate error.

## 1. Answer

**NEUTRAL (strength: moderate).** No exploitable expectations gap exists for the period that matters before finals (Nov 19). A modest, visible gap does exist for FY28.

**Q2 FY27 and FY27: consensus matches the evidence.**
- Q2 FY27 revenue consensus is $11,176M (-10.1%). My bottom-up build from Nike's own data gives -9.1% to -11.1% (central about -10%).
- FY27 EPS consensus is $1.26 to $1.29, against a guide midpoint of $1.25.
- FY27 revenue consensus (-7.0%) sits at the shallow end of the guide. That leans SHORT, but only by about $0.4B.

**FY28: consensus is still too high.**
- Consensus is EPS $1.65, revenue +1.1%, EBIT margin 7.3% (from 5.7%).
- Two simple scenarios based on the evidence give $1.38 to $1.53, about 7% to 16% below consensus.
- Revisions are still flowing down: FY28 fell from 1.78 to 1.65 in the last 7 days.

**The price has not followed the sell-side numbers.**
- FY27 EPS consensus was cut about 25%, yet the stock fell only 3.6% the next day and recovered fully within 7 sessions.
- Before the print, buy-side expectations were already about $1.50, versus sell-side $1.61 to $1.71 (Piper Sandler, SNIPPET relay).
- Options price only about a 3.6% Investor Day move.

**New CFO Denton's record with first guides is mixed.**
- Pfizer: two low initial guides were beaten by 46% and 11%.
- Lowe's: the FY2019 initial guide was missed by about 5%.

**Implication for the pitch.** "Consensus is too high" is not a strong SHORT argument on its own: the FY27 bar is fair and the FY28 gap is small, known and partly priced in. "The bar is now too low" is not a LONG argument either: FY27 numbers sit at, not below, the evidence.

## 2. Data tables

### 2.1 Current consensus (fetched 2026-10-14 unless marked)

| Item | Q2 FY27 (Nov-26) | Q3 FY27 | FY27 | FY28 | FY29 |
|---|---|---|---|---|---|
| EPS mean, Yahoo (n) | 0.381 (26), range 0.29 to 0.54 | 0.265 (26) | 1.288 (35), range 1.01 to 1.69 | 1.646 (39), range 1.10 to 3.22 | n/a |
| EPS mean, Nasdaq/Zacks (n) | 0.39 (12) | 0.30 (11) | 1.26 (11), range 1.13 to 1.69 | 1.78 (14), range 1.23 to 3.22 | 2.31 (6) |
| EPS, MarketScreener | n/a | n/a | 1.288 | 1.646 | 2.07 |
| Revenue mean, Yahoo ($M) | 11,176 (-10.1%), range 10,813 to 11,968 | 10,403 (-7.8%) | 43,152 (-7.0%) | 43,645 (+1.1%) | n/a |
| Revenue, MarketScreener ($M) | 11,176 | 10,403 | 43,152 | 43,645 | 45,308 (+3.8%) |
| EBIT, MarketScreener ($M, margin) | 769 (6.9%) | 517 (5.0%) | 2,479 (5.74%) | 3,179 (7.28%) | 4,039 (8.91%) |
| Net income, MarketScreener ($M) | 577 | 402 | 1,916 | 2,418 | 3,018 |

- MarketScreener quarterly revenue for FY27 Q4 is 10,175 (-7.3%).
- MarketScreener FY28 quarterly revenue is 10,994 / 11,233 / 10,560 / 10,403, which is y/y -2.0% / +0.5% / +1.5% / +2.2% [arith].
- The FY27 quarterly sum is 42,967, versus an annual mean of 43,152, a small inconsistency inside MarketScreener.

Sources:
- Yahoo quoteSummary earningsTrend, fetched 2026-10-14 (OPENED, file `expgap/dl/qs_NKE_1014.json`).
- Nasdaq earnings-forecast and estimate-momentum APIs, Zacks-sourced, asOf null, fetched 2026-10-14 (OPENED).
- MarketScreener finances page via WebFetch, 2026-10-14 (OPENED; the page shows no update date).

**Gross margin consensus:** I found no free source. The implied Q2 FY27 GM from MarketScreener EBIT of 769 is 41.2% to 41.9%, against 40.6% LY [arith]. The range comes from assuming Q2 SG&A down 3% to 5% from Q2 FY26's about $4,039M (GP 5,045 less EBIT 990 less other 16; REPO `data/nike_filing_facts.csv`).

So consensus embeds Q2 GM up about 60 to 130 bps. That is consistent with:
- Q1 FY27 GM up 60 bps (REPO);
- lapping the -360 bps tariff hit in Q2 FY26 (REPO, `gm_driver_product_cost_tariff_bps`), partly offset by the Section 122 replacement tariffs (REPO cross-branch notes: 10% from Feb 24, 2026, and 15% from August in Nike's plan).

### 2.2 How revisions moved (Yahoo epsTrend, 2026-10-14, OPENED)

| Period | 90 days ago | 30 days ago | 7 days ago | Now | Down revisions (7d / 30d) |
|---|---|---|---|---|---|
| Q2 FY27 EPS | 0.534 | 0.523 | 0.398 | 0.381 | 18 / 1 (as published) |
| Q3 FY27 EPS | 0.434 | 0.432 | 0.292 | 0.265 | 1 / 15 |
| FY27 EPS | 1.731 | 1.712 | 1.356 | 1.288 | 24 / 2 |
| FY28 EPS | 2.267 | 2.221 | 1.780 | 1.646 | 24 / 23 |

- Zacks: FY27 1.69 a month ago, 1.26 now, unchanged over the past week; Q2 0.53, then 0.40, then 0.39 (OPENED).
- Pre-print FY27 consensus:
  - EPS $1.61 (Nasdaq, 13 estimates, range 1.42 to 1.75);
  - revenue $45.31B, about -2% (LSEG via CNBC);
  - Q1 LSEG $0.43 EPS and $11.32B revenue (actual $0.48 and $11.21B).
  - Source: StockTitan, 2026-10-01, updated 2026-10-05 (OPENED).
- Since Oct 1, the FY27 EPS mean is down about 25% and the revenue mean about $2.2B [arith].
- FY27 has nearly stopped moving (Zacks flat over the week). FY28 is still moving: -7.5% in the latest 7 days.
- Stale highs remain: FY27 high 1.69 is above the top of the guide, and FY28 high 3.22. The published means will keep drifting lower as laggards update. This mechanical drift is not new information.

### 2.3 Broker actions after the print (Yahoo upgradeDowngradeHistory, OPENED)

| Date | Firm | Rating | Target (old to new) |
|---|---|---|---|
| Oct 2 | JPMorgan | UW | 40 to 33 |
| Oct 2 | Goldman | N | 38 to 30 |
| Oct 2 | BofA | U/P | 30 to 24 |
| Oct 2 | Morgan Stanley | UW | 31 to 27 |
| Oct 2 | Truist | Hold | 42 to 29 |
| Oct 2 | Wells Fargo | EW | 40 to 30 |
| Oct 2 | Piper | N | 38 to 28 |
| Oct 2 | Evercore | In-Line | 34 to 28 |
| Oct 2 | Citi | N | 39 to 32 |
| Oct 2 | UBS | N | 42 to 34 |
| Oct 2 | Telsey | MP | 44 to 35 |
| Oct 2 | Baird | N | 44 to 36 |
| Oct 2 | Stifel | Hold | 40 to 36 |
| Oct 2 | BNP | U/P | 23 to 19 |
| Oct 2 | Guggenheim | Buy | 60 to 50 |
| Oct 2 | BTIG | Buy | 55 to 50 |
| Oct 5 | Barclays | OW | 48 to 37 |

- Mean target $38.04; median $34.40 (36 analysts).

Analyst detail:
- **Piper Sandler** (Investing.com, 2026-10-02, OPENED): FY27 sales cut to -9%; Q2 FY27 sales -11% and EPS $0.39. The guide was "below the firm's sense of buy-side expectations around $1.50".
- **Bernstein** (Investing.com, 2026-10-02, OPENED): guidance "roughly 25% below Street expectations". Management "promised to present a five-year algorithm" at the November investor day, and "not much will change until then".
- **BofA** cut FY27 and FY28 EPS by 21% and 22% (SNIPPET).
- **Stifel** cut FY27 and FY28 EPS by $0.20 each and said Investor Day gives little reason to raise expectations (SNIPPET).

### 2.4 What Nike's own guide implies for Q2 FY27 (Q1 FY27 call transcript, Oct 1, 2026, OPENED, Nike PDF in scratchpad)

What Nike said on the call:
- No numeric Q2 guide.
- Quote: "in the second quarter, we are also lapping significant promotional activities in EMEA from Cyber Week and a higher comparison of North America sell-in activities versus last year. These 2 items will represent a headwind of approximately 400 basis points to revenues in the second quarter."
- Denton: "if you look sequentially quarter-over-quarter, you will see because of that comparison, growth rates being pressured in Q2."
- FY27: "revenues to decline in the high single-digit range"; "EBIT to decline by a greater percentage than revenue"; "SG&A to remain down year-over-year"; adjusted EPS $1.15 to $1.35, which excludes about $0.15 for Pace.
- Pressure on reported revenue "for the remainder of fiscal '27 and into '28".
- Pace: about $2.5B of savings, "majority of the program savings to be realized in fiscal years '29 and '30". Nike intends to "reinvest a portion".

**Bottom-up Q2 build [arith].** Base is Q2 FY26 revenue of $12,427M, with segments from REPO `data/nike_filing_facts.csv`.

Q1 FY27 segment y/y:

| Segment | Q1 FY27 y/y |
|---|---|
| NA | +2.1% |
| EMEA | -4.7% |
| Greater China | -22.0% |
| APLA | -1.8% |
| Converse | -28.1% |

Excluding China and Converse, Q1 was -0.7%.

Method A (Q1 ex-China/Converse run rate):
- Start from -0.7%.
- Less the 400 bps item, which is about $497M or 4.6 pts of the ex-China/Converse base.
- Less 1 to 2 pts of World Cup fade.
- Plus China at -25% to -35%: management guided China worse than Q1 for the balance of the year (REPO `china_floor.md`, OPENED transcript).
- Plus Converse at -30%.
- Result: $11,050M to $11,299M, which is **-9.1% to -11.1%**.

Method B (segment ranges):

| Segment | Assumed Q2 y/y |
|---|---|
| NA | -4% to -10% |
| EMEA | -6% to -12% |
| Greater China | -25% to -35% |
| APLA | -2% to -6% |
| Converse | -25% to -35% |

Result: $10,754M to $11,534M, which is -7.2% to -13.5%.

Consensus: $11,176M (-10.1%); Piper -11%. **The consensus sits in the middle of the evidence-based range.** Neither S1 nor L1 holds.

Factory and channel cross-checks (REPO):
- `supplier_nowcast.md`: Feng Tay Nike orders -9% to -12% for Jul to Sep, "in line with, not worse than, the guided path".
- `na_sell_through.md`: NA end demand about -1% while NA wholesale grew 9%. The sell-in unwind is "partly in guidance".

FY27 arithmetic [arith]:
- EPS guide 1.15 / 1.25 / 1.35 less Q1's $0.48 leaves Q2 to Q4 of 0.67 / 0.77 / 0.87.
- Consensus implies 0.78 (Zacks) to 0.81 (Yahoo), against FY26 Q2 to Q4 ex-IEEPA of 1.08 (0.53 + 0.35 + 0.72 - 0.52 IEEPA; REPO).
- Revenue: if Q2 is -10.1%, consensus -7.0% implies H2 -6.7%. A guide midpoint of -8% implies H2 -8.8%.
- Consensus FY27 EBIT of $2,479M equals what the $1.25 midpoint implies at a mid-20s tax rate (1.25 x about 1,487M shares / 0.75 = about $2.48B).

**Result:** EPS sits on the midpoint (neither S2 nor L2 fully). Revenue sits at the shallow end (mild S2, about $0.4B or 1 pt).

### 2.5 FY28: does consensus contradict Nike's own timing?

Consensus FY28 needs revenue +1.1%, EBIT +$700M (+28%) and margin +150 bps, on almost flat sales.

Evidence against:
- Nike: pressure "into '28".
- Sportswear, Jordan and Greater China actions extend beyond FY27 (Q1 FY27 10-Q p. 20, REPO `guidance_vs_actual.csv` note).
- Partner online sales in mainland China end 2027-01-01. That is not lapped until Q3 FY28 (REPO `china_floor.md`).
- Q1 FY28 laps the World Cup sell-in. Yet consensus has Q1 FY28 at only -2.0%.
- Pace savings come mostly in FY29 and FY30, with partial reinvestment.

Evidence for:
- Q2 FY28 laps the 400 bps one-off. FY27 compares are easy.
- Performance (Running, Football) is growing high single digits.
- Partners describe an improving Aug to Sep trend (REPO `na_sell_through.md` section 3.7).

Scenarios [arith]. Both use a 35% decremental margin on revenue below consensus, keep consensus' own margin expansion otherwise, a 25% tax rate and 1,470M shares:

| FY28 revenue | EBIT | EPS | vs consensus 1.646 |
|---|---|---|---|
| Flat vs FY27 ($43.15B) | about $3.0B | about $1.53 | -7% |
| -2% vs FY27 | about $2.7B | about $1.38 | -16% |

**Result:** S3 and S4 hold for FY28. The size is moderate (7% to 16%).

### 2.6 New CFO Dave Denton's first-guide record (new primary data, SEC 8-K Ex. 99, OPENED)

| Company, year | Initial guide (date) | Consensus at guide | Path | Actual | Actual vs initial midpoint | Stock day 0 / day 1 (excess vs S&P) |
|---|---|---|---|---|---|---|
| Lowe's FY2019 | Diluted EPS $6.00 to $6.10 (Dec 12, 2018 investor day 8-K; reiterated Feb 27, 2019) | not found | Cut to adj. $5.45 to $5.65 (May 22, 2019); $5.63 to $5.70 (Nov 20, 2019) | Adj. about $5.72 (quarters 1.22 + 2.15 + 1.41 + 0.94; GAAP $5.49) | about -5% (**miss**) | Investor day: +2.9% / +5.4% (xs +2.4 / +4.9); May 2019 cut: -11.8% day 0 |
| Pfizer 2024 | Adj. $2.05 to $2.25 (Dec 13, 2023) | $3.16 (SNIPPET, Motley Fool) | Raised May, Jul and Oct 2024 to $2.75 to $2.95 | Adj. $3.11 | **+45%** | -6.7% / -8.6% (xs -8.1 / -10.2); day 60 -2.0% |
| Pfizer 2025 | Adj. $2.80 to $3.00 (Dec 17, 2024) | n/a | Raised to $2.90 to $3.10 (Aug 5, 2025) | Adj. $3.22 | **+11%** | +4.7% / +2.5% (xs +5.1 / +5.9) |
| Pfizer 2026 | Adj. $2.80 to $3.00 (Dec 16, 2025) | n/a | EPS reaffirmed, revenue midpoint raised $0.5B (Aug 4, 2026) | pending | n/a | n/a |

Sources:
- Lowe's 8-K Ex. 99.1: Dec 12, 2018; Feb 27, 2019; May 22, 2019; Aug 21, 2019; Nov 20, 2019; Feb 26, 2020 (sec.gov, OPENED).
- Pfizer 8-K Ex. 99: Jan 30, 2024; May 1, 2024; Jul 30, 2024; Oct 29, 2024; Feb 4, 2025; Aug 5, 2025; Feb 3, 2026; Aug 4, 2026 (sec.gov, OPENED).
- Prices: Yahoo chart API, fetched 2026-10-14 (OPENED).

Caveats:
- Pfizer's 2024 beat was helped by COVID-product items and a cost programme, not only conservative guidance.
- Lowe's 2019 was a retail operating turnaround, which is closer to Nike.

**Result:** L2 is only partly supported. Denton set Pfizer bars low, but the closer analog (Lowe's turnaround) missed its first guide.

### 2.7 How past Nike resets and investor days moved the stock

From REPO `data/trackrecord/price_reactions.csv` (closes from `data/nke_daily_prices.csv`):

| Event | Day 1 | Day 20 excess vs S&P |
|---|---|---|
| Dec 2023 FY24 cut and $2B savings | -11.8% | -19.3% |
| Jun 2024 FY25 down MSD | -20.0% | -22.6% |
| Oct 2024 guidance withdrawn | -6.8% | -14.2% |
| Mar 2026 multi-quarter guide | -15.5% | -25.3% |
| Jun 2026 cut | +4.9% | +7.7% |
| **Oct 1, 2026 FY27 initial guide** | **-3.6%** | n/a |

- The last case is the smallest negative reaction to a full-year reset in the table.
- The stock then went 33.87 (Oct 2), 34.61, 34.36, 34.74, 34.71, 35.35 (Oct 12), back to the pre-print close of 35.40 (Sep 30) (REPO prices).

Earlier Nike resets kept drifting lower (S5 true historically). Through Oct 12 this one has not (L4 true now).

Nike investor days, computed from Yahoo chart data fetched 2026-10-14 (OPENED):

| Investor day | Day 0 | Day 1 | Day 5 | Day 20 | Day 60 |
|---|---|---|---|---|---|
| Oct 14, 2015 | +0.0% | +2.4% (xs +1.4) | +5.3% | +1.3% (xs -2.3) | -5.3% |
| Oct 25, 2017 | +2.8% | +6.3% (xs +6.7) | +3.1% | +10.6% (xs +9.5) | +25.7% (xs +15.2) |
| Jun 2021 targets (with Q4 FY21 print, REPO) | | +15.5% | | xs +21.1 | |

Options (Yahoo v7 options, 2026-10-14, OPENED). At-the-money straddle as % of spot:

| Expiry | Straddle |
|---|---|
| Nov 13 | 8.0% |
| Nov 20 | 9.5% (spans Investor Day, Nov 16 to 17) |
| Dec 18 | 13.2% (spans the estimated Dec 17 Q2 print) |

- Variance between Nov 13 and Nov 20 implies about 5.1% for that week, against about 3.7% for a normal week. That leaves an **Investor Day event move of about 3.6%** [arith].
- The market does not price a large reset at Investor Day.

Positioning (REPO `consensus_and_valuation.md`): short interest rose from 75.6M to 99.2M shares between Aug 31 and Sep 30, 2026 (6.7% of shares outstanding).

## 3. Alternative explanations tested

1. **"The stock held up because the market expects Investor Day to raise numbers, so consensus is too low."** Partly ruled out:
   - Options imply only about 3.6% for the event.
   - Bernstein and Stifel expect little change before or at Investor Day (SNIPPET and OPENED).
   - The hold is better explained by buy-side expectations already near $1.50 (Piper) and by short covering after a 31% rise in short interest. That last part is not verified; short data dated Oct 15 publishes around Oct 24.
2. **"Consensus FY27 is too high because Nike missed its last two initial full-year guides (FY24, FY25)."** Weakened:
   - Those guides were set by the prior CFO (Friend) under Donahoe (REPO `guidance_vs_actual.csv`).
   - Under Hill, next-quarter revenue guides were met or beaten in 6 of 6 cases, though Q1 FY27 (-4.3%) came in below the guide midpoint and missed LSEG.
   - The new CFO says the guide is "reasonable and attainable", and his Pfizer record is conservative.
   - Not fully ruled out: Lowe's 2019 shows he can miss.
3. **"Q2 consensus is too low because the 400 bps headwind is already in Q1's run rate."** Ruled out. The two items are Q2-specific laps (EMEA Cyber Week 2025, NA sell-in in Q2 FY26), so they are not in Q1.
4. **"FY28 consensus is stale rather than wrong."** Partly true. Highs of 3.22 (Yahoo/Zacks) and Telsey's earlier $2.05 are pre-guide. Even so, the updated contributors' central case (Yahoo 1.646 after 24 down revisions) still requires +28% EPS on +1% revenue. The stale names only add further mechanical downside to the mean.
5. **"Tariff relief makes FY27 and FY28 margins easier than modeled."** Open:
   - Q2 FY26 carried -360 bps from tariffs (REPO).
   - What replaces Section 122 after its 150-day window, and the rate actually in force in Sep to Nov 2026, is unverified. The repo marks replacement tariffs "not researched".
   - This could add up to about 100 bps of Q2 GM upside versus the 60 to 130 bps consensus implies. It cuts in the LONG direction for Q2 EPS.

## 4. What is still unknown, and what would settle it

**Unknown:**
- The free-source FY27 and FY28 gross margin consensus.
- The tariff rate in force for Q2 FY27 receipts.
- Whether Investor Day frames FY28 as a growth year or another transition year.
- The October factory data.

**What would settle it (all before Nov 19):**
1. Investor Day (Nov 16 to 17): the FY28 framework and the five-year algorithm, compared with consensus FY28 EPS of 1.65 and FY29 EBIT margin of 8.9%.
2. Feng Tay, Pou Chen and Eclat October monthly revenue (MOPS, about Nov 10). This is the first read on Q3 FY27 builds.
3. Yahoo/Zacks FY28 revision trend in the weeks to Nov 16: is it still falling or flat?
4. FINRA short interest for Oct 15 and Oct 31.
5. The Federal Register or CBP notice on the tariff regime after Section 122.

## 5. Sources (all fetched 2026-10-14)

- Yahoo quoteSummary NKE: earningsTrend, financialData, recommendationTrend, upgradeDowngradeHistory, calendarEvents (OPENED).
- Yahoo v7 options NKE, expiries Oct 16, 2026 to Mar 19, 2027 (OPENED).
- Yahoo v8 chart for NKE 2015 to 2018, LOW, PFE and ^GSPC (OPENED).
- api.nasdaq.com analyst/NKE: earnings-forecast, estimate-momentum, ratings (Zacks; OPENED).
- MarketScreener NIKE-INC-13739 finances (WebFetch, OPENED).
- StockTitan "Why Nike Stock Fell After Its October 2026 Earnings" (2026-10-01, updated 2026-10-05; OPENED).
- Investing.com: Bernstein note (2026-10-02, OPENED) and Piper Sandler note (2026-10-02, OPENED).
- CNBC Oct 1, 2026 article: 403, not opened. LSEG numbers are taken from the StockTitan relay.
- WebSearch summaries for BofA, Stifel and Telsey: SNIPPET.
- Nike Q1 FY27 call transcript, Oct 1, 2026 (Nike PDF, OPENED in scratchpad `na_st/raw/nke_q1fy27.txt`).
- Lowe's 8-K Ex. 99.1 (sec.gov/Archives/edgar/data/60667/): 000006066718000205, 000006066719000022, 000006066719000074, 000006066719000134, 000006066719000179, 000006066720000029 (OPENED).
- Pfizer 8-K Ex. 99 (sec.gov/Archives/edgar/data/78003/): 000007800324000017, 000007800324000103, 000007800324000155, 000007800324000188, 000007800325000017, 000007800325000136, 000007800326000005, 000007800326000094 (OPENED).
- Motley Fool, Dec 13, 2023, Pfizer consensus $3.16 (SNIPPET).
- Repo files cited inline: `data/nike_filing_facts.csv`; `data/trackrecord/*.csv`; `research_notes/thesis_tests/consensus_and_valuation.md`; and the crux notes `china_floor.md`, `supplier_nowcast.md` and `na_sell_through.md`.
