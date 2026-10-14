# D5: Is Nike's roughly 60% forward P/E premium to peers justified?

Prepared 2026-10-14. Price about $35.3 (Oct 13 close $35.33 for the headline table). Labels: **OPENED** = source read in this session. **SNIPPET** = search-result text only. **REPO** = earlier repo work, not reopened. **DERIVED** = my arithmetic on the cited inputs.

Data files in this folder: `D5_valuation_monthly_premium.csv` (218 month-ends, Aug 2008 to Sep 2026), `D5_valuation_annual_xbrl.csv` (fiscal-year inputs for Nike and nine US peers), `D5_valuation_midcycle_scenarios.csv`, `D5_valuation_now_crosssection_raw.csv` (Oct 14 Yahoo pull), `D5_scripts/` (re-runnable; `hist.py` expects raw SEC and Yahoo JSON in `../raw`).

## 1. Headline

1. **The premium is mostly an earnings-trough artifact, and it is not unusual for Nike at a margin trough.** FY28 consensus EBIT margin is 7.2% against 12.7% in FY24. On the same FY28 revenue ($43.6B), Nike's P/E at the current price is 12.1x at a 12.7% margin (8% below the 13.2x peer median) and 15.3x at a 10% margin (+16%). The EBIT margin at which the premium is zero is **11.6%**; the margin implied by a 63% premium is 7.1%, which is what consensus models (DERIVED, section 4).
2. **Nike's own history shows premiums of this size at depressed earnings.** NTM P/E premium on a clean-EPS, perfect-foresight basis: median +43% (range +10% to +87%) in Jun 2017 to Jun 2019, and +50% (range +16% to +88%) in Jul 2024 to Dec 2025. In the 2008 to 2010 trough it was only +15% to +28% (section 3).
3. **But the premium is not "justified" by any quality measure.** Revenue growth (+1.1% vs +6.5% peer median), EBIT margin (7.9% vs 13.2%), gross margin (43.4% vs 55.0%), ROE (21.6% vs 24.3%), ROA (6.9% vs 9.6%) and FCF conversion (57% vs 81%) are all at or below the peer median. The one measure that supports a premium is FY27 to FY28 EPS growth (+28% vs +17.7%), and that growth is the margin rebound itself, not a separate argument (section 5).
4. **On EV measures there is no premium at all today.** EV/Sales 1.20 vs 1.22 and EV/EBITDA 11.3 vs 12.0 (Yahoo, Oct 14; Nike's historical EV/Sales premium median was +85%, section 3). The P/E premium exists because Nike's FY27 EPS falls 39% from FY26 GAAP ($1.28 vs $2.10) while peers' rise.
5. **Honest conclusion for the pitch: the premium is neither proof of overvaluation nor unjustified.** It says the price already assumes a margin recovery to about 11.6% (parity with peers) on flat revenue. If Nike gets to 12.7%, the stock is slightly cheaper than peers; at 10%, 16% dearer; at consensus 7.2%, 63% dearer. Berenberg's "premium looks unjustified" line (dig 5) is the weaker of our pillars; use the reverse DCF (dig 1) and the margin-breakeven framing instead. This agrees with dig 1: the bet is on margins, not on the multiple.

## 2. Method and data (and what it cannot do)

- **Fundamentals:** SEC XBRL company facts (data.sec.gov, OPENED, pulled today) for Nike and nine US peers: VFC, COLM, DECK, UAA, LULU, CROX, PVH, RL, WWW. First-filed value per fiscal year, split-adjusted using Yahoo split events. Nike EBIT = pre-tax income minus net interest income (matches repo EBIT: FY2018 4,379, FY2024 6,539, FY2026 3,850; DERIVED, checked). Nike's FY2018 10-K and FY2009 10-K were opened on the investors.nike.com mirror for the adjustments below.
- **Prices:** Yahoo chart API month-end closes (split-adjusted), 2005 to Oct 2026 (OPENED).
- **Forward EPS is perfect foresight, not consensus.** For month-end t, NTM EPS = time-weighted blend of the next two fiscal years' actual EPS. This is the same proxy used in the repo (PitchBook-based `nke_multiples_history.csv`, REPO; I read it from the wonderful-franklin branch). Cross-check: my Sep 2010 Nike NTM P/E is 17.8x, against 17.2x forward in a Sep 2010 Motley Fool table (SNIPPET).
- **Clean EPS for Nike:** FY2008 $3.45 and FY2009 $3.81 (pre-split), from the reconciliation in Nike's FY2009 10-K (OPENED); FY2018 = reported $1.17 plus Tax Act charges ($1,875M transition tax plus $158M remeasurement, FY2018 10-K, OPENED) over 1,659.1M shares = $2.40 (DERIVED; ignores the unquantified offsetting Tax Act benefit, so it is slightly high). Peers are left on GAAP EPS, which is noisy, so I use medians and require at least 4 valid peers.
- **Trailing** uses the last fiscal year reported (fiscal year-end plus 60 days). **EV/Sales** uses the last reported year-end balance sheet and revenue, excluding leases, so it can be up to 12 months stale; compare it within the same date, not across years.
- **Peer set is survivor-biased and US-only for history.** Skechers, Foot Locker and Hanesbrands have no Yahoo price history (acquired). Adidas, Puma, On, ASICS and Anta are not in the history (no XBRL); they are in the Oct 2026 table only. Peers' history is therefore a different set from today's.
- **FY mismatch:** NTM blending calendarizes; the dig 5 headline (FY2 vs FY2) does not, and flatters peers (Nike's FY2 ends May 2028). Calendarized to CY2027 the premium is 79% (dig 5, REPO).

## 3. Nike's premium to peers at comparable points in the cycle

Clean-EPS NTM P/E (perfect foresight) unless stated. Peer median of the available US peers (n in the CSV). Source: `D5_valuation_monthly_premium.csv`, DERIVED.

| Date | Cycle point | Nike last-FY EBIT margin | Nike NTM P/E | Peer median | Premium | Trailing P/E premium | EV/Sales premium (trailing) |
|---|---|---|---|---|---|---|---|
| 2008-12-31 | GFC, FY09 EPS about to fall | 13.4% | 13.3x | 11.6x (n=8) | +15% | n/a (peers lack FY08) | n/a |
| 2009-03-31 | Market low | 13.4% | 12.2x | 9.9x | +23% | +25% (n=4) | n/a |
| 2010-06-30 | Post-trough recovery | 10.2% | 15.3x | 12.0x | +28% | +19% | +54% |
| 2013-06-30 / 2013-12-31 | Mid-cycle, growth | 12.4% / 12.4% | 21.0x / 23.1x | 23.8x / 26.2x | -12% / -12% | +26% / +13% | +9% / +24% |
| 2017-06-30 | FY17 peak margin, pre-reset | 14.3% | 24.6x | 22.4x | +10% | +1% | +119% |
| 2018-03-31 | FY18 margin trough begins | 14.4% | 26.9x | 18.8x | +43% | -46% (peer GAAP noise) | +112% |
| 2018-06-30 | FY18 EPS ex Tax Act | 14.4% | 33.0x | 24.2x | +36% | -45% | +133% |
| 2019-06-30 | Before COVID | 12.0% | 47.8x | 32.7x | +46% | +233% | +71% |
| 2020-06-30 | COVID, FY20 margin 8.0% | 12.4% | 27.4x | 30.2x | -9% | +93% | +208% |
| 2022-09-30 | Inventory glut | 14.7% | 24.5x | 9.8x | +149% | +111% | +188% |
| 2023-12-31 | FY24 EPS pending | 12.1% | 38.6x | 15.3x | +153% | +26% | +127% |
| 2024-06-30 | FY25 EPS fell 42% | 12.1% | 35.0x | 20.1x | +74% | +29% | +53% |
| 2026-06-30 | Trailing only | 8.2% | n/a | n/a | n/a | 0% | 0% |
| **2026-10-13** | **Consensus, FY2 vs FY2** | **8.3%** | **21.5x (FY28)** | **13.2x** | **+63%** | n/a | -2% (EV/Sales Yahoo) |

Window medians (monthly, premium of Nike to peer median; min to max):

| Window | NTM P/E premium, clean | EV/EBIT NTM premium | EV/Sales trailing premium |
|---|---|---|---|
| All, Jul 2009 to Jun 2026 | +11% (-40% to +188%) | +29% | +85% |
| GFC, Oct 2008 to Jun 2009 | +15% (0% to +23%) | n/a | n/a |
| 2010 to 2012 | +3% | +15% | +25% |
| 2013 | -14% | -14% | +14% |
| 2014 to 2016 | -8% | +2% | +105% |
| Jun 2017 to Jun 2019 | +43% (+10% to +87%) | +60% | +97% |
| COVID, Mar to Dec 2020 | +4% (distorted) | +32% | +246% |
| Jul 2022 to Dec 2023 | +116% (+68% to +175%) | +155% | +186% |
| Jul 2024 to Dec 2025 | +50% (+16% to +88%) | +55% | +36% |

Reading, in numbers:

- **A 60% premium is inside Nike's own trough history** (FY18 to FY19: +43% median, +87% peak; 2024 to 2025: +50%; 2022 to 2023: +116%). It is far above the 2008 to 2010 trough (+15% to +28%).
- **Peers de-rated more than Nike.** Peers' median clean NTM P/E was 23.1x in 2010 to 2019 and 13.2x now (-43%); Nike was 22.1x then and about 24.9x now on NTM consensus (0.63 x $1.288 + 0.37 x $1.646 = $1.42; DERIVED), +13% on its own history. Part of the premium is peers being cheap, not Nike being dear. Caveat: the history set and the Oct 2026 set differ.
- **Outcome after high-premium troughs was mixed, not reassuring.** After Jun 2017 to Jun 2019 EPS recovered (FY21 $3.56). After 2022 to 2023 premiums of +116% EPS fell (FY25 $2.16, FY26 $2.10) and the stock fell. The premium has not been a reliable signal either way, in line with `positioning_valuation_history.md` (REPO): the 2017 and 2022 bottoms came at 21x to 26x.
- **Correlation of premium with fundamentals in Nike's own history is weak.** Regressing the semiannual clean NTM premium on (Nike minus peer median EBIT margin) and Nike revenue growth gives R-squared 0.04 (n=31); EV/Sales premium vs margin gap has a correlation of 0.32 (n=34). Nike's premium has historically been a franchise-quality or recovery-hope premium, not a margin-driven one. Low-powered, so treat as "no evidence", not "disproved".

## 4. Trough-earnings test: what premium is implied on mid-cycle EPS

Inputs: price $35.33; FY28 consensus revenue $43,645M (dig 1); net interest income $50M (FY26 XBRL); tax 22.5% (dig 1; FY26 actual 20.3%); diluted shares 1,481.0M (FY26 XBRL). Calibration check: 7.2% margin gives $1.67 vs consensus $1.646, so the bridge reproduces consensus within 1.5%. All DERIVED. File: `D5_valuation_midcycle_scenarios.csv`.

| FY28 EBIT margin | EPS | P/E at $35.33 | Premium to peer FY2 median 13.2x | Premium to peer FY1 median 15.8x |
|---|---|---|---|---|
| 7.2% (consensus) | $1.67 | 21.1x | +60% | +34% |
| 8.3% (FY26 actual) | $1.92 | 18.4x | +39% | +17% |
| 10.0% | $2.31 | 15.3x | +16% | -3% |
| 11.8% (10-year average, dig 1) | $2.72 | 13.0x | -2% | -18% |
| 12.7% (FY24) | $2.93 | 12.1x | -8% | -23% |

If the margin gets there only by FY31 on 3% revenue growth ($47.7B): P/E on FY31 EPS is 14.0x at 10% ($2.52), 11.9x at 11.8% and 11.1x at 12.7% ($3.20). These are undiscounted; dig 1's reverse DCF is the discounted version (about 9.5% annual return if FY24 margin is regained by FY31).

Breakevens: zero premium needs EPS $2.68 (11.6% margin); a 25% premium needs $2.14 (9.3%); today's 63% needs $1.64 (7.1%).

Two limits on this test. (a) Peers' 13.2x is not on mid-cycle earnings either. Using each US peer's latest fiscal-year operating margin (pre-tax where no operating line) against its own 2012 to 2025 median (XBRL, DERIVED): VFC 6.0% vs 12.1%, COLM 6.1% vs 10.1%, CROX 3.7% vs 8.1%, PVH 2.6% vs 8.1%, UAA -3.3% vs 4.7% are depressed; DECK 23.1% vs 15.9%, RL 14.5% vs 11.2%, WWW 8.0% vs 6.4% are elevated; LULU 19.9% vs 21.4%. Nike is at 66% of its own median (8.4% vs 12.8%), against a peer median ratio of about 0.9, so Nike is more depressed than a typical peer and some premium is fair. A like-for-like mid-cycle peer P/E would be lower than 13.2x for the depressed peers, which narrows Nike's implied discount at 12.7%. (b) Reaching the mid-cycle margin on flat revenue is the claim in dispute (D1, dig 1), not a given.

## 5. Which measures could justify a premium now? (Oct 14 Yahoo pull, `D5_valuation_now_crosssection_raw.csv`; P/E from the Oct 13 table)

| Measure | Nike | Peer median | Supports a premium? | Note |
|---|---|---|---|---|
| FY2 revenue growth (consensus) | +1.1% | +6.5% (ASICS +11.3%, On +19.0%, adidas +6.5%) | **No** | Peers' P/E vs revenue growth: R about 0.18 (n=8); On and ASICS at 17.3x and 21.8x are the only peers near Nike. |
| FY2 EPS growth | +28.0% | +17.7% | Yes, but circular | It is the margin rebound from a -39% FY27 step down. Peers' P/E correlates 0.74 with EPS growth (n=8, UAA's +79% drives much of it). Regression on 7 peers ex UAA predicts Nike at 15.3x (R-squared 0.10, very weak); with UAA 16.2x. |
| PEG (FY2 P/E over FY2 EPS growth) | 0.77 | 0.89 | Yes, marginally | Same circularity. |
| EBIT margin (TTM) | 7.9% | 13.2% | **No** now; yes if 11.6%+ returns | Own 10-year average 11.8%. |
| Gross margin | 43.4% | 55.0% | **No** | Gap is structural (wholesale mix, Direct discounting), not a trough artifact. |
| ROE / ROA | 21.6% / 6.9% | 24.3% / 9.6% | **No** | Nike reported ROIC 18.7% FY26, 20.2% FY25 (dig 1, REPO). Peer US ROIC proxies in the CSV are noisy (negative-equity names). |
| FCF / net income (TTM) | 57% | 81% | **No** | Nike FCF $1.77B vs about $2.4B annual dividend at $1.64 per share (REPO; D6 covers this). |
| EV/Sales, EV/EBITDA (TTM) | 1.20x, 11.3x | 1.22x, 12.0x | n/a (no premium) | Premium is only in forward P/E. |
| Brand share | Nike share of 14-company China peer set 65% (2022) to 50% (H1 2026) (REPO scoreboard) | n/a | **No** | Share is falling where measured. |
| Balance sheet | Net debt about -$0.5B (debt 7.9B, cash 8.4B, dig 1) | Mixed | Neutral | Not a premium driver. |

Only two things put Nike above peers on a quality basis: scale and the size of the possible rebound. Neither is a measured earnings driver today.

## 6. Alternatives considered and how each was tested

| Explanation of the 63% premium | Test | Result |
|---|---|---|
| Trough earnings (EPS depressed by margin) | Mid-cycle EPS grid, section 4 | **Survives, main driver.** Zero premium at 11.6% margin. |
| Fiscal-year mismatch | Calendarized CY2027 in dig 5 | Ruled out (makes premium bigger, 79%). |
| Peer-set choice | dig 5: survives all sets except On and ASICS | Partly; Nike trades like the two fastest growers on +1% growth. |
| Peers de-rated, Nike not | Peers' NTM P/E 23.1x (2010 to 2019) vs 13.2x; Nike 22.1x vs about 24.9x | **Survives, secondary.** Roughly 40 points of the gap versus history comes from peers. |
| Higher growth | Section 5 | Ruled out for revenue; circular for EPS. |
| Higher quality (ROIC, margin, cash conversion) | Section 5 | Ruled out; Nike is below median on each. |
| Nike always carries a premium | Section 3: median +11% all-period NTM, +85% EV/Sales | Partly. Historical premium was in sales multiples (margin 12% to 15% vs peers about 8%), which has now vanished (-2%). |
| Brand or share strength | Share data (REPO) | Ruled out where measured (China, Europe). |
| Accounting basis (GAAP vs adjusted) | dig 5: consensus on adjusted basis | Ruled out as an overstatement. |
| Dividend or buyback support | Not tested here | Left to D6. |

Two explanations survive: **trough earnings** (large) and **peers' own de-rating** (secondary). Data that would separate them further: contemporaneous consensus (not perfect-foresight) multiples for Nike and a fixed peer set over 2008 to 2026, and a margin-normalized peer P/E.

## 7. Routes tried (never accept inconclusive)

| # | Route to the fact "Nike's and peers' contemporaneous forward P/E history" | Result |
|---|---|---|
| 1 | SEC XBRL actual EPS, perfect-foresight NTM | **Worked** (used; proxy, not consensus) |
| 2 | Yahoo quoteSummary earningsTrend history | Partial: current estimates only, no history |
| 3 | web.archive.org snapshots of quote pages | **Blocked** (connection reset by proxy) |
| 4 | Stooq price download; Macrotrends P/E page | **Blocked** (reset; HTTP 403) |
| 5 | Web search for dated forward P/E statements (Mar 2009, 2018) | Partial: one SNIPPET (Sep 2010: Nike 17.2x, Columbia 23.7x, Polo Ralph Lauren 17.4x); nothing for 2009 or 2018 |
| 6 | Repo PitchBook-based `nke_multiples_history.csv` (other branch) | Partial: Nike only, also perfect foresight; consistent with this note (e.g. FY2016 end forward 23.1x) |
| 7 | Yahoo prices for delisted peers (SKX, FL, HBI) | **Blocked** (404) |
| 8 | Peers' FY2008 EPS for 2008 to 2009 trailing P/E | Partial: XBRL starts FY2009 for most; trailing premium before Mar 2009 left blank, NTM used |
| 9 | Nike 10-Ks via investors.nike.com mirror (FY2009, FY2018) | **Worked** (adjustments sourced) |

Settling it needs Bloomberg BEst, FactSet or Refinitiv historical consensus (`research_notes/Refinitiv pull list.md` lists the pull).

## 8. Weaknesses

1. History uses actual future EPS, which flatters the premium whenever EPS later rebounded (2018 to 2019) and understates it when EPS fell (2023 to 2025). It is not what the market saw.
2. Peer history is nine US names on GAAP EPS with survivor bias; today's set is global. The two are not comparable levels, only direction.
3. Peer ROIC proxies are noisy; I rely on Yahoo ROE and ROA, which carry leases and buyback distortions.
4. Mid-cycle margin test holds revenue at consensus; Berenberg and D1 argue revenue is lower, which would raise the margin needed for parity.
5. Yahoo prices on Oct 14 differ slightly from the Oct 13 table (NKE FY1 and FY2 EPS $1.276 and $1.634 vs $1.288 and $1.646); the premium is 63% on Oct 13 data.
6. Regressions are tiny samples (n=7 to 34, autocorrelated) and are shown only to say that no fundamental explains the premium well.

## 9. Use in the pitch

- Drop or soften "the premium is unjustified". Say instead: "At $35 Nike trades at 21.5x FY28 EPS vs a 13.2x peer median because FY28 margin is 7.2%. Peer parity needs an 11.6% EBIT margin on flat revenue, 4.4 points above consensus and just under Nike's 10-year average of 11.8%."
- Lead with the margin breakeven and dig 1's reverse DCF, not the multiple.
- If a judge says "troughs always look expensive", concede and cite section 3 (+43% in FY18 to FY19, +50% in 2024 to 2025) and that the later outcomes were mixed.
