# Deep dive: definitive tests of Nike's supply cut and full-price recovery

**Started:** October 13, 2026. **Status:** live document, updated and committed as each test reports. **Why this exists:** the review-tone test (`research_notes/thesis_tests/review_tone_jin2023.md`) came back inconclusive because it measured a proxy (how buyers feel) instead of the quantities that decide the thesis (pairs, price, stock left, time to markdown), and it had no control group. Every test here is designed to (1) measure the quantity directly, (2) compare a treated group with a control group or a before with an after, and (3) state in advance what result would prove the thesis wrong.

**The two questions every test feeds:**
1. **Supply or demand?** Is Nike's decline in Jordan and lifestyle footwear a deliberate supply cut that will restore full-price selling, or lower full-price demand that supply cuts will not fix (`research_notes/12_jordan_brand_thesis.md`)?
2. **Is full-price recovery on track?** Does the evidence support the timing the share price needs (12% to 14% EBIT margin by FY2031 at a 10% WACC; `research_notes/thesis_tests/consensus_and_valuation.md`), or has it slipped (`research_notes/16_full_price_recovery.md`)?

Labels follow the house rules (`CLAUDE.md`): filing citations with printed pages, *Nike transcript*, *Nike release*, *secondary*, *data provider*, *market data*, *my arithmetic*, *my inference*. Findings marked **[KEY FINDING]** are the strongest, best-sourced results and are candidates for the pitch.

## Headline findings

1. **[KEY FINDING] The supply-cut signature appears only where Nike is shrinking the business, not where the Jordan cut is aimed** (Test 5). Greater China (units -26%, ASP flat on lower discounts) and Converse (units -34%, ASP +6 points) show units cut at stable prices in Q1 FY2027. North America, the focus of the Jordan retro cut, sold 2% more footwear pairs at lower ASP, and EMEA cites higher discounts (Q1 FY27 10-Q pp. 26 to 28). All 694 unit and price statements Nike filed since FY2017 are in `data/definitive/nike_units_asp_tidy.csv`.
2. **[KEY FINDING] Nike's main shoe factory cut in 2023, four quarters before Nike's footwear revenue fell, and barely cut when it did** (Test 1, chart 20). Feng Tay revenue fell 10% to 23% a year in Q3 FY23 to Q2 FY24 while Nike footwear grew; in FY2025 Nike footwear fell 11.7% but Feng Tay only 4.7%. The factory data fit the 2023 inventory clear-out, not a supply cut behind the FY2025 decline. Feng Tay also leads Nike footwear growth by about one quarter (correlation 0.68 excluding COVID years), and its Q1 FY27 -8.8% points to continued weakness in Q2.
3. **[KEY FINDING] Retros released just before the October 2026 cut sit in full size runs at full price weeks after launch** (Test 3). AJ4 Rare Air Tour Yellow has all 13 sizes in stock at nike.com, Foot Locker and Champs on day 38, the oversupply pattern measured directly on the shelf. Whether the cut changes this is decided by re-running the tracker on the AJ1 Royal around October 24 and November 7.
4. **[KEY FINDING] Nike holds Jordan retro prices on its own site while the shoes do not sell** (Tests 2 to 4). 2 of 113 listed colourways in the main Jordan retro lines are discounted on nike.com today, against all 22 Pegasus 41 colourways from 2024; yet retros sit in full size runs weeks after launch and trade 26% to 35% below retail on resale. The markdown happens at retailers and in resale, so a held list price is not evidence of full-price demand.
5. **[KEY FINDING] Retailers are discounting 2026 Jordan retros that Nike still sells at full price** (Test 2). Foot Locker has the 2026 AJ3 IF4396-100 21% off and 2025 to 2026 women's AJ4s 18% to 23% off, while no AJ1 High, AJ3 or AJ4 release from 2024 to 2026 was seen discounted within 90 days on nike.com. Nike's full-price list hides the markdowns happening in its wholesale channel.
6. **The FY2018 "supply reset" began with discounting** (Test 5). North America footwear units were flat while discounts cut 3 points off revenue in Q1 FY2018 (Q1 FY18 10-Q p. 26); units fell only in the next two quarters. The FY2018 analog for Jordan is a discount-then-cut sequence.

