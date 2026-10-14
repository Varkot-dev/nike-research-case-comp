# What 25 Nike earnings calls say about LONG vs SHORT

Written 2026-10-14. Stock $35.35. Covers every Nike call from Q1 FY21 (Sep 2020) to Q1 FY27 (Oct 1, 2026): 25 official transcripts, 852 speaker turns, 167 analyst questions, about 221,000 words. Tags follow the scoreboard: OPENED (we read the source itself), SNIPPET (search summary only), REPO (earlier work in this repo), DERIVED (our arithmetic). Every quote below was checked word for word against the transcript text by script; page numbers are PDF pages of the official transcript.

## 1. Verdict

**Points SHORT, moderate strength, on the FY28 question that decides the pitch. It does not support a SHORT on the next quarterly print.**

- **Management itself puts the pain into FY28 and most of the savings into FY29 to FY30.** On Oct 1, 2026 the new CFO said the drag will "probably bleed in a little bit into fiscal '28" and that Pace savings peak "in '29 and '30". Asked directly whether total revenue turns positive in FY28, he declined to answer until Investor Day. Six months earlier, Nike had said restructuring benefits would "build through fiscal '28". Nothing in 25 calls supports +28% FY28 EPS growth on about +1% revenue.
- **Nike's multi-year promises are unreliable, and the slippage did not stop under Hill.** All four FY25 targets set in June 2021 were missed by wide margins after being reaffirmed up to five times. Under Hill, the "clean marketplace by end of 1H FY26" promise was declared done for North America and EMEA in December 2025, then reversed, and is now pushed "into '28". The "Win Now done by end of calendar 2026" promise vanished from the Q1 FY27 call (0 mentions, against 16 to 24 a call before).
- **But Hill's next-quarter guidance is deliberately low.** It was beaten or met 14 of 14 times, with revenue landing on average 2.3 points above the midpoint. A SHORT that depends on a Q2 FY27 miss (about Dec 17) is fighting that pattern. The new CFO calls his approach "reasonable and attainable" guidance, so Investor Day (Nov 16 to 17) is more likely to set a low FY28 bar than a high one. **A low bar at Investor Day is the SHORT case for the finals (consensus FY28 has to come down). After that, the low bar becomes the LONG case.**
- **Retailers praise Nike's performance product, but they do not show a turn in lifestyle.** DICK'S and Academy name Nike positively 43 times and never negatively across 14 calls, all about running, basketball and new styles. Their complaints, about legacy styles slowing and brands discounting on their own sites, match Nike's own problem areas.

| # | Analysis | Points to | Strength |
|---|---|---|---|
| 1 | Promise tracker | SHORT (long-dated promises); LONG risk on quarterly beats | Moderate |
| 2 | Language trends | SHORT, once two artifacts are removed | Weak to moderate |
| 3 | Analyst Q&A | SHORT (same worries every call, FY28 questions deflected) | Weak |
| 4 | Guidance specificity | SHORT (least detail since the CEO change) | Weak |
| 5 | FY28 clues | SHORT | Moderate |
| 6 | Retailer and adidas calls | NEUTRAL (performance LONG, lifestyle SHORT) | Weak |

**What this changes on the scoreboard:** it supports Q7 (expectations) leaning SHORT on FY28, and it weakens one input to Q8 (history). Q8 assumed that "Nike's own guide implies gross margin flat to up in Q2 and Q3". That framing came from the Q4 FY26 call. In Q1 FY27 the new CFO stopped guiding gross margin ("we're probably not going to provide guidance specifically for gross margin", Q1 FY27 p. 18). He also described FY27 as reflecting "continued pressure on gross margin" (Q1 FY27 p. 11), calling it a "push and pull". Q1 itself was +60 bp (Q1 FY27 10-Q p. 22), so the rising-margin path is now an assumption, not a guide.

## 2. Method

