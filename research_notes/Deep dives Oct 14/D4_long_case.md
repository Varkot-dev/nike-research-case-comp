# D4: The best long case, what Nike must show at Investor Day, and the judge Q&A for our short

Prepared 2026-10-14 (session 01UTnW4B3cubTQp4NYZ2xN8G). Stock $35.35 (Oct 12 close). Submission Nov 1, Investor Day Nov 16 to 17, finals Nov 19.

Purpose: build the strongest long case the data allows, so that the short pitch survives a judge who holds it. Nothing here changes the recommendation. It stress-tests it.

## Tags and how this note was checked

- **OPENED**: I read the source myself in this session. Only two things qualify: `data/nike_filing_facts.csv` (each row cites a filing and printed page; I did not re-open the SEC document behind each row) and the Yahoo v8 chart API (fetched 2026-10-14, price series for SBUX, ADS.DE, UAA, LULU).
- **SNIPPET**: seen only as a search summary or as a quote in another repo note that was itself a snippet.
- **DERIVED**: my own arithmetic on the cited figures. Method is shown inline.
- **REPO**: a number taken from an existing repo note that carries its own citation. I did not re-open its source. Where it matters I say which note.
- Opinions (analysts, management) are quoted only as labelled opinion and are never the explanation.
- Rule check: no em-dashes or en-dashes; no email address was used in any request (Yahoo requests carried a generic browser user-agent only).

Inputs read in full or in part: CLAUDE.md, RESEARCH_MAP.md, `Long or short cruxes/00_SCOREBOARD.md`, `expectations_gap.md`, `risk_tariffs.md`, `risk_history_margin.md`, `earnings_calls_analysis.md`, `positioning_valuation_history.md`, `Thesis decision/01_ruling.md`, `advocate_long_fixable.md`, `advocate_long_peak_pessimism.md` (including both red teams), `dig_1` to `dig_5`, and `slides/pptx/build_deck.js`. D1 (FY28 bridge), D5 (valuation), D6 (dividend) and D7 (Investor Day precedents) are being written by other sessions and were not available. Where this note overlaps them I say so and mark my numbers provisional.

## 0. Bottom line

1. The long case is not "Nike is cheap". The repo's own reverse DCF and peer table kill that. The strongest long case is narrower: **the FY27 guide has a built-in H2 margin step-down that sits oddly against Q1's actual operating trend, and FY28 consensus is reachable from identifiable, dated items.** If you hold that view, FY28 EPS of about $1.65 is a fair number, not a stretch, and the "FY28 gap" that carries our short shrinks to roughly $0.00 to $0.27 (section 1, argument 3).
2. **The weakest part of our short is the link from "FY28 EPS slightly below consensus" to "the stock falls".** The stock did not follow the sell-side cut (FY27 EPS -25%, stock -3.6% on day 1, back to the pre-print close within 7 sessions), buy-side expectations were already near $1.50, and the options market prices only a 3.6% Investor Day move. Our variant FY28 range ($1.38 to $1.53) is roughly where the buy side already is. Section 4 explains what evidence would fix this.
3. **Investor Day probability (subjective, grounded in section 2):** about 8% that Nike delivers what the long needs, about 50% that it confirms the short, about 42% mixed. Nike giving no numeric FY28 EPS at all is a coin flip (about 50%), and our pre-registered rule does not say how to score silence. Fix that before Nov 1.
4. **Three facts a judge can use against us that the deck does not yet answer** (details in section 3): Q1 FY27 EBIT was flat ($907M vs $904M) on revenue down $507M; the "14 of 14 guides" statistic includes a Q1 FY27 result that was below the midpoint and missed LSEG; and tariff relief plus Pace plus modest revenue growth add up to roughly the $700M of FY28 EBIT growth that consensus needs.

---

## 1. The three strongest long arguments

Common base data (all DERIVED from `data/nike_filing_facts.csv`, filing and page cited in the CSV; REPO-CSV below):

| Item | FY24 | FY25 | FY26 | Q1 FY26 | Q1 FY27 |
|---|---|---|---|---|---|
| Revenue ($M) | 51,362 | 46,309 | 46,398 | 11,720 | 11,213 |
| Gross margin | 44.56% | 42.73% | 42.91% | 42.2% | 42.8% |
| Demand creation, % revenue | 8.34% | 10.13% | 10.25% | 10.14% | 11.17% |
| Operating overhead, % revenue | 23.93% | 24.62% | 24.48% | 24.13% | 23.70% |
| EBIT ($M) | 6,539 | 3,778 | 3,850 | 904 | 907 |
| EBIT margin | 12.73% | 8.16% | 8.30% | 7.71% | 8.09% |

FY26 includes a one-time $986M IEEPA tariff recovery (10-K p.30, CSV). Ex-refund, FY26 gross margin is 40.79% and EBIT is $2,864M, a 6.17% margin. Every "recovery from 8.3%" statement in the deck and in this note's long arguments should be read against 6.2%, not 8.3%, on a like-for-like basis. This cuts both ways: the starting point is lower than the headline (bad for the long), but the FY27 consensus margin of 5.7% is then only about 50 bps below ex-refund FY26 (good for the long, because it means the "decline" in the guide is mostly a lapped cost, not new damage).

FY24 to FY26 EBIT margin bridge, in points of revenue (DERIVED): gross margin -1.65, demand creation -1.91, operating overhead -0.55, other income -0.33, total -4.43 (12.73% to 8.30%). Ex-refund the gross margin line is -3.77 and the total is -6.56.

### Long argument 1: The revenue decline is concentrated in two businesses plus one lap, and the base for FY28 is mechanically easier

**Claim.** After Q1 FY27, 86% of the net revenue decline is Greater China and Converse. Outside them the guide-implied FY27 decline is about -3% to -6%, a rate that is already smaller than the Nike-wide headline, and a FY28 consensus of +1.1% revenue needs only low single-digit growth outside two shrinking lines.

**Decomposition of Q1 FY27 (revenue -$507M, -4.3%; DERIVED, CSV, 10-Q p.25):**

| Driver | Q1 FY27 | Q1 FY26 | Change $M | Change % | Share of net -$507M | Share of gross declines (-$620M) |
|---|---|---|---|---|---|---|
| Geography: Greater China | 1,180 | 1,512 | -332 | -22.0% reported (-26% c-n) | 65% | 54% |
| Geography: Converse | 263 | 366 | -103 | -28.1% | 20% | 17% |
| Geography: EMEA | 3,176 | 3,331 | -155 | -4.7% (-5% c-n per REPO) | 31% | 25% |
| Geography: APLA | 1,463 | 1,490 | -27 | -1.8% | 5% | 4% |
| Geography: North America | 5,127 | 5,020 | +107 | +2.1% | -21% | n/a |
| Channel: NIKE Direct | 4,142 | 4,514 | -372 | -8.2% | 73% | n/a |
| Channel: wholesale | 6,804 | 6,839 | -35 | -0.5% | 7% | n/a |
| Product: footwear | 6,951 | 7,410 | -459 | -6.2% (units -5% per 10-Q p.23, so ASP/mix about -1.3% reported) | 91% | n/a |
| Product: apparel | 3,384 | 3,313 | +71 | +2.1% | -14% | n/a |
| Currency | reported -4.3% vs c-n about -5% (release, quoted in `dig_2.md`, REPO) | | about +1 point tailwind | | | |

