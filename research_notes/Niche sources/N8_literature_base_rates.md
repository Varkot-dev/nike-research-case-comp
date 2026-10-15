# N8: Published research applied to Nike (disclosure withdrawal, guidance, investor days, base rates, brand and distribution)

Prepared 2026-10-15. Extends `Smoking gun hunt/G11_disclosure_withdrawal.md`, `G9_guidance_record.md`, `Deep dives Oct 14/D7_investor_day.md`, `D5_valuation.md` and `20_base_rates.md`. Derived numbers are reproduced by `N8_derived.py` (writes `N8_derived_numbers.csv`). Run it with `python3 -I`.

Tags: **OPENED** = I read the full text of the file named (page numbers are the printed pages of that file). **ABSTRACT** = I read only the abstract, returned by the Crossref API (verbatim, no page number exists). **SNIPPET** = a search-result or secondary summary only. **DERIVED** = my arithmetic on tagged inputs. Everything a paper says is labelled "authors' finding". Everything labelled "application" is mine. All quoted text has en-dashes and em-dashes replaced with hyphens (repo rule); no other change.

## 1. Verdict

**Smoking gun: NO.** The literature does not turn G11, G9 or D7 into a return forecast. Of the three disclosure and guidance papers I could read in full or in part, none measures a long-run return after a firm withdraws KPIs. What the research does give is (a) one hard base-rate result that is strong and Nike-specific (the margin the market requires), (b) one event-size prior for a disclosure cut announced at the Investor Day, and (c) a clear statement of where Nike does and does not fit the profile of firms that go quiet.

Strongest predictions, ranked by how well they are supported:

| # | Prediction (application, mine) | Basis | Strength |
|---|---|---|---|
| 1 | Expected FY31 EBIT margin from FY26's 8.3% is about 9.4% (9.0% to 9.4% across sector mean choices), not 11% to 14%. Probability of reaching 11.6% is about 15% to 25%, of reaching 14% about 2% to 10% | Base Rate Book margin persistence (authors: 5-year r = 0.73 for consumer discretionary) plus Nike's own mean; cross-checked on 13 apparel and footwear margin-drop episodes (3 of 13 gained 3.3 points or more in 5 years, 2 of 13 gained 5.7 or more) | Strong on direction, moderate on the exact probability (dispersion is uncertain, section 6) |
| 2 | 85% to 87% of Nike's EBIT fall since FY23 and FY24 is not volume deleverage; recovering to 11.6% on FY28 revenue needs +$1.9B of EBIT, which at the sector operating-margin beta would require about $25.9B more sales | Base Rate Book operating margin beta 0.074 (consumer discretionary, 3-year) against Nike filings | Strong (arithmetic on opened inputs) |
| 3 | Revenue is NOT the hurdle: the consensus path (FY28 $43.6B, then 3% a year) is about +0.5% a year nominal FY26 to FY31, below the 2.0% real median for companies above $25B | Base Rate Book Exhibit 4 | Strong; it tells the pitch to argue margin, not growth |
| 4 | If Nike announces on Nov 16 to 17 that it will stop reporting standalone segments or KPIs, the prior is a 3-day abnormal return of about -4.8% (95% interval -8.9% to -0.7%), less if framed as long-term focus | Chen, Matsumoto and Rajgopal, N = 73 announcers | Moderate; their firms stopped quarterly EPS guidance, not segments |
| 5 | The first below-midpoint print cost Nike -4.4 points versus the S&P 500 on Oct 2, about one and a half times the roughly 3% quarterly premium that meeting or beating earns | Bartov, Givoly and Hayn (abstract) against Nike prices | Weak to moderate (abstract only) |
| 6 | After a disclosure cut, expect analyst coverage and forecast accuracy to deteriorate modestly (about 0.6 fewer analysts, forecast error up about 1 cent per share per quarter for a $35 stock) | Houston, Lev and Tucker Table 9 | Moderate on sign, small in dollars |

## 2. Disclosure withdrawal and future performance

### 2.1 What the papers found (authors' findings)

