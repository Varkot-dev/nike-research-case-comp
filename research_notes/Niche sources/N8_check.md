# N8 check: can the Base Rate Book margin claims survive a hostile judge?

Prepared 2026-10-15 by the skeptic pass on `N8_literature_base_rates.md`. Tags: **OPENED** = I read the file or page named; **SNIPPET** = search-result text only; **DERIVED** = my arithmetic on tagged inputs. Scripts and panel are in `N8_check_scripts/` and `N8_check_panel.csv` (run with `PYTHONPATH=. python3`; `fetch.py` needs only `data.sec.gov`, no contact header, no email). No dashes of the long kind are used; negative numbers carry a minus sign.

## 0. Verdict in one table

| # | N8 claim | Verdict | Why in one line |
|---|---|---|---|
| 1a | r = 0.73, consumer discretionary, 5 years, printed p. 62 | **SURVIVES** (statistic and page correct) | Exhibit 4 and Exhibit 5, p. 62, level correlation of operating profit margin (EBIT/sales, HOLT), SD of the yearly r = 0.08. Confirmed in two independent hosted copies |
| 1b | Expected FY31 margin 9.4% | **NEEDS CAVEAT** | 9.4% needs r = 0.73 AND Nike's own 12.4% mean. The book's prescribed mean is the sector (11%), giving 9.0%. On an independent 2009 to 2025 SEC panel the expected value is 8.2% to 9.0%, with no support for weighting Nike's own mean. Starting point is not a clean 8.3% (see 1d) |
| 1c | P(11.6%+) 15% to 25% | **SURVIVES** | Empirical share of comparable windows with a gain of 3.3 points or more is 16% to 24% (n = 26 to 51) |
| 1c | P(14%+) 2% to 10% | **WRONG at the low end** | Empirical 10% to 18%; normal model with a 4.3 to 5.0 point spread gives 14% to 18%. Say 5% to 15%, not 2% to 10% |
| 1d | FY26 margin of 8.3% is the starting point | **NEEDS CAVEAT** | 6.2% ex the $986M IEEPA refund, but that refund offsets about $1.07B to $1.14B of IEEPA tariff cost also in FY26; tariff-neutral and ex-severance the margin is about 9.3% to 9.5%. Both 6.2% and 9.4% are defensible depending on whether the tariff cost recurs. FY27 consensus is 5.7%, below both |
| 2 | 54 cents vs 7.4 cents | **54 survives only as a tariff-neutral coincidence; 7.4 is the WRONG comparator** | Nike is 47 to 54 cents tariff-neutral, 74 cents ex refund only. Peer median in 152 revenue-decline windows is 31 to 40 cents. The book's 0.074 is a pooled regression slope, not a decremental margin |
| 3 | $24 to $28 at 9.4% | **SURVIVES arithmetically** ($24.18 at 10% WACC, $27.75 at 9%) | Conditional on WACC. At 8% WACC the same margin is worth $32.53 (-8% vs $35.30). Terminal margin held flat at 9.4% forever is internally inconsistent with the same regression |
| 4 | 3 of 13 apparel episodes gained 3.3 points | **NOT REPRODUCIBLE as stated; direction survives** | The note's counts are typed into the script, not computed. My replication of its stated rule gives 4 of 12, and all four gainers start from a negative or one-off margin (COVID, impairments). From a positive persistent margin: 0 of 8 |

## 1. The r = 0.73 statistic

**What it is (OPENED).** Credit Suisse, "The Base Rate Book" (Mauboussin, Callahan, Majd), September 26, 2016, HOLT data, top 1,000 global companies by market value 1950 to 2015, financials and utilities excluded, winsorized at the 2nd and 98th percentiles (printed p. 59, p. 62 notes).
- p. 59, Exhibit 1: scatter of operating margin now vs next year, in 3 years, in 5 years, r = 0.91, 0.79, 0.72 (all sectors). Operating profit margin is "the ratio of operating income to sales" (p. 59), so it is an **EBIT-type margin, not EBITDA**. HOLT reports after stock compensation expense from about 2005 (p. 59). Nike's EBIT (pretax plus net interest) differs from GP minus SG&A by "other (income) expense" only: FY26 8.30% vs 8.18% (DERIVED from `nike_filing_facts.csv`).
- p. 61 to 62: Exhibit 4 title "Correlation Coefficients for Operating Margin for Eight Sectors" lists Consumer Discretionary 0.73 with standard deviation 0.08 (the spread of the yearly r, so 0.65 to 0.81 at one SD). Exhibit 5, p. 62: same r, median margin 10%, average 11%, "Toward What Mean?". The text before Exhibit 4 says "five-year changes", but Exhibit 3 shows it is margin level at t vs level at t+5, so it is a level correlation. N8 used it correctly as a level statistic.
- Second copy: josephnoko.com PDF (OPENED, text search) shows the same 0.73 / 0.08 / 0.10 / 0.11 row. First copy: mjbaldbard.wordpress.com. Two independent third-party hosts agree. The 0.77 for consumer discretionary in the same book is gross profitability (Exhibit 7), not margin, so the number cannot be mixed up.
- Routes to the official file (logged, all different): Credit Suisse portal (not reachable), Morgan Stanley PDF (403, per N8), Wayback (blocked, per N8), web search for other hosts (worked, found josephnoko.com), the mjbaldbard compilation (worked). Five routes; one official-copy gap remains and is immaterial because two hosts agree on the row.

