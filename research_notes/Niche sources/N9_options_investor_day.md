# N9: What the NKE option market prices for Investor Day (Nov 16 to 17), finals (Nov 19) and Q2 FY27 (about Dec 17)

Prepared 2026-10-15. Task N9 in `RESEARCH_MAP.md`. Tags: OPENED = I fetched and parsed the source in this session; SNIPPET = seen only in a search or page excerpt; DERIVED = my arithmetic from tagged inputs; REPO = taken from an existing repo note (not re-verified here).

## 0. Answer in six lines

1. **The options price Investor Day as one ordinary-sized event with no direction.** Variance differencing of the Nov 13 and Nov 20 expiries gives a 1-sd event move of **4.2% to 4.9%** (expected absolute move 3.4% to 3.9%), so D4's "about 3.6%" is an expected absolute move, not a 1-sd move (DERIVED, section 2). The whole Nov 13 to Nov 20 window has a 1-sd move of 6.7%.
2. **Market-implied tails for that window are thin: P(up more than 6%) 17% to 18%, P(down 10% or more) 5.5% to 6.2%, P(down 15% or more) 0.8% to 1.1%** (DERIVED, section 3). D7's historical mixture (25% UP, 46% neutral, 29% DOWN) implies 18%, 22% and 14%. D4's 8/42/50 probabilities with D7 means imply 7%, 38% and 25%. The market agrees with us on the upside and prices the down tail at one quarter to one twentieth of what our own base rates say.
3. **Skew is flat.** 25-delta risk reversal (put IV minus call IV) is -0.0 vol points for Nov 20 and +0.7 for Dec 18. Every peer I could pull the same day has a larger put premium (SPY +4.6 to +5.0, CROX +3.7 to +4.2, VFC +2.7, ONON +2.6, DECK +0.8 to +5.7, LULU 0.0 to +0.4). The downside is not expensive.
4. **Positioning in options is not crowded short.** Put/call open interest is 0.66 across all expiries (978,981 puts vs 1,475,285 calls); the near-money strikes 26.5 to 44 are puts-heavy (1.25) but the sign of the positions (who is long) is not in the data. With zero skew, the data do not show a rush to buy protection.
5. **Cost of the short is about 4% of spot for an at-the-money put through finals, 3.7% for a 35/30 put spread, 2.6% for the spread financed by a 40 call** (natural prices, 2026-10-14 close). At the market's own distribution the expected value of every structure is about minus the half-spread. They only have positive expected value if the DOWN probability is above 10% to 17% (at a -10% to -15% DOWN mean, section 5).
6. **Smoking gun: NO.** The option market does not settle long or short. It does show that the downside tail we believe in is cheap, not already in the price.

## 1. Data: what is a quote and what is derived

All chain numbers below are quotes unless marked DERIVED.

| Item | Value | Source and timestamp | Tag |
|---|---|---|---|
| NKE close | $35.30 (Oct 14) | Yahoo `regularMarketPrice` 35.30 at epoch 1792008002 = 2026-10-14 20:00:02 UTC (16:00 ET); AlphaQuery "Last Closing Price 35.30 (2026-10-14)"; Nasdaq "LAST TRADE $35.3 AS OF OCT 14, 2026" | OPENED |
| Full chain, 18 expiries, 1,114 contracts | bid, ask, last, volume, open interest, delta | CBOE delayed quotes `cdn.cboe.com/api/global/delayed_quotes/options/NKE.json`, file timestamp "2026-10-15 01:40:52" (timezone not stated; quotes are the Oct 14 close; the CBOE `current_price` field shows 35.06, a 15:59:59 print that disagrees with the 35.30 official close, so I do not use it; parity forwards confirm 35.30, see below) | OPENED |
| Cross-check chain | 18 expiries | Yahoo `v7/finance/options/NKE?date=...` with crumb (needs the cookie from `fc.yahoo.com`, no login). 345 near-money contracts: bid/ask mids identical to CBOE to the cent; open interest equal in 98.9% of contracts. Both are the OPRA consolidated tape, so this is a transcription check, not independent evidence | OPENED |
| Third cross-check | Nov 20 strikes 17.5 to 42.5 | Nasdaq `api.nasdaq.com/api/quote/NKE/option-chain` (no login): bid/ask and open interest identical to CBOE | OPENED |
| 30-day IV mean 34.54%, 60-day 38.84%, 90-day 40.32%; 30-day close-to-close historical vol 23.74% (60-day 27.03%, 90-day 26.96%); P/C volume 0.34 (30-day), P/C OI 0.50 | 2026-10-14 | AlphaQuery volatility pages | OPENED |
| CBOE `iv30` | 34.17% | same CBOE file | OPENED |
| Rate | 4.05% | 13-week bill, REPO `research_notes/17_insider_and_institutional_flows.md` (^IRX) | REPO |
| Forward per expiry | Oct 16: 35.31; Nov 13: 35.39; Nov 20: 35.46; Dec 18: 35.24; Jan 15: 35.37; Jun 17: 35.47 | Put-call parity, median of the 6 strikes nearest spot, mids. The Oct 16 forward (2 days) of 35.31 matches the 35.30 close. Dec 18 sits below spot because it spans the $0.41 Dec 1 ex-dividend date | DERIVED |
| Implied vols | all | Black-76 off those forwards, OTM options only, mids, spread filter (spread above max($0.20, 25% of mid) dropped) | DERIVED |

