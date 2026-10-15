# AC_FLOWS: what insiders, institutions, short sellers and the options market say about Nike (NKE)

Prepared 2026-10-13. Reference price $35.35 (NKE close 2026-10-12; Yahoo chart); options snapshot at $35.33 (Yahoo regularMarketPrice, 2026-10-13 about 20:00 UTC). Share counts: 1,485,308,829 total (Q1 FY27 10-Q cover, per `consensus_and_valuation.md`) and 1,203,921,077 Class B (Form 144 "units outstanding" field, accession 0001959173-26-007262). Class A is therefore 281,387,752 (my arithmetic).

This note extends `research_notes/thesis_tests/consensus_and_valuation.md`. It does not repeat that note's one-day short interest snapshot, beta or December ATM IV. It does not touch root causes, channels, China, Jordan, discounting, tariffs or product. The dividend question belongs to `research_notes/18_capital_and_dividend.md`; Section F only reports what option prices imply about it.

Source keys:
- F4 = Form 4 XML, https://www.sec.gov/Archives/edgar/data/320187/{accession}/ (158 filings from 2024-01-12 to 2026-09-17, listed by accession in `flows/insider_transactions_2024_2026.csv`)
- F144 = Form 144 XML, same path (36 notices, `flows/form144_2024_2026.csv`)
- SUB = https://data.sec.gov/submissions/CIK0000320187.json (fetched 2026-10-13; the latest filing is a Form 144 on 2026-10-05)
- 13G = Schedule 13G filings in the same index (accessions are given in Section D)
- 13FDS = SEC Form 13F data sets, https://www.sec.gov/data-research/sec-markets-data/form-13f-data-sets (7 quarterly zips, Dec 2024 through Aug 2026 filing windows), filtered to CUSIP 654106103
- FINRA = https://api.finra.org/data/group/otcMarket/name/consolidatedShortInterest (symbol NKE; fetched 2026-10-13)
- YOPT = https://query1.finance.yahoo.com/v7/finance/options/NKE?date={each of 18 expiries} (fetched 2026-10-13 with crumb)
- YQS = https://query1.finance.yahoo.com/v10/finance/quoteSummary/NKE?modules=institutionOwnership,fundOwnership,netSharePurchaseActivity,majorHoldersBreakdown,defaultKeyStatistics,calendarEvents (fetched 2026-10-13)
- YCH = https://query1.finance.yahoo.com/v8/finance/chart/NKE?period1=1672531200&period2=1792000000&interval=1d&events=div ; ^IRX chart for the 13-week T-bill (4.05%)

## (A) Plain-English summary

1. **Insiders bought, and they lost money.** Five directors made 10 discretionary open-market purchases, plus one 10b5-1 plan purchase, between Jan 2024 and Oct 2026. Together they bought 169,712 shares for $9.11M (F4). Every purchase is now under water. At $35.35 the shares are worth $6.00M, down 34% (my arithmetic). The CEO, Elliott Hill, bought twice, each time for about $1.0M: $61.10 on 2025-12-29 and $42.27 on 2026-04-13. Tim Cook bought $2.95M at $58.97 on 2025-12-22 and $1.06M at $42.43 on 2026-04-10.
2. **No insider has bought since the Oct 1, 2026 results.** In the last two buying rounds, purchases came 4 to 13 days after the earnings release. The latest filing in EDGAR (SUB, fetched Oct 13) is a 2026-10-05 Form 144 notice by the former CFO, Matthew Friend, to sell 19,572 shares. That leaves no Form 4 purchase 12 days after the release. A purchase on Oct 9 to 13 could still be filed, because Form 4 is due two business days after a trade.
3. **Insider selling is small and mostly planned.** In 2026 to date, open-market sales total $2.14M, and only $0.20M of that was discretionary (Amy Montagne, 2026-08-07). Mark Parker's 10b5-1 plan sold $48.9M in 2024 and $41.9M in 2025, mostly through option exercises. He has sold nothing in 2026, only giving shares away (33,616 shares) (F4, F144).
4. **The Knight family has not sold a share.** Swoosh, LLC distributed 4.0M Class A shares to its members in Jul 2024 and 5.0M in Dec 2025, and Phil Knight received 90% of each distribution. It still holds 221.75M Class A shares, which is 78.8% of Class A (my arithmetic). Phil Knight converted 4.5M Class A shares to Class B and gave them to his wife. Travis Knight's moves are trust and partnership transfers. No Knight entity reported an open-market sale or filed a Form 144 (F4).
5. **Active money split, and Capital Group was the largest buyer of the drop.** Capital Group (three 13F filers) grew its stake from 40.2M shares (Dec 2024) to 84.9M (Jun 2026), which is 7.1% of Class B. Its 13G shows 6.0% for Capital World Investors alone at 2026-06-30. In Q2 2026 Sixth Street (12.4M), Jupiter Topco (5.0M), Marshfield (4.3M) and Cable Car (2.3M) opened new positions, and Harris Associates (Oakmark) has built 14.4M since Q2 2025. On the other side, Pershing Square exited 18.8M shares in Q1 2025, Viking (9.0M) and Jennison (11.8M) exited in Q4 2025, Fundsmith (8.0M) exited in Q1 2026, and Janus Henderson (7.4M) and Longview (5.1M) exited in Q2 2026. Wellington (-16.1M), JPMorgan (-12.9M), BlackRock (-10.0M) and BNY (-8.3M) cut in Q2 2026 (13FDS).
6. **Holder breadth is shrinking while concentration rises.** The number of 13F filers holding NKE fell from 2,200 (Dec 2024) to 1,727 (Jun 2026), a 21% drop. The top five holders went from 28.0% to 32.9% of Class B, and the HHI from 344 to 437. Total 13F shares barely moved (955M vs 977M) (13FDS, my arithmetic).
7. **Short interest has risen about 7x and doubled since March.** Short interest was 14.5M shares (1.2% of Class B) on 2023-12-15. It reached 45.7M on 2026-03-31 and 99.2M on 2026-09-30 (8.2% of Class B, 6.7% of all shares). Days to cover stayed between 1.0 and 4.9 throughout, at 2.59 at the latest print (FINRA). The rise is persistent, but at about 2.6 days of volume it is not a crowded short.
8. **Options price a 6% to 7% earnings-day move and almost no crash premium, and they appear to price a lower dividend.** The term structure implies a one-standard-deviation move of about 6.4% to 7.2% for the Dec 17 print, against a 14-quarter average absolute move of 8.3%. The 1-sd range to Jun 17, 2027 is $25.79 to $49.47. Puts 10% out of the money cost about the same in IV as calls 10% out (skew 0 to 1.3 vol points). Put-call parity implies dividends roughly 45% to 60% below the current $0.41 quarterly rate, an unadjusted estimate that Section F qualifies (YOPT).

