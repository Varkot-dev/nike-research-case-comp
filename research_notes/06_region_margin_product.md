# Channel, region, margin and product: where Nike makes its money (FY2019 to Q1 FY2027)

**Prepared:** October 13, 2026. **Companion to** `05_channel_split.md`, which covers the NIKE Direct versus wholesale revenue split itself. This note asks the follow-on questions: which regions earn the best margins, whether a higher Direct share goes with better margins, how product categories are moving, and what new product Nike is relying on.

**Sources.** Segment revenue, channel split, EBIT and gross margin come from `data/nike_filing_facts.csv` and `data/nike_channel_split.csv`, joined by `scripts/build_region_channel.py` into `data/nike_region_profitability.csv`, which carries the filing and page for each input. EBIT margin and Direct share are **my arithmetic** on those reported figures. Chart: `charts/15_region_ebit_margin.png`. Page numbers are printed pages.

**What Nike does not disclose.** No filing gives profit or gross margin by channel (Direct versus wholesale), or product category by channel. Every statement below about channel profitability is either Nike's own gross margin bridge language or **my inference**, and is labelled as such.

## 1. Regional profitability: the ranking has flipped

Segment EBIT as a share of segment revenue (my arithmetic). Segment EBIT excludes Global Brand Divisions and Corporate costs, so these margins are higher than Nike's consolidated EBIT margin.

| Fiscal year | North America | EMEA | Greater China | APLA | Converse |
|---|---|---|---|---|---|
| FY2019 | 24.7% | 20.3% | 38.3% | 25.2% | 15.9% |
| FY2021 | 29.6% | 21.3% | 39.1% | 28.6% | 24.6% |
| FY2023 | 25.2% | 26.3% | 31.5% | 30.0% | 27.9% |
| FY2024 | 27.2% | 24.9% | 30.6% | 28.0% | 22.8% |
| FY2025 | 24.2% | 21.0% | 24.3% | 24.4% | 14.2% |
| FY2026 | 26.2% | 19.2% | 21.9% | 22.2% | 1.5% |
| Q1 FY2026 | 22.6% | 22.1% | 24.9% | 23.5% | 10.7% |
| Q1 FY2027 | 22.8% | 22.9% | 21.0% | 22.1% | 9.5% |

Inputs: segment notes of the FY2019 to FY2026 10-Ks and the Q1 FY2026 and Q1 FY2027 10-Qs (Q1 FY27 10-Q p. 25); full citations per row in `data/nike_region_profitability.csv`.

- **Greater China went from Nike's most profitable region to one of its least.** EBIT fell from $3,243 million in FY2021 to $1,278 million in FY2026 (FY21 10-K; FY26 10-K), a 61% decline on revenue down 29% (my arithmetic). In Q1 FY2027 it was the only major region where EBIT margin fell sharply (24.9% to 21.0%).
- **North America is now the most profitable region**, at 26.2% in FY2026. Caveat: FY2026 North America EBIT includes **$965 million** of expected IEEPA tariff recovery, and Converse includes **$21 million** (FY26 10-K p. 30). Nike says the recovery "largely offsets the impact of the IEEPA tariffs recognized during fiscal 2026" (Q4 FY26 release pp. 4 to 5), so the reported figure is roughly a no-tariff view. Excluding the recovery entirely, North America's FY2026 EBIT margin would be **21.5%** (($5,376M minus $965M) / $20,511M, my arithmetic), which is the with-tariffs view.
- **Converse has almost stopped earning money.** Revenue fell from $2,427 million (FY2023) to $1,174 million (FY2026), down 52%, and EBIT from $676 million to $18 million (FY23 and FY26 10-Ks, my arithmetic). Without the $21 million tariff recovery, FY2026 Converse EBIT would be about **-$3 million** (my arithmetic).
- **EMEA has the lowest Direct share and, in FY2026, the lowest margin of the four Nike Brand regions** (19.2%), but it improved in Q1 FY2027 (22.9%) on a 140 bps gross margin gain (Q1 FY27 10-Q p. 27).

## 2. Gross margin by region (disclosed only from FY2023)

Nike began disclosing segment gross margin in the FY2025 10-K, with FY2023 comparatives.

