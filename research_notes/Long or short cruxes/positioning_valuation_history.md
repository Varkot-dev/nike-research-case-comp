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

## Round 3: conditioning the base rates on reported fundamentals (2026-10-14)

Both earlier rounds agreed that price history alone could not say whether Nike bottoms, and that the deciding factor was the fundamental path (margin recovery). This round tags every deep-drawdown setup since 2010 with what the company had reported at that point (revenue growth, gross margin change, operating margin change, price/sales, trailing P/E) and with the next reported quarter. Nike has already guided its next quarters, so for Nike that is known now, not hindsight.

### 0. Pre-registered test (written before the data pull)

- LONG if: among setups 60% or more below the 5-year high where the last reported quarter matched Nike's state (revenue falling, gross margin up), the median 12-month excess return is positive with more than half positive, and clearly beats the "gross margin contracting" setups.
- SHORT if: Nike's bucket has a negative median with fewer than half positive, or analog bottoms came only after revenue growth itself turned.

### 1. New primary data

| # | Source | Date | Status |
|---|---|---|---|
| F1 | SEC XBRL companyfacts API (data.sec.gov/api/xbrl/companyfacts), 45 US filers: NKE UAA VFC LULU PVH CROX DECK CPRI TPR RL COLM WWW FOSL LEVI CRI GIII OXM VRA SHOO HBI SKX SBUX EL GAP KSS M URBN ANF AEO ZUMZ BBWI BOOT FL GES CHS EXPR PTON PYPL NWL MAT HAS CMG TGT INTC KHC. Quarterly revenue, gross profit (or revenue less cost of sales), operating income (pretax income where operating income is not tagged, e.g. Nike), diluted weighted shares. Q4 derived as annual less nine months. Current quarter uses the first-filed value; the prior-year comparison uses the version on file as of the current filing (same accounting basis after restatements, e.g. VF divestitures). | fetched 2026-10-14 | OPENED |
| F2 | Yahoo Finance v8 price files from rounds 1 and 2 (scratchpad/hist/dl and skep/dl), plus their split events, used to rebuild unadjusted prices and market caps | fetched 2026-10-14 | OPENED |
| F3 | Nike Q1 FY27 call transcript (Oct 1, 2026, in repo scratch flat_Q1FY27.txt): gross margin 42.8%, up 60bp, "benefits from our supply chain cost management efforts and FX tailwinds, partially offset by increased discounts"; FY27 revenue "decline in the high single-digit range"; Q2 has "a headwind of approximately 400 basis points to revenues"; supply reductions will pressure "reported revenues for the remainder of fiscal '27 and into '28"; EBIT to decline by a greater percentage than revenue | 2026-10-01 | OPENED |
| F4 | Nike Q4 FY26 transcript: Q4 gross margin 49.2% including a 900bp IEEPA tariff recovery; 40.2% excluding it, down 10bp | 2026-07 | OPENED |
| F5 | Nike Q2 FY26 transcript: gross margin down 300bp to 40.6% "primarily due to increased product costs due to higher tariffs in North America as well as inventory obsolescence in Greater China" | 2025-12 | OPENED |

Checks on F1/F2 (ARITH): Nike market cap $52.5B on 2026-10-12 (1,484.2M diluted shares x $35.35), $71.3B on 2014-01-02; UAA $14.6B on 2015-01-02; Deckers $10.4B on 2023-01-03; all in line with published figures. Nike XBRL quarters match the transcripts: Q1 FY27 revenue $11,213M (-4.3%), gross margin 42.8% (+61bp); Q4 FY26 49.2% (+888bp, tariff refund).

