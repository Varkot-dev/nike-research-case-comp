# G1: Product purchase obligations (PPO) as Nike's only forward demand signal

Date: Oct 15 2026. Series file: `G1_purchase_obligations_series.csv` (same folder). Tags: OPENED = read in the filing text, SNIPPET = search result only, DERIVED = my arithmetic from OPENED inputs. All filings fetched from the investors.nike.com mirror and split with `scripts/sec_pipeline/topages.py`; every value in the CSV was machine-checked to appear on its cited page. Page numbers are printed pages (seq page in the CSV).

## Bottom line

**Not a smoking gun.** The FY26 10-K PPO of about $4.9B ($4.7B within 12 months) is a real, low reading, but (1) PPO has had no usable relationship with next-full-year revenue (correlation -0.06 over FY16 to FY25, 0.38 excluding FY20 and FY21, n=10, DERIVED); (2) the one year-end figure everyone would compare against ($7.9B at FY25) was an error Nike corrected to about $5B; so the true change is about -2%, not -38%; (3) the ratio-implied FY27 revenue range ($35B to $52B, centre $39.8B to $40.4B) is far wider than the -7% to -9% guide ($42.2B to $43.2B), so the signal cannot say whether the guide is too high or too low. It leans mildly toward "guide could be light" but with a standard error of about 7.5 points of growth. It says nothing direct about FY28 (PPO covers only about 4 to 5 months of purchases).

## 1. The series (all USD millions unless stated; OPENED)

PPO as printed, within-12-month amount, then next-year ratios (DERIVED). FY15 to FY21 come from the Contractual Obligations table (PPO is 100% in year 1 every year). FY22 to FY26 are narrative in MD&A Liquidity, printed in $ billions to one decimal.

| FY (May 31) | PPO printed | PPO within 12m | PPO % next-FY revenue | PPO % next-FY cost of sales | PPO % inventory | PPO % next Q1 purchases (DERIVED proxy) | Source (printed p.) |
|---|---|---|---|---|---|---|---|
| 2015 | 3,735 | 3,735 | 11.5% | 21.5% | 86% | 83% | FY15 10-K p. 37 |
| 2016 | 4,149 | 4,149 | 12.1% | 21.8% | 86% | 83% | FY16 10-K p. 39 |
| 2017 | 4,521 | 4,521 | 12.4% | 22.1% | 89% | 86% | FY17 10-K p. 38 |
| 2018 | 4,566 | 4,566 | 11.7% | 21.1% | 87% | 83% | FY18 10-K p. 36 |
| 2019 | 5,203 | 5,203 | 13.9% | 24.6% | 93% | 87% | FY19 10-K p. 39 |
| 2020 | 4,234 | 4,234 | 9.5% | 17.2% | 57% | 82% | FY20 10-K p. 45 |
| 2021 | 6,448 | 6,448 | 13.8% | 25.6% | 94% | 101% | FY21 10-K p. 46 |
| 2022 | 6,600 | 6,600 | 12.9% | 22.8% | 78% | 79% | FY22 10-K p. 46 |
| 2023 | 6,400 | 6,400 | 12.5% | 22.5% | 76% | 86% | FY23 10-K p. 46 |
| 2024 | 5,700 | 5,700 | 12.3% | 21.5% | 76% | 81% | FY24 10-K p. 48 |
| 2025 | **7,900 printed; about 5,000 corrected** | 7,900 / 5,000 | 10.8% (on 5.0) | 18.9% | 67% | 68% | FY25 10-K p. 47; 8-K 2025-07-28 Item 8.01 |
| 2026 | 4,900 | **4,700** | n/a (FY27 open) | n/a | 65% | 72.5% (Q1 FY27 actual) | FY26 10-K p. 46 |

