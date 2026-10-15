# D7: Investor Day and strategy-update event study (28 precedents), and what it implies for Nike on Nov 16 to 17, 2026

Prepared Oct 14, 2026. Companion file: `D7_event_table.csv` (same folder, 29 rows including one leadership event, all columns, returns in percent). Price base for Nike: $35.30 (Oct 14 close, Yahoo chart API, `adjclose`), $35.35 on Oct 12 in `data/nke_daily_prices.csv`.

Source tags: **OPENED** = I opened the primary page (SEC 8-K exhibit, SGB article, price API). **SNIPPET** = rests on a search summary only; confirm before it goes on a slide. **DERIVED** = my arithmetic on tagged inputs.

## 1. Headline

1. **Selloffs follow near-term bad news and vagueness, not dated targets.** Of 28 precedents, 8 combined a dated long-run plan with a near-term guide cut or withdrawal, a lowered/delayed target, or no new numbers. All 8 fell on day 0 versus the S&P 500 (mean -10.8%, range -4.4% to -23.3%) and the average gap widened to -14.0% on day 1, -14.9% on day 5 and -19.2% on day 20 (DERIVED). The other 20 events (dated numeric targets, no near-term cut) averaged +2.3% on day 0 and +2.7% on day 1; the worst day-0 result among them was -4.7% (Lululemon 2022). Permutation p-value for the difference is below 0.001 at every horizon, but see the circularity caveat in section 6: the 8 "bad" events are bad news by construction.
2. **Dated targets that are raised versus the company's own prior targets rally, and the rally builds for a week.** 4 events are raised on documents alone (Nike 2015, Nike 2021, Under Armour 2015, Levi 2022): mean vs S&P +5.4% day 0, +5.9% day 1, +8.1% day 5, +3.4% day 20. Widening to 7 events where I found sourced analyst commentary that targets beat expectations: +4.8% / +6.2% / +8.1% / +3.9%, and 7 of 7 positive on days 1 and 5. Ex Nike 2021 (an earnings-day event): +3.0% / +5.0% / +6.5%. The day-20 median is -1.7%, so the rally partly fades.
3. **For a short, the risk is two-sided and the timing is bad.** The pitch is judged Nov 19, which is day 2 or 3 of the event window, exactly where upside precedents peak (+7.3% to +7.9% mean for the 7 "above" events) and where downside precedents are already -15%. Mean absolute day-1 move versus the S&P across all 28 events was 7.0% (median 4.7%), versus about 6.4% to 7.2% implied for Nike's Q2 print (repo note 17). Break-even for the short on day 3 is P(down) = 0.53 x P(up); at the sample base rates (25% up, 46% neutral, 29% down) expected short P&L is about +2.4%, but it turns negative if Nike's chance of a near-term cut or vague outcome is below about 16% while the chance of a credible above-consensus algorithm is 30% (section 5).
4. **Nike's own two precedents for a dated, raised algorithm were both rewarded (Oct 2015 +5.3% by day 5; Oct 2017 +3.1%), and the 2021 raise was +15.5% in one day.** Every 2017 and 2021 profit target was later missed (repo notes 19, `advocate_short_cash_dividend.md`), so the market paid for the target on the day and punished the miss later. That supports a short thesis on delivery, not a short thesis on the Investor Day reaction.

Bottom line for the pitch: a dated, higher-than-consensus algorithm is the base case (consensus FY28 operating margin is 7.2% and FY28 EPS $1.65, repo), so a rally of roughly +5% to +8% over days 1 to 3 is the central risk to a short held through Nov 19. A selloff needs a near-term cut, a lowered or delayed target, or vagueness. Size the position and the Nov 19 narrative for both branches.

## 2. Method

