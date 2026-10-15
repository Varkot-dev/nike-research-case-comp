# Jordan Brand: market, strategy and thesis evidence (as of 2026-10-13)

Method: followed `.claude/skills/verify-non-sec-claims/SKILL.md`. Every claim below cites a page that was opened (WebFetch, or curl for PDFs and SEC filings) unless marked otherwise. Statuses:

- **VERIFIED**: the page was opened and the quote or figure was on it.
- **VERIFIED (repo)**: the figure comes from SEC filings already extracted and checked in this repo (`data/nike_filing_facts.csv`). I also re-opened the FY26 10-K and the Q1 FY27 10-Q myself.
- **SNIPPET ONLY / UNVERIFIED**: seen only in a search snippet, or the page would not open. Do not use these as facts.
- **DERIVED**: my own arithmetic on verified inputs.

Source types: **SEC filing**, **Nike transcript** (Nike's official IR transcript PDF; a company statement), **Nike release**, **secondary news**, **analyst** (a sell-side view relayed by press), **data provider** (StockX, Sole Retriever, Piper Sandler, Lyst and similar).

Local copies of the opened PDFs and filings are in `jordan_market/dl/`. The transcripts are `q4fy23.txt`, `q4fy24.txt`, `q1fy25.txt` to `q4fy26.txt` and `q1fy27.txt`; the filings are `fy26_10k.htm` and `q1fy27_10q.htm`.

---

## 0. Hard numbers from filings (anchor table)

| Fiscal year | Jordan revenue ($M) | YoY | Basis / source | Status |
|---|---|---|---|---|
| FY2017 | 3,098 | | FY19 10-K p.27 | VERIFIED (repo) |
| FY2018 | 2,856 | -8% | FY19 10-K p.27 (the "FY18 reset" year) | VERIFIED (repo) |
| FY2019 | 3,138 | +10% | FY19 10-K p.27 | VERIFIED (repo) |
| FY2020 | 3,609 | +15% | FY20 10-K p.31 | VERIFIED (repo) |
| FY2021 | 4,711 (4,780 recast) | +31% | FY21 / FY22 10-K | VERIFIED (repo) |
| FY2022 | 5,122 | +7% | FY22 10-K p.32 | VERIFIED (repo) |
| FY2023 | 6,589 | +29% (+35% c-n) | FY23 10-K p.32, wholesale-equivalent basis | VERIFIED (repo) |
| FY2024 | 6,988 old basis; **8,701 recast** to reported-revenue basis | +6% (old basis) | FY24 10-K p.34; Q4 FY25 8-K Ex. 99.1 recast | VERIFIED (repo) |
| FY2025 | **7,270** | **-16%** | FY26 10-K: "sales of Jordan Brand products of $7,034 million, $7,270 million and $8,701 million in fiscal 2026, 2025 and 2024, respectively, decreasing 3% and 16% on a reported basis and decreasing 5% and 16% on a currency-neutral basis" | VERIFIED (re-opened FY26 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm) |
| FY2026 | **7,034** | **-3% (-5% c-n)** | same | VERIFIED |
| Q1 FY2027 (Jun to Aug 2026) | about 13% of Nike revenue; "revenue falling by mid-teens" | | Nike Q1 FY27 transcript, Oct 1, 2026 | VERIFIED (Nike transcript) |

- DERIVED: Nike Q1 FY27 revenue was about $11.2B, so Jordan was about $1.45B in the quarter at 13%. A share at the "Nike Inc. revenue" level is an assumption, since Hill said "13% of our global business".
- DERIVED: FY26 Jordan revenue was 19% below the recast FY24 peak ($7,034M vs $8,701M). If FY27 falls mid-teens, Jordan would be about $6.0B, roughly 30% below peak and near its FY2022 to FY2023 level.
- DERIVED: Jordan was 16.9% of Nike Inc. revenue in FY24 ($8,701M / $51,362M), 15.2% in FY26 ($7,034M / $46,398M) and about 13% in Q1 FY27.
- **Disclosure gap (SEC filing, VERIFIED):** FY26 10-K: "Sales and operating results for Jordan Brand products are reported within the respective NIKE Brand geographic operating segments." Nike discloses no Jordan EBIT, gross margin or inventory. **Every claim that Jordan is Nike's "highest-margin" business is unverifiable from filings.** I found no opened source supporting it (see Section 5).
- **Q1 FY27 10-Q (SEC filing, filed 2026-10-02, VERIFIED, re-opened):** "additional actions related to NIKE Sportswear and Jordan Brand are expected to extend beyond fiscal 2027. The need for these additional actions reflects, in part, higher levels of discounting and broader marketplace pressure experienced in these areas of our business." https://www.sec.gov/Archives/edgar/data/320187/000032018726000193/nke-20260831.htm

---

## 1. Retro cycle, oversupply, resale

### 1a. Management's own words, in chronological order (all Nike transcripts, VERIFIED, official PDFs at s1.q4cdn.com/806093406/files/doc_financials/...)

| Date | Call | Quote | Speaker |
|---|---|---|---|
| 2023-06-29 | Q4 FY23 | "Jordan grew mid-30s ... Jordan is on its way to becoming the second-largest footwear brand in North America." Also: "growth in performance footwear at Jordan is now outpacing retro footwear." And: "In most of our geos, Jordan penetration is about 10 points lower than it is in North America. This is the growth opportunity we plan to capture moving forward." | John Donahoe |
| 2024-06-27 | Q4 FY24 | "Back in Fiscal 18, we recalibrated the supply of select Jordan Brand franchises ... Over the subsequent quarters, we turned the page from double-digit declines in the Brand to the start of multiple consecutive years of strong double-digit growth." | Nike mgmt (Donahoe era) |
| 2024-10-01 | Q1 FY25 | "We have been intentionally reducing the proportion of our business driven by our Classics Footwear franchises, Air Force 1, Air Jordan 1, and Dunk ... In Q1, these franchises were down nearly 50% versus the prior year on NIKE Digital." "The Jordan brand was planned down double digits this quarter, and we expect Jordan to be down at the same rate for fiscal '25." | Matt Friend (CFO) |
| 2024-10-01 | Q1 FY25 Q&A | "Jordan is a big business in Greater China, and we're watching and managing that business carefully." | Nike mgmt |
| 2025-03-20 | Q3 FY25 | "declines in Nike sportswear and the Jordan brand, led by a double-digit decline in our classic footwear franchises" and "Air Force 1 inventory stabilize ... while Air Jordan 1 and Dunk remain elevated with continued actions planned ahead." Hill: "With AF1, Dunk and Air Jordan 1, it's about right-sizing, not sun-setting." | Friend; Hill |
| 2025-06-26 | Q4 FY25 | "we continue to rightsize Air Force 1, the AJ1 and the Dunk." | Hill |
| 2025-09-30 | Q1 FY26 | "Air Jordan one inventory levels are returning to health." | Hill |
| 2025-12-18 | Q2 FY26 | "Classic footwear franchises declining approximately 20% year-over-year" and "on track to decline from peak levels by more than $4 billion by fiscal year-end." Hill: "I've got to call Jordan out ... great sell-through of the AJ4 Black Cat ... that was our largest Black Friday ever ... the AJ11 Gamma, we had people lining up." Also: "Jordan, I think, still has some room to dimensionalize beyond Streetwear into things like Jordan Basketball, Jordan Training." | Friend; Hill |
| 2026-03-31 | Q3 FY26 | "intentionally reduced over $4 billion of revenue from the peak levels of classic footwear franchises." "the Air Force 1 and the AJ1, they stabilized this quarter ... month-to-month improvement in full price realization." "AJ11 Gamma, the AJ5 Wolf Grey ... had a high full price realization and really strong sell-through." Also: about a "5-point headwind this quarter of removing unhealthy inventory from those Classics". | Hill |
| 2026-06-30 | Q4 FY26 | "we're not living up to our full potential, particularly in NIKE Sportswear and Jordan Streetwear, where sell-through remains challenged, impacting both current discounting and future order books." "We expect Sportswear and Jordan Streetwear to continue to be negative this fiscal year with improvement expected in the back half ... together, they represent approximately half of our revenue." "As it relates to Sportswear and Jordan, we have taken $2 billion out of the market in FY '26 of our classic franchises." | Hill; Friend |
| 2026-10-01 | Q1 FY27 | "With Jordan Brand Footwear, we're going to get back to leading the scarcity model that we created. Simply put, we've been oversupplying our iconic retro product, asking them to do too much. And as we've done with the Air Jordan 1, we will deliberately reduce the volume and frequency of specific Jordan Retro launches. We've discussed it with our wholesale partners ... In the near term, North America will feel the biggest impact." "the Jordan Brand represented 13% of our global business with revenue falling by mid-teens." Q&A: "restoring the scarcity model for retro styles and you will see us dimensionalize the brand through sport ... our cleated business, our golf business, our training business." | Hill |
| 2026-10-01 | Q1 FY27 | "NIKE Sportswear and the Jordan Brand, including men's, women's and kids, represented a high single-digit drag on consolidated NIKE." Supply cuts "will create pressure on reported revenues for the remainder of fiscal '27 and into '28." | Dave Denton (CFO) |

**Key read (DERIVED from the quotes above):** the AJ1 cut (FY25 to FY26) appears to have pushed retro volume onto other numbered retros (AJ3, AJ4, AJ5, AJ11, AJ6). Management celebrated those launches in Dec 2025 and Mar 2026, then called retro "oversupplied" in Oct 2026. The AJ1 playbook is now being extended to the whole retro line, nine months after management cited those same retros as proof of recovery.

### 1b. Release-count and resale data

| Claim | Source | Type | Date | Status |
|---|---|---|---|---|
| Jordan averaged **10 retro releases a month** from Oct 2025 to Sep 2026; **19 in Feb 2026** (All-Star); AJ1 High retro colorways **20 (2021), 15 (2025), 12 (2026)**. Holiday 2026 is already set (Bred 4, Space Jam 11, Fireside 12). | Sneakz & Beatz essay relaying Sole Retriever counts, https://sneakzandbeatz.com/the-lane/nike-ceo-elliott-hill-jordan-retro-releases-cut-2027-back-to-scarcity-model-q1-fy27-earnings-call-october-1-2026 | secondary news relaying a data provider (Sole Retriever, methodology not given) | 2026-10-02 | VERIFIED on page (Sole Retriever original not opened) |
| Retro cuts expected to start in 2027 | same page (citing Hypebeast and Sole Retriever) | secondary news | 2026-10-02 | VERIFIED on page; timing is press inference, not a Nike statement |
| Hypebeast: AJ1 High releases "already halved", full cuts in 2027 | hypebeast.com/2026/10/nike-to-limit-air-jordan-retro-supply-moving-forward | secondary news | 2026-10 | SNIPPET ONLY (page returned empty) |
| StockX average resale premium on new **AJ1 Retro High** releases fell "from a high of 61 per cent in 2020 to 4 per cent in 2023"; Altan Insights data; Bernstein said investors worry Jordan is "losing steam" | Reuters via Cyprus Mail, https://cyprus-mail.com/2023/09/28/nike-air-jordans-are-losing-resale-value-is-sneaker-culture-moving-on ; also EconoTimes | secondary news (Reuters) citing data providers (StockX, Altan) and an analyst (Bernstein) | 2023-09-28 | VERIFIED |
| StockX: original 2018 Off-White AJ1 "Alaska" average resale **$4,231 (2024) to $2,855 (2025)**; 2026 V.A.A. AJ1 "Alaska" ($230 retail) averaged $710 on Mar 31, 2026, then $626 by Apr 6, 2026 | Complex, https://www.complex.com/sneakers/a/victor-deng/virgil-abloh-archives-air-jordan-1-alaska-resale-data-stockx | secondary news citing a data provider (StockX) | 2026-04-06 | VERIFIED. Caution: StockX attributes the 2025 drop to re-release rumors, not to brand weakness. |
| StockX Big Facts: AJ4 **+204% search traffic YoY**, most "favorited" sneaker on StockX; "the bubble has burst a bit on Jordan retros ... oversaturating the market with too many colorways" | DraftKings Network, https://dknetwork.draftkings.com/2025/11/25/air-jordan-4-black-cat-drops-november-28-where-to-buy-price-details-tinker-hatfield-michael-jordan-jordan-brand-retro-black-friday/ | secondary news relaying a data provider (StockX) | 2025-11-26 | VERIFIED on page (StockX report not opened) |
| Needham (Tom Nikic) cut PT $75 to $66; "rationalizing over-supplied product franchises (Jordan, Dunk)"; channel checks show "scarce" retro Jordans and Dunks "selling slowly" and discounted on StockX and GOAT | SGB Executive, https://sgbonline.com/exec-nike-faces-target-price-cut-from-needham-on-slow-recovery/ | analyst via secondary news | 2025-06-18 | VERIFIED |
| AJ6 "Oreo" 2026 ($215 retail) last sale $156, -27% premium; GS version -45% | stockx.com product page | data provider | 2026 | UNVERIFIED (page opened but prices did not load; snippet only) |
| Complex list of Jordans under retail (AJ3 Black Cement, AJ11 Legend Blue 2024, etc.) | complex.com | secondary news | undated | UNVERIFIED (host would not resolve) |
| Any broad 2025 to 2026 StockX, GOAT or Flight Club index of Jordan resale premiums | | | | NOT FOUND. No current, systematic resale index was found; the best systematic series (Altan, 61% to 4%) ends in 2023. |

---

## 2. Strategy under Sarah Mensah, athletes, verticals

| Claim | Source | Type | Date | Status |
|---|---|---|---|---|
| Mensah, President since June 1, 2023; first female Jordan president | Russell Reynolds podcast page, https://russellreynolds.com/en/insights/podcasts/outwork-the-competition-jordan-brands-winning-strategy-with-president-sarah-mensah ; repo note cites Nike profile | secondary; company profile | 2024-01-17 | VERIFIED |
| **Brazil:** Jordan away kit for Brazil's 2026 World Cup; Brazil is the first federation to partner with Jordan for a kit; Mensah: "Partnering with the Brazilian Football Federation is more than a collaboration; it's a celebration of greatness" | SI, https://www.si.com/soccer/brazil-slam-dunk-2026-world-cup-away-kit-jordan-collaboration/app/ | secondary news | 2026-03-13 | VERIFIED |
| Nike confirms "a Jordan Away kit for Brazil" | Q3 FY26 transcript | Nike transcript | 2026-03-31 | VERIFIED |
| Mensah: Jordan should sit where performance and lifestyle "meet"; "We've wanted to really go slow so that we can go fast"; no figures given | Complex interview, https://www.complex.com/sneakers/a/ben-felderstein/jordan-brand-brazil-football-soccer-world-cup-sarah-mensah-interview | secondary news (interview) | 2026-03-13 | VERIFIED |
| Mensah: "When Jordan enters a space, we do so intentionally"; growth "has to be done authentically, intentionally, and in a measured way" | SoccerBible, https://www.soccerbible.com/interviews/2026/03/sarah-mensah-takes-us-into-the-world-of-jordan-x-brazil/ | secondary news (interview) | 2026-03-23 | VERIFIED |
| **PSG:** Jordan x PSG (since 2018) extended "at least until 2027" (end of the 26-27 season); terms undisclosed; cites Le Parisien | Footy Headlines, https://www.footyheadlines.com/2024/12/jordan-to-continue-psg-kit-deal.html | secondary news (leak site) | 2025-04-17 | VERIFIED on page; no club or Nike confirmation found. A renewal decision is due by 2027. |
| **Golf:** Tony Finau moved from Nike to Jordan after about 10 years, debuting at the Jan 2026 Sony Open; Keegan Bradley is a Jordan shoe ambassador | PGA Tour, https://www.pgatour.com/pt/article/news/style-insider/2026/01/15/tony-finau-becomes-michael-jordan-jumpman-ambassador-bringing-the-court-to-the-course | secondary news | 2026-01-15 | VERIFIED |
| Hill: Jordan seeing "growth in our ... cleated business, our golf business, our training business"; golf grew double digits at Nike level | Q1 FY27 transcript | Nike transcript | 2026-10-01 | VERIFIED |
| **NFL:** Tetairoa McMillan (Panthers, No. 8 pick 2025) signed with Jordan, the first rookie WR to do so; roster includes Davante Adams, Jalen Hurts, Deebo Samuel | ClutchPoints, https://clutchpoints.com/sneakers/jordan-brand-signs-panthers-tetairoa-mcmillan | secondary news | 2025-05-16 | VERIFIED |
| **Women's:** Georgia Amoore (Mystics) signed May 7, 2026; Azzi Fudd NIL deal Mar 2026; roster lists Napheesa Collier (signed May 2025), Rhyne Howard, Kia Nurse | bookingagentinfo.com, https://bookingagentinfo.com/news/georgia-amoore-joins-jordan-brand-as-newest-wnba-athlete/ | secondary (low-tier) | 2026-05 | VERIFIED on page; low-quality outlet, so confirm the Collier and Fudd details elsewhere |
| Nike-level women's basketball: signature business grew "nearly 500% from FY 2022 to FY 2026"; Caitlin 1 is the "largest signature launch for women ever at 5,000 doors". These are **Nike** Basketball (Sabrina, A'ja, Caitlin), not Jordan | Q1 FY27 transcript | Nike transcript | 2026-10-01 | VERIFIED. Read: the women's signature growth engine sits in Nike Basketball, not Jordan. |
| **Zion:** Jordan reportedly ending Zion's signature line; Zion 4 (Jan 2025) the last; he stays on the roster until the deal ends later in 2026; original deal 7 yrs / $75M | Larry Brown Sports via Yardbarker, citing Sole Retriever, https://www.yardbarker.com/nba/articles/zion_williamson_is_losing_a_notable_endorsement_line/s1_127_43377400 | secondary news | 2026-01-24 | VERIFIED on page; no Nike confirmation |
| **Tatum:** ruptured Achilles in Game 4 vs Knicks (May 2025); returned Mar 6, 2026 after 298 days | Geo Super, https://www.geosuper.tv/latest/54080-jayson-tatum-makes-emotional-return-after-achilles-surgery | secondary news | 2026-03-07 | VERIFIED. Jordan's No. 2 signature athlete missed most of the 2025-26 season. |
| Luka extension with Jordan through 2029 (Marc Stein report) | Complex / Sportskeeda search results | secondary | c.2023 | SNIPPET ONLY |
| Luka 5 launched Jan 8, 2026 at $135; Tatum 4 "Bloodline" Nov 1, 2025 at $130 | search results (Sole Retriever, House of Heat) | data provider | 2025 to 2026 | SNIPPET ONLY |
| Jimmy Butler left Jordan (now wears Li-Ning per Curry quote below); Trae Young joined Jordan from adidas Nov 2024 | Highsnobiety, Complex | secondary | | SNIPPET ONLY |
| **World of Flight:** Philadelphia opened Oct 10, 2025 as the sixth flagship and first in the US, after Milan (2022), Seoul and Tokyo (2023), and Beijing and Mexico City (2024); "more World of Flight locations planned in key cities across the country" | Nike newsroom, https://about.nike.com/en/newsroom/releases/jordan-brand-world-of-flight-philadelphia | Nike release | 2025-10-02 | VERIFIED |
| Mexico City dual-brand World of Flight: "Q1 traffic and sales for this concept far exceeded our plan" | Q1 FY25 transcript | Nike transcript | 2024-10-01 | VERIFIED |
| World of Flight Osaka to open May 1, 2026 | prodism.jp | secondary | 2026 | SNIPPET ONLY |
| **China:** Q1 FY27 Greater China revenue -26%; Nike is anchoring "NIKE's and Jordan's digital marketplace in China" on fewer official flagships (Tmall, JD, Douyin) | Q1 FY27 transcript | Nike transcript | 2026-10-01 | VERIFIED. No Jordan-specific China figure is disclosed. |
| Nike: Jordan's "The One" tournament in 20 cities; Q4 FY24: Jordan "market share gains in basketball footwear" (APLA) | Q4 FY26 and Q4 FY24 transcripts | Nike transcript | 2026-06-30; 2024-06-27 | VERIFIED |

