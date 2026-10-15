# G5. Credit market read: what Nike's bonds say about stress

Prepared Oct 15, 2026 (last bond quote Oct 14, last ICE BofA print Oct 13). Builds on `research_notes/18_capital_and_dividend.md` (debt table, ratings history) and `Deep dives Oct 14/D6_dividend_cash.md` (cash cover). It does not repeat them.

**Source tags.** OPENED = page or file read in this session. SNIPPET = search summary only. DERIVED = my arithmetic from cited inputs. REPO = taken from an earlier repo note, not re-opened.

Files: `G5_credit_market_snapshot_oct14.csv` (spread vs scaled rating lines), `G5_credit_market_event_window.csv` (Sep 30 to Oct 14), `G5_credit_market_monthly_spreads.csv` (month-end, all bonds, Jan 2023 to Oct 2026), `data/credit/g5_bond_daily_spreads.csv` (17,783 daily rows), scripts in `scripts/credit/` (they read scratch downloads; paths inside need editing to rerun).

---

## 1. Verdict

**Smoking gun: NO.** The credit market prices Nike as a high single-A credit, not as BBB (stress) and not at its old AA minus.

| Test | Result | Tag |
|---|---|---|
| Nike 2030 note, Z-spread to Treasuries, Oct 14 | 49.8 bp (YTM 5.45%) | DERIVED |
| Nike 2040 / 2045 / 2050 notes | 84 / 78 / 79 bp (YTM 6.21% / 6.37% / 6.39%) | DERIVED |
| Rating lines scaled to the same maturity (ICE BofA AA, A, BBB OAS times maturity factor) | 3.5y: AA 52, A 62, BBB 91 bp. 13y to 23y: AA 73, A 86, BBB 127 bp | DERIVED |
| Where Nike sits | 3.5y: 12 bp inside the A line (AA-like). 13y to 23y: between the AA and A lines (A+ to A). A BBB price would be 41 bp (3.5y) to 41 to 52 bp (long end) wider than observed | DERIVED |
| Agency ratings | S&P A (negative) since Oct 5, 2026; Moody's A2 (stable). Market pricing is equal to or slightly better than the ratings, so no unrated stress is priced | see 4 |
| Spread move on the Oct 1 guide cut | Widened 9 to 14 bp across the curve from Sep 30 to Oct 14 while ICE index OAS was flat to down 2 bp. Marginal statistically (see 5) | DERIVED |

What would have been a smoking gun: bonds at BBB lines (2030 note near 91 bp, long bonds near 127 bp), or a spread jump several times the noise on Oct 2 to 5. Neither happened.

**Equity versus credit.** Equity has sold off about 3.6% on Oct 2 (REPO `data/nke_daily_prices.csv`: 35.15 to 33.87). Credit moved a fraction of one notch. Bondholders are paid by $8.4B of cash against $2.0B of 2027 maturities (Q1 FY27 10-Q p. 3, REPO D6), so a stress premium is not warranted on liquidity. The short thesis depends on earnings power in FY28, which a creditor with a 3.5 year to 24 year claim does not need.

---

## 2. Nike bond table, Oct 14, 2026

Clean prices are last-close indicative quotes on German retail venues (gettex), not FINRA TRACE institutional prints (see 7). Yield is my semiannual 30/360 YTM, settle T+1. "Treasury" is the Treasury.gov par curve linearly interpolated to the remaining life. Z-spread uses a par-curve bootstrap. finanzen.net's own yields (same day) are within 3 bp for the five bonds checked (2050: 6.427 vs my 6.388; 2030: 5.476 vs 5.454; 2045: 6.395 vs 6.365; 2040: 6.211 vs 6.207; 2027: 4.823 vs 4.792). Tag: OPENED (finanzen.net list and bond page, Oct 14 and 15) plus DERIVED.

| Note | Face | Years left | Clean px | YTM % | Treasury % | I-spread bp | Z-spread bp |
|---|---|---|---|---|---|---|---|
| 2.375% Nov 1, 2026 | $1.0B | 0.05 | 99.78 | n/m (17 days) | | n/m | n/m |
| 2.75% Mar 27, 2027 | $1.0B | 0.45 | 99.10 | 4.79 | 4.37 | 42.5 | 41.3 |
| 2.85% Mar 27, 2030 | $1.5B | 3.45 | 91.91 | 5.45 | 4.94 | 51.6 | 49.8 |
| 3.25% Mar 27, 2040 | $1.0B | 13.45 | 73.29 | 6.21 | 5.32 | 88.6 | 84.2 |
| 3.625% May 1, 2043 | $0.5B | 16.54 | 72.31 | 6.35 | 5.44 | 91.5 | 86.7 |
| 3.875% Nov 1, 2045 | $1.0B | 19.05 | 72.74 | 6.37 | 5.53 | 83.1 | 78.4 |
| 3.375% Nov 1, 2046 | $0.5B | 20.05 | 66.28 | 6.38 | 5.57 | 80.9 | 74.6 |
| 3.375% Mar 27, 2050 | $1.5B | 23.45 | 63.63 | 6.39 | 5.55 | 83.5 | 78.7 |

