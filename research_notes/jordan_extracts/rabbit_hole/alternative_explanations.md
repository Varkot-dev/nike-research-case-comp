# Jordan decline: alternative explanations tested (as of 2026-10-13)

Thesis under test: Jordan revenue fell from $8,701M (FY24) to $7,034M (FY26), -19.2%, and fell mid-teens in Q1 FY27, because Nike deliberately cut retro supply to restore scarcity.

Labels: VERIFIED (page or file opened, quote seen), VERIFIED (prior branch) (opened by an earlier agent, cited from its note), SNIPPET ONLY, UNVERIFIED, DERIVED (my arithmetic), OPINION (management or analyst view, quoted as evidence, not as explanation).

Rules followed: no email in any User-Agent (all fetches used "Mozilla/5.0"); nothing in the repo was edited. Local files: Nike transcripts and filings in `scratchpad/jordan_market/dl/`; adidas decks in `rh/alternatives/adidas_dl/`; DICK'S release in `rh/alternatives/dks_dl/`; Google Trends pulls `rh/alternatives/gt_set1.json`, `gt_set2.json`, `gt_set3.json`, script `gt.py`, Jul to Sep averages `gt_julsep.txt`.

Prior work reused (not duplicated): retailer sell-through (origin/claude/wonderful-franklin-u31n4e, `research_notes/thesis_tests/retailer_sell_through.md`), resale, China and teen data (origin/claude/stoic-shannon-dmkmyu, `research_notes/Nike decline execution vs structural/*.md`), channel margins (origin/claude/zealous-mccarthy-rj0t2h).

---

## 0. Decomposition frame (DERIVED, all inputs from filings in `data/nike_filing_facts.csv`)

| Driver | Measure | Result |
|---|---|---|
| Total Jordan change FY24 to FY26 | 8,701 to 7,034 | -$1,667M, -19.2% |
| Currency | FY25 -16% reported and c-n; FY26 -3% reported, -5% c-n (FY26 10-K p. 32) | Currency helped by about 2 pts in FY26. Constant-currency decline is about -20.2% (0.84 x 0.95). Currency is not a cause. |
| NIKE Brand ex-Jordan (common factors) | NIKE Brand 49,322 to 45,222 (FY24 10-K p. 38; FY26 10-K p. 32), less Jordan | Ex-Jordan -6.0%. Jordan is 17.6% of FY24 NIKE Brand but 41% of its FY24 to FY26 decline. About 6 of Jordan's 19 pts can be attributed to factors common to all of Nike; about 13 pts (about $1.1B) are Jordan-specific. |
| Channel mix (Jordan over-indexes to Direct, about 50%, per `12_jordan_brand_thesis.md` Section 4) | Apply NIKE Brand channel trends (Direct 21,519 to 17,720, -17.7%; wholesale 27,758 to 27,453, -1.1%) to Jordan's FY24 split | Jordan would be -9.3% vs NIKE Brand -8.3%. Heavier Direct weighting explains only about 1 pt (about $90M). |
| Greater China | Jordan penetration outside North America is "about 10 points lower" (Nike transcript, Q4 FY23). Solving 21,396p + 27,926(p - 0.10) = 8,701 gives NA about 23%, other geos about 13%. GC Jordan FY24 about $1.0B. | If GC Jordan fell like GC overall (-22.5%, 7,545 to 5,847), that is about $0.23B (14% of the decline); if it fell twice as fast, about $0.45B (27%). Assumption-heavy: Nike says "Jordan is a big business in Greater China" (Q1 FY25 call), so GC penetration could be higher than 13%. |
| Price | AJ1 High $180 to $185, AJ12 $200 to $205 (Complex, May 26, 2025, VERIFIED) | +2.5% to +2.8%. Raises revenue per pair, so it cannot produce a revenue decline unless demand elasticity exceeds 1. FY25 (-16%) predates the June 2025 increase. |