## Test 1. Factory orders: Nike's footwear suppliers' monthly revenue and pairs

- **Measures:** production volume and price per pair at the factories that make Nike's shoes, reported monthly in exchange filings, months before Nike reports.
- **Treated vs control:** Nike-dependent suppliers vs suppliers serving other brands; FY2018 reset vs today.
- **Would disprove "deliberate supply cut":** supplier pair volumes flat or rising while Nike's revenue falls (stock building somewhere), or no cut in volumes before Nike's revenue fell.

**Result (Oct 13, 2026).** Data in `data/definitive/suppliers/` (method notes in `FINDINGS_test1_supplier_cut.txt`); chart 20.
- **Series:** monthly revenue Dec 2013 to Sep 2026 for Feng Tay (9910.TW), Pou Chen (9904.TW), Eclat and Makalot from Taiwan's MOPS via the FinMind mirror (287 of 296 values checked against MOPS match; every Feng Tay month 2018 to 2026 matches Feng Tay's IR page). Yue Yuen (0551.HK) monthly revenue from 154 HKEX announcements, and pairs shipped and ASP per pair from 51 results announcements. All summed into Nike fiscal quarters and converted to USD at monthly averages (my arithmetic).
- **Customer:** Feng Tay's single largest footwear customer was 83% to 86% of revenue in 2017, 2018 and 2022 to 2025 (annual reports, major-customer note; my arithmetic). Feng Tay does not name it; it describes itself as Nike's longest-serving footwear manufacturing partner, so "Nike" is my inference. Yue Yuen is multi-brand (largest customer 18% to 26% of sales), so it is a weaker Nike signal.

| Nike fiscal quarter | Feng Tay revenue, USD, YoY | Nike Brand footwear revenue, YoY |
|---|---|---|
| Q3 FY23 (Dec 2022 to Feb 2023) | -13.7% | +19.7% |
| Q4 FY23 | -23.2% | +7.0% |
| Q1 FY24 | -12.4% | +3.8% |
| Q2 FY24 | -10.2% | +1.2% |
| FY2025 (full year) | -4.7% | -11.7% |
| FY2026 (full year) | +0.3% | +0.1% |
| Q1 FY27 | -8.8% | -6.2% |

- **[KEY FINDING] The big factory cut came four quarters before Nike's footwear revenue fell, and it matches the 2022 to 2023 inventory clear-out, not the Jordan and classics decline.** Feng Tay revenue fell 10% to 23% a year in Q3 FY23 to Q2 FY24 while Nike footwear was still growing; Yue Yuen pairs fell 19.9% in calendar 2023; Nike's inventory was up 44% a year earlier at Aug 2022 and down 14% at Nov 2023 (repo facts). Feng Tay's largest customer took NT$73.0 billion in 2023 against NT$81.6 billion in 2022 (-10.5%; Feng Tay 2023 financial report, major-customer note) while Nike footwear rose 0.9% in FY2024.
- **[KEY FINDING] When Nike's footwear revenue fell in FY2025, the factory barely cut.** Nike footwear fell 11.7% and Nike footwear units fell 8% ("Unit sales of footwear decreased 8%", FY25 10-K p. 34), but Feng Tay fell only 4.7% in USD (2.8% in NT$), and Yue Yuen pairs rose 16.9% in calendar 2024. There is no factory-level cut matching the timing or size of the FY2025 decline.
- **FY2018 comparison:** Feng Tay dipped -2% to -5% in USD in Q2 to Q4 FY17, one to two quarters before Nike's Q1 FY18 trough, and Nike footwear never fell (FY2018 +5.6%). The 2023 cut was two to four times deeper.
- **Lead:** excluding the COVID base years FY2020 to FY2022, Feng Tay revenue growth correlates 0.68 with Nike footwear growth one quarter later (n = 24) and 0.43 in the same quarter (my arithmetic; `leadlag_correlations.csv`). Feng Tay is a usable one-quarter lead indicator; its Q1 FY27 -8.8% points to continued footwear weakness in Q2 FY27.