| Fiscal year | North America | EMEA | Greater China | APLA | Converse | Source |
|---|---|---|---|---|---|---|
| FY2023 | 42.2% | 45.3% | 51.0% | 48.1% | 53.8% | FY25 10-K pp. 38 to 42 |
| FY2024 | 44.4% | 44.2% | 50.2% | 45.9% | 52.5% | FY26 10-K pp. 37 to 41 |
| FY2025 | 43.5% | 43.2% | 46.0% | 44.0% | 48.7% | FY25 10-K pp. 38 to 42 |
| FY2026 | 45.6% | 41.8% | 45.7% | 42.0% | 43.8% | FY26 10-K pp. 37 to 41 |
| Q1 FY2027 | 43.4% (+110 bps) | 44.4% (+140 bps) | 47.5% (+30 bps) | 42.3% (-150 bps) | 45.2% (-210 bps) | Q1 FY27 10-Q pp. 26 to 30 |

- **North America is the only region whose FY2026 gross margin is above FY2023**, and it is also the region that has moved furthest toward wholesale (Section 3). Every other region and Converse is down 400 to 1,000 bps since FY2023.
- **Greater China still has the highest gross margin of the Nike Brand regions** (45.7% in FY2026), yet its EBIT margin is below North America's. That gap points to operating cost deleverage (fixed store and marketing costs on falling revenue), not pricing alone (my inference).

## 3. Does more Direct mean better margins? Not on the evidence

FY2026, ranked by Direct share (my arithmetic on FY26 10-K p. 83 and the segment pages above):

| Segment | Direct share | Gross margin | EBIT margin |
|---|---|---|---|
| Greater China | 44.3% | 45.7% | 21.9% |
| Converse | 44.1% | 43.8% | 1.5% |
| North America | 41.7% | 45.6% | 26.2% |
| APLA | 39.5% | 42.0% | 22.2% |
| EMEA | 32.7% | 41.8% | 19.2% |

- **Across regions there is no clean pattern.** The two most Direct-heavy segments (Greater China, Converse) are the ones whose profits fell hardest.
- **Within North America, Direct share fell from 48.6% (FY2024) to 41.7% (FY2026) while gross margin rose from 44.4% to 45.6%.** Over the same period, Nike's bridge language shifted from Direct helping margin (FY2022: "higher margin in our NIKE Direct business," FY22 10-K p. 34) to wholesale mix lowering costs (FY2026: "Lower warehousing and logistics costs ... primarily due to channel mix," +20 bps, FY26 10-K p. 34; Q1 FY2027: +90 bps, Q1 FY27 10-Q p. 23).
- **Tested in `09_channel_margin_test.md`.** Nike's own numbers support the full-price condition at the gross margin level:
  - The Direct line in Nike's gross margin bridge added 160 bps to company gross margin in 9M FY2022, when promotions were low. It subtracted 130 bps in 9M FY2023 when Direct liquidated inventory, a swing of about $1.05 billion of gross profit (Q3 FY22 10-Q p. 30; Q3 FY23 10-Q p. 29).
  - Direct revenue over its internal wholesale-price cost peaked at 1.78x in FY2022 and fell back to 1.65x by FY2024.
  - **Peer check (that note, Test 3):** discounting does not erase Direct's *gross margin* lead. Skechers' DTC gross margin stays 17 to 30 points above wholesale. What discounting erases is the *operating* lead:
    - Deckers' DTC earned 3.8 to 5.0 points less than wholesale until full-price selling returned.
    - On a Foot Locker-sized cost to serve, Nike Direct's cushion runs out at an average markdown of roughly 8% to 16% (derived; Nike does not disclose markdown depth).

## 4. Product categories

| | FY2024 | FY2025 | FY2026 | Change FY24 to FY26 | Q1 FY2027 vs Q1 FY2026 | Source |
|---|---|---|---|---|---|---|
| Footwear ($M) | 33,427 | 29,510 | 29,525 | -11.7% | 6,951 vs 7,410 (-6.2%) | FY24 10-K p. 34; FY25 10-K p. 33; FY26 10-K p. 32; Q1 FY27 10-Q p. 22 |
| Apparel ($M) | 13,775 | 12,965 | 13,449 | -2.4% | 3,384 vs 3,313 (+2.1%) | same |
| Equipment ($M) | 2,075 | 2,191 | 2,199 | +6.0% | 611 vs 630 (-3.0%) | same |
| Jordan Brand ($M) | 6,988 | 7,270 | 7,034 | +0.7% | n/a | FY24 10-K p. 34; FY25 10-K p. 33; FY26 10-K p. 32 |
| NIKE Brand Digital ($B) | 12.1 | 9.6 | 8.6 | -29% | 1.8 vs 2.0 | FY24 10-K p. 35; FY25 10-K p. 34; FY26 10-K p. 33; Q1 FY27 10-Q p. 23 |
| Nike-owned stores ($B) | n/a | 9.2 | 9.1 | n/a | 2.3 | FY26 10-K p. 33; Q1 FY27 10-Q p. 23 |

