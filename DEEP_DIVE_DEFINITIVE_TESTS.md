# Deep dive: definitive tests of Nike's supply cut and full-price recovery

**Started:** October 13, 2026. **Status:** live document, updated and committed as each test reports. **Why this exists:** the review-tone test (`research_notes/thesis_tests/review_tone_jin2023.md`) came back inconclusive because it measured a proxy (how buyers feel) instead of the quantities that decide the thesis (pairs, price, stock left, time to markdown), and it had no control group. Every test here is designed to (1) measure the quantity directly, (2) compare a treated group with a control group or a before with an after, and (3) state in advance what result would prove the thesis wrong.

**The two questions every test feeds:**
1. **Supply or demand?** Is Nike's decline in Jordan and lifestyle footwear a deliberate supply cut that will restore full-price selling, or lower full-price demand that supply cuts will not fix (`research_notes/12_jordan_brand_thesis.md`)?
2. **Is full-price recovery on track?** Does the evidence support the timing the share price needs (12% to 14% EBIT margin by FY2031 at a 10% WACC; `research_notes/thesis_tests/consensus_and_valuation.md`), or has it slipped (`research_notes/16_full_price_recovery.md`)?

Labels follow the house rules (`CLAUDE.md`): filing citations with printed pages, *Nike transcript*, *Nike release*, *secondary*, *data provider*, *market data*, *my arithmetic*, *my inference*. Findings marked **[KEY FINDING]** are the strongest, best-sourced results and are candidates for the pitch.

## Headline findings

1. **[KEY FINDING] The supply-cut signature appears only where Nike is shrinking the business, not where the Jordan cut is aimed** (Test 5). Greater China (units -26%, ASP flat on lower discounts) and Converse (units -34%, ASP +6 points) show units cut at stable prices in Q1 FY2027. North America, the focus of the Jordan retro cut, sold 2% more footwear pairs at lower ASP, and EMEA cites higher discounts (Q1 FY27 10-Q pp. 26 to 28). All 694 unit and price statements Nike filed since FY2017 are in `data/definitive/nike_units_asp_tidy.csv`.
2. **The FY2018 "supply reset" began with discounting** (Test 5). North America footwear units were flat while discounts cut 3 points off revenue in Q1 FY2018 (Q1 FY18 10-Q p. 26); units fell only in the next two quarters. The FY2018 analog for Jordan is a discount-then-cut sequence.

## Test 1. Factory orders: Nike's footwear suppliers' monthly revenue and pairs

- **Measures:** production volume and price per pair at the factories that make Nike's shoes, reported monthly in exchange filings, months before Nike reports.
- **Treated vs control:** Nike-dependent suppliers vs suppliers serving other brands; FY2018 reset vs today.
- **Would disprove "deliberate supply cut":** supplier pair volumes flat or rising while Nike's revenue falls (stock building somewhere), or no cut in volumes before Nike's revenue fell.

*(Pending.)*

## Test 2. Time to markdown for each new release

- **Measures:** days from release to first discount, and discount depth, for each Jordan retro and key lifestyle release, on nike.com and major retailers.
- **Treated vs control:** release cohorts 2023, 2024, 2025, 2026; models Nike cut (AJ1 High) vs models it expanded (AJ3, AJ4).
- **Would disprove "full-price recovery":** 2026 releases reach markdown as fast as or faster than 2024 releases.

*(Pending.)*

## Test 3. Size runs left after launch

- **Measures:** which sizes remain in stock days and weeks after a release at nike.com, Foot Locker, Finish Line and JD. Broken size runs mean sold through; full size runs mean oversupply.
- **Treated vs control:** holiday 2026 retros (after the October 2026 cut) vs earlier releases.
- **Would disprove "supply cut is working":** full size runs still in stock two to four weeks after holiday 2026 launches.

*(Pending.)*

## Test 4. Resale panel: the same shoes re-priced over time

- **Measures:** resale price to retail for the same 247 shoes at several dates (historical captures plus the October 13, 2026 baseline in `data/jordan_resale_goat_20261013.csv`), and the depth of sellers listing each shoe.
- **Treated vs control:** AJ1 High (supply cut from 2024) vs AJ3 and AJ4 (supply raised): difference in differences.
- **Would disprove "scarcity works":** AJ1 premiums do not improve relative to AJ3 and AJ4 after the cut.

*(Pending.)*

## Test 5. Units vs price from Nike's own filings

- **Measures:** every footwear and apparel unit and average selling price change Nike states in its 10-Qs and 10-Ks, by segment and quarter, FY2017 to Q1 FY2027.
- **Treated vs control:** reset periods (FY2018, FY2025 to FY2027) vs normal periods; North America vs Greater China.
- **Would disprove "deliberate supply cut":** units falling only after ASP falls (discounting first), or units flat while revenue falls.

