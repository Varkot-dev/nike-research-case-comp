# DICK'S Sporting Goods (DKS) incl. Foot Locker: evidence on "Jordan supply cut" vs "demand collapse", and on Nike NA wholesale sell-in vs sell-through

Prepared 2026-10-13. Scope: DKS FY2022 10-K through Q2 FY2026 10-Q (quarter ended Aug 1, 2026, filed Sep 3, 2026), all earnings Ex. 99.1, and call transcripts for Q4 FY25, Q1 FY26 and Q2 FY26.

This note builds on origin/claude/wonderful-franklin-u31n4e:research_notes/thesis_tests/retailer_sell_through.md (the "prior note"). I re-opened and re-checked its DKS numbers (all matched) and avoided repeating it. New here:
- call-transcript evidence (launch count vs launch sell-through, allocation, the "legacy silhouette" inventory glut);
- a Foot Locker sales vs inventory calculation using Foot Locker's own XBRL;
- the first-half seasonal inventory build comparison;
- a keyword check for Jordan.

## Labels and sources
- VERIFIED = I opened the document myself.
- SNIPPET ONLY = seen only in a search result.
- UNVERIFIED = not checked.
- DERIVED = my own calculation.
- Filings were downloaded from SEC EDGAR to scratchpad/rh/dicks/dl and converted to paged text with scripts/sec_pipeline/topages.py (pages/). DKS printed page = sequential page. Earnings releases are cited "ER p. N", counted from page 1 of the exhibit.
- Transcripts:
  - Q2 FY26 call (2026-08-25): opened two independent automated transcripts, webull.com/news/15463631008252928 and earningswhispers.com/transcript/DKS/Q22026. The FactSet PDF on s27.q4cdn.com returned 403.
  - Q1 FY26 call (2026-05-27): opened the Benzinga full transcript (cdn4.benzinga.com/insights/news/26/05/52805610).
  - Q4 FY25 call (2026-03-12): opened the Motley Fool transcript on aol.com/articles/dicks-dks-q4-2025-earnings-154803123.html.
  - All transcript text was read through a WebFetch extraction step, so quotes are labelled VERIFIED (opened; automated transcript). Speaker spellings in those transcripts are imperfect.
  - Q3 FY25 call: InsiderMonkey was paywalled, and GuruFocus and AlphaStreet returned 403 or 503. For that call I rely on the prior note's SGB Media quotes.
- Per the RULES_UPDATE, no email address was sent in any request after the update. Foot Locker data came from data.sec.gov XBRL with a generic User-Agent.

## 1. Vendor concentration (VERIFIED)
| Fiscal year (DKS) | Nike share of merchandise purchases | Source |
|---|---|---|
| FY2022 | ~23% | 10-K FY22 p. 7: "with Nike, our largest vendor, representing approximately 23% of our merchandise purchases" |
| FY2023 | ~24% | 10-K FY23 p. 7 |
| FY2024 | ~25% | 10-K FY24 p. 7 |
| FY2025 (incl. Foot Locker from Sep 8, 2025) | ~31% | 10-K FY25 p. 9: "approximately 31% of our consolidated merchandise purchases within the DICK'S and Foot Locker Businesses" |

New risk-factor language in the FY25 10-K (p. 22): "any adverse development in a key supplier's brand power, reputation, financial condition, product innovation, or manufacturing capability, or its decision to change its distribution or allocation strategies, could materially adversely affect our business." DKS explicitly flags allocation strategy as a risk.

Jordan first appears in the DKS brand list in the FY23 10-K (p. 7, "Jordan, New Balance, Nike"). It is not in the FY22 list (p. 7).

## 2. Inventory growth vs sales growth by quarter (DERIVED from VERIFIED ERs)
DKS quarters are offset from Nike's. Nike Q1 FY27 (Jun to Aug 2026) is roughly DKS Q2 FY26 (May 3 to Aug 1, 2026). Nike Q2 FY26 (Sep to Nov 2025) is roughly DKS Q3 FY25.