Files: `data/niche/N9_nke_chain_2026-10-14.csv` (every contract with CBOE and Yahoo fields, forward, IV), `N9_cboe_raw_2026-10-14.json` (raw CBOE file), `N9_term_structure_2026-10-14.csv`, `N9_oi_by_strike_2026-10-14.csv`, `N9_peer_skew_2026-10-14.csv`, `N9_strategy_ev_2026-10-14.csv`, `N9_sensitivity_nov20.csv`, `N9_event_windows.json`, `N9_density_summary_{quad,svi}.json`, `N9_rn_density_*`, `N9_*_repricing_*`. Code: `scripts/niche/n9_chain.py`, `n9_term.py`, `n9_density.py`, `n9_strat.py`, `n9_peers.py` (run with `python3 -I`, scratch dir with the raw files, output dir).

Contract listing gaps: there is no Nov 14 expiry (it is a Saturday); the pre-event expiry is **Nov 13** (Friday). There is no Dec 11 or Dec 19 weekly; the Q2 comparison is Dec 18 against **Nov 27**, a 15-trading-day gap. Listed expiries in the window: Oct 16, 23, 30; Nov 6, 13, 20, 27; Dec 18; Jan 15; Mar 19; Apr 16; Jun 17.

## 2. ATM implied volatility term structure and event moves

### 2.1 Term structure (DERIVED from quotes; ATM IV interpolated at the forward)

| Expiry | Days | ATM IV | ATM straddle (nearest strike, mid) | % of spot | Put/call OI |
|---|---|---|---|---|---|
| Oct 23 | 9 | 34.3% | $1.53 | 4.3% | 0.50 |
| Oct 30 | 16 | 34.0% | $2.04 | 5.8% | 0.38 |
| Nov 6 | 23 | 35.0% | $2.50 | 7.1% | 0.77 |
| **Nov 13** | 30 | **34.5%** | $2.80 | 7.9% | 0.50 |
| **Nov 20** | 37 | **37.5%** | $3.35 | 9.5% | 0.80 |
| Nov 27 | 44 | 36.9% | $3.58 | 10.1% | 0.68 |
| **Dec 18** | 65 | **39.1%** | $4.63 | 13.1% | 0.50 |
| Jan 15 | 93 | 40.3% | $5.67 | 16.1% | 0.49 |
| Mar 19 | 156 | 39.0% | $7.13 | 20.2% | 0.56 |
| Apr 16 | 184 | 39.9% | $7.90 | 22.4% | 0.88 |
| Jun 17 | 246 | 39.8% | $8.98 | 25.4% | 1.09 |

(The 2-day Oct 16 expiry shows 38.2%, which is not informative.) Compared with REPO note 17's Oct 13 snapshot (forward-based, Yahoo): Nov 13 33.7% to 34.5%, Nov 20 37.3% to 37.5%, Dec 18 39.4% to 39.1%, Jun 17 39.6% to 39.8%. The surface moved by under one vol point in a day. Implied 30-day vol of 34.5% compares with 23.7% realized (AlphaQuery), a ratio of 1.45.

### 2.2 Investor Day window: Nov 13 close to Nov 20 close (5 trading days: Nov 16, 17, 18, 19, 20)

Method (standard variance differencing, DERIVED): total variance W = IV^2 x T (calendar years). Window variance = W(Nov 20) - W(Nov 13) = 0.004489 (1-sd 6.70%). Subtract the ordinary variance of five trading days, taken from the forward variance of other one-week gaps between weekly expiries:

| One-week forward variance between expiries | Value | Note |
|---|---|---|
| Oct 16 to Oct 23 | 0.00210 | clean |
| Oct 23 to Oct 30 | 0.00216 | clean |
| Oct 30 to Nov 6 | 0.00267 | contains the Nov 3 US election, so I treat it as the high base |
| Nov 6 to Nov 13 | 0.00204 | clean |
| **Nov 13 to Nov 20** | **0.00449** | the window; 2.1x a clean week |
| Nov 20 to Nov 27 | 0.00216 | 4 trading days (Thanksgiving) |

| Baseline used | Base variance | Event variance | Event 1-sd | Expected absolute move (0.8 x sd) |
|---|---|---|---|---|
| Mean of three clean weeks (0.00210) | 0.00210 | 0.00239 | **4.9%** | 3.9% |
| Election week (0.00267) | 0.00267 | 0.00182 | 4.3% | 3.4% |
| Nov 27 week scaled to 5 days (0.00270) | 0.00270 | 0.00179 | 4.2% | 3.4% |

Straddle check (simple, no differencing): Nov 20 straddle 9.49% of spot vs Nov 13 7.92% (matches the 9.5% and 8.0% quoted in D4). Reading: the extra straddle cost of 1.6 points is the market's price for the week; D4's "about 3.6%" equals the expected absolute move in the table (3.4% to 3.9%). **Use a 1-sd of 4.2% to 4.9% when comparing to D7 distributions.**

Confounds that cannot be removed with this chain (listed, not tested): Nov 20 is a standard monthly expiry, finals on Nov 19 are not a Nike event, and the same week can contain retailer earnings and macro prints (dates not checked). The 2.1x ratio therefore overstates the pure Nike Investor Day premium to an unknown degree; the event number is an upper bound on the Investor-Day-specific part.

### 2.3 Q2 FY27 window: Dec 18 expiry vs Nov 27 expiry (15 trading days)

Window variance 0.01083. Base per trading day from clean weeks 0.00042 (Nov 27 week 0.00054):

| Baseline | Event 1-sd | Expected absolute move |
|---|---|---|
| Clean weeks, 0.00042 per day | **6.7%** | 5.4% |
| Nov 27 week, 0.00054 per day | 5.2% | 4.2% |
| Election week, 0.00053 per day | 5.3% | 4.2% |

Compare: REPO note 17 (Oct 13) 6.4% to 7.2%; Nike's last 14 earnings reactions have a mean absolute move of 8.33%, median 6.73%, standard deviation 9.58%, 10 of 14 negative (REPO `data/flows/earnings_day_moves.csv`, mean -3.59%). So the options price Q2 at 0.6x to 0.8x the mean historical absolute move and about the median. Caveats: (a) the window also contains the Belgian customs hearing (Nov 30, press), the Dec 1 ex-dividend date and the aftermath of Investor Day; I cannot split them; (b) the Q2 date is an estimate (Yahoo flagged it as estimated in REPO note 17); if the print lands after Dec 18 the Dec 18 expiry does not contain it, and Jan 15 vs Nov 27 gives 8.5% to 10.5% but absorbs other events.

## 3. Risk-neutral distribution and tail probabilities

Method (DERIVED): take OTM mid IVs for the expiry, fit a smooth smile, price calls on a 4,001-point strike grid, take the second derivative in strike (Breeden-Litzenberger, density = e^(rT) d2C/dK2). Two smoothers: a quadratic in log-moneyness fit weighted by 1/spread (primary; density integrates to 1.000, 7 of 4,001 grid points slightly negative) and raw SVI (cross-check; its parameters hit bounds and 900 to 1,000 grid points are slightly negative in the far wings, so I treat it as a bound only). The Nov 20 chain has only $2.5 strike spacing away from 35, so the fit is smoothing about eight points; the fit reprices the market to within a few cents inside 30 to 42.5 (`N9_quad_repricing_2026-11-20.csv`).

### 3.1 From today's close ($35.30) to Nov 19 (includes about 26 trading days of ordinary vol)

Nov 20 density rescaled one trading day to Nov 19 (log-returns scaled by 0.985).

| Event | Quadratic smile | SVI | Flat-vol lognormal at 37.5% (reference, Nov 20) |
|---|---|---|---|
| Up more than 6% (above $37.42) | 29.2% | 30.1% | 30.5% |
| Down 10% or more (below $31.77) | 17.4% | 18.4% | 19.5% |
| Down 15% or more (below $30.00) | 8.3% | 9.3% | 9.0% |
| Up more than 10% | 18.8% | 19.5% | |
| Down 20% or more | 3.7% | 4.2% | |
| P(Nov 20 close above $40) | 12.9% | 13.3% | |
| P(Nov 20 close below $30) | 8.6% | 9.5% | |

