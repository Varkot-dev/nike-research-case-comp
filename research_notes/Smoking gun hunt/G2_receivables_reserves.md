# G2: Receivables and reserves forensics. Did Nike push North America wholesale on credit?

Prepared 2026-10-15. Extends `research_notes/Deep dives Oct 14/D2_north_america.md` (inventory, channel mix, retailer inventories) and `research_notes/15_why_nike_discounts.md` (sales-related reserve vs wholesale). Does not repeat them. Data files in this folder: `G2_nike_quarterly.csv`, `G2_nike_annual_reserves.csv`, `G2_peers.csv`, `G2_retailer_dpo.csv`.

Tags: OPENED = read in the cited filing in this session (34 Nike 10-K and 10-Q files from the investors.nike.com mirror, FY2018 to Q1 FY2027, converted with `scripts/sec_pipeline/topages.py`; printed pages). DERIVED = my arithmetic from OPENED inputs. SNIPPET = not used for any number here. Accounts receivable (AR) for all 33 quarter-ends matches `data/nike_filing_facts.csv`, and the reserve balances match `data/discount/sales_related_reserves.csv` (checked by script, zero mismatches).

## 1. Verdict

**Smoking gun: NO, not in the form hypothesized. A weaker, later and unexplained receivables flag: YES.**

1. **The fingerprint of "NA wholesale pushed on extended terms" is absent in the push quarter.** Q2 FY26 (NA wholesale $3,550M, +23.9% YoY, about $690M above run-rate per D2) shows total AR of $5,738M, which is *below* what the prior-year regional DSO mix predicts ($5,914M with FX; residual -$176M, DERIVED, section 5). Wholesale DSO was 68.3 days vs 67.7 (+0.6). If the $690M had been shipped on 30 extra days of terms it would add about $230M to AR on its own. Not there. Q1 FY26 (NA wholesale +10.5%) was the same: wholesale DSO 64.2 vs 64.9 (-0.7).
2. **Sales-related reserves did not rise with the push.** The reserve (returns, post-invoice discounts, claims) fell sequentially in Q2 FY26 ($1,788M to $1,748M, -$40M) when wholesale revenue rose $608M. In the three prior years the Q1 to Q2 move was +$127M to +$360M. Reserve as a share of quarter wholesale: 25.4% (Q1 FY26), 22.9%, 25.1%, 23.5%, 21.4% (Q1 FY27), against 18.0% to 27.9% in FY25. No guaranteed-markdown support is visible in the reserve at shipment. The caveat (section 4) is that an unchanged reserve can also mean under-reserving; the filings cannot tell the two apart because Nike stopped publishing the reserve rollforward after FY24.
3. **What is there: AR stopped following wholesale revenue one quarter after the push.** Wholesale DSO YoY: Q3 FY26 +9.7 days, Q4 FY26 +5.2 (after removing a $684M tariff-refund receivable), Q1 FY27 +4.5. After removing the FX effect (measured two ways, section 5) and mix, Q3 FY26 AR is still about $477M above the regional-mix prediction (6.6 days of wholesale sales, DERIVED). Net of the sales-related reserve, DSO is 51.1 days in Q3 FY26, within 0.3 day of the series high (51.4 in Q2 FY23, the last time NA wholesale surged +37% and Nike then took two years of returns and reserve build).
4. **Cause cannot be separated from filings.** Candidates that survive: (a) late-quarter shipment timing, which is what Nike's own 10-Q says ("higher wholesale revenues and the timing of wholesale shipments", Q3 FY26 10-Q p. 44); (b) retailers paying slower; (c) Nike granting longer terms inside its stated "90 days or less" policy; (d) AR mix toward higher-DSO regions. (b) is argued against by retailer payables (section 6). (a) is supported by trade AR falling $122M in Q4 FY26 and flat in Q1 FY27 (DERIVED). The data that would decide it is NA AR by quarter, which Nike stopped disclosing after the Q3 FY25 10-Q (section 3).