**Verdict (my inference):** the factory data reject a total-volume supply cut as the cause of the FY2025 decline: the deep cut happened earlier, as inventory correction, and during FY2025 factory revenue fell far less than Nike's footwear sales. This does not rule out a cut confined to Jordan and classic styles, because supplier totals cannot be split by franchise; style-level import records would decide that. Caveats: supplier revenue is not pairs (it mixes price, currency and about 15% non-Nike business), Yue Yuen counted pairs "produced" before 2018 and "shipped" after, and Yue Yuen quarters are offset one month from Nike's.

## Test 2. Time to markdown for each new release

- **Measures:** days from release to first discount, and discount depth, for each Jordan retro and key lifestyle release, on nike.com and major retailers.
- **Treated vs control:** release cohorts 2023, 2024, 2025, 2026; models Nike cut (AJ1 High) vs models it expanded (AJ3, AJ4).
- **Would disprove "full-price recovery":** 2026 releases reach markdown as fast as or faster than 2024 releases.

**Result (Oct 13, 2026).** Data and scripts: `data/definitive/markdown/`, `scripts/definitive/markdown/`. Today's price for 652 colourways comes from nike.com's public product feed (api.nike.com, opened Oct 13, 2026): 211 of 275 Jordan retro style codes from 2023 to 2026 and 381 control colourways (Pegasus 40 to 42, Vomero 5, Vomero 18, Dunk Low). Shares are my arithmetic over colourways the feed lists as available (listed, not necessarily in stock), collaborations excluded.

| Model, share discounted on nike.com today | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|
| AJ1 High OG | 0 of 4 | 0 of 8 | 0 of 8 | 0 of 7 |
| AJ3 | 0 of 2 | 0 of 1 | 0 of 6 | 0 of 5 |
| AJ4 | 0 of 3 | 1 of 9 | 0 of 5 | 0 of 6 |
| Pegasus 40 to 42 | 9 of 11 | 22 of 22 (median 29% off) | 17 of 17 (30% off) | 16 of 38 (25% off) |
| Vomero 5 | 0 of 2 | 18 of 23 (30% off) | 14 of 17 (30% off) | 7 of 13 (25% off) |
| Dunk Low | 9 of 10 (27% off) | 9 of 11 (31% off) | 6 of 10 (24% off) | 0 of 7 |

