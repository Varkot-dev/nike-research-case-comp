# G12: Sales-related reserve release. Does it explain the guidance beats? Earnings-quality test

Prepared 2026-10-15. Extends `G2_receivables_reserves.md` (reserve vs receivables), `G9_guidance_record.md` (16 of 16 inside or above guided range) and `research_notes/15_why_nike_discounts.md` (reserve as a discount channel). Does not redo them. Data files in this folder: `G12_nike_reserve_series.csv`, `G12_whatif.csv`, `G12_beat_test.csv`, `G12_yoy_reserve_swing.csv`, `G12_peers_control.csv`, `G12_companion_reserves.csv`.

Tags: OPENED = read in the cited filing this session (all 37 Nike 10-K and 10-Q files FY2018 to Q1 FY2027 re-downloaded from the investors.nike.com mirror, never www.sec.gov, paged with `scripts/sec_pipeline/topages.py`; printed pages cited). DERIVED = my arithmetic on OPENED inputs. SNIPPET = XBRL tag value or search snippet, filing text not read. Every reserve balance and wholesale figure in the series was re-extracted by script from the fresh filings and matches `G2_nike_quarterly.csv` and `data/discount/sales_related_reserves.csv` with zero mismatches. **Everything labelled "what-if" is arithmetic about a counterfactual. It is not an accusation, and nothing here says any figure is misstated.**

## 1. Verdict

**Smoking gun for misstatement: NO. Material earnings-quality driver that a short should price: YES.**

