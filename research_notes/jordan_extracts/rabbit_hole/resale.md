# Jordan retro resale premiums, 2023 to Oct 2026 (GOAT snapshot, 13 Oct 2026)

Dataset: `resale_dataset.csv` (277 rows; 249 general releases, or GRs, released 2023 to 2026, plus collabs and 1 reference shoe from 2022). Raw JSON, scripts and logs are in `raw/` and `../scripts/`.

## Method
- **Release list:** GOAT's own search API (`https://www.goat.com/web-api/consumer-search/get-product-search-results?...queryString=air+jordan+4+retro...`), queried through a headless Chromium session. Queries covered AJ1 High OG, AJ1 Low OG, AJ1 Mid, AJ3, AJ4, AJ5, AJ6, AJ11, AJ12 and AJ13, 6 pages of 48 results each. Each result gives the GOAT name, release date and retail price. I dropped GS/PS/TD sizes, samples, slides and golf models, and kept release dates from 2023-01-01 to 2026-10-13. I also searched 9 style codes by hand (2026 AJ1 Highs that were missing, plus Lost & Found DZ5485-612 as a 2022 reference).
- **Resale price:** GOAT `buy_bar_data` JSON for each shoe (`https://www.goat.com/web-api/v1/product_variants/buy_bar_data?productTemplateId=<id>&countryCode=US`; the URL is stored in each CSV row). It gives the lowest ask and last sale for each size, new with good box. Observed 2026-10-13 between 19:54 and 20:10 UTC. **VERIFIED** (JSON opened).
- **Size basis:** the main measure is the median of each size's last sale across US 7 to 13. Women's models use women's sizing. I also record the size 10 lowest ask, the size 10 last sale and the median lowest ask.
- **Retail price:** from Sole Retriever calendar cards (pages opened 2026-10-13, URL in `sr_url`) for 153 rows. For the other 124 rows I used GOAT's listed retail price, which is labeled in `retail_source`. The two sources differ on 32 shoes. Most of those gaps are $5, from Nike's 2025 price increases. Two gaps are larger and flagged: AJ1 Low OG 'Laser' ($125 on GOAT vs $165 on Sole Retriever) and AJ1 Mid 'White Black'.
- **Premium:** resale / retail - 1. **DERIVED.**
- **Grouping:** a shoe counts as a GR when it is not a collab or special edition (regex flag `collab_or_special`). The `too_new_lt60d` flag marks 11 shoes released fewer than 60 days before the snapshot.

## Results: GR median premium by line and release year (n, median, share below retail)
| Line | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|
| AJ1 High OG | 15, -26%, 93% | 9, -28%, 100% | 10, -35%, 100% | 7, -30%, 100% |
| AJ1 Low OG | 9, -3%, 56% | 14, -4%, 57% | 8, +4%, 50% | 7, -31%, 57% |
| AJ1 Mid | 3, +26% | 5, -2% | 3, +10% | 3, -19% |
| AJ3 | 7, +24%, 14% | 7, +11%, 29% | 10, -17%, 80% | 7, -22%, 71% |
| AJ4 | 6, +18%, 17% | 10, +24%, 10% | 12, +4%, 33% | 7, -20%, 100% |
| AJ5 | 6, +27% | 5, +22% | 9, -6% | 4, +12% |
| AJ11 (high) | 2, +4% | 3, +9% | 7, +4% | 1, -18% |
| AJ12 | 3, +47% | 4, +39% | 4, +20% | 3, +3% |
| AJ13 | 4, +32% | 3, +17% | 0 | 2, -17% |
| All GR | 64, +13%, 41% | 69, +6%, 45% | 68, -5%, 57% | 46, -19%, 76% |

Within AJ1 High OG, men's GRs were -23% (2023), -24% (2024), -31% (2025) and -29% (2026); women's were -32%, -28%, -36% and -30%. The size 10 lowest ask shows the same pattern (AJ1 High OG -34%, -29%, -45%, -33%). Reference points: Lost & Found (2022, DZ5485-612) is +62%. The newest pair, Royal 2026 (IQ5495-005, released 2026-10-10, after the 1 Oct 2026 supply-cut statement), is -9% after 3 days. AJ1 High '85 GRs (n=4) and AJ1 Low OG collabs (Travis Scott and others, median +220%) are the only AJ1 groups clearly above retail.

