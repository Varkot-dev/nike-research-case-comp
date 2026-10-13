# AD_TRACKRECORD: Does Nike management deliver what it promises?

Prepared 2026-10-13. Nike fiscal years end May 31 (FY2027 = June 2026 to May 2027). This note extends `research_notes/thesis_tests/say_vs_do_execution.md` (Pace commitments, hiring, partnerships, pay metrics, the December 2026 Win Now deadline) and does not repeat it. It does not cover root causes, channels, China, Jordan, discounting, tariffs or product, which other sessions own.

**Sources and labels**
- Guidance quotes come from Nike's official call transcripts on investors.nike.com (`/financial-information/financial-results`, PDFs under `/_assets/.../webcast_transcript/`), cited as "Q2 FY24 call p. 13". Q1 FY24 is the prepared-remarks PDF (Nike posted no Q&A transcript for that quarter). Page numbers are the PDF page numbers.
- Reported numbers come from `data/nike_filing_facts.csv`. Each one cites a filing, for example "(FY24 10-K p. 91)". Earnings releases have no printed page numbers, so they are cited as "seq p.".
- Other labels used: *market data* (`data/nke_daily_prices.csv`, and S&P 500 closes from the Yahoo chart API), *secondary* (an opened press or analyst page), *my arithmetic*, *my inference* and *my convention*.
- Downloads are treated as untrusted data.

**Files** (data in `data/trackrecord/`)
- `guidance_vs_actual.csv`: 102 scored guidance items, 5 milestones and 9 pending items, each with its quote, source page, actual figure and verdict.
- `actuals_by_period.csv`: quarterly and annual revenue, gross margin, SG&A, operating overhead, demand creation, tax rate and EPS, Q1 FY22 to Q1 FY27, all taken from the facts CSV.
- `longterm_targets_vs_actual.csv`: the October 2017, June 2020 and June 2021 targets against what was reported.
- `savings_audit_overhead.csv`: operating overhead FY2023 to FY2026, with charges stripped out, compared against a wage-inflation path and a revenue-scaled path, plus headcount.
- `price_reactions.csv`: 30 earnings events since June 2019 plus the Hill appointment. For each: 1-day, 5-day and 20-day moves, the drift from day 1 to day 20, and moves in excess of the S&P 500.
- Scripts are in `scripts/trackrecord/` (`guidance.py`, `actuals.py`, `targets_audit.py`, `prices.py`, `outlook.py`, `ctx.py`). Raw call-transcript PDFs, their page-marked text, BLS and S&P downloads are not committed (transcripts are Nike IR documents; fetch from investors.nike.com).

**Scoring convention** (*my convention*)
- Each word band maps to a numeric range:

| Guidance wording | Range used |
|---|---|
| flat | -1 to +1 |
| slightly up | 0 to +2 |
| slightly down | -2 to 0 |
| low single digits (LSD) | 1 to 3 |
| mid single digits (MSD) | 4 to 6 |
| high single digits (HSD) | 7 to 9 |
| low double digits (LDD) | 10 to 13 |
| low teens | 11 to 13 |
| mid-teens | 14 to 16 |
| high teens | 17 to 19 |
| low 20% range | 20 to 23 |
| "approximately X%" (revenue) | X plus or minus 1 pt |
| "approximately N bps" | N plus or minus 25 bps |

- A result inside the range is "in line". Higher revenue or gross margin is a "beat". Lower SG&A or a lower tax rate is also a "beat", and SG&A rows are flagged "below guide (lower cost)".
- Each item is assigned to the CEO whose management team issued the guidance. The Donahoe era runs through the Q1 FY25 call (Oct 1 2024). The Hill era starts with the Q2 FY25 call.

---

## (A) Plain-English summary

