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

*Pending: peers that report DTC and wholesale margins separately (Skechers, Deckers and others), plus retailer gross margins (Foot Locker, Dick's, JD Sports), are being collected and verified.*

## Verdict so far

1. **Supported by Nike's own numbers.**
   - When Direct sold at near full price (FY2022), it added 160 bps to company gross margin and its spread over wholesale rose to 43.7% of Direct revenue.
   - When Direct liquidated inventory (FY2023 to FY2024), the same business subtracted 130 bps and 40 bps, and the spread fell back to 39.5%.
   - Nike attributes the swing to promotional activity in every disclosure.
2. **Not yet proven.** Whether Direct beats wholesale *after* its own operating costs. A 39.5% gross spread sounds large, but stores and digital fulfilment must be paid out of it. That threshold is what the peer data (Test 3) is meant to establish.
3. **Model input for the case.**
   - Treat the Direct premium as about 39 to 40% of Direct revenue at normal promotion levels, falling about 0.6 to 0.9 points for every point of average markdown (sensitivity table).
   - The FY2022 peak of 43.7% is the best evidence of what a full-price Direct business earns.
   - For FY2025 onward, track the warehousing and logistics bridge line as the measurable benefit of the wholesale shift.
