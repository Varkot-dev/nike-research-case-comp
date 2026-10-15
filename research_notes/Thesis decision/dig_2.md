# Dig 2: Does Nike's FY27 guide show the decline spreading outside China?

Date: 2026-10-14. Scope: Pillar 2 of the SHORT ruling (01_ruling.md). Four things to check: (1) the exact wording of the FY27 revenue guide and whether it is reported or currency-neutral, (2) the Q1 FY27 segment figures on 10-Q p.25, (3) the NIKE Brand ex-Greater China range of -3.4% to -7.8% and the claim that "the other $30B falls 15% to 18%", (4) the exact transcript wording for "Performance ~$16B, growing high-single digits".

All arithmetic is mine. Scripts: scratchpad `dig2s/grid.py`. No modeling, only arithmetic on reported figures.

## Sources opened today

| Source | What it is | Opened? |
|---|---|---|
| Q1 FY27 Form 10-Q (nke-20260831.htm, EDGAR accession 0000320187-26-000193), local copy in scratchpad `dl/q1fy27.htm`, converted to rows | Segment table p.25, consolidated revenue p.22, MD&A p.23 | OPENED (local copy of the EDGAR file) |
| Q1 FY27 earnings release, 8-K Ex. 99.1 (q1fy27exhibit991er.htm), local copy in scratchpad `edgar/docs2/`; also listed in today's web search at sec.gov/Archives/edgar/data/0000320187/000032018726000184/ | "Outlook" section | OPENED (local copy) |
| Q1 FY27 official call transcript (NIKE-Inc-Q1FY27-OFFICIAL-Transcript_-FINAL.pdf, investors.nike.com q4cdn), local copy in scratchpad `tx/Q1FY27.pdf`, read with pdftotext | Guide wording, Performance quote | OPENED (local PDF) |
| Q4 FY26, Q1 to Q3 FY26, Q1 to Q4 FY25, Q4 FY24 transcripts (scratchpad `flat/*.txt`) | How Nike has worded its revenue guides in the past | OPENED (local text) |
| data/nike_filing_facts.csv (wonderful-franklin) | FY26 and quarterly segment revenue, each row cited to a 10-K, 10-Q or 8-K page | OPENED (repo) |
| data/trackrecord/guidance_vs_actual.csv | Nike's guide-versus-actual history | OPENED (repo) |
| Web search, 2026-10-14: investinglive, Stocktwits, S&P Global, Just Style | Press wording of the guide | Search snippets only, NOT opened |

## 1. Guide wording, word for word

- **Release (8-K Ex. 99.1, "Outlook"):** "Revenues are expected to decline high-single digits in fiscal 2027." No basis is named. In the same release Nike marks every currency-neutral figure with an asterisk and says "on a currency-neutral basis" in words (for example "down 4 percent on a reported basis and down 5 percent on a currency-neutral basis*"). The outlook bullet has neither the asterisk nor the words.
- **Call (Denton):** "For fiscal '27, we currently expect revenues to decline in the high single-digit range." The operator's opening convention says "All growth comparisons on the call today ... are currency-neutral, unless otherwise noted." The next lines then say: "We expect those actions will create pressure on **reported** revenues for the remainder of fiscal '27 and into '28." Then: "These 2 items will represent a headwind of approximately 400 basis points to revenues in the second quarter."
- **No FX statement.** The words FX, foreign exchange and currency appear in the call only in the operator's convention line, the Q1 c-n figure and the Q1 gross-margin "FX tailwinds". No FX assumption is given for FY27.
- **Nike's past habit (transcripts, opened):** Friend-era guides named the basis or the FX effect. Examples: "we expect reported revenues to be down low to mid-single digits with no expected benefit from foreign exchange" (Q4 FY26); "including one point of benefit from foreign exchange" (Q1 FY26); "a 3-point benefit from foreign exchange" (Q2 FY26). Those guides were reported numbers, with FX called out inside them. Denton's first guide drops that detail.

**Verdict:** the release wording (unqualified "Revenues", in a document that labels every non-GAAP c-n figure) means reported is the most likely reading. A c-n reading cannot be fully ruled out because of the call's default convention. This changes the result by only about 1 point. Q1 FX was worth about +0.7 pts (reported -4.3%, c-n about -5%), so a c-n guide of -7% to -9% is roughly -6% to -8% reported if FX stays similar. The grid below therefore includes a -6% row. **What would settle it:** a question at Investor Day (Nov 16 to 17), or the Q2 FY27 call (about Dec 17) restating the guide with a basis.

