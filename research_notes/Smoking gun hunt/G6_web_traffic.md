# G6: Did nike.com traffic fall with Digital revenue, or hold while revenue fell? (web traffic hunt)

Pulled and analysed 2026-10-15. Data and scripts: `data/hunt/web_traffic/` (README there lists every file). Extends, does not repeat, `data/hunt/search_attention/` (Wikipedia, Tranco semi-monthly, Reddit) and `data/hunt/apps_digital/` (Play reviews, Semrush overview 6-month history, Similarweb snapshot, HypeStat). Tags: OPENED = page or file read in full this session; SNIPPET = search-result text only; DERIVED = my arithmetic from tagged inputs.

## 0. Correction to the premise

"Nike Digital fell 26% in Q1 FY27" is the **EMEA** figure only. Reported (OPENED, Q1 FY27 10-Q MD&A, nke-20260831.htm, fetched from the investors.nike.com mirror): NIKE Brand Digital **-13%** total (Ex. 99.1: $1.8B vs $2.1B); by segment, currency-neutral: North America **-6%**, EMEA **-26%**, Greater China **-28%**, APLA **-10%**. The test therefore has to run region by region, and I did.

## 1. Headline (DERIVED, Semrush Aug 2026 YoY; Q1 FY27 = Jun to Aug 2026)

| Segment | Reported digital revenue growth (cc) | nike.com visits YoY, Aug 2026 (Semrush) | Implied revenue per visit |
|---|---|---|---|
| Global (reported USD) | -13% | -11.4% (97.45M visits) | -1.8% |
| North America | -6% | -11.4% (US 41.5M, CA 3.0M, weighted) | +6.1% |
| EMEA, 8 countries | -26% | +2.2% (GB alone +34.4%) | -27.6% |
| EMEA ex-GB (DE, FR, IT, ES, NL, PL, SE) | -26% | -6.8% | -20.6% |
| APLA (JP, KR, AU, MX, TW, IN) | -10% | -24.5% | +19.2% |
| Greater China | -28% | not measurable | n/a |

Formula: (1 + revenue growth) / (1 + visit growth) - 1. Files: `test_revenue_per_visit_wedge.csv`, `test_region_semrush_yoy_vs_digital.csv`.

What this says, in numbers:
- **Globally, traffic did not hold.** Visits fell 11.4% against revenue -13%, so revenue per visit moved only -1.8%. The "traffic held while revenue fell" signature is ruled out at the total level.
- **Only EMEA shows the "traffic held, revenue fell" signature**: revenue per visit -21% to -28% on flat-to-slightly-down visits. That is the region where Nike says it cut off-price (call quote, opinion, repo note `emea_converse_jordan.md`: "off-price was down over 50%" and "15-point improvement in full price realization").
- **NA and APLA show the opposite**: visits fell faster than digital revenue (revenue per visit +6% and +19%). That pattern is what a loss of low-intent or promo-driven visits looks like, but it is equally what a real demand loss at the top of the funnel looks like. Traffic alone cannot tell them apart.
- **Company-specific, not category-wide.** Same-month global YoY (OPENED, `semrush_trending_global_2026-08_long.csv`): adidas.com +12.5%, DICK'S +15.2%, ASICS +0.9%, New Balance +0.4%, Puma -5.6%, Under Armour -3.7%, Decathlon +0.2%; median of these seven +0.4% vs Nike -11.4%, a gap of about 12 points. US: Nike -12.2% vs adidas +9.4%, New Balance +2.2%, ASICS +2.1%, Puma -14.9%, DICK'S +15.9%, JD +67.7% (JD distorted by its Hibbett combination; median of the six +5.8%). This rules out "category traffic fell" as the cause.

## 2. Is it a smoking gun? No.

The data support a split verdict, not a clean one:
1. Global and NA/APLA digital declines are accompanied by equal-or-larger visit declines, which fits lost demand or lost promo-driven visits (both predicted by "deliberate" and "demand" stories).
2. EMEA's revenue fall is not visible in traffic, which is the one place the web data fits Nike's "deliberate" account. DERIVED arithmetic: Nike said in Q2 FY25 that digital was about "50% full price and 50% off price" (global, call quote, repo note `pricing_discounting.md`, SNIPPET of a repo note, not re-opened). If EMEA looked the same and off-price volume fell the stated "over 50%", the off-price cut alone removes about 25 of the 26 points, leaving full-price digital roughly flat. This is an assumption chain (EMEA mix unknown, volume is not dollars), so treat it as an upper bound on how much the deliberate cut can explain, not a finding.
3. What would separate the two for EMEA: Nike's EMEA digital orders, AOV and full-price share (not disclosed), or a dated nike.com/gb sale-page product count (Wayback is blocked, section 4).

Link to existing work: the hunt synthesis found nike.com US discount share flat YoY with hidden promos rising (`data/hunt/pricing_catalog`, `00_SYNTHESIS.md`). That fits NA digital only -6% with visits -12%: the US was not cut hard, and the US visit loss is not explained by a deliberate promo cut.

