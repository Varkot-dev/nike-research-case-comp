# W9: Nike advertising activity vs peers from ad transparency data, and what demand creation does to the margin bridge

Prepared 2026-10-16 (all pages accessed 2026-10-16 unless stated). Extends `research_notes/thesis_tests/marketing_payoff.md` (elasticities, 33-year history) and `research_notes/Nike decline root cause analysis/marketing_shift.md` (shift away from brand, segment table). Not repeated here. Overlap with `data/hunt/marketing_athletes/README.md` (Meta and Google blocked on 2026-10-14) is acknowledged: this note re-tests those routes, adds iSpot, adds quarterly and segment filings arithmetic, and runs the lift tests.

Labels: **OPENED** = I read the page or filing myself. **SNIPPET** = search-result summary only. **DERIVED** = my arithmetic, inputs named. No logins, no bot-protection bypass, no email in any request.

## 1. Bottom line

1. **Smoking gun: no.** The ad libraries that would give a direct activity count by advertiser (Google Ads Transparency Center, Meta Ad Library, LinkedIn, TikTok) are either blocked behind CAPTCHA, JavaScript challenge, Cloudflare or signed requests, or rate limited (section 3 and `ad_library_access_routes_log.csv`). The one source that opened (iSpot public brand pages) shows airing counts and rank but masks dollars. What does open says Nike's measurable ad activity is **not rising faster than peers** and **shows no lift in any demand signal in this repo**.
2. **Nike's own filings are the best spend measure, and they say the ratio rose because revenue fell, not because dollars surged.** Demand creation (DC) was $4,285M (FY2024), $4,689M (FY2025), $4,754M (FY2026, +1.4% reported; the 10-K says currency added about 2 points, so about -1% in constant currency, OPENED, FY2026 10-K p. 36) and $1,252M in Q1 FY2027 (+5%). Trailing four quarters to Q1 FY2027: DC $4,818M on revenue $45,891M = 10.50% (DERIVED). Versus FY2024 (8.34%) that is 216 bp of revenue, or **$991M a year**, equal to **25.7% of trailing EBIT of $3,853M** (DERIVED, `demand_creation_margin_sensitivity.csv`).
3. **Peers are growing marketing dollars faster than Nike**: FY2026 Nike +1.4% vs Deckers (HOKA plus UGG) +14.7%, lululemon (FY2025) +14.0%, adidas (2025) +8.4% in EUR, On (2025) +36.1% in CHF; only Under Armour fell (-8.7%) (DERIVED, `peer_marketing_growth_vs_nike.csv`). In the latest quarter Nike's DC was +5% against adidas Q2 2026 marketing and point-of-sale +30% (adidas figure from `marketing_payoff.md`, a prior OPENED worldfootwear.com read; not re-opened here).
4. **Mix of the spend moved to TV and away from paid social in the World Cup window** (Digiday citing AdClarity, 2026-07-10, OPENED via WebFetch): Nike TV share of its media mix went 42.9% to 50% in May to June 2026; Nike "reduced spending on Meta and TikTok" while adidas raised paid social. On iSpot linear TV, Nike ran its spot 80 times in the first part of the tournament (second only to Home Depot) vs adidas 32 (rank 30).
5. **Lift: none measurable.** US share of brand search for Nike (Google Trends, repo) averaged 46.6% in 2023, 40.6% in 2024, 38.3% in 2025, 38.1% in 2026 Q1 to Q3 while DC rose from 8.3% to 10.5% of revenue (DERIVED from `data/altdata/gtrends_quarterly_share_of_brand_search_pct.csv`). nike.com US visits were -12.2% YoY in Aug 2026 vs adidas.com +9.4% (Semrush, repo `data/hunt/web_traffic/`). Correlations of DC changes with search, search share and revenue growth at 0 to 3 quarter lags are negative or near zero (section 6).
6. **Margin bridge:** each 100 bp of DC is $459M on trailing revenue and about 12% of trailing EBIT (DERIVED). Q1 FY2027 shows the mechanism: DC +$64M absorbed 38% of the $170M operating-overhead saving (DERIVED, 10-Q). Management says SG&A stays down year over year in FY2027 (Q1 FY2027 call, OPENED, `data/hunt/earnings_calls/transcripts/Q1FY27.txt`), so DC growth is being funded by overhead cuts, not by gross profit.

