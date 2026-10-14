# Risk check: does "gross margin rising" really turn Nike's history into a coin flip?

Written 2026-10-14. Stock $35.35 (Oct 12, 2026). Pitch window: submission Nov 1, 2026; 6 months out is about May 2027 (contains the Q2 FY27 print, about Dec 17, and the Q3 FY27 print, about late March).

Tags: OPENED = source read directly; SNIPPET = search-result summary only; REPO = earlier work in this repo; DERIVED = our arithmetic on the cited data.

Data and scripts: `data/hunt/risk_history/` (scripts in `scripts/`, outputs in `out/`). Raw SEC companyfacts JSON and Yahoo price JSON stay in the session scratchpad (too large to commit, about 150MB); `out/quarterly_panel.csv` and `out/events_all.csv` hold everything the tables use.

## 1. Bottom line

**The finding is weaker than the scoreboard line suggests. History still leans SHORT for Nike, weakly.**

- The scoreboard's "about 45% beat the index when margin rose, 10 of 47 when it fell" adds the same events up across four overlapping specifications. Counted once per company episode, and with 28 more brands and retailers, the split is **39% (13 of 33) versus 29% (10 of 35)** at 6 months. At 12 months it is **42% versus 23%** (DERIVED, section 3).
- Even the "margin rising" bucket does worse than the plain base rate for deeply fallen consumer stocks. That base rate is 46% beating the S&P 500 at 6 months, median -5 points. The margin-up bucket has a median of **-14 points at 6 months and -9 at 12**. Rising margin softens the SHORT case. It does not make the setup neutral.
- Nike is very likely in the margin-up bucket for Q2 and Q3 FY27, but for the "wrong" reason. Q1 FY27's +60bp came from logistics (+90bp), FX (+40bp) and product cost (+10bp). Price (ASP) took off 30bp and royalties 40bp (Q1 FY27 10-Q p.23, OPENED via REPO fact base). Management also guides EBIT down more than revenue. The closest historical bucket (revenue down and getting worse, next gross margin up, next operating margin down) beat the S&P 500 **6 of 15 times at 6 months (median -23)** and **5 of 15 at 12 months (median -22)**.
- **What cuts the other way:** brand owners only (no pure retailers, Fossil excluded) with margin rising beat at **7 of 12, median +11 at 6 months**. Cases 75% or more below the high (Nike is about 80%) beat 7 of 13. Small samples, wide intervals (roughly 30% to 80%), but they show the LONG tail is real.
- **Verdict:** history makes Nike close to a coin flip at best, and more often a 35% to 40% proposition at 6 months, with a typical worst point about 30% below entry inside 12 months. **Points SHORT, weak strength.** It is not strong enough to be a reason to short. It is enough to say the margin finding does not rescue a LONG.

## 2. What the original study did (re-checked at source)

Scripts: scratchpad `fund2/tool/study.py`, `q2.py` (Round 3) and `skep3/study_om.py` (skeptic). I re-ran them (REPO, OPENED) and rebuilt the logic in `data/hunt/risk_history/scripts/panel.py` and `study.py`. The per-spec counts reproduce: drop 60% next-GM-up 6 of 15, next-GM-down 2 of 14 (the original had 1 of 13; one extra event now has a completed 12-month window because the price files run to Oct 2026). The other three specs are identical.

