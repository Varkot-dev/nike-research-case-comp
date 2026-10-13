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
3. **Classics over-supply and brand fatigue.** Resale premium collapse, Sportswear and Jordan drag (other repo notes).

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

## Challenge: REFUTER

Date: 2026-10-13. Lens: try to disprove "the DTC pivot and wholesale account cuts gave shelf space to competitors and caused the share loss." All filings below were downloaded from EDGAR in this session (OPENED) unless marked otherwise. Arithmetic is mine and labelled.

### R1. Verdict

**The hypothesis as stated ("caused the share loss") does not survive. Downgrade from contributing cause to minor.** The account cuts were real and challengers did use the vacated doors, but nearly every discriminating prediction fails: the shelf loss in revenue terms was small and temporary, it was fully reversed two years before Nike's decline began, Nike out-grew the US market during the peak cut years, challengers grew just as fast in places where Nike never vacated shelf, and a wholesale-heavy incumbent (VF / Vans) lost as much US share as Nike without any comparable door purge. I would cut the investigator's estimate of the shelf mechanism's share of the 2019 to 2025 US share loss from 20 to 40% (1 to 2 pts) to roughly 0 to 20% (0 to 1 pt), and keep it at the low end (about 5%) of the FY2024 to FY2026 revenue decline.

### R2. Failed predictions found in this pass

1. **The shelf was already back before the decline started (timing kill).** NA wholesale: $10,875M (FY2019), $9,371M (FY2020), $10,186M (FY2021), $9,621M (FY2022), **$11,273M (FY2023, a record above FY2019)**, $11,004M (FY2024), $10,484M (FY2025), $11,958M (FY2026) (`data/nike_channel_split.csv`, 10-K segment tables). The wholesale revenue trough lasted three COVID-confounded years and ended in FY2023. Nike's revenue decline began in FY2025, two years after NA wholesale had regained its FY2019 level. A shelf-space cause predicts the decline coincides with the shelf gap; it follows the shelf's return instead.
2. **Globally the cuts never shrank wholesale.** NIKE Brand wholesale went from $25,423M (FY2019) to $27,758M (FY2024), +9.2% (my arithmetic, same CSV). EMEA wholesale rose $7,076M to $8,522M (FY2019 to FY2023, +20%). "Giving away shelf" did not show up as lost wholesale dollars outside a temporary NA dip.
3. **Nike out-grew the US market during the peak cut years.** NA revenue rose from $15,902M (FY2019) to $21,608M (FY2023), +35.9% (my arithmetic), while Euromonitor puts US athletic footwear market growth at a 4.0% CAGR for 2019 to 2024, about +17% over four years (HGI, OPENED this session, 2026-01-13, citing Passport Dec 18, 2025). Price increases and COVID demand inflate both, but a company handing share to rivals through lost shelf should not grow about twice as fast as its market. This also fits GlobalData's flat 35% share 2021 to 2023 already in the notes.
4. **Hoka's growth shows no step-change when Nike's cuts peaked.** Hoka wholesale (Deckers 10-Ks, fiscal years ending March): $74.9M FY2016, $93.1M FY2017, $132.7M FY2018, $185.1M FY2019, $277.1M FY2020, $405.2M FY2021, $628.7M FY2022, $925.9M FY2023, $1,126.1M FY2024, $1,397.8M FY2025, $1,651.8M FY2026. Year-on-year growth (my arithmetic): +24%, +43%, +39%, +50%, +46%, +55%, +47%, +22%, +24%, +18%. Hoka was already growing about 40 to 50% a year before Consumer Direct Acceleration (June 2020) and before the 2020 to 2021 named exits. The only visible acceleration (FY2022, +55%) is about 5 to 9 pts above trend. Sources: Deckers FY2020 10-K (filed 2020-06-01, five-year segment table) and FY2022, FY2024, FY2026 10-Ks (filed 2022-05-27, 2024-05-24, 2026-05-22), OPENED. Hoka DTC $75.5M (FY2020) to $680.6M (FY2024), 9.0x, confirmed (FY2020 and FY2024 10-K brand tables, OPENED).
5. **Challengers boomed where Nike did not vacate shelf.**
   - On Europe sales: CHF 128.3M (2019), 187.5M (2020), 260.4M (2021), 354.3M (2022) (On 424B4 2021-09-16 and 2022 20-F filed 2023-03-21, OPENED). That is +176% while Nike's EMEA wholesale was rising 20%.
   - On Asia-Pacific: CHF 260.2M (2024) to 511.1M (2025), +106.7% constant currency (On 2025 20-F, filed 2026-03-03, OPENED), and +54.7% c.c. in Q2 2026 (On 6-K press release, 2026-08-11, OPENED via WebFetch). Nike kept its China distributors (Topsports, Pou Sheng) the whole time, yet Greater China is Nike's worst region.
   - On North America grew +86% in calendar 2020 (CHF 111.8M to 208.1M, 424B4, OPENED), mostly before the December 2020 and 2021 named account exits.
   The natural experiment (challenger growth in no-cut regions vs cut regions) shows growth everywhere, which is demand pull, not vacated-shelf push.