Units versus price inside China and Converse (10-Q pp.28, 31, CSV): GC footwear units -26% with ASP per pair flat; Converse units -34% with ASP adding about 6 points. So in both, the decline is units, not price. That matters for the long because a units decline caused by shipping fewer pairs into a channel is the thing Nike controls (see weak spot for how much of it is deliberate).

**Guide arithmetic (DERIVED).** FY26 revenue $46,398M, of which GC $5,847M and Converse $1,174M, leaving $39,377M for "the rest" (including $49M of Global Brand Divisions). Q2 to Q4 FY26 GC was $4,335M and Converse $808M.

| FY27 revenue guide read as | GC Q2 to Q4 at | "Rest of Nike" FY27 change |
|---|---|---|
| -7% | -26% | -3.7% |
| -7% | -35% | -2.7% |
| -8% | -26% | -4.9% |
| -8% | -35% | -3.9% |
| -9% | -26% | -6.1% |
| -9% | -35% | -5.1% |

(Converse Q2 to Q4 held at -28%, GC FY27 comes out at $4.0B to $4.4B and Converse at about $0.85B.) For comparison, the deck's slide 5 shows NIKE Brand outside Greater China at -2.6% to -7.8% for Q2 to Q4. Consistent.

**FY28 consensus reachability (DERIVED).** Consensus FY28 revenue is $43,645M, +1.1% on FY27 $43,152M (Yahoo and MarketScreener, REPO `expectations_gap.md`). Suppose GC and Converse are flat in FY28 at the FY27 levels above ($4.2B and $0.85B) and the rest of Nike grows 1.5% to 2.0% off about $37.7B: that gives $43.4B to $43.6B. So the consensus does not need a heroic rebound. It needs the two shrinking lines to stop shrinking and the rest to grow about 2%.

**The long's best sentence.** "Consensus FY28 revenue is the answer to one question: do China and Converse stop falling after the Jan 1, 2027 partner-online exit? Everything else only has to stop declining."

**Alternatives considered and how they fare**

| Alternative explanation of Q1 | Test | Result |
|---|---|---|
| Decline is spreading beyond the two lines | EMEA is 25% of gross declines (-$155M, Digital -26% per REPO red team) and NIKE Brand outside GC and NA fell 3.8% reported | Survives partly. The "86%" is a net figure. Gross, GC plus Converse is 70.5%. Use 70%, not 86%. |
| China is a channel decision | Units -26% with flat ASP; Nike-owned store sales -14%; Direct (not touched by the Jan 1 exit) -18% c-n, Digital -28% (10-Q p.28, REPO `dig_3.md`) | Ruled against the long. The deliberate part of the GC decline is estimated at 1 to 10 of the 26 points (REPO `dig_3.md`). Do not argue "channel" in front of judges. |
| Converse is deliberate | Converse revenue -52% FY23 to FY26, units -34% in Q1 FY27, demand creation cut 39% in FY26 (REPO) | Ruled against the long. The cut followed the collapse. |
| Currency | +1 point tailwind, so c-n is worse than reported | Does not help the long. |
| Tariff or macro | NA grew while tariffs were highest; revenue decline began Q1 FY25, eight months before 2025 tariffs (REPO `advocate_long_fixable.md`) | Ruled out as a cause of revenue, relevant to margin only. |

**Honest weak spot.** The long needs GC and Converse to flatten in FY28. Nike's own wording is that pressure on reported revenue continues "for the remainder of fiscal '27 and into '28" and the Jan 1, 2027 exit removes about $743M a year of partner-online revenue (12.7% of FY26 GC revenue, REPO `investigations/02`) before any recapture. If GC falls 12% and Converse 10% in FY28 while the rest grows 1%, FY28 revenue is about $42.5B, -1.5% (DERIVED). That is the short's scenario and it uses only Nike's own wording.

### Long argument 2: The margin bridge is mostly price-and-cost items that lap or reverse, not volume loss

**Claim.** Of the 4.4-point EBIT margin decline from FY24 to FY26, 2.5 points (demand creation 1.9, other income 0.3, mix of items) are spending or non-operating choices, and the FY26 gross margin base contains tariff costs that are lapping out of the comparison in Q2 and Q3 FY27.

**Gross margin bridge in basis points (10-K and 10-Q pages from the CSV; DERIVED sums):**

| Line | FY25 (10-K p.35) | FY26 (10-K p.34) | Q1 FY26 (10-Q p.22) | Q2 FY26 (p.27) | Q3 FY26 (p.30) | Q1 FY27 (10-Q p.23) |
|---|---|---|---|---|---|---|
| Total gross margin change | -190 | +20 | -320 | -300 | n/a (41.5 to 40.2 = -130 by level) | +60 |
| NIKE Brand ASP | -180 | n/a | -250 | -50 | +80 | -30 |
| Product costs excluding tariff | +80 | -20 | n/a | n/a | n/a | +10 |
| Tariff in product cost | n/a | n/a | -100 | -360 | -270 | no separate line |
| Warehousing and logistics | +20 | +20 | +50 | +50 | +20 | +90 |
| FX | -10 | +20 | +30 | +40 | +10 | +40 |
| Other costs, royalties | -90 | +20 | n/a | +40 | +60 | -40 |
| Converse | -20 | -20 | -30 | -20 | -30 | -10 |

(n/a means the CSV carries no row for that cell, not zero.)

What the long reads from it:

1. **Tariff lap.** Q2 FY26 and Q3 FY26 carried -360 and -270 bps of tariff in product cost (CSV). FY26 gross incremental tariff cost was about $1.5B annualized at the Q1 FY26 plan (10-Q p.19, CSV). The rate in force today is about 11.4% blended against about 19% to 20% a year ago (REPO `risk_tariffs.md`, DERIVED there), so roughly $0.36B of year-on-year relief at FY27 volumes (REPO). Q2 FY27 is the first full quarter of lower rate against a -360 bps comparison.
2. **Cost items already moving the right way:** logistics +90 bps in Q1 FY27; Q1 gross margin +60 bps on ASP -30 bps shows cost, not price, did the work (this also means the repair is not full-price driven: concede).
3. **Spending line.** Demand creation went from 8.34% to 10.25% of revenue FY24 to FY26 and was 11.17% in Q1 FY27 (CSV). Each 100 bps of gross margin on $43.6B is $436M, or $0.22 of EPS at a 25% tax rate and 1,484M shares (DERIVED; the repo's earlier $0.22 used 21% tax and 1,481M shares). Halving the 1.9-point demand creation increase is $415M, or $0.21.
4. **Overhead.** Operating overhead dollars fell $931M FY24 to FY26 (12,291 to 11,360, CSV). The 0.55 points of deleverage is revenue falling faster than cost, not cost growing. In Q1 FY27 overhead was 23.70% of revenue against 24.13%, down 43 bps even as revenue fell 4.3% (DERIVED).

**Sensitivity: EBIT and EPS at FY28 revenue of $43,645M (DERIVED, 25% tax, 1,484M shares, no change in net interest):**

| EBIT margin | EBIT $M | Implied EPS | Price at 15x / 18x / 21.5x |
|---|---|---|---|
| 7.3% (consensus) | 3,177 | $1.61 (consensus is $1.646, difference is interest and other) | $24 / $29 / $35 |
| 9.0% | 3,928 | $1.99 | $30 / $36 / $43 |
| 10.0% | 4,364 | $2.21 | $33 / $40 / $48 |
| 12.0% | 5,237 | $2.65 | $40 / $48 / $57 |
| 12.7% (FY24) | 5,542 | $2.80 | $42 / $50 / $60 |

So the line from "the stock is a call on margin" to "each point of margin is $0.22 of EPS and about $4 to $5 of price at 18x to 21x" is the whole debate. A recovery to 10% (FY28 or soon after) is worth $40 at 18x, +13% on today's price. A recovery to FY24's 12.7% is worth +41% at 18x. That is the long's payoff; it is not a screaming bargain.

**Alternatives considered**

| Alternative | Test | Result |
|---|---|---|
| Tariff relief is already in guidance | The Oct 1 guide was built 10 weeks after the lower rates began; the word "tariff" appears zero times on the Oct 1 call (REPO `risk_tariffs.md`, OPENED there) | Probably in the guide. Upside only if the guide used the 15% plan. Not provable (see route log, R1). Treat as a $0.04 to $0.07 FY27 and $0.08 to $0.14 FY28 tail, mid $0.065 and $0.12 (REPO DERIVED). |
| Demand creation is a cost of staying in the game, so it will not fall | Q1 FY27 demand creation 11.2% with revenue still down 4.3%; World Cup timing (REPO `dig_4.md` tested it) | Not ruled out. This is the red team's strongest point against the long: spending rose and revenue did not. The bridge cannot separate choice from necessity. |
| Gross margin is mix-flattered by the refund | Yes in FY26: 900 bps in Q4 FY26 (CSV, release p.1) | Ruled in. Use ex-refund 40.8% as the FY26 base. |
| Gross margin recovery needs full-price ASP, not cost | ASP line -30 bps in Q1 FY27; negative again after +80 in Q3 FY26 | Ruled in for the short: price (ASP) is not repairing. |

**Honest weak spot.** In the quarters shown in the table above the ASP line was positive only once (Q3 FY26, +80 bps). Nike moved its Sportswear and Jordan clean-up date from "end of December 2026" to "beyond fiscal 2027" (FY26 10-K p.30 vs Q1 FY27 10-Q p.20, REPO `dig_4.md`). The cost-driven margin gains are real but are the type that peers can also compete away.

### Long argument 3: The FY27 guide implies an H2 margin step-down that Q1's trend does not support, and the FY28 EBIT growth is fillable by named items

**Claim.** Q1 FY27 EBIT was $907M against $904M on revenue $507M lower, with SG&A down $106M and gross margin up 60 bps. FY27 consensus EBIT ($2,479M, 5.74% margin, MarketScreener, REPO) then requires Q2 to Q4 to run about 70 bps worse than the same quarters last year on an ex-refund basis, even though Q2 and Q3 lap tariff hits of -360 and -270 bps.

**Q1 operating trend (DERIVED, CSV):** revenue -$507M; gross profit -$145M (4,943 to 4,798); SG&A -$106M (4,016 to 3,910, with demand creation +$64M and overhead -$170M); EBIT +$3M.

**H2 implied by FY27 consensus (DERIVED):**

| | Q1 FY27 actual | Q2 to Q4 FY27 consensus | Q2 to Q4 FY26 ex-refund |
|---|---|---|---|
| Revenue $M | 11,213 | 31,754 (11,176 + 10,403 + 10,175) | 34,678 |
| EBIT $M | 907 | 1,572 (769 + 517 + 286, MarketScreener) | 1,960 (990 + 635 + 1,321 - 986) |
| EBIT margin | 8.09% (Q1 FY26 7.71%) | 4.95% | 5.65% |
| Year-on-year change in margin | +38 bps | -70 bps | |

What each result would add if Q2 to Q4 matched Q1's year-on-year margin trend instead (DERIVED, 25% tax, 1,484M shares): flat margin at 5.65% gives EBIT $1,794M (+$222M, +$0.11 EPS); +40 bps as in Q1 gives $1,921M (+$349M, +$0.18 EPS). So FY27 EPS would be about $1.40 to $1.47 against the $1.29 consensus and the $1.15 to $1.35 guide.

Management's stated reasons for the step-down (REPO `expectations_gap.md`, from the Q1 FY27 call, opinion/guide): "EBIT to decline by a greater percentage than revenue", fixed cost deleverage and higher input costs, a Q2 revenue headwind of "approximately 400 basis points" from lapping EMEA Cyber Week and NA sell-in, and "SG&A to remain down year-over-year". The long's reading is that this is the new CFO building a "reasonable and attainable" guide. The check against that reading: Hill-era next-quarter guides were beaten 6 of 7 on revenue (average +2.3 points above the midpoint) and met or beaten on gross margin 7 of 7 (REPO `earnings_calls_analysis.md`); the first result below the midpoint was Q1 FY27 itself (-4.3% vs a -1% to -6% range).

**FY28 EBIT bridge (DERIVED, provisional pending D1).** Consensus EBIT rises from $2,479M (FY27) to $3,179M (FY28), +$700M. Identifiable pieces:

| Piece | Basis | EBIT $M |
|---|---|---|
| Pace savings, FY28 share | $2.5B cumulative through FY31, "majority in FY29 and FY30" (10-Q p.20, CSV); allow $0.5B in FY28, half reinvested | about 250 |
| Tariff gap vs the 15% plan if the guide used 15% | FY28 mid $0.12 EPS x 1,484 / 0.75 | about 237 |
| Revenue +$493M at a gross-margin-less-variable-cost flow-through of 30% | arithmetic, assumption | about 150 |
| Total identified | | about 640 |

This is 91% of the $700M, built from three items with source anchors. The short's counters: the tariff piece is only valid if the guide used 15% (unprovable), Pace has a history of reinvestment and slippage (promise tracker: "begin in fiscal '27 and continue to build through fiscal '28" became "majority in '29 and '30"), and the flow-through on revenue is an assumption. But the long is entitled to say "consensus FY28 is not a stretch, it is a sum of three named items".

**Setup features (labelled).**
- Fact (REPO `expectations_gap.md`, Yahoo/Nasdaq, OPENED there): FY27 consensus is $1.29, above the midpoint of $1.25 by 3%. FY28 consensus fell from $2.22 to $1.65 in 30 days with 24 down revisions in 7 days. Median target $34.40 vs price $35.35.
- Fact: the stock closed on Oct 12 at $35.35, after a low of $33.87 on Oct 2 (OPENED, Yahoo, in `positioning_valuation_history.md`).
- Opinion, labelled: Bernstein (Oct 2, OPENED in `expectations_gap.md`): guidance "roughly 25% below Street expectations", with "not much will change until" Investor Day. Piper: guide "below the firm's sense of buy-side expectations around $1.50" (SNIPPET relay).

**Alternatives considered**

| Alternative | Test | Result |
|---|---|---|
| H2 step-down is real because Q1 was flattered by one-offs | Q1 logistics +90 bps and FX +40 bps drove the +60 bps gross margin; royalties -40, ASP -30 | Not ruled out. If logistics and FX are non-repeating, Q2 to Q4 gross margin starts about 130 bps lower. This is the short's best reply. |
| New CFO is sandbagging | Denton's Pfizer record: guides beaten +45% and +11% (SEC 8-K, OPENED in `expectations_gap.md`); Lowe's FY2019 missed by about 5% | Only half supported. Lowe's is the better analog (retail turnaround). |
| Consensus stale-high rather than low | FY28 highs $3.22 and Telsey earlier $2.05 | Stale highs mean the mean may fall further, which helps the short. |

**Honest weak spot.** Even if the long is right on FY27 and FY28 EPS, the stock needs a margin path to 10% to 12% by FY30 to earn a return. Management has never dated a double-digit EBIT margin return (the FY25 target of "high-teens" EBIT was reaffirmed through Q1 FY24 and came in at 8.2%).

### Where the three long arguments are collectively strong and weak

| Test | Result |
|---|---|
| Do they use Nike's reported numbers only? | Yes (revenue, gross margin bridge, SG&A). |
| Is the diagnosis Nike-specific? | Yes: currency-neutral -10.8% FY24 to FY26 against peers +15.4% (REPO ruling). That supports "self-inflicted" but equally supports "lost share that may not return". |
| Do they require a new fact the market lacks? | No. Bernstein and Jefferies (Buy, $75) already publish versions of arguments 1 and 3 (REPO `advocate_long_fixable.md` red team). So the long is a consensus-shaped bull case. |
| Do they overturn the valuation? | No. At 27.4x FY27 and 21.5x FY28 (peer medians 15.8x and 13.2x on Oct 13, REPO `dig_5.md`), the price already pays for margin recovery. |

---

## 2. What Nike must show at Investor Day (Nov 16 to 17), and how likely it is

**Date source.** Primary: Nike's Q4 FY26 call transcript (Jun 30, 2026), Hill. The Oct 1 call says only "November". No SEC filing carries the date (REPO `dig_5.md`, OPENED there). Cite the transcript, not the "Oct 1 memo" cited in REPORT.md.

### 2.1 Requirements for the stock to work (defined as a sustained re-rating of at least +15% from $35.35, i.e. into the high $30s to low $40s)

Anchor: the reverse DCF says $35.35 pays for 12.7% to 14% EBIT margin by FY31 at a 10% WACC and 11% to 12% at 9% (REPO `dig_1.md`, replicated there to 0.005 points). To move up from here the market needs either a higher FY28 or FY29 EPS or a credible, dated margin target. The table converts that to specific disclosures.

| # | What Nike must show | Why the stock needs it (driver) | Probability Nike delivers it (judgment) | Grounding |
|---|---|---|---|---|
| 1 | FY28 revenue growth, explicitly positive, with GC and Converse floor dates | Consensus FY28 revenue +1.1% rests on China and Converse stopping their fall | 35% | Denton declined twice to say if FY28 revenue turns positive ("we'll come back to it at Investor Day", Q1 FY27 p.25, REPO `earnings_calls_analysis.md`); he also said pressure "probably" bleeds "a little bit into fiscal '28" (opinion/guide). Firm commitments after a hedge are rarer than hedges. |
| 2 | A FY28 EPS or EBIT framework at or above consensus ($1.65, EBIT about $3.2B) | At 21.5x it is a direct price input | 15% | Nike said it would "return to providing full year and long-term guidance at our Investor Day" (Q3 FY26 call, REPO), but a full-year FY28 number is not the same as a long-term algorithm. New CFO has just reset FY27 and has every incentive to leave FY28 loose. |
| 3 | A dated long-term EBIT margin target of 13% or more, with an interim bridge | This is what falsifies Pillar 1 of the short (01_ruling.md) | 8% | Nike's 2021 targets (high-teens EBIT) were missed by more than half (FY25 8.2%). FY26 ex-refund was 6.2%. A 13% target means +6.8 points from the ex-refund base, or +4.7 points from the FY27 consensus 5.7% to 13% in about five years. The probability that a new CFO publishes that after a record guide reset is low. |
| 3b | A dated target of 10% to 12% | At 10% margin and 18x, price is about $40 (section 1, argument 2); at 12% it is about $48 | 40% for 10% or more dated; 20% for 12% or more dated | "Return to double-digit EBIT margins" has been repeated since Q4 FY25 without a date (REPO promise tracker). A five-year algorithm ("promised" per Bernstein, OPENED in `expectations_gap.md`) forces a date. 10% is the natural round number. |
| 4 | Pace scorecard: gross versus net savings by year, with the FY28 amount | $2.5B through FY31 is about $0.5B a year, $0.25 EPS a year at 25% tax (DERIVED); the year it lands decides FY28 | 50% for a table that shows phasing; 20% that it shows more than $0.5B net in FY28 | Management said "majority" lands in FY29 and FY30 (Q1 FY27, REPO). |
| 5 | Gross margin framework for FY28 (bps by driver) including ASP | Each 100 bps is $436M or $0.22 EPS | 45% for a numeric range; 15% for a range implying more than +150 bps | Nike said it was "probably not going to provide guidance specifically for gross margin" on Oct 1 (REPO). |
| 6 | Segment and Performance disclosure (Performance vs Sportswear revenue and growth, NA partner weeks of supply) | Lets the market audit the "$16B Performance growing high single digits" claim | 50% | Hill named Performance on calls; formal disclosure is a new-CFO move but not costly. |
| 7 | Capital return statement (dividend growth policy, buyback) | $1.64 dividend is 121% to 143% of guided EPS; FCF covered 0.91x in FY26 (REPO) | 85% some statement; the November declaration (Nov 14 to 20): token raise 45%, freeze 40%, cut 15% (REPO note 18, not re-opened) | A token raise is already priced; a cut is the historical bottoming trigger in 2 of 5 analogs (VF second cut, adidas; REPO `positioning_valuation_history.md`). Overlaps D6. |

### 2.2 Joint outcomes (subjective; these are judgments, not model outputs)

| Outcome | Definition | Probability |
|---|---|---|
| Long wins | Items 1, 3b (12%+) and 4 (net FY28 above $0.5B) or a FY28 EPS framework at or above $1.65 | 8% |
| Mixed | Positive FY28 revenue framing or a dated 10% to 12% target, but no FY28 EPS, thin gross margin detail | 42% |
| Short confirmed | FY28 framed as another transition year, EPS below $1.50 or no revenue growth, or an undated or sub-10% target | 50% |

Stock-price reading of those outcomes:

| Precedent or evidence | Number | Tag |
|---|---|---|
| Nike Investor Day Oct 14, 2015, day 1 | +2.4% | OPENED (REPO `expectations_gap.md`) |
| Nike Investor Day Oct 25, 2017, day 1 / day 20 / day 60 | +6.3% / +10.6% / +25.7% | OPENED (same) |
| Nike Jun 2021 targets with earnings, day 1 | +15.5% | OPENED (same) |
| Nike full-year guide resets since Dec 2023, day 1 | -11.8%, -20.0%, -6.8%, -15.5%, +4.9%, -3.6% | REPO price file |
| Options-implied Investor Day event move | about 3.6% (Nov 20 straddle 9.5% vs Nov 13 straddle 8.0%, variance difference) | DERIVED (REPO) |

Other companies, using Yahoo closes (OPENED, fetched 2026-10-14); **event dates are from memory, not verified against company releases (the one search I ran returned nothing usable), so treat as illustrative only and as unadjusted for the index.** Reaction measured from the prior close:

| Event (date used) | Day 0 | Day 1 | Day 5 | Day 20 | Day 60 |
|---|---|---|---|---|---|
| Starbucks investor day (2022-09-13) | -1.4% | +4.1% | +1.9% | -3.2% | +14.4% |
| adidas capital markets day (2021-03-10) | +2.8% | +6.2% | +0.9% | -0.9% | +5.1% |
| Under Armour investor day (2016-09-14) | -0.2% | +0.6% | +3.3% | +0.5% | -14.1% |
| Lululemon investor day (2022-04-07) | +2.0% | -0.6% | +5.1% | -14.7% | -24.6% |

Read-across: day-1 moves in this sample are inside +/-6%, in line with the options-implied 3.6% event move; what happens by day 60 depends on subsequent prints, not the event. The long needs more than an Investor Day pop. It needs the Q2 FY27 gross margin print (about Dec 17) to confirm.

Probability that the stock is up 10% or more on a 5-day basis through Nov 19: about 8% (about 2 sigma at the options-implied move, widened for fat tails given Nike's -20% to +15.5% history on resets). Probability it is down 8% or more: about 20% (the three worst Nike resets since Dec 2023 were -11.8%, -20.0%, -15.5%, but those were guide cuts; an Investor Day with a weak FY28 is a cousin of those). These are judgments, not estimates from a model.

### 2.3 A gap in our own decision rules (fix before Nov 1)

Deck slide 11 and the scoreboard say: SHORT if "FY28 EPS framed below about $1.50, or FY28 revenue below flat"; LONG if "FY28 held, plus FY29 margin target above about 9%". Nothing says how to score the case in which Nike gives no FY28 EPS and no FY28 revenue direction, which I put at about 50%. Suggested pre-registration: "No numeric FY28 revenue or EPS from Nike scores as neutral for the stock and as a mild negative for the 'FY28 held' leg, because consensus FY28 will then fall by the sell-side's own assumption of the guide's high end." Also add the 13% falsifier from `01_ruling.md` item 5, which is currently in the speaker notes but not in the table, and note it is inconsistent with the table's 9% FY29 long trigger (the scoreboard uses 9%; the ruling uses 13% as the falsifier of Pillar 1; they test different things, say so).

---

## 3. The 15 hardest judge questions for our short

Format: question, best data-driven answer, honest weak spot. Numbers cited are in sections 0 to 2 or the repo notes named.

**Q1. The stock is 80% below its peak at 1.13x EV/sales and a 4.6% yield. Why short a stock with that little left to fall?**
Answer: Against peers the multiple is not low: EV/sales 1.20x vs 1.18x median and EV/EBITDA 11.3x vs 11.6x (REPO `consensus_and_valuation.md`); the premium is entirely the P/E: 27.4x FY27 and 21.5x FY28 against 15.8x and 13.2x (63% premium, REPO `dig_5.md`). The sales-multiple discount to Nike's own history (1.13x vs 3.06x ten-year mean) is the margin collapse: 37% of the multiple, EBIT margin 11.8% to 8.2% (REPO). The drawdown is from a Nov 2021 price set at a much higher multiple, and about 45% of the log decline is sector de-rating (REPO).
Weak spot: base rates for 75%+ drawdowns are not bearish. Median 12-month excess +15 at 75% depth (brands plus retailers) and company-weighted +15 (REPO `positioning_valuation_history.md` skeptic). Our own risk note says history is a coin flip at best for the short.

**Q2. Consensus has already cut FY27 EPS 25% and FY28 26%. What is your edge versus 35 analysts who just reset?**
Answer: Our edge is narrow and we should say so: FY28 consensus still requires +28% EPS on +1.1% revenue and EBIT margin +160 bps (5.74% to 7.28%, MarketScreener) when Nike's best annual gain FY22 to FY26 was 60 bps (deck slide 4). Our scenarios give $1.38 to $1.53 (flat or -2% FY28 revenue, 35% decremental margin; REPO `expectations_gap.md`), 7% to 16% below.
Weak spot: that range is the buy-side level already ($1.50, Piper SNIPPET). The stock fell only 3.6% on a 25% EPS cut, so a modest FY28 miss may not move the price. And our long case in section 1 identifies roughly $640M of the $700M EBIT step-up needed.

**Q3. Q1 EBIT was flat ($907M vs $904M) on revenue down $507M, with gross margin up 60 bps and SG&A down 2.6%. Isn't operating leverage already turning?**
Answer: Gross margin +60 bps came from logistics +90, FX +40 and product cost +10, offset by ASP -30 and royalties -40 (10-Q p.23, CSV). Price did not contribute. SG&A fell $106M but demand creation rose $64M to 11.2% of revenue, so the cut came from overhead (-$170M), which is the part Pace restructuring is cutting. EBIT flat on lower revenue is cost-out, not demand. And management guides EBIT down more than revenue for FY27.
Weak spot: this is the long's best new fact (argument 3). If logistics and FX repeat, Q2 to Q4 consensus margin is too low. We have no data on what Nike assumed.

**Q4. North America grew five straight quarters (+4.0, +8.8, +3.3, +2.7, +2.1%), footwear units +6% in FY26, NA wholesale at a record $11,958M. Why is that not a recovery?**
Answer: Decomposition (DERIVED from CSV): FY26 NA revenue +$939M (+4.8%) is wholesale +$1,474M and Direct -$535M. About 22% to 34% of the wholesale gain is channel shift from Direct (REPO `investigations/01`, `09`), 35% to 54% only restores FY23 or FY24 levels, and NA revenue is still 4.1% below FY24 with Q1 FY27 5.5% below Q1 FY24 (REPO red team). Growth is decelerating, not accelerating like FY2018. NA EBIT margin ex-refund was 21.5% vs 27.2% in FY24 (DERIVED: (5,376 - 965) / 20,511 against 5,822 / 21,396). NIKE Direct NA -6% in Q1 FY27 (10-Q).
Weak spot: we cannot prove channel fill. NA footwear units ran at or above BEA real spending in the last four quarters, NA inventory was $3,491M, -0.9% y/y (REPO), and the Feng Tay vs US imports test failed (scoreboard Q1). Say "demand is not growing" and not "NA is channel stuffing".

**Q5. Tariffs are 11.4% blended against Nike's 15% plan. Doesn't that hand Nike a margin beat that is not in the numbers?**
Answer: Gap 3.6 points; worth $0.04 to $0.07 FY27 and $0.08 to $0.14 FY28 (REPO `risk_tariffs.md`, DERIVED there). It was a Q1 assumption from Jun 30; the Oct 1 guide was built after the new rate started; the word "tariff" appears zero times on the call. Tails are two-sided: Section 122 refund about $0.14 vs a pending Section 301 "excess capacity" case worth minus $0.26.
Weak spot: we cannot prove the guide used 11.4%. If it used 15%, then FY27 EPS has an unguided $0.04 to $0.07 and FY28 $0.12, which is most of the gap between our FY28 scenarios and consensus. Concede this is the best single reason the short could be wrong on EPS.

**Q6. Under Hill, quarterly guidance was met or beaten 14 of 14 times. Why bet against a management that sandbags?**
Answer: We do not short a Q2 miss; the thesis is FY28 and long-dated promises. Long-dated record: Donahoe era 10 of 13 resolved promises missed, Hill era 2 of 5 missed with 5 pending (2 at risk) (REPO `earnings_calls_analysis.md`, DERIVED there); FY25 targets (high-teens EBIT) came in at 8.2%.
Weak spot: the "14 of 14" statistic is tidy but loose. Q1 FY27 was the first result below the midpoint (-4.3% vs a -1% to -6% range; REPO) and missed LSEG consensus ($11.21B vs $11.32B, REPO `expectations_gap.md`). In the judge's hands, "met or beaten" includes "in range". Also the repo's other notes use "22 of 22" for a broader item list. State the definition and the exact sample (revenue 6 beat, 1 in range, 0 miss; gross margin 4/3/0) on the slide.

**Q7. Short interest is 99.2M shares, up 6.9x from Dec 2023. Isn't this a squeeze waiting to happen?**
Answer: 8.2% of tradable Class B shares, 2.59 to 3.8 days to cover, borrow 0.4% to 0.5%, lendable supply about 5x the short; on Oct 1 and 2, 255M shares traded without a squeeze (deck slide 10 notes, REPO). After record short interest in 27 consumer stocks (2021 to 2026) shorts won 81 of 119 cases at 6 months but about 12% ended more than 25% above the market (REPO). Express with puts or a defined-loss structure.
Weak spot: the same note shows our positioning signals (insiders, 13F, short interest) do not predict returns, so we cannot say positioning argues for or against us. Crowding is a risk to P&L, not a signal. And the 6.9x partly reflects a 71% lower share price: dollar short only doubled, from $1.76B to $3.51B (REPO red team).

**Q8. A 4.6% dividend yield is the carry on your short. If Nike cuts or holds the dividend at Investor Day, who wins?**
Answer: Dividend $1.64 a year is 121% to 143% of guided FY27 adjusted EPS, FCF covered 0.91x in FY26 and was -$64M in Q1 FY27 against $610M of dividends (REPO note 18). Carry on a six-month short is about $0.82 or 2.3% of price (DERIVED: 1.64 x 0.5 / 35.35). A freeze or token raise (85% combined, REPO) is a mild positive and works against us; a cut (15%) is the analog bottoming trigger in VF and adidas.
Weak spot: this is the event inside our window that most clearly helps the long. We should describe a cut as a risk to the short's timing, not a confirmation, and pair the pitch with a stated holding period and carry.

**Q9. Your reverse DCF needs 13.4% to 14.1% margin at 10% WACC, but at 9% only 11% to 12%. Why 10%?**
Answer: Use the WACC-free framing from `dig_1.md`: at $35.35, with 3% growth, the buyer earns about 9.5% a year if margin returns to FY24's 12.7% by FY31, 9.0% at the 10-year average 11.8%, 8.1% at 10%, and 7.2% at today's 8.3%; the market as a whole is priced for about 9.5% (Damodaran). So the price pays for a full recovery and leaves no reward for execution risk. Cost of equity inputs: 20-year Treasury 5.60%, beta 1.04, ERP 5% gives 10.8% and a 10.0% WACC; Damodaran's implied ERP of 4.2% gives 8.9% to 9.0% (REPO `dig_1.md`, OPENED there).
Weak spot: a judge can reach 9% and then our "above FY24" language is wrong. We should say "at least the 10-year average margin" and not "above FY24". The grid is only as good as the 3% terminal revenue CAGR and the 22.5% tax rate.

**Q10. Nike deserves a premium: ROIC history, brand, the largest athletic franchise. Why 63% above peers on P/E?**
Answer: EV/sales and EV/EBITDA are at the peer median with a similar EBITDA margin (Nike 10.7%, adidas 10.2%, VF 9.4%, REPO), so there is no earnings-quality premium visible in the data; the P/E gap reflects depressed Nike FY28 earnings (7.3% EBIT margin) that the market looks through. Calendarized to CY2027 the premium is 79% (REPO `dig_5.md`). adidas, growing about 9%, is at 12.9x FY2.
Weak spot: a P/E premium on trough earnings is normal in a cyclical bottom (REPO long advocate). If Nike's FY28 EPS is understated the premium shrinks. Puma at 88x is excluded as not meaningful. The peer set composition (adidas, Puma, VF, lululemon, On, Deckers and others) drives the median; show the full table.

**Q11. China: Topsports and Pou Sheng closed 26% of doors, but sales per door are rising and some of that is clean-up. Isn't this a managed reset?**
Answer: Four independent facts, not one: Nike guides worse than -26%; footwear units -26% with ASP flat (the decline is units shipped, 25 of 26 points; 10-Q p.28); Nike-owned stores -14%, which the Jan 1 exit does not touch; peer-set share 65% to 50% (2022 to H1 2026, HUNT). The deliberate part is estimated at 1 to 10 points of 26 (REPO `dig_3.md`).
Weak spot: no source counts Nike-only doors (partners also sell adidas), the June 2026 Topsports count is an estimate, the "adidas in the same doors" test is not in any filing as worded (Topsports reports Nike and adidas as one line), and units shipped include deliberate sell-in cuts (REPO `dig_3.md`). Door count is moderate; the strong grade rests on Nike's own guide and the share series.

**Q12. Performance is about $16B and growing high single digits, running added about $1B, and Nike gained 5 points of share in statement running footwear. How can the stock not work?**
Answer: Arithmetic from the guide: if Performance grows 5% to 9%, the other roughly $30B must fall 13% to 18.5% for the FY27 guide to hold (deck slide 5, DERIVED). The Performance category is an unaudited management figure (not in any 10-Q or 10-K segment table). Running volume is real (Dick's reviews +48.6% vs Hoka +21.6%) but price is mixed: 49% of Nike listings are marked down at Running Warehouse vs 10% for Hoka; same-shelf Pegasus $154.95 vs $174.95 (REPO ruling).
Weak spot: the +35.4% run-specialty figure is a year old (12 months to Sep 2025) and measures growth from a channel Nike had exited. The -30 bps ASP line is company-wide and cannot bound running pricing in either direction. The scoreboard grades running neutral. Do not claim running is discount-driven; claim it is real and not enough.

**Q13. Your own history study says a margin-up setup is close to a coin flip, and brand owners with rising margin beat 7 of 12. Why short?**
Answer: Agreed. We rate history neutral to weak short, not a reason (scoreboard Q8). The history that is relevant for Nike specifically: Nike path with next gross margin up beat the S&P 39% at 6 months (13 of 33), median -14 points; with the exact Nike guide shape (next gross margin up, next operating margin down) 6 of 15 at 6 months, median -23 (REPO `risk_history_margin.md`, DERIVED there). Worst point inside 12 months has a median of -30% below entry in the margin-up bucket.
Weak spot: the CI is 25% to 56%; brand owners only with margin rising have median +11 at 6 months on 9 companies; 75%+ drawdown events were +7 of 13. A judge who reads "coin flip" in our appendix will ask why this is a short and not a pass. Answer with: positive expected value is small, risk is skewed (fat right tail), so we propose puts.

**Q14. The next real data (Q2 FY27, about Dec 17) lands after finals, the options price only a 3.6% Investor Day move, and our own research says the bar is low. Why short now?**
Answer: The options price the event as ordinary, we can express with defined-loss structures, and the rule set in advance (section 2) turns Investor Day into the test. Dated pre-registered falsifiers (`01_ruling.md`): dated EBIT target of 13% or more with a bridge, NIKE Brand outside GC flat or up in Q2, ASP line positive for two quarters.
Weak spot: this is a timing weakness. Our first pre-finals test (Nov 16 to 17) is binary and, at 50% silence, could be uninformative. Q2's gross margin comparison (40.6% last year after -360 bps tariff) is a probable beat on the headline. Expect the judges to say "your short is a bet on a number you will not know until after you present".

**Q15. What single result would make you abandon the short, and have you written it down in advance?**
Answer: Yes (`01_ruling.md`, scoreboard section 5): a dated EBIT margin target of 13% or more with an interim bridge at Investor Day; NIKE Brand outside GC flat or up in Q2 FY27; ASP line positive two quarters running; Running Warehouse Nike markdown share toward the 23% store average; nike.com men's sale share below 39% (45.7% now). Add: FY28 EPS framed at or above $1.65 with revenue growth and Pace net savings above $0.5B in FY28.
Weak spot: the deck's long trigger is "FY29 margin target above about 9%" and the ruling's falsifier is "13% or more"; judges will see two numbers. And the FY27 guide itself implies ex-GC decline of 3% to 8% for Q2 to Q4, so the "NIKE Brand ex-GC flat or up in Q2" falsifier is far from the base case and cannot be tested before finals.

---

## 4. Verdict: the weakest part of our short and what would fix it

### 4.1 Ranking (my judgment, with the evidence for each)

| Rank | Component of the short | Strength before this review | Why it is weak | Fix |
|---|---|---|---|---|
| 1 (weakest) | **The causal link from "FY28 EPS slightly below consensus" to "the stock falls"** (deck slide 2: "the stock prices a FY28 recovery that Nike's own guidance does not support") | Neutral/decider in the scoreboard, moderate | (a) The gap is $0.12 to $0.27 (7% to 16%) of EPS (REPO), equal to or smaller than the tariff tail ($0.08 to $0.14) and the Pace year-one amount (about $0.25). (b) The stock did not follow the sell-side cut: -3.6% on a -25% FY27 EPS revision (REPO). (c) Buy-side expectations were already about $1.50 pre-print (Piper, SNIPPET). (d) The price is set by long-run margin (reverse DCF), not FY28 EPS; at 9% WACC the bar is 11% to 12%. (e) My section 1 identifies about $640M of the $700M FY28 EBIT step-up. | Evidence needed in order: see 4.2 |
| 2 | Investor Day as a decisive pre-finals test | Decisive | About 50% probability of silence on FY28; the rule does not score it; options-implied move 3.6%. | Add a silence rule (2.3); add a probability-weighted view to the deck |
| 3 | NA "demand not growing" | Moderate | Units at or above real PCE; NA inventory -0.9%; no direct proof of fill | Weeks-of-supply disclosure at Investor Day; Foot Locker and Dick's Q3 (late Nov, after finals) |
| 4 | Tariff dismissal | Moderate | Unprovable whether guide used 11.4% | Ask at Investor Day; or compare Q2 print to a 15% rate case |
| 5 | China | Strong | Strongest, but door counts are not Nike-only | Topsports interim (Oct 28), Pou Sheng (Nov 12), Tmall Double 11 rankings |

### 4.2 Evidence that would fix the weakest point

1. **A buy-side or whisper FY28 distribution.** If the buy-side median is $1.50 and consensus is $1.65, the short's expected move is the gap between the buy-side and what Nike frames at Investor Day, not the gap versus consensus. Candidate sources: Bloomberg/Visible Alpha crowd data (not free); sell-side notes after Oct 1 (Piper, Bernstein, Goldman, Stifel: SNIPPET only today); a poll in the Investor Day preview notes the week of Nov 9. Obtainable: broker previews 1 to 2 weeks before Nov 16.
2. **A revision-to-return study for Nike itself.** Regress 1-day, 5-day and 60-day excess return on the percentage change in next-year EPS consensus across Nike's last 12 earnings events. Data: `data/nke_daily_prices.csv` plus archived consensus history (Yahoo epsTrend snapshots, Wayback copies of Zacks and MarketBeat). The repo shows 6 resets and day-1 moves of -11.8% to +4.9%; the Oct 1 reset (-3.6%) is the exception. If revisions barely explain day-1 returns, the pitch should lead with the multiple and margin, not the FY28 EPS gap.
3. **A cross-section of "FY28 miss" outcomes.** For turnaround names with consensus +20% or more next-year EPS growth on ~1% revenue, the share that missed next-year consensus by 7% to 16% and the subsequent 6-month excess return. The same universe as `risk_history_margin.md` could be re-run on this variable (the repo built 295 deep-drawdown events). Obtainable from the existing `data/hunt/risk_history/` panel if analyst estimate history can be added (Wayback of Zacks, or EDGAR guidance 8-Ks).
4. **Move the lead from the FY28 EPS gap to the margin bar.** The reverse DCF, the peer-median multiples, and the Q1 EBIT/SG&A decomposition do not depend on FY28 EPS. On slide 2 say: "At $35.35 a buyer needs about 12% to 14% EBIT margin by FY31; consensus has 7.3% in FY28 and Nike's best gain in four years was 60 bps."
5. **Confirm the guide's tariff basis.** Ask at Investor Day (Q&A), or test indirectly: if Q2 FY27 gross margin exceeds 41.9% (the top of the consensus-implied range 41.2% to 41.9% in `expectations_gap.md`), the guide likely used 15%.

### 4.3 Illustrative payoff (judgment, not model output)

| 12-month scenario | Probability (judgment) | FY28 EPS | P/E | Price | Return on a short from $35.35, before 2.3% per six months carry |
|---|---|---|---|---|---|
| Bear: margins settle 8% to 10% | 35% | $1.4 to $1.5 | 15 to 18 | $21 to $27 | +24% to +41% |
| Base: consensus roughly right | 40% | $1.55 to $1.65 | 20 | $31 to $33 | +7% to +12% |
| Bull: Investor Day and Q2 confirm | 25% | $2.0 | 22 | $44 | -24% |

Expected short return about +9% (0.35 x 32.5 + 0.40 x 9.5 - 0.25 x 24 = 9.2), minus about 2.3% carry per six months, so about +7%. This is a coin flip with positive skew when sized and expressed correctly, which matches the scoreboard's "lean SHORT, low to moderate confidence". The bear price range uses the repo's own grid ($20 to $26 at sustained 8% to 10% margins; `01_ruling.md`).

---

## 5. Alternatives ruled out (log)

| Claim a long would make | Evidence that rules it out (or leaves it open) | Status |
|---|---|---|
| "The relapse is 86% two deliberate cuts" | Gross decline share is 70%, EMEA is 25%, and units drove both lines; the cut in Converse followed the collapse | Ruled out as worded; 70% is defensible |
| "China is a channel decision" | Units -26% with flat ASP, Nike-owned stores -14%, Direct and Digital falling | Ruled out |
| "NA profit has turned" | FY26 NA EBIT ex-refund $4,411M, -6.8% on FY25; ex-refund margin 21.5% vs 27.2% FY24; Q1 FY27 +$36M is plausibly tariff relief | Ruled out; Q1 FY27 +3.2% is real but small |
| "Price assumes permanent impairment" | Reverse DCF: needs 11% to 14% margin; P/E premium 63% | Ruled out |
| "Short interest and insiders mark a bottom" | Event studies show no predictive power (scoreboard Q8) | Ruled out as evidence either way |
| "Brand fatigue" | Apparel -2.4% FY24 to FY26; footwear -11.7%, NA apparel record | Not ruled out; footwear is where brand heat lives (red team L5) |
| "Tariff relief will lift FY27 gross margin beyond guidance" | The guide was built after the lower rate; word "tariff" absent from call | Open (route log R1) |
| "Hill beats every guide so Investor Day will be a beat" | Quarterly guides are not long-dated targets; every 2017 and 2021 profit target missed | Ruled out as a base rate |

## 6. Route log for items I leave as open

CLAUDE.md requires five genuinely different routes before reporting "inconclusive". The two items below remain open and are not reported as settled. Routes marked "repo" were tried by earlier sessions and I relied on their records; routes marked "D4" were run in this session. I did not re-run the repo routes.

**R1. Did the Oct 1 FY27 guide use the actual 11.4% tariff rate or the 15% June plan?**

| # | Route | Result |
|---|---|---|
| 1 | Q1 FY27 call transcript text search for "tariff" (repo, `risk_tariffs.md`) | Worked, no answer: zero hits |
| 2 | Q1 FY27 10-Q gross margin bridge (CSV, D4) | Worked, no answer: no tariff line, product costs +10 bps |
| 3 | Q4 FY26 call (Jun 30) for the stated assumption (repo) | Worked: 10% through July then 15%, for the Q1 outlook only |
| 4 | Back-solve Q2 consensus gross margin from EBIT (repo `expectations_gap.md`) | Partial: implies 41.2% to 41.9%, consistent with either |
| 5 | Sell-side notes after Oct 1 mentioning the tariff basis (repo SNIPPET; D4 searched for none) | Blocked: only snippets |
| 6 | Investor Day Q&A and the Q2 FY27 gross margin print (future) | Not yet available |

Needed to settle: management statement at Investor Day, or Q2 gross margin above 41.9%.

**R2. Investor Day precedents for the event reaction**

| # | Route | Result |
|---|---|---|
| 1 | Nike's own investor days via Yahoo (repo, `expectations_gap.md`) | Worked: 2015 and 2017 |
| 2 | Yahoo closes for SBUX, ADS.DE, UAA, LULU around remembered event dates (D4) | Partial: prices fetched, event dates not verified |
| 3 | Web search for Starbucks Sep 13, 2022 and adidas Mar 2021 reaction (D4) | Blocked: results returned unrelated Starbucks pieces |
| 4 | Company IR archives or 8-K for event dates (D4) | Not run (belongs to D7) |
| 5 | Wayback copies of company IR event calendars (D4) | Not run (belongs to D7) |
| 6 | D7 event study (other session) | Pending |

I count R2 as incomplete rather than inconclusive: fewer than five routes were attempted, and the precedent table above must not appear in the deck until D7 verifies the dates and adjusts for the index.

## 7. Must verify before anything here enters the deck or REPORT.md

1. Event dates and index-adjusted returns for the four non-Nike investor days in section 2.2 (D7 owns).
2. Footwear units for NA in FY26: the long advocate records +6% (10-K p.37) while the red team records 5% to 14% at ASP about 5 points lower; I used neither in an argument. Open the FY26 10-K p.37 before using either.
3. The FX translation effect on Q1 FY27 revenue (about +1 point is from a quote in `dig_2.md`, not re-opened).
4. The probabilities in section 2 are my judgment; the dividend odds (45/40/15) come from note 18 which I did not re-open; D6 should confirm.
5. The MarketScreener quarterly EBIT split (769, 517, 286) is a single-source page without an update date (REPO `expectations_gap.md`); the Q2 to Q4 implied-margin step-down in argument 3 depends on it. The full-year consensus EBIT (2,479) is the more reliable number and gives Q2 to Q4 EBIT of 1,572 whichever split is right.
6. Whether "SG&A down y/y" is a statement about the whole FY27 or only the adjusted figure (excludes Pace).

## 8. Files

- This note: `/home/user/nike-research-case-comp/research_notes/Deep dives Oct 14/D4_long_case.md`
- Input data: `/home/user/nike-research-case-comp/data/nike_filing_facts.csv`
- Scratch (Yahoo pulls, not committed): `/tmp/claude-0/-home-user-nike-research-case-comp/2bf9f309-3096-5c65-b9c3-02b984182743/scratchpad/` (SBUX.json, ADS.DE.json, UAA.json, LULU.json)
- Repo changes needed from this note: RESEARCH_MAP.md move D4 to Done (caller does this); consider adding the silence rule (2.3) and the lead-sentence change (4.2 item 4) to `slides/pptx/build_deck.js`. No git commands were run.