Percentage changes are my arithmetic.

- **The decline is a footwear problem.** Footwear accounts for almost all of the revenue lost since FY2024; apparel is roughly flat and growing again in Q1 FY2027. Currency-neutral, FY2026 footwear was -2% and apparel +2% (FY26 10-K p. 32).
- **Nike is still cutting classic franchises.** The Q1 FY2027 release announced new actions to "reposition NIKE Sportswear, Jordan Brand, and Greater China" (Q1 FY27 release p. 1), and the 10-Q says "additional actions related to NIKE Sportswear and Jordan Brand are expected to extend beyond fiscal 2027" (Q1 FY27 10-Q p. 20).

## 5. Converse: what happened

**Summary of drivers (my arithmetic on the figures in the table below):**
- **Revenue fell $1,253 million (-52%) from FY2023 to FY2026, and about 85% of that decline is volume.** Units fell 12%, 12% and 31% in FY2024, FY2025 and FY2026, a cumulative unit index of about 0.53. Price (ASP) fell about 3%, 6 points and 1 point, an index of about 0.90. Units times price gives 0.48, which matches reported revenue (1,174 / 2,427 = 0.48). Volume accounts for about 86% of the log decline. This is approximate: Nike reports ASP as percentage-point contributions on a currency-neutral basis.
- **Gross profit fell about $792 million, from about $1,306 million to about $514 million** (revenue times segment gross margin).
  - About $674 million is lost volume at the FY2023 margin.
  - About $117 million is the 10-point gross margin decline on FY2026 revenue. Nike attributes that decline to "higher discounts" in FY2024 and FY2025, and to discounts plus "inventory obsolescence reserves and employee severance costs" in FY2026.
- **Costs below gross profit fell only 21%** while revenue fell 52%. These costs, gross profit minus EBIT, cover demand creation, overhead and other items. They went from about $630 million to about $496 million, so they rose from 25.9% to 42.3% of revenue. That deleverage is why EBIT fell 97%, from $676 million to $18 million.
- **The fixed-cost base is still large for the business it serves.** The store base has only partly adjusted: 60 U.S. and 54 non-U.S. Converse stores at May 31, 2026, down from 82 and 54 three years earlier (10-Ks pp. 2 to 3), on 48% of FY2023 revenue.

| | FY2023 | FY2024 | FY2025 | FY2026 | Q1 FY2027 | Source |
|---|---|---|---|---|---|---|
| Revenue ($M) | 2,427 | 2,082 | 1,692 | 1,174 | 263 (-28%) | FY23 10-K p. 32; FY24 10-K p. 38; FY25 10-K p. 33; FY26 10-K p. 32; Q1 FY27 10-Q p. 25 |
| Direct to consumer ($M) | 974 | 832 | 694 | 477 | 97 (-33%) | FY23 10-K p. 41 to FY26 10-K p. 41; Q1 FY27 10-Q p. 30 |
| Wholesale ($M) | 1,299 | 1,098 | 875 | 605 | 144 (-26%) | same |
| Units sold, change | n/a | -12% | -12% | -31% | -34% | FY24 10-K p. 43; FY25 10-K p. 43; FY26 10-K p. 42; Q1 FY27 10-Q p. 31 |
| Gross margin | 53.8% | 52.5% | 48.7% | 43.8% | 45.2% | FY25 10-K p. 42; FY26 10-K p. 41; Q1 FY27 10-Q p. 30 |
| EBIT ($M) | 676 | 474 | 240 | 18 | 25 | FY23 10-K p. 36; FY24 10-K p. 38; FY25 10-K p. 37; FY26 10-K p. 36; Q1 FY27 10-Q p. 25 |
| U.S. Converse stores (May 31) | 82 | 81 | 78 | 60 | n/a | 10-Ks pp. 2 to 3 |

