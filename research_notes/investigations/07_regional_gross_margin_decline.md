# Why did EMEA, Greater China, APLA and Converse gross margins fall from FY2023 to FY2026?

> **Status: DRAFT (Oct 13, 2026).** Produced by the multi-agent investigation (one investigator, two adversarial reviewers, revision rounds). Independent spot-checks are logged at the end of this file.


**Prepared:** October 13, 2026 (revision 3, same day). Scratch research note (not yet in the repo).
**Question:** Segment gross margin fell 350 bps in EMEA, 530 bps in Greater China, 610 bps in APLA and 1,000 bps in Converse from FY2023 to FY2026. What caused each decline, by driver, and how much is Nike-specific rather than market-wide (FX especially)?

**Correction to the question's framing:** EMEA fell **350 bps** (45.3% to 41.8%), not 400 or more. The 400 to 1,000 bps range covers Greater China, APLA and Converse only (my arithmetic on FY25 10-K pp. 39 to 42 and FY26 10-K pp. 38 to 41).

**Labels used:** *filing* (10-K or 10-Q, printed page), *Nike release* (Nike-posted "UNOFFICIAL Transcript" or remarks PDF, PDF page), *peer filing* (adidas or PUMA annual report), *secondary*, *my arithmetic*, *assumption*, *opinion*.