## 2. Nike demand creation by quarter, share of revenue, and segment detail (item 5)

Full table: `data/wave3_w9/nike_quarterly_demand_creation_ratio.csv` (Q1 FY2019 to Q1 FY2027; DC, revenue, gross profit, EBIT, overhead, DC share, YoY, bp change). Source: `data/nike_filing_facts.csv`, each row tied to a 10-Q, 10-K or earnings-release exhibit (OPENED earlier by the filings session; Q1 FY2027 10-Q re-opened by me at investors.nike.com mirror, accession 0000320187-26-000193).

| Quarter | DC $M | DC % revenue | DC YoY | Revenue YoY | DC % chg vs prior-year quarter (bp) |
|---|---|---|---|---|---|
| Q1 FY2025 | 1,226 | 10.6% | +14.7% | -10.4% | +232 |
| Q2 FY2025 | 1,122 | 9.1% | +0.7% | -7.7% | +76 |
| Q3 FY2025 | 1,088 | 9.7% | +7.6% | -9.3% | +152 |
| Q4 FY2025 | 1,253 | 11.3% | +14.8% | -12.0% | +264 |
| Q1 FY2026 | 1,188 | 10.1% | -3.1% | +1.1% | -44 |
| Q2 FY2026 | 1,273 | 10.2% | +13.5% | +0.6% | +116 |
| Q3 FY2026 | 1,090 | 9.7% | +0.2% | +0.1% | +1 |
| Q4 FY2026 | 1,203 | 11.0% | -4.0% | -1.1% | -33 |
| Q1 FY2027 | 1,252 | 11.2% | +5.4% | -4.3% | +103 |

Read (DERIVED): FY2025 was the step-up year (+$404M, ratio +178 bp, of which most is the revenue denominator: DC at FY2024 dollars on FY2025 revenue would already be 9.25%). Since Q1 FY2026 DC has moved sideways in dollars ($1,090M to $1,273M a quarter). The ratio in Q4 FY2026 and Q1 FY2027 (11.0%, 11.2%) is the highest in the repo series (compare `marketing_payoff.md`).

**Forecast miss, labelled opinion/consensus:** Inside Retail (2025-12-18, OPENED) says CFO Friend in September 2025 forecast "an acceleration of demand creation investment" and that LSEG data expected DC to top $5B in FY2026. Actual was $4,754M, about 5% below that consensus. The $5B number is LSEG consensus, not Nike guidance. Q4 FY2026 DC was -4% on "lower brand marketing" (FY2026 10-K, Q4 release).

**Segment detail, Q1 FY2027 vs Q1 FY2026 (OPENED, Q1 FY2027 10-Q segment tables, pp. 25 to 31):**

| Segment | DC Q1 FY27 $M | DC Q1 FY26 $M | DC change | Revenue change (currency-neutral) | DC % of segment revenue now |
|---|---|---|---|---|---|
| North America | 511 | 442 | +16% | +2% | 10.0% |
| EMEA | 313 | 313 | 0% (mix shifted to key sports events) | -5% | 9.9% |
| Greater China | 88 | 99 | -11% | -26% | 7.5% |
| APLA | 93 | 97 | -4% | 0% | 6.4% |
| Global Brand Divisions | 232 | 203 | +14% | n/a | n/a |
| Converse | 14 | 33 | -58% | -28% | 5.3% |
| Corporate | 1 | 1 | 0% | n/a | n/a |
| Total | 1,252 | 1,188 | +5% | -4% (reported) | 11.2% |

North America arithmetic (DERIVED): DC +$69M for revenue +$107M reported ($5,127M vs $5,020M, `marketing_payoff.md` / refuter table) and gross profit +$101M; segment EBIT +$36M ($1,170M vs $1,134M). In North America 68 cents of each incremental gross profit dollar went to higher DC.

