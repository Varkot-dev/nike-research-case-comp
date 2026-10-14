# Nike LONG or SHORT: the scoreboard

Updated 2026-10-14, after the free-data hunt. Stock $35.35 (Oct 12, 2026). Submission Nov 1, finals Nov 19, Investor Day Nov 16 to 17.

This page sums up eight questions. Each one was investigated, checked by a skeptic, then re-graded with new free data gathered in the data hunt (folders under `data/hunt/`, each with a README listing sources, pull dates and caveats). Every hunt result was also re-run by a checker, and where the checker corrected a number we use the corrected one. The full notes are in this folder, one file per question, each with a new "data hunt" section at the bottom.

Tags: OPENED means we read the source itself, SNIPPET means we only saw a search summary, REPO means earlier work in this repo, DERIVED means our own arithmetic, HUNT means a dataset pulled and cleaned in the data hunt.

## 1. Bottom line

**Still lean SHORT, with low to moderate confidence. The data hunt did not change any grade, but it changed what the SHORT rests on.**

- **No question moved to strong or to weak.** We pulled about 17 new datasets (factory revenue, customs records, store locators, HKEX filings, Common Crawl archives of nike.com, resale prices, app reviews, Wikipedia and Reddit attention, hiring records, insider and 13F filings, government retail statistics, athlete podiums). They mostly agree with the earlier answers. Where a hunter claimed an upgrade to strong, the checker usually found a reason to pull it back (correlated benchmarks, a crawl confidence interval that was too narrow, a mixed-up period label).
- **What got firmer (SHORT side):**
  - China: a second, independent reason now backs the strong grade. Nike's partner stores in China are closing faster (Pou Sheng net closures per half: -40, -98, -200) while ANTA and Li Ning door counts are almost flat, and Nike's share of a 14-company China peer set fell from 65% (2022) to 50% (H1 2026).
  - Factory orders: on a two-year comparison Feng Tay is flat at about -6% a month, with no turn. Nike's own footwear revenue fell more than Feng Tay, so orders are not just moving to other factories.
  - Discounting: "the clean-up has stalled" is now close to strong. nike.com discount share was 30.5% in Mar to Sep 2025 and 31.0% in Mar to Sep 2026, and hidden "See Price in Bag" promotions are rising, which means the true 2026 number is higher.
  - Jordan retro: resale prices for the AJ1 High are still falling (-22% in USD in Q3 2026), so the part Nike says hits North America next has not bottomed.
  - Brand heat: Nike's share of World Marathon Majors podiums fell from 86% (2019) to 19% (2026), and its share of World Cup boots from 63% (2018) to 43% (2026).
- **What got weaker (also matters):**
  - "North America is channel fill" lost its direct proof. The test comparing Feng Tay with US imports fails on a two-year comparison, and Nike's NA footwear units ran at or above US consumer shoe spending (BEA real PCE) in the last 4 quarters. NA demand is not growing, but we cannot show it is being stuffed.
  - Nike's inventory is mid-pack against 12 peers, and its gross-margin gap to peers has narrowed. The "dirty balance sheet" story is gone.
  - Dunk and AF1 have hit a price floor on resale, and new Nike launches resell better than last year.
  - Hiring has stopped falling, and product and design roles rose from 32% to 44% of US corporate postings. This is a real product rebuild, but it reaches shelves in FY28 at the earliest.
- **The decider is still FY28 expectations (Investor Day, Nov 16 to 17).** Consensus FY28 EPS is about $1.65 on about +1% revenue. The hunt makes FY28 revenue look more like flat to -2% (China, Europe share loss, digital), but tariffs now running about 11.4% against Nike's 15% plan add about $0.08 to $0.12 of FY28 EPS, which offsets much of the gap.
- **Positioning is not evidence either way.** Record short interest (99.2M shares), 13F holder exits and the biggest insider buying in 20 years all failed to predict returns in our historical tests. Do not cite them as directional.

**In one sentence:** the new data confirms the business has not turned and that China and Europe are losing share, but most of it is already in Nike's guidance, so the pitch is a SHORT on FY28 expectations, and Investor Day will settle it.

## 2. The table

