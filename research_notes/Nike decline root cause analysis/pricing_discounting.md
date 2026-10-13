# Root cause test: pricing and discounting

Research date: 2026-10-13. Hypothesis under test: *Pricing and discounting (aggressive price increases, then heavy markdowns and Nike Direct promotions training consumers to wait for discounts) eroded value perception and full-price demand.*

Conventions: "REPO" means a number already verified in `research_notes/04_financial_data_pack.md` or `data/nike_filing_facts.csv` (filing and printed page given there). "10-K MD&A" quotes were read in this session from the local text of each 10-K (SEC URLs in the data pack, section 8). Transcript quotes come from Nike's official IR transcripts (investors.nike.com PDFs, saved and read in full text this session; URLs in the source list). OPENED means I read the page or file; SNIPPET means I saw only a search summary.

## 1. Bottom line

- **The hypothesis splits into two parts that behave differently in the data.**
  - **(A) Price increases outran value.** Nike took roughly three rounds of list-price increases: low single digits in spring 2022, mid single digits in FY2023 and low single digits in FY2024. NIKE Brand footwear ASP rose about 18% from FY2021 to FY2024, and North America footwear ASP about 20% (my compounding of 10-K MD&A figures). Over the same three years the US CPI for footwear rose only 5.8% (FRED, May 2021 to May 2024). Units started falling in FY2024 (footwear -2%, apparel -9%), and fell first in the geographies where ASP rose most. Management later conceded that it had "walked away" from "several billion dollars" of sub-$100 revenue (Friend, Oct 2024). This part is real but modest. It mostly cost growth before the peak, not the decline after it.
  - **(B) Discounting and promotion dependence.** This part is large in the numbers. Retailers were discounting 44% of Nike sneakers in early 2024, against 19.4% in early 2022 and 4.5% for Hoka (Reuters/Vertical Knowledge). Nike Digital was "50% full price and 50% off price" (Friend, Dec 2024). Almost all of the NIKE Brand revenue decline from FY2024 to FY2026 sits in Digital, the channel Nike itself had made promotional: Digital fell $3.5B out of a $4.1B NIKE Brand decline, while wholesale was roughly flat. Lower ASP from discounts and channel mix cut FY2025 footwear revenue by about $1.0B and gross margin by about 180 bps.
- **But discounting is mostly a symptom, not an independent cause.** Every discount wave followed a supply or demand shock:
  - The FY2023 wave followed the 2022 industry-wide inventory glut (Nike inventory +44% at Aug 31, 2022).
  - The FY2024 to FY2026 wave followed the classics oversupply (see `franchise_oversupply.md`).
  - Converse units fell before its ASP did.
  - High-heat Nike product (the $100-plus models in FY2024, running in FY2026) sold at full price even at higher prices.
  - The peer test points the same way. Hoka, priced higher (about $148 average), needed almost no discounting.
- **The "trained to wait" mechanism fails its cleanest test.** North America took Digital promotional days from "over 30" to zero (Jan to Feb 2025 vs 2024). Revenue still recovered: FY2026 +5%, with footwear units +6%. Consumers were not permanently trained to wait. They moved to wholesale and full-price channels. The mechanism does hold in Greater China. There Nike's own words are "Our brands have consistently been off-price for consumers, especially in digital, affecting our premium positioning" (Q2 FY26 call), and the decline is deepest. It holds partly in EMEA, where cutting off-price by 50% raised full-price realization 15 points but revenue still fell.
- **Value perception did not erode in the general US population.** YouGov's US Value score for Nike rose from 15.4 (early 2021) to 22.5 (late 2025), and Quality rose from 39.4 to 48.7. What eroded was full-price demand and brand heat among sneaker buyers. That is a product and supply problem showing up through price.
- **Estimate.** The pricing and discounting mechanism accounts for about **$1.5B to $2.5B (30% to 50%)** of the roughly $5.0B FY2024 to FY2026 revenue decline. This mostly overlaps with the oversupply, DTC and marketing estimates in the other notes. The **independent** share is roughly **$0.5B to $1.0B (10% to 20%)**: the price-architecture gap below $100, price increases above category inflation, and promotion habits that went beyond what clearing inventory required. **Fixable: yes for the discount half, partly overall.** North America fixed it in about four quarters. EMEA is mid-way. China runs "beyond fiscal 2027."
- **Verdict: symptom of another cause, with a small independent contribution.** The upstream causes are the classics oversupply and the 2022 glut (supply), the Consumer Direct Acceleration digital model that needed promotions to hit traffic targets (channel), and the lifestyle product cycle fading (demand).

## 2. Predictions and results

