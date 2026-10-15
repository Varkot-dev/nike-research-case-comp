# Dig 1: reverse DCF inputs, the 10% WACC, and "why not 9%?"

Prepared 2026-10-14. Price $35.35 (NKE close 2026-10-12). Scope: verify the reverse DCF grid and every input behind the 10% WACC, list every other explanation for the same result, and give a defensible answer to "why not 9%?". No new modeling: the existing reverse DCF was re-run only to check it and to test its assumptions one at a time. Replication script: `research_notes/Thesis decision/dig_1_rdcf_replication.py`. Raw downloads: scratchpad `dig1/dl/` (untrusted data).

## Bottom line

1. **The grid is right.** The script reproduces all 72 implied-margin cells and all 32 implied-growth cells in `data/valuation/reverse_dcf.csv` (branch wonderful-franklin, commit c2002f0) to within 0.005 percentage points, plus the per-share cross-check ($39.06 / $33.55 / $29.36 at 9% / 10% / 11%). The CAGR 3% column gives 14.1% to 13.4% at 10%, 12.2% to 11.4% at 9% and 10.3% to 9.4% at 8%, exactly as Pillar 1 states.
2. **The 10% is defensible, but not because of the inputs as written.** "5.24% + 1.10 x 5%" mixes a 10-year yield with an ERP that its own publisher (Kroll) pairs with the **20-year** yield, and uses the highest beta estimate available. The cleaner path to the same answer is the Kroll framework: 20-year UST 5.60% + beta 1.04 (our own 5-year monthly regression, and Damodaran's shoe-industry beta re-levered to Nike) x 5.0% ERP = 10.80% cost of equity, which gives a **10.00% WACC**. Use that.
3. **9% is also defensible, and a judge can reach it.** Damodaran's current implied ERP (4.20% on Oct 1, 2026, or 4.42% after his default-spread adjustment) with a beta of 1.0 to 1.04 gives a WACC of 8.9% to 9.0%. So do not claim 9% is wrong. Claim that the thesis holds at 9%.
4. **The WACC-free way to say it (recommended headline):** at $35.35, if Nike gets all the way back to FY24's 12.7% EBIT margin by FY31 on 3% growth, the buyer earns about **9.5% a year**. At the 10-year average margin (11.8%) about 9.0%; at a 10% margin 8.1%; if margins stay at FY26's 8.3%, 7.2%, only about 1.3 points above Nike's own bonds (about 5.9%). The market as a whole is priced for about 9.5% (Damodaran: 5.29% + 4.20%). So the price already pays for a full recovery to FY24 and leaves no reward for the execution risk.
5. **Wording fix for Pillar 1.** "Prices in margins better than FY24's" is true only at a WACC of about 9.5% or more. Safer: "The price needs Nike to get back to at least its 10-year average margin (11.8%) at a 9% cost of capital, and above FY24's 12.7% at 10%, from 8.3% today and 7.2% in FY28 consensus, on revenue 15% below FY24."

## 1. Every input checked against its source

| Input | Value used | Check | Source (opened today?) | Verdict |
|---|---|---|---|---|
| 10-year UST | 5.24% (Oct 12) | 5.24% on Oct 9 (Oct 12 was Columbus Day, bond market closed; Yahoo carries Oct 9 forward); 5.21% on Oct 13 | Treasury.gov daily par yield curve CSV 2026 (opened); Yahoo ^TNX chart (opened) | Confirmed |
| 20-year UST | not used | 5.65% Oct 9, 5.60% Oct 13 | Treasury.gov (opened) | Should be used with a 5% ERP (Kroll pairing) |
| 10-year TIPS real yield | not used | 2.91% Oct 9, 2.88% Oct 13, so breakeven inflation about 2.3% | Treasury.gov real yield curve (opened) | Terminal g of 2% to 3% nominal = about 0% to 0.7% real: conservative, not aggressive |
| Beta | 1.10 (Yahoo 1.099) | Our regressions on Yahoo dividend-adjusted closes vs S&P 500: 5y monthly 1.04 (r = 0.51, standard error 0.23); 3y monthly 0.82; 2y weekly 0.99; 1y weekly 1.00; 2y daily 0.89; 1y daily 0.68 | Yahoo chart NKE and ^GSPC (opened); Yahoo 1.099 from repo note consensus_and_valuation.md (not re-opened) | 1.10 is the top of the range. 1.04 is better supported |
| Industry beta | n/a | Damodaran Shoe (11 firms, Jan 2026): levered 1.02, unlevered 0.93; re-levered at Nike's 15% D/E = 1.04. Apparel 0.94 / 0.76 | pages.stern.nyu.edu Betas.html (opened) | Supports about 1.0 to 1.05 |
| ERP | 5.0% | Kroll recommended U.S. ERP 5.0%, reaffirmed Jan 2026, "matched with the higher of a U.S. normalized risk-free rate of 3.5% or the spot 20-year U.S. Treasury yield" | Kroll Cost of Capital Updates Jan 2026 executive summary PDF (opened); later reaffirmation Sep 2026 seen only in search snippet (not opened) | Valid only with the 20y yield |
| ERP alternative | n/a | Damodaran implied ERP Oct 1, 2026: 4.20% (trailing 12m, adjusted payout), with 5.29% T-bond; add 0.22% US default spread to ERP and deduct it from rf (5.07%). Alternatives 3.30% to 5.67%; prior month 4.14% | Damodaran home page (opened) | Supports a 9% WACC |
| Cost of debt (after tax) | 4.7% | Nike fair value of long-term debt $6.7B at Aug 31, 2026 (10-Q p.8) against $8.0B face (FY26 10-K Note 6 lists 8 notes, 2.375% to 3.875%, 2026 to 2050). Yield that prices that ladder at $6.7B: about 5.9% pre-tax, 4.6% after 22.5% tax. Ratings A+ (S&P) and A2 (Moody's), downgraded in 2025 (10-Q p.34; 10-K risk factors) | SEC EDGAR Q1 FY27 10-Q and FY26 10-K (opened) | Confirmed; immaterial (10 bp on Kd = 1 bp on WACC) |
| Debt weight | 13% | Debt 2,000 current + 5,893 long-term = 7,893; equity 35.35 x 1,485.3m = 52,506; weight 13.07% | Q1 FY27 10-Q p.3 balance sheet (opened); share count from 10-Q cover per repo (not re-opened) | Confirmed |
| Cash | 8,368 | 6,903 cash + 1,465 short-term investments | Q1 FY27 10-Q p.3 and fair value table (opened) | Confirmed |
| EV ex leases | 52,031 | 52,506 + 7,893 - 8,368 | arithmetic | Confirmed |
| Tax | 22.5% | FY26 effective 20.3% (10-K p.32); Q1 FY27 22.7% (10-Q p.9) | repo filing facts (not re-opened) | Reasonable; 20% to 25% moves the 10% answer from 13.7% to 14.6% |
| FY26 / FY24 EBIT margin | 8.3% / 12.7% | EBIT 3,850 on 46,398; 6,539 on 51,362 | FY26 10-K p.30 non-GAAP table (opened) | Confirmed |
| 10-year average margin | 11.8% | FY17 14.4, FY18 12.0 (PitchBook), FY19 to FY26 12.4, 8.0, 15.5, 14.7, 12.1, 12.7, 8.2, 8.3 (filings) = 11.83% | repo filing facts + PitchBook table (not re-opened) | Confirmed |
| Consensus FY27 / FY28 | EPS 1.288 / 1.646; revenue 43,152 / 43,645; margins 5.7% / 7.2% | Yahoo earningsTrend Oct 13 | repo note (not re-opened) | Accepted; using Zacks FY28 EPS 1.78 (7.8% margin) moves the 10% answer only from 13.8% to 13.7% |
| Terminal ROIC | 20% | Nike's own reported ROIC: 18.7% FY26, 20.2% FY25 (10-K p.30, lease-inclusive capital) | FY26 10-K (opened) | Reasonable, if anything generous at today's margins |

## 2. WACC under each mainstream framework (D/E weights 86.9% / 13.1%, Kd after tax 4.7%)

| Framework | Cost of equity | WACC | Implied steady-state margin, 3% CAGR, g 2% to 3% (midpoint g 2.5%) |
|---|---|---|---|
| Team as written: 10y 5.24 + 1.10 x 5.0 | 10.74% | 9.95% | 13.3% to 14.0% (13.7%) |
| **Kroll, own beta: 20y 5.60 + 1.04 x 5.0 (recommended base)** | **10.80%** | **10.00%** | **13.4% to 14.1% (13.8%)** |
| Kroll, beta 1.10 | 11.10% | 10.26% | 14.0% to 14.6% (14.3%) |
| Kroll, beta 1.00 | 10.60% | 9.83% | 13.1% to 13.8% (13.4%) |
| 10y 5.24 + 2y weekly beta 0.99 x 5.0 | 10.19% | 9.47% | 12.3% to 13.1% (12.7%) |
| Damodaran: 5.07 + 1.10 x 4.42 | 9.93% | 9.25% | 11.9% to 12.6% (12.3%) |
| **Damodaran: 5.07 + 1.04 x 4.42 (the "9%" case)** | **9.67%** | **9.02%** | **11.4% to 12.2% (11.8%)** |
| Damodaran: 5.07 + 1.00 x 4.42 | 9.49% | 8.86% | 11.1% to 11.9% (11.5%) |
| Outlier: 1y daily beta 0.68, 10y, 5.0 | 8.64% | 8.13% | 9.6% to 10.5% (10.1%) |

Reading: every mainstream combination lands between 8.9% and 10.3%. Across that whole band the price needs 11.1% to 14.6%, i.e. at least a return to the 10-year average and, in the upper half, more than FY24. Only an unusually low beta (0.68, from one year of daily data with r = 0.25) brings the bar down to around 10%.

## 3. "Why not 9%?" The answer to give

- **Concede, then show it does not matter.** "You can get to 9% with Damodaran's implied ERP. At 9% the price still needs 11.4% to 12.2% EBIT margins, the 10-year average, 3.5 points above FY26 (8.3%) and 4.6 points above FY28 consensus (7.2%), on revenue about 15% below FY24 ($43.6B vs $51.4B)."
- **Why we lead with 10%:** (a) Kroll's 5.0% ERP is the practitioner standard and is explicitly paired with the 20-year Treasury (5.60%), which also matches an equity's long duration; (b) Nike's measured beta is about 1.0 to 1.04, and the industry beta re-levers to 1.04; (c) the result, 10.0%, does not rely on the highest beta print.
- **Market cross-check:** peers trade at 12.9x FY2 earnings (median, repo peer table), an earnings yield of about 7.8%; with 2% to 3% growth that implies a cost of equity near 10% to 11% for the group, consistent with 10%, not 9%. (Rough check, not a model.)
- **The IRR framing removes the argument entirely:** buy at $35.35, get FY24 margins back, earn about 9.5%; get the 10-year average, about 9.0%. Both equal or trail the market's expected return of about 9.5% (Damodaran Oct 1, 2026) for a stock with company-specific execution risk.

Implied annual return (IRR) at $35.35, 3% revenue CAGR FY28 to FY36, terminal g 2% / 2.5% / 3%:

| Steady-state EBIT margin by FY31 | IRR |
|---|---|
| 8.3% (FY26 actual) | 6.9% / 7.2% / 7.5% |
| 10.0% | 7.9% / 8.1% / 8.3% |
| 11.8% (10-year average) | 8.8% / 9.0% / 9.2% |
| 12.7% (FY24) | 9.3% / 9.5% / 9.6% |
| 14.0% | 9.9% / 10.1% / 10.3% |
| 15.5% (FY21 peak) | 10.7% / 10.8% / 11.0% |

## 4. Alternative explanations for "the price implies a 12% to 14% margin", tested one at a time

Base: WACC 10%, g 2.5%, CAGR 3% gives 13.8% (9% WACC in brackets: 11.8%).

| Alternative | Test | Result | Status |
|---|---|---|---|
| Discount rate is lower than 10% | Section 2 | 9% gives 11.8%; 8.9% gives 11.5% | Partly remains: changes the level, not the conclusion (still at or above the 10-year average) |
| Nike earns a higher return on new capital (terminal ROIC) | ROIC 15% / 30% / 40% / infinite | 14.2% / 13.4% / 13.3% / 12.8% (at 9%: 12.1 / 11.5 / 11.3 / 10.8) | Ruled out as decisive: max 1 point; Nike's own ROIC is 18.7% (FY26 10-K p.30) |
| Less capital needed to grow (sales to capital) | 2.0 / 2.8 / 3.5 | 14.0% / 13.7% / 13.6% | Ruled out: under 0.3 points |
| Faster recovery (ramp ends FY30) or slower (FY33) | | 13.6% / 14.3% | Ruled out: under 0.5 points |
| Shorter forecast window (terminal at FY31) | | 14.3% | Ruled out |
| Working-capital release in down years | allow negative reinvestment | 13.6% | Ruled out |
| Consensus too low for FY28 | Zacks EPS 1.78 instead of 1.646 | 13.7% | Ruled out |
| Market expects more growth, not margin | implied-CAGR grid in reverse_dcf.csv | at a 10% margin needs 10% to 12% CAGR for 8 years at 10% WACC (6.8% at 9%) | Ruled out: FY24 to FY28 consensus is -4% a year |
| Tax rate | 20% / 25% | 13.7% / 14.6% at 10% | Ruled out |
| Leases | EV excludes $3.2B lease liabilities and EBIT is after rent; consistent | n/a | Ruled out |
| Takeover premium in the price | Class A shares controlled by Swoosh, LLC (Knight family) per FY26 10-K risk factor | n/a | Unlikely; not quantifiable |
| Price held up by dividend buyers (4.6% yield) rather than DCF value | dividend $1.64 vs FY27 guided EPS $1.15 to $1.35 = 121% to 143% payout | n/a | Remains as a technical support, not a valuation explanation; a dividend cut (declaration usually Nov 14 to 20) would test it |
| Rates fall | 10y was 3.95% at its 52-week low (Yahoo ^TNX) | about 1 point lower WACC moves the bar by about 2 points | **Remains: the main external risk to the short.** A short Nike position is partly a short on bond prices falling further |

## 5. What remains open and what would settle it

- **Beta is noisy.** Standard error 0.23 on the 5-year monthly estimate (r = 0.51). Settled only by convention: present 1.0 to 1.1 and show both ends.
- **ERP choice (4.4% vs 5.0%)** is a genuine professional disagreement; not settleable. Handle it by showing the 9% and 10% rows and leading with the IRR table.
- **Kroll September 2026 reaffirmation** seen only in a search snippet; the January 2026 PDF (opened) is enough for the claim.
- **Yahoo beta 1.099** not re-opened today (needs an API crumb); our own regression gives 1.04, which is the number we recommend citing.
- **Rates:** if the 10-year falls back toward 4%, the bar falls toward 11% to 12% even with a 5% ERP. Not settleable before Nov 1; state it as a risk.

## 6. Suggested slide text (plain language)

"At $35.35, Nike's price already assumes a full comeback. Even at a generous 9% cost of capital, it needs profit margins back at their 10-year average (11.8%), up from 8.3% last year and 7.2% expected for FY28, on sales 15% smaller than in FY24. At 10%, it needs more than FY24's 12.7%. Put differently: if everything goes right and margins return to FY24 levels, buyers earn about 9.5% a year, roughly what the whole market offers, with none of the turnaround risk paid for."

## Sources

- Treasury.gov daily par and real yield curves 2026, https://home.treasury.gov/resource-center/data-chart-center/interest-rates/ (opened 2026-10-14)
- Yahoo chart API, ^TNX, ^GSPC, NKE daily 2021-10-01 to 2026-10-13 (opened)
- Damodaran, Implied ERP Oct 1 2026, https://pages.stern.nyu.edu/~adamodar/New_Home_Page/home.htm (opened); industry betas Jan 2026, https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html (opened)
- Kroll Cost of Capital Updates, Jan 2026 executive summary PDF, https://edge.sitecorecloud.io/krollllc17bf0-kroll6fee-proda464-0e9b/media/Cost-of-Capital/kroll-cost-of-capital-updates-jan26-executive-summary.pdf (opened)
- Nike Q1 FY27 10-Q, https://www.sec.gov/Archives/edgar/data/320187/000032018726000193/nke-20260831.htm (opened: p.3 balance sheet, p.8 debt fair value, p.34 ratings)
- Nike FY26 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm (opened: p.30 EBIT and ROIC, Note 6 debt)
- Repo: data/valuation/reverse_dcf.csv and research_notes/thesis_tests/consensus_and_valuation.md on origin/claude/wonderful-franklin-u31n4e (opened)