**Fixed-cost floor (DERIVED, caveat):** endorsement contract obligations were about $15.5B at May 31, 2026 with about $1.7B payable within 12 months (FY2026 10-K, OPENED, "including associated marketing commitments"). $1.7B / FY2026 DC $4,754M = 35.8%. Those are minimum guaranteed payments, so at least roughly a third of annual DC is contractually locked, which is why cutting DC quickly to protect margin is hard. The figure is an approximation because the obligation definition includes marketing commitments and expense recognition is not identical to cash timing. The obligation fell 4.3% from $16.2B (FY2025) to $15.5B (FY2026) despite the deal extensions in section 5.

## 3. Ad libraries: what opened and what did not (items 1 to 4)

Route log with every attempt: `data/wave3_w9/ad_library_access_routes_log.csv`. Summary by source:

| Source | Result | What it gave |
|---|---|---|
| Google Ads Transparency Center | BLOCKED today (captcha redirect on the site, HTTP 429 on the RPC); five routes tried (site, RPC suggestions, RPC creatives, WebFetch shell, BigQuery public dataset) | Only the 2026-10-14 prior pull: lifetime ad-count buckets per advertiser entity (`google_ads_lifetime_creative_buckets_2026-10-14.csv`) |
| Meta Ad Library | BLOCKED: HTTP 403 JavaScript challenge; Graph API needs a token (not created, no login) | Nothing direct. EU DSA reach-by-country data is only inside that library, so it could not be read |
| TikTok Ad Library | PARTIAL: page loads, search API is signed ("system busy" 421 on an unsigned call), not pursued | Nothing |
| LinkedIn Ad Library | BLOCKED: Cloudflare 403 | Nothing |
| iSpot.tv | WORKED for airing counts and rank, MASKED for dollars | Table below |
| Press with AdClarity and iSpot figures | WORKED | Digiday 2026-07-10 and MediaPost 2026-07-02 figures (section 1, item 4) |
| Wayback Machine and Common Crawl for history | BLOCKED (connection reset via proxy) | No history |