**Three misuses that matter.**
1. **r is a pooled cross-sectional correlation, so it mixes persistence of firm-specific levels with persistence of deviations.** The authors say the expected value regresses toward the sector mean (11% for consumer discretionary) and add that "regression toward the mean works on a population, not necessarily on every individual company" (p. 62). Combining a pooled r with Nike's own 12.4% mean is N8's extension, not the book's rule. With the book's own mean the expected FY31 margin is 9.0% (DERIVED), with the sector median 8.8%.
2. **r is unstable across samples and the answer is very sensitive to it.** On an independent 2009 to 2025 SEC panel (73 companies, GAAP operating income / revenue from companyfacts on data.sec.gov, DERIVED), the 5-year winsorized correlation is 0.48 (57 consumer discretionary names), 0.36 (20 apparel, footwear, luxury names), 0.32 (16 "brand leader" names) against the book's 0.73. Plugging r = 0.36 into N8's own formula with Nike's own mean gives 10.9%; with r = 0.5, 10.3%. So the 9.4% is not a robust output of "the base rate"; a bull can move it 1.5 points by swapping the correlation. The panel is GAAP, so impairments and COVID inflate noise (flagged), which lowers r mechanically.
3. **Regression with an own-mean term does not support N8's weighting.** Regressing the margin 5 years ahead on today's margin and the firm's own average (winsorized, `reg.py`): brand set coefficient on own mean -0.01, leaders 0.06, consumer discretionary core 0.35; predicted Nike FY31 margin 8.2% (brand), 8.8% (leaders), 9.0% (core) at m0 = 8.3, and 7.7% to 8.2% at m0 = 6.2. These bracket 9.4% from below.

**Definition and sector checks.** EBIT vs EBITDA: it is EBIT, fine. Level vs change: level, fine. Sector: HOLT consumer discretionary includes retailers, autos, hotels, media, durables, so it is a loose reference class for a branded footwear maker; the book's own consumer staples r is 0.89, so the choice of sector alone moves the answer (staples r with own mean: 12.38 + 0.89 x (8.3 - 12.38) = 8.75%).

**Starting margin (FY26).** All DERIVED from `data/nike_filing_facts.csv` (FY2026 10-K p. 30, p. 31, p. 55, p. 89).
| Basis | FY26 EBIT $M | Margin |
|---|---|---|
| Reported | 3,850 | 8.30% |
| Ex $986M IEEPA recovery (refund only) | 2,864 | 6.17% |
| Ex refund and ex $385M Pace severance | 3,249 | 7.0% |
| Tariff-neutral: ex refund and ex the $1.07B to $1.14B FY26 IEEPA cost (tariffs.md 'Method A', Q4 call: 210 bps refund, GM 40.8% ex benefit) | 3,934 to 4,004 | 8.5% to 8.6% |
| Tariff-neutral and ex severance | 4,319 to 4,389 | 9.3% to 9.5% |
| FY27 consensus (D5, repo) | 5.7% | 5.7% |

The refund is booked in cost of sales as "largely offsetting" IEEPA tariffs recognized in fiscal 2026 (10-K p. 30), so 6.2% keeps the cost and drops the offset, which is the pessimistic bound if IEEPA-equivalent costs recur. Persistence forecasts at each start (r = 0.73, own mean 12.38): 6.2% gives 7.9%; 7.0% gives 8.5%; 8.3% gives 9.4%; 9.4% gives 10.2%; FY27 consensus 5.7% (4 years, r about 0.76) gives 7.3%. The honest statement is a range of 7.3% to 10%, centred near 8.5% to 9%.

