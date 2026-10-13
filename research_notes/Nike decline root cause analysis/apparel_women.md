# Root cause test: did Nike lose apparel, women and athleisure to Lululemon, Alo, Vuori and others, and is this a material driver of the decline?

Research date: 2026-10-13. Hypothesis under test: *Nike lost apparel, women and athleisure to Lululemon, Alo, Vuori and others, and this is a material driver of the decline.*

Status labels: **OPENED** = I fetched and read the page or filing in this session (curl or WebFetch). **OPENED (cache)** = the full document was already downloaded to the session scratchpad by a sibling researcher today and I read the text myself. **OPENED (repo)** = opened by an earlier researcher and recorded in this repo's notes; reused, not re-fetched. **SNIPPET** = seen only in a search-result summary. Nike numbers come from the Nike 10-Ks and 10-Qs on EDGAR (printed page from the "FORM 10-K nn" footer), `data/nike_filing_facts.csv` and `research_notes/04_financial_data_pack.md`. All arithmetic is mine and labelled "my arithmetic".

---

## 1. Bottom line

**Verdict: minor as a driver of the FY2024 to FY2026 decline. Real as a pre-2024 opportunity cost (Nike under-earned the athleisure boom, especially in Women's), but the specific, testable predictions of "lost apparel and women to Lululemon, Alo, Vuori" as a cause of the revenue decline fail on almost every axis: category, geography, gender, timing and peer behaviour.**

The five facts that kill it as a material driver:

1. **The decline is not an apparel decline.** NIKE Brand apparel fell only $326M from FY2024 to FY2026 (13,775 to 13,449), 6.6% of the $4,964M NIKE, Inc. revenue decline (my arithmetic; FY2026 10-K p. 32). Apparel's share of NIKE Brand revenue *rose* during the decline, from 27.9% (FY2024) to 29.7% (FY2026). Footwear fell $3,902M. If Nike were bleeding apparel to athleisure brands, apparel's share should fall, not rise.
2. **The geography is backwards.** Lululemon, Alo and Vuori are overwhelmingly US businesses (Lululemon: US $6,328M of $11,103M in FY2025, 10-K p. 57). Yet Nike **North America apparel is at an all-time high**: $6,075M in FY2026, above FY2024 ($5,953M) and FY2023 ($5,947M) (FY2026 10-K p. 37), and +6% again in Q1 FY2027 ($1,566M vs $1,474M; Q1 FY2027 10-Q p. 26). The apparel declines are in Greater China (-$293M FY24 to FY26) and EMEA (-$170M), where Alo and Vuori are negligible.
3. **The gender split is backwards.** The only year Nike disclosed revenue by consumer during the decline (FY2025 10-K p. 33), Women's fell 6% (-$647M), the same rate as Men's (-6%) and less than Jordan (-16%). Women's was 21.0% of NIKE Brand revenue but only 14.0% of the FY2025 decline (my arithmetic). A women's-led share loss predicts the opposite.
4. **The timing is backwards.** Lululemon's US revenue grew $3,492M (+122%) from FY2019 to FY2023 while Nike was *growing*. It then stalled (FY2025 -2.4%, the first US decline) and is now falling hard (Q2 FY2026 US -8%, Americas comparable sales -12%; 10-Q filed Sep 3, 2026, p. 10 and 21). In the most recent overlapping quarter (Jun to Aug 2026), Nike NA apparel grew +6% while Lululemon US shrank 8%. Same consumers, same months, opposite directions.
5. **The challengers are mostly eating each other.** Alo and Vuori's gains come from Lululemon (M Science: Lululemon athleisure share -10 points to 43.9% in Aug 2026, Alo +5.9, Vuori +2.2; Reuters Sep 4, 2026, OPENED) and Under Armour (Earnest, Apr 2024, OPENED). Shopper overlap is about twice as high with Lululemon as with Nike (Vuori 52% vs 30%; Alo 63% vs 34%).

What does hold (the opportunity cost):
- **Nike under-participated in the 2020 to 2023 athleisure boom.** Nike NA apparel grew +13.1% FY2019 to FY2023 ($5,260M to $5,947M) while Lululemon US grew +122% ($2,854M to $6,346M). Roughly half of US athleisure growth went to one challenger. That is a share loss, but in a growing pie; it shows up as foregone growth, not as the FY2025 revenue fall.
- **Women's lagged Men's before the decline.** On the consistent wholesale-equivalent basis, Women's grew +4.4% FY2021 to FY2024 vs Men's +13.5% (FY2022 10-K p. 32; FY2024 10-K p. 34). Women's share of Men's plus Women's fell from 30.9% to 29.2%. Management repeatedly called Women's "underserved" and a "growth opportunity" in that window.
- **FY2024 apparel units fell 9%** globally (NA -6%), masked by ASP +9 points (FY2024 10-K p. 35, 39). That is consistent with volume leakage, though footwear units also fell 7% in NA that year, so it is not apparel-specific.
- **Teen mindshare:** Lululemon was the No. 1 apparel brand for upper-income female teens from Fall 2021 to Spring 2024 (Piper Sandler via SGB, OPENED). Nike stayed No. 1 overall in teen apparel throughout (30% to 35%, 28% in Spring 2025, still No. 1 in Fall 2025).
- **Disclosure retreat:** Nike dropped the revenue-by-consumer table and every "Women's" attribution from the FY2026 10-K and FY2026 10-Qs (zero mentions vs 7 in the FY2025 10-K and 18 in FY2024; my count). BNP Paribas called it "a red flag ... particularly since women's was supposed to be a long-term growth driver" (Fortune, Jul 4, 2026, OPENED). This is a legitimate warning sign that Women's has not re-accelerated, but it is also consistent with Hill's reorganisation from a Men's/Women's/Kids construct to sport teams.

**Independent cause or symptom?** To the extent it exists, it is a symptom. Nike's women's and apparel under-performance in FY2021 to FY2024 coincides with the Consumer Direct Acceleration choices already documented in `org_talent.md`, `innovation_drought.md` and `franchise_oversupply.md`: product teams reorganised by gender rather than sport, a lifestyle footwear (Dunk, AF1, AJ1) concentration, and a digital-first funnel. Nike's Women's business was also footwear-heavy (Dunk "led" Women's in Q2 FY2024), so even the Women's decline in FY2025 is largely the classics footwear fade, not leggings.

**Contribution estimate:** about **0% to 10% of the FY2024 to FY2026 decline, central about 3% (roughly $150M)**. Direct: apparel lost $326M over the period, and only a fraction of that sits where the named challengers operate (NA apparel *grew*). Upper bound: assign all of the FY2025 Women's decline (-$647M) and all NA apparel loss in FY2025 to the hypothesis, which still gives less than 13% of the FY2025 decline and is clearly too generous (Women's includes footwear, and NA apparel recovered the next year). As an opportunity cost (growth Nike did not get in 2020 to 2023), it is larger, plausibly $1B to $2B of annual revenue Nike might have had if it had held its share of US athleisure, but that is not what fell.

**Fixable by management: partly.** Nike's apparel is already recovering in NA, its "away from body" fleece (Studio Fleece, the best-performing apparel collection of Q1 FY2027) fits the current silhouette shift that is hurting Lululemon's leggings, NikeSKIMS gives it a women's fashion-adjacent entry, and Heidi O'Neill, the Nike executive credited with growing women's apparel, now runs Lululemon. What management cannot fix: Alo, Vuori and Lululemon now have permanent store fleets and loyal premium customers in women's yoga and lounge, a niche Nike never owned.

---

## 2. Predictions and results

| # | Prediction if the hypothesis is true | Result | Held? |
|---|---|---|---|
| P1 Category | The decline should be concentrated in apparel, and apparel's share of revenue should fall | Apparel -$326M FY24 to FY26 vs footwear -$3,902M; apparel was 6.6% of the NIKE, Inc. decline. Apparel share of NIKE Brand rose 27.9% to 29.7%. In FY25 alone apparel was -$810M (16% of the -$5,053M decline), then recovered +$484M in FY26 (FY2026 10-K p. 32). | **No** |
| P2 Geography | Apparel losses should be largest in North America, where Lululemon, Alo and Vuori do most of their sales | NA apparel +$122M FY24 to FY26 (+2.0%), new high of $6,075M; +6% in Q1 FY27. Losses are in Greater China (-16.0%) and EMEA (-3.9%). Lululemon's US share of revenue is 57% (FY2025). | **No** (inverse) |
| P3 Gender | Women's should fall faster than Men's and account for more than its weight of the decline | FY25: Women's -6% (-$647M), Men's -6%, Kids' -5%, Jordan -16%. Women's 21.0% of revenue, 14.0% of the decline (FY2025 10-K p. 33). | **No** |
| P4 Timing | Nike's decline should coincide with the challengers' fastest growth | Lululemon US +122% FY2019 to FY2023 while Nike grew; Lululemon US flat to down from FY2024, -8% in Q2 FY2026. Nike's decline started Q1 FY2025, when Lululemon's own US business stopped growing. Jun to Aug 2026: Nike NA apparel +6%, Lululemon US -8%. | **No** for the decline. **Yes** for a pre-2024 share loss in a growing market. |
| P5 Who gains | Alo and Vuori's share gains should come substantially from Nike | Earnest (Apr 2024): Alo and Vuori +1 point each; Under Armour lost share; Adidas, Athleta, Fabletics steady or up. Shopper overlap: Vuori 52% Lululemon vs 30% Nike; Alo 63% vs 34%. M Science (Aug 2026): Lululemon -10 points; Alo +5.9; Vuori +2.2. Earnest: Nike 31.6% of US athleisure spend vs Lululemon 21.2%, Vuori 2.9%, Alo 1.3% (SNIPPET, date unclear). | **Mostly no.** The donors are Lululemon and Under Armour. One weak data point for: Vuori shoppers spent 17% less at Nike DTC in Apr 2024 (but Nike was cutting its own DTC at the time). |
| P6 Mindshare | Nike's teen apparel mindshare should fall and the athleisure brands should rise | Nike No. 1 in teen apparel every survey: 30% (Spr 22), 31%, 33%, 35% (Fall 23), 34%, 33%, 28% (Spr 25), still No. 1 (Fall 25). Lululemon No. 3 at 5% to 6%, losing 4 points among upper-income teens in Spring 2025. The Spring 2025 gainers were Hollister and American Eagle (denim, fashion), not Alo or Vuori. Alo and Vuori reached No. 11 and No. 15 among upper-income teens (Spring 2024) and then did not break into the top 3. | **Partly.** Nike's apparel mindshare dipped 2025, but to fashion brands, and Lululemon fell further. |
| P7 Peer control | If athleisure substitution is a general force, incumbent sportswear apparel should struggle everywhere | adidas apparel +15% c-n in 2025 and +35% c-n in Q2 2026 (footwear +1%); Under Armour (the true athleisure casualty) shrinking. Incumbent apparel can grow strongly in this market; Nike's issue, if any, is relative to adidas, not to yoga brands. | **No** for the yoga/lounge challengers; the apparel share Nike is losing in 2025 to 2026 goes to adidas (Three Stripes, Firebird, football). |
| P8 Pre-decline lag | Women's and apparel should have lagged in FY2021 to FY2024, before the revenue fall | Women's WE +4.4% vs Men's +13.5% (FY21 to FY24). NA apparel +13.1% FY19 to FY23 vs Lululemon US +122%. FY24 apparel units -9% globally, masked by ASP. Management repeatedly flagged women's as "underserved". | **Yes** (as opportunity cost, not decline) |

---

## 3. Evidence in detail

### 3.1 Nike apparel by geography (USD millions, as reported)

| Fiscal year | North America | EMEA | Greater China | APLA | NIKE Brand apparel | Source |
|---|---|---|---|---|---|---|
| FY2019 | 5,260 | 3,087 | 1,808 | 1,395 | 11,550 | FY2021 10-K p. 37 (prior-year column), FY2019 10-K p. 27 |
| FY2020 | 4,639 | 3,053 | 1,896 | 1,365 | 10,953 | FY2021 10-K p. 37 |
| FY2021 | 5,028 | 3,996 | 2,347 | 1,494 | 12,865 | FY2021 10-K p. 32, 37 |
| FY2022 | 5,492 | 4,527 | 1,938 | 1,610 | 13,567 | FY2022 10-K p. 32, 37 |
| FY2023 | 5,947 | 4,566 | 1,666 | 1,664 | 13,843 | FY2023 10-K |
| FY2024 | 5,953 | 4,380 | 1,828 | 1,614 | 13,775 | FY2024 10-K p. 34, 39 to 42 |
| FY2025 | 5,837 | 3,971 | 1,616 | 1,541 | 12,965 | FY2025 10-K p. 33, 38 |
| FY2026 | 6,075 | 4,210 | 1,535 | 1,629 | 13,449 | FY2026 10-K p. 32, 37 to 40 |
| Q1 FY2027 | 1,566 (+6%) | 1,163 (+5%) | 279 (-23%, -27% c-n) | 376 (+1%) | 3,384 (+2%) | Q1 FY2027 10-Q p. 22, 26 to 29 |

FY2024 to FY2026 change (my arithmetic): NA apparel +122 (+2.0%) vs NA footwear -1,220 (-8.4%); EMEA apparel -170 (-3.9%) vs footwear -830 (-9.8%); Greater China apparel -293 (-16.0%) vs footwear -1,364 (-24.6%); APLA apparel +15 vs footwear -488. **In every geography apparel held up better than footwear.**

10-K narrative (OPENED (cache), verbatim):
- FY2024 10-K p. 35: "NIKE Brand apparel revenues were flat on a currency-neutral basis, primarily due to lower revenues in Men's and Women's, offset by higher revenues in Kids'. Unit sales of apparel decreased 9%, while higher ASP per unit contributed approximately 9 percentage points of apparel revenue growth."
- FY2024 10-K p. 39 (North America): "Apparel revenues were flat on a currency-neutral basis due to lower revenues in Men's, Women's and the Jordan Brand, offset by higher revenues in Kids'. Unit sales of apparel decreased 6%..."
- FY2025 10-K p. 38 (North America): "Apparel revenues decreased 2% on a currency-neutral basis. Unit sales of apparel decreased 1%, while lower ASP per unit reduced apparel revenues by approximately 1 percentage point. Lower ASP per unit was primarily due to higher discounts and changes in channel mix". Compare footwear: "-13% ... Unit sales of footwear decreased 10%".
- FY2026 10-K p. 37 (North America): "Apparel revenues increased 4% on a currency-neutral basis. Unit sales of apparel increased 2%, while higher ASP per unit contributed approximately 2 percentage points".

### 3.2 Nike revenue by consumer (Women's vs Men's)

Wholesale-equivalent basis (non-GAAP; Jordan separated from FY2022 10-K on):

| FY | Men's | Women's | Kids' | Jordan | Source |
|---|---|---|---|---|---|
| FY2020 | 16,430 | 6,954 | 4,199 | 3,687 | FY2022 10-K p. 32 |
| FY2021 | 18,391 | 8,225 | 4,882 | 4,780 | FY2022 10-K p. 32 |
| FY2022 | 18,797 | 8,273 | 4,874 | 5,122 | FY2022 10-K p. 32 |
| FY2023 | 20,733 | 8,606 | 5,038 | 6,589 | FY2023 10-K p. 32; FY2024 10-K p. 34 |
| FY2024 | 20,868 | 8,586 | 5,111 | 6,988 | FY2024 10-K p. 34 |

Reported-revenue basis (recast in FY2025 10-K after wholesale equivalent was dropped):

| FY | Men's | Women's | Kids' | Jordan | Others | Source |
|---|---|---|---|---|---|---|
| FY2023 | 24,445 | 10,274 | 5,889 | 8,460 | (363) | FY2025 10-K p. 33 |
| FY2024 | 24,785 | 10,366 | 6,019 | 8,701 | (594) | FY2025 10-K p. 33 |
| FY2025 | 23,216 (-6%) | 9,719 (-6%, -5% c-n) | 5,695 (-5%) | 7,270 (-16%) | (1,234) | FY2025 10-K p. 33 |
| FY2026 | not disclosed | not disclosed | | | | FY2026 10-K: table removed; zero "Women's" mentions |

My arithmetic, FY2024 to FY2025 NIKE Brand decline of $4,608M: Men's -1,569 (34.0%), Women's -647 (14.0%), Kids' -324 (7.0%), Jordan -1,431 (31.1%), Others -640 (13.9%). Women's weight in FY2024 revenue was 21.0%, so Women's under-indexed the decline by 7 points.

Wholesale-equivalent growth FY2021 to FY2024: Women's +4.4%, Men's +13.5%. FY2020 to FY2024: Women's +23.5%, Men's +27.0%. Women's share of Men's plus Women's: 30.9% (FY2021) to 29.2% (FY2024).

Management on Women's size: "we're the largest Women's athletic brand in the world today at $8.5 billion" (Matt Friend, Q4 FY2021 call, Jun 24, 2021, OPENED (cache)); "Women's, which is already a roughly $9 billion business, and that's just a NIKE brand, excluding Jordan and Converse. Our Women's business has grown high single digits on average over the past 3 years" (Q2 FY2024 call, Dec 21, 2023, OPENED (cache)). The 10-K wholesale-equivalent series ($8,225M FY2021 to $8,586M FY2024) does not support high-single-digit growth from FY2021; it does from the COVID-depressed FY2020 base. The FY2021 10-K first printed FY2021 Women's at $8,555M before a later restatement to $8,225M (FY2021 10-K p. 32 vs FY2022 10-K p. 32).

### 3.3 Management commentary on Women's, leggings and athleisure (Nike official transcripts, OPENED (cache), Q1 FY2021 to Q1 FY2027)

- Q4 FY2023 (Jun 29, 2023), Donahoe: "We are blessed with structural tailwinds around an expanding definition of sport, particularly around health and wellness and a related structural tailwind around this movement toward athleisure."
- Q1 FY2024 (Sep 28, 2023): "we have opportunity to deliver more compelling assortments particularly when it comes to serving our Women's consumers." Also: "Zenvy, Go and Universa fueled double-digit growth in statement leggings".
- Q2 FY2024 (Dec 21, 2023): statement leggings "all of which are above $100, a price point we were not previously in"; "statement leggings fueled our fitness apparel growth in Women's for the quarter"; "Within Women's, Dunk, Free Metcon and our $100-plus statement leggings delivered strong growth."
- Q4 FY2024 (Jun 27, 2024): "statement leggings, a key focus for us, were up high double-digits in Q4"; "our Lifestyle business declined in Q4 across Men's, Women's, and Jordan".
- Q1 FY2025 (Oct 1, 2024): "Our men's and women's lifestyle business was planned down double digits in Q1".
- Q3 FY2025 (Mar 20, 2025): announcement of NikeSKIMS. Q4 FY2025 (Jun 26, 2025): "We entered over 200 women's-led doors, including boutiques like Aritzia"; "women's sportswear, footwear returned to growth in the quarter"; and Hill: "Instead of a men's, women's and kids' construct, NIKE, Jordan and Converse teams will now come to work every day with a mission to create the most innovative and coveted product..."
- Q2 FY2026 (Dec 18, 2025): "SKIMS had a successful launch."
- Q1 FY2027 (Oct 1, 2026): "We launched Studio Fleece for women and Solo Fleece for men during back-to-school season, and the Studio Fleece was the best-performing apparel collection of the quarter in all of NIKE, Inc."; "NIKE Sportswear and the Jordan Brand, including men's, women's and kids, represented a high single-digit drag on consolidated NIKE."

Reading: management never named Lululemon, Alo or Vuori as a cause of the decline in 25 quarters of calls (my search of all transcripts for "lululemon", "Alo", "Vuori", "yoga", "athleisure"). The decline drivers it named are Sportswear and Jordan (footwear-led classics), China and Converse. Leggings were a growth line through FY2024.

### 3.4 Lululemon (the main named challenger): its own US numbers

| Lululemon fiscal year (ends late Jan/early Feb) | US net revenue ($M) | Women's apparel / women's product ($M) | China Mainland ($M) | Source |
|---|---|---|---|---|
| FY2018 | 2,363 | 2,335 (women's product) | | 10-K FY2020 p. 72 approx. (OPENED) |
| FY2019 | 2,854 | 2,768 | | same |
| FY2020 | 3,105 | 3,050 | | same |
| FY2021 | 4,346 | 4,172 | | 10-K FY2023 p. 79 approx. (OPENED) |
| FY2022 | 5,654 | 5,260 | | same |
| FY2023 | 6,346 | 6,147 | 964 | 10-K FY2025 p. 57 approx. (OPENED) |
| FY2024 | 6,483 | 6,693 | 1,361 | same |
| FY2025 | 6,328 | 6,995 | 1,755 | same |
| Q2 FY2026 (May to Aug 2, 2026) | 1,302 (vs 1,415, -8.0%) | | 407 (+4%) | 10-Q filed Sep 3, 2026, p. 10 (OPENED) |
| H1 FY2026 | 2,615 (vs 2,778, -5.8%) | | | same |

Lululemon 10-Q (Sep 3, 2026, p. 21, OPENED): "Net revenue in the Americas decreased 8%, and comparable sales in the Americas decreased 12%. We experienced reduced traffic and lower conversion rates, as well as a decrease in average order value in the Americas."

My arithmetic: Lululemon US +$3,492M (+122%) FY2019 to FY2023, versus Nike NA apparel +$687M (+13.1%) FY2019 to FY2023. From FY2023 to FY2025 Lululemon US -0.3%; Nike NA apparel FY2024 to FY2026 +2.0%. China is the exception: Lululemon China Mainland +$791M FY2023 to FY2025 while Nike Greater China apparel fell $293M FY2024 to FY2026; some substitution in China is plausible, but Nike China footwear fell much faster (-24.6%) and `china.md` attributes China to a brand-wide problem.

Page numbers for Lululemon tables are from the nearest page footer in my text extraction and are approximate.

### 3.5 Alo and Vuori

- **Reuters (Neil J Kanatt, Juveria Tabassum), "Lululemon dives on risks of prolonged turnaround under new CEO", Sep 4, 2026**, syndicated at lufkindailynews.com (OPENED): "Sales of Lululemon's leggings declined about 20% in the second quarter, while its share of the athleisure market shrank 10 percentage points to 43.9% in August, according to data from M Science. Meanwhile, shares of newer rivals Alo and Vuori grew 5.9 percentage points and 2.2 percentage points, respectively." Interim CEO Meghan Frank: "there are shifts occurring with guests looking for away from body silhouettes." On O'Neill: "O'Neill's tenure at Nike, where she is credited with growing the women's apparel business, could assist Lululemon's efforts".
- **Retail Dive (Cara Salpini), "Alo Yoga, Vuori gaining share in activewear market, report finds", Apr 26, 2024** (OPENED), citing Earnest Analytics: "In the last 12 months, both brands have gained 1% market share, while Under Armour lost share ... Athleta, Adidas and Fabletics all either held steady on market share year over year or grew share." Shopper overlap "Lululemon (52% for Vuori, 63% for Alo Yoga) and Nike (30% and 34%, respectively)". "Vuori shoppers spent 17% less through Nike's DTC channels this April than the same timeframe last year." Piper Sandler: "Alo Yoga and Vuori came in 11th and 15th" among upper-income teens (Spring 2024) vs 35th and 24th in Fall 2023.
- **Earnest share of US athleisure spend** (Nike 31.6%, Lululemon 21.2%, Athleta 4.4%, Fabletics 4.4%, Vuori 2.9%, Alo 1.3%), via Retail TouchPoints (SNIPPET; page returned 403; snapshot date not visible). Earnest's own page returned 403.
- **Size:** Alo has never published revenue; Forbes (Apr 2025) estimated close to $2B for the parent Color Image Apparel including the since-sold Bella+Canvas (SNIPPET via theindustry.fashion and Forbes Australia). Vuori about $1B (analyst estimate, NBC News, 2024, SNIPPET), valued at $5.5B. Both are small relative to Nike's $13.4B apparel business and mostly US.

### 3.6 Teen mindshare (Piper Sandler Taking Stock With Teens)

Infographics Spring 2022 to Spring 2025, pipersandler.com/sites/default/files/document/TSWT_*_Infographic.pdf (OPENED (cache), downloaded today by a sibling researcher; Fall 2025 and Spring 2026 PDFs return 404):

| Survey | Nike share of favorite clothing brand (all teens) | Lululemon | Notes |
|---|---|---|---|
| Spring 2022 | 30%, No. 1 | No. 3, 5% | "LULU gains 300 bps Y/Y"; athletic brands 44% of favorite apparel, most ever |
| Fall 2022 | 31%, No. 1 | top 3 | |
| Spring 2023 | 33%, No. 1 | No. 3, 6% | |
| Fall 2023 | 35%, No. 1 | top 3 | Female teen apparel spend -9% Y/Y |
| Spring 2024 | 34%, No. 1 | No. 3, 5% | Lululemon "No. 1 among female upper-income teens"; Alo No. 11, Vuori No. 15 |
| Fall 2024 | 33%, No. 1 | No. 3, 5% (-1 pt); upper income -4 pts | Adidas female footwear 3% to 14% |
| Spring 2025 | 28%, No. 1 | not top 3 | Hollister 8%, American Eagle 6% |
| Fall 2025 | No. 1 | not top 3 | "Nike continues to dominate as the top clothing brand for teens with Hollister ranking number two and Brandy Melville a distant third among upper income teens" (Piper Sandler release, Oct 9, 2025, pipersandler.com, OPENED) |

SGB Media, Apr 10, 2025 (OPENED): Lululemon "No. 1 apparel brand for upper income females from fall 2021 to spring 2024. Lululemon lost 4 points of mindshare Y/Y." SGB Media, Apr 22, 2026 (OPENED): the survey moves to once a year; the 2026 study arrives in the fall (not yet published).

### 3.7 Peer control: adidas apparel

- adidas Q2 2026 release (adidas-group.com, OPENED (cache)): "Apparel revenues increased 35% on a currency-neutral basis in the second quarter"; "Footwear revenues were up 1%"; North America +17%.
- adidas FY2025 investor call deck (OPENED (cache)): adidas brand FY2025 product division growth footwear +12%, apparel +15%, accessories +6% (currency-neutral; my reading of the chart labels).
- adidas FY2024 release, Mar 5, 2025 (OPENED (cache)): "Apparel revenues grew 6% in 2024"; "Apparel revenues in Originals benefited from the increasing popularity of the Three Stripes through offerings such as Adicolor and Firebird."

Reading: an incumbent sportswear brand is growing apparel at double-digit rates while Lululemon's US business shrinks. The apparel share Nike is plausibly giving up in 2025 to 2026 goes to adidas (retro, football, Three Stripes), not to yoga and lounge brands. This overlaps with `challengers_taste.md`.

### 3.8 Disclosure retreat

- Count of "Women's" in the Nike filings (my grep of full text): FY2023 10-K 17, FY2024 10-K 18, FY2025 10-K 7, FY2026 10-K 0, Q2 FY2026 10-Q 0, Q3 FY2026 10-Q 0, Q1 FY2027 10-Q 0.
- Fortune (Phil Wahba), "Nike earnings: Elliott Hill's nascent comeback", Jul 4, 2026 (OPENED): Nike was "unexpectedly dialing back some disclosures in its financial results, such as a breakdown of sales by gender." BNP Paribas (Laurent Vasilescu): "Pulling back on yet another disclosure is a red flag to us particularly since women's was supposed to be a long-term growth driver."

---

## 4. Alternative explanations for what the hypothesis tries to explain

| Observation that might seem to support the hypothesis | Better explanation | Evidence |
|---|---|---|
| Women's fell 6% in FY2025 | Women's was footwear-heavy (Dunk, AF1); the classics fade hit all consumer groups equally; Jordan fell most | FY2025 10-K p. 33; Q2 FY2024 call "Within Women's, Dunk ... delivered strong growth"; `franchise_oversupply.md` |
| Nike apparel fell 6% in FY2025 | NIKE Direct and digital collapse (-19% NA digital), heavy discounting, then recovery as wholesale reopened | FY2025 10-K p. 38: lower ASP "due to higher discounts and changes in channel mix"; `dtc_wholesale.md` |
| Greater China apparel -16% FY24 to FY26 | China brand-wide collapse (footwear -24.6%) | `china.md` |
| Nike teen apparel mindshare down in Spring 2025 | Fashion rotation to denim and mall brands (Hollister, American Eagle); Lululemon fell too | Piper Sandler Spring 2025 |
| Alo and Vuori growth | Share taken mainly from Lululemon and Under Armour | M Science via Reuters; Earnest via Retail Dive |

---

## 5. Contribution estimate (my arithmetic)

- **Direct revenue lost by Nike apparel, FY2024 to FY2026:** $326M = 6.6% of the $4,964M NIKE, Inc. decline. Of that, North America (the only market where Lululemon, Alo and Vuori are large) contributed **+$122M**, i.e. no loss.
- **Generous upper bound for FY2025 alone:** Women's -$647M plus NA apparel -$116M, ignoring overlap and the fact that Women's includes footwear: $763M, or 15% of the FY2025 decline. Realistically Women's footwear (classics) is most of the -$647M, and NA apparel recovered the next year, so this bound is far too high.
- **Central estimate:** about 3% (about $150M) of the decline, range 0% to 10%. Most plausible residual: a small, persistent US women's premium-legging and lounge leakage, plus some China substitution toward Lululemon.
- **Opportunity cost (not part of the decline):** had Nike NA apparel grown in line with the US athleisure leaders from FY2019 to FY2023, it could plausibly be $1B to $2B larger today. This is speculative and depends on market-size data I could not open (Circana and Euromonitor apparel share tables not accessible).

---

## 6. Sources

| # | Source | Date | Status | Used for |
|---|---|---|---|---|
| 1 | Nike FY2021 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018721000028/nke-20210531.htm | 2021-07-20 | OPENED (cache) | Apparel by geography FY2019 to FY2021 (p. 32, 37); Women's WE (p. 32) |
| 2 | Nike FY2022 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018722000038/nke-20220531.htm | 2022-07-21 | OPENED (cache) | Women's, Men's WE FY2020 to FY2022 (p. 32); NA apparel (p. 37) |
| 3 | Nike FY2023 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018723000039/nke-20230531.htm | 2023-07-20 | OPENED (cache) | Consumer WE table (p. 32); apparel by geography |
| 4 | Nike FY2024 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018724000044/nke-20240531.htm | 2024-07-25 | OPENED (cache) | Apparel p. 34, 39 to 42; consumer WE p. 34; apparel units p. 35, 39 |
| 5 | Nike FY2025 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018725000047/nke-20250531.htm | 2025-07-17 | OPENED (cache) | Revenue by consumer (p. 33); NA narrative (p. 38) |
| 6 | Nike FY2026 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm | 2026-07-15 | OPENED (cache) | Apparel p. 32 to 40; FY2026 narrative p. 33, 37; no consumer table |
| 7 | Nike Q1 FY2027 10-Q, https://www.sec.gov/Archives/edgar/data/320187/000032018726000193/nke-20260831.htm | 2026-10-02 | OPENED (cache) | Q1 FY2027 apparel by geography (p. 14, 22, 26 to 29) |
| 8 | Nike Q2 and Q3 FY2026 10-Qs (URLs in `04_financial_data_pack.md`) | 2025-12-30, 2026-04-01 | OPENED (cache) | Zero "Women's" mentions |
| 9 | Nike official earnings call transcripts Q1 FY2021 to Q1 FY2027, investors.nike.com (q4cdn PDFs), incl. https://s1.q4cdn.com/806093406/files/doc_financials/2027/q1/NIKE-Inc-Q1FY27-OFFICIAL-Transcript_-FINAL.pdf | 2020-09 to 2026-10-01 | OPENED (cache; Q1 FY2027 also re-downloaded) | All management quotes in 3.3 |
| 10 | Lululemon FY2025 10-K, https://www.sec.gov/Archives/edgar/data/1397187/000139718726000020/lulu-20260201.htm | 2026-03-17 | OPENED | US, China, women's apparel FY2023 to FY2025 |
| 11 | Lululemon Q2 FY2026 10-Q, https://www.sec.gov/Archives/edgar/data/1397187/000139718726000127/lulu-20260802.htm | 2026-09-03 | OPENED | US -8%, Americas comps -12% |
| 12 | Lululemon FY2023 10-K, https://www.sec.gov/Archives/edgar/data/1397187/000139718724000010/lulu-20240128.htm | 2024-03-21 | OPENED | US FY2021 to FY2023, women's product |
| 13 | Lululemon FY2020 10-K, https://www.sec.gov/Archives/edgar/data/1397187/000139718721000009/lulu-20210131.htm | 2021-03-30 | OPENED | US FY2018 to FY2020, women's product |
| 14 | Reuters via Lufkin Daily News, "Lululemon dives on risks of prolonged turnaround under new CEO", https://lufkindailynews.com/news_reuters/business/lululemon-dives-on-risks-of-prolonged-turnaround-under-new-ceo/article_f8719526-5dc9-5378-a38c-785acdbda2db.html | 2026-09-04 | OPENED | M Science share data, leggings -20%, O'Neill |
| 15 | Retail Dive, "Alo Yoga, Vuori gaining share in activewear market, report finds", https://www.retaildive.com/news/alo-yoga-vuori-gaining-activewear-market-share/714384/ | 2024-04-26 | OPENED | Earnest share gains, shopper overlap |
| 16 | Retail TouchPoints, "Athleisure Faceoff", https://www.retailtouchpoints.com/features/athleisure-faceoff-how-lululemon-vuori-alo-and-fabletics-are-making-their-case-to-consumers-2/616614/ | unclear (2025) | SNIPPET (403) | Earnest Nike 31.6% vs Lululemon 21.2% |
| 17 | Earnest Analytics, https://www.earnestanalytics.com/insights/athleisure-shoppers-lean-into-vuori-alo-yoga | 2024-04 | SNIPPET (403) | Same as 15 |
| 18 | Piper Sandler TSWT infographics Spring 2022 to Spring 2025, pipersandler.com/sites/default/files/document/TSWT_*_Infographic.pdf | 2022-04 to 2025-04 | OPENED (cache) | Teen apparel mindshare |
| 19 | Piper Sandler, "Piper Sandler Completes 50th Semi-Annual Teen Survey", https://www.pipersandler.com/news/piper-sandler-completes-50th-semi-annual-teen-survey | 2025-10-09 | OPENED | Fall 2025 clothing ranking |
| 20 | SGB Media, "Piper Sandler Survey Reveals Nike, Lululemon and Stanley Losing Teen Mindshare", https://sgbonline.com/piper-sandler-survey-reveals-nike-lululemon-and-stanley-losing-teen-mindshare/ | 2025-04-10 | OPENED | Lululemon No. 1 upper-income female 2021 to 2024 |
| 21 | SGB Media, "Piper Sandler's Taking Stock With Teens Becomes an Annual Event", https://sgbonline.com/piper-sandlers-taking-stock-with-teens-becomes-an-annual-event/ | 2026-04-22 | OPENED | Survey format change |
| 22 | Fortune (Phil Wahba), https://fortune.com/2026/07/04/nike-earnings-elliott-hill-nascent-comeback/ | 2026-07-04 | OPENED | Gender disclosure removed; BNP quote |
| 23 | adidas Q2 2026 release, https://www.adidas-group.com/en/media/press-releases/adidas-grows-top-line-14percent-and-achieves-record-sales-in-q2 | 2026-07/08 | OPENED (cache) | Apparel +35% c-n |
| 24 | adidas FY2025 investor call deck (Investor_Call_FY_2025_final), adidas-group.com | 2026-03 | OPENED (cache) | FY2025 apparel +15% |
| 25 | adidas FY2024 results release | 2025-03-05 | OPENED (cache) | Apparel +6% in 2024 |
| 26 | Forbes / theindustry.fashion (Alo size); NBC News (Vuori size) | 2024 to 2026 | SNIPPET | Challenger scale only |
| 27 | Needham downgrade of Lululemon via StreetInsider | 2025 | SNIPPET | "Alo, Vuori, Fabletics, Athleta ... stifling LULU's growth" |
| 28 | Repo notes: `challengers_taste.md`, `franchise_oversupply.md`, `china.md`, `dtc_wholesale.md`, `org_talent.md`, `innovation_drought.md` | 2026-10-13 | OPENED (repo) | Cross-references |

## 7. Gaps

- No Circana or Euromonitor US activewear apparel share series opened; the market-size counterfactual in section 5 is therefore a rough range.
- Nike does not disclose women's apparel separately, and stopped disclosing revenue by consumer in FY2026, so the FY2026 and Q1 FY2027 Women's trend cannot be tested from filings.
- Piper Sandler Fall 2025 full infographic (apparel percentages) not obtained; only the release text.
- Alo and Vuori revenues are private estimates only.
