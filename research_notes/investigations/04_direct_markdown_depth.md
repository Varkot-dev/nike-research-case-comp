# NIKE Direct markdown depth, FY2022 to FY2026: was it above the 8% to 16% break-even?

> **Status: DRAFT (Oct 13, 2026).** Produced by the multi-agent investigation (one investigator, two adversarial reviewers, one revision round). Sources are cited inline; independent spot-check against source documents is in progress and results will be logged at the end of this file. Treat figures as provisional until marked verified.


**Prepared:** October 13, 2026 (revision 3). **Question:** What was NIKE Direct's average markdown depth (promotional intensity) from FY2022 to FY2026, and was it above the 8% to 16% break-even range derived in `research_notes/09_channel_margin_test.md`?

**Calculation scripts** (run with `python3 -I <script> <repo>`; both read `data/nike_filing_facts.csv` and `data/nike_channel_split.csv`):
- `scratchpad/rh/py/markdown_calc.py` (revision 1 and 2 tables A, B and the ratio history). Output: `scratchpad/rh/md/calc_out.txt`.
- `scratchpad/rh/py/markdown_calc_rev3.py` (this revision: joint offset conversion, break-even offsets, pricing caps, sensitivities, FY2026 regional bound, transfer-price bound). Output: `scratchpad/rh/md/calc_out_rev3.txt`.

Every derived number below comes from one of those scripts and is labelled **my arithmetic**.

