# Foot Locker evidence on the Jordan thesis (supply cut vs demand collapse)

Prepared 2026-10-13. The thesis under test: Jordan revenue fell because Nike deliberately cut retro supply, not because demand collapsed.

Labels used:
- VERIFIED: I opened the source myself.
- DERIVED: my own calculation.
- PRIOR BRANCH: taken from origin/claude/wonderful-franklin-u31n4e `research_notes/thesis_tests/retailer_sell_through.md` and not re-opened by me.

Fiscal calendars:
- Foot Locker (FL) fiscal year N ends in late January or early February of year N+1. For example, FL Q2 2025 is May 4 to Aug 2, 2025.
- DICK'S (DKS) Q2 2026 is May 3 to Aug 1, 2026. It overlaps Nike Q1 FY27 (Jun to Aug 2026) for about two months.

Sources and handling:
- **SEC filings.** Downloaded from EDGAR to `dl/` and converted to text in `txt/`. Pages cited are the printed footers ("2024 Form 10-K Page 29"). Earnings releases (ER) have no printed pages.
- **Contact header.** After the rules update, no further SEC requests were made with a contact header.
- **Call transcripts.** MarketBeat pages, opened in full with curl (`web/`). They are third-party transcriptions, not company-certified.
- **Excluded data.** No Jordan-only revenue, unit or price numbers exist in any Foot Locker or DICK'S document. Everything below is retailer commentary plus total-company metrics.

## 0. Deal and closing (VERIFIED)
- FL 8-K filed 2025-09-08 (acc. 0001104659-25-088056), Item 2.01: "Pursuant to the Merger Agreement, on September 8, 2025 (the 'Closing Date'), Merger Sub merged with and into the" company. The merger agreement was "dated as of May 15, 2025". Consideration per share was "$24.00, if an election to receive cash consideration was properly" made (stock alternative also available).
- The last FL standalone report was the 10-Q for the quarter ended Aug 2, 2025, filed 2025-09-02.

## 1. Nike share of Foot Locker purchases (10-K, VERIFIED)

| FL fiscal year | Nike % of merchandise purchases | Top-5 suppliers % | Source (printed page) |
|---|---|---|---|
| 2018 | 66% | 90% | 10-K FY2019 (filed 2020-03-27) p.27: "Approximately 71 percent and 66 percent was purchased from one supplier" |
| 2019 | 71% | 91% | same |
| 2020 | 75% | 91% | 10-K FY2020 p.27: "Approximately 75 percent and 71 percent was purchased" |
| 2021 | 68% | 87% | 10-K FY2021 p.29: "Approximately 68% and 75% was purchased from one supplier, Nike, Inc., in 2021 and 2020" |
| 2022 | 65% | 86% | 10-K FY2022 p.26: "Approximately 65% and 68% was purchased from one supplier, Nike, Inc., in 2022 and 2021" |
| 2023 | 65% | 84% | 10-K FY2023 p.30: "Approximately 65% was purchased from one supplier, Nike, Inc., in both 2023 and 2022." |
| 2024 | 59% | 85% | 10-K FY2024 p.29: "Approximately 59% and 65% was purchased from one supplier, Nike, Inc., in 2024 and 2023" |
| 2025 (DKS + FL from 9/8/25) | 31% of combined DKS + FL | n/a | PRIOR BRANCH: DKS 10-K FY2025 p.9 |

DERIVED index of Nike purchases (sales times Nike %; a crude proxy because the % is of purchases, not sales):

| FL fiscal year | Sales | Index | Change |
|---|---|---|---|
| FY2020 | $7,548M | about 5.66B | |
| FY2021 | $8,958M | about 6.09B | |
| FY2022 | $8,747M | about 5.69B | |
| FY2023 | $8,154M | about 5.30B | |
| FY2024 | $7,971M | about 4.70B | about -23% from FY2021 |

Sales come from each 10-K's segment table. FL's Nike buying peaked in the year that maps to Nike FY2022, then declined. Nike Jordan revenue still rose to its FY2024 peak over the same years. So the FL allocation cut was a channel shift toward Nike DTC, not a cut in Jordan volume.

