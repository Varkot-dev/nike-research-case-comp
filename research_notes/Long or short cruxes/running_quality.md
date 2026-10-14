# Crux: Is Nike's running recovery real share gain at healthy prices, or discount-driven?

Prepared 2026-10-14. Labels: OPENED = fetched and read in this session. OPENED (repo) = data fetched by an earlier researcher and stored in this repo, not re-fetched. SNIPPET = search-result summary only. [my arithmetic] = computed by me.

## 0. Pre-registered decision rules (written 2026-10-14 before any new data was gathered)

Measures: (a) share of CURRENT-generation Nike running models (Pegasus 42, Vomero 18, Vomero Plus, Structure 26, Pegasus Plus) that are discounted at run-specialty and mass retailers, vs the current-generation models of Hoka, On, ASICS, Brooks, Saucony on the same shelf; (b) the trend of Nike's markdown rate at the same retailer over time (archived snapshots); (c) whether competitors that report results say Nike is taking share, and whether they say the market is promotional; (d) industry data (Running Industry Association, Circana) on Nike's share and price in run.

Points LONG (durable full-price share gain):
- L1. Current-generation Pegasus 42 and Vomero 18 sell at full price at run specialty (Running Warehouse, Fleet Feet) and on nike.com in Oct 2026, with discounts limited to outgoing generations, the same pattern as Hoka, ASICS and Brooks.
- L2. Nike's markdown rate at Running Warehouse falls over time or is at or below the store average.
- L3. On, Deckers (Hoka) and ASICS report slower US growth or name Nike as a competitive factor AND describe the market as full-price (no promotional pressure).
- L4. Industry data (RIA, Circana) show Nike's run-specialty dollar share up with flat or rising average price.

Points SHORT (share bought with discounts):
- S1. Current-generation Pegasus 42 and Vomero 18 are widely discounted (one third or more of colorways) at specialty and mass retailers within about a year of launch, while competitors' current models are not.
- S2. Nike's Running Warehouse markdown rate is rising and well above the store and Hoka, On, ASICS.
- S3. Competitors report continued strong growth with no Nike pressure, or name Nike discounting as the cause of any pressure.
- S4. Industry data show Nike unit share up but average price down.

Neutral or unresolved: Nike discounts mostly older colorways in line with its own historical seasonal cadence (Nike has always run many colorways per model and cleared old colorways mid-life), or signals split.

## 1. Verdict (my judgement, after the data below)

**Points SHORT, moderate strength.** Nike's running growth is real (category and Nike both growing double digits) and Nike's shelf at Fleet Feet, the largest U.S. run-specialty chain, is clean and under-supplied. But the volume franchises that carry the recovery, Pegasus 42 and Vomero 18, are being moved at about 25% off through Nike's own nike.com and through online specialty clearance within 6 to 8 months of launch, faster than Pegasus 41 was marked down in 2024, while Hoka, ASICS and Brooks discount only outgoing model versions. Nike's own site sells the same Vomero 18 colourways for up to 30% less than Fleet Feet does. Competitors (Hoka, ASICS) report U.S. full-price sell-through and share gains in the same period, and On blames a "highly promotional" U.S. running market. The recovery is not "full-price share gain"; it is growth that is partly paid for with markdowns in Nike's own channel. That is not decisive SHORT, because the premium newer models (Vomero Plus, Vomero Premium, Pegasus Plus 2) hold full price and Fleet Feet demand exceeds Nike's allocation.

Pre-registered rules scored: L1 FAILS (Pegasus 42 and Vomero 18 are not full price on nike.com or Running Warehouse); L2 FAILS (Running Warehouse markdown rate rising and double the store); L3 FAILS (competitors report full-price growth and a promotional market, not Nike pressure at full price); L4 UNRESOLVED (no 2026 run-specialty brand data found). S1 MET on nike.com and Running Warehouse, NOT MET at Fleet Feet, Foot Locker, Zappos. S2 MET. S3 PARTLY MET (Hoka and ASICS still grow; On blames promotions). S4 indirectly supported (Circana running ASP flat in H1 2026 while list prices rose).

## 2. New primary data gathered 2026-10-14