- **Event set.** Every consumer, apparel, footwear or beauty/coffee precedent I could date and price: 28 target events plus one leadership event (Under Armour, Plank return, Mar 14 2024; excluded from statistics). Companies with no Yahoo history (Foot Locker, Hanesbrands, Skechers, delisted after being acquired or taken private) are in section 4 as unpriced.
- **Day 0** is the first session that could reflect the news (event date if released pre-market or intraday; next session if after the close: Nike Oct 1 2024 and Puma Jan 22 2025). Returns are close-to-close from the prior close, cumulative to day 0, 1, 2, 3, 5, 20 (trading days). Price: Yahoo chart API `adjclose` (no email in any request; user-agent "Mozilla/5.0"). Price file validated against reported moves: Crocs Sep 14 2021 +8.5% (reported +8.5%), Under Armour Dec 12 2018 -10.4% (reported about -10.5%), VF Mar 6 2025 -12.3% (reported more than -12%), Nike Jun 25 2021 +15.5% (reported +15.5%), Nike Oct 2 2024 -6.8% (reported -5% to -7%).
- **Benchmarks.** S&P 500 (`^GSPC`) for all; local index (DAX) in the CSV for adidas and Puma; sector = equal-weight basket of up to 16 US apparel/footwear names excluding the subject (NKE, LULU, VFC, UAA, PVH, RL, TPR, COLM, CROX, DECK, WWW, LEVI, KTB, GIL, CPRI, GIII, those with data on the date, at least 5); XLY for Starbucks, XLP for Estee Lauder. "Abnormal" = raw minus benchmark, no beta adjustment.
- **Classification (fixed before looking at the statistics).** UP = dated numeric targets, raised versus the company's prior targets or sourced as above expectations, no near-term cut. DOWN = near-term guide cut or withdrawn, or target lowered/delayed, or no new multi-year numbers (vague). NEUTRAL = dated numeric targets, new or reaffirmed, with no evidence found either way. The DOWN list uses company documents only. The UP list partly uses press commentary (flagged per row in the CSV `evidence` column).
- **Consensus change after the event** (requested): not obtainable free at event level. See route log in section 7. The substitute is (a) comparison with the company's own prior targets (OPENED for Levi, VF, Columbia, Capri), (b) sourced analyst commentary on expectations (SNIPPET), and (c) the price reaction itself, which is not used to classify.

## 3. Event table (returns in percent, DERIVED from Yahoo chart API)

Full text of targets, evidence and sources per row is in `D7_event_table.csv`.

