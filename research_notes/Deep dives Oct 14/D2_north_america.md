# D2: North America. Is consumer demand growing, or was NA wholesale growth channel fill?

Prepared 2026-10-14. Builds on `research_notes/Long or short cruxes/na_sell_through.md` (retailer Q2 2026 table, skeptic review) and does not repeat its retailer-by-retailer table. This note adds: a full Nike channel time series, a channel-shift identity test, Nike's own filing language by quarter, Nike NA inventory, a retailer inventory panel from SEC XBRL, and September CPI.

Tags: OPENED = I read the source in this session. DERIVED = my arithmetic from OPENED numbers (inputs shown). SNIPPET = search summary only. REPO = read from files already in this repo.

## 1. Headline

**NA consumer demand for Nike is not growing in total. Most of the +9% NA wholesale (Q1 FY27) is relocation of sales from NIKE Direct to wholesale partners, not new consumer demand. On top of that sits a one-quarter sell-in pulse in Q2 FY26 that Nike itself says it is now lapping. Whether a smaller piece of the Q1 FY27 +9% is fill or genuine new distribution cannot be separated from filings.**

Numbers behind this (all NA, Nike filings, OPENED on the investors.nike.com mirror):

| Metric | FY2024 | FY2026 | TTM to Q1 FY27 | Change TTM vs FY24 |
|---|---|---|---|---|
| NA wholesale $M | 11,004 | 11,958 | 12,203 | +1,199 (+10.9%) |
| NIKE Direct NA $M | 10,392 | 8,553 | 8,415 | -1,977 (-19.0%) |
| NA total $M | 21,396 | 20,511 | 20,618 | -778 (-3.6%) |
| Wholesale share of NA | 51.4% | 58.3% | 59.2% | +7.8 pts |

Source: `data/nike_channel_split.csv` (quarters summed; DERIVED). Q1 FY27 values re-read in the 10-Q (nke-20260831.htm, p. 26): wholesale $2,981M vs $2,736M, Direct $2,146M vs $2,284M (OPENED).

## 2. Every plausible explanation, tested

The thing to explain: NA wholesale +9% (Q1 FY27), +24% (Q2 FY26), +11% (Q3 FY26), +10% (Q4 FY26) while NIKE Direct NA is down 3% to 10% every quarter since Q1 FY26 and total NA is up only 2% to 9%.