**How wide is the real distribution?** N8's lowest SD (2.2, Nike's own year-to-year) is too narrow because it ignores regime change. On the independent panel, firms with m0 between 5.5% and 11.5% and at least 2 points below their own 10-year mean (`cond.py`, DERIVED): consumer discretionary core n = 51 (22 firms), median 5-year change -0.2, 10th to 90th percentile -9.0 to +4.8, robust SD 4.3, P(change of +3.3 or more) 16%, P(+5.7 or more) 10%, P(negative) 55%. Brand set n = 26: P(+3.3) 19%, P(+5.7) 12%. Leaders n = 17: 24% and 18%. Windows are overlapping, contain COVID, and carry GAAP one-offs: treat the percentages as rough (about plus or minus 10 points). Excluding windows that span 2020 leaves n of 3 to 9, so COVID cannot be removed with this data.

**Normal-model probabilities with a corrected SD of 4.3 to 5.0:** mean 9.4: P(11.6%+) = 30% to 33%, P(14%+) = 14% to 18%; mean 8.3: 22% and 9%. N8's 15% to 25% for 11.6% sits at the low end of that; the empirical analogs support it. N8's 2% to 10% for 14% does not survive.

**Recovery from a trough, named cases (own 5-year windows; GAAP unless stated).**
| Case | Trough or entry | Five years later | Change | Source |
|---|---|---|---|---|
| Nike FY2009 | 10.2% (peak 13.4) | FY10 13.3 (1 year), FY14 12.9 | +3.1 in 1 year, +2.7 in 5 | `D5_valuation_annual_xbrl.csv` / nike_m in N8_derived.py, DERIVED. One-year cyclical dip, not a multi-year one |
| adidas 2014 to 2019 | 6.1% reported 2014 (6.6% ex impairment), 6.5% 2015 | 11.3% in 2019 | +4.7 to +5.2 | adidas Annual Report 2015 printed p. 117 (operating profit EUR 883M reported and EUR 961M ex impairment in 2014 on sales of EUR 14.5B; EUR 1,059M and 1,094M in 2015; margin 6.5% vs 6.6% ex impairment) OPENED via ddd.uab.cat; AR2025 ten-year overview (11.3% 2019, 8.6% 2016, 9.8% 2017, 10.8% 2018) OPENED. **Recovery beyond the prior peak: the best bull analog.** 2015 to 2020 would be 6.5 to 4.0 (COVID) |
| adidas 2023 to 2025 | 1.3% (2023) | 8.3% (2025) | +7.0 in 2 years | AR2025 ten-year overview OPENED. A second bull case; Yeezy inventory and tariffs distort |
| Lululemon | 20.9% FY2014 (peak 28.7); trough 17.2% FY2017 | 22.3% FY2019 / 16.4% FY2022 (Mirror impairment year) | +1.4 / -0.8 | panel DERIVED |
| Ralph Lauren | 8.1% FY2018, 8.9% FY2019 (peak 16.2) | 10.9% FY2023, 11.4% FY2024 (14.5% FY2026) | +2.8, +2.5 in 5 years; 35% of gap | panel DERIVED. Real but partial recovery; full recovery took 8 years |
| Estee Lauder | 6.2% FY2024 (peak 17.9) | open (FY2026 5.2%) | not yet | panel DERIVED |
| Starbucks | 15.4% FY2019 (peak 19.6) | 15.0% FY2024; GFC dip 4.9 to 13.3 in 2 years | -0.4 | panel DERIVED |
| Coach / Tapestry | 23.3% FY2014, 14.7% FY2015 (peak 31.7) | 13.6% FY2019 | no recovery | panel DERIVED |
| Under Armour | 8.6% FY2016 (peak 12.7) | 8.4% FY2021 | -0.2 | panel DERIVED |

**Does a brand-leader subset recover faster?** No, on this data. Episodes (margin at least 3 points under its prior 5-year high for 2 straight years, margin above zero): leaders n = 11 (+8 still open), median change -0.4, 1 of 11 gained 3.3 or more, 0 of 11 gained 5.7. Brand set n = 18: median +0.1, 3 of 18, 1 of 18. All consumer names n = 49: median +0.1, 12 of 49 (24%), but gainers there include restaurant refranchising and tobacco spin-offs (YUM 2014, PM 2015, MAR 2020 COVID) that are not Nike analogs. Limits: current SEC filers only (survivorship biases recoveries upward, which makes the skeptic case stronger), small n, GAAP one-offs, XBRL starts about FY2009, so Nike 2008 to 2012 and adidas come from other sources.

