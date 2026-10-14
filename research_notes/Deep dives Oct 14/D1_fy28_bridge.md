# D1: FY28 revenue and EPS gap vs consensus (labelled-arithmetic bridge)

Prepared 2026-10-14. Price $35.35 (Oct 12 close). Replication script: `research_notes/Deep dives Oct 14/D1_fy28_bridge.py` (run `python3 -I D1_fy28_bridge.py`; every table below is its output). This is a bridge, not a full model.

Tags: OPENED = read in the filing or page itself today (Nike filings pulled from the investors.nike.com mirror, not www.sec.gov). SNIPPET = search summary only. REPO = earlier repo note or `data/nike_filing_facts.csv`, not re-opened. DERIVED = my arithmetic. ASSUMPTION = judgment, with the anchor named. Downloads (untrusted data) sit in the session scratchpad `d1/dl/`: Q1 FY27 10-Q (`0000320187-26-000193/nke-20260831.htm`), FY26 10-K (`0000320187-26-000088/nke-20260531.htm`), Oct 1 8-K Ex. 99.1 (`0000320187-26-000184/q1fy27exhibit991er.htm`), Q1 FY27 call transcript PDF (Nike IR).

## 1. Answer first

1. **The part of the FY28 gap that rests on filings is small. The part that is large rests on one judgment.** Consensus FY28 EPS $1.646 needs revenue of $43,645M (+1.1%) and EBIT of $3,179M (7.28% margin, +154 bps). Of the +$700M EBIT step, only about $203M is volume. The other **$497M (114 bps of FY28 revenue) must come from gross margin rate plus operating expense** (DERIVED, section 5).
2. **Base case FY28 adjusted EPS: $1.17** (revenue $42,158M, -1.2% vs the FY27 guide midpoint; EBIT $2,268M, 5.38%). **Low $0.54, High $2.03.** The range is wide because operating leverage is high (every 100 bps of gross margin is $0.21 of EPS; every 1 point of revenue is $0.07 to $0.09). The High case is above consensus; the range brackets it.
3. **How much of the gap survives (base EPS vs $1.646):**

| Case | FY28 EPS | Gap to $1.646 | Gap after netting the full tariff offset (+$0.08 / +$0.12) |
|---|---|---|---|
| A. Revenue only: my base revenue ($42,158M) but consensus's full margin step granted | $1.56 | -$0.09 (-5.3%) | -$0.01 / +$0.03, so about **zero survives** |
| B. Revenue flat on guide midpoint ($42,686M), consensus margin step kept, 35% decremental on the revenue shortfall | $1.46 | -$0.19 (-11.2%) | -$0.11 / -$0.07 (-6.4% / -3.9%) |
| **C. Base: margin step not granted (gross margin flat, Pace partly reinvested)** | **$1.17** | **-$0.48 (-28.9%)** | **-$0.40 / -$0.36 (-24.0% / -21.6%)** |

   So: **$0.00 to $0.11 of the gap survives on revenue evidence alone; $0.36 to $0.40 (22% to 24%) survives only if you also accept that the +114 bps gross margin plus opex step does not happen.** Section 6 shows what has to be true for it to happen.
4. **The tariff offset is not additive to every case.** It erases the gap in case A only if consensus was built on Nike's June 15% plan rate. If consensus was built on the rates actually in force (about 11.4%), the offset is zero and the pre-offset gaps stand. Nike never states the rate inside the Oct 1 guide (the word "tariff" appears zero times on the call; REPO `risk_tariffs.md`, call transcript OPENED).
5. **Verdict on the pitch:** "FY28 consensus is too high" is supported on revenue only weakly (-$0.09 to -$0.19 before the tariff offset). It is supported strongly only through a margin argument that Investor Day (Nov 16 to 17) will confirm or kill. Do not present the $0.48 as a filing-derived fact.

## 2. Starting point: FY27 guide midpoint (what Nike said, and what I derived)

