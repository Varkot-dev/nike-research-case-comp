# Profit bridge, earnings power and thesis scorecard (working view, Oct 13, 2026)

**Purpose.** Records the analysis explained in the working session so it lives in the repo: where Nike's operating margin went between FY2024 and FY2026, what earnings power looks like under simple scenarios, and how each thesis test currently scores. Filing figures cite `data/nike_filing_facts.csv`; everything else is labelled as arithmetic or links to the test note that sources it.

## 1. Where the operating margin went (FY2024 to FY2026)

Out of each dollar of revenue:

| Line | FY2024 | FY2026 | Change (pts of revenue) | Source |
|---|---|---|---|---|
| Revenue ($M) | 51,362 | 46,398 | | FY24 10-K p. 57; FY26 10-K p. 55 |
| Gross margin | 44.6% | 42.9% | -1.7 | FY24 10-K p. 33; FY26 10-K p. 32 |
| Demand creation (marketing) | 8.34% ($4,285M) | 10.25% ($4,754M) | -1.9 | FY24 10-K p. 57; FY26 10-K p. 55 (arithmetic) |
| Operating overhead | 23.93% ($12,291M) | 24.48% ($11,360M) | -0.6 | same pages (arithmetic) |
| Other items in EBIT (residual) | | | -0.3 | arithmetic |
| **EBIT margin** | **12.73%** ($6,539M) | **8.30%** ($3,850M) | **-4.4** | FY24 10-K p. 31; FY26 10-K p. 31 (arithmetic) |

- At the FY2024 EBIT margin, FY2026 revenue would have produced about **$2.06B more EBIT** (arithmetic: (12.73% - 8.30%) x $46,398M).
- Overhead *dollars* fell $931M, but overhead as a share of revenue rose because revenue fell $4,964M. That is deleverage, not cost growth.
- FY2026 gross margin includes the $986M expected IEEPA tariff recovery booked in Q4 FY2026 (about 900 bps of Q4 margin, Q4 FY26 release p. 1). Nike says it "largely offsets the impact of the IEEPA tariffs recognized during fiscal 2026" (Q4 FY26 release pp. 4 to 5), so the full-year margin is roughly tariff-neutral, not inflated.

### Gross margin drivers named by Nike
- FY2025: -190 bps total; "Lower NIKE Brand ASP (decreasing gross margin approximately 180 basis points), primarily due to higher discounts and changes in channel mix"; other costs -90 bps "including higher inventory obsolescence reserves"; product costs +80 bps (FY25 10-K p. 35).
- FY2026: +20 bps total; warehousing and logistics +20 bps "primarily due to channel mix"; product costs -20 bps (after the IEEPA recovery); Converse -20 bps; FX +20 bps (FY26 10-K p. 34).
- Q1 FY2027: +60 bps; warehousing and logistics +90 bps; ASP -30 bps; other costs and royalties -40 bps (Q1 FY27 10-Q pp. 19, 23).
- Tariff exposure: "we expect a gross incremental cost of approximately $1.5 billion on an annualized basis" (Q1 FY26 10-Q p. 19).

### Temporary versus structural (working classification; see notes 15 and 16 for the completed discount tests)
| Driver | Size | Classification | What decides it |
|---|---|---|---|
| Discounting / ASP | about -180 bps (FY25) | Temporary only if marketplace actions end; the Q1 FY27 10-Q (p. 20) says Sportswear and Jordan actions now "extend beyond fiscal 2027" | Discount deep dive done: notes 15 and 16 |
| Inventory obsolescence | part of -90 bps (FY25) | Temporary | Inventory vs sales growth |
| Channel mix toward wholesale | lowers ASP, lowers fulfilment cost (+20 to +90 bps logistics) | Deliberate, persistent | Channel margin note 09 |
| Tariffs | about $1.5B gross annualized | Policy-dependent | Trade policy |
| Demand creation step-up | -1.9 pts | Management choice | `thesis_tests/marketing_payoff.md`: returns likely low unless product improves |
| Overhead deleverage | -0.6 pts | Fixable with revenue or Pace | Pace savings of about $2.5B cumulative through FY2031 (8-K filed Oct 1, 2026, p. 2) |

