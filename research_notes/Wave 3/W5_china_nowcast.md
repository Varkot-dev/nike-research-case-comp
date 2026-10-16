# W5: Nike Greater China real-time nowcast (Q2 FY27, Sep to Nov 2026)

Written 2026-10-16. Tags: OPENED (we read the filing or page itself), SNIPPET (search summary only), DERIVED (our arithmetic). Data and scripts: `data/wave3_w5/` (README there; `routes_log.csv` lists every route and result). Builds on, and does not redo: `research_notes/Long or short cruxes/china_doors.md` (doors), `china_floor.md` (Pou Sheng quarters, Topsports bands, Denton quotes), `research_notes/Niche sources/N5_china_ecommerce_rankings.md` (festival ranks). Where this note overlaps `china_floor.md` (Pou Sheng implied Nike sell-through), it extends it with a back-test and a Nike dollar nowcast.

## 1. Verdict

**Nowcast, Nike Greater China revenue Q2 FY27: central $1,098m (-22.8% reported, -26.9% currency-neutral); range $975m to $1,146m (-31.5% to -19.4% reported, -35% to -24% cc), against $1,423m in Q2 FY26.** Arithmetic in section 6. No smoking gun. Nothing public yet covers Sep to Nov for Nike's two big partners except one month of Pou Sheng.

Why this range and not a narrower or higher one:

1. **Partner data alone point to a smaller decline than Q1** (scenarios A and B in section 6: -13% and -21% cc). Pou Sheng's September revenue fell only 2.5% (HKEX 2026101200300, OPENED), against -10.4% for Jun to Aug.
2. **Two items the partner data cannot see push the other way**, and they are why the central case is below -26%: (a) Nike told both partners on 2026-07-21 that their mainland online sales of Nike end 2027-01-01 (Topsports 2026072200069, Pou Sheng 2026072200197, OPENED), and that business is about a third of Nike's wholesale to them (section 5); (b) the CFO said on the Q1 call that the guide "assumes that China actually gets worse from a revenue perspective for the balance of this year" (Q1 FY27 transcript, OPENED, management guidance, used here as a constraint and labelled as opinion, not as the explanation).
3. **The Pou Sheng September print is flattered by the calendar.** Mid-Autumn was 2026-09-25 against 2025-10-06 (china_floor.md). Sep plus Oct together are the clean comparison, and October is not out (due about Nov 10).
4. **Back-test noise is large** (section 4): the gap between Nike wholesale and partner-implied sell-through has a standard deviation of 7.4 points over eight quarters. A range of about 12 points around the central case is therefore honest, not cautious.

**What would settle it:** Topsports Jun to Aug operating update (about Oct 21 to 22, not out, HKEX search to 2026-10-16) and interim results Oct 28 (board notice 2026101200757, OPENED); Pou Sheng October revenue (about Nov 10); NBS September retail sales (about Oct 19 to 22); Anta, Li Ning and Xtep Q3 updates (Oct 17 to 27 in 2025); Nike Q2 FY27 results (about Dec 18).

## 2. The panel (Nike fiscal quarters, `panel_nike_fiscal_quarters.csv`)

All growth rates are YoY. Nike fiscal quarters line up exactly with Topsports fiscal quarters (Nike Q1 = Jun to Aug = Topsports Q2) and with Pou Sheng months.

| Nike quarter | Nike GC cc | Nike GC reported | Nike wholesale cc (est) | Nike direct cc (est) | Pou Sheng total | PS-implied Nike sell-through | Topsports total sales | TS-implied Nike | Domestic brands (aligned) | NBS sports | NBS clothing | HK footwear (value) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 FY26 (Jun-Aug 25) | -10 | -9.2 | -8.8 | -11.7 | -10.5 | -26.8 | high-single decline (-8) | -19.2 | +0.8 | +12.9 | +2.2 | -4.5 |
| Q2 FY26 (Sep-Nov 25) | -16 | -16.8 | -14.3 | -17.9 | -3.3 | -14.1 | high-single decline (-8) | -20.4 | -1.1 | +7.0 | +4.8 | -4.2 |
| Q3 FY26 (Dec-Feb) | -10 | -6.8 | -13.9 | -4.7 | -2.5 | -14.1 | low-single decline (-2.5) | -12.4 | +2.9 | +5.8 | +6.6 | +2.3 |
| Q4 FY26 (Mar-May 26) | -17 | -12.1 | -19.6 | -13.7 | -3.0 | -14.6 | low-teens decline (-12) | -28.5 | +0.6 | -6.1 | +4.9 | -2.0 |
| **Q1 FY27 (Jun-Aug 26)** | **-26** | **-22.0** | **-31.9** | **-17.5** | **-10.4** | **-28.6** | not out (see below) | n/a | n/a (361 core +5.5) | -5.6 | +1.1 | -0.4 |
| Q2 FY27 (Sep-Nov 26) | nowcast | nowcast | nowcast | nowcast | Sep only: -2.5 | | not out | | | | | |

