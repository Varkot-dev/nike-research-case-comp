# Why did Nike Greater China collapse? (FY2021 to Q1 FY2027)

> **Status: DRAFT (Oct 13, 2026).** Produced by the multi-agent investigation (one investigator, two adversarial reviewers, one revision round). Sources are cited inline; independent spot-check against source documents is in progress and results will be logged at the end of this file. Treat figures as provisional until marked verified.


Scratch research note, built 2026-10-13, revision 2 the same day (see Section 7, Revision log). Not yet merged into the repo. Every number carries a label:
**filing** (SEC filing, or an HKEX filing or annual report of the company), **Nike release** (Nike earnings call remarks or release), **company release** (a peer's own press release), **official statistics** (NBS, Hong Kong C&SD), **secondary** (press or data aggregator), **snippet only** (search-engine summary, not usable as evidence), **my arithmetic** (computed in `scratchpad/rh/scripts/gc_calc.py`, output `scratchpad/rh/gc_calc_out.txt`, and in `scratchpad/rh/scripts/gc_calc_rev2.py`, output `scratchpad/rh/gc_calc_rev2_out.txt`), **assumption** (an input I chose, shown as a range), **opinion** (a management or analyst view quoted verbatim, never used as the explanation on its own).

Fiscal calendars differ. Nike's FY ends May 31 (FY2026 = Jun 2025 to May 2026). Peers report calendar years, except Topsports, whose FY ends at the end of February. When I compare, Nike FY(Y+1) is paired with calendar year Y (7 of 12 months overlap). Where possible, revision 2 also uses **exactly matched windows**: Topsports Mar to May 2026 against Nike Q4 FY26, and Pou Sheng Jun to Aug 2026 against Nike Q1 FY27. RMB conversions of Nike and adidas use period-average ECB reference rates (USD/CNY = CNY per EUR divided by USD per EUR, monthly averages from `data-api.ecb.europa.eu`, series EXR.M.CNY.EUR.SP00.A and EXR.M.USD.EUR.SP00.A).

---

## 0. Bottom line

1. **The revenue decline is a volume decline, not a price decline.** Weighted by Nike's unit and ASP disclosures, units explain about -12.6 of FY2025's -12 points and -12.4 of FY2026's -13 points (currency-neutral). ASP explains -0.2 and -0.5 points. In Q1 FY2027 units explain -25.7 of -26 points (my arithmetic from FY25 10-K p. 40, FY26 10-K p. 39, Q1 FY27 10-Q p. 28).
2. **FY2025 was mostly a Nike-wide problem; FY2026 and Q1 FY2027 are China-specific.** Benchmarked against Nike's other three regions (weighted by revenue), the rest of Nike fell -7.8% cn in FY2025, so about 65% of GC's -12% was shared with the rest of Nike (the Jordan and classics cycle, the digital collapse). The rest of Nike grew +1.4% in FY2026 and fell -0.6% in Q1 FY2027, so almost all of GC's -13% and -26% is specific to China (my arithmetic from the FY25 and FY26 10-K and Q1 FY27 10-Q region sections; Section 2.8).
3. **The core of it is weaker consumer sell-through, and it is visible in the cleanest sell-through measure.** Nike's own GC comparable store sales compound to -12.6% over FY2025 and FY2026. Comps contain no sell-in, so the destock question does not affect them, and Nike's own stores are the refreshed ones (the old-door argument does not apply). Over the matching window the NBS apparel category grew +3.5% (2023 to 2025), adidas Greater China +20.3% and the other five tracked brands +21.4% (official statistics, filings, my arithmetic). Removing the wholesale sell-in gap from GC revenue gives a "sell-in-neutral" decline of -11.9% to -15.9% from FY2023 to FY2026, against +30.6% for adidas and +16.9% for the NBS category over 2022 to 2025 (my arithmetic; Section 2.4). That is share loss in sell-through.
4. **Channel mechanics then amplified the timing and the size:**
   (a) **A sell-in round trip.** FY2024 wholesale grew +15% while comps grew +1%, and Q1 FY2025 wholesale grew +10% while comps fell -8% (filings). That overshipment unwound in FY2025 and FY2026. Summed over FY2024 to FY2026, the wholesale sell-in gap nets to only -0.4 points (comps benchmark) to -5.0 points (store-sales benchmark) (my arithmetic). So most of the FY2024 to FY2026 "destock" is the reversal of an FY2024 overshoot. It explains the timing of the FY2025 to FY2026 drop, not its level.
   (b) **A deliberate clean-up**, which grows into Q1 FY2027: sell-in cuts, accelerated partner returns, less promotion on Nike Digital, and the termination of all partner online sales of Nike in mainland China from 1 January 2027 (Topsports and Pou Sheng filings, 22 Jul 2026).
   (c) **Migration of online demand from Nike Digital to partner-run platform stores.** In FY2025/26, Topsports' online sales of Nike were about 22% of its revenue, and Pou Sheng's were about 15% of its 2025 revenue (filings). That is about US$1.17bn at retail, against my estimate of about US$0.66bn for Nike's own GC Digital in FY2026 (my arithmetic). Online demand that moved to partner stores is booked by Nike as wholesale at a lower price. Depending on how much of Nike Digital's roughly US$575m decline from FY2024 to FY2026 moved this way, the net revenue effect is -2.9 to -7.6 points of FY2024 GC revenue (my arithmetic, assumption-based).
5. **Margin: volume plus deleverage.** EBIT fell US$1,031m from FY2024 to FY2026: volume at the FY2024 gross margin -851.6, gross-margin rate -262.4, SG&A +90.0, other segment items -7.0. The bridge closes exactly (my arithmetic, corrected in revision 2). EBIT margin fell -8.75pp = GM -4.49pp, SG&A -4.38pp, other +0.12pp. Over the same years the other regions lost less margin: EMEA -5.7pp, APLA -5.8pp, NA -1.0pp (my arithmetic from repo `data/nike_region_profitability.csv`).
6. **Ruled out as drivers of the FY2025 to FY2027 decline:**
   - **The 2021 boycott, and a slow-burn "guochao" (domestic-brand) shift.** In 2025 the domestic incumbents grew more slowly than adidas: Li Ning +3.2%, ANTA brand +3.7%, Xtep core mass brand +1.5%, against adidas +9% cn. In Q2 2026 Li Ning sell-through fell low single digits and Xtep core fell mid single digits, against adidas Greater China +15% cn (filings, company release). The share went to premium and specialist brands, many of them foreign (FILA, Anta's "other brands" Descente and Kolon +25% to 30% in Q2 2026, Saucony, Amer, On), not to domestic mass brands.
   - **Price cuts as a revenue driver.**
   - **Hong Kong, Macau and Taiwan mix.** HK clothing and footwear sales fell only -3.9% in value in 2025 (official statistics), so any HK and Taiwan share makes the mainland decline worse than the GC average, not better.
   - **A total consumption collapse.** The category grew through 2025.

   **Price increases as an elasticity cause:** at most about -1.9 points of FY2025, confined to apparel (my arithmetic), and absent in FY2026 and Q1 FY2027.

   **Macro:** partly supported, mainly for mid-2026. NBS sports goods fell -5.6% in Jun to Aug 2026, Pou Sheng's revenue fell -10.4% in the same window, and Li Ning and Xtep sell-through turned negative in Q2 2026.
7. **What survives.** One explanation is necessary for every period and is not removed by any channel adjustment: **Nike lost consumer sell-through share in China**. It shows in comps -12.6% while the category and adidas grew. The cause was the Sportswear and Jordan franchise cycle (Nike-wide in FY2025) plus China-specific weakness from FY2026 that reaches Nike-owned stores by Q1 FY2027 (store sales -14% vs about -1% elsewhere).

   Three mechanisms sit on top of it and set the timing and the depth of the reported revenue. They are not rival explanations: the FY2024 overshoot and its unwind, deliberate clean-up, and the move of online demand to partner platforms.

   **Not identified:** the split among these three mechanisms in Q1 FY2027. Partner sell-through of Nike in Jun to Aug 2026 is implied at -18% to -30% from Pou Sheng's filings, which leaves destock at about 1 to 8 points rather than the 10 points the Nike-store proxy gives. Resolving the split needs Nike-brand sales at Topsports and Pou Sheng, and Nike's GMV on Tmall, JD and Douyin (Section 5).

---

## 1. Verdict table: every candidate explanation

| # | Candidate | Verdict | Quantified contribution | Evidence that decided it |
|---|---|---|---|---|
| 1 | **Share loss in consumer sell-through** (Nike-specific weakness against the category and peers) | **Supported. The only explanation needed in every period.** | Comps FY25 and FY26 compounded -12.6% against category +3.5% and adidas +20.3%. Sell-in-neutral GC revenue FY23 to FY26 -11.9% to -15.9%, against adidas +30.6%, the other five brands +36.6% (incl. Anta acquisitions) and NBS +16.9% over 2022 to 2025. Six-brand share 28.7% (2023) to 20.0% (2025) (my arithmetic) | Section 2.4 and 2.3; Nike comps (filings); NBS; peer filings. In FY26 GC comps (-6) were close to EMEA's (-7), so in FY26 the China-specific excess sat in wholesale and digital. By Q1 FY27 it reached Nike stores too (-14 vs NA -6, EMEA -1, APLA +5) |
| 2 | **Nike-wide product and franchise cycle** (Jordan, Dunk and other classics; global digital decline) | **Supported for FY25 (about 65% of GC's decline). Ruled out as the explanation for FY26 and Q1 FY27** | FY25: ex-GC Nike -7.8% cn against GC -12%, so the China-specific excess is -4.2 pts. FY26: ex-GC +1.4% against GC -13% (excess -14.4). Q1 FY27: ex-GC -0.6% against GC -26% (excess -25.4) (my arithmetic) | FY25 10-K pp. 38 to 41: every region names the Jordan Brand among the decliners; FY25 GC footwear -13% = NA footwear -13%. FY26 10-K pp. 37 to 40; Q1 FY27 10-Q pp. 26 to 29 |
| 3 | **FY24 sell-in overshoot and its unwind** (base effect) | **Supported. Explains timing, not level** | FY24 gap +4.6 (stores) to +7.5 pts (comps); Q1 FY25 wholesale +10% vs comps -8%. Cumulative FY24 to FY26 gap -0.4 to -5.0 pts (my arithmetic) | FY24 10-K p. 41; Q1 FY25 10-Q p. 26; Q4 FY24 call PDF p. 12 (Tmall 6.18 pull-forward: "Excluding this timing benefit, we fell short of our plan"); Q1 FY25 call PDF p. 9 ("elevated inventory in the marketplace") |
| 4 | **Deliberate wholesale sell-in cuts and partner returns** (clean-up) | **Supported. Size depends on the benchmark** | Nike-store benchmark: -4.0 (FY25), -5.6 (FY26), -10.0 (Q1 FY27). Comps benchmark: -3.4, -4.5. Topsports purchases test: about -1.5 pts of Topsports' Nike buying in FY25/26. Pou Sheng matched window: -0.7 to -7.8 pts in Q1 FY27 (my arithmetic, assumption-based) | FY26 10-K p. 39 "reflecting our actions to prioritize marketplace health"; Q2 FY26 call PDF p. 11 returns and buy cuts; Q3 FY26 call PDF p. 12 "partner inventory also declined double-digits". Returns and sales-related reserves sit inside this gap and cannot be separated from lower shipments |
| 5 | **Migration of online demand to partner-run platform stores** (Topsports and Pou Sheng Tmall, Douyin and mini-program stores; booked by Nike as wholesale) | **Supported as a mechanism. Size not identified** | Partner online Nike sales about US$1,171m at retail (FY25/26 Topsports, 2025 Pou Sheng), about US$743m at wholesale value (12.7% of FY26 GC revenue), against Nike's own GC Digital of about US$656m. Net effect of the Nike Digital decline: -7.6 pts (no migration) to -2.9 pts (full migration) of FY24 GC (my arithmetic, assumption-based) | Topsports inside information 22 Jul 2026 ("approximately 22%"); Pou Sheng business update 22 Jul 2026 ("approximately 15%"); Topsports online mix "low-twenties" (FY22/23) to "mid-30%" (FY24/25), "higher proportion" (FY25/26); Q1 FY26 call PDF p. 11 "consumer shopping moments extending longer on local platforms with deeper discounts" (opinion) |
| 6 | **Nike Digital decline and deliberate promotion cuts** | **Supported. Partly Nike-wide, partly China-specific, partly migration (row 5)** | About -3.6 (FY25) and -4.1 (FY26) pts of GC. FY25 GC digital -22 vs NA -19, EMEA -30 (Nike-wide); FY26 -29 vs -10, -10, -9 (China-specific) (my arithmetic) | Region sections of the 10-Ks; 11.11 "approximate 35% decline ... in line with our plans" (Q2 FY26 call PDF p. 11) |
| 7 | **Category mix: Sportswear and Jordan, including deliberate franchise supply cuts** | **Supported as the mechanism of rows 1 and 2. Deliberate and demand-driven parts both present** | Not disclosed for GC. Globally the Dunk was cut "by nearly 50%" in Q1 FY27 (about US$200m). The aged-inventory write-offs (FY25, Q2 FY26) show that sell-through fell short of plan, which deliberate cuts do not produce | Q1 FY27 call PDF p. 3 ("deliberate actions, product underperformance and broader marketplace pressure"); PDF p. 4 ("we've been oversupplying our iconic retro product"); Q2 FY26 call PDF p. 8 obsolescence "not contemplated ninety days ago"; Q3 FY25 call PDF p. 13 "retail sales underperformed our plan" |
| 8 | **Price increases (elasticity) against cheaper domestic brands** | **Partly supported, small and confined to FY25 apparel** | Upper bound -1.9 pts of FY25 GC (apparel revenue excess over the other regions x apparel weight 0.242). Footwear (74% of GC) had no ASP increase (-2 pts) and fell like NA (-13%). FY26 apparel ASP +1 from "product mix"; Q1 FY27 ASP flat to -2 with "lower discounts" (my arithmetic) | FY25 10-K p. 40 (GC apparel units -17%, ASP +5 "strategic pricing actions"), against APLA apparel units -3% with ASP +2 from the same "strategic pricing actions" (p. 41) |
| 9 | **Price cuts and discounting as a revenue driver** | **Ruled out for revenue; supported for margin** | ASP -0.2, -0.5, -0.6 pts. GM: FY25 -420 bps, Q2 FY26 -280 bps | Section 2.2; Topsports GM 41.8% to 38.4% in FY24/25 (partner discounting concentrated in Nike's FY25) |
| 10 | **Slow-burn guochao or nationalism shift** (not the acute boycott) | **Ruled out as a driver of FY25 to Q1 FY27; consistent with the 2021 to 2022 level shift only** | adidas share 12.9% to 14.3% (2023 to 2025) while Nike lost 8.7 pts. The large domestic incumbents (Li Ning, ANTA brand, Xtep) grew more slowly than adidas in 2025 and H1 2026; 361 is the exception in 2025 | Both Western brands are about -16% in RMB from 2021 to 2025 (adidas -16.2%, Nike FY22 to FY26 -15.4%), but all of adidas's loss is in 2022 (-35.9%), followed by +8.6%, +10.2% and +9.2%, then +15% cn in Q2 2026. Li Ning 2025 +3.2%, Q2 2026 sell-through LSD decline; Xtep core H1 2026 revenue -2.2% (filings) |
| 11 | **Acute 2021 Xinjiang boycott** | **Ruled out for FY25 to FY27; plausible for FY22, not separable from COVID** | About 0 for FY25 to FY27 | As in row 10; FY22 10-K p. 39 |
| 12 | **Macro consumption slowdown** | **Partly supported: about 0 in FY25 to FY26, meaningful in mid-2026** | Category +0.3% (2024), +3.2% (2025). Jun to Aug 2026: NBS sports goods -5.6%, Pou Sheng -10.4%. Up to about 5 of Q1 FY27's 26 points | NBS; Pou Sheng monthly filings; Li Ning and Xtep Q2 2026 updates |
| 13 | **Collapse of the sneaker resale and hype cycle** | **Unresolved in size. Folded into rows 2 and 7** | No resale-price data found (only secondary or anecdotal sources). Jordan is named among the decliners in all four regions in FY25, so it is not China-specific, and Nike says it oversupplied the retros, so the hype loss is partly caused by Nike's own supply | FY25 10-K pp. 38 to 41; Q1 FY27 call PDF p. 4 |
| 14 | **Hong Kong, Macau and Taiwan mix** | **Ruled out as a cause of the GC decline** | If HK, Macau and Taiwan were 10% to 30% of GC and fell 3.9% to 10%, the mainland fell -13.3% to -16.9% in FY26 (my arithmetic) | HK C&SD Dec 2025 retail release: clothing and footwear value -3.9% in 2025, footwear -6.5% (official statistics). Taiwan not checked |
| 15 | **COVID lockdowns** | **Supported for FY22 only** | FY22 -13% cn | FY22 10-K p. 39 |
| 16 | **FX translation** | **USD headline only; partly margin** | Translation about -5.7% over FY21 to FY26 | As revision 1 |
| 17 | **Premium challengers** (Amer, On, Anta other brands, Saucony) | **Supported as the destination of the lost share** | Anta "all other brands" Q2 2026 sell-through +25% to 30%; Saucony H1 2026 +LDD sell-through; Amer GC +43.4% in 2025 (secondary) | Anta and Xtep Q2 2026 updates (filings) |
| 18 | **Partner door closures** | **Supported as a channel mechanism (overlaps rows 4 and 12)** | Topsports stores -43.3%, gross selling area -26.9% (Feb 2022 to Feb 2026); offline revenue about -17% over FY22/23 to FY24/25 while online grew about +59% (my arithmetic, approximate mixes) | Topsports ARs |

---

## 2. Data tables

### 2.1 Nike Greater China, annual (USD m; filings)

| FY | Revenue | Wholesale | Direct | cn growth | EBIT | EBIT margin (my arithmetic) | Gross margin | Inventory at May 31 |
|---|---|---|---|---|---|---|---|---|
| 2021 | 8,290 | 4,513 | 3,777 | +19% | 3,243 | 39.1% | about 53.5% (my arithmetic, from bps changes) | 1,247 |
| 2022 | 7,547 | 4,081 | 3,466 | -13% | 2,365 | 31.3% | about 49.6% (my arithmetic) | 1,044 |
| 2023 | 7,248 | 3,866 | 3,382 | +4% | 2,283 | 31.5% | 51.0% | 973 |
| 2024 | 7,545 | 4,262 | 3,283 | +8% | 2,309 | 30.6% | 50.2% | 1,070 |
| 2025 | 6,586 | 3,699 | 2,887 | -12% | 1,602 | 24.3% | 46.0% | 951 |
| 2026 | 5,847 | 3,255 | 2,592 | -13% | 1,278 | 21.9% | 45.7% | 793 |
| Q1 FY27 | 1,180 | 644 | 536 | -26% | 248 | 21.0% (Q1 FY26 24.9%) | 47.5% | 853 (Aug 31) |

Sources: FY21 10-K p. 39; FY22 10-K p. 39; FY23 10-K p. 39; FY24 10-K p. 41; FY25 10-K p. 40 (GM, cost lines) and pp. 85 to 86 (inventory); FY26 10-K pp. 39 and 86; Q1 FY27 10-Q pp. 28 and 17. The FY21 and FY22 gross margins are derived from Nike's bps changes: FY23 "+140 bps" and FY22 "approximately 390 basis points" (labelled approximate).

Currency-neutral index (FY2021 = 100, my arithmetic): FY22 87.0, FY23 90.5, FY24 97.7, FY25 86.0, FY26 74.8. RMB-equivalent revenue (my arithmetic): FY21 55,329; FY24 54,458; FY26 41,089 (RMB m).

### 2.2 Units vs ASP (currency-neutral; filings, weights my arithmetic)

| Period | Footwear units | Footwear ASP | Apparel units | Apparel ASP | Weighted units (pts) | Weighted ASP (pts) | Source |
|---|---|---|---|---|---|---|---|
| FY22 | -7% | -3 pts | -15% | -6 pts | -9.5 | -3.9 | FY22 10-K p. 39 |
| FY23 | +7% | +1 pt | -8% | +1 pt | +2.8 | +1.0 | FY23 10-K p. 39 |
| FY24 | +8% | -2 pts | +7% | +7 pts | +7.7 | +0.3 | FY24 10-K p. 41 |
| FY25 | -11% | -2 pts | -17% | +5 pts | -12.6 | -0.2 | FY25 10-K p. 40 |
| FY26 | -14% | -1 pt | -8% | +1 pt | -12.4 | -0.5 | FY26 10-K p. 39 |
| Q1 FY27 | -26% | flat | -25% | -2 pts | -25.7 | -0.6 | Q1 FY27 10-Q p. 28 |

Weights are the prior-period footwear share of GC revenue; equipment is ignored. Q1 FY27 uses the FY26 annual mix.

**Price-elasticity test (revision 2).** Flat ASP does not rule out price increases as a cause of lower volume, so I compare GC with the other regions in FY2025, the year Nike cites "strategic pricing actions" (filings, my arithmetic):

| FY25 | Footwear revenue (units, ASP) | Apparel revenue (units, ASP) |
|---|---|---|
| NA | -13 (-10, -3) | -2 (-1, -1) |
| EMEA | -10 (-8, -2) | -9 (-6, -3) |
| GC | -13 (-11, -2) | -12 (-17, +5) |
| APLA | -4 (-2, -2) | -1 (-3, +2) |

- GC had the largest apparel price increase and the largest apparel unit fall. APLA cites the same "strategic pricing actions" with ASP +2 and units only -3. This is consistent with elasticity in apparel. Its upper bound is the GC apparel revenue excess over the ex-GC mean (-8.0 pts) times the apparel weight (0.242), which is **-1.9 pts of FY25 GC** (my arithmetic).
- Footwear (74% of GC) had lower ASP (-2), not higher, and fell exactly as much as in North America (-13). Price increases cannot explain the footwear volume loss.
- FY26 GC apparel ASP +1 is attributed to "product mix", not pricing. Q1 FY27 footwear ASP was flat "as lower discounts were offset primarily by channel mix" (filings). The elasticity mechanism has no support after FY25.

Sources: FY25 10-K p. 38 (NA), p. 39 (EMEA), p. 40 (GC), p. 41 (APLA).

### 2.3 China revenue of Nike vs peers (RMB m; filings unless labelled; conversions my arithmetic)

| Year (Nike FY in brackets) | Nike GC (RMB-equiv) | adidas GC (RMB-equiv) | Anta group | of which ANTA brand | of which FILA | Li Ning | Xtep (continuing) | 361 Degrees |
|---|---|---|---|---|---|---|---|---|
| 2019 (FY20) | 46,872 | n/a (adidas reported Asia-Pacific) | 33,928 | 17,450 | 14,770 | 13,870 | n/a | n/a |
| 2020 (FY21) | 55,329 | 34,175 | 35,512 | 15,749 | 17,450 | 14,457 | n/a | n/a |
| 2021 (FY22) | 48,544 | 35,094 | 49,328 | 24,012 | 21,822 | 22,572 | 9,042 | 5,933 |
| 2022 (FY23) | 50,127 | 22,508 | 53,651 | 27,723 | 21,523 | 25,803 | 11,528 | 6,961 |
| 2023 (FY24) | 54,458 | 24,432 | 62,356 | 30,306 | 25,103 | 27,598 | 12,743 | 8,423 |
| 2024 (FY25) | 47,559 | 26,933 | 70,826 | 33,522 | 26,626 | 28,676 | 13,577 | 10,074 |
| 2025 (FY26) | 41,089 | 29,400 | 80,219 | 34,754 | 28,469 | 29,598 | 14,151 | 11,146 |
| H1 2026 | Q1 FY27 -26% cn | +16% cn (company release) | 43,507 (+12.9%) | 17,771 (+4.8%) | 15,045 (+6.1%) | 15,235 (+2.8%) | 6,794.9; core Xtep brand 5,919.9 (-2.2%) | not collected |

Caveats: Anta group includes some non-China revenue (Jack Wolfskin from mid-2025, and overseas), so it overstates China. Xtep 2021 to 2025 is on the restated continuing-operations basis. adidas and Nike Greater China include Hong Kong, Macau and Taiwan. H1 2026 Li Ning and Xtep: interim results announcements, PDF p. 1 (filings, new in revision 2).

**Share of the six-brand tracked set (my arithmetic):**

| Year | Nike | adidas | Anta group | Li Ning | Xtep | 361 | Set total (RMB m) |
|---|---|---|---|---|---|---|---|
| 2021 | 28.5% | 20.6% | 28.9% | 13.2% | 5.3% | 3.5% | 170,514 |
| 2022 | 29.4% | 13.2% | 31.5% | 15.1% | 6.8% | 4.1% | 170,578 |
| 2023 | 28.7% | 12.9% | 32.8% | 14.5% | 6.7% | 4.4% | 190,011 |
| 2024 | 24.1% | 13.6% | 35.8% | 14.5% | 6.9% | 5.1% | 197,644 |
| 2025 | 20.0% | 14.3% | 39.0% | 14.4% | 6.9% | 5.4% | 205,604 |

Readings (my arithmetic):
- The 2022 hit was shared: adidas -36% in RMB, Nike -13% cn (FY22). adidas lost 7.4 share points that year, Nike none.
- From 2023 to 2025 Nike lost 8.7 points, Anta gained 6.2, adidas 1.4, 361 1.0 and Xtep 0.2, while Li Ning lost 0.1.
- **The guochao test (revision 2).** Both Western brands are below their 2021 level: adidas -16.2% (2021 to 2025) and Nike -15.4% (FY22 to FY26); combined -15.7%. All of adidas's loss came in 2022, and it has grown every year since (+8.6%, +10.2%, +9.2% in RMB, then +15% cn in Q2 2026). Over 2023 to 2025 adidas (+20.3%) outgrew Li Ning (+7.2%), the ANTA brand (+14.7%), FILA (+13.4%) and the Xtep group (+11.0%); only 361 Degrees (+32.3%) grew faster. In 2025 it outgrew Li Ning, the ANTA brand and Xtep (361 Degrees, +10.6%, was slightly faster than adidas's +9.2% in RMB). In Q2 2026 it outgrew every domestic brand that discloses sell-through (361 was not collected). A persistent preference shift toward domestic brands would show domestic mass brands taking share from both Western brands. From 2023 they did not. The 2021 to 2022 level shift is consistent with nationalism plus COVID, but the FY2025 to FY2027 decline is not.
- **Counterfactual (revision 2; replaces the FY24-based RMB 66.1bn, which used an overshipped base).** From the FY2023 base, Nike grown with the other five brands would be RMB 68,465m in FY2026, and grown with the NBS category RMB 58,598m, against an actual RMB 41,089m. The FY2023 base itself contains a -3.2 pt sell-in gap (FY23 wholesale +3.2% vs comps +9%), so it is not inflated. Sell-in-neutral Nike FY2023 to FY2026 is -11.9% (stores benchmark) to -15.9% (comps benchmark), against the other five +36.6% (including acquisitions), adidas +30.6% and NBS +16.9% (2022 to 2025) (my arithmetic, gc_calc_rev2 Section 4).

**Crude share of the total market (opinion-based):** Anta claims 21.8% (2025) and 20.8% (2024) of the Chinese sportswear market (Anta AR 2025 PDF p. 15, citing "a global authoritative institution", opinion). On that implied base Nike's share falls from 14.0% (FY25) to 11.2% (FY26) (my arithmetic; crude).

### 2.3b Matched window, Q2 2026 (Apr to Jun 2026) and Q1 FY27 (Jun to Aug 2026): peers (filings unless labelled)

| Brand or retailer | Measure | Period | Result | Source |
|---|---|---|---|---|
| ANTA brand | retail sales | Q2 2026 | "low-single digit positive growth" | Anta operational update 17 Jul 2026, PDF p. 1 |
| FILA | retail sales | Q2 2026 | "low-single digit positive growth" | same |
| Anta all other brands (Descente, Kolon Sport etc.) | retail sales | Q2 2026 | "25-30% positive growth" | same |
| Li Ning | retail sell-through | Q2 2026 | "decreased by low-single-digit"; e-commerce "mid-single-digit growth" | Li Ning operational update 15 Jul 2026, PDF p. 1 |
| Xtep core brand | retail sell-through | Q2 2026 | "Mid single digit year-on-year decline"; retail discount 25% to 30% | Xtep operational update 17 Jul 2026, PDF p. 1 |
| Saucony (Xtep) | retail sell-through | Q2 2026 | "Low single digit year-on-year growth" (H1: "Low teens") | same |
| adidas Greater China | revenue cn | Q2 2026 | +15% | adidas ad hoc release 30 Jul 2026 (company release) |
| Pou Sheng (multi-brand retailer; Nike and adidas) | revenue, RMB | Jun to Aug 2026 | -10.4% (my arithmetic from June -8.6%, July -13.9%, August -9.0%) | Pou Sheng monthly revenue announcements, PDF p. 2 each |
| NBS sports and recreation goods | retail sales | Jun to Aug 2026 | -5.6% (my arithmetic) | official statistics |
| Nike Greater China | revenue cn | Jun to Aug 2026 (Q1 FY27) | -26% (wholesale -31%, stores -14%, digital -28%) | Q1 FY27 10-Q p. 28 |

Reading: in mid-2026 the market was soft (domestic incumbents -5% to +3%), so macro explains part of Q1 FY27. But adidas still grew +15%, and Nike fell 20 to 30 points more than the domestic incumbents.

### 2.4 Channel decomposition (currency-neutral %, filings; contributions my arithmetic)

| Period | GC total | Wholesale | Direct | Digital | Nike stores | Comp stores | Implied digital weight in Direct | Digital contribution to Direct (pts) |
|---|---|---|---|---|---|---|---|---|
| FY23 | +4 | +3.2 (my arithmetic, derived) | +5 | -4 | n/a | +9 | n/a | n/a |
| FY24 | +8 | +15 | +1 | -8 | about +6 (my arithmetic, derived) | +1 | n/a | n/a |
| Q1 FY25 | -3 | +10 | -16 | -34 | n/a | -8 | n/a | n/a |
| Q2 FY25 | -11 | -15 | -7 | -4 | n/a | -8 | n/a | n/a |
| Q3 FY25 | -15 | -18 | -11 | -20 | n/a | -6 | n/a | n/a |
| FY25 | -12 | -13 | -12 | -22 | -6 | -7 | 0.38 | -8.2 |
| FY26 | -13 | -14 | -12 | -29 | -4 | -6 | 0.32 | -9.3 |
| Q1 FY26 | -10 | -9 | -12 | -27 | -4 | -5 | 0.35 | -9.4 |
| Q2 FY26 | -16 | -15 | -18 | -36 | -5 | -7 | 0.42 | -15.1 |
| Q3 FY26 | -10 | -13 | -5 | -21 | +1 | -1 | 0.27 | -5.7 |
| Q4 FY26 | -17 | -19 | -14 | -25 | -9 | n/a | n/a | n/a |
| Q1 FY27 | -26 | -31 | -18 | -28 | -14 | n/a | 0.29 | -8.0 |

Sources: FY23 10-K p. 39; FY24 10-K p. 41; Q1 FY25 10-Q p. 26; Q2 FY25 10-Q p. 31; Q3 FY25 10-Q p. 34; FY25 10-K p. 40; FY26 10-K p. 39; Q1 FY26 10-Q p. 27; Q2 FY26 10-Q p. 32; Q3 FY26 10-Q p. 36; Q1 FY27 10-Q p. 28. Q4 FY26 is from the Q4 FY26 call (Nike release, PDF p. 11). The digital weight solves Direct = w x Digital + (1 - w) x Stores, so rounding makes it approximate. FY23 wholesale is derived from total +4 and Direct +5 at a 0.541 wholesale weight. FY24 store sales are derived with a digital weight of 0.35 to 0.42 (range +5.8% to +7.5%; central +6.4%) (my arithmetic).

**FY2024 to FY2026 dollar bridge (reported, filings):** revenue -1,698 = wholesale -1,007 plus Direct -691.

**Sell-in gap proxy, two benchmarks (my arithmetic):**

| Period | Wholesale cn | vs Nike store sales: gap, pts of GC | vs comps: gap, pts of GC | Wholesale weight |
|---|---|---|---|---|
| FY23 | +3.2 | n/a | -5.8, -3.2 | 0.541 |
| FY24 | +15 | +8.6, +4.6 | +14.0, +7.5 | 0.533 |
| Q1 FY25 | +10 | n/a | +18 (wholesale pts) | n/a |
| Q2 FY25 | -15 | n/a | -7 | n/a |
| Q3 FY25 | -18 | n/a | -12 | n/a |
| FY25 | -13 | -7, -4.0 | -6, -3.4 | 0.565 |
| FY26 | -14 | -10, -5.6 | -8, -4.5 | 0.562 |
| Q2 FY26 | -15 | -10, -5.3 | -8, -4.2 | 0.528 |
| Q3 FY26 | -13 | -14, -8.0 | -12, -6.9 | 0.574 |
| Q4 FY26 | -19 | -10 (wholesale pts) | n/a | n/a |
| Q1 FY27 | -31 | -17, -10.0 | n/a | 0.591 |

- **Cumulative FY24 to FY26:** -5.0 pts (stores) or -0.4 pts (comps). GC cn FY23 to FY26 -17.3%; sell-in-neutral -11.9% (stores) to -15.9% (comps). FY24 to FY26 GC -23.4% cn; ex-gap -14.8% to -16.4% (my arithmetic).
- **This proxy is not a bound in either direction (revision 2 correction).** It assumes partner sell-through of Nike grows like Nike's own store sales or comps. The direction of the error differs by period, and I now test it with partner data instead of assuming it:
  - **FY25: probably understates destock.** Partners discounted heavily that year (Topsports GM 41.8% to 38.4%, -3.4pp, the largest drop in the series). They had been overstocked by the Q1 FY25 gap (+18 pts) (Q1 FY25 call PDF p. 9: "elevated inventory in the marketplace"). Partner sell-through in units was therefore probably above Nike's own store trend, which makes the true sell-in cut larger than -4.0.
  - **FY26: roughly neutral to an overstatement.** Topsports' GM moved only -0.4pp (attributed to online mix). Topsports' total purchases fell -5.6% against cost of sales -4.1%, so its own destock across all brands was about 1.5 pts. Under brand-weight assumptions (Nike 60% to 80% of principal brands, adidas +5% to +13%), Nike purchases at Topsports were -7.9% to -17.5% against Nike sales there of -6.5% to -15.7%, a Topsports-level destock of only 1.4 to 1.8 pts (my arithmetic, assumption-based; Section 2.5).
  - **Q4 FY26 and Q1 FY27: overstates destock.** On exactly matched windows, partner sell-through of Nike was worse than Nike's own stores. Topsports' Mar to May 2026 sales fell "low-teens", which implies Nike at Topsports of -17% to -35% against Nike Q4 FY26 wholesale of -19%. Pou Sheng's Jun to Aug 2026 revenue fell -10.4%, which implies Nike at Pou Sheng of -18% to -30% against Nike Q1 FY27 wholesale of -31%. The implied Q1 FY27 destock is -0.7 to -7.8 pts of GC, against -10.0 from the Nike-store proxy (my arithmetic, assumption-based; Section 2.10). This fits Nike's own view that partner doors are older (opinion), which is now backed by matched data rather than assumed.

### 2.5 Topsports (HK:6110), Nike's largest wholesale partner type (RMB m; filings)

| FY ending Feb | Revenue | Principal brands (Nike + adidas) | Principal % of revenue | Inventory | Gross margin | Inventory days | Stores at year end | Online share of retail sales |
|---|---|---|---|---|---|---|---|---|
| 2021 | 36,009.0 | 31,421.2 | 87.3% | 6,211.3 | n/c | 110.0 | n/c | n/c |
| 2022 | 31,876.5 | 27,569.3 | 86.5% | 6,686.2 | 43.4% | 130.4 | 7,695 | n/c |
| 2023 | 27,073.2 | 23,324.0 | 86.2% | 6,247.3 | 41.7% | 149.5 | 6,565 | "low-twenties" |
| 2024 | 28,933.2 | 24,834.1 | 85.8% | 6,283.8 | 41.8% | 136.1 | 6,144 | n/c |
| 2025 | 27,012.9 | 23,310.7 | 86.3% | 6,004.0 | 38.4% | 134.9 | 5,020 | "mid-30%" |
| 2026 | 25,739.9 | 22,329.9 | 86.7% | 5,485.9 | 38.0% | 131.4 | 4,360 | "higher proportion"; Nike online about 22% of total revenue |
| Q1 FY26/27 (Mar to May 2026) | "low-teens decline" (retail plus wholesale sales) | n/d | n/d | n/d | n/d | n/d | selling area -11.2% YoY | n/d |

Sources: Topsports AR 2021/22 PDF pp. 4, 13, 80; AR 2022/23 PDF pp. 8, 14, 91 (online "the mix to total retail sales elevated to low-twenties"); AR 2023/24 PDF pp. 16, 56; AR 2024/25 PDF pp. 11, 16, 58 (online "accounted for mid-30% of total retail sales"); AR 2025/26 PDF pp. 4, 5, 9, 10, 16, 58, 117 (PDF p. 9: "a higher proportion of online retail sales recorded in the year, led to deeper year-on-year discounts"); Q1 FY2026/27 operational update (25 Jun 2026); inside information announcement 22 Jul 2026, PDF p. 1. n/c = not collected; n/d = not disclosed.

Derived (my arithmetic):
- FY2025/26 purchases (cost of sales plus the change in inventory) were 15,437.2, -5.6% year on year, against revenue -4.7% and cost of sales -4.1%.
- Brand-weight scenarios (assumption: Nike 60% to 80% of principal brands; adidas sales and purchases +5% to +13%; other brands' purchases move like their sales, -7.4%): Nike sales at Topsports -6.5% to -15.7%, Nike purchases at Topsports -7.9% to -17.5%, Topsports-level destock 1.4 to 1.8 pts. Against Nike's FY26 GC wholesale of -14%, Topsports alone implies only a small FY26 destock. The rest of Nike's wholesale decline came from Topsports buying less because it sold less Nike.
- Online (approximate; mixes taken as 22% and 35%): RMB 5,956m (FY22/23) to 9,455m (FY24/25), about +59%; offline 21,117m to 17,558m, about -17%. Over the same years Nike's own GC Digital fell about -28% cn (FY23 to FY25).
- Stores -43.3% and gross selling area -26.9% from Feb 2022 to Feb 2026.

**Pou Sheng (Yue Yuen's China retail arm; RMB m; filings):** 2021 23,350.2; 2022 18,638.0 (-20.2%); 2024 18,453.9; 2025 17,132.1 (-7.2%); GM 2025 33.5% (-0.7pp, "aggressive promotions across the retail industry and increased average mark downs", Yue Yuen AR 2025 PDF p. 19). Monthly 2026: June 1,080.0 (-8.6%), July 993.9 (-13.9%), August 1,129.4 (-9.0%), September 1,314.8 (-2.5%); 9M 2026 12,402.7 (-3.9%) (Pou Sheng monthly revenue announcements, PDF p. 2). Online sales of Nike were "approximately 15% of the total revenue of the Group" in 2025 (business update 22 Jul 2026, PDF p. 1).

### 2.6 China official retail sales, enterprises above designated size (NBS; % YoY)

| Period | Clothes, shoes, hats and textiles | Sports and recreational articles | Total retail sales |
|---|---|---|---|
| 2021 | +12.7 | n/c | +12.5 |
| 2022 | -6.5 | n/c | -0.2 |
| 2023 | +12.9 | +11.2 | +7.2 |
| 2024 | +0.3 | +11.1 | +3.5 |
| 2025 | +3.2 | +15.7 | +3.7 |
| Jun 2026 | +3.9 | -2.2 | +1.0 |
| Jul 2026 | -1.0 | -10.6 | +0.6 |
| Aug 2026 | -0.5 | -4.8 | +0.4 |
| Jun to Aug 2026 combined (my arithmetic) | +1.1 | -5.6 | n/c |

Sources (NBS English press releases): 2021 `stats.gov.cn/english/PressRelease/202201/t20220118_1826503.html`; 2022 `.../202301/t20230118_1892301.html`; 2023 `.../202402/t20240201_1947119.html`; 2024 `.../202501/t20250124_1958445.html`; 2025 `.../202601/t20260120_1962354.html`; Jun 2026 `.../202607/t20260717_1964156.html`; Jul 2026 `.../202608/t20260819_1965078.html`; Aug 2026 `.../202609/t20260916_1965341.html`. Index (2021 = 100): 2022 93.5, 2023 105.6, 2024 105.9, 2025 109.3 (my arithmetic).

### 2.7 Margin bridge (USD m; filings, bridge my arithmetic; corrected in revision 2)

| Item | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|
| Revenue | 7,248 | 7,545 | 6,586 | 5,847 |
| Gross profit | 3,696 | 3,784 | 3,028 | 2,670 |
| Demand creation | 499 | 519 | 529 | 455 |
| Operating overhead | 1,012 | 1,019 | 973 | 993 |
| SG&A % revenue | 20.8% | 20.4% | 22.8% | 24.8% |
| Overhead % revenue | 14.0% | 13.5% | 14.8% | 17.0% |
| Other segment items added back (my arithmetic: EBIT minus GP plus SG&A) | n/c | +63 | n/c | +56 |
| EBIT | 2,283 | 2,309 | 1,602 | 1,278 |

Source: FY25 10-K p. 40 and FY26 10-K p. 39 (segment cost lines).

- **FY24 to FY26 EBIT bridge (corrected):** volume (lost revenue at the FY24 GM of 50.15%) -851.6; GM rate (45.66% vs 50.15%) -262.4; SG&A +90.0; other segment items -7.0 (+63 to +56). Sum -1,031.0 = actual -1,031. The bridge closes exactly; there is no rounding residual (my arithmetic).
- **EBIT margin FY24 to FY26 (corrected):** 30.60% to 21.86%, -8.75pp = GM -4.49pp + SG&A -4.38pp + other +0.12pp (my arithmetic).
- **Benchmark (revision 2):** EBIT margin change FY24 to FY26: NA -1.0pp, EMEA -5.7pp, APLA -5.8pp, GC -8.7pp (my arithmetic from repo `data/nike_region_profitability.csv`, which cites the 10-K segment tables). GC lost about 3pp more than EMEA and APLA, consistent with its larger volume loss on a fixed overhead base (GC overhead rose from 13.5% to 17.0% of revenue).
- **FY21 to FY26:** -17.3pp, of which GM about -7.8pp (approximate) and SG&A plus other about -9.5pp.
- **Sensitivity:** FY26 EBIT at the FY21 margin would be about US$2,287m, against an actual US$1,278m.
- **Gross-margin drivers in Nike's words:** FY25 -420 bps "primarily due to unfavorable changes in standard foreign currency exchange rates and higher inventory obsolescence reserves" (FY25 10-K p. 40). FY26 -30 bps "primarily due to unfavorable changes in standard foreign currency exchange rates" (FY26 10-K p. 39). Q2 FY26 -280 bps "higher inventory obsolescence reserves and higher product costs" (Q2 FY26 10-Q p. 33). Q3 FY26 +300 bps "lower inventory obsolescence reserves" (Q3 FY26 10-Q p. 36).

### 2.8 Greater China vs Nike's other regions (currency-neutral %, filings; revision 2)

| Period | NA | EMEA | APLA | Ex-GC weighted (my arithmetic) | GC | China-specific gap | Share of GC change shared with the rest of Nike |
|---|---|---|---|---|---|---|---|
| FY24 | -1 | 0 | +5 | +0.3 | +8 | +7.7 | about 3% |
| FY25 | -8 | -10 | -3 | -7.8 | -12 | -4.2 | about 65% |
| FY26 | +5 | -3 | -1 | +1.4 | -13 | -14.4 | none |
| Q1 FY27 | +2 | -5 | 0 | -0.6 | -26 | -25.4 | about 2% |

Weights are prior-period reported revenues (repo `data/nike_region_profitability.csv`; Q1 FY27 uses FY26). Note: the reported-USD changes the reviewer cited (FY26 EMEA +2.6%) differ from the currency-neutral figures used here (EMEA -3%).

By channel (GC vs NA, EMEA, APLA; filings):

| Period | Wholesale | Direct | Digital | Store sales | Comps |
|---|---|---|---|---|---|
| FY25 | GC -13 vs -5, -6, -3 | -12 vs -12, -16, -3 | -22 vs -19, -30, -9 | -6 vs -1, +5, +4 | -7 vs -1, +5, +1 |
| FY26 | -14 vs +14, 0, +2 | -12 vs -6, -9, -6 | -29 vs -10, -10, -9 | -4 vs -2, -8, -1 | -6 vs -2, -7, -4 |
| Q1 FY27 | -31 vs +9, -1, +2 | -18 vs -6, -12, -3 | -28 vs -6, -26, -10 | -14 vs -6, -1, +5 | n/d |

Readings (my arithmetic, simple ex-GC means):
- **FY25:** GC Direct (-12) and Digital (-22) were in line with the rest of Nike; NA Direct was also -12. The China-specific excess was wholesale (-4.7 pts of GC) and Nike stores (comps -7 vs ex-GC mean +1.7). Footwear was not China-specific (-13 = NA -13). The Nike-wide cycle (Jordan, classics, the digital traffic collapse) is the main FY25 driver.
- **FY26:** GC comps (-6) were close to EMEA (-7). The China-specific excess sits in wholesale (-10.9 pts of GC; NA wholesale +14) and digital (-29 vs about -10). These are the channels of the deliberate clean-up and of partner-platform discounting.
- **Q1 FY27:** the excess shows in every channel, including Nike-owned stores (-14 vs ex-GC mean -0.7).
- **Product category:** Q1 FY27 call: Nike Performance up "high single digits"; excluding GC, "up low double digits" (call PDF p. 10). For the total to be below ex-GC, GC Performance must have grown more slowly than the total. Under most of the weights I tried (GC 8% to 16% of Performance, total 7% to 9%, ex-GC 10% to 13%), GC Performance declined (implied +4% to -62%). So GC's Q1 FY27 weakness was not only Sportswear (my arithmetic, assumption-based).

### 2.9 Partner online channel (revision 2)

| Item | Value | Label and source |
|---|---|---|
| Topsports: online sales of Nike as % of total revenue, FY ended 28 Feb 2026 | "approximately 22%" | filing: Topsports inside information 22 Jul 2026, PDF p. 1 (also 25 Jun 2026 announcement) |
| Pou Sheng: online sales of Nike as % of total revenue, 2025 | "approximately 15%" | filing: Pou Sheng business update 22 Jul 2026, PDF p. 1 |
| Implied Topsports Nike online revenue | RMB 5,663m (US$806m at FY26 average 7.0274) | my arithmetic |
| Implied Pou Sheng Nike online revenue | RMB 2,570m (US$366m) | my arithmetic |
| Combined, at retail | US$1,171m | my arithmetic |
| Wholesale-equivalent at partner cost-of-sales ratios (Topsports 62.0%, Pou Sheng 66.5%) | US$743m = 22.8% of FY26 GC wholesale, 12.7% of FY26 GC revenue | my arithmetic; assumption that online cost ratios equal the group average (online carries deeper discounts, so the true ratio is probably higher) |
| Nike's own GC Digital (estimated) | FY24 about 1,231; FY25 about 924; FY26 about 656 (US$m) | my arithmetic from implied digital weights 0.375 and 0.32; approximate |
| Nike Digital decline FY24 to FY26 | about -575 US$m = -7.6% of FY24 GC | my arithmetic |
| Net revenue effect if 0%, 50% or 100% of that lost volume moved to partner online and was booked at 0.62 of retail | -7.6, -5.3, -2.9 pts of FY24 GC | my arithmetic, assumption-based |

Interpretation: partner-run online stores sold more Nike product at retail than Nike's own Digital channel did. Topsports' online channel grew about 59% while Nike Digital in GC fell about 28% (FY23 to FY25). Nike's statements describe consumers shopping "on local platforms with deeper discounts" (Q1 FY26 call PDF p. 11, opinion). Nike then terminated all partner online sales from 1 January 2027 (filings above; Q1 FY27 call PDF p. 5 "eliminating distribution through channels that are not aligned with our marketplace strategy"). So part of the Nike Digital decline is channel migration, not lost demand. It is still a real revenue loss, because Nike earns a wholesale price on those units. The share that migrated is not identified (Section 5). **Forward implication (my arithmetic):** about US$743m of partner online wholesale is at stake from January 2027, about 12.7% of FY26 GC revenue, before any recapture by Nike's own Tmall, JD and Douyin flagships.

### 2.10 Partner sell-through on exactly matched windows (revision 2; my arithmetic, assumption-based)

**Pou Sheng Jun to Aug 2026 (= Nike Q1 FY27):** revenue -10.4% (filings). Assume Nike 50% to 70% of Pou Sheng sales, adidas 20% to 30% growing +10% to +15%, and other brands flat. Then Nike at Pou Sheng fell -17.8% to -29.9%. Against Nike GC wholesale of -31%, the sell-in gap is -1.1 to -13.2 wholesale pts, or -0.7 to -7.8 pts of GC (central about -4).

**Topsports Mar to May 2026 (= Nike Q4 FY26):** "low-teens decline" (filings), taken as -11% to -14%. With Nike 60% to 80% of principal brands, adidas +10% to +15% and other brands -7.4%, Nike at Topsports fell -16.9% to -35.0%. Against Nike GC Q4 FY26 wholesale of -19%, the gap is -2.1 to +16.0 wholesale pts. In most scenarios Nike's sell-in fell less than Topsports' Nike sales, which points to no extra destock at Topsports that quarter.

These tests rest on undisclosed brand weights and on adidas growing at partners as it did overall. They are evidence, not measurement. They also include the partners' online Nike sales, which were still running.

### 2.11 Hong Kong check (official statistics; revision 2)

HK C&SD provisional retail sales, Dec 2025 release (`gia.info.gov.hk/general/202602/03/P2026020300456_531276_1_1770103979194.pdf`), Table 1, PDF p. 1: "Clothing, footwear and allied products ... 42,402 ... -3.9" (value, Jan to Dec 2025 over 2024); "Footwear, allied products ... 5,826 ... -6.5". Volume, PDF p. 3: -2.2. Nike does not disclose GC by territory. If HK, Macau and Taiwan were 10% to 30% of GC and fell 3.9% to 10%, then the mainland fell -13.3% to -16.9% in FY26 (my arithmetic). Territory mix cannot explain the decline; it makes the mainland look worse. Taiwan was not checked.

---

## 3. Verbatim quotes with sources

### Nike filings (canonical URLs `https://www.sec.gov/Archives/edgar/data/320187/<accession>/<file>`; downloaded from the investors.nike.com mirror)
- FY22 10-K p. 39 (0000320187-22-000038, nke-20220531.htm): "Greater China revenues for fiscal 2022 decreased 13%, reflecting impacts from supply chain constraints, government restrictions due to COVID-19 as well as marketplace dynamics."
- FY23 10-K p. 39 (0000320187-23-000039, nke-20230531.htm): "Greater China revenues increased 4% on a currency-neutral basis, primarily due to higher revenues in the Jordan Brand ... NIKE Direct revenues increased 5%, due to comparable store sales growth of 9% and the addition of new stores, partially offset by digital sales declines of 4%."
- FY24 10-K p. 41 (0000320187-24-000044): "Greater China revenues increased 8% on a currency-neutral basis ... Wholesale revenues increased 15%. NIKE Direct revenues increased 1%, driven by comparable store sales growth of 1% and the addition of new stores, partially offset by a decline in digital sales of 8%."
- Q1 FY25 10-Q p. 26 (nke-20240831.htm): "Greater China revenues decreased 3% on a currency-neutral basis, primarily due to lower revenues in the Jordan Brand. Wholesale revenues increased 10%. NIKE Direct revenues decreased 16% due to digital sales declines of 34% and comparable store sales declines of 8%".
- FY25 10-K p. 40 (0000320187-25-000047): "Unit sales of footwear decreased 11%, while lower ASP per pair reduced footwear revenues by approximately 2 percentage points." and "Unit sales of apparel decreased 17%, while higher ASP per unit contributed approximately 5 percentage points of apparel revenue growth. Higher ASP per unit was primarily due to strategic pricing actions, partially offset by higher discounts."
- FY25 10-K p. 38: "North America revenues decreased 8% on a currency-neutral basis primarily due to lower revenues in the Jordan Brand, Men's and Women's." p. 41: "APLA ... Revenues decreased primarily due to lower revenues in the Jordan Brand and Men's." and "Unit sales of apparel decreased 3%, while higher ASP per unit contributed approximately 2 percentage points ... primarily due to strategic pricing actions".
- FY26 10-K p. 39 (0000320187-26-000088): "Wholesale revenues decreased 14%, reflecting our actions to prioritize marketplace health. NIKE Direct revenues decreased 12% due to declines in digital sales of 29% and declines in store sales of 4%. Comparable store sales decreased 6%."
- FY26 10-K p. 37: "North America revenues increased 5% on a currency-neutral basis. Wholesale revenues increased 14% including expanded distribution, higher shipments to existing partners and fewer marketplace management actions taken in the current year." p. 38: "EMEA revenues decreased 3% ... Comparable store sales decreased 7%."
- FY26 10-K p. 30: "in Greater China, a trend of declining store traffic, elevated promotional activity and higher levels of inventory across the marketplace are negatively impacting revenues and overall profitability" (opinion).
- Q1 FY27 10-Q p. 28 (0000320187-26-000193): "Greater China revenues decreased 26% on a currency-neutral basis. Wholesale revenues decreased 31%. NIKE Direct revenues decreased 18% due to declines in digital sales of 28% and declines in store sales of 14%." and "Unit sales of footwear decreased 26%, while ASP per pair was flat as lower discounts were offset primarily by channel mix." p. 26: "North America revenues increased 2% ... NIKE Direct revenues decreased 6% due to declines in digital sales of 6% and declines in store sales of 6%."
- Q1 FY27 10-Q p. 20: "The actions related to Converse are expected to continue throughout fiscal 2027 and for Greater China to extend beyond fiscal 2027."
- Q2 FY26 10-Q p. 33 (0000320187-25-000151): "Gross margin contraction of 280 basis points, primarily due to higher inventory obsolescence reserves and higher product costs, driven by product mix, partially offset by higher ASP."

### Nike earnings call remarks (Nike release; PDFs at `https://s1.q4cdn.com/806093406/files/...`; PDF page numbers)
- Q4 FY24 PDF p. 9: "particularly in Greater China, where brick-and-mortar traffic declined as much as double-digits versus prior year" (opinion). PDF p. 12: "In Greater China, Q4 revenue grew 7%, including several points of contribution from TMall's earlier start to the 6.18 shopping holiday. Excluding this timing benefit, we fell short of our plan".
- Q1 FY25 PDF p. 9: "Nike Direct declined 16%, with Nike Digital down 34% and Nike Stores down 4%. Wholesale grew 10%. ... traffic decelerated in our channels with lower sell-thru rates. This has resulted in elevated inventory in the marketplace in an already promotional environment."
- Q3 FY25 PDF p. 13: "In Q3, traffic declined double-digits and retail sales underperformed our plan." and "we are taking aggressive steps to clean-up the marketplace, with the priority being the health of our partners. These steps had a negative impact on our revenue and gross margin this quarter."
- Q4 FY25 PDF p. 11: "Greater China executed a deeper reset of inventory relative to our other geographies, with higher sales related reserves, higher discounts and supply reductions."
- Q1 FY26 PDF p. 11: "traffic declined versus the prior year in both Nike owned and partner stores, resulting in lower in-season sell-thru rates. Digital remains a highly promotional marketplace in Greater China, with consumer shopping moments extending longer on local platforms with deeper discounts." and "Running is a bright spot in China, growing high single digits". PDF p. 7: "With over 5,000 mono-brand stores in China, this will take investment and it will take time."
- Q2 FY26 PDF p. 8: "inventory obsolescence in Greater China that was not contemplated ninety days ago." PDF p. 10: "These challenges resulted in a higher mix of off-price sales with higher markdowns, higher sales- related returns, higher wholesale discounts, and higher obsolescence charges to clean marketplace inventory levels." PDF p. 11: "We were less promotional during 11.11, resulting in an approximate 35% decline versus the prior year, in line with our plans. We accelerated returns of aged inventory owned by partners, and wrote off both partner and Nike inventory in the quarter. ... We reduced sell-in plans for spring, and we cut our buys for summer".
- Q3 FY26 PDF p. 12: "Running grew double digits in the quarter ... Sportswear declined double - digits as expected. Wholesale sell-in was managed down, while seasonal sell through rates sequentially improved." and "Inventory was down mid-teens versus the prior year, with units down more than 20%, and partner inventory also declined double-digits". APLA, same page: "Running up double digits ... while Sportswear declined double digits." PDF p. 14: "We expect Greater China to be down approximately 20% in the fourth quarter, reflecting reduced sell-in that we highlighted last quarter".
- Q4 FY26 PDF p. 11: "In Greater China, Q4 revenue declined 17%. Nike Direct declined 14%, with Nike Digital down 25%, and Nike Stores down 9%. Wholesale declined 19%."
- Q1 FY27 (`content_files/NIKE-Inc-Q1FY27-UNOFFICIAL-Transcript.pdf`) PDF p. 3: "Nike Sportswear, which accounted for just under half of this quarter's revenue, was down low double-digits. The decline reflected a combination of deliberate actions, product underperformance and broader marketplace pressure." and "As planned, we reduced revenue from the Dunk by nearly 50% in the quarter. That resulted in roughly 200-milion-dollar headwind in Sportswear." PDF p. 4: "Simply put we've been oversupplying our iconic retro product asking them to do too much." PDF p. 5: "We are eliminating distribution through channels that are not aligned with our marketplace strategy which will decrease the deep discounting of our brands." and "The majority of our partner's physical doors in Greater China have not been refreshed in the past 7 years." PDF p. 10: "if we were to exclude the reset in Greater China, Nike Performance would have been up low double digits in Q1." PDF p. 13: "We will continue to take actions to reduce supply across key parts of the marketplace".

### Peers and partners (filings or company releases)
- Topsports inside information, 22 Jul 2026 (`www1.hkexnews.hk/listedco/listconews/sehk/2026/0722/2026072200069.pdf`) PDF p. 1: "the Group's existing online sales of Nike's products in mainland China will terminate completely with effect from January 1, 2027" and "the revenue contribution from the online sales of Nike's products accounted for approximately 22% of the total revenue of the Group for the financial year ended February 28, 2026."
- Pou Sheng business update, 22 Jul 2026 (`www1.hkexnews.hk/listedco/listconews/sehk/2026/0722/2026072200197.pdf`) PDF p. 1: "For the year ended December 31, 2025, the revenue contribution from online sales of Nike's products accounted for approximately 15% of the total revenue of the Group while its contribution to the Group's profit was insignificant."
- Pou Sheng monthly revenue, June 2026 (`.../2026/0710/2026071000275.pdf`) PDF p. 2: "1,080,007 (2025 (RMB'000): 1,181,264), decreased by 8.6%"; July (`.../2026/0810/2026081000336.pdf`): "993,878 (2025 (RMB'000): 1,154,119), decreased by 13.9%"; August (`.../2026/0910/2026091000378.pdf`): "1,129,431 (2025 (RMB'000): 1,241,261), decreased by 9.0%"; September (`.../2026/1012/2026101200300.pdf`): "1,314,827 (2025 (RMB'000): 1,347,982), decreased by 2.5%".
- Topsports AR 2024/25 (`www1.hkexnews.hk` annual report) PDF p. 11: "online retail sales, including public domain and private domain, experienced double-digit growth compared to the previous year and accounted for mid-30% of total retail sales." AR 2022/23 PDF p. 8: "retail online sales soared year-on-year, and the mix to total retail sales elevated to low-twenties". AR 2025/26 PDF p. 9: "fierce promotional activities in China's online sports footwear and apparel market, together with a higher proportion of online retail sales recorded in the year, led to deeper year-on-year discounts".
- Anta operational update Q2 2026 (`www1.hkexnews.hk/listedco/listconews/sehk/2026/0717/2026071700328.pdf`) PDF p. 1: ANTA and FILA "low-single digit positive growth"; all other brands "25-30% positive growth".
- Li Ning operational update Q2 2026 (`.../2026/0715/2026071500286.pdf`) PDF p. 1: "the retail sell-through of LI-NING POS ... decreased by low-single-digit on a year-on-year basis". Li Ning interim 2026 (`.../2026/0820/2026082001445.pdf`) PDF p. 1: "Revenue rose by 2.8% to RMB15,235 million".
- Xtep operational update Q2 2026 (`.../2026/0717/2026071700195.pdf`) PDF p. 1: core brand "Mid single digit year-on-year decline"; "Retail discount level 25%-30%". Xtep interim 2026 (`.../2026/0825/2026082500235.pdf`) PDF p. 1: "Revenue of the core Xtep brand decreased modestly by 2.2% to RMB5,919.9 million".
- adidas Annual Report 2022 and 2025, the adidas Q2 2026 ad hoc release, Anta, Li Ning, Xtep, 361 Degrees, Topsports and Yue Yuen annual reports: as in revision 1 (unchanged; paths in Section 6).

### Secondary (labelled; not used alone)
- FashionUnited, Feb 2026: Amer Greater China "+43.4 percent to 1.86 billion US dollars" (secondary).
- On Holding FY2025 Asia-Pacific +96.4% (snippet only, not evidence).
- Pou Sheng H1 2026 gross margin 33.9% (secondary, FilingReader summary; the primary interim report is on HKEX, `.../2026/0812/2026081200368.pdf`, downloaded but not read for this line).
- Sneaker resale (Dewu/Poizon, StockX): no quantitative 2024 to 2026 source found; snippet only.

---

## 4. Decomposition of FY2026 (-13% cn) and Q1 FY2027 (-26% cn) (revised)

All points are of GC currency-neutral revenue change (my arithmetic). Ranges reflect the stated assumptions. The rows are channel-based and overlap with the causal verdicts in Section 1, as noted.

Channel identity (my arithmetic, gc_calc_rev2 Section 10): GC change = wholesale growth x wholesale weight + Direct growth x Direct weight. The wholesale part splits into the sell-in gap (destock) and partner sell-through of Nike.

| Component | FY2026 | Q1 FY2027 | Basis |
|---|---|---|---|
| Wholesale contribution | -7.9 (-14 x 0.562) | -18.3 (-31 x 0.591) | filings, my arithmetic |
| of which sell-in below partner sell-through (FY24 unwind plus deliberate clean-up, including returns) | -1.0 to -5.6 | -0.7 to -10.0 (Pou Sheng matched window -0.7 to -7.8, central about -4; Nike-store proxy -10) | Sections 2.4, 2.5, 2.10 |
| of which partner sell-through of Nike | -2.3 to -6.9 pts, i.e. Nike sold through partners -4% to -12% | -8.3 to -17.6 pts, i.e. -14% to -30% | remainder |
| Direct contribution | -5.3 (-12 x 0.438) | -7.4 (-18 x 0.409) | filings |
| of which Nike Digital (part Nike-wide, part promotion cuts, part migration to partner platforms) | -4.1 (China excess over other regions about -2.7) | -3.3 | Sections 2.4, 2.8, 2.9 |
| of which Nike-owned stores | -1.2 (stores -4; comps -6, close to EMEA -7) | -4.1 (stores -14 vs ex-GC mean about -1) | Section 2.4 |
| **Total** | -13.1 (reported -13) | -25.7 (reported -26) | |

Benchmarks for the sell-through lines: the rest of Nike +1.4% (FY26) and -0.6% (Q1 FY27); the category +3.2% (NBS apparel 2025) and about -5% to +3% in mid-2026 (NBS sports goods -5.6%; domestic incumbents' sell-through); adidas +9% cn (2025) and +15% (Q2 2026). Partner sell-through of Nike at -4% to -12% (FY26) and -14% to -30% (Q1 FY27) is well below every benchmark. That gap is the share loss.

**Which explanation survives, and why the others do not:**

1. **Consumer sell-through share loss is necessary in every period.** It is the one explanation that the channel adjustments do not remove:
   - Nike-owned comps fell -12.6% over FY25 and FY26 while the category grew +3.5% and adidas +20.3%.
   - After removing every sell-in gap, GC still fell -11.9% to -15.9% from FY23 to FY26, while every peer and the category grew.
   - On the matched mid-2026 windows, Nike fell 20 to 30 points more than the domestic incumbents and about 40 points more than adidas.
2. **Its cause changes over time.**
   - In FY25 it is mostly the Nike-wide Sportswear, Jordan and digital cycle: GC footwear fell exactly as much as NA footwear, and Jordan led the decline in all four regions.
   - From FY26 it is China-specific: the rest of Nike was flat. The China-specific part sat in wholesale and digital in FY26, and reached Nike's own stores in Q1 FY27.
   - Q1 FY27 data imply that GC Performance probably also declined, so it is not only Sportswear.
3. **The channel mechanics are real but do not stand alone.**
   - The FY24 overshoot and its unwind net to about zero over FY24 to FY26.
   - The deliberate clean-up is the largest in Q1 FY27, but matched partner data put it at about 1 to 8 points rather than 10.
   - Migration to partner platforms changes how much revenue Nike books per unit of demand. It does not create the demand loss.
4. **Ruled out:** the guochao or boycott shift (domestic mass brands lag adidas from 2023), price cuts, territory mix, and a total consumption collapse.

   **Small and bounded:** elasticity from price increases (at most about 2 pts, FY25 apparel only).

---

## 5. Unresolved, and the data that would resolve it

1. **The split among destock, partner sell-through and channel migration in Q1 FY27 (about 1 to 10 points).** Needs Nike-brand revenue and inventory at Topsports and Pou Sheng (not disclosed; Topsports reports only "principal brands" = Nike plus adidas), or Nike's GC sell-through and partner weeks of supply. Topsports' Q2 FY2026/27 operational update (Jun to Aug 2026, not yet published as of 13 Oct 2026) would give a second matched window.
2. **How much of the Nike Digital decline migrated to partner online stores.** Needs Nike-brand GMV on Tmall, JD and Douyin split by Nike flagship vs partner stores (Syntun, Moojing or similar). The 2027 termination will itself show the answer: if Nike's own digital recaptures the partner online volume, migration was large.
3. **Who took the share, by category.** Needs platform GMV by brand, or Euromonitor China sportswear brand shares 2021 to 2026. Also Amer Sports' Greater China revenue from its own 6-K (the 43.4% here is secondary), and On and Deckers China disclosures.
4. **GC category mix (Sportswear, Jordan, Performance) in dollars.** Not disclosed. The Q1 FY27 Performance inference rests on assumed weights.
5. **Sneaker resale premiums in China** (Dewu/Poizon price indices for Jordan 1, Dunk and AF1) to size the hype-cycle effect.
6. **Partner returns and sales-related reserves in GC.** Disclosed only qualitatively (Q4 FY25, Q2 FY26 calls). They sit inside the wholesale gap and cannot be separated from lower shipments.
7. **Taiwan retail data, and Nike's revenue by territory within GC.**
8. **FY21 and FY22 GC gross margin and SG&A.** Segment cost lines start in the FY25 10-K (covering FY23 onward).

---

## 6. Files

- Revision 1 downloads: `scratchpad/rh/dl/gc/` (nike/, pages/, calls/, adidas/, anta/, lining/, xtep/, d361/, topsports/, yueyuen/, nbs/, fx/).
- Revision 2 downloads: `scratchpad/rh/dl/gc_rev2/`:
  - anta_q2_2026_update.pdf, lining_q2upd.pdf, lining_interim.pdf, xtep_q2upd.pdf, xtep_interim.pdf
  - ps_m2605 to ps_m2609.pdf, ps_bizupd_0722.pdf, ps_interim2026.pdf
  - tops_inside_0625.pdf, tops_inside_0722.pdf
  - hk_retail_dec2025.pdf
  - HKEX title-search listings s_*.json
- Calculations: `scratchpad/rh/scripts/gc_calc.py` (output `gc_calc_out.txt`) and `scratchpad/rh/scripts/gc_calc_rev2.py` (output `gc_calc_rev2_out.txt`). Page finder: `scratchpad/rh/scripts/findpg.py`. Revision 1 backup: `scratchpad/rh/gc_decline_rev1_backup.md`.

---

## 7. Revision log

**Revision 2 (2026-10-13), in response to two reviewer reports (both "weakened").**

Fixed source and arithmetic checks:
1. **EBIT bridge sign error (2.7, Bottom line 5).** Other segment items are added back to EBIT (+63 in FY24, +56 in FY26), so their change is -7, not +7. The bridge now closes exactly (-851.6 - 262.4 + 90.0 - 7.0 = -1,031.0). The claimed "-14 rounding residual" was spurious and has been removed. The margin split is corrected to GM -4.49 + SG&A -4.38 + other +0.12 = -8.75pp (it previously read "other -0.1", and the components did not add up). Recomputed in gc_calc_rev2.py Section 1.
2. **"Upper bound" label on the sell-in proxy removed (2.4).** It was an assumption. The proxy is now shown with both the store-sales and comps benchmarks, and the direction of its bias is tested by period with partner data instead of asserted. FY25: likely an understatement (partner discounting; Topsports GM -3.4pp). FY26: about neutral (Topsports purchases test). Q4 FY26 and Q1 FY27: an overstatement (Topsports and Pou Sheng matched windows).
3. **"Boycott ruled out because adidas grew" (old row 7).** Replaced by a two-part test. adidas and Nike are both about -16% below 2021, but adidas's entire loss is in 2022. From 2023, and in 2025 and Q2 2026, adidas outgrew the domestic mass brands. A slow-burn guochao shift is therefore ruled out as a driver of FY25 to FY27, though not of the 2021 to 2022 level shift (new rows 10 and 11).
4. **FY24-based share counterfactual (old RMB 66.1bn) replaced (2.3).** FY24 was overshipped (wholesale +15% vs comps +1%). The counterfactual now uses the FY23 base plus sell-in-neutral growth rates.
5. **"Price ruled out because ASP flat" (old row 6).** Now split into price cuts (ruled out for revenue) and price increases or elasticity (new row 8). The latter is tested against the other regions and bounded at about -1.9 pts, FY25 apparel only.

New alternatives tested (all new data in Sections 2.3b and 2.8 to 2.11):
6. **Nike-wide product cycle:** supported for FY25 (about 65% of the GC decline is shared with the other regions); not the explanation for FY26 or Q1 FY27 (new row 2, Section 2.8).
7. **FY24 sell-in overshoot and unwind:** supported; the cumulative FY24 to FY26 gap is -0.4 to -5.0 pts (new row 3).
8. **Deliberate franchise supply cuts inside the "share loss" residual:** supported in part (Dunk -50% globally, Jordan retro cuts). Aged-inventory write-offs and "underperformed our plan" show that demand-driven shortfalls also occurred (row 7).
9. **Migration of online demand to partner-run platforms:** supported as a mechanism with new filings (Topsports 22%, Pou Sheng 15%). The size is a range (row 5, Section 2.9).
10. **Partner discounting holding up unit sell-through:** tested with Topsports GM by year. It matters for FY25 (-3.4pp), little for FY26 (-0.4pp), and Pou Sheng's GM rose in H1 2026 (secondary).
11. **Partner returns and reserves:** listed separately (row 4, Section 5 item 6); not separable.
12. **Resale and hype collapse:** no data found; Nike-wide in FY25 and partly caused by Nike's own oversupply (row 13).
13. **Digital reclassification:** folded into the migration test (row 5).
14. **HK, Macau and Taiwan mix:** ruled out with HK C&SD data (row 14, Section 2.11).

Other changes:
15. Bottom line rewritten. Section 4 now uses a channel identity that adds back to the reported change (-13.1 and -25.7), instead of mixing benchmarks with channel contributions. The sell-through share loss is now established with comps and sell-in-neutral revenue rather than as a residual. The FY25 global versus FY26 China-specific split is explicit. The Section 4 decomposition is revised with matched partner windows (the Q1 FY27 destock estimate cut from "up to 10" to 0.7 to 10, central about 4).
16. Added FY23 and Q1 to Q3 FY25 GC channel rows, the H1 2026 Li Ning and Xtep revenue, the regional EBIT margin benchmark, and the forward estimate of about US$743m of partner online wholesale at stake from January 2027.
