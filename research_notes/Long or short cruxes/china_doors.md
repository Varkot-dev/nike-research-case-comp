# China Nike-selling doors: what is the real trend, 2023 to Oct 2026?

Written 2026-10-14. Data and scripts: `data/hunt/china_doors/` (README lists every route). Tags: OPENED means we read the source itself, SNIPPET means a search summary only, HUNT means a dataset pulled in this hunt, DERIVED means our own arithmetic.

## Verdict

**SHORT, moderate.** Nike's two largest China partners shut doors about five times faster than the domestic brands that held steady, and the decline has not stopped. It is not strong, because no source counts Nike doors alone, the partners also sell adidas and others, and one domestic brand (361) is closing nearly as fast.

Rule stated in advance: falling faster than domestic brands points SHORT; stabilizing points LONG. Result against that rule:

| Test | Partners (Pou Sheng plus Topsports) | Domestic | Reads as |
|---|---|---|---|
| 3 years, Jun/Aug 2023 to Jun 2026 | -26.3% (9,932 to 7,322, Topsports end point estimated) | ANTA +2.6%, Li Ning -1.7%, Xtep Adult -2.1%, 361 core -10.0%, ANTA KIDS -4.9%, Xtep Kids -8.4%, 361 Kids -10.0% | Faster: SHORT |
| 1 year, Jun/Aug 2025 to Jun 2026 | -9.6% (Topsports is 9 months, so about -12% annualized) | ANTA -0.9%, Li Ning -0.6%, Xtep Adult -0.8%, 361 core -10.5%, kids lines -6% to -12% | Faster than three of four, level with 361: SHORT, lower confidence |
| Direction of the pace | Combined half-year change -6.8, -2.7, -3.9, -8.9, -4.4, -5.3, -4.5% (2023H1 to 2026H1). Plateau near -4% to -5% per half | Flat | Not stabilizing (LONG needs near 0), not accelerating |

All figures HUNT/DERIVED from `data/hunt/china_doors/rate_comparison.csv` and `partner_doors_halfyear.csv`.

## The tidy half-year series (directly operated doors, HKEX)

| Half | Pou Sheng (Jun/Dec) | Chg % | Topsports (Aug/Feb) | Chg % | Combined | Chg % |
|---|---|---|---|---|---|---|
| 2023H1 | 3,723 | -9.0 | 6,209 | -5.4 | 9,932 | -6.8 |
| 2023H2 | 3,523 | -5.4 | 6,144 | -1.0 | 9,667 | -2.7 |
| 2024H1 | 3,478 | -1.3 | 5,813 | -5.4 | 9,291 | -3.9 |
| 2024H2 | 3,448 | -0.9 | 5,020 | -13.6 | 8,468 | -8.9 |
| 2025H1 | 3,408 | -1.2 | 4,688 | -6.6 | 8,096 | -4.4 |
| 2025H2 | 3,310 | -2.9 | 4,360 | -7.0 | 7,670 | -5.3 |
| 2026H1 | 3,110 | -6.0 | about 4,212 (ESTIMATE, May 2026) | -3.4 (one quarter) | about 7,322 | -4.5 |

What the two companies show separately:
- **Topsports** peaked in closures in the half to Feb 2025 (-793 net), then ran at -332 and -328 per half. Annual closures were 1,559, 947, 1,382, 861 and openings 429, 526, 258, 201 for FY23 to FY26 (annual report FY25/26 p.9, OPENED). Selling area YoY: -14.1% (Aug 2025), -13.4%, -9.7% (Feb 2026), -11.2% (May 2026): no turn. The Aug 2026 count is not out (results 2026-10-28, board notice 2026-10-12, OPENED).
- **Pou Sheng** is accelerating: -0.9%, -1.2%, -2.9%, -6.0% per half (HKEX interim announcement 2026-08-12, OPENED, 3,310 to 3,110).
- Sales per door are rising as weak doors close. Topsports principal-brand (Nike plus adidas) revenue per average door: RMB 3.91m (FY24), 4.18m (FY25), 4.76m (FY26), +14% in FY26 (DERIVED; includes online and wholesale, so crude). Closures are partly clean-up of unproductive doors, not only lost demand.

