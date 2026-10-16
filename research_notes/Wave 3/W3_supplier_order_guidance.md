# W3: Supplier order books, the other side of the trade (Oct 16, 2026)

**Question.** Nike's contract manufacturers see Nike orders 3 to 9 months ahead. What have they said, 2025 to Oct 16 2026, about Nike orders, share of business, 2026 H2 and 2027 visibility, pricing and capacity? Do they see Nike recovering in H1 2027 (long) or still falling while other brands grow (short)? How does that compare with Nike's FY28 consensus?

**Companion file.** `W3_supplier_statements.csv` (58 rows: date, company, ticker, speaker type, original quote, English translation, metric, number, unit, horizon, direction for Nike, tag, URL, notes).

**Tags.** OPENED = I opened the page or file this session. Many OPENED news pages were read through the fetch tool, which returns a model-written extract of the page; the Chinese quotes are the extract's quotes of the page text, not my own transcription, and a few were verified against a second source. Yue Yuen's interim results (HKEX PDF), six Feng Tay conference decks and the Feng Tay 2026 Q2 financial report were read directly as PDF text. SNIPPET = seen only in a search result. DERIVED = my arithmetic. "Opinion" = management or analyst outlook, recorded but not used as an explanation.

**Overlap.** Monthly supplier revenue series are NOT redone; this note extends `Long or short cruxes/supplier_nowcast.md` and `data/definitive/suppliers/` with the qualitative and forward-looking layer. Quarterly YoY figures below are recomputed from the repo files only to anchor the statements.

---

## 1. Verdict

**Smoking gun: NO.** No supplier says Nike orders recover in H1 2027, and none says they keep falling. The farthest-dated Nike-specific statement is a Sep 9 2026 analyst paraphrase of Feng Tay's Sep 8 conference: "most major customers are still negotiating their 2027 order strategy; actual pull-in volume and mix not yet clear." The firm-order window is about 3 months and the rolling forecast about 6 months, so Feng Tay cannot see past roughly March 2027 (Nike's FY27 Q4 is Mar to May 2027). That is a structural limit, not a data gap: Yue Yuen says normal order lead time is 10 to 12 weeks and rising numbers of orders ask for 30 to 45 days (HKEX, OPENED).

**Direction of the evidence: leans SHORT on the Nike-specific suppliers, with one long-ish item.**

| Evidence | Direction | Grade |
|---|---|---|
| Feng Tay (Nike 88% to 90% of sales) USD revenue Jul to Sep 2026 -8.4% (DERIVED), after -2.6% in Q2 and -3.5% in Q1; implied Nike-only about -10.4% to -11.6% (DERIVED, assumption in section 4) | SHORT | Strong (reported numbers) |
| Feng Tay gross margin 19% in Q2 2026 vs 24%, operating margin 6% vs 12% (company deck, OPENED): deleverage with flat NT$ revenue | SHORT | Strong |
| Huali CSC/Haitong classification: Nike and Puma "still bottoming/adjusting"; adidas, On, Asics, HOKA growing (sell-side, OPENED) | SHORT (relative) | Moderate, opinion |
| Shenzhou (JPM): Nike and Puma "main drags" in H1; declines "narrowing" in H2 (opinion) | Mixed | Weak, opinion |
| Pou Chen / Yue Yuen: "US-brand adjustments nearly finished", H2 shipments to beat H1, Sep 2026 manufacturing +6.6% YoY | LONG (mild) | Weak: US brand not named, one month, brand mix unknown |
| Feng Tay: 2027 growth from "new Nike models starting to ship" plus Salomon capacity | LONG (thin) | Weak, analyst paraphrase |
| Feng Tay capex commitments (unpaid construction contracts) NT$612m at Jun 2026 vs NT$1,338m a year earlier (-54%, DERIVED) and "no special capacity expansion for Nike" (Dec 2025) | SHORT (supplier is not building for a rebound) | Moderate |

**Honest bottom line for the pitch.** The suppliers support "no recovery visible through at least Q1 2027 and Nike-specific", not "orders still falling into H1 2027". Their numbers are consistent with Nike's own FY27 Q2 consensus revenue of $11,176M (-10.1% YoY; consensus note, Yahoo Oct 13 2026) and with an FY27 total of -7.0%. They are silent on FY28 (starts Jun 2027), so they neither confirm nor contradict the consensus +1.1% ($43,645M vs $43,152M).

## 2. Headline statements (quote, translation, tag)

