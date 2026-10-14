# Nike US inbound shipments: is Nike cutting or rebuilding the holiday 2026 pipeline?

**Written:** Oct 14, 2026. **Data:** `data/hunt/nike_shipments/` (README lists every source and every attempt). **Builds on:** `data/hunt/trade_imports/` and `supplier_nowcast.md`.

Labels: OPENED = page or file opened this session. DERIVED = my arithmetic. BOL = bill of lading (one US customs manifest record).

## Verdict

**INCONCLUSIVE. Strength: weak.** Free data cannot measure Nike-brand US inbound volume for 2023 to 2026. The visible proxies lean slightly LONG on holiday timing (Nike Canada and factory leaks rise into Jul-Sep while peers fall). Converse, the only clean Nike-owned series, is falling hard, but that is already in reported numbers. None of this outweighs the hard Nike-specific data point, Feng Tay revenue -8.4% in USD for Jul-Sep 2026 (`supplier_nowcast.md`). Do not cite shipments as evidence for either side in the pitch beyond the Converse point.

## What was found

1. **Nike masks its name on US manifests almost all the time, not only since Nov 2022** (OPENED: ImportGenius and ImportInfo company pages, Panjiva public page). "Nike USA, Inc." shows 0 shipments in 2019, 1 in 2020, 41,370 in 2021, 96,160 in 2022, 0 in 2023 and 0 in 2024 (ImportGenius annual counts). Panjiva's last Nike USA record is 2022-11-16. Nike's factories (Feng Tay, Chang Shin, Pratama, TK Industrial, Lotus) appear as shippers at scale only in the same Feb 2021 to Nov 2022 window. The visible window looks like a lapse in the two-year 19 CFR 103.31 confidentiality certificate. So there is no 2019-2020 baseline either, and the 95,363 BOLs in 2022 are the exception, not the norm.
2. **What leaks since 2024 is small and provider-specific.** Nike factory names re-appear with a blank consignee and notify party "Expeditors International, 2508 N Marine Dr, Portland". The rate is about 1% to 3% of 2022, and the two providers disagree (PT Chang Shin Indonesia 2026 YTD: 14 on ImportGenius vs about 150 on ImportInfo). Single names switch on and off (Chang Shin Vietnam 76 to 400 in Jul-Sep; Lotus India 0 to 130). These are visibility series, not volume.
3. **Converse (Nike-owned, never masked) is a clean monthly series, and it is collapsing.** Jul-Sep BOLs: 278 (2024), 214 (2025), 154 (2026), so -28% YoY and -45% vs 2024; Jan-Sep 2026 -53% YoY (DERIVED from ImportInfo). The holiday months are less bad than H1 (Jan-Jun 2026 averaged 32 a month vs 51 in Jul-Sep), so the inbound decline is easing, not deepening. This is consistent with reported Converse revenue (FY23 $2,427M to FY26 $1,174M; Q1 FY27 -$103M, repo notes) and adds little new information.
4. **Nike Canada (named consignee, cargo landed at Tacoma/Seattle)**: Jul-Sep 955 BOLs vs 495 (+93%) and 409 in 2024. October 1 to about 9 already shows 216 vs 111 for all of October 2025. But Jan-Sep is +0.5%, so this is a shift of timing or routing into holiday, not more annual volume.
5. **Market comparators.** US footwear imports Jul-Aug 2026 -1.4% YoY (Aug estimated), -7.6% vs 2024. Clean visible peer consignees (adidas, ASICS, Brooks, New Balance, On, Vans) Jul-Sep median -19% YoY, -2% vs 2024; their holiday loading ratio fell from 1.09 to 0.94.
6. **Logistics context.** NIKE Retail Services filed WARN notices on Jan 26-27, 2026 for 583 workers at two Memphis DCs and 193 at Byhalia MS, effective Apr 3, 2026. Nike called it consolidation of domestic DC operations plus automation (FreightWaves, Bloomberg). Nike NA inventory was $3,491M at Aug 31, 2026, -0.9% YoY (Q1 FY27 10-Q, repo). Neither says Nike is cutting or rebuilding Q3 inbound.

## Pre-registered tests (rules written in the data README before computing)

| Test | Rule | Nike-linked | Benchmark | Result |
|---|---|---|---|---|
| T1 Converse Jul-Sep YoY vs clean peer median | SHORT if more than 10 pts below | -28.0% | -19.0% | NEUTRAL (gap -9.0 pts) |
| T1b Converse vs 2024 (supplementary) | same | -44.6% | -2.0% | SHORT |
| T2 Nike brand visible proxies | LONG if Nike Canada and factory leaks rise, beat market, and 3+ of 6 strict factory names rise without visibility-break names | Nike Canada +92.9%; strict factories without break names +18.3% (115 to 136 BOLs); 2 of 3 clean names rise; Feng Tay Taiwan, the purest Nike name, -33% (95 to 64) | US footwear imports -1.4% | INCONCLUSIVE (breadth test fails) |
| T3 Holiday loading (Jul-Sep avg / Jan-Jun avg) | LONG if Nike-linked ratios rise while peers fall | Nike Canada 0.58 to 1.50; strict factories 1.29 to 1.24; Converse 0.81 to 1.59 | peers 1.09 to 0.94; market 1.09 to 1.11 | LONG-leaning, weak |

## How to use this in the pitch

- **Short side:** Converse inbound -53% YTD and -45% vs 2024 confirms the Converse decline is volume, not price. That is already in guidance.
- **Long side:** nothing in visible shipments shows Nike starving the holiday pipeline. Nike-linked arrivals are, if anything, loaded later into the year than in 2025, while peers loaded less. But the samples are tiny and prone to visibility breaks, so treat this as "no evidence of a cut", not as evidence of a rebuild.
- **Do not claim** a Nike monthly shipment count for 2023 to 2026, or a 2019-2020 baseline. Neither exists in free data. A paid PIERS, Panjiva or ImportGenius search on "FOOTWEAR DIVISION OF GOODS", "OCM-CTP" or notify party Expeditors Portland would be the next step.

## What was blocked

Census API (needs a key, so an email registration), OEC port/district/state cubes (authorization), USA Trade Online and USITC DataWeb (login), Seair, Volza, ExportGenius, ImportYeti and Eximpedia (Cloudflare 403), ImportInfo HTML pages and search (bot challenge; robots.txt disallows search), ImportGenius search (robots.txt) and monthly charts (paid), ImportGenius Vietnam data (ends by early 2024), JOC Top 100 importers (paywall), and company-level import data for Nike Europe, Japan and China (none public).
