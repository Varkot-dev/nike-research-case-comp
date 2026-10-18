# Which parts of Nike earn high or low margins, and how big is each part?

**Prepared:** October 18, 2026. **Extends** `06_region_margin_product.md` (regional margins, which it reports) and `09_channel_margin_test.md` (Direct revenue over its wholesale-price cost, and the operating cost of serving Direct). This note adds three things nobody in the repo had done: (1) an exact split of NIKE Brand gross margin into wholesale and Direct for FY2019 to FY2024; (2) product category margin estimates from the one peer that discloses them; (3) a mix bridge showing how much of the FY2024 to FY2026 gross margin decline is mix.

**Scripts and data.** `scripts/margin_mix/channel_gm.py` and `scripts/margin_mix/profit_pools.py` (run from the repo root) read only `data/nike_filing_facts.csv` and `data/nike_region_profitability.csv` and write `data/margin_mix/channel_gm_decomposition.csv`, `channel_gm_fy25_fy26_assumed.csv` and `profit_pools.csv`. All outputs are DERIVED (my arithmetic). Peer figures are SNIPPET (seen in search summaries of the company's own report pages; the pages could not be opened from this session because the container's network policy blocks sec.gov, investors.nike.com, puma.com and WebFetch). They need opening before they go into REPORT.md.

## 0. Answer in brief

| Business cut | What Nike discloses | High margin | Low margin | Size of the gap |
|---|---|---|---|---|
| **Channel** | Revenue only; FY2019 to FY2024 also the internal sales from wholesale operations to Direct at wholesale price | NIKE Direct: about **59% to 63% gross margin** | Wholesale: about **31% to 37%** | **About 26 to 29 points**; the largest gap of any cut (DERIVED, Section 2) |
| **Region** | Segment revenue, EBIT, and gross margin from FY2023 | Greater China (gross), North America (EBIT) | Converse, EMEA | About 4 points of gross margin between regions, about 7 points of EBIT margin excluding Converse (reported, Section 3) |
| **Product** | Revenue, units and ASP changes only | Apparel (peer evidence) | Footwear (peer evidence) | About **1 to 2 points** at Puma, every year 2021 to 2025 (SNIPPET); not identifiable from Nike's own data (Section 4) |
| **Jordan** | Revenue only | Gross margin at least about 2 points above NIKE Brand **from channel mix alone** (Direct share about 50% to 55% vs 44%) | n/a | DERIVED, Section 5 |

**What this means for the pitch (my inference):**
- **Channel and price set Nike's gross margin; product category barely matters.**
  - Holding FY2024 margins constant, the drop in Direct share from 43.7% to 39.2% explains about **-118 bps** of the **-129 bps** fall in NIKE Brand gross margin from FY2024 to FY2026.
  - Regional mix explains about -24 bps, and the footwear to apparel shift about +4 bps (Section 6).
  - These effects overlap, because regions carry different channel mixes, so they are not additive.
- **The wholesale pivot lowers reported gross margin by construction.** Each 1 point of revenue share that moves from Direct to wholesale costs about **27 bps** of NIKE Brand gross margin at FY2024 channel margins (0.01 x 26.7 points, my arithmetic), before any opex saving. Whether EBIT gains depends on the store and digital costs that sit below gross profit; `09_channel_margin_test.md` covers those.
- **For a margin-recovery bull case,** a return to 11% to 14% EBIT margin through a wholesale-led recovery has to come from opex leverage and full-price ASP, not from gross margin mix.

## 1. How big is each part? (revenue share, FY2026 unless stated)

| Cut | Part | Revenue ($M) | Share | Source |
|---|---|---|---|---|
| Product (NIKE Brand) | Footwear | 29,525 | 65.4% of product revenue | FY26 10-K p. 32 |
| | Apparel | 13,449 | 29.8% | FY26 10-K p. 32 |
| | Equipment | 2,199 | 4.9% | FY26 10-K p. 32 |
| Channel (NIKE Brand) | Wholesale | 27,453 | 60.8% | FY26 10-K p. 32 |
| | NIKE Direct | 17,720 | 39.2% | FY26 10-K p. 32 |
| | of which Digital | about 8,600 | about 19% of NIKE Brand | FY26 10-K p. 33 ($8.6B) |
| | of which Nike-owned stores | about 9,100 | about 20% | FY26 10-K p. 33 ($9.1B) |
| Region (of five segments) | North America | 20,511 | 44.3% | `nike_region_profitability.csv` |
| | EMEA | 12,572 | 27.1% | same |
| | Greater China | 5,847 | 12.6% | same |
| | APLA | 6,243 | 13.5% | same |
| | Converse | 1,174 | 2.5% | FY26 10-K p. 32 |
| Brand | Jordan (reported basis) | 7,034 | 15.6% of NIKE Brand | FY26 10-K p. 32 |