6. **Nike re-took the NA shelf in FY2026 and Q1 FY2027 and challengers kept growing; where they slowed, they said it was their own choice.** NA wholesale +14% c.n. in FY2026 and +9.0% reported in Q1 FY2027 ($2,981M vs $2,736M; NA Direct -6.0%, $2,146M vs $2,284M; NA total +2.1%, my arithmetic from the channel CSV). Over the same period: On Americas +23.4% c.c. in 2025 and +13.0% c.c. in Q2 2026; On wholesale +32.6% c.c. in 2025 and +12.7% c.c. in Q2 2026, with On saying it is "deliberately managing wholesale sell-in ... to protect full-price integrity in a promotional marketplace" (On 6-K, 2026-08-11, OPENED via WebFetch). Hoka wholesale +18.2% in FY2026 (Deckers FY2026 10-K, OPENED); Hoka Q1 FY2027 +7.7% to $703.5M (Just Style, July 2026, OPENED via WebFetch; Deckers release copies SNIPPET). Honest caveat: the Hoka slowdown is consistent with Nike's shelf return, so the reversal test is not a clean kill; but Nike's own total did not recover, which is what the hypothesis needs.
7. **Peer control: a wholesale-heavy incumbent lost as much share without a Nike-style purge.** Euromonitor US athletic footwear company shares (HGI table, OPENED): VF Corp 9.4% (2019) to 3.9% (2025), about -5.5 pts, versus Nike -5.2 pts. adidas, which also cut thousands of US accounts in 2021, went 11.0% to 10.1% (-0.9). Top-10 combined share was flat (77.7% to 77.8%). Share moved from fading franchises (Vans, Nike classics) to On (6.3% in 2025), Skechers (9.0%), New Balance (6.4%) and Deckers (3.8%), regardless of the incumbent's channel strategy. HGI also reports Nike's global share fell 540 bps to 22.9% over the 10 years to 2025, which includes markets where Nike made no comparable cuts.
8. **The biggest share loss came before the cuts.** Euromonitor via HGI: Nike 40.5% (2016) to 34.1% (2019), -6.4 pts, with Nike's full wholesale footprint mostly intact (CDO was announced June 2017 and the named exits were mostly 2020 to 2021). Verified on the opened HGI page.

### R3. Checks on numbers the investigator cited