Nike guide, Oct 1 2026 (Q1 FY27 8-K Ex. 99.1 p. 1 of exhibit, OPENED): revenue "decline high-single digits"; effective tax rate "mid-20 percent range"; adjusted diluted EPS "$1.15 to $1.35", which "excludes approximately $0.15 of restructuring expenses related to Pace". Call (OPENED): EBIT "to decline by a greater percentage than revenue"; "SG&A to remain down year-over-year"; no gross margin guide ("we're probably not going to provide guidance specifically for gross margin"); pressure on reported revenue "for the remainder of fiscal '27 and into '28"; Pace "majority of the program savings to be realized in fiscal years '29 and '30".

| Item | Value | Basis |
|---|---|---|
| FY26 revenue | $46,398M | FY26 10-K p. 32 (OPENED) |
| FY27 revenue at midpoint (-8%) | $42,686M | ASSUMPTION: "high-single digit" read as -7% to -9% (Nike does not define it). Consensus $43,152M is -7.0% |
| Q1 FY27 actual | $11,213M, -4.3% | Q1 FY27 10-Q p. 22 (OPENED). Q2 to Q4 must fall 9.2% at the midpoint |
| Adjusted EPS | $1.25 | guide midpoint |
| Shares | 1,485M | Q1 FY27 diluted 1,484.2M (REPO facts). No buyback: Q1 cash return was dividends only, about $610M (8-K p. 1); FY26 repurchased 1.8M shares (REPO facts, FY26 10-K p. 45) |
| Tax | 25% | midpoint of "mid-20s". Q1 FY27 actual 22.7% (10-Q p. 24), FY26 20.3% (10-K p. 35) |
| Pretax / EBIT | $2,475M / $2,420M (5.67%) | DERIVED: 1.25 x 1,485 / 0.75, less net interest income about $55M (FY26 $50M; Q1 $14M). Consensus FY27 EBIT $2,479M (5.74%, REPO) |
| Pace charge excluded | about $297M pretax | DERIVED: $0.15 x 1,485 / 0.75. Matches Nike's "approximately $0.3 billion" in FY27 (10-Q p. 18, OPENED) |
| SG&A (ex-Pace) | $15,334M | ASSUMPTION: FY26 $16,114M less 3% (Q1 FY27 run rate, -3%), less the Pace charge |
| Implied gross margin | **41.5%** | DERIVED: (2,420 + 15,334 - 50 other income) / 42,686. Not guided. Cross-check: FY26 ex-IEEPA-recovery gross margin was (19,911 - 986) / 46,398 = 40.8% (FY26 10-K p. 30 and 32); FY27 at 41.5% needs Q2 to Q4 about 41.2%, consistent with Q1 at 42.8% and with Q2 to Q4 FY26 at about 40.2% to 40.6% |

Sensitivity: if SG&A is $100M lower than assumed, implied FY27 gross margin is 23 bps lower. EBIT is pinned by the EPS guide, so the FY28 EPS bridge does not depend on this split except through the volume line (revenue change x gross margin).

Not used: FY26 reported EPS $2.10 includes a $0.52 benefit from the expected IEEPA tariff recovery (Q4 FY26 release p. 1; FY26 10-K p. 30: $986M, which "largely offset" the IEEPA tariffs expensed in FY26) and $385M of severance (10-K p. 30). FY26 is not a clean base, so the bridge starts at the FY27 guide.

## 3. Revenue by segment

### 3.1 FY27 guide-implied path (ASSUMPTION for Q2 to Q4, solved to hit the midpoint)

Q1 FY27 actuals (10-Q p. 25, OPENED): NA $5,127M (+2% c-n), EMEA $3,176M (-5%), Greater China $1,180M (-26% c-n, -22% reported), APLA $1,463M (0% c-n), Converse $263M (-28%). Assumed Q2 to Q4 y/y: Greater China -30% (Denton: guide "assumes that China actually gets worse ... for the balance of this year", REPO `china_floor.md`, OPENED transcript), Converse -30%, APLA -3%, NA -5.5%; EMEA solves to -7.1%. The Q2 headwind of about 400 bps (EMEA Cyber Week lap, NA sell-in lap) is inside these.

