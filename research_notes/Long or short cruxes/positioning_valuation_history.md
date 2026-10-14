# Positioning and valuation history: do setups like Nike's Oct 2026 tend to bottom or keep falling?

Prepared 2026-10-14. Working folder: `scratchpad/hist/` (session scratchpad). Raw price files: Yahoo Finance v8 chart API, daily, dividend-adjusted (`adjclose`), fetched 2026-10-14 (OPENED).

Labels: **OPENED** (read on a fetched page or file), **SNIPPET** (search-result text only), **REPO** (from this repo, with path), **ARITH** (my arithmetic on the above).

## 0. Decision rule, written before gathering data

The setup today (Oct 12 to 14, 2026): stock $35.35, about 80% below the 2021 peak; about 27x FY27 consensus EPS; FY27 guide is a decline; dividend $1.64 run-rate against $1.15 to $1.35 adjusted EPS (payout 121% to 143%); short interest 99.2M shares, 6.7% of shares outstanding, a series high (REPO `data/flows/short_interest_finra_2023_2026.csv`).

**Points LONG if:**
- L1. In Nike's own past troughs, the first guide cut that came with a CEO or strategy reset (not the first warning) was followed by positive 12-month excess returns in most cases (at least 3 of 4).
- L2. Across comparable brand resets, setups with a new CEO, a stock at least 60% below peak, and record short interest had median 12-month excess return above +10%.
- L3. A high forward P/E on trough earnings did not predict further falls (that is, prior troughs also looked expensive on depressed EPS and still bottomed).

**Points SHORT if:**
- S1. Comparable setups at the 2nd or 3rd year of a decline, with a guide cut into a further sales decline, more often kept falling over 6 to 12 months (median 12-month excess return below -10%).
- S2. Dividend payout above 100% was followed by a cut, and cuts came with further falls.
- S3. Nike's past bottoms happened at materially lower multiples than 27x forward (for example at or below the market multiple), so the current multiple has room to compress.

**Inconclusive if:** the analog results split roughly evenly, or depend on which date is called the setup.

## 1. Sources

| # | Source | Date | Status |
|---|---|---|---|
| S1 | Yahoo Finance v8 chart API, daily close and dividend-adjusted close, 2000 to 2026-10-13: NKE, UAA, VFC, LULU, SBUX, ADS.DE, PVH, CROX, DECK, GAP, KSS, M, URBN, ANF, AEO, CPRI, TPR, RL, COLM, WWW, FOSL, GIL, LEVI, PUM.DE, CRI, ZUMZ, GIII, OXM, BBWI, VRA, BOOT, SHOO, ^GSPC, ^GDAXI | fetched 2026-10-14 | OPENED (raw JSON) |
| S2 | FINRA consolidated short interest API (api.finra.org, `consolidatedShortInterest`), settlement dates 2017-12-29 to 2026-09-30: NKE, VFC, LULU, SBUX, UAA, UA, ADDYY | fetched 2026-10-14 | OPENED (raw JSON) |
| S3 | Yahoo fundamentals-timeseries: annual revenue, total debt (includes leases), cash, diluted shares, diluted EPS, last 4 fiscal years: NKE, VFC, UAA, LULU, SBUX, ADDYY | fetched 2026-10-14 | OPENED (raw JSON) |
| S4 | Yahoo chart `events=div`: dividend per share history | fetched 2026-10-14 | OPENED |
| S5 | Nike FY2009 Q4 and full year release (investors.nike.com, 2009): revenue $19.2B, diluted EPS $3.03, $3.81 excluding Umbro impairment and restructuring | 2009-06 | SNIPPET |
| S6 | Nike FY2010 Q4 and full year release (investors.nike.com, 2010-06-23): diluted EPS $3.86, up 27%; revenue $19.0B | 2010-06-23 | SNIPPET |
| S7 | Nike FY2001 10-K income statement: net income $589.7M, diluted EPS $2.16; total costs $8,567.4M plus pretax income $921.4M imply revenue $9,488.8M | 2001-08 | SNIPPET (revenue is ARITH) |
| R1 | REPO `data/trackrecord/price_reactions.csv` (Nike event dates and day-1 reactions) | 2026-10-13 | REPO |
| R2 | REPO `data/flows/short_interest_finra_2023_2026.csv`, `data/capital/dividend_history.csv`, `data/valuation/nke_multiples_history.csv` | 2026-10-13 | REPO |
| R3 | REPO `research_notes/Long or short cruxes/expectations_gap.md` section 2.7 (investor day reactions, options-implied move) | 2026-10-14 | REPO |