These include a month of ordinary volatility before the event, so they are not comparable to D7's event-window base rates. The like-for-like comparison follows.

### 3.2 Event window (Nov 13 close to Nov 20 close) against D7 and D4 (DERIVED, 400,000 draws each, `scripts/niche/n9_strat.py`)

Market window: lognormal with 1-sd of 6.7% (base 4.6% plus event 4.9%, martingale), no skew (risk reversal is 0), with an alternative where the event leg is Student-t with 4 degrees of freedom. D7 mixture: UP, NEUTRAL and DOWN day-3 abnormal returns drawn from the group means and standard deviations in `D7_event_table.csv` (UP +7.9 / 4.6, NEUTRAL -0.2 / 2.9, DOWN -15.0 / 6.7) plus 2% sd for market noise over four days (an assumption I made; it makes the tails slightly wider).

| Window outcome | Market (normal) | Market (fat event leg) | D7 base rates 25/46/29 | D4 probs 8/42/50 with D7 means | D4 probs, DOWN mean -8% |
|---|---|---|---|---|---|
| P(up more than 6%) | 18.3% | 16.7% | 18.1% | 6.9% | 7.9% |
| P(down 10% or more) | 6.2% | 5.5% | 21.9% | 38.3% | 19.5% |
| P(down 15% or more) | 0.8% | 1.1% | 14.2% | 25.1% | 7.9% |
| Mean | 0.0% | 0.0% | -2.4% | -7.0% | -3.5% |
| Sd | 6.7% | 6.8% | 10.0% | 10.0% | 7.5% |
| P(absolute move above 10%) | 13.5% | 11.8% | 30.4% | 41.1% | 22.5% |

Reading, in numbers:
- Up tail: the market's 17% to 18% matches D7's 18%. D4's own "8% probability of an up move of 10% or more over 5 days" compares with a market window probability of 7.3% (DERIVED: normal, 1-sd 6.7%); they agree.
- Down tail: D4's own judgment of "20% probability of down 8% or more" compares with 11.4% in the market window (DERIVED). D7's DOWN scenario, if it happens at its mean (-15.0%), is a 2.4-sd move in the market's distribution (0.8% to 1.1%). The market prices the DOWN branch at roughly 1/14th to 1/20th of D7's sample frequency for -15% and 1/4th for -10%.
- This does not prove the options are wrong. D7 itself says its 8 DOWN events are "bad news by construction" and that the all-event mean day-1 abnormal return is -2.1% and for investor-day-only events -0.7%, close to zero. If the investor-day-only mean of -0.7% is the right prior, the market is about right. The test that decides is whether Nike's Nov 16 to 17 content looks like D7's DOWN class (lowered or delayed target, near-term cut, or no numbers). D4 puts 50% on "short confirmed"; the mapping of "short confirmed" to D7's DOWN class is an assumption (D4 does not require a near-term guide cut), which is why the -8% variant is shown.

Alternatives I ruled out for why the market down tail is thin: (a) a strike-spacing artifact of the fit: ruled out, raw SVI gives 9% to 10% for -15% from today and does not change the window result, which is built from variance not strikes; (b) stale quotes: ruled out, Yahoo, Nasdaq and CBOE agree to the cent and the Oct 16 forward matches spot; (c) dividend confusion in the Nov 20 expiry: ruled out, there is no ex-date before Nov 20 (ex-date about Dec 1 per D7); (d) a thin wing in the quotes: partly, the 27.5 put is quoted 0.05 to 0.15, so the far left tail beyond -22% is not resolvable.

## 4. Skew: Nike against its own history and peers

All values are in vol points, same method, same day (DERIVED from CBOE chains).