"High single digits" is read as 7% to 9%. Nike's own guide table uses that reading: "high single-digits" is coded 7 to 9 in guidance_vs_actual.csv (Q3 FY23 row).

## 2. Q1 FY27 segment figures (10-Q p.25, opened)

The page-25 segment table sits between the printed page markers "24" and "25" in the converted file.

| $M | Q1 FY27 | Q1 FY26 | Reported | C-n |
|---|---|---|---|---|
| North America | 5,127 | 5,020 | +2% | +2% |
| EMEA | 3,176 | 3,331 | -5% | -5% |
| Greater China | 1,180 | 1,512 | -22% | -26% |
| APLA | 1,463 | 1,490 | -2% | 0% |
| Global Brand Divisions | 6 | 9 | | |
| **Total NIKE Brand** | **10,952** | **11,362** | -4% | -4% |
| Converse | 263 | 366 | -28% | -28% |
| Corporate | (2) | (8) | | |
| **Total NIKE, Inc.** | **11,213** | **11,720** | -4% | -5% |

Results:
- Total change: 11,213 / 11,720 - 1 = **-4.33%**. Confirmed.
- NIKE Brand ex-GC: 9,772 / 9,850 - 1 = **-0.79%** reported; about -0.7% c-n (region c-n rates weighted by prior-year revenue). Confirmed as -0.8%.
- Both the -4% (NIKE Brand) and -5% (NIKE, Inc. c-n) figures in the press are correct. They describe different lines (10-Q p.22 and p.25).

FY26 bases (nike_filing_facts.csv, citing the FY26 10-K pp.32, 36, Q2 and Q3 FY26 10-Qs and the Q4 FY26 8-K):
- NIKE, Inc. FY26: $46,398M. Q2 to Q4 FY26: 12,427 + 11,279 + 10,972 = **$34,678M**.
- Greater China Q2 to Q4 FY26: 1,423 + 1,615 + 1,297 = **$4,335M**.
- Converse Q2 to Q4 FY26: 300 + 264 + 244 = **$808M**.
- Corporate Q2 to Q4 FY26: $10M.
- NIKE Brand Q2 to Q4 FY26: $33,860M. **Ex-GC: $29,525M.** Cross-check: brand + Converse + corporate = 34,678.

## 3. Recompute

### 3a. What the full-year guide leaves for Q2 to Q4

| FY27 reported | FY27 $M | Q2 to Q4 $M | vs $34,678M |
|---|---|---|---|
| -6% | 43,614 | 32,401 | -6.6% |
| -7% | 43,150 | 31,937 | **-7.9%** |
| -8% | 42,686 | 31,473 | -9.2% |
| -9% | 42,222 | 31,009 | **-10.6%** |

The ruling's -7.9% to -10.6% is confirmed for the 7% to 9% reading. Q1 was -4.3%, so the guide does imply the rest of the year is worse than Q1.

### 3b. NIKE Brand ex-GC, Q2 to Q4 FY27 (Converse at -28%, corporate set to 0)

| FY27 | GC -26% | GC -30% | GC -35% | GC -40% |
|---|---|---|---|---|
| -6% | -3.1% | -2.5% | -1.8% | -1.0% |
| -7% | -4.7% | -4.1% | **-3.3%** | -2.6% |
| -8% | -6.2% | -5.6% | -4.9% | -4.2% |
| -9% | **-7.8%** | -7.2% | -6.5% | -5.8% |

- The advocate's -3.4% to -7.8% reproduces: -3.35% rounds to -3.3%, and the -7.8% matches exactly.
- **The range is too narrow on the GC side.** Denton said the guide "assumes that China actually gets worse from a revenue perspective for the balance of this year." The Jan 1, 2027 partner-online exit (about $743M a year, investigations/02) falls in Q3 and Q4. Half a year of it is about $370M against Q3 to Q4 FY26 GC of $2,912M, which adds roughly -13 pts in H2 on top of an underlying -26%. GC at -40% for Q2 to Q4 is therefore plausible, and it moves the best case to **-2.6%**.
- **Corrected range:** NIKE Brand ex-GC Q2 to Q4 falls about **-2.6% to -7.8%** on a 7% to 9% reported reading (-1.0% to -7.8% if the guide is read as -6%), against **-0.8% in Q1**. Every cell in the table is worse than Q1.
- Converse sensitivity is small: at -35% instead of -28%, about $57M, or 0.2 pts.

