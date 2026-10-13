# AB: Nike capital allocation, dividend and balance-sheet risk (as of Oct 13, 2026)

Scope: cash flow, dividend, debt, ratings, buybacks, a forward cash model and dividend-cut precedents. Other sessions own root causes, channels, China, Jordan, discounting, tariffs and product, so those topics are not covered here. Filing figures cite the filing and printed page. Earnings releases are paged from the first page of Exhibit 99.1. Labels: *market data* (Yahoo Finance chart API, downloaded Oct 13, 2026), *secondary* (an opened news or aggregator page), *my arithmetic*, *my inference*, *my judgment*. USD millions unless noted.

Supporting CSVs are in `data/capital/`:
- `cashflow_fy2019_q1fy2027.csv`: CFO, capex, FCF, dividends, buybacks, working-capital lines, SBC, restructuring cash, interest paid
- `dividend_history.csv`: DPS, EPS, payout of EPS and of FCF, raise dates and sizes, the streak
- `debt_schedule.csv`: each note, the revolvers, CP, and indicative yields (secondary)
- `ratings_history.csv`
- `buyback_and_shares.csv`
- `forward_model.csv`: base, stress (refinance), and stress with debt repaid from cash, FY2027 to FY2029 plus FY2030 and FY2031 extrapolations
- `forward_model_severe_sp_burn.csv`
- `precedents_market.csv`: Yahoo-computed reactions
- `precedents_summary.csv`

Scripts are in `scripts/capital/` (`fwd.py`, `tables.py`, `prec.py`). Raw downloads (Yahoo prices, Nike IR dividend releases, bond quotes) are not committed; the scripts list their sources.

---

## (A) Plain-English summary

1. **The dividend is not covered by free cash flow now.**
   - FY2026: CFO $2,868M minus capex $684M gives FCF of $2,184M, against dividends paid of $2,407M (FY26 10-K p. 58; my arithmetic), so dividends were 110% of FCF.
   - Q1 FY2027: FCF was -$64M ($135M CFO minus $199M capex) against $610M of dividends (Q1 FY27 10-Q p. 4; my arithmetic).
2. **Payout of earnings is above 100%.**
   - The $1.64 annual rate ($0.41 a quarter, Q1 FY27 10-Q p. 5) is 121% to 143% of FY2027 adjusted EPS guidance of $1.15 to $1.35 (Q1 FY27 release p. 1; my arithmetic). Guidance excludes about $0.15 of Pace charges, so GAAP payout is higher.
   - At FY2028 consensus EPS of $1.65 the payout is 99% (my arithmetic).
3. **The balance sheet absorbs this for now.**
   - Cash and short-term investments were $8,368M at Aug 31, 2026, against $7,893M of book debt ($2,000M current plus $5,893M long-term), so net cash was $475M (Q1 FY27 10-Q p. 3; my arithmetic).
   - Revolvers of $3.0B are undrawn and no commercial paper is outstanding (FY26 10-K p. 69; Q1 FY27 10-Q p. 34).
4. **Two maturities fall due by March 2027, and the ratings are sliding.**
   - Nike owes $1.0B at 2.38% due Nov 1, 2026 (19 days away) and $1.0B at 2.75% due Mar 27, 2027 (FY26 10-K p. 70).
   - S&P cut Nike to A from A+ with a negative outlook on Oct 5, 2026. It expects about $1.2B of cash burn a year for two to three years (secondary: Reuters via capital.com; Tradingpedia). The Q1 10-Q, filed Oct 2, still shows A+ and A2 (Q1 FY27 10-Q p. 34).
5. **Cash returns already ran ahead of cash generation.**
   - FY2023 to FY2026: dividends of $8,888M plus buybacks of $12,861M totalled $21,749M, against FCF of $16,941M (cash flow statements; my arithmetic).
   - Cash and short-term investments fell from $12,997M (May 2022) to $9,027M (May 2026) (data pack balances; my arithmetic).
   - Buybacks have been paused since Q1 FY2026. About $5.9B of the $18B program remains (Q1 FY27 10-Q p. 33).
6. **Forward model (my arithmetic):**
   - Base case (EPS $1.25, $1.65, $2.30): FCF covers the dividend 0.77x in FY2027, 1.04x in FY2028 and 1.36x in FY2029.
   - Stress case (EPS $1.00, Pace cash $1.0B, refinancing at 5.5%): coverage is 0.58x to 0.71x every year, and net cash turns to net debt of about $1.5B by FY2029.
   - Stress case with both 2027 notes repaid from cash: cash reaches the FY2019 low-water mark ($4.66B) in FY2029, so from FY2030 the dividend needs new debt.
7. **A filing-based tell.**
   - Every earnings release from Q3 FY2023 through Q3 FY2026 cited the "consecutive years of increasing dividend payouts."
   - The Q4 FY2026 (Jun 30, 2026) and Q1 FY2027 (Oct 1, 2026) releases dropped the phrase and say only "NIKE has a strong track record of returns to shareholders" (p. 1 of each; text search of all releases).
   - The November 2025 raise was 1 cent (3%), the smallest of the streak (Nike release, Nov 20, 2025).
