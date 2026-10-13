# Root cause test: do tariffs, freight and sourcing costs explain Nike's margin and earnings decline (and do they explain revenue at all)?

Research date: 2026-10-13. Hypothesis under test: *Tariffs, freight, and sourcing costs explain the margin and earnings decline. Test whether they explain revenue at all.*

Status labels (same convention as the companion notes):
- **REPO**: verified number already in `data/nike_filing_facts.csv` or `research_notes/04_financial_data_pack.md` (filing and printed page given there).
- **REPO-NOTE**: taken from an earlier repo note, with the status that note recorded.
- **OPENED**: I read the document myself in this session. This includes Nike 10-K text files (FY2019 to FY2026) and Nike official earnings call transcripts (Q1 FY21 to Q1 FY27, investors.nike.com "webcast_transcript" PDFs converted to text) already downloaded to the session scratchpad by earlier workflow steps, plus the Q2 FY2026 and Q3 FY2026 10-Qs I downloaded from sec.gov in this step.
- **SNIPPET**: seen only in a search-result summary. Treat as a lead.

All arithmetic is mine and labelled. "FY" is Nike's fiscal year ending May 31. No em-dashes are used in this note.

---

## 1. Bottom line

**Verdict: minor contributor to the overall decline; zero contribution to revenue; a real but temporary and mostly refunded hit to FY2026 gross margin. The hypothesis as stated is falsified.**

1. **Tariffs explain none of the FY2025 collapse.** FY2025 is where most of the damage happened (EBIT -$2,761M of the -$3,675M FY24 to FY26 decline, excluding the tariff refund). In FY2025 Nike's own gross margin bridge shows *lower* product costs (+80 bps) and *lower* warehousing and logistics costs (+20 bps). The 190 bps margin drop came from lower ASP (-180 bps, "higher discounts and changes in channel mix") and higher other costs (-90 bps, "including higher inventory obsolescence reserves") (FY25 10-K p. 35, REPO). Costs were a tailwind while margin fell.
2. **Tariffs were the largest single gross margin driver in FY2026, but were mostly refunded.** Two independent estimates put the FY2026 gross incremental tariff cost at about **$1.07B to $1.14B** (230 bps of revenue by the 10-K bridge; sum of quarterly 10-Q product cost lines). Nike booked a **$986M** IEEPA recovery in Q4 FY2026 that "largely offset" it (FY26 10-K, OPENED). Net of the refund, the FY2026 tariff cost was roughly **$0.1B to $0.2B** (my arithmetic).
3. **Tariffs explain none of the revenue decline.** The only tariff-exposed segment, North America, is where revenue held up best (FY26 +4.8% while tariffs were at their peak). Revenue outside North America fell 13.6% FY24 to FY26 versus -4.1% in North America; North America is only 18% of the revenue decline. The decline began in Q1 FY2025 (Jun to Aug 2024), about eight months before the first 2025 tariffs.
4. **Peers with the same or worse exposure did fine.** On (90% of footwear made in Vietnam, about half of sales in the US) raised gross margin from 60.6% to 62.8% and grew 30% in 2025. Deckers (Vietnam and Indonesia) held gross margin at 57.7% (-20 bps) on +10% revenue. adidas lifted gross margin 0.8pp to 51.6% despite a US tariff hit of about EUR 120M. Puma's margin fell 270 bps, but Puma itself attributes this "mainly" to write-downs and promotions, and says tariffs hurt less than expected.
5. **Removing tariffs does not restore earnings.** Tariffs stop being a year-over-year headwind after Q1 FY2027 (management, Q3 FY26 call), and Q1 FY2027's product costs were already a +10 bps tailwind with logistics +90 bps. Yet Nike guides FY2027 revenue down high-single digits and adjusted EPS to $1.15 to $1.35, about 21% below FY2026's $1.58 ex-refund (my arithmetic, midpoint). The earnings decline continues with tariffs neutral.
6. **Freight** was a FY2022 to FY2023 story (about 200 bps cumulative, per CFO Friend), during which revenue *grew* (+5%, +10%). Freight relief added margin in FY2024 and logistics has been a tailwind every year since. **Sourcing disruption** (Vietnam COVID closures, about 130M units cancelled) cut FY2022 revenue growth, not the FY2025 to FY2027 decline.

