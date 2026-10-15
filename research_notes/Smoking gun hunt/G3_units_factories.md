# G3: Unit volumes, ASP and the factory base (smoking-gun hunt)

Run date: October 15, 2026. Owner: G3 lane of the smoking-gun hunt (RESEARCH_MAP.md row G3). Builder scripts: `scripts/hunt_g3_build.py` and `scripts/hunt_g3_pull_comtrade_annual.py`. All CSVs sit in this folder with the prefix `G3_`. Tags: OPENED (read on the page or file), SNIPPET (seen only in a search result), DERIVED (my arithmetic from OPENED inputs).

## 1. Bottom line

**Smoking gun: no, not a hidden fact. But a sharper, filing-backed unit and price decomposition than the repo had, with three findings that matter for a short on FY28 expectations.**

1. **The brief's premise is wrong in a useful way.** Nike's 10-Ks and 10-Qs do report units, as a percentage change, for NIKE Brand footwear and apparel every year (and in the 10-Q, every quarter), with the ASP contribution in percentage points. The Impact Reports do not report annual pairs or units at all (one level only: "more than 1 billion units" shipped in FY15). The unit series below therefore comes from the filings, 12 years deep (FY15 to FY26) plus 13 quarters. Levels (millions of pairs) are never disclosed. OPENED, all pages cited in `G3_nike_units_asp_annual.csv`.
2. **Footwear volume is back at its FY19 level, and every dollar of growth since is price.** FY19 to FY26: units -0.1% (band -3.5% to +3.5% from rounding), reported revenue +21.9%, so revenue per pair +22.0% (currency-neutral ASP +27.2%). DERIVED.
3. **The price gains are now reversing while volume is still falling, and the near-term trend is down, not up.** FY24 to FY26: units -8.9%, revenue -11.7%, revenue per pair -3.0% (cn ASP -4.2%). Quarterly footwear units: Q1 FY26 +2%, Q2 0%, Q3 -2%, Q1 FY27 -5% (ASP -1 point), so currency-neutral footwear revenue is -6% in the latest quarter. OPENED (10-Q pages) for each quarter.

Pre-registered test (from the task): "volume cut deeper than revenue decline means ASP is up and the recovery is price; shallower means price is falling." Result by window, footwear:

| Window | Units | Reported revenue | Revenue per pair | Reading |
|---|---|---|---|---|
| FY19 to FY23 | +11.9% | +36.8% | +22.2% | growth was one-third volume, two-thirds price |
| FY23 to FY26 (unit peak to now) | -10.7% (band -12.1 to -9.3) | -10.9% | -0.2% | volume cut equals revenue cut; ASP flat |
| FY24 to FY26 (revenue peak to now) | -8.9% (band -9.9 to -8.0) | -11.7% | -3.0% | volume cut is shallower than revenue; price is falling |
| FY25 to FY26 | -1.0% | +0.1% | +1.1% | flat reported revenue; see FX below |
| FY19 to FY26 | -0.1% | +21.9% | +22.0% | all price |

Source: `G3_nike_units_windows.csv`. Apparel is the opposite case: FY23 to FY26 units -12.7% (band -14.0 to -11.3) against revenue -2.8%, revenue per unit +11.3% (volume cut deeper than revenue; price carried it). The footwear and apparel stories differ, and the apparel price premium is the part that has not yet unwound (FY25 ASP flat, FY26 +1 point).

**FX hides the FY26 footwear decline.** FY26 footwear reported revenue was $29,525M vs $29,510M (+0.1%, FY26 10-K p. 32), yet currency-neutral revenue was -2% (units -1%, ASP -1 point, p. 33). The gap is about 2 points of foreign-currency tailwind, roughly $0.6B (DERIVED: 2.0% of $29.5B). "Footwear stabilized" is true only in dollars.

## 2. The unit and ASP series (NIKE Brand footwear)

Identity checked for every year: units % + ASP points = currency-neutral revenue growth (column `check_units_plus_asp_minus_cn` is 0 in all 24 product-years). Note that the ASP points are on a wholesale-equivalent basis from FY21 (10-K wording), so DTC price effects are translated to wholesale.