### DICK'S Business (standalone before Sep 2025)
| DKS quarter | Approx. Nike quarter | Sales yoy | Inventory yoy | Comp |
|---|---|---|---|---|
| Q1 FY24 | Q4 FY24 | +6.2% | +6% | +5.3% |
| Q2 FY24 | Q1 FY25 | +7.8% | +11% | +4.5% |
| Q3 FY24 | Q2 FY25 | +0.5% | +13% | +4.2% |
| Q4 FY24 (vs 14-wk) | Q3 FY25 | +0.5% | +18% | +6.4% |
| Q1 FY25 | Q4 FY25 | +5.2% | +12% | +4.5% |
| Q2 FY25 | Q1 FY26 | +5.0% | +7% | +5.0% |
| Q3 FY25 | Q2 FY26 | +5.9% (segment) | +2% | +5.7% |
| Q4 FY25 | Q3 FY26 | +4.0% (segment) | +1% | +3.1% |
| Q1 FY26 | Q4 FY26 | +6.4% (segment) | +3% | +6.0% |
| Q2 FY26 | Q1 FY27 | +5.6% (segment) | +6% | +4.9% |

- Segment sales are from ER segment tables: ER Q3 FY25 p. 5, ER Q4 FY25 p. 5, ER Q1 FY26 p. 3, ER Q2 FY26 p. 4.
- Segment inventory growth is from the ER footnotes, for example ER Q2 FY26 p. 3: "Inventory increased 6% for the DICK'S Business as compared to August 2, 2025."
- Reading: through all of Nike FY26 and Q1 FY27, DICK'S own inventory grew at or below its sales. There is no inventory build at DICK'S.
- CFO Navdeep Gupta, Q2 FY26 call (2026-08-25): "Inventory for the Dick's business was up 6% in line with our total sales growth." VERIFIED (automated transcript; same wording in both).
- The DICK'S build happened earlier, in FY24 (inventory up 11% to 18% vs sales up 0.5% to 8%). That is before Nike's NA wholesale acceleration, and it cleared with merchandise margin up (prior note).

### Foot Locker Business
Prior-year figures are Foot Locker standalone, from Foot Locker XBRL companyfacts (CIK 850209): InventoryNet and RevenueFromContractWithCustomerExcludingAssessedTax. DKS reports Foot Locker inventory rounded to $0.1B, so the inventory changes are given as ranges.

| DKS quarter | FL sales (DKS) vs FL standalone prior year | FL inventory vs prior year | Pro forma comp |
|---|---|---|---|
| Q3 FY25 (stub period, sales not comparable) | n/a | $1.8B vs $1,744M: +0% to +6% | -4.7% |
| Q4 FY25 | $2,175.3M vs $2,248M: -3.2% | $1.5B vs $1,525M: -5% to +2% | -3.4% |
| Q1 FY26 | $1,787.1M vs $1,794M: -0.4% | $1.7B vs $1,665M: -1% to +5% | +0.6% |
| Q2 FY26 | $1,736.9M vs $1,857M: -6.5% | $2.0B vs $1,709M: **+14% to +20%** | -3.6% |

- Sources: ER Q2 FY26 p. 3 note (4), "$3.6 billion for the DICK'S Business and $2.0 billion for the Foot Locker Business"; ER Q2 FY26 p. 4 segment table; ER Q1 FY26 p. 3.
- Seasonal check (DERIVED). The Feb to Aug inventory build was $1,525M to $1,709M (+12%) in 2025 for Foot Locker standalone. In 2026 it was $1.5B to $2.0B, or +26% to +41% (midpoint +33%).
- Caveats:
  - Foot Locker sales fall partly because of store closures: 84 North America closures in H1 FY26 (10-Q Q2 FY26 p. 24).
  - DKS applies the retail inventory method to Foot Locker (10-Q p. 16 note 3), so the bases differ slightly.
  - Even with both caveats, an inventory gain of about 20 points against a sales decline of about 6.5% in the Nike Q1 FY27 window is a build.
- Consolidated cash flow, 26 weeks: "Inventories (662,488)" vs "(54,084)" a year earlier (10-Q Q2 FY26 p. 8). VERIFIED.
- Foot Locker segment gross margin: 27.9% in Q1 FY26 (DERIVED, 498.7/1,787.1, ER Q1 FY26 p. 3) fell to 25.66% in Q2 FY26 (10-Q p. 28). That is about -225 bps quarter on quarter (DERIVED; not seasonally adjusted).