| # | Prediction if the hypothesis is true | Data | Held? |
|---|---|---|---|
| P1 | **Price increases precede the unit decline.** Nike's realized prices should rise faster than the category, and units should fall afterwards, first where ASP rose most. | NIKE Brand footwear ASP added +7, +7, +3 pts in FY22, FY23 and FY24, compounding to +17.9%. Apparel ASP +20.2%. NA footwear ASP +20.2%. US CPI footwear +5.8% (May 2021 to May 2024); all-items CPI +16.7%. Units turned down in FY24 (footwear -2%, apparel -9%) while ASP was still rising. FY24 cross-section, footwear: NA ASP +5, units -7. EMEA ASP +5, units -4. Greater China ASP -2, units +8. APLA ASP +1, units +6 (10-K MD&A). | **Yes, partly.** Confounded: FY24 lapped FY23 liquidation volume (NA footwear units +17% in FY23), and Nike deliberately restrained sell-in in Q1 FY24. Nike's ASP also includes the DTC mix shift, while CPI is US-only. In real terms (vs all-items CPI), Nike's price rise only matched general inflation. |
| P2 | **Discounting should precede the revenue decline**, not just follow it. | Retailer discount share on Nike sneakers rose from 19.4% (Q1 2022) to 44% (early 2024). That came before the FY25 revenue fall (Q1 FY25 -10%). Average Nike sneaker price at the 8 chains fell from $103.61 to $79.92. Friend, Q3 FY24 (Mar 2024): "heavy level of promotional activity happening across digital" (REPO). | **Yes** |
| P3 | **The peer test.** If high prices were the problem, higher-priced challengers should struggle. If discounting is Nike-specific, Nike should discount more than peers at the same retailers. | Same 8 chains, early 2024: Hoka 4.5% discounted, Adidas 18.9%, On 23.1%, Puma 37.4%, Nike 44%. On and Hoka averaged about $148 a pair, above Nike. Adidas grew through 2024 to 2026 while cutting discounts (REPO). | **"High price causes weakness" fails. "Nike-specific discounting" holds.** |
| P4 | **Within Nike.** If price levels drive demand loss, premium items should suffer most and cheap lines should hold up. | Q2 FY24: "our $100-plus footwear models driving strong growth in units sold" and "lower markdown rates than many of our competitors." Q3 FY24: performance footwear high single digits, with double-digit growth from $100-plus franchises (Kobe, Ja, Metcon, Structure, Vomero). FY26 running grew over 20% in some quarters at full price. Converse, Nike's cheapest brand, fell 43.6% from FY24 to FY26, with units falling before ASP (FY24 units -12%, ASP -3%; FY26 units -31%, ASP -1 pt). | **Fails** for the price-level leg. Supports discounting as a consequence of weak demand. |
| P5 | **Channel localisation.** The decline should concentrate in the channel with the most promotions (Nike Digital). | NIKE Brand Digital: FY23 $12.6B, FY24 $12.1B, FY25 $9.6B, FY26 $8.6B (REPO). NIKE Brand revenue FY24 to FY26: -$4.1B. Wholesale: $27,758M to $27,453M (-1%). Direct ex-digital (stores, my arithmetic): about $9.4B to $9.1B. Friend, Dec 2024: Digital "50% full price and 50% off price." Off-price mix on Digital "up high single digits." | **Yes, strongly.** About 85% of the NIKE Brand decline is Digital. |
| P6 | **"Trained to wait."** Removing promotions should leave full-price demand persistently depressed and should not move volume to other channels. | NA: Digital promo days went from "over 30" to "zero" (Jan to Feb 2025 vs 2024). Site-wide promo days cut by more than 50 (Q1 FY26). NA FY26 revenue +5% ($19,572M to $20,511M), NA footwear units +6%, NA Q2 FY26 wholesale "over 20%" growth (helped by value-channel liquidation). EMEA, Q4 FY26: off-price "down over 50%," "15-point improvement in full price realization," but EMEA revenue -6% and Q1 FY27 -4.7%. Greater China: digital -27% to -36% c.n. while Nike limited discounts. Reuters (Jul 2026): full-price online sales "have risen over the last two quarters." | **Mixed.** The strong form fails in NA. It holds partly in EMEA and mostly in China. |
| P7 | **Value perception falls.** | YouGov US Value: 15.4 (early 2021) to 22.5 (late 2025). Quality 39.4 to 48.7. Satisfaction 30.4 to 35.7. Global 2025 Value 23.0 vs adidas 25.6. Interbrand brand value -25.9% to $33.7B (2025, SNIPPET). | **Fails** among general consumers. Brand *value* (Interbrand) and heat fell, but perceived value for money rose, probably because of the discounts themselves. |
| P8 | **Margin signature.** Discounting should cut gross margin roughly when the revenue decline starts. | ASP drag on gross margin: Q2 FY25 -330 bps, FY25 -180 bps, Q1 FY26 -250 bps, 9M FY26 -80 bps, Q1 FY27 -30 bps. Full-price ASP (strategic pricing) had *added* 200 to 320 bps in FY24 (REPO). FY25 10-K: lower footwear ASP "primarily due to higher discounts and changes in channel mix, partially offset by strategic pricing actions." | **Yes** (but it is the consequence the hypothesis predicts, not proof of cause) |
| P9 | **Independence.** If discounting is a root cause, discount waves should start without a prior supply or demand shock. | Every wave followed a shock. Inventory hit $9,662M at Aug 31, 2022 (+44%), and the FY23 10-K attributes the margin hit to "higher promotional activity to liquidate inventory." The FY25 to FY26 discounts are tied in the 10-K to "actions to reduce supply of certain footwear products," meaning the classics. Converse units fell first. | **Fails as an independent cause.** Discounting is a symptom. |

## 3. Evidence detail

### 3.1 The price-increase timeline (Nike's own words, transcripts OPENED)
- **Q1 FY22, Sep 23, 2021, Friend:** "the price increases that we've implemented in the second half are in the low-single-digit range." Also: "we exceeded our 65% full price sales realization goal."
- **Q3 FY22, Mar 21, 2022, Friend:** "We did implement a low single-digit price increase in the second half of this year ... But our approach to pricing and to the consumer is a careful one."
- **Q4 FY22, Jun 27, 2022, Friend:** "full-price realization in three of our geographies to be over 70%, whereas our long-term goal was to be at 65%." For FY23, "we're planning for mid-single-digit price increases." He also planned for "normalization of historically low markdown rates."
- **Q2 FY23, Dec 20, 2022, Friend:** "we increased prices by mid-single digits this quarter, and we continue to see that so long as the product is valued by the consumer, we've been able to stick those price increases." In the same call: "NIKE brand ASP is up year-over-year across our geographies, even with higher discounts to liquidate excess inventory."
- **Q4 FY23, Jun 29, 2023:** "our top franchises drove strong full-price sales with mid-single digit price increases" and "low single-digit price increases in FY24." Friend: "the opportunity that creates for us to raise prices."
- **Q2 FY24, Dec 21, 2023, Friend:** "we're excited about the product portfolio we have below $100 ... to get back on our front foot at an important price point."
- **Q3 FY24, Mar 21, 2024, Friend:** "over the last couple of years, given our brand strength, we've been able to implement strategic pricing in order to be able to offset some of the headwinds."
- **Q4 FY24, Jun 27, 2024, Friend:** "better balance between high price points and lower price points."
- **Q1 FY25, Oct 1, 2024, Friend:** "the core opportunity, which we define as below $100 ... represents several billion dollars' worth of revenue that we walked away from over the last couple of years." **This is the strongest admission for leg (A).** It is about price *architecture* and the distribution that serves it, not list-price increases alone, and it overlaps with `dtc_wholesale.md`.
- **Q4 FY25, Jun 26, 2025, Friend:** "a surgical price increase in the United States with phased implementation beginning in fall '25" (tariffs). Press reports (SNIPPET, FashionUnited, May 22, 2025): from June 1, 2025, shoes priced $100 to $150 went up $5 and shoes above $150 up to $10, shoes under $100 were unchanged, and adult apparel and equipment rose $2 to $10. Kids, Jordan and the AF1 were excluded.
- **Q1 FY27, Oct 1, 2026, Hill:** Family Footwear ("core footwear") is "at $65 to $85 segment" across running, basketball, training and sportswear.

Specific list prices (SNIPPET, search summary of sneaker press): AF1 and Dunk Low $90 (2021), $100 (2022), $115 (2023). AJ1 High $160 (2019) to $170 (informal post). Not verified on Nike's site.

### 3.2 Units vs ASP (10-K MD&A, OPENED; currency-neutral; NIKE Brand)

| Year | Footwear units | Footwear ASP (pts) | Apparel units | Apparel ASP (pts) | Nike's stated ASP driver |
|---|---|---|---|---|---|
| FY2019 | +8% | +4 | +6% | +5 | full-price ASP, lower discounts |
| FY2020 | -8% | +6 | -8% | +5 | full-price and Direct ASP |
| FY2021 | +11% | +7 | +14% | +1 | full-price ASP, "lower discounts" |
| FY2022 | -3% | +7 | flat | +6 | Direct ASP, higher full-price mix |
| FY2023 | +13% | +7 | +4% | +4 | strategic pricing, offset by "higher promotional activity" in Direct |
| FY2024 | -2% | +3 | -9% | +9 | full-price ASP (strategic pricing) |
| FY2025 | -8% | -3 | -5% | 0 | "higher discounts and changes in channel mix, partially offset by strategic pricing actions" |
| FY2026 | -1% | -1 | +1% | +1 | channel mix, offset by product mix and strategic pricing |

