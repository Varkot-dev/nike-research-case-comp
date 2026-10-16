# W8: Product newness counted from launch calendars, Jan 2023 to Dec 2026 (announced)

Date of work: Oct 16, 2026. Extends `research_notes/jordan_extracts/rabbit_hole/release_counts.md` (Jordan retro counts) and `research_notes/Smoking gun hunt/G7_ip_pipeline.md` (2026 trademark names). Data and scripts: `data/hunt/w8_launch_newness/`. Monthly counts CSV: `research_notes/Wave 3/W8_launch_monthly_counts.csv`.

Evidence tags: OPENED (page or file read in full or parsed by me), SNIPPET (search-result or fetch-summary text only), DERIVED (my arithmetic on OPENED data).

## Answer

1. **Smoking gun: no.** Newness in the launch flow is rising by count, but it is (a) concentrated in basketball signature lines and in a handful of running models, (b) not visible in the forward calendars for holiday 2026 and spring 2027, which are blind to running and retro-heavy beyond about 8 weeks, and (c) too small in dollars to refill the classics gap by FY28 on any sizing I can support. It does not break the lean-short thesis and it does not hand the long a clean datapoint.
2. **Nike new-model share of its own calendar rises** (Sneaker Bar Detroit, "SBD", adult colorway releases, DERIVED): new-model plus new-version rows (including collabs built on a new or performance base) were 8.8% of Nike rows in H1 2023, 35.1% in H1 2024, 44.7% in H2 2025, 47.1% in H1 2026. Ratio of new to retro rows: 0.11 (H1 2023), 0.57 (H1 2024), 0.83 (H2 2025), 0.92 (H1 2026). Retro and retro-based collabs were still 51.1% of Nike rows in H1 2026.
3. **Jordan newness is flat to down** on the same calendar: new share 6% (H1 2023), 18% (H2 2025), 7% (H1 2026 and H2 2026 scheduled). 93% of scheduled H2 2026 Jordan rows are retro or retro-based. (Jordan counts from SBD do not reconcile with the earlier Sole Retriever count in 2025, see Alternatives, so this is direction only.)
4. **New franchise debuts (class A, first appearance on SBD)** for Nike: 5 in 2023, 6 in 2024, 9 in 2025, 10 in 2026 (3 of the 10 are forward-listed Oct to Dec); Jordan adds one in 2023 and one in 2025. Real but small numbers.
5. **Calendars cannot show the running pipeline.** SBD and Nice Kicks list none of Alphafly 4, Apex, Swooshfly, Hybrid RN, Hybrid Fly, Vomero 18 or Vomero Plus (0 matches in 2,949 SBD rows and 106 Nice Kicks rows, OPENED); Pegasus Premium, which SR carries with dozens of colorway pages, shows up on SBD only as 3 collab rows (Melitta Baumeister, A Ma Maniere). Only 5 of 279 Nike plus Jordan performance-version rows on SBD are running or training (DERIVED). Sole Retriever (SR) article slugs and Nike's newsroom do show them.
6. **Peers' share of new models by half-year could not be built from the hype calendars** (SBD coverage of New Balance fell from 41 rows in H2 2023 to 4 in H1 2026 and Puma from 22 in H2 2024 to 1, so share is an artifact). On running, RunRepeat's reviewed catalog gives Nike 13% to 28% of new running model-versions among six brands per half-year with no upward trend (Nike 5 to 11 of 38 to 46).
7. **FY28 sizing (assumption-driven, DERIVED):** 18 new franchises times $120M each is $2.2B, 7.3% of FY26 footwear revenue ($29,525M, FY2026 10-K p. 32, from `data/nike_filing_facts.csv`). Range 3.0% to 9.8% on the cases I consider defensible. Refilling the gross classics cut of more than $4B (13.5% of FY26 footwear; repo figure, gross and unaudited) would take about 34 franchises at $120M, which is 3 to 4 years of the observed debut pace.

## What I built