1. **Nike usually beats its next-quarter guidance and usually misses its full-year and multi-year promises.** Under Donahoe, next-quarter guidance was met or beaten on 22 of 26 items (85%). Full-year and longer guidance was met on only 28 of 44 (64%), and full-year revenue missed on 7 of 15 (47%). The first full-year gross margin guide missed in all three years that had one: FY23 guided flat to -50 bps, actual -250; FY24 guided +140 to +160, actual +110; FY25 guided +10 to +30, actual -190 (my arithmetic on the facts CSV; guides from Q4 FY22 call p. 18, Q4 FY23 call p. 15, Q4 FY24 call p. 14).
2. **Under Hill, quarterly guidance has been conservative: 22 of 22 items met or beaten, and revenue beat in 6 of 7 quarters.** Reported revenue landed on average 2.3 points above the midpoint of the guide. Gross margin landed 36 bps above the midpoint (my arithmetic). The beats survive after removing currency in most quarters. For example, Q1 FY26 was guided "down mid-single digits" and came in +1.1% reported and -1% currency-neutral.
3. **The dated milestones did not hold.** The "healthy and clean" marketplace due by the end of H1 FY26 was reached only in North America and EMEA (Q4 FY25 call p. 8; Q2 FY26 call p. 7). It was then re-dated to December 2026 (Q3 FY26 call p. 12), and later moved past FY2027 (Q1 FY27 10-Q p. 20).
4. **Every long-term target set in 2017 and 2021 missed, apart from the international growth mix and the 30% digital share.** The 2017 targets ran through FY2023. Revenue growth averaged 6.9% a year against a high-single-digit goal. Gross margin fell 110 bps against a goal of up to +50 bps a year. EPS grew 4.3% a year against mid-teens. The 2021 targets ran through FY2025. They called for a high-teens EBIT margin (actual 8.2%), gross margin in the high 40s (actual 42.7%) and owned digital at 40% of the business (actual 21.5%) (my arithmetic).
5. **Nike never reported a figure for the $2 billion savings plan of December 2023.** After the FY2024 10-K, the plan's wording ("enterprise initiative", "cost savings") disappears from the 10-Ks. It last appears in the Q3 FY25 10-Q, in a restructuring note. The only progress update came on a call: savings "unlocked", with "nearly one billion dollars" to be reinvested in FY25 (Q4 FY24 call p. 10).
6. **Overhead dollars did fall, but only in line with revenue, so margins gained nothing.** Operating overhead excluding charges fell from $12,317M (FY23) to $11,129M (FY26), down 9.6%, while revenue fell 9.4%. Overhead stayed at 24.0% of revenue at both ends. Against a wage-inflation path the cumulative gap is about $5.3B, but SG&A as a share of revenue rose from 32.0% to 34.7% and EBIT margin fell from 12.1% to 8.3% (my arithmetic).
7. **The market punishes guidance cuts hard and does not reward beats against Nike's own guidance.** Six cut or withdrawal events averaged -8.9% on day one, including -20.0% on Jun 28 2024. Hill-era quarters that beat the revenue guide produced day-one moves anywhere from -15.5% to +15.2%. 13 of the 18 tracker-period earnings events fell on day one (market data).
8. **Pace ($2.5B through FY2031) is smaller per year than the 2023 plan and back-loaded.** It works out to $0.5B a year on average against about $0.67B a year for the 2023 plan, with the majority due in FY29 to FY30 (Q1 FY27 call p. 10). The November 16 to 17 Investor Day matters for one reason: whether Nike commits to a public, dated scorecard of net savings. It did not do so in 2023.

---

## (B) Guidance versus actual, Q1 FY23 to Q1 FY27

### B1. Next-quarter guidance (each row is the guide given on the prior quarter's call)

| Target quarter | Guide given on | Revenue guide (reported) | Actual | GM guide (bps y/y) | Actual | SG&A guide | Actual | Verdict (rev / GM / SG&A) |
|---|---|---|---|---|---|---|---|---|
| Q1 FY23 | Jun 27 2022 (p. 17 to 18) | flat to slightly up | +3.6% | worse than -100 | -220 | n/a | n/a | beat / in line (open-ended) / n/a |
| Q2 FY23 | Sep 29 2022 (p. 16) | LDD | +17.2% | -350 to -400 | -300 | n/a | n/a | beat / beat |
| Q3 FY23 | Dec 20 2022 (p. 13) | n/a | +14.0% | similar to Q2 (-300) | -330 | $ in line with Q2 ($4,124M) | $3,959M | n/a / miss / beat (lower) |
| Q4 FY23 | Mar 21 2023 (p. 14) | flat to LSD | +4.8% | n/a | -140 | n/a | n/a | beat |
| Q1 FY24 | Jun 29 2023 (p. 15) | flat to LSD | +2.0% | -50 to -75 | -10 | LDD | +5.0% | in line / beat / beat (lower) |
| Q2 FY24 | Sep 28 2023 (p. 12) | up slightly | +0.5% | about +100 | +170 | MSD to HSD | +0.5% | in line / beat / beat (lower) |
| Q3 FY24 | Dec 21 2023 (p. 13) | slightly negative | +0.3% | +160 to +180 | +150 (incl. about 50 bps restructuring, Q3 FY24 call p. 11) | n/a | +6.7% | beat / miss |
| Q4 FY24 | Mar 21 2024 (p. 14) | up slightly | -1.7% | +160 to +180 | +110 | down slightly | -6.5% | miss / miss / beat (lower) |
| Q1 FY25 | Jun 27 2024 (p. 15) | about -10% | -10.4% | +10 to +30 | +120 | up MSD | -1.7% | in line / beat / beat (lower) |
| Q2 FY25 | Oct 1 2024 (p. 9) | -8% to -10% | -7.7% | about -150 | -100 | roughly flat | -3.4% | beat / beat / beat (lower) |
| Q3 FY25 | Dec 19 2024 (p. 13 to 14) | down LDD | -9.3% | -300 to -350 | -330 | slightly down | -8.0% | beat / in line / beat (lower) |
| Q4 FY25 | Mar 20 2025 (p. 16) | down mid-teens, low end | -12.0% | -400 to -500 | -440 | up LSD to MSD | +1.5% | beat / in line / in line |
| Q1 FY26 | Jun 26 2025 (p. 13) | down MSD | +1.1% | -350 to -425 | -320 | up LSD | -0.8% | beat / beat / beat (lower) |
| Q2 FY26 | Sep 30 2025 (p. 11) | down LSD | +0.6% | -300 to -375 | -300 | up HSD | +0.8% | beat / in line / beat (lower) |
| Q3 FY26 | Dec 18 2025 (p. 11 to 12) | down LSD | +0.1% | -175 to -225 | -130 | up LSD | +2.3% | beat / beat / in line |
| Q4 FY26 | Mar 31 2026 (p. 13) | -2% to -4% | -1.1% | -25 to -75 | -10 excluding the one-time 900 bps IEEPA benefit (+890 reported; Q4 FY26 call p. 8) | flat to down slightly | -1.6% | beat / beat / in line |
| Q1 FY27 | Jun 30 2026 (p. 12) | down LSD to MSD | -4.3% | slightly positive | +60 | flat | -2.6% | in line / beat / beat (lower) |
| Q2 FY27 | Oct 1 2026 (p. 11) | no number; about 400 bps headwind from two items | pending | not guided (Q1 FY27 call p. 18) | pending | n/a | pending | pending |

