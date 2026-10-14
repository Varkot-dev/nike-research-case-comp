# Risk check: does tariff relief threaten the SHORT?

Written 2026-10-14. Stock $35.35. Question: the scoreboard says tariffs now in force (10% to 12.5%) are below the 15% Nike assumed, so gross margin could beat. Is that a real threat to the short?

Tags: OPENED = I read the primary document myself this session. SNIPPET = seen only in a search summary or a secondary write-up. REPO = earlier verified repo note. DERIVED = my arithmetic (script: `data/hunt/risk_tariffs/scripts/size_tariff_gap.py`, output `data/hunt/risk_tariffs/tariff_gap_sizing.csv`). Raw files are in `data/hunt/risk_tariffs/raw/`.

## 1. Verdict

**Weak threat to the SHORT. Points SHORT-to-NEUTRAL on this question, strength: moderate. The scoreboard's framing overstates it and should be corrected.**

1. **The rate gap is real but small.** In force today: Vietnam and China +12.5%, Indonesia and Cambodia +10%, on top of MFN (USTR Section 301 final action, in force since Jul 24, 2026, OPENED). Blended on Nike's US-bound mix that is about **11.4%** against the **15%** Nike's June plan assumed from August: a gap of about **3.5 points** (DERIVED).
2. **The 15% was a Q1 assumption from June, not the basis of the FY27 guide.** The 15% appears in the Q4 FY26 call (Jun 30, 2026) next to the **Q1** outlook. Nike gave no full-year guide then. The first full-year FY27 guide (adjusted EPS $1.15 to $1.35) came on **Oct 1, 2026**, ten weeks after the 10%/12.5% regime started. New CFO Denton called it his "best assessment of where this business stands today", built on a "comprehensive business and financial review". Nike never states the rate inside the Oct 1 guide, and "tariff" appears zero times on that call, so this is an inference. Still, a guide built in September at rates already in force almost certainly uses actual rates, not a lapsed 15% plan. FY27 consensus ($1.288, Yahoo, REPO) sits inside that guide.
3. **Even if all of it were unmodeled, it is small.** Against 15%, the gap is worth about **$0.04 to $0.07 of FY27 EPS (20 to 33 bps of GM)** and **$0.08 to $0.14 of FY28 EPS (35 to 60 bps)**, mid case $0.065 and $0.12 (DERIVED). That is 3% to 5% of FY27 EPS. Only the FY28 figure is material (about 7% of the $1.65 consensus), and it is almost certainly already in models that use current rates.
4. **The y/y tariff tailwind is real, but it is guided.** FY26 ex-refund carried about $1.07B to $1.14B of gross tariffs at IEEPA rates of about 19% to 20% (REPO). FY27 runs at about 11.4%, worth roughly $0.36B less y/y (DERIVED). Nike guided it as "gross margin to inflect positive" (Q3 FY26 call) and "gross margin expansion earlier beginning in Q1" (Q4 FY26 call). The Q2 FY27 print (about Dec 17) is the first full quarter of the lower rate against a -360 bps tariff comparison, so a Q2 GM beat is plausible. But it lands after finals and is a known tailwind, not a hidden one.
5. **The tails run both ways and are larger than the base gap.** LONG tails: a possible Section 122 refund (about $0.27B one-time, about $0.14/share, not in guidance) and a court loss for the Section 301 forced-labor tariffs (up to about $0.74B a year). SHORT tail: a pending Section 301 "excess capacity" investigation that names all four of Nike's main sourcing countries (+7.5 pts would cost about $0.49B a year, about $0.26/share). None resolves before Nov 19 with any known date.

**For the pitch:** treat tariffs as a second-order FY28 swing (plus or minus $0.10 to $0.25), not as a hidden FY27 beat. Drop "tariffs now in force are below Nike's 15% plan, so gross margin could surprise upward" as a reason the SHORT could fail. Replace it with: "Tariff policy is a two-sided tail (Section 122 refund upside vs excess-capacity 301 downside); the base-case gap is already in the Oct 1 guide."

## 2. What tariffs apply today (Oct 14, 2026) to Nike's US imports

### 2.1 Regime timeline