Why Nike's share fell (VERIFIED):
- FL ER Q4 2021 (2022-02-25), the 8-K "Update on Vendor Mix" section: "Beginning in the fourth quarter 2022, Foot Locker, Inc. does not expect any one vendor to represent more than 55% of total supplier spend, down from 65% in the fourth quarter of 2021 ... This change reflects the accelerated strategic shift to DTC by one of the Company's vendors."
- The same call, Dick Johnson (CEO), 2022-02-25: "the hype ... the heat from certain styles that Nike certainly drives through their DTC and that's where the allocation pressure will be."

## 2. Comparable sales by quarter (VERIFIED unless noted)

| Quarter (FL or DKS fiscal) | Comp | Source |
|---|---|---|
| Q2 2021 | +6.9% | ER 2021-08-20 |
| Q3 2021 | +2.2% | ER 2021-11-19 |
| Q4 2021 | +0.8% | ER 2022-02-25 |
| Q1 2022 | -1.9% | ER 2022-05-20 |
| Q2 2022 | -10.3% (North America -16.1%) | 10-Q Q2 2022 p.23 table |
| Q3 2022 | +0.8% | ER 2022-11-18 |
| Q4 2022 | +4.2% | ER 2023-03-20 |
| Q1 2023 | -9.1% | ER 2023-05-19 |
| Q2 2023 | -9.4% | ER 2023-08-23 |
| Q3 2023 | -8.0% | ER 2023-11-29 |
| Q4 2023 | -0.7% | ER 2024-03-06 |
| Q1 2024 | -1.8% | ER 2024-05-30 |
| Q2 2024 | +2.6% | ER 2024-08-28 |
| Q3 2024 | +2.4% | ER 2024-12-04 |
| Q4 2024 | +2.6% (global Foot Locker + Kids Foot Locker +3.6%) | ER 2025-03-05 |
| Q1 2025 | -2.6% (North America -0.5%, international -8.5%) | ER 2025-05-29 |
| Q2 2025 | -2.0% (North America +1.4%; NA ex-WSS +2.6%; Europe and Asia Pacific -10.3%) | ER 2025-08-27 |
| Q3 2025 (DKS pro forma) | -4.7% | PRIOR BRANCH (DKS ER Q3 2025) |
| Q4 2025 (DKS pro forma) | -3.4% (prior year +2.3%) | DKS ER 2026-03-12 |
| Q1 2026 (DKS pro forma) | +0.6% (North America +1.4%; U.S. Foot Locker banner +6.4%; international -1.7%) | DKS ER 2026-05-27; call 2026-05-27, Gupta |
| Q2 2026 (DKS pro forma) | -3.6% (international -3.3%; North America also down per Gupta) | DKS ER 2026-08-25 |

Notes:
- DKS pro forma prior-year figures differ slightly from FL's reported comps: Q1 2025 is -2.9% vs -2.6%, and Q2 2025 is -2.2% vs -2.0%. DKS says these were "adjusted to conform".
- Foot Locker segment gross margin (DERIVED from the DKS ER segment tables):
  - Q4 2025: 25.0% (544,601 / 2,175,265)
  - Q1 2026: 27.9% (498,666 / 1,787,064)
  - Q2 2026: 25.7% (445,769 / 1,736,928)
  - Q2 2026 segment loss was $(31.9)M.
- Foot Locker Business inventory was $2.0B on Aug 1, 2026 (DKS ER Q2 2026 note 4), against FL standalone inventory of $1,709M on Aug 2, 2025 (FL ER 2025-08-27). That is about +17% (DERIVED; rounding range +14% to +20%) while comps were -3.6%.

## 3. Jordan, allocation, sell-through and markdowns: chronological quotes

### A. FY2021 scarcity era (an FY2018-like analog)
- FL 10-K FY2021 p.24 (VERIFIED): gross margin rose 550 bps, "since we were significantly less promotional than a year ago, due to increased demand and relatively short supply of certain merchandise."
- Johnson, call 2022-02-25 (VERIFIED): "there is nothing like a retro Jordan launch that comes in on a Friday and sells on a Saturday".