All rows are in the CSV; the ones that matter most:

1. **Feng Tay, Sep 9 2026 (MoneyDJ on the Sep 8 conference, OPENED, analyst-attributed).** 「目前主要客戶對2027年的訂單策略多仍在洽談階段 ... 實際拉貨規模及產品組合尚未明朗」 = "Most major customers are still negotiating their 2027 order strategy; actual volume and mix not yet clear." Also 「今年全年生產出貨量及營收均可能呈低個位數衰退 ... Nike動能仍平緩」 = "Full-year shipments and revenue likely to fall low single digits ... Nike momentum still flat." And 「成長動能主要來自Salomon新增產能逐步放量，以及Nike新鞋型開始出貨」 = "2027 growth mainly Salomon capacity ramp and the start of shipments of new Nike models."
2. **Feng Tay, Dec 4 2025 (Fugle memo, OPENED).** 「預期營收規模與今年(2025)差不多」 = revenue flat in 2026; 「主要客戶 Nike 這邊不會有特別的擴充」 = no special capacity expansion for Nike; Salomon capacity up low-to-mid teens percent; 「面臨客戶持續的價格壓力」 = continued customer price pressure. **Outcome check:** 2026 is tracking to a low-single-digit decline (above), gross margin -5 points. Management guidance was too optimistic by roughly the amount of the decline.
3. **Yue Yuen, Aug 12 2026 (HKEX interim results, OPENED, printed pp. 16 to 17, 24).** "In the second half of 2026, the Group expects the operational environment to remain unsettled ... with the visibility of near-term order demand yet to improve." H1 shipments 118.6m pairs (-6.4%), ASP US$20.95 (+1.6%), manufacturing gross margin 14.3% (-3.4 points) from "operating deleveraging". Newly built Indonesia/India lines to be started "flexibly ... in response to evolving demand". Capex US$129.3m vs US$146.0m.
4. **Pou Chen, Jun 5 2026 call (Fugle, OPENED).** Visibility "不高", lead time 10 to 12 weeks; Q2 pairs to recover vs Q1 (Outcome: Q2 61.7m vs Q1 56.9m pairs, repo DERIVED, call was right); 「因公司採多品牌代工策略，不便提供單一品牌數據」 = will not give single-brand data. Oct 12 to 15 2026 press (MoneyDJ, OPENED): 「美系品牌調整已接近尾聲」 = US-brand adjustment nearly over; H2 shipments > H1; USD view 「量跌價穩」 (volume down, price stable); analysts see mid-single-digit USD revenue decline for 2026.
5. **Huali (300979.SZ; customers include Nike, Converse, Vans, adidas, On, HOKA, Puma), Sep 8 and 14 2026 management investor-survey records (OPENED).** 「部分品牌基于对未来经济形势的不确定性，预告订单相对保守」 = some brands give conservative order previews; 「本期订单有所下滑，导致产能利用率有所降低」; management "cautiously optimistic" for H2. H1 pairs 104m (-9.0%), ASP about RMB105 (-5.2%), utilization 90.3% (-5.5 points), total capacity -3.1% (CSC research, OPENED). 2026 adds one new factory (Haitong snippet).
6. **Shenzhou, JPM Aug 6 to Sep 10 2026 (OPENED, opinion).** H2 sales forecast cut from +10% (Aug 6) to +2% (Sep 10) within five weeks, 2027 sales +5%, profit +14%; Nike and Puma "main drags", declines "narrowing".
7. **Lai Yih, May 6 2026 (udn, OPENED).** Q1 revenue -26.9% on Converse (a Nike Inc brand) shipment drop plus an adidas product transition; full year "flat", H2 better than H1; sneakers about 90% of revenue; HOKA "main long-term growth driver". Derived USD Q1 -24.1%, Q2 -6.2%, Q3 +1.3% (repo series).
8. **Chih Chiang (6768), Apr 27 2026 (ctee, OPENED).** 「耐吉休閒款出貨量下滑」 = Nike casual-shoe shipments declining; adidas shipments +20% in 2025; analysts see 2026 pairs -4.5% (but a Jun 17 udn piece says +10%: sources conflict, flagged).

## 3. Management characterizations of Nike versus other brands