| Name | Expiry | ATM IV | 25-delta put minus call | 90% put minus 110% call | 80% put minus 120% call | P/C OI |
|---|---|---|---|---|---|---|
| **NKE** | Nov 20 | 37.5% | **-0.0** | +0.1 | +5.7 | 0.80 |
| **NKE** | Dec 18 | 39.1% | **+0.7** | +0.5 | +1.9 | 0.50 |
| LULU | Nov 20 / Dec 18 | 41.7% / 50.9% | 0.0 / +0.4 | 0.0 / +0.3 | +0.8 / +0.5 | 0.74 / 0.51 |
| DECK | Nov 20 / Dec 18 | 50.6% / 45.7% | +0.8 / +5.7 | +0.8 / +5.3 | +1.3 / n.a. | 1.25 / 1.19 |
| ONON | Dec 18 | 46.3% | +2.6 | +1.8 | +4.5 | 0.66 |
| VFC | Nov 20 | 57.5% | +2.7 | +2.1 | -0.4 | 0.22 |
| CROX | Nov 20 / Dec 18 | 50.1% / 46.3% | +4.2 / +3.7 | +4.7 / +4.8 | n.a. | 1.48 / 0.38 |
| SPY | Nov 20 / Dec 18 | 13.5% / 14.0% | +4.6 / +5.0 | +11.3 / +10.7 | n.a. | 5.71 / 2.37 |

Nike's skew is as flat as LULU's (the only peer in the same range) and 2 to 5 points below DECK (Dec 18), ONON, VFC, CROX and SPY. The 80%/120% wing figure for Nov 20 (+5.7) rests on thin quotes (27.5 put 0.05/0.15) and should not be read. Several peer near-month expiries may contain their own earnings prints (dates not checked), which can add to skew, so treat the peer comparison as indicative.

**Nike's own history of skew: not obtained.** Only two data points exist in the repo and here: REPO note 17 on Oct 13 (90/110 skew +0.35 for Nov 20, +1.26 for Dec 18; it states skew is 0 to 1.3 points for every expiry from Nov on) and today's +0.14 and +0.50. So the skew has been flat for at least two days. The routes to a longer history are in section 7.

## 5. Three ways to express the short through finals and through Q2

Entry at the Oct 14 close prices. "Natural" = pay the ask on long legs and receive the bid on short legs; "mid" in the CSV. Held to expiry; payoffs discounted at 4.05%. All per share (multiply by 100 per contract), no commissions. Max loss is the debit paid unless a short call is present. Strikes are the listed 2.5-dollar strikes around 35.

### 5.1 Costs, breakevens and payoffs (quotes for cost, DERIVED for the rest)

**Through finals: Nov 20 expiry** (35 put 1.42/1.47, volume 2,540, OI 19,900; 30 put 0.16/0.19; 40 call 0.40/0.41; 37.5 call 0.87/0.97)

| Structure | Net debit (natural) | % of spot | Max loss | Breakeven | Max gain | P&L if $38 / $30 / $43.5 |
|---|---|---|---|---|---|---|
| A. Long 35 put | 1.47 | 4.2% | 1.47 | 33.53 (-5.0%) | 33.53 (stock to zero) | -1.47 / +3.53 / -1.47 |
| B. Put spread, long 35 put / short 30 put | 1.31 | 3.7% | 1.31 | 33.69 (-4.6%) | 3.69 at $30 or below (-15.0%) | -1.31 / +3.69 / -1.31 |
| C. Spread financed by short 40 call | 0.91 | 2.6% | 0.91 below $40; above $40 loses $1 per $1 | 34.09 (-3.4%) | 4.09 | -0.91 / +4.09 / -4.41 |
| C2. Same, short 37.5 call | 0.44 | 1.2% | 0.44 below $37.50; above loses $1 per $1 | 34.56 (-2.1%) | 4.56 | -0.94 / +4.56 / -6.44 |
| Memo: long 32.5 put | 0.59 | 1.7% | 0.59 | 31.91 (-9.6%) | 31.91 | -0.59 / +1.91 / -0.59 |
| Memo: 32.5/27.5 put spread | 0.54 | 1.5% | 0.54 | 31.96 (-9.5%) | 4.46 | -0.54 / +1.96 / -0.54 |

The short 40 call has a risk-neutral probability of finishing in the money of about 13% by Nov 20 (quadratic smile; 13.3% SVI), so it is not a remote leg. Financing is partial: the 40 call bid of 0.40 offsets 30% of the 1.31 spread debit.

**Through Q2: Dec 18 expiry** (35 put 2.13/2.22, OI 23,886; 30 put 0.41/0.56; 40 call 0.73/0.79; 37.5 call 1.38/1.48; spreads are wider than for Nov 20)

