# people_governance: insiders, institutions, short sellers, votes and talent at Nike (NKE)

Pulled 2026-10-14. All sources are free and need no login. SEC requests used the User-Agent "NikeCaseCompResearch/1.0 research-contact@example.org" (a placeholder, no personal data). Every pull script is in `scripts/` and re-runs from the files in `raw/`.

This folder adds to, and does not repeat, `data/flows/` on branch claude/wonderful-franklin-u31n4e (Form 4 table 2024 to 2026, 13F panel Dec 2024 to Jun 2026, FINRA short interest) and `data/hunt/risk_short_interest/` (short interest for about 60 consumer stocks, daily short volume Oct 2025 to Oct 2026).

## Tidy files

| File | What it is | Rows | Source |
|---|---|---|---|
| `insider_open_market_peers_2006_2026.csv` | Every open-market buy (P) and sell (S) by insiders at Nike and 29 apparel, footwear and retail peers, 2006 Q1 to 2026 Q3, deduplicated | about 32k | SEC Insider Transactions Data Sets, https://www.sec.gov/data-research/sec-markets-data/insider-transactions-data-sets (83 quarterly zips, filtered by ticker; zips not kept) |
| `nke_insider_yearly_2006_2026.csv` | Nike insider buyers, sellers and dollars by year | 21 | derived from the file above |
| `insider_cluster_events.csv` | Insider purchase clusters (2+ insiders, $250k+, 60 days) at peers, with forward excess return vs SPY | 69 | derived; prices from `prices_peers_2006_2026.csv` |
| `nke_10b51_plan_adoptions_2023_2026.csv` | Every Rule 10b5-1 plan adopted by Nike officers and directors (Reg S-K Item 408 text in 10-Q and 10-K) | 13 | Nike 10-Q and 10-K filings Sep 2023 to Oct 2026 (URLs in the file) |
| `nke_say_on_pay_2015_2026.csv` | Say-on-pay votes each year, with support from all votes and from Class B only | 12 | Nike 8-K Item 5.07, 2015 to 2026 (`raw/nke_8k/`) |
| `nke_director_votes_2015_2026.csv` | Votes for and withheld for every director | about 140 | same |
| `nke_13f_holder_panel_2018_2026.csv` | Every 13F filer holding NKE each quarter, 2018 Q1 to 2026 Q2 (shares, put and call shares, a rough class tag) | about 70k | 13f.info JSON, https://13f.info/data/cusip/654106103/{year}/{q} |
| `nke_13f_quarterly_flows_2018_2026.csv` | Per quarter: holders, new positions, exits, buyers vs sellers, put/call ratio, net shares by holder class | 33 | derived |
| `peer_13f_filings_by_quarter.csv` | Number of 13F filings holding each of 59 consumer stocks, 2014 to 2026 | about 2.9k | 13f.info CUSIP summary pages |
| `breadth_event_panel.csv` | Ownership breadth change (yoy, minus cross-section median) and forward excess returns, 59 stocks, 2017 to 2026 | about 2.1k | derived |
| `sec_fails_to_deliver_2019_2026.csv` | Daily fails to deliver for NKE, DECK, LULU, UAA, SKX, VFC, CROX, ONON, BIRK, FL | about 8.3k | SEC FTD files, https://www.sec.gov/data-research/sec-markets-data/fails-deliver-data (Jan 2019 to Sep 15, 2026) |
| `finra_short_volume_daily_2019_2026.csv` | FINRA Reg SHO daily short SALE volume, NKE and peers, Jan 2019 to Oct 13, 2026 | about 12k | https://cdn.finra.org/equity/regsho/daily/CNMSshvolYYYYMMDD.txt plus the existing risk_short_interest file |
| `nke_si_vs_short_volume_ratio.csv` | Each short interest period: SI change vs short volume ratio | 185 | derived |
| `nke_borrow_fee_ibkr_snapshot_2026-10.csv` | Interactive Brokers borrow fee and shares available, Oct 3 to 12, 2026 | 15 | chartexchange.com/symbol/nyse-nke/borrow-fee/ (page shows only the last 15 changes) |
| `efts_alumni_appointments_by_year.csv` | Other companies' 8-K Item 5.02 filings that say someone worked "at Nike" (and at 6 comparison companies), by year | 84 | EDGAR full-text search, https://efts.sec.gov/LATEST/search-index |
| `efts_nike_alumni_8k_hits.csv` | The individual filings behind the Nike count | 85 | same |
| `talent_moves_2024_2026.csv` | Named moves of Nike executives to rivals, and key hires into Nike | 9 | 8-Ks (opened) and news (search snippets, marked) |
| `blind_reviews_peers.csv`, `blind_ratings_by_year.csv` | Public Blind employee review headers (rating, date, role, status) for Nike, adidas, lululemon, Under Armour | 721 | https://www.teamblind.com/company/Nike/reviews?page=N (public list pages) |
| `prices_peers_2006_2026.csv` | Daily close and adjusted close for 27 tickers plus SPY | about 112k | Yahoo chart API |