| Claim | Primary source check | Result |
|---|---|---|
| Hoka wholesale $277M to $629M | Deckers FY2020 10-K: 277,097; FY2022 10-K: 628,674 (fiscal years ending March 2020 and March 2022) | Correct; note Deckers FY ends March, so FY2020 is about 10 months after Nike FY2019 |
| On North America CHF 112M to CHF 410M, "FY2019 to FY2022 window" | On 424B4: 111.8 (2019); 2022 20-F: 409.5 (2021), 738.5 (2022) | **Window mislabelled**: 410M is calendar 2021, not 2022. 2022 was CHF 738.5M. The point still stands but the pairing is wrong |
| Hoka DTC 9x vs wholesale 4x | FY2020 and FY2024 10-K brand tables: DTC 75.5 to 680.6; wholesale 277.1 to 1,126.1 | Correct (9.0x, 4.1x) |
| On wholesale CHF 1,375.5M (2024) | On 2025 20-F: 1,375.5 (2024), 1,753.4 (2025) | Correct |
| Foot Locker Nike 59% (2024) vs 65% (2023) | Foot Locker 10-K filed 2025-03-27 | Correct ("Approximately 59% and 65% was purchased from one supplier, Nike") |
| Euromonitor 40.5 / 34.1 / 28.9; 4.0% CAGR 2019 to 2024 | HGI page, curl this session | Correct |
| NA wholesale $9,621M FY2022, $11,958M FY2026 | channel CSV | Correct |

### R4. What survives

- The mechanism exists at the margin: Foot Locker's Nike share fell 75% to 59%, challengers explicitly cited Nike's retreat, and Hoka's slowdown in 2026 coincides with Nike's return. These are real but they explain where challengers got their first doors, not why consumers chose them or why Nike's revenue fell in FY2025 to FY2027.
- The better-supported story: product and franchise fatigue (classics over-supplied, running and comfort missed) shows up in every channel, every region and every incumbent with a fading franchise, while the shelf-specific predictions (timing, geography, reversal, peer control) fail.

### R5. Sources (this pass)

| Source | Date | Status |
|---|---|---|
| Deckers 10-K FY2020, https://www.sec.gov/Archives/edgar/data/910521/000091052120000016/deck331202010-k.htm | 2020-06-01 | OPENED |
| Deckers 10-K FY2022, https://www.sec.gov/Archives/edgar/data/910521/000091052122000017/deck-20220331.htm | 2022-05-27 | OPENED |
| Deckers 10-K FY2024, https://www.sec.gov/Archives/edgar/data/910521/000091052124000017/deck-20240331.htm | 2024-05-24 | OPENED |
| Deckers 10-K FY2026, https://www.sec.gov/Archives/edgar/data/910521/000162828026037664/deck-20260331.htm | 2026-05-22 | OPENED |
| On Holding 424B4 prospectus, https://www.sec.gov/Archives/edgar/data/1858985/000119312521275158/d175570d424b4.htm | 2021-09-16 | OPENED |
| On Holding 20-F FY2022, https://www.sec.gov/Archives/edgar/data/1858985/000185898523000011/onholdingag-20221231.htm | 2023-03-21 | OPENED |
| On Holding 20-F FY2025, https://www.sec.gov/Archives/edgar/data/1858985/000185898526000008/onholdingag-20251231.htm | 2026-03-03 | OPENED |
| On Holding 6-K Q2 2026 press release, https://www.sec.gov/Archives/edgar/data/0001858985/000185898526000018/a26q2-ex993xpressrelease.htm | 2026-08-11 | OPENED (WebFetch summary with quotes) |
| Just Style, Deckers Q1 FY27 result, https://www.just-style.com/news/deckers-q1-fy27-result/ | 2026-07 | OPENED (WebFetch) |
| Deckers Q1 FY27 release copies (BusinessWire, Las Vegas Sun) | 2026-07-23 | SNIPPET (402 / stream error) |
| Foot Locker 10-K FY2024, https://www.sec.gov/Archives/edgar/data/850209/000143774925009620/floc20241213_10k.htm | 2025-03-27 | OPENED |
| HGI, https://hgi.io/insights/have-athletic-footwear-industry-titans-lost-their-step/ | 2026-01-13 | OPENED (curl) |
| Nike channel and segment data, `data/nike_channel_split.csv` | FY2019 to Q1 FY2027 | OPENED (repo, verified) |

## Challenge: ROOT-CAUSE