| # | Question | Answer in one sentence | Points to | Strength before hunt | Strength after hunt | Best evidence (source, date) |
|---|---|---|---|---|---|---|
| 1 | Is North America consumer demand growing, or is +9% NA wholesale channel fill? | Consumer demand is not growing and sell-through is being bought with discounts, but the new data cannot prove an ongoing channel stuff beyond what Nike disclosed. | SHORT | Moderate | Moderate (unchanged) | Nike Q1 FY27 10-Q (SEC, 2026-10-02, OPENED): NIKE Direct NA -6%; plus r/RunningShoeGeeks Nike share of deal posts 18.8% to 32.9%, p=0.0006 (HUNT reviews_sentiment, Jun to Aug 2026) and Foot Locker NA doors 1,665 to 1,531 (filings, Feb 2025 to Aug 2026). |
| 2 | Are Nike's factory orders (Feng Tay and others) turning up? | No: Feng Tay is about -6% a month on a two-year basis with no turn, but the holiday pace matches peer factories and consensus. | SHORT | Moderate | Moderate (unchanged) | Taiwan MOPS monthly revenue (HUNT trade_imports, Jul to Sep 2026): two-year Feng Tay -5.9% vs Lai Yih -5.7%, Pou Chen -7.1%; Nike footwear revenue two-year -11.8% vs Feng Tay -7.7%. |
| 3 | Has Greater China found a floor? | No: Nike guides China worse than -26%, its partners are closing stores faster while domestic brands hold, and its peer-set share keeps falling about 7 points a year. | SHORT | Strong | Strong (unchanged, more robust) | HKEX filings (HUNT stores, to Jun 2026): Pou Sheng net closures -40, -98, -200 per half vs ANTA plus ANTA KIDS -1.8%; Nike China peer-set share 65% (2022) to 50% (H1 2026) (HUNT peers_reported). |
| 4 | Is discounting getting better or worse? | Not better: nike.com discount share is flat year on year with hidden in-bag promos rising, but there is no clean proof it is getting worse in a Nike-specific way. | SHORT | Moderate | Moderate ("stalled" is near strong) | Common Crawl nike.com product-page panel, about 19,700 pages (HUNT pricing_catalog, Mar 2023 to Sep 2026): 30.5% to 31.0% Mar to Sep YoY; hidden promos 0/117 to 10/150 pages. |
| 5 | Are lifestyle classics (Dunk, AF1, Jordan) near a bottom? | Dunk and AF1 have hit a price floor, but Jordan retro has not, and attention to Dunk keeps falling, so the drag does not shrink within 2 to 3 quarters. | SHORT | Moderate | Moderate (firmer) | SNKRDUNK resale, 4,626 products (HUNT resale_secondary, Q3 2026): AJ1 High -22.0% YoY in USD vs -15.8% a year earlier; nike.com lifestyle discount share Aug to Sep 34% (2024), 41% (2025), 47% (2026). |
| 6 | Is the running recovery real full-price demand, or discount-driven? | Partly bought with discounts (especially Vomero), but the product is well rated and Nike discounts running about as much as Brooks, Saucony and ASICS. | SHORT | Moderate | Moderate (unchanged) | r/RunningShoeGeeks deal posts (HUNT reviews_sentiment, FY27 Q1): Nike Vomero deal posts 7 to 24; Shopify retailer markdowns (HUNT pricing_catalog, 2026-10-14): Nike running 35% vs Brooks 36%, Saucony 42%. |
| 7 | Are Wall Street expectations too high or too low? | Q2 and FY27 numbers match the evidence; FY28 revenue looks high, but tariff relief offsets much of the EPS gap. | NEUTRAL (decider) | Moderate | Moderate (unchanged) | Tariff gap sizing (HUNT risk_tariffs): actual blended rate 11.4% vs 15% plan, FY28 EPS +$0.08 to $0.12; Yahoo earningsTrend (2026-10-14, OPENED): FY28 EPS 1.646. |
| 8 | Do setups like Nike's today tend to bottom or keep falling? | History is a coin flip, and the new positioning data (insiders, 13F breadth, short interest) does not predict direction either. | NEUTRAL | Moderate | Moderate (unchanged) | SEC insider data and 13F panel, 59 stocks (HUNT people_governance, 2006 to 2026): insider clusters after a 40%+ fall, 252-day median excess -12.8% (5 of 11); breadth losers at a 60%+ drawdown -3.4% vs -9.0% for all deep fallers. |

## 3. The most surprising new data findings