| ID | Company | Day 0 | Group | Raw d0 / d1 / d5 / d20 | vs S&P d0 / d1 / d5 / d20 | vs sector d0 / d1 / d5 / d20 | Tag |
|---|---|---|---|---|---|---|---|
| E01 | Nike: Investor Day (Beaverton), $50B FY2020 revenue target | 2015-10-14 | UP | +0.0 / +2.4 / +5.3 / +1.3 | +0.5 / +1.4 / +4.5 / -2.3 | +1.0 / +2.9 / +8.2 / +11.0 | SNIPPET |
| E02 | Nike: Investor Day, 5-yr algorithm (HSD rev, mid-teens EPS) | 2017-10-25 | NEUTRAL | +2.8 / +6.3 / +3.1 / +10.6 | +3.3 / +6.7 / +2.7 / +9.5 | +2.7 / +6.0 / +7.1 / +7.7 | SNIPPET |
| E03 | Nike: Q4 FY21 results with long-term outlook to FY25 (HSD-LDD rev, high-teens EBIT) | 2021-06-25 | UP | +15.5 / +14.0 / +19.6 / +23.6 | +15.2 / +13.5 / +17.6 / +19.9 | +14.4 / +14.4 / +18.0 / +23.4 | SNIPPET |
| E04 | Nike: Q1 FY25 results: guidance withdrawn, Nov 19 2024 Investor Day postponed | 2024-10-02 | DOWN | -6.8 / -7.9 / -7.5 / -14.2 | -6.8 / -7.7 / -9.0 / -16.1 | -5.4 / -5.8 / -5.8 / -9.5 | SNIPPET |
| E05 | adidas: Investor & Media Day "Own the Game" (2021-2025 targets) | 2021-03-10 | NEUTRAL | +2.8 / +6.2 / +0.9 / -0.9 | +2.2 / +4.5 / -1.7 / -6.6 | +2.0 / +4.1 / -2.8 / -3.2 | SNIPPET |
| E06 | adidas: FY2025 results: 2026 outlook and 2028 mid-term targets | 2026-03-04 | DOWN | -3.6 / -1.4 / -4.8 / -6.9 | -4.4 / -1.6 / -4.2 / -3.4 | -3.1 / +0.8 / +3.0 / +1.1 | SNIPPET |
| E07 | Under Armour: Investor Day 2015, $7.5B 2018 revenue target | 2015-09-16 | UP | +4.7 / +5.5 / +2.8 / -1.4 | +3.9 / +4.9 / +4.8 / -2.2 | +1.8 / +3.8 / +4.6 / +3.2 | SNIPPET |
| E08 | Under Armour: Investor Day 2018, 2023 low-double-digit margin goal | 2018-12-12 | DOWN | -10.4 / -15.1 / -18.2 / -11.1 | -11.0 / -15.7 / -13.3 / -9.5 | -11.7 / -13.6 / -13.9 / -13.4 | SNIPPET |
| E09 | Under Armour: Plank returns as CEO (leadership change) | 2024-03-14 | EXCLUDE | -10.2 / -10.7 / -8.9 / -19.2 | -9.9 / -9.7 / -10.3 / -18.3 | -8.1 / -8.3 / -10.0 / -7.8 | SNIPPET |
| E10 | Under Armour: Investor Day 2024 (qualitative strategy, FY25 outlook referenced) | 2024-12-12 | DOWN | -5.2 / -12.9 / -17.6 / -20.2 | -4.7 / -12.3 / -14.1 / -16.2 | -4.2 / -12.2 / -14.3 / -18.2 | SNIPPET |
| E11 | Puma: Capital Markets Day London, 2018-2022 targets | 2018-03-20 | NEUTRAL | +5.7 / +5.1 / -0.3 / +8.5 | +5.6 / +5.1 / +3.4 / +8.6 | +4.7 / +4.1 / -0.4 / +3.9 | SNIPPET |
| E12 | Puma: Prelim FY24 + nextlevel plan, 8.5% EBIT margin by 2027 (cut vs 2025 aim) | 2025-01-23 | DOWN | -22.8 / -23.4 / -25.8 / -32.6 | -23.3 / -23.7 / -25.6 / -31.4 | -23.8 / -24.4 / -30.3 / -27.6 | SNIPPET |
| E13 | Lululemon: Investor Day, Power of Three x2 (double revenue by 2026) | 2022-04-20 | NEUTRAL | -4.8 / -6.8 / -12.5 / -32.7 | -4.7 / -5.2 / -6.3 / -20.6 | -4.6 / -5.4 / -4.0 / -13.6 | SNIPPET |
| E14 | VF Corp: Investor Day FY27 plan (15% op margin) | 2022-09-28 | DOWN | -6.9 / -12.3 / -9.0 / -19.6 | -8.8 / -12.1 / -12.8 / -24.6 | -10.0 / -12.4 / -15.4 / -27.6 | OPENED |
| E15 | VF Corp: Reinvent to Grow Part 2 Investor Day | 2025-03-06 | DOWN | -12.3 / -18.4 / -30.2 / -50.0 | -10.5 / -17.2 / -24.7 / -42.3 | -11.2 / -16.3 / -23.0 / -31.8 | OPENED |
| E16 | Kontoor: Virtual Investor Day 2021 | 2021-05-24 | NEUTRAL | +1.0 / +0.6 / +5.9 / -8.2 | -0.0 / -0.2 / +4.8 / -10.4 | +0.2 / -0.1 / +2.5 / -9.2 | SNIPPET |
| E17 | Kontoor: Helly Hansen Investor Day, 2030 targets | 2026-09-02 | NEUTRAL | -2.9 / -1.3 / -10.7 / -14.3 | -3.3 / -2.8 / -10.2 / -14.7 | -2.7 / -2.1 / -6.5 / -12.1 | SNIPPET |
| E18 | Columbia: Investor Day, 2025 targets (14% op margin) | 2022-09-22 | NEUTRAL | -2.7 / -3.7 / -2.0 / +1.4 | -1.8 / -1.1 / +1.9 / +4.7 | +0.4 / +2.2 / +5.8 / +9.3 | OPENED |
| E19 | Levi Strauss: Investor Day, FY27 targets | 2022-06-01 | UP | +1.2 / +5.1 / +5.1 / -10.1 | +1.9 / +4.0 / +5.5 / -1.7 | +1.8 / +1.9 / +2.6 / +2.2 | OPENED |
| E20 | PVH: Investor Day, PVH+ Plan (15% op margin by 2025) | 2022-04-13 | NEUTRAL | +5.4 / +3.6 / +2.2 / -15.8 | +4.2 / +3.7 / +2.3 / -5.2 | +3.3 / +1.6 / -2.0 / -1.6 | SNIPPET |
| E21 | Tapestry: Investor Day 2022, FY25 targets | 2022-09-09 | NEUTRAL | +2.7 / +5.2 / -5.9 / -9.0 | +1.2 / +2.6 / -2.6 / +0.2 | +0.1 / +0.2 / -2.7 / +3.2 | SNIPPET |
| E22 | Tapestry: Investor Day 2025 Amplify, FY27-28 targets | 2025-09-10 | UP | +0.1 / +1.6 / +4.5 / +11.1 | -0.2 / +0.5 / +3.1 / +7.4 | +0.9 / +0.6 / +4.8 / +11.7 | SNIPPET |
| E23 | Ralph Lauren: Investor Day 2022, FY25 targets | 2022-09-19 | NEUTRAL | +3.0 / +0.8 / -10.2 / +2.4 | +2.3 / +1.2 / -4.6 / +7.5 | +0.6 / +0.9 / -0.3 / +9.2 | SNIPPET |
| E24 | Ralph Lauren: Investor Day 2025, 3-yr outlook | 2025-09-16 | NEUTRAL | -0.4 / -3.1 / -1.6 / +1.0 | -0.2 / -2.8 / -2.3 / +0.5 | -0.0 / -3.2 / -1.5 / +3.1 | SNIPPET |
| E25 | Capri: Investor Day, new long-term targets | 2025-02-19 | NEUTRAL | +5.0 / +1.6 / -1.8 / -3.1 | +4.7 / +1.8 / +1.0 / +4.3 | +5.6 / +2.5 / +2.4 / +12.7 | OPENED |
| E26 | Starbucks: Investor Day 2022, Reinvention plan (EPS 15-20%) | 2022-09-13 | UP | -1.4 / +4.1 / +1.9 / -3.2 | +2.9 / +8.1 / +8.1 / +9.5 | +3.8 / +8.0 / +7.4 / +13.4 | SNIPPET |
| E27 | Starbucks: Investor Day 2026, FY28 targets (13.5-15% margin) | 2026-01-29 | NEUTRAL | -1.3 / -3.4 / +1.0 / +3.7 | -1.2 / -2.8 / +3.5 / +5.1 | -0.9 / -2.9 / +4.5 / +7.7 | SNIPPET |
| E28 | Estee Lauder: Beauty Reimagined with Q2 FY25 results | 2025-02-04 | DOWN | -16.1 / -20.3 / -14.6 / -12.7 | -16.8 / -21.4 / -15.8 / -10.2 | -15.2 / -20.1 / -16.2 / -16.7 | SNIPPET |
| E29 | Crocs: Investor Day, $5B 2026 revenue, >26% op margin | 2021-09-14 | UP | +8.5 / +11.6 / +10.7 / -5.5 | +9.0 / +11.3 / +13.3 / -2.9 | +9.0 / +12.7 / +15.1 / +1.1 | SNIPPET |

