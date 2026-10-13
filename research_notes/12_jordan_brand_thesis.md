# Jordan Brand: oversupply, a demand reset, and a supply cut that has not yet worked

**Prepared:** October 13, 2026. **Sources:** Nike 10-Ks FY2017 to FY2026, the Q1 FY2027 10-Q, earnings releases, and Nike's official earnings call transcripts (Q4 FY23, Q4 FY24, Q1 FY25 to Q1 FY27), plus opened secondary pages. Full extracts with verbatim quotes, URLs and verification status: `research_notes/jordan_extracts/JORDAN_SEC_FINDINGS.md` and `research_notes/jordan_extracts/JORDAN_MARKET_FINDINGS.md`. Charts: `charts/17_jordan_resets.png`, `charts/18_jordan_demand_tests.png`. The ten-way evidence test of October 13, 2026 is in `research_notes/jordan_extracts/rabbit_hole/`. Labels follow the house rules: filing citations, *Nike transcript*, *secondary*, *my arithmetic*, *my inference*.

## 1. The thesis in one paragraph

Jordan is Nike's only disclosed sub-brand and about 15% of revenue. It is **19% below its FY2024 peak** on a consistent basis and fell by mid-teens again in Q1 FY2027, a drop most readers miss because Nike changed how it reports Jordan in FY2025 (Section 2). We first framed the decline as a deliberate scarcity reset like FY2018. A ten-way evidence test (Section 5) rejects the pure version of that story. **What the evidence supports:** Nike oversupplied retro Jordans through FY2024, consumer interest and resale premiums fell while revenue was still rising, and Nike cut supply in response. The first cut (Air Jordan 1 High, 2024 to 2025) has not restored resale premiums, and the volume moved into Air Jordan 3 and 4, which then lost their premiums too. The broad retro cut announced on October 1, 2026 is the real test, and it lands in calendar 2027. Our estimate that about half of Jordan revenue runs through NIKE Direct (Section 4) still stands and ties Jordan to the digital collapse. For the pitch this is a falsifiable "show me" call, not a hidden-value call: the holiday 2026 retros, the November 16 to 17 Investor Day and the Q2 FY2027 call will show whether fewer pairs bring prices back.

## 2. The number most people have wrong

- **Headline:** "Jordan Brand products of $7,034 million, $7,270 million and $8,701 million in fiscal 2026, 2025 and 2024, respectively, decreasing 3% and 16% on a reported basis" (FY26 10-K p. 32, footnote 3).
- **Why it looks smaller than it is:** until FY2024, Nike reported Jordan on a *wholesale equivalent* basis, which priced Jordan sold through NIKE Direct at an internal wholesale price. From Q1 FY2025 "we have removed the non-GAAP financial measure of wholesale equivalent revenues" (Q1 FY25 10-Q p. 19), and prior years were "recast to conform to fiscal 2025 presentation" (FY25 10-K p. 33). FY2024 Jordan went from $6,988M (FY24 10-K p. 34) to $8,701M; FY2023 from $6,589M to $8,460M (FY25 10-K p. 33).
- **Consequence:** anyone chaining the old FY2024 figure ($6,988M) to the new FY2025 figure ($7,270M) sees growth of 4%. The filed figure is -16%. On a consistent basis, Jordan is **19% below peak** after FY2026 (my arithmetic: $7,034M / $8,701M).
- **Q1 FY2027:** "the Jordan Brand represented 13% of our global business with revenue falling by mid-teens" (Nike transcript, Q1 FY27 call, Oct 1, 2026). If the full year fell mid-teens, Jordan would be about $6.0B, roughly 31% below peak (my arithmetic, illustrative; Nike gives no full-year Jordan guidance).
- A second, smaller break: from FY2022, "unisex products are classified within Men's, and Jordan Brand revenues are separately reported" (FY22 10-K p. 32), moving FY2021 from $4,711M to $4,780M.

**Repo data note:** `revenue_jordan` in `data/nike_filing_facts.csv` holds each year's first-reported figure, so FY2023 and FY2024 are on the old basis and FY2025 and FY2026 on the new one. Use `revenue_jordan_reported_basis` (FY2023 to FY2026, added Oct 13, 2026) for any trend across FY2024 and FY2025.

## 3. The precedent: the FY2018 reset

| Fiscal year | Jordan growth (as filed) | Source |
|---|---|---|
| FY2018 | -8% | FY19 10-K p. 27 |
| FY2019 | +10% | FY19 10-K p. 27 |
| FY2020 | +15% | FY20 10-K p. 31 |
| FY2021 | +30% (recast) | FY22 10-K p. 32 |
| FY2022 | +7% | FY22 10-K p. 32 |
| FY2023 | +29% | FY23 10-K p. 32 |
| FY2024 | +3% (reported basis) | FY25 10-K p. 33 |
| FY2025 | -16% | FY26 10-K p. 32 |
| FY2026 | -3% | FY26 10-K p. 32 |