8. **Verdict (my judgment).**
   - For the November 2026 declaration, which usually falls on Nov 14 to 20 and this year coincides with Investor Day on Nov 16 to 17, I put about 45% on a token raise that keeps the streak at 25, about 40% on a freeze, and about 15% on a cut.
   - I put the probability of a cut by May 2028 at about 30% in the base case and about 60% if FY2028 EPS tracks near $1.00.
   - Precedents say a cut that comes with a reset (VF's second cut, Estee Lauder) hurts on the day but was followed by gains at 12 months. First, partial cuts made by levered companies (Kraft Heinz, VF's first cut, Walgreens) did not mark the bottom.

---

## (B) Cash flow, FY2019 to Q1 FY2027

FCF is CFO minus PP&E additions (not a Nike measure; my arithmetic). Working-capital lines are as Nike reports them on the cash flow statement. Nike combines payables with accrued and other liabilities.

| Period | Net income | CFO | Capex | FCF | Dividends | Buybacks | Div % FCF | FCF less div and buybacks | AR | Inventories | Prepaid and other | Payables, accrued, other | WC total | SBC | Restructuring or severance cash | Interest paid | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FY2019 | 4,029 | 5,903 | 1,119 | 4,784 | 1,332 | 4,286 | 28% | -834 | -270 | -490 | -203 | 1,525 | 562 | 325 | n/d | 153 | FY21 10-K p. 60 |
| FY2020 | 2,539 | 2,485 | 1,086 | 1,399 | 1,452 | 3,067 | 104% | -3,120 | 1,239 | -1,854 | -654 | 24 | -1,245 | 429 | n/d | 140 | FY21 10-K p. 60 |
| FY2021 | 5,727 | 6,657 | 695 | 5,962 | 1,638 | 608 | 27% | 3,716 | -1,606 | 507 | -182 | 1,326 | 45 | 611 | n/d (charges $294M) | 293 | FY23 10-K p. 58; FY21 10-K p. 60 |
| FY2022 | 6,046 | 5,188 | 758 | 4,430 | 1,837 | 4,014 | 41% | -1,421 | -504 | -1,676 | -845 | 1,365 | -1,660 | 638 | n/d | 290 | FY23 10-K p. 58 |
| FY2023 | 5,070 | 5,841 | 969 | 4,872 | 2,012 | 5,480 | 41% | -2,620 | 489 | -133 | -644 | -225 | -513 | 755 | n/d | 347 | FY23 10-K p. 58 |
| FY2024 | 5,700 | 7,429 | 812 | 6,617 | 2,169 | 4,250 | 33% | 198 | -329 | 908 | -260 | 397 | 716 | 804 | 123 | 381 | FY26 10-K p. 58, 89 |
| FY2025 | 3,219 | 3,698 | 430 | 3,268 | 2,300 | 2,985 | 70% | -2,017 | -257 | 120 | -224 | -426 | -787 | 709 | 247 | 389 | FY26 10-K p. 58, 89 |
| FY2026 | 3,108 | 2,868 | 684 | 2,184 | 2,407 | 146 | 110% | -369 | -1,207 | -31 | 519 | -959 | -1,678 | 715 | 142 | 323 | FY26 10-K p. 58, 89 |
| Q1 FY2026 | 727 | 222 | 207 | 15 | 591 | 126 | n/m | -702 | -215 | -610 | -165 | 93 | -897 | 185 | n/d | n/d | Q1 FY27 10-Q p. 4 |
| Q1 FY2027 | 712 | 135 | 199 | -64 | 610 | 0 | n/m | -674 | 695 | -312 | -10 | -1,219 | -846 | 158 | about 243 | n/d | Q1 FY27 10-Q p. 4, 17 |

**Why FCF fell from $6,617M (FY2024) to $2,184M (FY2026), a $4,433M drop (my arithmetic from FY26 10-K p. 58).** Four explanations were tested:
- **Lower net income: -$2,592M** ($5,700M to $3,108M).
- **Working capital: -$2,394M** (+$716M to -$1,678M). The FY2026 receivables build of $1,207M includes the $684M IEEPA tariff receivable, which Nike had recorded but not collected at May 31, 2026 (FY26 10-K p. 30). Nike says the working-capital drain was "primarily driven by an increase in Accounts receivable and a decrease in Income taxes payable" (FY26 10-K p. 45).
- **Non-cash add-backs: +$425M.** D&A, deferred taxes, SBC, impairment and FX went from $1,013M to $1,438M.
- **Capex: +$128M** ($812M to $684M).

Lower capex is ruled out as a cause, since it helped. Earnings and working capital together explain the whole decline. Within working capital, about $684M is timing (IEEPA), and it reversed in Q1 FY2027: receivables fell $695M "primarily due to receipt of the International Emergency Economic Powers Act tariff receivable and the related U.S. federal income tax payment" (Q1 FY27 10-Q p. 33). Even if the receivable had been collected inside FY2026, FCF would have been about $2,868M, only 1.19x the dividend (my arithmetic). Moreover, the $986M IEEPA benefit in FY2026 net income "largely offset" tariffs that Nike expensed and paid during the year (FY26 10-K p. 30), so it is not recurring cash.

