# O_COMPETITORS: Nike versus the athletic peer set (structural share loss or Nike-specific problem?)

Prepared 2026-10-13. Raw downloads: `scratchpad/peers2/` (SEC filings) and `scratchpad/peers2/web/` (adidas, Puma, ASICS, Anta, Li Ning IR and HKEX files). All downloads were treated as untrusted data and read with `python3 -I` or `pdftotext`.

**Verification.** A script (`scratchpad/scripts2/verify.py`) checked every peer quote in Section A against the downloaded source text. 355 of 355 peer rows matched once whitespace, table pipes, curly quotes and hyphens were normalised. The 37 Nike rows are copied from `data/nike_filing_facts.csv`, which an earlier pipeline had already verified. Quotes are verbatim, with two exceptions: en and em dashes were changed to hyphens, and double quotes were removed (both required by the output format). Every value labelled "derived" is my own calculation from printed figures. Nothing in this file relies on a search snippet alone. One web search was used to find the Li Ning HKEX PDF, and the PDF itself was then downloaded and read.

**Sources by peer**
- **SEC filings (8-K or 6-K earnings exhibits):** Deckers (HOKA), On Holding, Lululemon, Under Armour, Skechers, VF Corp (Vans), Amer Sports and Birkenstock.
  - Skechers was taken private. Its merger closed and NYSE delisting was requested on 2025-09-12 (8-K). Its last results cover calendar Q2 2025.
- **Company IR sites:** adidas (adidas-group.com results releases), Puma (about.puma.com releases) and ASICS (corp.asics.com Q2 2026 financial summary).
- **Hong Kong filings:** Anta (ir.anta.com, quarterly operational updates and the 2026 interim results announcement) and Li Ning (HKEX 2026 interim results announcement).
- **Gaps:**
  - ASICS: only H1 2026 was extracted.
  - Anta: discloses quarterly retail-sales growth only as ranges, with revenue half-yearly.
  - Li Ning: only H1 2026 was extracted.

**Calendar alignment rule.** Nike's fiscal year ends May 31. I assign each Nike quarter to the calendar quarter that holds most of its months:

| Nike quarter | Months | Calendar quarter |
|---|---|---|
| Q1 | Jun-Aug | CQ3 |
| Q2 | Sep-Nov | CQ4 |
| Q3 | Dec-Feb | CQ1 of the next year |
| Q4 | Mar-May | CQ2 |

Peer quarters are assigned the same way:
- **Calendar-year reporters** (On, Amer, Skechers, adidas, Puma, ASICS, Anta, Li Ning) map directly.
- **Deckers, Under Armour and VF** (fiscal years ending around March 31) map directly, for example Apr-Jun is CQ2.
- **Lululemon** (Feb-Jan year): Feb-Apr is CQ1, May-Jul CQ2, Aug-Oct CQ3 and Nov-Jan CQ4.
- **Birkenstock** (Oct-Sep year) maps directly.

Each Nike quarter therefore sits about one month later than its peer comparison. Nike's latest quarter (Q1 FY27, Jun-Aug 2026 = CQ3 2026) has almost no peer counterpart yet. The exceptions are Amer Sports' preliminary Q3 2026 outlook of +20 to 22%, and Lululemon's May-Jul quarter, which overlaps Nike's by two months.

## A. Data (CSV)