Actuals: revenue growth, gross margin change and SG&A growth come from `actuals_by_period.csv` (facts CSV; quarterly figures are from the earnings releases, seq p. 1). Tax-rate guides are scored in the CSV only. Under Donahoe, quarterly tax guides were met 6 of 10 times and beaten (lower rate) 3 times. Under Hill they were met 3 of 5 times and missed 2 times: FY25 came in at 17.1% against "mid-teens", and FY26 at 20.3% against "19% to 20%".

### B2. Full-year guidance as first given and as revised

| Fiscal year | First guide (call, page) | Revisions | Reported | Verdict on first guide |
|---|---|---|---|---|
| FY22 | Revenue up LDD and "surpass $50 billion" (Q4 FY21 call p. 13) | Sep 2021: cut to MSD (Q1 FY22 call p. 8) | $46,710M, +4.9% (FY22 10-K) | miss |
| FY23 | c-n revenue up LDD; GM flat to -50 bps; SG&A up HSD to LDD; tax mid-teens (Q4 FY22 call p. 17 to 18) | Sep 2022: GM -200 to -250. Dec 2022: c-n low teens. Mar 2023: reported HSD, GM about -250 | c-n +16%, reported +9.6%, GM -250, SG&A +10.6%, tax 18.2% | revenue beat; GM miss by 200 bps; tax miss |
| FY24 | Reported revenue up MSD; GM +140 to +160; SG&A slightly above revenue; tax similar to FY23 (Q4 FY23 call p. 14 to 15) | Dec 2023: revenue about 1%, plus a $400M to $450M restructuring charge. Mar 2024: GM about +120 | +0.3%; GM +110; SG&A +1.2% (-1.1% excluding $379M restructuring); tax 14.9%; EPS $3.73 GAAP, $3.95 excluding restructuring (Q4 FY24 release seq p. 1) | revenue miss; GM miss |
| FY25 | Mar 2024 preview: "revenue and earnings to grow", H1 down LSD (Q3 FY24 call p. 15). Jun 2024: revenue down MSD, H1 down HSD, GM +10 to +30, SG&A up slightly (Q4 FY24 call p. 14) | Oct 1 2024: **withdrawn** (Q1 FY25 call p. 3) | -9.8%; H1 -9.1%; GM -190; SG&A -2.9%; tax 17.1% | revenue miss twice; GM miss by 200 bps |
| FY26 | No full-year guide. Pieces given: SG&A up LSD (Q4 FY25 call), tax 19% to 20%, wholesale "modest growth", NIKE Direct no growth (Q1 FY26 call p. 12) | tax raised to "low 20%" (Q1 FY26 call p. 11) | SG&A +0.2%; tax 20.3%; wholesale +6.1%; Direct -5.7% | mostly met; tax slightly above the original range |
| FY27 | Revenue down HSD; EBIT down more than revenue; SG&A down; tax mid-20%; **adjusted EPS $1.15 to $1.35** excluding about $0.15 of Pace charges (Q1 FY27 release seq p. 1; call p. 11 to 12) | none yet | pending | pending |

Only 1 of 4 first full-year revenue guides (FY22 to FY25) was met: FY23. None of the 3 first full-year gross margin guides (FY23 to FY25) was met.

### B3. Hit rates by era (counts from `guidance_vs_actual.csv`, my arithmetic)

| Bucket | Donahoe (calls Jun 2022 to Oct 2024) | Hill (calls Dec 2024 to Jun 2026) |
|---|---|---|
| All scored items | 70: 29 beat, 21 in line, 20 miss (71% met or beat) | 32: 17 beat, 11 in line, 4 miss (88%) |
| Next-quarter items | 26: 16 / 6 / 4 (85%) | 22: 14 / 8 / 0 (100%) |
| Full-year and longer | 44: 13 / 15 / 16 (64%) | 5: 1 / 2 / 2 (60%; tax only) |
| Revenue, full-year and longer | 15: 6 / 2 / 7 (53%) | none given |
| Gross margin, all horizons | 20: 5 / 6 / 9 (55%) | 7: 4 / 3 / 0 (100%) |
| SG&A | 15: 10 / 3 / 2 | 8: 5 / 3 / 0 |
| Dated milestones | not scored here (see section C) | 5: 2 beat, 1 in line, 2 miss (H1 FY26 clean marketplace; Win Now by Dec 2026) |
| Revenue: average gap between actual and guide midpoint, next quarter | +1.2 pts (9 quarters) | +2.3 pts (7 quarters) |
| GM: average gap between actual and guide midpoint, next quarter | +30 bps (8 quarters) | +36 bps (7 quarters) |

The Donahoe column counts the same target more than once when it was re-guided (FY24 revenue was guided four times), which flatters neither era. On FY23 targets alone, Donahoe's team met 80% of items. On FY24 and FY25 targets it met 67%.