| Check | Finding |
|---|---|
| Sample selection | 45 US filers picked by hand in 2026, including non-consumer names (PYPL, INTC, KHC, CMG, SBUX). They have to be at least 60% below their 5-year high, 2010 onward, 2020 excluded, and the S&P 500 up over the trailing year. |
| "Gross margin rising" definition | **Reported**, **year over year**, any change above 0bp, for the **next** quarter after the event (realized, so it uses future data). Not guided, not sequential. A +5bp quarter counts as "rising". |
| Look-ahead | For history the bucket is the margin that actually printed. For Nike it has to be forecast, so Nike's bucket is a probability, not a fact (section 4). |
| The "10 of 47" | It is 1 of 13 + 1 of 5 + 7 of 22 + 1 of 7 across drop 60%, drop 75%, quarterly 60% and quarterly 75%. The 75% sets sit inside the 60% sets, and drop and quarterly events overlap in time. So the same episode is counted up to four times. "About 45%" is 28 of 67 by the same addition (DERIVED). |
| Bucket size | Per spec, 5 to 25 events from 5 to 14 companies. Fossil alone is 5 to 6 of the margin-up cases. |
| Survivorship | Yahoo has no prices for J.C. Penney, Francesca's, Pier 1, Stage Stores, Delta Apparel, Hibbett, Nordstrom and Victoria's Secret, so they cannot be scored. Their XBRL (OPENED) shows 33 Nike-path setups since 2014. 27 had next-quarter margin down and most ended in bankruptcy, so the missing names mainly flatter the margin-DOWN bucket. Only J.C. Penney May 2019 (next GM +312bp, bankrupt May 2020) is a margin-up case that went to zero. Net effect: the real split is probably a little wider than measured, but the margin-up bucket is not hurt. |
| Benchmark | Original: S&P 500 only. Added: XRT (equal-weight retail ETF) and XLY (consumer discretionary). |

## 3. The re-run: expanded universe, one event per company episode, with intervals

Universe: the original 45 plus 28 more US filers. The added names are Dick's, Academy, Genesco, Caleres, Designer Brands, Buckle, Burlington, Ross, TJX, Children's Place, Cato, Tilly's, FIGS, YETI, Revolve, Stitch Fix, Weyco, Ascena, Tailored Brands, Destination XL, Duluth, Lakeland, Lands' End, Vince, J.Jill, Kontoor, e.l.f. and Coty. Fundamentals come from SEC XBRL companyfacts (data.sec.gov, fetched 2026-10-14, OPENED) and prices from the Yahoo v8 chart API (fetched 2026-10-14, OPENED). Ticker reuse excluded SMRT, CBK and BBBY. Non-consumer names (PYPL, INTC, KHC, CMG, SBUX) are dropped from the main table.

Method: all four specs are pooled, then cut down to one event per company per 180 days. "Nike path" means revenue down year over year now and the next quarter more than 2 points worse. Wilson 95% interval and company-cluster bootstrap 95% interval (2,000 draws). Output: `out/analysis_main.txt`, `analysis_extra.txt`, `analysis_robust.txt` (DERIVED).

