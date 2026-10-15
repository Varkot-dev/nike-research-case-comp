# G11: Disclosure forensics. What Nike added and removed, FY2019 to Q1 FY2027, and whether removals follow deterioration

Prepared 2026-10-15. Data: `G11_disclosure_withdrawal.csv` (68 rows: document, item, added or removed, last value, trend, page cites). Related: `G2_receivables_reserves.md` (AR, returns, allowance), `G1_purchase_obligations.md`, `18_capital_and_dividend.md`, `G3_*` (factories).

Tags: OPENED = read in the document itself (every row's value was machine-checked to appear on the cited page, and every "absent" claim is a full-text search of the later document, 0 hits). DERIVED = my arithmetic from OPENED inputs. SNIPPET = web-search result only (used once, labelled).

## 1. Verdict

**Smoking gun: NO. A real, bunched and adverse-skewed disclosure retreat: YES, but mostly low information loss, and statistically fragile.**

1. **Bunching is the robust finding.** Discretionary item families removed from Q1 FY25 (Aug 2024) to Q1 FY27 (Aug 2026), 9 quarters: 16. Same kind of removal in the 24 quarters Q1 FY19 to Q4 FY24: 5 (online share of Direct, long-term goals table, category table, Sojitz paragraph, factory-count redefinition; excluding 4 removals explained by SEC or accounting rules). Rate 1.8 per quarter vs 0.21 per quarter; Poisson P(16 or more | 1.9 expected) = 2e-10 (DERIVED). Caveat: I looked hardest at recent filings; label-level and XBRL churn (section 5) is not abnormal, so the bunching is in KPI-type disclosures, not in total filing volume.
2. **Direction skew exists but is not robust.** Of the 12 removed families in FY25 to Q1 FY27 with a clear good or bad direction, 11 were deteriorating over their final two disclosed periods (92%); among 29 kept discretionary families with a clear direction, 12 were deteriorating (41%). Fisher exact, one-sided p = 0.003, two-sided 0.005. Sensitivity (DERIVED, section 4): treating the 4 ambiguous removed families as non-deteriorating and the 3 ambiguous kept as deteriorating moves two-sided p to 0.22; counting only removals with real information loss gives p = 0.04. Verdict on statistics: suggestive, not proven, and the control list was assembled by me.
3. **Economic meaning is small to moderate.** Of 16 removed families, 4 lost no information (derivable from items still disclosed or boilerplate): Direct share of revenue, buyback statements, annual channel table, seasonality sentence. The ones that matter: NA and segment receivables (AR 5,931 at May 2026, up 26% YoY, includes $684M IEEPA receivable), the returns-reserve rollforward (provision 12.4% of wholesale in FY24; each 1pp is about $281M of FY26 wholesale revenue, DERIVED), the Men's/Women's/Kids' split (all four lines had turned negative), comparable store sales (-1%, -3%, -5% in the last three quarters shown), the ASP/discount line of the gross-margin bridge (-180 bps in FY25), the largest-factory share (footwear 11% vs 9%). Everything else is small ($27M allowance) or already explained.
4. **No misstatement, no concealment evidence.** Nike kept, and in places added, adverse data in the same cycle: three largest US customers 25% to 29% (kept), Moody's one-notch cut and S&P cut disclosed, headcount 77,800 to 73,000 (kept), Converse US stores 78 to 60 (kept), Greater China inventory (kept), new dollar inventory reserve $233M vs $155M (+50%, added FY25), written outlook of high-single-digit decline (added Q1 FY27), net income margin 4.6% vs 7.0% (added Q3 FY26). A concealment story needs those not to exist.

For the pitch, writable with these exact words: "In the nine quarters from Q1 FY25 to Q1 FY27 Nike withdrew 16 discretionary disclosure families, 11 of the 12 with a clear direction while the metric was deteriorating; the most informative losses are receivables by segment, the returns-reserve rollforward and comparable store sales. Nike also added an inventory reserve, a net income margin line and a written outlook in the same period." Do not write "Nike is hiding deterioration".

## 2. What was audited and how

Documents (all from investors.nike.com mirror, index from data.sec.gov submissions, no email in any request): 10-K FY18 to FY26 (9; FY18 is the FY19 baseline), 10-Q Q1 FY19 to Q1 FY27 (25 of 25), earnings-release Ex. 99.1 Q4 FY18 to Q1 FY27 (34 of 34), plus FY17 Q1 to Q4 releases and calls and the FY16 and FY17 10-Ks for the futures item. Converted with `scripts/sec_pipeline/topages.py` (printed pages for 10-K and 10-Q; releases cited by sequential exhibit page). Methods, in order: (a) table row-label diff of every 10-K against the prior year (24 to 54 removed labels a year), every 10-Q against the same quarter a year earlier, every release against the same quarter a year earlier; (b) fuzzy sentence diff of 10-Ks, keeping sentences present in three consecutive years and then gone; (c) a 45-pattern keyword presence matrix over all documents (units, ASP, digital, comps, stores, factories, customers, AR, allowance, reserves, dividend, buyback, targets, etc.); (d) manual reading of every candidate. Items were then verified against the document, including the false positives (credit-rating sentence, units and ASP, digital growth, FY26 inventory by segment: all KEPT).

Checked and found KEPT through Q1 FY27 (controls): units and ASP commentary by region, digital and store sales growth by region, inventories by segment (including Greater China), segment EBIT, Converse revenue and EBIT, Jordan Brand revenue, three largest US customers, no-10%-customer statement, US store counts by type, employees, factory counts and country shares, four-manufacturer concentration, sales-related and returns reserves, inventory reserve, credit ratings, gross margin bridge in bps, currency-neutral tables.

Not in any Nike filing at any time in the window (so nothing was removed): member counts, EBIT by product, Converse revenue by territory table, wholesale customer names, inventory in transit vs finished goods (only "substantially all finished goods", kept), inventory-obsolescence reserve before FY25 (added FY25), order backlog.

## 3. Ledger summary (full detail and cites in the CSV)

REMOVED, Q1 FY25 to Q1 FY27 (cycle B). Trend = direction of the metric over its last two disclosed periods.

| Family | First document without it | Last value disclosed (page) | Trend | Information lost |
|---|---|---|---|---|
| F1 AR by segment | FY25 10-K; Q1 FY26 10-Q | FY24 10-K p.88: NA 1,723, total 4,427; Q3 FY25 10-Q p.21: NA 1,957 | deteriorating (AR/revenue 8.07% to 8.62%) | yes |
| F2 PP&E by segment | FY25 10-K; Q1 FY26 10-Q | FY24 10-K p.88: total 5,000 | ambiguous | immaterial |
| F3 Schedule II returns rollforward | FY25 10-K p.91 | FY24 10-K p.97: provision 3,583, write-offs 3,325, balance 799 | deteriorating (9.6%, 11.7%, 12.4% of wholesale) | yes |
| F4 Dollar allowance for AR | FY26 10-K | FY25 10-K p.64: $27M (35) | improving | small |
| F5 Direct share of NIKE Brand revenue | Q2 FY26 10-Q; FY26 10-K | FY25 10-K p.29: 42% (44%); Q1 FY26 10-Q p.19: 40% (42%) | deteriorating | no |
| F6 Comparable store sales | Q1 FY27 10-Q | Q3 FY26 10-Q p.29: -5% (Q2 -3%, Q1 -1%) | deteriorating | yes |
| F7 Men's/Women's/Kids'/Jordan/Others | FY26 10-K; Q4 FY26 release | FY25 10-K p.33: -6%, -6%, -5%, -16%; Others (1,234) vs (594) | deteriorating | yes (Jordan kept) |
| F8 Largest single factory share | FY26 10-K | FY25 10-K p.3: footwear 11% (9%), apparel 8% (9%) | deteriorating (footwear) | yes |
| F9 Wholesale equivalent revenues | Q1 FY25 10-Q; FY25 10-K; Q4 FY25 release | FY24 10-K p.34: 40,767, +2% (+11%) | deteriorating | yes |
| F10 Buyback pace statements | Q2 FY26 release; FY26 10-K | Q1 FY26 release p.1: $123M; series 1.2B, 1.1B, 0.5B, 0.2B, 0.12B, 0 | deteriorating | no |
| F11 Dividend-streak sentence | Q4 FY26 release | Q3 FY26 release p.1: 24 years; raises 8.8%, 8.1%, 2.5% | deteriorating | partial |
| F12 GM bridge ASP/discount line | FY26 10-K | FY25 10-K p.35: -180 bps (FY24 +200) | deteriorating | yes |
| F13 Accrued endorsement compensation | Q1 FY26 10-Q; FY26 10-K | FY25 10-K p.68: 481 (578) | ambiguous | small |
| F14 Seasonality sentence | FY26 10-K | FY25 10-K p.2 (sentence false in FY23 to FY26) | ambiguous | no |
| F15 Annual channel table in Q4 release | Q4 FY26 release | Q4 FY25 release p.5: wholesale 25,883 (-7%), Direct 18,783 (-13%) | deteriorating | no (restored by region in Q1 FY27) |
| F16 $1.5B gross tariff estimate | Q3 FY26 10-Q | Q2 FY26 10-Q p.23 | ambiguous (court ruling) | partial |

REMOVED earlier (cycle A): futures program share (FY17 83%, 84%, 87%) and futures-order growth (+11%, +7%, +2%, -1% c-n over Q4 FY16 to Q3 FY17; off the release Dec 2016, gone FY18): deteriorating, out of window. Online share of Direct (Q1 FY19 27% vs 22%): improving, derivable. Long-term goals table (FY21): deteriorating at last disclosure, improving at removal. Product category table (FY22): improving, replaced. Regulatory: five-year financial history (FY21, SEC Item 301 eliminated, effective Feb 10 2021), contractual obligations table (FY22, Item 303(a)(5)), lease table (ASC 842), Hurley rows (divestiture).

ADDED: dividend-streak sentence (Q4 FY20, 18 years), inventory reserve in dollars (FY25 10-K p.64), significant segment expenses (FY25, ASU 2023-07), net income margin (Q3 FY26), written Outlook (Q1 FY27 release p.1, the first in any release since Q4 FY18), regional channel revenue table (Q1 FY27 release p.5), IEEPA recovery $986M and $684M receivable (FY26 10-K p.30), ROIC and EBIT margin (FY21), Pace and a plan to report three geographies in FY28 (Q1 FY27 10-Q p.20 to 21).

Format change worth noting: the FY26 10-K p.33 replaced the revenue summary tables with donut-chart images (alt text gives 45% NA, 14% APLA, 13% GC, 28% EMEA; 61% wholesale, 39% Direct; 65% footwear). The detailed tables remain on p.32, so no loss.

## 4. Test of "disclosures are withdrawn when the metric deteriorates"

Unit: disclosure family (a family withdrawn in several documents counts once). Universe: discretionary families only; regulatory and ASU-driven items excluded. Direction rule: adverse if the metric moved the wrong way by at least 2% relative or 1pp over its last two periods; ambiguous items (no good or bad direction, e.g. PP&E, headcount) are excluded from the primary test. Kept list: 32 families named in the CSV (K rows), built from the same checklist before classification.

| | Deteriorating | Not deteriorating (improving or flat) |
|---|---|---|
| Removed (cycle B) | 11 | 1 (allowance) |
| Kept (same period) | 12 | 17 |

Fisher exact p = 0.003 (one-sided), 0.005 (two-sided). Odds ratio 15.6. Removal rate 48% of deteriorating families vs 6% of non-deteriorating (DERIVED).
Sensitivity (two-sided p): ambiguous removed as non-deteriorating and ambiguous kept as deteriorating, 0.22; all ambiguous as non-deteriorating, 0.066; ambiguous removed as deteriorating and kept as not, 0.0002; only removals with real information loss, 0.04; drop the restored annual channel table, 0.03. Cycle A (FY19 to FY24): of 4 clear-direction discretionary removals, 2 deteriorating and 2 improving: no pattern. Conclusion: significant at the 5% level in the primary spec and in three of five variants, not at 5% in the two pessimistic variants. I would not present a p-value to a skeptic without the caveat that the kept list is my construction.

## 5. Alternatives tested and ruled out (or not)

| # | Alternative | Verdict | Evidence |
|---|---|---|---|
| 1 | SEC or accounting rule change | Explains 4 of 25 removals, not the cycle B ones | Item 301 (FY21 history) and Item 303(a)(5) (FY22 contractual table) explain those. ASU 2023-07 (adopted FY25) added segment expense lines and (FY25 10-K p.67) says nothing that requires dropping segment AR or PP&E; ASC 280 requires a segment asset measure only if the CODM uses it, so dropping AR implies it is no longer in the CODM package (an inference, not a statement) |
| 2 | ERP rollout (Nike's stated reason for wholesale equivalent) | Supported for F9 only | Q1 FY25 10-Q p.19 and FY25 10-K p.33 fn 4 give the reason; Q1 FY24 call: NA wholesale ERP go-live in FY24. For AR by segment the timing fails: ERP reason was given Aug 2024 but segment AR stayed in Q2 and Q3 FY25 10-Qs |
| 3 | Materiality | Plausible only for allowance ($27M, 0.5% of AR) and PP&E | AR by segment is 8.6% of revenue; returns provision is 12.4% of wholesale |
| 4 | Standard de-cluttering | Plausible for seasonality, endorsement accrual, tariff estimate, buyback paragraph | Does not fit the pairs where adverse numbers were also kept |
| 5 | Zero activity (nothing to report) | Explains F10 | no repurchases after Q1 FY26 |
| 6 | New CFO | Not supported | Friend still quoted in Q4 FY26 release (Jun 30 2026), 7 days after the separation 8-K (Jun 23); Denton first quoted Q1 FY27. The first wave (Q1 FY25 to Q1 FY26) is under Friend |
| 7 | SEC staff pressure | Ruled out as a trigger for withdrawal | EDGAR lists 27 UPLOAD and CORRESP letters, 2006 to Feb 14 2014; none since. The 2011, 2012 and 2014 letters created ASP and unit commentary, the wholesale-equivalent scrutiny and the digital-share and comps template; three items Nike agreed to provide on Feb 10 2014 (online share, Direct share, comps) have now been dropped without any recorded staff comment |
| 8 | Peers dropped the same things | Partly | See section 6 |
| 9 | Aggregate churn is abnormal | Ruled out | 10-K table-label churn FY25 34 removed, FY26 24 (FY20 39, FY21 54, FY22 32). XBRL concepts dropped: Nike FY25 3.0%, FY26 3.6% vs its history 2.4% to 14%; Deckers 5.6%, 8.6%; Under Armour 6.9%, 6.2% (DERIVED, companyfacts) |
| 10 | Cause cannot be separated | Open | Whether AR by segment was dropped for system reasons, for CODM-package reasons or for optics cannot be read from the filings |

## 6. Peers (feasible subset)

- US filers by XBRL companyfacts (Deckers, Under Armour, Skechers, Lululemon, VF, Columbia, Crocs, Foot Locker, DICK'S): tag retirement 3% to 9% a year, so Nike FY25 to FY26 is at or below peers. Item-level: Lululemon stopped tagging Schedule II reserves after FY2021; Crocs after 2024; DICK'S dropped the allowance tag in FY2025; VF dropped the inventory-reserve tag. Deckers, Under Armour, VF, Columbia, Crocs kept allowance tags. Peers also withdraw reserve disclosures, but none in this set withdrew segment receivables (none ever disclosed them in tagged form).
- adidas (annual reports 2017 to 2025) and Puma (2018 to 2025), 14 keyword families each (receivable allowance and aging, returns and refund liabilities, inventory allowance, own-store counts, employees, supplier and factory data, production country shares, largest customer, mid-term targets, dividend policy): no withdrawal found. Puma's "Refund liabilities" line (351.2 in 2021) was renamed "liabilities from refund obligations" and kept; adidas kept mid-term targets, DTC share (41%, then 40%) and expanded receivable-aging text (about 60 hits to 170 in 2024). Limitation: keyword, not table-by-table, comparison; Deckers and Under Armour 10-K text was not opened (IR host blocked, see section 8).

## 7. Routes tried (rule: five different routes before calling anything inconclusive)

Question: why were AR, PP&E and the returns rollforward dropped, and is the cause financial?

| # | Route | Result |
|---|---|---|
| 1 | Nike 10-K and 10-Q text, notes and ASU 2023-07 paragraph | WORKED for facts, PARTIAL for reason: only the generic "schedules omitted" clause |
| 2 | SEC comment letters (data.sec.gov index, letters fetched via the investors.nike.com mirror) | WORKED, empty after Feb 2014 |
| 3 | Earnings-call transcripts FY21 to Q1 FY27 (26 files) | WORKED: ERP timeline (Q1 FY24 call), dividend priority (Q1 FY27 call p.25); nothing on AR by segment |
| 4 | XBRL companyfacts (Nike and 9 peers) | PARTIAL: allowance tag dropped FY26; dimensional segment AR not in the API |
| 5 | Peer annual reports (adidas, Puma) | WORKED: no comparable withdrawal |
| 6 | Web search (SNIPPET) | PARTIAL: confirmed only the ERP wording; nothing on AR by segment |
| 7 | Deckers IR site, www.sec.gov peer documents | BLOCKED (proxy refused investor.deckers.com; sec.gov not used by rule) |
Verdict: reason for F1 and F3 stays OPEN after 7 routes. What would settle it: ask on the Q2 FY27 call or at the Nov 16 to 17 Investor Day for (a) NA receivables or DSO by region, (b) provision and write-offs for the sales-related reserve for FY25 to FY27, (c) whether segment AR is still in the CODM package.

## 8. What I could not do

- Converse "folded in" to the FY28 three geographies: NOT VERIFIED. The Q1 FY27 10-Q p.20 to 21 names Americas (North America and Latin America), APGC (Asia Pacific and Greater China) and EMEA and is silent on Converse. If it happens, standalone Greater China (FY26 revenue 5,847, -11%; EBIT 1,278, -20%; Q1 FY27 revenue -22%, EBIT -34%), standalone North America (FY26 EBIT 5,376 includes the $965M IEEPA benefit) and Converse (EBIT 18 vs 240) all disappear from FY28 reporting, which is the largest pending disclosure change and sits on the three worst-trending units. Recast comparatives will be required by ASC 280.
- Deckers and Under Armour 10-K text (IR host refused; EDGAR documents not used for peers); adidas and Puma compared by keyword only.
- Nike's quarterly "Part II Item 2" repurchase tables and every footnote were not diffed line by line beyond labels; items with identical labels but changed definitions would be missed.
- The control list and trend thresholds are my judgment; the CSV lets a reviewer reclassify.