### B. 2022 to 2023 allocation cut (deliberate, DTC-driven): Jordan retro sell-through stayed strong at lower units
- Andrew Page (CFO), call 2022-11-18 (VERIFIED): "this fourth quarter is the first big impact of the Nike drop in allocation."
- Dillon, call 2023-05-19 (VERIFIED): "Retro sell-throughs, albeit at reduced quantities, were very good."
- Bracken, same call (VERIFIED): "the release of the Jordan Retro 4 Thunder generated incredible excitement and sellout results."
- Mary Dillon (CEO), call 2023-08-23 (VERIFIED): loyalty sales share fell "driven by lower Nike launch product allocation".
- Frank Bracken (CCO), same call (VERIFIED): "we're still seeing very good sell-through on launch-type products ... In the base business or of non-launch, we are seeing that promotional pressure is impacting sell-throughs".
- Dillon, call 2023-11-29 (VERIFIED): "Retro sell-throughs remained solid in the third quarter, albeit with lower units compared to last year."
- Comps were -8% to -9% in Q1 to Q3 2023. The cited drivers were macro, "changing vendor mix", and the Champs repositioning (ERs 2023-05-19, 2023-08-23, 2023-11-29).

Read: this period fits "supply cut, demand intact" for Jordan retro at Foot Locker. But it was a channel reallocation while Nike Jordan revenue was still growing.

### C. Nike reverses: allocation returns, but classics are oversupplied (2024)
- Dillon, call 2024-03-06 (VERIFIED): "we expect to return to growth with Nike on an allocation basis later in this year during the holiday quarter."
- Bracken, call 2024-05-30 (VERIFIED): "Nike's Dunk and Air Force 1 and the Jordan AJ 1 continue to be the icons that consumers demand most. As Nike rebalances supply in the marketplace to manage these critical franchises..."
- Bracken, call 2024-08-28 (VERIFIED): "our Jordan Retro business continues to be a critical connection point ... and we saw strong sell-throughs as we exited the quarter and then the beginning of back to school."
- Bracken, call 2024-12-04, prepared remarks (VERIFIED), on Q3 2024:
  - "we are contending with some more recent softness out of our top partner, Nike."
  - "As Nike rebalances their product mix and inventory levels in the near term across the basketball classics franchises, we are seeing some short-term negative impacts on our business. We are seeing higher promotional levels in the marketplace across both DTC and competition".
- Bracken, same call, Q&A (VERIFIED): "while we work through some of the short-term pressure on some of the sell-throughs and some of the classics and lifestyle running ... as we work into 2025, feel that there'll be a better sort of supply and demand balance."
- FL ER 2024-12-04 (VERIFIED), Dillon: "softer consumer demand outside of key selling periods".
- FL 10-K FY2024 p.26 (VERIFIED): "we were less promotional in 2024 despite the highly promotional marketplace". FL's own markdowns fell, and gross margin rose 120 bps.

### D. Q4 2024 (Nov 2024 to Jan 2025): allocation growth returns; premium retros sell out
- Bracken, call 2025-03-05, prepared remarks (VERIFIED):
  - "The Jordan Brand delivered gains thanks to very compelling launches in the quarter".
  - "Retro 9, Retro 3, and the Carolina Blue Retro 11, all of which were sellouts with consumers."
  - "partner with them to bring health back to critical consumer franchises like Air Force 1, Dunk, and the AJ 1".
- Bracken, same call, Q&A (VERIFIED):
  - "we did return to allocation growth in Q4, and you saw that read-through in our results in the Jordan Brand and our launch business."
  - "We're definitely supportive of the actions being taken on those big three basketball classic franchises."
- Dillon, same call (VERIFIED): "Last weekend, we had a Jordan Retro 12."
- Mike Baughn (CFO), same call (VERIFIED): "Merchandise margins were up 300 basis points year-over-year due to lower markdown levels". He also cited "key launches like the Retro 12". Note: the ER says "despite elevated promotions in the marketplace".

Read: this is direct evidence of deliberate supply management of AJ1 (the "big three"). It is also direct evidence that limited premium retro launches sold out at Foot Locker through early 2025. Supports the thesis for that window.

