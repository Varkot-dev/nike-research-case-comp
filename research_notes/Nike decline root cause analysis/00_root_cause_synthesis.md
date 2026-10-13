# Nike decline: root cause synthesis (lead investigator)

Date: 2026-10-13. Scope: the FY2024 to FY2026 revenue decline of **$4,964M** (FY24 $51,362M, FY24 10-K p. 57; FY26 $46,398M, FY26 10-K p. 55), the Q1 FY2027 relapse ($11,720M to $11,213M, -$507M, Q1 FY27 10-Q p. 1), and, separately, the stock decline from $177.51 (Nov 5, 2021) to $35.35 (Oct 12, 2026), -80.1% (`data/nke_daily_prices.csv`, market data, my arithmetic).

Inputs: all 23 hypothesis notes in this folder, each with the investigator's findings and the appended REFUTER and ROOT-CAUSE challenges, plus `REPORT.md`, `04_financial_data_pack.md`, `data/nike_filing_facts.csv`, `data/nike_channel_split.csv` and `data/nke_daily_prices.csv`. I did no new web research for this synthesis; every number below is taken from those notes or the repo data, with the source label the original researcher recorded. Labels: **REPO** = verified in the repo data files with filing and page; **OPENED** = the researcher read the document; **SNIPPET** = search summary only; **my arithmetic** and **my judgment** are marked.

A measurement note that matters for every share below. The reported decline ($4,964M) understates the business decline because currency was a tailwind: FX translation was a detriment of about $419M in FY25 (FY25 10-K p. 45) and a benefit of about $1,023M in FY26 (FY26 10-K p. 44), about $0.6B net (REPO, my arithmetic). The currency-neutral FY24 to FY26 decline is about 10.8%, roughly **$5.5B** (`peer_differential.md`, my arithmetic). My attribution buckets are therefore expressed as shares of the reported $4,964M and sum to slightly more than 100% at their central values.

---

## 1. Bottom line (five sentences, ranked)

