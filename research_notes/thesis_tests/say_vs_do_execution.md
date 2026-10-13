# T_EXECUTION: Is Nike actually executing the wholesale / full-price turnaround?

Prepared 2026-10-13. Question: do money, people, partnerships and incentives match the stated strategy ("Repositioning NIKE Brand Digital as a full-price platform and reinvesting in wholesale distribution", "investments to elevate the presentation of our brands in physical retail", clean-up "by the end of December 2026")?

Citation conventions: SEC filings are cited as filing + printed page (p.). Earnings releases have no printed pages and are cited "seq p.". Call quotes come from Motley Fool transcripts (Q3 FY26 and Q1 FY27) or from trade press that quoted the call (Q1 FY26, Q2 FY26, Q4 FY26), marked "via [outlet]". "Snippet-only" means only a search headline was seen. All quotes are verbatim and under 25 words.

Data files (all in `/tmp/claude-0/-home-user-nike-research-case-comp/97c520cc-64e5-53f3-8fe9-898f5b11e054/scratchpad/execution/`):
- `money_trends.csv`: capex, PP&E software and leasehold balances, demand creation, sales-related reserves, employees, Global Brand Divisions cost, severance and Pace figures, top-3 customer share, channel revenue.
- `store_counts_by_year.csv`: Nike-owned store counts FY2019 to FY2026 (Item 1) and leased stores (Item 2).
- `hiring_counts_2026-10-13.csv`: my function buckets for all 381 corporate postings.
- `hiring_site_facets_2026-10-13.csv`: Nike's own career-area counts (1,300 postings, 381 corporate).
- `nike_corporate_jobs_2026-10-13.csv`: all 381 corporate postings with title, family, city, URL, bucket.
- `hiring_archive_comparison.csv`: Wayback snapshots of old jobs.nike.com, 2022 to 2024.
- `partnership_timeline.csv`: dated wholesale events with sources.
- Raw pages in `raw/`, text versions in `txt/`, scripts in `scripts/`.

---

## (A) Plain-English summary (for a finance beginner)

1. **The money follows wholesale. Proof: revenue mix and partner rebates.** In FY2026, sales to stores like DICK'S and Foot Locker rose to $27.5B (+6%). Nike's own channels fell to $17.7B (-6%), and its app and website fell from $9.6B to $8.6B (10-K FY2026, p. 32 to 33). Nike also paid to clean up partners' shelves. Its reserve for partner returns and discounts rose from $994M (FY2023) to $1,834M (FY2025), then eased to $1,589M (FY2026) (10-K FY2026 p. 84; FY2023 p. 84).
2. **Nike is shrinking its own store fleet.** Full-price Nike-owned "in-line" stores fell from 146 to 125 in FY2026. Leased stores worldwide fell from 1,029 to 980 (10-K FY2026 p. 2 and 25). Management said it will "close doors that are no longer aligned" (Q4 FY26 call, via SGB).
3. **Capital spending is low, and Nike does not say what it buys.** Capex was $684M in FY2026, about 60% of the FY2019 level ($1,119M) (10-K FY2026 p. 58). Nike does not split capex into stores, distribution and technology. Money for partner displays mostly sits inside "demand creation" (marketing), which grew only 1% in FY2026.
4. **The people changes point at wholesale and away from digital.** The Chief Technology Officer job was eliminated (Dec 2025). About 1,400 jobs were cut in April 2026, "the majority in Technology". A Walmart veteran, Jane Ewing, now runs Sales and Nike Direct as Chief Commercial Officer, with the VP of Global Sales reporting to her (Aug 27 2026 release).
5. **Nike's job postings do not show a wholesale hiring push.** Of 381 corporate openings on Nike's career site today, only 18 (4.7%) are sales, account or marketplace jobs, and only 2 of those are in the US. Technology is 105 (27.6%), but 63 of those are in India. That fits a move of tech work to Bengaluru, not a wholesale build-out.
6. **Partnerships are real, but many predate the current CEO.** New since late 2024: Amazon (May 2025), Academy's Jordan launch in 145 stores (April 2025, confirmed in Academy's SEC filing) and Urban Outfitters' "On Rotation" concept. Nike also claims more than 15,000 refreshed wholesale spaces in FY2026. The DSW, Macy's, Zappos and Urban Outfitters returns started in 2022 and 2023, under the previous CEO.
7. **Pay is not tied to wholesale or full-price health.** Annual bonuses depend only on adjusted revenue and adjusted EBIT. Long-term stock awards use revenue, EPS and relative TSR (shareholder return compared with S&P 500 companies). The Dec 2025 retention grants use EBIT margin growth. No metric measures channel mix, sell-through or full-price share (2026 proxy p. 30 to 34).
8. **The December 2026 deadline has slipped.** The FY2026 10-K said the clean-up would be done "by the end of December 2026". The Q1 FY2027 10-Q (Oct 2026) dropped that date: Sportswear and Jordan actions now run beyond FY2027, and China also runs beyond FY2027. North America wholesale growth slowed from +24% to +9% over five quarters. Management also admits part of the growth was a pipeline fill, meaning product shipped into stores ahead of consumer demand ("North America sell-in").