Sources and tags:
- Nike cc: earnings call transcripts in `data/hunt/earnings_calls/transcripts/` (OPENED); reported and channel dollars: `data/nike_channel_split.csv` (10-Q and 10-K, OPENED). Wholesale and direct cc are estimated by adding each quarter's total FX gap (cc minus reported) to the reported channel change (DERIVED; Nike gives no cc by channel in the 10-Q text we could read).
- Pou Sheng: 58 HKEX monthly revenue announcements (`pousheng_monthly_revenue.csv`; Sep 2026 is HKEX 2026101200300, Aug 2026091000378, Jul 2026081000336), summed to Nike quarters (`pousheng_nike_fiscal_quarters.csv`, DERIVED).
- Topsports: HKEX quarterly updates (`topsports_quarterly_updates_source.csv`, OPENED). Bands are mapped to points: low-single -2.5, high-single -8, low-teens -12. Topsports does not give numbers.
- Domestic: Anta brand, Li Ning platform, Xtep core retail sell-through bands from `data/hunt/peers_reported/china_peers_sellthrough_quarterly.csv` (OPENED earlier), averaged and time-weighted 1/3 and 2/3 onto Nike quarters; 361 from its HKEX business updates (OPENED).
- NBS: stats.gov.cn English monthly releases (`nbs_monthly.csv`, OPENED), quarters rebuilt from levels. Scope: category rows cover enterprises above designated size.
- HK: C&SD tables 620-67002 and 620-67003 (`hk_retail_monthly.csv`, OPENED).

### 2.1 Pou Sheng monthly (RMB thousand; YoY as reported, OPENED)

| Month | Revenue | YoY |
|---|---|---|
| Apr 2026 | 1,375,870 | +0.1% |
| May 2026 | 1,457,256 | -2.7% |
| Jun 2026 | 1,080,007 | -8.6% |
| Jul 2026 | 993,878 | -13.9% |
| Aug 2026 | 1,129,431 | -9.0% |
| Sep 2026 | 1,314,827 | -2.5% |
| Nine months | 12,402,721 | -3.9% |

Jul to Sep 2026 combined: 3,438,136 against 3,743,362, -8.2% (DERIVED). Pou Sheng's own interim report (HKEX 2026081200368, OPENED) says direct retail did better than sub-distributors, online "remained resilient", doors fell 3,310 to 3,110, inventory RMB 4,668m at Jun 2026 against 4,865m a year earlier (-4.0%), and average inventory days 148 against 146.

### 2.2 Yue Yuen / Pou Chen split (manufacturing versus retail)

Taiwan MOPS and TWSE openapi block scripted access, and pouchen.com publishes only the consolidated NT$ total (Sep 2026 NT$21.40bn). The same split is public through Yue Yuen's HKEX monthly announcements (`yueyuen_monthly.csv`, OPENED, Sep 2026 doc 2026101200384):

| Month | Manufacturing YoY (USD) | Pou Sheng YoY (RMB) | Yue Yuen total YoY |
|---|---|---|---|
| Jul 2026 | -10.0% | -13.9% | -9.7% |
| Aug 2026 | -1.6% | -9.0% | -2.1% |
| Sep 2026 | +6.6% | -2.5% | +5.6% |
| Jan to Sep | -3.8% | -3.9% | -2.1% |

Manufacturing is global footwear orders, mostly not China sell-through. It moved from -10% to +6.6% in three months, which says Nike and other brands' global orders to this supplier are no longer falling, not that Chinese consumers are buying more. It is no evidence for Greater China.