1. **The primary cause is Nike's own Consumer Direct strategy**, launched by insider CEO Mark Parker on June 15, 2017 and escalated by John Donahoe as Consumer Direct Acceleration on June 25, 2020: it pulled Nike back from wholesale and run specialty, concentrated lifestyle in three classics (Dunk, Air Force 1, Air Jordan 1) fed through a promotional NIKE Digital channel, and dissolved the sport category teams, and its forced unwind outside China (classics cut by more than $4B from peak, NIKE Digital down $3.5B) explains about **40% to 50%** of the $4,964M FY24 to FY26 decline.
2. **Second is Nike's execution in Greater China** (sell-in to partners grew 15% in FY24 while Nike's own Direct grew 1%, distributors then cleared the excess online, stores went unrefreshed for seven years), which explains about **18% to 26%**, while adidas grew 9% to 17% currency-neutral each quarter through the same Topsports doors.
3. **Third, and genuinely external, is a fashion rotation** away from court, basketball and canvas silhouettes toward running-inspired and terrace styles (Converse -52% and Vans -42% from peak under different owners), worth about **10% to 20%**, plus a post-2021 lower ceiling for foreign brands in China worth about **6% to 16%**.
4. **The rest is small:** a Converse-specific reset (5% to 8%) and macro effects including 2026 softness, the Middle East conflict and the US Hispanic pullback (2% to 8%, rising to perhaps 15% to 30% of the FY27 leg), while tariffs, technology, governance, the CEO change, the World Cup, the marketing shift, pricing and lost wholesale shelf each explain about 0% to 5% on their own because they are either mis-timed or downstream of cause 1.
5. **Net of the currency tailwind and a flat-to-growing market, essentially the whole revenue decline is Nike-specific and mostly fixable** (North America returned to growth four quarters after the classics reset, as it did after the FY2018 Jordan tightening), but the stock is a different story: about **45%** of the log share-price fall is a sector-wide de-rating (adidas's P/E fell by the same 52% on flat EPS) that no Nike management can reverse.

Ranked causes (FY24 to FY26 revenue decline, adjudicated, non-overlapping buckets):

| Rank | Cause | Root or symptom | Share of $4,964M | $B | Fixable |
|---|---|---|---|---|---|
| 1 | Consumer Direct model (2017 CDO, 2020 CDA) and its unwind outside China: classics concentration and oversupply on NIKE Digital, promotion dependence, channel give-back, lifestyle newness gap, Jordan retro | Root (Nike decision) | 40% to 50% | 2.0 to 2.5 | Partly, already working in NA |
| 2 | Greater China execution: FY24 channel loading, distributor online price war, aged partner stores, thin local staff | Mostly the China expression of cause 1, amplified by China's partner-run structure | 18% to 26% | 0.9 to 1.3 | Partly, "beyond fiscal 2027" |
| 3 | Fashion rotation away from court, basketball and canvas silhouettes (incl. Converse canvas cycle) | Root (exogenous); Nike's exposure to it was a symptom of cause 1 | 10% to 20% | 0.5 to 1.0 | Partly (ride the next wave) |
| 4 | China external: post-2021 boycott and guochao ceiling for foreign incumbents, 2026 China softness | Root (exogenous); timing deferred by Nike | 6% to 16% | 0.3 to 0.8 | No |
| 5 | Converse-specific reset (marketing cut 39%, SKU and supply cuts, two CEO changes) | Management response to cause 3 | 5% to 8% | 0.25 to 0.4 | Partly |
| 6 | Macro: 2026 discretionary softness, European promotions, Middle East, Hispanic pullback | Root (exogenous) | 2% to 8% | 0.1 to 0.4 | No (mean-reverts) |
| | **Sum of central values** | | **about 105%** | **about 5.2** | Consistent with a c-n decline of about $5.5B |

On this ledger, Nike's own decisions (rows 1, 2, 5) account for about **65% to 75% of the gross headwinds**, and external forces (rows 3, 4, 6) for about **25% to 35%**. Against the net figure, the FX tailwind (+$0.6B) and a flat-to-growing market offset most of the external part, which is why the peer differential finds the Nike-specific residual at about 90% or more of the net decline (`peer_differential.md`, REFUTER re-estimate).

---

## 2. Causal map

### 2.1 Chain with decision dates

```
CONTEXT (FY2015 to FY2017, Parker)
  Demand shifts to "the look of sport"; Sportswear ~$8.6B, NA wholesale "promotional",
  Running flat; Hoka wholesale already growing 40% to 50% a year (Deckers 10-Ks)
        |
        v
ROOT DECISION A: Consumer Direct Offense (June 15, 2017, insider CEO Parker)
  - own channel worth "nearly twice the revenue" per transaction (CFO Campion, Q4 FY17 call)
  - ~25% fewer styles, "edit" to scaled "power franchises", 12 key cities
  - exit "less differentiated" wholesale, incl. run specialty ("more than 4 years ago,
    we pulled back", Friend, Oct 1, 2024)
  - Mar 2018: categories cut from nine to six; Nike Brand President exits
        |
        v
ROOT DECISION B: Consumer Direct Acceleration (June 25, 2020, Donahoe; Parker Exec Chairman)
  Nike's own words: "a new digitally empowered phase of the Consumer Direct Offense"
  (FY21 10-K p. 28)
  - "lead with NIKE Digital"; Men's/Women's/Kids construct replaces sport teams;
    ~700 HQ jobs cut (WARN, Nov 2020)
  - classics feed Digital: "continuously adding new styles" (Sept 22, 2020);
    "exclusivity at scale" (Sept 2021); 700+ Jordan releases a year 2022 and 2023
  - marketing moves "deeper into the funnel" to paid performance media (Sept 2020)
  - digital revenue = 1/3 of company-wide bonus FY21 to FY23 (2021 proxy p. 35);
    60% direct / 40% digital targets (June 2021); "exited about 50%" of partners (Sept 2021)
        |
        |   EXOGENOUS SHOCKS that masked or amplified it:
        |   COVID scarcity FY21 to FY22 (demand "significantly exceed[s]" supply, Mar 2022)
        |   Vietnam closures, ~130M units cancelled (Q2 FY22)
        |   Xinjiang boycott (late Mar 2021); 2022 bullwhip (inventory +44% at Aug 31, 2022)
        |   Resale collapse 2022 to Feb 2023 (Panda Dunk >$300 to <=$150; AJ1 premium 61% to 4%)
        v
TRANSMISSION (symptoms, FY2023 to FY2024)
  - FY23 liquidation inflates the peak (NA +27% to +30% in Q2 and Q3 FY23; GM -250 bps)
  - China channel loading: GC wholesale +15% in FY24 vs Direct +1%, digital -8%
  - NA units fall under price increases (footwear units -10% and -17% in Q1, Q2 FY24)
  - Digital slows to +2% (Q1 FY24); 44% of Nike sneakers discounted at 8 chains (early 2024)
  - Dec 21, 2023 guidance cut ("managing our franchises"); Mar 21, 2024 "pulling back supply
    of classics"; June 27, 2024 guidance cut, Lifestyle declines (NKE -20.0% next day)
        |                                        ROOT C (exogenous): silhouette rotation
        |                                        Vans falls from 2022; Converse from Q1 FY24;
        v                                        running and terrace rise (Circana)
THE DECLINE (FY2025 to Q1 FY2027)                         |
  - Q1 FY25 cliff -10.4% (before Hill's first day, Oct 14, 2024)  <----------+
  - classics cut >$4B from peak; Digital $12.1B -> $9.6B -> $8.6B
  - NA promo days "over 30" -> zero (Jan to Feb 2025); FY25 footwear ASP -3 pts, GM -180 bps
  - GC distributor online clearance, Topsports GM 41.8% -> 38.0%; Nike exits distributor
    online from Jan 1, 2027                      ROOT D (exogenous): post-2021 China ceiling
  - Converse reset, demand creation -39% FY26    for foreign incumbents (adidas -14% c-n vs 2021)
        |
        v
REVERSAL (Hill): sport teams back (May 2024, Sept 2025), wholesale rebuilt (NA wholesale
record $11,958M FY26), running +$1B in five quarters -> North America grows from Q1 FY26.
Persistence in FY27 = Greater China (-26% c-n), Converse (-28%), aged Sportswear and
Jordan retro ("lack of energy in the lifestyle space", Oct 1, 2026).
```

### 2.2 Which causes are roots and which are symptoms

| Classification | Items |
|---|---|
| **Root, Nike decision** | The Consumer Direct strategy, set in June 2017 (CDO) and escalated in June 2020 (CDA). One decision set, two dates. |
| **Root, external** | The silhouette rotation (court, basketball and canvas down; running-inspired and terrace up); the post-2021 China ceiling for foreign incumbents; 2026 macro softness; COVID scarcity and the 2022 bullwhip as amplifiers and maskers, not as causes of the FY25 to FY26 fall; US tariffs (margin only); the 2026 sector de-rating (stock only). |
| **Transmission mechanisms (symptoms of the root that carry real dollars)** | Classics oversupply; promotional NIKE Digital and its unwind; Nike's China sell-in and distributor price war; the lifestyle newness gap; the run-specialty and wholesale retreat. |
| **Symptoms with little independent weight** | Discounting; the marketing shift; the 2020 org construct and talent loss; the digital bonus metric; technology cost base; teen mindshare and resale "culture"; Women's and apparel lag; partner destocking at Foot Locker and Hibbett; the rising tax rate; executive churn (15 of 19 named exits came after Sept 2024). |
| **Ruled out as causes of the revenue decline** | See section 4. |

### 2.3 Adjudication of the root date: 2017 or 2020?

The investigators placed the root at CDA in 2020 and implicitly on the outsider CEO. Four ROOT-CAUSE challenges (`org_talent.md`, `innovation_drought.md`, `marketing_shift.md`, `dtc_wholesale.md`) moved it to 2017. **I side with the challengers on the origin and with the investigators on the escalation.**
- For 2017: Nike itself calls CDA "a new digitally empowered phase of the Consumer Direct Offense" (FY21 10-K p. 28, OPENED). The own-channel economics were stated in 2017 ("nearly twice the revenue", Q4 FY17 call, 8-K Ex. 99.1 filed 2017-07-05, OPENED). Running's share of NIKE Brand wholesale-equivalent revenue was already falling, 15.9% (FY17) to 13.8% (FY19) (FY19 10-K p. 27, OPENED, my arithmetic). Nike's US share fell more in 2016 to 2019 (40.5% to 34.1%) than in 2019 to 2025 (to 28.9%) (Euromonitor via HGI, OPENED). Adult athletic-footwear preference among 25 to 34 year olds fell from 45% (2017) to 36% (2022) (Cowen via SGB, 2022-10-24, OPENED).
- For 2020 as the escalation that produced the FY25 cliff: the classics-on-digital scaling ("continuously adding new styles", "exclusivity at scale", 700+ Jordan releases a year) and the dismantling of category teams are 2020 to 2022 decisions, and the dollars that later fell were built in that window.
- Consequence for the thesis: this is not an "outsider CEO" story. The strategy was conceived by insider leadership and approved by a founder-led board, and Parker remained Executive Chairman throughout. Hill's program reverses both phases.

---

## 3. Every hypothesis: final verdict after challenges

Shares are independent shares of the FY24 to FY26 reported decline ($4,964M) after my adjudication. Rows overlap where noted; only the section 1 ledger is additive.

| # | Hypothesis (file) | Final verdict | Independent share | Fixable | Confidence | Single strongest evidence |
|---|---|---|---|---|---|---|
| 1 | Timeline forensics (`timeline_forensics.md`) | Method. Supports the Consumer Direct chain as primary; refuter's correction accepted that timing cannot rank pricing, liquidation base effect and franchise supply decisions inside that chain | Chain: 40% to 50% (not 50% to 60%) | Partly | Medium | Nike grew 10% in FY23 while adidas NA fell 16% c-n and Vans fell; the Q1 FY25 cliff (-10.4%) came before Hill (Oct 14, 2024) and tariffs (Apr 2025) (REPO; adidas FY23 release, OPENED) |
| 2 | Peer differential (`peer_differential.md`) | Primary (as a diagnostic): Nike-specific share of the net decline about 90% or more | n/a (diagnostic) | Mostly | High | Over Nike FY24 to FY26, peer pool +15.4% and incumbent cohort +6.2% constant FX, Nike about -10.8% c-n; 9 of 12 peers grew (SEC XBRL and peer reports, OPENED; my arithmetic) |
| 3 | Classics franchise oversupply (`franchise_oversupply.md`) | Contributing cause; the principal transmission mechanism of the Consumer Direct root | 15% to 25% independent (gross classics cut >$4B from peak) | Partly | Medium | Within-franchise gradient: Dunk still cut "nearly 50%" in Q1 FY27 while AF1 stabilised first (Nike transcripts, OPENED); Hill: "we've been oversupplying our iconic retro product" (Q1 FY27 call, OPENED) |
| 4 | DTC pivot and wholesale shelf (`dtc_wholesale.md`) | Strategy: root (cause 1). Shelf mechanism: minor for FY24 to FY26 | Shelf 0% to 5%; strategy counted in cause 1 | Partly (shelf already rebought) | High | NA wholesale was back above FY19 by FY23 ($11,273M) and a record $11,958M in FY26 while NA Direct fell $1,839M (REPO) |
| 5 | Digital and technology (`digital_tech.md`) | Symptom of cause 1; technology itself minor | Revenue 0% to 5%; about 3% to 5% of EBIT decline | Partly | High | Under Armour shows the same channel signature on a different stack: eCommerce -23% vs stores -2% after "planned reductions in promotional activities" (UA FY25 Q4 Ex. 99.1, OPENED) |
| 6 | Pricing and discounting (`pricing_discounting.md`) | Symptom (visible clearing of the glut) | 0% to 5% independent; mechanism about $1.0B FY25 footwear ASP drag, about 180 bps GM | Partly | Medium-high | Same 8 chains, early 2024: Nike 44% of items discounted vs Hoka 4.5%, On 23.1%, Puma 37.4% (Reuters/Vertical Knowledge via syndicated copy, OPENED) |
| 7 | Innovation drought (`innovation_drought.md`) | Symptom: running leg was a channel decision; lifestyle leg was the classics doctrine | 0% to 10% | Yes (running already fixed) | Medium | Performance "grew double digits" in Q4 FY24, the quarter Lifestyle first fell (Q4 FY24 call, OPENED); Friend: "More than 4 years ago, we pulled back on our engagement with that channel" (Q1 FY25 call, OPENED) |
| 8 | Marketing shift (`marketing_shift.md`) | Symptom (marketing arm of cause 1) | 0% to 5% | Partly | Medium | Demand creation at 11.2% of revenue in Q1 FY27, the highest in the series, yet revenue -4.3% (Q1 FY27 10-Q, REPO; my arithmetic) |
| 9 | Org, talent and churn (`org_talent.md`) | Symptom (implementation layer of the 2017 to 2020 strategy) | 0% to 5% | Partly | Medium | Greater China had the most stable leader (GM Apr 2015 to Mar 2026) and the worst decline (-22.5%); NA had three GMs and the smallest (REPO; Nike release and Yicai, OPENED) |
| 10 | Governance and incentives (`governance_incentives.md`) | Symptom and amplifier (no challenge passes run) | 0% to 5%, fully overlapping cause 1 | Partly (metric removed for FY24) | Medium | "Digital Revenue" entered the bonus in June 2020 "to support digital growth in connection with our Consumer Direct Acceleration strategy" (2021 proxy p. 35, OPENED): pay followed strategy |
| 11 | China-specific forces (`china.md`) | Contributing cause, split: Nike-made channel problems are the larger part; external forces are real but smaller | Nike-made 18% to 26%; external 6% to 16% | Partly | Medium-low | adidas Greater China grew +9% to +17% c-n every quarter from Q3 2024 to Q2 2026 while Nike fell -3% to -20%; the gap opens in Q1 FY25 (adidas quarterly PDFs, OPENED; REPO) |
| 12 | Challengers and taste shift (`challengers_taste.md`) | Contributing cause; the "regardless of execution" claim fails | 10% to 20% execution-independent (includes Converse canvas cycle) | Partly | Medium | Nike run-specialty dollars +35.4% while On -19.7% and Hoka -7.4% (12 months to Sept 2025, SGB, OPENED): the trend reverses when Nike executes |
| 13 | EMEA, APLA, Converse, Jordan (`emea_converse_jordan.md`) | Converse-specific reset contributing; EMEA and APLA residuals minor; Jordan a symptom | Converse-specific 5% to 8%; EMEA plus APLA residual 2% to 6% | Partly | Medium | Converse fell a year before NIKE Brand (Q1 FY24) in all territories and both channels; FY26 demand creation -39% (FY26 10-K, OPENED) |
| 14 | Culture and demographics (`culture_demographics.md`) | Symptom (no challenge passes run); exogenous residual sits inside row 12 | Inside row 12 | Partly | Medium | Sept 2026: scarce Nike drops traded at 27% to 56% resale premiums while six of seven Jordan retros traded below retail: same culture, different supply (note sources, OPENED) |
| 15 | Apparel and women (`apparel_women.md`) | Minor | 0% to 5% (central about 3%) | Partly | High | NA apparel hit a record $6,075M in FY26 and grew 6% in Q1 FY27 while lululemon US fell 8% (FY26 10-K p. 37, Q1 FY27 10-Q p. 26, REPO; lululemon 10-Q, OPENED) |
| 16 | Macro and COVID cycle (`macro_covid_cycle.md`) | Minor for FY24 to FY26; larger in FY27 | 2% to 8% gross excluding the silhouette cycle; about 0 net of FX; FY27 15% to 30% | No (mean-reverts) | Medium-high | US footwear PCE rose +1.8% (2024) and +4.4% (2025) and sits above its pre-COVID trend (FRED, OPENED) while Nike NA footwear fell 13% in FY25 |
| 17 | Tariffs, freight, sourcing (`tariffs_costs.md`) | Minor: 0% of revenue; FY26 margin hit mostly refunded | Revenue 0%; FY26 gross tariff about $1.07B to $1.14B, net $0.1B to $0.2B after the $986M IEEPA recovery | Partly | High | North America, the only tariff-exposed segment, grew 4.8% in FY26 while tariffs peaked (REPO) |
| 18 | Valuation vs business (`valuation_vs_business.md`) | Contributing cause of the stock fall only (no challenge passes run) | 0% of revenue; about 45% of the log stock decline | No (sector-wide) | Medium-high | adidas's trailing P/E fell the same 52% (about 40x to 19.2x) with flat EPS (adidas reports and market data, OPENED) |
| 19 | Effective tax rate drift (`effective_tax_rate_drift.md`) | Minor and largely a symptom of lower pretax profit | 0% of revenue; 7% to 9% of the EPS decline; about 5% of the log stock decline | Partly | High | Pillar Two "did not have a material impact on the Company's financial statements for fiscal 2025" (FY25 10-K, OPENED) |
| 20 | Middle East conflict 2026 (`middle_east_conflict_2026.md`) | Minor | Under 2% ($0.02B to $0.08B) | No | Medium | Q3 FY26 ended Feb 28, 2026, the day the strikes began, yet that quarter carried the EMEA store break; Q4 EMEA stores improved from -20% to about -9% (10-Q and calls, OPENED) |
| 21 | US partner destocking (`us_wholesale_partner_destocking.md`) | Symptom (transmission of the classics glut into FY27) | About 0% in FY24 to FY26; FY27 $0.1B to $0.3B | Partly | Medium | NA wholesale grew +10.8%, +9.8%, +9.0% in Q3 FY26 to Q1 FY27; Hill: Foot Locker comps "positive for the first time in 4 years" (REPO; Q4 FY26 call, OPENED) |
| 22 | World Cup 2026 shift (`world_cup_2026_event_shift.md`) | Not supported | About 0% | No | High | Nike Global Football grew "strong double-digit" in all four geographies and NIKE Brand apparel rose 2% in Q1 FY27 (Q1 FY27 call and 10-Q, OPENED) |
| 23 | US Hispanic consumer pullback (`hispanic_consumer_pullback.md`) | Minor | About 1% to 3% realized; low confidence | No | Low | Nike NA grew in every quarter of the peak enforcement window (+4.0%, +8.8%, +3.3%, +2.7%, +2.1%, REPO); the NA decline began in Q1 FY25, before the cause |

### 3.1 Where investigators and skeptics disagreed, and my ruling

| Hypothesis | Investigator | Skeptics | Ruling and reason |
|---|---|---|---|
| Franchise oversupply | Primary, 40% to 60% | Contributing, 10% to 25%; symptom of CDA | **Skeptics on independence, investigator on importance.** The ">$4B" is a gross, unaudited, peak-based figure, and comparing it with a net fiscal-year decline is a category error (REFUTER R1, second pass test 2). FY25's non-classics business fell about $3B (R2). Classic silhouettes with no scarcity model (Vans -42%, Converse -52%, Samba) faded by similar amounts (R5, RC3). But the within-franchise gradient and Hill's admission make it the main channel through which cause 1 reached revenue. Independent share 15% to 25%. |
| Timeline forensics | Primary, CDA chain 50% to 60% | Contributing; NA broke first in wholesale and units, digital lead is partly a base effect | **Split.** The refuter is right on the facts (Q1 FY24 NA wholesale -8% "to manage inventory supply", footwear units -10% with ASP +8 pts, 10-Q OPENED; the Q1 FY25 +120 bps GM came from freight, not absent discounting). But those facts are all inside the same Consumer Direct decision set (supply discipline, pricing, franchise management), and every candidate trigger outside it (macro, boycott, tariffs, Hill, account cuts, marketing) remains ruled out on timing. I keep the chain as primary at 40% to 50%. |
| DTC and wholesale shelf | Contributing, 5% to 15% | Minor, 0% to 5% | **Skeptics.** The peak-to-trough logic is decisive: shelf lost in 2020 to 2023 was already missing from the FY24 base, and NIKE Brand wholesale was $27,758M (FY24), $25,883M (FY25), $27,453M (FY26) (REPO). The broader DTC strategy is the root (cause 1); the shelf mechanism is not a driver of the FY24 to FY26 fall. |
| Innovation drought | Contributing, 10% to 25% | Symptom, 0% to 10% | **Skeptics.** The category test (Performance grew to about $16B while Sportswear fell) and the reversal test (running +$1B yet total -4% in Q1 FY27) both fail. The CFO's full quote ties the running loss to the channel pullback. Real forgone growth in FY21 to FY24, not part of the measured decline. |
| China | External $0.3B to $0.6B | ROOT-CAUSE: external $0.9B to $1.4B; REFUTER: $0.2B to $0.6B; C9 addendum: about half and half | **Between them: external $0.3B to $0.8B.** C1 and C2 (FY24 sell-in ahead of sell-through, GC inventory +10% while Nike total fell 11%) are solid and make the China story mostly Nike-made in timing. But the -21% adidas benchmark was in euros; currency-neutral it is about -14% and adidas is now near its 2021 level, which caps the external level effect at about $0.85B before removing the 2022 lockdown overlap (R2-1, R2-2, C9). |
| Challengers and taste | 25% to 45% (execution-independent 15% to 25%) | REFUTER 19% to 33% (10% to 15% independent); ROOT-CAUSE 10% to 20% | **10% to 20% execution-independent, including the Converse canvas cycle.** The rotation is real and hits every owner of the fading silhouettes, but geography is inverse (NA, the challengers' home, fell least) and Nike wins inside the trend when it executes. The investigator's 25% to 45% double-counts dollars in rows 3, 6 and 7. |
| EMEA, Converse, Jordan | 25% to 30% distinct | 7% to 15% | **Skeptics.** The EMEA residual estimate ($0.2B to $0.5B) exceeded EMEA's entire FY26 c-n loss (about $0.37B); peers (On EMEA +20.5% c-c, ASICS Europe +43.8%) grew in Europe in the same quarters. The Converse canvas cycle is the same silhouette wave already counted in row 3 of the ledger. |
| Macro | 15% to 25% gross | 8% to 22% gross; about 0 net of FX | **2% to 8% for macro proper**, after moving the silhouette cycle into its own bucket. Net of the $0.6B FX tailwind it is about zero for FY24 to FY26. FY27 is different (15% to 30%, low confidence). |
| Pricing, marketing, org | 10% to 20%, 5% to 15%, 10% to 20% | 0% to 10%, 0% to 8%, 0% to 5% | **Skeptics in all three.** Each is a real mechanism whose dollars are already inside cause 1; none passes its discriminating test (Hoka priced higher and discounted least; record demand creation intensity without revenue response; China's stable leadership with the worst decline). |
| Peer differential | 95% to 155% Nike-specific | REFUTER: about 90% or more, central 100% to 110% | **REFUTER.** China market proxy corrected (apparel and footwear retail +0.3% and +3.2%, not sports goods +11% and +16%); UA also had a double-digit self-inflicted DTC decline, so the channel signature is an incumbent reset playbook, not unique to Nike. |

---

## 4. Explanations ruled out

| Explanation | Ruled out as | Evidence |
|---|---|---|
| Macro and COVID payback as the main driver | Main cause of FY24 to FY26 | Nike grew 10% in FY23 (NA +18%) while the industry fell (adidas NA -16% c-n in 2023, Vans -12% then -24%, US footwear -3% Jan to Aug 2023 per Circana via SGB, OPENED). US footwear PCE rose every year 2021 to 2025 and is 7% above its 2014 to 2019 trend in 2025 (FRED, OPENED). adidas brand +13% c-n in both 2024 and 2025, New Balance +19%, ASICS +19.5%, On +30% (filings and releases, OPENED). Holding share of a market up about 6% would have put FY26 near $54B, so the gap is share, not market size (my arithmetic). |
| The 2022 bullwhip and inventory glut | Cause of the FY25 cliff | Inventory was -10% to -14% YoY through FY24 (REPO) and "weeks of supply at their lowest levels since the pandemic" by Mar 2024 (Q3 FY24 call, OPENED). The glut explains the FY23 margin dip (46.0% to 43.5%), not the FY25 revenue fall. |
| Tariffs, freight, sourcing | Any cause of the revenue decline; cause of the FY25 earnings collapse | Revenue decline began Q1 FY25, about eight months before the first 2025 tariffs. FY25 product costs (+80 bps) and logistics (+20 bps) were margin tailwinds (FY25 10-K p. 35, REPO). The tariff-exposed segment (NA) grew 4.8% in FY26. On (90% of footwear from Vietnam) raised GM to 62.8% (20-F, OPENED). The $986M IEEPA recovery offset most of the FY26 cost. Earnings keep falling in FY27 with tariffs neutral (Q1 FY27 10-Q p. 23, REPO). |
| The 2021 Xinjiang boycott and guochao as the trigger in China | Trigger of the 2024 to 2026 collapse | Greater China grew +4% (FY23) and +8% (FY24) c-n (REPO) and broke only in Q1 FY25, the same quarter as the global classics break. Foreign premium brands outgrew domestic mass brands in 2025 to 2026 (adidas +13%, ASICS +19.9% vs Anta brand +3.7%, Li-Ning +3.2%; HKEX and company filings, OPENED). Nike China Running grew six straight quarters. Caveat: the boycott-era level reset is part of the external China bucket. |
| The outsider CEO (Donahoe) as the root | Root cause | The strategy was Parker's 2017 CDO; Nike calls CDA a "phase" of it (FY21 10-K p. 28, OPENED). Parker was Executive Chairman throughout. Revenue rose 37% under Donahoe (FY20 to FY24, REPO). |
| Elliott Hill's reset as the cause | Trigger | The June 27, 2024 guidance cut and the Q1 FY25 quarter (-10.4%) both precede his Oct 14, 2024 start. He chose the depth of the FY25 to FY26 supply cuts, which is a cost of the cure, not the disease. |
| Executive churn and layoffs | Cause of FY24 to FY26 | 15 of 19 named senior exits came after Sept 2024 (`data/people_events.csv`, REPO). Headcount fell 12.8% FY23 to FY26 during the decline; that is forward risk, not an explanation. |
| Lost wholesale shelf as a driver of FY24 to FY26 | Driver of the measured decline | The shelf had been restored before the decline (NA wholesale $11,273M in FY23, above FY19), and NIKE Brand wholesale fell only $305M FY24 to FY26 while Direct fell $3,799M (REPO). At Dick's, a favoured partner, Nike's purchase share rose from about 17% (FY21) to about 25% (FY24) while US share kept falling (Dick's 10-Ks, OPENED). |
| A technology or app failure | Revenue driver | Digital grew 60%, 18% and 24% (FY21 to FY23) on the same systems; NA digital and store trends converge once promotion cuts are lapped; UA shows the same gap on a different stack; much of China's digital decline ran on Tmall, JD and Douyin (`digital_tech.md`, OPENED sources). |
| Dual-class control and buybacks | Cause of the bad decisions | Dual-class has been constant since 1980; outside investors cheered the strategy (NKE +15.5% on June 25, 2021, REPO); widely held adidas ran the same DTC pivot. Demand creation rose while buybacks ran ($3,114M FY21 to $4,285M FY24, REPO). |
| Losing women and apparel to lululemon, Alo, Vuori | Material driver | Apparel fell only $326M (6.6% of the decline) and its share of NIKE Brand rose; NA apparel is at a record; Women's fell at the same rate as Men's in FY25 (FY25 10-K p. 33, REPO). |
| Logo fatigue and athlete losses (Mbappe) | Driver | NIKE Brand apparel, the most logo-dependent category, fell only 2.4%; Mbappe left on Sept 18, 2026, 27 months after the decline began; endorsement obligations rose (REPO). |
| World Cup 2026 shifting spend to adidas | Cause of the Q1 FY27 relapse | Nike football, apparel and North America all grew in the tournament quarter; the relapse sits in footwear, Greater China, Converse and Digital, and predates the tournament (Q4 FY26 -4% c-n) (Q1 FY27 10-Q and call, OPENED). |
| Pillar Two minimum tax | Cause of the EPS decline | "Did not have a material impact" (FY25 10-K, OPENED); no minimum-tax line in the FY26 rate reconciliation. |
| The Middle East conflict as the cause of the EMEA break | Cause of the Q3 FY26 EMEA store decline | The quarter ended on the day the strikes began; EMEA inventory was already up double digits; the first full war quarter showed EMEA stores improving (`middle_east_conflict_2026.md`, OPENED sources). |
| Foot Locker clean-out as a drag on H2 FY26 | Drag on FY26 | NA wholesale accelerated through the clean-out; the NA slowdown sits in NIKE Direct (REPO). |

---

## 5. What remains unexplained or uncertain, and what would settle it

| Open question | Why it matters | Data that would settle it |
|---|---|---|
| How the $3.8B NIKE Direct decline splits between (a) classics supply cut, (b) removed promotions and paid media, (c) channel relocation to wholesale at about half the revenue per pair, and (d) genuine traffic loss | Decides how much of cause 1 is a one-time, chosen give-back versus lost demand. Q1 FY27 Digital still fell 13% after the promotion cut was lapped (Q1 FY27 10-Q p. 22, REPO), which points to some real demand loss on Nike's own channel | Franchise-by-channel revenue and traffic and conversion data, which Nike does not disclose; Similarweb or Sensor Tower series for 2025 to 2026 |
| What exactly is in the ">$4 billion" classics bucket (does it include the Chuck Taylor?), and how much of the drop from peak falls inside FY24 | The size of the oversupply mechanism | A Nike definition of the bucket, or franchise-level data; no filing names the franchises |
| Nike's sell-through versus sell-in in Greater China, and its category split | Decides whether the external China share is $0.3B or $0.8B, and how much of the -26% is chosen destocking | Topsports and Pou Sheng Nike-only sell-through (not public); Nike China category revenue; Dewu price series |
| Whether the lifestyle slump is a cycle or durable category shrinkage | The biggest uncertainty for fixability. Hill: "a lack of energy in the lifestyle space" and "a sea of sameness ... across our brands and our competitors" (Q1 FY27 call, OPENED); Circana shows sport lifestyle declining in H1 2026 | Q2 and Q3 FY27 Sportswear growth as the "more than a dozen" new styles land; Circana H2 2026 sport-lifestyle data; adidas Lifestyle in H2 2026 |
| Converse: cycle versus management | Splits $0.9B between external and fixable | Vans FY2027 trajectory; Converse c-n growth once the 39% and 58% demand-creation cuts are lapped |
| A consistent annual US share series including DTC | Dates Nike's share loss (2016 to 2019 vs 2024 to 2025) precisely | Circana brand share with DTC, or a single Euromonitor annual series 2016 to 2025 |
| Whether pre-2024 brand erosion was broad | Only one survey (Cowen, July 2022, via SGB) shows adult erosion from 2017; teen data peaked in 2023 | The underlying Cowen report; YouGov or Morning Consult series 2017 to 2024 |
| The FY27 macro share | My 15% to 30% is low confidence | Peer H2 2026 results in Europe and China; NBS sports goods data for H2 2026 |
| Partner destocking in FY27 | Tests whether Foot Locker and Hibbett become a separate drag | Q2 FY27 NA wholesale (due late Dec 2026) against Dick's and Academy comps |
| The mid-20s FY27 tax guide | Whether OBBBA changes to FDII and GILTI explain part of it | Nike's Q2 FY27 10-Q tax note |
| Who took Nike's vacated doors and when | Only qualitative evidence (Foot Locker Nike share 75% to 59%, Hoka in Foot Locker from July 2022) | Account-level sell-through; Nike's list of exited accounts, never disclosed |

---

## 6. What this means for the case thesis

### 6.1 Thesis

**Nike's decline is primarily an execution failure and is mostly fixable, but "fixable" means returning to the incumbent growth line, not to the FY2024 peak or the 2021 valuation.** One strategic bet, the Consumer Direct strategy of 2017 to 2023, concentrated the brand in three lifestyle classics sold through a promotional own channel and pulled it out of the doors and categories where the next trend was forming. The revenue line from FY25 records the unwinding of that bet, magnified in China by partner loading and a distributor price war. External forces are real but secondary: a fashion rotation away from Nike's silhouettes, a lower ceiling for foreign brands in China, and, for the stock, a sector-wide de-rating. On my ledger, Nike's own decisions account for about 65% to 75% of the gross headwinds and essentially all of the net decline.

### 6.2 Five strongest proof points

1. **Peers grew while Nike fell, in the same markets and quarters.** Over Nike FY24 to FY26 the peer pool grew 15.4% and the incumbent cohort 6.2% in constant FX, while Nike fell about 10.8% currency-neutral; 9 of 12 peers grew (`peer_differential.md`, SEC XBRL and company reports, OPENED; my arithmetic).
2. **The fix already worked where it was applied first.** North America returned to growth four quarters after the classics reset and wholesale rebuild (+4.0%, +8.8%, +3.3%, +2.7%, +2.1% from Q1 FY26 to Q1 FY27, REPO), with NA footwear units +6% in FY26 (FY26 10-K p. 37, OPENED). That is the same shape as FY2018, when a Jordan tightening cost three negative NA quarters and new product restored growth in the fourth (8-K transcripts, OPENED).
3. **The trend reverses when Nike executes inside it.** Running added "roughly $1 billion" over five quarters, Performance reached about $16B in FY26, and Nike run-specialty dollars rose 35.4% while On fell 19.7% and Hoka 7.4% (Nike calls, OPENED; SGB, 2025-12-03, OPENED). A structural force operating "regardless of execution" would not reverse in four to six quarters.
4. **The decline sits where Nike's own model was concentrated.** NIKE Direct fell $3,799M versus wholesale -$305M (FY24 to FY26, REPO); classics on Digital were "down nearly 50%" in Q1 FY25 while wholesale trends were "substantially better" (Q1 FY25 call, OPENED); Hill: "we've shifted investments away from creating demand for our brand to capturing the brand demand through performance marketing" and Digital ran "50% full price and 50% off price" (Q2 FY25 call, OPENED).
5. **China is a same-store natural experiment.** Through the same Topsports doors, adidas Greater China grew +9% to +17% c-n per quarter from mid-2024 while Nike fell -3% to -20%; the gap opened in exactly the quarter Nike began cutting classics globally; Nike's FY24 China sell-in (+15%) ran ahead of its own Direct (+1%) and GC inventory rose 10% while total Nike inventory fell 11% (adidas PDFs, Nike 10-Ks, OPENED); Hill: "we've become a lifestyle brand competing on price in China" (Q2 FY26 call, OPENED).

### 6.3 Three hardest objections

1. **"Fixable" is not showing up in the total.** Two years into the reset, with sport teams restored, record demand-creation intensity (11.2% of Q1 FY27 revenue) and running back, Nike still fell 4.3% in Q1 FY27 and guides FY27 down high-single digits (REPO). NIKE Digital fell 13% after the promotion cut had been lapped, and management describes a lifestyle market with "a lack of energy" across all brands. If lifestyle sneakers are in durable decline, part of what I call execution is structural. *Response:* the live decline is concentrated in Greater China (65% of Q1 FY27) and Converse (20%); NIKE Brand outside China fell only 0.8% (REPO, my arithmetic). The objection is fair for timing, not for direction.
2. **Over the long window Nike is just another incumbent losing share.** Nike's US share fell from 40.5% (2016) to 28.9% (2025) (Euromonitor via HGI, OPENED), and indexed to 2019 Nike (about 119 to 124) sits on the incumbent line (about 114 to 121) while challengers reached about 267 (`peer_differential.md`). Fragmentation toward On, Hoka, New Balance and ASICS hit adidas, VF, UA and Puma too. *Implication:* the FY24 to FY26 fall is the loss of a premium built in FY21 to FY24 that was itself inflated by DTC pricing, classics oversupply and FY23 liquidation; the realistic recovery target is the incumbent line, not $51B.
3. **China and the stock may not be fixable on management's timetable.** Nike says China actions extend "beyond fiscal 2027" and that China "actually gets worse" this year (Q1 FY27 10-Q p. 20 and call, REPO and OPENED); the external China slice could be as high as about $0.85B; and about 45% of the 80% log stock decline is a sector-wide multiple compression (adidas -50%, Puma, UA, VF and lululemon -79% to -80% from Nov 5, 2021) that no operating fix reverses. Nike also still trades at about 28x guided FY27 EPS, so the market already prices a recovery (`valuation_vs_business.md`, market data).

### 6.4 Stock versus business, in one paragraph

The stock and the business are separate stories with different causes. From Nov 5, 2021 to Sept 30, 2022 the price fell 53% while EPS fell 6%; 91% of that log move was multiple compression and Nike moved in line with peers. From June 2024 to Oct 2026 the price fell 62.5% and 79% of the log move was EPS (ex-IEEPA), with Nike falling far more than adidas or On (`valuation_vs_business.md`). Over the whole window about 45% of the log decline is P/E (sector and rates), about 55% is EPS (the business causes above), and about 5% of the total is the rising tax rate, itself mostly a by-product of lower pretax profit (`effective_tax_rate_drift.md`).

---

## 7. Sources

Labels and dates are carried over from the notes that opened them. Each note in this folder has a fuller source table.

### 7.1 Repo data (verified, with filing and page)
| Source | Date | Status |
|---|---|---|
| `data/nike_filing_facts.csv` (revenues, segments, gross margin, EPS, FX translation, inventory) | filings FY2016 to Q1 FY2027 | REPO |
| `data/nike_channel_split.csv` (Direct, Digital, wholesale by segment) | FY2019 to Q1 FY2027 | REPO |
| `research_notes/04_financial_data_pack.md` | 2026-10-12 | REPO |
| `data/nke_daily_prices.csv` (Yahoo Finance closes) | to 2026-10-12 | REPO (market data) |
| `data/people_events.csv` (executive exits) | to 2026-10-12 | REPO |

### 7.2 Nike SEC filings and official transcripts
| Source | Date | Status |
|---|---|---|
| Nike FY2017 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018717000090/nke-5312017x10k.htm | 2017-07-20 | OPENED (`dtc_wholesale.md`) |
| Nike Q4 FY17 call transcript, 8-K Ex. 99.1, https://www.sec.gov/Archives/edgar/data/320187/000032018717000059/q4fy17erccexhibit991.htm | 2017-07-05 | OPENED |
| Nike Q3 FY18 call transcript, 8-K Ex. 99.1, https://www.sec.gov/Archives/edgar/data/320187/000032018718000037/q3fy18erccexhibit991.htm | 2018-03-27 | OPENED (`timeline_forensics.md`) |
| Nike earnings releases Q4 FY16 to Q2 FY23 (27 documents, 8-K Ex. 99.1) | 2016-06 to 2022-12 | OPENED (`timeline_forensics.md`) |
| Nike FY2019 to FY2021 10-Ks (category wholesale-equivalent tables p. 27, p. 31, p. 32; CDA "phase" wording FY21 p. 28) | 2019-07 to 2021-07 | OPENED (`org_talent.md`) |
| Nike FY2020 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018720000047/nke-531202010k.htm (CDA, p. 27) | 2020-07-24 | OPENED |
| Nike FY2022 to FY2024 10-Ks (units and ASP, Greater China channel rates, Digital $12.1B) | 2022-07 to 2024-07-25 | OPENED |
| Nike Q1 FY24 and Q2 FY24 10-Qs (NA wholesale -8% and -9%, units -10% and -17%) | 2023-10, 2024-01 | OPENED (`timeline_forensics.md` REFUTER) |
| Nike Q1 FY25 10-Q, https://www.sec.gov/Archives/edgar/data/320187/000032018724000065/nke-20240831.htm | 2024-10 | OPENED |
| Nike FY2025 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018725000047/nke-20250531.htm (footwear ASP -3 pts, GM bridge p. 35, Pillar Two) | 2025-07-17 | OPENED |
| Nike FY2026 10-K, https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm (pp. 30 to 44; Converse "strategic reset"; IEEPA recovery) | 2026-07-15 | OPENED |
| Nike Q1 FY27 10-Q, https://www.sec.gov/Archives/edgar/data/320187/000032018726000193/nke-20260831.htm | 2026-10-02 | OPENED |
| Nike official call transcripts Q1 FY21 to Q1 FY27 (investors.nike.com webcast_transcript PDFs) | 2020-09 to 2026-10-01 | OPENED (`franchise_oversupply.md`, `china.md`, `innovation_drought.md` and others) |
| Nike proxies 2021 to 2026 (digital revenue in bonus, 2021 proxy p. 35) | 2021 to 2026 | OPENED (`governance_incentives.md`) |
| Nike EDGAR submissions index, https://data.sec.gov/submissions/CIK0000320187.json | 2026-10-13 | OPENED |

### 7.3 Peers, partners and markets
| Source | Date | Status |
|---|---|---|
| adidas quarterly results PDFs Q2 2024 to Q2 2026; FY2022 to FY2025 releases; Annual Reports 2023 to 2025 Greater China pages | 2023-03 to 2026-07-30 | OPENED |
| adidas FY2023 results (World Footwear, EQS ad hoc) | 2024-03 | SNIPPET |
| Puma AR2024; FY2025 release (2026-02-26) | 2025, 2026 | OPENED |
| Puma Q2 2025 and Q2 2026 releases | 2025-07, 2026-07-31 | SNIPPET |
| Under Armour FY2025 Q4 8-K Ex. 99.1, https://www.sec.gov/Archives/edgar/data/1336917/000133691725000058/exhibit991-fiscal2025q4.htm | 2025-05-15 | OPENED |
| Deckers 10-Ks FY2020, FY2022, FY2024, FY2026 | 2020-06-01 to 2026-05-22 | OPENED |
| On Holding 424B4 (2021-09-16), 20-Fs FY2022 and FY2025, Q2 2026 6-K release (2026-08-11) | 2021 to 2026 | OPENED |
| ASICS FY2025 consolidated summary | 2026-02-13 | OPENED |
| VF Corp FY2023 and FY2025 10-Ks (Vans) | 2023-05, 2025-05 | OPENED |
| lululemon FY2025 10-K and Q2 FY2026 release | 2026-03-17, 2026-09-03 | OPENED |
| Crocs Q4 2025 and Q2 2026 releases | 2026-02-12, 2026-07-30 | OPENED |
| Foot Locker 10-Ks 2017 to 2025 (Nike 75% to 59% of purchases); Q1 and Q2 2025 8-Ks (WSS comps) | 2017 to 2025 | OPENED |
| Dick's Sporting Goods 10-Ks FY2016 to FY2025; 10-Q for quarter ended 2026-08-01 | 2017 to 2026 | OPENED |
| Topsports HKEX results FY2022/23 to FY2025/26, Q1 FY2026/27 update, inside information (Nike online 22% of revenue) | 2023-05-23 to 2026-07-22 | OPENED |
| Pou Sheng voluntary announcement (Nike online 15% of revenue) | 2026-07-22 | OPENED |
| Anta, Li-Ning, Xtep, 361 Degrees 2025 and 2026 interim filings (HKEX) | 2026-03 to 2026-08 | OPENED |
| Amer Sports 20-F FY2025 | 2026 | OPENED |
| NBS retail sales releases (Dec 2024, Dec 2025, June 2026, Aug 2026) | 2025-01-17 to 2026-09-15 | OPENED |
| HGI, "Have athletic footwear industry titans lost their step?" (Euromonitor Passport, Dec 18, 2025), https://hgi.io/insights/have-athletic-footwear-industry-titans-lost-their-step/ | 2026-01-13 | OPENED |
| Al Jazeera (GlobalData US share 2021 to 2023) | 2024-06-28 | OPENED |
| Circana via MR Magazine (2025 footwear) and Retail Dive (H1 2025); Circana release (H1 2026) | 2026-02-05, 2025-08-19, 2026-08-17 | OPENED |
| FRED: US footwear PCE (DFTWRC1A027NBEA), CPI footwear, shoe-store sales | to 2026 | OPENED |
| Euromonitor sportswear forecast press release | 2025 or 2026 | SNIPPET (502) |

### 7.4 Press, surveys and commentary
| Source | Date | Status |
|---|---|---|
| Axios, sneaker resale prices drop (Panda Dunk <=$150), via web.archive.org | 2023-02-22 | OPENED |
| Reuters via Cyprus Mail, AJ1 resale premium 61% to 4% | 2023-09-28 | OPENED |
| Reuters, "Retailers slash prices on more Nike sneakers in 2024" (Vertical Knowledge), via syndicated copy | 2024 | OPENED |
| WSJ (Inti Pacheco) republished by InvestNews (700+ Jordan releases a year) | 2024-10-02 | OPENED (republication; WSJ original not opened; exact SNKRS figures SNIPPET-grade) |
| Bloomberg Businessweek Donahoe feature | 2024-09-13 | SNIPPET (403) |
| Massimo Giunco essay via FashionUnited and Puck summaries | 2024-08 | SNIPPET |
| Piper Sandler Taking Stock With Teens via SGB Media (49% spring 2025; female under 40%) | 2025-04-10 | OPENED |
| Cowen consumer survey via SGB Media (adult preference 45% to 36%, 2017 to 2022) | 2022-10-24 | OPENED |
| SGB Media, run specialty (Nike +35.4%, On -19.7%, Hoka -7.4%) | 2025-12-03 | OPENED |
| CNN via ABC17 (Nike "exited about 50%" of partners; NA accounts cut "roughly 30%") | 2021-12-08, 2021-03-22 | OPENED |
| Modern Retail (DSW and Macy's return Oct 2023) | 2023-06-09 | OPENED |
| Apparel Resources (Foot Locker restores Nike running placement after two years) | 2025-08-19 | OPENED |
| Gear Patrol (Samba $500 resale to $75 at Dick's) | 2024-10-30 | OPENED |
| Xinhua reprint of Beijing Youth Daily (¥400 price gaps for the same Nike shoe) | 2026-07-24 | OPENED |
| Reuters via MarketScreener (Shoe Palace traffic, Kantar Hispanic visits) | 2025-11-12 | OPENED |
| NBC News (Hispanics 23% of sneaker sales, NPD) | 2017-07-20 | OPENED |
| Retail Insight Network (conflict start Feb 28, 2026) | 2026-04-14 | OPENED |
| TheIndustry.fashion (ASICS Europe +43.8%, Q1 2026) | 2026-05-13 | OPENED |
| Morningstar Tmall boycott estimate; Euromonitor 2020 China shares (qianzhan) | 2021 | SNIPPET |
| Trade press on 2017 to 2021 account exits (Retail TouchPoints, RetailWire, formula4media, worldfootwear) | 2017 to 2021 | SNIPPET |

### 7.5 Companion notes in this folder (each with its own OPENED and SNIPPET table)
`apparel_women.md`, `challengers_taste.md`, `china.md`, `culture_demographics.md`, `digital_tech.md`, `dtc_wholesale.md`, `effective_tax_rate_drift.md`, `emea_converse_jordan.md`, `franchise_oversupply.md`, `governance_incentives.md`, `hispanic_consumer_pullback.md`, `innovation_drought.md`, `macro_covid_cycle.md`, `marketing_shift.md`, `middle_east_conflict_2026.md`, `org_talent.md`, `peer_differential.md`, `pricing_discounting.md`, `tariffs_costs.md`, `timeline_forensics.md`, `us_wholesale_partner_destocking.md`, `valuation_vs_business.md`, `world_cup_2026_event_shift.md` (all dated 2026-10-13).