```csv
company,metric,period,calendar_quarter,value,unit,source,url,page_or_section,quote
Nike,ebit_margin,FY2024,FY,12.7,%,FY2024 Form 10-K (filed 2024-07-25),https://www.sec.gov/Archives/edgar/data/320187/000032018724000044/nke-20240531.htm,p. 31,EBIT Margin 12.7% 12.1% 14.7%
Nike,ebit_margin,FY2025,FY,8.2,%,Q4 FY2025 earnings release; 8-K Ex. 99.1 (filed 2025-06-26),https://www.sec.gov/Archives/edgar/data/320187/000032018725000034/q4fy25exhibit991er.htm,p. 6 of exhibit,EBIT margin 1 2.7 13.3 8.2 12.7
Nike,ebit_margin,FY2026,FY,8.3,%,FY2026 Form 10-K (filed 2026-07-15),https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm,p. 31,EBIT margin 8.3% 8.2% 12.7%
Nike,ebit_margin,Q1FY2027 (Jun-Aug),2026Q3,8.1,%,Q1 FY2027 Form 10-Q (filed 2026-10-02),https://www.sec.gov/Archives/edgar/data/320187/000032018726000193/nke-20260831.htm,p. 21,EBIT margin 8.1% 7.7%
Nike,gross_margin,FY2024,FY,44.6,%,FY2024 Form 10-K (filed 2024-07-25),https://www.sec.gov/Archives/edgar/data/320187/000032018724000044/nke-20240531.htm,p. 33,Gross margin 44.6 43.5 46.0
Nike,gross_margin,FY2025,FY,42.7,%,FY2025 Form 10-K (filed 2025-07-17),https://www.sec.gov/Archives/edgar/data/320187/000032018725000047/nke-20250531.htm,p. 32,Gross margin 42.7 44.6 43.5
Nike,gross_margin,FY2026,FY,42.9,%,FY2026 Form 10-K (filed 2026-07-15),https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm,p. 32,Gross margin 42.9 42.7 44.6
Nike,gross_margin,Q1FY2027 (Jun-Aug),2026Q3,42.8,%,Q1 FY2027 Form 10-Q (filed 2026-10-02),https://www.sec.gov/Archives/edgar/data/320187/000032018726000193/nke-20260831.htm,p. 22,Gross margin 42.8% 42.2% 60 bps
Nike,gross_margin,Q4FY2026 (Mar-May),2026Q2,49.2,%,Q4 FY2026 earnings release; 8-K Ex. 99.1 (filed 2026-06-30),https://www.sec.gov/Archives/edgar/data/320187/000032018726000076/q4fy26exhibit991er.htm,p. 2 of exhibit,Gross margin 49.2 40.3 42.9 42.7
Nike,greater_china_growth_cc,FY2026,FY,-13,%,FY2026 Form 10-K (filed 2026-07-15),https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm,p. 36,"Greater China 5,847 6,586 -11 -13"
Nike,greater_china_growth_cc,Q1FY2027 (Jun-Aug),2026Q3,-26,%,Q1 FY2027 Form 10-Q (filed 2026-10-02),https://www.sec.gov/Archives/edgar/data/320187/000032018726000193/nke-20260831.htm,p. 25,"Greater China 1,180 1,512 -22 -26"
Nike,greater_china_growth_cc,Q2FY2026 (Sep-Nov),2025Q4,-16,%,Q2 FY2026 Form 10-Q (filed 2025-12-30),https://www.sec.gov/Archives/edgar/data/320187/000032018725000151/nke-20251130.htm,p. 29,"Greater China 1,423 1,711 -17 -16"
Nike,greater_china_growth_cc,Q3FY2026 (Dec-Feb),2026Q1,-10,%,Q3 FY2026 Form 10-Q (filed 2026-04-01),https://www.sec.gov/Archives/edgar/data/320187/000032018726000037/nke-20260228.htm,p. 32,"Greater China 1,615 1,733 -7 -10"
Nike,greater_china_growth_cc,Q4FY2026 (Mar-May),2026Q2,-17,%,Q4 FY2026 earnings release; 8-K Ex. 99.1 (filed 2026-06-30),https://www.sec.gov/Archives/edgar/data/320187/000032018726000076/q4fy26exhibit991er.htm,p. 4 of exhibit,"Total 1,297 1,476 -12 -17"
Nike,revenue_growth_cc,FY2025,FY,-9,%,Q4 FY2025 earnings release; 8-K Ex. 99.1 (filed 2025-06-26),https://www.sec.gov/Archives/edgar/data/320187/000032018725000034/q4fy25exhibit991er.htm,p. 1 of exhibit,down 9 percent on a currency-neutral basis
Nike,revenue_growth_cc,FY2026,FY,-2,%,Q4 FY2026 earnings release; 8-K Ex. 99.1 (filed 2026-06-30),https://www.sec.gov/Archives/edgar/data/320187/000032018726000076/q4fy26exhibit991er.htm,p. 1 of exhibit,flat on a reported basis and down 2 percent on a currency-neutral basis
Nike,revenue_growth_cc,Q1FY2025 (Jun-Aug),2024Q3,-9,%,Q1 FY2025 earnings release; 8-K Ex. 99.1 (filed 2024-10-01),https://www.sec.gov/Archives/edgar/data/320187/000032018724000062/q1fy25exhibit991er.htm,p. 1 of exhibit,down 9 percent on a currency-neutral basis
Nike,revenue_growth_cc,Q1FY2026 (Jun-Aug),2025Q3,-1,%,Q1 FY2026 earnings release; 8-K Ex. 99.1 (filed 2025-09-30),https://www.sec.gov/Archives/edgar/data/320187/000032018725000091/q1fy26exhibit991er.htm,p. 1 of exhibit,down 1 percent on a currency-neutral basis
Nike,revenue_growth_cc,Q1FY2027 (Jun-Aug),2026Q3,-5,%,Q1 FY2027 earnings release; 8-K Ex. 99.1 (filed 2026-10-01),https://www.sec.gov/Archives/edgar/data/320187/000032018726000184/q1fy27exhibit991er.htm,p. 1 of exhibit,down 4 percent on a reported basis and down 5 percent on a currency-neutral basis
Nike,revenue_growth_cc,Q2FY2025 (Sep-Nov),2024Q4,-9,%,Q2 FY2025 earnings release; 8-K Ex. 99.1 (filed 2024-12-19),https://www.sec.gov/Archives/edgar/data/320187/000032018724000069/q2fy25exhibit991er.htm,p. 1 of exhibit,down 9 percent on a currency-neutral basis
Nike,revenue_growth_cc,Q2FY2026 (Sep-Nov),2025Q4,0,%,Q2 FY2026 earnings release; 8-K Ex. 99.1 (filed 2025-12-18),https://www.sec.gov/Archives/edgar/data/320187/000032018725000138/q2fy26exhibit991er.htm,p. 1 of exhibit,up 1 percent on a reported basis and flat on a currency-neutral basis
Nike,revenue_growth_cc,Q3FY2025 (Dec-Feb),2025Q1,-7,%,Q3 FY2025 earnings release; 8-K Ex. 99.1 (filed 2025-03-20),https://www.sec.gov/Archives/edgar/data/320187/000032018725000011/q3fy25exhibit991er.htm,p. 1 of exhibit,down 7 percent on a currency-neutral basis
Nike,revenue_growth_cc,Q3FY2026 (Dec-Feb),2026Q1,-3,%,Q3 FY2026 earnings release; 8-K Ex. 99.1 (filed 2026-03-31),https://www.sec.gov/Archives/edgar/data/320187/000032018726000026/q3fy26exhibit991er.htm,p. 1 of exhibit,flat on a reported basis and down 3 percent on a currency-neutral basis
Nike,revenue_growth_cc,Q4FY2025 (Mar-May),2025Q2,-11,%,Q4 FY2025 earnings release; 8-K Ex. 99.1 (filed 2025-06-26),https://www.sec.gov/Archives/edgar/data/320187/000032018725000034/q4fy25exhibit991er.htm,p. 1 of exhibit,down 12 percent on a reported basis and down 11 percent on a currency-neutral basis
Nike,revenue_growth_cc,Q4FY2026 (Mar-May),2026Q2,-4,%,Q4 FY2026 earnings release; 8-K Ex. 99.1 (filed 2026-06-30),https://www.sec.gov/Archives/edgar/data/320187/000032018726000076/q4fy26exhibit991er.htm,p. 1 of exhibit,down 1 percent on a reported basis and down 4 percent on a currency-neutral basis
Nike,revenue,FY2024,FY,51362,USD m,FY2024 Form 10-K (filed 2024-07-25),https://www.sec.gov/Archives/edgar/data/320187/000032018724000044/nke-20240531.htm,p. 57,"Revenues 51,362 51,217 46,710"
Nike,revenue,FY2025,FY,46309,USD m,FY2025 Form 10-K (filed 2025-07-17),https://www.sec.gov/Archives/edgar/data/320187/000032018725000047/nke-20250531.htm,p. 32,"Revenues 46,309 51,362 -10 51,217 0"
Nike,revenue,FY2026,FY,46398,USD m,FY2026 Form 10-K (filed 2026-07-15),https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm,p. 55,"Revenues 46,398 46,309 51,362"
Nike,revenue,Q1FY2025 (Jun-Aug),2024Q3,11589,USD m,Q1 FY2025 Form 10-Q (filed 2024-10-07),https://www.sec.gov/Archives/edgar/data/320187/000032018724000065/nke-20240831.htm,p. 1,"Revenues 11,589 12,939"
Nike,revenue,Q1FY2026 (Jun-Aug),2025Q3,11720,USD m,Q1 FY2026 Form 10-Q (filed 2025-10-01),https://www.sec.gov/Archives/edgar/data/320187/000032018725000097/nke-20250831.htm,p. 1,"Revenues 11,720 11,589"
Nike,revenue,Q1FY2027 (Jun-Aug),2026Q3,11213,USD m,Q1 FY2027 Form 10-Q (filed 2026-10-02),https://www.sec.gov/Archives/edgar/data/320187/000032018726000193/nke-20260831.htm,p. 1,"Revenues 11,213 11,720"
Nike,revenue,Q2FY2025 (Sep-Nov),2024Q4,12354,USD m,Q2 FY2025 Form 10-Q (filed 2025-01-03),https://www.sec.gov/Archives/edgar/data/320187/000032018725000004/nke-20241130.htm,p. 1,"Revenues 12,354 13,388 23,943 26,327"
Nike,revenue,Q2FY2026 (Sep-Nov),2025Q4,12427,USD m,Q2 FY2026 Form 10-Q (filed 2025-12-30),https://www.sec.gov/Archives/edgar/data/320187/000032018725000151/nke-20251130.htm,p. 1,"Revenues 12,427 12,354 24,147 23,943"
Nike,revenue,Q3FY2025 (Dec-Feb),2025Q1,11269,USD m,Q3 FY2025 Form 10-Q (filed 2025-04-03),https://www.sec.gov/Archives/edgar/data/320187/000032018725000016/nke-20250228.htm,p. 1,"Revenues 11,269 12,429 35,212 38,756"
Nike,revenue,Q3FY2026 (Dec-Feb),2026Q1,11279,USD m,Q3 FY2026 Form 10-Q (filed 2026-04-01),https://www.sec.gov/Archives/edgar/data/320187/000032018726000037/nke-20260228.htm,p. 1,"Revenues 11,279 11,269 35,426 35,212"
Nike,revenue,Q4FY2025 (Mar-May),2025Q2,11097,USD m,Q4 FY2025 earnings release; 8-K Ex. 99.1 (filed 2025-06-26),https://www.sec.gov/Archives/edgar/data/320187/000032018725000034/q4fy25exhibit991er.htm,p. 2 of exhibit,"Revenues 11,097 12,606 -12 46,309 51,362 -10"
Nike,revenue,Q4FY2026 (Mar-May),2026Q2,10972,USD m,Q4 FY2026 earnings release; 8-K Ex. 99.1 (filed 2026-06-30),https://www.sec.gov/Archives/edgar/data/320187/000032018726000076/q4fy26exhibit991er.htm,p. 2 of exhibit,"Revenues 10,972 11,097 -1 46,398 46,309 0"
Deckers,revenue,Q1 FY27 (Apr-Jun 2026),2026Q2,1019.5,USD m,8-K Ex.99.1 2026-07-23,https://www.sec.gov/Archives/edgar/data/910521/000091052126000015/deckex991pressrelease-6302.htm,First Quarter Fiscal 2027 Financial Review,"Net sales increased 5.7% to $1.020 billion compared to $964.5 million. On a constant currency basis, net sales increased 4.8%."
Deckers,revenue_growth_reported,Q1 FY27,2026Q2,5.7,%,8-K Ex.99.1 2026-07-23,https://www.sec.gov/Archives/edgar/data/910521/000091052126000015/deckex991pressrelease-6302.htm,First Quarter Fiscal 2027 Financial Review,Net sales increased 5.7% to $1.020 billion compared to $964.5 million.
Deckers,revenue_growth_cc,Q1 FY27,2026Q2,4.8,%,8-K Ex.99.1 2026-07-23,https://www.sec.gov/Archives/edgar/data/910521/000091052126000015/deckex991pressrelease-6302.htm,First Quarter Fiscal 2027 Financial Review,"On a constant currency basis, net sales increased 4.8%."
Deckers,hoka_growth,Q1 FY27,2026Q2,7.7,%,8-K Ex.99.1 2026-07-23,https://www.sec.gov/Archives/edgar/data/910521/000091052126000015/deckex991pressrelease-6302.htm,Brand,HOKA® brand net sales increased 7.7% to $703.5 million compared to $653.1 million.
Deckers,dtc_growth,Q1 FY27,2026Q2,13.0,%,8-K Ex.99.1 2026-07-23,https://www.sec.gov/Archives/edgar/data/910521/000091052126000015/deckex991pressrelease-6302.htm,Channel,Direct-to-Consumer (DTC) net sales increased 13.0% to $352.8 million compared to $312.2 million.
Deckers,wholesale_growth,Q1 FY27,2026Q2,2.2,%,8-K Ex.99.1 2026-07-23,https://www.sec.gov/Archives/edgar/data/910521/000091052126000015/deckex991pressrelease-6302.htm,Channel,Wholesale net sales increased 2.2% to $666.7 million compared to $652.4 million.
Deckers,international_growth,Q1 FY27,2026Q2,8.4,%,8-K Ex.99.1 2026-07-23,https://www.sec.gov/Archives/edgar/data/910521/000091052126000015/deckex991pressrelease-6302.htm,Geography,International net sales increased 8.4% to $502.1 million compared to $463.3 million.
Deckers,gross_margin,Q1 FY27,2026Q2,56.4,%,8-K Ex.99.1 2026-07-23,https://www.sec.gov/Archives/edgar/data/910521/000091052126000015/deckex991pressrelease-6302.htm,First Quarter Fiscal 2027 Financial Review,Gross margin was 56.4% compared to 55.8%.
Deckers,operating_margin (derived: 155.3/1019.5),Q1 FY27,2026Q2,15.2,%,8-K Ex.99.1 2026-07-23,https://www.sec.gov/Archives/edgar/data/910521/000091052126000015/deckex991pressrelease-6302.htm,First Quarter Fiscal 2027 Financial Review,Operating income was $155.3 million compared to $165.3 million.
Deckers,inventory_growth (derived: 807.6/849.4-1),Jun 30 2026,2026Q2,-4.9,%,8-K Ex.99.1 2026-07-23,https://www.sec.gov/Archives/edgar/data/910521/000091052126000015/deckex991pressrelease-6302.htm,Balance Sheet,Inventories were $807.6 million compared to $849.4 million.
Deckers,guidance_FY27_revenue,FY27 (Apr 2026-Mar 2027),guidance,5860-5910,USD m,8-K Ex.99.1 2026-07-23,https://www.sec.gov/Archives/edgar/data/910521/000091052126000015/deckex991pressrelease-6302.htm,Full Fiscal Year 2027 Outlook,Net consolidated sales are still expected to be in the range of $5.86 billion to $5.91 billion.
Deckers,guidance_FY27_hoka,FY27,guidance,low double digit,%,8-K Ex.99.1 2026-07-23,https://www.sec.gov/Archives/edgar/data/910521/000091052126000015/deckex991pressrelease-6302.htm,Full Fiscal Year 2027 Outlook,HOKA is still expected to increase by a low-double-digit percentage versus last year.
Deckers,guidance_FY27_operating_margin,FY27,guidance,slightly better than 21.5,%,8-K Ex.99.1 2026-07-23,https://www.sec.gov/Archives/edgar/data/910521/000091052126000015/deckex991pressrelease-6302.htm,Full Fiscal Year 2027 Outlook,Operating margin is now expected to be slightly better than 21.5%.
Deckers,revenue,Q4 FY26 (Jan-Mar 2026),2026Q1,1119.3,USD m,8-K Ex.99.1 2026-05-21,https://www.sec.gov/Archives/edgar/data/910521/000091052126000007/deckex991pressrelease-3312.htm,Fourth Quarter Fiscal 2026 Financial Review,"Net sales increased 9.6% to $1.119 billion compared to $1.022 billion. On a constant currency basis, net sales increased 7.7%."
Deckers,revenue_growth_cc,Q4 FY26,2026Q1,7.7,%,8-K Ex.99.1 2026-05-21,https://www.sec.gov/Archives/edgar/data/910521/000091052126000007/deckex991pressrelease-3312.htm,Fourth Quarter Fiscal 2026 Financial Review,"On a constant currency basis, net sales increased 7.7%."
Deckers,hoka_growth,Q4 FY26,2026Q1,14.5,%,8-K Ex.99.1 2026-05-21,https://www.sec.gov/Archives/edgar/data/910521/000091052126000007/deckex991pressrelease-3312.htm,Brand,HOKA® brand net sales increased 14.5% to $671.2 million compared to $586.1 million.
Deckers,gross_margin,Q4 FY26,2026Q1,57.6,%,8-K Ex.99.1 2026-05-21,https://www.sec.gov/Archives/edgar/data/910521/000091052126000007/deckex991pressrelease-3312.htm,Fourth Quarter Fiscal 2026 Financial Review,Gross margin was 57.6% compared to 56.7%.
Deckers,operating_margin (derived: 156.7/1119.3),Q4 FY26,2026Q1,14.0,%,8-K Ex.99.1 2026-05-21,https://www.sec.gov/Archives/edgar/data/910521/000091052126000007/deckex991pressrelease-3312.htm,Fourth Quarter Fiscal 2026 Financial Review,Operating income was $156.7 million compared to $173.9 million.
Deckers,revenue,FY26 (Apr 2025-Mar 2026),FY,5472,USD m,8-K Ex.99.1 2026-05-21,https://www.sec.gov/Archives/edgar/data/910521/000091052126000007/deckex991pressrelease-3312.htm,Full Fiscal Year 2026 Financial Review,"Net sales increased 9.8% to $5.472 billion compared to $4.986 billion. On a constant currency basis, net sales increased 9.0%."
Deckers,hoka_revenue,FY26,FY,2587,USD m,8-K Ex.99.1 2026-05-21,https://www.sec.gov/Archives/edgar/data/910521/000091052126000007/deckex991pressrelease-3312.htm,Full Fiscal Year 2026 Financial Review,HOKA® brand net sales increased 15.9% to $2.587 billion compared to $2.233 billion.
Deckers,dtc_growth,FY26,FY,6.3,%,8-K Ex.99.1 2026-05-21,https://www.sec.gov/Archives/edgar/data/910521/000091052126000007/deckex991pressrelease-3312.htm,Full Fiscal Year 2026 Financial Review,DTC net sales increased 6.3% to $2.264 billion compared to $2.130 billion.
Deckers,international_growth,FY26,FY,26.8,%,8-K Ex.99.1 2026-05-21,https://www.sec.gov/Archives/edgar/data/910521/000091052126000007/deckex991pressrelease-3312.htm,Full Fiscal Year 2026 Financial Review,International net sales increased 26.8% to $2.281 billion compared to $1.799 billion.
Deckers,gross_margin,FY26,FY,57.7,%,8-K Ex.99.1 2026-05-21,https://www.sec.gov/Archives/edgar/data/910521/000091052126000007/deckex991pressrelease-3312.htm,Full Fiscal Year 2026 Financial Review,Gross margin was 57.7% compared to 57.9%.
Deckers,operating_margin (derived: 1263/5472),FY26,FY,23.1,%,8-K Ex.99.1 2026-05-21,https://www.sec.gov/Archives/edgar/data/910521/000091052126000007/deckex991pressrelease-3312.htm,Full Fiscal Year 2026 Financial Review,Operating income was $1.263 billion compared to $1.179 billion.
Deckers,inventory_growth (derived: 487.0/495.2-1),Mar 31 2026,2026Q1,-1.7,%,8-K Ex.99.1 2026-05-21,https://www.sec.gov/Archives/edgar/data/910521/000091052126000007/deckex991pressrelease-3312.htm,Balance Sheet,"Inventories, including the impact of incremental tariffs, were $487.0 million compared to $495.2 million."
Deckers,guidance_FY28_30_framework,FY28-FY30,guidance,high single digit,%,8-K Ex.99.1 2026-05-21,https://www.sec.gov/Archives/edgar/data/910521/000091052126000007/deckex991pressrelease-3312.htm,Multi-Year Financial Framework,Net consolidated sales to increase high-single-digit percentages annually.
Deckers,revenue,Q3 FY26 (Oct-Dec 2025),2025Q4,1958,USD m,8-K Ex.99.1 2026-01-29,https://www.sec.gov/Archives/edgar/data/910521/000091052126000002/deckex991pressrelease-1231.htm,Third Quarter Fiscal 2026 Financial Review,"Net sales increased 7.1% to $1.958 billion compared to $1.827 billion. On a constant currency basis, net sales increased 6.8%."
Deckers,hoka_growth,Q3 FY26,2025Q4,18.5,%,8-K Ex.99.1 2026-01-29,https://www.sec.gov/Archives/edgar/data/910521/000091052126000002/deckex991pressrelease-1231.htm,Brand,HOKA® brand net sales increased 18.5% to $628.9 million compared to $530.9 million.
Deckers,gross_margin,Q3 FY26,2025Q4,59.8,%,8-K Ex.99.1 2026-01-29,https://www.sec.gov/Archives/edgar/data/910521/000091052126000002/deckex991pressrelease-1231.htm,Third Quarter Fiscal 2026 Financial Review,Gross margin was 59.8% compared to 60.3%.
Deckers,operating_margin (derived: 614.4/1958),Q3 FY26,2025Q4,31.4,%,8-K Ex.99.1 2026-01-29,https://www.sec.gov/Archives/edgar/data/910521/000091052126000002/deckex991pressrelease-1231.htm,Third Quarter Fiscal 2026 Financial Review,Operating income was $614.4 million compared to $567.3 million.
Deckers,inventory_growth (derived: 633.5/576.7-1),Dec 31 2025,2025Q4,9.8,%,8-K Ex.99.1 2026-01-29,https://www.sec.gov/Archives/edgar/data/910521/000091052126000002/deckex991pressrelease-1231.htm,Balance Sheet,"Inventories, including the impact of incremental tariffs, were $633.5 million compared to $576.7"
Deckers,revenue,Q2 FY26 (Jul-Sep 2025),2025Q3,1431,USD m,8-K Ex.99.1 2025-10-23,https://www.sec.gov/Archives/edgar/data/910521/000091052125000041/deckex991pressrelease-9302.htm,Second Quarter Fiscal 2026 Financial Review,"Net sales increased 9.1% to $1.431 billion compared to $1.311 billion. On a constant currency basis, net sales increased 8.3%."
Deckers,hoka_growth,Q2 FY26,2025Q3,11.1,%,8-K Ex.99.1 2025-10-23,https://www.sec.gov/Archives/edgar/data/910521/000091052125000041/deckex991pressrelease-9302.htm,Brand,HOKA® brand net sales increased 11.1% to $634.1 million compared to $570.9 million.
Deckers,gross_margin,Q2 FY26,2025Q3,56.2,%,8-K Ex.99.1 2025-10-23,https://www.sec.gov/Archives/edgar/data/910521/000091052125000041/deckex991pressrelease-9302.htm,Second Quarter Fiscal 2026 Financial Review,Gross margin was 56.2% compared to 55.9%.
Deckers,operating_margin (derived: 326.5/1431),Q2 FY26,2025Q3,22.8,%,8-K Ex.99.1 2025-10-23,https://www.sec.gov/Archives/edgar/data/910521/000091052125000041/deckex991pressrelease-9302.htm,Second Quarter Fiscal 2026 Financial Review,Operating income was $326.5 million compared to $305.1 million.
Deckers,revenue,Q1 FY26 (Apr-Jun 2025),2025Q2,964.5,USD m,8-K Ex.99.1 2025-07-24,https://www.sec.gov/Archives/edgar/data/910521/000091052125000028/deckex991pressrelease-6302.htm,First Quarter Fiscal 2026 Financial Review,"Net sales increased 16.9% to $964.5 million compared to $825.3 million. On a constant currency basis, net sales increased 16.3%."
Deckers,hoka_growth,Q1 FY26,2025Q2,19.8,%,8-K Ex.99.1 2025-07-24,https://www.sec.gov/Archives/edgar/data/910521/000091052125000028/deckex991pressrelease-6302.htm,Brand,HOKA® brand net sales increased 19.8% to $653.1 million compared to $545.2 million.
Deckers,gross_margin,Q1 FY26,2025Q2,55.8,%,8-K Ex.99.1 2025-07-24,https://www.sec.gov/Archives/edgar/data/910521/000091052125000028/deckex991pressrelease-6302.htm,First Quarter Fiscal 2026 Financial Review,Gross margin was 55.8% compared to 56.9%.
Deckers,operating_margin (derived: 165.3/964.5),Q1 FY26,2025Q2,17.1,%,8-K Ex.99.1 2025-07-24,https://www.sec.gov/Archives/edgar/data/910521/000091052125000028/deckex991pressrelease-6302.htm,First Quarter Fiscal 2026 Financial Review,Operating income was $165.3 million compared to $132.8 million.
Deckers,revenue,Q4 FY25 (Jan-Mar 2025),2025Q1,1022,USD m,8-K Ex.99.1 2025-05-22,https://www.sec.gov/Archives/edgar/data/910521/000091052125000013/deckex991pressrelease-3312.htm,Fourth Quarter Fiscal 2025 Financial Review,"Net sales increased 6.5% to $1.022 billion compared to $959.8 million. On a constant currency basis, net sales increased 7.5%."
Deckers,hoka_growth,Q4 FY25,2025Q1,10.0,%,8-K Ex.99.1 2025-05-22,https://www.sec.gov/Archives/edgar/data/910521/000091052125000013/deckex991pressrelease-3312.htm,Fourth Quarter Fiscal 2025 Financial Review,HOKA® brand net sales increased 10.0% to $586.1 million compared to $533.0 million.
Deckers,gross_margin,Q4 FY25,2025Q1,56.7,%,8-K Ex.99.1 2025-05-22,https://www.sec.gov/Archives/edgar/data/910521/000091052125000013/deckex991pressrelease-3312.htm,Fourth Quarter Fiscal 2025 Financial Review,Gross margin was 56.7% compared to 56.2%.
Deckers,operating_margin (derived: 173.9/1022),Q4 FY25,2025Q1,17.0,%,8-K Ex.99.1 2025-05-22,https://www.sec.gov/Archives/edgar/data/910521/000091052125000013/deckex991pressrelease-3312.htm,Fourth Quarter Fiscal 2025 Financial Review,Operating income was $173.9 million compared to $144.3 million.
Deckers,revenue,FY25 (Apr 2024-Mar 2025),FY,4986,USD m,8-K Ex.99.1 2025-05-22,https://www.sec.gov/Archives/edgar/data/910521/000091052125000013/deckex991pressrelease-3312.htm,Full Fiscal Year 2025 Financial Review,"Net sales increased 16.3% to $4.986 billion compared to $4.288 billion. On a constant currency basis, net sales increased 16.5%."
Deckers,revenue,FY24 (Apr 2023-Mar 2024),FY,4288,USD m,8-K Ex.99.1 2025-05-22,https://www.sec.gov/Archives/edgar/data/910521/000091052125000013/deckex991pressrelease-3312.htm,Full Fiscal Year 2025 Financial Review,Net sales increased 16.3% to $4.986 billion compared to $4.288 billion.
Deckers,gross_margin,FY25,FY,57.9,%,8-K Ex.99.1 2025-05-22,https://www.sec.gov/Archives/edgar/data/910521/000091052125000013/deckex991pressrelease-3312.htm,Full Fiscal Year 2025 Financial Review,Gross margin was 57.9% compared to 55.6%.
Deckers,gross_margin,FY24,FY,55.6,%,8-K Ex.99.1 2025-05-22,https://www.sec.gov/Archives/edgar/data/910521/000091052125000013/deckex991pressrelease-3312.htm,Full Fiscal Year 2025 Financial Review,Gross margin was 57.9% compared to 55.6%.
Deckers,operating_margin (derived: 1179/4986; 927.5/4288=21.6),FY25,FY,23.6,%,8-K Ex.99.1 2025-05-22,https://www.sec.gov/Archives/edgar/data/910521/000091052125000013/deckex991pressrelease-3312.htm,Full Fiscal Year 2025 Financial Review,Operating income was $1.179 billion compared to $927.5 million.
Deckers,hoka_revenue,FY25,FY,2233,USD m,8-K Ex.99.1 2025-05-22,https://www.sec.gov/Archives/edgar/data/910521/000091052125000013/deckex991pressrelease-3312.htm,Full Fiscal Year 2025 Financial Review,HOKA® brand net sales increased 23.6% to $2.233 billion compared to $1.807 billion.
Deckers,revenue,Q3 FY25 (Oct-Dec 2024),2024Q4,1827,USD m,8-K Ex.99.1 2025-01-30,https://www.sec.gov/Archives/edgar/data/910521/000091052125000002/deckex991pressrelease-1231.htm,Third Quarter Fiscal 2025 Financial Review,"Net sales increased 17.1% to $1.827 billion compared to $1.560 billion. On a constant currency basis, net sales increased 16.6%."
Deckers,hoka_growth,Q3 FY25,2024Q4,23.7,%,8-K Ex.99.1 2025-01-30,https://www.sec.gov/Archives/edgar/data/910521/000091052125000002/deckex991pressrelease-1231.htm,Third Quarter Fiscal 2025 Brand Summary,HOKA® brand net sales increased 23.7% to $530.9 million compared to $429.3 million.
Deckers,gross_margin,Q3 FY25,2024Q4,60.3,%,8-K Ex.99.1 2025-01-30,https://www.sec.gov/Archives/edgar/data/910521/000091052125000002/deckex991pressrelease-1231.htm,Third Quarter Fiscal 2025 Financial Review,Gross margin was 60.3% compared to 58.7%.
Deckers,revenue,Q2 FY25 (Jul-Sep 2024),2024Q3,1311,USD m,8-K Ex.99.1 2024-10-24,https://www.sec.gov/Archives/edgar/data/910521/000091052124000056/deckex991pressrelease-9302.htm,Second Quarter Fiscal 2025 Financial Review,"Net sales increased 20.1% to $1.311 billion compared to $1.092 billion. On a constant currency basis, net sales increased 20.4%."
Deckers,hoka_growth,Q2 FY25,2024Q3,34.7,%,8-K Ex.99.1 2024-10-24,https://www.sec.gov/Archives/edgar/data/910521/000091052124000056/deckex991pressrelease-9302.htm,Second Quarter Fiscal 2025 Brand Summary,HOKA® brand net sales increased 34.7% to $570.9 million compared to $424.0 million.
Deckers,gross_margin,Q2 FY25,2024Q3,55.9,%,8-K Ex.99.1 2024-10-24,https://www.sec.gov/Archives/edgar/data/910521/000091052124000056/deckex991pressrelease-9302.htm,Second Quarter Fiscal 2025 Financial Review,Gross margin was 55.9% compared to 53.4%.
On Holding,revenue,Q2 2026 (Apr-Jun),2026Q2,850.3,CHF m,6-K Ex.99.3 2026-08-11,https://www.sec.gov/Archives/edgar/data/1858985/000185898526000018/a26q2-ex993xpressrelease.htm,Key Financial and Operating Metrics,"net sales increased by 13.5% to CHF 850.3 million, or by 21.6% on a constant currency basis;"
On Holding,dtc_growth (cc 34.3),Q2 2026,2026Q2,26.0,%,6-K Ex.99.3 2026-08-11,https://www.sec.gov/Archives/edgar/data/1858985/000185898526000018/a26q2-ex993xpressrelease.htm,Key Financial and Operating Metrics,"sales channel increased by 26.0% to CHF 388.4 million, or by 34.3% on a constant currency basis;"
On Holding,wholesale_growth (cc 12.7),Q2 2026,2026Q2,4.8,%,6-K Ex.99.3 2026-08-11,https://www.sec.gov/Archives/edgar/data/1858985/000185898526000018/a26q2-ex993xpressrelease.htm,Key Financial and Operating Metrics,"net sales through the wholesale sales channel increased by 4.8% to CHF 461.9 million, or by 12.7% on a constant currency basis;"
On Holding,apac_growth (cc 54.7),Q2 2026,2026Q2,43.1,%,6-K Ex.99.3 2026-08-11,https://www.sec.gov/Archives/edgar/data/1858985/000185898526000018/a26q2-ex993xpressrelease.htm,Key Financial and Operating Metrics,"Americas and Asia-Pacific increased by 15.4% to CHF 228.2 million, 4.5% to CHF 451.6 million and 43.1% to CHF 170.5 million"
On Holding,shoes_growth (cc 18.9),Q2 2026,2026Q2,10.9,%,6-K Ex.99.3 2026-08-11,https://www.sec.gov/Archives/edgar/data/1858985/000185898526000018/a26q2-ex993xpressrelease.htm,Key Financial and Operating Metrics,"net sales from shoes, apparel and accessories increased by 10.9% to CHF 781.6 million"
On Holding,gross_margin,Q2 2026,2026Q2,65.4,%,6-K Ex.99.3 2026-08-11,https://www.sec.gov/Archives/edgar/data/1858985/000185898526000018/a26q2-ex993xpressrelease.htm,Key Financial and Operating Metrics,gross profit margin increased to 65.4% from 61.5%;
On Holding,operating_margin (derived: 119.4/850.3),Q2 2026,2026Q2,14.0,%,6-K Ex.99.3 2026-08-11,https://www.sec.gov/Archives/edgar/data/1858985/000185898526000018/a26q2-ex993xpressrelease.htm,Income statement,Operating result 119.4 92.8 236.9 169.8
On Holding,inventory_growth (derived: 472.9/360.4-1),Jun 30 2026,2026Q2,31.2,%,6-K Ex.99.3 2026-08-11 and 2025-08-12,https://www.sec.gov/Archives/edgar/data/1858985/000185898526000018/a26q2-ex993xpressrelease.htm,Balance sheet,Inventories 472.9 419.8
On Holding,guidance_FY26_revenue,FY2026,guidance,low-20% cc growth; CHF 3.47-3.56bn,%,6-K Ex.99.3 2026-08-11,https://www.sec.gov/Archives/edgar/data/1858985/000185898526000018/a26q2-ex993xpressrelease.htm,Outlook,Expected to grow in the low-20% range on a constant currency basis
On Holding,guidance_2026_2029,2026-2029,guidance,high-teens cc net sales CAGR,%,6-K Ex.99.1 2026-09-22,https://www.sec.gov/Archives/edgar/data/1858985/000185898526000021/exhibit991oninvestorday202.htm,Investor Day 2026,On introduces the ambition to achieve a high-teens constant currency net sales CAGR through 2029
On Holding,revenue,Q1 2026 (Jan-Mar),2026Q1,831.9,CHF m,6-K Ex.99.1 2026-05-12,https://www.sec.gov/Archives/edgar/data/1858985/000185898526000014/a26q1-ex991xpressrelease.htm,Highlights,"Net sales increase by 14.5% year-over-year, or by 26.4% on a constant currency basis, reaching CHF 831.9 million."
On Holding,apac_growth (cc 61.4),Q1 2026,2026Q1,44.4,%,6-K Ex.99.1 2026-05-12,https://www.sec.gov/Archives/edgar/data/1858985/000185898526000014/a26q1-ex991xpressrelease.htm,Highlights,"The Asia-Pacific region grows 44.4%, or 61.4% on a constant currency basis"
On Holding,gross_margin,Q1 2026,2026Q1,64.2,%,6-K Ex.99.1 2026-05-12,https://www.sec.gov/Archives/edgar/data/1858985/000185898526000014/a26q1-ex991xpressrelease.htm,Key metrics,gross profit margin increased to 64.2% from 59.9%;
On Holding,operating_margin (derived: 117.4/831.9),Q1 2026,2026Q1,14.1,%,6-K Ex.99.1 2026-05-12,https://www.sec.gov/Archives/edgar/data/1858985/000185898526000014/a26q1-ex991xpressrelease.htm,Income statement,Operating result 117.4 77.0
On Holding,revenue,Q4 2025 (Oct-Dec),2025Q4,743.8,CHF m,6-K Ex.99.1 2026-03-03,https://www.sec.gov/Archives/edgar/data/1858985/000185898526000010/ex991pressreleasedatedmarc.htm,Key financial metrics Q4,"net sales increased by 22.6% to CHF 743.8 million, or by 30.6% on a constant currency basis;"
On Holding,gross_margin,Q4 2025,2025Q4,63.9,%,6-K Ex.99.1 2026-03-03,https://www.sec.gov/Archives/edgar/data/1858985/000185898526000010/ex991pressreleasedatedmarc.htm,Key financial metrics Q4,gross profit margin increased to 63.9% from 62.1%;
On Holding,revenue,FY2025,FY,3014.0,CHF m,6-K Ex.99.1 2026-03-03,https://www.sec.gov/Archives/edgar/data/1858985/000185898526000010/ex991pressreleasedatedmarc.htm,Key financial metrics FY,"net sales increased by 30.0% to CHF 3,014.0 million, or by 35.6% on a constant currency basis;"
On Holding,apac_growth,FY2025,FY,96.4,%,6-K Ex.99.1 2026-03-03,https://www.sec.gov/Archives/edgar/data/1858985/000185898526000010/ex991pressreleasedatedmarc.htm,Key financial metrics FY,"17.6% to CHF 1,740.1 million and 96.4% to CHF 511.1 million, respectively"
On Holding,gross_margin,FY2025,FY,62.8,%,6-K Ex.99.1 2026-03-03,https://www.sec.gov/Archives/edgar/data/1858985/000185898526000010/ex991pressreleasedatedmarc.htm,Key financial metrics FY,gross profit margin increased to 62.8% from 60.6%;
On Holding,operating_margin (derived: 377.0/3014.0; FY24 211.6/2318.3=9.1),FY2025,FY,12.5,%,6-K Ex.99.1 2026-03-03,https://www.sec.gov/Archives/edgar/data/1858985/000185898526000010/ex991pressreleasedatedmarc.htm,Income statement,Operating result 377.0 211.6 78.2 % 82.5 53.1 55.4 %
On Holding,inventory_growth,Dec 31 2025,2025Q4,0.1,%,6-K Ex.99.1 2026-03-03,https://www.sec.gov/Archives/edgar/data/1858985/000185898526000010/ex991pressreleasedatedmarc.htm,Balance sheet,Inventories 419.8 419.2 0.1 %
On Holding,revenue,Q3 2025 (Jul-Sep),2025Q3,794.4,CHF m,6-K Ex.99.1 2025-11-12,https://www.sec.gov/Archives/edgar/data/1858985/000185898525000015/a25q3-ex991xpressrelease.htm,Key metrics,"net sales increased by 24.9% to CHF 794.4 million, or by 34.5% on a constant currency basis;"
On Holding,gross_margin,Q3 2025,2025Q3,65.7,%,6-K Ex.99.1 2025-11-12,https://www.sec.gov/Archives/edgar/data/1858985/000185898525000015/a25q3-ex991xpressrelease.htm,Key metrics,gross profit margin increased to 65.7% from 60.6%;
On Holding,revenue,Q2 2025 (Apr-Jun),2025Q2,749.2,CHF m,6-K Ex.99.3 2025-08-12,https://www.sec.gov/Archives/edgar/data/1858985/000185898525000012/a25q2-ex993xpressrelease.htm,Key metrics,"net sales increased by 32.0% to CHF 749.2 million, or by 38.2% on a constant currency basis;"
On Holding,gross_margin,Q2 2025,2025Q2,61.5,%,6-K Ex.99.3 2025-08-12,https://www.sec.gov/Archives/edgar/data/1858985/000185898525000012/a25q2-ex993xpressrelease.htm,Key metrics,gross profit margin increased to 61.5% from 59.9%;
On Holding,revenue,Q1 2025 (Jan-Mar),2025Q1,726.6,CHF m,6-K Ex.99.1 2025-05-13,https://www.sec.gov/Archives/edgar/data/1858985/000185898525000008/a25q1-ex991xpressrelease.htm,Key metrics,"net sales increased by 43.0% to CHF 726.6 million, or by 40.0% on a constant currency basis;"
On Holding,revenue,Q4 2024 (Oct-Dec),2024Q4,606.6,CHF m,6-K Ex.99.1 2025-03-04,https://www.sec.gov/Archives/edgar/data/1858985/000185898525000005/ex991pressreleasedatedmarc.htm,Key highlights Q4,"net sales increased by 35.7% to CHF 606.6 million, or by 40.6% on a constant currency basis;"
On Holding,revenue,FY2024,FY,2318.3,CHF m,6-K Ex.99.1 2025-03-04,https://www.sec.gov/Archives/edgar/data/1858985/000185898525000005/ex991pressreleasedatedmarc.htm,Key highlights FY,"net sales increased by 29.4% to CHF 2,318.3 million, or by 33.2% on a constant currency basis;"
On Holding,revenue,FY2023,FY,1792.1,CHF m,6-K Ex.99.1 2025-03-04,https://www.sec.gov/Archives/edgar/data/1858985/000185898525000005/ex991pressreleasedatedmarc.htm,Income statement,"Net sales 2,318.3 1,792.1 29.4 %"
On Holding,gross_margin,FY2024,FY,60.6,%,6-K Ex.99.1 2025-03-04,https://www.sec.gov/Archives/edgar/data/1858985/000185898525000005/ex991pressreleasedatedmarc.htm,Key highlights FY,gross profit margin increased to 60.6% from 59.6%;
On Holding,revenue,Q3 2024 (Jul-Sep),2024Q3,635.8,CHF m,6-K Ex.99.1 2024-11-12,https://www.sec.gov/Archives/edgar/data/1858985/000185898524000029/a24q3-ex991xpressrelease.htm,Key metrics,"net sales increased by 32.3% to CHF 635.8 million, or by 33.2% on a constant currency basis;"
Lululemon,revenue,Q2 FY26 (May 4-Aug 2 2026),2026Q2,2415.6,USD m,8-K Ex.99.1 2026-09-03,https://www.sec.gov/Archives/edgar/data/1397187/000139718726000126/lulu-20260802xex991.htm,p.1 summary bullets (Second quarter),"Net revenue decreased 4% to $2.4 billion, or decreased 5% on a constant dollar basis."
Lululemon,revenue_growth_reported,Q2 FY26,2026Q2,-4,%,8-K Ex.99.1 2026-09-03,https://www.sec.gov/Archives/edgar/data/1397187/000139718726000126/lulu-20260802xex991.htm,p.1 summary bullets (Second quarter),"Net revenue decreased 4% to $2.4 billion, or decreased 5% on a constant dollar basis."
Lululemon,revenue_growth_cc,Q2 FY26,2026Q2,-5,%,8-K Ex.99.1 2026-09-03,https://www.sec.gov/Archives/edgar/data/1397187/000139718726000126/lulu-20260802xex991.htm,p.1 summary bullets (Second quarter),"Net revenue decreased 4% to $2.4 billion, or decreased 5% on a constant dollar basis."
Lululemon,americas_growth,Q2 FY26,2026Q2,-8,%,8-K Ex.99.1 2026-09-03,https://www.sec.gov/Archives/edgar/data/1397187/000139718726000126/lulu-20260802xex991.htm,p.1 summary bullets (Second quarter),Americas net revenue decreased 8%.
Lululemon,china_mainland_growth (reported; cc -2),Q2 FY26,2026Q2,4,%,8-K Ex.99.1 2026-09-03,https://www.sec.gov/Archives/edgar/data/1397187/000139718726000126/lulu-20260802xex991.htm,Net revenue change table,China Mainland 4 (6) (2)
Lululemon,gross_margin (incl. 560bp tariff refund),Q2 FY26,2026Q2,60.5,%,8-K Ex.99.1 2026-09-03,https://www.sec.gov/Archives/edgar/data/1397187/000139718726000126/lulu-20260802xex991.htm,p.1 summary bullets (Second quarter),This includes $134.5 million of tariff refunds(1) which increased gross margin by 560 basis points.
Lululemon,operating_margin (incl. 560bp tariff refund),Q2 FY26,2026Q2,18.8,%,8-K Ex.99.1 2026-09-03,https://www.sec.gov/Archives/edgar/data/1397187/000139718726000126/lulu-20260802xex991.htm,p.1 summary bullets (Second quarter),Income from operations decreased 13% to $453.7 million and operating margin decreased 190 basis points to 18.8%.
Lululemon,inventory_growth,Aug 2 2026,2026Q2,-1,%,8-K Ex.99.1 2026-09-03,https://www.sec.gov/Archives/edgar/data/1397187/000139718726000126/lulu-20260802xex991.htm,Balance Sheet Highlights,Inventories at the end of the second quarter of 2026 decreased by 1% to $1.7 billion
Lululemon,guidance_FY26_revenue,FY26 (to Jan 31 2027),guidance,10350-10500 (-5% to -7%),USD m,8-K Ex.99.1 2026-09-03,https://www.sec.gov/Archives/edgar/data/1397187/000139718726000126/lulu-20260802xex991.htm,2026 Outlook,"now expects net revenue to be in the range of $10.350 billion to $10.500 billion, representing a decline of 5% to 7%."
Lululemon,guidance_Q3_FY26_revenue,Q3 FY26,guidance,2290-2320 (-10% to -11%),USD m,8-K Ex.99.1 2026-09-03,https://www.sec.gov/Archives/edgar/data/1397187/000139718726000126/lulu-20260802xex991.htm,2026 Outlook,"the Company expects net revenue to be in the range of $2.290 billion to $2.320 billion, representing a decline of 10% to 11%."
Lululemon,revenue,Q1 FY26 (Feb-Apr 2026),2026Q1,2471.6,USD m,8-K Ex.99.1 2026-06-04,https://www.sec.gov/Archives/edgar/data/1397187/000139718726000077/lulu-20260503xex991.htm,p.1 summary bullets (First quarter),"Net revenue increased 4% to $2.5 billion, or increased 2% on a constant dollar basis."
Lululemon,americas_growth,Q1 FY26,2026Q1,-3,%,8-K Ex.99.1 2026-06-04,https://www.sec.gov/Archives/edgar/data/1397187/000139718726000077/lulu-20260503xex991.htm,p.1 summary bullets (First quarter),"Americas net revenue decreased 3%, or 4% on a constant dollar basis."
Lululemon,china_mainland_growth (reported; cc 23),Q1 FY26,2026Q1,30,%,8-K Ex.99.1 2026-06-04,https://www.sec.gov/Archives/edgar/data/1397187/000139718726000077/lulu-20260503xex991.htm,Net revenue change table,China Mainland 30 (7) 23
Lululemon,gross_margin,Q1 FY26,2026Q1,54.2,%,8-K Ex.99.1 2026-06-04,https://www.sec.gov/Archives/edgar/data/1397187/000139718726000077/lulu-20260503xex991.htm,p.1 summary bullets (First quarter),Gross profit decreased 3% to $1.3 billion and gross margin decreased 410 basis points to 54.2%.
Lululemon,operating_margin,Q1 FY26,2026Q1,11.2,%,8-K Ex.99.1 2026-06-04,https://www.sec.gov/Archives/edgar/data/1397187/000139718726000077/lulu-20260503xex991.htm,p.1 summary bullets (First quarter),Income from operations decreased 37% to $276.9 million and operating margin decreased 730 basis points to 11.2%.
Lululemon,inventory_growth,May 3 2026,2026Q1,2,%,8-K Ex.99.1 2026-06-04,https://www.sec.gov/Archives/edgar/data/1397187/000139718726000077/lulu-20260503xex991.htm,Balance Sheet Highlights,Inventories at the end of the first quarter of 2026 increased by 2% to $1.7 billion
Lululemon,revenue,Q4 FY25 (Nov 2025-Jan 2026),2025Q4,3640.8,USD m,8-K Ex.99.1 2026-03-17,https://www.sec.gov/Archives/edgar/data/1397187/000139718726000019/lulu-20260201xex991.htm,p.1 summary bullets (Fourth quarter),"Net revenue increased 1% to $3.6 billion, or was flat on a constant dollar basis."
Lululemon,revenue_growth_ex53rd_week,Q4 FY25,2025Q4,6,%,8-K Ex.99.1 2026-03-17,https://www.sec.gov/Archives/edgar/data/1397187/000139718726000019/lulu-20260201xex991.htm,p.1 summary bullets (Fourth quarter),"Excluding net revenue from the 53rd week of 2024, net revenue increased 6%, or 4% on a constant dollar basis."
Lululemon,china_mainland_growth (reported; cc 21),Q4 FY25,2025Q4,24,%,8-K Ex.99.1 2026-03-17,https://www.sec.gov/Archives/edgar/data/1397187/000139718726000019/lulu-20260201xex991.htm,Net revenue change table,China Mainland 24 (3) 21 29 (1) 28
Lululemon,gross_margin,Q4 FY25,2025Q4,54.9,%,8-K Ex.99.1 2026-03-17,https://www.sec.gov/Archives/edgar/data/1397187/000139718726000019/lulu-20260201xex991.htm,p.1 summary bullets (Fourth quarter),Gross profit decreased 8% to $2.0 billion and gross margin decreased 550 basis points to 54.9%.
Lululemon,operating_margin,Q4 FY25,2025Q4,22.3,%,8-K Ex.99.1 2026-03-17,https://www.sec.gov/Archives/edgar/data/1397187/000139718726000019/lulu-20260201xex991.htm,p.1 summary bullets (Fourth quarter),Income from operations decreased 22% to $812.3 million and operating margin decreased 660 basis points to 22.3%.
Lululemon,revenue,FY25 (Feb 2025-Jan 2026),FY,11102.6,USD m,8-K Ex.99.1 2026-03-17,https://www.sec.gov/Archives/edgar/data/1397187/000139718726000019/lulu-20260201xex991.htm,p.1 summary bullets (full year),Net revenue increased 5% to $11.1 billion.
Lululemon,china_mainland_growth (reported),FY25,FY,29,%,8-K Ex.99.1 2026-03-17,https://www.sec.gov/Archives/edgar/data/1397187/000139718726000019/lulu-20260201xex991.htm,Net revenue change table,China Mainland 24 (3) 21 29 (1) 28
Lululemon,gross_margin,FY25,FY,56.6,%,8-K Ex.99.1 2026-03-17,https://www.sec.gov/Archives/edgar/data/1397187/000139718726000019/lulu-20260201xex991.htm,p.1 summary bullets (full year),Gross profit was flat at $6.3 billion and gross margin decreased 260 basis points to 56.6%.
Lululemon,operating_margin,FY25,FY,19.9,%,8-K Ex.99.1 2026-03-17,https://www.sec.gov/Archives/edgar/data/1397187/000139718726000019/lulu-20260201xex991.htm,p.1 summary bullets (full year),operating margin decreased 380 basis points to 19.9%.
Lululemon,inventory_growth,Feb 1 2026,2025Q4,18,%,8-K Ex.99.1 2026-03-17,https://www.sec.gov/Archives/edgar/data/1397187/000139718726000019/lulu-20260201xex991.htm,Balance Sheet Highlights,"Inventories at the end of 2025 increased by 18% to $1.7 billion. On a unit basis, inventories increased 6%."
Lululemon,revenue,Q3 FY25 (Aug-Oct 2025),2025Q3,2565.9,USD m,8-K Ex.99.1 2025-12-11,https://www.sec.gov/Archives/edgar/data/1397187/000139718725000054/lulu-20251102xex991.htm,p.1 summary bullets (Third quarter),Net revenue increased 7% to $2.6 billion.
Lululemon,china_mainland_growth (reported),Q3 FY25,2025Q3,46,%,8-K Ex.99.1 2025-12-11,https://www.sec.gov/Archives/edgar/data/1397187/000139718725000054/lulu-20251102xex991.htm,Net revenue change table,China Mainland 46 1 47
Lululemon,gross_margin,Q3 FY25,2025Q3,55.6,%,8-K Ex.99.1 2025-12-11,https://www.sec.gov/Archives/edgar/data/1397187/000139718725000054/lulu-20251102xex991.htm,p.1 summary bullets (Third quarter),gross margin decreased 290 basis points to 55.6%.
Lululemon,operating_margin,Q3 FY25,2025Q3,17.0,%,8-K Ex.99.1 2025-12-11,https://www.sec.gov/Archives/edgar/data/1397187/000139718725000054/lulu-20251102xex991.htm,p.1 summary bullets (Third quarter),operating margin decreased 350 basis points to 17.0%.
Lululemon,revenue,Q2 FY25 (May-Jul 2025),2025Q2,2525.2,USD m,8-K Ex.99.1 2025-09-04,https://www.sec.gov/Archives/edgar/data/1397187/000139718725000038/lulu-20250803xex991.htm,p.1 summary bullets (Second quarter),"Net revenue increased 7% to $2.5 billion, or increased 6% on a constant dollar basis."
Lululemon,china_mainland_growth (reported),Q2 FY25,2025Q2,25,%,8-K Ex.99.1 2025-09-04,https://www.sec.gov/Archives/edgar/data/1397187/000139718725000038/lulu-20250803xex991.htm,Net revenue change table,China Mainland 25 (1) 24
Lululemon,gross_margin,Q2 FY25,2025Q2,58.5,%,8-K Ex.99.1 2025-09-04,https://www.sec.gov/Archives/edgar/data/1397187/000139718725000038/lulu-20250803xex991.htm,p.1 summary bullets (Second quarter),gross margin decreased 110 basis points to 58.5%.
Lululemon,operating_margin,Q2 FY25,2025Q2,20.7,%,8-K Ex.99.1 2025-09-04,https://www.sec.gov/Archives/edgar/data/1397187/000139718725000038/lulu-20250803xex991.htm,p.1 summary bullets (Second quarter),operating margin decreased 210 basis points to 20.7%.
Lululemon,inventory_growth,Aug 3 2025,2025Q2,21,%,8-K Ex.99.1 2025-09-04,https://www.sec.gov/Archives/edgar/data/1397187/000139718725000038/lulu-20250803xex991.htm,Balance Sheet Highlights,Inventories at the end of the second quarter of 2025 increased 21% to $1.7 billion
Lululemon,revenue,Q1 FY25 (Feb-Apr 2025),2025Q1,2370.7,USD m,8-K Ex.99.1 2025-06-05,https://www.sec.gov/Archives/edgar/data/1397187/000139718725000026/lulu-20250504xex991.htm,p.1 summary bullets (First quarter),"Net revenue increased 7% to $2.4 billion, or increased 8% on a constant dollar basis."
Lululemon,china_mainland_growth (reported),Q1 FY25,2025Q1,21,%,8-K Ex.99.1 2025-06-05,https://www.sec.gov/Archives/edgar/data/1397187/000139718725000026/lulu-20250504xex991.htm,Net revenue change table,China Mainland 21 1 22
Lululemon,gross_margin,Q1 FY25,2025Q1,58.3,%,8-K Ex.99.1 2025-06-05,https://www.sec.gov/Archives/edgar/data/1397187/000139718725000026/lulu-20250504xex991.htm,p.1 summary bullets (First quarter),gross margin increased 60 basis points to 58.3%.
Lululemon,operating_margin,Q1 FY25,2025Q1,18.5,%,8-K Ex.99.1 2025-06-05,https://www.sec.gov/Archives/edgar/data/1397187/000139718725000026/lulu-20250504xex991.htm,p.1 summary bullets (First quarter),operating margin decreased 110 basis points to 18.5%.
Lululemon,revenue,"Q4 FY24 (Nov 2024-Feb 2 2025, 14 weeks)",2024Q4,3611.5,USD m,8-K Ex.99.1 2025-03-27,https://www.sec.gov/Archives/edgar/data/1397187/000139718725000012/lulu-20250202xex991.htm,p.1 summary bullets (Fourth quarter),"Net revenue increased 13% to $3.6 billion, or 14% on a constant dollar basis."
Lululemon,revenue,FY24 (53 weeks),FY,10588.1,USD m,8-K Ex.99.1 2025-03-27,https://www.sec.gov/Archives/edgar/data/1397187/000139718725000012/lulu-20250202xex991.htm,p.1 summary bullets (full year),"Net revenue increased 10% to $10.6 billion, or increased 11% on a constant dollar basis."
Lululemon,revenue,FY23,FY,9619.3,USD m,8-K Ex.99.1 2025-03-27,https://www.sec.gov/Archives/edgar/data/1397187/000139718725000012/lulu-20250202xex991.htm,Statements of Operations,"Net revenue $ 3,611,497 $ 3,205,103 $ 10,588,126 $ 9,619,278"
Lululemon,gross_margin,FY24,FY,59.2,%,8-K Ex.99.1 2025-03-27,https://www.sec.gov/Archives/edgar/data/1397187/000139718725000012/lulu-20250202xex991.htm,p.1 summary bullets (full year),Gross margin increased 90 basis points to 59.2%.
Lululemon,operating_margin,FY24,FY,23.7,%,8-K Ex.99.1 2025-03-27,https://www.sec.gov/Archives/edgar/data/1397187/000139718725000012/lulu-20250202xex991.htm,p.1 summary bullets (full year),Operating margin increased 150 basis points to 23.7%.
Lululemon,china_mainland_growth (reported),FY24,FY,41,%,8-K Ex.99.1 2025-03-27,https://www.sec.gov/Archives/edgar/data/1397187/000139718725000012/lulu-20250202xex991.htm,Net revenue change table,China Mainland 46 2 48 41 2 43
Lululemon,revenue,Q3 FY24 (Aug-Oct 2024),2024Q3,2396.7,USD m,8-K Ex.99.1 2024-12-05,https://www.sec.gov/Archives/edgar/data/1397187/000139718724000040/lulu-20241027xex991.htm,p.1 summary bullets (Third quarter),"Net revenue increased 9% to $2.4 billion, or increased 8% on a constant dollar basis."
Under Armour,revenue,Q1 FY27 (Apr-Jun 2026),2026Q2,1097.9,USD m,8-K Ex.99.1 2026-08-07,https://www.sec.gov/Archives/edgar/data/1336917/000133691726000108/exhibit991-fiscal2027q1.htm,First Quarter Fiscal 2027 Review,Revenue decreased 3 percent to $1.1 billion (down 4 percent constant currency).
Under Armour,apac_growth,Q1 FY27,2026Q2,-7,%,8-K Ex.99.1 2026-08-07,https://www.sec.gov/Archives/edgar/data/1336917/000133691726000108/exhibit991-fiscal2027q1.htm,First Quarter Fiscal 2027 Review,Asia-Pacific decreased 7 percent (down 10 percent constant currency)
Under Armour,north_america_growth,Q1 FY27,2026Q2,-9,%,8-K Ex.99.1 2026-08-07,https://www.sec.gov/Archives/edgar/data/1336917/000133691726000108/exhibit991-fiscal2027q1.htm,First Quarter Fiscal 2027 Review,North America revenue declined 9 percent to $610 million
Under Armour,wholesale_dtc_growth,Q1 FY27,2026Q2,wholesale -2; DTC -6,%,8-K Ex.99.1 2026-08-07,https://www.sec.gov/Archives/edgar/data/1336917/000133691726000108/exhibit991-fiscal2027q1.htm,First Quarter Fiscal 2027 Review,Wholesale revenue decreased 2 percent to $638 million and direct-to-consumer (DTC) revenue decreased 6 percent to $437 million.
Under Armour,footwear_growth,Q1 FY27,2026Q2,-8,%,8-K Ex.99.1 2026-08-07,https://www.sec.gov/Archives/edgar/data/1336917/000133691726000108/exhibit991-fiscal2027q1.htm,First Quarter Fiscal 2027 Review,footwear revenue declined 8 percent to $245 million
Under Armour,gross_margin (incl. IEEPA refund),Q1 FY27,2026Q2,54.1,%,8-K Ex.99.1 2026-08-07,https://www.sec.gov/Archives/edgar/data/1336917/000133691726000108/exhibit991-fiscal2027q1.htm,First Quarter Fiscal 2027 Review,"Gross margin increased 590 basis points to 54.1 percent, primarily due to refunds received"
Under Armour,operating_margin,Q1 FY27,2026Q2,4.3,%,8-K Ex.99.1 2026-08-07,https://www.sec.gov/Archives/edgar/data/1336917/000133691726000108/exhibit991-fiscal2027q1.htm,Statements of Operations,"Income (loss) from operations 46,739 4.3 % 3,323 0.3 %"
Under Armour,inventory_growth,Jun 30 2026,2026Q2,-3,%,8-K Ex.99.1 2026-08-07,https://www.sec.gov/Archives/edgar/data/1336917/000133691726000108/exhibit991-fiscal2027q1.htm,First Quarter Fiscal 2027 Review,Inventory decreased 3 percent to $1.1 billion.
Under Armour,guidance_FY27_revenue,FY27 (Apr 2026-Mar 2027),guidance,mid-single-digit decline,%,8-K Ex.99.1 2026-08-07,https://www.sec.gov/Archives/edgar/data/1336917/000133691726000108/exhibit991-fiscal2027q1.htm,Updated Fiscal 2027 Outlook,Revenue is now expected to decline at a mid-single-digit percentage rate compared with the prior outlook of a slight decline.
Under Armour,revenue,Q4 FY26 (Jan-Mar 2026),2026Q1,1171.2,USD m,8-K Ex.99.1 2026-05-12,https://www.sec.gov/Archives/edgar/data/1336917/000133691726000059/exhibit991-fiscal2026q4.htm,Fourth Quarter Fiscal 2026 Review,Revenue decreased 1 percent to $1.2 billion (down 4 percent constant currency).
Under Armour,apac_growth,Q4 FY26,2026Q1,13,%,8-K Ex.99.1 2026-05-12,https://www.sec.gov/Archives/edgar/data/1336917/000133691726000059/exhibit991-fiscal2026q4.htm,Fourth Quarter Fiscal 2026 Review,Asia-Pacific increased 13 percent (up 8 percent constant currency)
Under Armour,footwear_growth,Q4 FY26,2026Q1,0,%,8-K Ex.99.1 2026-05-12,https://www.sec.gov/Archives/edgar/data/1336917/000133691726000059/exhibit991-fiscal2026q4.htm,Fourth Quarter Fiscal 2026 Review,footwear was flat at $282 million
Under Armour,gross_margin,Q4 FY26,2026Q1,42.0,%,8-K Ex.99.1 2026-05-12,https://www.sec.gov/Archives/edgar/data/1336917/000133691726000059/exhibit991-fiscal2026q4.htm,Fourth Quarter Fiscal 2026 Review,"Gross margin declined 470 basis points to 42.0 percent, primarily due to higher tariffs"
Under Armour,operating_margin (derived: -34/1171),Q4 FY26,2026Q1,-2.9,%,8-K Ex.99.1 2026-05-12,https://www.sec.gov/Archives/edgar/data/1336917/000133691726000059/exhibit991-fiscal2026q4.htm,Fourth Quarter Fiscal 2026 Review,Operating loss was $34 million.
Under Armour,revenue,FY26 (Apr 2025-Mar 2026),FY,4966.4,USD m,8-K Ex.99.1 2026-05-12,https://www.sec.gov/Archives/edgar/data/1336917/000133691726000059/exhibit991-fiscal2026q4.htm,Full Year Fiscal 2026 Review,Revenue decreased 4 percent to $5.0 billion (down 5 percent constant currency).
Under Armour,revenue,FY25,FY,5164.3,USD m,8-K Ex.99.1 2026-05-12,https://www.sec.gov/Archives/edgar/data/1336917/000133691726000059/exhibit991-fiscal2026q4.htm,Statements of Operations,"Net revenues $ 1,171,161 100.0 % $ 1,180,583 100.0 % $ 4,966,370 100.0 % $ 5,164,310"
Under Armour,revenue,FY24,FY,5701.9,USD m,8-K Ex.99.1 2025-05-13,https://www.sec.gov/Archives/edgar/data/1336917/000133691725000058/exhibit991-fiscal2025q4.htm,Statements of Operations,"$ 5,164,310 100.0 % $ 5,701,879 100.0 %"
Under Armour,footwear_growth,FY26,FY,-11,%,8-K Ex.99.1 2026-05-12,https://www.sec.gov/Archives/edgar/data/1336917/000133691726000059/exhibit991-fiscal2026q4.htm,Full Year Fiscal 2026 Review,footwear revenue declined 11 percent to $1.1 billion
Under Armour,apac_growth,FY26,FY,-5,%,8-K Ex.99.1 2026-05-12,https://www.sec.gov/Archives/edgar/data/1336917/000133691726000059/exhibit991-fiscal2026q4.htm,Full Year Fiscal 2026 Review,declined by 5 percent in Asia-Pacific (down 6 percent constant currency)
Under Armour,gross_margin,FY26,FY,45.5,%,8-K Ex.99.1 2026-05-12,https://www.sec.gov/Archives/edgar/data/1336917/000133691726000059/exhibit991-fiscal2026q4.htm,Full Year Fiscal 2026 Review,"Gross margin decreased 240 basis points to 45.5 percent, primarily due to higher tariffs"
Under Armour,operating_margin (derived: -163/4966; adj. 107 = 2.2%),FY26,FY,-3.3,%,8-K Ex.99.1 2026-05-12,https://www.sec.gov/Archives/edgar/data/1336917/000133691726000059/exhibit991-fiscal2026q4.htm,Full Year Fiscal 2026 Review,Operating loss was $163 million.
Under Armour,gross_margin,FY25,FY,47.9,%,8-K Ex.99.1 2025-05-13,https://www.sec.gov/Archives/edgar/data/1336917/000133691725000058/exhibit991-fiscal2025q4.htm,Full Year Fiscal 2025 Review,Gross margin increased 180 basis points to 47.9 percent
Under Armour,operating_margin (derived: -185/5164; adj. 198 = 3.8%),FY25,FY,-3.6,%,8-K Ex.99.1 2025-05-13,https://www.sec.gov/Archives/edgar/data/1336917/000133691725000058/exhibit991-fiscal2025q4.htm,Full Year Fiscal 2025 Review,Operating loss was $185 million.
Under Armour,footwear_growth,FY25,FY,-13,%,8-K Ex.99.1 2025-05-13,https://www.sec.gov/Archives/edgar/data/1336917/000133691725000058/exhibit991-fiscal2025q4.htm,Full Year Fiscal 2025 Review,footwear revenue declined 13 percent to $1.2 billion
Under Armour,revenue,Q3 FY26 (Oct-Dec 2025),2025Q4,1327.8,USD m,8-K Ex.99.1 2026-02-06,https://www.sec.gov/Archives/edgar/data/1336917/000133691726000025/exhibit991-fiscal2026q3.htm,Third Quarter Fiscal 2026 Review,Revenue decreased 5 percent to $1.33 billion (down 6 percent on a currency-neutral basis).
Under Armour,footwear_growth,Q3 FY26,2025Q4,-12,%,8-K Ex.99.1 2026-02-06,https://www.sec.gov/Archives/edgar/data/1336917/000133691726000025/exhibit991-fiscal2026q3.htm,Third Quarter Fiscal 2026 Review,footwear declined 12 percent to $265 million
Under Armour,gross_margin,Q3 FY26,2025Q4,44.4,%,8-K Ex.99.1 2026-02-06,https://www.sec.gov/Archives/edgar/data/1336917/000133691726000025/exhibit991-fiscal2026q3.htm,Third Quarter Fiscal 2026 Review,"Gross margin declined 310 basis points to 44.4 percent, primarily due to higher tariffs."
Under Armour,revenue,Q2 FY26 (Jul-Sep 2025),2025Q3,1333.4,USD m,8-K Ex.99.1 2025-11-06,https://www.sec.gov/Archives/edgar/data/1336917/000133691725000193/exhibit991-fiscal2026q2.htm,Second Quarter Fiscal 2026 Review,Revenue decreased 5 percent to $1.3 billion (down 6 percent currency neutral).
Under Armour,footwear_growth,Q2 FY26,2025Q3,-16,%,8-K Ex.99.1 2025-11-06,https://www.sec.gov/Archives/edgar/data/1336917/000133691725000193/exhibit991-fiscal2026q2.htm,Second Quarter Fiscal 2026 Review,footwear revenue declined 16 percent to $264 million
Under Armour,gross_margin,Q2 FY26,2025Q3,47.3,%,8-K Ex.99.1 2025-11-06,https://www.sec.gov/Archives/edgar/data/1336917/000133691725000193/exhibit991-fiscal2026q2.htm,Second Quarter Fiscal 2026 Review,Gross margin declined by 250 basis points to 47.3 percent
Under Armour,revenue,Q1 FY26 (Apr-Jun 2025),2025Q2,1134.1,USD m,8-K Ex.99.1 2025-08-08,https://www.sec.gov/Archives/edgar/data/1336917/000133691725000134/exhibit991-fiscal2026q1.htm,First Quarter Fiscal 2026 Review,Revenue declined 4 percent to $1.1 billion (down 4 percent currency neutral).
Under Armour,gross_margin,Q1 FY26,2025Q2,48.2,%,8-K Ex.99.1 2025-08-08,https://www.sec.gov/Archives/edgar/data/1336917/000133691725000134/exhibit991-fiscal2026q1.htm,First Quarter Fiscal 2026 Review,Gross margin increased 70 basis points to 48.2 percent
Under Armour,revenue,Q4 FY25 (Jan-Mar 2025),2025Q1,1180.6,USD m,8-K Ex.99.1 2025-05-13,https://www.sec.gov/Archives/edgar/data/1336917/000133691725000058/exhibit991-fiscal2025q4.htm,Fourth Quarter Fiscal 2025 Review,Revenue was down 11 percent to $1.2 billion (down 10 percent currency neutral).
Under Armour,gross_margin,Q4 FY25,2025Q1,46.7,%,8-K Ex.99.1 2025-05-13,https://www.sec.gov/Archives/edgar/data/1336917/000133691725000058/exhibit991-fiscal2025q4.htm,Fourth Quarter Fiscal 2025 Review,Gross margin increased 170 basis points to 46.7 percent
Under Armour,revenue,Q3 FY25 (Oct-Dec 2024),2024Q4,1401.0,USD m,8-K Ex.99.1 2025-02-06,https://www.sec.gov/Archives/edgar/data/1336917/000133691725000013/exhibit991-fiscal2025q3.htm,Third Quarter Fiscal 2025 Review,Revenue was down 6 percent to $1.4 billion (down 6 percent currency neutral).
Under Armour,gross_margin,Q3 FY25,2024Q4,47.5,%,8-K Ex.99.1 2025-02-06,https://www.sec.gov/Archives/edgar/data/1336917/000133691725000013/exhibit991-fiscal2025q3.htm,Third Quarter Fiscal 2025 Review,Gross margin increased 240 basis points to 47.5 percent
Under Armour,revenue,Q2 FY25 (Jul-Sep 2024),2024Q3,1399.0,USD m,8-K Ex.99.1 2024-11-07,https://www.sec.gov/Archives/edgar/data/1336917/000133691724000164/exhibit991-fiscal2025q2.htm,Second Quarter Fiscal 2025 Review,revenue was down 11 percent to $1.4 billion (down 10 percent currency neutral).
Under Armour,gross_margin,Q2 FY25,2024Q3,49.8,%,8-K Ex.99.1 2024-11-07,https://www.sec.gov/Archives/edgar/data/1336917/000133691724000164/exhibit991-fiscal2025q2.htm,Second Quarter Fiscal 2025 Review,Gross margin increased 200 basis points to 49.8 percent
Skechers,status_taken_private,Sep 12 2025,n/a,merger completed; delisted,n/a,8-K 2025-09-12,https://www.sec.gov/Archives/edgar/data/1065837/000119312525201846/d41926d8k.htm,Item 3.01,that the Merger had been completed and requested that NYSE file with the SEC
Skechers,revenue,Q2 2025 (Apr-Jun),2025Q2,2440.0,USD m,8-K Ex.99.1 2025-08-08,https://www.sec.gov/Archives/edgar/data/1065837/000095017025105856/skx-ex99_1.htm,Highlights,"Second quarter sales of $2.44 billion, a year-over-year increase of 13.1%"
Skechers,revenue_growth_cc,Q2 2025,2025Q2,11.5,%,8-K Ex.99.1 2025-08-08,https://www.sec.gov/Archives/edgar/data/1065837/000095017025105856/skx-ex99_1.htm,Highlights,"sales of $2.41 billion on a constant currency basis, a year-over-year increase of 11.5%"
Skechers,wholesale_dtc_growth,Q2 2025,2025Q2,wholesale 15.0; DTC 11.0,%,8-K Ex.99.1 2025-08-08,https://www.sec.gov/Archives/edgar/data/1065837/000095017025105856/skx-ex99_1.htm,Highlights,Wholesale sales grew 15.0%
Skechers,china_growth,Q2 2025,2025Q2,-8.2,%,8-K Ex.99.1 2025-08-08,https://www.sec.gov/Archives/edgar/data/1065837/000095017025105856/skx-ex99_1.htm,Supplemental regional table,China sales $ 287.2 $ 312.7 (25.6 ) (8.2 )
Skechers,gross_margin,Q2 2025,2025Q2,53.3,%,8-K Ex.99.1 2025-08-08,https://www.sec.gov/Archives/edgar/data/1065837/000095017025105856/skx-ex99_1.htm,Summary table,Gross margin 53.3 % 54.9 % (160) bps
Skechers,operating_margin,Q2 2025,2025Q2,7.1,%,8-K Ex.99.1 2025-08-08,https://www.sec.gov/Archives/edgar/data/1065837/000095017025105856/skx-ex99_1.htm,Summary table,Operating margin 7.1 % 9.6 % (250) bps
Skechers,inventory_growth (derived: 1871.8/1514.5-1),Jun 30 2025,2025Q2,23.6,%,8-K Ex.99.1 2025-08-08 and 2024-07-25,https://www.sec.gov/Archives/edgar/data/1065837/000095017025105856/skx-ex99_1.htm,Balance sheet,"Inventory 1,871,805 1,919,386"
Skechers,guidance,FY2025,guidance,withdrawn,n/a,8-K Ex.99.1 2025-04-24,https://www.sec.gov/Archives/edgar/data/1065837/000095017025058057/skx-ex99_1.htm,Outlook,the Company is not providing financial guidance at this time and is withdrawing the annual 2025 guidance
Skechers,revenue,Q1 2025 (Jan-Mar),2025Q1,2411.6,USD m,8-K Ex.99.1 2025-04-24,https://www.sec.gov/Archives/edgar/data/1065837/000095017025058057/skx-ex99_1.htm,Highlights,"Record sales of $2.41 billion, a year-over-year increase of 7.1%; sales of $2.46 billion on a constant currency basis, a year-over-year increase of 9.0%"
Skechers,china_growth,Q1 2025,2025Q1,-15.9,%,8-K Ex.99.1 2025-04-24,https://www.sec.gov/Archives/edgar/data/1065837/000095017025058057/skx-ex99_1.htm,Supplemental regional table,China sales $ 268.7 $ 319.5 (50.8 ) (15.9 )
Skechers,gross_margin,Q1 2025,2025Q1,52.0,%,8-K Ex.99.1 2025-04-24,https://www.sec.gov/Archives/edgar/data/1065837/000095017025058057/skx-ex99_1.htm,Summary table,Gross margin 52.0 % 52.5 % (50) bps
Skechers,operating_margin,Q1 2025,2025Q1,11.0,%,8-K Ex.99.1 2025-04-24,https://www.sec.gov/Archives/edgar/data/1065837/000095017025058057/skx-ex99_1.htm,Summary table,Operating margin 11.0 % 13.3 % (230) bps
Skechers,revenue,Q4 2024 (Oct-Dec),2024Q4,2212.4,USD m,8-K Ex.99.1 2025-02-06,https://www.sec.gov/Archives/edgar/data/1065837/000095017025015399/skx-ex99_1.htm,Highlights,"Sales of $2.21 billion, a year-over-year increase of 12.8%"
Skechers,china_growth,Q4 2024,2024Q4,-11.5,%,8-K Ex.99.1 2025-02-06,https://www.sec.gov/Archives/edgar/data/1065837/000095017025015399/skx-ex99_1.htm,Supplemental regional table,China sales $ 333.5 $ 376.7 (43.2 ) (11.5 )
Skechers,gross_margin,Q4 2024,2024Q4,53.3,%,8-K Ex.99.1 2025-02-06,https://www.sec.gov/Archives/edgar/data/1065837/000095017025015399/skx-ex99_1.htm,Summary table,Gross margin 53.3 % 53.1 % 20 bps
Skechers,revenue,FY2024,FY,8969.4,USD m,8-K Ex.99.1 2025-02-06,https://www.sec.gov/Archives/edgar/data/1065837/000095017025015399/skx-ex99_1.htm,Highlights,"Sales of $8.97 billion, a year-over-year increase of 12.1%; sales of $9.04 billion on a constant currency basis"
Skechers,revenue,FY2023,FY,8000.3,USD m,8-K Ex.99.1 2025-02-06,https://www.sec.gov/Archives/edgar/data/1065837/000095017025015399/skx-ex99_1.htm,Summary table,"Sales $ 8,969.4 $ 8,000.3 969.1 12.1"
Skechers,gross_margin,FY2024,FY,53.2,%,8-K Ex.99.1 2025-02-06,https://www.sec.gov/Archives/edgar/data/1065837/000095017025015399/skx-ex99_1.htm,Summary table,Gross margin 53.2 % 51.9 % 120 bps
Skechers,operating_margin,FY2024,FY,10.1,%,8-K Ex.99.1 2025-02-06,https://www.sec.gov/Archives/edgar/data/1065837/000095017025015399/skx-ex99_1.htm,Summary table,Operating margin 10.1 % 9.8 % 30 bps
Skechers,china_growth,FY2024,FY,-0.9,%,8-K Ex.99.1 2025-02-06,https://www.sec.gov/Archives/edgar/data/1065837/000095017025015399/skx-ex99_1.htm,Supplemental regional table,"China sales $ 1,218.2 $ 1,228.6 (10.4 ) (0.9 )"
Skechers,inventory_growth,Dec 31 2024,2024Q4,25.8,%,8-K Ex.99.1 2025-02-06,https://www.sec.gov/Archives/edgar/data/1065837/000095017025015399/skx-ex99_1.htm,Balance Sheet,"Inventory was $1.92 billion, an increase of $394.0 million or 25.8% from December 31, 2023"
Skechers,revenue,Q3 2024 (Jul-Sep),2024Q3,2347.7,USD m,8-K Ex.99.1 2024-10-24,https://www.sec.gov/Archives/edgar/data/1065837/000095017024117064/skx-ex99_1.htm,Highlights,"Record quarterly sales of $2.35 billion, a 15.9% increase"
Skechers,china_growth,Q3 2024,2024Q3,-5.7,%,8-K Ex.99.1 2024-10-24,https://www.sec.gov/Archives/edgar/data/1065837/000095017024117064/skx-ex99_1.htm,Supplemental regional table,China sales $ 252.4 $ 267.6 (15.2 ) (5.7 )
Skechers,gross_margin,Q3 2024,2024Q3,52.1,%,8-K Ex.99.1 2024-10-24,https://www.sec.gov/Archives/edgar/data/1065837/000095017024117064/skx-ex99_1.htm,Summary table,Gross margin 52.1 % 52.9 % (80) bps
VF Corp,revenue,Q1 FY27 (Apr-Jun 2026),2026Q2,1669.4,USD m,8-K Ex.99.2 2026-07-29,https://www.sec.gov/Archives/edgar/data/103379/000010337926000113/q12027earningspressrelease.htm,Reconciliation table,"Revenues $ 1,669,379 $ - $ 1,669,379"
VF Corp,"revenue_growth_reported (ex Dickies +1%, flat C$)",Q1 FY27,2026Q2,-5,%,8-K Ex.99.2 2026-07-29,https://www.sec.gov/Archives/edgar/data/103379/000010337926000113/q12027earningspressrelease.htm,VF Q1 27 results ahead of guidance,"Revenue ex Dickies® +1% vs. LY or flat C$, ahead of guidance of down low-single digits C$ vs. LY"
VF Corp,vans_growth,Q1 FY27,2026Q2,-8,%,8-K Ex.99.2 2026-07-29,https://www.sec.gov/Archives/edgar/data/103379/000010337926000113/q12027earningspressrelease.htm,VF Q1 27 results ahead of guidance,"Vans® (8%) vs. LY or (9%) C$, with continued growth in Americas DTC, more than offset by Wholesale declines"
VF Corp,dtc_growth (ex Dickies),Q1 FY27,2026Q2,2,%,8-K Ex.99.2 2026-07-29,https://www.sec.gov/Archives/edgar/data/103379/000010337926000113/q12027earningspressrelease.htm,VF Q1 27 results ahead of guidance,"Continued positive performance in global DTC, +2% vs. LY or +5% C$ ex Dickies®"
VF Corp,gross_margin,Q1 FY27,2026Q2,54.9,%,8-K Ex.99.2 2026-07-29,https://www.sec.gov/Archives/edgar/data/103379/000010337926000113/q12027earningspressrelease.htm,VF Q1 27 results ahead of guidance,"Gross margin (GM) of 54.9%, up 100 bps vs. LY"
VF Corp,operating_margin,Q1 FY27,2026Q2,-5.0,%,8-K Ex.99.2 2026-07-29,https://www.sec.gov/Archives/edgar/data/103379/000010337926000113/q12027earningspressrelease.htm,VF Q1 27 results ahead of guidance,"Operating income (loss) of ($83M) and operating margin (OM) of (5.0%), down 10 bps vs. LY"
VF Corp,guidance_FY27_revenue,"FY27 (to Mar 2027, 53 weeks)",guidance,+2% or better C$ (ex Dickies),%,8-K Ex.99.2 2026-07-29,https://www.sec.gov/Archives/edgar/data/103379/000010337926000113/q12027earningspressrelease.htm,Raising FY 27 revenue guidance,"Revenue +2% or better C$ vs. LY1, and vs. prior guidance of +1% to +2% C$"
VF Corp,revenue,Q4 FY26 (Jan-Mar 2026),2026Q1,2166.0,USD m,8-K Ex.99.2 2026-05-20,https://www.sec.gov/Archives/edgar/data/103379/000010337926000028/q42026earningspressrelease.htm,Reconciliation table,"Revenues $ 2,166,034"
VF Corp,"revenue_growth_reported (ex Dickies +8%, +3% C$)",Q4 FY26,2026Q1,1,%,8-K Ex.99.2 2026-05-20,https://www.sec.gov/Archives/edgar/data/103379/000010337926000028/q42026earningspressrelease.htm,Q4 26 revenue growth,"Revenue ex Dickies® +8% vs. LY or +3% C$, ahead of guidance of flat to +2% C$ vs. LY"
VF Corp,vans_growth,Q4 FY26,2026Q1,-1,%,8-K Ex.99.2 2026-05-20,https://www.sec.gov/Archives/edgar/data/103379/000010337926000028/q42026earningspressrelease.htm,Q4 26 revenue growth,"Vans® (1%) vs. LY or (5%) C$, with a return to growth in Americas DTC"
VF Corp,revenue,FY26 (Apr 2025-Mar 2026),FY,9605.2,USD m,8-K Ex.99.2 2026-05-20,https://www.sec.gov/Archives/edgar/data/103379/000010337926000028/q42026earningspressrelease.htm,Reconciliation table,"Revenues $ 9,605,207"
VF Corp,revenue,FY25,FY,9504.7,USD m,8-K Ex.99.2 2026-05-20,https://www.sec.gov/Archives/edgar/data/103379/000010337926000028/q42026earningspressrelease.htm,Reconciliation table,"Revenues $ 9,504,691"
VF Corp,revenue,FY24 (continuing ops),FY,9915.7,USD m,Q4 FY25 earnings presentation Ex.99.1 2025-05-21,https://www.sec.gov/Archives/edgar/data/103379/000010337925000021/q425earningsex991.htm,Financial Summary,"Revenue $ 2,143.8 $ 2,247.3 (5%) (3%) $ 9,504.7 $ 9,915.7 (4%) (4%)"
VF Corp,gross_margin,FY26,FY,54.8,%,8-K Ex.99.2 2026-05-20,https://www.sec.gov/Archives/edgar/data/103379/000010337926000028/q42026earningspressrelease.htm,FY 26 highlights,"FY'26 gross margin (GM) of 54.8%, up 130 bps vs. LY"
VF Corp,operating_margin,FY26,FY,6.0,%,8-K Ex.99.2 2026-05-20,https://www.sec.gov/Archives/edgar/data/103379/000010337926000028/q42026earningspressrelease.htm,FY 26 highlights,"FY'26 operating income (OI) of $577M and operating margin (OM) of 6.0%, up 280 bps vs. LY"
VF Corp,revenue,Q3 FY26 (Oct-Dec 2025),2025Q4,2875.8,USD m,8-K Ex.99.2 2026-01-28,https://www.sec.gov/Archives/edgar/data/103379/000010337926000008/q32026earningspressrelease.htm,Reconciliation table,"Revenues $ 2,875,801"
VF Corp,vans_growth,Q3 FY26,2025Q4,-8,%,8-K Ex.99.2 2026-01-28,https://www.sec.gov/Archives/edgar/data/103379/000010337926000008/q32026earningspressrelease.htm,Highlights,"Product newness and digital performance drove holiday period at Vans®, (8%) vs. LY or (10%) C$"
VF Corp,revenue,Q2 FY26 (Jul-Sep 2025),2025Q3,2802.7,USD m,8-K Ex.99.2 2025-10-28,https://www.sec.gov/Archives/edgar/data/103379/000010337925000058/q22026earningspressrelease.htm,Highlights,"Revenue of $2.8B, +2% vs. LY or (1%) C$"
VF Corp,gross_margin,Q2 FY26,2025Q3,52.2,%,8-K Ex.99.2 2025-10-28,https://www.sec.gov/Archives/edgar/data/103379/000010337925000058/q22026earningspressrelease.htm,Highlights,"Gross margin of 52.2%, flat vs. LY"
VF Corp,operating_margin,Q2 FY26,2025Q3,11.2,%,8-K Ex.99.2 2025-10-28,https://www.sec.gov/Archives/edgar/data/103379/000010337925000058/q22026earningspressrelease.htm,Highlights,"Operating margin of 11.2%, +130bps vs. LY"
VF Corp,vans_growth,Q2 FY26,2025Q3,-9,%,8-K Ex.99.2 2025-10-28,https://www.sec.gov/Archives/edgar/data/103379/000010337925000058/q22026earningspressrelease.htm,Highlights,Vans® revenue sequentially improved to (9%) vs. LY or (11%) C$
VF Corp,revenue,Q1 FY26 (Apr-Jun 2025),2025Q2,1760.7,USD m,8-K Ex.99.2 2025-07-30,https://www.sec.gov/Archives/edgar/data/103379/000010337925000033/q12026earningspressrelease.htm,Highlights,"Revenue of $1.8B, flat vs. LY or (2%) C$"
VF Corp,vans_growth,Q1 FY26,2025Q2,-14,%,8-K Ex.99.2 2025-07-30,https://www.sec.gov/Archives/edgar/data/103379/000010337925000033/q12026earningspressrelease.htm,Highlights,"Vans® was (14%) vs. LY or (15%) C$, impacted by channel rationalization actions"
VF Corp,revenue,Q4 FY25 (Jan-Mar 2025),2025Q1,2143.8,USD m,Q4 FY25 earnings presentation Ex.99.1 2025-05-21,https://www.sec.gov/Archives/edgar/data/103379/000010337925000021/q425earningsex991.htm,Financial Summary,"Revenue of $2.1 billion, (5%) vs. LY and (3%) C$ vs. LY"
VF Corp,revenue,Q3 FY25 (Oct-Dec 2024),2024Q4,2833.9,USD m,8-K Ex.99.2 2026-01-28,https://www.sec.gov/Archives/edgar/data/103379/000010337926000008/q32026earningspressrelease.htm,Prior-year reconciliation table,"Revenues $ 2,833,912"
VF Corp,revenue,Q2 FY25 (Jul-Sep 2024),2024Q3,2757.9,USD m,8-K Ex.99 2024-10-28,https://www.sec.gov/Archives/edgar/data/103379/000010337924000028/vfcq22025exhibit99.htm,Highlights,"Revenue $2.8 billion, down 6% vs. last year, an improvement vs. Q1'FY25 down 10%"
VF Corp,gross_margin,Q2 FY25,2024Q3,52.2,%,8-K Ex.99 2024-10-28,https://www.sec.gov/Archives/edgar/data/103379/000010337924000028/vfcq22025exhibit99.htm,Highlights,"Gross margin 52.2%, up 120 basis points vs. last year"
Amer Sports,revenue_growth_prelim_guidance,Q3 2026 (Jul-Sep),2026Q3,20-22,%,6-K 2026-09-16 preliminary release,https://www.sec.gov/Archives/edgar/data/1988894/000198889426000086/investordaypre-release.htm,Updated outlook for third quarter 2026,Amer Sports now expects third quarter 2026 year-over-year revenue growth of 20 - 22% versus the previous guidance range of 18 - 20%
Amer Sports,guidance_long_term,"2026 base, 5+ years",guidance,low-double digits to mid-teens CAGR,%,6-K 2026-09-16 preliminary release,https://www.sec.gov/Archives/edgar/data/1988894/000198889426000086/investordaypre-release.htm,Updated long-term financial algorithm,Annual revenue CAGR: low-double digits to mid-teens
Amer Sports,revenue,Q2 2026 (Apr-Jun),2026Q2,1633,USD m,6-K Ex.99.1 2026-08-18,https://www.sec.gov/Archives/edgar/data/1988894/000198889426000083/pressreleaseq22026.htm,Second quarter 2026 results,"Revenue increased 32% to $1,633 million, or 30% on a constant currency basis1."
Amer Sports,greater_china_growth,Q2 2026,2026Q2,35.5,%,6-K Ex.99.1 2026-08-18,https://www.sec.gov/Archives/edgar/data/1988894/000198889426000083/pressreleaseq22026.htm,Revenue by region table,Greater China (1) $ 556.0 $ 410.2 35.5 %
Amer Sports,gross_margin (incl. 390bp tariff refund),Q2 2026,2026Q2,65.6,%,6-K Ex.99.1 2026-08-18,https://www.sec.gov/Archives/edgar/data/1988894/000198889426000083/pressreleaseq22026.htm,Second quarter 2026 results,"Gross margin increased 710 basis points to 65.6%, including a benefit of 390 basis points from net tariff refunds"
Amer Sports,operating_margin (incl. 390bp tariff refund),Q2 2026,2026Q2,11.7,%,6-K Ex.99.1 2026-08-18,https://www.sec.gov/Archives/edgar/data/1988894/000198889426000083/pressreleaseq22026.htm,Second quarter 2026 results,"Operating margin increased 820 basis points to 11.7%, including a benefit of 390 basis points from net tariff refunds."
Amer Sports,inventory_growth,Jun 30 2026,2026Q2,19,%,6-K Ex.99.1 2026-08-18,https://www.sec.gov/Archives/edgar/data/1988894/000198889426000083/pressreleaseq22026.htm,Balance sheet,"Year-over-year inventories increased 19% to $1,897 million."
Amer Sports,guidance_FY26_revenue,FY2026,guidance,approximately +24% reported,%,6-K Ex.99.1 2026-08-18,https://www.sec.gov/Archives/edgar/data/1988894/000198889426000083/pressreleaseq22026.htm,Full-year 2026 outlook,"Reported revenue growth: approximately 24%, which assumes a 200 - 250 basis point currency benefit at current exchange rates"
Amer Sports,revenue,Q1 2026 (Jan-Mar),2026Q1,1945,USD m,6-K Ex.99.1 2026-05-19,https://www.sec.gov/Archives/edgar/data/1988894/000198889426000073/pressreleaseq12026.htm,Highlights,"Revenue increased 32% to $1,945 million, or +26% ex-currency"
Amer Sports,greater_china_growth,Q1 2026,2026Q1,44.5,%,6-K Ex.99.1 2026-05-19,https://www.sec.gov/Archives/edgar/data/1988894/000198889426000073/pressreleaseq12026.htm,Revenue by region table,Greater China (1) $ 644.5 $ 446.0 44.5 %
Amer Sports,gross_margin,Q1 2026,2026Q1,59.9,%,6-K Ex.99.1 2026-05-19,https://www.sec.gov/Archives/edgar/data/1988894/000198889426000073/pressreleaseq12026.htm,Highlights,Gross margin increased 210 basis points to 59.9%
Amer Sports,operating_margin,Q1 2026,2026Q1,16.5,%,6-K Ex.99.1 2026-05-19,https://www.sec.gov/Archives/edgar/data/1988894/000198889426000073/pressreleaseq12026.htm,Highlights,Operating margin increased 200 basis points to 16.5%.
Amer Sports,revenue,Q4 2025 (Oct-Dec),2025Q4,2101.1,USD m,6-K Ex.99.1 2026-02-24,https://www.sec.gov/Archives/edgar/data/1988894/000198889426000002/pressreleaseq425.htm,Fourth quarter 2025 results,"Revenue increased 28% to $2,101 million, or 26% on a constant currency basis1."
Amer Sports,greater_china_growth,Q4 2025,2025Q4,41.8,%,6-K Ex.99.1 2026-02-24,https://www.sec.gov/Archives/edgar/data/1988894/000198889426000002/pressreleaseq425.htm,Revenue by region table,"Greater China (1) 544.2 383.9 41.8 % 1,861.9 1,298.1 43.4 %"
Amer Sports,gross_margin,Q4 2025,2025Q4,57.7,%,6-K Ex.99.1 2026-02-24,https://www.sec.gov/Archives/edgar/data/1988894/000198889426000002/pressreleaseq425.htm,Fourth quarter 2025 results,Gross margin increased 160 basis points to 57.7%
Amer Sports,operating_margin,Q4 2025,2025Q4,10.9,%,6-K Ex.99.1 2026-02-24,https://www.sec.gov/Archives/edgar/data/1988894/000198889426000002/pressreleaseq425.htm,Fourth quarter 2025 results,Operating margin decreased 90 basis points to 10.9%.
Amer Sports,inventory_growth,Dec 31 2025,2025Q4,33,%,6-K Ex.99.1 2026-02-24,https://www.sec.gov/Archives/edgar/data/1988894/000198889426000002/pressreleaseq425.htm,Balance sheet,"Year-over-year inventories increased 33% to $1,622 million."
Amer Sports,revenue,FY2025,FY,6566.2,USD m,6-K Ex.99.1 2026-02-24,https://www.sec.gov/Archives/edgar/data/1988894/000198889426000002/pressreleaseq425.htm,Fiscal year 2025 results,"Revenue increased 27% to $6,566 million, or 26% on a constant currency basis."
Amer Sports,greater_china_growth,FY2025,FY,43.4,%,6-K Ex.99.1 2026-02-24,https://www.sec.gov/Archives/edgar/data/1988894/000198889426000002/pressreleaseq425.htm,Revenue by region table,"Greater China (1) 544.2 383.9 41.8 % 1,861.9 1,298.1 43.4 %"
Amer Sports,gross_margin,FY2025,FY,57.6,%,6-K Ex.99.1 2026-02-24,https://www.sec.gov/Archives/edgar/data/1988894/000198889426000002/pressreleaseq425.htm,Fiscal year 2025 results,Gross margin increased 220 basis points to 57.6%
Amer Sports,operating_margin,FY2025,FY,10.7,%,6-K Ex.99.1 2026-02-24,https://www.sec.gov/Archives/edgar/data/1988894/000198889426000002/pressreleaseq425.htm,Fiscal year 2025 results,Operating margin increased 160 basis points to 10.7%.
Amer Sports,revenue,FY2024,FY,5183.3,USD m,6-K Ex.99.1 2025-02-25,https://www.sec.gov/Archives/edgar/data/1988894/000162828025007522/pressreleaseq424.htm,Fiscal year 2024 results,"Revenue increased 18% to $5,183 million, or 19% on a constant currency basis."
Amer Sports,revenue,FY2023,FY,4400.4,USD m,6-K Ex.99.1 2025-02-25,https://www.sec.gov/Archives/edgar/data/1988894/000162828025007522/pressreleaseq424.htm,Income statement,"Revenue $ 1,635.5 $ 1,327.5 $ 5,183.3 $ 4,400.4"
Amer Sports,gross_margin,FY2024,FY,55.4,%,6-K Ex.99.1 2025-02-25,https://www.sec.gov/Archives/edgar/data/1988894/000162828025007522/pressreleaseq424.htm,Fiscal year 2024 results,Gross margin increased 290 basis points to 55.4%
Amer Sports,operating_margin,FY2024,FY,9.1,%,6-K Ex.99.1 2025-02-25,https://www.sec.gov/Archives/edgar/data/1988894/000162828025007522/pressreleaseq424.htm,Fiscal year 2024 results,Operating margin increased 220 basis points to 9.1%.
Amer Sports,revenue,Q3 2025 (Jul-Sep),2025Q3,1756,USD m,6-K Ex.99.1 2025-11-18,https://www.sec.gov/Archives/edgar/data/1988894/000198889425000019/pressreleaseq32025.htm,Highlights,"Revenue increased 30% to $1,756 million"
Amer Sports,greater_china_growth,Q3 2025,2025Q3,47,%,6-K Ex.99.1 2025-11-18,https://www.sec.gov/Archives/edgar/data/1988894/000198889425000019/pressreleaseq32025.htm,Revenue by region table,"Greater China (1) 461.5 312.9 47 % 1,317.7 914.2 44 %"
Amer Sports,gross_margin,Q3 2025,2025Q3,56.8,%,6-K Ex.99.1 2025-11-18,https://www.sec.gov/Archives/edgar/data/1988894/000198889425000019/pressreleaseq32025.htm,Highlights,Gross margin increased 160 basis points to 56.8%
Amer Sports,revenue,Q2 2025 (Apr-Jun),2025Q2,1236,USD m,6-K Ex.99.1 2025-08-19,https://www.sec.gov/Archives/edgar/data/1988894/000198889425000011/pressreleaseq22025.htm,Highlights,"Revenue increased 23% to $1,236 million"
Amer Sports,greater_china_growth,Q2 2025,2025Q2,42,%,6-K Ex.99.1 2025-08-19,https://www.sec.gov/Archives/edgar/data/1988894/000198889425000011/pressreleaseq22025.htm,Revenue by region table,Greater China (2) 410.2 289.6 42 % 856.2 601.2 42 %
Amer Sports,revenue,Q1 2025 (Jan-Mar),2025Q1,1473,USD m,6-K Ex.99.1 2025-05-20,https://www.sec.gov/Archives/edgar/data/1988894/000162828025026672/pressreleaseq12025.htm,Highlights,"Revenue increased 23% to $1,473 million in 1Q25"
Amer Sports,greater_china_growth,Q1 2025,2025Q1,43,%,6-K Ex.99.1 2025-05-20,https://www.sec.gov/Archives/edgar/data/1988894/000162828025026672/pressreleaseq12025.htm,Revenue by region table,Greater China (2) 446.0 311.6 43 %
Amer Sports,revenue,Q4 2024 (Oct-Dec),2024Q4,1635.5,USD m,6-K Ex.99.1 2025-02-25,https://www.sec.gov/Archives/edgar/data/1988894/000162828025007522/pressreleaseq424.htm,Highlights,Revenue increased 23% to $1.6 billion
Amer Sports,revenue,Q3 2024 (Jul-Sep),2024Q3,1354,USD m,6-K Ex.99.1 2024-11-19,https://www.sec.gov/Archives/edgar/data/1988894/000162828024048330/pressrelease.htm,Highlights,"Revenue increased 17% to $1,354 million"
Birkenstock,revenue,Q3 FY26 (Apr-Jun 2026),2026Q2,719.5,EUR m,6-K Ex.99.1 2026-08-13,https://www.sec.gov/Archives/edgar/data/1977102/000119312526347762/birk-ex99_1.htm,Financial highlights Q3,"Revenue of EUR 720 million, an increase of 13% on a reported basis and 15% in constant currency"
Birkenstock,apac_growth (cc 23),Q3 FY26,2026Q2,18,%,6-K Ex.99.1 2026-08-13,https://www.sec.gov/Archives/edgar/data/1977102/000119312526347762/birk-ex99_1.htm,Financial highlights Q3,18% in APAC on a reported basis (23% in constant currency)
Birkenstock,dtc_b2b_growth,Q3 FY26,2026Q2,DTC 14; B2B 13,%,6-K Ex.99.1 2026-08-13,https://www.sec.gov/Archives/edgar/data/1977102/000119312526347762/birk-ex99_1.htm,Financial highlights Q3,"DTC revenue growth of 14%, 16% in constant currency"
Birkenstock,gross_margin,Q3 FY26,2026Q2,59.1,%,6-K Ex.99.1 2026-08-13,https://www.sec.gov/Archives/edgar/data/1977102/000119312526347762/birk-ex99_1.htm,Financial highlights Q3,"Gross profit margin of 59.1%, down 140 basis points from 60.5% in the prior-year period"
Birkenstock,guidance_FY26_revenue,FY26 (Oct 2025-Sep 2026),guidance,"+15% cc; high end of EUR 2,300-2,350m",%,6-K Ex.99.1 2026-08-13,https://www.sec.gov/Archives/edgar/data/1977102/000119312526347762/birk-ex99_1.htm,Updated Fiscal 2026 guidance,"Revenue growth of 15% in constant currency, resulting in reported revenue at the high end of EUR 2,300-2,350 million"
Birkenstock,revenue,Q2 FY26 (Jan-Mar 2026),2026Q1,618,EUR m,6-K Ex.99.1 2026-05-13,https://www.sec.gov/Archives/edgar/data/1977102/000119312526220435/birk-ex99_1.htm,Financial highlights,"Revenue of EUR 618 million, an increase of 8% on a reported basis and 14% in constant currency"
Birkenstock,gross_margin,Q2 FY26,2026Q1,53.9,%,6-K Ex.99.1 2026-05-13,https://www.sec.gov/Archives/edgar/data/1977102/000119312526220435/birk-ex99_1.htm,Financial highlights,"Gross profit margin of 53.9%, down 380 basis points from 57.7% in the prior-year"
Birkenstock,revenue,Q1 FY26 (Oct-Dec 2025),2025Q4,402,EUR m,6-K Ex.99.1 2026-02-12,https://www.sec.gov/Archives/edgar/data/1977102/000119312526047586/birk-ex99_1.htm,Financial highlights,"Revenue of EUR 402 million, an increase of 11.1% on a reported basis and 17.8% in constant currency"
Birkenstock,gross_margin,Q1 FY26,2025Q4,55.7,%,6-K Ex.99.1 2026-02-12,https://www.sec.gov/Archives/edgar/data/1977102/000119312526047586/birk-ex99_1.htm,Financial highlights,"Gross profit margin of 55.7%, down 460 basis points from 60.3% in the prior-year"
Birkenstock,revenue,FY25 (Oct 2024-Sep 2025),FY,2097.4,EUR m,6-K Ex.99.1 2025-12-18,https://www.sec.gov/Archives/edgar/data/1977102/000119312525323615/birk-ex99_1.htm,Financial highlights FY,"Revenue of EUR 2.1 billion, an increase of 16% on a reported basis and 18% in constant currency"
Birkenstock,revenue,FY24,FY,1804.7,EUR m,6-K Ex.99.1 2025-12-18,https://www.sec.gov/Archives/edgar/data/1977102/000119312525323615/birk-ex99_1.htm,Income statement,"Revenue 526,338 455,764 2,097,429 1,804,690"
Birkenstock,gross_margin,FY25,FY,59.1,%,6-K Ex.99.1 2025-12-18,https://www.sec.gov/Archives/edgar/data/1977102/000119312525323615/birk-ex99_1.htm,Financial highlights FY,"Gross profit margin of 59.1%, up 30 basis points from 58.8% in fiscal 2024"
Birkenstock,revenue,Q3 FY25 (Apr-Jun 2025),2025Q2,635.0,EUR m,6-K Ex.99.1 2025-08-14,https://www.sec.gov/Archives/edgar/data/1977102/000095017025108382/birk-ex99_1.htm,Financial highlights,"Revenue of EUR 635 million, an increase of 12% on a reported basis and 16% in constant currency"
Birkenstock,revenue,Q2 FY25 (Jan-Mar 2025),2025Q1,574,EUR m,6-K Ex.99.1 2025-05-15,https://www.sec.gov/Archives/edgar/data/1977102/000095017025071881/birk-ex99_1.htm,Financial highlights,"Revenue of EUR 574 million, an increase of 19% on a reported basis and 18% in constant currency"
adidas,revenue,Q2 2026 (Apr-Jun),2026Q2,6743,EUR m,IR results release 2026-07-30,https://res.cloudinary.com/confirmed-web/image/upload/v1785388904/adidas-group/investors/financial-publications/2026/Q2/EN/adidasAG_Q2_2026_Results_EN_Final_z7f9t2.pdf,Second-quarter results,"In euro terms, revenues grew 13% to € 6,743 million (2025: € 5,952 million)"
adidas,revenue_growth_cc,Q2 2026,2026Q2,14,%,IR results release 2026-07-30,https://res.cloudinary.com/confirmed-web/image/upload/v1785388904/adidas-group/investors/financial-publications/2026/Q2/EN/adidasAG_Q2_2026_Results_EN_Final_z7f9t2.pdf,Major developments Q2 2026,"Currency-neutral revenues up 14%, leading to record net sales of € 6.7 billion"
adidas,dtc_growth_cc,Q2 2026,2026Q2,25,%,IR results release 2026-07-30,https://res.cloudinary.com/confirmed-web/image/upload/v1785388904/adidas-group/investors/financial-publications/2026/Q2/EN/adidasAG_Q2_2026_Results_EN_Final_z7f9t2.pdf,Net sales development table,"Direct-to-Consumer (DTC) 2,909 2,338 24% 25%"
adidas,wholesale_growth_cc,Q2 2026,2026Q2,6,%,IR results release 2026-07-30,https://res.cloudinary.com/confirmed-web/image/upload/v1785388904/adidas-group/investors/financial-publications/2026/Q2/EN/adidasAG_Q2_2026_Results_EN_Final_z7f9t2.pdf,Net sales development table,"Wholesale 3,825 3,604 6% 6%"
adidas,greater_china_growth_cc,Q2 2026,2026Q2,15,%,IR results release 2026-07-30,https://res.cloudinary.com/confirmed-web/image/upload/v1785388904/adidas-group/investors/financial-publications/2026/Q2/EN/adidasAG_Q2_2026_Results_EN_Final_z7f9t2.pdf,Net sales development table,Greater China 953 798 19% 15%
adidas,footwear_growth_cc,Q2 2026,2026Q2,1,%,IR results release 2026-07-30,https://res.cloudinary.com/confirmed-web/image/upload/v1785388904/adidas-group/investors/financial-publications/2026/Q2/EN/adidasAG_Q2_2026_Results_EN_Final_z7f9t2.pdf,Net sales development table,"Footwear 3,492 3,476 0% 1%"
adidas,running_growth,Q2 2026,2026Q2,about 30,%,IR results release 2026-07-30,https://res.cloudinary.com/confirmed-web/image/upload/v1785388904/adidas-group/investors/financial-publications/2026/Q2/EN/adidasAG_Q2_2026_Results_EN_Final_z7f9t2.pdf,Second-quarter results,"Meanwhile, Running continued to grow around 30%"
adidas,gross_margin,Q2 2026,2026Q2,52.5,%,IR results release 2026-07-30,https://res.cloudinary.com/confirmed-web/image/upload/v1785388904/adidas-group/investors/financial-publications/2026/Q2/EN/adidasAG_Q2_2026_Results_EN_Final_z7f9t2.pdf,Major developments Q2 2026,Gross margin improves 0.8 percentage points to 52.5%
adidas,operating_margin (derived: 574/6743),Q2 2026,2026Q2,8.5,%,IR results release 2026-07-30,https://res.cloudinary.com/confirmed-web/image/upload/v1785388904/adidas-group/investors/financial-publications/2026/Q2/EN/adidasAG_Q2_2026_Results_EN_Final_z7f9t2.pdf,Major developments Q2 2026,Operating profit up 5% to € 574 million
adidas,inventory_growth,Jun 30 2026,2026Q2,13,%,IR results release 2026-07-30,https://res.cloudinary.com/confirmed-web/image/upload/v1785388904/adidas-group/investors/financial-publications/2026/Q2/EN/adidasAG_Q2_2026_Results_EN_Final_z7f9t2.pdf,Balance sheet,"Inventories increased 13% to € 5,969 million at June 30, 2026 (2025: € 5,261 million)"
adidas,guidance_FY26_revenue,FY2026,guidance,+9% to +10% cc,%,IR results release 2026-07-30,https://res.cloudinary.com/confirmed-web/image/upload/v1785388904/adidas-group/investors/financial-publications/2026/Q2/EN/adidasAG_Q2_2026_Results_EN_Final_z7f9t2.pdf,Increased top-line outlook for FY 2026,Revenues now expected to grow between 9% and 10%
adidas,revenue,Q1 2026 (Jan-Mar),2026Q1,6592,EUR m,IR results release Q1 2026,https://res.cloudinary.com/confirmed-web/image/upload/v1777440493/adidas-group/investors/financial-publications/2026/Q1/adidasAG_Q1_2026_Results_EN_Final_vkqpi2.pdf,Net sales table,"Total net sales 6,592 6,153 7% 14%"
adidas,greater_china_growth_cc,Q1 2026,2026Q1,17,%,IR results release Q1 2026,https://res.cloudinary.com/confirmed-web/image/upload/v1777440493/adidas-group/investors/financial-publications/2026/Q1/adidasAG_Q1_2026_Results_EN_Final_vkqpi2.pdf,Net sales table,"Greater China 1,135 1,029 10% 17%"
adidas,gross_margin,Q1 2026,2026Q1,51.1,%,IR results release Q1 2026,https://res.cloudinary.com/confirmed-web/image/upload/v1777440493/adidas-group/investors/financial-publications/2026/Q1/adidasAG_Q1_2026_Results_EN_Final_vkqpi2.pdf,Major developments,Healthy gross margin of 51.1%
adidas,operating_margin,Q1 2026,2026Q1,10.7,%,IR results release Q1 2026,https://res.cloudinary.com/confirmed-web/image/upload/v1777440493/adidas-group/investors/financial-publications/2026/Q1/adidasAG_Q1_2026_Results_EN_Final_vkqpi2.pdf,Operating profit,representing an operating margin of 10.7%
adidas,revenue,Q4 2025 (Oct-Dec),2025Q4,6076,EUR m,IR FY 2025 results release,https://res.cloudinary.com/confirmed-web/image/upload/v1772605768/adidas-group/investors/financial-publications/2025/Q4/adidasAG_FY_2025_Results_EN_Final_tb9z6m.pdf,Fourth-quarter results,"In euro terms, revenues reached a level of € 6,076 million"
adidas,revenue_growth_cc (incl. Yeezy base),Q4 2025,2025Q4,10,%,IR FY 2025 results release,https://res.cloudinary.com/confirmed-web/image/upload/v1772605768/adidas-group/investors/financial-publications/2025/Q4/adidasAG_FY_2025_Results_EN_Final_tb9z6m.pdf,Fourth-quarter results,"Including Yeezy sales in the prior year, currency- neutral revenues increased 10%."
adidas,greater_china_growth_cc,Q4 2025,2025Q4,15,%,IR FY 2025 results release,https://res.cloudinary.com/confirmed-web/image/upload/v1772605768/adidas-group/investors/financial-publications/2025/Q4/adidasAG_FY_2025_Results_EN_Final_tb9z6m.pdf,Q4 net sales table,Greater China 848 794 7% 15% 15%
adidas,gross_margin,Q4 2025,2025Q4,50.8,%,IR FY 2025 results release,https://res.cloudinary.com/confirmed-web/image/upload/v1772605768/adidas-group/investors/financial-publications/2025/Q4/adidasAG_FY_2025_Results_EN_Final_tb9z6m.pdf,Fourth-quarter results,The company’s gross margin increased 1.0 percentage points to 50.8% in the fourth quarter
adidas,revenue,FY2025,FY,24811,EUR m,IR FY 2025 results release,https://res.cloudinary.com/confirmed-web/image/upload/v1772605768/adidas-group/investors/financial-publications/2025/Q4/adidasAG_FY_2025_Results_EN_Final_tb9z6m.pdf,Net sales table,"Total net sales 24,811 23,683 5% 10% 13%"
adidas,greater_china_growth_cc,FY2025,FY,9,%,IR FY 2025 results release,https://res.cloudinary.com/confirmed-web/image/upload/v1772605768/adidas-group/investors/financial-publications/2025/Q4/adidasAG_FY_2025_Results_EN_Final_tb9z6m.pdf,Net sales table,"Greater China 3,623 3,459 5% 9% 13%"
adidas,gross_margin,FY2025,FY,51.6,%,IR FY 2025 results release,https://res.cloudinary.com/confirmed-web/image/upload/v1772605768/adidas-group/investors/financial-publications/2025/Q4/adidasAG_FY_2025_Results_EN_Final_tb9z6m.pdf,Highlights,Gross margin improves 0.8pp to 51.6%
adidas,operating_margin,FY2025,FY,8.3,%,IR FY 2025 results release,https://res.cloudinary.com/confirmed-web/image/upload/v1772605768/adidas-group/investors/financial-publications/2025/Q4/adidasAG_FY_2025_Results_EN_Final_tb9z6m.pdf,Highlights,"Operating profit up 54% to € 2,056 million, operating margin increases 2.6pp to 8.3%"
adidas,guidance_2026_2028,2026-2028,guidance,high-single-digit cc every year,%,IR FY 2025 results release,https://res.cloudinary.com/confirmed-web/image/upload/v1772605768/adidas-group/investors/financial-publications/2025/Q4/adidasAG_FY_2025_Results_EN_Final_tb9z6m.pdf,Highlights,Currency-neutral revenues to grow at high-single-digit rate every year 2026-2028
adidas,revenue,Q3 2025 (Jul-Sep),2025Q3,6630,EUR m,IR Q3 2025 results release,https://res.cloudinary.com/confirmed-web/image/upload/v1761718887/adidas-group/investors/financial-publications/2025/Q3/adidasAG_Q3_2025_Results_EN_Final_rylckc.pdf,Third-quarter results,"€ 6,630 million (2024: € 6,438 million) in the quarter"
adidas,operating_margin,Q3 2025,2025Q3,11.1,%,IR Q3 2025 results release,https://res.cloudinary.com/confirmed-web/image/upload/v1761718887/adidas-group/investors/financial-publications/2025/Q3/adidasAG_Q3_2025_Results_EN_Final_rylckc.pdf,Operating profit,Operating profit growing to € 736 million reflects operating margin of 11.1% in Q3
adidas,gross_margin,Q3 2025,2025Q3,51.8,%,IR Q3 2025 results release,https://res.cloudinary.com/confirmed-web/image/upload/v1761718887/adidas-group/investors/financial-publications/2025/Q3/adidasAG_Q3_2025_Results_EN_Final_rylckc.pdf,Highlights,Gross margin improves 0.5 percentage points to 51.8%
adidas,revenue_growth_cc (incl. Yeezy base),Q2 2025,2025Q2,8,%,IR Q2 2025 results release,https://res.cloudinary.com/confirmed-web/image/upload/v1753852841/adidas-group/investors/financial-publications/2025/Q2/adidasAG_Q2_2025_Results_EN_Final_pa2trd.pdf,Second-quarter results,"in the prior year, currency-neutral revenues increased 8%."
adidas,gross_margin,Q2 2025,2025Q2,51.7,%,IR Q2 2025 results release,https://res.cloudinary.com/confirmed-web/image/upload/v1753852841/adidas-group/investors/financial-publications/2025/Q2/adidasAG_Q2_2025_Results_EN_Final_pa2trd.pdf,Highlights,Gross margin improves 0.9 percentage points to 51.7%
adidas,revenue,Q1 2025 (Jan-Mar),2025Q1,6153,EUR m,IR Q1 2025 results release,https://res.cloudinary.com/confirmed-web/image/upload/v1745903646/adidas-group/investors/financial-publications/2025/Q1/adidasAG_Q1_2025_Results_EN_Final_mju03h.pdf,First-quarter results,"In euro terms, revenues grew 13%, or nearly € 700 million, to € 6,153 million"
adidas,revenue_growth_cc,Q1 2025,2025Q1,13,%,IR Q1 2025 results release,https://res.cloudinary.com/confirmed-web/image/upload/v1745903646/adidas-group/investors/financial-publications/2025/Q1/adidasAG_Q1_2025_Results_EN_Final_mju03h.pdf,First-quarter results,"In the first quarter of 2025, currency-neutral revenues increased 13% versus the prior year."
adidas,revenue,Q4 2024 (Oct-Dec),2024Q4,5965,EUR m,IR FY 2024 results release,https://res.cloudinary.com/confirmed-web/image/upload/v1741155965/adidas-group/investors/financial-publications/2024/Q4/adidasAG_FY_2024_Results_EN_vf_ptevlo.pdf,Fourth-quarter results,"euro terms, revenues grew 24% to € 5,965 million (2023: € 4,812 million)."
adidas,revenue_growth_cc,Q4 2024,2024Q4,19,%,IR FY 2024 results release,https://res.cloudinary.com/confirmed-web/image/upload/v1741155965/adidas-group/investors/financial-publications/2024/Q4/adidasAG_FY_2024_Results_EN_vf_ptevlo.pdf,Fourth-quarter results,Currency-neutral revenues increased 19% during the fourth quarter.
adidas,revenue,FY2024,FY,23683,EUR m,IR FY 2024 results release,https://res.cloudinary.com/confirmed-web/image/upload/v1741155965/adidas-group/investors/financial-publications/2024/Q4/adidasAG_FY_2024_Results_EN_vf_ptevlo.pdf,Full-year results,"revenues increased 11% to € 23,683 million in 2024 (2023: € 21,427 million)."
adidas,gross_margin,FY2024,FY,50.8,%,IR FY 2024 results release,https://res.cloudinary.com/confirmed-web/image/upload/v1741155965/adidas-group/investors/financial-publications/2024/Q4/adidasAG_FY_2024_Results_EN_vf_ptevlo.pdf,Full-year results,The company’s gross margin increased 3.3 percentage points to 50.8% in 2024 (2023: 47.5%).
adidas,operating_margin,FY2024,FY,5.6,%,IR FY 2024 results release,https://res.cloudinary.com/confirmed-web/image/upload/v1741155965/adidas-group/investors/financial-publications/2024/Q4/adidasAG_FY_2024_Results_EN_vf_ptevlo.pdf,Full-year results,The operating margin was 5.6% in 2024
adidas,revenue,Q3 2024 (Jul-Sep),2024Q3,6438,EUR m,IR Q3 2024 results release,https://res.cloudinary.com/confirmed-web/image/upload/v1730182962/adidas-group/investors/financial-publications/2024/Q3/adidasAG_Q3_2024_Results_EN_final_aqkvyz.pdf,Third-quarter results,"In euro terms, revenues grew 7% to € 6.438 billion (2023: € 5.999 billion)."
adidas,revenue_growth_cc,Q3 2024,2024Q3,10,%,IR Q3 2024 results release,https://res.cloudinary.com/confirmed-web/image/upload/v1730182962/adidas-group/investors/financial-publications/2024/Q3/adidasAG_Q3_2024_Results_EN_final_aqkvyz.pdf,Third-quarter results,Currency-neutral revenues increased 10% during the third quarter.
Puma,revenue,Q2 2026 (Apr-Jun),2026Q2,1690.6,EUR m,IR Q2 2026 release 2026-07-31,https://about.puma.com/sites/default/files/financial-report/2026/puma-q2-2026-release-eng-final.pdf,Key developments Q2 2026,"Sales down 9.4% currency adjusted (ca) to € 1,690.6 million"
Puma,wholesale_growth_ca,Q2 2026,2026Q2,-14.0,%,IR Q2 2026 release 2026-07-31,https://about.puma.com/sites/default/files/financial-report/2026/puma-q2-2026-release-eng-final.pdf,Sales by channel,"By distribution channel, Wholesale declined 14.0% (ca) to € 1,094.8 million in Q2 2026"
Puma,dtc_growth_ca,Q2 2026,2026Q2,0.4,%,IR Q2 2026 release 2026-07-31,https://about.puma.com/sites/default/files/financial-report/2026/puma-q2-2026-release-eng-final.pdf,Sales by channel,PUMA’s Direct-to-Consumer (DTC) business rose slightly by 0.4% (ca) to € 595.8 million.
Puma,greater_china_growth_ca,Q2 2026,2026Q2,0.9,%,IR Q2 2026 release 2026-07-31,https://about.puma.com/sites/default/files/financial-report/2026/puma-q2-2026-release-eng-final.pdf,Sales by region,Sales in Greater China increased by 0.9% (ca) driven by DTC
Puma,footwear_growth_ca,Q2 2026,2026Q2,-11.7,%,IR Q2 2026 release 2026-07-31,https://about.puma.com/sites/default/files/financial-report/2026/puma-q2-2026-release-eng-final.pdf,Sales by product,Footwear sales declined by 11.7% (ca) to € 935.6 million
Puma,gross_margin,Q2 2026,2026Q2,48.0,%,IR Q2 2026 release 2026-07-31,https://about.puma.com/sites/default/files/financial-report/2026/puma-q2-2026-release-eng-final.pdf,Key developments Q2 2026,Gross profit margin up by around 180 basis points to 48.0%
Puma,ebit_margin (derived: -53.1/1690.6),Q2 2026,2026Q2,-3.1,%,IR Q2 2026 release 2026-07-31,https://about.puma.com/sites/default/files/financial-report/2026/puma-q2-2026-release-eng-final.pdf,Key developments Q2 2026,EBIT improved to € -53.1 million from € -109.1 million in Q2 2025
Puma,inventory_growth,Jun 30 2026,2026Q2,-15.3,%,IR Q2 2026 release 2026-07-31,https://about.puma.com/sites/default/files/financial-report/2026/puma-q2-2026-release-eng-final.pdf,Key developments Q2 2026,"Inventories decreased 15.3% to € 1,821.1 million"
Puma,guidance_FY26_revenue,FY2026,guidance,low- to mid-single-digit decline ca,%,IR Q2 2026 release 2026-07-31,https://about.puma.com/sites/default/files/financial-report/2026/puma-q2-2026-release-eng-final.pdf,FY 2026 outlook,Currency-adjusted sales to decline in the low- to mid-single-digit percentage range
Puma,revenue,Q1 2026 (Jan-Mar),2026Q1,1863.8,EUR m,IR Q1 2026 release,https://about.puma.com/sites/default/files/financial-report/2026/puma-q1-2026-release-eng-final.pdf,Key developments,"Sales of € 1,863.8 million down 1.0% currency adjusted (ca)"
Puma,greater_china_growth_ca,Q1 2026,2026Q1,9.0,%,IR Q1 2026 release,https://about.puma.com/sites/default/files/financial-report/2026/puma-q1-2026-release-eng-final.pdf,Sales by region,positive performance in Greater China of 9.0% (ca)
Puma,gross_margin,Q1 2026,2026Q1,47.7,%,IR Q1 2026 release,https://about.puma.com/sites/default/files/financial-report/2026/puma-q1-2026-release-eng-final.pdf,Key developments,Gross profit margin up 60 basis points to 47.7%
Puma,revenue,Q4 2025 (Oct-Dec),2025Q4,1564.9,EUR m,IR FY 2025 release,https://about.puma.com/sites/default/files/financial-report/2025/puma-q4-fy-2025-release-english-final.pdf,Fourth quarter,"In the fourth quarter, currency-adjusted sales decreased by 20.7% to € 1,564.9 million"
Puma,gross_margin,Q4 2025,2025Q4,40.2,%,IR FY 2025 release,https://about.puma.com/sites/default/files/financial-report/2025/puma-q4-fy-2025-release-english-final.pdf,Fourth quarter,The gross profit margin declined by 750 basis points to 40.2% (Q4 2024: 47.7%).
Puma,revenue,"FY2025 (restated, ex PUMA United)",FY,7296.2,EUR m,IR FY 2025 release,https://about.puma.com/sites/default/files/financial-report/2025/puma-q4-fy-2025-release-english-final.pdf,Highlights,"Sales decline by 8.1% on a currency-adjusted basis (ca) to € 7,296.2 million"
Puma,gross_margin,FY2025,FY,45.0,%,IR FY 2025 release,https://about.puma.com/sites/default/files/financial-report/2025/puma-q4-fy-2025-release-english-final.pdf,Highlights,Gross profit margin down 260 basis points to 45.0%
Puma,ebit_margin (derived: -357.2/7296.2),FY2025,FY,-4.9,%,IR FY 2025 release,https://about.puma.com/sites/default/files/financial-report/2025/puma-q4-fy-2025-release-english-final.pdf,Highlights,Reported EBIT amounts to € -357.2 million
Puma,revenue,Q3 2025 (Jul-Sep),2025Q3,1955.7,EUR m,IR Q3 2025 release,https://about.puma.com/sites/default/files/financial-report/2025/puma-q3-2025-release-english-final.pdf,Highlights,"Sales decrease by 10.4% on a currency-adjusted basis (ca) to € 1,955.7 million"
Puma,revenue,Q2 2025 (Apr-Jun),2025Q2,1942.2,EUR m,IR Q2 2025 release,https://about.puma.com/sites/default/files/financial-report/2025/puma-q2-2025-release-english-final.pdf,Highlights,"Currency-adjusted sales down by 2.0% to € 1,942 million (-8.3% reported)"
Puma,revenue,Q1 2025 (Jan-Mar),2025Q1,2076.0,EUR m,IR Q1 2025 release,https://about.puma.com/sites/default/files/financial-report/2025/puma-q1-2025-release-english-final.pdf,Highlights,"Currency-adjusted sales up by 0.1% to € 2,076 million (-1.3% reported)"
Puma,revenue,"Q4 2024 (Oct-Dec, as first reported)",2024Q4,2289,EUR m,IR preliminary FY 2024 release 2025-01-22,https://about.puma.com/sites/default/files/financial-report/2024/2025-1-22-pressrelease-en.pdf,Release,"reporting a currency adjusted (ca) sales growth of 9.8% to € 2,289 million (+15.5% reported) in the fourth quarter of 2024"
Puma,revenue,FY2024 (as first reported),FY,8817,EUR m,IR preliminary FY 2024 release 2025-01-22,https://about.puma.com/sites/default/files/financial-report/2024/2025-1-22-pressrelease-en.pdf,Release,"On a full-year basis, sales grew by 4.4% (ca) to € 8,817 million (+2.5% reported)"
Puma,ebit_margin,FY2024,FY,7.1,%,IR preliminary FY 2024 release 2025-01-22,https://about.puma.com/sites/default/files/financial-report/2024/2025-1-22-pressrelease-en.pdf,Release,full-year 2024 EBIT margin was 7.1%.
ASICS,revenue,H1 2026 (Jan-Jun),H1 2026,534.4,JPY bn,IR Q2 2026 financial summary with script,"https://assets.asics.com/system/libraries/4225/Consolidated%20Financial%20Summary%20For%20The%20Second%20Quarter%20and%20The%20Six%20Months%20Ended%20June%2030,%202026%ef%bc%88with%20script%ef%bc%89.pdf",FY26Q2 Financial Summary (1),Sales： 534.4 billion yen+32.7%
ASICS,revenue_growth_cc,H1 2026,H1 2026,22.0,%,IR Q2 2026 financial summary with script,"https://assets.asics.com/system/libraries/4225/Consolidated%20Financial%20Summary%20For%20The%20Second%20Quarter%20and%20The%20Six%20Months%20Ended%20June%2030,%202026%ef%bc%88with%20script%ef%bc%89.pdf",FY26Q2 Financial Summary (1),"YoY, +22.0% on a currency-neutralbasis"
ASICS,performance_running_growth (cc 8.2),H1 2026,H1 2026,19.3,%,IR Q2 2026 financial summary with script,"https://assets.asics.com/system/libraries/4225/Consolidated%20Financial%20Summary%20For%20The%20Second%20Quarter%20and%20The%20Six%20Months%20Ended%20June%2030,%202026%ef%bc%88with%20script%ef%bc%89.pdf",Category Performance,Sales： +19.3% YoY(+8.2％ on a currency-neutral basis)
ASICS,greater_china_growth_cc,H1 2026,H1 2026,17.6,%,IR Q2 2026 financial summary with script,"https://assets.asics.com/system/libraries/4225/Consolidated%20Financial%20Summary%20For%20The%20Second%20Quarter%20and%20The%20Six%20Months%20Ended%20June%2030,%202026%ef%bc%88with%20script%ef%bc%89.pdf",Regional commentary,Greater China continued sales growth of +17.6% YoY with strong performance mainly in retail and EC.
ASICS,gross_margin,H1 2026,H1 2026,57.3,%,IR Q2 2026 financial summary with script,"https://assets.asics.com/system/libraries/4225/Consolidated%20Financial%20Summary%20For%20The%20Second%20Quarter%20and%20The%20Six%20Months%20Ended%20June%2030,%202026%ef%bc%88with%20script%ef%bc%89.pdf",FY26Q2 Financial Summary (1),Gross margin： 57.3% (+0.6ppt YoY)
ASICS,operating_margin,H1 2026,H1 2026,22.5,%,IR Q2 2026 financial summary with script,"https://assets.asics.com/system/libraries/4225/Consolidated%20Financial%20Summary%20For%20The%20Second%20Quarter%20and%20The%20Six%20Months%20Ended%20June%2030,%202026%ef%bc%88with%20script%ef%bc%89.pdf",Income statement slide,Operating margin 20.1% 22.5% +2.4ppt
ASICS,guidance_FY26_revenue,FY2026,guidance,1050 (+29.5% YoY),JPY bn,IR Q2 2026 financial summary with script,"https://assets.asics.com/system/libraries/4225/Consolidated%20Financial%20Summary%20For%20The%20Second%20Quarter%20and%20The%20Six%20Months%20Ended%20June%2030,%202026%ef%bc%88with%20script%ef%bc%89.pdf",FY26 Financial Forecast Upward Revision,"Net Sales 950.0 1,050.0 +10.5% +5.3％ +29.5％"
Anta Sports,revenue,H1 2026 (Jan-Jun),H1 2026,43507,RMB m,HKEX interim results announcement 2026-08-26,https://manager.wisdomir.com/files/394/2026/0826/20260826121502_21980085_en.pdf,Highlights,"Revenue increased by 12.9% year on year to RMB43,507 million."
Anta Sports,gross_margin,H1 2026,H1 2026,63.9,%,HKEX interim results announcement 2026-08-26,https://manager.wisdomir.com/files/394/2026/0826/20260826121502_21980085_en.pdf,Financial highlights table,Gross profit margin 63.9 63.4 p 0.5
Anta Sports,operating_margin,H1 2026,H1 2026,27.0,%,HKEX interim results announcement 2026-08-26,https://manager.wisdomir.com/files/394/2026/0826/20260826121502_21980085_en.pdf,Financial highlights table,Operating profit margin 27.0 26.3 p 0.7
Anta Sports,anta_brand_segment_growth,H1 2026,H1 2026,4.8,%,HKEX interim results announcement 2026-08-26,https://manager.wisdomir.com/files/394/2026/0826/20260826121502_21980085_en.pdf,Management discussion,"ANTA segment revenue increased by 4.8% as compared with the same period of 2025 to RMB17,771 million"
Anta Sports,anta_brand_retail_sales,Q2 2026 (Apr-Jun),2026Q2,low-single-digit positive,%,HKEX operational update 2026-07-17,https://manager.wisdomir.com/files/394/2026/0717/20260717190200_13882075_en.pdf,Retail sales Q2 2026 ANTA brand,retail sales (in terms of retail value) of ANTA branded products recorded low-single digit positive growth
Anta Sports,anta_brand_retail_sales,Q1 2026 (Jan-Mar),2026Q1,high-single-digit positive,%,HKEX operational update 2026-04-13,https://manager.wisdomir.com/files/394/2026/0413/20260413164501_71372045_en.pdf,Retail sales Q1 2026 ANTA brand,retail sales (in terms of retail value) of ANTA branded products recorded high-single digit positive growth
Anta Sports,anta_brand_retail_sales,Q4 2025 (Oct-Dec),2025Q4,low-single-digit negative,%,HKEX operational update 2026-01-20,https://manager.wisdomir.com/files/394/2026/0120/20260120164502_67400748_en.pdf,Retail sales Q4 2025 ANTA brand,retail sales (in terms of retail value) of ANTA branded products recorded low-single digit negative growth
Anta Sports,revenue,FY2025,FY,80219,RMB m,HKEX annual results announcement 2026-03-25,https://manager.wisdomir.com/files/394/2026/0325/20260325121501_54061636_en.pdf,Highlights,"Revenue increased by 13.3% year on year to RMB80,219 million."
Anta Sports,gross_margin,FY2025,FY,62.0,%,HKEX annual results announcement 2026-03-25,https://manager.wisdomir.com/files/394/2026/0325/20260325121501_54061636_en.pdf,Management discussion,overall gross profit margin slightly declined by 0.2% points to 62.0% (2024: 62.2%)
Anta Sports,operating_margin,FY2025,FY,23.8,%,HKEX annual results announcement 2026-03-25,https://manager.wisdomir.com/files/394/2026/0325/20260325121501_54061636_en.pdf,Management discussion,Group effectively lifted its overall operating profit margin at 23.8% (2024: 23.4%)
Anta Sports,puma_stake,Oct 7 2026,n/a,29.06% of Puma SE acquired,n/a,HKEX announcement list 2026-10-07 (title only),https://ir.anta.com/en/news.php,"Announcements list, item dated 2026.10.07",MAJOR TRANSACTION - COMPLETION OF THE ACQUISITION OF 29.06% EQUITY INTEREST IN PUMA SE
Li Ning,revenue,H1 2026 (Jan-Jun),H1 2026,15235,RMB m,HKEX interim results announcement 2026-08-20,https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0820/2026082001445.pdf,Highlights,"Revenue rose by 2.8% to RMB15,235 million"
Li Ning,gross_margin,H1 2026,H1 2026,50.9,%,HKEX interim results announcement 2026-08-20,https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0820/2026082001445.pdf,Financial highlights,Gross profit margin (%) 50.9 50.0
Li Ning,operating_margin (derived: 2451.9/15235.3),H1 2026,H1 2026,16.1,%,HKEX interim results announcement 2026-08-20,https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0820/2026082001445.pdf,Income statement,"Operating profit 2,451,890 2,438,485"
Li Ning,footwear_growth (derived: 8283.8/8230.7-1),H1 2026,H1 2026,0.6,%,HKEX interim results announcement 2026-08-20,https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0820/2026082001445.pdf,Note 4 revenue by category,"Footwear 8,283,759 8,230,716"
Li Ning,channel_split,H1 2026,H1 2026,franchised 46.0; direct 23.1; e-commerce 29.7,% of revenue,HKEX interim results announcement 2026-08-20,https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0820/2026082001445.pdf,Revenue by sales channel,Sales to franchised distributors 46.0 46.5 (0.5)
Li Ning,inventory_growth (derived: 2701.6/2693.8-1; vs Dec 2025),Jun 30 2026,H1 2026,0.3,%,HKEX interim results announcement 2026-08-20,https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0820/2026082001445.pdf,Balance sheet,"Inventories 11 2,701,596 2,693,793"
```

