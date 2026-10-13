# Valuation vs business: how much of the 80% stock drop is multiple compression?

Research date: 2026-10-13. Hypothesis under test: *Much of the 80% stock drop reflects multiple compression from a 2021 bubble valuation and changed expectations rather than business deterioration; separate the stock story from the business story quantitatively.*

Conventions: USD unless noted. "Log share" means each factor's share of ln(price now / price at peak), the only order-independent way to split a product (price = EPS x P/E). "TTM" = trailing four reported quarters known on that date (release date assumed effective the next session). "Ex-IEEPA" removes the one-off $0.52 Q4 FY2026 EPS benefit from the expected IEEPA tariff recovery (Q4 FY26 release p. 1). All Nike filing numbers are reused from `research_notes/04_financial_data_pack.md` and `data/nike_filing_facts.csv` (each row carries filing and printed page). Price data: `data/nke_daily_prices.csv` (Yahoo Finance) plus peer prices pulled from the same Yahoo chart API on 2026-10-13 (market data, not filings).

## 1. Bottom line

1. **The hypothesis is half right, and the half that is right is not about Nike.** About **45%** of the log decline from the $177.51 record close (Nov 5, 2021) to $35.35 (Oct 12, 2026) is a fall in the trailing P/E (47.1x to 22.7x ex-IEEPA). The other **55%** is a fall in trailing EPS ($3.77 to $1.56 ex-IEEPA).
2. **The multiple compression is a sector-wide common factor, not a Nike-specific bubble bursting.** Over the same window, adidas's trailing P/E fell by the same 52% (about 40x to 19.2x) while its EPS was flat (EUR 7.47 FY2021 vs EUR 7.80 TTM to Jun 2026). Deckers' fell 56% (27.2x to 12.0x) while its EPS rose 171%. Nike's multiple compression (ex-IEEPA) is no larger than the healthy peers'. The S&P 500 Consumer Discretionary forward P/E fell from 33.9 to 23.2 (FactSet), and the 10-year real Treasury yield rose from -1.09% to 2.91% (FRED).
3. **What made Nike fall 80% rather than adidas's 50% is the business.** Nike's TTM revenue is unchanged from Nov 2021 ($46.2B vs $45.9B nominal; about -19% in real terms), but TTM EBIT fell from $7.3B (15.8% margin) to $2.9B ex-IEEPA (6.2%). Nike promised FY2025 "high-teens EBIT margin and mid-to-high teens EPS growth" in June 2021; FY2025 delivered an 8.2% EBIT margin and EPS of $2.16.
4. **The 2021 price was not an obvious bubble on Nike's own plan.** $177.51 divided by the EPS implied by Nike's June 2021 FY2025 targets (about $6.0 to $6.9) is 26x to 30x, below Nike's own pre-COVID trailing P/E (median 34.4x, Mar 2019 to Feb 2020). The peak price was a bet that the plan would be delivered. It was not.
5. **Timing splits cleanly into a valuation phase and a business phase.** Nov 2021 to Sep 2022: price -53%, EPS -6%, 91% of the log move is P/E, and Nike fell in line with peers (adidas -60%, Puma -57%, On -59%). Jun 2024 to Oct 2026: price -62.5%, 79% of the log move is EPS (ex-IEEPA), and Nike fell much more than adidas (-33%) or On (-9%) while the S&P 500 rose 42%.
6. **"Changed expectations" is a symptom, not an independent cause.** The expectation resets happened on earnings days: 20 earnings-reaction sessions (about 1.6% of trading days) carry 40% of the total log decline and 43% of the 2024 to 2026 decline, against only 17% of the 2021 to 2022 decline. As late as June 20, 2024, consensus FY2025 EPS was $3.94 and revenue $52.4B; actual was $2.16 and $46.3B.
7. **No sign of a sentiment overshoot at Nike specifically.** Nike still trades at a premium multiple: about 28x guided FY2027 EPS and 22.7x TTM ex-IEEPA, against 19.1x forward for the S&P 500, 19.2x TTM for adidas, 12.0x for Deckers and 7.8x for Lululemon. The market is still paying for a recovery, not pricing permanent impairment.