## (B) Insider transactions, directors and executive officers, Jan 2024 to Oct 13, 2026

Full detail (236 rows, every code, after removing two 4/A duplicates) is in `flows/insider_transactions_2024_2026.csv`. Plan status comes from the Form 4 "Rule 10b5-1" checkbox, the footnote "effected pursuant to a 10b5-1 trading plan adopted on ...", or the plan adoption date on the matching Form 144.

### B1. Open-market purchases (code P)

| Date | Name | Role | Shares | Price | Value ($) | Plan? | Return to $35.35 | Accession |
|---|---|---|---|---|---|---|---|---|
| 2024-06-28 | Robert Swan | Director | 2,941 | 77.02 | 226,516 | 10b5-1 (adopted 2023-07-03) | -54.1% | 0001127602-24-019550 |
| 2024-12-27 | John W. Rogers Jr. | Director | 2,500 | 76.65 | 191,624 | Discretionary | -53.9% | 0001127602-24-030177 |
| 2025-04-04 | Robert Swan | Director | 8,600 | 58.46 | 502,756 | Discretionary | -39.5% | 0001127602-25-011755 |
| 2025-11-07 | Jorgen Vig Knudstorp | Director | 16,150 | 62.09 | 1,002,754 | Discretionary | -43.1% | 0000320187-25-000105 |
| 2025-12-22 | Timothy D. Cook | Director | 50,000 | 58.97 | 2,948,500 | Discretionary | -40.1% | 0000320187-25-000146 |
| 2025-12-22 | Robert Swan | Director | 8,691 | 57.54 | 500,080 | Discretionary | -38.6% | 0000320187-25-000142 |
| 2025-12-29 | Elliott Hill | President and CEO, Director | 16,388 | 61.10 | 1,001,307 | Discretionary | -42.1% | 0000320187-25-000152 |
| 2026-04-07 | Robert Swan | Director | 11,781 | 42.44 | 500,002 | Discretionary | -16.7% | 0000320187-26-000043 |
| 2026-04-09 | John W. Rogers Jr. | Director | 4,000 | 43.34 | 173,360 | Discretionary | -18.4% | 0000320187-26-000045 |
| 2026-04-10 | Timothy D. Cook | Director | 25,000 | 42.43 | 1,060,750 | Discretionary | -16.7% | 0000320187-26-000049 |
| 2026-04-13 | Elliott Hill | President and CEO, Director | 23,660 | 42.27 | 1,000,118 | Discretionary | -16.4% | 0000320187-26-000053 (4/A, weighted average; original -000051 showed 42.265) |
| **Total** | 5 people | | **169,712** | | **9,107,767** | | **-34.1% ($6.00M at $35.35)** | |

Notes. Cook's Apr 2026 Form 4 footnote says "sold" while the transaction is coded P, which looks like a template typo. Hill's direct Class B holding after the 2026-09-01 award and tax withholding is 373,730 shares (F4 0000320187-26-000137). Cook holds 135,527 shares (F4 0000320187-26-000147).

**No purchases by** Mark Parker, any Knight, CFO David Denton, other executive officers or the remaining directors. Denton's only Form 4 is a 2026-09-01 award of 71,234 RSUs/PSUs and 259,946 options (F4 0000320187-26-000133). Alexandre Arnault (Form 3 filed 2026-09-17) received 5,171 restricted shares (F4 0000320187-26-000174).

**After the Oct 1, 2026 results:** no Form 4 purchase filed through the 2026-10-13 SUB fetch. Nike's policy footnote (in every F4) opens the window "after the first full trading day after the release of quarterly earnings", so the window opened about Oct 2 to 3. Re-check SUB after Oct 15.

### B2. Open-market sales (code S)

