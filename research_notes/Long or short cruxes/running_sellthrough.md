# Crux 6 rescue: Nike running sell-through by routes other than SNKRDUNK and Tranco

Prepared 2026-10-14. Data and scripts: `data/hunt/running_sellthrough/` (README lists every route). Labels: OPENED = fetched and read this session; OPENED (repo) = data stored in this repo by an earlier session; SNIPPET = search summary only; HUNT = dataset pulled and cleaned in this folder; [my arithmetic] = computed from those files.

This note adds to `running_quality.md` (which already holds the Fleet Feet, nike.com and Running Warehouse markdown work and the skeptic review). It does not repeat that work. It adds the volume side (review velocity, stock depth, Amazon rank, run-specialty share, gear data, peer growth) that the two failed tests could not give.

## 1. Verdict

**NEUTRAL, weak to moderate. Volume is real; price health is mixed. It does not overturn the existing SHORT (moderate) on discounting, but it removes one argument for SHORT: that Nike's running gain is channel stuffing.**

Rule stated in advance: Nike running proxies growing faster than Hoka, ASICS and Brooks at healthy price points points LONG; growth only with deep discounts or stock piling up points SHORT.

| Part of the rule | Result | Reads as |
|---|---|---|
| Faster than Hoka | Dick's review flow Jun to Jul 2026 vs 2025: Nike +48.6%, Hoka +21.6% | met |
| Faster than Brooks | Brooks +15.8% on the same measure | met |
| Faster than ASICS | ASICS 0.0% at Dick's (81 vs 81 reviews, tiny base) but ASICS reports North America +33.8% and US wholesale +36.6% (SGB, 2026-08-17, OPENED) | not met on company data |
| Healthy prices | Pegasus 42: about 25% of units at about 25% off at Fleet Feet; 43% to 63% of colourways discounted on nike.com (see `running_quality.md`). Vomero 18, Vomero Plus, Vomero Premium, Pegasus Plus 2: 0% on markdown at Fleet Feet | mixed: volume franchise discounted, premium tier holds price |
| Stock piling | Fleet Feet holds 0.072 Nike units per 30-day product view against Hoka 0.127, ASICS 0.219, Brooks 0.361, Saucony 0.479. Nike's live colours are out of stock on 48% of colour x size cells against Hoka 25%, Brooks 23% | not met (no pile-up where we can see) |

Why not LONG: Nike is not outgrowing ASICS or adidas (running +28%), its Fleet Feet distribution started only on 2026-04-09 (so some growth is new doors, not same-store sell-through), and review counts cannot separate price-driven from full-price volume. Why not SHORT: the stuffing and stock-pile arms of the SHORT case find nothing in the channels we can read, and the new premium tier (Vomero Plus at $180, Pegasus Plus 2 at $170, Vomero Premium at $230) is selling at full price.

Suggested wording for scoreboard row 6 (not edited here): "Running volume is real (share of Dick's review flow +3.8 points, no stock pile at Fleet Feet), but the volume franchise Pegasus 42 is being moved with markdowns, so full-price share gain is only shown for the premium tier." Direction stays SHORT-lean on price, moderate; the volume sub-question is NEUTRAL.

## 2. Key numbers

### 2.1 Review velocity at Dick's (route 3; HUNT, from Foot Locker Bazaarvoice reviews syndicated from dickssportinggoods.com)

Files: `dicks_window_yoy.csv`, `dicks_nike_family_yoy.csv`, `dicks_monthly_brand.csv`.

| Window | Nike | Hoka | Brooks | ASICS | Nike share of the four |
|---|---|---|---|---|---|
| Jun to Jul, 2025 reviews | 407 | 976 | 645 | 81 | 19.3% |
| Jun to Jul, 2026 reviews | 605 | 1,187 | 747 | 81 | 23.1% |
| Change | +48.6% | +21.6% | +15.8% | 0.0% | +3.8 points |
| Jun to Aug change (2025 to 2026) | +14.6% | -4.6% | -13.2% | -14.0% | 20.0% to 23.8% |