| Brand | What suppliers say (2026) | Source / tag |
|---|---|---|
| Nike | Feng Tay: "momentum flat", "no expansion"; Chih Chiang: casual shipments down; Huali (sell-side): "bottoming"; Shenzhou (JPM): "main drag"; Lai Yih: Converse down | OPENED; mostly opinion |
| adidas | Lai Yih: core customer, product transition in H1 then "restocking wave"; Huali: "high growth", planned capacity of 50m+ pairs; Shenzhou: momentum; Chih Chiang: shipments +20% in 2025, football boots +3% to 4% in 2026; fabrics (FENC, Kuang Hsing): orders up | OPENED |
| On | Fulgent Sun: #1 customer since 2025, revenue +32.7% in Jul to Sep USD (repo); Huali: "good growth" | OPENED |
| HOKA | Lai Yih: long-term growth driver, over 20% capacity growth room (analyst); Huali: "accelerating in H2" (sell-side) | OPENED |
| Salomon | Feng Tay: double-digit shipment growth, capacity up low-to-mid teens percent | OPENED |
| lululemon | Not named by any supplier in 2025 to 2026 sources opened. Eclat visibility about 6 months, cautiously optimistic, no brand split | Gap, see section 8 |

Read: the weakness is Nike-specific plus Puma, not an industry-wide order drought. This reproduces the repo's earlier finding (supplier_nowcast.md) with management-language support. The characterizations are mostly sell-side or press labels, not supplier executives naming Nike (Yue Yuen, Pou Chen and Huali explicitly refuse to name brands).

## 4. Quantitative guidance extracted and recomputed

| Item | Number | Source / tag |
|---|---|---|
| Feng Tay Nike share of sales | 88% to 90% (press 2026); "over 85%" (Oct 2025); single customer NT$69.6bn of NT$83.5bn in 2025 = 83.3% (DERIVED from filing) | OPENED |
| Feng Tay 2026 shipments | 118m pairs (+1%, Feb) to 117m (May); Sep: "low single-digit decline" (sell-side, not guidance; Feng Tay does not disclose pairs) | OPENED |
| Feng Tay order visibility | 3 months firm, 6 months rolling, unchanged Jun 2025, Dec 2025, Sep 2026 | OPENED |
| Feng Tay USD revenue YoY | Q1 CY26 -3.5%, Q2 -2.6%, Q3 -8.4%; Jan to Sep -5.0% (NT$ -3.1%) | DERIVED from repo files |
| Feng Tay margins | GM 17% (Q1) and 19% (Q2) vs 21% and 24%; OPM 6% vs 12% in Q2 | OPENED |
| Feng Tay margin sensitivity | At the Q2 2025 gross margin (24%), Q2 2026 gross profit would be NT$4,891m vs NT$3,960m, i.e. NT$931m higher (DERIVED: 20,380 x 0.24) | DERIVED |
| Feng Tay capex | H1 2026 NT$1,066m vs NT$3,032m full-year 2025; unpaid construction contracts NT$612m (Jun 26) vs NT$978m (Dec 25) vs NT$1,338m (Jun 25) | OPENED, DERIVED |
| Feng Tay output mix 2025 | Vietnam 43%, India 35%, Indonesia 14%, China 8% | OPENED |
| Feng Tay receivables from top customer | 69% (Jun 25), 66% (Dec 25), 60% (Jun 26) | OPENED |
| Yue Yuen H1 2026 | Pairs 118.6m (-6.4%), ASP US$20.95 (+1.6%), mfg revenue US$2,485.1m (-4.8%), mfg GM 14.3% (-3.4 pts) | OPENED |
| Yue Yuen units vs price | -6.4% units, +1.6% price: price did not fall, units did (matches Nike G3 finding at the retailer end) | DERIVED |
| Yue Yuen monthly | Jul 2026 -10.0%, Sep +6.6%, Jan to Sep mfg -3.8% | OPENED |
| Huali H1 2026 | Pairs 104m (-9.0%), ASP about RMB105 (-5.2%), utilization 90.3% (-5.5 pts), NA 74% of sales | OPENED (sell-side data) |
| Shenzhou H1 2026 | Revenue RMB14.18bn (-5.3%), sportswear -10.7%, GM 22.6% (-4.5 pts) | OPENED (sell-side) |
| Capacity plans | Yue Yuen: Indonesia/India, ramp "flexible"; Huali: 1 new factory in 2026 vs 7 in 2024 to 2025; Eclat Indonesia mass production Q4 2027; Shenzhou Indonesia garments from Q4 2027; Chih Chiang Indonesia 6m to 12m pairs over 3 years | OPENED |
| Pricing | Pou Chen and Huali both state cost-plus quoting with a lag; Feng Tay has an annual price negotiation with Nike including tariffs and FX re-pricing within about 1 month; Pou Chen says USD prices "stable" | OPENED |