| Date | Name | Role | Shares | Price | Value ($) | Type | Plan adopted (Form 4 or 144) |
|---|---|---|---|---|---|---|---|
| 2024-02-14 | Mark Parker | Executive Chairman | 110,000 + 58,378 | 105.00 | 17,679,690 | Option exercise (strike $38.76) and sale, plus vested RS | 10b5-1, 2023-11-07 |
| 2024-05-07 | Monique Matheson | EVP CHRO | 45,000 | 94.16 | 4,237,200 | Option exercise ($77.54) and sale, **no plan** | none |
| 2024-05-09 | Johanna Nielsen | VP Controller | 282 | 93.64 | 26,406 | 10b5-1 | 2024-02-07 |
| 2024-05-14 | Mark Parker | Executive Chairman | 110,000 + 58,378 | 93.14 | 15,682,727 | Option exercise and sale | 10b5-1, 2023-11-07 |
| 2024-06-05 | Matthew Friend | EVP CFO | 9,350 | 95.10 | 889,185 | 10b5-1 | 2024-02-14 |
| 2024-07-18 | Mark Parker | Executive Chairman | 110,000 | 72.97 | 8,026,700 | Option exercise and sale | 10b5-1, 2023-11-07 |
| 2024-08-07 | Matthew Friend | EVP CFO | 5,410 | 72.88 | 394,281 | 10b5-1 | 2024-02-14 |
| 2024-08-14 | Mark Parker | Executive Chairman | 52,487 | 78.00 | 4,093,986 | 10b5-1 | 2023-11-07 |
| 2024-11-14 | Mark Parker | Executive Chairman | 45,190 | 76.64 | 3,463,362 | 10b5-1 | 2023-11-07 |
| 2025-02-11 | Heidi O'Neill | President, Consumer, Product and Brand | 14,147 | 71.18 | 1,006,983 | **Discretionary** | none |
| 2025-02-13 | Robert Leinwand | EVP CLO | 4,506 | 72.81 | 328,082 | 10b5-1 | 2024-11-14 |
| 2025-02-14 | Mark Parker | Executive Chairman | 110,000 + 59,732 | 72.83 | 12,361,582 | Option exercise ($56.40) and sale | 10b5-1, 2024-11-07 |
| 2025-05-14 | Mark Parker | Executive Chairman | 110,000 + 42,976 | 62.05 | 9,492,161 | Option exercise and sale | 10b5-1, 2024-11-07 |
| 2025-07-16 | Mark Parker | Executive Chairman | 110,000 | 72.29 | 7,951,900 | Option exercise and sale | 10b5-1, 2024-11-07 |
| 2025-08-05 | Robert Leinwand | EVP CLO | 1,644 | 74.91 | 123,152 | 10b5-1 | 2024-11-14 |
| 2025-08-13 | Philip McCartney | EVP Chief Innovation, Product and Design Officer | 3,162 | 77.21 | 244,138 | **Discretionary** | none |
| 2025-08-14 | Mark Parker | Executive Chairman | 86,078 | 75.93 | 6,535,903 | 10b5-1 | 2024-11-07 |
| 2025-09-05 | Robert Leinwand | EVP CLO | 1,019 | 74.64 | 76,058 | 10b5-1 per Form 144 (Form 4 box unticked) | 2024-11-14 |
| 2025-10-02 | Robert Leinwand | EVP CLO | 697 | 75.13 | 52,367 | **Discretionary** | none |
| 2025-10-06 | Treasure Heinle | EVP Chief People Officer | 4,300 | 71.27 | 306,461 | **Discretionary** (144 shows a plan date equal to the sale date) | none |
| 2025-11-14 | Mark Parker | Executive Chairman | 86,078 | 64.80 | 5,577,854 | 10b5-1 | 2024-11-07 |
| 2026-02-12 | Robert Leinwand | EVP CLO | 9,065 | 62.33 | 565,021 | 10b5-1 | 2024-11-14 |
| 2026-06-12 | Philip McCartney | EVP CIPDO | 17,398 | 46.18 | 803,440 | 10b5-1 | 2025-10-24 |
| 2026-08-05 | Friend, McCartney, Alagirisamy (COO), Leinwand | officers | 2,463 / 524 / 890 / 821 | 41.60 | 195,437 total | 10b5-1 (sales of vested RSUs) | various 2025-10 to 2026-02 |
| 2026-08-07 | Amy Montagne | President, Nike | 4,867 | 42.05 | 204,657 | **Discretionary** | none |
| 2026-09-09 | Alagirisamy, Leinwand, McCartney | officers | 3,671 / 3,646 / 2,559 | 37.59 | 371,239 total | 10b5-1 | 2025-11 to 2026-02 |

Form 144 notices with no Form 4 yet, because Friend is no longer a Section 16 officer: 5,304 shares (~2026-09-09, $199,377), 12,658 (~2026-09-30, $453,916) and 19,572 (~2026-10-05, $658,266). F144 accessions are 0001959173-26-006812, -007147 and -007262; plan adopted 2025-10-08.

### B3. Totals by category (F4; values at reported prices; my arithmetic)

| Category | Rows | Shares | Value ($) |
|---|---|---|---|
| Open-market purchase, discretionary | 10 | 166,771 | 8,881,251 |
| Open-market purchase, 10b5-1 | 1 | 2,941 | 226,516 |
| Option exercise and same-day sale, 10b5-1 (Parker) | 6 | 660,000 | 52,610,800 |
| Option exercise and sale, no plan (Matheson) | 1 | 45,000 | 4,237,200 |
| Open-market sale, 10b5-1 | 24 | 552,683 | 42,035,344 |
| Open-market sale, discretionary | 5 | 27,173 | 1,814,606 |
| Tax withholding on vesting (code F, not open market) | 46 | 146,409 | 9,573,110 |
| Gifts and trust transfers (code G) | 13 | Parker 152,304 shares to 2026-08-14; Phil Knight 4.5M to spouse; Travis Knight GRAT disbursements | n/a |
| Grants and awards (code A) | 98 | | n/a |

By year (all S rows): 2024 $54.5M (all plan or option-related); 2025 $44.1M ($1.6M discretionary); 2026 to date $2.1M ($0.2M discretionary). Purchases by year: $0.42M, $5.96M and $2.73M.

Cross-check: Yahoo netSharePurchaseActivity (6 months) shows 3.44M insider shares "bought" (YQS). That figure includes Travis Knight's 2.85M-share GRAT disbursement and the annual director awards, so it overstates open-market buying by about 60x.

## (C) Swoosh, LLC and the Knight family