## B. Comparison

### B1. Quarterly revenue growth, constant currency (%), aligned to calendar quarters

| Calendar qtr | Nike (fiscal qtr) | Nike cn | Deckers | HOKA (rep.) | On | Amer (1) | Lululemon (2) | Birkenstock | adidas (3) | Puma | Under Armour | VF (4) | Skechers |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2024 Q3 | Q1 FY25 | -9 | 20.4 | 34.7 | 33.2 | 17 | 8 | n/a | 10 | n/a | -10 | -6 | 15.9 |
| 2024 Q4 | Q2 FY25 | -9 | 16.6 | 23.7 | 40.6 | 23 | 8 | n/a | 19 | 9.8 | -6 | 2 | 12.8 |
| 2025 Q1 | Q3 FY25 | -7 | 7.5 | 10.0 | 40.0 | 23 | 8 | 18 | 13 | 0.1 | -10 | -3 | 9.0 |
| 2025 Q2 | Q4 FY25 | -11 | 16.3 | 19.8 | 38.2 | 23 | 6 | 16 | 8 | -2.0 | -4 | -2 | 11.5 |
| 2025 Q3 | Q1 FY26 | -1 | 8.3 | 11.1 | 34.5 | 30 | 7 | 15.5 | 8 | -10.4 | -6 | -1 | private |
| 2025 Q4 | Q2 FY26 | 0 | 6.8 | 18.5 | 30.6 | 26 | 4 | 17.8 | 10 | -20.7 | -6 | 1.5 | private |
| 2026 Q1 | Q3 FY26 | -3 | 7.7 | 14.5 | 26.4 | 26 | 2 | 14 | 14 | -1.0 | -4 | 3 | private |
| 2026 Q2 | Q4 FY26 | -4 | 4.8 | 7.7 | 21.6 | 30 | -5 | 15 | 14 | -9.4 | -4 | 0 | private |
| 2026 Q3 | Q1 FY27 | -5 | not yet | not yet | not yet | 20-22 (prelim. guide) | Q3 guide -10 to -11 (reported) | not yet | not yet | not yet | not yet | not yet | private |