Nike now, on the same definitions: revenue -4.3% and guided worse. FY26 revenue $46.4B; a 7% to 9% decline gives $42.2B to $43.2B; less Q1 $11.21B leaves $31.0B to $32.0B for Q2 to Q4 against $34.68B, i.e. -7.8% to -10.6% (ARITH). Gross margin up 61bp; Q2 FY27 laps a 40.6% quarter that carried tariff costs and China obsolescence (F5), so gross margin is likely up again in Q2. Price/sales 1.14x ($52.5B / $45.99B trailing revenue). 5-year drawdown about 80%.

### 2. Method

Universe: the 45 F1 names with price data (39 had both). Two setup definitions, as in round 2: (a) "drop": one-day fall of 8% or more (proxy for a guide cut), one per 90 days; (b) "quarterly": first trading day every third month while below the depth threshold. Filters: event after mid-2010 (XBRL era), 2020 excluded, S&P trailing 12 months above -5% (idiosyncratic only). State = latest quarter ended at least 20 days before the event and filed within 30 days after it (proxy for the earnings release); a strict "filed before the event" version gave the same signs. Excess = stock total return minus S&P 500 total return. coW = median of per-company medians. Scripts: scratchpad/fund2/tool/ (q2.py, val.py, study.py, trough.py).

### 3. Result A: reported margin state alone does not separate outcomes

| Bucket (all 39 names) | Drop, 60% | Drop, 75% | Quarterly, 60% | Quarterly, 75% |
|---|---|---|---|---|
| All | N=141, med12 -9, 45% pos | N=59, +3, 51% | N=282, -12, 41% | N=93, -7, 45% |
| Revenue down, GM down | -10, 41% | 0, 50% | -6, 44% | 0, 50% |
| Revenue down, GM up (Nike) | -4, 50% (N=50) | +7, 52% (N=31) | -11, 46% (N=90) | -7, 44% (N=45) |
| Revenue down, GM up, op margin up (Nike exactly) | -17, 40% (N=30) | -14, 41% (N=22) | -17, 40% (N=55) | -15, 40% (N=30) |

Pre-registered LONG test fails in 2 of 4 specifications and passes weakly in 2. No edge either way from the reported state.

### 4. Result B: valuation. Nike is unusually expensive for its drawdown

Among quarterly samples at 75% or more below peak, only 11 of 93 were at 0.8x sales or above (Nike 1.14x). At the 27 clean idiosyncratic troughs since 2011 (section 6) the median price/sales was 0.42x; 5 of 25 bottomed at 1.0x or above (UA Nov 2017 1.03x, Capri Jun 2017 1.19x, Tapestry Sep 2015 1.82x, Hasbro Nov 2023 1.10x, PayPal Oct 2023 1.97x). So premium brands can bottom above 1x sales. Valuation buckets were noisy and not monotonic (0.5x to 1.0x was the worst bucket in all four specifications: 28% to 36% positive).

### 5. Result C: the strongest discriminator is whether the next revenue print gets worse, and it splits on gross margin