Shares are my arithmetic. The product total excludes Global Brand Divisions revenue ($49M). Direct sub-channels are rounded billions as printed.

**Change since FY2024 (my arithmetic on FY24 10-K p. 34 and FY26 10-K p. 32):**
- Footwear fell from 67.8% to 65.4% of product revenue.
- Direct fell from 43.7% to 39.2% of channel revenue.
- Greater China fell from 14.7% to 12.6% of segment revenue, and Converse from 4.1% to 2.5%.

## 2. Channel: an exact split of gross margin into wholesale and Direct (FY2019 to FY2024)

**The disclosure that makes it possible.** Through FY2024, Nike's revenue table printed "Sales from our Wholesale Operations to NIKE Direct Operations." This is the product that Direct sold, valued at the wholesale price (W; for example $13,009M in FY2024, FY24 10-K p. 34). Nike stopped printing it from the FY2025 10-K.

**Identity (my derivation).** Let g_w be the gross margin Nike earns at wholesale price. Product sold through Direct then cost W x (1 - g_w), so:
- NIKE Brand gross profit = g_w x wholesale revenue + (Direct revenue - W x (1 - g_w)).
- Solving: **g_w = (Brand GP + W - Direct revenue) / (wholesale revenue + W)**, and Direct gross margin = 1 - W x (1 - g_w) / Direct revenue.
- NIKE Brand GP is NIKE, Inc. gross profit less Converse gross profit:
  - FY2023 and FY2024 use Converse's disclosed gross margin (53.8% and 52.5%, FY25 10-K p. 42 and FY26 10-K p. 41).
  - FY2019 to FY2022 bracket it at 50% to 54%, which moves both results by 0.2 points or less.

| | FY2019 | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 |
|---|---|---|---|---|---|---|
| Wholesale revenue ($M) | 25,423 | 23,156 | 25,898 | 25,608 | 27,397 | 27,758 |
| Direct revenue ($M) | 11,753 | 12,382 | 16,370 | 18,726 | 21,308 | 21,519 |
| Internal sales to Direct, W ($M) | 7,127 | 7,452 | 9,872 | 10,543 | 12,730 | 13,009 |
| Direct revenue / W | 1.65x | 1.66x | 1.66x | 1.78x | 1.67x | 1.65x |
| NIKE Brand gross margin | 44.2% | 42.9% | 44.4% | 45.6% | 43.1% | 44.2% |
| **Wholesale gross margin** | **36.3% to 36.5%** | **33.7% to 33.9%** | **34.3% to 34.6%** | **33.3% to 33.5%** | **30.9%** | **32.6%** |
| **Direct gross margin** | **61.4% to 61.5%** | **60.1% to 60.2%** | **60.4% to 60.5%** | **62.4% to 62.6%** | **58.7%** | **59.3%** |
| Direct share of revenue | 31.6% | 34.8% | 38.7% | 42.2% | 43.7% | 43.7% |
| **Direct share of gross profit** | 43.8% | 48.8% | 52.6% | 57.8% | 59.6% | 58.5% |

Inputs: revenue and W from the FY2019 10-K p. 27, FY2022 10-K p. 32, FY2023 10-K p. 32 and FY2024 10-K p. 34; gross profit from FY2019 10-K p. 26, FY2022 10-K p. 56, FY2023 10-K p. 31 and FY2024 10-K p. 57; FY2020 and FY2021 per `data/nike_filing_facts.csv`. Margins and shares are my arithmetic. The ranges reflect the Converse bracket.

**Reading it:**
- **In FY2024, Direct earned about 59% of NIKE Brand gross profit on 44% of revenue.** That is the "higher-margin NIKE Direct" in Nike's own bridge language (FY19 10-K p. 29, quoted in `06` Section 3).
- **Both channel margins fell from FY2022 to FY2023**: wholesale by about 2.5 points and Direct by about 3.8 points. This matches Nike's bridge, where the Direct line went from +160 bps (9M FY2022) to -130 bps (9M FY2023) as Direct cleared inventory (`09` Test 1).
- **Wholesale gross margin has been falling since FY2019**, from about 36% to 31% to 33%. Gross margin "at wholesale price" absorbs freight, warehousing, product cost inflation, tariffs and royalties (cost of sales definition, FY26 10-K notes), and the filings do not split these by channel.