(Face from `data/capital/debt_schedule.csv`. The 2.40% Mar 2025 note has no quotes and matured, consistent with REPO debt table.)

Long-bond price is below 75 for every note from 2040 on. The loss versus Dec 30, 2025 for the 2050 note (71.56 to 63.63) is mostly Treasury yield: yield +87 bp, Treasury +77 bp, Z-spread +10 bp (DERIVED). From Sep 30 to Oct 14 the 2050 yield rose 2.5 bp, with Treasuries down 11 bp and spread up 14 bp: all of the widening was credit, offset by lower Treasury yields.

**Funding cost read-through (DERIVED).** A new 3.5 year note would price near 5.45%, matching the 5.5% refinancing assumption already in note 18 (about $59M a year extra interest on $2.0B, about $0.03 EPS). A BBB-style spread of 91 bp instead of 50 bp would add 41 bp on $2.0B, which is $8M a year pretax, about $0.004 per share. The credit rating is not a profit driver for FY28.

---

## 3. Peers on the same day

Same method. USD peers use the Treasury benchmark; EUR peers use the ECB AAA government spot curve (converted to annual compounding), so EUR spreads are I-spreads only and are not comparable one-to-one with USD. Ratings column: SNIPPET from search results, not verified at source, some stale.

| Bond | Years | Px | YTM % | Z / I bp | ICE bucket OAS bp | Agency rating (snippet) |
|---|---|---|---|---|---|---|
| Nike 2.85% 2030 | 3.45 | 91.91 | 5.45 | 49.8 | 73 | S&P A, Moody's A2 (OPENED) |
| Ralph Lauren 2.95% 2030 | 3.67 | 91.54 | 5.53 | 56.2 | 73 | not found |
| Tapestry 5.1% 2030 | 3.40 | 98.20 | 5.69 | 73.2 | 73 | Baa2/BBB at Dec 2024 pricing (SNIPPET) |
| PVH 5.5% 2030 | 3.66 | 98.30 | 6.02 | 104.7 | 73 | not found |
| Levi 3.5% 2031 (USD) | 4.38 | 89.92 | 6.16 | 114.9 | 73 | not found |
| Under Armour 7.25% 2030 | 3.75 | 96.78 | 8.26 | 321.0 | 73 | S&P BB- on CreditWatch negative, Moody's Ba2 (SNIPPET, undated) |
| Ralph Lauren 5.0% 2032 | 5.67 | 97.17 | 5.59 | 54.3 | 86 | not found |
| Tapestry 3.05% 2032 | 5.42 | 87.02 | 5.88 | 83.5 | 86 | Baa2/BBB (SNIPPET) |
| Tapestry 5.5% 2035 | 8.40 | 95.39 | 6.21 | 104.8 | 102 | Baa2/BBB (SNIPPET) |
| VF 6.0% 2033 | 7.00 | 93.97 | 7.11 | 196.4 | 102 | S&P BB (SNIPPET, undated) |
| adidas 3.125% Nov 2029 (EUR) | 3.1 | 98.60 | 3.61 | 42.6 (I) | n/a | A-/A3 in 2022; current not found (SNIPPET) |
| adidas 2.75% Nov 2030 (EUR) | 4.1 | 95.94 | 3.85 | 62.7 (I) | n/a | same |
| adidas 0.625% Sep 2035 (EUR) | 8.9 | 73.56 | 4.26 | 76.7 (I) | n/a | same |
| VF 4.25% Mar 2029 (EUR) | 2.4 | 98.85 | 4.76 | 160.9 (I) | n/a | S&P BB |
| PVH 4.125% Jul 2029 (EUR) | 2.8 | 100.20 | 4.04 | 87.5 (I) | n/a | not found |
| Levi 4.0% Aug 2030 (EUR) | 3.8 | 97.49 | 4.73 | 151.6 (I) | n/a | not found |

Hanesbrands: no quotes on any German venue for the 9.0% 2031 or 4.875% 2026 notes (finanzen.net lists them with no yield; history empty on 7 venues). Not comparable. Not tried further because the notes are likely redeemed or delisted after the Gildan deal; unverified.