---

## (B) SAY vs DO scorecard

| Stated commitment | Concrete evidence it is happening | Strength | Source |
|---|---|---|---|
| "Reinvesting in wholesale distribution" | FY2026 wholesale $27,453M (+6%) vs NIKE Direct $17,720M (-6%). NA wholesale +14% "including expanded distribution, higher shipments to existing partners and fewer marketplace management actions". | **Strong in North America; weak elsewhere** (Greater China wholesale -14% FY26; total wholesale -1% in Q1 FY27) | 10-K FY2026 p. 32, 37, 39; ER Q1 FY27 seq p. 1 |
| Wholesale partners get more of the pie | Top-3 US customer share: 21% (FY24), 25% (FY25), 29% (FY26). "During fiscal 2026, our three largest United States customers accounted for approximately 29% of sales in the United States." Part of this is the DICK'S/Foot Locker merger. | Strong (but merger-inflated) | 10-K FY2024, FY2025, FY2026 p. 2 |
| "Higher sales returns and discounts with our wholesale partners" | Sales-related reserves (returns, post-invoice discounts, claims): $994M FY23, $1,282M FY24, $1,834M FY25, $1,589M FY26. Returns reserve $1,277M to $1,099M. | **Strong** (cash really given to partners; easing in FY26 fits cleanup progress) | 10-K FY2026 p. 84; FY2025 p. 83; FY2024 p. 85; FY2023 p. 84 |
| "Repositioning NIKE Brand Digital as a full-price platform" | Digital sales $9.6B to $8.6B. NA: site-wide promotion days down by more than 50 (Q1 FY26). EMEA: "off-price was down by more than 50 percent", "15-point improvement in full-price realization" (Q4 FY26). | **Strong** (revenue knowingly given up) | 10-K FY2026 p. 33; SGB Q1 FY26 and Q4 FY26 (URLs in D) |
| "Investments to elevate the presentation of our brands in physical retail" (first appears in Q1 FY26 10-Q; absent from FY2025 10-K) | Management claims: more than 15,000 wholesale spaces refreshed in FY26; 5,000+ football doors; 600+ ACG doors; China "must-win doors". Demand creation (which includes "retail brand presentation costs") only +1% in FY26 ($4,754M) with lower brand marketing; Q1 FY27 +5%. No dollar figure disclosed. | **Medium** (activity claims, no audited spend) | 10-K FY2026 p. 34; Q3 FY26 and Q1 FY27 transcripts; WWD/SGB Q4 FY26 |
| Capital behind the strategy | Capex $1,119M (FY19), $1,086M, $695M, $758M, $969M, $812M, $430M (FY25), $684M (FY26); Q1 FY27 $199M vs $207M. Leasehold improvements gross $2,037M to $2,114M; internal-use software gross $1,693M to $1,832M (still rising). | **Weak / ambiguous** (low, undifferentiated; software still growing) | 10-K FY2026 p. 58, 67; 10-Q Q1 FY27 p. 4 |
| Close or rezone own stores (implicit DTC retreat) | Nike in-line stores 146 to 125; Converse stores 132 to 114; leased retail stores 1,029 to 980. Hill: "close doors that are no longer aligned with our strategy". | Strong | 10-K FY2026 p. 2, 25; FY2025 p. 2 to 3, 25; SGB Q4 FY26 |
| Shift technology/digital spend down | Dec 2025: "we've eliminated the EVP, Chief Technology Officer role on the SLT". Apr 2026: "approximately 1,400 roles in Global Operations, with the majority in Technology". Q4 FY26: "redeployed resources from our Nike Direct technology teams". Global Brand Divisions (digital ops + enterprise tech) overhead -14% in Q1 FY27; FY26 GBD loss only -2%. FY26 severance mostly "within Global Brand Divisions, North America and EMEA". | **Medium to strong** (headcount cut; spend line only starting to fall) | 8-K Dec 2 2025; fox5ny.com; 10-K FY2026 p. 36, 89; 10-Q Q1 FY27 p. 30 |
| Leadership pointed at the marketplace | Geography heads report to CEO (Dec 2025). Ewing EVP CCO leads "Sales and Nike Direct", with VP Global Sales Erica Bullard reporting to her (eff. Sept 7 2026). Peddie rehired as VP Marketplace Partners (Jul 2024, pre-Hill), then NA GM. | **Strong** | 8-K Dec 2 2025 seq p. 1; Nike Aug 27 2026 release; Retail Dive 720981 |
| Hire wholesale talent ("retail marketing, visual merchandising and account management teammates", Hill, June 2025) | Today: 18 of 381 corporate postings (4.7%) are sales/account/marketplace, only 2 in the US; 14 (3.7%) are physical retail presentation. Nike's own "Sales & Customer Service" area = 20. | **Weak** (no visible current surge; may already be filled or frozen ahead of Pace) | careers.nike.com scrape (C); Modern Retail Jun 2025 |
| Pace savings reinvested in strategy | Pace: ~$1.0B charges, ~$2.5B savings through FY2031, majority of savings in FY29 to FY30. Stated reinvestment targets: "product innovation, brand storytelling, consumer connection, sport and growth". Wholesale not named. | **Weak link** to wholesale | 8-K Oct 1 2026 seq p. 2; Nike Oct 1 2026 memo; Q1 FY27 transcript |
| Incentives reward wholesale / full-price health | PSP = Adjusted Revenue 50% + Adjusted EBIT 50%; PSU FY26 to 28 = Adjusted Revenue 50% + Adjusted EPS 50% with rTSR modifier; retention = FY27 EBIT margin growth; MBOs = overhead spend and engagement. No channel, sell-through or full-price metric. | **Weak** (only indirect via margin) | 2026 proxy p. 30, 32, 34 |
| China: partner online stores end January 2027 | Nike release (Jul 21 2026): "partner-operated online storefronts will transition out of selling Nike product". Partners refocused on "elevating the brick-and-mortar experience". Note: this *cuts* wholesale digital to protect price. | Medium (announced; execution starts Jan 2027) | about.nike.com magazine; Retail Dive 825894 |
| Clean-up complete "by the end of December 2026" | Q3 FY26 10-Q and FY26 10-K: "we expect to complete these actions by the end of December 2026". Q1 FY27 10-Q: NSW and Jordan actions "expected to extend beyond fiscal 2027"; Greater China "to extend beyond fiscal 2027". | **Contradicted** (deadline slipped) | 10-Q Q3 FY26 p. 26; 10-K FY2026 p. 30; 10-Q Q1 FY27 p. 20 |