Method (ARITH): event day = first trading day the market could react (Nike prints after the close, so the next session). Forward returns use dividend-adjusted closes from the event-day close, at +6 months (183 days) and +12 months (365 days). Excess = stock minus S&P 500 (DAX for adidas and Puma). "dd5y" = event-day close versus the highest close in the prior 5 years. "min12" = lowest dividend-adjusted close in the next 12 months versus the event-day close. Scripts: `scratchpad/hist/tool/px.py`, `ev.py`, `base_idio.py`, `sirec.py`.

## 2. Nike's own past troughs: they bottomed fast (LONG for the old Nike)

| Setup (event day) | Event | dd5y | 6m excess | 12m excess | Worst point in next 12m |
|---|---|---|---|---|---|
| 2001-02-27 | i2 supply chain warning, guide cut (day 1 -19.8%) | -34% | +36 | +61 | -8% |
| 2001-09-17 | post 9/11 reopen | -26% | +32 | +11 | -7% |
| 2008-06-26 | FY09 outlook (day 1 -9.8%) | -15% | +16 | +15 | -34% |
| 2008-12-19 | Q2 FY09, cost cuts | -27% | +8 | +4 | -24% |
| 2009-03-20 | Q3 FY09, after Feb 2009 layoffs | -36% | -8 | +15 | 0% |
| 2017-03-22 | Q3 FY17 futures miss | -20% | -7 | +8 | -5% |
| 2017-06-16 | Consumer Direct Offense, 2% layoffs | -24% | +18 | +36 | 0% |
| 2017-09-27 | Q1 FY18, North America -3% | -22% | +21 | +46 | -3% |
| 2022-09-30 | Q1 FY23 inventory glut (day 1 -12.8%) | -53% | +34 | -4 | 0% |

Source: S1, ARITH. 12m excess positive in 8 of 9; median +15.

Valuation at those bottoms (ARITH from S5 to S7 and S1; Yahoo closes are split-adjusted, so raw price = close x 8 for 2001 and x 4 for 2009, after the 2007, 2012 and 2015 2-for-1 splits):
- Feb 2001: raw price about $39.4; FY01 EPS $2.16 gives about 18x current-year EPS; about 273M diluted shares (589.7 / 2.16) gives market cap about $10.7B on $9.49B revenue, about 1.1x sales.
- Mar 2009: raw price about $45.0; FY10 EPS $3.86 (perfect foresight) gives about 11.7x; about 491M shares (1,487 / 3.03) gives market cap about $22.1B on $19.2B revenue, about 1.15x sales.
- Jun to Sep 2017: about 21 to 22x FY18 EPS, EV/sales about 2.5x (R2).
- Sep 2022: $83.12 / FY23 EPS $3.23 = about 26x, EV/sales about 2.7x (ARITH, R2).
- Today: about 1.1x EV/sales (R2), about 27x FY27 guide midpoint.

Key point: in 2001 and 2009 Nike bottomed at about 1.1x sales, as now, but at 12 to 18x EPS, because margins were intact and EPS grew the next year (FY10 +27%, S6). Today the same sales multiple is 27x EPS because the margin is roughly half. In 2017 and 2022 the stock bottomed at 21 to 26x, so a high forward P/E alone did not prevent bottoms. S3 (prior bottoms at materially lower multiples) is only half true: true for 2001 and 2009, false for 2017 and 2022.

But these troughs differ from today on every structural measure: drawdown 15% to 53% (today 80%), one or two resets (today seven), and EPS recovered within one fiscal year.

## 3. Nike's current cycle: every bottom signal has already failed

