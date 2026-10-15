# N2: Expert sell-through statements and a sell-in minus sell-through test for Nike North America footwear

Prepared 2026-10-15. Extends `research_notes/Deep dives Oct 14/D2_north_america.md` (channel shift test, retailer inventory panel) and `data/hunt/running_sellthrough/README.md` (review and stock proxies). It does not repeat them.

Tags: OPENED = I read the page in this session. SNIPPET = search summary only. DERIVED = my arithmetic from OPENED inputs (inputs shown). Expert opinion is labelled OPINION and is never used as the explanation.

Files: `data/niche/N2_expert_statements.csv` (32 statements with date, period, metric, number, source, whether the speaker saw the data), `data/niche/N2_nike_sellin_vs_sellthrough.csv` (quarterly), `data/niche/N2_scenarios.csv` (annual), `scripts/niche/n2_sellin_vs_sellthrough.py` and `n2_build_statements_csv.py` (regenerate both).

## 1. Headline

**No brand-level Nike sell-through exists in free sources. The only Nike-specific US share series is a modelled one (Euromonitor, Nike 40.5% in 2016, 34.1% in 2019, 28.9% in 2025). Circana publishes category growth only. A filing-based test using Circana category growth shows a clear pattern in the quarterly swing, but the cumulative level is not identified.**

1. Pattern that survives every assumption (DERIVED, `N2_nike_sellin_vs_sellthrough.csv`): Nike NA wholesale footwear sell-in grew faster than the US athletic market's dollar growth by about +19 to +25 points in Q2 FY26 (sell-in +24.6% vs market proxy +5.3%), +13 to +18 points in Q3 FY26 and +11 to +16 points in Q4 FY26. In every quarter of FY25 it grew slower than the market, by -0.1 to -17.6 points.
2. In dollars (wholesale footwear, DERIVED, three share-loss scenarios): FY25 sell-in ran $0.6B to $1.0B below partner sell-through (Nike shipped less than partners sold, a destock), FY26 ran $0.8B to $1.1B above. Net FY25 plus FY26: -$0.2B to +$0.5B. So the FY26 wholesale surge is largely a refill of the FY25 shortfall. The sign of the net cumulative position cannot be fixed from free data.
3. Real sell-through datum that is not an estimate: NIKE Direct NA footwear (own stores and nike.com, estimated by applying the NA footwear share to Direct) fell about 12% in calendar 2025 (DERIVED, $6,428M to $5,656M) against an athletic market proxy of about +4.6%. Direct is where Nike controls sell-through, and it lost roughly 16 points of relative share in one year. Wholesale-partner sell-through of Nike cannot be observed.
4. Level of share: not pinned. Nike retail-equivalent NA footwear (about $18B to $21B in CY2024 at wholesale-to-retail ratios of 0.60 to 0.50, DERIVED) divided by a Circana-based athletic market gives 33% to 47% depending on the unknown size of performance footwear; Euromonitor says 28.9% on a broader definition. Powell's own 2016 NPD figure (Nike plus Jordan about 60%) versus Euromonitor's 40.5% for the same year shows definitions move the level by about 20 points. Trend, not level, is usable.
5. Smoking gun: **No.** Nothing here decides long or short. It supports "FY26 NA wholesale growth is mostly refill of a FY25 shortfall plus a Q2 FY26 pulse," consistent with D2, and "Nike lost relative share in its own stores in 2025."

## 2. What each expert source gave (full list in the CSV)