**Implied Nike-only change at Feng Tay (DERIVED, assumptions stated).** Q3 CY26 total USD -8.4%. If non-Nike customers (10% to 15% of base; Salomon double-digit growth) grew +10%, Nike = (-8.4 - 1.0 to 1.5) / (0.90 to 0.85) = about -10.4% to -11.6%. Salomon growth of +10% is management guidance, not the realized rate; if non-Nike grew 0%, Nike is -9.3% to -9.9%.

## 5. Comparison with Nike's consensus path

| Period | Nike consensus (Yahoo, Oct 13 2026) | Supplier read |
|---|---|---|
| FY27 Q2 (Sep to Nov 2026) | $11,176m, -10.1% YoY | Feng Tay Jul to Sep USD -8.4%, implied Nike -10.4% to -11.6%: in line |
| FY27 full year | $43,152m, -7.0% | Consistent with "momentum flat" plus Q1 FY27 decline; no supplier sees improvement before 2027 |
| FY28 (Jun 2027 to May 2028) | $43,645m, +1.1% | Suppliers have no visibility; only "new Nike models start shipping" (analyst paraphrase) and press "Nike normalizes after 2027" (no named source) |

Suppliers lead Nike revenue by roughly one to two quarters (repo `leadlag_correlations.csv`), so Feng Tay's current rolling forecast to about March 2027 maps to Nike's FY27 Q3 to Q4 shipments to customers. A real inflection would need to show in Feng Tay's USD revenue turning from -8% toward flat in Dec 2026 to Mar 2027 months; that is the testable catalyst, along with Q4 2026 monthly prints (Nov to Jan).

## 6. Alternatives tested for "Feng Tay revenue falling"

| Alternative | Test | Result |
|---|---|---|
| FX (weaker TWD) | NT$ -2.1% vs USD -8.4% in Q3; TWD averaged about 32.0 vs 30.0 | Ruled out as cause of USD drop; FX moved NT$ revenue the other way. Press attributes lower NT$ ASP to FX (ctee), but USD is the relevant unit |
| Non-Nike customers dragging | Salomon double-digit growth, other brands growing (MoneyDJ) | Ruled out; Nike is the drag |
| Industry-wide order drought | Lai Yih Q3 +1.3%, Fulgent Sun +32.7%, Pou Chen NT$ +4.7% (USD -2.0%) | Ruled out; weakness is Nike-concentrated |
| Capacity moves to India (35% of output) disrupting shipments | Feng Tay Jun 2025 call said transfers would "short-term affect shipments" | Cannot be fully ruled out for 2025 H2; does not explain 2026 gross margin -5 pts with flat NT$ revenue |
| Deliberate Nike supply cut vs lower sell-through | Filings and calls cannot separate (Nike "conservative ordering" per analysts; Nike wholesale order book per Nike) | **Remains unresolved.** Data that would decide: Nike's reported wholesale futures, Circana/GfK sell-through by brand |
| Sell-side miss is Nike-specific mis-forecasting | Yue Yuen +3% to 5% (Dec 2025) vs -4.8% actual; JPM Shenzhou H2 +10% to +2% in 5 weeks | Sell-side supplier forecasts have been too high all year; discount "recovery" forecasts accordingly |

## 7. Routes tried and results (log for the next person)