| FY | Units | ASP pts | cn growth | Revenue $M | Units idx (FY19=100) | Rev per pair idx (reported) |
|---|---|---|---|---|---|---|
| FY15 | +9 | +8 | +17 | 18,318 | 77.8 | 97.2 |
| FY16 | +9 | +6 | +15 | 19,871 | 84.8 | 96.7 |
| FY17 | +7 | +1 | +8 | 21,081 | 90.8 | 95.9 |
| FY18 | +2 | +2 | +4 | 22,268 | 92.6 | 99.3 |
| FY19 | +8 | +4 | +12 | 24,222 | 100.0 | 100.0 |
| FY20 | -8 | +6 | -2 | 23,305 | 92.0 | 104.6 |
| FY21 | +11 | +7 | +18 | 28,021 | 102.1 | 113.3 |
| FY22 | -3 | +7 | +4 | 29,143 | 99.1 | 121.5 |
| FY23 | +13 | +7 | +20 | 33,135 | 111.9 | 122.2 |
| FY24 | -2 | +3 | +1 | 33,427 | 109.7 | 125.8 |
| FY25 | -8 | -3 | -11 | 29,510 | 100.9 | 120.7 |
| FY26 | -1 | -1 | -2 | 29,525 | 99.9 | 122.0 |

Sources (OPENED): FY16 10-K p. 23-24 (FY15, FY16), FY17 10-K p. 23-24, FY18 10-K p. 22-23, FY19 10-K p. 27-28, FY20 10-K p. 31-32, FY21 10-K p. 32-33, FY22 10-K p. 32-33, FY23 10-K p. 32-33, FY24 10-K p. 34-35, FY25 10-K p. 33-34, FY26 10-K p. 32-33. Indices are chained from rounded integers, so each cumulative figure carries up to plus or minus 0.5 point of rounding error per year; bands are in `G3_nike_units_windows.csv`.

Quarterly (`G3_nike_footwear_units_quarterly.csv`, three-month figures, OPENED): units +3, +28, +19 (Q1 to Q3 FY23); -1, -6, +2 (FY24); -10, -7, -8 (FY25); +2, 0, -2 (FY26); -5 (Q1 FY27). Q4 quarters are not in any 10-Q. The FY26 sequence +2, 0, -2, then -5 is a monotonic deceleration over four reported quarters.

### Why the footwear units fell, by region (decomposition)

From the regional MD&A in the FY24 to FY26 10-Ks (`G3_footwear_units_by_region.csv`; weights are prior-year regional footwear revenue, an approximation because ASP differs by region; the weighted sums reproduce the reported totals within 0.5 point in all three years):

| Region | FY24 units | FY25 | FY26 | Cumulative FY23=100 | Share of gross unit loss FY23 to FY26 |
|---|---|---|---|---|---|
| North America | -7 | -10 | +6 | 88.7 | about 45% |
| EMEA | -4 | -8 | -2 | 86.6 | about 30% |
| Greater China | +8 | -11 | -14 | 82.7 | about 25% |
| APLA | +6 | -2 | -3 | 100.8 | none (small gain) |

DERIVED shares: contribution = cumulative region change times FY23 revenue weight (45.0%, 24.9%, 16.4%, 13.7%): -5.1, -3.3, -2.8, +0.1 points. North America is the largest absolute contributor to lost footwear units; Greater China is the fastest-falling region (Q1 FY27 footwear units -26%, Q1 FY27 10-Q p. 28, repo fact `gc_footwear_units_change_pct`). North America turned positive in FY26 (+6% units, ASP -1 point), which is the only region where the unit trend has improved. Units here are Nike's recognized unit sales (sell-in to wholesale plus DTC), so the filings cannot separate deliberate supply cuts from lower sell-through. That separation needs retailer or panel sell-through data (Circana, NPD, GfK); it is not in these sources.

## 3. Hypotheses for "volume is flat vs FY19 but revenue is +22%" and what ruled them out