Notes:
1. Amer: reported growth where no constant-currency figure was disclosed (2024 Q3 to 2025 Q3).
2. Lululemon:
   - 2024 Q4 and 2025 Q4 exclude the 53rd week (+8% reported and +4% constant dollar).
   - 2025 Q3 is reported growth.
3. adidas: the 2025 Q2 to Q4 rates include the Yeezy prior-year base. Brand adidas alone grew 12%, 12% and 11%.
4. VF:
   - 2024 Q3, 2024 Q4 and 2025 Q4 are reported growth.
   - 2025 Q4 is derived: 2,875.8 / 2,833.9.
   - 2026 Q1 and 2026 Q2 are ex-Dickies constant-dollar growth. Reported growth was +1% and -5%.

Other cells:
- Birkenstock 2025 Q3 is reported growth, derived from 526.3 / 455.8.
- Puma 2024 Q4 is the currency-adjusted rate as first reported, before the PUMA United restatement.

**Composites (my calculation, `scratchpad/scripts2/calc.py`)**
- **Weighted** = cc growth weighted by each peer's prior-year quarterly revenue. Revenue is converted at fixed assumed rates of EUR = 1.10 USD and CHF = 1.15 USD.
- **Incumbents** = adidas, Puma, Under Armour, VF, Skechers.
- **Challengers** = Deckers, On, Amer, Lululemon, Birkenstock.

