# Root cause test: did the 2020 reorganization, layoffs, talent loss and executive churn cause Nike's decline?

Research date: 2026-10-13. Hypothesis under test: *The 2020 reorganization (the "consumer construct" of Men's, Women's and Kids replacing sport categories), the 2020 and later layoffs, the loss of institutional and product talent, and executive churn under an outsider CEO caused the decline.*

Source status labels:
- **OPENED**: I read the page or document myself in this session.
- **REPO**: a verified number already in `research_notes/04_financial_data_pack.md`, `data/nike_filing_facts.csv` or `data/people_events.csv`, with the filing and printed page given there.
- **REPO-NOTE**: taken from an earlier note in this repo, carrying the status that note recorded.
- **SNIPPET**: seen only in a search-result summary. A lead, not a fact.
- **10-K (footer page)**: quoted from the EDGAR text of the 10-K, which I opened in this session; the printed page is inferred from the "FORM 10-K nn" footer that follows the quote.

Earnings-call quotes come from Nike's official transcripts (investors.nike.com "webcast_transcript" PDFs), already downloaded and converted to text in this session's scratchpad. I searched all 25 calls from Q1 FY21 to Q1 FY27 in full text: **OPENED**.

Companion notes in this folder, whose estimates I reuse and do not re-derive: `innovation_drought.md`, `franchise_oversupply.md`, `dtc_wholesale.md`.

---

## 1. Bottom line

- **Verdict: contributing cause, operating mainly as a transmission mechanism of an upstream strategy choice. It is not the primary cause, and the "executive churn" and "outsider CEO" parts of the hypothesis mostly fail.**
- **What is real.** The 2020 reorganization happened, it was large, and both CEOs later reversed it:
  - Nike cut about 700 jobs at its Beaverton headquarters (WARN notice, Nov 2020) and booked $200M to $250M of termination costs (FY2020 10-K, REPO).
  - Headquarters headcount fell from about 12,800 (May 2020) to 11,700 (May 2021) and 11,200 (May 2022). It is about 10,600 today, 17% below the 2020 level (10-Ks, footer pages). Over the same years, total headcount *rose* to 83,700 (FY2023).
  - Insiders and analysts described a talent drain: at least 20 high-level executives left in H1 2021 (Business Insider via newsletter, SNIPPET-grade), and a former footwear designer predicted it "would show up on store shelves" in spring and summer 2023 (BI, OPENED).
  - Donahoe began undoing the construct in mid-2023 ("we brought the best of the category offense right back in", Mar 2024). Hill finished the job: "We lost our obsession with sport" (Dec 2024), then "Instead of a men's, women's and kids' construct..." (Jun 2025), and he "flipped the entire organization in early September" 2025.
- **What fails.** The tests that tell this hypothesis apart from the alternatives mostly fail.
  1. **Geography is inverse to leadership churn.** Greater China had the most stable leader in the company (Angela Dong, GM from April 2015 to March 2026) and the worst decline (-22.5% FY24 to FY26). North America had three GMs between 2020 and 2023 and the smallest decline (-4.1%).
  2. **The organization does not sort the brands.** Jordan Brand doubled under the same outsider CEO and reorganization ($3,609M FY20 to $7,270M FY25). Converse sat outside the Men's/Women's/Kids construct and still collapsed (-43.6% FY24 to FY26).
  3. **Senior churn follows the decline.** Of the 19 named senior exits in `people_events.csv`, 15 came in or after Sept 2024. The revenue decline began in Q1 FY25 (June to Aug 2024, -10%).
  4. **The org reversal has not stopped the decline.** The sport-based structure was rebuilt twice (completed per Donahoe by about May 2024; Sport Offense Sept 2025). Running recovered, yet total revenue was still -4% in Q1 FY27 and FY27 is guided down high-single digits.
  5. **The insider CEO has not stopped the decline either.** The stock is down 57% since Hill started ($81.60 on Oct 14, 2024 to $35.35 on Oct 12, 2026), more than the 20% fall over Donahoe's tenure. The product-lag caveat applies.
