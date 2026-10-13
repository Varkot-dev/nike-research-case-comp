# Root cause test: do macro and cycle effects explain Nike's decline more than Nike-specific factors?

Research date: 2026-10-13. Hypothesis under test: *Macro and cycle effects (COVID demand pull-forward, the 2022 inventory bullwhip, weaker lower-income and discretionary consumer spending, sneaker market saturation) explain the decline more than Nike-specific factors.*

Status labels:
- **REPO**: verified number already in `data/nike_filing_facts.csv`, `data/nike_channel_split.csv` or `research_notes/04_financial_data_pack.md` (filing and printed page given there).
- **REPO-NOTE**: taken from an earlier repo note, with the status that note recorded.
- **OPENED**: I read the document, data file or filing text myself in this session. This includes SEC XBRL company-facts JSON (data.sec.gov), FRED CSV downloads, Eurostat JSON, VF 10-K text pulled from EDGAR, adidas results PDFs and Nike's official call transcripts (investors.nike.com "webcast_transcript" PDFs, asset IDs 9384 to 9591), which earlier steps of this workflow downloaded and converted to text in the session scratchpad. I searched all 25 calls (Q1 FY21 to Q1 FY27) in full text.
- **SNIPPET**: seen only in a search-result summary. Treat as a lead.

All arithmetic is mine and labelled. "FY" is Nike's fiscal year ending May 31. Peer fiscal years differ and are stated.

---

## 1. Bottom line

**Verdict: minor contributor. The hypothesis as stated (macro and cycle explain more than Nike-specific factors) is falsified.** About 15 to 25% of the FY24 to FY26 revenue decline (-$4,964M) is plausibly macro or category-cycle driven. The other 75 to 85% is Nike-specific. The macro share is larger in the FY27 leg (my estimate: 25 to 40% of the guided FY27 decline), because US consumer sentiment, China retail and European promotions all worsened in 2026.

Why the hypothesis fails:
1. **Wrong timing.** The industry's COVID hangover and 2022 bullwhip hit in calendar 2022 to 2023. Adidas North America fell 16% currency-neutral in 2023, Vans fell 12% and then 24%, and US footwear dollars fell about 3% (Jan to Aug 2023, Circana). In that same window Nike grew: FY23 revenue +10% and North America +18%. Nike's decline started in Q1 FY25 (Jun to Aug 2024), *after* the industry had digested its inventory and while peers were accelerating.
2. **The market did not shrink.** US personal consumption of footwear (BEA via FRED) rose every year from 2021 to 2025: +4.4% (2022), +3.3% (2023), +1.8% (2024), +4.4% (2025). It is above its 2014 to 2019 trend line in both nominal and real terms, so there was no below-trend payback of COVID pull-forward. Circana's US footwear total was flat at $89.2B (2024) and about $90B (2025), with sport lifestyle +3% and +4%. Nike North America footwear fell 13% in FY25.
3. **Peers facing the same consumers grew.** During Nike's FY25 and FY26 decline: adidas brand +13% currency-neutral in both 2024 and 2025 (North America +10% in 2025, +15% in H1 2026); New Balance +19% to $9.2B in 2025 (North America 20%+); ASICS +19.5% (2025); On +30% (2025); Deckers +16% (FY25) and +10% (FY26); Anta +13.3% (2025); Skechers +12% (2024). The peers that fell (Puma, Vans/VF, Under Armour, Converse) each have documented company-specific resets or the same fashion-cycle exposure as Nike's classics.
4. **The demographic signature is wrong.** A lower-income squeeze should hit value brands and value channels first and spare upper-income buyers. Instead, Nike's teen share loss was steepest among *upper-income* female teens (56% to 45%, Fall 2023 to Fall 2024, Piper Sandler, REPO-NOTE), and value brand Skechers grew 12% in 2024.
5. **Nike's own managers stopped blaming macro.** "Macro" appeared 13 times on the Dec 2023 call, when Donahoe cut guidance citing "more cautious consumer behavior". In Mar 2024, CFO Friend said "we continue to have industry tailwinds". Hill (Dec 2024): "We lost our obsession with sport." Friend (Sept 2025): Q1 "didn't have anything to do with pull forwards." Hill (Mar 2026): "an expanding market." Q2 FY26: currency-neutral revenue "grew 6% excluding" the classics reduction.

What survives, in narrower form:
- **A real category (fashion) cycle in canvas and classic lifestyle sneakers.** Converse (Nike-owned) and Vans (VF-owned) both lost about half their revenue from peak: Converse -52% FY23 to FY26, Vans -49% FY22 to FY26 (my arithmetic). Two owners, same category, same direction, about a year apart. That is the strongest evidence for a non-Nike cause. It explains roughly half or more of Converse's $908M FY24 to FY26 drop.
- **The FY21 to FY24 peak was inflated.** Nike North America footwear revenue divided by US footwear PCE was about 105 to 110 before COVID (FY18 to FY19), rose to 124 to 133 in FY21 to FY24, and fell back to about 107 to 108 in FY25 to FY26 (my index). Measured from FY19, Nike NA footwear grew +32.6% to FY26 against US footwear PCE +31.9% (2019 to 2025). Part of the "decline" is a return to the pre-COVID share of wallet. But the inflation came mainly from Nike's own choices: DTC margin capture (NA DTC share rose from 32% to 49%), Dunk and Jordan oversupply, and the FY23 liquidation push. So that portion is a **symptom** of Nike strategy, not an independent macro cause.
- **Macro at the margin, mostly from 2026.** China retail softened in 2026 (NBS sports and entertainment goods -3.7% Jan to Aug 2026, REPO-NOTE). Europe turned promotional (adidas Q2 2026; Nike Q3 FY26 call). US sentiment fell to 52.2 (2026 average to August, University of Michigan). Hill in Jun 2026 cited "added pressure on traffic and discretionary spending". This matters for FY27, not for the FY25 collapse.

**Fixable by management: partly.** The macro piece is not fixable but will mean-revert. The category cycle is not fixable for the classics and canvas silhouettes themselves, but it is fixable through portfolio rotation (adidas and New Balance rode the next lifestyle cycle; ASICS SportStyle and Onitsuka Tiger each grew more than 40% in 2025). The rest is Nike-specific and is covered in the companion notes.

---

## 2. Predictions table