**Google lifetime ad-count buckets (OPENED 2026-10-14 by prior session, SearchSuggestions RPC; the bucket is the library's own range label):** Nike, Inc. (US) 9,000 to 10,000; Under Armour, Inc. (US) 7,000 to 8,000; Under Armour Europe B.V. 7,000 to 8,000; On AG (CH) 2,000 to 3,000; adidas America, Inc. 2,000 to 3,000; Brooks Sports Inc 1,000 to 2,000; New Balance Athletic Shoe, Inc. (US) 1,000 to 2,000; Skechers U.S.A., Inc 2,000 to 3,000; lululemon Canada 10,000 to 20,000. No Nike regional entity (Europe, China, Japan) appeared in the suggestion results for the query used, so I cannot give a region split; the prior session also saw one Sep 2026 US creatives bucket of 1,000 to 2,000 for Nike. These are lifetime counts, not dated, and **I could not get any history or date range**, so they cannot show a trend (ruled out as a test of "rising faster": no time dimension).

**iSpot public brand pages, trailing 30 days ending 2026-10-16 (OPENED, `ispot_brand_pages_30d_snapshot_2026-10-16.csv`):**

| Brand | National airings (30d) | Spend rank (all advertisers) | Airing rank |
|---|---|---|---|
| Skechers | 4,327 | #243 | #176 |
| New Balance | 536 | #296 | #910 |
| Nike | 282 | #738 | #1,154 |
| Brooks | 76 | #849 | #1,701 |
| adidas | 18 | #1,797 | #2,538 |
| Under Armour | 10 | #1,041 | #2,872 |
| HOKA | 6 | #3,365 | #3,135 |
| lululemon | 3 | #2,680 | #3,468 |

The weekly #1 US TV spender (Progressive) spent an estimated $12.6M in the week (OPENED, iSpot top spenders). Nike ranks #738 for spend in the post-World Cup month: **Nike's US national TV presence in the shoulder month is a fraction of Skechers and New Balance** and ahead of adidas, Under Armour and HOKA. Dollars are masked (placeholders), pages for Jordan, ASICS, PUMA and Converse show creative counts only, and On has no iSpot brand page found. iSpot's weekly window is one point in time; there is no prior-month comparison available (history blocked), so this is a level, not a trend. During the tournament, iSpot reported Nike national TV spend of $6.6M on the Fox networks over June 11 to July 1 (MediaPost, 2026-07-02, OPENED) and Nike share of voice of 1.97% (7th) vs adidas 1.53% (SNIPPET inside search summary, mediapost/ppc.land). $6.6M is about 0.5% of Q1 FY2027 DC ($1,252M), which shows how little of DC measured national linear TV captures (DERIVED).

Ruled out as inferences:
- **Ad count as proxy for spend.** A count of creatives (Google, iSpot "Total Creatives" 351 for Nike vs 455 Skechers) measures creative variety, not dollars or impressions. Not used for spend.
- **Ad libraries as a measure of total DC.** DC includes endorsement contracts, complimentary product, events and retail presentation (Q1 FY2027 10-Q definition). At least about 36% is minimum guaranteed endorsement payments (section 2). Libraries cannot see that.
- **Regional entities.** Spend is booked by entity (Nike, Inc. US vs European and Chinese entities, and agency or retailer co-op accounts). A missing entity makes any one entity's count a floor. I found no Nike regional entity in the available suggestion data, so cross-region comparison is impossible from this source.
- **Agency-run or retailer accounts.** Ads placed by agencies or by wholesale partners (co-op) appear under the agency or retailer, not Nike, so a library undercounts Nike more than a pure DTC brand like lululemon. Direction of bias: understates Nike.

## 4. Is Nike's ad activity rising faster than peers? (long's brand-rebuild claim)

Marketing dollars and intensity, latest two years (DERIVED from filings in `data/marketing/peer_marketing_intensity.csv`, `peer_marketing_growth_vs_nike.csv`; definitions differ, so compare growth within company):

| Company | Latest FY marketing growth | Prior FY | Latest ratio | Ratio change latest yr (bp) |
|---|---|---|---|---|
| Nike (FY2026) | +1.4% (about -1% constant currency) | +9.4% | 10.25% | +12 |
| adidas (2025, EUR) | +8.4% | +12.4% | 12.41% | +41 |
| On (2025, CHF) | +36.1% | +41.3% | 12.49% | +56 |
| Deckers (FY2026) | +14.7% | +23.9% | 9.06% | +39 |
| lululemon (FY2025) | +14.0% | +26.0% | 5.56% | +45 |
| Under Armour (FY2026) | -8.7% | -3.3% | 10.11% | -54 |

Nike's step-up was FY2025 (+9.4%, below adidas +12.4% in 2024 and far below On, Deckers and lululemon in their prior years). Since then Nike's growth in dollars has been the slowest in the group except Under Armour. Intensity rose because revenue fell (FY2025 revenue -9.8%, DERIVED), not because spend outpaced peers. Nike is also not at a spending-intensity extreme: 10.25% vs adidas 12.41% and On 12.49%. The mix shift that is visible (Digiday/AdClarity: more TV, less Meta and TikTok in May to June 2026) points to event concentration around the World Cup, not a broad rise in activity.

## 5. Sponsorship changes 2025 to 2026 and the endorsement obligation (item 6)

Event ledger: `data/hunt/marketing_athletes/endorsement_events.csv` (20 events, prior session; not re-researched). New items found today, all **SNIPPET** (one search, not opened on primary pages; `data/wave3_w9/sponsorship_events_added_2026-10-16.csv`): Wembanyama long-term extension with signature shoe (reported 2026-07-31, KSAT/SI), A'ja Wilson six-year extension (ESPN report, undated in result), US Soccer extended to 2033 (nss-sports.com, undated), South Carolina 10-year deal from 2026-07-01 (already in ledger). Losses already in the ledger: Liverpool to adidas, Penn State and Tennessee to adidas, Mbappe to On (Sep 2026), Portugal to Puma, Tiger Woods.

Disclosed obligation (OPENED, 10-Ks; `data/marketing/nike_endorsement_obligations.csv`): $7.6B (FY2023), $10.6B (FY2024), $16.2B (FY2025, definition widened to include associated marketing commitments), $15.5B (FY2026); within 12 months $1.7B, $1.6B, $1.7B. DERIVED: the 12-month payable is flat at 35.8% of DC while the total fell 4.3%. Filings cannot say whether the decline came from expirations (Liverpool, college deals, Woods) outrunning new signings, or from re-pricing; the Q1 FY2027 10-Q does not repeat the obligations table (checked), so the next datapoint is the FY2027 10-K (July 2027). What would settle it: contract-level data (SportsBusiness Journal, Sportcal) with deal values.

## 6. Does the spend lift any measured demand signal in this repo?

Tests (DERIVED; `dc_vs_demand_signal_correlations.csv`; quarterly, FY2021 to Q1 FY2027, n = 21 to 25; US Google Trends from `data/altdata/gtrends_nike_fiscal_quarter_vs_digital_revenue.csv`):

| Test | Result |
|---|---|
| DC dollar growth vs Nike search growth, lag 0 to 3 quarters | r = -0.04 (lag 0), -0.01 (1), +0.18 (2), -0.17 (3): zero |
| DC dollar growth vs change in Nike share of brand search (pp), lag 0 to 3 | r = -0.13, -0.27, -0.49, -0.55: negative, i.e. more spend preceded a falling share |
| Change in DC share of revenue (bp) vs revenue growth, lag 0 | r = -0.70 (mechanical: ratio rises when revenue falls) |
| Same, lag 1 to 3 | r = -0.39, -0.33, -0.46 |
| Pre/post step-up: US Nike share of brand search, calendar year means | 2023 46.6%, 2024 40.6%, 2025 38.3%, 2026 YTD 38.1% while DC went from 7.9% (FY2023) to 10.5% |
| nike.com US visits Aug 2026 YoY vs adidas.com | -12.2% vs +9.4% (Semrush, `test_nike_vs_peers_semrush_yoy_aug2026.csv`) |

Interpretation, with the confounds named: the negative lagged correlations do not prove spend hurt demand. They reflect that Nike raised spend while demand was already falling (denominator effect and reverse causality documented in `marketing_payoff.md` section C, 6 reasons) and that the sample includes the COVID quarters. What the tests do show is that **no lift appears** at any lag in the signals this repo holds, which is consistent with Lodish et al. ("works in year one or never", in `marketing_payoff.md`). The test that would show lift, a within-quarter jump in search share in the World Cup quarter, is the one positive: Q1 FY2027 (June to August 2026) search yoy +18% and share yoy +1.9 pp (US), the first positive share change in the series since FY2023. This is the only positive reading and it is the event quarter; the Nike performance categories grew (Running double digits, Football double digits, Q1 FY2027 call), but consolidated revenue still fell 4%. If search share in Q2 FY2027 (Sept to Nov 2026) falls back, the World Cup effect was transient. This is the date to watch (Investor Day on Nov 16 to 17 comes right after).

Two or more explanations survive for the Q1 FY2027 search bump and cannot be separated with this data: (a) World Cup event interest that would have lifted the whole category (peer search share moved too: US adidas share 16.3% in 2026 Q3 from 14.8% in Q1, same file), and (b) a Nike-specific return on spend. Data that would decide it: Google Trends by country with a non-World-Cup control (running, basketball queries), and Nike Q2 FY2027 sell-through. Not obtainable today.

## 7. Margin bridge implications (each 100 bp of DC is 100 bp of EBIT margin)

From `demand_creation_margin_sensitivity.csv` (DERIVED; trailing four quarters Q2 FY2026 to Q1 FY2027, revenue $45,891M, EBIT $3,853M = 8.40% margin):

| Counterfactual DC ratio | DC $M | EBIT uplift $M | EBIT margin | EBIT uplift % |
|---|---|---|---|---|
| Actual 10.50% | 4,818 | 0 | 8.40% | 0 |
| FY2017 to FY2019 average 9.71% | 4,456 | +362 | 9.18% | +9.4% |
| FY2024 ratio 8.34% | 3,827 | +991 | 10.55% | +25.7% |
| FY2022 ratio 8.24% | 3,781 | +1,037 | 10.65% | +26.9% |
| FY2021 ratio 6.99% | 3,208 | +1,610 | 11.90% | +41.8% |

Each 100 bp of revenue = $459M of trailing EBIT (11.9% of it); on FY2027 revenue of $42.7B (an illustrative -8%, the guide is "down high single digits") 100 bp is $427M. Revenue lost at constant dollars: to break even on $991M of excess DC at the trailing gross margin of 43.1% (DERIVED: trailing gross profit $19,766M / $45,891M) Nike needs about **$2.3B of extra revenue**; at the long-term elasticity of 0.24 (Sethuraman et al., `marketing_payoff.md`) the extra DC of roughly $530M above FY2024 dollars buys about 2.6% revenue or $1.2B, so the incremental payoff covers roughly half the cost of the FY2024-ratio gap. This is the labelled-arithmetic frame the repo's FY28 bridge (D1) can use.

Implication for the short thesis (opinion, flagged): a lasting FY2027 EBIT margin gap to FY2024-type ratios is about 215 bp, and it only closes if revenue grows into the dollars (DC dollars flat, revenue +8%, closes the gap to 9.7%) or Nike cuts DC. The second path is hard because about 36% is contractual minimums; the first path has no measured lift so far.

## 8. Alternatives considered for "Nike's ad activity rose" and what ruled them out

| Explanation | Test | Result |
|---|---|---|
| Real increase in advertising dollars outpacing peers | Filings growth FY2025 to Q1 FY2027 vs peers (section 4) | Ruled out for FY2026 and Q1 FY2027; true only in FY2025 (+9.4%, near adidas) |
| Denominator effect (ratio rises as revenue falls) | Hold FY2024 dollars, apply to FY2025 revenue | Explains most of the FY2025 ratio rise (9.25% of the 10.13%), DERIVED |
| Currency | FY2026 10-K: currency added about 2 points | FY2026 constant-currency DC about -1% |
| Shift to TV from paid social | Digiday/AdClarity May to June 2026 | Supported (42.9% to 50%) but SNIPPET-level on totals; combined spend only $52.8M, a small slice of $1.25B quarterly DC |
| Event timing (World Cup in Q1 FY2027, Olympics in Q1 FY2025) | Q1 FY2025 +14.7% and Q1 FY2027 +5.4% with `higher investment in key sports events` text in both 10-Qs | Supported; DC step-ups cluster in event quarters |
| Lower brand marketing elsewhere funds events | Q4 FY2026 -4% and Greater China -11%, Converse -58% | Supported: events up, regional brand marketing down |

## 9. What I could not get, and what would settle it

- Google Ads Transparency Center by region, format and date range, and Meta/EU DSA reach by country: **inconclusive after five distinct routes each** (log has 16 rows). To obtain: a human in a normal browser session can export Google Ads Transparency Center advertiser pages and Meta Ad Library CSV reports; or a paid feed (Pathmatics/Sensor Tower, AdClarity, Vivvix); or Refinitiv/university access to MediaRadar. These are in the Refinitiv pull list lane.
- iSpot dollars and a history of the 30-day window: masked and archives blocked; the lead-form gate is not bypassed.
- Peer On Holding on iSpot: no brand page found.
- A contract-level value for the sponsorship changes.

## 10. Files

- `data/wave3_w9/nike_quarterly_demand_creation_ratio.csv`
- `data/wave3_w9/demand_creation_margin_sensitivity.csv`
- `data/wave3_w9/peer_marketing_growth_vs_nike.csv`
- `data/wave3_w9/dc_vs_demand_signal_correlations.csv`
- `data/wave3_w9/ispot_brand_pages_30d_snapshot_2026-10-16.csv`
- `data/wave3_w9/ispot_ad_pages_published_dates.csv` (ad page publish dates, the 24 to 30 most recent ads per brand on the brand page; recency-sorted list, so it is not a rate comparison. 20 of the 24 listed Nike pages were published April to September 2026, consistent with a World Cup creative burst; adidas shows 8 in Q1 2025.)
- `data/wave3_w9/google_ads_lifetime_creative_buckets_2026-10-14.csv`
- `data/wave3_w9/ad_library_access_routes_log.csv`
- `data/wave3_w9/sponsorship_events_added_2026-10-16.csv`
