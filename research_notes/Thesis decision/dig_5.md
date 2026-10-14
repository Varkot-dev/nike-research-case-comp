# Dig 5: Investor Day date, the peer P/E table, and what Berenberg already said

Built 2026-10-14. Scope: three supporting facts for the SHORT thesis in `01_ruling.md`:
(a) the Investor Day date from a primary Nike source; (b) the peer P/E table from one source on one date; (c) the Berenberg Oct 6 Sell at $27.50, and what the pitch adds beyond it.

Labels: **OPENED** = I opened the document in this session and read the line. **SNIPPET** = search-result text only. **REPO** = taken from a repo note and not reopened. **arithmetic** = my calculation. No modeling.

Files: `dig_5_peer_pe_refresh.py` (re-runnable, one source, one run), `dig_5_peer_pe_close_20261013.csv` (output of today's run). Raw PDFs are in the session scratchpad `dig5/dl/` (untrusted data).

---

## 1. Verdict

| Item | Status | One line |
|---|---|---|
| Investor Day Nov 16 to 17 | **Confirmed. Change the citation** | The primary source is Nike's official Q4 FY26 call transcript (Jun 30, 2026, p. 7, Elliott Hill). It is not an SEC filing: EDGAR full-text search finds no "Investor Day" in any Nike filing since Jun 2026. The Oct 1 call (p. 7, 10, 21, 23, 25) says only "November" and does not change the date. The "Oct 1 memo, Nov. 16-17" citation in REPORT.md could not be reopened. |
| Peer P/E table | **Confirmed. Refreshed to Oct 13 close. Final refresh still due about Oct 30** | One source (Yahoo quoteSummary), one run. NKE 27.4x FY27 and 21.5x FY28. Peer medians 15.8x and 13.2x (were 15.5x and 12.9x on Oct 12). The FY2 premium is **63%** (67% on Oct 12). "About 65%" holds. Calendarized to CY2027, the premium is **79%**, so 65% is the conservative figure. |
| Berenberg Oct 6 | **Confirmed in three secondary write-ups. The note itself was not opened (paywalled)** | Hold to Sell, $49 to $27.50, Nick Anderson. The target is 18.1x (adidas's 20-year average P/E) times FY29 EPS. Berenberg already says the valuation premium "looks unjustified", that Nike was "conspicuously silent" on FY27 gross margin, and that China and Sportswear problems persist beyond FY27. So Pillar 1's premium point and part of Pillar 3's timetable point are **not** unique to us. What we add is narrower than the brief assumed. See section 4. |

---

## 2. Investor Day date

| # | Source | What it says | Label |
|---|---|---|---|
| 1 | NIKE, Inc. FY26 Q4 Earnings Release Conference Call Transcript, Jun 30, 2026, "OFFICIAL Transcript FINAL", hosted on Nike's IR file host (s1.q4cdn.com/806093406/files/doc_financials/2026/q4/NIKE-Inc-Q4FY26-OFFICIAL-Transcript_-FINAL.pdf), p. 7, speaker [ELLIOTT HILL] | "Most importantly, we look forward to sharing the next phase of our growth strategy at our Investor Day on November 16 and 17." | **OPENED** |
| 2 | Same transcript, Q&A (Hill) | "we are going to share more of what's to come next at our Investor Day this fall." | **OPENED** |
| 3 | NIKE Q1 FY27 official transcript, Oct 1, 2026 (same host, /2027/q1/NIKE-Inc-Q1FY27-OFFICIAL-Transcript_-FINAL.pdf), p. 7 (Hill) | "At our Investor Day in November, we will provide a clearer view of our long-term growth algorithm..." | **OPENED** |
| 4 | Same, p. 10 (Denton) | "...additional details on these actions, our investment priorities and the measures we will use to assess our progress at our upcoming Investor Day." | **OPENED** |
| 5 | Same, p. 25 (Denton) | "in November, we're going to give you a financial algorithm, so you can begin to assess what not just '27 looks like, but what does the next 5 years begin to look like" | **OPENED** |
| 6 | EDGAR full-text search, CIK 0000320187, "Investor Day", Jan 2025 to Oct 14, 2026 | 0 hits. The same search for "Pace" returns the Oct 1 8-K, the 10-Q and the 10-K, so the index covers these filings. | **OPENED** (search API) |
| 7 | investors.nike.com news page | No Investor Day event listed today. The IR calendar URL returns 404. | **OPENED** |
| 8 | REPORT.md: "At our Investor Day on Nov. 16-17, we'll share more details" (Nike release, Oct 1, 2026 memo) | Not found on Nike's site or in search today. | **REPO**, not reopened |
| 9 | Jefferies via parameter.io (Sep 28), sharedeals.de, Beta Finch | All say Nov 16 to 17. | **SNIPPET** |

**Alternative readings, and how each is ruled out**

- *The date moved after June.* Nike's Oct 1 call refers to "November" five times and gives no new date. No release or report found today mentions a change. This is ruled out as of Oct 14, but the risk is not zero. **Settles it:** a dated webcast listing on investors.nike.com. Check again about Oct 30.
- *The date comes only from secondary sources.* Ruled out. Row 1 is Nike's own transcript, on Nike's IR host.
- *It is a one-day event, or a hybrid with only one investor-facing day.* Not settled. The transcript says "November 16 and 17" and gives no agenda. For the pitch, this matters only because the finals on Nov 19 come two days later.

**Pitch wording:** "Investor Day, Nov 16 to 17 (Nike Q4 FY26 call transcript, p. 7; reaffirmed as 'November' on the Oct 1 call)."

---

## 3. Peer P/E table (one source, one run)

Method: `dig_5_peer_pe_refresh.py`. Yahoo quoteSummary (`price` and `earningsTrend`) in a single run on 2026-10-14. P/E FY1 = last close divided by consensus EPS for the current fiscal year; FY2 uses the next fiscal year. On (price in USD, reports in CHF) and Anta (HKD, reports in CNY) are converted with Yahoo FX from the same run. These are the same peers and method as `thesis_tests/consensus_and_valuation.md` table B3 (REPO). Closes are Oct 13, except ASICS (Oct 14 Tokyo).

| Ticker | Price | FY1 end | P/E FY1 | P/E FY2 | Oct 12 table (B3) FY1 / FY2 |
|---|---|---|---|---|---|
| **NKE** | 35.33 USD | May 2027 | **27.4** | **21.5** | 27.4 / 21.5 |
| ADS.DE | 153.25 EUR | Dec 2026 | 16.8 | 13.2 | 16.4 / 12.9 |
| PUM.DE | 23.41 EUR | Dec 2026 | NM | 88.1 | NM / 87.2 |
| DECK | 84.02 USD | Mar 2027 | 11.2 | 10.0 | 11.2 / 10.1 |
| ONON | 35.49 USD | Dec 2026 | 20.6 | 17.3 | 20.6 / 17.2 |
| LULU | 94.34 USD | Jan 2027 | 9.8 | 10.9 | 9.8 / 11.0 |
| UAA | 4.90 USD | Mar 2027 | 45.3 | 25.3 | 45.5 / 25.5 |
| 7936.T | 4,588 JPY | Dec 2026 | 25.3 | 21.8 | 24.7 / 21.3 |
| 2020.HK | 72.45 HKD | Dec 2026 | 11.9 | 10.9 | 11.7 / 10.7 |
| VFC | 16.07 USD | Mar 2027 | 14.7 | 11.9 | 14.5 / 11.8 |
| **Peer median** | | | **15.8** | **13.2** | 15.5 / 12.9 |

NKE premium on FY2: 21.5 / 13.2 = **+63%** (arithmetic). On FY1: +74%. The Oct 12 figures were +67% and +77%.

**Alternative explanations for the premium, and how each is tested**

1. *Fiscal-year mismatch flatters Nike.* Nike's FY2 ends May 2028. Most peers' FY2 ends Dec 2027. Calendarized, NKE CY2027 EPS = 5/12 x 1.288 + 7/12 x 1.646 = 1.497, so the P/E is **23.6x** and the premium is **79%** (arithmetic). The mismatch makes Nike look *cheaper*, so it cannot explain the premium. Ruled out.
2. *Peer-set choice.* FY2 median by peer set (arithmetic): all 9 peers 13.2x (+63%); without the distressed Puma and Under Armour, 11.9x (+81%); six footwear-led peers 15.25x (+41%); adidas alone 13.2x (+63%); the two fastest growers, On and ASICS, 19.6x (+10%). **The premium survives every peer set except the growers.** Nike trades about in line with On (consensus FY2 revenue +19%) and ASICS (+11%), while Nike's own FY2 consensus revenue growth is +1.1% (B3, REPO). That is a sharper line than "65% above peers".
3. *Trough earnings inflate the P/E, and it is normal for a cyclical low.* This explanation is partly valid, and the pillar already uses it: EV/Sales (1.20 vs 1.18) and EV/EBITDA (11.3 vs 11.6) sit at the peer median (Oct 12, B3, REPO; not refreshed today). Test: even on FY29 consensus EPS of $2.31 (REPO), NKE is at 35.35 / 2.31 = **15.3x**, still above peers' CY2027 median of 13.2x. Two to three years further out, Nike remains more expensive than peers are on next year's earnings. This weakens "it is just a trough", but it does not refute it. The reverse DCF grid (dig 1) is the better answer.
4. *Nike always traded at a premium (10-year forward proxy averaged 33.1x, REPO).* That premium came with 11.8% average EBIT margins and growth. The bear's own anchor is adidas's 20-year average of 18.1x (Berenberg, below), and today's 21.5x FY28 sits above it. Not ruled out as a sentiment argument, but it relies on history the thesis disputes.
5. *Consensus basis mixes GAAP and adjusted EPS (Pace charges).* FY1 consensus of $1.288 sits inside the adjusted guide of $1.15 to $1.35, which excludes about $0.15 of Pace charges. So consensus is effectively on the adjusted basis, and a GAAP basis would make the P/E higher. Ruled out as a source of overstatement.
6. *Single-source error (Yahoo).* Known Yahoo flaws are recorded in B3 (ASICS year-ago revenue, Puma market cap). Neither affects P/E. Lululemon FY2 EPS falls below FY1 (8.64 vs 9.63), which matches a guided decline and is not an error. Not cross-checked against a second vendor because the brief asks for one source. **Settles it:** spot-check adidas and Deckers FY2 EPS on one other vendor during the final refresh.

**Still to do:** re-run `python3 -I dig_5_peer_pe_refresh.py out.csv` on about Oct 30 (the last trading day before the Nov 1 submission) and quote that date. EV/Sales and EV/EBITDA were not refreshed; they need TTM EBITDA and debt from the same run.

---

## 4. Berenberg, Oct 6, 2026

| Fact | Source | Label |
|---|---|---|
| Downgraded Hold to Sell; target $49 to $27.50; analyst Nick Anderson; published premarket Tuesday Oct 6 | finviz/news/399044 (Oct 6, 06:56); parameter.io; Teleborsa via Borsa Italiana (Oct 6, 13:48) | **OPENED** (all three) |
| Target = **18.1x** P/E (adidas's 20-year average) x FY2029 EPS | finviz; parameter.io (method, without the multiple) | **OPENED** |
| Estimate cuts: revenue -6.5% / -11% / -13% (FY27/28/29); EPS -38% / -46% / -34%; FY27 EPS $1.08 | finviz, parameter.io, Teleborsa (all agree) | **OPENED** |
| Quotes: strategy "reads as an admission that market structure has shifted irreversibly against Nike"; "conspicuously silent" on FY27 gross margin; valuation premium "looks unjustified" | finviz | **OPENED** |
| China and Sportswear challenges persist "beyond fiscal 2027"; Pace gives limited support through 2029 | Teleborsa (Italian, translated) | **OPENED** |
| Cites Performance +HSD (running, football, NA basketball, tennis, golf +DD), Sportswear -LDD, Jordan -mid-teens | finviz, parameter.io | **OPENED** |
| One German outlet dates it Oct 5 | search result | **SNIPPET** |
| The Berenberg PDF itself | not available | **NOT OPENED** |

Checks (arithmetic): the Oct 5 close was $33.96 (Yahoo chart, OPENED), so $27.50 is 19.0% below it, matching "about 19% below the last close". That confirms Oct 6 premarket and rules out Oct 5. NKE closed Oct 6 at $34.61 (+1.9%), so the stock rose on the day of the downgrade. Implied Berenberg FY29 EPS = 27.50 / 18.1 = **$1.52**, against consensus of $2.31 (34% below). A 34% cut from about $2.30 also gives $1.52, so the reported numbers are consistent with each other. Berenberg's FY27 EPS of $1.08 is below the adjusted guide's low end ($1.15). It may be on a GAAP basis that includes about $0.15 of Pace charges (1.25 - 0.15 = 1.10). That cannot be settled without the note.

**What the pitch adds, stated honestly**

| Our pillar point | Already in Berenberg's write-ups? | What we add |
|---|---|---|
| P/E premium vs peers (Pillar 1) | **Yes**: premium "looks unjustified" | The reverse-DCF margin grid (dig 1); EV/Sales and EV/EBITDA at the peer median, which shows the whole premium is a margin bet; parity with On and ASICS despite +1% growth. Note that Berenberg's own target uses 18.1x, *above* today's peer FY2 median of 13.2x. At 13.2x, Berenberg's own $1.52 gives about $20 (arithmetic, an illustration, not a target). |
| Guide-implied spread outside China (Pillar 2) | **No.** Berenberg cites FY27 -HSD and China "at least another quarter" but no Q2 to Q4 or ex-GC arithmetic | Q2 to Q4 must fall 7.9% to 10.6% after Q1's -4.3%; NIKE Brand ex-GC falls 3.4% to 7.8% after -0.8% in Q1 (dig 2) |
| Slipping clean-up timetable (Pillar 3) | **Partly.** Teleborsa: problems persist "beyond fiscal 2027" | The *slip itself*: "end of December 2026" (FY26 10-K p. 30, REPO) to "beyond fiscal 2027" (Q1 FY27 10-Q p. 20, REPO) within one quarter; ASP line -30 bps seven quarters after the worst discount quarter |
| Same-shelf markdowns (Pillar 3) | **No** | Running Warehouse 49% of Nike listings marked down vs about 10% for Hoka; Pegasus 41 at 22 of 22 colourways discounted; Foot Locker Jordan retros 21% to 24% off vs 2 of 113 on nike.com (REPO, not reopened here) |
| "Share loss is irreversible" | **Yes, it is Berenberg's headline** | Do **not** use it. Our version is measurable: the decline is spreading on Nike's own guide, and the businesses being rebuilt carry more discount and more demand-creation spend. |

**Alternative explanations for "Berenberg already covers our thesis"**

- *Our thesis is the Berenberg call repackaged.* Partly true on valuation. Not true on the three data points above, based on the three write-ups. **Remaining doubt:** the full note may contain the ex-China or timetable arithmetic. **Settles it:** obtain the PDF (via a university Bloomberg or Refinitiv terminal) and search it for "December 2026", "ex-China" and "markdown".
- *The bear view is consensus, so the short has no edge.* Berenberg is one Sell among about 7 (Yahoo sell plus strong sell, REPO). The median target ($34.40, REPO) is about at the price, and consensus still models FY28 EPS up 28%. Consensus has not adopted the bear view. The stock rose 1.9% on the downgrade day, so the market did not take it on either. This is not ruled out as a crowding risk: short interest is at a record (REPO note 17).

---

## 5. Corrected numbers for the pitch

- Investor Day: cite "Nike Q4 FY26 call transcript, Jun 30, 2026, p. 7". Do not cite an SEC filing; none names the date.
- Peer P/E as of Oct 13 close: NKE 27.4x / 21.5x vs peer medians 15.8x / 13.2x; adidas 16.8x / 13.2x; premium +63% (FY2), +79% calendarized. Re-run about Oct 30.
- Berenberg: Sell, $27.50 (from $49), Oct 6, 2026, 18.1x adidas 20-year average P/E on FY29 EPS (implied about $1.52); FY27 EPS $1.08.
