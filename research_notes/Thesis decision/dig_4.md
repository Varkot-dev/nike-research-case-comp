# Dig 4: Is the margin repair really slipping?

Date: 2026-10-14. Scope: Pillar 3 of the SHORT ruling (01_ruling.md). Five things to check: (1) the timetable quotes on FY26 10-K p.30 and Q1 FY27 10-Q p.20, word for word; (2) the "NIKE Brand ASP -30 bps" line on Q1 FY27 10-Q p.23; (3) the ASP-line history since Q2 FY25 and the "7 quarters vs 3 to 4 in precedents" comparison; (4) whether the 11.2% demand-creation ratio is World Cup timing; (5) every other explanation for the same data.

No modeling. All arithmetic is mine and marked as such. Scratch files are in the session scratchpad (`w/*.txt` are the filings converted to text with printed page footers kept; `tr/q1p.txt` is the transcript with PDF page numbers).

## Sources opened today

| Source | Used for | Opened? |
|---|---|---|
| FY26 Form 10-K (nke-20260531.htm, sec.gov/Archives/edgar/data/320187/000032018726000088/), downloaded today | Timetable quote p.30; GM bridge p.34; demand creation p.34 | OPENED |
| Q1 FY27 Form 10-Q (nke-20260831.htm, .../000032018726000193/), downloaded today | Timetable p.19 to 20; channel revenue p.22 to 23; GM bridge p.23; S&A p.24; segments p.26 to 29 | OPENED |
| Q3 FY26 10-Q (nke-20260228.htm, .../000032018726000037/) | First appearance of the December 2026 date (p.26); ASP line p.30 | OPENED |
| Q2 FY26 10-Q (nke-20251130.htm), Q1 FY26 10-Q (nke-20250831.htm), FY25 10-K (nke-20250531.htm), Q3 FY25 10-Q (nke-20250228.htm), Q2 FY25 10-Q (nke-20241130.htm), Q1 FY25 10-Q (nke-20240831.htm), FY24 10-K (nke-20240531.htm) | ASP-line history; channel revenue; earlier timetable wording; demand creation wording | OPENED |
| Q1 FY18, Q2 FY18, Q3 FY18, Q1 FY19 10-Qs (.../000032018717000184/, .../000032018718000007/, .../000032018718000041/, .../000032018718000213/) | Precedent ASP lines and the metric definition then | OPENED |
| Q4 FY25 and Q4 FY26 earnings releases, 8-K Ex. 99.1 (.../000032018725000034/, .../000032018726000076/) | Q4 gross margin wording; IEEPA effect | OPENED |
| Q1 FY27 official call transcript, s1.q4cdn.com/806093406/files/doc_financials/2027/q1/NIKE-Inc-Q1FY27-OFFICIAL-Transcript_-FINAL.pdf | Denton and Hill on discounts, World Cup, timing | OPENED (PDF page numbers) |
| data/nike_filing_facts.csv (wonderful-franklin) | Quarterly revenue and demand creation dollars | OPENED (repo); every figure used was cross-checked against the filing text above |
| research_notes/16_full_price_recovery.md (wonderful-franklin) | Precedent table and the earlier reconciliation | OPENED (repo) |

## 1. The timetable quotes, word for word

**FY26 10-K p.30 (filed 2026-07-15), verified:**
> "Our reportable operating segments are at different stages of progress, and we expect to complete these actions by the end of December 2026. The timing of financial impacts has varied and will continue to vary by segment. North America has made the most progress against these actions, while Greater China and Converse will take more time."
> "... We expect negative impacts from Greater China and Converse to continue throughout fiscal 2027."

"These actions" are the three bullets just above it on the same page: Product Management, Marketplace Management ("liquidating inventory through increased markdowns across NIKE Direct, and higher sales returns and discounts with our wholesale partners") and Brand Management.

**Q1 FY27 10-Q p.20 (filed 2026-10-02), verified. The three bullets are on p.19 with the same wording:**
> "Our reportable operating segments are at different stages of progress with respect to these actions. While we have seen progress with certain areas of our business, additional actions related to NIKE Sportswear and Jordan Brand are expected to extend beyond fiscal 2027. The need for these additional actions reflects, in part, higher levels of discounting and broader marketplace pressure experienced in these areas of our business."
> "... The actions related to Converse are expected to continue throughout fiscal 2027 and for Greater China to extend beyond fiscal 2027."

**How the date appeared and went away (filings opened):**