## 2. "54 cents vs 7.4 cents"

**Recompute (DERIVED, `nike_filing_facts.csv`).** Revenue FY24 51,362, FY26 46,398 (-4,964). EBIT 6,539 and 3,850 (-2,689). 2,689 / 4,964 = **0.542**. FY23 to FY26: 2,345 / 4,819 = 0.487. Arithmetic is right. Distortions:
| Adjustment | EBIT lost | Sales lost | Cents per $ |
|---|---|---|---|
| Reported | 2,689 | 4,964 | 54 |
| Strip $986M IEEPA refund only | 3,675 | 4,964 | 74 |
| Tariff-neutral (also strip $1.07B to $1.14B FY26 IEEPA cost) | 2,535 to 2,605 | 4,964 | 51 to 52 |
| Tariff-neutral, also strip FY24 $443M restructuring and FY26 $385M severance | 2,593 to 2,663 | 4,964 | 52 to 54 |
| Constant-currency revenue (translation: FY25 -419, FY26 +1,023, so +604 net since FY24; no EBIT FX split filed after FY24) | 2,689 | 5,568 | 48 |
| Strip net rise in sales-related reserves FY24 to FY26 (1,282 to 1,589, +307, contra-revenue; treated as 100% margin, an upper bound) | 2,382 | 4,657 | 51 |
The FY25 reserve build (1,282 to 1,834, +552) is a revenue deduction, so it overstates the sales lost in FY25 but reverses by FY26 (-245). Conclusion: **the 54 survives as 47 to 54 cents on tariff-neutral bases; it jumps to 74 cents only if the refund is removed while the tariff cost stays.** Do not quote 54 without saying the refund and tariff cost net to about zero.

**Is the sector comparator the same measure? No.** Book p. 50, Exhibit 11, and p. 51, Exhibit 12: consumer discretionary three-year operating margin beta 0.074 is the slope of a least-squares line of the 3-year change in operating income on the 3-year change in sales, in 2015 dollars, winsorized, for all sales changes (mostly increases) for the top 1,000 companies 1950 to 2015. Problems: (a) a pooled regression slope with sales changes noisy from acquisitions and FX is attenuated, and 0.074 is below the sector's own 11% average margin, which no decremental margin can be; (b) it is not conditioned on declines; (c) it is a slope with an intercept (17.4), not a two-point ratio. On my SEC panel (`decr.py`, DERIVED, GAAP, nominal) the same pooled slope is 0.21 and 0.19 on declines only. The right comparator is the realised ratio in windows with a revenue fall: 152 three-year windows with a revenue drop of 5% or more among 57 consumer discretionary names: EBIT lost per $ of sales lost p25 0.09, **median 0.31**, p75 0.63; 29% exceed 0.54 and 18% exceed 0.74. Two-year windows (n = 151): median 0.40, p75 0.79, 40% exceed 0.54. So Nike's 0.54 is above median, not seven times the sector; 0.74 is around the 80th percentile. Rewrite: "about 50 cents (47 to 54, tariff-neutral) against a peer median of 31 to 40 cents".

**Cause (opex flex).** Gross profit fell 2,976: volume at the FY24 gross margin 2,212, rate 764; opex fell only 462 (9 cents of cost flex per $ of sales lost); unchanged. Stripping FY24 restructuring in SG&A (379) and FY26 severance in operating overhead (231): SG&A 16,197 vs 15,883, a change of -314, or 6 cents per $ (DERIVED). The conclusion that costs did not flex stands.

## 3. Reverse DCF at 9.4%

Rerun of `dig_1_rdcf_replication.py` (copied as `N8_check_scripts/rd.py`; equity per share = (EV + cash 8,368 - debt 7,893) / 1,487M shares; check: 14.11% at 10% WACC, g 2%, CAGR 3% gives $35.31 = price). DERIVED. Base: tax 22.5%, ROIC 20% in the terminal reinvestment, margin ramp from FY28 consensus (7.2%) to the target in FY31, held to FY36, terminal at FY36.

