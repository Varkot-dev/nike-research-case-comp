# Why did North America gross margin rise while the other regions fell? (FY2024 to Q1 FY2027)

> **Status: DRAFT (Oct 13, 2026).** Produced by the multi-agent investigation (one investigator, two adversarial reviewers, one revision round). Sources are cited inline; independent spot-check against source documents is in progress and results will be logged at the end of this file. Treat figures as provisional until marked verified.


**Prepared:** October 13, 2026 (revision 2, same day). Scratch research note; not yet merged into the repo.
**Inputs reused from the repo:** `data/nike_region_profitability.csv`, `research_notes/06_region_margin_product.md` (Section 2 regional gross margin table), `research_notes/09_channel_margin_test.md` (Direct vs wholesale price spread, Test 1).
**Filings read in full for this note (page text saved under `scratchpad/rh/dl/nike/pages/`):** FY2025 and FY2026 10-Ks; Q1 FY2025 to Q3 FY2025 and Q1 FY2026 to Q1 FY2027 10-Qs; Nike's prepared earnings call remarks for Q4 FY2025 to Q1 FY2027 (`scratchpad/rh/dl/transcripts/`). The cached remarks are prepared remarks only; the analyst Q&A was not available.
**Arithmetic:** `scratchpad/rh/na/calc.py` (output `calc_out.txt`) for the base tables, and `scratchpad/rh/na/calc2.py` (output `calc2_out.txt`) for every figure added in revision 2.