| Date | Filer | Event | Shares | After | Source |
|---|---|---|---|---|---|
| 2024-07-09 | Swoosh, LLC | "Private pro rata distribution to members" of Class A | -4,000,000 A | 226,750,000 A | F4 0000320187-24-000031 |
| 2024-07-09 | Phil Knight | Received from Swoosh (90% of the distribution) | +3,600,000 A | 27,479,487 A direct; 8,335,687 B direct; 521,792 A by spouse | F4 0001127602-24-020315 |
| 2024-10-29 | Travis Knight | GRAT disbursement to himself (exempt, Rule 16a-13) | 3,180,141 B | 4,836,462 B direct | F4 0001127602-24-026159 |
| 2025-12-22 | Travis Knight | Contributed 1,694,859 B to Three Strings Investors, L.P. (100% his) | change in form | | F4 0000320187-26-000002 |
| 2025-12-29 | Swoosh, LLC | Second pro rata distribution | -5,000,000 A | 221,750,000 A | F4 0000320187-25-000154 |
| 2025-12-29 | Phil Knight | Received from Swoosh (90%) | +4,500,000 A | 31,979,487 A direct | F4 0000320187-25-000156 |
| 2025-12-31 | Travis Knight | 3,000,000 B from his 2009 trust, then contributed to Three Strings | change in form | Three Strings 4,694,859 B | F4 0000320187-26-000002 |
| 2026-02-02 | Phil Knight | Converted Class A to Class B (one-for-one) | 4,500,000 | 27,479,487 A; 12,835,687 B direct | F4 0000320187-26-000005 |
| 2026-02-11 | Phil Knight | Gift of Class B to spouse Penelope Knight | 4,500,000 B | 8,335,687 B direct; 4,500,000 B by spouse | F4 0000320187-26-000012 |
| 2026-04-02 | Travis Knight | Sold a 49% LP interest in Three Strings to his own 2012 children's trust for $288,317,000. Attributable Nike Class B: 2,300,480. Nike shares were "a minority of the value" of the partnership | 0 net market shares | | F4 0000320187-26-000041 |
| 2026-07-30 | Travis Knight | GRAT disbursement | 2,850,717 B | 2,889,704 B direct (after 2026-09-08 award) | F4 0000320187-26-000159 |

Reading:
- **No sales, no Form 144, no 13D or 13G** by Swoosh, Phil Knight or Travis Knight in Nike's EDGAR index for 2024 to Oct 2026 (SUB; all 36 Form 144s are by officers or Parker, see `flows/form144_2024_2026.csv`).
- Every move is estate or tax planning: member distributions, GRAT annuity payments, family partnership and trust transfers, an inter-spouse gift and a conversion. Shares moved inside the family rather than to the market.
- Control is unchanged. Swoosh's 221.75M Class A shares are 78.8% of the 281.4M Class A and 14.9% of all shares (my arithmetic). Class A elects three-quarters of the board (charter, per prior repo notes; not re-verified here).
- The one open question: Phil Knight converted 4.5M shares to Class B, which is the tradable class. Those shares now sit with his spouse and have not been sold. A Form 144 or Form 4 sale by Penelope Knight would be the first real Knight supply signal. She is not a Section 16 filer herself, so watch Phil Knight's Form 4s for indirect "by spouse" changes.

## (D) Institutional ownership from 13F filings (Q4 2024 to Q2 2026)

Method: every 13F-HR in the SEC Form 13F data sets with CUSIP 654106103 (Class B), equity rows only (puts and calls kept separately). Per filer and quarter I take the latest original or restatement filing and add "new holdings" amendments. Nine filings that reported dollar value in the share field were corrected to value divided by the quarter-end close (for example, J. Stern & Co. at 2025-12-31 reported 48,054,542 "shares" with $48.05M in value; corrected to 754k). Vanguard's six entities and Capital Group's three are combined, because Vanguard split its reporting on 2026-01-12 (13G/A 0000102909-26-001994, which says so). Cross-check: my Jun 2026 figures equal Yahoo institutionOwnership exactly for BlackRock 81,814,490, Capital World Investors 72,055,429, Wellington 22,208,933 and UBS 17,395,783 (YQS). Q3 2026 13Fs (as of 2026-09-30) are due by Nov 16, 2026, so post-Oct 1 institutional flows are not visible yet. Files: `flows/13f_holders_panel_2024Q4_2026Q2.csv` (every filer), `flows/13f_top25_grouped.csv` and `flows/13f_large_flows_by_quarter.csv` (moves of at least 1.5M shares).

### D1. Top 20 holders at 2026-06-30 (shares, millions; % of 1,203.9M Class B)

| # | Holder | Dec-24 | Jun-25 | Dec-25 | Mar-26 | Jun-26 | % Cl. B | Q2-26 chg | Chg since Dec-24 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Vanguard (all entities) | 108.19 | 113.82 | 116.99 | 117.50 | 136.05 | 11.30 | +18.55 | +27.86 |
| 2 | Capital Group (CWI+CII+CRGI) | 40.15 | 47.37 | 59.31 | 68.90 | 84.94 | 7.05 | +16.04 | +44.79 |
| 3 | BlackRock | 93.82 | 92.13 | 92.16 | 91.80 | 81.81 | 6.80 | -9.98 | -12.00 |
| 4 | State Street | 58.68 | 59.15 | 59.32 | 59.55 | 63.60 | 5.28 | +4.05 | +4.92 |
| 5 | Geode | 25.38 | 25.86 | 26.44 | 28.94 | 29.26 | 2.43 | +0.32 | +3.88 |
| 6 | Wellington | 36.34 | 32.30 | 31.77 | 38.35 | 22.21 | 1.84 | -16.14 | -14.13 |
| 7 | FMR (Fidelity) | 14.80 | 24.91 | 21.61 | 21.00 | 21.17 | 1.76 | +0.17 | +6.36 |
| 8 | Morgan Stanley | 20.70 | 23.48 | 19.40 | 22.04 | 20.08 | 1.67 | -1.96 | -0.62 |
| 9 | UBS Group | 6.55 | 8.65 | 13.78 | 12.86 | 17.40 | 1.44 | +4.53 | +10.85 |
| 10 | Invesco | 6.21 | 12.16 | 13.37 | 15.13 | 14.90 | 1.24 | -0.23 | +8.68 |
| 11 | Harris Associates (Oakmark) | 0 | 8.75 | 14.96 | 14.78 | 14.40 | 1.20 | -0.37 | +14.40 |
| 12 | Norges Bank | 14.88 | 11.75 | 13.03 | n/d | 13.36 | 1.11 | n/d | -1.53 |
| 13 | Goldman Sachs Group | 6.94 | 15.59 | 9.36 | 7.57 | 12.45 | 1.03 | +4.89 | +5.52 |
| 14 | Charles Schwab IM | 9.21 | 9.95 | 10.45 | 10.91 | 12.38 | 1.03 | +1.47 | +3.18 |
| 15 | Sixth Street Partners Management | 0 | 0 | 0 | 0 | 12.38 | 1.03 | +12.38 (new) | +12.38 |
| 16 | Flossbach von Storch | 8.30 | 11.27 | 12.75 | 12.19 | 11.91 | 0.99 | -0.28 | +3.61 |
| 17 | Northern Trust | 14.69 | 14.04 | 12.91 | 12.37 | 11.86 | 0.99 | -0.51 | -2.83 |
| 18 | Royal Bank of Canada | 5.70 | 13.34 | 8.36 | 11.47 | 11.53 | 0.96 | +0.06 | +5.83 |
| 19 | Bank of America | 9.87 | 16.48 | 14.29 | 14.18 | 10.66 | 0.89 | -3.52 | +0.79 |
| 20 | Legal and General | 9.44 | 9.12 | 8.19 | 8.12 | 8.00 | 0.66 | -0.12 | -1.44 |

