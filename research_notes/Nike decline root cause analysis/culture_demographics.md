# Root cause test: are cultural and demographic shifts (Gen Z perception, sneakerhead and resale decline, basketball relevance, logo fatigue, athlete losses) a driver of Nike's decline?

Research date: 2026-10-13. Hypothesis under test: *Cultural and demographic shifts (Gen Z brand perception, decline of sneakerhead and resale culture, basketball culture losing relevance, logo fatigue, athlete roster losses like Mbappe) are a driver of Nike's revenue decline.*

Status labels:
- **REPO**: verified number already in `data/nike_filing_facts.csv` or `research_notes/04_financial_data_pack.md` (filing and printed page given there).
- **OPENED (repo)**: opened by an earlier researcher and recorded in an earlier repo note; reused, not re-fetched.
- **OPENED**: I read the document text myself in this session. This includes Nike earnings call transcripts (Q1 FY24 to Q1 FY27) and Piper Sandler "Taking Stock With Teens" infographics (Spring 2022 to Spring 2025) that earlier steps of this workflow had downloaded to the session scratchpad; I re-read their text today.
- **SNIPPET**: seen only in a search-result summary. A lead, not a fact.

All arithmetic is mine and labelled "my arithmetic". Scope for the decline is FY2024 revenue $51,362M to FY2026 $46,398M, a fall of $4,964M (REPO).

---

## 1. Bottom line

**Verdict: symptom of another cause, with a small independent residual. The culture story describes *where* the decline sits (lifestyle, Jordan retro, Converse, teen mindshare) but not *why* it happened.**

The hypothesis bundles five sub-claims. I tested each against timing, category, geography, peer and "same consumer, different supply" natural experiments:

| Sub-claim | Result |
|---|---|
| Gen Z has turned against Nike | **Fails as a cause; holds as a symptom.** Teen footwear mindshare hit a record 61% in Spring and Fall 2023, *after* resale premiums had collapsed and while Dunk was oversupplied. It fell only from 2024, in step with (not ahead of) the revenue decline. Nike is still No. 1 with teens at 46%, more than 3x No. 2, and Gen Z is Nike's *strongest* generation on YouGov consideration. |
| Sneakerhead and resale culture is dying | **Fails as an exogenous cause.** Resale is not shrinking (StockX: about 200 brands set records in 2025; Nike and Jordan are still No. 1 and No. 2 traded sneaker brands). What collapsed is the premium on *oversupplied* Nike and Jordan lines. In the same month (Sept 2026), scarce Nike drops traded at 27% to 56% premiums while six of seven Jordan retros traded below retail. Same culture, same consumer, different supply. |
| Basketball culture is losing relevance | **Fails for the sport; holds only for basketball-derived lifestyle silhouettes.** NBA 2025-26 regular-season viewership rose 16% (league figures); Nike Basketball grew double digits in North America (Q1 FY27); Kobe became "the market's largest signature franchise, with demand far exceeding available supply" (Q2 FY25). The fall is in AJ1, Dunk and AF1 *as fashion*, which is the taste rotation already measured in `challengers_taste.md`. |
| Logo fatigue / "quiet" branding | **Fails.** NIKE Brand apparel, the most logo-dependent category, fell only 2.4% FY24 to FY26 (REPO). Adidas, a loud-logo brand, grew Lifestyle double digits in 2024 and +12% in 2025. Logo-light lululemon *also* fell in the Americas (comps -3% in FY2025). |
| Athlete roster losses (Mbappe) | **Fails on timing and direction.** Mbappe left on Sept 18, 2026, 27 months after the decline began. Nike's endorsement obligations *doubled* from $7.6B (May 2023) to $16.2B (May 2025) (REPO). Nike signed or launched Caitlin Clark and Shai Gilgeous-Alexander signature shoes in Q1 FY27. |

**What survives:** (1) a real, partly exogenous youth fashion rotation away from basketball and court silhouettes toward running-inspired, terrace and Japanese heritage shoes; (2) a market-wide cooling of speculative sneaker buying after COVID scarcity, higher rates and Chinese regulation; (3) weaker teen spending (-6% Spring 2024, -7% Fall 2025). In 2026 the whole lifestyle footwear market softened (Circana; adidas Lifestyle only +2% in Q2 2026), so the culture headwind is real *now* even though it did not start the decline.

