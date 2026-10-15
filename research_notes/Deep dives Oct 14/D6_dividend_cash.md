# D6. Dividend, free cash flow, buyback and balance sheet coverage

Prepared 2026-10-14 for the NKE pitch (reference price $35.35, Oct 12 close; $35.30 Oct 14 per Yahoo chart). Model and tables are reproducible: `D6_dividend_cash_model.py` (run `python3 -I D6_dividend_cash_model.py`), `D6_nike_history.csv`, `D6_peer_dividend_cases.csv`, all in this folder.

**Source tags.** OPENED = I read the source in this session (Nike filings from the investors.nike.com mirror, not www.sec.gov). SNIPPET = search summary only. DERIVED = my arithmetic from cited figures. REPO = number taken from an earlier repo note (named), not re-opened here. ASSUMPTION = an input I chose, listed in section 3 so it can be changed. Filing cites use the printed page.

---

## 1. Headline conclusion

**Coverage is comfortable on the balance sheet and thin to negative on earnings and free cash flow. Both statements are true at once, and the pitch should say so.**

| Test | FY2027E (company guide) | FY2028E low case (EPS $1.00) | FY2028E high case (EPS $1.65) |
|---|---|---|---|
| Dividend $1.64 as % of adjusted EPS | 121% to 143% (GAAP, after $0.15 of Pace: 137% to 164%) | 164% | 99% |
| Free cash flow / dividend ($2.45B) | 0.87x to 1.07x at the EPS midpoint (0.60x to 1.33x across the EPS range and working capital cases) | 0.76x (0.56x to 0.97x) | 1.16x (0.95x to 1.36x) |
| Break-even adjusted EPS for FCF = dividend | n/a | $1.39 with flat working capital; $1.73 if working capital drains $0.5B; $1.82 if stock compensation is treated as a cash cost | same |

- **Balance sheet cover is strong.** Cash and short-term investments $8,368M vs debt $7,893M: net cash $475M (Q1 FY27 10-Q p. 3). After repaying both 2027 notes ($2.0B by Mar 27, 2027) $6.4B remains: **10.4 quarters of the dividend with zero operating cash flow, 5.5 quarters if Nike keeps a $3B cash floor**, 6.4 quarters of dividend plus a $1.5B a year buyback (zero floor). No debt matures between Mar 27, 2027 and Mar 27, 2030 (FY26 10-K p. 70). The covenants Nike lists limit asset disposals and secured debt, with no dividend restriction (FY26 10-K p. 46). The dividend is a choice, not a forced event, inside the Nov 1 submission and the Nov 19 finals window.
- **Earnings and FCF cover is not comfortable.** FY2026 FCF was 0.91x the dividend (FY26 10-K p. 58). On the FY2027 guide, FCF cover at the EPS midpoint is about 0.87x to 1.07x (0.66x if working capital drains $1.0B) depending on one number we cannot see in the guide: working capital outside the tariff refund and severance. Q1 FY27 suggests that number is still a drain (section 4).
- **The cut-or-hold decision is worth little in cash.** A 50% cut frees $1.2B a year ($0.82 a share, 2.3% of market cap) and, if spent on buybacks at $35.35, adds about $0.03 to EPS a year. A token 1-cent raise costs $59M a year. A freeze versus that raise saves $0.04 a share. The value is in the signal, not the cash (section 8).
- **Peers that cut or suspended were mostly over-levered or cash-negative; Nike is neither.** Of 8 cutters in section 9, 4 had GAAP debt / (operating income plus D&A) of 4.3x to 11.2x, 2 more (Kraft Heinz, Walgreens) had negative operating income from impairments on $30.8B and $9.1B of debt, 1 (Foot Locker) was about 1.2x, 1 (adidas) was not computed; 6 of 8 had negative EPS or negative FCF. Nike is 1.73x gross (FY26 10-K p. 55, 58, 70) and net cash. The closest Nike analogues in the sample are the holders (Gap, adidas FY2023, Nike FY2020). One cutter (Foot Locker) had near-zero net debt, so leverage is not a complete explanation.
- **Management has put the dividend on the record.** CFO Denton, Q1 FY27 call, Oct 1, 2026 (OPENED transcript, management opinion, not evidence): "Dividend is a very significant priority for us here at NIKE. ... under all scenarios, we have support for maintaining and ultimately growing the dividend over time. So just we can put that to bed with that statement." A cut seven weeks later would reverse a statement made to an analyst who asked about the over-100% payout. This lowers the odds of a cut at the November declaration.

**What this means for the short pitch.** The dividend does not give a forced catalyst. It is a dated test of how long management thinks the trough lasts (Investor Day Nov 16 to 17, "financial algorithm" promised on the same call). The uncovered-dividend fact is real and filing-based; the step from "uncovered" to "cut" is not supported by balance sheet data for at least 4 to 5 years under S&P's own burn estimate.

---

## 2. Dividend vs EPS and FCF, FY2019 to FY2027E (all per-share and $M)

Source: FY24, FY25, FY26 10-K cash flow statements (OPENED, pp. 60, 59, 58); FY2019 to FY2022 from SEC XBRL company facts (DERIVED); full table in `D6_nike_history.csv`.