| Setup (event day) | Signal | Day 1 | dd5y | 6m excess | 12m excess |
|---|---|---|---|---|---|
| 2023-12-22 | FY24 cut, $2B savings | -11.8% | -39% | -24 | -53 |
| 2024-06-28 | FY25 guide down MSD | -20.0% | -58% | -7 | -17 |
| 2024-09-20 | CEO change (Hill named) | +6.8% | -51% | -20 | -33 |
| 2024-10-02 | guidance withdrawn | -6.8% | -53% | -20 | -26 |
| 2024-12-20 | muted reaction to guide | -0.2% | -57% | -22 | -40 |
| 2025-03-21 | Q4 guide down mid-teens | -5.5% | -62% | -12 | -37 |
| 2025-06-27 | "worst is behind us" rally | +15.2% | -59% | -27 | -61 |
| 2025-10-01 | positive reaction | +6.4% | -58% | -37 | -65 |
| 2025-12-19 | Q2 FY26 | -10.5% | -67% | -35 | n/a |
| 2026-04-01 | multi-quarter guide | -15.5% | -75% | -35 | n/a |
| 2026-07-01 | positive reaction to cut | +4.9% | -76% | n/a | n/a |
| 2026-10-02 | FY27 initial guide, muted | -3.6% | -81% | n/a | n/a |

Source: S1, R1 (day 1 from R1), ARITH. 6m excess negative in 10 of 10 measurable cases; 12m excess negative in 8 of 8.

Record short interest has also failed here. Nike set new series highs (since Dec 2017) in Feb to Apr 2025 (33.5M to 50.4M shares); 12m excess after those prints was -21, -36, -31 and -45 (S2, ARITH). The current record (99.2M, Sep 30, 2026) is the sixth successive record of 2026. Days to cover is only 2.59 (S2), versus 8.03 at VF's May 2024 high and 15.0 at Under Armour's July 2018 high, so squeeze fuel is modest.

## 4. Comparable brand resets

| Ticker | Event day | Event | dd5y | Day 1 | 6m excess | 12m excess |
|---|---|---|---|---|---|---|
| ADS.DE | 2022-10-21 | profit warning, Rorsted exit | -69% | -9.5% | +33 | +47 |
| ADS.DE | 2023-02-10 | Yeezy write-off, loss guide | -59% | -10.9% | +25 | +14 |
| ADS.DE | 2023-03-08 | results, dividend cut 3.30 to 0.70 EUR | -56% | +2.1% | +23 | +14 |
| UAA | 2016-10-25 | first guide cut | -37% | -13.2% | -52 | -71 |
| UAA | 2017-01-31 | guide cut, CFO exit | -59% | -25.7% | -24 | -59 |
| UAA | 2017-08-01 | guide cut, restructuring | -65% | -8.6% | -37 | -9 |
| UAA | 2017-10-31 | guide cut (4th) | -76% | -23.7% | +41 | +71 |
| UAA | 2019-11-04 | SEC probe | -67% | -18.9% | -36 | -23 |
| UAA | 2022-05-06 | guide cut | -60% | -23.8% | -15 | -21 |
| UAA | 2024-03-14 | Plank returns as CEO | -74% | -10.7% | -8 | -17 |
| UAA | 2025-08-08 | guide below | -80% | -18.1% | +30 | -13 |
| LULU | 2024-03-22 | guide light | -21% | -15.8% | -44 | -27 |
| LULU | 2025-03-28 | guide light | -43% | -14.2% | -59 | -64 |
| LULU | 2025-06-06 | guide cut | -48% | -19.8% | -43 | -79 |
| LULU | 2025-09-05 | guide cut | -67% | -18.6% | -3 | -57 |
| LULU | 2026-04-23, 2026-09-04 | further resets | -72%, -80% | -13.3%, -17.4% | n/a | n/a |
| VFC | 2022-07-29 | guide cut | -55% | -8.0% | -28 | -64 |
| VFC | 2022-12-05 | CEO exit | -71% | -11.2% | -44 | -49 |
| VFC | 2023-02-09 | dividend cut 0.51 to 0.30 | -74% | -8.5% | -31 | -61 |
| VFC | 2023-05-19 | FY24 guide | -81% | -8.2% | -15 | -59 |
| VFC | 2023-10-31 | dividend cut 0.30 to 0.09, guide pulled | -85% | -14.0% | -35 | +16 |
| VFC | 2024-02-07 | guide cut | -85% | -9.7% | +12 | +43 |
| VFC | 2025-05-21 | guide | -87% | -15.8% | +9 | +9 |
| SBUX | 2024-05-01 | miss, guide cut | -41% | -15.9% | +17 | +1 |
| SBUX | 2024-07-31 | Q3 FY24 | -38% | +2.6% | +32 | +2 |
| SBUX | 2024-10-23 | guidance suspended | -23% | +0.9% | -7 | -27 |
| SBUX | 2025-04-30 | miss | -36% | -5.7% | -17 | +6 |