| Bucket | Drop 60% | Drop 75% | Quarterly 60% | Quarterly 75% |
|---|---|---|---|---|
| Revenue down now, next quarter more than 2 pts worse (Nike's guided path) | N=28/15 cos, med6 -20, med12 -20, 6m pos 7/28, coW6 -19 | N=16/9, -17, -11, 5/16, -19 | N=47/19, -23, -17, 17/47, -13 | N=23/11, -14, -11, 9/23, -10 |
| Revenue down now, next 3 quarters all better | N=37, med6 +10, med12 +17, 6m pos 21/37 | N=19, +7, +34, 10/19 | N=90, +13, +3, 56/90 | N=28, +19, +5, 19/28 |
| Nike path AND next-quarter GM down | N=13, med6 -25, med12 -27, 6m pos 1/13 | N=5, -19, -37, 1/5 | N=22, -25, -31, 7/22 | N=7, -29, -41, 1/7 |
| Nike path AND next-quarter GM up | N=15, -11, -9, 6/15 | N=11, -11, -9, 4/11 | N=25, -20, -1, 10/25 | N=16, +1, +12, 8/16 |
| Nike path AND GM up now AND next GM up | N=12, -1, -11, 6/12 | N=9, -5, -12, 4/9 | N=18, +2, -6, 9/18 | N=14, +6, -7, 7/14 |
| Nike path AND P/S 0.9x or more | N=7, +15, -19, 4/7 | N=3, +15, -19, 2/3 | N=8, +9, +8, 6/8 | N=3, +21, -48, 2/3 |
| Nike path AND P/S under 0.9x | N=20, -27, -22, 3/20 | N=12, -24, -5, 3/12 | N=36, -25, -18, 11/36 | N=20, -18, -10, 7/20 |

Apparel names only (Nike path): drop 60% N=22, med6 -27, 6m pos 4/22; quarterly 60% N=38, med6 -25, 12/38. Apparel names with GM up now and next: 4/9 and 7/14 positive at 6 months.

Read: "revenue about to get worse" is a strong negative on its own (25% to 39% positive at 6 months in all four specifications, 32% for apparel only), but almost all of that comes from cases where gross margin was also contracting (10 of 47 positive at 6 months, medians -19 to -29) or the stock was already cheap and distressed. When gross margin kept rising through the worse revenue prints, outcomes were a coin flip (42% to 50% positive, medians -12 to +6). The premium-valued cases (Capri 2017, Estee Lauder Feb 2025, Hasbro Oct 2023, Kraft Heinz 2022) did better than average, but the sample is 3 to 8 cases from the same few names, so it is not evidence either way.

Cases in the Nike-path, premium-valued group (drop, 60%): Capri 2017-02-07 x6 +15 x12 +63; Estee Lauder 2025-02-04 +28 / +61 (after the Nov 2024 dividend cut and Jan 2025 CEO change); Hasbro 2023-10-26 +16 / +4; Intel 2024-08-02 -22 / -27 (dividend suspended that day); Peloton 2024-11-01 -5 / -19 and 2025-03-06 +15 / -57; Vera Bradley 2016-12-07 -43 / -29.

Nike's own record fits the split: Mar 2025 (revenue -9.3%, next -12.0%, GM -326bp, so the GM-down bucket) was followed by -37 twelve-month excess (round 1).

### 6. Result D: did bottoms wait for the worst revenue quarter? No

Clean troughs: price at its lowest within plus or minus 18 months, 60% or more below the 5-year high, at least 120 days apart, S&P no more than 12% below its 1-year high (removes Apr 2025, 2022 and 2011 market bottoms). N=27 troughs, 20 companies (ARITH, trough.py).
- 16 of 27 bottomed before the worst revenue quarter was released (10 of them more than 100 days before); 11 of 27 after. Median: trough 22 days before the worst print.
- 14 of 27 bottomed while the latest reported revenue growth was still negative.
- 6 of 27 bottomed with a print more than 2 points worse coming next quarter: UA Nov 2017, Deckers Oct 2012, Wolverine Oct 2023, Fossil Apr 2024, Vera Bradley Nov 2017, Hasbro Nov 2023.
So the strict SHORT test ("bottoms come only after revenue turns") fails: stocks often bottomed before the worst revenue print.

### 7. Alternatives tested

1. "Worse revenue ahead means short." True on average (section 5, first row), but explained by gross margin direction and distress. With GM rising, the edge disappears. Not a sufficient short case for Nike unless its GM turns down.
2. "Nike's guided decline is already priced, so the historical 'worse next quarter' cases are not comparable (those were surprises)." Partly tested: the drop sample is made of guide-cut days, where the market had just repriced, and results are the same as the quarterly sample. Not fully settled; no historical consensus data were available.
3. "Premium-valued brands bottom earlier." Weakly supported (5 of 25 troughs at 1x sales or more; 4/7 and 6/8 positive at 6 months in the premium Nike-path cases), but N is 3 to 8 and dominated by Estee Lauder, Capri and Hasbro. Not established.
4. "Margin recovery is what makes a bottom." Supported in the direction that matters: margin contraction plus worse revenue is reliably negative (10 of 47 positive at 6 months). Margin expansion plus worse revenue is only neutral, not positive.
5. "Look-ahead bias from using the next quarter." For Nike the next-quarter revenue direction is in guidance (F3); gross margin direction is not guided, which is why it is left as the open variable.
6. "Results depend on the quarter-release timing proxy." Strict filed-date timing gave the same signs (quarterly 60%: Nike-path GM down 27% to 25% positive at 12 months; GM up 42% to 46%).

### 8. Verdict for this round

History does not settle LONG versus SHORT for Nike on the facts known today. It does settle the conditional: what decides it is the gross margin on Q2 FY27 (reported about Dec 17, 2026) and Q3 FY27 while revenue falls 8% to 11%.
- If gross margin keeps rising year over year through the worse revenue prints (likely in Q2, given the 40.6% comparison that carried tariffs and China obsolescence), history is a coin flip (about 45% positive, medians near zero at 6 months), with a typical worst point about 28% to 35% below the entry price within 12 months.
- If gross margin turns down year over year while revenue falls (the discount-driven marketplace reset Nike describes could do this), history is strongly SHORT: 10 of 47 positive at 6 months, medians -19 to -29 at 6 months and -27 to -41 at 12 months.
Note the mechanical problem for Q4 FY27 (reported about late June 2027): it laps a 49.2% gross margin inflated by the 900bp IEEPA refund, so reported gross margin will be sharply down that quarter. That is outside a 6-month window from Nov 2026, but it is a known bad optic.

### 9. What would settle it

- Nike's Q2 FY27 gross margin versus 40.6% (Dec 2026), and any gross margin framing at the Nov 16 to 17 Investor Day. Down year over year means the strongly negative bucket; up means neutral.
- Q2 FY27 revenue versus the implied -8% to -11%: a decline smaller than about 6% would move Nike out of the "next quarter worse" bucket into the bucket that has been 54% to 68% positive.
- Historical consensus revisions (not freely available) would test alternative 2.

## Skeptic review (Round 3)

Prepared 2026-10-14 by an independent reviewer of Round 3. Scripts: `scratchpad/skep3/` (`study_om.py`, a copy of `fund2/tool/study.py` with next-quarter operating margin, second-next-quarter gross margin, earnings-reaction and P/E splits added; `rec.py`, a release-anchored event study). Same SEC XBRL and Yahoo files as Round 3 (fetched 2026-10-14, OPENED).

### 1. Numbers re-checked at source

- Round 3 tables reproduce exactly when `study.py` is re-run (drop 60%: Nike path N=28, 6m positive 7/28, next-GM-down 1/13, next-GM-up 6/15; quarterly 75%: next-GM-down 1/7, next-GM-up 8/16) (ARITH, OPENED).
- Nike XBRL (data.sec.gov companyfacts, fetched 2026-10-14, OPENED): Q2 FY26 gross profit $5,045M on $12,427M = 40.6%; Q3 FY26 $4,530M on $11,279M = 40.2%; Q4 FY26 $5,393M on $10,972M = 49.2%; Q1 FY27 $4,798M on $11,213M = 42.8%. Q1 FY27 SG&A $3,910M vs $4,016M (-2.6%), pretax $921M, tax $209M (22.7%), diluted shares 1,484.2M. All match Round 3.
- Q1 FY27 transcript (Oct 1, 2026, OPENED, scratch flat_Q1FY27.txt): Round 3 quoted the gross margin and revenue lines correctly. It left out one sentence that matters: "We currently expect EBIT to decline by a greater percentage than revenue. This outlook reflects continued pressure on gross margin and fixed cost deleverage associated with lower revenue levels, higher input costs." Taken alone, that reads like a gross margin decline. Section 2 resolves what it means.
- Q4 FY26 transcript (Jul 2026, OPENED): before the reset, Nike guided "gross margins to inflect positive in Q2" and then "gross margin expansion earlier beginning in Q1", with tariff costs assumed at 10% through July and 15% after that.

### 2. New: the EPS guide pins down the gross margin direction for Q2 to Q4 (ARITH from section 1 data)

Round 3 calls gross margin "not guided" and treats it as the open swing variable. The EPS and revenue guide, combined with the SG&A statement, largely closes that gap.
- FY26 Q2 to Q4: revenue $34,678M; gross profit $14,968M, which is $13,981M after removing the roughly $987M IEEPA refund (900bp x $10,972M); gross margin excluding the refund 40.3% (43.2% reported). SG&A $12,098M. Non-operating items +$108M.
- FY27 Q2 to Q4 implied by the guide: revenue $31.0B to $31.9B (FY down 7% to 9%, less Q1). EPS $1.15 to $1.35 less Q1 $0.48 gives $0.67 to $0.87, which is net income $995M to $1,292M and pretax $1,287M to $1,671M at Q1's 22.7% tax rate. If SG&A falls 3% (Q1's rate), gross profit is $12.9B to $13.3B and gross margin about 41.6% at matched ends (range 40.4% to 42.9%). That is about +130bp against the 40.3% base excluding the refund. If SG&A falls 6%, gross margin is about 40.5%, roughly flat. Pretax margin is 4.1% to 5.2% against 5.7%.
- Reading: the guide implies gross margin flat to up in Q2 and Q3 against the weak 40.6% and 40.2% comparisons. It implies operating margin down, and reported gross margin down only in Q4 (against 49.2%) and for the full year (against 42.9%). So "continued pressure on gross margin" fits the reported full-year and Q4 optics, not a decline in Q2 or Q3. A Q2 or Q3 gross margin decline would require missing Nike's own guide or cutting SG&A much faster than the 2.6% Q1 pace.
- Consequence: the 6-month window that matters for the Nov 2026 pitch (to about May 2027) contains the Q2 and Q3 prints, and both should land in Round 3's "gross margin up" bucket. The strongly SHORT bucket (10 of 47) is a tail risk for this window, not the base case. The Q4 FY27 print (late June 2027) falls outside it.