| Source | What it gave | Coverage | Tag |
|---|---|---|---|
| Sneaker Bar Detroit main calendar, 8 archived half-year pages plus current page | 2,949 deduped release rows, name, style code, date, price, Jan 2023 to Jun 2027 | Nike, adidas, New Balance, Puma, Reebok, some ASICS; almost no running, no On or Hoka | OPENED |
| SBD Air Jordan calendar, 9 archive pages plus current | Jordan rows (in the 2,949), through Jun 2027 | Jordan; July 2025 page missing | OPENED |
| Nice Kicks upcoming calendar (pages 1 to 3) | 106 forward rows, Oct 16 2026 to Jun 29 2027 | Nike 27, Jordan 47, adidas 13; snapshot only | OPENED |
| Nike SNKRS upcoming (nike.com/launch/upcoming, page state) | 20 products launching Oct 16 to Oct 24, 2026 | 8-day window only | OPENED |
| Nike product_feed threads API (the public feed behind nike.com/launch) | 1,050 of 6,564 SNKRS threads (API refuses anchor above about 1,450), Nov 2023 to Oct 2026, mostly editorial | Partial, mixed editorial and product, no launch date field | OPENED |
| Sole Retriever sitemaps (news, 17,384 URLs; products, 10,007 URLs) | 9,033 "release-date" article slugs with lastmod and target month or season; 3,166 Nike plus 1,083 Jordan product slugs by model | Article volume collapsed from 2025 (see Alternatives); product lastmod is a bulk rewrite (Aug 2026), unusable for dating | OPENED |
| RunRepeat running catalog (22 catalog pages, 632 shoe review pages) | 564 dated shoes; release-date field on 102, review-publication date on 462 | Reviewed shoes only (selection), all brands incl. Hoka and On | OPENED |
| Marathon Handbook running release calendar | 166 entries, all 2025 except one Q1 2026 | Fetch-summary, not raw HTML | SNIPPET |
| Nike newsroom pages (Swooshfly, Hybrid) and Sole Retriever, Hypebeast, Captain Creps articles via search | Launch dates for Hybrid RN, Hybrid Fly, Alphafly 4, Apex, Swooshfly | Five announcements | OPENED (newsroom), SNIPPET (press) |

Files: `w8_release_rows_sbd.csv` (row level with class, collab base class, segment, debut flag), `w8_monthly_counts_sbd.csv`, `w8_halfyear_nike_jordan_sbd.csv`, `w8_release_rows_nicekicks_upcoming.csv`, `w8_runrepeat_running_shoes.csv`, `w8_runrepeat_nike_share_by_halfyear.csv`, `w8_marathonhandbook_2025_running_calendar.csv`, `w8_sr_news_release_articles.csv`, `w8_sr_announced_by_oct15_vintage.csv`, `w8_sr_product_db_nike_jordan_mix.csv`, `w8_snkrs_upcoming_snapshot_2026-10-16.csv`, `w8_snkrs_feed_threads_partial.csv`, `w8_forward_vs_realized_composition.csv`, `w8_trademark_calendar_check.csv`, `w8_fy28_new_model_sizing_grid.csv`, `raw/`, `scripts/`.

### Classification rules (rule-based on the release name; `scripts/classify2.py`)

- **D collab:** name contains " x " (partner x Nike or Jordan). I also classify the base product of each collab so retro-based collabs can be counted as retro.
- **A new model or franchise:** explicit list of models whose first calendar appearance is Jan 2023 or later or whose line launched 2022 or later (Ja 1, Book 1, Sabrina 1, Caitlin 1, A'One, Tatum 1, Luka 1, Air Max Dn, Dn8, Muse, Pulse, Mind 001 and 002, Clogposite, Lunar Roam, NOCTA Glide, Hyperflight, First Sight, V2K Run, V5 RNR, Rejuven8, Vomero Plus and Premium, Pegasus Premium, GT Future, ACG models, Air Jordan 40xx numbers).
- **B new version of a performance line:** LeBron 20 and up, KD 16 and up, Ja 2 and up, Book 2 and up, Sabrina 2 and up, GT Cut, Freak and Immortality, Luka, Tatum and Zion 2 and up, Air Jordan 36 to 42, Pegasus, Vomero 18 and up, Alphafly, Vaporfly, Structure, Invincible, Zoom Fly and similar running names.
- **C retro or classic:** Dunk, AF1, Air Jordan 1 to 23, Air Max 1/90/95/97/Plus and other heritage Air Max, Blazer, Cortez, Terminator, Foamposite, Shox, Kobe Protro, Zoom Vomero 5, older LeBron and KD numbers, and similar heritage names.
- **Excluded:** golf, cleats, slides, clogs (95 rows). Kids (GS, PS, TD) and women's rows are kept in the files and flagged; headline tables use adult rows (women's included).
- **Debut flag:** first row of a model key (name minus colorway, size and suffix words) in classes A and B, counted only if first seen April 2023 or later (3-month burn-in because the series starts mid-cycle).
- **Not used:** unclassified rows (class U, 0 to 6 per half-year for Nike, under 3% of rows).