### 2a. Fleet Feet live catalogue (NEW, OPENED 2026-10-14)

Source: the public product search index that fleetfeet.com's own browse pages query (Typesense collection `fleetfeet_product_variants_v5`, search-only key embedded in the page HTML of https://www.fleetfeet.com/browse/shoes/mens?brand=nike, OPENED 2026-10-14). Fields used: price, original price, discounted flag, colourway inventory (units, chain-wide as reported by the index), 30-day and 7-day product page views. 13,849 unique shoe colourways for 8 brands. Data: `data/marketplace/fleetfeet_shoe_colorways_20261014.csv`; scripts `scripts/marketplace/ff_pull.py`, `ff_an.py`, `ff_models.py`. Only colourways with inventory above zero are counted.

| Brand | In-stock colourways | Share of colourways discounted | Avg depth when discounted | Units in stock | Share of units on discounted colourways |
|---|---|---|---|---|---|
| Brooks | 529 | 36.3% | 23.2% | 551,198 | 17.6% |
| HOKA | 698 | 25.9% | 22.5% | 231,110 | 3.4% |
| Saucony | 610 | 35.7% | 24.8% | 192,255 | 3.7% |
| ASICS | 396 | 24.2% | 22.2% | 159,720 | 4.0% |
| On | 445 | 28.8% | 24.8% | 92,478 | 7.8% |
| New Balance | 658 | 25.2% | 22.5% | 78,259 | 16.7% |
| **Nike** | 497 | **5.6%** | 21.7% | 28,958 | **3.9%** |
| adidas | 188 | 5.9% | 20.0% | 9,321 | 0.8% |

Demand vs supply at Fleet Feet [my arithmetic]: Nike is 6.0% of 30-day product views (5.9% of 7-day views) but 2.2% of in-stock units among these 8 brands, a views-to-inventory ratio of 2.78 (HOKA 1.42, ASICS 1.33, On 1.15, Brooks 0.53). Nike is under-allocated relative to shopper interest at Fleet Feet.

Current-generation model comparison at Fleet Feet (share of in-stock colourways discounted):

| Model | Colourways | Discounted | Units | 30-day views |
|---|---|---|---|---|
| Nike Pegasus 42 (launched Apr 9, 2026) | 26 | **30.8%** (23.7% of units), all at $108.97 vs $145 | 3,988 | 27,911 |
| Nike Vomero 18 | 43 | 0% | 2,564 | 45,454 |
| Nike Vomero Plus | 27 | 0% | 2,709 | 70,740 |
| Nike Pegasus Plus 2 (Aug 2026) | 16 | 0% | 1,823 | 31,683 |
| Nike Vomero Premium | 20 | 0% | 1,781 | 33,507 |
| HOKA Clifton 11 | 56 | 0% | 45,778 | 244,932 |
| HOKA Bondi 9 | 78 | 5.1% | 32,295 | 448,674 |
| ASICS Gel-Nimbus 28 | 60 | 0% | 45,849 | 164,569 |
| ASICS Novablast 6 | 31 | 0% | 17,697 | 143,516 |
| Brooks Ghost 18 | 46 | 0% | 24,136 | 232,275 |
| On Cloudmonster 3 | 36 | 19.4% | 12,878 | 65,776 |
| On Cloudsurfer Max | 34 | 61.8% | 8,743 | 70,699 |

Outgoing versions are 100% discounted for HOKA (Clifton 10, Arahi 8), ASICS (Novablast 5, GT-2000 14, Kayano 32) and Brooks (Adrenaline GTS 25, Glycerin Max 2). That is the normal run-specialty pattern: discount the old version, hold the current one. Among current flagships at Fleet Feet, only Nike Pegasus 42 and On's models break it.

Scale check [my arithmetic]: Nike's best Fleet Feet model by views (Vomero Plus, 70,740) has about one sixth of HOKA Bondi 9's views (448,674). Nike's run-specialty position is still small.

### 2b. Same SKU, Nike's own site vs Fleet Feet (NEW cross-match, OPENED)

Matched 131 Nike running colourway codes present in both the Fleet Feet index (Oct 14, 2026) and the nike.com product feed (repo `data/marketplace/nike_current_products.csv`, fetched Oct 13, 2026, OPENED (repo)). Examples:

| Code | Model | Fleet Feet price | nike.com price | Full price |
|---|---|---|---|---|
| HM6803-115 | Men's Vomero 18 | $155 | $108.97 | $155 |
| HM6803-021 | Men's Vomero 18 | $155 | $116.97 | $155 |
| HM6804-117 | Women's Vomero 18 | $155 | $116.97 | $155 |
| IB1873-105 | Men's Pegasus 42 | $145 | $97.97 | $145 |
| IB1873-005 | Men's Pegasus 42 (445 units at FF) | $145 | $102.97 | $145 |
| IB1881-501 | Women's Pegasus 42 (534 units at FF) | $145 | $94.97 | $145 |
| HJ1101-113 | Women's Structure 26 | $145 | $82.97 | $145 |
| HQ3049-114 | Women's Structure Plus | $170 | $128.97 | $170 |

Of the Vomero 18 colourways in both places, Fleet Feet holds full price on all of them, while nike.com discounts most of them by 10% to 30%. **The discounting is Nike's own, in its own channel, undercutting its specialty partner.** This matches DICK'S Q2 2026 call: "a number of brands got very promotional on their sites and those promotions spilled into the broader marketplace" (repo `research_notes/jordan_extracts/rabbit_hole/dicks.md`, VERIFIED by prior researcher).

nike.com current running models, share of colourways discounted (repo product feed, Oct 13, 2026, my arithmetic, deduplicated by style code): Pegasus 42 29 of 67 (43%, avg 22.8% off); Vomero 18 29 of 115 (25%, 18.4%); Structure 26 41%; Structure Plus 56%; Pegasus Premium 56%; Vomero Plus 12%; Pegasus Plus 0%; Vomero Premium 0%.

### 2c. Time to markdown: Pegasus 42 (2026) vs Pegasus 41 (2024) on nike.com

From repo `data/definitive/markdown/time_to_markdown_by_colorway.csv` (Wayback checks, OPENED (repo)): Pegasus 41 2024 colourways were discounted by day 180 in 3 of 12 cases (25%), and 0 of 14 by day 90; several stayed at full price past day 450 (e.g. FD2722-001 full price at day 491). Pegasus 42 (launch Apr 9, 2026, Fleet Feet post date Mar 10, 2026, so about day 188 to 218 on Oct 13): 16 of 38 listed colourways (42%) discounted, median depth 25% (repo `live_cohort_table_20261013.csv`). **Pegasus 42 is reaching markdown faster than Pegasus 41 did during the 2024 clean-up.** Caveat: different methods (Wayback windows vs a single live read), and Wayback samples are small. Nuance: Pegasus 42 MSRP is $145 vs $140 for most Pegasus 41, so a discounted Pegasus 42 ($102.97 to $108.97) still realises about $4 to $10 more than a discounted Pegasus 41 ($98.97).

### 2d. Running Warehouse over time (OPENED (repo); model detail is my new arithmetic)

| Snapshot | Nike share of men's road colourways on sale | Store average | HOKA | On |
|---|---|---|---|---|
| 2025-02-05 | 61.5% | 26.0% | 25.9% | 16.7% |
| 2025-09-11 | 25.4% | 18.4% | 21.1% | 8.8% |
| 2025-10-16 | 33.3% | 20.0% | 12.8% | 10.8% |
| 2026-04-26 | 35.7% | 17.4% | 15.9% | 26.5% |
| 2026-10-13 | **49.0%** | 23.3% | 9.5% | 12.5% |

Year on year (Oct 2025 to Oct 2026): Nike +15.7 pp, store +3.3 pp, HOKA -3.3 pp. Nike's gap to the store widened from 13.3 pp to 25.7 pp. Nike's colourway share of the page fell from 10.6% to 9.6% while its colourway count rose 87 to 98 [my arithmetic].