---

## 3. Michael Jordan's royalty

| Claim | Source | Type | Date | Status |
|---|---|---|---|---|
| Forbes: MJ earned $1.3B from Nike since 1984, including **$130M** in the last year; Jordan FY19 sales $3.1B | Fox Business, https://www.foxbusiness.com/sports/nike-jordan-brand-worth-sales | secondary news citing Forbes | 2020-05-04 | VERIFIED |
| Forbes: "His most recent annual royalty check from Nike was for **$260 million**"; net worth $3B, Forbes 400 No. 379 | CBS News, https://www.cbsnews.com/amp/news/michael-jordan-forbes-400-net-worth-3-billion | secondary news citing Forbes | 2023-10-03 | VERIFIED |
| Sportico: MJ "took an estimated **$275 million in 2025**, most of it from Nike"; career earnings $3.28B ($4.5B inflation-adjusted) | Billionaires.Africa citing Sportico, https://www.billionaires.africa/2026/09/19/billionaire-michael-jordan-tops-all-time-athlete-earnings-at-4-5-billion/ ; Yahoo Sports / HITC, https://sports.yahoo.com/articles/michael-jordan-nearly-walked-away-125257693.html (2026-06-19) | secondary news citing Sportico | 2026-09-19 | VERIFIED on secondary pages (Sportico original is paywalled via tollbit) |
| $330M in 2023 from "5% of the brand's royalties" | beIN Sports | secondary, no source given | c.2025-05-01 | VERIFIED on page but unsourced; conflicts with Forbes' $260M, so treat as weak |
| The royalty is "5% of Jordan Brand sales" | many blogs | | | **UNVERIFIED.** No opened page gives a primary source. Nike does not disclose it. |