1. **Nike delisted 33 of its 73 US full-price stores in one week** (Jul 18 to 25, 2026), mostly suburban "Nike Live" and "Well Collective" doors, per a weekly crawl of Nike's own store locator. The press reported 15 to 24. Factory outlets stayed flat at 212. The revenue hit is small, but it is a retreat from full-price Nike Direct. (HUNT stores)
2. **Nike hides its name on US customs records**, and has done so since Nov 2022 (shipper names too). So no one can count Nike's US shipments from free bill-of-lading data. The one Nike-owned brand still visible, Converse, shows Jul to Sep arrivals -28% YoY and -45% vs 2024, which matches Converse's reported -28%. (HUNT nike_shipments, trade_imports)
3. **nike.com hides a growing share of promotions behind "See Price in Bag"**, so the page shows full price. 0 of 117 archived pages in Aug to Sep 2024, 10 of 150 in Aug to Sep 2026. Adjusted, Aug to Sep discount share went from 32.9% to 40.7%. (HUNT pricing_catalog)
4. **Elite athletes are leaving Nike shoes.** World Marathon Majors podium share 86% (2019) to 19% (2026), with adidas at 56%. World Athletics podiums 57% (2022) to 38% (2025). NBA is the exception, steady at about 71%. (HUNT marketing_athletes)
5. **In Japan's resale market, Nike is holding activity better than rivals.** Trade days on SNKRDUNK fell about 22% for older Nike products vs about 45% for rival lifestyle lines (adidas Samba fading fast). Prices in USD are still falling, though. This is the best new LONG-side fact. (HUNT resale_secondary)
6. **Nike's job IDs are numbered in sequence**, so archived job links give a hiring-flow series. New requisitions fell from 35.8k a year (Jul 2025) to 22.1k (Jul 2026), then Jun to Sep 2026 ran about 14% above last year. Hiring stopped falling, and the mix moved toward product creation. (HUNT hiring)
7. **The "smart money is leaving" story is mostly a reporting rule.** Nike 13F holders fell by 147 and 187 in the last two quarters, but about 80% of those exits were small positions that no longer had to be reported once the price fell. True net exits are -25 and -39. (HUNT people_governance)
8. **Insider buying is the largest in 20 years, but it has not worked.** Nike's Dec 2025 and Apr 2026 insider buy rounds each lost 31 to 34 points against the S&P 500 over the next six months. (HUNT people_governance)
9. **The adidas "attention win" in summer 2026 was all World Cup.** After the World Cup (Aug to Oct), Nike gained on adidas in Chinese and German Wikipedia page views (+16% to +17%). (HUNT search_attention)
10. **A record-low margin index for US shoe stores** (BLS PPI, 91.2 in Aug 2026, lowest in 24 years) is not confirmed by Caleres or Genesco's reported margins, so we ignore it. (HUNT macro_category)

## 4. Every new dataset (for reuse)

All paths are under `data/hunt/`. Each folder has a README.md with source URLs, pull dates, methods and caveats, and a `scripts/` folder to re-run the pull. Raw pulls are in each `raw/` folder.