## 1. Nike counts by half-year (SBD, adult rows, Jan 2023 to Dec 2026)

| Half-year | Rows | A new | B version | C retro | D collab | of which collab on retro base | New-equiv share* | Retro-equiv share* | New / retro ratio |
|---|---|---|---|---|---|---|---|---|---|
| 2023 H1 | 125 | 4 | 6 | 88 | 25 | 16 | 8.8% | 83.2% | 0.11 |
| 2023 H2 | 202 | 16 | 8 | 122 | 50 | 45 | 12.4% | 82.7% | 0.15 |
| 2024 H1 | 151 | 25 | 18 | 73 | 33 | 20 | 35.1% | 61.6% | 0.57 |
| 2024 H2 | 162 | 21 | 20 | 72 | 45 | 31 | 29.6% | 63.6% | 0.47 |
| 2025 H1 | 169 | 25 | 28 | 72 | 44 | 22 | 39.6% | 55.6% | 0.71 |
| 2025 H2 | 197 | 32 | 41 | 66 | 58 | 40 | 44.7% | 53.8% | 0.83 |
| 2026 H1 | 221 | 25 | 60 | 89 | 47 | 24 | 47.1% | 51.1% | 0.92 |
| 2026 H2 (Jul to Sep realized, Oct to Dec listed) | 155 | 17 | 44 | 61 | 30 | 19 | 43.9% | 51.6% | 0.85 |

*New-equivalent = A plus B plus collabs built on an A or B base; retro-equivalent = C plus collabs on a C base. File: `w8_halfyear_nike_jordan_sbd.csv`. June 2023 has zero Nike rows because the SBD H1 2023 page omits June, so 2023 H1 is a 5-month count. The 2026 H2 row is thin after October (Nov 11, Dec 7 Nike rows listed versus 26 to 46 realized in a normal month).

Calendar-year Nike rows (DERIVED): 2023 327 (A 20, B 14, C 210, D 75); 2024 313 (46, 38, 145, 78); 2025 366 (57, 69, 138, 102); 2026 376 incl. listed (42, 104, 150, 77). Retro (class C) rows were 210, 145, 138, 150 in 2023 to 2026, a 29% decline from 2023 to 2026, not a collapse.

