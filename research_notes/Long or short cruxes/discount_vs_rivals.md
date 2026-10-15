# Crux: Is Nike's discounting worse than rivals, and is the shoe-retailer margin squeeze Nike's doing?

Prepared 2026-10-14. Rescues two failed tests from the earlier hunts (`data/hunt/pricing_catalog/`, `data/hunt/macro_category/`). Labels: OPENED = fetched and read in this session (page, SEC data API or live page). SNIPPET = search-result summary only. [my arithmetic] = computed from files in `data/hunt/discount_vs_rivals/`. Route log, caveats and scripts: `data/hunt/discount_vs_rivals/README.md`.

## 0. Stated in advance (before any new data)

- SHORT if Nike's discount depth or incidence rises faster than adidas, Hoka, On, ASICS on the same shelves, with retailer margins at lows during Nike's wholesale surge (+9% North America in Q1 FY27).
- LONG if Nike improves relative to those rivals.
- Standing repo rule: no "inconclusive" before five genuinely different routes. Routes tried: 6 produced usable data (PPI decomposition, SEC retailer margins, Zappos live, Foot Locker live, 25-store Shopify panel, Germany Common Crawl panel) plus brand commentary; 8 were blocked or too thin (adidas UK/JP/CA/AU, Wayback, Keepa/Amazon, eBay, off-price sites, Dick's/Finish Line/Hibbett, Zappos Common Crawl).

## 1. Verdict

**NEUTRAL on "Nike discounts worse than rivals" (strength: moderate; was weak SHORT). The margin squeeze at shoe retailers is real and footwear-specific, but it cannot be pinned on Nike's wholesale surge from the data (attribution: weak).**

Neither stated rule is met. Nike's discount incidence on third-party shelves is not rising faster than adidas's, and it is not improving relative to the share gainers either. What the new data adds:

1. Nike is not the most discounted brand on the shelves we can measure. adidas and ASICS are far more discounted at Zappos, adidas.com and adidas.de; Nike is level with adidas at Foot Locker and on Shopify partner stores.
2. Nike is more discounted than On and (on most shelves) Hoka, the two share gainers. That is the part that stays SHORT-leaning: the brands that are winning are not discounting, and the brands that are losing or flat (Nike, adidas-in-US, ASICS) are.
3. The PPI shoe-store margin collapse (-39% YoY) is footwear-only (clothing stores +2.1%, sporting goods stores +0.1%), but its timing does not line up with Nike's wholesale growth, and the retailers' own commentary says "industry inventory" and Foot Locker's legacy-silhouette exposure, not Nike alone.

## 2. Pre-stated rules against the evidence

| Rule | Evidence | Result |
|---|---|---|
| SHORT: Nike depth/incidence rising faster than adidas on same shelves | US: nike.com +4.6 pts vs adidas.com +12.7 pts (Aug to Sep 2025 to 2026; earlier pricing hunt, DiD -8.2, CI -13.3 to -3.3). Germany (new): Nike +2.5 pts vs adidas -10.8 pts all categories (DiD +13.3, CI +7.2 to +19.5) but footwear Nike +4.3 vs adidas +4.5 (DiD -0.2, CI -10.3 to +9.5) | NOT MET (US) / mixed (DE) |
| SHORT: Nike rising faster than Hoka, On, ASICS on same shelves | Only snapshots exist for these brands (no time series); Nike above On and Hoka at Foot Locker and on Shopify partners, level at Zappos | Cannot test "rising faster"; level is above On, near Hoka |
| SHORT: retailer margins at lows | PPI shoe-store margin index at series low (91.2, Aug 2026); reported gross margins mixed (Section 5) | MET for the PPI, mixed for reported margins |
| SHORT: lows coincide with Nike wholesale surge | Index fell hardest (YoY -8%, -23%, -39%) in the three quarters when Nike total wholesale growth was +5%, +4%, -1%; correlation of index level with wholesale growth over 9 quarters 0.02 [my arithmetic] | NOT MET (timing is the wrong way round) |
| LONG: Nike improving relative to rivals | Nike not improving in any measured pair | NOT MET |

## 3. Same-shelf discount panel, 2026-10-14 snapshot (new)

Share of listed styles with a price below list. Bootstrap 95% intervals resample styles (they do not capture which styles the retailer chose to show).

| Brand | Zappos (n styles, share, CI) | Foot Locker (n, share) | Shopify partners, 25 stores, markdown 10%+ share (n) | Shopify, products under 6 months old |
|---|---|---|---|---|
| Nike | 203, 24.6% (18.7 to 30.5) | 99, 33.3% | 22.9% (6,707) | 15.4% |
| Jordan | not listed | 113, 30.1% | 34.0% (2,465) | 19.4% |
| adidas | 251, 59.0% (53.0 to 64.9) | 114, 31.6% | 17.9% (3,139) | 9.5% |
| HOKA | 95, 20.0% (12.6 to 28.4) | 101, 22.8% | 18.5% (798) | 12.9% |
| On | 101, 17.8% (10.9 to 25.7) | 99, 19.2% | 6.5% (1,078) | 1.5% |
| ASICS | 161, 60.2% (52.8 to 67.7) | 100, 10.0% | 25.2% (1,478) | 22.0% |
| New Balance | 222, 45.0% (38.3 to 51.4) | 108, 33.3% | 21.0% (2,037) | 7.0% |
| Saucony | 128, 25.0% | 48, 33.3% | not reported | |
| Brooks | 76, 35.5% | 81, 11.1% | not reported | |

Differences with intervals:
- Zappos, Nike minus: adidas -34.3 pts (CI -43.0 to -25.8); ASICS -35.6 (-45.9 to -26.5); New Balance -20.4 (-29.3 to -12.1); Hoka +4.6 (-5.6 to +13.9); On +6.8 (-2.6 to +16.2); Brooks -10.9 (-23.1 to +1.4); Saucony -0.4 (-9.7 to +9.0). Mean depth when discounted: Nike 20.7%, adidas 16.9%, Hoka 24.3%, On 22.0%. Running shoes only: Nike 24.0% (n 100), adidas 56.0%, ASICS 53.0%, Hoka 24.7%, On 22.4%.
- Shopify, 25 stores, linear probability model with store and age fixed effects, store-clustered errors: Nike +2.6 pts vs adidas (SE 6.2); On -9.7 (SE 6.0); Hoka -3.2 (6.1); ASICS +5.7 (5.4); New Balance +5.1 (5.4); Jordan +10.0 (9.3). The 16-store estimate in the earlier hunt was Nike +9.7 (SE 7.9); adding 9 stores (Stadium Goods reports no compare-at prices) shrinks it. Nike-adidas is not distinguishable from zero.
- Foot Locker: Nike 33.3% (CI 24.2 to 42.4) vs adidas 31.6% (22.8 to 40.4), Hoka 22.8%, On 19.2%, ASICS 10.0%, Brooks 11.1%. First-page samples only (48 items per page, relevance order), so treat as indicative. Nike supplies 30 of the 96 styles on the first page of Foot Locker's men's and women's shoe sale walls (17 of 48 men's, 13 of 48 women's); Nike's brand page lists 4,948 items vs adidas 1,664 and Hoka 184.

Germany, Common Crawl product pages (`cc_intl_de_panel.csv`, about 400 random pages per brand and crawl; adidas.de 2024 pages carry no price, so adidas has 2025 and 2026 only):

| Crawl month | Nike nike.com/de | adidas.de |
|---|---|---|
| Aug 2024 | 14.2% (n 226) | no price |
| Sep 2024 | 14.3% (n 223) | no price |
| Aug 2025 | 20.4% (n 269) | 55.9% (n 399) |
| Sep 2025 | 8.5% (n 378) | 63.7% (n 400) |
| Aug 2026 | 16.0% (n 400) | 48.2% (n 400) |
| Sep 2026 | 15.3% (n 398) | 49.8% (n 400) |

Nike Germany is flat at 14% to 16% over two years and far below adidas at every date. The Aug to Sep 2025 to 2026 difference-in-differences (+13.3 pts, CI +7.2 to +19.5, all categories) leans on the single low Nike reading in Sep 2025 (8.5%); footwear alone gives zero. Four crawl-months per brand is too few for crawl-clustered intervals.

Reading: on the shelves that could be measured, Nike's third-party discounting is not unusual versus adidas or the market. Nike holds retail prices at wholesale accounts (nike.com flags 9,435 of 32,225 live colourways as PROMOS_EXCLUDED; Foot Locker flags Nike items as promo-code excluded least often at 49.5%, but that is a different flag), and the deeper discounting sits on nike.com itself (footwear 43.1%, depth 29.1% on 2026-10-14, pricing hunt) and in wholesale terms that never show as a shelf price. That is a limit of every shelf-price route, and is why this verdict is NEUTRAL, not LONG.

## 4. Decomposing the BLS shoe-store margin index

FRED series pulled today (OPENED, fredgraph.csv, 2026-10-14), PPI retail trade margins, 3-month average Jun to Aug 2026 vs Jun to Aug 2025 [my arithmetic]:

| Series | Jun to Aug 2026 | YoY | Percentile of latest value in own history |
|---|---|---|---|
| Shoe stores 448210 | 92.9 (2025: 152.3) | **-39.0%** | 0th (series low, Aug 2026 91.2; series starts 2002) |
| All shoe stores 4482 | 91.0 (2025: 149.3) | -39.0% | 0th |
| Clothing stores 4481 | 142.3 | +2.1% | 87th |
| Sporting goods stores 451110 | 182.4 | +0.1% | 97th |
| Sporting goods, hobby, musical 4511 | 137.5 | +0.8% | 96th |
| Hobby, toy, game stores 451120 | 89.8 | +2.9% | 27th |
| Jewelry stores 448310 | 269.4 | +10.5% | 100th |
| Footwear manufacturing PPI 316210 (cost side) | 149.5 | +3.3% | 100th |

- The shoe-store index is the only one of ten retail margin indexes that fell. The 3-month YoY of -39% is 8.3 historical standard deviations below zero (SD 4.7 points of YoY outside the last year); the previous worst 3-month YoY was -9.8% (Dec 2024). The index is volatile month to month (it swung 147.8 to 129.5 in Aug to Oct 2024), but this is a step down that has not reversed: Mar 2026 129.3, Apr 100.3, May 99.0, Jun 93.3, Jul 94.1, Aug 91.2.
- Footwear-specific, not sector-wide: clothing stores and sporting goods stores (Dick's, Academy, Hibbett are NAICS 451110) show flat margins in the same months. Footwear manufacturers' prices rose 3.3%, so shoe stores are not passing the cost increase through (a squeeze, not a cost decline).
- Nike wholesale link, by Nike fiscal quarter (`ppi_by_nike_fiscal_quarter.csv`): index YoY Q1 FY26 +14.9%, Q2 FY26 +8.1%, Q3 FY26 -8.0%, Q4 FY26 -22.8%, Q1 FY27 -39.0%. Nike total wholesale growth +7%, +8%, +5%, +4%, -1% (repo `nike_standing.md`). The index was highest when Nike wholesale growth was highest (Q1 and Q2 FY26) and fell furthest as wholesale growth faded. Correlation of level with wholesale growth over the nine quarters from Q1 FY25: 0.02. The index is not evidence that "Nike stock pushed through retailers at lower retailer margin" in the +9% NA quarter. It is consistent with a lagged effect (Nike's oversupply of retro, then clearance a few quarters later) but nine quarters cannot show a lag.
- Not proven to be a clean margin: the PPI margin is margin per unit of trade service, not a gross margin percentage (macro hunt caveat), and reported margins disagree (next section).

## 5. Reported retailer margins and commentary

SEC XBRL gross margin (OPENED, data.sec.gov company facts; `retailer_gross_margin_yoy_bps.csv`), quarter ended Aug 1, 2026 vs Aug 2, 2025:

| Retailer | Gross margin | YoY | Note |
|---|---|---|---|
| Shoe Station Group (formerly Shoe Carnival) | 31.87% | **-691 bps** | revenue $284.3M, -7.2%; 10-Q filed 2026-09-10. Management (SNIPPET): heavier promotions, liquidation of aged and excess inventory; merchandise margin 630 bps of the drop |
| Dick's consolidated | 34.78% GAAP, 34.06% adjusted | -228 bps GAAP, -300 bps adjusted | Foot Locker mix (OPENED, 8-K Ex. 99.1) |
| Dick's core business segment | 37.8% | +79 bps | $1,457.0M on $3,849.9M [my arithmetic from the segment table] |
| Foot Locker segment | 25.7% | about -166 bps vs Foot Locker's own 27.4% in the quarter ended Aug 2, 2025 | segment loss $31.9M; FY26 outlook cut from +$110M to $150M profit to a $40M to $80M loss |
| Academy Sports | 40.42% | +437 bps | tariff-refund affected (SNIPPET) |
| Genesco | 51.36% | +558 bps GAAP (adjusted +140 bps) | refund-affected |
| Caleres | 54.78% GAAP (adjusted 46.8%) | +1,138 bps GAAP (adjusted +340 bps) | refund-affected; Famous Footwear segment 42.7%, -100 bps (SNIPPET) |

Dick's booked $38.1M of tariff refunds for prior-year costs in the quarter (OPENED, 8-K Ex. 99.1), so GAAP margins for the whole group are lifted by a one-time item. Strip it out and the two clean readings both fall: Shoe Station and Foot Locker, the retailers most reliant on athletic launch and retro product. The retailers with a fashion or family mix (Caleres, Genesco) or a broad sporting goods mix (Academy, Dick's core) did not show it. That cross-section fits "footwear squeeze concentrated in Nike-heavy specialty doors" and is the only piece of evidence that links the PPI to Nike's mix, but it is two retailers.

Commentary (all dates 2026):
- Dick's Q2 call, Sep 2026 (OPENED, Webull transcript, automated): Ed Stack: "inventory levels were building up across parts of the industry, leading to a much more promotional environment"; "I've never seen the specialty channel of distribution so promotional in my career" (relayed from a brand executive); "So we're not leading this margin erosion"; "the margin pressure on Foot Locker is much greater than Dick's". Release: conditions "became increasingly promotional, and we took action to remain competitively priced"; Foot Locker comps -3.6% pro forma, tied (SNIPPET) to "greater exposure to legacy footwear silhouettes and greater dependence on footwear launch and retro product". Opinion, labelled as such. Stack also says Nike's Vomero and Peg "have done extremely well", so the promotion is not all Nike.
- Nike Q1 FY27 call, 2026-10-01 (OPENED, Webull transcript): David Denton: gross margin 42.8%, up 60 bps, "partially offset by increased discounts as well as channel mix"; "we are taking discounts and resetting the marketplace, which is dampening gross margins over time". Elliott Hill: "we proactively work with our wholesale partners to work through excess inventory"; "we've been oversupplying our iconic retro product, asking them to do too much"; Dunk revenue cut "nearly 50% in the quarter". This is Nike's own admission that retail partners carry its excess retro, which is the mechanism behind the Foot Locker comment, and is the strongest Nike-specific link in this note (opinion/management statement, not a measurement).
- adidas Q2 2026, late Jul 2026 (OPENED, World Footwear): gross margin 52.5%, +80 bps on "strong full-price sales and a favourable channel mix"; North America +17% currency-neutral; "cautious approach to wholesale sell-in" in "a promotional marketplace, particularly in Europe".
- On Q2 2026, 2026-08-11 (SNIPPET): gross margin 65.4% vs 61.5%, credited to DTC mix and "full-price discipline", excluding tariff refunds.
- Deckers Q1 FY27, 2026-07-23 (SNIPPET): "Our full price sell-through continues to be strong"; inventories down 5%; no significant change in promotional cadence assumed.
- Rival gross margins rose on full-price selling (adidas +80 bps, On +390 bps); Nike's rose 60 bps with discounts named as an offset. This is the cleanest Nike-specific signal in the commentary, and it matches the SHORT-leaning point 2 in the verdict.
- Vertical Knowledge via Reuters and Complex, 2024-02-02 (OPENED): about 44% of Nike sneakers at chain retailers on sale in 2024 vs 19.4% in Q1 2022, "more Nike sneakers ... at a discount ... than Hoka, Adidas, On, or Puma"; "small data sample". Different date and method; no 2026 equivalent is free.

## 6. What was ruled out, and what could not be tested

| Alternative explanation for the PPI drop | Test | Result |
|---|---|---|
| All retail margins fell (macro) | Nine other PPI retail margin indexes | Ruled out: clothing +2.1%, sporting goods +0.1%, jewelry +10.5% |
| Footwear cost inflation squeezed margin | Footwear manufacturing PPI | Partly: costs +3.3% while store margin index -39%, so the index fell far more than cost; margin per unit of service, not the same as percent margin |
| Nike +9% NA wholesale sell-in causes it | Timing by Nike fiscal quarter | Not supported: index kept falling as Nike wholesale growth faded (correlation 0.02, n 9); lag not testable |
| Tariff-refund timing | Dick's $38.1M, Caleres, Genesco, Academy jumps | Distorts reported margins upward; does not explain a fall |
| Foot Locker acquisition mix | Dick's segment table | Explains the Dick's consolidated drop, not Shoe Station or the PPI |
| Nike alone vs whole athletic market | Zappos, Foot Locker, Shopify, Germany | adidas and ASICS discount more than Nike on most shelves; Nike above On and Hoka |

Could not test: Hoka, On, ASICS discount trends over time on the same shelves (no time series, adidas UK/JP/CA/AU blocked, Wayback blocked, Keepa/Amazon need an account or are bot-blocked); off-price (TJX, Ross, Burlington, Rack, Saks Off 5th) share of Nike goods and Nike factory-store sale intensity (sites serve bot challenges, 2026 commentary on Nike not found); eBay new-with-tags supply (403). Wholesale terms (markdown allowances, returns, rebates) are invisible to shelf prices.

## 7. What changes on the scoreboard (Q4)

- Keep: "Nike's own discounting has not improved" (nike.com 30.5% to 31.0%, 37% in Aug to Sep 2026; Nike's own "increased discounts") as SHORT, moderate.
- Change: the sub-question "is it worse than rivals" moves from weak SHORT to **NEUTRAL, moderate** (Nike is below adidas, ASICS and New Balance on most shelves, near Foot Locker adidas, above On and Hoka).
- Add as SHORT-leaning, moderate: the share gainers (On, Hoka, and adidas on gross margin) are growing without discounting, while Nike's margin gain is offset by discounts; and Nike-heavy specialty doors (Shoe Station, Foot Locker) show falling margins with Nike naming retro oversupply.
- Do not use the PPI index as evidence of channel stuffing in the pitch; use it only as "footwear stores' margin per unit is at a 24-year low while apparel and sporting goods stores are flat".

## 8. Skeptic

1. Snapshot data (Zappos, Foot Locker, Shopify) cannot show direction; only the nike.com, adidas.com and Germany crawl panels can.
2. Zappos and Foot Locker listings are relevance-sorted and capped; Nike's wide assortment (4,948 items at Foot Locker) is sampled more thinly than Hoka's 184.
3. A low shelf markdown for Nike can mean Nike enforces price floors at accounts while paying for markdowns through allowances (hidden, which bears on margin, not on the shelf).
4. Germany is Europe: Nike EMEA revenue was -5% in Q1 FY27, so the country sites are not the US business.
5. Reported retailer margins include one-time tariff refunds and acquisition mix, so only Shoe Station and the Foot Locker segment are close to clean, and the Shoe Station management explanation is SNIPPET only.
6. Common Crawl panels are not random draws of the live catalog.

## 9. Sources

| Source | Date | Status |
|---|---|---|
| FRED fredgraph.csv, series PCU448210448210, PCU44824482, PCU44814481, PCU451110451110, PCU45114511, PCU451120451120, PCU448310448310, PCU316210316210 (`raw/fred/`, `macro_category/raw/`) | pulled 2026-10-14, data to Aug 2026 | OPENED |
| SEC XBRL company facts, data.sec.gov (Dick's 1089063, Foot Locker 850209, Academy 1817358, Genesco 18498, Caleres 14707, Shoe Carnival 895447); Shoe Carnival 10-Q accession 0001193125-26-387855 | filed 2026-09-10 (others 2026-09-03 to 09-10) | OPENED |
| Dick's Q2 FY26 earnings release, 8-K Ex. 99.1, sec.gov/Archives/edgar/data/0001089063/000108906326000033/dks-2026801xex991earningsr.htm | Aug/Sep 2026 | OPENED |
| Dick's Q2 2026 call transcript, webull.com/news/15463631008252928 | Sep 2026 | OPENED (automated transcript) |
| Nike Q1 FY27 call transcript, webull.com/news/15677874570593280 | 2026-10-01 | OPENED (automated transcript) |
| adidas Q2 2026 report, worldfootwear.com/news/adidas-delivers-record-secondquarter-revenue/11684.html | Jul 2026 | OPENED |
| Complex, "Twice As Many Nikes Are Going on Sale Than in 2022" (Vertical Knowledge via Reuters) | 2024-02-02 | OPENED |
| Shoe Station Group Q2 2026 release (businesswire.com/news/home/20260910114887) and FashionUnited, 2026-09-11 | 2026-09-10 | SNIPPET |
| Caleres Q2 2026 release (businesswire 20260909945245), Genesco Q2 2026 | 2026-09-09 / 09-10 | SNIPPET (via `macro_category/shoe_retailer_margin_crosscheck.csv`) |
| On Q2 2026 6-K Ex. 99.3, sec.gov/Archives/edgar/data/0001858985/000185898526000018/a26q2-ex993xpressrelease.htm | 2026-08-11 | SNIPPET (opened by search summary only) |
| Deckers Q1 FY27 call highlights (nasdaq.com, marketbeat.com) | 2026-07-23 | SNIPPET (fetch returned 503) |
| Live pages: zappos.com listing pages, footlocker.com brand and sale pages, 10 Shopify stores' public products.json | 2026-10-14 | OPENED |
| Common Crawl: adidas.de and nike.com/de product pages, crawls CC-MAIN-2024-33/38, 2025-33/38, 2026-34/39 | crawl dates Aug and Sep 2024 to 2026 | OPENED |
| Placer.ai, eMarketer, ShopBack, Groupon, Slickdeals (off-price and outlet context) | 2025 to 2026 | SNIPPET, no Nike-specific data |
