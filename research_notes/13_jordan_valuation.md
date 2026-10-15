# Jordan Brand: scenario valuation (illustrative)

**Prepared:** October 13, 2026. **Status:** illustrative. Nike discloses no Jordan profit, margin, units or inventory, so every growth rate and margin below is a labelled **assumption**, chosen to bracket the evidence in `12_jordan_brand_thesis.md`. **Built by:** `scripts/jordan_valuation.py`. **Outputs:** `data/valuation/jordan_scenarios.csv`, `data/valuation/jordan_sensitivity.csv`. **Chart:** `charts/19_jordan_valuation.png`.

## 1. Method

- **Starting point:** Jordan FY2026 revenue of $7,034M (FY26 10-K p. 32). FY2024 peak $8,701M on the same basis (FY26 10-K p. 32).
- **FY2027 in every scenario: -15%.** Q1 FY2027 Jordan revenue fell "by mid-teens" (Nike transcript, Q1 FY27 call, Oct 1, 2026), and Nike says the Jordan actions "extend beyond fiscal 2027" (Q1 FY27 10-Q p. 20).
- **Margin path:** Jordan starts at 5.7% EBIT margin in FY2027, the consolidated margin implied by consensus EPS (`research_notes/thesis_tests/consensus_and_valuation.md` Section C). It ramps in a straight line to each scenario's FY2031 margin.
- **DCF conventions copied from the repo's reverse DCF** so the two can be compared:
  - 10% WACC.
  - 22.5% tax.
  - Reinvestment equals revenue growth divided by a sales-to-capital ratio of 2.5, with no credit for shrinkage.
  - Terminal value uses a 20% ROIC.
  - Valuation date October 12, 2026. FY2027 is pro-rated by 0.63, with mid-period discounting.
  - 1,487M diluted shares and an NKE price of $35.35 (`data/valuation/peer_multiples.csv`).
- **Margin anchors** (all my arithmetic):
  - NKE consolidated EBIT margin was 8.3% in FY2026 ($3,850M / $46,398M) and 12.7% in FY2024 ($6,539M / $51,362M) (FY26 and FY24 10-K p. 31).
  - The reverse DCF says today's price needs Nike back to roughly 12% to 14% by FY2031.
- **Jordan-specific cost items that move its margin away from Nike's average** (none disclosed):
  - A royalty to Michael Jordan of about 4% of Jordan revenue (my arithmetic on Forbes and Sportico estimates, secondary).
  - A heavier NIKE Direct mix, estimated at about 50% (`12_jordan_brand_thesis.md` Section 4). It raises gross margin but also operating cost.

## 2. Scenarios

| Scenario | Revenue path FY27 to FY31 (assumption) | FY2031 revenue | vs FY2024 peak | FY2031 EBIT margin (assumption) | Terminal growth | FY2031 EBIT | FY2031 EPS contribution | DCF value | Per NKE share | Share of $35.35 |
|---|---|---|---|---|---|---|---|---|---|---|
| Bear: structural drag | -15%, -8%, 0%, 0%, 0% | $5,501M | -37% | 8% | 1% | $440M | $0.23 | $3.4B | $2.32 | 7% |
| Base: slow repair | -15%, -3%, +5%, +5%, +5% | $6,714M | -23% | 11% | 2.5% | $739M | $0.39 | $5.6B | $3.79 | 11% |
| Bull: FY2018 replay | -15%, +5%, +12%, +12%, +10% | $8,662M | about 0% | 14% | 3% | $1,213M | $0.63 | $8.9B | $5.96 | 17% |

What each scenario represents (assumptions tied to the evidence):
- **Bear.** The holiday 2026 retros trade below retail and the October 2026 retro cut does not restore pricing. Jordan settles at a lower level with margins at today's consolidated level.
- **Base.** Demand stabilizes after the FY2027 cut. Jordan grows with sport categories and new doors (Academy, Famous Footwear), but retro premiums do not return.
- **Bull.** The broad retro cut works the way FY2018 did, a year later than FY2018 did: growth from FY2028 and back to the FY2024 peak by FY2031. FY2019 to FY2024 Jordan growth averaged well above 10% a year (chart 17), so 10% to 12% is within the brand's own history.

Terminal value is 68% to 85% of each DCF value, so the result rests mainly on where Jordan settles, not on the path.

## 3. Sensitivity: value per NKE share

| Revenue path | 6% margin | 8% | 11% | 14% | 17% |
|---|---|---|---|---|---|
| Bear | $1.82 | $2.32 | $3.07 | $3.82 | $4.57 |
| Base | $2.14 | $2.80 | $3.79 | $4.79 | $5.78 |
| Bull | $2.45 | $3.32 | $4.64 | $5.96 | $7.27 |

- **Margin moves Jordan's value more than revenue does.** Going from 8% to 14% margin on the base path adds $1.99 a share. Going from the bear to the bull revenue path at 11% adds $1.57.
- That links Jordan to the full-price question in `12_jordan_brand_thesis.md`. Fewer pairs sold at full price can be worth more than more pairs sold at a discount.

## 4. What this means for the pitch (my inference)

1. **Jordan is a 10% lever on the stock, not a doubling.** The bull-to-bear spread is $3.64 a share, about 10% of the $35.35 price. A Jordan-only thesis cannot carry a large price target; it has to sit inside the wider margin-recovery case.
2. **The market is already paying near the bull case for Jordan.** At NKE's own EV/Sales of about 1.2x (peer_multiples.csv), Jordan's FY2026 revenue is worth $8.4B, or $5.68 a share. That is close to the bull DCF ($5.96), because NKE's multiple already embeds the 12% to 14% margin recovery the reverse DCF found.
   - On these assumptions, Jordan is mainly a **downside risk**: about $1.90 to $3.40 a share if it ends in the base or bear case ($5.68 less $3.79 or $2.32).
   - Upside exists only if Jordan beats the bull case, for example by passing its FY2024 peak or exceeding a 14% margin.
3. **EPS view.** The bull-to-bear spread in Jordan's FY2031 EPS contribution is about $0.40. That is roughly a third of the FY2027 adjusted EPS guidance midpoint of $1.25 (Q1 FY27 release p. 1; midpoint my arithmetic). Jordan matters more for the earnings recovery than for the valuation multiple.
4. **Cross-check.** The median EV/EBIT of seven peers is 8.2x, against 14.6x for NKE (`data/valuation/peer_ev_ebit_20261013.csv`, Yahoo market data, Oct 13, 2026). At the peer median, the base-case FY2031 Jordan EBIT of $739M would be worth about $6.1B before discounting (my arithmetic). That is in line with the base DCF before discounting, so the DCF is not out of line with the market.

## 5. Limits

- **Margins.** Every margin is an assumption. A Jordan EBIT or contribution-margin disclosure at Investor Day (Nov 16 to 17, 2026) would replace them.
- **Revenue paths.** These are scenarios, not forecasts. The bear path's -8% in FY2028 and the bull path's +12% are judgement calls bracketing the evidence.
- **Corporate costs.** No separate allocation is made beyond using consolidated-margin anchors.
- **Share count.** It is held flat at 1,487M.
- **Cost of capital.** The 10% WACC follows the repo's reverse DCF. At 9%, every value rises. The script can be re-run with other inputs.