- **DERIVED (implied rate):** $130M / $3.1B (FY19) = 4.2%; $260M / $6.6B (FY23) = 3.9%; $275M / $7.27B (FY25) = 3.8%. Sportico and Forbes estimates imply about 4% of reported Jordan revenue, below the folklore 5%. Possible reasons: the royalty is on wholesale or a narrower base, or the estimates are rough.
- **DERIVED (thesis point):** MJ's payout tracks Jordan revenue. A mid-teens FY27 decline cuts his take too, so the person behind the brand shares the pain of the volume reset, which helps alignment. If FY27 Jordan is about $6.0B, a 4% to 5% royalty would be about $240M to $300M.

---

## 4. Competition

| Claim | Source | Type | Date | Status |
|---|---|---|---|---|
| **adidas Q2 2026: basketball -21% currency-neutral**, "the steepest decline among the sports categories"; football +74%, running +28%, golf -10% | Merca2.0, https://www.merca20.com/?p=12600254 (citing the adidas investor presentation) | secondary news | 2026-09-01 (page date) | VERIFIED on page; adidas presentation not opened. Read: basketball softness is category-wide, not only a Jordan problem. |
| adidas Q2 2026 revenue +14% c-n to EUR 6.7B, a record; FY26 guide raised to +9% to 10% | search summary (Retail Gazette, Pulse2) | secondary news | 2026-07-30 | SNIPPET ONLY |
| **Stephen Curry signed a 10-year deal with Li-Ning (Jun 1, 2026)**, reported at over $400M (ESPN/Charania); covers basketball, athleisure and golf; "We have plans to launch Curry Brand stores together in China and the US" | WBTV, https://www.wbtv.com/2026/06/03/nba-superstar-stephen-curry-reaches-landmark-deal-with-chinese-sports-company-li-ning/ | secondary news | 2026-06-02 | VERIFIED. The deal value is a report, not disclosed. |
| Anta and Li-Ning together hold 28% of China sneaker sales; China fell from 22% of Nike sales (2018) to about 15% | CKGSB Knowledge, https://english.ckgsb.edu.cn/knowledge/article/how-anta-overtook-nike-in-chinese-sportswear-brands/ (citing BoF, Reuters) | secondary (business-school publication) | 2026-03-13 | VERIFIED on page; year of the 28% figure not stated |
| Domestic brands' China share rose from under 30% (2015) to about 50% (2025); Anta 21.8% | faxiangongchang.com, daxueconsulting | secondary (low-tier) | | SNIPPET ONLY |
| **Qiaodan:** China's Supreme People's Court (Dec 2016) found "malicious intent" and barred Qiaodan Sports (about 6,000 shops) from using the Chinese characters of Jordan's name; the romanized "Qiaodan" was allowed at that time | World Footwear, https://www.worldfootwear.com/news/michael-jordan-wins-trademark-battle-in-china/2161.html | secondary news | 2016-12-09 | VERIFIED |
| A 2020 ruling went further: Qiaodan can no longer use the romanized name, but keeps its silhouette logo | Cassius, https://cassiuslife.com/173372/michael-jordan-wins-lawsuit-qiaodan/ | secondary news | 2020-04-15 | VERIFIED on page (low-tier; checking the legal detail is advised) |
| Shanghai No. 2 Intermediate Court (Dec 30, 2020) found Qiaodan "did deliberately pick" the name 乔丹 | Norton Rose Fulbright blog, https://www.nortonrosefulbright.com/en/inside-sports-law/blog/michael-jordan-and-qiaodan-sports-name-rights-infringement | law-firm commentary | 2021-02-02 | VERIFIED |
| The 2020 remedies: RMB 300,000 damages plus RMB 50,000 costs and a public apology | search snippet | | | SNIPPET ONLY |
| Piper Sandler Fall 2024: Nike footwear mindshare 57% (from 61%); adidas 9%, New Balance 7%, On No. 7 | SGB Executive, https://sgbonline.com/exec-piper-sandlers-fall-survey-finds-continued-shifts-in-brands-winning-with-teens/ | data provider via secondary news | 2024-10-09 | VERIFIED |
| Circana or NPD basketball footwear share data for 2025 to 2026 | | | | NOT FOUND / UNVERIFIED. The "Nike plus Jordan 93% of US basketball shoes" figure seen in search has no source or date. |
| Sabrina 1 "taken two points of share across the entire U.S. basketball market" | Q4 FY24 transcript | Nike transcript | 2024-06-27 | VERIFIED (Nike claim) |