| Period | Authority | Rate on Nike's 4 countries | Source | Tag |
|---|---|---|---|---|
| Apr 2025 to Feb 23, 2026 | IEEPA "reciprocal" (plus China fentanyl IEEPA) | Vietnam 20%, Indonesia 19%, Cambodia 19%, China about 20% | REPO (expectations_gap.md S.2; tariffs_costs.md) | REPO |
| Feb 20, 2026 | Supreme Court strikes IEEPA tariffs | n/a | Nike Q3 FY26 10-Q "Other matters" (SEC, filed 2026-04-01) | OPENED |
| Feb 24 to Jul 23, 2026 | **Section 122** (Trade Act of 1974), Proclamation 11012, FR doc 2026-03824, published Feb 25, 2026 | **10% ad valorem, all countries**, "effective with respect to goods entered ... on or after 12:01 a.m. eastern standard time on February 24, 2026, and shall continue in effect through 12:01 a.m. eastern daylight time on July 24, 2026" (150 days). Statute allows "up to 15 percent". | govinfo PDF of FR 2026-03824, `raw/proclamation_11012_section122_fr2026-03824.txt` | OPENED |
| Feb 21, 2026 | Stated intent to raise Section 122 to 15% | **Never implemented**; the operative rate stayed 10% | Global Trade Alert, Ginger Control, tariffschart.com summaries (Sep to Oct 2026) | SNIPPET |
| **Jul 24, 2026 to now** | **Section 301 forced-labor action** ("FLIP"), USTR notice signed Jul 23, 2026, FR doc 2026-15181, published Jul 28, 2026; President's memorandum of Jul 23, 2026 | **Vietnam 12.5%** (HTS 9903.05.84), **China 12.5%** (9903.05.31), **Indonesia 10%** (9903.05.45), **Cambodia 10%** (9903.05.28). India, Bangladesh, Sri Lanka, Pakistan also 10%. | USTR PDF "FLIP 301 Investigation Final Action FRN 7-23-26", `raw/ustr_flip301_final_frn_2026-15181.txt` | OPENED |
| Still in force Oct 2026 | Same headings in the live tariff schedule | 9903.05.84 "The duty provided in the applicable subheading + 12.5%", 9903.05.45 "+ 10%", etc. | USITC HTS REST API, **HTS 2026 Revision 21 (current, released 2026-10-09)**, fetched 2026-10-14, `raw/hts_lookup_2026rev21.json` | OPENED |
| Jul 23, 2026 | CBP implementation | CSMS #69326983 "GUIDANCE: Section 301 Forced Labor Import Duties", applies to entries on or after 12:01 a.m. Jul 24, 2026 | content.govdelivery.com bulletin 421d887 | OPENED (via web fetch summary) |

### 2.2 Key terms of the Section 301 action (FR 2026-15181, OPENED)

- **Stacks on top of MFN.** U.S. note 52(a): products "shall also be subject to the general rates of duty imposed under subheadings in chapters 1 to 97" and "shall also be subject to any additional duty provided for in this subchapter". So for China it also stacks on legacy China Section 301 duties (9903.88.15 is "+ 7.5%" in HTS Rev 21, OPENED; which footwear lines it covers I did not check line by line).
- **The net-of-MFN cap applies only to the EU, Taiwan, Japan, Korea and Switzerland**, not to Vietnam, Indonesia, China or Cambodia. So high footwear MFN rates bring no relief.
- **No footwear or apparel exemption for Nike's countries.** I parsed every product list in note 52(b) to (k). No chapter 64 code appears anywhere. Chapter 61 and 62 codes appear only in the textile carve-outs for Guatemala, El Salvador and Jordan (headings 9903.06.06, 9903.06.09, 9903.06.20). The Cambodia and Indonesia carve-outs (9903.06.02 to .03, 9903.06.16 to .17) cover plants, wood, cork, silk and gems, not apparel or footwear (OPENED, DERIVED by text parse).
- **Textile TRQs pending.** For Bangladesh, Cambodia, Indonesia and Malaysia, USTR will set tariff-rate quotas (initial 3 years) letting some apparel made with US cotton or US textile inputs enter free of the 301 duty. "Until the Trade Representative establishes the TRQs ... [it] shall impose the applicable section 301 tariffs ... (here, 10 percent)." Small, possible future relief for Nike's Cambodian and Indonesian apparel (OPENED).
- **No expiry date.** Unlike Section 122 (150 days), a Section 301 action has no sunset in the notice. Statute: 4-year review (general knowledge, not verified this session).
- **In-transit rule:** goods loaded before Jul 24 and entered before Jul 28 paid no 301 duty (heading 9903.05.85, OPENED).