- **Transcripts:** the official PDFs from investors.nike.com (all 25 quarters, OPENED 2026-10-13), converted to text with page markers in `data/hunt/earnings_calls/transcripts/` (README lists every URL). The 25 `t_*.pdf` files in the scratch folder are these same official PDFs, named by Nike's asset id (9384 = Q1 FY21 through 9591 = Q1 FY27). The `Q*.pdf` files are duplicates of them, and the `Q*.txt` files are their `pdftotext -layout` output. No quarter was missing.
- **Scripts** (`data/hunt/earnings_calls/scripts/`, run order in the README): parse speaker turns for four labelling styles, count terms, extract dated promises, code guidance, pair analyst questions with answers, extract FY28 references, and count peer mentions. Hand-coded items (promise outcomes, guidance detail scores, peer tone) are written into the scripts as data, so they can be audited.
- **Eras:** Donahoe era = 17 calls (Q1 FY21 to Q1 FY25). Hill era = 8 calls (Q2 FY25 to Q1 FY27). Elliott Hill became CEO on Oct 14, 2024. Dave Denton replaced Matt Friend as CFO on the Q1 FY27 call.
- **Outcomes** come from `data/nike_filing_facts.csv` (filings, with page) or from later calls.

## 3. Analysis 1: promise tracker

**Stated beforehand.** LONG if dated promises under Hill are being kept on time, especially the end-state ones (clean marketplace, Win Now done, margin path). SHORT if they keep being pushed, or are quietly dropped, the way the Donahoe-era targets were.

**Result** (`promise_tracker.csv`, `promise_events.csv`: 27 promises, 83 dated statements). Negative guides, such as "Direct will not grow", are tracked but not scored.

| Era | Resolved promises | Kept or beat | Kept late | Partly | Missed | Pushed or cut, per promise | Pending |
|---|---|---|---|---|---|---|---|
| Donahoe | 13 | 2 | 1 | 0 | 10 | 0.57 | 1 (Investor Day) |
| Hill | 5 | 2 | 0 | 1 | 2 | 0.80 | 5 (2 at risk) |

**The chains that matter:**

| Promise | Made | What happened | Pushes or cuts | Status |
|---|---|---|---|---|
| FY25 targets: revenue growth high single to low double digits, gross margin "high 40s", EBIT margin "high-teens", China growth low to mid teens | Q4 FY21 p. 11 to 13 | Reaffirmed in Q1 FY22, Q2 FY22, Q3 FY22, Q1 FY23, Q2 FY23 and Q1 FY24 ("we still believe those long-term goals of profitability are achievable", p. 20). The Investor Day meant to reset them was postponed in Q1 FY25 (p. 3). Actual FY25: revenue CAGR +1.0%, gross margin 42.7%, EBIT margin 8.2%, China shrinking (FY25 10-K p. 32; Q4 FY25 release p. 6; DERIVED). | Never formally cut | Missed on all four |
| Clean, healthy marketplace by end of 1H FY26 (Nov 2025) | Q3 FY25 p. 15; Q4 FY25 "on track" | Q2 FY26 p. 8: "In North America and EMEA, which represent almost 3/4 of our business, we have returned to a healthy marketplace." Q3 FY26 p. 16: "exit the fourth quarter with elevated inventory in EMEA". Q4 FY26 p. 10: EMEA inventory "up low double digits". Q1 FY27 p. 3: partners must "work through excess inventory to create a healthy marketplace". Q1 FY27 p. 11: supply cuts pressure revenue "into '28". | 3 | Missed; declared done, then reversed |
| Win Now actions finished by end of calendar 2026 | Q3 FY26 p. 3 | Reaffirmed in Q4 FY26 p. 22 ("on track to sunset"). In Q1 FY27 the term "Win Now" appears 0 times (16 to 24 in each earlier Hill call); the new "Pace" program appears 23 times. | 0 (dropped) | Pending, at risk |
| Revenue for Q4 FY26 to Q2 FY27 down low single digits | Q3 FY26 p. 12 | Q4 FY26: "down low to mid-single digits" (cut). Q1 FY27: FY27 down "high single-digit" (cut again, implying a weaker second half). | 2 | Missed |
| Restructuring benefits "begin in fiscal '27 and continue to build through fiscal '28" | Q3 FY26 p. 9 | Q1 FY27 p. 10: "the majority of the program savings to be realized in fiscal years '29 and '30". | 1 | Pending, at risk |
| Gross margin expansion from Q2 FY27 | Q3 FY26 p. 12 | Q4 FY26 p. 11: moved earlier, to Q1 (raised). Q1 FY27: +60 bp (Q1 FY27 10-Q p. 22). FY27 gross margin no longer guided. | 1 cut | Partly |
| Return to double-digit EBIT margins | Q4 FY25 p. 26 | Repeated in Q1 FY26, Q2 FY26, Q3 FY26 and Q4 FY26, never with a date. Q1 FY27 p. 11: FY27 "EBIT to decline by a greater percentage than revenue". FY26 EBIT margin 8.3% (FY26 10-K p. 31). | 1 | Pending, undated |
| Investor Day with a 5-year algorithm | Q3 FY24 p. 4 ("later this year") | Postponed in Q1 FY25 (p. 3); now set for Nov 16 to 17, 2026. | About 2 years | Pending |
| Kept: Q4 FY25 is the low point | Q3 FY25 p. 15 | Revenue and gross margin declines moderated every quarter after (DERIVED from 10-Qs) | 0 | Kept |
| Kept: wholesale back to growth in FY26 | Q1 FY26 p. 12 | FY26 wholesale +6.1% (FY26 10-K p. 32; FY25 10-K p. 33; DERIVED) | 0 | Beat |