| Bucket (consumer universe, deduped) | N / cos | Beat S&P 6m | 95% CI | Median 6m | Beat S&P 12m | Median 12m | Beat XRT 12m | Median vs XRT 12m |
|---|---|---|---|---|---|---|---|---|
| All deep-drawdown events (base rate) | 295 / 51 | 46% | 40-52 | -5 | 42% | -10 | 48% | -3 |
| Nike path, all | 66 / 31 | 33% | 23-45 | -21 | 32% | -25 | 33% | -12 |
| Nike path, next GM up | 33 / 22 | **39%** | 25-56 | **-14** | **42%** | **-9** | 45% | -1 |
| Nike path, next GM down | 33 / 23 | **27%** | 15-44 | **-25** | **21%** | **-31** | 21% | -25 |
| Next GM up, next op margin down (Nike's guide) | 15 / 11 | 40% | 20-64 | -23 | 33% | -22 | 40% | -3 |
| Next GM up, next op margin up | 17 / 12 | 41% | 22-64 | -12 | 47% | -3 | 47% | -1 |
| Current GM up (known on the day, no look-ahead) | 30 / 17 | 47% | 30-64 | -9 | 50% | 0 | 50% | +3 |
| Current GM down | 36 / 22 | 22% | 12-38 | -25 | 17% | -31 | 19% | -24 |
| Next revenue -5% to -14% (Nike's size), GM up | 20 / 15 | 35% | 18-57 | -16 | 40% | -13 | 45% | -1 |
| Same, GM down | 21 / 14 | 19% | 8-40 | -25 | 19% | -34 | 19% | -26 |

Original 45 only, deduped: next GM up 10 of 21 (48%, median -5) versus next GM down 4 of 23 (17%, median -25) at 6 months. So the clean split in the scoreboard comes mostly from the original hand-picked set. Adding 28 names roughly halves the gap at 6 months, but it holds at 12 months.

Robustness (DERIVED, `analysis_robust.txt`):
- Without Fossil and Peloton: margin up 10 of 27 (37%, median -20) versus margin down 9 of 29 (31%) at 6 months; at 12 months, 41% versus 24%.
- Brand owners only (no pure retailers), Fossil excluded: margin up 7 of 12 (58%, median +11 at 6m, +10 at 12m); margin down 4 of 13 (31%) and 3 of 13 (23%). This is the best evidence for LONG, but it rests on 9 companies.
- At least 75% below the high, Fossil and Peloton excluded: margin up 7 of 13 (54%, median +7).
- Two quarters of margin up in a row: 11 of 24 (46%) at 6 months. Up then down: 2 of 9.
- Worst point inside 12 months, margin-up bucket: median -30%; 20 of 33 cases fell 25% or more at some point.

Read: the gross margin split is real and holds up better at 12 months than at 6. But "margin up" moves outcomes from clearly bad (about 30%) to slightly below average (about 40%). It does not move them to a coin flip versus the S&P 500, except in the small brand-only and deep-drawdown subsets. Against XRT the margin-up bucket is close to even at 12 months (45%, median -1).

## 4. Is Nike really in the "margin rising" bucket, and why?

### Facts

| Item | Value | Source | Date | Tag |
|---|---|---|---|---|
| Q1 FY27 gross margin | 42.8%, +60bp vs 42.2% | Q1 FY27 10-Q p.19, p.22 | filed 2026-10-02 | OPENED (REPO fact base `data/nike_filing_facts.csv`, branch wonderful-franklin) |
| Q1 FY27 bridge | Warehousing and logistics +90bp; FX +40bp; product costs +10bp; ASP -30bp; other costs (royalties) -40bp; Converse -10bp | Q1 FY27 10-Q p.23 | 2026-10-02 | OPENED (REPO) |
| Q1 FY27 call | GM up "benefits from our supply chain cost management efforts and FX tailwinds, partially offset by increased discounts as well as channel mix" | Q1 FY27 call transcript | 2026-10-01 | OPENED (scratch `flat_Q1FY27.txt`) |
| Q1 FY27 call | No FY gross margin guide; supply chain moves "bolstering gross margin... at the same time, we are taking discounts and resetting the marketplace, which is dampening gross margins over time" | same | 2026-10-01 | OPENED |
| Q1 FY27 call | "EBIT to decline by a greater percentage than revenue... continued pressure on gross margin... higher input costs" | same | 2026-10-01 | OPENED |
| Q2 FY26 (the Q2 FY27 comparison) | 40.6%, -300bp; product costs -360bp "primarily due to higher tariffs" | Q2 FY26 10-Q p.27; 8-K | 2025-12-30 | OPENED (REPO) |
| Q3 FY26 | 40.2%, -130bp; product costs -270bp, tariffs | Q3 FY26 10-Q p.30 | 2026-04-01 | OPENED (REPO) |
| Q4 FY26 | 49.2%, +890bp, including about +900bp IEEPA recovery ($986M); 40.2% without it | Q4 FY26 8-K Ex. 99.1; call | 2026-06-30 | OPENED (REPO; `flat_Q4FY26.txt`) |
| Tariff assumption | "incremental tariff rates of 10% continuing through the end of July and then increasing to 15% thereafter" | Q4 FY26 call | 2026-06-30 | OPENED |
| Q4 FY26 margin driver | Underlying margin beat guide; "the biggest driver was discount improvement... in North America" | Q4 FY26 call | 2026-06-30 | OPENED |

### Tariff relief versus underlying price and discount (DERIVED)

- **Q1 FY27 (+60bp):** about +140bp came from cost and FX (logistics +90, FX +40, product cost +10). About -80bp came from price, mix and royalties (ASP -30, royalties -40, Converse -10). Tariffs were roughly neutral year over year: product cost was only +10bp, because the 10% rate this year roughly matched last year's partly flowed-through IEEPA cost. **Underlying pricing was negative.**
- **Q2 FY27 (reported about Dec 17):** it laps 40.6%, which carried -360bp of product cost, mostly tariffs. Tariffs are still being paid at the assumed 15%, so the tariff relief is only the gap between 15% and last year's blended IEEPA rate. I put that at roughly 50 to 150bp, low confidence. Lapping EMEA Cyber Week promotions also helps. Against this, Nike says discounts are rising as it resets the marketplace, and a China clean-up is under way. Round 3's skeptic backed out of the EPS guide a Q2 to Q4 gross margin of about 41.6% against a 40.3% base without the refund (REPO). **Gross margin up in Q2 is likely. I put it at about 75 to 80%.** In history, current margin up led to next margin up 23 of 30 times on the Nike path (DERIVED), and the comparison is easy. But the rise would come from cost and the easy comparison, not from pricing.
- **Q3 FY27 (late March):** it laps 40.2% (-270bp tariffs). Same logic, likely up.
- **Q4 FY27 (late June 2027):** it laps the reported 49.2%, so reported gross margin will fall about 600 to 900bp. In XBRL-based screens Nike then sits in the margin-DOWN bucket. That is outside the 6-month window but inside 12 months. Against the 40.2% base without the refund it could still rise.
- **Contamination note:** the 2026 IEEPA refunds hit reported gross margin across the sector. Under Armour shows "next GM +590bp" for its 2026 setup in this panel (`out/recent_setups.txt`). Any 2026 cases in the history must be read with this in mind. None of them has a 12-month outcome yet.

### Is a cost-driven rise worse than a pricing-driven one?

- Test (DERIVED): margin-up cases where the margin rise fell in a known input-cost deflation window (cotton 2012-13, freight 2023-24, N=13) beat 6 of 13 (46%, median -20) at 6 months. Outside those windows (N=20) they beat 7 of 20 (35%, median -14). No evidence that cost-driven rises are worse, but the time-window proxy is crude.
- Freight-relief cases that look like Nike now (cost relief plus promotions, revenue falling): Under Armour Oct 2023 (-20 at 6m / -9 at 12m), Under Armour May 2024 (+15 / -24), VF Oct 2023 (-35 / +16), Macy's May 2023 (-23 / -1), Children's Place Feb 2024 (-76 / -79), Vince May 2023 (-83 / -90). Winners: Gap Jun 2023 (+148 / +250, with lower discounting as well as freight), Lands' End Aug 2023 (+13 / +76), Wolverine Feb 2024 (+59 / +148), Fossil Feb 2024 (+3 / +24) (DERIVED, `analysis_extra.txt` C6).
- Operating margin is a usable stand-in for quality. Margin up while operating margin falls, which is Nike's guide, gives 40% and 33% at 6 and 12 months, a bit worse than margin up with operating margin up (41% and 47%).

## 5. Non-US and newer cases

| Case | Setup | Margin | Outcome | Source / tag |
|---|---|---|---|---|
| Puma, Jul 25, 2025 (profit warning) | 82% below 5-year high; Q3 2025 sales -10.4% currency-neutral (worse) | Q3 GM -260bp to 45.2% from "increased wholesale promotions, inventory reserves... higher freight costs"; FY25 GM -260bp to 45.0% | 6m -13 vs DAX; 12m +33 vs DAX | Puma Q3 2025 release and FY25 report (SNIPPET, 2025-10-30 and 2026-02-26, via webdisclosure.com and annual-report.puma.com); prices Yahoo PUM.DE, ^GDAXI (OPENED, 2026-10-14) |
| Puma, Oct 30, 2025 | 84% below high, reset quarter | GM down | 6m +38 vs DAX | same |
| adidas, Oct 21, 2022 | 69% below high; reported revenue still growing, so not the Nike path | GM down (Q4 2022 large fall) | 6m +33, 12m +47 vs DAX | Yahoo ADS.DE (OPENED); margin from memory, not re-checked (unverified) |
| Nike, Apr 1, 2025 | revenue -9.3%, next -12.0% | next GM -442bp | 6m -10, 12m -46 vs S&P (in study) | SEC XBRL + Yahoo (OPENED) |
| Under Armour, Feb 2025 | revenue -5.7%, next -11.4% | next GM +165bp, op margin down | 6m -24, 12m -40 | same |
| Estee Lauder, Feb 2025 | revenue -6.4%, next -9.9% | next GM +305bp, op margin down | 6m +7, 12m +28 | same |

Puma is a margin-DOWN case that went up after 12 months, and adidas 2022 sits outside the bucket. Neither supports the idea that margin direction is the deciding variable for large European sportswear brands. Two cases, so not evidence either way. VF, Under Armour, Lululemon, Hanesbrands, Gap, Levi, Crocs, Skechers, Columbia and Foot Locker are all in the US panel. Lululemon, Levi, Skechers, Columbia and Hanesbrands produced no deduped Nike-path events with a scored outcome (their revenue declines were too shallow, or the setups are too recent).

## 6. Verdict

**History leans SHORT for Nike, weakly. It is not a coin flip in Nike's favor.**

- Probability Nike beats the S&P 500 over 6 months, weighted by bucket: about 0.78 x 39% + 0.22 x 29% = **about 37%** (expanded set), or about 41% (original 45, deduped). The median outcome is about -15 to -20 points. The base rate for all deeply fallen consumer stocks is 46% (DERIVED).
- At 12 months it is similar: about 38%. The Q4 FY27 reported gross margin drop (lapping 49.2%) falls inside that window.
- The rising margin is real but cost- and FX-led. Price and discount are taking margin away (ASP -30bp in Q1, "taking discounts"), and operating margin is guided down. The closest bucket (next GM up, next OM down) is 40% and 33%.
- **What would move it toward LONG:** Q2 FY27 gross margin well above 41% with the ASP line turning positive in the 10-Q bridge (pricing, not cost). The brand-only margin-up subset (7 of 12, median +11) becomes the relevant base rate if the Investor Day shows Nike behaving like Estee Lauder 2025 or Capri 2017 rather than Under Armour 2023-25.
- **What would make it strongly SHORT:** a Q2 gross margin below 40.6%. Then Nike is in the margin-down bucket: 27% at 6 months, 21% at 12, medians -25 and -31.

Strength of this finding as a counter to SHORT: **weak**. The scoreboard row 8 should read "Lean SHORT, weak" rather than "NEUTRAL, moderate". Suggested wording: "Falling-revenue setups mostly kept falling (33% beat the S&P 500 at 6 months). Rising gross margin helps but does not neutralize: 39% beat (median -14) versus 27% when margin fell. Nike's rise is cost and FX led, with price negative and operating margin guided down; closest bucket 40% (median -23)."

## 7. Files

- `data/hunt/risk_history/scripts/fetch.py`: SEC companyfacts and Yahoo download (generic User-Agent, no personal data).
- `scripts/panel.py`: quarterly revenue, gross margin and operating margin panel (logic copied from Round 3 `q2.py`).
- `scripts/study.py`: events in all four specs, with outcomes against the S&P 500, XRT and XLY.
- `scripts/analyze.py`, `analyze2.py`, `analyze3.py`: buckets, Wilson and cluster-bootstrap intervals, cost windows, robustness.
- `scripts/recent.py`: 2024-2026 setups scored at 6 months only.
- `out/quarterly_panel.csv` (73 tickers), `out/events_all.csv` (1,064 events), `out/analysis_*.txt`, `out/recent_setups.txt`.
- Rebuild: `python3 -I fetch.py <rawdir>`, then `panel.py <secdirs> out/quarterly_panel.csv <tickers>`, then `study.py out/quarterly_panel.csv <pxdirs> out`, then `analyze.py out/events_all.csv main`.