**Is it a symptom?** The tariff itself is exogenous policy. But how much it hurt is partly a symptom of weak brand heat. Nike's "surgical" price rises were cancelled out by discounts (FY26 ASP had a net 0 bps effect in the 10-K bridge; H1 FY26 ASP -150 bps), while On, Deckers and adidas passed through price or absorbed costs from much higher margins. Nike also entered the tariff period with a gross margin already 380 bps lower for non-tariff reasons (inventory clean-up, discounting).

**Fixable by management: partly.** The policy is outside Nike's control. The IEEPA portion was refunded. The rest is being mitigated (China share of US footwear imports cut from about 16% toward high single digits, cost sharing with suppliers and retailers, pricing, Pace supply chain savings). Management can fix the pass-through problem only by restoring full-price demand, which is the upstream cause covered in the companion notes.

---

## 2. Predictions table

| # | Prediction if the hypothesis is true | Test and result | Held? |
|---|---|---|---|
| P1 | **Timing.** Margin and earnings decline should start when new tariffs or freight spikes hit (tariffs: Feb to Apr 2025; Red Sea freight spike: 2024). | Revenue decline began Q1 FY25 (Jun to Aug 2024, -10%, REPO). Margin decline began Q2 FY25 (Sep to Nov 2024, 43.6% vs 44.6%, REPO). First new tariffs (China and Mexico IEEPA) landed in Q4 FY25, and Q4 FY25's 440 bps margin drop was explained as "higher wholesale discounts, higher discounts in our NIKE Factory Stores, supply chain cost deleverage and channel mix headwinds" with no mention of tariffs (Q4 FY25 call, OPENED). FY25 bridge: product costs +80 bps, logistics +20 bps (FY25 10-K p. 35, REPO). | **No.** The decline predates tariffs by 8 months and the cost lines were tailwinds in FY25. |
| P2 | **Bridge.** In Nike's own gross margin bridge, tariff, freight and product cost lines should be the dominant negatives across the decline. | FY25: biggest negatives are ASP (-180 bps) and other costs/obsolescence (-90 bps); product costs +80, logistics +20 (REPO). FY26 (reported): product costs -20 bps *including* the +210 bps refund, so about -230 bps ex-refund; logistics +20, FX +20, other +20, Converse -20 (FY26 10-K p. 34, REPO; FY26 refund bps from Q4 FY26 call, OPENED). Quarterly FY26 product cost lines "primarily due to higher tariffs": Q1 -100, Q2 -360, Q3 -270 bps (10-Qs, REPO). | **Partly.** True for FY26 only (ex-refund). False for FY25. Across FY24 to FY26 ex-refund (-380 bps), tariffs are about 230 bps, all in FY26, and mostly refunded. |
| P3 | **Geography.** US tariffs only hit goods imported into the US, so the margin and EBIT damage should be concentrated in North America (and US-sold Converse), and revenue damage, if any, there too. | Tariff language appears only in the North America segment discussion: Q2 FY26 NA "Gross margin contraction of 330 basis points, primarily due to new tariffs"; Q3 FY26 NA "350 basis points, primarily due to higher tariffs" (10-Qs, OPENED). Other segments cite discounts, FX and obsolescence. Refund: $965M NA, $21M Converse (FY26 10-K, OPENED). But EBIT fell in every segment: FY24 to FY26 NA -1,411 ex-refund, EMEA -971, Greater China -1,031, APLA -498, Converse -456 (REPO, my arithmetic). About $2.96B of segment EBIT loss is outside North America, where US tariffs do not apply. Revenue: NA -4.1%, ex-NA -13.6% (my arithmetic). | **Margin: partly (NA only). EBIT and revenue: No.** The pattern is the reverse of what tariffs predict. |
| P4 | **Peers.** Brands with the same Asian sourcing and US exposure should show similar margin and earnings damage. | On: 2025 gross margin 62.8% vs 60.6%, revenue +30%; "approximately 90% ... of our footwear products were produced in Vietnam" (On 20-F FY2025, OPENED). Deckers FY26 (to Mar 2026): GM 57.7% vs 57.9%, "primarily due to incremental tariffs ... partially offset by cost-sharing arrangements, strategic price increases" (Deckers 10-K FY2026, OPENED); production "predominantly from Vietnam and Indonesia". adidas 2025: GM +0.8pp to 51.6%, operating profit +54% "despite the negative impact from higher US tariffs" (adidas FY2025 release, OPENED); US tariff hit about EUR 120M (FashionUnited, Oct 29, 2025, OPENED). Puma 2025: GM -270 bps to 45.0%, "mainly due to higher inventory write-downs and increased promotional activities"; tariffs "a burden" (Puma Annual Report 2025, OPENED). | **No.** Same-exposure peers held or grew margins. The one peer whose margin fell blames the same thing Nike does: discounts and write-downs. |
| P5 | **Earnings recover when tariffs lift.** If tariffs explain the earnings decline, removing them (IEEPA struck Feb 20, 2026; YoY headwind ends after Q1 FY27) should bring earnings back. | Q1 FY27: product costs +10 bps, logistics +90 bps, no tariff line in the bridge (Q1 FY27 10-Q p. 23, REPO); zero mentions of "tariff" on the Q1 FY27 call (OPENED). Yet Q1 FY27 revenue -4%, EPS $0.48 vs $0.49 (REPO), and FY27 guidance is revenue down high-single digits, adjusted EPS $1.15 to $1.35 vs $1.58 ex-refund in FY26 (REPO). CFO Denton: EBIT to "decline by a greater percentage than revenue" due to "fixed cost deleverage associated with lower revenue levels, higher input costs" (Q1 FY27 call, OPENED). | **No.** Earnings keep falling with tariffs neutral. |
| P6 | **Revenue via price elasticity.** If tariffs explain revenue, Nike's price increases should cut US units and revenue; the US should underperform. | Nike's "surgical price increase in the United States with phased implementation beginning in fall '25" (Q4 FY25 call, OPENED); $5 to $10 on select footwear (SGB Media, OPENED, citing the class action complaint). US footwear CPI rose only +1.1% to +1.5% YoY Aug 2025 to Feb 2026 (BLS CUUR0000SEAE via FRED, OPENED). NA revenue rose 4.8% in FY26 (REPO). Q2 FY26 currency-neutral revenue "grew 6% excluding" the classics reduction (Q2 FY26 call, OPENED). | **No.** The tariff-exposed region grew while prices rose. |
| P7 | **Revenue via China retaliation or nationalism.** If the 2025 trade war drove the China decline, it should start in 2025 and hit US brands but not others. | Greater China decline began Q1 FY25 (Jun to Aug 2024, -3% c-n, REPO), before the 2025 trade war. American brand lululemon grew mainland China +29% (FY2025) and adidas Greater China +13% c-n in 2025 (china.md, REPO-NOTE). | **No.** |
| P8 | **Freight.** Freight spikes should line up with the margin and revenue decline. | Freight cost about 100 bps in FY22 and another 100 bps in FY23, "about a 200 basis point impact on a two-year basis" (CFO Friend, Q4 FY22 call, OPENED), "paying about five times the rate that we paid pre-pandemic." Recaptured from Q2 FY24 (Q2 FY24 call, OPENED). During the freight years revenue grew: FY22 +5%, FY23 +10% (REPO). Logistics a tailwind in FY25 (+20), FY26 (+20), Q1 FY27 (+90 bps) (REPO). | **No** for the decline window. Freight explains part of the FY23 dip (46.0% to 43.5%) and the FY24 rebound. |
| P9 | **Sourcing disruption.** Supply shocks should coincide with lost revenue in the decline window. | Vietnam COVID closures: "10 weeks of production already lost in Vietnam since mid-July" (Q1 FY22 call, OPENED); "cancel production of roughly 130 million units" (Q2 FY22 call, OPENED). FY22 revenue guidance cut from low-double-digit to mid-single-digit growth. Sourcing mix in the decline years was stable: footwear Vietnam/Indonesia/China 50/27/18% (FY24), 51/28/17% (FY25), 52/27/16% (FY26) (10-Ks, OPENED). | **No** for FY25 to FY27. Yes for FY22, a growth year. |
| P10 | **Market reaction.** If tariffs were the main problem, the stock should fall mainly on tariff news and recover when they are lifted. | 62% of the log decline from the Nov 5, 2021 peak ($177.51) to Oct 12, 2026 ($35.35) happened before Apr 2, 2025 (my arithmetic on `data/nke_daily_prices.csv`, REPO). Tariff days: Apr 3, 2025 -14.4%; Apr 9 +11.4% (pause); Apr 10 -8.3%; May 12 +7.3% (US-China truce). Apr 2 ($64.96) to May 12 ($62.58): -3.7% net. Supreme Court ruling Feb 20, 2026: -0.3%, next day -3.5%. Since the ruling the stock fell from $65.40 to $35.35. Largest drops were earnings days: Jun 28, 2024 -20.0%; Dec 19, 2025 -10.5%; Apr 1, 2026 -15.5%. | **No.** |