Reading, at the 2030 point (3.4 to 3.8 years): Nike 50, Ralph Lauren 56, Tapestry 73, PVH 105, Levi 115, Under Armour 321. Nike is the tightest, 6 bp inside Ralph Lauren, 23 bp inside Tapestry (Baa2/BBB), 55 bp inside PVH. The market ranks Nike as the strongest credit in the group, above a BBB peer by 23 bp. Out of scope here but noted: Nike's EUR peer adidas 2030 sits at 63 bp over AAA euro governments, which cannot be placed on the USD scale.

Sector context: from Sep 30 to Oct 14 the spread changes were Ralph Lauren -3 to +12, Tapestry -2 to +6, PVH +6, VF +9, Under Armour -9. Nike's +9 to +14 is at the top of the range but not alone (Levi -34 is a quote artifact or tightening; do not rely on it).

---

## 4. Rating actions, 2024 to 2026

| Date | Agency | Action | Rating after | Outlook | Tag |
|---|---|---|---|---|---|
| Oct 2024 | S&P | outlook to negative, AA minus affirmed (REPO row); the Oct 2024 downgrade to A+ is mentioned in a search summary and conflicts with the REPO date of Jul 2025 | AA- | negative | REPO; conflict flagged |
| Jul 2025 | S&P | one notch down | A+ | stable | REPO (FY25 10-K p. 46 shows A+) |
| Nov 12, 2025 | Moody's | one notch down | A2 | stable | SNIPPET here, REPO opened (Q2 FY26 10-Q p. 40 shows A2) |
| Oct 5, 2026 | S&P | one notch down | A | negative | OPENED (Reuters via capital.com, Oct 5, 2026 14:48 UTC): "sees co burning about $1.2 billion of cash annually over the next two to three years" |
| Fitch | none found | | | | see route log; the Q1 FY27 10-Q p. 34 names only S&P and Moody's as raters (OPENED) |

Open conflict: a search summary says S&P cut Nike from AA- to A+ in October 2024. REPO and the FY25 10-K support July 2025. Not resolved here; S&P's own release is behind a 403. It does not change the verdict because both dates fall before the current A.

Q1 FY27 10-Q (filed Oct 2) still lists "A+ and A2" and states "Any changes to these ratings could result in interest rate and facility fee changes" (OPENED, text search of nke-20260831.htm). The 5-year revolver is priced at SOFR + 0.725% (REPO).

---

## 5. Did spreads move on the Oct 1 guide cut?

The Q1 FY27 release came after the close on Oct 1; first trading reaction is Oct 2 (equity: 35.15 to 33.87, REPO). Z-spread bp, from `G5_credit_market_event_window.csv`:

| Bond | Sep 30 | Oct 2 | Oct 5 (S&P cut) | Oct 14 | Total change |
|---|---|---|---|---|---|
| 2030 | 41.1 | 44.7 | 44.6 | 49.8 | +8.7 |
| 2040 | 72.7 | 73.5 | 76.1 | 84.2 | +11.5 |
| 2045 | 66.7 | 71.5 | 72.9 | 78.4 | +11.7 |
| 2050 | 64.7 | 70.8 | 72.1 | 78.7 | +14.0 |
| ICE 15+ year OAS (all ratings) | 102 | 102 | 101 | 102 (Oct 13) | 0 |
| ICE A OAS | 72 | 72 | 72 | 70 | -2 |
| ICE BBB OAS | 103 | 104 | 104 | 103 | 0 |

Noise (DERIVED, 961 daily 2050-bond observations since Jan 2023): daily change standard deviation 4.5 bp; 9 trading day change standard deviation 7.2 bp. Quote bid-ask in spread terms is about 5 bp (bid 63.88 / ask 64.29 per finanzen.net, Oct 14) to 12 bp (clean 63.62 / 64.50, same page). So:

- Guide cut and downgrade together: +14 bp on the 2050 note is 1.9 standard deviations of a 9 day move, and about equal to the quote width. It is real in direction (all six long bonds widened by 9 to 14 bp against flat indices) but small.
- Split by date: Sep 30 to Oct 2 (guide cut) +6.1 bp; Oct 2 to Oct 5 (S&P cut, which followed the guide cut) +1.3 bp; Oct 5 to Oct 14 +6.6 bp. The S&P downgrade day carried almost nothing, so it was priced on Oct 2 or earlier, or priced gradually.
- A one-day artifact exists: the Oct 1 quote (before the release) is already 74.3 bp, then 70.8 on Oct 2. That is quote timing noise of the size of the whole effect, so a precise day-by-day attribution is not possible.