### 2.3 Topsports (6110.HK)

- Mar to May 2026 (Q1 FY27): total retail plus wholesale sales "low-teens decline" (HKEX 2026062500529, OPENED), gross selling area -11.2% YoY.
- **Jun to Aug 2026 (Q2 FY27): not published as of 2026-10-16.** Management told analysts after the Q1 update that sales since June were weaker than the Q1 low-teens decline, helped by a Dragon Boat holiday shift (CICC note, zhitong 2026-06-26, SNIPPET of management commentary; Gelonghui/Tianfeng 2026-06-30 repeats the Q1 band). That sets the working expectation for the upcoming update at low-teens or worse, which maps to a TS-implied Nike sell-through of -28% or lower (section 3), consistent with Nike's own -26% for the same months.
- FY26 (Mar 2025 to Feb 2026, annual report HKEX 2026062400677, OPENED): revenue RMB 25,739.9m (-4.7%), retail -2.7%, wholesale -16.6%, principal brands (Nike plus adidas) 86.7%; largest supplier 62.7% of purchases; inventory RMB 5,485.9m (-8.6% YoY). Nike online sales were about 22% of group revenue.
- Interim results for the half to Aug 31 2026: board meeting 2026-10-28 (HKEX 2026101200757, OPENED).

### 2.4 Domestic brands (quarterly operating updates, OPENED)

| Calendar quarter | Anta brand | Li Ning platform | Xtep core | 361 core | Source |
|---|---|---|---|---|---|
| Q1 2026 | high-single (+8) | mid-single (+5) | low-single (+2.5) | about +10 | HKEX 2026041300450, 2026042200179, 2026042100089, 2026041500013 |
| Q2 2026 | low-single (+2.5) | low-single decline (-2.5) | mid-single decline (-5) | mid-to-high single (+6.5) | HKEX 2026071700328, 2026071500286, 2026071700195, 2026071500037 |
| Q3 2026 (Jul-Sep) | not out | not out | not out | mid-single (+5); kids +5; e-commerce mid-to-high single | 361: HKEX 2026101400065 (14 Oct) |

Anta, Li Ning and Xtep Q3 2026 updates were not published by 2026-10-16 (HKEX search; routes in `routes_log.csv`). The domestic composite for Nike Q2 FY27 therefore cannot be built yet; the working assumption is a composite of about -2% to +2% (Q2 2026 composite -1.7%, 361 +5%).

### 2.5 NBS (OPENED, stats.gov.cn, release of 2026-09-16)

| | Jun 26 | Jul 26 | Aug 26 | Jun-Aug 26 (rebuilt) | Jan-Aug 26 |
|---|---|---|---|---|---|
| Sports and recreational articles YoY | -2.2% | -10.6% | -4.8% | -5.6% | -3.7% |
| Clothes, shoes, hats and textiles YoY | +3.9% | -1.0% | -0.5% | +1.1% | +5.1% |

Total retail sales of consumer goods +0.4% in Aug. The September release was not out on 2026-10-16. Context: sports articles grew +12.9% in Jun to Aug 2025 (trade-in and event tailwinds, base effect), so the 2-year stack for Jun to Aug 2026 is about +6.7%. The category is a weak control for Nike (it includes equipment and recreation goods), so it is used only as a second market benchmark.

### 2.6 Hong Kong and Macau (OPENED for HK, SNIPPET for Macau)

C&SD retail sales value, footwear, allied products and other clothing accessories: Jun to Aug 2026 -0.4% YoY (Jun to Aug 2025 -4.5%); wearing apparel -0.5%. Total retail Aug 2026: see `hk_retail_monthly.csv`. Nike does not disclose HK sales; HK is inside Greater China but is a small part of it, so it moves the nowcast by well under one point. Macau: adults' clothing -2.7% in Q2 2026 (Trading Economics via search, SNIPPET; DSEC page not opened). Neither is a driver.

## 3. The Nike-specific component