| # | Prediction if the hypothesis is true | Test and result | Held? |
|---|---|---|---|
| P1 | **Timing (pull-forward and bullwhip).** Nike's decline should start when the industry hangover hit (CY2022 to 2023) and end once inventories normalised (2024). | Industry hangover was CY2022 to 2023: adidas 2023 c-n revenue flat, North America -16% "particularly affected by... conservative sell-in strategy to reduce high inventory levels" (adidas FY2023 release, OPENED). Vans FY23 -12%, FY24 -24% (VF 10-Ks, OPENED). Circana US footwear revenue -3% Jan to Aug 2023 (SGB, OPENED). Nike FY23 revenue +10% (REPO), NA +18%, NA footwear +22% (FY23 10-K, OPENED). Nike inventories peaked at $9,662M on Aug 31, 2022 (REPO) and were "healthy" with "weeks of supply at their lowest levels since the pandemic" by Mar 2024 (Q3 FY24 call, OPENED). Nike's decline began in Q1 FY25 (-10%, REPO), after normalisation. | **No.** The bullwhip explains Nike's FY24 stall (+0.3%) and the FY23 gross-margin hit (46.0% to 43.5%, REPO), not the FY25 to FY26 decline. |
| P2 | **Market size.** If demand was pulled forward, aggregate consumer spending on footwear should fall below its pre-COVID trend in 2024 to 2025. | US PCE footwear (FRED DFTWRC1A027NBEA, OPENED): $91.9B (2019), $105.8B (2021), $110.4B (2022), $114.0B (2023), $116.1B (2024), $121.2B (2025). The 2014 to 2019 CAGR was 3.5%, giving a 2025 trend of $113.0B; actual is 7% above trend. Real (DFTWRX1A020NBEA): 2025 = 113.3 vs trend 111.7, +1.4% above. Circana: 2024 $89.2B flat; 2025 about $90B flat, units down low single digits (OPENED). Census shoe-store sales (MRTSSM4482USN, OPENED): $37.0B (2019), $39.9B (2023), $38.5B (2024), $38.7B (2025), Jan to Jul 2026 +2.9% YoY. | **No.** No below-trend payback. Store-level softness in 2024 (shoe stores -3.6%, sporting goods stores -4.0%) is small next to Nike NA footwear -13% in FY25. |
| P3 | **Peers.** A macro or cycle cause should hit most peers at the same time and by a similar amount. | During CY2024 to 2025 (Nike FY25 to FY26): adidas brand +13% c-n each year; New Balance +19% (2025); ASICS +19.5% (2025); On +30% (2025, CHF 3,014.0M vs CHF 2,318M, 20-F OPENED); Deckers +16.3% FY25 and +9.8% FY26 (XBRL, OPENED); Anta +13.3% (2025); Skechers +12.1% (2024, XBRL OPENED); lululemon +10.1% and +4.9% (XBRL). Decliners: Puma -8.1% c-n 2025, attributed to its own "reset", "inventory takebacks and reduced mass merchant exposure" (Puma release, OPENED); Under Armour FY25 -9.4%, FY26 -3.8% (own reset); VF FY25 -4.1% (Vans). | **No.** Dispersion is extreme, and the decliners have company-specific causes. |
| P4 | **Geography.** Nike's decline should track local macro: worst where consumer demand is weakest, and matched by peers there. | North America: US footwear PCE +1.8% (2024) and +4.4% (2025), adidas NA +10% (2025), NB NA 20%+, yet Nike NA FY25 -8.5%. Europe: adidas Europe +19% (2024) and +10% (brand, 2025), NB Europe 30%+, ASICS EMEA +18.4% (2025, SNIPPET), yet Nike EMEA FY25 -9.9%. China: the market grew in 2024 and 2025 (NBS sports goods +11.1% and +15.7%, REPO-NOTE china.md), yet Nike Greater China fell 12% and 13% c-n in FY25 and FY26. Only in 2026 do China (NBS -3.7% Jan to Aug) and Europe (promotional) turn macro-negative. | **No for FY25 to FY26; partly for FY27.** |
| P5 | **Income cohort.** A lower-income squeeze should hit value brands and value channels hardest, and Nike's losses should be concentrated in lower-income buyers. | Lower-income US card spending lagged (Sept 2025: 0.6% vs 2.6% for higher income, BofA Institute, SNIPPET; qualitative "growth remains muted", OPENED). Value retailers were soft: Academy FY24 -3.7%, FY25 -3.7%, FY26 +2.0%; Shoe Carnival FY25 -5.6% (XBRL, OPENED). But value brand Skechers grew 12.1% (2024), and Nike's teen footwear share fell most among upper-income female teens (56% to 45%, REPO-NOTE). | **Mostly no.** A real but small headwind; the wrong demographic signature for Nike's loss. |
| P6 | **Category saturation.** If sneakers were saturated, the sneaker category itself should shrink, across brands. | Circana sport lifestyle: +3% (2024, $31B) and +4% (2025) (OPENED). Running +6% (2024) and +9% (2025). Sport lifestyle declined only in H1 2026 (REPO-NOTE, SNIPPET). Within lifestyle, the losers were specific silhouettes: canvas (Converse -52% from FY23, Vans -49% from FY22) and Nike's Dunk/AF1/AJ1 classics (down "more than $4 billion" from peak, REPO-NOTE). Winners were terrace (adidas Originals double-digit growth in 2024, OPENED), NB retro and ASICS SportStyle/Onitsuka (each +40%+ in 2025, SNIPPET). | **Partly.** No saturation of the category before 2026. There was a real rotation away from canvas and classics, which hit any brand overweight in them. |
| P7 | **Narrative.** If macro were primary, management under a new CEO would keep citing it and not take ownership. | "Macro" mentions by call: 13 (Dec 2023), 5 (Mar 2024), 5 (Jun 2024), 2 (Oct 2024), 1 (Dec 2024), 0 (Jun 2025), 0 (Dec 2025), 4 (Jun 2026). Hill and Friend attribute FY25 to FY26 to classics, digital, inventory and "sport" focus. Friend (Sept 30, 2025): "our performance in the first quarter didn't have anything to do with pull forwards." Macro returns in the Jun 2026 call (discretionary pressure). | **No for FY25 to FY26; yes for FY27.** |
| P8 | **Peak inflation.** If the cycle hypothesis is right, Nike's FY24 peak should look abnormally high against a market baseline, and the decline should return it to the pre-COVID relationship. | Nike NA footwear revenue per $ of US footwear PCE (my index): FY18 105.1, FY19 110.5, FY21 124.4, FY22 113.2 (supply-constrained), FY23 132.8, FY24 126.4, FY25 106.9, FY26 about 108 (2026 PCE assumed +3 to 4%). FY19 to FY26: Nike NA footwear +32.6% vs PCE footwear +31.9% (2019 to 2025). | **Yes, but as a symptom.** The inflation drivers were Nike-made: DTC mix rose from 31.6% to 48.6% of NA revenue (FY19 to FY24, REPO), which captures retail margin per pair, plus classics oversupply and FY23 liquidation volume. |

---

## 3. Evidence detail

### 3.1 The 2022 bullwhip: real, but it hit before Nike's decline and mainly hit margin

- **Nike Q1 FY23 call, Sept 29, 2022 (OPENED):** "Earlier ordering by retailers, driven by strong consumer demand and less predictable delivery timelines, had led to elevated inventory levels broadly across consumer goods. Then transit times began to rapidly improve." "Our North America inventory grew 65% versus the prior year, with in-transit inventory growing approximately 85%." Guidance: "approximately 150 basis points of annual impact from higher markdowns and higher off-price mix to liquidate elevated inventory." Donahoe framed it as "transitional", with "industry-wide excess inventory."
- **Nike inventory (REPO):** $8,420M (May 31, 2022), $9,662M (Aug 31, 2022), $8,905M (Feb 28, 2023), $7,519M (May 31, 2024).
- **Nike revenue during the bullwhip (REPO):** FY23 $51,217M, +9.6%. NA footwear +22% to $14,897M (FY23 10-K, OPENED). Gross margin fell 250 bps to 43.5%.
- **Q3 FY24 call, Mar 21, 2024 (OPENED):** "Our inventory position remains healthy, with total marketplace units down double-digits versus prior year, and weeks of supply at their lowest levels since the pandemic." The quarter was compared against "14% reported and 19% currency-neutral growth one year ago, as we were liquidating excess inventory in Q3 of Fiscal '23."
- **Peers in the bullwhip year:** adidas FY2023 release (OPENED): "Apparel revenues were down 6% on a currency-neutral basis, as this product category was particularly impacted by the high inventory levels in the marketplace"; "currency-neutral revenues in North America declined 16%." Foot Locker revenue $8,759M (FY22) to $8,168M (FY23), -6.7% (XBRL, OPENED).
- **Inference:** Nike pushed liquidation volume through its own and off-price channels in FY23, which *raised* FY23 revenue while peers shrank. The bullwhip then explains the FY24 flat year (Nike cut wholesale sell-in for H1 FY24, Q2 FY24 call, OPENED: "we moved proactively in the prior year to liquidate excess inventory and reduce wholesale sell-in for the first half of fiscal '24"). It does not explain why FY25 fell 10% while peers grew double digits.