**Q1 FY2027 detail.**
- Working capital drained $846M even with the IEEPA receipt.
- Accrued liabilities fell $754M ($6,092M to $5,338M), of which compensation and benefits fell $457M (Q1 FY27 10-Q p. 7). That includes the $243M FY2026 severance accrual, which was "substantially all" paid (Q1 FY27 10-Q p. 17).
- Income taxes payable fell $199M, and inventories rose $312M (Q1 FY27 10-Q pp. 3, 4).

**Stock-based compensation.**
- SBC of $715M was 25% of FY2026 CFO and 33% of FCF (my arithmetic).
- With buybacks paused, SBC now shows up as dilution: shares outstanding rose from 1,475,990,487 (Mar 28, 2025, Q3 FY25 10-Q cover) to 1,485,308,829 (Sep 28, 2026, Q1 FY27 10-Q cover), up 0.63% (my arithmetic).
- FCF that adds back SBC overstates cash available to shareholders by the cost of offsetting that dilution. At $35.33 (market data, Oct 13, 2026), 9.3M shares would cost about $330M (my arithmetic).

**Other cash claims (FY26 10-K p. 46).**
- Endorsement obligations are about $15.5B, about $1.7B of it payable within 12 months.
- Product purchase obligations are $4.9B.
- Supplier-finance obligations of about $1.1B sit inside payables (Q1 FY27 10-Q p. 18).

---

## (C) Dividend history and coverage

| FY | DPS declared | Diluted EPS | Payout of EPS | Dividends % of FCF | Raise declared (Nike release) | Quarterly rate | Raise | Streak after raise |
|---|---|---|---|---|---|---|---|---|
| FY2019 | 0.860 | 2.49 | 35% | 28% | Nov 2018 (not opened) | 0.20 to 0.22 (inferred) | n/d | 17 |
| FY2020 | 0.955 | 1.60 | 60% | 104% | Nov 14, 2019 | 0.22 to 0.245 | 11% | 18 |
| FY2021 | 1.070 | 3.56 | 30% | 27% | Nov 19, 2020 (board date) | 0.245 to 0.275 | 12% | 19 |
| FY2022 | 1.190 | 3.75 | 32% | 41% | Nov 18, 2021 | 0.275 to 0.305 | 11% | 20 |
| FY2023 | 1.325 | 3.23 | 41% | 41% | Nov 15, 2022 | 0.305 to 0.340 | 11% | 21 |
| FY2024 | 1.450 | 3.73 | 39% | 33% | Nov 14, 2023 | 0.340 to 0.370 | 9% | 22 |
| FY2025 | 1.570 | 2.16 | 73% | 70% | Nov 14, 2024 | 0.37 to 0.40 | 8% | 23 |
| FY2026 | 1.630 | 2.10 | 78% | 110% | Nov 20, 2025 | 0.40 to 0.41 | 3% | 24 |
| FY2027 | 1.64 run-rate | 1.15 to 1.35 adjusted guide | 121% to 143% | Q1: n/m | expected Nov 2026 | 0.41 to ? | ? | 25 if raised |

Sources:
- DPS and EPS: 10-Ks (FY19 p. 22, 26; FY20 p. 25; FY21 p. 57, 61; FY22 p. 56, 60; FY23 p. 55 and Q4 FY23 release p. 2; FY24 p. 57, 61; FY25 p. 56 and Q4 FY25 release p. 2; FY26 p. 55, 59).
- Raise dates and sizes: Nike releases opened on investors.nike.com (detail ids 96, 73, 60, 46, 29, 12, 556).
- Payout ratios: my arithmetic.
- The FY2019 starting rate is inferred from 0.86 = 0.20 + 3 x 0.22.

**Notes on the payout.**
- FY2026 GAAP EPS of $2.10 includes a $0.52 IEEPA benefit (Q4 FY26 release p. 1). Excluding it, payout of EPS was 103% (1.63 / 1.58; my arithmetic).
- The dividend now costs about $2,436M a year (1,485,308,829 shares x $1.64; my arithmetic).
- At $35.33 the yield is 4.64% (market data; my arithmetic).

**Timing.** Every raise in the record was declared between Nov 14 and Nov 20 and paid in late December or early January. The next decision therefore lands in the same window as Investor Day, Nov 16 to 17, 2026. That date comes from REPORT.md, which cites Nike's Oct 1, 2026 employee memo; I did not reopen it.

