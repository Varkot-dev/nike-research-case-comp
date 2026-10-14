# Dig 3: Greater China, "lost sell-through, not a channel choice"

Built 2026-10-14. Scope: the Pillar 2 claim taken from `research_notes/investigations/02_greater_china_decline.md` on branch `origin/claude/zealous-mccarthy-rj0t2h`:

> "units -25.7 of -26 pts, GC comps -12.6% against adidas in the same doors (Topsports and Pou Sheng HKEX filings), Nike-owned stores -14%, the $743M partner-online figure, and GC EBIT $2,309M to $1,278M in both 10-Ks."

Labels: **opened** = I opened the primary document in this session and read the line. **arithmetic** = my calculation, script `scratchpad/dig3/py/calc.py` (session scratchpad), reproduced below. **inherited** = taken from investigation 02 or 07 and not reopened here. No em-dashes.

---

## 1. Verdict in one paragraph

Every number checks out against the primary filings, with two wording problems and one framing problem. (1) "adidas in the same doors" is not in any filing: Topsports reports Nike and adidas only as one combined "principal brands" line, and Pou Sheng gives no brand split. What the filings do show is adidas Greater China growing +10.3%, +9% and +15% cn while Nike's own GC stores shrank, plus adidas reporting double-digit growth in both wholesale and its own stores in GC in Q4 2024. (2) "Units explain -25.7 of -26" is correct arithmetic, but units are units *shipped*, so they include Nike's deliberate sell-in cuts. The unit split rules out price as the driver; it cannot by itself prove "not a channel choice". (3) The honest finding is "mostly lost sell-through, with deliberate channel cuts on top", not "not a channel choice". Nike-owned store data (comps -7% and -6%, store sales -14%) are the clean sell-through evidence, and Topsports and Pou Sheng data show that a few points of each period are destock. Status: **confirmed with changes**.

---

## 2. Number-by-number check

| # | Claim | Primary source | Status | What the source says |
|---|---|---|---|---|
| 1 | GC Q1 FY27 -26% cn; footwear units -26%, ASP flat; apparel units -25%, ASP -2 pts | Q1 FY27 10-Q (nke-20260831), p. 28 | **opened, confirmed** | "Greater China revenues decreased 26% on a currency-neutral basis. Wholesale revenues decreased 31%. NIKE Direct revenues decreased 18% due to declines in digital sales of 28% and declines in store sales of 14%." "Unit sales of footwear decreased 26%, while ASP per pair was flat as lower discounts were offset primarily by channel mix." "Unit sales of apparel decreased 25%, while lower ASP per unit reduced apparel revenues by approximately 2 percentage points." |
| 2 | Units = -25.7 of -26 pts | arithmetic on #1 | **confirmed, wording fix** | With Q1 FY26 revenue weights (footwear 1,109, apparel 362, equipment 41; 10-Q p. 28): units -25.1, ASP -0.5, equipment (no unit split) -0.5, total -26.0. The -25.7 figure normalises out equipment. Say "units explain about 25 of the 26 points; price about half a point". |
| 3 | GC comps -12.6% compounded | FY25 10-K p. 40 ("Comparable store sales decreased 7%"); FY26 10-K p. 39 ("Comparable store sales decreased 6%") | **opened, confirmed** | 0.93 x 0.94 = 0.874, so -12.6% (arithmetic). Window Jun 2024 to May 2026. |
| 4 | "against adidas in the same doors (Topsports and Pou Sheng HKEX filings)" | Topsports annual results FY2025/26 (HKEX 2026052701005), revenue table; Pou Sheng monthly announcements | **opened, NOT supported as worded** | Topsports: "Principal brands include Nike and Adidas", one line, RMB 22,329.9m, -4.2% (FY ended 28 Feb 2026) and -6.1% the year before. No brand split exists. Pou Sheng monthly filings give only total revenue. adidas's own releases (opened): GC +10.3% cn in 2024, +9% cn in 2025, +15% cn in Q2 2026 ("reflecting continued strong market share gains"); Q4 2024 GC growth "reflecting double-digit improvements in the wholesale channel as well as the company's own retail stores". adidas +10.3% x +9% compounds to +20.2% (arithmetic). |
| 5 | Nike-owned stores -14% | Q1 FY27 10-Q p. 28 | **opened, confirmed, wording fix** | It is *store sales*, not comps. Nike did not disclose Q1 FY27 GC comps. Same quarter, other regions' store sales: NA -6%, EMEA -1% (10-Q p. 26 and 27, opened); APLA +5% (inherited). |
| 6 | ~$743M partner-online | Topsports inside information 22 Jul 2026 (HKEX 2026072200069); Pou Sheng business update 22 Jul 2026 (HKEX 2026072200197); Topsports FY2025/26 results | **opened for inputs; figure is an estimate** | Topsports: online Nike "approximately 22% of the total revenue of the Group for the financial year ended February 28, 2026", termination "with effect from January 1, 2027". Pou Sheng: "approximately 15% of the total revenue of the Group" for 2025, "while its contribution to the Group's profit was insignificant". Topsports revenue RMB 25,739.9m, GM 38.0% (opened). Pou Sheng 2025 revenue RMB 17,132.1m and GM 33.5% (inherited, Yue Yuen AR 2025). Retail value RMB 8,233m = US$1,171m at 7.0274; converted to Nike's wholesale value at partner cost ratios = **US$743m** (US$725m to US$756m at 7.2 to 6.9 CNY per USD). 12.7% of FY26 GC revenue. Not a Nike disclosure. |
| 7 | GC EBIT $2,309M to $1,278M "in both 10-Ks" | FY24 10-K (2,309); FY25 10-K (1,602 and 2,309); FY26 10-K p. 39 (1,278, 1,602, 2,309) | **opened, confirmed** | FY26 10-K GC table: "EARNINGS BEFORE INTEREST AND TAXES $ 1,278 $ 1,602 -20 % $ 2,309 -31 %". FY24 10-K: "Greater China 2,309 2,283". -1,031M, -44.7% (arithmetic). From FY23 (2,283) the fall is -1,005M, so the claim does not rest on an inflated FY24 base. |
| 8 | Pou Sheng Jun to Aug 2026 -10.4% (used in investigation 02 for the "same doors" test) | Pou Sheng monthly revenue announcements, HKEX 2026071000275, 2026081000336, 2026091000378, 2026101200300 | **opened (downloaded today), confirmed** | June 1,080,007 vs 1,181,264 (-8.6%); July 993,878 vs 1,154,119 (-13.9%); August 1,129,431 vs 1,241,261 (-9.0%); September 1,314,827 vs 1,347,982 (-2.5%). Jun to Aug combined -10.4% (arithmetic). |