### 3.2 COVID pull-forward: no aggregate payback in footwear

US PCE on footwear, $ billions (FRED, BEA NIPA, OPENED):

| Year | Nominal | YoY | Real (chained 2017 $) | YoY |
|---|---|---|---|---|
| 2019 | 91.9 | | 91.8 | |
| 2020 | 81.4 | -11.4% | 83.4 | -9.1% |
| 2021 | 105.8 | +29.9% | 104.6 | +25.3% |
| 2022 | 110.4 | +4.4% | 104.3 | -0.2% |
| 2023 | 114.0 | +3.3% | 107.5 | +3.1% |
| 2024 | 116.1 | +1.8% | 108.7 | +1.1% |
| 2025 | 121.2 | +4.4% | 113.3 | +4.3% |

YoY columns are my arithmetic.

- In real terms, 2022 was flat after the 2021 spike, which is the only visible pull-forward digestion. It coincided with Nike FY23 growth of +10%.
- Census shoe-store sales (excluding online) were $37.0B (2019), $39.0B (2021), $39.6B (2022), $39.9B (2023), $38.5B (2024), $38.7B (2025). Sporting-goods store sales show the clearest COVID boom and fade: $43.5B (2019), $62.2B (2021), $61.2B (2023), $58.7B (2024), $58.0B (2025), then Jan to Jul 2026 +8.1%. That category includes bikes, fitness equipment, firearms and outdoor gear, which boomed in COVID. Even after the fade it is 33% above 2019.
- **Circana:** 2025 "held steady... at $90 billion", "units sold declined in the low single digits", performance +6%, running +9%, sport lifestyle +4%, fashion -2% (Mr-Mag, Feb 5, 2026, OPENED). 2024: $89.2B, flat; sport lifestyle $31B, +3%; running +6% to $7.4B (SGB, Jan 31, 2025, OPENED).
- **Discrepancy noted:** BEA PCE shows 2023 footwear +3.3%, while Circana shows US footwear revenue -3% for Jan to Aug 2023. Panel data and national accounts differ in coverage and price treatment. Both agree 2024 to 2025 was flat to up, not down.

### 3.3 Consumer and macro indicators against Nike's revenue path

University of Michigan consumer sentiment, annual average (FRED UMCSENT, OPENED; my arithmetic): 2019 96.0, 2021 77.6, **2022 59.0** (trough of 50.0 in Jun 2022), 2023 65.4, **2024 72.5**, 2025 57.6, 2026 (Jan to Aug) 52.2.

- Nike grew +10% in FY23, when sentiment was at its lowest in decades. Nike fell 10% in FY25, when sentiment was at its best since 2021. In FY25 the correlation runs the wrong way for a macro story.
- From mid-2025, sentiment fell sharply, and the June 2026 call (OPENED) says: "We're operating in a more complex macro environment, where we're seeing added pressure on traffic and discretionary spending across our geographies", and "we are not expecting the environment to improve meaningfully over the next 6 months." This supports a macro share in the FY27 guide (high-single-digit decline).

### 3.4 Peer natural experiment (revenue, as reported unless stated)

| Company (FY end) | 2019 or FY19/20 | Latest | Growth in Nike's decline window | Source |
|---|---|---|---|---|
| Nike (May) | FY19 $39,117M | FY26 $46,398M | FY25 -9.8%, FY26 +0.2% | REPO |
| adidas (Dec) | 2019 €23.64B (REPO-NOTE) | 2025 €24.8B | 2024 +12% c-n; 2025 brand +13% c-n; H1 2026 +14% c-n | adidas releases, OPENED |
| New Balance (Dec, private) | n/a | 2025 $9.2B | 2025 +19%; NA 20%+, Europe 30%+ | NB release, Feb 19, 2026, OPENED |
| ASICS (Dec) | n/a | 2025 ¥810.9B | 2025 +19.5% (+19.4% c-n) | SGI Europe, alchempro, SNIPPET |
| On (Dec) | 2019 about CHF 267M (REPO-NOTE) | 2025 CHF 3,014.0M | 2025 +30% | On 20-F FY2025, OPENED |
| Deckers (Mar) | FY20 $2,133M | FY26 $5,472M | FY25 +16.3%, FY26 +9.8% | XBRL, OPENED |
| Skechers (Dec) | 2019 $5,220M | 2024 $8,969M | 2024 +12.1% (taken private 2025) | XBRL, OPENED |
| lululemon (Jan/Feb) | FY19 $3,979M | FY25 $11,103M | +10.1%, +4.9% | XBRL, OPENED |
| Anta (Dec) | n/a | 2025 RMB 80.22B | 2025 +13.3% | ir.anta.com and FashionUnited, SNIPPET |
| Puma (Dec) | n/a | 2025 €7,296M | 2025 -8.1% c-n (self-declared "reset") | Puma release, Feb 26, 2026, OPENED |
| Under Armour (Mar) | 2019 $5,267M | FY26 $4,966M | FY25 -9.4%, FY26 -3.8% | XBRL, OPENED |
| VF (Mar) | FY20 $10,489M | FY26 $9,605M | FY25 -4.1%, FY26 +1.1% | XBRL, OPENED |
| Vans brand (VF) | | | FY23 -12%, FY24 -24%, FY25 -16%, FY26 -9% | VF 10-Ks, OPENED |
| Converse (Nike) | FY19 $1,906M | FY26 $1,174M | FY24 -14%, FY25 -19%, FY26 -31% | REPO |
| Crocs (Dec) | 2019 $1,231M | 2025 $4,041M | 2024 +3.5%, 2025 -1.5% | XBRL, OPENED |
| Columbia (Dec) | 2019 $3,043M | 2025 $3,397M | 2024 -3.4%, 2025 +0.9% | XBRL, OPENED |
| Dick's (Jan/Feb) | FY19 $8,751M | FY24 $13,443M (pre-Foot Locker) | FY24 +3.5% | XBRL, OPENED |
| Foot Locker (Jan/Feb) | FY19 $8,005M | FY24 $7,988M | FY23 -6.7%, FY24 -2.2% | XBRL, OPENED |
| Academy (Jan/Feb) | FY19 $4,830M | FY25 $6,053M | FY24 -3.7%, FY25 +2.0% | XBRL, OPENED |
| Shoe Carnival (Jan/Feb) | FY19 $1,037M | FY25 $1,135M | FY24 +2.3%, FY25 -5.6% | XBRL, OPENED |

Growth rates are my arithmetic from the XBRL values unless the source states them.

Pattern: the brands that grew are performance-running and new-lifestyle-cycle brands (adidas terrace, NB retro, ASICS/Onitsuka, On, Hoka). The ones that shrank are concentrated in fading lifestyle silhouettes (Vans, Converse, Nike classics), are mid-reset (Puma, Under Armour), or are retailers tied to those silhouettes (Foot Locker). A macro shock does not sort winners and losers by silhouette.

### 3.5 Canvas and classics cycle: the one place a shared cycle shows up