---

## Evidence detail by bucket

### 1. MONEY (filings)

- Capex (Additions to PP&E, $M): FY19 1,119 (10-K FY19 p. 53); FY20 1,086 (p. 59); FY21 695 (p. 60); FY22 758 (p. 59); FY23 969 (p. 58); FY24 812 (p. 60); FY25 430 (p. 59); FY26 684 (10-K FY26 p. 58); Q1 FY27 199 vs 207 (10-Q Q1 FY27 p. 4).
  - FY26 10-K p. 45: "cash used by investing activities was $488 million, primarily driven by additions to Property, plant and equipment".
  - No breakdown by purpose. PP&E gross at May 31 2026 vs 2025 (p. 67): buildings 3,589 vs 3,510; machinery 3,027 vs 2,954; internal-use software 1,832 vs 1,693; leasehold improvements 2,114 vs 2,037. Software (largely digital/technology) still grew in gross terms. This is an inference from balances that are net of disposals.
- Nike-owned stores (Item 1). Nike Brand total and in-line: FY19 951 / 86; FY20 935 / 80; FY21 898 / 76; FY22 901 / 95; FY23 896 / 123; FY24 910 / 138; FY25 902 / 146; FY26 874 / 125. Converse: 172 (FY19) to 114 (FY26). Leased retail stores (Item 2): 1,043 (FY21), 1,041, 1,027, 1,040, 1,029, 980 (FY26). FY26 10-K p. 25: "We lease approximately 980 retail stores worldwide, which primarily consist of factory stores." Distribution centers outside the US fell from 72 to 65 (10-K FY25 and FY26 p. 3 / p. 2).
- Demand creation ($M): 3,850 (FY22), 4,060, 4,285, 4,689 (FY25), 4,754 (FY26, +1%); Q1 FY27 1,252 vs 1,188.
  - Definition, 10-K FY26 p. 34: "Brand marketing expense includes advertising and promotion costs such as production and media costs, digital marketing expense, brand events and retail brand presentation costs".
  - FY26 driver, p. 34: "higher sports marketing expense ... partially offset by lower brand marketing expense".
  - Wholesale-directed spend is not split out.