Sources: S1 (prices), S4 (dividend amounts), ARITH. Event labels are my description of the day's large move; the move itself is in the data.

**Pooled test (the decision rule S1 / L2):** comparable events with the stock at least 60% below its 5-year peak and 12m data available: N = 14 (ex Nike). Median 12m excess -15; 5 of 14 positive; median 6m excess -11.5. Including Nike's one qualifying measurable event: N = 15, median -17. Per company medians: adidas +47, Under Armour -15, VF -20, Lululemon -57. ARITH.

What the bottoms that did happen had in common:
- adidas Oct 2022: new CEO from outside within two weeks (Gulden named Nov 4, 2022; day 1 +21.4%, S1), then a kitchen-sink guide and a 79% dividend cut. Bottom at about 1.07x EV/sales (ARITH: 103.86 EUR x about 178.6M shares = 18.5B EUR, plus 6.46B debt less 0.80B cash, on 22.5B EUR revenue, S3).
- Under Armour Oct 2017: fourth cut in 12 months, -76% from peak, day 1 -23.7% (capitulation reaction). It held only about 12 months; the stock then made new lows from 2019 to 2026 and is -81% today.
- VF Oct 2023 to Apr 2024: second dividend cut (70%), new CEO about three months in, -85% to -88% from peak, record short interest with days to cover up to 8 (S2). About 1.25x EV/sales (ARITH from S3).
- Starbucks May to Aug 2024: bottomed at the first guide cut (-41% from peak), and the outside CEO hire (Niccol, Aug 13, 2024, day 1 +24.5%) confirmed it.
- None of them bottomed on a muted reaction alone; the bottoms came with an outside CEO, a dividend cut, or a capitulation-size drop.

## 5. Base rate: every idiosyncratic apparel and footwear collapse since 2005

Screen (ARITH, S1): close at least 75% below the 5-year high, stock 12m return at least 30 points below the index, index 12m return above -5% (idiosyncratic, not a market crash), first qualifying day then one per 12 months, 2020 excluded (Covid rebound contaminates it).

| Universe | N | Median 6m excess | Median 12m excess | 12m excess positive | 12m excess at or below -20 | Median worst point in next 12m |
|---|---|---|---|---|---|---|
| All 31 names | 36 | -2 | +5 | 20 of 36 | 12 of 36 | -20% |
| Brands only | 24 | -10 | -2 | 11 of 24 | 9 of 24 | -24% |
| Brands, 60% threshold | 60 | +5 | -12 | 26 of 60 | 25 of 60 | -28% |

Brand cases at 75%: UAA 2017-10 +71, 2023-09 -10, 2025-03 -11; VFC 2023-03 -59, 2024-03 +10, 2025-06 +28; CROX 2012-06 -21, 2016-05 -36; DECK 2012-10 +116; CPRI 2025-04 +3; WWW 2023-08 +30; FOSL nine cases from -95 to +186; PUM.DE 2025-02 -31; CRI 2025-07 +36; VRA 2015 +1, 2017 -1, 2024 -47.