### 2.3 Base MFN duties (separate and unchanged; HTS 2026 Rev 21, fetched 2026-10-14, OPENED)

| HTS | Product | MFN general rate |
|---|---|---|
| 6404.11.90 | Athletic footwear, textile upper, rubber/plastic sole, over $12/pair | **20%** |
| 6402.99.90 / 6402.91.90 | Rubber/plastic upper footwear over $12/pair (tennis, basketball, training shoes) | **20%** |
| 6404.11.20 | Athletic footwear, textile upper, $6.50 to $12/pair | 10.5% |
| 6404.19.90 | Other textile-upper footwear over $12/pair | 9% |
| 6403.99.90 | Leather-upper footwear over $2.50/pair | 10% |
| 6110.30.30 | Synthetic knit sweaters/sweatshirts | **32%** |
| 6104.63.20 | Women's synthetic knit trousers/shorts | 28.2% |
| 6109.10.00 | Cotton T-shirts | 16.5% |
| 6114.30.30 | Other synthetic knit garments | 14.9% |

So a Vietnam-made $12-plus running shoe now pays about **32.5%** (20% MFN + 12.5% Section 301), against about 40% under IEEPA and 20% before 2025. The MFN layer was always in Nike's cost base. Only the 301 layer is "incremental", which is how Nike describes its rate assumptions.

## 3. What Nike assumed

| Date | Statement | Source | Tag |
|---|---|---|---|
| 2025-06-26 | Gross incremental tariff cost "approximately $1 billion" | Q4 FY25 call | REPO (tariffs_costs.md) |
| 2025-09-30 | Raised to "approximately $1.5 billion" annualized; net FY26 GM headwind about 120 bps | Q1 FY26 call; Q1 FY26 10-Q p. 19 | REPO |
| 2026-03-31 | NA Q3 FY26 GM down 360 bps "despite nearly 650 basis points of gross impact from new U.S. tariffs". "Assuming no significant changes, we expect the first quarter of fiscal '27 to be the final quarter where higher tariffs continue to be a material year-over-year headwind to gross margin. We expect gross margin expansion to begin in the second quarter due to actions to mitigate tariffs". "We will return to providing full year and long-term guidance at our Investor Day in the fall." | Q3 FY26 call transcript (Nike IR), `raw/nike_q3fy26_call_2026-03-31.txt` | OPENED |
| 2026-04-01 | IEEPA tariffs paid about $1.0B; recovery "not probable" at that date | Q3 FY26 10-Q, Other matters | OPENED |
| **2026-06-30** | "Specifically for the first quarter ... We expect gross margin in Q1 to be slightly positive. The tariff environment continues to be uncertain. **Our forecast is based on incremental tariff rates of 10% continuing through the end of July and then increasing to 15% thereafter** as we communicated last quarter." The only multi-quarter frame given: Q4 FY26 to Q2 FY27 earnings "flattish", excluding the refund. | Q4 FY26 call transcript, `raw/nike_q4fy26_call_2026-06-30.txt` | OPENED |
| 2026-06-30 | $986M IEEPA recovery booked in Q4 FY26 ($965M NA, $21M Converse), "largely offsetting" FY26 IEEPA tariffs; "Subsequent to May 31, 2026, we received substantially all of the remaining IEEPA tariff receivable." | FY26 10-K (filed 2026-07-15) | OPENED |
| **2026-10-01** | First full-year FY27 guide: revenue down high-single digits, adjusted EPS $1.15 to $1.35 (excluding about $0.15 of Pace costs). EBIT to fall more than revenue on "fixed cost deleverage ... higher input costs". "This range reflects our best assessment of where this business stands today." "We're making fairly significant moves in our supply chain and sourcing programs today. That is actually bolstering gross margin." **The word "tariff" appears 0 times on the call.** No FY27 GM guide ("we're probably not going to provide guidance specifically for gross margin"). | Q1 FY27 call transcript, `raw/nike_q1fy27_call_2026-10-01.txt` | OPENED |
| 2026-10-02 | Q1 FY27 bridge: product costs +10 bps, logistics +90 bps, FX +40 bps; NA GM +110 bps with "higher product costs, driven by product mix". No tariff line. Risk text only: "evolving tariff policies". | Q1 FY27 10-Q (nke-20260831) | OPENED |

