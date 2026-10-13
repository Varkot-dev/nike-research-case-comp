# Hypothesis: region and brand declines outside China (EMEA, APLA, Converse, Jordan) have their own distinct causes that matter to the total

Investigated Oct 13, 2026. Repo numbers are reused with their original citations (REPO = `research_notes/04_financial_data_pack.md`, `data/nike_filing_facts.csv`, `data/nike_channel_split.csv`). Filing text was read from local copies of the SEC documents (10-Ks FY2024 to FY2026, all 10-Qs Q1 FY2024 to Q1 FY2027, downloaded from EDGAR this session or earlier sessions) and from Nike's official call transcripts (Nike IR PDFs, text copies in the session scratchpad). "My arithmetic" marks every number I computed.

## 1. Verdict in one paragraph

The hypothesis splits four ways, and only one part holds as a truly distinct cause.

- **Converse is a distinct, independent cause.** It started falling a full year before the NIKE Brand did (Q1 FY24, -9% c-n, while NIKE Brand grew). It fell in every territory and both channels, and it kept falling (FY26 -32%, Q1 FY27 -28%) after North America recovered. About two-thirds of it tracks a canvas and skate-shoe fashion cycle that also hit Vans under a different owner. The other third is Converse-specific: a deliberate reset with demand creation cut 39% (FY26) and 58% (Q1 FY27), SKU cuts, layoffs and two CEO changes. Converse cost about **$0.9B** of revenue FY24 to FY26 (18% of the reported decline) and almost all of its EBIT ($474M to $18M).
- **EMEA matters a lot more than reported numbers show, but mostly NOT for distinct reasons.** In currency-neutral terms EMEA lost about **$1.73B** FY24 to FY26, as much as Greater China ($1.77B). A $0.69B currency tailwind hides this in reported dollars. But EMEA fell in the same quarter and by the same amount as North America in FY25 (Q1 FY25: EMEA -12%, NA -11%), for the same stated reasons (classic footwear franchises, digital promotion pull-back, Jordan). It is the same global Sportswear and classics cause, hitting a region with a "higher portfolio mix with sportswear than our other geographies" (Q4 FY26 call). A real regional residual exists from Q3 FY26 on (a promotional, low-traffic European lifestyle market, which adidas also describes, and Middle East disruption), worth roughly **$0.2B to $0.5B**.
- **APLA is minor.** Currency-neutral it fell only -3% (FY25), -1% (FY26) and 0% (Q1 FY27), about **$0.27B**. Most of its $486M reported decline is currency. Its named weak spots (Korea, Japan, Southeast Asia and India) fit a local challenger story (ASICS, Onitsuka Tiger, New Balance), but the dollars are small.
- **Jordan is a symptom, not a distinct cause.** It is large (about -$1.67B FY24 to FY26 on the recast basis), but it is booked inside the four geographies, it turned down in the same year as Nike's other classics (FY25), and the CEO names the cause as Nike's own oversupply of retro product. That is the upstream classics and supply cause (`franchise_oversupply.md`), not a separate Jordan-only problem.

**Net:** distinct, non-China causes outside the global classics and DTC story explain roughly **$1.2B to $1.6B (about 25% to 30%)** of the FY24 to FY26 reported decline of $4.96B, and Converse is about two-thirds of that. Without Converse, the region-specific part is only about 5% to 10%.

## 2. Predictions table

