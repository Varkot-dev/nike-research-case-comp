# G9: Nike's record against its own quarterly guidance, Q2 FY25 to Q1 FY27

Prepared 2026-10-15. Nike fiscal years end May 31. Scope: every quarter reported from Q2 FY25 (Dec 19 2024) through Q1 FY27 (Oct 1 2026), scored against the guidance Nike gave on the prior call. Companion CSV: `research_notes/Smoking gun hunt/G9_guidance_record.csv` (one row per guide item, with verbatim wording, page, band, midpoint, actual, scores).

## 1. Answer

**Which of the three documents is right?** All three are arithmetically correct about different things, and none is complete.

| Document | Claim | Verdict on primary sources |
|---|---|---|
| `research_notes/19_management_track_record.md` | 22 of 22 next-quarter items met or beaten | True only if "met" means "inside or above the guided range", and only for 7 quarters (Q3 FY25 to Q1 FY27) of revenue, gross margin, SG&A (21 items) plus the Q2 FY26 tax rate (1 item). It leaves out the Q2 FY25 guide and both full-year tax-rate guides that were missed. Against the midpoint it is 21 of 22 (tolerance scoring) or 19 of 22 (strict). |
| `slides/pptx/build_deck.js`, `research_notes/Long or short cruxes/earnings_calls_analysis.md` | 14 of 14 quarterly guides met or beaten | True against the range for 7 quarters x (revenue, gross margin). Against the midpoint it is 13 of 14 (tolerance) or 12 of 14 (strict). "Beaten" is wrong for Q1 FY27 revenue. |
| `research_notes/Deep dives Oct 14/D4_long_case.md` | Q1 FY27 revenue fell below the guide midpoint and missed LSEG consensus | Below the midpoint: true (-4.33% against a -3.5% midpoint). "Missed the guide": false, it was inside the range and management said so on the call (Q1 FY27 call p. 2, quoted in section 7). The LSEG miss is a consensus fact, not a guidance fact (secondary source, section 7). |

**The one sentence for the deck and the report:**

> In the eight quarters reported since December 2024, Nike landed inside or above its own guided range on revenue and gross margin 16 times out of 16, but Q1 FY27 revenue (down 4.3% against a guide of down low to mid single digits, midpoint about -3.5%) was the first to fall below the midpoint.

Use this in place of "met or beaten 14 of 14" and "22 of 22". If a slide needs a shorter form: "Quarterly revenue and gross margin guides: 16 of 16 inside or above the range since Q2 FY25; Q1 FY27 revenue was the first below the midpoint." Do not write "beat" or "sandbag" for the whole run, and do not drop the full-year caveat in section 4.

## 2. Scoring rules (stated before looking at results)

