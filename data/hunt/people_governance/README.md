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