**Assumptions to state in Q&A:**
1. Product sold through Direct is assumed to carry the same cost-to-wholesale-price ratio as product sold to wholesale customers. If Direct carries more high-margin product (for example SNKRS launches), the true wholesale margin is a little higher and Direct a little lower.
2. Corporate segment items in cost of sales (hedge results) are ignored. Corporate revenue was between -$97M and +$40M a year.
3. **This is gross margin only.** Store occupancy, store labor and digital platform costs sit in operating overhead and demand creation, below gross profit. `09_channel_margin_test.md` shows that Direct's operating advantage depends on full-price selling.

**FY2025 and FY2026 (ASSUMED markup).** Without W, I assume Direct revenue / W of 1.60x to 1.70x. FY2019 to FY2024 ranged from 1.65x to 1.78x, and was 1.65x to 1.67x outside the FY2022 peak. Results:

| | FY2025 | FY2026 |
|---|---|---|
| Wholesale gross margin | 30.4% to 31.7% | 32.0% to 33.1% |
| Direct gross margin | 57.3% to 59.1% | 58.2% to 60.0% |
| Direct share of revenue / of gross profit | 42.1% / 56.8% to 58.5% | 39.2% / 53.2% to 54.8% |

Caveat: FY2026 gross profit includes tariff costs and Nike's expected IEEPA tariff recovery ($965M in North America and $21M in Converse EBIT, FY26 10-K p. 30). The filings available in the repo do not say how much of that recovery sits in cost of sales, so FY2026 within-channel margins are not a clean read.

## 3. Region (reported; detail in `06_region_margin_product.md`)

| Segment | FY2026 revenue share | Gross margin | EBIT margin | Share of segment EBIT | Share of segment EBIT ex tariff recovery |
|---|---|---|---|---|---|
| North America | 44.3% | 45.6% | 26.2% (21.5% ex recovery) | 51.3% | 46.5% |
| EMEA | 27.1% | 41.8% | 19.2% | 23.1% | 25.5% |
| Greater China | 12.6% | 45.7% | 21.9% | 12.2% | 13.5% |
| APLA | 13.5% | 42.0% | 22.2% | 13.2% | 14.6% |
| Converse | 2.5% | 43.8% | 1.5% (-0.3% ex recovery) | 0.2% | 0.0% |

Gross margins: FY26 10-K pp. 37 to 41. EBIT and shares: `data/nike_region_profitability.csv`, with shares and the ex-recovery view as my arithmetic. Segment EBIT excludes Global Brand Divisions (-$4,603M) and Corporate (-$2,023M) in FY2026, so these margins are well above the consolidated 8.3%.

**Change since FY2024:** Greater China's share of segment EBIT fell from 16.6% to 12.2%, and Converse's from 3.4% to 0.2% (my arithmetic).

## 4. Product category: estimate from peers, because Nike's data cannot identify it

**Nike discloses no profit or margin by footwear, apparel or equipment.** I tried two routes on Nike's own numbers. Neither identifies the gap:
1. **Across segments:** In FY2024, footwear was 67.9% of North America product revenue, 62.3% in EMEA, 73.6% in Greater China and 72.3% in APLA (FY24 figures in `data/nike_filing_facts.csv`, my arithmetic). Segment gross margins were 44.4%, 44.2%, 50.2% and 45.9%.
   - The most footwear-heavy regions have the highest gross margins, but that is four data points, confounded with Greater China pricing and Direct share.
   - A regression that separates product from region and channel has more unknowns than observations.
2. **Over time:** consolidated gross margin moves with tariffs, discounting, FX and channel mix every year (gross margin bridge, `15_why_nike_discounts.md`). The footwear share moved only about 2.5 points over FY2024 to FY2026, too little to separate.

**Peer that discloses it (SNIPPET: PUMA annual reports 2022 to 2025, "results of operations" pages, gross profit margin by product division):**

| PUMA | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| Footwear | 47.3% | 44.9% | 45.4% | 46.9% | 44.3% |
| Apparel | 48.9% | 47.3% | 47.8% | 48.1% (48.6% restated) | 46.0% |
| Accessories | 47.1% | 47.4% | 46.6% | 47.6% (48.0% restated) | 45.5% |
| Apparel minus footwear | +1.6 pts | +2.4 pts | +2.4 pts | +1.2 pts (+1.7 restated) | +1.7 pts |

URLs: annual-report.puma.com/2022, /2023, /2024 and /2025 "results of operations." The 2024 restatement is for the discontinued PUMA United operation. **adidas:** recent reports give group gross margin only. A 2012 to 2017 product split may exist in older annual reports, but none was seen (search, not opened).

**Estimate for Nike (ASSUMPTION, calibrated to NIKE Brand gross margin):**
- Applying Puma's 2025 gaps (apparel +1.7 points, equipment +1.2 points over footwear) and solving for the weighted average to equal NIKE Brand gross margin gives, for FY2026:
  - footwear about **42.4%**;
  - apparel about **44.1%**;
  - equipment about **43.6%**.