1. *Currency.* Ruled out as the main driver: the 10-K ASP contribution is currency-neutral and sums with units to currency-neutral growth in all 12 years; cn ASP index FY19 to FY26 is +27.2%, larger than the reported +22.0%. FX was a headwind to the cumulative figure, not the source of it (DERIVED).
2. *Mix toward DTC.* Partly true and visible in the 10-K ASP explanations (FY19 to FY24 ASP language cites higher NIKE Direct ASP and DTC growth), but the same language shows full-price ASP and lower discounts. The filings do not quantify the split, so DTC mix versus like-for-like price cannot be separated from these pages. Remains one of two surviving explanations, together with 3.
3. *Pricing actions and fewer discounts.* Consistent with the 10-K text and with Nike's gross margin bridge (full-price ASP added 200 bps to FY24 gross margin, FY24 10-K p. 36, repo fact `gm_driver_full_price_asp_bps`). Survives.
4. *Category or product mix (heavier price-point shoes).* Not testable from these data; flagged as the third unresolved piece. What would decide it: Nike Brand units and ASP by price tier, or Circana price-band shares.
5. *Reversal check on the other side.* Nike's own gross margin bridge cost of lower ASP in FY25 was 180 bps (FY25 10-K p. 35): 1.8% of $46,309M = $834M of gross profit. The 10-K units/ASP data imply a footwear ASP revenue effect of -3 points on FY24 footwear revenue $33,427M = -$1,003M (apparel ASP was flat). The two independent disclosures agree within about 17%, which supports using the 10-K ASP points as a dollar driver (DERIVED).

## 4. Sensitivities (DERIVED, illustrative)

- One point of footwear unit growth is worth about $295M of NIKE Brand footwear revenue at FY26 revenue per pair.
- If FY27 footwear units ran at the Q1 FY27 rate (-5%) with ASP at -1 point, footwear revenue would fall about 6% in currency-neutral terms, roughly $1.8B (6% of $29.5B), and the unit index would drop to about 95 (FY19=100), the lowest since FY20 (92.0).
- If footwear ASP per pair were back at its FY24 level on FY26 units, FY26 footwear revenue would be about $0.9B higher on reported revenue per pair (+3.1%) or $1.3B on currency-neutral ASP (+4.5%). That is the size of the price gain already given back, and the gap that further discounting would widen.

## 5. Factory and worker base

### What is and is not available as a time series

The Manufacturing Map as a time series is not available from the archives reachable here (see section 7). Substitutes that are time series: (a) workers by region FY15 to FY25 from the Impact Reports and Sustainability Data (`G3_workers_by_region_year.csv`); (b) factory counts by product from the 10-K Item 1 (`G3_factory_counts_10k.csv`); (c) one historical map snapshot, found in a third-party GitHub gist, that reconciles to the FY21 Impact Report (`G3_map_snapshot_FY21_thirdparty_copy.csv`).

**Authenticating the FY21 snapshot.** The gist has 528 rows. Its region worker totals are Americas 66,769, EMEA 25,783, N Asia 141,928, S Asia 293,321, SE Asia 528,196, total 1,055,997. The FY21 Impact Report (p. 150 PDF) reports a Tier 1 plus Tier 2 total of 1,055,803 (Americas 66,332, EMEA 26,356, N Asia 140,245, S Asia 293,933, SE Asia 528,937): a 0.02% difference in total and under 2.5% in every region (EMEA -2.2%, N Asia +1.2%, Americas +0.7%). Its finished goods rows sum to 982,719 workers against 980,729 Tier 1 in the report, and its finished-goods-components rows sum to 73,278 against 75,074 Tier 2. So the file is the map as of roughly mid-2021 (a Wayback capture dated 2021-06-15 exists), even though the gist itself is third-party and undated. The 2021-vs-2026 comparison below rests on that reconciliation. Two en-dash characters in factory names were replaced with hyphens in the saved copy; no values were changed.

### Footwear: units, factories and workers