| Segment | FY26 | FY27 path | y/y | FY28 Low | FY28 Base | FY28 High |
|---|---|---|---|---|---|---|
| North America | 20,511 | 19,766 | -3.6% | -2% | 0% | +3% |
| EMEA | 12,572 | 11,760 | -6.5% | -3% | 0% | +3% |
| Greater China | 5,847 | 4,214 | -27.9% | -20% | -12% | -4% |
| APLA | 6,243 | 6,073 | -2.7% | -1% | +1% | +4% |
| Converse | 1,174 | 829 | -29.4% | -20% | -10% | 0% |
| Global Brand Div. + Corporate | 51 | 44 | | flat | flat | flat |
| **Total** | **46,398** | **42,686** | **-8.0%** | **40,869 (-4.3%)** | **42,158 (-1.2%)** | **43,706 (+2.4%)** |

FY26 segment figures: FY26 10-K p. 36 (OPENED). Consensus FY28 revenue $43,645M (+1.1% on $43,152M).

### 3.2 Why each FY28 base assumption (evidence, and what ruled out the alternatives)

- **Greater China -12% (Low -20%, High -4%).** The partner-online exit on Jan 1 2027 (Topsports, Pou Sheng) is only five months in FY27. The repo estimate is $743M a year at wholesale value (REPO, Thesis ruling; a team estimate, not a Nike figure), of which $310M falls in FY27, leaving **$433M (10.3% of the FY27 China base) as pure carryover in Jun to Dec 2027** (DERIVED: 743 x 5/12 = 310; 743 x 7/12 = 433). JPMorgan's Boss estimates a "$1 billion revenue headwind in China for fiscal 2028" from the same exit (SNIPPET, Stocktwits article opened; I could not open the JPMorgan note). Nike says Greater China actions "extend beyond fiscal 2027" (10-Q p. 20, OPENED). Base -12% = -10 carryover and -2 underlying. Alternative "China stabilizes in FY28": ruled out as a base because the exit is a dated, announced event and Q1 FY27 units fell 26% (footwear) with ASP flat, i.e. a volume loss, not a price one (10-Q p. 28). It stays in the High case (-4%). Pou Sheng's September revenue of -2.5% is a single month and covers many brands (REPO `china_floor.md`).
- **North America 0% (Low -2%, High +3%).** Q1 FY27 NA +2% was wholesale +9% against Direct -6% (10-Q p. 26). Repo estimate of NA consumer sell-through is about -1% (REPO `na_sell_through.md`, strength strong but no Nike-specific POS data). Alternatives: (a) NA sell-in growth is real demand: ruled out by that note's retailer inventory and markdown tests; (b) the unwind is fully in FY27 guide: partly, Q2 to Q4 at -5.5% already assumes it. Flat in FY28 means shipments converge to a sell-through of about -1% to 0% with Direct stabilizing.
- **EMEA 0% (Low -3%, High +3%).** Q1: footwear units -5%, footwear ASP -6 points (higher discounts and channel mix); Direct -12% with digital -26% (10-Q p. 27). FY28 Q2 laps the Cyber Week promotion, which helps compares. Flat is an easy-compare offset to continued discounting.
- **APLA +1%, Converse -10%.** APLA was 0% c-n in Q1 with footwear units flat (10-Q p. 29). Converse fell 31% c-n in FY26 and 28% in Q1 with units -34% (10-K p. 41; 10-Q p. 31); Nike says the Converse reset continues "throughout fiscal 2027" (10-Q p. 20), so FY28 is the first year of a smaller decline.
- **Reporting change.** Nike will move to three geographies in FY28 (Americas, APGC, EMEA; 10-Q p. 20, OPENED). FY28 segment data will not match NA, Greater China and APLA, so segment comparisons to consensus after Investor Day will need a recast.

### 3.3 Segment consensus: not available free (routes tried)