Read: being 75% to 80% down is not by itself a buy signal. It is a coin flip with fat tails both ways, and the typical holder still sits through another 20% to 25% drawdown inside 12 months. Survivorship bias: Yahoo has no data for delisted names (Express, Tailored Brands, Ascena went bankrupt; Skechers, Hanesbrands, Guess, Foot Locker were acquired). Bankruptcies bias this table toward LONG; buyouts bias it toward SHORT. Nike is not a bankruptcy or buyout candidate, so the bias is roughly neutral for this use.

## 6. Dividend payout above 100%

| Company | Payout above 100% | What it did | Next 12m excess from the decision |
|---|---|---|---|
| VF | FY23 | cut 41% (Feb 2023), then 70% (Oct 2023) | -61 after first cut; +16 after second |
| adidas | 2022 to 2023 | cut 79% (paid May 2023) | +14 (from Mar 8, 2023) |
| Starbucks | FY25 (GAAP EPS $1.63 vs $2.44 paid in FY25, S3, S4) | token raise 0.61 to 0.62 (Nov 2025) | +10% total return from Nov 14, 2025 to Oct 13, 2026 vs S&P +16%, so about -5 excess, under 12 months (S1, ARITH) |
| Nike | FY27 guide: $1.64 run-rate vs $1.15 to $1.35 adjusted EPS (R2) | token raise 0.40 to 0.41 (Nov 2025, S4); next decision normally mid-Nov | open |

Read: a payout above 100% did not force a cut at Starbucks. Where a cut came (VF), the first cut did not mark the bottom; the second did. Not decisive in either direction for Nike's November decision.

## 7. Alternatives tested

1. **"Nike always bottoms within weeks of a reset, so buy" (L1).** True for 2001, 2008 to 2009, 2017 and 2022 (8 of 9 positive). Ruled out as the right reference class: the same rule has now failed 8 of 8 times in this cycle on 12m excess (section 3), and those troughs were 15% to 53% drawdowns with EPS recovering within a year.
2. **"Record short interest marks the bottom."** Ruled out as a standalone signal: VF set records from Dec 2021 to Oct 2023 while falling another 75%; Nike's 2025 records were followed by -21 to -45 excess; Lululemon is at a record now and still falling (S2, S1). Records came at true bottoms (VF May 2024, UA 2018) only alongside other capitulation markers.
3. **"Muted reaction to bad news means it is priced in."** Ruled out for Nike: muted or positive reactions in Dec 2024, Jun 2025 and Oct 2025 were followed by -40, -61 and -65 excess (section 3).
4. **"Cheap enough: about 1.1x sales, where Nike bottomed in 2001 and 2009."** Weakened: Lululemon is at about 1.0x EV/sales and about 7x trailing EPS ($94.34 x 119.1M shares = $11.2B vs $11.09B TTM revenue and $13.26 FY25 EPS, S1, S3, ARITH) and still made new lows in Sep and Oct 2026. Sales multiples only mark bottoms once margins are believed to recover.
5. **"The pooled result is just Lululemon and VF dragging the median."** Partly true: per company, adidas +47 and Starbucks positive versus UA -15, VF -20, LULU -57. 3 of 5 companies still have negative medians at the 60% drawdown stage. Not ruled out that clustering exaggerates the result; sample is small (5 companies).
6. **"Outcomes depend on which date you call the setup."** Tested: using every large-move date in the window instead of hand-picked dates (sections 4 and 5) gives the same direction at the 60% threshold (median -12 to -15) and roughly neutral at the 75% threshold (-2 to +5).

## 8. Verdict on the decisive question

History says setups at Nike's stage (third year or later of decline, repeated guide cuts, 60%+ below peak, record short interest, no dividend cut yet) more often kept falling over the next 6 to 12 months: comparable events had median 12m excess of -15 (5 of 14 positive), and Nike's own current-cycle signals are 8 of 8 negative. That meets the SHORT threshold S1 set in section 0. The old-Nike pattern (L1) is real but belongs to shallower troughs with intact margins. The deep-drawdown base rate (section 5) is close to a coin flip with a fat right tail (UA 2017 +71, VF 2024 +43, adidas +47), so the strength is moderate, not decisive.

