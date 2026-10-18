# Nike (NYSE: NKE): equity research for the case competition

**Status as of October 18, 2026.** Submission is Nov 1, finals are Nov 19, and Nike's Investor Day is Nov 16 to 17. No financial model has been built yet. Everything below comes from filings, free data and labelled team arithmetic. Every number in this README links to a note that carries its source, and every note says which claims were opened at the source (OPENED), seen only in a search summary (SNIPPET), or computed by us (DERIVED).

---

## 1. The call in one paragraph

**Lean SHORT, low to moderate confidence.** At about $35.30 the stock needs Nike's operating (EBIT) margin to get back to roughly **11% to 14% by FY31**. FY26 was 8.3% reported (6.2% without a one-time tariff refund), FY27 is guided lower, and FY28 consensus is about 7.2%. Base rates say the most likely FY31 margin is **about 9%**. Among 73 US companies that fell this far below their own average margin, only about **one in five** regained 3.3 points within five years. At a 9.4% margin, the same discounted cash flow model that sets the 11% to 14% bar gives **$24 to $28 a share**. We searched hard for a single decisive fact (30 forensic hunts and 7 deep dives) and **did not find a smoking gun**. The short rests on several pieces of evidence that point the same way.

---

## 2. Key numbers

| Item | Value | Source note |
|---|---|---|
| Share price | about $35.30 (Oct 14, 2026) | `research_notes/Niche sources/N9_options_investor_day.md` |
| FY26 revenue | $46.4B (FY24 peak $51.4B) | `REPORT.md` section 5 |
| FY26 EBIT margin | 8.3% reported, 6.2% ex one-time tariff refund (FY24 12.7%) | `research_notes/Deep dives Oct 14/D1_fy28_bridge.md` |
| FY27 guide | Revenue down high single digits; adjusted EPS $1.15 to $1.35 | Q1 FY27 call transcript, `data/hunt/earnings_calls/transcripts/Q1FY27.txt` |
| FY28 consensus EPS | $1.617, down 26.6% in 30 days (28 cuts, 0 raises) | `research_notes/Wave 3/W7_revision_dynamics.md` |
| P/E on FY28 | about 21.5x vs peer median 13.2x | `research_notes/Deep dives Oct 14/D5_valuation.md` |
| EV/Sales, EV/EBITDA | 1.20x and 11.3x, about the peer median | same |
| Margin the price needs | about 11% to 14% by FY31 (9% to 10% cost of capital) | `research_notes/Thesis decision/dig_1.md`, `D5_valuation.md` |
| Base-rate expected FY31 margin | about 9.0% to 9.4% | `research_notes/Niche sources/N8_literature_base_rates.md`, `N8_check.md` |
| Value at 9.4% margin | $24.18 (10% WACC) to $27.75 (9% WACC) | `N8_check.md` |
| Options-implied Investor Day move | 1 standard deviation about 4.2% to 4.9%; market odds of a 10% drop about 6% | `N9_options_investor_day.md` |

---

## 3. Why we lean short (the evidence that survived checking)

1. **The price needs a margin Nike has not earned since FY24.** On sales and EBITDA Nike already trades like an average peer. The whole premium on earnings is a bet that margin comes back. Base rates (Mauboussin and Callahan, *The Base Rate Book*, p. 62) and a 73-company SEC panel put the odds of reaching 11.6% at about 16% to 24%, and brand leaders did no better (1 of 11). (`N8`, `N8_check`)
2. **Volume has not grown in seven years.** Nike footwear units are flat versus FY19 while revenue per pair is up 22%. Since the FY23 peak, units are down 10.7%, and price turned negative in FY25 (-3 points), FY26 (-1) and Q1 FY27 (-1), with Q1 FY27 units down 5%. All from Nike's own 10-K unit and price disclosures. (`research_notes/Smoking gun hunt/G3_units_factories.md`)
3. **Nike's own history says this kind of slump is slow.** Shocks (2009, 2020) and the 1987 Air Jordan rebound recovered in 1 to 2 years. Cost-structure slumps (FY94, FY98) left EBIT margin below the old peak for 9 or more years. Today matches FY98: since FY21, rising selling and admin costs explain 5.5 of the 7.3-point margin fall. (`research_notes/Niche sources/N3_nike_history_analogs.md`)
4. **Marketing cost is high and sticky.** Demand creation is 10.5% of revenue against 8.3% in FY24, worth 216 basis points of margin; about $1.7B a year is locked into endorsement contracts; Nike's share of US brand search kept falling (46.6% in 2023 to 38.1% in 2026). (`research_notes/Wave 3/W9_ad_spend.md`)
5. **Share loss where markets still grow.**
   - China: Nike fell from #1 to #3 on Tmall sports rankings (11.11 2025 and 618 2026, behind adidas and FILA); its two largest partners closed 26% of doors in three years; our Q2 FY27 China estimate is down about 23% (range -19% to -32%). (`N5`, `Long or short cruxes/china_doors.md`, `Wave 3/W5_china_nowcast.md`)
   - Europe: Nike has trailed the European peer median by 14 to 18 points for eight quarters. (`Deep dives Oct 14/D3_europe_converse.md`)
   - Digital: nike.com visits fell 11.4% year on year in August 2026 while adidas.com rose 12.5%, so the digital decline is lost demand, not only a deliberate cut. (`Smoking gun hunt/G6_web_traffic.md`)
   - Running: at Japan's Hakone Ekiden relay, Nike's share of runners fell from 95.7% (2021) to 16.7% (2026); Running USA's 2026 survey has Nike as favorite racing shoe down 4.2 points. (`Niche sources/N7_amateur_running_counts.md`)