- **Where it bites.** The construct removed sport-category ownership, and with it the franchise-management and running expertise. That fed the two mechanisms already measured in the companion notes:
  - the running and newness gap (Brooks No. 1 in US performance running from Q1 2022; Nike's men's running head left to run Hoka in Feb 2024);
  - the loss of "the discipline of franchise management" (Hill's words, Dec 2024), which let Dunk, AF1 and AJ1 be over-supplied.
  It also thinned the wholesale sales organization, which Nike says it is now "rebuilding the scale, talent and capabilities" of (Mar 2025).
- **Upstream cause.** The organizational change was the implementation of the Consumer Direct Acceleration strategy (digital-first, data-led, fewer layers). An outsider CEO chose that strategy and the board approved it. The org change did not originate independently. The talent outflow was partly a consequence of the reorganization: insiders said it removed middle-management roles and advancement paths. Hill-era executive churn is a *response* to the decline.
- **Estimated contribution.** Roughly **10% to 20% of the $4,964M FY24 to FY26 revenue decline (about $0.5B to $1.0B)**, flowing through the innovation and franchise-management channels. This is an overlapping share of what the companion notes already attribute to those mechanisms, so it is **not additive**.
  - Upper bound: about 48%. The mechanism has little traction in Greater China and Converse, which account for $2,606M (52%) of the decline.
  - Lower bound: near 0% for C-suite churn as such.
- **Fixable by management: partly.** The structure has already been reversed, and where it was reversed with product behind it (Running), the business recovered within about 4 to 6 quarters. Lost tacit knowledge cannot be rehired on demand. The remaining decline (Sportswear, Jordan retro, China, Converse) is not an org-chart problem. Constant reorganizations add disruption risk: there was a structural reset every year from 2020 to 2026, Pace runs to FY2031, and the CFO and CAO turned over in Aug and Sept 2026.

---

## 2. Predictions and results

| # | Prediction if the hypothesis is true | Result | Held? |
|---|---|---|---|
| P1 | **Timing.** The decline appears 2 to 4 years after the mid-2020 reorg (one product cycle), and share loss should not predate 2020. | Nike said in Sept 2022 it was "now starting to see the product that reflects our shift two years ago to our new consumer construct." Analysts called the lineup "stale" in May 2023 (BI, OPENED). Lifestyle first declined in Q4 FY24, and revenue fell in FY25. **But** Euromonitor shows Nike lost more US athletic footwear share in 2016 to 2019 (40.5% to 34.1%, before Donahoe) than in 2019 to 2025 (REPO-NOTE, `dtc_wholesale.md`). Brooks took No. 1 in US performance running in Q1 2022, on product largely developed before the reorg. | **Partly.** The lag fits, but share erosion predates the reorg. |
| P2 | **Category.** Damage concentrates in the sport categories whose teams were dissolved (running, basketball, football, training), not in lifestyle. | Running share loss in 2022 to 2024 fits. But the FY25 to FY27 decline sits in Sportswear, Jordan retro and classics, while Performance grew (Q4 FY24 Performance "grew double digits"; FY26 Performance about $16B, +MSD) (REPO-NOTE, `innovation_drought.md`). | **No for the measured decline**; yes for the earlier running share loss. |
| P3 | **Reversal.** Rebuilding sport teams should restore the affected categories, and total revenue should follow. | Sport-based "field of play" teams were "completely" aligned by about May 2024 (Donahoe, Jun 27, 2024 call). The Sport Offense "flipped the entire organization in early September" 2025 (Hill, Sept 30, 2025 call). Running grew more than 20% for several quarters and added about $1B. Total revenue: FY26 +0.2%, Q1 FY27 -4%, FY27 guided -HSD (REPO). | **Partly.** The mechanism works locally but does not explain the total. |
| P4 | **Leadership continuity.** Segments with more leadership churn decline more. | Greater China: Angela Dong was GM from Apr 2015 to Mar 31, 2026 (Yicai; Nike release), and the segment fell 22.5% FY24 to FY26 (-26% c-n in Q1 FY27). EMEA: Grebert was VP/GM from 2020 to Feb 2026 (SNIPPET), -7.6%. North America: Hebert (2020 to Mar 2021), Mensah (2021 to May 2023), Uzzell (from May 2023), -4.1%, and NA grew in FY26. | **No (inverse).** |
| P5 | **Brand control group.** Brands outside the Men's/Women's/Kids construct should hold up better. | Converse (separate subsidiary, not part of the construct; Q4 FY21 call lists the construct as "Women's, Men's, Kids and Jordan") fell from $2,427M (FY23) to $1,174M (FY26). The FY26 10-K blames unit declines "in all territories". Jordan (folded into the construct as its own unit) doubled to FY25 under the same CEO. Converse did have CEO churn: Uzzell left in May 2023 and Carver left in Jul 2025. | **No for the construct.** Converse weakly fits the churn leg, but its decline is a Chuck Taylor fashion and promotion story (10-Ks). |
| P6 | **Churn precedes decline.** Senior turnover should cluster before the revenue turn. | `people_events.csv`: 4 named senior exits before Sept 2024 (Sprunk, Hill, Hebert, Campion) and 15 from Sept 2024 on. Revenue turned negative in Q1 FY25 (Jun to Aug 2024). Caveat: the csv tracks only the C-suite. BI reported about 20 "high-level" executives leaving in H1 2021 and about 20 director-level in late 2021 (via KYW newsletter, SNIPPET-grade). | **No for C-suite churn; partly for the director-level exodus of 2021.** |
| P7 | **Talent loss is measurable, and it flows to the winners.** | HQ headcount: 12,800 (FY20), 11,700 (FY21), 11,200 (FY22), 11,400 (FY23), 10,700 (FY24), 10,500 (FY25), 10,600 (FY26) (10-Ks, footer pages). About 700 HQ layoffs in the WARN notice. Ex-Nike leaders went to North Face, VF, Columbia, Lululemon and Allbirds (BI, Nov 2022, OPENED). Robin Green, Nike global VP of Men's Running and Fitness, became Hoka president in Feb 2024 (Retail Dive, OPENED). But Hoka had already grown from $571M (FY21) to $1,807M (FY24) (REPO-NOTE) before she moved. | **Yes, the drain is real.** But the flow to Hoka followed Hoka's success rather than causing it. |
| P8 | **Outsider-CEO effect.** If the outsider CEO was the cause, the insider's return should halt the decline within a product cycle. | Revenue under Donahoe: $37,403M (FY20) to $51,362M (FY24), +37% (REPO). Under Hill: still falling 24 months in. Stock: $102.16 on Jan 13, 2020, $81.60 on Oct 14, 2024, $35.35 on Oct 12, 2026 (`nke_daily_prices.csv`). | **No so far.** This is not decisive, because product takes 18 to 36 months to come through. |
| P9 | **Management attribution.** Both CEOs should blame the structure and the loss of talent. | Structure: yes. Hill (Dec 2024): "We lost our obsession with sport." Donahoe (Mar 2024): "we brought the best of the category offense right back in". Talent: no. Hill (Dec 2024): "One question I know you want to ask me is if we have the talent at NIKE? ... The short answer to both is yes... how much expertise we've added since I've been away in spaces like supply chain, product creation, technology, materials, sports science." Donahoe blamed remote work instead ("hard to ... develop a boldly disruptive shoe on Zoom", REPO-NOTE). | **Partly.** Structure yes, talent no. Self-serving on both sides. |

Score: 1 held (P7), 4 partly (P1, P3, P6, P9), 4 failed (P2, P4, P5, P8). The failed ones are the discriminating tests: geography, brand, the C-suite timing leg of P6, and the insider reversal. The ones that hold show that the mechanism exists and that the talent loss was real.

---

## 3. Evidence for

1. **The reorganization was large and deliberate.**
   - Nike leadership release of Jul 22, 2020 (via Retail Dive, Jul 23, 2020, REPO-NOTE OPENED): new leaders for "Men's, Women's and Kids" and "a simpler approach to product categories". Amy Montagne moved from VP/GM of global categories to Men's.
   - Donahoe (Q2 FY21 call, Dec 2020, OPENED): "realigning our organization to a new consumer construct."
   - FY2020 10-K (REPO): $200M to $250M employee termination costs.
2. **The layoffs hit HQ and experienced staff.**
   - Retail Dive, Nov 3, 2020 (OPENED): the updated Oregon WARN notice says "approximately 700 employees will be impacted ... at its Beaverton headquarters by Jan. 8"; the July notice said "at least" 500. Nike "will streamline its organization, including its Corporate Leadership Team."
   - BI, Kish, Jan 21, 2022 (OPENED): 700 of 12,800 HQ workers, "many of them with decades of experience." Unlike in earlier reorganizations, employees "weren't given the option to take early retirement or accept lower positions." Layoffs "seemed indiscriminate", "a spreadsheet exercise" (anonymous insiders). Donahoe (2018): "I grew up at Bain. For every 10 people we hired, we managed half out within two years."
3. **HQ shrank while the company grew.** WHQ occupancy fell from 12,800 to 11,200 (-12.5%) between FY20 and FY22. Over FY20 to FY23, worldwide headcount rose 11% (75,400 to 83,700) and operating overhead rose from $9,534M to $12,317M (REPO). Resources were reallocated away from the HQ product, brand and category functions toward stores, distribution and technology.
4. **Insiders and analysts called it a talent and knowledge drain, before the decline.**
   - BI, May 26, 2023 (OPENED): "A 2020 round of layoffs whittled away at the company's footwear ranks. Others left voluntarily, with one former Nike footwear designer last year telling Insider the talent drain would show up on store shelves this year. 'You'll definitely see it next year in spring and summer '23.'" Sam Poser (Williams Trading): "Nike has lost many senior people throughout the entire company with, now necessary, historical institutional knowledge of Nike ... Nike's game today is not as good as it was five years ago."
   - BI, Nov 7, 2022 (OPENED): Nike alumni now lead at Columbia, VF and The North Face, Lululemon and Allbirds. Insiders said Donahoe's reorganization "resulted in fewer middle-management roles and fewer opportunities for advancement."
   - BI, Jan 19, 2022 (OPENED): "Some current and former insiders are worried about an exodus of Nike veterans", and Donahoe was described as a "technocrat".
   - KYW newsletter, Jan 24, 2022 (OPENED; the underlying BI figure is SNIPPET-grade): at least 20 high-level executives left in H1 2021, plus about 20 director-level executives in the following three months.
   - KYW, Dec 10, 2021 (OPENED): designers Sergio Lozano (Air Max 95 and 98), Nate Jobe and Tom Rushbrook left. Chad Knight cited "the old guard's and MBA's lack of interest in ideas that aren't their own."
5. **An ex-insider's diagnosis.** Massimo Giunco, a former Nike senior brand director, essay of about Jul 31, 2024. Reproduced on sfin.ro, which does not name the author on the page (OPENED); attribution confirmed by FashionUnited (OPENED). He says Nike would "eliminate categories from the organization (brand, product development and sales)" and the "Product engine became gender led: women, men, and kids". He adds that "the decision was advised by McKinsey", "hundreds of colleagues were fired", Nike "lost a solid process and thousands of years of experience and expertise", and "they lost the competence, not only the focus". He dates the categories' return to "the reorg. announced by the CEO in December 2023" (renamed "Fields of Play"). This is opinion from an interested party.
6. **Running-specific talent loss.** Robin Green, global VP of Men's Running and Fitness after more than 17 years at Nike, was named Hoka president (Retail Dive, Feb 12, 2024, OPENED). Matt Powell said Nike "virtually shut down the innovation lab during COVID-19", while New Balance, Brooks and Asics "kept the innovation engine going" (SGB Media, Feb 16, 2024, OPENED).
7. **Both CEOs reversed it, which implies they judged it harmful.**
   - Donahoe (Mar 21, 2024): "we brought the best of the category offense right back in." He started "9 months ago", that is, about June 2023.
   - Donahoe (Jun 27, 2024): "over the last 90 days, we completed completely aligning our organization along the lines of sport."
   - Hill (Dec 19, 2024): "We lost our obsession with sport"; "We will return to the discipline of franchise management."
   - Hill (Jun 26, 2025): "Instead of a men's, women's and kids' construct, NIKE, Jordan a[nd Converse]" organized "by sport."
   - Friend (Mar 20, 2025): "rebuilding the scale, talent and capabilities of our sales organization."
8. **Where the structure was reversed with product behind it, the business came back.** Running grew more than 20% for several quarters, Vomero 18 became a "$100 million-plus franchise", and Nike "nearly tripled" its max-cushion share (REPO-NOTE, `innovation_drought.md`). This is consistent with sport-category ownership mattering.
9. **The literature fits the outsider over-change story.** Zhang and Rajagopalan (2010, SMJ) find an inverted-U between strategic change and performance, steeper for outsider CEOs (REPO-NOTE, `academic_literature.md`).

## 4. Evidence against (or that it is not the main cause)

1. **Geography is inverse to leadership churn** (P4).
   - Greater China had 11 years of leadership continuity under Angela Dong (Yicai, Jan 21, 2026, OPENED: "2015年4月，董炜升任耐克全球副总裁及大中华区总经理"; Nike release, Jan 20, 2026, OPENED). It still had the largest decline: $7,545M to $5,847M (-22.5%), and -26% c-n in Q1 FY27 (REPO).
   - The FY2026 10-K blames "declining store traffic, elevated promotional activity and higher levels of inventory" (REPO-NOTE).
   - North America, with the most GM turnover, had the smallest decline.
2. **Brands do not sort by the construct** (P5).
   - Jordan Brand ran inside the same company, under the same outsider CEO and through the same layoffs, and doubled from FY20 to FY25 (REPO; restatement caveat).
   - Converse, outside the construct, fell 43.6%. The 10-Ks attribute this to unit declines and DTC discounting: FY24 -15% c-n, FY25 -18%, FY26 -32% (10-Ks, OPENED).
3. **Senior churn is mostly a response, not a cause** (P6). 15 of 19 named senior exits came after the decline began. Most were Hill's deliberate removals: O'Neill, Dogan and Williams roles eliminated; Heaf's role eliminated (REPO). The churn the hypothesis would need came too late to cause the FY25 drop.
4. **Share erosion predates the reorg.** US share fell from 40.5% (2016) to 34.1% (2019) (Euromonitor, REPO-NOTE), the adidas Boost and Yeezy era. Hoka's and On's rise began before 2020.
5. **Performance grew during the decline** (P2). The categories the construct dissolved were growing by FY24 to FY26. The hole is in Sportswear, Jordan retro, China and Converse.
6. **The revenue decline came after the org had already been reversed.** Sport teams were "completely" realigned by about May 2024 (Donahoe). The decline then ran from June 2024 to at least Aug 2026, and Hill flipped the org again in Sept 2025.
7. **Under the reorganized structure, revenue first grew strongly.** FY21 +19%, FY22 +5%, FY23 +10% (REPO). The "spring and summer '23" designer prediction showed up as staleness but not as revenue loss until Nike deliberately cut classics in FY25.
8. **The returning insider says the talent is there.** Hill (Dec 2024): "expertise we've added since I've been away in ... product creation, technology, materials, sports science ... Our talent is world-class." This is self-interested, but it comes from the person with the strongest motive to blame his predecessor's org.
9. **The 2023 to 2024 talent complaints centre on digital and tech teams.** The leaked 2022 tech survey ranked tech staff below the rest of the company on 48 of 51 items (BI via search, SNIPPET). The Nov 2023 cuts came "across talent and product management teams" in the digital product division (KYW Vol. 321, OPENED, citing Footwear News). These are not the footwear-creation teams.

## 5. Independent cause or symptom?

**Mostly a symptom and transmission channel of the Consumer Direct Acceleration strategy, with one partly independent strand.**
- The Men's/Women's/Kids construct, the HQ layoffs and the flatter structure were the organizational implementation of CDA: lead with digital, segment by consumer, cut layers. Donahoe announced them together (June to July 2020). The consumer construct existed to feed a digital, data-led merchandising model. That model also over-fed the app with classics (`franchise_oversupply.md`) and over-built NIKE Direct (`dtc_wholesale.md`).
- The talent outflow was partly a consequence of the reorg (fewer middle-management roles, layoffs without early-retirement options) and partly the normal poaching of a dominant firm's alumni.
- Hill-era executive churn is a response to the decline, not a cause.
- The partly independent strand is the loss of tacit category knowledge (franchise management, running and specialty relationships). Even a good strategy executed through that structure would probably have weakened these. This strand is what the Running reversal shows: rebuild sport teams plus product, and share returns.
- Further upstream: the board's 2019 choice of an outsider CEO with a Bain, eBay and ServiceNow background, and Parker as executive chair (REPO-NOTE `01_ceo_and_board.md`).

## 6. Quantification (my arithmetic, labelled)

- FY24 to FY26 revenue change: $51,362M to $46,398M = **-$4,964M** (REPO).
- By segment (REPO; FY24 10-K p. 38, FY26 10-K p. 32 and 36):

  | Segment | Change ($M) | Change (%) |
  |---|---|---|
  | North America | -885 | -4.1% |
  | EMEA | -1,035 | -7.6% |
  | Greater China | -1,698 | -22.5% |
  | APLA | -486 | -7.2% |
  | Converse | -908 | -43.6% |
  | Global Brand Divisions and Corporate | +48 | n/a |

- Greater China plus Converse = **$2,606M, 52.5%** of the decline. In those two units the org and talent hypothesis has little purchase: leadership was stable in China, and Converse sat outside the construct.
- The rest of NIKE Brand (NA, EMEA, APLA) = -$2,406M. Inside it, Performance grew, so the decline there is Sportswear, Jordan and classics. Companion notes attribute that to the oversupply ($2B to $3B gross) and the lifestyle-newness gap ($0.5B to $1.2B).
- The org and talent mechanism is one of the upstream reasons for both of those. COVID remote work, COVID scarcity misread as lasting demand, and the digital model are the others. If I give it about a third to a half of the newness gap and a fifth to a third of the excess oversupply, it comes to roughly **$0.5B to $1.0B, or about 10% to 20%** of the net decline. That is a judgment call, not a measurement, and it overlaps the companion estimates rather than adding to them.
- C-suite churn and "outsider CEO" as such: roughly **0%** of the measured FY25 to FY26 decline, because churn followed it and the insider's return has not reversed it. Forward risk is non-zero: the finance function turned over in Aug to Sept 2026, and Pace is the third restructuring since FY24.

## 7. Fixability

**Partly.**
- The structure is already reversed: sport teams in 2024 and the Sport Offense from Sept 2025. Where the reversal came with product, it worked within about 4 to 6 quarters (Running).
- The sales organization is being rebuilt (Friend, Mar 2025), and NA wholesale reached a record $11,958M in FY26 (REPO-NOTE).
- Not fixable quickly:
  - Tacit knowledge that left between 2020 and 2024.
  - The remaining decline drivers (China, Sportswear fashion cycle, Converse), which no org chart addresses.
  - Reorganization fatigue: a structural reset every year from 2020 to 2026, plus Pace layoffs from 2027 and a geography merge in FY28. These are a new self-inflicted risk.

## 8. Timeline of organizational change (for reference)

| Date | Event | Source |
|---|---|---|
| Jan 13, 2020 | Donahoe (outsider; Bain, eBay, ServiceNow) becomes CEO | REPO; BI Jan 19, 2022 (OPENED) |
| Feb 18, 2020 | Sprunk (COO) and Hill (President, Consumer and Marketplace) retirements announced | REPO |
| Jun to Jul 2020 | CDA announced; consumer construct of Men's, Women's, Kids; Jul 23 WARN notice for at least 500 HQ jobs | Retail Dive Jul 23, 2020 (REPO-NOTE OPENED); WWeek Jul 30, 2020 (SNIPPET) |
| Nov 2020 to Jan 8, 2021 | WARN notice updated to about 700 HQ jobs | Retail Dive Nov 3, 2020 (OPENED) |
| H1 2021 | At least 20 high-level executive exits reported | BI via KYW Jan 24, 2022 (SNIPPET-grade) |
| Mar 1, 2021 | NA GM Hebert resigns | REPO |
| Sept 2022 | Nike: product from "our new consumer construct" is now reaching market | Q1 FY23 call (OPENED) |
| May 24, 2023 | O'Neill and Williams co-presidents; Spillane retires; Uzzell from Converse CEO to NA GM; Mensah to Jordan | Retail Dive May 25, 2023 (OPENED) |
| about Jun 2023 to May 2024 | Donahoe brings "category offense" back; sport "field of play" teams completed | Q3 FY24 and Q4 FY24 calls (OPENED) |
| Dec 2023 to Feb 2024 | $2B savings plan; "more than 1,500" layoffs; Robin Green to Hoka | REPO; Retail Dive Feb 12, 2024 (OPENED) |
| Jun to Aug 2024 (Q1 FY25) | Revenue -10%: decline begins | REPO |
| Oct 14, 2024 | Hill (insider) becomes CEO | REPO |
| 2025 | O'Neill, Heaf, Wilkins, Hoke, Carver, Dogan, Williams exit; Sport Offense announced (Jun 2025) and implemented (early Sept 2025) | REPO; Q4 FY25 and Q1 FY26 calls (OPENED) |
| 2026 | Grebert, Dong, Bignell, Friend, Nielsen exit; Mar 2026 severance plan; Apr 2026 about 1,400 tech cuts; Oct 1, 2026 Pace with about $1.0B charges and 3 geographies from FY28 | REPO |

## 9. Gaps and what would settle it

- No Nike attrition rate by function or year. Revelio Labs pages are paywalled (SNIPPET); the 10-K gives only HQ occupancy.
- The original BI H1 2021 "at least 20 executives" article was not opened; the figure is via the newsletter.
- The Giunco LinkedIn original was not reachable. I used the sfin.ro reproduction and FashionUnited's attribution.
- Nike does not disclose R&D or product-creation headcount, so a direct "capacity cut" test is impossible.
- A cleaner test would compare Running share by quarter against the dates of category-team rebuilds (2023 to 2025). Circana quarterly data is not public.

---

## 10. Sources

| Source | Date | Status |
|---|---|---|
| Nike FY2019 to FY2026 10-Ks, Properties section (HQ occupancy 12,600; 12,800; 11,700; 11,200; 11,400; 10,700; 10,500; 10,600), footer pages 19, 22, 24, 24, 24, 26, 25, 25 | Jul 2019 to Jul 2026 | OPENED (EDGAR text) |
| Nike FY2024, FY2025, FY2026 10-Ks, Converse revenue explanations | Jul 2024 to Jul 2026 | OPENED |
| `04_financial_data_pack.md` (revenue, segments, Jordan, employees, opex, FY2020 termination costs) | Oct 12, 2026 | REPO |
| `data/people_events.csv`, `data/nke_daily_prices.csv` | Oct 12, 2026 | REPO |
| Nike earnings call transcripts Q1 FY21 to Q1 FY27 (quotes dated Dec 2020, Mar 2021, Jun 2021, Sept 2022, Dec 21, 2023, Mar 21, 2024, Jun 27, 2024, Dec 19, 2024, Mar 20, 2025, Jun 26, 2025, Sept 30, 2025, Oct 1, 2026) | 2020 to 2026 | OPENED |
| Retail Dive, "Nike increases layoffs at headquarters to 700" (Cara Salpini), https://www.retaildive.com/news/nike-increases-layoffs-at-headquarters-to-700/588298/ | Nov 3, 2020 | OPENED |
| Willamette Week, "Nike will lay off 500 people at its Beaverton world headquarters" | Jul 30, 2020 | SNIPPET |
| Business Insider (Kish), "Nike layoffs, John Donahoe, 2020 reorganization", https://www.businessinsider.com/nike-layoffs-john-donahoe-2020-reorganization-2022-1 | Jan 21, 2022 | OPENED |
| Business Insider (Kish), "Nike CEO John Donahoe 2 years, stock soaring, talent drain", https://www.businessinsider.com/nike-ceo-john-donahoe-2-years-stock-soaring-talent-drain-2022-1 | Jan 19, 2022 | OPENED (first part of article) |
| Business Insider (Kish), "Nike alums leading top sportswear brands", https://www.businessinsider.com/nike-alums-leading-top-sportswear-brands-like-lululemon-hoka-columbia-2022-11 | Nov 7, 2022 | OPENED |
| Business Insider (Santana and Kish), "Nike shuffles executives as unwanted Air Maxes and Air Jordans pile up", https://www.businessinsider.com/nike-shuffles-executives-unwanted-air-maxes-air-jordans-pile-up-2023-5 | May 26, 2023 | OPENED |
| Business Insider, leaked Nike tech employee survey (48 of 51 categories) | May to Jun 2022 | SNIPPET |
| The Kicks You Wear Vol. 198 (Mike D. Sykes II), https://kyw.substack.com/p/the-kicks-you-wear-vol-198-nikes | Jan 24, 2022 | OPENED |
| The Kicks You Wear Vol. 192, https://kyw.substack.com/p/the-kicks-you-wear-vol-192-addition | Dec 10, 2021 | OPENED |
| The Kicks You Wear Vol. 321, https://kyw.substack.com/p/the-kicks-you-wear-vol-321-the-cost | Nov 17, 2023 | OPENED |
| sfin.ro, "Nike: An Epic Saga of Value Destruction" (reproduction of the Giunco essay; author not named on page), https://www.sfin.ro/nike-an-epic-saga-of-value-destruction/ | Jul 31, 2024 | OPENED |
| FashionUnited, "Just Can't Do It: Nike's ongoing strategy struggles", https://fashionunited.com/executive/report/just-cant-do-it-nikes-ongoing-strategy-struggles/2024080261226 | about Aug 2, 2024 | OPENED |
| Retail Dive, "Hoka names Nike executive Robin Green president" (Salpini), https://www.retaildive.com/news/hoka-names-nike-executive-robin-green-president/707241/ | Feb 12, 2024 | OPENED |
| SGB Media, "EXEC: Nike Inc. set to cut approximately 1,600 jobs", https://sgbonline.com/?p=306045 | Feb 16, 2024 | OPENED |
| Retail Dive, "Nike executive shuffle, Jordan president" (Salpini), https://www.retaildive.com/news/nike-executive-shuffle-jordan-president/651275/ | May 25, 2023 | OPENED |
| Nike release, "NIKE, Inc. announces new geography leadership appointments" (Spanish edition), https://about.nike.com/es-ES/newsroom/releases/nike-inc-announces-new-geography-leadership-appointments | Jan 20, 2026 | OPENED |
| Yicai (第一财经), Angela Dong appointment history, https://www.yicai.com/news/103017535.html | Jan 21, 2026 | OPENED |
| Textilwirtschaft / InsideRetail, Grebert VP/GM EMEA since 2020 | Jan 2026 | SNIPPET |
| Revelio Labs Nike headcount pages | 2026 | SNIPPET |
| `innovation_drought.md`, `franchise_oversupply.md`, `dtc_wholesale.md` (this folder) | Oct 13, 2026 | REPO-NOTE |
| `03_departures_and_layoffs.md`, `01_ceo_and_board.md`, `Nike decline execution vs structural/academic_literature.md` | Oct 12 to 13, 2026 | REPO-NOTE |

---

## Challenge: REFUTER

Research date: 2026-10-13. Lens: try to disprove the hypothesis, check the cited numbers against primary filings, and find tests the investigation missed. Note on method: the shared web-search budget for this run was already used up when this challenge started, so no new news searches were possible. All new evidence below comes from SEC EDGAR filings fetched directly with curl (Nike CIK 320187, VF Corp CIK 103379) and from the repo's own data files. Arithmetic is mine and labelled.

### A. Number checks (all held)

- Segment changes FY24 to FY26: NA 21,396 to 20,511 (-885, -4.1%), EMEA 13,607 to 12,572 (-1,035), Greater China 7,545 to 5,847 (-1,698, -22.5%), APLA 6,729 to 6,243 (-486), Converse 2,082 to 1,174 (-908, -43.6%). Total -4,964. All match `data/nike_filing_facts.csv` (FY24 10-K p. 38; FY26 10-K pp. 32, 36). REPO.
- HQ occupancy 12,800 (May 2020) and 11,700 (May 2021): confirmed in FY2020 and FY2021 10-K Properties text ("occupied by approximately 12,800 employees" / "11,700 employees"). OPENED (EDGAR, Oct 13, 2026). FY2022: 11,200, OPENED.
- Senior exits: `people_events.csv` has 19 rows; 4 before Sept 2024 (Sprunk, Hill, Hebert, Campion), 15 from Sept 2024 on. Confirmed. REPO.
- One citation is wrong in a way that matters (see D3): "Jordan doubled, $3,609M FY20 to $7,270M FY25" splices two different Jordan series.

### B. New evidence that cuts against the hypothesis

**B1. The HQ "hollowing out" is a reversion to the 2017 baseline, not a loss below it.** Nike 10-K Properties sections (OPENED, EDGAR): HQ occupied by about **10,800** employees (FY2017 10-K, filed Jul 20, 2017), **11,200** (FY2018), 12,600 (FY2019), 12,800 (FY2020), then 11,700, 11,200 and **10,600** today. The 2020 to 2022 cut removed the 2,000-person build-up of FY2017 to FY2020 (the Parker-era Consumer Direct Offense years). Today's HQ is only about 2% below FY2017 (my arithmetic: 10,600 vs 10,800), when the NIKE Brand was earning $32,233M and growing (REPO). The investigator's "-17%" uses the all-time peak as the base. HQ occupancy cannot show a capacity hole relative to the period when Nike's product engine is regarded as healthy. The 700 WARN-notice layoffs were 5.5% of the 12,800 HQ base (my arithmetic).

**B2. Running weakness predates the 2020 construct.** NIKE Brand wholesale-equivalent revenue by category, FY2019 10-K (one consistent series, OPENED): Running **$4,576M (FY17), $4,496M (FY18), $4,488M (FY19)**, flat to down for two years (-2% reported, -4% c-n in FY18), while Sportswear went $9,272M to $10,720M to $12,442M (+34% over two years). Running then fell to $3,830M in FY20 (FY20 10-K, COVID year) and rose only 4% to $3,987M in FY21 (FY21 10-K). The running drift is visible three years before the Men's/Women's/Kids construct was announced (June 2020), under an insider CEO with intact category teams. That undercuts the "construct dissolved running expertise, so running share fell" chain, which is the hypothesis's strongest category leg. It fits the investigator's own Euromonitor point that US share loss was larger in 2016 to 2019.

**B3. A reorganization plus job cuts under the insider CEO in 2017 was followed by growth.** FY2017 and FY2018 10-Ks (OPENED): "In June 2017, we announced the Consumer Direct Offense, a new company alignment"; FY2018 overhead included "one-time wage-related costs associated with the Consumer Direct Offense organizational realignment". Revenue then grew in FY18 and FY19. Nike was also already reporting Men's, Women's and Young Athletes' revenue in FY2015 to FY2017 (FY2017 10-K, OPENED). Large reorganizations with cuts are routine at Nike; the 2020 one is not unique in kind, and the earlier one did not precede a decline.

**B4. The channel split points away from talent and toward a strategy choice.** FY24 to FY26 (REPO, FY24 10-K p. 84, FY26 10-K p. 83): total DTC including Converse $22,351M to $18,197M (**-$4,154M, about 84% of the decline**); total wholesale $28,856M to $28,058M (**-$798M, about 16%**) (my arithmetic). NIKE Brand Digital fell from $12.1B to $8.6B (REPO). The investigator's sales-organization leg (Friend: "rebuilding the scale, talent and capabilities of our sales organization") predicts weakness in wholesale. Wholesale was the channel that held, and NA wholesale hit a record in FY26 (REPO-NOTE). The decline is concentrated in the digital channel that Nike deliberately cut back (fewer promotions, fewer classics in the app). That is a marketplace-strategy result, not a product-talent result.

**B5. Converse has an outside control with a different organization: Vans.** VF Corp 10-Ks (OPENED, EDGAR): "Vans brand global revenues decreased 12% in Fiscal 2023", "decreased 24% in Fiscal 2024", "decreased 16% in Fiscal 2025", "decreased 9% in Fiscal 2026" (VF fiscal years end around late March or early April; 10-Ks filed May 25, 2023; May 23, 2024; May 22, 2025; May 20, 2026). Compounded, Vans fell about **49%** (my arithmetic: 0.88 x 0.76 x 0.84 x 0.91 = 0.51). Converse fell **52%** from FY23 to FY26 ($2,427M to $1,174M, REPO). The other big canvas and vulcanized-sole brand, run by a different company with a different structure, shrank by the same amount over the same years. Converse's 18% share of the decline is a category cycle. Caveat against my own point: VF also had heavy executive churn (CEO change in 2022 to 2023), so this test refutes the Nike-construct leg for Converse, not churn in general.

### C. Evidence I checked that does not refute it

- Running did recover after sport teams were rebuilt (REPO-NOTE `innovation_drought.md`). That is local support for the category-ownership mechanism, although B2 shows the original weakness predated the construct.
- The Dec 2023 to Feb 2024 layoffs ("more than 1,500") came just before the revenue turn. But they were announced on Dec 21, 2023 alongside lowered guidance and a $2B cost plan (REPO), so they are a response to softening demand, not an independent shock.

### D. Problems with the investigator's case

1. **Its supporting quantitative evidence is base-period dependent** (B1). Without the HQ decline, the "talent drain" rests on anonymous insider quotes, a newsletter's second-hand executive count (SNIPPET-grade), one named running VP who left in Feb 2024, and an interested ex-employee's essay. None measures product-creation capacity.
2. **The mechanism the estimate relies on is borrowed, not shown.** The $0.5B to $1.0B figure is "a third to a half" of the newness gap and "a fifth to a third" of oversupply. Those fractions are not derived from any test in the note. The oversupply of Dunk, AF1 and AJ1 was a merchandising and digital-allocation decision (CDA), and B4 shows the decline sits in exactly that channel. Attributing it to lost "franchise-management" talent rather than to the strategy that directed the volume is not supported by a discriminating test.
3. **The Jordan figure mixes series.** $3,609M (FY20, FY20 10-K p. 31) and $7,270M (FY25, FY25 10-K p. 33) are on different bases. The recast FY24 Jordan figure is $8,701M (Q4 FY25 release, REPO), so on a comparable basis Jordan fell from $8,701M to $7,034M FY24 to FY26 (**-$1,667M, -19%**, my arithmetic). The correct reading: Jordan grew strongly from FY20 to FY24 under the construct (where the hypothesis predicts damage), then fell with retro oversupply. The conclusion against the hypothesis stands, but the "doubled to FY25" wording should be corrected.
4. **Every discriminating test still fails**: geography (China stable leadership, worst decline), brand (Converse matched by Vans), timing (churn after the turn; running drift before the construct), channel (decline in DTC, not wholesale), and reversal (sport structure restored by May 2024, decline started Jun 2024).

### E. Revised verdict

The hypothesis as stated ("caused the decline") does not survive. The organization and talent strand is at most a **minor** contributor. I would cut the estimate to roughly 0% to 10% of the FY24 to FY26 decline (about $0 to $0.5B), overlapping the oversupply and newness estimates, and treat even that as unmeasured. The 2020 construct and layoffs are better read as one implementation detail of the Consumer Direct Acceleration strategy, whose measurable damage shows up in the DTC channel and in classics oversupply, not in lost capability. Running's weakness began before 2020; the HQ shrinkage merely undid a 2017 to 2020 build-up; and the two largest non-strategy pieces (Greater China and Converse) are explained by China-specific factors and a canvas-category cycle that hit Vans equally.

### F. Sources for this challenge

| Source | Date | Status |
|---|---|---|
| Nike FY2017 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018717000090/nke-5312017x10k.htm (HQ 10,800; CDO June 2017; Men's/Women's/Young Athletes revenue) | Jul 20, 2017 | OPENED |
| Nike FY2018 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018718000142/nke-5312018x10k.htm (HQ 11,200; CDO realignment wage costs) | Jul 25, 2018 | OPENED |
| Nike FY2019 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018719000051/nke-531201910k.htm (Running and Sportswear FY17 to FY19) | Jul 23, 2019 | OPENED |
| Nike FY2020 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018720000047/nke-531202010k.htm (HQ 12,800; construct text; Running FY20) | Jul 24, 2020 | OPENED |
| Nike FY2021 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018721000028/nke-20210531.htm (HQ 11,700; Running FY21) | Jul 20, 2021 | OPENED |
| Nike FY2022 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018722000038/nke-20220531.htm (HQ 11,200; no category table) | Jul 21, 2022 | OPENED |
| VF Corp 10-Ks FY2023 to FY2026 (Vans global revenue changes), e.g. https://www.sec.gov/Archives/edgar/data/103379/000010337926000030/vfc-20260328.htm | May 2023 to May 2026 | OPENED |
| `data/nike_filing_facts.csv` (segments, channel totals, Jordan recast), `data/people_events.csv` | Oct 12, 2026 | REPO |

---

## Challenge: ROOT-CAUSE

Challenger research date: 2026-10-13. Lens: assume the organizational damage is real and ask whether it is a downstream effect of a different, earlier cause. Method note: the shared WebSearch budget for this run was exhausted before this challenge began, so all new evidence below comes from primary SEC filings fetched directly from EDGAR (full-text search plus documents), which I OPENED and parsed in this session. Growth rates and shares marked "my arithmetic" are computed from the reported dollar values.

### C1. Verdict

**The hypothesis does not survive as an independent cause. It is a symptom (an implementation layer) of a product-mix and channel strategy that Nike's insider leadership adopted in 2017, three years before the 2020 reorganization and before the outsider CEO arrived.** The original note already calls the org change a "transmission mechanism" of Consumer Direct Acceleration (CDA) and points upstream to the board's choice of an outsider CEO. The filings show that upstream point is placed too late and on the wrong person. Every mechanism the note credits to the 2020 construct (running weakness, a lifestyle-heavy mix, "power franchise" scaling of classics, headquarters capacity) was already visible under Mark Parker's category-based organization in FY2017 to FY2019. Revised verdict: **symptom of another cause.** Incremental share of the $4,964M FY24 to FY26 decline that I would assign to the org and talent change itself, net of the pre-existing trend: **roughly 0% to 5% (about $0 to $0.25B)**, down from the original 10% to 20%.

### C2. New evidence the original note missed

1. **Nike itself calls CDA a phase of Parker's 2017 strategy, not a new one.** FY2021 10-K (filed 2021-07-20, p. 28, OPENED): "Since fiscal 2018, through the Consumer Direct Offense and our Triple Double strategy, we have focused on doubling the impact of innovation, increasing our speed and agility to market and growing our direct connections with consumers. In June 2020, we announced a new digitally empowered phase of the Consumer Direct Offense strategy: Consumer Direct Acceleration." The Consumer Direct Offense was announced June 15, 2017 by Parker (insider CEO), who then stayed on as Executive Chairman through the whole Donahoe era and is still Executive Chairman today (REPO-NOTE, `01_ceo_and_board.md`). The "outsider CEO" framing misattributes the strategy.

2. **The "edit and scale power franchises" logic that the note blames on lost franchise discipline was Parker-era policy.** Q4 FY2017 call (8-K Ex. 99.1, filed 2017-07-05, OPENED): "We have to be better editors"; the reorganization "put categories, designed product and merchandising all together as a full unit"; the CDO cut about 25% of styles (REPO-NOTE, `timeline_forensics.md`). Q3 FY2018 call (8-K Ex. 99.1, filed 2018-03-27, OPENED): Nike was "editing our assortments to offer more compelling choice of our power franchises." EDGAR full-text search (OPENED) finds "Edit to Amplify" in Nike filings from 2011 to March 2018. The narrowing toward a few scaled franchises predates the Men's/Women's/Kids construct.

3. **The same franchise over-distribution failure already happened under the category organization, intact talent and an insider CEO.** Q3 FY2018 call (OPENED): North America contracted on "a deliberate tightening in the distribution of styles within the Jordan Brand" and "we believe Jordan inventories are now clean." So the failure mode the note attributes to the construct (loss of "the discipline of franchise management") occurred in 2017 with the sport-category teams and the pre-layoff workforce in place. It is a recurring feature of Nike's demand-pull, sell-the-heat model, not a product of the 2020 org chart.

4. **Running was already stagnating under the category structure, before the 2020 construct and before the layoffs.** Nike's own NIKE Brand wholesale-equivalent revenue by category (each pair on the same basis, from one filing):

   | Period (same restated basis) | Running | Sportswear | Total NIKE Brand WE | Source |
   |---|---|---|---|---|
   | FY17 vs FY19 | $4,576M to $4,488M (-1.9%) | $9,272M to $12,442M (+34.2%) | $28,694M to $32,550M (+13.4%) | FY2019 10-K p. 27 (OPENED) |
   | FY18 vs FY19 | $4,496M to $4,488M (0%, +4% c-n) | $10,720M to $12,442M (+16%) | +7% | FY2019 10-K p. 27 (OPENED) |
   | FY19 vs FY21 | $4,488M to $3,987M (-11.2%) | $12,442M to $15,053M (+21.0%) | $32,550M to $35,770M (+9.9%) | FY2020 10-K p. 31, FY2021 10-K p. 32 (OPENED) |

   Running share of NIKE Brand wholesale-equivalent revenue (my arithmetic): 15.9% (FY17), 13.8% (FY19), 11.1% (FY21). Sportswear share: 32.3%, 38.2%, 42.1%. The running share fell about 1.05 points a year before the construct (FY17 to FY19) and about 1.35 points a year in FY19 to FY21 (which also contains COVID). If the pre-2020 trend is the counterfactual, the construct's incremental running loss by FY21 is about 0.6 points of a $35.8B base, roughly $0.2B (my arithmetic, a rough bound). This fits `dtc_wholesale.md`, which shows Hoka growing 40% to 50% a year from FY2017. Nike stopped disclosing sport categories after FY2021 (FY2022 10-K p. 32 shows only Men's, Women's, Kids' and Jordan), so the test cannot be extended.