Date: 2026-10-13. Lens: assume the symptom (Nike lost shelf at multi-brand retail and lost share) is real, and ask whether the shelf loss is itself a downstream effect of a different upstream cause. Status labels as above. Filings below were downloaded from EDGAR in this session (OPENED). Arithmetic is mine and labelled. Note: the shared web-search budget ran out partway through this pass, so some threads (Topsports brand mix, Dick's brand-level data) could not be pursued; I did not work around the limit.

### RC1. Verdict

**Symptom of another cause. The shelf mechanism is a transmission belt between two upstream causes, not a cause in its own right.**

1. **Upstream cause A (the decision): the Consumer Direct Offense was a deliberate per-transaction economics play adopted in response to a North American wholesale problem that already existed.** The account cuts were the designed consequence, not an accident.
2. **Upstream cause B (the demand): the product cycle, especially running, decided who filled the vacated shelf and whether Nike could win it back.** Retailers kept moving away from Nike even when Nike gave them more allocation than planned. They moved back only when Nike's running product earned it.

The REFUTER pass already showed that the shelf predictions fail on timing, geography and peers. This pass adds why: the same data are fitted better by "Nike chose the economics of its own channel, and then lost the product contest". Shelf space sits downstream of both.

### RC2. New evidence: the account cuts were downstream of a decision made for revenue per pair, in a market that was already soft

- **Nike's own stated rationale was the economics of a transaction.** CFO Andy Campion, Q4 FY2017 call (Nike 8-K Ex. 99.1, filed 2017-07-05, OPENED): direct "represent[s] roughly 35% of our business on a wholesale equivalent basis but drove 70% of our growth in fiscal year '17", and "fulfilling demand through NIKE.com generates nearly twice the revenue and significantly higher-margin on each transaction... So we will continue to prioritize and drive a more immediate shift towards more direct service of the consumer." In the same call: "In fiscal year '18, we will more deliberately fuel growth in the direct dimensions of our business while also more deliberately transforming or transitioning away from other less differentiated and less productive points of distribution."
- **The North American wholesale market was already weak before the cuts.** Same call: "we continue to see a high single-digit disparity between revenue growth and Futures growth in North America. While the North America retail landscape remains promotional..." Nike FY2017 10-K (filed 2017-07-20, OPENED): NA marketplace "impacted by... shifting consumer traffic patterns across digital and physical channels, retail consolidation and a promotional environment", and NA footwear growth came from "Sportswear and Jordan Brand categories, partially offset by declines in other categories". NIKE Brand futures for June to November 2017 were $14.7B, 2% below the prior year (FY2017 10-K, Orders).
- **Interpretation (inference):** the shelf withdrawal was a choice with two upstream drivers: (a) Nike believed a pair sold on its own site was worth about 2x a wholesale pair, and (b) its wholesale business was already soft and promotional, with growth concentrated in lifestyle classics. Euromonitor's 2016 to 2019 share loss (-6.4 pts, already in these notes) belongs to the same pre-existing weakness. The shelf ceded later is a consequence of that diagnosis, not a separate root cause.
- **The same economics explain most of today's revenue arithmetic.** The CFO's "nearly twice the revenue" ratio is the primary-source basis for the investigator's "roughly half the revenue per pair" give-back assumption, which until now rested on inference. When Nike reverses the pivot, revenue falls mechanically even if pairs sold do not.

### RC3. New evidence: in North America, the FY2026 revenue pattern is a channel-mix effect of the unwind, not lost shelf

- Nike FY2026 10-K (filed 2026-07-15, OPENED), North America, p. 37: "Wholesale revenues increased 14% including expanded distribution, higher shipments to existing partners and fewer marketplace management actions... NIKE Direct revenues decreased 6% due to declines in digital sales of 10%... Unit sales of footwear increased 6%, while lower ASP per pair reduced footwear revenues by approximately 1 percentage point. Lower ASP per pair was primarily due to channel mix."
- Same 10-K, p. 30, the strategy: "Repositioning NIKE Brand Digital as a full-price platform and reinvesting in wholesale distribution. This includes liquidating inventory through increased markdowns across NIKE Direct, and higher sales returns and discounts with our wholesale partners."
- Same 10-K, p. 33: NIKE Brand Digital fell from $9.6B to $8.6B, "primarily due to reduced traffic". Globally, NIKE Brand footwear units fell 1% and lower ASP, "primarily due to channel mix", took another 1 pt.
- NA channel arithmetic (channel CSV, my arithmetic): FY2025 to FY2026 NA wholesale +$1,474M, NA Direct -$535M, NA total +$939M.
- **Interpretation:** in the one region where Nike re-bought the shelf, Nike sold 6% more pairs in FY2026. Part of the "reduced traffic" on Digital is self-inflicted: Nike removed promotions from the channel that had relied on them (Hill's roughly 50/50 full-price split is SNIPPET only, see section 9). The mechanism behind the Digital collapse is the reversal of the CDA promotional-digital model. Lost shelf does not explain it. This repeats the investigator's own separation of "broader DTC unwind" from "shelf mechanism", and strengthens it with Nike's own unit data.

### RC4. New evidence: retailers moved away from Nike on sell-through even when Nike gave them more allocation

- **Nike moderated the cuts at Foot Locker, but the shift continued.** SGB Media, 2022-11-18 (OPENED): Foot Locker "now expects to end the year with a higher Nike sales mix than it first anticipated", and the shift will be "more gradual" (CEO Mary Dillon). New Balance sales at Foot Locker rose "almost 70%" in the quarter.
- **After the March 2023 reset, Foot Locker's Nike share kept falling.** Retail Dive, 2023-03-20 (OPENED): Foot Locker and Nike worked to "revitalize" the partnership "complementary to the Nike direct-to-consumer strategy", while Foot Locker planned a bigger running category with Hoka and On. Yet Foot Locker's Nike share of purchases fell from 65% (2023) to 59% (2024) (Foot Locker 10-K filed 2025-03-27, verified in REFUTER R3). A shelf-supply cause predicts Nike's share stabilises once Nike resumes supply. It kept falling, which fits a demand cause.
- **The shelf followed product, in both directions.** Apparel Resources, 2025-08-19 (OPENED), citing JPMorgan's Matthew Boss: Foot Locker had placed On, Hoka, adidas and New Balance ahead of Nike in the lead running columns, and only now restored Nike to "pole position", "the first time in two years". The article says Nike "lost ground" in running "while prioritizing lifestyle sneakers". The two years when Nike was behind (about 2023 to 2025) came *after* the Foot Locker reset. Retailers demoted Nike on sell-through and promoted it again when its running product (the Pegasus and Vomero cycle under Hill, per other notes) improved.
- **Challengers grew in China, where Nike never vacated the shelf.** On 2025 20-F (filed 2026-03, OPENED): APAC net sales CHF 141.1M (2023), 260.2M (2024), 511.1M (2025), and "The 96.4% increase in net sales in APAC was primarily driven by strong sales growth in China and Japan across both channels." On also runs 38 locations in China, including Hong Kong. This sharpens the REFUTER's APAC point: the On growth is explicitly China and Japan, and in both channels. In Greater China, Nike kept Topsports and Pou Sheng and fell 22.5% over two years.

### RC5. Alternative explanation that fits the same data better

**The chain: (1) by FY2017 Nike's wholesale business was soft, promotional and dependent on lifestyle; (2) Nike chose own-channel economics (about 2x revenue per pair) and cut accounts; (3) the vacated doors were filled by the brands whose product consumers wanted (running and comfort: Hoka, On, New Balance); (4) after Nike had narrowed product creation toward classics fed through Digital, retailers rationally gave those brands more space even after Nike offered supply back; (5) unwinding the promotional Digital model now costs revenue mechanically (channel mix) and through lost traffic.** Under this chain:
- Timing fits: share loss before the cuts (2016 to 2019), flat share while the cuts peaked (2021 to 2023), renewed loss after supply returned (2024 to 2025).
- Geography fits: the biggest decline is in China, where no shelf was ceded.
- Reversal fits: shelf bought back, units up in NA, but revenue per pair down and Digital down.
- Retailer behaviour fits: Foot Locker's Nike share fell further after the reset, and placement followed running sell-through.
The pure shelf hypothesis predicts none of the last three.

### RC6. Quantification under this lens

- Shelf mechanism as an independent cause of the FY2024 to FY2026 revenue decline: **about 0 to 10%** (below the investigator's 5 to 15%, consistent with REFUTER's low end). Most of what looks like shelf effect is product pull (RC4) or channel-mix arithmetic of the unwind (RC3).
- The upstream CDA decision (account cuts plus promotional Digital plus classics supply) remains the largest single cause, consistent with timeline_forensics.md (50 to 60%). The shelf is one of its outputs.
- 2019 to 2025 US share loss: shelf plausibly about 0.5 to 1 pt of 5.2 (10 to 20%), mostly as the entry ramp for Hoka and On in 2020 to 2022. Inference, wide error bars.

### RC7. Gaps

- No account-level sell-through data to separate Foot Locker's "push" (Nike allocation) from "pull" (consumer choice) quarter by quarter.
- The web-search budget ran out before I could check Topsports brand mix or Dick's brand-level data for challenger gains at a favoured Nike partner.
- The 2x revenue-per-transaction ratio is Nike's FY2017 figure. The current ratio after promotions is not disclosed.

### RC8. Sources (this pass)

| Source | Date | Status | Used for |
|---|---|---|---|
| Nike Q4 FY2017 earnings call transcript, 8-K Ex. 99.1, https://www.sec.gov/Archives/edgar/data/320187/000032018717000059/q4fy17erccexhibit991.htm | 2017-07-05 (call 2017-06-29) | OPENED | "nearly twice the revenue"; "less differentiated and less productive points of distribution"; NA futures disparity and promotional landscape |
| Nike FY2017 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018717000090/nke-5312017x10k.htm | 2017-07-20 | OPENED | NA retail consolidation and promotional environment; growth only in Sportswear and Jordan; futures $14.7B, -2% |
| Nike FY2026 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm | 2026-07-15 | OPENED | NA footwear units +6%, ASP down on channel mix (p. 37); Digital repositioned as full-price (p. 30); Digital $8.6B, "reduced traffic" (p. 33); global footwear units -1% |
| On Holding 2025 20-F, https://www.sec.gov/Archives/edgar/data/1858985/000185898526000008/onholdingag-20251231.htm | 2026-03 | OPENED | APAC CHF 141.1M / 260.2M / 511.1M; growth "driven by strong sales growth in China and Japan across both channels"; 38 China locations |
| On Q4 and FY2025 results release, https://press.on-running.com/on-announces-fourth-quarter-and-full-year-results-and-the-filing-of-its-annual-report-on-form-20-f-for-2025 | 2026-03-03 | OPENED | Regional and channel growth rates for 2025 |
| SGB Media, "Foot Locker finds surprise boost from Nike in third quarter", https://sgbonline.com/foot-locker-finds-surprise-boost-from-nike-in-third-quarter/ | 2022-11-18 | OPENED | Higher Nike mix than planned; shift "more gradual"; New Balance up about 70% |
| Retail Dive, "Foot Locker to close 400 stores, revitalize Nike partnership", https://www.retaildive.com/news/foot-locker-close-400-stores-revitalize-nike-partnership/645420/ | 2023-03-20 | OPENED | Reset "complementary to the Nike direct-to-consumer strategy"; running expansion with Hoka and On |
| Apparel Resources, "Foot Locker restores Nike Prime store placement", https://apparelresources.com/business-news/retail/foot-locker-restores-nike-prime-store-placement-partnership-rebuilds/ | 2025-08-19 | OPENED | Nike behind On, Hoka, adidas, New Balance in running for two years; "lost ground" in running while prioritising lifestyle |
| CNBC, Foot Locker renewed Nike relationship (2023-03-20) | 2023-03-20 | Not opened (403) | Not used for any claim |
| Press reports that Nike is about 45% of JD Sports' sales (MarketScreener, Reuters syndication) | 2025 | SNIPPET | Context only; not used for any conclusion |
| Nike channel data, `data/nike_channel_split.csv` | FY2019 to FY2026 | OPENED (repo, verified) | NA FY2025 to FY2026 channel changes |