Net for the pitch: do not write "channel stuffing financed by receivables". Writable, with these exact words: "Nike's wholesale receivables days rose 4.5 to 9.7 days YoY from Q3 FY26 to Q1 FY27 (after IEEPA and FX), reaching a net level equal to the series high (51.1 vs 51.4 in Q2 FY23); the same disclosures that would show where (NA receivables by quarter, the returns-reserve rollforward, the dollar allowance) were dropped from the filings in the FY25 reporting cycle."

## 2. Nike quarterly series (Aug 2018 to Aug 2026, 33 quarter-ends; full data in `G2_nike_quarterly.csv`)

Definitions (DERIVED): DSO (total) = AR / quarter revenue x 91. DSO (wholesale) = AR / quarter wholesale revenue (NIKE Brand plus Converse "Sales to Wholesale Customers", from the revenue note of each 10-Q and 10-K; Q4 = fiscal year less nine months) x 91. All AR is attributed to wholesale because NIKE Direct customers pay at the point of sale (revenue note: "Payment is due at the time of sale for retail", FY26 10-K p. 61). AR ex-IEEPA removes the $684M tariff-refund receivable that the FY26 10-K says sits inside Accounts receivable, net at May 31, 2026 (FY26 10-K p. 30 and p. 61).

| Quarter | AR $M (ex-IEEPA) | Wholesale rev $M | NA wholesale YoY | Wholesale DSO | YoY days | Reserve $M | Reserve % wholesale | Net DSO (AR less reserve) | YoY days | CF change in AR $M |
|---|---|---|---|---|---|---|---|---|---|---|
| Q1 FY25 | 4,764 | 6,685 | -10.7% | 64.9 | +5.8 | 1,200 | 18.0 | 48.5 | +1.9 | -312 |
| Q2 FY25 | 5,302 | 7,132 | -1.2% | 67.7 | +8.7 | 1,560 | 21.9 | 47.7 | +2.6 | -631 |
| Q3 FY25 | 4,491 | 6,363 | +2.4% | 64.2 | +4.0 | 1,682 | 26.4 | 40.2 | -3.7 | +779 |
| Q4 FY25 | 4,717 | 6,578 | -8.5% | 65.3 | +10.3 | 1,834 | 27.9 | 39.9 | +0.8 | -93 |
| Q1 FY26 | 4,962 | 7,034 | +10.5% | 64.2 | -0.7 | 1,788 | 25.4 | 41.1 | -7.4 | -215 |
| Q2 FY26 | 5,738 | 7,642 | +23.9% | 68.3 | +0.6 | 1,748 | 22.9 | 47.5 | -0.2 | -806 |
| Q3 FY26 | 5,369 | 6,608 | +10.8% | **73.9** | **+9.7** | 1,658 | 25.1 | **51.1** | **+10.9** | +398 |
| Q4 FY26 | 5,247 (5,931 reported) | 6,774 | +9.8% | 70.5 | +5.2 | 1,589 | 23.5 | 49.1 | +9.2 | -584 |
| Q1 FY27 | 5,242 | 6,948 | +9.0% | 68.7 | +4.5 | 1,488 | 21.4 | 49.2 | +8.1 | +695 |

Sources (OPENED): AR is the balance sheet line "Accounts receivable, net" on printed p. 3 of each 10-Q (Q1 FY27 10-Q: $5,242M vs $5,931M) and FY26 10-K p. 57 ($5,931M vs $4,717M); reserves are the "Sales-related reserves" line in the Accrued liabilities note (Q1 FY27 10-Q p. 7; FY26 10-K p. 67); cash-flow change in AR from the cash flow statement (YTD, differenced; FY26 10-K p. 58 shows -1,207). Wholesale and NA wholesale from the revenue note (Q1 FY27 10-Q p. 14: wholesale $6,948M vs $7,034M; NA $2,981M vs $2,736M).