What turned the analogs that did bottom: an outside CEO hire (adidas, Starbucks), a dividend cut that reset the capital story (VF second cut, adidas), or a capitulation-size drop on the fourth or later cut (UA Oct 2017). Nike has used its CEO change (Sep 2024, failed) and has not cut the dividend. The November dividend decision (normally declared mid-November, right after the Nov 16 to 17 Investor Day) is the nearest event that resembles a historical bottoming trigger.

## 9. What would settle it

- Nike's November 2026 dividend declaration: a cut (VF and adidas pattern) or a freeze with an explicit capital plan would be the first trigger of the kind that preceded comparable bottoms; another token raise repeats the Starbucks path, which did not end the slide.
- Q2 FY27 results (expected around Dec 17, 2026): every analog bottom that held was confirmed by the first beat against a reset bar within one to two quarters (UA Feb 13, 2018 +17.4%; adidas May 5, 2023 +8.9%, S1).
- FINRA short interest for Oct 15 and Oct 30, 2026 (published about Oct 24 and Nov 10): covering into Investor Day with the price flat would be a positioning, not a fundamental, signal.

## Skeptic review

Prepared 2026-10-14 by an independent reviewer. Scripts: `scratchpad/skep/` (`chk.py`, `wide.py`, `uncond.py`, `drop.py`, `drop2.py`), reusing `scratchpad/hist/tool/px.py`. New price files for 30 non-apparel consumer and brand names fetched from the Yahoo v8 chart API on 2026-10-14 (OPENED).

### 1. Numbers re-checked at source (all reproduce)

- NKE close $35.35 on 2026-10-12 and $35.33 on 2026-10-13; low of 2026 was $33.87 on 2026-10-02 (Yahoo v8, fetched 2026-10-14, OPENED).
- 12m excess after 2023-12-22 (-53), 2024-06-28 (-17), 2024-09-20 (-33), 2025-06-27 (-61), 2025-10-01 (-65), 2022-09-30 (-4), 2017-06-16 (+36): all match section 2 and 3 (fresh download, OPENED, ARITH).
- FINRA consolidated short interest (api.finra.org, fetched 2026-10-14, OPENED): 99,243,778 shares on 2026-09-30, days to cover 2.59, average daily volume 38.3M. Path: 57.0M (Jun 15), 72.3M (Jun 30), 57.4M (Jul 31), 75.6M (Aug 31), 85.7M (Sep 15), 99.2M (Sep 30). Short interest rose 31% in September while the price fell from $39.06 to $35.40. Against Class B float (about 1.17B to 1.2B shares; Class A is held by Swoosh LLC) that is about 8% to 8.5%, not an extreme level.
- Dividends (Yahoo events, OPENED): NKE 0.40 to 0.41 from Dec 2025; SBUX 0.61 to 0.62 from Nov 2025. Both match.

### 2. Where the verdict is weaker than stated

**(a) "8 of 8 negative" in Nike's current cycle is one observation, not eight.** The 12-month windows overlap (Dec 2023 to Oct 2026), so they all measure the same slide. This is a description of the last three years, not an independent base rate. It should carry little weight as a forecast.

**(b) The headline -15 median comes from hand-picked events at the 60% threshold, with 5 companies.** I ran a systematic version on the same 31-name universe and price files: every day with a one-day drop of 8% or more (a proxy for a guide cut) when the stock was already at least X% below its 5-year high, one event per 90 days, index trailing 12m above -5% (idiosyncratic), 2020 excluded (ARITH, `drop2.py`):

| Universe and depth | N events | Companies | Median 6m excess | Median 12m excess | 12m positive | Company-weighted median | Companies with positive median |
|---|---|---|---|---|---|---|---|
| Brands, 60% or more below peak | 89 | 18 | -8 | -17 | 35 of 89 | -10 | 8 of 18 |
| Brands, 75% or more below peak (Nike is at 80%) | 40 | 9 | -10 | -4 | 19 of 40 | +14 | 6 of 9 |
| Brands plus retailers, 60% | 138 | 26 | -1 | -2 | 68 of 138 | +13 | 15 of 26 |
| Brands plus retailers, 75% | 53 | 14 | -2 | +15 | 29 of 53 | +15 | 10 of 14 |

