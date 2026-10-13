# Source re-verification: items earlier research could not open

Research date: 2026-10-13. Scope: every claim in the five note files in this folder and in `reports/Nike decline execution vs structural.md` that was marked snippet only, not opened, blocked, paywalled, 403, 405, 503, timed out or "could not open". The existing notes and report were not edited. This file records what changed.

Status labels used below:
- **NOW OPENED**: I fetched the page and read its text. URL and a short verbatim quote are given.
- **CORRECTED**: the page was opened and the figure, date or attribution in the notes is wrong or incomplete. The right figure is given.
- **STILL BLOCKED**: routes tried are listed. Keep the claim marked snippet only.

## How the retries were done

- **SEC filings.** sec.gov returned HTTP 403 to a User-Agent without a contact address. The `sec-filing-research` skill requires a named contact, none was set in the session (`SEC_USER_AGENT` empty), and I did not put the user's email into a third-party request. I therefore read the Nike FY2026 10-K, the Q1 FY2027 10-Q and the Q4 FY2026 earnings exhibit from Wayback Machine copies of the exact sec.gov URLs (`web.archive.org/web/<timestamp>id_/https://www.sec.gov/...`). The figures match the machine-checked values already in `data/nike_filing_facts.csv`. To re-pull directly from EDGAR, set `SEC_USER_AGENT` and use `scripts/sec_pipeline/dl.py`.
- **HKEX.** The HKEX title-search JSON endpoint (`www1.hkexnews.hk/search/titleSearchServlet.do`) and the PDF links worked. All Chinese-brand and distributor figures below come from the issuers' own HKEX filings.
- **Company IR.** adidas-group.com press releases (it returned 503 earlier) now load. The ASICS FY2025 Japan GAAP summary PDF loads from assets.asics.com.
- **Market data.** Daily closes come from the Yahoo Finance chart API (`query1.finance.yahoo.com/v8/finance/chart/...`). I label these as market data.
- **Still blocked through the proxy:** cnbc.com (403 direct, and the connection is reset through Wayback), ft.com (403), bloomberg.com (403), reuters.com (401), retailtouchpoints.com (403), sgieurope.com (405), retailgazette.co.uk (403), roic.ai (403), benzinga.com (403), invezz.com (403 direct, but readable through Wayback), huxiu.com (timeout and 502), zhihu.com (403), archive.ph (connection reset), Weibo (visitor login wall), Xiaohongshu (JavaScript shell with no content), Handelsblatt search (JavaScript wall). The Wayback availability API returned 429 after a few calls, so I used direct `web/2026id_/URL` requests.

---

## Summary of changes

| # | Claim (as in notes or report) | New status | Change |
|---|---|---|---|
| 1 | Nike FY26 Greater China revenue $5,847M, −13% c-n; segment EBIT not opened | NOW OPENED (10-K p. 39 segment table) | Confirmed. FY26 GC EBIT $1,278M (−20%), GC gross margin 45.7%, wholesale −14% c-n, digital −29% |
| 2 | 10-K "attributes the drop in wholesale revenue primarily to lower revenues in Greater China" | CORRECTED | Total Nike Brand wholesale *rose* 6% (+4% c-n). China was the main *offset* to North America growth, not the cause of a wholesale decline |
| 3 | Huxiu: "FY2026 Greater China revenue plunges 17%" | CORRECTED (via Nike Q4 release) | −17% is Q4 FY26 currency-neutral (Q4 revenue $1,297M, −12% reported). The full year was −11% reported, −13% c-n |
| 4 | Nike ~$986M IEEPA tariff refund; "not probable as of 15 May 2026" | NOW OPENED; second half CORRECTED | $986M ($965M North America, $21M Converse) confirmed, with $302M received in cash by 31 May 2026. The 10-K says recovery was deemed *probable* during Q4 FY26. "Not probable as of 15 May" is not in the 10-K or release; drop it |
| 5 | Adidas Q2 2026 Greater China +15% c-n (adidas-group.com 503) | NOW OPENED | Confirmed; H1 Greater China +16% |
| 6 | Adidas FY2025: ~€24.8bn, +13% c-n, €2.056bn op. profit, 8.3% margin, GM 51.6% | NOW OPENED | Confirmed (€24,811M). Note: +13% is the adidas brand excluding Yeezy; including Yeezy in the base, +10% |
| 7 | Adidas China 2025 +13% to ~US$4.2bn (SCMP 403) | NOW OPENED | Confirmed (SCMP 12 Oct 2026; adidas release confirms +13% c-n) |
| 8 | Bernstein PT $68 vs $80 conflict; "de-risked" call snippet only | NOW OPENED; CORRECTED | Both were true at different dates: $80 (Apr to Jun 2026), $72 (1 Jul), $68 (29 Jul to Sep). After Q1 FY27 Bernstein cut to **$45** (Outperform). Current PT is $45, not $68 or $80 |
| 9 | Williams Trading (Poser) downgrade to Hold, 2 Oct 2026 (CNBC 403) | CONFIRMED via aggregator; CNBC STILL BLOCKED | Buy to Hold on 2 Oct 2026, PT **$57 to $30** (stockanalysis.com). Rationale still not retrieved |
| 10 | Piper Sandler Spring 2025 Nike footwear 49% "conflicts" with series | NOW OPENED; CORRECTED | 49% is confirmed for all teens ("down from 57%"). It does not conflict: series is 61 / 59 / 57 / **49** / 46. The report's advice not to use it should be reversed |
| 11 | Topsports: Nike online ~22% of revenue; FY to Feb 2025 revenue −6.6%, op. profit −42.8%; Q1 FY26/27 low-teens decline | NOW OPENED (HKEX) | All confirmed. Added FY to Feb 2026: revenue RMB 25,739.9M (−4.7%) |
| 12 | Pou Sheng: Nike online ~15% of revenue | NOW OPENED (HKEX) | Confirmed, for calendar 2025, and "its contribution to the Group's profit was insignificant" |
| 13 | Anta 2022 revenue RMB 53.651bn passed Nike China RMB 51.422bn | PARTLY CONFIRMED | Anta RMB 53,651M confirmed (HKEX). The RMB 51.422bn Nike figure has no located source, and the winshang page cited does not contain it. SCMP (opened) dates the crossover to **2021**. The year depends on how fiscal years are matched |
| 14 | Anta H1 2026 ~+12.9%; Li-Ning ~+2.8% | NOW OPENED (HKEX) | Confirmed. Added: Xtep H1 2026 revenue **−0.6%** (core brand −2.2%); 361° +8.0%; Anta brand segment +4.8% |
| 15 | 361° H1 2026 RMB 6.16bn, +8%, net store count −318 | NOW OPENED (HKEX) | Confirmed (5,394 to 5,076 stores) |
| 16 | Anta China share ~23% (2024, Euromonitor) and 21.8% (2025, own) | Both opened; CONFLICT flagged | Anta's 2025 results say 21.8% in 2025 vs **20.8% in 2024**. Primicias quotes Euromonitor at 23% for 2024. Different scopes; cite each with its source |
| 17 | Nike brand share 20.1% (2020) to 16.2% (2024) | STILL UNVERIFIED; likely garbled | Not found anywhere. Euromonitor via Chinanews (opened) gives 2021 **Nike 25.2%, Adidas 14.8%, Anta Group 16.2%, Li-Ning 8.2%**. "16.2%" matches Anta's 2021 share. Do not use the 20.1% to 16.2% series |
| 18 | 2021 Tmall boycott: Adidas −78%, Nike −59%, Li-Ning "more than ninefold", category −11% | NOW OPENED (CGTN, Inverse); CORRECTED | 78% and 59% confirmed (Morningstar, April 2021). The SCMP article cited does *not* contain them. The ">800%" rise was **China Li-Ning** (the premium sub-line), not Li-Ning overall. The −11% category figure was not found |
| 19 | Academy: Jordan in ~145 stores (Apr 2025); "growth engine"; ~200 Jordan shops "later in 2025" | NOW OPENED; date CORRECTED | 145 doors, 23 Apr 2025 confirmed. "Growth engine" and adding 55 shops to reach 200 come from the **Q1 FY2026 call (June 2026)**, not 2025 |
| 20 | Fleet Feet x Nike nationwide partnership, Pegasus 42, from 9 Apr 2026 | NOW OPENED | Confirmed. More than 285 stores |
| 21 | Skechers taken private by 3G, ~$9.4bn, $63/share, delisted 12 Sep 2025 | NOW OPENED | Confirmed ($9.42bn, $63). "About 40% from China" not confirmed: Reuters says only that China is "a bulk of imports" |
| 22 | McKinsey Sporting Goods 2025: incumbents lost ~3 pts 2019 to 2024 | NOW OPENED (Wayback) | Confirmed: Nike and Adidas combined share 27% (2019), 26% (2022), 24% (2024), source Euromonitor; growth ~6% a year 2024 to 2029 |
| 23 | FT interview with Hill ("underestimated") | PARTLY CONFIRMED; FT STILL BLOCKED | stock3 (22 Jun 2026) paraphrases the FT: more work than he realized when he took over, and the road is longer than hoped. The word "underestimated" is not verified |
| 24 | Asics FY2025 ¥810.9bn, +19.5%, 17.6% margin | NOW OPENED (primary PDF) | Confirmed |
| 25 | New Balance 2025 $9.2bn, +19% | NOW OPENED | Confirmed (company-reported, unaudited) |
| 26 | Nike China online sales −36% "latest quarter" | CORRECTED | Nike's Q1 FY27 10-Q: Greater China **digital −28%**, stores −14%, wholesale −31%. FY26 digital −29%. −36% not supported |
| 27 | YouGov: Nike leads "in consideration and quality"; Gen X 39.1, Boomers 20.6 | CORRECTED | Nike leads on consideration (36.3%). **Levi's leads on quality** (54.1 vs Nike 47.8). Old Navy leads on value. The Gen X and Boomer Nike scores are not on the page |
| 28 | JD Sports CEO "Nike will be fine" (dated 2025) | CORRECTED | That quote is from **Aug 2024** (Q2 2024 call) |
| 29 | Topsports shares fell "as much as 26.2% to HK$1.41" | Refined with market data | Yahoo: closed HK$1.45 on 22 Jul 2026 (−24.1%), intraday low HK$1.34, then −6.9% on 23 Jul |
| 30 | DKS fell ~30% on 25 Aug 2026 (CNBC 403) | CONFIRMED with market data | Close $124.31, −30.7% (Yahoo). CNBC still blocked |

