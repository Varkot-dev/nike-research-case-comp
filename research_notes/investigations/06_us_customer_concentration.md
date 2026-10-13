# Why did Nike's top three U.S. customers rise from 21% (FY24) to 29% (FY26) of U.S. sales?

> **Status: DRAFT (Oct 13, 2026).** Produced by the multi-agent investigation (one investigator, two adversarial reviewers, one revision round). Sources are cited inline; independent spot-check against source documents is in progress and results will be logged at the end of this file. Treat figures as provisional until marked verified.


Scope: Nike FY24 (Jun 2023 to May 2024) to FY26 (Jun 2025 to May 2026). Scripts: `rh/conc/calc.py` (output `calc_out.txt`) and, for revision 2, `rh/conc/calc2.py` (output `calc2_out.txt`), both in the scratchpad. Labels: **filing**, **Nike release** (earnings call transcript posted by Nike), **secondary**, **snippet only** (not usable as evidence), **my arithmetic**, **opinion**.

## Answer in one paragraph

The 8 point rise is not one event. An exact three-factor identity (top 3 / U.S. = top 3 / NA wholesale x NA wholesale / NA x NA / U.S.) splits it into the following pieces (my arithmetic, log-mean split, details in section 1):

1. **About 3.1 points come from Nike Direct shrinking (channel mix).** As Direct fell from 48.6% to 41.7% of North America revenue, wholesale became a bigger share of the denominator. This term holds the top three's share of wholesale constant, so it is mechanical. Its causes (Nike's digital pullback) are covered in other notes. Range across rounding bands: 3.0 to 3.2 points.
2. **About 0.4 points come from the U.S. denominator items outside the NA Nike Brand segment, mainly the Converse collapse (FY26 only).** U.S. revenue minus NA revenue went from +$155m to -$153m. Over the same period Converse revenue fell $908m and Converse said FY26 declines hit "all territories". The term is almost independent of rounding (0.36 to 0.37).
3. **About 4.5 points (rounding band 3.5 to 5.5) come from the top three gaining share within NA wholesale.** That breaks down as:
   - **JD Sports buying Hibbett (closed 25 Jul 2024): about 3.0 to 4.2 points over two years.** FY25 contributes 2.5 to 3.7 points if Nike counts Hibbett inside JD from the close date, or 2.9 to 3.8 if for the full year. FY26 annualization adds about 0.45 to 0.5. Revision 2 recomputes this from Hibbett's last 10-K (Nike = 73.7% of purchases), from JD's reported £713m of Hibbett revenue, and with a calibration for the known upward bias of retailer-side estimates.
   - **A FY25 residual of -0.7 to +0.6 points at the reported percents (-1.8 to +1.7 across rounding bands).** FY25 share gains at large accounts are therefore **not required by the data, but not excluded either**.
   - **A FY26 residual of about +0.85 to +0.95 points.** Four effects can fill it: Dick's absorbing Foot Locker, which frees a top-three slot; a rebound from FY25's wholesale returns and discounts (0 to +0.8 points, depending on how much of them fell on the top three); existing-partner gains; and who the new #3 is.

**Verdicts in brief (revision 2):**
- **JD plus Hibbett is the largest single identified driver within wholesale.** JD North America would have to buy under about 30% to 34% of its goods from Nike to rank below Hibbett. Its largest U.S. chain, Finish Line, last disclosed 66%. Academy (largest vendor at most about $0.44bn) and Kohl's (all-brand footwear at cost about $0.91bn) cannot outrank it. So JD was very likely the FY24 #3, and the merger adds about Hibbett's volume.
- **Dick's and Foot Locker merging explains nothing in FY25** (not yet closed). In FY26 it is part of a residual of under 1 point, plus whatever the slot effect adds.
- **FY25 share gains at large accounts are unresolved** (residual -0.7 to +0.6 points). A shift between Dick's and Foot Locker inside the top three does not change the top-three sum.
- **FY25 off-price entry is very unlikely.** To enter the top three in FY25, an off-price buyer needed at least about $1.15bn of Nike product, about 11% of NA wholesale. Nike's only FY25 mention is one quarter's "increased shipments to our value partners", in a quarter when NA wholesale rose $59m in total. Sales to off-price buyers outside the top three lower concentration, they do not raise it.
- **Exits of small accounts are ruled out as a driver** (non-top-3 wholesale grew $0.5bn in FY26).
- **Converse is a real but small driver** (+0.4 points, all in FY26). It was missing from revision 1.
- **The FY26 #3 is still unidentified.** Academy (at most about $0.5bn) can be #3 only if the FY25 top-three members grew 10% or more with Foot Locker aggregated for the full year, or 18% or more if not. Amazon, Kohl's and off-price buyers remain open.

## 1. Candidate explanations: verdicts