| FY31 margin | 8% WACC | 9% | 10% | 11% |
|---|---|---|---|---|
| 6.2% | 22.10 | 18.96 | 16.62 | 14.81 |
| 7.3% | 25.68 | 21.98 | 19.22 | 17.09 |
| 8.3% | 28.94 | 24.73 | 21.58 | 19.15 |
| 9.4% | 32.53 | **27.75** | **24.18** | 21.42 |
| 11.6% | 39.71 | 33.79 | 29.38 | 25.97 |
| 14.0% | 47.53 | 40.38 | 35.05 | 30.92 |

N8's $24 and $28 were a linear interpolation; the exact rerun gives $24.18 and $27.75, so the figures survive (-31% and -21% vs $35.30). Price is linear in margin (about $2.36 per point at 10%), so there is no convexity correction for the right tail, and N8's remark that the mean "ignores the right tail" is unnecessary.

Sensitivities at 9.4% (price per share): growth CAGR 0% / 1% / 3% / 5%: $22.12 / 22.76 / 24.18 / 25.78 at 10% WACC and 2% g; $25.05 / 25.89 / 27.75 / 29.85 at 9%. Terminal growth 1% / 2% / 3% at 10% WACC and 3% CAGR: $23.30 / 24.18 / 25.30; at 9%: $26.43 / 27.75 / 29.49. Tax 18% / 20% / 22.5% / 25% / 28%: $25.47 / 24.90 / 24.18 / 23.47 / 22.61 (10% WACC). Ramp done by FY29 / FY31 / FY33: $24.59 / 24.18 / 23.81. **WACC is the swing:** at 8% the same 9.4% is worth $32.53, only 8% below the price; the market-implied margin at $35.30 is 14.1% (10%), 12.2% (9%), 10.3% (8% WACC, 3% CAGR). So "$24 to $28" holds for 9% to 10% WACC only and the pitch must defend that range.

**Internal inconsistency.** The model holds 9.4% as the terminal margin forever, but the same regression (r = 0.73 per 5 years) predicts a further closing of the gap after FY31: 12.38 - 4.08 x 0.73^2 = 10.2% by FY36. A terminal margin of 10.2% gives $29.95 (9%) and $26.07 (10%); 11% (sector mean) gives $32.14 and $27.96; 12.4% gives $35.99 and $31.27. A bull will say the pitch values Nike at a margin its own method says is only a waypoint. Fair reply: this adds $2 to $4 per share, leaving $26 to $30, still 15% to 26% under the price at 10% to 9% WACC.

## 4. The 13-episode apparel cross-check

- **Not reproducible as written.** `N8_derived.py` types `n_ep=13; k33=3; k57=2` ("counts typed here"); the note says they were computed in section 6 but no code is in the repo. My replication of the stated rule on `D5_valuation_annual_xbrl.csv` (9 firms excluding Nike; operating income, pretax plus interest where blank; margin at least 4 points under the prior 5-year max; one per spell; five more years) gives **12 episodes, 4 gaining 3.3 or more, 3 gaining 5.7 or more** (DECK 2017 +18.0, PVH 2021 +17.6, WWW 2021 +15.7, UAA 2018 +5.3). 
- **The gainers are not Nike-like.** All four start at a negative margin (-0.1, -15.0, -7.7, -0.5): impairment, COVID loss or restructuring years where reversal is arithmetic. From a positive margin the count is 0 of 8, median change about -0.6. That strengthens the skeptic conclusion but means the "23%" is not meaningful as stated either way.
- **Sample.** Nine hand-picked US filers (VFC, COLM, DECK, UAA, LULU, CROX, PVH, RL, WWW); no adidas, Puma, Skechers, Levi, Tapestry, Hanesbrands, G-III, Capri. Survivorship: filers alive in 2026 (biases recovery up). Comparability: most of these firms have revenue under $5B against Nike's $46B (only VFC, RL and PVH are larger; I did not tabulate it). LULU entered at a 24.6% margin, a different situation. Overlapping years, COVID inside many windows, GAAP one-offs. My wider panel (73 companies, same rule with a 2-year persistence filter, positive margin) gives 12 of 49 (24%) and 3 of 18 for brands, consistent with N8's 15% to 25% for +3.3, but with the small and noisy caveats above.
- **Nike is not the median analog.** Nike has a 15-of-19-years record of EBIT margin at 12% or more (DERIVED from nike_m), which the bull will cite, but its decline is a two-year, not a one-year, dip (FY25 8.2%, FY26 8.3%).

## 5. What survives and what must change in N8