**Verdict: contributing cause** (about 45% of the log decline, roughly the first -50% of price), but it is a market and sector-wide factor that management cannot fix. The Nike-specific part of the stock collapse (the gap between Nike's -80% and the healthy peers' -50% or better) is business deterioration.

## 2. Falsifiable predictions and results

| # | If the hypothesis is true, then... | What the data show | Held? |
|---|---|---|---|
| P1 | **Timing:** most of the fall should occur while EPS was stable, as P/E deflated (2022 rate shock). | Nov 5, 2021 to Sep 30, 2022: price $177.51 to $83.12 (-53.2%), TTM EPS $3.77 to $3.53 (-6%), P/E 47.1x to 23.5x; 91% of the log move is P/E. But Jun 27, 2024 to Oct 12, 2026: price $94.19 to $35.35 (-62.5%), TTM EPS $3.40 to $1.56 ex-IEEPA; 79% of the log move is EPS (50% if IEEPA is left in). Between them (Sep 2022 to Jun 2024) the stock rose 13% and the P/E re-expanded to 27.7x. | **Partly.** True for the first leg only. |
| P2 | **Peers:** sportswear names with healthy earnings should fall about as much as Nike. | Phase 1 (Nov 2021 to Sep 2022): NKE -53%, adidas -60%, Puma -57%, On -59%, UA -73%, VFC -60%, LULU -40%, DECK -26%: Nike was ordinary. Full period to Oct 12, 2026: NKE -80%, adidas -50%, DECK +19%, On -10%, Anta -43%; the only names that matched Nike (Puma -79%, UA -80%, VFC -79%, LULU -80%) all had business or expectation problems of their own. | **Phase 1 yes; full period no.** |
| P3 | **Peak valuation:** Nike's Nov 2021 multiple should be extreme vs its own history and the market. | TTM P/E 47.1x vs pre-COVID median 34.4x (range 30.1x to 37.7x, Mar 2019 to Feb 2020): a 37% premium to its own norm. Forward P/E about 47x (Zacks, snippet) vs S&P 500 21.4x and Consumer Discretionary 33.9x (FactSet, Nov 5, 2021). | **Partly.** Elevated, but Nike always traded at 30x+. Only ln(34.4/47.1) = 19% of the log decline is a return to its own pre-COVID multiple. |
| P4 | **Implausible expectations:** the peak price should require assumptions beyond management's own plan. | Nike's June 2021 FY2025 targets: high-single to low-double-digit revenue growth, "high-teens EBIT margin and mid-to-high teens EPS growth" (SGB, Jun 28, 2021; Motley Fool, Jun 25, 2021). From FY2021 EPS $3.56, 14% to 18% a year gives FY2025 EPS of about $6.0 to $6.9 (my arithmetic). $177.51 / $6.0 to $6.9 = 26x to 30x, below Nike's pre-COVID multiple. The stock rose 15.5% on the day the targets were given (Jun 25, 2021, $133.60 to $154.35). | **No.** The peak priced the plan at a normal multiple. The plan failed: FY2025 revenue $46.3B vs about $60.6B to $67.6B implied; EBIT margin 8.2% vs "high teens". |
| P5 | **Nike-specific multiple compression:** Nike's P/E should compress more than peers' (that would be the bubble-specific part). | Trailing P/E, Nov 2021 to Oct 2026: Nike 47.1x to 22.7x ex-IEEPA (-52%; -64% with IEEPA left in); adidas about 40.0x to 19.2x (-52%); Deckers 27.2x to 12.0x (-56%); Lululemon about 62.5x to 7.8x (-88%). On a forward basis Nike went from about 47x (Zacks, snippet) to 28x (-41%). | **No.** Nike's compression equals the healthy peers'. It is a common factor. |
| P6 | **Business intact:** if the stock story is separate from the business story, fundamentals should be roughly intact. | TTM revenue $46,192M (to Aug 2021) vs $45,891M (to Aug 2026): -0.7% nominal, about -19% real (CPI +22.0%, Sep 2021 to Aug 2026, FRED). TTM EBIT $7,306M (15.8%) to $2,867M ex-IEEPA (6.2%), -61%. TTM net margin 13.2% to 5.1% ex-IEEPA. FY2025 EPS missed the June 20, 2024 consensus by 45% ($2.16 vs $3.94). | **No.** |
| P7 | **Event study:** if valuation and sentiment drove the fall, earnings days should not carry a disproportionate share. | 20 earnings-reaction sessions out of about 1,240 carry -0.639 of the -1.614 total log move (40%); 32% of Nike's excess return vs the S&P 500. Phase 1: earnings days only 17% of the move. Phase 3: 43% (Jun 28, 2024 -20.0% on the FY25 guide cut; Apr 1, 2026 -15.5%; Dec 19, 2025 -10.5%; Oct 2, 2024 -6.8%). | **No for 2024 to 2026; yes for 2021 to 2022.** |
| P8 | **Overshoot:** if the fall is mostly sentiment, Nike should now look cheap against peers and the market. | Nike: 28x guided FY27 EPS midpoint ($1.25), 22.7x TTM ex-IEEPA, 17.0x GAAP TTM. S&P 500: 19.1x forward; Consumer Discretionary 23.2x (FactSet, Oct 9, 2026). adidas 19.2x, Deckers 12.0x, Lululemon 7.8x TTM. If Nike traded at the S&P forward multiple on guided FY27 EPS: about $24. | **No.** Nike still carries a premium multiple that assumes recovery. |

