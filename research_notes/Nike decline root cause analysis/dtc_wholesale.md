# Root cause test: did the DTC pivot and wholesale account cuts cede shelf space and cause Nike's share loss?

Research date: 2026-10-13. Hypothesis under test: *The 2017 to 2023 direct-to-consumer pivot (Consumer Direct Offense, then Consumer Direct Acceleration) and the cutting of wholesale accounts gave shelf space to competitors and caused the share loss.*

Status labels: **OPENED** = I read the page or filing myself in this session. **OPENED (repo)** = opened by an earlier researcher and recorded in this repo's notes; reused, not re-fetched. **SNIPPET** = seen only in a search-result summary. Filing numbers come from `data/nike_filing_facts.csv`, `data/nike_channel_split.csv` or the 10-K text I downloaded from EDGAR in this session. Where a 10-K page is marked "(page from footer markers)", I inferred the printed page from the "FORM 10-K nn" or "nn Table of Contents" footer that precedes the quote in the EDGAR text. All arithmetic is mine and labelled.

## 1. Bottom line

**Verdict: contributing cause (an enabler), not the primary cause of the FY2025 to FY2027 decline.**

- The account cuts were real and large (Nike "exited about 50%" of retail partners by Sept 2021) and they demonstrably handed distribution to On, Hoka and New Balance between 2020 and 2023. Foot Locker cut Nike from 75% of its purchases (2020) to 59% (2024); On's CFO said Nike's move "clearly increases the opportunity"; Hoka entered Foot Locker in July 2022.
- But the predictions that discriminate between "shelf space caused the loss" and the alternatives mostly fail:
  1. **Channel:** from FY2024 to FY2026 NIKE Brand wholesale fell only $305M while NIKE Direct fell $3,799M; NIKE Brand Digital alone fell $3.5B, about 71% of the $4,964M revenue decline.
  2. **Geography:** the region with the biggest DTC pivot (North America) had the smallest decline, and the region with the smallest pivot (Greater China) had the largest. The rank correlation across the four NIKE Brand geographies is perfectly inverse (n = 4).
  3. **Timing:** Nike's US share was roughly flat during the peak account-cut years (GlobalData: 35.4% in 2021, 34.97% in 2023). Euromonitor shows a bigger loss *before* the 2020 acceleration (40.5% in 2016 to 34.1% in 2019) than after it (to 28.9% in 2025).
  4. **Reversal:** Nike has already bought the shelf back in North America. NA wholesale hit a record $11,958M in FY2026 (+14% currency-neutral, "including expanded distribution"), yet total revenue is still falling and Euromonitor puts 2025 US share at its lowest.
  5. **Challengers' own channels:** Hoka's DTC grew 9x (FY2020 to FY2024) and On's 14x (2019 to 2024), faster than their wholesale (4x and 7x). That is consumer pull, not just shelf push.
- **Best reading:** the account cuts lowered the barrier to entry for challengers whose rise was driven by a running and comfort product cycle Nike missed. The share actually moved when Nike's own product demand failed (classics over-supplied through Nike's own digital channel, digital traffic falling). The wider DTC strategy matters a lot, but through a different mechanism: the over-built, promotion-dependent digital business is now unwinding. Shelf space ceded to competitors is a secondary symptom of that strategy.

## 2. Predictions and results