**Labels used:** **filing** (10-K or 10-Q), **Nike release** (Nike's prepared remarks PDF on its IR site, which Nike marks "not an official transcript"), **secondary**, **snippet only** (not usable as evidence), **my arithmetic**, **opinion**.

## Bottom line

1. **Nike never discloses an average markdown depth.** No filing or set of prepared remarks from FY2022 to Q1 FY2027 gives a markdown percentage, a full-price sales share, a full-year count of promotional days or an off-price share of NIKE Direct. The only Nike release figures are partial:
   - North America digital went from "over 30 promotional days to zero" (January to February 2025 versus 2024).
   - There were "more than fifty" fewer days of sitewide promotion (Q1 FY2026).
   - There was a "several percentage point improvement in demand at full price" (Q3 FY2025).
2. **The 8% to 16% range in note 09 is an *incremental* markdown measured against the FY2024 realized Direct price, not a markdown off list price.**
   - At FY2024 prices, Direct sold at 1.654x the wholesale value of the same goods.
   - The thresholds equal Direct-to-wholesale ratios of 1.524x, 1.406x and 1.383x, which correspond to Foot Locker gross margins of 34.4%, 28.9% and 27.7%.
   - Nike's data measure realized price relative to the internal wholesale transfer price, not relative to MSRP. The question can only be answered on that basis.
3. **FY2022 to FY2024: not above the range, by construction, on Nike's transfer-price basis.** The realized ratio was 1.776x (FY22), 1.674x (FY23) and 1.654x (FY24). Every year was at or above the FY2024 base, so the incremental markdown versus FY2024 was zero or negative.
   - **New caveat (unresolved):** internal transfers are priced at what "external wholesale customers" pay. Closeouts may therefore be transferred at off-price, which would make 1.654x overstate Direct's price relative to *full-price* wholesale.
   - For that to place FY2024 itself at the 7.8%, 15.0% or 16.4% threshold, closeout dilution of the transfer base (closeout share times its discount to full-price wholesale) would need to be at least 7.8%, 15.0% or 16.4% (my arithmetic).
   - Nike gives no closeout share, so this cannot be tested.
   - For the channel decision note 09 is about, the off-price transfer price is the right comparator for closeout goods (opinion). The caveat therefore matters for reading the ratio as "promotional intensity", not for the break-even comparison.
4. **FY2025 full year: below 15% to 16.4% (strong, conditional only on Nike's pricing statements). Above 7.8% only if at least 62% to 100% of FY2025 discount dollars sat in NIKE Direct (unresolved).**
   - The incremental Direct markdown versus FY2024 lies between **2.5%** (discounts shared with wholesale pro rata, no pricing offset) and **9.8%** (all discounts in Direct, 100 bps pricing offset). Revision 2 printed 9.5%; that was an arithmetic error, fixed here.
   - Reaching 15.0% needs a pricing and product-mix offset of at least **239 bps** even with every discount dollar in Direct. That equals a uniform list-price increase of about 4.5% on all NIKE Brand revenue for the whole year (a 4% increase is worth 213 bps, a 5% increase 263 bps; my arithmetic).
   - Nike's own statements cap the offset far below that:
     - FY2024 increases were "low single- digit" (Q4 FY23 Nike release p. 15).
     - FY2025 pricing was only "from the prior year" (Q1 FY25 10-Q p. 22) and "decreasing" from Q2 (Q1 FY25 Nike release p. 10).
     - Pricing is not named in the Q3 FY2025 ASP line (Q3 FY25 10-Q p. 28).
     - Product mix is named as a *headwind* in Q2 FY2025 (Q2 FY25 10-Q p. 26).
   - Even giving FY2025 the full-year value of a 3% or 4% increase (161 or 213 bps), the all-in-Direct bound is 12.1% or 14.0%.
5. **FY2026 and the FY2024 to FY2026 cumulative: probably below 15%, but not excluded when three extreme assumptions stack.**
   - FY2026 has no ASP bridge line (the listed items sum to the +20 bps total), and only EMEA among the Nike Brand segments names "higher discounts" (FY26 10-K p. 38).
   - North America, 48.3% of NIKE Brand Direct revenue, had *higher* ASP from "strategic pricing and product mix" (FY26 10-K p. 37).
   - Treating EMEA's whole -140 bps gross margin decline as Direct discount adds 1.8% to the cumulative markdown. With a 100 bps cushion it adds 3.0%.
   - Cumulative versus FY2024 (my arithmetic):
     - **13.6% to 14.8%** when FY2025 gets the 3% pricing cap.
     - **15.5% to 16.6%** only when FY2025 also gets the 4% cap *and* all FY2025 discounts are in Direct.
6. **Worst quarters (all discounts in Direct; my arithmetic): 7.8% is crossed in Q2 FY25, Q4 FY25 and Q1 FY26 even with zero pricing offset. 15% needs at least 105 bps (Q2 FY25), 106 bps (Q4 FY25) or 174 bps (Q1 FY26) of offset.**
   - Q4 FY2025 is effectively excluded at 15%, because Nike's Q4 FY25 margin drivers name no pricing benefit (Q4 FY25 Nike release p. 9).
   - Q1 FY2026 is effectively excluded at 15%, because the new US price increase only began phasing in "beginning in Fall 25".
   - Q2 FY2025 at 15% remains open. It needs Q2 pricing worth about 2% of list price on top of a quarter (Q2 FY24) whose own full-price ASP line was already +320 bps.
7. **So the note 09 hypothesis ("the pivot is consistent with the data if Direct markdowns were above 8% to 16%") is not supported at the 15% to 16.4% thresholds for any full fiscal year.** It is possible at the 7.8% threshold for FY2025, but only if most FY2025 discounting sat in NIKE Direct rather than with wholesale partners. It is also possible at 15% for one quarter (Q2 FY2025) under extreme assumptions. Section 5 lists the disclosures that would settle each point.

## 1. Candidate explanations and verdicts

The question is a measurement. The "explanations" are therefore the competing readings of how deep NIKE Direct markdowns were, plus every way the bound itself could be wrong.

| # | Candidate explanation | Verdict | Quantified contribution (my arithmetic unless stated) | Deciding evidence |
|---|---|---|---|---|
| 1 | FY2025 full-year incremental Direct markdown exceeded **15.0% to 16.4%** | **Ruled out** for any offset consistent with Nike's "low single-digit" pricing | All-in-Direct: 9.8% at a +100 bps offset, 12.1% at the 3% cap (161 bps), 14.0% at the 4% cap (213 bps). 15.0% needs 239 bps; 16.4% needs 278 bps | FY25 10-K p. 35 (ASP -180 bps); Q4 FY23 Nike release p. 15 ("low single- digit price increases in FY24"); Q1 FY25 10-Q p. 22 ("from the prior year"); Q1 FY25 Nike release p. 10 ("decreasing benefit"); Q3 FY25 10-Q p. 28 (no pricing in ASP line) |
| 1b | FY2024 to FY2026 cumulative exceeded 15.0% | **Unlikely; not excluded** | 13.6% to 14.8% with FY25 at the 3% cap. 15.5% to 16.6% only with FY25 at the 4% cap, all FY25 discounts in Direct, and EMEA discounts all in Direct | FY26 10-K pp. 34, 37, 38 (no ASP line; North America ASP up; EMEA "higher discounts") |
| 1c | A single quarter exceeded 15% | **Q2 FY25 unresolved; Q4 FY25 and Q1 FY26 unlikely** | 15% needs offset ≥ 105 bps (Q2 FY25), ≥ 106 (Q4 FY25), ≥ 174 (Q1 FY26), all-in-Direct | Q2 FY25 10-Q p. 26 (pricing named, product mix a headwind); Q4 FY25 Nike release p. 9 (no pricing named); Q4 FY25 Nike release p. 13 (new price increase "beginning in Fall 25") |
| 2 | FY2025 incremental markdown exceeded **7.8%** | **Unresolved** | Exceeds 7.8% only if NIKE Direct bore at least 100%, 91%, 79%, 64% or 62% of gross FY25 discount dollars at offsets of 50, 69, 100, 150 or 161 bps. Pro rata it needs 291 bps (impossible under the cap) | Nike names Direct markdowns *and* wholesale discounts and returns in every FY25 description (FY25 10-K pp. 29, 30, 35). Returns reserve rose from $799M to $1,277M (FY25 10-K p. 83) |
| 3 | FY2022 to FY2024 Direct markdowns exceeded the range | **Ruled out on the transfer-price basis (by construction)**; level caveat unresolved (row 11) | FY22 to FY24 ratios are all ≥ the FY24 base, so incremental markdown ≤ 0. Peak-to-trough FY22 to FY24 fall: 6.9% (ratio), 7.3% (Nike's Direct-margin lines), 9.4% (also assigning all off-price margin lines to Direct) | FY22 10-K p. 32; FY23 10-K p. 32; FY24 10-K p. 34 (internal sales); Q3 FY23 10-Q p. 29; FY24 10-K p. 36 |
| 4 | The FY2022 to FY2023 swing was a timing effect of internal transfers, not markdowns | **Partly supported** | Ratio fell 5.8%. Implied -140 bps against Nike's -130 bps (9M FY23), so most of the swing is real price | Q3 FY23 10-Q p. 29 ("higher promotional activity to liquidate inventory") |
| 5 | The FY2025 ASP decline was mostly channel mix, not discounts | **Partly supported** | Mix explains about 42 of the 180 bps (23%) | Table C; FY25 10-K p. 35 |
| 6 | FY2026 Direct markdowns deepened again | **Ruled out in North America; small elsewhere** | Brand ASP line about 0 against -74 bps of channel mix. EMEA's whole -140 bps GM change equals at most 1.8% of NIKE Brand Direct revenue (3.0% with a 100 bps cushion) | FY26 10-K p. 34 (bridge); p. 37 (North America ASP up); p. 38 (EMEA discounts); pp. 39, 40 (Greater China and APLA GM changes "primarily due to" FX) |
| 7 | Strategic pricing or product mix masked deeper markdowns (size of the offset) | **Bounded by data** | FY25: Q1 gross pricing ≥ 69 bps; Q2 "decreasing"; Q3 pricing not named in the quarterly ASP line; Q4 FY25 not named. Full-year cap: 161 bps (3%) to 213 bps (4%). FY24 Q4 full-price ASP net of discounts already -27 bps (implied). FY26: total tariff mitigation of about 200 bps (320 gross to 120 net), which also covers supplier and partner cost-sharing | Table E2 sources |
| 8 | Mix inside Direct shifted toward Nike Factory, lowering the realized ratio without deeper per-item markdowns | **Irrelevant to the break-even verdict; unresolved for per-item depth** | The bound is built on the realized ratio, and intra-Direct mix sits inside the ASP residual that is assigned to discounts. So it is already inside the bound. It cannot be separated from per-item markdowns | Digital share of Direct fell from 59.1% (FY23) to 48.5% (FY26) (Table H) |
| 9 | Absolute markdown depth versus MSRP was above 8% to 16% | **Unresolved; not the note 09 quantity** | Not disclosed | n/a |
| 10 | Wholesale-partner discounting, not Direct markdowns, drove the FY2025 to Q1 FY2026 ASP hit | **Partly supported; this is the same open question as row 2** | Returns reserve +$478M (balance) | Q1 FY26 10-Q p. 19; Q3 FY25 Nike release p. 10 |
| 11 | **(New) Transfer-price confound:** closeouts are transferred to Direct at off-price wholesale prices, so the ratio hides factory markdowns | **Plausible; unresolved; does not change the break-even comparison** | FY22 to FY24 fall widens from 6.9% to at most 9.4% if all off-price margin lines are Direct. For FY24 to already sit at the 7.8% threshold, closeout dilution of the transfer base must reach 7.8% | FY24 10-K p. 32 (transfer at prices "comparable to those charged to external wholesale customers"); FY23 10-K p. 34 and FY24 10-K p. 36 keep a separate "off-price margin, on a wholesale equivalent basis" line |
| 12 | **(New) Inventory-obsolescence reserves moved markdown cost out of the ASP line** | **Ruled out as a source of hidden revenue loss** | Even if all 90 bps were treated as Direct markdown, FY25 reaches 15% only at a 149 bps offset (near the 3% cap) | A reserve writes down inventory *cost*. When the goods later sell at a low price, the revenue shortfall still appears in ASP. Counting both double-counts (opinion based on the accounting definition) |
| 13 | **(New) Wholesale returns liquidated through Nike Factory, so the loss lands in Direct** | **Plausible; inside the all-in-Direct bound** | Shifts the estimate toward the all-in-Direct rows (5.8% to 12.1%) and makes row 2 more likely. It cannot push the full year past 15% | Q4 FY25 Nike release p. 14: "liquidating excess inventory through our value stores and select value partners" (both channels) |
| 14 | **(New) Same unit cost in both channels (former A1) is false** | **Not needed for the bound; it bears on the note 09 threshold** | A markdown removes revenue whatever the channel cost. Nike does confirm Direct carries extra logistics in cost of sales: FY26 warehousing +20 bps "primarily due to channel mix" equals $93M, or about 8.7% of the $1,063M Direct revenue decline. That is a crude upper estimate, and it would *lower* the note 09 thresholds | FY26 10-K p. 34 |
| 15 | **(New) Rounding of the FY2026 bridge hides an ASP line of about -40 bps** | **Tested; small** | Adds 1.8 to 1.9 pts to FY26 m26 at offsets of 100 to 200 bps. Covered by the regional bound in row 6 | FY26 10-K p. 34 |

**Assumptions behind every bound (restated):**
- **A1 (replaced).** A markdown removes revenue with costs unchanged. This is true by definition and does not require equal unit cost across channels.
- **A2.** Nike's ASP bridge line contains discounts, channel mix, strategic pricing and product mix. Obsolescence sits in "other costs"; Converse and FX are separate lines.
- **A3.** The channel-mix effect is valued at the FY2024 ratio of 1.654x.
- **A4 (fixed).** Bps-to-dollar conversion is now joint. Gross discount plus mix dollars X solve (GP+X)/(Rev+X) minus GP/Rev = (ASP bps + offset bps). Revision 2 converted the two pieces separately and added them, which understated X.

## 2. Data tables built

### Table A: realized NIKE Direct price relative to the wholesale value of the same goods (filing data, my arithmetic)

Ratio = NIKE Direct revenue divided by internal sales "from our wholesale operations to our NIKE Direct operations, which are charged at prices comparable to those charged to external wholesale customers" (FY24 10-K p. 32).

| FY | NIKE Direct ($M) | Internal at wholesale prices ($M) | Ratio | Change vs prior year | Source |
|---|---|---|---|---|---|
| FY2019 | 11,753 | 7,127 | 1.649 | n/a | FY19 10-K p. 27 |
| FY2020 | 12,382 | 7,452 | 1.662 | +0.8% | FY20 10-K p. 31 |
| FY2021 | 16,370 | 9,872 | 1.658 | -0.2% | FY21 10-K p. 32 |
| FY2022 | 18,726 | 10,543 | 1.776 | +7.1% | FY22 10-K p. 32 |
| FY2023 | 21,308 | 12,730 | 1.674 | -5.8% | FY23 10-K p. 32 |
| FY2024 | 21,519 | 13,009 | 1.654 | -1.2% | FY24 10-K p. 34 |
| FY2025, FY2026 | 18,783; 17,720 | not disclosed | bounded below | | FY25 10-K p. 33; FY26 10-K p. 32 |

The disclosure ended deliberately. FY24 10-K p. 32: "Beginning in fiscal 2025, with the continued rollout of a new Enterprise Resource Planning Platform, the Company will replace wholesale equivalent revenues and gross margin drivers with a comparable U.S. GAAP metric." (filing)

### Table B: calibration against Nike's NIKE Direct margin line (my arithmetic)

| FY | Ratio change | Implied GM effect | Nike's Direct-margin line | Comparable period? |
|---|---|---|---|---|
| FY2022 | +7.1% | +148 bps | +160 bps (9M FY22, Q3 FY22 10-Q p. 30) | No: full year vs nine months |
| FY2023 | -5.8% | -140 bps | -130 bps (9M FY23, Q3 FY23 10-Q p. 29); quarters -90, -160, -140 | No: full year vs nine months |
| FY2024 | -1.2% | -27 bps | -40 bps (FY24 10-K p. 36) | **Yes** |

Only FY2024 is a like-for-like test (13 bps gap). FY2022 and FY2023 are indicative only, since Nike gave no full-year Direct line for those years: the FY22 and FY23 10-K bridges are unquantified (FY23 10-K p. 34). Nike's Direct line is itself on a "wholesale equivalent basis", so it cannot test the transfer-price confound (row 11).

### Table C: break-even thresholds (my arithmetic on note 09 inputs)

| Benchmark | Threshold ratio | Incremental markdown vs FY2024 |
|---|---|---|
| Foot Locker FY2021 GM 34.4% | 1.524x | 7.8% |
| Foot Locker FY2024 GM 28.9% | 1.406x | 15.0% |
| Foot Locker FY2023 GM 27.7% | 1.383x | 16.4% |

### Table D: FY2025 bound, joint conversion (filing bridge data, my arithmetic)

Inputs:
- FY25 revenue $46,309M and gross profit $19,790M (FY25 10-K p. 32).
- ASP line -180 bps (FY25 10-K p. 35).
- Direct $18,783M and wholesale $25,883M (FY25 10-K p. 33).
- Channel mix (Direct share of wholesale-equivalent value 31.9% to 30.5%): -$345M, or 42 bps.

| Pricing and product-mix offset | All-in-Direct: discount $M | All-in-Direct: incremental markdown | Implied ratio | Pro rata (42.1%): markdown |
|---|---|---|---|---|
| 0 | 1,158 | 5.8% | 1.558x | 2.5% |
| +50 | 1,592 | 7.8% | 1.525x | 3.4% |
| +100 | 2,035 | **9.8%** (was 9.5% in revision 2) | 1.492x | 4.4% |
| +150 | 2,486 | 11.7% | 1.461x | 5.3% |
| +161 (3% price cap) | 2,587 | 12.1% | n/a | 5.5% |
| +213 (4% price cap) | n/a | 14.0% | n/a | 6.4% |
| +250 | 3,414 | 15.4% | 1.400x | 7.1% |

**Break-even offsets (my arithmetic):**
- 7.8% needs 51 bps all-in-Direct or 291 bps pro rata.
- 15.0% needs 239 or 682.
- 16.4% needs 278 or 760.

**Revenue-ASP cross-check (unchanged):** footwear ASP -3 pts and apparel flat, so brand ASP was about -2.08%. Channel mix accounts for -0.77%, leaving a residual of -1.32% ($587M), net of pricing.

### Table E: break-even offsets by quarter (all discounts in Direct unless stated; my arithmetic, joint conversion)

| Period | ASP line (source) | Markdown at +0 / +100 / +150 | Offset for 7.8% (all-in / pro rata) | Offset for 15.0% | Offset for 16.4% |
|---|---|---|---|---|---|
| Q2 FY2025 | -330 (Q2 FY25 10-Q p. 26) | 11.0% / 14.8% / 16.6% | 0 / 156 | 105 | 144 |
| Q3 FY2025 | -150 (Q3 FY25 10-Q p. 28) | 4.5% / 8.3% / 10.2% | 87 / 327 | 285 | 326 |
| Q4 FY2025 | about -310 (derived: FY minus 9M; 9M -140, Q3 FY25 10-Q p. 29) | 11.1% / 14.8% / 16.5% | 0 / 174 | 106 | 146 |
| Q1 FY2026 | -250 (Q1 FY26 10-Q p. 22) | 8.1% / 12.1% / 14.0% | 0 / 246 | 174 | 212 |
| Q2 FY2026 | -50 (Q2 FY26 10-Q p. 27) | 0.0% / 2.0% / 4.3% | 232 / 496 | 408 | 445 |
| Q1 FY2027 | -30 (Q1 FY27 10-Q p. 23) | 0.0% / 3.8% / 6.0% | 191 / 452 | 363 | 400 |

Revision 2 printed 14.4% for Q2 FY25 at +100. The correct joint figure is 14.8%.

### Table E2: evidence on the size of the pricing and product-mix offset

| Period | Evidence | Label, source |
|---|---|---|
| FY2024 | Price increases were "low single- digit" | Nike release, Q4 FY23 PDF p. 15 |
| FY2024 by quarter | Full-price ASP net of discounts: +300 (Q1), +320 (Q2), +180 (Q3), +200 (FY). Implied Q4 about **-27 bps** | Filing (Q1 FY24 10-Q p. 24; Q2 FY24 10-Q p. 28; Q3 FY24 10-Q p. 29; FY24 10-K p. 36); Q4 is my arithmetic |
| Q4 FY2024 outlook | "partially offset by higher markdowns" | Nike release, Q3 FY24 PDF p. 15 |
| Q1 FY2025 | ASP +40 bps "primarily due to benefits from strategic pricing actions from the prior year". With 29 bps of mix headwind, gross pricing was ≥ 69 bps | Filing, Q1 FY25 10-Q p. 22; my arithmetic |
| Q2 FY2025 | Guidance: "decreasing benefit from strategic pricing actions". The ASP line names "product mix" as a *negative* | Nike release, Q1 FY25 PDF p. 10; filing, Q2 FY25 10-Q p. 26 |
| Q3 FY2025 | Quarterly ASP line: "primarily due to higher discounts and changes in channel mix" (no pricing named). The 9M line still names pricing | Filing, Q3 FY25 10-Q pp. 28, 29 |
| Q4 FY2025 | GM drivers: "higher wholesale discounts, higher discounts in our Nike factory stores, supply chain cost deleverage and channel mix headwinds" (no pricing) | Nike release, Q4 FY25 PDF p. 9 |
| FY2026 | "surgical price increase in the United States, with phased implementation beginning in Fall 25" | Nike release, Q4 FY25 PDF p. 13 |
| FY2026 | Tariffs: "gross headwind of approximately 320 basis points ... net impact of approximately 120 basis points". Total mitigation is about 200 bps, from all actions including supplier and retail-partner cost-sharing | Nike release, Q2 FY26 PDF p. 8; my arithmetic |
| Cap arithmetic | A uniform price increase on all NIKE Brand revenue is worth 55 bps (1%), 108 (2%), 161 (3%), 213 (4%) or 263 (5%) of FY25 gross margin | My arithmetic |

**Reading (opinion):** FY2025's benefit was a fading rollover of a low single-digit FY2024 increase. It was named in Q1 and Q2 only, and product mix worked against it in Q2 and Q3. The full-year offset was therefore most likely 50 to 100 bps. The 3% cap (161 bps) is a generous ceiling. The 239 bps needed for 15% is not consistent with these statements.

### Table F: FY2026 and the cumulative FY2024 to FY2026 bound (my arithmetic)

**FY2026 bridge:**
- Listed items (warehousing +20, FX +20, other costs +20, Converse -20, product costs -20) sum to the reported +20 bps (FY26 10-K p. 34). There is no ASP line.
- Note: FY26 gross margin includes a 210 bps IEEPA tariff recovery inside cost of sales (Q4 FY26 Nike release PDF p. 9; FY26 10-K p. 30). It is a cost item and does not touch ASP.
- Channel mix at 1.654x: -$605M, or 74 bps.

**Segment statements (filing, FY26 10-K):**
- North America p. 37: "Higher ASP primarily reflects strategic pricing and product mix, partially offset by channel mix."
- EMEA p. 38: "primarily due to lower ASP, reflecting higher discounts, and unfavorable changes in standard foreign currency exchange rates" (-140 bps).
- Greater China p. 39 (-30 bps) and APLA p. 40 (-200 bps): "primarily due to unfavorable changes in standard foreign currency exchange rates."

| FY25 assumption | FY26 Direct increment | Cumulative vs FY24 | Implied FY26 ratio |
|---|---|---|---|
| FY25 at 3% cap (12.1%), EMEA 140 bps all Direct (1.8%) | 1.8% | 13.6% | 1.428x |
| FY25 at 3% cap, EMEA 240 bps (3.0%) | 3.0% | 14.8% | 1.410x |
| FY25 at 4% cap (14.0%), EMEA 140 bps | 1.8% | 15.5% | 1.397x |
| FY25 at 4% cap, EMEA 240 bps | 3.0% | 16.6% | 1.379x |

- EMEA gross profit is not disclosed, so the conversion uses the company FY26 gross margin as a proxy (assumption). EMEA 240 bps equals an 11.8% markdown on EMEA Direct alone.
- The older bridge-only method, with FY26 offsets of 100 to 200 bps and an unlisted ASP line of 0 or -40 bps, gives FY26 increments of 1.2% to 7.5%. That is wider, because it ignores the segment statements. With FY25 at +100, cumulative 15% needs a FY26 offset of 200 bps (ASP 0) or 160 bps (ASP -40).

### Table G: transfer-price confound bound (filing bridge lines, my arithmetic)

| Change | Direct line only | Direct plus off-price margin line | Sources |
|---|---|---|---|
| FY22 to FY23 | -5.7% of Direct revenue (9M -130 bps) | -7.0% (adds Q3 FY23 off-price -30 bps; no 9M figure given) | Q3 FY23 10-Q p. 29 |
| FY23 to FY24 | -1.7% (-40 bps) | -2.6% (-60 bps) | FY24 10-K p. 36 |
| FY22 to FY24 cumulative | 7.3% | 9.4% | my arithmetic |

- Nike's FY22 to FY24 bridge separates "NIKE Direct" margin from "off-price margin, on a wholesale equivalent basis" and from the "mix of full-price sales, on a wholesale equivalent basis" (+70 bps in 9M FY22, Q3 FY22 10-Q p. 30). That is consistent with factory-store closeouts being measured against an off-price wholesale price, but it does not prove it.
- Algebra (my arithmetic): if a share c of FY24 transfers was closeout priced at k times full-price wholesale, the full-price-basis ratio is 1.654 × (1 - c(1 - k)). FY24 would sit at the 7.8%, 15.0% or 16.4% threshold when c(1 - k) = 7.8%, 15.0% or 16.4%.

### Table H: digital share of NIKE Direct (filing data, my arithmetic)

| FY | Digital ($B) | NIKE Direct ($B) | Digital share | Source |
|---|---|---|---|---|
| FY2022 | 10.7 | 18.73 | 57.1% | FY23 10-K p. 33 |
| FY2023 | 12.6 | 21.31 | 59.1% | FY23 10-K p. 33 |
| FY2024 | 12.1 | 21.52 | 56.2% | FY24 10-K p. 35 |
| FY2025 | 9.6 | 18.78 | 51.1% | FY25 10-K p. 34 |
| FY2026 | 8.6 | 17.72 | 48.5% | FY26 10-K p. 33 |

## 3. Verbatim quotes with sources

Nike filing URLs follow `https://investors.nike.com/sec-filings/all-sec-filings/content/<accession>/<file>`.
- FY22 10-K: 0000320187-22-000038/nke-20220531.htm
- FY23 10-K: 0000320187-23-000039/nke-20230531.htm
- FY24 10-K: 0000320187-24-000044/nke-20240531.htm
- FY25 10-K: 0000320187-25-000047/nke-20250531.htm
- FY26 10-K: 0000320187-26-000088/nke-20260531.htm
- Q3 FY22 10-Q: 0000320187-22-000017/nke-20220228.htm
- Q1 FY23 10-Q: 0000320187-22-000058/nke-20220831.htm
- Q2 FY23 10-Q: 0000320187-23-000003/nke-20221130.htm
- Q3 FY23 10-Q: 0000320187-23-000013/nke-20230228.htm
- Q1 FY25 10-Q: 0000320187-24-000065/nke-20240831.htm
- Q2 FY25 10-Q: 0000320187-25-000004/nke-20241130.htm
- Q3 FY25 10-Q: 0000320187-25-000016/nke-20250228.htm
- Q1 FY26 10-Q: 0000320187-25-000097/nke-20250831.htm
- Q2 FY26 10-Q: 0000320187-25-000151/nke-20251130.htm
- Q3 FY26 10-Q: 0000320187-26-000037/nke-20260228.htm
- Q1 FY27 10-Q: 0000320187-26-000193/nke-20260831.htm

Q1 to Q3 FY24 10-Q quotes come from `data/nike_filing_facts.csv` (sec.gov archive URLs listed there).

Nike release PDFs are at `https://s1.q4cdn.com/806093406/files/doc_financials/<year>/q<n>/NIKE-Inc-Q<n>FY<yy>-UNOFFICIAL-Transcript.pdf`. The exception is Q1 FY27, which is under `files/content_files/`. The Q2 FY25 PDF returned 404 at that path and is not used.

**Filings (new or changed in this revision are marked "new")**
- FY24 10-K p. 32 (new): "internal sales from our wholesale operations to our NIKE Direct operations, which are charged at prices comparable to those charged to external wholesale customers. Beginning in fiscal 2025, with the continued rollout of a new Enterprise Resource Planning Platform, the Company will replace wholesale equivalent revenues and gross margin drivers with a comparable U.S. GAAP metric."
- FY24 10-K p. 36: "Higher NIKE Brand full-price ASP, net of discounts, on a wholesale equivalent basis (increasing gross margin approximately 200 basis points), primarily due to strategic pricing actions"; "Lower margin in our NIKE Direct business (decreasing gross margin approximately 40 basis points)"; "Lower off-price margin, on a wholesale equivalent basis (decreasing gross margin approximately 20 basis points)".
- FY23 10-K p. 34 (new): "Lower margin in our NIKE Direct business, driven by higher promotional activity to liquidate inventory"; "Lower off-price margin, on a wholesale equivalent basis." (no bps given).
- Q3 FY22 10-Q p. 30 (new): "Higher mix of full-price sales, on a wholesale equivalent basis, (increasing gross margin approximately 70 basis points)".
- Q3 FY23 10-Q p. 29 (new): "Lower off-price margin, on a wholesale equivalent basis (decreasing gross margin approximately 30 basis points)"; "Higher NIKE Brand full-price ASP, net of discounts, on a wholesale equivalent basis, (increasing gross margin approximately 370 basis points)".
- FY25 10-K p. 29: "increased markdowns across NIKE Direct and discounts and higher sales returns with our wholesale partners".
- FY25 10-K p. 35: "Lower NIKE Brand ASP (decreasing gross margin approximately 180 basis points), primarily due to higher discounts and changes in channel mix, partially offset by strategic pricing actions"; "Higher other costs (decreasing gross margin approximately 90 basis points), including higher inventory obsolescence reserves".
- FY25 10-K p. 83: "sales returns reserve balance ... was $1,277 million and $799 million, respectively".
- FY26 10-K p. 30 (new): "we recognized a benefit of $986 million in Cost of sales ... for the recovery of IEEPA tariffs paid".
- FY26 10-K p. 34: bridge items as listed in Table F; no ASP line.
- FY26 10-K p. 37 (new, North America): "Higher ASP primarily reflects strategic pricing and product mix, partially offset by channel mix."
- FY26 10-K p. 38 (new, EMEA): "Gross margin contraction of 140 basis points primarily due to lower ASP, reflecting higher discounts, and unfavorable changes in standard foreign currency exchange rates."
- FY26 10-K p. 39 (new, Greater China): "Gross margin contraction of 30 basis points primarily due to unfavorable changes in standard foreign currency exchange rates."
- FY26 10-K p. 40 (new, APLA): "Gross margin contraction of 200 basis points primarily due to unfavorable changes in standard foreign currency exchange rates."
- Q1 FY25 10-Q p. 22: "Higher NIKE Brand ASP (increasing gross margin approximately 40 basis points), primarily due to benefits from strategic pricing actions from the prior year, partially offset by changes in channel mix."
- Q2 FY25 10-Q p. 26: "Lower NIKE Brand ASP (decreasing gross margin approximately 330 basis points), primarily due to higher discounts, product mix and changes in channel mix, partially offset by benefits from strategic pricing actions".
- Q3 FY25 10-Q p. 28 (new): "Lower NIKE Brand ASP (decreasing gross margin approximately 150 basis points), primarily due to higher discounts and changes in channel mix;" (quarter).
- Q3 FY25 10-Q p. 29: "Lower NIKE Brand ASP (decreasing gross margin approximately 140 basis points), primarily due to higher discounts and changes in channel mix, partially offset by benefits from strategic pricing" (nine months).
- Q1 FY26 10-Q p. 19: "due to higher discounts with our wholesale partners, higher discounts in our NIKE Brand factory stores, an increase in product costs including new tariffs and changes in channel mix".
- Q3 FY26 10-Q p. 30: "Higher NIKE Brand ASP (increasing gross margin approximately 80 basis points), primarily due to strategic pricing and product mix".

**Nike releases (prepared remarks; "not an official transcript")**
- Q4 FY23 PDF p. 15 (new): "We also expect continued structural gains from our focus on price value, including low single- digit price increases in FY24".
- Q3 FY24 PDF p. 15 (new): "Our outlook is now partially offset by higher markdowns, reduced benefits from channel mix".
- Q1 FY25 PDF p. 4: "requiring higher levels of promotional activity in Q1 to drive conversion".
- Q1 FY25 PDF p. 10 (page added): "higher promotions, channel mix headwinds, and supply chain deleverage more than offsetting lower product costs and decreasing benefit from strategic pricing actions".
- Q3 FY25 PDF pp. 9, 10, 11, 15: as in revision 2 (30 promotional days to zero; "higher markdowns on Nike Direct, higher wholesale discounts"; "several percentage point improvement in demand at full price"; "shifting closeout liquidation to our Nike Factory stores"; "increasing markdowns to drive velocity").
- Q4 FY25 PDF p. 9: "due to higher wholesale discounts, higher discounts in our Nike factory stores, supply chain cost deleverage and channel mix headwinds".
- Q4 FY25 PDF p. 13 (new): "we have implemented a surgical price increase in the United States, with phased implementation beginning in Fall 25".
- Q4 FY25 PDF p. 14 (new): "Nike will continue liquidating excess inventory through our value stores and select value partners".
- Q1 FY26 PDF p. 10: "reducing the number of days of sitewide promotion by more than fifty"; also (new) "Closeout mix is approaching normalized levels" (North America).
- Q2 FY26 PDF p. 8 (new): "This represents a gross headwind of approximately 320 basis points to gross margin in Fiscal 26. And while we have begun to take actions to reduce this to a net impact of approximately 120 basis points".
- Q3 FY26 PDF p. 11 (EMEA): "more aggressive with promotions on Nike Digital at end of season".
- Q4 FY26 PDF p. 9 (new): "Gross margin was 42.9%, up 20 basis points versus the prior year, including a 210 basis point benefit related to recovery of IEEPA tariffs."

**Secondary (context only):** Complex (Victor Deng, February 2, 2024), citing Vertical Knowledge data via Reuters. It covers wholesale partners, not Nike.com. Not used as evidence. **Snippet only:** the StyleSage 2018 figure. Not used.

## 4. Method notes

- **Direction of bias.**
  - All-in-Direct overstates Direct markdown, because Nike names wholesale discounts and returns in every FY2025 to Q1 FY2026 period.
  - Rows 13 (returns cleared through factory stores) and 11 (closeouts transferred at off-price) both push the true value toward the upper rows.
  - The pricing cap bounds the upper rows from above.
  - Most likely FY2025 range (opinion): 3.4% to 9.8%.
- **Joint versus separate conversion.** The gross-margin formula is nonlinear, so the offset must be converted together with the ASP line. Converting separately understated FY25 at +100 bps by 0.3 pt and Q2 FY25 by 0.4 pt.
- **What the bound measures.** The bound measures the realized Direct-to-transfer-price ratio. That is the quantity note 09's break-even uses, so intra-Direct mix (row 8) does not need to be separated for the break-even verdict.

## 5. What remains unresolved and the data that would resolve it

1. **Direct share of FY2025 discount dollars (row 2, the 7.8% question).** Settled by a channel split of the ASP line, or a restored internal-sales or NIKE Direct gross-margin disclosure. The "comparable U.S. GAAP metric" Nike promised in the FY24 10-K (p. 32) appears to be the combined "NIKE Brand ASP" bridge line, which does not split channels or separate discounts from mix.
2. **Q2 FY2025 pricing benefit (row 1c).** A quarterly split of the Q2 FY25 -330 bps line into discounts, mix, pricing and product mix.
3. **Closeout transfer pricing and closeout share (row 11).** Nike's transfer-pricing policy for closeouts, plus factory versus in-line revenue.
4. **EMEA gross profit (row 6).** It would firm up the FY2026 regional bound, which currently uses the company margin as a proxy.
5. **Absolute markdown depth versus MSRP (row 9).** It needs a Nike.com price-tracking panel. None was found in an openable source.

## Revision log

**Revision 3 (October 13, 2026)**
- **Fixed failed arithmetic check.** The pricing offset is now converted to dollars jointly with the ASP line (A4). Corrected figures:
  - FY25 at +100 bps: 9.8% (was 9.5%).
  - Q2 FY25 at +100 bps: 14.8% (was 14.4%).
  - Q2 FY25 at +150 bps: 16.6% (new).
  - FY24 to FY26 cumulative maxima: re-derived in Table F.
  - The claim "no scenario reaches 15%" was removed: it only held because the offset was capped by assumption.
- **Offset no longer assumed; bounded with data.** Added Table E2 with Nike's own pricing statements:
  - FY24 increases "low single-digit".
  - FY24 quarterly full-price ASP lines and the implied Q4 FY24 -27 bps.
  - Q2 FY25 "decreasing benefit" and product mix as a headwind.
  - No pricing named in the Q3 FY25 ASP line or in the Q4 FY25 drivers.
  - The FY26 tariff mitigation of about 200 bps.
  - Added break-even offsets for every period (Tables D and E) and price-increase caps.
- **Verdict changes.**
  - Row 1 is split into 1 (FY25 full year: ruled out, now conditional on Nike's pricing statements rather than an assumed cap), 1b (cumulative: unlikely, not excluded) and 1c (quarters: Q2 FY25 unresolved).
  - Row 2 now states the exact Direct share of discounts needed (62% to 100%).
  - Row 3 is restated as "by construction on the transfer-price basis", and the transfer-price caveat is added.
  - Row 6 is strengthened with FY26 segment statements.
  - Row 8 is reclassified as irrelevant to the break-even verdict.
- **New alternatives tested:**
  - 11: transfer-price confound (Table G, algebra for the level effect).
  - 12: obsolescence reserves (ruled out as hidden revenue loss; sensitivity reported).
  - 13: returns cleared through factory stores (inside the all-in-Direct bound).
  - 14: unit-cost assumption A1 (replaced; Direct logistics cost estimated from the FY26 warehousing line).
  - 15: FY26 bridge rounding (tested at -40 bps).
- **Table B relabelled.** Only FY2024 is a like-for-like calibration; FY22 and FY23 are nine months versus a full year.
- **Removed the "FY24 vs FY19 to FY21 average" framing** from the bottom line as a test of the range. The range is incremental to FY24 by definition.
- **New downloads** in `scratchpad/rh/dl/rev3/`: Q3 FY22, Q1 FY23, Q2 FY23 and Q3 FY23 10-Qs. The Q2 FY25 release PDF was not available (404). The FY21 to FY24 10-Ks were re-paged from `dl/gc/nike/` into `md/rev3/`.
- Revision 2 text is preserved at `scratchpad/rh/markdown_depth.rev2.bak.md`.
