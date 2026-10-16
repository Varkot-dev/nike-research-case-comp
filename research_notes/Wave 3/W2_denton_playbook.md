# W2: CFO Denton's investor-day playbook (Lowe's, CVS, Pfizer) and what it implies for Nike's Nov 16 to 17, 2026 Investor Day

Prepared Oct 16, 2026. Task W2 in `RESEARCH_MAP.md` (Wave 3). Files: this note, `W2_denton_events.csv` (16 events, targets, consensus, outcome, returns), `W2_scripts/w2_returns.py` (price code). Builds on D7 (`research_notes/Deep dives Oct 14/D7_investor_day.md`) and N9 (`research_notes/Niche sources/N9_options_investor_day.md`); no overlap redone.

Tags: **OPENED** = I read the primary page or file in this session (SEC exhibit, Lowe's PDF, Nike page, XBRL, price API). **SNIPPET** = rests on a search summary or a secondary page I could only see in part. **DERIVED** = my arithmetic on tagged inputs. Executive quotes are labelled opinion. Returns are close-to-close from the prior close, cumulative to day 0, 1, 5, 20 (trading days), abnormal = raw minus S&P 500 (`^GSPC`), Yahoo chart API `adjclose`, no email in any request, same convention as D7.

## 0. Answer in eight lines

1. **Denton always puts numbers on the table; dates and "above consensus" are the weak points.** Across 16 events (Lowe's 3, CVS 9 including the Aetna deal, Pfizer 4) every event with a target had numeric ranges (OPENED). Multi-year targets were dated at CVS 2010 to 2015 (2015) and CVS Dec 2016 savings (2021), but the headline growth and margin targets at Lowe's (Dec 2018 "medium-term", Dec 2020 "long-term") and CVS Dec 2016 ("longer-term") were not dated in the documents I could open.
2. **He has never set a guide above consensus in any event where I could find the consensus.** Of 7 events with a sourced consensus, 4 were in line (CVS Dec 2011, CVS Dec 2015, Pfizer Dec 2024, Lowe's Dec 2018 sales) and 3 were below (CVS Nov 2016 by 10.4%, Pfizer Dec 2023 by 30.6%, Pfizer Dec 2025 by 4.9%); 0 above (SNIPPET consensus, DERIVED gaps). With 0 of 7, a 95% upper bound on the chance of an above-consensus set is about 41% (exact binomial, DERIVED), so the sample cannot rule out the bullish case, but it gives it no support.
3. **Delivery landed inside or above the guided range in 10 of 12 testable guides** (CVS 2012 to 2017, Lowe's FY2020, Pfizer 2023 reset, 2024, 2025; at or above the top in 8). The two below-range outcomes: Lowe's FY2019 (first guide, 3 weeks after he joined: EPS $5.49 vs $6.00 to $6.10) and Lowe's FY2022 GAAP EPS ($10.17 vs $12.25 to $13.00, after Canada-sale charges, delivered after he left). The "beatable guide" pattern holds for annual guides (DERIVED from OPENED filings, section 2).
4. **The Lowe's "conservative target" story is mostly a demand windfall, not sizing.** The Dec 2018 medium-term 12% margin was reached in FY2021 (12.56%), but sales were up 35.0% and sales per square foot up 37.8% against a planned ~10% (DERIVED). The data cannot separate conservative sizing from the windfall.
5. **Reactions followed the guide-versus-consensus gap and a bundled capital-return upgrade.** 8 in-line events (7 of them with a buyback or dividend increase): mean abnormal +4.1% day 0, +4.9% day 1, +5.5% day 5, +6.5% day 20, all 8 positive on days 0, 1 and 5. 4 resets below consensus: mean -6.4% day 0, -5.8% day 1, -7.0% day 5, -6.5% day 20 (DERIVED, section 4).
6. **Nike's situation differs on the two things that carried the rallies:** the reset has already happened (Oct 1: FY27 adj EPS $1.15 to $1.35 vs about $1.65 expected; NKE -4.4% vs S&P on Oct 2), and a large capital-return step-up looks unlikely (payout above 100% of FY27 EPS midpoint, Denton: dividend a "significant priority" and "under all scenarios" maintained and "ultimately" grown, opinion; repurchases paused since Q1 FY26; about $5.9B left on the $18B program, DERIVED from the 10-Q).
7. **Probability shift vs D7 (my inference, section 6):** UP (dated, credible, above consensus) 25% to **17%**; NEUTRAL 46% to **52%**; DOWN (lowered, delayed, vague, near-term cut) 29% to **31%**. The bullish D7 base case (a dated, above-consensus margin target) falls from the modal outcome to a minority; the modal outcome becomes a numeric, dated-by-construction five-year algorithm sized to be met.
8. **Versus options (N9):** Denton's own 16 events averaged an absolute day-0 abnormal move of 4.1% (median 3.4%), almost exactly the market's 4.2% to 4.9% 1-sd and 3.4% to 3.9% expected absolute move. But the class mix implies tails the options do not price: P(down 10% or more) 12% to 24% vs 5.5% to 6.2% priced; P(up more than 6%) 12% vs 17% to 18% priced. **Smoking gun: NO.**

## 1. Events reconstructed (full detail in the CSV)

Denton became CFO of CVS in 2010 (Lowe's release Aug 22, 2018, per `DEEP_DIVE_DENTON_EWING.md`), CFO of Lowe's from Nov 19, 2018 to Apr 30, 2022, CFO of Pfizer from May 2, 2022 to Aug 15, 2026. Day 0 is the first session that could reflect the news; every release below was issued before the open.

| ID | Date | Event | Targets (OPENED unless tagged) | vs consensus | Outcome |
|---|---|---|---|---|---|
| L1 | 2018-12-12 | Lowe's Analyst and Investor Conference | FY2019: sales +~2%, comps +~3%, EPS $6.00 to $6.10, $10B buyback. Medium-term "path to 12% operating margin" appears only in a Wedbush note (SNIPPET, opinion) | Sales in line (FY2018 sales ~4% vs 4.11% expected, Reuters, SNIPPET) | FY2019 EPS $5.49 vs guide: **missed 8.5% to 10.0%**; 12% margin **met** FY2021 (12.56%) |
| L2 | 2020-12-09 | Lowe's Investor Update (Total Home) | FY2020 adj EPS $8.62 to $8.72, $15B buyback; long-term sales per sq ft $460, adj op margin 13%, ROIC 32% (Lowe's Dec 2022 deck) | not found | FY2020 adj EPS $8.86 (+1.6% above top); targets met in FY2021 to FY2022 |
| L3 | 2021-12-15 | Lowe's FY2022 outlook | Sales $94B to $97B, op margin 12.5% to 12.8%, EPS $12.25 to $13.00, ROIC ~35% | not found | Sales $97.06B (above top); Denton left Apr 30, 2022 |
| C0 | 2010-11-03 | CVS Caremark steady-state 2010 to 2015 (timing is my inference, earnings day) | CAGR: revenue 5% to 8%, op profit 8% to 10%, adj EPS 7% to 9%; payout 25% to 30% by 2015 (OPENED: Denton at William Blair, Jun 12, 2013) | not found | Op profit CAGR 9.1% (in range), revenue 9.9% and GAAP EPS 13.2% (above) |
| C1 | 2011-12-20 | CVS Analyst Day | 2012 adj EPS $3.15 to $3.25; dividend +30%; >$30B cash 2011 to 2015 | In line ($3.21 consensus, SNIPPET) | 2012 adj EPS $3.39 (+4.3% above top) |
| C2 | 2012-12-13 | CVS Analyst Day release | 2013 adj EPS $3.84 to $3.98; dividend +38% | not found | 2013 about $3.95 to $3.99, top of range |
| C3 | 2013-12-18 | CVS Analyst Day, 5-year steady-state targets | 2014 adj EPS $4.36 to $4.50; $6B buyback; 5-year numbers not retrievable | not found | 2014 $4.49 (derived), top of range |
| C4 | 2014-12-16 | CVS Analyst Day | 2015 adj EPS $5.05 to $5.19; $6B buyback | not found | 2015 $5.16 |
| C5 | 2015-12-16 | CVS Analyst Day | 2016 adj EPS $5.73 to $5.88; dividend +21% | In line ($5.80 consensus, SNIPPET) | 2016 $5.84 |
| C6a | 2016-11-08 | CVS Q3 release, 2017 guide | 2017 adj EPS $5.77 to $5.93 | **Below**: $6.53 expected (Benzinga, SNIPPET) | 2017 $5.90, inside the range |
| C6 | 2016-12-15 | CVS Analyst Day (reaffirm) | "on average, 10% growth in Adjusted EPS longer-term", $7B to $8B annual cash, $700M to $750M savings by 2021, $15B buyback | reaffirmation | 2017 EPS growth +1.0% ($5.84 to $5.90) |
| P1 | 2023-10-13 | Pfizer cost realignment and 2023 guide cut | Savings at least $3.5B; 2023 EPS $1.45 to $1.65 from $3.25 to $3.45 | guide cut ~53% | 2023 actual $1.84, above the cut guide |
| P2 | 2023-12-13 | Pfizer 2024 guide | Revenue $58.5B to $61.5B, EPS $2.05 to $2.25; savings raised to at least $4.0B | **Below** $3.10 (-30.6%, Zacks, SNIPPET) | 2024 actual $3.11 (+38% above top) |
| P3 | 2024-12-17 | Pfizer 2025 guide | EPS $2.80 to $3.00 | In line ($2.89 to $2.90, SNIPPET) | 2025 actual $3.22 (+7.3% above top) |
| P4 | 2025-12-16 | Pfizer 2026 guide | EPS $2.80 to $3.00 | **Below** $3.05 (-4.9%, SNIPPET) | Open; Aug 4, 2026 update kept EPS range |
| C7 | 2017-12-04 | Aetna deal | not a target event | n/a | -4.5% day 0 vs S&P |

Excluded: Lowe's Aug 22, 2018 (CFO hire day, also Q2 earnings day, +5.8% raw), because the news is confounded. No Lowe's investor event in Dec 2019: the Lowe's 8-K list from the EDGAR index shows no Item 7.01 filing between Dec 12, 2018 and Dec 9, 2020 (OPENED, data.sec.gov submissions).

### Price reaction vs S&P 500 (DERIVED, percent)

| ID | Day 0 | Day 1 | Day 5 | Day 20 |
|---|---|---|---|---|
| L1 Lowe's 2018-12-12 | +2.40 | +4.85 | +5.87 | +10.28 |
| L2 Lowe's 2020-12-09 | +6.67 | +6.86 | +7.94 | +5.82 |
| L3 Lowe's 2021-12-15 | +0.38 | -0.44 | -2.44 | -1.24 |
| C0 CVS 2010-11-03 | +0.75 | +0.91 | -0.14 | +2.41 |
| C1 CVS 2011-12-20 | +5.88 | +7.48 | +8.58 | +8.30 |
| C2 CVS 2012-12-13 | +2.65 | +4.62 | +2.28 | +6.20 |
| C3 CVS 2013-12-18 | +2.65 | +3.38 | +3.26 | -1.50 |
| C4 CVS 2014-12-16 | +3.56 | +3.62 | +4.25 | +7.97 |
| C5 CVS 2015-12-16 | +3.92 | +2.36 | +5.37 | +9.40 |
| C6a CVS 2016-11-08 | -12.20 | -9.68 | -12.31 | -8.58 |
| C6 CVS 2016-12-15 | -1.24 | +0.55 | -0.56 | +5.63 |
| C7 CVS 2017-12-04 | -4.46 | -4.99 | -3.39 | -5.24 |
| P1 Pfizer 2023-10-13 | -1.96 | +0.51 | -4.01 | -10.75 |
| P2 Pfizer 2023-12-13 | -8.08 | -10.21 | -4.50 | -2.60 |
| P3 Pfizer 2024-12-17 | +5.06 | +5.86 | +6.46 | +5.43 |
| P4 Pfizer 2025-12-16 | -3.17 | -3.86 | -7.23 | -3.92 |
| Memo: NKE Oct 2, 2026 (Q1 FY27 reset) | -4.38 | -4.79 | -3.14 | n/a |

Raw returns, S&P returns and the code are in the CSV and script. Pfizer Dec 16, 2025: a data site said the stock traded up 2.3% intraday (SNIPPET); the close-to-close figure is -3.4% raw.

## 2. Targets versus later actuals (financial decomposition, not narrative)

**CVS 2010 to 2015 steady-state targets (set by Denton's team, restated by him in 2013).** Operating profit CAGR 9.1% ($6,137M to $9,475M) sits inside the 8% to 10% target: the operating target was met, not beaten. The EPS beat has an arithmetic source: GAAP EPS CAGR 13.2% ($2.49 to $4.63) against a 7% to 9% target, with diluted shares falling 3.9% a year (1,377M to 1,126M) and income from continuing operations growing 8.7% (XBRL, DERIVED). So roughly 4 points a year of the EPS result came from buybacks, which was part of the plan (">$30B cash 2011 to 2015"). Revenue CAGR 9.9% vs 5% to 8% reflects acquisitions and mix, not tested further. Adjusted-EPS CAGR was not computed because I did not pull the 2010 adjusted figure.

**Lowe's Dec 2018 "12% medium-term" and Dec 2020 targets.** Adjusted operating margin went from 8.56% (FY2018) to 12.56% (FY2021, GAAP equals adjusted in the Lowe's deck): +400 bps. Sales rose 35.0% ($71,309M to $96,250M) and sales per square foot 37.8% ($336 to $463), against about 10% per-square-foot growth in the Wedbush description of the plan (SNIPPET). At the 2018 margin of 8.56%, FY2021 operating income would have been $8,239M; actual was $12,093M, so of the $5,988M gain over adjusted FY2018 ($6,105M) about $2,134M is volume at constant margin and $3,854M is rate (DERIVED). The margin rate alone cleared the 12% target by 56 bps, but on 3.5 times the planned growth (35.0% vs about 10%), and diluted shares fell 13.9% (812M to 699M). Lowe's own Dec 2022 deck says the 2020 targets (13% margin, 32% ROIC, $460 per square foot) were already passed or at hand (ROIC 35.3% in FY2021; margin 13.0% in FY2022E). The ruled-out explanation "targets were sized conservatively" cannot be confirmed or rejected: demand explains the beat and no filing separates it from sizing.

**Lowe's FY2019, the one clear miss.** The Dec 2018 EPS guide of $6.00 to $6.10 (reiterated Feb 27, 2019) implied GAAP operating margin of 9.39% to 9.49% (5.64% plus 375 to 385 bps). Actual: 8.75%, a gap of 64 to 74 bps, about $0.50 of EPS at $72.1B sales, a 24% tax rate and 778M shares (DERIVED). Adjusted margin was 9.13%, so about 37 bps of the gap was $265M of FY2019 Canada and Mexico charges and the rest, 27 to 37 bps, was operating shortfall (DERIVED; I could not verify whether those charges were in the guide).

**Pfizer.** Initial-guide to actual adjusted EPS: 2023 cut guide $1.45 to $1.65, actual $1.84; 2024 $2.05 to $2.25, actual $3.11; 2025 $2.80 to $3.00, actual $3.22 (Pfizer Feb 2025 and Feb 2026 releases, OPENED). Cost savings ratcheted: at least $3.5B (Oct 13, 2023) to at least $4.0B (Dec 13, 2023) (OPENED); the larger later totals are in `DEEP_DIVE_DENTON_EWING.md`. Reported 2024 EPS was $1.41 against $3.11 adjusted, so "beat" is on the adjusted measure only.

**What the Pfizer and CVS data show about reset timing.** Pfizer reset 17 months after he joined and re-reset 2 months later; CVS reset in year 7 of his tenure (Nov 2016); Lowe's had no reset (the first guide was 3 weeks in, in line, and then missed). Nike's reset came 6 weeks in (Oct 1).

## 3. Denton's stated guidance rule (opinion, OPENED)

Q1 FY27 call, Oct 1, 2026 (transcript opened): "I believe guidance should be grounded in the realities of the business, informed by both the risk and the opportunities ahead of us and set at a level that we believe is reasonable and attainable." He added that Nike will give a full-year view "and update that perspective as the year progresses," and: "in November, we're going to give you a financial algorithm, so you can begin to assess what not just '27 looks like, but what does the next 5 years begin to look like, both from a top line and a bottom line perspective." Hill: "At our Investor Day in November, we will provide a clearer view of our long-term growth algorithm." Denton also already gave dated numeric Pace targets: about $2.5B savings, about $1.0B cost to implement, "the majority of the program savings to be realized in fiscal years '29 and '30, with the full realization ... into fiscal year '31" (OPENED). These are quotes (opinion) and a stated method; the evidence they will be conservative is the delivery record in section 2, not the quote.

## 4. How reactions sorted (DERIVED, abnormal vs S&P, percent)

| Group | n | Day 0 | Day 1 | Day 5 | Day 20 |
|---|---|---|---|---|---|
| Analyst or investor days with a framework (L1, L2, C1 to C6) | 8 | +3.3 | +4.2 | +4.6 | +6.5 |
| In-line guide plus buyback or dividend raise (L1, L2, C1 to C5, P3) | 8 | +4.1 | +4.9 | +5.5 | +6.5 |
| Resets below consensus (C6a, P1, P2, P4) | 4 | -6.4 | -5.8 | -7.0 | -6.5 |
| All 16 events | 16 | +0.2 | +0.7 | +0.6 | +1.7 |

Caveats. n is small; the reset group is defined by the consensus gap, so the sign is partly by construction (same circularity D7 flagged). 7 of the 8 in-line events bundled a buyback or a dividend raise (Pfizer Dec 2024 did not and still rose 5.1% on day 0, which weakens the capital-return reading and leaves the in-line guide itself as a sufficient cause) ($10B Lowe's 2018, about 13.8% of a roughly $72.7B market cap; $15B Lowe's 2020, about 13.2% of roughly $113B; CVS dividend +30%, +38%, +22%, +21%; market caps at prior close times FY diluted shares, DERIVED), so the data cannot cleanly split the effect of the framework from the effect of capital return. Lowe's Dec 2018 also coincided with the market low (S&P -4.9% over days 0 to 5 vs Lowe's +0.95% raw). Mean absolute day-0 abnormal move across the 16 events: 4.1% (median 3.4%); absolute day 1: 4.4%.

## 5. Nike's pre-event record (Nike pages, transcripts, press)

- **Elliott Hill's own public statements on long-term targets:** none numeric. Oct 1, 2026 letter to employees (about.nike.com, OPENED): "At our Investor Day on Nov. 16-17, we'll share more details about Nike's next phase of growth, the financial plan behind it, and how Pace supports our long-term competitive position," with no figures. Q4 FY26 call, Jun 30, 2026 (investors.nike.com transcript, OPENED): Hill "we look forward to sharing the next phase of our growth strategy at our Investor Day on November 16 and 17" and "expand our margins over time"; the "double-digit margins" language is the then-CFO Friend's: margin actions "contribute to this trajectory to get back to double-digit margins" (opinion, undated). D4 already records that management has never dated a double-digit EBIT margin return, and the repo earnings-call table logs the Friend quote as undated.
- **Agenda and speakers:** nothing published as of Oct 16, 2026. The investors.nike.com IR calendar lists "There are no upcoming events scheduled at this time"; past events are Oct 1, Sep 8 and Jun 30 only (OPENED). The only official content description is Hill's Oct 1 letter above, plus an all-hands (NTM) on Nov 18. Speakers are not named anywhere I could open; Hill and Denton are the obvious presenters (my inference).
- **Sell-side previews free to read:** Morgan Stanley (Underweight, $27) says FY29 is the year management will point to when Pace can move the dial (CNBC Oct 2, via search snippet, SNIPPET, opinion); Bernstein (Outperform, $45) expects about 6% margin for FY27 (SNIPPET); Piper Sandler's bull case assumes $600M to $1B a year of cost savings worth 130 to 200 bps of margin (24/7 Wall St, OPENED, opinion); Jefferies (Sept 28) called Investor Day the bigger catalyst because Denton "owns none of the prior guidance" (repo note, opinion); an older UBS note had about 10% EBIT margin long term (SNIPPET, 292 days old). No broker preview with an FY30 or FY31 margin number was found.

## 6. What it implies for D7's outcome classes (my inference from the above)

D7 classes: **UP** = dated numeric targets above the prior plan or consensus, no near-term cut (D7 base 25%); **NEUTRAL** = dated numeric targets without evidence either way (46%); **DOWN** = near-term cut, lowered or delayed target, or no new numbers (29%).

| Evidence from Denton's record | Direction for Nike |
|---|---|
| Numbers in every event; no vague framework | Lowers the "vague" part of DOWN. Five-year horizon is explicit ("next 5 years"), so dated by construction |
| 0 of 7 above-consensus guides; "reasonable and attainable" stated rule | Lowers UP (a stretch, above-consensus margin target) |
| 10 of 12 guides delivered inside or above the range | A target sized to be met is NEUTRAL by D7's test, even if a headline looks high |
| 3 of 7 resets below consensus, one within 2 months of a prior reset (Pfizer) | Keeps DOWN alive despite the Oct 1 reset |
| 7 of 8 in-line rallies came with a capital-return step-up (Pfizer Dec 2024, +5.1% day 0, had none); Nike has paused buybacks, payout above 100%, about $5.9B left on the program | Removes the support that accompanied Denton's rallies, so NEUTRAL outcomes may not rally as they did (+4.1% day 0 in sample) |
| FY27 EPS guide already about 24% below consensus ($1.25 vs $1.65); stock only -4.4% vs S&P | Part of the reset is priced; a below-consensus FY28 is the live DOWN path (consensus FY28 EPS $1.65, margin 7.2%, repo) |

**Probabilities (judgement, no model fits them):**

| Class | D7 base | D4 (N9) | **W2** | Rough mapping to a margin outcome |
|---|---|---|---|---|
| UP | 25% | 8% | **17%** | Dated target at or above 12% with a bridge and unchanged FY27 guide |
| NEUTRAL | 46% | 42% | **52%** | Dated numeric target around double-digit (about 9% to 12%) by FY30 or FY31, FY28 near consensus |
| DOWN | 29% | 50% | **31%** | FY28 or FY29 below consensus, target under about 10%, or timeline beyond FY29 (Morgan Stanley's FY29 framing is a signal here), or FY27 re-cut |

The shift moves 8 points out of UP, 6 into NEUTRAL, 2 into DOWN versus D7. Expected short payoff per D7's formula (UP -7.9%, NEUTRAL +0.2%, DOWN +15.0% on day 3): D7 base +2.4%; W2 mix +3.4%. If NEUTRAL carries Denton's in-line mean instead of 0 (+3.3% day 0 against the short), W2 EV is +1.6% (DERIVED). The short's edge sits in the DOWN branch, not in the NEUTRAL one.

### Versus the option market (N9: 1-sd event move 4.2% to 4.9%, expected absolute 3.4% to 3.9%)

- **Centre of the distribution:** Denton's own mean absolute day-0 move (4.1%) and day-1 (4.4%) match the option-implied 1-sd. The market is not mispricing the typical size of a Denton event.
- **Tails.** Using N9's class conditionals (P(up more than 6% | UP) 0.72, P(down 10% or more | DOWN) 0.76, P(down 15% or more | DOWN) 0.48, derived from the D7 mixture in N9):

| Tail | Market (N9) | D7 base mix | D4 mix | **W2 mix** |
|---|---|---|---|---|
| Up more than 6% | 17% to 18% | 18% | 7% | **12%** |
| Down 10% or more | 5.5% to 6.2% | 22% | 38% | **24%** (12% using Denton's own reset severity, below) |
| Down 15% or more | 0.8% to 1.1% | 14% | 25% | **15%** |

Denton's own four resets had day-1 abnormal moves of +0.5%, -3.9%, -9.7% and -10.2%, shallower than D7's DOWN mean of -14.0%; weighting that severity (about 1 in 4 reaching -10% or worse) gives P(down 10% or more) near 8% to 12% rather than 24%. So the W2 conclusion is robust in sign and sensitive in size: the options price the downside tail at one half to one quarter of what Denton's record plus D7 imply, and price the upside tail above what Denton's record supports. This does not make the short cheap: N9 shows the ATM put costs about 4% of spot through finals and structures only have positive expected value above 10% to 17% DOWN probability (N9 section 0), and W2's 31% is inside that range but is a judgement, not a measurement.

## 7. Alternatives ruled out and what survives (CLAUDE.md "rabbit hole")

| Question | Alternatives | Verdict |
|---|---|---|
| Why did the Lowe's 2018 and 2020 targets "beat"? | (a) conservative sizing; (b) demand windfall; (c) buybacks; (d) cost levers | (b) and (c) are measured: sales +35.0%, sales per sq ft +37.8% vs about 10% planned, shares -13.9%; (a) and (d) cannot be separated from (b) with filings. Survives: windfall plus unknown sizing. Data that decides: the Dec 2018 and Dec 2020 slide decks (bridge assumptions), not obtained |
| Why did CVS 2010 to 2015 EPS beat? | (a) conservative EPS target; (b) operating beat; (c) buybacks | (b) ruled out: op profit CAGR 9.1% inside 8% to 10%; (c) explains about 3.9 points a year of the roughly 13% EPS CAGR. (a) is the remainder |
| Is the Denton rally pattern caused by the framework? | (a) framework; (b) in-line guide; (c) bundled capital return; (d) market | Not fully separable: 7 of 8 rallies bundle (c) and the eighth (Pfizer 2024) rose on an in-line guide alone; Lowe's Dec 2018 also coincides with the Dec 24, 2018 market low (d). Survives: (b) and (c) |
| Does Denton reset at the first opportunity? | Evidence for: Pfizer Dec 2023, CVS Nov 2016, Nike Oct 1. Against: Lowe's Dec 2018 (in line, 3 weeks in), CVS 2011 to 2015 (in line) | Mixed: 3 below consensus of 7. Not a first-opportunity rule |
| Would the Pfizer events have been "Denton events"? | The Pfizer releases carry only Bourla quotes and no Denton quote | I treat the CFO as owner of the guide, a convention, not a verified fact |

## 8. Route log (CLAUDE.md "never accept inconclusive")

| Gap | Route | Result |
|---|---|---|
| Lowe's Dec 2018 medium-term 12% in primary document | Lowe's press release (corporate.lowes.com) | OPENED, near-term only |
| | Hometextiles, PR Newswire title in search | partial, near-term only |
| | Seeking Alpha transcript, CNBC article, Benzinga Wedbush note | blocked (403) |
| | Wayback availability API and page fetch | API worked, page fetch blocked (web.archive.org, 403) for cnbc.com copy; no Seeking Alpha copy archived |
| | Lowe's IR events page for archived decks | no 2018 or 2020 decks listed |
| | Wedbush via search summaries | partial: "path to 12%", $10 EPS power, SNIPPET |
| Lowe's Dec 2020 long-term targets | Dec 9, 2020 release PDF and 8-K Ex 99.1 | OPENED, no long-term numbers |
| | Guessing the investis PDF deck URL | 404 |
| | Lowe's Dec 7, 2022 analyst-conference deck (investis PDF) | **worked**: slide "Long-term target from 2020 investor update": $460, 13%, 32% |
| | News search for stock reaction and consensus | partial: Reuters/Globe: shares +4% premarket |
| CVS Dec 2013 five-year numbers | Dec 18, 2013 8-K Ex 99.1 | OPENED, no numbers |
| | Pharmacy Times and PR Newswire titles | no numbers |
| | Drugstorenews, Seeking Alpha Q4 2013 transcript | blocked (403) |
| | Nasdaq 2012 analyst-day transcript | 503 |
| | Yahoo Q3 2013 transcript (December 2013 date only), Dec 2015 and Dec 2016 releases (refer back to the targets) | worked for context, numbers still missing |
| | Result | **Inconclusive after 6 routes.** What would settle it: the Dec 18, 2013 analyst-day slide deck or the CVS Q4 2013 call transcript (Feb 2014); the CVS 2013 10-K MD&A might restate them (untested) |
| Nike Investor Day agenda and speakers | investors.nike.com IR calendar and press releases | OPENED: nothing listed |
| | about.nike.com Oct 1, 2026 release | OPENED: dates and themes only |
| | Q1 FY27 and Q4 FY26 transcripts | OPENED |
| | Kavout preview | paywalled |
| | CNBC Oct 2 piece | blocked (403); content via search snippet |
| | Broker note searches (Jefferies, Bernstein, Wells Fargo, Barclays, Evercore) | partial: Morgan Stanley FY29, Bernstein 6%, Evercore PT cut, no FY30 or FY31 number |
| | Result | **No agenda or speaker list exists publicly yet as of Oct 16**; re-check investors.nike.com in the first week of November (Nike usually posts the webcast about 2 to 4 weeks ahead, my inference) |
| Consensus at each event | Search snippets (Thomson, Bloomberg, Zacks, FactSet, Visible Alpha, Reuters) | partial: 7 of 16 events |
| | Event-level consensus archives | not free; what would settle it: FactSet or Bloomberg consensus history |

Note on downloads: filings were read through a page-fetch tool on sec.gov exhibit URLs and `data.sec.gov` JSON indexes and XBRL (no personal contact in any request); direct www.sec.gov downloads with curl returned 403, as expected, and I did not use them. Lowe's and Nike pages were fetched directly.

## 9. Limits

Sample of one executive with 3 employers; the consensus gap is known for 7 of 16 events and comes from secondary summaries (SNIPPET); market-adjusted returns have no beta adjustment; Pfizer is a pharma, not a consumer name, and the Pfizer rows only test "guide style", not retail targets. The Dec 2018 and Dec 2020 Lowe's targets rest on Lowe's own 2022 deck and an analyst note rather than the original slides. Nothing here is evidence about whether Nike's FY30 or FY31 margin target will be met: Denton's own Lowe's record cannot separate conservative sizing from a windfall.

## 10. Sources

- Lowe's: [Dec 12, 2018 release](https://corporate.lowes.com/newsroom/press-releases/lowes-outlines-areas-strategic-focus-2018-analyst-and-investor-conference-12-12-18); [Dec 9, 2020 release (PDF)](https://lowes-corp-d9.sid2-e1.investis.com/sites/lowes-corp/files/pdf/2020-investor-update-press-release-v2.pdf); [Dec 7, 2022 analyst conference deck (PDF)](https://lowes-corp-d9.sid2-e1.investis.com/sites/lowes-corp/files/2022-12/cfo-financial-update.pdf); [Dec 15, 2021 outlook 8-K Ex 99.1](https://www.sec.gov/Archives/edgar/data/60667/000119312521357421/d260319dex991.htm); [Feb 27, 2019 Ex 99.1](https://www.sec.gov/Archives/edgar/data/60667/000006066719000022/exhibit991_02012019.htm); [May 2021 Ex 99.1](https://www.sec.gov/Archives/edgar/data/60667/000006066721000064/exhibit991-04302021.htm); [Wedbush via Benzinga (SNIPPET)](https://benzinga.com/analyst-ratings/analyst-color/18/12/12847010/wedbush-on-lowes-a-new-day-has-arrived); [Reuters via Business Standard (SNIPPET)](https://www.business-standard.com/amp/article/reuters/lowe-s-to-buy-back-10-billion-shares-reiterates-2018-forecast-118121201300_1.html).
- CVS: 8-K Ex 99.1 for [Dec 20, 2011](https://www.sec.gov/Archives/edgar/data/64803/000110465911070217/a11-31959_1ex99d1.htm), [Dec 13, 2012](https://www.sec.gov/Archives/edgar/data/64803/000110465912083760/a12-29282_1ex99d1.htm), [Dec 18, 2013](https://www.sec.gov/Archives/edgar/data/64803/000006480313000033/pressreleasedateddecember1.htm), [Dec 16, 2014](https://www.sec.gov/Archives/edgar/data/64803/000006480314000040/pressreleasedateddecember1.htm), [Dec 16, 2015](https://www.sec.gov/Archives/edgar/data/64803/000006480315000066/exhibit9912015analystdaypr.htm), [Dec 15, 2016](https://www.sec.gov/Archives/edgar/data/64803/000006480316000104/exhibit9912016analystdaypr.htm), [Feb 9, 2017](https://www.sec.gov/Archives/edgar/data/64803/000006480317000004/exhibit991releasedatedfeb9.htm), [Feb 8, 2018](https://www.sec.gov/Archives/edgar/data/64803/000006480318000012/cvs-20180208ex9914c5024.htm); [William Blair session Jun 12, 2013](https://finance.yahoo.com/news/cvs-caremark-corporation-management-presents-184904746.html).
- Pfizer: 8-K Ex 99 for [Oct 13, 2023](https://www.sec.gov/Archives/edgar/data/78003/000007800323000099/ex99_pressrelease1013.htm), [Dec 13, 2023](https://www.sec.gov/Archives/edgar/data/78003/000007800323000120/exh99pr121323.htm), [Dec 17, 2024](https://www.sec.gov/Archives/edgar/data/78003/000007800324000195/pfe-12172024xexh99.htm), [Dec 16, 2025](https://www.sec.gov/Archives/edgar/data/78003/000007800325000167/pfe-12162025xexh99.htm), [Feb 4, 2025](https://www.sec.gov/Archives/edgar/data/78003/000007800325000017/pfe-12312024xex99.htm), [Feb 3, 2026](https://www.sec.gov/Archives/edgar/data/78003/000007800326000005/pfe-12312025xex99.htm).
- Nike: [Q1 FY27 transcript](https://s1.q4cdn.com/806093406/files/doc_financials/2027/q1/NIKE-Inc-Q1FY27-OFFICIAL-Transcript_-FINAL.pdf); [Q4 FY26 transcript](https://investors.nike.com/financial-information/financial-results/transcript/9540/fy-2026-transcript); [Oct 1, 2026 operating-model letter](https://about.nike.com/en/newsroom/releases/nike-inc-corporate-announcement-october-1-2026); [IR calendar](https://investors.nike.com/news-events/ir-calendar); [24/7 Wall St, Oct 2](https://247wallst.com/investing/2026/10/02/will-nike-ever-stop-falling-one-analyst-is-sure-that-buying-now-will-yield-100-gains/); Q1 FY27 10-Q (repurchase note).
- Data: SEC XBRL companyfacts for Lowe's (CIK 60667) and CVS (CIK 64803); Yahoo chart API (LOW, CVS, PFE, NKE, `^GSPC`).
- Repo: `DEEP_DIVE_DENTON_EWING.md`, `research_notes/Deep dives Oct 14/D7_investor_day.md`, `research_notes/Niche sources/N9_options_investor_day.md`, `research_notes/Deep dives Oct 14/D4_long_case.md`, `research_notes/Long or short cruxes/earnings_calls_analysis.md`.
