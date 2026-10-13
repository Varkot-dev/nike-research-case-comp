# Channel, region, margin and product: where Nike makes its money (FY2019 to Q1 FY2027)

**Prepared:** October 13, 2026. **Companion to** `05_channel_split.md`, which covers the NIKE Direct versus wholesale revenue split itself. This note asks the follow-on questions: which regions earn the best margins, whether a higher Direct share goes with better margins, how product categories are moving, and what new product Nike is relying on.

**Sources.** Segment revenue, channel split, EBIT and gross margin come from `data/nike_filing_facts.csv` and `data/nike_channel_split.csv`, joined by `scripts/build_region_channel.py` into `data/nike_region_profitability.csv`, which carries the filing and page for each input. EBIT margin and Direct share are **my arithmetic** on those reported figures. Chart: `charts/15_region_ebit_margin.png`. Page numbers are printed pages.

**What Nike does not disclose.** No filing gives profit or gross margin by channel (Direct versus wholesale), or product category by channel. Every statement below about channel profitability is either Nike's own gross margin bridge language or **my inference**, and is labelled as such.

## 1. Regional profitability: the ranking has flipped

Segment EBIT as a share of segment revenue (my arithmetic). Segment EBIT excludes Global Brand Divisions and Corporate costs, so these margins are higher than Nike's consolidated EBIT margin.

| Fiscal year | North America | EMEA | Greater China | APLA | Converse |
|---|---|---|---|---|---|
| FY2019 | 24.7% | 20.3% | 38.3% | 25.2% | 15.9% |
| FY2021 | 29.6% | 21.3% | 39.1% | 28.6% | 24.6% |
| FY2023 | 25.2% | 26.3% | 31.5% | 30.0% | 27.9% |
| FY2024 | 27.2% | 24.9% | 30.6% | 28.0% | 22.8% |
| FY2025 | 24.2% | 21.0% | 24.3% | 24.4% | 14.2% |
| FY2026 | 26.2% | 19.2% | 21.9% | 22.2% | 1.5% |
| Q1 FY2026 | 22.6% | 22.1% | 24.9% | 23.5% | 10.7% |
| Q1 FY2027 | 22.8% | 22.9% | 21.0% | 22.1% | 9.5% |

Inputs: segment notes of the FY2019 to FY2026 10-Ks and the Q1 FY2026 and Q1 FY2027 10-Qs (Q1 FY27 10-Q p. 25); full citations per row in `data/nike_region_profitability.csv`.

- **Greater China went from Nike's most profitable region to one of its least.** EBIT fell from $3,243 million in FY2021 to $1,278 million in FY2026 (FY21 10-K; FY26 10-K), a 61% decline on revenue down 29% (my arithmetic). In Q1 FY2027 it was the only major region where EBIT margin fell sharply (24.9% to 21.0%).
- **North America is now the most profitable region**, at 26.2% in FY2026. Caveat: FY2026 North America EBIT includes **$965 million** of expected IEEPA tariff recovery, and Converse includes **$21 million** (FY26 10-K p. 30). Nike says the recovery "largely offsets the impact of the IEEPA tariffs recognized during fiscal 2026" (Q4 FY26 release pp. 4 to 5), so the reported figure is roughly a no-tariff view. Excluding the recovery entirely, North America's FY2026 EBIT margin would be **21.5%** (($5,376M minus $965M) / $20,511M, my arithmetic), which is the with-tariffs view.
- **Converse has almost stopped earning money.** Revenue fell from $2,427 million (FY2023) to $1,174 million (FY2026), down 52%, and EBIT from $676 million to $18 million (FY23 and FY26 10-Ks, my arithmetic). Without the $21 million tariff recovery, FY2026 Converse EBIT would be about **-$3 million** (my arithmetic).
- **EMEA has the lowest Direct share and, in FY2026, the lowest margin of the four Nike Brand regions** (19.2%), but it improved in Q1 FY2027 (22.9%) on a 140 bps gross margin gain (Q1 FY27 10-Q p. 27).

## 2. Gross margin by region (disclosed only from FY2023)

Nike began disclosing segment gross margin in the FY2025 10-K, with FY2023 comparatives.

| Fiscal year | North America | EMEA | Greater China | APLA | Converse | Source |
|---|---|---|---|---|---|---|
| FY2023 | 42.2% | 45.3% | 51.0% | 48.1% | 53.8% | FY25 10-K pp. 38 to 42 |
| FY2024 | 44.4% | 44.2% | 50.2% | 45.9% | 52.5% | FY26 10-K pp. 37 to 41 |
| FY2025 | 43.5% | 43.2% | 46.0% | 44.0% | 48.7% | FY25 10-K pp. 38 to 42 |
| FY2026 | 45.6% | 41.8% | 45.7% | 42.0% | 43.8% | FY26 10-K pp. 37 to 41 |
| Q1 FY2027 | 43.4% (+110 bps) | 44.4% (+140 bps) | 47.5% (+30 bps) | 42.3% (-150 bps) | 45.2% (-210 bps) | Q1 FY27 10-Q pp. 26 to 30 |