**What the "new" rows are.** Of the 279 adult B rows (Nike plus Jordan) in 2023 to 2026, 98% by SBD naming are basketball signature lines (LeBron 23, KD 18 and 19, Ja 3, Book 2, Sabrina 3, Giannis Freak, GT Cut) and the Jordan performance numbers; running and training make up 5 rows (DERIVED, `segment` column). New franchises (A) by first appearance, Nike plus Jordan: 2023 (Air Max Pulse, Tatum 1, Ja 1, Sabrina 1, NOCTA Glide, ACG Torre, Lunar Roam), 2024 (ACG Exploraid, Book 1, Air Max Dn, ACG Rufus, Air Max SNDR, Clogposite), 2025 (Air Max Muse, Dn8, Air Superfly, Air Max Craze, A'One, ACG Phassad, GT Future, Rejuven8), 2026 (V2K Run, Vomero Plus, Mind 001 and 002, First Sight, Zoom Hyperflight, V5 RNR, Vomero Premium, Caitlin 1, Air Max Foamdome, plus unexplained Air Jordan 4014 to 4028 numbers). Many are ACG, women's lifestyle or collector lines with no disclosed revenue.

**Independent corroboration of the retro side.** Dunk rows on SBD fell 62 (H2 2023) to 25 (H2 2024) to 11 (H1 2026) and 2 (H2 2026 listed to date); the Dunk share of SR Nike release-date articles fell from 8.9% to 3.6% over the same span (two sources, same direction, DERIVED), consistent with management's "nearly 50%" Dunk cut in Q1 FY27 (repo note `franchise_oversupply.md`). AF1 rows did not fall (14, 12, 4, 13, 10, 15, 23, 25), so the retro cut is Dunk, not the whole classics group.

## 2. Jordan

SBD Jordan rows by half-year (adult): 65, 85, 73, 55, 50, 50, 54, 58; new-equivalent share 6%, 20%, 22%, 13%, 16%, 18%, 7%, 7% (`w8_halfyear_nike_jordan_sbd.csv`). New Jordan models are few: Tatum, Luka and Zion numbered versions and Air Jordan 38 to 41. Forward Jordan (Oct 16 2026 to Mar 31 2027): SBD 41 rows, 37 retro, 3 collab, 1 version; Nice Kicks 36 rows, 29 retro. The Oct 1 2026 Hill statement to cut Jordan retro volume and frequency (repo `JORDAN_MARKET_FINDINGS.md`) is not yet visible in any calendar, as expected for a 2027 action.

## 3. Trademark names versus calendars (G7 list)

Of the 21 new class 25 names filed Jan to Sep 2026, the check (`w8_trademark_calendar_check.csv`, 6 calendar sources plus Nike newsroom and web search for each):

| Name | Filed | What it is | First public appearance | Launch |
|---|---|---|---|---|
| SWOOSHFLY | 2026-05-15 | New running model (Nike: "isn't a reduced version of an existing racing shoe") | Nike newsroom and SR, 2026-09-30 (4.5 months after filing) | China Feb 2027, global spring 2027 |
| HYBRID RN | 2026-06-03 | New training/running model | Nike newsroom 2026-08-03 (2 months) | China 2026-09-24, global 2026-10-08 |
| HYBRID FLY | 2026-06-03 | New racing model | Nike newsroom 2026-08-03 (2 months) | Global April 2027 |
| GOATEK | 2026-07-23 | Outsole technology inside Swooshfly | 2026-09-30 | with Swooshfly |
| ACG PICKLEJUS | 2026-08-24 | ACG trail/running shoe | SR article 2026-08-27 (3 days) | not dated |
| RADICAL AIRFLOW | 2026-02-11 | ACG collection | SR article 2026-07-01 | July 2026 |
| S.T. CHARGE | 2026-07-21 | Cade Cunningham signature shoe | SR 2026-02-18, 5 months before filing | SBD Jul 1 2026 onward |
| S.T. DYNAMITE | 2026-06-02 | Nike ST youth style | SR product page by 2026-09-23 | not dated |
| AIR RIFT | 2026-03-24 | Heritage model | SR 2023-05-09, 34 months before filing | many releases since 2023 |
| HYPERJOGGER, NIKE FREE IQ, FLIGHTKNIT | 2026-03-24, 06-25, 09-09 | Unknown | none found anywhere | none |

Result: 9 of 21 names are visible on a calendar or announcement (Swooshfly, Hybrid RN, Hybrid Fly, Goatek, Picklejus, Radical Airflow, S.T. Charge, S.T. Dynamite, Air Rift); AF1 is an existing franchise; Tech Fleece, Hyperjacket and Nike Pro are apparel or house names; CA, CH, B9, NSW and TOMA are too generic to search; Hyperjogger, Free IQ and Flightknit are on nothing. For the genuinely new footwear names the lag from filing to first public mention was 3 days to 4.5 months, so the filing led the announcement but only by one to two quarters. Three names (S.T. Charge, Nike Mind, Air Rift) were on calendars before the filing, so the filing is not a consistent leading indicator. Of the 2025 filings, MAVN, AERONODES, FLYWEB, FOREVER KING are on no calendar 12 to 16 months after filing. G7's count of 21 new names therefore overstates the number of distinct new footwear franchises: of the 21, 3 are confirmed new footwear models (Swooshfly, Hybrid RN, Hybrid Fly), 3 are ACG or technology names (Picklejus, Radical Airflow, Goatek), 2 are ST-line names (Charge is a signature shoe already on sale, Dynamite a youth style) and 1 is a heritage model (Air Rift).

## 4. Peers: Nike share of new models

- **Hype calendars are unusable for peer share.** SBD rows by brand, H2 2023 to H1 2026: New Balance 41 to 4, Puma 12 to 1, Reebok 14 to 9, adidas 51 to 43 while Nike 207 to 237 (DERIVED, SBD). The editors narrowed to Nike over time, so any peer share from SBD is a curation artifact.
- **RunRepeat reviewed running catalog** (six brands, dated shoes, class A = unnumbered name, B = version 2 or later; `w8_runrepeat_nike_share_by_halfyear.csv`):

| Half-year | Nike | Six-brand total | Nike share | Nike A of six A | Nike B of six B |
|---|---|---|---|---|---|
| 2023 H1 | 3 | 13 | 23.1% | 0 of 0 | 3 of 13 |
| 2023 H2 | 6 | 46 | 13.0% | 1 of 14 | 5 of 32 |
| 2024 H1 | 11 | 40 | 27.5% | 1 of 8 | 10 of 32 |
| 2024 H2 | 9 | 42 | 21.4% | 5 of 14 | 4 of 28 |
| 2025 H1 | 5 | 38 | 13.2% | 1 of 9 | 4 of 29 |
| 2025 H2 | 8 | 42 | 19.0% | 2 of 14 | 6 of 28 |
| 2026 H1 | 7 | 44 | 15.9% | 4 of 14 | 3 of 30 |

  Nike new-franchise (A) rows in 2024 H2 to 2026 H1: 12 of 51 (24%). Caveats: 462 of 564 dates are RunRepeat review-publication dates (lag the launch by weeks to months); it is a sample (it holds 72% of the Nike shoes Marathon Handbook lists for 2025: 13 versus 18); half-year samples are 8 to 14 per brand. 2026 H2 (Nike 1 of 21) is incomplete.
- **Marathon Handbook 2025 running calendar** (SNIPPET): Nike 18 of 80 entries for the six brands (22.5%) versus ASICS 14, Hoka 14, New Balance 13, On 11, adidas 10. Of Nike's 18, one is unnumbered new (Pegasus Premium), the rest are version updates or Q1 2026 Alphafly 4.
- **What this means:** in running, the field launches roughly 40 new model-versions per half-year across six brands; Nike supplies about one in five, of which most are version updates. Nike is not out-launching peers in count. Whether its models outsell peers' is a revenue question this data cannot answer.

## 5. Is newness rising for holiday 2026 and spring 2027?

Forward calendar composition (Nike, adult rows; `w8_forward_vs_realized_composition.csv`):

| Window | Source | Rows | New (A+B) share | Retro (C) share | Collab share |
|---|---|---|---|---|---|
| Oct 16 2023 to Mar 31 2024 | SBD realized | 178 | 21.3% | 54.5% | 20.2% |
| Oct 16 2024 to Mar 31 2025 | SBD realized | 151 | 31.8% | 39.7% | 27.2% |
| Oct 16 2025 to Mar 31 2026 | SBD realized | 208 | 40.9% | 33.7% | 25.5% |
| Oct 16 2026 to Mar 31 2027 | SBD forward-listed | 47 | 36.2% | 48.9% | 10.6% |
| Oct 16 2026 to Mar 31 2027 | Nice Kicks forward-listed | 27 | 44.4% | 33.3% | 14.8% |
| Dec 1 2026 to Mar 31 2027 only | SBD forward-listed | 16 | 37.5% (5 Caitlin 1, 1 LeBron 24) | 50.0% | 6.3% |
| 2026 and 2027 undated entries | SBD | 32 | 3.1% | 78.1% | 18.8% |

Reading: the next 8 weeks (Halloween and Black Friday) look like prior years, new-heavy, because they are basketball signature colorways (Sabrina 4, Ja 4, KD 19, Book 2, Freak 8, LeBron 24, Caitlin 1, Air Max Foamdome, A'Two). Beyond December the list is 50% to 78% retro (Kobe Protro, Foamposite, Zoom Flight, Air Max 95, AF1), and the new items are Caitlin 1 colorways. This does not tell us the true holiday 2026 or spring 2027 mix, for two measured reasons:
1. **Lead-time bias.** Retro dates are set far ahead; new products are revealed late. Swooshfly was announced on Sep 30 for Feb 2027 and Hybrid Fly on Aug 3 for April 2027, and neither is on SBD or Nice Kicks. I could not get historical forward snapshots (Wayback is blocked by the egress policy), so I cannot calibrate how much a forward list understates final newness.
2. **Running blindness.** The named running pipeline for the window is Hybrid RN (Oct 8 2026), Alphafly 4 (wide release reported as Oct 29 2026; Nike says "October"), Apex (January 2027), Swooshfly (February 2027 China, spring global), Hybrid Fly (April 2027). None is on a hype calendar. SR has Alphafly 4 (article 2026-09-17), Apex (article and product page 2026-09-30 and 10-07), Hybrid (2026-08-03).

SR announcement vintages (articles published by Oct 15 and targeting Oct to Jun; `w8_sr_announced_by_oct15_vintage.csv`): new share 17.7% (2023, n=293), 14.4% (2024, n=139), 28.3% (2025, n=60), 19.7% (2026, n=71). No trend, and the 2025 and 2026 samples are small because SR news volume fell 89% (Nike articles 799 in H2 2022 to 87 in H1 2025).

**Verdict on the test:** holiday 2026 is not dominated by retro in Nike's own signature and Air Max lines (new-equivalent about 36% to 44% of dated rows), but it is still retro-dominated for Jordan (90%) and for everything dated after December. The data cannot separate "newness rising" from "new is revealed late". What would decide it: a dated snapshot of these calendars in October 2025 (to measure the forward-list bias), Nike's pair or dollar split by franchise, and the Q2 FY27 call (December 2026) disclosure of new-franchise sell-through.

## 6. FY28 sizing: new models as a share of Nike footwear revenue (assumption-driven)

Base: FY26 NIKE footwear revenue $29,525M (FY2026 10-K p. 32; `data/nike_filing_facts.csv`, revenue_footwear FY2026). I hold FY28 footwear flat at that level to isolate the share.

Definition: a "new franchise" is class A (not an update to a numbered line), launched June 2025 to May 2027, so it is in its first or second selling year during FY28 (June 2027 to May 2028). New versions of existing lines (class B) mostly replace the prior version and are assumed to add $0 net.

Inputs I can source:
- Count: SBD class A debuts for Nike plus Jordan, Jul 2025 to Dec 2026 (including listed): about 15 distinct keys (DERIVED); 18 is a middle case after adding RunRepeat-only running ones (Pegasus Premium, Vomero Plus, Vomero Premium, Structure Plus, ACG trail models); announced additions to May 2027 are Apex, Swooshfly, Hybrid RN and Hybrid Fly. Cases: 12, 18, 24 franchises.
- Revenue per franchise: no Nike disclosure. One datapoint: the Vomero 18 became a "$100 million dollar plus franchise" within about 90 days of launch (Nike earnings call, in repo `research_notes/07_new_products_detail.md`; annualised pace about $400M). Running grew "roughly a billion dollars" over five quarters (same note), which is 3.4% of FY26 footwear for all of running, new and existing. Cases: $50M, $120M, $300M per franchise (my assumptions, the $300M case needs several Vomero-class hits).

| Franchises | $50M each | $120M each | $300M each |
|---|---|---|---|
| 12 | 2.0% ($0.6B) | 4.9% ($1.4B) | 12.2% ($3.6B) |
| 18 | 3.0% ($0.9B) | 7.3% ($2.2B) | 18.3% ($5.4B) |
| 24 | 4.1% ($1.2B) | 9.8% ($2.9B) | 24.4% ($7.2B) |

Plausible range 3% to 10% of FY26 footwear, central about 7% ($2.2B). The $300M column would need the Vomero-18 outcome repeated across most new franchises and I treat it as outside the plausible range without evidence. Context: the classics cut from peak is more than $4B gross (13.5% of FY26 footwear; `franchise_oversupply.md`, which flags it as gross, unaudited and peak-based) and Jordan was $7,034M in FY26 with a mid-teens decline in Q1 FY27; new franchises at the central case replace about half of the classics gap and none of the Jordan decline. Sensitivity: each additional $100M franchise adds 0.34 points of FY26 footwear revenue.

Not in the data: pairs per release, sell-through, and cannibalisation of existing lines. Colorway counts say nothing about dollars: the 42 to 47% new share of Nike SBD rows would not translate to 42 to 47% of revenue, because SBD lists limited collector releases and Nike's volume sits in general-release styles (Pegasus, Vomero, AF1) that appear in the calendars as one row per colorway.

## 7. Alternatives ruled out or left open

| Alternative explanation for "newness rising" | Test | Result |
|---|---|---|
| SBD coverage change (editors list more Nike) | Brand mix of SBD rows by half-year | Real: non-Nike rows fell sharply (New Balance 41 in H2 2023 to 4 in H1 2026, Puma 22 in H2 2024 to 1, Reebok 23 in H2 2024 to 8 in H2 2026), so Nike share of SBD is an artifact. Within Nike the class mix is less exposed, but not immune. Left open: no second full census of Nike releases exists in the sources I could open |
| Retro "cut" is just SBD curation | Dunk rows on SBD versus SR article share versus management's cut | Ruled out for Dunk (two sources agree, plus Q1 FY27 "nearly 50%"); AF1 flat to up; Jordan SBD counts diverge from SR core counts in 2025 (SBD C class 80 versus SR core 113), so Jordan trend from SBD is unreliable |
| Kids' and women's rows distort mix | Compare all, adult, adult-ex-women's | Kids are 0.6% to 3.8% of rows, women's 1.2% to 13.8%; new share changes by 3 points at most (2024 H1: 31.2% all, 28.5% adult; 2026 H1: 38.6% versus 38.5%). Ruled out |
| Regional launches shift counts | China-first launches (Hybrid RN China 2026-09-24 versus global 2026-10-08, 14 days; Swooshfly China February versus global spring) | US dates move a few launches by up to a quarter; cannot move a half-year share. Swooshfly alone straddles FY27 and FY28 and is the main timing risk to the sizing |
| Misclassification | Unmatched rows; collab base | Class U under 3% of rows; collabs mostly retro-based (2025 H2: 40 of 58). Reported with and without |
| Duplicate listings across pages | Deduped by (name, style, date) | Done; 2 rows dropped for out-of-window dates |
| Calendar gaps | Monthly counts | Nike June 2023 and Jordan July 2025 absent on SBD; both flagged. Not fixed (no second source with dates) |
| Newness is only basketball | Segment split | Largely true on hype calendars (99% of B rows); running is not covered, so the calendar answer for running comes from RunRepeat and SR |

Open and not resolved: (i) whether new-franchise colorway counts translate into pairs or dollars; (ii) the forward-list bias; (iii) Hoka and On new-model counts beyond RunRepeat and Marathon Handbook (SBD and SR carry no Hoka, On is 120 SR pages).

## 8. Routes tried and results (so the next person does not repeat dead ends)

| Target | Route | Result |
|---|---|---|
| Sole Retriever release pages | Direct fetch (curl, WebFetch) | Blocked 403 (bot protection; not bypassed) |
| | Wayback Machine | Availability API: no snapshot; page fetch blocked by egress policy |
| | RSS (`/rss.xml`) | Worked, recent items only |
| | News and product sitemaps | Worked: 9,033 release-date slugs with lastmod; product lastmod not usable |
| | Playwright (used by the earlier Jordan agent) | Not installed in this session; not attempted |
| Sneaker News | Direct and WebFetch | 403 |
| | `/feed/` RSS | Worked, 7 items only |
| | Wayback | No snapshot returned |
| KicksOnFire | Direct and WebFetch | 403 |
| | Wayback | Snapshot exists (May 22 2026) but fetch blocked by egress policy; feed 403 |
| Hypebeast | Direct and WebFetch | HTTP 202 with empty body (client-side render) |
| | RSS | 202 empty |
| Sole Collector, Sole Supplier | Direct | Egress policy refused |
| Nike SNKRS | Page state (`__NEXT_DATA__`) | Worked: 20 upcoming products |
| | product_feed API | Worked partially: 1,050 of 6,564 threads (anchor capped near 1,450); filters for upcoming or footwear rejected (400) |
| Running new arrivals | Running Warehouse new arrivals | 200 but no release dates on page; not parsed |
| | Believe in the Run calendar | 404 on the URL I guessed; not found |
| | RunRepeat | Worked via review pages (release-date field on 102 of 632 only) |
| | Marathon Handbook calendar | Worked as fetch summary; 2025 only |
| Peer On and Hoka launch calendars | SBD, SR | Almost none; RunRepeat and Marathon Handbook only |
| Historical forward snapshots of calendars | Wayback, Google cache | Blocked or empty; this is the missing piece for the forward-bias test |
| Pair counts per release | Press, filings | None found (repo notes already record none for 2023 to 2026) |

What would settle the open items: dated forward snapshots of SBD, Nice Kicks or SR (the Internet Archive page content is blocked here; a session with unrestricted network could pull monthly snapshots from 2023 on); Circana or NPD unit data by franchise; Nike's franchise revenue disclosure at the Nov 16 to 17 Investor Day.

## Reproduce

`data/hunt/w8_launch_newness/scripts/`: `parse_sbd.py`, `classify2.py`, `build_w8.py`, `build_tables.py`, `build_misc.py`, `sr_slugs.py`, `sr_analysis.py`, `nk_crawl.py`, `rr_crawl2.py`, `build_rr.py`, `build_final_csv.py`, `pull_feed2.py`. Paths inside the scripts point to a scratch directory; raw parsed inputs are in `raw/`.