---

## 3. Evidence detail

### 3.1 Nike's gross margin bridge, FY2022 to Q1 FY2027 (all REPO unless marked)

| Period | GM % | Change | Product costs | Warehousing/logistics | ASP | Other costs | FX | Source |
|---|---|---|---|---|---|---|---|---|
| FY2022 | 46.0 | +120 | negative ("elevated freight and logistics costs") | in product costs | n/a | negative (China obsolescence) | positive | FY22 10-K (OPENED) |
| FY2023 | 43.5 | -250 | negative ("higher input costs and elevated inbound freight and logistics costs") | in product costs | positive (full-price ASP) | positive | negative | FY23 10-K (OPENED) |
| FY2024 | 44.6 | +110 | +10 ("lower ocean freight rates and logistics costs largely offset by higher product input costs") | in product costs | +200 (full-price ASP) | +10 | -40 | FY24 10-K p. 36 |
| FY2025 | 42.7 | -190 | **+80** | **+20** | **-180** | **-90** (obsolescence) | -10 | FY25 10-K p. 35 |
| FY2026 | 42.9 | +20 | -20 (incl. about +210 refund) | +20 | not listed | +20 | +20 | FY26 10-K p. 34 |
| FY2026 ex-refund | 40.8 | -190 | about -230 | +20 | not listed | +20 | +20 | Q4 FY26 call (OPENED); my arithmetic |
| Q1 FY2026 | 42.2 | -320 | -100 ("primarily due to higher tariffs") | +50 | -250 | n/a | +30 | Q1 FY26 10-Q p. 22 |
| Q2 FY2026 | 40.6 | -300 | -360 ("primarily due to higher tariffs") | +50 | -50 | +40 | +40 | Q2 FY26 10-Q p. 27 |
| Q3 FY2026 | 40.2 | -130 | -270 ("primarily due to higher tariffs") | +20 | +80 | +60 | +10 | Q3 FY26 10-Q p. 30 |
| Q4 FY2026 | 49.2 (40.2 ex-refund) | +890 (-10 ex) | refund +900; tariffs guided -250 | n/a | n/a | n/a | n/a | Q4 FY26 release p. 1; Q3 FY26 call guidance (OPENED) |
| Q1 FY2027 | 42.8 | +60 | **+10** | **+90** | -30 | -40 (royalties) | +40 | Q1 FY27 10-Q p. 23 |

