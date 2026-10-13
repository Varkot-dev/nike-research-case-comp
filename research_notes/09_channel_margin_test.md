# Testing the channel margin hypothesis: is NIKE Direct only more profitable at full price?

**Prepared:** October 13, 2026. **Hypothesis under test** (from `06_region_margin_product.md` Section 3): NIKE Direct earns more than wholesale only when it sells at full price; heavy Direct discounting erases the advantage. Nike does not report profit by channel, so this note assembles every indirect measure Nike does disclose, then checks them against peers that do report channel margins.

**Sources.**
- Nike 10-Ks and 10-Qs, downloaded from the investors.nike.com mirror of EDGAR. Page numbers are printed pages.
- `data/nike_filing_facts.csv`. The FY2022 and FY2023 NIKE Direct bridge values were added in this round, each with a verbatim quote.
- `data/nike_channel_split.csv`.

All ratios, dollar conversions and sensitivities are **my arithmetic** on those figures.

## Test 1: what NIKE Direct earns above a wholesale sale (FY2017 to FY2024)

Until FY2024, Nike disclosed its internal sales "from our wholesale operations to our NIKE Direct operations, which are charged at prices comparable to those charged to external wholesale customers" (FY19 10-K p. 25; same wording through FY24 10-K p. 32). Dividing NIKE Direct revenue by that internal cost shows how much more Nike collected by selling a unit itself rather than through a retailer.

| Fiscal year | NIKE Direct revenue ($M) | Internal purchases at wholesale prices ($M) | Direct revenue / wholesale value | Spread as % of Direct revenue | Source |
|---|---|---|---|---|---|
| FY2017 | 9,082 | 5,616 | 1.62x | 38.2% | FY19 10-K p. 27 |
| FY2018 | 10,428 | 6,332 | 1.65x | 39.3% | FY19 10-K p. 27 |
| FY2019 | 11,753 | 7,127 | 1.65x | 39.4% | FY19 10-K p. 27 |
| FY2020 | 12,382 | 7,452 | 1.66x | 39.8% | FY20 10-K p. 31 |
| FY2021 | 16,370 | 9,872 | 1.66x | 39.7% | FY21 10-K p. 32 |
| **FY2022** | 18,726 | 10,543 | **1.78x** | **43.7%** | FY22 10-K p. 32 |
| FY2023 | 21,308 | 12,730 | 1.67x | 40.3% | FY23 10-K p. 32 |
| FY2024 | 21,519 | 13,009 | 1.65x | 39.5% | FY24 10-K p. 34 |

- **The spread is the gross dollars NIKE Direct earns over a wholesale sale, before Direct's own costs** (stores, digital fulfilment, Direct marketing), which Nike does not disclose. In FY2024 it was **$8.5 billion**, or 39.5% of Direct revenue.
- **The spread rose only once, in FY2022, by 4.0 points of Direct revenue**, the one year Nike says Direct sold with "lower promotional activity ... reflecting limited available for sale inventory due to supply chain constraints" (Q3 FY22 10-Q p. 30). It fell back by FY2024 as promotions returned (Test 2).
- **Caveat: timing.** Internal purchases are recorded when Nike's wholesale arm ships to Direct, not when Direct sells. FY2022 inventory was constrained and FY2023 inventory was built up, which flatters FY2022 and depresses FY2023. Averaging the two years removes most of the timing effect. The FY2022 to FY2023 average is **1.72x**, still above the FY2019 to FY2021 average of **1.66x** and the FY2024 level of **1.65x**.
- **Discontinued:** Nike dropped this disclosure in FY2025, so no direct read is available for FY2025 onward.

**Sensitivity: how a markdown on Direct shrinks the spread** (FY2024 ratio of 1.654x; average markdown applied uniformly to Direct revenue):

| Average Direct markdown | 0% | 5% | 10% | 15% | 20% |
|---|---|---|---|---|---|
| Spread as % of Direct revenue | 39.5% | 36.4% | 32.8% | 28.9% | 24.4% |