- **North America is the only region whose FY2026 gross margin is above FY2023**, and it is also the region that has moved furthest toward wholesale (Section 3). Every other region and Converse is down 400 to 1,000 bps since FY2023.
- **Greater China still has the highest gross margin of the Nike Brand regions** (45.7% in FY2026), yet its EBIT margin is below North America's. That gap points to operating cost deleverage (fixed store and marketing costs on falling revenue), not pricing alone (my inference).

## 3. Does more Direct mean better margins? Not on the evidence

FY2026, ranked by Direct share (my arithmetic on FY26 10-K p. 83 and the segment pages above):

| Segment | Direct share | Gross margin | EBIT margin |
|---|---|---|---|
| Greater China | 44.3% | 45.7% | 21.9% |
| Converse | 44.1% | 43.8% | 1.5% |
| North America | 41.7% | 45.6% | 26.2% |
| APLA | 39.5% | 42.0% | 22.2% |
| EMEA | 32.7% | 41.8% | 19.2% |

- **Across regions there is no clean pattern.** The two most Direct-heavy segments (Greater China, Converse) are the ones whose profits fell hardest.
- **Within North America, Direct share fell from 48.6% (FY2024) to 41.7% (FY2026) while gross margin rose from 44.4% to 45.6%.** Over the same period, Nike's bridge language shifted from Direct helping margin (FY2022: "higher margin in our NIKE Direct business," FY22 10-K p. 34) to wholesale mix lowering costs (FY2026: "Lower warehousing and logistics costs ... primarily due to channel mix," +20 bps, FY26 10-K p. 34; Q1 FY2027: +90 bps, Q1 FY27 10-Q p. 23).
- **My inference:** Direct only earns better margins when it sells at full price. Once Direct turned promotional (FY2023 onward, "higher promotional activity to liquidate inventory," FY23 10-K p. 34), its price advantage disappeared and its fulfilment and store costs remained. A smaller, full-price Direct business plus a larger wholesale business can therefore carry a *higher* margin than the FY2024 mix. Nike does not publish the data to prove this, so treat it as a stated modelling assumption.

## 4. Product categories

| | FY2024 | FY2025 | FY2026 | Change FY24 to FY26 | Q1 FY2027 vs Q1 FY2026 | Source |
|---|---|---|---|---|---|---|
| Footwear ($M) | 33,427 | 29,510 | 29,525 | -11.7% | 6,951 vs 7,410 (-6.2%) | FY24 10-K p. 34; FY25 10-K p. 33; FY26 10-K p. 32; Q1 FY27 10-Q p. 22 |
| Apparel ($M) | 13,775 | 12,965 | 13,449 | -2.4% | 3,384 vs 3,313 (+2.1%) | same |
| Equipment ($M) | 2,075 | 2,191 | 2,199 | +6.0% | 611 vs 630 (-3.0%) | same |
| Jordan Brand ($M) | 6,988 | 7,270 | 7,034 | +0.7% | n/a | FY24 10-K p. 34; FY25 10-K p. 33; FY26 10-K p. 32 |
| NIKE Brand Digital ($B) | 12.1 | 9.6 | 8.6 | -29% | 1.8 vs 2.0 | FY24 10-K p. 35; FY25 10-K p. 34; FY26 10-K p. 33; Q1 FY27 10-Q p. 23 |
| Nike-owned stores ($B) | n/a | 9.2 | 9.1 | n/a | 2.3 | FY26 10-K p. 33; Q1 FY27 10-Q p. 23 |

Percentage changes are my arithmetic.

- **The decline is a footwear problem.** Footwear accounts for almost all of the revenue lost since FY2024; apparel is roughly flat and growing again in Q1 FY2027. Currency-neutral, FY2026 footwear was -2% and apparel +2% (FY26 10-K p. 32).
- **Nike is still cutting classic franchises.** The Q1 FY2027 release announced new actions to "reposition NIKE Sportswear, Jordan Brand, and Greater China" (Q1 FY27 release p. 1), and the 10-Q says "additional actions related to NIKE Sportswear and Jordan Brand are expected to extend beyond fiscal 2027" (Q1 FY27 10-Q p. 20).

## 5. New products

<!-- NEW_PRODUCTS -->
*Pending: new product research (launches, channel and geography) is being verified and will be added here.*

## 6. What this means for the thesis (my inference)

1. **North America is the proof case for the wholesale pivot.** It moved furthest toward wholesale and is the only region with better gross margin than FY2023. If the case argues the strategy works, this is the evidence; the tariff recovery caveat must sit next to it.
2. **Greater China is the swing factor.** It used to deliver almost 40% EBIT margins; at 21% and falling on a revenue base that shrank 28% in Q1 FY2027 wholesale alone (`05_channel_split.md` Section 4), it is now the largest drag on mix.
3. **Converse is a strategic question, not a margin question.** At roughly break-even before tariff recovery, the case can reasonably ask whether Converse belongs in the portfolio.
4. **Channel margin is the missing number.** Any recommendation that depends on "wholesale is more profitable than Direct" must say this is inferred from Nike's bridge language, because Nike does not disclose it.