- **[KEY FINDING] Nike does not mark down Jordan retros on its own site; it marks down running shoes and Dunks.** 2 of 113 listed colourways in the main retro lines (AJ1 High and Low OG, AJ3, AJ4, AJ5, AJ11, AJ12) are discounted on nike.com today, and 8 of 139 including other Jordan lines, against 22 of 22 Pegasus 41 colourways from 2024. AJ1 High OG "Midnight Navy" is still listed at its full $180, 759 days after release (product feed, Oct 13, 2026); a Wayback capture shows it at full price on day 82 too (https://web.archive.org/web/20241205162606id_/https://www.nike.com/t/air-jordan-1-retro-high-og-midnight-navy-mens-shoes-8xgDfd/DZ5485-401). All 15 Wayback price checks of 2024 and 2026 AJ1 High, AJ3 and AJ4 releases, between day 6 and day 138, were at full price.
- **Read with Tests 3 and 4 (my inference):** on nike.com, Jordan retro prices are held at full price, but the same shoes sit in full size runs weeks after launch (Test 3), many 2025 to 2026 retros were taken off nike.com rather than discounted (product status INACTIVE or HOLD, Test 3), and on the resale market AJ1 High general releases trade 26% to 35% below retail. The price cut for unsold Jordan retros happens off nike.com, at retailers (for example AJ3 Spring 16% to 21% off at Foot Locker and Champs, Test 3) and in resale, not in Nike's own channel. A held list price is therefore not evidence of full-price sell-through.
- **Caveats:** the "available" flag counts listed colourways, so retros that sold out or were removed drop out and bias the Jordan share toward zero; for sold-out items the feed may show full price; control release dates are approximate (feed start date or first capture).
**Time to first markdown (priority subset, final for this run).** 91 colourways: 61 AJ1 High OG, AJ3 and AJ4 general releases from 2024 to 2026, and 15 Pegasus 41 and 15 Vomero 5 colourways from 2024 as controls. Each colourway's nike.com product page captures on the Wayback Machine were searched for the first discounted price; 69 of 91 have at least one dated check (`time_to_markdown_by_colorway.csv` has the windows and source URLs; `time_to_markdown_cohort_table.csv` the table). "Discounted within N days" is counted only where it is known: a discount on or before day N, or a full-price capture on or after day N (my arithmetic).

| Model and release year | Discounted within 30 days | 60 days | 90 days | 180 days | Full price at last check (median day) | Median depth when discounted |
|---|---|---|---|---|---|---|
| AJ1 High OG 2024 | 0 of 7 | 0 of 5 | 0 of 4 | n/a | day 91 | none |
| AJ1 High OG 2025 | 0 of 4 | 0 of 4 | 0 of 3 | 0 of 1 | day 103 | none |
| AJ1 High OG 2026 | 0 of 3 | 0 of 1 | 0 of 1 | n/a | day 54 | none |
| AJ3 2024 and 2025 | 0 of 6 | 0 of 5 | 0 of 4 | n/a | day 75 to 101 | none |
| AJ4 2024 | 0 of 3 | 0 of 3 | 0 of 3 | 0 of 1 | day 168 | 25% (one colourway, by day 210) |
| Pegasus 41 2024 (control) | 0 of 15 | 0 of 14 | 0 of 14 | 3 of 12 | none at full price | 30% |
| Vomero 5 2024 (control) | 0 of 14 | 0 of 12 | 1 of 10 | 4 of 12 | 3 still full | 29% |

- **On nike.com, no AJ1 High OG, AJ3 or AJ4 release from 2024 to 2026 was seen discounted within 90 days**, while the running controls start marking down from about day 50 (Vomero 5 HF5493-600 was 31% off by day 75: https://web.archive.org/web/20241003020836id_/https://www.nike.com/t/zoom-vomero-5-mens-shoes-MgsTqZ/HF5493-301). The only Jordan markdowns found are two AJ4 colourways at about 25%, none on AJ1 High.
- **The pre-registered disproof is not met on this sample: 2026 releases are not marking down faster than 2024 releases on nike.com.** But the sample is thin (only one 2026 release checked past day 60), and Nike's own site is where it holds price, so this mainly confirms the pricing policy found above.
- **[KEY FINDING] Retailers are already discounting 2026 Jordan retros that nike.com sells at full price.** Foot Locker, Oct 13, 2026: AJ3 IF4396-100 (2026) at $169.99 vs $215 list (21% off) and CK9246-400 at $159.99 vs $205 (22% off); 2025 and 2026 women's AJ4 colourways 18% to 23% off; AJ1 High OG IH4363-100 (2025) at $139.99 vs $185 (24% off) (`footlocker_priority_20261013.csv`, footlocker.com pages opened; discounts my arithmetic). 6 of the 13 Jordan retros Foot Locker lists from this sample are discounted, against 0 of 61 seen discounted within 90 days on nike.com.
- **Caveats:** Wayback timeouts left 22 colourways with no dated check; a Jordan that sold out never shows a markdown, so "no markdown" can also mean sold through (Test 3 shows most did not); the search assumes a markdown stays on once taken; control release dates are approximate.

## Test 3. Size runs left after launch

- **Measures:** which sizes remain in stock days and weeks after a release at nike.com, Foot Locker, Finish Line and JD. Broken size runs mean sold through; full size runs mean oversupply.
- **Treated vs control:** holiday 2026 retros (after the October 2026 cut) vs earlier releases.
- **Would disprove "supply cut is working":** full size runs still in stock two to four weeks after holiday 2026 launches.

**Result (Oct 13, 2026; first run, decisive re-runs scheduled).** A re-runnable tracker (`scripts/definitive/size_tracker/size_tracker.py`, see its README) recorded size-level stock and price for 73 Jordan retros released Oct 2025 to Oct 2026 plus 10 controls at nike.com (api.nike.com product feed; a size counts only when the product is ACTIVE and past its start date), Foot Locker and Champs; Finish Line and JD US blocked automated access (HTTP 403). Results in `data/definitive/sizes/size_runs_per_shoe_20261013.csv` (per retailer, per size: `size_runs_combined_20261013.csv`); Foot Locker history from Wayback captures in `fl_history_summary_final.csv`. All shares are my arithmetic.

| Shoe | Days since release | Share of sizes 7 to 13 in stock (Nike / Foot Locker / Champs) | Core sizes 9 to 11 | Price vs retail |
|---|---|---|---|---|
| AJ1 High OG Royal (first release after the Oct 1 cut) | 3 | 1.00 / 0.85 / 0.77 | all in stock | full price ($185) |
| AJ12 Bucks | 31 | 0.85 / 0.77 / 0.77 | all | full price |
| AJ4 Rare Air Tour Yellow | 38 | 1.00 / 1.00 / 1.00 | all | full price ($220) |
| Wmns AJ1 Nails & Grails | 41 | 1.00 / 0.91 / 0.82 | all | full price |
| AJ1 High Love The Game | 73 | 0.92 / 0.85 / 0.77 | all | full price |
| AJ3 Spring | 199 | off nike.com / 0.77 / 0.77 | all | 16% to 21% off |
| AJ4 Toro Bravo | 136 | off nike.com / 0 / 0 | none | sold through |
| Control: Vomero 5 | 1,108 | 1.00 / 0.77 / 0.92 | all | full price |

- **[KEY FINDING] Jordan retros released just before the cut are still sitting in full size runs at full price four to ten weeks after launch.** AJ4 Rare Air Tour Yellow has every size from 7 to 13 in stock at all three retailers on day 38; AJ12 Bucks has 10 to 11 of 13 sizes on day 31 (live product data, Oct 13, 2026). That is the oversupply pattern the test was built to detect, measured directly on the shelf.
- **History says the same:** Foot Locker captures show full or near-full runs about 30 days after release for AJ1 Black White 2.0 (12 of 13 sizes, day 24), AJ1 Black Gold (12/13, day 30), AJ3 Cement Grey (13/13, day 31), AJ5 White Black (13/13, day 22) and AJ12 French Blue (12/13, day 32). The only fast sell-through found was AJ4 White Cement 2025 (1 of 13 sizes left on day 20). Nine of about 50 shoes had usable captures.
- **Not yet decided for the post-cut period.** The AJ1 Royal, released October 10, is in full runs at full price on day 3, which is too early to judge. **Re-run the tracker on about October 24 and November 7** (days 14 and 28). If it still shows full runs then, the pre-registered disproof is met. Holiday releases to track next: AJ12 Fireside (Oct 24), AJ4 Bred (about Nov 27) and AJ11 Space Jam (Dec 12) (secondary: release-date reports).
- **Caveats:** "in stock" means a size can be bought online, not how many pairs exist; a retailer not listing a shoe may mean it sold out or never carried it; Finish Line and JD are not covered; some retail prices in the GOAT list are wrong (AJ12 Bucks is $215 on nike.com, not $200).

## Test 4. Resale panel: the same shoes re-priced over time

- **Measures:** resale price to retail for the same 247 shoes at several dates (historical captures plus the October 13, 2026 baseline in `data/jordan_resale_goat_20261013.csv`), and the depth of sellers listing each shoe.
- **Treated vs control:** AJ1 High (supply cut from 2024) vs AJ3 and AJ4 (supply raised): difference in differences.
- **Would disprove "scarcity works":** AJ1 premiums do not improve relative to AJ3 and AJ4 after the cut.

**Directional result (Oct 13, 2026; coverage too thin to decide).** Historical prices come from StockX product pages captured by the Wayback Machine, accepted only when StockX's style code matches the baseline (`data/definitive/resale_panel/resale_panel_stockx_wayback.csv`, each row with capture URL and timestamp; estimates in `did_results.csv` and `did_cells.csv`; scripts in `scripts/definitive/resale_panel/`). Measure: median lowest ask across US sizes 7 to 13 against retail (my arithmetic). Coverage: 19 shoes and 46 dated points (14 AJ1 High OG, 5 AJ3, **no AJ4**), because web.archive.org kept dropping connections.

| Half-year | AJ1 High OG, mean premium (shoes) | AJ3, mean premium (shoes) |
|---|---|---|
| 2023 H2 | +18% (4) | +3% (2) |
| 2024 H1 | -16% (6) | -7% (2) |
| 2024 H2 | -30% (6) | +7% (3) |
| 2025 H1 | -28% (4) | +11% (3) |
| 2025 H2 | -20% (7) | +8% (1) |

- **Difference in differences, shoe and half-year effects:** AJ1 High after 2024 relative to AJ3 = **-22.7 points**, shoe-clustered bootstrap 95% interval -48.3 to +3.5 points (42 observations, 18 shoes; only 6 AJ1 and 2 AJ3 shoes are seen both before and after). Moving the cut date to 2025 H1 gives -20.6 points. Every estimate has AJ1 doing *worse* relative to AJ3 after its supply cut, which is the direction of the disproof, but the interval includes zero and there is no AJ4 control, so the test is **not decided**.
- **Same-shoe example:** AJ1 High OG "Mauve" ($180 retail) had a median StockX ask 41% below retail on Jan 6, 2024 and 56% below on Jul 29, 2025 (https://web.archive.org/web/20240106094451id_/https://stockx.com/air-jordan-1-retro-high-og-sky-j-mauve). The two post-cut AJ1 releases covered trade 38% to 40% below retail after about a year.
- **Overhang:** StockX ask counts per shoe fall as shoes age (AJ1 High median 1,759 asks in 2023 H1 to 396 in 2025 H2), so listings are clearing over time rather than growing. On GOAT today, 86% of AJ1 High sizes have a lowest ask below retail, against 53% for AJ3 and 43% for AJ4 (`goat_depth_20261013.csv`; my arithmetic).
- **Baseline stability:** re-pulling 40 baseline shoes two hours later moved the median last sale by 0.0% (largest change 5.1%; `goat_drift_recheck_20261013.csv`).
- **To finish:** re-run `cdx_shoe.py` and `fetchcaps.py` (they resume, AJ4 and AJ3 first), then `panel.py` and `did.py`, at a time when no other job is using web.archive.org.

## Test 5. Units vs price from Nike's own filings

- **Measures:** every footwear and apparel unit and average selling price change Nike states in its 10-Qs and 10-Ks, by segment and quarter, FY2017 to Q1 FY2027.
- **Treated vs control:** reset periods (FY2018, FY2025 to FY2027) vs normal periods; North America vs Greater China.
- **Would disprove "deliberate supply cut":** units falling only after ASP falls (discounting first), or units flat while revenue falls.

**Result (Oct 13, 2026).** Every unit and ASP statement in all 10 10-Ks and 30 10-Qs from FY2017 to Q1 FY2027 was extracted: 694 rows by quarter, segment and category, each with filing, printed page and verbatim quote (`data/definitive/nike_units_asp_tidy.csv`; episode tags in `data/definitive/units_asp_episode_patterns_DERIVED.csv`; scripts in `scripts/definitive/units_asp/`). In Nike's filings "ASP" is usually the percentage-point contribution of price per pair to revenue growth, not a percent change.

Footwear, units change % / ASP contribution in points:

| Period | North America | Greater China | NIKE Brand | Converse | Source |
|---|---|---|---|---|---|
| Q1 FY18 | 0 / -3 (discounts) | +13 / -3 | +3 / -2 | -17 / 0 | Q1 FY18 10-Q pp. 22 to 31 |
| Q2 FY18 | -11 / +4 | +17 / 0 | 0 / +3 | -12 / +5 | Q2 FY18 10-Q |
| Q2 FY22 | +7 / +6 | -20 / -5 | -7 / +6 | +5 / +9% | Q2 FY22 10-Q |
| Q2 FY23 | +37 / +2 | +15 / +6 | +28 / +8 | +6 / +5% | Q2 FY23 10-Q |
| Q2 FY24 | -17 / +12 | +3 / 0 | -6 / +6 | -13 / 0% | Q2 FY24 10-Q |
| Q1 FY25 | -15 / +1 | -1 / -1 | -10 / 0 | -11 / -3% | Q1 FY25 10-Q p. 25 (NA) |
| Q2 FY25 | -6 / -8 (discounts) | -9 / -5 | -7 / -5 | -12 / -6% | Q2 FY25 10-Q |
| Q2 FY26 | +14 / -5 (channel mix) | -20 / 0 (lower discounts) | 0 / -1 | -26 / -5% | Q2 FY26 10-Q p. 32 (GC) |
| Q1 FY27 | +2 / -1 | -26 / 0 (lower discounts) | -5 / -1 | -34 / +6 (lower discounts) | Q1 FY27 10-Q pp. 26 to 28 |

Verdict by episode (my inference from the table):
- **FY2018 started with discounting, not a supply cut.** "Unit sales of footwear for the first quarter of fiscal 2018 were flat, while lower ASP per pair reduced footwear revenues by approximately 3 percentage points primarily due to lower full-price ASP, driven by product mix and higher discounts" (North America, Q1 FY18 10-Q p. 26). Units fell only in Q2 and Q3 (-11%, -9%) with ASP rising. **So the FY2018 analog used for Jordan was a discount-then-cut sequence, not a pure supply cut.**
- **FY2023 glut: volume clearance first, cut second.** North America footwear units rose 10%, 37% and 26% in Q1 to Q3 FY2023; the cut came in Q1 and Q2 FY2024 (units -10%, -17%, ASP +8 and +12 points).
- **FY2025 to Q1 FY2027, North America: units fell first** (Q1 FY2025 units -15%, ASP +1 point "due to strategic pricing actions, partially offset by higher discounts", Q1 FY25 10-Q p. 25), then discounting (Q2 FY2025 ASP -8 points), then **more units at lower ASP in FY2026** (+5% to +14% units, -5 points), mainly from channel mix toward wholesale.
- **[KEY FINDING] Only Greater China and Converse show the deliberate supply-cut signature now.** Greater China: "Unit sales of footwear decreased 26%, while ASP per pair was flat as lower discounts were offset primarily by channel mix" (Q1 FY27 10-Q p. 28), after "Unit sales of footwear decreased 20%, while ASP per pair was flat as channel mix was offset by lower discounts" (Q2 FY26 10-Q p. 32). Converse: units -34% with ASP +6 points on lower discounts in Q1 FY2027. **North America, the region the Jordan retro cut targets, is still selling more pairs at lower prices**, and EMEA footwear cites "channel mix and higher discounts" (Q1 FY27 10-Q p. 27).

What this test cannot separate: units falling with flat or rising ASP is consistent with a deliberate shipment cut *and* with buyers taking fewer pairs at higher prices. Tests 1 to 3 (factory pairs, time to markdown, size runs) are designed to split those.

## Log

| Date | Change |
|---|---|
| 2026-10-13 | Document created; five tests launched. |
| 2026-10-13 | Test 5 (units vs price) reported: 694 filing statements, two key findings. |
| 2026-10-13 | Test 1 (factory orders) reported: Feng Tay, Pou Chen, Yue Yuen series 2013 to 2026; chart 20. |
| 2026-10-13 | Test 3 (size runs) reported: 83 shoes at three retailers, tracker script committed; decisive re-runs on Oct 24 and Nov 7. |
| 2026-10-13 | Test 2 (time to markdown) reported: nike.com prices for 652 colourways, first-markdown windows for 91, Foot Locker prices today. |
| 2026-10-13 | Test 4 (resale panel) directional: AJ1 vs AJ3 difference -22.7 points (95% interval -48.3 to +3.5), no AJ4 yet; interim folder retired. |