**Next-quarter guidance is the opposite story** (`guidance_scorecard.csv`, 32 guides, actuals from the facts CSV):

| Era | Revenue guides: beat / in range / miss | Gross margin guides: beat / in range / miss | Average revenue vs guide midpoint |
|---|---|---|---|
| Donahoe (from Q4 FY22) | 5 / 3 / 1 | 5 / 2 / 2 | +1.2 pts |
| Hill | 6 / 1 / 0 | 4 / 3 / 0 | +2.3 pts |

Hill-era revenue landed above the midpoint by +2.2, +2.0, +6.1, +2.6, +2.1 and +1.9 points. Then Q1 FY27 came in at -0.8 points, the first result below the midpoint under Hill (-4.3% against a -1% to -6% range; DERIVED). The cushion is thinner, but this is one quarter.

**Alternative explanations checked.** (a) Donahoe-era misses were partly external: Vietnam factory closures (FY22), COVID in China, and freight. Even so, the FY25 targets were reaffirmed through FY24, after those shocks were known. (b) Some Hill-era slippage reflects new tariffs, which management did not control. The clean-marketplace reversal and the FY28 savings shift, however, are internal decisions. (c) Small sample: only 5 resolved Hill promises. We therefore rate this moderate, not strong.

**Verdict: SHORT for anything long-dated (Investor Day targets, FY28), moderate. LONG risk for quarterly prints, because Hill's quarterly guides are built to be beaten.**

## 4. Analysis 2: language trends

**Stated beforehand.** LONG if recovery words (recover, comeback, momentum, inflect, stabilize, return to growth, confident) rise while hedges (headwind, challenging, uncertainty, pressure) fall, in both prepared remarks and Q&A, and for the CEO himself. SHORT if they do not, or if the rise is driven by one word or one speaker.

**Raw result** (`language_trends.csv`, `tone_index.csv`; per 10,000 management words). The naive answer looks LONG. Net tone (upbeat minus hedges) hit its Hill-era highs in Q3 FY26 (56.6) and Q4 FY26 (48.9), and hedges fell from 38.6 (Q1 FY26) to 19.9 (Q1 FY27).

**Two artifacts reverse that:**

1. **"Improve" drives the recovery count.** It is mostly aspirational ("improve operating margins", "improve inventory management"). The new CFO used it 60 times per 10,000 words in Q1 FY27. Without it, recovery words fell to **9 per 10k in Q1 FY27**, from 43 in Q3 FY26 and 36 in Q4 FY26. That is the lowest level since Q4 FY22.
2. **The fall in hedges is one person's vocabulary.** Matt Friend said "headwind" 20 to 50 times per 10k words in every Hill-era call; Denton said it 8 times. Hill himself almost never uses it. Strip the CFO out and there is no hedge decline to read.

