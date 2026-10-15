# G7: Is Nike's IP pipeline (trademarks, design and utility patents) drying up ahead of FY28?

Research date: 2026-10-15. Question: trademark applications (new names) and design patents are filed ahead of product launches, so if the product rebuild does not reach shelves in FY28, the 2025 to 2026 filing pipeline should be thin against Nike's own history and against peers. Companion notes: `research_notes/Nike decline root cause analysis/innovation_drought.md` (management admissions and Running recovery) and `research_notes/Deep dives Oct 14/D4_long_case.md` (the long case this tests).

Source tags: **OPENED** = I queried the live source myself in this session and read the returned records. **DERIVED** = my arithmetic on OPENED records (script and CSV named). **SNIPPET** = none used. **SECONDARY** = a mirror of the same USPTO data, used only to cross-check.

All files are in `data/hunt/g7_ip_pipeline/` (scripts, raw pulls, CSVs). Re-run order: `g7_tm_pull.py`, `g7_tm_analyze.py`, `g7_pat_pull.py`, `g7_pat_analyze.py`, `g7_pooled_share.py`, `g7_pat_verify.py`.

---

## 1. Bottom line

**Smoking gun for the short: NO.** The IP pipeline does not show a thin FY28 pipeline. It shows the opposite on the one measure that is visible in real time, and flat on the measure that is delayed.

1. **Trademarks (visible through Sep 30, 2026, OPENED, DERIVED).** Nike filed 47 US trademark applications in Jan to Sep 2026, against 15 in the same months of 2025 and 10 in 2024. Of the 2026 filings, 42 are intent-to-use (Section 1(b)) filings, which are the only filings that precede launch. Intent-to-use filings for new class 25 product names (footwear and apparel) were 21 in Jan to Sep 2026 versus a prior maximum of 7 in the same months of any year 2012 to 2025 (2018 and 2022). The USPTO-wide count of class 25 applications rose 13.7% in the same period, so this is not a general filing surge (Section 4.4).
2. **Patents (visible only for filings up to about 2023 to 2024, OPENED, DERIVED).** Nike's footwear design grants average 559.5 per year in 2024 to 2026 (2026 annualized) against 518.3 in 2017 to 2019 (+7.9%; the 2017 value of 665 is a one-year outlier, and against a 2018 to 2019 base of 445 the gain is +25.7%). Footwear utility grants are +8.9% (250.7 to 272.9 per year). Footwear utility applications published are down 17.8% (295.3 to 242.7 per year) and all utility applications published are down 24.0% (448.7 to 341.1). Design filings by filing year (2023: 553; 2024: 516 so far) are inside the 2015 to 2022 range of 427 to 725. No collapse in designs; a decline in published utility applications.
3. **Peers are catching up in IP, which is the only part that supports the short.** Nike's share of the Nike-plus-peer-set total fell from 91.6% to 81.5% for footwear design grants, 89.1% to 70.9% for footwear utility grants and 85.0% to 64.7% for footwear utility applications (2017 to 2019 versus 2024 to 2026, Section 5.3). The cause is peer growth from small bases (the six footwear peers' footwear design grants went from 47.7 to 127.1 per year), not a Nike decline: Nike still has 4.4 times the six peers combined in footwear design grants (559.5 / 127.1; it was 10.9 times in 2017 to 2019). Share loss measures competitive intensity, not a missing pipeline.
4. **Abandonments do not show a cull of the footwear pipeline.** 16 Nike applications were abandoned in 2024 to Sep 2026 (7, 4, 5). 12 of the 16 carry class 9, 41 or 42 goods (virtual goods and services marks filed 2019 to 2023). 6 touch class 25 and only 3 are class 25 only (ZION, BO KNOWS, FOREVER KING) (Section 6).
5. **The premise needs a correction.** Nike's trademark filings do not lead launches by 12 to 24 months. Among 45 Nike class 25 intent-to-use filings (2012 to 2023) that later declared a first-use date, the median gap from filing to first use is 78 days (interquartile range -220 to +246 days). Many Nike names are filed after launch (VAPORFLY was first used 2017-07-20 and filed 2025-04-29 under Section 1(a); NIKE ZOOMX and ALPHAFLY likewise). So the 2026 intent-to-use surge speaks to product that ships in roughly the next 3 to 12 months (late FY27 to FY28), which is consistent with the long case that a rebuild reaches shelves in FY28. Design patents give a longer lead but cannot be seen for 2025 to 2026 filings (Section 5.4).