| # | Prediction if the hypothesis is true | Test and data | Result | Held? |
|---|---|---|---|---|
| P1 | **Timing independence.** A distinct cause should start and end on its own clock, not in the same quarter as NIKE Brand North America. | Converse c-n: Q1 FY24 -9, Q2 -13, Q3 -20, Q4 -17 while NIKE Brand grew (REPO). EMEA c-n: Q1 FY25 -12 vs NA -11; Q2 -10 vs -8; Q3 -6 vs -4; Q4 -10 vs -11 (REPO). Divergence only from Q3 FY26: EMEA -7, -6, -5 vs NA +3, +3, +2. Jordan: +3% FY24 (recast), -16% FY25, same year as Dunk and AF1. | Converse yes; EMEA no in FY25, yes from Q3 FY26; Jordan no. | **Partly** |
| P2 | **Category breadth.** A regional macro or market cause should hit all categories. A global classics cause hits Sportswear footwear only. | EMEA Q1 FY27: footwear -11% c-n, apparel +5% (10-Q). EMEA performance: running, football, golf "grew double digits" (Q4 FY26 call); "Sportswear declined double digits" (Q3 and Q4 FY26). FY24 to FY26 EMEA footwear -9.8% vs apparel -3.9% (REPO, `challengers_taste.md`). Converse: units -31% FY26 "driven by declines in all territories", wholesale and DTC both -33% (FY26 10-K). | EMEA is category-specific, so it is the global cause. Converse is brand-wide, so it is distinct. | **Partly** |
| P3 | **Peer test, Europe.** If EMEA has its own regional cause (weak European consumer), adidas Europe and the main European retailer should also fall. | adidas Europe c-n: 2024 quarterly +14, +19, +18, +25 (REPO adidas note); 2025 +10%; Q2 2026 +6% with DTC double-digit (adidas releases, OPENED local). Puma EMEA 2025 -6.9% c-a (own reset, OPENED). JD Sports Europe LFL -2.7% in Q2 to Aug 1, 2026 (World Footwear, OPENED). Consumer Edge: "In Europe, Adidas has taken market share over the past year while Nike's share has fallen" (Reuters, Oct 8, 2024, OPENED). | Through FY25 the European market grew and Nike lost share: no regional macro cause. In 2026 the market softened (JD LFL negative, adidas Europe slowed to +6% and blamed "heavy discounting at many retailers, especially in Europe"). | **No for FY25, partly for 2026** |
| P4 | **Converse vs a control brand.** If Converse's fall is a canvas-shoe cycle, it should track Vans. If it is Converse-specific, it should diverge. | Vans c-n: FY24 -24%, FY25 -16%, FY26 -9% (VF 10-Ks, REPO `macro_covid_cycle.md`). Converse c-n: FY24 -15%, FY25 -18%, FY26 -32%. Cumulative: Vans to 58% of base, Converse to 47% (my arithmetic). | Tracks in FY24 and FY25 (cycle), diverges by about 23 points in FY26 (Converse-specific reset). | **Yes, for both parts** |
| P5 | **Jordan geography.** A distinct Jordan cause (for example a basketball culture fade) should show a different geographic and timing pattern from Nike classics. | FY25 10-K names Jordan as a decliner in all four geographies, alongside Men's. Q1 FY27 call (Hill): "we've been oversupplying our iconic retro product"; "North America will feel the biggest impact". Scarce Nike drops still earned resale premiums in Sept 2026 (REPO `culture_demographics.md`). | Same pattern and timing as Nike classics; cause stated as supply. | **No (symptom)** |
| P6 | **APLA matters to the total.** If APLA has its own material cause, its currency-neutral decline should be material. | APLA c-n FY25 -3%, FY26 -1%, Q1 FY27 0% (REPO). Cumulative c-n about -$267M vs reported -$486M; about $219M is currency (my arithmetic). Nike Korea FY Jun 2023 to May 2024 revenue KRW 2.005T, -0.3%, first decline since audit reports began (NewDaily, Sept 19, 2024, OPENED). | Small. | **No (minor)** |
| P7 | **Size test.** If outside-China units matter to the total, their currency-neutral losses should be a large share of the total. | FY24 to FY26 c-n losses at FY24 base (my arithmetic): Greater China -$1,769M, EMEA -$1,728M, Converse -$921M, NA -$727M, APLA -$267M; sum -$5,412M vs total c-n -$5,557M. Q1 FY27 vs Q1 FY26 reported: GC -$332M, EMEA -$155M, Converse -$103M, APLA -$27M, NA +$107M (REPO). | EMEA + Converse + APLA = about 54% of the c-n decline. Large in size, but see P1 and P2 on cause. | **Yes (size), no (cause) for EMEA** |
| P8 | **Profit test.** A distinct brand cause should also wreck that unit's profit independently. | Converse EBIT $676M (FY23), $474M, $240M, $18M (FY26); Q2 FY26 -$4M, Q3 FY26 -$40M (REPO). Margin 22.8% to 1.5% (my arithmetic). EMEA EBIT margin 24.9% (FY24) to 19.2% (FY26). | Converse profit collapse is near total and its own. | **Yes (Converse)** |

## 3. Key data

### 3.1 Currency-neutral decomposition, FY2024 to FY2026 (my arithmetic on REPO data)

Method: FY24 reported segment revenue times compounded currency-neutral growth (FY25 then FY26). Growth rates from the FY2025 10-K p. 37 and FY2026 10-K p. 32 and 36 (REPO).

| Unit | FY24 | FY26 | Reported change | C-n cumulative | C-n loss at FY24 base | Currency and other |
|---|---|---|---|---|---|---|
| North America | 21,396 | 20,511 | -885 (-4.1%) | -3.4% | -727 | -158 |
| EMEA | 13,607 | 12,572 | -1,035 (-7.6%) | -12.7% | **-1,728** | **+693** |
| Greater China | 7,545 | 5,847 | -1,698 (-22.5%) | -23.4% | -1,769 | +71 |
| APLA | 6,729 | 6,243 | -486 (-7.2%) | -4.0% | -267 | -219 |
| Converse | 2,082 | 1,174 | -908 (-43.6%) | -44.2% | -921 | +13 |
| NIKE, Inc. | 51,362 | 46,398 | -4,964 (-9.7%) | -10.8% | -5,557 | +593 |