## Does the AJ1 supply cut show up in resale prices?
1. **The AJ1 High OG level has not recovered.** The 2025 to 2026 releases (median about -30% to -35%) trade at or below the 2023 releases (-26%). Every GR AJ1 High OG released after 2023 is below retail on GOAT. This snapshot contains no recovery signal for the model that was cut first.
2. **The relative pattern partly fits the thesis.** The models not yet cut deteriorated much faster. The AJ4 cohort went from +18% to +24% (2023 to 2024) to -20% (2026), and AJ3 went from +24% to -22%. The AJ4 minus AJ1 High gap shrank from about 44pp (2023 cohort) to about 10pp (2026 cohort). That fits retro volume shifting from AJ1 into AJ3 and AJ4 in 2024 to 2025 and those lines then hitting the same ceiling. It does not show that cutting AJ1 restored a premium.
3. **The evidence cannot separate a deliberate supply cut from lower sell-through.** Resale price depends on units released relative to buyers at retail price. We have no unit counts by SKU, so a flat -30% for AJ1 High fits two readings: cuts too small or too recent to matter, or demand per unit falling as fast as supply. The one dated StockX number for this line (Altan via Reuters, +4% in 2023, near release) is above our current 2023-cohort figure (-26%), so those pairs have kept losing value after release.

## Published indices after 2023 (verified on opened pages)
- **SneakerPing, "Sneaker Resale Market Report", data as of 18 Aug 2026** (https://sneakerping.com/sneaker-resale-market-report, opened 2026-10-13). **VERIFIED.**
  - Sample: 3,538 releases from 18 Aug 2024 to 16 Aug 2026, priced from the median of recorded sales on StockX, GOAT and eBay. Each release counts once, regardless of size.
  - Jordan: 605 releases, 70.7% below retail, median -20.0%.
  - By model line: Jordan 3 (69) 84.1% below retail, -25.8%; Jordan 4 (134) 75.4%, -27.3%; Jordan 1 (168, High, Low and Mid **combined**) 73.2%, -22.3%; Jordan 11 (46) 69.6%, -12.7%; Jordan 5 (41) 51.2%, -1.1%; Jordan 12 (24) 45.8%, +3.9%.
  - There is **no split by release date or by High/Low/Mid**, so it cannot test whether AJ1 recovered.
  - The report says: "The pattern tracks release volume" (that is the report's opinion).
  - The "700+ Jordan styles in 2022 and 2023" figure is **not** SneakerPing's. BallerAlert (https://balleralert.com/sneaker-resale-culture-market-decline/, opened) attributes it to WSJ reporting. That number is UNVERIFIED at source.
- **StockX Big Facts: Current Culture Index (2026), via SGB Media 12 Jan 2026** (https://sgbonline.com/stockx-2025-big-facts/, opened 2026-10-13). **VERIFIED.**
  - Verbatim: "After a period of softness, Nike and Jordan show early signs of recovery, with average sneaker prices up 5 percent and 6 percent year-over-year, respectively."
  - StockX opinion, verbatim: "a more disciplined release strategy for core Jordan silhouettes should further boost the brand."
  - There is no model-level Jordan detail. The StockX original returned a Cloudflare 403. The 6% is an average sale price, not a premium to retail, so it can reflect a shift in mix.
- **StockX product page, AJ1 High OG 'Flight Club'** (search snippet only): 3-month average sale $117 against $185 retail (-37%). GOAT median last sale here is $134 (-28%), so the two agree on direction. **SNIPPET ONLY.**
- **Not found:** any post-2023 Altan Insights AJ1 series. No Cowen/TD Cowen, Jefferies or Piper resale notes or GOAT annual report with Jordan numbers turned up on pages I could open.

## How this compares with SneakerPing
For releases from Aug 2024 to Aug 2026, collabs included, my medians are less negative: AJ1 (all) -11%, AJ4 +3%, AJ3 -17%, AJ11 -6%. My sample is GOAT search results sorted by relevance, which favors popular SKUs. It uses the median across sizes rather than one latest sale, and leaves out kids' sizes. My numbers are probably biased upward. SneakerPing's are the broader census.

## Caveats
- **Single snapshot.** Premiums are compared across release cohorts at different ages, and older GRs can drift either way. A real test needs the same SKUs priced over time (a GOAT or StockX history, or a re-pull every quarter).
- **Last sale has no date.** For thin sizes it may be stale.
- **Sample counts.** Model-year cells with n < 5 are only directional.
- **Retail prices.** Prices taken from GOAT were not all cross-checked. A $5 to $10 error moves the premium by about 3 to 5pp.
- **Blocked sources** (2026-10-13; Cloudflare on the site's side, not the proxy):
  - StockX: 403 for curl and headless browser.
  - Flight Club, KicksCrew, eBay, Sneaker News, Kicks On Fire, Sneaker Bar Detroit: 403.
  - Nice Kicks: 503.
  - KicksDB: 500; kicks.dev API: 401 (needs a key).
  - restocks.net: TLS error; solecollector.com: 502.
  - Sole Retriever: 403 after repeated loads; worked with a fresh browser context and 20 s gaps.
  - GOAT: began returning 403 after about 260 calls. The remaining 75 lower-priority IDs (mostly AJ1 Mid and collabs) were left out, except 14 Mids retried later.
