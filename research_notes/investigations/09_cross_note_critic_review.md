# Completeness critic: cross-note review of the eight rh/ notes

> **Status: DRAFT (Oct 13, 2026).** Produced by the multi-agent investigation (one investigator, two adversarial reviewers, revision rounds). Independent spot-checks are logged at the end of this file.


**Prepared:** October 13, 2026. **Notes read in full:** na_wholesale.md (rev 2), gc_decline.md (rev 2), direct_decline.md (rev 2), markdown_depth.md (rev 3), na_margin.md (rev 2), concentration.md (rev 2), region_gm_decline.md (rev 3), footwear_decline.md (rev 2).
**Arithmetic:** `scratchpad/rh/critic/critic_calc.py`, output `scratchpad/rh/critic/critic_calc_out.txt` (run with `python3 -I`). Every derived number below is from that script and labelled **my arithmetic**. Inputs are the figures the notes themselves cite (filing pages given), plus repo `data/nike_region_profitability.csv`.
**Labels:** filing, Nike release, secondary, snippet only, my arithmetic, opinion.

---

## (a) Contradictions between notes

Ranked by how much they matter for the pitch.

### A1. "Top-3 concentration rose because Dick's absorbed Foot Locker" (na_wholesale) vs concentration.md (direct contradiction)
- **na_wholesale.md, verdict row 11:** "Top-3 concentration rose from 21% to 29% because Dick's absorbed Foot Locker."
- **concentration.md, bridge and row 3:** the Dick's and Foot Locker merger explains **0** of the FY25 rise (closed Sept 8, 2025, Nike FY26 Q2) and is only one candidate inside an FY26 residual of about +0.85 to +0.95 pts. The identified drivers are channel mix (+3.1 pts) and JD plus Hibbett (+3.0 to 4.2 pts) (my arithmetic in that note).
- **Fix:** na_wholesale row 11 should cite concentration.md and drop the causal claim. Its "ruled out as independent" verdict can stay; its stated reason is wrong.

### A2. Greater China's EBIT benchmark uses NA's margin with the IEEPA refund still in it (gc_decline vs na_margin)
- **gc_decline.md, bottom line 5 and Section 2.7:** "EBIT margin change FY24 to FY26: NA -1.0pp, EMEA -5.7pp, APLA -5.8pp, GC -8.7pp", which it uses to argue the other regions "lost less margin".
- **na_margin.md:** NA FY26 includes a $965M IEEPA refund in Cost of sales (FY26 10-K p. 30, filing).
- **Recomputed (my arithmetic from repo `data/nike_region_profitability.csv`):** NA EBIT margin 27.21% (FY24) to 26.21% (FY26) reported, -1.00 pp. Excluding the $965M refund, FY26 is 21.51%, **-5.71 pp**. That equals EMEA (-5.67 pp) and APLA (-5.80 pp). GC (-8.75 pp) is still the worst, by about 3 pp, not about 8 pp versus NA.
- **Caveat:** the ex-refund NA figure still carries FY26 tariffs. On na_margin's no-new-tariff basis NA gross margin rose, so neither reading supports "NA lost about 1 pp". The note should show the benchmark both ways.

### A3. Discounting and Greater China gross margin (gc_decline vs region_gm_decline)
- **gc_decline.md, verdict row 9:** price cuts and discounting "ruled out for revenue; **supported for margin**", citing "GM: FY25 -420 bps, Q2 FY26 -280 bps".
- **region_gm_decline.md, row 3:** lower ASP from discounts is "**ruled out** as a main GC driver". Nike's own GC bullets for those same periods name standard FX and obsolescence reserves (FY25), and obsolescence plus product costs (Q2 FY26), each "partially offset by **higher** ASP" (FY25 10-K p. 40; Q2 FY26 10-Q p. 33, filing; both quoted in gc_decline itself).
- **Resolution:** region_gm_decline is correct on Nike's wording. gc_decline row 9 should read "ruled out for Nike's GC gross margin, where ASP was a tailwind. Partner discounting (Topsports GM -3.4 pp) hit partners, not Nike's segment margin directly." gc_decline's margin section also never mentions standard-rate FX. region_gm_decline puts FX at -91 to -134 bps (FY25) and -17 to -25 bps (FY26) of GC's FY24 to FY26 decline (central, my arithmetic in that note). gc_decline's -262.4 GM-rate line should cite that split.