**What this means for the pitch (financial framing).** IP counts cannot be converted into revenue, so this note does not move any EPS number. It removes one tempting short argument ("the pipeline is empty") and adds one data-backed concern (peers file more and more). Labelled arithmetic: FY26 revenue is $46,398M and FY26 Nike Brand footwear is $29,525M (`data/nike_filing_facts.csv`, FY2026 10-K). A single $100M franchise (the repo's innovation note records Vomero 18 reaching "$100 million-plus" in about 90 days, status REPO-NOTE) is 0.22% of FY26 revenue (DERIVED: 100 / 46,398), so a revenue recovery needs on the order of 14 such franchises per +3 points of growth (DERIVED: 0.03 x 46,398 / 100). The 21 new class 25 names filed in Jan to Sep 2026 and the 10 filed in calendar 2025 are the candidate count; whether they reach that scale is not decidable from IP data.

---

## 2. What was counted

- **Trademarks:** USPTO Trademark Search backend (the TESS successor, `tmsearch.uspto.gov`), index of 13.3M case files loaded through 2026-10-01 (OPENED). Application counts by filing date, year 2012 to 2026 (2026 = Jan 1 to Sep 30). Owners matched by owner name: Nike (Nike, Inc. and variants, Nike USA, BRS Inc.; 541 case files filed 2005 to 2026), adidas (adidas AG, adidas International Marketing B.V.), On (On Clouds GmbH, On AG), Deckers (Deckers Outdoor Corp, UGG Holdings; Hoka is a Deckers brand and cannot be split except by the 15 HOKA-named marks), New Balance (New Balance Athletics, New Balance Athletic Shoe), ASICS (ASICS Corp, ASICS Tiger, ASICS America), Puma (Puma SE, Puma AG Rudolf Dassler Sport), Lululemon (Lululemon Athletica Canada and Inc.). Jordan Brand marks are filed by Nike, Inc. and are included. Converse Inc. is a separate legal owner and is excluded (not pulled).
- **Nike Innovate C.V.:** zero US trademark records under that owner name (checked by owner name and full owner text) and 13 patent documents listing it (2015 to 2019). All other Nike IP sits under Nike, Inc.
- **Classes:** class 25 (footwear, apparel, headwear) versus classes 9 and 42 (software), with 18, 28, 35 and 41 reported in the CSV. A footwear-goods flag inside class 25 is derived from the goods text (Nike class 25 filings: 2026 Jan to Sep, 31 of 31 contain a footwear term; this flag is loose because the terms list includes socks and insoles).
- **Patents:** USPTO Patent Public Search (`ppubs.uspto.gov`, anonymous JSON API, OPENED): granted utility (kind B1, B2), granted design (S) and published applications (A1), by publication year 2012 to 2026 (through 2026-10-13, 0.784 of the year), assignee or applicant name containing the company name. Footwear split: utility = CPC A43B or A43C; design = USPC main class D2/89x to D2/99x excluding socks, cross-checked by title words (they disagree on 0 to 13 documents per year, column in CSV).
- **Not delivered as asked:** EUIPO eSearch and WIPO Global Brand Database counts, Lens.org counts, PatentsView counts (all blocked, Section 9). The US PPUBS and USPTO trademark index replace them. Single-source caveat applies to the patent side.

---

## 3. Verification (every pull checked against an independent number)

| Check | Result |
|---|---|
| Index completeness: USPTO-wide applications by filing year vs USPTO's own scale | 2019: 497,971 case files; 2020: 665,731; 2024: 597,075; consistent with the known post-2020 surge (OPENED, `g7_uspto_wide_control_jan_sep.csv` and the histogram run) |
| Owner totals vs Trademarkia owner pages (SECONDARY mirror of USPTO data) | Nike Inc. 969 (Trademarkia) vs 989 (mine, all years, phrase "Nike, Inc."); adidas AG 395 vs 398; On Clouds 143 vs 147; Deckers 234 vs 245; New Balance Athletics 211 vs 210; ASICS Corp 810 vs 808. Within about 4% |
| Five 2026 Nike serials (AIR RIFT 99722241, HYPERJOGGER 99722287, SWOOSHFLY 99826570 and others) found on a second site | Serial numbers confirmed on Trademarkia search pages (OPENED) |
| Patent rows pulled vs independent count queries (4 companies x 5 years x 3 kinds, 60 cells) | 54 of 60 cells identical; 6 cells differ by 1 to 10 documents, all on published applications, where my pull has more rows than the A1 count query because it also keeps kinds A2 and A9 (so published-application counts are overstated by up to about 3% in those cells), `g7_pat_verify_counts.csv` |
| Nike design grants 2025 | 654 by count query "S" kind = 654 rows pulled |

---

## 4. Trademarks

### 4.1 Annual US trademark applications, Nike vs seven peers (DERIVED, `g7_tm_annual_counts.csv`)

| Filed | Nike apps | Nike class 25 | Nike intent-to-use | Nike class 9/42 | Nike design-only (no word) | 7 peers apps | 7 peers class 25 | 7 peers class 9/42 |
|---|---|---|---|---|---|---|---|---|
| 2012 | 15 | 5 | 13 | 4 | 4 | 68 | 52 | 2 |
| 2013 | 20 | 10 | 16 | 5 | 2 | 67 | 54 | 6 |
| 2014 | 19 | 10 | 14 | 1 | 0 | 59 | 33 | 3 |
| 2015 | 3 | 2 | 0 | 0 | 0 | 81 | 48 | 9 |
| 2016 | 8 | 6 | 5 | 1 | 0 | 67 | 45 | 14 |
| 2017 | 9 | 4 | 4 | 1 | 1 | 68 | 53 | 11 |
| 2018 | 20 | 18 | 18 | 2 | 1 | 79 | 50 | 10 |
| 2019 | 12 | 6 | 9 | 2 | 2 | 67 | 51 | 18 |
| 2020 | 26 | 14 | 10 | 4 | 6 | 102 | 80 | 15 |
| 2021 | 27 | 17 | 13 | 12 | 13 | 100 | 80 | 14 |
| 2022 | 30 | 23 | 23 | 10 | 7 | 78 | 43 | 28 |
| 2023 | 19 | 12 | 12 | 6 | 4 | 100 | 86 | 5 |
| 2024 | 19 | 19 | 5 | 0 | 2 | 106 | 87 | 2 |
| 2025 | 21 | 20 | 13 | 0 | 2 | 144 | 130 | 3 |
| 2026 (Jan to Sep) | 48 | 31 | 43 | 3 | 9 | 145 | 136 | 1 |

By company, applications filed (full `g7_tm_annual_counts.csv`): 2017 / 2019 / 2024 / 2025 / 2026 Jan to Sep: Nike 9 / 12 / 19 / 21 / 48; adidas 24 / 21 / 13 / 26 / 22; On 5 / 14 / 18 / 5 / 14; Deckers 4 / 4 / 14 / 3 / 0; New Balance 9 / 4 / 7 / 22 / 30; ASICS 8 / 1 / 8 / 30 / 39; Puma 7 / 14 / 15 / 9 / 6; Lululemon 11 / 9 / 31 / 49 / 34.

### 4.2 Same-period comparison (Jan 1 to Sep 30 of each year, so 2026 needs no annualization; `g7_tm_same_period_jan_sep.csv`)

| Year (Jan to Sep) | Nike apps | Nike intent-to-use, class 25 | Nike intent-to-use NEW product names, class 25 | 7 peers: same measure | Nike share of Nike+7 peers (new names) |
|---|---|---|---|---|---|
| 2017 | 4 | 2 | 2 | 26 | 7.1% |
| 2018 | 12 | 10 | 7 | 11 | 38.9% |
| 2019 | 6 | 1 | 1 | 16 | 5.9% |
| 2020 | 22 | 4 | 3 | 24 | 11.1% |
| 2021 | 15 | 2 | 2 | 6 | 25.0% |
| 2022 | 24 | 12 | 7 | 7 | 50.0% |
| 2023 | 16 | 5 | 4 | 28 | 12.5% |
| 2024 | 10 | 3 | 2 | 30 | 6.2% |
| 2025 | 15 | 6 | 5 | 65 | 7.1% |
| 2026 | 47 | 27 | 21 | 93 | 18.4% |

"New product name" = a word mark Nike (or the peer) had not filed before in 2005 to date, excluding house marks (NIKE, SWOOSH, JUST DO IT, JUMPMAN, JORDAN, ACG, AIR, CONVERSE and the peers' own names). Ranking claim computed across all 15 years before writing: Nike's 21 is the highest of 2012 to 2026 (prior maximum 7); the peers' 93 is also the highest (prior maximum 65 in 2025).

Pooled shares (`g7_pooled_share_2017_19_vs_2024_26.csv`, DERIVED): Nike share of Nike plus seven peers, 2017 to 2019 versus 2024 to 2026 (Jan to Sep each year):

| Metric | 2017 to 2019 | 2024 to 2026 | Change |
|---|---|---|---|
| All applications | 11.7% | 18.3% | +6.6 pp |
| Class 25 applications | 10.8% | 15.6% | +4.8 pp |
| Intent-to-use, class 25 | 15.3% | 14.8% | -0.5 pp |
| Intent-to-use, new product names, class 25 | 15.9% | 13.0% | -2.9 pp |

On the pipeline-relevant measures (the last two rows) Nike holds its share against a peer group that is itself filing 3.5 times as many new names (peers' Jan to Sep new intent-to-use class 25 names: 17.7 per year in 2017 to 2019, 62.7 per year in 2024 to 2026).

### 4.3 What the 2026 names are (OPENED, `tm_raw_Nike.jsonl`)

New intent-to-use class 25 names filed Jan to Sep 2026 (21): TECH FLEECE, CA, RADICAL AIRFLOW, AF1, CH, B9, AIR RIFT, NSW, HYPERJOGGER, HYPERJACKET, TOMA, SWOOSHFLY, S.T. DYNAMITE, HYBRID RN, HYBRID FLY, NIKE PRO, NIKE FREE IQ, S.T. CHARGE, GOATEK, ACG PICKLEJUS, FLIGHTKNIT. Filed in calendar 2025 (10): PROTRO, AERONODES, FLYWEB, CC, FOREVER KING, ALL VICTORIES START WITH TRAINING, NIKE MAVN, MAVN, NIKE MIND, PB. Some are apparel, slogans or code names, not footwear franchises. Of Nike's 47 filings Jan to Sep 2026, a batch of core-brand extensions (NIKE, SWOOSH, JUST DO IT in classes 14 and 16, ACG across 9 classes, NIKE GRIND in 28/27/19) inflates the total count and is excluded from the "new names" metric above. This is why "all applications" overstates the signal and the new-name row is the one to quote.

### 4.4 Alternatives tested for the 2026 surge

| Alternative explanation | Test | Result |
|---|---|---|
| General USPTO filing surge | USPTO-wide class 25 applications Jan to Sep: 2025 48,003; 2026 54,578 | +13.7% market-wide vs Nike class 25 +114% (14 to 30) and new-name intent-to-use +320% (5 to 21). Ruled out as the main driver |
| Core-brand extension batches | Remove house marks and non-class-25 | Surge survives (21 new names vs max 7). Batch filings explain part of the 47 total, not the new-name count |
| Re-filing of lapsed names | First-seen test against all Nike filings since 2005 | HYPERVENOM, PHANTOM and BO KNOWS (abandoned 2026-01-05, re-filed 2025-12-01) are re-filings and are automatically excluded from the 21 new names. Effect on the 21: nil |
| Pull-forward of use-based filings | Count only intent-to-use | Done; the metric is intent-to-use only |
| Filing-practice change to trade dress | Design-only (no word) share of Nike filings: 2021 13 of 27, 2022 7 of 30, 2026 9 of 48 | No shift. Ruled out |
| Nike Innovate C.V. holding marks instead of Nike, Inc. | Owner-name search | Zero records; ruled out |

### 4.5 Premise test: do Nike trademark filings lead launches by 12 to 24 months?

(OPENED, DERIVED, `g7_tm_leadlag_first_use.csv`, `tm_raw_Nike.jsonl`.)

- Nike class 25 intent-to-use filings 2012 to 2023 with a declared first-use date: n = 45, median first use minus filing = +78 days, quartiles -220 and +246 days, 64% filed before first use. So the lead is about 2.6 months at the median, not 12 to 24 months.
- Use-based (1(a)) filings are made after launch (first-use date in the USPTO record, OPENED): VAPORFLY first used 2017-07-20, filed 2025-04-29; NIKE ZOOMX first used 2019-04-28, filed 2025-07-07; ALPHAFLY first used 2020-02-26, filed 2020-08-17. Even FLYKNIT, filed as intent-to-use, was filed 2012-03-30, 38 days after its 2012-02-21 first use. HYPERADAPT and LUNAREPIC have zero US word-mark records at all, so trademark counts miss some Nike product names entirely.
- Consequence: trademark counts can only say that something is queued for the next 3 to 12 months. They cannot say what ships in FY28 (June 2027 to May 2028) beyond filings made through about Q1 2027. Jan to Sep 2026 filings map to late FY27 and FY28 H1, which is inside the window.

### 4.6 Software marks (classes 9 and 42)

Nike filed 12 (2021), 10 (2022) and 6 (2023) class 9 or 42 applications (the virtual goods and metaverse push), and 0, 0 and 3 in 2024, 2025 and 2026 (DERIVED). The peers did the same: 7-peer class 9/42 filings fell from 28 (2022) to 5, 2, 3 and 1. Nike's software-class pipeline was not culled idiosyncratically; the whole group stopped. The decline in class 9/42 between 2017 to 2019 and 2024 to 2026 is -19.8% for Nike and -83.8% for the peers (annualized, `g7_tm_change_2024_26_vs_2017_19.csv`).

---

## 5. Patents

### 5.1 Footwear design patents granted, by publication year (OPENED, DERIVED, `g7_pat_annual_by_pub_year.csv`)

| Pub year | Nike | adidas | On | Deckers | New Balance | ASICS | Puma | Lululemon | 6 footwear peers | Nike share of Nike+7 peers |
|---|---|---|---|---|---|---|---|---|---|---|
| 2012 | 67 | 0 | 0 | 8 | 3 | 1 | 0 | 0 | 12 | 84.8% |
| 2013 | 201 | 0 | 0 | 2 | 3 | 0 | 0 | 0 | 5 | 97.6% |
| 2014 | 158 | 2 | 0 | 12 | 3 | 0 | 0 | 0 | 17 | 90.3% |
| 2015 | 127 | 2 | 0 | 5 | 2 | 2 | 0 | 1 | 11 | 91.4% |
| 2016 | 135 | 1 | 0 | 17 | 6 | 0 | 3 | 0 | 27 | 83.3% |
| 2017 | 665 | 14 | 1 | 10 | 0 | 2 | 0 | 0 | 27 | 96.1% |
| 2018 | 388 | 27 | 6 | 6 | 1 | 1 | 5 | 0 | 46 | 89.4% |
| 2019 | 502 | 34 | 0 | 3 | 4 | 0 | 29 | 0 | 70 | 87.8% |
| 2020 | 621 | 28 | 3 | 2 | 4 | 1 | 84 | 0 | 122 | 83.6% |
| 2021 | 499 | 32 | 1 | 11 | 3 | 2 | 41 | 1 | 90 | 84.6% |
| 2022 | 606 | 22 | 1 | 2 | 3 | 0 | 20 | 0 | 48 | 92.7% |
| 2023 | 710 | 16 | 5 | 25 | 5 | 3 | 16 | 2 | 70 | 90.8% |
| 2024 | 610 | 36 | 6 | 28 | 2 | 11 | 41 | 3 | 124 | 82.8% |
| 2025 | 586 | 39 | 13 | 20 | 1 | 10 | 30 | 3 | 113 | 83.5% |
| 2026 (to Oct 13) | 378 | 21 | 13 | 27 | 2 | 37 | 13 | 1 | 113 | 76.8% |

Nike's 2017 value (665 versus 388 to 502 around it) is a one-year spike (a batch of grants; the cause is not visible in the data). Using a 2018 to 2019 base of 445 per year instead of 2017 to 2019 (518.3), the 2024 to 2026 average of 559.5 is +25.7% instead of +7.9%.

### 5.2 Footwear utility patents (CPC A43B or A43C), granted and published applications (DERIVED)

| Pub year | Nike grants | 6 peers grants | Nike share | Nike apps published | 6 peers apps | Nike share |
|---|---|---|---|---|---|---|
| 2017 | 211 | 35 | 85.8% | 325 | 46 | 87.6% |
| 2018 | 254 | 26 | 90.7% | 270 | 57 | 82.6% |
| 2019 | 287 | 31 | 90.3% | 291 | 53 | 84.6% |
| 2020 | 260 | 45 | 85.2% | 313 | 61 | 83.7% |
| 2021 | 285 | 49 | 85.3% | 315 | 92 | 77.0% |
| 2022 | 257 | 48 | 83.7% | 239 | 88 | 72.2% |
| 2023 | 317 | 64 | 82.6% | 317 | 96 | 76.2% |
| 2024 | 322 | 92 | 76.7% | 275 | 114 | 69.3% |
| 2025 | 272 | 118 | 69.0% | 199 | 133 | 59.1% |
| 2026 (to Oct 13) | 176 | 93 | 65.0% | 199 | 104 | 65.0% |

(Shares use Nike plus all seven peers; Lululemon adds under 10 footwear documents a year, and the CSV gives the six-peer version, which differs by about 1 point.)

### 5.3 Change 2024 to 2026 vs 2017 to 2019 (DERIVED, `g7_pat_change_2024_26_vs_2017_19.csv`, `g7_pooled_share_2017_19_vs_2024_26.csv`)

Per-year averages; the 2024 to 2026 average is (2024 + 2025 + 2026 annualized by 1 / 0.784) / 3:

| Measure | Nike 2017 to 2019 | Nike 2024 to 2026 | Nike change | Six footwear peers: 2017 to 2019 | Six peers: 2024 to 2026 | Six peers change |
|---|---|---|---|---|---|---|
| Footwear design grants | 518.3 | 559.5 | +7.9% | 47.7 | 127.1 | +166.6% |
| Footwear utility grants | 250.7 | 272.9 | +8.9% | 30.7 | 109.6 | +257.3% |
| Footwear utility apps published | 295.3 | 242.7 | -17.8% | 52.0 | 126.6 | +143.4% |
| All utility apps published | 448.7 | 341.1 | -24.0% | 87.3 | 162.7 | +86.3% |
| All utility grants | 420.7 | 371.3 | -11.7% | 63.3 | 142.3 | +124.8% |
| All design grants | 628.0 | 618.0 | -1.6% | 55.0 | 150.3 | +173.2% |

Pooled shares (same-length windows, no annualization; 2026 to Oct 13 for Nike and peers alike): Nike footwear design grants 91.6% to 81.5% (-10.1 pp); footwear utility grants 89.1% to 70.9% (-18.2 pp); footwear utility apps published 85.0% to 64.7% (-20.3 pp).

### 5.4 The pipeline for FY28 is mostly invisible in patents (right-censoring)

- Nike design patents take a median 14 to 21 months from filing to grant (2017 to 2026 grants, `g7_pat_lags_months.csv`); utility patents take 25 to 32 months to grant. A design filed in 2025 or 2026 is largely not public yet, and utility applications are published at about 18 months from earliest priority. Publication-year counts for 2026 therefore describe filings made roughly in 2024 to early 2025.
- Filing-year cohorts of Nike footwear design grants (`g7_pat_annual_by_filing_year.csv`): 2015 432, 2016 522, 2017 427, 2018 474, 2019 725, 2020 520, 2021 718, 2022 661, 2023 553, 2024 516 (partly censored), 2025 194 (heavily censored). The 2023 cohort, which is close to fully visible, is above the 2017 and 2018 cohorts and below 2019, 2021 and 2022. The 2024 cohort is already 93% of 2023 with grants still arriving. No evidence of a filing stop through 2024.
- Everything after 2024 requires a source that publishes sooner (EU registered designs, Hague registrations, PCT publications). All were blocked (Section 9).

### 5.5 Patent output per revenue dollar (DERIVED, `g7_nike_ip_intensity.csv`; revenue from `data/nike_filing_facts.csv`, Nike Brand footwear, 10-K)

Footwear design grants per $B of Nike Brand footwear revenue: 2017 31.5, 2018 17.4, 2019 20.7, 2024 18.2, 2025 19.9 (2026 is understated because patents run to Oct 13 against a full fiscal year). Design intensity is flat against 2018 to 2019. Footwear utility applications published per $B: 2017 15.4, 2018 12.1, 2019 12.0 (mean 13.2), 2024 8.2, 2025 6.7, which is -38% and -49% against the mean. Footwear utility grants per $B: 10.0, 11.4, 11.8 (mean 11.1) versus 9.6 and 9.2 (-14% and -17%). Footwear revenue rose from $24.2B (FY19) to $33.4B (FY24) while utility publications fell, so per revenue dollar Nike is lighter than its own history on utility patents. This is the one IP measure that points the short's way; it is a count of documents, not of franchise potential.

### 5.6 Did high filing precede success? (ruling out "patent counts predict revenue")

Design filing cohorts peaked in 2019 (725), 2021 (718) and 2022 (661), which feed launches roughly in FY22 to FY24. Revenue peaked in FY24 ($51,362M) and fell to $46,309M in FY25 and $46,398M in FY26 (facts CSV). Filing volume was highest immediately ahead of the revenue decline, so the count is not a leading indicator of Nike's revenue direction. The data cannot separate quality (franchise potential) from quantity (designs filed per shoe model). This is a limit on any inference from IP counts, in both directions.

---

## 6. Trademark abandonments and cancellations 2024 to 2026 (pipeline culled?)

OPENED, DERIVED, `g7_tm_abandon_cancel.csv`, `g7_nike_tm_abandoned_2024_26_detail.csv`, `g7_tm_cohort_abandon_rate.csv`.

| Event year | Nike abandoned | of which intent-to-use | of which no statement of use | of which class 25 | Nike registrations cancelled | cancelled class 25 |
|---|---|---|---|---|---|---|
| 2012 to 2023 average | 4.5 | 4.3 | 3.4 | 3.3 | 9.0 | 4.5 |
| 2024 | 7 | 7 | 6 | 1 | 3 | 2 |
| 2025 | 4 | 3 | 2 | 3 | 1 | 0 |
| 2026 (Jan to Sep) | 5 | 5 | 4 | 2 | 1 | 1 |

- 16 abandonments across 2024 to Sep 2026 against a 2012 to 2023 average of 4.5 per year. Annualizing 2026 (5 x 365/273 = 6.7) gives 5.9 per year, +31%, or about 1.4 more filings a year (DERIVED).
- Composition: 12 of the 16 carry class 9, 41 or 42 goods (METADUNGEON, PODX, SPACE POD, LOOT POD, D.A.R.T X, CRYPTOKICKS, MNLTH, FOOTWARE, DREAM IT. MAKE IT. PLAY IT., WHERE SPORT HAS NO RULES, and two others), i.e. the virtual-goods programme lapsing after years of extensions with no statement of use; 9 of them have no class 25 goods. Class 25 only: ZION (failure to respond), BO KNOWS (no statement of use; re-filed 2025-12-01) and FOREVER KING (lost an inter partes proceeding, abandoned 2026-04-23). Three more touch class 25 together with virtual-goods classes (METADUNGEON, DREAM IT. MAKE IT. PLAY IT., WHERE SPORT HAS NO RULES). Total touching class 25: 6.
- Registration cancellations are falling (9.0 per year average to 3, 1, 1), which reflects fewer lapsed renewals, not pruning.
- Cohort view: the share of each filing-year cohort now abandoned is 4.8% to 5.3% for 2024 and 2025 filings, below the 2012 to 2023 cohorts (8% to 55%; 2015 is 0 of 3), because young filings have not had time to lapse. This is not a pruning signal either way.
- Peers' abandonment counts are in the CSV for comparison.

---

## 7. Alternatives considered and ruled out (summary)

| Alternative | Evidence | Verdict |
|---|---|---|
| Nike changed filing strategy (moved to other jurisdictions or filing vehicles), so US counts mislead | US design filings by filing year are stable (cohorts 427 to 725 for 2015 to 2024); trademark filings rose. EU, Hague and PCT could not be opened | Cannot rule out for utility applications (-17.8% to -24%); not supported for designs or trademarks |
| Portfolio pruning | 16 abandonments 2024 to 2026, 11 of them software and virtual-goods marks; class 25 abandonments 6 | Ruled out for the footwear pipeline; the virtual-goods programme did wind down |
| Shift to trade dress | Design-only filings 9 of 48 in 2026, 13 of 27 in 2021 | Ruled out |
| API or index coverage gap | Owner totals within about 4% of Trademarkia; 56 of 60 patent cells exactly equal an independent count; USPTO-wide counts consistent | Ruled out for the US data |
| 2026 trademark spike is a general filing surge | USPTO class 25 +13.7% | Ruled out |
| 2017 design spike distorts the base | Computed both with and without 2017 | Conclusion unchanged (Section 5.1) |
| Pre-launch lead of 12 to 24 months for trademarks | Median 78 days (n = 45) | Premise false for Nike trademarks |
| IP counts predict revenue | Peak design filing cohorts 2019 to 2022 preceded the FY25 revenue fall | Not a predictor in Nike's history |
| Hoka inside Deckers distorts Deckers | 15 HOKA word marks out of 193 Deckers case files; design patents titled generically | Cannot split; Deckers includes UGG. Treat Deckers as a loose proxy |
| Lululemon is not a footwear maker | Reported with and without (peer sets of 7 and 6) | Conclusion unchanged |

Surviving explanations for "peers file more IP": (a) peers are building their footwear businesses from small bases (On, ASICS, Puma, adidas), (b) peers use US design patents more than before (Puma 84 design grants in 2020 alone). The data cannot separate genuine R&D growth from patent-count inflation (counts, not quality). What would decide it: forward citations and claim counts per patent (Lens or Google Patents), unavailable here.

---

## 8. Honest limits

- All counts are number of case files or documents, not products. A single Nike shoe model can generate many design patents (a variant per colorway or sole view) and Nike design counts per shoe model are not disclosed anywhere I could open.
- Trademark ownership is current owner at the 2026-10-01 snapshot. A mark assigned away from Nike would drop out of history.
- The 2026 trademark window ends Sep 30 and the patent window Oct 13.
- No IP count translates into revenue. Revenue conversion needs management launch calendars (not in filings) or retailer line lists.

---

## 9. Routes tried (every route and its result)

| # | Fact sought | Route | Result |
|---|---|---|---|
| 1 | US trademark applications, abandonments | USPTO Trademark Search backend, `tmsearch.uspto.gov` (JSON, anonymous; the TESS successor) | **Worked** (13.3M records, loaded 2026-10-01) |
| 2 | Same | USPTO TSDR, `tsdr.uspto.gov` | Partial: host reachable, JavaScript app; no bulk endpoint without an API key |
| 3 | Same | USPTO bulk data `bulkdata.uspto.gov`; `developer.uspto.gov` | Blocked: bulkdata CONNECT 502; developer site redirects to `data.uspto.gov` Open Data Portal |
| 4 | Same | USPTO Open Data Portal API, `api.uspto.gov` | Blocked: "Missing Authentication Token" (needs an API key, requires registering an email; not done, per the no-email rule) |
| 5 | Cross-check of owner totals | Trademarkia owner pages | **Worked** (SECONDARY mirror; totals within about 4%) |
| 6 | EU and global trademarks | EUIPO eSearch (`euipo.europa.eu/eSearch`), TMview (`tmdn.org/tmview`) | Blocked: page shell loads, data endpoints return "Empty reply from server" (no JSON path reachable) |
| 7 | Global trademarks | WIPO Global Brand Database (`www3.wipo.int/branddb`, `branddb.wipo.int`) | Blocked: returns an altcha proof-of-work bot challenge; not circumvented |
| 8 | Archived copies | `web.archive.org`, `archive.ph`, `index.commoncrawl.org` | Blocked: tunnel resets (proxy log) |
| 9 | Third-party trademark mirrors | `uspto.report`, `trademarks.justia.com` | Blocked: HTTP 403 |
| 10 | US patents granted and published | USPTO Patent Public Search `ppubs.uspto.gov` (anonymous JSON session) | **Worked** |
| 11 | Same | PatentsView (`search.patentsview.org`, `data.patentsview.org`, `api.patentsview.org`) | Blocked: CONNECT 502 for the new hosts; the legacy API redirects (301) to the Open Data Portal transition guide; the S3 bulk file returns AccessDenied |
| 12 | Same | Lens.org free search and API | Blocked: web pages need a JavaScript session; API `api.lens.org` returns 401 (token needs an account with an email) |
| 13 | Same | Google Patents (`patents.google.com/xhr/query`), Google BigQuery patents-public-data | Blocked: 503 CAPTCHA page; `bq` has no project or credentials |
| 14 | Same | Espacenet, EPO OPS | Blocked: 403; OPS needs credentials |
| 15 | Same | WIPO PATENTSCOPE | Blocked: 403 |
| 16 | Same | FreePatentsOnline, Justia patents | Blocked: SSL reset, 403 |
| 17 | Design patents and registrations filed 2025 to 2026 (forward view) | WIPO Hague Global Design Database (`designdb.wipo.int`), EUIPO DesignView | Partial or blocked: shell loads, no reachable search endpoint; EUIPO empty replies |
| 18 | Verification of the patent pull | Independent count queries on PPUBS | **Worked** (Section 3) |

Routes 6 to 9, 11 to 17 are more than five genuinely different routes for the question "what did Nike and its peers file in the EU or globally in 2025 to 2026" and for the patent cross-check; the result for those facts is **not obtained**. The US answer was obtained by routes 1, 10 and 18.

**What would settle the open items and how to get it:** (1) Registered Community Designs and Hague registrations by Nike, Inc. filed 2025 to 2026 (published within days to months, so they show the FY28 pipeline directly): EUIPO DesignView or WIPO Global Design Database exports; a person with a browser can run the search by holder name "Nike" and download the CSV, or a Lens.org or IFI Claims token (free or institutional) would allow it by API. (2) PCT publications (18 months) and forward citations: Lens.org token or PATENTSCOPE export. (3) Revenue mapping: Nike's launch calendar by quarter or a retailer line list, neither of which is in public filings. (4) Per-patent quality (claim counts, family size, forward citations).