`data/people_events.csv` (repo root data folder) gained one row: John W. Rogers Jr. retiring from the board at the 2026 annual meeting (8-K filed 2026-06-18).

## Known gaps and caveats

- Insider data sets do not flag 10b5-1 plans; `data/flows/insider_transactions_2024_2026.csv` does for 2024 to 2026. Pre-2024 Nike buys are tiny, so this does not change the history.
- Insider cluster study: price history is missing for delisted SKX, FL, HBI (survivor bias toward stronger names). Events overlap in time, so the n overstates independent evidence.
- 13f.info: the Vanguard split into several CIKs in 2026 Q1, BlackRock's CIK change in 2024 and Norges Bank's late Q1 2026 filing make CIK-level flows noisy for the largest holders. Holder counts and new/exit counts are robust to this; share flows for "index" holders are not. The class tags (hedge_or_trading, index_bank_pension, other_active_adviser) are name regexes and rough. 2026 Q3 13Fs are due Nov 14, 2026 and are excluded.
- Breadth is a count of 13F filings, so it moves with the number of small advisers. The breadth test subtracts the cross-section median each quarter to remove that.
- FINRA short volume is short SALE volume, mostly market-maker activity, not short interest.
- Borrow fee history beyond 15 changes is not public without an account (iborrowdesk.com was unreachable; see blocked list).
- Blind: only review headers are public; pros and cons text is visible only on some pages, so text shares are not comparable over time. Sample sizes after 2024 are small (22 Nike reviews in 2026).
- Talent moves from news are search snippets unless marked "opened".

## Blocked or not usable

openinsider.com (connection reset), iborrowdesk.com (connection reset / empty reply), fintel.io (403), glassdoor.com (403), indeed.com reviews (401), comparably.com (403), capitoltrades.com (429), kununu (404), chartexchange borrow fee history (only last 15 rows in page; CSV export is client-side), LinkedIn (login wall, not attempted), web.archive.org (reset in earlier sessions, not retried). secform4.com, whalewisdom.com, stockzoa.com and quiverquant.com answered 200 but duplicate SEC data already pulled directly.

## Checker review

Checked 2026-10-14 by a second agent. Raw samples were re-pulled from the original sources (SEC placeholder User-Agent, no personal data) into a scratch folder, compared with the files here, and every test script was re-run.

### Re-pulls (sample vs this folder)