### A4. NA channel-shift share counts Direct retail dollars as wholesale dollars (na_wholesale vs direct_decline and markdown_depth)
- **na_wholesale.md:** NA Direct -$535M "against wholesale +$1,474M (36% matched)" for FY26. For Q1 FY27, "NA Direct fell $138M, which equals 56% of the $245M wholesale gain (channel shift)".
- **direct_decline.md T10 and markdown_depth.md Table A:** a dollar of Direct revenue is worth about 1/1.654 = 0.605 dollars at wholesale (FY24 10-K p. 34 internal sales, filing).
- **Recomputed (my arithmetic):** at wholesale-equivalent value, channel shift is **21.9%** of FY26 NA wholesale growth (not 36%) and **34.1%** of Q1 FY27 growth (not 56%). That leaves about $160M, not $107M, of Q1 FY27 growth for price/mix, World Cup, Foot Locker fill and new doors. The fill and World Cup slices therefore get bigger.
- Related inconsistency: na_wholesale T6 assumes a Direct/wholesale unit price ratio r = 1.3 to 2.0 "as my assumption". The repo already has the measured FY24 value of 1.654 (note 09; markdown_depth Table A), with FY25 bounded at about 1.49 to 1.56 (markdown_depth Table D). T6 should anchor on these values.

### A5. Q1 FY27 footwear "fully explained" (footwear_decline) vs channel fill (na_wholesale)
- **footwear_decline.md, row 17:** Q1 FY27 footwear -$459M = about -$243M GC plus about -$200M Dunk, "leaving about -$16M". The verdict on ongoing demand weakness is "outside the window", which reads as "no residual weakness".
- **na_wholesale.md:** Q1 FY27 NA wholesale (+9%) was flattered by a Foot Locker inventory build (inventory +14.1% to +15.5% against sales -6.5%) and World Cup sell-in. Nike says aged Sportswear "sold-through below expectations" (Q1 FY27 remarks p. 3, Nike release).
- **The conflict:** a -$16M residual on *shipments* says nothing about *sell-through*. If NA shipments ran ahead of sell-through, the true demand residual is negative and masked by fill. Also, the -$200M Dunk figure is global and overlaps the GC -$243M; the note admits "overlap ignored", so the -$16M is not a measurement. Row 17 should be "unresolved: shipment residual about 0, sell-through residual unknown and probably negative".

### A6. FY25 China-specific footwear is overstated in footwear_decline (vs gc_decline)
- **footwear_decline.md, Section 2.9:** "China-specific weakness about -253", assumed as "35% of GC's CN footwear decline ... following gc_decline section 0 item 2".
- **gc_decline.md, Sections 1 (row 2) and 2.8:** FY25 GC **footwear** was *not* China-specific ("FY25 GC footwear -13% = NA footwear -13%"). The 35% China-specific share applies to total GC revenue, not footwear.
- **Recomputed (my arithmetic, region inputs from footwear_decline Section 2.3):** revenue-weighted ex-GC footwear FY25 was -10.52% currency-neutral against GC -13%. The China-specific excess is **about -$138M**, not -$253M. The unexplained residual in Section 2.9 grows from -$423M to **about -$537M**. That strengthens footwear_decline's own point that a non-classic, non-China FY25 decline existed.

### A7. Reserve balance changes used as revenue effects in three notes, but called "not the revenue effect" in a fourth
- **direct_decline.md T12:** "A balance change is not the same as the revenue effect."
- **footwear_decline.md (2.9, 2.10)** and **concentration.md (Table F)** treat the balance change as the revenue swing: +$552M build in FY25, -$245M release in FY26, a +$797M swing, of which about +$508M is footwear.
- **na_wholesale.md, row 14:** "ruled out for FY26" using FY26 10-K p. 47 ("variances ... not material"). It also uses the **May 2025 to Aug 2026** decline of $346M (23.5% of the FY26 NA gain) as if it were FY26. The FY26 decline (May 31, 2025 to May 31, 2026) is $245M, **16.6%** (my arithmetic; FY26 10-K p. 84).
- **What is consistent:** p. 47 rules out *estimate reversals*. It does not rule out lower gross provisions, which is a real YoY revenue lift (lapping). So footwear's +$508M "accounting, not demand" slice and na_wholesale's "lapping" are the same dollars. Neither note can size the flow, because provisions and usage are not disclosed. All three should carry direct_decline's caveat and label the swing "balance proxy, upper bound on direction only".