Reading: on reported numbers EMEA looks like a mid-sized problem. On a currency-neutral basis it is tied with Greater China as the largest. The FY2025 10-K says the FY25 decline was "primarily due to lower revenues in North America, Europe, Middle East & Africa ("EMEA") and Greater China which each decreased NIKE, Inc. Revenues by 4, 3 and 2 percentage points, respectively". The FY2026 10-K says Greater China, Converse and EMEA "decreased NIKE, Inc. Revenues by approximately 2, 1 and 1 percentage points" while North America added about 2 points.

### 3.2 Quarterly currency-neutral growth (%) (REPO, `nike_filing_facts.csv`)

| Quarter | NA | EMEA | GC | APLA | Converse | NIKE, Inc. |
|---|---|---|---|---|---|---|
| Q1 FY24 | -1 | 6 | 12 | 3 | -9 | 2 |
| Q2 FY24 | -3 | -3 | 8 | 10 | -13 | -1 |
| Q3 FY24 | 3 | -4 | 6 | 4 | -20 | n/a |
| Q4 FY24 | -1 | 1 | 7 | 4 | -17 | 0 |
| Q1 FY25 | -11 | -12 | -3 | -2 | -14 | -9 |
| Q2 FY25 | -8 | -10 | -11 | -2 | -18 | -9 |
| Q3 FY25 | -4 | -6 | -15 | -4 | -16 | -7 |
| Q4 FY25 | -11 | -10 | -20 | -3 | n/a in CSV | -11 |
| Q1 FY26 | 4 | 1 | -10 | 1 | -28 | -1 |
| Q2 FY26 | 9 | -1 | -16 | -4 | -31 | 0 |
| Q3 FY26 | 3 | -7 | -10 | -2 | -37 | -3 |
| Q4 FY26 | 3 | -6 | -17 | -1 | -34 | -4 |
| Q1 FY27 | 2 | -5 | -26 | 0 | -28 | -5 |

Three clocks are visible: Converse (starts Q1 FY24, deepens through FY26), NA and EMEA together (Q1 FY25 to Q4 FY25), and Greater China (Q1 FY25 on, deepening). EMEA leaves the NA clock from Q3 FY26.

### 3.3 EMEA channel split (REPO `nike_channel_split.csv`, USD m)

| FY | Direct | Wholesale | Total |
|---|---|---|---|
| FY2023 | 4,896 | 8,522 | 13,418 |
| FY2024 | 5,045 | 8,562 | 13,607 |
| FY2025 | 4,235 | 8,022 | 12,257 |
| FY2026 | 4,111 | 8,461 | 12,572 |

FY24 to FY26: Direct -$934M, wholesale -$101M. The EMEA loss is a NIKE Direct (mostly digital) loss: FY25 digital -30%, stores +5% (FY25 10-K); Q4 FY25 digital -36% (call); Q1 FY27 digital -26%, stores -1% (10-Q). This is the same digital reset as North America (`digital_tech.md`, `pricing_discounting.md`).

## 4. Evidence by unit

### 4.1 EMEA

What the filings say (all OPENED, local text of the SEC filings):
- Q2 FY24 10-Q: "EMEA revenues decreased 3% ... Wholesale revenues decreased 8%, reflecting our proactive decisions to prioritize marketplace health in the current year coupled with our liquidation of excess inventory in the prior year."
- FY24 10-K p. 40: "EMEA revenues were flat on a currency-neutral basis ... Unit sales of footwear decreased 4%, while higher ASP per pair contributed approximately 5 percentage points". Units were already falling as prices rose (see `pricing_discounting.md`).
- Q1 FY25 10-Q: "EMEA revenues decreased 12% ... due to lower revenues in Men's, Women's, the Jordan Brand and Kids' ... NIKE Direct revenues decreased 12%, due to digital sales declines of 24%".
- FY25 10-K: "EMEA revenues decreased 10% ... due to lower revenues in Men's, the Jordan Brand, Kids' and Women's ... decline in digital sales of 30%, partially offset by an increase in store sales of 5%."
- FY26 10-K p. 38: "EMEA revenues decreased 3% ... NIKE Direct revenues decreased 9% due to declines in digital sales of 10% and declines in store sales of 8%. Comparable store sales decreased 7%." Footwear -5%, "Lower ASP per pair was primarily due to higher discounts"; apparel flat.
- Q3 FY26 10-Q: EMEA -7%, NIKE Direct -13%, "declines in store sales of 20%. Comparable store sales decreased 19%."
- Q1 FY27 10-Q p. 27: EMEA -5%, wholesale -1%, digital -26%, stores -1%; footwear -11% ("Unit sales of footwear decreased 5%, while lower ASP per pair reduced footwear revenues by approximately 6 percentage points"); apparel +5%.

