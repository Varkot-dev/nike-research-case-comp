# W4: Supplier labor in local-language press (2024 to Oct 2026)

Run date: October 16, 2026. Lane: W4 of the Wave 3 hunt (RESEARCH_MAP.md). Files in this folder: `W4_events.csv` (27 events), `W4_map_group_tally.csv` (Nike manufacturing map by supplier group, FY21 vs Oct 2026), `W4_official_stats.csv` (official and association statistics), `W4_routes_log.csv` (every route tried). Builds on, and does not redo: `research_notes/Smoking gun hunt/G3_units_factories.md` (map worker counts), `data/hunt/trade_imports/README.md` (Feng Tay and import tests), `research_notes/Long or short cruxes/supplier_nowcast.md` (Feng Tay and peer revenue in USD).

Tags: OPENED = page or file read in full this session. SNIPPET = seen only in a search-result summary (not used for any conclusion unless stated). DERIVED = my arithmetic from OPENED inputs. Quotes are given in the original language with a translation; translations are mine.

## 1. Bottom line

**Smoking gun: no.** The local-language press does not show a Nike-wide factory labor collapse ahead of the units decline. It shows a small, Indonesia-only set of Nike-dominant cuts, a Vietnam labor force that is flat to up and short of workers, and supplier capacity still being added. What it supports for the short case is narrow: the Nike-dominant plants are the ones cutting or furloughing, while adidas-serving and unbranded new capacity is being hired into, which is a share-shift pattern, not an industry downturn.

Headline tally (events in `W4_events.csv`; strict press counts, Indonesia is the only country with Nike-dominant cut events):

| Bucket | Cuts | Furloughs (reversible) | Hiring or openings (plans unless noted) |
|---|---|---|---|
| A. Nike-dominant: Adis Dimension (1,500), Victory Chingluh (2,000 in Nov 2024 to Jan 2025, then 2,200 to 2,804 in Oct 2025) | -5,700 to -6,304 | -4,000 (Feng Tay Indonesia, Bandung, Jun 2026; layoff plan cancelled 23 Jun) | none quantified; union says Victory Chingluh will hire at a Cirebon branch "in 1 to 2 years" (relocation, not net add) |
| B. Mixed or brand not stated: Nikomas (-279, KSPI, SNIPPET) | -279 | 0 | Pouyuen HCMC realized +3,800 (37,000 Jan 2024 to 40,800 May 2026); plans: Hwaseung +12,000 (2026), Pou Phong +3,000 (H1 2026), Kuningan 2,000 to 7,000, Hong Fu India 20,000 to 25,000 |
| C. Non-Nike: LeCrown Cambodia (Vans, North Face; SNIPPET) | -2,700 | 0 | Tah Sung Hung (adidas) recruited about 8,000 since 2020, relocating to Brebes/Cirebon (SNIPPET) |

Sizing against the Nike base (DERIVED, using G3: 223,204 Indonesian and 601,092 global Tier 1 footwear workers on the Oct 2026 map): the Bucket A cuts equal 2.6% to 2.8% of Nike's Indonesian footwear workers and 0.9% to 1.0% of global footwear Tier 1 workers; adding the furlough gives 1.6% to 1.7% of global. If labor scaled one for one with units, a -5% Q1 FY27 unit rate equals about 30,000 workers (5% of 601,092), so the press-visible cuts explain at most about one fifth (19% to 21%) of that. This is illustrative: labor does not scale with units, and the press covers only plants where a union or newspaper noticed.

Hiring is under-reported relative to layoffs (layoffs create a news event, hiring rarely does), so the absence of Nike-dominant hiring drives is weak evidence. Net-of-reporting-bias, the only quantified tally is the Bucket A cut; I do not assign a net negative number to Nike's supply base because the map says the opposite (section 4).

## 2. Events by country

Full detail, original quotes and sources are in `W4_events.csv`. Highlights:

**Indonesia (the only country with Nike-dominant labor-cut events).**
- Adis Dimension Footwear (Tangerang; Nike's long-time Indonesian partner, Inside Retail): about 1,500 cut Nov 2024 to Jan 2025; Banten labor office attributes it to brand orders. Kemenperin disputes scope and says 10,100 workers remain. OPENED (detikFinance 6 Mar 2025, Inside Retail 11 Mar 2025).
- Victory Chingluh Indonesia (Ching Luh group; Nike per Kompas and the union alliance KASBI): about 2,000 cut Nov 2024 to Jan 2025, then 2,200 (Kompas, KASBI) to 2,804 (BHRRC) in October 2025, with about 3,000 planned (CNBC Indonesia). Workforce was about 15,000 (ProPublica). OPENED. Quote: "Kalau untuk alasan PHK sendiri itu memang ada retur barang ekspor, jadi bukan karena persoalan upah" (KASBI chair; "the reason for the layoff itself is returns of export goods, so it is not a wage issue"). Kemenperin says the company is relocating to central Java for much cheaper wages ("Mereka pindah ke daerah tengah yang upahnya lebih murah, jauh lebih murah"). The two explanations are not reconciled in any source (see section 5).
- Feng Tay Indonesia (Bandung, about 14,000 workers, map 14,311): about 4,000 sent home from 15 June 2026. KSPN: raw materials from America delayed ("pasokan bahan baku/material yang mengalami keterlambatan dari Amerika"), with the worry that Nike is cutting orders ("penurunan daya beli terhadap sepatu NIKE, sehingga pihak NIKE mengurangi ordernya"). The employers' association chair Anton Supit instead blamed weaker global orders. Layoffs were cancelled on 22 to 23 June on condition of 1 to 2 days off a week; the company's proposed 50% daily wage cut during rotating days off was refused. OPENED (CNBC Indonesia 18 Jun 2026, detikFinance 23 Jun 2026). Whether orders or materials caused it is not separable from the sources; Feng Tay's USD revenue was already -8.0%, -8.5%, -8.8% for Jul, Aug, Sep (repo supplier_nowcast), which favors orders.
- Reallocation, not a shrinking base: ProPublica (3 Mar 2026, Nike's factory lists Nov 2015 and Nov 2025): Nike's Indonesian suppliers employ about 280,000; high-wage areas lost about 36,000 jobs and parts of central and west Java gained nearly 112,000, a net +76,000 over 2015 to 2025. OPENED. Tangerang to Cirebon/Brebes/Pekalongan moves are wage driven (Cirebon minimum wage 45% below the Jakarta area).
- Sector context: leather and footwear employment 966,147 in Feb 2026, +45,061 (+4.9%) y/y; value added +5.28% (Q1) and +11.30% (Q2 2026, highest in 15 quarters); footwear exports 2025 $7.98B (+9.54%). OPENED (Kontan, CNBC Indonesia Research). Counter-signal: Kemenperin's Industry Confidence Index for August 2026 had leather and footwear as the only contracting subsector of 23, blamed on uncertain US-bound orders and weak domestic demand after back-to-school; Kemenperin says the contraction is concentrated in domestically oriented firms. OPENED (Kontan, Katadata 31 Aug 2026).

**Vietnam (no Nike-supplier layoff reports found for 2024 to Oct 2026).**
- Pouyuen Vietnam (HCMC; Nike, adidas, Reebok; peak nearly 80,000): about 37,000 (Jan 2024, Tuoi Tre), 39,500 (Dec 2024), about 41,000 (Jan 2026, Tien Phong), 40,800 (May 2026, HCMC Labour Federation event). Net +3,800 (+10.3%) since Jan 2024 and +1,300 (+3.3%) since Dec 2024. OPENED. The 2023 cycle (50,500 down by about 6,000 plus 2,300) is outside the window.
- Pou Phong Vietnam (Dong Nai) is recruiting 3,000 in H1 2026 "following orders and the production plan"; brands not stated. OPENED (VietnamPlus 3 Mar 2026).
- Official: the NSO Q2 2026 manufacturing survey for "leather and related products" (footwear is most of it): employment balance -5.8 in Q2 (25.0% of firms cut, 19.2% added) against -1.4 for all manufacturing, but the Q3 forecast is +4.3; new orders balance +13.9 (Q2) and +14.6 (Q3 forecast); 47.3% cite low international demand and 38.8% cannot recruit the workers they need; capacity use 80.1% vs 75.5%. Q1 2026 text: 46.0% low international demand, 38.0% cannot recruit. OPENED. Vietnamese footwear exports were up 0.5% in H1 2026 and about 1% in Jan to Aug (OPENED).
- On the map, Freetrend Industrial (Dean Shoes group) fell from 17,560 workers (FY21) to 6,265 and Dean Shoes Vietnam (14,602) is absent; the group's Vietnam footwear headcount is 32,162 to 6,265 (DERIVED). I found no press or filing explaining it. It is the largest unexplained Nike-linked headcount drop and the one item worth chasing (section 7).

**Taiwan-listed multi-country suppliers.** Yue Yuen H1 2026: pairs 118.6M (-6.4%), ASP +1.6%, shipment mix Indonesia 52%, Vietnam 33%, China 9%; manufacturing headcount "up vs the same period last year" with new plants ramping and "highly uneven capacity loading" (製造業務人數較去年同期上升; 產能負載高度不均問題，致使產效下降). Manufacturing gross profit -23.3%, margin 14.3%. OPENED (CTEE 25 Jul 2026, SGB 12 Aug 2026). The largest multi-brand maker is adding people while shipping fewer pairs: capacity is ahead of orders. Feng Tay (Nike 88% to 90%) analysts expect about 117M pairs in 2026, a slight decline (CTEE 4 May 2026, OPENED).

**Cambodia, India, China.** No Nike-footwear supplier labor event found in Cambodia (the one footwear layoff, LeCrown 2,700, serves VF brands; sector footwear exports +24.5% in 2025, SNIPPET). India: Hong Fu (Nike among brands) Panapakkam plant and Pou Chen's Kallakurichi plant are announced (20,000 to 25,000 jobs each), with no confirmation of start-up or hiring (SNIPPET); the Nike map shows Feng Tay India workers 21,807 to 28,261 (+29.6%). China: no factory-level 2024 to 2026 events found in English or Chinese; the map shows Nike footwear workers in China -50.4% (G3) and Yue Yuen ships 9% of its pairs from China.

## 3. Nike-dominant vs other-brand comparison

Factory-level net labor changes cannot be tallied symmetrically, because the press covers Nike-dominant layoffs far better than other brands' hiring. What exists:

| Group | Press events 2024 to Oct 2026 | Revenue read (USD, Jul to Sep 2026, repo supplier_nowcast) |
|---|---|---|
| Nike-dominant (Feng Tay, Adis, Victory Chingluh) | cuts 5,700 to 6,304; furlough 4,000 | Feng Tay -8.4% |
| adidas-serving (Tah Sung Hung, Panarub, Lai Yih) | Tah Sung Hung hiring and moving to Brebes; no layoffs found 2024 to 2026 (Panarub cuts are 2022 to 2023) | Lai Yih (adidas 52%, Hoka 32%) +1.3% |
| On-serving (Fulgent Sun) | none found | +32.7% |
| ASICS, Hoka-specific Vietnamese or Indonesian plants | none found | n/a |
| Non-Nike cut | LeCrown (VF) -2,700 | n/a |

Reading: weakness is concentrated at Nike-dominant plants while adidas, Hoka and On suppliers grow, which is the same Nike-specific pattern as the revenue data. It does not add a new quantity beyond what the repo already has from Feng Tay and Lai Yih.

## 4. Net labor change on Nike's own map (DERIVED, whole-factory headcount; `W4_map_group_tally.csv`)

Mid-2021 third-party copy (authenticated in G3) vs the Oct 14 2026 live map, Tier 1 footwear:

| Group (class) | FY21 | Oct 2026 | Change |
|---|---|---|---|
| Feng Tay (Nike-dominant) | 97,177 | 96,875 | -0.3% |
| Shoetown, incl. Adis (Nike-dominant, Adis only) | 32,354 | 35,598 | +10.0% |
| Taekwang (Nike-dominant, unverified) | 59,614 | 75,876 | +27.3% |
| Chang Shin (Nike-dominant, unverified) | 55,649 | 74,899 | +34.6% |
| Four groups combined | 244,794 | 283,248 | +15.7% |
| Pou Chen / Yue Yuen (mixed) | 78,455 | 74,346 | -5.2% |
| Ching Luh (mixed, disputed) | 51,243 | 52,974 | +3.4% |
| Dean Shoes / Freetrend (mixed) | 40,600 | 9,742 | -76.0% |

Over the same span Nike footwear units are about -2.2% (G3, band -4.6% to +0.3%). Nike-dominant suppliers' whole-factory headcount rose 15.7% while units fell, so pairs per worker fell (headcount up, units flat to down: spare capacity, or lower productivity per head). Excluding the two groups I could not verify as Nike-dominant, Feng Tay plus Shoetown is +2.3%. Group-level map totals include other brands' production and are self-reported, so this is a consistency check, not a measure of Nike orders. One factory-level observation (hypothesis, DERIVED): Victory Chingluh's main Tangerang entry fell from 13,512 (FY21) to 11,562 (Oct 2026), -1,950, close to the first-round 2,000 cut; a second entry of 3,949 appeared and the Oct 2025 round is not yet visible, so the map lags press by months.

## 5. Alternatives tested for "why are Nike-dominant plants cutting?"

| Candidate | Evidence | Verdict |
|---|---|---|
| Tariff-driven relocation between countries | Indonesia and Vietnam shares of Nike pairs are up or flat (G3: implied Indonesia pairs index 24.5 to 27.0, Vietnam flat); Vietnam became the largest US footwear supplier in Q1 2026 (+9.3%) while China's fell by more than half (VOV, OPENED). The Banten cuts are intra-Indonesia moves to Cirebon/Central Java | Ruled out as the cause of the Indonesian cuts; relevant only to the China decline (map -50%) |
| Intra-country wage arbitrage (Tangerang to central Java) | Kemenperin, KSPI, ProPublica: Cirebon minimum wage 45% below Jakarta area; net +76,000 jobs in Indonesia 2015 to 2025; Tah Sung Hung (adidas) moved the same way | Survives as a driver of where jobs sit, and explains why Banten headcount falls while Indonesia's base grows. It does not explain Feng Tay Bandung (West Java, a low-wage area) |
| Quality returns at the plant (KASBI) | Union claim only; company, Aprisindo and Nike gave no confirmation; Nike's published response (20 Nov 2025, SNIPPET via search summary) says it checked legal compliance | Cannot be tested; a single-source union claim |
| Automation | Nike cites automation as a driver of geographic moves (ProPublica); no plant-level source mentions robots, and Yue Yuen headcount is rising | No evidence; not supported |
| Seasonal layoffs | Cuts were permanent with severance at 2x statutory minimum (Oct 2025) and spanned Nov to Jan and Oct, not a recurring seasonal pattern; the June 2026 event was a furlough at minimum wage | Ruled out for the severance cases; the furlough could be seasonal or material-driven and is not separable |
| Brand mix / share shift away from Nike plants | Feng Tay -8.4% USD vs Lai Yih +1.3% and Fulgent Sun +32.7% (Jul to Sep 2026); adidas-serving Tah Sung Hung is hiring; Indonesian sector value added +11.3% in Q2 2026 while Nike-dominant plants cut | Survives: consistent with Nike orders falling while the industry grows |
| Lower Nike orders vs materials delay (Feng Tay Bandung) | KSPN says materials; Aprisindo chair says orders; USD revenue -8% | Two explanations survive; what would decide: Feng Tay's Q3 2026 report and call, or Nike's own supplier statement |
| Nike deliberate supply cuts vs weaker sell-through | Same gap noted in G3: factory labor data cannot separate them | Remains open; needs Circana or GfK sell-through |

## 6. What the labor data says against the units and FY28 consensus

Nike footwear units: Q1 FY27 -5% (10-Q p. 28, via G3), FY26 -1%. FY28 consensus (repo consensus_and_valuation, Yahoo, 13 Oct 2026): revenue $43,645M (+1.1%), EPS $1.646.

- Timing test (3 to 6 month lead): the Nov 2024 to Jan 2025 cuts came after the Q1 FY25 unit trough start (-10% for Jun to Aug 2024) and were coincident with Q2 and Q3 FY25 (-7%, -8%): a lag, not a lead. The October 2025 Victory Chingluh round led the Q3 FY26 (-2%, Dec to Feb) and Q1 FY27 (-5%) declines by about 2 and 8 months: a lead. The June 2026 furlough would lead Q2 FY27 (Sep to Nov 2026), which is not yet reported. With three events and mixed timing, no lead-lag relation is established.
- Direction for FY28: nothing in the labor data points to a Nike-specific hiring wave that would precede a revenue recovery; the only Nike-dominant hiring mention is relocation capacity at Cirebon. Meanwhile supplier capacity is being added (Yue Yuen headcount up with pairs down; Pou Phong, Hwaseung, new central Java plants), so excess capacity sits ahead of orders, which pressures supplier margins (Yue Yuen manufacturing gross margin 14.3%) and is compatible with continued Nike discounting. This neither confirms nor refutes the consensus path of +1.1% revenue and +150 bps margin; it leans mildly toward the bear case on units and mildly against any near-term supply shortage.
- Vietnam, the largest Nike source at 52% of pairs, shows no cut signal at all and a Q3 employment forecast of +4.3: if Nike were about to take a large unit step down, the Vietnamese survey for footwear does not yet show it, though it covers all brands.

## 7. What I could not get, and what would settle it

- **Official indices.** Vietnam GSO/NSO monthly footwear production index: gso.gov.vn is proxy-blocked and the nso.gov.vn IIP pages show 2022 data only (Excel attachment unreachable), so I substituted the NSO Q2 2026 business survey. Indonesia BPS IBS footwear production index: bps.go.id returns 403 on every route; substitutes are BPS GDP value added (via Kontan and CNBC Indonesia), Feb 2026 employment, and Kemenperin IKI. Settling item: BPS table "Perkembangan Produksi Industri Manufaktur Besar dan Sedang" (ISIC 15) and NSO "IIP-VIE.xlsx" for 2026, from a network that reaches those sites.
- **Press coverage gaps.** Bisnis.com and Tirto return 403 on both fetch tools (content from search summaries only); Vietnamese direct-site searches (VnExpress, Tuoi Tre, Lao Dong) found nothing for 2024 to 2026 but cannot be treated as proof of absence; Putian and Dongguan local press could not be reached.
- **Unverified items.** The Nikomas 279 layoff (KSPI list, SNIPPET), Hong Fu and Pou Chen India start-up status, LeCrown brands, Nike's 20 Nov 2025 Victory Chingluh response text, whether Feng Tay Bandung workers returned in July 2026, Taekwang and Chang Shin Nike share, and the cause of the Freetrend/Dean Shoes Vietnam headcount drop.
- **Companies' own headcount.** Employee counts in Yue Yuen's 2025 annual report (HKEX) and Feng Tay's annual report (MOPS) would give a time series of manufacturing headcount per country; not pulled here. Nike's map refresh (next snapshot) would show whether the Oct 2025 Victory Chingluh cut enters the factory totals.
- **Not decidable from this data:** layoffs from order cuts vs quality problems at Victory Chingluh, and Nike supply cuts vs weaker sell-through.

## 8. Data conflicts noted

- Victory Chingluh Oct 2025 count: 2,200 (Kompas), 2,804 (BHRRC), about 3,000 (CNBC); I carry 2,200 to 2,804 as the range.
- Adis: 1,500 cut (Banten labor office) vs 10,100 workers remaining (Kemenperin) vs 8,371 on the Oct 2026 map.
- Indonesia IKI: Kemenperin says footwear is the only contracting subsector in August 2026, while a Fortune IDN summary says the footwear production index rose from 54.55 to 55.70 (SNIPPET); not resolved.
- Vietnam footwear export totals for 2025 differ across outlets ($22.82B for footwear plus handbags in Viet Nam News vs "more than $24B footwear" in VOV); I use only the growth rates.
- Feng Tay's July 2026 +1.0% in sgbonline is in NT$; in USD it is -8.0% (repo nowcast), because the TWD was about 10% weaker.