| # | Explanation | Verdict | Test and evidence |
|---|---|---|---|
| 1 | **Shift of sales from Direct to wholesale** (Nike cut digital promotion and pushed volume to partners) | **SURVIVES, the largest piece** | Identity (DERIVED): retail-equivalent sales = Direct + wholesale / r, where r = wholesale revenue per retail dollar. TTM vs FY24 is flat at r = 60.6% (break-even = 1,199 / 1,977). Nike wholesale typically sells at about 50% to 55% of retail (my assumption, not a Nike disclosure). Implied change: r=0.45 +2.0%, r=0.50 +1.3%, r=0.55 +0.7%, r=0.60 +0.1%, r=0.65 -0.5%. So the retail-equivalent sell-in is flat to up about 1%, not +11%. Nike confirms the mechanism: Q4 FY26 call, digital "off-price was down over 50% following aggressive actions to reduce promotions" and "15-point improvement in full price realization" (Q4FY26 transcript, OPENED). Wholesale share of NA rose from 51.4% to 59.2% (above). Limit: assumes lost Direct dollars moved 1:1 to partners, which is generous, and r is assumed. |
| 2 | **Restocking after the 2024 destock** | **PARTLY TRUE for the year-over-year comparisons, RULED OUT as the explanation for the level** | FY25 NA wholesale fell only 4.7% (10,484 vs 11,004, DERIVED), so there was no deep wholesale destock to rebuild. TTM wholesale is now 10.9% above FY24, so partners are being shipped more than in the pre-destock year while Nike NA footwear units are still about 4.6% below FY24 (units: FY25 -10%, FY26 +6%, from the 10-Ks; 0.90 x 1.06 = 0.954, DERIVED). Nike's wording does flag comparison effects: Q1 FY26 10-Q "in part due to shipment timing in the prior year", Q2 FY26 10-Q "marketplace management actions in both the current and prior year", FY26 10-K "fewer marketplace management actions" (all OPENED). Those explain growth rates, not the level. |
| 3 | **Channel fill (sell-in above sell-through)** | **SURVIVES for Q2 FY26 and for lifestyle product, NOT shown as an ongoing build** | Retailer inventory pulse: four retailers with clean Aug-to-Aug history (Academy, Shoe Station, Caleres, Genesco) had combined inventory +11.3% YoY at Aug 2, 2025 ($2,903M to $3,231M), then +4.5% at Aug 1, 2026 ($3,378M). DICK'S standalone +7.1% and Foot Locker standalone +3.7% at Aug 2025 (SEC XBRL companyfacts, OPENED; DERIVED). That pulse coincides with Nike NA wholesale +10.5% (Q1 FY26) and +23.9% (Q2 FY26). Management admissions: "some aged, higher volume, sportswear footwear sold through below expectations ... impacted our future order books" and "we've been oversupplying our iconic retro product" (Q1 FY27 call, OPENED); "higher comparison of North America sell-in activities versus last year" worth about 400 bps with EMEA (Q1 FY27 call, OPENED); Q3 FY26 call "sell-through has been below plan" in NA. Against an ongoing build: Nike's own NA inventory $3,491M at Aug 31, 2026 vs $3,524M a year earlier (-0.9%) and $3,519M in Aug 2024 (10-Qs, OPENED); as a share of TTM NA revenue it is 16.9% / 17.8% / 16.9% for Aug 2024 / 2025 / 2026 (DERIVED), so Nike is not carrying more. Retailer growth in Aug 2026 (+4.5%) is below Nike shipments (+9%), but dollar inventory is inflated by tariffs (Q3 FY26 call: inventory dollars +low single digits with units down high single digits, "the spread primarily due to tariffs"), so retailer dollar inventory overstates units. |
| 4 | **Genuine sell-through growth (performance, running)** | **TRUE but too small to explain +9%** | Nike NA: running up "double digits" (Q2 FY26 call), Q1 FY27 growth "driven by performance led by Running, Global Football and Basketball", "good sell-through" at DICK'S, Academy, SCHEELS, JD, Foot Locker (Q1 FY27 call, OPENED; that is management opinion). Circana H1 2026: US footwear dollars +1%, running +13%, sport lifestyle down (WWD summary, REPO). Nike is about half Sportswear, which was "down low double digits" in Q1 FY27 (OPENED). Offset: performance up, lifestyle down, total NIKE Direct (Nike-owned sell-through) -6%. |
| 5 | **Liquidation to off-price / value channels** | **SURVIVES as part of Q2 FY26 only** | Friend, Q2 FY26 call: "the quarter certainly benefited from liquidation to value channels as we cleaned up the marketplace" (OPENED). Revenue from closeouts counts in wholesale but is not full-price consumer demand. Size not disclosed. |
| 6 | **New doors / expanded distribution (Amazon, Academy Jordan, others)** | **SURVIVES, size unknown** | Nike named "expanded distribution" as a wholesale driver in the Q1 FY26 10-Q, Q2 FY26 10-Q, Q3 FY26 10-Q and FY26 10-K (OPENED). The Q1 FY27 10-Q gives no driver for the +9% (OPENED). Q2 FY26 call: "balanced contribution of growth from both new and existing partners". A new door is real sell-through at the shelf, but it replaces Direct and other partner sales rather than adding category demand; the category itself grew about 1% (Circana H1 2026, REPO). |
| 7 | **Price and mix** | **PARTLY TRUE, does not close the gap** | NA footwear Q1 FY27 +1% = units +2%, ASP about -1 pt, "channel mix and higher discounts" (10-Q, OPENED). Apparel +6% = units flat, ASP +6 pts, "product mix and strategic pricing, partially offset by higher discounts" (OPENED). Wholesale-only ASP is not disclosed. Footwear CPI: +3.4% in Sep 2026 (154.506 vs 149.463), +3.6% in Aug (FRED CUUR0000SEAE, OPENED; DERIVED). Nike footwear ASP lagging CPI means Nike is losing price position, not gaining. |
| 8 | **Timing (shipment calendar)** | **SURVIVES, small and reversing** | Q4 FY26 call: Q2 FY27 revenue has "timing of North America wholesale shipments" as part of a "multipoint headwind" (OPENED). Q2 FY26 NA wholesale was $3,550M vs $2,902M two years earlier (+22.3%), while Q1 FY26 was $2,736M vs $2,772M two years earlier (-1.3%) (DERIVED). Excess in Q2 FY26 over the Q1 two-year run-rate is about $690M (3,550 - 2,902 x 0.987; DERIVED). This is the clearest single pulse in the series. |
| 9 | **FX** | **RULED OUT** | NA reported growth equals currency-neutral growth in every quarter checked (Q1 FY27: 2% and 2%; Q1 FY26: 4% and 4%; 10-Qs, OPENED). |
| 10 | **New product launches / World Cup** | **PARTLY TRUE, one-off** | Football booking units "nearly 40% higher than World Cup '22" (Q2 FY26 call, OPENED); DICK'S comp +4.9% includes World Cup (REPO). Laps in Q2 FY27 and is football, not lifestyle. |
| 11 | **Retailer inventory rebuild by choice (partners wanted more Nike)** | **WEAKENED** | DICK'S standalone and Academy are the retailers that say Nike performance sells; their inventory moved with sales (REPO). But JD NA, Foot Locker NA, Famous and Shoe Carnival comps were negative while Nike shipped them more ("higher shipments to existing partners", FY26 10-K, OPENED). A partner that wanted more would not mark down aged Nike product (Foot Locker $40.4M write-down, REPO). |
| 12 | **Macro (category weak, not Nike-specific)** | **PARTLY TRUE** | Census shoe-store sales Jan to Jul 2026 +2.9% nominal vs footwear CPI about +3.25%, about -0.4% real (REPO, re-checked: Apr 2,998, May 3,328, Jun 3,050, Jul 3,600 vs 2,967 / 3,336 / 2,993 / 3,569; FRED MRTSSM4482USN, OPENED). Category is flat in real terms, so any Nike NA gain above flat has to be share gain; Direct -6% says Nike is not gaining there. |