**Placebos** (Nike 2050 note Z-spread, same method): Oct 2024 outlook revision window +14.6 bp (Oct 17 to 31, 2024); Jul 2025 S&P A+ window -6.2 bp; Nov 2025 Moody's window -1.1 bp; Jun 2025 Q4 FY25 window -14.5 bp; Dec 2025 Q2 FY26 window +1.0 bp. A move of +14 bp is inside Nike's own history. Whole-sample range of the 2050 Z-spread: 33 bp (Nov 30, 2023) to 113 bp (Apr 9, 2025, tariff shock).

**Ratio to the index.** Nike 2050 Z-spread divided by ICE 15+ year OAS is 0.77 on Oct 14. That ratio was 0.77 to 0.80 in Nov 2024 to Apr 2025 and Mar 2026, when Nike was AA-/A1 or A+/A1. It was 0.28 to 0.34 in Nov to Dec 2023. So the Oct 2026 level is not a new high for the ratio; the spread is back where it was in 2024 to 2025. ICE data on FRED only reaches Oct 16, 2023, so earlier ratios are unavailable.

---

## 6. Nov 1, 2026 note and new issuance

- **Status (OPENED, EDGAR index via data.sec.gov, filings listed to Oct 5, 2026): not yet due.** $1.0B 2.375% matures Nov 1, 2026, 17 days after Oct 15. Current portion of long-term debt is $2,000M at Aug 31, 2026 (Q1 FY27 10-Q p. 3 balance sheet, OPENED). No 8-K or other filing reports repayment or a tender; none is required.
- **New issuance: none.** The only Nike prospectus filings are 424B2/424B5/FWP in Oct 2015, Oct 2016 and Mar 2020 (the 2030/2040/2050 notes), and S-3ASR shelves in 2016, 2019, 2022 and Jul 17, 2025. No 424B or FWP since Mar 2020 (data.sec.gov submissions, OPENED, 1,000 most recent filings plus listed older files only partly checked; the recent list ends Oct 5, 2026 with a Form 144).
- **8-Ks in the window:** Mar 9, 2026 8-K (Items 1.01, 1.02, 2.03): entry into a $1B 364-day credit agreement maturing Mar 5, 2027, expandable to $1.5B (OPENED). Oct 1, 2026 8-K: Items 2.02, 2.05, 9.01 (Pace, about $1.0B of charges; OPENED). Neither is a debt issue.
- **Market signal for the Nov 26 note:** clean price 99.78 on Oct 14. Dirty price 100.86 against a final payment of 101.19 implies about 6.7% annualized for 18 days, against a 1-month bill of 4.11%. A 0.1 point quote error is worth about 200 bp annualized at this horizon, so the number is not informative; no default signal. (DERIVED)
- **Likely path** (my inference, not a source fact): repay from cash. Reasons: cash and short-term investments of $8.4B, no CP drawn, S&P expects repayment from cash (REPO note 18). The Mar 27, 2027 $1.0B note is the next maturity.

---

## 7. Alternatives considered and ruled out

| Alternative explanation of the Oct 2026 widening | Test | Result |
|---|---|---|
| Rates, not credit | Z-spread removes the Treasury curve; Treasury yields fell 11 bp Sep 30 to Oct 14 on the 2050 maturity | Ruled out: spread rose while rates fell |
| Market-wide credit move | ICE 15+ OAS 102 to 102, BBB 103 to 103, A 72 to 70 | Ruled out |
| Sector move (apparel/footwear credits) | Peers same window: RL -3/+12, TPR -2/+6, PVH +6, VF +9, UA -9 | Partly: sector mixed to slightly wider; Nike at top of range. Not fully separable |
| Quote noise, stale prices | 2050 daily sd 4.5 bp, 9-day sd 7.2 bp, bid-ask 5 to 12 bp; all six long bonds moved the same direction | Cannot be fully ruled out for any single bond; consistent direction argues against pure noise |
| Refinancing or liquidity risk | $8.4B cash vs $2.0B maturities in 5 months; no maturities Mar 2027 to Mar 2030 (REPO FY26 10-K p. 70) | Ruled out as the driver; no evidence of stress |
| Forced selling after downgrade | S&P A is still index-eligible; Oct 2 to Oct 5 change +1.3 bp | Ruled out |
| Cash-burn expectation (S&P: about $1.2B a year burn, REPO FCF cover 0.87x to 1.07x) | Consistent with magnitude: a one-notch change within A prices at roughly the 11 bp AA to A gap (ICE A 70 vs AA 59, DERIVED) | Surviving explanation, but cannot be separated from the guide cut because the two events are four days apart and the S&P report is based on the guide |