n/d = not disclosed. Norges Bank omits NKE from its Q1 and Q3 13Fs and adds the holding about a year later as a "new holdings" amendment. Its Q1 2024 and Q1 2025 positions arrived that way in May 2025 and May 2026, so its Q3 2025 and Q1 2026 positions are not yet public; this is not an exit.

Vanguard's +18.6M in Q2 2026 comes almost entirely from Vanguard Portfolio Management (28.5M to 45.8M), in the second quarter after the realignment. Vanguard Capital Management's 13G (0002100119-26-000802) shows 89.48M shares with sole dispositive power at 2026-03-31, against 77.37M in its 13F. Treat the Vanguard jump as a reporting artifact until the Q3 13F confirms it.

### D2. Who bought the drop and who sold (13FDS; shares, millions)

| Quarter (price at quarter end) | Notable buyers and new positions | Notable sellers and exits |
|---|---|---|
| Q1 2025 ($63.48) | Goldman +15.9; Nomura +9.7; JPM +9.6; Wellington +9.0; new: Jennison 8.0, Nuveen 7.9, **Viking Global 5.5**, Generation IM 3.4, PRIMECAP 1.8 | **Pershing Square exit 18.77**; Fisher -9.5; Two Sigma (two entities) -5.6; Renaissance exit 2.6 |
| Q2 2025 ($71.04) | FMR +10.0; DZ Bank +8.8; **new Harris Associates 8.75**; RBC +8.2; Two Sigma +8.0; Invesco +4.8 | Wellington -13.1; Goldman -7.3; Nomura -9.2; Wells Fargo -7.4; Sands Capital exit 3.75 |
| Q3 2025 ($69.73) | JPM +13.2; Nomura +6.8; Jennison +3.5; **Viking +2.0 (to 9.0)**; Citadel +2.5 | Wellington -12.0; RBC -6.7; Pacer -6.0; Generation IM exit 3.6; MFS -3.7 |
| Q4 2025 ($63.71) | Capital Group +12.9; Wellington +11.4; Harris +6.3; UBS +6.0; Jasper Ridge +4.7 | **Viking exit 9.0; Jennison exit 11.8**; JPM -8.9; Nomura -7.3; Goldman -4.9; BofA -4.4; FMR -4.4; Alyeska exit 2.5; Voloridge exit 2.0; Renaissance exit 1.5 |
| Q1 2026 ($52.82) | Capital Group +9.6; Wellington +6.6; RBC +3.1; Citadel +2.5; Susquehanna +3.9 (two entities) | **Fundsmith exit 8.0** (two entities); DZ Bank -7.0; Ameriprise -3.5; JPM -2.8; OMERS -2.5 |
| Q2 2026 ($41.05) | Capital Group +16.0; **new Sixth Street 12.38** (about $508M at $41.05); Arrowstreet +5.6; **new Jupiter Topco 5.03; new Marshfield Associates 4.34; new Cable Car Capital 2.31**; Goldman +4.9; UBS +4.5; Renaissance +3.8; Millennium +2.4 | Wellington -16.1; JPM -12.9; BlackRock -10.0; BNY -8.3; **Janus Henderson exit 7.4; Longview exit 5.1**; Citadel -4.5; BofA -3.5; Franklin -2.7 |

Bank, broker and quant lines (JPM, Goldman, Nomura, Citadel, Susquehanna, Jane Street) often reflect market-making, swap hedges or index books, not directional views. The fundamental signal sits in the long-only and concentrated holders. Buyers at falling prices: Capital Group, Harris/Oakmark, Sixth Street, Marshfield, Cable Car, Flossbach. Sellers: Pershing, Viking, Jennison, Fundsmith, Janus Henderson, Longview, Wellington. How these firms classify themselves (value, quality growth and so on) is not taken from their filings, so it is not asserted here.

### D3. Concentration and breadth (13FDS; my arithmetic)