Group = my classification (section 2). Sector for E26 is XLY and for E28 is XLP. E09 (Plank return, a leadership event) is shown in the CSV only.

## 4. Results

### 4.1 Group means and medians, abnormal return vs S&P 500 (percent, DERIVED)

| Group | n | Day 0 | Day 1 | Day 3 | Day 5 | Day 20 |
|---|---|---|---|---|---|---|
| UP (raised or above expectations) | 7 | +4.8 (med +2.9) | +6.2 (+4.9) | +7.9 (+5.8) | +8.1 (+5.5) | +3.9 (-1.7) |
| NEUTRAL (dated numeric, no evidence either way) | 13 | +0.9 | +0.8 | -0.2 | -0.6 | -1.3 |
| DOWN (cut, lowered or vague) | 8 | -10.8 (-9.7) | -14.0 (-14.0) | -15.0 (-13.8) | -14.9 (-13.7) | -19.2 (-16.1) |
| Memo: dated numeric, no cut (UP + NEUTRAL) | 20 | +2.3 | +2.7 | +2.6 | +2.5 | +0.5 |
| Memo: objective RAISED only (Nike 2015, Nike 2021, UA 2015, Levi 2022) | 4 | +5.4 | +5.9 | +7.5 | +8.1 | +3.4 |
| Memo: investor-day-only events (excluding 5 earnings-day events) UP / NEUTRAL / DOWN | 6 / 13 / 4 | +3.0 / +0.9 / -8.8 | +5.0 / +0.8 / -14.3 | n/a | +6.5 / -0.6 / -16.2 | +1.3 / -1.3 / -23.2 |

Against the sector basket the result is the same sign at every horizon (UP +4.7 / +6.3 / +8.7 / +9.4 at d0 / d1 / d5 / d20; DOWN -10.6 / -13.0 / -14.5 / -18.0). Permutation tests (20,000 shuffles, difference in means): dated-no-cut vs cut/vague p < 0.001 at d0, d1, d2, d3, d5 and d20 against both benchmarks; UP vs DOWN p between 0.0001 and 0.0004. Probability that a random dated-no-cut event beats a random cut/vague event is 0.92 to 0.99.

### 4.2 Test of the question asked

**Do dated, higher-than-consensus targets lead to rallies?** Yes, modestly, and only when "higher" is also credible near-term: +4.8% on day 0 and +8.1% by day 5 versus the S&P for the 7 UP events (all 7 positive on days 1 and 5). One of the 7 (Nike 2021, +15.2% on day 0) is an earnings-day event. Day 20 is mixed (3 of 7 positive), so the move is not a durable re-rating on its own.

**Do vague or lowered targets lead to selloffs?** Yes, and the selloff is bigger and more durable than the rally: 8 of 8 negative versus the S&P at every horizon from day 0 to day 20 (versus the sector basket, 7 of 8 are negative on day 1; the exception is adidas 2026 at +0.8 against a US basket). The two clean "vague" investor days (Under Armour Dec 2024, VF Mar 2025) lost -4.7% and -10.5% on day 0 and -16.2% and -42.3% by day 20 (the VF day-20 figure includes the April 2025 tariff crash; vs the sector basket it is -18.1%).