| # | Prediction if the hypothesis is true | What the data show | Held? |
|---|---|---|---|
| P1 Timing | Share loss starts or accelerates after the account cuts (2017 CDO; cuts in 2018 to 2022) and is concentrated in 2020 to 2023 | Euromonitor US athletic footwear (company shares): Nike 40.5% (2016), 34.1% (2019), 28.9% (2025). That is about 2.1 pts a year lost in 2016 to 2019 (before CDA) and about 0.9 pts a year in 2019 to 2025 (my arithmetic). GlobalData US sports footwear: 35.4% (2021), 35.37% (2022), 34.97% (2023), essentially flat during the peak cut years. Bridging the two (different scopes, caution), most of the post-2019 loss falls in 2024 to 2025, *after* Nike started reopening accounts in 2023. | **No** (partly: challenger door gains do date to 2020 to 2023) |
| P2 Channel | The revenue decline is led by wholesale (lost shelf) | FY2024 to FY2026: NIKE Brand wholesale 27,758 to 27,453 (-305); NIKE Direct 21,519 to 17,720 (-3,799) (FY24 10-K p. 34; FY26 10-K p. 32). NIKE Brand Digital $12.1B (FY24) to $9.6B (FY25) to $8.6B (FY26), -$3.5B, about 71% of the $4,964M total decline (my arithmetic). FY2025 10-K: results "reflected a decrease in traffic across NIKE Direct" | **No** |
| P3 Geography | Bigger declines where the DTC pivot and account cuts were biggest (North America) | DTC share of segment revenue FY2019 to FY2024 and revenue change FY2024 to FY2026 (my arithmetic on 10-K segment tables): NA +17.0 pts, -4.1%; APLA +12.9 pts, -7.2%; EMEA +9.2 pts, -7.6%; Greater China +3.5 pts, -22.5%. The ranking is exactly inverse. Converse (+12.4 pts) fell 44%, with wholesale and DTC both down. | **No** (inverse) |
| P4 Competitor channel | Challenger gains come through wholesale at accounts Nike vacated, timed with the cuts | Hoka wholesale $277M (FY2020) to $1,126M (FY2024); On wholesale CHF 200.7M (2019) to CHF 1,375.5M (2024). On co-CEO Hoffmann (Mar 2022): Nike's move "clearly increases the opportunity". Hoka first entered a Foot Locker store July 2022. Foot Locker non-Nike comps up about 30% in a quarter while Nike comps declined (Axios, Mar 2022). Jefferies (Aug 2025): "much of On's past wholesale growth came while Nike pulled back". **But** Hoka DTC grew 9.0x FY2020 to FY2024 vs wholesale 4.1x; On DTC 14.2x 2019 to 2024 vs wholesale 6.9x (my arithmetic). Demand followed the brands into their own channels. | **Partly** |
| P5 Retailer behaviour | Retailers whose Nike allocation was cut shift buys to rivals; favoured "strategic" partners do not | Foot Locker Nike share of purchases: 68% (2016), 67% (2017), 66% (2018), 71% (2019), 75% (2020), 68% (2021), 65% (2022), 65% (2023), 59% (2024); 10-K filed Mar 2022: "we do not expect any one supplier to represent more than 55%". Dick's (a favoured partner): 18% (FY2017), 19% (FY2018), 21% (FY2019), 19% (FY2020), 17% (FY2021), 23% (FY2022), 24% (FY2023), 25% (FY2024), 31% (FY2025 incl. Foot Locker). DSW (cut): CEO said it could make up lost Nike revenue with other athletic brands. | **Yes** |
| P6 Reversal | Reopening wholesale restores share and revenue | North America did reopen: wholesale +14% currency-neutral in FY2026 "including expanded distribution" to a record $11,958M (FY26 10-K p. 37; channel CSV); DSW and Macy's back from Oct 2023, Amazon 2025, Academy Jordan shops, Fleet Feet national deal; Nike run-specialty dollars +35.4% to Sept 2025. Yet NA total is still below FY2024 ($20,511M vs $21,396M), Q1 FY2027 wholesale fell 1% and Hill says weak sell-through of aged Sportswear "has impacted our future order books". Euromonitor 2025 US share is the lowest in the series. | **Partly** (shelf came back, share did not) |
| P7 Peer control | Brands that cut wholesale lose share; brands that stayed in wholesale do not | Adidas also exited "thousands of non-strategic wholesale accounts, particularly in the US" (Rorsted, Mar 2021) yet gained US share 2016 to 2019 (8.6% to 11.0%) and recovered in 2024 to 2025 on product (wholesale +14% c.n. 2024 on "significantly increased shelf space allocation"). Under Armour cut 2,000 to 3,000 NA doors and declined. Puma, wholesale-led, fell 8.1% currency-adjusted in 2025. The channel choice does not sort winners from losers; product does. | **No** |
| P8 Category | Loss concentrated where shelf matters most (running specialty, performance) rather than in Nike-controlled lifestyle | Historically yes in running: Hoka was Fleet Feet's No. 1 seller in 2024 and Nike was in "a fraction" of Fleet Feet doors two years before 2026. But the FY2025 to FY2027 decline is concentrated in Sportswear, Jordan and classics, which Nike over-supplied through its own channels (Denton, Oct 2026: Sportswear and Jordan "represented a high single-digit drag"), plus Converse and Greater China. Performance and running are growing. | **Partly** (history yes, current decline no) |