**Board and management statements (opinion, quoted as evidence).**
- Nov 2019 (Parker): "NIKE has consistently delivered strong cash flow and returns for shareholders ... This dividend increase, combined with the four-year $15 billion share repurchase program announced in 2018, reflects continued confidence in our strategies."
- Nov 2020 (Donahoe): "This dividend increase reflects NIKE's financial strength and strong track record of returning capital to shareholders."
- Nov 2023 (Donahoe): "Nike has a consistent track record of delivering strong cash flow and returns for shareholders."
- Nov 2024 and Nov 2025: no executive quote at all, only the streak count. The Nov 2025 release: "Today's announcement marks the 24th consecutive year that NIKE has increased its quarterly dividend."
- Repurchases: "We continue to expect funding of any future share repurchases to come from operating cash flows" (Q1 FY27 10-Q p. 33). There is no equivalent sentence about dividends.
- Streak language in earnings releases: present in every release from Q3 FY2023 to Q3 FY2026, absent in Q4 FY2026 and Q1 FY2027 (p. 1 of each; text search).
  - Ruled out: a new-CFO style change, because the Q4 release (Jun 30) predates David Denton's Aug 16 start (8-K filed Jun 23, 2026, p. 2).
  - Cannot separate: editorial trimming versus deliberate de-emphasis ahead of a freeze. The Nov 2026 declaration decides it.

**Retained earnings** were -$155M at May 31, 2026 and -$56M at Aug 31, 2026 (FY26 10-K p. 57; Q1 FY27 10-Q p. 3). Dividends and buybacks have run through accumulated earnings. I found no filing that ties this to a legal limit on dividends.

---

## (D) Debt schedule, liquidity and ratings

**Senior notes** (FY26 10-K p. 70; unsecured, semi-annual coupons):

| Maturity | Fiscal year due | Coupon | Principal | Book May 31, 2026 | Swapped to floating | Indicative yield Oct 13, 2026 (secondary) |
|---|---|---|---|---|---|---|
| Nov 1, 2026 | FY2027 | 2.38% | 1,000 | 1,000 | no | matures in 19 days |
| Mar 27, 2027 | FY2027 | 2.75% | 1,000 | 1,000 | no | 4.81% (finanzen.net; quote time stale) |
| Mar 27, 2030 | FY2030 | 2.85% | 1,500 | 1,495 | no | 5.49% at 91.9 (finanzen.net, gettex) |
| Mar 27, 2040 | FY2040 | 3.25% | 1,000 | 986 | yes | n/d |
| May 1, 2043 | FY2043 | 3.63% | 500 | 497 | yes | n/d |
| Nov 1, 2045 | FY2046 | 3.88% | 1,000 | 987 | yes | 6.43% at 72.4 (finanzen.net, gettex) |
| Nov 1, 2046 | FY2047 | 3.38% | 500 | 493 | no | n/d |
| Mar 27, 2050 | FY2050 | 3.38% | 1,500 | 1,484 | no | 6.47% at 63.2 (finanzen.net, gettex) |
| **Total** | | **3.14% weighted (my arithmetic)** | **8,000** | **7,942** | $2.4B notional | |

- **Maturities.** Scheduled face maturities for FY2027 to FY2031 are "$2 billion, $0 billion, $0 billion, $1.5 billion and $0 billion" (FY26 10-K p. 70). The full $2.0B is current at Aug 31, 2026 (Q1 FY27 10-Q p. 3).
- **Fair value** of the notes was about $6.7B at Aug 31, 2026, against $7.9B book (Q1 FY27 10-Q p. 8), consistent with the above-coupon market yields in the table.
- **Swaps.** Nike receives fixed and pays SOFR plus a spread on $2.4B notional at 2.9% to 3.8% (FY26 10-K p. 70).
- **Bank lines.**
  - 5-year revolver: $2.0B (expandable to $3.0B), matures Mar 7, 2030, priced at Term SOFR + 0.725% with a 0.05% fee.
  - 364-day revolver: $1.0B (expandable to $1.5B), matures Mar 5, 2027, priced at Term SOFR + 0.625% with a 0.03% fee.
  - Both are undrawn (FY26 10-K p. 69). Pricing steps up if ratings fall, but "Changes in our long-term debt ratings would not trigger acceleration" (FY26 10-K p. 46).
  - $3B commercial paper program: nothing outstanding (Q1 FY27 10-Q p. 34).
  - Shelf registration for unlimited securities expires Jul 17, 2028 (Q1 FY27 10-Q p. 34).
- **Liquidity.** $8.4B of cash and investments plus $3.0B of revolvers gives $11.4B, matching S&P's "$11.4 billion" liquidity figure (secondary: Tradingpedia; my arithmetic).
- **Interest cost.**
  - Coupon cost is about $251M a year (my arithmetic). Interest paid was $323M in FY2026 (FY26 10-K p. 58).
  - Portfolio interest income was $278M (FY26 10-K p. 68), so net interest was income of $50M (FY26 10-K p. 55); Q1 FY2027 was income of $14M.
  - As cash is spent, net interest turns to expense. Refinancing the $2.0B of 2027 notes at about 5.5% instead of an average 2.56% adds about $59M a year before tax, about $0.03 of EPS (my arithmetic). This is small against FY2026 EBIT of $3,850M.