---

## 5. Analyst views

| Claim | Source | Type | Date | Status |
|---|---|---|---|---|
| Telsey: "an inflection back to sales growth is now not likely until calendar 2028, at the earliest" | Sherwood News, https://sherwood.news/snacks/newsletters/nikes-plan-to-make-jordans-cool-again/ | analyst via secondary news | 2026-10-05 | VERIFIED |
| Evercore ISI (Michael Binetti) cut Nike to In Line from Outperform, PT $57 to $46 | Newsquawk, https://www.newsquawk.com/headlines/us-broker-moves-tgt-upgraded-at-wolfe-nke-downgraded-at-evercore-isi-23-06-2026 | analyst via secondary news | 2026-06-23 | VERIFIED (rating and PT only) |
| Evercore's reasons included "struggling Jordan retro launches" | mexc.com | | 2026-06-23 | SNIPPET ONLY (page 410). Do not cite as verified. |
| Needham Jordan and Dunk oversupply note | see Section 1b | analyst | 2025-06-18 | VERIFIED |
| TD Cowen "Jordan retro fatigue", PT $78 to $73 | tipranks | analyst | c.late 2024 | SNIPPET ONLY |
| Bernstein: Jordan may be "losing steam" | Reuters via Cyprus Mail | analyst | 2023-09 | VERIFIED |
| **Sell-side Jordan revenue estimates, a standalone Jordan valuation, sum-of-the-parts models or spin-off speculation** | | | | **NOT FOUND** on any opened page. The online "Jordan worth $10B to $15B" figures come from unsourced SEO sites. |
| **"Jordan is Nike's highest-margin business"** | fourweekmba (claims 55% to 60% gross margin, unsourced) | | | **UNVERIFIED.** Nike does not report Jordan profit (10-K). Nike's own remarks point the other way: Jordan needs "higher levels of discounting" actions beyond FY27 (10-Q), and Denton said Sportswear and the Jordan and Converse brands must get "back to financial health" (Q1 FY27). |