## Nike-specific cross-checks (all weaker than the door totals)

1. **Management's own rounded anchors, OPENED (repo copies of investors.nike.com transcripts).** Jun 29 2023 Q4 FY23 call: "we have 6,000 monobrand doors". Mar 21 2024 Q3 FY24 call: "we have 6,000 monobrand doors". Sep 30 2025 Q1 FY26 call: "With over 5,000 mono-brand stores in China". Dec 18 2025 Q2 FY26 call: "thousands of 5,000 doors". Applying the partner index change from 2023H1 to 2025H1 (-18.5%) to 6,000 gives about 4,890, close to "over 5,000" (DERIVED, consistent within rounding). Rolling "over 5,000" forward by the partner index to Jun 2026 (x 0.904) gives roughly 4,500 to 4,900 Nike mono-brand doors (DERIVED, low confidence; the true base could be 5,000 to 5,400).
2. **Nike-owned China doors are not the problem.** Locator, owned records, which Nike maintains (HUNT): 237 (Apr 2025), 230 (Oct 2025), 224 (Mar 2026), 225 (Aug 2026), 236 listed on 2026-10-03 but 10 of those carry future opening dates (2027-01 to 2027-05), so about 226 operating. Down about 5% in 18 months and flat in 2026. Press says Nike-owned "more than 200" (SNIPPET).
3. **Nike's largest-supplier share at the partners (Nike by inference, supplier unnamed).** Topsports 59.0%, 62.8%, 64.8%, 66.6%, 62.7% of purchases FY22 to FY26. Pou Sheng 60%, 61%, 58%, 55% for FY22 to FY25 (annual reports, OPENED). Nike's weight in the partners is stable to falling at Pou Sheng, so partner door cuts are not hiding a switch to Nike.
4. **adidas runs through the same doors and grew** (+9% to +17% c-n per quarter, repo note `china.md`), so the closures are a retailer footprint reduction, in which Nike is the larger part (60%+ of purchases) but not the only part.

## Why the locator failed, now proven (HUNT, Nike per-store API, 400 records sampled 2026-10-14)

- 310 of 310 sampled China partner records read storeStatus OPEN, published, with no closing date. Their modification dates run from 2024-01-10 to **2025-10-15**; 1 of 310 is dated after Aug 2025 and none after 2025-10-15.
- 87 of 90 Nike-owned records were modified in 2026. Nike keeps its own records current and let partner records freeze on 2025-10-15, when the partner file was apparently last loaded.
- Even the owned records lag: 17 owned China doors dropped from the locator in 2025 to 2026 carry closing dates between 2022-03 and 2025-11 (`nike_owned_cn_dropped_api_check.csv`). The locator is also a registry that never prunes partner doors: of 2,740 China ids ever seen, only 22 partner ids were ever removed, 21 of them before Oct 2024.
- Conclusion: the 2,438 figure has no information about closures after Oct 2025 and is a registry, not a count. Do not cite it as a door count in either direction.

## Sources (dates, OPENED or SNIPPET)