Score: 1 held, 4 partly, 3 failed. A primary cause should pass P2, P3 and P6 most of all, and it fails or only half-passes all three.

## 3. Evidence for the hypothesis

1. **Nike's own filings record the cuts and expected the wholesale loss.** FY2021 10-K (page from footer markers, p. 37): "over the last three years we have significantly reduced the number of undifferentiated wholesale accounts. During fiscal 2021, we took further steps towards account and channel consolidation by reprioritizing product allocation to benefit NIKE Direct and our differentiated strategic wholesale customers. We expect that over the next two fiscal years, we will more aggressively accelerate these changes as we work to reprofile the shape of the marketplace and recapture wholesale revenue declines over time." FY2022 10-K (p. 28): "we have reduced the number of wholesale accounts globally." FY2020 10-K (p. 27): the strategy "will lead with NIKE Digital and our own stores, as well as through select strategic partners."
2. **Scale of the cuts.** CFO Matt Friend in Sept 2021: Nike "exited about 50%" of its retail partners (CNN via ABC17, Dec 8, 2021). In March 2021 he said Nike had "reduced the number of undifferentiated accounts in North America by roughly 30%" since 2017 (CNN via ABC17, Mar 22, 2021). Named exits: Belk, Bob's Stores, Boscov's, City Blue, Dillard's, EbLens, Fred Meyer, VIM and Zappos (2020); DSW, Urban Outfitters, Shoe Show, Dunham's, Olympia and Big 5 (2021) (SNIPPET: Retail TouchPoints, RetailWire).
3. **NA wholesale shrank while the market grew.** NA wholesale fell from $10,875M (FY2019) to $9,621M (FY2022), -11.5% (FY19 10-K p. 80; FY22 10-K p. 85; my arithmetic). Euromonitor puts US athletic footwear market growth at a 4.0% CAGR for 2019 to 2024 (HGI, OPENED).
4. **Challengers' wholesale exploded in the same window** (Deckers 10-Ks; On 20-Fs), and challengers said so: Hoffmann's "clearly increases the opportunity" (Axios, Mar 22, 2022); Deckers credited Hoka growth to "share gains with one specialty account in the wholesale channel" (eMarketer, Mar 21, 2023).
5. **Retailers say it.** Foot Locker's Nike share fell from 75% to 59%, and its 10-K warned "whether our suppliers will choose to further sell such merchandise through their own direct-to-customers channel". Ed Stack (Nov 2025): Foot Locker "did not react quickly enough as its largest brand pivoted toward a direct-to-consumer model" (OPENED (repo)). Intersport COO Tesch (Feb 2025): retailers ran short of Nike stock when Nike focused on direct sales, and "Adidas has widened the gap" (Börsen-Zeitung, OPENED). Intersport Germany CEO von Preen (Sept 2024): only 36% of Nike orders arrived on time, "Das ist gerade bei Saisonware eine Katastrophe" (Tagesspiegel, OPENED, paywalled after the lede).
6. **Management admits it.** Hill (Dec 19, 2024): "Some partners and channels feel we've turned our back on them and we stopped engaging consistently" and "Prioritizing Nike digital revenue has impacted the health of our marketplaces" (Retail Dive, OPENED). Friend (Mar 2024): "We don't like the way our brand is showing up in wholesale and we own that" (Retail Dive, OPENED). Friend (Oct 2024): "The multi-brand environment is very competitive today and it will take time to expand market share" (SGB, OPENED). S&P (Jul 2025): "strategy missteps that resulted in lost market share" (OPENED (repo)).
7. **Mechanism is causal in the literature.** Van Crombrugge et al. (Journal of Marketing, 2025): when a supplier opened a webshop, about 2,000 retailers cut orders about 19% (OPENED (repo), via summaries).
8. **The fix works where applied.** NA wholesale +14% c.n. in FY2026 with "expanded distribution", NA EBIT +14% to $5,376M (FY26 10-K p. 36 to 37); Nike run-specialty +35.4% (OPENED (repo)).