At the 60% stage the SHORT result holds (median -17). But Nike is not at the 60% stage; it is at 80%. At Nike's actual depth the brand result is about a coin flip on events (-4, 19 of 40) and slightly positive by company (+14, 6 of 9). The 75% bucket is dominated by small caps (Fossil 17 events, Vera Bradley, Wolverine, Carter's), so it is a noisy reference too.

**(c) The benchmark is not zero.** Sampling every month for the same 31 names (2005 to 2025, 2020 excluded), the median single-stock 12m excess versus the index is -3.6 (46% positive, N = 6,436). For months when the stock was already 60% or more below its 5-year high it is -1.2 (49% positive, N = 888) (ARITH, `uncond.py`). So "below zero" is the normal outcome for a single apparel stock against the index. A -4 median at 75% depth is no different from the unconditional rate.

**(d) Wider consumer-brand set (new data).** I added 25 large consumer and brand names outside apparel (EL, CMG, MCD, MAT, HAS, INTC, PTON, KHC, DIS, TGT, PYPL, SBUX, CROX, ANF, BUD, NWL, LVMUY, KER.PA, BURBY and others), first day each year at 60% or 75% below the 5-year high, same idiosyncratic filter (ARITH, `wide.py`):
- 60% depth: N = 63, median 12m excess -9, 26 of 63 positive, median worst point in the next 12 months -22%.
- 75% depth: N = 26, median -16, 12 of 26 positive. Altria (MO) cases are spin-off artifacts (Kraft and PMI spin-offs cut the price, not the value); removing them leaves 10 of 24 positive. Losers are mostly levered or broken models (Peloton, PayPal, Newell, Estee Lauder 2024); winners are brand turns (Burberry Sep 2024 +96, Kering 2003 and 2025 +23 and +22, Abercrombie Aug 2017 +68, Crocs 2009 to 2010 +88 and +102).
- Without the idiosyncratic filter (letting in 2003 and 2009), the 60% sample turns neutral to positive (N = 79, median -3, 24-month median +7), which shows how much of any "bottom" depends on the market tide.

This tilts slightly SHORT but is not decisive; Estee Lauder (most like Nike: iconic brand, China exposure, high P/E on trough EPS, dividend cut, new CEO) shows -72, -13 and +1 after its 60% and 75% crossings, so it fell for two years after the dividend cut and new CEO, which undercuts the "dividend cut is the bottoming trigger" idea in section 8.

### 3. Data the original missed that points LONG

- In the brand universe at 75% or more below peak, company-weighted results are positive (+14, 6 of 9). The right tail is large: VF Feb 2024 +43 and Jun 2025 +32, Wolverine Nov 2023 +164, Carter's Jul 2025 +36, Puma Jul 2025 +33, UA Oct 2017 +71.
- Short interest rose 31% in September 2026 to a record, but days to cover is only 2.59, so this is a crowded view, not a squeeze setup. It does mean the bearish view is consensus positioning, which a short pitch has to beat.

### 4. Reviewer verdict

The data I re-checked are accurate. The conclusion that history points SHORT is overstated. (1) The Nike current-cycle "8 of 8" is a single overlapping path. (2) The pooled -15 depends on the 60% threshold; at Nike's actual 80% depth the systematic event study gives about -4 by event and +14 by company, against an unconditional benchmark of about -4. (3) The wider consumer-brand set tilts mildly negative at 75% (10 of 24 positive excluding Altria artifacts) but with fat tails both ways. History at this valuation and sentiment does not resolve LONG versus SHORT: it is close to a coin flip with a typical further drawdown of 20% to 25% inside 12 months and a fat right tail. Verdict: NEUTRAL (history does not settle it). The deciding evidence has to be fundamental (Investor Day FY28 framing on Nov 16 to 17, the mid-November dividend declaration, Q2 FY27 around Dec 17), not base rates.