Score: 0 predictions fully held, 3 partly held (P1, P2, P3, each only for the 2021 to 2022 leg), 5 failed. The pattern is exactly what a two-factor story predicts: a sector-wide de-rating first, then a Nike-specific earnings collapse.

## 3. The quantitative separation

### 3.1 Price = TTM EPS x TTM P/E (Nike)

Computed from `data/nke_daily_prices.csv` and quarterly diluted EPS in `data/nike_filing_facts.csv` (Q1 FY2019 to Q1 FY2027). Release dates from the 8-K filing dates in the same CSV.

| Date | Close | TTM EPS (through) | TTM P/E |
|---|---|---|---|
| 2019-06-28 | 83.95 | 2.49 (Q4 FY19) | 33.7 |
| 2019-12-31 | 101.31 | 2.86 (Q2 FY20) | 35.4 |
| 2021-06-25 | 154.35 | 3.56 (Q4 FY21) | 43.4 |
| **2021-11-05 (peak)** | **177.51** | **3.77 (Q1 FY22)** | **47.1** |
| 2022-09-30 (2022 low) | 83.12 | 3.53 (Q1 FY23) | 23.5 |
| 2023-06-30 | 110.37 | 3.23 (Q4 FY23) | 34.2 |
| 2024-06-27 | 94.19 | 3.40 (Q3 FY24) | 27.7 |
| 2024-06-28 | 75.37 | 3.73 (Q4 FY24) | 20.2 |
| 2025-04-08 | 53.27 | 3.01 (Q3 FY25) | 17.7 |
| 2025-12-31 | 63.71 | 1.70 (Q2 FY26) | 37.5 |
| 2026-06-30 | 41.05 | 1.51 (Q3 FY26) | 27.2 |
| **2026-10-12** | **35.35** | **2.08 GAAP / 1.56 ex-IEEPA (Q1 FY27)** | **17.0 / 22.7** |

Pre-COVID (Mar 22, 2019 to Feb 20, 2020) TTM P/E: mean 34.2x, median 34.4x, range 30.1x to 37.7x.

**Log decomposition, Nov 5, 2021 to Oct 12, 2026** (total ln = -1.614, price -80.1%):

| Basis | EPS share | P/E share |
|---|---|---|
| TTM, ex-IEEPA (preferred) | **55%** | **45%** |
| TTM, GAAP (IEEPA left in) | 37% | 63% |
| Forward: $3.56 FY22 consensus (Zacks, snippet) to $1.25 FY27 guide midpoint | 65% | 35% |
| "Normalized" sensitivity: EPS at a 10.3% FY2019 net margin on today's revenue ($3.10) | 12% | 88% |

The last row is the strongest version of the hypothesis: if one insists Nike's earning power is still about $3, the market has re-rated it to about 11x "normal" earnings, and nearly all of the fall is "changed expectations". But that re-rating happened on earnings days and in response to guidance (P7), and it is far larger than the healthy peers' (P5), so it is the market pricing a damaged business, not a valuation bubble.