What management said on calls (OPENED, Nike IR transcripts):
- Dec 21, 2023 (Q2 FY24): "This new outlook reflects increased macro headwinds, particularly in Greater China and EMEA."
- Dec 19, 2024 (Q2 FY25): "we moved first in EMEA to reposition NIKE Digital as a premium platform."
- Jun 26, 2025 (Q4 FY25): "EMEA is furthest along in cleaning up the marketplace and repositioning NIKE Digital"; Q4 digital -36%, stores +5%.
- Dec 18, 2025 (Q2 FY26): "Sportswear growth was driven by apparel, with footwear flat, as a mid-20s percent decline in Classic footwear franchises was offset by growth in Air Max and the look of Running styles." "We saw growth in Central and Eastern Europe and the Middle East, offset by slight declines in Western Europe." "EMEA activated their sport offense on December 1, so they've just started rehiring these critically important revenue-generating roles in key countries."
- Mar 31, 2026 (Q3 FY26): "Sportswear was down double digits, and sell-through has not tracked with sell-in expectations. Promotions across the marketplace were up ... We were also more aggressive with promotions on NIKE Digital at the end of the season". "Given the softness in Sportswear, traffic patterns and promotions across Europe as well as recent disruption in the Middle East, we anticipate ending the fourth quarter with elevated inventory." Hill: "That city-led approach is especially important in EMEA, where we lack a fully integrated marketplace and it has been one of our biggest hurdles." Friend: "this quarter, we also experienced traffic disruption from the Middle East."
- Jun 30, 2026 (Q4 FY26): "EMEA continues to work through heightened inventory and promotional levels, disruption in the Middle East and a higher portfolio mix with sportswear than our other geographies." "off-price was down over 50% following aggressive actions to reduce promotions. This resulted in a 15-point improvement in full price realization."
- Oct 1, 2026 (Q1 FY27): "Training grew globally, led by EMEA." Q2 FY27 laps "significant promotional activities in EMEA from Cyber Week".

Peers (natural experiment):
- adidas brand Europe c-n: 2024 Q1 +14%, Q2 +19%, Q3 +18%, Q4 +25% (REPO `adidas_gulden.md`, adidas releases); 2025 +10% (EUR 8,136M vs 7,551M); Q4 2025 +6% with "conservative wholesale sell-in approach, especially in Europe"; Q2 2026 +6%, DTC double digit; Gulden: "The lifestyle footwear market, especially for him, is currently under pressure due to heavy discounting at many retailers, especially in Europe" and "sales declines in several Middle Eastern countries" (adidas FY2025 release Mar 4, 2026 and Q2 2026 release Jul 30, 2026, OPENED local PDFs).
- Puma EMEA 2025: "EMEA sales dropped by 6.9% (ca) to € 3,143.2 million", "with declines in Europe partly balanced by growth in EEMEA"; Q4 -24.3% from "reduction of undesired business" (Puma release Feb 26, 2026, OPENED). Puma is itself in a reset, so it is a weak control.
- JD Sports (Nike about 45% of its sales per the search summary, SNIPPET): Europe organic -0.4%, LFL -2.7% in the quarter to Aug 1, 2026; "The market stayed highly promotional" (World Footwear, Aug 27, 2026, OPENED).
- Reuters, Oct 8, 2024 (news24 syndication, OPENED): "In Europe, Adidas has taken market share over the past year while Nike's share has fallen", "according to direct to consumer sales data from Consumer Edge", with "significant gains by On Running, Puma, and Hoka."

Diagnosis for EMEA:
1. FY24 to FY25 (the big drop, about -$1.4B c-n): the same cause as North America. Same quarter, same size, same named drivers (Men's, Jordan, digital -30%, classics). The European market was growing (adidas +17% to +25%), so it was share loss, not regional macro. The regional flavour is the competitor: the adidas terrace wave (Samba, Gazelle, Spezial) was strongest in Europe, so Nike's classics lost more there. That is still the global classics and taste cause (`challengers_taste.md`, `franchise_oversupply.md`), with a European-strength rival.
2. Q3 FY26 onward (about -$0.3B to -$0.5B so far): partly regional. EMEA has a higher Sportswear mix than other geographies (exposure, not a new cause). It reset its sales organisation later (Sport Offense from Dec 1, 2025, versus North America earlier). It cannot copy North America's wholesale expansion (NA wholesale +14% FY26 with Amazon, DSW, Macy's; EMEA wholesale flat). On top: a genuinely external, promotional and low-traffic European lifestyle market (adidas and JD say the same), and Middle East disruption (adidas also saw declines there). Nike also relapsed into digital promotions in Q3 FY26, which is self-inflicted.
3. The EMEA store decline (stores -20%, comps -19% in Q3 FY26; -9% in Q4 FY26; -1% in Q1 FY27) coincides with the Middle East disruption and with Nike pulling promotions, but Nike gives no split, so I cannot size it.

