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

## Skeptic review

Prepared 2026-10-14 by an independent reviewer. I re-checked the key inputs at source and looked for data pointing the other way. Raw files are in the session scratchpad under `skeptic/`; they are not committed.

### S.1 Verdict

**I keep NEUTRAL (moderate), but for different reasons.** Two of the investigator's three legs are weaker than written, and one new primary fact points the other way:
- The FY28 "consensus too high" leg is weaker. Consensus FY28 revenue (+1.1%, with Q1 FY28 at -2.0% and the turn to growth from Q2 FY28) matches what Denton actually said: pressure will "probably bleed in a little bit into fiscal '28". The note's paraphrase ("pressure into fiscal 28") overstates it. The EPS leg (+28% on +1% revenue) is still a stretch, but it depends on Pace savings timing, which Investor Day will set. Goldman made the same point on Oct 2 (Stocktwits, OPENED): the key question is "whether fiscal 2027 represents the trough or another step-down".
- The "stock looked through the cut" leg is weaker in excess-return terms. The stock is back to its pre-print level, but the market and the sector rallied (table S.3). Against athletic peers, Nike lagged badly.
- New and pointing LONG for the Dec print: I verified the post-Section 122 tariff regime at the primary source (S.2). The Q2 FY26 comparison carried -360 bps of tariffs at IEEPA rates of 19% to 20%. Q2 FY27 receipts face 10% to 12.5%. That supports Q2 gross margin above the 60 to 130 bps rise that consensus implies. The Q2 print (about Dec 17) comes after finals, though, so this cannot carry the pitch.

Net: on the expectations question alone, neither LONG nor SHORT is supported. Investor Day (Nov 16 to 17) remains the event that settles it.

### S.2 New primary evidence: the tariff regime now in force (closes the investigator's open item 5)

- USTR, "Notice of Actions in Section 301 Investigations ... Forced Labor", signed July 23, 2026; FR doc 2026-15181, published Jul 28, 2026 (ustr.gov PDF "FLIP 301 Investigation Final Action FRN 7-23-26", OPENED). Key terms:
  - Effective 12:01 a.m. ET, July 24, 2026, the moment Section 122 lapsed.
  - **Vietnam: MFN + 12.5%** (HTS 9903.05.84, "The duty provided in the applicable subheading + 12.5%").
  - **Indonesia, Cambodia, India, Bangladesh: 10%.**
  - China: 12.5%, on top of existing Section 301 duties.
  - The "net of MFN" cap applies only to the EU, Taiwan, Japan, Korea and Switzerland. It does not apply to Vietnam or Indonesia, so footwear gets no relief from its high MFN rates.
  - I found no chapter 64 (footwear) HTS codes in the Annex exclusions.
- Nike's sourcing mix (REPO `data/nike_filing_facts.csv`, FY26 10-K): footwear Vietnam 52%, Indonesia 27%, China 16%; apparel Vietnam 34%, China 12%.
- Blended new rate on footwear: about 11.7% [arith].

How this compares:

| Benchmark | Rate | Source |
|---|---|---|
| Nike's own FY27 plan (Jun 2026) | 10% through July, then 15% | Q4 FY26 call, REPO `tariffs_costs.md` |
| In force now | about 11.5% to 12% | USTR notice above |
| Q2 FY26 comparison (IEEPA) | about 19% to 20% | Vietnam 20%, Indonesia 19% |

- On Oct 1, Nike did not mention tariffs anywhere in the call; the only reference is "higher input costs" (transcript, OPENED). So whether the Oct 1 guide still embeds 15% is unknown.
- If it does, the lower actual rate is worth very roughly $0.05 to $0.10 of FY27 EPS [arith]. The basis is Nike's $1.5B annualized gross tariff at IEEPA rates scaled to 15% and to 11.5%, with about 0.6 of a year's flow-through in FY27.
- The notice is being challenged in court (secondary sources). No stay was found.

Q2 FY27 gross margin cross-check [arith]:

| Step | Estimate |
|---|---|
| Q2 FY26 tariff drag | -360 bps |
| Q2 FY27 tariff drag at about 0.55 to 0.7 of that rate | about -200 to -250 bps |
| Tariff effect, y/y | about +110 to +160 bps |
| Non-tariff items, using Q1 FY27 as a guide (total +60 bps, of which product cost only +10 bps) | about +50 bps |
| **Q2 FY27 GM change, y/y** | **about +150 to +200 bps, to about 42.1% to 42.6%** |
| Consensus-implied (investigator's range) | 41.2% to 41.9% |

- Each 50 bps of GM on $11.18B of revenue is about $56M of EBIT, or roughly $0.03 of EPS.
- Q2 EPS upside of $0.03 to $0.07 against the $0.38 consensus is plausible.
- Risks to this: deeper holiday discounting from the marketplace reset (Denton's "push and pull"), and China (45.7% GM) shrinking 25% to 35%, which hurts mix.

### S.3 Price action re-checked (Nasdaq historical API, closes, fetched 2026-10-14, OPENED)

Nike reported after the close on Oct 1, so the pre-print close is **$35.15 (Oct 1)**, not $35.40 (Sep 30) as the note states. The -3.6% day-1 move is still correct.

| Ticker | Oct 1 | Oct 13 | Change |
|---|---|---|---|
| NKE | 35.15 | 35.33 | +0.5% |
| SPY | 763.99 | 778.01 | +1.8% |
| XRT | 82.62 | 84.33 | +2.1% |
| DECK | 79.57 | 84.02 | +5.6% |
| ONON | 30.20 | 35.49 | +17.5% |
| LULU | 95.86 | 94.34 | -1.6% |

- Nike's excess return since the print is -1.3% vs SPY and -1.6% vs XRT. It lagged DECK by about 5 points and ONON by about 17 points.
- That is still far milder than earlier resets (-14% to -25% day-20 excess). L4 holds in direction, but "fully recovered" is mostly beta, not a sign the market priced in a rebound.

### S.4 Other re-checks

- **Consensus (Yahoo, investigator's saved payload re-parsed; Nasdaq/Zacks API re-fetched 2026-10-14, OPENED).** The numbers match:
  - Yahoo: Q2 0.381, FY27 1.288, FY28 1.646.
  - Zacks: FY27 1.26 (n 11), FY28 1.78 (n 14, high 3.22), FY29 2.31 (n 6).
  - Zacks has Q1 FY28 at 0.50 and Q2 FY28 at 0.47 (n 5).
  - The single stale 3.22 adds about $0.12 to the Zacks FY28 mean [arith]. Excluding it, Zacks is about 1.66, the same as Yahoo.
  - Yahoo still shows FY27 down 5% in the last 7 days (1.356 to 1.288), so FY27 has not fully settled, contrary to "nearly stopped moving".
  - A fresh Yahoo re-fetch was blocked (HTTP 429).
- **Options (investigator's saved chain re-computed, OPENED).**
  - Event variance = 9.5%^2 minus 8.0%^2, less 7 days at the base variance of 0.00021 per day.
  - Result: an Investor Day straddle-equivalent move of about 3.4%, or a 1-sigma of about 4.3%. This confirms the low priced event risk.
- **Short interest (FINRA consolidated short interest API, OPENED).**

  | Settlement date | Shares short (M) | Days to cover |
  |---|---|---|
  | Jun 15 | 57.0 | |
  | Jun 30 | 72.3 | |
  | Jul 15 | 63.9 | |
  | Jul 31 | 57.4 | |
  | Aug 14 | 68.8 | |
  | Aug 31 | 75.6 | |
  | Sep 15 | 85.7 | |
  | Sep 30 | 99.2 | 2.6 |

  - Shorts added 23.6M shares in September into the print. The covering test needs the Oct 15 figure, published around Oct 23 to 24.
- **"Buy-side about $1.50" (Piper).** I could not re-verify this; the search did not surface the Investing.com wording. The Stocktwits roundup of Oct 2 (OPENED) has no buy-side figure, and Citi says only that the guide was "below market expectations". Treat it as a single-source claim.

### S.5 Alternatives, after review

- **"FY28 consensus revenue contradicts management."** Ruled out by the transcript wording ("bleed in a little bit"). The FY28 risk sits in EPS and Pace timing, not revenue.
- **"Tariff relief is upside not in numbers."** Partly confirmed:
  - The regime is verified at 10% to 12.5%, below Nike's 15% plan.
  - It is still open whether the Oct 1 guide already uses actual rates. Nike was silent.
- **"The muted reaction proves the market priced through the cut."** Weakened:
  - The excess return is -1.3%, and peers rallied 5% to 17%.
  - A record short build (+31% in September) may explain the lack of follow-through selling.

### S.6 What would settle it

1. Investor Day FY28 framework and Pace savings phasing against FY28 EPS of 1.65 and FY29 EBIT margin of 8.9%. This is unchanged from the note.
2. Any Nike comment, at Investor Day or in an 8-K, on the tariff rate embedded in guidance.
3. FINRA short interest for Oct 15 (out about Oct 23) and Oct 31.
4. The Q2 FY27 gross margin (about Dec 17), against about 41.5% implied by consensus.

## Re-weighed with hunt data (2026-10-14)

**Verdict: stays NEUTRAL (moderate).** The hunt data (in `data/hunt/*/`) firm up the FY28 revenue risk a little and add a small, quantified EPS offset that leans LONG. They give no independent read showing that Q2 FY27 or FY27 consensus is wrong. Only tests the checker did not fail are used, at the checker's corrected strength.

### What the new data says about each leg

**Leg 1: Q2 FY27 and FY27 consensus (-10.1% Q2, EPS $1.26 to $1.29) still matches the evidence.**
- Supplier flow (`trade_imports`): Feng Tay Jul to Sep 2026 was -8.4% YoY. On a two-year stack it was -5.9%, against US footwear imports at -7.6%. The holiday build shows no Nike-specific collapse, which fits the guided path and the consensus (NEUTRAL, moderate).
- Discounting (`pricing_catalog`): the nike.com discounted-page share did not improve over 12 months (+0.5 pts YoY; crawl-cluster CI -4.4 to +5.6). Nike flagged "increased discounts" itself, so this is already in the guide.
- Digital (`apps_digital`): Play-review counts imply about -15% for Q2 digital. The checker found r = -0.17 inside the decline regime, so this is the fit's intercept and not a reading. Weak, and not used to move Q2.
- NA (`peers_reported`, `macro_category`): NA share of the peer set is flat at about 50%. The NA sell-in vs sell-through split is still not settled (checker: NEUTRAL). Nothing here contradicts the 400 bps Q2 headwind Nike gave.
- Guide track record (`earnings_calls/guidance_scorecard.csv`): under Hill, next-quarter revenue guides came in as 6 beats and 1 in range out of 7. Q1 FY27 (-4.3%) landed just below the midpoint of -1% to -6%, and Q1 FY27 GM (+60 bps) beat. This record mildly supports the skeptic's view that the bar is achievable. It is not a strong LONG signal, because the latest quarter was the weakest result in the run.
- Net: no new source points to a miss or a beat against Q2/FY27 consensus. S1 and L1 both stay unmet.

**Leg 2: FY28 consensus (EPS $1.646, revenue +1.1%) is still somewhat high. Revenue risk is firmer; EPS risk is partly offset.**
- Revenue risk confirmed by independent sources:
  - China (`peers_reported`): Nike's share of the China peer set went 65% (2022), 62% (2024), 56% (2025), 50% (H1 2026), losing 7 to 8 pts a year with no slowdown. The checker kept this SHORT while noting Nike is sell-in and domestic brands are sell-through.
  - China doors (`stores`, HKEX filings): Pou Sheng net closures per half went -40, -98, -200. Topsports selling area kept shrinking steadily. The checker re-rated this moderate SHORT. Partner online sales end 2027-01-01, which hits Q3 FY28.
  - EMEA (`peers_reported`): the gap to peers is not narrowing (-16.9 / -14.0 pts in CQ1 to CQ2 2026 vs -15.7 average in 2025). Share of the EUR peer set fell from 42.7% to 39.2%.
  - These are the regions where consensus needs the turn to growth from Q2 FY28. They support the investigator's "flat to -2%" FY28 revenue scenarios more than consensus +1.1%.
- Offsets that lean LONG on FY28 EPS:
  - Tariffs (`risk_tariffs/tariff_gap_sizing.csv`): the rate in force (about 11.4% blended) is about 3.6 pts below Nike's 15% plan. If Nike keeps 70% to 100% of it, the gap is worth about $0.04 to $0.06 of FY27 EPS and $0.08 to $0.12 of FY28 EPS. That closes roughly half to all of the low scenario gap ($1.53 vs $1.65) and about a third of the high gap ($1.38).
  - Gross margin (`peers_reported` T2b): the GM gap to peers narrowed, but the checker cut it to weak LONG because part of it is peers falling.
  - Product pipeline (`hiring`): product and design share of postings rose (US-only like-for-like 32% to 44%), which fits a rebuild with a 12 to 18 month lag. That lands in FY28 at the earliest, so it is not evidence against consensus.
- Net: FY28 revenue consensus looks about 1 to 3 pts too high on China and EMEA alone. The tariff gap removes much of the EPS consequence. The FY28 EPS gap stays about 0% to 12%, small and known.

**Leg 3: is it priced? Positioning data is two-sided.**
- Short interest (`people_governance`, `risk_short_interest`): 99.2M shares on Sep 30 after four straight rises. Borrow is easy (IBKR fee 0.41%, days to cover 2.6). Across about 60 consumer stocks, a run of four rises is followed by another rise only 47% of the time. The bearish view is crowded in the stock, which argues against a large unpriced downside surprise.
- 13F breadth: down 14.5% YoY, the worst since 2018, but about 80% smaller once small-position exemptions are excluded, and it does not predict returns in a 2,111 stock-quarter test (NEUTRAL).
- Insiders: 2025 and 2026 open-market buying is the largest in 20 years, but both Nike buy rounds lost 31 to 34 pts vs SPY over 126 days, and nobody has bought since Oct 1 (weak LONG at most).

### Scoring against the pre-registered rules

| Rule | Before hunt | After hunt |
|---|---|---|
| S1 / L1 (Q2 consensus vs bottom-up) | neither | neither; supplier and pricing data fit -9% to -11% |
| S2 / L2 (FY27 vs guide, CFO record) | mild S2 on revenue; L2 partial | unchanged; Hill-era guide record adds slight L2 support |
| S3 (FY28 vs management timing) | holds, moderate | revenue leg firmer (China, EMEA share loss); EPS leg partly offset by tariffs |
| S4 (revisions still falling) | holds for FY28 | unchanged (no new revision data) |
| S5 / L4 (price after reset) | L4 in direction, mostly beta | unchanged; crowded short with cheap borrow |

### Why not strong, why not weak

- Not strong: the only legs with firmer data (China and EMEA share loss) are about FY28 revenue, which Investor Day (Nov 16 to 17) will reset anyway. The tariff sizing cuts the other way on EPS. None of the hunt sources speaks to the size of the gap between consensus and the stock price, which is what an expectations trade needs.
- Not weak: the core finding (Q2 and FY27 bars are fair, FY28 a little high) is confirmed by different sources (supplier revenue, pricing panel, peer-reported share) and nothing in the hunt contradicts it.

### Sources used (all in this repo)
- `data/hunt/trade_imports/` (Feng Tay vs US imports, two-year stack)
- `data/hunt/pricing_catalog/` (nike.com discount panel)
- `data/hunt/peers_reported/` (regional share of peer set, GM gap)
- `data/hunt/stores/` (Pou Sheng, Topsports HKEX counts)
- `data/hunt/risk_tariffs/tariff_gap_sizing.csv` (FY27 and FY28 EPS from plan vs actual tariff rate)
- `data/hunt/earnings_calls/guidance_scorecard.csv` (Hill-era guide outcomes)
- `data/hunt/people_governance/` and `data/hunt/risk_short_interest/` (SI, borrow, 13F breadth, insiders)
- `data/hunt/hiring/` (product mix, US-only like-for-like)
- `data/hunt/apps_digital/` (Play reviews, treated as weak per the checker)