---

## 6. Nike-stated Jordan milestones (company statements)

- Q4 FY23 (2023-06-29): "Jordan grew mid-30s"; "on its way to becoming the second-largest footwear brand in North America"; international penetration is "about 10 points lower" than North America. VERIFIED (Nike transcript).
- First $1B Jordan quarter, disclosed by Mark Parker (Q2 FY20). VERIFIED via Fox Business (2020-05-04).
- FY24 to FY26 figures and Q1 FY27 "13% ... falling by mid-teens": see Section 0.
- Classics: "more than $4 billion" off peak by FY26 end (Q2 and Q3 FY26); "$2 billion out of the market in FY '26" across Sportswear and Jordan (Q4 FY26). VERIFIED (Nike transcripts). Nike does not split this between AF1, Dunk and AJ1.

---

## 7. Brand heat

| Claim | Source | Type | Date | Status |
|---|---|---|---|---|
| Piper Sandler Fall 2025 (latest posted; 10,969 teens): Nike "No. 1 in all footwear, with mindshare starting to stabilize sequentially"; male share grew sequentially for the first time since fall 2022; On No. 4 passed HOKA No. 5. No Jordan line given. | pipersandler.com/teens | data provider | Fall 2025 | VERIFIED |
| Fall 2025 article: Nike "still lost a bit to Adidas, New Balance, and On"; teen spend -7% to $2,213 | SGI News, https://www.sginews.com/Content/teen-survey-finds-nike-stabilizing-as-spending-falls.aspx | data provider via secondary news | 2025-10 | VERIFIED |
| Piper Sandler moving to an annual survey, with the 2026 study due in the fall | SGB (search snippet) | | 2025 to 2026 | SNIPPET ONLY. No Spring 2026 edition was found. **The Fall 2026 release (usually mid-October) is a near-term catalyst to watch.** |
| Spring 2025: Nike footwear share 49% vs 60% average in 2022 to 2023 | search snippet | | 2025-04 | SNIPPET ONLY |
| Lyst Index Q2 2026: no Nike or Jordan in the top 20 brands or top 10 products (Chanel No. 1; top product a Knicks cap; adidas only via a Willy Chavarria jersey) | Lyst, https://www.lyst.co.uk/the-lyst-index/q2-26/ | data provider | Q2 2026 | VERIFIED |
| Google Trends for "jordans", "air jordan" | trends.google.com | data provider | | **UNVERIFIED**: the API returned HTTP 429. Pull it manually in a browser. |

---

## 8. Could not open (excluded from conclusions)

Benzinga transcript (403), Sportico pieces (tollbit paywall), Hypebeast Oct 2026 (empty), Kicks Crew (403), Malay Mail (403), AOL (404), StockX price history (did not load), sgieurope (405), mexc Evercore detail (410), Khaosod and SportBusiness Qiaodan pieces (403), Google Trends (429).