| Calendar qtr | Nike cn | Peer median | Peer weighted | Incumbent median | Challenger median | adidas | Nike minus weighted (pp) | Nike minus incumbent median (pp) |
|---|---|---|---|---|---|---|---|---|
| 2024 Q3 | -9 | 12.9 | 7.9 | 2.0 | 18.7 | 10 | -16.9 | -11.0 |
| 2024 Q4 | -9 | 12.8 | 12.2 | 9.8 | 19.8 | 19 | -21.2 | -18.8 |
| 2025 Q1 | -7 | 8.5 | 8.4 | 0.1 | 18.0 | 13 | -15.4 | -7.1 |
| 2025 Q2 | -11 | 9.8 | 7.7 | -2.0 | 16.3 | 8 | -18.7 | -9.0 |
| 2025 Q3 | -1 | 8.0 | 6.0 | -3.5 | 15.5 | 8 | -7.0 | +2.5 |
| 2025 Q4 | 0 | 6.8 | 5.3 | -2.2 | 17.8 | 10 | -5.3 | +2.2 |
| 2026 Q1 | -3 | 7.7 | 9.4 | 1.0 | 14.0 | 14 | -12.4 | -4.0 |
| 2026 Q2 | -4 | 4.8 | 7.1 | -2.0 | 15.0 | 14 | -11.1 | -2.0 |