- Wholesale sales returns and discounts (reserve balances above).
  - 10-K FY26 p. 30: "higher sales returns and discounts with our wholesale partners to reduce inventory and create capacity for new product".
  - Q1 FY26 gross margin was hit by "higher wholesale discounts" (via SGB Q1 FY26).
- Restructuring money:
  - FY26 severance $385M (10-K FY26 p. 89): "The majority of these charges were classified within Global Brand Divisions, North America and EMEA."
  - Purpose (p. 30): "realigning costs across our supply chain and technology to serve an integrated marketplace".
  - Pace (8-K Oct 1 2026 seq p. 2): "pre-tax charges of approximately $1.0 billion" and "approximately $2.5 billion in cumulative savings through fiscal 2031".
  - Denton (Q1 FY27 call): "expect the majority of the program savings to be realized in fiscal years '29 and '30".
- Technology/digital spend:
  - Global Brand Divisions holds "costs associated with NIKE Direct global digital operations and enterprise technology" (10-Q Q1 FY27 p. 15). Its loss was (4,720) FY24, (4,699) FY25, (4,603) FY26 (10-K FY26 p. 36).
  - Q1 FY27 10-Q p. 30: "Operating overhead expense decreased 14% primarily due to lower wage-related expense."
  - Employees: 83,700 (FY23), 79,400, 77,800, 73,000 (FY26) (10-K p. 6 each year).

### 2. PEOPLE

- Dec 2 2025 SLT note (8-K Dec 2025, Ex. 99.1 seq p. 1):
  - "the senior leaders of Nike's four Geographies will now join the SLT, reporting to me".
  - "we've eliminated the EVP, Chief Technology Officer role on the SLT".
  - Global Sales and Nike Direct moved under the CFO: "insights from our stores, our digital platforms, and our wholesale partners directly shape our corporate planning".