| Structure | Net debit | % of spot | Breakeven | Max gain |
|---|---|---|---|---|
| A. Long 35 put | 2.22 | 6.3% | 32.78 (-7.1%) | 32.78 |
| B. Put spread 35/30 | 1.81 | 5.1% | 33.19 (-6.0%) | 3.19 |
| C. Spread + short 40 call | 1.08 | 3.1% | 33.92 (-3.9%) | 3.92 |
| C2. Spread + short 37.5 call | 0.43 | 1.2% | 34.57 (-2.1%) | 4.57 |

The Dec 18 puts also benefit from the $0.41 Dec 1 dividend already in the prices (the Dec 18 forward is 35.24). Q2 cost is higher because the 35 put carries the full month of ordinary vol plus the print.

### 5.2 Expected value (DERIVED, simulation described in section 3.2; natural prices)

Pre-event path to Nov 13 at the market's Nov 13 vol (9.9% sd, martingale); event outcome drawn from the scenario's day-3 abnormal return; for Dec 18 the day-20 abnormal return (D7: UP +3.9 / 8.7, NEUTRAL -1.3 / 9.5, DOWN -19.2 / 12.9) plus 4.5% market noise, then a Q2 reaction drawn either from Nike's 14 historical reactions ("history", mean -3.6%) or from a zero-mean normal at the implied 6.7% ("implied"). The D4 probabilities are applied to the three D7 classes: long wins = UP, mixed = NEUTRAL, short confirmed = DOWN.

**Nov 20 (finals), EV per share and as a percent of the debit; probability of profit in brackets**

| Distribution | A. 35 put | B. 35/30 spread | C. spread + short 40 call |
|---|---|---|---|
| Market (risk neutral) | -0.025 (half-spread) | -0.04 | -0.045 |
| D7 base rates 25/46/29 | +0.72, +49% (42%) | +0.41, +31% (43%) | +0.46, +51% (46%) |
| D4 probs 8/42/50, DOWN mean -15% | +1.69, +115% (56%) | +1.07, +81% (57%) | +1.29, +141% (60%) |
| D4 probs 8/42/50, DOWN mean -8% | +0.70, +47% (46%) | +0.52, +39% (47%) | +0.70, +77% (51%) |
| No news only (NEUTRAL) | -0.16, -11% (33%) | -0.09, -7% (35%) | +0.09, +10% (39%) |

The "market" row is natural cost minus mid cost: at mid the structures are fair by construction (the fitted density reprices the quotes to within 1 to 7 cents, inside 30 to 42.5), so the expected loss is the half-spread paid on entry (put 0.025, spread 0.04, financed spread 0.045), before any exit cost.

5th-percentile outcomes under D7 base rates: A and B lose the full debit (-1.47, -1.31); C loses 3.63 per share (10% of spot) because the short call is exercised in the UP branch.

**Dec 18 (Q2), EV per share (history Q2 / implied Q2)**

| Distribution | A. 35 put | B. 35/30 spread | C. spread + short 40 call |
|---|---|---|---|
| D7 base rates | +1.98 / +1.14 | +0.77 / +0.37 | +1.02 / +0.52 |
| D4 probs, D7 means | +3.14 / +2.27 | +1.23 / +0.88 | +1.63 / +1.21 |
| D4 probs, DOWN mean -8% | +1.92 / +1.06 | +0.84 / +0.44 | +1.15 / +0.65 |
| No news only | +0.86 / +0.03 | +0.42 / -0.05 | +0.63 / +0.04 |

Debits for reference: 2.22, 1.81, 1.08. Under the market-consistent "implied" Q2 and no ID news the EV is about zero, as it should be.

### 5.3 What probability do we need? (Nov 20, `N9_sensitivity_nov20.csv`)

Break-even DOWN probability (EV = 0 at natural prices; UP probability fixed; DOWN mean at day 3):

| UP probability | DOWN mean | A. 35 put | B. 35/30 spread | C. spread + short 40 call |
|---|---|---|---|---|
| 25% (D7 sample) | -15% | 10% | 12% | 11% |
| 25% | -10% | 16% | 17% | 16% |
| 25% | -5% | 32% | 33% | 30% |
| 8% (D4) | -15% | 10% | 10% | 10% |
| 8% | -10% | 10% | 10% | 10% |
| 8% | -5% | 20% | 17% | 10% |

(Grid starts at 10%, so "10%" means "10% or lower"). D7's sample DOWN frequency is 29% and D4's is 50%; the market-implied probability of a move of -10% or worse is 6%. The structure pays if the true probability of a D7-style DOWN outcome exceeds 10% to 17% and the outcome averages -10% or worse; it needs 30% or more if the DOWN outcome is only -5%.