Reading the table (DERIVED):
- **Seasonality is real.** DSO is lowest in Q4 and highest in Q2 to Q3 every year, so only same-quarter YoY changes are used.
- **FY25 (before the push): DSO rose 4 to 10 days while wholesale revenue fell 3% to 10%.** Reserves built from $1,282M to $1,834M. AR is gross of the sales-related reserve since ASC 606 (FY19 10-K, revenue note: the reserves "were previously reported ... as a reduction to Accounts receivable, net"), so the FY25 AR rise is largely a reserve gross-up plus weak collections on returns-heavy accounts. Net of the reserve, FY25 DSO moved only -3.7 to +2.6 days.
- **Q1 FY26 to Q2 FY26 (the push): DSO flat YoY.** Net DSO -7.4 and -0.2. No receivables fingerprint.
- **Q3 FY26 to Q1 FY27: DSO up, and the reserve fell $24M to $300M YoY.** Gross-up cannot explain it (the gross-up would push AR down as the reserve shrinks). Net DSO +8.1 to +10.9.
- **Cash flow.** The cash-flow AR line equals the balance-sheet change within $30M in each sequential quarter from Q2 FY26 to Q1 FY27, so the rise is real cash not collected, not a reclassification. Q1 FY27 +$695M is the tariff-refund receipt (Q1 FY27 10-Q p. 33: "decreases in Accounts receivable ... primarily due to receipt of the International Emergency Economic Powers Act tariff receivable").
- **Correlation across quarters** (17 quarters, Q4 FY22 to Q1 FY27 excluding Q4 FY26): YoY change in wholesale DSO vs YoY NA wholesale growth r = +0.27; net DSO vs NA wholesale growth r = +0.39 (DERIVED). Weak. The one strong precedent is Q2 FY23 (NA wholesale +36.8%, wholesale DSO +12.1, net +11.1 days) when AR rose with the surge. FY26 repeated the revenue surge without the same-quarter AR response.

## 3. What Nike stopped disclosing (all OPENED, in the FY25 reporting cycle)

| Disclosure | Last shown | Gone from | Why it matters |
|---|---|---|---|
| AR by segment (North America, EMEA, Greater China, APLA, Converse) | Q3 FY25 10-Q, Feb 28, 2025, p. 21 (NA $1,957M) | Q4 FY25 10-K onward (FY25 10-K segment note shows inventories and PP&E only) | The only NA-specific receivables series. Missing exactly for the five push quarters. |
| Schedule II rollforward of sales returns reserve (provision, write-offs) | FY24 10-K p. 97 (provision $3,583M, write-offs $3,325M) | FY25 10-K Item 15 p. 91: "All financial statement schedules are omitted" | Would show whether FY25 and FY26 provisions kept pace with actual returns. Provision was 8.3% of wholesale in FY19 and 12.4% in FY24 (DERIVED, annual CSV). |
| Dollar allowance for uncollectible AR | FY25 10-K p. 64 ($27M vs $35M) | FY26 10-K p. 63 drops the figure; no XBRL tag for FY26 | Allowance history: $30M, $30M, $214M (FY20), $93M, $34M, $35M, $35M, $27M. |

This is a disclosure change, not evidence of misstatement. The only stated reason is generic: "All financial statement schedules are omitted because they are not applicable or the required information is shown in the financial statements or notes thereto" (FY25 10-K p. 91; FY26 10-K Item 15). Possible benign reasons: SEC Schedule II relief when information is in the notes (the FY25 10-K now gives the returns reserve balance in Note 14), and the ASU 2023-07 segment disclosure rewrite. Neither explains removing NA AR.

NA AR before the cut (OPENED, segment note; DERIVED DSO = NA AR / NA wholesale x 91): Nov 2023 59.6, Nov 2024 76.9 (+17.3 days with NA wholesale -1.2%, AR $2,421M vs $1,902M, Q2 FY25 10-Q p. 20), Feb 2024 69.8, Feb 2025 71.3. So the largest NA receivables jump in the record predates the NA revenue surge by a year and coincides with the reserve build (reserve +$430M YoY in Nov 2024), consistent with the ASC 606 gross-up above.

## 4. Reserves and the reserve-based tests