| FY | DPS declared | Diluted EPS | Payout of EPS | CFO | Capex | FCF | Dividends paid | FCF / dividend | Buybacks | Dividends + buybacks / FCF | Net cash (cash+STI less debt) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2019 | 0.860 | 2.49 | 35% | 5,903 | 1,119 | 4,784 | 1,332 | 3.59x | 4,286 | 1.17x | n/a |
| 2020 | 0.955 | 1.60 | 60% | 2,485 | 1,086 | 1,399 | 1,452 | 0.96x | 3,067 | 3.23x | n/a |
| 2021 | 1.070 | 3.56 | 30% | 6,657 | 695 | 5,962 | 1,638 | 3.64x | 608 | 0.38x | n/a |
| 2022 | 1.190 | 3.75 | 32% | 5,188 | 758 | 4,430 | 1,837 | 2.41x | 4,014 | 1.32x | n/a |
| 2023 | 1.325 | 3.23 | 41% | 5,841 | 969 | 4,872 | 2,012 | 2.42x | 5,480 | 1.54x | 1,742 |
| 2024 | 1.450 | 3.73 | 39% | 7,429 | 812 | 6,617 | 2,169 | 3.05x | 4,250 | 0.97x | 2,673 |
| 2025 | 1.570 | 2.16 | 73% | 3,698 | 430 | 3,268 | 2,300 | 1.42x | 2,985 | 1.62x | 1,185 |
| 2026 | 1.630 | 2.10 | 78% | 2,868 | 684 | 2,184 | 2,407 | 0.91x | 146 | 1.17x | 1,085 |
| Q1 FY27 | 0.410 | 0.48 | 85% | 135 | 199 | -64 | 610 | negative | 0 | 1.00x | 475 |

Net cash: FY23 cash $7,441M + STI $3,234M less debt $8,927M + notes payable $6M; FY24, FY25, FY26 from the balance sheets (FY24 10-K p. 59, FY25 10-K p. 58, FY26 10-K p. 57); Aug 31, 2026 from Q1 FY27 10-Q p. 3. FY2027E and FY2028E are in sections 5 and 6.

Facts that follow from the table (DERIVED):
- **FY23 to FY26 cumulative:** FCF $16,941M; dividends $8,888M; buybacks $12,861M; returned $21,749M; gap $4,808M. Cash plus short-term investments fell $1,648M ($10,675M to $9,027M) and net cash fell $657M ($1,742M to $1,085M), after $1,000M of debt was repaid and with $2,223M of option exercise proceeds as an offset.
- **Dividend per share rose 12.4% FY24 to FY26 ($1.45 to $1.63) while EPS fell 43.7% ($3.73 to $2.10).** At a constant $1.45, FY26 payout would be 69% vs 78%, so dividend growth explains 9 points of the 39-point payout rise from FY24; the rest is earnings.
- **Nike has been here once before.** FY2020 FCF was 0.96x the dividend (104% of FCF) and the board raised the dividend 12% the next year (0.955 to 1.07). The rebound in FY21 FCF to 3.64x the dividend is why that raise was affordable.
- **Option exercise proceeds are a source both advocate notes omit.** They were $651M, $667M, $551M, $354M in FY23 to FY26 (10-K cash flow statements). Including them, FY26 cover is 1.05x, not 0.91x. They have stopped: Q1 FY27 proceeds were $0 vs $127M in Q1 FY26 (Q1 FY27 10-Q p. 4), consistent with a stock price below most exercise prices. The lost source is about $0.35B to $0.55B a year, or 0.15x to 0.25x of the dividend.

---

## 3. FY2027E build (company guide) and every assumption

**Filing inputs (OPENED).** Q1 FY27 release and 10-Q: revenue to decline high-single digits; effective tax rate mid-20 percent; adjusted diluted EPS $1.15 to $1.35 excluding about $0.15 of Pace charges (Q1 FY27 release p. 1, text confirmed in the investors.nike.com release 575). Pace: about $1.0B of pre-tax charges through FY31 in addition to about $0.3B recognized in FY26; about $0.3B in FY27; "majority" cash; about $2.5B cumulative savings through FY31, "majority of the program savings" in FY29 and FY30 per the CFO (8-K Oct 1, 2026 Item 2.05; 10-Q p. 17 to 18; transcript). Q1 FY27 dividends declared $613M, run-rate $2,452M (10-Q p. 5). Diluted shares 1,484.2M (10-Q p. 1).

**ASSUMPTIONS (change these in the script):**

| Input | Value | Basis |
|---|---|---|
| Diluted shares FY27 / FY28 | 1,485M / 1,490M | Q1 FY27 diluted count, +0.3% dilution |
| Non-cash add-backs (D&A + SBC) | $1,404M | Q1 FY27 run-rate x4: D&A $193M, SBC $158M (10-Q p. 4). FY26 was $747M + $715M. Deferred tax assumed 0 (FY24 to FY26: -$497M, -$288M, -$96M; each further -$100M costs 0.04x) |
| Capex | $796M | Q1 FY27 $199M x4; FY26 $684M, FY24 $812M. Non-cash PP&E additions were $225M in Q1 vs $101M, so cash capex may lag |
| IEEPA refund, net cash in FY27 | +$457M | $684M receivable collected "substantially all" (10-K p. 30) less tax at 23% on the $986M benefit. Q1 shows the matching receivable fall $695M and tax payable fall $199M (10-Q p. 4) |
| Pace cash drag vs adjusted net income | -$300M after tax | FY26 severance accrual $243M paid in Q1 (10-Q p. 17) plus about half of the $300M FY27 charge paid in year, after tax at 23%. Range -$190M to -$420M |
| Other working capital (not IEEPA, not Pace) | -$1,000M / -$500M / 0 / +$500M | Section 4 explains why this is the swing factor |