### B2. Greater China and Asia (latest available, %)

| Company | Period | Greater China or Asia growth | Basis |
|---|---|---|---|
| Nike | Q1 FY27 (Jun-Aug 2026) | -22 reported, -26 cn | Greater China |
| Nike | Q4 FY26 / Q3 FY26 / Q2 FY26 | -17 / -10 / -16 cn | Greater China |
| Amer Sports | Q2 2026 / Q1 2026 / FY2025 | +35.5 / +44.5 / +43.4 | Greater China, reported |
| adidas | Q2 2026 / Q1 2026 / Q4 2025 / FY2025 | +15 / +17 / +15 / +9 | Greater China, cn |
| ASICS | H1 2026 | +17.6 | Greater China, cn |
| On | Q2 2026 | +43.1 reported, +54.7 cc | Asia-Pacific (incl. Greater China) |
| Lululemon | Q2 FY26 (May-Jul 2026) / Q1 FY26 | +4 reported (-2 cc) / +30 (+23 cc) | China Mainland |
| Puma | Q2 2026 / Q1 2026 | +0.9 / +9.0 | Greater China, ca |
| Anta Group | H1 2026 | +12.9 group revenue; ANTA segment +4.8 | China-centred, reported |
| Li Ning | H1 2026 | +2.8 | China-centred, reported |
| Skechers | Q2 2025 / Q1 2025 | -8.2 / -15.9 | China, reported |
| Under Armour | Q1 FY27 (Apr-Jun 2026) | -7 reported, -10 cc | Asia-Pacific |