| Quarter end | 13F holders (grouped) | 13F shares (M) | % of Class B | Top 5 % of Class B | HHI of 13F holders | 13F put / call underlying (M) |
|---|---|---|---|---|---|---|
| 2024-12-31 | 2,200 | 954.6 | 79.3 | 28.0 | 344 | 54.8 / 37.9 |
| 2025-03-31 | 2,115 | 1,010.6 | 83.9 | 29.7 | 340 | 59.3 / 43.9 |
| 2025-06-30 | 2,071 | 989.4 | 82.2 | 28.6 | 343 | 72.3 / 60.6 |
| 2025-09-30 | 2,062 | 971.0 | 80.7 | 28.5 | 355 | 61.6 / 62.4 |
| 2025-12-31 | 2,070 | 970.8 | 80.6 | 29.9 | 373 | 60.8 / 46.3 |
| 2026-03-31 | 1,919 | 945.0 | 78.5 | 31.2 | 411 | 58.6 / 41.2 |
| 2026-06-30 | 1,727 | 977.1 | 81.2 | 32.9 | 437 | 77.7 / 62.6 |

The number of holders fell 21% over six quarters while total institutional shares were flat, so smaller holders sold to bigger ones. Puts held by 13F filers hit a series high of 77.7M shares underlying at Jun 2026. The top put holders are market makers: Susquehanna 17.4M, Citadel 14.4M, Jane Street 14.0M, then Marshall Wace 3.3M, Millennium 3.3M and D. E. Shaw 3.1M. Yahoo's 6-month "net institutional buying" of -204M shares (-20.5%) is inconsistent with this flat total and probably reflects the Vanguard re-filing (YQS).

13G filings in the period: Capital World Investors 6.0% (72.57M sole dispositive) at 2026-06-30 (0001422849-26-000147), a new 5% crossing. State Street 5.0%, 4.9% and 5.0% (Jun 2025, Sep 2025, Mar 2026). Vanguard Capital Management 7.5% at 2026-03-31. Vanguard Group 8.95% at 2023-12-29 and BlackRock 7.3% at 2023-12-31 (filed 2024).

## (E) Short interest history, Dec 2023 to Sep 2026 (FINRA, biweekly)

Full series (68 settlement dates) in `flows/short_interest_finra_2023_2026.csv`. % of Class B uses 1,203.9M; % of all shares uses 1,485.3M. Days to cover is FINRA's (short interest divided by average daily volume). Selected points:

| Settlement | Short shares (M) | % Class B | % all shares | Avg daily vol (M) | Days to cover | NKE close |
|---|---|---|---|---|---|---|
| 2023-12-15 | 14.48 | 1.20 | 0.97 | 8.33 | 1.74 | 121.55 |
| 2024-06-28 | 22.66 | 1.88 | 1.53 | 24.72 | 1.00 | 75.37 |
| 2024-12-31 | 27.90 | 2.32 | 1.88 | 15.19 | 1.84 | 75.67 |
| 2025-02-28 | 42.12 | 3.50 | 2.84 | 16.43 | 2.56 | 79.43 |
| 2025-04-15 | 50.42 | 4.19 | 3.39 | 36.85 | 1.37 | 54.83 |
| 2025-08-15 | 42.09 | 3.50 | 2.83 | 8.63 | 4.88 (series high) | 76.97 |
| 2025-09-30 | 32.10 | 2.67 | 2.16 | 17.16 | 1.87 | 69.73 |
| 2025-12-31 | 41.14 | 3.42 | 2.77 | 32.84 | 1.25 | 63.71 |
| 2026-03-31 | 45.71 | 3.80 | 3.08 | 16.11 | 2.84 | 52.82 |
| 2026-04-15 | 56.12 | 4.66 | 3.78 | 39.77 | 1.41 | 45.44 |
| 2026-06-30 | 72.29 | 6.00 | 4.87 | 32.95 | 2.19 | 41.05 |
| 2026-08-31 | 75.59 | 6.28 | 5.09 | 30.83 | 2.45 | 39.06 |
| 2026-09-15 | 85.70 | 7.12 | 5.77 | 27.61 | 3.10 | 36.22 |
| 2026-09-30 | 99.24 | 8.24 | 6.68 | 38.32 | 2.59 | 35.40 |

Reading:
- Short interest rose about 6.9x from Dec 2023 to Sep 2026 (my arithmetic). It rose in five straight prints from 2026-07-31 (57.4M) to 2026-09-30 (99.2M), which is +73% in two months.
- In dollars: about $3.51B short at $35.40, against $1.76B at $121.55 in Dec 2023 (my arithmetic). Share count roughly doubled while price fell by 71%.
- Days to cover never exceeded 4.9. Volume rose with the short position (ADV 8M in Dec 2023, 38M in Sep 2026), so a squeeze would need little buying relative to normal trading.
- FINRA's 2.59 days differs from Yahoo's 3.03 for the same date (consensus note); Yahoo uses a different volume average.
- The 13F put total (77.7M underlying at Jun 2026) and market-maker hedging mean part of reported short interest is delta hedging, not outright bearish positions. The data cannot split the two. Borrow fees were not available from an openable source.
- The Oct 1 results fall between the 2026-09-30 and 2026-10-15 settlement dates. The Oct 15 print (published about Oct 24 to 27) is the first reading after the results.

## (F) Options market, 2026-10-13 (YOPT; spot $35.33)

Files: `flows/options_chain_2026-10-13.csv` (every contract, with bid, ask, OI, volume, Yahoo IV and my Black-Scholes IV), `flows/options_term_structure_2026-10-13.csv` (per expiry: ATM IV with a 4.64% continuous dividend yield, straddle, OI and volume put/call), and `flows/options_surface_forward_based.csv` (Black-76 IV off the forward implied by put-call parity, which removes the dividend assumption; 1-sd range; risk-neutral probabilities). Also `flows/options_implied_dividends.csv` and `flows/earnings_day_moves.csv`. Rate: 13-week T-bill 4.05% (^IRX).

### F1. Term structure (forward-based ATM IV)