Each additional 5 points of average markdown removes 3.1 to 4.5 points of the Direct spread, and the loss grows as markdowns deepen. Whether Direct still beats wholesale at a given markdown depends on Direct's own cost to serve, which Test 3 benchmarks with peers.

## Test 2: Nike's own gross margin bridge isolates the Direct effect

From FY2022 to FY2024, Nike quantified "margin in our NIKE Direct business" as a separate line in its gross margin bridge. The figure is the year-over-year change in Nike, Inc. gross margin attributable to Direct.

| Period | NIKE Direct margin effect on company gross margin | Nike's stated reason | $ impact (bps x revenue) | Source |
|---|---|---|---|---|
| Q3 FY2022 | **+140 bps** | "lower promotional activity ... reflecting limited available for sale inventory due to supply chain constraints" | +$152M | Q3 FY22 10-Q p. 30 |
| 9M FY2022 | **+160 bps** | same | **+$552M** | Q3 FY22 10-Q p. 30 |
| Q1 FY2023 | **-90 bps** | "higher promotional activity in North America" | -$114M | Q1 FY23 10-Q p. 24 |
| Q2 FY2023 | **-160 bps** | "higher promotional activity ... largely in North America to liquidate excess inventory" | -$213M | Q2 FY23 10-Q p. 28 |
| Q3 FY2023 | **-140 bps** | "higher promotional activity to liquidate inventory" | -$173M | Q3 FY23 10-Q p. 29 |
| 9M FY2023 | **-130 bps** | same | **-$499M** | Q3 FY23 10-Q p. 29 |
| Q1 FY2024 | +10 bps | n/a | +$13M | Q1 FY24 10-Q p. 24 |
| Q2 FY2024 | -20 bps | n/a | -$27M | Q2 FY24 10-Q p. 28 |
| Q3 FY2024 | -50 bps | n/a | -$62M | Q3 FY24 10-Q p. 29 |
| FY2024 | **-40 bps** | "Lower margin in our NIKE Direct business" | **-$205M** | FY24 10-K p. 36 |

Revenue used for the conversions (facts CSV):
- Q3 FY22: $10,871M. 9M FY22: $34,476M.
- Q1 to Q3 FY23: $12,687M, $13,315M and $12,390M. 9M FY23: $38,392M.
- Q1 to Q3 FY24: $12,939M, $13,388M and $12,429M. FY24: $51,362M.

- **This is the direct test, and it supports the hypothesis.** The same Direct business added 160 bps of company gross margin (+$552M over nine months) when promotions were low, then subtracted 130 bps (-$499M) the next year when promotions rose. Nike names promotional activity as the cause in every one of these bullets. The swing is roughly **$1.05 billion of gross profit** between the two nine-month periods (my arithmetic).
- **Full-price pricing was rising over the same period.** Nike's wholesale-equivalent full-price ASP added +200 bps in Q1 FY2023, +410 bps in Q2 and +370 bps in Q3 (Q1 FY23 10-Q p. 24; Q2 FY23 10-Q p. 28; Q3 FY23 10-Q p. 29). The Direct drag came from markdowns, not from lower list prices.

## Test 2b: FY2025 onward, the wholesale shift trades price for cost

From FY2025 Nike stopped isolating Direct margin. Instead its bridge shows two opposing channel effects:

| Period | NIKE Brand ASP effect (includes channel mix) | Warehousing and logistics effect | Source |
|---|---|---|---|
| FY2025 | -180 bps, "primarily due to higher discounts and changes in channel mix" | +20 bps | FY25 10-K p. 35 |
| Q1 FY2026 | -250 bps | +50 bps | Q1 FY26 10-Q p. 22 |
| Q2 FY2026 | -50 bps | +50 bps | Q2 FY26 10-Q p. 27 |
| Q3 FY2026 | +80 bps | +20 bps | Q3 FY26 10-Q p. 30 |
| FY2026 | not a bridge line (apparel ASP rose "primarily due to product mix, partially offset by higher discounts and channel mix," FY26 10-K p. 33) | +20 bps, "primarily due to channel mix" | FY26 10-K p. 34 |
| Q1 FY2027 | -30 bps, "primarily due to higher discounts and channel mix, partially offset by strategic pricing" | **+90 bps** | Q1 FY27 10-Q p. 23 |