**Testing why Hill-era quarterly guides always land:**
1. *Currency tailwinds?* Mostly ruled out. In three of the four FY26 quarters Nike included the FX benefit inside the guide: +1 pt in Q2 (Q1 FY26 call p. 11), +3 pts in Q3 (Q2 FY26 call p. 11) and +2 pts in Q4 (Q3 FY26 call p. 13). Currency-neutral results still met or beat the implied currency-neutral ranges: Q1 FY26 -1%, Q2 0%, Q3 -3%, Q4 -4% (facts CSV).
2. *One-time timing shifts?* These explain individual quarters only. Q3 FY25 included a Cyber Week shift that Nike flagged in the guide itself (Q2 FY25 call p. 14).
3. *Conservative calibration.* This survives. The revenue miss was zero or positive in 6 of 7 quarters, and the gross margin result was above the guide midpoint in 6 of 7 quarters. Denton said he wants guidance "set at a level that we believe is reasonable and attainable" (Q1 FY27 call p. 10).
4. *The underlying trend improving faster than management expected?* This cannot be separated from conservatism with public data. Separating them would need Nike's internal plan or a long run of consensus estimates, and the repo holds neither.

### B4. Changes in guidance practice

| Date | Change | Source |
|---|---|---|
| Mar 21 2023 | Annual guidance given only on the Q4 call: "consistent with my approach over the past few years, I will provide specific guidance for fiscal 24 on our next earnings call" | Q3 FY23 call p. 15 |
| Dec 21 2023 | First "excluding restructuring" framing: SG&A guided excluding the charge, and earnings guided "excluding restructuring charges" | Q2 FY24 call p. 13 to 14 |
| Jun 27 2024 | Non-GAAP diluted EPS excluding restructuring ($3.95) published in the release; Investor Day promised for November 2024 | Q4 FY24 release seq p. 1; Q4 FY24 call p. 27, 30 |
| Oct 1 2024 | FY25 guidance **withdrawn**, quarterly-only guidance from then on, Investor Day **postponed** | Q1 FY25 call p. 3 |
| Mar 31 2026 | Nine-month qualitative outlook (Q4 FY26 to Q2 FY27); promise to "return to providing full year and long-term guidance at our Investor Day in the fall" | Q3 FY26 call p. 12 to 13 |
| Jun 30 2026 | Nine-month revenue outlook lowered to "down low to mid-single digits"; earnings "flattish ... excluding the benefit from tariff recovery"; Investor Day dated Nov 16 and 17 | Q4 FY26 call p. 7, 11 |
| Oct 1 2026 | New CFO Denton reinstates full-year guidance before the Investor Day. It is the first explicit EPS range of the period ($1.15 to $1.35 adjusted, excluding Pace), and the first "Outlook" section in an earnings release. He declined to guide gross margin | Q1 FY27 release seq p. 1; Q1 FY27 call p. 11, 18 |

Long-term targets were last set in June 2021, running through FY25. The CFO acknowledged in December 2023 that "we know that we're due to provide an update on those long-term goals" (Q2 FY24 call p. 18). No update has come in the five years since.

---

## (C) 2017 and 2020/2021 targets versus results

The Oct 25 2017 Investor Day targets are stated in the FY2019 10-K as "long-term financial goals through fiscal 2023, on average, per year" (FY19 10-K p. 24). Nike's IR outlook PDF ("NIKE-INC.-FINANCIAL-OUTLOOK-THROUGH-FISCAL-25.pdf") lists them as "Previous" next to the June 2021 "New (Through FY25)" targets. That PDF adds a capex target of "3-4% of Revenue" to the 2017 set.

| Program | Target | Window | Result (my arithmetic on the facts CSV unless noted) | Verdict |
|---|---|---|---|---|
| Oct 2017 | High single-digit revenue growth | FY17 to FY23 | 6.9% a year ($34,350M to $51,217M); 6.3% a year for FY17 to FY22 | miss |
| Oct 2017 | GM expansion "as much as 50 basis points" a year | FY17 to FY23 | -110 bps in total (44.6% to 43.5%). Peak was FY22 at 46.0%, which is +28 bps a year | miss |
| Oct 2017 | "Slight" SG&A leverage | FY17 to FY23 | SG&A rose from 30.8% to 32.0% of revenue | miss |
| Oct 2017 | Mid-teens EPS growth | FY17 to FY23 | 4.3% a year ($2.51 to $3.23); 8.4% a year for FY17 to FY22 | miss |
| Oct 2017 | ROIC in the low 30s | FY20 to FY23 | 21.5%, 48.8%, 46.5%, 31.5% (10-K ROIC tables, p. 30). FY18 and FY19 are not in the repo | mixed |
| Oct 2017 | International to supply 75% of incremental growth over 5 years (Q2 FY18 call p. 7) | FY17 to FY22 | 75% (Nike Inc. revenue +$12,360M; North America +$3,137M) | met |
| Oct 2017 | North America to grow mid-single digits (Q2 FY18 call p. 14) | FY17 to FY22 | 3.8% a year | miss |
| Oct 2017 | Owned plus partner digital at 30% of business by 2023, from about 15% (restated in Q2 FY19 call p. 6) | FY21 | "over 30% of our total business" (Q1 FY21 call p. 6). This is a management claim; partner digital sales were never disclosed | met early (Covid year) |
| 2015 target, reaffirmed 2017 | $50B revenue by FY2020; then "within the next five years" (Parker, *secondary*: Retail Dive, Oct 26 2017) | FY20 to FY23 | FY20 $37,403M; FY22 $46,710M; first above $50B in FY23 ($51,217M) | late |
| Jun 25 2020 (Consumer Direct Acceleration) | Reach the 30% digital goal "more than two years ahead of plan this coming year"; overall business to reach "50% digital penetration" (Q4 FY20 call p. 3, 6) | FY21 onward | 30% reached. The 50% cannot be checked because partner digital is not disclosed. Owned NIKE Brand Digital peaked at $12.6B, or 26% of NIKE Brand revenue, in FY23 (FY23 10-K p. 33, 36) | 30% met; 50% not shown |
| Jun 24 2021 (through FY25) | Revenue growth HSD to LDD | FY21 to FY25 | 1.0% a year | miss |
| Jun 2021 | Gross margin in the high 40s by FY25 | FY25 | 42.7% (peak 46.0% in FY22) | miss |
| Jun 2021 | EBIT margin in the high teens by FY25 | FY25 | 8.2% (Q4 FY25 release), against 15.5% in FY21 | miss |
| Jun 2021 | EPS growth mid-to-high teens | FY21 to FY25 | -11.7% a year ($3.56 to $2.16) | miss |
| Jun 2021 | ROIC above the low 30s | FY22 to FY25 | 46.5%, 31.5%, 34.9%, 20.2% | mixed |
| Jun 2021 | Capex roughly 3% of revenue | FY22 to FY25 | 1.6%, 1.9%, 1.6%, 0.9% | below target |
| Jun 2021 | NIKE Direct about 60% of NIKE Brand business in FY25 (Q4 FY21 call p. 12) | FY25 | 42% (FY25 10-K p. 29) | miss |
| Jun 2021 | Owned digital 40% and owned plus partner digital 50% in FY25 | FY25 | Owned digital 21.5% ($9.6B of $44.7B; FY25 10-K p. 34, 37) | miss |
| Jun 2021 | Wholesale "roughly flat versus fiscal 21" | FY25 | $25,898M to $25,883M | met |