## 3. Launch count vs launch sell-through: the decomposition the thesis needs
The thesis needs the Foot Locker/retro weakness split into (a) fewer units offered and (b) lower sell-through per unit offered. DKS names both drivers in one sentence and quantifies neither.
- ER Q2 FY26 p. 1, Ed Stack (VERIFIED): "This environment had a more significant impact on the Foot Locker Business given its greater exposure to legacy footwear silhouettes and greater dependence on footwear launch and retro product. Not only were there fewer launches in the second quarter, but those launches performed below both industry and our expectations."
- Q2 FY26 call, CFO Gupta: Foot Locker results were hit by "fewer launches and weaker consumer response to key launches during the quarter." VERIFIED (automated transcript).
- Q2 FY26 call, Stack: "the launch product in Q2 was disappointing in the marketplace, not just for us, but for the entire marketplace." VERIFIED (automated transcript).
- Interpretation:
  - (a) "Fewer launches" fits a deliberate supply cut.
  - (b) "Performed below both industry and our expectations" is a sell-through shortfall on the product that was offered. A pure scarcity strategy predicts the opposite: fewer launches selling out faster.
  - DKS gives no launch count, unit or sell-through rate, so the split between (a) and (b) cannot be computed from DKS disclosures.

## 4. The inventory glut is in legacy silhouettes, and brands are discounting on their own sites
- 10-Q Q2 FY26 p. 21, Business Environment (VERIFIED): "As demand shifted during the quarter, inventory grew within the industry, particularly in certain legacy footwear silhouettes and apparel franchises that are not resonating with our athletes the way they once did, resulting in an increasingly aggressive promotional environment for key athletic brands and across the retail marketplace."
- This sentence is new. The Q1 FY26 10-Q Business Environment (p. 20) mentions only macro, tariffs and fuel. So the shift happened in May to July 2026.
- Q2 FY26 call, Stack (VERIFIED, automated transcript):
  - "inventory levels were building up across parts of the industry, leading to a much more promotional environment."
  - "a number of brands got very promotional on their sites and those promotions spilled into the broader marketplace."
  - "I've never seen the specialty channel of distribution so promotional in my career" (quoting a brand).
  - "We're not leading this margin erosion."
- Relevance: a deliberate cut in retro supply would leave legacy/retro product scarce and at full price. DKS describes the opposite: excess legacy inventory across the industry, discounted on brand-owned sites. Brand-owned sites include Nike's, though Stack did not name Nike as a promoter.

## 5. Jordan specifically
- **Keyword check.** "Jordan", "AJ1", "Dunk" and "Air Force 1" do not appear in the Q2 FY26 call transcript (both versions checked). "Jordan" does not appear in the Q1 FY26 transcript.
- **Only Jordan mention found on the Q4 FY25 call (2026-03-12).** Stack mentioned an "NBA All-Star activation with Nike, Jordan, Adidas, and others." VERIFIED (automated transcript).
- **No Jordan figures in any DKS filing.** The 10-Ks name Jordan only in the brand list. No DKS filing or call I opened gives Jordan sales, Jordan allocation or Jordan retro supply.
- **Limit on attribution.** Linking the "legacy silhouettes" and "retro product" weakness to Jordan specifically is an inference. DKS never names the franchises.
- **Basketball.** The positive basketball commentary is about signature and performance product, not retro:
  - Hobart, Q4 FY25 call: "Signature basketball is also doing really, really well."
  - Stack, Q1 FY26 call: "Basketball business is coming back in a really big fashion and really built around the women's basketball business."
  - Stack, Q2 FY26 call: "What we see coming from our friends from Nike in basketball, we are extremely excited about."
  - All VERIFIED (automated transcripts).
- **Launches were selling well six months earlier.** Q4 FY25 call (2026-03-12), Stack: "a series of sought-after launches that drove exceptional sell-throughs," with the example "an Air Force 1 in color." VERIFIED (automated transcript). The launch problem therefore developed between Feb and Jul 2026.

## 6. Allocation: DKS reports getting MORE product, not less
- Q1 FY26 call (2026-05-27), Stack: "We did talk to brands and they got us some additional allocation of product so that we'd be in better stock." Also: "Foot Locker will now have a different allocation of product that they didn't have before."
- Q1 FY26 call, Hobart: brand support "shows up in the access, allocation and marketing support we receive."
- Q4 FY25 call (2026-03-12), Hobart: "we are increasingly getting access and allocation to really great products."
- Q2 FY26 call, Stack: "Some of the brands have provided us additional product, higher heat product that we can sell at full price." The brands are not named. Separately, Stack said "greater allocation" referring to Ugg and Birkenstock.
- All VERIFIED (automated transcripts).
- This matches Nike's "expanded distribution, higher shipments to existing partners" in North America. The largest Nike partner says its allocation went up through Feb to Jul 2026.

## 7. Analyst Q&A on footwear and Nike, Q2 FY26 call (2026-08-25)
All VERIFIED (automated transcripts). Management answers are opinion.
- **Simeon Gutman (Morgan Stanley), on footwear demand.**
  - Stack: "I don't think this is a demand issue going forward from a footwear standpoint." "some of these older legacy silhouettes and franchises that have done so well have slowed." "But I think this is temporary."