5. **Category consolidation also started under Parker.** FY2017 10-K Item 1 (OPENED): "nine key categories: Running, NIKE Basketball, the Jordan Brand, Football (Soccer), Men's Training, Women's Training, Action Sports, Sportswear ... and Golf." FY2018 10-K Item 1 (filed 2018-07-25, OPENED): "six key categories." The phrase "category offense" appears in Nike filings every year from 2008 and last appears in the Q2 FY2018 call transcript filed 2017-12-27 (EDGAR full-text search, OPENED). The March 15, 2018 restructuring (8-K Ex. 99.1, OPENED) split the company into "Consumer and Marketplace" (Elliott Hill) and "Categories, Design, Product and Merchandising" (Michael Spillane) after Nike Brand President Trevor Edwards' 25-year tenure ended. Nike was also already reporting Men's, Women's and Young Athletes' revenue in the FY2016 10-K (OPENED). The consumer-segment lens and the shrinking of the category layer were both under way before 2020.

6. **The headquarters "talent drain" is the reversal of a 2018 to 2020 build-up, not a cut below the level that produced Nike's last innovation wave.** World headquarters occupancy (10-K Item 2, OPENED): about 10,700 (FY16), 10,800 (FY17), 11,200 (FY18), 12,600 (FY19, p. 19), 12,800 (FY20), then 11,700, 11,200, 11,400, 10,700, 10,500, 10,600 (FY21 to FY26, per the original note). Today's 10,600 equals the FY2016 to FY2017 level, the years that produced VaporMax, React and ZoomX. The 2020 layoffs removed roughly the 2,000 people added in FY18 to FY20, the CDO digital build-out years (the composition of those hires is not disclosed; this is an inference). A 17% cut measured from the 2020 peak overstates the loss of product capacity.

