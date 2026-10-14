# Nike (NYSE: NKE): Final Thesis Memo

**Prepared:** October 14, 2026. **For:** the team, ahead of submission (Nov 1, 2026) and finals (Nov 19, 2026).
**Stock price used:** $35.35 (close Oct 12, 2026) unless a line says otherwise.
**Built from:** the ruling (`01_ruling.md`) and five verification digs (`dig_1.md` to `dig_5.md`) in this folder. Where a dig corrected the ruling, this memo uses the corrected number.

**How to read the source labels.** "Opened" means a teammate or agent opened the primary document and read the figure. "Repo" means the figure comes from a repo note or data file that was re-read, not from a fresh look at the original source. "Our arithmetic" means simple math on cited figures. "Not verified" means we could not open the original.

---

## 1. The thesis and the recommendation

**Recommendation: SHORT.** (Short means we expect the share price to fall, or at least to do worse than peers.)

**The thesis in one sentence:** Nike's fix is real but narrow, yet the stock is priced as if profit margins will climb back to about their 10-year average or better, while Nike's own forecast shows the sales decline spreading beyond China and the repair timetable slipping.

Downside we think is reasonable: about $20 to $26 a share, which is moderate, not a collapse. The $20 end is Berenberg's earnings forecast times the peer average multiple (illustration only, our arithmetic). The $26 end is the team's earlier estimate in the ruling and is not separately verified.

---

## 2. What the market believes, and what we believe instead

**What the market believes.** Nike is near the bottom. China and Converse are temporary problems. Running is growing. Margins will rebuild once old stock is cleared. Analysts already expect FY28 earnings per share to rise about 28%. That is why Nike trades at a much higher price-to-earnings multiple than its peers.

**What we believe instead (our "variant view").** The recovery is real in one place (Performance, mainly running and football) but it is not big enough, or profitable enough, to justify the price.

- The price only makes sense if Nike's operating margin returns to at least its 10-year average (11.8%), and above FY24's 12.7% on stricter assumptions. Today it is 8.3%. Analysts expect 7.2% in FY28.
- Nike's own full-year forecast implies the rest of the year is much worse than Q1, and not only in China.
- Nike quietly dropped its "end of December 2026" date for finishing the clean-up and now says some actions run "beyond fiscal 2027", tied to "higher levels of discounting".

**How this differs from the most visible bear call.** Berenberg (Sell, $27.50, Oct 6) argues that Nike's brand position has "shifted irreversibly". We do not rely on that taste argument. We add four things we did not find in the three Berenberg write-ups we opened: the margin the price requires, the forecast arithmetic outside China, the filing-to-filing timetable change, and same-shelf running prices. (We did not open the Berenberg PDF itself.)

---

## 3. Three reasons

### Reason 1. The price already pays for a full margin recovery.

Nike looks expensive on earnings but normal on sales. That means the entire premium is a bet that margins come back.

| Measure (Yahoo, one pull, Oct 13 close) | Nike | Peer median |
|---|---|---|
| P/E on FY27 earnings (P/E = price divided by earnings per share) | 27.4x | 15.8x |
| P/E on FY28 earnings | 21.5x | 13.2x |
| EV/Sales (company value divided by sales; Oct 12 table, not refreshed) | 1.20x | 1.18x |
| EV/EBITDA (company value divided by operating cash profit; Oct 12 table, not refreshed) | 11.3x | 11.6x |

Source: `dig_5_peer_pe_close_20261013.csv` (opened, Yahoo). The FY28 premium is **63%** over nine peers. It is +41% against six footwear-led peers, +81% if Puma and Under Armour are removed, and only +10% against the fast growers On and ASICS.