- **Mechanism, in Nike's words:** moving units from Direct to wholesale lowers average selling price, because Nike books the wholesale price instead of the retail price. It also lowers warehousing and logistics cost per unit.
- **What can be measured:** in Q1 FY2027 the logistics saving (+90 bps) exceeded the entire ASP drag (-30 bps), and gross margin rose 60 bps (Q1 FY27 10-Q p. 23).
- **What cannot be measured:** Nike does not split the ASP line between "higher discounts" and "channel mix." The net gross margin effect of the channel shift alone is therefore not disclosed. It is also a gross margin view; store and digital operating costs sit in operating overhead, which Nike does not split by channel.

## Test 3: peer benchmarks

Full tables, quotes and URLs: `research_notes/10_peer_channel_margins.md`. Peer filings were read from annual report PDFs and company IR documents. Every peer figure below was taken from a printed filing table, and the Skechers FY2024 and Deckers FY2018 to FY2024 segment figures were re-checked against the downloaded PDFs.

**3a. Gross margin: DTC beats wholesale by about 17 to 30 points, and discounting has not closed that gap at any peer.**

| Skechers (only peer reporting gross margin by channel) | FY2019 | FY2021 (recast) | FY2022 | FY2023 | FY2024 | H1 2025 |
|---|---|---|---|---|---|---|
| DTC gross margin | 59.6% | 66.1% | 65.6% | 66.0% | 66.2% | 66.5% |
| Wholesale gross margin | 42.9% (derived) | 38.2% | 36.0% | 41.0% | 43.3% | 42.8% |
| Gap (points) | 16.7 | 27.9 | 29.6 | 25.0 | 22.9 | 23.7 |

Sources: Skechers FY2019 10-K pp. 35, 74; FY2022 10-K pp. 19, 43; FY2023 10-K p. 46; FY2024 10-K p. 47; Q2 2025 10-Q segment table.

- **Nike cross-check (derived, with one assumption).** With the same unit cost in both channels, the gross margin gap equals (1 minus wholesale gross margin) times the Direct spread from Test 1. Nike's FY2024 spread was 39.5%. Assuming a Nike wholesale gross margin of 35% to 45%, the implied Nike gap is **21.7 to 25.7 points**, in line with Skechers' 22.9 points in FY2024. Nike's channel economics look like Skechers' at the gross margin line.
- **Discount effects are single-digit points:**
  - Skechers DTC gross margin rose 590 bps in FY2021 on "reduced promotional activity" (FY2021 10-K p. 19, original basis).
  - Under Armour lost about 130 bps of gross margin to "increased promotional activities within our direct-to-consumer channel" (FY2024 10-K) and regained 80 bps from less DTC discounting (FY2025 10-K).
  - Nike's own swing was +160 bps to -130 bps of company gross margin (Test 2).
  - None of these comes close to a 17 to 30 point gap.

**3b. Operating margin: DTC loses to wholesale when its costs are not covered.**

| Deckers (UGG, HOKA), segment operating margin | FY2018 | FY2019 | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 |
|---|---|---|---|---|---|---|---|
| DTC | 21.9% | 25.9% | 24.8% | 32.8% | 35.9% | 34.7% | 40.3% |
| Wholesale (five brand segments combined) | 25.7% | 29.7% | 29.8% | 30.6% | 27.1% | 27.1% | 30.3% |
| Gap (points) | **-3.8** | **-3.8** | **-5.0** | +2.2 | +8.8 | +7.6 | +10.1 |