| Measure | FY19 | FY21 | FY23 | FY26 / Oct 2026 |
|---|---|---|---|---|
| 10-K footwear factories | 112 | 191 (older definition) | 123 | 95 |
| Map footwear Tier 1 factories | n/a | 117 (84 finished goods + 33 components) | n/a | 96 (80 Nike, 16 Converse) |
| Map footwear Tier 1 workers | n/a | 621,458 | n/a | 601,092 |
| Units index (FY19=100) | 100.0 | 102.1 | 111.9 | 99.9 |
| Units per 10-K factory index (FY19=100) | 100.0 | not comparable | 101.9 | 117.8 |

Readings (DERIVED): footwear factories fell 23% between FY23 and FY26 (123 to 95) while units fell 10.7%, so average pairs per factory rose about 16%. The October 2026 map shows 96 Tier 1 footwear facilities against the 10-K figure of 95 at May 31, 2026, a consistency check between two independent Nike disclosures. Footwear Tier 1 workers fell 3.3% from mid-2021 to October 2026 while footwear units fell 2.2% (band -4.6% to +0.3%) over the same span, so units per worker are roughly unchanged (+1.1%). Caveat: map "Total Workers" is whole-factory headcount including other brands' production, so this is a consistency test, not a measurement of Nike-dedicated labor.

By country (footwear, `G3_map_by_country_product_FY21_vs_Oct2026.csv`): Vietnam 304,844 to 281,689 workers (-7.6%); Indonesia 177,521 to 223,204 (+25.7%); China 89,491 to 44,407 (-50.4%, factories 33 to 17); India 21,807 to 28,261 (+29.6%). The 10-K production shares move the same way (`G3_footwear_pairs_index_by_country.csv`): the implied China pairs index went from 21.4 (FY21) to 16.0 (FY26), -25%; Indonesia from 24.5 to 27.0, +10%; Vietnam from 52.1 to 52.0, flat (index = 10-K share x units index, FY19 total=100, shares rounded to 1 point). The 10-K Vietnam share fell to 44% in FY22 and recovered to 50% in FY23 (the cause is not stated in the data used here).

### Apparel: units fell, headcount rose

Apparel units FY21 to FY26 -9.2% (band -11.5% to -6.9%) while map apparel Tier 1 workers rose 17.4% (286 to 323 factories; 390,318 to 458,210 workers); the 10-K apparel factory count went from 344 (FY21) to 321 (FY26) on a different definition. Pakistan (+125% workers), Cambodia (+40%), Indonesia (+79%) and Vietnam (+3.5%) account for the increase; China (-27%) and Thailand (-35%) fell. Because worker counts are whole-factory, this shows Nike adding or enlarging apparel suppliers while its own apparel units declined; it does not by itself show excess Nike-dedicated capacity.

### Latest snapshot vs 2019 and vs 2023 (Tier 1 workers by region)

| Region | FY19 (source base) | FY23 (Tier 1) | Oct 2026 map (Tier 1) | vs FY19 | vs FY23 |
|---|---|---|---|---|---|
| Americas | 70,835 | 56,985 | 68,562 | -3.2% | +20.3% |
| EMEA | 22,128 | 35,240 | 37,344 | +68.8% | +6.0% |
| N Asia | 153,645 | 107,104 | 81,138 | -47.2% | -24.2% |
| S Asia | 292,481 | 391,285 | 426,754 | +45.9% | +9.1% |
| SE Asia | 513,023 | 542,660 | 531,754 | +3.7% | -2.0% |
| Total | 1,052,112 | 1,133,274 | 1,145,552 | +8.9% | +1.1% |

The FY15 to FY20 "source base" and the FY21 onward "Tier 1" are different bases (FY20 source base 1,153,199 vs FY21 Tier 1 980,729), so the FY19 column is indicative only. The FY23-to-October-2026 comparison is on one basis. Tier 1 facilities in the current map: 506 (FY25 SASB count 482; FY23 and FY24 454).

Reading: since FY23, Nike's Tier 1 worker base is up 1.1% while footwear units are down 10.7% and apparel units down 12.7% (DERIVED, different measures: whole-factory workers vs Nike units). The shift of workers toward South Asia (+9.1% vs FY23, +46% vs FY19) and away from North Asia (-24% vs FY23, -47% vs FY19) is consistent with the 10-K China share decline (23% FY19 to 16% FY26 in footwear, 18% to 12% in apparel production share FY23 to FY26).