### 3. New: guide-cut reaction and consensus (SNIPPET and OPENED)

- AskTraders, 2026-10-01 (OPENED): FY27 revenue consensus before the print was $45.34B, and analysts expected FY27 EPS of $1.66. The guide midpoint of about $1.25 is roughly 25% below that, and revenue is about 6 points below consensus. The stock was indicated at $33.20 after hours (-5.55% from $35.15).
- Finviz/RTTNews, 2026-10-02 (OPENED): "nearly 9%" down pre-market. Q1 revenue $11.21B vs $11.35B expected; EPS $0.48 vs $0.44 expected.
- Yahoo closes (OPENED): Oct 2 $33.87 (-3.6%), Oct 12 $35.35, above the pre-print $35.15. The stock absorbed a roughly 25% EPS reset within 7 trading days and did not register as an 8% "drop" event. This is the strongest datum against SHORT that Round 3 did not use: the guided decline looks priced, and short interest had already risen 31% in September (Round 2 review).
- Historical test of that pattern (`rec.py`, release-anchored, Nike path, 60% depth, N=40, 17 companies): over all releases, 6m median excess -10 (17/40 positive) and 12m median -12 (14/38). When the stock had recovered to the pre-release close within 7 trading days: 6m +1 (8/15) but 12m -15 (4/15). Only one exact analog had a down day of 3% or more followed by full recovery: Under Armour, 2024-05-23 (-3.3%, then +1.0%; next gross margin up): 6m +31, 12m -19. At 75% depth: recovered 3/6, not recovered 5/13. Read: absorbing the news helps a little at 6 months and nothing at 12. Not decisive.

