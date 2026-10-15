# P_ALTDATA: Alternative data on Nike consumer demand versus peers (2019 to October 2026)

> Repository copy: the 18 CSVs listed below are in `data/altdata/` (same file names). One App Store app name contained an em-dash and was changed to a hyphen.

Pulled 2026-10-13. All downloads were treated as untrusted data and parsed with `python3 -I`. Raw files sit in `altdata/raw_*` subfolders; scripts in `scratchpad/altdata_scripts/`. Nike fiscal year ends May 31 (FQ1 = Jun to Aug, FQ2 = Sep to Nov, FQ3 = Dec to Feb, FQ4 = Mar to May).

## 1. What was pulled, and what worked

| # | Source | Method | Result | Range |
|---|---|---|---|---|
| 1 | Google Trends (trends.google.com) | `pytrends` 4.9 `interest_over_time`, timeframe `2019-01-01 2026-10-12`, monthly, geo `US` and worldwide (`''`), 5 terms per batch, 15 to 20 s sleeps | WORKED (one 429 per run, cleared by a 60 s backoff). 7 brand/product batches per geo, plus 1 control batch per geo, plus a daily US check for Feb 15 to Jul 15 2026 | Jan 2019 to Oct 2026 (Oct 2026 partial) |
| 2 | Wikimedia pageviews REST API (wikimedia.org/api/rest_v1/metrics/pageviews/per-article) | urllib, descriptive User-Agent, one request every 45 s with retries | SEE SECTION 5 (heavy 429 rate limiting on the shared egress IP) | Jan 2019 to Sep 2026 |
| 3 | Apple App Store (itunes.apple.com/lookup, /search; itunes.apple.com/{cc}/rss/topfreeapplications/genre=6024 Shopping and genre=6013 Health and Fitness) | curl, 2 to 8 s sleeps | WORKED for lookup, search (some 403 retries) and the legacy iTunes RSS top 100. rss.applemarketingtools.com redirected (301) to rss.marketingtools.apple.com which returned 504. China lookup of the US app IDs returned no rows (China apps are separate listings) | Snapshot 2026-10-13 only |
| 4a | FRED (fred.stlouisfed.org/graph/fredgraph.csv) for Census retail sales and BLS CPI | curl | WORKED: MRTSSM451USS, MRTSSM448USS, MRTSSM4482USS, MRTSSM44812USS, RSSGHBMS, RSCCAS, CUSR0000SEAE (footwear CPI), CPIAPPSL, CPIAUCSL. Men's/women's/boys' footwear CPI sub-series IDs tried returned 404 | Jan 2019 to Jul or Aug 2026 |
| 4b | Internet Archive Wayback (web.archive.org CDX + `id_` raw snapshots) of `nike.com/w/sale-3yaep` (US Sale wall) | CDX monthly collapse, then raw snapshot; parsed embedded JSON `"totalResources"` (product count) | WORKED, flaky (connection resets, 503; retried). 75 monthly counts | Aug 2019 to Oct 2026 |
| - | stockx.com, goat.com, reddit.com | not retried (403 per caller's prior test) | BLOCKED | - |
| - | China search (Baidu Index) | not attempted; Google is not used in China | NOT COVERED | - |

Key caveats for Google Trends:
- Values are 0 to 100 relative indices within each 5-term request, rounded to integers. Small terms (Hoka, On, Asics, Vomero, Pegasus, "Nike running shoes") have low integer values in Nike-anchored batches, so their percentage changes are noisy. To improve resolution, On was chained through a Hoka-anchored batch (B5) and rescaled to Nike units via Hoka. Re-pulling the same batch moved about 6 of 94 monthly values by 1 point (sampling noise).
- Search terms, not Google "topics", were used. "On running" plus "On Cloud" is a proxy for On; "Hoka" and "Puma" can pick up unrelated meanings; "Jordan" includes the country and people.
- A first worldwide pull silently returned US data (pytrends session reuse). It was discarded and re-pulled with a fresh session per request; the worldwide files used here are verified different from the US files.
- Category-wide spike, April to June 2026: "Nike", "adidas", "Hoka", generic "shoes" and "sneakers" all jumped (US "shoes" monthly 12 to 19, weekly peak mid April), while "Walmart", "Amazon" and "weather" did not. Daily data show a smooth multi-week rise from late March and decay by mid July, not a one-day event. Census sporting goods store sales stepped up at the same time (+4.7% YoY in March to +11.7% in April 2026), so it may be a real category surge, but the cause is not identified here. Calendar Q2 2026 (and Nike FQ4 FY2026) absolute YoY search changes are therefore distorted and should not be read as Nike-specific strength. Share-of-search measures largely net this out.

## 2. Nike share of combined brand search (Google Trends)

Share = Nike / (Nike + adidas + New Balance + Asics + Hoka + On + Lululemon + Puma), quarterly averages of monthly indices in Nike units. Calendar quarters; 2026Q3 is the last full quarter.

| Quarter | US Nike share % | World Nike share % | US adidas % | World adidas % | World On % | World NB % |
|---|---|---|---|---|---|---|
| 2019Q1 | 54.7 | 49.4 | 20.6 | 29.9 | 2.3 | 4.2 |
| 2021Q1 | 56.8 | 53.7 | 16.3 | 23.1 | 2.3 | 4.9 |
| 2022Q1 | 51.7 | 52.1 | 13.9 | 21.9 | 3.0 | 6.5 |
| 2023Q1 | 48.9 | 49.6 | 12.2 | 21.0 | 3.2 | 8.6 |
| 2024Q1 | 42.1 | 42.5 | 13.3 | 24.6 | 3.8 | 9.8 |
| 2025Q1 | 40.6 | 38.6 | 13.1 | 24.0 | 4.5 | 10.4 |
| 2025Q2 | 37.8 | 37.1 | 13.7 | 24.6 | 4.6 | 10.5 |
| 2025Q3 | 36.2 | 36.0 | 14.9 | 24.0 | 5.9 | 10.5 |
| 2025Q4 | 38.4 | 36.6 | 13.1 | 23.8 | 6.4 | 10.2 |
| 2026Q1 | 38.8 | 35.1 | 14.8 | 25.1 | 6.9 | 10.6 |
| 2026Q2 | 36.5 | 34.1 | 19.2 | 26.1 | 6.1 | 11.7 |
| 2026Q3 | 39.0 | 35.3 | 16.3 | 26.0 | 6.4 | 10.1 |

Trailing 12-month Nike share (monthly file): US peaked at 56.1% (12 months to Apr 2021) and troughed at 37.3% (12 months to May 2026); worldwide peaked at 53.4% (Dec 2021) and troughed at 35.3% (Aug 2026). US monthly Nike share was up year on year in Jun to Oct 2026 (+1.7, +0.7, +3.6, +4.5, +2.9 pp; Oct partial). Worldwide it turned flat to slightly positive only in Sep and Oct 2026 (+0.3, +0.7 pp).

## 3. Year-over-year change in search interest by calendar quarter (%)

| Geo | Quarter | Nike | adidas | New Balance | Asics | Hoka | On | Lululemon | Puma | generic "shoes" |
|---|---|---|---|---|---|---|---|---|---|---|
| US | 2024Q3 | -8 | +37 | +16 | +100 | -5 | +13 | -6 | +8 | 0 |
| US | 2024Q4 | -11 | +11 | +9 | +70 | +5 | +13 | +6 | +8 | -5 |
| US | 2025Q1 | -4 | -2 | -4 | +45 | -5 | +8 | +4 | 0 | -9 |
| US | 2025Q2 | -7 | -10 | -2 | +12 | -9 | +16 | +16 | +8 | -8 |
| US | 2025Q3 | -6 | -7 | 0 | +5 | -5 | +35 | +33 | +31 | +3 |
| US | 2025Q4 | -2 | 0 | +2 | +12 | 0 | +35 | +1 | +14 | +3 |
| US | 2026Q1 | +8 | +28 | +4 | +6 | +5 | +47 | -4 | +46 | +12 |
| US | 2026Q2* | +75 | +155 | +74 | +78 | +62 | +67 | +4 | +250 | +58 |
| US | 2026Q3 | +6 | +8 | -13 | 0 | 0 | +6 | -30 | +12 | +5 |
| World | 2024Q3 | -8 | +21 | +17 | +47 | +25 | +18 | +10 | +5 | +3 |
| World | 2024Q4 | -12 | +7 | +13 | +56 | +27 | +28 | +14 | +5 | +7 |
| World | 2025Q1 | -9 | -2 | +6 | +37 | +8 | +18 | +27 | +5 | -3 |
| World | 2025Q2 | -9 | -8 | +8 | +32 | +7 | +20 | +23 | +5 | 0 |
| World | 2025Q3 | -2 | +2 | +18 | +36 | +27 | +64 | +39 | +10 | +6 |
| World | 2025Q4 | -4 | +9 | +14 | +28 | +29 | +66 | +9 | +5 | +9 |
| World | 2026Q1 | +5 | +21 | +18 | +23 | +21 | +79 | +4 | +15 | +32 |
| World | 2026Q2* | +43 | +66 | +75 | +38 | +50 | +108 | +15 | +77 | +63 |
| World | 2026Q3 | +2 | +13 | 0 | +6 | 0 | +14 | -19 | +2 | +24 |

\* Distorted by the April to June 2026 category-wide search spike (Section 1).

Nike YoY minus peer YoY, percentage points (negative = Nike lagging):

| Geo | Quarter | vs adidas | vs NB | vs Asics | vs Hoka | vs On | vs Lululemon | vs Puma |
|---|---|---|---|---|---|---|---|---|
| US | 2025Q1 | -2 | 0 | -49 | +1 | -12 | -8 | -4 |
| US | 2025Q2 | +3 | -5 | -20 | +2 | -23 | -23 | -15 |
| US | 2025Q3 | +1 | -6 | -11 | -1 | -41 | -39 | -37 |
| US | 2025Q4 | -2 | -4 | -13 | -2 | -36 | -3 | -16 |
| US | 2026Q1 | -20 | +4 | +2 | +3 | -39 | +12 | -38 |
| US | 2026Q3 | -1 | +20 | +6 | +6 | 0 | +36 | -5 |
| World | 2025Q1 | -7 | -15 | -46 | -16 | -27 | -36 | -14 |
| World | 2025Q2 | -1 | -17 | -41 | -16 | -28 | -32 | -14 |
| World | 2025Q3 | -4 | -21 | -38 | -29 | -67 | -42 | -12 |
| World | 2025Q4 | -13 | -18 | -32 | -33 | -70 | -13 | -9 |
| World | 2026Q1 | -15 | -13 | -18 | -16 | -74 | +2 | -9 |
| World | 2026Q3 | -11 | +2 | -4 | +2 | -12 | +21 | 0 |

Nike franchise and product terms, YoY % (low-volume terms are noisy):

| Geo | Quarter | "Nike shoes" | Air Force 1 | Dunk | Jordan 1 | Air Max | Vomero | Pegasus |
|---|---|---|---|---|---|---|---|---|
| US | 2024Q3 | +4 | -22 | -35 | -45 | -12 | n/m | 0 |
| US | 2025Q1 | -4 | -25 | -29 | -20 | -19 | +150 | -14 |
| US | 2025Q3 | -8 | -14 | -27 | -17 | 0 | +75 | +17 |
| US | 2025Q4 | -11 | 0 | -20 | -33 | -7 | +75 | 0 |
| US | 2026Q1 | 0 | +17 | 0 | -17 | +38 | +40 | +17 |
| US | 2026Q3 | +4 | +17 | 0 | -20 | +7 | +14 | -14 |
| World | 2025Q3 | +7 | -11 | -21 | -20 | +11 | +100 | +13 |
| World | 2026Q1 | +14 | -11 | -8 | -11 | +19 | +75 | +25 |
| World | 2026Q3 | +13 | +12 | -18 | 0 | 0 | +17 | -12 |

Reading: the lifestyle franchise drag (Dunk, AF1, Jordan 1 down 20% to 45% YoY through 2024) has faded to roughly flat; Vomero search grew strongly from a tiny base through 2025 (consistent with the running reset), but these terms are low-volume.

Nike vs generic "shoes" (control) ratio, YoY %: US 2025Q3 -8, 2025Q4 -12, 2026Q1 -6, 2026Q3 0; World 2025Q3 -6, 2025Q4 -14, 2026Q1 -22, 2026Q3 -20. Globally Nike is still losing share of footwear-related search intent; in the US it has stopped losing.

## 4. Correlation with NIKE Brand Digital revenue

Digital revenue from Nike 10-K/10-Q text as recorded in this repo's `data/nike_filing_facts.csv` (FY2019 3.8, FY2020 5.5, FY2021 9.1, FY2022 10.7, FY2023 12.6, FY2024 12.1, FY2025 9.6, FY2026 8.6 $B; quarterly FY2024 Q1 to FY2027 Q1, Q4 derived as FY minus 9 months). FY2023 was later recast to $12.4B and FQ1 FY2026 to $2.1B; the original figures are used here.

| Fiscal quarter | US Nike search YoY % | World Nike search YoY % | US Nike share YoY pp | Digital $B | Digital YoY % |
|---|---|---|---|---|---|
| FY25 Q1 | -7.2 | -7.3 | -6.3 | 2.3 | -20.7 |
| FY25 Q2 | -12.8 | -12.1 | -5.0 | 2.8 | -20.0 |
| FY25 Q3 | -7.6 | -12.5 | -3.8 | 2.5 | -16.7 |
| FY25 Q4 | -4.3 | -4.9 | -1.8 | 2.0 | -25.9 |
| FY26 Q1 | -2.4 | -5.4 | -2.4 | 2.0 | -13.0 |
| FY26 Q2 | -4.5 | -3.4 | -3.2 | 2.4 | -14.3 |
| FY26 Q3 | +1.8 | 0.0 | -1.3 | 2.3 | -8.0 |
| FY26 Q4* | +59.1 | +36.1 | -2.8 | 1.8 | -10.0 |
| FY27 Q1 | +18.3 | +7.8 | +1.9 | 1.8 | -10.0 (-14 vs recast $2.1B) |

Correlations (n = 9 quarters, FY25 Q1 to FY27 Q1): Nike search YoY vs digital YoY r = 0.54 (US and World); US Nike share YoY vs digital YoY r = 0.51; World share r = 0.40. Fiscal-year levels FY2020 to FY2026 (n = 7): r = 0.43 (US), 0.71 (World); FY YoY (n = 6): r = 0.20 (US), 0.54 (World). Quarterly levels r = -0.26 (US). These are small samples with one distorted quarter; treat as directional only. Search held up far better than digital revenue: FY2025 search fell 8% (US) while digital fell 21%, consistent with Nike deliberately cutting promotional digital traffic and shifting to wholesale rather than with brand attention collapsing by the same amount.

## 5. Wikipedia pageviews

Source: `https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/{title}/monthly/2019010100/2026101300`, plus the en.wikipedia aggregate (`/aggregate/en.wikipedia/all-access/user/monthly/...`) as a control. User agent `NikeCaseResearch/1.0 (academic case competition research; contact: research)`. WORKED, but slowly: most requests returned 429 and the 13 calls took about 35 minutes at one call per 45 s. English Wikipedia, human (user) traffic only, Jan 2019 to Sep 2026.

Caveats: the API counts views of the exact title only, so renamed articles were summed with their old titles (Lululemon = `Lululemon` + `Lululemon_Athletica`, moved in 2025; Asics = `Asics` + `ASICS`; Hoka = `Hoka` + `Hoka_One_One`). The Hoka article evidently sat under a third, unidentified title from mid 2025 to early 2026 (views near zero), so Hoka is excluded from shares and its YoY is not usable. `On_(company)` data starts Jun 2021. Total English Wikipedia user views are themselves falling (-5% to -11% YoY in 2025 to 2026), and brand pages spike on news events (Nike views were unusually high in 2023), so this is a weak, news-driven attention proxy.

Quarterly YoY % (sum of monthly views):

| Quarter | Nike | adidas | New Balance | Asics | On | Lululemon | Puma | All en.wiki |
|---|---|---|---|---|---|---|---|---|
| 2024Q3 | -40 | -26 | 0 | -9 | +29 | -16 | -24 | -3 |
| 2024Q4 | -43 | -27 | -16 | -14 | +27 | -8 | -31 | -4 |
| 2025Q1 | -42 | -27 | +3 | +2 | +25 | -28 | -13 | -6 |
| 2025Q2 | -34 | -38 | +4 | +10 | -3 | -6 | -22 | -8 |
| 2025Q3 | -30 | -27 | -11 | -14 | +1 | -20 | -16 | -6 |
| 2025Q4 | -33 | -22 | -22 | -22 | -7 | -11 | -20 | -6 |
| 2026Q1 | -36 | -31 | -33 | -38 | -26 | -7 | -41 | -11 |
| 2026Q2 | -26 | -7 | -38 | -26 | -21 | -32 | -16 | -5 |
| 2026Q3 | -18 | -7 | -32 | -23 | -11 | -30 | -22 | -7 |

Nike share of combined brand pageviews (ex Hoka): 2019Q1 37.6%, 2021Q1 35.1%, 2023Q1 33.1%, 2024Q1 34.4%, 2025Q1 26.3%, 2025Q3 22.5% (low), 2026Q1 24.1%, 2026Q3 22.6%. adidas drew level with Nike (22.8% vs 22.6%) in 2026Q3, and On rose to 15.9%. Reading: Wikipedia confirms the 2024 to 2025 loss of attention and does not yet show a Nike recovery; the Nike decline rate is narrowing (-42% YoY in 2025Q1 to -18% in 2026Q3) but that is partly the fading of 2024 news spikes.

## 6. App Store snapshot (2026-10-13, US storefront; snapshot only, not a time series)

| App | Rating count (all time) | Avg rating |
|---|---|---|
| Nike: Engineered for Athletes | 1,698,598 | 4.88 |
| Nike SNKRS | 1,412,303 | 4.86 |
| Nike Run Club | 419,514 | 4.77 |
| Nike Training Club | 282,275 | 4.85 |
| adidas: Shop Shoes & Clothing | 825,603 | 4.89 |
| adidas CONFIRMED | 174,627 | 4.85 |
| adidas Running | 108,636 | 4.80 |
| lululemon | 534,032 | 4.90 |
| ASICS Runkeeper | 380,378 | 4.83 |
| PUMA | 114,541 | 4.92 |
| On: Shop Shoes & Apparel (launched Apr 2024) | 75,610 | 4.93 |
| HOKA | no HOKA shopping app found in US search | - |

Top Free Shopping chart (top 100, iTunes RSS, 2026-10-13): US Nike #43, Dick's #56, adidas #57, lululemon #61, SNKRS not in top 100. China: adidas #23, Nike #56. Germany: adidas #53, Nike #97. Japan: adidas #54, Nike #70. UK: adidas #78, Nike not in top 100 (JD Sports #20 and #43). Health and Fitness US: Nike Run Club #53. One-day ranks are volatile; the consistent pattern is adidas ranking above Nike outside the US, including China.

## 7. Macro demand and pricing (FRED: Census MARTS, BLS CPI), YoY %

| Quarter | Sporting goods stores (451) | Clothing stores (448) | Shoe stores (4482) | Footwear CPI | Apparel CPI | All-items CPI |
|---|---|---|---|---|---|---|
| 2024Q3 | -4.9 | +1.3 | -4.6 | 0.0 | +0.7 | +2.7 |
| 2024Q4 | -2.5 | +3.0 | -3.9 | +0.7 | +0.9 | +2.7 |
| 2025Q1 | -1.5 | +4.5 | -2.8 | 0.0 | +0.5 | +2.7 |
| 2025Q2 | +0.3 | +5.0 | +1.2 | -1.1 | -0.8 | +2.5 |
| 2025Q3 | +3.8 | +7.3 | +1.8 | +1.2 | 0.0 | +2.9 |
| 2025Q4 | +5.7 | +6.5 | +2.3 | n/a (Oct 2025 CPI missing) | n/a | n/a |
| 2026Q1 | +8.2 | +6.7 | +5.7 | +1.2 | +2.0 | +3.6 |
| 2026Q2 | +12.6 | +5.5 | +1.7 | +4.1 | +4.4 | +4.2 |

Latest months: sporting goods stores +10.0% (Jul 2026, revised) and +9.6% (Aug 2026 advance); shoe stores 0.0% (Jul 2026); footwear CPI +4.6% (Jul) and +3.2% (Aug). Nominal retail sales are not deflated; with footwear prices up 3% to 5% (tariff pass-through), shoe store unit volume was roughly flat to down in mid 2026, while sporting goods stores (which include hobby, music and book stores) show real growth.

## 8. Nike.com US Sale wall product counts (Wayback)

| Year | Mean count | Min | Max | Snapshots |
|---|---|---|---|---|
| 2019 | 2,748 | 2,253 | 3,242 | 2 |
| 2020 | 3,181 | 2,069 | 4,217 | 9 |
| 2021 | 2,512 | 1,925 | 4,138 | 10 |
| 2022 | 3,644 | 2,486 | 5,183 | 12 |
| 2023 | 4,370 | 2,992 | 5,521 | 12 |
| 2024 | 4,034 | 3,524 | 4,630 | 11 |
| 2025 | 2,923 | 2,059 | 3,652 | 11 |
| 2026 (to Oct) | 4,287 | 3,425 | 5,131 | 8 |

Recent months: May 2025 2,059; Jun 2025 2,163; Sep 2025 2,368; Dec 2025 3,588; Jan 2026 4,238; Jun 2026 3,425; Aug 2026 5,131; Sep 2026 4,889; Oct 2026 4,831. Caveats: one snapshot per month at an arbitrary day (sale events and season-end clearances swing counts), counts are product listings (colorways), not units or dollars, and raw counts ignore catalog size. A second Wayback series of the all-products wall (`nike.com/w`, same `totalResources` field; 39 usable months) allows a sale share of catalog for 34 months where both walls were captured in the same month (snapshot days can differ):

| Month | Sale items | All items | Sale share % |
|---|---|---|---|
| 2021-06 | 1,925 | 7,366 | 26.1 |
| 2022-10 | 4,665 | 11,223 | 41.6 |
| 2023-01 | 4,939 | 11,790 | 41.9 |
| 2023-11 | 2,992 | 13,496 | 22.2 |
| 2024-10 | 4,100 | 13,931 | 29.4 |
| 2025-02 | 3,652 | 10,788 | 33.9 |
| 2025-06 | 2,163 | 10,899 | 19.8 |
| 2025-10 | 3,175 | 14,436 | 22.0 |
| 2026-05 | 3,887 | 14,056 | 27.7 |
| 2026-10 | 4,831 | 18,170 | 26.6 |

So the raw sale count rose about 52% from Oct 2025 to Oct 2026, but the total catalog also grew about 26%, and the sale share rose a more moderate 4.6 points (22.0% to 26.6%). That is above the mid 2025 low (about 20%) and well below the 2022 to early 2023 glut (about 40% to 42%).

## 9. Verdict: Nike demand momentum versus peers, 2025 to 2026

1. 2025 was another year of share loss in consumer attention. Nike's share of combined brand search fell from 40.6% (2025Q1) to 36.2% (2025Q3) in the US and from 38.6% to 36.0% worldwide, with Nike YoY search running 2 to 9 points below zero while On (+35% to +66% YoY), Asics, New Balance and Hoka (worldwide) kept growing. adidas, by contrast, was not gaining on Nike in the US in 2025 (the gap was within plus or minus 3 points) but was gaining worldwide.
2. 2026 shows the first signs of a bottom, led by the US. US Nike share of brand search has been up year on year for five straight months (Jun to Oct 2026), the trailing 12-month US share troughed at 37.3% in May 2026, and in calendar 2026Q3 Nike's US search growth (+6%) matched On and adidas and beat New Balance, Hoka, Asics and Lululemon. The lifestyle franchise drag (Dunk, AF1, Jordan 1) has faded from -20% to -45% YoY to roughly flat, and "Nike shoes" search is up modestly.
3. Worldwide, the picture is stabilization rather than recovery, and English Wikipedia pageviews (still -18% YoY for Nike in 2026Q3, with adidas now level with Nike in pageview share) show no recovery yet. Nike's worldwide share only stopped falling in Sep and Oct 2026 (trailing 12-month trough 35.3% in Aug 2026), adidas still out-grew Nike by 11 points in 2026Q3, and Nike lost further ground against generic "shoes" search (-20% YoY ratio). App Store shopping ranks also put adidas ahead of Nike in China, Germany, Japan and the UK. China is not covered by Google data at all.
4. Revenue link: search YoY and digital revenue YoY move together (r about 0.5 over 9 quarters), but digital revenue has fallen much more than search, so some of the digital decline is Nike's own channel and promotion choices. Digital was still -10% YoY in FQ1 FY2027 while US search turned positive, which is consistent with demand stabilizing before reported digital sales do.
5. Pricing and markdown caution: the US Sale wall carried about 4,800 to 5,100 products in Aug to Oct 2026 versus about 2,400 to 3,300 a year earlier. Normalized by the total catalog, the sale share rose from about 20% to 22% in mid to late 2025 to about 27% in 2026, well below the 40%+ of the 2022 to 2023 glut. So markdown exposure on Nike.com has crept back up, which argues against a clean full-price recovery, but it is not a new glut. Industry footwear prices are up 3% to 5% YoY, and shoe store sales are flat in nominal terms, so the category itself is not providing volume tailwind.

Bottom line: the alternative data supports "US brand attention has bottomed and is turning up modestly in mid 2026", but not yet "Nike is regaining global share". International (especially China and Europe) attention and the rising sale assortment are the main contradicting signals. The April to June 2026 category-wide search spike means absolute YoY numbers for that quarter should not be used in the case.

## 10. CSV files (all in `/tmp/claude-0/-home-user-nike-research-case-comp/97c520cc-64e5-53f3-8fe9-898f5b11e054/scratchpad/altdata/`)

- `/tmp/claude-0/-home-user-nike-research-case-comp/97c520cc-64e5-53f3-8fe9-898f5b11e054/scratchpad/altdata/appstore_ratings_snapshot_2026-10-13.csv`
- `/tmp/claude-0/-home-user-nike-research-case-comp/97c520cc-64e5-53f3-8fe9-898f5b11e054/scratchpad/altdata/appstore_topfree_chart_ranks_2026-10-13.csv`
- `/tmp/claude-0/-home-user-nike-research-case-comp/97c520cc-64e5-53f3-8fe9-898f5b11e054/scratchpad/altdata/fred_retail_sales_and_cpi_monthly.csv`
- `/tmp/claude-0/-home-user-nike-research-case-comp/97c520cc-64e5-53f3-8fe9-898f5b11e054/scratchpad/altdata/gtrends_annual_share_of_brand_search_pct.csv`
- `/tmp/claude-0/-home-user-nike-research-case-comp/97c520cc-64e5-53f3-8fe9-898f5b11e054/scratchpad/altdata/gtrends_monthly_index_nike_units.csv`
- `/tmp/claude-0/-home-user-nike-research-case-comp/97c520cc-64e5-53f3-8fe9-898f5b11e054/scratchpad/altdata/gtrends_monthly_nike_share_and_ratios.csv`
- `/tmp/claude-0/-home-user-nike-research-case-comp/97c520cc-64e5-53f3-8fe9-898f5b11e054/scratchpad/altdata/gtrends_monthly_raw_long.csv`
- `/tmp/claude-0/-home-user-nike-research-case-comp/97c520cc-64e5-53f3-8fe9-898f5b11e054/scratchpad/altdata/gtrends_nike_fiscal_quarter_vs_digital_revenue.csv`
- `/tmp/claude-0/-home-user-nike-research-case-comp/97c520cc-64e5-53f3-8fe9-898f5b11e054/scratchpad/altdata/gtrends_nike_fiscal_year_vs_digital_revenue.csv`
- `/tmp/claude-0/-home-user-nike-research-case-comp/97c520cc-64e5-53f3-8fe9-898f5b11e054/scratchpad/altdata/gtrends_quarterly_avg_nike_units.csv`
- `/tmp/claude-0/-home-user-nike-research-case-comp/97c520cc-64e5-53f3-8fe9-898f5b11e054/scratchpad/altdata/gtrends_quarterly_nike_yoy_minus_peer_yoy_pp.csv`
- `/tmp/claude-0/-home-user-nike-research-case-comp/97c520cc-64e5-53f3-8fe9-898f5b11e054/scratchpad/altdata/gtrends_quarterly_share_of_brand_search_pct.csv`
- `/tmp/claude-0/-home-user-nike-research-case-comp/97c520cc-64e5-53f3-8fe9-898f5b11e054/scratchpad/altdata/gtrends_quarterly_yoy_pct.csv`
- `/tmp/claude-0/-home-user-nike-research-case-comp/97c520cc-64e5-53f3-8fe9-898f5b11e054/scratchpad/altdata/wayback_nike_us_sale_vs_total_catalog.csv`
- `/tmp/claude-0/-home-user-nike-research-case-comp/97c520cc-64e5-53f3-8fe9-898f5b11e054/scratchpad/altdata/wayback_nike_us_sale_wall_item_counts.csv`
- `/tmp/claude-0/-home-user-nike-research-case-comp/97c520cc-64e5-53f3-8fe9-898f5b11e054/scratchpad/altdata/wikipedia_pageviews_monthly_by_article_raw.csv`
- `/tmp/claude-0/-home-user-nike-research-case-comp/97c520cc-64e5-53f3-8fe9-898f5b11e054/scratchpad/altdata/wikipedia_pageviews_monthly_by_brand.csv`
- `/tmp/claude-0/-home-user-nike-research-case-comp/97c520cc-64e5-53f3-8fe9-898f5b11e054/scratchpad/altdata/wikipedia_quarterly_yoy_and_share.csv`

Raw downloads (untrusted inputs, kept for audit): `/tmp/claude-0/-home-user-nike-research-case-comp/97c520cc-64e5-53f3-8fe9-898f5b11e054/scratchpad/altdata/raw_gtrends/` (including `gt_US_daily_2026spring.csv`), `raw_wiki/`, `raw_appstore/`, `raw_fred/`, `raw_wayback/`.