- Nike's own account: "Back in Fiscal 18, we recalibrated the supply of select Jordan Brand franchises ... we turned the page from double-digit declines in the Brand to the start of multiple consecutive years of strong double-digit growth" (Nike transcript, Q4 FY24 call, June 2024).
- On a like-for-like chain, Jordan was back above its FY2017 level within two years of the FY2018 reset and was about 2.3x its FY2018 trough by FY2024 (my arithmetic; chart 17).
- **The same playbook, stated explicitly in October 2026:** "we're going to get back to leading the scarcity model that we created. Simply put, we've been oversupplying our iconic retro product ... as we've done with the Air Jordan 1, we will deliberately reduce the volume and frequency of specific Jordan Retro launches. We've discussed it with our wholesale partners ... In the near term, North America will feel the biggest impact" (Nike transcript, Q1 FY27 call).
- **What is different this time (my inference):** the FY2018 reset was one year at -8%. This one is already two years and about -19%, with a further mid-teens drop in Q1 FY2027 and a second round of cuts. The 10-Q says "additional actions related to NIKE Sportswear and Jordan Brand are expected to extend beyond fiscal 2027," reflecting "higher levels of discounting and broader marketplace pressure" (Q1 FY27 10-Q p. 20). A deeper reset means a bigger rebound if the model holds, and a longer wait.

## 4. New estimate: Jordan is Nike's most DTC-dependent franchise

Nike does not disclose Jordan by channel. The FY2025 restatement lets us estimate it.

**Method (my inference):**
- The restatement replaced internal transfer prices with actual NIKE Direct retail revenue, so for any brand, *restated minus old* = Direct retail revenue minus the internal price of the same goods.
- For NIKE Brand as a whole in FY2024: internal sales to NIKE Direct were $13,009M (FY24 10-K p. 34) against NIKE Direct revenue of $21,519M (FY24 10-K p. 34). Internal price was therefore about 60.5% of Direct retail revenue (my arithmetic). The restatement check works: total NIKE Brand reported revenue ($49,322M) minus total wholesale equivalent revenue ($40,767M, FY24 10-K p. 34) is $8,555M, close to $21,519M minus $13,009M ($8,510M).
- Jordan's restatement gap was $1,713M in FY2024 and $1,871M in FY2023. Assuming Jordan's internal price ratio matches Nike's average, Jordan's Direct revenue was $1,713M / (1 - 0.605), about **$4.3B, or about 50% of Jordan revenue in FY2024**. FY2023 gives about 55%. NIKE Brand overall was 43.6%.

| Assumed internal price as % of Direct retail | 50% | 55% | 60.5% (Nike average) | 65% | 70% |
|---|---|---|---|---|---|
| Implied Jordan Direct share, FY2024 | 39% | 44% | 50% | 56% | 66% |

- **The robust part**, which needs only the "same ratio" assumption: Jordan accounted for 20% of the FY2024 restatement gap and 22% of FY2023's, against 17.6% and 17.3% of NIKE Brand revenue (my arithmetic). Jordan over-indexes to NIKE Direct either way.
- **Why it matters:**
  1. NIKE Brand Digital fell 32% from its FY2023 peak to $8.6B in FY2026 (`05_channel_split.md`). Retro launches were the core of the SNKRS and app model, so the Jordan decline and the digital decline are largely the same story told twice.
  2. Jordan is therefore the brand most exposed to Nike's shift from Direct to wholesale, and North America, where Direct has fallen every quarter since Q4 FY2024, is where "North America will feel the biggest impact."
  3. If the full-price digital reset works, Jordan has the most to gain: scarcity is easiest to enforce in channels Nike controls.
- **Caveats:** if Jordan's Direct sales ran at deeper discounts than average (factory stores), its internal price ratio is higher and the Direct share is higher still. If Jordan includes a larger mix of kids' or lower-priced product sold Direct, it could be lower. Treat 45% to 55% as the working range.

## 5. The ten-way evidence test (October 13, 2026)

Question: is the Jordan decline mainly a supply decision by Nike, or weaker demand? Each line of evidence was researched separately from primary documents where possible; extracts with verbatim quotes and verification labels are in `research_notes/jordan_extracts/rabbit_hole/`.