### 4.2 Converse

Filings (OPENED, local SEC text):
- Q1 FY24 10-Q: "Converse revenues decreased 9% on a currency-neutral basis as revenue declines in North America were partially offset by an increase in Asia ... ASP decreased 3%, reflecting promotional activity in digital."
- Q2 FY24 10-Q: -13%, "declines in North America and Western Europe were partially offset by growth in Asia."
- Q3 FY24 10-Q: -20%, "driven by revenue declines in North America, Western Europe, and Asia."
- FY24 10-K p. 43: -15%, "Combined unit sales ... decreased 12%, driven primarily by a decrease in wholesale, while ASP decreased 3%, primarily driven by increased promotional activity in direct to consumer." EBIT -30%.
- FY25 10-K: -18%, "driven by revenue declines across all territories. Unit sales decreased 12%, while lower ASP reduced revenues by approximately 6 percentage points." Wholesale -20% "as declines in Western Europe and Asia were partially offset by growth in North America." EBIT -49%; gross margin -380 bps.
- FY26 10-K p. 41: -32%, "driven by declines in all territories. Unit sales decreased 31%". Gross margin -490 bps "as well as the brand and marketplace reset costs, including higher inventory obsolescence reserves and employee severance costs". "Demand creation expense decreased 39%". EBIT -93%.
- Q1 FY27 10-Q: -28%, "Unit sales decreased 34%, while higher ASP contributed approximately 6 percentage points ... Higher ASP per unit was primarily due to product mix and lower discounts." "Demand creation expense decreased 58%". Risk text: "Converse is in the midst of a strategic reset of the brand and marketplace. The actions related to Converse are expected to continue throughout fiscal 2027".

Calls (OPENED): Q1 FY26 (Sept 30, 2025): "With Converse, we just put new leadership in place and we're going to take aggressive actions". Q3 FY26: "We also rightsized operating costs at Converse this quarter". Q4 FY26: "Converse sharpened its strategy ... especially with the Chuck Taylor and Jack Purcell franchises ... Shai Gilgeous-Alexander has joined the NIKE Basketball family ... This move allows Converse to fully focus on serving creators through its lifestyle business." Converse is barely quantified on the calls.