| Expiry | Days | ATM IV | 1-sd range at expiry | 90% put IV | 110% call IV | Skew (pts) | P/C OI | RN P(<$30) | RN P(>$45) |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-23 | 10 | 34.4% | 33.46 to 37.50 | 40.7% | 38.1% | +2.6 | 0.52 | 0.2% | 0.0% |
| 2026-11-20 | 38 | 37.3% | 31.53 to 40.11 | 38.4% | 38.1% | +0.4 | 0.80 | 8.8% | 2.2% |
| 2026-11-27 | 45 | 36.5% | 31.32 to 40.47 | 36.8% | 36.9% | -0.1 | 0.89 | 10.1% | 2.9% |
| 2026-12-18 (after Dec 17 print) | 66 | 39.4% | 29.91 to 41.83 | 40.3% | 39.1% | +1.3 | 0.50 | 18.4% | 6.4% |
| 2027-01-15 | 94 | 40.5% | 28.88 to 43.57 | 40.9% | 40.3% | +0.6 | 0.49 | 23.8% | 10.4% |
| 2027-06-17 | 247 | 39.6% | 25.79 to 49.47 | 39.8% | 39.0% | +0.8 | 1.07 | 35.5% | 19.2% |
| 2028-01-21 | 465 | 40.3% | 23.09 to 57.37 | 40.6% | 39.7% | +0.9 | 0.83 | 42.2% | 24.4% |

The 1-sd range is lognormal around the parity forward. RN P is the risk-neutral probability N(d2), which includes no risk premium.

- **Shape:** front-month IV is about 34%, rising to about 39% to 41% from December onward. The curve is flat from Dec 2026 to 2029 (40% to 42%). The market prices persistently high volatility, not one event.
- **Skew is nearly flat:** puts 10% out of the money are priced within 1.3 vol points of calls 10% out for every expiry from Nov 2026 on. Single stocks usually carry a put premium. A flat skew after a 71% drawdown means the market is not paying up for crash protection relative to upside.
- **Put/call OI:** 974,079 puts against 1,463,026 calls, a ratio of 0.67. Much of the call OI is stale far out-of-the-money strikes left from higher prices: Jan 2027 50C 29,964, 60C 28,948, 77.5C 27,426; Dec 2026 60C 28,562. Excluding them would raise the ratio, so 0.67 overstates call demand. The largest positions near the money are Oct 16 40C 54,044 and 35P 40,896, Jan 2027 40P 30,103, and Dec 2026 40C 24,057 and 35P 23,803. Volume P/C on 2026-10-13 was 0.89 (46,110 puts against 52,082 calls).

### F2. Implied move around the next earnings (estimated 2026-12-17; Yahoo calendarEvents says "isEarningsDateEstimate true")

- The Dec 18 ATM straddle costs $4.665, or 13.2% of spot. That covers 66 days of ordinary volatility plus the print.
- Event variance (Dec 18 total variance less Nov 27 total variance less the base variance for the 21 extra days) gives a one-day 1-sd move of **6.4%** using Nov 27 IV as the base, or **7.2%** using Nov 13 IV. The expected absolute move is about 0.8x that, so 5.1% to 5.8% (my arithmetic). Using Jan 15 instead, in case the date slips past Dec 18, gives 8.0% to 10.3%, but that window also absorbs the rising long-dated curve.
- History (YCH; next-day close against the close before each 8-K Item 2.02 release, 14 releases from Jun 2023 to Oct 2026): average absolute move 8.3%, median 6.7%. The last four were -3.6% (2026-10-01), +4.9% (2026-06-30), -15.5% (2026-03-31) and -10.5% (2025-12-18). Ten of the 14 moves were negative.
- Conclusion: the options price roughly a median Nike earnings move, not a tail move. Of the last 14 reactions, 5 exceeded 7.2% in absolute size (my count from `earnings_day_moves.csv`).

### F3. What option prices imply about the dividend

Put-call parity on mids, at strikes within 10% of spot, gives the present value of dividends before each expiry. The scheduled amount assumes $0.41 on each ex-date (Dec 1, Mar 1, Jun 1, Sep 1; YCH dividends).

| Expiry | Ex-dates before expiry | Implied PV of dividends | Scheduled PV at $0.41 | Gap |
|---|---|---|---|---|
| 2026-12-18 | 1 | 0.21 | 0.41 | -48% |
| 2027-06-17 | 3 | 0.58 | 1.21 | -52% |
| 2028-01-21 | 5 | 0.77 | 2.00 | -62% |

Caveats:
- Expiries with no dividend show an implied value of -0.05 to -0.17, which points to a spot timing or basis error of about $0.10. Correcting for that narrows the Dec 2026 gap to about -25%, but the 2027 and 2028 gaps stay above 40%.
- The options are American. Calls on a 4.6% yielder carry an early-exercise premium that biases parity-implied dividends downward, so part of the gap is model bias.
- Read this as a directional hint that the options market prices some probability of a dividend cut, consistent with the forwards drifting above spot (Jan 2028 forward $36.39). It is not a measured probability. The dividend question itself is owned by note 18.

## (G) Verdict: what each signal says and how far to trust it