Nike by family, Jun to Jul: Pegasus 89 to 154 (+73%), Pegasus Premium 39 to 50 (+28%), Vomero 240 to 222 (-7%), Vomero Plus 0 to 167 (new). Growth comes from Pegasus and the new Plus tier, not from Vomero 18.

Caveats: Dick's syndication stepped up in June 2025 for every brand and the feed thins from August 2026, so only matched windows inside the stable regime and cross-brand shares are used. Reviews are a proxy and a markdown can raise them. Pegasus 42 may be selling because of its markdown.

Generation over generation (first 90 days of reviews, Zappos, `gen_over_gen_n90.csv`): Pegasus 42 / Pegasus 41 = 0.72 (31 vs 43), Ghost 18 / 17 = 1.53, Nimbus 28 / 27 = 0.43, Novablast 6 / 5 = 0.48. Samples are 30 to 330 reviews, so this is INCONCLUSIVE; the Pegasus 41 launch baseline at Dick's cannot be read (launch dates before June 2025 are artefacts of the syndication step).

### 2.2 Stock depth and views at Fleet Feet (route 2; HUNT, 12,746 colour x size rows for 32 current models, 2026-10-14)

Files: `fleetfeet_sizerun_by_brand.csv`, `fleetfeet_sizerun_depth.csv`, `fleetfeet_brand_views.csv`, `fleetfeet_markdown_by_model.csv`.

| Brand | Share of live-colour UPCs out of stock | Units per 30-day view | Core sizes in stock | Product views, 30d vs prior 30d (all products) |
|---|---|---|---|---|
| Nike | 48.3% | 0.072 | 75% | -7.0% (5.5% of views) |
| Hoka | 24.9% | 0.127 | 85% | -3.0% |
| Brooks | 22.5% | 0.361 | 89% | -8.3% |
| ASICS | 33.6% | 0.219 | 92% | -15.9% |
| Saucony | 23.3% | 0.479 | 90% | -12.2% |
| On | 17.4% | 0.212 | 97% | -22.1% |
| New Balance | 47.0% | 0.081 | 68% | -6.2% |
| adidas | 52.8% | 0.063 | 73% | +14.9% |