Denominators (OPENED, each year's own 10-K; revenue / cost of sales page then inventory page): FY15 30,601 / 16,534 (p. 21), inv 4,337 (p. 18); FY16 32,376 / 17,405 (p. 22), 4,838 (p. 19); FY17 34,350 / 19,038 (p. 22), 5,055 (p. 19); FY18 36,397 / 20,441 (p. 21), 5,261 (p. 18); FY19 39,117 / 21,643 (p. 26), 5,622 (p. 22); FY20 37,403 / 21,162 (p. 56), 7,367 (p. 25); FY21 44,538 / 24,576 (p. 31), 6,854 (p. 59); FY22 46,710 / 25,231 (p. 31), 8,420 (p. 58); FY23 51,217 / 28,925 (p. 31), 8,454 (p. 57); FY24 51,362 / 28,475 (p. 33), 7,519 (p. 59); FY25 46,309 / 26,519 (p. 32), 7,489 (p. 58); FY26 46,398 / 26,487 (p. 32), 7,501 (p. 57). FY19 pages are sequential minus 2 because the footer was not detected.

Next-Q1 purchases proxy = Q1 cost of sales + (August inventory minus May inventory), from each Q1 10-Q (income statement p. 1 or 4, balance sheet p. 3). It ignores reserves and FX, so treat as approximate (DERIVED). Q1 FY27 (10-Q p. 1 and 3): revenue 11,213, cost of sales 6,415, inventory 7,846 vs 7,501, so purchases about 6,760, which is -8.7% vs 7,402 in Q1 FY26.

### Endorsement, other purchase and operating lease commitments (OPENED)

| FY | Endorsement total | within 12m | Other purchase obl. total | within 12m | Operating leases (undiscounted) | Year 1 | Endorsement % next-FY rev (DERIVED) |
|---|---|---|---|---|---|---|---|
| 2015 | 6,192 | 1,009 | n/a | n/a | 2,974 | 447 | 19.1% |
| 2016 | 9,420 | 1,198 | 772 | 384 | 3,231 | 491 | 27.4% |
| 2017 | 9,850 | 1,323 | 1,915 | 1,000 | 3,905 | 537 | 27.1% |
| 2018 | 10,501 | 1,391 | 2,646 | 1,437 | 3,965 | 589 | 26.8% |
| 2019 | 10,209 | 1,382 | 2,760 | 1,331 | 3,732 | 553 | 27.3% |
| 2020 | 9,342 | 1,330 | 2,227 | 1,085 | 3,784 | 550 | 21.0% |
| 2021 | 8,392 | 1,502 | 2,736 | 1,347 | 3,745 | 534 | 18.0% |
| 2022 | 7,600 | 1,300 | 3,100 | 1,700 | 3,529 | 491 | 14.8% |
| 2023 | 7,600 | 1,300 | 3,300 | 1,700 | 3,588 | 506 | 14.8% |
| 2024 | 10,600 | 1,700 | 3,500 | 1,900 | 3,367 | 572 | 22.9% |
| 2025 | 16,200 | 1,600 | 3,100 | 1,900 | 3,338 | 565 | 34.9% |
| 2026 | 15,500 | 1,700 | 2,400 | 1,600 | 3,592 | 564 | n/a |

FY15 and FY16 other purchase obligations were not a separate line in FY15. Lease pages: FY15 to FY21 in the contractual table (same pages as above); FY22 p. 90, FY23 p. 88, FY24 p. 89, FY25 p. 87, FY26 p. 88. FY26 lease schedule: FY27 564, FY28 553, FY29 512 (p. 88). Operating leases and endorsements are fixed-cost commitments, not demand signals; they matter for deleverage: endorsement plus lease payments within 12 months are 4.9% of FY26 revenue (2,264 / 46,398, DERIVED) vs 3.5% at FY23, so if FY27 revenue falls 8% the same dollars are about 5.3% of revenue.

### 10-Q disclosure FY16 to Q1 FY27 (OPENED, all 30 prior 10-Qs plus 4 FY26/FY27 10-Qs searched in full text)
PPO is never updated in any 10-Q. The only quarterly contractual update is endorsement obligations: Q2 FY16 and Q3 FY16 (tables), Q2 FY24 $9.1B (p. 41), Q3 FY24 $9.9B (p. 43), Q2 FY25 $15.9B (p. 38), Q3 FY25 $15.1B (p. 41). The FY26 10-Qs (Q1 to Q3) and Q1 FY27 10-Q say nothing on PPO or endorsements beyond FX remarks. So the next PPO print is the FY27 10-K (about July 2027).

## 2. Wording changes (OPENED)

- "We generally order product at least four to five months in advance of sale" is identical in FY15 through FY26. Lead time wording did not change. Source basis changed: FY15 to FY17 "based primarily on futures orders", FY18 onward "advanced orders" from wholesale customers plus internal DTC orders; FY20 on "direct to consumer operations".
- FY15 10-K: PPO "exclude product purchase liabilities included in Accounts payable" (p. 37 note 3). That language is gone from FY16 on.
- FY22 to FY25: same paragraph, "$X billion, all of which are payable within the next 12 months".
- **FY25 10-K (p. 47): $7.9B. 8-K filed July 28 2025 (Item 8.01, p. 2): "voluntarily filing ... to correct an error ... The amount was overstated ... As corrected ... approximately $5 billion, all of which are payable within the next 12 months."** No cause given. This is the biggest wording event in the series and is not in the repo's earlier notes (the facts CSV holds both figures).
- FY25 endorsement: now "including associated marketing commitments" (first in the Q2 FY25 10-Q, $15.9B vs $9.9B in Q3 FY24 and $10.6B in FY24, a definitional widening plus new contracts). Other purchase obligations lost the phrase "marketing commitments associated with endorsement contracts" in the FY25 10-K. Combined endorsement plus other: FY24 14.1B (10.6+3.5) to FY25 19.3B (16.2+3.1) to FY26 17.9B (15.5+2.4), DERIVED.
- **FY26 10-K (p. 46): first time Nike splits the total from the 12-month amount: about $4.9B total, about $4.7B within 12 months** (so about $0.2B extends beyond 12 months), and "approximately" now precedes every figure. Other purchase obligations: "technology investments, external service and marketing commitments" (construction dropped, "external" added).
- Nothing changed in FY24 vs FY23 text. Q1 FY27 10-Q: no change.

## 3. What FY26 implies for FY27 and FY28 (DERIVED)

Guide as supplied: FY27 revenue -7% to -9% of $46,398M = $43,150M to $42,222M (midpoint -8% = $42,686M, matching D1; note D1 flags that Nike has not defined the range). Nike's own Q4 FY26 call text (OPENED, official transcript, CFO prepared remarks) says "take actions to tighten buys, reduce future sell-in and manage inventory. This will result in revenue moderating, but also higher gross margins" and for Q1 "down low to mid-single digits"; Q1 actual was -4% (10-Q p. 1). That is management opinion, labelled as such.

1. **PPO % next-FY revenue** FY15 to FY25: mean 12.1%, median 12.3%, range 9.5% to 13.9%, sd 1.2 points. Implied FY27 revenue from $4.9B: $40.4B at mean, $39.8B at median (-13% to -14%), $35.2B at the max ratio, $51.5B at the min ratio; excluding FY20/FY21 range $35.2B to $45.5B. Using $4.7B (12-month): $38.2B to $38.8B. The guide midpoint requires 11.5% (4.9/42.686), inside the band and below the median. So PPO leans lower than the guide, but only if the FY22 to FY24 style ratio still holds.
2. **PPO % next-FY cost of sales**: mean 21.8%, range 17.2% to 25.6%. Guide-implied FY27 cost of sales (Q1 FY27 gross margin 42.8%, 10-Q p. 1 text) is about $24.4B, so required ratio is 20.1%, between the FY25 corrected reading (18.9%) and the median.
3. **Growth regression** (PPO yoy vs next-year revenue yoy, FY16 to FY25, n=10): slope -0.02, r = -0.06; excluding FY20 and FY21: r = 0.38, slope 0.26, predicted FY27 growth +1.1% at PPO -2%, residual sd 7.5 points. Zero predictive value for the full year. PPO yoy vs next-Q1 purchases growth r = 0.65 (slope 0.45), next-H1 revenue growth r = 0.47.
4. **Short horizon test**: PPO covered 79% to 87% of next-Q1 purchases in 10 of 11 years FY15 to FY25 (FY21 101% was supply-chain double ordering). FY25 corrected was 67.5% and FY26 is 72.5%. At the historical 83% norm, $4.9B would have implied about $5.9B of Q1 FY27 purchases; actual was about $6.76B (+15% above). So PPO understated Q1 inflow relative to history; weakness in PPO did not translate into proportionally weaker buying. Q1 FY27 purchases were -8.7% yoy vs revenue -4% and cost of sales -5%, with inventory build +345M vs +625M a year earlier.
5. **H1 revenue**: PPO % next-H1 revenue averaged 24.2% (FY15 to FY24); $4.9B / 24.2% = $20.3B H1 FY27 (-16% yoy) vs actual Q1 of $11.2B, which would force Q2 to $9.1B (-27%). At the FY25 ratio (20.7%) H1 is $23.7B (-2%). Implausible extremes; again unresolved.
6. **Futures calibration (the old signal)**: PPO / Jun to Nov futures orders = 27.7% (FY15, futures $13.5B, 10-K p. 3), 27.8% (FY16, $14.9B, p. 3 and 25), 30.8% (FY17, $14.7B, p. 3). Nike stopped reporting futures after FY17, so nothing today can be converted.
7. **FY28**: nothing. PPO covers 4 to 5 months of buys (disclosed lead time), so FY28 (starting June 2027) is beyond its horizon; no FY28 revenue can be inferred. The only contractual FY28 data are fixed costs: lease payments 553 (p. 88), endorsement amounts for FY28 not disclosed in the new narrative format (the FY21 table last gave yearly endorsement amounts).

## 4. Alternatives tested for the FY26 PPO level (and what ruled them out)

| Alternative | Test | Result |
|---|---|---|
| A1 FY25 comparison is an error, so a "-38% collapse" is false | 8-K Item 8.01 | CONFIRMED. True yoy about -2% (4.9 vs about 5.0, rounded; plus or minus 0.25B each) |
| A2 Timing of commitments (year-end calendar) | PPO / next-Q1 purchases stable at 79% to 87% FY15 to FY24 | Not a driver before FY25; FY25 and FY26 sit at 68% and 72.5%. Timing within the quarter cannot be tested (no quarterly PPO). Partial |
| A3 Lead-time change | Wording unchanged ("four to five months") FY15 to FY26 | Wording ruled out; actual practice not ruled out. The drop in coverage to 68% to 73% is what a shorter effective lead time or more reactive in-season buying would produce. Surviving |
| A4 Mix shift to shorter-lead items (apparel) | NIKE Brand footwear share 67.8% FY24, 66.1% FY25, 65.4% FY26 (10-K FY26 p. 32; FY24 p. 34, DERIVED) | Shift of 2.4 points to apparel/equipment. Even assuming apparel carried zero PPO, it cuts PPO about 3.5% (2.4/67.8), against a decline from $6.4B (FY23) to $4.9B (-23%). Ruled out as the main cause (at most 3.5 of 23 points) |
| A5 Supplier finance changes | Note 19: confirmed outstanding $1.1B (FY26), $1.1B (FY25), $0.84B (FY24) (10-K FY26 p. 89; FY25 10-K Note, FY24 10-K); confirmed invoices $11.5B (FY26) vs $11.8B (FY25), paid $11.5B both (FY26 10-K p. 89) | Invoice flow -2.5% yoy while purchases proxy falls; programs affect payment timing, not open POs, and PPO text covers open purchase orders. Ruled out |
| A6 Reporting method change at Nike | FY25 overstatement of $2.9B unexplained | Cannot rule out a break in method FY25 to FY26, nor that FY22 to FY24 had a milder version of the same error. Partial: FY22 to FY24 coverage 79% to 86% is consistent with FY15 to FY20 (82% to 87%), which argues the older series was clean. Surviving |
| A7 Deliberate supply cuts vs weaker sell-through | Filings cannot separate. Management (opinion): "tighten buys, reduce future sell-in" (Q4 FY26 call); inventory flat at $7.5B yoy (10-K p. 57) and 103 days of cost of sales vs 95 days FY15 and FY19 (DERIVED) | Not separable from PPO. Q1 FY27 inventory +$345M vs +$625M in Q1 FY26 shows tighter buying than last year. Surviving |
| A8 Price per unit (tariffs raise cost per unit) | Would raise PPO dollars per unit | Works against the drop, so units are down by more than dollars if tariff costs rose. Cannot quantify; Nike discloses no unit PPO. Partial |
| A9 FX | PPO is in USD at purchase cost | No disclosure of FX in PPO; not tested. Partial |

Two explanations survive for why the sign of PPO is "low": deliberate cuts of buys against high inventory (A7) and shorter effective lead times (A3). Data that would decide: Q2 FY27 10-Q purchases proxy and PPO in the FY27 10-K; supplier shipments (Feng Tay, Yue Yuen, Pou Chen, Vietnam and Indonesia export data); Nike's own statement of order-book coverage.

## 5. Routes tried (rule: at least five before calling anything unresolved)

For "what drove the FY25 PPO error and is the FY26 figure comparable":
1. FY25 10-K and FY26 10-K text, full read of Liquidity section: worked (numbers), no cause given.
2. 8-K July 28 2025: worked, confirms error, no cause.
3. Web search for analyst or press explanation: blocked/partial (only the 8-K itself surfaced).
4. Cross-check against independent flow data (Q1 purchases proxy from 10-Qs): worked, FY25 printed 7.9 would be 107% coverage, impossible against 79% to 87% history; supports correction.
5. XBRL companyfacts for a PPO tag: not checked (Nike does not tag this narrative figure; text is outside financial statements). Not tried.
6. Q4 FY26 call transcript (s1.q4cdn.com PDF, OPENED): worked for management direction (tighten buys), no PPO commentary.
7. Third-party supplier shipments: not done here; see `research_notes/Long or short cruxes/supplier_nowcast.md` (Feng Tay Nike orders -9% to -12% for Jul to Sep; Yue Yuen 1H26 pairs -6.4%, per that note, not re-verified by me).
8. 10-Qs FY16 to Q1 FY27 for interim PPO: worked (none exist).

## 6. What I could not verify

- Cause of the FY25 $2.9B overstatement, and whether the FY26 $4.9B uses the corrected method (no filing says).
- A quarterly PPO series (does not exist).
- The "-7% to -9%" guide itself: taken from the task statement and D1 line 30 (an assumption there). The Q4 FY26 call text I opened says Q1 low to mid single digit decline; I did not locate a full-year FY27 percentage in the filings or transcript text I grepped.
- Whether FY22 to FY24 PPO were consistent with the corrected FY25 method (coverage test suggests yes, not proof).
- Revenue and cost of sales FY19 printed page numbers (footer not detected; derived from sequential offset).
- Unit-level PPO, FX, and tariff effects.

## 7. Verdict

Fact-level: FY26 PPO of about $4.9B is -2% against the corrected FY25 figure, is 65% of inventory (lowest since FY20's 57%), and is about 11.5% of the guide-midpoint revenue. It supports the "FY27 revenue is not being protected by order book" reading but cannot size it. It does not decide long or short on its own. The extra finding for the thesis is the FY25 correction: any prior note quoting $7.9B should be changed to about $5B.

## Parent check (Oct 15, 2026)
The FY27 revenue guide this note could not find is in the Q1 FY27 call transcript, page 11 (`data/hunt/earnings_calls/transcripts/Q1FY27.txt`, OPENED): "For fiscal '27, we currently expect revenues to decline in the high single-digit range." The -7% to -9% used in D1 and the deck is the team's reading of "high single-digit"; Nike did not state a numeric range or whether it is reported or currency-neutral. The call also states the Q2 headwind of about 400 bps from lapping EMEA Cyber Week promotions and North America sell-in, and the adjusted EPS range of $1.15 to $1.35 excluding about $0.15 of Pace charges (page 12).
