# U_REVIEWS: Consumer review tone for Nike, following Jin (2023)

> Repository copy: aggregated and product-level CSVs are in `data/reviews/`, scripts in `scripts/reviews/`. Review-level files (individual review text, which can include reviewer nicknames) and the large filtered dataset are not committed; the scripts regenerate them from the public sources.

Prepared 2026-10-13. Method: Jin, S. (2023), "More than words: Can tone of consumer product reviews help predict firms' fundamentals?", Journal of Business Finance & Accounting 50:1910-1942 (Section 3.1.1, Appendix A, Appendix C). Everything here is alternative data built from public review pages and a public academic dataset. It is one firm, a short sample and simple correlations, not the paper's 292-firm panel regression.

## A. Plain-English summary (for a finance beginner)

1. **What we collected.** About 3.1 million Amazon reviews (2005 to Sep 2023) of shoes and apparel sold under Nike, Jordan, Converse and nine rival brands; about 151,000 newer reviews (2021 to Oct 2026) from nike.com and Foot Locker (with some overlap, because Foot Locker shows reviews copied from brand sites); and snapshots of how many items each brand lists at Foot Locker, on nike.com and in Amazon Best Seller lists.
2. **What "tone" means.** Each review has a one-line summary ("Love these!", "Fell apart after a month"). A simple machine-learning model (Naive Bayes, as in the paper) reads the summary and scores it from -1 (very negative) to +1 (very positive). AbnormalTone is this quarter's average tone minus the average of the previous four quarters, so it says whether shoppers are getting happier or unhappier than usual.
3. **Nike's Amazon reviews got clearly worse from 2020 to late 2021, more than rivals'.** Nike's average Amazon star rating fell from 4.39 (Dec 2019 to Feb 2020) to 3.90 (Sep to Nov 2021), and the share of 1 to 2 star reviews roughly doubled, from 11% to 23%. Rivals slipped too, but Nike went from in line with peers to the worst of the ten firms, about 0.2 stars below the peer average.
4. **Part of that is a channel story, not only a product story.** Nike stopped selling directly on Amazon in late 2019, so later Amazon reviews of Nike goods mostly describe purchases from third-party sellers. Mentions of "fake" or "counterfeit" in Nike reviews tripled (0.6% of reviews in FY2017 to 1.9% in FY2023), the highest of any brand tracked. Amazon tone after 2019 therefore partly measures the reseller experience, not just Nike's shoes.
5. **The Amazon gap stopped widening in late 2021.** Nike's tone gap versus peers was worst in Sep to Nov 2021 (-0.10) and narrowed to about -0.06 in FY2023; Nike's AbnormalTone was positive in three of the last four quarters the dataset covers.
6. **On nike.com, unpaid reviews show a second, later slide that looks like it bottomed in early 2026.** Among reviews not flagged as incentivized, the average rating fell from 4.80 (Sep to Nov 2023) to 4.47 (Dec 2025 to Feb 2026), and 1 to 2 star reviews rose from 2% to 9%. In Jun to Aug 2026 the rating recovered to 4.54 and AbnormalTone turned positive for the first time since early 2024. At the same time the share of incentivized (free-product) reviews jumped from 12% to 20% in 2021 to 2024 to 34% in 2025 and 42% in 2026, which props up Nike's headline rating.
7. **Shelf space is recovering.** Nike, Jordan and Converse together held 67% of the men's shoe listings of the major athletic brands at Foot Locker in Jan 2021, fell to about 35% in late 2022 and 2023, and are back near 49% in Oct 2026. Nike Inc items took about 2% of the slots in Amazon's top-30 shoe Best Seller lists in 2022 and about 8% in the second half of 2026.
8. **Did tone predict Nike's sales? Not reliably in this small sample.** Over 22 fiscal quarters (Q4 FY2018 to Q1 FY2024) Nike's AbnormalTone had essentially no correlation with next-quarter revenue growth (r = -0.14) or next-quarter NIKE Direct growth (r = -0.22, 14 quarters). Excluding the COVID quarters, the sign turns to what the paper predicts (r = +0.41 with next-quarter abnormal sales, n = 17, p = 0.11; negative tone changes alone r = +0.46, p = 0.06), but nothing passes a 5% significance test. Use review tone as a cross-check on product sentiment, not as a stand-alone sales forecast.

## B. Method

### B1. Sources and URLs

| Source | What | URL / access | Sample |
|---|---|---|---|
| Amazon Reviews 2023 (McAuley Lab, UCSD) metadata | store/brand, title, categories | https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/meta_categories/meta_Clothing_Shoes_and_Jewelry.jsonl.gz (4.05 GB, streamed, never saved) | 7,218,481 items read; 359,097 matched |
| Amazon Reviews 2023 reviews | rating, summary (title), text, timestamp, verified purchase, helpful votes | https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/review_categories/Clothing_Shoes_and_Jewelry.jsonl.gz (7.11 GB, streamed) | 66,033,346 reviews read; 3,182,474 matched; 3,144,610 after dedupe |
| nike.com reviews | TurnTo review CDN that nike.com product pages call (site key is in the page source): https://cdn-ws.turnto.com/v5/sitedata/{key}/{style}/d/review/en_US/0/1000/RECENT/false/false/ | 1,260 shoe styles, one per model on today's men's, women's and running walls (style codes from the other agent's marketplace/data/nike_current_products.csv) | 74,562 unique reviews, Jun 2016 to Oct 2026 (newest 1,000 per style); 846 styles have reviews |
| Foot Locker reviews | Bazaarvoice display API that footlocker.com product pages call (passkey is in the page source): https://api.bazaarvoice.com/data/products.json and /reviews.json | top 25 products by review count per brand (product stats for the top 200), en_US, newest 1,000 per product, back to Jun 2021 | 76,474 reviews; 2,023 product rows |
| Foot Locker listing pages | brand filter counts, product tiles (review count, rating rounded to whole stars) | https://www.footlocker.com/category/mens/shoes.html and /womens/shoes.html, live (29 brand pages, pageSize=200) and Wayback (https://web.archive.org/web/{ts}id_/...) one snapshot per quarter | 24 men's and 20 women's Wayback snapshots, Jan 2021 to Oct 2026, plus today |
| Amazon Best Sellers | rank, title, brand, stars, rating count | Wayback snapshots of six lists (men's and women's running, athletic, fashion sneakers), one per quarter where archived, plus the other agent's live pages (read-only reuse) | 78 list pages, 3,080 item rows; 60 pages carry stars |
| nike.com wall counts | total shoes on /w/mens-shoes-nik1zy7ok and /w/womens-shoes-5e1x6zy7ok | reused read-only from marketplace/data/nike_wall_history.csv (other agent) | quarterly, 2022 to 2026 |
| Nike fundamentals | quarterly revenues, NIKE Direct growth | /home/user/nike-research-case-comp/data/nike_filing_facts.csv (revenues, growth_nike_direct_reported_pct, revenue_nike_direct), read only | Q1 FY2018 to Q1 FY2027 |

Fetching was polite: 2 to 3 s between requests per site, 5 to 6 s for the Wayback Machine with a 90 s backoff on HTTP 429, public pages only, no logins. Amazon live product and search pages were not touched. The two big files were streamed through a resumable HTTP Range reader and filtered in memory (the first metadata pass was cut off by a dropped connection at 6.19 M rows, so it was rerun in full).

### B2. Brand matching rules (Amazon)

1. Candidate pass: any metadata item whose `store` or `details.Brand` matched a loose brand regex (362,256 candidates).
2. Normalise `store` (strip "Brand: ", "Visit the ... Store", "(Designer)"), lower-case, and require an exact match to an allow-list: Nike = {nike, nike golf, nike sb, nike acg}; Jordan = {jordan, air jordan, nike jordan}; Converse = {converse}; adidas = {adidas, adidas originals, adidas outdoor, adidas by stella mccartney, adidas golf, adidas performance}; HOKA = {hoka one one, hoka}; On = {on, on running, on ag}; New Balance = {new balance}; Brooks = {brooks, brooks heritage}; ASICS = {asics, asics tiger}; Skechers = store names starting "Skechers" plus "Concept 3 by Skechers"; Under Armour = {under armour}; PUMA = {puma, puma golf}. Look-alikes seen in samples and excluded: Brooks Brothers, Ashford & Brooks, Jordan Craig, Julia Jordan, CARE OF by PUMA (an Amazon private label), HKNB Heidi Klum for New Balance.
3. The brand token must appear in the title (drops 1,659 miscategorised items, for example a Samsung screen protector listed under "AIR JORDAN"), and titles with third-party phrasing ("for Nike", "compatible with", "replacement", "shoelaces for") are dropped (44 items). Random samples of each store were read to confirm (for example "ON Running Womens Cloudflow", "HOKA ONE ONE Womens Bondi 6").
4. Firm = Nike Inc for Nike + Jordan + Converse (the paper aggregates at firm level). Matched products: Nike 81,166; adidas 75,643; Skechers 57,701; PUMA 40,814; ASICS 30,961; Under Armour 30,253; New Balance 16,920; Converse 10,376; Brooks 8,697; HOKA 3,126; Jordan 2,789; On 651. Matched reviews after dedupe: Skechers 855,609; adidas 580,053; New Balance 394,690; Nike Inc 375,490 (Nike 320,056, Converse 50,225, Jordan 5,209); Under Armour 330,907; ASICS 302,258; PUMA 206,063; Brooks 85,402; HOKA 9,952; On 4,186. All products are kept (footwear and apparel, as the paper uses all of a firm's products); a `footwear` flag is saved and a footwear-only firm series is in the quarterly files (`level = firm_footwear_only`).
5. Part 2 sources are brand-labelled by the retailer (Foot Locker brand filter, Bazaarvoice brand id, nike.com itself); Amazon Best Seller titles are matched by brand prefix (scripts/brandmatch.py).

### B3. Tone method and variables

* **Text used:** the review summary (Amazon `title`), as in the paper (Section 4.2). Empty summaries get no tone.
* **Naive Bayes (Appendix C):** scikit-learn MultinomialNB on unigram and bigram counts, trained on 15,000 randomly drawn summaries, 80/20 train/test split, three classes. **Deviation:** the paper's 15,000 summaries were hand-coded by two coders; here labels come from stars (4 to 5 = positive, 3 = neutral, 1 to 2 = negative). Test accuracy is 86.2% against an 82.3% "always positive" baseline (the paper reports above 92% against human labels). A 200,000-summary model (87.1% accuracy) is a robustness check (`tone_nb_big`, correlation 0.91 with the main score). Score per summary = P(positive) minus P(negative), in [-1, 1]. A class-based variant (positive class scores P(pos), negative class scores -P(neg), neutral 0, the paper's literal wording) is saved as `tone_nb_class`. Strongest positive n-grams: "five stars", "perfect", "great shoe", "very comfortable"; strongest negative: "two stars", "one star", "poor quality", "terrible", "fell apart", "fake".
* **Lexicon check:** VADER compound score of the summary (`tone_vader`). It correlates 0.49 with the NB score and 0.46 with stars; NB tone correlates 0.70 with stars, partly by construction because stars were the training labels. Old Amazon summaries such as "Five Stars" are machine-generated and tie tone to stars further.
* **Per firm and quarter (calendar and Nike fiscal):** distinct products reviewed (listing proxy), review count, mean stars, share of 1 to 2 star reviews, mean tone, standard deviations. **AbnormalTone** = mean tone in quarter q minus the mean of the previous four quarters' means (all four required); **AbnormalRating** the same for stars; **AbnormalReviewCnt** = (count in q minus mean of previous four) / 100 (paper scales in hundreds); **Negative_AbnormalTone** = min(AbnormalTone, 0) and **Positive_AbnormalTone** = max(AbnormalTone, 0) (the paper splits non-zero AbnormalTone into negative and positive observations). StdDevTone and StdDevRating as in Appendix A.
* **Nike fiscal quarters:** Q1 = Jun to Aug, Q2 = Sep to Nov, Q3 = Dec to Feb, Q4 = Mar to May; FY named after the May year end.
* **Dedupe:** same user + product + timestamp dropped; identical summary-plus-text pairs with text longer than 40 characters dropped even across users (the paper drops duplicates written by different accounts). Window 2005 to Sep 2023.
* **Recent sources:** the same 15k Amazon-trained NB model and VADER score nike.com and Foot Locker review titles (93% of nike.com reviews have a title). Recent quarters run Q1 FY2022 to Q1 FY2027 (Jun to Aug 2026); Q2 FY2027 holds only September 2026 and is shown but not used for conclusions.