**February 2020:** I found no separate February 2020 target event in Nike's transcripts or filings. Donahoe's first call was Q3 FY20 on Mar 24 2020. The 2020 digital targets were set on Jun 25 2020, and the 2017 target of 30% digital "by fiscal year 23" was restated there.

**Pattern:** the targets that were met were mix and penetration goals: international share of growth, the 30% digital share and flat wholesale. Every profit and growth-rate target missed: revenue growth, gross margin, SG&A leverage, EBIT margin and EPS. The digital goals were also reached by giving up wholesale and full-price revenue, and that work belongs to other sessions.

---

## (D) The December 2023 "$2 billion" plan, and what it implies for Pace

### D1. What was promised
- "identifying opportunities to deliver up to $2 billion in cumulative cost savings over the next three years" (8-K filed Dec 21, 2023, seq p. 2; Q2 FY24 release seq p. 1).
- The CFO described it as "not just SG&A ... up and down the P&L" (Q2 FY24 call p. 18). The company said it would "reallocate and invest the majority of these savings" (Q2 FY24 call p. 10).
- The 10-Qs and the FY24 10-K described the plan as "a majority of the future annual wage savings ... will be reinvested" (Q3 FY24 10-Q p. 26; FY24 10-K p. 30).
- Charges: $443M ($379M in operating expense, $64M in cost of sales), against the $400M to $450M guided (FY24 10-K p. 91).
- Headcount fell from 83,700 to 79,400 (FY23 and FY24 10-Ks p. 6).

### D2. What Nike later reported as achieved
- **No cumulative savings figure was ever disclosed.** The only update was qualitative: "At the end of Fiscal 24, we have unlocked savings from initiatives up and down our P&L ... we are re-investing nearly one billion dollars in consumer-facing activities in Fiscal 25" (Q4 FY24 call p. 10).
- The phrases "enterprise initiative" and "cost savings" do not appear in the FY2025 or FY2026 10-Ks. The initiative is last named in the Q3 FY25 10-Q (p. 22), and only in a restructuring-charge note.
- The plan's three years end around December 2026, inside FY2027. Pace replaced it on Oct 1 2026, and Nike has not scored the old plan.

### D3. Did overhead dollars actually fall? (`savings_audit_overhead.csv`, my arithmetic)

| FY | Operating overhead reported ($M) | Charges inside it | Overhead ex charges | % of revenue | Path if grown with US private wage ECI* | Gap vs wage path | Path if scaled to revenue | Employees |
|---|---|---|---|---|---|---|---|---|
| FY23 | 12,317 | 0 | 12,317 | 24.05% | 12,317 | 0 | 12,317 | 83,700 |
| FY24 | 12,291 | 379 | 11,912 | 23.19% | 12,822 (+4.1%) | 910 | 12,352 | 79,400 |
| FY25 | 11,399 | 0 | 11,399 | 24.62% | 13,271 (+3.5%) | 1,872 | 11,137 | 77,800 |
| FY26 | 11,360 | 231 | 11,129 | 23.99% | 13,682 (+3.1%) | 2,553 | 11,158 | 73,000 |
| Q1 FY27 | 2,658 (-6.0% y/y) | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

*ECI = BLS Employment Cost Index, wages and salaries, private industry, 12-month change (series CIU2020000000000A, api.bls.gov). The reading used is the calendar Q2 in which each fiscal year ends. It is a US proxy for a global workforce.

Charges: $379M in FY24 (FY24 10-K p. 91; the FY24 10-K p. 36 says overhead was flat because savings "were offset by restructuring charges"). $231M of FY26 severance sat in overhead (FY26 10-K p. 89). Overhead figures are from the facts CSV. Q1 FY27 is from the Q1 FY27 10-Q p. 24.