People: Jared Carver CEO from 2023, left Jul 2025; Aaron Cain (Nike Men's VP/GM) CEO from Jul 2025 (REPO `02_current_exec_team.md`, `people_events.csv`, Retail Dive Jul 10, 2025 opened there).

Press: Bloomberg via FashionNetwork, Oct 16, 2025 (OPENED): "Converse has posted revenue declines for eight consecutive quarters"; "Converse tends to go in and out of style." Boston Globe (Bloomberg recording), 2026, URL dated May 7, 2026 (OPENED): "The company's signature Chuck Taylor shoe has fallen out of favor and newer styles haven't caught on with shoppers"; Cain: Converse will "do more with fewer products", focus on Chuck Taylor and Jack Purcell, and invest in "New York, Los Angeles, London, Paris, Shanghai and Seoul".

History check: Converse also fell in an earlier cycle, $2,042M (FY17) to $1,886M (FY18), EBIT $477M to $310M (FY19 10-K p. 27, 31; REPO). Converse is a cyclical fashion brand.

Diagnosis: the FY24 and FY25 fall matches the Vans canvas and skate cycle (Vans -24%, -16%), so it is mostly exogenous taste. FY26 diverges by about 23 points (Converse -32% vs Vans -9%), which matches the deliberate reset (marketing cut 39% then 58%, obsolescence write-offs, severance, SKU cuts, signature basketball moved to Nike). Excess over the Vans path is about $0.26B on the FY23 base or about $0.39B on FY26 alone (my arithmetic). Vans is not a perfect control (VF had its own execution problems), so this split is approximate.

### 4.3 APLA

Filings (OPENED, local SEC text): FY24 +5% "higher revenues in Southeast Asia & India, Mexico and Japan"; Q1 FY25 -2% "lower revenues in Korea, Pacific, Central and South America ("CASA") and Japan"; FY25 -3% "lower revenues in Southeast Asia & India and Korea, partially offset by higher revenues in Mexico. Revenues decreased primarily due to lower revenues in the Jordan Brand and Men's"; FY26 -1% "lower revenues in Southeast Asia & India, Japan and Korea, partially offset by higher revenues in Central & South America and Pacific", wholesale +2%, digital -9%; Q1 FY27 flat, "lower revenues in Japan, Korea and Mexico". FY26 EBIT -9% with gross margin -200 bps "primarily due to unfavorable changes in standard foreign currency exchange rates".

Calls: Q4 FY25: "APLA's progress varies by individual country". Q2 FY26: "We still have work to do in Greater China, parts of APLA and Converse."

Korea: Nike Korea revenue KRW 1.2936T (FY to May 2020), 1.4522T, 1.6749T, 2.0109T (+20.1%), then 2.0050T (Jun 2023 to May 2024, -0.3%), operating profit KRW 29.0B (-25.3%); causes cited "신제품의 부재와 트렌드 대응의 실패" (no new products, failure to follow trends), with Hoka, On, New Balance, ASICS and Mizuno gaining (NewDaily, Sept 19, 2024, OPENED). A recruiting site shows KRW 1.8913T for 2025 (SNIPPET only, unverified, not an audit report). Japan: no Japan-specific Nike revenue found; ASICS and Onitsuka Tiger growth is documented in REPO (`challengers_taste.md`, `source_reverification.md`) but I found no Japanese source with Nike Japan sales (search in Japanese, SNIPPET only, no hit).

Diagnosis: APLA's currency-neutral decline is small (about $0.27B over two years) and its named drivers are Jordan and Men's (the global cause) plus local challengers in Korea and Japan. Most of the reported APLA gap is currency (about $0.22B). Minor.

### 4.4 Jordan Brand

- Jordan revenue (recast definition): FY23 $8,460M, FY24 $8,701M (+3%), FY25 $7,270M (-16%), FY26 $7,034M (-3% reported, -5% c-n) (FY25 10-K p. 33 table line and FY26 10-K footnote 3, OPENED local; REPO). Q1 FY27: "the Jordan Brand represented 13% of our global business with revenue falling by mid-teens" (call, OPENED).
- FY24 to FY26 change -$1,667M (my arithmetic), about 34% of the reported decline, but it is already inside the four geographies. It cannot be added to them.
- Cause, in management's words (Q1 FY27 call, OPENED): "we've been oversupplying our iconic retro product, asking them to do too much. And as we've done with the Air Jordan 1, we will deliberately reduce the volume and frequency of specific Jordan Retro launches." "In the near term, North America will feel the biggest impact."
- Jordan was named as a decliner in every geography in the FY25 10-K: NA ("lower revenues in the Jordan Brand, Men's and Women's"), EMEA, Greater China and APLA. In FY24 Jordan was still growing in EMEA (Q2 FY24 10-Q: EMEA decline "partially offset by higher revenues in the Jordan Brand") and APLA.
- Resale evidence of oversupply: 70.7% of 605 Jordan releases sold below retail (SneakerPing study via BallerAlert, Sept 13, 2026; REPO `culture_demographics.md`, methodology unverified); scarce Nike drops still earned premiums in the same month (Needham tracker via FN/Yahoo, Oct 9, 2026, REPO).

Diagnosis: Jordan's decline is the same supply-led classics cause as Dunk and AF1, with the same timing, across all regions. Symptom, not a distinct cause.

## 5. Strongest evidence for and against

For (distinct causes that matter):
1. Converse started falling in Q1 FY24, a year before the NIKE Brand, fell in every territory and both channels, and kept falling at -28% to -37% while NA recovered.
2. Converse EBIT collapsed from $676M (FY23) to $18M (FY26), with losses in Q2 and Q3 FY26.
3. In currency-neutral terms EMEA lost about $1.73B FY24 to FY26, equal to Greater China; a $0.69B currency tailwind hides it.
4. EMEA decoupled from NA from Q3 FY26 (-7, -6, -5 vs +3, +3, +2), with management naming region-specific factors: higher Sportswear mix, no "fully integrated marketplace", promotional Europe, Middle East disruption.
5. adidas and JD Sports independently describe a promotional, softer European market in 2026, and adidas cites Middle East declines.

Against:
1. EMEA fell in the same quarter and by the same size as NA in FY25 (Q1 FY25 -12% vs -11%), for the same named reasons (classics, Jordan, digital -30%).
2. EMEA's decline is footwear and Sportswear only: Q1 FY27 footwear -11%, apparel +5%, running, football, training and golf growing. A regional macro cause would not spare performance and apparel.
3. adidas Europe grew +14% to +25% per quarter in 2024 and +10% in 2025 while Nike EMEA fell 10%: the European market was not the problem through FY25.
4. Jordan's decline is attributed by the CEO to Nike's own oversupply, appears in all geographies, and turned in the same year as Dunk and AF1.
5. APLA's currency-neutral decline is only about $0.27B; most of its reported decline is currency.
6. About two-thirds of Converse's fall tracks Vans, a different owner's brand, so a large part of the Converse "distinct cause" is an industry fashion cycle rather than something Nike did.

## 6. Upstream causes

- EMEA FY25: symptom of the global classics oversupply and Sportswear concentration, the Consumer Direct Acceleration digital model and its promotional unwind (see `franchise_oversupply.md`, `dtc_wholesale.md`, `digital_tech.md`, `pricing_discounting.md`), with adidas's terrace wave as the European-strength challenger.
- EMEA FY26 onward: the same upstream cause amplified by EMEA's higher Sportswear mix and slower org reset, plus a modest external European market and Middle East effect.
- Jordan: symptom of supply decisions (700+ Jordan releases a year in 2022 and 2023 per REPO notes, retro oversupply).
- Converse: independent. A canvas and skate fashion cycle (shared with Vans), deepened by Converse-specific management (two CEOs in three years, demand creation cuts, reset write-offs).
- APLA: mostly the global cause plus currency; small local challenger effect in Korea and Japan.

## 7. Contribution estimate (FY24 to FY26 reported decline $4,964M)

| Component | Estimate | Share | Basis |
|---|---|---|---|
| Converse, total | about $0.9B | about 18% | Reported -$908M; c-n -$921M |
| of which canvas cycle (exogenous) | $0.55B to $0.7B | 11% to 14% | Vans-path comparison |
| of which Converse-specific management and reset | $0.25B to $0.4B | 5% to 8% | FY26 excess over Vans path |
| EMEA region-specific residual (Europe market, Middle East, slower reset) | $0.2B to $0.5B | 4% to 10% | Q3 FY26 onward decoupling from NA, sized as EMEA gap vs NA for 3 to 4 quarters at about 8 to 10 points on a $3B quarterly base, minus the part explained by higher Sportswear mix |
| APLA region-specific residual (Korea, Japan, SEA&I challengers) | $0.1B to $0.2B | 2% to 4% | C-n -$267M, less the Jordan and Men's share |
| Jordan as a distinct cause | about $0 | 0% | Symptom; counted in `franchise_oversupply.md` |
| **Total distinct, non-China** | **about $1.2B to $1.6B** | **about 25% to 30%** | Converse is about two-thirds |

Note on currency: in reported dollars a further roughly $0.7B of EMEA c-n loss is masked by FX and about $0.2B of APLA reported loss is FX only. Neither is a business cause.

## 8. Can management fix it?

- **Converse: partly.** Management controls SKU count, supply, marketing and distribution, and is acting (Cain, Chuck Taylor and Jack Purcell focus, six key cities). It cannot control the canvas fashion cycle. Converse fell and recovered before (FY17 to FY19), so a cycle turn is possible, but Q1 FY27 is still -28% and the 10-Q says actions continue "throughout fiscal 2027". Divestiture is the other lever (press speculation only, Bloomberg Oct 2025).
- **EMEA: mostly yes**, because most of it is the global Sportswear and classics problem that North America has already shown can be fixed (NA +5% FY26). The regional parts (European promotions, Middle East) are not controllable, but the integrated marketplace gap and promotional discipline are. New GM Cesar Garcia from Feb 2, 2026; Nike targets the end of calendar 2026; Q2 FY27 laps the EMEA Cyber Week promotions.
- **APLA: yes, small.**
- **Jordan: yes**, through supply cuts (already done on AJ1), but at a near-term revenue cost (mid-teens decline in Q1 FY27).

## 9. Sources

| # | Source | Date | Status | Used for |
|---|---|---|---|---|
| 1 | `research_notes/04_financial_data_pack.md`, `data/nike_filing_facts.csv`, `data/nike_channel_split.csv` | built Oct 12, 2026 | REPO (OPENED) | Segment revenue, c-n growth, EBIT, channel, Jordan, Converse |
| 2 | Nike FY2024 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018724000044/nke-20240531.htm | 2024-07-25 | OPENED (local text) | EMEA flat, units -4%; APLA +5%; Converse -15% detail, EBIT -30% |
| 3 | Nike FY2025 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018725000047/nke-20250531.htm | 2025-07-17 | OPENED (local text) | EMEA -10%, digital -30%; APLA -3%; Converse -18%; Jordan 7,270 / 8,701 / 8,460; NA/EMEA/GC point contributions |
| 4 | Nike FY2026 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm | 2026-07-15 | OPENED (local text) | EMEA -3%, APLA -1%, Converse -32%, demand creation -39%, EBIT -93%; Jordan footnote; point contributions |
| 5 | Nike 10-Qs Q1 FY24 to Q3 FY26 (URLs in data pack section 8) | 2023-10-06 to 2026-04-01 | OPENED (downloaded from EDGAR this session) | Quarterly EMEA, APLA, Converse explanations by territory |
| 6 | Nike Q1 FY27 10-Q, https://www.sec.gov/Archives/edgar/data/320187/000032018726000193/nke-20260831.htm | 2026-10-02 | OPENED (local text) | EMEA -5% detail, APLA flat, Converse -28%, demand creation -58%, reset language |
| 7 | Nike earnings call transcripts Q2 FY24 to Q1 FY27 (Nike IR PDFs; text copies in session scratchpad `tx/`) | 2023-12-21 to 2026-10-01 | OPENED | Management quotes on EMEA, Converse, Jordan, APLA |
| 8 | adidas FY2025 results release | 2026-03-04 | OPENED (local PDF text) | Europe +10% c-n 2025, Q4 +6%, regional table |
| 9 | adidas Q2 2026 results release | 2026-07-30 | OPENED (local PDF text) | Europe +6%, "heavy discounting at many retailers, especially in Europe", Middle East declines |
| 10 | `research_notes/Gulden and Plank turnarounds vs Nike/adidas_gulden.md` | Oct 2026 | REPO | adidas Europe 2024 quarterly growth |
| 11 | Puma, "PUMA completes reset in 2025", https://about.puma.com/en/newsroom/corporate-news/2026/26-02-2026-puma-completes-reset-2025-2026-designated-transition-year | 2026-02-26 | OPENED | EMEA -6.9% c-a 2025, Q4 -24.3% |
| 12 | World Footwear, "JD Sports cuts profit guidance amid tough market conditions", https://www.worldfootwear.com/news/jd-sports-cuts-profit-guidance-amid-tough-market-conditions/11723.html | 2026-08-27 | OPENED | Europe organic -0.4%, LFL -2.7%, "highly promotional" |
| 13 | JD Sports, Nike about 45% of sales (search result summary, ii.co.uk / Retail Gazette) | 2026 | SNIPPET | Nike share of JD sales |
| 14 | Reuters via news24, "As Nike struggles, Adidas must surf Samba wave with caution", https://www.news24.com/business/companies/as-nike-struggles-adidas-must-surf-samba-wave-with-caution-20241008 | 2024-10-08 | OPENED | Consumer Edge: adidas gained, Nike lost share in Europe |
| 15 | Bloomberg via FashionNetwork, "Should Nike 'Just Do It' and sell Converse?", https://us.fashionnetwork.com/news/Should-nike-just-do-it-and-sell-converse-,1774107.html | 2025-10-16 | OPENED | Eight straight quarters of decline; "goes in and out of style" |
| 16 | Boston Globe (Bloomberg recording), https://www.bostonglobe.com/2026/05/07/business/converse-ceo-sales-ceo/ | 2026 (URL date May 7) | OPENED | Chuck Taylor "fallen out of favor"; Cain plan; demand creation cut "almost 60 percent" |
| 17 | NewDaily (Korea), https://biz.newdaily.co.kr/site/data/html/2024/09/19/2024091900091.amp.html | 2024-09-19 | OPENED | Nike Korea revenue series and causes |
| 18 | catch.co.kr recruiting page (Nike Korea 2025 revenue KRW 1.8913T) | n/a | SNIPPET (unverified) | Indicative only |
| 19 | fnnews, https://www.fnnews.com/news/202610022251371994 | 2026-10-05 | OPENED | Contains no Nike Korea data (checked) |
| 20 | VF Vans growth rates via `macro_covid_cycle.md` (VF 10-Ks) | Oct 2026 | REPO | Vans FY24 -24%, FY25 -16%, FY26 -9% |
| 21 | REPO notes `challengers_taste.md`, `culture_demographics.md`, `pricing_discounting.md`, `digital_tech.md`, `dtc_wholesale.md`, `02_current_exec_team.md` | Oct 2026 | REPO | Segment footwear/apparel, Jordan resale, EMEA promotions, leadership |

## 10. Gaps

- Nike does not disclose EMEA by country, the Middle East share of EMEA, or the cause of the Q3 FY26 store decline (-20%), so the Middle East effect cannot be sized.
- No independent European market-share series (Circana Europe, Kantar) was found for 2025 to 2026; the share-loss claim rests on Consumer Edge (2024) and peer growth.
- Nike Korea's 2025 audit report was not opened (DART not reached); Nike Japan sales are not published.
- Jordan's geographic split is not disclosed.
- Vans is an imperfect control for Converse.