- Aug 27 2026 release (https://about.nike.com/en/newsroom/releases/nike-inc-august-27-2026-senior-leadership-announcement):
  - "Jane will lead our global Marketplace organization, including Sales and Nike Direct".
  - "VP of Global Sales Erica Bullard, VP of Nike Direct Shannon Glass and VP of Geo & Marketplace Analytics Gail Cornelius will report" (abridged).
  - "accelerate growth across Nike Direct and wholesale".
  - WWD: "Ewing's role is focused solely on leading Nike's integrated marketplace across wholesale and Nike Direct" (https://wwd.com/footwear-news/shoe-industry-news/nike-chief-commercial-officer-jane-ewing-walmart-1239172832/).
- Tom Peddie (Retail Dive, Jul 10 2024, https://www.retaildive.com/news/nike-tom-peddie-returns-vice-president-marketplace-partners-dtc-wholesale/720981/): "Tom Peddie will return to Nike as vice president of marketplace partners". This was a Donahoe-era hire. Peddie became NA GM in Oct 2024 and joined the SLT in Dec 2025.
- April 2026 cuts (https://www.fox5ny.com/news/nike-cut-1400-jobs, quoting COO memo):
  - "a reduction of approximately 1,400 roles in Global Operations, with the majority in Technology".
  - Technology was refocused on "two main hubs" (Beaverton and the Nike India Technology Center).
- Q4 FY26 call, Hill (via SGB, https://sgbonline.com/exec-nike-sees-weakness-in-sportswear-and-jordan-weighing-on-turnaround/): "We've redeployed resources from our Nike Direct technology teams to better support the company end-to-end".
- Q4 FY25 call, Jun 26 2025 (via Modern Retail, https://www.modernretail.co/operations/nike-says-its-making-progress-with-its-wholesale-turnaround-as-it-readies-for-its-return-to-amazon/): Nike is boosting hiring of "retail marketing, visual merchandising and account management teammates".
- Pace memo, Oct 1 2026 (https://about.nike.com/en/newsroom/releases/nike-inc-corporate-announcement-october-1-2026): "Decisions about impacted roles related to this work will begin in calendar year 2027 and beyond." There is also a new Bengaluru campus, and APGC leadership moves to Singapore.

### 3. PARTNERSHIPS: see section (D).

### 4. INCENTIVES: see section (E).

### 5. RESULTS SO FAR

North America wholesale growth by quarter (currency-neutral), with management's stated reason:

| Quarter | NA wholesale | Total NIKE Brand wholesale (c-n) | Management explanation | Source |
|---|---|---|---|---|
| Q1 FY26 (Aug 2025) | +11% | +5% | "in part due to shipment timing in the prior year as well as expanded distribution". Also "higher liquidation volume to off-price channels" (via SGB, paraphrase). | 10-Q Q1 FY26 p. 25; ER seq p. 1 |
| Q2 FY26 (Nov 2025) | +24% | +8% | "impacts of our marketplace management actions in both the current and prior year, expanded distribution ... shipment growth to existing partners" | 10-Q Q2 FY26 p. 30 |
| Q3 FY26 (Feb 2026) | +11% | +1% | "driven by new distribution and lapping marketplace management actions with existing partners" (Friend) | 10-Q Q3 FY26 p. 33; Q3 FY26 call |
| Q4 FY26 (May 2026) | +10% | +1% | "driven by new and existing distribution" (via SGB) | ER Q4 FY26; SGB |
| Q1 FY27 (Aug 2026) | +9% | -1% | Q2 FY27 faces "a higher comparison of North America sell-in activities versus last year" (Denton) | 10-Q Q1 FY27 p. 26; Q1 FY27 call |

Management quotes on order books, futures, inventory and sell-through:
- Q4 FY25 (Jun 2025), Hill via Modern Retail: "our order book is improving sequentially, with our holiday orders up."
- Q1 FY26 (Sep 30 2025), via SGB (https://sgbonline.com/exec-nikes-sales-show-some-recovery-tariffs-expected-to-cost-1-5-billion/):
  - Hill: "we are also pleased with the launch of the Nike Brand store on Amazon".
  - Friend: "steady progress on our plans for a healthy marketplace by the end of the first half".
  - Spring order book up versus the prior year (paraphrase).
- Q2 FY26 (Dec 18 2025), Hill via WWD (https://wwd.com/footwear-news/shoe-industry-news/nike-earnings-analysis-q2-2026-china-converse-1238430467/): "The team has done an excellent job of reconnecting with partners".
- Q3 FY26 (Mar 31 2026), transcript https://www.fool.com/earnings/call-transcripts/2026/04/01/nike-nke-q3-2026-earnings-call-transcript/:
  - Friend: "Order books are growing, and we are taking back shelf space."
  - Friend: "However, sell-through trends are not yet where we want them to be."
  - Hill: "By the end of the calendar year, we expect to have finished our Win Now actions."
  - Friend: "we have a clear set of plans in place to complete our Win Now actions by the end of the calendar year."
  - Friend (Greater China): "partner inventory also declined double digits."
  - Hill: "Aged inventory across the marketplace will be healthy".
- Q4 FY26 (Jun 30 2026), Hill via WWD (https://wwd.com/footwear-news/shoe-industry-news/nike-q4-live-updates-conference-call-1239048536/): "Sell-through remains challenged, impacting both current discounting and future order books". Friend (via SGB) said Nike is "taking actions to tighten buys, reduce future sell-in, and manage inventory".
- Q1 FY27 (Oct 1 2026), transcript https://www.fool.com/earnings/call-transcripts/2026/10/02/nike-nke-q1-2027-earnings-call-transcript/:
  - Hill: "that has impacted our future order books as we proactively work with our wholesale partners to work through excess inventory".
  - Hill: "we are seeing good sell-through across all channels" (performance product in NA).
  - Hill: "we will deliberately reduce the volume and frequency of specific Jordan Retro launches."
  - Denton: "We will continue to take actions to reduce supply across key parts of the marketplace".
  - Denton: "we are taking discounts and resetting the marketplace, which is dampening gross margins over time."
  - FY27 revenue guided to a high single-digit decline.

What was promised "done by December 2026" and what happened:

| Date | What Nike said | Source |
|---|---|---|
| Apr 1 2026 (Q3 FY26 10-Q) | "we expect to complete these actions by the end of December 2026" | 10-Q Q3 FY26 p. 26 |
| Jul 15 2026 (FY26 10-K) | Repeated the December 2026 completion target. "North America has made the most progress ... Greater China and Converse will take more time." | 10-K FY26 p. 30 |
| Oct 2 2026 (Q1 FY27 10-Q) | Date removed. "additional actions related to NIKE Sportswear and Jordan Brand are expected to extend beyond fiscal 2027". Converse "throughout fiscal 2027". Greater China "to extend beyond fiscal 2027". | 10-Q Q1 FY27 p. 20 |

---

## (C) Hiring data and method

**Method.**
1. jobs.nike.com now redirects to careers.nike.com, a Paradox-hosted site. Its JSON endpoint (`/api/get-jobs`) returned 403, so I read the server-rendered job data embedded in each listing page instead.
2. I pulled all 39 pages of the "Corporate" filter (`?page_number=N&filter[cf_job_category][0]=Corporate`), 10 jobs per page, 381 unique requisitions, 2.2 seconds apart. I also took the site's own facet counts for all 1,300 postings.
3. Each corporate posting went into one bucket, using Nike's job-family field plus title keywords (`scripts/classify.py`). The rule order is: HR/accounting go to other; "Direct" goes to digital/Nike Direct; marketplace or retail presentation; tech families or titles; e-commerce/digital titles; account/sales/wholesale; otherwise other.
4. Spot checks: "NA Wholesale Revenue Senior Accountant" and "HRBP, Marketplace" were moved to other. "GM, Jordan Direct GC" went to Nike Direct.

**Current snapshot (2026-10-13), corporate postings = 381:**

| Bucket | Count | Share | of which India | of which US |
|---|---|---|---|---|
| Wholesale / sales / account / marketplace | 18 | 4.7% | 1 | 2 |
| Physical retail presentation (VM, retail marketing, door development) | 14 | 3.7% | 0 | 4 |
| Digital / e-commerce / Nike Direct | 14 | 3.7% | 0 | 4 |
| Technology / data / engineering | 105 | 27.6% | 63 | 28 |
| Other corporate (product, design, marketing, finance, supply chain, etc.) | 230 | 60.4% | 4 | 127 |

Nike's own taxonomy, same date (all 1,300 postings):

| Area | Postings |
|---|---|
| Retail Stores (own-store staff) | 905 |
| Software Engineering | 61 |
| Design | 65 |
| Product Creation | 62 |
| Merchandising | 34 |
| Marketing | 28 |
| Sales & Customer Service | 20 |
| Information Technology | 13 |
| Data | 4 |
| Machine Learning | 3 |

Corporate postings by country: United States 165, Mainland China 88, India 68.

**Archived comparison (Wayback, old jobs.nike.com):**

| Date | Total postings | Technology category |
|---|---|---|
| Jan 16 2022 | 1,806 | n/a |
| Jun 4 2022 | 1,884 | n/a |
| Apr 22 2023 | 1,054 | 84 (8.0%). Technology or Digital: 89, which implies about 5 Digital-only. |
| May 25 2023 | 1,080 | n/a |
| Oct 12 2023 | 1,419 | n/a |
| May 13 2024 | n/a | Technology full-time: 2 (unreliable) |
| Oct 13 2026 | 1,300 | Nike's tech areas: 82 (6.3%). My broader tech bucket: 105. |

- No Sales-only archived snapshot exists for 2022 to 2024, so a wholesale-hiring trend cannot be measured.
- LinkedIn public search returned HTTP 429 (rate-limited), so it was not used.

**Reading.**
- Postings show neither a wholesale hiring push nor a technology exit. Sales and account roles are a small share, mostly in China and Europe.
- Tech roles are now concentrated in India (60% of tech postings). That is consistent with the April 2026 memo and the Pace Bengaluru campus.
- The tech share of all postings (about 6% to 8%) is similar to April 2023. The categories changed, so treat this as indicative only.

---

## (D) Partnership timeline (details and sources in `partnership_timeline.csv`)

| Date | Partner | Event | CEO era | Evidence |
|---|---|---|---|---|
| 2022 (approx) | Urban Outfitters | Wholesale quietly resumed | Donahoe | WWD list (secondary) |
| Oct 2023 | DSW, Macy's | Nike returned to DSW floors; Macy's "expanded selection", more stores in 2024 | Donahoe | WWD https://wwd.com/footwear-news/shoe-industry-news/lists/nike-wholesale-strategy-amazon-dtc-retail-return-1237809601/ |
| mid-2023 | Zappos, Belk, Shoe Show | Re-engaged | Donahoe | WWD citing WSJ/BI (secondary) |
| Jul 2024 | Peddie hire | VP Marketplace Partners | Donahoe | Retail Dive 720981 |
| Aug 21 2024 | Foot Locker | Reimagined store with Nike/Jordan basketball | Donahoe | snippet-only (PR Newswire headline) |
| Dec 19 2024 | DICK'S, Foot Locker, JD | Hill: "Some partners and channels feel we've turned our back on them" | Hill | Retail Dive 736175 |
| Mar 20 2025 (launch late Apr) | Academy Sports + Outdoors | "Launch of Jordan Brand in 145 Stores and Online" | Hill | Academy SEC Ex. 99.1 (https://www.sec.gov/Archives/edgar/data/1817358/000181735825000022/exhibit991pressreleaseye20.htm), seq p. 1 |
| May 19 2025 | Urban Outfitters | "Nike is the first On Rotation partner." | Hill | Retail Dive 748431 |
| May 2025 | Amazon US; Printemps | "expanding to new digital accounts, including Amazon in the U.S., new physical partners like Printemps" (Nike statement) | Hill | Retail Dive 748986; Modern Retail |
| Q1 FY26 (Jul to Aug 2025) | Amazon | Nike Brand store live; "stronger engagement and sales than anticipated" | Hill | SGB Q1 FY26 |
| Sep 8 2025 | DICK'S + Foot Locker | Merger closed; Nike "approximately 31% of our consolidated merchandise purchases" (FY2025) vs 25% (FY2024) | n/a | DICK'S 10-K FY2025 p. 9 |
| FY2026 | Wholesale doors | "refreshing more than 15,000 spaces in wholesale doors" (management claim via WWD) | Hill | WWD Q4 FY26 |
| Mar 31 2026 | Foot Locker, JD; DICK'S, Academy | "We are building long-term plans with Foot Locker and JD in athletic specialty." "Dick's and Academy are leaning in with us." | Hill | Q3 FY26 transcript |
| Jul 21 2026 | China (Topsports, Pou Sheng, 16 partners) | From January 2027, "partner-operated online storefronts will transition out of selling Nike product"; partners refocus on physical stores | Hill | about.nike.com magazine; Retail Dive 825894 |
| Aug 18 2026 | Foot Locker | Community hub store concept with Nike | Hill | snippet-only (FashionUnited headline) |
| Oct 1 2026 | Wholesale + Direct | Caitlin 1 in 5,000 doors; China "must-win doors" co-investment | Hill | Q1 FY27 transcript |

**Takeaway.**
- The big US re-entries (DSW, Macy's, Zappos, Urban Outfitters) began in 2022 and 2023 under Donahoe.
- Since Hill arrived (Oct 2024), the concrete new channels are Amazon, Academy Jordan, the Urban Outfitters concept and Printemps, plus large in-store refresh claims.
- China cuts partner digital distribution. It is a pro-price move, not pro-wholesale volume.

---

## (E) Incentive metrics (2026 proxy, DEF 14A filed 2026-07-15)

| Plan | Metrics | What it rewards | Wholesale / full-price link? | Source |
|---|---|---|---|---|
| FY2026 PSP (annual cash) | "equally weighted financial metrics of Adjusted Revenue and Adjusted EBIT". CEO 100% financial; other NEOs 80% financial plus 20% MBOs. | Targets: revenue +0.5% vs FY25, EBIT -15% vs FY25. Results: revenue $45.8B (76% earnout), EBIT $3.3B (125%). Paid at 74% (CEO) and 78% (other NEOs) after negative discretion. | None directly. EBIT rewards margin; revenue rewards volume, which can work against supply cuts. | proxy p. 30, 32 |
| MBOs (non-CEO NEOs, 20%) | "Managing wage-related operating overhead spend" and "Enterprise goals for employee engagement" | Cost control and engagement | None | proxy p. 30 |
| FY2026 to 2028 PSUs | "Adjusted Revenue (50%) and Adjusted EPS (50%) ... with a Relative TSR modifier" | Growth and EPS | None | proxy p. 32 |
| Dec 2025 retention grants ($15M Hill, $4M each other NEO) | 50% time-based, 50% "Adjusted Operating Margin Growth" (FY27 EBIT margin vs FY26) | Profitability in FY27 | Indirect: full-price sales and fewer discounts lift margin | proxy p. 34 |
| FY2024 to 2026 PSUs | Relative TSR | Paid 0% ("Relative TSR ... was at the 1st percentile") | n/a | proxy p. 34 |

**Verdict:** no pay metric names wholesale, channel mix, sell-through, inventory health or full-price realization. Alignment is only indirect, through EBIT and EBIT margin.

---

## (F) Gaps and what could not be verified

- Capex purpose is not disclosed (stores vs distribution vs technology). The PP&E line changes are only a proxy.
- Spend on partner "retail brand presentation" is buried in demand creation and not quantified. The "15,000 spaces" and "5,000 doors" figures are unaudited management claims.
- Transcripts:
  - Motley Fool has full transcripts only for Q3 FY26 and Q1 FY27 (Q1, Q2 and Q4 FY26 URLs returned 404).
  - Q1 FY26, Q2 FY26 and Q4 FY26 quotes come from SGB, WWD and Modern Retail coverage of the calls (secondary). Some SGB/WWD lines are paraphrases, marked as such.
- Hiring:
  - Current counts are a single-day snapshot.
  - The old site's categories differ from the new ones.
  - No archived Sales-category snapshot was found for 2022 to 2024.
  - The 2024-05-13 Technology full-time count (2) looks anomalous.
  - LinkedIn returned 429.
  - Classification is keyword-based and may misplace a few roles. The full list is in `nike_corporate_jobs_2026-10-13.csv` for review.
- Partnerships:
  - The Foot Locker 2024 and 2026 store concepts are snippet-only.
  - The Zappos return rests on secondary reporting.
  - Amazon sales size is undisclosed (Friend: not a "material needle-mover" right away, via Modern Retail).
  - DICK'S House of Sport openings (16 in 2025, about 14 in 2026, DICK'S 10-K FY2025) are not confirmed as Nike-specific shops.
  - The JD "long-term plans" have no public detail.
- Blocked sources: no Oregon WARN for April 2026 was found; Bloomberg, Reuters and CNBC are blocked.
- Q4 FY26 NA wholesale +10% is taken from SGB's call coverage and the caller's figure; the 10-K gives only the full-year +14%.
- The Google News decoder hit 503 errors on the last attempts, so some later articles could not be resolved.
