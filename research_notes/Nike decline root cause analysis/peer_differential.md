# Root cause test: cross-cutting peer differential (how much of Nike's decline is Nike-specific?)

Research date: 2026-10-13. Hypothesis under test: *Decompose Nike's underperformance against adidas, Puma, ASICS, Deckers/Hoka, On, New Balance, Skechers, Anta, Li Ning, lululemon, Under Armour and VF by period, region, category and channel for 2019 to 2026. Whatever hit all peers is industry or structural; whatever hit only Nike is Nike-specific. Quantify the Nike-specific share.*

Status labels:
- **REPO**: verified number already in `data/nike_filing_facts.csv`, `data/nike_channel_split.csv` or `research_notes/04_financial_data_pack.md` (filing and printed page given there).
- **REPO-NOTE**: taken from an earlier repo note, with the status that note recorded.
- **OPENED**: I read the document or data file myself in this session (curl or WebFetch, converted to text). This includes SEC XBRL company-facts JSON from data.sec.gov, which I pulled today for Nike, Deckers, lululemon, Under Armour, VF, Skechers and On.
- **SNIPPET**: seen only in a search-result summary. Treat as a lead.

Conventions: local currency unless stated. "c-n" = currency-neutral. All arithmetic is mine and labelled "my arithmetic". To line up fiscal years with calendar years, Nike FY(t) (June to May) is mapped to calendar year t-1, because 7 of its 12 months fall in t-1. The same rule applies to Deckers, Under Armour and VF (years ending March) and lululemon (years ending late January or early February). So Nike FY2024 to FY2026 is compared with peers' 2023 to 2025. The remaining misalignment is up to 5 months. Peer-pool sums use constant approximate 2023 average exchange rates that I assumed (EUR 1.0813, CHF 1.1127, JPY 140.5, RMB 7.084 per USD). This is a constant-currency weighting device, not reported dollars.

Calculation scripts and downloads are in the session scratchpad (`pd/calc/panel.py`, `pd/adidas/`, `pd/puma/`, `pd/fil/`).

---

## 1. Bottom line

**Verdict: Nike-specific factors are the primary cause of the FY2024 to FY2026 decline. Measured against peers, the industry was a tailwind, not a headwind. But over 2019 to 2025 as a whole, Nike simply converged back to the incumbent cohort's path. Its long-run loss of share to the challengers is structural and shared by every incumbent.**

Five findings decide it:

1. **The decline is Nike-specific in timing, breadth and size.** Over Nike FY2024 to FY2026 (peers' 2023 to 2025), Nike fell 9.7% reported and about 10.8% currency-neutral (REPO; FY26 10-K p. 32 shows -9% and -2% c-n by year; compounding is my arithmetic). Nine of twelve peers grew. The three that shrank (Puma -10.9% like-for-like, Under Armour -12.9%, VF -3.1%) each have a documented reset of their own or a canvas/skate brand in its fashion down-cycle (Vans). Revenue-weighted, the peer pool grew **+15.4%**, the incumbent cohort (adidas, Puma, UA, VF, Skechers, Li Ning) grew **+6.2%** and the challenger cohort (ASICS, On, Deckers, lululemon, Anta, New Balance) grew **+31.1%** (my arithmetic, constant FX).
2. **Nike's share of the peer set fell from 36.4% (2021) to 35.0% (2023) to 29.7% (2025)** (Nike plus the twelve peers, constant FX, my arithmetic). Most of the loss falls in the last two years, after the industry's 2022 to 2023 inventory hangover, which Nike had outgrown.
3. **Over the long window, Nike is just an incumbent.** Indexed to 2019 = 100 in constant FX: incumbents 114 (2023) and 121 (2025); Nike 131 to 137 (FY2024) and 119 to 124 (FY2026), depending on whether FY2019 or FY2020 is the base; challengers 207 and 267. Nike ran about 15 to 20 points *above* the incumbent cohort at its FY2023 to FY2024 peak, then fell back to parity. Every incumbent definition I tested gives a 2025 index of 114 to 121. The FY24 to FY26 decline is the loss of a Nike-specific premium built in FY2021 to FY2024. Nike did not fall below where an incumbent would be. The long-run gap to the market as a whole (US athletic footwear grew at a 4.0% CAGR in 2019 to 2024 per Euromonitor via HGI, against Nike's 2.5% FY2019 to FY2026 CAGR) is shared with adidas, Puma, UA and VF. That gap is structural fragmentation toward challengers.
4. **The Nike-specific signature is in the channel and the category.** In channel terms it is Nike Direct, especially digital. In category terms it is footwear, and within footwear the classic lifestyle franchises.
   - NIKE Direct fell about 19% c-n over FY24 to FY26 (-12%, then -8%; FY26 10-K p. 32). That is $3,799M reported, 77% of the $4,964M total decline (REPO, my arithmetic).
   - Over the same window, adidas DTC grew about 21% c-n (+11% in 2024, +9% in 2025), Deckers DTC +6.3% (FY26) and On DTC +34% cc (Q2 2026). Puma, in the middle of its own reset, still grew DTC 3.4% c-a in 2025.
   - Nike footwear fell 12.8% c-n while adidas footwear grew 25% c-n.
   - Nike apparel fell only 3.1% c-n, against a mixed apparel peer set: adidas +22%, lululemon +15%, UA -13%, Puma -10% (2025 only).
5. **By region, the Nike-specific gap is largest in Greater China and EMEA and smallest in North America.**
   - Nike's two-year c-n changes: North America -3.4%, EMEA -12.7%, Greater China -23.4%, APLA -4.0% (FY26 10-K p. 36; compounding is my arithmetic).
   - Comparable adidas segments, c-n: North America +2.3%, Europe +28.4%, Greater China +20.2%, Latin America about +54% (inflated by hyperinflation accounting), Japan/South Korea about +22%.
   - In FY2026 alone, Nike North America (+5% c-n) sits inside the North American peer range: adidas +4% (+10% for the brand ex-Yeezy), ASICS +5.8%, Deckers domestic +0.2%, lululemon US -2.4%, UA -8%, Puma Americas -10%.
   - Greater China is the outlier that is still widening. In Q2 2026 adidas Greater China grew 15% c-n, while in Q1 FY27 Nike Greater China fell 26% c-n.

**Quantification (section 5).** Of the FY24 to FY26 net decline of $4,964M:
- Market-wide effects (things that hit all peers) were a **tailwind of $0 to about +$3B**.
- FX was a tailwind of about **$0.56B**.
- Shocks shared with a cohort rather than the whole industry (the canvas and classic lifestyle cycle that hit Vans, Converse and Nike's classics) cost about **$0.7B to $0.9B**.
- The **Nike-specific residual is about $4.7B to $7.8B**. That is roughly **95% to 155% of the net decline** and **about 85% to 90% of the gross headwinds**.

By region, the Nike-specific gap against regional benchmarks splits roughly one-third Greater China, one-third EMEA, one-sixth North America, one-seventh APLA, plus a small Converse-specific piece. In the FY2027 leg the industry share rises, because peers slowed in 2026: lululemon -4.3%, Deckers +5.7%, Puma -9.4% and UA -3.2% in their latest quarters. Nike ex-Greater China fell only 0.8% in Q1 FY27 (REPO-NOTE), roughly in line with a slowing industry. What remains clearly Nike-specific is China.

**Independent cause or symptom?** The peer differential is a *measurement*, not a mechanism. It shows that the cause is inside Nike, and its signature points upstream:
- The Consumer Direct Acceleration channel bet: the Direct and digital collapse is unique to Nike.
- Over-reliance on classic lifestyle franchises: footwear, and the Dunk/AF1/AJ1 fade.
- Nike's China channel and discount problems: China diverges from adidas, ASICS and lululemon in the same market.
These are covered in `dtc_wholesale.md`, `franchise_oversupply.md` and `china.md`.

**Fixable by management: mostly yes, partly already fixed.**
- The Nike-specific part is fixable by definition, and North America shows it: Nike re-converged with NA peers within about four quarters of the wholesale and product reset.
- The structural part is not fixable by Nike alone: incumbents as a group losing share of growth to challengers (about 6 to 7 share points of the US market moved from Nike, VF, adidas and UA to On, Hoka, New Balance, ASICS and Brooks between 2019 and 2025, per Euromonitor via HGI).
- Recovering to the incumbent line is realistic. Recovering the FY2024 premium over incumbents is not, because that premium was itself inflated by DTC pricing and classics oversupply.

---

## 2. Predictions and results

| # | Prediction if Nike's decline is Nike-specific (vs industry) | Result | Held? |
|---|---|---|---|
| P1 | **Timing.** The divergence from peers should start on a Nike-specific date, not coincide with industry shocks (COVID 2020, the 2022 to 2023 inventory bullwhip, the 2026 slowdown). | Nike kept pace with or beat incumbents in 2021 to 2023. Nike's share of the peer set was 36.4% (2021), 36.0% (2022), 35.0% (2023): -1.4 pts in two years. It then fell to 30.9% (2024) and 29.7% (2025): -5.3 pts. In 2023 adidas was flat c-n with North America -16%, and Vans fell 24%, while Nike FY24 was +0.3%. In CY2024 (Nike FY25) peers grew +8.8% and Nike fell 9.8%. Quarterly: in Nike's Q1 FY25 (Jun to Aug 2024, -10%), Deckers grew +22.1% (Apr to Jun 2024), lululemon +7.3%, Skechers +7.2% and +15.9%, On +27.8%. Only UA (-10.1%) and VF (-15.2%) fell (SEC XBRL, OPENED). | **Yes** |
| P2 | **Breadth.** If industry-driven, most peers should decline too, and by similar amounts. | 9 of 12 peers grew over 2023 to 2025: adidas +15.8% (EUR), ASICS +42.2% (JPY), On +68.2% (CHF), Deckers +27.6%, lululemon +15.4%, Anta +28.6% (RMB), Li Ning +7.2%, New Balance +41.5% (unaudited), Skechers about +23% (2025 estimated from H1 growth). Decliners: Puma -10.9% (H2 2025 reset), UA -12.9% (turnaround), VF -3.1% (Vans). Pool +15.4% constant FX. | **Yes** |
| P3 | **Geography.** A Nike-specific cause should show a gap in every region, regardless of local market conditions. An industry cause should track each local market. | Two-year c-n, Nike vs adidas: NA -3.4% vs +2.3%; EMEA -12.7% vs Europe +28.4%; Greater China -23.4% vs +20.2%; APLA -4.0% vs Latin America +54% (hyperinflation-inflated) and Japan/South Korea +22%. The Greater China market grew (NBS sports goods +11.1% in 2024, +15.7% in 2025, REPO-NOTE), as did ASICS China (+19.9% in 2025) and lululemon China Mainland (+82% over two years). The gap appears everywhere. It is largest in China and EMEA and smallest in NA. | **Yes**, with NA the weakest case |
| P4 | **Category.** A Nike-specific franchise problem should concentrate the gap in footwear. A general sportswear demand slump would hit apparel equally. | Nike footwear c-n -12.8% (-11%, -2%) vs apparel -3.1% (-5%, +2%) (FY26 10-K p. 32). adidas footwear +25.2% c-n (+17%, +7%), apparel +21.9% (+6%, +15%). The footwear gap is about -38 pts; the apparel gap is about -25 pts against adidas but only about -6 pts against the four-peer apparel median (adidas, lululemon, UA, Puma). On shoes +27.5% CHF in 2025 alone. Euromonitor puts US athletic footwear growth at 4.0% CAGR 2019 to 2024. | **Yes** |
| P5 | **Channel.** If an industry-wide channel shift (DTC fatigue, e-commerce saturation) were the cause, peers' DTC should also fall. | Nike Direct -19% c-n (FY24 to FY26), wholesale -2.2% c-n. adidas DTC +11% (2024) and +9% (2025) c-n, e-commerce +6% (group) and +16% (brand) in 2025, wholesale +14% and +10%. Puma DTC +3.4% c-a in 2025 even while wholesale fell 12.8%. Deckers DTC +6.3% (FY26). On DTC +34.3% cc (Q2 2026). Skechers DTC +8.8% (H1 2025). No peer's DTC fell double digits. | **Yes, strongest signature** |
| P6 | **Shared-cohort control.** Shocks that hit only one niche (canvas and classic lifestyle) should show up at Nike's niche brands *and* at peers in the same niche. That part is not Nike-specific. | Converse c-n: FY24 -15%, FY25 -18%, FY26 -32%. Vans: FY24 -24%, FY25 -16%, FY26 -9% (REPO-NOTE `emea_converse_jordan.md`). The two track each other in FY24 and FY25; Converse diverges in FY26 (deliberate reset). The cohort part is about $0.5B for Converse plus $0.2B to $0.4B of the classics fade (REPO-NOTE `macro_covid_cycle.md`). | **Yes**: a real shared component exists, but it is small |
| P7 | **Long window.** If Nike had a structural Nike-only problem since 2019, it should lag the incumbent cohort over 2019 to 2025, not just the challengers. | Index 2019 = 100: incumbents 121.3 (2025), with a 113.8 to 121.3 range across cohort definitions; Nike 118.6 (FY2019 base) or 124.0 (FY2020 base); challengers 266.6. Nike North America FY2019 to FY2026 +29% ($15,902M to $20,511M, REPO) vs adidas North America (adidas brand) 2019 to 2025 +5% (EUR 4,828M to 5,087M). Nike Greater China FY2020 to FY2026 -12% ($6,679M to $5,847M, REPO) vs adidas China -31% (EUR 5,278M country sales incl. Reebok to 3,623M). | **No.** Over the long window Nike matches or beats the incumbents. The long-run share loss is cohort-wide. |
| P8 | **Convergence where fixed.** If the gap is Nike-specific and management acts, it should close first where Nike acted (NA wholesale and running reset) and persist where it has not (China). | FY26 Nike NA +5% c-n, within the NA peer range (adidas +4%, ASICS +5.8%, Deckers domestic +0.2%, lululemon US -2.4%, UA -8%, Puma Americas -10%). Q1 FY27: Nike ex-China -0.8% (REPO-NOTE) vs latest peer quarters lululemon -4.3%, Deckers +5.7%, UA -3.2%, Puma -9.4%, adidas +14% c-n, On +21.6% cc. Greater China Q1 FY27 -26% c-n vs adidas Greater China Q2 2026 +15% c-n. | **Yes** |
| P9 | **Margins and stock (side tests).** Tariffs hit all peers, so gross margin pressure should be shared. A sector de-rating should hit healthy peers' stocks too. | Gross margin: Nike 44.6% (FY24) to 42.9% (FY26), REPO. adidas 47.5% (2023) to 51.6% (2025), up despite tariffs. Puma 46.3% to 47.4% (2023 to 2024). UA -240 bp in FY26, "mainly tariffs" (REPO-NOTE). Tariffs are shared; Nike's markdown and mix pressure is not. Stock, Nov 5, 2021 to Oct 12, 2026: Nike -80%, adidas -50%, Anta -43%, On -10%, Deckers +19%, Puma -79%, UA -80%, VF -79%, lululemon -80% (scratchpad price files; REPO-NOTE `valuation_vs_business.md`). About half of Nike's price fall is a sector-wide multiple compression. | **Partly** (the industry share is larger for the stock than for revenue) |

---

## 3. Evidence in detail

### 3.1 The peer panel (local currency, millions; calendar mapping as in the conventions)

| Company | 2019 | 2021 | 2023 | 2024 | 2025 | 2019 to 2025 | 2023 to 2025 | Source |
|---|---|---|---|---|---|---|---|---|
| Nike (USD; FY2020 for 2019, ..., FY2026 for 2025) | 37,403 | 46,710 | 51,362 | 46,309 | 46,398 | +24.0% (FY19 to FY26: +18.6%) | -9.7% (c-n about -10.8%) | REPO |
| adidas (EUR) | 23,640 (incl. Reebok; about 21,893 ex-Reebok, my arithmetic) | 21,234 | 21,427 | 23,683 | 24,811 | +13.3% ex-Reebok | +15.8% (c-n +12%, +10%) | adidas AR 2025 ten-year overview p. 425, OPENED; adidas AR 2020 segment note (Reebok 2019 by segment), OPENED; FY2024 and FY2025 releases, OPENED |
| Puma (EUR) | 5,502.2 | 6,805.4 | 8,601.7 | 8,817.2 | 7,660 like-for-like (7,296.2 reported after PUMA United restatement) | +39.2% | -10.9% (c-a +4.4%, -8.1%) | Puma AR2024 group development table, OPENED; Puma FY2025 release, Feb 26, 2026, OPENED; 2024 +4.4% c-a, SNIPPET |
| ASICS (JPY m) | 378,050 (unverified) | 404,082 | 570,463 | 678,526 | 810,916 | +114.5% | +42.2% (2025 c-n +19.4%) | ASICS FY2025 summary, Feb 13, 2026, OPENED (2024, 2025); marketscreener and Modaes, SNIPPET (2021 to 2023); 2019 unverified |
| On (CHF) | 267.1 | 724.6 | 1,792.1 | 2,318.3 | 3,014.0 | +1,028% | +68.2% | SEC XBRL (20-F), OPENED |
| Deckers (USD; FY Mar) | 2,132.7 | 3,150.3 | 4,287.8 | 4,985.6 | 5,472.3 | +156.6% | +27.6% | SEC XBRL, OPENED; FY26 10-K, OPENED |
| lululemon (USD; FY Jan/Feb) | 3,979.3 | 6,256.6 | 9,619.3 | 10,588.1 | 11,102.6 | +179.0% | +15.4% | SEC XBRL, OPENED |
| Under Armour (USD) | 5,267.1 | 5,682.6 | 5,701.9 | 5,164.3 | 4,966.4 | -5.7% | -12.9% | SEC XBRL, OPENED |
| VF (USD; FY Mar) | 10,488.6 | 11,841.8 | 9,915.7 | 9,504.7 | 9,605.2 | -8.4% | -3.1% | SEC XBRL, OPENED (values as filed; later divestitures not restated) |
| Skechers (USD) | 5,220.1 | 6,310.2 | 8,000.3 | 8,969.4 | n/a (taken private Sep 2025); H1 2025 +10.0% | about +89% (2025 estimated) | about +23% (2025 estimated) | SEC XBRL and Q2 2025 10-Q, OPENED |
| Anta (RMB) | 33,928 | 49,328 | 62,356 | 70,826 | 80,219 | +136.4% | +28.6% | Anta AR 2025 five-year summary, OPENED; 2019, SNIPPET |
| Li Ning (RMB) | 13,870 | 22,572 | 27,598 | 28,676 | 29,598 | +113.4% | +7.2% | SNIPPET (Li Ning AR 2023 via search; STCN Mar 2026) |
| New Balance (USD, unaudited) | n/a | about 4,380 (implied) | 6,500 | 7,800 | 9,200 | n/a | +41.5% | SNIPPET (2023, 2024); 2025 OPENED (repo) NB business update |

Cohort sums at constant 2023 FX (my arithmetic, `panel.py`):

| Year | Peer pool (USD m, const FX) | Nike | Nike share | Peer YoY | Nike YoY |
|---|---|---|---|---|---|
| 2021 | 81,773 | 46,710 | 36.4% | +27.7% | +4.9% |
| 2022 | 90,994 | 51,217 | 36.0% | +11.3% | +9.6% |
| 2023 | 95,248 | 51,362 | 35.0% | +4.7% | +0.3% |
| 2024 | 103,610 | 46,309 | 30.9% | +8.8% | -9.8% |
| 2025 | 109,955 | 46,398 | 29.7% | +6.1% | +0.2% |

The 2020 figure (41.0%) is distorted: Nike's FY2021 recovery year is set against peers' COVID-hit calendar 2020, so I start the series in 2021. New Balance's 2021 figure is implied from "up 21%" in 2022 (SNIPPET). Skechers 2025 applies H1 2025 growth (estimate).

Index (2019 = 100, constant FX, New Balance excluded for lack of a 2019 figure):

| Year | Incumbents (adidas, Puma, UA, VF, Skechers, Li Ning) | Challengers (ASICS, On, Deckers, lululemon, Anta) | Nike (FY2020 base) | Nike (FY2019 base) |
|---|---|---|---|---|
| 2019 | 100.0 | 100.0 | 100.0 | 95.6 |
| 2020 | 87.5 | 106.4 | 119.1 | 113.9 |
| 2021 | 109.1 | 144.4 | 124.9 | 119.4 |
| 2022 | 117.2 | 173.7 | 136.9 | 130.9 |
| 2023 | 114.1 | 207.1 | 137.3 | 131.3 |
| 2024 | 119.5 | 237.5 | 123.8 | 118.4 |
| 2025 | 121.3 | 266.6 | 124.0 | 118.6 |

Sensitivity: the incumbent 2025 index is 113.8 without Skechers, 117.7 without Li Ning, 118.5 for adidas plus Puma, and 113.3 for adidas alone. In every case Nike ends at roughly the incumbent line. The 2023 gap above incumbents ranges from about +17 to +39 points depending on base and definition (the top end is adidas alone).

**Reading.** Two different stories sit in one chart. (a) Since 2019, the whole incumbent cohort, Nike included, has lost share of growth to challengers that grew 2.7x. That is industry structure. (b) Nike alone rose well above the incumbent line in FY2021 to FY2024, then fell back to it in FY2025 to FY2026. That round trip is Nike-specific. The FY24 to FY26 decline is (b).

### 3.2 Region by region (two-year c-n unless stated; Nike FY24 to FY26, peers 2023 to 2025)

Nike segment c-n by year (FY26 10-K p. 36, OPENED): NA -8%, +5%; EMEA -10%, -3%; Greater China -12%, -13%; APLA -3%, -1%; Converse -18%, -32%. Compounded (my arithmetic): NA -3.4%, EMEA -12.7%, GC -23.4%, APLA -4.0%, Converse -44.2%.

| Region | Nike | Peers (same window) | Gap vs plausible benchmark |
|---|---|---|---|
| North America | -3.4% | adidas NA -1.6%, +4% (c-n; +10% brand ex-Yeezy in 2025) = +2.3% (FY2024 and FY2025 releases, OPENED). lululemon US $6,346M to $6,328M, -0.3%; Americas +2.8% (10-K, OPENED). Deckers domestic $2,863.7M to $3,191.5M, +11.4%, of which FY26 +0.2% (10-K, OPENED). UA NA -11%, -8% = -18.1% (8-Ks, OPENED). Puma Americas +7.0%, -10.0% = -3.7% (SNIPPET, OPENED). ASICS NA 2025 +5.8% c-n (OPENED). On Americas CHF 1,162.2M to 1,740.1M, +49.7% (20-F, OPENED). Skechers Americas H1 2025 +4.6% (10-Q, OPENED). Market: Circana US footwear flat in 2024 and 2025; US footwear PCE +1.8%, +4.4% (REPO-NOTE). | Benchmark 0% to +6% gives a gap of -3 to -10 pts, about **$0.7B to $2.0B** on a $21.4B base. FY2026 alone: no gap. |
| EMEA | -12.7% | adidas Europe +18.9% (2024), +8% (2025) = +28.4%. Puma EMEA +2.1%, -6.9% = -5.0%. ASICS Europe 2025 +22.1% c-n. On EMEA CHF 488.7M to 762.7M, +56%. Skechers EMEA H1 2025 +29.4%. UA EMEA flat, +3% c-n. New Balance Europe "30%+" in 2025 (REPO-NOTE). | Benchmark 0% to +10% (excluding the outliers adidas and On) gives a gap of -13 to -23 pts, about **$1.7B to $3.1B** on $13.6B. |
| Greater China | -23.4% | adidas Greater China +10.3%, +9% = +20.2% (brand +13% in 2025). ASICS GC +19.9% (2025). lululemon China Mainland $964M to $1,755M, +82%. Anta +28.6% (group). Li Ning +7.2%. Puma APAC +3.8%, -7.4% (GC soft). Skechers APAC H1 2025 +1.4%. Market: NBS sports goods +11.1% and +15.7% (REPO-NOTE). | Benchmark +5% to +15% (local mass brands to foreign premium) gives a gap of -28 to -38 pts, about **$2.1B to $2.9B** on $7.5B. |
| APLA | -4.0% | adidas Latin America +27.6%, +21% (hyperinflation-inflated), Japan/South Korea +10.1%, +11%, Emerging Markets +19.4%, +15%. ASICS Japan +22.7%, Oceania +19.2% c-n, Southeast and South Asia +33.0% (2025). UA Asia-Pacific -13%, -6%; UA Latin America flat, +6%. Puma APAC -3.9%. | Benchmark +5% to +20% gives a gap of -9 to -24 pts, about **$0.6B to $1.6B** on $6.7B. |
| Converse | -44.2% | Vans FY24 to FY26 path about -24% (REPO-NOTE) | Converse-specific excess about **$0.26B to $0.4B** (REPO-NOTE). The rest is the shared canvas cycle. |

Midpoints of the regional gaps (my arithmetic): China about $2.5B, EMEA about $2.4B, NA about $1.3B, APLA about $1.1B, Converse about $0.3B. Shares of the summed gap: **China about 33%, EMEA about 32%, NA about 17%, APLA about 14%, Converse about 4%.** These gaps measure shortfall against benchmarks, not Nike's own dollar decline, so they sum to more than $4.96B. The ranking is more robust than the levels.

Long-window regional natural experiments (local currency, reported):
- North America: Nike +29% (FY2019 to FY2026) vs adidas brand +5% (2019 to 2025).
- China: Nike -12% (FY2020 to FY2026) vs adidas -31% (2019 country sales including a small Reebok business, to 2025).
- So the long-run China decline is shared by foreign incumbents (the guochao and 2021 boycott era). The 2024 to 2026 China decline is Nike-only: adidas has grown 2024 to 2026 while Nike fell.

### 3.3 Category

- Nike, FY24 to FY26 (FY26 10-K p. 32, OPENED): footwear $33,427M to $29,525M (-11%, -2% c-n); apparel $13,775M to $13,449M (-5%, +2%); equipment +6%, -2%.
- adidas (ten-year overview p. 425 and releases, OPENED): footwear EUR 12,139M (2023) to 14,232M (2025), c-n +17% and +7% (+12% brand); apparel EUR 7,806M to 8,764M, c-n +6% and +15%.
- Puma (OPENED): footwear EUR 4,733.6M to 4,113.8M (2025, -7.1% c-a); apparel 2,703.7M to 2,328.5M (-9.7%), restated basis.
- On: shoes CHF 2,199.6M to 2,804.4M in 2025 (+27.5%) (20-F, OPENED).
- The footwear gap against the best incumbent is about -38 pts. The apparel gap against the apparel peer median is about -6 pts. Nike's peer-relative problem is a footwear problem, matching the repo finding that footwear accounts for 94% of the FY24 to FY26 decline (REPO-NOTE `challengers_taste.md`).

### 3.4 Channel

- Nike (FY26 10-K p. 32, OPENED): NIKE Direct $21,519M to $17,720M (-12%, -8% c-n); wholesale $27,758M to $27,453M (-6%, +4% c-n).
  - North America: Direct -12% then -6%, wholesale -5% then +14%.
  - EMEA: Direct -16% then -9%.
  - Greater China: Direct -12% then -12%; digital -29% in FY26 (REPO-NOTE).
- adidas (OPENED): DTC +11% (2024) and +9% (2025) c-n; wholesale +14% and +10%.
- Others (OPENED): Puma DTC +3.4% c-a (2025); Deckers DTC +6.3% and wholesale +12.3% (FY26); Skechers DTC +8.8% and wholesale +11.0% (H1 2025); On DTC CHF 388.4M, +34.3% cc (Q2 2026, repo competitors note OPENED).
- Nike Direct accounts for $3,799M of the $4,964M total decline (77%, my arithmetic on REPO).
- No peer had a double-digit DTC decline. This is the single cleanest Nike-only signature. It ties the decline to the Consumer Direct Acceleration build-up and to the 2024 to 2025 deliberate cuts in classics and digital promotion.

### 3.5 Timing, quarter by quarter (SEC XBRL quarterly revenue, OPENED; YoY my arithmetic)

| Quarter ending | Nike | Deckers | lululemon | Skechers | Under Armour | VF | On |
|---|---|---|---|---|---|---|---|
| mid-2023 | Aug 2023 +2.0% | Jun 2023 +10.0% | Jul 2023 +18.2% | Jun 2023 +7.7% | Jun 2023 -2.4% | Jul 2023 -7.7% | Jun 2023 +52.3% |
| mid-2024 | Aug 2024 -10.4% | Jun 2024 +22.1% | Jul 2024 +7.3% | Jun 2024 +7.2% | Jun 2024 -10.1% | Jun 2024 -15.2% | Jun 2024 +27.8% |
| late 2024 | Nov 2024 -7.7% | Sep 2024 +20.1% | Oct 2024 +8.7% | Sep 2024 +15.9% | Sep 2024 -10.7% | Sep 2024 -5.6% | n/a |
| mid-2025 | Aug 2025 +1.1% | Jun 2025 +16.9% | Aug 2025 +6.5% | Jun 2025 +13.1% | Jun 2025 -4.2% | Jun 2025 -0.5% | Jun 2025 +32.0% |
| mid-2026 | Aug 2026 -4.3% | Jun 2026 +5.7% | Aug 2026 -4.3% | private | Jun 2026 -3.2% | n/a | Jun 2026 +13.5% reported, +21.6% cc |

Also: adidas group c-n +12% (2024), +10% (2025), +14% (Q2 2026); Puma -9.4% organic (Q2 2026) (OPENED). Reading: Nike's fall in mid-2024 coincided only with the two peers in their own resets (UA, VF/Vans). By mid-2026 the industry itself has slowed, so Nike's peer gap is narrowing outside China.

### 3.6 Market-size cross-check

- US athletic footwear: 4.0% CAGR 2019 to 2024, forecast 2.9% for 2024 to 2030. Nike US share 34.1% (2019) to 28.9% (2025); adidas 11.0% to 10.1%; VF 9.4% to 3.9%; UA 2.7% to below the top ten; On 6.3%, Deckers 3.8%, NB 3.6% to 6.4% (Euromonitor Passport Dec 18, 2025, via HGI, Jan 13, 2026, OPENED).
- Globally, Nike's share fell 540 bp to 22.9% over ten years, in a $168B global athletic footwear market (same source).
- Circana: US footwear $89.2B (2024) and about $90B (2025), both flat (REPO-NOTE). Euromonitor forecasts 2% global sportswear CAGR 2025 to 2030 (SNIPPET; press page not reachable).
- Consequence: a "hold share" counterfactual from FY2024 gives Nike FY2026 revenue of about $51.4B to $54.5B (market flat to +6%). Actual is $46.4B.

---

## 4. Strongest evidence for and against

**For (Nike-specific dominates the FY24 to FY26 decline):**
1. The constant-FX peer pool grew 15.4%, and the incumbent cohort alone 6.2%, while Nike fell about 10.8% c-n over the same two years. Nike's share of the peer set fell 5.3 points in 2024 to 2025, against 1.4 points in 2021 to 2023.
2. No peer's DTC fell double digits. Nike Direct fell about 19% c-n and accounts for 77% of the decline.
3. Greater China: adidas +20%, ASICS +20% (2025), lululemon China +82% over the window, against Nike -23% c-n. The gap is still widening (Q2 2026 adidas +15% vs Q1 FY27 Nike -26%).
4. EMEA: adidas Europe +28%, ASICS Europe +22% (2025), On EMEA +56%, against Nike -12.7%.
5. North America converged with peers within four quarters of Nike's own wholesale and running reset (FY26 +5% c-n, NA wholesale +14%). That is what a fixable, firm-specific problem looks like.

**Against (or limiting):**
1. Over 2019 to 2025 Nike tracks the incumbent cohort: index about 119 to 124 vs 114 to 121. Nike's long-run share loss (US 34.1% to 28.9%; global -540 bp over ten years) is shared with adidas, VF, UA and Puma. It is industry structure (fragmentation toward On, Hoka, NB, ASICS), not a Nike-only defect.
2. A real cohort shock hit Nike's lifestyle niche: Vans tracked Converse in FY24 and FY25, and classic lifestyle silhouettes faded across brands. That is about $0.7B to $0.9B of the decline.
3. Peers slowed sharply in 2026 (lululemon -4.3%, UA -3.2%, Puma -9.4%, Deckers +5.7%, Li Ning +2.8%, Anta brand +4.8%; China NBS sports goods -3.7% Jan to Aug 2026). The FY2027 leg therefore has a larger industry component.
4. Peer selection bias: the "peer pool" includes the winners that took Nike's share. Their growth is partly Nike's loss, so the pool overstates the counterfactual. That is why I use the incumbent cohort and market-size data as the main benchmarks.
5. The stock: about half of Nike's 80% price fall is sector-wide multiple compression (adidas -50% on rising revenue; Puma, UA, VF and lululemon -79% to -80%) (REPO-NOTE `valuation_vs_business.md`).

---

## 5. Quantification

FY24 to FY26 net revenue change: -$4,964M (REPO). Decomposition (my arithmetic):

| Component | Basis | Amount |
|---|---|---|
| Market-wide (hit all peers) | Market growth 0% (Circana US flat) to +6% (global and US PCE) on a $51.4B base | **+$0 to +$3.1B** (tailwind) |
| FX | Reported -9.7% vs c-n about -10.8% | about **+$0.56B** (tailwind) |
| Cohort shock (canvas and classic lifestyle cycle, shared with Vans) | Converse about $0.5B (Vans-matched), classics fade not caused by Nike $0.2B to $0.4B (REPO-NOTE) | **-$0.7B to -$0.9B** |
| Nike-specific residual | Net change minus the rows above | **-$4.7B to -$7.8B** |

- The Nike-specific residual is **about 95% to 155% of the net decline** and **about 85% to 91% of the gross headwinds** (residual divided by residual plus cohort shock).
- Cross-check with the incumbent cohort: had Nike grown with the incumbents (+6.2%), FY2026 revenue would be about $54.5B, a shortfall of about $8.1B. With the market flat, the shortfall is about $5.0B. The residual range brackets both.
- Regional split of the Nike-specific shortfall: China about 33%, EMEA about 32%, North America about 17%, APLA about 14%, Converse-specific about 4%.
- **FY2027 leg (guided high-single-digit decline):** the industry share rises. US and European peers are now flat to down, and China's market is negative in 2026. My estimate is that the Nike-specific share falls to roughly 50% to 70% of the FY27 decline, almost all of it Greater China (Nike -26% vs adidas +15%) and Converse. Confidence is low.
- **Long window caveat:** measured from FY2019, Nike is at the incumbent line. Of the cumulative underperformance against the total market since 2019, essentially none is Nike-specific; it is incumbent-cohort structure. The FY24 to FY26 decline is the unwinding of a Nike-specific premium, not a fall below the cohort.

---

## 6. Independent cause or symptom; fixability

- **Symptom, not a mechanism.** The differential is a diagnostic. It locates the cause inside Nike and points to the upstream causes covered in companion notes:
  1. The DTC and digital build-up and its unwinding (`dtc_wholesale.md`, `digital_tech.md`).
  2. Footwear franchise over-reliance and oversupply (`franchise_oversupply.md`, `innovation_drought.md`).
  3. China channel and discount mismanagement (`china.md`).
- **Fixable: mostly.**
  - The Nike-specific premium-loss is reversible to the incumbent line, as North America showed in FY2026.
  - China is the open case: Nike's own guidance says China actions "extend beyond fiscal 2027" (REPO).
  - Not fixable by Nike: the incumbent cohort's structural share loss to challengers, the canvas and classics fashion cycle, and the sector de-rating of the stock.

---

## 7. Sources

| # | Source | Date | Status | Used for |
|---|---|---|---|---|
| 1 | Nike filings via `research_notes/04_financial_data_pack.md`, `data/nike_filing_facts.csv`, `data/nike_channel_split.csv` | FY2019 to Q1 FY2027 filings | REPO | All Nike totals, segments, channels, FY c-n growth |
| 2 | Nike FY2026 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm, pp. 32 to 37 | 2026-07-15 | OPENED (scratchpad copy) | Footwear, apparel, Direct and wholesale c-n by year; segment c-n; NA, EMEA and GC product and channel tables |
| 3 | adidas Annual Report 2025, ten-year overview p. 425 and segmental note, https://res.cloudinary.com/confirmed-web/image/upload/v1790580010/adidas-group/investors/financial-publications/2025/FY/2025_annual_report_adidas_EN_kpmxtm.pdf | 2026 | OPENED | adidas sales, footwear and apparel 2016 to 2025; 2024 and 2025 segments; gross margins |
| 4 | adidas Annual Report 2023 PDF, https://res.cloudinary.com/confirmed-web/image/upload/v1714487129/adidas-group/investors/financial-publications/2023/2023_annual_report_adidas_EN_final_cctsob.pdf | 2024 | OPENED | 2022 and 2023 segment sales and c-n; footwear and apparel 2023 |
| 5 | adidas Annual Report 2021, note 36, https://report.adidas-group.com/2021/en/consolidated-financial-statements/notes/additional-information/36-segmental-information.html | 2022 | OPENED | 2020 and 2021 segment sales (Greater China EUR 4,597M in 2021, NA EUR 5,105M) |
| 6 | adidas Annual Report 2020, note 38, https://report.adidas-group.com/2020/en/consolidated-financial-statements/notes/additional-information/38-segmental-information.html | 2021 | OPENED | 2019 adidas-brand NA EUR 4,828M; Reebok 2019 by segment; China country sales EUR 5,278M |
| 7 | adidas FY2024 results release PDF, https://res.cloudinary.com/confirmed-web/image/upload/v1741155965/adidas-group/investors/financial-publications/2024/Q4/adidasAG_FY_2024_Results_EN_vf_ptevlo.pdf | 2025-03-05 | OPENED | 2024 segment c-n, group +12%, DTC +11%, wholesale +14%, footwear +17% |
| 8 | adidas FY2025 results release (scratchpad `ads/fy2025.txt`) | 2026-03-04 | OPENED | 2025 c-n by segment, product and channel; group +10% incl. Yeezy |
| 9 | adidas Q2 2026 results release (scratchpad `ads/q2_2026.txt`) | 2026-07-30 | OPENED | Q2 and H1 2026 by segment, product, channel |
| 10 | Puma AR2024 group development, https://annual-report.puma.com/2024/en/downloads/PUMA_AR2024_group_development_EN.pdf | 2025 | OPENED | Puma 2015 to 2024 sales, footwear, apparel, gross margin |
| 11 | Puma FY2025 release, https://about.puma.com/en/newsroom/corporate-news/2026/26-02-2026-puma-completes-reset-2025-2026-designated-transition-year | 2026-02-26 | OPENED | 2025 sales (restated), regions, products, channels |
| 12 | Puma FY2024 release (search summary), https://about.puma.com/en/newsroom/corporate-news/2025/12-03-2025-puma-grows-currency-adjusted-sales-44-2024-and-provides | 2025-03-12 | SNIPPET | 2024 c-a +4.4%; Americas +7.0%, APAC +3.8%, EMEA +2.1% |
| 13 | ASICS FY2025 summary of consolidated results (scratchpad `hk/asics.txt`) | 2026-02-13 | OPENED | 2024 and 2025 sales, segments, categories |
| 14 | ASICS 2021 to 2023 sales (marketscreener, Modaes, SGI Europe) | 2022 to 2024 | SNIPPET | 2021 to 2023 yen sales; 2019 and 2020 unverified |
| 15 | SEC XBRL company facts (data.sec.gov) for NKE, DECK, LULU, UAA, VFC, SKX, ONON | retrieved 2026-10-13 | OPENED | Annual and quarterly revenue |
| 16 | lululemon FY2025 10-K, https://www.sec.gov/Archives/edgar/data/1397187/000139718726000020/lulu-20260201.htm | 2026-03-17 | OPENED | US, Americas, China Mainland revenue FY2023 to FY2025 |
| 17 | Skechers Q2 2025 10-Q, https://www.sec.gov/Archives/edgar/data/1065837/000095017025105871/skx-20250630.htm | 2025-08-08 | OPENED | H1 2025 regional, DTC, wholesale growth |
| 18 | On Holding 2025 20-F, https://www.sec.gov/Archives/edgar/data/1858985/000185898526000008/onholdingag-20251231.htm | 2026-03-03 | OPENED | Regional and product sales 2023 to 2025 |
| 19 | Deckers FY2026 10-K, https://www.sec.gov/Archives/edgar/data/910521/000162828026037664/deck-20260331.htm | 2026-05-22 | OPENED | HOKA $2,587.3M (+15.9%), domestic vs international, DTC vs wholesale |
| 20 | Under Armour FY2026 Q4 and FY2025 Q4 8-K Ex. 99.1 (scratchpad `ua/`) | 2026-05-12; 2025-05-13 | OPENED | Regional growth FY25 and FY26 |
| 21 | Anta Annual Report 2025, five-year financial summary (scratchpad `hk/anta2025.txt`) | 2026 | OPENED | Revenue 2021 to 2025 |
| 22 | Anta 2019 and 2020 revenue (winshang, 36kr.jp) | 2021 | SNIPPET | RMB 33.93B, 35.51B |
| 23 | Li Ning 2019 to 2023 (hkexnews AR 2023 via search) and 2024 to 2025 (STCN, https://www.stcn.com/article/detail/3688297.html) | 2024; 2026-03-20 | SNIPPET | Li Ning revenue series |
| 24 | New Balance sales 2020, 2022 to 2024 (Wikipedia, SGI News, Yahoo via itiger) | various | SNIPPET | NB series; 2025 $9.2B from NB business update (REPO-NOTE, OPENED) |
| 25 | HGI, "Have athletic footwear industry titans lost their step?", https://hgi.io/insights/have-athletic-footwear-industry-titans-lost-their-step/ (Euromonitor Passport, Dec 18, 2025) | 2026-01-13 | OPENED (cached curl copy, re-read today) | US shares 2016, 2019, 2025; US market CAGR; global share -540 bp to 22.9%; $168B global market |
| 26 | Euromonitor sportswear press release (2% CAGR 2025 to 2030) | 2025 or 2026 | SNIPPET (page unreachable, 502) | Global forecast |
| 27 | Circana US footwear 2024 and 2025 (SGB, Mr-Mag) | 2025-01-31; 2026-02-05 | REPO-NOTE (OPENED there) | US market flat |
| 28 | Repo notes: `macro_covid_cycle.md`, `emea_converse_jordan.md`, `china.md`, `challengers_taste.md`, `valuation_vs_business.md`, `competitors_and_turnarounds.md` | 2026-10-13 | REPO-NOTE | Vans, Converse cycle, NBS China, stock decomposition, On Q2 2026 |
| 29 | Daily close prices for NKE and peers (scratchpad `all.json`, Yahoo Finance) | to 2026-10-12 | OPENED (data file) | Peer stock moves Nov 5, 2021 to Oct 12, 2026 |

## 8. Gaps and caveats

- ASICS 2019 and 2020, Anta 2019 and 2020, Li Ning and New Balance figures are SNIPPET or unaudited. ASICS 2019 is unverified. Results for 2023 to 2025 do not depend on the 2019 values.
- Skechers 2025 is an estimate (H1 growth applied); it went private in September 2025.
- VF XBRL values are as filed in each year and do not restate later divestitures.
- Puma 2025 is restated for the PUMA United licensing change; I chain the reported 2025 growth onto the original 2024 base.
- adidas Latin America c-n includes Argentine hyperinflation effects, which inflate the APLA benchmark. I therefore used a wide APLA band.
- No European or global market-size series by year was opened. The EMEA benchmark band rests on peers and is the least certain row.
- Fiscal-year misalignment of up to 5 months. Quarterly tests use the nearest calendar quarter.
- The peer pool is not the market. Winners' growth partly *is* Nike's loss, so pool-based counterfactuals overstate what Nike "should" have done. I lean on the incumbent cohort and market data.
- A SEC EDGAR request early in this session carried a contact header; later requests used a generic research user agent.

---

## Challenge: REFUTER

Date: 2026-10-13. Scope kept deliberately narrow: the core finding is robust enough that a full re-research is not warranted, so I tested the four claims most likely to break (FX, the China market benchmark, the "no peer DTC fell double digits" signature, and the adidas comparison base). Two factual errors found, neither overturns the verdict.

### What I checked and found

1. **FX tailwind: confirmed.** Nike's translation impact on revenue was -$419M in FY2025 (FY25 10-K p. 45) and +$1,023M in FY2026 (FY26 10-K p. 44), net about +$604M (REPO, `data/nike_filing_facts.csv`; my arithmetic). The investigator's +$0.56B is consistent.

2. **China market benchmark is the wrong NBS line (error).** The +11.1% (2024) and +15.7% (2025) used as "the market" are the NBS *体育、娱乐用品类* (sports and entertainment goods) category. That line is equipment-heavy; MOFCOM attributes 2025 growth to ski, hiking and cycling gear. It is also small: RMB 170.3B in 2025. Sports footwear and apparel sit inside *服装、鞋帽、针纺织品类* (apparel, footwear, headwear, textiles): RMB 1,469.1B, +0.3% in 2024; RMB 1,521.5B, +3.2% in 2025. That is about +3.5% over two years.
   - Sources: NBS, December 2024 retail sales release, 2025-01-17, https://www.stats.gov.cn/sj/zxfb/202501/t20250117_1958327.html (OPENED). NBS, December 2025 release, 2026-01-19, https://www.stats.gov.cn/xxgk/sjfb/zxfb2020/202601/t20260119_1962323.html (OPENED). MOFCOM commentary via search (SNIPPET).
   - Consequence: the low end of the China benchmark should be about +3.5%, not +5%. The China gap becomes about -27 to -38 pts, roughly **$2.0B to $2.9B** instead of $2.1B to $2.9B. The China verdict stands, because adidas (+20%) and Anta (+29%) grew in the same market. But the "growing market" framing in P3 overstates how fast the relevant market grew. China was a flat-to-low-growth apparel market in which local and some foreign brands took share.

3. **"No peer's DTC fell double digits" is false (error).** Under Armour's FY2025 (April 2024 to March 2025, which maps to the same window) shows direct-to-consumer revenue -11% and eCommerce -23%, "due to planned reductions in promotional activities". In Q4 alone DTC was -15% and eCommerce -27%. Source: UA FY2025 Q4 8-K Ex. 99.1, filed 2025-05-15, https://www.sec.gov/Archives/edgar/data/1336917/000133691725000058/exhibit991-fiscal2025q4.htm (OPENED).
   - This is the same mechanism Nike reported: a deliberate pull-back of promotional digital sales. So the Direct collapse is not a uniquely Nike signature. It is an incumbent reset playbook, also run by UA and, through store cuts, by Puma.
   - It does not make the cause industry-wide. Both are firm-level choices by brands that had over-discounted their own channels. But the channel test (P5) should be downgraded from "strongest signature" to "shared with incumbents in reset". Part of Nike's Direct decline is the *chosen* cost of the fix, not the original defect.

4. **adidas is a rebound-base comparison.** adidas 2023 was flat c-n, +2% ex-Yeezy, with North America -16% (adidas FY2023 release via World Footwear and EQS ad hoc, 2024-03; SNIPPET). Over 2019 to 2025, adidas ex-Reebok grew +13.3%, against Nike's +18.6% to +24% (investigator's own panel).
   - So the 2023 to 2025 adidas surge (Europe +28%, footwear +25%) is partly adidas recovering its own 2022 to 2023 trough, and partly a zero-sum swing of the lifestyle trend from Nike classics (Dunk, AF1, AJ1) to adidas terrace models (Samba, Gazelle).
   - Using adidas as the benchmark for the footwear gap (-38 pts) and the EMEA gap therefore double-counts. Nike's loss *is* adidas's gain, the same peer-selection bias the investigator flagged for challengers. The investigator excluded adidas from the EMEA benchmark band, but not from the footwear gap or the bottom line.
   - The fashion rotation is exogenous in timing, but failing to own the next silhouette is a Nike product failure. On balance it stays Nike-specific. The size of the footwear gap should be read against the market (Euromonitor US footwear about +4% a year), not against adidas: about -15 to -20 pts, not -38.

5. **Market tailwind upper bound is generous.** The +6% two-year market (+$3.1B) uses the high end. Circana has US footwear flat in 2024 and 2025 (REPO-NOTE), China apparel and footwear grew about +3.5% (above), and Euromonitor forecasts about 2% global CAGR. A 0% to +4% band (+$0 to +$2.1B) is more defensible.

### Re-estimate (my arithmetic)

Residual = net change minus (market + FX + cohort shock):
- Low end: -4,964 - (0 + 604 - 900) = **-$4.67B**.
- High end: -4,964 - (2,100 + 604 - 700) = **-$6.97B**.
- That is about **94% to 140% of the net decline**, against the investigator's 95% to 155%.

My range is somewhat lower and tighter than the investigator's. Even on the least favourable reading, the Nike-specific residual is at least about 90% of the decline.

### Where the hypothesis bends but does not break

- The channel signature is weaker than claimed. UA shows a self-inflicted DTC and eCommerce decline of similar size. Nike's Direct drop is partly the cost of the cure.
- The China gap holds against peers. The "growing market" framing does not hold for footwear and apparel.
- The adidas-based gaps overstate how much was Nike-specific, because they include a share swap and adidas's own rebound.
- I found no peer, region or period that contradicts the core prediction: Nike fell while the relevant market was flat to slightly up and most peers grew. P1 (timing), P2 (breadth) and P8 (North America convergence after the reset) survive my checks.

### Verdict

**Survives as primary cause**, with two factual corrections: the China market proxy, and UA's double-digit DTC decline. The share should be reworded to "about 90% or more of the net decline, central estimate around 100% to 110%". The 155% upper bound, the -38 pt footwear gap and "strongest signature" for channel should be dropped.

Sources (this section):
- NBS December 2024 retail sales release, 2025-01-17, https://www.stats.gov.cn/sj/zxfb/202501/t20250117_1958327.html, OPENED.
- NBS December 2025 retail sales release, 2026-01-19, https://www.stats.gov.cn/xxgk/sjfb/zxfb2020/202601/t20260119_1962323.html, OPENED.
- MOFCOM commentary on 2025 sports goods (via search summary), 2026-01, SNIPPET.
- Under Armour FY2025 Q4 8-K Ex. 99.1, 2025-05-15, https://www.sec.gov/Archives/edgar/data/1336917/000133691725000058/exhibit991-fiscal2025q4.htm, OPENED.
- adidas FY2023 results (World Footwear, https://www.worldfootwear.com/news/adidas-posts-betterthanexpected-operating-profit-in-2023/9641.html; EQS ad hoc), 2024-01/03, SNIPPET.
- Nike FX translation impacts FY2025 and FY2026, `data/nike_filing_facts.csv` (10-K p. 45, p. 44), REPO.