The P/E share can be split further (preferred basis, ex-IEEPA):
- Return of Nike's own multiple to its pre-COVID median (47.1x to 34.4x): **19%** of the log decline.
- Fall from the pre-COVID median to today (34.4x to 22.7x): **26%**.
- Peer benchmark: adidas and Deckers both lost 52% to 56% of their trailing P/E with flat or rising EPS, which accounts for essentially all of Nike's 45% P/E share. The Nike-specific residual multiple compression is about zero on this basis.

**Dollar counterfactuals** (order matters in dollar terms, so both are shown):
- Business frozen at Nov 2021 EPS ($3.77), P/E falls to today's 22.7x: $85.6 (-52%). Valuation alone explains $91.9 of the $142.2 per-share fall (65%).
- P/E frozen at 47.1x, EPS falls to $1.56: $73.5 (-59%). Business alone explains $104.0 (73%).
- If Nike had hit its June 2021 FY2025 plan (EPS about $6.0 to $6.9) and traded at today's adidas multiple (19.2x): about $115 to $132. At its own 22.7x: about $136 to $157.

### 3.2 Market cap = revenue x net margin x P/E

Market cap: about $287.5B on Nov 5, 2021 (1,619.6M Q1 FY22 weighted diluted shares x $177.51; approximation, not the cover count) to $52.5B on Oct 12, 2026 (1,485,308,829 shares, Q1 FY27 10-Q cover). About **$235B** of value lost. ln = -1.70.