**Result (Oct 13, 2026).** Every unit and ASP statement in all 10 10-Ks and 30 10-Qs from FY2017 to Q1 FY2027 was extracted: 694 rows by quarter, segment and category, each with filing, printed page and verbatim quote (`data/definitive/nike_units_asp_tidy.csv`; episode tags in `data/definitive/units_asp_episode_patterns_DERIVED.csv`; scripts in `scripts/definitive/units_asp/`). In Nike's filings "ASP" is usually the percentage-point contribution of price per pair to revenue growth, not a percent change.

Footwear, units change % / ASP contribution in points:

| Period | North America | Greater China | NIKE Brand | Converse | Source |
|---|---|---|---|---|---|
| Q1 FY18 | 0 / -3 (discounts) | +13 / -3 | +3 / -2 | -17 / 0 | Q1 FY18 10-Q pp. 22 to 31 |
| Q2 FY18 | -11 / +4 | +17 / 0 | 0 / +3 | -12 / +5 | Q2 FY18 10-Q |
| Q2 FY22 | +7 / +6 | -20 / -5 | -7 / +6 | +5 / +9% | Q2 FY22 10-Q |
| Q2 FY23 | +37 / +2 | +15 / +6 | +28 / +8 | +6 / +5% | Q2 FY23 10-Q |
| Q2 FY24 | -17 / +12 | +3 / 0 | -6 / +6 | -13 / 0% | Q2 FY24 10-Q |
| Q1 FY25 | -15 / +1 | -1 / -1 | -10 / 0 | -11 / -3% | Q1 FY25 10-Q p. 25 (NA) |
| Q2 FY25 | -6 / -8 (discounts) | -9 / -5 | -7 / -5 | -12 / -6% | Q2 FY25 10-Q |
| Q2 FY26 | +14 / -5 (channel mix) | -20 / 0 (lower discounts) | 0 / -1 | -26 / -5% | Q2 FY26 10-Q p. 32 (GC) |
| Q1 FY27 | +2 / -1 | -26 / 0 (lower discounts) | -5 / -1 | -34 / +6 (lower discounts) | Q1 FY27 10-Q pp. 26 to 28 |

Verdict by episode (my inference from the table):
- **FY2018 started with discounting, not a supply cut.** "Unit sales of footwear for the first quarter of fiscal 2018 were flat, while lower ASP per pair reduced footwear revenues by approximately 3 percentage points primarily due to lower full-price ASP, driven by product mix and higher discounts" (North America, Q1 FY18 10-Q p. 26). Units fell only in Q2 and Q3 (-11%, -9%) with ASP rising. **So the FY2018 analog used for Jordan was a discount-then-cut sequence, not a pure supply cut.**
- **FY2023 glut: volume clearance first, cut second.** North America footwear units rose 10%, 37% and 26% in Q1 to Q3 FY2023; the cut came in Q1 and Q2 FY2024 (units -10%, -17%, ASP +8 and +12 points).
- **FY2025 to Q1 FY2027, North America: units fell first** (Q1 FY2025 units -15%, ASP +1 point "due to strategic pricing actions, partially offset by higher discounts", Q1 FY25 10-Q p. 25), then discounting (Q2 FY2025 ASP -8 points), then **more units at lower ASP in FY2026** (+5% to +14% units, -5 points), mainly from channel mix toward wholesale.
- **[KEY FINDING] Only Greater China and Converse show the deliberate supply-cut signature now.** Greater China: "Unit sales of footwear decreased 26%, while ASP per pair was flat as lower discounts were offset primarily by channel mix" (Q1 FY27 10-Q p. 28), after "Unit sales of footwear decreased 20%, while ASP per pair was flat as channel mix was offset by lower discounts" (Q2 FY26 10-Q p. 32). Converse: units -34% with ASP +6 points on lower discounts in Q1 FY2027. **North America, the region the Jordan retro cut targets, is still selling more pairs at lower prices**, and EMEA footwear cites "channel mix and higher discounts" (Q1 FY27 10-Q p. 27).

What this test cannot separate: units falling with flat or rising ASP is consistent with a deliberate shipment cut *and* with buyers taking fewer pairs at higher prices. Tests 1 to 3 (factory pairs, time to markdown, size runs) are designed to split those.

## Log

| Date | Change |
|---|---|
| 2026-10-13 | Document created; five tests launched. |
| 2026-10-13 | Test 5 (units vs price) reported: 694 filing statements, two key findings. |