6. **Factories see no rebound.** Feng Tay (about 90% Nike) says "Nike momentum is flat" and 2027 orders are still being negotiated; implied Nike orders were down about 10% to 12% in July to September 2026, while On's main supplier grew 33%. (`Wave 3/W3_supplier_order_guidance.md`)
7. **Disclosure is shrinking.** Nike withdrew 16 KPI-type disclosures in the last nine quarters against about 5 in the prior 24; 11 of the 12 with a clear direction were deteriorating when pulled. We describe this as a pattern, not as hiding. (`Smoking gun hunt/G11_disclosure_withdrawal.md`)

---

## 4. What argues against the short (be ready for these in Q&A)

- **The Street already cut FY28.** At $1.617, consensus is only 3.6% above our filing-based bear case, so "FY28 is too high" is mostly priced in. The argument that remains is the long-run margin. (`W7`, `D1`)
- **Cost of capital decides it.** At an 8% WACC a 9.4% margin is worth about $32.50, only 8% below the price. The short needs 9% or more. (`N8_check`)
- **Real recoveries exist.** adidas went from 6% to 11.3% margin (2014 to 2019) and from 1.3% to 8.3% (2023 to 2025); Ralph Lauren rebuilt from 8% to 14.5%. (`N8_check`)
- **Product pipeline is rebuilding.** Nike filed 21 trademarks for new product names in January to September 2026, against a prior 15-year high of 7, and its share of new models in release calendars rose from 9% to 47% since 2023. Most of the newness so far is basketball and Jordan, and only 3 of the 21 names are confirmed new footwear. (`Smoking gun hunt/G7_ip_pipeline.md`, `Wave 3/W8_launch_newness.md`)
- **Guidance is conservative.** Nike landed inside or above its guided range on revenue and gross margin 16 of 16 times in eight quarters. Q1 FY27 revenue was the first below the midpoint. (`Smoking gun hunt/G9_guidance_record.md`)
- **No financial stress.** Bonds price Nike as a solid single-A; the balance sheet covers the dividend for years; no financial covenants. (`G5_credit_market.md`, `Deep dives Oct 14/D6_dividend_cash.md`, `Wave 3/W1_internal_targets.md`)

---

## 4A. Is the plan working? Execution speed from alternative data

We tracked 17 free alternative-data indicators across Nike's plan pillars (each with a baseline, the latest reading and the pace per quarter). The indicators were rebuilt from Common Crawl and Wayback captures, the Nike store locator, HKEX partner filings, retailer earnings calls and job postings.

**What Nike controls directly is moving fast:**
- Air Force 1 products on nike.com fell from 172 to 53 (2023H1 to 2026H1), and Dunk from 69 to 31.
- Nike-owned in-line stores fell from 135 to 96 (Feb 2025 to Oct 2026).
- Doors at Nike's two largest China partners fell from 8,468 to 7,322 in 18 months.
- Sales roles rose from 7% to 16% of corporate job postings.

**The market's response is flat or moving the wrong way:**
- nike.com product pages showing a discount rose from 22.6% to 36.0% (Q3 2024 vs Q3 2026).
- The nike.com sale page grew from 3,927 to 4,831 products.
- Nike and Jordan's share of Foot Locker sale items is unchanged at about 37%.
- Nike's share of Running Warehouse road-running styles slipped from 10.4% to 9.6%.

**Counterpoint for Q&A:** DICK'S management's tone on Nike turned more positive, with no negative sentences across six calls.

Management's promise record under Hill: 4 of 8 resolved promises kept or beaten, with 5 pending (2 at risk).

Read the per-table caveats first: most sources are page samples, not full counts. (`research_notes/23_execution_speed_altdata.md`; Excel workbook `data/execution_speed/nike_execution_speed.xlsx`)

---

## 5. Claims we checked and dropped or corrected