Structure choice (DERIVED reasoning, no opinion): the outright put has the highest EV when the DOWN branch is large (D4 probabilities) because D7's DOWN tail goes beyond the $30 cap (day-5 worst -25.6%); the spread has the best loss limit per dollar (max loss 1.31 against max gain 3.69, 2.8 to 1); the financed version has the highest EV per dollar of debit but converts the UP branch (probability about 18% for more than +6%) into an uncapped loss above $40. D7's UP tail case (+17.6% by day 5) is $41.5, where the financed spread loses 2.41 (0.91 debit plus 1.50 on the call), so a short 40 call is breached exactly in the branch that is the main risk to the short.

Timing observation (DERIVED, not simulated at multiple entry dates): the Nov 20 35 put today costs 1.47 because it includes 26 trading days of ordinary vol. The window-only value of an ATM put on Nov 13 at the same 37.5% IV is about F x (2N(sigma/2) - 1) with sigma = 6.7% (ATM forward put equals call), which is about $0.95. Buying on Nov 12 or 13 instead of today would cost about a third less if the spot and IV are unchanged, but gives up protection against a pre-event move (9.9% sd) and runs the risk that IV ramps into the event. I did not model the ramp.

## 6. Open interest, volume and whether the options already show a heavy short

All from the CBOE file (OI is the previous-day figure; volume is Oct 14). 

| Slice | Puts | Calls | P/C OI |
|---|---|---|---|
| All 18 expiries | 978,981 | 1,475,285 | 0.66 |
| Oct 16 to Jun 17, 2027 | 692,123 | 1,172,239 | 0.59 |
| Strikes 26.5 to 44, all expiries | 709,441 | 566,672 | 1.25 |
| Nov 20 | 93,476 | 117,311 | 0.80 |
| Dec 18 | 102,797 | 205,942 | 0.50 |
| Jan 15 | 153,757 | 314,664 | 0.49 |
| Volume Oct 14, Oct to Jun | 18,590 | 38,886 | 0.48 |

Delta-adjusted shares of open interest (CBOE deltas, unsigned): puts 49.1M, calls 27.1M, all expiries; 25.5M and 12.9M through Jan 15. Gross put contracts equal 97.9M shares, close to short interest of 99.2M shares at Sep 30 (REPO note 17), and 13F-reported puts were 77.7M shares at Jun 2026, held mostly by market makers (REPO note 17). Coincidence of totals is not evidence of a link; OI does not say who is long.

Largest strike concentrations: Nov 20: 40 call 28,137; 37.5 call 22,275; 32.5 put 22,270; 35 put 19,900; 35 call 19,031; 30 put 17,476. Dec 18: 40 call 24,284; 35 put 23,886; 40 put 14,047. Jan 15: 40 put 30,148; 50 call 29,907; 60 call 28,981; 40 call 20,899. Oct 16: 40 call 53,544 and 35 put 40,054. Many far calls (50, 60, 77.5) are stale holdovers from higher prices (same finding as REPO note 17).

Oct 13 to Oct 14 open-interest change on 961 matched contracts (REPO Oct 13 chain vs today): puts +4,720, calls +11,580 contracts on a base of 2.45M; no build. Biggest changes: Oct 16 35.5 call +2,690, Jun 2027 25 put +1,865.

Is positioning already heavily short through options? Evidence against: (1) total P/C OI 0.66 and Oct-Jun volume P/C 0.48 are call-heavy; (2) skew is zero, so puts are not bid relative to calls (SPY, CROX, VFC, ONON, DECK all carry more put premium); (3) the most active Nov 20 contract is the 35 put (2,540) but call contracts trade as much (Oct 16 35 call 2,814, Mar 19 42.5 call 2,802); (4) AlphaQuery P/C volume 0.34. Evidence that is ambiguous: puts dominate the near-the-money strikes (1.25) and the Jan 15 40 put has 30,148 OI. The data cannot separate protection bought by long holders, spreads, and market-maker hedges of customer calls. What would settle it: signed trade data (OPRA trade-by-trade with aggressor side, or a paid flow product such as Cboe LiveVol); I have only end-of-day OI and volume.

## 7. Routes tried and results