| Folder and key files | What it is | Period |
|---|---|---|
| `trade_imports/nike_vs_industry_monthly.csv` | Feng Tay, Pou Chen, Lai Yih, Fulgent Sun monthly revenue in USD vs US footwear imports and imports weighted to Nike's sourcing mix | 2019-01 to 2026-09 |
| `trade_imports/us_imports_footwear_apparel_monthly.csv`, `us_imports_hs6_athletic_monthly.csv` | US Census / Comtrade footwear and apparel imports by country; sports footwear HS 640411 and 640219 | 2019-01 (HS6 from 2023-01) to 2026-07 |
| `trade_imports/eu_imports_footwear_monthly.csv`, `indonesia_exports_footwear_monthly.csv`, `vietnam_exports_footwear_monthly_2019_2023.csv` | EU footwear imports from VN, ID, CN; Indonesia and Vietnam footwear exports | 2019 to 2026-07 (Vietnam to 2023) |
| `trade_imports/nike_factory_map_2026-10-14.csv` | Nike's published factory list with worker counts | Snapshot 2026-10-14 |
| `trade_imports/importinfo_*.csv`, `nike_shipments/bol_monthly_by_entity.csv`, `nike_shipments/importgenius_*.csv` | Bill-of-lading counts for Nike entities, Converse, Nike Canada, Nike factories and peers | 2019-01 to 2026-10 (annual from 2006) |
| `stores/nike_locator_weekly_counts.csv`, `nike_locator_store_events.csv`, `nike_locator_2026-10-14.csv` | Nike's own store locator crawled weekly: counts by country and type, openings and closures | 2023-01 to 2026-10 |
| `stores/partner_doors_filings.csv`, `partner_doors_weekly_atp.csv` | US partner door counts (Foot Locker, DICK'S, Academy, Genesco, JD) from filings and store locators | FY2024 to Aug 2026 |
| `stores/pousheng_store_counts.csv`, `topsports_store_counts.csv`, `topsports_quarterly_updates.csv`, `anta_store_counts.csv`, `lining_pos_counts.csv` | China store counts and selling area from HKEX filings (Nike partners and domestic controls). Note: Pou Sheng net_change mixes full-year and half-year rows. | 2018 to Jun 2026 |
| `pricing_catalog/pdp_panel_tidy.csv.gz`, `pdp_nike_monthly.csv`, `pdp_nike_month_yoy.csv`, `pdp_nike_window_by_category.csv` | nike.com product pages from Common Crawl: discounted or not, depth, category | 2023-03 to 2026-09 |
| `pricing_catalog/cc_pdp_panel_adidas.csv`, `pdp_adidas_window_by_category.csv` | Same for adidas.com (thin: two crawls per window) | 2023 to 2026-09 |
| `pricing_catalog/live_nikecom_union_catalog_20261014.csv.gz`, `live_category_walls_20261014.csv` | Live nike.com catalog and category wall counts | Snapshot 2026-10-14 |
| `pricing_catalog/shopify_tidy_brand_products_20261014.csv.gz` and `shopify_*` tests | 16 US Shopify sneaker and running retailers: markdowns by brand and product age | Snapshot 2026-10-14 |
| `resale_secondary/snkrdunk_product_month.csv`, `snkrdunk_products.csv` | SNKRDUNK (Japan) daily resale trades rolled to product-month, 4,626 products, Nike and 9 rivals | 2019 to 2026-10 |
| `resale_secondary/sneakerping_brand_below_retail_aug2026.csv`, `laced_products_sold28d.csv`, `usdjpy_monthly_ecb.csv` | US resale vs retail by brand; UK Laced units sold; yen rate for USD conversion | Snapshots Aug to Oct 2026; FX 2022-12 to 2026-10 |
| `reviews_sentiment/fl_bv_reviews_tidy.csv.gz`, `fl_bv_monthly_family.csv` | Foot Locker review feed including reviews syndicated from DICK'S, by brand and model | 2009 to 2026-10 |
| `reviews_sentiment/nike_reviews_tidy.csv.gz`, `nike_reviews_monthly_by_model.csv` | nike.com reviews, organic vs incentivized, by model | 2016-05 to 2026-10 |
| `reviews_sentiment/zappos_reviews_tidy.csv`, `fleetfeet_products_2026-10-14.csv` | Zappos reviews by launch cohort; Fleet Feet product view counts | 2022 to 2026; snapshot |
| `reviews_sentiment/reddit_posts_tagged.csv.gz` | Reddit posts (r/RunningShoeGeeks, r/Sneakers, r/Nike, r/Hoka and others) tagged by brand, model, deal flair. Sample break from Oct 2025. | 2020 to 2026-10 |
| `search_attention/wiki_pageviews_daily_long.csv` | Wikipedia page views for Nike, Jordan, Dunk, AF1 and 14 rival brands, several languages. Salomon double-count: use the checker fix. | 2019-01 to 2026-10-13 |
| `search_attention/gtrends_batches_long.csv`, `tranco_rank_semimonthly_long.csv`, `deals_titles_brand_tags.csv`, `stocktwits_messages.csv` | Google Trends, web-traffic rank, Reddit deal posts, Stocktwits sentiment | 2019 to 2026-10 |
| `apps_digital/play_reviews_monthly.csv`, `play_reviews_fq.csv` | Google Play review counts for Nike, SNKRS, adidas and US retail apps, several countries | 2019 to 2026-10 |
| `apps_digital/snkrs_products_tidy.csv`, `web_semrush_history.csv`, `appstore_charts_brand_ranks_2026-10-14.csv` | SNKRS launch feed; web visits for 25 domains; App Store shopping ranks in 40 countries | 2021 to 2026-10; Mar to Sep 2026; snapshot |
| `hiring/req_velocity_monthly.csv`, `nike_open_postings_series.csv`, `cc_job_objects_bucketed.csv`, `live_postings_workday_2026-10-14.csv` | Nike requisitions opened per month, open postings, job-family mix | 2019-10 to 2026-10 |
| `hiring/h1b_lca_clean.csv`, `qcew_washington_county_or.csv`, `warn_notices_warntracker.csv`, `adidas_open_postings_series.csv` | H-1B filings by role for Nike and peers; Beaverton-area employment; layoff notices; adidas postings | 2018 to 2026 |
| `people_governance/insider_open_market_peers_2006_2026.csv`, `nke_insider_yearly_2006_2026.csv`, `insider_cluster_events.csv` | SEC insider trades for Nike and 29 peers; cluster event study | 2006 to 2026-09 |
| `people_governance/nke_13f_holder_panel_2018_2026.csv`, `breadth_event_panel.csv` | Every Nike 13F holder by quarter; breadth for 59 consumer stocks with forward returns | 2018 Q1 (panel 2014) to 2026 Q2 |
| `people_governance/finra_short_volume_daily_2019_2026.csv`, `sec_fails_to_deliver_2019_2026.csv`, `nke_borrow_fee_ibkr_snapshot_2026-10.csv` | Short volume, fails to deliver, borrow fee | 2019-01 to 2026-10 |
| `people_governance/nke_say_on_pay_2015_2026.csv`, `nke_director_votes_2015_2026.csv`, `efts_alumni_appointments_by_year.csv`, `blind_ratings_by_year.csv` | Shareholder votes, Nike alumni appointed elsewhere, employee ratings | 2015 to 2026 |
| `risk_short_interest/si_all.csv`, `nke_short_interest_2017_2026.csv`, `prices_all.csv` | Short interest and prices for about 60 stocks, run-persistence events | 2017-12 to 2026-09 |
| `risk_tariffs/tariff_gap_sizing.csv` | Actual vs planned tariff rate and EPS effect | FY27 to FY28 |
| `risk_history/out/` | Event study of similar setups across US brands and retailers | 2010s to 2026 |
| `macro_category/us_category_monthly_long.csv`, `test1_us_category_vs_nike_na_quarterly.csv`, `us_footwear_circana_press.csv` | BEA PCE shoes, Census shoe and sporting goods stores, Circana press figures, aligned to Nike quarters | 2015 to 2026-08 |
| `macro_category/china_nbs_retail_categories_monthly.csv` | China NBS retail sales by category (clothing and shoes; sports and recreation incl. toys) | 2022 to 2026-08 |
| `macro_category/uk_ons_retail_monthly.csv`, `canada_retail_by_naics_monthly.csv`, `europe_retail_hicp_monthly_long.csv`, `test3_us_retail_margin_ppi_monthly.csv` | UK, Canada and EU retail; BLS shoe-store margin index | 1988 / 2017 / 2015 to 2026 |
| `peers_reported/panel_region_quarterly.csv`, `panel_growth_comparable.csv`, `china_peers_sellthrough_quarterly.csv` | Regional revenue for Nike and 14 peers (adidas, Puma, ASICS, On, Deckers, Lululemon, Amer, ANTA, Li Ning, Xtep and others) | 2016 to 2026 Q2 |
| `marketing_athletes/elite_visibility_share.csv`, `nba_shoe_brand_minutes_by_season.csv`, `kits_team_season_tidy.csv`, `endorsement_events.csv` | Marathon, athletics and World Cup podium and boot shares; NBA shoe minutes; big-5 league kit suppliers; endorsement wins and losses | 2014 to 2026 (use NBA from 2020-21) |
| `marketing_athletes/instagram_top_accounts_wiki_revisions.csv`, `youtube_subscribers_history.csv`, `tiktok_brand_snapshot_2026-10-14.csv` | Social follower histories for Nike, rivals and top-50 Instagram accounts | 2016 to 2026-10 |
| `earnings_calls/turns.csv`, `guidance_scorecard.csv`, `fy28_clues.csv`, `tone_index.csv` | Parsed Nike call transcripts, guidance vs actual scorecard, FY28 language | FY21 to Q1 FY27 |

## 5. What could still flip the answer

**Before the Nov 1 submission:**

| Date (2026) | Data | LONG if | SHORT if |
|---|---|---|---|
| From Oct 15 | Tmall Double 11 presale rankings | Nike back at #1 (China floor hint) | Nike keeps losing rank to ANTA, Li Ning |
| About Oct 16 to 20 | China NBS September retail sales | Clothing and shoes reaccelerate, gap to Nike narrows | Category steady while Nike falls (confirms Nike-specific) |
| About Oct 16 | Census Aug shoe-store sales | Real growth with Nike flat would weaken the share-loss story for Nike | Weak shoe stores keep the channel soft |
| About Oct 23 | FINRA short interest, Oct 15 settlement | A big fall (shorts covering) | Another rise (context only; it does not predict) |
| About Oct 22 to 28 | Topsports interim results (Jun to Aug) | Sales better than a low-teens decline, selling area stops shrinking | Low-teens or worse, area still down about 11% |
| Late October | adidas, ANTA, Li Ning, Xtep Q3 China updates | Peers also weak (macro, not Nike) | Peers recover while Nike does not |

**Before the Nov 19 finals:**

| Date (2026) | Data | LONG if | SHORT if |
|---|---|---|---|
| **About Nov 10** | **Feng Tay October revenue (Taiwan MOPS)** | Better than about -3% on a two-year USD basis | Worse than about -8% while Lai Yih and Pou Chen hold |
| About Nov 10 to 12 | Pou Sheng October revenue; 9-month results Nov 12 | Two-year stack better than -8% | Closures and sales keep accelerating |
| Mid November | Census Sep shoe stores; Yue Yuen Q3 pairs; Feng Tay Q3 report | Pairs, not price, explain Feng Tay | Pairs falling |
| Weekly | Nike store locator (our crawl) | No more US closures | More full-price door cuts |
| **Nov 16 to 17** | **Nike Investor Day** | FY28 held near consensus and an FY29 EBIT margin target above about 9% | FY28 EPS framed below about $1.50, or FY28 revenue below flat |

**After the finals (cannot help the pitch, but would prove it):** DICK'S and Foot Locker Q3 (late Nov) and Nike Q2 FY27 (about Dec 17), where gross margin above or below 40.6% decides which history bucket Nike sits in.

## 6. Where investigator, skeptic and data hunt disagreed

| Question | Disagreement | How we resolved it |
|---|---|---|
| Q1 NA | Investigator strong; skeptic moderate. Macro hunter claimed strong; checker found Nike NA footwear units at or above real PCE in the last 4 quarters and the channel-fill import test failed on a two-year basis. | **Moderate.** Demand not growing is well supported; ongoing channel fill is not proven. |
| Q2 Factory orders | Trade hunter claimed strong on two-year share loss; checker said the benchmarks are correlated and the loss is already in Nike's reported revenue. | **Moderate.** No turn, but in line with consensus. |
| Q3 China | Stores hunter and peers hunter claimed strong; checker cut the store test to moderate (Topsports shrink is steady, not accelerating). | **Strong**, now resting on guidance plus a shrinking channel plus share loss. |
| Q4 Discounting | Pricing hunter claimed strong; checker found the crawl-level interval is -4.4 to +5.6 points and acceleration rests on two months. | **Moderate.** "Stalled" is near strong; "getting worse" is not shown. |
| Q5 Lifestyle | Resale hunter leaned LONG; checker found the resale price "bottom" is mostly the weaker yen. | **Moderate SHORT.** Dunk and AF1 at a floor, Jordan retro not. |
| Q6 Running | Reviews hunter found strong product ratings; checker found Nike ties Brooks and HOKA, not beats them. | **Moderate SHORT.** Discounted but not uniquely so. |
| Q7 Expectations | FY28 revenue risk firmer; tariff relief offsets EPS gap. | **NEUTRAL, the decider.** |
| Q8 History | Insider and 13F signals looked directional; event studies show they are not. | **NEUTRAL.** Do not cite positioning either way. |

**How we weighed it overall:** we did not average the eight. Six business questions say "not yet turned", and the hunt confirms it from new, independent sources. But Nike has already guided most of it. The call rests on FY28, where share loss in China and Europe argues revenue comes in below consensus and tariff relief argues EPS holds up better. That is why the answer is lean SHORT with low to moderate confidence, and why Investor Day on Nov 16 to 17 matters more than any data point we can gather before then.