- **Leverage (my arithmetic).**
  - FY2026 EBITDA was $4,597M (EBIT $3,850M plus D&A $747M). Gross debt to EBITDA was 1.73x, or 2.40x including $3,091M of operating lease liabilities (FY26 10-K p. 57). Lease costs are not added back, so the lease-adjusted ratio is overstated.
  - Net cash: $475M at book, $368M at face, at Aug 31, 2026.

**Ratings history:**

| Date | Agency | Action | Rating | Outlook | Source |
|---|---|---|---|---|---|
| FY2019 to FY2024 | S&P / Moody's | held | AA- / A1 | | 10-Ks (FY19 p. 39 to FY24 p. 47) |
| Oct 2024 | S&P | outlook revised, AA- affirmed | AA- | negative | secondary: SGB Media, Oct 20, 2024 |
| Jul 2025 | S&P | downgrade | A+ | stable | secondary: SGB Media, Jul 16, 2025; FY25 10-K p. 46 shows A+ and A1 |
| Nov 12, 2025 | Moody's | downgrade | A2 | stable (from negative) | secondary: Reuters via MarketScreener, Nov 13, 2025; Q2 FY26 10-Q p. 40 shows A2 |
| Oct 5, 2026 | S&P | downgrade | A | negative | secondary: Reuters via capital.com; Tradingpedia |

What the agencies said (secondary, quoted as evidence):
- S&P on Oct 5, 2026: "turnaround efforts will take more time and higher investments than previously expected." It expects Nike to be "burning about $1.2 billion of cash annually over the next two to three years." The rating "could be lowered further at any time in the next 12-24 months" (Reuters via capital.com).
- S&P expects Nike to "pause share repurchase programs," and wants "adjusted free operating cash flow-to-debt ratio above 25%" (Tradingpedia).
- Moody's in Nov 2025 said cash flow would "remain constrained by higher capital expenditures and its sizable dividend," and projected adjusted debt to EBITDA of 2.5x in FY2026, falling to "the mid-1x range in fiscal 2027" (Reuters via MarketScreener). My base FY2027 EBITDA of about $3.2B implies 1.9x even after the $2.0B is repaid, so that 2025 path now looks too optimistic (my inference).

**Buyback status.**
- The $18B four-year program was approved in June 2022. In June 2026 it was "reapproved ... to continue without a fixed expiration date and without increasing the aggregate amount authorized."
- At Aug 31, 2026, 124.4M shares had been bought for about $12.1B (average $97.57), leaving about $5.9B (Q1 FY27 10-Q p. 33; FY26 10-K p. 26).
- Pace: remaining authorization went from $13.2B (May 2023, FY23 10-K p. 25) to $8.9B (May 2024, FY24 10-K p. 27) to $6.0B (May 2025, FY25 10-K p. 26). FY2026 purchases were only 1.8M shares for $122.4M (FY26 10-K p. 45), and Q1 FY2027 purchases were zero.
- Annual shares retired: 54.3M (FY2019) and 50.0M (FY2023), then 1.8M (FY2026) (10-Ks; `buyback_and_shares.csv`).

---

## (E) Forward cash scenarios, FY2027 to FY2029 (my arithmetic)

**Common assumptions (my assumptions unless sourced).**
- Start: cash and short-term investments of $9,027M at May 31, 2026 (FY26 10-K p. 57), so Q1 FY2027 is inside the FY2027 year. Debt face is $8,000M.
- Tax: 25% ("mid-20 percent range" guided, Q1 FY27 release p. 1).
- Non-cash items: D&A $760M (FY26 $747M; Q1 $193M), SBC $650M (Q1 $158M), other non-cash -$100M.
- Shares: 1,485M rising 0.5% a year, with no buybacks.
- EPS inputs are adjusted EPS. Pace cash is deducted separately, after tax.
- The comparison floor is $4,663M, the lowest May-31 cash and short-term investments in FY2019 to FY2026 (FY19 10-K p. 52).
- FCF/debt is my approximation (FCF over face debt plus $3,179M of leases). It is not S&P's calculation.

**Scenario inputs:**

| Input | Base | Stress |
|---|---|---|
| Adjusted EPS FY27 / FY28 / FY29 | 1.25 / 1.65 / 2.30 | 1.00 / 1.00 / 1.00 |
| Working capital | -300 / -200 / -300 (Q1 already -846) | -300 / 0 / 0 |
| Capex | 750 / 750 / 800 | 800 a year |
| Pace pre-tax cash | 300 / 250 / 150 (Nike: $0.3B of charges in FY27, "majority" cash, Q1 FY27 10-Q p. 18) | 350 / 350 / 300 ($1.0B) |
| DPS paid | 1.66 / 1.70 / 1.74 (1-cent raise each November) | 1.64 frozen |
| 2027 maturities ($2.0B) | repaid from cash (S&P expects this; secondary) | refinanced at 5.5% (2030 note yield, secondary) |

**Results:**