Readings:
- **Nominal overhead excluding charges fell $1,188M (-9.6%) from FY23 to FY26.** Revenue fell 9.4% over the same years. Overhead per employee rose from $147.2K to $152.5K.
- **Against a wage-inflation path, the cumulative "avoided" overhead is about $5.3B over FY24 to FY26.** That is far more than $2B, but it is not a reported savings number. It also includes cost Nike avoided for reasons other than the plan (alternatives tested below).
- **Against a revenue-scaled path, the gap is close to zero.** It was +$440M in FY24, -$262M in FY25 and +$29M in FY26. Overhead moved in step with revenue, so there was no operating leverage.
- **SG&A as a share of revenue rose from 32.0% (FY23) to 34.7% (FY26).** Demand creation rose $694M, from $4,060M to $4,754M, which is consistent with the promised reinvestment. EBIT margin went from 12.1% (FY23) to 12.7% (FY24) to 8.2% (FY25) to 8.3% (FY26) (facts CSV). Whatever was saved did not show up in the EBIT margin.

**Alternative explanations for the overhead decline:**
1. *The savings plan itself.* Consistent with the record: headcount fell 12.8% from FY23 to FY26, and the 10-Ks cite "lower wage-related expenses" in FY24 and FY25 and "lower other administrative costs" in FY25 and FY26 (FY24 10-K p. 36; FY25 10-K p. 35; FY26 10-K p. 34).
2. *Lower incentive pay because targets were missed.* Plausible but not quantified. The FY26 bonus plan paid 74% to 78% (2026 proxy p. 32), and filings do not split wage cost into base pay and incentive pay.
3. *Lower NIKE Direct variable costs as digital revenue fell* (from $12.6B to $8.6B, FY23 10-K p. 33 to FY26 10-K p. 33). Plausible: overhead includes "NIKE Direct variable costs" (FY23 10-K p. 34). The amount is not disclosed.
4. *Currency.* Ruled out as a source of the decline. FX was not material in FY24 or FY25 and added about 1 point to overhead in FY26 (FY26 10-K p. 34).

The filings cannot separate 1 from 2 and 3. Separating them would need wage expense split into base and incentive, and NIKE Direct variable cost disclosed in dollars.

### D4. What this implies for Pace ("approximately $2.5 billion in cumulative savings through fiscal 2031", 8-K filed Oct 1, 2026, seq p. 2)
- **The terms are looser than they look.** The savings are "stated before the expected pre-tax charges ... and any future reinvestment" (8-K Oct 1 2026 seq p. 2; Q1 FY27 10-Q p. 20). The charges are about $1.0B, plus $0.3B of FY26 severance on top (Q1 FY27 10-Q p. 18). Net of charges, the savings are about $1.2B to $1.5B cumulative (my arithmetic). Nike also "intend[s] to reinvest a portion" (Q1 FY27 call p. 10).
- **It is a smaller annual ask than 2023, and back-loaded.** $2.5B over five years is $0.5B a year on average, against $0.67B a year for the 2023 plan (my arithmetic). The "majority of the program savings" falls in FY29 and FY30 (Q1 FY27 call p. 10). Even fully delivered, $0.5B is 4.5% of FY26 overhead excluding charges, or about 110 bps of FY26 revenue (my arithmetic). At a 25% tax rate and 1,485M shares, it is about $0.25 of EPS a year (my arithmetic; share count from the Q1 FY27 10-Q cover).
- **Nike can already show overhead falling.** Q1 FY27 overhead was -6% (Q1 FY27 10-Q p. 24), and Denton said "we are beginning to see savings now even through Q1" (Q1 FY27 call p. 24). The 2023 record shows the risk: falling overhead does not prove the program, because revenue can fall just as fast.
- **The credibility test is disclosure.** Denton promised "the measures we will use to assess our progress" at the Investor Day (Q1 FY27 call p. 10). A dated, published scorecard of gross savings, charges, reinvestment and net effect, reported each quarter, would break from the 2023 practice. Without one, the record suggests treating the $2.5B as a ceiling with no accountability attached.

---

## (E) Price reactions (`price_reactions.csv`, market data, my arithmetic)

Nike reports after the close. "Day 0" is the close on the release date. "1d" and "5d" run from that close to the close one and five trading days later. "Drift" runs from day 1 to day 20. "Excess" is the move minus the S&P 500 over the same window.