## 4. Evidence against (or that it is not the main cause)

1. **The decline is in Nike's own channels, not wholesale** (P2). Digital fell $3.5B from FY2024 to FY2026. The FY2025 10-K (p. 29) says results "reflected a decrease in traffic across NIKE Direct and our actions to reduce supply of certain footwear products." The FY2024 10-K (p. 35) already showed digital "declines... reflecting reduced digital traffic." Consumers left Nike's own app and site, where shelf space is not an issue.
2. **Inverse geography** (P3). Greater China, the least-pivoted segment, fell 22.5% in two years and 26% c.n. in Q1 FY2027. Nike kept its big China partners (Topsports, Pou Sheng) throughout. The FY2026 10-K (p. 30) blames "declining store traffic, elevated promotional activity and higher levels of inventory across the marketplace" in Greater China.
3. **Timing mismatch** (P1). More US share was lost in 2016 to 2019 (-6.4 pts, the adidas Boost and Yeezy era) than in 2019 to 2025 (-5.2 pts). Share held at about 35% through 2021 to 2023 when the cuts peaked (GlobalData via Al Jazeera, OPENED).
4. **Shelf restored, share not** (P6). NA wholesale is 10% above FY2019 (my arithmetic), DSW and Macy's returned in Oct 2023, Amazon in 2025. Yet the binding constraint is now sell-through: Hill (Oct 1, 2026) said aged Sportswear sell-through "has impacted our future order books" (OPENED (repo)). Stack (Aug 2026) described a "hangover" of excess legacy lifestyle inventory promoted on brands' own sites (OPENED (repo)).
5. **Challengers grew faster in their own DTC than in wholesale** (P4). Consumers sought out Hoka and On directly, which means demand pull from product, not just shelf push.
6. **Peers break the pattern** (P7). Adidas cut thousands of US accounts in 2021 too and is winning. Puma stayed wholesale-led and fell 8.1% in 2025. Product cycles sort the winners.
7. **Favoured partners still diversified.** Dick's raised its Nike share (19% to 25%), yet New Balance and On also gained there (YipitData via Morning Brew, OPENED; details vague).
8. **Converse collapsed in both channels** (wholesale $1,098M to $605M, DTC $832M to $477M, FY2024 to FY2026), a brand and product problem the shelf thesis cannot explain.

## 5. Independent cause or symptom?

**A symptom of a wider strategy, acting as an enabler.** The upstream cause is the Consumer Direct Acceleration operating model (2020 to 2023): lead with digital, reallocate product to NIKE Direct, dissolve sport category teams, feed the app with high-volume classics (AF1, Dunk, Jordan 1), then clear the excess with promotions. That model produced three effects:

1. **Shelf ceded to challengers (this hypothesis).** Real but modest. It gave On, Hoka and New Balance distribution at Foot Locker, run specialty, DSW and European independents while their running and comfort products were catching a consumer trend Nike's innovation pipeline missed.
2. **Digital dependence and promotion.** This is the large one in the numbers: Digital rose to $12.1B, then fell $3.5B. Hill (Dec 2024): digital ran "roughly a 50/50 split of full-price to promotional sales" (SNIPPET, via search summary of the call).
3. **Classics over-supply.** Resale premium collapse (Air Jordan 1 High general releases 26% to 35% below retail, `data/jordan_resale_goat_20261013.csv`), Sportswear and Jordan drag (other repo notes).