## 6. Cross-checks against suppliers and official statistics

| Check | Result | Verdict |
|---|---|---|
| Yue Yuen (Pou Chen group) pairs, Nike-fiscal-year aligned (`G3_yueyuen_vs_nike_units.csv`) | Correlation of yoy with Nike footwear units -0.22 (n=10). FY25: Yue Yuen +14.0% vs Nike -8%; FY21: -13.2% vs +11% | Not a usable proxy: Yue Yuen covers five named brands (Nike, adidas, Asics, New Balance, Salomon), switched from "produced" to "shipped" in 2019, and its 2021 volumes fell while Nike's rose |
| US imports of sports footwear (HS 640411 + 640219) pairs, Jun-May (`G3_us_sports_footwear_import_pairs.csv`) | World 213.1M (FY24), 255.8M (FY25, +20.0%), 252.8M (FY26, -1.2%); Vietnam +20.1% then -1.7%; Indonesia +46.5% then +22.5%; China +5.7% then -25.2% | All brands, US only. In FY25 industry US sports footwear pairs rose 20% while Nike global footwear units fell 8% and Nike US-heavy North America units fell 10%: Nike lost share of imported US sports footwear (DERIVED, with the caveat that FY25 had tariff-driven front-loading by other importers, flagged in the trade_imports README) |
| Official exports, value (`G3_official_footwear_exports_annual.csv`, UN Comtrade) | Indonesia 2024 $7.28B (+13.1%), 2025 $7.98B (+9.5%); Vietnam 2023 $20.77B (-15.4%); China 2025 $46.18B (-9.4%) | Indonesia's total exports grew while Nike's implied Indonesia pairs index fell (29.6 FY24, 28.3 FY25, 27.0 FY26): Nike under-indexed its Indonesian supply base. Value, not pairs; calendar vs fiscal year. Vietnam is not reported after 2023 |
| Indonesia BPS (via Databoks) | Q1 2025 footwear exports 97,390 tons, US 33,270 tons (OPENED page; BPS table itself paywalled) | Level only, no year-on-year comparison available from the page |
| Vietnam LEFASO | 2025 export value nearly $29B (+5%), FDI 80% of it; capacity 1.3 to 1.4B pairs (OPENED, VnEconomy). The 2024 "1.3B pairs shipped" is SNIPPET only | Used only for scale. If Nike's Vietnam share is 52% of its pairs and Vietnam makes 1.3 to 1.4B pairs, Nike is a minority of Vietnam output; not computable without Nike's pairs level |
| Feng Tay pairs | About 120M pairs in 2025 (+3%) from an AI-extracted third-party summary of its annual report | SNIPPET only; not used. Feng Tay shipments were already analyzed in `data/hunt/trade_imports/README.md` (not repeated here) |

### Impact Report physical proxies: tested and rejected

`G3_proxy_vs_10k_units_correlation.csv` tests nine Impact Report physical series (footwear manufacturing waste tonnes, rubber, EVA foam, leather, polyester and cotton tonnes, Tier 1 footwear Scope 3 emissions, waste per unit, textile dyeing water) against the 10-K unit growth, FY21 to FY25. Correlations range from -0.72 to +0.58, and none reproduces the sign of unit growth in more than 3 of 5 years. For example, footwear rubber tonnage was +13.4% in FY24 (units -2%) and -24.2% in FY25 (units -8%); Tier 1 footwear emissions fell 27% in FY25 on a focus-factory scope (decarbonization and scope changes, not a 27% volume drop). Footwear manufacturing waste was 110,733 t (FY20) and 115,182 t (FY25), nearly flat. The waste-per-unit measure (292 g in FY20 to 262 g in FY25) is a weighted index, so units cannot be backed out of it. Conclusion: the Impact Reports cannot reconstruct a unit series; the 10-K MD&A is the correct source.

