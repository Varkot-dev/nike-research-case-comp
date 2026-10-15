# reviews_sentiment: product reviews and enthusiast chatter as a sell-through and quality proxy

Pulled 2026-10-14 (UTC). Question served: is Nike's running recovery real consumer sell-through, and is product quality improving (crux 6, running quality; also crux 1 NA sell-through, crux 4 discounting, crux 5 lifestyle bottom).

No logins, no cookies, no personal data in any request. Every script sleeps between requests (1.2 s to 2.5 s). Reviewer names, user ids and review text are NOT kept in any tidy file (only dates, stars, flags).

## Tidy files

| File | What it is | Rows / period |
|---|---|---|
| nike_reviews_tidy.csv.gz | nike.com reviews (TurnTo) one row per review: style, model, family, generation, date, stars, incentivized flag and type (SAMPLE, SWEEPSTAKES), fit, comfort, locale, US flag | 33,581 reviews, 170 styles with reviews, May 2016 to Oct 13 2026 |
| nike_reviews_monthly_by_model.csv | same, monthly by model: count, US count, organic (non-incentivized), avg stars, 1-2 star share | monthly |
| nike_launch_cohorts.csv | per model: launch proxy (2nd percentile of review dates), reviews in first 90/180/270/365 days, organic US counts, stars, incentivized share | 59 models |
| nike_styles_input.csv | style codes queried (51 analyst-listed historical codes validated by TurnTo's own catalog title, plus 190 current codes from the repo nike.com feed) | 241 |
| fl_bv_reviews_tidy.csv.gz | Foot Locker Bazaarvoice reviews for running families (Pegasus, Vomero, Structure, Invincible, Winflo, Clifton, Bondi, Arahi, Novablast, Nimbus, Kayano, Cumulus, Ghost, Adrenaline, Glycerin, Cloudmonster, Ride, Triumph, 880) with syndication source (dickssportinggoods.com, brooksrunning.com, Nike, eastbay.com, FL native), deduped across product ids | 98,900 deduped tagged reviews (Nike 16,034, Brooks 67,954, HOKA 9,117, ASICS 4,627, Saucony 1,069, On 99), 2008 to Oct 2026 |
| fl_bv_monthly_family.csv | monthly counts and stars by brand, family, generation | monthly |
| zappos_listing_snapshot_2026-10-14.csv | Zappos running listings and model searches: review count, rating, price, sale flag, % off | snapshot |
| zappos_reviews_tidy.csv | Zappos native reviews (date, stars, fit) for 30 products: Pegasus 41/42, Vomero 18, Structure 26, Clifton 10/11, Bondi 9, Novablast 5/6, Nimbus 27/28, Ghost 17/18, Cloudmonster 1/2/3 | 6,694 deduped reviews with source (Zappos native vs brand-syndicated) and incentive flags, 2022 to Oct 2026 |
| zappos_launch_cohorts.csv | same-age cohorts on Zappos (first 90/180/365 days), stars, 1-2 star share, last-90-day flow | 16 models |
| fleetfeet_products_2026-10-14.csv | Fleet Feet public search index, one row per product: review count, average rating, fit, trendScore, views 7/30/60 days (so prior-30-day views = views60 - views30), inventory, price | 2,115 products, 10 brands, snapshot |
| reddit_posts_tagged.csv.gz | Reddit post metadata (id, time, score, comments, flair; titles dropped) tagged by brand and model regex | r/RunningShoeGeeks 79,451 posts Jan 2019 to Oct 2026; r/Nike and r/Hoka Jan 2021 to Oct 2026 (167,539 posts in all). r/Sneakers pull was stopped at Jul 2021 and dropped (too slow); re-run the script to add it |
| reddit_monthly_mentions.csv | monthly brand/model mention counts, comments, Deal-flair and Review-flair posts | monthly |
| test1_... to test4_... | outputs of scripts/run_tests.py | |

## Sources and methods

1. **nike.com reviews (TurnTo).** `https://cdn-ws.turnto.com/v5/sitedata/78GDJmj4zEDYwwHsite/{STYLE}/d/review/en_US/{offset}/1000/RECENT/false/false/`. The site key is the `turnToSiteKey` value in the nike.com product page source (fetched 2026-10-14). Paging by 1000 reaches the full history (the earlier repo pull capped at the newest 1000). Script: scripts/pull_nike_turnto.py, clean: scripts/clean_nike_turnto.py.
2. **Foot Locker Bazaarvoice.** `https://api.bazaarvoice.com/data/products.json` (Search=keyword, Stats=Reviews) and `/reviews.json` (Filter=ProductId, ContentLocale:en_US) with the public display passkey already used in the repo (scripts/reviews/bv_footlocker_reviews.py on branch claude/wonderful-franklin-u31n4e). Scripts: pull_footlocker_bv_models.py (product search + Nike reviews), pull_footlocker_bv_reviews_subset.py (rival reviews), clean_footlocker_bv.py. Key discovery: most FL running reviews are syndicated, and the biggest source is **dickssportinggoods.com**, which gives a consistent third-party, non-brand-site review stream for Nike, HOKA, Brooks and ASICS.
3. **Zappos.** Listing JSON in `window.__INITIAL_STATE__` of `https://www.zappos.com/search?term=...` and `/men-running-shoes`; reviews from `https://www.zappos.com/product/review/{productId}/page/{n}/orderBy/newest` (25 per page, page cap 80). Script: pull_zappos.py, clean_zappos.py. Raw v1 pull (no incentive flags) in raw/zappos/v1; v2 adds incentivizedReview, customerRewardReview, premierReview, source.
4. **Fleet Feet.** Public Typesense index `fleetfeet_product_variants_v5` (search-only key in `window.ffTypesense` on fleetfeet.com browse pages; key not stored here, re-read it from the page). Grouped by product.slug. Script: pull_fleetfeet_reviews_views.py, clean_fleetfeet.py.
5. **Reddit via Arctic Shift.** `https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=...&after=...&limit=auto&sort=asc&fields=id,created_utc,title,num_comments,score,link_flair_text` (author not requested). Script: pull_reddit_arcticshift.py, clean_reddit.py (brand and model regex on titles).
6. **Trustpilot nike.com** (WebFetch summary, snapshot 2026-10-14): 13,171 reviews, TrustScore 1.5, 76% one-star, 14% five-star. Recent reviews about one a day. Customer-service complaints, not product; not used in tests.

## Blocked or not usable (2026-10-14)

- reddit.com JSON search: 403. api.pullpush.io: 429. Arctic Shift aggregate and full-text endpoints: "Timeout" errors (bulk paging works; 422 retries are normal).
- trustpilot.com via curl: 403 (WebFetch worked for one snapshot).
- hoka.com 403/406, asics.com 403, brooksrunning.com 403, newbalance.com 403, on.com (bot page), rei.com 403, kohls.com 403, finishline.com 403, jdsports.com 403, scheels.com 403, hibbett.com 403, famousfootwear.com 403, dickssportinggoods.com 403 (its reviews reached via Foot Locker syndication instead), academy.com 503 on product pages.
- web.archive.org CDX: connection failed (so no archived review counts).
- Amazon live review pages: not fetched (login wall; repo already has McAuley 2023 dataset).
- Running Warehouse: reachable but review volumes tiny (Pegasus 42 colourway 0, Clifton 10 13, Ghost 17 1). Road Runner Sports: reachable, PowerReviews, Pegasus 42 only 19 reviews; PowerReviews merchant key not found in bundles, search API 403.
- Fleet Feet review dates: native widget, not in the index; only counts and averages.

## Caveats

- Review volume is a proxy for units, not units. Prompts, sampling programs and syndication deals change counts. nike.com incentivized (free sample) reviews are flagged and excluded in "organic" series; Dick's and Zappos reviews carry no or few incentive flags.
- nike.com coverage: older generations are queried by their main style code only, current models by every style code in the Oct 13 feed, so all-style totals overstate recent growth. Tests use the main code (most-reviewed style per model and gender) only.
- Dick's syndication into Foot Locker steps up in June 2025 for every brand and lags at the end (Aug to Oct 2026 counts collapse for all brands, Dec 2025 also near zero). Year-on-year tests use June to July windows, which sit inside the stable regime, and cross-brand shares, which the common step does not move.
- Brooks counts at FL are dominated by brooksrunning.com syndication in 2020 to 2023. The Nike worker (pull_footlocker_bv_models.py) was stopped once it reached the rival terms, which the second worker had already covered; its gz file is truncated at the end and the cleaner reads it up to the last full line.
- Zappos reviews are partly syndicated from brand sites (source = Hoka, ASICS, Brooks Running, Nike); brand-syndicated reviews rate higher for every brand, so rating comparisons use Zappos-native reviews or Dick's-sourced reviews.
- r/RunningShoeGeeks post counts fall sharply after 2024 (subreddit rules or archive coverage), so only shares are used, not levels.
- Fleet Feet is one snapshot; views30 vs prior 30 days is the only time comparison.

## Tests run (scripts/run_tests.py, plus test5 inline)

| Test | Pre-registered LONG / SHORT reading | Result |
|---|---|---|
| T1 nike.com organic US reviews, Jun-Sep, main style codes | LONG: performance running organic volume still growing double digits and lifestyle decline narrowing. SHORT: running decelerating to low growth and lifestyle still falling at the same pace | Perf running organic US +107% (2025) then +9% (2026, 437 vs 402). Lifestyle -32% (2025) then -32% (2026, 152 vs 223). Organic perf running rating 4.45 (2024) to 4.51 to 4.60. |
| T2 Dick's-sourced reviews (Foot Locker BV syndication), Jun-Jul YoY by brand | LONG: Nike running review flow at a third-party retailer grows faster than HOKA, Brooks, ASICS. SHORT: slower | Nike +49% (407 to 605), HOKA +22%, Brooks +16%, ASICS 0%. Nike share of the four brands 19.3% to 23.1%, but down from a 29% to 30% peak in Feb-Mar 2026. |
| T3 ratings on third-party, non-incentivized reviews by generation | LONG: current Nike generation rated at or above predecessor and peers. SHORT: below | Dick's: Pegasus 42 4.85 (n=82) vs Pegasus 41 4.78; Vomero 18 4.79; Clifton 11 4.55 vs Clifton 10 4.78; Ghost 18 4.85; Nimbus 27 4.69. Nike FY27Q1 4.80, 1-2 star 1.6%, best of the four brands. Zappos native: Structure 26 weak (3.08 at 180 days, 42% 1-2 star). |
| T4 r/RunningShoeGeeks deal intensity (Nike share of Deal-flair posts / Nike share of brand mentions) | LONG: falling. SHORT: rising | FY27Q1 (Jun-Aug 2026) 1.73, highest since at least FY23 (FY26Q1 0.97). Nike share of deal posts 32.9% vs 18.8% a year earlier, z = 3.43, p = 0.0006, while Nike mention share is flat at 19%. |
| T5 subreddit activity | LONG: r/Nike holding vs r/Hoka. SHORT: falling | r/Nike posts FY27Q1 2,816 vs 5,029 (-44%); r/Hoka 546 vs 496 (+10%). Archive coverage also fell for r/RunningShoeGeeks (-55%), so weak evidence. |

## Checker review

Checked 2026-10-14 by a second agent. Re-pull files are in raw/checker/ (no logins, public endpoints only, 2 to 3 s sleeps).

### Re-pulls against the original sources

| Dataset | Sample re-pulled | Result |
|---|---|---|
| nike.com TurnTo | first 1,000 reviews of HM6803 (Vomero 18 M), FD2722 (Pegasus 41 M), CW2288 (AF1 '07 M) | 3,000 of 3,000 review ids found in nike_reviews_tidy, 0 rating or incentive-flag mismatches; totals 1534 / 1424 / 4271 match (tidy has 4269 for CW2288). Dates are UTC from dateCreatedMillis and line up. |
| Foot Locker Bazaarvoice | all en_US reviews of products 449620 (Vomero 18), 440649 (Clifton 10), 478381 (Ghost 17) | 449620 and 440649: 100% of ids in tidy, 0 rating mismatches, Dick's-sourced Jun-Jul 2025 and 2026 counts identical (81/80 and 187/427). 478381: 64 brooksrunning.com reviews absent from tidy; they are in the raw file and are dropped by design by the (src_name, submitted, rating) dedupe. Does not touch the Dick's tests. |
| Reddit (Arctic Shift) | r/RunningShoeGeeks, 3 two-day windows (Jul 2025, Jul 2026, Aug 2026) | 41/41, 52/52, 23/23 ids match; only flair difference is null vs NaN encoding. |
| Fleet Feet Typesense | mens/womens Pegasus 42, mens Clifton 10 | views7/30/60, review count and rating identical to the snapshot. Views are product-level (same on every variant doc), so group_limit=1 is fine. The page key excludes sales and cogs fields; nothing was attempted beyond it. |
| Zappos | page 1 of 10043215 (Pegasus 42), 10020711 (Vomero 18), 10047368 (Clifton 11) | 73 of 73 (date, rating) pairs match. Clifton 11 shows 43 total now vs 41 in tidy; the regex parser also returns 23 of 25 reviews on that page, so a small parse loss (about 1 in 12 on some pages) exists. |

Cleaning: no duplicate review ids in any tidy file; no full-row duplicates; dates parse; Zappos and BV ratings are 1-5 integers. All test CSVs reproduce byte-for-byte from scripts/run_tests.py.

### Tests: what holds and what does not

- **T2 Dick's YoY (claimed LONG, moderate): overstated, downgrade to LONG weak.** The Nike bucket includes new franchises (Vomero Plus 0 to 167, Pegasus Premium 39 to 50) and the lifestyle Zoom Vomero 5 (92 to 66, the "vomero" regex catches it), while the rival search terms cover only legacy families (no HOKA Mach or Skyward, no ASICS Superblast, no Brooks Glycerin Max), so rival new launches are out of scope. Like-for-like core families (numbered Pegasus, Vomero excl. 5, Structure, Winflo, Invincible): Nike +31% (243 to 318) vs HOKA +22%, Brooks +16%, ASICS 0%. Nike share of the core four-brand flow 12.5% to 13.6%, z about 1.1, p about 0.29: not significant. Also Pegasus 41 still out-reviewed Pegasus 42 at Dick's in Jun-Jul 2026 (102 vs 49), which is prior-generation sell-through, likely at markdown.
- **T1 nike.com organic (claimed SHORT, moderate): direction holds, magnitude not robust.** Running growth of +9% depends on the main-style restriction and on September. All style codes: +32% (423 to 557). Jun-Aug only: +23% main-style, +47% all styles; September alone -41% main, -17% all. So "decelerating from +107%" holds, "low growth" does not. Lifestyle -32% holds under both codings (226 to 154 all styles) and is significant (z about 3.7), but it rests on 9 aging style codes (2019-2021 launches) with 7 to 35 organic reviews each per window, so it partly measures SKU age. Keep moderate SHORT on lifestyle, weak on running.
- **T3 ratings (claimed LONG, strong): downgrade to LONG moderate.** Dick's Jun-Aug 2026, Zoom Vomero 5 removed: Nike 4.785 (se 0.023, n=666), Brooks 4.786 (se 0.021), HOKA 4.765 (se 0.019), ASICS 4.56. Nike ties Brooks, it is not clearly best. Pegasus 42 vs 41 (4.85 vs 4.78, n=82) is inside noise. The nike.com organic 180-day trend across generations (Pegasus 39 4.43 to 42 4.70; Vomero 17 4.41 to 18 4.72) is the stronger part. Parity with rivals plus a clear generational improvement, with Structure 26 the exception.
- **T4 Reddit deal intensity (claimed SHORT, moderate): holds.** After removing near-duplicate reposts (first 35 alphanumeric characters of the title), Nike share of brand tags on Deal posts is 32.7% (50 of 153) vs 18.3% (42 of 229), z = 3.21, p = 0.0013. Sep to mid-Oct 2026 is 26%, still above every FY26 quarter. The deal titles are dominated by Vomero Plus and Vomero Premium at $67 to $110 (list about $180) and Nike outlet clearance posts, which ties the signal to the new franchises that drive T2. Small counts; shares only.
- **T5 r/Nike vs r/Hoka (weak SHORT): stays weak.** r/Hoka monthly volume in the same archive is flat to up, which argues against a pure archive-coverage artefact, but r/Nike is mostly a sneaker and lifestyle forum and mod rules are unknown.
- **T6 Fleet Feet views (weak LONG): stays weak.** One window, and brand view changes are driven by model transitions (Clifton 10 views -42% vs prior 30 days as Clifton 11 arrives; men's Pegasus 42 -23%).

Net: the review data support "Nike running product is good and selling through at parity or slightly better than peers, with growth carried by new franchises that are already being discounted heavily", and "lifestyle has not bottomed on nike.com". They do not support a strong LONG on running sell-through.