1. **Size (hold-the-ratio what-if).** The reserve fell from 6.85% of trailing-twelve-month (TTM) wholesale revenue (May 2025) to 5.32% (Aug 2026). Had it stayed at 6.85%, Nike would have booked $429M less revenue over Q1 FY26 to Q1 FY27 ($70M, $75M, $107M, $82M, $95M). Gross margin effect (GM) per quarter: 17 to 30 bps (central) and 35 to 57 bps (upper bound). EBIT effect 4% to 12% of quarterly EBIT. EPS effect $0.026 to $0.041 per quarter central, $0.037 to $0.058 upper; cumulative $0.16 central and $0.23 upper over five quarters ($0.13 and $0.18 inside FY26's reported $2.10). Q1 FY27: 21 bps (central) to 49 bps (upper), EPS $0.034 to $0.050.
2. **Against the guidance beats (section 5).** Two lenses. (i) Hold the May 2025 ratio: the effect is 10% to 45% of the revenue gap to the guide midpoint and 26% to 61% (central) or 51% to 140% (upper) of the gross margin gap. Without it every quarter would still be inside the guided range, so "16 of 16 inside or above range" survives; the gross margin "beat" label would fall to "in range" in Q4 FY26 and Q1 FY27 (both bounds), Q1 FY26 and Q3 FY26 (upper bound only). (ii) Year-over-year (YoY) swing in the reserve movement, usage held equal: **$400M in Q2 FY26, $212M in Q3, $221M in Q4 = 125%, 90% and 106% of the revenue gap to the guide midpoint**. Lapping the FY25 reserve build ($552M, the revenue drag Nike took in FY25) is a first-order explanation of the FY26 revenue beats, on an arithmetic lens that assumes equal usage. Management says the same in words (section 5.3).
3. **Why this is not a smoking gun.** (a) The reserve is still 5.32% of TTM wholesale, above every quarter-end from FY19 to FY24 (range 3.28% to 4.94%, mean 4.12%); against that benchmark the reserve is $334M too high, not too low (section 3.2). (b) The fall is a reversal of a build Nike made in FY25 and discussed on its calls. (c) PwC's only critical audit matter in every 10-K FY20 to FY26 is income taxes; sales-related reserves is not a CAM (section 7). (d) Policy wording is essentially unchanged (section 8). (e) Peers show the same direction at Under Armour and adidas, the opposite at Puma and Deckers (section 6).
4. **What keeps it a flag.** Nike removed the only disclosures that separate "usage of earlier reserves" from "lower provision rate": the Schedule II returns rollforward (last in the FY24 10-K, p. 97), the dollar allowance for doubtful accounts (last in the FY25 10-K, p. 64), and NA receivables (G2). Management added a sentence that variances between actual and expected reserves "were not material to reported Revenues" (FY25 10-K p. 48; FY26 10-K p. 47) and the phrase "based on current marketplace needs" to the estimation policy. The release is also not constant: for Q2 to Q4 FY27 a flat reserve balance would remove $40M, $90M and $69M of prior-year release from the YoY comparison (section 9), roughly $200M of revenue, about $0.07 (central) to $0.10 (upper) of EPS (DERIVED).

## 2. Series: reserve as a percent of trailing wholesale and total revenue, Q1 FY19 to Q1 FY27

Definitions (DERIVED). Wholesale = NIKE Brand plus Converse "Sales to Wholesale Customers" from the revenue note (Q4 = fiscal year less nine months). TTM = sum of the last four quarters. TTM wholesale needs four quarters of NIKE Brand plus Converse wholesale; FY18 Converse wholesale by quarter is not disclosed (FY19 10-K p. 80 gives FY19 only), so Q1 to Q3 FY19 TTM wholesale is n/a. TTM total revenue for those quarters uses FY18 quarters from the FY19 10-Q prior-year columns. Reserve = "Sales-related reserves" line in the Accrued liabilities note (includes returns, post-invoice discounts and claims; DTC reserves are inside it, FY19 10-K p. 64 Note 1). The reserve is gross of the separate asset for the estimated cost of inventory for returns (Prepaid expenses and other current assets).

| Quarter end | Reserve $M | Quarter wholesale $M | TTM wholesale $M | Reserve % TTM wholesale | Reserve % TTM revenue | Reserve % quarter wholesale | Reserve source (printed page) |
|---|---|---|---|---|---|---|---|
| Q1 FY19 (2018-08-31) | 1,048 | 6,916 | n/a | n/a | 2.81 | 15.2 | 10-Q_2018-08-31 printed p. 9 |
| Q2 FY19 (2018-11-30) | 1,107 | 6,362 | n/a | n/a | 2.91 | 17.4 | 10-Q_2018-11-30 printed p. 11 |
| Q3 FY19 (2019-02-28) | 1,244 | 6,482 | n/a | n/a | 3.21 | 19.2 | 10-Q_2019-02-28 printed p. 11 |
| Q4 FY19 (2019-05-31) | 1,218 | 6,910 | 26,670 | 4.57 | 3.11 | 17.6 | 10-K_2019-05-31 printed p. 65 |
| Q1 FY20 (2019-08-31) | 1,157 | 7,209 | 26,963 | 4.29 | 2.9 | 16.0 | 10-Q_2019-08-31 printed p. 8 |
| Q2 FY20 (2019-11-30) | 1,256 | 6,864 | 27,465 | 4.57 | 3.08 | 18.3 | 10-Q_2019-11-30 printed p. 9 |
| Q3 FY20 (2020-02-29) | 1,361 | 6,641 | 27,624 | 4.93 | 3.3 | 20.5 | 10-Q_2020-02-29 printed p. 9 |
| Q4 FY20 (2020-05-31) | 1,178 | 3,596 | 24,310 | 4.85 | 3.15 | 32.8 | 10-K_2020-05-31 printed p. 70 |
| Q1 FY21 (2020-08-31) | 1,127 | 6,737 | 23,838 | 4.73 | 3.02 | 16.7 | 10-Q_2020-08-31 printed p. 7 |
| Q2 FY21 (2020-11-30) | 1,126 | 6,682 | 23,656 | 4.76 | 2.94 | 16.9 | 10-Q_2020-11-30 printed p. 8 |
| Q3 FY21 (2021-02-28) | 1,146 | 6,180 | 23,195 | 4.94 | 2.98 | 18.5 | 10-Q_2021-02-28 printed p. 8 |
| Q4 FY21 (2021-05-31) | 1,077 | 7,652 | 27,251 | 3.95 | 2.42 | 14.1 | 10-K_2021-05-31 printed p. 70 |
| Q1 FY22 (2021-08-31) | 1,029 | 7,312 | 27,826 | 3.7 | 2.23 | 14.1 | 10-Q_2021-08-31 printed p. 7 |
| Q2 FY22 (2021-11-30) | 903 | 6,422 | 27,566 | 3.28 | 1.95 | 14.1 | 10-Q_2021-11-30 printed p. 8 |
| Q3 FY22 (2022-02-28) | 898 | 6,031 | 27,417 | 3.28 | 1.92 | 14.9 | 10-Q_2022-02-28 printed p. 8 |
| Q4 FY22 (2022-05-31) | 1,015 | 7,135 | 26,900 | 3.77 | 2.17 | 14.2 | 10-K_2022-05-31 printed p. 68 |
| Q1 FY23 (2022-08-31) | 950 | 7,327 | 26,915 | 3.53 | 2.01 | 13.0 | 10-Q_2022-08-31 printed p. 7 |
| Q2 FY23 (2022-11-30) | 1,149 | 7,591 | 28,084 | 4.09 | 2.34 | 15.1 | 10-Q_2022-11-30 printed p. 8 |
| Q3 FY23 (2023-02-28) | 1,067 | 6,746 | 28,799 | 3.7 | 2.11 | 15.8 | 10-Q_2023-02-28 printed p. 8 |
| Q4 FY23 (2023-05-31) | 994 | 7,032 | 28,696 | 3.46 | 1.94 | 14.1 | 10-K_2023-05-31 printed p. 67 |
| Q1 FY24 (2023-08-31) | 1,003 | 7,312 | 28,681 | 3.5 | 1.95 | 13.7 | 10-Q_2023-08-31 printed p. 7 |
| Q2 FY24 (2023-11-30) | 1,130 | 7,375 | 28,465 | 3.97 | 2.19 | 15.3 | 10-Q_2023-11-30 printed p. 9 |
| Q3 FY24 (2024-02-29) | 1,227 | 6,845 | 28,564 | 4.3 | 2.38 | 17.9 | 10-Q_2024-02-29 printed p. 9 |
| Q4 FY24 (2024-05-31) | 1,282 | 7,324 | 28,856 | 4.44 | 2.5 | 17.5 | 10-K_2024-05-31 printed p. 69 |
| Q1 FY25 (2024-08-31) | 1,200 | 6,685 | 28,229 | 4.25 | 2.4 | 18.0 | 10-Q_2024-08-31 printed p. 7 |
| Q2 FY25 (2024-11-30) | 1,560 | 7,132 | 27,986 | 5.57 | 3.19 | 21.9 | 10-Q_2024-11-30 printed p. 8 |
| Q3 FY25 (2025-02-28) | 1,682 | 6,363 | 27,504 | 6.12 | 3.52 | 26.4 | 10-Q_2025-02-28 printed p. 8 |
| Q4 FY25 (2025-05-31) | 1,834 | 6,578 | 26,758 | 6.85 | 3.96 | 27.9 | 10-K_2025-05-31 printed p. 68 |
| Q1 FY26 (2025-08-31) | 1,788 | 7,034 | 27,107 | 6.6 | 3.85 | 25.4 | 10-Q_2025-08-31 printed p. 7 |
| Q2 FY26 (2025-11-30) | 1,748 | 7,642 | 27,617 | 6.33 | 3.76 | 22.9 | 10-Q_2025-11-30 printed p. 8 |
| Q3 FY26 (2026-02-28) | 1,658 | 6,608 | 27,862 | 5.95 | 3.56 | 25.1 | 10-Q_2026-02-28 printed p. 8 |
| Q4 FY26 (2026-05-31) | 1,589 | 6,774 | 28,058 | 5.66 | 3.42 | 23.5 | 10-K_2026-05-31 printed p. 67 |
| Q1 FY27 (2026-08-31) | 1,488 | 6,948 | 27,972 | 5.32 | 3.24 | 21.4 | 10-Q_2026-08-31 printed p. 7 |

Reading: the TTM wholesale ratio was 3.3% to 4.9% from Q4 FY19 to Q4 FY24 (mean 4.12% over those 21 quarter-ends; the total-revenue ratio averaged 2.56% over 24 quarter-ends, range 1.92% to 3.30%). It rose to 6.85% in May 2025 and is 5.32% in Aug 2026. Q4 FY20 quarter-based ratios are COVID-distorted (wholesale fell to $3,596M). Seasonal pattern: the ratio on quarterly wholesale peaks in Q3 (Feb) every year, so the what-ifs use TTM bases.

## 3. What-if arithmetic (all figures DERIVED; WHAT-IF, not an accusation)

Method, stated before computing. Reserve change flows through revenue: provision = change in balance + usage, and revenue = gross sales less provision. For a benchmark balance B*, the reported figure was higher than the counterfactual by S = (benchmark balance minus actual balance). Positive S means the actual reserve is below the benchmark and reported revenue is flattered relative to it. Negative S means the actual reserve is above the benchmark (reported revenue lower than the benchmark would give). Usage (credits and returns taken) is held at its actual level because it is not disclosed.

Flow-through to gross profit. The returns part of the reserve has an offsetting asset (estimated cost of inventory for expected returns) that is recorded as a reduction of Cost of sales ("The related estimated cost of inventory for product returns is recorded as a reduction to Cost of sales with an offsetting increase to Prepaid expenses and other current assets", FY25 10-K p. 62, FY26 10-K p. 62). So returns-driven revenue changes flow to gross profit only net of that cost. Discounts and claims flow 100%. Using year-end splits (returns reserve share of total; asset as a share of returns reserve), the central flow-through is 71.2% (FY25 split: 1,277/1,834 and 528/1,277), 67.8% (FY26 split: 1,099/1,589 and 511/1,099). **Upper** = 100% flow-through (all discounts and claims). **Central** = the blended figure. The quarterly split between returns and discounts is not disclosed, so the year-end split is an assumption.

Gross margin effect = actual GM minus counterfactual GM, with counterfactual GP and revenue each reduced by the effect (Q4 FY26 excludes the $986M IEEPA recovery from GP, as G9 does). EBIT effect = GP effect (SG&A unchanged; bad debt expense ignored). EPS effect = EBIT effect times (1 minus that quarter's effective tax rate: Q1 FY26 21.2%, Q2 20.7%, Q3 20.0%, Q4 19.6%, Q1 FY27 22.7%) divided by that quarter's diluted shares (1,479.0; 1,481.0; 1,481.6; 1,482.9; 1,484.2; Q4 FY26 shares from the Q4 FY26 release p. 2). Income statement lines: each quarter's 10-Q p. 1 (Q1 FY27 10-Q p. 1: revenues $11,213M, gross profit $4,798M, income before taxes $921M, tax $209M, diluted EPS $0.48).

### 3.1 Benchmark (c): hold the ratio at the May 2025 level (6.85% of TTM wholesale). This is an added scenario, labelled as such; it is the cleanest test of "the release since May 2025".

Quarterly flow, path-consistent (each quarter's effect is the change in the benchmark balance minus the change in the actual balance; cumulative effect equals $429M, the gap between the Aug 2026 actual balance of $1,488M and the $1,917M the ratio would imply, plus the base effect).

| Quarter | Ratio used % | Benchmark reserve $M | Actual reserve $M | Revenue effect $M | GP effect $M (central / upper) | GM effect bps (central / upper) | EBIT effect $M (central) and % of EBIT | EPS effect (central / upper) |
|---|---|---|---|---|---|---|---|---|
| Q1 FY26 | 6.854 | 1,858 | 1,788 | 70 | 50 / 70 | 17.4 / 34.7 | 50 (5.5%) | 0.026 / 0.037 |
| Q2 FY26 | 6.854 | 1,893 | 1,748 | 75 | 53 / 75 | 18.6 / 36.0 | 53 (5.4%) | 0.029 / 0.040 |
| Q3 FY26 | 6.854 | 1,910 | 1,658 | 107 | 76 / 107 | 29.7 / 57.2 | 76 (12.0%) | 0.041 / 0.058 |
| Q4 FY26 | 6.854 | 1,923 | 1,589 | 82 | 56 / 82 | 21.0 / 45.3 | 56 (4.2%) | 0.030 / 0.045 |
| Q1 FY27 | 6.854 | 1,917 | 1,488 | 95 | 64 / 95 | 21.4 / 48.9 | 64 (7.1%) | 0.034 / 0.050 |

Five-quarter totals: revenue $429M; gross profit and EBIT $300M (central) or $429M (upper); EPS $0.160 central, $0.229 upper. FY26 only (Q1 to Q4): revenue $334M, EBIT $235M (central) = 8.2% of FY26 EBIT excluding the $986M IEEPA recovery ($2,864M, DERIVED from the FY26 10-K p. 55 income statement), EPS $0.127 central. Q4 FY26 EBIT percentage is computed on EBIT that includes the IEEPA recovery, so it is understated. Same exercise on a total-revenue base (3.96% of TTM revenue) is in `G12_whatif.csv` (base = rev) and gives the same order of magnitude.

### 3.2 Benchmark (a): the prior-year same-quarter ratio, and (b): the FY19 to FY24 average (4.12% of TTM wholesale)

Presented as the stand-alone effect if the quarter had closed at the benchmark ratio with the actual opening balance. Stand-alone effects are not additive across quarters. Path-consistent versions are in `G12_whatif.csv` (view = flow).

**(a) Prior-year same-quarter ratio**

| Quarter | Ratio used % | Benchmark reserve $M | Actual reserve $M | Revenue effect $M | GP effect $M (central / upper) | GM effect bps (central / upper) | EBIT effect $M (central) and % of EBIT | EPS effect (central / upper) |
|---|---|---|---|---|---|---|---|---|
| Q1 FY26 | 4.251 | 1,152 | 1,788 | -636 | -453 / -636 | -149.4 / -297.5 | -453 (-50.1%) | -0.241 / -0.339 |
| Q2 FY26 | 5.574 | 1,539 | 1,748 | -209 | -148 / -209 | -50.5 / -98.1 | -148 (-15.0%) | -0.080 / -0.112 |
| Q3 FY26 | 6.115 | 1,704 | 1,658 | 46 | 33 / 46 | 12.7 / 24.4 | 33 (5.1%) | 0.018 / 0.025 |
| Q4 FY26 | 6.854 | 1,923 | 1,589 | 334 | 227 / 334 | 86.9 / 187.9 | 227 (17.2%) | 0.123 / 0.181 |
| Q1 FY27 | 6.596 | 1,845 | 1,488 | 357 | 242 / 357 | 82.4 / 188.2 | 242 (26.7%) | 0.126 / 0.186 |

Reading (a): in Q1 and Q2 FY26 the reserve was above the prior-year ratio (the FY25 build was still in progress a year earlier at 4.25% and 5.57%), so holding last year's ratio would have meant a lower reserve and more revenue, not less. The sign flips in Q3 FY26: Nike closed $46M below the prior-year ratio, then $334M (Q4) and $357M (Q1 FY27). On this lens the release becomes visible only from Q3 FY26. Q4 FY26 under (a): revenue $334M lower, GM 87 bps (central) to 188 bps (upper) lower, EPS $0.12 to $0.18 lower. These are large, but (a) assumes the FY25 peak ratio (6.85%, which includes clean-up reserves) should have persisted, which is the aggressive end of the test.

**(b) FY19 to FY24 average ratio**

| Quarter | Ratio used % | Benchmark reserve $M | Actual reserve $M | Revenue effect $M | GP effect $M (central / upper) | GM effect bps (central / upper) | EBIT effect $M (central) and % of EBIT | EPS effect (central / upper) |
|---|---|---|---|---|---|---|---|---|
| Q1 FY26 | 4.124 | 1,118 | 1,788 | -670 | -477 / -670 | -157.0 / -312.8 | -477 (-52.8%) | -0.254 / -0.357 |
| Q2 FY26 | 4.124 | 1,139 | 1,748 | -609 | -434 / -609 | -143.0 / -277.6 | -434 (-43.8%) | -0.232 / -0.326 |
| Q3 FY26 | 4.124 | 1,149 | 1,658 | -509 | -362 / -509 | -134.1 / -258.4 | -362 (-57.1%) | -0.196 / -0.275 |
| Q4 FY26 | 4.124 | 1,157 | 1,589 | -432 | -293 / -432 | -104.8 / -226.6 | -293 (-22.2%) | -0.159 / -0.234 |
| Q1 FY27 | 4.124 | 1,154 | 1,488 | -334 | -227 / -334 | -72.6 / -165.7 | -227 (-25.0%) | -0.118 / -0.174 |

Reading (b): the sign is negative in every quarter. At the pre-clean-up average Nike's reserve is $334M (Aug 2026) to $670M (Aug 2025) too high, so the average-ratio benchmark says the reserve still holds excess. Revenue at risk if Nike moved back to the old norm is upside, not downside: a further $334M release would add about $0.12 (central) to $0.17 (upper) of EPS (DERIVED: 334 x 0.678 x 0.773 / 1,484 and 334 x 0.773 / 1,484, at the Q1 FY27 tax rate and shares). That capacity matters for FY28: the earnings support from the reserve is not exhausted, but the YoY swing fades (section 9).

## 4. Companion items (earnings-quality series)

`G12_companion_reserves.csv` has the full table.

| Item | FY19 | FY20 | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 | Source |
|---|---|---|---|---|---|---|---|---|---|
| Allowance for uncollectible AR $M | 30 | 214 | 93 | 34 | 35 | 35 | 27 | not disclosed | FY19 10-K Note 1; FY20 p. 64; FY21 p. 65; FY22 p. 64; FY23 p. 63; FY24 p. 65; FY25 p. 64; FY26 10-K p. 63 drops the figure |
| As % of year-end AR (DERIVED) | 0.7 | 7.8 | 2.1 | 0.7 | 0.9 | 0.8 | 0.6 | n/a | `G2_nike_annual_reserves.csv` |
| Inventory reserve $M (lower of cost or net realizable value) | n/d | n/d | n/d | n/d | n/d | 155 | 233 | 213 | FY25 10-K p. 64; FY26 10-K p. 63 (earlier 10-Ks give no dollar figure) |
| As % of inventory (DERIVED; inventories $7,519M, $7,489M, $7,501M) | | | | | | 2.1 | 3.1 | 2.8 | FY24 10-K p. 59, FY25 p. 58, FY26 p. 57 |
| Returns reserve $M | 843 | 682 | 595 | 525 | 549 | 799 | 1,277 | 1,099 | Schedule II (FY19 p. 89 to FY24 p. 97); FY25 p. 83; FY26 p. 84 |
| Cost-of-inventory asset for returns $M | 410 | 313 | 269 | 194 | 226 | 331 | 528 | 511 | Note 1 / Note 14 of each 10-K |
| Asset as % of returns reserve (DERIVED) | 48.6 | 45.9 | 45.2 | 37.0 | 41.2 | 41.4 | 41.3 | 46.5 | |
| Returns provision charged $M, % of wholesale (DERIVED) | 2,209 (8.3%) | 2,263 (9.3%) | 2,617 (9.6%) | 2,573 (9.6%) | 3,344 (11.7%) | 3,583 (12.4%) | not disclosed | not disclosed | Schedule II as revised |
| Discounts and claims (reserve less returns) $M | 375 | 496 | 482 | 490 | 445 | 483 | 557 | 490 | DERIVED |

Observations (DERIVED unless noted).
- **The one allowance item that is disclosed fell**: the doubtful-accounts allowance went from $35M to $27M (FY25) and then the dollar figure was dropped (FY26 10-K p. 63). It was 0.57% of year-end AR; the FY20 COVID reserve of $214M was released to $93M and $34M. At the FY19 to FY24 ex-COVID level (0.7% to 0.9% of AR), the FY25 AR of $4,717M implies $33M to $42M against $27M reported, a $6M to $15M difference. Immaterial. For FY26 (AR ex-IEEPA $5,247M) the same range implies $37M to $47M, but the actual is undisclosed.
- **Inventory reserve**: $233M to $213M in FY26 (-$20M, -8.6%). Nike's bridge shows lower "other costs" from lower obsolescence reserves of +40 bps in Q2 FY26 and +60 bps in Q3 FY26 (Q2 FY26 10-Q p. 27; Q3 FY26 10-Q p. 30), i.e. about $50M and $68M of YoY gross profit (DERIVED: bps x revenue). But the balance fell only $20M for the year, so this is mostly lapping the FY25 charges (other costs -70, -90 and about -153 bps in Q2, Q3 and Q4 FY25, bridge in note 15), not a large reserve release. In Q1 FY27 the Greater China segment names "higher inventory obsolescence reserves" (Q1 FY27 10-Q p. 28). The Q3 FY26 gross margin beat of 70 bps vs the guide midpoint coincides with a named +60 bps from lower obsolescence; this lever is separate from, and not additive in the same way as, the sales-reserve what-if (one is a YoY bridge line, the other a held-ratio counterfactual).
- **Asset ratio**: the cost asset was 41.3% of the returns reserve at both May 2024 and May 2025, then 46.5% at May 2026. At the 41.3% ratio the FY26 asset would be $454M, not $511M; the extra $57M of asset supports gross profit (it is the other side of the returns reserve). It is also inside the FY19 to FY21 range (45% to 49%), so it is not anomalous. Cannot be separated from product mix toward higher-cost returns.
- **Schedule II history**: the rollforward columns were revised twice for management-identified, immaterial errors (FY21 10-K p. 99 note 3: charged to costs understated by $286M and $250M for FY20 and FY19 with offsetting write-offs; FY22 10-K p. 98 note 2: $46M and $36M for FY21 and FY20). Balances were unaffected. The schedule then disappeared after the FY24 10-K.
- **Tax-basis cross-check (SNIPPET, XBRL)**: deferred tax asset for "returns and allowances" fell from $205M (May 2025) to $175M (May 2026), -14.6%, matching the -13.9% fall in the returns reserve (1,277 to 1,099). It confirms the direction through an independent tax record, not the cause.

## 5. Do reserve releases explain the guidance beats?

Scoring uses G9's bands and midpoints. Revenue gap = actual revenue minus prior-year revenue x (1 + guide midpoint). GM gap = actual bps change minus guide midpoint.

### 5.1 Lens 1: hold the May 2025 ratio (section 3.1)

| Quarter | Revenue vs guide midpoint $M | Reserve effect (hold May 2025 ratio) $M | % of gap | Rev growth actual / counterfactual % | GM gap vs midpoint bps | GM effect bps central / upper | GM counterfactual bps central / upper | Status of GM vs range: actual / cf central / cf upper | EPS effect central / upper |
|---|---|---|---|---|---|---|---|---|---|
| Q2 FY25 | 171 | -371 | -216.9 | -7.72 / -4.95 (beat / beat) | 50.0 | -89.0 / -164.3 | -11 / 64 | beat / beat / beat | -0.152 / -0.204 |
| Q3 FY25 | 269 | -143 | -53.2 | -9.33 / -8.18 (beat / beat) | -5.0 | -41.1 / -73.5 | -289 / -256 | in range / beat / beat | -0.068 / -0.091 |
| Q4 FY25 | 382 | -185 | -48.5 | -11.97 / -10.5 (beat / beat) | 10.0 | -55.6 / -98.0 | -384 / -342 | in range / beat / beat | -0.062 / -0.083 |
| Q1 FY26 | 710 | 70 | 9.8 | 1.13 / 0.53 (beat / beat) | 67.5 | 17.4 / 34.7 | -337 / -355 | beat / beat / in range | 0.026 / 0.037 |
| Q2 FY26 | 320 | 75 | 23.4 | 0.59 / -0.02 (beat / beat) | 37.5 | 18.6 / 36.0 | -319 / -336 | in range / in range / in range | 0.029 / 0.040 |
| Q3 FY26 | 235 | 107 | 45.4 | 0.09 / -0.86 (beat / beat) | 70.0 | 29.7 / 57.2 | -160 / -187 | beat / beat / in range | 0.041 / 0.058 |
| Q4 FY26 | 208 | 82 | 39.6 | -1.13 / -1.87 (beat / beat) | 40.0 | 21.0 / 45.3 | -31 / -55 | beat / in range / in range | 0.030 / 0.045 |
| Q1 FY27 | -97 | 95 | n/a (revenue below midpoint) | -4.33 / -5.14 (in range / in range) | 35.0 | 21.4 / 48.9 | 39 / 11 | beat / in range / in range | 0.034 / 0.050 |

FY25 rows (Q2 to Q4 FY25) are shown for contrast: the benchmark there is the May 2024 ratio, the reserve was being built, and the effect is negative. **The FY25 beats happened while Nike was adding $552M to the reserve (a $552M drag on revenue), so reserve releases cannot explain them.** Under lens 1 the release explains 10% (Q1 FY26), 23%, 45%, 40% of the revenue gap in Q1 to Q4 FY26. Revenue stays at or above the guide range in every quarter without the release (Q1 FY27 was already below the midpoint). The gross margin gap to the midpoint is explained (central) 26% (Q1 FY26), 50% (Q2), 42% (Q3), 52% (Q4) and 61% (Q1 FY27); upper bound 51%, 96%, 82%, 113% and 140%. Without the release the reported gross margin beat would become "in range" in Q4 FY26 and Q1 FY27 on both bounds, and in Q1 FY26 and Q3 FY26 on the upper bound; Q2 FY26 was already in range. No quarter would drop below the guided range, so "inside or above range 16 of 16" holds either way.

### 5.2 Lens 2: YoY swing in the reserve movement (usage held equal; FY25 build lapped)

| Quarter | Reserve change this year $M | Same quarter last year $M | Swing $M | Swing as % of YoY wholesale change | Swing as % of revenue gap vs midpoint | GP effect central / upper $M | GM bps central / upper | EPS central / upper |
|---|---|---|---|---|---|---|---|---|
| Q2 FY25 | 360 | 127 | -233 | 96.0 | -136.0 | -173 / -233 | -56.6 / -104.4 | -0.095 / -0.128 |
| Q3 FY25 | 122 | 97 | -25 | 5.0 | -9.0 | -19 / -25 | -7.2 / -13.0 | -0.012 / -0.016 |
| Q4 FY25 | 152 | 55 | -97 | 13.0 | -25.0 | -72 / -97 | -29.4 / -51.8 | -0.032 / -0.044 |
| Q1 FY26 | -46 | -82 | -36 | -10.0 | -5.0 | -26 / -36 | -8.9 / -17.7 | -0.014 / -0.019 |
| Q2 FY26 | -40 | 360 | 400 | 78.0 | 125.0 | 285 / 400 | 101.8 / 197.6 | 0.152 / 0.214 |
| Q3 FY26 | -90 | 122 | 212 | 87.0 | 90.0 | 151 / 212 | 59.5 / 114.6 | 0.082 / 0.115 |
| Q4 FY26 | -69 | 152 | 221 | 113.0 | 106.0 | 150 / 221 | 56.9 / 123.0 | 0.081 / 0.120 |
| Q1 FY27 | -101 | -46 | 55 | -64.0 | n/a | 37 / 55 | 12.3 / 28.2 | 0.019 / 0.029 |

Reading: the FY26 revenue beats in Q2, Q3 and Q4 (+$320M, +$235M, +$208M vs midpoint) are matched in size by the reserve swing ($400M, $212M, $221M). FY26 total swing $797M = 1.7% of FY26 revenue; central gross profit effect $560M, EPS $0.30 (central) to $0.43 (upper), against reported FY26 EPS of $2.10 (14% to 20%). The caveats that matter: (i) Nike's guidance given on the prior call already embedded management's own plan for returns and discounts; the beat is the unexpected part, which public data cannot isolate; (ii) usage was not equal in the two years, because FY25's high provision partly consumed FY25 and FY26 returns of clean-up goods (the usage is exactly what the dropped Schedule II would show); (iii) this lens measures the swing in the net balance, not the swing in the provision rate. Both caveats move the number in unknown directions, so it is a bound-style arithmetic.

### 5.3 What management said (opinion, quoted verbatim, labelled as such)

- Q4 FY25 call (June 26, 2025) p. 24, then-CFO Matt Friend: "we started to move more aggressively with that through sales-related returns, through more discounts to our retail partners so that they could mark down that inventory and move it through, and as well as selling off-price product to our value partners. When we get into the second half of fiscal year '26, we expect to be in a clean marketplace".
- Q4 FY26 call (June 30, 2026) p. 24, Friend: "We didn't sell in up 10%. There was a meaningful amount of that revenue growth that was associated with lower returns or sales-related reserves and returns, lower discount and lower cancellations."
- Same call p. 23: "We're seeing lower sales-related reserves in North America, lower cancellations and lower discounts. And so that's been giving us confidence that margins are coming back."
- Same call p. 22: Q4 gross margin ex-tariff-refund was down 10 bps against a guide of down 25 to 75 bps and "the biggest driver was discount improvement".
Management therefore states in words the mechanism this note quantifies. The "meaningful amount" is not sized. For Q4 FY26 North America wholesale grew $260M reported (+9.8%, G2), against a Q4 reserve decline of $69M company-wide (net balance), so the balance movement can account for at most about one quarter of that growth even if all of it sat in North America, unless usage fell too (DERIVED).

### 5.4 Answer

Releases do **not** explain the size of the revenue beats on lens 1 (10% to 45%), and cannot explain the FY25 beats (reserve was building). They explain roughly 26% to 61% of the gross margin gap to midpoint (central) on lens 1 and about 90% to 125% of the Q2 to Q4 FY26 revenue gaps on lens 2. Q1 FY27 revenue was below the midpoint, so there was no revenue beat to explain; the reserve moved by $95M (lens 1) and the gross margin gap of 35 bps is 61% (central) to 140% (upper) explained. Q1 FY27 diluted EPS was $0.48; the release is $0.034 (central) to $0.050 (upper) on lens 1 and $0.019 to $0.029 on lens 2. Against the LSEG consensus of $0.43 (secondary, relayed in `expectations_gap.md` per G9 section 7, not independently verified), the upper bound could account for the whole $0.05 EPS beat; the central estimate for about two-thirds of it.

## 6. Control: peers' reserves (`G12_peers_control.csv`)

Definitions differ, so compare direction, not level. Ratios are reserve over TTM total revenue (DERIVED).

| Company | Reserve line | Latest vs prior-year ratio | Pre-2025 level | Read |
|---|---|---|---|---|
| Nike (USD) | Sales-related reserves | 3.24% (Aug 2026) vs 3.85% (Aug 2025), -0.61 pts; peak 3.96% (May 2025) | 2.56% mean FY19 to FY24 | Still above pre-2025 range |
| adidas (EUR) | Provision for returns and warranty, other provisions note (additions, usage, reversals disclosed) | 2.68% of net sales (Dec 2025) vs 2.92% (Dec 2024); 3.34%, 3.62%, 3.01% in 2021 to 2023 | 3.0% to 3.6% | Down 0.24 pt in 2025, and 0.9 pt from 2022. Marketing and sales accrual (discounts, rebates, commissions) flat at EUR 1,034M vs EUR 1,030M |
| Puma (EUR) | Liabilities from refund obligations | 4.14% (Dec 2025, restated continuing sales) vs 2.42% (Dec 2024); 2.75% (Dec 2023) | 2.4% to 2.8% | Up sharply; Puma reports channel takebacks. The 2025 denominator is restated, so level not strictly comparable |
| Under Armour | Customer refund liability (XBRL) | 2.22% (Jun 2026) vs 2.75% (Jun 2025), -0.52 pt; 2.54% Mar 2026 vs 2.83% | 2.63% mean 2023 to 2024 (range 2.32% to 3.20%) | Down in 3 straight quarters; revenue also falling (TTM $4.93B vs $5.12B) |
| Deckers | Contract-with-customer refund liability (XBRL) | 1.06% (Jun 2026) vs 0.95%; 1.46% Mar 2026 vs 1.27% | 1.42% mean 2023 to 2024 | Flat to up (growth company) |
| Skechers | Allowance tagged AllowanceForDoubtfulAccountsReceivableCurrent; believed to be the combined bad debt, returns and chargebacks allowance (composition not verified) | 0.80% (Jun 2025) vs 0.64% | 0.76% mean | Flat to up; last filing Jun 2025 (taken private) |
| VF | Bad-debt allowance only; no returns reserve is tagged or disclosed | 0.25% (Mar 2026) vs 0.34% | 0.24% to 0.28% | Not a returns control |

Interpretation: a falling reserve ratio while revenue is stable is not unique to Nike (Under Armour -0.52 pt, adidas -0.24 pt), but Nike's move (-1.28 pts of wholesale, from a peak 2.7 pts above its own norm) is the largest relative to its own history. adidas is the only peer that discloses additions, usage and reversals (2025: opening EUR 691M, additions 559, usage -478, reversals -48, FX -59, closing 664). That disclosure is what Nike's dropped Schedule II used to provide. adidas reversals were EUR 29M to 58M a year in 2022 to 2025, 5% to 9% of additions. Nike's equivalent is not published.

## 7. Auditor critical audit matters (PwC, auditor since 1974)

| 10-K | CAM(s) | Page |
|---|---|---|
| FY20 | Accounting for income taxes (only CAM) | p. 55 |
| FY21 | Accounting for income taxes | p. 56 |
| FY22 | Accounting for income taxes | p. 55 |
| FY23 | Accounting for income taxes | p. 54 |
| **FY24** | **Accounting for income taxes (only CAM)** | **p. 56** |
| **FY25** | **Accounting for income taxes (only CAM)** | **p. 55** |
| **FY26** | **Accounting for income taxes (only CAM)** | **p. 54** |

**Sales-related reserves is not a critical audit matter in any year.** Each report says "The critical audit matter communicated below" (singular). The FY19 10-K (first year of the PCAOB requirement for large accelerated filers is FY20) has none. The FY24 audit report refers to "the related notes and financial statement schedule" (p. 55); the FY25 10-K lists no schedule (Item 15, p. 91: "All financial statement schedules are omitted because they are not applicable or the required information is shown in the financial statements or notes thereto"), so from FY25 the audit opinion no longer covers a returns rollforward. The only reserve-related management statement in the FY25 and FY26 critical accounting policy sections is the non-material-variance sentence.

## 8. Policy wording FY19 to FY26 (word-level diffs, OPENED)

Three places: MD&A critical accounting policy "SALES-RELATED RESERVES" (FY19 p. 41, FY20 p. 47, FY21 p. 48, FY22 p. 47, FY23 p. 47, FY24 p. 49, FY25 p. 48, FY26 p. 47), Note 1 "SALES-RELATED RESERVES" (FY19 p. 57 to FY26 p. 62), and Note 1 "REVENUE RECOGNITION".

| Change | First appears | Substance |
|---|---|---|
| ASC 606 adoption: reserve balances previously reported net of inventory cost and inside accounts receivable (wholesale); now gross in Accrued liabilities, with a separate asset | FY19 10-K Note 1 p. 57, Note 16 p. 80 | Presentation. May 2018 balance was $675M net (Note 16) |
| Sentence on pre-FY19 presentation deleted | FY21 10-K | Housekeeping |
| Future-tense to present-tense ("would be recorded" became "is recorded"; "net revenues" to "Revenues") | FY21 Note 1; FY26 critical policy | Editorial |
| MD&A policy rewritten from "provision for ... consists" to "Provisions ... consist"; cross-reference text and inventory reserve text moved | FY23 10-K p. 47 | Editorial |
| "miscellaneous claims" became "claims" | FY25 10-K Note 1 p. 62 and Revenue Recognition | Narrowing of wording; no disclosure of what changed |
| New: "The related estimated cost of inventory for product returns is recorded as a reduction to Cost of sales with an offsetting increase to Prepaid expenses and other current assets" | FY25 10-K Note 1 p. 62 | Clarifies the cost side (used in section 3) |
| New in estimate (3): "not yet finalized with customers **based on current marketplace needs**" | FY25 10-K p. 48 | Ties reserve to marketplace conditions; wider management judgment on timing |
| New sentence: "For fiscal 2025, any variances between actual and expected sales-related reserves were not material to reported Revenues" (FY26: "In fiscal 2026 ...") | FY25 10-K p. 48; FY26 10-K p. 47 | New assertion; absent in FY19 to FY24 |
| Wholesale payment terms: "which may be governed by the country of sale" added; "country of sale or" deleted from control language | FY25 Revenue Recognition | Terms (see G2) |
| Allowance for uncollectible AR: dollar figure and the "non-current if more than 12 months" sentence dropped | FY26 10-K p. 63 | Disclosure removed |
| Schedule II omitted | FY25 10-K Item 15 p. 91 | Disclosure removed |
| Significant-estimates list changed from "revenue recognition" (FY19 to FY23) to "sales-related reserves" | FY24 10-K p. 23 | Emphasis |

Return rights wording ("contractual return rights and discretionary authorized returns", "contractual programs and discretionary discounts") is unchanged from FY19 to FY26.

## 9. Forward implication (arithmetic, not a forecast)

Reserve movements are a one-time YoY comparison item. If the balance is flat in Q2 to Q4 FY27, the YoY comparison loses the prior-year declines: Q2 -$40M, Q3 -$90M, Q4 -$69M (total -$199M; central gross profit about -$135M, EPS about -$0.07; upper -$0.10). If instead Nike continues to release toward the FY19 to FY24 average (a further $334M available at 4.12% of TTM wholesale, DERIVED), revenue and EPS are supported by up to about $0.12 (central) to $0.17 (upper) in total. Q2 FY27 also carries Nike's own warning of a "multi-point headwind" from timing (G9 section 8). The short therefore should not rely on the reserve reversing; it is a swing item with a $0.07 to $0.10 negative YoY risk to FY27 if the balance simply stabilizes, and the filings do not let anyone tell which way management intends to go.

## 10. Alternatives ruled out (data, not common sense)

| # | Alternative explanation for the fall in the reserve ratio | Verdict | Evidence |
|---|---|---|---|
| 1 | **Lower wholesale mix** | Ruled out | Wholesale share of TTM revenue rose: 56.4% (May 2024), 57.9% (May 2025), 60.7% (May 2026), 61.1% (Aug 2026). TTM wholesale grew $1,214M (+4.5%) from May 2025 to Aug 2026 while the reserve fell $346M (-18.9%). The ratio to total revenue also fell (3.96% to 3.24%). |
| 2 | **Fewer returns because of lower Direct** | Partial at most; cannot exceed 46% | Direct revenue TTM fell $1,699M (-8.7%) May 2025 to Aug 2026 (revenue-note DTC rows). Even if the entire $1,834M reserve scaled with Direct, the mix effect is -$160M of the -$346M fall (46%), and that assumes no reserve on wholesale. A regression of the reserve on TTM wholesale and Direct, Q4 FY19 to Q4 FY24 (21 points), has R-squared 0.07 and a negative Direct coefficient, so no stable per-channel rate can be fitted; the channel split of the reserve is undisclosed. Wholesale growth works the other way (+4.5% x $1,834M x wholesale share). |
| 3 | **Shorter return windows** | Survives, untested | Policy wording on return rights is unchanged FY19 to FY26 (section 8); no 10-K or 10-Q mentions a change in return terms. Wholesale return rights are contractual and not disclosed. The nike.com returns page is rendered by script and returned no readable text; Wayback fetches were reset or rate-limited (429). |
| 4 | **Faster claim settlement (credit memos)** | Contradicted for credit-memo settlement; cash settlement untested | Credits settle against gross receivables, so receivables would fall with the reserve. Instead trade AR ex-IEEPA rose from $4,717M to $5,247M (May 2025 to May 2026) and net-of-reserve DSO rose 9.2 days (G2). Cash settlement would appear in operating cash flows inside accrued liabilities; Nike does not split it. |
| 5 | **Genuine fall in markdown support** | Partly survives, with management support in North America | Discounts and claims portion fell from $557M to $490M (-12%), less than the returns portion (-14%). Nike's bridge still says ASP is lower from "higher discounts and channel mix" in Q1 FY27 (10-Q p. 23, ASP -30 bps) and NA "partially offset by higher discounts" (p. 26); management says discounts were lower in NA in Q4 (call p. 22 to 24). Cannot be tested without markdown dollars. |
| 6 | **FX** | Ruled out | A weaker dollar raises the dollar value of non-US reserves, so FX works against the observed decline. Non-North America wholesale was about 57% of FY26 wholesale (NA $11,958M of $28,058M, G2/revenue note). At a roughly 3.5% average appreciation that is about +$37M, so the constant-currency fall is about $37M larger than reported (DERIVED, rough). |
| 7 | **Usage of FY25 clean-up reserves** (benign: provision rate unchanged, balance consumed) | Survives | The FY25 build was explicitly clean-up of aged inventory "through sales-related returns" (Q4 FY25 call p. 24; Q4 FY25 call p. 9: "higher sales-related returns"). If those returns arrived in FY26, the balance falls with no change in the provision rate. The only data that separates this from lower provisioning is the usage column, withdrawn in FY25. |
| 8 | **Lower provision rate on current shipments** | Survives | Management attributes part of NA wholesale growth to "lower returns or sales-related reserves" (Q4 FY26 call p. 24). The reserve ratio has fallen below the prior-year level only since Q3 FY26 (section 3.2 rule (a)). |
| 9 | **Reserve-driven timing of receipts (AR/IEEPA)** | Ruled out | The $684M IEEPA receivable is in AR, not the reserve (FY26 10-K p. 30, 61); excluded in all adjusted figures. |

Surviving after tests: 5 (partly), 7 and 8. They cannot be separated from public data. What would decide: (i) the returns reserve rollforward (additions, usage, reversals) for FY25 to FY27, the Schedule II information Nike used to provide through FY24 and that adidas still provides; (ii) the split of the reserve by channel and region; (iii) quarterly dollars of returns credited; (iv) NA receivables by quarter; (v) Circana sell-through by franchise against shipments. Requests that can be made: ask on the Q2 FY27 call (about Dec 17, 2026) or at the Nov 16 to 17 Investor Day for the FY26 and H1 FY27 returns provision and usage, in dollars.

## 11. Routes tried (per repo rule; at least five different routes for the usage-versus-rate question)

| # | Route | Result |
|---|---|---|
| 1 | Nike 10-K and 10-Q text, Schedule II and Note 14 | PARTIAL. Rollforward through FY24 (p. 97); balances only after |
| 2 | SEC XBRL companyfacts for Nike (tags ValuationAllowancesAndReserves*, ContractWithCustomerRefundLiability, DeferredTax...ReturnsAndAllowances) | PARTIAL. Schedule II tags last used FY12; refund liability annual only (FY24 to FY26); tax-basis asset $205M to $175M |
| 3 | Cost-of-inventory-for-returns asset ratio | WORKED, not discriminating (41.3% to 46.5%) |
| 4 | Earnings-call transcripts (25 calls) for reserve, returns, markdown allowance | WORKED. Q4 FY25 and Q4 FY26 statements quoted in 5.3; nothing in Q1 FY27 (Denton) |
| 5 | Receivables and cash-flow cross-checks (G2) | WORKED. Contradicts settlement via credit memos; cannot size usage |
| 6 | Peer disclosure benchmark (adidas rollforward, Puma, UA, Deckers, Skechers, VF) | WORKED for direction; only adidas discloses usage |
| 7 | Regression of reserve on channel revenue | WORKED, uninformative (R-squared 0.07) |
| 8 | Wayback and nike.com return policy | BLOCKED (connection reset, HTTP 429, script-rendered page) |
| 9 | Peer filing text on www.sec.gov | BLOCKED (HTTP 403, requires a declared contact; none supplied by design). Replaced by data.sec.gov XBRL and company annual reports |
| 10 | Skechers and VF returns reserve text via IR sites | BLOCKED or empty (Skechers redirect, VF IR connect failed). VF returns reserve is not tagged |

Verdict: the cause of the decline (usage versus lower provision rate versus lower markdown support) remains open after 7 working or partial routes. Data that would decide it is listed in section 10.

## 12. What I could not verify

- The returns reserve and discounts split by quarter (only year-end values), so the quarterly flow-through to gross profit (71.2% and 67.8%) is an assumption; the upper bound (100%) brackets it.
- Usage (credits and returns taken) and the provision rate after FY24.
- Whether Nike's guidance embedded the release (public data cannot show the plan).
- Peer definitions: Skechers allowance composition and VF returns; Under Armour and Deckers series from XBRL tag values only (SNIPPET), filing text not read; Puma 2025 denominator restated.
- FY18 quarterly Converse wholesale (TTM wholesale for Q1 to Q3 FY19).
- Q4 FY26 EBIT percentage effect is on EBIT including the IEEPA recovery.
- LSEG consensus ($0.43) is secondary.

## 13. Sources

Nike 10-K FY2018 to FY2026 and 10-Q Q1 FY2018 to Q1 FY2027 from https://investors.nike.com/sec-filings/all-sec-filings/content/<accession>/<file> (accessions from data.sec.gov submissions CIK 0000320187; e.g. 0000320187-26-000193 nke-20260831.htm, 0000320187-26-000088 nke-20260531.htm). Q4 FY26 release 0000320187-26-000076 q4fy26exhibit991er.htm. Nike earnings call transcripts: `data/hunt/earnings_calls/transcripts/` (investors.nike.com asset store PDFs). SEC XBRL companyfacts (data.sec.gov) for CIK 320187, 1336917, 910521, 1065837, 103379. adidas Annual Reports 2022 to 2025 notes pages at report.adidas-group.com. Puma Annual Reports 2024 and 2025 consolidated financial statements PDFs at annual-report.puma.com. Scripts and intermediates were kept in the session scratchpad, not the repo.
