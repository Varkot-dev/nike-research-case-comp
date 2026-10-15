# G12 check: adversarial review of the sales-related reserve release claim

Prepared 2026-10-15 by the skeptic agent. Target: `G12_reserve_release.md` and its CSVs. Tags: OPENED = read in the cited document this session; SNIPPET = search or tool snippet only; DERIVED = my arithmetic on OPENED inputs. Filings were re-downloaded for this check into a fresh scratch folder from the investors.nike.com mirror (never www.sec.gov; no email or contact header sent), all 34 10-K and 10-Q files from the FY2018 10-K to the Q1 FY2027 10-Q, paged with `scripts/sec_pipeline/topages.py`. Printed pages are cited. Transcript pages are the "=== PAGE n ===" markers in `data/hunt/earnings_calls/transcripts/`.

## 1. Verdict in one table

| G12 claim | Status | Why |
|---|---|---|
| Reserve balances ($1,834M May 2025 to $1,488M Aug 2026, all 29 quarter-ends) | SURVIVES | Re-extracted from the filings, zero mismatches (section 2) |
| Wholesale revenue by quarter, TTM wholesale, reserve % of TTM wholesale (6.85% to 5.32%), FY19-FY24 mean 4.12% | SURVIVES | Re-derived, zero mismatches against `G12_nike_reserve_series.csv` (section 2) |
| EPS arithmetic (tax rate, share count, 71.2% / 67.8% flow-through) | SURVIVES with a caveat | Reproduces to the cent; flow-through is validated on annual data for the YoY swing but is 93% for FY26 alone (section 7) |
| "Swing equals 90% to 125% of the Q2 to Q4 FY26 revenue gaps to guide midpoint" | WRONG as stated (category error and fragile input) | Compares a YoY change in a net balance with a surprise against guidance; guidance already embedded the lapping; the ratio ranges from 46% to over 500% depending on how "low single digits" is read; across 8 quarters beat and swing have correlation -0.08 (sections 3, 5, 6) |
| "$0.30 to $0.43 of FY26 EPS" | NEEDS A CAVEAT (not a beat explanation) | It is an upper-bound arithmetic of lapping a charge Nike took in FY25, assuming equal usage; the share of the FY25 "drag" that was excess is unknowable (section 4) |
| "FY25 build was a $552M revenue drag" | WRONG wording | $552M is a net balance change (provision minus usage), not a revenue drag (section 4) |
| "CFO Friend confirmed the mechanism on the Q4 FY26 call" | OVERSTATED | Quote is about North America wholesale, Q4 only, a YoY growth composition, unsized, lists four items (returns or reserves, discount, cancellations), and is not about the guide (section 8) |
| "Reserve is still too high versus FY19-FY24 norm" | NEEDS A CAVEAT | True on a wholesale-ratio basis; on a usage-turnover basis it depends on the unobservable usage rate (section 5) |
| Forward claim: flat FY27 reserve removes $0.07 to $0.10 | SURVIVES as arithmetic only, WRONG as a forecast baseline | Math reproduces ($0.068 to $0.104); "flat" is not a neutral baseline and Q1 FY27 already contradicted a reserve-drives-revenue story (section 9) |
| "Not a smoking gun for misstatement" | SURVIVES, and is stronger than G12 states | See section 10 |

## 2. Task 1: re-derivation from filings (all OPENED)

Reserve line "Sales-related reserves" in the Accrued liabilities note (Note 3 in the 10-K, the Accrued liabilities note in each 10-Q); wholesale = "Sales to Wholesale Customers", total NIKE, Inc. column, in the revenue note; Q4 = fiscal year less the 9-month figure in the Q3 10-Q (the note shows quarter figures for Q1 to Q3 and annual in the 10-K). TTM = last four quarters.