| # | Route | Result |
|---|---|---|
| 1 | Yahoo earningsTrend (REPO, `expectations_gap.md`) | partial: total revenue, EPS only |
| 2 | Nasdaq/Zacks estimates API (REPO) | partial: total EPS, FY28 $1.78 incl. a stale $3.22 high |
| 3 | MarketScreener finances page (OPENED today) | partial: totals only. FY28 sales 43,570, EBIT 3,155, net income 2,398, EPS 1.634, shares 1,485,309k. No segments, no gross margin, no SG&A. Note the page now differs slightly from the saved 43,645 / 3,179 / 1.646 |
| 4 | WebSearch for FY28 segment consensus | partial: only a stale Investing.com figure ($47.09B, Sep 23, before the guide, SNIPPET) |
| 5 | Stocktwits on JPMorgan (OPENED) | worked: a China-only analyst estimate ($1B FY28 headwind) |
| 6 | tickflow.io forecast page | blocked (HTTP 429) |
| 7 | Nike IR | Nike publishes no consensus |

Seeking Alpha, Visible Alpha and FactSet carry segment consensus but are paywalled and I did not access them; the repo's `Refinitiv pull list.md` is the existing plan. **What would settle it:** a Visible Alpha, FactSet or Refinitiv segment consensus pull. **Substitute used:** the growth each segment would need to reach the consensus total (DERIVED):

| Assumption for China and Converse | NA + EMEA + APLA must grow in FY28 to reach $43,645M |
|---|---|
| China -12%, Converse -10% (my base) | +4.1% (vs my base +0.1%) |
| China -22%, Converse -20% | +5.5% |
| China -4%, Converse 0% | +3.0% |
| China -12%, Converse -10%, FY27 starting at consensus $43,152M | +3.0% |

Read: even with a generous start and a benign China, consensus needs the three healthy regions to grow about 3% to 4% after a guided -3.6% / -6.5% / -2.7% FY27.

## 4. Units versus price, channel, currency (filing evidence)

### 4.1 Units versus ASP, Q1 FY27 (all currency-neutral; 10-Q pp. 23 to 31, OPENED)

| Segment | Revenue c-n | Footwear units / ASP | Apparel units / ASP | Wholesale / Direct |
|---|---|---|---|---|
| North America | +2% | +2% / -1 pt | 0% / +6 pts | +9% / -6% |
| EMEA | -5% | -5% / -6 pts | +2% / +3 pts | -1% / -12% |
| Greater China | -26% | -26% / 0 | -25% / -2 pts | -31% / -18% |
| APLA | 0% | 0% / -1 pt | +3% / +1 pt | +2% / -3% |
| Converse | -28% | units -34% / ASP +6 pts (all products) | | -25% / DTC -34% |
| NIKE Brand | -4% | -5% / -1 pt | -2% / +4 pts | -1% / -9% (Direct, NIKE Inc basis) |

FY26 for comparison (10-K pp. 33, 37 to 41, OPENED): footwear units -1%, ASP -1 pt; apparel units +1%, ASP +1 pt; NA wholesale +14% and Direct -6%; Greater China footwear units -14%.

Implied FY28 base by driver (DERIVED, holding Q1 FY27 ASP contributions): Greater China -12% revenue means footwear and apparel units of about -11% to -12% (ASP is flat to -2 pts). NA flat revenue with Q1's blended ASP contribution of about +1.2 pts (footwear 63.6% of NA x -1, apparel 30.5% x +6) means units of about -1%. EMEA flat revenue with Q1's blended ASP of about -2.3 pts means units must rise about 2%, which is the hardest of the three given Q1 units of -5% in footwear. So **the FY28 base is a volume story in China and a price/discount story in EMEA, and consensus needs both volume recovery and a stop to discounting.**

### 4.2 Channel

Direct was 39.2% of NIKE Brand revenue in FY26 ($17,720M of $45,222M, 10-K p. 32) and 37.8% in Q1 FY27 ($4,142M of $10,952M, 10-Q p. 22); wholesale moved the other way. Nike does not disclose gross margin by channel, so the channel effect on margin **cannot be separated** from the "ASP" bridge line (which Nike words as "higher discounts and channel mix", Q1 10-Q p. 23). What the data does show: to reach consensus revenue (+2.2% from the guide midpoint, ignoring Converse and brand divisions) with Direct at 37.8% of mix, wholesale must grow +3.5% if Direct is flat, or +5.4% if Direct falls 3% (DERIVED). In Q1 wholesale was -1% with NA +9% and China -31%.

### 4.3 Currency