## 2. Earnings power scenarios (arithmetic, illustrative)

Assumptions: 21% tax rate, about 1,481M diluted shares (FY26 10-K p. 55), negligible net interest.

| Scenario | Revenue | EBIT margin | EPS | At 20x | At 18x |
|---|---|---|---|---|---|
| Recovery | $43B | 12% | about $2.75 | about $55 | about $50 |
| Partial | $43B | 10% | about $2.29 | about $46 | about $41 |
| Stuck | $42B | 6.5% | about $1.46 | about $29 | about $26 |

Reference points: share price $35.35 (Oct 12, 2026, market data); consensus EPS FY2027 $1.29 and FY2028 $1.65 (Yahoo, Oct 13, 2026; `thesis_tests/consensus_and_valuation.md`). The reverse DCF there finds $35.35 implies a steady-state EBIT margin of about 11 to 14% by FY2031 at a 9 to 10% WACC, against 12.7% in FY2024 and about 8% today.

## 3. Thesis scorecard (status Oct 13, 2026)

| Test | Leans | Measured result | Note |
|---|---|---|---|
| Valuation and consensus | Short | Price implies 11 to 14% steady-state EBIT margin; FY2027 and FY2028 EPS cut about 25% after Oct 1 | `thesis_tests/consensus_and_valuation.md` |
| Retailer sell-through | Short | Foot Locker comps negative in 3 of 4 quarters while Nike NA wholesale grew 9 to 24%; Foot Locker inventory about +17%; DICK'S Foot Locker inventory write-downs and liquidation of about $260M | `thesis_tests/retailer_sell_through.md` |
| Competitors | Long | Peers grew 5 to 12% a quarter while Nike ran -11% to 0%; adidas +8 to +19% a quarter after its reset | `thesis_tests/competitor_benchmarks.md` |
| Marketing payoff | Short-leaning | Advertising elasticities of about 0.12 short-term and 0.24 long-term; Nike's demand-creation share has no predictive link to next-year growth (R-squared 0.009, FY1994 to FY2026) | `thesis_tests/marketing_payoff.md` |
| Say versus do | Short-leaning | December 2026 completion date dropped between the FY26 10-K (p. 30) and Q1 FY27 10-Q (p. 20); 4.7% of 381 corporate postings are sales or account roles; pay metrics include no channel or full-price measure | `thesis_tests/say_vs_do_execution.md` |
| Consumer interest | Mixed | U.S. search share up year over year for 5 months (from a 37.3% low); worldwide flat at about 35% with adidas +11 pts faster in 2026 Q3 | `thesis_tests/consumer_interest_altdata.md` |
| Marketplace pricing | Short-leaning | nike.com men's sale share 43 to 46% in 2026 (26 to 39% in 2022 to 2023); Running Warehouse Nike markdown share 49% vs HOKA 10% | `thesis_tests/marketplace_pricing_and_shelf_share.md` |
| Review tone (Jin 2023) | Neutral | No statistically reliable link to Nike's next-quarter sales; unpaid nike.com ratings bottomed Feb 2026 (4.47) and rose to 4.54 | `thesis_tests/review_tone_jin2023.md` |

**Working framing.** The evidence currently supports: the share price assumes a margin recovery to roughly FY2024 levels, while Nike's own October 2026 10-Q pushes the end of discount-driven marketplace actions beyond FY2027. The main risk to that framing is the U.S. bottoming visible in search and review data. The discount deep dive (causes and recovery path) will decide the direction.

## 4. Data requests outside this environment
Sources that block automated access or need a login, and that the team can pull through Penn: Euromonitor Passport (sportswear brand shares by country, including China), Mintel or MRI-Simmons (consumer brand preference surveys), Bloomberg (consensus history, short interest), WRDS I/B/E/S (estimate revisions). Uploaded files will be cited and hard-coded into the model.