### 3c. Take out the named Q2 one-off (the 400 bps lap)

Denton: "a headwind of approximately 400 basis points to revenues in the second quarter", from lapping EMEA Cyber Week promotions and a higher NA sell-in comparison. That is 4% x $12,427M = **about $497M**. Both items sit outside China.

| | GC -26% | GC -35% | GC -40% |
|---|---|---|---|
| FY -6%, ex-lap | -1.4% | -0.1% | +0.6% |
| FY -7%, ex-lap | -3.0% | -1.7% | -0.9% |
| FY -9%, ex-lap | -6.1% | -4.8% | -4.1% |

On the softest assumptions (-7% FY, GC -40%, lap removed), ex-GC Q2 to Q4 is -0.9%, the same as Q1. **So "the decline is spreading" depends on where in the guide range Nike lands and on how deep China goes.** At the guide midpoint (-8%) it holds in every cell: -4.2% to -6.2% before the lap, about -2.5% to -4.5% after it.

### 3d. "The other ~$30B falls 15% to 18%"

Other = FY27 total minus Performance. FY26 Performance base = $16,000M, so other = $30,398M.

| FY27 | Perf 0% | Perf +5% | Perf +7% | Perf +9% |
|---|---|---|---|---|
| -6% | -9.2% | -11.8% | -12.8% | -13.9% |
| -7% | -10.7% | -13.3% | **-14.4%** | -15.4% |
| -8% | -12.2% | -14.8% | -15.9% | -16.9% |
| -9% | -13.7% | -16.4% | -17.4% | **-18.5%** |

- Correct the range to **-14.4% to -18.5%** for "Performance +7% to +9%, total -7% to -9%". The figure "15 to 18" is the inner part of that range.
- Moving the $16B base by ±$0.5B shifts each cell by about 0.3 to 0.4 pts.
- **Robust version:** for the non-Performance business to fall less than 10%, Performance must *shrink*: by about 1.3% at FY -7% and about 7.1% at FY -9%. Management says Performance is growing, so the rest of Nike falls double digits on any reading of the guide. Even at FY -6% with Performance flat, it falls 9.2%.
- **Important correction:** management did NOT guide Performance to grow high-single digits for FY27. "High single digits" describes **Q1 only**, is currency-neutral by the call convention, and Denton says it was "benefiting from the World Cup". FY26 Performance grew "mid-single digits". The pitch must say "if Performance keeps growing at its FY26 to Q1 pace (5% to 9%)", not "Nike guides Performance +HSD". On that basis the range is -13.3% to -18.5% at FY -7% to -9%.

### 3e. Cross-check against management's own split (Q1)

Inputs: Performance about 34% of revenue (16.0/46.4), up HSD (+8%), about +2.8 pts. Sportswear "just under half", down "low double digits" (about -11%), about -5.3 pts. Jordan "13% of our global business ... falling by mid-teens", about -2.0 pts. Converse 3.1% x -28%, about -0.9 pts.
- Sum: about -5.4% against the actual -5% c-n.
- Denton's own figure, "NIKE Sportswear and the Jordan Brand ... represented a high single-digit drag on consolidated NIKE", agrees with the -7.3 pts implied above.
- The shares add up: FY26 Sportswear residual = 46,398 - 16,000 - 7,034 (Jordan, repo, FY26 10-K p.32) - 1,174 = $22,190M, or 47.8%, matching "just under half".

The unaudited categories are internally consistent with the audited totals.

## 4. Performance quote, word for word (transcript, opened)

- Hill, prepared remarks: "Our NIKE Brand Performance portfolio continued to grow. Last fiscal year, we grew this business to $16 billion. We built on that foundation this quarter, growing NIKE Performance by another high single digits."
- Denton: "if you were to isolate our NIKE Performance business, it was up high single digits this quarter, benefiting from the World Cup. Additionally, if you were to exclude the reset in Greater China, NIKE Performance would have been up low double digits in Q1."
- Hill, Q&A: "the Q1 performance growth was on top of the performance growing mid-single digits in FY '26 to $16 billion."

Status: **confirmed with changes.**
- The $16B is FY26, rounded, and NIKE Brand. It appears in no 10-K or 10-Q.
- "High single digits" is Q1, currency-neutral by the call convention, and helped by the World Cup. It is not an FY27 guide.

## 5. Alternative explanations for "guide implies a worse Q2 to Q4 outside China"