| Dataset | Re-pulled | Result |
|---|---|---|
| Insider open-market file (Nike rows) | All 70 Nike Form 4 XMLs filed 2025-10-01 to 2026-10-14 from EDGAR (submissions JSON + Archives) | All 9 purchases (Knudstorp, Cook x2, Swan x3, Hill x2, Rogers) and all 2026 S rows match on date, shares and price. No duplicates (0 on exact and on key columns). Hill's Apr 13, 2026 buy is kept once but from the 4/A (filing date 2026-04-22) rather than the original Form 4 filed 2026-04-14; harmless for counts. |
| 10b5-1 plans | Nike 10-Q filed 2026-10-02 (Item 5) | Holds: no director or officer adopted or terminated a plan in the quarter to Aug 31, 2026. Plans adopted Sep 1 to Oct 14 are not yet disclosed. |
| 13f.info holder JSON | 2021q4, 2025q4, 2026q1, 2026q2 | Byte-level row counts identical (2609, 2231, 2070, 1904 rows). Distinct CIKs match the panel. Capital World +21.6M, Wellington -16.1M, JPMorgan -12.9M, Arrowstreet +5.6M, Marshfield +4.3M, Jupiter Topco +5.0M, RenTech +3.8M all reproduce. |
| Say-on-pay and director votes | 8-K for 2026 meeting (0000320187-26-000143) and 2020 meeting (0000320187-20-000054) | Exact match (2026: 736,936,017 for / 349,508,277 against; Duckett 310,517,784 withheld = 38.5%. 2020: 671,411,282 / 571,342,132). Class B-only support assumes all Class A shares (280.7M in 2026) voted FOR, which is consistent with Class A director votes being unanimous. |
| FINRA short sale volume | CNMSshvol files for 2021-03-03, 2026-07-15, 2026-10-13 | NKE and LULU match (rounded fractional shares). Oct 1 to 13 volume-weighted SVR 0.494 reproduces. |
| FINRA short interest (used in SI tests) | api.finra.org consolidatedShortInterest, NKE Jul to Sep 2026 | All six prints match (99,243,778 on Sep 30; +20.0, +9.8, +13.4, +15.8%; days to cover 2.59). |
| SEC fails to deliver | cnsfails202607a/b | NKE rows match (2,357,661 on 2026-07-06). |
| IBKR borrow fee | chartexchange page, Oct 14 | Same 15 rows; latest Oct 14 06:16 still 0.41% and 10,000,000 available (10M is IBKR's display cap, so availability is at least 10M). |
| EDGAR full-text search | "at Nike" 8-K 2021 and 2025 | Same totals (21 and 29 hits); 5.02 counts after own-CIK and adsh de-duplication are consistent. |
| Blind | Nike reviews page 1 | The three newest review titles in the file are on the live page. Newer dates on the page are forum posts, not reviews. |
| Yahoo prices | NKE Dec 18 to 31, 2025 and Oct 7 to 13, 2026 | Closes match to the cent. |

### Re-run tests

All four scripts reproduce their outputs exactly (breadth panel and cluster event file diff to zero lines). What holds and what does not:

1. **Insiders (LONG, weak): holds as weak, but two claims need narrowing.**
   - Holds: 2025 buying $5.96M (4 buyers) and 2026 $2.73M (4 buyers) are 20-year highs.
   - Does not hold as worded: "2026 selling is the lowest in 20 years, so selling is drying up." On a like-for-like Jan to Sep basis, total selling fell from $38.1M (2025) to $2.1M (2026), but all of that drop is Mark Parker. Excluding Parker and the Knights, Jan to Sep selling was $10.1M (2022), $6.8M (2023), $5.5M (2024), $1.8M (2025) and $2.1M (2026): flat vs 2025, not a new low. Many 2026 S rows are same-price sell-to-cover sales on vest dates (Aug 5 at $41.60, Sep 9 at $37.59). Parker's new 165k-share plan (adopted Dec 24, 2025) has produced no sales; a price-limit plan not triggering as the stock fell from about $60 to $35 is an equally good explanation as conviction.
   - New, missed by the hunter: two Form 144 notices by Matthew Friend, now "Former Officer" (ex-CFO), for 12,658 shares ($454k, about Sep 30, under a plan adopted Oct 8, 2025) and 19,572 shares ($658k, about Oct 5, no plan date given). Former officers do not file Form 4, so these are outside the insider data set. This is post-results selling, not buying. It does not change the yearly ranking ($3.2M with these), but it is the only post-Oct 1 insider-type trade on file.
   - Strengthens the "has not worked" side: both Nike buy rounds lost about a third vs SPY. Dec 23, 2025 round: -34.3% vs SPY at 126d (reproduced). Apr 14, 2026 round (suppressed in the cluster file by the one-event-per-180-days rule): NKE -18.5% vs SPY +12.6% over the next 126 trading days, about -31pp.
   - Peer clusters reproduce: n=55, median +7.2% at 126d (31/55), median -3.4% at 252d (22/51). The 252d mean is +19.0%, so the "lost at 12 months" read depends on using the median (right-skewed outcomes). Survivor bias remains (SKX, FL, HBI unpriced).

2. **13F breadth (NEUTRAL, moderate): holds, and can be pushed toward "strong NEUTRAL".**
   - Reproduced: holders 2,073 to 1,926 to 1,739, net entries -147 and -187, NKE rel_breadth -17.2pp.
   - New check, mechanical artifact: Rule 13f lets managers omit positions under 10,000 shares and under $200k. As NKE fell from $63.71 to $41.05, more small positions qualify. Exits that were de minimis eligible at the new quarter-end price were 122 of 295 (2026q1) and 148 of 342 (2026q2), vs 56 to 71 a quarter in 2025q2 to 2025q4. Net entries excluding those exits are -25 and -39: still the two worst since 2018 (prior low -17 in 2022q3), so the drop is real but about four-fifths smaller than the headline. Price-driven quarters (2020q1, 2022q1 to q3, 2024q1 to q2) always show the same pattern.
   - Predictive test: a Fama-MacBeth style rank correlation of rel_breadth with forward excess return, quarter by quarter, is -0.013 (t -0.31, 37 quarters) at 63d, -0.015 (t -0.34) at 126d and -0.021 (t -0.51) at 252d. There is no signal. The universe is 56 survivors (no delisted names).
   - Selective reporting: the hunter cites "fell >25% and big breadth loser" 252d median -6.5% vs -20.2% (LONG-looking), but at 126d the same split is -6.7% vs -0.6% (SHORT-looking). The two horizons disagree, which supports NEUTRAL.
   - Label caveat: "hedge or trading added a net 24.1M shares in Q2, the largest in the series" includes Marshfield Associates (+4.3M, a long-only concentrated value manager) and Jupiter Topco (+5.0M, type unknown), both tagged by the name regex. At least 4.3M of the 24.1M is value-investor buying, not hedge or trading flow.

3. **Short interest (SHORT, weak): holds.**
   - SI run persistence reproduces: after 4 straight rises the next print rose 47.0% of the time (n=653) vs a 49.8% base rate, across 62 tickers.
   - SVR vs SI change correlation is 0.079 (0.047 after removing a 12-period rolling mean). Note that the NKE SVR has trended up (yearly medians 0.28 in 2019, 0.46 in 2025), so "93rd percentile since 2019" overstates it; since 2024 it is the 83rd percentile.
   - Correction: the FTD peak is 2,518,475 shares on 2025-10-20 (7.4% of the Oct 15, 2025 SI of 34.2M), not 2.36M in Jul 2026. The Jul 6, 2026 peak is 3.3% of the Jun 30 SI, so "even the peaks are under 2.5% of SI" does not hold. Yearly FTD means are over days with a fail record, not all trading days, which inflates them. The conclusion (not tight, borrow easy) still holds: fee 0.41%, at least 10M shares available on Oct 14.

4. **Governance and talent (SHORT, weak): holds as weak.**
   - Votes reproduce exactly. Blind: 2021 to 2023 mean 3.69 (n=355) vs 2024 to 2026 mean 3.23 (n=117); permutation p < 0.0001, so the drop is not noise, though Blind skews to tech staff and layoff periods.
   - Alumni count: 13 in 2025 holds, but 2026 YTD is 5 by Oct 14 (about 6.5 annualized), below every year from 2021 to 2025. Many 2025 hits (Marriott, Expeditors, Lithia, Papa John's, Yum) are long-ago alumni, not recent departures. Heidi O'Neill retired from Nike in 2025 before joining lululemon in 2026. The "exodus" reading is weaker than stated.

### Net

No dataset failed a re-pull. Numbers in the tidy files are accurate. Verdicts after checking: insiders LONG weak (selling "drying up" is one person; both Nike buy rounds lost about 31 to 34pp vs SPY at 126d, which leans the other way); breadth NEUTRAL, moderate to strong (artifact partly mechanical, zero predictive IC); short interest SHORT weak (FTD peak wording corrected); governance SHORT weak (alumni count is falling in 2026).
