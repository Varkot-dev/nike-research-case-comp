# How fast is Nike implementing its plan? Ten alternative-data indicators

**Prepared:** October 18, 2026. **Question:** for each pillar of Nike's turnaround plan, is the free alternative data moving in the direction the plan requires, and how fast?
- **Excel-ready output:** `data/execution_speed/nike_execution_speed.xlsx` has a Summary sheet plus one sheet per table, and the same tables are CSVs in that folder.
- **Script:** `scripts/execution_speed/build.py` (run from the repo root; regenerate, do not hand-edit).

**Method.**
- **No new scraping.** This session's container cannot reach web.archive.org, nike.com, retailer sites or sec.gov (network policy). Every table is therefore rebuilt from raw pulls that earlier sessions already committed under `data/`. Each source folder's README carries its own routes, sample sizes and caveats.
- **Measures:** each indicator gets a baseline (Nike's own plan start or the first reliable reading), the latest reading, the change, and the pace per quarter (change divided by quarters elapsed). All are my arithmetic.
- **Status rule (fixed before reading results):**
  - "Moving with plan" if the change is in the direction the plan requires.
  - "Against plan" if it moves the other way.
  - "Little change" if the move is under 5% of the baseline.

## 1. Result in one table

| Pillar | Indicator | Baseline | Latest | Change | Pace per quarter | Status |
|---|---|---|---|---|---|---|
| Classics wind-down | Air Force 1 products listed on nike.com | 172 (2023H1) | 53 (2026H1) | -69% | -9.9 | Moving with plan |
| Classics wind-down | Dunk products listed on nike.com | 69 (2023H1) | 31 (2026H2 to date) | -55% | -2.9 | Moving with plan |
| Classics wind-down | Air Jordan 1 products listed on nike.com | 102 (2023H1) | 118 (2026H1) | +16% | +1.3 | Against plan |
| Full-price Digital | Men's shoes on nike.com sale wall, % of men's shoes | 42.6% (Oct 2024) | 44.0% (Oct 2026) | +1.4 pts | +0.2 pts | Little change |
| Full-price Digital | nike.com product pages showing a discount | 22.6% (2024Q3) | 36.0% (2026Q3) | +13.4 pts | +1.7 pts | Against plan |
| Inventory clean-up | Nike + Jordan share of Foot Locker sale items | 37.5% (Nov 2024) | 37.4% (Oct 2026) | -0.1 pts | 0.0 | Little change |
| Inventory clean-up | Products on nike.com sale wall | 3,927 (Oct 2024) | 4,831 (Oct 2026) | +23% | +112 | Against plan |
| Wholesale reinvestment | Nike share of products on academy.com (Aug to Oct) | 28.3% (2025) | 16.3% (2026) | -12.0 pts | -3.0 pts | Against plan |
| Wholesale reinvestment | Nike share of products on famousfootwear.com (Aug to Oct) | 1.6% (2024) | 2.9% (2026) | +1.4 pts | +0.2 pts | Moving with plan (small sample) |
| Partners' view | DICK'S call: net positive Nike sentences | 3 (May 2025) | 8 (Aug 2026) | +5 | +1.0 | Moving with plan |
| Partners' view | Academy call: net positive Nike sentences | 3 (Mar 2024) | 1 (Sep 2026) | -2 | -0.2 | Against plan |
| Store fleet | Nike-owned in-line stores worldwide (store locator) | 135 (Feb 2025) | 96 (Oct 2026) | -29% | -6.1 | Moving with plan |
| Store fleet | Nike-owned stores in the US (store locator) | 295 (Feb 2025) | 252 (Oct 2026) | -15% | -6.7 | Moving with plan |
| Sport offense (running) | Nike share of men's road-running colorways, Running Warehouse | 10.4% (Feb 2025) | 9.6% (Oct 2026) | -0.8 pts | -0.1 pts | Against plan |
| China reset | Topsports + Pou Sheng doors | 8,468 (2024H2) | 7,322 (2026H1) | -13.5% | -192 | Moving with plan (pace only) |
| Reorganisation | Sales and merchandising share of corporate job postings | 7.1% (2025H1) | 16.0% (2026Q3) | +8.9 pts | +1.8 pts | Moving with plan |
| Dated commitments | Hill-era promises kept or beaten, of those resolved | n/a | 4 of 8 | 50% | n/a | 5 pending, 2 at risk |

Source file for each row: `data/execution_speed/Summary.csv`, column `source`.

## 2. What the pattern says (my inference, from the table)

**Actions Nike controls directly are moving at speed.**
- Classics listings: Air Force 1 at -69% and Dunk at -55%.
- In-line stores closed: -29% worldwide, and the US Nike-owned fleet -43 stores in 19 months.
- The partner door clean-up in China: -1,146 doors in 18 months.
- Corporate hiring mix: the sales and merchandising share more than doubled.

These measure inputs that management decides directly.

**Indicators that measure the market's response are flat or moving against plan.**
- On nike.com, the share of product pages showing a discount rose from 22.6% to 36.0% (same calendar quarter, 2024 vs 2026), and the sale wall grew 23%.
- Nike and Jordan's share of Foot Locker sale items is unchanged at about 37%.
- Nike's share of full-price road-running colorways at Running Warehouse slipped from 10.4% to 9.6%.

The plan's stated aims (a full-price Digital platform, a clean marketplace, share gains in running) would need these to move the other way.

**For the pitch:** execution speed on inputs is not the question; conversion into full-price sell-through is. That is consistent with:
- the slipped December 2026 clean-up date (`thesis_tests/say_vs_do_execution.md`);
- the "clean marketplace by end of 1H FY26" promise scored as missed (T10a, H02).

**Two exceptions argue the other way and must be shown in Q&A:**
- DICK'S management's tone on Nike turned more positive (net +3 to +8 sentences, zero negative sentences across six calls).
- Famous Footwear's Nike share rose, but from a 385-product sample.

**Classics timing:** the Air Force 1 decline started in 2024H2, before Elliott Hill's first full quarter, so not all of it is the new plan.

## 3. Caveats per indicator (read before citing)

| Table | Caveat |
|---|---|
| T01 classics | Common Crawl captures of nike.com wall counters ("N results"). Half-year medians, 4 to 16 captures per half. A smaller listing count can mean fewer styles, fewer colorways or sold-out pages; the counter cannot separate them. Air Jordan 1 rebounded from 46 (2025H1) to 118 (2026H1) |
| T02 discount share | Product-page panel from Common Crawl, not a random sample of the catalog. The source README says hidden "See Price in Bag" promotions are counted as full price, which would understate discounting. Its own crawl-level confidence interval is wide (`data/hunt/pricing_catalog/README.md` Section 3) |
| T03 Foot Locker | Wayback snapshots of footlocker.com/sale only. These measure share of sale items, not of all items |
| T04 partner sites | Common Crawl product-URL samples. Academy's 2024 sample (430 products) found no Nike pages, while Academy's full sitemap shows 8.9% Nike (`Niche sources/N6_offprice_census.md`), so 2024 is excluded and the baseline is 2025. Year-to-year swings can reflect which pages the crawler captured |
| T05 retailer calls | Sentence-level tone is a keyword classifier from the earlier session (positive or negative words). DICK'S has six calls (FY2025Q1 onward); Academy has eight |
| T06 stores | The locator series is consistent only from Feb 22, 2025 (crawl method changed). The China owned count is flat at 236 throughout; Nike's China partner feed is known to be frozen (`data/hunt/china_doors/README.md`), so do not read the China owned count as evidence |
| T07 running | Running Warehouse road page, 5 snapshots. Colorway share is shelf breadth, not sales |
| T08 China | HKEX filings of Topsports and Pou Sheng. The 2026H1 Topsports figure is estimated from selling area. Nike gives no door target, so this measures pace, not success |
| T09 hiring | Common Crawl samples of the careers site. 2025H1 has only 126 corporate postings. The sales share peaked at 23.3% in 2025H2 |
| T10 promises | Scored by the earlier session against filings; outcomes and pages in `data/hunt/earnings_calls/promise_tracker.csv` |

## 4. How these feed the valuation model (my inference)

| Indicator | Model driver it informs |
|---|---|
| Classics listings (T01) | Footwear revenue path and the size of the remaining classics headwind (Nike: classics down more than $4B from peak, T10a H12) |
| Discount share, sale wall (T02, T03) | Gross margin: the "lower full-price ASP" and "higher discounts" lines of Nike's gross margin bridge, in bps |
| Partner shelf share and tone (T04, T05) | Wholesale revenue growth and channel mix. At FY2024 channel margins, each point of mix moved to wholesale costs about 27 bps of gross margin (`22_margin_by_business_and_mix.md`) |
| Store closures (T06) | Operating overhead (occupancy) and Direct revenue |
| China doors (T08) | Greater China revenue growth |
| Promise ledger (T10) | How much weight to put on management's Investor Day targets (Nov 16 to 17) |

## 5. Not run, and why (network policy of this session)

| Planned indicator | Route | Status |
|---|---|---|
| Site-wide promotion days on nike.com | Wayback daily homepage snapshots | Blocked (web.archive.org refused by proxy) |
| Promotional email count, Nike vs adidas, Hoka, On | Milled.com archive | Blocked |
| Nike share of full-price shelf at DICK'S and Foot Locker | Wayback brand pages | Blocked; only the Foot Locker sale page history exists (T03) |
| Former Nike store listings | LoopNet, Crexi | Blocked |
| China partner site product counts | Tmall, JD, Douyin via Wayback | Blocked |

These are not inconclusive results; they were not attempted beyond the connection test. Enabling `web.archive.org`, `nike.com` and `milled.com` in the environment's network settings would allow them.