---

## A. Nike filings (SEC)

### A1. FY2026 10-K Greater China segment table and EBIT
- Original: notes said the 10-K segment table and EBIT could not be opened, and the $5,847M and −13% came from snippets.
- **NOW OPENED**: [Nike FY2026 10-K, Wayback copy of sec.gov](https://web.archive.org/web/20260927181314/https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm), Greater China segment section, printed p. 39 ("2026 FORM 10-K 39"):
  - "TOTAL REVENUES | $ | 5,847 | $ | 6,586 | -11 | % | -13 | %" (FY2024: 7,545)
  - "Sales to Wholesale Customers | $ | 3,255 | $ | 3,699 | -12 | % | -14 | %"; "Sales through NIKE Direct | 2,592 | 2,887 | -10 | % | -12 | %"
  - "Gross margin | 45.7% | 46.0% | -30 bps | 50.2%"
  - "EARNINGS BEFORE INTEREST AND TAXES | $ | 1,278 | $ | 1,602 | -20 | %" (FY2024: 2,309)
  - "NIKE Direct revenues decreased 12% due to declines in digital sales of 29% and declines in store sales of 4%. Comparable store sales decreased 6%."
  - "Unit sales of footwear decreased 14%"
- MD&A outlook quote confirmed verbatim: "We expect negative impacts from Greater China and Converse to continue throughout fiscal 2027."
- Sourcing: "Vietnam, Indonesia and China manufactured approximately 52%, 27% and 16% of total NIKE Brand footwear"; for apparel, China ~12%. Confirmed.
- Number changes: none to revenue. New: EBIT $1,278M (−20%), GC gross margin 45.7%, digital −29%.

### A2. "Attributes the drop in wholesale revenue primarily to lower revenues in Greater China"
- **CORRECTED.** The 10-K says: "NIKE Brand wholesale revenues were $27.5 billion in fiscal 2026 compared to $25.9 billion in fiscal 2025, up 6% on a reported basis and up 4% on a currency-neutral basis. The increase on a currency-neutral basis was driven by higher revenues in North America, primarily offset by lower revenues in Greater China." There was no total wholesale decline. Greater China *wholesale* fell 14% c-n.

### A3. Huxiu "耐克2026财年大中华区营收暴跌17%" ("Nike FY2026 Greater China revenue plunges 17%")
- Huxiu: **STILL BLOCKED** (www.huxiu.com timeout; m.huxiu.com 502; no Wayback copy).
- **Resolved through the primary source**: [Nike Q4 FY26 earnings release, 8-K Ex. 99.1 (Wayback copy)](https://web.archive.org/web/20261004081500/https://www.sec.gov/Archives/edgar/data/320187/000032018726000076/q4fy26exhibit991er.htm): "Greater China ... Total | 1,297 | | 1,476 | | -12 | % | -17 | % | 5,847 | | 6,586 | | -11 | % | -13 | %". The 17% is the Q4 currency-neutral decline. 21jingji (opened, below) confirms: "耐克大中华区第四季度营收12.97亿美元，在报告基础上下降12%" ("Nike Greater China Q4 revenue was $1.297bn, down 12% on a reported basis").

### A4. ~$986M IEEPA tariff refund (Sportico snippet)
- **NOW OPENED** (10-K, Wayback copy): "During the fourth quarter of fiscal 2026, we deemed the recovery of IEEPA tariffs paid to be probable. Accordingly, we recognized a benefit of $986 million in Cost of sales ... for which $965 million and $21 million of the benefit was classified within North America and Converse, respectively ... As of May 31, 2026, we received $302 million and recorded $684 million of outstanding IEEPA tariff receivables ... Subsequent to May 31, 2026, we received substantially all of the remaining IEEPA tariff receivable."
- Q4 release: "The expected recovery of the IEEPA tariffs of $986 million increased gross margin by approximately 900 basis points"; Q4 EPS of $0.72 includes "a $0.52 benefit".
- **CORRECTED**: the notes' "Nike said recovery was 'not probable' as of 15 May 2026" does not appear in the 10-K or the release. Drop it.
- Sportico page now opens ([Sportico](https://www.sportico.com/law/analysis/2026/nike-trump-tariffs-lawsuit-refund-1234899233/)): consumer suit *Dunn v. Nike* in Oregon federal court, class period "from June 1, 2025, through Feb. 24, 2026". SGB ([opened](https://sgbonline.com/nike-sued-by-customers-seeking-refunds-of-tariff-costs/)): "Filed in the U.S. District Court for the District of Oregon on May 8".

### A5. Tariff cost estimate $1.5bn and 9-month gross margin
- Modern Retail **NOW OPENED** ([30 Sep 2025](https://www.modernretail.co/operations/nike-grappling-with-further-fallout-from-tariffs-now-expects-1-5b-in-annualized-costs/)): "it expects $1.5 billion in gross incremental costs, on an annualized basis, because of tariffs. That's a 50% increase from Nike's last estimate, provided in June, of $1 billion"; Friend: "from approximately 75 basis points to 120 basis points". CFO Dive (opened) agrees.
- The 9M FY26 gross margin of 41.0% (−250 bps) is already machine-checked in `data/nike_filing_facts.csv` (Q3 FY26 10-Q, p. 30: "41.0 | 43.5 | -250 bps"). The "snippet only" label in the report can be upgraded to filing-verified.

### A6. Greater China latest-quarter digital decline (notes: "online sales reportedly −36%")
- **CORRECTED** from the [Q1 FY2027 10-Q (Wayback copy)](https://web.archive.org/web/20261009215024/https://www.sec.gov/Archives/edgar/data/320187/000032018726000193/nke-20260831.htm): "Greater China revenues decreased 26% on a currency-neutral basis. Wholesale revenues decreased 31%. NIKE Direct revenues decreased 18% due to declines in digital sales of 28% and declines in store sales of 14%."

---

## B. Adidas

### B1. Q2 2026 Greater China +15% (adidas-group.com 503)
- **NOW OPENED**: [adidas press release, Q2 2026](https://www.adidas-group.com/en/media/press-releases/adidas-grows-top-line-14percent-and-achieves-record-sales-in-q2): "Currency-neutral net sales grew 15% in Greater China, reflecting continued strong market share gains." H1: "Greater China (+16%)". Q2 revenue "€ 6,743 million (2025: € 5,952 million)"; operating margin 8.5%; H1 operating profit €1,279M, 9.6%. Matches the Deutsche Börse EQS copy in the competitors note.

### B2. FY2025 totals (Retail Sector UK 403, FashionNetwork snippet)
- **NOW OPENED**: [adidas FY2025 results, 4 Mar 2026](https://www.adidas-group.com/en/media/press-releases/adidas-reports-record-revenues-for-2025-and-expects-strong-sales-and-profit-growth-to-continue-over-the-next-years): "13% currency-neutral growth for adidas brand drives record topline of € 24.8 billion"; "Operating profit up 54% to € 2,056 million, operating margin increases 2.6pp to 8.3%"; "gross margin increased 0.8 percentage points to 51.6%"; "Greater China (+13%)"; 2026 outlook "around € 400 million negative impact from US tariffs and unfavorable currency developments"; "operating margin of more than 10% in 2028".
- Preliminary release ([29 Jan 2026](https://www.adidas-group.com/en/media/press-releases/adidas-reports-record-revenues-in-2025-and-launches-share-buyback)): "revenues reached a record level of € 24,811 million (2024: € 23,683 million)".
- Caveat added: the +13% excludes Yeezy from the 2024 base ("Including Yeezy sales in the prior year ... currency-neutral revenues increased 10%").
- Q1 2026 Greater China +17% is also confirmed on the [adidas Q1 release](https://www.adidas-group.com/en/media/press-releases/adidas-records-strong-start-to-the-year-in-the-first-quarter-of-2026): "Greater China (+17%)". The "12th consecutive quarter" wording comes from Jing Daily, not adidas.

### B3. Adidas China 2025 ~US$4.2bn, Gulden on outdoor and street dance (SCMP 403)
- **NOW OPENED** via Wayback: [SCMP, Daniel Ren, 12 Oct 2026](https://www.scmp.com/business/china-business/article/3370520/adidas-ceo-taps-outdoor-sport-street-dance-new-drivers-china-competition-heightens): "reported a 13 per cent year on year sales jump in China last year, which hit US$4.2 billion. In comparison, Nike's revenue in China slumped 12 per cent to US$5.85 billion." Gulden: "We see that there's a running boom and an outdoor boom [in China]".
- The same article says: "Anta Sports leapfrogged Nike to become the largest sportswear company in China by sales in 2021." See C4.
- Minor: SCMP's "slumped 12 per cent" for Nike differs from the 10-K's −11% reported, −13% c-n.

### B4. Adidas 2023 to 2024 trajectory and the €500m guide (RetailDetail, Paperjam, BusinessDay snippets)
- Paperjam **NOW OPENED** ([link](https://en.paperjam.lu/article/adidas-revenue-increased-11)): Gulden: "improved our operating profit by more than €1bn to €1.337bn"; "the phase-out of the Yeezy inventory, which contributed €200m to operating profit in 2024".
- BusinessDay **NOW OPENED** ([1 Feb 2024](https://www.businessday.co.za/bd/companies/2024-02-01-adidas-shares-fall-after-disappointing-2024-forecast/)): "Adidas forecast 2024 operating profit of about €500m versus a €1.294bn consensus".
- RetailDetail opened. It confirms the Yeezy sell-off narrative but not the €268m 2023 operating profit, which remains unconfirmed on an opened page.

### B5. German press (Börsen-Zeitung)
- "Der Fehler von Nike" **NOW OPENED** ([Börsen-Zeitung](https://www.boersen-zeitung.de/meinung-analyse/nike-adidas-handel), mid-2024): "Dass Nike den Fachhandel vernachlässigt hat, rächt sich. Auch ein Adidas-Chef hatte diesen Fehler schon mal gemacht." ("Nike's neglect of specialist retail is taking its revenge. An Adidas boss once made the same mistake.") It compares Donahoe and Rorsted: "Beide sind damit auf die Nase gefallen" ("Both fell flat on their faces"). This confirms the snippet's EXEC reading.
- "Die Aufholjagd von Adidas" **NOW OPENED** ([link](https://www.boersen-zeitung.de/kapitalmaerkte/die-aufholjagd-von-adidas), mid-2023). It is about investor confidence in Gulden, not Nike.
- Handelsblatt, Manager Magazin, FAZ: homepages load, but the Handelsblatt search is behind a JavaScript wall and FAZ redirects. No Nike article was opened. **STILL BLOCKED.** A German-language stand-in that did open is stock3 (see D4).

---

## C. China market

### C1. Topsports (滔搏, 6110.HK)
- **NOW OPENED** (HKEX):
  - [Inside information, 22 Jul 2026](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0722/2026072200069.pdf): "On July 21, 2026 after trading hours, the Group received official notice from Nike that the Group's existing online sales of Nike's products in mainland China will terminate completely with effect from January 1, 2027 ... approximately 22% of the total revenue of the Group for the financial year ended February 28, 2026."
  - [Inside information, 25 Jun 2026](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0625/2026062500521.pdf): at that date the company "has not received any official notice from Nike". This confirms the rumour preceded the notice by about a month.
  - [Q1 FY2026/27 operational update, 25 Jun 2026](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0625/2026062500529.pdf): "the total sales of retail and wholesale operations registered a low-teens decline on a year-on-year basis"; directly operated gross selling area "declined by 11.2% on a year-on-year basis".
  - [Annual results to 28 Feb 2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0521/2025052101059.pdf): Revenue RMB 27,012.9M vs 28,933.2M (−6.6%, derived); operating profit RMB 1,592.7M vs 2,786.5M (−42.8%, derived). This confirms the iTiger snippet.
  - [Annual results to 28 Feb 2026](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0527/2026052701005.pdf): "the Group's revenue decreased by 4.7%, from RMB27,012.9 million ... to RMB25,739.9 million"; principal brands (Nike and Adidas) 86.7% of revenue; wholesale revenue −16.6%.
- Relationship of more than 27 years: Tiger Brokers (opened, [link](https://www.itiger.com/news/1120124157)) says "dates back to 1999".
- Share price (Yahoo market data): 21 Jul close HK$1.91; 22 Jul close HK$1.45 (−24.1%), intraday low HK$1.34; 23 Jul HK$1.35 (−6.9%). The Reuters "as much as 26.2% to HK$1.41" was an intraday reading.
- "Fire sale": BigGo Finance **NOW OPENED** ([link](https://finance.biggo.com/news/22fa2ba7-c30c-4380-8c04-17c5e59ff75c)): ZOOM FLY 6 at ¥599.4 vs ¥999 list on Topsports' mini-program, but "customer service representatives ... responded on July 23 that they had not received any price-cut notifications". Treat as reported, not confirmed.
- Bamboo Works: **STILL BLOCKED** (403; Wayback 404). It is no longer needed, because the HKEX filings cover it.

### C2. Pou Sheng (宝胜, 3813.HK)
- **NOW OPENED**: [Voluntary announcement, 22 Jul 2026](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0722/2026072200197.pdf): "For the year ended December 31, 2025, the revenue contribution from online sales of Nike's products accounted for approximately 15% of the total revenue of the Group while its contribution to the Group's profit was insignificant."

### C3. Channel-change details still at snippet level
- Cathy Sparks rebuilding around Tmall, JD, Douyin and the Nike app: now in BigGo (opened): "Starting January 2027, Nike will concentrate all online resources on official flagship stores on Tmall, JD.com, and Douyin, as well as Nike's own website and app". This is a secondary source paraphrasing Sparks' bylined article. The bylined article itself was not opened.
- "About 60% of Nike Greater China revenue flows through distributors": **STILL UNVERIFIED.** It is not on any opened page. The 10-K gives GC wholesale at $3,255M of $5,847M (about 56%, derived), which is the nearest filing figure.
- Retail Gazette (403), SGI Europe (405): **STILL BLOCKED**.
- 36Kr EN, "Nike Terminates Topsports' Online Distribution Rights" **NOW OPENED** ([link](https://eu.36kr.com/en/p/3906210973291648)). It quotes Hill on the Q2 FY26 call: "We have become a casual lifestyle brand competing through price wars in China." Verify that quote against the call transcript before using it.
- Citi (gelonghui) **NOW OPENED** ([格隆汇, 22 Jul 2026](https://m.gelonghui.com/live/2564860)): Citi opened a 30-day positive catalyst watch on Anta and Li-Ning because "耐克将自2027年1月起终止与中国零售商的大部分在线分销业务 ... 预期将导致其未来在华市场份额流失" ("Nike will end most online distribution with Chinese retailers from January 2027 ... expected to cost it future China share"). Buy ratings; PTs HK$108.8 (Anta), HK$22.8 (Li-Ning). The note's "Anta then Li-Ning" ordering is not stated on this page.

### C4. Anta passing Nike China in 2022 (winshang snippet, McKinsey cited)
- Anta 2022 revenue **NOW OPENED** (HKEX, [2022 annual results, 21 Mar 2023](https://www1.hkexnews.hk/listedco/listconews/sehk/2023/0321/2023032100283.pdf)): "Revenue 53,651 49,328 8.8" (RMB M).
- The winshang page cited (news702268) **NOW OPENED** but does **not** contain the RMB 53.651bn vs 51.422bn comparison or McKinsey. It gives an unrelated figure (Anta "年收益 ... 355.1亿元"), so it is not a usable source for the crossover.
- Nike side: Nike Greater China revenue was $7,547M in FY22 (Jun 2021 to May 2022) and $7,248M in FY23 (`data/nike_filing_facts.csv`). At about RMB 6.5 to 7.0 per USD (an approximate derived conversion), that is roughly RMB 48bn to 51bn, below Anta's RMB 53.65bn for 2022.
- **Conflict on the year**: SCMP (opened, 12 Oct 2026) says Anta "leapfrogged Nike ... in 2021". Anta 2021 revenue was RMB 49.3bn. Nike's FY21 Greater China was $8,290M, so a 2021 crossover depends on matching calendar 2021 against Nike's FY22.
- Recommended wording: "By 2022 Anta Group's revenue (RMB 53.7bn) exceeded Nike's Greater China revenue in RMB terms (derived)." Drop the RMB 51.422bn figure and the McKinsey attribution.

### C5. Anta, Li-Ning, Xtep, 361° H1 2026 (HKEX not opened earlier)
- **NOW OPENED** (HKEX):
  - [Anta 2026 interim results, 26 Aug 2026](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0826/2026082600213.pdf): "Revenue increased by 12.9% year on year to RMB43,507 million"; "ANTA segment revenue grew 4.8% year-on-year to RMB17.77 billion".
  - [Li-Ning interim results, 20 Aug 2026](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0820/2026082001445.pdf): "Revenue rose by 2.8% to RMB15,235 million".
  - [Xtep 2026 interim results, 25 Aug 2026](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0825/2026082500235.pdf): "Revenue of the Group amounted to RMB6,794.9 million. Revenue of the core Xtep brand decreased modestly by 2.2% to RMB5,919.9 million" (group −0.6% vs RMB 6,837.6M).
  - [361° 2026 interim results, 18 Aug 2026](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0818/2026081800247.pdf): "Revenue increased from RMB5,704.8 million to RMB6,159.8 million" (+8.0%). Store table: 5,076 at 30 Jun 2026 vs 5,394 (−318). This confirms the SGI Europe snippet.
- New fact for the deck: Xtep's group revenue *fell* in H1 2026, which strengthens the "whole mass market stalling" point.

### C6. Euromonitor shares and the 20.1% to 16.2% series
- Anta's own share figure **NOW OPENED** ([Anta 2025 annual results, 25 Mar 2026](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0325/2026032500245.pdf)): "According to data from a global authoritative institution, ANTA Sports' market share in the Chinese sportswear market climbed to 21.8% (2024: 20.8%)".
- Primicias **NOW OPENED** ([24 Feb 2026](https://www.primicias.ec/economia/sacudon-mercado-mundial-ropa-deportiva-titan-chino-anta-controlara-puma-acecha-nike-adidas-116554/)): "Según datos de Euromonitor International, Anta lidera el mercado chino ... con una cuota que alcanzó el 23% en 2024" ("According to Euromonitor International data, Anta leads the Chinese market ... with a share that reached 23% in 2024"). **Conflict**: 23% (Euromonitor via Primicias) vs 20.8% (Anta's own citation) for 2024.
- Euromonitor 2021 baseline **NOW OPENED** ([Chinanews, 17 Jun 2022](https://www.chinanews.com.cn/cj/2022/06-17/9781846.shtml)): "2021年，耐克和阿迪达斯在中国的市场占有率滑落至40%(耐克25.2%，阿迪达斯14.8%) ... 安踏集团增至16.2%，首次超越阿迪达斯上升至第二位。第四名李宁的市场占有率也上涨至8.2%。" ("In 2021 Nike and Adidas's combined China share slipped to 40% (Nike 25.2%, Adidas 14.8%) ... Anta Group rose to 16.2%, passing Adidas for second place for the first time. Fourth-placed Li-Ning rose to 8.2%.")
- **The Nike 20.1% (2020) to 16.2% (2024) brand-level series remains unlocated.** Two searches found no source. "16.2%" coincides with Anta Group's 2021 Euromonitor share, which suggests a mix-up. Lanjinger (opened, 24 Jul 2026, a self-media column) writes "21.8%对14.6%" (Anta vs, apparently, Nike) with no source. Recommendation: remove the 20.1% to 16.2% series from the scorecard. If a Nike share is needed, use Euromonitor 2021 (25.2%) and label any later figure as unverified.

### C7. 2021 Tmall boycott figures
- **NOW OPENED**: [CGTN, 8 May 2021](https://news.cgtn.com/news/2021-05-08/Adidas-Nike-web-sales-in-China-plunge-amid-boycott-104yI2pP0mQ/share_amp.html): "In April, sales in Adidas and Nike's Tmall stores slumped by 78 percent and 59 percent respectively, according to American financial services firm Morningstar"; "China Lining's sales on Tmall jumped by more than 800 percent in April, Morningstar said." Also [Inverse](https://www.inverse.com/input/style/nike-adidas-china-sales-online-tmall-uyghur-genocide-raw-materials): "fallen 78 percent for Adidas and 59 percent for Nike ... according to a report by Bloomberg."
- **CORRECTED**:
  - The ">ninefold" figure is for **China Li-Ning**, the premium fashion line, not Li-Ning overall.
  - The SCMP article the report cites ([26 Mar 2021, opened via Wayback](https://www.scmp.com/business/companies/article/3127107/anta-li-ning-shares-surge-chinese-consumers-back-domestic-brands)) covers share-price moves (Anta +5.6%, Li-Ning +2.9%) and does **not** contain the Tmall figures. Re-cite to CGTN or Inverse (Morningstar via Bloomberg).
  - The −11% overall Tmall sportswear figure and the "Ivan Su" attribution were not found on an opened page.
- Business Insider NL redirected to its homepage. Bloomberg (BNN amp) returned 502.

### C8. 21jingji 2 Jul 2026 (503 earlier) and the Guangzhou outlet discounts (Huxiu timeout)
- 21jingji **NOW OPENED** ([www version](https://www.21jingji.com/article/20260702/herald/389311293936f26ca7c4ec4a795db190.html)), 贺泓源, 2 Jul 2026:
  - "库存方面，耐克大中华区库存和库存单位数量均下降双位数" ("On inventory, Greater China inventory value and units both fell by double digits")
  - Friend: "我们继续相信，在这个市场，盈利能力将在销售额之前触底" ("We continue to believe that in this market profitability will bottom before sales")
  - "在今年'618'期间，耐克在天猫运动户外品类的排名仅为第三" ("During this year's 618 festival, Nike ranked only third in Tmall's sports and outdoor category")
  - Friend "将于9月4日正式离任" ("will formally leave on September 4"), which is consistent with Denton as CFO by October
- The Q3 "inventory units down more than 20%" claim is not in this article. **STILL UNVERIFIED.** The 10-K shows GC inventories of $951M (31 May 2025) and $793M (31 May 2026), −17% (derived from `data/nike_filing_facts.csv`).
- Guangzhou outlet (footwear 55 to 70% of list, apparel 60%): Huxiu **STILL BLOCKED**. Syndicated pieces opened:
  - [QQ News / 都市快报, 4 Jun 2026](https://news.qq.com/rain/a/20260604A030RC00): "原价899元，几个月后变成429元；奥特莱斯的货架上，堆积如山" ("listed at ¥899, a few months later ¥429; piled up on outlet shelves"). It also confirms management's "频繁的折扣销售，正在严重削弱品牌在市场中的影响力" ("frequent discount selling is seriously weakening the brand's influence in the market").
  - [Lanjinger](https://www.lanjinger.com/d/1781763819409937286): "打五折都没人抢" ("nobody rushes to buy even at 50% off").
  - [winshang 2023](https://m.winshang.com/news717135.html): outlets "低至5.5折清仓" ("clearance down to 45% off"), dated 2023.
  - None gives the Guangzhou-specific 55 to 70% and 60% split. Keep it snippet only.

### C9. Zhihu "耐克说要跟上中国速度，可解药要等到2027年底" ("Nike says it will keep up with China speed, but the cure won't come until end-2027")
- **STILL BLOCKED** (zhihu 403; no Wayback copy). It is a personal opinion piece and low priority.

### C10. Xiaohongshu, Weibo, Caixin, LatePost
- Weibo search redirects to the Sina visitor login. Xiaohongshu returns a JavaScript shell with no posts. Caixin Global search returns 404. LatePost connection failed. **STILL BLOCKED.** The Weibo trending topic ("原价899的耐克降至429，消费者仍不买账", "Nike at ¥899 cut to ¥429, consumers still not buying") is documented second-hand in Lanjinger and Tiger Brokers (both opened).

---

## D. Analysts and consumer data

### D1. Bernstein (Aneesha Sherman): call and PT
- Invezz **NOW OPENED** via Wayback ([2 Oct 2026](https://invezz.com/en-ae/news/2026/10/02/bernstein-says-nike-stock-now-de-risked-buy-on-post-earnings-dip/)): "Bernstein maintained an 'Outperform' rating on NKE shares, with a $45 price target"; guidance anticipates "high-single-digit sales contraction alongside operating margins hovering near 6%"; "rightsizing its wholesale distribution exposure across Greater China".
- PT history **NOW OPENED** ([stockanalysis.com, Aneesha Sherman](https://stockanalysis.com/analysts/aneesha-sherman/), aggregator, read 13 Oct 2026; dates are as the aggregator records them):

  | Date | PT |
  |---|---|
  | 1 Apr 2026 | $85 to $80 |
  | 1 Jul 2026 | $80 to $72 |
  | 29 Jul 2026 | $72 to $68 |
  | 5 Oct 2026 | $68 to $45 |
  | 9 Oct 2026 | $45 reiterated |

- **CORRECTED**: the $68 vs $80 "conflict" is two snapshots of a falling target. The current Bernstein PT is **$45**. Add Bernstein ($68 to $45) to the post-Q1 FY27 table.
- Related: the report's post-earnings PT range of "$19 to $75" uses Jefferies' $75, which was set on 28 Sep 2026 *before* the 1 Oct print. Among post-print targets on opened pages, the highest is $50 (Guggenheim, BTIG). The report should either say "$19 to $50 after the print" or note that the $75 was pre-earnings.

### D2. Williams Trading (Sam Poser) downgrade
- CNBC video: **STILL BLOCKED** (403 direct; Wayback connection reset; X not tried).
- **CONFIRMED via aggregator** ([stockanalysis.com, Sam Poser](https://stockanalysis.com/analysts/sam-poser/), read 13 Oct 2026): 2 Oct 2026 "Downgraded", Buy to Hold, PT $57 to $30. Earlier entries: Upgraded Sell to Buy on 16 Aug 2024 (so "a Buy since 2024" is right); PT $80 to $57 on 1 Apr 2026.
- WWD "On vs. Nike" **NOW OPENED** ([12 Aug 2026](https://wwd.com/footwear-news/shoe-industry-news/nike-on-specialty-retail-competition-1239106007/)): "Williams Trading analyst Sam Poser believes 'On will lose share to Nike over the next six-to-nine months.'"
- Rationale for the downgrade: still not retrieved.

### D3. Piper Sandler Spring 2025
- **NOW OPENED** (lede only, then paywall): [SGI News](https://sginews.com/Content/teen-survey-sees-upstarts-gaining-mindshare.aspx): "Nike remained atop the footwear ranking for all teens at 49%, down from 57% in the ..." It is an all-teens figure from the Spring 2025 survey.
- **CORRECTED**: the figure is consistent with the series (Fall 2024 57%, Spring 2025 49%, Fall 2025 46%). The report's line saying it "conflicts with this series ... should not be used" should be reversed.
- Annual format **NOW OPENED** ([SGB, Apr 2026](https://sgbonline.com/piper-sandlers-taking-stock-with-teens-becomes-an-annual-event/)): "The 2026 annual teen study will arrive in the fall."

### D4. FT interview with Hill (Benzinga 403, FT 403)
- **STILL BLOCKED** (ft.com 403; benzinga.com 403).
- Partial confirmation **NOW OPENED**: [stock3, 22 Jun 2026](https://stock3.com/news/nike-und-der-lange-lauf-zum-turnaround-17127091): "Hill wählt im Interview mit der Financial Times dafür einen Ton, der gleichermaßen kämpferisch aber auch ernüchtert klingt. Die Richtung stimme, sagt der CEO, doch der Weg sei länger als erhofft. Nike habe mehr Arbeit vor sich, als ihm bei seinem Amtsantritt bewusst gewesen sei." ("In the FT interview Hill strikes a tone that is both combative and sobered. The direction is right, the CEO says, but the road is longer than hoped. Nike has more work ahead than he realized when he took office.")
- Use the paraphrase. Do not put "underestimated" in quotation marks until the FT text is read.

### D5. YouGov rankings (Retail Dive snippet)
- **NOW OPENED** ([Retail Dive press release, 11 Mar 2026](https://retaildive.com/press-release/20260311-nike-leads-us-fashion-brand-rankings-as-athletic-and-heritage-brands-domi-1/)): "Nike ranks first overall in consumer consideration, with 36.3%"; "55.4% of Gen Z adults and 53.6% of Millennials"; "Levi's ranks highest in perceived quality with a Quality score of 54.1, ahead of Nike (47.8)"; "Old Navy ranks first for perceived value for money with a Value score of 36.7".
- **CORRECTED**: Nike does not lead on quality. The page has no verbatim "do not think the brand offers comparable value" line. Nike is simply absent from the value top three. Gen X 39.1 and Boomers 20.6 for Nike are not on the page; the page gives Levi's 39.7% for Gen X and Skechers 45.5% for Boomers.

### D6. Other analyst-side items
- investinglive **NOW OPENED** ([link](https://investinglive.com/stocks/nike-beats-q1-profit-estimates-but-sees-fiscal-2027-revenue-falling-high-single-digits/)): "Nike expects fiscal 2027 revenue to decline by a high-single-digit percentage and guided to adjusted earnings per share of $1.15 to $1.35". The premarket price of $31.79 and the −9.6% were not checked.
- roic.ai: **STILL BLOCKED** (403).
- Bloomberg 10 Jun 2026 (RBC "slower than anticipated"): **STILL BLOCKED** (403).
- Front Office Sports (Powell, Oct 2024) **NOW OPENED** ([link](https://frontofficesports.com/article/nike-brand-struggles-but-dominant-market-share-still/)): "I don't think Nike gives up the No. 1 spot, but it wouldn't surprise me if they have a smaller share in the U.S."
- Statista / Rakuten Insight **NOW OPENED** ([link](https://www.statista.com/statistics/372774/chinese-penetration-rate-of-sportswear-brands/)): "According to a survey conducted by Rakuten Insight in August 2025", Nike 64.
- RetailBoss **NOW OPENED** ([link](https://retailboss.co/89-percent-of-chinese-shoppers-preferred-homegrown-brands-over-foreign-brands-fashion-study)): "The survey, conducted in March 2024, reveals that a staggering 89 percent of Chinese consumers now prefer domestic fashion brands over foreign ones."
- Kantar BrandZ Nike rank: SGI Europe **STILL BLOCKED** (405). The brandclickx page opened and lists "69 | Nike | United States | 41,188", but it does not say the ranking is Kantar's. Leave the rank out.

---

## E. Retailers and running

### E1. Academy Sports + Outdoors Jordan shops
- **NOW OPENED**:
  - [SGB, 10 Jun 2025](https://sgbonline.com/exec-academy-ceo-sees-promising-returns-from-improved-nike-allocations-jordan-launch/): "the introduction of Jordan on April 23 to 145 doors and online"; "Academy invested over $7 million into the Jordan brand launch and Nike expansion".
  - [SGB, 9 Jun 2026](https://sgbonline.com/exec-academy-sports-returns-to-positive-comps-sees-gas-prices-restraining-fy-spend/): "Lawrence said Academy plans to add 55 Jordan Brand shops in the second quarter, bringing its total to 200, or about two-thirds of its store base ... Jordan and Nike combined delivered mid-single-digit comp increases in the quarter ... 'We think Nike is a growth engine for us.'"
- **CORRECTED**: the "growth engine" quote, the mid-single-digit comps and the 200-shop plan are from **June 2026** (Q1 FY2026, quarter ended 2 May 2026), not "later in 2025".
- The originally cited chief-merchant interview ([SGB, 12 Jun 2025](https://sgbonline.com/exec-academys-chief-merchant-talks-jordan-launch-nike-success-tariff-disruption/)) opened. It says Jordan launched "in about half of Academy's stores".

### E2. Fleet Feet x Nike, Pegasus 42
- **NOW OPENED**: [Footwear Magazine, 8 Apr 2026](https://footwearmagazine.com/fleet-feet-and-nike-formalize-a-full-nationwide-partnership-built-around-the-pegasus-42/): "moving Nike Running from a limited presence in select doors to a full rollout across Fleet Feet's nationwide network of more than 285 stores"; "available at select Fleet Feet doors and on fleetfeet.com from April 9, 2026".
- [Running Insight, 23 Apr 2026](https://www.runninginsight.com/fleet-feet-and-nike-expand-partnership): "Fleet Feet has finally entered into an 'official vendor partnership' with Nike".
- Note: this accelerates Pointer's January 2026 expectation of Nike in about half of doors by end-2026.

### E3. Vomero and Circana (WWD/FN, earlier paywall redirect)
- **NOW OPENED**:
  - [FN, 14 Aug 2026](https://wwd.com/footwear-news/shoe-industry-news/consumer-spending-trends-running-shoes-1239125374/): Circana: running shoes "with both dollar and unit sales increasing a very 13 percent"; "sport lifestyle footwear showed a decline in the period"; "the U.S. industry will close out 2026 generally flat."
  - [FN, 16 Jan 2026](https://wwd.com/footwear-news/sneaker-news/nike-vomero-search-volume-running-comeback-1238458292/): Jefferies "tracks search results for 154 running franchises"; Vomero most searched in December, Pegasus second; Vomero "had already hit $100 million in sales off the back of the Vomero 18".
  - [FN running comeback](https://wwd.com/footwear-news/shoe-industry-news/nike-running-comeback-retailers-confirm-1237979667/): "The Vomero 18 has become a top-seller for specialty retailers and a $100 million franchise for Nike."

### E4. Dick's Q2 FY26 stock drop (CNBC 403) and Retail TouchPoints (403)
- CNBC and Retail TouchPoints: **STILL BLOCKED**.
- **CONFIRMED with market data** (Yahoo chart API): DKS closed $179.33 on 24 Aug 2026 and $124.31 on 25 Aug 2026 (−30.7%).
- The Q1 FY26 "Fast Break ~250 stores" claim (CNBC snippet) remains unverified.

### E5. JD Sports 2025 "Nike will be fine"
- **NOW OPENED** ([FN via Yahoo](https://finance.yahoo.com/news/jd-sports-ceo-says-nike-181047127.html)): "On the company's second quarter 2025 earnings call on Thursday, JD Sports chief executive officer Régis Schultz told analysts that 'Nike will be fine'". The byline date is "August 22, 2024". "Second quarter 2025" is JD's fiscal year 2025 (year to early 2025), so the remark was made in Aug 2024, not 2025.

---

## F. Competitors and industry

### F1. New Balance 2025
- **NOW OPENED** ([FashionUnited, 19 Feb 2026](https://fashionunited.uk/news/business/new-balance-achieves-9-2-billion-dollars-in-annual-sales/2026021986388)): "recording an annual global sales growth of 19 percent year-over-year, amounting to 9.2 billion dollars"; "fifth consecutive year of double-digit growth"; North America and Europe "up 20 percent and 30 percent". Company-reported; New Balance is private.

### F2. Asics FY2025 (Alchempro 405 earlier)
- **NOW OPENED (primary)**: [ASICS Summary of Consolidated Financial Statements FY2025 (Japan GAAP), 13 Feb 2026](https://assets.asics.com/system/libraries/4124/Summary%20of%20Consolidated%20Financial%20Statements%20For%20the%20Fiscal%20Year%20Ended%20December%2031,%202025%20%28Japan%20GAAP%29.pdf): "December 31, 2025 810,916 19.5 142,519 42.4 139,295 50.4 98,719 54.7" (net sales, operating profit, ordinary profit and net profit in ¥M, with % change).
- Alchempro also now opens ([link](https://www.alchempro.com/news/apparel-news/japan-s-asics-posts-record-profit-as-fy25-operating-margin-hits-17-6--308433-newsdetails.htm)): SportStyle ¥141.3bn (+43.6%), Onitsuka Tiger ¥136.5bn (+43%), Greater China ¥120.5bn (+19.9%), FY26 guide ¥950bn sales and ¥171bn operating profit.
- Nikkei Asia opens, but articles are paywalled after the lede. One opened lede ([31 Dec 2024](https://asia.nikkei.com/business/business-trends/nike-shoes-lose-ground-in-japan-s-hakone-relay-race-as-rivals-rally)): "Nike shoes were once the unquestioned champion of a prominent long-distance relay race held in Japan, but now the brand has ceded ground to rival shoemakers."

### F3. Skechers / 3G
- **NOW OPENED**: [Reuters via Yahoo, 5 May 2025](https://finance.yahoo.com/news/footwear-brand-skechers-taken-private-125913651.html): "agreed to be taken private by 3G Capital for $9.42 billion"; "$63 per Skechers share in cash"; "withdrew its annual results forecast in April and warned of the fallout from President Donald Trump's 145% import tariff on Chinese goods."
- [FashionUnited, 15 Sep 2025](https://fashionunited.com/news/business/skechers-goes-private-3g-capital-completes-acquisition/2025091568201): "Skechers' shares will no longer be traded on the NYSE as of September 12."
- **CORRECTED**: "about 40% of its goods came from China" is not on either page. Reuters says "China accounts for a bulk of imports for the brand's U.S. business."

### F4. McKinsey Sporting Goods 2025
- **NOW OPENED** via Wayback ([McKinsey, 4 Mar 2025](https://www.mckinsey.com/industries/retail/our-insights/sporting-goods-industry-trends)): "the two largest players ceded three percentage points of market share during this period"; "In 2019, large incumbents accounted for 27 percent of the market ... In 2022 ... 26 percent ... By 2024, large incumbents accounted for 24 percent"; source Euromonitor; "growth outlook for 2024 to 2029 is projected at a slightly more modest 6 percent a year"; "44 percent of industry executives are feeling optimistic"; "Eighty-four percent of sporting goods executives expressed concern about the impact of the geopolitical environment".
- Precision fix: the 84% is concern about "the geopolitical environment" generally, of which tariffs are one example.

### F5. Deckers FY2026
- **NOW OPENED** ([FashionUnited, 22 May 2026](https://fashionunited.uk/news/business/hoka-and-ugg-drive-deckers-brands-to-5-47-billion-dollars-in-fy26-net-sales/2026052288200)): "net sales increased 9.8 percent to 5.47 billion dollars"; "Hoka brand increased 15.9 percent to 2.59 billion dollars"; Q4 Hoka "+14.5 percent"; FY2027 "5.86 billion dollars to 5.91 billion dollars. Hoka net sales are expected to increase by a low-double-digit percentage".

### F6. Puma
- HL **NOW OPENED** ([link](https://www.hl.co.uk/news/puma-expects-another-loss-and-cancels-dividend-in-turnaround-drive)): "reported an operating loss of 357.2 million euros in 2025 having made a profit of 548.7 million a year earlier"; 2026 guide "an operating loss of between 50 million and 150 million euros".
- Note the 2024 conflict: €548.7M (HL/Reuters) vs €622M EBIT (Börsen-Zeitung). This is probably a restated or continuing-operations basis. Cite one with its source.
- People Matters **NOW OPENED** ([link](https://www.peoplematters.in/amp/news/workforce-planning/puma-plans-900-more-job-cuts-as-part-of-reset-phase-in-q3-47042)): "around 900 additional jobs ... This decision will bring the total number of layoffs to 1,300, following the 500 job cuts already made earlier this year." So the "1,400" in the notes is 900 + 500, while the article itself says 1,300. Both totals are in circulation.

### F7. Nike FY1998 slump
- TextilWirtschaft **NOW OPENED** (lede, [30 Jun 1998](https://www.textilwirtschaft.de/fashion-management/nike-gewinneinbruch-im-fiskaljahr-1998-27828)): "Der Gewinn sank um 40% auf 479,1 Mill. Dollar (Vorjahr 795,8 Mill. Dollar)" ("Profit fell 40% to $479.1M (prior year $795.8M)"); restructuring charge $129.9M; Knight: "1998 war ein turbulentes Jahr für Nike" ("1998 was a turbulent year for Nike").

### F8. On Holding prior guide "at least 23%"
- Investing.com: **STILL BLOCKED** (403). Not retried on SEC because of the User-Agent issue above. Still unconfirmed.

### F9. Other competitor snippets not retried or still blocked
- Barchart (202, empty body), Modaes (403), Puck (403), Korean Daum (connection reset): **STILL BLOCKED**.
- President Online **NOW OPENED** ([link](https://president.jp/articles/-/113157), a "best of April 2026" roundup): "かつてスニーカーといえばナイキ1強だったが、最近はめっきり数が減った。代わりに台頭しているのが、オンやホカといった新興スニーカーだ" ("Sneakers used to mean Nike alone, but lately there are far fewer. Rising in their place are newer sneaker brands such as On and Hoka"). This confirms the framing. ASICS is not named in the opened excerpt.

---

## G. Items still blocked (keep labelled snippet only)

| Item | Routes tried |
|---|---|
| CNBC: Poser downgrade rationale; DKS Q1 and Q2 FY26 stories | Direct (403), Wayback (connection reset), WebSearch (no transcript). Rating change and stock drop confirmed by other routes |
| FT Hill interview verbatim ("underestimated") | ft.com (403), Benzinga (403), WebSearch; only the stock3 paraphrase opened |
| Huxiu 4846923 and 4864825 | www (timeout), m. (502/none), Wayback (none); content resolved via the Nike release and syndicated copies, except the Guangzhou 55 to 70% figure |
| Nike brand share 20.1% to 16.2% (2020 to 2024) | Two Chinese searches, gelonghui, lanjinger, chinanews; source not found and likely garbled |
| Nike China RMB 51.422bn (2022) and McKinsey attribution | winshang page opened and does not contain it |
| About 60% of Nike GC revenue via distributors | Not on any opened page; use 10-K wholesale share (about 56%, derived) |
| Q3 FY26 China inventory units down more than 20% | 21jingji 2 Jul (opened) does not contain it; Q3 10-Q not opened |
| Tmall 2021 sportswear −11% and "Ivan Su" | CGTN and Inverse opened, figure absent; BNN Bloomberg 502; BI redirect |
| Retail Gazette, SGI Europe (China channel, 361°, Kantar), Retail TouchPoints, roic.ai, Bamboo Works, Bloomberg, Zhihu | 403, 405 or 404 direct and through Wayback |
| On "at least 23%" prior guide | Investing.com 403 |
| Handelsblatt, Manager Magazin, FAZ, Caixin, LatePost, Weibo, Xiaohongshu | JavaScript or login walls, 404 search, or connection failures |
| Kantar BrandZ Nike rank and value | SGI Europe 405; brandclickx opened but does not name Kantar |
| Nike FY26 10-K directly from EDGAR | sec.gov 403 without a contact User-Agent; read through Wayback instead (set `SEC_USER_AGENT` to re-pull) |

## Scratch files

Downloaded pages and PDFs are in the session scratchpad (`.../scratchpad/pages`, `.../scratchpad/hk`), not in the repo, per the `sec-filing-research` skill.