## 3. Alternatives and what ruled them out

| Alternative explanation | Test | Result |
|---|---|---|
| Traffic held, revenue fell (pure conversion or price cut), globally | Semrush global visits -11.4% vs digital -13% | Ruled out globally; survives in EMEA only |
| Category-wide traffic decline (macro) | Peer sites same month, same country | Ruled out: peer median about 0 to +6% |
| GB data error drives EMEA result | Recompute ex-GB (-6.8%) | EMEA wedge shrinks from -28% to -21% but stays large; GB +34% on Semrush is itself suspicious (adidas.co.uk +32.5%, JD +26.9% in the same country, so it may be a panel or bot artifact) |
| Single-month noise (Aug only) | Other points: Semrush US Jul 2026 YoY -10.6% (SNIPPET), Semrush global Jan 2026 -5.1% (SNIPPET via RetailBoss, OPENED summary) vs reported digital -9% in Q3 FY26 | Consistent direction; only Aug is OPENED raw. Jun and Jul YoY not recoverable (Semrush page shows latest month only) |
| Traffic moved to the Nike app (web visits understate demand) | Not testable with web data | NOT ruled out. Needs app MAU or session data (Sensor Tower, Similarweb app panel), see `apps_digital` README for what was tried |
| Tranco rank shows nike.com traffic stable (-2% adj), so decline is conversion-only | Validate Tranco against Semrush and reported digital | Tranco fails validation (section 5); the stability is not evidence |
| Bot or non-shopper traffic inflates EMEA visits | No bot-share data | NOT ruled out |

Survivors for EMEA: (a) deliberate off-price cut lowering conversion while browsing persists, (b) weaker conversion from weak product or pricing, (c) measurement artifact in Semrush. Data that would decide: Nike EMEA digital orders and AOV; a time series of the nike.com/gb sale-page product count; independent panel (Similarweb Pro, Adobe or Salesforce commerce indices) for UK and DE.

## 4. Routes tried (worked / blocked / partial)

| # | Route | Result |
|---|---|---|
| 1 | Cloudflare Radar site `radar.cloudflare.com/domains/domain/nike.com` (curl and WebFetch) | BLOCKED, HTTP 403 |
| 2 | Cloudflare Radar API `api.cloudflare.com/client/v4/radar/ranking/...` without token | BLOCKED, HTTP 400 (token required; none exists) |
| 3 | Tranco: lists API + top-100k download, 177 dates (1st and 15th of each month, 2019-06-01 to 2026-10-01), 50 sportswear and retail domains plus a 40-domain control basket and top-5000 snapshots for list-wide drift | WORKED; but see section 5, signal invalid for YoY |
| 4 | Tranco `ranks/domain` API | WORKED but only last 37 days (nike.com rank 642 on 2026-10-01, 669 on 2026-10-14) |
| 5 | Tranco by country | BLOCKED: Tranco publishes no country lists |
| 6 | CrUX top lists by country (zakird/crux-top-lists via raw.githubusercontent.com): global 2022-06 to 2026-09, US/DE/GB/JP/CN 2025-01 to 2026-09 | WORKED but only rank-magnitude buckets (1000, 5000, 10000...), see section 5 |
| 7 | CrUX BigQuery public dataset / `data.chromium.org` | BLOCKED (no connection) |
| 8 | Wayback (`web.archive.org` CDX and snapshots, via curl and WebFetch) for Similarweb and Semrush pages | BLOCKED by egress policy; `archive.org/wayback/available` works but only returns a 2026-02-13 Similarweb snapshot with status 202 (bot challenge page) and no Semrush snapshots |
| 9 | Similarweb nike.com page (WebFetch summary, repo + Similarweb blog Sep 2026) | PARTIAL: Sep 2026 MoM -15.4%, global rank 309 vs 273 three months earlier; no YoY, no history |
| 10 | Semrush `trending-websites/<cc>/<category>` pages, embedded state, 18 countries x 5 categories + global x 5 | WORKED: gives YoY and MoM for the latest month (Aug 2026) for the top 100 domains; no date parameter, so no history. Also: Semrush country figures for nike.com US (41.5M) differ from the overview country split (30.5M Sep share x total) because categories and scope differ; I only compare YoY, not levels |
| 11 | Semrush overview for `nike.com.cn` | BLOCKED (404): no mainland China data on Semrush |
| 12 | Cisco Umbrella top-1M (current) | PARTIAL: nike.com rank 18,823, adidas.com 26,652 (DNS cache effects make it useless as a traffic rank); no history |
| 13 | Majestic Million (current) | PARTIAL: backlink-based (nike.com 754, adidas.com 2,210), not traffic; no history |
| 14 | Common Crawl: `index.commoncrawl.org` | BLOCKED (no connection); webgraph domain-rank files reachable on data.commoncrawl.org (1.3 GB each) but are link-graph centrality, not traffic, so not pursued |
| 15 | Statista "web visits to nike.com" | MASKED (values hidden behind paywall) |
| 16 | Altindex NKE web traffic | PARTIAL: Apr to Sep 2026 monthly estimates only (Jun 102.4M, Jul 113.8M, Aug 111.0M, Sep 94.4M; source "aggregated from the top providers", not comparable to Semrush levels) |
| 17 | Exploding Topics, RetailBoss | PARTIAL: Sep 2026 single value; Jan 2026 Semrush table (nike.com 105.66M, YoY -5.08%; adidas.com +14.3%; ASICS +28.4%) |
| 18 | Umbrella/Majestic/Tranco provider-specific history | BLOCKED: only blended Tranco history is public |