**Scripts and outputs (scratchpad `rh/`):**
- Revision 1 and 2: `py/gmx.py`, `py/segdump.py`, `py/fxstd.py`, `py/rgm_calc.py`; outputs `gm/bullets.txt`, `gm/seg10k.txt`, `gm/fxstd_out.txt`, `gm/calc_out.txt`.
- Revision 3: `py_r3/fx_r3.py` (translation test of currency weights, output `gm/r3_fx_out.txt`), `py_r3/recon_r3.py` and variants `recon_r3_u.py`, `recon_r3_tol15u.py` (reconciliation of the FX model with Nike's company-level FX disclosures, outputs `gm/r3_recon_out.txt`, `gm/r3_recon_u_out.txt`), `py_r3/alts_r3.py` (bounds for alternative explanations, output `gm/r3_alts_out.txt`), `py_r3/qcheck.py` (checks every quote against the downloaded source text), `py_r3/find.py` and `py_r3/pdfpg.py` (page lookup).
- New downloads: `dl/r3/nike/` (Q1 to Q3 FY24 10-Qs, Q1 to Q3 FY23 10-Q text, SEC submissions index), `dl/r3/fx/ecb_m_more.csv` (ECB monthly rates for 21 currencies from 2019), `dl/r3/adidas/` (adidas segmental-information notes 2022 to 2025 and 2023 income statement).

---

## 0. Answer in brief

No single cause explains all four segments. After revision 3, the picture is:

1. **Standard-rate FX is the largest identifiable driver in EMEA and Greater China and a large one in APLA, but it is smaller than revision 2 claimed.** Nike books each region's USD-priced product purchases at standard rates set 9 to 12 months ahead. Nike's own company-level numbers (consolidated "net FX including hedges" minus the Corporate actual-vs-standard change) imply segment standard-rate FX of about **-157 bps of company gross margin over FY2024 to FY2026** (-154, +9, -12 by year). My uncalibrated model overshot this by 1.1x to 3x. Only scenarios with an effective USD pass-through of about 0.55 to 0.75 fit Nike's figures in every year. Constrained that way, the cumulative FX effect is:

   | Segment | FX, constrained to Nike's disclosures (central; wide) | Total decline | FX share (central) |
   |---|---|---|---|
   | EMEA | -227 to -267; wide -207 to -493 | -350 | about 65 to 76% |
   | Greater China | -262 to -385; wide -239 to -444 | -530 | about 49 to 73% |
   | APLA | -208 to -430; wide -174 to -625 | -610 | about 34 to 70% |
   | Converse | -39 to -233; wide -36 to -268 | -1,000 | about 4 to 23% |

   (my arithmetic, Section 2.10; "central" keeps scenarios within ±15 bps of Nike's implied company-level FX in each year, "wide" within ±25 bps). **FX alone no longer exceeds EMEA's decline.**
2. **The Corporate offset is real but is a timing effect, and its size depends on the base year.** Corporate gross profit swung from -$535M (FY2023) to +$97M (FY2026).
   - From an FY2023 base, 40 to 50% of the combined EMEA + GC + APLA decline is recovered in Corporate.
   - From an FY2022 base, only 17 to 21% is (my arithmetic, Section 2.7).
   - The FX cost was not avoided. It hit the consolidated P&L earlier, in FY2023, through Corporate. It then moved into segment margins when standard rates reset in FY2024.
3. **Non-FX drivers, by segment:**
   - **Converse** (-1,000): lower ASP from discounts (-551) and FY2026 reset costs, meaning obsolescence reserves and severance in cost of sales (residual about -390 to -410 in FY2026). IEEPA tariffs nearly net to zero within FY2026, because Nike's recovery offsets the IEEPA tariffs it expensed that year. Post-IEEPA replacement tariffs cost at most about -37 bps.
   - **Greater China**: FY2025 obsolescence reserves (FY2025 residual -276 to -319), after the FY2024 inventory build.
   - **EMEA**: the FY2024 price increase was given back through discounts and channel mix in FY2025 and FY2026. The non-FX remainder (-231 to -271 cumulative) sits mostly in FY2024. Most of it looks like product and channel mix inside the per-unit ASP measure, not a cost line, because Nike cites lower product and other costs for EMEA in FY2024. FY2026 also carries some severance in cost of sales (0 to -122 bps) and an inventory build.
   - **APLA**: the split between FX and the rest stays open. The non-FX residual is -266 to -488 cumulative. Three things sit in it:
     - CASA distributor transition: at most about -50 bps, in Q1 FY2024 only.
     - FY2025 warehousing and logistics, discounts and inventory clean-up.
     - An FY2026 territory mix that shifted toward the Central & South America distributor business.
4. **Peer read-across, corrected for base year.** adidas's 2022 Greater China margin was a trough (46.7%, down 5.1 pts). From a common pre-shock base (adidas 2021, Nike FY2022):
   - adidas gained +80 bps in Europe/EMEA and +80 bps in Greater China.
   - Nike lost -410 and -390 bps.
   - The gap is still 470 to 490 bps, but it is smaller than revision 2's comparison implied (for GC, -530 vs +590).
   - adidas's central gross profit stayed at +178 to +214 bps of sales from 2023 to 2025, so its segment margins are not distorted by a central swing like Nike's.
   - adidas credits its improvement to lower sourcing costs, a better mix and less discounting. Part of that is its own cycle (recovery from its 2022 trough), so the gap shows FX was not sufficient to explain Nike's decline. It does not prove how much of the gap is a Nike "failure" versus adidas tailwinds. PUMA's 2025 pattern (write-downs and promotions) resembles Nike's.

---

## 1. Candidate explanations and verdicts

Quantities are cumulative FY2023 to FY2026 segment gross margin effects in bps unless stated. Negative means it lowered margin. "Central" FX is the Section 2.10 constrained range.

| # | Candidate explanation | Verdict | Quantified contribution | Evidence that decided it |
|---|---|---|---|---|
| 1 | **Standard-rate FX:** a weaker local currency raises the local cost of USD-priced purchases | **Supported** (largest identifiable driver for EMEA and GC; large for APLA; small for Converse). **Revised down** in revision 3 | Central: EMEA -227 to -267; GC -262 to -385; APLA -208 to -430; Converse -39 to -233 (my arithmetic, Section 2.10) | Nike names standard FX in FY24 for all four segments, FY25 for GC and APLA, FY26 for EMEA, GC and APLA. Magnitudes are now constrained by Nike's company-level FX (bridge minus Corporate FX change: -154, +9, -12 bps). The uncalibrated model overshot 1.1x to 3x |
| 2 | **Reporting construct:** hedge results and actual-vs-standard differences sit in Corporate, and the FY23 base was flattered | **Supported, base-year dependent; a timing effect, not avoided cost** | From FY23: 40 to 50% of the combined three-region decline (471 bps) recovered in Corporate. From FY22: 17 to 21% of 514 bps (my arithmetic, Section 2.7) | Corporate GP -$535M (FY23), -$38M (FY24), -$31M (FY25), +$97M (FY26). FX changes $588M (FY24 10-K p. 44), -$88M (FY25 10-K p. 43), +$147M (FY26 10-K p. 42), -$352M (FY23 10-K p. 42) |
| 3 | **Lower ASP from discounts and promotions** | **Supported** for Converse and EMEA (FY25 to FY26), partly for APLA; **ruled out** as a main GC driver | ASP effect (local currency): EMEA +425, -142, -135 (net +148); GC -36 net; APLA +86 net; Converse -551 | Units and ASP bullets in each 10-K. GC bullets cite *higher* ASP from pricing in FY24 and FY25 (FY25 10-K p. 40) |
| 4 | **Channel mix:** lower Direct share | **Partly supported** (inside #3, not additive) | EMEA -57 to -95; GC -35 to -58; APLA -37 to -61; Converse about 0 (assumes a 15 to 25 pt Direct vs wholesale GM gap) | Direct share EMEA 36.5% to 32.7%, GC 46.7% to 44.3%, APLA 41.9% to 39.5% (my arithmetic). EMEA FY25 10-K p. 39: "Lower ASP primarily reflects changes in channel mix and higher discounts" |
| 5 | **Inventory obsolescence reserves** | **Supported** for GC (FY25) and Converse (FY26); **partly** for EMEA (Q2 FY25, reversed) | GC FY25 residual -276 to -319 (central); Converse FY26 residual -386 to -410, which also holds severance and tariffs (#6, #9) | GC FY25 10-K p. 40; GC Q3 FY26 10-Q p. 36 "+300 ... primarily due to lower inventory obsolescence reserves"; Converse FY26 10-K p. 42 |
| 6 | **Severance in cost of sales** | **Supported** for Converse (FY26); **partly supported** for EMEA (FY26) | Converse: inside the FY26 residual. EMEA FY26: 0 to -122 (bound); about -40 if EMEA took a third of the $154M (assumption) | FY26 10-K p. 89: $154M of severance "classified within Cost of sales ... The majority ... within Global Brand Divisions, North America and EMEA". Q4 FY26 remarks PDF p. 9: "additional severance costs related to supply chain actions in North America and EMEA" |
| 7 | **Higher product costs** (input costs, product mix) | **Partly supported:** offsetting by year | EMEA Q3 FY25 "other product costs": at least -281 bps of the quarter, about -64 bps of FY25; **reversed in Q3 FY26, so net zero FY23 to FY26** | Q3 FY25 10-Q p. 33; consolidated Q3 FY25 "Higher NIKE Brand product costs (-70 bps)" p. 28; Q3 FY26 10-Q p. 35 "+100 ... primarily due to higher other product costs in the prior year" |
| 8 | **Warehousing and logistics** | **Partly supported:** headwind for APLA (FY25) and Converse (FY25, Q1 FY26), tailwind for EMEA | Not separable; inside residuals | APLA FY25 10-K p. 41; Converse FY25 10-K p. 43; Converse Q1 FY26 10-Q p. 30 |
| 9 | **U.S. tariffs** | **Ruled out** for EMEA, GC and APLA. **Converse: about net zero for IEEPA within FY26; replacement tariff at most -37** | IEEPA cost about -179 and recovery +179 (FY26); post-February 2026 replacement tariff -12 to -37 (bound, my arithmetic) | FY26 10-K p. 30: recovery "largely offsetting the impact of the IEEPA tariffs recognized during fiscal 2026". Q4 FY26 remarks PDF pp. 8 to 9: offsets "the IEEPA tariffs embedded within cost of sales that had been expensed through the income statement throughout Fiscal 26". Q4 FY26 PDF p. 12: "incremental tariff rates of 10% continuing through the end of July" |
| 10 | **Converse licensee mix** | **Ruled out** as a cause (it helped) | About +75 | Converse tables FY24 to FY26 10-Ks |
| 11 | **Industry-wide promotions** | **Partly supported** (EMEA FY26; PUMA parallel) | Not quantifiable | Nike Q1 FY26 call; adidas "reduced discounting" in Europe and GC; PUMA 2025 promotions |
| 12 | **Segment restatement, or the CASA business-model change, distorting the base** | **Restatement ruled out. CASA partly supported but small:** APLA FY24 0 to -50 | CASA: -34 to -38 under assumed distributor terms; data cap -50 (my arithmetic, Section 2.11) | FY23 and FY24 GM identical across the FY25 and FY26 10-Ks. Q1 FY24 10-Q p. 30: transition "reduced APLA revenue growth by approximately 3 percentage points"; 6M FY24 10-Q p. 35 and FY24 10-K p. 42: "did not have a material impact on APLA revenues" |
| 13 | **Inventory glut** | **Supported** for GC (FY24 build, FY25 reserves); **partly supported** for EMEA (FY26 build feeding discounts) and APLA (FY25 to FY26 clean-up); **ruled out** for Converse | Works through #3 and #5 | EMEA days 98 (FY24) to 112 (FY26); Q4 FY26 remarks PDF pp. 10 to 11: "heightened inventory and promotional levels" and "Total inventory dollars were up low double digits". APLA Q4 FY25: "further work required to clean up inventory" |
| 14 | **Lower volume as such** | **Ruled out** as a direct GM cause; it works through #3, #5, #6 and #8 | 0 directly | GM is a ratio |
| 15 | **Country and territory mix within segments** (new) | **APLA FY26: partly supported, unquantified. EMEA, GC: unresolved** (no disclosure) | Cannot be sized; Nike's FY26 APLA bullet names FX alone | FY26 10-K p. 40: APLA revenue lower "in Southeast Asia & India, Japan and Korea, partially offset by higher revenues in Central & South America and Pacific". The translation test (Section 2.10) allows APLA USD-like weights from 0 to 0.50 |
| 16 | **Non-US duties or anti-dumping costs** (new) | **Not supported** (no evidence) | 0 identified | A search of every FY23 to Q1 FY27 10-K and 10-Q found "duty" or "anti-dumping" only in risk-factor text. EMEA FY24 and FY25 cite *lower* product costs |
| 17 | **Peer outcome reflects adidas's own recovery, not Nike failure** (new) | **Partly supported** | It narrows the GC gap from about 11 pts to 4.7 pts | adidas GC 2022 "decreased by 5.1 percentage points to 46.7% from 51.8% in 2021" (adidas 2022 AR); common-base comparison in Section 2.9 |

**Surviving explanations by segment (weight in brackets, central case):**
- **EMEA:** standard FX (about two-thirds); FY24 pricing given back through discounts and channel mix in FY25 and FY26; product and channel mix not captured as price; FY26 inventory build and severance (small).
- **Greater China:** standard FX (about half to three-quarters); FY25 obsolescence after the FY24 inventory build.
- **APLA:** standard FX (about one-third to two-thirds) plus discounts, logistics, inventory clean-up, CASA (at most -50) and FY26 territory mix. The FX share is unresolved within a range of about 220 bps.
- **Converse:** discounting (more than half), FY26 reset costs (obsolescence and severance), small FX. Tariffs net to about zero within FY26.

---

## 2. Data tables

### 2.1 Segment gross margin and yearly change (filing; changes are my arithmetic and match Nike's stated bps)

| Segment | FY2022* | FY2023 | FY2024 | FY2025 | FY2026 | FY24 bps | FY25 bps | FY26 bps | FY23 to FY26 | Q1 FY2027 (y/y) |
|---|---|---|---|---|---|---|---|---|---|---|
| EMEA | 45.9% | 45.3% | 44.2% | 43.2% | 41.8% | -110 | -100 | -140 | **-350** | 44.4% (+140) |
| Greater China | 49.6% | 51.0% | 50.2% | 46.0% | 45.7% | -80 | -420 | -30 | **-530** | 47.5% (+30) |
| APLA | 50.0% | 48.1% | 45.9% | 44.0% | 42.0% | -220 | -190 | -200 | **-610** | 42.3% (-150) |
| Converse | 53.3% | 53.8% | 52.5% | 48.7% | 43.8% | -130 | -380 | -490 | **-1,000** | 45.2% (-210) |

Sources: FY25 10-K pp. 39 to 42 (FY23); FY26 10-K pp. 38 to 41 (FY24 to FY26); Q1 FY27 10-Q pp. 27 to 30. \*FY2022 is my arithmetic: FY23 level minus the FY23 10-K bps (EMEA -60, p. 38; GC +140, p. 39; APLA -190, p. 40; Converse +50, p. 41).

### 2.2 Every segment gross margin bullet, FY2023 to Q1 FY2027 (filing; drivers in Nike's order; "+" means expanded)

Abbreviations: **FX** = standard FX; **ASP-** = lower ASP; **disc** = discounts; **chmix** = channel mix; **pmix** = product mix; **obs** = obsolescence reserves; **PC** = product costs; **W&L** = warehousing and logistics.

| Period (doc, page) | EMEA | Greater China | APLA | Converse |
|---|---|---|---|---|
| FY23 (FY23 10-K pp. 38 to 41) | -60: PC (input, freight, pmix), other costs, FX; offset by full-price ASP | +140: laps FY22 obs, FX favorable, ASP; offset by PC | -190: PC, FX; offset by ASP | +50: ASP, lower other costs, licensees; offset by PC, DTC promos, FX |
| Q1 FY24 (10-Q p. 30 for APLA) | n/a | n/a | **-410: PC, FX, Direct margin; offset by ASP** (CASA revenue effect -3 pts this quarter) | n/a |
| FY24 (FY24 10-K pp. 40 to 43) | -110: **largely FX**; offset by pricing, lower other costs, lower PC (freight) | -80: **FX**; offset by pricing, lower other costs | -220: **FX**, Direct margin, PC; offset by ASP | -130: **FX**, lower ASP, other costs, DTC margin; offset by freight |
| Q1 FY25 (10-Q pp. 26 to 29) | +190: lower PC (freight), W&L; offset by FX | -170: **FX**, PC, other costs incl. **obs**; offset by pricing | +20: pricing; offset by PC | -50: ASP-, logistics, FX |
| Q2 FY25 (10-Q pp. 30 to 34) | +100: **FX favorable**, W&L; offset by ASP- (chmix), obs | -490: **FX**, ASP- (disc), **obs** | -120: ASP- (chmix, disc), W&L | -380: ASP-, logistics, **obs** |
| Q3 FY25 (10-Q pp. 33 to 37) | **-420: higher other PC**, ASP- (chmix, disc); offset by W&L | -580: **obs**, **FX**; offset by ASP | -250: ASP- (disc, pmix), FX, W&L; offset by lower PC | -470: ASP- (disc); offset by lower PC |
| FY25 (FY25 10-K pp. 39 to 43) | -100: ASP- (chmix, disc); offset by W&L, PC | -420: **FX and obs**; offset by ASP | -190: **FX**, ASP-, W&L | -380: ASP- (disc), W&L; offset by PC |
| Q1 FY26 (10-Q pp. 26 to 30) | -310: PC, ASP- (disc); offset by W&L | -150: PC (pmix) | -270: ASP- (pmix, disc, chmix), FX | -620: ASP- (disc, pmix), W&L (**no PC cited**) |
| Q2 FY26 (10-Q pp. 31 to 36) | -270: ASP- (disc), PC; offset by W&L, lower obs | -280: **obs**, PC (pmix); offset by ASP | -180: PC, FX | -700: ASP- (disc) and **higher PC** |
| Q3 FY26 (10-Q pp. 35 to 40) | +100: laps prior-year "other PC"; offset by disc, FX | **+300: lower obs** | -200: **FX** | **-970: reset costs (severance, obs)** |
| FY26 (FY26 10-K pp. 38 to 42) | -140: ASP- (disc), **FX** | -30: **FX** | -200: **FX** | -490: ASP- (disc, chmix), reset costs (obs, severance) |
| Q1 FY27 (10-Q pp. 27 to 31) | +140: lower PC, W&L; offset by ASP- | +30: lower PC; offset by ASP-, obs | -150: ASP- (disc, chmix), FX | -210: PC, W&L; offset by higher ASP |

**Counts (my arithmetic on the table):** In the 9 region-years from FY2024 to FY2026 for EMEA, GC and APLA, the annual bullet names standard FX first or alone in 7 and as a driver in 8. No EMEA, GC or APLA bullet from FY23 to Q1 FY27 cites tariffs or duties.

### 2.3 Quarterly gross margin (my arithmetic, approximate)

FY24 Q1 to Q3 are derived from FY25 10-Q bps changes; FY25 and FY26 Q1 to Q3 are reported. Q4 equals (FY gross profit minus 9M gross profit) / (FY revenue minus 9M revenue); about ±0.5 pt rounding error.

| Segment | FY24 Q1 | Q2 | Q3 | Q4 | FY25 Q1 | Q2 | Q3 | Q4 | FY26 Q1 | Q2 | Q3 | Q4 | Q1 FY27 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| EMEA | 44.2 | 44.9 | 43.9 | 43.7 | 46.1 | 45.9 | **39.7** | 40.3 | 43.0 | 43.2 | 40.7 | 40.0 | 44.4 |
| Greater China | 50.4 | 49.0 | 50.8 | 50.6 | 48.7 | **44.1** | 45.0 | 46.2 | 47.2 | **41.3** | 48.0 | 45.9 | 47.5 |
| APLA | 46.3 | 45.2 | 46.1 | 46.3 | 46.5 | 44.0 | 43.6 | 41.8 | 43.8 | 42.2 | 41.6 | 40.7 | 42.3 |
| Converse | 54.0 | 52.1 | 51.1 | 52.5 | 53.5 | 48.3 | 46.4 | 45.0 | 47.3 | 41.3 | **36.7** | 49.0* | 45.2 |

\* Converse Q4 FY26 includes the full-year $21M IEEPA recovery (FY26 10-K p. 30), worth about 860 bps on Q4 revenue of about $244M (my arithmetic). The IEEPA tariffs it offsets were expensed across Q1 to Q4 FY26 (Q4 FY26 remarks PDF p. 9), so Q1 to Q3 are understated and Q4 overstated by tariff timing. Q4 excluding the recovery is about 40%.

### 2.4 FX: proxy standard rates (my arithmetic on ECB monthly reference rates; local currency per USD)

**Method:** Nike assigns standard rates twice a year, "approximately nine and twelve months in advance," "based on average market spot rates in the calendar month preceding" (FY24 10-K p. 86). The proxy averages the spot rate of the month before setting, at 9 and 12 month leads, for seasons starting June and December. Nike does not publish its standard rates.

| Currency | FY23 std | FY24 std | FY25 std | FY26 std | Change FY24 | FY25 | FY26 | FY27 | FY23 to FY26 | FY26 actual avg |
|---|---|---|---|---|---|---|---|---|---|---|
| EUR | 0.858 | 0.962 | 0.922 | 0.934 | +12.1% | -4.1% | +1.2% | -7.4% | +8.8% | 0.858 |
| GBP | 0.729 | 0.829 | 0.796 | 0.787 | +13.7% | -3.9% | -1.2% | -5.0% | +7.9% | 0.744 |
| CNY | 6.41 | 6.88 | 7.16 | 7.22 | +7.3% | +4.2% | +0.7% | -1.6% | +12.6% | 7.03 |
| JPY | 112.1 | 134.8 | 145.3 | 151.9 | +20.3% | +7.8% | +4.5% | -0.8% | +35.6% | 153.1 |
| KRW | 1,167 | 1,306 | 1,322 | 1,389 | +11.9% | +1.3% | +5.0% | +2.4% | +19.1% | 1,437 |
| AUD | 1.355 | 1.454 | 1.530 | 1.533 | +7.3% | +5.2% | +0.2% | -1.3% | +13.1% | 1.485 |
| MXN | 20.3 | 19.6 | 17.3 | 19.2 | -3.8% | -11.6% | +10.9% | -3.8% | -5.7% | 18.1 |
| INR | 74.2 | 80.3 | 82.9 | 84.7 | +8.2% | +3.2% | +2.2% | +4.1% | +14.1% | 89.9 |
| TRY | 10.3 | 17.8 | 26.5 | 34.2 | +72.5% | +49.3% | +28.6% | +21.3% | +231% | 42.5 |

Positive change = local currency weaker = GM headwind. Revision 3 extends the proxy to CHF, PLN, SEK, ZAR, HKD, NZD, SGD, THB, PHP, IDR, MYR and CAD, with a one-quarter cost-of-sales lag variant (`gm/r3_fx_out.txt`, block A). FY23 std vs FY22 std is about flat for EUR (-0.1%), which is consistent with Nike citing only minor standard FX effects in FY23 bullets.

**The lag explains the FY2026 pattern.** In FY2026 the actual euro (0.858) was stronger than the standard rate (0.934). Reported EMEA revenue rose 3% while currency-neutral revenue fell 3% (FY26 10-K p. 38), yet EMEA's segment margin still shows unfavorable standard FX. The benefit landed in Corporate (+$147M FY26 change). CFO, Q1 FY26 call PDF p. 14: "Foreign exchange has become a tailwind to reported revenue, but we expect minimal benefit to gross margin in Fiscal 26 due to our hedged positions entering the year."

**Directional check.** The proxy predicts an FX tailwind for EMEA in FY2025 and FY2027. Nike's Q2 FY25 EMEA bullet cites "favorable changes in standard foreign currency exchange rates" (Q2 FY25 10-Q p. 30), and Q1 FY27 EMEA cites no FX headwind. APLA is the only region where the proxy still weakens into FY2027 (KRW, INR), and it is the only Nike Brand region still citing FX in Q1 FY2027. The proxy gets the direction right. Revision 3 shows that its magnitude, applied at full pass-through, is too large (Section 2.10).

### 2.5 Decomposition (my arithmetic; revision 3 replaces the revision 2 table)

**Model:** (1 - GM_t) / (1 - GM_t-1) = (1 + u x fx) x (1 + c) / (1 + p). Here fx is the basket standard-rate change; u is effective pass-through (USD-priced share of cost of sales times any proxy scaling); p is the local-currency ASP change from Nike's units and ASP bullets; c is the residual.
- Bps per factor = -(1 - GM_t-1) x ln(factor). The decomposition is additive in logs, so **the order of the factors does not change the numbers**. What can be argued is the *interpretation* of p (see EMEA below).
- **Revision 3 change:** currency weights are restricted to sets consistent with Nike's reported FX translation (Section 2.10, test 1). u and the weights are then restricted to scenarios whose company-level total matches Nike's implied segment standard FX in each year (test 2).

| Segment | Year | Actual Δ | FX central (±15 fit) | ASP (p) | Residual, central |
|---|---|---|---|---|---|
| EMEA | FY24 | -110 | -289 to -340 | +425 (+8.1%) | -195 to -246 |
| | FY25 | -100 | +83 to +98 | -142 (-2.5%) | -41 to -56 |
| | FY26 | -140 | -21 to -24 | -135 (-2.3%) | +16 to +19 |
| | **Cumulative** | **-350** | **-227 to -267** (wide -207 to -493) | **+148** | **-231 to -271** (wide -5 to -291) |
| Greater China | FY24 | -80 | -154 to -226 | +6 | +68 to +140 |
| | FY25 | -420 | -91 to -134 | -10 | **-276 to -319** |
| | FY26 | -30 | -17 to -25 | -32 | +19 to +27 |
| | **Cumulative** | **-530** | **-262 to -385** (wide -239 to -444) | **-36** | **-109 to -232** (wide -50 to -255) |
| APLA | FY24 | -220 | -119 to -266 | +141 (+2.8%) | -95 to -242 |
| | FY25 | -190 | +13 to -40 | -55 (-1.0%) | -95 to -148 |
| | FY26 | -200 | -101 to -124 | 0 | -76 to -99 |
| | **Cumulative** | **-610** | **-208 to -430** (wide -174 to -625) | **+86** | **-266 to -488** (wide -71 to -522) |
| Converse | FY24 | -130 | -40 to -203 | -141 (-3.0%) | +51 to +214 |
| | FY25 | -380 | +25 to -1 | -335 (-6.8%) | -44 to -70 |
| | FY26 | -490 | -5 to -29 | -75 (-1.4%) | **-386 to -410** |
| | **Cumulative** | **-1,000** | **-39 to -233** (wide -36 to -268) | **-551** | **-216 to -410** (wide -181 to -413) |

Source: `gm/r3_recon_u_out.txt` (blocks C6 and C7, ±15 and ±25 runs).

**How to read it:**
- **EMEA:** FX is about two-thirds of the decline, not more than all of it. The FY24 residual of about -200 to -250 conflicts with Nike's FY24 bullet, which cites *lower* other and product costs. The likely reconciliation (opinion) is that p overstates the price benefit: footwear ASP rose partly on "a higher mix of NIKE Direct sales" and apparel ASP +11 pts came with units -17% (FY24 10-K p. 40). Higher per-unit ASP from mix carries higher cost per unit, so it adds less margin than a pure price rise. Read ASP and residual together: net price, mix and cost effects come to -83 to -123 bps cumulative, against FX of -227 to -267. Under either reading FX is the largest single item, but the ranking depends on treating the ASP-plus-residual as one bucket.
- **Greater China:** FX about half to three-quarters. The FY25 residual (about -300) matches "higher inventory obsolescence reserves". The FY24 positive residual matches pricing and lower other costs.
- **APLA:** FX and non-FX are each between about one-third and four-fifths. Unresolved (Section 4).
- **Converse:** ASP (discounting) is the largest driver. The FY26 residual (about -400) is reset costs (obsolescence plus severance), any non-tariff "higher product costs" in Q2, and at most -37 of post-IEEPA replacement tariffs. **IEEPA nets to about zero within FY26**: Nike says the $21M recovery offsets IEEPA tariffs expensed during FY26. Revision 2's "excluding the recovery, the residual would be about -580" was wrong, because it removed the recovery but left the matching tariff cost in.

### 2.6 Consolidated gross margin bridge (filing; company-level bps)

| Driver | FY24 (10-K p. 36) | FY25 (10-K p. 35) | FY26 (10-K p. 34) |
|---|---|---|---|
| NIKE Brand full-price ASP / ASP | +200 | -180 | n/a |
| Product costs | +10 | +80 | -20 |
| Net FX incl. hedges | **-40** | **-10** | **+20** |
| Other costs (incl. obsolescence in FY25) | +10 | -90 | +20 |
| Nike Direct margin | -40 | n/a | n/a |
| Off-price margin | -20 | n/a | n/a |
| Warehousing and logistics | n/a | +20 | +20 |
| Converse | n/a | -20 | -20 |
| Restructuring | -10 | +10 | n/a |
| **Total** | **+110** | **-190** | **+20** |

The FY23 10-K bridge lists "Unfavorable changes in net foreign currency exchange rates, including hedges" without bps (FY23 10-K p. 34). In FY25 and FY26 Converse has its own bridge line, so Converse FX sits there rather than in the FX line.

### 2.7 Corporate offset (filing inputs; my arithmetic)

| | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|
| Corporate gross profit ($M) | about -183 (implied) | -535 | -38 (incl. -$64M restructuring) | -31 | +97 |
| Corporate FX change disclosed ($M) | | -352 | +588 | -88 | +147 |
| EMEA + GC + APLA revenue ($M) | 25,981 | 27,097 | 27,881 | 25,094 | 24,662 |

Sources: FY25 10-K p. 43 (FY23 to FY25 Corporate); FY26 10-K p. 42; FY24 10-K p. 44 ($588M; $64M restructuring); FY23 10-K p. 42 ("an unfavorable change of $352 million related to the difference between actual foreign currency exchange rates and standard foreign currency exchange rates"). The FY22 figure is my arithmetic: FY23 Corporate GP less the FY23 FX change, assuming other Corporate items were unchanged. The FY23 10-K does not report Corporate gross profit.

**Sensitivity of "how much is recovered in Corporate" (my arithmetic, `gm/r3_alts_out.txt` D5):**

| Base year | Share of Corporate FX attributed to the three regions (assumption) | Segment-basis decline to FY26 | Including allocated Corporate | Recovered |
|---|---|---|---|---|
| FY23 | 0.80 / 0.90 / 1.00 | -471 | -282 / -258 / -235 | 40% / 45% / 50% |
| FY22 | 0.80 / 0.90 / 1.00 | -514 | -426 / -415 / -404 | 17% / 19% / 21% |

The share is below 1.0 because Corporate FX also covers Canada (inside North America) and Converse's non-USD business. The Section 2.10 model puts these at roughly 10 to 15% of company standard-rate FX.

**Non-FX items in Corporate gross profit are small.** The FY24 change of +$497M equals FX +$588M, restructuring -$64M and other -$27M (my arithmetic). Treating FY23's -$535M as mostly FX is reasonable, but it is not exact.

**Reading:** the "flattered base" is specific to FY2023, when the dollar spike was booked in Corporate before standard rates reset. Measured from FY2022, the three-region decline is still about 400 to 430 bps after Corporate. Most of the decline is economic, not an artefact of the segment split.

### 2.8 Channel and inventory (filing inputs; my arithmetic)

| Segment | Direct share FY23 / FY24 / FY25 / FY26 | Inventory at May 31, $M (FY23 / 24 / 25 / 26) | Inventory / COGS days |
|---|---|---|---|
| EMEA | 36.5 / 37.1 / 34.6 / 32.7% | 2,167 / 2,028 / 2,042 / 2,253 | 108 / 98 / 107 / 112 |
| Greater China | 46.7 / 43.5 / 43.8 / 44.3% | 973 / 1,070 / 951 / 793 | 100 / 104 / 98 / 91 |
| APLA | 41.9 / 41.6 / 41.2 / 39.5% | 894 / 810 / 905 / 964 | 98 / 81 / 94 / 97 |
| Converse | 40.1 / 40.0 / 41.0 / 40.6% | 305 / 296 / 272 / 171 | 99 / 109 / 114 / 95 |

Sources: channel tables FY24 10-K pp. 40 to 43, FY25 10-K pp. 39 to 42, FY26 10-K pp. 38 to 41; segment inventories FY24 10-K p. 88, FY25 10-K p. 85, FY26 10-K p. 86. Segment inventories are at standard rates. The FY26 EMEA build is confirmed in Nike's words: "EMEA continues to work through heightened inventory and promotional levels" and "Total inventory dollars were up low double digits" (Q4 FY26 remarks PDF pp. 10 to 11).

### 2.9 Peers: regional gross margin (peer filing)

| Region | adidas 2021 | 2022 | 2023 | 2024 | 2025 | adidas stated drivers | Nike FY22 / FY23 / FY26 |
|---|---|---|---|---|---|---|---|
| Europe / EMEA | 50.8% (EMEA) | 50.5% (EMEA) | 46.4% (EMEA); 45.9% (Europe, restated) | 50.3% | 51.6% | 2023: "Unfavorable currency developments, significantly higher supply chain costs and the negative impact from higher discounting"; 2024: "Lower sourcing costs, a better business mix, and reduced discounting more than offset negative currency developments" | 45.9 / 45.3 / 41.8% |
| Greater China | 51.8% | 46.7% | 48.7% | 49.6% | 52.6% | 2022: "inventory write-offs, significantly higher discounting and higher supply chain costs"; 2025: "reduced discounting, lower sourcing costs, and a better business mix" | 49.6 / 51.0 / 45.7% |
| Asia-Pacific; then Japan/South Korea | 51.3% | 52.9% | 53.5% | 53.1% (JP/SK) | 52.6% (JP/SK) | 2025: "more than offset by unfavorable currency movements" | APLA 50.0 / 48.1 / 42.0% |
| Latin America | 48.2% | 47.5% | 45.6% | 47.9% | 47.5% | 2024: "more than offset significant negative currency developments" | |

**Common pre-shock base (my arithmetic, D6):**
- Europe/EMEA: adidas 2021 to 2025 +80 bps vs Nike FY22 to FY26 -410 bps (gap -490).
- Greater China: adidas +80 bps vs Nike -390 bps (gap -470).
- Latin America vs APLA: adidas -70 bps vs Nike -800 bps (not like-for-like; APLA includes Japan and Korea).

Revision 2 measured adidas from its 2022 trough (GC +590), which overstated the gap. The adidas 2021 EMEA and 2025 Europe segments differ in perimeter.

**Hedge and central-item comparability.**
- adidas reports "HQ/Consolidation" gross profit outside its segments: EUR 398M (2023), 506M (2024; 520M as restated in 2025) and 442M (2025). That is +186, +214 and +178 bps of group sales (2024 and 2025 segmental-information notes; my arithmetic).
- adidas's central functions include "central treasury, and global sourcing", whose results "are presented in the reconciliations" (adidas 2025 AR, segmental information).
- Nike's Corporate GP moved from -104 to +21 bps of company revenue over FY23 to FY26, a swing of about 125 bps. adidas's central GP moved by about 36 bps.
- So adidas segment margins were not depressed and then flattered by a central-FX swing of Nike's size in this window. I could not confirm whether adidas allocates hedge results to segments. The notes do not say.

**PUMA:** regional gross margin disclosed from 2025 only (2025 AR PDF pp. 42 to 43): Europe 47.8% to 46.3% (-150 bps), MEA&I -300, Latin America -230, Greater China 54.3% to 50.4% (-390), Rest of Asia-Pacific -160.

**Read-across (opinion):**
- adidas faced the same currencies and still expanded margins, so FX is not a sufficient explanation for Nike.
- adidas's drivers (lower sourcing costs, better mix, less discounting) partly reflect its recovery from its own 2022 trough. That is a brand-cycle and share effect, so the gap is not purely a Nike failure.
- PUMA's 2025 pattern (write-downs and promotions in a reset) matches Nike's. That points to company-specific inventory and brand problems, not an industry-wide margin collapse.
- Calendar years (adidas, PUMA) vs a May fiscal year (Nike) remain a mismatch.

### 2.10 FX magnitude: two tests against Nike's own numbers (revision 3; my arithmetic)

**Test 1: currency weights must reproduce Nike's reported translation effect.** For each segment, observed translation = (1 + reported growth) / (1 + currency-neutral growth) - 1, using reported dollars and Nike's currency-neutral % (rounded to 1 pt). Candidate weight grids (assumptions) are kept if the basket of actual average rates matches within the rounding band ±0.7 pt in FY24, FY25 and FY26. FY23 is shown but not used, because of TRY and ARS hyperinflation, the CASA exit and sharp intra-year moves.

| Segment | Observed translation FY24 / FY25 / FY26 | Weight sets kept | Revision 2 scenarios |
|---|---|---|---|
| EMEA | +0.9..+1.9 / -0.5..+0.6 / +5.2..+6.3% | 317 of 677 | "low" (85% EUR, no TRY) predicts +3.6% in FY24: **rejected**. "High" (incl. 3% TRY) fits |
| GC | -4.1..-3.2 / -1.4..-0.2 / +1.5..+2.6% | 12 of 12 (CNY 80 to 100%) | both fit |
| APLA | -0.8..+0.1 / -4.7..-3.7 / +0.4..+1.4% | 22,526 of 53,694; JPY 10 to 35%, KRW 10 to 25%, MXN 10 to 20%, USD-like 0 to 50% | both roughly fit; **the test does not pin down APLA weights** |
| Converse | +0.3..+1.5 / -1.5..-0.3 / +1.3..+2.8% | 187 of 216; USD-like 43 to 85% | both fit |

**Test 2: company-level reconciliation.** Segment standard-rate FX at company level is implied by: consolidated "net FX incl. hedges" minus the Corporate actual-vs-standard change divided by company revenue.

| | FY24 | FY25 | FY26 | Cumulative |
|---|---|---|---|---|
| Bridge net FX (bps; ±5 rounding) | -40 | -10 | +20 | -30 |
| Corporate FX change ($M) / company revenue ($M) | 588 / 51,362 = +114 | -88 / 46,309 = -19 | 147 / 46,398 = +32 | +127 |
| **Implied segment standard FX** | **-154** | **+9** | **-12** | **-157 (±15)** |
| Model, fitted weights, u = 0.85 to 1.0, no lag | -180 to -345 | +19 to -40 | -32 to -82 | -197 to -467 |
| Model, u = 0.75, no lag, least-exposed weights | -160 | +14 | -28 | -174 |

The model includes Canada at an assumed 4 to 8% of North America revenue. Sources: bridge lines FY24 10-K p. 36, FY25 10-K p. 35, FY26 10-K p. 34; Corporate FX FY24 10-K p. 44, FY25 10-K p. 43, FY26 10-K p. 42; revenues from the segment notes. Outputs: `gm/r3_recon_out.txt` (C1, C2), `gm/r3_recon_u_out.txt` (C6).

- **Result:** no scenario with u ≥ 0.70 fits all three years within ±15 bps. **55** scenarios fit with u = 0.55 to 0.65 (no lag). **2,639** fit within ±25 bps with u = 0.50 to 0.75.
- **Interpretation (opinion):** either a smaller share of segment cost of sales moves with standard rates than assumed, or my proxy overstates Nike's standard-rate moves, for example if Nike's rates are set closer to the season or with forward points. Both scale FX the same way, so the data cannot separate them. In both cases, revision 2's FX ranges were too large by about 1.4x to 2.4x in FY24 and FY26, as the reviewer found.
- **Caveats:**
  - The identity assumes the bridge FX line contains only standard-rate and Corporate FX effects. The line is rounded to 10 bps.
  - From FY25 the Converse bridge line absorbs Converse FX.
  - A uniform rescaling of all segments, rather than the scenario filter, gives similar ranges (EMEA -262 to -298, GC -184 to -321, APLA -204 to -336, Converse -17 to -126; `gm/r3_recon_out.txt` C3).

### 2.11 Bounds for alternative explanations (revision 3; my arithmetic, `gm/r3_alts_out.txt`)

**CASA transition in the APLA FY23 base (D1).**
- Inputs:
  - Q1 FY23 APLA revenue was $1,535M, and the transition "reduced APLA revenue growth by approximately 3 percentage points" in Q1 FY24 (Q1 FY24 10-Q p. 30). That is a revenue gap of about $46M.
  - The 6M FY24 10-Q (p. 35) and the FY24 10-K (p. 42) say it "did not have a material impact on APLA revenues". Q2 and Q3 FY24 bullets do not mention CASA.
- Model: owned sales replaced by distributor sales at 55 to 85% of the price, with the same units and owned GM of 45 to 50% (assumptions).
- Result: -146 to -161 bps in Q1 FY24, or **-34 to -38 bps of APLA FY24**.
- Data cap: Q1 FY24 APLA contracted 410 bps against 200 and 190 in Q2 and Q3 (Q2 FY24 10-Q p. 35; Q3 FY24 10-Q p. 37). Even if that whole excess (-215) were CASA, the FY24 effect is **-50 bps**.
- Nike's Q1 FY24 bullet attributes the -410 to "higher product costs, as well as unfavorable changes in standard foreign currency exchange rates and lower margin in NIKE Direct". **Verdict: 0 to -50 bps, FY24 only.**

**Converse FY26 tariffs (D2).**
- IEEPA: the $21M recovery is +179 bps of FY26 Converse revenue ($1,174M). Nike says the recovery offsets the IEEPA tariffs expensed in FY26, so the IEEPA cost is about -179 and the **net is about 0**.
- Replacement tariff after February 2026 (10% per Q4 FY26 remarks PDF p. 12): on Q4 COGS excluding the recovery (about $145M), with an assumed US share of 40 to 60% and 25 to 50% of Q4 COGS from post-February imports, the cost is **-12 to -37 bps** of FY26.
- The only FY26 Converse bullet citing product costs is Q2 ("lower ASP, reflecting higher discounts and higher product costs"). Q1 FY26 cites ASP and warehousing only. IEEPA cost in Q2 is plausible but is netted by the Q4 recovery within the fiscal year.

**EMEA FY26 severance in cost of sales (D3).** $154M company-wide in cost of sales (FY26 10-K p. 89). At EMEA shares of 10%, 33% and 100% (assumption), that is -12, -40 and -122 bps of EMEA FY26 GM. The FY26 EMEA bullet does not name severance, which points to the lower end.

**EMEA Q3 FY25 "higher other product costs" (D4).**
- Consolidated Q3 FY25: "Higher NIKE Brand product costs (decreasing gross margin approximately 70 basis points)" (Q3 FY25 10-Q p. 28).
- In Q3 FY25, North America cites lower product costs (9M), APLA and Converse cite lower product costs, and GC cites none. EMEA therefore carried at least the net: **at least -281 bps of EMEA Q3 GM, about -64 bps of EMEA FY25**.
- The cost is unnamed in the 10-Q and in the Q3 FY25 remarks ("product cost and channel mix headwinds", PDF p. 10). Q3 FY26 reverses it ("primarily due to higher other product costs in the prior year", Q3 FY26 10-Q p. 35), so **its cumulative FY23 to FY26 effect is zero**.

---

## 3. Verbatim quotes with sources

Nike filing URLs: https://investors.nike.com/sec-filings/all-sec-filings/content/<accession>/<file>.htm. Accessions (SEC submissions index, `dl/r3/nike/subs.json`):
- FY23 10-K: 0000320187-23-000039 / nke-20230531.htm
- Q1 FY24: 0000320187-23-000052 / nke-20230831.htm
- Q2 FY24: 0000320187-24-000004 / nke-20231130.htm
- Q3 FY24: 0000320187-24-000019 / nke-20240229.htm
- FY24 10-K: 0000320187-24-000044 / nke-20240531.htm
- Q1 FY25: 0000320187-24-000065 / nke-20240831.htm
- Q2 FY25: 0000320187-25-000004 / nke-20241130.htm
- Q3 FY25: 0000320187-25-000016 / nke-20250228.htm
- FY25 10-K: 0000320187-25-000047 / nke-20250531.htm
- Q1 FY26: 0000320187-25-000097 / nke-20250831.htm
- Q2 FY26: 0000320187-25-000151 / nke-20251130.htm
- Q3 FY26: 0000320187-26-000037 / nke-20260228.htm
- FY26 10-K: 0000320187-26-000088 / nke-20260531.htm
- Q1 FY27: 0000320187-26-000193 / nke-20260831.htm

**Standard-rate mechanism and Corporate (filing)**
- FY24 10-K p. 86: "standard foreign currency rates are assigned twice per year ... These rates are set approximately nine and twelve months in advance of the future selling seasons to which they relate ... Inventories and Cost of sales for geographic operating segments and Converse reflect the use of these standard rates to record non-functional currency product purchases in the entity's functional currency. Differences between assigned standard foreign currency rates and actual market rates are included in Corporate, together with foreign currency hedge gains and losses ..."
- FY23 10-K p. 42: "an unfavorable change of $352 million related to the difference between actual foreign currency exchange rates and standard foreign currency exchange rates assigned to the NIKE Brand geographic operating segments and Converse, net of hedge gains and losses; these results are reported as a component of consolidated gross margin"
- FY24 10-K p. 44: "a favorable change in net foreign currency gains and losses of $588 million related to the difference between actual foreign currency exchange rates and standard foreign currency exchange rates assigned to the NIKE Brand geographic operating segments and Converse, net of hedge gains and losses; these results are reported as a component of consolidated Gross profit"
- FY25 10-K p. 43: "an unfavorable change in net foreign currency gains and losses of $88 million related to the difference between actual foreign currency exchange rates and standard foreign currency exchange rates assigned to the NIKE Brand geographic operating segments and Converse, net of hedge gains and losses; these results are reported as a component of consolidated Gross profit." Corporate table, gross profit row: (31) FY25, (38) FY24, (535) FY23.
- FY26 10-K p. 42: "a favorable change in net foreign currency gains and losses of $147 million related to the difference between actual foreign currency exchange rates and standard foreign currency exchange rates assigned to the NIKE Brand geographic operating segments and Converse, net of hedge gains and losses; these results are reported as a component of consolidated Gross profit"

**EMEA (filing)**
- FY24 10-K p. 40: "Gross margin contraction of 110 basis points largely due to unfavorable changes in standard foreign currency exchange rates, partially offset by higher full-price ASP, net of discounts, primarily due to strategic pricing actions, as well as lower other costs and lower product costs, reflecting lower ocean freight rates and logistics costs."
- FY24 10-K p. 40: "Unit sales of apparel decreased 17%, while higher ASP per unit contributed approximately 11 percentage points of apparel revenue growth."
- Q2 FY25 10-Q p. 30: "Gross margin expansion of 100 basis points primarily due to favorable changes in standard foreign currency exchange rates, as well as lower warehousing and logistics costs."
- Q3 FY25 10-Q p. 33: "Gross margin contraction of 420 basis points primarily due to higher other product costs and lower ASP, partially offset by lower warehousing and logistics costs. Lower ASP primarily reflects changes in channel mix and higher discounts."
- Q3 FY25 10-Q p. 28: "Higher NIKE Brand product costs (decreasing gross margin approximately 70 basis points)"
- FY25 10-K p. 39: "Gross margin contraction of 100 basis points primarily due to lower ASP ... Lower ASP primarily reflects changes in channel mix and higher discounts, partially offset by strategic pricing actions."
- FY26 10-K p. 38: "Gross margin contraction of 140 basis points primarily due to lower ASP, reflecting higher discounts, and unfavorable changes in standard foreign currency exchange rates."
- Q3 FY26 10-Q p. 35: "Gross margin expansion of 100 basis points, primarily due to higher other product costs in the prior year, partially offset by higher discounts and unfavorable changes in standard foreign currency exchange rates."
- Q1 FY27 10-Q p. 27: "Gross margin expansion of 140 basis points primarily due to lower product costs and lower warehousing and logistics costs, partially offset by lower ASP."
- FY26 10-K p. 89: "$154 million were classified within Cost of sales on the Consolidated Statements of Income. The majority of these charges were classified within Global Brand Divisions, North America and EMEA."

**Greater China (filing)**
- FY24 10-K p. 41: "Gross margin contraction of approximately 80 basis points, primarily due to unfavorable changes in standard foreign currency exchange rates, partially offset by higher full-price ASP, net of discounts, and lower other costs."
- FY25 10-K p. 40: "Gross margin contraction of approximately 420 basis points, primarily due to unfavorable changes in standard foreign currency exchange rates and higher inventory obsolescence reserves, partially offset by higher ASP."
- Q3 FY25 10-Q p. 34: "Gross margin contraction of approximately 580 basis points, reflecting higher inventory obsolescence reserves and unfavorable changes in standard foreign currency exchange rates, partially offset by higher ASP."
- Q2 FY26 10-Q p. 33: "Gross margin contraction of 280 basis points, primarily due to higher inventory obsolescence reserves and higher product costs, driven by product mix, partially offset by higher ASP."
- Q3 FY26 10-Q p. 36: "Gross margin expansion of 300 basis points, primarily due to lower inventory obsolescence reserves."
- FY26 10-K p. 39: "Gross margin contraction of 30 basis points primarily due to unfavorable changes in standard foreign currency exchange rates."

**APLA and CASA (filing)**
- FY23 10-K p. 40: "We completed the sale of our entity in Chile and our entities in Argentina and Uruguay to third-party distributors in the first and second quarters of fiscal 2023, respectively. The impacts of closing these transactions are included within Corporate and are not reflected in the APLA operating segment results."
- Q1 FY24 10-Q p. 30: "Within our CASA territory, the transition of our Chile, Argentina and Uruguay entities to a third-party distributor operating model reduced APLA revenue growth by approximately 3 percentage points."
- Q1 FY24 10-Q p. 30: "Gross margin contraction of approximately 410 basis points primarily due to higher product costs, as well as unfavorable changes in standard foreign currency exchange rates and lower margin in NIKE Direct. This was partially offset by higher full-price ASP, net of discounts."
- FY24 10-K p. 42: "Within our CASA territory, the transition of our Chile, Argentina and Uruguay entities to a third-party distributor operating model did not have a material impact on APLA revenues."
- FY24 10-K p. 42: "Gross margin contraction of approximately 220 basis points primarily due to unfavorable changes in standard foreign currency exchange rates, lower margin in NIKE Direct and higher product costs, reflecting higher product input costs and product mix. This was partially offset by higher full-price ASP, net of discounts, primarily due to product mix and strategic pricing actions."
- FY25 10-K p. 41: "Gross margin contraction of approximately 190 basis points primarily due to unfavorable changes in standard foreign currency exchange rates, lower ASP and higher warehousing and logistics costs. Lower ASP reflects product mix, higher discounts and changes in channel mix, partially offset by strategic pricing actions."
- FY26 10-K p. 40: "Asia Pacific & Latin America revenues decreased 1% on a currency-neutral basis primarily due to lower revenues in Southeast Asia & India, Japan and Korea, partially offset by higher revenues in Central & South America and Pacific."
- FY26 10-K p. 40: "Gross margin contraction of 200 basis points primarily due to unfavorable changes in standard foreign currency exchange rates."
- Q1 FY27 10-Q p. 29: "Gross margin contraction of 150 basis points primarily due to lower ASP and unfavorable changes in standard foreign currency exchange rates."

**Converse and tariffs (filing; Nike release)**
- FY24 10-K p. 43: "Gross margin contraction of approximately 130 basis points due to unfavorable changes in standard foreign currency exchange rates, lower full-price ASP, net of discounts, higher other costs and lower margin in direct to consumer, partially offset by lower ocean freight rates."
- FY25 10-K p. 43: "Gross margin contraction of approximately 380 basis points due to lower ASP and higher warehousing and logistics costs, partially offset by lower product costs. Lower ASP primarily reflects higher discounts."
- Q1 FY26 10-Q p. 30: "Gross margin contraction of approximately 620 basis points, primarily due to lower ASP and higher warehousing and logistics costs. Lower ASP primarily reflects higher discounts and product mix."
- Q2 FY26 10-Q p. 36: "Gross margin contraction of approximately 700 basis points, primarily due to lower ASP, reflecting higher discounts and higher product costs."
- Q3 FY26 10-Q p. 40: "Gross margin contraction of approximately 970 basis points, primarily due to the brand and marketplace reset costs, including employee severance costs and higher inventory obsolescence reserves."
- FY26 10-K p. 42: "Gross margin contraction of 490 basis points primarily due to lower ASP, as well as the brand and marketplace reset costs, including higher inventory obsolescence reserves and employee severance costs. Lower ASP primarily reflects higher discounts and channel mix."
- FY26 10-K p. 30: "we recognized a benefit of $986 million in Cost of sales ... for the recovery of IEEPA tariffs paid, for which $965 million and $21 million of the benefit was classified within North America and Converse, respectively, largely offsetting the impact of the IEEPA tariffs recognized during fiscal 2026."
- Q3 FY26 10-Q p. 26: "Total IEEPA tariffs paid as of the date of this report is approximately $1.0 billion."
- Q4 FY26 remarks (Nike release), PDF pp. 8 to 9: "This resulted in the recognition of a one-time benefit of $986 million, ... offsetting the IEEPA tariffs embedded within cost of sales that had been expensed through the income statement throughout Fiscal 26."
- Q4 FY26 remarks, PDF p. 12: "Our forecast is based on incremental tariff rates of 10% continuing through the end of July, and then increasing to 15% thereafter, as we communicated last quarter"

**Consolidated (filing)**
- FY24 10-K p. 36: "Unfavorable changes in net foreign currency exchange rates, including hedges (decreasing gross margin approximately 40 basis points)"
- FY25 10-K p. 35: "Higher other costs (decreasing gross margin approximately 90 basis points), including higher inventory obsolescence reserves"; "Unfavorable changes in net foreign currency exchange rates, including hedges (decreasing gross margin approximately 10 basis points)."
- FY26 10-K p. 34: "Favorable changes in net foreign currency exchange rates, including hedges (increasing gross margin approximately 20 basis points); and"
- FY26 10-K p. 31 (definition): "Currency-neutral revenues are calculated using actual exchange rates in use during the comparative prior year period in place of the exchange rates in use during the current period."

**Nike call remarks (Nike release; s1.q4cdn.com/806093406/files/doc_financials/<year>/<qN>/NIKE-Inc-Q#FY##-UNOFFICIAL-Transcript.pdf; Q1 FY27 under /files/content_files/)**
- Q1 FY26, PDF p. 14 (CFO): "Foreign exchange has become a tailwind to reported revenue, but we expect minimal benefit to gross margin in Fiscal 26 due to our hedged positions entering the year."
- Q1 FY26, PDF p. 10: "EMEA has largely cleaned the marketplace, even as promotional activity has increased across the industry."
- Q3 FY25, PDF p. 10: "Gross margins declined 330 basis points to 41.5% on a reported basis, due to higher markdowns on Nike Direct, higher wholesale discounts, inventory obsolescence, and product cost and channel mix headwinds."
- Q4 FY25, PDF p. 12: "APLA delivered mixed results across countries, with further work required to clean up inventory."
- Q4 FY26, PDF p. 9: "Excluding this benefit, gross margin would have been 40.2%, down 10 basis points versus prior year, which included additional severance costs related to supply chain actions in North America and EMEA we highlighted last quarter."
- Q4 FY26, PDF pp. 10 to 11: "EMEA continues to work through heightened inventory and promotional levels, disruption in the Middle East, and a higher portfolio mix of Sportswear than the other geographies." ... "Total inventory dollars were up low double digits, with actions in place to reduce supply and accelerate liquidation to improve marketplace health"
- Q1 FY27, PDF p. 13: "in the second quarter, we are also lapping significant promotional activities in EMEA from Cyber Week and a higher comparison of North America sell-in activities versus last year."

**adidas (peer filing; https://report.adidas-group.com/<year>/en/group-management-report-financial-review/business-performance-by-segment/<segment>.html; segmental note https://report.adidas-group.com/<year>/en/consolidated-financial-statements/notes/additional-information/segmental-information.html)**
- EMEA 2022: "Gross margin in EMEA decreased 0.3 percentage points to 50.5% from 50.8% in 2021."
- Greater China 2022: "Gross margin in Greater China decreased by 5.1 percentage points to 46.7% from 51.8% in 2021. The negative impact from inventory write-offs, significantly higher discounting and higher supply chain costs could not be offset by positive currency and pricing effects."
- Asia-Pacific 2022: "Gross margin in Asia-Pacific increased 1.6 percentage points to 52.9% (2021: 51.3%), mainly driven by less promotional activity, a favorable currency development, and positive pricing effects."
- Latin America 2022: "Gross margin in Latin America decreased 0.7 percentage points to 47.5% (2021: 48.2%)."
- EMEA 2023: "Gross margin in EMEA decreased 4.1 percentage points to 46.4% from 50.5% in 2022. Unfavorable currency developments, significantly higher supply chain costs and the negative impact from higher discounting weighed on the margin development."
- Europe 2024: "Gross margin in Europe increased 4.3 percentage points to 50.3% from 45.9% in 2023. Lower sourcing costs, a better business mix, and reduced discounting more than offset negative currency developments."
- Europe 2025: "Gross margin in Europe increased 1.3 percentage points to 51.6% from 50.3% in 2024, mainly reflecting lower sourcing costs."
- Greater China 2025: "Gross margin in Greater China improved by 2.9 percentage points to 52.6% from 49.6% in 2024, reflecting reduced discounting, lower sourcing costs, and a better business mix."
- Japan/South Korea 2025: "Gross margin in Japan/South Korea decreased by 0.5 percentage points to 52.6% from 53.1% in 2024, as the positive effects from a better business mix and lower sourcing costs were more than offset by unfavorable currency movements."
- Segmental information 2025: "certain centralized corporate functions do not meet the definition of IFRS 8 for an operating segment. This includes, in particular, functions such as Global Brands and Global Sales (central brand and distribution management), central treasury, and global sourcing as well as other headquarter functions. Assets, liabilities, income, and expenses relating to these corporate functions are presented in the reconciliations." Gross profit reconciliation table (values, not prose): HQ/Consolidation 442 (2025) and 520 (2024 restated); 2024 note: 506 (2024) and 398 (2023), EUR millions.
- 2023 consolidated income statement (table values): net sales EUR 21,427M (2023) and 22,511M (2022); gross profit EUR 10,184M and 10,644M.

**PUMA (peer filing; 2025: https://www.annualreports.com/HostedData/AnnualReports/PDF/OTC_PMMAF_2025.pdf; 2024: https://www.annualreports.com/HostedData/AnnualReportArchive/p/OTC_PMMAF_2024.pdf)**
- 2025 AR PDF p. 37: "This margin development was mainly due to higher inventory write-downs and increased promotional activities in the wholesale business. In addition, there were negative currency effects on the gross profit margin, primarily from the Turkish lira as well as the Mexican and Argentine peso ..."
- 2025 AR PDF p. 42 (Europe): "the gross profit margin decreased by 150 basis points from 47.8% to 46.3%. This was attributable to higher inventory write-downs and increased promotional measures in retail."
- 2025 AR PDF p. 43 (Greater China): "the gross profit margin declining by 390 basis points from 54.3% to 50.4%. The material impact drivers here were costs for the clean-up as well as write-downs of inventories."
- 2024 AR PDF p. 35: "Headwinds from currencies and discounts were more than offset by a favourable product and distribution channel mix. The negative currency effects on the gross profit margin, including the effects of currency hedging, resulted primarily from the US dollar ..."

**FX data:** ECB reference rates, https://data-api.ecb.europa.eu/service/data/EXR/M.USD+CAD+HKD+CHF+PLN+SEK+ZAR+SGD+THB+PHP+IDR+MYR+NZD+CNY+JPY+KRW+GBP+AUD+MXN+INR+TRY.EUR.SP00.A?format=csvdata&startPeriod=2019-01 (downloaded Oct 13, 2026; USD cross rates are my arithmetic).

---

## 4. What remains unresolved, and what would resolve it

1. **Exact FX bps per segment.** It is now constrained by Nike's company-level FX, but the per-segment split still rests on reconstructed standard rates and weight grids. The data cannot separate "lower pass-through" from "proxy overstates standard-rate moves".
   - *Resolves it:* Nike's segment-level standard-rate impact in bps, or its actual standard rates (for example from Investor Day materials).
2. **APLA: FX vs everything else** (FX -208 to -430 central). The translation test allows USD-like weights from 0 to 50%.
   - *Resolves it:* APLA revenue by territory (Japan, Korea, SE Asia & India, Pacific, Mexico, CASA) and the invoicing currency of CASA distributors.
   - FY26 shows mix moving toward CASA (FY26 10-K p. 40), but its size is unknown.
3. **EMEA: how much of the FY24 residual is ASP mix vs cost.** The ASP measure mixes price, product mix and channel mix.
   - *Resolves it:* Nike's EMEA full-price ASP change in bps, or a regional gross margin bridge.
4. **Converse FY26 reset costs vs other product costs.** Nike gives no bps.
   - *Resolves it:* the Converse share of the $154M severance in cost of sales and of FY26 obsolescence reserves.
5. **EMEA Q3 FY25 "other product costs":** still unnamed (at least -281 bps that quarter), but it reversed in Q3 FY26 and does not affect the FY23 to FY26 comparison.
6. **Country mix in EMEA and GC** (Turkey and Middle East within EMEA; mainland China vs Hong Kong and Taiwan within GC): not disclosed. The translation test needs some exposure to weak currencies in EMEA (the 85% EUR, no TRY scenario is rejected).
7. **Peer comparability:** whether adidas allocates hedge results to segments (its notes do not say), and calendar-year vs May fiscal-year timing.

**Bottom line (opinion, grounded in the tables above):**
- **Greater China:** about half to three-quarters standard-rate FX on a yuan that went from about 6.4 to 7.2 per USD, plus FY2025 obsolescence.
- **EMEA:** about two-thirds FX, the rest net price and mix give-back after FY2024 pricing, with a small FY2026 contribution from inventory clean-up and severance.
- **APLA:** FX from the yen and won plus discounts, logistics, inventory clean-up, a small CASA effect and FY2026 territory mix. The split is unresolved within about 220 bps.
- **Converse:** discounting and reset costs. FX is small, and tariffs net to about zero within FY2026.
- The FY2023 starting point flatters the decline by about 190 to 235 bps for the three regions combined. From FY2022, the decline after Corporate is still about 400 bps.
- adidas did better from a common base by 470 to 490 bps in Europe and Greater China. That shows FX was not sufficient, but part of the gap is adidas's own recovery.

---

## Revision log

**Revision 3 (October 13, 2026)**, responding to two reviewer verdicts of "weakened":

1. **FX magnitude (reviewer 1, check 1; reviewer 2, alternative 5).** Confirmed the reviewer's arithmetic: implied company-level segment standard FX of -154, +9 and -12 bps. Added two tests (Section 2.10):
   - Currency weights must match Nike's reported translation effect. This rejects the old EMEA "low" scenario.
   - The company-level total must match Nike's implied FX in each year. This shows only an effective pass-through of 0.50 to 0.75 fits.
   - Replaced the FX ranges throughout. EMEA moves from -373/-659 to -227/-267 central.
   - Removed the claim that "FX alone would have cut margin by more than the observed 350 bps".
   - The non-FX residuals are now more negative, as the reviewer predicted.
2. **CASA ruled out (reviewer 1, check 2).** Downloaded the Q1 to Q3 FY24 10-Qs. The transition cut APLA Q1 FY24 revenue growth by about 3 pts and was immaterial after that. Bounded the APLA FY24 effect at 0 to -50 bps (Section 2.11). The verdict changes from "ruled out" to "partly supported, small".
3. **Converse tariffs (reviewer 1, check 3; reviewer 2, check 2 and alternative 4).** Found Nike's statements that the $986M recovery offsets IEEPA tariffs expensed during FY26 (FY26 10-K p. 30; Q4 FY26 remarks PDF pp. 8 to 9). IEEPA therefore nets to about zero within FY26.
   - Withdrew the wrong "-580 bps excluding recovery" figure.
   - Bounded the non-IEEPA replacement tariff at -12 to -37 bps.
   - Corrected the reviewer's premise: the Q1 FY26 Converse bullet does not cite product costs; only Q2 does.
4. **adidas base year (reviewer 2, check 1 and alternative 1).** Added adidas 2021 margins and Nike FY22 margins. The common-base gap is 470 to 490 bps, against the old GC comparison of -530 vs +590. Added adidas HQ/Consolidation gross profit (+178 to +214 bps of sales, stable) to address hedge and central-item comparability. Reworded the "Nike-specific failure" conclusion.
5. **"About half is an accounting split" (reviewer 1, alternative 6; reviewer 2, alternative 7).**
   - Added FY22-base and allocation-share sensitivity: 40 to 50% from FY23, 17 to 21% from FY22.
   - Reconciled FY24 Corporate (other items -$27M).
   - Reframed the offset as a timing effect, not avoided cost.
6. **EMEA Q3 FY25 "other product costs" (reviewer 1, alternative 4).** Bounded it at least -281 bps of the quarter using the consolidated -70 bps bridge line and the other segments' bullets. Showed that Q3 FY26 reverses it, so the cumulative effect is zero. Its nature remains unnamed.
7. **Order of decomposition (reviewer 2, alternative 3).** Stated that the log decomposition does not depend on order. Showed that the real ambiguity is ASP mix vs price in the EMEA FY24 residual, and gave the combined ASP-plus-residual reading.
8. **Inventory glut in EMEA (reviewer 2, alternative 6).** Changed from "ruled out" to "partly supported (FY26)" using the Q4 FY26 remarks. Added severance in cost of sales (FY26 10-K p. 89) as an EMEA and Converse FY26 driver with bounds.
9. **Country mix (both reviewers).** Added as explanation #15. APLA FY26 territory mix is partly supported from the FY26 10-K; EMEA and GC are unresolved. **Non-US duties** added as #16: no evidence in any filing.
10. **Quote fixes.** Ran `py_r3/qcheck.py` against all downloaded sources. Completed or ellipsized 13 quotes that stopped before the end of the sentence and dropped offsetting clauses: FY24 10-K p. 86, p. 44; Q3 FY25 EMEA; Q3 FY26 EMEA; GC FY24, Q3 FY25, Q2 FY26; APLA FY24, FY25; Converse FY24; FY26 10-K p. 30; FY26 bridge FX; Q1 FY27 call; PUMA 2025 p. 37 and 2024 p. 35. Corrected the FY23 Converse bullet summary ("lower other costs" was missing).

**Revision 2 and earlier:** see `region_gm_decline.rev2.bak.md` in the scratchpad (state before revision 3).

## Independent verification log
- Oct 13, 2026: Corporate gross profit confirmed: FY2023 "(535)" (FY2025 10-K, Corporate table) and FY2026 "97" (FY2026 10-K, Corporate table: "Gross profit (loss) | 97 | (31) | - | (38)"). The FX attribution ranges are model estimates and were not recomputed.