Sources: FY2019 to FY2026 10-Ks, "NIKE Brand Revenues by ... Fiscal 20xx compared to Fiscal 20xx" sections (URLs in the data pack). Readings:
- Footwear units were only about 2% lower in FY2026 than in FY2021 (my compounding). Most of the revenue growth up to the FY2024 peak came from price and mix (footwear ASP +17.9% FY22 to FY24). The FY2024 peak was therefore price-built, and the elasticity bill came due as units fell.
- In FY2025 units fell further (-8%) *while* ASP fell (-3 pts). Cheaper Nike did not sell more units. That is a demand or heat problem, not a price-level problem.
- Geography, FY2025 footwear units: NA -10%, EMEA -8%, GC -11%, APLA -2%. FY2026: NA +6%, EMEA -2%, GC -14%, APLA -3%. NA was the first market to clean up and the first to grow units.

### 3.3 Discounting depth and Nike-specificity
- **Reuters / Vertical Knowledge, via FashionNetwork USA, 2024-02-02 (OPENED):** online prices at eight national chains (Foot Locker, Dick's, Macy's among them). Retailers "slashed prices on 44 percent of their Nike sneakers on average in 2024," up from 19.4% in the comparable 2022 period. Hoka 4.5%, Adidas 18.9%, On 23.1%, Puma 37.4%. The average Nike sneaker price fell to $79.92 from $103.61 (Q1 2022), and On and Hoka averaged about $148. Matt Powell: Nike was "stuffing the market," and frequent discounts risk Nike "becoming another shoe brand." The "2024" period is the first weeks of calendar 2024, given the publication date.
- **Nike Digital promotions (transcripts OPENED):**
  - Q2 FY25 (Dec 19, 2024): "on NIKE Digital, our off-price mix was up high single digits versus the prior year." Friend: "the business being 50% full price and 50% off price today, the profitability of the channel has significantly been challenged."
  - Q3 FY25 (Mar 20, 2025), Hill: "Nike Digital in North America went from over 30 promotional days to zero" (Jan to Feb, year on year). Friend: "we were buying against a different plan."
  - Q1 FY26 (Sep 30, 2025): "reducing the number of days of site-wide promotion by more than 50." Organic traffic "continues to decline double digits," because last year's business was "more concentrated on classic footwear franchises and sneaker launch as well as a higher mix of off-price sales."
  - Q2 FY26 (Dec 18, 2025), on Greater China: "Our brands have consistently been off-price for consumers, especially in digital, affecting our premium positioning across the entire integrated marketplace."
  - Q3 FY26 (Mar 31, 2026), on EMEA: "We were also more aggressive with promotions on NIKE Digital at the end of the season." This was a relapse.
  - Q4 FY26 (Jun 30, 2026), on EMEA: "off-price was down over 50% following aggressive actions to reduce promotions. This resulted in a 15-point improvement in full price realization." Friend: "a much higher level of digital promotions in EMEA last year in the second quarter."
- **Q1 FY27 10-Q (REPO, OPENED):** the additional Sportswear and Jordan actions reflect "in part, higher levels of discounting and broader marketplace pressure." Lower NIKE Brand ASP cut gross margin by about 30 bps.

### 3.4 Origins of each discount wave (shows it is downstream)
- **2020 (COVID):** factory-store markdowns because of low traffic (Q1 and Q2 FY21 calls). This was temporary.
- **FY2021 to FY2022:** markdowns were "historically low" and full-price realization was above 70%, because supply was constrained (Vietnam closures, transit delays). The price increases were taken *in this scarce window*, when they were easiest to "stick."
- **FY2023:** inventory reached $9,662M at Aug 31, 2022 (+44% YoY, REPO). FY23 10-K: lower Direct margin was "driven by higher promotional activity to liquidate inventory in the current period compared to lower promotional activity in the prior period resulting from lower available inventory supply." Q1 FY23 guidance cited "approximately 150 basis points of annual impact from higher markdowns and higher off-price mix to liquidate elevated inventory." The whole industry had this glut. Adidas cut sell-in and limited point-of-sale spend in 2023 (REPO, `adidas_gulden.md`).
- **FY2024 to FY2026:** classics oversupply. The FY25 10-K describes "our actions to reduce supply of certain footwear products in the marketplace through increased markdowns across NIKE Direct and discounts and higher sales returns with our wholesale partners." See `franchise_oversupply.md` for the evidence on the Dunk, AF1 and AJ1.
- **Converse (10-K MD&A, OPENED):**
  - FY24: units -12%, "ASP decreased 3%, primarily driven by increased promotional activity in direct to consumer."
  - FY25: units -12%, ASP -6 pts "higher discounts in direct to consumer."
  - FY26: units -31%, ASP -1 pt.
  - Units led, discounts followed, and the brand's low price points did not protect it.

### 3.5 Value perception data
- **YouGov, Feb 5, 2026 (OPENED):** US Value: adidas 23.5 vs Nike 15.4 (early 2021), adidas 26.1 vs Nike 22.5 (late 2025). US Quality: Nike 39.4 to 48.7. Global 2025: Value Nike 23.0 vs adidas 25.6; Index 34.5 vs 35.3. Nike's perceived value rose through the decline, so "eroded value perception" is not supported among the general population. The plausible reading: discounts raised perceived value for money while lowering willingness to pay full price for the product that was oversupplied.
- **Interbrand 2025 (SNIPPET, SGI Europe):** Nike brand value -25.9% to $33.7B. That is a financial-based valuation, so it partly restates the revenue and margin fall.
- **YouGov US consideration (SNIPPET):** Skechers rose from 33.4 (2024) to 35.5 (2025), close to Nike.
- **WSJ (Inti Pacheco), via Kanebridge News, Jan 13, 2025 (OPENED):** "Nike also cut back on styles that sold for less than $100." Skechers sales of $8 billion in 2023, up from $1.8 billion a decade earlier.

### 3.6 Academic mechanism (SNIPPET only, abstracts)
- **Mela, Gupta and Lehmann (1997), JMR 34(2):** in packaged-goods panel data, consumers become more price- and promotion-sensitive over time "because of reduced advertising and increased promotions." This supports the mechanism in principle. Nike cut brand advertising in favour of performance marketing while raising promotions (`marketing_shift.md`).
- **Soysal and Krishnamurthi (2012), Marketing Science 31(2):** in fashion retail, strategic consumers wait for markdowns, and that delay cut retailer revenue by about 9% vs myopic consumers. Limited availability reduces the delay. The scarcity-to-abundance switch on the classics would raise strategic waiting, consistent with `franchise_oversupply.md`.
- These papers show the mechanism exists. They do not measure it at Nike.