Revenue has fallen for 13 consecutive quarters, from Q1 FY2024 to Q1 FY2027 (quarterly figures in `data/nike_filing_facts.csv`).

**Three phases, in Nike's own words:**
1. **FY2024: demand fades in the West.** "Converse revenues decreased 15% on a currency-neutral basis primarily due to declines in North America and Western Europe ... ASP decreased 3%, primarily driven by increased promotional activity in direct to consumer." Asia DTC was still growing (FY24 10-K p. 43).
2. **FY2025: discounting spreads to every region.** "Converse revenues decreased 18% on a currency-neutral basis driven by revenue declines across all territories ... Lower ASP per unit primarily reflects higher discounts in direct to consumer." Gross margin fell about 380 bps "due to lower ASP" (FY25 10-K p. 43).
3. **FY2026 onward: a deliberate reset.** "Converse is in the midst of a strategic reset of the brand and marketplace. We expect negative impacts from Greater China and Converse to continue throughout fiscal 2027" (FY26 10-K p. 30). Units fell 31%, DTC fell 33% "reflecting reduced traffic in all territories," and gross margin fell 490 bps including "brand and marketplace reset costs, including higher inventory obsolescence reserves and employee severance costs." Brand marketing spend ("demand creation") was cut 39% (FY26 10-K p. 42) and a further 58% in Q1 FY2027 (Q1 FY27 10-Q p. 31). The Q1 FY2027 10-Q says the Converse actions "are expected to continue throughout fiscal 2027" (p. 20). Nike gives no date for a return to growth.

**First sign of a floor:** in Q1 FY2027, "higher ASP contributed approximately 6 percentage points of revenue growth ... primarily due to product mix and lower discounts" (Q1 FY27 10-Q p. 31). Converse is selling far fewer pairs, but at better prices.

**Profit math (my arithmetic):** Converse kept about $28 of operating profit per $100 of sales in FY2023 and about $1.50 in FY2026. FY2026 EBIT of $18 million includes a $21 million tariff recovery (FY26 10-K p. 30), so underlying FY2026 EBIT was about -$3 million.