### B3. Margins

**Gross margin, latest quarter** (calendar Q2 2026 or nearest)

| Company | Gross margin (%) | Note |
|---|---|---|
| On | 65.4 | |
| Amer | 65.6 | incl. 390 bp tariff refund |
| Anta | 63.9 | H1 |
| Lululemon | 60.5 | incl. 560 bp refund |
| Birkenstock | 59.1 | |
| ASICS | 57.3 | H1 |
| Deckers | 56.4 | |
| VF | 54.9 | |
| Under Armour | 54.1 | incl. IEEPA refund |
| adidas | 52.5 | |
| Li Ning | 50.9 | H1 |
| Puma | 48.0 | |
| Nike | 42.8 | Q1 FY27 |

Nike's Q4 FY26 gross margin is recorded at 49.2% in the repo facts file. It is an outlier against its other quarters (40.2 to 42.8) and was not re-examined here.

**Full-year gross margin trend (%)**

| Company | Earliest | Middle | Latest |
|---|---|---|---|
| Nike | FY24 44.6 | FY25 42.7 | FY26 42.9 |
| Deckers | FY24 55.6 | FY25 57.9 | FY26 57.7 |
| On | 2023 59.6 | 2024 60.6 | 2025 62.8 |
| Amer | | 2024 55.4 | 2025 57.6 |
| adidas | 2023 47.5 | 2024 50.8 | 2025 51.6 |
| Under Armour | FY24 about 46.1 (derived) | FY25 47.9 | FY26 45.5 |
| Lululemon | | FY24 59.2 | FY25 56.6 |
| Puma | | 2024 47.6 (restated) | 2025 45.0 |
| Anta | | 2024 62.2 | 2025 62.0 |