Labels used: **filing** (10-K or 10-Q), **Nike release** (Nike's own prepared call remarks PDF), **secondary** (non-Nike source), **my arithmetic**, **estimate** (my arithmetic that also needs an assumption, which is stated), **opinion** (my inference).

---

## 0. Bottom line

1. **The reported FY2024 to FY2026 rise (44.4% to 45.6%, +120 bps) depends on the IEEPA refund.** Nike booked the North America share of the refund ($965M) in Q4 FY2026 Cost of sales. That is 470 bps of FY2026 North America revenue (my arithmetic).
   - Excluding the refund but keeping all tariffs, FY2026 North America margin was 40.9%, **-350 bps** vs FY2024 (my arithmetic). That is a larger fall than EMEA (-240 bps) and close to APLA (-390 bps).
2. **The refund is at least as large as the IEEPA cost it reverses inside FY2026, never smaller (corrected in revision 2).**
   - Nike recognized the recovery of *all* IEEPA tariffs paid ($986M; $302M received plus $684M receivable) in Cost of sales.
   - Some of the tariffs paid were never FY2026 expense:
     - tariffs on goods sold before June 1, 2025, expensed in FY2025 (call this E25);
     - tariffs on goods still in inventory at May 31, 2026 (call this I26).
   - So the refund minus FY2026 IEEPA expense equals E25 plus I26, which is zero or positive. The reported 45.6% therefore **overstates** a "no IEEPA" margin, by:
     - a hard upper bound of 111 bps, which gives a floor of 44.5%;
     - a central estimate of 7 to 41 bps, which gives 45.2% to 45.5% (estimate, Section 2c).
3. **On a "no new tariffs at all" basis, the FY2026 margin is about 45.8% (central), with a range of 45.4% to 46.3%.** That is **+100 to +190 bps vs FY2024**, central +143 bps (estimate, Section 2b).
   - This figure no longer uses the circular Q4 plug. It removes the refund, adds back every FY2026 tariff dollar (IEEPA and the Section 122 replacement), and takes Q4 from Nike's own Q4 guidance.
   - Because the FY2026 tariffs are added back directly, E25 and I26 drop out of this measure.
4. **What drives the underlying rise, vs FY2024, is lower cost per unit, not price (new in revision 2).**
   - NA footwear and apparel revenue per unit fell about 2.5% from FY2024 to FY2026 (my arithmetic from Nike's ASP bullets). The shift to wholesale alone would have cut it by about 3.3% (estimate), so price, product mix and discounts net of channel added only about +0.8%.
   - To get from 44.4% to about 45.8% anyway, cost per unit excluding new tariffs must have fallen about **4% to 6%** (estimate). Nike names the components:
     - lower product costs (ocean freight, input costs and product mix in FY2025; product mix and "lower product costs" in FY2026);
     - lower warehousing and logistics costs.
   - Nike does not size them for North America, so how the cost reduction splits between them is **unresolved**.
5. **Lapping the FY2025 Win Now clean-up explains FY2025 to FY2026, not FY2024 to FY2026 (logic correction).** FY2024 is the base year, so a trough in FY2025 cannot by itself lift FY2026 above FY2024.
6. **Why the other regions fell and North America did not:**
   - Greater China and APLA name standard-rate FX as the main cause in FY2025 and FY2026, and EMEA names it in FY2026.
   - FX *can* reach North America, through Canada and through the factory currency adjustment program. Both moved against NA over this period: CAD averaged 1.351 per USD in FY2024 and 1.379 in FY2026 (secondary data, my arithmetic).
   - So FX worked **against** NA's rise and cannot explain it. Its NA size is undisclosed and probably small (opinion).
7. **Q1 FY2027 (+110 bps to 43.4%) is not a clean comparison.**
   - The Q1 FY2026 base carried IEEPA cost (about $117M to $180M, estimate) that was later refunded.
   - Q1 FY2027 carries the Section 122 replacement tariff, plus any refunded IEEPA cost still flowing out of May 31, 2026 inventory (estimate: $0 to $58M).
   - Nike attributes NA's higher Q1 FY2027 product cost to "product mix", not tariffs. The tariff load in each quarter is undisclosed, so the underlying Q1 change is **unresolved**.
   - The question's premise also fails this quarter: EMEA (+140 bps) and Greater China (+30 bps) rose too.

---

## 1. Candidate explanations: verdicts

| # | Candidate | Verdict | Quantified contribution (FY24 to FY26 unless stated) | Deciding evidence |
|---|---|---|---|---|
| 1 | **IEEPA refund booked in Q4 FY26** ($965M in NA) | **Supported** as what makes the reported FY26 figure rise. | +470 bps of FY26 NA revenue. Without it, FY24 to FY26 is -350 bps (my arithmetic). | FY26 10-K p. 30 and p. 61. Q4 FY26 remarks PDF pp. 8 to 9. |
| 2 | **Refund covers tariffs that were not FY26 expense** (E25 plus I26: an out-of-period credit) | **Partly supported, small.** The sign is now fixed: the effect is zero or positive. Revision 1 called it "ruled out as material". | Central estimate $15M to $85M, or +7 to +41 bps of FY26 NA revenue. Hard upper bound $228M (+111 bps). No-IEEPA FY26 NA margin: 45.2% to 45.5% (central), floor 44.5% (estimate). | Refund = "recovery of IEEPA tariffs paid", and $302M + $684M = $986M (FY26 10-K p. 30). About $1.0B paid (Q3 FY26 10-Q p. 26). Duties sit in inventory cost (FY26 10-K p. 63). IEEPA collection stopped for entries on or after February 24, 2026 (secondary: GHY). The bound comes from the inventory-flow calibration in Section 2c. |
| 3 | **Tariff cost itself** (IEEPA, then Section 122 from February 24, 2026) | **Supported** as the cause of the Q1 to Q3 FY26 declines. Section 122 cost in Q4 FY26 was not refunded. | NA tariff estimates: Q1 about $117M (floor; possibly up to $180M); Q2 $293M; Q3 $327M; Q4 about $274M (Nike's Q4 guide, includes Section 122). FY26 total about $1,011M, range $920M to $1,111M (estimate). | Q2 FY26 remarks PDF p. 9 (520 bps). Q3 FY26 remarks PDF p. 11 (650 bps) and p. 14 (Q4 guide 250 bps). Q2 FY26 remarks PDF p. 8 (FY26 "gross headwind of approximately 320 basis points"). |
| 4 | **Lower cost per unit, excluding new tariffs** (base product cost, freight, input costs, product-mix cost, W&L) | **Supported as the main driver** of the underlying FY24 to FY26 rise. | Cost per unit ex new tariffs -4.2% to -5.8% FY24 to FY26 (estimate, Section 2d). Split between components unresolved. | NA bullets: FY25 "lower product costs" (FY25 10-K p. 38); FY26 "lower product costs, lower warehousing and logistics costs" (FY26 10-K p. 37). Q1 FY25 consolidated "lower ocean freight rates and lower product input costs" (Q1 FY25 10-Q p. 22). Q2 FY25 NA "lower product costs, reflecting product mix and lower product input costs" (Q2 FY25 10-Q p. 29). |
| 5 | **Ocean freight deflation** (part of #4) | **Partly supported** for FY24 to FY25. **Not tested** for FY25 to FY26: no FY26 Nike filing mentions freight. | Not sized for NA. Consolidated Q1 FY25 product cost +120 bps, "primarily due to lower ocean freight rates and lower product input costs". | Q1 FY25 10-Q p. 22. No freight mention in any FY26 or Q1 FY27 gross margin bullet (searched all nine filings). |
| 6 | **"Lower product costs" in the FY26 NA bullet is really the net refund** (reviewer alternative) | **Partly supported, bounded.** It cannot be the main FY25 to FY26 driver. | Net tariff/refund effect on FY25 to FY26 = 965 - FY26 tariffs + E25 = -$146M to +$85M, i.e. -71 to +42 bps of the +210 bps (estimate). So at least about 170 bps of the FY25 to FY26 gain is non-tariff. | Section 2c. The 9M FY26 NA bullet has no "lower product costs" (Q3 FY26 10-Q p. 34); the full-year bullet does (FY26 10-K p. 37). The Q4 swing therefore includes the refund. |
| 7 | **Channel mix (shift to wholesale)** | **Supported as a net headwind**, partly offset by W&L savings. Revision 1 listed only the W&L benefit. | ASP effect of the channel shift at constant channel margins: -150 to -177 bps (estimate). W&L offset: at most about +90 bps (upper bound if all consolidated W&L savings were NA). Net -60 to -177 bps (estimate). | NA Direct share 48.6% to 41.7% (my arithmetic). Note 09 Test 1: Direct revenue was 1.654x wholesale value in FY24, a channel gross margin gap of 21.7 to 25.7 points. FY26 10-K p. 37: footwear "Lower ASP per pair was primarily due to channel mix". |
| 8 | **Strategic pricing, product mix in price, lower discounts (ASP)** | **Partly supported, small vs FY24.** It is larger FY25 to FY26, where it comes mostly from lapping Q4 FY25 liquidation. | Revenue per unit, footwear plus apparel: FY25 -2.42%, FY26 -0.05%, cumulative -2.47% (my arithmetic). Channel mix alone explains about -3.25%, leaving about +0.8% for price, product mix and discounts (estimate). | FY25 10-K p. 38 and FY26 10-K p. 37 ASP bullets. 9M FY26 NA ASP was lower (Q3 FY26 10-Q p. 34), but full-year ASP was higher, so the gain sits in Q4. Q4 FY25 remarks PDF p. 10 ("higher discounts to liquidate aged inventory"). |
| 9 | **Lapping the FY25 clean-up** (discounts, liquidation, obsolescence) | **Supported for FY25 to FY26. Not an explanation for FY24 to FY26.** | FY24 to FY25 NA -90 bps "primarily due to lower ASP and higher inventory obsolescence reserves". Recovering that only returns NA to the FY24 level. | FY25 10-K p. 38; FY26 10-K p. 37; Q2 and Q3 FY26 10-Qs (lower obsolescence reserves). |
| 10 | **Category mix** (Performance up, Sportswear and classic franchises down more than $2B) | **Partly supported. Not separable** from #4 and #8, because Nike books product mix in both ASP and product cost. | Not quantified. Apparel ASP rose "primarily due to product mix" (FY26). Q1 FY26 NA product costs "flat as higher tariffs were offset primarily by product mix". | FY26 10-K p. 37; Q1 FY26 10-Q p. 25; Q4 FY26 remarks PDF p. 8 (classics reduced "by more than $2 billion"). |
| 11 | **FX** (Canada standard rates; factory currency adjustment program) | **Ruled out as a cause of the rise**: wrong sign. Revision 1's "cannot hit NA" is withdrawn. | CAD per USD averaged 1.3513 (FY24), 1.3955 (FY25), 1.3785 (FY26), so CAD was weaker in FY26 than FY24. That raises Canadian product cost, a headwind. A weaker USD in 2025 also raises USD inventory cost under the factory program, another headwind. Size undisclosed. Illustration: if Canada were 10% of NA revenue, about 11 bps (estimate). | FY26 10-K p. 37 (NA FY25 vs FY24 revenue -9% reported vs -8% currency-neutral, so NA has non-USD sales). FY26 10-K p. 85 (standard rates). FY26 10-K p. 43 (a weakening USD "increases our inventory cost"). FRED DEXCAUS (secondary). |
| 12 | **Restatement or segment reclassification** | **Ruled out.** | 0 | FY24 NA gross profit is $9,497M in both the FY25 10-K (p. 38) and the FY26 10-K (p. 37). |
| 13 | **Supply chain severance (Q4 FY26)** | **Supported as a small headwind.** | Not sized for NA. | Q4 FY26 remarks PDF p. 9. |

**Surviving explanation.** The underlying FY24 to FY26 North America gain is about **+100 to +190 bps** on a no-new-tariff basis (central +143). It is a per-unit cost story:
- North America sold a mix that cost less to make and land;
- some of the drop is freight and input-cost deflation that Nike cited in FY2025;
- lower warehousing and logistics costs as volume moved to wholesale.

Together these more than offset the price drag of that same channel shift (#4, #5, #7). Strategic pricing and product mix in price add a small positive (#8). On top of the underlying gain, the reported 45.6% carries:
- a small out-of-period IEEPA credit (#2, central +7 to +41 bps);
- an unrefunded Section 122 tariff cost in Q4 (inside #3).

The other regions fell mainly because of standard-rate FX (#11), which hit them hard and hit NA only mildly, in the same adverse direction. The share of the per-unit cost decline due to freight, input costs, product mix and W&L is **unresolved**: Nike publishes no NA bridge.

---

## 2. Data tables built

### 2a. North America quarterly gross margin, Q1 FY2025 to Q1 FY2027 ($M)

| Quarter | Revenue | Cost of sales | Gross profit | GM reported | GM ex IEEPA refund | YoY reported (bps) | Source |
|---|---|---|---|---|---|---|---|
| Q1 FY25 | 4,826 | 2,627 | 2,199 | 45.6% | 45.6% | +180 (stated) | Q1 FY26 10-Q p. 25 (comparative); Q1 FY25 10-Q p. 25 for the bps |
| Q2 FY25 | 5,179 | 2,896 | 2,283 | 44.1% | 44.1% | flat (stated) | Q2 FY26 10-Q p. 30; Q2 FY25 10-Q p. 29 |
| Q3 FY25 | 4,864 | 2,766 | 2,098 | 43.1% | 43.1% | -210 (stated) | Q3 FY26 10-Q p. 33; Q3 FY25 10-Q p. 32 |
| Q4 FY25 | 4,703 | 2,767 | 1,936 | 41.2% | 41.2% | n/a | my arithmetic: FY25 (FY25 10-K p. 38) minus 9M FY25 (Q3 FY26 10-Q p. 33) |
| Q1 FY26 | 5,020 | 2,897 | 2,123 | 42.3% | 42.3% | -330 | Q1 FY26 10-Q p. 25 |
| Q2 FY26 | 5,633 | 3,335 | 2,298 | 40.8% | 40.8% | -330 | Q2 FY26 10-Q p. 30 |
| Q3 FY26 | 5,026 | 3,036 | 1,990 | 39.6% | 39.6% | -350 | Q3 FY26 10-Q p. 33 |
| Q4 FY26 | 4,832 | 1,892 | 2,940 | 60.8% | 40.9% | +1,968 reported; **-29 ex refund** | my arithmetic: FY26 (FY26 10-K p. 37) minus 9M FY26 (Q3 FY26 10-Q p. 33); refund from FY26 10-K p. 30 |
| Q1 FY27 | 5,127 | 2,903 | 2,224 | 43.4% | 43.4% | +110; **-219 vs Q1 FY25** | Q1 FY27 10-Q p. 26 |
| FY24 | 21,396 | 11,899 | 9,497 | 44.4% | 44.4% | | FY26 10-K p. 37 |
| FY25 | 19,572 | 11,056 | 8,516 | 43.5% | 43.5% | -90 | FY25 10-K p. 38 |
| FY26 | 20,511 | 11,160 | 9,351 | 45.6% | **40.9%** | +210 reported; -263 ex refund | FY26 10-K p. 37 |

Check: Q1 to Q3 sums equal the 9M figures exactly for both FY25 and FY26 (calc_out.txt).

**Implied FY2024 quarters** (my arithmetic, approximate because Nike rounds bps to 10). Nike did not disclose segment gross margin in the FY2024 10-Qs, so these come from the FY2025 10-Q year-on-year bps:

| Quarter | Revenue | Implied GM | How |
|---|---|---|---|
| Q1 FY24 | 5,423 | 43.8% | 45.6% minus "expansion of 180 basis points" (Q1 FY25 10-Q p. 25) |
| Q2 FY24 | 5,625 | 44.1% | "Gross margin was flat" (Q2 FY25 10-Q p. 29) |
| Q3 FY24 | 5,070 | 45.2% | 43.1% plus "contraction of 210 basis points" (Q3 FY25 10-Q p. 32) |
| Q4 FY24 | 5,278 | about 44.5% | FY24 gross profit 9,497 minus implied Q1 to Q3 gross profit |

### 2b. No-new-tariff FY2026 NA margin, built without a plug (revision 2; replaces the circular table)

Revision 1 set the Q4 FY26 tariff to "965 minus Q1 to Q3". That forced the full year to 45.6% by construction, so the result was circular. This table takes every quarter's tariff from a separate Nike statement instead. The FY26 total is then free to differ from the refund.

| Quarter | NA tariff in Cost of sales (estimate) | Basis (each from a separate source) | NA GM ex refund, ex all new tariffs |
|---|---|---|---|
| Q1 FY26 | $117M (floor; range $100M to $180M) | Consolidated "Higher NIKE Brand product costs ... approximately 100 basis points ... primarily due to higher tariffs in North America" x $11,720M (Q1 FY26 10-Q p. 22). This is a *net* product cost line, and the NA bullet says tariffs were "offset primarily by product mix" (p. 25), so gross NA tariffs were probably higher. The top of the range is my assumption. | 44.6% (45.9% at $180M) |
| Q2 FY26 | $293M | Nike release: 520 bps x NA revenue $5,633M (Q2 FY26 remarks PDF p. 9) | 46.0% |
| Q3 FY26 | $327M (alt. $338M) | Nike release: "nearly 650" bps x $5,026M (Q3 FY26 remarks PDF p. 11); alt. 300 bps x consolidated $11,279M | 46.1% |
| Q4 FY26 | $274M (range $200M to $300M) | Nike release, guidance: "250 basis points due to higher tariffs in North America" (Q3 FY26 remarks PDF p. 14) x Q4 consolidated revenue $10,972M (FY26 $46,398M minus 9M $35,426M, my arithmetic). It includes Section 122 from February 24. It is a forecast, not an actual; Q4 ex-refund GM beat the guide (-10 bps vs -25 to -75). | 46.6% |
| **FY26** | **$1,011M** (range $920M to $1,111M) | sum | **45.8%** (range 45.4% to 46.3%) |

- **Formula.** No-new-tariff FY26 NA GM = (gross profit 9,351 - refund 965 + FY26 tariffs T) / 20,511 (my arithmetic). It does not depend on E25 or I26, because neither was ever FY26 expense.
- **Versus FY24 (44.4%):** about +143 bps central, +98 to +192 bps across the range (estimate). The rise survives even at the low end of the range.
- **Cross-check against Nike's full-year statement:** Nike calls FY26 "Stabilizing Gross margins excluding the impact of incremental tariffs" (Q4 FY26 remarks PDF p. 8). That fits a flat-to-higher underlying margin for the company (opinion).
- **Quarterly pattern:**
  - Ex-tariff, ex-refund NA GM rises from 44.6% (Q1) to about 46% (Q2, Q3) and 46.6% (Q4, guide-based).
  - Versus FY24 quarters (43.8%, 44.1%, 45.2%, about 44.5%), that is about +80, +190, +90 and +210 bps (my arithmetic).
  - Q4 has the weakest independent input, because it rests on guidance.
- **Q4 FY26 consistency with Nike (reviewer point).** Q4 FY26 ex refund was -29 bps YoY. Ex refund and ex tariffs it was **+538 bps** YoY (my arithmetic, using the guide-based Q4 tariff).
  - Nike says that "excluding the tariff refund benefit, underlying gross margin profitability continued to improve year-over-year" (Q4 FY26 remarks PDF p. 10).
  - In Q3, Nike used "underlying" next to "despite nearly 650 basis points of gross impact from new US tariffs" (Q3 FY26 remarks PDF p. 11). So Nike's "underlying" excludes tariffs too.
  - That makes the -29 bps and Nike's statement consistent. The apparent conflict was definitional (opinion based on Nike's usage).

### 2c. The IEEPA timing identity: is the refund bigger than the FY26 expense? (revision 2)

**Identity (my arithmetic, from filing wording).** North America's $965M refund = E25 + FY26 NA IEEPA expense + I26. Here:
- E25 = tariffs paid and expensed in FY2025;
- I26 = tariffs paid and still in inventory at May 31, 2026.

The whole recovery went to Cost of sales: the 10-K's "$302 million" received plus "$684 million" receivable equals the $986M benefit. It follows that:
- refund - FY26 IEEPA expense = E25 + I26 >= 0;
- reported 45.6% - no-IEEPA margin = (E25 + I26) / 20,511.

| Item | Value | Basis |
|---|---|---|
| Residual R = 965 - (Q1 to Q3 NA tariff estimates) | $228M | my arithmetic (estimate; uses $117M for Q1) |
| R = E25 + Q4 FY26 IEEPA expense + I26 | | identity |
| **Hard upper bound on E25 + I26** | **$228M = 111 bps** | It cannot exceed R, since Q4 IEEPA expense >= 0. No-IEEPA FY26 GM floor 44.48%, so FY24 to FY26 is at least +9 bps (my arithmetic). |
| Implied post-entry inventory cover | 63 days | R / Q3 daily IEEPA expense ($3.63M/day). NA inventory is 107 days of Q4 cost of sales (3,320 / 2,857 x 92), but goods in transit carry no duty yet (estimate). |
| I26 (IEEPA still in inventory May 31, 2026) | **$0 to about $58M** | IEEPA collection stopped for entries "on or after 12:00 a.m. ET on February 24, 2026" (secondary: GHY), 96 days before May 31. FIFO with about 63 days of cover gives about $0. Nike values inventory on "an average or a specific identification cost basis" (FY26 10-K p. 63); with averaging at 60 to 70 days of cover, about 20% to 25% of R remains, $46M to $58M (estimate). |
| E25 (IEEPA expensed in FY25) | **about $15M to $35M** | Before April 5, 2025, IEEPA hit only China-origin goods (China was "roughly 16% of the footwear we import into the United States", Q4 FY25 remarks PDF p. 13). With 60 to 70 days of cover, only February to March 2025 entries would have sold by May 31 (assumption). Nike did not list tariffs among the Q4 FY25 gross margin drivers (Q4 FY25 remarks PDF p. 9). It said tariffs were in the higher May 31, 2025 inventory, i.e. capitalized, not expensed (PDF p. 10). This is an estimate resting on stated assumptions; Nike gives no figure. |
| **E25 + I26, central** | **$15M to $85M = 7 to 41 bps** | No-IEEPA FY26 NA GM 45.18% to 45.52%, i.e. **+79 to +113 bps vs FY24** (estimate). |

- **Cross-check from consolidated bridges (my arithmetic).**
  - FY26 Nike Brand product costs: -20 bps x $46,398M = -$93M. 9M FY26: -240 bps x $35,426M = -$850M. Implied Q4 product-cost swing: +$757M (+/- $41M from bps rounding).
  - The refund was $986M, so Q4 tariffs minus Q4 base product-cost savings minus lapped E25 = about $229M. That is close to the guide-based $274M for NA Q4 tariffs, so the guide is not far off (opinion).
- **Corroboration of R.**
  - At February 28, 2026, NA "Inventory dollars grew low-single digits, while units were down high-single digits, with the spread primarily due to tariffs" (Q3 FY26 remarks PDF p. 11).
  - A dollars-vs-units spread of roughly 8 to 12 points on about $3.2B of inventory implies about $250M to $380M of extra cost per unit, "primarily" tariffs. That is the same order as R (estimate; NA inventory at February 28 is not disclosed, so $3.2B is assumed from the May 31 values of $3,198M and $3,320M, FY26 10-K p. 86).

**Reviewer's range (44.6% to 45.3%) vs this note.** The reviewer assumed I26 of $50M to $200M on top of a 45.6% base. The 63-day calibration and the February 24 cut-off put I26 at the low end of that range. The no-IEEPA central range (45.2% to 45.5%) overlaps the top of the reviewer's range. Neither range can be confirmed until Nike discloses E25 and I26.

### 2d. Price vs cost per unit, FY2024 to FY2026 (revision 2)

| Step | Value | Basis |
|---|---|---|
| Footwear revenue per pair, FY25 / FY26 | about -3 pts / about -1 pt | FY25 10-K p. 38; FY26 10-K p. 37 ("lower ASP per pair reduced footwear revenues by approximately 1 percentage point ... primarily due to channel mix, partially offset by product mix and strategic pricing") |
| Apparel revenue per unit, FY25 / FY26 | about -1 pt / about +2 pts | same pages ("primarily due to product mix, partially offset by channel mix") |
| Weighted footwear + apparel revenue per unit | FY25 -2.42%, FY26 -0.05%, **cumulative -2.47%** | my arithmetic (prior-year revenue weights; Nike rounds each to about 1 pt) |
| Channel shift alone (Direct share 48.6% to 41.7%; Direct = 1.654x wholesale value) | **-3.25%** | estimate (assumes the same product mix in each channel; 1.654x from note 09 Test 1, FY24 10-K p. 34) |
| Residual: price, product mix, discounts | **about +0.8%** | estimate |
| Channel shift effect on GM at constant channel margins | **-149 to -177 bps** | estimate (note 09 gap of 21.7 to 25.7 points x -6.9 pts share) |
| Unit index (revenue index / price index) | 0.983 | my arithmetic |
| COGS ex new tariffs, FY26 vs FY24 | 11,014 to 11,205 vs 11,899 | 11,160 + 965 - T |
| **Cost per unit ex new tariffs, FY24 to FY26** | **-4.2% to -5.8%** | estimate |

- **Reading.** Relative to FY24, North America sells at slightly lower revenue per unit, because more goes through wholesale. It makes more margin anyway, because each unit costs about 5% less to buy, land, store and ship (excluding new tariffs).
- **Where Nike points:**
  - product costs (FY25: freight, input costs, product mix; FY26: "lower product costs");
  - W&L ("lower warehousing and logistics costs driven by channel mix");
  - lower obsolescence reserves in FY26 Q2 and Q3.
- **Limits.**
  - The ASP percentages are rounded to about 1 pt each.
  - Equipment (5% of revenue) is excluded.
  - The channel price premium is a FY24 company-wide figure.
  - A cost-per-unit fall from product mix also lowers price per unit, which sits in the +0.8% residual.
  - The 4% to 6% is therefore a direction and a rough size, not a precise split.

### 2e. Other regions for contrast (gross margin, from note 06 Section 2, FY25 and FY26 10-Ks)

| Segment | FY24 | FY25 | FY26 | FY24 to FY26 (bps, my arithmetic) | Nike's main stated reason, FY26 | Direct share FY24 to FY26 (my arithmetic) |
|---|---|---|---|---|---|---|
| North America (reported) | 44.4% | 43.5% | 45.6% | +120 | lower product costs, W&L from channel mix, higher ASP | 48.6% to 41.7% |
| North America (ex refund, all tariffs in) | 44.4% | 43.5% | 40.9% | -350 | (tariffs) | |
| North America (no new tariffs, estimate) | 44.4% | about 43.5% | about 45.8% | about +143 (+98 to +192) | | |
| EMEA | 44.2% | 43.2% | 41.8% | -240 | lower ASP (discounts) and standard FX | 37.1% to 32.7% |
| Greater China | 50.2% | 46.0% | 45.7% | -450 | standard FX | 43.5% to 44.3% |
| APLA | 45.9% | 44.0% | 42.0% | -390 | standard FX | 41.6% to 39.5% |
| Converse | 52.5% | 48.7% | 43.8% | -870 | lower ASP, brand reset costs, obsolescence | n/a |

- **EMEA is the control case for channel mix.** It also shifted to wholesale, and its margin fell, from discounts plus FX. NA had both of the following, and EMEA had neither (opinion based on the bullets):
  - a per-unit cost tailwind large enough to beat the channel price drag;
  - only a mild FX headwind.
- **NA's FX exposure is small but real.** Canada sits inside NA. NA FY25 vs FY24 revenue was -9% reported vs -8% currency-neutral (FY26 10-K p. 36). CAD averages (FRED DEXCAUS, secondary): FY24 1.3513, FY25 1.3955, FY26 1.3785, Q1 FY27 1.4015 CAD per USD. A weaker CAD raises a Canadian unit's cost of USD product.
  - Nike gives no Canada revenue. "Revenues derived in the United States were $20,358 million" in FY26, but that includes Converse (FY26 10-K p. 87), so Canada cannot be derived.

### 2f. Q1 FY2027 by region (Q1 FY27 10-Q pp. 26 to 31), and what contaminates the NA comparison

| Segment | Change | Stated reason |
|---|---|---|
| North America | +110 bps to 43.4% | higher ASP and lower W&L, partly offset by higher product costs (product mix) |
| EMEA | +140 bps | lower product costs and lower W&L, partly offset by lower ASP |
| Greater China | +30 bps | lower product costs, partly offset by lower ASP and higher obsolescence reserves |
| APLA | -150 bps | lower ASP and standard FX |
| Converse | -210 bps | higher product costs and higher W&L, partly offset by higher ASP |

- **What contaminates the NA comparison (revision 2):**
  - **Q1 FY26 base.** It included about $117M to $180M of IEEPA cost (estimate) that was refunded later, in Q4 FY26. Without it, Q1 FY26 would have been 44.6% to 45.9%.
  - **Q1 FY27 tariff load.** It includes Section 122 (10% on entries from February 24 "for 150 days through July 24, 2026", secondary: GHY). It also includes any IEEPA cost still in May 31 inventory (I26, $0 to about $58M), which was already credited in Q4 FY26 and is now expensed a second time in the P&L.
  - **Nike's Q1 FY27 data.** Consolidated "Lower NIKE Brand product costs, increasing gross margin approximately 10 basis points" (Q1 FY27 10-Q p. 23). NA "higher product costs, driven by product mix" (p. 26). Neither names tariffs.
- **Illustration.** If Q1 FY27 NA tariffs were $100M to $200M, the no-tariff Q1 FY27 margin would be 45.3% to 47.3% (estimate).
- **Verdict.** Q1 FY27 is not cleanly comparable with either Q1 FY26 or Q1 FY25. The +110 bps survives as a reported fact; its underlying size is **unresolved**.

## 3. Verbatim quotes with sources

Nike filings URL pattern: `https://investors.nike.com/sec-filings/all-sec-filings/content/<accession>/<file>.htm`. Page = printed page.

**FY2026 Form 10-K** (accession 0000320187-26-000088, `nke-20260531.htm`), filing:
- p. 30 (and the same text in Note 1, p. 61): "we recognized a benefit of $986 million in Cost of sales within the Consolidated Statements of Income for the recovery of IEEPA tariffs paid, for which $965 million and $21 million of the benefit was classified within North America and Converse, respectively, largely offsetting the impact of the IEEPA tariffs recognized during fiscal 2026."
- p. 37, North America table: "Gross margin | 45.6% | 43.5% | 210 bps | 44.4% | -90 bps"
- p. 37: "Gross margin expansion of 210 basis points primarily due to lower product costs, lower warehousing and logistics costs driven by channel mix, and higher ASP. Higher ASP primarily reflects strategic pricing and product mix, partially offset by channel mix."
- p. 37: "Wholesale revenues increased 14% including expanded distribution, higher shipments to existing partners and fewer marketplace management actions taken in the current year."
- p. 34, consolidated bridge: "Lower warehousing and logistics costs (increasing gross margin approximately 20 basis points), primarily due to channel mix;" and "Higher NIKE Brand product costs (decreasing gross margin approximately 20 basis points)."
- p. 38 (EMEA): "Gross margin contraction of 140 basis points primarily due to lower ASP, reflecting higher discounts, and unfavorable changes in standard foreign currency exchange rates."
- p. 39 (Greater China): "Gross margin contraction of 30 basis points primarily due to unfavorable changes in standard foreign currency exchange rates."
- p. 40 (APLA): "Gross margin contraction of 200 basis points primarily due to unfavorable changes in standard foreign currency exchange rates."
- p. 42 (Converse): "Gross margin contraction of 490 basis points primarily due to lower ASP, as well as the brand and marketplace reset costs, including higher inventory obsolescence reserves and employee severance costs."
- p. 85 (Note 15): "Inventories and Cost of sales for geographic segments and Converse reflect the use of these standard rates to recognize non-functional currency product purchases in the entity's functional currency."
- p. 43: the NTC "buys NIKE branded products from third-party factories, predominantly in U.S. Dollars."

**FY2025 Form 10-K** (0000320187-25-000047, `nke-20250531.htm`), filing:
- p. 38: "Gross margin contraction of 90 basis points primarily due to lower ASP and higher inventory obsolescence reserves, partially offset by lower product costs. Lower ASP primarily reflects higher discounts and changes in channel mix."
- p. 38 table: FY24 NA "Gross profit | 8,516 | 9,497" and "Gross margin | 43.5% | 44.4% | -90 bps | 42.2% | 220 bps".
- p. 35, consolidated: "Lower NIKE Brand product costs (increasing gross margin approximately 80 basis points);" and "Higher other costs (decreasing gross margin approximately 90 basis points), including higher inventory obsolescence reserves;"
- p. 40 (Greater China): "Gross margin contraction of approximately 420 basis points, primarily due to unfavorable changes in standard foreign currency exchange rates and higher inventory obsolescence reserves".

**Q1 FY2025 10-Q** (0000320187-24-000065, `nke-20240831.htm`), filing, p. 25: "Gross margin expansion of 180 basis points primarily due to lower product costs, as well as lower warehousing and logistics costs."

**Q2 FY2025 10-Q** (0000320187-25-000004, `nke-20241130.htm`), filing, p. 29: "Gross margin was flat primarily due to lower ASP, reflecting product mix, changes in channel mix and higher discounts, as well as higher other costs, in part due to inventory obsolescence reserves. These were offset by lower product costs ... as well as lower warehousing and logistics costs."

**Q3 FY2025 10-Q** (0000320187-25-000016, `nke-20250228.htm`), filing, p. 32: "Gross margin contraction of 210 basis points primarily due to lower ASP and higher inventory obsolescence reserves. Lower ASP primarily reflects higher discounts and changes in channel mix".

**Q1 FY2026 10-Q** (0000320187-25-000097, `nke-20250831.htm`), filing:
- p. 25: "Gross margin contraction of 330 basis points, primarily due to new tariffs and lower ASP, partially offset by lower warehousing and logistics costs. ... Overall product costs were flat as higher tariffs were offset primarily by product mix."
- p. 22: "Higher NIKE Brand product costs (decreasing gross margin approximately 100 basis points), primarily due to higher tariffs in North America;" and "Lower warehousing and logistics costs (increasing gross margin approximately 50 basis points), primarily due to channel mix;"

**Q2 FY2026 10-Q** (0000320187-25-000151, `nke-20251130.htm`), filing:
- p. 30: "Gross margin contraction of 330 basis points, primarily due to new tariffs, partially offset by lower warehousing and logistics costs due to channel mix, and lower inventory obsolescence reserves. ASP was flat as product mix and strategic pricing were offset primarily by channel mix."
- p. 23: "we expect a gross incremental cost of approximately $1.5 billion on an annualized basis."

**Q3 FY2026 10-Q** (0000320187-26-000037, `nke-20260228.htm`), filing:
- p. 33: "Gross margin contraction of 350 basis points, primarily due to higher tariffs, partially offset by higher ASP and lower inventory obsolescence reserves."
- p. 34 (9M): "Gross margin contraction of 340 basis points, primarily due to higher tariffs and lower ASP, partially offset by lower warehousing and logistics costs due to channel mix and lower inventory obsolescence reserves. Lower ASP primarily reflects channel mix, partially offset by strategic pricing."
- p. 26: "Total IEEPA tariffs paid as of the date of this report is approximately $1.0 billion. ... we have determined that potential recovery of any funds is not probable."

**Q1 FY2027 10-Q** (0000320187-26-000193, `nke-20260831.htm`), filing:
- p. 26: "Gross margin expansion of 110 basis points primarily due to higher ASP and lower warehousing and logistics costs, partially offset by higher product costs, driven by product mix. Higher ASP primarily reflects product mix and strategic pricing, partially offset by higher discounts."
- p. 23: "Lower warehousing and logistics costs, increasing gross margin approximately 90 basis points;"
- p. 33: "receipt of the International Emergency Economic Powers Act tariff receivable".

**Nike prepared call remarks** (Nike release; PDF page numbers; `https://s1.q4cdn.com/806093406/files/doc_financials/<yyyy>/<qN>/NIKE-Inc-Q#FY##-UNOFFICIAL-Transcript.pdf`; Q1 FY27 at `https://s1.q4cdn.com/806093406/files/content_files/NIKE-Inc-Q1FY27-UNOFFICIAL-Transcript.pdf`):
- Q4 FY25, PDF p. 13: "we have implemented a surgical price increase in the United States, with phased implementation beginning in Fall 25." PDF p. 10: "Inventory dollars and units increased, due partially to investment to support new distribution, unfavorable shipment timing, and new tariffs."
- Q2 FY26, PDF p. 9: "North America gross margins only declined 330 basis points versus the prior year, despite 520 basis points of impact from new US tariffs."
- Q3 FY26, PDF p. 11: "North America gross margins declined 360 basis points versus the prior year, despite nearly 650 basis points of gross impact from new US tariffs." (The 10-Q gives -350 bps; the remarks round differently.) PDF p. 14: "Q4 down approximately 25 to 75 basis points, including 250 basis points due to higher tariffs in North America."
- Q4 FY26, PDF pp. 8 to 9: "recognition of a one-time benefit of $986 million, offsetting the IEEPA tariffs embedded within cost of sales that had been expensed through the income statement throughout Fiscal 26." PDF p. 9: "Gross margin was 49.2%, up 890 basis points versus prior year, driven by a 900 basis point benefit related to recovery of IEEPA tariffs. Excluding this benefit, gross margin would have been 40.2%, down 10 basis points versus prior year, which included additional severance costs related to supply chain actions in North America and EMEA". PDF p. 10: North America "EBIT increased 91% on a reported basis. Excluding the tariff refund benefit, EBIT would have declined 1%." PDF p. 12: "Our forecast is based on incremental tariff rates of 10% continuing through the end of July, and then increasing to 15% thereafter".
- Q1 FY27, PDF pp. 10 to 11: "Gross margin was 42.8 percent, up 60 basis points compared to LY. The result included benefits from our supply chain cost management efforts and FX tailwinds, partially offset by increased discounts as well as channel mix."

---


**Added in revision 2 (all quotes re-read from the saved page text this session):**
- FY2026 10-K, filing:
  - p. 30: "As of May 31, 2026, we received $302 million and recorded $684 million of outstanding IEEPA tariff receivables reflected within Accounts receivable, net on the Consolidated Balance Sheets."
  - p. 63: "Inventory costs primarily consist of product cost from the Company's suppliers, as well as inbound freight, import duties, taxes, insurance, logistics and other handling fees. ... valued on either an average or a specific identification cost basis."
  - p. 86: segment inventories, North America "3,320" (May 31, 2026), "3,198" (2025), "3,134" (2024).
  - p. 87: "Revenues derived in the United States were $20,358 million, $19,725 million and $21,551 million for the fiscal years ended May 31, 2026, 2025 and 2024, respectively."
  - p. 43: "a weakening U.S. Dollar against the indexed foreign currencies increases our inventory cost."
  - p. 36: NA revenue FY25 vs FY24 "-9" reported and "-8" excluding currency changes.
  - p. 34: the full consolidated bridge has no NIKE Brand ASP line for FY26; product costs are "approximately 20 basis points" adverse.
- Q1 FY2025 10-Q, filing, p. 22: "Lower NIKE Brand product costs (increasing gross margin approximately 120 basis points), primarily due to lower ocean freight rates and lower product input costs".
- Q2 FY2025 10-Q, filing, p. 29 (NA): "These were offset by lower product costs, reflecting product mix and lower product input costs, as well as lower warehousing and logistics costs."
- Q2 FY2026 10-Q, filing, p. 27: "Higher NIKE Brand product costs (decreasing gross margin approximately 360 basis points), primarily due to higher tariffs in North America".
- Q3 FY2026 10-Q, filing, p. 30 (9M): "Higher NIKE Brand product costs (decreasing gross margin approximately 240 basis points), primarily due to higher tariffs in North America". Income statement p. 1: 9M revenues "35,426"; Q3 "11,279".
- Q1 FY2027 10-Q, filing, p. 23: "Lower NIKE Brand product costs, increasing gross margin approximately 10 basis points."
- Nike release (prepared remarks):
  - Q4 FY25, PDF p. 9: "Gross margins declined 440 basis points to 40.3% on a reported basis, due to higher wholesale discounts, higher discounts in our Nike factory stores, supply chain cost deleverage and channel mix headwinds." PDF p. 13: "China represents roughly 16% of the footwear we import into the United States".
  - Q1 FY26, PDF p. 10: "On inventory, North America drove continued progress through the first quarter. Units declined versus the prior year, while dollars were flat, primarily due to new US tariffs."
  - Q2 FY26, PDF p. 8: "$1.5 billion of annualized incremental product costs due to higher U.S. tariffs. This represents a gross headwind of approximately 320 basis points to gross margin in Fiscal 26."
  - Q3 FY26, PDF p. 11: "Inventory dollars grew low-single digits, while units were down high-single digits, with the spread primarily due to tariffs." and "Underlying profitability has now improved over three consecutive quarters".
  - Q4 FY26, PDF p. 8: "Stabilizing Gross margins excluding the impact of incremental tariffs." PDF p. 10: "Inventory grew mid-single digits, in line with our plans, with a healthy closeout mix. Importantly, excluding the tariff refund benefit, underlying gross margin profitability continued to improve year-over-year".
- Secondary:
  - GHY International, "U.S. 10% Section 122 Tariff In Effect Feb. 24; IEEPA Tariffs Cease" (https://www.ghy.com/trade-compliance/us-10-section-122-tariff-in-effect-feb-24-ieepa-tariffs-directed-to-wind-down-de-minimis-suspension-continues/): CBP confirmed IEEPA duty collection will cease for goods entered "on or after 12:00 a.m. ET on February 24, 2026"; "10% Section 122 Tariff Effective Feb. 24: Applies across the board for 150 days through July 24, 2026." Read via WebFetch summary; treat the wording as close to, not certainly identical with, the page text.
  - FRED series DEXCAUS (Board of Governors H.10, https://fred.stlouisfed.org/graph/fredgraph.csv?id=DEXCAUS), saved at `scratchpad/rh/dl/na_fx/dexcaus.csv`; the fiscal-year averages are my arithmetic.

---

## 4. Unresolved, and the data that would resolve it

1. **The split of the roughly 5% per-unit cost fall** between product cost (freight, input costs, sourcing, product mix), W&L and obsolescence.
   - **Resolving data:** an NA gross margin bridge in bps (Nike publishes only consolidated bridges), or management answers in the call Q&A (not cached here).
2. **E25 and I26 exactly**, which decide whether the no-IEEPA FY26 NA margin is 45.2% to 45.5% (central) or as low as 44.5% (bound).
   - **Resolving data:** IEEPA tariffs expensed in Q4 FY25, and IEEPA tariffs capitalized in NA inventory at May 31, 2026. Both are absent from the 10-K and the prepared remarks.
3. **Actual Q4 FY26 tariff expense (IEEPA plus Section 122)** in place of the guidance figure, and the true gross Q1 FY26 NA tariff in place of the consolidated net line. Between them they move the no-new-tariff FY26 margin from 45.4% to 46.3%.
4. **The Q1 FY27 tariff load** (Section 122 plus the refunded IEEPA leaving inventory), needed to state an underlying Q1 FY27 change.
5. **Canada's share of NA revenue**, to size the FX headwind. The sign (adverse) is known; the size is not.
6. **Freight from FY25 to FY26.** Nike's FY26 filings do not mention it. Nike's own landed freight cost per unit, or contract-rate data matched to Nike's inventory timing, would test it.

---

## 5. Revision log

**Revision 2 (October 13, 2026), responding to two reviewer reports ("weakened").**

1. **Fixed the sign of refund vs FY26 IEEPA expense.**
   - Revision 1 said the net was "0 or slightly negative". Because the full recovery of tariffs *paid* ($302M received + $684M receivable = $986M) went to Cost of sales, the refund minus FY26 expense = E25 + I26 >= 0.
   - The reported 45.6% therefore overstates, never understates, a no-IEEPA margin. Bottom line item 2 and new Section 2c were rewritten accordingly.
2. **Removed the circular Q4 plug.**
   - Revision 1 set Q4 tariffs = 965 - Q1 to Q3, which forced FY26 to 45.6% by construction.
   - Q4 now comes from Nike's own Q4 guide (250 bps x Q4 consolidated revenue). The FY26 no-new-tariff margin (45.8%, range 45.4% to 46.3%) is computed rather than assumed.
   - The Q1 figure is relabelled a floor, since it is a consolidated net line and NA tariffs were "offset primarily by product mix".
3. **Bounded the out-of-period credit** (E25 + I26, reviewer alternatives 1 and 2): hard bound $228M (111 bps), central $15M to $85M (7 to 41 bps).
   - The bound uses the February 24, 2026 IEEPA cut-off (secondary source), an inventory-cover calibration and Nike's statements on capitalized tariffs.
   - Candidate #9 of revision 1 ("ruled out as material") is now #2, "partly supported, small".
4. **Withdrew "the underlying rise is about +120 bps operating improvement".** It is replaced with two separate measures:
   - no-IEEPA, +79 to +113 bps central, floor +9 bps;
   - no-new-tariff, +98 to +192 bps, central +143 bps.
5. **Corrected the FX verdict.** "North America buys and sells in US dollars, so this line cannot hit it" was false:
   - NA includes Canada (reported vs currency-neutral revenue differ);
   - the factory currency program raises USD inventory cost when the USD weakens.
   - Both moved against NA (CAD averages from FRED). FX is now "ruled out as a cause of the rise (wrong sign)", not "cannot hit".
6. **Tested the ASP driver against unit data** (reviewer alternative 3).
   - Footwear ASP per pair fell; weighted revenue per unit is -2.47% vs FY24.
   - Channel shift alone accounts for about -3.25%, so price, product mix and discounts add only about +0.8%. ASP is downgraded to "small vs FY24".
7. **Added the per-unit cost test (Section 2d):** cost per unit ex new tariffs fell 4.2% to 5.8%. This is now the main surviving driver.
8. **Added channel mix as a net headwind** (#7): -150 to -177 bps price effect vs at most +90 bps W&L. Revision 1 listed only the W&L side.
9. **Corrected a logic error.** Lapping the FY25 clean-up explains FY25 to FY26, not FY24 to FY26.
10. **Tested "lower product costs = net refund"** (reviewer alternative): bounded at -71 to +42 bps of the FY25 to FY26 +210 bps, so it is not the main driver.
11. **Added freight deflation** (#5): filing-supported for FY24 to FY25, not mentioned in FY26 filings. Added **category mix** (#10): real but not separable.
12. **Resolved the Q4 FY26 "underlying improved" vs -29 bps conflict.** Nike's "underlying" excludes tariffs (its Q3 usage). Ex tariffs, Q4 FY26 NA was about +538 bps YoY.
13. **Q1 FY27: replaced "neither quarter has a refund" with a contamination analysis.**
    - The Q1 FY26 base carried IEEPA later refunded.
    - Q1 FY27 carries Section 122 and possibly refunded IEEPA leaving inventory.
    - The Q1 FY27 underlying change is now marked unresolved.
14. **Kept unchanged**, all re-checked by the reviewers: the base data tables (2a), the $965M refund quotes, the 520, 650 and 250 bps quotes, the regional FX contrast, and the restatement check.

**Revision 1 (October 13, 2026):** initial note.

## Independent verification log
- Oct 13, 2026: recomputed. FY2026 NA gross margin excluding the $965M refund = (20,511 x 45.6% - 965) / 20,511 = 40.9%, -350 bps vs FY2024 44.4% (confirmed).