Absolute pairs, low confidence: Nike's FY14/15 report gives footwear manufacturing waste of 147 g per pair (FY15, p. 92 PDF). If that ratio still held, FY20 waste of 110,733 t would imply about 753M pairs and FY25 waste of 115,182 t about 784M pairs (DERIVED). Grams per pair are not reported after FY15, and Nike's blended waste per unit index fell about 10% over FY20 to FY25, which would raise the implied pairs. Treat 0.75B to 0.9B as a rough range. It is not used in any conclusion above, which all rest on percentage changes.

## 7. Routes tried for items that came back blocked or partial

Full log: `G3_routes_log.csv`. Summary:

- **Manufacturing Map snapshots 2015 to 2026 (the 2019 and 2023 map files):** the Wayback availability API confirms captures exist (2019-05-25, 2021-06-15, 2023-06-05, 2025-05-31) but every route to the captured content is blocked in this environment (web.archive.org https and http, CDX, r.jina.ai proxy, memento, archive.ph, Common Crawl index, Internet Archive search, Open Supply Hub API needing a token, Scribd, Wikirate, Modaes). Eleven failed routes. One route worked for 2021 (the gist). To obtain the 2019 and 2023 map files: open `https://web.archive.org/web/20190525144238/http://manufacturingmap.nikeinc.com/` and `https://web.archive.org/web/20230605173340/https://manufacturingmap.nikeinc.com/` from a network without this egress policy and save the factory JSON in the page bundle (the same extraction `data/hunt/trade_imports/scripts/parse_nike_map.py` uses).
- **Annual units in the Impact Reports:** 12 documents searched in full text; only one unit level exists (FY15 over 1 billion). Rejected derivations are listed above.
- **Official pairs statistics:** Comtrade quantity is zero for HS 64 totals; BPS, GSO and LEFASO sites are blocked or paywalled. What would settle Vietnam and Indonesia pairs: Vietnam Customs monthly footwear export quantity (pairs) by country, and BPS Indonesia HS 6403/6404 volume tables. Both need a network path to their sites.
- **Feng Tay and Yue Yuen pairs:** Yue Yuen worked; Feng Tay pairs rest on a snippet and were not used.

## 8. What I could not verify

- Nike pairs and apparel units in absolute terms (not disclosed; only the rough 0.75B to 0.9B footwear range above).
- Map snapshots for 2019 and 2023 (archive content unreachable); the FY21 file is third-party and authenticated only by reconciliation to the FY21 Impact Report.
- Quarterly Q4 unit growth (not in 10-Qs); the Q4 FY26 rate can only be bracketed from the full-year -1% and 9M 0% and is not stated here.
- Footwear ASP split between DTC mix, price and discounts (filings state direction, not the split).
- Sell-in versus sell-through: Nike's "unit sales" are recognized sales, so whether the FY25 to Q1 FY27 declines are deliberate supply cuts or weaker end-demand is not separable from these sources. The competing explanations that survive are: (a) deliberate wholesale sell-in reductions to clear inventory, (b) lower consumer sell-through. Data that would decide: Circana or GfK footwear unit sell-through for Nike versus Nike units sold into the channel, quarter by quarter.
- Feng Tay's 120M pairs and the LEFASO 2024 1.3B pairs (snippets).

## 9. Implication for the short thesis

The unit data support the bear case in one specific, measurable way and do not support it in another. Supports: footwear units are only at the FY19 level after seven years, ASP is now falling (-3, -1, -1 points in FY25, FY26, Q1 FY27), and Q1 FY27 (-5%) is the weakest reported quarter since Q3 FY25 (-8%; Q4 quarters are not reported in 10-Qs), with Greater China at -26%; a recovery in FY27 and FY28 revenue would need either units to turn or the 22% price premium over FY19 to hold, and neither is visible in the latest data. Does not support: the volume decline since the FY23 peak (-10.7%) is no deeper than the revenue decline (-10.9%) once FX is counted, so there is no evidence here of a hidden price collapse; price is down only about 3% from the FY24 peak, and apparel price (+11% since FY23) has not unwound at all, which is where further ASP downside would come from if apparel discounting follows footwear.

The run needs the three follow-ups in section 7 (2019 and 2023 map captures, pairs-based export statistics, sell-through data) to move any conclusion above from "consistent with" to "proven".