Method (DERIVED): partner sales growth g_P = s x g_Nike + a x g_adidas + o x g_other. Solve for g_Nike. Pou Sheng assumptions: Nike share s = 0.52 (largest supplier is 55% of purchases, annual report 2025, HKEX 2026042100610), adidas a = 0.25, other brands 0.23 growing +3%. adidas Greater China cc growth is from its releases (Q2 2025 +13%, Q3 +10%, Q4 +15%, Q1 2026 +17%, Q2 2026 +15%, ex-Yeezy; `data/hunt/peers_reported/`).

**Q1 FY27 (Jun to Aug 2026):** (-10.4 - 0.25 x 15.0 - 0.23 x 3) / 0.52 = **-28.6%** implied Nike sell-through at Pou Sheng. Sensitivity to the share assumptions (s 0.45 to 0.58, a 0.20 to 0.30): -24.3% to -34.9%. The same method gave Nike a measurement that brackets the reported -26% cc total and -31.9% estimated wholesale cc.

**Nike-specific component** (Nike sell-through minus market), Q1 FY27: -28.6 minus NBS sports -5.6 = **-23.0 points**; minus the Q2 2026 domestic composite (-1.7) = **-26.9 points**; minus adidas (+15.0) = **-43.6 points**. Q4 FY26: PS-implied -14.6 and TS-implied -28.5 against domestic +0.6, i.e. -15 to -29 points. In this arithmetic the market (NBS sports, domestic brands, HK) explains under a fifth of Nike's decline at the partners; the rest is Nike-specific.

**What the filings cannot separate** (stated, not guessed): within the Nike-specific component, lower unit sell-through, deeper discounts per unit, and partners' deliberate run-down of Nike stock are not separable, because Pou Sheng and Topsports do not report Nike units, ASP or Nike inventory. Only total partner inventory is public (PS -4.0% YoY, TS -8.6% YoY), which says partners are not carrying more stock in aggregate. What would separate them: Topsports interim notes (Nike purchases and brand revenue), and Nike's Q2 call (units versus ASP for Greater China).