Translation added $1,023M to FY26 revenue (about 2.2 points; reported 0% vs c-n -2%, FY26 10-K p. 32, REPO facts) and only about $26M in Q1 FY27 (REPO facts), so FX is no longer a revenue tailwind. Base FY28: 0. Sensitivities (DERIVED): 1% move in non-US currencies (56% of revenue, FY26 10-K) is about $236M of revenue and under $0.01 of EPS by translation alone; the larger channel is the gross margin hedge line (FY24 -40 bps, FY25 -10, FY26 +20, Q1 FY27 +40; facts CSV). Low/Base/High use -20 / 0 / +30 bps ($0.04 / 0 / $0.07).

## 5. Dollar EPS bridge, FY27 guide midpoint to FY28

Method (DERIVED): volume = change in revenue x FY27 gross margin (41.47%); gross margin rate = bps x FY28 revenue; opex = change in SG&A dollars; all taxed at 25% and divided by 1,485M shares; then the tax-rate and share-count effects. Opex "deleverage" is the change in SG&A as a share of revenue.

| $ per share | Low | **Base** | High |
|---|---|---|---|
| FY27 adjusted EPS at guide midpoint | 1.250 | **1.250** | 1.250 |
| Volume (revenue change at FY27 gross margin) | -0.381 | **-0.111** | +0.214 |
| Gross margin rate (sum of lines below) | -0.222 | **0.000** | +0.369 |
| Opex (SG&A dollars) | -0.094 | **+0.034** | +0.161 |
| Tax rate (26% / 25% / 24%) | -0.007 | **0.000** | +0.027 |
| Share count (1,490 / 1,488 / 1,480M) | -0.002 | **-0.002** | +0.007 |
| **FY28 adjusted EPS** | **0.544** | **1.171** | **2.027** |
| Revenue / EBIT margin | 40,869 / 2.54% | 42,158 / 5.38% | 43,706 / 8.91% |
| vs consensus $1.646 | -$1.10 (-67%) | **-$0.48 (-29%)** | +$0.38 (+23%) |

### 5.1 Gross margin rate lines (bps, Nike's own bridge categories; $/share in brackets for Base)

| Line | Low | Base | High | Evidence anchor (Nike bridge, facts CSV unless noted) |
|---|---|---|---|---|
| Tariff (annualization) | -10 | -10 [-0.021] | -10 | FY27 COGS carries about 5.5 months of Section 122 entries at 10% and 6.5 months at about 11.4%; FY28 is all 11.4%. 0.6 pt x $6.5B = about $39M = 9 bps. Rates: REPO `risk_tariffs.md` (USTR notice OPENED there) |
| Warehousing and logistics | 0 | +20 [+0.043] | +50 | FY25 +20, FY26 +20, Q1 FY27 +90 (10-Q p. 23, OPENED). Base follows the annual history, not the Q1 spike |
| NIKE Brand product costs (sourcing, Pace supply chain) | +10 | +40 [+0.085] | +80 | FY24 +10, FY25 +80, FY26 -20, Q1 FY27 +10. Denton: supply-chain moves "bolstering gross margin" (call, OPENED) |
| NIKE Brand ASP (discounts, channel) | -40 | -20 [-0.043] | +20 | FY25 -180, 9M FY26 -80, Q1 FY27 -30. Nike links further Sportswear and Jordan actions beyond FY27 to "higher levels of discounting" (10-Q p. 20) |
| FX incl. hedges | -20 | 0 | +30 | FY24 -40, FY25 -10, FY26 +20, Q1 FY27 +40 |
| Other costs (third-party royalties) | -30 | -20 [-0.043] | 0 | Q1 FY27 -40 (royalties); FY26 +20; FY25 -90 |
| Converse gross margin | -10 | -5 [-0.011] | 0 | FY25 -20, FY26 -20, Q1 FY27 -10; Converse shrinks to under 2% of revenue |
| Greater China mix | -8 | -5 [-0.011] | -3 | DERIVED: China share of revenue falls 9.9% to 8.8%; China gross margin 47.5% vs company 42.8% (10-Q pp. 22, 28) |
| **Total** | **-108** | **0** | **+167** | |

All bps values are ASSUMPTION within the historical ranges shown; Nike gave no FY28 gross margin guide.