| Scenario | Year | CFO | FCF | Dividends | FCF / div | FCF less div | Cash + STI end | Debt face | Net cash | Debt / EBITDA | FCF / (debt + leases) | Payout of adj EPS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Base | FY2027 | 2,641 | 1,891 | 2,465 | 0.77x | -574 | 6,453 | 6,000 | 453 | 1.85x | 20.6% | 133% |
| Base | FY2028 | 3,384 | 2,634 | 2,536 | 1.04x | 98 | 6,551 | 6,000 | 551 | 1.48x | 28.7% | 103% |
| Base | FY2029 | 4,348 | 3,548 | 2,610 | 1.36x | 938 | 7,489 | 6,000 | 1,489 | 1.12x | 38.6% | 76% |
| Stress (refinance) | FY2027 | 2,210 | 1,410 | 2,435 | 0.58x | -1,025 | 8,002 | 8,000 | 2 | 2.92x | 12.6% | 164% |
| Stress (refinance) | FY2028 | 2,495 | 1,695 | 2,447 | 0.69x | -751 | 7,251 | 8,000 | -749 | 2.91x | 15.2% | 164% |
| Stress (refinance) | FY2029 | 2,541 | 1,741 | 2,460 | 0.71x | -719 | 6,531 | 8,000 | -1,469 | 2.90x | 15.6% | 164% |
| Stress, repay from cash | FY2027 | 2,232 | 1,432 | 2,435 | 0.59x | -1,003 | 6,024 | 6,000 | 24 | 2.19x | 15.6% | 164% |
| Stress, repay from cash | FY2028 | 2,540 | 1,740 | 2,447 | 0.71x | -707 | 5,317 | 6,000 | -683 | 2.18x | 19.0% | 164% |
| Stress, repay from cash | FY2029 | 2,585 | 1,785 | 2,460 | 0.73x | -675 | 4,642 | 6,000 | -1,358 | 2.17x | 19.4% | 164% |
| Stress, repay from cash | FY2030 (extrapolation) | 2,817 | 2,017 | 2,471 | 0.82x | -454 | 2,687 | 4,500 | -1,813 | 1.62x | 26.3% | 164% |
| S&P burn ($1.2B a year after dividends, debt repaid) | FY2027 / FY2028 / FY2029 | | | | | -1,200 a year | 5,827 / 4,627 / 3,427 | 6,000 | -173 / -1,373 / -2,573 | | | |

**When does the dividend have to be funded by cash or debt?**
- **From cash, immediately in both cases.** FY2027 FCF falls short of the dividend by about $0.6B in the base case and about $1.0B in the stress case. Q1 FY2027 FCF was already negative.
  - In the base case the gap closes in FY2028, but only if EPS reaches the $1.65 consensus.
  - Break-even: adjusted EPS of about $1.26 covers the current $2.44B dividend with flat working capital and no Pace cash, and about $1.52 is needed with -$200M of working capital and about $190M of after-tax Pace cash. I derived these from NI = dividends + capex - D&A - SBC + 100 - WC + Pace, divided by 1,490M shares (my arithmetic).
- **From debt, in the stress case.**
  - If the 2027 notes are repaid from cash, cash reaches the FY2019 floor in FY2029 ($4,642M). The $1.5B March 2030 maturity then pushes cash to about $2.7B, so the dividend needs new borrowing from FY2030.
  - If Nike refinances instead, cash holds above the floor through FY2031 ($5.5B extrapolated), but net debt reaches about $2.5B. The dividend is then debt-funded in substance from FY2028, when net cash turns negative.
  - On S&P's burn rate the floor is crossed in FY2028 ($4,627M).
- **Rating arithmetic.** My FCF/debt approximation is below S&P's 25% threshold in base FY2027 (20.6%) and in every stress year (12.6% to 19.4%). That points to further downgrade pressure in the stress case (my inference).
  - FOCF is measured before dividends, so a dividend cut does not raise the ratio. It only frees cash to repay debt. This explains why levered precedents (Kraft Heinz, VF, Walgreens, Hanesbrands) tied cuts to "deleveraging."
- **Sensitivity.** Each $0.10 of EPS is about $149M of cash (my arithmetic). Every cent of quarterly dividend costs about $59M a year (1,485M x $0.04; my arithmetic).

---

## (F) Precedents: dividend pressure at large consumer and quality companies

The KHC, VFC, INTC and EL rows are market data (Yahoo Finance chart API, adjusted close for the 6- and 12-month columns, raw close for the reaction day). The other rows are secondary. Payouts are my arithmetic on the cited figures.