---

## 3. EBIT bridge, FY24 to FY26 (filing figures, arithmetic)

FY26 10-K p. 39 GC table (opened): revenue 7,545 to 5,847; gross profit 3,784 to 2,670; total S&A 1,538 to 1,448; other segment items (63) to (56).

| Driver | US$m |
|---|---|
| Lost revenue at FY24 gross margin (50.15%) | -851.6 |
| Gross-margin rate (50.15% to 45.66%) | -262.4 |
| of which standard-rate FX (FY25 and FY26 central, inv. 07, inherited) | about -63 to -93 |
| Lower S&A | +90.0 |
| Other segment items | -7.0 |
| **Total** | **-1,031.0** |

Reading: about 83% of the profit loss is lost volume. FX is at most about 9%. Part of the gross-margin rate item is FY25 obsolescence reserves (inv. 07: FY25 residual about -276 to -319 bps), which is itself a symptom of unsold product.

---

## 4. Every alternative explanation, and where it stands

| # | Alternative | Evidence | Verdict |
|---|---|---|---|
| A | **Deliberate sell-in cuts and partner returns** (the channel choice) | FY26 10-K p. 39: wholesale -14% "reflecting our actions to prioritize marketplace health". Topsports principal brands -4.2% in FY25/26; with Nike 60% to 80% of that line and adidas between 0% and +13%, Nike sales at Topsports fell -5% to -16%, against Nike GC wholesale -14% (arithmetic). Pou Sheng Jun to Aug 2026 -10.4%: if Nike fell -31% there like Nike's sell-in, the rest of the store would need +10% to +38% growth while NBS sports goods fell -5.6%, which is implausible for Nike weights of 60% or more. So in Q1 FY27 Nike shipped less than partners sold. Inv. 02 sizes destock at about 1 to 6 pts of FY26 and about 1 to 10 pts (central about 4) of Q1 FY27 (inherited). | **Partly true. Real, but the smaller part.** It cannot explain Nike's own stores. Settles with: Nike-brand sales at Topsports or Pou Sheng (not disclosed), or Nike's GC partner inventory weeks. |
| B | **Units are shipped units, so "units -25" proves nothing about demand** | Correct as logic. | **Accepted.** The units line only rules out price. Use Nike-owned store data for the sell-through claim. |
| C | **Nike deliberately cut discounts in its own stores and traded volume for price** | If so, ASP would rise. Footwear ASP flat, apparel ASP -2 pts in Q1 FY27; FY26 footwear ASP -1, apparel +1 (10-Q p. 28, FY26 10-K p. 39, opened). | **Ruled out as a main driver.** No price gain appears. |
| D | **Nike closed its own stores, so store sales fall without demand falling** | FY25 store sales -6% vs comps -7%; FY26 -4% vs -6% (opened): comps were worse than total store sales, so footprint was not the cause. Nike's non-US NIKE Brand store count 604 (FY25) to 587 (FY26), -2.8% (FY25 and FY26 10-K Item 1, opened); GC not split. | **Ruled out for FY25 and FY26. Small open item for Q1 FY27,** because comps were not disclosed. Settles with: Q1 FY27 GC comps or the GC store count (ask at Investor Day). |
| E | **Deliberate digital pullback** (fewer promotions) | 11.11 down about 35% "in line with our plans" (Q2 FY26 call, inherited). GC digital -29% in FY26 vs about -10% elsewhere. | **Partly true** for digital. Does not touch store comps. |
| F | **Demand moved to partner online stores, not lost** | Topsports online Nike 22% of revenue, Pou Sheng 15% (opened). Topsports says online grew while "declining offline foot traffic" hurt (FY2025/26 results, opened). | **Partly true as a mechanism.** It changes the price Nike books, not the store comps. From 1 Jan 2027 this channel ends, so it becomes a forward risk, not a defence. |
| G | **China macro, not Nike** | Topsports blames "sluggish macro consumption environment and declining offline foot traffic" (opened, opinion). NBS sports goods -5.6% in Jun to Aug 2026 (inherited). But NBS apparel +0.3% (2024) and +3.2% (2025), and adidas GC +10.3%, +9%, +15% cn (opened). | **Partly true in mid-2026 only** (inv. 02: up to about 5 of Q1 FY27's 26 pts). Cannot explain FY25 to FY26 while adidas grew. |
| H | **adidas is just recovering from its 2022 collapse, so the contrast flatters the case** | adidas GC fell about 36% in 2022 and is still below 2021 in RMB (inherited). | **Partly true; weakens the adidas comparison, not the conclusion.** The NBS category and the six-brand set also grew while Nike fell (inherited: six-brand share 28.7% to 20.0%, 2023 to 2025). |
| I | **Nike-wide product cycle (Jordan, Dunk), not China** | FY25: rest of Nike -7.8% cn vs GC -12%, so about 65% shared. FY26: rest of Nike +1.4% vs GC -13%. Q1 FY27: rest -0.6% vs GC -26% (inherited, from 10-K region tables). | **True for FY25, ruled out for FY26 and Q1 FY27.** |
| J | **FX, not business** | Revenue: reported -22.5% vs cn -23.4% FY24 to FY26 (arithmetic), so translation helped slightly. Margin: standard-rate FX about -63 to -93m of the -1,031m (Section 3). | **Ruled out as the main driver;** at most about 9% of the EBIT fall. |
| K | **FY24 base was overshipped, so the fall is from a fake peak** | FY24 wholesale +15% vs comps +1% (inherited). But FY23 EBIT 2,283 vs FY24 2,309 (opened), and the cumulative FY24 to FY26 sell-in gap is only -0.4 to -5.0 pts (inherited). | **Ruled out for EBIT; small for revenue.** |
| L | **Hong Kong, Macau, Taiwan mix** | HK clothing and footwear -3.9% in 2025 (inherited, HK C&SD). | **Ruled out;** mainland is worse than the GC average. Taiwan not checked. |
| M | **The $743M is all lost** | It is gross partner online value converted to wholesale. Nike says it will anchor on its own Tmall, JD and Douyin flagships (Q1 FY27 call, opened), so some will be recaptured. Pou Sheng says the channel's profit contribution was "insignificant" (opened). Only Jan to May 2027 falls in FY27: about US$310m (arithmetic). Other partners' online sales are not included, so the gross figure could also be low. | **The number is fair as gross revenue at risk, not as net loss.** Settles with: Nike's GC digital growth in Q3 and Q4 FY27. |

What management says (opened, Q1 FY27 call transcript): CFO Dave Denton, "the guidance range ... assumes that China actually gets worse from a revenue perspective for the balance of this year, and that's because of some of the actions we're taking". The bull will use this line to argue the next leg is deliberate. Our answer is alternatives C and D: Nike's own stores fell 14% with no price gain, and nothing in Nike's actions explains that.

---

## 5. Corrected wording for Pillar 2 (China sentence)

> Greater China is mostly lost demand, with deliberate cuts on top. In Nike's own stores, where there is no wholesale shipping to cut, comparable sales fell 7% and then 6% (FY25 and FY26 10-K), and store sales fell 14% in Q1 FY27 against -6% in North America and -1% in EMEA (Q1 FY27 10-Q p. 28). Over the same period adidas grew in Greater China by 10%, 9% and 15% (currency-neutral; adidas releases). Price is not the cause: units explain about 25 of the 26-point drop. Partner data (Topsports, Pou Sheng) put deliberate destocking at only a few points. From 1 January 2027, Nike ends partner online sales that we estimate at about US$743M a year at wholesale value (from Topsports and Pou Sheng HKEX filings), before any recapture. GC EBIT fell from US$2,309M to US$1,278M (FY26 10-K p. 39), and about 83% of that is lost volume.

Drop: "adidas grew in the same Topsports doors" (not in any filing) and "not a channel choice" (overstated).

---

## 6. What would settle the remaining doubt

1. Q1 FY27 GC comparable store sales, or the GC store count (Investor Day, Nov 16 to 17, or the Q2 FY27 10-Q around Dec 17).
2. Topsports Q2 FY2026/27 operational update (Jun to Aug 2026; not yet published as of Oct 13, inherited). It gives a second exactly matched window.
3. Nike GC digital growth in Q3 and Q4 FY27, which shows how much of the US$743M Nike's own flagships recapture.
4. adidas Q3 2026 results (early November): a GC slowdown would move weight toward alternative G (macro).