- Balances (OPENED; annual CSV): sales-related reserve $1,218M (May 2019), $1,178M, $1,077M, $1,015M, $994M (May 2023), $1,282M, $1,834M (May 2025), $1,589M (May 2026), $1,488M (Aug 2026). Returns portion: $843M (FY19), $682M, $595M, $525M, $549M, $799M, $1,277M, $1,099M. Estimated cost of inventory for expected returns (asset): $410M (FY19), $313M, $269M, $194M, $226M, $331M, $528M, $511M.
- Discounts and claims (reserve less returns): $375M (FY19), $496M (FY20), $482M, $490M, $445M, $483M, $557M (FY25), $490M (FY26) (DERIVED). Discounts and claims, the line a guaranteed-markdown program would sit in, stayed between $375M and $557M over eight years while wholesale revenue moved between 24,310 and 28,856, and fell from $557M to $490M in FY26. No build during the push.
- Management states true-ups were immaterial: "In fiscal 2026, any variances between actual and expected sales-related reserves were not material to reported Revenues" (FY26 10-K p. 47; the FY25 10-K has the same sentence for fiscal 2025).
- **Under-reserving test.** If the Q2 FY26 pulse needed the normal reserve rate, Q2 FY26 would have added about 22% of the incremental wholesale (Q2 FY25 ratio 21.9%) to the balance, about $150M on $690M. The balance instead fell $40M quarter on quarter. Explanations that survive: (i) FY25 clean-up reserves were being consumed by actual returns and credits (consistent with the cost-of-inventory-for-returns asset staying at $511M to $528M); (ii) reserve rate was cut. The rollforward (additions vs usage) would decide; it is exactly what Schedule II used to show.
- Sensitivity (DERIVED): each 1 percentage point of reserve on quarterly wholesale of $7.0B is $70M of revenue. Restoring the FY25 peak ratio (27.9%) on Q1 FY27 wholesale would require a $450M reserve increase; restoring only the FY24 average (about 17%) would release about $300M. Revenue risk is two-sided.

## 5. Alternatives tested and ruled out