**Chen, Matsumoto and Rajgopal, "Is Silence Golden?"** (J. Accounting and Economics 2011; I opened the October 2006 preprint at `business.columbia.edu/sites/default/files-efs/pubfiles/12918/Rajgopal_is_silence.pdf`, OPENED; page numbers below are the preprint's). Sample: 96 firms that publicly renounced quarterly EPS guidance from 10/2000 to 1/2006 (72 stoppers, 24 switchers to annual only; 73 with usable return data).
- Abstract (unnumbered cover page): "We document an average negative 4.8% three-day return around the announcement to stop guidance and this reaction is associated with poor future performance."
- p. 2: "Together these results suggest that, on average, the primary driver behind the decision to stop guidance is not to focus investors on the long-term, as many firms claim."
- p. 21 (Table 3, p. 48): "The intercept indicates that the average market reaction, after controlling for the surprise in earnings, is a statistically significant negative return of -4.8% (p<0.01)." The three-day return is negative for 65.8% of the sample (Table 3 Panel A, p. 48). t = -2.31, so the standard error is about 2.1 points (DERIVED) and the 95% interval is -8.9% to -0.7%.
- p. 23: "The coefficient on DFEARN is positive and statistically significant (t=3.83, p<0.01), indicating that firms with more negative revisions in expected future performance are penalized with a more negative market reaction at the time of the announcement." (DFEARN = revision in analysts' next-quarter forecast after the announcement.) The paper does not report a post-announcement abnormal return or earnings path; "future performance" is measured by analyst revisions.
- p. 25: firms with a history of meeting or beating consensus "fare better" on announcement; firms that state a long-term focus reason are "penalized less severely" (t = 2.27, one-tailed).
- Abstract: after stopping, "analyst forecast dispersion increases and forecast accuracy decreases", with no change in analyst following.

**Houston, Lev and Tucker, "To Guide or Not to Guide?"** (Contemporary Accounting Research 2010; I opened the February 2008 working paper, `archive.nyu.edu/bitstream/2451/27472/2/SSRN-id875184.pdf`, OPENED; printed pages). Sample: 222 stoppers and 676 maintainers, 2002 to Q1 2005.
- Abstract: "Taken together, our evidence indicates that guidance stoppers are primarily troubled firms and stopping guidance does not benefit either the stoppers or their investors."
- p. 13: "Most guidance stoppers do not announce or explain the change in disclosure policy." Only 26 of 222 (11.7%) announced (p. 15).
- p. 18: stoppers had lower earnings change, fewer meet-or-beat quarters, more loss quarters and lower returns, "These comparisons indicate that the stoppers are troubled firms."
- Table 3 (p. 41), stoppers versus maintainers: meet-or-beat share of prior quarters 69.2% vs 83.3% (mean); one-year market-adjusted buy-and-hold return -24.3% (median -31.1%) vs -0.2% (median -10.0%); change in CEO or CFO within 6 months 19.8% vs 8.7%; loss quarters 27.6% vs 17.9%; FutureEPS (change in EPS from four pre-event to four post-event quarters, deflated by price) mean -0.001 vs +0.006, t = -1.11 (not significant), Wilcoxon z = -3.13 (significant).
- Table 5 (p. 44): stoppers' meet-or-beat rate falls from 75.7% (4 quarters before) to 63.5% (1 quarter before) and 59.9% one quarter after; maintainers stay at 80% to 84%. Share of stoppers with an EPS decrease peaks at 52.3% one quarter before, against 31.8% for maintainers.
- Table 9 (p. 49, robust regression): the Stop coefficient is -0.577 on change in analyst following (t = -3.95), +0.0002 on forecast dispersion (t = 6.55) and +0.0003 on forecast error (t = 3.35), both deflated by price. Table 7 (p. 46): no increase in capex (coefficient -0.0011, t = -0.90); R&D coefficient +0.0014 (t = 3.13).
- p. 3: "we do not substantiate any of the major benefits claimed for ceasing the practice of guidance." p. 3: stoppers "did not enhance, but curtail, the disclosure of alternative, forward-looking information."
- p. 4, footnote 5: analyst coverage falls for stoppers who did not announce, not for those who announced (so the announced-only sample of Chen et al. likely understates the coverage loss).

**Segment and KPI-level papers (ABSTRACT only, via Crossref; full texts not opened, see section 8):**
- Hope and Thomas (J. Accounting Research 2008, DOI 10.1111/j.1475-679x.2008.00289.x): "nondisclosing firms, relative to firms that continue to disclose geographic earnings, experience greater expansion of foreign sales, produce lower foreign profit margins, and have lower firm value in the post-SFAS 131 period. Our conclusions are strengthened by the fact that these differences do not exist in the pre-SFAS 131 period and do not relate to domestic operations."
- Berger and Hann (The Accounting Review 2007, DOI 10.2308/accr.2007.82.4.869): "Our results are consistent with the agency cost motive hypothesis, whereas we find mixed evidence with regard to the proprietary cost motive hypothesis." (Agency cost motive = managers withhold segments with low abnormal profits.)
- Botosan and Stanford (The Accounting Review 2005, DOI 10.2308/accr.2005.80.3.751): firms "used the latitude in SFAS No. 14 to hide profitable segments operating in less competitive industries" and "no evidence" they used it "to mask poor performance". This is the opposite motive and the one result in the set that cuts against the adverse reading of G11.
- Kothari, Shu and Wysocki (J. Accounting Research 2009, DOI 10.1111/j.1475-679x.2008.00318.x): "Our analysis suggests that management, on average, delays the release of bad news to investors."
- Hutton, Marcus and Tehranian (J. Financial Economics 2009, DOI 10.1016/j.jfineco.2008.10.003), SNIPPET from SSRN abstract: opacity (earnings management proxy) is linked to higher R-square and more frequent stock price crashes, with the relation fading after Sarbanes-Oxley.

### 2.2 Does Nike's G11 pattern match their samples? (application)

| Feature | Literature sample | Nike (G11, G9, repo) | Match? |
|---|---|---|---|
| Poor performance precedes the withdrawal | All 4 performance variables significant at 5% (HLT p. 4 to 5) | 11 of 12 removed families with a clear direction were deteriorating (G11) | Yes, same sign |
| Strength of the skew | EPS-decrease share 52.3% for stoppers vs 31.8% for maintainers at t-1, a ratio of 1.6 (HLT Table 5, p. 44) | Removal rate 48% of deteriorating families vs 6% of non-deteriorating, a ratio of about 8 (G11 section 4) | Nike's skew is larger, but the units differ (firms vs KPI families) and G11's control list is my own; do not compare the ratios as like for like |
| Guidance record | Stoppers' meet-or-beat 63.5% at t-1 vs 82.7% for maintainers (HLT Table 5) | 16 of 16 inside or above the guided range, 14 of 16 at or above midpoint (87.5%) (G9 section 8) | **No.** Nike looks like a maintainer on this feature |
| Announced or silent | 88.3% silent (HLT p. 15) | All 16 G11 removals unannounced | Yes |
| Management change within 6 months | 19.8% vs 8.7% (HLT Table 3); odds ratio e^0.974 = 2.65 (HLT Table 4, p. 43) | CEO change Oct 14 2024; CFO separation 8-K Jun 23 2026 (G9, G11) | Yes (timing of the first G11 wave relative to the 6-month window is not tested; G11 alt. 6 found the first wave is under the old CFO) |
| Prior one-year stock return | -24.3% market-adjusted for stoppers | NKE -49.2% vs S&P 500 +14.4% to Sep 30 2026, a gap of 63.6 points (market data, DERIVED) | Yes, 2.6 times as severe |
| Item withdrawn | Quarterly EPS guidance, which Nike never gave | KPI families, receivables by segment, returns rollforward, comps | **Different object.** No paper opened tests KPI-family withdrawal |

Alternatives for "why Nike went quiet", tested against the above:
1. Long-term focus (the reason stoppers give): the authors' evidence is against it (CMR p. 2; HLT p. 3 show no capex gain and curtailed forward-looking disclosure). Nike gave no reason for 15 of 16 families (G11). Ruled out as an explanation supported by evidence, not as a motive.
2. Rule changes: explains 4 of 25 removals (G11). Ruled out for the rest.
3. Proprietary-cost protection (Botosan and Stanford, Berger and Hann on the proprietary side): predicts withdrawal of HIGH-profit items. G11's removed items were deteriorating, not high-profit. Ruled out for the bulk; cannot be excluded for the largest-factory share.
4. Agency-cost motive (Berger and Hann, Hope and Thomas): predicts withdrawal of low-profit items, with lower margins and firm value afterward. Survives, and is the only explanation that also fits G11's direction.
5. Troubled-firm effect (HLT): survives for the earnings, stock-return and management-change variables; fails on the meet-or-beat variable.
Two explanations survive (3 partly, 4 and 5). What would decide: the Q2 FY27 10-Q and the Investor Day (are the FY28 three-geography segments a recast with comparatives, ASC 280) and I/B/E/S dispersion and coverage counts for Nike since Q1 FY25 (on the Refinitiv pull list).

### 2.3 What future earnings and returns follow? (application, with limits)
- Earnings: HLT's FutureEPS gap is -0.7% of price (stoppers -0.001 against +0.006). At $35.30 that is -$0.25 per share, about 19% of FY27 consensus EPS $1.29, but it is statistically insignificant on means (t = -1.11) and significant only on ranks. Use the sign, not the size. DERIVED.
- Returns: no opened paper reports abnormal returns beyond the announcement window. CMR's -4.8% is an announcement effect and Nike's removals were never announced, so there is no event to apply it to. The only direct application is to a future announced change (section 4).
- Information environment: HLT p. 49 gives -0.577 analysts, +0.0003 of price in forecast error. At $35.30, +$0.011 a quarter, or about 3% of a quarterly EPS of about $0.35 to $0.40 (my approximation). Small.
- Crash risk (Hutton et al., SNIPPET): linked to opacity. Not tested on Nike; no Nike-specific number.

## 3. Conservative guidance and the first sub-midpoint print (G9)

What I could open: abstracts only (Crossref). Authors' findings:
- Bartov, Givoly and Hayn (J. Accounting and Economics 2002, SSRN 247435): "firms that manage to meet or beat their earnings expectations enjoy an average quarterly return that is higher by almost 3% than their peers that fail to do so" and the premium reflects that meeting or beating is "informative of the firm's future performance."
- Skinner and Sloan (Rev. Accounting Studies 2002, SSRN 172060): "growth stocks exhibit an asymmetric response to earnings surprises... while growth stocks are at least as likely to announce negative earnings surprises as positive earnings surprises, they exhibit an asymmetrically large negative price response to negative earnings surprises." They attribute the growth-stock return shortfall to "overoptimistic expectational errors that are corrected through subsequent negative earnings surprises."
- Myers, Myers and Skinner (J. Accounting, Auditing and Finance 2007): firms with long strings of consecutive EPS increases "enjoy abnormal returns that average more than 20 percent per year during the first five years of these strings" and the premia disappear with "rapidity... once the strings end".
- Chen et al. (OPENED, p. 25) and HLT Table 5 (OPENED, p. 44): firms with a meet-or-beat history are penalized less when they do stop guiding.

Application to Nike:
1. Nike's streak is intact on the measures that the literature uses. G9: 16 of 16 inside or above the range on revenue and gross margin; Q1 FY27 EPS was $0.48 against LSEG consensus $0.43 (secondary, G9 section 7), i.e. an EPS beat. Only revenue versus the guide midpoint (-4.33% against -3.5%) broke. The Myers et al. string logic therefore does not yet apply: no EPS string has ended.
2. Observed reaction: NKE fell 3.64% on Oct 2 2026 (35.15 to 33.87) while the S&P 500 rose 0.73%, an abnormal -4.4 points (`data/nke_daily_prices.csv`, Yahoo `^GSPC`, DERIVED). That is about 1.5 times the roughly 3% quarterly premium in Bartov et al., and below the 7% earnings move that options implied (repo note 17). Nike has not been repriced as a broken streak; it has been repriced as a one-quarter revenue shortfall.
3. The asymmetry (Skinner and Sloan) matters for Dec 17, because Nike trades at 21.5 times FY28 EPS against a 13.2 peer median (D5), i.e. as a glamour stock on trough earnings. If Q2 FY27 revenue lands below the low end of the "multi-point headwind" framing, the authors' result predicts a larger loss than the symmetric gain from a beat. Magnitude cannot be set from abstracts.
4. Alternatives for "the beats were conservative guidance" versus "the trend improved faster than management expected" (G9 section 8, items 2 and 3): not separable with these papers either. What would separate them: sell-side estimate paths around each guide (I/B/E/S), not available.
5. The Base Rate Book (OPENED) has a 5,400-event study of one-day drops of 10% or more relative to the S&P 500 ("Managing the Man", printed pp. 95 to 109). Nike's -4.4 points is below that threshold, so those base rates do not apply to Oct 2 and I do not use them.

## 4. Investor and analyst days (D7)

What I could open: the Crossref abstract of Kirk and Markov, a university summary and a 2023 abstract. Full text of Kirk and Markov (The Accounting Review 91(6), 2016, DOI 10.2308/accr-51418) was **not** opened (section 8).
- Authors' findings (ABSTRACT): "Analyst/investor days are less frequent, but with longer duration and greater price impact than conference presentations." "When these two mediums are scheduled in close temporal proximity to each other, analyst/investor days diminish the information content of conference presentations, but not vice versa." SMU summary (SNIPPET): "Around analyst/investor days, the authors find a significant bump in return volatility and trading, compared to a conference presentation."
- Miwa (Global Finance Journal 2023, ABSTRACT): "abnormal returns around AI days are irrelevant to the tone of the Question-and-Answer session, suggesting that AI days mainly provide a partially known supplemental explanation rather than offer new information to analysts and investors." (The Q&A tone does predict later analyst forecast revisions.)

Comparison with D7 (application):
- Consistent: D7's mean absolute day-1 move versus the S&P 500 of 7.0% (median 4.7%) across 28 events is the "greater price impact" Kirk and Markov report. Their abstract gives the size relative to conference presentations, not a sign, so it neither confirms nor contradicts D7's finding that cut or vague events fall (mean -10.8% day 0) and raised dated targets rally (+4.8%).
- Miwa's result fits D7's NEUTRAL group (13 events, about 0): when the day carries mostly known content, the abnormal return is unrelated to the tone of the discussion.
- New input for D7's decision table (D7 section 5.5 rows "Segment disclosure ... Not in sample"): if the Investor Day announces a disclosure cut (for example ending standalone North America, Greater China and Converse reporting from FY28, G11 section 8), the Chen et al. announcement prior is -4.8% over three days (95% interval -8.9% to -0.7%), softened if framed as long-term focus. D7's 28 events do not contain such a case, so this is the only external prior available. Caveat: their firms stopped quarterly EPS guidance, a larger information loss than a segment recast with restated comparatives.
- Not resolved by the literature: whether Investor Day target changes leave a drift. Needs the full Kirk and Markov tables.

## 5. Base rates (Mauboussin and Callahan)

Source: Credit Suisse, "The Base Rate Book" (September 26, 2016), Credit Suisse HOLT data, top 1,000 global companies by market value, 1950 to 2015, **inflation-adjusted**. OPENED from a third-party-hosted compilation of Credit Suisse base-rate reports (`mjbaldbard.wordpress.com/wp-content/uploads/2020/09/michael-mauboussin-e28093-base-rate-books-2015-2016.pdf`, 215 pages; the September 2016 edition starts on its page 65). The Credit Suisse and Morgan Stanley official files were not reachable (section 8). Cross-check of the copy against an independent secondary summary: the 3.0% share of $1.25B to $2.0B firms sustaining more than 20% for 10 years matches Exhibit 4 exactly (SNIPPET). Page numbers below are the report's own printed pages.

### 5.1 Sales growth for a company of Nike's size (authors' data; application mine)
Nike FY26 revenue $46.4B (FY2026 10-K p. 31), so the reference class is "Sales >$25,000 Mn" (Exhibit 4, p. 25). Authors' finding, p. 26: "as firm size increases the mean and median growth rates decline, as does the standard deviation of the growth rates."

| Real sales CAGR | 3-year | 5-year |
|---|---|---|
| Mean / median / standard deviation | 2.4% / 2.2% / 10.9% | 2.1% / 2.0% / 8.6% |
| P(CAGR below 0) | 36.9% | 35.6% |
| P(CAGR 5% or more) | 36.2% | 31.8% |
| P(CAGR 10% or more) | 18.0% | 13.7% |
| Observations (>$25B class) | 3,3xx (3-year bins sum to the table) | see report p. 26 appendix |

(Probabilities are my sums of Exhibit 4 bins, DERIVED; the report's appendix gives the counts.) Authors' warning on narrow forecasts, p. 21: "the standard deviation of estimates is 8.3 percent versus a standard deviation of 18.7 percent for the past growth rates." Authors' advice, p. 28: "you might start with the base rate and seek reasons to move away from it."
- Persistence of growth (Exhibit 9, p. 29): r = 0.30 for one year; the extracted exhibit shows 0.17 and 0.19 for the 3- and 5-year horizons (labels ambiguous in my text extraction; the May 2015 edition gives 0.27, 0.14 and 0.12 for 3, 5 and 10 years). Nike's prior decline therefore carries little information about the next three to five years of growth.
- Nike so far: FY23 to FY26 revenue CAGR -3.2% nominal; FY21 to FY26 +0.8% nominal (DERIVED, filings). Consensus FY28 $43.6B (D5) is -3.1% a year from FY26, then 3% a year to FY31 gives about $47.6B, +0.5% a year over five years. In real terms that is below the 2.0% median of the class.
- What the base rate implies: the market's required path is not a growth bet. A 3% nominal rebound after FY28 sits near the median of its class (a 5-year real CAGR of 0.5% is at about the 35th to 64th percentile band: 35.6% of companies shrank, 64.4% grew). The pitch should not argue "growth will disappoint"; it should argue margin.
- Management targets versus base rates: Nike's 2021 outlook was high-single to low-double-digit revenue growth (D7 E03). A 5-year real CAGR of 5% or more occurred in 31.8% of the class; Nike delivered +0.8% nominal over FY21 to FY26 (DERIVED, nominal; an inflation adjustment would lower it). The 2021 target was at about the 68th percentile of outcomes (inside view), and the result is at about the 40th to 50th. This is a calibration data point, not proof.

### 5.2 Margin persistence and what the market requires (the key calculation)
Authors' findings (printed pp. 59 to 62): "the operating profit margin is very persistent over one-, three-, and five-year periods. For example, the correlation between operating margin in the current year and three years in the future has a coefficient, r, of 0.79... But even the five-year correlation is relatively high at 0.72" (p. 59). "There is only slight regression toward the mean... a sensible approach is to start with last year's operating margin and seek reasons to move away from it" (p. 60). Exhibit 5, p. 62: consumer discretionary five-year r = 0.73, median operating margin 10%, average 11%.

Application (DERIVED; `N8_derived.py`). Nike EBIT margin FY2026 8.3% (FY2026 10-K p. 31, 32: EBIT $3,850M, revenue $46,398M); Nike mean FY08 to FY26 12.4% (`D5_valuation_annual_xbrl.csv`), 10-year mean 11.8%.

| Reversion target | Expected FY31 EBIT margin from 8.3% (r = 0.73) |
|---|---|
| Nike's own 19-year mean 12.4% | 9.4% |
| Nike's 10-year mean 11.8% | 9.3% |
| Sector average 11% | 9.0% |
| Sector median 10% | 8.8% |
| From FY27 consensus 5.7%, four years, r about 0.76 (interpolated) | 7.3% |

The market requires 12% to 14% at a 10% WACC and about 11% to 12% at a 9% WACC (`thesis_tests/consensus_and_valuation.md` reverse DCF; parity with peers at 11.6%, D5). The authors' persistence says the expected outcome is roughly 3 to 4 points short of that, and the pooled model never reaches the requirement on expectation.

Probability of reaching the requirement, normal approximation around 9.4% (DERIVED). The base rate book gives r and the sector mean but not the dispersion of 5-year margin outcomes for one firm, so I bracket it:

| Dispersion (standard deviation, points) | P(margin 11%+) | P(11.6%+) | P(12%+) | P(14%+) |
|---|---|---|---|---|
| 2.2 (Nike's own year-to-year dispersion FY08 to FY26) | 23% | 16% | 12% | 2% |
| 3.5 | 32% | 27% | 23% | 9% |
| 5.0 | 38% | 33% | 30% | 18% |
| 8.2 (pooled residual of 10 apparel and footwear firms, noisy GAAP EBIT with one-offs) | 42% | 39% | 38% | 29% |

Empirical check that does not depend on the dispersion assumption (DERIVED from `D5_valuation_annual_xbrl.csv`, 9 apparel and footwear firms excluding Nike; episode = margin at least 4 points below its prior-five-year maximum, one episode per spell, with five more years of data; n = 13): median five-year change in margin -0.6 points; 3 of 13 (23%, Wilson 95% interval 8% to 50%) gained at least 3.3 points (the gap from 8.3% to 11.6%); 2 of 13 (15%, interval 4% to 42%) gained at least 5.7 points (the gap to 14%). The median share of the gap to the prior peak that was closed after five years is -8%; 2 of 13 closed all of it. Own-sample caveats: tiny n, GAAP EBIT with restructuring and impairments (for example Crocs, Under Armour, VF), overlapping years, COVID inside many windows.

**Reading.** Combining the regression (about 16% to 27% for 11.6% at the two lowest dispersions) and the empirical check (23%), the probability that Nike's FY31 EBIT margin reaches the 11.6% parity level is about 15% to 25%, and for 14% about 2% to 10% (empirical 15% is the upper bound). The market price needs the upper tail of the distribution, not the middle. Value mapping (my interpolation of the repo reverse DCF cross-checks, `consensus_and_valuation.md` lines 239 and 247): an expected margin of 9.4% corresponds to about $24 per share at a 10% WACC and about $28 at 9%, against $35.30, that is -21% to -32%. This is a model value from a mean, not a price target, and ignores the right tail.

### 5.3 Why margins fell and what recovery would take (operating leverage)
Authors' Exhibits 11 and 12 (p. 50): consumer discretionary operating-margin beta 0.081 (one-year) and 0.074 (three-year), regression y = 0.074x + 17.4 ($M change in operating income on $M change in sales over three years).
- Nike FY23 to FY26: sales -$4,819M, EBIT -$2,345M. The sector slope predicts -$339M. **85.5% of the EBIT fall is not explained by volume leverage.** FY24 to FY26: sales -$4,964M, EBIT -$2,689M, predicted -$350M, 87.0% unexplained (DERIVED). This is consistent with the repo's rate-driven bridge (gross margin 44.6% in FY24 to 42.9% in FY26 and operating overhead near 24.5% of revenue; `research_notes/14_profit_bridge_and_thesis_scorecard.md`), and it is a regression across firms, so it is a benchmark, not Nike's own beta.
- Recovery: FY28 EBIT at consensus 7.2% is $3.14B; at 11.6% it is $5.06B, +$1.92B. At the sector beta that needs about +$25.9B of additional sales (DERIVED), more than half of FY28 revenue. Recovery to the market-required margin must therefore come from gross margin rate and overhead, not from volume. This is the base-rate version of D1's margin-first framing.

## 6. Limits of section 5 (alternatives and what is not shown)
| Alternative explanation or challenge | Verdict |
|---|---|
| "Nike is a special company, base rates do not apply" | Not ruled out. The authors say start with the base rate and move away for reasons. Reasons for Nike: brand, scale, FY21 15.5% margin, Pace savings. Reasons against: Nike's own record of 2017 and 2021 profit targets all missed (note 19). Both are tilting arguments, not numbers |
| Survivorship | Authors: "modest survivorship bias" (p. 23); a 10-year sample needs 10 years of survival. It biases outcomes up, making 9.4% generous |
| Regression applies to a firm-specific mean | Used Nike's own mean (12.4%) as the most favourable choice for Nike; expected margin is 9.4% there and lower under sector means |
| Dispersion unknown | Bracketed in a table; the empirical check does not need it but has n = 13 |
| Cyclical depression (tariffs, China) will reverse | Persistence r already includes cycles. Tariffs (IEEPA refunds, one-offs) and China are in the repo's separate notes; not re-tested here |
| Sales and margin are correlated | Section 5.3 shows volume explains about 13% to 15% of the EBIT fall, so the correlation is weak for Nike so far |
| Mean reversion to 12.4% assumes the 2008 to 2024 structure holds | Not testable here; D5 shows the premium is a trough-earnings artifact, which is consistent |

## 7. Brand decline, availability and distribution (Romaniuk and Sharp, Ehrenberg-Bass, Thomas and Kohli)

**What I could and could not open.** I could not open Sharp's *How Brands Grow*, Romaniuk and Sharp's *How Brands Grow Part 2*, any Ehrenberg-Bass distribution paper, Keller, or Thomas and Kohli in full text (section 8). I therefore quote no passage and no page number from them. Opened instead:
- **Reibstein and Farris, "Market Share and Distribution: A Generalization, a Speculation, and Some Implications"** (Marketing Science 14(3), 1995, G190-G202). OPENED: the April 1994 working paper from the University of Pennsylvania repository (`repository.upenn.edu/marketing_papers/244`, scanned file read by OCR and the key page checked by eye; page numbers below are the working paper's printed pages). This is the paper that explains double jeopardy with distribution.
- **Wilbur and Farris, "Distribution and Market Share"** (J. Retailing 2014, SSRN 1175869): ABSTRACT only.
- **Ehrenberg, Goodhardt and Barwise, "Double Jeopardy Revisited"** (J. Marketing 1990): ABSTRACT only: "a small brand typically has far fewer buyers than a larger brand. In addition, its buyers tend to buy it less often."
- **Thomas and Kohli, "A brand is forever!"** (Business Horizons 2009) and "Reviving Weak and Dead Brands": SNIPPET only (a trade-blog excerpt of their conclusion: "Managers need to constantly watch for signs of brand decline, in the form of problems with brand knowledge, brand differentiation, and customer response"). No quantified recovery rate is available from what I opened.

Authors' findings (Reibstein and Farris working paper):
- Abstract (p. 1 unnumbered): the cross-sectional distribution-share relationship is convex, and "the marginal effect of weighted distribution on share is likely to be increasing". "In some cases, and for some measures of distribution, these convex curves have been observed in time-series data for brands that failed and lost distribution over a relatively short-period of time."
- p. 10: "For all twelve product categories, the least squared estimated exponent, a, was significantly, at the 99% confidence level, greater than one, indicating a convex relationship. The estimated values ranged from 1.80 to 4.68 across the twelve product categories." (IRI 1988 supermarket scanner data, share on %ACV; consumer packaged goods, not footwear.)
- p. 8: "Evidence for the convex effect of distribution in time series is more speculative at this point." and that distribution "forced" above a brand's "natural" level "will see it fall back to the original levels unless extraordinary efforts are made to maintain the new distribution levels" (the authors citing Nuttall's experiments).
- Wilbur and Farris (ABSTRACT): in 86% of 37 categories (79,000 SKUs) the share-distribution relation "is increasing and convex at the SKU level".

Application to Nike (mine; none of these studies is on footwear or apparel, and the exponent is cross-sectional):
1. If share is proportional to distribution raised to a, a 10% loss of weighted distribution costs 17% of share at a = 1.80 and 39% at a = 4.68; a 5% loss costs 9% to 21% (DERIVED). The sign and convexity are the authors' finding; the footwear exponent is unknown.
2. Nike's wholesale record: NIKE Brand wholesale revenue $27,397M (FY23), $27,758M (FY24), $25,883M (FY25), $27,453M (FY26) (data pack, 10-K pp. 32 to 34); Direct $21,308M, $21,519M, $18,783M, $17,720M. Wholesale returned to its FY23 level in FY26 while Direct fell 16.8% from FY23. This is a revenue series, not a distribution (ACV) series, so the exponent cannot be applied to it; Nike has not published doors or weighted distribution.
3. The "forced distribution reverts" result matches the repo's evidence that the return came on price: Amazon first-party entry models 25% to 30% below nike.com price and 49% of Nike road colorways marked down at Running Warehouse (`thesis_tests/marketplace_pricing_and_shelf_share.md`). The authors' reading predicts that regained shelf space not backed by sell-through erodes again; G2's wholesale DSO +4.5 to +9.7 days is consistent with that, but it is not a test.
4. Convexity cuts both ways: the loss from the wholesale exit was larger than proportional, and each regained point of distribution is worth more than a proportional point if sell-through holds. The literature cannot separate "regained points are productive" from "regained points are pushed" for Nike; this is the same sell-in versus sell-through question the repo already carries (D2).
5. Double jeopardy (Ehrenberg et al., ABSTRACT): small share brands have fewer buyers and lower purchase frequency. Nike is the largest brand in its category, so double jeopardy raises the cost of share loss (fewer buyers and fewer repeat purchases at once) but does not say Nike's base is at risk at current scale. Not quantifiable from what I opened.

## 8. Routes tried and what I could not open (rule: at least five different routes before "inconclusive")

| Target | Routes tried and result | Outcome |
|---|---|---|
| Chen et al. 2011 | Crossref DOI lookup (worked, found DOI and preprint link); web search found Columbia Business School pubfile; direct download of preprint (worked) | OPENED (preprint, Oct 2006, 58 PDF pages) |
| Houston, Lev, Tucker | Web search found NYU archive; download of SSRN-id875184.pdf (worked); SSRN Delivery.cfm (403) | OPENED (working paper Feb 2008, 51 pages) |
| Kirk and Markov 2016 | SSRN abstract and Delivery (403, both); AAA journal page and article PDF (403, 403); ScienceDirect (403); ResearchGate (403); CORE search (403); Semantic Scholar API (429 and 202); Unpaywall (HTTP 422, needs an email, none supplied by rule); Wayback (connection reset); Warrington faculty page (CV link, no full text); Crossref abstract (worked); SMU Cox summary (worked) | **Full text NOT opened** after 10 routes; ABSTRACT and a university summary only |
| Kirk and Markov numbers (CARs, volatility ratios) | Same routes | Not obtained. Would be settled by the paper's tables 3 to 5 via library access or the SSRN download |
| Mauboussin and Callahan, Base Rate Book | Credit Suisse research portal (not reachable; search showed a Chrome-extension link only); Morgan Stanley PDFs (Akamai 403 with four header variants and WebFetch); Wayback of the Morgan Stanley PDFs (an available snapshot exists but Wayback is blocked from this host: connection reset and tool refusal); third-party compilation (worked) | OPENED via an unofficial third-party copy; provenance flagged; official copy not opened |
| Morgan Stanley Counterpoint Global later papers (Bayes and Base Rates 1 and 2, Competitive Advantage Period, Impact of Intangibles on Base Rates) | Direct PDFs 403 (Akamai); HTML pages 403; Wayback blocked | **NOT opened.** SNIPPET only (web-search summary): 5-year sales CAGR mean 6.9%, standard deviation 11.1% on about 19,300 observations; sales-growth r 0.16 (3-year) and 0.14 (5-year) for 1950 to 2025. These later numbers are not used in the calculations above |
| Skinner and Sloan | Springer PDF (returned a 3 KB stub, no text); RePEc abstract (worked); Crossref abstract (worked) | ABSTRACT only |
| Myers, Myers, Skinner | SAGE PDF (403); Crossref abstract (worked) | ABSTRACT only |
| Berger and Hann | AAA PDF (403); Crossref abstract (worked) | ABSTRACT only |
| Hope and Thomas; Botosan and Stanford; Kothari, Shu, Wysocki; Bartov et al. | Crossref abstracts (worked); publisher PDFs not attempted after the pattern of 403s | ABSTRACT only |
| Hutton, Marcus, Tehranian | SSRN (403 via search summary); no open copy found | SNIPPET only |
| Reibstein and Farris | UPenn repository pre-publication scan (worked, OCR plus visual check); INFORMS (not attempted, paywalled) | OPENED (1994 working paper) |
| Wilbur and Farris | Crossref abstract (worked); no open PDF found | ABSTRACT only |
| Romaniuk and Sharp, *How Brands Grow*; Ehrenberg-Bass distribution papers; Keller | Web search found no open full text or distribution-cut study | **NOT opened. No quote, page number or number is taken from them.** Would be settled by the books (library) or the Ehrenberg-Bass marketingscience.info reports (not reached) |
| Thomas and Kohli | Crossref (metadata only); econbiz (500, then bot wall); Brandland blog excerpt (worked); Birmingham repository (403) | SNIPPET only |
| SEC staff statements on KPIs | SEC release 33-10751 PDF on sec.gov (403); law-firm summaries via search (secondary: effective Feb 25 2020; asks for definition, usefulness and how management uses a metric; the guidance does not itself require continued disclosure) | SNIPPET only. Not used in conclusions. The "ceases to present" wording was not found |
| Other | The web search budget for this session was exhausted midway (shared limit of 200). Searches for further papers on dropping KPIs, same-store sales or non-GAAP measures and for investor-day return studies were therefore not run | Open. A follow-up search is needed |

## 9. What would settle the open points
1. Kirk and Markov full text (library or SSRN download): size and sign of abnormal returns and drift around investor days, to replace the 28-event sample prior in D7 with a large-sample one.
2. A 5-year margin-change distribution for large consumer firms conditional on a drop (Compustat or HOLT via the university): replaces the n = 13 check and the dispersion bracket in section 5.2.
3. I/B/E/S estimate history for Nike (coverage, dispersion and forecast error since Q1 FY25): tests the information-environment predictions in section 2.1 directly.
4. Nike weighted distribution or door counts by account (Circana or retailer filings): converts the convexity exponent into a number for Nike.
5. Morgan Stanley Counterpoint Global PDFs (open in a normal browser): update the Base Rate Book to the 1950 to 2025 sample.

## 10. Files
`research_notes/Niche sources/N8_derived.py` and `N8_derived_numbers.csv` (every derived number above). Inputs used from the repo: `data/nike_filing_facts.csv` via `research_notes/04_financial_data_pack.md`, `Deep dives Oct 14/D5_valuation_annual_xbrl.csv`, `data/nke_daily_prices.csv`, G9 and G11 notes. Market data: Yahoo chart API for the S&P 500 (no contact details in the request).