Separately, the challengers' rise has its own upstream driver (the running and comfort trend plus an innovation gap), shown by their DTC growth. China (local brands, deflationary price war) and Converse are independent of this channel story.

## 6. How much of the decline? (quantified as honestly as possible)

**Scope A: the FY2024 to FY2026 revenue decline of $4,964M** (FY24 and FY26 10-Ks).
- Change by channel (my arithmetic): NIKE Brand wholesale -$305M (6% of the decline); NIKE Direct -$3,799M (77%); Converse -$908M; other and corporate the rest. By geography: Greater China -$1,698M (34%), EMEA -$1,035M, Converse -$908M, NA -$885M, APLA -$486M.
- The shelf-cede mechanism works through lost wholesale and lost consumer traffic at multi-brand retail. Wholesale explains at most about 6% of the decline, and the FY2025 wholesale drop was mostly Nike's own clean-up (returns and discounts, FY25 10-K p. 30). Some Direct traffic loss is consumers buying Hoka, On or New Balance at retailers where Nike had thinned out, which I cannot measure.
- **Estimate: about 5 to 15% of the FY2024 to FY2026 decline (roughly $0.25B to $0.75B).** This is an inference with wide error bars.
- **The broader DTC strategy unwind** (digital collapse, including a mechanical give-back when a pair moves from Nike's app at retail price back to wholesale at roughly half the revenue) is much bigger: plausibly **40 to 70%** of the decline. That is a different mechanism from the one in this hypothesis.

**Scope B: the 2019 to 2025 US share loss of 5.2 pts** (Euromonitor via HGI).
- Upper-bound check: Hoka plus On wholesale grew by about $0.85B (Hoka, FY2020 to FY2024) plus about CHF 1.2B (On, 2019 to 2024) globally. Even if a third to a half of that came from Nike-vacated space (Jefferies says "much"; their faster DTC growth says not all), that is about $0.6B to $1.0B a year of wholesale-value sales, roughly 1.3% to 2.2% of Nike's FY2026 revenue (my arithmetic, inference).
- **Estimate: the shelf mechanism explains roughly 20 to 40% of the 2019 to 2025 US share loss (about 1 to 2 pts of 5.2).** The rest is product and innovation, classics fatigue and the comfort and running trend.

## 7. Can management fix it?

**Partly.** The shelf itself is fixable and is largely fixed in North America (record wholesale, DSW, Macy's, Amazon, Academy, Fleet Feet, Foot Locker "Nike Prime" placement). What cannot simply be bought back:
- Challengers now have durable brand equity, their own fast-growing DTC, and permanent multi-brand assortments. JD's CEO (Sept 2026) said JD's share with "some of the new brands" in key regions is above its Nike share (OPENED (repo)). Foot Locker targets about 40% non-Nike (SNIPPET).
- Restored shelf only converts if product sells through. Q1 FY2027 shows it does not yet for Sportswear and Jordan.
- In China the issue is the opposite (Nike is now *cutting* distributor online channels from 2027-01-01, OPENED (repo)), so the shelf lever does not apply there.

## 8. Natural experiments used

| Experiment | Treated | Control | Result |
|---|---|---|---|
| Regions with big vs small DTC pivots | NA (+17 pts DTC share) | Greater China (+3.5 pts) | Control declined far more; rejects shelf as main driver |
| Retailers cut vs favoured | Foot Locker (Nike 75% to 59%), DSW | Dick's (Nike 19% to 25%) | Cut retailers diversified, as predicted |
| Brands that cut accounts | Nike, adidas, Under Armour (all cut 2020 to 2021) | Puma (wholesale-led) | Outcomes diverge by product, not channel |
| Before vs after reversal | NA FY2022 (wholesale trough $9,621M) | NA FY2026 (record $11,958M) | Shelf restored; revenue and share not restored |
| Challenger channels | Hoka, On wholesale (4x, 7x) | Hoka, On DTC (9x, 14x) | DTC grew faster: demand pull dominates |

## 9. Gaps

- No annual Euromonitor or Circana US Nike share series 2019 to 2025 from one consistent source; the GlobalData (2021 to 2023) and Euromonitor (2016, 2019, 2025) series have different scopes, so the "loss concentrated in 2024 to 2025" reading is an inference.
- No door counts for Nike before and after (Amalthea's "30,000 to 3,000" claim is unreconciled with Friend's "about 50%").
- No account-level sell-through data showing which Nike-vacated doors went to which brand.
- Hoka and On regional wholesale splits by account type not extracted.
- Nike's Q2 FY2025 call transcript was not opened directly; Hill's "50/50" quote is snippet only.

## 10. Sources

### SEC filings (all OPENED: downloaded from EDGAR this session and searched in full text)
| Source | Date | Used for |
|---|---|---|
| Nike FY2020 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018720000047/nke-531202010k.htm | 2020-07-24 | CDA strategy quote (p. 27, from footer markers); segment channel table p. 88 |
| Nike FY2021 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018721000028/nke-20210531.htm | 2021-07-20 | "significantly reduced the number of undifferentiated wholesale accounts" (p. 37, from footer markers) |
| Nike FY2022 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018722000038/nke-20220531.htm | 2022-07-21 | "reduced the number of wholesale accounts globally" (p. 28); Digital $10.7B FY22, $9.1B FY21 (p. 33) |
| Nike FY2024 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018724000044/nke-20240531.htm | 2024-07-25 | Digital $12.1B, "reduced digital traffic" (p. 35); channel table p. 34, 84 |
| Nike FY2025 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018725000047/nke-20250531.htm | 2025-07-17 | "decrease in traffic across NIKE Direct" (p. 29); marketplace actions (p. 30); Digital $9.6B (p. 34); NA wholesale -5% (p. 38) |
| Nike FY2026 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm | 2026-07-15 | Marketplace actions, China and Converse (p. 30); Digital $8.6B (p. 33); NA wholesale +14% "including expanded distribution" (p. 37) |
| Nike FY2019 to FY2026 channel and segment data | various | `data/nike_channel_split.csv`, `research_notes/04_financial_data_pack.md` (verified, reused) |
| Foot Locker 10-Ks filed 2017-03-23 to 2025-03-27 (CIK 850209), e.g. https://www.sec.gov/Archives/edgar/data/850209/000143774925009620/floc20241213_10k.htm | 2017 to 2025 | Nike share of purchases 68%, 67%, 66%, 71%, 75%, 68%, 65%, 65%, 59% (2016 to 2024); "not more than 55%" (filed 2022-03-24) |
| Foot Locker XBRL company facts (data.sec.gov) | 2025 | Revenue, cost of sales |
| Dick's 10-Ks filed 2018-03-30 to 2026-03-27 (CIK 1089063), e.g. https://www.sec.gov/Archives/edgar/data/1089063/000108906326000007/dks-20260131.htm | 2018 to 2026 | Nike share of purchases 18% to 31% |
| Deckers 10-Ks FY2019 to FY2026 (CIK 910521), e.g. https://www.sec.gov/Archives/edgar/data/910521/000162828026037664/deck-20260331.htm | 2019 to 2026 | Hoka wholesale and DTC by year |
| On Holding 20-Fs FY2021 to FY2025 (CIK 1858985), e.g. https://www.sec.gov/Archives/edgar/data/1858985/000185898526000008/onholdingag-20251231.htm | 2022 to 2026 | On wholesale, DTC, regional sales |

### Web sources
| Source | Date | Status | Used for |
|---|---|---|---|
| HGI (Marie Driscoll), "Have athletic footwear industry titans lost their step?", https://hgi.io/insights/have-athletic-footwear-industry-titans-lost-their-step/ | 2026-01-13 | OPENED (curl) | Euromonitor Passport (Dec 18, 2025) US athletic footwear company shares 2016, 2019, 2025; US market 4.0% CAGR 2019 to 2024 |
| Al Jazeera, "Nike stock plunges on surprise forecast of drop in sales" | 2024-06-28 | OPENED | GlobalData US sports footwear: Nike 35.4% (2021), 35.37% (2022), 34.97% (2023) |
| CNN via ABC17, "Nike will stop selling sneakers at one of America's largest shoe chains" | 2021-12-08 | OPENED | Friend: "exited about 50%"; DSW about 7% of sales; DSW CEO quote |
| CNN via ABC17, "Nikes are getting harder to find at stores" | 2021-03-22 | OPENED | NA undifferentiated accounts cut "roughly 30%"; Rorsted adidas quote; independent stores |
| Modern Retail, "After years of focusing on DTC, Nike is quietly bringing more wholesale partners back" | 2023-06-09 | OPENED | DSW and Macy's return Oct 2023; Saunders and Nikic quotes |
| Retail Dive, Nike Q3 FY24 | 2024-03-22 | OPENED | Donahoe "some important adjustments"; Friend "we own that" |
| Retail Dive, Nike Q2 FY25 | 2024-12-20 | OPENED | Hill quotes on partners and digital |
| SGB Media, Nike Q1 FY25 | 2024-10-02 | OPENED | Friend on missteps and market share |
| SGB Media, "Nike admits it has a problem and its solution is Air" | 2024-03-22 | OPENED | 40 strategic partners; 30,000 to 3,000 claim (Amalthea); 40% to 80% "differentiated" goal |
| Axios Pro, "On Running seeks to fill the void left by Nike" (via web.archive.org) | 2022-03-22 | OPENED | Hoffmann quote; Foot Locker non-Nike comps about +30% |
| eMarketer, "On Running posts explosive growth as Nike doubles down on D2C" (via web.archive.org) | 2023-03-21 | OPENED | Deckers "share gains with one specialty account" |
| Retail Brew, Hoka wholesale | 2023-04-18 | OPENED | Hoka first in Foot Locker July 2022; Champs making room for Brooks and Hoka |
| Footwear News via Yahoo, Jefferies (Konik) | 2025-08-15 | OPENED | "much of On's past wholesale growth came while Nike pulled back" |
| Morning Brew, YipitData at Dick's | 2024-03-23 | OPENED | New Balance and On gaining at Dick's (vague) |
| Börsen-Zeitung, "Adidas sprints ahead" | 2025-02-11 | OPENED | Intersport COO quotes |
| Tagesspiegel, Nike leadership change | 2024-09-20 | OPENED (lede only) | Intersport Germany 36% on-time deliveries |
| Jing Daily, Puma 2025 | 2026-02-27 | OPENED | Puma -8.1% c.a. in 2025 |
| adidas FY2024 and FY2025 results releases (local copies of adidas IR PDFs in session scratchpad) | 2025, 2026 | OPENED | adidas wholesale +14% c.n. 2024 on "significantly increased shelf space allocation"; 2025 wholesale +10% c.n. |
| Retail TouchPoints, RetailWire on 2020 and 2021 account exits | 2020 to 2021 | SNIPPET (403 and 429) | Named exited accounts |
| Under Armour door cuts (Retail Dive, Formula4Media) | 2021-02 | SNIPPET | 2,000 to 3,000 NA doors |
| Puma H1 2025 wholesale (Just Style) | 2025 | SNIPPET | Wholesale -4.9% c.a. H1 2025 |
| Hill "50/50" digital full-price split, Q2 FY25 call | 2024-12-19 | SNIPPET | Digital promotion dependence |
| Repo notes reused: `retailers_and_resale.md`, `academic_literature.md`, `analysts_and_consumer_data.md`, `competitors_and_turnarounds.md`, `china_market.md`, `nike_standing.md` | 2026-10-13 | OPENED (repo) | Stack, JD, Fleet Feet, Van Crombrugge, Circana run specialty, Q1 FY27 call |