| Quarter end | Reserve $M (printed page) | Quarter wholesale $M (printed page of note) | TTM wholesale $M | Reserve % TTM wholesale |
|---|---|---|---|---|
| May 2024 | 1,282 (FY24 10-K p. 69) | 7,324 (FY24 10-K p. 84, annual 28,856) | 28,856 | 4.44 |
| Aug 2024 | 1,200 (Q1 FY25 10-Q p. 7) | 6,685 (p. 15) | 28,229 | 4.25 |
| Nov 2024 | 1,560 (p. 8) | 7,132 (p. 17) | 27,986 | 5.57 |
| Feb 2025 | 1,682 (p. 8) | 6,363 (p. 18) | 27,504 | 6.12 |
| May 2025 | 1,834 (FY25 10-K p. 68) | 6,578 (annual 26,758, FY25 10-K p. 82) | 26,758 | 6.85 |
| Aug 2025 | 1,788 (p. 7) | 7,034 (p. 15) | 27,107 | 6.60 |
| Nov 2025 | 1,748 (p. 8) | 7,642 (p. 17) | 27,617 | 6.33 |
| Feb 2026 | 1,658 (p. 8) | 6,608 (p. 18) | 27,862 | 5.95 |
| May 2026 | 1,589 (FY26 10-K p. 67) | 6,774 (annual 28,058, FY26 10-K p. 83) | 28,058 | 5.66 |
| Aug 2026 | 1,488 (Q1 FY27 10-Q p. 7) | 6,948 (p. 14) | 27,972 | 5.32 |