**What margin the price needs.** We ran a "reverse DCF". (A DCF values a company from its future cash. A reverse DCF starts from today's price and asks what profit margin the market must be assuming.) WACC is the yearly return investors demand; a higher WACC means a higher bar.

| Required long-run operating margin | at 8% WACC | at 9% WACC | at 10% WACC |
|---|---|---|---|
| Range across growth assumptions | 9.4% to 10.3% | 11.4% to 12.2% | 13.4% to 14.1% |

Compare: FY26 actual 8.3%, FY24 12.7% (FY26 10-K p.30, opened), 10-year average 11.8% (our arithmetic), analyst consensus 5.7% (FY27) and 7.2% (FY28) (repo note, Oct 13). Source: `data/valuation/reverse_dcf.csv`, replicated cell by cell in `dig_1_rdcf_replication.py` (our arithmetic).

**Which WACC is right?** 10% comes from a 20-year Treasury yield of 5.60% plus beta 1.04 times a 5.0% equity risk premium (Kroll's published 5%, PDF opened; beta from our own 5-year regression). 9% comes from Damodaran's lower 4.4% premium. Both are professional choices. We show both. Even at 9%, the price needs the 10-year average margin, 3.5 points above today and on revenue about 15% below FY24 ($43.6B consensus FY28 vs $51.4B).

**A simpler way to say it.** If you buy at $35.35 and sales grow 3% a year, your yearly return depends on where margins settle (our arithmetic, `dig_1.md`):

| Margin settles at | Yearly return to a buyer |
|---|---|
| 12.7% (FY24) | about 9.5% |
| 11.8% (10-year average) | about 9.0% |
| 10% | about 8.1% |
| 8.3% (FY26) | about 7.2% |

The whole US market is priced for about 9.5% (Damodaran, Oct 1). So Nike only offers a market-level return if margins fully recover to FY24. Any shortfall makes it a below-market investment.

**Key numbers:** 21.5x FY28 vs 13.2x peers (63% premium). Required margin 11.4% to 14.1% at 9% to 10% WACC vs 8.3% today and 7.2% FY28 consensus. FY28 revenue about $43.6B vs FY24 $51.4B.

### Reason 2. On Nike's own forecast, the decline is spreading beyond China.

Nike guided FY27 revenue to "decline high-single digits" (Q1 FY27 8-K Exhibit 99.1, opened). We read that as a 7% to 9% fall. The release does not say whether this is reported or currency-neutral. Read as currency-neutral, the reported figure would be about 1 point better. We test both.

**The arithmetic.** FY26 revenue was $46,398M. Q1 FY27 was $11,213M, down 4.3% (Q1 FY27 10-Q p.25, opened). To land at -7% to -9% for the year, Q2 to Q4 must fall **7.9% to 10.6%**, roughly double the Q1 rate (our arithmetic, checked twice).

**Outside China.** NIKE Brand excluding Greater China fell only 0.8% in Q1 ($9,772M vs $9,850M, 10-Q p.25, opened). Even if Greater China falls 26% to 40% for the rest of the year, the guide implies NIKE Brand outside China falls **about 2.6% to 7.8%** in Q2 to Q4 (our arithmetic, `dig_2.md`). Every scenario is worse than Q1. If the guide is really -6% reported, the range is -1.0% to -3.1%, still worse than Q1.

**The growing part is too small.** Management said Performance reached "$16 billion" in FY26 and grew "high single digits" in Q1 (Q1 FY27 call transcript, opened; this was Q1 only, helped by the World Cup, and is not a full-year forecast). If Performance keeps growing 5% to 9%, the other roughly $30B of Nike must fall **about 13% to 18.5%** for the guide to hold (our arithmetic).

**Greater China is mostly lost shoppers, not just a channel choice.**
- Q1 FY27 Greater China revenue fell 26% currency-neutral. Units explain about 25 of the 26 points; price barely moved (10-Q p.28, opened).
- Nike's own stores show it best, because Nike controls them: store sales fell 14% in Q1 FY27 vs North America -6% and EMEA -1%. Comparable store sales fell 7% (FY25) and 6% (FY26) (10-Ks p.40 and p.39, opened).
- adidas grew in Greater China at the same time: +9% (2025) and +15% (Q2 2026), currency-neutral (adidas releases, opened). We cannot prove adidas grew "in the same stores", so we do not claim it.
- Greater China operating profit fell from $2,309M (FY24) to $1,278M (FY26), down 45%. About 83% of that fall is lost volume (10-Ks, opened; our bridge).
- Fair caveat: partners also ran down Nike stock, worth about 1 to 10 points of the Q1 fall. So: "mostly lost sell-through, with deliberate channel cuts on top".
- Next hit: Nike exits partner online sales in China on Jan 1, 2027. We estimate about $743M a year is at risk, about $310M of it in FY27, before Nike's own online stores win any back (estimate, not a Nike figure).

**Key numbers:** Q2 to Q4 implied -7.9% to -10.6% vs Q1 -4.3%. NIKE Brand outside China -2.6% to -7.8% vs Q1 -0.8%. China operating profit $2,309M to $1,278M.

### Reason 3. The repair keeps slipping, and the growth comes with discounts.

**The timetable changed between filings.**
- FY26 10-K p.30 (opened): "we expect to complete these actions by the end of December 2026".
- Q1 FY27 10-Q p.20 (opened): "additional actions related to NIKE Sportswear and Jordan Brand are expected to extend beyond fiscal 2027. The need for these additional actions reflects, in part, higher levels of discounting and broader marketplace pressure."
- Fiscal 2027 ends May 31, 2027. The December date is gone from the 10-Q and the call. To be precise: Nike added new actions rather than formally moving the old date.

**Pricing turned positive, then slipped again.** Nike's gross margin bridge has a line for average selling price (ASP). It was +80 bps in Q3 FY26 (10-Q p.30, opened) and about +258 bps implied in Q4 FY26 (our arithmetic). In Q1 FY27 it was **-30 bps**, "primarily due to higher discounts and channel mix" (10-Q p.23, opened). Higher discounts are named in North America, EMEA and APLA (pp.26, 27, 29). (A bps, or basis point, is 0.01 percentage points.) Caveat: channel mix alone could explain much of the -30 bps, so this is supporting evidence. The stronger evidence is Nike's own sentence linking new actions to discounting.

**Marketing costs more per dollar of sales.** Demand creation (advertising and sponsorship) rose from 8.34% of revenue in FY24 ($4,285M / $51,362M) to **10.25%** in FY26 ($4,754M / $46,398M) (10-Ks, opened). That is about $880M a year more at FY26 revenue. We do not use the Q1 FY27 11.2%, which was World Cup timing.

**Running, the growth engine, sells at a lower price on the same shelf.** At Running Warehouse (a specialist US running retailer, scraped Oct 13, 2026, repo data `runningwarehouse_brand_summary.csv`):
- Median men's road shoe list price: Nike $154.95 vs Hoka $174.95 (Nike about 11% lower).
- Colourways on sale: Nike 49% vs Hoka 9.5% and On 12.5%. Caveat: this falls during the Pegasus 41 to 42 changeover, and Saucony and Brooks are also above 30%.
- nike.com showed 22 of 22 Pegasus 41 colourways discounted (repo test, Oct 2026).

Nike does not disclose margins by category, so we cannot prove Performance earns a lower margin. What we can show is that the growing part is sold at lower prices and with more discounting than its closest rivals.

**Key numbers:** "end of December 2026" to "beyond fiscal 2027". ASP line +80 bps (Q3 FY26) to -30 bps (Q1 FY27). Demand creation 8.34% to 10.25% of revenue. Running shelf price $154.95 vs $174.95; 49% vs 9.5% on sale.

---

## 4. Why the other side is wrong: three strongest objections

**Objection 1: "Nike is a best-in-class brand. Peer multiples do not apply. At its 10-year average margin the stock is fine."**
Answer: That is our point. The price already assumes the 10-year average margin or better. Today's margin is 8.3% and FY28 consensus is 7.2%. Nike would need to add 3.5 to 6 points of margin on about $8B less revenue than FY24. Even on FY29 consensus earnings ($2.31), Nike trades at 15.3x, still above peers' 13.2x on 2027 earnings. And on sales and cash profit (EV/Sales, EV/EBITDA) Nike already trades at the peer median, so the market is not paying a "brand" premium on today's business, only on a recovery.

**Objection 2: "The worst is behind it. North America has grown five quarters, Performance is growing, and stocks this beaten-down usually bounce."**
Answer: We concede North America is growing and running is real. We also show the base rate: deeply fallen large caps have had a median 1-year rebound of +44% to +52% (repo note 20). But Nike's own forecast says Q2 to Q4 will fall 7.9% to 10.6%, and the non-China brand must swing from -0.8% to between -2.6% and -7.8%. Management is telling us the next three quarters are worse, not better. A bounce needs a better outlook, and the outlook went the other way.

**Objection 3: "The short is crowded, you pay a 4.6% dividend, and Berenberg already said all this."**
Answer: We concede the cost and the crowding. The dividend ($1.64 a year) is a real cost and supports the price. But the payout already exceeds earnings: FY27 guided adjusted EPS of $1.15 to $1.35 does not cover $1.64. A freeze or token raise is likely (and mildly positive), which is why we do not make the dividend a pillar. On Berenberg: their case is "taste has shifted irreversibly". Ours rests on Nike's filings and forecast. If the brand recovers taste but margins stall at 9% to 10%, we still win.

Other points we concede openly: consensus already expects FY28 EPS up about 28%; like-for-like North America profit margin is close to its past level (about 26.4% vs 27.2%); and the downside is moderate ($20 to $26), not dramatic.

---

## 5. What would prove us wrong

1. **Investor Day margin target.** A dated long-term operating margin target of **13% or more**, with a year-by-year bridge to get there. That is roughly the bar at a 10% WACC.
2. **A softer re-guide.** If Investor Day narrows FY27 to a mid-single-digit decline (-5% to -6%), the gap outside China mostly disappears.
3. **Pricing turns positive again.** The Q2 FY27 10-Q shows a positive ASP line without "higher discounts" named.
4. **China own-store stabilisation.** Nike-owned store sales in Greater China near flat, or comparable sales disclosed as positive.
5. **Running shelf discounts fall.** Running Warehouse share of Nike colourways on sale drops toward 20% to 25% after the Pegasus changeover.
6. **Interest rates fall sharply.** About 1 point lower in WACC lowers the required margin by about 2 points. The 10-year Treasury was 3.95% at its 52-week low and 5.21% on Oct 13.
7. **A meaningful dividend raise** (above a token amount) in mid-November, which would signal management confidence in cash flow.

---

## 6. Upcoming events that test the thesis

| Date | Event | What to watch |
|---|---|---|
| About Oct 30 | Re-run peer P/E table (`dig_5_peer_pe_refresh.py`) | Is the FY28 premium still about 60%+? Use one source, one date. |
| Nov 1 | Submission deadline | Freeze numbers as of the Oct 30 refresh. |
| Early Nov (date not verified) | adidas Q3 2026 results | Did adidas keep growing in Greater China? If adidas also slowed, China weakness is partly market-wide. |
| Late Oct to mid Nov (dates not verified) | On, ASICS, Deckers (Hoka) results | Do running rivals keep growing at full price? |
| Nov 14 to 20 (usual window) | Nike dividend declaration | Freeze or token raise expected (mildly positive). A large raise works against us. |
| **Nov 16 to 17** | **Nike Investor Day** (date from Nike's Q4 FY26 call, Jun 30, 2026, p.7) | Long-term margin target and date; FY27 re-guide; any China store data; whether the December 2026 clean-up date returns. |
| Nov 19 | Finals | Update the pitch for Investor Day results. |
| About Dec 17 (after finals) | Q2 FY27 results | Q2 revenue vs our -7.9% to -10.6% implied range; ASP line; NIKE Brand outside China. |
| Late Dec 2026 or early Jan 2027 | Q2 FY27 10-Q | The ASP line wording: "higher discounts" named again or not. |
| Jan 1, 2027 | Nike exits partner online sales in China | How much Nike's own online channels win back. |

---

## 7. What we would need to model next (list only)

- A simple revenue bridge for Q2 to Q4 FY27 by segment (Greater China, NIKE Brand outside China, Converse) under the guide.
- Performance vs the rest of Nike: revenue split and growth paths through FY29.
- A margin bridge from 8.3% to the targets: gross margin (pricing, discounts, tariffs, mix), demand creation, overhead.
- China partner-online exit: lost revenue vs recapture by Nike's own online stores.
- Reverse DCF sensitivity to rates (10-year Treasury from 4% to 5.5%).
- Dividend coverage: earnings and free cash flow per share vs $1.64.
- Price target range from peer multiples on FY28 and FY29 earnings scenarios.

---

## 8. Short source list

**Nike primary documents (opened):**
- FY26 Form 10-K: p.30 (timetable quote, margins), p.39 (Greater China EBIT, comps), demand creation.
- FY25 and FY24 Form 10-K: Greater China comps (FY25 p.40), EBIT, demand creation.
- Q1 FY27 Form 10-Q: p.3 (debt, cash), p.20 (timetable), p.23 (ASP line), p.24 (demand creation), p.25 (segments), pp.26 to 29 (regions).
- Q3 FY26 Form 10-Q: p.26 (first "December 2026" date), p.30 (ASP +80 bps).
- Q1 FY27 earnings release, 8-K Exhibit 99.1 (FY27 guide wording).
- Q1 FY27 and Q4 FY26 official call transcripts (Performance $16B quotes; Investor Day Nov 16 to 17 on the Jun 30 call, p.7).

**Other primary sources (opened):** adidas quarterly releases (Greater China growth); Topsports and Pou Sheng HKEX filings (Jul 22, 2026) and Pou Sheng monthly revenue; Treasury.gov yields; Kroll equity risk premium note (Jan 2026); Damodaran implied equity risk premium (Oct 1, 2026).

**Market and analyst data:** Yahoo Finance peer P/E pull, Oct 13 close (opened, `dig_5_peer_pe_close_20261013.csv`); Berenberg Oct 6 downgrade via finviz, parameter.io and Teleborsa (opened; Berenberg PDF not opened).

**Repo data:** `data/valuation/reverse_dcf.csv` (replicated); `data/marketplace/runningwarehouse_brand_summary.csv` (Running Warehouse scrape, Oct 13, 2026); `research_notes/20` (base rates); investigations/02 (Greater China, zealous-mccarthy branch).

**Working notes:** `01_ruling.md`, `dig_1.md` to `dig_5.md` in this folder.