| # | Target | Route | Result |
|---|---|---|---|
| 1 | Feng Tay | IR page `fengtay.com/tw/investor/conference`, six 2025 to 2026 deck PDFs (pdftotext) | WORKED for numbers; decks are financial tables only, Q&A slide blank, no guidance text |
| 2 | Feng Tay | Fugle AI memos for each call date (Jun 2025, Dec 2025 worked; 2026-03/06/09 URLs 404) | PARTIAL |
| 3 | Feng Tay | MoneyDJ, ctee, chinatimes, udn articles (Sep 9, May 4, Apr 12, Feb 11 2026) | WORKED (analyst-attributed) |
| 4 | Feng Tay | 2026 Q2 financial report PDF notes (commitments, receivables) | WORKED |
| 5 | Yue Yuen | HKEX interim PDF (fetched, pdftotext) | WORKED (full text) |
| 6 | Yue Yuen | Quartr AI summary, SGI Europe, World Footwear | PARTIAL / BLOCKED (SGI 405); no call transcript found for the Aug 2026 call |
| 7 | Pou Chen | Fugle memos Mar 27 and Jun 5 2026 | WORKED; Sep 2026 call memo not found (404 on guessed URLs, no search hit) |
| 8 | Shenzhou | 10jqka and Gelonghui broker summaries | WORKED (opinion only); HKEX interim not opened |
| 9 | Huali | Gelonghui (CSC), 10jqka investor-survey records | WORKED |
| 10 | Lai Yih, Chih Chiang, Eclat, Makalot, Fulgent Sun | udn, ctee, Uanalyze, chinatimes, Fugle | WORKED; Lai Yih and Fulgent Sun conference decks not located (MOPS foreign-company page blocked in prior pass) |
| 11 | Chang Shin, Taekwang | Korean-language search (Chang Shin INC, 태광실업), English/Vietnamese search, Nike manufacturing map worker counts, sustainabilityreports.com, Vietstock | BLOCKED / EMPTY for orders. Chang Shin (Busan) and Taekwang are private; no DART periodic filings found; only worker snapshot (Chang Shin 39,268 Vietnam workers, Nike map) |
| 12 | Nien Hsing, Ruentex | Chinese search | EMPTY: denim/textile makers with no Nike line found; not a Nike supplier by any source opened. Ruled out as irrelevant |
| 13 | Materials | FENC, Formosa Taffeta, Taiwan Chemical Fiber, Kuang Hsing, Toray searches | EMPTY for Nike orders; they quote adidas and World Cup only. Toray: nothing found |
| 14 | Name clean-up | Fulgent Sun is 9802 (鈺齊-KY, On is #1 customer), Makalot is 1477 (聚陽, Gap/Target/Fast Retailing/Dick's/Kohl's, no Nike), Eclat is 1476 (儒鴻). The task's "Fulgent Sun (1477?)" is Makalot | Corrected |

Only 3 genuinely distinct routes failed for Korea (no filings, no press, no worker data trends); the Korean question is not closed by the 5-route standard. See next section.

## 8. What I could not get, and what would settle it

- **Conference-call transcripts or video** for Feng Tay (Mar, Jun, Sep 2026), Pou Chen (Sep 2026 Q2 call) and Yue Yuen (Aug 2026 call). The Sep 8 2026 Feng Tay paraphrase is analyst-written. Source: Feng Tay YouTube/IR video, MOPS "法說會" attachments (mops.twse.com.tw, 公開資訊觀測站 > 法人說明會), Fugle premium. Not obtainable through the search tools used here.
- **Korean data.** Chang Shin (Changshin INC) and Taekwang (Taekwang Industrial / TKG Taekwang Vina) are unlisted; DART audit reports (外部감사) for Taekwang Industrial or Chang Shin Vina may exist; Vietnamese Ministry of Planning and Investment or Dong Nai/Binh Duong provincial labour data and Vietnamese press (VnExpress, Tuoi Tre) are the next routes. Not done here; W4 (supplier labour) owns this.
- **Lai Yih and Fulgent Sun investor decks** (MOPS foreign-company pages block automated access).
- **Shenzhou and Huali primary filings** (HKEX interim, CNINFO 半年报 text) rather than broker summaries.
- **Nike-only order data.** No supplier discloses Nike orders separately except Feng Tay's customer concentration note. What would decide the open question (deliberate cut vs lower sell-through): Nike's reported wholesale futures and Circana/GfK brand sell-through.
- **Nike next-3-month catalyst.** Feng Tay Oct, Nov and Dec revenue (MOPS, Nov 10, Dec 10, Jan 10) and Pou Chen/Yue Yuen October and November prints; a flip of Feng Tay USD YoY from about -8% to above -3% would be the first supplier-side evidence for the long.

## 9. Corrections and caveats

- The Yahoo/MoneyDJ Dec 2025 article's "50~60萬雙" per month for Salomon in Vietnam is 500k to 600k pairs; one tool extract rendered it as "million". Use 500k to 600k.
- Lai Yih "NT$70.77 billion" Q1 revenue in the udn story is a unit error (repo series gives USD -24.1% for Q1); use the -26.9% YoY the article prints.
- The cnyes 2026-09-10 article calls Pou Chen's H1 2026 net profit a "turn from loss to profit"; this conflicts with other coverage and is not used.
- Two Chih Chiang 2026 shipment estimates conflict (-4.5% vs +10%); both recorded.
- No email address or phone number was placed in any request.