- **Footwear's share of product gross profit is then 64.5%, against 65.4% of revenue.**
- Stress test: triple Puma's gap (apparel 5.1 points above footwear). Footwear's share of gross profit is still 62.8%.
- So whatever the true gap, **footwear earns roughly two-thirds of Nike's gross profit** (`data/margin_mix/profit_pools.csv`).

**Limits:**
- Puma's channel mix and price points differ from Nike's.
- The ordering itself (apparel above footwear) is peer evidence, not Nike evidence. The FY2024 cross-section above points the other way, but is confounded.
- What would settle it: a Nike Investor Day (Nov 16 to 17) disclosure, sell-side models with category margin assumptions (Refinitiv, `research_notes/Refinitiv pull list.md`), or older Nike 10-Ks if they once gave category margins. None was found.

## 5. Jordan: Direct share and the channel-mix margin effect (DERIVED)

Nike reported Jordan on two bases for the same years:
- the old **wholesale equivalent** basis, with Direct sales valued at wholesale price ($6,589M FY2023, FY23 10-K p. 32; $6,988M FY2024, FY24 10-K p. 34);
- the new **reported** basis ($8,460M FY2023, FY25 10-K p. 33; $8,701M FY2024, FY26 10-K p. 32).

**Method:** the difference equals Jordan Direct revenue x (1 - 1 / markup). Using Nike Brand's markup that year (Section 2):
- **Jordan Direct revenue was about $4,650M in FY2023 and about $4,330M in FY2024**, a Direct share of about **55% and 50%**, against 43.7% for NIKE Brand.
- At the Section 2 channel margins, channel mix alone puts Jordan's gross margin at about **46.2% (FY2023) and 45.9% (FY2024)**, against 43.1% and 44.2% for NIKE Brand.
- This assumes Jordan product carries the same margins within each channel as the rest of NIKE Brand. Nike discloses nothing on that.

**Caveat:** the FY2024 Jordan Direct share uses NIKE Brand's 1.65x markup. If Jordan's Direct sells at a higher markup (launch-heavy SNKRS), the implied Direct share is lower. This revises the Jordan valuation inputs in `13_jordan_valuation.md` only if that note assumed a Jordan gross margin. Check before reuse.

## 6. Mix bridge: FY2024 to FY2026 gross margin (DERIVED; effects overlap)

NIKE Brand gross margin went from 44.2% to 42.9%, **-129 bps** (FY2026 at the 1.65x assumed markup only for the within-channel split; the total is reported). Mix effects, holding FY2024 margins constant:

| Mix effect | Change in mix | FY2024 margin gap used | Effect |
|---|---|---|---|
| Channel | Direct share 43.7% to 39.2% | Direct minus wholesale 26.7 points | **About -118 bps** |
| Region | Greater China and Converse shares down, North America up | FY2024 segment gross margins | **About -24 bps** |
| Product | Footwear 67.8% to 65.4% | Puma gaps (assumed) | **About +4 bps** |

- At the assumed 1.65x markup, FY2026 within-channel margins come out almost unchanged from FY2024: wholesale 32.5% vs 32.6%, Direct 59.1% vs 59.3%. In that case most of the decline is channel mix.
- This rests on the markup assumption and the unknown cost-of-sales treatment of the tariff recovery (Section 2), so treat it as indicative, not as a finding.
- Nike's own FY2026 bridge reports channel mix as a *positive* on warehousing and logistics costs (+20 bps, FY26 10-K p. 34). The two are consistent: Nike's bridge isolates cost lines, while the identity above captures the price difference between selling at retail and at wholesale.

## 7. Routes tried (per CLAUDE.md)

| Route | Result |
|---|---|
| Nike 10-K revenue disaggregation by segment and product, FY2019 to FY2026 (investors.nike.com mirror) | Blocked: container network policy (403). Repo facts cover product by region only for FY2021, FY2022 and FY2024, plus North America FY2023 to FY2026 |
| data.sec.gov submissions index; sec.gov; WebFetch of any host | Blocked (403 or DNS) |
| Wholesale equivalent disclosure in the repo facts | **Worked**: exact channel split FY2019 to FY2024 |
| PUMA product division gross margins | Worked (SNIPPET, 2021 to 2025); open the pages before citing in REPORT.md |
| adidas product gross margins | Not found in 2022 to 2025 reports; older reports not opened |
| Nike management statements on category margins | None found (search) |
| Nike cross-section and time series | Run; not identified (Section 4) |

**To do with network access:** open the PUMA pages and the FY2019 to FY2026 10-K disaggregation tables, then re-run Section 4 on a full product-by-region panel.