| Filing | Timing language |
|---|---|
| Q1 FY26 10-Q (Oct 2025) | No date. "different stages of progress against these actions ... timing of financial impacts have varied" |
| Q2 FY26 10-Q (Dec 2025) | No date. Adds "North America has made the most progress ... Greater China and Converse will take more time" |
| Q3 FY26 10-Q p.26 (Apr 2026) | **First date:** "we expect to complete these actions by the end of December 2026" |
| FY26 10-K p.30 (Jul 2026) | Date repeated. Greater China and Converse *impacts* "throughout fiscal 2027" |
| Q1 FY27 10-Q p.20 (Oct 2026) | **Date removed.** Sportswear and Jordan "additional actions ... beyond fiscal 2027"; Greater China *actions* "beyond fiscal 2027" |

The word "December" does not appear anywhere in the Q1 FY27 10-Q MD&A (searched). The Q1 FY27 call does not restate a completion date either (searched for "December", "calendar", "complete"). On the call, Denton said the actions "create pressure on reported revenues for the remainder of fiscal '27 and into '28" (transcript p.11), and Hill said the China digital clean-up will "take multiple seasons" (p.5).

**Correction to the pillar wording.** "The clean-up end moved from 'end of December 2026' to 'beyond fiscal 2027'" is close but not literal. The literal facts are: (a) the December 2026 completion date was dropped one quarter after the 10-K repeated it; (b) Nike added "additional actions" for Sportswear and Jordan that run beyond May 2027; (c) for Greater China the wording went from negative *impacts* "throughout fiscal 2027" to *actions* that "extend beyond fiscal 2027". Suggested slide wording: *"In July Nike said the clean-up would be done by December 2026. In October it dropped the date and said new Sportswear and Jordan actions will run past May 2027, needed 'in part' because of 'higher levels of discounting'."*

## 2. The ASP line, word for word (Q1 FY27 10-Q p.23, verified)

> "Consolidated gross margin was 60 basis points higher than the prior year due to: Lower warehousing and logistics costs, increasing gross margin approximately 90 basis points; Favorable changes in net foreign currency exchange rates, including hedges, increasing gross margin approximately 40 basis points; and Lower NIKE Brand product costs, increasing gross margin approximately 10 basis points. This was partially offset by: Higher other costs, primarily due to third-party royalties, decreasing gross margin approximately 40 basis points; **Lower NIKE Brand ASP, decreasing gross margin approximately 30 basis points, primarily due to higher discounts and channel mix, partially offset by strategic pricing**; and Lower gross margin from Converse, decreasing gross margin approximately 10 basis points."

The -30 bps figure and the page are correct. Gross margin rose 60 bps only because of logistics and FX. On the call, Denton described the same quarter as "partially offset by increased discounts as well as channel mix" (transcript p.9) and said, about FY27: "we are taking discounts and resetting the marketplace, which is dampening gross margins over time" (p.18). The FY27 outlook "reflects continued pressure on gross margin" (p.11).

**Regional split (Q1 FY27 10-Q pp.26 to 29, verified).** "Higher discounts" is cited in three of four regions. Greater China and Converse cite *lower* discounts:
- North America (p.26): GM +110 bps. Higher ASP "primarily reflects product mix and strategic pricing, partially offset by higher discounts". Footwear ASP -1 pt "primarily due to channel mix and higher discounts".
- EMEA (p.27): footwear ASP -6 pts "primarily due to channel mix and higher discounts". GM +140 bps on lower product and logistics costs.
- Greater China (p.28): footwear ASP flat "as lower discounts were offset primarily by channel mix".
- APLA (p.29): GM -150 bps "primarily due to lower ASP ... Lower ASP primarily reflects higher discounts and channel mix".
- Converse (p.31): higher ASP from "product mix and lower discounts".

So in Q1 FY27 the discounting is coming from North America, EMEA and APLA, not from China. That fits the 10-Q's Sportswear and Jordan wording.

## 3. ASP-line history since Q2 FY25 (all OPENED, printed page numbers)