Sources and notes:
- Segment net sales and income from operations come from the FY2020 10-K p. F-41, FY2022 10-K pp. F-38 to F-39 and FY2024 10-K p. F-38. All margins are derived.
- Deckers transfers product to DTC "at the Company's cost," so the DTC segment carries the full brand-plus-retail margin. This is the closest public analogue to a Nike channel P&L.
- Warehouse and distribution-centre costs are unallocated, so DTC is somewhat overstated.

- **For three years DTC earned *less* than wholesale despite its higher gross margin.** Deckers then credits the turn to "higher-full priced selling driven by less discounting and promotional activity" (FY2019 10-K p. 39), "lower overall retail store operating costs driven by store closures" (p. 40) and later "higher full-price sell through" (FY2024 10-K p. 35). The filings do not separate the price effect from the store-closure and e-commerce-mix effects.
- **PUMA's CFO describes the mechanism (opinion):** channel mix is "basically a swap between the OpEx and the gross profit margin side on DTC versus Wholesale" (PUMA Q1 2025 aide-memoire p. 3).

**3c. What a wholesale partner keeps (the break-even benchmark).**

| | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 |
|---|---|---|---|---|---|---|
| Foot Locker gross margin | 31.8% | 28.9% | 34.4% | 31.9% | 27.7% | 28.9% |
| Nike share of Foot Locker purchases | 71% | 75% | 68% | 65% | 65% | 59% |

Source: Foot Locker 10-Ks (detail file). Dick's gross margin was 29.2% to 38.3% from FY2019 to FY2024.

US retailers include store occupancy in cost of sales, so this is a floor on the share of the shelf price a retailer captures.

**Break-even markdown (derived, assumption stated).** Assume NIKE Direct's cost to run stores and digital fulfilment, as a share of its revenue, is similar to what a large sneaker retailer needs to cover. Then Direct beats wholesale only while its spread over wholesale stays above that retailer's gross margin. Using the Test 1 FY2024 ratio of 1.654x, the spread falls to:
- Foot Locker's FY2024 gross margin (28.9%) at an average Direct markdown of about **15%**.
- Its FY2023 gross margin (27.7%) at about **16%**.
- Its FY2021 full-price-year gross margin (34.4%) at about **8%**.

## Verdict

1. **The strong form is wrong.** "Discounting erases the Direct *gross margin* advantage" is contradicted by every data set:
   - Even in FY2023, its most promotional year, NIKE Direct still sold at 1.67x the wholesale value (Test 1).
   - Skechers' DTC gross margin stayed 17 to 30 points above wholesale through every promotional cycle.
2. **The defensible form, which the case should use:** NIKE Direct beats wholesale at the *operating* level only while its spread over wholesale exceeds its own cost to serve, and promotions consume that cushion. The supporting evidence:
   - **Nike:** the Direct line in Nike's gross margin bridge went from +160 bps to -130 bps of company gross margin, a swing of about $1.05 billion, on promotional activity alone (Test 2).
   - **Deckers:** DTC earned 3.8 to 5.0 points *less* than wholesale at the operating level until full-price selling returned and stores closed (Test 3b).
   - **Break-even:** on a Foot Locker-sized cost to serve, the cushion runs out at an average Direct markdown of roughly 8% to 16% (Test 3c).
3. **Implication for Nike's pivot (data-based, not proven).** Nike moved volume to wholesale while its Direct business was promotional and shrinking:
   - Digital fell from $12.6 billion to $8.6 billion (`05_channel_split.md` Section 2).
   - Nike-owned store comparable sales fell 4% in FY2026.

   That is the Deckers FY2018 to FY2020 pattern, where fixed store and fulfilment costs are spread over less full-price revenue. The pivot is consistent with the data if Nike's Direct markdowns were above the 8% to 16% range. Nike does not disclose average markdown depth, so the case should present this as a threshold to monitor, not a fact.
4. **What would change the conclusion:** a disclosure of Nike's Direct operating costs, or average markdown depth, at the November 2026 Investor Day.
