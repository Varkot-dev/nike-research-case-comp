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