| Event | Guidance signal | Day-0 close | 1d | 5d | 20d | Drift d1 to d20 | Excess 1d | Excess 20d |
|---|---|---|---|---|---|---|---|---|
| Q4 FY22 (Jun 27 2022) | initial FY23 | 110.50 | -7.0% | -5.6% | -4.8% | +2.4% | -5.0 | -5.3 |
| Q1 FY23 (Sep 29 2022) | GM cut | 95.33 | -12.8% | -5.4% | -5.0% | +8.9% | -11.3 | -9.6 |
| Q2 FY23 (Dec 20 2022) | raise | 103.21 | +12.2% | +11.4% | +22.7% | +9.4% | +10.7 | +18.7 |
| Q3 FY23 (Mar 21 2023) | raise (GM to low end) | 125.61 | -4.9% | -6.2% | 0.0% | +5.2% | -3.3 | -3.8 |
| Q4 FY23 (Jun 29 2023) | initial FY24 | 113.37 | -2.6% | -7.9% | -4.2% | -1.6% | -3.8 | -8.4 |
| Q1 FY24 (Sep 28 2023) | maintain | 89.63 | +6.7% | +6.9% | +11.6% | +4.6% | +7.0 | +15.4 |
| Q2 FY24 (Dec 21 2023) | cut; $2B plan | 122.53 | -11.8% | -11.4% | -16.8% | -5.7% | -12.0 | -19.3 |
| Q3 FY24 (Mar 21 2024) | FY25 preview down | 100.82 | -6.9% | -6.8% | -6.2% | +0.8% | -6.8 | -1.0 |
| Q4 FY24 (Jun 27 2024) | FY25 cut | 94.19 | -20.0% | -19.9% | -23.0% | -3.7% | -19.6 | -22.6 |
| Hill named CEO (Sep 19 2024) | not guidance | 80.98 | +6.8% | +10.4% | +3.0% | -3.6% | +7.0 | +0.8 |
| Q1 FY25 (Oct 1 2024) | withdrawn | 89.13 | -6.8% | -9.4% | -12.0% | -5.6% | -6.8 | -14.2 |
| Q2 FY25 (Dec 19 2024) | quarterly | 77.10 | -0.2% | -0.9% | -4.0% | -3.8% | -1.3 | -7.7 |
| Q3 FY25 (Mar 20 2025) | quarterly | 71.86 | -5.5% | -8.4% | -22.4% | -17.9% | -5.6 | -15.7 |
| Q4 FY25 (Jun 26 2025) | quarterly | 62.54 | +15.2% | +22.1% | +22.0% | +5.9% | +14.7 | +18.0 |
| Q1 FY26 (Sep 30 2025) | quarterly | 69.73 | +6.4% | -1.2% | -3.3% | -9.1% | +6.1 | -6.3 |
| Q2 FY26 (Dec 18 2025) | quarterly | 65.63 | -10.5% | -7.2% | -3.0% | +8.4% | -11.4 | -3.3 |
| Q3 FY26 (Mar 31 2026) | nine-month outlook | 52.82 | -15.5% | -18.3% | -16.0% | -0.6% | -16.2 | -25.3 |
| Q4 FY26 (Jun 30 2026) | nine-month outlook cut | 41.05 | +4.9% | +4.5% | +5.3% | +0.4% | +5.1 | +7.7 |
| Q1 FY27 (Oct 1 2026) | FY27 guide, below consensus; Pace | 35.15 | -3.6% | -1.2% | n/a | n/a | -4.3 | n/a |

**Group averages:**

| Group | Events | Avg 1d | Avg 5d | Avg drift d1 to d20 | Avg excess 20d |
|---|---|---|---|---|---|
| Cuts or withdrawals | 6 | -8.9% | -8.1% | -0.8% | -9.8 pts |
| Raise, maintain or initial guide | 5 | +0.9% | n/a | +4.0% | n/a |
| Hill quarterly-only quarters | 5 | +1.1% | n/a | -3.3% | n/a |
| All events with a 1-day move of -5% or worse (since 2019) | 11 | -10.1% | n/a | 0.0% | -11.3 pts |

Since 2019 the average absolute 1-day move on earnings is 7.5%. Over the tracker window (18 events) it is 8.5%. The share price fell from $110.50 (Jun 27 2022) to $35.35 (Oct 12 2026), down 68%.

**Readings:**
- *Drift after misses is not systematic.* In 2024 the cuts kept falling after day 1: Q2 FY24 -5.7%, Q4 FY24 -3.7%, Q1 FY25 -5.6%. The September 2022 cut instead rebounded +8.9%. Averaged over all -5% days, the drift is 0.0%, so most of the damage is priced on day one.
- *Beating Nike's own guidance tells you little about the price reaction.* Every Hill-era quarter from Q3 FY25 to Q4 FY26 beat or met the revenue guide. Day-one moves still ranged from -15.5% (Q3 FY26) to +15.2% (Q4 FY25). The market reacts to the forward outlook against consensus. Consensus history is not in the repo, apart from the post-print FY27 EPS cut from 1.71 to 1.29 recorded in `research_notes/thesis_tests/consensus_and_valuation.md`.
- *Limitation:* there is no consensus series before Oct 2026, so the "guidance signal" column shows the direction of Nike's own guide, not the surprise against the Street.

---

## (F) The Nov 16 to 17, 2026 Investor Day

**Facts:**
- The date comes from Nike: "our Investor Day on November 16 and 17" (Q4 FY26 call p. 7).
- Nike's stated agenda: "a clearer view of our long-term growth" (Q1 FY27 call p. 7), plus Pace "additional details on these actions, our investment priorities and the measures we will use to assess our progress" (Q1 FY27 call p. 10).
- It will be the first Investor Day since October 2017. The one promised for November 2024 (Q4 FY24 call p. 27) was postponed (Q1 FY25 call p. 3).

**Previews** (*secondary*):
- Jefferies (Randal Konik, Buy, $75), via Parameter, Sep 28 2026: a new CFO "owns none of the prior guidance". The key question is "whether Denton establishes realistic fiscal 2027 and 2028 targets that the organization can consistently achieve or exceed." Source: https://parameter.io/nike-nke-stock-could-double-jefferies-maintains-bullish-stance-before-thursdays-earnings/
- Piper Sandler (Abbie Zvejnieks, Overweight, $75), via 24/7 Wall St, Oct 2 2026: the bull case rests on cost cuts freeing "$600 million to $1 billion in yearly savings", lifting operating margin "about 130 to 200 basis points". Source: https://247wallst.com/investing/2026/10/02/will-nike-ever-stop-falling-one-analyst-is-sure-that-buying-now-will-yield-100-gains/
- ms-aktuell.de, Sep 5 2026: specific multi-year targets "has not yet been officially set". The open questions are how running and wholesale gains turn into broad growth, how China stabilizes, and what financial framework Nike sets. Source: https://ms-aktuell.de/?p=156159
- CNBC (Oct 2 2026) and WWD (Denton preview) returned 403 or paywall pages and were not used.