**Upstream cause:** the brand-signal erosion was produced mainly by Nike's own supply decisions under Consumer Direct Acceleration (700+ Jordan releases a year in 2022 and 2023, Dunk and AF1 "continuously adding new styles"), consistent with Berger and Heath (2008): a taste is abandoned when the signal spreads too far. Hill said so directly: "we've been oversupplying our iconic retro product, asking them to do too much" (Q1 FY27 call).

**Contribution:** about **5% to 15% of the $4,964M FY24 to FY26 decline (central about 10%, roughly $0.5B)** is attributable to cultural and demographic forces that Nike did not cause. Most of that overlaps with the "regardless of execution" share in `challengers_taste.md` and must not be added to it. The larger share of the culture-*looking* loss (teen mindshare, Jordan premiums) is a symptom of oversupply and is counted in `franchise_oversupply.md`.

**Fixable by management: partly.** Scarcity and product are fixable and Nike has proof inside its own portfolio (scarce drops still sell at premiums; performance basketball growing). The exogenous rotation away from basketball-derived lifestyle silhouettes and the cooler resale market are not fixable on demand.

---

## 2. Predictions and results

| # | Prediction if the hypothesis is true | Result | Held? |
|---|---|---|---|
| P1 Timing (Gen Z) | Gen Z brand perception should deteriorate *before* revenue falls, and at a time when Nike's supply and product were normal | Piper Sandler teen footwear mindshare: 56% (Spring 2021, implied from "+400 bps Y/Y"), 60% (Spring 2022), 60% (Fall 2022), 61% (Spring 2023), 61% (Fall 2023), 59% (Spring 2024), 57% (Fall 2024), 49% (Spring 2025), 46% (Fall 2025). Peak came in 2023, while the AJ1 resale premium had already collapsed to 4% and Dunk was oversupplied. The fall runs concurrently with revenue (Q1 FY25 -10%) and its biggest step (-8 pts) came in Spring 2025, *after* revenue had dropped. | **No** as leading cause. Mindshare is a coincident symptom. |
| P2 Category (basketball) | Basketball should decline across both performance and lifestyle, and the sport's popularity should be falling | Performance basketball grew: "Kobe became the market's largest signature franchise, with demand far exceeding available supply" (Q2 FY25); basketball "up high single digits" (Q3 FY26); "Basketball was up double digits in North America" (Q1 FY27). NBA 2025-26 national regular-season average 1.78M, +16% (Front Office Sports, league data, new Nielsen methodology). Only Jordan *Streetwear* and basketball-derived lifestyle classics fell. | **No** for basketball culture. **Yes** only for basketball-derived *fashion* silhouettes (a taste rotation, see `challengers_taste.md`). |
| P3 Resale culture | If sneakerhead culture is fading, resale should shrink across brands, and even scarce Nike drops should fail | StockX 2025: about 200 brands set annual sales records; Nike and Jordan No. 1 and No. 2 most-traded for the third straight year; Nike +5% and Jordan +6% average prices. H1 2026: Jordan sneaker sales +6%, prices +5%, CEO says Jordan "showing signs of recovery". Needham Sept 2026: 13 high-heat launches (19 a year earlier, 30+ a month in 2021 to 2022), 9 of 13 were Nike, average premium 27%; but six of seven Jordan retros traded at discounts. | **No.** Hype is concentrated on scarce product; the failures are oversupplied lines. Speculative volume has cooled (fewer high-heat launches), which is partly exogenous. |
| P4 Logo fatigue | Logo-heavy categories (apparel, graphic tees, fleece) should fall more than footwear; logo-light brands should gain; loud-logo peers should lose | NIKE Brand apparel -2.4% FY24 to FY26 vs footwear -13.3% (REPO, `challengers_taste.md`). Adidas Lifestyle +double digits (2024), +12% (2025), +2% (Q2 2026). lululemon Americas comps -3% (FY2025). | **No.** |
| P5 Athletes | Athlete losses should precede the decline, and Nike's athlete investment should be falling | Mbappe left Sept 18, 2026 (contract not renewed after July 31). Decline began Q1 FY25 (Jun to Aug 2024). Endorsement obligations: $7.6B (May 2022, May 2023), $10.6B (May 2024), $16.2B (May 2025), $15.5B (May 2026) (REPO). New signature shoes for Caitlin Clark and Shai Gilgeous-Alexander launched Oct 1, 2026. | **No.** Athlete losses are an *effect* of a weaker Nike and a forward risk, not a cause of FY25 to FY26. |
| P6 Peer control (same consumers) | Peers selling to the same Gen Z consumers in lifestyle sneakers should decline too | Adidas Lifestyle grew in 2024 and 2025 (adidas FY results, OPENED). Adidas Originals "strong double-digit growth" (2024). Only in 2026 did the lifestyle footwear market weaken for everyone (adidas Q2 2026: "lifestyle footwear market ... currently under pressure due to heavy discounting"). Vans and Converse (canvas and skate) fell with Nike (`challengers_taste.md`). | **Partly.** Not in FY25 (Nike's worst year). Yes for canvas and skate silhouettes and for the whole lifestyle market in 2026. |
| P7 Geography | Decline should be largest where sneaker and basketball culture is strongest (US) and where Gen Z nationalism is strongest (China), with foreign peers suffering there too | NA fell least (-4.1% FY24 to FY26; NA footwear +5% in FY26). Greater China fell most (-22.5%), but adidas China grew +13% (2025) and +16% (H1 2026), so guochao (a Gen Z cultural shift) does not explain it (`china.md`). Hill: "we've become a lifestyle brand competing on price in China" (Q2 FY26). | **No** for the US. **No** for China as a cultural cause; it is Nike-specific channel and discount execution. |
| P8 Demographics (spending power) | Teen and young-adult spending should fall, hurting youth-skewed brands | Piper: teen self-reported spending -6% Y/Y (Spring 2024, $2,263), +6% (Spring 2025, $2,388), -7% vs Spring (Fall 2025, $2,213). Teen footwear spend -1% Y/Y (Spring 2024). | **Partly.** Real but small and cyclical; affects all youth brands, not Nike in particular. |

---

## 3. Evidence in detail

### 3.1 Where the decline sits: the "culture" businesses (Nike calls, OPENED)
- Performance vs Sportswear is roughly a 50-50 split (analyst question, Q4 FY26 call). Q1 FY27: "NIKE Sportswear, which accounted for just under half of this quarter's revenue, was down low double digits." "NIKE Sportswear and the Jordan Brand ... represented a high single-digit drag on consolidated NIKE." Performance "was up high single digits", "on top of the performance growing mid-single digits in FY '26 to $16 billion."
- Q4 FY26: "particularly in NIKE Sportswear and Jordan Streetwear, where sell-through remains challenged"; "Our consumer is under pressure around the world, and we can particularly see it having a larger impact on sportswear, which declined double digits in the quarter with a similar decline in retail sales." "we have taken $2 billion out of the market in FY '26 of our classic franchises."
- Q2 FY26: classics "on track to decline from peak levels by more than $4 billion by fiscal year-end."
- Q1 FY27: "As planned, we reduced revenue from the Dunk by nearly 50% in the quarter." "the Jordan Brand represented 13% of our global business with revenue falling by mid-teens." Running-inspired Sportswear silhouettes (P-6000, V5 Runner) "grew by strong double digits."
- Jordan Brand revenue (reported basis): FY2024 $8,701M (recast), FY2025 $7,270M (-16%), FY2026 $7,034M (-3%) (REPO: Q4 FY25 release p. 5; FY26 10-K p. 32). FY24 to FY26: -$1,667M, about 34% of the total decline (my arithmetic).
- Converse: $2,082M (FY24) to $1,174M (FY26), -$908M (REPO).
- **Inference:** the decline is entirely in the lifestyle, streetwear and canvas businesses whose value depends on cultural heat. That is the strongest *for* evidence: the hypothesis correctly predicts *where* the damage is. But the same pattern is predicted by the oversupply hypothesis, so the location does not discriminate. The tests below do.

### 3.2 Gen Z perception: Piper Sandler "Taking Stock With Teens" (OPENED infographics; Fall 2025 OPENED (repo))
| Wave | Nike footwear (all teens) | Nike apparel | Notes |
|---|---|---|---|
| Spring 2022 | 60% (+400 bps Y/Y) | 30% | Vans -400 bps |
| Fall 2022 | 60% | 31% | |
| Spring 2023 | 61% | 33% | On No. 12, Hoka No. 19 for all teens |
| Fall 2023 | 61% | 35% | New Balance passes Vans to No. 4 |
| Spring 2024 | 59% | 34% | "mindshare decreased 190 bps Y/Y"; Nike -510 bps in athletic footwear among upper-income teens; Converse lost the most mindshare |
| Fall 2024 | 57% | 33% | Female 48% (from 56%); upper income -11 pts; adidas among females 14% (from 3%) |
| Spring 2025 | 49% | 28% | adidas 8%; top celebrity and influencer: LeBron James |
| Fall 2025 | 46% | 26% | "stabilizing sequentially"; adidas 14%, New Balance 8% |

- Fall 2026 (now an annual survey) had not been published as of 2026-10-13 (search; SNIPPET of SGB April 2026 notice).
- **Inferences:**
  - Nike's teen footwear mindshare was at its highest level in this series in 2023, while the "death of hype" was already visible: Reuters/StockX (Sept 2023, OPENED (repo)) showed the AJ1 High resale premium at 4%, down from 61% in 2020. If sneakerhead decline or Gen Z disaffection were an independent cause, mindshare should have been falling by 2023. It was not.
  - The erosion began in Spring 2024 and accelerated in Spring 2025, the same window as Nike's classics oversupply hangover, the deliberate classics cut and the DTC discounting (`franchise_oversupply.md`, `marketing_shift.md`). It is coincident, not leading.
  - Losses were concentrated among female and upper-income teens, the trend-setting cohorts, and their gains went to adidas (Samba, Gazelle), New Balance, Hoka and On. That is a product and silhouette story (who had the right shoe), consistent with `challengers_taste.md`.
  - Spring 2025: LeBron James was the No. 1 celebrity *and* No. 1 influencer among teens. A Nike athlete topping teen culture while Nike lost mindshare argues against "basketball culture losing relevance" with Gen Z.
- **Other Gen Z trackers:** YouGov (Mar 2026; consideration Gen Z 55.4, Millennials 53.6, Gen X 39.1, Boomers 20.6; SNIPPET via Retail Dive press release, recorded in repo). Rival Technologies (903 Gen Z in US and Canada, reported Aug 20, 2026, OPENED): Apple and Nike are the two brands Gen Z is most loyal to and would recommend; no Nike figures. Morning Consult Most Trusted Brands 2026: Nike 12th among Gen Z at net trust 42.3 (SNIPPET; the report page I opened did not show Nike). Gen Z is Nike's best generation, not its worst.

### 3.3 Sneakerhead and resale culture
- **Premium collapse (2020 to 2023):** AJ1 High average premium 61% (2020) to 4% (2023); Altan Insights tied the 2020 to 2021 premiums to pandemic supply constraints (Reuters via Cyprus Mail, Sept 28, 2023, OPENED (repo)).
- **Jordan below retail:** SneakerPing study of 3,538 releases (Aug 2024 to Aug 2026): 70.7% of 605 Jordan releases last sold below retail, median 20% under; cites Nike releasing more than 700 Jordan styles each in 2022 and 2023 (BallerAlert, Sept 13, 2026, OPENED (repo); methodology unverified).
- **Resale is not shrinking overall:** StockX Big Facts Current Culture Index (Jan 12, 2026; SGB OPENED (repo); nss magazine Jan 15, 2026 OPENED): about 200 brands set record annual sales on StockX in 2025; Nike and Jordan top two sneaker brands for the third straight year; Nike average prices +5%, Jordan +6%. StockX H1 2026 (FashionUnited, Aug 2026, OPENED): Jordan sneaker sales +6%, average prices +5% "driven by retro silhouettes"; Saucony +239% displaced Asics as top sneaker; CEO Greg Schwartz: consumers "want the archive as much as the new release."
- **Natural experiment, Sept 2026 (Needham tracker via FN/Yahoo, Oct 9, 2026, OPENED):** 13 high-heat launches (vs 19 in Sept 2025 and "30+" a month in 2021 to 2022). Nike had 9 of the 13. Premiums: Air Max 1000 56%, Book 2 43%, Air Max 90 x Wagyu 43%, Caitlin 1 27% (launched Oct 1). At the same time Jordan 6 Women's Low -47% and Jordan 7 "Tennis Day" -40%; six of seven Jordan retros traded at discounts. Nike accounts for 19 of 27 potential October high-heat launches.
- **China (Huxiu / 巨潮WAVE, Oct 23, 2024, OPENED):** "年轻人不炒鞋了" ("young people stop speculating on sneakers"); the craze "从两年前就已经开始降温了" (began cooling about two years earlier, i.e. 2022); PBOC Shanghai had warned in 2019 that sneaker speculation was a "击鼓传花式资本游戏"; Dewu and Nice cancelled consignment services; Dewu cut 5% of staff in Aug 2024 citing "市场环境变得严峻". The article attributes the cooling to more rational young consumers *and* brand inventory and discounting.
- **Inferences:**
  - The speculative layer of sneaker culture did cool, globally and in China, from about 2022. That part is exogenous (COVID scarcity unwound, rates rose, Chinese regulators and platforms clamped down). But it cooled two years before Nike's revenue fell, and Nike grew revenue 10% in FY2023 with the premium already near zero. It is not the trigger.
  - Collector demand still concentrates on Nike when supply is scarce. In the same month and same market, scarce Nike product earns premiums and oversupplied Jordan retros trade 40% to 47% under retail. The variable that differs is supply, not culture. Hill concedes this: "With Jordan Brand Footwear, we're going to get back to leading the scarcity model that we created. Simply put, we've been oversupplying our iconic retro product" (Q1 FY27, OPENED).

### 3.4 Basketball culture
- **Sport demand is up.** NBA 2025-26 regular season national average 1.78M viewers, +16%, "most-watched season in seven years"; reach 170M, +86%; caveat: Nielsen Big Data + Panel methodology inflates comparisons and these are league-announced figures (Front Office Sports, Apr 15, 2026, OPENED). SFIA 2026 Topline: team sports passed 90M participants, led by basketball, baseball and soccer in youth (SNIPPET; no basketball count opened).
- **Nike Basketball (performance) grew throughout the decline** (calls, OPENED): Q3 FY24 "double-digit growth from $100-plus franchises, including Kobe and Ja"; Q2 FY25 "Ja grew double digits, Kobe became the market's largest signature franchise, with demand far exceeding available supply"; Q3 FY25 "strong growth in Kobe Protro"; Q1 FY26 North America "Running, training and basketball each delivered double-digit growth"; Q3 FY26 "basketball up high single digits"; Q1 FY27 "Basketball was up double digits in North America"; women's signature basketball "grown ... nearly 500% from FY '22 to FY '26"; Caitlin 1 launched in 5,000 doors.
- **Basketball as fashion is down.** Basketball's share of US athletic footwear fell from about 13% (2014) to under 5% (NPD via Axios, about 2019, SNIPPET), a decline that *predates* the current Nike slump and coincided with Nike's 2016 to 2019 US share loss to adidas, after which Nike recovered with the Dunk and AF1 retro wave. A Substack (Apr 14, 2026) attributes an 11% decline in 2025 basketball shoe sales to Circana (SNIPPET from search summary; the article I opened was paywalled and showed no figures). Circana's 2025 sport-lifestyle growth was "driven primarily by running-inspired and soccer/football-inspired styles" (OPENED (repo)).
- **Inference:** "basketball culture" is two different things. The sport and its performance product are healthy and growing for Nike. What lost relevance is basketball-derived *lifestyle* silhouettes (AJ1, Dunk, AF1) as youth fashion. That is a cyclical silhouette rotation (it happened in 2014 to 2019 too, and reversed), measured in `challengers_taste.md`.

### 3.5 Logo fatigue and "quiet" positioning
- NIKE Brand apparel $13,775M (FY24) to $13,449M (FY26), -2.4%, vs footwear -13.3% (REPO; `challengers_taste.md`).
- adidas (FY2024 results, OPENED): Lifestyle "increased at a double-digit rate as a result of strong double-digit growth in Originals"; FY2025 (OPENED): "Lifestyle revenues for the adidas brand increased 12% during 2025"; Q2 2026 (OPENED): "In Lifestyle, revenues rose 2%", "The lifestyle footwear market ... is currently under pressure due to heavy discounting."
- lululemon FY2025 (ended Feb 1, 2026): Americas comparable sales -3%, Americas net revenue -1% (Business Wire and SEC 8-K, Mar 17, 2026, SNIPPET).
- **Inference:** a logo-heavy peer grew in lifestyle while Nike shrank, and a logo-light peer shrank in the Americas. Logo intensity does not sort winners from losers. The "quiet" leg shows up only as a silhouette preference (Onitsuka, Asics, Salomon), already counted in the taste note.

### 3.6 Athlete roster
- Mbappe: On announced the signing Sept 18, 2026; Nike contract ran out July 31 and was not renewed (search summaries of Reuters and Goal, SNIPPET; FashionUnited, OPENED: contract value not disclosed; Federer also moved to On; Nike keeps Haaland and Vinicius). Hill on the Q1 FY27 call (OPENED): "we're proud of what we achieved together on and off the pitch ... we are excited about what our portfolio has in NIKE football."
- Other cited losses: Tiger Woods (2024) and Lamine Yamal choosing adidas (BBC via Yahoo, Oct 2, 2026, OPENED (repo)).
- Endorsement obligations (REPO): $10.2B (May 2019), $8.4B (May 2021), $7.6B (May 2022 and May 2023), $10.6B (May 2024), $16.2B (May 2025), $15.5B (May 2026).
- **Inference:** the trough in athlete commitments (2021 to 2023) coincided with record Nike revenue; the decline (FY25 to FY26) coincided with record athlete commitments. Athlete losses are a lagging *consequence* of reduced Nike heat (Derdenger: athletes now want to join "change and growth") and a forward risk for football, not a cause of the FY25 to FY26 decline.

### 3.7 China: a Gen Z cultural shift?
- Covered in `china.md` (OPENED (repo)): adidas China +13% (2025) and +16% (H1 2026), ASICS China +19.9% (2025), while domestic mass brands grew low single digits. A Gen Z nationalist turn (guochao) that hurt Nike should hurt adidas too; it did not.
- Nike's own framing: "we've become a lifestyle brand competing on price in China" (Q2 FY26, OPENED); "we have to be more premium and culturally relevant" (Q4 FY26, OPENED); "focused on becoming a more premium and culturally relevant brand" (Q1 FY27, OPENED). Nike claimed to be "Chinese consumers' #1 cool and favorite brand" as late as Q2 FY24 (OPENED). Lost cultural relevance in China is real but it followed Nike's own discounting and channel choices.

---

## 4. Strongest evidence for and against

**For:**
1. The decline sits entirely in the culture-dependent businesses: Sportswear and Jordan Streetwear were a high-single-digit drag in Q1 FY27 while Performance grew high single digits; Jordan -$1,667M FY24 to FY26 (about 34% of the decline); Converse -$908M.
2. Teen footwear mindshare fell 15 points, 61% (Fall 2023) to 46% (Fall 2025), led by female and upper-income teens.
3. Speculative sneaker culture cooled globally and in China from 2022 (high-heat launches down from 30+ a month to 13; Dewu layoffs; "年轻人不炒鞋了"), and the whole lifestyle footwear market weakened in 2026 (adidas Lifestyle +2%, "heavy discounting").
4. Basketball-derived silhouettes lost fashion share (a pattern visible in 2014 to 2019 as well).
5. Athletes now choose challengers (Mbappe to On, Yamal at adidas), a forward-looking signal of lower brand heat.

**Against:**
1. Timing: teen mindshare peaked at 61% in 2023, *after* the resale premium collapse; revenue grew 10% in FY2023. The cultural signals move with, or after, the revenue decline.
2. Same consumers, different supply: scarce Nike drops still carried 27% to 56% premiums in Sept 2026 while oversupplied Jordan retros traded 40% to 47% below retail; Kobe demand exceeded supply.
3. Peer control: adidas Lifestyle grew double digits in 2024 and 12% in 2025, selling to the same Gen Z consumers, with loud logos.
4. Basketball the sport is up (NBA viewership +16%; Nike Basketball growing double digits in North America).
5. Athlete commitments doubled to $16.2B during the decline; Mbappe left 27 months after it began.
6. Gen Z remains Nike's strongest cohort (YouGov consideration; Rival Technologies No. 2 most-loved; Piper No. 1 at more than 3x No. 2).
7. Management names supply, not culture: "we've been oversupplying our iconic retro product, asking them to do too much."

---

## 5. Independent cause or symptom?

- **Mostly a symptom.** The cultural signals (teen mindshare, Jordan resale discounts, China "cultural relevance") deteriorated after Nike over-supplied its cultural franchises and discounted them through its own digital channel. Berger and Heath (2008, *JPSP*; OPENED (repo) `academic_literature.md`): people abandon a taste when the signal spreads to groups they do not want to be identified with. Nike's own supply decisions spread the signal. Upstream: the Consumer Direct Acceleration model, which fed Nike Digital with classics and Jordan retro volume (`franchise_oversupply.md`, `dtc_wholesale.md`).
- **Small independent residual:** (a) a youth fashion rotation away from basketball and court silhouettes toward running-inspired, terrace and Japanese heritage shoes (also counted in `challengers_taste.md`); (b) the end of COVID-era speculative sneaker buying, including Chinese regulation of 炒鞋; (c) softer teen spending; (d) a market-wide lifestyle footwear slowdown in 2026.

---

## 6. Contribution estimate

Scope: $4,964M decline, FY2024 to FY2026. All allocations are judgment, anchored as noted.

| Component | Exogenous share (judgment) | $ | Anchor |
|---|---|---|---|
| Youth silhouette rotation away from basketball-derived lifestyle shoes | Overlaps `challengers_taste.md` "regardless of execution" share (15% to 25%); I assign the culture-specific slice | $0.2B to $0.5B | Vans and Converse fades; Circana lifestyle growth driven by running-inspired styles; offset by adidas Lifestyle growth in 2024 to 2025 showing the lifestyle market itself was not shrinking until 2026 |
| End of speculative sneaker demand (resale cooling, China 炒鞋 crackdown) | Small | $0.1B to $0.2B | Cooling began 2022 while Nike grew; premiums survive where supply is scarce |
| Teen spending weakness | Small | under $0.1B | -6% and -7% Piper readings, partly reversed in Spring 2025 |
| Logo fatigue | About zero | 0 | Apparel -2.4%; adidas Lifestyle grew |
| Athlete losses | About zero for FY25 to FY26 | 0 | Mbappe left Sept 2026; commitments doubled |
| **Total exogenous culture and demographics** | **about 5% to 15%** | **about $0.3B to $0.8B, central about $0.5B (10%)** | |

- **Not additive** with `challengers_taste.md` (which already includes the silhouette rotation) or with `franchise_oversupply.md` (which owns the oversupply-driven signal erosion).
- If one counts every culture-*looking* loss (teen mindshare, Jordan streetwear, Converse) regardless of what caused it, the number would be 50% or more of the decline. That figure measures *location*, not *cause*.
- **Forward risk (not in the $4,964M):** the 2026 lifestyle footwear slowdown and football roster losses (Mbappe) are live headwinds for FY2027, when guidance is a high-single-digit decline.

---

## 7. Can management fix it?

**Partly.**
- **Fixable:** supply discipline (AJ1 stabilised after supply cuts; the Jordan retro reset began Oct 2026), product newness in running-inspired lifestyle (P-6000, V5 Runner strong double digits), and performance-led cultural relevance (Kobe, Caitlin 1, Shai, World Cup). Nike's own launches show demand returns when supply is scarce.
- **Not fixable on demand:** the rotation of youth fashion away from basketball and court silhouettes, the end of COVID-era speculative buying, Chinese regulation of resale, and the 2026 lifestyle market slowdown. The Fall 2026 Piper Sandler survey (due this fall) is the next test: stabilisation at about 46% would support the symptom reading.

---

## 8. Sources

| # | Source | Date | Status | Used for |
|---|---|---|---|---|
| 1 | Nike financial data pack and `data/nike_filing_facts.csv` (10-Ks FY2019 to FY2026, Q4 FY25 release p. 5, FY26 10-K p. 32) | 2019 to 2026 | REPO | Revenue, Jordan, Converse, apparel, endorsement obligations |
| 2 | Nike earnings call transcripts Q1 FY24 to Q1 FY27 (Nike IR PDFs, text in session scratchpad `tx/`) | Sept 2023 to Oct 1, 2026 | OPENED | Sportswear vs Performance, Jordan, basketball, Mbappe answer, China relevance quotes |
| 3 | Piper Sandler Taking Stock With Teens infographics, Spring 2022 to Spring 2025 (session scratchpad `piper/`) | 2022 to 2025 | OPENED | Mindshare series, teen spending, LeBron No. 1 |
| 4 | SGB Media, Piper Sandler Fall 2025 and Fall 2024 | Oct 9, 2025; Oct 9, 2024 | OPENED (repo) | 46%, 57%, female 48% |
| 5 | SGB Media, Taking Stock With Teens becomes annual | Apr 2026 | SNIPPET | No Fall 2026 yet |
| 6 | Front Office Sports, NBA 2025-26 viewership (frontofficesports.com/?p=232016) | Apr 15, 2026 | OPENED | +16%, 1.78M, caveats |
| 7 | FN via Yahoo Finance, Needham high-heat tracker (finance.yahoo.com/markets/stocks/articles/sneaker-resale-market-had-sluggish-163420876.html) | Oct 9, 2026 | OPENED | 13 vs 19 vs 30+, Nike 9 of 13, Jordan discounts |
| 8 | FashionUnited, StockX H1 2026 report | Aug 2026 (URL dated Aug 12) | OPENED | Jordan +6%, Saucony +239%, Schwartz quote |
| 9 | nss magazine, "Ist die Sneaker-Industrie rückläufig?" | Jan 15, 2026 | OPENED | StockX 2025 records, Nike +5%, Jordan +6% |
| 10 | SGB Media, StockX Big Facts 2025 | Jan 12, 2026 | OPENED (repo) | Nike and Jordan top two |
| 11 | Reuters via Cyprus Mail, AJ1 premium 61% to 4% | Sept 28, 2023 | OPENED (repo) | Premium collapse timing |
| 12 | BallerAlert, SneakerPing study | Sept 13, 2026 | OPENED (repo) | 70.7% of Jordans below retail; 700+ releases |
| 13 | Huxiu / 巨潮WAVE, "年轻人不炒鞋了" (m.huxiu.com/article/3607652.html) | Oct 23, 2024 | OPENED | China resale cooling, Dewu layoffs |
| 14 | FashionUnited, Mbappe leaves Nike for On | Sept 18, 2026 | OPENED | Mbappe, Federer, terms undisclosed |
| 15 | Reuters, Goal, Gulf News via search on Mbappe | Sept 18, 2026 | SNIPPET | Contract ended July 31 |
| 16 | adidas FY2024, FY2025, Q2 2026 results PDFs (session scratchpad `dl/pdf/`) | Mar 2025, Mar 2026, Jul/Aug 2026 | OPENED | Lifestyle +DD, +12%, +2%; lifestyle market under pressure |
| 17 | lululemon Q4 FY2025 release (Business Wire, SEC 8-K) | Mar 17, 2026 | SNIPPET | Americas comps -3% |
| 18 | Appleworld.today on Rival Technologies Gen Z study | Aug 20, 2026 | OPENED | Nike No. 2 Gen Z loyalty (no figures) |
| 19 | Morning Consult Most Trusted Brands 2026 | 2026 (survey Jan 1 to May 15) | OPENED (Nike not shown); Nike 12th Gen Z net trust 42.3 is SNIPPET | Gen Z trust |
| 20 | YouGov / Retail Dive press release, generational consideration | Mar 11 and Mar 20, 2026 | SNIPPET (repo) | Gen Z 55.4 consideration |
| 21 | Sportsverse Substack, "How Can Basketball Get Its Bounce Back in Fashion?" | Apr 14, 2026 | OPENED (paywalled, no figures visible); 11% Circana 2025 basketball decline is SNIPPET | Basketball fashion decline |
| 22 | Axios, "The decline of the basketball shoe" (NPD 13% to under 5%) | about 2019 | SNIPPET | Prior basketball fashion cycle |
| 23 | SFIA 2026 Topline summary | 2026 | SNIPPET | Youth team sports led by basketball |
| 24 | BBC via Yahoo, "How the world's sportswear giant lost its mojo" | Oct 2, 2026 | OPENED (repo) | Derdenger, Woods, Yamal |
| 25 | Sibling notes: `challengers_taste.md`, `franchise_oversupply.md`, `china.md`, `marketing_shift.md`, `academic_literature.md`, `analysts_and_consumer_data.md`, `retailers_and_resale.md` | Oct 2026 | OPENED (repo) | Taste rotation, classics, China, Berger and Heath |

## 9. Gaps
- Piper Sandler Fall 2026 not yet published; Circana basketball category numbers for 2024 to 2026 not opened (WWD paywall); Google Trends not pulled; no Dewu (Poizon) price series for Nike in China; Morning Consult Nike Gen Z trend not opened.
