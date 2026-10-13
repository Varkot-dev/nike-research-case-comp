# Why NIKE Brand footwear fell 11.7% (FY24 to FY26) while apparel fell 2.4% and equipment rose 6.0%

> **Status: DRAFT (Oct 13, 2026).** Produced by the multi-agent investigation (one investigator, two adversarial reviewers, one revision round). Sources are cited inline; independent spot-check against source documents is in progress and results will be logged at the end of this file. Treat figures as provisional until marked verified.


Revision 2 (2026-10-13). Scope: NIKE Brand product lines as reported in the 10-K revenue table (Converse is a separate line; section 2.11 tests whether Nike's "classics" figures include Converse). All dollar figures are $ millions unless stated. "CN" = currency-neutral. Derived figures come from `scratchpad/rh/scripts/fw_calc.py` and `scratchpad/rh/scripts/fw_rev2.py` (run with `python3 -I`; output `scratchpad/rh/fw_rev2_out.txt`) and are labelled "my arithmetic". Inputs I chose are labelled "assumption".

## 0. Bottom line

The two-year number hides **two different movements, not one cause**:

1. **FY25 (footwear -$3,917M): two causes.**
   - **Classics (AF1, AJ1, Dunk) shrank.** Nike says FY25 classics fell "more than 20%", and in Q4 FY25 "more than 30%, representing almost a $1 billion headwind" (Q4 FY25 call p. 14). The Q2 FY26 and Q4 FY25 statements bound the classics base (section 2.8).
     - Estimated FY25 classics decline: **about $1.4B to $3.6B**, central about $2.3B to $3.1B (my arithmetic, scenario).
     - That is **35% to 92%** of the FY25 footwear decline (central about 60% to 80%).
   - **Non-classic NIKE Brand footwear also fell, by about $0.3B to $2.5B** (central about $0.8B to $1.6B; my arithmetic).
   - A tentative split of the central $1.27B case (section 2.9):
     - FX: about -$0.24B (filing arithmetic);
     - the build-up of returns and discount reserves charged against revenue: about -$0.35B (footwear-proportional proxy);
     - China-specific weakness: about -$0.25B (assumption-based);
     - a residual of about -$0.4B, consistent with Nike's own words that Performance "also declined" and Digital lost traffic on "fewer launches".
2. **FY26 (footwear +$15M): classics fell by more than $2B, and non-classic footwear grew by at least about $1.57B to $2.0B.**
   - About $0.6B of that growth is FX, and about $0.5B is the swing from building to releasing returns and discount reserves (proxy).
   - That leaves about $0.5B to $0.9B or more of underlying growth, which fits Nike's claim that Running "added roughly a Billion dollars" (my arithmetic, section 2.10).
   - Part of the FY26 wholesale growth was sell-in that Nike later said ran ahead of sell-through (Q4 FY26 p. 12; Q1 FY27 pp. 3, 13).
   - **Greater China** footwear kept falling in FY26 (-$617M) while footwear outside GC rose (+$632M). That is a second, China-specific cause, not part of the classics event (section 2.12).

**Over two years:**
- Classics fell by **at least about $2.9B to $3.4B** (lower bound, depending on whether Converse is inside Nike's FY26 "$2B"). In the central case it fell about $4.3B to $5.1B.
- Non-classic footwear therefore changed by somewhere between **-$1.0B and +$1.7B** over FY24 to FY26 (my arithmetic).
- Classics is the **largest identified component**, and in the central case it accounts for more than the whole two-year decline.
- It is **not the only cause**:
  - In FY25 a non-classic decline of roughly $0.3B to $2.5B happened alongside it.
  - Greater China is a separate drag in FY26.
  - Revision 1's "1.03x match" of the >$4B "from peak" figure against the $3.9B decline is withdrawn as evidence (section 5).

**Why apparel and equipment diverged:** the classics are footwear franchises with no apparel equivalent. Apparel also reset earlier (FY24 apparel units -9% vs footwear -2%) and never boomed (FY22 to FY24 apparel +1.5% vs footwear +14.7%). Both are unchanged from revision 1 (section 1, #13).

**Still open (section 4):**
- the exact FY25 classics decline (Nike gives only "more than 20%");
- the split of the FY25 non-classic decline among Digital traffic, Performance, non-AJ1 Jordan retro and China;
- how much of the FY26 non-classic rebound is sell-through demand rather than pipeline refill;
- deliberate supply cut vs consumer demand inside classics.

A long-run view frames the result (my arithmetic, FY24 10-K p. 34, FY26 10-K p. 32):

| | FY22 to FY24 | FY24 to FY26 | FY22 to FY26 |
|---|---|---|---|
| Footwear | +14.7% | -11.7% | **+1.3%** |
| Apparel | +1.5% | -2.4% | -0.9% |
| Equipment | +27.8% | +6.0% | +35.4% |

## 1. Verdict table (every candidate)

| # | Candidate explanation | Verdict | Quantified contribution | Deciding evidence |
|---|---|---|---|---|
| 1 | Classic lifestyle franchises (AF1, AJ1, Dunk) reduced | **Supported: largest identified component. Not the sole cause.** | FY25: about -$1.4B to -$3.6B, which is 35% to 92% of the FY25 footwear decline (section 2.8, scenario). FY26: more than -$2.0B (at least -$1.56B for NIKE Brand if Converse is inside). Two-year: at least about -$2.9B to -$3.4B, central about -$4.3B to -$5.1B, against a footwear decline of -$3,902M (my arithmetic). | Q4 FY25 call p. 14 ("more than 20%" in FY25; Q4 "more than 30% ... almost a $1 billion headwind"; Q4 "down approximately 10 points from the peak" in mix); Q2 FY26 p. 8 (~$550M, "over 20%", ex-classics +6%); Q4 FY26 p. 8 (more than $2B) |
| 1a | Of which: deliberate supply cuts vs consumer demand fading | **Unresolved** (both present) | Not separable | Deliberate: "accelerating planned reductions" (Q4 FY24 p. 7). Demand: classics "underperformed our overall digital business" (Q4 FY24 p. 8); "Air Jordan 1 and Dunk remain elevated" (Q3 FY25 p. 12); "aged, higher-volume Sportswear footwear sold-through below expectations" (Q1 FY27 p. 3) |
| 1b | **NEW: FY25 non-classic footwear decline** (reviewer alternative) | **Supported as a second FY25 component.** Its internal split is partly unresolved. | -$0.3B to -$2.5B (central about -$0.8B to -$1.6B). Tentative split of the central -$1.27B: FX -$0.24B; reserve build -$0.35B (proxy); GC-specific -$0.25B (assumption); residual -$0.42B (my arithmetic, section 2.9) | Q4 FY25 p. 10 ("Performance also declined"); Q4 FY24 p. 13 ("lower traffic on fewer launches"); Q4 FY24 p. 14 ("muted wholesale order books, with newness not yet at scale; a softer outlook in Greater China"); FY25 10-K p. 83 (reserves $1,282M to $1,834M) |
| 1c | **NEW: FY26 non-classic rebound is partly pipeline and accounting, not demand** | **Partly supported** | Rebound of at least +$1.57B to +$2.0B. Of that, about +$0.6B is FX and about +$0.5B is the reserve swing (proxy). The residual is at least about +$0.5B to +$0.9B (my arithmetic, section 2.10). Sell-in timing is not quantified for the year. | FY26 10-K p. 37 (NA wholesale +14% including "fewer marketplace management actions"); Q1 FY26 p. 10 ("shipment timing in the prior year, as well as higher liquidation volume"); Q1 FY27 p. 13 ("higher comparison of North America sell-in"); FY26 10-K p. 84 (reserves down to $1,589M) |
| 2 | Unit declines rather than price | **Supported** (a description, not a cause) | CN units index 0.911, implied ASP index 0.958; about 68% of the CN log decline is units (my arithmetic) | FY25 10-K p. 34; FY26 10-K p. 33 |
| 3 | Pricing (ASP) | **Partly supported** as discounts plus channel mix. **Ruled out** as deliberate list-price cuts. | About 4 of roughly 13 CN points (my arithmetic) | FY25 10-K p. 34; FY26 10-K p. 33; FY25 10-K p. 35 (ASP -180 bps GM) |
| 4 | Channel: Nike Digital collapse | **Supported as the channel where #1, #1b and #5b showed up.** Revision 1's "same event as #1" is withdrawn as unproven. | NIKE Brand Direct -$3,799M vs wholesale -$305M. Product by channel is not disclosed, so how much of the Direct decline is footwear classics cannot be shown. | FY26 10-K p. 33 (Digital decline "primarily due to reduced traffic"); Q1 FY26 p. 13 (prior year "more concentrated on classic footwear franchises and sneaker launch, as well as a higher mix of off-price sales"); see `direct_decline.md` |
| 5 | Wholesale order cuts and destocking | **Supported for FY25, reversed in FY26** | Wholesale -$1,875M (FY25), +$1,570M (FY26). Part of the FY25 cut is the classics weeks-of-supply reduction; part is returns and discounts (reserve build +$552M company-wide) | FY25 10-K pp. 29, 83; Q2 FY25 call (secondary transcript: "summer order books will be down") |
| 5b | **NEW: Sneaker launch (SNKRS) traffic loss** | **Partly supported. Not separable** from #1 and #9 | Not disclosed | Q4 FY24 p. 13 "fewer launches"; Q1 FY26 p. 13 "sneaker launch" |
| 6 | Region: Greater China | **Supported as an independent cause in FY26** (it is not the classics event). **Shared with the Nike-wide cycle in FY25.** | GC footwear -$747M (FY25), -$617M (FY26). Ex-GC footwear rose +$632M in FY26. The China-specific part of FY25 is about -$0.25B (assumption). Two-year GC total -$1,364M; its classics content is not disclosed. | FY26 10-K p. 30 ("declining store traffic, elevated promotional activity and higher levels of inventory"); FY26 10-K p. 39; `gc_decline.md` section 0 item 2 |
| 7 | Running share loss | **Ruled out as a FY24 to FY26 driver; it became an offset in FY26.** Possibly a small FY25 drag (men's running flat in Q2 FY25, secondary). | Running "added roughly a Billion dollars" (management claim) | Q4 FY26 p. 3; Q1 FY25 p. 4 |
| 8 | Lifestyle share shift to adidas terrace styles | **Partly supported** (demand side of #1a) | adidas footwear +EUR 2,149M (+17.8%) CY23 to CY25 | adidas AR 2024, AR 2025 |
| 9 | Jordan Brand decline, including non-AJ1 retro | **Supported in FY25. Non-AJ1 retro share unresolved.** | Jordan -$1,431M FY25, -$236M FY26, all products. AJ1 sits inside #1. Retro "oversupply" is Nike's own words for the period up to Q1 FY27. | FY25 10-K p. 33; FY26 10-K p. 32 note 3; Q1 FY27 p. 4; Q1 FY27 p. 10 |
| 10 | FX translation | **Ruled out over two years** (+$0.4B). By year: FY25 about -$0.24B, FY26 about +$0.6B (my arithmetic) | | FY25 10-K p. 33; FY26 10-K p. 32 |
| 11 | Converse (Chuck Taylor) | **Ruled out for the NIKE Brand footwear line.** **Material for the classics bridge:** if Nike's FY26 "$2B" includes Chuck Taylor, NIKE Brand classics in FY26 fell at least $1.56B | Converse footwear -$787M FY24 to FY26 (-$343M, -$444M) | FY26 10-K p. 41; Q1 FY26 p. 6 |
| 12 | Reporting change | **Ruled out** | | FY25 10-K p. 33 note 4 |
| 13 | Apparel spared because it reset earlier | **Partly supported** | FY24 apparel units -9% vs footwear -2% | FY24 10-K p. 35 |
| 14 | Equipment growth | Context only | +$124M | FY26 10-K p. 37 |
| 15 | **NEW: Kids** | **Ruled out as material** | Kids revenue, all products, -$324M (-5.4%) in FY25. That is at most 8% of the FY25 footwear decline (my arithmetic). Not disclosed for FY26. | FY25 10-K p. 33 |
| 16 | **NEW: Non-Jordan basketball** | **Ruled out for FY26** (it grew). FY25 is not disclosed. | | Q1 FY26 p. 10 (NA "Running, Training, and Basketball each delivered double-digit growth") |
| 17 | **NEW: Ongoing demand weakness after the reset (Q1 FY27)** | **Outside the window.** Q1 FY27 footwear -$459M is about -$243M GC plus about -$200M Dunk, leaving about -$16M (my arithmetic, overlap ignored) | | Q1 FY27 10-Q pp. 14, 22; Q1 FY27 call p. 3 |

## 2. Data tables

### 2.1 NIKE Brand revenue by product ($M)

Sources: FY24 10-K p. 34 (FY22, FY23); FY25 10-K p. 33; FY26 10-K p. 32. Label: filing.

| | FY22 | FY23 | FY24 | FY25 | FY26 | FY24 to FY26 $ | % |
|---|---|---|---|---|---|---|---|
| Footwear | 29,143 | 33,135 | 33,427 | 29,510 | 29,525 | -3,902 | -11.7 |
| Apparel | 13,567 | 13,843 | 13,775 | 12,965 | 13,449 | -326 | -2.4 |
| Equipment | 1,624 | 1,727 | 2,075 | 2,191 | 2,199 | +124 | +6.0 |

Changes are my arithmetic. Footwear is 95% of the net three-line decline of -$4,104M.

### 2.2 Units and ASP: NIKE Brand, currency-neutral (filing; compounding is my arithmetic)

| | FY24 | FY25 | FY26 | Compounded FY24 to FY26 |
|---|---|---|---|---|
| Footwear revenue CN | +1% | -11% | -2% | index 0.872 |
| Footwear units | -2% | -8% | -1% | index 0.911 |
| Footwear ASP (pts) | +3 | -3 | -1 | implied index 0.958 |
| Apparel revenue CN | 0% | -5% | +2% | index 0.969 |
| Apparel units | -9% | -5% | +1% | index 0.959 |
| Apparel ASP (pts) | +9 | 0 | +1 | implied index 1.010 |

Sources: FY24 10-K p. 35; FY25 10-K p. 34; FY26 10-K p. 33. Approximation: Nike reports ASP as point contributions, and I treat revenue index ÷ units index as the ASP index.

Quarterly NIKE Brand footwear (10-Qs; filing):

| Quarter | CN rev | Units | ASP pts | Source |
|---|---|---|---|---|
| Q1 FY25 | -10% | -10% | 0 | Q1 FY25 10-Q p. 22 |
| Q2 FY25 | -12% | -7% | -5 | Q2 FY25 10-Q p. 25 |
| Q3 FY25 | -9% | -8% | -1 | Q3 FY25 10-Q p. 27 |
| Q1 FY26 | -2% | +2% | -4 | Q1 FY26 10-Q p. 22 |
| Q2 FY26 | -1% | 0% | -1 | Q2 FY26 10-Q p. 26 |
| Q3 FY26 | -1% | -2% | +1 | Q3 FY26 10-Q p. 29 |
| Q1 FY27 | -6% | -5% | -1 | Q1 FY27 10-Q p. 23 |

Pattern: FY25 was a volume collapse (units -7% to -10% every quarter). In FY26, units were roughly flat while classics were still falling by more than $2B, so other footwear was growing.

### 2.3 Footwear by region ($M; FY25 10-K pp. 38 to 41, FY26 10-K pp. 37 to 40; derived columns are my arithmetic)

| Region | FY24 | FY25 | FY26 | $ chg | % chg | Share of reported decline | CN cum. | CN $ | Units cum. | ASP cum. |
|---|---|---|---|---|---|---|---|---|---|---|
| North America | 14,537 | 12,684 | 13,317 | -1,220 | -8.4 | 31% | -8.7% | -1,257 | -4.6% | -4.2% |
| EMEA | 8,473 | 7,569 | 7,643 | -830 | -9.8 | 21% | -14.5% | -1,229 | -9.8% | -5.2% |
| Greater China | 5,552 | 4,805 | 4,188 | -1,364 | -24.6 | 35% | -26.1% | -1,446 | -23.5% | -3.4% |
| APLA | 4,865 | 4,452 | 4,377 | -488 | -10.0 | 13% | -6.9% | -335 | -4.9% | -2.0% |
| Total | 33,427 | 29,510 | 29,525 | -3,902 | -11.7 | 100% | | -4,267 | | |

Region CN and units inputs are from the region bullets: NA FY25 CN -13%, units -10%, ASP -3; FY26 CN +5%, units +6%, ASP -1. EMEA FY25 -10, -8, -2; FY26 -5, -2, -3. GC FY25 -13, -11, -2; FY26 -15, -14, -1. APLA FY25 -4, -2, -2; FY26 -3, -3, 0.

North America had turned around by FY26 (+5% CN, units +6%) while Greater China kept falling (units -14%). GC is the only region still shedding volume at double-digit rates in FY26.

### 2.4 Channel ($M; FY25 10-K p. 33, FY26 10-K p. 32; changes are my arithmetic)

| NIKE Brand | FY24 | FY25 | FY26 | FY24 to FY26 |
|---|---|---|---|---|
| Wholesale | 27,758 | 25,883 | 27,453 | -305 (-1.1%) |
| NIKE Direct | 21,519 | 18,783 | 17,720 | -3,799 (-17.7%) |
| of which Digital ($B) | 12.1 | 9.6 | 8.6 | -3.5 (-29%) |
| Direct share | 43.7% | | 39.2% | |

### 2.5 Jordan Brand (reported basis; FY25 10-K p. 33; FY26 10-K p. 32 note 3)

| FY23 | FY24 | FY25 | FY26 | FY24 to FY26 |
|---|---|---|---|---|
| 8,460 | 8,701 | 7,270 | 7,034 | -1,667 (-19.2%) |

**Repo data issue (my finding).** `research_notes/06_region_margin_product.md` section 4 and `data/nike_filing_facts.csv` (`revenue_jordan`, FY2024 = 6,988) put the FY24 **wholesale-equivalent** figure from the FY24 10-K p. 34 ("Jordan Brand | 6,988 | 6,589") next to the FY25 and FY26 **reported** figures. Nike recast FY24 to 8,701 on the reported basis (FY25 10-K p. 33). The note's "+0.7%" should read **-19.2%**. Not edited, per ground rules.

### 2.6 Classics: what Nike quantifies (Nike release, i.e. call remarks as prepared; arithmetic labelled)

| Statement | Period | Value | Source |
|---|---|---|---|
| Classics down nearly 50% on Nike Digital | Q1 FY25 | ~-50% (Digital only) | Q1 FY25 call p. 4 |
| Classics share of footwear mix to fall >10 points | Q4 FY25 | >10 pts | Q3 FY25 call p. 15 |
| NA classics down near 40% | Q4 FY25 | ~-40% | Q4 FY25 call p. 10 |
| NA classics down 30% | Q1 FY26 | -30% | Q1 FY26 call p. 10 |
| Classics headwind ~$550M, down over 20% | Q2 FY26 | -$550M | Q2 FY26 call p. 8 |
| Classics inventory removal ~5-point headwind | Q3 FY26 | ~5 pts of revenue | Q3 FY26 call p. 2 |
| Classics down more than 20% (FY25); Q4 more than 30%, almost $1B; Q4 mix down ~10 pts from peak | FY25, Q4 FY25 | > -20%; ~ -$1,000M | Q4 FY25 call p. 14 |
| Classics reduced by more than $2B | FY26 vs FY25 | > -$2,000M | Q4 FY26 call p. 8 |
| Classics more than $4B below peak | Peak to FY26 end | > -$4,000M | Q2 FY26 call p. 7; Q3 FY26 call p. 7 |
| Dunk revenue down nearly 50%, ~$200M | Q1 FY27 | -$200M | Q1 FY27 call p. 3 |

Bounds (my arithmetic):
- **Q2 FY25 classics base.** $550M ÷ 0.20 = at most about $2,750M, which is at most 35.9% of Q2 FY25 footwear ($7,655M). So classics were at most about a third of footwear by late calendar 2024. The $550M is a Nike Inc figure; comparing it with NIKE Brand footwear assumes the classics are NIKE Brand footwear (see 2.11).
- **FY26 non-classic footwear.**
  - Footwear changed +$15M while classics fell by more than $2,000M, so non-classic footwear grew by more than $2,015M.
  - Suppose the $2B also counts Converse Chuck Taylor. The most Converse could account for is its whole FY26 footwear decline of -$444M. Even then, non-classic NIKE Brand footwear grew by more than $1,571M.
  - These are reported dollars. FX added about 2 points to FY26 footwear, so the currency-neutral lower bound is roughly $1.0B.
- **Two-year comparison (superseded in revision 2).** Revision 1 set the more-than-$4B "from peak" figure against the -$3,902M decline (ratio 1.03). That is not like-for-like: the peak date is undisclosed and the basis (Converse, reported or CN) is unknown. Section 2.8 replaces it with a bottom-up FY25 estimate.

### 2.7 Peer footwear growth (market vs share)

| Company | Measure | Earlier | Later | Change | Label / source |
|---|---|---|---|---|---|
| Deckers HOKA (FY ends Mar) | Net sales $M | FY24 1,807 | FY26 2,587 (FY25 2,233) | +780 (+43.2%) | Company release: ir.deckers.com detail/240 (FY24) and detail/656 (FY26) |
| On (calendar) | Shoes net sales CHF M | 2023 1,711.8 (derived from 2,199.6 at +28.5%) | 2025 2,804.4 | +1,093 (+63.8%) | Company release FY24 PDF; press.on-running.com FY25 release |
| adidas (calendar) | Footwear net sales EUR M | 2023 12,083 | 2025 14,232 (2024 13,975; restated 13,977) | +2,149 (+17.8%) | adidas Annual Report 2024 and 2025, income statement pages |
| ASICS (calendar) | Performance Running net sales | | 2025 JPY 363.5bn, about +11% CN | | ASICS FY2025 financial summary, PDF p. 22 |

Changes are my arithmetic. The windows do not line up exactly with Nike's June to May year.

Reading:
- HOKA plus On plus adidas footwear added roughly $4B or more of footwear revenue. I have not converted currencies; this is order of magnitude only (opinion).
- That is comparable to Nike's $3.9B footwear decline. The market grew while Nike shrank, so this is share loss, not a shrinking category.
- The share went mostly to lifestyle (adidas terrace styles) and to running specialists before FY25.
- In FY26, Nike says it was gaining running share back.

### 2.8 NEW: Sizing the FY25 classics decline (my arithmetic; inputs are Nike release and filing)

Quarterly NIKE Brand footwear ($M) comes from 10-Q disaggregation tables. Q2 and Q4 are derived as YTD differences (my arithmetic):

| | Q1 | Q2 | Q3 | Q4 | Source |
|---|---|---|---|---|---|
| FY24 | 8,421 | 8,607 | 8,162 | 8,237 | Q1 FY25 10-Q p. 15; Q3 FY25 10-Q pp. 18 to 19; FY24 total 33,427 |
| FY25 | 7,462 | 7,655 | 7,208 | 7,185 | Q1 FY25 10-Q p. 15; Q2 FY26 10-Q p. 18; Q3 FY25 10-Q p. 18; FY25 10-K p. 33 |
| FY26 | 7,410 | 7,659 | 7,353 | 7,103 | Q1 FY26 10-Q p. 15; Q2 FY26 10-Q p. 18; Q3 FY26 10-Q pp. 18 to 19; FY26 10-K p. 32 |

The constraints Nike gives (all Nike release, remarks as prepared, PDF pages):
- **(a) Q2 FY25 classics base, from the Q2 FY26 call (p. 8).**
  - Facts: a headwind of "approximately $550 million", "down over 20%", total CN revenue "flat", and CN revenue "grew 6% excluding the impact of this headwind".
  - Upper bound: "over 20%" means the base is at most $2,750M.
  - The "+6% ex-classics" statement only works if the classics base is removed from the denominator. With CN growth exactly 0%, the base is $2,354M to $3,892M, so $2,354M to $2,750M together with the cap.
  - Q2 FY26 10-Q p. 25 shows total CN growth only as a rounded "0 %". At +0.5% the lower end falls to about $1,231M, so I do not rely on it. Instead I use the regional rates in the same call: North America "approximately 20%" (p. 9) and EMEA "a mid-20's percent decline" (p. 10). These make a global rate above 30% unlikely (assumption).
  - Adopted: **Q2 FY25 classics $1,833M to $2,750M, which is 23.9% to 35.9% of Q2 FY25 NIKE Brand footwear.**
- **(b) Q4.** A decline of "more than 30%" worth "almost a $1 billion headwind" (Q4 FY25 p. 14).
  - With a headwind of $850M to $1,000M: Q4 FY24 classics were at most $2,833M to $3,333M (34% to 40% of Q4 FY24 footwear), and Q4 FY25 classics at most $1,983M to $2,333M.
  - Mix: Q4 FY25 was "down approximately 10 points from the peak as a percent of our total footwear mix". The peak share is at least the Q2 FY25 share. So the Q4 FY25 share is at least 12.9% to 24.9%, and Q4 FY25 classics are at least $930M to $1,791M.
- **(c) FY25 annual rate.** "Year over year declines of more than 20%" (Q4 FY25 p. 14). I use 20% to 25% (assumption: Nike would likely have said "more than 25%" if it were).
- **(d) Pattern of the quarterly rates.** In Q1 FY25 classics declined "more than the total business" (Q1 FY25 p. 4). In Q2 FY25 the rate was "greater than the first quarter" (Q2 FY25 call, secondary transcript, fool.com). In Q3 FY25 it was "double-digit" (Q3 FY25 p. 11), and in Q4 more than 30%.

Scenario (assumption on the shape: Q1 FY25 between 1.0x and 1.1x Q2; Q3 between Q2 and Q4):

| | Low | Central | High |
|---|---|---|---|
| FY25 classics level | 5,526 | 9,396 | 10,858 |
| FY25 decline at r = 20% | 1,382 | 2,349 | 2,714 |
| FY25 decline at r = 25% | 1,842 | 3,132 | 3,619 |
| Non-classic FY25 footwear change (-3,917 + decline) | -2,535 | -1,568 to -785 | -298 |
| Implied FY24 classics as % of FY24 footwear | 20.7% | 35% to 37.5% | 43.3% |

Cross-check: suppose FY26 classics fell at no more than 30% (Q1 FY26 NA "30%"; Q2 FY26 global "over 20%"). Then FY25 classics were at least $2,000M ÷ 0.30 = $6,667M, and the FY25 decline at r = 20% was at least $1,667M. That fits the table.

**Conclusion of 2.8:**
- Classics cannot account for the whole FY25 footwear decline in any scenario except the very top of the range.
- A non-classic FY25 decline of roughly $0.3B to $2.5B is required.
- This confirms the reviewers' objection.

### 2.9 NEW: What made up the FY25 non-classic decline (central case -$1,267M; tentative)

| Component | $M | Label and basis |
|---|---|---|
| FX translation | about -240 (±167 from rounding) | my arithmetic: reported -$3,917M vs CN -11% of $33,427M (FY25 10-K p. 33) |
| Build-up of returns and discount reserves charged against revenue | about -352 | my arithmetic, proxy. Company-wide reserve balance $1,282M (May 2024) to $1,834M (May 2025), +$552M (FY25 10-K p. 83; FY24 10-K p. 85), allocated to footwear by revenue share (assumption). The returns reserve alone went from $799M to $1,277M. |
| China-specific weakness | about -253 | assumption: 35% of GC's CN footwear decline (13% of $5,552M) is China-specific, following `gc_decline.md` section 0 item 2 |
| Residual: Performance decline, Digital launch traffic, non-AJ1 Jordan retro, Air Max and other lifestyle, Kids | about -423 | my arithmetic. Not separable. Kids revenue, all products, fell $324M in FY25 (FY25 10-K p. 33). Nike: "Performance also declined" (Q4 FY25 p. 10, NA); "lower traffic on fewer launches" (Q4 FY24 p. 13). |

Caveats:
- Some of the reserve build relates to classics returns, so it overlaps #1.
- If Nike's classics figures are on a reported basis, the FX line partly belongs to classics.
- This split is indicative only. It shows that the FY25 non-classic decline can be accounted for by identified mechanisms of the right order of magnitude. It does not rank them precisely.

### 2.10 NEW: Quality of the FY26 non-classic rebound

| Component | $M | Label and basis |
|---|---|---|
| Non-classic change implied by Nike's figures | at least +2,015 (at least +1,571 if Converse is inside the $2B) | my arithmetic: footwear +$15M, classics -$2,000M or more |
| FX | about +605 | my arithmetic: footwear reported 0% vs CN -2% of $29,510M (FY26 10-K p. 32) |
| Reserve swing (from a $552M build in FY25 to a $245M release in FY26), footwear share | about +508 | my arithmetic, proxy (FY26 10-K p. 84: $1,834M to $1,589M) |
| Residual (underlying) | at least about +902 (at least about +458 with Converse inside) | my arithmetic. Fits Running "roughly a Billion dollars" (Q4 FY26 p. 3) plus Air Max and Look of Running (Q2 FY26 p. 10) |

Evidence that part of the FY26 wholesale sell-in ran ahead of sell-through, which makes some of the residual timing rather than demand:
- Q1 FY26 p. 10: NA wholesale growth was "partially due to shipment timing in the prior year, as well as higher liquidation volume to value channels".
- FY26 10-K p. 37: NA wholesale +14% "including expanded distribution, higher shipments to existing partners and fewer marketplace management actions".
- FY26 10-K p. 29: inventories flat, "primarily reflecting an increase in units".
- Q4 FY26 p. 12: "taking actions to tighten buys, reduce future sell-in".
- Q1 FY27 p. 13: "a higher comparison of North America sell-in activities versus last year".

Nike does not quantify the sell-in timing for FY26, so that slice is unresolved.

### 2.11 NEW: Converse inside "classics"?

- **What Nike said.**
  - FY25 statements name only "Air Force 1, Air Jordan 1, and Dunk" (Q1 FY25 p. 4).
  - From Q1 FY26 Nike speaks of "our largest classic franchises ... for the Nike, Jordan, and Converse brands", including "the Chuck Taylor" (Q1 FY26 p. 6).
- **What the regional rates suggest.** The Q2 FY26 classics rates are given for North America and EMEA, which are NIKE Brand segments (Converse is its own segment). That fits a NIKE Brand-only definition but does not prove it.
- **Effect on the figures (my arithmetic).**
  - Converse footwear: FY23 $2,155M, FY24 $1,800M, FY25 $1,457M, FY26 $1,013M (FY25 10-K p. 42; FY26 10-K p. 41). That is -$343M in FY25, -$444M in FY26 and -$787M from FY24 to FY26.
  - If the FY26 ">$2B" includes all of Converse's FY26 footwear decline, NIKE Brand classics fell at least $1,556M in FY26.
  - If the ">$4B from peak" includes Converse footwear's whole decline since FY23, NIKE Brand classics fell at least $2,858M from peak.
- **Verdict.** Unresolved. Section 0 and the table carry both cases.

### 2.12 NEW: Greater China as an independent cause

| $M | FY24 | FY25 | FY26 | FY25 chg | FY26 chg |
|---|---|---|---|---|---|
| GC footwear | 5,552 | 4,805 | 4,188 | -747 | -617 |
| Footwear ex-GC | 27,875 | 24,705 | 25,337 | -3,170 | **+632** |

Sources: FY25 10-K p. 40, FY26 10-K p. 39; differences are my arithmetic.

- In FY26 every region outside GC either grew footwear in reported dollars or fell slightly, while GC CN footwear fell 15% with units -14%.
- Nike's 10-K gives a China-specific mechanism: "a trend of declining store traffic, elevated promotional activity and higher levels of inventory across the marketplace" (FY26 10-K p. 30).
- `gc_decline.md` finds the rest of Nike +1.4% CN in FY26 against GC -13%.
- **Verdict:** GC is an independent cause in FY26, not the classics event seen another way.
- Its classics content is not disclosed. The one Nike statement on regional classics mix found so far is for APLA ("Our mix of classic footwear franchises in APLA is below our global business", Q2 FY25 call, secondary transcript), not GC.

## 3. Verbatim quotes with sources

Filings (label: filing). URL root: `https://investors.nike.com/sec-filings/all-sec-filings/content/`
- FY25 10-K p. 34 (`0000320187-25-000047/nke-20250531.htm`): "NIKE Brand footwear revenues decreased 11% on a currency-neutral basis. Unit sales of footwear decreased 8%, while lower average selling price ("ASP") per pair reduced footwear revenues by approximately 3 percentage points. Lower ASP per pair was primarily due to higher discounts and changes in channel mix, partially offset by strategic pricing actions."
- FY25 10-K p. 34: "NIKE Brand apparel revenues decreased 5% on a currency-neutral basis. Unit sales of apparel decreased 5%, while ASP per unit was flat"
- FY25 10-K p. 33, note 4: "we have removed the non-GAAP financial measure of wholesale equivalent revenues. There is no change to our reported revenues or gross margin."
- FY25 10-K p. 34: "NIKE Direct revenues decreased 12% due to declines in NIKE Brand Digital sales of 20% from $12.1 billion in fiscal 2024 to $9.6 billion in fiscal 2025"
- FY26 10-K p. 33 (`0000320187-26-000088/nke-20260531.htm`): "On a currency-neutral basis, NIKE Brand footwear revenues decreased 2%. Unit sales of footwear decreased 1%, while lower average selling price ("ASP") per pair reduced footwear revenues by approximately 1 percentage point. Lower ASP per pair was primarily due to channel mix, partially offset by product mix and strategic pricing."
- FY26 10-K p. 32, note 3: "sales of Jordan Brand products of $7,034 million, $7,270 million and $8,701 million in fiscal 2026, 2025 and 2024, respectively"
- FY26 10-K p. 39 (Greater China): "Footwear revenues decreased 15% on a currency-neutral basis. Unit sales of footwear decreased 14%"
- FY26 10-K p. 37 (North America): "Footwear revenues increased 5% on a currency-neutral basis. Unit sales of footwear increased 6%"
- FY24 10-K p. 35 (`0000320187-24-000044/nke-20240531.htm`): "Unit sales of apparel decreased 9%, while higher ASP per unit contributed approximately 9 percentage points"
- FY24 10-K p. 34: "Jordan Brand | 6,988 | 6,589" (wholesale-equivalent basis)
- Q1 FY27 10-Q p. 23 (`0000320187-26-000193/nke-20260831.htm`): "Unit sales of footwear decreased 5%, while lower average selling price ("ASP") per pair reduced footwear revenues by approximately 1 percentage point."

Nike earnings-call remarks as prepared (label: Nike release). URLs: `https://s1.q4cdn.com/806093406/files/doc_financials/<yyyy>/<qn>/NIKE-Inc-<QnFYyy>-UNOFFICIAL-Transcript.pdf`; Q1 FY27 is at `.../files/content_files/NIKE-Inc-Q1FY27-UNOFFICIAL-Transcript.pdf`. Page numbers are PDF pages.
- Q3 FY24, PDF p. 10: "we are pulling back supply of classics such as the Air Force 1; and we are reducing supply of Pegasus ahead of launching new innovation in the Pegasus 41."
- Q4 FY24, PDF p. 7: "we are also accelerating planned reductions for our three largest franchises. This will have a meaningful near-term impact on our overall Lifestyle growth rate."
- Q4 FY24, PDF p. 8: "we missed our Q4 plan on softer traffic, higher promotions, and lower sales of certain classic footwear franchises. More specifically, these franchises underperformed our overall digital business in the quarter"
- Q4 FY24, PDF p. 9: "we are aggressively adjusting our forward-looking plans for these franchises on Nike Digital, where they have their highest share of business."
- Q4 FY24, PDF p. 5: "Road Running, which remains a competitive battlefield."
- Q1 FY25, PDF p. 4: "We have been intentionally reducing the proportion of our business driven by our classic footwear franchises: Air Force 1, Air Jordan 1, and Dunk." and "In Q1, these franchises were down nearly fifty percent versus the prior year on Nike Digital, while we saw much better sales trends in wholesale." and "The Jordan Brand was planned down double-digits this quarter"
- Q1 FY25, PDF p. 4: running "has been one of our toughest fights over the past few years" and "Men's and Women's running footwear delivered positive growth in Q1"
- Q3 FY25, PDF p. 11: "we see the declines in classic footwear franchises almost being offset by growth in performance dimensions of our portfolio"
- Q3 FY25, PDF p. 12: "we are beginning to see Air Force 1 inventory stabilize with current retail sales, while Air Jordan 1 and Dunk remain elevated with continued actions planned ahead."
- Q3 FY25, PDF p. 15: "we expect our classic footwear franchises will be down by more than 10 points as a percent of our total footwear mix. We intend to drive this mix lower in Fiscal 26, with total units planned down double digits, with the most aggressive actions on the Dunk."
- Q4 FY25, PDF p. 10: "Sportswear declined in the quarter, driven by a near 40% reduction in our classic footwear franchises" (North America)
- Q1 FY26, PDF p. 10: "managing a 30% decline in our classic footwear franchises" (North America)
- Q1 FY26, PDF p. 13: "With a business in the prior year that was more concentrated on classic footwear franchises and sneaker launch, as well as a higher mix of off-price sales, traffic comps will remain under pressure"
- Q2 FY26, PDF p. 7: "The classics footwear franchises are on track to decline from peak levels by more than $4 billion by fiscal year end."
- Q2 FY26, PDF p. 8: "This included a top-line headwind of approximately $550 million from the reduction of our Classics franchises, down over 20% versus the prior year."
- Q3 FY26, PDF p. 2: "further removing unhealthy inventory of our classic footwear franchises from the marketplace. That created roughly a five-point headwind to our reported results."
- Q3 FY26, PDF p. 7: "by the end of this fiscal year, we will have intentionally reduced over 4 billion dollars of revenue from the peak levels of classics footwear franchises."
- Q4 FY26, PDF p. 8: "driving momentum and growth in Performance while reducing Classic footwear franchises by more than $2 billion, keeping revenue flat on a reported basis versus prior year."
- Q4 FY26, PDF p. 3: "we've added roughly a Billion dollars to our Running business." and "In FY26, across Western Europe and North America, we gained five points of Running marketshare in statement footwear"
- Q1 FY27, PDF p. 3: "As planned, we reduced revenue from the Dunk by nearly 50% in the quarter. That resulted in roughly 200-milion-dollar headwind in Sportswear." and "some aged, higher-volume Sportswear footwear sold-through below expectations."
- Q1 FY27, PDF p. 4: "Simply put we've been oversupplying our iconic retro product asking them to do too much."

Peers (label: company filing or release unless noted):
- Deckers FY26 release (https://ir.deckers.com/news-events/press-releases/detail/656/deckers-brands-reports-fourth-quarter-and-full-fiscal-year-2026-financial-results): "HOKA® brand net sales increased 15.9% to $2.587 billion compared to $2.233 billion."
- Deckers FY24 release (https://ir.deckers.com/news-events/press-releases/detail/240/deckers-brands-reports-fourth-quarter-and-full-fiscal-year-2024-financial-results): "HOKA® brand net sales increased 27.9% to $1.807 billion compared to $1.413 billion."
- On FY25 release (https://press.on-running.com/on-announces-fourth-quarter-and-full-year-results-and-the-filing-of-its-annual-report-on-form-20-f-for-2025): "net sales from shoes, apparel and accessories increased by 27.5% to CHF 2,804.4 million"
- On FY24 results PDF p. 2 (https://investors.on-running.com/files/doc_financials/2024/q4/On-presents-Q4-FY-Results-2024_EN_vFFF.pdf): "net sales from shoes, apparel and accessories increased by 28.5% to CHF 2,199.6 million"
- adidas AR 2025 (https://report.adidas-group.com/2025/en/group-management-report-financial-review/business-performance/income-statement.html): "Footwear | 14,232 | 13,977 | 2% | 7% | 12%" and "Footwear revenues for the adidas brand grew 12% on a currency-neutral basis in 2025."
- adidas AR 2024 (https://report.adidas-group.com/2024/en/group-management-report-financial-review/business-performance/income-statement.html): "Footwear | 13,975 | 12,083 | 16% | 17%" and "Next to additional newness and depth for its iconic Samba, Gazelle, Handball Spezial, and Campus products"
- ASICS FY2025 summary, PDF p. 22 (https://assets.asics.com/system/libraries/4140/Consolidated%20Financial%20Summary%20For%20The%20Fiscal%20Year%20Ended%20December%2031,%202025%28with%20script%29.pdf): "Net sales were 363.5 billion yen, up approximately 11% on a currency-neutral basis."
- Secondary only (not used as evidence): worldfootwear.com 2026-05-25 HOKA $2.59bn; worldfootwear.com 2026-03-11 adidas footwear +12%.

Revision 2 additions (Nike release unless stated; PDF pages of the remarks-as-prepared files in `dl/transcripts/`):
- Q4 FY25, PDF p. 14: "In Fiscal 25, we made significant progress managing down our classic footwear franchises, with year over year declines of more than 20%. In Q4, these declines accelerated to more than 30%, representing almost a $1 billion headwind to revenue; we also finished Q4 down approximately 10 points from the peak as a percent of our total footwear mix."
- Q4 FY25, PDF p. 10: "Sportswear declined in the quarter, driven by a near 40% reduction in our classic footwear franchises; Performance also declined"
- Q4 FY24, PDF p. 14: "more aggressive actions in managing our classic footwear franchises; continuing challenges on Nike Digital; muted wholesale order books, with newness not yet at scale; a softer outlook in Greater China"
- Q4 FY24, PDF p. 13: "lower Nike Digital growth, especially in the first half of the year, due to lower traffic on fewer launches"
- Q1 FY25, PDF p. 4: "Nike revenue in Q1 from these franchises decelerated, declining more than the total business"
- Q3 FY25, PDF p. 11: "led by a double-digit decline in our classic footwear franchises"
- Q1 FY26, PDF p. 6: "putting our largest classic franchises into a healthier position for the Nike, Jordan, and Converse brands" and "the Chuck Taylor is in the early stages of a global marketplace reset"
- Q1 FY26, PDF p. 10: "Running, Training, and Basketball each delivered double-digit growth" and "Wholesale returned to growth in the quarter, partially due to shipment timing in the prior year, as well as higher liquidation volume to value channels"
- Q2 FY26, PDF p. 8: "This means our currency neutral revenue grew 6% excluding the impact of this headwind."
- Q2 FY26, PDF p. 9 (North America): "Classic footwear franchises declining approximately 20% year over year"
- Q2 FY26, PDF p. 10 (EMEA): "a mid-20's percent decline in Classic footwear franchises was offset by growth in Air Max and the Look of Running styles"
- Q4 FY26, PDF p. 12: "we are taking actions to tighten buys, reduce future sell-in, and manage inventory" and "timing of North America Wholesale shipments"
- Q1 FY27, PDF p. 10: "Nike Sportswear and the Jordan Brand, including Men's, Women's and Kids, represented a high-single-digit drag on consolidated Nike, Inc."
- Q1 FY27, PDF p. 13: "a higher comparison of North America sell-in activities versus last year"
- Q2 FY24, PDF p. 9: Jordan "Remix footwear line, which has already surpassed the $1 billion annual revenue mark"
- Q2 FY25 call (secondary: fool.com transcript, https://www.fool.com/earnings/call-transcripts/2024/12/19/nike-nke-q2-2025-earnings-call-transcript/; Nike's own Q2 FY25 remarks PDF could not be located on s1.q4cdn.com): "For Q2, these franchises again decelerated faster than the overall business and at a rate greater than the first quarter." and "in running, men's was flat and women's up low to mid single digits" and "Our mix of classic footwear franchises in APLA is below our global business."

Filings (revision 2 additions):
- FY25 10-K p. 83: "As of May 31, 2025 and 2024, the Company's sales-related reserve balance, which includes returns, post-invoice sales discounts and claims, was $1,834 million and $1,282 million, respectively" and "sales returns reserve balance ... was $1,277 million and $799 million"
- FY26 10-K p. 84: "As of May 31, 2026 and 2025, the Company's sales-related reserve balance ... was $1,589 million and $1,834 million, respectively"
- FY24 10-K p. 85: "was $1,282 million and $994 million, respectively"
- FY26 10-K p. 37: "Wholesale revenues increased 14% including expanded distribution, higher shipments to existing partners and fewer marketplace management actions taken in the current year."
- FY26 10-K p. 30: "in Greater China, a trend of declining store traffic, elevated promotional activity and higher levels of inventory across the marketplace are negatively impacting revenues"
- FY26 10-K p. 29: "Inventories as of May 31, 2026 were $7.5 billion, flat compared to the prior year, primarily reflecting an increase in units, offset by product mix."
- FY26 10-K p. 41: Converse "Footwear | $ 1,013 | $ 1,457 | -30 % | -32 % | $ 1,800"
- FY25 10-K p. 33: "Kids' | 5,695 | 6,019 | -5 % | -5 %"
- Q2 FY26 10-Q p. 25: "TOTAL NIKE, INC. REVENUES | $ 12,427 | $ 12,354 | 1 % | 0 %"
- Q1 FY27 10-Q p. 14: Footwear "$ 3,259 | $ 1,798 | $ 866 | $ 1,028 | ... | $ 6,951"

## 4. What remains unresolved and what would resolve it

1. **The exact FY25 classics decline.** The range is $1.4B to $3.6B. It is driven by Nike's loose "more than 20%" and by unknown quarterly levels.
   - *Resolving data:* annual or quarterly classics revenue for FY24 to FY26, or the precise FY25 rate.
   - This single number fixes the FY25 non-classic decline, because the two sum to -$3,917M.
2. **The split of the FY25 non-classic decline** (section 2.9) among Performance, Digital launch traffic (SNKRS), non-AJ1 Jordan retro, Air Max and other lifestyle, Kids, and China.
   - *Resolving data:* NIKE Brand footwear revenue by sport or category (Sportswear vs Performance), and Jordan footwear vs apparel.
3. **How much of the FY26 non-classic rebound is sell-through.**
   - *Resolving data:* wholesale sell-through vs sell-in for FY26 (partner POS, Circana), and the quarterly reserve provisions and usage that Nike does not disclose.
   - The reserve-balance proxy in sections 2.9 and 2.10 nets provisions against usage and is only an approximation.
4. **The definition of "classics".** Whether Converse Chuck Taylor is included, and whether the figures are reported or CN, and Nike Inc or NIKE Brand. Also the peak year behind ">$4B from peak".
5. **Deliberate cut vs demand loss inside classics** (unchanged from revision 1).
6. **Greater China classics content.**
7. **Product by channel.**
8. **Market sizing for share** (unchanged; section 2.7).

## 5. Revision log

**Revision 2 (2026-10-13), in response to two reviewer objections ("weakened").**

1. **Failed check: "the >$4B classics reduction is about the same size, 1.03x, as the $3,902M decline, so classics is the single cause."**
   - *Withdrawn.* The ">$4B" runs from an undated peak, so it does not line up with the FY24 to FY26 window.
   - The note's own figures put almost the whole two-year decline in FY25, when classics fell by only "more than 20%" (Q4 FY25 p. 14, which revision 1 had left out).
   - Replaced by a bottom-up FY25 classics estimate (new section 2.8). It uses the Q2 FY26 base implied by the "$550 million ... over 20% ... grew 6% excluding" statements and the Q4 FY25 "$1 billion ... more than 30% ... 10 points from the peak" statements.
   - Result: FY25 classics fell about $1.4B to $3.6B, which leaves a non-classic FY25 decline of about $0.3B to $2.5B. The bottom line now presents two movements, not one cause.
2. **Failed check: "the Digital collapse, Jordan and region are the same event seen another way."**
   - *Withdrawn as unproven.* Verdicts #4, #6 and #9 were rewritten.
   - GC is now an independent cause in FY26 (new section 2.12: ex-GC footwear +$632M while GC fell -$617M).
   - The Digital link to footwear classics is stated as not shown, since product by channel is not disclosed.
3. **Failed check: Converse ruled out without testing inclusion in "classics".**
   - New section 2.11 tests it, citing the Q1 FY26 p. 6 framing.
   - The two-year classics lower bound is now given both with and without Converse inside (at least about $2.9B or at least about $3.4B).
4. **Reviewer note: "$550M is a total-company figure bounded against NIKE Brand footwear."**
   - Section 2.8 now states the assumption explicitly: classics are NIKE Brand footwear franchises.
   - It uses the NA and EMEA classics rates to support that. Nike does not disclose whether the figure includes Converse.
5. **New alternatives tested:**
   - FY25 non-classic decline (#1b, supported);
   - FY26 rebound quality (#1c, partly supported);
   - SNKRS (#5b, not separable);
   - Kids (#15, ruled out as material);
   - non-Jordan basketball (#16, ruled out for FY26);
   - post-window demand weakness (#17, Q1 FY27 explained by GC plus Dunk);
   - Jordan retro beyond AJ1 (#9, unresolved).
   - New quantifications: FX by year, and the swing in returns and discount reserves (FY24, FY25 and FY26 10-K reserve notes).
6. **Section 2.6 "two-year comparison" bullet:** now marked as superseded by section 2.8.
7. **Unchanged and re-confirmed by the reviewers:**
   - all filing and call quotes and numbers from revision 1;
   - the FX, reporting-change and list-price rulings;
   - the units vs ASP split;
   - the Jordan repo-data issue (section 2.5).
8. **Data I could not get:** Nike's own Q2 FY25 remarks PDF (404 at the usual s1.q4cdn.com paths). The Q2 FY25 quotes therefore come from a secondary transcript and are labelled as such.

## Independent verification log
- Oct 13, 2026: footwear FY2024 $33,427M and FY2026 $29,525M confirmed against the facts CSV (FY24 10-K p. 34; FY26 10-K p. 32). FY2025 NIKE Brand footwear "Unit sales of footwear decreased 8%, while lower average selling price ... reduced footwear revenues by approximately 3 percentage points" confirmed verbatim.

## Cross-note corrections (from 09_cross_note_critic_review.md)
- A5: the Q1 FY27 "residual about -$16M" is a shipment residual. Sell-through weakness may be masked by Foot Locker fill, and the global Dunk figure overlaps the GC figure. Read row 17 as unresolved.
- A6: FY25 China-specific footwear is overstated. At the footwear level it is about **-$138M**, not -$253M (GC footwear -13% vs ex-GC -10.5%). The unexplained FY25 non-classic residual therefore grows to about **-$537M**.
- A7: the reserve balance change is a proxy (direction and upper bound only), not a measured revenue flow.