| Claim that appeared earlier | What the checking found |
|---|---|
| "Channel stuffing" in North America | Not supported. The wholesale surge is channel mix, retailer consolidation (DICK'S/Foot Locker, JD/Hibbett) and a refill of the FY25 destock. (`D2`, `G2`, `W6`) |
| Reserve releases explain the guidance beats | Rejected by a skeptic check: a pre-announced base effect, not separable from usage. (`G12_check.md`) |
| "Teen mindshare fell from 61% to 46%" | Mixes two survey groups. Like-for-like the decline has flattened (56, 51, 45, 46). (`N1_brand_health_panel.md`) |
| "Premium is unjustified" | Mostly trough earnings; at FY24 margins Nike would trade 8% below peers. (`D5`) |
| "Dividend cut is likely" | Balance sheet covers it for years; a freeze is plausible, a cut is not a thesis. (`D6`) |
| "Met or beaten 14 of 14" / "22 of 22" | Replaced by the 16 of 16 inside-range sentence above. (`G9`) |
| FY25 purchase obligations of $7.9B | A filing error; Nike corrected it to about $5B. (`G1`) |

---

## 6. Dates that matter

| Date | Event | Supports the short if | Supports a long if |
|---|---|---|---|
| Oct 21 to 28 | Topsports quarterly update and interim results | China sales low-teens down or worse | Mid-single-digit decline or better |
| About Nov 10 | Feng Tay and Pou Sheng October revenue | Feng Tay worse than -8% (two-year, USD) | Feng Tay better than -3% |
| Nov 14 to 20 | Dividend declaration | Cut | Large raise |
| **Nov 16 to 17** | **Nike Investor Day** | No dated margin target, or one below about 12%. CFO Denton set 0 of 7 targets above consensus at Lowe's, CVS and Pfizer (`Wave 3/W2_denton_playbook.md`) | Dated EBIT margin target of 13% or more with a bridge |
| Nov 19 | Finals | | |
| Nov 30 | Belgian customs hearing (EUR 1.5B claim per Belgian press, unreserved by Nike) | Adverse ruling: $0.23 to $0.36 one-time EPS in the base case | Nike wins |
| About Dec 17 | Q2 FY27 results | Gross margin below 40.6% | Gross margin above 41% with pricing positive |

**How to express the short:** a Nov 20 $35/$30 put spread costs about $1.31 per share and breaks even about 4.6% lower. It has limited loss, which matters because the short interest is high (8.2% of tradable shares) even though it is not a squeeze setup. (`N9`)

---

## 7. What we still need (and could not get for free)

1. **Analyst margin consensus beyond FY28** (I/B/E/S, FactSet or Visible Alpha). Refinitiv access through Penn was denied; WRDS or Bloomberg may work. See `research_notes/Refinitiv pull list.md`.
2. **Sales to shoppers by brand** (Circana or Euromonitor). Filings show only what Nike ships to stores.
3. **A financial model.** Next step: a margin bridge to FY31 and a price target built on the base-rate case.

---

## 8. Where to read more (in this order)

| Start here | What it is |
|---|---|
| `slides/pptx/Nike Short Thesis.pptx` | 15-slide editable deck with the current pitch |
| `REPORT.md` section 11A | One-page summary of the long vs short decision inside the full report |
| `research_notes/Smoking gun hunt/00_HUNT_SYNTHESIS.md` | Twelve forensic hunts (units, receivables, reserves, disclosures, traffic, patents, credit, tax, litigation, Belgian customs) |
| `research_notes/Niche sources/00_NICHE_SYNTHESIS.md` | Nine unusual sources (base rates, Nike history, China festivals, race shoe counts, options, subsidiaries) |
| `research_notes/Wave 3/00_WAVE3_SYNTHESIS.md` | Management targets, suppliers, China nowcast, retailers, consensus, launches, ads |
| `research_notes/Deep dives Oct 14/00_SYNTHESIS.md` | FY28 bridge, North America, Europe and Converse, long case and judge Q&A, valuation, dividend, Investor Day study |
| `research_notes/23_execution_speed_altdata.md` | Execution speed: 17 alternative-data indicators by plan pillar, with an Excel workbook in `data/execution_speed/` |
| `research_notes/22_margin_by_business_and_mix.md` | Margin by channel, region, product and Jordan, with revenue mix; wholesale about 31% to 37% vs Direct about 59% to 63% gross margin |
| `research_notes/Long or short cruxes/00_SCOREBOARD.md` | The original eight long vs short questions and grades |
| `RESEARCH_MAP.md` | Register of every research topic, owner and output file |
| `REPORT.md` | Full report: financials, charts, leadership, valuation |
| `data/` | Cleaned data with READMEs and scripts; `data/nike_filing_facts.csv` holds 6,281 filing facts with page cites |