FY19 Q4 to FY24 Q4 (21 quarter-ends): mean 4.124%, min 3.28%, max 4.94% (DERIVED, matches G12). Whole series compared programmatically to `G12_nike_reserve_series.csv`: 0 mismatches. Other inputs re-opened: Q1 FY26 to Q1 FY27 income statements (10-Q p. 1 each: effective tax 21.2%, 20.7%, 20.0%, Q4 19.6% from FY26 10-K less 9M, Q1 FY27 22.7%; diluted shares 1,479.0, 1,481.0, 1,481.6, 1,484.2; Q4 about 1,482.4 from 4 x 1,481.0 less the three quarters, vs G12's 1,482.9 from the release); AR $5,931M May 2026 vs $4,717M May 2025 (FY26 10-K p. 57), of which $684M is IEEPA receivable (FY26 10-K p. 30 and p. 61); returns reserve $1,277M and $1,099M and cost-of-inventory asset $528M and $511M (FY25 10-K p. 83, FY26 10-K p. 84).

## 3. Task 2: provision versus usage, and does the swing double count?

### 3.1 What the filings let you say (OPENED)

- Revenue recognition note (FY26 10-K p. 62): the company "estimates the most likely amount it will be entitled to receive and records an anticipated reduction against Revenues, with an offsetting increase to Accrued liabilities at the time revenues are recognized." The estimated cost of inventory for returns goes "as a reduction to Cost of sales with an offsetting increase to Prepaid expenses and other current assets." So only the provision touches revenue. Credits and returns actually taken (usage) reduce the liability and gross receivables (or cash) and do not touch revenue.
- Identity: change in balance = provision - usage. G12's lens 2 defines swing = (change last year) - (change this year) = (P last - P this) + (U this - U last). Only the first bracket is revenue. G12 assumes the second bracket is zero. Every dollar by which FY26 usage exceeds FY25 usage is counted as revenue benefit by G12 when it is not. This is the single-count version of the error. There is no double counting inside lens 2 itself, but the headline stacks three overlapping presentations of the same balance fall (lens 1, lens 2, Friend quote) as if corroborating; they are one number measured three ways.
- Cash flow statement (FY26 10-K p. 58): the only line is "Increase (decrease) in accounts payable, accrued liabilities, operating lease liabilities and other current and non-current liabilities" (-959 FY26, -426 FY25, +397 FY24). Reserve usage is buried inside it; it cannot be isolated. AR line (-1,207 FY26) includes the $684M IEEPA receivable.
- Last disclosure of provision and usage: Schedule II, sales returns reserve only (returns, not discounts or claims), through FY24 (FY24 10-K p. 97). Dropped from the FY25 10-K. Rows (balance start / charged / other / write-offs / end; $M): FY22 595 / 2,573 / -31 / -2,612 / 525; FY23 525 / 3,344 / -11 / -3,309 / 549; FY24 549 / 3,583 / -8 / -3,325 / 799 (FY24 10-K p. 97). FY19 to FY21 are as revised in FY21 10-K p. 99 and FY22 10-K p. 98. Note the FY19 to FY21 provision was revised up three times (FY19 1,959 to 2,209; FY20 1,941 to 2,227 to 2,263; FY21 2,571 to 2,617), so even this schedule has needed correcting.

### 3.2 Scale of usage versus the balance move (DERIVED from Schedule II and the revenue note)

| Year | Provision % of wholesale | Usage % of wholesale | Change in returns balance $M | Change as % of wholesale | Balance in days of usage |
|---|---|---|---|---|---|
| FY20 | 9.3 | 9.8 | -161 | -0.66 | 104 |
| FY21 | 9.6 | 10.1 | -87 | -0.32 | 79 |
| FY22 | 9.6 | 9.7 | -70 | -0.26 | 73 |
| FY23 | 11.7 | 11.5 | +24 | +0.08 | 61 |
| FY24 | 12.4 | 11.5 | +250 | +0.87 | 88 |
| FY25 (no schedule) | n/d | n/d | +478 | +1.79 | n/d |
| FY26 (no schedule) | n/d | n/d | -178 | -0.63 | n/d |

(FY19 is excluded from the days column: it straddles the ASC 606 transition.) Reading: usage runs about $2.4B to $3.3B a year, so the balance is only 60 to 105 days of usage. A $40M to $90M quarterly balance move is 5% to 11% of a quarter's usage (about $830M). A one-point swing in the usage rate on FY26 wholesale ($28.1B) is $281M, larger than the entire FY26 total reserve fall ($245M). The usage rate itself moved by 1.8 points between FY22 and FY23. So the balance change cannot identify the provision change.

Two bounding cases for FY26 returns (DERIVED, assumptions stated):
- Case A, usage rate held at the FY24 level (11.52% of wholesale): FY26 usage 3,233, provision 3,055 = 10.9% of wholesale; FY25 provision 3,561 = 13.3%. This reproduces G12's lens 2 (a 2.4 point lower provision rate, about $670M on returns).
- Case B, provision rate unchanged at 13.3%: FY26 provision 3,732, usage 3,910 = 13.9% of wholesale, 2.4 points above the highest usage rate on record in Schedule II (11.5%), but FY25's 13.3% provision is itself above the 12.4% record, and the FY25 build was explicitly aged inventory expected to come back (Q4 FY25 call p. 24; Q2 FY26 call p. 10 to 11, Greater China "accelerated returns of aged inventory owned by partners"). In case B the whole fall is usage and there is no FY26 revenue effect from the reserve beyond lapping.
The filings cannot choose between A, B and anything between.

### 3.3 Peer demonstration that usage dominates balances (OPENED: adidas Annual Report other-provisions notes 2022 to 2025, report.adidas-group.com)

adidas "Returns and warranty" (EUR M): 2022 additions 772, usage -607, closing 815; 2023 additions 563, usage -656, reversals -29, FX -49, closing 646; 2024 additions 622, usage -546, closing 691; 2025 additions 559, usage -478, reversals -48, FX -59, closing 664. Additions % of net sales: 3.43, 2.63, 2.63, 2.25; usage % of net sales 2.70, 3.06, 2.31, 1.93 (net sales 22,511; 21,427; 23,683; 24,811, taken from G12's peer file). Two lessons: (i) the 2025 balance fall of EUR 27M is more than explained by FX (-59); ex-FX the balance rose, so adidas is not a clean "reserve fell" peer; (ii) in 2023, after a high-provision 2022, usage rose to 3.06% of sales while additions fell, a mix of both effects, exactly the identification problem. Puma (OPENED, annual-report.puma.com consolidated statements PDFs): refund obligations EUR 236.9M (2023), 213.5M (2024), 302.1M (2025, restated continuing-operations denominator), i.e. a build in 2025, a year after Nike's build. The industry-wide pattern is a build and unwind cycle with differing timing, not something unique to Nike.

## 4. Is the "$0.30 to $0.43" a measure of the release or of lapping?

FY25 EPS (2.16) already absorbed the FY25 provision. FY26 laps it. The swing is therefore a year-over-year base effect, not a flattering release against a normal level. Cumulative position (DERIVED): relative to the May 2024 ratio (4.44%), the reserve excess is $645M at May 2025, $342M at May 2026 and $245M at Aug 2026. FY26 and Q1 FY27 revenue are still net of more reserve than the May 2024 norm. So "FY26 results were flattered by a release" has the sign wrong relative to a pre-build baseline; they were less depressed than FY25.

The size of the FY25 "drag" is also unknowable. Using FY24 flow rates (provision 12.4%, usage 11.5% of wholesale), FY25 would have built about $241M on returns alone with no extra provisioning, so only about $237M of the $478M returns build is excess, plus up to $74M on discounts and claims. On a constant-ratio basis (4.44%) the drag is $645M. So the FY25 drag ranges from roughly $300M to $645M, not $552M, and the YoY swing ($797M) inherits that range. G12 section 1 point 2 calls $552M "the revenue drag Nike took in FY25": that is wrong, it is a net balance change.

FY26 EPS $2.10 includes the $986M IEEPA recovery in cost of sales (FY26 10-K p. 30). Ex-IEEPA EPS is about $1.57 (DERIVED: 986 x (1 - 0.20) / 1,481, tax rate assumed). The $0.30 to $0.43 is 14% to 20% of reported but 19% to 27% of ex-IEEPA EPS; the note should say which base.

## 5. Task 3: was FY25 the anomaly, and is the fall just normalization?

Evidence for normalization (OPENED/DERIVED):
- Ratio history. Quarter-end ratio on TTM wholesale: 3.28% to 4.94% over FY19 to FY24, then 6.85% (May 2025). Same-quarter (August) ratios: 4.29, 4.73, 3.70, 3.53, 3.50, 4.25, 6.60, 5.32 (FY20 to FY27). By Aug 2026 59% to 64% of the rise from the pre-build level (4.25% Aug 2024 or 4.44% May 2024) to the peak has reversed (DERIVED).
- The decline is smooth: ratio steps of -0.25, -0.27, -0.38, -0.29, -0.34 points per quarter, excess over the 4.44% base of 2.41, 2.16, 1.89, 1.51, 1.22, 0.88 points. That shape fits a run-off of a stock of aged-inventory returns and credits, not discrete releases.
- Size of the FY26 draw: -0.63% of wholesale (returns), inside the historical range of annual moves (-0.66% in FY20). The FY25 build (+1.79%) is the outlier.
- Management said it in advance. Q4 FY25 call (June 26, 2025) p. 24, Friend: "we started to move more aggressively with that through sales-related returns, through more discounts to our retail partners ... When we get into the second half of fiscal year '26, we expect to be in a clean marketplace, a healthy marketplace. And so that business in the second half will be more full price, it will be more profitable, but there will be a revenue headwind from the compare to the higher level of off-price liquidation in the prior year." (opinion, labelled). Same call p. 9 and p. 10: "higher sales-related returns", "higher sales-related reserves" in North America and Greater China. Q1 FY26 call p. 16, Friend: "we do expect the benefit from less inventory clearance to start to take shape in our margins in the second half".
- Peers: build and unwind at adidas (2022 build, 2023 unwind) and Puma (2025 build).

Evidence against complete normalization:
- Ratio of 5.32% is still 1.2 points above the FY19 to FY24 mean 4.12%, which is $334M by G12's arithmetic.

Caveat on that benchmark: it assumes the right denominator is wholesale revenue and that usage turnover is unchanged. At May 2026 the returns balance is 124 days of usage if usage is 11.5% of wholesale (above every year 61 to 104 days), but only about 103 days if usage were 13.9% (case B), inside history. The "still too high" claim therefore depends on the unobservable usage rate. The provision rate in Schedule II also trended up for six years (8.3% to 12.4% of wholesale), so FY19 to FY24 is not a stationary norm. Verdict: the normalization alternative survives and is the better default; it explains why analysts expected the direction.

Alternatives ruled in or out for the Q2 to Q4 FY26 beats (each tested against data):
1. Lower provision rate on current shipments (G12). Survives, unsized.
2. Higher usage of FY25 clean-up reserves (no revenue effect). Survives (section 3.2).
3. Shipment timing and pull-forward in North America. Survives and is named by management: Q4 FY26 call p. 18, Friend: "we also had extraordinarily high wholesale growth in North America in Q2 last year, also related to some timing anomalies" (opinion). Q2 FY26 North America wholesale +$684M (+24%, 10-Q Q2 FY26 p. 30).
4. Value-channel liquidation: Q2 FY26 call p. 10: "the quarter certainly benefited from liquidation to value channels as we cleaned up the marketplace". Survives.
5. Units and distribution: Q2 FY26 10-Q p. 30 NA footwear units +14% with ASP -5 points ("channel mix, partially offset by product mix and strategic pricing"); NA wholesale +24% "primarily driven by the impacts of our marketplace management actions in both the current and prior year, expanded distribution ... as well as shipment growth to existing partners". Q3 FY26 10-Q p. 33: NA wholesale +11%, footwear units +4%, ASP +2 points from "product mix and strategic pricing". FY26 10-K p. 37: NA wholesale +14% "including expanded distribution, higher shipments to existing partners and fewer marketplace management actions". Filing language lists the reserve-related item last and unsized. Survives as a major driver; the ASP lines do not credit lower discounts for NA footwear.
6. FX: Q2 and Q3 guides already included +1 and +3 points of FX; ruled out as a source of the beat.
7. Conservative guiding habit: beat in 15 of 16 quarters in G9 regardless of reserve direction (below).
Surviving after tests: 1, 2, 3, 4, 5, 7. They cannot be separated with public data.

Decisive counter-evidence (DERIVED): revenue gap to midpoint in $M versus reserve swing in $M: Q2 FY25 171 / -233; Q3 FY25 269 / -25; Q4 FY25 382 / -97; Q1 FY26 710 / -36; Q2 FY26 320 / 400; Q3 FY26 235 / 212; Q4 FY26 208 / 221; Q1 FY27 -97 / 55. Correlation of beat with swing across the 8 quarters is -0.08 (-0.13 excluding Q1 FY27). The largest beat in the record (Q1 FY26, $710M) coincided with a swing of -$36M. Beats also occurred in the three FY25 quarters while the reserve was being built. G12 selects Q2 to Q4 FY26 and omits the contrary quarters from the 90% to 125% headline.

## 6. Task 4: did guidance already embed the lower reserve? (OPENED, transcripts)

- Timing. Q2 FY26 guide was given Sept 30, 2025 (one month into the quarter), Q3 guide Dec 18, 2025 (three weeks in), Q4 guide Mar 31, 2026 (one month in). Management set each guide with a month of known provisions and its own reserve plan.
- Q1 FY26 call (Sept 30, 2025) p. 11 to 12, Friend: "We have made steady progress on our plans for a healthy marketplace by the end of the first half. And so we expect to begin to see a modest headwind on revenue across both wholesale and NIKE Direct as we lap aggressive clearance activity in the prior year." This guided lapping as a revenue headwind (off-price liquidation) and, in the same call p. 16, a margin benefit from less clearance in H2.
- Q2 FY26 call (Dec 18, 2025) p. 11: Q3 revenue "down low single digits, with modest growth in North America as we see reduced liquidation activity versus prior quarters".
- Q3 FY26 call (Mar 31, 2026) p. 10: "Wholesale revenue growth was driven by new distribution and lapping marketplace management actions with existing partners in the prior year." Q4 guide p. 13: down 2% to 4%, "modest growth in North America despite lapping a value liquidation in the prior year". Actual North America wholesale +$260M (+9.8%), far above "modest".
- Q4 FY26 call (Jun 30, 2026) p. 11 to 12: Q1 FY27 revenue down low to mid single digits; Q2 FY27 "multi-point headwind" from EMEA digital promotion compare and North America wholesale timing.
- Analyst questions on reserves: none found in the five calls Q4 FY25 to Q1 FY27 beyond (a) Jay Sole, Q4 FY25 p. 23 to 24, asking about the H2 FY26 revenue headwind from lapping promotions, answered with the returns and discounts explanation; (b) Aneesha, Q4 FY26 p. 21 to 23, on margin drivers, answered with "lower sales-related reserves in North America"; (c) Ike Boruchow, Q4 FY26 p. 23 to 24, on quarterly shape of North America wholesale, answered with "meaningful amount of that revenue growth was associated with lower returns or sales-related reserves". No analyst asked about the dollar size of the reserve. Third-party commentary: two web searches (Barchart, GuruFocus, Bullfincher, Zacks hits) returned no reserve-specific commentary; the Barchart page fetched empty. Status: PARTIAL; consensus models are not public.
- Conclusion. The lapping and the cleaner H2 were public and explicit from June 2025. What was not public was the dollar size of the reserve effect. G12 section 12 admits public data cannot show whether guidance embedded the release, but section 5.4 and the headline still score the swing against the midpoint. A YoY swing in a flow cannot be a share of a surprise against a guide that already included that flow. Valid comparison would be the swing minus what management planned, which is unobservable.

Guide-reading sensitivity (DERIVED). Q2 and Q3 FY26 were guided "down low single digits", and G9 scores that as -3% to -1%, midpoint -2%. Swing as % of the gap by assumed midpoint: Q2 FY26: -4% 71%, -3% 90%, -2% 125% (G12), -1.5% 155%, -1% 204%. Q3 FY26: -4% 46%, -3% 61%, -2% 90% (G12), -1% 173%. Q4 FY26 was numerically guided (-2% to -4%, midpoint -3%): 106%. So only the Q4 figure is not an artifact of the qualitative reading, and the Q2 and Q3 "90% to 125%" is a point in a 46% to 204% range.

## 7. Task 6: EPS arithmetic

Reproduced (DERIVED): Q2 FY26 400 x 71.2% x (1 - 20.7%) / 1,481.0 = $0.1525; Q3 212 x 71.2% x 0.800 / 1,481.6 = $0.0815; Q4 221 x 67.8% x (1 - 19.6%) / 1,482.9 = $0.0813; Q1 FY26 -36 x 71.2% x 0.788 / 1,479.0 = -$0.0137; sum $0.302 central; upper (100% flow-through) $0.429. G12's numbers are arithmetically correct.

Checks:
- Tax rate: effective rates tie to the 10-Qs. Using the average rather than marginal rate is a modeling choice; negligible.
- Flow-through. G12 applies 71.2% and 67.8% from the asset-to-reserve ratio (asset $528M of returns reserve $1,277M; returns $1,277M of $1,834M). A direct annual check from balances (DERIVED): FY25 build: revenue -552, cost-of-inventory asset +197 (331 to 528), so gross profit -(478 - 197 + 74) = -355 (64%). FY26 release: revenue +245, asset -17 (528 to 511), gross profit +(178 - 17 + 67) = +228 (93%). FY26 over FY25 swing: revenue 797, gross profit 583 = 73%. So the central 71.2% is validated for the swing, and flow-through for FY26 alone is higher than G12's 67.8% (the extra asset retained supports profit). Quarterly splits of returns versus discounts are not disclosed, so quarterly central figures remain assumptions.
- Not netted: bad debt expense, any related demand creation or incentive accruals; immaterial.
- Q4 FY26 EBIT percentage in G12 3.1 is understated because EBIT includes the IEEPA recovery (G12 already says so).

## 8. Task 5: what exactly did Friend say, and is G12's allocation consistent?

Verbatim (OPENED, Q4 FY26 call June 30, 2026, p. 24, answering Ike Boruchow on North America wholesale, transcript line about 740): "I think when you look at Q4 and you look at the North America wholesale growth reported up 10% I just want to make the point that we didn't sell in up 10%. There was a meaningful amount of that revenue growth that was associated with lower returns or sales-related reserves and returns, lower discount and lower cancellations. And so it's a healthier business in North America that contributed to that growth in Q4." Also p. 22 to 23 (margin answer to Aneesha): "the biggest driver was discount improvement that we're seeing in North America. We're seeing lower sales-related reserves in North America, lower cancellations and lower discounts."

Findings:
1. Scope: North America wholesale, fourth quarter only. Nothing on Q2 or Q3, nothing on Nike total, nothing on the guide.
2. It is a growth-composition statement (YoY), consistent with lapping, not a statement that the reserve release caused a beat versus guidance.
3. It is a bundle of three or four items. Cancellations are not a reserve item. "Discounts" overlaps with post-invoice discounts that sit inside the reserve, so the bundle is not additive to the reserve either.
4. "Meaningful amount" is unsized. It is opinion, labelled, and per CLAUDE.md cannot be the explanation by itself.
5. G12 is internally inconsistent. Section 5.3 sizes the Q4 effect with the balance change (-$69M, "at most one quarter" of $260M), while section 5.2 sizes the same quarter with the swing ($221M, 85% of $260M if all in NA). The same quote cannot support both. Regional split of the reserve is undisclosed, and the FY25 build included Greater China ("higher sales-related reserves", Q4 FY25 call p. 10) where Q2 FY26 shows accelerated partner returns of aged inventory (usage), so the company-wide swing should not be assigned to NA.
6. Swing as % of NA wholesale YoY change if wholly in NA: Q2 400/684 = 58%, Q3 212/269 = 79%, Q4 221/260 = 85%, FY 797/1,474 = 54% (DERIVED). The Q2 NA surge is attributed by management to timing (section 5).
7. Q1 FY27 contradicts a pure lower-discount story: the reserve fell $101M (largest quarterly fall in the cycle) while the 10-Q reports higher discounts (Q1 FY27 10-Q p. 23: NIKE Brand ASP -30 bps "primarily due to higher discounts and channel mix"; p. 26 NA footwear ASP "channel mix and higher discounts"). A reserve fall with higher reported discounts points to usage (settlement of earlier accruals) as at least part of the fall. Revenue was also below the guide midpoint that quarter.

## 9. Task 7: forward claim (flat FY27 reserve removes $0.07 to $0.10)

Reproduced: Q2 to Q4 FY27 prior-year declines -40, -90, -69 = -199. EPS at 25% tax (Nike raised the FY27 rate guide to mid-20s on Oct 1, 2026 per G9) and 1,484.2M shares: central 199 x 0.678 x 0.75 / 1,484.2 = $0.068; upper $0.100. At the Q1 FY27 rate of 22.7%: $0.073 and $0.104. Rule of thumb: $0.035 (central) to $0.05 (upper) per $100M of YoY change in net reserve movement.

Problems:
- Not a baseline. A constant provision rate gives a balance that moves with wholesale (about 5.3% x change in TTM wholesale), and the seasonal pattern is rises into November and February in normal years (Aug to Nov changes: FY20 +99, FY21 -1, FY22 -126, FY23 +199, FY24 +127). "Flat" is just one scenario on a continuum; a normal seasonal build would make the YoY comparison worse, a continued glide at the FY26 pace better.
- It depends on the equal-usage assumption (section 3).
- Q1 FY27 already shows the link between balance and revenue is weak (swing +$55M, revenue below midpoint, higher reported discounts).
- Management already telegraphed Q2 FY27 as a multi-point headwind from timing (Q4 FY26 call p. 18), so the sell side is not blind to a tougher Q2 compare.
Verdict: arithmetic survives; as a forecast it must be written as a sensitivity ("each $100M change in the net reserve move is worth about $0.04 to $0.05"), not as "$0.07 to $0.10 of EPS tailwind removed".

## 10. Strongest honest claim, and the bull's answer

Strongest version a judge could not knock down: "Nike's sales-related reserve rose from $1,282M to $1,834M in FY25 (4.44% to 6.85% of TTM wholesale) and has fallen to $1,488M (5.32%) by August 2026 (FY25 and FY26 10-Ks pp. 68 and 67; Q1 FY27 10-Q p. 7). Because the reserve is a net balance, the filings cannot say how much of the fall is a lower provision (which lifts revenue) and how much is the usage of earlier reserves (which does not); Nike withdrew the returns rollforward after FY24, and a swing of only 1 point in the usage rate on $28B of wholesale ($281M) is larger than the whole FY26 balance fall ($245M). If usage was unchanged, lapping the FY25 build is worth $797M of FY26 revenue and about $0.30 to $0.43 of EPS year over year, and management has said lower returns, reserves and discounts contributed to North America wholesale growth in the March to May 2026 quarter. This is a year-over-year base effect that management pre-announced in June 2025, it does not explain guidance beats (correlation with the beat is -0.08 over eight quarters; the largest beat came with a negative swing), and the reserve remains $245M above its May 2024 ratio, so it is a fact for the earnings-quality discussion and the FY27 comparison, not evidence of a misstatement."

One sentence a bull would use: "Nike took a self-announced, self-described clean-up reserve in FY25, told the market in June 2025 that H2 FY26 would be a clean marketplace, and the balance is still above its pre-build ratio, so FY26 is lapping a charge, not harvesting a release; the beats show up equally when the reserve was being built."

Recommendation for the pitch: do not lead with G12 as an explanation of beats. Use only: (1) reserve balances and ratios (survive); (2) YoY lapping arithmetic labelled as an equal-usage upper bound with the range of the FY25 drag ($300M to $645M); (3) the information-loss point (Schedule II withdrawn, allowance dollar figure dropped, new "not material" variance sentences); (4) a request for the FY25 to FY27 returns rollforward in dollars on the Q2 FY27 call or at the investor day.

## 11. What would settle it

The returns and discounts rollforward (additions, usage, reversals) for FY25 to FY27, split by region and channel; quarterly cost-of-inventory asset for returns; Circana sell-through against shipments for North America; a 10-Q disclosure of reserve true-ups (Nike says variances were "not material to reported Revenues", FY26 10-K p. 47, which if taken literally means no material change-in-estimate revenue in FY26 and pushes the explanation toward rate-driven provisioning on current shipments or usage, not prior-period true-ups). Obtainable by asking on the Q2 FY27 call (about Dec 17, 2026) or the Nov 16 to 17 investor day, or from Nike's debt-investor Q&A.

## 12. Routes tried (per repo rule), usage versus provision, and analyst expectation questions

| # | Route | Result |
|---|---|---|
| 1 | Revenue recognition and critical accounting policy text FY26 10-K p. 47, p. 62 | WORKED for mechanics; no usage figure |
| 2 | Schedule II FY19 to FY24 (p. 89 to p. 100 across 10-Ks) | PARTIAL; ends FY24; revised three times |
| 3 | Cash flow statement FY26 10-K p. 58 | BLOCKED; accrued liabilities lumped |
| 4 | Cost-of-inventory asset ratio and AR (balance sheet p. 57) | PARTIAL; AR up $530M ex-IEEPA is weakly against credit-memo usage but confounded by timing, FX, terms |
| 5 | Peer rollforward (adidas additions, usage, reversals 2022 to 2025) | WORKED as analogy; shows both effects occur |
| 6 | Puma refund obligations 2023 to 2025 | WORKED for direction (build in 2025) |
| 7 | Transcript Q&A for Q4 FY25 to Q1 FY27 | WORKED for guidance language; no reserve-sizing question |
| 8 | Web search for analyst commentary on Nike reserves (2 queries; Barchart fetch returned empty) | BLOCKED/empty |
| 9 | 10-Q segment text units versus ASP, NA wholesale | WORKED; reserve not named as driver in ASP bullets |
| 10 | Tax-basis deferred asset (G12 SNIPPET, not re-run) | Not repeated; direction only |
Verdict on the attribution: after more than five different routes, usage versus provision remains undecidable from public data. The data that would settle it is in section 11.

## 13. Limits of this check

Not re-run: G12's Under Armour, Deckers, Skechers, VF XBRL peer rows (SNIPPET status stays); the LSEG $0.43 consensus; the 25 transcript set beyond the calls cited. The IEEPA tax rate used for ex-IEEPA EPS is an assumption. Q4 FY26 diluted shares 1,482.4 (mine) versus 1,482.9 (G12) changes EPS by under $0.0001.