### 4. Robustness problems in the "gross margin up" bucket (points neither way)

- Concentration: Fossil (0.05x to 0.4x sales, near-distressed) is 6 of 25 quarterly-60% cases and 5 of 15 drop-60% cases in the "next gross margin up" bucket, and Peloton adds 2 more. Excluding FOSL and PTON: next GM up 6m positive 3/8, 1/5, 7/17, 5/7 (12m 5/8, 3/5, 8/17, 5/7). Next GM down 1/12, 1/4, 7/18, 1/5. The gross-margin split survives; the GM-up bucket stays a coin flip at 6 months and leans slightly positive at 12.
- Nike's forward state is revenue worse, gross margin up, operating margin down. That bucket gives 6m positive 2/6, 1/5, 4/12, 4/6 and 12m 4/6, 3/5, 5/12, 4/6 (N=5 to 12): too small to read.
- P/E of 20x or more inside the Nike path: 6m 1/6, 3/8, 2/6 positive (VFC 2023, Fossil 2018, ANF 2014 to 2016 lost; Gap 2023 and Vera Bradley won). N too small, but this does not support the idea that premium names bottom early.
- Closest brand analogs in the GM-up bucket: Under Armour 2023 to 2025 (6m -20, +15, -24, -29; 12m -8, -24, -40) and VF Nov 2023 (-24 / +27) lean negative. Capri 2017 (+11 / +60) and Estee Lauder Feb 2025 (+7 / +28) lean positive. Two and two.