| Factor | Nov 2021 (TTM to Aug 31, 2021) | Oct 2026 (TTM to Aug 31, 2026) | Log share of market-cap fall |
|---|---|---|---|
| Revenue | $46,192M | $45,891M | **0%** |
| Net margin (to FY2019's 10.3%) | 13.2% | (10.3%) | **14%** (unwinding the COVID-peak margin) |
| Net margin (below FY2019) | (10.3%) | 5.1% ex-IEEPA | **42%** (genuine deterioration) |
| P/E (market cap / TTM net income) | 47.3x | 22.6x ex-IEEPA | **43%** |
| Share count | 1,619.6M | 1,485.3M | offsets about +5% (buybacks) |

Quarterly inputs: revenue, net income and EBIT by quarter from `data/nike_filing_facts.csv` (Q2 FY21 to Q1 FY22 and Q2 FY26 to Q1 FY27). IEEPA adjustment: $986M pre-tax from EBIT and $0.52 x 1,482.9M diluted shares (about $771M) from net income (Q4 FY26 release p. 1).

### 3.3 The cross-section of sportswear stocks (natural experiment)

Prices: Yahoo chart API, closes on Nov 5, 2021 and Oct 12, 2026 (pulled 2026-10-13). EPS: company filings as noted.

| Company | Price change | TTM EPS then | TTM EPS now | EPS change | TTM P/E then -> now | P/E change |
|---|---|---|---|---|---|---|
| **Nike** | **-80.1%** | $3.77 | $1.56 ex-IEEPA ($2.08 GAAP) | **-59%** | 47.1x -> 22.7x | **-52%** |
| adidas (XETRA) | -49.9% | EUR 7.47 (FY2021, cont. ops) | EUR 7.80 (FY2025 7.46 - H1 2025 4.47 + H1 2026 4.81) | +4% | about 40.0x -> 19.2x | -52% |
| Deckers | +19.4% | $2.59 split-adjusted (TTM to Sep 2021, $15.54 pre 6:1 split) | $7.03 (TTM to Jun 2026) | +171% | 27.2x -> 12.0x | -56% |
| Lululemon | -79.8% | $7.49 (FY2021, to Jan 2022; hindsight) | $12.17 (TTM to Aug 2, 2026) | +62% | about 62.5x -> 7.8x | -88% |
| Puma | -79.4% | n/a | 2025 operating loss EUR 357.2m (repo note) | collapse | n/a | n/a |
| Under Armour | -80.3% | n/a | FY2026 EPS -$1.16 (SEC XBRL) | collapse | n/a | n/a |
| VF Corp | -78.7% | n/a | FY2026 EPS $0.64 vs FY2022 $3.53 (SEC XBRL) | -82% | n/a | n/a |
| On Holding | -9.8% | | | | | |
| Anta (HK) | -43.2% | | | | | |
| S&P 500 | +66.2% | | | | fwd 21.4x -> 19.1x | -11% |
| XLY (Cons. Disc. ETF) | +6.3% | | | | sector fwd 33.9x -> 23.2x | -32% |

Reading: every sportswear name lost roughly half or more of its multiple. The names that then also lost earnings (Nike, Puma, UA, VF) ended near -80%. The names whose earnings held or grew ended between -50% and +19%. Lululemon is the exception that shows "expectations" can crush a stock without realized deterioration (EPS up 62%, price -80%); Nike is not that case, because Nike's realized EPS fell 59%.

### 3.4 Phase table (price change)

| | Nov 5, 2021 to Sep 30, 2022 | Sep 30, 2022 to Jun 27, 2024 | Jun 27, 2024 to Oct 12, 2026 |
|---|---|---|---|
| NKE | -53.2% | +13.3% | -62.5% |
| adidas | -60.2% | +87.2% | -32.8% |
| Deckers | -26.2% | +219.9% | -49.4% |
| On | -59.0% | +143.2% | -9.4% |
| Lululemon | -40.3% | +10.3% | -69.3% |
| Puma | -57.3% | -8.3% | -47.3% |
| S&P 500 | -23.7% | +52.9% | +42.4% |
| US 10y yield (FRED DGS10) | 1.45% (Nov 5, 2021) to 3.83% (Sep 30, 2022) | 4.29% (Jun 27, 2024) | 5.24% (Oct 9, 2026) |

Phase 1 is the valuation story (Nike in line with peers). Phase 2 is the first business divergence: winners re-rated on growth while Nike stalled (FY2024 revenue +0.3%). Phase 3 is the business story.

## 4. Evidence for and against

### Strongest evidence FOR the hypothesis
- 45% of the log decline (ex-IEEPA) is P/E, 63% with the IEEPA benefit left in; up to 88% on a "normalized earnings" lens.
- Nov 2021 to Sep 2022: -53% with EPS down only 6%; 91% of that leg is P/E; earnings days explain only 17% of it.
- Nike's peak TTM P/E (47.1x) was 37% above its own pre-COVID median and 2.2x the S&P 500 forward multiple; the Consumer Discretionary sector forward P/E itself was 33.9x (FactSet, Nov 5, 2021).
- Real 10-year yields rose about 4 percentage points (-1.09% to 2.91%, FRED DFII10), a large headwind for long-duration consumer brands.
- adidas (EPS flat) and Deckers (EPS +171%) both lost 52% to 56% of their multiples, showing a large common de-rating that had nothing to do with Nike's operations.
- About 14% of the market-cap fall is the unwinding of a COVID-peak net margin (13.2% vs 10.3% in FY2019), a 2021 "earnings bubble" rather than a structural loss.

### Strongest evidence AGAINST (Nike-specific decline is business)
- Nike's multiple compression is no larger than healthy peers' (P5); the extra 30 points of decline vs adidas (-80% vs -50%) map onto Nike's 59% EPS fall.
- TTM revenue flat in nominal terms for five years (about -19% real) and TTM EBIT -61% ex-IEEPA; FY2025 EPS of $2.16 vs a June 2024 consensus of $3.94 and a June 2021 plan implying about $6.0 to $6.9.
- The peak price was consistent with Nike's own plan at a below-normal multiple (26x to 30x FY2025 target EPS), so the "bubble" was mostly a bet on execution.
- 2024 to 2026: 79% of the log move is EPS; 43% of it happened on earnings days; the single largest day (-20.0%, Jun 28, 2024) was a guidance cut.
- Nike still trades at a premium multiple (28x forward, 22.7x TTM ex-IEEPA) to the S&P 500 and to every sportswear peer measured; there is no sentiment overshoot to "revert".

## 5. Independent cause or symptom?

Two separate things are bundled in the hypothesis:
1. **Sector and rate de-rating (about 45% of the log decline).** Independent of Nike's business. Caused by the end of zero real rates and the unwinding of the 2020 to 2021 athleisure and sneaker premium across the whole consumer discretionary group. Not a symptom of Nike's problems and not fixable by Nike.
2. **"Changed expectations" specific to Nike.** A symptom. The Nike-specific re-rating happened when Nike reported or guided (Jun 2024, Dec 2025, Apr 2026) and is the market capitalizing the business deterioration documented in the other root-cause notes (classics oversupply, DTC pivot and wholesale loss, China, innovation, Converse). Upstream causes: see `dtc_wholesale.md`, `franchise_oversupply.md`, `china.md`, `innovation_drought.md`.

## 6. Contribution and fixability

- **Share of the 80% stock decline:** about **45% of the log decline** (roughly the first -50% of price, or $65 to $92 of the $142 per-share fall depending on ordering) is multiple compression, and that piece is matched almost one-for-one by healthy sportswear peers. The Nike-specific share of multiple compression is about **0 to 10%** of the log decline. The remaining **about 55%** is EPS, of which about 14 points of market cap reflect the unwinding of COVID-peak margins and about 42 points reflect deterioration below pre-COVID margins.
- **Share of the business (revenue) decline:** **0%.** A stock multiple cannot cause revenue to fall from $51.4B to $46.4B. This hypothesis explains none of the operating decline.
- **Fixable by management: partly.** The sector and rate de-rating is outside management's control and is unlikely to reverse to 2021 levels. The Nike-specific part (EPS) is fixable through the business: at today's 22.7x ex-IEEPA multiple, a return to FY2024 EPS ($3.73) would imply about $85; at adidas's 19.2x, about $72. The guided FY2027 adjusted EPS of $1.15 to $1.35 is the hurdle.

## 7. Sources

| # | Source | Date | Status | Used for |
|---|---|---|---|---|
| 1 | Nike 10-Ks, 10-Qs and earnings 8-Ks, FY2019 to Q1 FY2027 (as compiled in `04_financial_data_pack.md` and `data/nike_filing_facts.csv`, each with URL and printed page) | 2019-07-23 to 2026-10-02 | OPENED (repo, previously verified) | Quarterly EPS, revenue, EBIT, net income, shares, IEEPA $0.52 and $986M, FY27 guide |
| 2 | `data/nke_daily_prices.csv` (Yahoo Finance chart API) | pulled 2026-10-12 | OPENED (repo) | NKE closes |
| 3 | Yahoo Finance chart API, query1.finance.yahoo.com/v8/finance/chart for ADS.DE, ADDYY, DECK, LULU, PUM.DE, UAA, VFC, ONON, 2020.HK, ^GSPC, XLY, RSP | pulled 2026-10-13 | OPENED (raw JSON) | Peer and index prices |
| 4 | FactSet Earnings Insight, [Nov 5, 2021](https://advantage.factset.com/hubfs/Website/Resources%20Section/Research%20Desk/Earnings%20Insight/EarningsInsight_110521.pdf) | 2021-11-05 | OPENED (PDF) | S&P 500 forward P/E 21.4; Consumer Discretionary 33.9 |
| 5 | FactSet Earnings Insight, [Oct 9, 2026](https://advantage.factset.com/hubfs/Website/Resources%20Section/Research%20Desk/Earnings%20Insight/EarningsInsight_100926.pdf) | 2026-10-09 | OPENED (PDF) | S&P 500 forward P/E 19.1 (10-year avg 19.1); Consumer Discretionary 23.2 |
| 6 | FRED [DGS10](https://fred.stlouisfed.org/series/DGS10) and [DFII10](https://fred.stlouisfed.org/series/DFII10) | data to 2026-10-09 | OPENED (CSV) | 10y nominal 1.45% -> 5.24%; real -1.09% -> 2.91% |
| 7 | FRED [CPIAUCSL](https://fred.stlouisfed.org/series/CPIAUCSL) | Sep 2021 273.910; Aug 2026 334.131 | OPENED (CSV) | Real revenue deflator (+22.0%) |
| 8 | SGB Online, ["Analyst price hikes follow Nike's blow-out Q4"](https://sgbonline.com/analyst-price-hikes-follow-nikes-blow-out-q4/) | 2021-06-28 | OPENED | FY2025 targets: "high single-digit to low double-digit growth", "high-teens EBIT margin and mid-to-high teens EPS growth"; analyst PTs $171 to $214 |
| 9 | Motley Fool, ["Why Nike stock surged today"](https://www.fool.com/investing/2021/06/25/why-nike-stock-surged-today) | 2021-06-25 | OPENED | EBIT margin "to the high teens, up from 15%"; digital 50% by 2025 |
| 10 | SGB Online, ["EXEC: Nike Hit By Analyst Estimate Cuts Ahead of Earnings Report"](https://sgbonline.com/?p=315304) | 2024-06-20 | OPENED | FY25 consensus sales $52.4B, EPS $3.94; FY24 $3.75 |
| 11 | Zacks notes syndicated (finanzen.net redirect to [zacks.com 2919332](https://www.zacks.com/stock/news/2919332/nike-nke-stock-declines-while-market-improves-some-information-for-investors)) | late 2021 (exact date not seen) | SNIPPET (Zacks page bot-blocked) | Nike forward P/E about 47.4x to 47.8x on FY22 consensus EPS $3.56 |
| 12 | Evercore note via search summary ([investing.com](https://investing.com/news/company-news/nike-price-target-cut-amid-lowered-fy25-guidance-still-outperform-93CH-3501016)) | Jun 2024 | SNIPPET | Alternative FY25 consensus $3.86 |
| 13 | adidas [FY2022 results release](https://res.cloudinary.com/confirmed-web/raw/upload/v1706003622/adidas-group/investors/financial-publications/2022/20230308_adidas_ag_fy2022_results_en_xdfsuy.pdf) | 2023-03-08 | OPENED (PDF) | 2021 basic and diluted EPS cont. ops EUR 7.47; net income cont. ops EUR 1,492m |
| 14 | adidas [FY2025 results release](https://res.cloudinary.com/confirmed-web/image/upload/v1772605768/adidas-group/investors/financial-publications/2025/Q4/adidasAG_FY_2025_Results_EN_Final_tb9z6m.pdf) | 2026-03 | OPENED (PDF) | 2025 EPS cont. ops EUR 7.46; net income EUR 1,377m |
| 15 | adidas [Q2 2026 results release](https://res.cloudinary.com/confirmed-web/image/upload/v1785388904/adidas-group/investors/financial-publications/2026/Q2/EN/adidasAG_Q2_2026_Results_EN_Final_z7f9t2.pdf) | 2026-07-30 | OPENED (PDF) | H1 2026 EPS EUR 4.81 vs H1 2025 EUR 4.47 |
| 16 | SEC XBRL companyfacts API (data.sec.gov) for Lululemon (CIK 1397187), Deckers (910521), VF (103379), Under Armour (1336917) | pulled 2026-10-13 | OPENED (JSON) | Quarterly and annual diluted EPS |
| 17 | `research_notes/Nike decline execution vs structural/analysts_and_consumer_data.md` | 2026-10 | OPENED (repo) | Post-Q1 FY27 PT cuts; BofA FY27/28 EPS cuts; Citi "cost-cutting story" |
| 18 | `research_notes/Gulden and Plank turnarounds vs Nike/adidas_gulden.md` | 2026-10 | OPENED (repo) | adidas operating profit history; "strong business, weak share" (Boersen-Zeitung) |
| 19 | `research_notes/Nike decline execution vs structural/competitors_and_turnarounds.md` | 2026-10 | OPENED (repo) | Puma 2025 operating loss EUR 357.2m |

## 8. Caveats

- Nov 2021 share count is the Q1 FY22 weighted diluted figure, not a cover count; it moves the market-cap estimate by about 1%.
- adidas and Lululemon "then" EPS use fiscal 2021 actuals (reported after Nov 2021), so their peak P/Es are approximate. Using TTM to Q3 2021 would change adidas's peak P/E by a few turns, not the conclusion.
- Lululemon's 7.8x TTM is unusually low; it reflects market expectations of a fall in LULU earnings that is not yet in reported numbers. I did not research its cause.
- Forward-P/E comparisons mix a Zacks consensus (snippet) at the peak with Nike's own guidance today; the TTM basis is the cleaner one and is used for the headline.
- Nike had no pre-2019 price data in the repo, so the "own history" multiple uses only Mar 2019 to Feb 2020.
- Prices are not dividend-adjusted in the main decomposition. Total return (Yahoo adjusted close) is -78.2% vs -80.1% price.