**Alternatives ruled out as the cause of the Nike partner gap:**
- *Market-wide weakness:* NBS sports -5.6% and domestic composite -1.7% are 20 to 27 points above Nike's implied -28.6%. Ruled out as the main driver.
- *Door closures alone:* Pou Sheng doors fell 8.7% in a year (3,408 to 3,110, Jun 2025 to Jun 2026) and Topsports selling area fell 11.2%, but the Nike gap is far larger, and closures hit adidas too, which grew +15% (china_doors.md). Ruled out as the main driver.
- *Pou Sheng's other brands dragging the total:* varying other-brand growth from -5% to +10% moves the Q1 FY27 implied Nike figure by 3 points. Ruled out.
- *Inventory build at partners absorbing the weakness:* partner inventories are flat to down. Ruled out for the recent quarters (but see back-test: in Q1 FY26 Nike's wholesale ran 18 points ahead of the implied sell-through, which is the one quarter consistent with partner stock building before the Q2 FY26 to Q1 FY27 slide).

## 4. Back-test (`backtest_pousheng_implied_vs_nike.csv`)

| Nike quarter | Nike GC cc | Nike wholesale cc (est) | PS-implied Nike | Gap (wholesale minus implied) |
|---|---|---|---|---|
| Q2 FY25 | -11 | -14.8 | -21.6 | +6.7 |
| Q3 FY25 | -15 | -18.1 | -16.0 | -2.1 |
| Q4 FY25 | -20 | -23.7 | -24.9 | +1.3 |
| Q1 FY26 | -10 | -8.8 | -26.8 | +18.0 |
| Q2 FY26 | -16 | -14.3 | -14.1 | -0.3 |
| Q3 FY26 | -10 | -13.9 | -14.1 | +0.1 |
| Q4 FY26 | -17 | -19.6 | -14.6 | -5.0 |
| Q1 FY27 | -26 | -31.9 | -28.6 | -3.3 |

Mean gap +1.9, standard deviation 7.4 (all eight quarters); last four quarters mean -2.1, standard deviation 3.7. The gap on the total (cc minus implied) averages +4.5. Reading: the partner-implied series gets the direction right in every quarter and the level to within about 5 points in six of eight quarters, with Q1 FY26 (+18) and Q2 FY25 (+7) the misses, both quarters where Nike sold in ahead of partner sell-through.

## 5. The online cut in dollars (DERIVED)

- Topsports: Nike online 22% of FY26 revenue = 0.22 x RMB 25,739.9m = RMB 5,663m at retail revenue. At the group cost ratio (62.0%, gross margin 38.0%) the Nike product cost behind it is about RMB 3,511m.
- Pou Sheng: 15% of FY25 revenue = 0.15 x RMB 17,132m = RMB 2,570m; at a cost ratio of 66.5% (FY25 cost of sales 11,396m on 17,132m) about RMB 1,709m.
- Together about RMB 5,220m, about **$0.73bn a year at 7.15 RMB/USD**, which is about 22% of Nike's FY26 Greater China wholesale ($3,255m) and about 12.5% of FY26 Greater China revenue ($5,847m). Assumptions: online carries the group cost ratio (online discounts are deeper, so the true Nike wholesale may be lower) and none of it is recaptured through Nike's own flagship stores (Nike says it will rebuild the channel through official Tmall, JD and Douyin flagships and nike.com, so some will return as Direct revenue).
- Coverage check: Nike purchases by the two partners are about RMB 9,679m (Topsports: 62.7% x purchases of 15,437m = COGS 15,955m plus inventory change -518m) plus about RMB 6,268m (Pou Sheng: 55% x cost of sales 11,396m) = RMB 15,947m, about $2.23bn, which is about 69% of Nike's FY26 Greater China wholesale. So the two partners are roughly two thirds to 70% of the wholesale line, and the online share of that purchasing is about a third ($0.73bn / $2.23bn).
- Timing: a full-year loss of $0.73bn is about $183m a quarter; Jan to May 2027 (Q3 and Q4 FY27) carry about $0.30bn of it before recapture. In Q2 the cut is partial. The scenarios use -5 points of wholesale (about 20% of one quarter's online-bound sell-in) as the central assumption: 5 points x $767m = $38m, which is 21% of a quarter's $183m of online-bound wholesale; -10 points is 42%. These are assumptions with no data behind them. They are the single largest unobserved input and are why the range is wide.

## 6. Nowcast arithmetic (`nowcast_scenarios_q2fy27.csv`)

Base quarter, Q2 FY26 (10-Q, OPENED): total $1,423m = wholesale $767m + direct $656m. Weights 53.9% and 46.1%.

Formula: wholesale cc = (PS total - 0.25 x adidas 15 - 0.23 x 3) / 0.52 + gap + online cut. Total cc = 0.539 x wholesale cc + 0.461 x direct cc. Reported USD = $1,423m x (1 + total cc) x 1.055. The 1.055 FX factor: in Q1 FY27 reported -22.0% against cc -26% gives (1-0.220)/(1-0.26) = 1.054; the RMB moved 6.1% against USD year on year (7.176 to 6.763 monthly means, Frankfurter ECB data) so Nike realised about 89% of the spot move; Sep to Nov 2026 spot is about +6.2% (7.117 to about 6.70), so 1.055 (DERIVED).

| Scenario | PS Sep-Nov YoY | Implied Nike sell-through | Gap | Online cut | Wholesale cc | Direct cc | GC cc | GC USD m | Reported YoY |
|---|---|---|---|---|---|---|---|---|---|
| A bull, partner data only | -4 | -16.2 | 0 | 0 | -16.2 | -9 | -12.9 | 1,308 | -8.1% |
| B base, partner data only | -8 | -23.9 | -2.1 | 0 | -26.0 | -15 | -20.9 | 1,187 | -16.6% |
| C base plus online cut | -8 | -23.9 | -2.1 | -5 | -31.0 | -15 | -23.6 | 1,146 | -19.4% |
| **E central** | -8 | -23.9 | -2.1 | -5 | -31.0 | -22 | **-26.9** | **1,098** | **-22.8%** |
| D bear | -12 | -31.6 | -4.6 | -10 | -46.2 | -22 | -35.1 | 975 | -31.5% |

Choices behind the columns:
- PS Sep to Nov: bull -4 (the September print persists); base -8 (midpoint of Sep -2.5 and Jul/Aug about -11.5, treating Sep as partly calendar); bear -12 (the Jul/Aug run-rate returns after Mid-Autumn reverses in October).
- Gap: last four quarters' mean -2.1; bear uses mean minus one standard deviation (-4.6).
- Direct cc: Q1 FY27 was -17.5 (reported -13.4%). The last five quarters ran -11.7, -17.9, -4.7, -13.7, -17.5, mean -13.1. Q2 FY26 is an easy comp (direct -18.7% reported). Bull -9, base -15; central and bear -22, which adds 4.5 points to Q1's rate for the digital cleanup the Q1 call said would "dampen" China (ASSUMPTION; Nike gave no direct-channel guide).
- **Central E** is C with direct at -22. It is the lowest-risk reading of "partner data plus the two things the partners cannot show". The bull and base-without-cut cases (A, B) are shown because they are what the partner series says by itself; they are excluded from the range because they contradict the CFO's statement that China gets worse, and because the online termination is a fact, not a forecast.
- Sensitivity: each 1 point of cc is $15.0m of reported revenue (1,423 x 0.01 x 1.055). At the Q1 FY27 segment EBIT margin of about 21% ($250m on $1,180m, EBIT figure from the S&P preview snippet, SNIPPET) a $100m revenue shortfall is about $21m of EBIT on an average, not incremental, basis; this is arithmetic, not a forecast.

## 7. Comparison with consensus

- **No Q2 FY27 Greater China consensus is freely available.** Seven routes tried (`routes_log.csv`): three searches, S&P (403), roic.ai (403), fxstreet (403), Zacks previews (found, but they are Q4 FY25 and older: $1.48bn / -20.4% matches Q4 FY25's actual $1,476m).
- **Last known pre-print consensus, for Q1 FY27 (SNIPPET, S&P Global preview of 2026-09-23 via search summary):** Greater China revenue -12.6% to about $1.3bn, EBIT about $310m. Actual: $1,180m (-22.0% reported, -26% cc) and EBIT about $250m. The miss was 9.4 points of reported growth or about $120m.
- Total company: consensus FY27 revenue of about $45.1bn (SNIPPET, Oct 2026 summary), against management's guide of a high-single-digit decline from $46.4bn (about $42.7bn at -8%), so the published consensus summary looks stale or pre-guide; do not rely on it.
- Implication: unless analysts have since moved Q2 Greater China to below $1.15bn, they are above the top of our range; the Q1 miss and the July online notice make a cut likely, but we could not see it.

## 8. Is there a smoking gun? No.

Rule stated in advance: a smoking gun would be a partner or official print for Sep to Nov that is incompatible with the -24% to -35% cc range (a Topsports Jun to Aug band better than high-single digit, or Pou Sheng Sep plus Oct combined better than -4%), or a partner statement quantifying the Nike shipment cut. None exists. The evidence is concordant but indirect:

- Pou Sheng's quarter-by-quarter implied Nike sell-through matched Nike's reported cc direction in all eight back-test quarters.
- Pou Sheng Sep -2.5% leans the other way and is the only data point that does; it is one month with a holiday shift.
- Topsports (the larger partner, and the one with Nike online at 22% of revenue) is the most important missing print.

## 9. What we could not get (routes in `routes_log.csv`)

- Topsports Jun to Aug 2026 update and interim results: not published (about Oct 21 to 22 and Oct 28).
- Anta, Li Ning, Xtep Q3 2026 updates: not published (361 is).
- NBS September 2026 retail sales: not published.
- Nike-only partner data: no partner discloses Nike sales, units, ASP or Nike inventory; the Nike share inputs (0.52, and 0.58 at Topsports) are assumptions anchored on largest-supplier shares of purchases.
- Taiwan MOPS (blocked); replaced by Yue Yuen's HKEX monthly split.
- Q2 FY27 Greater China consensus: not found free.
- Macau: official DSEC page not opened.

## 10. Updates to make when new prints arrive

1. Topsports Jun to Aug band: if low-teens or worse, TS-implied Nike is -28% or lower and the Q1 FY27 calibration holds; if mid-single or better, move toward scenarios B and C.
2. Pou Sheng October (about Nov 10): if Sep plus Oct combined is above -5%, shift the base PS input from -8 toward -4.
3. Topsports interim (Oct 28): replace the 0.58 Nike share with the disclosed figure if any, and read Nike online share and inventory.