| Company, date | Action | Payout before | Reaction day | 6m | 12m (SPY 12m) | Further low within 12m vs reaction close | Cut marked bottom? |
|---|---|---|---|---|---|---|---|
| Kraft Heinz, Feb 21, 2019 (after close) | cut 36%, $0.625 to $0.40 | 71% of 2018 adjusted EPS $3.51; GAAP loss (-$8.36) | -27.5% (Feb 22) | -45.3% | -40.3% (+22.5%) | -28.5% (Aug 27, 2019) | No |
| VF Corp, Feb 7, 2023 | cut 41%, $0.51 to $0.30; ended 50-year streak | about 97% of FY23 adjusted EPS guide $2.05 to $2.15 | -0.5% | -29.7% | -43.9% (+23.4%) | -54.1% (Nov 1, 2023) | No |
| VF Corp, Oct 30, 2023 (after close) | cut 70% to $0.09; guidance withdrawn; Reinvent | $1.20 run-rate vs Q2 adjusted EPS $0.63 | -14.0% (Oct 31); -23.5% over 2 days | -28.1% | +33.0% (+41.5%) | -18.7% (May 23, 2024) | Near: +51% vs reaction close at 12m |
| Intel, Feb 22, 2023 | cut 66%, $0.365 to $0.125 | dividend about $6B vs 2022 FCF about -$9.4B (secondary) | -2.3% | +27.2% | +67.2% (+29.1%) | -2.2% (Feb 27, 2023) | Yes (12m) |
| Intel, Aug 1, 2024 (after close) | suspended | n/a | -26.1% (Aug 2) | -32.9% | -30.1% (+17.1%) | -15.6% (Apr 8, 2025) | No |
| Estee Lauder, Oct 31, 2024 | cut 47%, $0.66 to $0.35; guidance withdrawn; new CEO | 102% of FY24 adjusted EPS $2.59; 244% of GAAP $1.08 | -20.9% | -33.2% | +9.0% (+19.2%) | -27.4% (Apr 8, 2025) | Not on the day; +35% vs reaction close at 12m |
| Walgreens, Jan 4, 2024 | cut 48%, $0.48 to $0.25 | 48% of FY23 adjusted EPS $3.98; 55% to 60% of FY24 guide | -6.5% at 11:10am, as much as -11.7% (secondary) | n/d | stock -64% in calendar 2024 (secondary) | n/d | No |
| Walgreens, Jan 30, 2025 | suspended | n/a | -15% at 9:31am (secondary, Bloomberg) | n/d | n/d | n/d | n/d |
| Hanesbrands, Feb 2, 2023 | eliminated $0.15 a quarter | $0.60 vs 2022 adjusted EPS (not verified; Q4 $0.07) | -23% to more than -27% (secondary) | n/d | n/d | n/d | n/d |

Sources:
- Kraft Heinz: AP/Reuters (foodprocessing.com, business-standard.com).
- VF: release excerpts (simplysafedividends, BusinessWire Oct 30, 2023).
- Intel: Reuters (kitco, businesstoday), Motley Fool; Aug 2024 via Reuters (adaderana, tuoitrenews).
- Estee Lauder: TipRanks, Globe and Mail; FY24 release (elcompanies.com).
- Walgreens: Motley Fool, Barchart, Bloomberg headline, supermarketnews.
- Hanesbrands: Axios, Motley Fool, ASI.
- Yahoo had no data for WBA or HBI, both delisted.

**What the precedents say, and what they cannot separate.**
1. **Payout before the cut.** Nike's 121% to 143% payout of guided adjusted EPS is above every adjusted-EPS payout in the set (48% to 102%). Only Estee Lauder (102%) and VF's first cut (about 97%) are close.
2. **Balance sheet.** The cutters, except Estee Lauder, were cutting to repay debt (stated reasons above). Nike has net cash and A ratings, the strongest balance sheet in the set. On leverage alone, Nike has less need to cut than any of them. The case for a cut rests on payout and cash burn, not solvency.
3. **Reaction size.** Unexpected cuts announced alongside guidance cuts fell 14% to 28% on the day (Kraft Heinz, VF's second cut, Intel's suspension, Estee Lauder, Hanesbrands). Telegraphed cuts barely moved (VF's first cut -0.5%, Intel's 2023 cut -2.3%). The data cannot separate the dividend effect from the earnings news on the same day, because every large move coincided with an earnings miss, an impairment or withdrawn guidance.
4. **Was the cut the bottom?** Of the 6 Yahoo-measured events, only Intel's 2023 cut had no meaningful further low (-2.2%). The stock was above the reaction-day close 12 months later in 3 of 6: VF's second cut (+51%), Intel's 2023 cut (+69%) and Estee Lauder (+35%). The 3 that worked were deep "reset" cuts. Partial first cuts (Kraft Heinz, VF's first cut, Walgreens) were followed by further declines.

---

## (G) Verdict

**Can Nike sustain the dividend?** Through FY2029, yes, financially. $8.4B of cash, net cash of about $0.5B, undrawn $3B lines and no maturities between Mar 2027 and Mar 2030 (filings above) cover a stress shortfall of $0.7B to $1.0B a year for about three years. It cannot sustain it from operations unless adjusted EPS returns to roughly $1.26 to $1.52 (break-even above), and FY2027 guidance is $1.15 to $1.35. **In the base case the dividend is cash-funded for one year (FY2027). In the stress case it is cash-funded every year and becomes debt-funded around FY2029 to FY2030** (section E).