| # | Alternative | Status | Evidence |
|---|---|---|---|
| A1 | The guide is c-n, so the reported decline is smaller | **Mostly ruled out; about 1 pt either way.** | Release wording is unqualified and Nike labels c-n figures. Even reading -6% reported, every GC cell in 3b is worse than Q1's -0.8%. |
| A2 | China takes the whole deterioration (deeper GC cut plus online exit) | **Partly true; narrows the range, does not close it.** | At GC -40%, ex-GC is still -2.6% to -5.8% for FY -7% to -9%. Only at FY -5% to -6% does ex-GC approach Q1. |
| A3 | It is a one-quarter calendar effect (the Q2 400 bps lap) | **Partly true.** | The $497M lap is about 1.7 pts of the ex-GC base. After removing it, the midpoint is still -2.5% to -4.5%. At the soft corner (FY -7%, GC -40%) it falls to -0.9%, the same as Q1. Part of the lap is itself a choice (not repeating promotions), and part (the NA sell-in comparison) is a fill lap, which supports the argument that the NA gain was fill. |
| A4 | The ex-GC fall is the deliberate Sportswear and Jordan supply cuts, not spreading weakness | **Cannot be ruled out by arithmetic; partly contradicted by management.** | Hill: "some aged, higher volume, sportswear footwear sold through below expectations. Looking ahead, that has impacted our future order books", plus "product underperformance and broader marketplace pressure" and "lack of energy in the lifestyle space ... impacting traffic". Nike's own split puts part of the decline outside its deliberate actions, but Nike gives no dollar split. **Wording fix:** "spreading beyond China", not "spreading beyond the deliberate cuts", unless the second claim is sourced to these quotes. |
| A5 | The guide is sandbagged by a new CFO | **Open.** | Denton: "set at a level that we believe is reasonable and attainable." The Friend-era revenue record in guidance_vs_actual.csv shows both beats and misses (FY24 guide +MSD, actual +0.3%). At FY -5%, ex-GC Q2 to Q4 is -0.2% to -1.5%: no spread. **Settles:** Q2 FY27 on about Dec 17 (after finals), Investor Day re-guide (Nov 16 to 17). |
| A6 | Q1 was flattered by the World Cup, so the "deterioration" is a lap of a one-off | **Open, not sized.** | Denton says Performance was "benefiting from the World Cup"; Football was "strong double-digit ... in all 4 geos"; team kit sales "doubled" versus 2022. Nike gives no dollars. Upper bound: NIKE Brand apparel rose only $71M yoy (10-Q p.22), so a kit-driven boost to brand-level ex-GC is probably under 1 pt, but footwear (boots) is not separable. |
| A7 | FX moves reported revenue | **Small.** | Q1 FX was +0.7 pts; no FY27 FX guidance. Covered by the -6% row. |
| A8 | Converse or corporate distort the result | **Ruled out.** | A 7-pt swing in the Converse decline is 0.2 pts; corporate is $10M. |
| A9 | The $16B Performance figure is wrong or defined differently | **Low impact.** | ±$0.5B changes "other" by less than 0.4 pts. The decomposition in 3e reconciles to reported totals. |

## 6. Bottom line for Pillar 2

1. **Confirmed:** Q1 numbers (-4.3% total, -0.8% NIKE Brand ex-GC); the release guide wording; Q2 to Q4 implied at -7.9% to -10.6% on a 7% to 9% reported reading; the Performance $16B and HSD wording.
2. **Change the ex-GC range** to "about -2.5% to -8% for Q2 to Q4, against -0.8% in Q1". The -3.4% floor ignores Denton's statement that China gets worse; at GC -40% the floor is -2.6%.
3. **Change the "other $30B" claim** to: "If Performance keeps growing 5% to 9%, the rest of Nike (about $30B) falls 13% to 18.5% in FY27. For it to fall less than 10%, Performance would have to shrink." Do NOT say Nike guided Performance +HSD.
4. **Change the pillar title** from "past the deliberate cuts" to "beyond China". Support the non-deliberate part with Hill's "sold through below expectations ... impacted our future order books" quote, not with arithmetic.
5. **The weakest link** is the bottom of the guide range. If FY27 lands at -6% or better and GC falls 35% to 40%, the ex-GC spread nearly disappears once the Q2 lap is removed. Pre-registered falsifier (already in the ruling): NIKE Brand ex-GC flat or up in Q2 FY27. Add this one: an Investor Day re-guide to "mid-single digit" decline would weaken this pillar.