7. **The construct missed its own stated goals, and the growth it did see came from the one unit it left intact.** The FY2020 10-K (p. 27, OPENED) said the construct would mean "reinvesting in our Women's and Kids' businesses." Wholesale-equivalent revenue FY21 to FY24 (FY2022 10-K p. 32; FY2024 10-K p. 34, OPENED; my arithmetic): Women's $8,225M to $8,586M (+4.4%), Kids' $4,882M to $5,111M (+4.7%), Men's $18,391M to $20,868M (+13.5%), Jordan $4,780M to $6,988M (+46.2%), total $35,770M to $40,767M (+14.0%). That shows the construct was ineffective. It does not show it caused the FY25 to FY26 decline, which started after the construct was already being reversed.

8. **Greater China repeats the global pattern with stable leadership.** `china.md` (REPO-NOTE) records that Nike China Running grew for six straight quarters to Q1 FY27 while Sportswear and Jordan "declined double digits," and that the Nike-vs-adidas China gap is about -20 points. The same split (performance up, lifestyle classics down) appears in a segment with 11 years of leadership continuity. A common upstream cause (lifestyle and classics over-exposure plus channel saturation) fits both China and North America. Org churn fits neither.

### C3. The upstream chain that fits the same data better

1. **2015 to 2017 (Parker, insider):** demand shifts to "the look of sport." Sportswear becomes Nike's biggest growth engine ($8.6B in FY17, "nearly $8.6 billion business," Q4 FY17 call), North American wholesale is promotional, and Running stalls while Hoka grows 40% to 50% a year.
2. **June 2017 (Parker):** Consumer Direct Offense. Fewer styles, scale power franchises, direct channel first, account cuts. **March 2018:** the category leadership layer is consolidated (nine to six categories; the Nike Brand President exits; Categories and Consumer/Marketplace split).
3. **2020 (Donahoe, with Parker as Executive Chairman):** COVID scarcity makes the classics-through-Digital model look unbeatable. CDA, the Men's/Women's/Kids construct and the HQ cuts are the next phase of the same strategy (Nike's own wording).
4. **2021 to 2023:** the model over-feeds classics (`franchise_oversupply.md`), Running keeps losing share, and Digital promotions build.
5. **2024 to 2026:** the classics cycle turns, and China and Converse collapse. The org chart had already been reversed (May 2024 and Sept 2025), and the decline continued.

Under this chain the org and talent changes are an effect of step 2 and step 3, and their incremental contribution beyond the trend set in 2017 is small. The discriminating fact is item 4 above: running weakness and the lifestyle tilt already existed in the FY17 to FY19 category data.

### C4. What still stands from the original note

- The 2020 cuts were real, and anecdotes of lost footwear expertise are credible (BI, May 26, 2023, OPENED in the original note).
- Running did recover after sport teams were rebuilt, so sport-category ownership matters at the margin.
- Reorganization fatigue (a structural reset every year from 2020 to 2026, plus Pace) is a real forward risk.

### C5. Limits

- No web search was available to this challenge. I did not test peer organizations (for example, whether adidas made similar Men's/Women's restructurings) and did not reopen any news article.
- The FY17 to FY19 Running series covers only two years, and Nike restated category definitions between filings (the FY18 10-K shows Running at $5,198M for FY18; the FY19 10-K restates it to $4,496M). I used only same-filing comparisons.
- The composition of the FY18 to FY20 headquarters hiring is inferred, not disclosed.

### C6. Sources (all OPENED from EDGAR on 2026-10-13)

| Source | Filed | Used for |
|---|---|---|
| Nike Q4 FY2017 call transcript, 8-K Ex. 99.1, https://www.sec.gov/Archives/edgar/data/320187/000032018717000059/q4fy17erccexhibit991.htm | 2017-07-05 | "better editors"; categories, design and merchandising combined; Sportswear "nearly $8.6 billion" |
| Nike Q3 FY2018 call transcript, 8-K Ex. 99.1, https://www.sec.gov/Archives/edgar/data/320187/000032018718000037/q3fy18erccexhibit991.htm | 2018-03-27 | "power franchises"; Jordan distribution tightening; "Jordan inventories are now clean" |
| Nike leadership restructure press release, 8-K Ex. 99.1, https://www.sec.gov/Archives/edgar/data/320187/000032018718000026/pressrelease.htm | 2018-03-16 | Edwards exit; Hill and Spillane split |
| Nike FY2016 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018716000336/nke-5312016x10k.htm | 2016-07-21 | Men's, Women's, Young Athletes' split; HQ about 10,700; nine categories |
| Nike FY2017 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018717000090/nke-5312017x10k.htm | 2017-07-20 | nine categories; "category offense"; HQ about 10,800 |
| Nike FY2018 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018718000142/nke-5312018x10k.htm | 2018-07-25 | six categories; HQ about 11,200 |
| Nike FY2019 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018719000051/nke-531201910k.htm | 2019-07-23 | Running and Sportswear FY17 to FY19 (p. 27); HQ about 12,600 (p. 19) |
| Nike FY2020 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018720000047/nke-531202010k.htm | 2020-07-24 | consumer construct and Women's/Kids reinvestment (p. 27); Running FY20 (p. 31) |
| Nike FY2021 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018721000028/nke-20210531.htm | 2021-07-20 | CDA as "a new digitally empowered phase of the Consumer Direct Offense" (p. 28); Running and Sportswear FY21 (p. 32) |
| Nike FY2022 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018722000038/nke-20220531.htm | 2022-07-21 | sport-category table discontinued; Men's/Women's/Kids'/Jordan FY21 restated (p. 32) |
| Nike FY2024 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018724000044/nke-20240531.htm | 2024-07-25 | Men's/Women's/Kids'/Jordan FY24 (p. 34) |
| EDGAR full-text search (efts.sec.gov), Nike CIK 320187, phrases "consumer construct", "category offense", "Edit to Amplify" | 2026-10-13 | first and last use of each phrase in filings |

---

## Challenge: REFUTER

Second refuter pass, 2026-10-13. Kept short on purpose: the earlier REFUTER and ROOT-CAUSE sections above already re-checked the segment numbers, the HQ series back to FY2016, the FY17 to FY19 running data, the DTC versus wholesale split and the Vans control. I agree with them and do not repeat them. I ran only the checks they left open.

1. **HQ figures FY23 to FY26 confirmed, and their shape cuts against the hypothesis.** 10-K Item 2 text (EDGAR, OPENED Oct 13, 2026): HQ "occupied by approximately" 11,400 (FY2023 10-K), 10,700 (FY2024), 10,500 (FY2025), 10,600 (FY2026). Headquarters was *growing again* from FY22 (11,200) to FY23 (11,400), the two years when the 2020 talent loss should have been biting hardest. The next cut (11,400 to 10,700, -6%, my arithmetic) came with the Dec 2023 cost plan, alongside the return to sport teams, and it is the one that sits right before the Jun 2024 revenue turn. So the HQ cut closest in time to the decline belongs to the reversal of the 2020 construct, not to the construct itself.
2. **Worldwide headcount confirmed** (same 10-Ks, OPENED): 83,700 (FY23), 79,400 (FY24), 77,800 (FY25), 73,000 (FY26). The largest workforce reductions (-12.8% FY23 to FY26, my arithmetic) happened during the decline and under the insider CEO. If cuts drain capability with a 2 to 3 year lag, as the hypothesis requires, this is forward risk for FY27 to FY29. It is not an explanation for FY25 to FY26.
3. **Peer check, from the repo** (`Gulden and Plank turnarounds vs Nike/`, REPO-NOTE): Under Armour under a returning founder (Plank) had heavy management churn and repeated restructurings, and still shrank. adidas under Gulden recovered without a big 2023 layoff program. Leadership continuity versus churn does not sort peer outcomes any better than it sorts Nike's own segments.

**Net:** nothing here rescues the hypothesis. I side with the earlier REFUTER: it is a **minor** contributor, about 0% to 10% of the FY24 to FY26 decline, overlapping the oversupply and newness estimates and not measured directly. The talent strand is real as history and as forward risk, but the data does not show it causing the FY25 to FY26 decline.

Sources: Nike FY2023 to FY2026 10-Ks, Items 1 and 2 (https://www.sec.gov/Archives/edgar/data/320187/000032018723000039/nke-20230531.htm, .../000032018724000044/nke-20240531.htm, .../000032018725000047/nke-20250531.htm, .../000032018726000088/nke-20260531.htm), OPENED Oct 13, 2026 from text copies already in this session's scratchpad. Peer notes: REPO-NOTE.

---

## Challenge: ROOT-CAUSE

Second ROOT-CAUSE pass, 2026-10-13. Kept deliberately short. The first ROOT-CAUSE section above (C1 to C6) already traced the org and talent change upstream to the 2017 Consumer Direct Offense, using primary filings, and two REFUTER passes checked the numbers. A fresh full challenge would repeat them, so I ran one check on the open gap (C5: no web search was available) and stopped.

1. **Nike's own 2020 announcement ties the construct to CDA, not the other way round.** Nike's June 2020 release, reposted by Santa Clara University's Retail Management Institute (https://www.scu.edu/business/retail-management-institute/news-and-events/news-stories/nike-announces-senior-leadership-changes-to-unlock-future-growth-through-the-consumer-direct-acceleration-.html, SNIPPET, seen 2026-10-13), is headed "Senior Leadership Changes to Unlock Future Growth Through the Consumer Direct Acceleration" and says the "new, simpler consumer construct of Men's, Women's and Kids" serves that strategy. The org chart was a tool of the channel and franchise strategy. That matches C2 item 1 (FY2021 10-K p. 28, OPENED): CDA was "a new digitally empowered phase of the Consumer Direct Offense" of 2017.
2. **Web commentary adds no testable evidence.** The same search (2026-10-13) returned blogs and commentary (Founding Fuel, philippdubach.com, presse-citron.net; SNIPPET) that repeat the "lost sport expertise" story. None gives category, region or timing data that would separate the construct from the 2017 strategy or from the classics cycle, so none changes the result.

**Net:** I agree with the first ROOT-CAUSE pass. The organizational and talent change is a **symptom of another cause**: it implemented a classics-heavy, DTC-first franchise strategy set in 2017 by an insider CEO. Its incremental share of the $4,964M FY24 to FY26 decline is about 0% to 5%. Its forward risk (yearly reorganizations, the 2026 CFO and CAO turnover, -12.8% headcount FY23 to FY26) is real but sits outside the measured decline.
