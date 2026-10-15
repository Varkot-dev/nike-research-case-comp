# N4: Nike subsidiary statutory accounts (Korea, EMEA hub, UK, Australia) as a check on the group 10-K

Date of research: 15 Oct 2026. Tags: OPENED = I read the filing or page itself in this session; SNIPPET = seen only in a search result or summary; DERIVED = my arithmetic on OPENED inputs. Data: `data/niche/N4_subsidiary_accounts.csv` (358 rows, every extracted figure), `data/niche/N4_derived_tests.csv` (125 derived rows), extracted filing text in `data/niche/N4_raw/`. Scripts: `N4_build_csv.py`, `N4_derived.py` in this folder. Extends `G10_belgian_customs.md` (Nike Retail B.V. already used there for the customs paragraph; not redone) and `G2_receivables_reserves.md` / `G12_check.md` (group receivables and reserves; cross-checked below).

## 1. Bottom line

**Smoking gun: no.** Nothing in the local accounts contradicts the 10-K. The accounts add four data points that the 10-K does not give, and one structural fact that limits what local profit can tell us.

1. **Nike Korea LLC revenue fell faster than the reported region, three years running (DERIVED).** KRW revenue growth FY24 -0.3%, FY25 -5.7%, FY26 -5.2% (fiscal years end 31 May, same as Nike's) against APLA currency-neutral growth of +5%, -3%, -1%: a gap of -5.3, -2.7 and -4.2 points. KRW is the local currency, so these are already currency-neutral. Korea's share of APLA revenue falls from 23.7% (FY23) to 20.0% (FY26) (USD conversion approximate, section 3.4). Ex-Korea APLA revenue was about +1.9% in FY26 (about $4,993M vs $4,900M), while reported APLA was 0%.
2. **Local profit is a transfer-pricing output, not a demand signal.** Nike Korea's operating margin before the transfer price adjustment line in cost of sales is exactly 2.00% in four of six years (FY21, FY24, FY25, FY26); FY22 was 3.7% and FY23 2.8%. FY26 reported operating profit rose 118% (KRW 37.8bn to 82.5bn) but a KRW 46.6bn transfer price credit in cost of sales is 104% of that KRW 44.6bn increase; without it operating profit fell 5.2%, in line with revenue. Do not use local EBIT of the selling subsidiaries as evidence of demand.
3. **Local balance sheets show inventory and receivables moving in opposite directions by entity.** Nike Korea inventory -16.2% (KRW 315.9bn vs 377.0bn) on revenue -5.2%. The EMEA entity (Nike Retail B.V.) inventory +5.1% (EUR 1,288M vs 1,226M) on revenue -11.2%, and its trade receivables +26.5% (EUR 904.5M vs 715.3M), which is +9.1 days of trade receivables (30.6 vs 21.5) and a bad-debt reserve that rose from EUR 2.8M to EUR 11.7M. The +9.1 days is similar to the +10.3 days of group wholesale DSO YoY at Q4 FY25 in G2, so that group figure is not a US-only artefact; but NRBV's 30.6 days is a reversion to its FY22 level (32.1), after two years near 21.6, so it is not a record.
4. **Returns provisions are not rising.** Nike Korea's returns provision fell 21.0% in FY26 (KRW 62.9bn to 49.7bn; 2.77% of revenue vs 3.33% in FY25 and a FY21 to FY26 range of 2.3% to 3.3%), because provision usage (KRW 257.8bn) exceeded the new charge (KRW 244.6bn). This is the same direction as the group's sales-related reserve ($1,834M May 2025 to $1,589M May 2026, G2) and is consistent with the G12 "lapping the FY25 build" reading, but the filing cannot separate lower returns from lower sell-in.
5. **Converse Korea LLC is the one distressed entity.** Revenue KRW 30.8bn in FY26, -34.4% YoY and -66.8% from FY22 (KRW 92.8bn); operating loss KRW 8.8bn; shareholders' equity KRW -23.5bn (FY25: -12.1bn); funded by a USD 8M loan from Converse Netherlands B.V. The auditor (Samil, report dated 24 Aug 2026) gives a clean opinion with no material-uncertainty paragraph. It is about $21M of revenue (DERIVED), so it is not material to Nike's income statement; it is a datapoint for the Converse trend only.

## 2. Coverage table: what exists, what I got

| Entity | Free public accounts? | Latest year obtained | Status |
|---|---|---|---|
| Nike Korea LLC (유한회사 나이키코리아) | Yes, DART audit reports (Samil PwC) | FY26 (year to 31 May 2026), filed 11 Sep 2026; FY21 to FY26 all read | Complete |
| Converse Korea LLC (유한회사 컨버스코리아) | Yes, DART | FY26, filed 7 Sep 2026; FY21 to FY26 | Complete |
| Nike Retail Services Korea | No separate filer found on DART (Nike 360 (Korea) appears only as a related party with KRW 6M of sales) | n/a | Not separate |
| Nike (UK) Limited (01887016) | Companies House PDFs | FY21 (to 31 May 2021); dissolved 4 Jun 2024 | Partial: it was a commission and cost-reimbursement entity; its trade moved to Nike Retail B.V. |
| Converse Retail (UK) Limited (10584502) | Companies House PDFs | FY25 (to 31 May 2025), FY23 from comparatives | Partial: one outlet, immaterial |
| Nike Retail B.V. (EMEA principal, UK establishment FC019114) | Companies House PDFs | FY25 (filed 17 Apr 2026); FY24, FY23 from comparatives; FY22 read from its own report | FY21 and older not like-for-like (pre-merger) and not read |
| Nike 360 Holding B.V. (FC032565), accounts of parent Nike Flight B.V.; holds Nike Trading Co and Nike Global Trading, Singapore branches | Companies House PDFs | FY24 (filed 17 Apr 2026), FY23 comparative | The sourcing hub: sells about $21B a year to Nike entities |
| Nike Australia Pty Ltd | Tax data only (ATO Corporate Tax Transparency, data.gov.au) | Income year 2024-25 | Total income only, no balance sheet |
| Nike Japan Group LLC | No: a godo kaisha has no duty to publish a 決算公告; no Nike entity found in the Kanpo-based database | none | Not obtainable free |
| Nike India Pvt Ltd, Nike Taiwan, Nike Hong Kong, Singapore entities, Nike Canada, Switzerland | No free financials found | none | See section 8 |
| Belgium (NBB Balanscentrale) | No operating Belgian entity files (per G10 6a) | n/a | Belgian activity runs as Nike Retail B.V. branches |

## 3. Nike Korea LLC (KRW billions; all OPENED from the DART audit reports unless marked DERIVED)

Filings: rcpNo 20210914000321 (FY21), 20220914000354 (FY22), 20230914000346 (FY23), 20240913000749 (FY24), 20250912000263 (FY25), 20260911000443 (FY26). Auditor Samil PwC; the FY26 opinion is unqualified per the NewsSpace report (I did not read the audit opinion pages of the Nike Korea reports; I did read the Converse Korea FY26 opinion, section 4). The FY26 notes state there is no pending litigation. The FY26 filing was also reported by NewsSpace on 11 Sep 2026 (secondary; every figure in it that I checked matches the filing). The company is wholly owned by NIKE GmbH (Austria). Statements follow Korean general accounting standards (not K-IFRS).

### 3.1 Income statement and ratios

| | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|---|---|
| Revenue | 1,452.2 | 1,674.9 | 2,010.9 | 2,005.0 | 1,891.3 | 1,793.6 |
| YoY (DERIVED) | +12.3% | +15.3% | +20.1% | -0.3% | -5.7% | -5.2% |
| APLA currency-neutral YoY (10-K / releases) | +8% | +16% | +17% | +5% | -3% | -1% |
| Korea minus APLA (pts, DERIVED) | +4.3 | -0.7 | +3.1 | -5.3 | -2.7 | -4.2 |
| Cost of sales | 1,214.6 | 1,309.3 | 1,659.1 | 1,644.7 | 1,530.6 | 1,388.2 |
| of which transfer price adjustment (credit negative) | none shown | -34.2 (inside purchases; amount from the FY23 report comparative) | -13.1 | +0.6 | 0 | -46.6 |
| Gross profit | 237.6 | 365.5 | 351.8 | 360.2 | 360.7 | 405.4 |
| Gross margin reported | 16.4% | 21.8% | 17.5% | 18.0% | 19.1% | 22.6% |
| Gross margin ex TP line (DERIVED) | 16.4% | 19.8% | 16.8% | 18.0% | 19.1% | 20.0% |
| SG&A | 208.5 | 269.7 | 282.6 | 320.8 | 322.9 | 323.0 |
| SG&A % revenue (DERIVED) | 14.4% | 16.1% | 14.1% | 16.0% | 17.1% | 18.0% |
| Operating profit | 29.0 | 95.9 | 69.2 | 39.5 | 37.8 | 82.5 |
| Operating margin reported | 2.0% | 5.7% | 3.4% | 2.0% | 2.0% | 4.6% |
| Operating margin ex TP line (DERIVED) | 2.0% | 3.7% | 2.8% | 2.0% | 2.0% | 2.0% |
| Net income | -6.0 | 8.0 | 106.3 | 48.2 | 31.3 | 81.2 |

FY22 and FY23 contain Korean tax audit items (section 3.5) that distort net income (effective tax rate 92.0% in FY22, -53.4% in FY23, 9.1% in FY26).

### 3.2 FY26 operating profit bridge (DERIVED, KRW bn): why profit rose while revenue fell

Operating profit FY25 37.8 to FY26 82.5, +44.6:
- Transfer price adjustment credit in cost of sales: +46.6
- Gross profit ex that line (revenue -5.2%, ex-TP margin 20.0% vs 19.1%): -1.9 (the ex-TP gross margin rose 0.9 point, but revenue fell 97.7bn)
- SG&A (flat at 323.0, 0.03% higher): -0.1
Sum +44.6. The ex-TP operating margin of 2.00% in FY21, FY24, FY25 and FY26 means invoice pricing from Nike Global Trading is set to deliver a 2.0% operating margin to this entity. What the extra KRW 46.6bn is, the filing does not say. Explanations that survive: (a) a retroactive true-up for earlier years (the FY23 and FY24 notes say tax-audit results changed transfer price adjustments in the related-party note), (b) a change in the target margin, (c) a one-time group decision. No text in the filing separates them. What would: the transfer pricing report or the tax note of the FY27 audit report (if the line recurs, (b); if not, (a) or (c)).

Sensitivity (DERIVED): at the FY22 reported operating margin (5.7%), FY26 operating profit would be KRW 102.7bn; at the 2.0% pricing margin it is KRW 35.9bn.

Implication for Nike's group P&L (my inference, labelled): because the Korean entity is held to about 2.0%, the economic margin on Korean sales and any markdown or returns cost sits in Nike Global Trading and Nike, Inc., not in Korea. The local accounts show Korean volume and balance-sheet quality, not Korean profitability.

### 3.3 Balance sheet and the 10-K "hidden" items

| | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|---|---|
| Inventory (net) | 245.5 | 304.8 | 524.2 | 367.6 | 377.0 | 315.9 |
| Inventory valuation allowance | 16.7 | 20.6 | 30.8 | 33.2 | 29.6 | 27.1 |
| Inventory days on cost of sales ex TP (DERIVED) | 73.8 | 85.0 | 114.4 | 81.6 | 89.9 | 80.4 |
| Goods purchases | 1,208.4 | 1,380.4 | 1,902.8 | 1,499.0 | 1,549.3 | 1,384.3 |
| of which from Nike Global Trading, Singapore branch | 1,125.9 | 1,304.8 | 1,817.6 | 1,388.5 | 1,442.1 | 1,325.5 |
| Purchases % revenue (DERIVED) | 83.2% | 82.4% | 94.6% | 74.8% | 81.9% | 77.2% |
| Receivables (no allowance recorded) | 77.4 | 108.5 | 86.7 | 89.1 | 97.5 | 101.1 |
| Receivable days (DERIVED) | 19.5 | 23.7 | 15.7 | 16.2 | 18.8 | 20.6 |
| Trade payables | 164.5 | 254.6 | 443.6 | 382.7 | 296.1 | 180.4 |
| Returns provision (balance) | 37.5 | 51.4 | 60.6 | 45.9 | 62.9 | 49.7 |
| Returns provision charge (increase) | 96.5 | 117.6 | 237.8 | 233.0 | 263.5 | 244.6 |
| Returns provision usage | 112.0 | 103.7 | 228.6 | 247.7 | 246.4 | 257.8 |
| Returns provision balance % revenue (DERIVED) | 2.6% | 3.1% | 3.0% | 2.3% | 3.3% | 2.8% |
| Early-payment discount provision | 1.5 | 1.4 | 11.1 | 9.5 | 9.1 | 9.0 |
| Returned-goods recovery asset (gross) | 23.6 | 42.5 | 39.6 | 18.9 | 30.0 | 37.4 |
| Provision less recovery asset (DERIVED) | 13.9 | 8.9 | 20.9 | 26.9 | 33.0 | 12.4 |
| Cash | 70.9 | 109.7 | 30.0 | 61.3 | 65.6 | 189.6 |
| Operating cash flow | -4.1 | 75.3 | -58.6 | 82.8 | 48.0 | 144.1 |
| Equity | 236.9 | 249.6 | 362.7 | 417.6 | 455.6 | 543.6 |

Reading (DERIVED unless noted):
- **Inventory is being cut, not built.** Inventory -16.2% against revenue -5.2%; purchases from Nike Global Trading -8.1% against revenue -5.2%; trade payables -39.1% (KRW 180.4bn vs 296.1bn). Inventory days 80 vs 90. The FY23 peak (KRW 524bn, 114 days, purchases 94.6% of revenue) is the Korean version of the group FY23 inventory build.
- **Operating cash flow KRW 144.1bn (FY26) is working capital, not earnings:** inventory release KRW 61.1bn, partly offset by payables KRW -115.8bn and receivables.
- **Receivables are up 3.7% on revenue -5.2%** (receivable days 20.6 vs 18.8, +1.8 days; the FY22 level was 23.7). No credit allowance is booked (KRW 0 each year).
- **Returns reserve.** The balance fell KRW 13.2bn in FY26 (usage 257.8 > charge 244.6). The FY25 to FY26 swing in the balance (+17.1bn then -13.2bn) is the Korean mirror of the group build and release in G12; the swing is 1.7% of FY26 revenue. The charge as a share of revenue stepped from 6.6% to 7.0% (FY21 and FY22) to 11.6% to 13.9% (FY23 to FY26); the filings do not say why (a change in returns accounting or customer mix would both fit), so it is shown as a level only. Early-payment discount provision stepped from KRW 1.4bn to 11.1bn in FY23 and has been flat since.
- **Store and franchise footprint (OPENED, Nike store locator crawl of 14 Oct 2026 in `data/hunt/stores/`):** 274 Korean doors, of which 22 Nike-owned and 252 franchise partners (Daeyeon 59, Winwin 37, Shoeland 27 as the three largest operators). The audit report gives no store count or headcount. Salaries and wages KRW 80.6bn (+4.3%); employee count not disclosed.
- **Lease commitments** KRW 92.2bn at 31 May 2026 (FY21: KRW 130.6bn); of which KRW 17.7bn due within one year.
- **Capex and logistics:** construction in progress KRW 76.7bn (KRW 65.98bn is the logistics automation contract signed Aug 2023, running to Jun 2026).
- **Going-concern, impairment, customs notes:** none in any year for Nike Korea. No customs or duty note.

### 3.4 Korea vs the reported region (the "falling faster" test)

| | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|
| Korea revenue, KRW bn | 2,010.9 | 2,005.0 | 1,891.3 | 1,793.6 |
| Korea revenue, USD M approx (DERIVED) | 1,523 | 1,513 | 1,351 | 1,250 |
| APLA reported revenue, $M (10-K) | 6,431 | 6,729 | 6,251 | 6,243 |
| Korea share of APLA | 23.7% | 22.5% | 21.6% | 20.0% |
| APLA ex Korea, $M approx | 4,908 | 5,216 | 4,900 | 4,993 |
| ex-Korea YoY | n/a | +6.3% | -6.1% | +1.9% |

KRW per USD is the simple average of daily Yahoo Finance KRW=X closes over each 1 Jun to 31 May (1,320.7; 1,325.5; 1,400.2; 1,434.9; market data), so the USD column carries an error of perhaps 1 to 2%; the share column moves by at most about 0.4 point for a 2% FX error and the trend is unaffected. Korea is assumed to sit inside APLA (the 10-K does not list countries). Caveat: the Korean LLC sells only to Korean customers and its own stores, whereas APLA also contains Latin America, Japan, Australia, India and others.

Alternatives for "Korea is falling faster" tested:
- *Currency:* ruled out, KRW revenue is local currency.
- *Fiscal-year mismatch:* ruled out, both end 31 May.
- *Channel mix change inside Korea:* cannot be tested; the audit report has one revenue line (goods sales KRW 1,793.4bn plus KRW 0.2bn other). Surviving, not separable: loss of franchise sell-in vs lower own-store and digital sales vs price. Data that would decide: Nike Korea franchise partner sell-in or Korean card-spending data for sports retail (KB or Hyundai Card; not obtained).
- *Units vs price:* not separable from the filing. Revenue per pair is not disclosed at country level.

### 3.5 Tax and withholding items (OPENED, notes)

- FY21 note: Seoul Regional Tax Office audit of the company's 5th to 10th fiscal periods (FY15 to FY20); KRW 17.7bn of corporate tax and penalties assessed and paid, KRW 9.0bn more expected and expensed; appeal at the Tax Tribunal.
- FY22: audit of 2017 to 2020 produced assessed tax on withholding for related parties; the company booked an "other provision" of KRW 206.6bn (about $174M at the FY22 average rate) with an offsetting asset for the amount borne by related parties.
- FY23: after the tax appeal process (result notified June 2023) the assessment was cancelled; the KRW 206.6bn provision reversed to zero and the cancelled tax and a transfer price adjustment (-13.1bn) were booked (effective tax rate -53.4%, net income KRW 106.3bn).
- FY24: a refund of 2015 to 2016 tax following a Tax Tribunal decision reduced FY24 tax expense.
This is a Korean tax-authority dispute that Nike won on appeal; nothing recurs in FY26. It matters only because it confirms that Korean transfer pricing is actively audited and adjusted, which is the same mechanism as the FY26 KRW 46.6bn credit.

## 4. Converse Korea LLC (KRW bn; OPENED from DART, rcpNo 20210910000526, 20220907000308, 20230907000200, 20240906000216, 20250905000091, 20260907000048)

| | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|---|---|
| Revenue | 85.8 | 92.8 | 84.5 | 74.7 | 47.0 | 30.8 |
| YoY (DERIVED) | +28.7% | +8.1% | -8.9% | -11.6% | -37.0% | -34.4% |
| Gross profit | 41.6 | 45.3 | 33.2 | 27.3 | 15.5 | 10.8 |
| Gross margin | 48.5% | 48.8% | 39.3% | 36.6% | 33.0% | 34.9% |
| Operating profit | 9.9 | 9.2 | -2.2 | -5.0 | -8.8 | -8.8 |
| Net income | 11.8 | 6.5 | -2.8 | -8.7 | -9.7 | -12.2 |
| Inventory (net) | 16.3 | 9.8 | 16.8 | 13.2 | 9.5 | 6.8 |
| Receivables | 6.0 | 8.8 | 10.2 | 12.1 | 5.4 | 4.7 |
| Returns provision | 1.6 | 2.4 | 2.1 | 2.2 | 1.1 | 2.0 |
| Equity | 0.3 | 7.4 | 5.0 | -3.1 | -12.1 | -23.5 |

FY26 detail (OPENED): inventory of goods KRW 4.9bn vs 11.2bn with valuation allowance KRW 0.9bn vs 2.9bn; in-transit KRW 2.8bn vs 1.1bn; borrowing USD 8M facility from the parent Converse Netherlands B.V. at TSFR 1M + 308 bp, due 5 Oct 2030, KRW 10.5bn drawn (now non-current; KRW 9.7bn current in FY25); trade payables KRW 18.9bn vs 11.4bn (+66%), a payable build to related parties that funds the loss (DERIVED; the payee split was not read). Corporate tax: none (no taxable income; no deferred tax asset recognised). The Converse segment gross margin reported by the group was already analysed in `08_converse_detail.md`; this is the Korean country slice: revenue -66.8% from FY22, gross margin down 13.9 points over the same period (48.8% to 34.9%) (DERIVED), and SG&A of KRW 19.6bn exceeds gross profit of KRW 10.8bn. Converse Korea is supported by an administrative-services contract with Nike Korea (KRW 1.6bn a year paid, OPENED).

## 5. Nike Retail B.V., EMEA (EUR millions; OPENED from Companies House FC019114, OCR)

The principal that distributes Nike products across EMEA (registered Hilversum; accounts filed in the UK as an overseas company). Nike European Operations Netherlands B.V. merged into it on 1 May 2022 with carryover accounting from 1 Jun 2021 and no restatement of the FY21 comparative, so FY22 (the first merged year) is the first like-for-like year and FY21 is not comparable (EUR 2,628.6M revenue, retail only). FY22 headcount (7,239) rises to 9,193 in FY23 without a stated reason. FY25 revenue EUR 10,977M is about 97% of reported EMEA revenue converted at roughly $1.08 per EUR (DERIVED, rough), so this is nearly the whole segment. Statutory result is on the entity's own accounting policies.

| | FY22 | FY23 | FY24 | FY25 |
|---|---|---|---|---|
| Revenue | 10,710.5 | 12,702.9 | 12,354.8 | 10,977.3 |
| YoY | n/a | +18.6% | -2.7% | -11.2% |
| of which Netherlands | 834.6 | 924.4 | 1,051.4 | 1,009.9 |
| of which rest of EMEA | 9,521.6 | 11,548.7 | 11,100.1 | 9,807.7 |
| rest of EMEA YoY | n/a | +21.3% | -3.9% | -11.6% |
| of which other | 354.2 | 229.8 | 203.3 | 159.7 |
| Trade revenue / other revenue | 10,439.5 / 271.0 | 12,494.0 / 208.9 | 12,153.0 / 201.8 | 10,800.6 / 176.7 |
| Gross profit | 2,807.7 | 3,192.0 | 2,805.3 | 2,495.0 |
| Gross margin | 26.2% | 25.1% | 22.7% | 22.7% |
| Operating profit | 318.2 | 423.6 | -324.2 | -36.0 |
| Operating margin | 3.0% | 3.3% | -2.6% | -0.3% |
| Net result | 902.7 | 778.0 | 94.2 | 426.1 |
| Inventories | 1,174.1 | 1,536.3 | 1,225.9 | 1,288.5 |
| of which finished goods | n/a | 1,139.4 | 1,049.6 | 972.0 |
| of which in transit | n/a | 396.9 | 176.3 | 316.4 |
| Trade accounts receivable | 917.9 | 746.6 | 715.3 | 904.5 |
| Trade receivable days (DERIVED, on trade revenue) | 32.1 | 21.8 | 21.5 | 30.6 |
| Bad-debt reserve (trade receivables) | n/a | 5.7 | 2.8 | 11.7 |
| Average employees | 7,239 | 9,193 | 9,489 | 9,155 |
| Equity | n/a | 3,417.0 | 3,127.3 | 3,560.6 |

Other items (OPENED): NRBV discloses the European Commission State Aid investigation (opened Jan 2019, tax rulings granted to NEON) as an unresolved risk in FY22 and FY25 with no provision; cost of inventories expensed EUR 5,481.5M (FY24: 6,165.8M); PwC's report (27 Jan 2026) lists a fraud risk on revenue recognition (existence, occurrence and cut-off of revenue and unsettled revenue in accounts receivable) and concludes that no material going-concern uncertainty exists, with no specific indications of fraud (OCR text); guarantees to banks and the Belgian customs paragraph are as in G10 (no provision).

Reading (DERIVED):
- **Revenue decomposition FY25:** -EUR 1,377.5M in total: rest of EMEA -1,292.4, Netherlands -41.5, other -43.6. The one line the filing gives is geography; units, price and channel are not given. Group: EMEA reported revenue $12,257M, -9.9% (10-K) against NRBV in EUR -11.2%; the currencies differ and I did not pull EUR/USD averages, so the 1.3 point gap is not interpreted. Not separable further.
- **Gross margin is flat at 22.7% in FY24 and FY25 after -2.4 points in FY24**; the loss of 2.4 points (25.1% to 22.7%) happened in FY24 when revenue was nearly flat (-2.7%), then did not recover. The company-level bridge items are not given; the group's own EMEA gross margin bridge is in the 10-K.
- **Operating profit** improved by EUR 288M in FY25 (-324.2 to -36.0) on EUR 310M less gross profit, so operating expenses fell EUR 598M: selling -61.4 and G&A -537.1 (G&A FY24 1,873.2 to FY25 1,336.0). G&A in FY24 was EUR 254M above FY23; the FY25 level is EUR 283M below FY23 (1,619.1). The entity's G&A includes intercompany charges, so the drop is a mix of real cost (headcount -3.5% in FY25) and recharges. Not separable.
- **Inventory:** finished goods fell 7.4% but in-transit goods rose 79.5% (EUR 316.4M vs 176.3M), so total inventory is +5.1% against revenue -11.2%. Days of cost of inventories expensed: 365 x 1,288.5 / 5,481.5 = 85.8 days at FY25 vs 365 x 1,225.9 / 6,165.8 = 72.6 days at FY24 (DERIVED; this cost of inventories line is only part of cost of sales of EUR 8,482M, so absolute days are indicative, the +13 day change is the point). Inventory to revenue is 11.7% at FY25 vs 9.9% at FY24, 12.1% at FY23 and 11.0% at FY22 (DERIVED), so the FY25 level is inside the four-year range. Alternatives: (a) timing of shipments (in transit rose 140M), (b) a deliberate pre-build for FY26, (c) lower sell-through. Not separable; group inventory at 31 May 2026 was $7,501M vs $7,489M (flat, 10-K), so the group did not unwind it in FY26.
- **Receivables:** trade receivable days of 30.6 at FY25 are back near the FY22 level of 32.1 after 21.5 to 21.8 in FY23 and FY24, so FY25 is a reversion to the FY22 level rather than an unprecedented high (DERIVED). Trade receivables +26.5% on trade revenue -11.1%: the move is customer balances, not intercompany (receivables from affiliates fell from EUR 114.0M to 79.4M). Candidates: later-quarter wholesale shipments, slower payment, longer terms. Same ambiguity as G2.

## 6. UK

- **Nike (UK) Limited (01887016), FY21 (OPENED, OCR):** revenue GBP 63.3M (-20.6% vs 79.8M), operating profit GBP 20.1M (31.7% margin on a cost-plus type revenue line), net profit GBP 15.6M, net assets GBP 111.0M, 260 average employees (279 in FY20; selling 72, administration 188). Revenue is "a commission based upon a fixed percentage of the revenues generated on behalf of Nike group companies" in the UK and Ireland plus reimbursement of local costs, so it is not a sales figure. Accounts for FY21 were prepared on a basis other than going concern: trade and assets were to transfer at book value to another Nike company and the company to be liquidated within a year; dissolved by voluntary strike-off 4 Jun 2024. No accounts for FY22 or later exist. UK sales therefore sit in Nike Retail B.V., which reports no UK split.
- **Nike Retail UK (BR003350) and Nike 360 UK Branch (BR017640):** UK establishments of Dutch companies; the register carries no separate accounts.
- **Converse Retail (UK) Limited (10584502), OPENED:** turnover GBP 7.345M (FY23), 3.881M (FY24, -47.2% after two outlet closures; three stores operated in the year), 3.443M (FY25, -11.3% on the one remaining outlet, Cheshire Oaks); operating profit GBP 402k, 492k, 107k; inventory GBP 282k, 249k, 226k; stock impairment expensed GBP 52.7k, 56.7k, 29.2k; average employees 51, 24, 28. The directors attribute the FY25 turnover decline to "general slowdown in retail business performance", which is the filing's wording and not an explanation I can decompose (units, price and traffic not disclosed). Group support: shareholders' funds GBP 2.27M after a GBP 1.77M share issue to the parent in FY25. Immaterial.
- **Is UK revenue falling faster than the region?** Cannot be tested at Nike level: no UK-only revenue is filed anywhere free. Nike's own UK doors are visible in the store locator (51 Nike-owned doors on 14 Oct 2026; DERIVED from `data/hunt/stores/`). What would settle it: UK Companies House filing of the UK branch of Nike Retail B.V. (none exists), the HMRC or ONS trade statistics for footwear imports (not pulled), or the Nike Retail B.V. segment note by country (not in the Dutch GAAP accounts).

## 7. Sourcing hub, Nike Flight B.V. consolidated (USD millions; OPENED, filed at Companies House under Nike 360 Holding B.V., FC032565, FY24)

Consolidated accounts of Nike Flight B.V. (the parent of Nike 360 Holding B.V.; filed in the UK for Nike 360 Holding under Article 2:403 of the Dutch Civil Code) covering the Nike Trading Company and Nike Global Trading branches in Singapore (more than 90% of revenue) plus the liaison offices (Hong Kong, Italy, Korea, Malaysia, Sri Lanka, Taiwan, Turkey, UK, Vietnam, China). They buy from factories and sell to Nike and Converse entities worldwide; Nike Korea's goods purchases (section 3.3) are bought from this hub.

| | FY23 | FY24 |
|---|---|---|
| Revenue | 21,839.6 | 20,986.9 (-3.9%) |
| Gross profit | 1,107.6 | 933.3 (4.4% of revenue vs 5.1%) |
| Operating profit | 72.8 | 111.9 |
| Net result | 135.6 | 250.3 |
| Inventories | 1,679.6 | 1,806.8 (+7.6%) |
| Accounts receivable | 2,769.0 | 2,546.1 |
| Cash | 5,448.1 | 6,276.9 |
| Average employees (company incl. subsidiaries) | | 2,678 |

Reading (DERIVED): the hub's FY24 inventory rose 7.6% while its sales to Nike entities fell 3.9%, the same sign as the group (group FY24 inventories fell 11% to $7,519M, so the hub went the other way). FY25 accounts are not yet filed (filing lag about 12 months at Companies House). The hub's margin is thin (4.4%), which is consistent with a cost-plus or low-margin routing entity and with Korea being held to a 2.0% margin: most of Nike's group profit is booked in the principal (Nike, Inc. and the US entities), not in these affiliates. That is an inference from the margins, not a statement in the filings.

## 8. Australia (ATO Corporate Tax Transparency, OPENED, data.gov.au workbooks)

Nike Australia Pty Ltd (ABN 99055141743), income years ending 2014-15 to 2024-25. AUD M:

| Year | Total income | Taxable income | Tax payable |
|---|---|---|---|
| 2018-19 | 571.8 | 14.1 | 4.2 |
| 2019-20 | 517.7 | 32.6 | 9.8 |
| 2020-21 | 722.9 | 9.1 | 2.7 |
| 2021-22 | 705.9 | 30.0 | 9.0 |
| 2022-23 | 944.3 | 42.9 | 12.9 |
| 2023-24 | 924.9 (-2.1%) | 32.2 (-25.0%) | 9.7 |
| 2024-25 | 894.0 (-3.3%) | 21.6 (-32.8%) | 6.5 |

Total income is all income (sales plus other), so it is a proxy for revenue only. The income year is a Nike-aligned year if the entity reports to 31 May (the register does not state the year end; Nike's fiscal year is the likeliest). Taxable income is about 2.4% of total income in 2024-25, in the same low-single-digit range as Korea's ex-TP 2.0%, which again points to a limited-risk distributor margin. FY26 data (income year 2025-26) is published by the ATO around Oct to Dec 2027, so APLA's FY26 Australia datum is not available. Australia: 44 Nike doors, of which 10 Nike-owned and 34 mono-brand partners (Oct 2026 locator). Australia total income fell less (-3.3%) than Korea (-5.7%) in the matching year, and 2024-25 is the only year both exist.

## 9. Japan, India, Taiwan, Hong Kong, Singapore, Canada, Switzerland, Belgium: what I could not get

| Entity | Why |
|---|---|
| Nike Japan Group LLC | A godo kaisha (合同会社) is not required to publish financial notices; the Kanpo-based database (catr.jp) returns no Nike result; the official Kanpo site is blocked by the session's egress proxy; the Korean audit report names Nike Japan Group LLC as a related party but with only KRW 0.2bn of sales to it. |
| Nike India Pvt Ltd | MCA, Zauba and TheCompanyCheck return 403; Tofler error; no free alternative opened. MCA filings are paid per document. |
| Taiwan, Hong Kong | Taiwan GCIS (findbiz) 403; Hong Kong ICRIS is a paid search; a liaison office of Nike 360 exists in each (section 7) but no standalone accounts were found. |
| Singapore | Nike Global Trading and Nike Trading Company are Dutch B.V. companies with Singapore branches; their results sit in Nike 360 Holding B.V. (section 7), not in a Singapore filer. ACRA BizFile is paid. |
| Canada | No public financial filing regime for Nike Canada Corp found. |
| Switzerland | Zefix is reachable but lists legal form, address and purpose only; no financials. NRBV formed a Switzerland branch on 1 Feb 2023 (OPENED NRBV FY25 text). |
| Belgium (NBB) | The NBB consult API answered but needs a parameter I could not infer; G10 route 6a stands (no operating Belgian legal entity files). |

## 10. Routes log (worked, blocked, partial)

| # | Target | Route | Result |
|---|---|---|---|
| 1 | Nike Korea | DART detailSearch by company name "나이키코리아" with a 5-year window | Partial: the search returns nothing when the date span exceeds about 3 years or when the name differs; worked once windows were narrowed to 1 Aug to 31 Oct of each year |
| 2 | Nike Korea | DART search of all 감사보고서 filed on 11 Sep 2026, then the filing viewer for the financial statements | Worked: FY26 found, rcpNo 20260911000443 |
| 3 | Nike Korea | Year-by-year windows for FY21 to FY25 | Worked; FY20 (filed 2020) and older not on DART (empty for 2018 to 2020; Nike Korea began filing external audit reports in 2021) |
| 4 | Nike Korea | NewsSpace article on the FY26 audit report | Worked as secondary cross-check (figures match) |
| 5 | Nike Korea | Catch.co.kr and Saramin company pages | Blocked (catch 403); not needed once DART worked |
| 6 | Converse Korea | DART by name for each year | Worked (FY21 to FY26) |
| 7 | UK | Companies House search (names containing NIKE, CONVERSE) and filing histories, PDF download | Worked; PDFs are scanned images, read with RapidOCR (page images at 2.2x); Nike (UK) FY21 and Converse Retail UK FY24 and FY25, NRBV FY22, FY24 and FY25 and Nike Flight FY24 OCR complete (about 5 to 8 minutes per file); Nike 360 FY22, Converse Retail FY22 and NRBV FY23/FY21/FY20 not OCRed (comparatives in later reports used instead) |
| 8 | Netherlands | KvK (paid) not used; UK Companies House overseas-company copies of NRBV (FC019114) and Nike 360 Holding (FC032565) | Worked |
| 9 | Netherlands | Other Nike Dutch entities in the UK register (Nike Retail UK, Nike 360 UK Branch are UK establishments only; Nike European Operations Netherlands merged into NRBV on 1 May 2022 per G10) | Partial |
| 10 | Belgium | NBB Balanscentrale API | Partial (parameter unknown); G10 6a result reused |
| 11 | Australia | ATO Corporate Tax Transparency workbooks (11 years) | Worked (tax data, not statements) |
| 12 | Japan | Kanpo official site | Blocked by egress proxy |
| 13 | Japan | catr.jp (Kanpo-based 決算 database) search "ナイキ" | Worked mechanically: no Nike result (consistent with no publication duty for a 合同会社) |
| 14 | Japan | gBizINFO | Blocked (500 error); the API needs a registered token (not requested, because registration needs an email address and I do not send the user's) |
| 15 | India | MCA, Zauba, TheCompanyCheck, Tofler, IndiaFilings | Blocked or empty |
| 16 | Taiwan | GCIS findbiz | Blocked (403) |
| 17 | Hong Kong, Singapore | ICRIS, BizFile (paid search) | Blocked or paid |
| 18 | Ireland | CRO | Blocked (403) |
| 19 | Web search for Japan, India, Taiwan | Search tool | Blocked: the session's search budget was used up after the Korea searches; I did not use curl against a search engine |

The CLAUDE.md rule asks for five different routes before reporting "inconclusive". For Japan I tried routes 12 to 14 plus the legal-duty check (a 合同会社 does not publish), which together make four routes; the fifth available route (a Japanese credit-bureau extract such as Teikoku Databank or Tokyo Shoko Research) is paid. For India I tried five sites (route 15). For Taiwan, Hong Kong, Singapore, Canada and Switzerland I reached fewer than five and the status is "not obtained", not "inconclusive": see section 11 for the follow-up.

## 11. What I could not get, and what would settle it

- **UK retail revenue and returns provisions:** not filed separately anywhere free. Settled by the country note of the Nike Retail B.V. consolidation at KvK (paid, about EUR 2.25 per extract) or a Refinitiv or Orbis pull for "Nike Retail B.V." segment data.
- **Nike Retail B.V. FY21 and earlier, and Nike Flight FY22 and earlier:** scanned PDFs exist on Companies House (NRBV FY20 to FY23, Nike 360 FY17 to FY23) but were not OCRed because the OCR took 5 to 8 minutes a file; NRBV FY21 is pre-merger and not comparable anyway. The sourcing hub's FY22 and FY21 would give the sales-to-Nike-entities trend over a longer window.
- **Nike Korea headcount and store count:** not in the audit report. Salaries KRW 80.6bn only.
- **Korea units vs price:** not disclosed.
- **Japan:** a Teikoku Databank report on ナイキジャパングループ合同会社 (paid) or the Japanese customs HS 6403 import series for Nike's share (free but not done).
- **India:** MCA V3 filings (paid per document) for Nike India Pvt Ltd.
- **FY26 for NRBV and the sourcing hub:** will appear on Companies House in about April 2027.

## 12. Verdict for the pitch

Use, with these exact words and labels:
- "Nike Korea LLC, whose audit reports are public on DART, saw KRW revenue fall 5.7% in FY25 and 5.2% in FY26 (fiscal years to 31 May), against APLA currency-neutral growth of -3% and -1%; its share of APLA revenue is about 20% in FY26 from 23.7% in FY23 (share is my arithmetic with approximate FX)."
- "The rise in Nike Korea's FY26 operating profit (KRW 37.8bn to 82.5bn) is more than explained by a KRW 46.6bn transfer price credit in cost of sales; before it, the operating margin is 2.00%, the same as FY25."
- "Nike Retail B.V. (EMEA principal, UK-filed accounts) shows revenue -11.2%, inventory +5.1% and trade receivable days +9.1 in FY25."
Do not use: local EBIT of any selling subsidiary as evidence of consumer demand, or the Korean returns charge ratio as a level (definition unknown). Smoking gun: no; the local data supports a SHORT only as a third source for the same two signals already in the 10-K (wholesale receivables days and inventory), and it adds the Korea share-loss datapoint and the Converse Korea loss and negative equity.