### 5. Reviewer verdict

Round 3's numbers are accurate and its gross-margin split is real and robust to dropping the dominant names. I add two things it missed, and they point in opposite directions. (1) The EPS guide implies gross margin flat to up in Q2 and Q3 FY27, so in the pitch window Nike most likely sits in the coin-flip bucket, not the SHORT bucket. That makes history less able to support SHORT than Round 3's "swing variable" framing suggests. (2) The coin-flip bucket is genuinely a coin flip, and the closest sportswear analog (Under Armour 2023 to 2025, the same marketplace-cleanup playbook) lost in 3 of 4 cases at 6 months. The market shrugging off a 25% EPS guide cut is a mild positive at 6 months and nothing at 12. History does not settle it. Verdict: NEUTRAL, moderate. The base-rate SHORT case only becomes live if Q2 gross margin comes in below 40.6% (Dec 2026) or Investor Day frames FY28 below the FY27 trough. Base rates cannot supply a LONG case; that would have to come from the fundamental work elsewhere in the repo.

## Re-weighed with hunt data (2026-10-14)

Previous verdict (Skeptic review, Round 3): NEUTRAL, moderate. History does not settle it; the base-rate SHORT case only becomes live if Q2 FY27 gross margin falls below 40.6% or Investor Day frames FY28 below the FY27 trough.

Only hunt tests the checker did not fail are used. Folders: `data/hunt/people_governance/`, `data/hunt/peers_reported/`, `data/hunt/pricing_catalog/`, `data/hunt/macro_category/`.

### 1. New positioning data from a different source (people_governance)

This question was graded on price, short interest and fundamentals. The hunt adds three positioning series that were not in the repo: SEC insider data sets 2006 to 2026 (Nike and 29 peers), 13F holder breadth for 59 consumer stocks 2014 to 2026, and borrow, short-volume and fails-to-deliver data.
- 13F breadth: NKE holders fell 14.5% YoY to 2026Q2 (3rd lowest of 56 stocks). After the checker's fix for exits that became eligible for the 13F small-position exemption, net entries are -25 and -39, still the worst since 2018 but about 80% smaller than first stated. Across 2,111 stock-quarters, breadth losers of this size did not underperform (median 126d excess +1.3% vs -2.9% for all). The checker found the deep-drawdown split disagrees across horizons (126d SHORT-looking, 252d LONG-looking).
- Insiders: Nike open-market buying in 2025 and 2026 is the largest in 20 years ($5.96M, $2.73M). The checker showed that "selling drying up" rests on Parker only, and that both of Nike's own buy rounds (Dec 2025, Apr 2026) lost 31 to 34 pts vs SPY over 126 days.
- Short side: SI rose 4 straight prints to 99.2M; across about 60 consumer stocks, a 4-print SI run is followed by another rise only 47% of the time (base rate 50%). Borrow is easy (IBKR 0.41%, 8 to 10M shares available; days to cover 2.6). Crowded but not squeezable, which matches the Round 2 skeptic.