| Per 10k words | Hill era, first 6 calls (avg) | Q4 FY26 | Q1 FY27 |
|---|---|---|---|
| Recovery words excluding "improve" (all management) | 27.0 | 36 | **9** |
| "Confident/confidence" (all management) | 13.1 | 12 | **4** |
| "Confident" (Hill only) | 9 to 19 | 13.2 | **4.6** (Hill-era low) |
| "Momentum" (all management) | 13.2 | 12.9 | **4.3** |
| "Pressure" (all management) | 3.4 | 6 | **10** (Hill-era high) |
| China / Jordan / Sportswear mentions | 25.9 / 8.3 / 19.4 | 30 / 8 / 24 | **44 / 24 / 34** |
| Discount / inventory / digital mentions | 24.6 / 23.3 / 45.8 | 22 / 19 / 37 | 7 / 4 / 9 |

**Alternative explanations checked.** (a) The fall in discount, inventory and digital words in Q1 FY27 is **not** evidence of fewer discounts. Denton simply stopped walking through channels and geographies ("NIKE Direct": 0 mentions, against 8 in Q4 FY26), and the 10-Q still names "higher discounts" (scoreboard Q4, REPO). (b) Tariff talk was stripped out in a separate count (sentences mentioning tariffs removed); the Hill-era pattern is unchanged. (c) The CEO-only series shows that the confidence drop is not just the CFO change.

**Verdict: SHORT, weak to moderate.** Clean measures show the most cautious call of the Hill era, and the talk is shifting toward the three problem areas (China, Jordan, Sportswear).

## 5. Analysis 3: analyst Q&A