### A8. Stale cross-reference: direct_decline cites revision 2 markdown figures
- **direct_decline.md** T9 and verdict 11 cite the FY25 all-in-Direct bound as "$1,979M (all in Direct with a +100 bps pricing offset)".
- **markdown_depth.md rev 3, Table D:** "$2,035M ... 9.8% (was 9.5% in revision 2)". The $1,979M appears only in `markdown_depth.rev2.bak.md` line 97.
- **Fix:** $2,035M. The FY25 range "19% to 79% of the FY25 digital decline" needs recomputing on $2,035M.

### A9. Small numeric mismatches (do not change verdicts)
- **GC digital estimate.** gc_decline 2.9: FY24 about $1,231M to FY26 about $656M (-$575M). direct_decline T3: $1,231M to $682M currency-neutral (-$549M). The two use the same 0.375 weight but different bases (reported vs cn), and neither note says so. A $26M gap (my arithmetic).
- **Dick's scale check.** na_wholesale: Nike purchases at Dick's "at most $2,154M" (25% x COGS). concentration Table D includes the FY2024 inventory build of $501M (Dick's FY2025 10-K p. 60, filing): range $2,084M to $2,280M (my arithmetic). Five percent growth on $2,280M is $114M, **7.7%** of the FY26 NA gain, not 7.3%. The conclusion stands.
- **Converse IEEPA.** region_gm_decline: Converse IEEPA "nets to about zero within FY26". na_margin shows the refund minus FY26 expense = E25 + I26 >= 0. The same identity applies to Converse's $21M, so Converse FY26 GM is overstated by zero or a little. It is not neutral.
- **Direct/wholesale gross-margin gap.** region_gm_decline assumes 15 to 25 pts. na_margin uses 21.7 to 25.7 pts (note 09). The ranges should be harmonised.
- **Channel premium in na_margin.** The 1.654x FY24 ratio is applied to the FY24 to FY26 shift. markdown_depth bounds the FY25 ratio at about 1.49 to 1.56 (all-in-Direct rows), so na_margin's -3.25% channel-mix price effect is an upper bound. Its "+0.8% residual price" is then a lower bound.

### A10. Checked and **not** a contradiction
- Q4 FY26 gross margin. markdown_depth quotes "Gross margin was 42.9%, up 20 basis points ... including a 210 basis point benefit". na_margin and region_gm quote "49.2%, up 890 ... 900 basis point benefit ... Excluding this benefit ... 40.2%". Both appear in `dl/transcripts/Q4FY26.txt`: the first is the **full year**, the second **Q4**. markdown_depth should label its quote "full-year statement in the Q4 FY26 remarks".
- These agree across notes: NA wholesale and Direct dollars (T1 sums match na_margin and concentration: FY26 NA 20,511 = 11,958 + 8,553); Direct share 48.6% to 41.7%; Foot Locker Nike 59%; sales-related reserves ($994M, $1,282M, $1,834M, $1,589M); FY25 price residual (-$586M vs -$587M); the classics Q4 FY24 cap (about $3.3B) in direct_decline and footwear_decline; and the withdrawn ">$4B from peak" bound (both notes withdrew it).

---

## (b) Conclusions resting on snippet-only, secondary, stale or opinion inputs

Only items where a verdict or a headline number depends on the weak input. Snippets used only as context are omitted.

| Note | Conclusion | Weak input | Why it matters | What would firm it up |
|---|---|---|---|---|
| na_wholesale | The Foot Locker build is "mostly Nike" product | **Inference** (Nike's "oversupplying" admission; Foot Locker's retro dependence). Dick's does not split inventory by brand | This is the core fill claim for Q1 FY27 | Dick's Q2 2026 10-Q segment note (accession 0001089063-26-000036; the saved copies are error pages); Dick's Q3 2026 Foot Locker inventory |
| na_wholesale | Retailer inventory dollars are not tariff-inflated | **Opinion:** "Landed tariff cost per unit at Aug 2026 was therefore not above Aug 2025" | Contradicted in direction by Nike's own Q4 FY26 guide (10% to July, then 15%; Nike release). It is not load-bearing only because the inventory/COGS test cancels a common cost rise | Keep the inventory/COGS test as the evidence; drop or soften the opinion |
| na_wholesale | Athletic specialty sell-through weak | JD NA LFL -6.8% (**secondary**, AJ Bell); Foot Locker Q2 2025 NA comp +1.4% and Academy Q2 2026 comp -0.4% (**snippet only**, shown in tables) | Supports "no" for athletic specialty in row 8 | JD trading update PDF (download failed); Academy Q2 2026 10-Q |
| concentration | JD was the FY24 #3, so JD plus Hibbett adds +3.0 to 4.2 pts (largest identified driver) | Finish Line FY2018 10-K (**stale**: before the JD takeover, 66%) and LBC "45%" (**secondary**). The calibration f is solved under each candidate #3 and fits both (0.83 to 0.98 vs 0.91 to 1.01), so f does not discriminate. The 30 to 34% threshold vs a 2018 share does | The single largest within-wholesale driver rests on an eight-year-old vendor share | A current JD NA vendor share (JD annual report gives none); Nike's customer aggregation rule |
| direct_decline | Of the digital-specific $2.6B to $2.9B, part is "a sneaker-launch and hype audience whose demand fell faster on Nike's own platform" | **Opinion** with no data (no SNKRS metrics; resale data not found per gc_decline) | It appears in short-answer item 5 as an explanation | Label it as a hypothesis. App or SNKRS active users (Sensor Tower is snippet only here) |
| footwear_decline | "Share loss, not a shrinking category" | Peer footwear sum "roughly $4B or more" with **no currency conversion (opinion)**; peer windows are mismatched | The verdict is probably right but unproven as stated | Convert On (CHF) and adidas (EUR) at period-average ECB rates in code. ECB data are already downloaded under `dl/r3/fx/` |
| footwear_decline | FY25 classics scenario shape | Constraint (d) "rate greater than the first quarter" from fool.com (**secondary**); FY25 rate capped at 25% by **assumption** ("Nike would likely have said more than 25%") | Sets the $1.4B to $3.6B FY25 classics range, and with it the non-classic residual | Nike's own Q2 FY25 remarks PDF (404 at s1.q4cdn.com; try the Nike IR events page) |
| na_margin | No-new-tariff FY26 NA GM about 45.8% (+143 bps vs FY24) | Q4 tariff comes from **guidance**, not actuals; Q1 is a floor; the IEEPA cut-off date is from GHY via a WebFetch summary (**secondary**, wording "close to") | It is the headline answer to "why NA margin rose" | Actual Q4 FY26 NA tariff expense (call Q&A or Q2 FY27 10-Q); CBP or Federal Register notice for the Feb 24, 2026 cut-off |
| na_margin | Nike's "underlying" excludes tariffs, so -29 bps and "improved" are consistent | **Opinion** from Nike's Q3 usage | Reconciles a stated conflict | Q4 FY26 call Q&A text |
| gc_decline | Nike share of the "total market" 14.0% to 11.2% | Anta's claim citing "a global authoritative institution" (**opinion**) | Already labelled crude; not load-bearing | Euromonitor or Momentum data |
| gc_decline | Destination of lost share includes Amer (+43.4%) and On | Amer: **secondary** (FashionUnited); On APAC +96.4%: **snippet only** | Row 17 "supported" partly rests on these | Amer 6-K Greater China line; On 20-F regional table |
| region_gm_decline | FX shares (EMEA about two-thirds, GC half to three-quarters) | **Model**: proxy standard rates with a pass-through fitted to Nike's company-level FX. Disclosed by the note | Defensible as a bounded estimate, not a measurement | Nike segment standard-rate impact in bps (Investor Day) |
| markdown_depth | FY25 offset "most likely 50 to 100 bps"; "most likely FY2025 range 3.4% to 9.8%" | **Opinion** | The "ruled out at 15%" verdict uses Nike's "low single-digit" statement (Nike release), not this opinion, so the verdict survives | n/a |

No note uses a snippet-only item as the *sole* basis for a "supported" or "ruled out" verdict. The weakest load-bearing items are the **inferred Nike share of the Foot Locker build** (na_wholesale) and the **stale JD vendor share** (concentration).

---

## (c) The single most important unresolved question for the pitch

**Question:** Of Nike North America's wholesale growth from FY26 to Q1 FY27 (+$1,474M in FY26; +$245M in Q1 FY27), how much was consumer sell-through, and how much was inventory placed into the top three U.S. accounts (Dick's with Foot Locker, JD with Hibbett, and #3) that must now be worked down in Q2 to Q4 FY27?

**Why this one:**
1. NA is the only region that grew in FY26 (+5% currency-neutral; FY26 10-K p. 37, filing). The other big questions are either settled in direction or less important for the pitch. GC is share loss in sell-through (gc_decline). Direct is mostly digital units (direct_decline). The NA gross margin story is cost per unit plus tariffs (na_margin).
2. The notes, read together, point at a concentration of growth in the accounts where fill shows up:
   - Top-3 U.S. customer dollars rose by **$772M to $1,173M** FY25 to FY26, so non-top-3 NA wholesale rose by only **$301M to $702M** of the $1,474M (my arithmetic, ±0.5 pt bands on the 25% and 29% filing figures; concentration.md Table A). na_wholesale never uses this cap. New doors, Amazon, women's doors and running specialty all sit inside the non-top-3 slice unless one of them is the new #3.
   - In the same accounts, sell-through was mixed: Foot Locker proforma comps -3.6% and inventory +14.1% to +15.5% at Aug 1, 2026 (Dick's Q2 2026 release; my arithmetic in na_wholesale); DICK'S Business comps +4.9% with inventory in line (company release).
   - Nike itself says "aged ... Sportswear footwear sold-through below expectations", "oversupplying our iconic retro product" and "North America will feel the biggest impact" (Q1 FY27 remarks pp. 3 to 5, Nike release). It flags a "higher comparison of North America sell-in activities" in Q2 FY27 (p. 13).
3. The answer separates the two halves of the repo's thesis question (REPORT.md: execution that new leadership can fix, versus a structural problem). If NA growth was mostly sell-through (Running, Basketball), the turnaround is real and the problem is GC plus Sportswear. If it was largely fill plus one-off World Cup and lapping, FY26's "recovery" was borrowed from FY27, and FY27 NA wholesale should decline.

**What remains open in the notes:**
- Nike's share of the Foot Locker build (inference only).
- The size of the World Cup sell-in.
- How the $954M of FY26 NA wholesale above FY24 splits among new doors, fill, liquidation and channel shift. Channel shift is about $324M at wholesale-equivalent value in FY26 (my arithmetic: $535M x 0.605).

**Exact data that would resolve it, in order of availability:**
1. **Nike Q2 FY27 10-Q** (quarter to Nov 30, 2026; due late December 2026). NA wholesale dollars vs Q2 FY26's $3,550M; NA footwear units and ASP bullets; sales-related reserves vs $1,488M at Aug 31, 2026; any NA "marketplace management" language. **Test:** if NA wholesale falls by more than the roughly 400 bps company-wide lap Nike guided (which it says also includes EMEA Cyber Week) while DICK'S Business comps stay positive, the Q2 FY26 and Q1 FY27 excess was sell-in.
2. **Dick's Q3 2026 release and 10-Q** (quarter to Oct 31, 2026; early December 2026). Foot Locker segment inventory vs $1,822M to $1,850M a year earlier (na_wholesale T4a) and Foot Locker comps. **Test:** Foot Locker inventory falling while its comps stay negative means Nike sell-in to Foot Locker is being cut, which confirms fill. Also retry the **Dick's Q2 2026 10-Q** (accession 0001089063-26-000036) for any brand or category inventory note.
3. **Nike Investor Day (November 2026).** NA partner weeks of supply, the new-vs-existing account split, Amazon and value-channel revenue. This would directly split the $954M.
4. **Circana Retail Tracking Service** U.S. athletic footwear point-of-sale for the Nike and Jordan brands by channel (sporting goods vs athletic specialty), June 2025 to August 2026, against Nike NA wholesale shipments over the same months. This is the only direct sell-through series. It is paid data; no openable public source was found in this sweep.
5. **JD Sports half-year report** for the 26 weeks to August 1, 2026, if published (not checked in this sweep). North America inventory and any brand-concentration statement, to test the JD+Hibbett account the same way as Foot Locker.

---

## Short list of required edits to the notes (for whoever merges them)

1. na_wholesale row 11: replace the cause with concentration.md's bridge (A1).
2. gc_decline bottom line 5 and 2.7: NA benchmark ex-refund, -5.7 pp (A2); row 9 margin verdict (A3); cite region_gm for the FX vs obsolescence split.
3. na_wholesale: channel-shift shares at 0.605 (22% FY26, 34% Q1 FY27); anchor T6's r on 1.654 (A4); FY26 reserve decline $245M, not $346M (A7); add the non-top-3 cap of $301M to $702M (c).
4. footwear_decline: row 17 to "unresolved"; China-specific FY25 footwear about -$138M, residual about -$537M (A5, A6); convert peer currencies.
5. direct_decline: $2,035M, not $1,979M (A8); label the "hype audience" line as a hypothesis.
6. footwear_decline, concentration: add the balance-is-not-flow caveat to the reserve proxies (A7).
7. region_gm_decline: Converse IEEPA "zero or slightly favourable", not "about zero" (A9).
8. markdown_depth: label the 42.9% quote as full-year (A10).