### 2. Extra test run for this re-grade (pre-set)

Script: `data/hunt/people_governance/scripts/regrade_positioning_conditional.py` (ARITH on the hunt CSVs).
Rule set in advance: if, among deeply fallen stocks, insider clusters or breadth losses separate later outcomes (12m median excess beyond +/-10 with at least 60% one way), positioning history would move this question toward LONG or SHORT. Otherwise it stays NEUTRAL.
- Insider purchase clusters at peers after a prior 12-month fall of 40% or more: N=13, 126d median +7.4 (8 of 13 positive), 252d median -12.8 (5 of 11 positive). At a fall of 50% or more: 126d +17.9 (6/8), 252d -12.8 (3/7). Short-horizon pop, then a fade, with N under 15 and overlapping 2022 events (VFC twice, AEO, WWW).
- 13F breadth panel restricted to stocks 60% or more below their 5-year high (26 tickers with prices, 449 rows): all such quarters 126d median -8.8 (32/68), 252d -9.0 (22/59). Adding a breadth loss of 10 pts or more: 126d -6.3 (20/41), 252d -3.4 (16/39). Breadth losers did slightly better than other deep fallers, not worse. Nike's own first breadth-loss signal (Feb 2026) was followed by -50.2 excess over 126 days, one in-sample point.
- Result: neither signal separates outcomes. Deeply fallen stocks drift mildly negative at 12 months (about 38% to 41% positive), which is the same coin flip with a negative median found in Rounds 1 and 3.

### 3. Fundamental data relevant to Round 3's gross-margin split

- peers_reported (checker-adjusted): Nike's gross margin gap to peers closed from -530 bps to -75 bps, but about 145 bps of that is peers falling; Nike GM in Jun to Aug 2026 was +61 bps YoY (42.8%). This is reported data from a different source that agrees with the Round 3 skeptic: Nike sits in the "GM up" (coin-flip) bucket for the pitch window, not the "GM down" (strongly SHORT) bucket.
- pricing_catalog (checker-adjusted): nike.com discount share was flat YoY over Mar to Sep 2026 (crawl-cluster CI -4.4 to +5.6) with a Jul to Aug rise, partly hidden "price in bag" promotions growing. That is a risk to Q2 FY27 gross margin, but it did not stop Q1 GM from rising, so it does not move Nike into the GM-down bucket yet.
- macro_category and peers_reported both show share loss in China and EMEA. That is fundamental evidence for other questions, not for whether base rates resolve direction.

### 4. Verdict

Unchanged: NEUTRAL, moderate. The new positioning data are a genuinely different source (insider filings, 13F holder counts, borrow market), and they independently agree that positioning and sentiment history do not call the direction for a stock this far down: insider clusters pop then fade (126d +7, 252d -13, N=13), breadth losses in deep drawdowns are no worse than other deep fallers, SI runs do not extrapolate, and borrow is cheap. That confirms "history does not settle it" rather than pushing it to LONG or SHORT. It is not upgraded to strong because the extra tests have N of 13 to 41 with overlapping events, and the GM-bucket assignment still depends on Q2 FY27 (Dec 2026). For the pitch: do not cite record short interest, 13F exits or insider buying as directional evidence either way; cite them as "crowded, cheap to hold, no squeeze trigger."