| Test | Result | Points to |
|---|---|---|
| Decomposition of the FY2024 to FY2026 fall | Jordan -19.2% against -6.0% for NIKE Brand excluding Jordan; Jordan was 17.6% of NIKE Brand but 41% of its decline. About 13 points are Jordan-specific; heavier NIKE Direct weighting explains about 1 point; currency helped by about 2 points (my arithmetic on FY26 10-K p. 32) | Jordan-specific cause |
| Market and category | US footwear flat in 2025 and +1% in H1 2026 (Circana, secondary); Nike North America footwear units +6% in FY2026 (FY26 10-K); Nike Basketball in North America "up double digits" (Nike transcript, Q1 FY27). adidas basketball -20% and -21% in Q1 and Q2 2026 (adidas investor decks), but adidas calls the business small | Market decline ruled out |
| Was the cut planned? | "The Jordan brand was planned down double digits this quarter, and we expect Jordan to be down at the same rate for fiscal '25" (Nike transcript, Q1 FY25 call); FY2025 came in at -16% (FY26 10-K p. 32) | Supply, for FY2025 |
| Release counts (Sole Retriever archive, 3,273 listings) | Core adult retro releases 98 (2023), 96 (2024), 113 (2025), about 91 (2026 incl. scheduled). AJ1 High fell from 20 to about 10 a year; AJ4 rose from 7 to 33 (2025) and AJ3 from 8 to 13 to 15 | Supply shifted between models, not cut in total; any cut was in pairs per release, which public data cannot show |
| Search interest (Google Trends, US, July to September) | "Jordan 1" fell 59% and "Air Jordan" 41% from 2021 to 2024, while Jordan revenue rose 32% from FY2022 to FY2024 (chart 18). Since the cuts, "Air Jordan" is flat; "Jordan 1" and "Jordan 4" are still falling; Samba, On and New Balance rose | Demand fell first, during oversupply |
| SNKRS app | Weekly US downloads fell from 101K to 32K in Q2 2023 (Sensor Tower, secondary) | Demand fell before the cuts |
| Resale premiums (GOAT, 247 general releases, Oct 13, 2026) | Median premium by release year: all retros +13% (2023), +6%, -5%, -19% (2026). AJ1 High OG -26%, -28%, -35%, -30%: 40 of 41 below retail, no recovery after its cut. AJ4 +18%, +24%, +4%, -20%; AJ3 +24%, +10%, -17%, -22% (my arithmetic; data/jordan_resale_goat_20261013.csv) | The cut has not restored scarcity; premiums fall wherever volume goes |
| Independent resale study | SneakerPing (Aug 18, 2026): 605 Jordan items, 70.7% last sold below retail, median -20% (opened). StockX: Jordan average resale price +6% in 2025, "early signs of recovery" (via SGB, opened) | Mostly demand-constrained, one positive signal |
| Retailers | Foot Locker 2023: retro "sell-throughs, albeit at reduced quantities, were very good"; Q4 2024: Retro 9, Retro 3 and Carolina 11 "were sellouts"; mid-2025 filing: "lower demand of key basketball footwear styles"; DICK'S Q2 2026: "fewer launches" that "performed below both industry and our expectations" and industry inventory up "in certain legacy footwear silhouettes"; Shoe Station units -4% and price and mix -3% with liquidation; Academy and Famous Footwear added Jordan doors in 2025 | Scarcity worked through late 2024, then stopped working |
| Nike's own words | "sell-through remains challenged, impacting both current discounting and future order books" (Nike transcript, Q4 FY26); "we've been oversupplying our iconic retro product" and "some aged, higher volume, sportswear footwear sold through below expectations" (Nike transcript, Q1 FY27); "higher levels of discounting" (Q1 FY27 10-Q p. 20) | Both |
| FY2018 analog | Same mechanism (retro cut, no price cut, North America first). Then: -8%, 3 quarters, inventory clean in 2 quarters, China growing 30% to 50%. Now: -19% over about 10 quarters in two waves, China -26%, discounting continuing. Mechanical timing: global Jordan growth around FY2028, North America around FY2029 | Recovery later than the FY2018 analog implies |

**Verdict (my inference, low to moderate confidence on the split).** Market, category, accounting and currency explanations are ruled out. The decline is Jordan-specific and comes from two linked causes:
1. **Oversupply eroded demand first.** Search interest, SNKRS downloads and resale premiums fell in 2022 to 2023 while Nike was still growing Jordan revenue. That is a supply mistake, not a planned reset.
2. **Nike then cut supply, and the cut has not yet restored pricing.** The AJ1 High cut did not lift AJ1 premiums; volume moved to AJ3 and AJ4, whose premiums then fell to AJ1 levels. Retailers report fewer launches and weaker results on each launch in mid-2026.