### 3.7 China and EMEA (mechanism holds best here; REPO notes)
- Greater China gross margin went from 51.0% (FY23) to 45.7% (FY26). Outlet clearance at 55% of list already in 2023. Industry discounts at about 50% to 70% of list. Management admits frequent discounting "严重削弱品牌在市场中的影响力" ("severely weakens the brand's influence in the market") (Sina 2026-06-05, REPO).
- **Reuters (Casey Hall, Danielle Kaye), Jul 22, 2026, via KELO (OPENED):**
  - Wei Kan (former Nike Greater China brand director): "Otherwise, the consumer will always expect the discounted Nike product."
  - Ivan Su (Morningstar): "Consolidating into official storefronts only works if the product justifies the price."
  - From January 2027, key retailers will stop selling Nike online.
- China is where the "trained to wait" mechanism best fits. China's decline is also confounded by guochao, Anta and the macro slump (`china.md`).

## 4. Strongest evidence for
1. Channel localisation. Digital, the channel Nike ran at "50% off price," accounts for about $3.5B of the $4.1B NIKE Brand decline from FY24 to FY26. Wholesale is flat.
2. Nike discounted far more than peers at the same retailers in early 2024: 44% of sneakers vs Hoka 4.5%, Adidas 18.9% and On 23.1%. This came before the FY25 revenue fall.
3. Price increases outran the category: footwear ASP +17.9% (FY22 to FY24) vs US CPI footwear +5.8%. Units started falling in FY24 in NA and EMEA, where ASP rose most, while Greater China, with lower ASP, grew units.
4. Management admitted walking away from "several billion dollars" of sub-$100 revenue, and in China that off-price positioning damaged "premium positioning."
5. Lower ASP (discounts and mix) cut FY25 footwear revenue by about $1.0B (3 pts of $33.4B) and gross margin by about 180 bps (about $0.8B).

## 5. Strongest evidence against
1. Discounting followed supply shocks every time: the 2022 glut, the classics oversupply, and Converse unit declines that came before ASP declines. It is a downstream symptom.
2. High-heat Nike product sold at full price despite higher prices ($100-plus models in FY24, running in FY26). Higher-priced Hoka and On needed little discounting. Price level was not the binding constraint.
3. The North America natural experiment: Digital promo days went to zero, yet NA revenue grew 5% in FY26 and footwear units grew 6%. Consumers were not durably trained to wait.
4. US perceived value (YouGov) rose from 15.4 to 22.5 during the decline.
5. In FY25, units fell 8% even as ASP fell 3 pts. Cutting realized price did not restore volume, which points to demand and heat, not price.
6. In real terms Nike's price rises roughly matched general inflation (all-items CPI +16.7% vs footwear ASP +17.9%). The gap is against the footwear category, which was flat because it was promotional.

## 6. Upstream causes
- **Supply:** the classics oversupply (Dunk, AF1, AJ1) and the 2022 inventory glut created the inventory that had to be marked down.
- **Channel model:** Consumer Direct Acceleration needed Digital traffic growth. Performance marketing plus promo days delivered it, and Nike Digital became a clearance channel (Hill, Dec 2024: "capturing demand and competing with our wholesale partners rather than creating and growing demand").
- **Product cycle:** lifestyle classics fatigue and a thin innovation pipeline removed full-price demand (`innovation_drought.md`, `challengers_taste.md`).
- **Independent element:** a price-architecture choice (premiumising and leaving sub-$100 and family footwear) and list-price increases taken during the 2021 to 2022 scarcity window. These are genuine pricing decisions, but small relative to the decline.

## 7. Quantification
Total decline FY2024 to FY2026: $51,362M to $46,398M = **-$4,964M** (REPO).

| Component | Estimate | Basis | Overlap |
|---|---|---|---|
| Lower realized ASP (discounts plus channel mix) | about -$1.2B | FY25 footwear ASP -3 pts x $33,427M = -$1.0B. FY26 footwear -1 pt x $29,510M = -$0.3B, partly offset by apparel +1 pt (+$0.13B) | Mostly the clearing of oversupplied classics. Channel-mix part overlaps `dtc_wholesale.md` |
| Promotion-dependent Digital revenue removed when promos were cut | about $1.0B to $1.5B gross, $0.5B to $1.0B net of shift to wholesale | Digital -$3.5B FY24 to FY26. Nike names promo days, markdowns, classics, launches and paid media together. I assign about a third to promos and markdowns. NA shows much of it moved to wholesale | Overlaps `marketing_shift.md` (paid media) and `franchise_oversupply.md` |
| Price-architecture and elasticity loss (sub-$100 exit, increases above the category) | $0B to $0.5B of the decline after the peak | Friend's "several billion" was lost *before* the peak, so it mostly reduced growth. FY24 to FY26 unit losses are mainly explained by classics and China | Overlaps `dtc_wholesale.md` (family footwear accounts) |
| **Total mechanism** | **about $1.5B to $2.5B (30% to 50%)** | | Largely shared with other hypotheses |
| **Independent of other causes** | **about $0.5B to $1.0B (10% to 20%)** | price architecture, increases above the category, promotion habits beyond what clearance needed (EMEA relapse in Q3 FY26) | |

Gross margin: the ASP drag (discounts and mix) was about 180 bps in FY25 (about $0.8B of gross profit), the largest single driver of the FY25 margin fall. In FY26 to Q1 FY27 it shrank to 80 bps (9M FY26) and 30 bps (Q1 FY27), and tariffs became the larger drag.

## 8. Fixability
**Fixable: partly, and the discount half is the most fixable part of Nike's problem.**
- **North America:** promo days went to zero, closeout mix "very healthy," NA margins up ex-tariffs for three quarters, and revenue growing. This took about 4 quarters.
- **EMEA:** off-price -50% and full-price realization +15 pts in Q4 FY26. Revenue is still falling, and Sportswear sell-through is "challenging." Nike targeted end of calendar 2026.
- **Greater China:** distributor online channel to be cut from Jan 2027. The 10-Q says the drag extends "beyond fiscal 2027."
- **Price architecture:** the $65 to $85 core line through Family Footwear is being rebuilt (Q1 FY27).
- **Limits:** ending discounts exposes weak underlying demand. Under Armour's 20% to 27% e-commerce declines are the cautionary case (REPO, `under_armour_plank.md`). Removing promotions removes the revenue they bought, so the fix lowers revenue before it raises margin. It cannot by itself create full-price demand for oversupplied lifestyle product.

## 9. Gaps
- Nike does not disclose its markdown rate, its full-price realization percentage after FY22, or Digital off-price share beyond "50/50." No third-party Nike.com discount-share series was found. The Vertical Knowledge series is a single snapshot (Q1 2022 vs early 2024).
- No Circana Nike-specific ASP or unit series was found.
- CPI is US-only, while Nike's ASP is global, wholesale-equivalent and mix-affected. So the "price outran category" comparison is directional.
- The academic evidence is from abstracts only (SNIPPET).
- The BLS API daily limit was hit, so I used FRED's copy of the same BLS series (CUUR0000SEAE, CPIAUCNS).

## 10. Sources