### 5.2 Opex detail

| | Low | Base | High |
|---|---|---|---|
| Demand creation (FY27 $4,800M, ASSUMPTION; FY26 $4,754M; no World Cup in FY28 base) | +1% | 0% | +1% |
| Overhead inflation on FY27 $10,534M | +2.5% | +1.5% | +0.5% |
| Pace gross savings in FY28 | $250M | $375M | $600M |
| Share of savings reinvested | 50% | 40% | 30% |
| Net Pace savings | $125M | $225M | $420M |
| SG&A FY28 | $15,520M | $15,267M | $15,014M |
| SG&A as % of revenue vs FY27 35.92% | +205 bps | **+29 bps** | -157 bps |

Pace anchor: $2.5B "cumulative savings through fiscal 2031", "majority ... in fiscal years '29 and '30", intent to "reinvest a portion" (10-Q p. 20; call). If cumulative means the sum of annual savings and the ramp is 5/15/30/30/20%, FY28 is $375M (my base). If it means a run-rate reached by FY31, FY28 could be higher; that ambiguity is why High uses $600M. Filings do not settle it; Investor Day should.

### 5.3 Tariff offset (the $0.08 to $0.12)

REPO sizing (`data/hunt/risk_tariffs/tariff_gap_sizing.csv`, mid base $6.5B of US-bound imports, rate gap 3.56 points between the 15% plan and about 11.44% in force, 70% to 100% pass-through): FY28 EPS $0.086 to $0.122 (full range $0.079 to $0.141). I re-derived the arithmetic: $0.10 = $212M pretax = 50 bps of base FY28 revenue; $0.08 = 38 bps, $0.12 = 56 bps. The $6.0B to $7.5B import base is derived from Nike's own $1.5B annualized IEEPA cost and an FY26 "650 bps" statement, not from Census data (not retrievable), so it carries about +/- 15%.

**Why the offset is conditional (alternatives tested):**
- Consensus and the guide embed the 15% plan: possible (the 15% was stated Jun 30 for Q1). Counter: the Oct 1 guide was built ten weeks after the lower rates started and Nike calls it its "best assessment of where this business stands today". Not ruled out. If true, offset applies in full.
- They embed the actual 11.4%: more likely, and then the offset is zero. This is the case where my -10 bps tariff line (a slight annualization headwind) is the right tariff figure.
- Neither knowable from filings. **What would decide it:** Nike stating the tariff rate in its FY27 guide at Investor Day, or a sell-side model disclosure (Boss, Hutchinson).
- Tails not in any number above: Section 122 refund (about $0.14 one-time), forced-labor 301 vacated (up to +$0.39 a year), excess-capacity 301 +7.5 points (about -$0.26 a year) (REPO).

## 6. What would have to be true for consensus (the margin ledger)

Consensus FY27 to FY28 EBIT bridge (DERIVED from MarketScreener/Yahoo means): EBIT +$700M = volume $203M (revenue +$493M x 41.2% implied gross margin) + **$497M** from gross margin rate and opex.

| Source of the $497M | My base | Needed for consensus |
|---|---|---|
| Net Pace savings after wage inflation (base: $225M less $158M overhead inflation) | +$67M net SG&A reduction | up to $375M if Pace is fully retained and wage inflation is zero |
| Gross margin rate (net of tariff, logistics, product, ASP, FX, royalties, Converse, mix) | 0 bps | at least +29 bps ($122M) even in that best case on opex |
| Total | $67M | $497M |

So consensus needs Pace savings to drop through in full **and** at least 29 bps of net gross margin gain, with no wage inflation, no reinvestment and no further discounting drag. The evidence against full drop-through: Denton intends to "reinvest a portion", the majority of savings land in FY29 and FY30, and Nike lists Pace charges of about $1.0B to get there. The evidence for: Q1 FY27 overhead already fell 6% (10-Q p. 24) and gross margin rose 60 bps. Neither is decisive; **the margin step is the real disagreement**, not revenue.

