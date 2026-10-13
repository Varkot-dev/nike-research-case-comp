# Jordan Brand: the scarcity reset thesis

**Prepared:** October 13, 2026. **Sources:** Nike 10-Ks FY2017 to FY2026, the Q1 FY2027 10-Q, earnings releases, and Nike's official earnings call transcripts (Q4 FY23, Q4 FY24, Q1 FY25 to Q1 FY27), plus opened secondary pages. Full extracts with verbatim quotes, URLs and verification status: `research_notes/jordan_extracts/JORDAN_SEC_FINDINGS.md` and `research_notes/jordan_extracts/JORDAN_MARKET_FINDINGS.md`. Chart: `charts/16_jordan_resets.png`. Labels follow the house rules: filing citations, *Nike transcript*, *secondary*, *my arithmetic*, *my inference*.

## 1. The thesis in one paragraph

Jordan is Nike's only disclosed sub-brand and roughly 15% of revenue. It is down 19% from its FY2024 peak, and management says it fell by mid-teens again in Q1 FY2027. Most readers see the headline "-3% in FY2026" and miss the size of the drop, because Nike changed how it reports Jordan in FY2025. **Our claim:** the decline is mainly a supply decision, not a demand collapse, and Nike has run this exact play once before. In FY2018 it cut Jordan supply, revenue fell 8%, and Jordan then grew about 2.3x from that trough to FY2024 on a like-for-like basis. The current reset is about two and a half times as deep and is still under way, so the payoff is larger but later. Our estimate is that Jordan sells about half its volume through NIKE Direct, more than the rest of Nike. That makes it the franchise most tied to the digital collapse, and the one that gains most if the full-price digital reset works. The thesis is falsifiable within two to three quarters (Section 7).

## 2. The number most people have wrong

- **Headline:** "Jordan Brand products of $7,034 million, $7,270 million and $8,701 million in fiscal 2026, 2025 and 2024, respectively, decreasing 3% and 16% on a reported basis" (FY26 10-K p. 32, footnote 3).
- **Why it looks smaller than it is:** until FY2024, Nike reported Jordan on a *wholesale equivalent* basis, which priced Jordan sold through NIKE Direct at an internal wholesale price. From Q1 FY2025 "we have removed the non-GAAP financial measure of wholesale equivalent revenues" (Q1 FY25 10-Q p. 19), and prior years were "recast to conform to fiscal 2025 presentation" (FY25 10-K p. 33). FY2024 Jordan went from $6,988M (FY24 10-K p. 34) to $8,701M; FY2023 from $6,589M to $8,460M (FY25 10-K p. 33).
- **Consequence:** anyone chaining the old FY2024 figure ($6,988M) to the new FY2025 figure ($7,270M) sees growth of 4%. The filed figure is -16%. On a consistent basis, Jordan is **19% below peak** after FY2026 (my arithmetic: $7,034M / $8,701M).
- **Q1 FY2027:** "the Jordan Brand represented 13% of our global business with revenue falling by mid-teens" (Nike transcript, Q1 FY27 call, Oct 1, 2026). If the full year fell mid-teens, Jordan would be about $6.0B, roughly 31% below peak (my arithmetic, illustrative; Nike gives no full-year Jordan guidance).
- A second, smaller break: from FY2022, "unisex products are classified within Men's, and Jordan Brand revenues are separately reported" (FY22 10-K p. 32), moving FY2021 from $4,711M to $4,780M.

**Repo data note:** `revenue_jordan` in `data/nike_filing_facts.csv` holds each year's first-reported figure, so FY2023 and FY2024 are on the old basis and FY2025 and FY2026 on the new one. Use `revenue_jordan_reported_basis` (FY2023 to FY2026, added Oct 13, 2026) for any trend across FY2024 and FY2025.

## 3. The precedent: the FY2018 reset

| Fiscal year | Jordan growth (as filed) | Source |
|---|---|---|
| FY2018 | -8% | FY19 10-K p. 27 |
| FY2019 | +10% | FY19 10-K p. 27 |
| FY2020 | +15% | FY20 10-K p. 31 |
| FY2021 | +30% (recast) | FY22 10-K p. 32 |
| FY2022 | +7% | FY22 10-K p. 32 |
| FY2023 | +29% | FY23 10-K p. 32 |
| FY2024 | +3% (reported basis) | FY25 10-K p. 33 |
| FY2025 | -16% | FY26 10-K p. 32 |
| FY2026 | -3% | FY26 10-K p. 32 |