| Quarter | NIKE Brand ASP line, bps of GM | Nike's stated cause | Source |
|---|---|---|---|
| Q1 FY25 | +40 | strategic pricing from the prior year, partly offset by channel mix | Q1 FY25 10-Q p.22 |
| **Q2 FY25** | **-330** | higher discounts, product mix, channel mix | Q2 FY25 10-Q p.26 |
| Q3 FY25 | -150 | higher discounts and channel mix | Q3 FY25 10-Q p.28 |
| Q4 FY25 | about -307 implied (range -270 to -344) | not split out; Q4 release: GM -440 bps "primarily due to higher discounts and changes in channel mix" | derived from FY25 10-K p.35 (-180) and 9M FY25 (-140, Q3 FY25 10-Q p.29); my arithmetic, revenue-weighted |
| Q1 FY26 | -250 | higher discounts and channel mix | Q1 FY26 10-Q p.22 |
| Q2 FY26 | -50 | channel mix and higher discounts, partly offset by strategic pricing | Q2 FY26 10-Q p.27 |
| **Q3 FY26** | **+80** | "primarily due to strategic pricing and product mix" (discounts not named) | Q3 FY26 10-Q p.30 |
| Q4 FY26 | about +258 implied (range +179 to +338) | FY26 10-K bridge (p.34) lists no ASP line at all; 9M FY26 was -80 (Q3 FY26 10-Q p.30) | my arithmetic; assumes the full-year line was within ±15 bps because Nike lists items down to 20 bps |
| **Q1 FY27** | **-30** | higher discounts and channel mix, partly offset by strategic pricing | Q1 FY27 10-Q p.23 |

Rough two-year view (adding the two y/y lines is an approximation, my arithmetic): Q2 FY26 about -380, Q3 FY26 about -70, Q4 FY26 about -50, **Q1 FY27 about -280** (-250 then -30). Against the same quarter two years earlier, Q1 FY27 recovered none of the Q1 FY26 liquidation hit.

### The "7 quarters vs 3 to 4 in precedents" claim does not hold as written