**What does not cause selloffs.** Dated, numeric, ambitious long-run targets with an unchanged near-term outlook. The 20 such events had a worst day-0 abnormal return of -4.7% (Lululemon 2022, re-issued Power of Three goals), -3.3% (Kontoor Helly Hansen 2026), -1.8% (Columbia 2022), -1.2% (Starbucks 2026, FY28 margin 13.5% to 15% vs 10.1% latest quarter). Their worst day-5 results were -10.2% (Kontoor 2026) and -6.3% (Lululemon 2022). Under Armour Dec 2018 is the cautionary case: ambitious 2023 targets (EPS CAGR about 40%) were buried by a 2019 outlook below consensus (revenue +3% to 4% vs about 5%; EPS 31 to 33 cents vs 33 cents consensus), and the stock fell -11.0% on day 0 and -13.3% by day 5 vs the S&P.

### 4.3 Other tests

| Hypothesis | Test | Result |
|---|---|---|
| Stocks that already fell hard are protected ("priced in") | Day-1 abnormal return for events with 52-week drawdown of 40% or more (n=3: VF 2022, Capri 2025, Estee Lauder 2025) | Mean -10.6% vs -1.0% for the rest; no protection. Weak test, n=3. Nike today: -47.7% from the 52-week high (high $67.46, DERIVED). |
| Rally into the event, then sell the news | Pre-event 10-day return vs S&P | UP +1.4%, NEUTRAL +0.9%, DOWN -0.7%: no systematic run-up that reverses. Not informative. |
| Rallies fade, sell-offs persist | Median day-20 abnormal return | UP median -1.7% (mean +3.9%); DOWN median -16.1%, 8 of 8 negative. Asymmetric persistence: bad news sticks. |
| Nike specifically | Three Nike target events: Oct 2015, Oct 2017, Jun 2021 | Day 5 raw +5.3%, +3.1%, +19.6%; day 20 +1.3%, +10.6%, +23.6%. No fade inside 20 days. The Oct 2024 postponement (-6.8% day 0, -14.2% by day 20) is the one adverse Nike precedent. |

### 4.4 Precedents that could not be priced

| Event | Facts | Why unpriced | Tag |
|---|---|---|---|
| Foot Locker Investor Day, Mar 2022 ("Lace Up", EBIT margin 8.5% to 9% by 2026, FY24 to FY26) | Shares -5.8% to $39.83 as 2023 EPS was guided well below analyst targets | Delisted after Dick's acquisition; no free daily history. Consistent with DOWN. | SNIPPET |
| Foot Locker Investor Day, Mar 20 2023 | Fool.com "Why Foot Locker got tripped up today" | Same | SNIPPET |
| Hanesbrands Full Potential plan, May 11 2021 (revenue about $7.4B, operating margin above 14% by 2024) | Reaction not found | Delisted after Gildan deal | SNIPPET |
| Skechers | No investor day found; $10B by 2026 goal reiterated in earnings releases | Taken private; Yahoo history gone | SNIPPET |
| Nike "2020 and 2023 investor days" (in the request) | I found no Nike Investor Day in 2020 or 2023. Nike's long-term targets in this period came in June 2021 with Q4 FY21 results (E03). The Nov 19 2024 Investor Day was postponed on Oct 1 2024 (E04). | Event apparently did not occur; not proven absent (EDGAR full-text search returns 403) | SNIPPET |
| adidas "Capital Markets Day 2023/2025" (in the request) | I found none. adidas targets came on Mar 10 2021 (Investor & Media Day, E05) and with FY25 results on Mar 4 2026 (E06). One Italian broker note mentions a possible first investor event under Gulden, with no date. | Not found | SNIPPET |
| Puma CMD 2024, Under Armour 2024 "plus Plank return" | UA: Plank return Mar 14 2024 (E09, excluded) and Dec 12 2024 investor day (E10). Puma: 2018 CMD (E11) and Jan 2025 nextlevel plan (E12). No Puma CMD found in 2024. | n/a | SNIPPET |

Survivorship note: the unpriced names (Foot Locker, Hanesbrands, Skechers) are exactly the ones that left the market; at least one (Foot Locker) fits the DOWN pattern. The priced sample therefore probably understates the frequency of bad outcomes.

## 5. Implication for Nike's Nov 16 to 17 Investor Day (short position)

### 5.1 What Nike has said and what is priced

- CFO Denton: "we're going to give you a financial algorithm, so you can begin to assess... what does the next 5 years begin to look like" (Q1 FY27 call; quote as recorded in repo `nike_standing.md` line 176, transcript opened there). That is a **dated, numeric, multi-year** target, so the event type is not "vague". The mix sits in the 20-event "dated, no cut" population unless Nike also cuts near-term guidance or sets a target below consensus.
- Bar to clear: consensus FY27 EBIT margin 5.7% and FY28 7.2%; FY28 EPS $1.65 (after falling from $2.22 in 30 days); FY28 revenue $43.6B (repo, `00_THESIS.md`). Any 5-year margin target above about 10% is "higher than consensus" by 3 points or more almost mechanically. The precedent question is therefore not "higher or lower" but "credible and paired with an unchanged near-term outlook, or not".
- Credibility record: every profit target in the Oct 2017 and Jun 2021 sets was missed (repo note 19), the Nov 2024 Investor Day was postponed, and the Dec 31 2026 clean-up date was dropped from the Q1 FY27 10-Q (thesis memo Reason 3). Precedent says markets still pay for the target on the day (Nike 2017, 2021).

