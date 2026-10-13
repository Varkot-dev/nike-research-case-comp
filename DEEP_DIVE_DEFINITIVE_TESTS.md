# Deep dive: definitive tests of Nike's supply cut and full-price recovery

**Started:** October 13, 2026. **Status:** live document, updated and committed as each test reports. **Why this exists:** the review-tone test (`research_notes/thesis_tests/review_tone_jin2023.md`) came back inconclusive because it measured a proxy (how buyers feel) instead of the quantities that decide the thesis (pairs, price, stock left, time to markdown), and it had no control group. Every test here is designed to (1) measure the quantity directly, (2) compare a treated group with a control group or a before with an after, and (3) state in advance what result would prove the thesis wrong.

**The two questions every test feeds:**
1. **Supply or demand?** Is Nike's decline in Jordan and lifestyle footwear a deliberate supply cut that will restore full-price selling, or lower full-price demand that supply cuts will not fix (`research_notes/12_jordan_brand_thesis.md`)?
2. **Is full-price recovery on track?** Does the evidence support the timing the share price needs (12% to 14% EBIT margin by FY2031 at a 10% WACC; `research_notes/thesis_tests/consensus_and_valuation.md`), or has it slipped (`research_notes/16_full_price_recovery.md`)?

Labels follow the house rules (`CLAUDE.md`): filing citations with printed pages, *Nike transcript*, *Nike release*, *secondary*, *data provider*, *market data*, *my arithmetic*, *my inference*. Findings marked **[KEY FINDING]** are the strongest, best-sourced results and are candidates for the pitch.

## Headline findings

*(Filled in as tests report.)*

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

*(Pending.)*

## Log

| Date | Change |
|---|---|
| 2026-10-13 | Document created; five tests launched. |