### B4. Deviations and caveats

* **The Amazon dataset's coverage collapses from April 2023.** Monthly matched reviews fall from about 28,000 (Jan to Mar 2023) to 17,900 (Apr), 11,400 (May), 7,600 (Jun) and 4,800 (Aug); September has 328. This hits all brands alike, so Q4 FY2023 and Q1 FY2024 star and tone averages are usable but their review counts and AbnormalReviewCnt are not. Q2 FY2024 (September only) is excluded.
* **Nike left Amazon as a direct seller in Nov 2019**, so afterwards Nike's Amazon reviews mostly describe goods bought from third parties. The listing proxy (distinct Nike Inc products reviewed per quarter) fell from about 7,400 (Q3 FY2020) to about 2,000 in FY2023.
* **Platform-wide drift.** All ten firms' Amazon ratings fell from 2020 to 2022 (a common factor). Nike's AbnormalTone correlates 0.82 with the peer-average AbnormalTone over 33 quarters, so a Nike-minus-peers version (RelAbnormalTone) is tested too.
* **Survivorship in Part 2.** nike.com and Foot Locker reviews come from products listed today or the most-reviewed products, so older quarters are mainly reviews of long-lived classics and recent quarters add new launches. Review counts by quarter are not comparable over time; averages (stars, tone, 1 to 2 star share) are more comparable but still mix-sensitive. The newest-1,000 cap per product means heavy-traffic products only reach back to 2023 or 2024.
* **Syndication.** Most Foot Locker reviews are syndicated from brand sites (81% of Nike, 96% of adidas, 96% of HOKA, 89% of New Balance, 4% of On), so Foot Locker's Nike reviews overlap with nike.com. Native-only series are saved separately (`[native FL only]` units).
* **Incentivized reviews.** nike.com flags them; their share was 12% to 20% in 2021 to 2024, then 34% (2025) and 42% (2026). Results are shown with and without them.
* **Foot Locker tile ratings are rounded to whole stars**, so the live tile table (C10) is only a coarse cross-check; Bazaarvoice product stats (C9) carry decimals.
* **Listing counts** at Foot Locker are the counts in the category page's brand filter. The filter list changes over time, so shares use the sum of the focus brands (Nike, Jordan, Converse, adidas, HOKA, On, New Balance, Brooks, ASICS, Skechers, Under Armour, PUMA, Saucony) as the denominator, not all brands. Foot Locker's own assortment decisions (for example its 2025 adidas expansion) move these numbers as much as consumer demand does.
* **Not repeated here:** discount depth and sale share (the other agent's marketplace work).

## C. Tables

Units: stars on a 1 to 5 scale, tone in [-1, 1], shares as fractions unless labelled percent. Peer = the nine non-Nike firms (adidas, HOKA, On, New Balance, Brooks, ASICS, Skechers, Under Armour, PUMA), simple average across firms. Full per-quarter files for every brand, both calendar and Nike fiscal quarters, are listed in Section F.

### C1. Amazon (2023 dataset), Nike Inc by Nike fiscal quarter, with the 9-competitor average

| quarter | Nike Inc products reviewed | reviews | stars | 1-2 star share | tone NB | tone VADER | AbnTone | Neg_AbnTone | AbnRating | AbnReviewCnt (100s) | peer reviews | peer avg stars | peer avg tone | peer avg AbnTone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1FY2019 | 6,233 | 13,386 | 4.318 | 0.119 | 0.685 | 0.220 | -0.018 | -0.018 | -0.013 | 31 | 79,801 | 4.311 | 0.689 | -0.022 |
| Q2FY2019 | 6,324 | 13,527 | 4.301 | 0.130 | 0.664 | 0.285 | -0.031 | -0.031 | -0.024 | 27 | 70,336 | 4.363 | 0.697 | -0.007 |
| Q3FY2019 | 6,760 | 15,782 | 4.407 | 0.106 | 0.692 | 0.328 | 0.009 | 0.000 | 0.093 | 38 | 77,920 | 4.432 | 0.712 | 0.013 |
| Q4FY2019 | 5,998 | 13,843 | 4.356 | 0.119 | 0.666 | 0.328 | -0.015 | -0.015 | 0.027 | 2.685 | 76,818 | 4.387 | 0.689 | -0.012 |
| Q1FY2020 | 6,947 | 19,190 | 4.392 | 0.110 | 0.678 | 0.322 | 0.001 | 0.000 | 0.047 | 51 | 103,659 | 4.401 | 0.696 | -0.001 |
| Q2FY2020 | 5,544 | 14,320 | 4.320 | 0.129 | 0.655 | 0.308 | -0.020 | -0.020 | -0.044 | -13 | 78,432 | 4.319 | 0.666 | -0.032 |
| Q3FY2020 | 7,449 | 23,249 | 4.388 | 0.110 | 0.682 | 0.320 | 0.009 | 0.000 | 0.019 | 75 | 146,334 | 4.417 | 0.701 | 0.010 |
| Q4FY2020 | 4,114 | 10,068 | 4.197 | 0.157 | 0.612 | 0.293 | -0.059 | -0.059 | -0.167 | -76 | 66,724 | 4.295 | 0.654 | -0.034 |
| Q1FY2021 | 3,633 | 9,936 | 4.157 | 0.168 | 0.592 | 0.285 | -0.064 | -0.064 | -0.168 | -68 | 93,467 | 4.260 | 0.624 | -0.055 |
| Q2FY2021 | 3,167 | 7,951 | 4.147 | 0.167 | 0.588 | 0.286 | -0.047 | -0.047 | -0.119 | -64 | 73,898 | 4.261 | 0.635 | -0.026 |
| Q3FY2021 | 3,345 | 9,051 | 4.136 | 0.172 | 0.583 | 0.273 | -0.036 | -0.036 | -0.086 | -38 | 78,504 | 4.294 | 0.657 | 0.003 |
| Q4FY2021 | 3,950 | 11,378 | 4.070 | 0.187 | 0.565 | 0.265 | -0.029 | -0.029 | -0.089 | 21 | 111,586 | 4.231 | 0.632 | -0.010 |
| Q1FY2022 | 2,954 | 8,203 | 4.003 | 0.206 | 0.535 | 0.266 | -0.047 | -0.047 | -0.124 | -14 | 99,959 | 4.197 | 0.614 | -0.023 |
| Q2FY2022 | 2,202 | 5,533 | 3.900 | 0.232 | 0.474 | 0.244 | -0.093 | -0.093 | -0.189 | -36 | 67,905 | 4.127 | 0.574 | -0.061 |
| Q3FY2022 | 2,210 | 5,950 | 3.974 | 0.212 | 0.510 | 0.260 | -0.029 | -0.029 | -0.053 | -26 | 66,028 | 4.163 | 0.593 | -0.026 |
| Q4FY2022 | 2,030 | 6,037 | 3.961 | 0.217 | 0.518 | 0.258 | -0.003 | -0.003 | -0.025 | -17 | 72,276 | 4.117 | 0.565 | -0.038 |
| Q1FY2023 | 2,099 | 7,534 | 3.995 | 0.208 | 0.532 | 0.264 | 0.023 | 0.000 | 0.036 | 11 | 84,558 | 4.151 | 0.593 | 0.007 |
| Q2FY2023 | 2,019 | 7,203 | 3.973 | 0.219 | 0.516 | 0.252 | 0.007 | 0.000 | 0.015 | 9.395 | 73,413 | 4.148 | 0.582 | 0.001 |
| Q3FY2023 | 2,199 | 8,468 | 4.068 | 0.192 | 0.559 | 0.263 | 0.040 | 0.000 | 0.093 | 18 | 70,656 | 4.234 | 0.612 | 0.028 |
| Q4FY2023 | 1,774 | 6,280 | 3.912 | 0.233 | 0.518 | 0.223 | -0.013 | -0.013 | -0.087 | -10 | 51,441 | 4.103 | 0.573 | -0.016 |
| Q1FY2024 | 964 | 2,540 | 3.994 | 0.210 | 0.558 | 0.194 | 0.026 | 0.000 | 0.007 | -48 | 16,120 | 4.105 | 0.601 | 0.011 |

### C2a. Amazon AbnormalTone by firm and Nike fiscal quarter

| quarter | ASICS | Brooks | HOKA | New Balance | Nike Inc | On | PUMA | Skechers | Under Armour | adidas |
|---|---|---|---|---|---|---|---|---|---|---|
| Q1FY2020 | 0.012 | 0.023 | -0.045 | 0.012 | 0.001 | 0.000 | -0.009 | -0.009 | 0.006 | 0.002 |
| Q2FY2020 | -0.018 | -0.005 | -0.059 | -0.024 | -0.020 | -0.086 | -0.027 | -0.030 | -0.013 | -0.028 |
| Q3FY2020 | 0.029 | 0.048 | -0.008 | 0.024 | 0.009 | -0.060 | -0.009 | 0.029 | 0.021 | 0.016 |
| Q4FY2020 | -0.038 | -0.053 | -0.068 | -0.031 | -0.059 | 0.102 | -0.054 | -0.042 | -0.059 | -0.061 |
| Q1FY2021 | -0.024 | -0.058 | -0.026 | -0.006 | -0.064 | -0.208 | -0.045 | -0.012 | -0.061 | -0.057 |
| Q2FY2021 | -0.035 | -0.053 | -0.031 | -0.049 | -0.047 | 0.077 | -0.031 | -0.015 | -0.056 | -0.039 |
| Q3FY2021 | -0.009 | -0.002 | 0.051 | -0.011 | -0.036 | 0.048 | 0.001 | 0.005 | -0.025 | -0.027 |
| Q4FY2021 | 0.003 | -0.008 | 0.029 | -0.025 | -0.029 | -0.064 | -0.012 | 0.010 | -0.004 | -0.022 |
| Q1FY2022 | -0.010 | -0.024 | -0.041 | -0.043 | -0.047 | 0.006 | -0.033 | -0.012 | -0.010 | -0.040 |
| Q2FY2022 | -0.062 | -0.063 | -0.062 | -0.083 | -0.093 | -0.061 | -0.065 | -0.051 | -0.048 | -0.051 |
| Q3FY2022 | -0.027 | -0.023 | -0.055 | -0.025 | -0.029 | -0.015 | -0.022 | -0.019 | -0.035 | -0.014 |
| Q4FY2022 | -0.070 | -0.022 | 0.009 | -0.038 | -0.003 | -0.101 | -0.023 | -0.037 | -0.036 | -0.025 |
| Q1FY2023 | -0.004 | 0.005 | 0.053 | 0.004 | 0.023 | -0.008 | -0.008 | -0.008 | 0.013 | 0.013 |
| Q2FY2023 | -0.019 | 0.005 | -0.009 | 0.000 | 0.007 | 0.019 | 0.008 | -0.004 | 0.001 | 0.007 |
| Q3FY2023 | 0.021 | 0.054 | -0.009 | 0.040 | 0.040 | -0.012 | 0.046 | 0.035 | 0.042 | 0.037 |
| Q4FY2023 | 0.009 | 0.004 | -0.049 | -0.015 | -0.013 | -0.075 | 0.004 | -0.010 | 0.006 | -0.015 |
| Q1FY2024 | -0.004 | 0.028 | -0.038 | 0.039 | 0.026 | -0.053 | 0.037 | 0.004 | 0.049 | 0.036 |

### C2b. Amazon average stars by firm and Nike fiscal quarter

| quarter | ASICS | Brooks | HOKA | New Balance | Nike Inc | On | PUMA | Skechers | Under Armour | adidas |
|---|---|---|---|---|---|---|---|---|---|---|
| Q1FY2020 | 4.412 | 4.496 | 4.398 | 4.314 | 4.392 | 4.283 | 4.441 | 4.385 | 4.444 | 4.439 |
| Q2FY2020 | 4.341 | 4.481 | 4.338 | 4.238 | 4.320 | 3.987 | 4.401 | 4.334 | 4.395 | 4.360 |
| Q3FY2020 | 4.425 | 4.587 | 4.362 | 4.338 | 4.388 | 4.243 | 4.440 | 4.446 | 4.460 | 4.448 |
| Q4FY2020 | 4.268 | 4.375 | 4.261 | 4.216 | 4.197 | 4.435 | 4.281 | 4.274 | 4.278 | 4.271 |
| Q1FY2021 | 4.312 | 4.365 | 4.326 | 4.264 | 4.157 | 4.000 | 4.254 | 4.346 | 4.241 | 4.234 |
| Q2FY2021 | 4.303 | 4.318 | 4.235 | 4.173 | 4.147 | 4.298 | 4.290 | 4.321 | 4.198 | 4.213 |
| Q3FY2021 | 4.317 | 4.408 | 4.399 | 4.222 | 4.136 | 4.130 | 4.339 | 4.378 | 4.228 | 4.230 |
| Q4FY2021 | 4.295 | 4.329 | 4.231 | 4.157 | 4.070 | 4.073 | 4.246 | 4.350 | 4.218 | 4.182 |
| Q1FY2022 | 4.285 | 4.284 | 4.102 | 4.115 | 4.003 | 4.243 | 4.144 | 4.318 | 4.171 | 4.110 |
| Q2FY2022 | 4.198 | 4.186 | 4.134 | 3.999 | 3.900 | 4.150 | 4.074 | 4.226 | 4.094 | 4.079 |
| Q3FY2022 | 4.226 | 4.273 | 4.091 | 4.054 | 3.974 | 4.101 | 4.166 | 4.290 | 4.144 | 4.119 |
| Q4FY2022 | 4.113 | 4.279 | 4.165 | 4.014 | 3.961 | 3.945 | 4.146 | 4.243 | 4.064 | 4.084 |
| Q1FY2023 | 4.184 | 4.299 | 4.090 | 4.066 | 3.995 | 4.004 | 4.134 | 4.270 | 4.166 | 4.146 |
| Q2FY2023 | 4.131 | 4.292 | 4.157 | 4.029 | 3.973 | 4.086 | 4.153 | 4.243 | 4.124 | 4.118 |
| Q3FY2023 | 4.247 | 4.390 | 4.202 | 4.147 | 4.068 | 4.051 | 4.274 | 4.360 | 4.216 | 4.216 |
| Q4FY2023 | 4.162 | 4.248 | 4.056 | 3.995 | 3.912 | 3.855 | 4.160 | 4.223 | 4.138 | 4.087 |
| Q1FY2024 | 4.111 | 4.245 | 3.905 | 4.107 | 3.994 | 3.807 | 4.170 | 4.197 | 4.255 | 4.149 |

### C2c. Amazon distinct products reviewed (listing proxy) by firm and Nike fiscal quarter

| quarter | ASICS | Brooks | HOKA | New Balance | Nike Inc | On | PUMA | Skechers | Under Armour | adidas |
|---|---|---|---|---|---|---|---|---|---|---|
| Q1FY2020 | 1,143 | 464 | 211 | 1,887 | 6,947 | 49 | 2,914 | 4,595 | 3,356 | 5,970 |
| Q2FY2020 | 1,022 | 317 | 227 | 1,508 | 5,544 | 30 | 2,448 | 3,978 | 2,845 | 4,931 |
| Q3FY2020 | 1,233 | 426 | 262 | 1,840 | 7,449 | 37 | 3,484 | 5,024 | 3,609 | 6,932 |
| Q4FY2020 | 763 | 312 | 128 | 1,249 | 4,114 | 20 | 2,182 | 3,072 | 2,305 | 4,168 |
| Q1FY2021 | 834 | 346 | 183 | 1,311 | 3,633 | 24 | 2,436 | 4,225 | 2,132 | 4,226 |
| Q2FY2021 | 798 | 307 | 174 | 1,232 | 3,167 | 23 | 2,159 | 3,684 | 1,998 | 3,983 |
| Q3FY2021 | 751 | 269 | 141 | 1,154 | 3,345 | 24 | 2,189 | 3,229 | 1,964 | 4,049 |
| Q4FY2021 | 853 | 282 | 151 | 1,271 | 3,950 | 23 | 2,416 | 4,074 | 1,873 | 4,455 |
| Q1FY2022 | 798 | 240 | 146 | 1,122 | 2,954 | 37 | 1,846 | 3,774 | 1,696 | 3,925 |
| Q2FY2022 | 642 | 203 | 78 | 899 | 2,202 | 24 | 1,399 | 3,238 | 1,460 | 3,204 |
| Q3FY2022 | 640 | 171 | 97 | 820 | 2,210 | 24 | 1,408 | 2,754 | 1,545 | 3,077 |
| Q4FY2022 | 615 | 182 | 84 | 784 | 2,030 | 36 | 1,369 | 2,484 | 1,486 | 3,104 |
| Q1FY2023 | 585 | 177 | 76 | 789 | 2,099 | 47 | 1,381 | 2,449 | 1,469 | 3,229 |
| Q2FY2023 | 492 | 180 | 83 | 784 | 2,019 | 39 | 1,309 | 2,200 | 1,362 | 3,066 |
| Q3FY2023 | 550 | 173 | 67 | 749 | 2,199 | 52 | 1,298 | 1,973 | 1,391 | 2,966 |
| Q4FY2023 | 511 | 157 | 66 | 691 | 1,774 | 52 | 1,136 | 1,781 | 1,131 | 2,465 |
| Q1FY2024 | 296 | 100 | 36 | 386 | 964 | 36 | 523 | 958 | 616 | 1,295 |

### C3. Amazon by calendar quarter: AbnormalTone for Nike Inc, adidas, HOKA, On, New Balance

| quarter | HOKA | New Balance | Nike Inc | On | adidas |
|---|---|---|---|---|---|
| 2019Q1 | 0.020 | -0.008 | 0.001 | -0.012 | 0.000 |
| 2019Q2 | 0.008 | -0.006 | -0.008 | 0.031 | -0.012 |
| 2019Q3 | -0.077 | -0.002 | -0.006 | -0.067 | -0.006 |
| 2019Q4 | -0.056 | -0.001 | -0.010 | -0.052 | -0.012 |
| 2020Q1 | -0.002 | 0.013 | 0.008 | -0.022 | 0.009 |
| 2020Q2 | -0.126 | -0.052 | -0.096 | -0.055 | -0.093 |
| 2020Q3 | 0.025 | -0.008 | -0.052 | -0.056 | -0.046 |
| 2020Q4 | -0.028 | -0.040 | -0.039 | 0.099 | -0.039 |
| 2021Q1 | 0.066 | -0.011 | -0.045 | -0.011 | -0.020 |
| 2021Q2 | 0.005 | -0.032 | -0.024 | -0.016 | -0.028 |
| 2021Q3 | -0.019 | -0.043 | -0.052 | -0.028 | -0.038 |
| 2021Q4 | -0.099 | -0.081 | -0.072 | -0.097 | -0.044 |
| 2022Q1 | -0.032 | -0.038 | -0.033 | -0.037 | -0.020 |
| 2022Q2 | 0.016 | -0.017 | 0.004 | -0.058 | -0.009 |
| 2022Q3 | 0.035 | 0.003 | 0.022 | 0.020 | 0.012 |
| 2022Q4 | 0.058 | 0.023 | 0.032 | -0.022 | 0.022 |
| 2023Q1 | -0.066 | 0.010 | 0.008 | -0.010 | 0.017 |
| 2023Q2 | -0.061 | 0.001 | -0.011 | -0.085 | -0.014 |
| 2023Q3 | -0.015 | 0.066 | 0.055 | -0.053 | 0.047 |

### C4. Share of Amazon reviews mentioning 'fake' themes, percent, by Nike fiscal year

| fy | ASICS | Brooks | HOKA | New Balance | Nike Inc | On | PUMA | Skechers | Under Armour | adidas |
|---|---|---|---|---|---|---|---|---|---|---|
| 2,017 | 0.120 | 0.090 | 0.130 | 0.190 | 0.640 | 0.000 | 0.290 | 0.090 | 0.320 | 0.320 |
| 2,018 | 0.120 | 0.210 | 0.060 | 0.250 | 0.750 | 0.000 | 0.280 | 0.140 | 0.280 | 0.550 |
| 2,019 | 0.280 | 0.140 | 0.210 | 0.290 | 0.970 | 0.510 | 0.450 | 0.180 | 0.380 | 0.750 |
| 2,020 | 0.390 | 0.240 | 0.220 | 0.420 | 1.000 | 0.000 | 0.410 | 0.210 | 0.420 | 0.930 |
| 2,021 | 0.530 | 0.270 | 0.330 | 0.400 | 1.550 | 0.270 | 0.460 | 0.200 | 0.570 | 1.270 |
| 2,022 | 0.430 | 0.260 | 0.200 | 0.490 | 1.670 | 0.470 | 0.620 | 0.250 | 0.660 | 1.270 |
| 2,023 | 0.250 | 0.230 | 0.350 | 0.410 | 1.910 | 1.460 | 0.320 | 0.210 | 0.490 | 0.820 |

### C4. Share of Amazon reviews mentioning 'quality' themes, percent, by Nike fiscal year

| fy | ASICS | Brooks | HOKA | New Balance | Nike Inc | On | PUMA | Skechers | Under Armour | adidas |
|---|---|---|---|---|---|---|---|---|---|---|
| 2,017 | 3.090 | 4.400 | 2.760 | 3.510 | 2.450 | 4.020 | 2.190 | 3.130 | 2.310 | 2.440 |
| 2,018 | 3.180 | 4.270 | 2.930 | 3.340 | 2.940 | 5.350 | 2.460 | 3.230 | 2.450 | 2.570 |
| 2,019 | 3.220 | 3.930 | 4.430 | 3.860 | 3.030 | 7.110 | 2.220 | 3.510 | 2.620 | 2.710 |
| 2,020 | 3.070 | 3.610 | 3.740 | 3.720 | 2.810 | 4.580 | 2.380 | 3.460 | 2.530 | 2.700 |
| 2,021 | 3.720 | 3.950 | 3.270 | 4.090 | 3.440 | 6.470 | 2.600 | 3.410 | 3.170 | 3.080 |
| 2,022 | 3.750 | 4.620 | 4.440 | 5.350 | 4.500 | 4.090 | 3.730 | 3.900 | 3.860 | 3.850 |
| 2,023 | 3.830 | 4.160 | 5.320 | 5.060 | 4.570 | 5.190 | 3.390 | 3.850 | 3.460 | 3.970 |

### C5. Nike (nike.com) [non-incentivized only]: reviews of currently listed shoe styles, by Nike fiscal quarter

| fis_q | review_cnt | products | avg_rating | share_1_2_star | share_incentivized | avg_tone_nb | avg_tone_vader | AbnormalTone | Negative_AbnormalTone | AbnormalRating |
|---|---|---|---|---|---|---|---|---|---|---|
| Q1FY2022 | 1,073 | 42 | 4.673 | 0.041 | 0.000 | 0.792 | 0.350 |  |  |  |
| Q2FY2022 | 567 | 48 | 4.474 | 0.090 | 0.000 | 0.743 | 0.331 |  |  |  |
| Q3FY2022 | 563 | 44 | 4.623 | 0.051 | 0.000 | 0.775 | 0.359 |  |  |  |
| Q4FY2022 | 552 | 42 | 4.611 | 0.062 | 0.000 | 0.735 | 0.277 |  |  |  |
| Q1FY2023 | 597 | 43 | 4.623 | 0.052 | 0.000 | 0.747 | 0.322 | -0.014 | -0.014 | 0.028 |
| Q2FY2023 | 746 | 52 | 4.598 | 0.063 | 0.000 | 0.755 | 0.316 | 0.005 | 0.000 | 0.015 |
| Q3FY2023 | 1,211 | 72 | 4.765 | 0.022 | 0.000 | 0.817 | 0.345 | 0.063 | 0.000 | 0.151 |
| Q4FY2023 | 1,264 | 77 | 4.744 | 0.034 | 0.000 | 0.811 | 0.356 | 0.048 | 0.000 | 0.095 |
| Q1FY2024 | 2,461 | 95 | 4.749 | 0.033 | 0.000 | 0.792 | 0.338 | 0.010 | 0.000 | 0.067 |
| Q2FY2024 | 3,378 | 103 | 4.795 | 0.023 | 0.000 | 0.800 | 0.342 | 0.007 | 0.000 | 0.082 |
| Q3FY2024 | 3,205 | 119 | 4.743 | 0.031 | 0.000 | 0.808 | 0.351 | 0.003 | 0.000 | -0.021 |
| Q4FY2024 | 3,314 | 139 | 4.671 | 0.047 | 0.000 | 0.795 | 0.352 | -0.008 | -0.008 | -0.086 |
| Q1FY2025 | 2,724 | 145 | 4.635 | 0.052 | 0.000 | 0.790 | 0.351 | -0.009 | -0.009 | -0.105 |
| Q2FY2025 | 2,417 | 163 | 4.551 | 0.068 | 0.000 | 0.752 | 0.341 | -0.046 | -0.046 | -0.160 |
| Q3FY2025 | 3,601 | 195 | 4.643 | 0.049 | 0.000 | 0.771 | 0.342 | -0.015 | -0.015 | -0.007 |
| Q4FY2025 | 3,376 | 228 | 4.580 | 0.066 | 0.000 | 0.757 | 0.332 | -0.020 | -0.020 | -0.045 |
| Q1FY2026 | 3,162 | 245 | 4.539 | 0.073 | 0.000 | 0.736 | 0.328 | -0.032 | -0.032 | -0.063 |
| Q2FY2026 | 2,963 | 290 | 4.494 | 0.086 | 0.000 | 0.718 | 0.319 | -0.036 | -0.036 | -0.084 |
| Q3FY2026 | 3,160 | 367 | 4.474 | 0.086 | 0.000 | 0.715 | 0.317 | -0.031 | -0.031 | -0.089 |
| Q4FY2026 | 4,097 | 484 | 4.492 | 0.087 | 0.000 | 0.716 | 0.311 | -0.016 | -0.016 | -0.030 |
| Q1FY2027 | 4,517 | 625 | 4.538 | 0.072 | 0.000 | 0.728 | 0.323 | 0.007 | 0.000 | 0.039 |

### C5. Nike (nike.com): reviews of currently listed shoe styles, by Nike fiscal quarter

| fis_q | review_cnt | products | avg_rating | share_1_2_star | share_incentivized | avg_tone_nb | avg_tone_vader | AbnormalTone | Negative_AbnormalTone | AbnormalRating |
|---|---|---|---|---|---|---|---|---|---|---|
| Q1FY2022 | 1,198 | 44 | 4.654 | 0.040 | 0.104 | 0.789 | 0.348 |  |  |  |
| Q2FY2022 | 658 | 50 | 4.500 | 0.079 | 0.138 | 0.758 | 0.336 |  |  |  |
| Q3FY2022 | 725 | 45 | 4.633 | 0.044 | 0.223 | 0.796 | 0.370 |  |  |  |
| Q4FY2022 | 738 | 43 | 4.623 | 0.057 | 0.252 | 0.763 | 0.300 |  |  |  |
| Q1FY2023 | 792 | 46 | 4.648 | 0.045 | 0.246 | 0.778 | 0.330 | 0.002 | 0.000 | 0.045 |
| Q2FY2023 | 935 | 54 | 4.609 | 0.053 | 0.202 | 0.773 | 0.321 | -0.001 | -0.001 | 0.007 |
| Q3FY2023 | 1,297 | 74 | 4.776 | 0.021 | 0.066 | 0.823 | 0.349 | 0.045 | 0.000 | 0.147 |
| Q4FY2023 | 1,441 | 79 | 4.752 | 0.030 | 0.123 | 0.816 | 0.362 | 0.032 | 0.000 | 0.088 |
| Q1FY2024 | 2,757 | 96 | 4.753 | 0.030 | 0.107 | 0.798 | 0.343 | 0.001 | 0.000 | 0.057 |
| Q2FY2024 | 3,960 | 114 | 4.800 | 0.020 | 0.147 | 0.810 | 0.352 | 0.008 | 0.000 | 0.077 |
| Q3FY2024 | 3,750 | 127 | 4.754 | 0.028 | 0.145 | 0.821 | 0.365 | 0.009 | 0.000 | -0.016 |
| Q4FY2024 | 3,950 | 152 | 4.686 | 0.042 | 0.161 | 0.812 | 0.364 | 0.000 | 0.000 | -0.079 |
| Q1FY2025 | 3,438 | 156 | 4.652 | 0.044 | 0.208 | 0.808 | 0.360 | -0.003 | -0.003 | -0.096 |
| Q2FY2025 | 3,027 | 175 | 4.599 | 0.056 | 0.202 | 0.785 | 0.361 | -0.028 | -0.028 | -0.124 |
| Q3FY2025 | 4,443 | 200 | 4.662 | 0.043 | 0.190 | 0.791 | 0.356 | -0.016 | -0.016 | -0.011 |
| Q4FY2025 | 3,978 | 240 | 4.609 | 0.059 | 0.151 | 0.778 | 0.348 | -0.021 | -0.021 | -0.040 |
| Q1FY2026 | 6,009 | 288 | 4.636 | 0.045 | 0.474 | 0.806 | 0.383 | 0.016 | 0.000 | 0.005 |
| Q2FY2026 | 5,292 | 324 | 4.590 | 0.055 | 0.440 | 0.782 | 0.362 | -0.008 | -0.008 | -0.037 |
| Q3FY2026 | 5,466 | 413 | 4.596 | 0.057 | 0.422 | 0.784 | 0.368 | -0.005 | -0.005 | -0.028 |
| Q4FY2026 | 7,204 | 510 | 4.611 | 0.055 | 0.431 | 0.791 | 0.365 | 0.003 | 0.000 | 0.003 |
| Q1FY2027 | 7,512 | 656 | 4.619 | 0.047 | 0.399 | 0.789 | 0.357 | -0.002 | -0.002 | 0.011 |

### C6. Foot Locker (Bazaarvoice) reviews, average stars, by brand and Nike fiscal quarter

| fis_q | FL: ASICS | FL: Brooks | FL: Converse | FL: HOKA | FL: Jordan | FL: New Balance | FL: Nike | FL: Nike Inc (Nike+Jordan+Converse) | FL: On | FL: PUMA | FL: Skechers | FL: Under Armour | FL: adidas |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1FY2022 | 5.000 | 4.235 | 4.635 | 4.000 | 4.634 | 4.661 | 4.536 | 4.593 |  | 4.774 |  | 4.459 | 4.786 |
| Q2FY2022 | 4.615 | 4.550 | 4.702 | 4.467 | 4.626 | 4.680 | 4.361 | 4.559 | 4.500 | 4.535 |  | 3.867 | 4.596 |
| Q3FY2022 | 4.867 | 4.608 | 4.804 | 4.618 | 4.598 | 4.667 | 4.433 | 4.644 | 5.000 | 4.475 |  | 2.357 | 4.512 |
| Q4FY2022 | 4.800 | 4.405 | 4.733 | 4.610 | 4.596 | 4.496 | 4.452 | 4.638 | 5.000 | 4.506 |  | 5.000 | 4.711 |
| Q1FY2023 | 5.000 | 4.309 | 4.708 | 4.614 | 4.563 | 4.443 | 4.451 | 4.606 | 4.583 | 4.216 |  | 4.000 | 4.645 |
| Q2FY2023 | 4.000 | 4.562 | 4.640 | 4.610 | 4.352 | 4.446 | 4.261 | 4.493 | 4.333 | 4.611 |  |  | 4.733 |
| Q3FY2023 |  | 4.542 | 4.625 | 4.670 | 4.400 | 4.564 | 4.292 | 4.513 | 5.000 | 4.368 |  |  | 4.773 |
| Q4FY2023 | 5.000 | 4.439 | 4.531 | 4.688 | 4.641 | 4.551 | 4.461 | 4.518 | 4.636 | 4.652 |  | 4.875 | 4.702 |
| Q1FY2024 | 5.000 | 4.511 | 4.511 | 4.610 | 4.649 | 4.632 | 4.567 | 4.560 | 4.267 | 3.909 |  |  | 4.680 |
| Q2FY2024 | 4.000 | 4.275 | 4.550 | 4.596 | 4.685 | 4.797 | 4.548 | 4.595 | 4.467 | 4.400 |  |  | 4.768 |
| Q3FY2024 | 3.333 | 4.279 | 4.483 | 4.662 | 4.606 | 4.611 | 4.628 | 4.573 | 4.556 | 4.462 |  | 3.000 | 4.528 |
| Q4FY2024 | 3.667 | 4.219 | 4.410 | 4.617 | 4.542 | 4.667 | 4.618 | 4.499 | 4.308 | 3.474 |  | 4.691 | 4.705 |
| Q1FY2025 | 4.583 | 4.438 | 4.419 | 4.611 | 4.378 | 4.648 | 4.567 | 4.465 | 4.077 | 3.882 |  | 4.667 | 4.682 |
| Q2FY2025 | 4.095 | 4.493 | 4.506 | 4.574 | 4.500 | 4.728 | 4.518 | 4.508 | 4.632 | 4.667 | 5.000 | 4.800 | 4.715 |
| Q3FY2025 | 4.654 | 4.500 | 4.519 | 4.691 | 4.660 | 4.686 | 4.611 | 4.606 | 4.247 | 4.423 |  | 4.773 | 4.579 |
| Q4FY2025 | 4.538 | 4.833 | 4.516 | 4.592 | 4.672 | 4.616 | 4.535 | 4.562 | 4.296 | 4.886 | 5.000 | 4.628 | 4.731 |
| Q1FY2026 | 4.824 | 4.000 | 4.483 | 4.685 | 4.683 | 4.702 | 4.717 | 4.646 | 4.619 | 4.750 |  | 4.812 | 4.827 |
| Q2FY2026 | 4.852 |  | 4.570 | 4.726 | 4.673 | 4.619 | 4.642 | 4.637 | 4.714 | 5.000 | 5.000 | 4.480 | 4.693 |
| Q3FY2026 | 4.750 | 4.333 | 4.626 | 4.782 | 4.837 | 4.640 | 4.635 | 4.673 | 4.838 | 5.000 | 5.000 | 4.829 | 4.765 |
| Q4FY2026 | 4.875 | 4.750 | 4.543 | 4.725 | 4.744 | 4.531 | 4.651 | 4.662 | 4.800 | 3.000 | 5.000 | 4.167 | 4.682 |
| Q1FY2027 | 4.583 | 5.000 | 4.202 | 4.763 | 4.699 | 4.535 | 4.560 | 4.567 | 4.250 | 5.000 | 5.000 | 3.500 | 4.829 |

### C6. Foot Locker (Bazaarvoice) reviews, tone NB, by brand and Nike fiscal quarter

| fis_q | FL: ASICS | FL: Brooks | FL: Converse | FL: HOKA | FL: Jordan | FL: New Balance | FL: Nike | FL: Nike Inc (Nike+Jordan+Converse) | FL: On | FL: PUMA | FL: Skechers | FL: Under Armour | FL: adidas |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1FY2022 | 0.923 | 0.663 | 0.793 | 0.895 | 0.803 | 0.851 | 0.794 | 0.795 |  | 0.875 |  | 0.797 | 0.831 |
| Q2FY2022 | 0.918 | 0.811 | 0.800 | 0.827 | 0.741 | 0.847 | 0.764 | 0.772 | 0.645 | 0.827 |  | 0.498 | 0.772 |
| Q3FY2022 | 0.960 | 0.828 | 0.833 | 0.953 | 0.757 | 0.862 | 0.790 | 0.810 | 0.970 | 0.813 |  | -0.215 | 0.776 |
| Q4FY2022 | 0.986 | 0.729 | 0.802 | 0.872 | 0.768 | 0.828 | 0.782 | 0.793 | 0.813 | 0.801 |  | 0.936 | 0.752 |
| Q1FY2023 | 0.970 | 0.633 | 0.809 | 0.860 | 0.763 | 0.693 | 0.779 | 0.794 | 0.841 | 0.677 |  | 0.510 | 0.751 |
| Q2FY2023 | 0.381 | 0.782 | 0.776 | 0.852 | 0.703 | 0.750 | 0.651 | 0.731 | 0.791 | 0.892 |  |  | 0.833 |
| Q3FY2023 |  | 0.778 | 0.775 | 0.849 | 0.750 | 0.796 | 0.751 | 0.767 | 0.972 | 0.730 |  |  | 0.823 |
| Q4FY2023 | 0.997 | 0.734 | 0.702 | 0.863 | 0.781 | 0.794 | 0.797 | 0.735 | 0.988 | 0.860 |  | 0.820 | 0.794 |
| Q1FY2024 | 0.985 | 0.724 | 0.762 | 0.844 | 0.717 | 0.919 | 0.786 | 0.758 | 0.734 | 0.262 |  |  | 0.803 |
| Q2FY2024 | 0.351 | 0.645 | 0.726 | 0.835 | 0.738 | 0.917 | 0.779 | 0.743 | 0.719 | 0.933 |  |  | 0.799 |
| Q3FY2024 | -0.013 | 0.619 | 0.727 | 0.824 | 0.718 | 0.795 | 0.818 | 0.762 | 0.841 | 0.765 |  | -0.495 | 0.781 |
| Q4FY2024 | 0.813 | 0.647 | 0.681 | 0.818 | 0.679 | 0.800 | 0.832 | 0.731 | 0.769 | 0.417 |  | 0.846 | 0.812 |
| Q1FY2025 | 0.845 | 0.723 | 0.679 | 0.823 | 0.694 | 0.826 | 0.824 | 0.735 | 0.679 | 0.656 |  | 0.835 | 0.810 |
| Q2FY2025 | 0.814 | 0.692 | 0.712 | 0.798 | 0.747 | 0.842 | 0.786 | 0.743 | 0.806 | 0.818 | 1.000 | 0.869 | 0.827 |
| Q3FY2025 | 0.847 | 0.710 | 0.721 | 0.874 | 0.772 | 0.818 | 0.817 | 0.777 | 0.744 | 0.790 |  | 0.886 | 0.807 |
| Q4FY2025 | 0.888 | 0.995 | 0.699 | 0.803 | 0.761 | 0.810 | 0.787 | 0.743 | 0.678 | 0.822 | 0.997 | 0.898 | 0.845 |
| Q1FY2026 | 0.970 | 0.883 | 0.649 | 0.830 | 0.715 | 0.844 | 0.860 | 0.778 | 0.852 | 0.934 |  | 0.861 | 0.853 |
| Q2FY2026 | 0.920 |  | 0.697 | 0.860 | 0.751 | 0.835 | 0.831 | 0.787 | 0.918 | 0.968 | 0.977 | 0.847 | 0.813 |
| Q3FY2026 | 0.906 | 0.519 | 0.781 | 0.873 | 0.827 | 0.832 | 0.843 | 0.834 | 0.905 | 0.963 | 0.977 | 0.864 | 0.833 |
| Q4FY2026 | 0.884 | 0.967 | 0.707 | 0.871 | 0.813 | 0.785 | 0.841 | 0.818 | 0.935 | -0.550 | 0.529 | 0.677 | 0.816 |
| Q1FY2027 | 0.842 |  | 0.652 | 0.876 | 0.763 | 0.779 | 0.800 | 0.773 | 0.816 | 0.883 | 0.797 | 0.798 | 0.854 |

### C6. Foot Locker (Bazaarvoice) reviews, AbnormalTone, by brand and Nike fiscal quarter

| fis_q | FL: ASICS | FL: Brooks | FL: Converse | FL: HOKA | FL: Jordan | FL: New Balance | FL: Nike | FL: Nike Inc (Nike+Jordan+Converse) | FL: On | FL: PUMA | FL: Skechers | FL: Under Armour | FL: adidas |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1FY2022 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Q2FY2022 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Q3FY2022 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Q4FY2022 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Q1FY2023 | 0.023 | -0.125 | 0.003 | -0.027 | -0.004 | -0.154 | -0.004 | 0.001 |  | -0.152 |  | 0.006 | -0.032 |
| Q2FY2023 | -0.578 | 0.032 | -0.035 | -0.026 | -0.054 | -0.058 | -0.128 | -0.061 | -0.026 | 0.112 |  |  | 0.070 |
| Q3FY2023 |  | 0.035 | -0.030 | -0.035 | 0.003 | 0.013 | 0.001 | -0.015 | 0.118 | -0.066 |  |  | 0.045 |
| Q4FY2023 |  | 0.003 | -0.088 | 0.004 | 0.035 | 0.027 | 0.056 | -0.036 | 0.133 | 0.085 |  |  | 0.004 |
| Q1FY2024 |  | -0.008 | -0.004 | -0.012 | -0.032 | 0.161 | 0.042 | 0.002 | -0.164 | -0.527 |  |  | 0.003 |
| Q2FY2024 |  | -0.110 | -0.028 | -0.017 | -0.000 | 0.102 | 0.033 | -0.004 | -0.152 | 0.247 |  |  | -0.015 |
| Q3FY2024 |  | -0.101 | -0.015 | -0.023 | -0.029 | -0.062 | 0.039 | 0.011 | -0.012 | 0.069 |  |  | -0.024 |
| Q4FY2024 | 0.233 | -0.033 | -0.048 | -0.024 | -0.059 | -0.056 | 0.036 | -0.019 | -0.051 | -0.288 |  |  | 0.018 |
| Q1FY2025 | 0.311 | 0.065 | -0.045 | -0.008 | -0.019 | -0.032 | 0.020 | -0.014 | -0.086 | 0.062 |  |  | 0.012 |
| Q2FY2025 | 0.315 | 0.033 | 0.008 | -0.026 | 0.039 | 0.008 | -0.027 | 0.000 | 0.054 | 0.125 |  |  | 0.026 |
| Q3FY2025 | 0.232 | 0.040 | 0.022 | 0.058 | 0.063 | 0.002 | 0.003 | 0.034 | -0.030 | 0.126 |  | 0.372 | -0.000 |
| Q4FY2025 | 0.058 | 0.302 | 0.001 | -0.025 | 0.038 | -0.011 | -0.027 | -0.003 | -0.072 | 0.152 |  | 0.039 | 0.031 |
| Q1FY2026 | 0.121 | 0.103 | -0.054 | 0.005 | -0.029 | 0.020 | 0.056 | 0.029 | 0.125 | 0.163 |  | -0.011 | 0.031 |
| Q2FY2026 | 0.041 |  | 0.001 | 0.034 | 0.002 | 0.006 | 0.019 | 0.027 | 0.148 | 0.127 |  | -0.032 | -0.020 |
| Q3FY2026 | -0.000 |  | 0.089 | 0.031 | 0.077 | 0.006 | 0.019 | 0.063 | 0.108 | 0.085 |  | -0.009 | 0.004 |
| Q4FY2026 | -0.037 |  | 0.000 | 0.029 | 0.050 | -0.045 | 0.011 | 0.033 | 0.096 | -1.472 |  | -0.191 | -0.020 |
| Q1FY2027 | -0.078 |  | -0.056 | 0.018 | -0.013 | -0.045 | -0.044 | -0.031 | -0.086 | 0.304 |  | -0.014 | 0.026 |

### C6. Foot Locker (Bazaarvoice) reviews, 1-2 star share, by brand and Nike fiscal quarter

| fis_q | FL: ASICS | FL: Brooks | FL: Converse | FL: HOKA | FL: Jordan | FL: New Balance | FL: Nike | FL: Nike Inc (Nike+Jordan+Converse) | FL: On | FL: PUMA | FL: Skechers | FL: Under Armour | FL: adidas |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1FY2022 | 0.000 | 0.123 | 0.046 | 0.250 | 0.065 | 0.048 | 0.076 | 0.061 |  | 0.024 |  | 0.115 | 0.043 |
| Q2FY2022 | 0.077 | 0.075 | 0.059 | 0.067 | 0.067 | 0.040 | 0.111 | 0.080 | 0.000 | 0.069 |  | 0.233 | 0.073 |
| Q3FY2022 | 0.000 | 0.013 | 0.018 | 0.059 | 0.075 | 0.052 | 0.092 | 0.051 | 0.000 | 0.113 |  | 0.643 | 0.083 |
| Q4FY2022 | 0.000 | 0.072 | 0.044 | 0.037 | 0.055 | 0.097 | 0.096 | 0.060 | 0.000 | 0.076 |  | 0.000 | 0.039 |
| Q1FY2023 | 0.000 | 0.095 | 0.023 | 0.059 | 0.068 | 0.129 | 0.103 | 0.055 | 0.083 | 0.137 |  | 0.000 | 0.060 |
| Q2FY2023 | 0.000 | 0.040 | 0.057 | 0.076 | 0.130 | 0.098 | 0.102 | 0.078 | 0.167 | 0.056 |  |  | 0.037 |
| Q3FY2023 |  | 0.061 | 0.041 | 0.023 | 0.067 | 0.081 | 0.124 | 0.067 | 0.000 | 0.053 |  |  | 0.024 |
| Q4FY2023 | 0.000 | 0.084 | 0.054 | 0.035 | 0.062 | 0.102 | 0.078 | 0.062 | 0.091 | 0.043 |  | 0.000 | 0.033 |
| Q1FY2024 | 0.000 | 0.062 | 0.073 | 0.058 | 0.072 | 0.105 | 0.068 | 0.072 | 0.200 | 0.273 |  |  | 0.048 |
| Q2FY2024 | 0.000 | 0.110 | 0.070 | 0.074 | 0.050 | 0.017 | 0.078 | 0.066 | 0.133 | 0.100 |  |  | 0.019 |
| Q3FY2024 | 0.333 | 0.092 | 0.071 | 0.050 | 0.069 | 0.066 | 0.059 | 0.065 | 0.074 | 0.077 |  | 0.000 | 0.077 |
| Q4FY2024 | 0.333 | 0.136 | 0.096 | 0.054 | 0.078 | 0.065 | 0.058 | 0.080 | 0.154 | 0.368 |  | 0.036 | 0.044 |
| Q1FY2025 | 0.083 | 0.079 | 0.086 | 0.069 | 0.127 | 0.068 | 0.077 | 0.091 | 0.192 | 0.235 |  | 0.020 | 0.044 |
| Q2FY2025 | 0.191 | 0.072 | 0.073 | 0.069 | 0.103 | 0.050 | 0.090 | 0.086 | 0.079 | 0.074 | 0.000 | 0.017 | 0.045 |
| Q3FY2025 | 0.077 | 0.069 | 0.082 | 0.052 | 0.065 | 0.062 | 0.073 | 0.072 | 0.168 | 0.115 |  | 0.027 | 0.060 |
| Q4FY2025 | 0.115 | 0.000 | 0.076 | 0.076 | 0.045 | 0.069 | 0.089 | 0.073 | 0.111 | 0.000 | 0.000 | 0.000 | 0.043 |
| Q1FY2026 | 0.000 | 0.000 | 0.086 | 0.050 | 0.046 | 0.045 | 0.033 | 0.050 | 0.095 | 0.000 |  | 0.000 | 0.023 |
| Q2FY2026 | 0.000 |  | 0.064 | 0.031 | 0.059 | 0.063 | 0.045 | 0.052 | 0.057 | 0.000 | 0.000 | 0.040 | 0.055 |
| Q3FY2026 | 0.021 | 0.000 | 0.065 | 0.026 | 0.024 | 0.059 | 0.055 | 0.050 | 0.027 | 0.000 | 0.000 | 0.000 | 0.032 |
| Q4FY2026 | 0.025 | 0.000 | 0.087 | 0.033 | 0.033 | 0.082 | 0.042 | 0.045 | 0.040 | 0.000 | 0.000 | 0.167 | 0.039 |
| Q1FY2027 | 0.083 | 0.000 | 0.164 | 0.029 | 0.047 | 0.085 | 0.066 | 0.070 | 0.083 | 0.000 | 0.000 | 0.500 | 0.017 |

### C6b. Foot Locker review counts by brand and quarter (top 25 products per brand, capped at 1,000 newest reviews per product)

| fis_q | FL: ASICS | FL: Brooks | FL: Converse | FL: HOKA | FL: Jordan | FL: New Balance | FL: Nike | FL: Nike Inc (Nike+Jordan+Converse) | FL: On | FL: PUMA | FL: Skechers | FL: Under Armour | FL: adidas |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1FY2022 | 9.000 | 162 | 282 | 4.000 | 93 | 62 | 276 | 651 |  | 84 |  | 61 | 187 |
| Q2FY2022 | 13 | 40 | 336 | 15 | 254 | 75 | 332 | 922 | 4.000 | 101 |  | 30 | 109 |
| Q3FY2022 | 15 | 74 | 506 | 34 | 107 | 96 | 360 | 973 | 6.000 | 80 |  | 14 | 84 |
| Q4FY2022 | 5.000 | 111 | 617 | 82 | 109 | 113 | 292 | 1,018 | 4.000 | 79 |  | 1.000 | 128 |
| Q1FY2023 | 2.000 | 84 | 431 | 101 | 103 | 70 | 253 | 787 | 12 | 51 |  | 1.000 | 200 |
| Q2FY2023 | 2.000 | 176 | 300 | 118 | 54 | 112 | 157 | 511 | 6.000 | 18 |  |  | 296 |
| Q3FY2023 |  | 456 | 363 | 173 | 45 | 124 | 161 | 569 | 4.000 | 19 |  |  | 459 |
| Q4FY2023 | 1.000 | 910 | 550 | 202 | 64 | 49 | 256 | 870 | 11 | 23 |  | 8.000 | 215 |
| Q1FY2024 | 1.000 | 1,059 | 683 | 241 | 345 | 19 | 351 | 1,379 | 15 | 11 |  |  | 231 |
| Q2FY2024 | 2.000 | 812 | 653 | 230 | 537 | 59 | 412 | 1,602 | 15 | 10 |  |  | 211 |
| Q3FY2024 | 3.000 | 1,040 | 509 | 299 | 348 | 288 | 613 | 1,470 | 27 | 13 |  | 1.000 | 714 |
| Q4FY2024 | 3.000 | 926 | 669 | 313 | 179 | 414 | 435 | 1,283 | 13 | 19 |  | 55 | 522 |
| Q1FY2025 | 24 | 404 | 768 | 350 | 362 | 514 | 658 | 1,788 | 26 | 17 |  | 51 | 595 |
| Q2FY2025 | 21 | 223 | 803 | 303 | 398 | 478 | 575 | 1,776 | 38 | 27 | 1.000 | 60 | 596 |
| Q3FY2025 | 52 | 216 | 632 | 346 | 913 | 1,052 | 1,014 | 2,559 | 101 | 78 |  | 220 | 316 |
| Q4FY2025 | 26 | 6.000 | 549 | 277 | 335 | 1,066 | 439 | 1,323 | 27 | 44 | 1.000 | 51 | 353 |
| Q1FY2026 | 34 | 2.000 | 476 | 717 | 262 | 1,237 | 965 | 1,703 | 21 | 8.000 |  | 48 | 133 |
| Q2FY2026 | 27 |  | 328 | 776 | 474 | 1,439 | 1,057 | 1,859 | 35 | 4.000 | 1.000 | 25 | 218 |
| Q3FY2026 | 48 | 3.000 | 155 | 977 | 337 | 2,607 | 1,289 | 1,781 | 37 | 2.000 | 4.000 | 35 | 187 |
| Q4FY2026 | 40 | 4.000 | 127 | 1,147 | 270 | 2,710 | 720 | 1,117 | 25 | 1.000 | 3.000 | 6.000 | 619 |
| Q1FY2027 | 36 | 1.000 | 104 | 1,344 | 319 | 1,658 | 609 | 1,032 | 12 | 1.000 | 3.000 | 2.000 | 1,452 |

### C7. Foot Locker mens shoes: listing counts by brand (brand filter counts) and Nike Inc share of focus-brand listings

| snapshot_date | ASICS | Brooks | Converse | HOKA | Jordan | New Balance | Nike | On | PUMA | Saucony | Under Armour | adidas | nike_inc_share_pct |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2021-01-01 | 25 | 14 | 104 |  | 138 | 107 | 686 |  | 123 | 1.000 | 28 | 163 | 67 |
| 2021-04-10 | 31 | 17 | 107 |  | 124 | 110 | 527 |  | 140 |  | 37 | 148 | 61 |
| 2021-07-01 | 45 | 19 | 102 |  | 100 | 132 | 466 |  | 154 |  | 30 | 133 | 57 |
| 2021-10-05 | 46 | 24 | 77 |  | 78 | 110 | 381 | 12 | 140 |  | 16 | 112 | 54 |
| 2022-01-04 | 40 | 25 | 66 |  | 48 | 127 | 263 | 12 | 142 | 1.000 | 13 | 109 | 45 |
| 2022-04-01 | 38 | 41 | 69 |  | 72 | 171 | 324 | 19 | 171 |  | 24 | 158 | 43 |
| 2022-07-15 | 48 | 51 | 75 | 8.000 | 99 | 208 | 405 | 46 | 198 |  | 32 | 256 | 41 |
| 2022-10-03 | 71 | 99 | 80 | 95 | 116 | 243 | 519 | 44 | 206 | 55 | 67 | 423 | 35 |
| 2023-01-03 | 56 | 59 | 82 | 90 | 136 | 210 | 445 | 54 | 191 | 12 | 82 | 482 | 35 |
| 2023-04-07 | 66 | 94 | 86 | 46 | 195 | 263 | 492 | 73 | 199 | 9.000 | 123 | 473 | 36 |
| 2023-07-14 | 87 | 131 | 89 | 81 | 218 | 229 | 547 | 84 | 216 | 38 | 163 | 582 | 35 |
| 2023-10-02 | 90 | 135 | 92 | 89 | 250 | 229 | 567 | 102 | 235 | 35 | 160 | 441 | 37 |
| 2024-01-01 | 92 | 107 | 87 | 81 | 266 | 216 | 644 | 97 | 214 | 33 | 163 | 379 | 42 |
| 2024-04-02 | 63 | 94 | 68 | 70 | 255 | 161 | 628 | 100 | 169 | 26 | 203 | 412 | 42 |
| 2024-07-06 | 52 | 93 | 66 | 94 | 289 | 174 | 654 | 96 | 176 | 22 | 176 | 364 | 45 |
| 2024-10-01 | 46 | 79 | 69 | 113 | 277 | 147 | 746 | 110 | 176 | 19 | 292 | 349 | 45 |
| 2025-02-01 | 40 | 53 | 71 | 110 | 224 | 156 | 897 | 102 | 190 | 62 | 278 | 293 | 48 |
| 2025-04-07 | 39 | 51 | 66 | 108 | 191 | 146 | 862 | 89 | 173 | 73 | 255 | 343 | 47 |
| 2025-08-26 | 58 | 58 | 53 | 91 | 180 | 136 | 840 | 86 | 169 | 110 | 130 | 555 | 44 |
| 2025-12-11 | 34 | 24 | 20 | 92 | 118 | 89 | 647 | 56 | 96 | 97 | 46 | 303 | 48 |
| 2026-01-09 | 37 | 21 | 23 | 94 | 124 | 76 | 657 | 55 | 46 | 98 | 36 | 268 | 52 |
| 2026-04-19 | 43 | 68 | 31 | 99 | 146 | 96 | 683 | 60 | 48 | 108 | 36 | 381 | 48 |
| 2026-07-14 | 49 | 66 | 28 | 95 | 158 | 102 | 709 | 65 | 51 | 71 | 30 | 419 | 49 |
| 2026-10-03 | 50 | 63 | 39 | 85 | 168 | 130 | 729 | 58 | 60 | 142 | 32 | 382 | 48 |
| 2026-10-13 | 46 | 62 | 31 | 80 | 176 | 127 | 727 | 60 | 59 | 141 | 33 | 352 | 49 |

### C7. Foot Locker womens shoes: listing counts by brand (brand filter counts) and Nike Inc share of focus-brand listings

| snapshot_date | ASICS | Brooks | Converse | HOKA | Jordan | New Balance | Nike | On | PUMA | Saucony | Under Armour | adidas | nike_inc_share_pct |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2021-01-19 | 23 | 12 | 33 |  | 24 | 16 | 277 |  | 66 | 1.000 |  | 25 | 70 |
| 2021-04-10 | 16 | 8.000 | 28 |  | 17 | 12 | 205 |  | 77 | 1.000 |  | 38 | 62 |
| 2021-07-01 | 11 | 8.000 | 34 |  | 10 | 17 | 221 |  | 71 | 1.000 |  | 30 | 66 |
| 2021-10-05 | 15 | 10 | 33 |  | 5.000 | 19 | 208 | 6.000 | 60 | 1.000 |  | 35 | 63 |
| 2022-01-04 | 19 | 12 | 44 |  | 16 | 26 | 238 | 9.000 | 78 | 1.000 |  | 35 | 62 |
| 2022-04-01 | 18 | 24 | 55 |  | 20 | 31 | 267 | 14 | 79 |  |  | 59 | 60 |
| 2022-08-01 | 26 | 32 | 59 | 5.000 | 36 | 26 | 288 | 15 | 80 |  |  | 86 | 59 |
| 2022-10-03 | 33 | 71 | 75 | 70 | 38 | 63 | 333 | 16 | 87 | 15 | 7.000 | 124 | 48 |
| 2023-01-03 | 30 | 47 | 87 | 58 | 43 | 52 | 306 | 24 | 94 | 2.000 |  | 124 | 50 |
| 2023-04-07 | 31 | 109 | 99 | 41 | 57 | 76 | 326 | 37 | 87 | 7.000 | 18 | 103 | 49 |
| 2023-07-14 | 41 | 109 | 114 | 54 | 93 | 90 | 389 | 52 | 110 | 11 | 23 | 127 | 49 |
| 2023-10-02 | 46 | 111 | 120 | 65 | 110 | 89 | 408 | 53 | 116 | 12 | 24 | 105 | 51 |
| 2024-01-01 | 45 | 91 | 101 | 66 | 114 | 95 | 434 | 56 | 109 | 12 | 21 | 96 | 52 |
| 2024-04-02 | 34 | 90 | 86 | 66 | 129 | 84 | 446 | 55 | 90 | 12 | 21 | 123 | 53 |
| 2024-07-06 | 25 | 91 | 89 | 81 | 145 | 98 | 467 | 65 | 76 | 10 | 16 | 105 | 55 |
| 2024-10-01 | 26 | 73 | 84 | 83 | 135 | 87 | 455 | 74 | 74 | 8.000 | 14 | 69 | 57 |
| 2025-03-13 | 18 | 55 | 68 | 76 | 106 | 91 | 459 | 74 | 70 | 39 | 17 | 82 | 55 |
| 2025-04-16 | 20 | 52 | 66 | 75 | 90 | 94 | 420 | 68 | 75 | 45 | 17 | 83 | 52 |
| 2025-09-21 | 42 | 47 | 55 | 112 | 84 | 98 | 458 | 60 | 75 | 67 | 14 | 411 | 39 |
| 2026-07-21 | 45 | 71 | 11 | 75 | 100 | 78 | 526 | 62 | 68 | 59 | 8.000 | 389 | 43 |
| 2026-10-13 | 43 | 68 | 11 | 56 | 94 | 91 | 513 | 55 | 71 | 119 | 9.000 | 348 | 42 |

### C8. Amazon Best Sellers (top 30, six shoe lists), averages by half-year

| period | snapshots | nike_inc_share_top30_pct | nike_inc_avg_stars | peer_avg_stars | hoka_on_items |
|---|---|---|---|---|---|
| 2022H1 | 8 | 2.475 | 4.600 | 4.560 | 0.000 |
| 2022H2 | 9 | 0.367 | 4.600 | 4.534 | 0.000 |
| 2023H1 | 11 | 2.109 | 4.617 | 4.516 | 0.273 |
| 2023H2 | 2 | 1.650 | 4.700 | 4.521 | 0.500 |
| 2024H1 | 3 | 4.467 | 4.600 | 4.499 | 0.667 |
| 2024H2 | 4 | 2.475 | 4.600 | 4.499 | 0.500 |
| 2025H1 | 5 | 1.980 | 4.700 | 4.503 | 0.800 |
| 2025H2 | 16 | 4.994 | 4.567 | 4.499 | 0.562 |
| 2026H1 | 12 | 5.817 | 4.600 | 4.501 | 0.833 |
| 2026H2 | 8 | 8.325 | 4.462 | 4.428 | 1.500 |

### C9. Foot Locker catalog (Bazaarvoice), top products by review count: lifetime average rating

| brand | products | total_reviews | review_weighted_avg_rating |
|---|---|---|---|
| ASICS | 200 | 6,735 | 4.550 |
| Brooks | 200 | 85,442 | 4.394 |
| Converse | 200 | 35,819 | 4.641 |
| HOKA | 92 | 16,151 | 4.678 |
| Jordan | 200 | 47,977 | 4.603 |
| New Balance | 200 | 64,465 | 4.592 |
| Nike | 200 | 123,393 | 4.544 |
| On | 95 | 640 | 4.478 |
| PUMA | 200 | 3,682 | 4.507 |
| Skechers | 36 | 67 | 4.746 |
| Under Armour | 200 | 17,553 | 4.236 |
| adidas | 200 | 237,473 | 4.687 |

### C10. Foot Locker live listing pages today (2026-10-13), top 200 by relevance per brand (ratings shown rounded to whole stars)

| query_brand | gender | products | share_with_reviews | total_reviews | median_reviews | review_weighted_rating | share_on_sale |
|---|---|---|---|---|---|---|---|
| Brooks | mens | 62 | 0.855 | 27,801 | 291 | 4.714 | 0.048 |
| Brooks | womens | 68 | 0.765 | 32,991 | 225 | 4.286 | 0.103 |
| Converse | mens | 31 | 0.710 | 38,812 | 3.000 | 5.000 | 0.387 |
| Converse | womens | 11 | 0.909 | 1,970 | 12 | 4.995 | 0.273 |
| HOKA | mens | 80 | 0.850 | 32,108 | 29 | 4.990 | 0.225 |
| HOKA | womens | 55 | 0.836 | 36,650 | 52 | 4.997 | 0.091 |
| Jordan | mens | 176 | 0.920 | 62,948 | 135 | 4.910 | 0.193 |
| Jordan | womens | 92 | 0.924 | 12,165 | 46 | 4.400 | 0.174 |
| New Balance | mens | 127 | 0.976 | 54,889 | 62 | 4.641 | 0.228 |
| New Balance | womens | 81 | 0.938 | 94,829 | 426 | 4.913 | 0.321 |
| Nike | mens | 200 | 0.905 | 56,494 | 77 | 4.596 | 0.260 |
| Nike | womens | 184 | 0.842 | 70,632 | 218 | 4.594 | 0.212 |
| On | mens | 60 | 0.900 | 460 | 3.000 | 4.933 | 0.117 |
| On | womens | 51 | 0.804 | 1,021 | 15 | 4.818 | 0.235 |
| PUMA | mens | 59 | 0.593 | 252 | 1.000 | 4.730 | 0.322 |
| PUMA | womens | 70 | 0.571 | 638 | 1.000 | 4.759 | 0.186 |
| Under Armour | mens | 33 | 0.576 | 3,889 | 4.000 | 4.896 | 0.000 |
| Under Armour | womens | 9.000 | 0.111 | 79 | 0.000 | 5.000 | 0.000 |
| adidas | mens | 200 | 0.835 | 450,947 | 294 | 4.997 | 0.185 |
| adidas | womens | 188 | 0.915 | 215,256 | 725 | 4.994 | 0.112 |

## D. Test against Nike's own results

**Set-up.** Nike Inc AbnormalTone from Amazon (Nike fiscal quarters) against Nike's reported revenue (nike_filing_facts.csv, metric `revenues`) and NIKE Direct growth (`growth_nike_direct_reported_pct`; Q3 FY2024 derived from `revenue_nike_direct`). Two sales measures as in the paper: same-quarter YoY growth (SameQtrSalesGrowth) and AbnormalSales = (sales in q minus mean of the previous four quarters) / that mean. Main test: tone in quarter q against sales in quarter q+1. The revenue file starts at Q1 FY2018, so YoY growth starts Q1 FY2019; the last usable tone quarter is Q1 FY2024. Quarterly NIKE Direct growth starts Q1 FY2021.

| Tone measure (quarter q) | Outcome | Sample | n | Pearson r | p | Spearman rho | p |
|---|---|---|---|---|---|---|---|
| AbnormalTone | revenue YoY, q+1 | Q4 FY2018 to Q1 FY2024 | 22 | -0.14 | 0.54 | -0.01 | 0.98 |
| AbnormalTone | revenue YoY, q+1 | same, ex COVID | 17 | +0.26 | 0.31 | +0.16 | 0.53 |
| AbnormalTone | revenue YoY, q+1 | ends Q3 FY2023 (before coverage drop) | 20 | -0.12 | 0.63 | +0.12 | 0.62 |
| AbnormalTone | AbnormalSales, q+1 | full | 22 | -0.22 | 0.33 | -0.17 | 0.46 |
| AbnormalTone | AbnormalSales, q+1 | ex COVID | 17 | +0.41 | 0.11 | +0.34 | 0.18 |
| Negative_AbnormalTone | AbnormalSales, q+1 | full | 22 | -0.22 | 0.33 | -0.18 | 0.42 |
| Negative_AbnormalTone | AbnormalSales, q+1 | ex COVID | 17 | +0.46 | 0.06 | +0.33 | 0.19 |
| Negative_AbnormalTone | revenue YoY, q+1 | ex COVID | 17 | +0.28 | 0.27 | +0.25 | 0.33 |
| AbnormalTone | NIKE Direct YoY, q+1 | Q4 FY2020 to Q1 FY2024 | 14 | -0.22 | 0.45 | -0.28 | 0.33 |
| AbnormalTone | NIKE Direct YoY, q+1 | ex COVID | 10 | -0.11 | 0.77 | -0.09 | 0.81 |
| RelAbnormalTone (Nike minus peers) | NIKE Direct YoY, q+1 | full | 14 | -0.53 | 0.05 | -0.40 | 0.15 |
| AbnormalTone (VADER) | revenue YoY, q+1 | ex COVID | 17 | +0.24 | 0.35 | +0.47 | 0.06 |
| AbnormalTone | revenue YoY, same quarter | full | 21 | +0.10 | 0.66 | +0.19 | 0.42 |

"Ex COVID" drops the tone quarters Q3 FY2020, Q4 FY2020, Q1 FY2021, Q3 FY2021, Q4 FY2021 so that neither the March to May 2020 collapse nor the March to May 2021 rebound (+96% YoY) sits on either side of a pair. An OLS in the spirit of the paper's Equation (1) (next-quarter AbnormalSales on AbnormalTone, AbnormalRating, AbnormalReviewCnt; n = 22, no controls or fixed effects) gives AbnormalTone -1.85 (t = -1.04), AbnormalRating +1.23 (t = 1.46), AbnormalReviewCnt -0.0027 (t = -3.11). Full results: data/nike_tone_correlations.csv, data/nike_tone_ols_eq1_style.csv, panel in data/nike_tone_vs_fundamentals.csv.

**Reading it honestly.**
* With all quarters, there is no link. The sample is dominated by the COVID collapse and rebound, which have nothing to do with how people felt about their shoes.
* Without COVID, every tone measure points the paper's way (better tone, stronger next-quarter sales; the negative-change measure is the strongest, r = +0.46, p = 0.06), but n = 17 and nothing is significant at 5%. This is suggestive, not evidence.
* NIKE Direct growth shows no positive link. The Nike-minus-peers version is negatively correlated (r = -0.53, p = 0.05), which most likely reflects that Nike's Amazon reviews after Nov 2019 come from third-party sellers, a channel that competes with NIKE Direct rather than mirroring it.
* Caveats: one firm and 22 or fewer quarters (the paper uses 6,726 firm-quarters with controls, industry and year effects); star-derived training labels instead of human coding; Nike's Amazon presence changed mid-sample; the dataset's coverage thins from April 2023; Nike's revenue is global while Amazon US reviews are one US channel.
* What does line up: Nike's most negative AbnormalTone (Q2 FY2022, Sep to Nov 2021, -0.094) came one quarter before revenue growth stalled (Q3 FY2022, -0.9% YoY), and the run of positive AbnormalTone in FY2023 coincided with the strong FY2023 revenue quarters. Anecdotes, not a test.

## E. Verdict: what review data says about Nike product quality and consumer sentiment, 2022 to 2026

1. **2020 to 2021: a Nike-specific deterioration on Amazon, partly self-inflicted by channel strategy.** Nike's Amazon rating fell 0.45 stars from FY2020 to its worst quarter (3.90 in Q2 FY2022) against about 0.25 for peers, and its 1 to 2 star share reached 23%, the highest of the ten firms. Counterfeit and "fake" mentions rose fastest for Nike. Quality-failure mentions ("fell apart", "ripped", "poor quality") also rose for Nike (2.8% of reviews in FY2020 to 4.5% in FY2022), but they rose for New Balance (3.7% to 5.4%) and adidas (2.7% to 3.9%) too, so the product-quality signal on its own is not clearly Nike-specific.
2. **Late 2021 to 2023: the Amazon decline stopped.** The Nike-minus-peer tone gap narrowed from -0.10 to about -0.06, Nike's stars recovered to 4.07 in Q3 FY2023, and AbnormalTone was positive in four of the last five usable quarters. On nike.com the honest-review rating rose to its high in FY2024 (4.80 in Q2 FY2024).
3. **2024 to early 2026: a second, nike.com-visible decline in unpaid reviews.** Non-incentivized nike.com ratings slid over nine quarters (one bounce, in Q3 FY2025), from 4.80 (Q2 FY2024) to 4.47 (Q3 FY2026), with 1 to 2 star shares up from 2.3% to 8.6% and AbnormalTone negative from Q4 FY2024 to Q4 FY2026. This lines up with the period of Nike's revenue declines and franchise fatigue. The headline nike.com rating hid most of this (it only fell to 4.59 to 4.61) because the share of incentivized reviews jumped from about 15% to over 40%; incentivized reviews rate higher. An investor reading only Nike's displayed stars would have missed the deterioration.
4. **Signs of a bottom, mid 2026.** (a) Non-incentivized nike.com rating up two quarters in a row (4.47, 4.49, 4.54) and AbnormalTone positive in Q1 FY2027 (+0.007) with AbnormalRating +0.039, the first positive reading on both since FY2024; 1 to 2 star share down from 8.7% to 7.2%. (b) Foot Locker's mostly syndicated Nike Inc reviews had positive AbnormalTone in all four FY2026 quarters (+0.03, +0.03, +0.06, +0.03) and the 1 to 2 star share fell from 9.1% (Q1 FY2025) to about 5% (FY2026), although Q1 FY2027 dipped again (-0.03, 7.0%). (c) Shelf space: Nike Inc's share of focus-brand men's shoe listings at Foot Locker is back to 49% (from a 35% trough in 2022 to 2023); nike.com's own men's shoe wall rose from 630 styles (May 2026) to between 762 and 791 (Aug to Oct 2026), per the other agent's wall history. (d) Amazon Best Sellers: Nike Inc items now take about 8% of top-30 slots, versus about 2% in 2022 to 2025, consistent with Nike's broader presence on Amazon again.
5. **Competitive context.** On review stars Nike is not an outlier today: Foot Locker product-level averages are Nike 4.54, Jordan 4.60, Converse 4.64 versus adidas 4.69, HOKA 4.68, New Balance 4.59, Brooks 4.39, On 4.48 (lifetime averages of the top 200 products per brand). HOKA and On kept gaining Amazon Best Seller presence (HOKA plus On items per top-30 list rose from 0 in 2022 to about 1.5 in late 2026) and HOKA's Foot Locker listings roughly held up. Nike's problem in 2024 to 2025 looked more like weaker enthusiasm for current product (falling unpaid ratings) than a collapse in quality.
6. **Bottom line for the investment case.** Review data supports a "sentiment trough in late 2025 to early 2026, early stabilisation in mid 2026" narrative, with two quarters of improving unpaid ratings and recovering wholesale shelf space. It is a modest, noisy signal: the formal link to Nike's sales in 2018 to 2023 was not statistically reliable, and the recent data has survivorship and incentivized-review biases. Worth monitoring each quarter (rerun scripts/parse_nike_turnto.py and scripts/recent_tone.py after refreshing the TurnTo fetch); a further rise in unpaid nike.com ratings and positive AbnormalTone in Q2 FY2027 (Sep to Nov 2026) would strengthen the bottoming case, and a fall back below 4.50 would weaken it.

## F. Files

All under /tmp/claude-0/-home-user-nike-research-case-comp/97c520cc-64e5-53f3-8fe9-898f5b11e054/scratchpad/reviews/ .

Scripts (scripts/):
* stream_gz.py: resumable HTTP Range streamer, decompresses to stdout, writes nothing to disk.
* meta_candidates.py: loose brand candidates from the metadata stream.
* match_brands.py: exact store allow-list, title token and third-party filters, writes data/matched_products.csv.gz.
* filter_reviews.py: keeps reviews of matched parent_asins from the review stream.
* tone_quarterly.py: dedupe, Naive Bayes (15k and 200k) and VADER tone, calendar and Nike fiscal quarter aggregation, Abnormal variables.
* complaint_themes.py: fake, used, quality and sizing mention shares by firm and fiscal year.
* fundamentals_test.py: correlations and Eq. (1)-style OLS against Nike revenue and NIKE Direct.
* fetch.py: polite cached curl fetcher with 429 backoff. brandmatch.py: shared brand rules.
* parse_amazon_bestsellers.py, parse_footlocker.py, parse_nike_turnto.py, bv_brand_ids.py, bv_footlocker_reviews.py, recent_tone.py, summarise_part2.py, make_tables.py.

Data (data/):
* matched_products.csv.gz (359,097 products: parent_asin, brand, firm, store, title, category, footwear flag); meta_candidates.jsonl.gz.
* amazon_reviews_filtered.csv.gz (3,182,474 raw matched reviews with rating, title, text, timestamp, verified, helpful votes, user id); amazon_reviews_scored.parquet (3,144,610 deduped reviews with tone scores, quarters).
* amazon_quarterly_calendar.csv and amazon_quarterly_nike_fiscal.csv (per firm, per brand and footwear-only firm: listings_proxy, review_cnt, avg_rating, share_1_2_star, tone means and SDs, AbnormalTone, AbnormalTone_big, AbnormalTone_vader, AbnormalRating, AbnormalReviewCnt, StdDevTone, StdDevRating, Negative_ and Positive_AbnormalTone).
* tone_model_info.json, nb_model_15k.pkl; amazon_complaint_themes_by_fy.csv.
* nike_tone_vs_fundamentals.csv, nike_tone_correlations.csv, nike_tone_ols_eq1_style.csv.
* nike_styles_queried.csv, nike_com_reviews.csv.gz, nike_com_style_summary.csv; footlocker_bv_reviews.csv.gz, footlocker_bv_products.csv, footlocker_bv_brand_stats.csv, bv_brand_ids.json; recent_reviews_scored.csv.gz, recent_reviews_quarterly_fiscal.csv.
* footlocker_live_items.csv, footlocker_live_brand_facets.csv, footlocker_live_ratings_by_brand.csv, footlocker_wayback_items.csv, footlocker_wayback_brand_facets.csv, footlocker_listing_counts_by_brand.csv, footlocker_nike_inc_listing_share.csv.
* amazon_bestsellers_ratings.csv (item level: rank, brand, stars, rating count), amazon_bestsellers_snapshot_summary.csv, amazon_bestsellers_by_halfyear.csv.
* tables_draft.md (the Section C tables).

Raw downloads (untrusted, kept separate from scripts) are in dl/ (amazon_wayback, footlocker, footlocker_wayback, nike, nike_turnto, bv, cdx) with fetch logs.