**Operating margin (latest full year)**

| Company | Operating margin (%) | Basis |
|---|---|---|
| Deckers | 23.1 | FY26, derived |
| Anta | 23.8 | 2025 |
| Lululemon | 19.9 | FY25 |
| On | 12.5 | 2025, derived |
| Amer | 10.7 | 2025 |
| adidas | 8.3 | 2025 |
| Nike EBIT | 8.3 | FY26 (12.7 in FY24) |
| VF | 6.0 | FY26 |
| Under Armour | -3.3 | FY26 |
| Puma | -4.9 | 2025, derived |

### B4. Share-shift arithmetic (my calculation, clearly hypothetical)

Method: for each aligned quarter, "Nike at peer growth" = Nike's prior-year quarter revenue x (1 + peer weighted cc growth). I compare this with Nike's prior-year revenue x (1 + Nike cn growth). Both legs are constant currency, so FX is excluded. In the table, "Nike actual" is reported revenue.

| Calendar qtr | Nike qtr | Prior-year Nike revenue ($m) | Nike at peer weighted growth ($m) | Nike actual ($m) | Gap vs Nike-at-cc ($m) |
|---|---|---|---|---|---|
| 2024 Q3 | Q1 FY25 | 12,939 | 13,957 | 11,589 | 2,182 |
| 2024 Q4 | Q2 FY25 | 13,388 | 15,015 | 12,354 | 2,832 |
| 2025 Q1 | Q3 FY25 | 12,429 | 13,475 | 11,269 | 1,916 |
| 2025 Q2 | Q4 FY25 | 12,606 | 13,578 | 11,097 | 2,359 |
| 2025 Q3 | Q1 FY26 | 11,589 | 12,280 | 11,720 | 807 |
| 2025 Q4 | Q2 FY26 | 12,354 | 13,005 | 12,427 | 651 |
| 2026 Q1 | Q3 FY26 | 11,269 | 12,325 | 11,279 | 1,394 |
| 2026 Q2 | Q4 FY26 | 11,097 | 11,881 | 10,972 | 1,228 |

Totals:
- **Year-on-year shortfall, summed over the 8 quarters:** about $13.4B against the weighted peer composite, about $14.4B against the peer median and about $17.3B against adidas alone.
- **FY26 revenue level, compounding peer growth from FY24 quarters** (my calculation; actual FY26 was $46.4B):

| Benchmark | Nike FY26 at benchmark growth | Gap to actual |
|---|---|---|
| Weighted peer set | about $59.9B | about $13.5B |
| Peer median | about $60.9B | about $14.5B |
| adidas growth path | about $64.4B | about $18.0B |
| Incumbent median (adidas, Puma, UA, VF, Skechers) | about $51.8B | about $5.4B |

  At its own cn rates the same compounding gives $45.8B. The $0.6B difference from actual is FX.
- **Q1 FY27 (Jun-Aug 2026):** at the latest peer weighted rate (+7.1%), Nike would have had about $12.55B against $11.21B actual, a gap of about $1.3B. At Amer's preliminary Q3 rate the gap would be larger still.

Caveats on this arithmetic:
- The peers are smaller. Their combined quarterly revenue is roughly $20B against Nike's $11B to 12B. Fast-growing challengers grow from small bases, so "Nike at peer growth" is an upper bound.
- The incumbent-median benchmark ($5.4B) is the most conservative estimate. The adidas benchmark ($18.0B) is the most demanding.
- About one month of calendar mismatch remains, and the FX weights are assumptions.

### B5. Current guidance (latest disclosed)

| Company | Period | Guidance | Source date |
|---|---|---|---|
| adidas | FY2026 | cn revenue +9% to +10% (raised from high single digit); operating profit around EUR 2.3bn | 2026-07-30 |
| Amer Sports | FY2026 / Q3 2026 / long term | FY2026 about +24% reported; Q3 2026 +20% to 22% (raised 2026-09-16); low-double-digit to mid-teens CAGR | 2026-08-18, 2026-09-16 |
| On | FY2026 / 2026-2029 | low-20% cc growth, gross margin at least 65%; high-teens cc CAGR through 2029 | 2026-08-11, 2026-09-22 |
| ASICS | FY2026 | net sales JPY 1,050bn (+29.5%), raised | Aug 2026 |
| Birkenstock | FY26 (to Sep 2026) | +15% cc, raised | 2026-08-13 |
| Deckers | FY27 (to Mar 2027) | $5.86bn to $5.91bn (about +7% to 8%, derived); HOKA low double digit; FY28 to FY30 high single digit | 2026-07-23 |
| VF | FY27 | +2% or better C$ ex Dickies, raised | 2026-07-29 |
| Lululemon | FY26 (to Jan 2027) / Q3 | -5% to -7%, cut from -1% to 0%; Q3 -10% to -11% | 2026-09-03 |
| Under Armour | FY27 | mid-single-digit decline, cut from slight decline | 2026-08-07 |
| Puma | FY2026 | low- to mid-single-digit decline ca | 2026-07-31 |
| Anta / Li Ning | | no numeric revenue guidance found in the documents read | |

### B6. Narrative

1. **The market grew while Nike shrank.**
   - Weighted peer growth was positive in every aligned quarter, at +5.3% to +12.2% in constant currency. The median ran +4.8% to +12.9%.
   - Nike's currency-neutral growth was -7% to -11% through FY25. It then improved to between 0% and -4% in FY26 and slipped back to -5% in Q1 FY27.
   - Nike trailed the weighted peer set by 5 to 21 percentage points every quarter, an average of about 13.5 pp.
2. **The split is challengers against incumbents, but the best incumbent disproves inevitability.**
   - The challenger median (HOKA, On, Amer, Lululemon, Birkenstock) grew 14% to 20% a quarter.
   - The incumbent median (adidas, Puma, UA, VF, Skechers) hovered around zero.
   - That pattern looks structural: premium running and outdoor specialists are taking share from scaled lifestyle-led brands. Puma (-9.4% in Q2 2026, footwear -11.7%), Vans (-8%) and Under Armour (-4%; footwear -8% to -16% for four straight quarters) show the same disease.
   - However, adidas has a similar scale, wholesale-heavy model and China exposure. It grew 8% to 19% cc in every quarter, with DTC +25% and running about +30% in Q2 2026.
   - Since mid-2025 Nike has roughly matched the weak incumbents (within about 2 to 4 pp, and ahead of them in CQ3 and CQ4 2025). It still trailed adidas by 9 to 18 pp.
3. **China is the sharpest discriminator.**
   - Nike Greater China fell 26% cn in Jun-Aug 2026 and 10% to 17% in each of the prior three quarters.
   - In the same market, other foreign brands grew: Amer +35.5%, adidas +15%, ASICS +17.6% (H1), Puma +0.9% and Lululemon +4% reported.
   - Domestic champions grew modestly: ANTA segment +4.8% and Li Ning +2.8% in H1 2026.
   - China is not collapsing for western brands. Nike's China decline is roughly 30 to 40 pp worse than adidas's.
4. **Margins point to Nike-specific execution.**
   - Nike has the lowest gross margin in the set (42.8%). Its full-year gross margin fell 170 bp from FY24 to FY26, and its EBIT margin went from 12.7% to 8.3%.
   - adidas raised gross margin 410 bp over 2023 to 2025. Deckers, On and Amer also expanded despite tariffs.
   - The peers that compressed margins are the ones in reset (Puma -260 bp, UA -240 bp in FY26, Lululemon -260 bp). That is the company Nike is keeping.
5. **The challenger wave is decelerating.**
   - HOKA slowed from +34.7% (CQ3 2024) to +7.7% (CQ2 2026).
   - On slowed from about 40% cc to 21.6%.
   - Lululemon has turned negative and cut guidance twice.
   - The structural pressure on Nike from new entrants is therefore real but fading at the margin, which favours fixability.

## C. Verdict

**Mostly company-specific and fixable, with a real but secondary structural headwind.** I would weight it roughly two-thirds Nike-specific and one-third structural, judged by the share-shift ranges: about $5.4B of FY26 shortfall against weak incumbents, versus about $13.5B against the full peer set and about $18.0B against adidas.

**Strongest evidence for company-specific:**
1. **adidas.**
   - Same size class, same channel mix and same China exposure as Nike.
   - It grew +14% cc in CQ2 2026 against Nike's -4%, and +15% in Greater China against Nike's -17%. It also expanded gross margin to 52.5% while Nike sat at 42.8%.
   - On adidas's growth path Nike's FY26 revenue would have been about $18B higher (my calculation).
2. **Greater China.** Every foreign brand with a 2026 China-specific disclosure grew there (Amer, adidas, ASICS, Puma, Lululemon), while Nike fell 26% cn in its latest quarter. Under Armour's broader Asia-Pacific region fell 7%, and Skechers China fell in 2025.
3. **Market growth.** The peer market grew in every quarter (weighted +5% to +12% cc), so Nike's decline is not a shrinking market.
4. **Margins.** Nike's gross margin is the lowest of 13 peers and still below FY24, which indicates discounting, inventory clean-up and mix problems inside Nike rather than a category-wide price collapse.

**Evidence for a structural component:**
1. **The incumbent cohort.** The cohort (Puma, UA, Vans, Skechers in its last public quarters) has also stalled or shrunk, while premium specialists (HOKA, On, Amer, ASICS at +22% cc in H1 2026) grew mid-teens or better. Some share has migrated, durably, to performance-running and outdoor specialists.
2. **Nike against the weak incumbents.** Nike's underperformance against that weaker cohort is small, about 2 to 4 pp in CQ1 and CQ2 2026, and it was ahead of them in CQ3 and CQ4 2025.

**What would change the call:**
- **Towards structural:** a decline at adidas, or Nike Greater China still falling at double digits while peers there keep growing through FY27.
- **Towards company-specific and fixable:** Nike returning to growth while challengers keep decelerating (Deckers guides HOKA to low double digits; On guides to low-20% falling towards high-teens).
- **The next test:** the CQ3 2026 releases due late October and November.