### 5.2 Scenarios, using sample means vs S&P (DERIVED)

Price base $35.30. Short P&L is the negative of the stock's abnormal move; Nike's beta to the market is ignored.

| Scenario | Precedent set | Day 1 | Day 3 | Implied price (day 3) | Short P&L (day 3) |
|---|---|---|---|---|---|
| Credible algorithm above consensus, near-term unchanged | UP (n=7) | +6.2% | +7.9% | $38.1 | -7.9% |
| Same, tail case (Nike 2021 style) | max of UP | +13.5% | +17.6% (day 5) | $41.5 | -17.6% |
| Dated targets, no news either way | NEUTRAL (n=13) | +0.8% | -0.2% | $35.2 | +0.2% |
| Lowered/delayed target, near-term cut or vague | DOWN (n=8) | -14.0% | -15.0% | $30.0 | +15.0% |
| Same, tail case (Puma 2025) | min of DOWN | -23.7% | -25.6% (day 5) | $26.3 | +25.6% |

The DOWN tail ($26.3) sits at the top of the thesis downside range ($20 to $26); neither tail is a modal outcome.

Expected value of the short held through day 3, as a function of the probability of an UP outcome (p_U) and a DOWN outcome (p_D), with the remainder NEUTRAL:

EV = p_D x 15.0 - p_U x 7.9 + (1 - p_U - p_D) x 0.2, in percent of position.

| p_U \ p_D | 10% | 20% | 29% (sample) | 40% |
|---|---|---|---|---|
| 15% | +0.5 | +1.9 | +3.2 | +4.9 |
| 25% (sample) | -0.3 | +1.1 | +2.4 | +4.1 |
| 35% | -1.2 | +0.3 | +1.6 | +3.3 |
| 45% | -2.0 | -0.5 | +0.8 | +2.5 |

Break-even: p_D = 0.53 x p_U. At the sample base rates the short has a small positive expected value, but the distribution is a coin-flip-like payoff with a fat left tail (good for the short) and a rally branch that is likelier to be the first thing judges see. There is no evidence in 28 events of a free lunch: the all-event mean day-1 abnormal return is -2.1% and for investor-day-only events -0.7% (DERIVED), i.e., near zero.

### 5.3 Where Nike sits on the p_D question (my inference)

Reasons p_D is lower than the 29% base rate: Nike already re-based FY27 on Oct 1 (revenue down high single digits; FY27 EPS consensus fell from $1.71 to $1.29 in 30 days, repo), so a bundled near-term guide cut is less likely than at VF 2022, Puma 2025 or Estee Lauder 2025, where the Investor-Day-type message arrived with the cut. Reasons it is higher: a new CFO who "owns none of the prior guidance" has an incentive to reset the base (repo `advocate_long_fixable.md` line 309); the Q1 print implies Q2 to Q4 revenue falls 7.9% to 10.6% versus -4.3% in Q1 (thesis memo Reason 2), so a reaffirmed FY27 guide could still be cut on Dec 17; and Nike Oct 2024 is the one local example of withdrawal. The sample cannot separate these.

Reasons p_U is not small: short interest 99.2M shares (6.7% of shares, 2.6 days to cover; REPO note 17) is large but not squeeze fuel; the 4.6% yield attracts income buyers; credible dated plans (Crocs 2021, Levi 2022) rallied, while Tapestry 2025 gained only modestly (+0.5% day 1, +3.1% day 5 vs the S&P).

### 5.4 Asymmetric risk, stated plainly

1. **Timing.** Finals on Nov 19 fall on day 2 or day 3 of the window. The UP rally is at its mean peak around then (+7.3% day 2, +7.9% day 3, +8.1% day 5) and fades by day 20 (median -1.7%), whereas DOWN reactions compound (-14.0% day 1, -19.2% day 20). A short that is right on the 20-day horizon can look wrong on Nov 19 if the algorithm is credible.
2. **Skew of outcomes.** Size of tails: worst DOWN -23.7% (day 1), best UP +13.5% (day 1). Left tail is larger than right tail, which favours the short, but the right-tail probability for a dated algorithm without a near-term cut is the higher one.
3. **Costs inside the window.** The last four ex-dividend dates were Dec 1, Mar 2, Jun 1, Sep 1 at $0.41 (`data/nke_dividends_exdate.csv`), so the next ex-date (about Dec 1, my inference from the pattern) is after finals; the declaration (about Nov 14 to 20) is a signal event, not a cash cost. A large raise would go against the short; the memo expects a freeze or token raise. Borrow cost not obtained.
4. **Base-rate trap.** The 8 DOWN events are bad news by construction. Do not present "selloffs follow Investor Days" as a general rule; the supported statement is "selloffs followed Investor Days that came with a cut, a lowered or delayed target, or no numbers."