Eighteen routes tried; routes 3, 4, 6 and 10 returned usable data. History of YoY from a single provider remains unavailable, which is the main thing I could not get.

## 5. Tranco and CrUX: why they do not answer the question (DERIVED)

- **Zipf conversion.** Assumption: visits proportional to rank^(-alpha). Fit across 16 domains with Semrush Sep 2026 global visits vs Tranco 2026-10-01 rank (`test_alpha_calibration.csv`): alpha = 0.79, correlation -0.94, so the cross-section follows a power law (this is the validation of the *level* relation). Used alpha 0.8, 1.0, 1.2 as a range. A rank change from 599 (Jun 2025) to 653 (Aug 2026) implies -8% traffic at alpha 1.0 and -7% at alpha 0.79.
- **But the YoY changes are not usable.** Across 9 US domains, the correlation between Tranco-implied YoY (Aug 2026, drift-adjusted) and Semrush US YoY is **-0.31** (`test_tranco_vs_semrush_us_yoy_aug2026.csv`): Tranco says almost every consumer domain lost 10% to 40% (adidas.com -15% adj while Semrush says +9%, lululemon -25% vs +35%). Against reported NIKE Brand Digital growth by quarter (FY25 Q1 to FY27 Q1, n=9) the correlation of Tranco nike.com YoY is **-0.10 to -0.32**: Tranco showed +9% raw in Jun to Aug 2024 when reported digital was -20%, and -0.7% to -5.5% (adjusted to raw) in Q1 FY27 when digital was -13% (`test_tranco_nike_vs_reported_digital.csv`). The provider mix changed (Alexa out 2023, CrUX and Radar in), Umbrella-style DNS and app and API calls count as "traffic", and the list-drift and retail-basket controls do not fix it. Nike's Tranco rank slid from 599 to about 650 (8%), which on its own would not reveal a 13% digital decline.
- **Share inside the peer set** (`tranco_zipf_peer_share_by_fq.csv`, alpha 0.79): Nike share of the seven-domain set 53.3% (FY25 Q1), 50.5% (FY26 Q1), 54.7% (FY27 Q1). Noisy and contradicted by Semrush; on.com is missing before 2024 (it traded as on-running.com). Not used.
- **CrUX buckets** (`raw/crux_buckets_long.csv`, 2312 rows): nike.com stayed in the top-1000 bucket in global, US, DE and GB in every month pulled. In Japan nike.com has sat in the 5000 bucket since 2026-04 (it flipped between buckets seasonally in 2025), consistent with Semrush JP -32%. adidas.com US fell from the 1000 to the 5000 bucket in 2026-08 and hoka.com US in 2026-09, while Semrush has adidas US +9%: another sign the buckets are too coarse to read YoY.

Conclusion on the lists: they are INCONCLUSIVE for the demand-versus-deliberate question after the routes above; the usable evidence is the Semrush YoY cross-section, which is one provider's modelled estimate (Semrush Traffic Analytics), one month, with a suspicious GB number and no China.

## 6. Implication for the short thesis

- Positive for the short: nike.com visits are down about 11% YoY globally and 12% in the US while every named peer except Puma is flat or growing (DERIVED, Semrush). This is a Nike-specific loss of web audience, not a category move.
- Neutral to negative for the short: in EMEA, the largest digital revenue decline coincides with flat traffic and Nike's stated promo cut; that part is plausibly recoverable by management choice (revenue per visit can be dialled back up by promoting again), which is the same mechanism the long case uses.
- Do not use the Tranco ranks as evidence for either side in the deck. Do not quote "Digital -26%" as the total; it is EMEA.

## 7. What I could not get

1. Any multi-year monthly nike.com visit series from a single traffic provider (Similarweb Pro, Semrush Traffic Analytics history, Adobe, Comscore): needs a paid or logged-in account, or an analyst data pull.
2. Jun and Jul 2026 YoY (Semrush trending page shows only the latest month; a Jun/Jul copy would have to come from the Wayback, which is blocked).
3. China (nike.com.cn): no free source exposes it.
4. Nike EMEA digital orders, AOV and full-price share, and app usage, which would separate the three EMEA survivors.

Next best step (cheap): re-pull `pull_semrush_trending.py` on the 10th of each month to build the YoY series forward, and ask the user's Refinitiv or Visible Alpha desk for Similarweb or Sensor Tower history on nike.com and the Nike app.