| Source | What is public | Nike-specific number? | Saw data? |
|---|---|---|---|
| Circana press releases and Goldstein quotes (C01 to C15) | Quarterly and annual US footwear dollars, units, ASP, by segment (sport lifestyle, performance, running, fashion). Never a Nike figure | No. Only Brooks ~20% of adult performance running (C15) and Brooks and Hoka ~23% each of running all channels, Nike third-largest running seller at ASP $83 (C10) | Yes (Circana staff) |
| Karnan Associates at The Running Event (C11) | Run specialty 12 months to Sep 2025: dollars +3.1%, Nike +35.4% (rank 9 to 8), Hoka -7.4%, Brooks -6.8%, On -19.7% | Growth rate only, no share. One roundup printed Nike +3.5%, unresolved | Yes (Karnan panel) |
| Matt Powell (BCE Consulting, Spurwink River) (P01 to P04) | Opinion: "They already have a smaller share than they had five years ago" (Oct 2024); "stuffing the market" (Feb 2024). 2016 NPD: Nike plus Jordan about 60% | Only the 2016 number | 2016 yes; 2024 unknown, no figure given. OPINION |
| Euromonitor via Hertzman (E01 to E03) | Nike US athletic footwear share 40.5 / 34.1 / 28.9; market CAGR 4.0% 2019-24, 2.9% 2024-30 | Yes, modelled | No. Third-party model |
| YipitData (Y01) | Nike share of spend "about half"; declined in store and online in 2025; no magnitude | Direction only | Yes (vendor), public page withholds numbers |
| Vertical Knowledge via Reuters (V01) | 44% of Nike sneakers marked down in 2024 vs 19.4% in 2022; avg price $79.92 vs $103.61 | Markdown depth, not sell-through | Yes (vendor) |
| Placer.ai (L01 to L03) | Nike stores visits +59% CQ3 2023; negative YoY for eight straight months to Jun 2025; DICK'S visits -6.0% (Q1 25), -2.6% (Q3 25), +2.2% (Oct 25) | Visits to Nike owned stores, direction only after 2023 | Yes |
| SFIA (S01) | Athletic footwear wholesale $24.1B 2025, +7.4%; running $7.1B +7.3% | Industry only; SNIPPET | Yes (manufacturer survey) |
| Nike management (N01, N02) | Running +$1B in five quarters, +5 share points | Claim, market undefined | MANAGEMENT OPINION |

Circana universe warning (DERIVED): quarterly totals are $9.1B (Q1 24), $10.2B (Q2 24), $10.5B (Q3 24) and $19.3B (Q1 25), while annual totals are $89.2B (2024) and $90B (2025). Q2 24 is described as wholesale data excluding brand DTC. Levels from different releases are not comparable; only growth rates within a release are used.

## 3. The best-possible share series

What can be built: a share index, not a level. Anchors: Euromonitor 40.5% (2016), 34.1% (2019), 28.9% (2025). Average relative share loss 2019 to 2025 = (28.9/34.1)^(1/6) - 1 = -2.7% per year (DERIVED). Nothing exists for 2023 or 2024 in free sources. Units: Circana publishes no athletic unit growth; total footwear units were -1% (Q3 25), -2% (H1 25), low single digits down (2025), and running units +4% (12m to Sep 2025) and +13% (H1 26). Nike NA footwear units (10-Q and 10-K, OPENED): FY24 -7%, FY25 -10%, FY26 +6% (D2), so units fell about 11% FY23 to FY26 against a total-footwear unit base down a few points. The unit share trend is down but cannot be quantified for athletic footwear.

| Test | Result |
|---|---|
| T1 Euromonitor vs filings. Euromonitor implies Nike US retail value index 2019 to 2025 = (28.9/34.1) x 1.04^5 x 1.029 = 1.061 | Filings imply 1.25 to 1.27: NA footwear revenue CY2025 $12,997M vs CY2019 proxy $9,687M (mean of FY19 and FY20), times a retail-equivalent mix adjustment (Direct share 31.6% to 43.5%, wholesale at 0.50 to 0.60 of retail). Gap about 19 to 21 points |
| T2 Circana level. Nike retail-equivalent CY2024 $18.2B to $20.6B vs Circana sport lifestyle $31B plus performance $12.7B to $25B | 33% to 47%. Performance total is not published; $12.7B comes from the Q1 24 leisure to performance ratio (4.4 : 1.8) |

T1 does not close. Surviving explanations: (a) Euromonitor share is a model with its own price basis and may not track Nike's DTC mix; (b) Nike NA includes Canada and the FY19 to CY2019 calendar proxy is crude; (c) Nike sell-in outran sell-through cumulatively by roughly 15 to 20 points of base. Ruled out: market CAGR misuse (2019-24 4.0% used, 2025 at 2.9%); Converse (excluded from NA footwear, reported as its own segment). Not separable with free data. What would decide: Euromonitor methodology note, or Circana brand-level Nike dollars (paid).

## 4. Sell-in minus sell-through by quarter (DERIVED)