### 5.5 What to watch on Nov 16 to 17, mapped to the precedent groups

| Observation | Group it maps to | Expected abnormal move (days 1 to 5) |
|---|---|---|
| Dated FY30-31 operating margin target of 12% to 13% or more (the thesis bar is 13% at a 10% WACC) with a year-by-year bridge, FY27 guide reaffirmed | UP | +5% to +8% |
| Target below about 10% or timeline pushed beyond FY29 | DOWN (lowered/delayed: Puma 2025 pattern) | -14% to -25% |
| Revenue or margin guide for FY27 cut, or "annual guidance only" with no FY28 anchor | DOWN (vague/withdrawn: Nike 2024, VF 2025, UA 2024) | -10% to -17% |
| Numbers match consensus (about 7% FY28 margin, mid-to-high single digit growth) | NEUTRAL | about 0% |
| Segment disclosure (Performance vs Sportswear, partner weeks of supply, China timeline) | Not in sample; treat as information that can move either way | n/a |

Suggested use in the case: prepare the Nov 19 slide as a decision tree on the first three rows. The pitch survives an UP outcome only if it already argues that a dated target at or above 12% is not credible given 0-for-N on profit targets since 2017 and the FY27 revenue arithmetic; the numeric reaction in the first week is not the test.

## 6. Alternatives ruled out and limits (CLAUDE.md "go down the rabbit hole")

| Alternative explanation for the group differences | Test | Verdict |
|---|---|---|
| Market-wide moves, not company news | Abnormal vs S&P and vs sector basket; both reported | Rules out as sole driver. Residual confounds: SBUX Sep 13 2022 (CPI day, S&P -4.3% on day 0, SBUX -1.4% raw, +2.9% abnormal); VF Mar 2025 day 20 and UA Dec 2024 day 20 overlap the Apr 2025 and Jan 2025 volatility |
| Earnings-day bundling rather than the target | Re-run excluding the 5 earnings-day events (E03, E04, E06, E12, E28) | Same sign: UP +3.0 / +5.0 / +6.5, NEUTRAL +0.9 / +0.8 / -0.6, DOWN -8.8 / -14.3 / -16.2 at d0 / d1 / d5. Survives, but DOWN falls to n=4 |
| One outlier (Nike 2021, +15.2%) drives UP | Drop E03 | UP becomes +3.0 / +5.0 / +6.5 (d0 / d1 / d5). Survives |
| Day-0 timing error (after-close releases) | Checked Nike Oct 2024 and Puma Jan 2025; Kontoor May 2021 ran from 2:30 pm ET so day 0 is partial | Handled for the two; Kontoor E16 day-1 is the cleaner read (+0.6% raw) |
| Classification circularity: UP rows partly cite favourable press (E22, E26, E29) | Objective-only RAISED group (4 events from company documents) | Same direction and similar size (+5.4 / +5.9 / +8.1 / +3.4). Survives. NEUTRAL group has 13 events with no sign |
| DOWN is tautological (cut = bad news) | Not removable. Reported as a finding about what causes the selloffs, not as evidence that dated targets lower prices | Limit |
| Beaten-down stocks bounce | Drawdown split (n=3 at 40% or more) | No protection (-10.6% vs -1.0% day 1). Underpowered |
| Pre-event run-up reverses | Pre-10-day abnormal return by group | No pattern |
| Non-US stocks (adidas, Puma) vs US benchmarks | CSV also gives local-index and sector columns | Does not change group signs |

Other limits: n is small (28 events, groups of 7, 13, 8); returns are not beta-adjusted; the sector basket changes with data availability (5 to 16 names); the US basket is used for adidas and Puma; survivorship (section 4.4); adjusted close treats dividends as reinvested (immaterial over 20 days); consensus changes are not measured, so "higher than consensus" rests on 12 events with some evidence and is not tested on a numeric consensus gap. Statistical significance in section 4.1 should be read with the circularity caveat: the p-values test whether the groups differ, not whether the classification is independent of the news.

## 7. Route log for the "inconclusive" items (CLAUDE.md rule)