- Vans index (FY22 = 100, my arithmetic from VF's stated growth rates): FY23 88, FY24 67, FY25 56, FY26 51.
- Converse index (FY23 = 100, REPO): FY24 86, FY25 70, FY26 48.
- Both fell by about half from peak, under two different owners, with Vans leading by about one year. This is evidence of a category fashion cycle away from canvas and vulcanised skate shoes, consistent with Circana's "fashion" category declining (-3% 2024, -2% 2025).
- Nike's FY26 Converse drop (-31%) is much steeper than Vans's FY26 drop (-9%). Nike says "The actions related to Converse are expected to continue throughout fiscal 2027" (Q1 FY27 10-Q p. 20, REPO), which points to deliberate clean-up on top of the cycle.
- Classics: on Q1 FY25 Digital, "the 3 classic franchises being down nearly 50%" (Q1 FY25 call, OPENED). In Q2 FY26 there was "a top line headwind of approximately $550 million from the reduction of our Classics franchises, down over 20%... our currency-neutral revenue grew 6% excluding" it (Q2 FY26 call, OPENED). The classics fade is partly a fashion cycle (the same rotation that hit Vans) and partly Nike's own oversupply (see `franchise_oversupply.md`, which attributes half to two-thirds to oversupply).

### 3.6 Nike's own framing over time (call transcripts, OPENED)

- Dec 21, 2023 (Donahoe, guidance cut): "we are seeing indications of more cautious consumer behavior around the world in an uneven macro environment." The new outlook "reflects increased macro headwinds, particularly in Greater China and EMEA." The same call also cites "life cycle management of key product franchises." Stock: $122.53 to $108.04 the next day, -11.8% (REPO prices, my arithmetic).
- Mar 21, 2024 (Friend): "we continue to have industry tailwinds, consumer interest in sport, more people participating in running events and marathons... there are natural consumer tailwinds that are going to continue to drive growth in our sector."
- Jun 27, 2024 (guidance cut): "increased macro uncertainty" is mentioned, but the driver is "a product cycle transition." Stock: $94.19 to $75.37, -20.0%.
- Oct 1, 2024 (Friend): "retail sales moderated across the industry, and NIKE was not immune."
- Dec 19, 2024 (Hill): "We lost our obsession with sport."
- Sept 30, 2025 (Friend): "our performance in the first quarter didn't have anything to do with pull forwards." Hill: "turning our business around in the face of a cautious consumer, tariff uncertainty and teams that are still settling."
- Mar 31, 2026 (Hill): "I'm incredibly positive on the athletic industry overall... an expanding market." (Friend, same call: EMEA "has seen challenges in traffic and also a higher level of promotional activity.")
- Jun 30, 2026: "added pressure on traffic and discretionary spending across our geographies."

Interpretation: management used macro language most at the moment it was least true (Dec 2023, a strong consumer year), and dropped it once a new CEO took ownership. Macro language came back in 2026, when the data (sentiment, China NBS, Europe promotions) also turned.

### 3.7 Where the current (FY27) decline comes from

Q1 FY27 versus Q1 FY26 (REPO, my arithmetic): total -$507M. North America +$107M (+2.1%), EMEA -$155M, Greater China -$332M, APLA -$27M, Converse -$103M. The ongoing decline is China plus Converse plus EMEA. North America, the region with the clearest US macro data, is growing. China's 2026 market softness (NBS -3.7% Jan to Aug 2026, REPO-NOTE) is real, but Nike China's -26% c-n is far larger, and adidas Greater China grew +15% c-n in Q2 2026 (OPENED).

---

## 4. Independent cause or symptom?

- **The bullwhip** was an industry event, but Nike's way of handling it (liquidating aggressively into FY23 to post growth, then cutting sell-in) moved revenue between years. It is a timing effect, not a driver of the FY24 to FY26 level drop.
- **The COVID peak inflation** in Nike's North America numbers is mainly a *symptom* of Nike's DTC pivot and classics supply decisions. The COVID boom created the demand, but Nike's own choices turned it into an unsustainably high revenue base.
- **The canvas and classics fashion rotation** is a genuinely external cycle. Its impact on Nike was amplified by Nike-specific over-concentration (classics) and Converse management.
- **Macro proper** (lower-income squeeze, 2026 sentiment drop, China and Europe softness, tariffs on consumer confidence) is independent, but small before 2026.

---

## 5. Quantification (my estimate, method shown)

Decline to explain: FY24 $51,362M to FY26 $46,398M = **-$4,964M** (REPO).

1. **Macro demand (US, Europe):** US footwear spending rose in 2024 and 2025, and European peers grew double digits through 2025. The FY24 to FY26 contribution is about $0 to $0.2B. EMEA promotional softness in late FY26 is the only measurable piece.
2. **China macro (not guochao):** NBS sports goods grew in 2024 and 2025 and turned negative only in 2026. `china.md` puts all external China forces at $0.3B to $0.6B, including guochao and local competition. The pure macro part is perhaps a third of that: **about $0.1B to $0.2B**.
3. **Lower-income squeeze:** value retailers were soft (Academy, Shoe Carnival), but Nike's loss skews to upper-income buyers. **About $0 to $0.2B** (assumption).
4. **Canvas and classic lifestyle fashion cycle, the portion not caused by Nike:** Converse fell $908M FY24 to FY26. If Converse had matched Vans's trajectory (about -24% from FY24 levels over the comparable two years, my arithmetic: FY25 -16%, FY26 -9%), it would have lost about $0.5B; the cycle explains about **$0.5B**. Nike classics: of the more than $4B fall, the companion note assigns one-third to one-half to a normal fade. I use a narrower **$0.2B to $0.4B** of *net* revenue effect, because newness had back-filled most of the gap by FY26 (+6% ex-classics in Q2 FY26).
5. **Bullwhip and pull-forward:** about **$0** for the FY24 to FY26 level change. FY24 had already normalised (NA footwear index 126 vs 124 in FY21).

**Total: about $0.8B to $1.3B, or 15% to 25% of the FY24 to FY26 decline.** Central estimate about 20%. Nike-specific causes account for the remaining 75 to 85%.

**FY27 leg:** The guide is a high-single-digit decline. Macro is now visible: US sentiment at 52, China retail negative, Europe promotional, Hill's "discretionary" comment. Nike-specific China and Converse resets are still dominant. My estimate is that macro and cycle are 25 to 40% of the FY27 decline. Confidence is low.

**Counterfactual check:** had Nike simply held its share of a market growing about 5 to 6% over two years (US PCE footwear +6.3%, 2023 to 2025), FY26 revenue would be about $54B. The gap between that and the actual $46.4B (about $8B) is larger than the whole measured decline, which is itself evidence that the problem is share, not market size.

**Error bands:** wide. BEA PCE and Circana disagree for 2023. The NA footwear index mixes wholesale and DTC prices, and Canada is in Nike's NA segment but not in US PCE. Peer fiscal years are misaligned by up to five months. The Converse-versus-Vans counterfactual assumes the two brands share one cycle.

---

## 6. Strongest evidence

**For the hypothesis:**
1. Converse and Vans both lost about half their revenue from peak under different owners: a shared external category cycle.
2. Nike NA footwear's share of US footwear spending returned almost exactly to its FY19 level (+32.6% vs +31.9%), so the FY23 to FY24 peak was cycle-inflated.
3. The 2022 bullwhip was industry-wide (Nike's own words: "industry-wide excess inventory"; adidas 2023 NA -16%).
4. From mid-2025, US sentiment fell to multi-decade lows (52.2 in 2026), China retail turned negative and Europe became promotional, and Nike cited "discretionary" pressure in Jun 2026.
5. Lower-income card spending lagged higher-income spending (BofA Institute 2025), and value retailers (Academy, Shoe Carnival, Foot Locker) were soft.

**Against the hypothesis:**
1. Timing: Nike grew +10% in the bullwhip year (FY23) and started falling in Q1 FY25, when the industry was growing again.
2. US footwear PCE rose +1.8% (2024) and +4.4% (2025) and stays above its pre-COVID trend, so there was no payback. Circana shows a flat market and growing sport lifestyle in 2024 to 2025.
3. Peers in the same markets grew strongly during Nike's decline: adidas +13% c-n twice, NB +19%, ASICS +19.5%, On +30%, Deckers +16%, Anta +13%.
4. Nike's loss was among upper-income teens, not lower-income ones; value brand Skechers grew 12%.
5. Nike's own new management attributes the decline to its own decisions ("We lost our obsession with sport"; "didn't have anything to do with pull forwards"; +6% c-n excluding classics in Q2 FY26).
6. North America, where the macro data is clearest, is growing again (+2.1% in Q1 FY27). The current decline is China and Converse, both with documented Nike-specific resets.

---

## 7. Sources

| # | Source | Date | Status | Used for |
|---|---|---|---|---|
| 1 | Nike 10-K FY2019 to FY2026, quarterly 10-Qs and 8-K releases (via `04_financial_data_pack.md`, `nike_filing_facts.csv`, `nike_channel_split.csv`) | 2019 to 2026 | REPO | Revenue, segments, channels, inventories, Converse, Q1 FY27 |
| 2 | Nike FY2020, FY2021, FY2022, FY2023, FY2024, FY2025 and FY2026 10-K text, North America segment tables (EDGAR, scratchpad text) | filed 2020-07-24 to 2026-07-15 | OPENED | NA footwear $9,322M (FY18), $10,045M (FY19), $9,329M, $11,644M, $12,228M, $14,897M, $14,537M, $12,684M, $13,317M (FY26) |
| 3 | Nike earnings-call transcripts, Q1 FY21 to Q1 FY27, investors.nike.com webcast_transcript PDFs, asset IDs 9384 to 9406, 9540, 9591 | 2020-09-22 to 2026-10-01 | OPENED (full text) | All management quotes; "macro" counts |
| 4 | FRED DFTWRC1A027NBEA and DFTWRX1A020NBEA (BEA PCE footwear, nominal and real), https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFTWRC1A027NBEA | downloaded 2026-10-13, data through 2025 | OPENED | Footwear spending and trend test |
| 5 | FRED MRTSSM4482USN (shoe stores) and MRTSSM45111USN (sporting goods stores), Census MRTS | downloaded 2026-10-13, data through Jul 2026 | OPENED | Store sales |
| 6 | FRED UMCSENT (University of Michigan sentiment) | downloaded 2026-10-13, data through Aug 2026 | OPENED | Sentiment averages |
| 7 | SEC XBRL company facts (data.sec.gov/api/xbrl/companyfacts) for Skechers, Deckers, Under Armour, VF, Crocs, lululemon, Columbia, Foot Locker, Dick's, Academy, Genesco, Shoe Carnival (Shoe Station Group), Wolverine, Steve Madden | downloaded 2026-10-13 | OPENED | Peer annual revenue |
| 8 | VF 10-Ks FY2020 to FY2026 (EDGAR, e.g. https://www.sec.gov/Archives/edgar/data/103379/000010337925000023/vfc-20250329.htm) | filed 2020-05-27 to 2026-05-20 | OPENED | Vans growth rates |
| 9 | On Holding 20-F FY2025 (SEC, scratchpad text) | 2026 | OPENED | On net sales CHF 3,014.0M, +30% |
| 10 | adidas FY2022, FY2023, FY2024, FY2025 and Q2 2026 results releases (adidas IR PDFs, scratchpad text) | 2023-03-08 to 2026-07-30 | OPENED | adidas growth, NA -16% in 2023, inventory language, regional growth |
| 11 | Puma, "PUMA completes reset 2025; 2026 designated transition year", https://about.puma.com/en/newsroom/corporate-news/2026/26-02-2026-puma-completes-reset-2025-2026-designated-transition-year | 2026-02-26 | OPENED | Puma -8.1% c-n and its causes |
| 12 | New Balance, "2025 Business Update", https://newbalance.newsmarket.com/latest-news/2025-business-update---joe-preston--president---ceo--new-balance-athletics--inc./s/ecb51e70-4baa-4592-85a8-03452a7ae163 | 2026-02-19 | OPENED | NB $9.2B, +19%, NA 20%+, Europe 30%+ |
| 13 | SGB Media, "Report: Flat U.S. Footwear Retail Sales Led by Sport Lifestyle Growth in 2024" (Circana), https://sgbonline.com/?p=333194 | 2025-01-31 | OPENED | 2024 Circana figures |
| 14 | Mr-Mag, "Circana issues Q4 2025 footwear industry pulse report", https://mr-mag.com/circana-issues-q4-2025-footwear-industry-pulse-report/ | 2026-02-05 | OPENED | 2025 Circana figures |
| 15 | SGB Media, "Report: Footwear Sales Decline 3 Percent Through August" (Circana), https://sgbonline.com/?p=292501 | 2023-09-27 | OPENED | 2023 market softness |
| 16 | Bank of America Institute, "Consumer Checkpoint: The tale of two wallets", https://institute.bankofamerica.com/economic-insights/consumer-checkpoint-october-2025.html | Oct 2025 | OPENED (qualitative only); income-group percentages SNIPPET | Lower-income spending lag |
| 17 | ASICS FY2025 results (SGI Europe, alchempro, insideretail.asia) | Feb 2026 | SNIPPET | ASICS +19.5%, SportStyle and Onitsuka +40% |
| 18 | Anta 2025 results (ir.anta.com, FashionUnited) | 2026-03-25 | SNIPPET | Anta +13.3% |
| 19 | Eurostat sts_trtu_a, EU27 retail volume and turnover (G47_X_G473, G476) | updated 2026-10-10 | OPENED | Tested; EU-level clothing and footwear series not published at annual level, so not used |
| 20 | `research_notes/Nike decline root cause analysis/china.md`, `franchise_oversupply.md`, `dtc_wholesale.md`; `Nike decline execution vs structural/analysts_and_consumer_data.md` | 2026-10-13 | REPO-NOTE | NBS China data, Piper Sandler teen survey, classics quantification, Circana H1 2026 |
| 21 | `data/nke_daily_prices.csv` (Yahoo Finance) | through 2026-10-12 | REPO | Stock moves on Dec 22, 2023 and Jun 28, 2024 |

## 8. Gaps

- No Circana full-year 2023 US footwear total was found (only Jan to Aug, -3%).
- No Euromonitor or Circana *brand* share time series was available to test share directly. The NA footwear vs PCE index is a proxy.
- No income-cohort data on Nike's own customers. The Piper teen survey is the only demographic cut.
- ASICS, Anta and New Balance 2024 figures were not opened.

---

## Challenge: REFUTER

Challenger date: 2026-10-13. Lens: try to disprove the hypothesis and check the investigator's numbers. Status labels as above. One limit: the shared WebSearch budget for this workflow was used up while I worked, so I used SEC XBRL APIs, cached FRED downloads (pulled today by an earlier step and read by me from disk), HKEX announcements already in the scratchpad (I read the text myself) and Nike and adidas documents already in the scratchpad. I could not check On, ASICS or Puma 2026 interims; those remain gaps.

### R1. Number checks (all reproduce)

| Claim | Check | Result |
|---|---|---|
| FY24 to FY26 decline -$4,964M | 51,362 minus 46,398 (REPO) | Correct |
| US footwear PCE +1.8% (2024), +4.4% (2025) | FRED DFTWRC1A027NBEA cached CSV: 114.021, 116.061, 121.150 | Correct (+1.79%, +4.38%). OPENED |
| NA footwear +32.6% vs PCE +31.9% (FY19/2019 to FY26/2025) | 10,045 to 13,317; 91.872 to 121.150 | Correct. Caveat: Nike FY26 runs to May 2026, PCE is CY2025 |
| Converse -52% FY23 to FY26 | 2,427 to 1,174 (REPO) | Correct (-51.6%) |
| "Hold share" counterfactual about $54B | 51,362 x (121.150 / 114.021) = $54.6B | Arithmetic correct, but it scales global revenue (including apparel, China, EMEA) by a US footwear index. Directionally fine, not precise |
| Converse-as-Vans cycle about $0.5B | 0.84 x 0.91 = 0.764; 2,082 x 23.6% = $491M | Arithmetic correct; the premise is weak (R3) |

No number I checked was wrong. The problems are in attribution, not arithmetic.

### R2. Natural experiments the notes did not use

**(a) Channel split: the decline sits almost entirely in the channel Nike controls.** FY24 to FY26 (REPO, `nike_filing_facts.csv`, my arithmetic): DTC including Converse $22,351M to $18,197M, **-$4,154M (84% of the whole decline)**. Wholesale including Converse $28,856M to $28,058M, -$798M (16%). Nike Brand Digital $12.1B to $8.6B, about -$3.5B (about 70% of the decline). A demand shock reaches retailers' sell-through and then wholesale orders. Instead, wholesale was nearly flat and grew +4.9% in FY26 (26,758 to 28,058), while Nike's own digital store, where Nike sets prices, markdown days and assortment, fell by a third. That is the signature of a Nike decision (cutting promotional digital volume and moving back to wholesale), not of consumers spending less.

**(b) Sentiment versus Nike North America by fiscal year runs the wrong way, including FY27.** UMich sentiment averaged over Nike fiscal years (FRED UMCSENT cached CSV, OPENED, my arithmetic): FY23 59.3, FY24 70.8, FY25 65.6, **FY26 54.5**, **Q1 FY27 52.1**. Nike North America revenue (REPO): FY23 +18%, FY24 -1.0%, FY25 -8.5%, **FY26 +4.8%** (19,572 to 20,511), **Q1 FY27 +2.1%** (5,020 to 5,127). Nike NA grew in the two worst sentiment periods on record in this data and fell in the best one. Whatever the US consumer is doing, it is not what moved Nike NA.

**(c) Value-channel retailer grew through the 2026 "squeeze".** Academy Sports + Outdoors, a value-oriented sporting goods chain (SEC XBRL company facts, OPENED, filed 10-Qs 2026-06-10 and 2026-09-09): quarter to May 2, 2026 $1,442.0M vs $1,351.4M (+6.7%); quarter to Aug 1, 2026 $1,647.3M vs $1,599.8M (+3.0%). Deckers (HOKA, UGG), quarter to Jun 30, 2026: $1,019.5M vs $964.5M (+5.7%) (XBRL, 10-Q filed 2026-07-30, OPENED). adidas North America +17% c-n in Q2 2026 (adidas Q2 2026 release, 2026-07-30, OPENED). The one US peer I found falling was lululemon, quarter to Aug 2, 2026 $2,415.6M vs $2,525.2M (-4.3%) (XBRL, OPENED), which has its own widely reported US reset. A lower-income squeeze should show first at Academy; it did not.

**(d) Inside Nike, the decline sorts by Nike's own categories, not by consumer income or region.** Q1 FY27 call (2026-10-01, transcript in scratchpad, OPENED): "Running is up double digits again with consistent share gains. Global Football ... strong double-digit growth in all 4 geos ... Basketball was up double digits in North America ... both tennis and golf grew double digits." Against that: "As planned, we reduced revenue from the Dunk by nearly 50% in the quarter. That resulted in roughly $200 million headwind in Sportswear." A discretionary squeeze would hit $160 running shoes too. It did not. Performance up, Nike's oversupplied lifestyle franchises down, is a portfolio story.

**(e) China peers in the same 2026 market (HKEX interims, H1 2026, read from scratchpad text, OPENED):** Anta Group revenue +12.9% to RMB43,507M (main ANTA brand +4.8%, FILA +6.1%) (2026-08-26); Li Ning +2.8% to RMB15,235M (2026-08-20); 361 Degrees +8.0% to RMB6,159.8M (2026-08-18); Xtep RMB6,794.9M vs RMB6,837.6M (-0.6%, my arithmetic) (2026-08-25); adidas Greater China +15% c-n in Q2 2026 (OPENED). Nike Greater China Q1 FY27: -26% c-n. Anta's interim also cites NBS H1 2026 retail sales of "apparel, footwear, hats and textiles ... up 6.7% year-on-year" (OPENED). The investigator leans on NBS "sports and entertainment goods" (-3.7% Jan to Aug 2026), a broad category, while the apparel and footwear line grew (+5.1% Jan to Aug, per `china.md`). Only Topsports, whose revenue is 86.7% Nike and adidas, fell (low-teens decline in Mar to May 2026, HKEX 2026062500529, OPENED), which is what you expect if its largest supplier is shrinking supply.

### R3. The "canvas cycle" control is contaminated

The largest macro/cycle component ($0.7B to $0.9B) rests on Vans as an external control for Converse. VF's own FY2025 10-K (EDGAR, filed 2025-05, scratchpad `refuter/vf25.htm`, OPENED) says: "The decline in Vans ® was also attributed to deliberate strategic actions taken in Fiscal 2025, including reducing wholesale store fronts and inventory in the Asia-Pacific region (specifically in China), exiting value-channel wholesale customers and closing unprofitable owned retail stores in the Americas region, and reducing distressed sales." VF also installed a new Vans president (July 2024) and ran a turnaround. So Vans's FY25 to FY26 trajectory is partly a company-specific reset, not a clean read of the category. Using it as the "pure cycle" counterfactual overstates the external share. Timing also argues against one shared cycle: Vans fell 12% in VF FY23 (CY2022) while Converse grew +3.4% in Nike FY23 (2,346 to 2,427, REPO). The same consumers did not leave both brands at the same time.

Two further definitional points:
- A rotation from Nike Dunk and AF1 to adidas Samba and terrace, NB retro and Onitsuka Tiger is market share moving to competitors. Counting it as "cycle" rather than as a Nike product and supply failure is generous to the hypothesis. Nike's own Q1 FY27 language ("some aged, higher volume, sportswear footwear sold through below expectations") points at Nike's assortment.
- The 2026 lifestyle softness is real but category-specific. adidas Q2 2026 (OPENED): "The lifestyle footwear market, especially for him, is currently under pressure due to heavy discounting at many retailers, especially in Europe". Yet adidas Lifestyle still grew 2% and Europe 6%, while Nike EMEA fell 5% c-n in Q1 FY27.

### R4. The FY27 leg (25 to 40%) is too high

- The CFO frames the FY27 high-single-digit decline as chosen: "we are making deliberate choices across portions of the portfolio, particularly in NIKE Sportswear, the Jordan Brand and Greater China ... We will continue to take actions to reduce supply" (Q1 FY27 call, OPENED). Q2 also laps "significant promotional activities in EMEA from Cyber Week and a higher comparison of North America sell-in activities", "approximately 400 basis points" of headwind: Nike's own prior-year actions, not macro.
- Q1 FY27 c-n decline was about 5% (about $0.5B to $0.6B). Explicitly deliberate items alone: Dunk about $200M, Converse -$103M reported with "actions ... expected to continue throughout fiscal 2027" (10-Q p. 20, REPO), and China "eliminate some online distribution that was unprofitable and brand dilutive" (call, OPENED). North America, the region where the macro data is clearest, grew.
- My bottom-up for Q1 FY27: China market drag about 4% of Nike's $1.5B base (about $60M); about half of the EMEA decline to a promotional lifestyle market (about $80M); a residual Converse category fade at Vans's FY26 rate (about $30M). Total about $170M, or 15 to 30% depending on how much of EMEA and Converse one grants. I would put FY27 macro and cycle at **15 to 30%**, below the investigator's 25 to 40%.

### R5. Revised share

| Component | Investigator | Refuter | Reason |
|---|---|---|---|
| Canvas and classics cycle | $0.7B to $0.9B | $0.3B to $0.7B | Vans control includes VF's deliberate reset; classics rotation went to competitors |
| China macro | $0.1B to $0.2B | $0.1B to $0.2B | Agree (market grew 2024 to 2025) |
| EMEA promotions and US lower-income | $0B to $0.4B | $0B to $0.2B | Wholesale flat, Academy grew, NA rose as sentiment fell |
| Bullwhip and pull-forward | about $0 | about $0 | Agree |
| **Total FY24 to FY26** | **$0.8B to $1.3B (15 to 25%)** | **$0.4B to $1.1B (about 8 to 22%, central about 13%)** | |

Strictly defined macro (aggregate demand only, excluding a fashion rotation that went to rivals) is about $0.1B to $0.4B, 2 to 8%.

### Verdict

The hypothesis does not survive. Every testable prediction fails on at least one clean natural experiment: channel (84% of the fall in Nike's own DTC, wholesale flat), timing (Nike NA grew in the worst sentiment years), income (value retailer Academy grew in 2026), category (Nike Performance up double digits while Nike lifestyle fell), and geography (China peers and adidas grew in the same market). The investigator's "minor" verdict stands, and if anything the macro share is overstated, mainly because Vans is not a clean external control and because rotation to competitors is counted as cycle.

### Refuter sources

| Source | Date | Status |
|---|---|---|
| Nike `data/nike_filing_facts.csv` (revenues, DTC, wholesale, digital, regions, Converse) | filings 2023-07-20 to 2026-10-02 | REPO |
| Nike Q1 FY27 earnings call transcript (investors.nike.com PDF, scratchpad `tx/Q1FY27.txt`) | 2026-10-01 | OPENED |
| VF Corp FY2025 Form 10-K, Vans discussion (scratchpad `refuter/vf25.htm`) | filed May 2025 | OPENED |
| SEC XBRL company facts: Academy (CIK 1817358), Deckers (910521), lululemon (1397187), Dick's (1089063, not used: Foot Locker acquisition breaks comparability) | downloaded 2026-10-13 | OPENED |
| FRED UMCSENT and DFTWRC1A027NBEA (cached CSVs downloaded 2026-10-13; a fresh download today was refused by the FRED server) | data through Aug 2026 and 2025 | OPENED |
| adidas Q2 2026 results release | 2026-07-30 | OPENED |
| HKEX: Anta interim 2026-08-26; Li Ning 2026-08-20; 361 Degrees 2026-08-18; Xtep 2026-08-25; Topsports Q1 FY26/27 update 2026-06-25 | 2026 | OPENED |
| Not checked (search budget exhausted): On Q2 2026, ASICS H1 2026, Puma Q2 2026, US monthly footwear PCE for 2026 | | GAP |

---

## Challenge: ROOT-CAUSE

Challenger date: 2026-10-13. Lens: accept that the symptoms are real (a 2022 bullwhip, a fading canvas and classics cycle, a softer consumer from mid-2025) and ask which way the causal arrow runs. Two questions: (1) are macro shocks the hidden upstream cause of the "Nike-specific" factors (for example, did the COVID bullwhip create the classics oversupply that later collapsed)? (2) are some items booked as "macro" actually downstream of Nike decisions? Limit: the shared WebSearch budget for this workflow was exhausted before I started, so I used Nike filing data in the repo, adidas results PDFs already in the scratchpad (text read by me), and fresh FRED downloads made today. Status labels as above.

### RC1. The bullwhip was a common shock; it does not explain why Nike, and not adidas, declined

If the bullwhip were the upstream cause of Nike's decline (via forced liquidation, brand damage and a delayed reset), then a peer hit by the same shock at least as hard should show the same full-cycle outcome, perhaps with different timing.

- **Size of the shock.** adidas inventories at Dec 31, 2022: EUR 5,973M, +49% (2021: EUR 4,009M), "mainly driven by higher product and freight costs, a different order pattern as a result of longer transportation lead times, the termination of the Yeezy partnership, as well as lower prior year comparables due to last year's impact from the factory lockdowns in Vietnam" (adidas FY2022 results release, 2023-03-08, OPENED, scratchpad `ads/fy2022.txt`). That is 26.5% of 2022 revenue (EUR 22,511M; my arithmetic). Nike: $8,420M at May 31, 2022 (18.0% of FY22 revenue $46,710M) and $9,662M at Aug 31, 2022 (20.7%), +44% year on year (REPO; my arithmetic). Same causes (transit times, Vietnam lockdowns), same order of magnitude, and adidas was hit slightly harder relative to sales.
- **Full-cycle outcome, both companies measured through their bullwhip and its aftermath (currency-neutral, compounded, my arithmetic).** adidas 2022 +1% (FY2022 release, OPENED), 2023 0%, 2024 +12%, 2025 +10% (REPO-NOTE `adidas_gulden.md`, from adidas releases): **+24% from 2021 to 2025, after absorbing the loss of Yeezy** (about EUR 650M of revenue still in 2024 and zero in 2025, FY2025 release, OPENED). Nike FY22 +6%, FY23 +16%, FY24 +1%, FY25 -9%, FY26 -2% (REPO, 10-K and 8-K rows in `nike_filing_facts.csv`): **+11% from FY21 to FY26.** Adding the current year widens the gap: adidas H1 2026 +14% c-n (Q2 2026 release, OPENED) versus Nike's FY27 guide of a high-single-digit decline.
- **Inference.** The "deferred bust" reading (adidas took its bullwhip pain in 2023, Nike took it in FY25 to FY26, same thing at different times) predicts that the two full-cycle paths converge. They do not: a gap of about 13 points by 2025/FY26 and widening in 2026. The bullwhip was a **trigger** that both companies received; the **differential** is how Nike responded to it (liquidating through FY23 to post +16% c-n growth, then running the classics-heavy, promotion-fed digital model into FY24). In root-cause terms the bullwhip is a necessary-but-not-sufficient condition, and the sufficient cause is Nike's operating model. This confirms the investigator's "about $0" for bullwhip and pull-forward, and it also answers `franchise_oversupply.md` RC2 (which argues the FY23 unit surge was a bullwhip): the surge was industry-wide, but only Nike's version became a multi-year revenue decline.

### RC2. The one macro factor large enough to measure, currency, ran in Nike's favour

The notes do not use foreign exchange, which is a pure macro variable. Nike's own filings quantify it: FX translation was a detriment of about **$419M** to FY25 revenue (FY2025 10-K p. 45, REPO) and a benefit of about **$1,023M** to FY26 revenue (FY2026 10-K p. 44, REPO). Net, about **+$604M of macro tailwind** over FY24 to FY26 (my arithmetic). On a currency-neutral basis the underlying decline is therefore about **$5.6B, not $5.0B** (approximation: 4,964 + 604; each year's FX effect is measured against that year's prior-year rates). Two consequences:
1. The denominator for any attribution grows by about 12%, so the same $0.4B to $1.3B of macro and cycle headwind is a smaller share (7% to 23%).
2. If "macro" is counted honestly in both directions, macro net of FX is close to zero for FY24 to FY26 (gross headwinds $0.4B to $1.3B minus a $0.6B FX tailwind).

### RC3. The digital collapse is not downstream of a post-COVID e-commerce reversal

A macro root cause for Nike's largest single loss (Nike Brand Digital about $12.1B to $8.6B, FY24 to FY26, per the REFUTER section) would be a general consumer shift from online back to stores after COVID. FRED, Census quarterly e-commerce (ECOMNSA and ECOMPCTSA, downloaded 2026-10-13, OPENED; annual sums and averages my arithmetic): US retail e-commerce $1,087B (2023), $1,170B (2024, +7.6%), $1,234B (2025, +5.4%); e-commerce share of retail 15.3% (2023), 16.1% (2024), 16.35% (2025), 17.05% (H1 2026). There was no channel reversal: online kept gaining share while Nike Digital fell 20% and 21% in Q1 and Q2 FY25 (10-Qs, REPO). adidas e-commerce grew 25% and 27% c-n in Q1 and Q2 2026 (REPO-NOTE `digital_tech.md`). Management planned the digital decline itself: "we expect digital traffic to be down double digits in Fiscal 26" after cutting promotional days and paid media (Q3 FY25 call, REPO-NOTE `digital_tech.md`). Upstream cause: the CDA promotional-digital model and its deliberate unwind, not consumer channel behaviour.

### RC4. The "return to FY19 share of wallet" evidence is an artefact of the denominator

Evidence-for item 2 says Nike NA footwear revenue has returned to its FY19 ratio with US footwear PCE (+32.6% vs +31.9%), implying the FY23 to FY24 peak was cycle inflation now unwound. But PCE footwear is *all* footwear (dress, boots, sandals, kids), and athletic took share of that total over the period. Within athletic footwear, Euromonitor puts Nike's US company share at 34.1% (2019) and 28.9% (2025) (REPO-NOTE `dtc_wholesale.md`, SNIPPET there). So against its own category Nike is about 5 points *below* its pre-COVID position, not back at it. The ratio to all-footwear PCE looks "normal" only because the athletic category grew faster than footwear as a whole. The reversion reading overstates the cycle share; what the data show is a market that grew and a brand that lost share inside it.

### RC5. Where macro genuinely sits upstream, and why it still does not carry the weight

The best case for a macro root cause is psychological, not arithmetic: COVID scarcity (sold-out Dunks, an 80%+ digital surge in FY21, REPO rows `growth_digital_cn_pct` Q1 and Q2 FY21) gave Nike a demand signal it extrapolated into the CDA bet on digital and classics. That chain is real (also argued in `franchise_oversupply.md`). But a cause that works only through a management misreading is, for attribution purposes, a management cause: the same signal reached adidas, Deckers, New Balance and On, and none of them produced a multi-year decline from it. The counterfactual test is clean: hold the shock fixed, vary the response, and the outcome follows the response (RC1).

The canvas cycle remains the only external force with a cross-owner signature (Vans and Converse). I accept the REFUTER's reduction ($0.3B to $0.7B) because the Vans control contains VF's own deliberate reset, and because Converse grew in FY23 (+3.4%, REPO) while Vans was already falling, so the two did not share one cycle clock.

### RC6. Revised attribution

| Component | Investigator | ROOT-CAUSE | Reason |
|---|---|---|---|
| Canvas and classics cycle (external part) | $0.7B to $0.9B | $0.3B to $0.7B | Agree with REFUTER (Vans control contaminated) |
| China macro | $0.1B to $0.2B | $0.1B to $0.2B | Agree; NBS apparel and footwear grew 2024 and 2025 |
| EMEA promotions and US lower-income | $0B to $0.4B | $0B to $0.2B | E-commerce grew, Nike NA grew in FY26 as sentiment fell |
| Bullwhip and pull-forward | about $0 | about $0 as a cause; a trigger only | Same shock at adidas, opposite full-cycle outcome (RC1) |
| FX (not in notes) | not counted | **-$0.6B (tailwind)** | 10-K FX translation, FY25 and FY26 |
| **Gross headwinds / share of c-n decline (about $5.6B)** | $0.8B to $1.3B (15% to 25% of reported) | **$0.4B to $1.1B, about 7% to 20%** | |
| **Net of FX** | | **about -$0.2B to +$0.5B, roughly 0% to 10%** | |

FY27 leg: Q1 FY27 North America grew 2.1% while sentiment averaged about 52 (REPO; REFUTER R2b). I side with the REFUTER's 15% to 30% rather than 25% to 40%.

### Verdict

The hypothesis does not survive under the root-cause lens. Macro shocks were real **triggers** (bullwhip, COVID scarcity signal, 2026 sentiment), but each one also hit a peer that did not decline, so the cause of Nike's decline sits downstream of the trigger, in Nike's response: the CDA digital and classics model, its liquidation choices and its newness gap. Three items the notes count as macro or cycle evidence are better explained as Nike-made or as measurement artefacts: the digital collapse (no e-commerce reversal), the FY19 share-of-wallet "reversion" (a denominator effect; athletic share is down 5 points), and the FY24 base "inflation" (the investigator already labels it a symptom). The one macro variable Nike itself quantifies, FX, helped revenue by about $0.6B net. Verdict: **minor**. On a currency-neutral basis macro and cycle explain about 7% to 20% gross and close to zero net of FX.

### ROOT-CAUSE sources

| Source | Date | Status |
|---|---|---|
| adidas FY2022 results release (inventories EUR 5,973M, +49%, causes; 2022 c-n +1%; revenue EUR 22,511M), scratchpad `ads/fy2022.txt` | 2023-03-08 | OPENED |
| adidas FY2025 results release (brand +13% c-n, company +10% c-n, Yeezy about EUR 650M in 2024), scratchpad `ads/fy2025.txt` | 2026-03 | OPENED |
| adidas Q2 2026 results release (H1 2026 +14% c-n), scratchpad `ads/q2_2026.txt` | 2026-07-30 | OPENED |
| adidas 2023 and 2024 c-n growth (0%, +12%), `Gulden and Plank turnarounds vs Nike/adidas_gulden.md` | compiled 2026 | REPO-NOTE |
| Nike FX translation impact FY25 (-$419M, 10-K p. 45) and FY26 (+$1,023M, 10-K p. 44); c-n growth FY22 to FY26; inventories; digital growth rows, `data/nike_filing_facts.csv` | filed 2022-07-21 to 2026-07-15 | REPO |
| FRED ECOMNSA and ECOMPCTSA (US Census quarterly e-commerce), https://fred.stlouisfed.org/graph/fredgraph.csv?id=ECOMPCTSA | downloaded 2026-10-13, data through Q2 2026 | OPENED |
| Euromonitor US athletic footwear share (34.1% 2019, 28.9% 2025), via `dtc_wholesale.md` | 2026 | REPO-NOTE (SNIPPET in that note) |
| `franchise_oversupply.md` RC2, `digital_tech.md` (planned digital traffic decline, adidas e-com 2026) | 2026-10-13 | REPO-NOTE |
| Not checked (search budget exhausted): adidas 2020 and 2021 c-n rates (so the full-cycle comparison starts at 2021), adidas "Own the Game" DTC target as a second test of the COVID-signal response | | GAP |