- **Christopher Horvers (JPMorgan), on a "hangover" from new running silhouettes.**
  - Stack: "I think the hangover, we have the hangover right now."
  - Hobart: "the running category in itself and all performance is doing really well ... this is focused on the lifestyle legacy silhouettes that aren't doing well."
- **Adrian Yee (Barclays), on whether DKS is cancelling orders.**
  - Stack: "we are modifying some orders here and there, but nothing really out of the ordinary."
  - Stack also: "The lifestyle has been a bit more of an issue."
- **Lorraine Hutchinson (BofA), on Foot Locker margins.**
  - Stack: "if a shoe is at a certain price in the marketplace, then we feel we need to be competitively priced."
- **Guidance change (VERIFIED, ER Q2 FY26 p. 5; 10-Q p. 22).**
  - Foot Locker FY26 pro forma comp: cut to -2% to 0%, from +1.5% to +3%.
  - Foot Locker segment: loss of $(80)M to $(40)M.
  - DICK'S comp guidance: unchanged at +2.5% to +4.0%.
  - DICK'S gross margin pressure "most pronounced in the third quarter."

## 8. Other DKS context (VERIFIED)
- **DICK'S comp drivers, Q2 FY26** (10-Q p. 28): "+3.6% increase in sales per transaction and a 1.3% increase in transactions," with "broad-based growth across footwear, apparel and hardlines, including strong results from the 2026 FIFA World Cup and trading cards."
  - Price/mix is the larger driver.
  - DICK'S merchandise margin was +137 bps, mainly from IEEPA tariff refunds. So full-price selling at DICK'S is not shown clean of one-offs.
- **House of Sport:** 35 to 41 stores in H1 FY26 (10-Q p. 24).
- **Foot Locker clean-up charges:**
  - $217.9M to write down and liquidate Foot Locker inventory in FY25 (10-K FY25 p. 39).
  - $42.7M in Q1 FY26 (10-Q Q1 FY26 p. 20); $40.4M year to date in H1 FY26 (10-Q Q2 FY26 p. 21).
- **Foot Locker inventory acquired at close:** $1,718.1M (10-Q Q2 FY26 p. 11, purchase price allocation).
- **Q1 FY26 call:**
  - Stack: "our inventory is in terrific shape."
  - Q1 FY26 Foot Locker US banner comp: +6.4% (Stack and Gupta, automated transcript).
  - That optimism reversed within one quarter.

## 9. Conclusions
1. **NA wholesale sell-in vs sell-through.**
   - At DICK'S Business the growth is real sell-through: inventory was +1% to +6% against sales of +4% to +6.4% in every quarter that overlaps Nike FY26 and Q1 FY27.
   - At Foot Locker, in the Nike Q1 FY27 window, inventory rose +14% to +20% while sales fell 6.5% and comps fell 3.6% (DERIVED).
   - The H1 inventory build was about 2.7x last year's seasonal build (midpoint +33% vs +12%).
   - Management said allocations were increased.
   - So part of Nike's NA wholesale growth into the combined account in mid-2026 is channel fill at Foot Locker, not consumer sell-through.
   - DKS does not split inventory by brand, so the Nike share of that build is not measurable. Nike was about 59% of Foot Locker purchases in FY24 (prior note).
2. **Supply cut vs demand collapse.** DKS evidence does not support a pure "deliberate supply cut" story for retro/legacy product.
   - Three findings point against it:
     - DKS says launches were fewer AND underperformed.
     - Industry inventory grew specifically in legacy silhouettes.
     - Brands were discounting that product on their own sites.
   - Equally, DKS evidence does not show a broad "demand collapse" for Nike:
     - Performance, running and signature basketball are described as strong (management opinion).
     - DICK'S footwear grew.
     - DICK'S comps stayed at +4.9%.
   - The most defensible reading: a supply reduction in launches combined with weaker per-launch and legacy-lifestyle sell-through. DKS gives no units, so the mix between the two cannot be quantified from DKS.
   - Jordan is never named as the problem franchise, so any Jordan attribution is inference.
3. **What would settle it.**
   - Nike's own Jordan unit vs ASP split, and Nike Direct markdown rates.
   - Resale premiums on Q2 2026 Jordan retro releases (StockX/GOAT).
   - Foot Locker brand-level inventory, which DKS does not disclose.