**Reading:** the 15% is a June statement for the Q1 quarter (Jun to Aug), where it barely mattered: only August entries were affected, and they did not reach COGS before Q1 ended. The FY27 guide that consensus anchors on was built later, with the lower rate already in force for 10 weeks. Whether it uses 11% or 15% is not disclosed (an open question for Investor Day), but the burden of proof sits with "it still uses 15%".

## 4. Sizing the gap (DERIVED, `tariff_gap_sizing.csv`)

Inputs:
- **US-bound dutiable import value: $6.0B to $7.5B, mid $6.5B.** Method A: $1.5B annualized / about 20% blended IEEPA rate = about $7.5B. Method B: Q3 FY26 NA "nearly 650 bps" x NA revenue $5,026M = about $327M a quarter, about $1.31B a year, / about 20% = about $6.5B. FY27 volume is lower (revenue guided down high-single digits, NA buys tightened). I could not pull Census HS 64/61/62 import data (the API now needs a key), so this rests on Nike's own disclosures.
- **US-bound sourcing mix (assumption):** footwear Vietnam 55%, Indonesia 30%, China 8%, other 7%; apparel Vietnam 40%, Cambodia 15%, China 8%, others at 10% 37%; footwear 65% of value. Global mix from the FY26 10-K (REPO): footwear Vietnam 52%, Indonesia 27%, China 16%; apparel Vietnam 34%, Cambodia 15%, China 12%. China is cut for US-bound goods (management, REPO).
- **Blended actual rate: 11.4%** (footwear 11.6%, apparel 11.2%). Plan: 15%. **Gap: 3.6 points.**
- **Timing:** inventory $7,846M at Aug 31, 2026 against Q1 FY27 COGS $6,415M gives about 112 days on hand, about 3.7 months from entry to COGS. Plan and actual are identical through July (10%), so the gap starts with August entries and reaches COGS from about December. That leaves about 6.3 months of benefit in FY27.
- **Pass-through kept:** 70% to 100% (some cost-sharing or price actions may unwind). Tax 21.5%. 1,484M diluted shares. FY27 revenue about $43.1B, FY28 about $43.6B.

| Case | Annual gap ($M) | FY27 GM | FY27 EPS | FY28 GM | FY28 EPS |
|---|---|---|---|---|---|
| Low (base $6.0B, keep 70%) | 149 | +18 bps | +$0.04 | +34 bps | +$0.08 |
| **Mid (base $6.5B, keep 100%)** | **231** | **+28 bps** | **+$0.065** | **+53 bps** | **+$0.12** |
| High (base $7.5B, keep 100%) | 267 | +33 bps | +$0.07 | +61 bps | +$0.14 |

Context:
- FY27 guide width is $0.20 ($1.15 to $1.35). The FY27 gap fits inside it.
- FY28 consensus is $1.65. +$0.12 is about 7%. That is material only if FY28 models use 15%, and models usually run current statutory rates. I found no analyst note, and no Q&A on the Oct 1 call, that frames tariffs as unmodeled upside (search 2026-10-14, SNIPPET-level negative result).
- This matches the earlier repo estimate of $0.05 to $0.10 for FY27 (expectations_gap.md S.2).

**Is it in consensus?** Probably yes, for three reasons. (1) The FY27 guide postdates the regime. (2) Consensus moved to the guide (24 FY28 cuts in 7 days, REPO). (3) Nobody on the Oct 1 call asked about tariffs, which suggests the sell side saw nothing to clarify. Confidence: moderate. Nike never stated the rate inside the Oct 1 guide.