### E. Q2 2025 (May to Aug 2025), the last standalone filing: demand language
- FL 10-Q Q2 2025 p.20 (VERIFIED): "comparable sales decreased within the stores channel due to ongoing macroeconomic headwinds, declines in consumer discretionary spending, and lower demand of key basketball footwear styles, which affected customer traffic."
- The same page says North America constant-currency sales rose on "exciting product offerings from strategic brands".
- This is the only filing sentence that attributes weakness to demand for basketball styles. Jordan is not named; "key basketball footwear styles" at FL are dominated by Nike and Jordan classics (inference).

### F. After the acquisition (DKS on the Foot Locker banner)
- Ed Stack (Executive Chairman), DKS call 2025-11-25 (VERIFIED):
  - "One of the reasons it's struggled is they haven't had access to some of the key product. They haven't had allocation of some of the product."
  - "We need to clean out the garage".
- DKS ER 2026-03-12 note (VERIFIED): $217.9M was charged to "write down and liquidate inventory from the Company's review of the Foot Locker Business".
- Stack, call 2026-03-12 (VERIFIED): "our NBA All-Star activation with Nike, Jordan, Adidas, and others ... sought-after launches that drove exceptional sell-throughs."
- **Q2 2026 (the quarter that overlaps Nike Q1 FY27).**
  - DKS ER 2026-08-25 p.1 (VERIFIED), Stack: "greater dependence on footwear launch and retro product. Not only were there fewer launches in the second quarter, but those launches performed below both industry and our expectations."
  - Navdeep Gupta (CFO), call 2026-08-25 (VERIFIED): comps reflected "fewer launches and weaker consumer response to key launches during the quarter."
  - Stack, same call (VERIFIED):
    - "the launch product in Q2 was disappointing in the marketplace, not just for us, but for the entire marketplace."
    - "inventory built up in parts of the industry, particularly within certain legacy footwear silhouettes and apparel franchises that simply are not resonating the way they once did."
  - Stack, opinion (VERIFIED): "I do not think this is a demand issue going forward from a footwear standpoint ... some of these older legacy silhouettes and franchises that have done so well have slowed and slowed relatively quickly."
  - The FY2026 Foot Locker outlook was cut from +1.5% to +3.0% comps and $110M to $150M segment profit, to -2.0% to 0.0% comps and a $(80)M to $(40)M loss (DKS ER 2026-05-27 vs 2026-08-25, VERIFIED).
  - DKS never names Nike or Jordan in the Q2 2026 materials.

## 4. Conclusion
The Foot Locker evidence does not support the pure form of the thesis. It splits into a supply part and a demand part.

**Supply cut is real and deliberate.**
- 2022 to 2023: Nike cut Foot Locker allocation, and FL said "Retro sell-throughs, albeit at reduced quantities, were very good."
- 2024 to early 2025: Nike managed the "big three" (AF1, Dunk, AJ1), and premium retros "were sellouts".
- Q2 2026: there were "fewer launches".

**Demand weakness is also documented, and it is the newer signal.**
- Q3 2024: "short-term pressure on some of the sell-throughs" in classics, with Nike DTC promotions. The classics cut came after oversupply showed up in sell-through and markdowns. It did not arrive out of the blue like a scarcity play.
- Q2 2025: "lower demand of key basketball footwear styles" (10-Q p.20).
- Q2 2026: even the reduced launch slate "performed below both industry and our expectations". Legacy silhouettes are "not resonating", and Foot Locker inventory rose about 17% (DERIVED) while comps were -3.6%.
- A pure scarcity strategy would show launches selling out and full-price selling rising. In the quarter that matters (Nike Q1 FY27), the evidence shows the opposite.

**Net read.** Moderately against "NOT demand" for mid-2026. The evidence is consistent with "supply cut plus demand softening", with the supply cut partly a response to weaker sell-through.

Limits:
- There are no Jordan-specific units, prices or sell-through rates.
- DKS does not name Nike or Jordan for Q2 2026.
- The EMEA promotional environment (international -3.3%) and FL's own turnaround (store closures, a 30% SKU cut) are confounders.
- The units vs price split and the full-price vs markdown split for Jordan cannot be separated from these documents.
