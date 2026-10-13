# Nike revenue by channel: NIKE Direct versus wholesale (FY2017 to Q1 FY2027)

**Prepared:** October 13, 2026. **Sources:** the revenue disaggregation note in each 10-K and 10-Q (parsed into `data/nike_channel_split.csv` by `scripts/sec_pipeline/channel_split.py`; every table sums to its reported total and matches `data/nike_filing_facts.csv`), plus MD&A text read in full (extracts with verbatim quotes in `research_notes/channel_extracts/`). Page numbers are printed pages. Q4 figures are **derived** (fiscal year minus nine months) because Nike files no Q4 10-Q. Nike does **not** disclose profit by channel, so nothing here measures channel margins directly.

**Definitions.** *NIKE Direct* = Nike-owned stores plus NIKE Brand Digital (app and websites). *Wholesale* = sales to retailers (Foot Locker, Dick's, JD Sports and so on). Converse reports the same split as "direct to consumer" and "wholesale." Shares below are Direct / (Direct + Wholesale), which excludes the small "Other" line.

## 1. The arc: build DTC to a peak, then unwind it

| Fiscal year | NIKE Direct | Wholesale | Direct share | Direct growth | Wholesale growth | Source |
|---|---|---|---|---|---|---|
| FY2017 | 9,082 | 23,078 | 28.2% |  |  | FY19 10-K p. 27 |
| FY2018 | 10,428 | 23,969 | 30.3% | +15% | +4% | FY19 10-K p. 27 |
| FY2019 | 11,753 | 25,423 | 31.6% | +13% | +6% | FY19 10-K p. 80 |
| FY2020 | 12,382 | 23,156 | 34.8% | +5% | -9% | FY20 10-K p. 88 |
| FY2021 | 16,370 | 25,898 | 38.7% | +32% | +12% | FY21 10-K p. 86 |
| FY2022 | 18,726 | 25,608 | 42.2% | +14% | -1% | FY22 10-K p. 85 |
| FY2023 | 21,308 | 27,397 | 43.7% | +14% | +7% | FY23 10-K p. 83 |
| FY2024 | 21,519 | 27,758 | 43.7% | +1% | +1% | FY24 10-K p. 84 |
| FY2025 | 18,783 | 25,883 | 42.1% | -13% | -7% | FY25 10-K p. 82 |
| FY2026 | 17,720 | 27,453 | 39.2% | -6% | +6% | FY26 10-K p. 83 |

- Direct revenue grew **2.4x** from FY2017 to FY2024 while wholesale grew 20%. Since the FY2024 peak, Direct has lost **$3.8 billion (-18%)**; wholesale is back to roughly its FY2024 level.
- The strategy language tracks the numbers. FY2021: "over the last three years we have significantly reduced the number of undifferentiated wholesale accounts" (FY21 10-K p. 37). FY2024: "increasing investment to elevate and differentiate our brand experience within our wholesale partners" (FY24 10-K p. 30). FY2025 and FY2026: "Repositioning NIKE Brand Digital as a full-price platform and reinvesting in wholesale distribution" (FY25 10-K p. 30; FY26 10-K).

## 2. Digital is the part of Direct that collapsed

| Fiscal year | NIKE Brand Digital ($B) | Growth (currency-neutral) | Source |
|---|---|---|---|
| FY2019 | 3.8 | +35% | FY19 10-K p. 28 |
| FY2020 | 5.5 | +49% | FY20 10-K p. 32 |
| FY2021 | 9.1 | +60% | FY21 10-K p. 33 |
| FY2022 | 10.7 | +18% | FY22 10-K p. 33 |
| FY2023 | 12.6 (recast to 12.4 in the FY24 10-K) | +24% | FY23 10-K p. 33 |
| FY2024 | 12.1 | -3% | FY24 10-K p. 35 |
| FY2025 | 9.6 | -20% | FY25 10-K p. 34 |
| FY2026 | 8.6 | -12% | FY26 10-K p. 33 |

- Digital has fallen **32%** from its FY2023 peak (my arithmetic on $12.6B to $8.6B). Nike-owned store sales were first given in dollars in FY2026: **$9.1 billion, -4%**, with comparable store sales -4% (FY26 10-K pp. 29, 33). So in FY2026 stores were slightly larger than digital within NIKE Direct.
- Q1 FY2027: digital -13%, Nike-owned stores -5% (Q1 FY27 release p. 1).

## 3. By region: North America swung furthest

Direct share of each segment's revenue:

| Fiscal year | North America | EMEA | Greater China | APLA | Converse | Source |
|---|---|---|---|---|---|---|
| FY2019 | 31.6% | 27.9% | 40.0% | 28.7% | 30.7% | FY19 10-K p. 80 |
| FY2020 | 35.3% | 29.7% | 43.1% | 32.2% | 34.3% | FY20 10-K p. 88 |
| FY2021 | 40.7% | 31.8% | 45.6% | 36.6% | 36.1% | FY21 10-K p. 86 |
| FY2022 | 47.6% | 32.9% | 45.9% | 40.7% | 41.9% | FY22 10-K p. 85 |
| FY2023 | 47.8% | 36.5% | 46.7% | 41.9% | 42.9% | FY23 10-K p. 83 |
| FY2024 | 48.6% | 37.1% | 43.5% | 41.6% | 43.1% | FY24 10-K p. 84 |
| FY2025 | 46.4% | 34.6% | 43.8% | 41.2% | 44.2% | FY25 10-K p. 82 |
| FY2026 | 41.7% | 32.7% | 44.3% | 39.5% | 44.1% | FY26 10-K p. 83 |

Dollar view ($ millions):

| Region | FY2019 Direct | FY2019 Wholesale | FY2024 Direct | FY2024 Wholesale | FY2026 Direct | FY2026 Wholesale |
|---|---|---|---|---|---|---|
| North America | 5,027 | 10,875 | 10,392 | 11,004 | 8,553 | 11,958 |
| EMEA | 2,736 | 7,076 | 5,045 | 8,562 | 4,111 | 8,461 |
| Greater China | 2,482 | 3,726 | 3,283 | 4,262 | 2,592 | 3,255 |
| APLA | 1,508 | 3,746 | 2,799 | 3,930 | 2,464 | 3,779 |
| Converse | 553 | 1,247 | 832 | 1,098 | 477 | 605 |
| NIKE, Inc. | 12,306 | 26,670 | 22,351 | 28,856 | 18,197 | 28,058 |

## 4. Quarter by quarter: the wholesale rebound is a North America story

| Quarter | NIKE Direct | Wholesale | Direct share | Direct growth | Wholesale growth | NA wholesale growth | NA Direct growth | Greater China wholesale growth | Source |
|---|---|---|---|---|---|---|---|---|---|
| Q1 FY24 | 5,357 | 6,983 | 43.4% | +6% | +0% | -8% | +7% | +7% | Q1 FY24 10-Q p. 17 |
| Q2 FY24 | 5,742 | 7,118 | 44.7% | +6% | -2% | -9% | +3% | +14% | Q2 FY24 10-Q p. 18 |
| Q3 FY24 | 5,351 | 6,588 | 44.8% | +0% | +3% | +5% | +2% | +10% | Q3 FY24 10-Q p. 19 |
| Q4 FY24 | 5,069 | 7,069 | 41.8% | -8% | +5% | +5% | -9% | +9% | derived: 2024 10-K minus 9M (Q3 10-Q) |
| Q1 FY25 | 4,687 | 6,410 | 42.2% | -13% | -8% | -11% | -11% | +8% | Q1 FY25 10-Q p. 15 |
| Q2 FY25 | 5,017 | 6,920 | 42.0% | -13% | -3% | -1% | -15% | -12% | Q2 FY25 10-Q p. 17 |
| Q3 FY25 | 4,723 | 6,155 | 43.4% | -12% | -7% | +2% | -10% | -20% | Q3 FY25 10-Q p. 18 |
| Q4 FY25 | 4,356 | 6,398 | 40.5% | -14% | -9% | -9% | -14% | -24% | derived: 2025 10-K minus 9M (Q3 10-Q) |
| Q1 FY26 | 4,514 | 6,839 | 39.8% | -4% | +7% | +11% | -3% | -8% | Q1 FY26 10-Q p. 15 |
| Q2 FY26 | 4,616 | 7,499 | 38.1% | -8% | +8% | +24% | -10% | -15% | Q2 FY26 10-Q p. 17 |
| Q3 FY26 | 4,539 | 6,466 | 41.2% | -4% | +5% | +11% | -5% | -11% | Q3 FY26 10-Q p. 18 |
| Q4 FY26 | 4,051 | 6,649 | 37.9% | -7% | +4% | +10% | -6% | -15% | derived: 2026 10-K minus 9M (Q3 10-Q) |
| Q1 FY27 | 4,142 | 6,804 | 37.8% | -8% | -1% | +9% | -6% | -28% | Q1 FY27 10-Q p. 14 |

- **The headline wholesale slowdown in Q1 FY2027 (-1%) hides two opposite moves**: North America wholesale **+9%** while Greater China wholesale **-28%**. In FY2026, North America wholesale rose 14% "including expanded distribution, higher shipments to existing partners and fewer marketplace management actions taken in the current year" (FY26 10-K p. 37).
- North America Direct has fallen every quarter since Q4 FY2024.
- Nike's FY2026 10-K says its marketplace actions should be completed "by the end of December 2026," and that "North America has made the most progress against these actions, while Greater China and Converse will take more time" (FY26 10-K p. 30). If that holds, comparisons should get easier from Q3 FY2027 (December to February).

## 5. Channel and gross margin: the sign flipped

- FY2019 to FY2022: Direct growth *helped* margin. "The increase in gross margin for fiscal 2022 was primarily due to higher margin in our NIKE Direct business" (FY22 10-K p. 34).
- FY2023: "Lower margin in our NIKE Direct business, driven by higher promotional activity to liquidate inventory" (FY23 10-K p. 34).
- FY2024: "Lower margin in our NIKE Direct business (decreasing gross margin approximately 40 basis points)" (FY24 10-K p. 36).
- FY2025: "Lower NIKE Brand ASP (decreasing gross margin approximately 180 basis points), primarily due to higher discounts and changes in channel mix" (FY25 10-K p. 35).
- FY2026: the wholesale shift now *helps* costs. "Lower warehousing and logistics costs (increasing gross margin approximately 20 basis points), primarily due to channel mix" (FY26 10-K p. 34). Q1 FY2027's 90 bps warehousing and logistics benefit fits the same pattern (Q1 FY27 10-Q p. 23).
- **Implication (my inference):** a wholesale sale carries a lower price to Nike than a full-price Direct sale but saves fulfilment and store cost. Nike does not publish channel margins, so whether the mix shift is net positive for operating margin cannot be proven from filings. This is a modelling assumption to state explicitly.

## 6. Wholesale concentration is rising

| Fiscal year | Top 3 U.S. customers, % of U.S. sales | Top 3 non-U.S. customers, % of non-U.S. sales | Source |
|---|---|---|---|
| FY2019 | 24% | 14% | FY19 10-K pp. 2 to 3 |
| FY2021 | 24% | 15% | FY21 10-K pp. 2 to 3 |
| FY2023 | 22% | 14% | FY23 10-K pp. 2 to 3 |
| FY2024 | 21% | 15% | FY24 10-K pp. 2 to 3 |
| FY2025 | 25% | 16% | FY25 10-K pp. 2 to 3 |
| FY2026 | 29% | 16% | FY26 10-K pp. 2 to 3 |

- No single customer is 10% or more of revenue in any year. The FY2026 risk factor says concentration "has increased and may continue to increase," citing "attrition as struggling retailers exit the market" (FY26 10-K p. 16, risk factors).
- **Open question to verify (not from Nike filings):** whether retailer consolidation (for example, any combination of large U.S. sporting goods chains) explains part of the jump from 21% to 29%. Check the retailers' own filings before using this.

## 7. Other definitions and caveats
- "Wholesale equivalent" revenue (which counted NIKE Direct's internal purchases as if wholesale) ran from $5.6B (FY2017) to $13.0B (FY2024) of internal sales, and was dropped from FY2025, so older gross margin bridges are not directly comparable (FY24 10-K p. 32).
- Digital figures were recast in the FY2024 10-K (FY2023 from $12.6B to $12.4B).
- Q4 FY2019 to Q4 FY2020 releases do not give quarterly channel dollars.
- The Greater China partner-run online store change (from January 2027) is **not in any filing**; it rests on Just Style (secondary, July 2026).

## 8. What this means for the thesis (my inference)
1. **Bull reading:** the DTC unwind is largely complete in North America, where wholesale is still growing 9% to 24% a quarter. Marketplace actions are scheduled to finish by December 2026, and the wholesale shift is lowering logistics costs. If digital stabilizes at a full-price base of roughly $8B to $9B, the channel mix stops being a drag from FY2028.
2. **Bear reading:** Direct is still shrinking 6% to 8% a quarter with no sign of a floor. Total wholesale growth has stalled because China wholesale is collapsing (-28%). U.S. growth relies on fewer, larger retailers (top three now 29% of U.S. sales), which shifts pricing power to them.
3. **The deciding test is sell-through:** is North America wholesale growth matched by retailer sell-through, or is it inventory build at partners? That needs the retailers' own filings and alternative data, not Nike's.