| Source | Date | Status | Used for |
|---|---|---|---|
| Nike 10-Ks FY2019 to FY2026, MD&A unit/ASP and gross margin sections (SEC URLs in `04_financial_data_pack.md` section 8; local text copies read) | 2019-07-23 to 2026-07-15 | OPENED | Units vs ASP table, margin drivers, Converse, FY23 promo language, FY25 markdown language |
| `data/nike_filing_facts.csv`, `04_financial_data_pack.md` | 2026-10-12 | REPO | Revenue, Digital, inventory, gm_driver bps, segment revenue |
| Nike Q1 FY21 to Q1 FY27 official call transcripts, investors.nike.com/_assets/.../nike/db/938/{9384..9406,9540,9591}/webcast_transcript/*.pdf | 2020-09-22 to 2026-10-01 | OPENED (full text) | Every Friend, Hill and Donahoe quote in sections 3.1, 3.3 and 3.4 |
| FRED CUUR0000SEAE (CPI footwear) and CPIAUCNS, fred.stlouisfed.org/graph/fredgraph.csv | fetched 2026-10-13 | OPENED | CPI footwear +5.8% and all-items +16.7% (May 2021 to May 2024) |
| Reuters via FashionNetwork USA, "Retailers slash prices on more Nike sneakers in 2024, data shows," us.fashionnetwork.com/news/...,1600865.html | 2024-02-02 | OPENED | 44% vs 19.4%, peer shares, $79.92 vs $103.61, Powell quotes |
| WSJ (Inti Pacheco) via Kanebridge News, "Skechers Went After the Customers Nike Didn't," kanebridgenews.com/skechers-went-after-the-customers-nike-didnt-it-paid-off/ | 2025-01-13 | OPENED | Nike cut sub-$100 styles; Skechers $8B |
| YouGov (Rishad Dsouza), "adidas vs Nike: A close race in global brand perception," yougov.com/articles/54038 | 2026-02-05 | OPENED | Value, Quality and Satisfaction scores |
| Reuters (Hall, Kaye) via KELO, "After tackling discounts in China, Nike still needs to win back shoppers," kelo.com/2026/07/22/... | 2026-07-22 | OPENED | Wei Kan, Ivan Su quotes; Jan 2027 online cut |
| FashionUnited, "Nike to raise prices in the US amid tariffs," fashionunited.com/news/business/nike-to-raise-prices-in-the-us-amid-tariffs/2025052266167 | 2025-05-22 | SNIPPET | June 2025 price-increase tiers |
| Fast Company, "Nike to introduce $100 sneaker line..." fastcompany.com/91150550 | 2024-06/07 | SNIPPET | $100-and-under line, GlobalData "price-sensitive consumers" |
| YouGov, "Nike leads U.S. fashion brand consideration as Skechers gains ground," yougov.com/en-us/articles/54374 | 2025/26 | SNIPPET | Skechers consideration 33.4 to 35.5 |
| SGI Europe, Interbrand 2025 ranking | 2025 | SNIPPET | Nike brand value -25.9% to $33.7B |
| Sneaker price history (nicekicks.com, kyw.substack.com search summaries) | 2021 to 2023 | SNIPPET | AF1 and Dunk $90 to $115; AJ1 $160 to $170 (unverified) |
| Mela, Gupta, Lehmann (1997) JMR 34(2):248-261, DOI 10.1177/002224379703400205 | 1997 | SNIPPET | Promotion raises long-run price sensitivity |
| Soysal and Krishnamurthi (2012) Marketing Science 31(2):293-316, DOI 10.1287/mksc.1110.0693 | 2012 | SNIPPET | Strategic waiting cuts revenue about 9% |
| Deckers call summaries (MarketBeat, Nasdaq) | 2023 to 2026 | SNIPPET | Hoka full-price selling (qualitative) |
| Repo notes reused: `franchise_oversupply.md`, `dtc_wholesale.md`, `marketing_shift.md`, `china.md`, `retailers_and_resale.md`, `adidas_gulden.md`, `under_armour_plank.md`, `nike_standing.md`, `china_market.md` | 2026-10-13 | REPO | Stack "hangover," China discount data, adidas and UA playbooks, Q1 FY27 Denton quotes |

## Challenge: REFUTER

Date: 2026-10-13. Lens: try to disprove the hypothesis and check the investigator's numbers against primary sources. Sources are local text copies of Nike's official IR call transcripts (investors.nike.com PDFs, read in full this session), Nike 10-K and 10-Q filings on SEC EDGAR (local text copies read), FRED, and adidas' and Piper Sandler's own PDFs. All marked OPENED were read this session. Limit: the session's shared WebSearch budget ran out before this check started. So I found no new third-party discount-rate series after early 2024, and I could not re-open the Reuters/Vertical Knowledge article. Its 44% figure stays as the investigator's OPENED citation, not re-verified by me.

### R1. Numbers checked against primary sources

| Claim in the notes | Check | Result |
|---|---|---|
| Digital $12.1B (FY24) to $8.6B (FY26); NIKE Brand -$4.1B; about 85% in Digital | REPO `revenue_nike_brand` 49,322 to 45,222 = -4,100; `revenue_nike_brand_digital` 12.1 to 8.6 | Arithmetic correct (85%). But the "wholesale flat" claim only holds as a two-year endpoint. Wholesale fell $1,875M (-7%) in FY25 (27,758 to 25,883) and then recovered. |
| FY25 footwear ASP -3 pts, units -8%, gross margin ASP drag 180 bps | FY25 10-K MD&A (OPENED) | Correct. But the 10-K attributes the ASP decline to "higher discounts **and changes in channel mix**, partially offset by strategic pricing actions." It does not split the two. |
| FY26 ASP -1 pt counted as discounting | FY26 10-K MD&A (OPENED): "Lower ASP per pair was primarily due to channel mix, partially offset by product mix and strategic pricing" | **Wrong attribution.** Discounts are not named as a FY26 driver. The about $0.2B net for FY26 should not be counted as discounting. |
| US CPI footwear +5.8% May 2021 to May 2024 | FRED CUUR0000SEAE fetched 2026-10-13 (OPENED): 138.385 to 146.401 | Correct (+5.79%). |
| "50% full price and 50% off price" | Q2 FY25 transcript, Dec 19, 2024 (OPENED) | Verbatim, about NIKE Digital profitability. |
| "Over 30 promotional days to zero" | Q3 FY25 transcript, Mar 20, 2025 (OPENED) | Verbatim, NA Digital, Jan to Feb vs prior year. |

### R2. Leg A ("aggressive price increases") is overstated: ASP is not list price
- **FY22 ASP was mostly mix and fewer markdowns, not price increases.** FY22 10-K (OPENED): the +7 pt ASP was "primarily due to higher NIKE Direct ASP, the favorable impact of growth in our NIKE Direct business, higher full-price ASP, net of discounts ... and a higher mix of full-price sales." Nike Direct is booked at retail price, so moving to DTC raises ASP mechanically.
- **So the +17.9% ASP vs +5.8% CPI comparison mixes up two different things.** Nike's own stated list-price actions were:
  - low single digits in the second half of FY22 (Q1 FY22 and Q3 FY22 calls, OPENED);
  - mid single digits in FY23 (Q4 FY22 and Q2 FY23 calls, OPENED);
  - low single digits in FY24 (Q4 FY23 call, OPENED).
- **In real terms, list prices fell.** Those increases compound to roughly 8% to 10% (my estimate from the stated ranges). That is close to footwear CPI (+5.8%) and well below all-items CPI (+16.7%). "Aggressive" list pricing is not supported. The price-level leg survives only as a price-*architecture* choice (exiting sub-$100). That is a product and distribution decision, not a pricing-and-discounting mechanism.
- **The FY24 cross-section that the notes use is confounded.**
  - Greater China units +8% at ASP -2 in FY24 was the post-lockdown reopening year (FY23 included the 2022 lockdowns).
  - NA footwear units -7% in FY24 lapped +17% in FY23 liquidation volume. The two-year NA unit stack is still positive (my arithmetic: 1.17 x 0.93 = about +9%).

### R3. Time series: the biggest promotion wave was followed by stronger full-price pricing, not weaker
- **FY23 was Nike's heaviest promotional year.** FY23 10-K (OPENED): Direct margin fell on "higher promotional activity to liquidate inventory."
- **"Trained to wait" predicts weak full-price realization in FY24. The opposite happened.** FY24 10-K (OPENED): gross margin +110 bps, with "Higher NIKE Brand full-price ASP, net of discounts ... (increasing gross margin approximately 200 basis points), primarily due to strategic pricing actions." Consumers paid more for full-price Nike right after the liquidation year.
- **Adidas shows the same pattern.** It liquidated Yeezy and excess inventory in 2023, then returned to full-price growth with gross margin at 51.6% in 2025 (adidas FY2025 results PDF, OPENED). Heavy promotion did not durably impair either brand when product heat existed.

### R4. Channel localisation fails on timing and dose-response
The notes treat the Digital collapse as revenue that existed only because of promotions. The quarterly data does not support that.

- **Digital fell hardest while promotions were rising, not after they were cut.** Global NIKE Digital (calls, OPENED):
  - Q3 FY24: -4%, during a "heavy level of promotional activity happening across digital."
  - Q4 FY24: -10%.
  - Q1 FY25: -20%.
  - Q2 FY25: NA -22% and EMEA -32%, in the same quarter that "on NIKE Digital, our off-price mix was up high single digits." Friend later called it "a much higher level of digital promotions in EMEA last year in the second quarter" (Q4 FY26 call).
  - More discounting did not hold Digital volume up.
- **Cutting promotions did not cause a step down.**
  - NA Digital went from -22% (Q2 FY25, promotional) to -12% (Q3 FY25, the Jan to Feb window with zero promotional days). Removing promotions coincided with a *smaller* decline.
  - EMEA Digital: -32% with heavy promotions (Q2 FY25) and -24% with off-price "down over 50%" (Q4 FY26). The rate of decline barely depended on how heavy promotions were.
- **Nike's own explanation is supply and traffic.**
  - Q1 FY25 (OPENED): the classic franchises "were down nearly 50% versus the prior year on NIKE Digital while we saw much better sales trends in wholesale." That was a deliberate allocation cut.
  - Q3 FY25 and Q1 FY26 (OPENED): paid media was cut, "reduced the classic share of business," and "reduced the launch share of business."
  - FY25 10-K (OPENED): results "reflected a decrease in traffic across NIKE Direct."
  - Removing promotional days is one of five simultaneous actions. Nothing in the data isolates it.
- **The investigator's figure for promotion-dependent Digital revenue is a judgment, not a measurement.** The "$0.5B to $1.0B net" comes from "I assign about a third." The dose-response pattern above gives no support for a separate promotion component of that size.

### R5. After the discount drag ended, the decline continued and became pure volume
- **The ASP drag is now small.** Q1 FY27 10-Q (OPENED): NIKE Brand footwear -6% currency-neutral, units -5%, ASP only -1 pt ("channel mix and higher discounts, partially offset by strategic pricing"). The investigator's own series puts the gross-margin ASP drag at 30 bps.
- **Greater China is the decisive case.** This is where the notes say the mechanism "holds best."
  - FY26: footwear units -14%, with lower ASP "partially offset by lower discounts" (FY26 10-K, OPENED).
  - Q1 FY27: footwear units -26%, ASP flat "as lower discounts were offset primarily by channel mix" (Q1 FY27 10-Q, OPENED).
  - Discounts are falling, yet the unit decline is getting worse.
- **The peer test shows the market is not the problem.** In the same market and the same promotional environment, adidas Greater China grew +15% currency-neutral in Q2 2026 and +16% in H1 2026. Adidas described the period as "heightened promotional activity in the marketplace" (adidas Q2 2026 results, Aug 2026, OPENED).
- **What adidas' growth points to.** It shows that consumers in China still buy foreign sportswear at full price. That is consistent with "Nike consumers were trained to wait" only if the training is Nike-specific. The simpler reading is that Nike lost demand in China for product and competitive reasons, and Nike is now removing the discounts that were masking that loss.

### R6. Value-perception and brand-heat data
- **Teen mindshare fell, but the fall does not track the discount waves.** Piper Sandler Taking Stock With Teens infographics (Piper Sandler PDFs, OPENED; scratchpad copies): Nike footwear mindshare was 60% (Spring 2022), 61% (Spring 2023), 57% (Fall 2024) and 49% (Spring 2025). Spring 2024 noted a loss of 510 bps among upper-income teens in athletic footwear.
  - The decline begins in 2024, after the FY23 promotion wave had already been followed by strong full-price FY24.
  - It lines up with lifestyle-classics fatigue and challenger growth (New Balance gained about 200 bps in Fall 2023).
  - This is brand heat, not value perception. The YouGov US Value rise (15.4 to 22.5) still contradicts the "eroded value perception" part of the hypothesis.

### R7. Revised quantification (refuter view)
| Component | Investigator | Refuter | Why |
|---|---|---|---|
| Lower realized ASP | about $1.2B | about $0.4B to $0.7B | Only the FY25 discount share of the -3 pts counts. The 10-K pairs discounts with channel mix, and the channel mix follows mechanically from the Digital decline. The FY26 -1 pt is channel mix by the 10-K's own wording. All of it is clearing of oversupplied classics (upstream). |
| Promotion-dependent Digital revenue | $0.5B to $1.0B net | about $0B to $0.3B | No step down when promotions were cut. The decline was steepest at peak promotion (R4). |
| Price architecture | $0B to $0.5B | $0B to $0.3B | List prices fell in real terms. The sub-$100 exit is a product and distribution choice, already in `dtc_wholesale.md`. |
| **Mechanism total** | $1.5B to $2.5B (30% to 50%) | **about $0.5B to $1.2B (10% to 25%)** | |
| **Independent of other causes** | $0.5B to $1.0B (10% to 20%) | **about $0.2B to $0.5B (5% to 10%)** | Mainly the Greater China and EMEA promotion habit beyond what clearance needed (the Q3 FY26 EMEA relapse). |

The gross-margin effect is real. The 180 bps in FY25 is confirmed (FY25 10-K), but it includes the channel-mix effect, and most of the drag is the cost of clearing upstream oversupply.

### R8. Refuter verdict
- **As a root cause of the revenue decline, the hypothesis does not survive.** Its specific predictions fail:
  - List prices did not outrun inflation in real terms.
  - The heaviest promotion year (FY23) was followed by stronger full-price pricing (FY24).
  - Digital fell hardest while promotions rose and did not step down when they were cut.
  - Units kept falling in FY25 when Nike was cheaper.
  - Units are falling faster in China now that discounts are being cut, while adidas grows in the same market.
- **What does survive.** Nike discounted more than its peers (Vertical Knowledge, early 2024), and discounting cut FY25 gross margin. Both are consequences of the classics oversupply and of a Digital model that depended on traffic.
- **Verdict:** symptom of another cause, with a smaller independent share than the investigator estimated (about 5% to 10%).

### R9. Refuter sources
| Source | Date | Status |
|---|---|---|
| Nike call transcripts Q1 FY22, Q3 FY22, Q4 FY22, Q2 FY23, Q4 FY23, Q3 FY24, Q4 FY24, Q1 FY25, Q2 FY25, Q3 FY25, Q4 FY25, Q1 FY26, Q4 FY26, Q1 FY27 (investors.nike.com PDFs; local text) | 2021-09-23 to 2026-10-01 | OPENED |
| Nike FY2022, FY2023, FY2024, FY2025, FY2026 10-K MD&A and gross margin sections (sec.gov/Archives/edgar/data/320187/..., local text) | 2022-07-21 to 2026-07 | OPENED |
| Nike Q1 FY2027 10-Q, nke-20260831.htm (sec.gov) | filed 2026-10-02 | OPENED |
| REPO `data/nike_filing_facts.csv` (revenue_nike_brand, revenue_nike_brand_digital, revenue_wholesale, segment channel lines) | 2026-10-12 | REPO |
| FRED CUUR0000SEAE, fred.stlouisfed.org/graph/fredgraph.csv?id=CUUR0000SEAE | fetched 2026-10-13 | OPENED |
| adidas Q2 2026 results PDF (adidas-group.com) | Aug 2026 | OPENED |
| adidas FY2025 results PDF (adidas-group.com) | Mar 2026 | OPENED |
| Piper Sandler Taking Stock With Teens infographics, Spring 2022 to Spring 2025 (pipersandler.com PDFs) | 2022 to 2025 | OPENED |

## Challenge: ROOT-CAUSE

Challenge date: 2026-10-13. Lens: accept that the symptom is real (Nike took price, then discounted heavily, and full-price demand fell) and ask whether pricing and discounting is itself the downstream effect of a different cause. Status labels as above. Nike call quotes were re-read by me from the official Nike IR transcript PDFs (full-text copies in the session scratchpad): **OPENED**. Nike, Deckers and adidas filings and results releases were read by me from EDGAR or company IR copies saved in the session scratchpad: **OPENED**. Quarterly Digital growth rates are from `data/nike_filing_facts.csv` (**REPO**, each row cites its 10-Q and page). All arithmetic is mine. Note: the shared web-search budget for this run was exhausted before this pass began, so this challenge rests on primary documents already downloaded plus the repo, and I did not work around the limit.

### Verdict
**The investigator's "symptom" verdict survives, and the independent share should be cut further.** Each leg of the hypothesis traces upstream to something else: the price increases to COVID-era cost inflation that the whole industry passed through, the discount waves to supply shocks and the classics concentration, the sub-$100 exit to the Consumer Direct Acceleration (CDA) account cuts, and the Digital revenue collapse to the deliberate pull of classics from Digital plus a traffic loss that was already under way while promotions were *rising*. The cleanest new test (RC2) shows Digital fell about 20% a quarter in H1 FY25 while off-price mix on Digital was going *up*, before the North America promotional days were cut. That is the opposite of what "revenue lost when promotions were removed" predicts. A peer natural experiment (RC4) shows adidas ran the same price-up, discount-down sequence in the same years, including a 36% collapse with inventory takebacks in Greater China, and then grew double digits in every region once its product was hot. Consumers were not durably "trained" against a brand whose product they wanted. My estimate of the truly independent share: **about 0% to 5% of the FY24 to FY26 decline (up to about $0.25B)**, versus the investigator's 10% to 20%. As a transmission mechanism (non-additive) the investigator's $1.5B to $2.5B is reasonable for FY25 margin and ASP, but most of its Digital component belongs to the classics and CDA notes.

### RC1. The price increases were cost pass-through, and the industry did the same
- **FY23 10-K (filed 2023-07-20, OPENED), Overview:** "Inflationary pressures, including higher product input, freight and logistics costs negatively impacted gross margin for fiscal 2023. The strategic pricing actions we have taken partially offset the impacts of these higher costs." Gross margin fell 250 bps to 43.5% *despite* the mid-single-digit increases. In North America, gross margin contraction of 310 bps came from "higher input costs and inbound freight and logistics costs ... partially offset by higher full-price ASP, net of discounts, largely due to strategic pricing actions." [FY23 10-K](https://www.sec.gov/Archives/edgar/data/320187/000032018723000039/nke-20230531.htm)
- **FY22 10-K (filed 2022-07-21, OPENED):** FY22 margin expansion was "partially offset by elevated freight and logistics costs"; management listed "pricing actions" among mitigation steps for supply-chain disruption. [FY22 10-K](https://www.sec.gov/Archives/edgar/data/320187/000032018722000038/nke-20220531.htm)
- **adidas FY2022 results (released 2023-03-08, OPENED, adidas IR PDF):** "Broad-based price increases were more than offset by the strong increase in supply chain costs." Q4 2022 gross margin fell 9.9 pts to 39.1% on "significantly higher supply chain costs as well as the strong increase in promotional activity."
- **Deckers FY2024 10-K (period ended 2024-03-31, filed 2024-05-24, OPENED, accession 0000910521-24-000017):** gross margin rose to 55.6% from 50.3% helped by "selective price increases" and "favorable full-price selling"; HOKA net sales grew 27.9% to $1,806.7M. A peer raised prices in Nike's FY24 window and grew fast.
- **Reading:** a list-price rise that only partly covered cost inflation, and that peers matched, is not "aggressive pricing" in a causal sense. The upstream cause of leg (A) is the 2021 to 2022 cost and freight shock. The part that is Nike-specific is narrower: FY24 full-price ASP added 200 bps (REPO) once freight normalised, i.e. Nike kept the price after the cost went away. That residual is small and coincided with units -2% in FY24, which lapped FY23 liquidation volume.

### RC2. New timing test: Digital collapsed while promotions were rising, not after they were cut
- Nike Brand Digital growth (REPO, 10-Qs): Q1 FY24 +2%, Q2 FY24 +1%, Q3 FY24 -4%, **Q1 FY25 -20%, Q2 FY25 -21%**, Q3 FY25 -15%.
- **Q1 FY25 call (Oct 1, 2024, OPENED), Friend:** "Traffic declines across NIKE Direct were more significant than we anticipated ... particular softness in traffic on NIKE Digital", with marketplace inventories "requiring higher levels of promotional activity in Q1 to drive conversion." On the classics: "we have taken the most aggressive actions in NIKE Direct and especially Digital. In Q1, these franchises were down nearly 50% versus the prior year on NIKE Digital while we saw much better sales trends in wholesale."
- **Q2 FY25 call (Dec 19, 2024, OPENED), Friend:** "on NIKE Digital, our off-price mix was up high single digits versus the prior year, with performance marketing increasing over the same period."
- **Q3 FY25 call (Mar 20, 2025, OPENED), Hill:** the North America "over 30 promotional days to zero" comparison is January and February 2025, i.e. *after* the two -20% quarters.
- **Earlier warning, Q1 FY24 (Sept 2023) and Q2 FY24 (Dec 21, 2023) calls (OPENED):** consumers "shifted from our digital to physical channels"; "softness in digital traffic and higher levels of promotional activity across the marketplace"; and in response, "we are stepping up our plans to reduce marketplace supply of our key franchises." Traffic softened first, then promotions rose, then Nike pulled the classics.
- **Reading:** the first and largest leg of the Digital decline happened while discounting on Digital was *increasing*. More discounting did not hold revenue, and the decline coincided with a deliberate ~50% cut of classics on Digital. That locates the cause in (1) the classics pull and (2) a traffic loss that preceded the promotional surge. Promotion removal explains at most part of the H2 FY25 and FY26 legs, and in North America that revenue reappeared in wholesale (NA wholesale +14%, NA footwear units +6% in FY26, REPO). The investigator's "$0.5B to $1.0B net of promotion-dependent Digital revenue" should mostly move to `franchise_oversupply.md` and `digital_tech.md`.

### RC3. The sub-$100 exit was a distribution decision, not a pricing decision
- Friend's "several billion dollars' worth of revenue that we walked away from" (Q1 FY25, OPENED) refers to the "core" below-$100 segment, and in the same answer he says "our partners are very excited about the new product that's coming in this dimension." The sub-$100 business sits mainly in family and value wholesale doors.
- Those are the doors CDA cut: DSW, Shoe Show, Dunham's, Big 5 and others in 2021, after Belk, Dillard's and others in 2020 (REPO, `dtc_wholesale.md`). DSW and Macy's returned from October 2023, and the Q1 FY27 rebuild of the $65 to $85 "Family Footwear" line runs through the same partners (investigator's section 3.1).
- **Reading:** the price-architecture gap that the investigator counts as an *independent* pricing element is the downstream product consequence of the CDA channel choice (fewer value doors, a Digital assortment built around $100-plus classics and launches). It belongs with the CDA cause.

### RC4. Peer natural experiment: the same pricing and discount pattern, opposite outcomes
- adidas took "broad-based price increases" in 2022 and then ran heavy promotions (Q4 2022 gross margin 39.1%); Greater China revenue fell 36% in 2022 with "significant inventory takebacks" (FY2022 release, OPENED). Gulden: "We need to reduce inventories and lower discounts."
- By 2025, adidas brand revenue grew 10% currency-neutral with growth in Europe (+10%), North America (+10%) and **Greater China (+13%)**, "broad-based ... in both the wholesale and direct-to-consumer (DTC) business", and gross margin of 51.6% (adidas FY2025 results and investor call, OPENED, adidas IR PDFs).
- **Reading:** if heavy discounting durably trained consumers to wait, adidas, which discounted and took back inventory in the same years and in the same Chinese market, should not have recovered full-price growth within two years. It did, when its product (Terrace, running-look) was in demand. Greater China is where the investigator thinks the "trained to wait" mechanism fits best, yet a peer recovered there under the same industry discount levels. That points the China damage at Nike-specific product and brand heat (`china.md`, `challengers_taste.md`), with discounting as the visible symptom management names.

### RC5. Alternative chain that fits the same data better
1. **Upstream (2020 to 2022):** CDA plus COVID. Digital targets and scarcity-era demand led Nike to scale classics on Digital and cut value doors; freight and input inflation led to industry-wide price increases.
2. **Shock:** the 2022 bullwhip glut (inventory +44%) forced the FY23 liquidation wave; adidas and others did the same.
3. **Demand turn (FY24):** taste rotated away from court classics; Digital traffic softened from mid-2023; Nike stepped up supply cuts (Dec 2023).
4. **Symptom:** retailers and Nike Digital discounted the classics (44% at eight chains, early 2024; Digital 50/50); off-price mix rose in H1 FY25 *while* Digital fell 20% a quarter.
5. **Unwind (FY25 to FY26):** promotions removed; in North America volume moved to wholesale and units grew; in EMEA and China, where newness and brand heat were weaker, removing promotions exposed the demand gap.

Every prediction the pricing hypothesis gets right (margin hit, ASP drop, discount depth, Digital localisation) is also predicted by this chain. The predictions only the pricing hypothesis makes (durable waiting, falling perceived value, high-price products suffering most, peers who discounted failing to recover) all fail.

### RC6. Quantification under this lens
- Mechanism (non-additive, same as investigator): about $1.5B to $2.5B, of which the FY25 ASP drag (-$1.0B footwear) and 180 bps margin hit are the solid parts.
- Re-allocation: the Digital "promotion-dependent revenue" component goes mostly to the classics pull and traffic loss (RC2); the price-architecture component goes to CDA account cuts (RC3); list-price increases above inflation are largely cost pass-through matched by peers (RC1).
- **Independent residual: about 0% to 5% (0 to about $0.25B)**, mainly keeping FY24 full-price ASP after freight normalised and the EMEA promotional relapse in Q3 FY26.

### RC7. Weaknesses of this challenge
- Nike does not disclose classics' share of Digital, so I cannot split the H1 FY25 Digital decline exactly between the classics pull, traffic loss and discount effects.
- The adidas comparison is brand-level; adidas's China recovery also had local-sourcing and product changes, so it shows discounting was survivable, not that it was harmless.
- No new web sources: the search budget was used up before this pass, so I relied on primary filings and transcripts already downloaded.

### Sources added in this challenge
| Source | Date | Status |
|---|---|---|
| Nike FY2022 10-K and FY2023 10-K, gross margin and Overview sections (EDGAR links above) | 2022-07-21, 2023-07-20 | OPENED |
| Nike official call transcripts Q1 FY24, Q2 FY24, Q1 FY25, Q2 FY25, Q3 FY25 (Nike IR PDFs) | 2023-09-28 to 2025-03-20 | OPENED (full text) |
| `data/nike_filing_facts.csv`, `digital_sales_growth_pct` Q1 FY24 to Q3 FY25 (10-Qs) | various | REPO |
| Deckers Brands FY2024 10-K, accession 0000910521-24-000017 (HOKA +27.9%, selective price increases) | 2024-05-24 | OPENED |
| adidas FY2022 results release (price increases, Q4 2022 discounting, Greater China -36%) | 2023-03-08 | OPENED |
| adidas FY2025 results release and investor call (brand +10% c.n., Greater China +13%, gross margin 51.6%) | 2026-03 | OPENED |
| `dtc_wholesale.md` (account cuts 2020 to 2021, DSW return Oct 2023) | 2026-10-13 | REPO |