Nike Vomero line (men's): 55% to 63% of live-colour cells out of stock. Reads: no Nike pile-up at Fleet Feet; stock is thin against interest. This fits both "selling through" and Nike's stated plan to cut supply, and the data cannot separate them. A one-day read; Aug to Sep is also seasonal.

### 2.3 Amazon US Best Sellers, running (route 1; HUNT, one snapshot 2026-10-14, top 80 ranks)

Nike appears only at entry level: Run Defy (men's #7), Run Swift 3 (#13), Revolution 8 (#18), Revolution 8 women's (#8). No Pegasus or Vomero in either list. Entries per brand (men's / women's): Brooks 13 / 10, New Balance 10 / 12, ASICS 8 / 9, Hoka 2 / 3, Nike 4 / 3. Amazon is not where Nike's performance recovery sells, and a single snapshot gives no trend. Weekly review counts, "bought in past month" and archived rank pages are not reachable (README rows 1b, 1c).

### 2.4 Run-specialty share, gear data and peer growth (routes 4 and 6; OPENED)

- Confluence Running run-specialty brand share, from a public spreadsheet created 2026-02-18 (OPENED): Nike 0.00% (Q1 and Q2 2025), 0.31% (Q4 2025), 1.43% (2026 to date, about seven weeks). Hoka 20.13 / 18.46 / 19.17, Brooks 20.38 / 18.90 / 17.05, ASICS 5.67 / 8.06 / 8.43, Saucony 14.05 / 11.66 / 12.46, New Balance 8.20 / 10.84 / 9.68, On 5.23 / 5.43 / 5.05, adidas 1.87 / 2.46 / 2.41. The page does not say whether shares are units or dollars. Nike is growing from nothing because it re-entered the channel.
- Fleet Feet and Nike announced a nationwide partnership on 2026-04-07 (Footwear Magazine, 2026-04-08, updated 2026-10-03, OPENED): more than 285 stores, Pegasus 42 on sale from 2026-04-09. The article has no sales figures.
- Strava (T3, OPENED): mid-year report 2025-08-28 puts ASICS first and Nike second among logged running shoe brands, Hoka third (Brooks first in the US). Year in Sport (T3, 2025-12-03): ASICS Novablast the most used shoe, Pegasus second, Clifton third; in 2024 the Pegasus was first. No 2026 Strava report was found. This is a lagging, pre-recovery read and points SHORT-lean.
- Circana US running H1 2026: +13% in dollars and +13% in units (SGB 2026-08-17 and Endurance Sports Wire 2026-08-14, both OPENED), so average price about flat. For 2025 Running Insight (2025-11-26, OPENED) had units +4%, price +4%, dollars +8%.
- Company-reported running growth, latest quarter (SGB 2026-08-17, OPENED, and the Nike Q1 FY27 call in `data/hunt/earnings_calls/turns.csv`): Nike Running "up double digits again", sixth straight quarter (management opinion, no figure); ASICS North America +33.8%, US +19.4%, run specialty North America +14.2%; adidas running +28%; Brooks first half +14% (Americas +9%); Hoka +7.7%; Saucony +9.9%; On Americas +13.0% constant currency. Nike's "double digits" against a category at +13% is not shown to be faster than the category.
- Marathon finisher surveys: only a six-athlete Chicago 2025 podium count was opened (Nike 2, adidas 2, Hoka 1, ASICS 1; Marathon Handbook, 2025-10-13). A search snippet quoting Nike at 27.4% of Chicago finishers was not on the opened page and is not used.

### 2.5 Attention and traffic (routes 5 and 7; HUNT)

- r/RunningShoeGeeks brand mentions, Jun to Sep 2024 / 2025 / 2026: Nike share 20.0% / 20.9% / 20.3% (flat); Vomero share of tagged model mentions 2.2% / 23.3% / 27.3%; Pegasus 11.9% / 13.4% / 6.6%; adidas 14.9% / 25.8% / 28.7%. Archive sample drops from Oct 2025, so only shares are used. NEUTRAL.
- Semrush modelled visits, Aug vs Jun 2026 (`semrush_visits_running_brands_vs_controls.csv`): nike.com +6.5%; Hoka +6.8%, On +23.0%, ASICS +10.7%, New Balance +12.8%, adidas -21.3%; controls Dick's +12.5%, Zappos +21.9%, Amazon -0.1%. Nike trails the run brands and the retail controls over the summer, but this is brand-wide, modelled, and six months long. Weak SHORT-lean.
- CrUX rank buckets (Feb 2021 to Sep 2026): nike.com is in the global top 1,000 in every month, so it cannot show a change; ASICS dropped from the 10,000 bucket to 50,000 in Sep 2026 and On rose from 50,000 to 10,000. Unusable for Nike.
- Google Trends: blocked (429). YouTube search `estimatedResults` is unstable (Vomero Plus last-year 121k vs Pegasus 42 3.5k) and is not used.

## 3. Alternatives and what ruled them out

1. "Nike's running gain is channel stuffing." Not supported where readable: Fleet Feet stock is lean (0.072 units per view), Dick's review share rose 3.8 points (reviews are written by buyers, not shipped), Amazon shows no Nike performance overhang. Not ruled out in Dick's and Foot Locker own stock, which are not observable.
2. "Nike's volume is bought with markdowns." Survives for Pegasus 42 (`running_quality.md`: 43% to 63% of colourways discounted on nike.com; here about 25% of Fleet Feet units at 25% off). Does not apply to Vomero Plus, Vomero Premium and Pegasus Plus 2.
3. "Growth is new distribution, not same-store gain." Survives. Fleet Feet rollout began 2026-04-09, Nike's run-specialty share was 0.00% in H1 2025 (Confluence), and Dick's Vomero Plus reviews start only in 2026. Same-store sell-through cannot be isolated with free data.
4. "Review counts are a price artefact or a syndication artefact." Partly survives; shares inside one regime reduce the second, nothing in free data removes the first.

## 4. What would settle it, and how to get it

- Daily repeats of the Amazon rank lists and Fleet Feet UPC stock until Nov 19 (`scripts/run_daily_snapshots.sh`): a falling out-of-stock share with unchanged prices would be SHORT-lean (demand fading); rising sell-through with Pegasus 42 markdowns clearing would be LONG-lean.
- A paid Circana or Karnan run-specialty brand series with average price (shown at The Running Event, early Dec 2026) or Nike's running full-price split at Investor Day (Nov 16 to 17).
- An archived baseline for Pegasus 41 stock and rank (needs web.archive.org, which is blocked here; only an authorised environment can pull it).
- Dick's own Q3 call (late November, after the finals) for running sell-through by brand.

## 5. Routes tried (full log in `data/hunt/running_sellthrough/README.md`)

Worked: Fleet Feet UPC stock, Fleet Feet views, Dick's review velocity, nike.com live catalog cut, Amazon Best Sellers (one snapshot), Reddit model shares, Confluence share, Strava (2025), Circana and peer growth quotes, Semrush windows. Partial: Zappos generation cohorts, YouTube, CrUX buckets, Running Warehouse reviews. Blocked: Amazon search and weekly reviews, Common Crawl for these retailers (1 capture in 48 queries), web.archive.org, Zappos best-seller sort (parameter ignored), Running Warehouse and REI and Dick's and brand sites, Google Trends, Cloudflare Radar, marathon finisher shares.

## 6. Sources

| # | Source | Date | Status |
|---|---|---|---|
| 1 | Fleet Feet public search index (UPC level), `raw/fleetfeet_upc_2026-10-14.csv.gz` | 2026-10-14 | OPENED |
| 2 | Foot Locker Bazaarvoice reviews syndicated from Dick's, `data/hunt/reviews_sentiment/fl_bv_reviews_tidy.csv.gz` | pulled 2026-10-14 | OPENED (repo) |
| 3 | Zappos reviews and launch cohorts, `data/hunt/reviews_sentiment/` | pulled 2026-10-14 | OPENED (repo) |
| 4 | Amazon US Best Sellers, men's and women's running | 2026-10-14 | OPENED |
| 5 | nike.com live catalog, `data/hunt/pricing_catalog/live_nikecom_union_catalog_20261014.csv.gz` | 2026-10-14 | OPENED (repo) |
| 6 | Confluence Running, run specialty market share sheet | 2026-02-18 | OPENED |
| 7 | Footwear Magazine, Fleet Feet and Nike partnership | 2026-04-08, updated 2026-10-03 | OPENED |
| 8 | SGB, Circana running footwear H1 2026 and brand results | 2026-08-17 | OPENED |
| 9 | Endurance Sports Wire, US running shoes H1 2026 | 2026-08-14 | OPENED |
| 10 | Running Insight, "Keeping the pace in 2026" | 2025-11-26 | OPENED |
| 11 | Runstyle via formula4media, "2026 Outlook: The Race is On" | 2025-11-21 | OPENED |
| 12 | T3, Strava Mid-Year report | 2025-08-28 | OPENED |
| 13 | T3, Strava Year in Sport 2025 | 2025-12-03 | OPENED |
| 14 | Marathon Handbook, Chicago Marathon 2025 shoes | 2025-10-13 | OPENED |
| 15 | Nike Q1 FY27 call, `data/hunt/earnings_calls/turns.csv` | 2026-10-01 | OPENED (repo) |
| 16 | Semrush and CrUX files, `data/hunt/apps_digital/` | 2026-03 to 2026-09 | OPENED (repo) |
| 17 | Search snippet: Chicago 2025 finisher shares (Nike 27.4%) | 2025 | SNIPPET, not used |
| 18 | Brooks first-half release (brooksrunning.com) | 2026-08-12 | SNIPPET (403 on fetch) |