| Source | Date | What it gave | Tag |
|---|---|---|---|
| Topsports annual report 2025/26 (HKEX 2026062400677) | 2026-06-24 | Store roll-forward FY23 to FY26, area changes, supplier concentration, principal brands | OPENED |
| Topsports Q1 FY2026/27 update (HKEX 2026062500529) | 2026-06-25 | Area -2.9% QoQ, -11.2% YoY, sales low-teens decline | OPENED |
| Topsports inside information (HKEX 2026072200069) and board notice (2026101200757) | 2026-07-22, 2026-10-12 | Nike online sales end 2027-01-01, 22% of group revenue; interim results 2026-10-28 | OPENED |
| Pou Sheng interim results (HKEX 20260812_2026081200368) and interim report 2026 (2026090700493) | 2026-08-12, 2026-09-07 | 3,310 to 3,110 doors, no Nike detail | OPENED |
| Topsports and Pou Sheng annual and interim reports 2021 to 2026 (19 documents) | various | Door counts, supplier concentration; Nike named only as a "principal brand" at Topsports, never at Pou Sheng | OPENED |
| ANTA, Li Ning HKEX results (documents in `domestic_doors_halfyear.csv`) | 2023 to 2026 | Door counts | OPENED |
| Xtep interim reports 2023 to 2026, annual reports 2023 to 2025 (doc.irasia.com) | 2023 to 2026 | Xtep Adult and Kids stores | OPENED |
| 361 Degrees results announcements and interim report 2026 (HKEX 2026081800247, 2026082800411) | 2023 to 2026 | 5,076 mainland core stores at Jun 2026 (5,394 at Dec 2025), kids POS 2,202 | OPENED |
| 361 Q3 2026 business update (HKEX 2026101400065) | 2026-10-14 | Retail sales mid single-digit growth, no door count | OPENED |
| Nike earnings call transcripts Q4 FY23, Q3 FY24, Q1 FY26, Q2 FY26 (`data/hunt/earnings_calls/transcripts/`) | 2023-06-29 to 2025-12-18 | Management door anchors | OPENED |
| Nike 10-K FY2026 (sec.gov nke-20260531.htm), p.2 | 2026-07-15 | Non-US owned stores 537 factory plus 50 in-line plus 54 Converse; no Greater China split | OPENED |
| Nike per-store API api.nike.com/store/store_locations/v1/<id> | 2026-10-14 | Status, closing and modification dates | OPENED (HUNT) |
| The Standard HK, "Shares of Topsports drop as Nike plans to restrict online sales in China" | 2026-07-22 | 16 store partners that "own and manage thousands of Nike stores" | OPENED |
| Inside Retail Asia, "Inside Nike's great China purge" | 2026-07-24 | Page opened; no door counts, online distributors only | OPENED |
| 36Kr, Beijing Business Today, Huxiu, 10jqka, Yicai via search | 2026-07-22 and after | Offline Nike and Jordan doors keep trading; "thousands" of online distributors cut; Topsports closes more stores in FY27 (BOCI view) | SNIPPET |
| Press: Topsports operates "over half" of Nike's China stores; Nike owns "more than 200" | 2026-07 | Context only | SNIPPET |

## Routes tried (full table in the README)

Worked: HKEX partner filings (total doors), domestic-brand filings, Nike per-store API (proves staleness), Nike calls (anchors). Partial: Nike 10-K (no China split), press (no counts), OpenStreetMap history via ohsome (mapping growth only: 24-city Nike shop count 51 to 117, adidas 74 to 136, ANTA 13 to 50, all rising every quarter). Blocked: Overpass, Geofabrik, Baidu, Amap (key required), web.archive.org and Common Crawl index (blocked or 429), nike.com.cn store pages (404), Dewu and Tmall (JS or login, and online anyway). Not yet available: Topsports Jun to Aug 2026 (2026-10-28).

## What this does and does not show

- It does show the physical network that sells Nike in China shrank about a quarter in three years and about a tenth in the last year, and the pace has plateaued near 4% to 5% per half, not turned.
- It does not isolate Nike doors. Both retailers are multi-brand, and Topsports and Pou Sheng do not disclose doors by banner. Closures at 361 (-5.9% in H1 2026) show the domestic control group is not uniformly flat, which is why this is moderate and not strong.
- It weakens one sentence in the scoreboard and `china_floor.md`: "domestic brands hold". ANTA, Li Ning and Xtep Adult hold (-1% to -2% over three years). 361 and the kids lines do not.
- It supports the repo's China SHORT through a physical channel that agrees with management guidance, but the strong grade still rests on guidance and the 2027-01-01 online cut, not on doors.

## What would settle the Nike-only count

1. Topsports interim results 2026-10-28: door count at 31 Aug 2026 and any banner split (first real test of whether the plateau holds; a net closure under about 150 would lean LONG-stabilizing, over about 330 would confirm a continuing pace).
2. Ask Nike IR or read the Q2 FY27 call (about 2026-12-18) for an updated mono-brand door number to replace "over 5,000".
3. A paid POI crawl (Amap or Baidu with an API key, brand "耐克" or "Nike" by city) repeated twice, which we could not do without creating an account.