**Probability and timing (my judgment, as of Oct 13, 2026):**

| Nov 2026 declaration (expected Nov 14 to 20, with Investor Day Nov 16 to 17) | Probability |
|---|---|
| Token raise (1 cent or less), streak extended to 25 | about 45% |
| Freeze at $0.41 (streak ends) | about 40% |
| Cut | about 15% |
| **Cut by May 2028, base case** | **about 30%** |
| **Cut by May 2028 if FY2028 EPS is near $1.00** | **about 60%** |

**Why this split, testing the alternatives.**
- **For holding or a token raise:**
  - The balance sheet allows it (section D).
  - FY2028 consensus ($1.65) roughly covers the dividend on earnings.
  - The board raised by 1 cent in Nov 2025 when the payout was already 73% of FY2025 EPS.
  - Swoosh, LLC holds 221,750,000 Class A shares (2026 proxy p. 70), and Class A elects three-quarters of the board, so it collects about $364M a year at $1.64 (my arithmetic). My inference is that the controlling holder's income favors continuity, but no filing says so.
- **For a freeze or cut:**
  - Payout is above 120% of guided earnings.
  - FCF has been negative year to date.
  - S&P downgraded and kept a negative outlook.
  - Release language dropped the streak in the last two quarters.
  - The November window coincides with Investor Day under a new CFO.
  - Estee Lauder is the closest precedent (above-100% payout, China pressure, leadership change, moderate leverage), and it cut alongside a reset.
- **What decides it:** the Nov 2026 declaration itself; any capital-allocation framework at Investor Day; Q2 FY2027 FCF (December); and whether Nike refinances the March 2027 note. Refinancing preserves cash for the dividend. Repaying from cash, as S&P expects, brings the stress floor forward.

**What it would mean for the stock and the shareholder base.**
- **Market pricing.** A 4.64% yield already prices doubt (market data; my inference). The yield on the 2030 note is about 5.5% (secondary). An equity yield that close to the company's own medium-term bond yield usually means the market doubts dividend growth (my inference).
- **A freeze** ends a 24-year streak. SPDR S&P Dividend ETF (SDY), which tracks a dividend-growth index, held Nike at 1.57% as of Sep 4, 2026 (secondary: koalagains). My inference is that a freeze triggers removal at the next reconstitution and forced selling; I did not open the index rules. A freeze saves only the 1-cent increments, about $59M a year.
- **A cut** to roughly 50% of FY2028 consensus EPS ($0.80 a year, $0.20 a quarter) would save about $1.25B a year (1,485M x $0.84; my arithmetic). That would close the stress FCF gap and protect the rating. The holder base would rotate from income and dividend-growth funds toward turnaround and value investors.
  - If the cut comes as a one-off "reset" with credible targets, precedents point to a 15% to 25% day move that recovers within 12 months (VF's second cut, Estee Lauder).
  - If it is a partial first cut in a still-deteriorating business, precedents point to further declines (Kraft Heinz, VF's first cut, Walgreens).
- **For the pitch:** the balance sheet is not the risk. The risk is that the dividend absorbs about $2.4B a year of cash that S&P's 25% FOCF/debt threshold and the Pace program also need. That makes the dividend decision a signal of how long management thinks the earnings trough lasts.

---

### Sources opened in this session (non-filing)
- Nike dividend releases, investors.nike.com press-release detail ids 96 (Nov 14, 2019), 73 (Nov 20, 2020), 60 (Nov 18, 2021), 46 (Nov 15, 2022), 29 (Nov 14, 2023), 12 (Nov 14, 2024), 556 (Nov 20, 2025), 565 (May 4, 2026), 572 (Aug 6, 2026). Saved in `capital/dl2/` and `capital/dl_ir/`.
- S&P Oct 2026: capital.com (Reuters, Oct 5, 2026, 14:48 UTC); tradingpedia.com (Oct 5, 2026).
- S&P Jul 2025 and Oct 2024: sgbonline.com (?p=345914; nikes-debt-ratings-lowered-by-sp).
- Moody's Nov 2025: ca.marketscreener.com (Reuters, Nov 13, 2025).
- Bond quotes: finanzen.net pages for WKN A28VAT (2050), A28VAR (2030), A1Z9N3 (2045), A28VAQ (2027), on gettex as of Oct 13, 2026. These are indicative retail-venue quotes. FINRA's bond center now redirects to a JavaScript page that could not be read.
- SDY weight: koalagains.com SDY holdings (Sep 4, 2026).
- Precedent articles as listed in (F).
- Market data: Yahoo Finance chart API for NKE, KHC, VFC, INTC, EL, SPY (`capital/dl_yahoo/`).

### Not verified, so excluded
- Hanesbrands full-year 2022 adjusted EPS.
- Walgreens' later outcome.
- SDY and VIG index removal rules.
- Restructuring cash for FY2019 to FY2023 (not disclosed in the filings searched).
- The November 2018 raise release.
- Investor Day dates (taken from REPORT.md, not reopened).