Method. Nike fiscal quarter n maps to calendar quarter n+2 (two of three months overlap). Market proxy = 0.71 x sport lifestyle growth + 0.29 x performance growth (weights from Q1 24 Circana dollars). Gaps in the published growth (marked ASSUMED in the script): sport lifestyle in H2 2024 set to +5.5 and Q4 25 to +5 so that annual figures (+3, +4) are met; Q1 and Q2 26 sport lifestyle set to -1 and -2 (sign reported, size not). Nike wholesale footwear = NA footwear revenue x (NA wholesale / NA total) per quarter, assuming footwear and apparel share the channel mix. Partner sell-through growth = market growth plus a relative Nike share change of 0, -2.7 or -5% per year. Excess = wholesale sell-in growth minus that, times the prior-year-quarter base. Annual sums of the excess equal the change in the annual (sell-in minus sell-through) flow versus the prior year.

| Nike quarter | NA footwear $M | Units YoY | Wholesale fw YoY | Market proxy | Excess, 0% share loss ($M) | Excess, -2.7% ($M) | Excess, -5% ($M) |
|---|---|---|---|---|---|---|---|
| Q3 FY24 | 3,460 | +7% | +6.0% | +1.0% | +79 | +122 | +158 |
| Q4 FY24 | 3,587 | n/d | +0.8% | +0.9% | -1 | +52 | +97 |
| Q1 FY25 | 3,212 | -15% | -13.7% | +3.9% | -335 | -282 | -236 |
| Q2 FY25 | 3,236 | -6% | -7.6% | +4.8% | -240 | -185 | -139 |
| Q3 FY25 | 3,132 | -8% | -3.4% | +1.9% | -87 | -41 | -2 |
| Q4 FY25 | 3,104 | n/d | -11.2% | +5.6% | -329 | -273 | -225 |
| Q1 FY26 | 3,219 | +5% | +6.5% | +5.6% | +15 | +62 | +102 |
| Q2 FY26 | 3,542 | +14% | +24.6% | +5.3% | +347 | +398 | +441 |
| Q3 FY26 | 3,326 | +4% | +13.8% | +0.7% | +211 | +254 | +292 |
| Q4 FY26 | 3,230 | n/d | +11.2% | +0.6% | +185 | +233 | +273 |
| Q1 FY27 | 3,259 | +2% | +8.0% | not yet published | n/a | n/a | n/a |

Annual sums: FY25 -991 / -781 / -602; FY26 +758 / +947 / +1,108 (wholesale footwear $M). Q2 FY26 is the single clearest pulse, matching D2's $690M of NA total wholesale above run-rate. NA footwear units +14% in Q2 FY26 against ASP -5 points ("channel mix", 10-Q) fits sell-in, not a price-led story.

Annual scenarios (`N2_scenarios.csv`, base CY2023 assumed neutral, which is questionable because FY24 units were -10% and -17% in Q1 and Q2): CY2025 cumulative sell-in minus sell-through ranges from -$778M (no share loss, high market) to +$596M (-5% per year, low market). Sign not identified.

### Alternatives for the FY26 wholesale surge, with what rules out or keeps them
| Explanation | Verdict | Evidence |
|---|---|---|
| Refill after FY25 under-shipping | KEEPS, largest | FY25 excess -$0.6B to -$1.0B; FY26 +$0.8B to +$1.1B; net -$0.2B to +$0.5B |
| Channel shift from Direct to wholesale | KEEPS (D2) | Direct footwear est. -12% CY2025; wholesale share of NA rose 51.4% to 59.2% |
| Genuine partner sell-through gain | WEAK | Circana market proxy only +0.6% to +5.6%; Nike would need share gain, while Y01 (YipitData) says Nike lost share in 2025; Karnan shows Nike +35.4% in run specialty only, a small channel (run specialty total +3.1%) |
| Price | RULED OUT | ASP -5 points in Q1 and Q2 FY26 per 10-Qs |
| Currency | RULED OUT | NA reported equals currency-neutral (D2) |
| Real fill beyond refill | CANNOT SEPARATE | Needs partner inventory by brand; D2 shows tracked retailer inventory +11.3% Aug 2025, +4.5% Aug 2026 |