| # | Candidate | Verdict | Quantified contribution (pts of U.S. sales; FY24 to FY26 total = +8) | Deciding evidence |
|---|---|---|---|---|
| 1 | Nike Direct shrinking raises the wholesale share of the denominator mechanically | **Supported** (accounting term; causes lie in Direct strategy) | **+3.1** (band 3.04 to 3.17). FY25 +0.93, FY26 +2.28 | NA wholesale share 51.4% (FY24), 53.6% (FY25), 58.3% (FY26) (Table B). The term holds the top three's share of NA wholesale fixed. Any Direct demand that migrated to the top three appears in #4, not here, so #1 and #4 do not double count |
| 2 | **JD Sports acquired Hibbett (closed 25 Jul 2024)**: two U.S. accounts became one customer | **Supported** (largest identified within-wholesale driver; magnitude estimated; aggregation rule unknown) | FY25: **+2.5 to 3.7** (aggregated from close) or **+2.9 to 3.8** (full year). FY26: **+0.44 to 0.52** annualization (only if aggregated from close) | Hibbett FY2024: Nike "73.7%" of purchases; COGS $1,145.2m; inventories fell $76.5m. Purchases at cost $699 to 773m per 52 weeks. JD: "Hibbett contributed £713m of revenue" (25 Jul 2024 to 1 Feb 2025). Calibration f = 0.83 to 0.98 (Table C2). JD > Hibbett unless JD NA's Nike share is below 30 to 34% (Finish Line: 66%) |
| 2a | JD was not the FY24 #3, so the merger adds less than Hibbett's volume | **Ruled out as material** (for Hibbett or Academy as the old #3); Kohl's very unlikely | If JD had been smaller than Hibbett, the effect would be JD + Hibbett(window) - Hibbett(full), which is lower. The data do not support that case | JD NA FY24 Nike purchases, alternative estimate $1,152 to 1,726m (my arithmetic; assumptions in Table D). Academy largest vendor at most $444m (2024). Kohl's all-brand footwear at cost $914m (2023). The FY24 gap (reported $4.5bn below the summed estimates) is consistent with a common overshoot factor f of 0.83 to 0.98 applied to all retailer estimates, JD included |
| 3 | Dick's acquisition of Foot Locker (closed 8 Sep 2025, in Nike FY26 Q2) | **Partly supported**: none of FY25; in FY26 a candidate within a residual of about +0.85 to 0.95 pts | FY25: **0**. FY26: if both were top three, the merger adds the old #4 account (X) to the sum. Whether X is large depends on member growth (Table G). If Foot Locker's Jun 1 to Sep 7 volume is not aggregated, about $0.4 to 0.55bn drops out (2.0 to 2.7 pts swing) | DKS 10-K: "On September 8, 2025, we completed the acquisition of Foot Locker". FY25 was already 25% before the close |
| 4 | Share gains at large accounts | **FY25: unresolved, bounded. FY26: partly supported, not separable from #3, #7 and #11** | FY25 residual **-0.70 to +0.63** at reported percents (**-1.80 to +1.74** across bands). Top-3 dollars excluding Hibbett grew -12.4% to +3.1% vs NA wholesale -4.7%. FY26: inside the residual of about +0.85 to 0.93 | FY26 10-K: NA wholesale +14% "including expanded distribution, higher shipments to existing partners". Q2 FY26: "meaningful growth coming from existing partners". Q4 FY26: Foot Locker comp "positive for the first time in four years" |
| 4a | A shift inside the top three (Dick's purchases up about 13%, Foot Locker U.S. down about 9% in Table D) | **Ruled out as an explanation of the change** | 0. A transfer between two top-three members leaves their sum unchanged. Foot Locker U.S. (at least $1.5bn x f) stays far above any #4 candidate, so it does not drop out | Table D; Academy and Kohl's bounds (Table G) |
| 5 | Exit of small accounts | **Ruled out as a driver** | About 0. Non-top-3 NA wholesale **rose $501m** in FY26. The FY25 drop of $926m includes about $0.6 to 0.75bn of Hibbett moving into JD | FY26 10-K "expanded distribution"; Q3 FY26 "new distribution" |
| 6 | Amazon became a top-3 customer | **Cannot explain FY25. FY26 unresolved** | FY25: 0 (launched fall 2025). FY26: at most about 8 months. No disclosed size; the only estimate is a snippet | Q4 FY25: "This Fall, they'll carry a select assortment" |
| 7 | Off-price (value channel) liquidation | **FY25: very unlikely to have raised concentration. FY26: unresolved** | FY25: about 0. An off-price buyer must exceed the smallest of Dick's, Foot Locker U.S. and JD+Hibbett (at least about $1.15bn) to enter the top three. Below that, its volume sits in the denominator and lowers concentration. FY26: possibly the new #3 | Q3 FY25 (PDF p. 12): NA wholesale +3% "due primarily to favorable shipment timing and increased shipments to our value partners". NA wholesale that quarter was $2,499m vs $2,440m, +$59m in total. The FY25 10-K NA text does not mention value channels. Q4 FY25 puts liquidation through "select value partners" in the "next two quarters" (FY26 H1) |
| 8 | Lower U.S. revenue (denominator) in FY25 | **Folded into #1 and #9**; not separate | n/a | U.S. revenue -8.5% in FY25 while top-3 dollars rose 9.0% |
| 9 | **Converse U.S. collapse** (and other U.S. items outside NA Nike Brand) shrinking the denominator | **Supported, small** (new in revision 2) | **+0.36** (FY25 -0.01, FY26 +0.41) as the exact NA/U.S. factor. Sensitivity: a $300 to 450m non-top-3 Converse U.S. loss is worth 0.42 to 0.63 | U.S. minus NA: +$155m, +$153m, -$153m. Converse revenue $2,082m, $1,692m, $1,174m; FY26 "declines in all territories". In FY25, Converse wholesale grew in North America, which matches the flat FY25 term. U.S. Converse stores fell 81 to 60 (repo note 08). The Canada split and the Corporate line (-42, -97, +2) are unknown, so this is not purely Converse |
| 10 | Change in how Nike defines or aggregates a "customer" | **Unresolved; it sets the size of #2 and #3** | FY25: 2.5 to 3.7 vs 2.9 to 3.8 pts (from close vs full year). FY26: 2.0 to 2.7 pt swing for Foot Locker pre-close | FY19 to FY24 series smooth (24, 24, 24, 22, 22, 21); concentration sentence unchanged |
| 11 | **Where FY25 "higher sales returns and discounts with our wholesale partners" landed** (FY26 rebound) | **Unresolved; sized** (new in revision 2) | FY25: concentration held down by 0 to 0.28 pts. FY26 rebound: **0 to +0.84 pts**, depending on how far the top three's share of NA returns exceeded their share of NA wholesale (47 to 49%) | Sales-related reserves (returns, post-invoice discounts, claims) $994m, $1,282m, $1,834m, $1,589m (FY23 to FY26). Revenue swing from accrual changes FY25 to FY26: +$797m globally, about $340m NA (my arithmetic, proportional to wholesale). Q4 FY25: "North America inventory actions continued with higher sales related returns" |
| 12 | U.S. vs NA proxy error | **Replaced by #9** (now measured, not assumed small) | see #9 | Revision 1 called this "small" without sizing it |

Bridge (my arithmetic; log-mean split, exactly additive):

| Component | FY24 to FY25 | FY25 to FY26 | FY24 to FY26 |
|---|---|---|---|
| Reported change | +4.0 | +4.0 | +8.0 |
| Channel mix (Direct shrink) | +0.93 | +2.28 | +3.11 |
| NA/U.S. factor (Converse, Canada, other) | -0.01 | +0.41 | +0.36 |
| Within NA wholesale | +3.08 | +1.31 | +4.53 (band 3.5 to 5.5) |
| of which JD plus Hibbett | +2.5 to 3.8 | +0.44 to 0.52 (0 if counted full year in FY25) | about +3.0 to 4.2 |
| of which residual | -0.7 to +0.6 | about +0.85 to 0.93 (dollar basis) | about +0.3 to 1.5 |
| candidates for the residual | share shift to or from large accounts; aggregation rule | Dick's+Foot Locker slot (X); returns rebound (0 to 0.84); existing-partner gains; new #3 identity | |

The FY26 residual uses the dollar basis (+1.37 pt within, less annualization). The log-mean basis gives +1.31. The difference is a rounding-scale matter.

## 2. Data tables

### A. Reported concentration and U.S. revenue (filing)

| FY | Top 3 U.S. customers, % of U.S. sales | U.S. revenue $m | Top-3 dollars $m (my arithmetic) | Band at ±0.5 pt | 10% single-customer cap $m (my arithmetic) |
|---|---|---|---|---|---|
| FY19 | 24 | 16,091 | | | |
| FY20 | 24 | 14,625 | | | |
| FY21 | 24 | 17,363 | | | |
| FY22 | 22 | 18,749 | | | |
| FY23 | 22 | 22,007 | | | |
| FY24 | 21 | 21,551 | 4,526 | 4,418 to 4,633 | 5,136 |
| FY25 | 25 | 19,725 | 4,931 | 4,833 to 5,030 | 4,631 |
| FY26 | 29 | 20,358 | 5,904 | 5,802 to 6,006 | 4,640 |

Consolidated revenue: $51,362m (FY24), $46,309m (FY25), $46,398m (FY26) (data/nike_channel_split.csv). Non-U.S. top three: 15%, 16%, 16%.

### B. Channel mix and the NA/U.S. factor (filing; ratios are my arithmetic)

| FY | NA wholesale $m | NA Direct $m | NA total $m | U.S. minus NA $m | Wholesale share | Top 3 / NA wholesale $ | NA / U.S. |
|---|---|---|---|---|---|---|---|
| FY24 | 11,004 | 10,392 | 21,396 | +155 | 51.4% | 41.1% | 0.9928 |
| FY25 | 10,484 | 9,088 | 19,572 | +153 | 53.6% | 47.0% | 0.9922 |
| FY26 | 11,958 | 8,553 | 20,511 | -153 | 58.3% | 49.4% | 1.0075 |

Converse (filing, segment note; data/nike_channel_split.csv): total $2,082m, $1,692m, $1,174m; wholesale $1,098m, $875m, $605m; direct $832m, $694m, $477m. Counterfactual at the FY24 wholesale share: FY26 25.6% (revision 1, unchanged).

### C. Dollar flows (my arithmetic)

| Period | Top-3 $ change | NA wholesale change | U.S. revenue change | Non-top-3 NA wholesale change |
|---|---|---|---|---|
| FY24 to FY25 | +$406m (+9.0%) | -$520m (-4.7%) | -8.5% | -$926m |
| FY25 to FY26 | +$973m (+19.7%) | +$1,474m (+14.1%) | +3.2% | +$501m |

### C2. Calibration of retailer-side estimates (my arithmetic)

Retailer cost of sales includes freight, distribution and shrink, so purchase estimates run above Nike's net revenue. I model the true value as f x estimate, with f common to all retailers. FY24 check: reported top 3 = f x (Dick's + Foot Locker U.S. + #3).
- If JD NA is #3: **f = 0.83 to 0.98**.
- If Hibbett is #3: f = 0.91 to 1.01. This requires JD NA < Hibbett, which needs JD NA's Nike share of purchases below 30% to 34% (Section 1, #2a).
- At f = 1 the implied FY24 #3 would be only $325 to 727m. That is the reviewer's point, and it is resolved by f < 1 rather than by a different #3.

### D. Retailer-side estimates of Nike purchases ($m; my arithmetic with labelled assumptions)

Method: Nike purchases ≈ Nike share x (cost of sales minus occupancy or lease cost, plus inventory increase or minus inventory decrease). Dick's, Foot Locker and JD rows are unchanged from revision 1. The Hibbett rows are revised.

| Account | Period | Inputs (filing) | Nike purchase estimate (before f) |
|---|---|---|---|
| Dick's | FY2023 (to Feb 3, 2024) | COGS 8,450.664; lease 757.142; CF inventories +18.823; Nike ~24% | 1,842 to 2,024 |
| Dick's | FY2024 (to Feb 1, 2025) | COGS 8,617.153; lease 782.920; CF inventories (501.033); Nike ~25% | 2,084 to 2,280 |
| Foot Locker | 2023 | Cost of sales 5,895; occupancy 1,029; CF inventories 120; Nike ~65%; U.S. 5,409 of 8,154 | U.S. ~2,046 |
| Foot Locker | 2024 | 5,666; 992; (40); Nike ~59%; U.S. 5,328 of 7,971 | U.S. ~1,859 |
| **Hibbett** | **FY2024 (53 wks to Feb 3, 2024)** | COGS 1,145.184; inventories decreased 76.545; operating lease 81.957 + variable 19.926; Nike 73.7% of purchases | **712 to 788 (53 wks); 699 to 773 per 52 wks** |
| Hibbett (check) | FY2023 | COGS 1,106.415 + inventory build 199.619; Nike 69.9% | 848 to 914. This was an inventory-rebuild year. Revision 1 omitted the build and used "70% of inventory"; FY2024 replaces it |
| **Hibbett in Nike FY25 after close** | Jul 25, 2024 to May 31, 2025 | (A) 0.852 of the 52-wk figure; (B) JD's £713m (Jul 25, 2024 to Feb 1, 2025) at an assumed 1.25 to 1.32 $/£, plus Feb 2 to May 31 at Hibbett's Q1 FY2025 run rate ($447.163m per 91 days), x COGS ratio 0.662 x 73.7% | (A) 596 to 659; (B) 721 to 745; **range 596 to 745** |
| Hibbett, Jun 1 to Jul 24 | FY26 annualization | Q2 FY2024 sales 374.877 per 91 days x 54/91 x 0.662 x 73.7% | 109 (x f = 0.44 to 0.52 pt) |
| JD Group North America | FY24 | NA revenue £3,352m | 838 to 1,244 (revision 1: Nike 40 to 50% of sales, secondary). Alternative: 1,152 to 1,726 (Nike 50 to 66% of purchases, COGS 55 to 60% of sales, FX 1.25 to 1.30; all assumptions, 66% from Finish Line FY2018) |
| JD Group U.S. | FY25 / FY26 | U.S. revenue £4,111m / £4,617m | 1,028 to 1,526 / 1,154 to 1,714 (revision 1 assumptions) |
| Dick's Inc. consolidated | FY2025 | COGS 11,547.858; write-down 217.926; lease 1,165.354; CF inventories +181.316; Nike ~31% | 3,095 to 3,456 (global) |

### E. FY25 to FY26: size of the new #3 (X) when Dick's and Foot Locker become one customer (my arithmetic, revision 1)

| Growth of FY25 top-3 members | X, Foot Locker aggregated full year | X, Foot Locker pre-close excluded ($400 to 550m) |
|---|---|---|
| 0% | 973 | 1,373 to 1,523 |
| 5% | 726 | 1,126 to 1,276 |
| 14.1% | 279 | 679 to 829 |

### F. Sales-related reserves (filing; differences are my arithmetic)

| May 31 | Reserve $m | Change $m | Of which sales returns reserve $m |
|---|---|---|---|
| FY23 | 994 | | |
| FY24 | 1,282 | +288 | 799 |
| FY25 | 1,834 | +552 | 1,277 |
| FY26 | 1,589 | -245 | 1,099 |

Concentration effect = (top-3 share of NA returns and discounts minus top-3 share of NA wholesale) x NA part of the accrual swing / U.S. revenue. The NA part is allocated by NA's share of Nike Inc. wholesale (0.39 FY25, 0.43 FY26; opinion that the reserves are mainly wholesale). Proportional allocation gives 0. If the top three took 75% or 100%: FY25 depressed by 0.15 or 0.28 pt, and the FY26 rebound adds 0.43 or 0.84 pt.

### G. Bounds on candidate #3 and #4 accounts (filing; my arithmetic)

| Account | Disclosure | Upper bound on Nike purchases |
|---|---|---|
| Academy 2024 (to Feb 1, 2025) | largest vendor ~11% of inventory purchases; COGS 3,921.990; inventories +114.681 | 444 |
| Academy 2025 (to Jan 31, 2026) | largest vendor ~12%; COGS 3,947.801; inventories +194.916 | 497 |
| Kohl's 2025 | no vendor >10% of net purchases; cost of merchandise sold 9,228 | 923 (weak) |
| Kohl's footwear, all brands, at cost | footwear sales x COGS/sales: 2023 914, 2024 816, 2025 756 | caps Nike footwear only |

Slot test for FY26: if X is Academy (at most $497m, or $487m after f), the FY25 members must have grown at least 9.6% (Foot Locker aggregated full year) or 17.8% to 21.0% (pre-close excluded). If X is at most $756m, they need at least 4.4% or 12.5% to 15.5%. NA wholesale grew 14.1%.

## 3. Verbatim quotes and sources

| # | Quote | Source, page | URL | Label |
|---|---|---|---|---|
| Q1 | "During fiscal 2024, our three largest United States customers accounted for approximately 21% of sales in the United States." | Nike FY2024 10-K, p. 2 | https://investors.nike.com/sec-filings/all-sec-filings/content/0000320187-24-000044/nke-20240531.htm | filing |
| Q2 | "During fiscal 2025, our three largest United States customers accounted for approximately 25% of sales in the United States." | Nike FY2025 10-K, p. 2 | https://www.sec.gov/Archives/edgar/data/320187/000032018725000047/nke-20250531.htm | filing |
| Q3 | "During fiscal 2026, our three largest United States customers accounted for approximately 29% of sales in the United States." | Nike FY2026 10-K, p. 2 | https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm | filing |
| Q4 | FY2023 "approximately 22%"; FY2022 "approximately 22%"; FY2021 "approximately 24%" | Nike FY2021 to FY2023 10-Ks, p. 2 | .../000032018723000039/nke-20230531.htm ; .../000032018722000038/nke-20220531.htm ; .../000032018721000028/nke-20210531.htm | filing |
| Q5 | "No customer accounted for 10% or more of our consolidated Revenues during fiscal 2026." | Nike FY2026 10-K, p. 3 | as Q3 | filing |
| Q6 | "Revenues derived in the United States were $20,358 million, $19,725 million and $21,551 million" | Nike FY2026 10-K, p. 87 | as Q3 | filing |
| Q7 | "We sell our products to thousands of wholesale accounts in the United States" (FY24) vs "to wholesale accounts" (FY25, FY26) | 10-Ks p. 2 | as Q1 to Q3 | filing |
| Q8 | "Wholesale revenues increased 14% including expanded distribution, higher shipments to existing partners and fewer marketplace management actions taken in the current year." | Nike FY2026 10-K, p. 37 | as Q3 | filing |
| Q9 | "North America revenues decreased 8% on a currency-neutral basis ... Wholesale revenues decreased 5%." | Nike FY2025 10-K, p. 38 | as Q2 | filing |
| Q10 | "higher sales returns and discounts with our wholesale partners to reduce inventory" | Nike FY2025 10-K, p. 30 | as Q2 | filing |
| Q11 | "over 20% wholesale growth in North America with meaningful growth coming from existing partners." | Q2 FY26 call, PDF p. 4 | https://s1.q4cdn.com/806093406/files/doc_financials/2026/q2/NIKE-Inc-Q2FY26-UNOFFICIAL-Transcript.pdf | Nike release |
| Q12 | "the quarter certainly benefitted from liquidation to value channels" | Q2 FY26 call, PDF p. 9 | as Q11 | Nike release |
| Q13 | "Wholesale returned to growth in the quarter, partially due to shipment timing in the prior year, as well as higher liquidation volume to value channels." | Q1 FY26 call, PDF p. 10 | https://s1.q4cdn.com/806093406/files/doc_financials/2026/q1/NIKE-Inc-Q1FY26-UNOFFICIAL-Transcript.pdf | Nike release |
| Q14 | "our revenue growth and retail sales comp with Foot Locker was positive for the first time in four years" | Q4 FY26 call, PDF p. 10 | https://s1.q4cdn.com/806093406/files/doc_financials/2026/q4/NIKE-Inc-Q4FY26-UNOFFICIAL-Transcript.pdf | Nike release |
| Q15 | "Wholesale revenue growth was driven by new distribution and lapping marketplace management actions" | Q3 FY26 call, PDF p. 10 | https://s1.q4cdn.com/806093406/files/doc_financials/2026/q3/NIKE-Inc-Q3FY26-UNOFFICIAL-Transcript.pdf | Nike release |
| Q16 | "we announced a new partnership with Amazon. This Fall, they'll carry a select assortment" | Q4 FY25 call, PDF p. 5 | https://s1.q4cdn.com/806093406/files/doc_financials/2025/q4/NIKE-Inc-Q4FY25-UNOFFICIAL-Transcript.pdf | Nike release |
| Q17 | "Over the next two quarters, Nike will continue liquidating excess inventory through our value stores and select value partners." | Q4 FY25 call, PDF p. 14 | as Q16 | Nike release |
| Q18 | "On September 8, 2025, we completed the acquisition of Foot Locker" | DICK'S FY2025 10-K, p. 8 | https://www.annualreports.com/HostedData/AnnualReports/PDF/NYSE_DKS_2025.pdf | filing |
| Q19 | "Nike, our largest vendor, representing approximately 31% of our consolidated merchandise purchases" | DICK'S FY2025 10-K, p. 9 | as Q18 | filing |
| Q20 | Segment net sales and gross profit, DICK'S and Foot Locker Businesses | DICK'S FY2025 10-K, p. 40 | as Q18 | filing |
| Q21 | COGS 11,547,858 / 8,617,153 / 8,450,664; lease cost 1,165,354 / 782,920 / 757,142; inventories 181,316 / (501,033) / 18,823 | DICK'S FY2025 10-K, pp. 56, 72, 60 | as Q18 | filing |
| Q22 | Nike "approximately 25%" (FY2024) and "approximately 24%" (FY2023) of merchandise purchases | DICK'S FY2024 and FY2023 10-Ks, p. 7 | https://www.annualreports.com/HostedData/AnnualReportArchive/d/NYSE_DKS_2024.pdf | filing |
| Q23 | "Approximately 59% and 65% was purchased from one supplier, Nike, Inc., in 2024 and 2023, respectively." | Foot Locker 2024 10-K, p. 29 | https://www.annualreports.com/HostedData/AnnualReports/PDF/NYSE_FL_2024.pdf | filing |
| Q24 | Cost of sales 5,666 / 5,895; occupancy 992 / 1,029; U.S. 5,328 / 5,409; inventories (40) / 120 | Foot Locker 2024 10-K, pp. 36, 26, 50, 40 | as Q23 | filing |
| Q25 | "During Fiscal 2023, approximately 70% of our inventory was purchased from one vendor, Nike" | Hibbett FY2023 10-K, p. 13 | https://www.annualreports.com/HostedData/AnnualReports/PDF/NASDAQ_HIBB_2023.pdf (URL resolves, 1,651,392 bytes; local copy now `dl/conc2/NASDAQ_HIBB_2023_FY2023_10K.pdf`) | filing |
| Q26 | "Cost of goods sold 1,106,415"; "Operating lease cost $ 76,051"; "Variable lease cost (1) 18,188" | Hibbett FY2023 10-K, pp. 38, 47 | as Q25 | filing |
| Q27 | "JD Group completed the acquisition of Hibbett on 25 July 2024" | JD FY26 results RNS (7 May 2026) | https://data.fca.org.uk/artefacts/NSM/RNS/2cc0a7ae-88bf-4bae-beb8-621993259a90.html | filing (UK RNS) |
| Q28 | "US (2026: £4,617 million; 2025: £4,111 million)"; "North America* 4,779 (1.8)% +3.2%" (total, LFL, organic) | JD FY26 results RNS | as Q27 | filing (UK RNS) |
| Q29 | "North America revenue* increased 27% to £4,242m including six months of Hibbett"; FY24 North America revenue 3,352 | JD FY25 results RNS (21 May 2025) | https://data.fca.org.uk/artefacts/NSM/RNS/5663132.html | filing (UK RNS) |
| Q30 | "JD said it makes about 45% of all its sales from Nike" | LBC, 2 Oct 2024 | https://www.lbc.co.uk/business/3d3a60d8c9164aa3a4869677a3ffc91c/ | secondary |
| Q31 | Goldman Sachs 2017 Amazon estimate | search summary | https://us.fashionnetwork.com/news/Nike-close-to-selling-directly-on-amazon,841642.html | snippet only (not usable as evidence) |
| Q32 | "Our largest vendor, Nike, represented 73.7%, 69.9%, and 61.0% of our purchases for Fiscal 2024, Fiscal 2023 and Fiscal 2022, respectively." Also p. 13: "approximately 74% of our inventory was purchased from one vendor, Nike" | Hibbett FY2024 10-K (to Feb 3, 2024), p. 44 (also p. 32) | https://www.sec.gov/Archives/edgar/data/1017480/000101748024000043/hibb-20240203.htm (accession 0001017480-24-000043 from data.sec.gov submissions; read through WebFetch because a curl download returned 403) | filing |
| Q33 | "Net sales $ 1,728,887 $ 1,708,316 $ 1,691,184"; "Cost of goods sold 1,145,184 1,106,415 1,044,777"; cash flow "Inventories, net 76,545"; "Operating lease cost" 81,957; "Variable lease cost (1)" 19,926 | Hibbett FY2024 10-K, pp. 39, 40, 48 | as Q32. XBRL check: data.sec.gov/api/xbrl/companyfacts/CIK0001017480.json gives CostOfGoodsAndServicesSold 1,145,184,000 and IncreaseDecreaseInInventories -76,545,000 (FY2024), Q1 FY2025 revenue 447,163,000, Q2 FY2024 revenue 374,877,000 | filing |
| Q34 | "Hibbett contributed £713m of revenue in the period." | JD FY25 results RNS (52 weeks to 1 Feb 2025) | as Q29 | filing (UK RNS) |
| Q35 | "accounted for approximately 66% and 71% of total Company purchases in fiscal 2018 and 2017, respectively." (Nike); "Approximately 66% of merchandise was purchased from one vendor (Nike)." | Finish Line FY2018 10-K (to Mar 3, 2018), pp. 4, 9 | https://www.sec.gov/Archives/edgar/data/886137/000088613718000035/finl201810k.htm (read through WebFetch) | filing (stale; before the JD takeover) |
| Q36 | "In 2024, purchases from our largest vendor represented approximately 11% of our total inventory purchases." COGS 3,921,990; inventories (114,681) | Academy FY2024 10-K, pp. 27, 72, 74 | https://www.annualreports.com/HostedData/AnnualReports/PDF/NASDAQ_ASO_2024.pdf | filing |
| Q37 | "In 2025, purchases from our largest vendor represented approximately 12% of our total inventory purchases." COGS 3,947,801; inventories (194,916) | Academy FY2025 10-K (to Jan 31, 2026), pp. 25, 69, 71 | https://www.annualreports.com/HostedData/AnnualReports/PDF/NASDAQ_ASO_2025.pdf | filing |
| Q38 | "No vendor individually accounted for more than 10% of our net purchases in 2025." Footwear net sales 1,210 / 1,299 / 1,444; cost of merchandise sold 9,228 / 9,661 / 10,498 | Kohl's FY2025 10-K, pp. 6, 50, 43 | https://www.annualreports.com/HostedData/AnnualReports/PDF/NYSE_KSS_2025.pdf | filing |
| Q39 | "the Company's sales-related reserve balance, which includes returns, post-invoice sales discounts and claims, was $ 1,589 million and $ 1,834 million" (FY26); "$ 1,834 million and $ 1,282 million" (FY25); "$ 1,282 million and $ 994 million" (FY24) | Nike FY2026 10-K p. 84; FY2025 10-K p. 83; FY2024 10-K p. 85 | as Q3, Q2, Q1 | filing |
| Q40 | "Wholesale increased 3%, due primarily to favorable shipment timing and increased shipments to our value partners in the third quarter." (NA) | Q3 FY25 call, PDF p. 12 | https://s1.q4cdn.com/806093406/files/doc_financials/2025/q3/NIKE-Inc-Q3FY25-UNOFFICIAL-Transcript.pdf | Nike release |
| Q41 | "for our wholesale partners, we are making investments in sales related returns, reducing forward supply, and providing higher wholesale discounts to liquidate aged inventory." | Q3 FY25 call, PDF p. 15 | as Q40 | Nike release |
| Q42 | "Sales to Wholesale Customers" row: 2,499 (Q3 FY25), 2,440 (Q3 FY24), +2% reported, +3% currency-neutral (NA table) | Nike Q3 FY25 10-Q, p. 32 | https://www.sec.gov/Archives/edgar/data/320187/000032018725000016/nke-20250228.htm (mirror investors.nike.com/sec-filings/all-sec-filings/content/0000320187-25-000016/nke-20250228.htm) | filing |
| Q43 | "Wholesale revenues decreased 20% on a currency-neutral basis, as declines in Western Europe and Asia were partially offset by growth in North America." (Converse FY25) | Nike FY2025 10-K, p. 43 | as Q2 | filing |
| Q44 | "Converse revenues decreased 32% on a currency-neutral basis driven by declines in all territories." | Nike FY2026 10-K, p. 42 | as Q3 | filing |
| Q45 | "North America inventory actions continued with higher sales related returns and higher discounts to liquidate aged inventory" | Q4 FY25 call, PDF p. 10 | as Q16 | Nike release |

NA and Converse channel values are in data/nike_channel_split.csv (segment note: FY24 10-K p. 84, FY25 p. 82, FY26 p. 83).

## 4. What remains unresolved and the data that would resolve it

1. **How Nike aggregates acquired customers.** This sets the Hibbett piece (2.5 to 3.7 vs 2.9 to 3.8 pts in FY25) and Foot Locker's pre-close volume in FY26 (a 2.0 to 2.7 pt swing in the required X). Only Nike can answer.
2. **FY25 share gains or losses at large accounts** (residual -0.7 to +0.6 at reported percents). A tighter Hibbett figure (Hibbett's FY2025 Nike purchases under JD) and the calibration factor f would narrow it. Exact percents, not "approximately", would remove the ±1 pt band.
3. **Distribution of FY25 returns and discounts across partners** (0 to +0.84 pts of the FY26 residual). Nike reports only the global reserve.
4. **Identity of the FY26 #3.** Academy is possible only if the members grew 10% or more (with full-year Foot Locker aggregation). Amazon, Kohl's and off-price buyers (TJX, Ross, Burlington) do not disclose Nike volume.
5. **U.S.-only channel and Converse U.S. revenue.** These would split the +0.41 FY26 NA/U.S. term between Converse, Canada and Corporate.
6. **JD North America's Nike share of purchases.** JD's FY26 annual report (annualreports.com LSE_JD_2025.pdf, checked) names Nike but gives no percentage. The 45% remains secondary.

## Revision log

**Revision 2 (this version), in response to two reviewer objections:**
1. **FY25 "share gains at large accounts: ruled out" changed to "unresolved, bounded".** The test now runs over rounding bands, the calibration factor f (0.8 to 1.0) and two Hibbett aggregation rules. The residual is -0.70 to +0.63 at the reported percents and -1.80 to +1.74 across bands, so revision 1's "residual about 0" was a coincidence of point estimates.
2. **Hibbett re-estimated from its last 10-K (FY2024, to Feb 3, 2024): Nike 73.7% of purchases, inventory decrease included.** Revision 1 used the FY2023 inventory-rebuild year and ignored the $199.6m build. A second method uses JD's reported £713m of Hibbett revenue. With calibration, the FY25 merger piece is now 2.5 to 3.8 pts, not 3.1 to 3.3.
3. **"U.S. vs NA proxy error is small" replaced by a measured Converse term.** A third factor (NA/U.S.) adds +0.36 pt over FY24 to FY26, all of it in FY26 (+0.41). The within-wholesale FY26 piece falls from +1.7 to +1.3 accordingly.
4. **"JD was the FY24 #3" tested rather than assumed.** It is supported by the JD-below-Hibbett threshold (30 to 34% Nike share needed) against Finish Line's 66%, by Academy's largest-vendor cap ($444m) and by Kohl's all-brand footwear at cost ($914m). The reviewer's implied-#3 point is reconciled by f < 1 (Table C2).
5. **FY25 off-price candidate tested** (new Q40 to Q42). An off-price buyer needs at least about $1.15bn to enter the top three. Below that it lowers concentration. Verdict: very unlikely.
6. **Shift inside the top three (Dick's up, Foot Locker down)** is now a separate candidate (#4a), ruled out because the sum is unchanged.
7. **FY25 returns and discounts sized** from the sales-related reserve (new Table F, candidate #11): 0 to +0.84 pt of the FY26 rebound and 0 to 0.28 pt of FY25 depression.
8. **"Channel mix is not a cause"**: the note now states that #1 is an accounting term with Direct-strategy causes. Demand migrating to the top three appears only in #4, so the two do not overlap.
9. **Source-file fix:** the local file `dl/conc/NASDAQ_HIBB_2023.pdf` is a 404 page, and the content came from `NASDAQ_HIBB_cur.pdf`. The cited URL (annualreports.com .../AnnualReports/PDF/NASDAQ_HIBB_2023.pdf) does resolve to the FY2023 10-K. It was re-downloaded to `dl/conc2/NASDAQ_HIBB_2023_FY2023_10K.pdf` (byte-identical to `_cur`).
10. **New candidate-#3 bounds** (Academy 2024 and 2025, Kohl's 2025) and the FY26 slot test (Table G) narrow which accounts can be the new #3.

**Revision 1:** original note (backup at `rh/conc/concentration_v1_backup.md`).

## Independent verification log
- Oct 13, 2026: **Hibbett's 73.7% Nike share (FY2024 10-K) could not be confirmed.** The FY2024 10-K download was an empty stub and no other copy was reachable. The latest Hibbett 10-K available (FY2023) states "Our largest vendor, Nike, represented 69.9%, 61.0%, and 65.0% of our purchases for Fiscal 2023, Fiscal 2022 and Fiscal 2021." Using 69.9% scales the JD-Hibbett contribution down about 5%, to about 2.9 to 4.0 points. The conclusion (largest identified within-wholesale driver) is unchanged.

## Cross-note corrections (from 09_cross_note_critic_review.md)
- Weak inputs: "JD was the FY24 #3" rests on Finish Line's FY2018 vendor share (66%, before the JD takeover), so the largest identified driver depends on a stale input. Hibbett's 73.7% could not be confirmed (see verification log).
- Critic cap: top-3 U.S. dollars rose $772M to $1,173M from FY25 to FY26, so non-top-3 NA wholesale rose only $301M to $702M of the $1,474M.