- Nike's own account: "Back in Fiscal 18, we recalibrated the supply of select Jordan Brand franchises ... we turned the page from double-digit declines in the Brand to the start of multiple consecutive years of strong double-digit growth" (Nike transcript, Q4 FY24 call, June 2024).
- On a like-for-like chain, Jordan was back above its FY2017 level within two years of the FY2018 reset and was about 2.3x its FY2018 trough by FY2024 (my arithmetic; chart 16).
- **The same playbook, stated explicitly in October 2026:** "we're going to get back to leading the scarcity model that we created. Simply put, we've been oversupplying our iconic retro product ... as we've done with the Air Jordan 1, we will deliberately reduce the volume and frequency of specific Jordan Retro launches. We've discussed it with our wholesale partners ... In the near term, North America will feel the biggest impact" (Nike transcript, Q1 FY27 call).
- **What is different this time (my inference):** the FY2018 reset was one year at -8%. This one is already two years and about -19%, with a further mid-teens drop in Q1 FY2027 and a second round of cuts. The 10-Q says "additional actions related to NIKE Sportswear and Jordan Brand are expected to extend beyond fiscal 2027," reflecting "higher levels of discounting and broader marketplace pressure" (Q1 FY27 10-Q p. 20). A deeper reset means a bigger rebound if the model holds, and a longer wait.

## 4. New estimate: Jordan is Nike's most DTC-dependent franchise

Nike does not disclose Jordan by channel. The FY2025 restatement lets us estimate it.

**Method (my inference):**
- The restatement replaced internal transfer prices with actual NIKE Direct retail revenue, so for any brand, *restated minus old* = Direct retail revenue minus the internal price of the same goods.
- For NIKE Brand as a whole in FY2024: internal sales to NIKE Direct were $13,009M (FY24 10-K p. 34) against NIKE Direct revenue of $21,519M (FY24 10-K p. 34). Internal price was therefore about 60.5% of Direct retail revenue (my arithmetic). The restatement check works: total NIKE Brand reported revenue ($49,322M) minus total wholesale equivalent revenue ($40,767M, FY24 10-K p. 34) is $8,555M, close to $21,519M minus $13,009M ($8,510M).
- Jordan's restatement gap was $1,713M in FY2024 and $1,871M in FY2023. Assuming Jordan's internal price ratio matches Nike's average, Jordan's Direct revenue was $1,713M / (1 - 0.605), about **$4.3B, or about 50% of Jordan revenue in FY2024**. FY2023 gives about 55%. NIKE Brand overall was 43.6%.

| Assumed internal price as % of Direct retail | 50% | 55% | 60.5% (Nike average) | 65% | 70% |
|---|---|---|---|---|---|
| Implied Jordan Direct share, FY2024 | 39% | 44% | 50% | 56% | 66% |

- **The robust part**, which needs only the "same ratio" assumption: Jordan accounted for 20% of the FY2024 restatement gap and 22% of FY2023's, against 17.6% and 17.3% of NIKE Brand revenue (my arithmetic). Jordan over-indexes to NIKE Direct either way.
- **Why it matters:**
  1. NIKE Brand Digital fell 32% from its FY2023 peak to $8.6B in FY2026 (`05_channel_split.md`). Retro launches were the core of the SNKRS and app model, so the Jordan decline and the digital decline are largely the same story told twice.
  2. Jordan is therefore the brand most exposed to Nike's shift from Direct to wholesale, and North America, where Direct has fallen every quarter since Q4 FY2024, is where "North America will feel the biggest impact."
  3. If the full-price digital reset works, Jordan has the most to gain: scarcity is easiest to enforce in channels Nike controls.
- **Caveats:** if Jordan's Direct sales ran at deeper discounts than average (factory stores), its internal price ratio is higher and the Direct share is higher still. If Jordan includes a larger mix of kids' or lower-priced product sold Direct, it could be lower. Treat 45% to 55% as the working range.

## 5. Bull case anchors