**Market context** (`consensus_and_valuation.md`):
- FY28 consensus EPS is about $1.65, down 26% in 30 days.
- The reverse DCF implies a steady-state EBIT margin of about 13.8%, against 8.3% in FY26.
- The Dec 18 2026 at-the-money straddle prices a move of about 13.3%. That expiry spans the Q2 FY27 report on about Dec 17 2026, not the Investor Day.

**Three scenarios** (my inference; magnitudes anchored on this note's event history, not forecasts):

| Scenario | What Nike would announce | Credibility test against the record | Likely stock reaction |
|---|---|---|---|
| **1. Reset low and vague** | No dated margin target ("expand margins over time"); revenue growth from FY29 only; Pace described again with no scorecard; FY28 EPS framed below the $1.65 consensus | Repeats the 2023 pattern of a headline number with no tracking | Negative, comparable to past withdrawal and cut events (-7% to -12% on day one), because FY28 and FY29 estimates would need to fall again |
| **2. Credible floor (base)** | Dated targets set below the 2021 levels: EBIT margin back to about 10% to 12% by FY29 or FY30; revenue growth in the low to mid single digits from FY28; Pace scorecard of gross savings, charges, reinvestment and net savings reported each quarter; capex about 2% of revenue; dividend kept | Matches Denton's "reasonable and attainable" framing (Q1 FY27 call p. 10) and the Hill-era record of beating conservative quarterly guides | Modestly positive. The new numbers would sit near the reverse-DCF path, and the scorecard lowers the discount for missed milestones |
| **3. Ambitious return to the 2021 algorithm** | High-teens EBIT margin or high-single-digit growth by FY30 or FY31; large buyback; Pace net savings above $2.5B | Every profit target in 2017 and 2021 missed: high-teens EBIT by FY25 became 8.2%. Pace alone covers only about 110 to 200 bps of margin (my arithmetic; Piper 130 to 200 bps, secondary). The rest would need gross margin recovery, owned by other sessions | Possibly a positive day one, but this note's record argues for fading it. The 2021 targets drew +15.5% on day one (Q4 FY21 release, Jun 24 2021) and then missed |

**Timing for the case competition:**
- The Investor Day (Nov 16 to 17) falls after the Nov 1 submission deadline and before the Nov 19 finals.
- The written pitch should therefore make the rating depend on Scenario 2. It should also state ahead of time which disclosures would confirm or break the thesis: a dated EBIT margin target, a Pace net-savings scorecard and an FY28 revenue direction.
- The finals deck needs one slide prepared in advance for each scenario, filled in on Nov 17 and 18 with what Nike actually said.

---

## (G) Verdict on credibility

1. **Short-term numbers: reliable, and conservative under Hill and Denton.** Quarterly revenue and gross margin guides have been met or beaten 22 of 22 times since December 2024. Models should treat quarterly guidance as a floor.
2. **Full-year and multi-year numbers: not reliable.**
   - Only 1 of 4 first full-year revenue guides (FY22 to FY25) was met, and 0 of 3 first full-year gross margin guides.
   - Every profit and growth target from 2017 and 2021 missed, by wide margins: EBIT margin 8.2% against high teens; EPS growth -11.7% a year against mid-to-high teens.
   - Dated milestones slipped twice under Hill: the H1 FY26 clean marketplace and Win Now by December 2026.
3. **Cost programs: the dollars are real, but they have not been shown to be "savings" and did not reach margins.** The 2023 $2B plan was never scored. Overhead fell exactly in line with revenue, and SG&A as a share of revenue rose 270 bps. Nike reports achievement only qualitatively.
4. **Implication for the pitch:**
   - Do not credit Pace's $2.5B beyond what overhead as a share of revenue shows each quarter.
   - Haircut any Investor Day margin target by the historical gap. For example, the FY25 EBIT target missed by about 900 bps (high teens, taken as about 17%, against 8.2%; my arithmetic).
   - The cleanest test of whether management has become more credible is whether the November targets come with a measurable scorecard. Until then, the track record supports a valuation discount for execution risk, not a premium for a turnaround story.

---

## Gaps and limitations
- The consensus history needed to label the market surprise on each event is not in the repo. The verdicts here are against Nike's own guidance only.
- Q1 FY24 has only the prepared-remarks PDF on Nike IR, so any Q&A guidance colour from that quarter is missing.
- ECI is a US private-sector index, while Nike's workforce is global (no global wage index was sourced). Overhead also includes non-wage costs, so the wage-path comparison overstates the gap. The revenue-scaled comparison is the more conservative test.
- Nike's restructuring note does not say whether all $379M of FY24 charges sat in operating overhead rather than demand creation. It reads "within Operating overhead expense" only in the Q4 release ($39M). Treating all $379M as overhead is my inference, supported by FY24 10-K p. 36.
- ROIC for FY18 and FY19 is not in the facts CSV.
- The Investor Day previews are from secondary outlets. Bloomberg, Reuters, CNBC and WWD were blocked or paywalled.