Reading the table: costs were a margin *tailwind* in FY2024, FY2025 and Q1 FY2027. The only year with a cost-driven margin hit inside the decline window is FY2026, and Q1 FY2027 shows the hit has already passed.

### 3.2 Sizing the FY2026 tariff cost (two methods)

- **Method A (10-K bridge):** FY26 product costs -20 bps including the refund. Refund = 210 bps (Matt Friend: "Gross margin was 42.9% ... including a 210 basis point benefit related to recovery of IEEPA tariffs. Excluding the benefit, gross margin would have been 40.8%", Q4 FY26 call, OPENED). So ex-refund product costs about -230 bps x $46,398M = **about $1.07B**. This line also includes any non-tariff product cost change (FY25 was +80 bps favorable), so the pure tariff figure could be somewhat higher.
- **Method B (quarterly lines):** Q1 -100 bps x $11,720M = $117M; Q2 -360 x $12,427M = $447M; Q3 -270 x $11,279M = $305M; Q4 guided tariff impact of 250 bps x $10,972M = $274M. Total **about $1.14B** (my arithmetic).
- **Management estimates:** "gross incremental cost increase to NIKE of approximately $1 billion" (Q4 FY25 call, Jun 26, 2025, OPENED), raised to "approximately $1.5 billion" annualized (Q1 FY26 call, Sept 30, 2025, OPENED; Q1 FY26 10-Q p. 19, REPO), "a gross headwind of approximately 320 basis points to gross margin in fiscal '26" (Q2 FY26 call, Dec 18, 2025, OPENED). Net of mitigation: "approximately 75 basis points", raised to "120 basis points to gross margin" for FY26 (Q4 FY25 and Q1 FY26 calls, OPENED).
- **North America intensity:** NA gross margin "only declined 330 basis points ... despite 520 basis points of impact from new U.S. tariffs" (Q2 FY26 call, OPENED); "declined 360 basis points ... despite nearly 650 basis points of gross impact" (Q3 FY26 call, OPENED). Management's own reading: underlying NA margin was *improving* by 190 to 290 bps once tariffs are removed.
- **Refund:** $986M booked in Q4 FY26, "largely offsetting the impact of the IEEPA tariffs recognized during fiscal 2026"; $302M received by May 31, 2026, the rest received in Q1 FY27 (FY26 10-K, OPENED; Q1 FY27 10-Q, OPENED via scratchpad copy). As of Apr 1, 2026, "Total IEEPA tariffs paid ... is approximately $1.0 billion" (Q3 FY26 10-Q p. 26, REPO).
- **Conclusion:** gross FY26 incremental tariffs about $1.07B to $1.14B (management's $1.5B annualized figure is the upper bound). Net after the refund, about $0.1B to $0.2B. Remaining tariffs after the ruling: Nike's FY27 forecast assumes "incremental tariff rates of 10% continuing through the end of July and then increasing to 15% thereafter" (Q4 FY26 call, OPENED).

### 3.3 EBIT and EPS decomposition, FY2024 to FY2026 (my arithmetic on REPO numbers)

- EBIT: FY24 $6,539M, FY25 $3,778M, FY26 $3,850M reported, **$2,864M ex-refund**. Decline FY24 to FY26 ex-refund: **$3,675M**, of which FY24 to FY25 $2,761M (tariffs about $0) and FY25 to FY26 $914M.
- Gross profit fell $3,962M (FY24 $22,887M to FY26 ex-refund $18,925M). Volume effect (lost revenue at the FY24 44.6% margin): about $2,212M. Margin-rate effect: about $1,750M. Operating expenses (gross profit minus EBIT) fell $287M, a small offset.
- Tariffs (about $1.1B gross) are therefore about 60% of the FY26 rate effect but **0% of the volume effect**, and about **24% to 33%** of the ex-refund EBIT decline (range 24% at $0.9B to 41% at management's $1.5B annualized upper bound).
- On the reported basis (refund counted), the net tariff cost of about $0.1B to $0.2B is **about 4% to 7%** of the reported EBIT decline of $2,689M.
- EPS: FY24 $3.73 to FY26 $1.58 ex-refund (-$2.15, Q4 FY26 call, OPENED). Nike valued the $986M refund at $0.52 per share (REPO), so about $1.1B gross tariffs equals about $0.58, or about 27% of the ex-refund EPS decline. Reported EPS fell $1.63 (to $2.10); net tariff effect after the refund is about $0.05 to $0.10 (my arithmetic).
- In FY2026 alone (ex-refund), EBIT fell $914M while gross tariffs were about $1.1B, so **without tariffs FY26 EBIT would have risen slightly**. Management said the same: Q4 FY26 margin "excluding the tariff benefit were down 10 basis points" and FY26 was "stabilizing gross margins, excluding the impact of incremental tariffs" (Q4 FY26 call, OPENED). This is the strongest evidence *for* the hypothesis, and it is limited to one year.

### 3.4 Revenue: no link

- Segment revenue FY24 to FY26 (REPO): North America $21,396M to $20,511M (-4.1%); outside NA $29,966M to $25,887M (-13.6%). NA is 18% of the $4,964M decline.
- NA FY24 to FY25 (no tariffs): -8.5%. NA FY25 to FY26 (peak tariffs, price increases): +4.8%. The tariff-exposed segment grew in the tariff year.
- Revenue explanations in the 10-Qs and calls are classics franchise reduction ("reducing classic footwear franchises by more than $2 billion", Q4 FY26 call, OPENED), digital reset, China and Converse. None cite tariffs as a revenue driver.
- FY27 guidance (revenue down high-single digits) is given when tariffs are no longer a YoY headwind.
- Only indirect revenue channel found: prices went up $5 to $10 on select US items from June 1, 2025 (SGB Media summary of the class action complaint, OPENED). With NA revenue up in FY26 and US footwear CPI up only about 1% to 1.5% YoY through Feb 2026, any elasticity effect is too small to detect.

### 3.5 Freight and sourcing history

- FY22: "roughly 100 basis points of additional transportation, logistics, and air freight costs" (Q1 FY22 call, OPENED). FY23: "a second straight year of more than 100 basis points of headwinds from elevated freight and logistics costs" (Q1 FY23 call, OPENED). Cumulative "350 basis points of transitory cost headwinds ... between elevated ocean freight and logistics and then the promotions" (Q3 FY23 call, OPENED).
- Recovery: FY24 gross margin "increased 110 basis points ... primarily due to strategic pricing actions and lower ocean freight rates and logistics costs" (FY24 10-K, OPENED).
- Vietnam 2021: "80% of our footwear factories located in the south and nearly half of our apparel factories in Vietnam are currently closed" (Q1 FY22 call, Sept 23, 2021, OPENED). This was a revenue *supply* shock in a strong demand year.
- Sourcing response to tariffs: "China represents roughly 16% of the footwear we import into the United States, and we expect this to reduce to the high single-digit range by the end of fiscal '26" (Q4 FY25 call, OPENED). Nike's US footwear duty base before 2025 was already "in the mid-teens range" (same call).
- Forward risk: FY27 commentary cites "higher input costs" and "oil prices" (Q1 FY27 and Q4 FY26 calls, OPENED). Deckers guides FY27 gross margin to 56.5% on higher freight and input costs (SNIPPET). This is an industry-wide cost, and Nike's FY27 earnings decline is guided mostly as volume deleverage.

### 3.6 Why tariffs hurt Nike's margin more than peers' (the symptom question)

- **Thin cushion:** Nike gross margin 42.7% (FY25) before tariffs vs adidas 50.8% (2024), Deckers 57.9% (FY25), On 60.6% (2024). A similar dollar duty takes more basis points from a lower-margin, discount-heavy mix.
- **No pricing power during the reset:** Nike raised US prices, but FY26 ASP had no net effect in the 10-K bridge, and H1 FY26 ASP was -150 bps "primarily due to ... higher discounts" (REPO). Deckers explicitly offset tariffs with "cost-sharing arrangements, strategic price increases, and favorable product mix" (Deckers FY26 10-K, OPENED). adidas raised prices "selectively" (FashionUnited, OPENED) and still expanded margin.
- **US weighting is not the explanation:** On's US share (about half of sales, SNIPPET for the 9-month 2025 figure) is higher than Nike's NA share (44% in FY26, REPO), and On's sourcing is more concentrated (90% Vietnam). On's margin still rose 220 bps.
- **Inference:** the tariff is exogenous, but the size of its margin damage is amplified by the same upstream problem driving revenue: weak full-price demand and a marketplace being cleaned up with discounts.

---

## 4. Quantitative estimate

| Measure | Total decline | Tariff, freight, sourcing contribution | Share |
|---|---|---|---|
| Revenue FY24 to FY26 | -$4,964M | about $0 | **about 0%** |
| Revenue FY27 guide (high-single-digit decline) | n/a | about $0 (tariffs neutral YoY after Q1) | **about 0%** |
| Gross margin FY24 to FY26, reported | -170 bps | net about -20 to -40 bps after refund | **about 10% to 25%** |
| Gross margin FY24 to FY26, ex-refund | -380 bps | about -230 bps gross tariffs (all FY26); freight/logistics +40 bps favorable | **about 50% to 60%** (FY26 only; 0% of FY25) |
| EBIT FY24 to FY26, reported | -$2,689M | net about $0.1B to $0.2B | **about 4% to 7%** |
| EBIT FY24 to FY26, ex-refund | -$3,675M | about $0.9B to $1.5B gross | **about 24% to 41%, central about 30%** |
| EPS FY24 to FY26, ex-refund | -$2.15 | about $0.49 to $0.81 | **about 25% to 35%** |
| FY27 earnings decline (guide) | adj. EPS about -21% vs $1.58 | tariffs neutral YoY after Q1; input costs and oil a small new headwind | **small** |

Honest central estimate: **tariffs and costs explain none of the revenue decline, none of the FY2025 margin and earnings collapse, about 30% of the ex-refund FY24 to FY26 EBIT decline (all of it in FY2026), and about 5% of the reported decline after the IEEPA refund.** Freight and sourcing contributed nothing net in the decline window (they were tailwinds).

---

## 5. Strongest evidence for and against

**For (narrow version: tariffs hurt FY2026 margins):**
1. FY26 quarterly 10-Q product cost lines of -100, -360 and -270 bps "primarily due to higher tariffs" (REPO).
2. NA gross margin absorbed 520 to 650 bps of gross tariff impact in Q2 and Q3 FY26 (calls, OPENED).
3. Ex-refund FY26 gross margin of 40.8% is the lowest in the series, and FY26 ex-refund EBIT would have risen without tariffs.
4. Gross FY26 tariff cost (about $1.1B) is close to the $1.0B Nike paid and the $986M refunded, a consistent picture.

**Against (the hypothesis as stated):**
1. FY25 margin bridge: product costs +80 bps and logistics +20 bps while margin fell 190 bps on discounts and obsolescence (FY25 10-K p. 35).
2. Revenue decline started Q1 FY25, eight months before the first 2025 tariffs; NA, the only tariff-exposed segment, grew 4.8% in the tariff year while ex-NA fell.
3. About $2.96B of FY24 to FY26 segment EBIT loss is in segments with no US tariff exposure.
4. On, Deckers and adidas, with similar or more concentrated Vietnam sourcing and big US exposure, held or raised gross margins in 2025 to FY26.
5. $986M of tariffs were refunded, and Q1 FY27 shows product costs and logistics as tailwinds, yet FY27 EPS is guided about 21% lower.
6. The stock had already lost 62% of its log decline before Liberation Day, shrugged off the Supreme Court ruling, and its biggest falls were earnings days.

---

## 6. Sources

| Source | Date | Status | Used for |
|---|---|---|---|
| Nike FY2022 10-K (sec.gov, scratchpad text) | 2022-07-21 | OPENED | FY22 margin bridge, freight |
| Nike FY2023 10-K | 2023-07-20 | OPENED | FY23 margin bridge, input and freight costs |
| Nike FY2024 10-K | 2024-07-25 | OPENED | FY24 bridge (p. 36), sourcing shares |
| Nike FY2025 10-K | 2025-07-17 | OPENED | FY25 bridge (p. 35), sourcing shares |
| Nike FY2026 10-K | 2026-07-15 | OPENED | FY26 bridge (p. 34), IEEPA recovery, sourcing shares |
| Nike Q2 FY2026 10-Q (nke-20251130.htm, downloaded this step) | 2025-12-30 | OPENED | NA segment margin "primarily due to new tariffs"; other segments' drivers |
| Nike Q3 FY2026 10-Q (nke-20260228.htm, downloaded this step) | 2026-04-01 | OPENED | NA "primarily due to higher tariffs"; Converse reset costs |
| Nike Q1 FY2026, Q1 FY2027 10-Qs; Q4 FY2026 and Q1 FY2027 releases | 2025-10-01 to 2026-10-02 | REPO | quarterly bridges, $1.5B estimate, $986M refund, FY27 guidance |
| `data/nike_filing_facts.csv`, `research_notes/04_financial_data_pack.md` | 2026-10-12 | REPO | all revenue, GM, EBIT, EPS, segment figures; gm_driver_* rows |
| `data/nke_daily_prices.csv` (Yahoo Finance) | through 2026-10-12 | REPO | stock event study |
| Nike earnings call transcripts Q1 FY22, Q2 FY22, Q3 FY22, Q4 FY22, Q1 FY23, Q2 FY23, Q3 FY23, Q4 FY23, Q1 FY24, Q2 FY24, Q3 FY24, Q4 FY24, Q1 FY25, Q3 FY25, Q4 FY25, Q1 FY26, Q2 FY26, Q3 FY26, Q4 FY26, Q1 FY27 (investors.nike.com PDFs, scratchpad text) | 2021-09-23 to 2026-10-01 | OPENED | freight bps, Vietnam closures, tariff estimates, NA tariff bps, refund bps, ex-refund margin and EPS, FY27 commentary |
| BLS CPI Footwear, CUUR0000SEAE (FRED CSV, scratchpad) | through Aug 2026 | OPENED | US footwear price inflation |
| On Holding 20-F FY2025 (sec.gov, scratchpad text) | 2026 (FY ended 2025-12-31) | OPENED | 90% Vietnam footwear; GM 62.8% vs 60.6%; sales +30% |
| On Holding 6-K Q2 and Q3 2025 MD&A (sec.gov) | 2025-08 and 2025-11 | SNIPPET | US about 51% of 9M 2025 sales; guidance includes July 31, 2025 reciprocal tariffs |
| Deckers 10-K FY2026 (sec.gov, scratchpad text) | 2026-05 | OPENED | GM 57.7% vs 57.9% and drivers; Vietnam and Indonesia sourcing |
| Deckers FY26 call coverage (fool.com, tikr.com, quartr.com) | 2025-08 to 2026-05 | SNIPPET | tariffs about 80 bps; unmitigated about $110M, net about $25M; FY27 GM guide 56.5% |
| adidas FY2025 results release and investor call slides (adidas-group.com PDFs, scratchpad text) | 2026-03-04 | OPENED | GM 51.6%, operating profit +54% "despite ... higher US tariffs"; 2026 tariff and FX headwind about EUR 400M |
| adidas Q2 2026 results release (scratchpad text) | 2026-07 | OPENED | H1 2026 GM 51.8%; tariff refunds of US$250M to 300M not in guidance |
| FashionUnited, "Bjorn Gulden details Adidas's turnaround amidst tariff headwinds" | 2025-10-29 (from URL) | OPENED | adidas 2025 tariff hit about EUR 120M (down from EUR 200M); selective US price rises |
| Reuters via AOL, "Adidas sees $140 million hit on operating profit from US tariffs" | 2025-10-29 | SNIPPET (page returned 404) | corroborates EUR 120M |
| Puma Annual Report 2025, results of operations (annual-report.puma.com) | 2026 | OPENED | GM -270 bps to 45.0% "mainly due to higher inventory write-downs and increased promotional activities"; tariffs "a burden" |
| Puma Q2 2025 preliminary release (about.puma.com) | 2025-07 | SNIPPET | about EUR 80M tariff hit to 2025 gross profit; Q2 GM decline mainly promotions and FX |
| CFO Dive, "Nike expects $1.5B in tariff costs this year, CFO says" (scratchpad text) | 2025-10-01 | OPENED | corroborates $1.5B |
| Modern Retail, "Nike ... now expects $1.5B in annualized costs" (scratchpad text) | 2025-10 | OPENED | net headwind raised from 75 to 120 bps |
| SGB Media, "Nike Sued by Customers Seeking Refunds of Tariff Costs" (scratchpad text) | 2026-05 | OPENED | $5 to $10 price increases from June 1, 2025 (per complaint) |
| Sportico, "Nike Sued for Refunds Over Trump's Illegal Tariff Price Hikes" (scratchpad text) | 2026-05 | OPENED | class period Jun 1, 2025 to Feb 24, 2026 |
| Reuters via Yahoo Finance, "Skechers to go private for $9.42 billion" (scratchpad text) | 2025-05-05 | OPENED | context: Skechers' China sourcing exposure and tariff-driven forecast withdrawal |
| Companion notes: china.md, macro_covid_cycle.md, franchise_oversupply.md | 2026-10-13 | REPO-NOTE | China timing, lululemon and adidas China growth, peer revenue growth |