1. **The line did turn positive.** Q3 FY26 was +80 and Q4 FY26 was about +258 implied. The accurate statement is "positive for two quarters, then negative again", not "still negative after 7 quarters". The repo's own note 16 already says this in its header.
2. **The "worst quarter" is not clear-cut.** Q2 FY25 is -330 as printed. The implied Q4 FY25 figure of -270 to -344 overlaps it, and Q4 FY25 had the much larger total GM drop (-440 bps, Q4 FY25 release p.1, vs Q2 FY25's -100 bps, Q2 FY25 10-Q p.24). Counting from Q4 FY25, the first positive line (Q3 FY26) came after 3 quarters, which is inside the precedent range. Counting from Q2 FY25 it came after 5.
3. **The metric changed, which makes the precedents unfair to Nike.** Up to FY24 Nike reported "full-price ASP, net of discounts, on a wholesale equivalent basis" (FY24 10-K p.36; Q1 FY19 10-Q p.23), with separate NIKE Direct and off-price lines. "Wholesale equivalent" strips out channel mix. From Q1 FY25 the single "NIKE Brand ASP" line includes channel mix, and Nike is deliberately moving sales from NIKE Direct to wholesale. Today's line is therefore held down by a mix effect that the precedent lines did not contain.
4. **Nike's own precedent includes a relapse.** FY18: Q1 -80 ("higher discounts and product mix"), Q2 +40, Q3 -50 ("primarily due to product mix"), then Q1 FY19 +100 "net of discounts" (Q1 FY18 10-Q p.22; Q2 FY18 10-Q p.24; Q3 FY18 10-Q p.25; Q1 FY19 10-Q p.23). A one-quarter relapse after a positive print happened before and the recovery then held. What is different now: the FY18 relapse was blamed on product mix and came 2 quarters after the trough. This one is blamed on "higher discounts" first, 5 to 7 quarters after the trough, and arrives together with a dropped completion date.

**Suggested slide wording:** *"Price recovery stalled. Nike's ASP line turned positive for two quarters (Q3 and Q4 FY26), then went negative again in Q1 FY27 (-30 bps), with Nike naming 'higher discounts' first. In the same filing Nike dropped its December 2026 completion date."* Do not use "7 quarters vs 3 to 4".

## 4. Is the -30 bps discounts or channel mix? (biggest open alternative)

Nike's channel revenue (filings opened; Direct share = Direct / (Wholesale + Direct), my arithmetic):

| Quarter | Wholesale $M | NIKE Direct $M | Direct share | Change y/y | ASP line |
|---|---|---|---|---|---|
| Q1 FY25 | 6,410 | 4,687 | 42.2% | | +40 |
| Q1 FY26 | 6,839 | 4,514 | 39.8% | -2.4 pts | -250 |
| Q2 FY26 | 7,499 | 4,616 | 38.1% | -3.9 pts | -50 |
| Q3 FY26 | 6,466 | 4,539 | 41.2% | -2.2 pts | +80 |
| Q1 FY27 | 6,804 | 4,142 | 37.8% | -2.0 pts | -30 |

Sources: Q1 FY25 10-Q, Q1 FY26 10-Q, Q2 FY26 10-Q, Q3 FY26 10-Q, Q1 FY27 10-Q p.23 (channel tables).

**Rough size of the mix effect (my arithmetic, a bounding estimate, not a model).** Assume Nike's wholesale price is 50% to 70% of its own retail price for the same item and that product cost is the same in both channels. Then a 2.0-pt fall in Direct share lowers average price per unit enough to cut gross margin by about **40 to 70 bps** on its own. The same method gives about 45 to 80 bps for Q3 FY26 (-2.2 pts).

What this means:
- **Channel mix alone can explain all of the Q1 FY27 -30 bps.** On this estimate, the non-mix parts (discounts, strategic pricing, product mix) netted to roughly +10 to +40 bps. On the same basis they were roughly +125 to +160 bps in Q3 FY26 (my arithmetic).
- So the honest reading is: **the improvement in discounting and pricing narrowed sharply from Q3 FY26 to Q1 FY27, but the bridge alone does not show it turning negative.** The swing from +80 to -30 comes with a *smaller* mix shift (2.0 pts vs 2.2 pts), so mix does not explain the swing. Something in discounts, pricing or product mix got worse by about 110 bps (my arithmetic).
- The mix estimate is crude. It ignores that Direct includes factory stores selling at a discount, that product mix differs by channel, and that the logistics saving from channel mix (+90 bps in Q1 FY27) shows up in a separate line.

**Why "higher discounts" still survives as a real driver (evidence, not inference):**
1. Nike names it first in the consolidated GM bullet ("higher discounts and channel mix"), and the CFO says "increased discounts" (transcript p.9).
2. Three of four regions cite "higher discounts" (pp.26, 27, 29).
3. The 10-Q says the extra Sportswear and Jordan actions are needed "in part" because of "higher levels of discounting" (p.20). That is Nike linking discounting to the slipped timetable in its own words.
4. Denton: "we are taking discounts and resetting the marketplace, which is dampening gross margins over time" (p.18).

**A second confound works against Nike, not for it (my inference).** World Cup kits are high-priced apparel. Q1 FY27 apparel ASP was +4 pts on "product mix and strategic pricing" (10-Q p.23) and Nike "doubled our World Cup team kit sales" (transcript, cited in investigations/01). That lifted the ASP line. Without the tournament, the line was probably weaker than -30. The filings do not size this.

**Strategic pricing is lapping (inference).** Nike's tariff-driven price increases took effect in Q1 FY26 (10-Q wording "partially offset by strategic pricing" begins in Q2 FY26). From Q1 FY27 they start to lap, so the pricing offset is shrinking. This partly explains the swing and is not a sign of demand weakness. Nike still lists strategic pricing as an offset in Q1 FY27, so it has not ended. The filings do not split pricing from discounts. This alternative remains open.

## 5. Demand creation: 11.2% is World Cup timing. Use 10.25%

Ratios (my arithmetic on 10-Q and 10-K dollars):

| Period | Demand creation $M | Revenue $M | % of revenue |
|---|---|---|---|
| FY24 | 4,285 | 51,362 | 8.34% |
| FY25 | 4,689 | 46,309 | 10.13% |
| **FY26** | **4,754** | **46,398** | **10.25%** |
| Q1 FY24 | 1,069 | 12,939 | 8.26% |
| Q1 FY25 (Paris Olympics) | 1,226 | 11,589 | 10.58% |
| Q1 FY26 | 1,188 | 11,720 | 10.14% |
| **Q1 FY27 (World Cup)** | **1,252** | **11,213** | **11.17%** |

Evidence it is event timing (all OPENED):
- Q1 FY27 10-Q p.24: demand creation "increased 5% primarily due to higher brand marketing expense, reflecting higher investment in key sports events."
- By segment: North America +16% ($442M to $511M) "reflecting higher investment in key sports events" (p.26); Global Brand Divisions +14% ($203M to $232M). EMEA flat, Greater China -11%, APLA -4%, Converse -58%. The tournament was hosted in North America.
- Denton: "increasing investments in demand creation associated with the World Cup" (transcript p.9).
- Same pattern last time: Q1 FY25 demand creation +15% "reflecting investment in key sports events" (Q1 FY25 10-Q p.23), then Q1 FY26 -3% "primarily due to higher investment in key sports events in the prior year" (Q1 FY26 10-Q p.23).
- Taking out the whole North America and Global Brand Divisions increase ($98M) leaves 10.29% for Q1 FY27, almost exactly FY26's 10.25% (my arithmetic).

**Corrected figure for Pillar 3: demand creation went from 8.3% of revenue (FY24) to 10.25% (FY26), +1.9 pts, about $880M a year at FY26 revenue (my arithmetic).** About half of that rise is higher spending ($4,285M to $4,754M, +11%). The other half is the smaller revenue base: FY26 spending on FY24 revenue would be 9.26% (my arithmetic). Do not use 11.2%. A comparison of 8.3% (a full year) with 11.2% (one event quarter) is not like for like and a judge can take it apart.

## 6. Alternative explanations: ruled out, and still open

| # | Alternative | Verdict | Evidence / what would settle it |
|---|---|---|---|
| A1 | The timetable did not slip. The December date covered the original actions, which are on track, and the Sportswear and Jordan work is new scope | **Partly survives** | Against it: the date was dropped completely, Greater China moved from "impacts throughout FY27" to "actions beyond FY27", and Nike says the new actions are needed because of "higher levels of discounting". For it: the 10-Q says "additional actions" and "we have seen progress". **Settles it:** Investor Day (Nov 16 to 17) or the Q2 FY27 call (about Dec 17) saying whether the original Win Now actions finished in December |
| A2 | The -30 bps is the deliberate channel shift, not discounting | **Survives for the level; ruled out for the swing** | Mix of 40 to 70 bps can explain the whole -30 (my estimate). But the mix shift in Q1 FY27 (-2.0 pts) was smaller than in Q3 FY26 (-2.2 pts, ASP +80), so mix does not explain the +80 to -30 swing. **Settles it:** Nike disclosing full-price share or ASP by channel |
| A3 | The swing is strategic pricing lapping, not new discounting | **Open** | Nike still lists pricing as an offset; the filings do not size it. **Settles it:** the Q2 FY27 10-Q wording (whether "strategic pricing" disappears as an offset and "higher discounts" stays) |
| A4 | Greater China clearance drives the ASP drag | **Ruled out** | Greater China cites *lower* discounts (10-Q p.28). The drag comes from NA, EMEA and APLA (pp.26, 27, 29) |
| A5 | -30 bps is noise; GM rose 60 bps | **Partly survives** | The size is small. The direction is backed by Nike's words (pp.20, 23; transcript pp.9, 11, 18) and the FY27 outlook of "continued pressure on gross margin". On its own the figure is weak, so present it with the quotes |
| A6 | One relapse quarter is normal; FY18 also relapsed and then recovered | **Partly survives** | True (Q3 FY18 -50 between +40 and +100). The difference: FY18's relapse was product mix and came 2 quarters after the trough, with no timetable change. This one names discounts first, comes 5 to 7 quarters after the trough, and arrives with a dropped date. **Settles it:** Q2 FY27 ASP line. Positive with discounts not named weakens the pillar; negative with "higher discounts" confirms it |
| A7 | The 11.2% demand-creation ratio shows structural over-spending | **Ruled out as stated** | It is World Cup timing (10-Q p.24, segment detail, transcript p.9, Olympics precedent). The structural rise is 8.3% to 10.25% |
| A8 | Demand creation went up only because revenue fell | **Partly survives** | About half the 1.9-pt rise is the smaller revenue base (my arithmetic). Spending is still up 11% in dollars from FY24 |
| A9 | World Cup kits flatter the Q1 FY27 ASP line | **Likely, against Nike** | Apparel ASP +4 pts on product mix (10-Q p.23). Not sized in filings |

## 7. Bottom line for Pillar 3

**Status: confirmed with changes.** Nike's own filings and call support "the repair keeps slipping", but three figures in the pillar need fixing:
1. Replace "ASP line negative 7 quarters after the worst quarter, vs 3 to 4 in precedents" with "positive for two quarters, then negative again in Q1 FY27 (-30 bps, 'higher discounts' named first)". The precedent comparison is flawed: the line did turn positive, the trough quarter is ambiguous, and the metric changed in FY25.
2. Present the timetable change literally: the December 2026 date was dropped and "additional actions" for Sportswear and Jordan now run "beyond fiscal 2027", "in part" because of "higher levels of discounting" (Q1 FY27 10-Q p.20, compared with FY26 10-K p.30).
3. Demand creation: use 8.3% (FY24) to 10.25% (FY26), not 11.2%. The 11.2% is World Cup timing.

The strongest single piece of evidence is the 10-Q sentence itself: "The need for these additional actions reflects, in part, higher levels of discounting." The ASP figure is supporting evidence only, because channel mix could explain all of it.

**Watch items (dated):** Investor Day Nov 16 to 17 (completion date for Win Now; full-price share or a dated GM target). Q2 FY27 10-Q late Dec 2026 or early Jan 2027 (sign of the ASP line and whether "higher discounts" is named first). Q1 FY28 (summer 2027) laps the World Cup demand-creation spend.