Model level, Oct 13, 2026, men's plus women's road (repo `runningwarehouse_items.csv`, my arithmetic): Pegasus 42 10 of 28 colourways on clearance (36%, 24% off); Vomero 18 17 of 26 (65%, 26% off); Pegasus Premium 19 of 27 (70%, 35% off); Structure Plus 9 of 14; Vaporfly 4 8 of 11. Competitor current models on the same page: HOKA Clifton 11 0 of 22, Bondi 9 2 of 38, ASICS Nimbus 28 0 of 33, Novablast 6 0 of 23, Brooks Ghost 18 0 of 23, Saucony Ride 19 0 of 30; their outgoing versions (Novablast 5, Adrenaline GTS 25, Triumph 23, Endorphin Speed 5) are 100% on sale.

Archived Running Warehouse pages could not be re-fetched for model-level history: web.archive.org connections were reset by the network on Oct 14, 2026 (archive.org availability API worked and showed the earliest men's road capture is Feb 5, 2025, already in the repo).

### 2e. Other retailers (OPENED 2026-10-14 unless noted)

- Zappos search pages for "nike-pegasus-42" and "nike-vomero-18" (OPENED): 8 Pegasus 42 listings, 1 at 10% off, rest full price; 5 Vomero 18 listings, all at or within 1% of full price.
- Foot Locker sale pages (OPENED (repo), Oct 13, 2026): only 2 Vomero 18 listings on sale (Vomero 18 RR men's $119.99, boys' $94.99); no Pegasus 42 on sale; HOKA's sale items are outgoing Clifton 10.
- Amazon and DICK'S returned 503 and 403 to direct requests; not measured.

### 2f. Competitor results and commentary

- **Deckers (HOKA), quarter to Jun 30, 2026** (10-Q filed Jul 30, 2026, sec.gov, OPENED): HOKA wholesale $446.8M, +2.9%; HOKA DTC $256.8M, +17.3%; HOKA total $703.5M, +7.7%. Gross margin 56.4% vs 55.8%, helped by "full-price selling primarily for the UGG brand ... and better management of product close-outs". Earnings release (Jul 23, 2026, sec.gov, OPENED): HOKA FY27 still "low-double-digit" growth. Call (MarketBeat transcript, OPENED): "HOKA and UGG each delivered healthy first quarter growth and full price unit sell-through in the U.S. market"; wholesale growth "driven by the U.S. market, which delivered higher sell-in" and a "strong increase in full price sell-through"; "we continue to maintain or gain share in performance run and trail ... we've gained share above $120". Read: HOKA's U.S. business is not being taken at full price by Nike; HOKA wholesale slowed (management says international timing).
- **On, Q2 2026** (call Aug 11, 2026, Investing.com transcript, OPENED): "the sell-out of some of our everyday running franchises tracked below our ambitions"; "With sellouts softer in some of our everyday running franchises in a highly promotional environment"; "a highly competitive environment where many brands resorted to promotions ... despite our choosing not to participate in promotional activity"; held back U.S. wholesale sell-in "to protect our full price strategy". On did not name Nike. Read: someone is buying everyday-running share with promotions in U.S. wholesale; Nike (Pegasus 42, Vomero 18 at Running Warehouse and nike.com) fits, but so may others, and On's own models are discounted at Fleet Feet.
- **ASICS, Q2 2026** (SGB Executive, Aug 14, 2026, OPENED; figures attributed to ASICS filings): North America sales ¥46,543M, +33.8%; Run Specialty channel +14.2% across North America; U.S. wholesale +36.6%. ASICS run specialty grew in line with the category, so no sign of share loss to Nike there.
- **Circana via SGB Executive** (Aug 17, 2026, OPENED): U.S. running footwear H1 2026 +13% in dollars and +13% in units; total footwear +1% "elevated by higher average prices that offset unit declines". Running average price therefore about flat [my inference] even though brands raised list prices in 2025 to 2026 (Nike Vomero 18 new colourways $165 vs $155; Pegasus 42 $145 vs $140). Flat price with rising list prices implies more discounting or mix to cheaper shoes in running.
- **YipitData blog** (April 2026, OPENED): in 2025 "Nike's share declined across both in-store and online channels"; "Nike, Adidas, and New Balance increased discounting levels in 2025"; On kept lower discount rates. Covers 2025, not 2026.
- **Nike Q1 FY27 call** (Oct 2026, official transcript PDF on s1.q4cdn.com, OPENED): "Running is up double digits again with consistent share gains"; Vomero "nearly tripled our share of the Max cushioning category over the past year"; gross margin "partially offset by increased discounts as well as channel mix"; CFO: "we are taking discounts and resetting the marketplace, which is dampening gross margins". Nike gives no running full-price or margin figure. "Double digits" vs a U.S. category growing 13% is not evidence of a large share gain.
- **Run-specialty brand data (Karnan/Circana)**: latest found is 12 months to Sep 2025 (Nike +35.4%, On -19.7%, HOKA -7.4%; SGB Dec 3, 2025, OPENED (repo)). No 2026 update found (searched SGB, Running Insight, RIA; SNIPPET only). Brooks claims No. 1 in U.S. specialty for six straight months with 14% growth (Aug 12, 2026, SNIPPET).

## 3. Alternative explanations tested

1. **"Nike always clears old colourways mid-life; this is normal cadence."** Mostly ruled out. Pegasus 41 in 2024 was discounted in 25% of colourways by day 180; Pegasus 42 is at 42% around day 190 to 218. HOKA, ASICS and Brooks keep current versions at 0% to 5% discounted at both Fleet Feet and Running Warehouse. Remains partly open because the Pegasus 41 sample is small (12 colourways with a day-180 read).
2. **"It is Running Warehouse only (retailer-specific overbuy)."** Ruled out as the whole story: nike.com discounts the same models (Pegasus 42 43%, Vomero 18 25%). But it is not market-wide either: Fleet Feet, Zappos and Foot Locker hold Nike running at or near full price. The discounting sits in Nike's own channel and in online specialty clearance.
3. **"A Pegasus 43 changeover is imminent, so Pegasus 42 clearance is normal."** Not supported: Running Warehouse flags new Pegasus 42 colourways as "New" at full price on Oct 13, 2026, and Fleet Feet posted Pegasus 42 in March 2026. Only a reseller blog claims a Pegasus 43 (SNIPPET, unreliable). Remains open until Nike's spring 2027 running calendar is known (Investor Day, Nov 16 to 17).
4. **"Discounts are market-wide, so Nike is not buying share."** Partly survives: On, DICK'S and Circana all describe a promotional running market, and On's own models are discounted at Fleet Feet. But HOKA and ASICS report full-price U.S. sell-through and hold current models at full price, so Nike is among the brands promoting, not a bystander.
5. **"Nike's discounting is in old lifestyle product, not running."** Ruled out for running specifically: running is 36.8% of colourways discounted on nike.com (repo franchise table, Oct 13, 2026), and current running flagships are discounted in Nike's own channel.
6. **"Tariff list-price increases mean discounted shoes still realise more."** Small effect: a discounted Pegasus 42 ($102.97 to $108.97) realises $4 to $10 more than a discounted Pegasus 41 ($98.97), but about $36 to $42 below the $145 full price.

## 4. What is still unknown and what would settle it

- Nike's running revenue split by full price vs markdown and by channel (not disclosed). Ask at Investor Day.
- 2026 run-specialty brand share and average price (Karnan/Circana data presented at The Running Event, early Dec 2026). LONG if Nike's run-specialty dollars grow with average price flat or up; SHORT if Nike unit share rises while its average price falls.
- A second Fleet Feet read in 4 to 8 weeks with the same scripts (does Pegasus 42 discounting spread to Vomero 18 at Fleet Feet; does Nike's views share hold).
- Nike Q2 FY27 (Dec 2026) 10-Q: footwear ASP line and whether "higher discounts" is again cited, plus any running comment on full price.
- Running Warehouse after holiday 2026 (Jan 2027): Nike markdown rate below 30% would weaken the SHORT read.

## 5. Source list

| # | Source | Date | Status |
|---|---|---|---|
| 1 | Fleet Feet product search index used by fleetfeet.com browse pages (13,849 shoe colourways) | 2026-10-14 | OPENED |
| 2 | nike.com product feed, repo `data/marketplace/nike_current_products.csv` | 2026-10-13 | OPENED (repo) |
| 3 | Running Warehouse items and history, repo `data/marketplace/runningwarehouse_items.csv`, `runningwarehouse_history.csv` | 2025-02 to 2026-10-13 | OPENED (repo) |
| 4 | Nike time-to-markdown and live cohort tables, repo `data/definitive/markdown/` | 2026-10-13 | OPENED (repo) |
| 5 | Deckers 10-Q for quarter ended Jun 30, 2026, sec.gov 0000910521-26-000022 | 2026-07-30 | OPENED |
| 6 | Deckers Q1 FY27 earnings release, sec.gov 0000910521-26-000015 Ex. 99.1 | 2026-07-23 | OPENED |
| 7 | Deckers Q1 FY27 call transcript, marketbeat.com | 2026-07-23 | OPENED |
| 8 | On Q2 2026 call transcript, investing.com | 2026-08-11 | OPENED |
| 9 | SGB Executive, ASICS North America Q2 2026 | 2026-08-14 | OPENED |
| 10 | SGB Executive, Circana running H1 2026 | 2026-08-17 | OPENED |
| 11 | YipitData blog, footwear market trends 2025 | 2026-04 | OPENED |
| 12 | Nike Q1 FY27 official transcript, s1.q4cdn.com | 2026-10 | OPENED |
| 13 | Zappos search pages, Pegasus 42 and Vomero 18 | 2026-10-14 | OPENED |
| 14 | Foot Locker sale items, repo `data/marketplace/footlocker_sale_items.csv` | 2026-10-13 | OPENED (repo) |
| 15 | DICK'S Q2 2026 10-Q and call quotes, repo `research_notes/jordan_extracts/rabbit_hole/dicks.md` | 2026-08 | OPENED (repo) |
| 16 | SGB, Karnan/Circana run specialty 12 months to Sep 2025 | 2025-12-03 | OPENED (repo) |
| 17 | Brooks specialty No. 1 claim; Pegasus 43 reseller blog; WWD On vs Nike (paywalled) | 2026 | SNIPPET |
| 18 | web.archive.org (connection reset, not reachable on 2026-10-14) | 2026-10-14 | FAILED |

## Skeptic review (2026-10-14, independent re-check)

**Verdict: holds. SHORT, moderate, and the nike.com discount evidence is stronger than stated above.** The investigator understated discounting on Nike's own site, but overstated what Fleet Feet's clean shelf proves.

### Numbers re-checked at source

1. **Fleet Feet (CSV re-run, OPENED in repo).** Pegasus 42 (any title containing it, in stock): 8 of 30 colourways discounted ($108.97 or $108.75 vs $145), 944 of 4,187 units (23%). Vomero 18 0 of 48. Vomero Plus, Pegasus Plus 2, Structure 26 and Pegasus Premium all 0%. Matches the note (26 vs 30 colourways depends on whether SE and other variants are counted).
2. **nike.com Vomero 18 figure is wrong, and it understates the discounting.** The "29 of 115 (25%)" figure counts about 70 NFL team, college, By You and GORE-TEX listings that are never discounted. The repo feed (2026-10-13) for the core inline adult shoe titled exactly "Nike Vomero 18" shows **27 of 44 colourways discounted (61%)**. For "Nike Pegasus 42" the same count is **25 of 48 (52%)**, not 43%. [my arithmetic, OPENED (repo)]
3. **Live re-pull of nike.com, 2026-10-14 (NEW, OPENED).** I read the search pages for "pegasus 42" and "vomero 18" (the page's embedded product data), excluding kids, By You and GORE-TEX. Pegasus 42 was **25 of 46 discounted (54%)**, average 23% off. Vomero 18 was **26 of 41 (63%)**, average 18% off. Vomero Plus was 5 of 32 (16%). Six discounted Pegasus 42 colourways carry Nike's own "Best Seller" badge, for example IB1873-105 at $97.97 vs $145 (32% off) and IB1873-005 at $102.97. **So the discounts are not limited to unpopular colours.** Big Kids' Pegasus 42 is mostly at $65.97 vs $112 (41% off). Saved to `data/marketplace/nike_search_pegasus42_vomero18_20261014.txt`.
4. **Pegasus 41 control (repo `time_to_markdown_by_colorway.csv`, OPENED (repo)).** Of 15 Pegasus 41 colourways from 2024, 9 had a Wayback capture at full price after day 214. Several were still at full price on days 469 to 539 (FD2722-001, -002, -102, FD2723-001, -002, -102). Pegasus 42 is at 52% to 54% discounted around day 190. The comparison is a stronger contrast than the note's 25% vs 42%. One caveat: Pegasus 42's age is measured from the model launch, and many colourways launched later, so colourway-level ages are younger. That makes Pegasus 42 look faster, not slower.

### Data the investigator missed that points the other way, or weakens their evidence

- **Fleet Feet's clean Nike shelf is new pipeline fill, not proof of sell-through.** Nike and Fleet Feet announced a nationwide vendor partnership on Apr 7, 2026. It moved Nike from select doors to a rollout across more than 285 stores, launched alongside the Pegasus 42 on Apr 9, 2026 (Footwear Magazine, published 2026-04-08 and updated 2026-10-03, OPENED). Stock that arrived recently, in new doors, is expected to be at full price. Shipments into those doors also lift Nike's reported wholesale running growth with sell-in, not consumer demand. Even so, **Pegasus 42 is already 27% to 31% discounted at Fleet Feet**, the new partner, within 6 months. This weakens Fleet Feet as LONG evidence.
- **Vomero 18 is an older model than the competitor comparisons assume.** Vomero 18 launched on Feb 27, 2025 (Complex, SNIPPET), so it is about 20 months old, while Clifton 11, Nimbus 28 and Ghost 18 are newer. Some Vomero 18 clearance on nike.com may be end of life, and a Vomero 19 is rumoured (Sundried review page, SNIPPET, unreliable). This is the best alternative explanation the investigator did not test, and it **partly survives for Vomero 18**. Three things argue against it: Nike is still adding new Vomero 18 colourways at $165, Fleet Feet holds all 48 Vomero 18 colourways at full price, and Nike has announced no successor. It **does not apply to Pegasus 42** (6 months old, still getting "Just In" colourways), and Pegasus 42 is the clean test.
- **LONG evidence that survives:** Nike gets 6.0% of Fleet Feet views on 2.2% of its units (ratio 2.78). Nike's premium running models (Vomero Plus 16% discounted on nike.com, Vomero Premium and Pegasus Plus 0%) hold price. Karnan put Nike's 2025 independent run-specialty sales at +35% (Running Insight, 2026-01-20, OPENED). These show real demand at the premium end of Nike's range, which is a small part of its running volume.
- **Nike's own filing agrees with SHORT.** NIKE Brand footwear in Q1 FY27 had units -5% and ASP -1 point on "channel mix and higher discounts". North America footwear pairs were +2% at a lower ASP (Q1 FY27 10-Q pp. 23 and 26, OPENED (repo) `data/discount/units_vs_asp.csv`). Growth in North America, where running is the stated driver, came with lower prices, not higher ones.
- Not found: any 2026 Nike-specific run-specialty share or average-price figure. Searches of Running Insight, SGB and Circana-via-press returned only 2025 data (SNIPPET).

### Alternatives after review

- "Only unpopular colourways are discounted": ruled out. Best Seller-badged Pegasus 42 colourways are 25% to 32% off on nike.com.
- "Vomero 18 is in end-of-life clearance": partly open. Settle it with Nike's spring 2027 calendar (Investor Day) or a Vomero 19 announcement.
- "The Fleet Feet full-price shelf shows healthy demand": weakened. The stock is weeks to months old after a rollout, and Pegasus 42 is already discounted there.

### Skeptic bottom line

The core claim survives at the source and gets stronger. More than half of Nike's two volume running shoes are discounted in its own channel, faster than in 2024. Nike's filing reports lower footwear ASP on higher discounts, and Circana shows running unit and dollar growth equal (flat ASP). Strength stays **moderate** rather than strong for three reasons: Nike does not disclose running price or margin data, the Vomero 18 age caveat is real, and premium Vomero and Pegasus Plus hold price. Sources added: nike.com search pages (2026-10-14, OPENED); Footwear Magazine on the Fleet Feet partnership (2026-10-03 update, OPENED); Running Insight (2026-01-20, OPENED); Complex on the Vomero 18 launch date (SNIPPET); Sundried on Vomero 19 (SNIPPET).