Survives as stated: the r = 0.73 statistic and page; $24 and $28 as outputs of the repo reverse DCF (exactly $24.18 and $27.75); the direction that the market price needs a margin well above the expected one; empirical 15% to 25% chance of +3.3 points.
Needs a caveat: 9.4% (say "about 8.5% to 9.4%, with the book's own sector mean giving 9.0%"); the FY26 start (8.3% includes a $986M refund that offsets an equal cost); the 54 cents (say tariff-neutral 47 to 54 and name the 74 cents ex-refund); the DCF (state WACC dependence and the flat terminal margin).
Wrong or must be removed: 7.4 cents as the sector decremental margin; "P(14%+) 2% to 10%" (use 5% to 15%); the "3 of 13" count (typed, not reproducible, gainers all start from negative margins); "9.4% is the most favourable choice for Nike" (a low r combined with Nike's own mean produces 10.3% to 10.9%).

## 6. Strongest honest version a judge cannot knock down

At $35.30 and a 10% cost of capital the market is paying for an EBIT margin near 14% by FY2031 (12.2% at 9%, 10.3% at 8%) against 8.3% reported in FY2026, which is 6.2% without a one-time $986M tariff refund that offsets about $1.1B of tariff cost in the same year and about 9.4% if both are removed. Mauboussin and Callahan's Base Rate Book (p. 62) puts five-year persistence of consumer discretionary operating margin at 0.73 with a sector mean of 11%, which implies an expected FY2031 margin of about 9.0% (9.4% if Nike's own 12.4% mean is used), and in 2009 to 2025 SEC filings for 57 consumer discretionary companies, firms sitting two or more points below their own ten-year mean gained 3.3 points or more over five years about one time in five (16% to 24%) and 5.7 points or more about one time in eight (10% to 18%), with a median change of zero. At 9.4% the repo's reverse DCF gives $24 at a 10% WACC and $28 at 9%, so the price asks for an outcome that happens in roughly the top fifth to top quarter of comparable cases, and a margin of 11.6% (Nike's peer-parity level) would still leave the shares worth $29 to $34 at a 10% to 9% WACC. The case does not depend on the point estimate; it depends on a cost of capital of 9% or higher and on FY2027 (consensus 5.7%) not being the bottom.

## 7. The sentence a bull will use

"adidas went from a 6% margin in 2014 to 11.3% in 2019 and from 1.3% in 2023 to 8.3% in 2025, Ralph Lauren rebuilt from 8% to 14.5%, Nike itself recovered from 10.2% to 13.3% in a single year in 2010, and a pooled correlation of 0.73 across 40,000 company-years of retailers, carmakers and hotels says nothing about a brand whose margin has been 12% or more in 15 of the last 19 years and whose FY2026 includes $385M of severance and a tariff regime that a court has since struck down; at an 8% to 9% cost of capital, which is where most sell-side models sit, a 9.4% margin is already worth $28 to $33 and 11.6% is worth $34 to $40."

## 8. Routes tried and result

| Fact needed | Route | Result |
|---|---|---|
| Book row r = 0.73 | mjbaldbard.wordpress.com compilation (curl, 20 MB, pdftotext) | worked, OPENED pp. 59 to 62 |
| same | josephnoko.com copy of the September 2016 edition | worked, same row |
| same | WebSearch for text of Exhibit 4 | partial (no figures in snippets) |
| same | official Credit Suisse and Morgan Stanley files, Wayback | not reachable per N8; not repeated; two hosted copies agree |
| Peer margins 2009 to 2025 | data.sec.gov companyfacts, 73 CIKs, no contact header, no email | worked (LCUT 404) |
| adidas margin history | AR2025 additional-information PDF (report.adidas-group.com), AR2015 via ddd.uab.cat | worked |
| Nike restructuring, IEEPA, FX | `data/nike_filing_facts.csv` | worked; no filed FX split of EBIT after FY24 (gap) |
| Pre-2009 comparables (Nike 2008 to 2012 from repo; Coach, RL pre-2009) | XBRL starts about FY2009 | partial; settle with each company's 10-K selected financial data |
| Panel margin adjustments for impairments | not done; XBRL impairment tags not merged | open: would remove GAAP noise and probably raise r and tighten the dispersion |

What would settle the open points: (i) a one-off-adjusted margin panel (add restructuring and impairment tags, or company non-GAAP) for 60+ consumer brands with pre-2009 history from 10-K selected data; (ii) the official Base Rate Book file or a newer Counterpoint Global edition to confirm 0.73 and give firm-level dispersion; (iii) the Q2 FY27 print (December) to see whether the FY27 5.7% consensus is the trough.