## 5. Risks the other way, and other tails

| Risk | Direction | Status (date, source, tag) | Size (DERIVED, mid base) | Before Nov 19? |
|---|---|---|---|---|
| **Section 301 "structural excess capacity" investigation** of 16 economies: China, EU, Singapore, Switzerland, Norway, **Indonesia**, Malaysia, **Cambodia**, Thailand, Korea, **Vietnam**, Taiwan, Bangladesh, Mexico, Japan, India. The initiation notice names footwear and apparel among the surplus sectors (China, others). | **Higher tariffs (SHORT)** | Initiated Mar 11, 2026 (USTR FRN, OPENED); hearings May 5 to 8, 2026; no finding or proposed action on the USTR page as of Oct 14, 2026 (OPENED); CRS Jul 2026 says "ongoing" (SNIPPET) | +7.5 pts (back to about IEEPA levels) = about $0.49B a year, about -$0.26 EPS before mitigation | Unknown. A proposed action would need comments and a hearing first, so a final rate before Nov 19 is unlikely. |
| **Court challenges to the Section 301 forced-labor tariffs**: In re Section 301 Forced Labor Cases (CIT); 25 states, State of Oregon v. Trump, No. 26-03467, filed Aug 3, 2026; three-judge panel hearing Sep 30, 2026 | **Lower tariffs (LONG)**, but likely replaced | No ruling, no stay found (STR, Cato, tradelawcounsel, internationaltradeinsights, Aug to Oct 2026, SNIPPET) | If vacated with no replacement: about $0.74B a year, about +$0.39 EPS. If the government wins, or swaps in the excess-capacity tariff: about 0. | Possible CIT ruling, but appeal and stay are likely (as happened with Section 122) |
| **Section 122 refund**: CIT held Proclamation 11012 ultra vires (Oregon v. US / Burlap and Barrel, Slip Op. 26-47, May 7, 2026); judgment covers only 3 named plaintiffs; CAFC stay pending appeal granted Jun 11, 2026 (Nos. 2026-1804, -1805); no merits ruling as of Sep 8, 2026 | **One-time gain (LONG)** | Strix Customs blog, Sep 8, 2026 (SNIPPET via fetch); PwC, Ward and Smith (SNIPPET). I found no sign that Nike is a plaintiff. Importers need protests or PSCs (first deadline about Dec 21, 2026) to keep refund rights. | 10% x about $6.5B x 5/12 = about $0.27B, about $0.14/share one-time. Like the $986M, likely excluded from adjusted EPS by investors. | No (appeal pending) |
| **Section 122 expiry** | Already happened Jul 24, 2026; replaced the same minute by the 301 action | Proclamation text (OPENED); FLIP FRN (OPENED) | n/a | n/a |
| **IEEPA refund clawback** | SHORT (small) | Cash already received ("substantially all", FY26 10-K, OPENED); the government cannot claw it back after the Supreme Court ruling. A consumer class action, Caldwell et al. v. Nike, 3:26-cv-00923 (D. Or., filed May 8, 2026), seeks pass-through of the refund to shoppers (Fashion Law, SGB, Fox Business, SNIPPET). | Exposure up to the price-increase share of $986M; probability-weighted small. | No |
| **Section 232** | n/a | No Section 232 action covers footwear or apparel. 232 goods (metals, autos, wood, semiconductors) are exempt from the 301 FLIP via 9903.05.90 (OPENED). | n/a | n/a |
| **Apparel TRQs** (Cambodia, Indonesia) | LONG (small) | Pending; USTR to publish an FR notice (OPENED) | Apparel from those two is about 15% to 20% of apparel; partial relief only | Unlikely |

**Net of the tails:** the two-sided risk (about +$0.39 / -$0.26 recurring, +$0.14 one-time) is larger than the base-case gap ($0.065 / $0.12). None has a decision date before Nov 19. So tariffs add **variance** to FY28, not a directional signal. If anything, the excess-capacity probe is the live policy track, and Nike's earlier 15% planning number looks like a deliberate cushion against it, which a new CFO is unlikely to throw away at Investor Day.