**Management commentary (Nike-posted earnings call remarks, titled "UNOFFICIAL Transcript," on Nike's investor site; PDF page numbers):**
- Q1 FY2026 (Sept 2025), CEO Elliott Hill: "the Chuck Taylor is in the early stages of a global market reset. With Converse, we just put new leadership in place and we're going to take aggressive actions" (p. 6).
- Q3 FY2026 (Mar 2026), Hill: "Converse will remain an important part of the NIKE, Inc. family" (p. 7). CFO Matt Friend: "We also rightsized operating costs at Converse this quarter" (p. 9).
- Q4 FY2026 (June 2026), Hill: Converse will grow "especially with the Chuck Taylor and Jack Purcell franchises," and Shai Gilgeous-Alexander has moved to Nike Basketball so "Converse [can] fully focus on serving creators through its lifestyle business" (p. 5).
- Q1 FY2027 (Oct 2026), Hill on lifestyle generally: "there's a lack of energy in the lifestyle space right now, which is impacting traffic" (pp. 3 to 4).

**Outside context (secondary, pages opened Oct 13, 2026):**
- **Leadership:** CEO Jared Carver left in July 2025 after about two years. He was replaced by Aaron Cain, a 21-year Nike veteran (Retail Dive, Jul 11, 2025, https://www.retaildive.com/news/nike-names-aaron-cain-ceo-converse-jared-carver-exits/752800/; WWD, Jul 10, 2025).
- **Layoffs:** a restructuring with layoffs was announced in February 2026, with no headcount given (FashionUnited, Feb 10, 2026, citing Bloomberg, https://fashionunited.uk/news/business/converse-initiates-restructuring-and-layoffs-amid-slumping-sales/2026021086196). An earlier round took place in May 2024 (RetailDetail, Feb 11, 2026).
- **Analyst diagnosis:** "There was an over-dependency on the Chuck Taylor shoe," according to Laurent Vasilescu of BNP Paribas (Boston Globe, Mar 31, 2026, https://www.bostonglobe.com/2026/03/31/business/nike-converse-authentic-brands/).
- **Sale speculation:**
  - Authentic Brands Group reportedly expressed interest in buying Converse "if it's put up for sale," but Nike "hasn't engaged in discussions" (same article).
  - Hill: "we're committed to the Converse brand" (same article, quoting Bloomberg TV).
  - Treat any sale scenario as speculation.
- **Product response:** three new Chuck Taylor models for 2026 (Throwback, Lo, Run Star Crush) (HIGHXTAR, Jan 12, 2026, https://highxtar.com/en/converse-updates-the-chuck-taylor-legacy-for-2026/).
- **Not verified, do not use:**
  - That New Balance or the Adidas Samba took Converse's customers. Only one opinion column makes the Samba point.
  - The February 2026 layoff headcount.
  - The Investor Day dates. The Q1 FY27 call confirms only "Investor Day in November."

**For the case (my inference):** Converse is about 2.5% of Nike's revenue (FY26 10-K p. 32, my arithmetic), so it does not explain Nike's overall decline. It is a portfolio decision: fix it (Chuck Taylor refresh, fewer stores, full-price discipline), shrink it into a licensing-style business, or sell it. Nike's own November Investor Day is the next point where management may say which.

## 6. New products

Full table (40 launches), verbatim quotes and source URLs: `research_notes/07_new_products_detail.md`. Converse detail: `research_notes/08_converse_detail.md`. Sources are Nike newsroom pages (about.nike.com), Nike-posted earnings call remarks (PDFs titled "UNOFFICIAL Transcript" on s1.q4cdn.com/806093406, labelled here as *Nike release*) and opened trade press (*secondary*). These are company statements, not independent evidence of performance. Earnings releases and 10-Qs name almost no individual products.

**The pipeline is running-led, and most launches go to both channels at once.**

| Product | Launch | Channel | Geography | What Nike says about results |
|---|---|---|---|---|
| Vomero 18 (max-cushion running) | Feb 2025 | nike.com and select retailers | Global | "in just over 90 days has already become a $100 million dollar plus franchise" (Q4 FY25 call); Vomero "nearly tripled our share of the Max Cushioning category" (Q1 FY27 call) |
| Vomero Premium | Oct 2025 | **Wholesale first:** "select retail partners October 2 and globally October 16" | Global | n/a |
| Structure Plus (stability running) | Jan 2026 | **Wholesale first:** "exclusively at running specialty stores worldwide January 8, 2026," nike.com from Feb 5 | Global | n/a |
| Pegasus 42 | Apr 2026 | nike.com and retailers; full rollout at Fleet Feet (285+ U.S. stores, secondary) | Global | n/a |
| NikeSKIMS (women's training) | Sep 2025 | Nike and SKIMS sites and stores first, wholesale partners in 2026 expansion | U.S., then EMEA and APLA from early 2026 | "early consumer response was very strong" |
| Nike Mind 001/002 (new footwear platform) | Jan 2026 | nike.com and select stores | Global | "sold out in all geographies"; production doubled |
| A'One (A'ja Wilson) | May 2025 | SNKRS, nike.com, select retail | Global | "sold out in 3 minutes on Nike Digital in North America" |
| Caitlin 1 (Caitlin Clark) | Oct 2026 | 5,000 doors, "twice the average for a Nike Basketball signature shoe" | **China first** (Sep 24), then global | "largest women's signature shoe launch in Nike's history" (Q1 FY27 call) |
| LeBron XXIII; Nike Hybrid RN | Sep to Oct 2025; Oct 2026 | nike.com and select retail | **China first**, then global | n/a |
| Mercurial boot; Aero-FIT World Cup kits | Jun 2026; Mar 2026 | Direct and wholesale (5,000+ elevated football doors) | Global | Mercurial "the fastest-selling 24-hour launch for cleated footwear in the history of Nike Direct"; kits sold 2.5x the 2022 World Cup by kick-off |
| Air Max 95 and 24.7 training | 2025 | **Partner-specific:** "Two wholesale partnership examples this quarter were with Dick's through our 24.7 training collection and with JD through the Air Max '95" (Q4 FY25 call) | Mainly U.S. and UK partners | Air Max 95 "strong sell-through" (Q3 FY26 call) |
| Nike on Amazon | Fall 2025 | **New wholesale channel** (brand store) | U.S. | "stronger engagement and sales than anticipated" (Q1 FY26 call) |

**What is being cut:** Nike "reduced revenue from the Dunk by nearly 50% in the quarter," a roughly $200 million Sportswear headwind, and is reducing Jordan retro launches (Q1 FY27 call). This matches the 10-Q's statement that NIKE Sportswear and Jordan actions extend beyond FY2027 (Q1 FY27 10-Q p. 20).

**How product is allocated between channels (Nike's words):** "For years, we were running a Nike direct-first offense. Now, we are rebalancing our offense through an integrated, elevated marketplace" (Q3 FY26 call). In practice:
- **Wholesale is segmented by type:** Dick's and Academy for sporting goods, Foot Locker and JD for athletic specialty, plus running specialty, football specialty and city specialty partners.
- **Nike Direct becomes the "premium destination,"** with fewer promotion days.
- **Greater China is going the other way.** From January 2027, online sales there narrow to Nike's own channels and its flagships on Tmall, JD.com and Douyin (Q1 FY27 call; Just Style, secondary).

**Read-across (my inference):**
- **Running and women's basketball are the only categories with stated growth, and the figures are management's, not reported.** Nike says running posted "five consecutive quarters of double-digit growth," adding "roughly a Billion dollars," and that its women's signature basketball business grew "nearly 500% from FY 22 to FY 26" (Q1 FY27 call). Neither figure appears in a filing, so neither can be reconciled to reported revenue. Reported footwear revenue is still down 6.2% in Q1 FY2027 (Section 4).
- **Wholesale gets new performance product early or exclusively.** The Structure Plus and Vomero Premium windows show this, which is consistent with North America wholesale growth in Section 3 and `05_channel_split.md`.
- **Greater China gets launch priority despite its decline.**
  - Three of the 40 launches in the detail file released in China one to two weeks before the global date: LeBron XXIII, Nike Hybrid RN and Caitlin 1. The Swooshfly is planned the same way.
  - Over the same period, Greater China wholesale fell 28% (Q1 FY2027, `05_channel_split.md` Section 4), and its EBIT margin fell from 24.9% to 21.0% (Section 1).
  - Whether China-first launches lift China sell-through cannot be measured from Nike's disclosures.
- **Not verified:** a Nike Hyrox partnership, any China-only product, and a Total 90 performance boot. Only a T90 x Palace collaboration is confirmed.

## 7. What this means for the thesis (my inference)

1. **North America's numbers are the only evidence that the wholesale pivot can coincide with better margins.** From FY2024 to FY2026:
   - Its Direct share fell from 48.6% to 41.7%.
   - Gross margin rose from 44.4% to 45.6%.
   - EBIT margin went from 27.2% to 26.2% reported, or 21.5% excluding the $965 million tariff recovery.
   - FY2026 wholesale grew 14% (FY26 10-K p. 37).

   The gross margin gain therefore did not carry through to EBIT on a with-tariffs basis. Any argument that the strategy works must show both figures.
2. **Greater China had the largest reported EBIT decline of any segment from FY2024 to FY2026**, -$1,031 million, against -$971 million for EMEA, -$498 million for APLA, -$456 million for Converse and -$446 million for North America. Excluding the tariff recovery, North America's decline would be larger at -$1,411 million (FY24 and FY26 10-Ks; my arithmetic).
   - **Sensitivity:** if Greater China's EBIT margin returned to its FY2024 level of 30.6% on FY2026 revenue of $5,847 million, segment EBIT would be about **$511 million higher**. That equals 13% of FY2026 total EBIT of $3,850 million.
3. **Converse accounts for $456 million of the FY2024 to FY2026 EBIT decline** on 2.5% of FY2026 revenue. Underlying EBIT is about -$3 million, and the reset is guided to last through FY2027 (Section 5).
   - **Fix-or-exit test:** assume FY2026 costs below gross profit stay at about $496 million. Returning to FY2024 EBIT of $474 million then needs gross profit of about $970 million:
     - At the FY2023 gross margin of 53.8%, that takes about $1.80 billion of revenue, 54% above FY2026.
     - At the FY2026 gross margin of 43.8%, it takes about $2.21 billion, 89% above FY2026.
     - Q1 FY2027 revenue was still falling 28%.
   - **Sale value:** the only sale benchmark on record is an opinion column citing a Morningstar estimate of 1 to 2 times sales (secondary). That implies $1.2 billion to $2.3 billion on FY2026 revenue.
4. **Channel margin is the missing number.** Any recommendation that depends on "wholesale is more profitable than Direct" must say this is inferred from Nike's bridge language, because Nike does not disclose it.