Q1 FY27 (DERIVED): Jordan about 13% x $11,213M = about $1.46B; a 15% decline implies about $1.71B a year earlier (14.6% of Q1 FY26 revenue) and a drop of about $0.26B. GC total revenue fell $332M (1,512 to 1,180, Q1 FY27 10-Q p. 25). GC Jordan at about 13% penetration (about $0.20B) falling 26% to 50% gives $0.05B to $0.10B, i.e. 20% to 39% of Jordan's Q1 drop. North America Nike revenue grew 2% in the same quarter (10-Q p. 25), so most of the Jordan drop sits outside China.

---

## 1. US athletic footwear market decline: RULED OUT as main driver

For the alternative:
- Units are falling: H1 2026 "higher average selling prices (ASP) continued to offset weaker demand reflected in a decline in units sold" (Circana, Aug 17, 2026, VERIFIED, circana.com/post/performance-shoe-sales-pick-up-the-pace-amid-selective-us-consumer-spending-in-the-footwear-market). FY2025 "units sold declined in the low single digits" (Circana via Mr Mag, Feb 5, 2026, VERIFIED, mr-mag.com/circana-issues-q4-2025-footwear-industry-pulse-report/).
- Retail: "2026 Outlook Revised Due to Challenging Athletic Footwear and Apparel Marketplace" (DICK'S Q2 2026 release, Aug 25, 2026, VERIFIED, s205.q4cdn.com/510074553/files/doc_news/DICKS-Sporting-Goods-Inc--Reports-Second-Quarter-Results-2026.pdf).

Against:
- US footwear dollars "held steady in 2025 at $90 billion"; sport lifestyle "up 4% in dollar sales" (Mr Mag/Circana, VERIFIED). H1 2026 total "+1%" (Circana, VERIFIED).
- Nike's own North America footwear rose 5% c-n in FY26, with units +6% (FY26 10-K, NA section, VERIFIED), and NA footwear +1% in Q1 FY27 (10-Q, VERIFIED). Jordan fell 19% over the same window.
- The DICK'S banner comped +4.9% in Q2 2026 (same release, VERIFIED).

Verdict: ruled out. The market is flat in dollars; Jordan is about 20 pts worse. Common market factors fit at most the 6 pts that Nike ex-Jordan also lost.

## 2. Basketball category decline: RULED OUT for Jordan retro; PARTIALLY FITS for performance

For:
- adidas basketball -20% (Q1 2026, investor call deck p. 15) and -21% (Q2 2026, deck p. 25), currency-neutral, "the steepest" of its categories (VERIFIED on adidas' own deck, res.cloudinary.com/.../Investor_Call_Q2_2026_qjofmo.pdf). This upgrades the repo's prior "unverified" label.
- Curry left Under Armour for Li-Ning (WBTV, VERIFIED in repo).

Against:
- "Basketball was up double digits in North America" (Nike transcript, Q1 FY27, VERIFIED, OPINION-free fact claim by management).
- Google Trends US "basketball shoes", Jul to Sep average: 17.0 (2022), 15.7 (2023), 17.7 (2024), 17.3 (2025), 17.3 (2026): flat (VERIFIED, my pull, `gt_julsep.txt`).
- Nike locates the problem in "Jordan Streetwear", not Jordan Basketball (Q4 FY26 call, VERIFIED). JD's FY26 annual report cites "several successful retro basketball product launches" (VERIFIED (prior branch), JD Annual Report FY26 PDF p. 14).

Verdict: ruled out as an explanation for the retro-led decline. adidas' basketball weakness is real but does not appear in Nike Basketball or US search interest.

## 3. Fashion shift to low-profile and running-inspired: PARTIALLY FITS (demand side)

For:
- Google Trends US, Jul to Sep average (VERIFIED, my pull): "jordan 1" 70 (2021), 64 (2022), 51 (2023), 29 (2024), 23 (2025), 17 (2026), -76% from 2021. "adidas samba" 1, 2, 11, 24, 20, 17. "new balance 9060" 0, 1, 7, 16, 16, 10. "onitsuka tiger" 1, 1, 2, 4, 6, 7. AJ1 interest fell 43% from 2023 to 2024, while Jordan revenue was still at its FY24 peak, i.e. before most of the cuts.
- Circana: 2025 sport lifestyle growth "driven primarily by running-inspired and soccer/football-inspired styles" (VERIFIED); H1 2026 "Growth in running-inspired styles was not enough to offset an overall decline in sport lifestyle footwear" (VERIFIED).
- Nike's own running-inspired P-6000 and V5 Runner "grew by strong double digits" while "aged, higher volume, sportswear footwear sold through below expectations" (Nike transcript, Q1 FY27, VERIFIED).

Against:
- The Samba peak passed in 2024 (search down about 30% by 2026), and adidas Originals grew only +4% in Q2 2026 (adidas deck p. 36, VERIFIED), yet Jordan kept falling. So the terrace trend explains the 2023 to 2024 onset, not the 2026 leg.
- "jordan 4" interest rose to 41.7 in 2024 then fell to 24.3 in 2026 (-42%), the period when Nike shifted retro volume onto AJ4. This fits both oversupply and fading demand.
- Caveat: Apr to Jun 2026 shows a simultaneous spike in every term pulled (likely a Trends sampling artifact); Jul to Sep comparisons avoid it.

Verdict: partially fits. Timing of the taste shift precedes the revenue decline by about a year.

## 4. Low-income/young consumer pressure and price increases: PARTIALLY FITS for 2026, RULED OUT for FY25

For:
- JD Sports North America like-for-like -6.8% in the quarter to Aug 1, 2026; ii: "Lower-income shoppers are under pressure due to rising energy costs ... particularly in its core younger market", and cites "the loss of brand heat at key supplier Nike" (ii.co.uk, Aug 20, 2026, VERIFIED, OPINION of the writer).
- Nike: "added pressure on traffic and discretionary spending across our geographies" (Q4 FY26 call, VERIFIED, OPINION).
- Nike US "surgical price increase ... beginning in fall '25" (Q4 FY25 call, VERIFIED); AJ1 High $180 to $185 (Complex, VERIFIED); "Nearly half of consumers report delaying purchases or choosing lower-priced alternatives due to price increases" (Circana, Aug 2026, VERIFIED).

Against:
- FY25's -16% (June 2024 to May 2025) came before the price increase. A 2.8% price rise cannot account for a mid-teens revenue fall.
- No Jordan buyer income or age data was found on any opened page (UNVERIFIED gap). Piper Sandler teen spending fell 7% in Fall 2025 (VERIFIED in repo), but Nike's male teen share grew, "driven by upper-income teens" (VERIFIED (prior branch)).

Verdict: partially fits as a 2026 headwind to units; cannot be quantified for Jordan.

## 5. Nike DTC/SNKRS collapse as cause: PARTIALLY FITS, but mostly the same decision

- NIKE Brand Digital $12.6B (FY23) to $8.6B (FY26) (10-Ks, VERIFIED in repo). Management planned it: classics "down nearly 50% versus the prior year on NIKE Digital" (Q1 FY25 call, VERIFIED).
- Google Trends "snkrs" Jul to Sep: 3.7 (2023), 1.7 (2024), 1.0 (2026); "stockx" 25.3 (2022) to 11.0 (2026) (VERIFIED, my pull; low absolute values, so noisy). The whole hype-release ecosystem shrank, not only Nike's app.
- No Sensor Tower, Appfigures or Similarweb data could be opened (UNVERIFIED).
- DERIVED: Jordan's Direct over-index adds only about 1 pt of extra decline (Section 0).

Verdict: partially fits. The digital pullback is largely the same supply decision, but falling search interest in SNKRS and StockX points to lower demand for launches as well.

## 6. Accounting/reporting artifacts: RULED OUT (once the restatement is handled)

- FY24 $8,701M and FY25 to FY26 are on the same post-restatement basis; the FY25 10-K says "Prior year amounts have been recast" and "There is no change to our reported revenues" (VERIFIED in repo). No filing reports a change in which products count as Jordan (`JORDAN_SEC_FINDINGS.md`).
- The only artifact is chaining old to new bases, which would show +4% instead of -16%.
- Currency helped in FY26 (+2 pts).

Verdict: ruled out. If anything, the artifacts flatter Jordan.

## 7. China-specific collapse: PARTIALLY FITS (about 15% to 40%, assumption-dependent)

- For: Q1 FY25 10-Q: "Greater China revenues decreased 3% ... primarily due to lower revenues in the Jordan Brand"; FY25 10-K lists Jordan among the GC drivers (VERIFIED in repo). Dewu resale for new Jordan retros was about 53% to 55% of retail in 2026 (21jingji, VERIFIED (prior branch)).
- Against: the FY25 10-K says "North America revenues decreased 8% ... primarily due to lower revenues in the Jordan Brand" (VERIFIED in repo). Hill: "North America will feel the biggest impact" of the new cuts (Q1 FY27, VERIFIED). DERIVED sizing in Section 0: China explains about 14% to 27% of FY24 to FY26 and about 20% to 39% of Q1 FY27.

## 8. Brand heat / cultural relevance: FITS (demand side), but cannot be separated from oversupply

- AJ1 search interest -76% from 2021 (Section 3). Piper Sandler Nike teen footwear mindshare 61% (Fall 2023) to 46% (Fall 2025) (VERIFIED (prior branch)). No Jordan in Lyst Q2 2026 top 20 (VERIFIED in repo).
- Resale: AJ1 High premium 61% (2020) to 4% (2023) (Reuters via Cyprus Mail, VERIFIED). SneakerPing: 70.7% of 605 Jordan releases from Aug 2024 to Aug 2026 last sold below retail, median 20% under (BallerAlert, VERIFIED (prior branch); methodology unverified). StockX Jordan average price +6% in 2025, "early signs of recovery" (SGB, VERIFIED (prior branch)).
- Sell-through: DICK'S says Foot Locker has "greater dependence on footwear launch and retro product. Not only were there fewer launches in the second quarter, but those launches performed below both industry and our expectations" (DICK'S Q2 2026, VERIFIED). Nike: "sell-through remains challenged, impacting both current discounting and future order books" (Q4 FY26, VERIFIED, OPINION). 10-Q: "higher levels of discounting and broader marketplace pressure" (Q1 FY27 10-Q p. 20, VERIFIED).

---

## Overall verdict

1. Not the market, basketball, accounting or currency. Those are ruled out or work in Jordan's favour.
2. Common Nike-wide factors (macro, DTC reset, China at the Nike level) account for about 6 of the 19 pts (DERIVED from NIKE ex-Jordan -6.0%). China inside Jordan accounts for about 2 to 5 pts. Price accounts for about 0 pts of revenue.
3. The remaining Jordan-specific 10 to 13 pts are a reduction in retro volume. The cut was deliberate: "The Jordan brand was planned down double digits ... we expect Jordan to be down at the same rate for fiscal '25" (Q1 FY25), and FY25 came in at -16%. But the evidence says the cut was a response to demand that had already fallen, not a voluntary sacrifice of healthy demand:
   - AJ1 search interest fell about 55% from 2022 to 2024, before revenue peaked.
   - AJ1 resale premiums had already collapsed by 2023.
   - "Air Jordan 1 and Dunk remain elevated" inventory (Q3 FY25).
   - Launches underperformed in 2026 even with fewer launches (DICK'S).
   - Most Jordan releases traded below retail through Aug 2026.
4. Rough split (DERIVED, low confidence): about 35% to 50% of the FY24 to FY26 decline is supply action Nike chose (retro volume and digital pullback); about 50% to 65% is demand: common Nike and market factors, China, and lower full-price sell-through. Even the supply part was triggered by demand. The evidence cannot separate units Nike withheld from units retailers declined to order, because Nike discloses no Jordan units, ASP, inventory or channel split.
5. So the defensible thesis is "Nike is cutting supply in response to a demand reset it caused by oversupply". "Deliberately cut supply" alone is not supported. "No other explanation fits" would be false.

## Single piece of evidence that would most change the verdict

How the reduced-volume holiday 2026 retros sell through at full price, and what they resell for, together with any Jordan units and inventory figure Nike gives at its Nov 16 to 17 Investor Day or on the Q2 FY27 call. The launches are AJ4 "Bred", AJ11 "Space Jam" and AJ12, plus the AJ1 "Royal" at $185 on Oct 10. If these sell out at full price and trade above retail on StockX, the supply story strengthens. If they trade below retail despite fewer pairs, demand is the binding constraint.
