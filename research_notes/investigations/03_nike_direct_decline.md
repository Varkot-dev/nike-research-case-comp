# Why NIKE Direct fell from $21.5B (FY2024) to $17.7B (FY2026)

> **Status: DRAFT (Oct 13, 2026).** Produced by the multi-agent investigation (one investigator, two adversarial reviewers, one revision round). Sources are cited inline; independent spot-check against source documents is in progress and results will be logged at the end of this file. Treat figures as provisional until marked verified.


**Prepared:** October 13, 2026 (revision 2 same day; see section 6). Research note for `research_notes/` (not yet merged into the repo).
**Question:** Why did NIKE Direct fall from $21.5B (FY24) to $17.7B (FY26), with digital down to $8.6B?

**Correction to the question's premise.** The $12.6B digital figure is **FY2023 as first reported** (FY23 10-K p. 33). The FY2024 10-K recast FY2023 to $12.4B and reports **FY2024 digital as $12.1B**: "NIKE Brand Digital sales were $12.1 billion for fiscal 2024 compared to $12.4 billion for fiscal 2023" (FY24 10-K p. 35). So over the FY24 to FY26 window, digital fell **$12.1B to $8.6B, which is -$3.5B** [my arithmetic].

**Labels:** [filing] = Nike 10-K or 10-Q. [Nike release] = Nike earnings call prepared remarks PDF; Nike labels these "UNOFFICIAL Transcript". [secondary] = press. [snippet only] = search-result text, not usable as evidence. [my arithmetic] = computed in `rh/py_direct/calc.py` from the cited inputs. [opinion] = management view, quoted but not treated as proof. [company release] = a peer company's own results release or annual report page.

**Scope:** "NIKE Direct" here means NIKE Brand only, excluding Converse. That is $21,519M in FY24 and $17,720M in FY26 (FY24 10-K p. 84; FY26 10-K p. 83; `data/nike_channel_split.csv`).

---

## 0. Short answer

1. **The decline is almost entirely digital.**
   - Digital fell about $3.5B and Nike-owned stores fell about $0.3B [my arithmetic].
   - So digital is about **92%** of the $3.8B. Because Nike rounds digital dollars to $0.1B, the rounding range is about 89% to 95%.
   - Store closures are a rounding error. The NIKE Brand owned fleet went from 910 to 874 stores (-4%), and in both years store sales moved in line with comparable store sales.
   - **Adjustment (new in revision 2):** Nike moved closeout liquidation from Nike Digital to Nike Factory stores starting in Q3 FY25. Part of the "digital" loss is therefore volume that moved into stores, not demand that left Direct. The size is not disclosed. Store-growth swings put it at roughly $0.1B to $0.3B [my arithmetic, T11]. On that range, digital's *own* share of the Direct decline is about 84% to 89%. It stays above 79% even at a generous $0.5B.
2. **By region (reported dollars):**

   | Region | Change in Direct | Share of the decline |
   |---|---|---|
   | North America | -$1,839M | 48% |
   | EMEA | -$934M | 25% |
   | Greater China | -$691M | 18% |
   | APLA | -$335M | 9% |

   Estimated regional digital declines, currency-neutral [my arithmetic, method in T3]: NA about -$1.72B, EMEA about -$1.12B, Greater China about -$0.55B, APLA about -$0.26B.
3. **Mechanism: mostly fewer units (traffic), with a FY25 price drag that later reversed.**
   - For NIKE Brand Digital specifically, every filing that gives a reason names traffic:
     - FY24 10-K p. 35: "reflecting reduced digital traffic."
     - Q2 FY26 10-Q p. 26 and Q3 FY26 10-Q p. 29: "with declines primarily due to reduced traffic."
     - FY26 10-K p. 33: same wording.
   - *Correction from revision 1:* the filings **do** cite price for NIKE Direct as a whole in FY25.
     - FY25 10-K p. 29: "a decrease in traffic across NIKE Direct and our actions to reduce supply ... through increased markdowns across NIKE Direct."
     - FY25 10-K p. 34: footwear ASP cut revenue by about 3 points, "primarily due to higher discounts and changes in channel mix."
     - Q2 FY25 10-Q p. 22: "a decrease in traffic and elevated promotional activity across NIKE Direct."
   - Sizing the price drag [my arithmetic, T9]:
     - **FY25:** the brand-level price residual (discounts net of strategic pricing and product mix) was about **-$0.59B**. That is at most about 23% of the FY25 digital decline, even if all of it fell on digital. Under the most extreme gross-margin allocation, the bound is $1.98B.
     - **FY26:** the residual reversed to about **+$0.43B**, because discounts fell.
     - **Net over FY24 to FY26:** about **-$0.16B**, or about 5% of the $3.5B digital decline.
   - So price explains part of FY25, but over the two years the decline is overwhelmingly fewer units sold.
   - Caveat: this is a brand-level net. Deeper digital markdowns could hide behind price increases elsewhere. Nike does not disclose digital ASP.
   - No filing or set of call remarks cites conversion.
4. **What cut the units.** The filings and call remarks name five Nike decisions:
   - **(a)** Classics supply cut, hardest on Nike Digital: "down nearly fifty percent versus the prior year on Nike Digital" in Q1 FY25.
   - **(b)** Full-price repositioning: fewer promotional days, lower markdown rates and tighter digital buys. North America went "from over 30 promotional days to zero" in January and February 2025.
   - **(c)** Paid-media cut. Nike said that as it "continue[s] to reduce investment in paid media," it expected digital traffic "down double digits in Fiscal 26."
   - **(d)** Allocation moved to wholesale.
   - **(e)** Liquidation moved to factory stores (item 1).

   Two external drivers act alongside them:
   - **(f)** Weaker consumer demand for Nike on digital and loss of share to competitors. This is partly supported and cannot be sized separately (T13, T14).
   - **(g)** Greater China market share loss plus the platform reset.
5. **How much of the decline could be brand-wide demand loss?** [my arithmetic, T13]
   - Owned-store comps were -1% (FY25) and -4% (FY26), and wholesale outside Greater China **rose** $702M.
   - If digital had followed the store comps, it would have lost only about **$0.6B** (17% of $3.5B). That rises to about $0.7B to $0.9B after adding back the liquidation transfer.
   - The other roughly $2.6B to $2.9B is specific to the digital channel.
   - That excess is the classics concentration on digital, the full-price reset and paid media, and a sneaker-launch and hype audience whose demand fell faster on Nike's own platform.
   - Demand-side evidence that survives:
     - Digital already fell in Q3 and Q4 FY24 (about -$0.4B against the prior year) while Nike was *more* promotional.
     - Traffic declines in Q1 FY25 were "more significant than we anticipated."
     - "Organic traffic continues to decline double digits" (Q1 FY26).
     - EMEA "traffic and demand remain soft" (Q1 FY26).
     - Peer DTC grew strongly over the same period: On DTC +88% CHF from 2023 to 2025, adidas e-commerce +6% cn (2024) and +16% cn for brand adidas (2025), Deckers DTC +22%.
6. **What the data cannot separate.** No public data allocate the roughly $3.5B digital decline among:
   - (a) classics supply,
   - (b) the full-price reset,
   - (c) paid media,
   - (f) the digital-specific part of the consumer pull-back.

   Nike does not disclose digital traffic, conversion, units, AOV, full-price share levels, franchise sales by channel or paid-media spend. Section 4 lists what would separate them.