| Goal | Route | Result |
|---|---|---|
| NKE chain | Yahoo `v7/finance/options/NKE` without crumb | blocked (401 "Invalid Crumb") |
| | Yahoo with crumb from `fc.yahoo.com` cookie, per expiry date | worked, 18 expiries (OPRA data) |
| | CBOE `cdn.cboe.com/api/global/delayed_quotes/options/NKE.json` | worked (follows a 307; needs `-L`), 1,114 contracts, greeks included |
| | Nasdaq `api.nasdaq.com/api/quote/NKE/option-chain` (the `www.nasdaq.com` path returns 404) | worked, matches CBOE |
| | AlphaQuery volatility pages | worked for 30, 60, 90 day IV, historical vol, P/C; current day only |
| | MarketChameleon IV page | blocked ("Access Denied", cloud-hosted client) |
| | Barchart volatility page | empty response (HTTP 202, 0 bytes) |
| | OptionCharts and IVolatility public pages | opened, but no usable IV history or chain in the HTML returned (JavaScript) |
| Nike skew history | Wayback Machine CDX for the CBOE and Yahoo endpoints | blocked (proxy tunnel closed twice); not retried |
| | AlphaQuery history | current day only (history chart is a paid VolVue download) |
| | Yahoo / CBOE / Nasdaq | current day only |
| | REPO note 17 Oct 13 snapshot | worked, one prior day |
| | Result: **partial**. Only two days. | Needs a data vendor series (LiveVol, OptionMetrics, Bloomberg skew history) or a daily snapshot habit from today. |
| adidas or Puma skew | CBOE `ADDYY.json`, `PUMSY.json` | blocked (403) |
| | Yahoo options for ADDYY, PUMSY | empty (no expirations listed) |
| | Yahoo options for `ADS.DE` | blocked (429) |
| | Nasdaq options for ADDYY | "Symbol not exists" |
| | AlphaQuery ADDYY | no data page |
| | Eurex product page | returned an unrelated PDF |
| | Result: **not obtained** after six routes. | The listed adidas options trade on Eurex (ADS); a Eurex or Bloomberg chain would settle it. US peers (LULU, DECK, ONON, VFC, CROX, SPY) used instead; UAA's chain was too thin to compute; Foot Locker (FL) returned 403 on CBOE and empty on Yahoo (likely delisted after the acquisition). |
| Q2 weekly pair | look for Dec 4, Dec 11, Dec 19 expiries | not listed on any of the three sources; used Nov 27 instead |

## 8. What this means for the pitch, in numbers

- **Price the event, do not claim it is priced.** The statement supported by the data is: the market prices the Nov 13 to Nov 20 window at a 1-sd of 6.7% (event leg 4.2% to 4.9%), no skew, and a P(down 10% or more) of 5.5% to 6.2%. It does not price our D4 distribution (P(down 10% or more) of 19% to 38%).
- **Cost of being wrong is small relative to the claimed payoff.** The 35/30 spread risks $1.31 (3.7% of spot) for a $3.69 payoff if the stock closes below $30 on Nov 20, a 2.8 to 1 ratio; the break-even is $33.69, or 4.6% below the close. D7's DOWN mean (-15.0% by day 3, price $30.0) hits the spread at max gain.
- **The edge is entirely in our probability, not in a mispriced quote.** At the market distribution EV is the half-spread. The positive EVs in section 5 come from D7's 29% (or D4's 50%) DOWN frequency, which D7 itself flags as classified with hindsight. If the right prior is D7's investor-day-only mean of -0.7%, the expected value is about zero minus the spread.
- **Two things that would change the call:** (1) a Nike pre-announcement or confirmed Investor Day agenda that drops "FY28 framing" (silence is 50% in D4) would make the neutral branch more likely, where the put structures lose 7% to 11% of the debit in expectation; (2) a jump in Nov 20 IV above about 42% before Nov 13 would make the put structures dearer; compare at purchase.

## 9. Limits

- Quotes are one end-of-day snapshot. Spreads on 2.5-dollar strikes in the Dec 18 and later expiries are wide (Dec 18 30 put 0.41/0.56).
- The Nov 20 smile is built from about eight usable strikes; a density from eight points is a smoother, not a measurement, especially beyond -22%.
- The simulation uses assumptions I made: 2% (3-day) and 4.5% (20-day) market noise, independence between the Investor Day outcome and the Q2 reaction, zero drift before Nov 13, and the mapping of D4 scenarios to D7 classes. Each is a label, not a measurement.
- Not tested: borrow cost, early assignment of the short call near the Dec 1 ex-dividend date for the Dec 18 version, margin requirements, and tax treatment.
- Dates marked estimated (Q2 about Dec 17, ex-dividend about Dec 1) are not confirmed in the files I opened.