Gap decomposition, Base vs consensus (DERIVED, per share): revenue shortfall at consensus margin -$0.055 (of which the FY27 starting level is -$0.017, FY28 growth part -$0.037; consensus FY27 revenue sits at the shallow end of the guide); margin step -$0.405; consensus's own EPS-to-EBIT inconsistency -$0.016 (consensus EBIT $3,179M at 25% tax and 1,488M shares gives $1.630, but the published EPS $1.646 implies 1,469M shares, i.e. fewer than the 1,484M to 1,485M actually outstanding: DERIVED); total -$0.475.

By segment (volume line only, FY28 vs FY27, $/share at each segment's Q1 FY27 gross margin; segment EBIT-margin version in brackets): Base: Greater China -$0.121 [-0.054], Converse -$0.019 [-0.004], APLA +$0.013 [+0.007], NA and EMEA 0; sum -$0.127 [-0.051]. Low: Greater China -$0.202, NA -$0.087, EMEA -$0.079, Converse -$0.038, APLA -$0.013. High: NA +$0.130, EMEA +$0.079, APLA +$0.052, Greater China -$0.040. **Greater China is the entire base-case revenue drag**; it is a known, dated event (Jan 1 2027).

## 7. What EPS would be at several revenue and margin points

Grid A: EPS by FY28 revenue and EBIT margin (25% tax, 1,488M shares, net interest +$55M). Bold = at or above $1.646.

| Revenue \ EBIT margin | 5.5% | 6.0% | 6.5% | 7.0% | 7.28% (cons.) | 7.5% | 8.0% | 9.0% |
|---|---|---|---|---|---|---|---|---|
| $41.0B | 1.16 | 1.27 | 1.37 | 1.47 | 1.53 | 1.58 | **1.68** | **1.89** |
| $42.0B | 1.19 | 1.30 | 1.40 | 1.51 | 1.57 | 1.62 | **1.72** | **1.93** |
| $42.7B (guide mid, flat) | 1.21 | 1.32 | 1.43 | 1.53 | 1.59 | 1.64 | **1.75** | **1.96** |
| $43.6B (consensus) | 1.24 | 1.35 | 1.46 | 1.57 | 1.63 | **1.68** | **1.79** | **2.01** |
| $44.5B | 1.26 | 1.37 | 1.49 | 1.60 | **1.66** | **1.71** | **1.82** | **2.05** |

EBIT margin needed for $1.646: 7.83% at $41.0B, 7.64% at $42.0B, 7.52% at $42.7B, 7.36% at $43.6B, 7.21% at $44.5B. For reference: FY26 8.3%, FY27 guide midpoint 5.7%, FY24 12.7% (FY26 10-K p. 31).

Grid B: EPS by revenue and gross margin (SG&A held at base FY28 $15,267M, other income $50M).

| Revenue \ Gross margin | 41.0% | 41.5% | 42.0% | 42.5% | 43.0% | 43.5% |
|---|---|---|---|---|---|---|
| $41.0B | 0.83 | 0.93 | 1.04 | 1.14 | 1.24 | 1.35 |
| $42.0B | 1.04 | 1.14 | 1.25 | 1.36 | 1.46 | 1.57 |
| $42.7B | 1.18 | 1.29 | 1.39 | 1.50 | 1.61 | 1.72 |
| $43.6B | 1.38 | 1.49 | 1.60 | 1.71 | 1.82 | 1.93 |
| $44.5B | 1.55 | 1.67 | 1.78 | 1.89 | 2.00 | 2.12 |

Gross margin needed for $1.646 at base SG&A: 44.9% at $41.0B, 43.9% at $42.0B, 43.2% at $42.7B, 42.2% at $43.6B, 41.4% at $44.5B (FY27 implied 41.5%, FY24 actual 44.6%).

Unit sensitivities (Base): 100 bps gross margin = $422M = $0.212; $100M SG&A = $0.050; 1 point of revenue = $422M = $0.088 at FY27 gross margin ($0.074 at 35% decremental); 1 point of tax = $0.016; 10M shares = $0.008. The guide range itself ($1.15 to $1.35) shifts every end point by -$0.10 / +$0.10; moving the start to consensus FY27 ($1.288) adds $0.04.

## 8. Alternative explanations for "consensus FY28 EPS is higher than my base", and what ruled each out

| Alternative | Test | Result |
|---|---|---|
| Consensus is stale (old highs) | Zacks FY28 $1.78 includes a $3.22 outlier worth about $0.12; Yahoo $1.646 after 24 down revisions; Zacks ex-outlier about $1.66 (REPO `expectations_gap.md` skeptic section) | Ruled out as the explanation of the level; stale highs only push the mean lower still |
| Revenue growth is higher than I assume | Section 3.3: needs NA+EMEA+APLA +3.0% to +4.1% | Not ruled out; needs Q2 FY28 turn (consensus quarterly path -2.0% / +0.5% / +1.5% / +2.2%, MarketScreener, REPO). Contradicted by Denton: pressure "bleed in a little bit into fiscal '28" (OPENED), but that wording is softer than "into fiscal 28" (skeptic note) |
| Tariff relief | Section 5.3 | Quantified at $0.08 to $0.12; applies only if consensus uses 15% |
| Pace savings faster than assumed | Section 6 | Not ruled out; needs full drop-through. Filing language says majority in FY29 and FY30 |
| Gross margin recovers (logistics, sourcing) | Section 5.1 | Needs about +29 bps even with full Pace drop-through; history shows +20 to +90 bps from logistics and 0 to +80 from product cost in individual years |
| Share count / buyback | Consensus implies 1,469M shares vs 1,485M outstanding; no buyback in Q1; FY26 operating cash flow $2,868M and capex $684M against about $2.4B of dividends (REPO facts) leave no room | Ruled out as a real driver; worth $0.016 of consensus EPS that is arithmetic inconsistency |
| Tax rate lower | Guide "mid-20s"; consensus implied 25.2% | Ruled out (no gap) |
| Currency | Q1 translation +$26M only | Ruled out as a revenue driver; hedge line is in the gross margin ledger |

**Still unresolved and what decides it:** (1) the tariff rate inside the guide and consensus (Investor Day or a model disclosure); (2) the Pace savings phasing and reinvestment (Investor Day "five-year algorithm"); (3) segment consensus (paid pull); (4) whether the Q2 FY27 print (about Dec 17) shows gross margin at 42.1% to 42.6% as the tariff lap implies (REPO skeptic estimate). All but (4) land before the Nov 19 finals.

## 9. What I could not verify

- Segment-level and gross-margin consensus (no free source after seven routes; section 3.3).
- FY27 gross margin, SG&A split, Pace phasing and the tariff rate in the guide: none disclosed; the first three are derived or assumed above.
- The $743M partner-online figure is a team estimate; I did not re-derive it from HKEX filings today, and I could not open JPMorgan's note.
- US-bound import value ($6.0B to $7.5B) for the tariff sizing is derived from Nike's own statements, not Census data.
- Q1 FY27 FX translation benefit ($26M) and several history values are from `data/nike_filing_facts.csv` and were not re-opened in the filing.
- Share count 1,485M and 25% tax are inputs, not Nike statements beyond "mid-20s".
- Probability weights on Low, Base and High are not assigned.

## Sources

- Nike Q1 FY27 10-Q (investors.nike.com/sec-filings/all-sec-filings/content/0000320187-26-000193/nke-20260831.htm), printed pp. 18 to 31 (OPENED).
- Nike FY26 10-K (.../0000320187-26-000088/nke-20260531.htm), printed pp. 30 to 41 (OPENED).
- Nike 8-K Ex. 99.1, Oct 1 2026 (.../0000320187-26-000184/q1fy27exhibit991er.htm) (OPENED); Q1 FY27 call transcript PDF, Nike IR (OPENED).
- MarketScreener NIKE-INC-13739 finances (OPENED 2026-10-14); Stocktwits JPMorgan article (OPENED); WebSearch results (SNIPPET).
- Repo: `data/nike_filing_facts.csv`, `data/hunt/risk_tariffs/tariff_gap_sizing.csv`, `research_notes/Long or short cruxes/expectations_gap.md`, `risk_tariffs.md`, `china_floor.md`, `na_sell_through.md`, `research_notes/Thesis decision/00_THESIS.md`, `dig_1.md`.