## 3. Consumer demand estimate (DERIVED, mostly from `na_sell_through.md` and updated)

- Measured: NIKE Direct NA Q1 FY27 -6.0% (-$138M; digital -6%, stores -6%). NIKE Direct comparable stores were -1% to -2% in FY26 (10-K, OPENED).
- Inferred: tracked partners' Nike sell-through about -5% to 0% (REPO estimate, weights are guesses).
- Net NA consumer sell-through for Q1 FY27: about -3% to +1% in dollars, central about -1% (REPO). Real and unit terms are lower after about 3.4% footwear CPI.
- Longer view: NA footwear units cumulative FY23 to FY26 = 0.93 x 0.90 x 1.06 - 1 = -11.3% (DERIVED from 10-K unit changes: FY24 -7%, FY25 -10%, FY26 +6%), while PCE shoes nominal grew (REPO macro table). Nike has lost share of the NA footwear category since FY23 and the FY26 recovery in units is only a partial retrace.

## 4. What this means for the pitch

- Do not say "NA wholesale +9% is consumer demand". Wholesale is up $1.2B vs FY24 only because Direct is down $2.0B; total NA is $0.8B (3.6%) below FY24.
- Do not say "massive channel stuffing that will unwind". The tests show a real sell-in pulse (Q2 FY26, about $690M above run-rate DERIVED) that Nike has disclosed and guided (about 400 bps Q2 FY27 headwind with EMEA), and Nike's own NA inventory is flat to sales.
- The defensible statement: **NA growth is channel mix and one-off sell-in on a shrinking consumer base; the real growth is in running and performance, and lifestyle (about half of Nike) is in decline with order books cut.**

## 5. What remains unresolved, and what would decide

Two explanations still survive for the residual after removing channel shift: (a) fill that will unwind beyond guidance, (b) genuine new distribution that persists. The filings do not separate them. What would decide:

1. Nike Q2 FY27 NA wholesale (about Dec 17): if it falls more than the guided 400 bps, fill is larger than disclosed.
2. DICK'S Q3 (late Nov): Foot Locker inventory per door with a NA / International split (not disclosed so far).
3. Nike wholesale ASP or wholesale footwear units by region (not disclosed; ask at Investor Day, Nov 16 to 17).
4. Brand-level Circana or card-panel data for Nike US Jun to Sep 2026 (paid).
5. Census August and September shoe-store sales (August not yet published on FRED today; the Aug 2025 base is 4,343).

## 6. Routes tried (per repo rule), with result

| # | Route | Result |
|---|---|---|
| 1 | Nike 10-Qs / 10-Ks (13 filings, Q1 FY24 to Q1 FY27) from the investors.nike.com mirror | WORKED. Source of channel, units, ASP, driver language, NA inventory |
| 2 | Nike call transcripts, Q1 FY26 to Q1 FY27 (`data/hunt/earnings_calls/transcripts`) | WORKED. Liquidation to value channels, timing of shipments, sell-in lap, order-book cuts |
| 3 | SEC XBRL companyfacts (data.sec.gov) for DKS, ASO, SHOE, CAL, GCO, FL: inventory and revenue by quarter | WORKED for inventory (2023 to Aug 2026); quarterly revenue has gaps for some filers (Caleres and Genesco revenue tags return old periods only), so only Academy and Shoe Station sales YoY were computed |
| 4 | SEC document pages (10-K text for Nike share of each retailer's purchases) via a generic User-Agent | BLOCKED (HTTP 403 "undeclared automated tool"). Not retried with an email. Shares used are those already in the REPO note |
| 5 | FRED: Census MRTS shoe stores and sporting goods stores, BLS footwear CPI | WORKED (Aug MRTS not yet published; CPI through Sep 2026) |
| 6 | Circana Q3 2026 / brand-level Nike US figures (web search) | PARTIAL. Only H1 2026 category figures found; Q3 not yet released, brand data paywalled |
| 7 | web.archive.org availability API for Circana and SEC pages | BLOCKED (HTTP 429 rate limit) |
| 8 | Repo sources: BEA PCE / macro_category tests, trade_imports, stores, reviews_sentiment | REUSED (see `00_SCOREBOARD.md`); two-year import test inconclusive, Dick's reviews show real running sell-through |

Not yet tried (next person): Hibbett / JD NA split in JD annual report, Foot Locker 10-Q store-level inventory by region in the DKS Q3 filing (due late Nov), Placer.ai foot traffic for Nike-heavy chains, Canadian Nike wholesale proxies (Stats Canada), retailer 10-K "Nike share of purchases" via a company IR mirror.

## 7. Source list

| Source | Status |
|---|---|
| Nike 10-Q Q1 FY27, https://investors.nike.com/sec-filings/all-sec-filings/content/0000320187-26-000193/nke-20260831.htm (NA table p. 26, inventory table p. 17) | OPENED |
| Nike 10-Qs Q1 FY24 to Q3 FY26 and 10-Ks FY24 to FY26, same mirror path pattern (accessions 0000320187-23-000052, -24-000004, -24-000019, -24-000065, -25-000004, -25-000016, -25-000097, -25-000151, -26-000037; 10-Ks -24-000044, -25-000047, -26-000088) | OPENED |
| `data/nike_channel_split.csv` | REPO (checked against 10-Q for Q1 FY27 and Q1 FY26) |
| Nike call transcripts Q1 FY26 to Q1 FY27, `data/hunt/earnings_calls/transcripts/` | OPENED |
| SEC XBRL companyfacts, data.sec.gov, CIK 1089063, 1817358, 895447, 14707, 18498, 850209, pulled 2026-10-14 | OPENED |
| FRED MRTSSM4482USN, MRTSSM45111USN, CUUR0000SEAE, pulled 2026-10-14 | OPENED |
| `research_notes/Long or short cruxes/na_sell_through.md`, `00_SCOREBOARD.md` | REPO |
| Circana H1 2026 via web search summary | SNIPPET |