| Signal | Reading | Direction | How reliable is this kind of signal |
|---|---|---|---|
| Director and CEO open-market purchases (Dec 2025 and Apr 2026 clusters, $9.1M, 5 people, CEO twice) | Discretionary (opportunistic) buys after earnings, consistent with board confidence. Small against the size of the company and against Parker's $90.8M of planned sales in 2024 and 2025. All under water by 16% to 54% | Mildly bullish, weakened by the losses and by no buying after Oct 1 | Medium for the signal type, low at Nike's size. Lakonishok and Lee (2001, RFS 14(1):79-111): the predictive power comes from purchases, sales show none, and the effect concentrates in smaller firms. Nike is a $52B mega-cap. Jeng, Metrick and Zeckhauser (2003, REStat): purchases earn more than 6% a year abnormal; sales earn nothing significant. Cohen, Malloy and Pomorski (2012, JF 67:1009-1044): only opportunistic (non-routine) trades predict returns, at 82 bp a month value-weighted; routine trades earn about zero. Nike's buys are irregular, so they count as opportunistic, but the cluster of five buyers in two windows looks more like signalling than private information |
| Absence of buys after the Oct 1, 2026 guide-down (through Oct 13) | Insiders who bought at $42 to $61 did not add at $34 to $35 in the first 8 trading days | Mildly bearish | Low; the window runs to about Dec 14. Absence of purchases is not studied as a signal in the papers above |
| Officer sales | Small (2026 to date $2.1M) and mostly 10b5-1 sales of vested RSUs | Neutral | Low. Lakonishok and Lee: sales are uninformative. Jagolinzer (2009, Management Science 55(2):224-239): some plan sales are timed ahead of bad news, but the amounts here are immaterial |
| Knight family and Swoosh | No sales; only estate-planning transfers; control block intact (78.8% of Class A) | Neutral to mildly bullish (no supply overhang) | High as a "no overhang" fact; not a return predictor |
| 13F flows | Concentrated long-only buyers (Capital Group to 7.1% of Class B; Sixth Street, Harris/Oakmark, Marshfield and Cable Car new or building) against quality and growth exits (Pershing, Viking, Jennison, Fundsmith, Janus, Longview) | Mixed: the shareholder base is rotating from growth or quality holders to value and contrarian holders | Low to medium. Chen, Jegadeesh and Wermers (2000, JFQA 35(3):343-368): stocks funds buy beat stocks they sell, but widely held stocks do not outperform. 13Fs lag 45 days and miss shorts and the post-Oct 1 period |
| Short interest | 99.2M shares, 6.7% of all shares, about 7x since Dec 2023, +73% in two months, 2.6 days to cover | Bearish (informed selling pressure) with limited squeeze fuel | Medium. Boehmer, Jones and Zhang (2008, JF 63(2):491-527): heavily shorted NYSE stocks underperform lightly shorted ones by 1.16% over the next 20 trading days (15.6% annualized). The monthly-level FINRA data used here is coarser than their daily order data, and part of the position is option hedging |
| Options: level and term | 39% to 41% IV through 2029 with a flat term structure; the Dec print is priced at about a 6.4% to 7.2% 1-sd move, close to the 6.7% median of past reactions | Neutral on direction; says uncertainty is persistent | High as a range estimate (it is a traded price) |
| Options: skew and parity | Flat skew; parity leans toward relatively expensive calls, and the implied dividend is about half the current rate | Skew neutral to mildly bullish. Parity is ambiguous: Cremers and Weinbaum (2010, JFQA 45(2):335-367) find stocks with relatively expensive calls outperform those with expensive puts by about 50 bp a week, but here the call richness can be fully explained by a market-expected dividend cut, which is bearish for income holders | Low to medium; the effect has declined over time (Cremers and Weinbaum) and American early-exercise bias contaminates it |

**Bottom line.** The flow data shows a stock passing from growth and quality holders and short-term traders to concentrated value buyers. Short sellers lean bearish, and the options market prices a wide range: 1-sd $25.8 to $49.5 by Jun 2027. The insider purchases are real but small, and they have not been repeated since Oct 1. The academic evidence says they matter less at mega-cap size. None of these signals is strong enough to carry a thesis alone. The one actionable asymmetry for a pitch is the flat skew: downside protection costs no more than upside calls even though short interest has doubled since March. A bearish view can be expressed cheaply in puts. A bullish view needs a catalyst before Dec 17, because 2.6 days to cover gives little squeeze fuel.

**What would change the reading:**
- Form 4 purchases by Hill, Cook or Denton before the window closes (about Dec 14, 2026).
- The Oct 15 and Oct 30 short interest prints (published about Oct 27 and Nov 10).
- Q3 2026 13Fs on Nov 16: did Capital Group and Sixth Street add below $40?
- Any Form 144 or "by spouse" sale by the Knights.

## Files (data in `data/flows/`)

- `insider_transactions_2024_2026.csv`: all Form 4 rows, classified (category, plan date, value, accession, URL)
- `form4_all_raw.csv`: raw parse of the 158 Form 4 XMLs
- `form144_2024_2026.csv`: 36 Form 144 notices
- `13f_holders_panel_2024Q4_2026Q2.csv`: every 13F filer, shares, puts and calls for 7 quarters
- `13f_top25_grouped.csv`: top 25 with Vanguard and Capital Group grouped
- `13f_large_flows_by_quarter.csv`: moves of at least 1.5M shares
- `short_interest_finra_2023_2026.csv`: 68 biweekly prints with % and days to cover
- `options_chain_2026-10-13.csv`, `options_term_structure_2026-10-13.csv`, `options_surface_forward_based.csv`, `options_implied_dividends.csv`, `earnings_day_moves.csv`
- Scripts: `scripts/flows/` (parse_f4.py, parse_144.py, classify.py, f13.py, panel13f.py, top13f.py, opt.py, skew_b76.py, impdiv_earn.py). Raw downloads (EDGAR XML, FINRA, Yahoo; about 600 MB) are not committed.

Academic sources opened: https://ideas.repec.org/a/oup/rfinst/v14y2001i1p79-111.html (Lakonishok and Lee 2001); https://www.nber.org/papers/w16454 (Cohen, Malloy and Pomorski; JF 2012); https://ideas.repec.org/a/bla/jfinan/v63y2008i2p491-527.html (Boehmer, Jones and Zhang 2008); https://ideas.repec.org/a/cup/jfinqa/v45y2010i02p335-367_00.html (Cremers and Weinbaum 2010). Search-result abstracts only (not opened in full): Jeng, Metrick and Zeckhauser 2003 (https://www.nber.org/papers/w6913); Jagolinzer 2009 (https://ideas.repec.org/a/inm/ormnsc/v55y2009i2p224-239.html); Chen, Jegadeesh and Wermers 2000 (https://ideas.repec.org/a/cup/jfinqa/v35y2000i03p343-368_00.html).
