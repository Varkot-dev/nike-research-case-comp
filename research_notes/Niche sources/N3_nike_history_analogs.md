# N3: Nike's own history as financial case studies (1984-88, FY1994, FY1998-01, FY2017-18, FY2009, FY2020) versus today

Prepared 2026-10-15. Scope: reconstruct each prior Nike episode of lost growth or margin, then ask how long margin recovery took and whether today looks like 1987 or something slower. Cross-company base rates are NOT repeated (see `research_notes/20_base_rates.md`; it notes Nike's 1997 to 2000 drawdown of -64.9% did not meet its 70% rule). Data files: `N3_nike_history_episodes.csv` (one row per episode), `N3_nike_history_annual.csv` (FY1986 to FY2026 annual series).

Source tags: **OPENED** = I read the page or file myself. **SNIPPET** = a search-result or search-inside snippet, or a fetch tool's summary of a page, not the full page. **DERIVED** = my arithmetic, formula shown. Books are labelled "author's account".

EBIT definition used throughout (matches the repo's `ebit_total`, e.g. FY24 $6,539M = 12.73%): income before income taxes plus net interest expense. It includes other income/expense (FX) and restructuring. Per-share and price figures are put on one basis: Yahoo split-adjusted close x16 = the FY96 10-K per-share basis, x8 = FY97 to FY00 10-K basis, x4 = FY08 to FY12 basis, x1 = FY16 onward.

## 1. Headline numbers

| Episode | Revenue peak to trough | EBIT margin peak to trough | Margin back to prior peak? | Stock peak to trough | Trough to new high |
|---|---|---|---|---|---|
| A. 1984-88 (Reebok, layoffs) | FY86 $1,069M to FY87 $877M, -18% | not disclosed; net margin 5.5% to 4.1% | Net margin 8.5% in FY88 (1 year); revenue peak regained FY88 (2 years) | Dec 1982 to Oct 1984, -75.2% | 3.7 years (5.6 from peak) |
| A2. FY1994 | FY93 $3,931M to FY94 $3,790M, -3.6% | 15.78% to 13.35% (-243 bp) | 14.67% by FY97; the 15.78% was never exceeded (FY21 15.54%) | Dec 1992 to Dec 1993, -51.2% | 1.6 years |
| B. FY1998-01 | FY98 $9,553M to FY99 $8,777M, -8.1% | 14.67% (FY97) to 7.46% (FY98), -721 bp | Within 0.6 pt in FY06 (14.07%, 9 years after FY97); exceeded only in FY21 (15.54%, 24 years) | Feb 1997 to Feb 2000, -64.9% | 4.0 years (7.1 from peak) |
| C. FY2017-18 | none (FY17 $34,350M to FY18 $36,397M, +6%) | 14.40% to 12.03% (-237 bp) | FY21 (4 years after FY17) | Nov 2015 to Nov 2016, -26.1% | 1.2 years |
| D. FY2009 (GFC) | FY09 $19,176M to FY10 $19,014M, -0.8% | 13.02% (FY08) to 10.16% (FY09) (3.1 pt is one-time charges) | 13.27% in FY10 (1 year) | Jun 2008 to Mar 2009, -45.0% | 1.0 year |
| E. FY2020 (COVID) | FY19 $39,117M to FY20 $37,403M, -4.4% | 12.40% to 7.96% (-444 bp) | 15.54% in FY21 (1 year) | Jan 2020 to Mar 2020, -40.0% | 0.4 years |
| **Now** | FY24 $51,362M to FY26 $46,398M, -9.7% | **12.73% (FY24) to 8.30% (FY26), -443 bp** | not yet | Nov 2021 to Oct 2, 2026, **-80.9%** | not yet (4.9 years down) |

All EBIT margins DERIVED from 10-K lines (OPENED); stock dates from Yahoo close (market data, data through 2026-10-14; Yahoo's 1986 and 1987 prices match Hoover's printed ranges to the cent, which validates the 1980s series). Price returns exclude dividends.

**Answers.**
1. **How long did margin recovery take?** It depends on the cause, and the data separate the cases cleanly. Shock years (FY09 GFC, FY20 COVID) and the 1987 product hit recovered within 1 to 2 years. Both episodes caused by inventory and cost structure (FY94 and FY98) did not: after FY97's 14.67% the margin took 9 years to get within 0.6 pt and 24 years to exceed. Gross margin came back in 2 years (+342 bp, FY98 to FY00); the part that never came back was selling and administrative expense, which rose from 25.1% of revenue (FY97) to 29.9% (FY06) and 34.7% (FY26).
2. **1987 or slower?** On the numbers, today is not a 1987. Section 7 gives the tests. The 1987 hit was a category-specific share loss (aerobics) at a company with $877M of revenue in a market it could out-grow, and the fix was a product line that was sized at over $100M. Today's revenue per pair is up 22% on flat units versus FY19, the loss is on S&A (+246 bp FY24 to FY26) and gross margin (-165 bp), and the nearest cost-structure analog is FY98, not FY87.
3. **Smoking gun?** No. Two findings change the pitch wording: (a) FY24's 12.7% is not Nike's peak. The series high is FY93 at 15.78%, then FY21 at 15.54%; (b) after the last cost-structure margin break, Nike has never again exceeded its pre-break peak except through the FY21 pandemic-year margin.

## 2. Provenance and routes log (never accept blocked without five routes)

| # | Route | Target | Result |
|---|---|---|---|
| 1 | investors.nike.com mirror, `?year=` filter on the filings list, files named `10-K.txt` / `10-K405.txt` | Nike 10-K FY95 to FY01, FY04 to FY18 | **Worked** (OPENED). Direct guesses of file names failed (404) until the listing page showed the names. |
| 2 | data.sec.gov submissions JSON (no contact header) | filing index back to 1995 | Worked |
| 3 | Yahoo chart API, NKE from 1980-12-02 | stock paths | Worked |
| 4 | SEC XBRL companyfacts | FY08 to FY26 annual lines | Worked (restated for discontinued operations in places; as-filed figures used where noted) |
| 5 | archive.org full-text download: Shoe Dog (`shoe-dog-philip-knight`) | quotes | **Worked** (OPENED). No page numbers in the text file; cited by passage. |
| 6 | archive.org full-text download: Swoosh, Just Do It | quotes | **Blocked** (HTTP 403/401, lending-restricted) |
| 7 | archive.org fulltext inside.php search-inside API (both server hosts) | Swoosh, Katz | **Blocked** ("Item not available") |
| 8 | Open Library search/inside.json | all books | Returned 0 hits for any query (unusable) |
| 9 | archive.org page_production FTS service | Swoosh | Guest session, full-text override false (unusable) |
| 10 | Google Books API v1 | Swoosh, Katz | **Blocked** (HTTP 429, quota 0 per day for keyless) |
| 11 | Google Books `SearchWithinVolume2` JSON on the book page | Swoosh (ids a1IPAQAAMAAJ, 1991 first edition), Katz (3VwfAQAAIAAJ, 1994) | **Worked** (SNIPPET; at most 3 hits per query, about 35 words each, printed page numbers given). All book quotes below come from this route. |
| 12 | nytimes.com direct | 1986-88 articles | **Blocked** (403) |
| 13 | latimes.com (WebFetch), apnews.com (curl), oregonlive.com (curl) | 1986-88 articles | **Blocked** (403 or tool refusal) |
| 14 | upi.com Archives, curl | UPI 1988-07-14 | Blocked by Cloudflare (403); **worked** through WebFetch (SNIPPET, summary text) |
| 15 | Fortune 1987-08-31 "Nike Hits Its Stride" (money.cnn.com) | text | curl 503 repeatedly; archive.fortune.com 400; web.archive.org snapshot fetch refused by egress policy (the Wayback availability API answers but the snapshot cannot be fetched). Only a search-result paraphrase obtained (SNIPPET). |
| 16 | Hoover's company profile mirror (oocities) | FY86 to FY95 revenue, net income, employees, calendar-year price ranges, P/E | Worked (OPENED, secondary source) |
| 17 | Nike 2004 annual report letter page (q4cdn) | 1984 letter and Knight retrospective | Worked (OPENED) |
| 18 | Nike annual reports FY84 to FY87 | primary figures | **Not found online** (Nike's q4cdn archive starts with the 1998 report; EDGAR starts 1995). Routes tried: EDGAR index, investors.nike.com, q4cdn, search. The 1984 to 1987 figures therefore rest on UPI 1988, Hoover and the FY96 10-K history (which starts at FY88). |
| 19 | Web search | all | Budget exhausted mid-task (200 per turn); not worked around. |

What would settle the open items: the Nike FY1985 to FY1987 annual reports (University of Oregon or Oregon Historical Society library; ProQuest Historical Newspapers for the NYT and Oregonian), and NPD or Sporting Goods Intelligence unit data for 1986 to 1988 and 1998 to 2000.

## 3. Episode A: 1984 to 1988 (Reebok overtakes Nike, layoffs, Air Jordan and Air Max)

### 3.1 Financial reconstruction

| Fiscal year (May) | Revenue $M | Net income $M | Net margin | Gross margin | Employees | Tag |
|---|---|---|---|---|---|---|
| FY1984 | 919 (SNIPPET, secondary) | "over $40 million" | about 4.4% (DERIVED, upper bound unknown) | n/a | n/a | SNIPPET |
| FY1986 | 1,069 | 59.2 | 5.5% | n/a | 3,400 | Hoover, UPI |
| FY1987 | 877 | 35.9 | 4.1% | n/a | 3,000 | Hoover, UPI |
| FY1988 | 1,203.4 | 101.7 | 8.5% | 33.2% | 3,450 | 10-K (FY96 10-K selected data), OPENED |
| FY1989 | 1,710.8 | 167.0 | 9.8% | 37.2% | 4,700 | 10-K |
| FY1990 | 2,235.2 | 243.0 | 10.9% | 38.1% | 3,400* | 10-K |

*Hoover prints 3,400 for 1990 and 4,700 for 1989; treat employee counts as approximate.

Net income FY87 fell 39.3% from the FY86 record (DERIVED from $59.2M to $35.9M) while revenue fell 18.0% ($1,069M to $877M). The decline was therefore not only volume: net margin fell 145 bp.

**FY88 net income bridge (DERIVED).** UPI (SNIPPET): FY88 net income $101.7M, up 183% from $35.9M; effective tax rate 38.8% against 51.3%, "attributed mainly to the 1986 federal tax reform". Pretax income FY87 = 35.9 / (1 - 0.513) = $73.7M (8.4% of revenue); FY88 = 101.7 / (1 - 0.388) = $166.2M (13.8%).

| Driver | Pretax $M | After tax at the FY87 51.3% rate $M | Share of the $65.8M increase |
|---|---|---|---|
| Revenue growth at the FY87 pretax margin (+$326.4M x 8.4%) | +27.4 | +13.3 | 20% |
| Pretax margin expansion (+5.4 pt x $1,203.4M) | +65.0 | +31.7 | 48% |
| Lower tax rate (tax reform) | n/a | +20.8 | 32% |
| Total | +92.5 | +65.8 | 100% |

So about 48% of the FY88 profit recovery was pretax margin and 32% was a tax-rate change that does not repeat; only 20% was volume at constant margin. (Pretax-margin drivers cannot be split into gross margin versus opex because Nike's FY87 income statement was not obtained.)

### 3.2 What happened to share, spending and people (authors' accounts)

- Reebok's lead. Strasser and Becklund, *Swoosh*, p. 591 (author's account, SNIPPET): "Reebok was heading toward a 30 percent market share ; Nike was hanging on to 21 percent . In early 1986 , before the analysts made it official , Knight acknowledged to his top men that Reebok was the top athletic footwear company in America."
- Spending was not the cause. Katz, *Just Do It*, p. 107 (author's account, SNIPPET): "In 1986 , when Nike spent over $ 64 million on advertising and Reebok spent less than $ 16 million , Reebok moved up even with Nike in terms of sales , and in 1987 , the R company completely passed Nike by." Arithmetic: Nike outspent Reebok about 4.0 to 1 (64 / 16), so under-spending on marketing is ruled out as the explanation.
- Missed category. The 1998 case study by the University of Utah (secondary, OPENED PDF `nike_case_oct98.pdf`) states Nike "had almost entirely missed" the aerobic shoe market, and Reebok (secondary, WebSearch snippet of an encyclopedia entry) had aerobics at 42% of its 1985 sales. Reebok's own 1987 sales ($1.39 billion per a Reebok timeline, secondary) against Nike's $877M put numbers on the lead.
- Inventory and cost cuts. *Swoosh*, p. 522 (author's account, SNIPPET): "million was cut from a $56 million budget . Over $27 million in old shoes were dumped for as low as $1 a pair . Nike was taking a beating in the press . The stock dropped to 934." (9 3/4 on the pre-splits basis; Yahoo x64 gives 9.9 for April 1985, a match.) *Swoosh*, p. 521: "In February 1984, Nike made more cutbacks, laying off 271 workers at one New England factory and another 26".
- Layoffs. *Swoosh*, prologue p. 2-3 (author's account): "Last year , Nike stock had caromed into the cellar . Four hundred employees lost their jobs . Air Jordan , built around one great basketball player , had brought in over $ 100 million and saved their ass ." Katz, p. 108: "Nothing marks Phil's psyche more than the fact of those layoffs" (said by then-president Dick Donahue). Knight, *Shoe Dog*, final chapter (OPENED, author's account): "Not being a good enough manager to avoid layoffs. Three times in ten years a total of fifteen hundred people. It still haunts." Employees fell 3,400 to 3,000 in FY87 (Hoover), -11.8% (DERIVED).
- Management. Knight was not President from June 1983 to September 1984 (FY97 10-K, OPENED); Woodell held it (*Swoosh*, p. 501, 508). *Swoosh*, p. 550 (SNIPPET): Knight told Woodell "he was taking back the presidency". Katz, p. 108: Knight blames himself for "backing away from hands-on management of the company in the mid 1980s". Opinion, not an explanation by itself: the data show a category miss and a cost base sized for growth.

### 3.3 The product hit in sales terms

| Measure | Value | Source and tag |
|---|---|---|
| Air Jordan sales at the time | "over $ 100 million" | *Swoosh*, p. 3, author's account, SNIPPET |
| Share of FY87 revenue | about 11% ($100M / $877M, a floor, because "over") | DERIVED |
| Royalty trigger | Jordan paid a royalty on all Nike Air basketball shoes "exceeding the 400,000 pairs that had been sold by Nike the prior year" | *Swoosh*, p. 544, SNIPPET |
| Air Max | Max model "had already been sold for delivery to retailers March 1"; "People in the industry were beginning to say Nike was back" | *Swoosh*, p. 630, SNIPPET (the book pairs this with the 1987 Visible Air launch; its index lists Air Max at p. 600, 621, 630, 632) |
| Revenue growth after the trough | FY88 +$326.4M (+37.2%), FY89 +$507.4M (+42.2%), FY90 +$524.4M (+30.6%) | DERIVED from 10-K (OPENED) |
| 1985 shows | "Nike was hot again" after losses in the second and third quarters | *Swoosh*, p. 571, SNIPPET |

What is not available: pairs and average selling price (Nike disclosed neither in the 1980s), so a units versus price split for 1987 cannot be made. What would decide it: the FY87 annual report and NPD data (see section 2, route 18).

### 3.4 Stock

Peak Dec 8, 1982 ($0.4326 Yahoo basis, $6.92 on the FY96 10-K per-share basis); trough Oct 31, 1984 ($0.1074, $1.72), -75.2% over 1.9 years; back above the 1982 peak on Jun 28, 1988: 3.66 years from the trough, 5.56 from the peak. From the trough the price rose 96% in one year, 113% in two and 149% in three (price only). P/E at trough no more than 6.5x (DERIVED: price $1.72 / EPS $0.266, with net income "over $40 million" and 150.6 million shares from the FY96 10-K FY88 average count; an upper bound). P/E at the 1982 peak not obtained (FY82 and FY83 earnings not found). P/E at May 31, 1988: 9.0x and at May 31, 1989: 8.6x (10-K). The stock recovered the same month the FY88 profit recovery was reported.

## 4. Episode A2: FY1994 (a milder precedent)

Revenue -3.6% ($3,931.0M to $3,789.7M; the first decline in the series). EBIT margin 15.78% to 13.35% (-243 bp, DERIVED): gross margin was flat (-1 bp, 39.3% both years) and S&A rose from 23.5% to 25.7% of revenue (+224 bp, deleverage), other expense -18 bp. Inventory fell 20.7% ($593.0M to $470.0M). Revenue regained the peak in FY95 (+25.6% to $4,760.8M). Stock -51.2% in 1.0 year; new high 1.6 years after the trough. P/E at the trough 9.2x on FY93 EPS (11.0x on FY94 EPS) against 18.8x at the peak (DERIVED, FY96 10-K per-share basis). Margin: 14.16% (FY95), 14.51% (FY96), 14.67% (FY97) and then the FY98 break; the FY93 peak of 15.78% was not exceeded in the next 33 years in this series (best: 15.54% in FY21).

## 5. Episode B: FY1998 to FY2001 (Asian crisis, US retail glut, closeouts)

### 5.1 Numbers (all OPENED from 10-Ks on the mirror)

| FY | Revenue $M | Gross margin | S&A % rev | Restructuring $M | EBIT $M | EBIT margin | Net income $M | Inventory $M | Futures at May 31 |
|---|---|---|---|---|---|---|---|---|---|
| 1996 | 6,470.6 | 39.6% | 24.6% | 0 | 938.6 | 14.51% | 553.2 | 931.2 | $3.9B |
| 1997 | 9,186.5 | 40.1% | 25.1% | 0 | 1,347.6 | **14.67%** | 795.8 | 1,338.6 | $4.9B |
| 1998 | 9,553.1 | 36.5% | 27.5% | 129.9 | 713.0 | **7.46%** | 399.6 | 1,396.6 | $4.2B |
| 1999 | 8,776.9 | 37.4% | 27.6% | 45.1 | 790.2 | 9.00% | 451.4 | 1,170.6 | $4.2B |
| 2000 | 8,995.1 | 39.9% | 29.0% | -2.5 | 964.2 | 10.72% | 579.1 | 1,446.0 | $4.3B |
| 2001 | 9,488.8 | 39.0% | 28.3% | -0.1 | 980.1 | 10.33% | 589.7 | 1,424.1 | $4.3B |
| 2002 | 9,893.0 | 39.3% | 28.7% | n/a | 1,051.3 | 10.63% | 668.3 | 1,373.8 | n/a |
| 2004 | 12,253.1 | 42.9% | 30.2% | n/a | 1,475.0 | 12.04% | 945.6 | 1,633.6 | n/a |
| 2006 | 14,954.9 | 44.0% | 29.9% | n/a | 2,104.8 | 14.07% | 1,392.0 | 2,076.7 | n/a |

Net income fell 49.8% FY97 to FY98 while revenue rose 4.0%. Net income regained the FY97 level only in FY04 ($945.6M, DERIVED comparison; FY02 and FY03 were $668.3M and $740.1M before an accounting-change effect). Futures orders fell 14% in the year to May 1998 ($4.9B to $4.2B) and were flat to +2% for three more years while revenue lagged (FY99 -8.1%): futures give no lead warning of the FY99 decline of the size it produced, because the revenue fall came in at-once and close-out channels (10-K cautions that the order mix shifts between futures and at-once orders).

### 5.2 EBIT margin bridge (DERIVED, basis points of revenue)

| Period | EBIT margin | Gross margin | S&A ratio (cost up = negative) | Restructuring | Other/FX |
|---|---|---|---|---|---|
| FY97 to FY98 | 14.67% to 7.46%, **-721** | **-359** | **-239** | **-136** | +13 |
| FY98 to FY00 | 7.46% to 10.72%, **+326** | **+342** | -151 | +139 | -4 |
| FY00 to FY06 | 10.72% to 14.07%, +335 | +412 | -97 | -3 | +23 |
| FY97 to FY06 | 14.67% to 14.07%, **-59** | **+395** | **-487** | 0 | +32 |

Nike's own bridge for the FY98 gross margin (10-K FY98, MD&A): "Significant to this decline were the increased levels of close-out sales at greatly reduced selling prices, and increased levels of inventory reserves against higher close-out inventory levels, particularly in the U.S. and Asia. The combination of these two factors reduced annual margins by more than 200 basis points." Other items named without amounts: stronger US dollar, fixed distribution costs, royalty costs for athlete contracts and R&D. For FY00 (10-K FY00, MD&A) Nike listed three drivers for the +250 bp, in order: higher in-line margins (apparel, equipment), lower closeout volume, and higher margins on closeouts through its outlet-store network.

**Reading.** Gross margin recovered fully in two years (39.9% in FY00 against 40.1% in FY97). The margin did not, because the S&A ratio stepped up from 25.1% to 27.5% in the crisis year and kept rising to 29.0% (FY00) and 29.9% (FY06) as Nike reinvested. By FY06 gross margin was 395 bp above FY97 and S&A was 487 bp higher.

### 5.3 What drove the revenue decline: units, price, region (FY98 to FY99, Nike's own figures)

| Component | $M | Share of the -$776.2M change | Source |
|---|---|---|---|
| US NIKE brand | -415.7 (-8%) | 53.6% | FY99 10-K MD&A |
| Non-US NIKE brand | -341.6 (-8.7%) | 44.0% | same |
| of which Asia Pacific | -409.4 (1,253.9 to 844.5, -32.7%) | 52.7% | FY99 10-K revenue table (DERIVED) |
| of which Europe | +159.7 (+7.6%) | -20.6% | same |
| of which Americas | -91.9 (residual) | 11.8% | DERIVED |
| Other brands (Bauer, Cole Haan etc.) | -18.9 | 2.4% | DERIVED |

US footwear FY98: pairs -3%, average selling price -4%, sales -7% (10-K FY98: "The reduction in sales was primarily attributable to the glut of inventory at retail which reduced customer order volumes and increased order cancellation rates ... close-out sales"). US footwear FY99: sales -7.3%, "a decrease in pairs sold of 6.3% and a decrease in average selling price of 2.6%" (as printed; the product of the two implies an ASP change of about -1.1%, so the printed pair does not reconcile). Category detail FY99: Basketball -30%, Training -26%, Running +3%, Brand Jordan +23%. For contrast the FY97 boom: US footwear +36%, +28% pairs and +6% ASP; Brand Jordan +133% in FY97, +57% in FY98 (10-K).

### 5.4 Alternatives for the FY98 to FY99 slump: tested and ruled in or out

| Candidate cause | Test | Result |
|---|---|---|
| Asian financial crisis | Asia Pacific revenue -32.7% in FY99 and flat in FY98 (10-K), -$409M | **Surviving cause**, 53% of the FY99 dollar decline; FY98 had the 10-K's Korea -29% and Germany -6% reported |
| US retailer inventory glut and Nike closeouts | US footwear pairs and ASP both down; Nike's own gross margin bridge: more than 200 bp from closeouts plus reserves | **Surviving cause** for gross margin (FY98) |
| Cost structure built for 42% growth (FY97) | S&A ratio +239 bp in FY98, S&A dollars +$320M in a year when revenue grew $367M | **Surviving cause** for opex deleverage (10-K FY98: S&A "27.5% of revenues compared to 25.1%") |
| Sweatshop and labor-practice backlash | The FY97 to FY01 10-Ks never mention labor practices as a revenue risk (only the words "adverse publicity" in the forward-looking boilerplate); US decline concentrated by category (Basketball -30%, Training -26%) while Running +3% and Jordan +23%, which a brand-wide boycott would not do | **Cannot be quantified from filings.** The category pattern argues against it as the main driver, and the effect on the unit and price lines is not separable. Knight's account (OPENED, *Shoe Dog*, final chapter, author's account): "I felt that same sense of betrayal when Nike came under attack for conditions in our overseas factories ... Of course my handling of the crisis only made it worse." What would decide: brand-tracking surveys or university-bookstore data from 1998 to 2000 (not obtained) |
| Currency | 10-K FY99: "Had this decrease been measured in dollars constant with that of the prior year, the net decrease would not have been materially different." | Ruled out as the main driver in FY99 (was a gross-margin item in FY98) |
| Hidden price collapse | US footwear ASP -4% (FY98), -2.6% printed (FY99) | Small (explains less than half of the FY98 US footwear decline; units explain the rest) |
| Product cycle (basketball and training down 30% and 26%) | Category figures above | **Still alive.** Cannot be separated from retailer destocking with 10-K data; NPD sell-through for 1998 to 1999 would decide |

### 5.5 Management actions and stock

Knight stayed CEO throughout and added the President title in June 2000 (10-K FY00, OPENED). $129.9M restructuring in the fourth quarter of FY98: 1,208 employees terminated, Asia Pacific headquarters downsized, Japan distribution center downsized, non-strategic endorsement contracts cancelled, Bauer manufacturing exited (Note 13, FY98 10-K). Employees: 22,800 at May 31, 1998 (10-K). FY99 S&A fell by nearly $200M; "Revenues decreased for the first time in five years" (10-K FY99). Closeout sales fell 14% in FY99 against in-line sales -7% (10-K FY99). Knight's own retrospective (Nike 2004 annual report letter, OPENED, opinion): "Between 1998 and 2001, the management that I praised in the '80s had a tough time keeping up with sales, which more than doubled between 1994 and 1997. I expected it to take some time for them to grow into our revenues."

Stock: peak Feb 13, 1997 ($75.75 on the FY97 to FY00 10-K basis), trough Feb 25, 2000 ($26.56), -64.9% over 3.0 years; new high Mar 9, 2004, 4.0 years after the trough and 7.1 after the peak. One year after the trough +85%, three years +70%. P/E: 40.3x at the peak on FY96 EPS $1.88 (28.3x on FY97 EPS $2.68), 16.9x at the trough on FY99 EPS $1.57 (12.8x on FY00 EPS $2.07). Price/EPS decomposition of the -64.9% (DERIVED): EPS FY96 to FY99 -16.5% ($1.88 to $1.57) times multiple -58% (40.3x to 16.9x) = 0.835 x 0.419 = 0.350, which reproduces the 35.1% remaining. About 70% of the drawdown was multiple compression, not earnings.

## 6. Episode C: FY2017 to FY2018 (adidas gains, Consumer Direct Offense)

| Item | FY16 | FY17 | FY18 | Source |
|---|---|---|---|---|
| Revenue $M | 32,376 | 34,350 | 36,397 | 10-K, OPENED |
| Gross margin | 46.2% | 44.6% | 43.8% | 10-K |
| S&A % revenue | 32.3% | 30.8% | 31.6% | 10-K |
| EBIT margin | 14.34% | 14.40% | 12.03% | DERIVED |
| North America revenue $M | n/a | 15,216 | 14,855 (-2.4%) | repo facts |
| Footwear units / ASP contribution | +9% / +6 pts | +7% / +1 pt | +2% / +2 pts | repo `G3_nike_units_asp_annual.csv` (10-K) |
| Jun-Nov futures | n/a | -2% reported, 0% ex-FX; North America -10%; $14.7B vs $15.0B | no total published | FY17 10-K |

**FY17 to FY18 EBIT bridge (DERIVED): -237 bp = gross margin -74, S&A ratio +88 (cost ratio down? no: S&A ratio rose from 30.8% to 31.6%, so -88), other/FX -75.** Check: -74 - 88 - 75 = -237. The FX line is Nike's: "Other expense (income), net changed from $196 million of other income, net for fiscal 2017 to $66 million of other expense, net for fiscal 2018, primarily due to a $287 million net detrimental change in foreign currency conversion" (FY18 10-K MD&A, SNIPPET of the printed sentence). So about one third of the margin drop (75 of 237 bp) was an FX line, a third gross margin, a third S&A.

What this shows: revenue grew, units did not fall, and ASP rose, so "leadership lost" in this episode was not a unit or price problem at the total level; the damage was North America (-2.4%) and a 15% futures drop there one year earlier. Management: no CEO change (Parker). Consumer Direct Offense announced June 2017: "Triple Double" strategy; FY18 overhead included "one-time wage-related costs associated with the Consumer Direct Offense organizational realignment" (FY18 10-K). Futures-order growth was dropped from Nike's disclosure after the FY17 10-K (repo `Smoking gun hunt/G11_disclosure_withdrawal.md`, cycle A; I confirmed no total in the FY18 10-K text). Stock: peak Nov 27, 2015 ($67.17), trough Nov 1, 2016 ($49.62), -26.1%, new high Jan 19, 2018; P/E 31.1x at the peak (FY16 EPS $2.16) and 19.8x at the trough on FY17 EPS $2.51 (23.0x on FY16). Margin: 14.40% regained in FY21 (15.54%), 4 years later, with an FY20 COVID trough of 7.96% in between.

## 7. Others found: FY2009 and FY2020

- **FY2009 (global financial crisis).** Revenue +2.9% in FY09 and -0.8% in FY10. EBIT margin 13.02% to 10.16%, of which $195M restructuring plus $199M goodwill impairment plus $202M intangible impairment = $596M = 3.1 pt of FY09 revenue (DERIVED from the FY10 10-K), so excluding them FY09 was 13.3%. Back to 13.27% in FY10. Futures for Jun-Nov 2009 were -12% (FY09 10-K), then +10% ex-FX for Jun-Nov 2010 (FY10 10-K). Stock -45.0% in 0.76 years; new high 1.0 year after the trough; P/E 10.3x at the trough on FY08 EPS. Recovery was fast because the cause was a one-time charge plus a demand shock, with gross margin flat (-16 bp) and S&A ratio flat (+11 bp).
- **FY2020 (COVID).** EBIT margin 12.40% to 7.96% (-444 bp; gross margin -130 bp, S&A ratio +262 bp), then 15.54% in FY21 (+759 bp; S&A ratio -585 bp on revenue +19%). Inventory $5,622M to $7,367M (+31%) then $6,854M. Stock -40.0%, new high within 0.4 years. Footwear units -8% in FY20 and +11% in FY21 (repo G3 file).

## 8. Compare with today

| Measure | 1987 (A) | FY98 (B) | FY18 (C) | Now (FY24 to FY26) |
|---|---|---|---|---|
| Revenue change | -18% | -8.1% | +6% | -9.7% |
| EBIT margin change | n/a (net margin -145 bp) | -721 bp | -237 bp | -443 bp |
| Gross margin change | n/a | -359 bp | -74 bp | -165 bp |
| S&A ratio change | n/a | +239 bp | +88 bp | +246 bp |
| Units vs price | not disclosed | US footwear pairs -3%, ASP -4% | footwear units +2%, ASP +2 pts | footwear units index 99.9 vs FY19, revenue per pair +22%; ASP contribution -3 (FY25), -1 (FY26) |
| Inventory / revenue | 90 days of COGS (FY88) | 14.6% | 14.5% | 16.2% (FY26) vs 14.6% (FY24) |
| Regional pattern | one category (aerobics), US | Asia -33%, US -8% | North America -2% | China FY26 $5,847M vs $8,290M in FY21 (-29%) |
| Stock drawdown | -75.2% | -64.9% | -26.1% | -80.9% |
| Trailing P/E at trough | at most 6.5x | 16.9x | 19.8x | 16.1x (FY26 EPS $2.10); 16.8x at $35.35 |

Tests against the 1987 template (each from the data above):
1. **Was the loss one category in a growing market?** 1987: yes (aerobics; Reebok's 1986 sales moved even with Nike's while Nike outspent it 4 to 1). Now: no evidence of a single category; footwear units are flat vs FY19 and China is down 29%. Fails.
2. **Did revenue per unit rise while the loss was happening?** 1987: unknown. Now: yes, +22% per pair, so volume is the flat part and the 22% price uplift is partly reversing (ASP contribution -3 then -1).
3. **Was the fix a new line sized as a share of revenue?** 1987: Air Jordan over $100M, 11% of FY87 revenue, followed by +37%, +42%, +31% revenue years. Scale check (DERIVED): +37% on $46.4B would be +$17.2B, against Jordan Brand revenue of $7.0B today. A product line of 1987's relative size does not exist at this scale.
4. **Did margin loss sit in gross margin (fast to fix) or in S&A (slow)?** Today S&A is 246 of the 443 bp since FY24 and 549 bp of the 725 bp since FY21. FY98 shows gross margin returned in 2 years and S&A never did.

**Sensitivity (DERIVED).** At FY26 S&A dollars ($16,114M), restoring the FY24 12.73% EBIT margin needs gross margin back to 44.6% and revenue about $50.0B (+8%); with gross margin stuck at 42.9% it needs about $53.4B (+15%). Each assumes other income/expense stays at its FY24 level (+0.3% of revenue), so revenue needs are approximate.

**Conclusion for the pitch.** Nike's own record says: product-led or shock-led margin losses recovered in 1 to 2 years; cost-structure and inventory-led losses (FY94, FY98) recovered gross margin in 2 years but the EBIT margin stayed 0.6 to 1.1 pt below the old peak for 9+ years. Today's profile (flat units, price gains fading, S&A ratio +549 bp since FY21, inventory at 16.2% of revenue) matches the second type. This does not prove the margin will fail to reach 11% to 14%: FY06 (14.07%) and FY16 to FY17 (14.3% to 14.4%) show 14% was reached twice in 20 years, after 9 and 19 years respectively. It says the reverse-DCF's 11% to 14% by FY2031 requires a recovery faster than FY98's 8-year path to 96% of the peak. The long-side counter (honest): gross margin did recover 342 bp in two years in FY98 to FY00, and the FY09 and FY20 recoveries were 1 year. The 1980s result is the only product-led precedent, and its units-versus-price split cannot be reconstructed.

## 9. What I could not get

- Nike annual reports for FY1984 to FY1987 and contemporary NYT, LA Times, Fortune text (routes 12 to 15 and 18). Consequences: no EBIT margin, gross margin, inventory or futures numbers for 1984 to 1987, and no peak P/E for the 1982 high.
- Verbatim book text beyond Google Books snippets for *Swoosh* and *Just Do It*; all book quotes carry the snippet's ellipses. I did not read *Shoe Dog* for Reebok or Air Jordan sales (it covers mostly 1962 to 1980 and the epilogue).
- Units and ASP for 1986 to 1988 and for the company total in FY98 to FY01 (only US footwear is disclosed).
- The sweatshop effect on revenue (not separable, section 5.4).
- FY85 revenue and net income: I recall $946M and about $45M but did not open a source, so they are excluded.