| # | Alternative explanation for the DSO rise | Verdict | Evidence |
|---|---|---|---|
| 1 | **Wholesale-vs-Direct mix mechanically raises DSO** | Ruled out for the wholesale-basis DSO; it does explain part of the total-revenue DSO | Wholesale DSO already divides by wholesale only. On total revenue DSO also rose (+7.0, +4.8, +4.0 days in Q3 FY26 to Q1 FY27), partly because wholesale share of revenue moved from 56.5% to 58.6% (Q3) and from 60.0% to 62.0% (Q1 FY27) (DERIVED). The conclusion above uses the wholesale basis. |
| 2 | **Regional mix** (NA and APLA carry higher DSO than Greater China) | Partly. Does not explain Q3 FY26 | Prior-year same-quarter regional DSO (NA, EMEA, Greater China, APLA, Converse from the segment note) applied to current regional wholesale (`channel_split.csv`), plus FX: predicted AR vs actual ex-IEEPA is -$139M (Q1 FY26), -$176M (Q2 FY26), **+$477M (Q3 FY26)**, **+$967M (Q4 FY26, base May 2024)**, +$130M (Q1 FY27, base Aug 2024) (DERIVED). The Q4 base year has $307M less reserve gross-up than May 2026, so about $660M of the Q4 gap is not reserve. Limit: bases use the last year with segment AR; APLA FX set to zero. |
| 3 | **FX** | Explains $162M of the Q3 FY26 YoY AR rise, not the rest | Two independent measures agree. (a) Balance-sheet change minus cash-flow change in AR, trailing four quarters: Feb 2026 $162M, Nov 2025 $101M, Aug 2025 $38M, May 2026 $7M, Aug 2026 -$17M. (b) Spot rates (Yahoo Finance chart API, market data): EUR/USD 1.040 (Feb 28, 2025) to 1.180 (Feb 27, 2026), +13.5%; CNY +6.5%; JPY -3.8%; applied to the Feb 2025 regional AR mix gives about $172M. Q3 FY26 wholesale DSO +9.7 days becomes about +7.5 days after FX. |
| 4 | **IEEPA tariff-refund receivable** | Explains the whole of May 2026 headline DSO (79.7) and the Q1 FY27 cash inflow | $684M inside AR at May 31, 2026 (FY26 10-K p. 30 and p. 61); $302M already received; "substantially all of the remaining" received after May 31. Removed in all adjusted figures. Any tariff receivable left in Aug 2026 is not quantified (up to about $50M would be 0.7 days). |
| 5 | **Quarter-end timing** (weekends, calendar) | Not supported by the calendar; supported by Nike's wording | Quarter-ends fall on Sat or Sun in both years (Feb 28, 2026 Sat vs Feb 28, 2025 Fri). Nike attributes the AR increase to "higher wholesale revenues and the timing of wholesale shipments" (Q3 FY26 10-Q p. 44) and FY25 to "the timing of wholesale shipments" (FY26 10-K p. 45). Trade AR then fell $122M in Q4 FY26 (5,369 to 5,247) and was flat in Q1 FY27 (5,247 to 5,242) even though Q1 is normally a build quarter (-$215M, -$312M, -$621M cash flow in Q1 FY26, FY25, FY24). Consistent with timing, not proof: monthly shipments are not disclosed. |
| 6 | **Receivables factoring or sale** (would lower, not raise, reported DSO) | Ruled out as a distortion | No mention of factoring, sale of receivables, securitization, non-recourse or credit insurance in any of the 34 Nike 10-K and 10-Q files (full-text search, 0 files). So reported DSO is not flattered by off-balance-sheet sales. |
| 7 | **Nike's supply chain finance program** | Wrong side of the ledger | Disclosed program is for suppliers and sits in Accounts payable: about $1.1B at May 31 and Aug 31, 2026 (Q1 FY27 10-Q Note 13, p. 18); XBRL: $0.84B (May 2024), $1.10B (May 2025), $1.31B (Aug 2025), $0.70B (Feb 2026). It changes DPO, not DSO. No customer-side program is disclosed. |
| 8 | **Longer contractual terms** | Cannot be tested directly; standard terms unchanged in wording | Revenue note, every 10-K FY19 to FY26: wholesale payment "generally required within 90 days or less of shipment" (wording identical FY19 to FY24; FY25 and FY26 add "which may be governed by the country of sale"). Terms of 60 days stretched to 90 would still comply. Q4 FY26 call says nothing on terms; a search of all Nike call transcripts (data/hunt/earnings_calls) for receivable, payment terms, dating, credit risk returns only the tariff receivable. |
| 9 | **Customer credit stress (bad debts)** | Ruled out as a driver | Allowance $27M at May 2025, 0.6% of AR; $35M in FY23 and FY24. The only spike, $214M in FY20, was COVID and was reversed to $93M and $34M. Allowance not disclosed for FY26. |
| 10 | **Deferred revenue or customer deposits** | Not material | "Immaterial amount of contract liabilities" in every filing (Q1 FY27 10-Q p. 14; FY26 10-K p. 84). No contract assets. |
| 11 | **Sell-in revenue was simply higher in the last month of the quarter** | Survives (same as 5) | No data. Needs monthly shipments or Nike's DSO by region. |

## 6. Other side of the transaction: retailer payables (route for payment stretching)