- **Guide source.** The guide for a quarter is what the CFO said in the outlook section of the prior quarter's earnings call (repo transcript copies in `data/hunt/earnings_calls/transcripts/`, cited by PDF page). Every transcript was re-downloaded from the investors.nike.com asset store and word-compared with the repo copy (section 10). Actuals come from each quarter's earnings release, Form 8-K Exhibit 99.1, fetched from the investors.nike.com mirror (accession numbers in section 7). Releases have no printed pages, so the source column names the table or sentence.
- **Numeric ranges are used as stated.** Word bands use the repo convention in `research_notes/19_management_track_record.md` (my convention, not Nike's): flat -1 to +1; slightly up 0 to +2; slightly down -2 to 0; low single digits (LSD) 1 to 3; mid single digits (MSD) 4 to 6; high single digits 7 to 9; low double digits 10 to 13; high teens 17 to 19; mid-teens 14 to 16; "low 20% range" 20 to 23; "approximately N bps" N +/- 25 bps; "slightly positive" gross margin 0 to +50 bps. "Low to mid single digits" is 1 to 6. Only 9 of the 29 scored items are numeric ranges in Nike's own words (7 revenue or gross margin ranges, the Q4 FY26 revenue range, and the FY26 tax range of 19% to 20%); the rest depend on these bands.
- **Direction.** Higher is better for revenue growth and gross margin. Lower is better for SG&A growth and tax rate (scored as favorable, as the repo does; a cost under-run can reflect deliberate cuts rather than skill, and filings cannot separate the two).
- **Score against the range:** beat (better than the favorable edge), in range, miss (worse than the unfavorable edge).
- **Score against the midpoint:** beat or miss if the result is more than 0.5 pt (revenue, SG&A, tax) or 25 bps (gross margin) from the midpoint in the favorable or unfavorable direction, otherwise met. The tolerance exists because word bands are coarse and releases round to 10 bps. A "strict" column in the CSV drops the tolerance (any shortfall against the midpoint counts).
- **Currency.** Every revenue guide was a reported-currency guide. Nike stated the FX effect inside the guide in 4 of 8 quarters (section 3).
- **Era.** The Q2 FY25 guide was given on Oct 1 2024 under Donahoe and Friend, 13 days before Hill started (Oct 14 2024). The repo's "Hill era" starts one quarter later (Q3 FY25). Both cuts are shown.

## 3. Revenue guides (reported growth, year over year)
| Target quarter | Guide call, date, PDF page | Guide wording (verbatim) | Band used | Midpoint | Actual | Actual minus midpoint (favorable +) | Vs range | Vs midpoint | Actual source |
|---|---|---|---|---|---|---|---|---|---|
| Q2 FY25 | Q1 FY25 call, 2024-10-01, p. 9 | "We expect Q2 revenues to be down in the 8% to 10% range." | -10.0% to -8.0% | -9.0% | -7.72% | +1.28 pts | beat | beat | Q2 FY25 release (8-K Ex. 99.1), income statement table: revenues $12,354M vs $13,388M; text: down 8 percent reported, down 9 percent currency-neutral |
| Q3 FY25 | Q2 FY25 call, 2024-12-19, p. 13 to 14 | "We expect Q3 revenues to be down low double digits." | -13.0% to -10.0% | -11.5% | -9.33% | +2.17 pts | beat | beat | Q3 FY25 release, revenues $11,269M vs $12,429M (text: down 9 percent reported, down 7 percent currency-neutral) |
| Q4 FY25 | Q3 FY25 call, 2025-03-20, p. 16 | "We expect Q4 revenues to be down in the mid-teens range, albeit at the low end." | -16.0% to -14.0% | -15.0% | -11.97% | +3.03 pts | beat | beat | Q4 FY25 release, revenues $11,097M vs $12,606M (text: down 12 percent reported, down 11 percent currency-neutral) |
| Q1 FY26 | Q4 FY25 call, 2025-06-26, p. 13 | "We expect Q1 revenues to be down mid-single digits." | -6.0% to -4.0% | -5.0% | +1.13% | +6.13 pts | beat | beat | Q1 FY26 release, revenues $11,720M vs $11,589M (text: up 1 percent reported, down 1 percent currency-neutral) |
| Q2 FY26 | Q1 FY26 call, 2025-09-30, p. 11 | "We expect Q2 revenues to be down low single digits, including one point of benefit from foreign exchange." | -3.0% to -1.0% | -2.0% | +0.59% | +2.59 pts | beat | beat | Q2 FY26 release, revenues $12,427M vs $12,354M (text: up 1 percent reported, flat currency-neutral) |
| Q3 FY26 | Q2 FY26 call, 2025-12-18, p. 11 | "We expect Q3 revenues to be down low single digits, with modest growth in North America ... as well as a 3-point benefit from foreign exchange." | -3.0% to -1.0% | -2.0% | +0.09% | +2.09 pts | beat | beat | Q3 FY26 release, revenues $11,279M vs $11,269M (text: flat reported, down 3 percent currency-neutral) |
| Q4 FY26 | Q3 FY26 call, 2026-03-31, p. 13 | "We expect revenues in Q4 to be down 2% to 4% ... We anticipate a 2-point benefit from foreign exchange." | -4.0% to -2.0% | -3.0% | -1.13% | +1.87 pts | beat | beat | Q4 FY26 release, revenues $10,972M vs $11,097M (text: down 1 percent reported, down 4 percent currency-neutral) |
| Q1 FY27 | Q4 FY26 call, 2026-06-30, p. 12 | "we expect reported revenues to be down low to mid-single digits with no expected benefit from foreign exchange and currency-neutral revenue growth consistent with recent performance." | -6.0% to -1.0% | -3.5% | -4.33% | -0.83 pts | in range | miss | Q1 FY27 release, revenues $11,213M vs $11,720M (text: down 4 percent reported, down 5 percent currency-neutral) |

Actual growth is derived: reported revenue divided by prior-year revenue from the same release table, to two decimals. Release text rounds (for example "down 4 percent").

**Currency-neutral view.** Implied currency-neutral band = reported band minus the FX effect Nike stated in the guide. Only quarters where Nike gave the number can be converted.

| Target quarter | FX effect stated in guide (call, page) | Implied currency-neutral midpoint | Actual currency-neutral (release text) | Gap | Reported gap (from table above) |
|---|---|---|---|---|---|
| Q2 FY25 | not stated | n/a | -9% | n/a | +1.28 pts |
| Q3 FY25 | "worsening foreign exchange headwinds", size not stated (Q2 FY25 call p. 14) | n/a | -7% | n/a | +2.17 pts |
| Q4 FY25 | 2 points of headwind (Q3 FY25 call p. 16) | -13% (-15% plus 2) | -11% | +2 pts | +3.03 pts |
| Q1 FY26 | not stated (Q4 FY25 call p. 13) | n/a | -1% | n/a | +6.13 pts |
| Q2 FY26 | 1 point of benefit (Q1 FY26 call p. 11) | -3% (-2% minus 1) | 0% (flat) | +3 pts | +2.59 pts |
| Q3 FY26 | 3 points of benefit (Q2 FY26 call p. 11) | -5% (-2% minus 3) | -3% | +2 pts | +2.09 pts |
| Q4 FY26 | 2 points of benefit (Q3 FY26 call p. 13) | -5% (-3% minus 2) | -4% | +1 pt | +1.87 pts |
| Q1 FY27 | no benefit expected (Q4 FY26 call p. 12) | -3.5% | -5% | -1.5 pts | -0.83 pts |

Reading: currency does not explain the beats in the four quarters where it can be tested (the currency-neutral gap is positive in each, and the FX effect was inside the guide). It makes Q1 FY27 slightly worse: reported -4.3% against currency-neutral -5% means a roughly 1 point FX tailwind arrived that the guide did not contain, and the currency-neutral shortfall is -1.5 pts. Q1 FY26 (reported +1.1%, currency-neutral -1%) remains above the -6% to -4% band either way.

## 4. Gross margin guides (change versus prior year, bps)
| Target quarter | Guide call, date, PDF page | Guide wording (verbatim) | Band used | Midpoint | Actual | Actual minus midpoint (favorable +) | Vs range | Vs midpoint | Actual source |
|---|---|---|---|---|---|---|---|---|---|
| Q2 FY25 | Q1 FY25 call, 2024-10-01, p. 9 | "We expect Q2 gross margins to be down approximately 150 basis points" | -175 bps to -125 bps | -150 bps | -100 bps | +50 bps | beat | beat | Q2 FY25 release, 'Gross margin decreased 100 basis points to 43.6 percent' |
| Q3 FY25 | Q2 FY25 call, 2024-12-19, p. 14 | "We expect Q3 gross margins to be down approximately 300 to 350 basis points, including restructuring charges during the same period in the prior year." | -350 bps to -300 bps | -325 bps | -330 bps | -5 bps | in range | met | Q3 FY25 release, 'Gross margin decreased 330 basis points to 41.5 percent' |
| Q4 FY25 | Q3 FY25 call, 2025-03-20, p. 16 | "We expect Q4 gross margins to be down approximately 400-500 basis points including restructuring charges during the same period last year." | -500 bps to -400 bps | -450 bps | -440 bps | +10 bps | in range | met | Q4 FY25 release, 'Gross margin decreased 440 basis points to 40.3 percent' |
| Q1 FY26 | Q4 FY25 call, 2025-06-26, p. 13 | "We expect Q1 gross margins to be down approximately 350 to 425 basis points. This includes approximately 100 basis points negative impact due to the new tariffs" | -425 bps to -350 bps | -388 bps | -320 bps | +68 bps | beat | beat | Q1 FY26 release, 'Gross margin decreased 320 basis points to 42.2 percent' |
| Q2 FY26 | Q1 FY26 call, 2025-09-30, p. 11 | "We expect Q2 gross margins to be down approximately 300 to 375 basis points including a net headwind of 175 basis points from the new incremental tariffs." | -375 bps to -300 bps | -338 bps | -300 bps | +38 bps | in range | beat | Q2 FY26 release, 'Gross margin decreased 300 basis points to 40.6 percent' |
| Q3 FY26 | Q2 FY26 call, 2025-12-18, p. 11 to 12 | "We expect Q3 gross margins to be down approximately 175 to 225 basis points." | -225 bps to -175 bps | -200 bps | -130 bps | +70 bps | beat | beat | Q3 FY26 release, 'Gross margin decreased 130 basis points to 40.2 percent' |
| Q4 FY26 | Q3 FY26 call, 2026-03-31, p. 13 | "We expect sequential improvement in gross margin with Q4 down approximately 25 to 75 basis points, including 250 basis points due to higher tariffs in North America." | -75 bps to -25 bps | -50 bps | -10 bps | +40 bps | beat | beat | Q4 FY26 call p. 8 (ex-benefit gross margin 40.2%, down 10 bps; benefit 'not included in our previous financial guidance') and p. 22 ('better than how we guided') |
| Q4 FY26 | Q3 FY26 call, 2026-03-31, p. 13 | "We expect sequential improvement in gross margin with Q4 down approximately 25 to 75 basis points, including 250 basis points due to higher tariffs in North America." | -75 bps to -25 bps | -50 bps | +890 bps | +940 bps | beat | beat | Q4 FY26 release, 'Gross margin increased 890 basis points to 49.2 percent' |
| Q1 FY27 | Q4 FY26 call, 2026-06-30, p. 12 | "We expect gross margin in Q1 to be slightly positive." | 0 bps to +50 bps | +25 bps | +60 bps | +35 bps | beat | beat | Q1 FY27 release, 'Gross margin expanded 60 basis points to 42.8 percent' |

**Q4 FY26 one-time item.** Reported gross margin rose 890 bps to 49.2% because Nike booked a $986M benefit for expected recovery of IEEPA tariffs (Q4 FY26 call p. 8). Nike states the benefit "was not included in our previous financial guidance" (p. 8), that excluding it gross margin was 40.2%, "down 10 basis points" (p. 8), and "better than how we guided. We guided to be down 25 to 75 basis points" (p. 22). The scored row therefore uses -10 bps. The as-reported +890 bps row is in the CSV as a sensitivity row and is not counted. Either way the result is a beat; the ex-item beat is 40 bps above the -50 midpoint.

## 5. SG&A guides (dollar growth, year over year)
| Target quarter | Guide call, date, PDF page | Guide wording (verbatim) | Band used | Midpoint | Actual | Actual minus midpoint (favorable +) | Vs range | Vs midpoint | Actual source |
|---|---|---|---|---|---|---|---|---|---|
| Q2 FY25 | Q1 FY25 call, 2024-10-01, p. 9 | "We expect SG&A to be roughly flat versus the prior year" | -1.0% to +1.0% | +0.0% | -3.40% | +3.40 pts | beat | beat | Q2 FY25 release, total selling and administrative expense $4,005M vs $4,146M (text: decreased 3 percent) |
| Q3 FY25 | Q2 FY25 call, 2024-12-19, p. 14 | "We expect Q3 SG&A dollars to be slightly down year-over-year, including restructuring charges in the prior year." | -2.0% to +0.0% | -1.0% | -8.02% | +7.02 pts | beat | beat | Q3 FY25 release, total selling and administrative expense $3,887M vs $4,226M |
| Q4 FY25 | Q3 FY25 call, 2025-03-20, p. 16 | "We expect Q4 SG&A dollars to be up low to mid-single-digits including restructuring charges in the prior year." | +1.0% to +6.0% | +3.5% | +1.47% | +2.03 pts | in range | beat | Q4 FY25 release, total selling and administrative expense $4,148M vs $4,088M |
| Q1 FY26 | Q4 FY25 call, 2025-06-26, p. 13 | "We expect Q1 SG&A dollars to be up low single digits." | +1.0% to +3.0% | +2.0% | -0.79% | +2.79 pts | beat | beat | Q1 FY26 release, total selling and administrative expense $4,016M vs $4,048M |
| Q2 FY26 | Q1 FY26 call, 2025-09-30, p. 11 | "We expect Q2 SG&A dollars to be up high single digits" | +7.0% to +9.0% | +8.0% | +0.85% | +7.15 pts | beat | beat | Q2 FY26 release, total selling and administrative expense $4,039M vs $4,005M |
| Q3 FY26 | Q2 FY26 call, 2025-12-18, p. 12 | "We expect Q3 SG&A dollars to be up low single digits due to higher demand creation and investments in our sport offense." | +1.0% to +3.0% | +2.0% | +2.32% | -0.32 pts | in range | met | Q3 FY26 release, total selling and administrative expense $3,977M vs $3,887M |
| Q4 FY26 | Q3 FY26 call, 2026-03-31, p. 13 | "We expect Q4 SG&A dollars to be flat to down slightly." | -2.0% to +1.0% | -0.5% | -1.59% | +1.09 pts | in range | beat | Q4 FY26 release, total selling and administrative expense $4,082M vs $4,148M |
| Q1 FY27 | Q4 FY26 call, 2026-06-30, p. 12 | "We expect Q1 SG&A dollars to be flat with operating overhead declining" | -1.0% to +1.0% | +0.0% | -2.64% | +2.64 pts | beat | beat | Q1 FY27 release, total selling and administrative expense $3,910M vs $4,016M |

SG&A beats are cost under-runs. Seven of eight were favorable by more than the tolerance, and the filings cannot say how much was deliberate cost cutting (Pace and the March 2026 realignment) versus slower spending than planned. Treat these rows as supporting, not as proof of guidance skill.

## 6. Tax-rate guides
| Target quarter | Guide call, date, PDF page | Guide wording (verbatim) | Band used | Midpoint | Actual | Actual minus midpoint (favorable +) | Vs range | Vs midpoint | Actual source |
|---|---|---|---|---|---|---|---|---|---|
| Q2 FY25 | Q1 FY25 call, 2024-10-01, p. 9 | "we expect our effective tax rate to be in the high teens range." | 17.0% to 19.0% | 18.0% | 17.9% | +0.10 pts | in range | met | Q2 FY25 release, 'The effective tax rate was 17.9 percent' |
| FY25 (full year) | Q3 FY25 call, 2025-03-20, p. 16 | "we expect the tax rate for the full year to be in the mid-teens range." | 14.0% to 16.0% | 15.0% | 17.1% | -2.10 pts | miss | miss | Q4 FY25 release, 'The effective tax rate was 17.1 percent' (fiscal 2025) |
| FY26 (full year) | Q4 FY25 call, 2025-06-26, p. 13 | "we expect the tax rate for the full year to be 19% to 20%" | 19.0% to 20.0% | 19.5% | 20.3% | -0.80 pts | miss | miss | Q4 FY26 release, 'The effective tax rate was 20.3 percent' (fiscal 2026) |
| Q2 FY26 | Q1 FY26 call, 2025-09-30, p. 11 to 12 | "We expect the tax rate for the second quarter and the full year to be in the low 20% range" | 20.0% to 23.0% | 21.5% | 20.7% | +0.80 pts | in range | beat | Q2 FY26 release, 'The effective tax rate was 20.7 percent' |
| FY26 (full year) | Q1 FY26 call, 2025-09-30, p. 11 to 12 | "We expect the tax rate for the second quarter and the full year to be in the low 20% range" | 20.0% to 23.0% | 21.5% | 20.3% | +1.20 pts | in range | beat | Q4 FY26 release, 'The effective tax rate was 20.3 percent' (fiscal 2026) |
| FY26 (full year) | Q3 FY26 call, 2026-03-31, p. 13 | "we expect our full year tax rate to be in the low 20% range." | 20.0% to 23.0% | 21.5% | 20.3% | +1.20 pts | in range | beat | Q4 FY26 release, 'The effective tax rate was 20.3 percent' (fiscal 2026) |
| FY27 (full year) | Q4 FY26 call, 2026-06-30, p. 12 | "We expect our full year tax rate to be in the low 20% range." | 20.0% to 23.0% | 21.5% | 22.7% | -1.20 pts | pending | pending | Q1 FY27 release, 'The effective tax rate was 22.7 percent' (Q1 only; full year not reported) |

Reading: quarterly tax guides were met both times (Q2 FY25 high teens, 17.9%; Q2 FY26 low 20s, 20.7%). **Full-year tax guides are the weak spot the 22-of-22 count hides.** FY25: guided "mid-teens" on the Q3 FY25 call, actual 17.1%, 1.1 pts above the 16% top, because Q4 tax was 33.6% on $318M of pre-tax income (Q4 FY25 release). FY26: guided 19% to 20% on the Q4 FY25 call, actual 20.3%, 0.3 pt above the top; Nike then reset the guide to the "low 20% range" on the Q1 FY26 call, which the 20.3% met. For FY27 the tax guide was raised from "low 20% range" (Q4 FY26 call p. 12) to "mid-20 percent range" (Q1 FY27 release, Outlook); Q1 FY27 was 22.7%. Full-year FY27 is pending and not scored. Duplicate and pending rows are in the CSV and not counted below.

## 7. Q1 FY27 in detail (the quarter the three documents disagree about)

- **Guide (Q4 FY26 call, Jun 30 2026, p. 12):** "we expect reported revenues to be down low to mid-single digits with no expected benefit from foreign exchange and currency-neutral revenue growth consistent with recent performance." The same call (p. 17) repeats it: "revenue to be down low- to mid-single digits."
- **Band and midpoint in dollars (derived):** prior-year Q1 FY26 revenue $11,720M (Q1 FY27 release table). Down 1% = $11,603M, down 6% = $11,017M, midpoint (-3.5%) = $11,310M.
- **Actual:** $11,213M, down 4.33% reported, down 5% currency-neutral (Q1 FY27 release). That is $97M below the midpoint, $196M above the bottom of the band and $390M below the top. Inside the range.
- **Management's own description:** "NIKE, Inc. revenue was within the range we guided to. Gross margin improved as we said it would" (Q1 FY27 call p. 2). The release says results were "consistent with our expectations" (Q1 FY27 release, CFO quote).
- **Other Q1 FY27 items:** gross margin +60 bps against "slightly positive" (0 to +50): beat. SG&A -2.64% against "flat": favorable. Q1 FY27 diluted EPS $0.48 (release).
- **LSEG consensus (secondary, not re-verified here):** revenue $11.32B, EPS $0.43, per `research_notes/Long or short cruxes/expectations_gap.md` lines 97 to 98 (relay via StockTitan; the CNBC page returned 403 there). If right, revenue was $0.11B (0.9%) below consensus, and consensus was about equal to the guide midpoint ($11.31B, derived above). Consensus is what analysts expected, not what Nike guided; keep the two apart in the deck.
- **Sensitivity of the verdict to the band.** If "low to mid" were read as 2 to 5 (not 1 to 6), the midpoint is still -3.5 and the result is still inside the band. The below-midpoint verdict does not depend on the band convention.

## 8. Counts

Items are the 8 quarters Q2 FY25 to Q1 FY27 (guides given on the Q1 FY25 to Q4 FY26 calls). Q4 FY26 gross margin uses the ex-IEEPA figure.

| Set | Items | Beat vs range | In range | Miss vs range | Met or better vs range | Beat vs midpoint | Met (within tolerance) | Miss vs midpoint | At or above midpoint, strict |
|---|---|---|---|---|---|---|---|---|---|
| Revenue | 8 | 7 | 1 | 0 | 8 of 8 | 7 | 0 | 1 | 7 of 8 |
| Gross margin | 8 | 5 | 3 | 0 | 8 of 8 | 6 | 2 | 0 | 7 of 8 |
| Revenue + gross margin | 16 | 12 | 4 | 0 | 16 of 16 | 13 | 2 | 1 | 14 of 16 |
| SG&A | 8 | 5 | 3 | 0 | 8 of 8 | 7 | 1 | 0 | 7 of 8 |
| Revenue + GM + SG&A | 24 | 17 | 7 | 0 | 24 of 24 | 20 | 3 | 1 | 21 of 24 |
| Legacy "14 of 14" (Q3 FY25 to Q1 FY27, revenue + GM) | 14 | 10 | 4 | 0 | 14 of 14 | 11 | 2 | 1 | 12 of 14 |
| Legacy "22 of 22" (the 14 + 7 SG&A + Q2 FY26 tax) | 22 | 14 | 8 | 0 | 22 of 22 | 18 | 3 | 1 | 19 of 22 |

Adding the quarterly tax guides (Q2 FY25 and Q2 FY26: both in range) and the two original full-year tax guides (FY25 and FY26: both miss) gives 28 numeric items, 26 inside or above the range and 2 outside it.

Average distance of reported revenue above the midpoint: +2.29 pts over the 8 quarters, +2.44 over the 7 Hill-era quarters (this note's bands). The repo's earlier "+2.3 pts" figure used a -15 to -13 band for Q4 FY25; with this note's -16 to -14 band Q4 FY25 is +3.03 instead of +2.03. Excluding Q1 FY27 the 7-quarter average is +2.74. Average gross margin distance above the midpoint: +38 bps over 8 quarters, +36 bps over the 7 Hill-era quarters (matches the earlier +36).

**What the record does and does not show.**
1. Alternative: the beats are luck or currency. Ruled out for currency in the four quarters with a stated FX effect (section 3). Luck is not testable.
2. Alternative: Nike guides conservatively. Consistent with 7 of 8 revenue results above the midpoint, by an average +2.4 pts. Management's own language supports it as opinion only: "set at a level that we believe is reasonable and attainable" (Q1 FY27 call p. 10, CFO Denton), said about guidance going forward.
3. Alternative: the underlying trend improved faster than management expected. Cannot be separated from conservative guiding with public data. Needed: Nike's internal plan versus guide, or a series of sell-side estimates around each guide. Not available in the repo.
4. What is unknown about Q2 FY27: Nike gave no Q2 revenue or gross margin number, only a "multi-point headwind" of "approximately 400 basis points" from EMEA Cyber Week and North America sell-in timing (Q1 FY27 call p. 11) and said it was "probably not going to provide guidance specifically for gross margin" (p. 18). The first full-year guide (FY27 revenue down high single digits) was set by the new CFO, Dave Denton, who describes his approach as "reasonable and attainable" (p. 10). Whether that makes Q2 FY27 easier to meet than the Friend-era guides cannot be tested until the Q2 FY27 report (about Dec 17 2026).

## 9. Full-year and multi-quarter items (not part of any "N of N" count)

| Item | Guide (call, page) | Result | Score |
|---|---|---|---|
| FY25 tax rate | "mid-teens range" (Q3 FY25 call p. 16) | 17.1% (Q4 FY25 release) | miss |
| FY26 tax rate, original | "19% to 20%" (Q4 FY25 call p. 13) | 20.3% (Q4 FY26 release) | miss by 0.3 pt |
| FY26 tax rate, revised | "low 20% range" (Q1 FY26 call p. 11 to 12; Q3 FY26 call p. 13) | 20.3% | in range |
| FY26 SG&A | "we continue to expect SG&A to grow low single digits in fiscal '26" (Q1 FY26 call p. 12) | +0.16% ($16,114M vs $16,088M, Q4 FY26 release) | below range (favorable cost) |
| FY26 wholesale | "we expect wholesale revenue to return to modest growth for fiscal '26" (Q1 FY26 call p. 12) | +6% reported, +4% currency-neutral (Q4 FY26 release) | beat |
| FY26 NIKE Direct | "we do not expect NIKE Direct to return to growth for fiscal '26" (Q1 FY26 call p. 12) | -6% reported, -8% currency-neutral | met |
| Nine-month outlook, Q4 FY26 to Q2 FY27 | revenue "down low single digits", earnings "flattish", gross margin expansion to "begin in the second quarter" (Q3 FY26 call p. 12) | Revised on the Q4 FY26 call (p. 11 to 12): revenue "down low to mid-single digits", gross margin expansion "earlier beginning in Q1"; earnings flattish only "excluding the benefit from tariff recovery" | revenue guide cut, gross margin guide raised |
| FY27 | revenue "decline in the high single-digit range"; adjusted EPS $1.15 to $1.35 excluding about $0.15 of Pace; tax "mid-20 percent range"; SG&A "down year-over-year" (Q1 FY27 call p. 11 to 12; release Outlook) | pending | not scored |

Nike never guided FY25 after Oct 1 2024 (withdrawn, Q1 FY25 call p. 3), so there is no FY25 revenue or gross margin guide to score under Hill.

## 10. Sources and routes log

Transcripts: none was missing, so the five-route fallback was not needed. Routes used and results:

| Route | Result |
|---|---|
| 1. Repo copies, `data/hunt/earnings_calls/transcripts/Q{1FY25..1FY27}.txt` | worked, all 9 present (Q1 FY25 to Q1 FY27) |
| 2. Fresh PDFs from investors.nike.com asset store (URLs in transcripts `README.md`), `pdftotext`, word-level comparison with repo copies | worked: word match 0.9979 to 0.9987 for all 9, the residue being page headers and footers; the quoted guide sentence was found on the cited PDF page in all 9 |
| 3. Nike earnings releases, Form 8-K Ex. 99.1, via `https://investors.nike.com/sec-filings/all-sec-filings/content/<accession>/<file>` (never www.sec.gov); index from data.sec.gov submissions JSON, no contact header sent | worked, all 9 releases below |
| 4. Wayback, Motley Fool, Seeking Alpha public pages | not attempted, not needed (routes 1 to 3 complete) |
| 5. LSEG consensus for Q1 FY27 | not independently verified in this task; taken from the repo's `expectations_gap.md` (secondary relay), labelled as such |

Release accessions (Form 8-K Item 2.02, all `qNfyYYexhibit991er.htm`): Q2 FY25 0000320187-24-000069 (Dec 19 2024); Q3 FY25 0000320187-25-000011 (Mar 20 2025); Q4 FY25 0000320187-25-000034 (Jun 26 2025); Q1 FY26 0000320187-25-000091 (Sep 30 2025); Q2 FY26 0000320187-25-000138 (Dec 18 2025); Q3 FY26 0000320187-26-000026 (Mar 31 2026); Q4 FY26 0000320187-26-000076 (Jun 30 2026); Q1 FY27 0000320187-26-000184 (Oct 1 2026). The Q1 FY25 release (0000320187-24-000062, Oct 1 2024) was also fetched for the call date.

## 11. Edits the other documents need (not made here)

- `slides/pptx/build_deck.js` lines 94, 105, 239, 248, 251, 286 and `research_notes/Long or short cruxes/earnings_calls_analysis.md` line 11: replace "met or beaten 14 of 14" with the sentence in section 1. Keep "revenue averaged about 2.3 to 2.4 points above the midpoint" only if the Q1 FY27 -0.8 is stated as inside it.
- `research_notes/19_management_track_record.md` lines 46 and 295: say "22 of 22 inside or above the range (21 of 22 at or above the midpoint within a half point), with two full-year tax-rate guides missed", and state the 7-quarter sample.
- `research_notes/Deep dives Oct 14/D4_long_case.md` lines 23 and 281: change "missed" to "fell below the guide midpoint, inside the range, and missed LSEG consensus (secondary)".
- `research_notes/Deep dives Oct 14/00_SYNTHESIS.md` line 21 flagged this check; it can be closed.