## 5. What this does not show
- It does not show channel stuffing. Cumulative level is unidentified and the market proxy has about +/-2 point error per quarter (assumed gaps above).
- Circana excludes brand DTC, so the market proxy compares to wholesale only. Nike's Direct is compared informally.
- Q1 FY27 wholesale footwear +8.0% has no matching Circana quarter until the Q3 2026 release (about November 2026).

## 6. Routes tried (rule: five genuinely different routes before calling anything inconclusive)

| # | Target | Route | Result |
|---|---|---|---|
| 1 | Circana Nike brand share | Circana press page and posts (Q1 26, 2023 styles) | WORKED for category data, no brand |
| 2 | same | SGB, FN/Yahoo, WWD, Sourcing Journal, MR Magazine, SGI Europe summaries (12 pages) | WORKED for category data; WWD pages 307-redirect to a paywall bot (tollbit), not followed |
| 3 | same | Goldstein bylined piece in Running Insight (Nov 2025) | WORKED, no brand share |
| 4 | same | Karnan/Circana TRE session (Dec 2025) | WORKED, best brand-level data found (growth, not share) |
| 5 | same | Retailer side: DICK'S Nike 25% of merchandise costs (Dow Jones snippet) | PARTIAL (sell-in, not sell-through) |
| 6 | same | Third-party model: Euromonitor via Hertzman | WORKED, modelled share |
| 7 | same | Vendor panels: YipitData, Vertical Knowledge | PARTIAL, direction and markdown only |
| 8 | same | Brand-level Circana Q3 2024 and Q4 2023 | NOT FOUND (no Nike mention in any opened release) |
| 9 | Powell Spurwink posts | WebSearch "Spurwink substack Matt Powell" | BLOCKED, no publication found |
| 10 | same | Direct fetch spurwink.substack.com, /archive, /feed, spurwinkriver.substack.com | BLOCKED, HTTP 404 |
| 11 | same | spurwinkriver.com | BLOCKED, HTTP 403 |
| 12 | same | Substack publication search API for "spurwink" and "matt powell footwear" | BLOCKED, empty results |
| 13 | same | r.jina.ai proxy, archive.ph, web.archive.org, Common Crawl index, LinkedIn profile URL | BLOCKED (404 passthrough, connection reset, HTTP 999 wall) |
| 14 | same | Bing HTML scrape | BLOCKED (garbled, unrelated) |
| 15 | same | Podcast and conference pages (Marketscale "What Just Happened?", Switchback bio, Classic Kicks) | PARTIAL: confirms Spurwink River LLC; podcast gives "about 40% of US athletic shoe sales in physical stores" (SNIPPET, undated) |
| 16 | same | Press quotes (Front Office Sports, Reuters) | WORKED for two opinion quotes, no share figure |
| 17 | Earnest, Bloomberg Second Measure, Consumer Edge | WebSearch for public Nike vs Hoka vs On charts | BLOCKED/NOT FOUND (only YipitData page surfaced) |
| 18 | Placer.ai Foot Locker visits | placer.ai site search results; Anchor articles | PARTIAL: Nike and DICK'S figures, no Foot Locker visit series |
| 19 | SFIA | SFIA newsletter PDF (binary, no text) and trade summaries | PARTIAL, SNIPPET; report paywalled |
| 20 | Running USA, Running Insight brand share | Running Insight article opened, Formula4 articles | PARTIAL: no Nike share in the public articles |

A mattpowell.substack.com feed exists but is a 2020 empty "coming soon" stub of unconfirmed ownership; not used. No email address was used in any request.

## 7. What would settle it, and how to get it
1. Circana Retail Tracking Service brand-level dollars and units for Nike, Jordan and Converse by quarter (paid; ask the Refinitiv/Circana sales desk or a sell-side subscriber). Gives the sell-through series directly.
2. Euromonitor Passport US athletic footwear brand shares 2019 to 2025 by year and methodology (paid).
3. Nike wholesale footwear units and ASP by region (not disclosed; ask at Investor Day, Nov 16 to 17).
4. Circana Q3 2026 release (about November 2026), the first quarter to match Nike Q1 FY27.
5. Retailer 10-K Nike share-of-purchases series for DICK'S and Foot Locker (fiscal 2025 10-Ks, March 2026) to cross-check wholesale shipments.