If retailers were paying Nike slowly because sell-through was poor, retailer days payable would lengthen. DPO = AP / quarter COGS x 91 (DERIVED, SEC XBRL; AP covers all vendors, and Nike is about 23% to 31% of DICK'S purchases, per `retailer_sell_through.md`). Data in `G2_retailer_dpo.csv`.

| Retailer | Aug 2025 qtr | Nov 2025 | Jan 2026 | May 2026 | Aug 2026 |
|---|---|---|---|---|---|
| DICK'S (YoY days; Foot Locker included from Sep 2025) | -3.5 | -9.1 | -13.2 | -12.8 | +0.5 |
| Academy | +6.7 | +2.6 | +1.8 | -8.5 | -1.8 |
| Shoe Station (formerly Shoe Carnival) | +1.7 | +5.8 | +15.9 | -0.4 | +0.6 |
| Genesco | -1.7 | -3.8 | -5.6 | +1.5 | +17.2 |
| Foot Locker (last 10-Q Aug 2, 2025) | +4.3 | n/a | n/a | n/a | n/a |

No consistent lengthening across the four retailers that carry the most Nike (DICK'S, Academy). Shoe Station and Genesco are noisy and small. So the evidence leans away from "retailers are stretching Nike" and toward either Nike-side timing or Nike-granted terms. Not conclusive: a retailer can stretch Nike while paying other vendors faster.

## 7. Peers: same ratios (`G2_peers.csv`)

DSO = AR / quarter sales x 91 (DERIVED). Total-sales basis for all (channel splits are dimensional XBRL and were not available); wholesale basis where the release gives it. YoY change in days for the most recent quarters:

| Company | Latest quarters, YoY change in DSO (days) | Wholesale-basis where available | Read |
|---|---|---|---|
| **Nike** (total / wholesale) | Q3 FY26 +7.0 / +9.7; Q4 FY26 +4.8 / +5.2; Q1 FY27 +4.0 / +4.5 | | Above every peer |
| adidas (EUR) | Q3 2025 +5.4; Q4 2025 +2.6; Q1 2026 +1.8; Q2 2026 +0.2 | Q4 2025 +11.6; Q1 2026 +6.4; Q2 2026 +5.8 | Also rising on wholesale basis. AR +16% and +9% vs sales +3% and +2% in Q3 2025 and Q4 2025. adidas cites "higher marketplace receivables" (FY2025 results release, p. 7). Share-gainer, so rising DSO is not unique to a weak seller |
| Puma (EUR) | Q1 2026 -10.3; Q2 2026 -6.5; Q4 2025 +0.4 | Q4 2025 +8.4; Q1 2026 -13.3; Q2 2026 -5.6 | AR falling 19% to 27% as wholesale shrinks 7% to 34%: collecting hard, shipping less |
| Deckers | Jun 2025 +2.1; Sep 2025 -3.0; Dec 2025 +0.9; Mar 2026 -3.7; Jun 2026 -1.7 | n/a | Flat |
| Under Armour | Jun 2025 -2.6; Sep 2025 0.0; Dec 2025 +1.9; Mar 2026 +0.9; Jun 2026 +3.6 | n/a | Slight rise on falling sales |
| Skechers | Jun 2024 +0.8; Sep 2024 +4.2; Dec 2024 +0.8; Mar 2025 +0.7; Jun 2025 -0.4 | n/a | Flat. Last quarter in XBRL is Jun 2025 (no later filing found in companyfacts) |
| On (CHF) | Jun 2025 -9.8 (AR $333.8M vs 314.0, sales +32%) | n/a | Falling. Only half-year balances are in XBRL |

Interpretation (DERIVED): Nike's Q3 FY26 rise is larger than any peer's, so it is not purely an industry-wide terms or FX effect. adidas shows a smaller version of the same pattern while its wholesale grows, which fits the "wholesale growth carries receivables" view (a real sell-in effect for both) rather than the "Nike-only extended terms" view. Skechers and Deckers, whose wholesale is growing, show none.

## 8. What the numbers imply for the pitch (financial, not sentiment)

- Excess receivables vs the mix-and-FX prediction: $477M in Q3 FY26 (6.6 days of wholesale sales), $130M in Q1 FY27 (DERIVED). Cash tied up: the Q1 FY27 operating cash flow was $135M (10-Q p. 33), and trade AR is $5.2B. Every 1 day of wholesale DSO is about $76M (6,948 / 91).
- Link to earnings is indirect. Receivables carry no margin effect by themselves. The profit exposure is through the reserve: restoring the 17.5% FY24 reserve ratio on Q1 FY27 wholesale means a release of about $270M to $300M, restoring the FY25 peak ratio means a charge of about $450M (DERIVED, section 4). The first is upside to revenue, the second is the downside the short needs. The filings give no basis to pick between them.
- The surviving short-relevant fact is narrower than "stuffing": reported wholesale receivables days hit the highest level in the 8-year series (73.9) one quarter after the largest sell-in quarter, and the NA-specific disclosure that would explain it was withdrawn.

## 9. Routes tried (per repo rule; at least five different routes for each "inconclusive")

For the question "did NA AR / terms rise in Q1 FY26 to Q1 FY27?" (NA AR not disclosed):

| # | Route | Result |
|---|---|---|
| 1 | Nike 10-Q and 10-K segment AR table | WORKED to Feb 28, 2025; BLOCKED after (withdrawn) |
| 2 | Total AR with regional mix model from the last segment table, FX and IEEPA adjusted | WORKED. Residual +$477M Q3 FY26 |
| 3 | Cash-flow statement vs balance sheet (FX/non-cash check) | WORKED. Confirms FX $162M |
| 4 | Nike MD&A cash-flow narrative | WORKED. Names "timing of wholesale shipments"; says nothing on terms |
| 5 | XBRL companyfacts for Nike (allowance FY26, segment AR) | PARTIAL. No allowance tag for FY26; dimensional segment AR not in the API |
| 6 | Nike call transcripts (`data/hunt/earnings_calls`) | WORKED, empty on terms |
| 7 | Retailer payables (DICK'S, Academy, Shoe Station, Genesco, Foot Locker) via XBRL | PARTIAL. No stretching pattern; AP not Nike-specific |
| 8 | Peer receivables (adidas, Puma, Deckers, UA, Skechers, On) | WORKED except On (half-year only; On IR site returned HTTP 403) |
| 9 | FX data from FRED | BLOCKED (empty reply / HTTP2 error); replaced by Yahoo chart API (WORKED) and by the cash-flow cross-check |
| 10 | Deckers and Skechers IR pages for wholesale-only revenue | BLOCKED (HTTP 502 and web.archive.org connection reset); SEC document pages at www.sec.gov not requested for peers (known 403 per D2) |
| 11 | Circana, Placer, customer-level AR, aging | NOT AVAILABLE free |

Verdict on "inconclusive": the cause of the Q3 FY26 to Q1 FY27 DSO rise remains **open between timing, retailer slow-pay and Nike-granted terms**, after 9 routes. Data that would decide: (i) NA AR by quarter or Nike's DSO by region (ask at the Nov 16 to 17 Investor Day, or in the Q2 FY27 10-Q); (ii) reserve rollforward (additions vs usage) for FY25 to FY27; (iii) monthly wholesale shipments or the share of quarterly wholesale revenue in the last four weeks; (iv) AR aging buckets; (v) retailer vendor-payable disclosures naming Nike.

## 10. What I could not verify

- Customer-level or region-level AR after Feb 28, 2025. Mix model uses stale regional DSOs.
- Aug 2026 IEEPA balance (assumed 0).
- Peer wholesale-basis DSO for Deckers, Under Armour, Skechers and On (total-sales basis only); adidas wholesale for 2023 and 2024; Puma 2025 and 2026 prior-year sales are as restated by Puma in later releases; adidas Q2 2025 sales as restated for discontinued operations in the Q2 2026 release.
- Yahoo Finance FX closes were not cross-checked against a central bank source (the cash-flow cross-check agrees).
- Nike Q4 wholesale values are fiscal year less nine months (DERIVED), as in `data/nike_channel_split.csv`.
- Whether the three dropped disclosures were removed for a benign reason.

## 11. Sources

Nike 10-K FY2018 to FY2026 and 10-Q Q1 FY2019 to Q1 FY2027, https://investors.nike.com/sec-filings/all-sec-filings/content/<accession>/<file>.htm (accessions from data.sec.gov submissions index CIK 0000320187; e.g. 0000320187-26-000193 nke-20260831.htm, 0000320187-26-000088 nke-20260531.htm). OPENED. SEC XBRL companyfacts (data.sec.gov) CIK 320187, 910521, 1065837, 1336917, 1089063, 1817358, 895447, 14707, 18498, 850209, 1017480, 1858985. OPENED. adidas results PDFs (Q1 2023 to Q2 2026) via adidas-group.com/en/investors/financial-reports. OPENED. Puma quarterly releases (Q1 2023 to Q2 2026) via about.puma.com/en/investor-relations/financial-publications. OPENED. Yahoo Finance chart API (EURUSD=X, GBPUSD=X, CNY=X, JPY=X). Market data.