1. **Precedent and intent.** The FY2018 reset worked (Section 3) and management is using the same words now.
2. **Room outside North America.** "In most of our geos, Jordan penetration is about 10 points lower than it is in North America" (Nike transcript, Q4 FY23 call, June 29, 2023).
3. **Proof that scarcity still sells at full price.** Hill on the AJ4 Black Cat: "that was our largest Black Friday ever" (Nike transcript, Q2 FY26 call, Dec 18, 2025); AJ11 Gamma and AJ5 Wolf Grey had "high full price realization and really strong sell-through" (Nike transcript, Q3 FY26 call, Mar 31, 2026). The AJ1 and Air Force 1 "stabilized this quarter" after their earlier cuts (same call).
4. **New sport categories.** Hill: "dimensionalize the brand through sport, and we're already seeing some success in growth in our ... cleated business, our golf business, our training business" (Nike transcript, Q1 FY27 call). Brazil's 2026 World Cup away kit is a Jordan kit, the first federation to partner with Jordan (Nike transcript, Q3 FY26 call; secondary: SI, Mar 13, 2026). Tony Finau moved to Jordan in golf (secondary: PGA Tour, Jan 15, 2026). The first U.S. World of Flight store opened in Philadelphia, with more planned (Nike release, Oct 2, 2025).
5. **Category-wide softness.** The weakness is not unique to Jordan: secondary reports put adidas basketball down 21% currency-neutral in Q2 2026 (unverified on adidas' own filing; check before citing).
6. **Aligned founder economics.** Forbes and Sportico estimates of Michael Jordan's Nike income ($130M on FY2019, $260M for 2023, $275M for 2025) imply about 4% of Jordan revenue, not the folklore 5% (secondary; my arithmetic). His income falls with the reset, so he has no incentive to push volume. No Nike filing discloses the arrangement.

## 6. Bear case anchors

1. **The reset keeps getting bigger.** Classic franchises were already "on track to decline from peak levels by more than $4 billion" (Nike transcript, Q2 FY26 call), yet Jordan needed a second round of cuts in October 2026. Telsey: "an inflection back to sales growth is now not likely until calendar 2028, at the earliest" (analyst via secondary: Sherwood News, Oct 5, 2026).
2. **It is not only Jordan.** "Sportswear and Jordan Streetwear ... together, they represent approximately half of our revenue" (Nike transcript, Q4 FY26 call); in Q1 FY27 they were "a high single-digit drag on consolidated NIKE" (Q1 FY27 call).
3. **The resale signal faded before the cuts.** StockX's average resale premium on new AJ1 Retro High releases fell "from a high of 61 per cent in 2020 to 4 per cent in 2023" (Reuters citing Altan Insights, via secondary). Needham found retro Jordans "selling slowly" and discounted on StockX and GOAT (analyst via secondary: SGB, Jun 18, 2025). No systematic resale index after 2023 was found.
4. **Volume is still high.** Sole Retriever counts relayed by a sneaker blog show about 10 Jordan retro releases a month from October 2025 to September 2026, with AJ1 High retro colorways only cut from 20 (2021) to 12 (2026) (secondary; low-tier source).
5. **Brand heat.** No Nike or Jordan product or brand appears in the Lyst Index Q2 2026 top 20 brands or top 10 products (data provider: Lyst). Stephen Curry signed a reported 10-year deal with Li-Ning that includes Curry Brand stores in the U.S. (secondary: WBTV, Jun 2, 2026). Zion Williamson's signature line has reportedly ended (secondary, citing Sole Retriever; not confirmed by Nike).
6. **No margin disclosure.** Nike reports no Jordan profit or margin. Claims that Jordan is Nike's highest-margin business are unsourced and should not be used.

## 7. What would prove or disprove the thesis

| Signal | Bull reading | Bear reading | When |
|---|---|---|---|
| Nike Investor Day | Jordan revenue or margin targets; restated Jordan history | No Jordan targets | November 2026 (Nike transcript, Q1 FY27 call) |
| Jordan growth on calls | Decline narrows from mid-teens in Q2 or Q3 FY27 | Decline persists or widens | Q2 FY27 call (December 2026) |
| North America Direct growth | Turns less negative as retro cuts annualize | Keeps falling 6% or more a quarter | Each quarter (10-Q) |
| Gross margin commentary | Full-price realization cited for Jordan | Jordan cited for discounting | Each quarter |
| Retro release counts and resale premiums | Fewer releases, premiums rising on new AJ1, AJ4, AJ11 | Release counts flat, premiums near zero | Sole Retriever, StockX, monthly |
| Piper Sandler teen survey | Nike and Jordan mindshare stabilize or rise | Mindshare falls | Fall 2026 edition (timing unverified) |

## 8. How to use this in the pitch (my inference)

- **Lead with the restatement.** "Jordan was not down 3% last year; it is down 19% from peak and still falling" is a fact most of the audience will not know, and it is fully sourced.
- **Then the precedent and the channel estimate.** Nike has run this reset before (about 2.3x from trough to peak in six years) and Jordan is about half NIKE Direct, so it sits at the centre of Nike's channel reset.
- **Be explicit about timing.** The FY2018 analogue suggests recovery two years after the trough. If FY2027 is the trough, the rebound shows in FY2029 and FY2030 numbers. That supports a long-horizon thesis, not a near-term catalyst call.
- **Do not overclaim.** No Jordan margin, no sell-side Jordan estimate and no recent resale index exist in public sources we could open. A valuation should treat Jordan's recovery as a scenario input, not a forecast.