**FY2027E FCF and coverage** (DERIVED, dividend $2,452M):

| Adjusted EPS | Adj. net income | FCF, other WC -$1.0B | -$0.5B | 0 | +$0.5B |
|---|---|---|---|---|---|
| $1.15 | 1,708 | 1,473 (0.60x) | 1,973 (0.80x) | 2,473 (1.01x) | 2,973 (1.21x) |
| $1.25 | 1,856 | 1,621 (0.66x) | 2,121 (0.87x) | 2,621 (1.07x) | 3,121 (1.27x) |
| $1.35 | 2,005 | 1,770 (0.72x) | 2,270 (0.93x) | 2,770 (1.13x) | 3,270 (1.33x) |

Payout of adjusted EPS 143%, 131%, 121%; of GAAP EPS (adjusted less $0.15 Pace) 164%, 149%, 137%.

Cross-check against an independent estimate: S&P projects "an annual cash burn of about $1.2 billion after dividend payments" over the next two to three years (Tradingpedia, Oct 5, 2026, OPENED via fetch; S&P's own report not opened). That implies FCF of about $1.25B a year on S&P's adjusted basis, which is at the low end of the grid above (0.51x). S&P also "expects Nike to pause share repurchase programs, trim capital expenditures" and use cash to repay debt maturing through early 2027.

---

## 4. Why FCF fell, and what the FY2027 working capital question really is

**FY24 to FY26 CFO fell $4,561M** (FY26 10-K p. 58; DERIVED):

| Driver | $M | Share of CFO decline |
|---|---|---|
| Net income ($5,700M to $3,108M) | -2,592 | 57% |
| Non-cash items ($1,013M to $1,438M) | +425 | -9% |
| Working capital and other ($716M to -$1,678M) | -2,394 | 52% |

Profit bridge FY24 to FY26 (income statement, 10-K p. 55): gross profit -$2,976M, of which revenue volume at the FY24 gross margin of 44.56% is -$2,212M and gross margin rate (44.56% to 42.91%) is -$764M; selling and administrative expense +$462M (lower); net interest income -$111M ($161M to $50M); other income -$175M. Pre-tax income $6,700M to $3,900M; FY26 includes the $986M tariff refund benefit, so underlying FY26 pre-tax was $2,914M.

**EPS bridge FY24 to FY27E midpoint** (DERIVED; FY27E pre-tax = adjusted net income $1,856M / 0.75 = $2,475M):
- FY24 $3.73 (pre-tax $6,700M, tax rate 14.9%, 1,529.7M shares).
- Pre-tax income to $2,475M at the FY24 tax rate and share count: -$2.35.
- Tax rate 14.9% to a mid-20s guide (25% assumed): -$0.16.
- Share count 1,529.7M to 1,485M: +$0.04.
- FY27E adjusted midpoint $1.25.

**Alternatives for "why coverage is below 1.0x" and how each was tested:**

| Explanation | Test | Result |
|---|---|---|
| Dividend raised too fast | Hold DPS at FY24 $1.45: FY27E payout would be 116% vs 131% | Explains 15 of 131 points. Ruled out as the main cause |
| Capex too high | Capex $684M FY26 vs $812M FY24 and $969M FY23 | Ruled out; capex fell |
| Buybacks draining cash | Buybacks $146M FY26, $0 Q1 FY27 | Ruled out; repurchases paused since Q1 FY26 (10-K p. 45) |
| Interest burden | Net interest was income of $50M in FY26; coupons $251M vs EBIT $3,850M (15.3x) | Ruled out |
| Tax | ETR 14.9% to guide mid-20s costs $0.16 of EPS; cash taxes paid were $1,299M, $1,226M, $1,270M in FY24 to FY26, i.e. $299M to $560M above book tax (10-K p. 71 and note 7) | Real but second-order: about 7% of the EPS decline |
| Tariff refund timing | $684M receivable at May 31 collected in Q1 FY27 | Real. It lifted FY27 cash and depressed FY26 cash. Explains $684M of the $1,678M FY26 working capital drain (41%) |
| Earnings fell | Net income -$2,592M FY24 to FY26 | The largest single driver. Gross profit volume effect -$2,212M is the core |
| Working capital outside the refund | FY26 WC -$1,678M; ex refund receivable ex severance accrual +$243M: about -$1,237M. FY25 WC -$787M, FY24 +$716M | **Survives.** Not caused by any single disclosed item. Accounts receivable +$1,207M (of which $684M refund), payables and accruals -$959M, income taxes payable -$292M (federal payments, 10-K p. 45) |

**Q1 FY27 read-through (DERIVED):** reported FCF was -$64M (CFO $135M less capex $199M). Removing the estimated net refund inflow (+$457M) gives about -$521M; also removing the $243M severance paid gives about -$278M. Other working capital in Q1 (ex refund, ex severance) was about -$1,060M, against a total working capital outflow of -$897M in Q1 FY26 (10-Q p. 4). Q1 is seasonally a working capital outflow (bonus payments, inventory build), so a Q1 comparison is the only clean like-for-like: other working capital was about $0.16B worse than a year ago. It was not yet releasing cash even though revenue fell 4.3% (10-Q p. 1).

**Honest read.** The red team's argument that working capital will reverse as revenue shrinks is plausible but is not in the Q1 data. The advocate's argument that coverage is structurally below 1.0x is also not proven. What the data support: coverage is within 0.6x to 1.1x for FY27 and the outcome depends on a line the guide does not give. The most useful single item for the November Investor Day is a full-year FY27 cash flow or working capital guide.

---

## 5. FY2028E: the D1-style lower case (EPS $1.00 to $1.65)

Treated as adjusted EPS (excluding Pace). Shares 1,490M. Pace cash drag after tax $230M (remaining about $0.7B of charges over FY28 to FY31 plus a spill of FY27 accruals). Capex $796M. Dividend $2,452M (no raise).

| FY28 adj. EPS | Adj. NI | Payout | FCF, WC 0 | Cover | FCF, WC -$0.5B | Cover | FCF, WC +$0.5B | Cover |
|---|---|---|---|---|---|---|---|---|
| $1.00 | 1,490 | 164% | 1,868 | 0.76x | 1,368 | 0.56x | 2,368 | 0.97x |
| $1.15 | 1,713 | 143% | 2,092 | 0.85x | 1,592 | 0.65x | 2,592 | 1.06x |
| $1.25 | 1,862 | 131% | 2,240 | 0.91x | 1,740 | 0.71x | 2,740 | 1.12x |
| $1.40 | 2,086 | 117% | 2,464 | 1.00x | 1,964 | 0.80x | 2,964 | 1.21x |
| $1.50 | 2,235 | 109% | 2,613 | 1.07x | 2,113 | 0.86x | 3,113 | 1.27x |
| $1.65 (consensus) | 2,458 | 99% | 2,836 | 1.16x | 2,336 | 0.95x | 3,336 | 1.36x |

- **Break-even EPS** where FCF equals the dividend: **$1.39** (flat working capital), $1.73 (working capital -$0.5B), $1.82 (counting stock compensation as a cash cost, which it is economically because buybacks or dilution must absorb it). Each $0.10 of EPS is $149M of net income, about $199M of pre-tax income (at 25% tax).
- **Sensitivity on the thesis:** at the FY24 EBIT margin of 12.7% (FY24 10-K, EBIT $6,539M over revenue $51,362M), FY27E revenue of $42.7B (FY26 $46,398M less 8%) would produce EBIT of about $5.4B vs adjusted FY27E pre-tax of about $2.5B. That gap is about $2.9B pre-tax, or about $2.2B after tax at 25%, which is the size of the $2.45B dividend: the dividend is uncovered because earnings sit at roughly 6% EBIT margin instead of 12.7%.
- **Pace savings** are back-end loaded (CFO: majority in FY29 and FY30), so FY28 carries charges and little saving. This is the main reason FY28 low-case cover does not improve on FY27.
- Consensus FY28 EPS $1.646, FY27 $1.288 (REPO consensus_and_valuation note; Yahoo; not re-opened). At $1.646 FY28 cover is 1.16x with flat working capital: this compares with 1.04x in the REPO note 18 base case.

---

## 6. Debt maturities, interest, leases and tax (balance sheet detail)

**Debt (FY26 10-K p. 70, OPENED).** Principal $8,000M (sum of Note 6 principal, DERIVED), book $7,942M, fair value about $6.8B.

| Maturity | Principal | Coupon |
|---|---|---|
| Nov 1, 2026 | $1,000M | 2.38% |
| Mar 27, 2027 | $1,000M | 2.75% |
| Mar 27, 2030 | $1,500M | 2.85% |
| 2040 to 2050 (five notes) | $4,500M | 3.25% to 3.88% |

- Scheduled maturity by fiscal year: FY27 $2.0B, FY28 $0, FY29 $0, FY30 $1.5B, FY31 $0 (p. 70).
- Liquidity: $1B 364-day facility (matures Mar 5, 2027, undrawn), $2B five-year facility (Mar 7, 2030, undrawn), $3B commercial paper program unused; S&P cites "sizable liquidity buffer, totaling $11.4 billion" (Tradingpedia; $8.4B cash plus $3.0B facilities, DERIVED). Rating changes "would not trigger acceleration" (10-K p. 46).
- **Nov 1, 2026 note: repaid or refinanced?** Not known as of Oct 14. Routes tried: (1) investors.nike.com all-SEC-filings list through Oct 5: filings are Form 144, 10-Q, 8-K Oct 1, Form 4, 8-K Sep 16, no 424B or S-3 (OPENED); (2) investors.nike.com press release list: latest items are Q1 results (575), board appointment (574), dividend declaration (572); no debt news; (3) web search for a Nike offering or redemption: none found (SNIPPET); (4) S&P text "expects Nike to use existing cash to repay debt maturing through early 2027" (Tradingpedia, OPENED); (5) the 10-Q p. 36 contains no refinancing statement. Status: no issuance signal, repayment from cash is the base expectation per S&P. The payment date (Nov 1 is a Sunday, DERIVED) settles after the Nov 1 submission.

**Interest (DERIVED):**
- Coupon run-rate $251M a year (sum of principal x coupon from the table above); average coupon 3.14%. Cash interest paid was $323M in FY26, $389M in FY25, $381M in FY24 (cash flow statements; the excess over coupons is mostly swap settlements on $2.4B of floating-pay swaps, 10-K p. 70).
- Interest income: portfolio income $278M in FY26 (10-K p. 68), a 3.06% yield on average cash and STI of $9.1B. Net result was net interest income of $50M (income statement). FY27 Q1 net interest income was $14M.
- Refinancing $2.0B at about 5.49% (indicative secondary-market yield on the 2030 notes, REPO note 18, not re-opened) instead of repaying at the 2.56% average coupon: +$59M pre-tax, $0.03 of EPS. Repaying from cash costs $61M of lost interest income at 3.06% and saves $51M of coupons: roughly neutral (-$10M).
- EBIT / coupons: FY26 15.3x ($3,850M / $251M). Interest is not a coverage problem.

**Leases (FY26 10-K p. 88 to 89, OPENED).** Operating lease liabilities $3,091M at May 31, 2026 ($3,179M at Aug 31, 2026, 10-Q p. 3); undiscounted payments $564M in FY27, $553M FY28, $512M FY29, $456M FY30, $361M FY31, $1,146M thereafter; operating cash paid for leases $668M in FY26. Lease cash is already inside CFO. EBITDAR FY26 $5,290M (EBIT $3,850M + D&A $747M + lease cost $693M). Debt plus leases / EBITDAR 2.09x, which matches the CFO's "leverage at roughly 2x" (transcript). Net of cash: 0.38x. Net debt including leases was $2.7B at Aug 31, 2026 (debt $7,893M + leases $3,179M - cash and STI $8,368M).

**Other cash requirements that compete with the dividend (10-K p. 46):** endorsement contracts $15.5B total, $1.7B within 12 months; product purchase obligations $4.9B ($4.7B within 12 months); other purchase obligations $2.4B ($1.6B within 12 months); bank guarantees and letters of credit $1.3B (up from $0.9B; p. 88). Supplier finance programs $1.1B inside accounts payable (10-Q p. 18): if suppliers or banks tightened terms after the rating cut, that $1.1B would convert to cash outflow. This is an unquantified tail, not a base case.

**Tax.** FY27 guide mid-20 percent ETR vs 14.9% in FY24 and 20.3% in FY26 (Q1 FY27 release; 10-K p. 32). Q1 FY27 ETR 22.7% because of foreign tax audit settlements. Cash taxes paid exceeded book tax by $299M (FY24), $560M (FY25), $478M (FY26): taxes payable fell from $669M to $377M in FY26 on federal payments (10-K p. 45).

---

## 7. How many quarters of cash cover dividend plus buybacks

Cash and short-term investments $8,368M less $2,000M of notes due by Mar 27, 2027 = $6,368M available. Quarterly dividend $613M. Buyback authorization remaining about $5.9B (10-K p. 45); repurchases are paused and "funding of any future share repurchases to come from operating cash flows" (10-K p. 45). Quarters of outflow covered with zero operating cash flow (DERIVED):

| Minimum cash kept | Dividend only | Dividend + $1.5B/yr buyback | Dividend + $3.0B/yr buyback (FY25 pace: $2,985M) |
|---|---|---|---|
| $0 | 10.4 | 6.4 | 4.7 |
| $3,000M | 5.5 | 3.4 | 2.5 |
| $4,000M | 3.9 | 2.4 | 1.7 |

(Nike does not disclose a minimum operating cash level or the split of cash held outside the US in the pages read. The $3B and $4B floors are assumptions.)

With operating cash flow included, the math is far longer: at S&P's $1.2B annual burn after dividends the $6.4B lasts 5.3 years (2.0 years above a $4B floor); at the FY28 $1.00 EPS case the annual dividend shortfall is $584M and $6.4B lasts 10.9 years; at the FY28 $1.25 case the shortfall is $212M. **A buyback restart on top of the dividend is the item the balance sheet cannot support at the FY25 pace** (4.7 quarters before any floor), which matches S&P's expectation that buybacks stay paused. The dividend alone is supportable for a multi-year trough.

---

## 8. What a dividend freeze or cut is worth (DERIVED)

Share count 1,483M (Class A 281M + Class B 1,202M, 10-Q p. 3); market cap at $35.35 = $52.4B.

| Action (annual DPS) | Cash retained a year vs $1.64 | Per share | Yield at $35.35 | % of market cap |
|---|---|---|---|---|
| Token raise to $1.68 (+$0.01 a quarter) | -$59M | -$0.04 | 4.8% | -0.11% |
| Freeze at $1.64 | 0 | 0 | 4.6% | 0 |
| Cut 25% to $1.23 | +$608M | +$0.41 | 3.5% | 1.16% |
| Cut 50% to $0.82 | +$1,216M | +$0.82 | 2.3% | 2.32% |
| Suspend | +$2,432M | +$1.64 | 0.0% | 4.64% |

- **A freeze is worth almost nothing in cash.** It avoids a $59M a year (0.11% of market cap) raise. Its value is the Dividend Aristocrat question: a 25th consecutive annual raise would make Nike eligible (REPO advocate note; articles OPENED there); I did not re-verify index rules.
- **A 50% cut: $1.2B a year** covers the full FY28 $1.00-EPS FCF shortfall ($584M) with $632M to spare, and ends the S&P burn (cash burn after dividends of $1.2B becomes about zero). If the saved cash buys stock at $35.35, 34.8M shares (2.35%) are retired a year: EPS +$0.03 on a $1.25 base. If it repays the 2027 notes instead of refinancing, the pre-tax saving is about $49M. Neither is large against $1.25 of EPS.
- **Equity value is neutral in theory:** cash kept inside the company is the same dollars the owners would have received. A cut changes value only through (a) credit cost, (b) the return earned on retained cash vs what owners could earn, (c) signalling about the length of the trough, and (d) holder turnover. Items (a) and (b) are under $0.05 of EPS a year (from the figures above). Items (c) and (d) are the whole story, and are measured in section 9.
- **Swoosh, LLC** (221.75M Class A shares, REPO note 18 from the 2026 proxy) collects 221.75M x $1.64 = $364M a year (DERIVED). It holds control of three-quarters of the board, so its incentive favours continuity. Not re-verified here.

---

## 9. Peer cases: dividend actions in margin troughs

Data: SEC XBRL company facts (annual 10-K values, DERIVED), Yahoo dividend events and daily closes (market data, DERIVED), action dates from web search (SNIPPET unless stated), adidas annual report pages (OPENED via fetch). Full table in `D6_peer_dividend_cases.csv`. "EBITDA proxy" = GAAP operating income + D&A, which understates EBITDA where impairments are large (n.m. where operating income is negative). This is a hand-picked set of well-known cases, not a screen, so it **cannot give a base rate** (see limits below).

| Company | Last full year before action | FCF / dividend | GAAP EPS / DPS | Gross debt / EBITDA proxy | Action |
|---|---|---|---|---|---|
| Estee Lauder | FY24 (Jun 2024) | 1.52x (FY23: 0.79x) | $1.08 / $2.64 (244%) | 4.3x | Rate flat at $0.66 for 8 payments (Nov 2022 to Aug 2024), then cut 47% to $0.35 on Oct 31, 2024 |
| V.F. Corp | FY23 (Apr 2023) | negative (FY22: 0.80x) | $0.31 / $1.81 (584%) | 11.2x | Cut 41% Feb 2023; cut 70% to $0.09 Nov 2023 |
| Kraft Heinz | 2018 | 0.55x | -$8.36 / $2.50 | n.m. | Cut 36% to $0.40 on Feb 21, 2019; flat since (7 years) |
| Walgreens | FY23 (Aug 2023) | 0.09x | -$3.57 / $1.92 | n.m. | Cut about 48% Jan 2024; suspended Jan 30, 2025 |
| Foot Locker | FY23 (Feb 2024) | negative | -$3.51 / $1.20 | 1.2x (cash $297M vs debt $395M) | Suspended 2023 (Aug 2023 per SNIPPET); not resumed in 2024 |
| Hanesbrands | 2022 | negative | -$0.36 / $0.60 | 6.2x | Eliminated Jan 2023; debt target 2x to 3x |
| Newell Brands | 2022 | negative | $0.47 / $0.92 (196%) | 8.8x | $0.92 flat 2018 to 2022; cut 70% from May 2023 |
| adidas | 2022 (EUR) | n.a. | EUR 1.25 / 3.30 | n.a. | Proposed 3.30 to 0.70 (-79%) at 49% of net income against a 30% to 50% policy; held 0.70 for FY2023 with EPS -0.67; paid 2.00 and 2.80 for FY2024 and FY2025 (Yahoo ex-dates 2025-05-16, 2026-05-08) |
| Gap Inc (held) | FY22 (Jan 2023) | negative (FY23: 5.0x) | -$0.55 / $0.60 | n.m. | Held $0.15 a quarter Apr 2022 to Jan 2025; FY23 FCF $1,112M, EPS $1.34; raised in 2025 |
| Nike FY2020 (own, held) | FY20 | 0.96x | $1.60 / $0.955 | n.a. | Raised 12% in FY2021 |

**What the sample shows (DERIVED, with the sample's selection bias stated):**
- **Of 8 cutters or suspenders, 6 had negative GAAP EPS or negative FCF in the year before the action (Kraft Heinz, Walgreens, Foot Locker, Hanesbrands: negative EPS; V.F., Newell: negative FCF); Nike has neither in FY26.** Nike's FY26 EPS is $2.10 and FY27 GAAP EPS is $1.00 to $1.20 (guide). The exception is Estee Lauder: positive EPS and FCF cover of 1.5x, but a GAAP payout of 244% and 4.3x leverage.
- **Nike's FCF cover (0.91x FY26, 0.87x to 1.07x FY27E at the EPS midpoint) is better than every cutter except Estee Lauder's FY24, and similar to Estee Lauder's FY23 (0.79x)**, which was followed by seven more quarters of a flat dividend and then a cut. A frozen dividend is not a stable end state if EPS keeps falling: Estee Lauder's EPS went $2.79 (FY23), $1.08 (FY24), -$3.15 (FY25).
- **The stated reason for 5 of 8 actions was deleveraging or cash rebuilding per search summaries** (Kraft Heinz, V.F., Hanesbrands, Walgreens, Foot Locker "cash rebuilding year"); adidas was a policy-range reset; Estee Lauder and Newell reasons not verified. Nike has no debt target to fix: net cash, debt / EBITDA 1.73x.
- **Holders, Gap and adidas FY2023, held through a loss year and then recovered within 4 to 8 quarters.** Gap FCF was -$78M with EPS -$0.55 in FY22 and the dividend was held; EPS recovered to $1.34 the next year; Gap shares rose 50% from Mar 2, 2023 to Mar 4, 2024 (Yahoo closes, DERIVED). This is the template for a freeze that works: it requires an earnings recovery inside about a year. Nike's recovery is FY28 consensus, 5 to 6 quarters after the FY27 trough on the guide.

**Day and 12-month price reactions** (Yahoo closes, return from the prior close; SPY in brackets; the dividend effect is confounded because the news came with other items):

| Event | Date | 1 day | 63 days | 126 days | 252 days | What else was announced |
|---|---|---|---|---|---|---|
| Estee Lauder cut | 2024-10-31 | -23.6% (SPY -1.5%) | -20.3% (+3.8%) | -32.8% (-3.7%) | +6.6% (+16.4%) | Guidance withdrawn, restructuring |
| Kraft Heinz cut | 2019-02-22 (day after the Feb 21 after-close release) | -29.0% (+0.8%) | -34.7% (+1.7%) | -46.8% (+5.4%) | -44.7% (+16.2%) | $15.4B impairment, SEC inquiry |
| V.F. cut 1 | 2023-02-02 | -3.2% (+0.4%) | -33.7% (-1.4%) | -38.7% (+8.8%) | -47.8% (+19.9%) | Q3 results (announcement time not verified) |
| V.F. cut 2 | 2023-11-03 | +7.7% (+1.1%) | +14.4% (+14.7%) | -14.4% (+20.1%) | +44.4% (+33.9%) | Q2 results; date per dividendhistory.org (10-K says declared Oct 24) |
| adidas cut proposal | 2023-03-01 | +0.9% (+0.4%) | +6.4% (+6.5%) | +28.1% (+13.3%) | +32.9% (+27.7%) | FY22 results; EUR price vs USD SPY |

The two largest drops (Estee Lauder, Kraft Heinz) coincided with guidance withdrawal or impairments; the pre-announced or policy-based cuts (V.F. second, adidas) moved the stock by under 8% on the day. A cut that is a surprise and comes with an earnings reset is a -20% to -30% day; a cut that is telegraphed does not. Nike's potential cut would follow a guided-down year and an explicit management statement of support, so it would be a surprise on the dividend line but not on earnings, and no cleanly comparable case exists in the sample.

**Limits and what would settle them.** (1) The sample is not random: it contains known cutters plus two holders, so the "5 of 8 stated deleveraging" figure does not translate into a probability of a Nike cut. The data that would settle this is a screen of all US consumer discretionary and staples dividend payers with EPS down more than 50% over two years and payout above 100% on a company-guided year, with the outcome (cut, hold, raise) over the next 8 quarters, from Compustat or a Refinitiv pull (the repo has a Refinitiv pull list). (2) Day reactions are confounded by same-day news and cannot isolate the dividend effect with this data.

---

## 10. Alternatives ruled out and what survives

| # | Claim | Test | Verdict |
|---|---|---|---|
| 1 | "Nike cannot afford the dividend" | Net cash $475M, $6.4B after 2027 notes, 10.4 quarters of dividend with no operating cash flow, 5.3 years at S&P's burn, no covenant or maturity wall to 2030 | **Ruled out** for at least FY27 to FY29. A cut would be a choice |
| 2 | "Nike will not cut because the dividend is a priority" | CFO statement is opinion; I did not check whether the cutters made similar statements before cutting, which is a gap | **Survives as a probability reducer, not proof.** Treat as management opinion |
| 3 | "FY26 0.91x is a timing artefact" | Refund receivable explains 41% of the working capital drain; FY27 Q1 still shows about -$1.06B of other working capital | **Partly true.** Refund timing real; the rest remains |
| 4 | "FY27 cover is structurally under 1.0x" | Grid 0.60x to 1.13x; central depends on other working capital | **Not proven either way.** Needs a working capital guide (Investor Day) |
| 5 | "Payout above every precedent" | GAAP payout: Nike FY27E 137% to 164%; V.F. 584%, Estee Lauder 244%, Newell 196%; five peers had negative EPS | **Ruled out on a GAAP basis.** On adjusted EPS the REPO note 18 range (48% to 102%) puts Nike (121% to 143%) above it; I could not reproduce those adjusted bases, so use only with that label |
| 6 | "Stock compensation is non-cash, so FCF understates cover" | SBC $715M FY26 is 33% of FCF; break-even EPS rises from $1.39 to $1.82 if SBC is a cash cost | **Ruled out as a reason for comfort.** The advocate and red team used SBC inconsistently; here both treatments are shown |
| 7 | "A cut creates value" | A 50% cut retains $1.2B; EPS +$0.03 via buybacks; interest effect under $0.05 | **Cash value small; signal large.** Neither side has data separating the signal effect from same-day news |
| 8 | "Interest costs threaten coverage" | EBIT / coupon 15.3x; refinancing costs $0.03 of EPS | **Ruled out** |
| 9 | "Tariff refund proves earnings are higher than they look" | Ex-refund FY26 EPS $1.58 (REPO from Q4 FY26 release); FY27E midpoint $1.25 | Refund inflated FY26 EPS by $0.52 and was non-recurring; it does not support FY27 cover |

**Explanations that still survive and cannot be separated with filings:** (a) working capital in FY27 and FY28 is a drain because suppliers, tax payments and accruals are normalising, vs (b) it releases as revenue and purchases fall. Data that would decide it: the Q2 FY27 balance sheet (about Dec 17), any Investor Day cash flow guide, and Feng Tay and Pou Chen monthly revenue as a read of purchase volumes (the scoreboard already has these; Oct data about Nov 10).

---

## 11. Corrections to the Thesis decision notes (this task checked them)

1. The advocate's "alternatives" and red team agree on 0.91x. The red team's 1.28x to 1.60x "pre working capital" figures require working capital to be neutral. Q1 FY27 other working capital was about $0.16B worse than Q1 FY26, so neutral is not yet visible.
2. The red team wrote the CFO said the dividend "remains a priority" (TIKR paraphrase). The transcript is stronger: "under all scenarios, we have support for maintaining and ultimately growing the dividend over time" (OPENED, Q1 FY27 transcript, Q&A at the end of the call). Use the transcript.
3. Estee Lauder's cut was Oct 31, 2024 from $0.66 to $0.35, after the rate had been flat for 8 payments. It was not in 2025 and not from $0.70 (web search correction, confirmed by Yahoo ex-dates and XBRL FY25 DPS of $1.71 = 0.66 + 3 x 0.35). Any prior mention of a different date or rate should be fixed.
4. S&P's "$1.2B annual cash burn" is explicitly "after dividend payments" (Tradingpedia, OPENED). Both notes cite it correctly in direction; it implies S&P FCF of about $1.25B, below this note's central FY27E and FY28E cases.
5. The Q4 FY26 dividend declaration releases (May 4 and Aug 6, 2026) do not contain the "consecutive years of increasing dividend payouts" phrase (OPENED, releases 565 and 572). This is consistent with the advocate's observation that the streak language was dropped, but the releases are one-paragraph notices that may never have carried it; the earlier-quarter comparison in REPO note 18 was based on the earnings releases. I did not re-run that comparison.
6. Nike's next declaration: the last three were May 4, Aug 6 (Q1 FY27) and Nov 20, 2025 (REPO). Payable Oct 1, 2026 record Sept 1 (OPENED). The Nov 2026 declaration date is not announced.

---

## 12. Route log (routes tried and results)

| Fact sought | Route | Result |
|---|---|---|
| FY24 to FY27 cash flow, debt, leases, tax | investors.nike.com mirror: FY24, FY25, FY26 10-K, Q1 FY27 10-Q, 8-K Oct 1 (converted with `scripts/sec_pipeline/topages.py`) | Worked (OPENED) |
| FY27 guide wording, dividend statement | Nike release 575 and official Q1 FY27 transcript PDF (q4cdn) | Worked (OPENED) |
| FY2019 to FY2022 history | SEC XBRL company facts (data.sec.gov; User-Agent contained no email) | Worked (DERIVED); FY2019 to FY2022 EPS from facts file |
| S&P rating text and "after dividends" qualifier | Tradingpedia (OPENED), capital.com and Newsquawk (headline only), 10-K/10-Q rating statements (still A+/A2 on Oct 2 filing, before the Oct 5 action) | Partial: S&P report itself is paywalled and not opened. Four routes tried |
| Nov 1, 2026 note repay or refinance | EDGAR index via investors.nike.com, IR press releases, web search, S&P commentary, 10-Q text | No issuance found; repayment from cash is S&P's expectation. Not settled; five routes tried; settles on or about Nov 2, 2026 |
| Peer dividend actions and dates | XBRL, Yahoo dividend events, web search, adidas annual report pages | Worked for amounts; dates SNIPPET for V.F., Kraft Heinz, Walgreens, Foot Locker, Hanesbrands; Newell announcement date and Foot Locker exact date not verified |
| Peer price reactions | Yahoo daily closes | Worked for Estee Lauder, V.F., Kraft Heinz, adidas, Gap; Walgreens, Hanesbrands, Foot Locker no longer listed, 404 |
| Minimum operating cash / offshore cash | 10-K liquidity text | Not disclosed by Nike; floors in section 7 are assumptions |
| Base rate of cut vs hold | No systematic dataset in the repo | Not computed; section 9 states what data would settle it |
| Option-implied dividend (REPO note 17) | Not re-run | REPO only |

No email address was used in any request.

## 13. Sources

- OPENED: Nike FY26 10-K (p. 29 to 30, 45 to 46, 55 to 59, 69 to 71, 88 to 89); FY25 10-K (balance sheet p. 58, cash flow p. 59); FY24 10-K (balance sheet p. 59, cash flow p. 60); Q1 FY27 10-Q (p. 1, 3 to 5, 17 to 18, 33 to 34); 8-K filed Oct 1, 2026 (Items 2.02 and 2.05); Q1 FY27 earnings release (investors.nike.com release 575); dividend declaration releases 565 (May 4, 2026) and 572 (Aug 6, 2026); Q1 FY27 official transcript (s1.q4cdn.com ... NIKE-Inc-Q1FY27-OFFICIAL-Transcript_-FINAL.pdf); Tradingpedia Oct 5, 2026; adidas Annual Report 2022 and 2023 "our share" pages.
- DERIVED from data: SEC XBRL company facts for Nike, Estee Lauder, V.F., Kraft Heinz, Walgreens, Foot Locker, Hanesbrands, Gap, Newell; Yahoo chart data for dividends and closes (EL, VFC, KHC, NWL, ADS.DE, GAP, SPY, NKE).
- SNIPPET: web search summaries for V.F., Estee Lauder, Kraft Heinz, Walgreens, Hanesbrands, Foot Locker, S&P action, Nike bond.
- REPO: `Thesis decision/advocate_short_cash_dividend.md` (including notes 17 to 21 cited there), `01_ruling.md`, `Long or short cruxes/00_SCOREBOARD.md`, `data/nke_daily_prices.csv`, `data/nke_dividends_exdate.csv`.