7. **"Consumers moved to multi-brand retail" works only in North America** (T10).
   - NA: wholesale +$954M against Direct -$1,839M. That offsets up to about 86% at wholesale-equivalent value, as an upper bound.
   - Outside NA and Greater China: wholesale -$252M against Direct -$1,269M, so no net recapture.
   - Excluding Greater China (whose wholesale fell $1,007M on a separate market problem), global wholesale rose $702M. That offsets at most about 37% of the ex-GC Direct loss at wholesale-equivalent value.
   - *Revision 1 said "globally, Direct revenue was mostly not recaptured; it was lost."* That global figure was dominated by Greater China. The corrected reading: partial recapture in NA, none visible elsewhere. Wholesale outside NA was also hit by the same classics cut and returns, so the true counterfactual is unknown.

---

## 1. Verdict table

| # | Candidate explanation | Verdict | Quantified contribution (FY24 to FY26, $3,799M total) | Deciding evidence |
|---|---|---|---|---|
| 1 | **Digital vs stores: which part of Direct fell** | **Settled (with a transfer adjustment)** | Reported: digital about -$3.5B (92%), stores about -$0.3B (8%) [my arithmetic, T2]. Excluding the liquidation shift into stores (#12), digital's own share is about 84% to 89%. | Digital $12.1B to $8.6B (FY24 10-K p. 35; FY26 10-K p. 33). Store sales $9.1B in FY26 (FY26 10-K p. 33). |
| 2 | **Classic footwear supply cut, hardest on Nike Digital** (AF1, AJ1, Dunk) | **Supported. Largest single named driver; dollar share unresolved** | **No lower bound can be derived** (revision 2 withdraws the "at least about $1B" bound; see Revision log). The upper bound is the whole $3.5B. Window-consistent data: Q1 FY25 classics on digital about -50%. Q4 FY25 classics declines across all channels of more than 30% were "almost a $1 billion headwind," which implies Q4 FY24 classics revenue across all channels of at most about $3.3B [my arithmetic]. | Q4 FY24 remarks p. 9: "aggressively adjusting our forward-looking plans for these franchises on Nike Digital, where they have their highest share of business." Q1 FY25 p. 4: "down nearly fifty percent versus the prior year on Nike Digital." FY24 10-K p. 31: "specifically NIKE Brand Digital revenues in the fourth quarter of fiscal 2024." The ">$4 billion from peak" figure (Q2 FY26 p. 7; Q3 FY26 p. 7) has no stated peak period, and Q4 FY25 p. 14 measures mix "from the peak" without a date, so neither can be lined up with FY24 to FY26. |
| 3 | **Full-price repositioning of Nike Digital** (fewer promo days, lower markdown rates, tighter digital buys) | **Supported as a cause of lower traffic and units from January 2025; size unresolved** | Not quantified by Nike. Timing [my arithmetic, T6]: H2 FY25 digital -$1.2B vs H2 FY24; FY26 -$1.0B vs FY25. Classics and paid-media cuts overlap the same periods. | Q3 FY25 remarks p. 9: "from over 30 promotional days to zero." p. 15: "reducing promotional days, reducing markdown rates" and "For Nike Digital, we are tightening our buys to support a full price business model." Q1 FY26 p. 10: sitewide promo days cut "by more than fifty." FY25 10-K p. 30: "Repositioning NIKE Brand Digital as a full-price platform." |
| 4 | **Lower demand creation / digital marketing spend** | **Total spend: ruled out. Paid media inside it: partly supported, unquantified** | Demand creation **rose**: $4,285M (FY24), $4,689M (FY25), $4,754M (FY26); 8.3% to 10.1% to 10.2% of revenue [my arithmetic]. | FY25 10-K p. 35; FY26 10-K p. 34. Q3 FY25 remarks p. 15: "as we continue to reduce investment in paid media, we expect digital traffic to be down double digits in Fiscal 26." |
| 5 | **SNKRS / app / launch traffic decline** | **Partly supported (traffic is the stated mechanism); SNKRS-specific share unresolved** | Not separable. | FY24 10-K p. 35: "reduced digital traffic." Q4 FY24 p. 13: "lower traffic on fewer launches." Q1 FY26 p. 13: prior year "more concentrated on classic footwear franchises and sneaker launch." No SNKRS metrics disclosed. |
| 6 | **Product allocation shifted to wholesale** (incl. Amazon) | **Supported in NA only. Outside NA and GC: no net recapture visible. Global-net framing corrected** | NA: wholesale +$954M vs Direct -$1,839M, offsetting up to 86% at wholesale-equivalent value (upper bound). Ex-GC: +$702M vs -$3,108M, up to 37%. Ex-NA ex-GC: -$252M vs -$1,269M, 0% [my arithmetic, T10]. | Q1 FY25 p. 4: "rebalancing product allocations to our highest-traffic channel." FY26 10-K p. 37: NA wholesale +14% "including expanded distribution." Counterfactual caveat: wholesale was also cut by classics supply, returns and discounts (FY25 10-K p. 29). |
| 7 | **Consumer channel preference shift to multi-brand retailers** | **Partly supported (classics in Q4 FY24 to Q1 FY25); not separable from #6 after that** | Not separable from #6. | Q4 FY24 p. 8: classics underperformed on digital "even as they continue to drive retail sales growth at high full-price realization in multi-brand retail." |
| 8 | **Store closures** | **Ruled out as material** | At most about $0.1B (fleet -36 stores; store sales tracked comps) [my arithmetic, T5]. | FY25 10-K p. 34; FY26 10-K p. 33; store tables FY24 to FY26 10-K pp. 2 to 3. |
| 9 | **Greater China digital** (promotional market, 11.11 pullback, platform clean-up, share loss to domestic brands) | **Supported as a regional component** | GC Direct -$691M reported; GC digital about -$0.55B cn, 15% of the digital decline [my arithmetic, T3]. Share loss in GC overall is documented in `rh/gc_decline.md`: Nike's share of a six-brand tracked set fell from 28.7% (2023) to 20.0% (2025), as Anta group and adidas gained. The digital part of that share loss is not separable. | FY25 10-K p. 40 (GC digital -22%); FY26 10-K p. 39 (-29%). Q2 FY26 p. 11: 11.11 "approximate 35% decline." Q2 FY26 p. 10: "Our brands have consistently been off price for consumers, especially in digital" (GC). |
| 10 | **Foreign exchange** | **Ruled out (helped)** | Net about +$290M favorable over two years [my arithmetic, T4]. | FY25 10-K p. 34; FY26 10-K p. 33. |
| 11 | **Lower digital price per unit (markdowns, discounts)** | **Revised: partly supported for FY25; reversed in FY26; minor net over the window** (revision 1 said "ruled out") | Brand-level price residual: FY25 about -$586M, FY26 about +$427M, net about -$159M, about 5% of the digital decline [my arithmetic, T9]. FY25 upper bounds for Direct: $486M (pro rata) to $1,979M (all in Direct with a +100 bps pricing offset), from `rh/markdown_depth.md`. The digital-only share of these is undisclosed; factory stores took "increased markdowns" too. | FY25 10-K p. 29: "increased markdowns across NIKE Direct." FY25 10-K p. 34: lower ASP "primarily due to higher discounts and changes in channel mix." Q2 FY25 10-Q p. 22: "elevated promotional activity across NIKE Direct." Q3 FY25 remarks p. 10: margins hit by "higher markdowns on Nike Direct." Then Q4 FY25 p. 10: "On Digital, we saw a meaningful improvement in markdown rates." FY26 10-K p. 33: ASP decline "primarily due to channel mix" (discounts not named). Contrast: for Converse DTC, the filing does name "lower ASP due to higher discounts" (Q3 FY25 10-Q p. 37), so Nike names price when it drives DTC. For NIKE Brand Digital it names traffic. |
| 12 | **Intra-Direct transfer: closeout liquidation moved from digital to Nike Factory stores** (new) | **Partly supported; small; changes the digital/store split, not the Direct total** | About $0.1B to $0.3B [my arithmetic, T11]: the Q3 to Q4 FY25 store-growth swing of +4 pts is worth about $95M, and the H1 vs H2 FY26 lapping gap about $184M. The ceiling is the whole FY26 cn store decline of about $0.37B. Digital's own share of the Direct decline: 89% at $0.1B, 84% at $0.3B, 79% at $0.5B. | Q3 FY25 p. 15: "shifting closeout liquidation to our Nike Factory stores" and "For Nike Factory Stores, we are increasing markdowns to drive velocity of higher volumes of closeout inventory." Q4 FY25 p. 14: "continue liquidating excess inventory through our value stores." Global store growth: Q3 FY25 -2%, Q4 FY25 +2%, Q1 FY26 -1%, Q2 FY26 -3%, Q3 FY26 -5%, Q4 FY26 -7% (remarks pp. 10, 9, 10, 8, 9, 9). |
| 13 | **Consumer demand / brand-heat loss and share loss to competitors** (new as a separate candidate) | **Partly supported; not separable from Nike's own levers. Channel-neutral part bounded at about $0.6B to $0.9B** | If digital had followed owned-store comps (-1%, -4%), the loss would be about $0.60B (17% of $3.5B), or $0.7B to $0.9B with the transfer added back [my arithmetic, T13]. Any brand-wide demand loss above that would also have shown in stores and wholesale, and ex-GC wholesale rose. A *digital-specific* consumer pull-back (sneaker-launch and hype buyers) can sit inside the remaining roughly $2.6B to $2.9B, but no public data separate it from #2, #3 and #4. | Pre-reset leg: Q3 FY24 -4% and Q4 FY24 -10%, about -$0.4B vs prior year (approximate), with "higher promotions" (Q4 FY24 p. 8). Q1 FY25 p. 3: traffic declines "more significant than we anticipated." Q1 FY26 p. 13: "Organic traffic continues to decline double digits." Q1 FY26 p. 10: EMEA "traffic and demand remain soft." EMEA full-price test (T13): Q4 FY25 full-price digital revenue fell unless the prior full-price share was at most about 18% to 27%. Peers (T14): On DTC +88% (2023 to 2025), adidas e-commerce +6% cn (2024) and +16% cn for brand adidas (2025), Deckers DTC +22% (FY24 to FY26). |
| 14 | **Higher digital sales returns / return reserves** (new) | **Ruled out as material** | The sales-returns reserve rose $478M in FY25 and fell $178M in FY26, net +$300M [my arithmetic]. Even if all of it were digital, that is at most about 9% of the decline. Nike attributes the higher returns to **wholesale partners**. | FY25 10-K p. 83: returns reserve "$1,277 million and $799 million." FY26 10-K p. 84: "$1,099 million and $1,277 million." FY25 10-K p. 29: "higher sales returns with our wholesale partners." |
| 15 | **APLA market-structure changes** (distributor transitions or exits in SE Asia and India, Korea) (new) | **Ruled out** | APLA digital is only about -$0.26B (7%) in total [T3]. The FY25 and FY26 10-Ks name lower revenue in "Southeast Asia & India and Korea" but report no distributor transition, divestiture or market exit. The only transition (Chile, Argentina, Uruguay) was in FY23, booked in Corporate, and "did not have a material impact." | FY25 10-K p. 41; FY26 10-K p. 40; FY24 10-K p. 42. A search of the FY25, FY26 and Q1 FY27 filings for "divestiture," "held for sale" and "distributor operating model" found nothing. |

**Surviving explanations: 7.** All are partly or wholly supported, and they overlap:

1. Classics supply cut on digital (#2).
2. Full-price repositioning, including tighter buys (#3).
3. Paid-media and launch traffic (#4/#5).
4. Greater China reset and share loss (#9).
5. Consumer demand and share loss (#13). Its channel-neutral part is bounded at about $0.6B to $0.9B; the digital-specific part is unsized.
6. FY25 price drag (#11). Minor net over the window.
7. Liquidation transfer to factory stores (#12). This explains the digital/store split, not the Direct total.

In North America, the allocation shift (#6/#7) is the counterpart of #2, not an independent cause. Ruled out: store closures, FX, total marketing spend, returns, APLA market structure, and "global net channel shift."

---

## 2. Data tables

### T1. NIKE Direct by region, reported $M [filing; my arithmetic for changes]

| Region | FY2024 | FY2025 | FY2026 | Change FY24 to FY26 | % change | Share of total decline | Wholesale change FY24 to FY26 |
|---|---|---|---|---|---|---|---|
| North America | 10,392 | 9,088 | 8,553 | -1,839 | -17.7% | 48.4% | +954 |
| EMEA | 5,045 | 4,235 | 4,111 | -934 | -18.5% | 24.6% | -101 |
| Greater China | 3,283 | 2,887 | 2,592 | -691 | -21.0% | 18.2% | -1,007 |
| APLA | 2,799 | 2,573 | 2,464 | -335 | -12.0% | 8.8% | -151 |
| **NIKE Brand** | **21,519** | **18,783** | **17,720** | **-3,799** | **-17.7%** | 100% | **-305** |

Sources: FY24 10-K p. 84; FY25 10-K p. 82; FY26 10-K p. 83 (revenue disaggregation notes), via `data/nike_channel_split.csv`. URLs: https://www.sec.gov/Archives/edgar/data/320187/000032018724000044/nke-20240531.htm , .../000032018725000047/nke-20250531.htm , .../000032018726000088/nke-20260531.htm (mirror: https://investors.nike.com/sec-filings/all-sec-filings/content/0000320187-26-000088/nke-20260531.htm).

- Ranking check: Greater China has the largest **percentage** decline (-21.0%). North America has the largest **dollar** decline (-$1,839M), almost half the total.

### T2. Digital vs stores, global ($B) [filing; implied stores = my arithmetic]

| FY | NIKE Direct | Digital | Stores | Digital share of Direct | Source |
|---|---|---|---|---|---|
| FY2024 | 21.52 | 12.1 | 9.42 (implied) | 56.2% | FY24 10-K p. 35 |
| FY2025 | 18.78 | 9.6 | 9.2 (stated in FY26 10-K) | 51.1% | FY25 10-K p. 34; FY26 10-K p. 33 |
| FY2026 | 17.72 | 8.6 | 9.1 (stated) | 48.5% | FY26 10-K p. 33 |
| Change | -3.80 | **-3.5** | **-0.3** | | |

- Caveat: the FY24 10-K made "certain reclassifications ... between NIKE-owned retail stores and NIKE Brand Digital in the prior period" (FY24 10-K p. 35). That affects FY23, not the FY24 to FY26 comparison.

Currency-neutral growth rates:

| FY | Digital | Stores | Comparable store sales | Source |
|---|---|---|---|---|
| FY24 | -3% | n/a | +3% | FY24 10-K p. 35 |
| FY25 | -20% | 0% | -1% | FY25 10-K p. 34 |
| FY26 | -12% | -4% | -4% | FY26 10-K p. 33 |

### T3. Estimated regional digital vs stores [my arithmetic]

**Method.** For FY25, each region's MD&A gives currency-neutral growth for NIKE Direct (D), digital (d) and stores (s). Since D = w x d + (1 - w) x s, the FY24 digital weight is w = (D - s) / (d - s).

**Inputs** (FY25 10-K pp. 38 to 41):

| Region | D | d | s |
|---|---|---|---|
| NA | -12 | -19 | -1 |
| EMEA | -16 | -30 | +5 |
| Greater China | -12 | -22 | -6 |
| APLA | -3 | -9 | +4 |

**Check.** The four regional estimates sum to **$12,116M**, against reported FY24 digital of **$12.1B**. FY25 rolled forward sums to $9,595M against $9.6B reported. That is a close fit.

**Roll-forward.** Each FY24 estimate is rolled forward with the stated FY25 and FY26 regional digital and store growth rates (FY26 10-K pp. 37 to 40: NA digital -10% / stores -2%; EMEA -10% / -8%; GC -29% / -4%; APLA -9% / -1%).

| Region | Implied FY24 digital weight (rounding range) | Digital FY24 | Digital FY26 (cn) | Digital change | Share of digital decline | Store change |
|---|---|---|---|---|---|---|
| North America | 0.611 (0.556 to 0.667) | 6,351 | 4,630 | -1,721 | 47.2% | -120 |
| EMEA | 0.600 (0.571 to 0.629) | 3,027 | 1,907 | -1,120 | 30.7% | -69 |
| Greater China | 0.375 (0.312 to 0.438) | 1,231 | 682 | -549 | 15.1% | -200 |
| APLA | 0.538 (0.462 to 0.615) | 1,507 | 1,248 | -259 | 7.1% | +38 |
| Total (cn) | | 12,116 | 8,467 | **-3,649** | 100% | **-351** |

- The reported change is -$3,799M. The remaining +$201M is FX and rounding, consistent with T4.
- Fit check: NA's estimated currency-neutral Direct change (-$1,841M) is within $2M of its reported change.
- **Reading:** EMEA's digital fell the most in percentage terms (about -37% over two years, against about -27% for NA) [my arithmetic]. Greater China's stores fell more than any other region's (about -$200M). APLA is the smallest contributor everywhere.
- **Caveat:** these are estimates. Nike does not disclose regional digital dollars, and the rounding ranges are wide for EMEA and APLA.

### T4. FX [my arithmetic from filing growth rates]

| Year | Reported change | Currency-neutral change (base x cn%) | Implied FX |
|---|---|---|---|
| FY25 | -2,736 | -2,582 (-12%) | -154 (±108 rounding) |
| FY26 | -1,063 | -1,503 (-8%) | +440 (±94 rounding) |

Net FX over the two years is about +$290M favorable. FX makes the reported decline smaller, not larger.

### T5. Store fleet [filing, 10-K Item 1 store tables pp. 2 to 3]

| FY end | US NIKE factory | US NIKE in-line | Non-US NIKE factory | Non-US NIKE in-line | NIKE Brand total | Leased stores worldwide (Item 2) |
|---|---|---|---|---|---|---|
| FY2024 | 211 | 85 | 561 | 53 | 910 | about 1,040 (FY24 10-K p. 26) |
| FY2025 | 213 | 85 | 543 | 61 | 902 | about 1,029 (FY25 10-K p. 25) |
| FY2026 | 212 | 75 | 537 | 50 | 874 | about 980 (FY26 10-K p. 25) |

- The fleet shrank by 36 stores (-4.0%) [my arithmetic].
- Store sales growth tracked comps: FY25 0% vs -1%; FY26 -4% vs -4%. So net openings and closures added about +1 pt in FY25 and 0 in FY26.
- **Store closures explain at most about $0.1B.** The $0.3B store decline is lower sales per comparable store.

### T6. Global digital by quarter ($B, currency-neutral growth) [filing for Q1 to Q3; Q4 = FY minus nine months, my arithmetic]

| Quarter | Digital $B | Growth | Event (same-period source) |
|---|---|---|---|
| Q1 FY24 | 2.9 | +2% | |
| Q2 FY24 | 3.5 | +1% | |
| Q3 FY24 | 3.0 | -4% | Decline begins while Nike is still promotional |
| Q4 FY24 | 2.7 | -10% | "softer traffic, higher promotions, and lower sales of certain classic footwear franchises" (Q4 FY24 remarks p. 8) |
| Q1 FY25 | 2.3 | -20% | Classics "down nearly fifty percent" on digital (Q1 FY25 p. 4) |
| Q2 FY25 | 2.8 | -21% | December still promotional (Q3 FY25 p. 11) |
| Q3 FY25 | 2.5 | -15% | Promo days cut in Jan and Feb 2025 (Q3 FY25 pp. 9, 11) |
| Q4 FY25 | 2.0 | -26% | Classics down over 30%; markdown rates improve (Q4 FY25 pp. 10, 14) |
| Q1 FY26 | 2.0 | -12% | "Organic traffic has slowed"; NA sitewide promo days cut by more than 50 (Q1 FY26 pp. 8, 10) |
| Q2 FY26 | 2.4 | -14% | GC 11.11 about -35% (Q2 FY26 p. 11) |
| Q3 FY26 | 2.3 | -9% | NA "continued improvement in average retail discounts" (Q3 FY26 p. 10) |
| Q4 FY26 | 1.8 to 1.9 | -12% | EMEA off-price down over 50% (Q4 FY26 p. 10) |
| Q1 FY27 | 1.8 | -13% | GC digital clean-up announced (Q1 FY27 p. 5) |

Notes on the table:
- Q4 FY26 is 1.9 if computed as FY less the sum of quarters, or 1.8 if computed as FY less the reported nine-month figure of 6.8. The difference is rounding.
- Growth sources: `data/nike_filing_facts.csv` rows `growth_nike_digital_pct`, `digital_sales_growth_pct`, `growth_nike_digital_cn_pct` (8-K Ex. 99.1 p. 1 and 10-Q MD&A pages).

**Half-year view [my arithmetic].**

| Half-year comparison | Digital change |
|---|---|
| H1 FY25 vs H1 FY24 | -$1.3B |
| H2 FY25 vs H2 FY24 | -$1.2B |
| H1 FY26 vs H1 FY25 | -$0.7B |
| H2 FY26 vs H2 FY25 | -$0.3B |

- About $1.3B of the $3.5B (37%) was lost **before** the January 2025 promo-day cut. That early loss comes from classics supply cuts and lower traffic, with "reduced promotional activity" only planned (Q4 FY24 remarks p. 13).
- About $2.2B came after the cut, when all three levers were active together.

### T7. Regional digital growth by quarter (cn) [filing 10-Q for Q1 to Q3; Nike release for Q4]

| Quarter | NA | EMEA | Greater China | APLA | Source |
|---|---|---|---|---|---|
| Q4 FY24 | -11% | -14% | +8% | -12% | Q4 FY24 remarks pp. 12 to 13 |
| Q1 FY25 | -15% | -24% | -34% | -15% | Q1 FY25 10-Q pp. 25 to 27 |
| Q2 FY25 | -22% | -32% | -4% | -8% | Q2 FY25 10-Q pp. 29 to 33 |
| Q3 FY25 | -12% | -25% | -20% | -8% | Q3 FY25 10-Q pp. 32 to 35 |
| Q4 FY25 | -25% | -36% | -31% | -6% | Q4 FY25 remarks pp. 10 to 12 |
| Q1 FY26 | -10% | -13% | -27% | -8% | Q1 FY26 10-Q pp. 25 to 28 |
| Q2 FY26 | -16% | -2% | -36% | -10% | Q2 FY26 10-Q pp. 30 to 34 |
| Q3 FY26 | -7% | -6% | -21% | -12% | Q3 FY26 10-Q pp. 33 to 38; remarks p. 10 |
| Q4 FY26 | -5% | -24% | -25% | -8% | Q4 FY26 remarks pp. 10 to 11 |

- EMEA swung from -2% (Q2 FY26) to -24% (Q4 FY26) in the same period as "aggressive actions to reduce promotions" and "off price was down over 50%" (Q4 FY26 p. 10). This is the cleanest single-region case of the promo cut driving the decline.
- North America digital stabilized to -5% to -7% in H2 FY26 as the promo comparisons lapped.

### T8. Demand creation [filing]

| FY | Demand creation $M | % of revenue [my arithmetic] | Nike's explanation |
|---|---|---|---|
| FY2024 | 4,285 | 8.3% | "higher advertising and marketing expense, digital marketing and sports marketing expense" (FY24 10-K p. 36) |
| FY2025 | 4,689 | 10.1% | "higher brand marketing expense, reflecting investment in key sports events" (FY25 10-K p. 35) |
| FY2026 | 4,754 | 10.2% | "higher sports marketing expense ... partially offset by lower brand marketing expense" (FY26 10-K p. 34) |

- FY26 by segment (FY26 10-K pp. 37 to 40, 42): NA +6% (sports marketing); EMEA +5%; Greater China -14% (lower brand marketing); APLA -1%; Converse -39%.
- Total spend rose. The cut was **paid media inside brand marketing**, which Nike does not size.

### T9. Price residual: FY25 drag and FY26 reversal [my arithmetic; inputs filing]

Script: `rh/py_direct2/calc2.py` (item 2). Inputs:
- Footwear ASP -3 pts and apparel flat in FY25 (FY25 10-K p. 34). Footwear -1 pt and apparel +1 pt in FY26 (FY26 10-K p. 33).
- Footwear and apparel weights of $29.5B and $13.0B (FY25), $13.4B (FY26 apparel), as used in `rh/py/markdown_calc.py`.
- Channel-mix effects of -0.77% (FY25) and -1.32% (FY26), from `rh/md/calc_out.txt` Tables C and D.

| Year | Brand revenue ASP effect | Of which channel mix | Residual (discounts net of pricing and product mix) | $M |
|---|---|---|---|---|
| FY25 | -2.08% | -0.77% | -1.31% | **-586** |
| FY26 | -0.38% | -1.32% | +0.94% | **+427** |
| Two-year net | | | | **-159** (about 5% of the $3.5B digital decline) |

Reading the table:
- FY25 alone: if the entire -$586M were digital, it would be 23% of the FY25 digital decline of about $2.5B.
- The gross-margin-based bounds in `rh/markdown_depth.md` (Table D) put the FY25 Direct discount at $486M (pro rata) to $1,979M (all in Direct, +100 bps pricing offset). On the extreme bound, that is 19% to 79% of the FY25 digital decline.
- Even the extreme case is a FY25 effect. FY26 discounts improved.
- **Limitation:** this is a brand-level *net*. Strategic price increases in wholesale could offset deeper digital markdowns. Settling it needs digital ASP or digital units, which Nike does not disclose.

### T10. Has partner wholesale recaptured lost Direct revenue? By region, FY24 to FY26, reported $M [filing; my arithmetic]

| Scope | Change in Direct | Change in wholesale | Direct loss at wholesale-equivalent value (x0.605) | Maximum share offset |
|---|---|---|---|---|
| Global | -3,799 | -305 | -2,298 | 0% |
| Excluding Greater China | -3,108 | +702 | -1,880 | 37% |
| Excluding GC and NA (EMEA + APLA) | -1,269 | -252 | -768 | 0% |
| North America | -1,839 | +954 | -1,113 | 86% |

- "Maximum" assumes every dollar of wholesale growth is recaptured Direct demand. In NA, wholesale growth also came from new doors, liquidation and lapping (`rh/na_wholesale.md`).
- In EMEA and APLA, wholesale was itself cut by the classics reduction, returns and discounts (FY25 10-K p. 29). Some recapture could therefore be hidden there. No data show it.

### T11. Liquidation transfer from digital to factory stores [filing and Nike release; my arithmetic]

Global NIKE store sales growth by quarter (currency-neutral):

| Quarter | Store growth | Source | Implied store $M (Direct minus digital, reported) |
|---|---|---|---|
| Q1 FY25 | +1% | Q1 FY25 remarks p. 8 | 2,387 |
| Q2 FY25 | n/a (comps -2%) | Q2 FY25 10-Q p. 25 | 2,217 |
| Q3 FY25 | -2% | Q3 FY25 remarks p. 10 | 2,223 |
| Q4 FY25 | +2% | Q4 FY25 remarks p. 9 | 2,356 |
| Q1 FY26 | -1% | Q1 FY26 10-Q p. 22 | 2,514 |
| Q2 FY26 | -3% | Q2 FY26 10-Q p. 26; remarks p. 8 | 2,216 |
| Q3 FY26 | -5% | Q3 FY26 10-Q p. 29; remarks p. 9 | 2,239 |
| Q4 FY26 | -7% | Q4 FY26 remarks p. 9 | 2,251 |

Implied store dollars carry about ±$50M to ±$100M of rounding, because digital is rounded to $0.1B.

Reading the pattern:
- Liquidation into factory stores was announced in March 2025 (Q3 FY25) and was planned "over the next two quarters" from June 2025 (Q4 FY25 p. 14).
- Store growth swung up 4 pts from Q3 to Q4 FY25. It then fell to -5% and -7% in H2 FY26 as that activity was lapped ("we then expect to see a modest headwind to revenue as we lap aggressive clearance activity," Q4 FY25 p. 14).
- Swing sizes: about $95M (Q3 to Q4 FY25) and about $184M (H1 vs H2 FY26 gap on the H1 store base).
- Ceiling: the whole FY26 cn store decline, about $368M.
- Central range: **$0.1B to $0.3B**.

| Transfer assumed | Digital's own share of the $3.8B Direct decline |
|---|---|
| $0 | 92% |
| $0.1B | 89% |
| $0.3B | 84% |
| $0.5B | 79% |
| $0.7B | 74% |

### T12. Returns reserve [filing]

| May 31 | Sales returns reserve $M | All sales-related reserves $M | Source |
|---|---|---|---|
| 2024 | 799 | 1,282 | FY25 10-K p. 83 |
| 2025 | 1,277 | 1,834 | FY25 10-K p. 83; FY26 10-K p. 84 |
| 2026 | 1,099 | 1,589 | FY26 10-K p. 84 |

- The returns reserve moved +$478M, then -$178M, so net +$300M over the window [my arithmetic].
- Nike ties the higher returns to wholesale partners (FY25 10-K pp. 29 to 30). A balance change is not the same as the revenue effect, so +$300M is an order of magnitude.

### T13. Separating channel-neutral demand loss from digital-specific causes [my arithmetic]

**Test 1: channel-neutral demand.**
- Owned-store comps were -1% (FY25 10-K p. 34) and -4% (FY26 10-K p. 33), for a cumulative factor of 0.9504.
- Applied to FY24 digital of $12.1B, that gives about **-$0.60B**, 17% of the digital decline.
- Adding back the transfer (T11) gives -$0.7B to -$0.9B (20% to 26%).
- Brand-wide demand loss beyond that would have shown in stores and wholesale. Ex-GC wholesale rose $702M (T10).
- Caveat: store comps include factory stores, which had extra liquidation volume. That is why the transfer is added back.

**Test 2: did full-price digital revenue fall (EMEA)?** A pure "Nike cut promotions" story predicts full-price demand flat or up, with only promotional sales lost.
- **Q4 FY25 EMEA:** digital was -36%, with "a double digit increase in the share of demand at full price" (Q4 FY25 p. 11).
  - If that means +10 points, full-price digital revenue fell unless the full-price share was 17.8% or less a year earlier.
  - At +15 points, the threshold is 26.7% or less.
  - If it means a +10% relative increase, full-price revenue fell about 30% regardless of the starting share.
- **Q4 FY26 EMEA:** digital was -24%, with "off price was down over 50%" (Q4 FY26 p. 10). With off-price down exactly 50%, full-price revenue fell unless off-price was at least 48% of EMEA digital a year earlier. At off-price shares of 20%, 30% and 40%, the full-price change would be -17.5%, -12.9% and -6.7%.
- **Reading:** unless EMEA digital was mostly off-price, full-price digital revenue fell too. Promo cuts alone cannot produce that. Classics supply cuts, tighter buys, paid-media cuts, or a genuine consumer pull-back can. This test rules out the pure promo-cut story for EMEA. It cannot separate the remaining causes, and Nike does not disclose the full-price share level.

**Test 3: the pre-reset leg.**
- Q3 FY24 digital was -4% and Q4 FY24 -10%. That is about -$0.13B and -$0.30B against the prior year (approximate, from reported dollars and cn growth).
- Nike cited "softer traffic, higher promotions" (Q4 FY24 p. 8).
- Digital fell even with more promotion, which is evidence of a demand-side component before the classics cut on digital took full effect.

### T14. Peer direct-to-consumer growth over the same window [company releases]

| Peer | Measure | Values | Change | Source |
|---|---|---|---|---|
| On | DTC net sales, CHF M | 2023 about 672.0 (derived: 942.8 at +40.3%); 2024 942.8 (+44.6% cc); 2025 1,260.5 (+39.9% cc) | +588.5 (+88% reported, 2023 to 2025) | On FY24 and FY25 releases (press.on-running.com) |
| adidas | E-commerce growth, cn | 2024 +6% (group; "pared back" by reduced discounting, lower Yeezy); 2025 +6% group, +16% brand adidas excl. Yeezy | n/a | adidas AR 2024 and AR 2025 income statement pages |
| adidas | DTC net sales, EUR M | 2024 9,490; 2025 9,931 (+9% cn) | +441 | adidas AR 2025 income statement |
| Deckers | DTC net sales, USD M | FY24 1,855 (+26.5%); FY25 2,130; FY26 2,264 (+6.3%) | +409 (+22.0%) | Deckers FY24 and FY26 releases |
| Nike | NIKE Brand Digital, USD B | FY24 12.1; FY26 8.6 | -28.9% | Nike 10-Ks |

- **Reading:** online and DTC demand for competing brands grew strongly while Nike Digital shrank. The online channel did not shrink for the category, so Nike lost share online.
- This does not show whether that share was taken from Nike by competitors or handed over by Nike's own supply, promo and media cuts.
- Calendar mismatch: On and adidas use calendar years and Deckers' fiscal year ends in March.

---

## 3. Verbatim quotes

**Filings**
- FY26 10-K p. 29 [filing]: "NIKE Direct revenues were $17.7 billion in fiscal 2026 compared to $18.8 billion in fiscal 2025, primarily driven by a decrease in traffic."
- FY26 10-K p. 33 [filing]: "On a currency-neutral basis, NIKE Direct revenues were down 8% due to declines in NIKE Brand Digital sales of 12% and declines in NIKE store sales of 4%. NIKE Brand Digital sales were $8.6 billion in fiscal 2026 compared to $9.6 billion in fiscal 2025, with declines primarily due to reduced traffic."
- FY25 10-K p. 29 [filing]: "Our results for fiscal 2025 reflected a decrease in traffic across NIKE Direct and our actions to reduce supply of certain footwear products in the marketplace through increased markdowns across NIKE Direct and discounts and higher sales returns with our wholesale partners."
- FY25 10-K p. 30 [filing]: "Marketplace Management: Repositioning NIKE Brand Digital as a full-price platform and reinvesting in wholesale distribution."
- FY25 10-K p. 34 [filing]: "NIKE Direct revenues decreased 12% due to declines in NIKE Brand Digital sales of 20% from $12.1 billion in fiscal 2024 to $9.6 billion in fiscal 2025, while NIKE store sales were flat."
- FY24 10-K p. 35 [filing]: "partially offset by declines in NIKE Brand Digital sales of 3%, reflecting reduced digital traffic."
- FY24 10-K p. 31 [filing]: "We are currently reducing the supply of certain footwear products ... This had a negative impact on our revenues, specifically NIKE Brand Digital revenues in the fourth quarter of fiscal 2024."
- FY25 10-K p. 35 [filing]: "Brand marketing expense includes advertising and promotion costs such as production and media costs, digital marketing expense, brand events and retail brand presentation costs."
- FY26 10-K p. 33 [filing]: "Lower ASP per pair was primarily due to channel mix, partially offset by product mix and strategic pricing."

**Nike call remarks** (PDF page numbers). URL pattern: https://s1.q4cdn.com/806093406/files/doc_financials/<year>/<q>/NIKE-Inc-Q#FY##-UNOFFICIAL-Transcript.pdf. Q1 FY27 is at https://s1.q4cdn.com/806093406/files/content_files/NIKE-Inc-Q1FY27-UNOFFICIAL-Transcript.pdf. The Q2 FY25 PDF returned 404 at the expected path and is not used.
- Q4 FY24, p. 8 [Nike release]: "Nike Digital declined 10% in the quarter ... we missed our Q4 plan on softer traffic, higher promotions, and lower sales of certain classic footwear franchises ... even as they continue to drive retail sales growth at high full-price realization in multi-brand retail."
- Q4 FY24, p. 9 [Nike release]: "we are aggressively adjusting our forward-looking plans for these franchises on Nike Digital, where they have their highest share of business."
- Q4 FY24, p. 13 [Nike release, outlook]: "lower Nike Digital growth, especially in the first half of the year, due to lower traffic on fewer launches, planned declines of classic footwear franchises given Q4 trends, as well as reduced promotional activity."
- Q1 FY25, p. 3 [Nike release]: "we delivered lower unit sales than we expected, partially offset by a higher ASP. Traffic declines across Nike Direct were more significant than we anticipated."
- Q1 FY25, p. 4 [Nike release]: "we have taken the most aggressive actions in Nike Direct, and especially Digital. In Q1, these franchises were down nearly fifty percent versus the prior year on Nike Digital, while we saw much better sales trends in wholesale. So, we are actively rebalancing product allocations to our highest-traffic channel."
- Q3 FY25, p. 9 [Nike release]: "comparing last year's January and February to this year's, Nike Digital in North America went from over 30 promotional days to zero."
- Q3 FY25, p. 11 [Nike release]: "in January and February we significantly reduced days of promotion in North America and EMEA. This resulted in a several percentage point improvement in demand at full price."
- Q3 FY25, p. 15 [Nike release]: "we are reducing promotional days, reducing markdown rates, and shifting closeout liquidation to our Nike Factory stores. Due to these actions, and as we continue to reduce investment in paid media, we expect digital traffic to be down double digits in Fiscal 26." Also: "For Nike Digital, we are tightening our buys to support a full price business model."
- Q4 FY25, p. 14 [Nike release]: "In Q4, these declines accelerated to more than 30%, representing almost a $1 billion headwind to revenue."
- Q1 FY26, p. 8 [Nike release]: "Organic traffic has slowed. We are working to find the right assortment and marketing mix to consistently bring consumers back to our digital eco-system."
- Q1 FY26, p. 10 [Nike release]: "reducing the number of days of sitewide promotion by more than fifty, and lowering markdown rates as well as increasing share of demand at full price."
- Q1 FY26, p. 13 [Nike release]: "With a business in the prior year that was more concentrated on classic footwear franchises and sneaker launch, as well as a higher mix of off-price sales, traffic comps will remain under pressure."
- Q2 FY26, p. 7 [Nike release]: "classics footwear franchises are on track to decline from peak levels by more than $4 billion by fiscal year end."
- Q2 FY26, p. 11 [Nike release]: "We were less promotional during 11.11, resulting in an approximate 35% decline versus the prior year."
- Q3 FY26, p. 11 [Nike release]: "We were also more aggressive with promotions on Nike Digital at end of season, which resulted in higher markdowns and a higher off price mix" (EMEA).
- Q4 FY26, p. 10 [Nike release]: "Although Digital revenue declined, off price was down over 50% following aggressive actions to reduce promotions; this resulted in a 15 point improvement in full price realization" (EMEA).
- Q1 FY26, p. 7 [Nike release]: "the launch of the Nike Brand Store on Amazon, where we're driving stronger engagement and sales than anticipated." [opinion on performance]

---


**Added in revision 2 (filings)**
- Q2 FY25 10-Q p. 22 [filing]: "Our results for the second quarter and six months ended November 30, 2024, reflect lower wholesale shipments, increased sales-related reserves, a decrease in traffic and elevated promotional activity across NIKE Direct."
- Q3 FY25 10-Q p. 24 [filing]: "Our results for the third quarter of fiscal 2025 reflected a decrease in traffic across NIKE Direct and our actions to reduce supply of certain footwear products in the marketplace through increased markdowns, higher sales-related reserves and discounts."
- Q3 FY25 10-Q p. 37 [filing, Converse, for contrast]: "Direct to consumer revenues decreased 15% on a currency-neutral basis, primarily due to reduced traffic in North America and lower ASP due to higher discounts."
- Q1 FY25 10-Q p. 19 [filing]: "In the first quarter of fiscal 2025, we experienced a decline in traffic across NIKE Brand Digital and our retail stores which negatively impacted our revenues."
- FY25 10-K p. 34 [filing]: "Unit sales of footwear decreased 8%, while lower average selling price ("ASP") per pair reduced footwear revenues by approximately 3 percentage points. Lower ASP per pair was primarily due to higher discounts and changes in channel mix, partially offset by strategic pricing actions."
- FY25 10-K p. 35 [filing]: "Lower NIKE Brand ASP (decreasing gross margin approximately 180 basis points), primarily due to higher discounts and changes in channel mix, partially offset by strategic pricing actions."
- FY25 10-K p. 83 [filing]: "the Company's sales returns reserve balance, included within sales-related reserves, was $1,277 million and $799 million, respectively."
- FY26 10-K p. 84 [filing]: "the Company's sales returns reserve balance, included within sales-related reserves, was $1,099 million and $1,277 million, respectively."
- FY26 10-K p. 30 [filing]: "This includes liquidating inventory through increased markdowns across NIKE Direct, and higher sales returns and discounts with our wholesale partners."
- FY25 10-K p. 41 [filing]: "APLA revenues decreased 3% on a currency-neutral basis primarily due to lower revenues in Southeast Asia & India and Korea."
- FY24 10-K p. 42 [filing]: "the transition of our Chile, Argentina and Uruguay entities to a third-party distributor operating model did not have a material impact on APLA revenues."

**Added in revision 2 (Nike call remarks, PDF pages)**
- Q1 FY25 p. 3 [Nike release]: "we delivered lower unit sales than we expected, partially offset by a higher ASP. Traffic declines across Nike Direct were more significant than we anticipated."
- Q3 FY25 p. 10 [Nike release]: "Gross margins declined 330 basis points to 41.5% on a reported basis, due to higher markdowns on Nike Direct, higher wholesale discounts, inventory obsolescence, and product cost and channel mix headwinds."
- Q3 FY25 p. 15 [Nike release]: "For Nike Digital, we are tightening our buys to support a full price business model. For Nike Factory Stores, we are increasing markdowns to drive velocity of higher volumes of closeout inventory."
- Q4 FY25 p. 10 [Nike release] (NA): "On Digital, we saw a meaningful improvement in markdown rates, as well as a higher share of demand at full price in the quarter."
- Q4 FY25 p. 11 [Nike release] (EMEA): "Nike Digital also delivered improvement in markdown rates, as well as a double digit increase in the share of demand at full price."
- Q4 FY25 p. 14 [Nike release]: "Over the next two quarters, Nike will continue liquidating excess inventory through our value stores and select value partners. In the second half, we then expect to see a modest headwind to revenue as we lap aggressive clearance activity in the prior year."
- Q4 FY25 p. 14 [Nike release]: "we also finished Q4 down approximately 10 points from the peak as a percent of our total footwear mix." (peak period not stated)
- Q1 FY26 p. 10 [Nike release] (EMEA): "EMEA is furthest ahead in repositioning Nike Digital to a full price business, however, traffic and demand remain soft."
- Q1 FY26 p. 13 [Nike release]: "Organic traffic continues to decline double digits."
- Q2 FY26 p. 10 [Nike release] (GC): "Our brands have consistently been off price for consumers, especially in digital, affecting our premium positioning across the entire integrated marketplace."
- Q3 FY26 p. 7 [Nike release]: "by the end of this fiscal year, we will have intentionally reduced over 4 billion dollars of revenue from the peak levels of classics footwear franchises." (peak period not stated)
- Q3 FY26 p. 8 [Nike release]: "Despite making progress versus a year ago, digital is still too promotional."
- Q3 FY26 p. 11 [Nike release] (EMEA): "Sportswear was down double-digits, and sell-thru has not tracked with sell-in expectations."

**Added in revision 2 (peer company releases)**
- On FY24 release, https://press.on-running.com/on-announces-fourth-quarter-and-full-year-results-and-the-filing-of-its-annual-report-on-form-20-f-for-2024 [company release]: "net sales through the DTC sales channel increased by 40.3% to CHF 942.8 million, or by 44.6% on a constant currency basis."
- On FY25 release, https://press.on-running.com/on-announces-fourth-quarter-and-full-year-results-and-the-filing-of-its-annual-report-on-form-20-f-for-2025 [company release]: "net sales through the DTC sales channel increased by 33.7% to CHF 1,260.5 million, or by 39.9% on a constant currency basis."
- adidas AR 2024, https://report.adidas-group.com/2024/en/group-management-report-financial-review/business-performance/income-statement.html [company report]: "Within DTC, own retail posted growth of 15% versus the prior year ... while e-commerce revenues increased 6%. The continued focus on reducing discounting activity and improving the overall business mix on own online platforms pared back much stronger growth in e-commerce full-price sales."
- adidas AR 2025, https://report.adidas-group.com/2025/en/group-management-report-financial-review/business-performance/income-statement.html [company report]: "E-commerce sales increased 16%, with a continued focus on full-price propositions"; table row "Direct-to-Consumer (DTC) 9,931 9,490 5% 9% 14%".
- Deckers FY24 release, https://ir.deckers.com/news-events/press-releases/detail/240/deckers-brands-reports-fourth-quarter-and-full-fiscal-year-2024-financial-results [company release]: "DTC net sales increased 26.5% to $1.855 billion compared to $1.467 billion."
- Deckers FY26 release, https://ir.deckers.com/news-events/press-releases/detail/656/deckers-brands-reports-fourth-quarter-and-full-fiscal-year-2026-financial-results [company release]: "DTC net sales increased 6.3% to $2.264 billion compared to $2.130 billion."

---

## 4. What remains unresolved and the data that would resolve it

1. **Dollar split of the roughly $3.5B digital decline** among (a) classics supply, (b) full-price repositioning (promo days, markdown rates, tighter buys), (c) paid media, and (f) the digital-specific part of the consumer pull-back.
   - These overlap in time from Q4 FY24 onward.
   - The channel-neutral demand part is bounded at about $0.6B to $0.9B (T13). The rest is digital-specific, but it is not allocated among the four causes.
   - **Would resolve:**
     - nike.com and app digital sales by franchise (classics vs rest) by quarter;
     - promotional days and markdown rate by quarter and region;
     - sessions, conversion, units and AOV;
     - paid-media spend;
     - organic vs paid traffic.
   - Third-party proxies, seen only as snippets in this session [snippet only, not used]:
     - Similarweb nike.com visits;
     - Sensor Tower or Apptopia Nike App and SNKRS active users;
     - card panels (Consumer Edge, Earnest) split by nike.com vs retailers.
   - A card panel that shows Nike brand spend across all retailers would separate "consumers left Nike" from "consumers bought Nike elsewhere."
2. **Digital ASP vs units, especially in FY25.**
   - The brand-level price residual nets to about -$0.16B over two years (T9).
   - But a larger digital markdown offset by wholesale price rises cannot be excluded.
   - **Would resolve:** digital ASP or digital units, or a Direct-margin bridge line for FY25 and FY26. Nike stopped publishing the internal-sales line after FY24.
3. **EMEA full-price share level** (T13 test 2). Nike reports changes in the full-price share ("double digit increase," "15 point improvement") but not the level.
   - If the full-price share of EMEA digital was above about 18% to 27% in Q4 FY24, full-price digital revenue fell in Q4 FY25.
   - That would show demand or supply loss beyond the promo cut.
4. **Size of the liquidation transfer into factory stores** (T11). **Would resolve:** factory vs in-line store sales, or closeout units by channel.
5. **How much of NA wholesale growth is recaptured Direct demand** (T10). **Would resolve:**
   - Amazon Nike-store sales;
   - sales by account (new vs existing doors);
   - retailer Nike sell-through by category (see `rh/na_wholesale.md`).
6. **The H1 FY25 loss of about $1.3B: demand problem or supply choice?** **Would resolve:** classics in-stock rates on nike.com from Q4 FY24 to Q2 FY25.
7. **SNKRS.** No Nike disclosure. **Would resolve:** launch counts and app active users.
8. **Greater China digital by platform** (Nike flagship stores on Tmall, JD and Douyin vs third parties) and 11.11 GMV split.
9. **Classics "from peak" base period.**
   - Nike has not said in which year classics peaked. If it was FY24, the ">$4 billion" reduction would cover the full FY24 to FY26 window.
   - **Would resolve:** a Nike statement of the peak year, or classics revenue by year.

## 5. Process notes
- **Downloads:**
  - `rh/dl/direct/` and `rh/dl/transcripts/`: Nike call remarks PDFs Q4 FY24 to Q1 FY27.
  - `rh/dl/peers/`: On, adidas, Deckers pages.
  - 10-K and 10-Q text was reused from `scratchpad/sec/pages/` (investors.nike.com mirror, paged with printed-page footers).
- **Calculations:**
  - `rh/py_direct/calc.py` (revision 1).
  - `rh/py_direct2/calc2.py` (revision 2; output in `rh/py_direct2/calc2_out.txt`).
  - Page lookups: `rh/py_direct/pdfpage.py` for PDFs, `rh/py_direct2/pg.py` for paged filing text.
- **Reused from sibling notes:**
  - FY25 markdown bounds from `rh/markdown_depth.md` (`rh/md/calc_out.txt`).
  - Greater China share data from `rh/gc_decline.md`.
  - Peer footwear figures from `rh/footwear_decline.md`.
- **Seen only as snippets (not evidence):** Statista or Similarweb nike.com visit counts; Digital Commerce 360 recap.

## 6. Revision log

**Revision 2 (October 13, 2026), responding to two reviewer objections ("weakened").**

1. **Fixed a failed source check: "Nike's filings never cite price or conversion" and verdict #11 "ruled out."** This was wrong.
   - What the filings say:
     - FY25 10-K p. 29 names "increased markdowns across NIKE Direct."
     - FY25 10-K p. 34 says lower footwear ASP (about -3 pts) was "primarily due to higher discounts and changes in channel mix."
     - Q2 FY25 10-Q p. 22 names "elevated promotional activity across NIKE Direct."
   - Short-answer item 3 now says the digital-specific filing language is traffic, while FY25 Direct also carried a price drag.
   - Verdict #11 is now "partly supported for FY25; reversed in FY26; minor net over the window," and is quantified in T9.
   - Revision 1 relied on call remarks and the FY26 ASP sentence only.
2. **Fixed a failed source check: the classics lower bound of "at least about $1B."** Withdrawn.
   - The ">$4 billion" figure is measured "from peak levels" (Q2 FY26 p. 7; Q3 FY26 p. 7) with no stated peak period, so it cannot be set against the FY24 to FY26 window.
   - Verdict #2 now gives no lower bound. It records only window-consistent facts: Q1 FY25 digital classics about -50%, and Q4 FY25 "almost $1 billion" on more than 30%.
3. **Corrected the global no-recapture claim** (verdict #6, short-answer item 7).
   - The -$305M global wholesale change was dominated by Greater China (-$1,007M).
   - T10 now splits it: NA up to 86% offset, ex-GC up to 37%, ex-NA ex-GC 0%.
   - The wording is changed from "lost, not recaptured" globally to "partial recapture in NA only; none visible elsewhere; counterfactual unknown."
4. **New candidate #12, liquidation transfer to factory stores.**
   - Tested with quarterly store growth (T11) and sized at about $0.1B to $0.3B.
   - Digital's own share of the Direct decline is now stated as about 84% to 89%, not 92%.
5. **New candidate #13, consumer demand / brand-heat and share loss.** Listed separately rather than folded into Nike's levers.
   - Tested three ways (T13): a channel-neutral bound using store comps (about $0.6B to $0.9B), an EMEA full-price-revenue test, and the pre-reset leg.
   - Peer DTC growth added in T14.
   - Verdict: partly supported. Its channel-neutral part is bounded; its digital-specific part is not separable from #2 to #4.
6. **New candidate #14, returns and return reserves.** Ruled out as material (net +$300M reserve change, attributed by Nike to wholesale; T12).
7. **New candidate #15, APLA market structure.** Ruled out: no transition or divestiture disclosed in FY25 or FY26, and APLA digital is only about 7% of the decline.
8. **Tighter digital buys** (Q3 FY25 p. 15) are added to #3 as part of the full-price repositioning, since Nike announced them as one program. They are not sized separately.
9. **Greater China domestic-brand share loss** is added to #9 from `rh/gc_decline.md`.
10. **Surviving count** changed from 4 to 7, because demand/share loss, the FY25 price drag and the store transfer are now listed separately. The statement "All four act through traffic, which is the only mechanism Nike names" is removed.
11. **Unchanged after re-check:** T1 to T8 figures, the 92% reported digital share, store closures immaterial, FX favorable, and total demand creation up.

Revision 1 is kept at `rh/direct_decline.rev1.bak.md`.