What would separate the guide cut from the downgrade: TRACE institutional prints on Oct 2 versus Oct 5 for the 2030 and 2050 CUSIPs (US654106AK94, US654106AM50). Not obtainable free (see 8).

---

## 8. Routes tried (nothing reported "inconclusive" before five distinct routes)

| # | Target | Route | Result |
|---|---|---|---|
| 1 | Nike/peer bond prices, institutional | FINRA Market Data Center / Investments Explorer (finra.org/finra-data), Morningstar finra-markets.morningstar.com | Partial: pages load but the data is JavaScript-rendered; no static query found. blocked |
| 2 | Bond history | api.finra.org otcMarket endpoint | blocked (404, needs authenticated API) |
| 3 | Bond quotes | MarketWatch, CNBC, Business Insider, Yahoo chart, stooq (com and pl), Boerse Frankfurt, Boerse Stuttgart | blocked (401/403/404/429/connection reset) |
| 4 | Bond quotes | Schwab and Fidelity fixed income pages | blocked or login-gated (landing pages only) |
| 5 | Bond prices and history | finanzen.net bond list, bond page and historic-price POST endpoint, venues BMN, STU, FSE, DUS | **worked** for 8 Nike notes (daily Jan 2023 to Oct 14, 2026), 10 USD peer notes, 8 EUR peer notes |
| 6 | Treasuries | Treasury.gov daily par curve 2023 to 2026; FRED DGS series; Fed H.15 page | worked; Treasury.gov and FRED agree on Oct 13 (5Y 5.00, 10Y 5.21) |
| 7 | Rating-line spreads | FRED ICE BofA OAS (AA, A, BBB, BB, maturity buckets) | worked, but FRED has only 3 years (starts Oct 16, 2023) and rounds to whole bp |
| 8 | Euro benchmark | ECB AAA government spot curve (data-api.ecb.europa.eu) | worked; FRED ICE euro OAS ids tried (BAMLEC0A0RM, BAMLER00OAS and others) not found, blocked |
| 9 | Nike ratings | S&P/Moody's/Fitch sites | S&P disclosure 403; Moody's page 2.7 KB shell; Fitch search page JS shell; blocked |
| 10 | Nike ratings | Reuters via capital.com (OPENED), marketscreener (502), search summaries | worked for S&P Oct 5, 2026; partial for Moody's |
| 11 | Nov 1 note, issuance | data.sec.gov submissions JSON, investors.nike.com mirror (8-Ks Mar 9 and Oct 1, 10-Q Aug 31) | worked |
| 12 | CDS | web search (GlobalCapital CDS level pages, general) | not found; no Nike CDS line in free sources; Markit/ICE and Bloomberg are paid. blocked |
| 13 | Peer ratings | web search for VF, Ralph Lauren, Tapestry, Levi, Under Armour, PVH | partial (VF BB, Tapestry Baa2/BBB, Under Armour BB-/Ba2 from snippets; others not found) |
| 14 | Hanesbrands | finanzen.net list, 7 venues | empty |

Not obtained: TRACE trade-level prices and sizes; CDS spreads; peer ratings at source; Fitch status confirmed at source; S&P's own press release; Moody's current page. What would settle the day-level attribution: a TRACE feed (FINRA data subscription or a Bloomberg/ICE terminal) for CUSIPs US654106AK94, AL77, AM50 on Sep 30 to Oct 14. Settling peers' ratings: each issuer's latest 10-K or 8-K, or the rating agency pages.

---

## 9. Limits of the method (stated so the verdict is not overread)

1. German retail venue quotes are indicative and stale on some days (the 2027 note had 2 distinct prices in 20 days; the 2030 note 11). Long bonds are more active (16 to 19 distinct).
2. The rating lines are ICE BofA index OAS (all maturities) times a maturity factor (bucket OAS divided by all-corporate OAS of 83 bp). This assumes the AA/A/BBB spread gap scales with maturity the same as the overall index. Index buckets are rated-mix, not pure. A pure-A 15+ year line is probably wider or narrower by 10 bp; I cannot check it free.
3. Discount bonds (price 64 to 73) can trade at spreads different from par bonds of the same rating. This could bias the long end either way.
4. Z-spread above the Treasury par curve is not the same as ICE OAS, but Nike's notes have only make-whole calls (no embedded optionality), so the gap should be small.