A rough split of the FY2024 to FY2026 decline is 35% to 50% supply Nike chose to withhold and 50% to 65% lower full-price sell-through, but **Nike discloses no Jordan units, average price or inventory, so the filings cannot separate the two.** That should be stated plainly in the pitch.

## 6. Bull case anchors

1. **The planned part was executed.** Nike said FY2025 would fall double digits and it fell 16%, which shows control over supply.
2. **Scarcity has worked recently.** Foot Locker reported retro sellouts and 300 bps higher merchandise margin on lower markdowns in Q4 2024, and the AJ4 Black Cat drove "our largest Black Friday ever" (Nike transcript, Q2 FY26).
3. **Brand-level interest has stabilized since the cuts.** "Air Jordan" search interest has been flat since 2024, and StockX reported Jordan average resale prices up 6% in 2025.
4. **The broad cut has not started yet.** Retro release counts did not fall in total through 2026. Hill's October 2026 cut covers all retro lines, so a recovery in premiums in 2027 would be the first real test of scarcity across the line.
5. **Room outside retro and outside North America.** Jordan grows where it is new to the shelf (Academy, Famous Footwear), Nike says penetration outside North America is "about 10 points lower" (Nike transcript, Q4 FY23), and Hill cites growth in Jordan cleats, golf and training (Q1 FY27).
6. **Peers recovered from resets.** adidas returned to growth in the fifth quarter after its 2023 reset and lifted operating margin from 1.3% (2023) to 8.3% (2025) (adidas releases, via rabbit_hole/peers.md).

## 7. Bear case anchors

1. **Demand fell before the cut.** "Jordan 1" search interest fell 59% from 2021 to 2024 while revenue rose (chart 18).
2. **The first cut failed the price test.** AJ1 High OG general releases from 2025 and 2026 trade 30% to 35% below retail, no better than 2023 releases; the AJ1 "Royal" released October 10, 2026 was 9% below retail after three days.
3. **Moving volume between models spreads the problem.** AJ4 and AJ3 premiums fell by about 40 points in two release years once their release counts rose.
4. **The reset is larger and longer than FY2018.** About 3.2% of Nike revenue lost against 0.7%, no China offset, and management already says pressure will "bleed in a little bit into fiscal '28" (Q1 FY27 call, via rabbit_hole/fy18_analog.md).
5. **Retailers carry the excess.** Foot Locker inventory up about 14% to 20% with comps -3.6% in mid-2026, and DICK'S reports brands promoting on their own sites.
6. **Taste is moving.** Samba, On and New Balance search interest rose sharply while retro Jordan models fell; JD's UK and Europe footwear mix shows retro basketball falling from about 37% to 18% of footwear sales from FY2024 to HY27 while running rose (JD slides, read from charts, about 1 point accuracy).

## 8. What would settle it

| Signal | Supply story wins if | Demand story wins if | When |
|---|---|---|---|
| Holiday 2026 retros (AJ4 Bred, AJ11 Space Jam, AJ12 Fireside) | Trade above retail on GOAT and StockX within 60 days | Trade below retail | Dec 2026 to Feb 2027; re-run the resale scripts |
| Re-price the same 247 shoes | AJ1 High premiums rise as AJ1 supply stays low | Premiums flat or falling | Quarterly |
| Investor Day | Jordan units, average price or inventory disclosed and units fall faster than revenue | No disclosure, or price falling with units | Nov 16 to 17, 2026 (Nike release, Oct 1, 2026) |
| Q2 FY2027 call | Jordan decline narrows from mid-teens with better full-price realization | Decline persists with discounting cited | December 2026 |
| Retailer launches | DICK'S, Foot Locker and JD report retro launches selling through at full price | "Launches performed below expectations" again | DICK'S and JD reports, Nov 2026 to Mar 2027 |
| Piper Sandler teen survey | Nike footwear mindshare above the 46% of Fall 2025 | Below 46% | Fall 2026 edition (timing unconfirmed) |

## 9. How to use this in the pitch (my inference)

- **Lead with the restatement.** Jordan is 19% below peak, not 3% down. Fully sourced and widely missed.
- **Then show the test, not the story.** Chart 17 shows interest fell while revenue rose, and resale premiums have not come back after the first cut. That makes the team credible: we tested management's scarcity claim and found it unproven.
- **Frame Jordan as a dated catalyst with a clear pass or fail.** If holiday 2026 retros trade above retail on fewer pairs, Jordan can repeat a version of FY2018 from FY2028. If they trade below retail, Jordan is a structural drag and should be valued at today's run rate or lower.
- **Do not overclaim.** No Jordan margin, units or inventory are public. The supply and demand split is an estimate. The resale data is a single snapshot from one marketplace.