**Stated beforehand.** LONG if analyst worries rotate (yesterday's issue is resolved and drops out) and answers carry numbers. SHORT if the same worries recur every call and management answers the key ones vaguely or defers them.

**Result** (`qa_pairs.csv`, `qa_topics_by_quarter.csv`; 167 question slots).

- **Unresolved, every call:** China was asked about in 8 of 8 Hill calls (16 of 17 under Donahoe), margins in 8 of 8, and recovery timing in 8 of 8. The share of questions about timing ("when", "how long", "bottom", "path to") doubled, from 20% under Donahoe to 40% under Hill. Capital allocation appeared for the first time in Q1 FY27: Binetti noted that the dividend payout is "over 100%" at the guidance midpoint (Q1 FY27 p. 24).
- **Who asks:** Matthew Boss (20 of 25 calls), Bob Drbul (18), Michael Binetti (17), Brooke Roach (11), Adrienne Yih (11). Binetti asked the FY28 revenue question in Q1 FY27, and Boss asked about "pain before gain" into FY28.
- **Deflections:** 3 of 109 questions under Donahoe, 7 of 58 under Hill, and all 7 came in the last two calls (Q4 FY26: 3 of 7 questions, Q1 FY27: 4 of 8, each handled at least partly by deferral). The key ones were FY28 revenue positivity ("hold that question", Q1 FY27 p. 25), Q2 revenue and FY27 gross margin (p. 18), regional guidance (p. 21), whether FY28 is a "normal" year (Q4 FY26 p. 21 to 22, answered "There's been nothing normal about this"), and the China timeline (Q2 FY26 p. 24: "tough to put an exact date on it").
- **Specificity of answers did not fall overall:** 0.92 quantitative tokens per 100 words under Hill against 1.00 under Donahoe, and 88% against 91% of answers containing at least one number. Median answer length is 461 against 492 words.

**Alternative explanation checked.** Deferring to an Investor Day that is weeks away is normal, and the pre-Investor Day call in Q4 FY24 also deferred. So deflections are only weak evidence. The pattern that matters is what was deflected: every FY28 and timeline question.

**Verdict: SHORT, weak.**

## 6. Analysis 4: guidance specificity

**Stated beforehand.** LONG if guidance holds or adds detail (management can see the business). SHORT if detail is withdrawn, especially on the metric bulls depend on (gross margin).

**Result** (`guidance_specificity.csv`; each call's outlook section was read in full and hand-scored on 11 fields; 3 = numeric, 2 = size bucket, 1 = direction only, 0 = not given):

| Call | Detail score | Numeric fields | Next-quarter items given |
|---|---|---|---|
| Donahoe-era average | 14.3 | 2.1 | 2.2 |
| Q2 FY25 (Hill's first call) | 10 | 2 | 4 |
| Q4 FY25, Q1 FY26, Q3 FY26 (Hill-era highs) | 21 | 3 to 4 | 4 |
| Q4 FY26 | 13 | 0 | 3 |
| **Q1 FY27** | **10** | **1** | **1** |

In Q1 FY27, Nike dropped the next-quarter gross margin guide it had given in every call since Q4 FY23, and replaced the next-quarter revenue guide with a single 400 bp Q2 headwind (p. 11). It also gave no next-quarter SG&A or other-income guide. It also dropped the gross margin guide for the year ("probably not going to provide", p. 18), geography detail ("we're not going to give guidance, obviously, by region", p. 21) and any tariff assumption (the word "tariff" appears 0 times, against 16 in Q4 FY26). It added the first explicit EPS range in 25 calls: FY27 adjusted EPS $1.15 to $1.35, excluding about $0.15 of Pace costs (p. 12).

**Alternative explanations checked.** (a) A new CFO often changes the guidance style, and Denton framed it as a move to full-year guidance (p. 11). (b) Detail also dropped at the two earlier transitions: Q1 FY25 withdrew the full-year guide, and Q2 FY25 scored 10. (c) Investor Day is six weeks away. A cleaner test is which items were dropped: the gross margin numbers that the bull case and our scoreboard Q8 rely on.

**Verdict: SHORT, weak.** It is consistent with a reset, not proof of one.

## 7. Analysis 5: FY28 clues

**Stated beforehand.** LONG if management signals FY28 as a year of revenue growth and margin recovery, consistent with consensus FY28 EPS of $1.65 (+28% on about +1% revenue; scoreboard, Yahoo 2026-10-14, REPO). SHORT if it places revenue pressure or the bulk of savings beyond FY28, or refuses to frame FY28.

**Everything said about FY28 and beyond** (`fy28_clues.csv`, 57 sentences since Q3 FY24):

| Call, page | Who | What was said | Reads |
|---|---|---|---|
| Q3 FY26 p. 9 | Friend | Restructuring benefits "begin in fiscal '27 and continue to build through fiscal '28" | LONG at the time |
| Q3 FY26 p. 12 | Friend | Q1 FY27 to be "the final quarter where higher tariffs continue to be a material year-over-year headwind to gross margin" | LONG for gross margin |
| Q4 FY26 p. 21 to 22 | Sherman / Hill | Is FY28 "the first 'normal' year"? Answer: "There's been nothing normal about this" ... more at Investor Day | Avoided |
| Q4 FY26 p. 23 | Friend | FY26 actions "drive margin expansion in fiscal year '27 and contribute to this trajectory to get back to double-digit margins" | LONG, undated |
| Q1 FY27 p. 7 | Hill | Teams "move into this new formation in fiscal year '28" (4 geographies to 3) | Execution risk in FY28 |
| Q1 FY27 p. 10 | Denton | Pace savings about $2.5B; "majority ... realized in fiscal years '29 and '30", full benefit into FY31 | SHORT for FY28 |
| Q1 FY27 p. 11 | Denton | Supply actions "create pressure on reported revenues for the remainder of fiscal '27 and into '28" | SHORT |
| Q1 FY27 p. 24 | Denton | Pain "through the balance of this year and probably bleed in a little bit into fiscal '28 as well" | SHORT |
| Q1 FY27 p. 24 to 25 | Binetti / Denton | A path to company revenue growth in FY28? "So why don't we hold that question, we'll come back to it at Investor Day" | Avoided |

**What the consensus needs (DERIVED; assumptions stated).** FY26 revenue was $46,398M (FY26 10-K p. 55). A high single digit decline puts FY27 at about $42.7B. Plus 1% gives FY28 at about $43.1B. At 1,484M diluted shares (Q1 FY27 10-Q p. 1) and a low-20s tax rate (21% assumed, from the Q4 FY26 call), the figures work out as follows:

| | FY27 guide midpoint | FY28 consensus |
|---|---|---|
| EPS | $1.25 | $1.65 (+32% vs guide midpoint; +28% vs consensus FY27 per scoreboard) |
| Implied net income | about $1.86B | about $2.45B |
| Implied EBIT margin | about 5.5% | about 7.2% |

So FY28 needs about +170 bp of EBIT margin on flat revenue. Nike's best year-on-year EBIT margin gain from FY22 to FY26 was +60 bp, in FY24 (12.1% to 12.7%: Q4 FY23 release p. 6; FY24 10-K p. 31). The calls offer three possible sources: tariff lapping, the FY26 restructuring benefits, and early Pace savings. But management has moved most of the savings to FY29 to FY30, says the revenue drag bleeds into FY28, and plans a reorganization during FY28.

**Alternative explanations checked.** (a) Tariffs in force are 10% to 12.5%, below Nike's 15% planning rate (scoreboard, REPO). That could add margin the calls do not show. (b) A guide built to be "reasonable and attainable" (Q1 FY27 p. 10) may hide upside, as the 14-of-14 quarterly record suggests. (c) Pace savings are gross, and part is reinvested (p. 10), which cuts against the bull reading.

**Verdict: SHORT, moderate.** Nothing management said supports FY28 EPS +28 to 32%. Every dated statement made since Q3 FY26 has moved benefits later.

## 8. Analysis 6: other companies' calls

**Stated beforehand.** LONG if retailers name Nike more often and more positively through 2026, including in lifestyle, and if adidas sees Nike as resurgent. SHORT if mentions fade, turn negative, or retailers blame brand discounting and excess inventory.

**Result** (`peers/peer_calls_summary.csv`, `peers/peer_nike_mentions.csv`; 14 Motley Fool transcripts, OPENED 2026-10-14; tone hand-coded on company-speaker sentences only):

| Retailer | Calls | Nike per 10k words | Nike sentences: positive / negative | Pattern |
|---|---|---|---|---|
| DICK'S (incl. Foot Locker from Q3 2025) | May 2025 to Aug 25, 2026 (6) | 12.4, 2.2, 2.9, 3.4, 1.1, **11.4** | 15 / 0 | The Aug 2026 call praised the Nike Mind shoe, the running construct, Vomero and Pegasus, Solo Fleece and basketball ("Nike is best positioned"). |
| Academy | Mar 2024 to Sep 10, 2026 (8) | 4.4, 4.3, 3.8, 6.7, **15.0**, 8.1, 10.0, **3.7** | 28 / 0 | Jordan launched in spring 2025. Jun 2026: Nike plus Jordan comp up mid single digits, "Nike is a growth engine". Sep 2026: no Nike comp given, and HOKA added (8 mentions). |

**The unnamed negatives in the same calls:**
- DICK'S, Aug 25, 2026 (Webull transcript, OPENED; Motley Fool, OPENED): "older legacy silhouettes and franchises that have done so well have slowed and slowed relatively quickly". Also: "A number of brands got very promotional on their sites, and those promotions spilled into the broader marketplace". And: "As several of these brands became more promotional to clear inventory, the margin pressure on Foot Locker is much greater". Foot Locker pro forma comps were -3.6%. Stack added "I don't think this is a demand issue".
- adidas, Jul 30, 2026 (Investing.com transcript, OPENED, partial): Nike is never named. Gulden said lifestyle footwear "is currently pretty heavily discounted" because "major brands have quite some inventory that have been sold in". On China he said: "The impact of a competitor's action in China is unknown." He also noted competitors "had zero growth".
- Foot Locker, Q3 2024 (Dec 4, 2024): Dillon cited Nike "softness" and promotions "higher than forecasted ... particularly in key brands" (SNIPPET, secondary summaries). We found no free Foot Locker transcript for 2024. Foot Locker has reported inside DICK'S since Q3 2025.
- JD Sports: no public Q&A transcript. Coverage says JD "has been hurt by troubles at key supplier Nike Inc, where a hoped-for turnaround is proving elusive" (Morningstar UK, 2026, SNIPPET).

**Alternative explanations checked.** (a) Retailers rarely criticize their largest vendor on a public call. Academy calls Nike "our biggest vendor", so zero negatives is the expected baseline, not evidence. (b) Mention spikes follow events (Academy's Jordan launch, the DKS Foot Locker deal), not demand. The informative signal is the content: performance praised, lifestyle blamed, and brand-site promotions blamed, which matches Nike's own split.

**Verdict: NEUTRAL, weak.** It confirms that performance is working (a LONG point already known) and that lifestyle and promotions are still the problem (SHORT, already known).

## 9. The five most telling quotes

1. **"In North America and EMEA, which represent almost 3/4 of our business, we have returned to a healthy marketplace."** Matt Friend, Q2 FY26 call (Dec 18, 2025), p. 8. Nine months later, Elliott Hill said: "we proactively work with our wholesale partners to work through excess inventory to create a healthy marketplace" (Q1 FY27, Oct 1, 2026, p. 3). This is the clearest declared-then-reversed promise.
2. **"that's going to be through the balance of this year and probably bleed in a little bit into fiscal '28 as well."** Dave Denton, Q1 FY27 call, p. 24, on the pain from the Sportswear, Jordan and China resets.
3. **"expect the majority of the program savings to be realized in fiscal years '29 and '30, with the full realization of the program to continue into fiscal year '31."** Dave Denton, Q1 FY27 call, p. 10. Compare Q3 FY26 p. 9: benefits "begin in fiscal '27 and continue to build through fiscal '28".
4. **"So why don't we hold that question, we'll come back to it at Investor Day, and we'll hit that head on."** Dave Denton, Q1 FY27 call, p. 25, answering whether Nike sees "a path to total company revenue positivity at some point in fiscal '28" (Binetti, p. 24).
5. **"This outlook reflects continued pressure on gross margin and fixed cost deleverage associated with lower revenue levels, higher input costs, but partially offset by disciplined expense management."** Dave Denton, Q1 FY27 call, p. 11, followed by "we're probably not going to provide guidance specifically for gross margin" (p. 18). This marks the end of the quarterly gross margin guide and the softening of the margin-inflection story.

Runner-up, for context on how much weight to put on Investor Day targets: "And we still believe those long-term goals of profitability are achievable." (Matt Friend, Q1 FY24, p. 20), about the FY25 high-teens EBIT margin target. FY25 came in at 8.2%.

## 10. What to watch, and what would change this view

- **Investor Day (Nov 16 to 17):** if FY28 is framed as revenue growth with EPS near $1.65 or above, analyses 1, 2 and 5 are wrong on direction. If FY28 is framed as "transition", or the algorithm starts in FY29, the SHORT on FY28 consensus works. Given the record above, discount any long-term margin target by its history: the 2021 targets missed by more than 50%.
- **Q2 FY27 (about Dec 17):** with no explicit guide and a 14-of-14 beat record, an in-line or better quarter is the base case. That is a risk to the SHORT after the finals, not before.
- **Win Now wording:** if Investor Day declares Win Now complete while still guiding supply cuts into FY28, that is the same declared-then-reversed pattern as the healthy-marketplace claim.

## 11. Sources

- Nike official call transcripts, Q1 FY21 to Q1 FY27, investors.nike.com (OPENED 2026-10-13); URLs in `data/hunt/earnings_calls/transcripts/README.md`.
- Nike filings via `data/nike_filing_facts.csv` (REPO): FY21 to FY26 10-Ks, Q1 FY27 10-Q, quarterly earnings releases, pages as cited.
- DICK'S Sporting Goods call transcripts, May 28, 2025 to Aug 25, 2026, fool.com (OPENED 2026-10-14). The Aug 25, 2026 call was also read on webull.com/news/15463631008252928 (OPENED 2026-10-14). DICK'S own q4cdn transcript PDF returned 403.
- Academy Sports + Outdoors call transcripts, Mar 21, 2024 to Sep 10, 2026, fool.com (OPENED 2026-10-14). URLs in `data/hunt/earnings_calls/peers/peer_urls.txt`.
- adidas Q2 2026 call, Jul 30, 2026, investing.com transcript (OPENED 2026-10-14, first 100,000 characters; the page truncates the end of Q&A).
- Foot Locker Q3 2024 call, Dec 4, 2024: secondary summaries via search (SNIPPET 2026-10-14).
- JD Sports: Morningstar UK and other coverage via search (SNIPPET 2026-10-14).
- Consensus FY28 EPS $1.65 and tariff rates: `00_SCOREBOARD.md` (REPO, 2026-10-14).