## 6. What would change this

1. **Investor Day (Nov 16 to 17):** any statement of the tariff rate in the FY28 framework. If Nike says "we planned at 15% and current rates are about 11%", the FY28 upside (+$0.12) becomes explicit and modestly LONG. If it says "current rates", this question closes as priced.
2. **USTR proposed action in the excess-capacity 301** (watch the USTR press page and the Federal Register). Any proposal covering Vietnam or Indonesia is SHORT.
3. **CIT ruling in the Section 301 forced-labor cases** (argued Sep 30). A ruling against the government, plus a stay denial, would be LONG.
4. **CAFC merits ruling on Section 122** (Nos. 2026-1804/-1805). An affirmance with broad relief would be a one-time LONG.
5. **Q2 FY27 print (about Dec 17, after finals):** product-cost line in the GM bridge. Our estimate is +110 to +160 bps y/y from tariffs (REPO expectations_gap.md S.2).

## 7. Corrections to the scoreboard

- "Tariffs now in force are 10% to 12.5%, below Nike's 15% plan ... so gross margin could surprise upward": **keep the facts, change the weight.** The 15% was the Q1 outlook assumption stated Jun 30, not a stated basis of the FY27 guide (first issued Oct 1). Rate the FY27 surprise as small ($0.04 to $0.07), likely priced. Rate FY28 as a two-sided tail.
- Section 4 "Biggest unknowns" item on 15% vs actual: keep it, add "Investor Day may answer it", and add the excess-capacity 301 as a downside unknown and the Section 122 refund as a one-time upside unknown.

## 8. Sources

| Source | Date | Tag | Used for |
|---|---|---|---|
| USTR, Notice of Actions in Section 301 Investigations ... Forced Labor (FR 2026-15181), ustr.gov PDF | signed 2026-07-23, published 2026-07-28 | OPENED | rates, headings, note 52, exemptions, TRQs |
| Proclamation 11012 (Section 122), FR 2026-03824, govinfo PDF | 2026-02-25 | OPENED | 10%, 150 days, Feb 24 to Jul 24 window |
| USITC HTS REST API, 2026 Revision 21 (current from 2026-10-09) | fetched 2026-10-14 | OPENED | MFN rates; 9903.05.xx still in force; 9903.88.15 +7.5% |
| CBP CSMS #69326983 | 2026-07-23 | OPENED (fetched summary) | implementation, stacking order |
| USTR, Initiation of Section 301 Investigations, Structural Excess Capacity (FRN PDF) and USTR investigation page | 2026-03-11; page fetched 2026-10-14 | OPENED | 16 economies; no action yet |
| Nike Q3 FY26, Q4 FY26, Q1 FY27 call transcripts (Nike IR PDFs, text copies in raw/) | 2026-03-31, 2026-06-30, 2026-10-01 | OPENED | assumptions, guide wording, zero tariff mentions |
| Nike FY26 10-K; Q3 FY26 and Q1 FY27 10-Qs (SEC) | 2026-07-15; 2026-04-01; 2026-10-02 | OPENED | refund, bridge, inventory |
| `data/nike_filing_facts.csv` | various | REPO | revenue, inventory, shares, sourcing mix |
| Strix Customs, "Section 122 Refunds: Where the Appeal Stands as of September 8, 2026" | 2026-09-08 | SNIPPET (secondary, fetched) | CIT and CAFC dates and case numbers |
| PwC Tax Insights; Ward and Smith; Global Trade Alert; Ginger Control; tariffschart.com | 2026-05 to 2026-10 | SNIPPET | Section 122 ruling, 15% never implemented |
| STR Trade Report; Cato brief; tradelawcounsel; internationaltradeinsights (25 states suit) | 2026-08 to 2026-10 | SNIPPET | FLIP 301 litigation status |
| Fashion Law, SGB Media, Fox Business on Caldwell v. Nike | 2026-05 | SNIPPET | consumer class action |
| Census API (HS 64/61/62 by country) | 2026-10-14 | NOT OBTAINED (API key required) | import base sized from Nike disclosures instead |