**Item A: consensus estimate revisions after each event (requested "consensus change after").** Result: NOT obtained at event level. Routes tried: (1) WebSearch per event for analyst commentary on expectations, partial (usable for UA 2018, Puma 2025, EL 2025, Capri 2025, VF 2022 only via guidance tables); (2) SEC 8-K Ex 99.1 for Levi, VF, Columbia, Capri, partial (gives prior targets, never consensus); (3) Yahoo `quoteSummary?modules=earningsTrend` blocked ("Invalid Crumb"; also current-only); (4) Wayback `finance.yahoo.com/quote/UAA/analysis` (Dec 2018) and `VFC/analysis` (Mar 2025): no snapshot; (5) Nasdaq historical API: returns prices only, delisted symbols "Symbol not exists"; (6) Stooq (CSV and .pl mirror): connection reset or JavaScript challenge; (7) TipRanks / TheFly / MarketBeat price-target pages: undated or post-hoc, partial. Number of genuinely different routes failed: 7. What would settle it: FactSet, Bloomberg BEst or Refinitiv I/B/E/S snapshots of FY+2 EBIT margin and EPS on the day before and 5 days after each event (see `research_notes/Refinitiv pull list.md`), or sell-side previews and post-event notes from a library terminal. For Nike itself this is available from the repo's own consensus tables.

**Item B: daily prices for Foot Locker, Hanesbrands, Skechers.** Result: NOT obtained. Routes: (1) Yahoo chart API with the ticker and variants (FL, FL.DL, HBI, HBI.DL, SKX): "No data found, symbol may be delisted"; (2) Nasdaq API: "Symbol not exists"; (3) Stooq: reset; (4) Financial Modeling Prep demo key: invalid; (5) Wayback of Yahoo history pages: no snapshot; (6) Wayback of macrotrends: annual summary only (Aug 2025 snapshot), no daily data. Six routes failed. What would settle it: CRSP or Bloomberg daily history, or a library terminal.

**Item C: Nike 2020 and 2023 investor days.** Result: none found. Routes: (1) three WebSearch queries for 2020, 2023 and history; (2) the investors.nike.com Oct 25 2017 page and the page listing (no event archive visible); (3) repo notes (they cite only the Oct 2017 and Jun 2021 sets); (4) EDGAR full-text search: blocked (403). Fewer than five genuinely distinct routes; I therefore report "not found" and not "did not occur". What would settle it: Nike IR calendar archive via web.archive.org or the 8-K Item 7.01 list on EDGAR.

**Item D: adidas "Capital Markets Day 2023/2025" and Puma CMD 2024.** Not found after four search variants (including German-language queries); see section 4.4.

## 8. Sources

- Prices: Yahoo Finance chart API (`query2.finance.yahoo.com/v8/finance/chart`), pulled Oct 14 2026, OPENED; Nike also `data/nke_daily_prices.csv` (repo).
- OPENED primary: Levi Strauss 8-K Ex 99.1 Jun 1 2022 (`sec.gov/Archives/edgar/data/94845/000009484522000030/exhibit991-june12022pressr.htm`); VF 8-K Ex 99.1 Sep 28 2022 (`sec.gov/Archives/edgar/data/103379/000119312522252793/d383894dex991.htm`); Columbia 8-K Ex 99.1 Sep 22 2022 (`sec.gov/Archives/edgar/data/1050797/000105079722000068/colm2022investordayex991.htm`); Capri 8-K Ex 99.1 Feb 19 2025 (`sec.gov/Archives/edgar/data/1530721/000153072125000026/cpri8-k021825exhibit991.htm`); SGB Mar 7 2025 on VF (`sgbonline.com/?p=335876`); Investing.com Oct 25 2017 on Nike (`investing.com/news/stock-market-news/nike-gives-upbeat-forecast-at-investor-conference-shares-rise-547754`).
- SNIPPET (search summaries; confirm before use): Nike 2015 (CNBC, Fortune, Benzinga), Nike 2021 (SGB / Retail Dive), Nike Oct 2024 (TipRanks, Fool, Fortune, Bernstein quote), adidas 2021 and 2026 (Retail TouchPoints, adidas annual report, Invezz, Il Sole 24 Ore, FashionUnited), Under Armour 2015, 2018, 2024 (press release, Benzinga, CNBC, Investing.com, Sportico, Axios), Puma 2018 and 2025 (Puma release Mar 20 2018, optionfinance, World Footwear), Lululemon 2022 (Coresight), PVH 2022 (SGB), Tapestry 2022 and 2025 (Business Wire, analyst summaries), Ralph Lauren 2022 and 2025 (Coresight, Briefing.com), Starbucks 2022 and 2026 (Fool, Benzinga, Stocktwits), Estee Lauder 2025 (Benzinga), Crocs 2021 (Bloomberg, Investing.com), Kontoor 2021 and 2026 (Kontoor, FashionUnited), Foot Locker 2022 and 2023 (Fool).
- Repo: `research_notes/Thesis decision/00_THESIS.md`, `advocate_long_peak_pessimism.md`, `advocate_long_fixable.md`, `advocate_short_cash_dividend.md`, `research_notes/Gulden and Plank turnarounds vs Nike/nike_standing.md`, `data/nke_dividends_exdate.csv`.
- Reproduction: scripts are in the session scratchpad (`es.py`, `events.py`, `build.py`, `stats.py`); the CSV is the output of `build.py`. Not copied into the repo.
