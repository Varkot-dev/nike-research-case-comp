# W_DISCOUNT_RECOVERY: Will Nike's discounting end, how long will full-price recovery take, and what is it worth?

> Repository copy: CSVs are in `data/recovery/`.
>
> **Reconciliation with note 15 (read this first).** This note describes the NIKE Brand ASP line as still negative seven quarters after its worst point. The quarterly bridge in note 15 (`data/discount/gm_bridge_bps.csv`) shows the line went -330 bps (Q2 FY25), -150 (Q3 FY25), about -307 implied (Q4 FY25), -250 (Q1 FY26), -50 (Q2 FY26), **+80 (Q3 FY26, "primarily due to strategic pricing and product mix", Q3 FY26 10-Q p. 30)**, about +258 implied (Q4 FY26, derived), then -30 (Q1 FY27 10-Q p. 23). So the ASP line did turn positive for two quarters, about 5 to 6 quarters after the worst quarter (within the precedent range of 3 to 6 once the implied Q4 is counted), then slipped back. The accurate statement is: ASP recovered briefly in H2 FY2026 and turned slightly negative again in Q1 FY2027, while the Q1 FY27 10-Q (p. 20) extends Sportswear and Jordan actions beyond FY2027. Part of the remaining gap is channel mix, which the filings say will not reverse (FY26 10-K p. 33).


Prepared 2026-10-13. Scratch work only; no repo files were edited. CSVs are in `scratchpad/recovery/` (listed at the end).

Citation conventions: Nike filings are cited by printed page, for example (Q1 FY27 10-Q p. 23). Earnings releases are cited by page counted from the first page of the exhibit. PitchBook figures come from `scratchpad/pb/a.xlsx` (quarterly) and `b.xlsx` (annual), in USD thousands, and are labelled *PitchBook*. Peer 10-Ks were downloaded from sec.gov with a generic contact header (sec.gov returned 403 without one). Older Nike filings (FY2009, FY2010, FY2017, FY2018 and their 10-Qs) came from the investors.nike.com mirror. *My arithmetic*, *my inference* and *my judgement* mark anything not printed in a source. Management and analyst words are quoted as *opinion*.

---

## A. Plain-English summary (for someone new to finance)

1. **What "gross margin" means here.** For every $100 of sales, Nike keeps $42.90 after paying for the product (FY2026, FY26 10-K p. 32). It kept $44.60 in FY2024 (FY24 10-K p. 33) and $46.00 in FY2022 (FY22 10-K p. 31). The pitch question is whether that $1.70 gap comes back.
2. **Why it fell.** Nike's own bridge for FY2025 says the largest cause was a lower average selling price (ASP): "Lower NIKE Brand ASP (decreasing gross margin approximately 180 basis points), primarily due to higher discounts and changes in channel mix" (FY25 10-K p. 35). 180 bps is $1.80 per $100. All the other items in FY2025 and FY2026 roughly net out (my arithmetic, Section E table E0).
3. **Nike's own history says these clean-ups usually take 3 to 5 quarters.** In 2009 to 2010, 2017 to 2018 and 2022 to 2023, gross margin turned up 3 to 4 quarters after the worst discounting quarter and 4 to 5 quarters after inventory peaked (Section B).
4. **This time Nike is already past that clock.** The worst ASP quarter was Q2 FY2025 (-330 bps, Q2 FY25 10-Q p. 26). Seven quarters later, ASP is still a drag (-30 bps in Q1 FY2027, Q1 FY27 10-Q p. 23), and Nike now says the Sportswear and Jordan actions "are expected to extend beyond fiscal 2027" (Q1 FY27 10-Q p. 20), not "by the end of December 2026" as the 10-K said (FY26 10-K p. 30).
5. **Peers show margin can come back fast, but sales usually pay for it.** Ralph Lauren cut sales 16.5% over two years and raised its adjusted gross margin by about 400 bps over the same two years (my arithmetic). adidas recovered its margin in 4 to 5 quarters, helped by selling its Yeezy stock. Under Armour and Vans raised margins while sales kept falling for years (Section C).
6. **What to watch.** The cleanest signals are: the ASP line in Nike's gross margin bridge turning positive for two quarters; inventory growing at least 3 points slower than sales; nike.com's men's sale share falling below 39% (it is 45.7% today); and Nike's markdown rate at Running Warehouse falling from 49% toward the store's 23% (Section D).
7. **What it is worth.** Each 100 bps of gross margin on about $43 to $44 billion of revenue is about $430 to $436 million of operating profit, or about $0.22 to $0.23 per share after a 21% to 25% tax rate, roughly 13% to 14% of the FY2028 consensus EPS of $1.65. At 20 times earnings that is about $4.40 to $4.60 per share (my arithmetic, Section E).
8. **Verdict (my judgement).** Some recovery is likely, but not on management's original timetable and probably not all of it. A sustained ASP gain looks unlikely before the second half of FY2028, and part of the lost ASP comes from Nike's shift toward wholesale, which will not reverse when discounting stops. At $35.35 the stock already prices in roughly a 43% gross margin, so the payoff from here depends on whether Nike gets above 43.5% (Section F).

---

## B. Nike's own precedents

Quarterly series for all of these episodes are in `nike_pb_quarterly_gm_inventory.csv` (PitchBook, FY1990 to Q1 FY27) and `nike_current_episode_quarterly.csv` (filing facts, Q1 FY23 to Q1 FY27). Annual history is in `nike_pb_annual_gm_inventory.csv`.

| Episode | Inventory peak | Peak markdown quarter | First positive GM quarter (y/y) | Quarters from inventory peak / from markdown peak | First positive price line | Quarters with inventory growth at least 3 pp below sales | GM lost | GM recovered | Revenue given up |
|---|---|---|---|---|---|---|---|---|---|
| FY2009 to FY2010 recession glut | Feb 2009, $2,467M, +3% y/y while revenue fell 2% (*PitchBook*) | Q4 FY09: GM 43.4%, -240 bps (FY10 10-K p. 22). Q1 FY10: -100 bps, "increased discounts" (Q1 FY10 10-Q p. 19) | Q3 FY10 (Feb 2010): 46.9% vs 43.9%, +300 bps (Q3 FY10 10-Q p. 21) | 4 / 3 | No ASP line then. Q3 FY10 driver: "Improved inventory positions across most businesses, which drove fewer discounted close-out sales" (Q3 FY10 10-Q p. 21) | 4 (Q2 FY10 to Q1 FY11; *PitchBook*) | FY09 44.9% vs FY08 45.0% (-10 bps for the year, -240 bps in Q4) (FY10 10-K p. 21) | FY10 46.3%, +140 bps (FY10 10-K p. 26); Q4 FY10 47.4%, +400 bps (FY10 10-K p. 22). Above the FY08 level | FY10 revenue $19,014M vs $19,176M, -1% (FY10 10-K p. 24); Q1 FY10 -12% (*PitchBook*, my arithmetic) |
| FY2016 to FY2019 North America clean-up | Growth peak May 2016: $4,838M, +12% vs revenue +6% (FY19 10-K p. 22). Dollar peak Feb 2018: $5,366M (*PitchBook*) | Q1 FY18: GM -180 bps. Full-price ASP -80 bps "reflecting higher discounts", off-price -50 bps, NIKE Direct -40 bps, FX -130 bps (Q1 FY18 10-Q p. 22) | Q4 FY18 (May 2018): 44.7% vs 44.1%, +60 bps (FY18 10-K p. 19) | 1 from the dollar peak, 8 from the growth peak / 3 | Q1 FY19: full-price ASP +100 bps, plus full-price mix +30 bps "reflecting reduced promotional activity" (Q1 FY19 10-Q p. 23). Q2 FY18's +40 bps did not last (Q3 FY18 was -50) | 4 (Q4 FY18 to Q3 FY19; *PitchBook*) | FY16 46.2% to FY18 43.8%, -240 bps, of which FX was about -90 bps in each year (FY17 10-K p. 25; FY18 10-K p. 24) | FY19 44.7%, +90 bps (FY19 10-K p. 26); Q3 FY19 45.1%. FY16 level regained only in FY22 (46.0%) | North America revenue -2% in FY18 while NIKE, Inc. grew 6% (FY18 10-K p. 27) |
| FY2023 post-COVID glut | Aug 2022, $9,662M, +44% vs revenue +4% (Q1 FY23 release p. 3) | Q2 FY23: GM 42.9%, -300 bps (Q2 FY23 release p. 1); NIKE Direct margin -160 bps "to liquidate excess inventory" (Q2 FY23 10-Q p. 28) | Q2 FY24 (Nov 2023): +170 bps (Q2 FY24 10-Q p. 28) | 5 / 4 | Q1 FY24: full-price ASP +300 bps and NIKE Direct margin +10 bps (Q1 FY24 10-Q p. 24) | 5 (Q4 FY23 to Q4 FY24) | FY22 46.0% to FY23 43.5%, -250 bps (FY23 10-K p. 34) | FY24 44.6%, +110 bps (FY24 10-K p. 36); Q3 FY24 44.8%. Regained 110 of the 250 bps lost | None up front (FY23 revenue +10%). FY24 +0.3%, with footwear units -2% and apparel units -9% (FY24 10-K p. 35) |
| **FY2025 to now** | No glut in dollars: $7.5B to $8.3B since FY24 (Q1 FY25 10-Q p. 3; Q1 FY27 10-Q p. 3). The issue is aged Sportswear and Jordan product | Q2 FY25: NIKE Brand ASP line -330 bps (Q2 FY25 10-Q p. 26); nike.com men's sale share peaked at 52.9% in 2025Q1 (`nike_sale_share_quarterly.csv`) | **None yet on an underlying basis.** Q4 FY26 was +890 bps, of which about 900 bps was the IEEPA tariff recovery (Q4 FY26 release p. 1). Q1 FY27 was +60 bps, driven by logistics +90 bps (Q1 FY27 10-Q p. 23) | n/a / **7 and counting** | Q3 FY26 +80 bps (Q3 FY26 10-Q p. 30), then Q1 FY27 -30 bps (Q1 FY27 10-Q p. 23). Not sustained | 3 (Q1 to Q3 FY26, -1 to -4 pp), then +1 pp in Q4 FY26 and Q1 FY27 (my arithmetic) | FY24 44.6% to FY25 42.7%, -190 bps (FY25 10-K p. 35) | FY26 42.9%, +20 bps (FY26 10-K p. 34); Q1 FY27 42.8% | FY25 -10%; FY26 flat; FY27 guided to a high-single-digit decline (Q1 FY27 release p. 1) |

**What the precedents say (my arithmetic from the table):**
- Nike's clock in its three earlier clean-ups ran **3 to 4 quarters** from the worst discount quarter to a positive gross margin, and **4 quarters** to a sustained positive price line. Inventory then grew at least 3 points slower than sales for **4 to 5 quarters**.
- The size of the recovery varied. The FY2010 rebound overshot the pre-crisis margin (+140 bps for the year). FY2019 regained 90 of 240 bps, and FY2024 regained 110 of 250 bps. Neither returned to the prior peak within two years. **Partial recovery is the norm for Nike, not the exception.**
- The current episode has now run **7 quarters** past its markdown peak with no sustained positive ASP line, which is longer than any of the three precedents. Two things differ. First, there is no dollar inventory glut to burn off: inventory is flat, so the problem is the mix of aged styles, which a falling inventory total cannot show. Second, Nike is moving revenue from NIKE Direct to wholesale: the Direct share fell from 43.7% in FY24 to 39.2% in FY26 (05_channel_split.md, citing FY24 10-K p. 84 and FY26 10-K p. 83). Wholesale sales carry a lower ASP, so this mix shift lowers the ASP line even with no extra discounting.
- In FY2010 and FY2024, cost tailwinds explained part of the rebound. FY10 had "reduced raw material and freight costs" (FY10 10-K p. 26). FY24 had full-price ASP of +200 bps from "strategic pricing actions" (FY24 10-K p. 36), and the earlier product-cost headwind had faded. Today's cost line is not a tailwind: product costs were +10 bps in Q1 FY27 (Q1 FY27 10-Q p. 23), and the tariff regime after the IEEPA refund is not quantified in the 10-Q.

---

## C. Peer cases of full-price recovery or failure

Detail and sources: `peer_cases.csv`.

| Company and episode | What they did | Inventory | Gross margin path | Time to GM recovery | Price metric | Revenue given up first | Outcome |
|---|---|---|---|---|---|---|---|
| **adidas**, 2023 Yeezy and inventory clean-up | Conservative wholesale sell-in; North America deliberately shrunk for 7 quarters; sold the Yeezy stock rather than writing it off; scaled Samba and Gazelle supply below demand (adidas_gulden.md, adidas releases) | EUR 5,973M at end-2022 (+49%) to EUR 4.5B at end-2023, "down almost EUR 1.5 billion" | 2021 50.7%; 2022 47.3%; 2023 47.5%; 2024 50.8%; 2025 51.6%; Q1 2026 51.1%; Q2 2026 52.5% | 2 quarters to the first y/y gain (Q2 2023, Yeezy-aided); 4 to 5 quarters to a clean gain (Q4 2023 +5.5pp; Q1 2024 51.2%, +6.4pp). Pre-crisis level passed in year 2 | No ASP disclosure. 2024 gains were "driven by lower product and freight costs" and lower discounting | Yeezy revenue of more than EUR 1.2B (2022); North America -16% c.n. in 2023; group c.n. growth 0% in 2023 | **Success.** Revenue grew 12% c.n. in 2024. But about EUR 500M of Yeezy operating profit (2023 to 2024) helped, and Nike has no equivalent asset to sell |
| **Under Armour**, 2017 to 2021 off-price exit | Cleared inventory through off-price in 2018, then cut off-price's share of wholesale from 2019; by 2021 was "exiting undifferentiated retail" (UA 2021 10-K p. 29) | $1,158.5M Dec 2017 to $1,019.5M Dec 2018 (-12%) (UA 2018 10-K p. 27) and $892.3M Dec 2019 (XBRL) | 2015 48.1%; 2016 46.4%; 2017 45.1%; 2018 45.1%; 2019 46.9%; 2020 48.3%; 2021 50.3% (UA 10-Ks 2017 p. 32, 2018 p. 32, 2019 p. 34, 2020 p. 38, 2021 p. 29) | About 4 to 5 quarters from the Dec 2017 inventory peak to the first annual GM gain (2019; annual data only). 2015 level regained in 2020 | Lower off-price share added about +50 bps in 2019 (UA 2019 10-K p. 34) and about +220 bps in 2020 (UA 2020 10-K p. 38) | North America -$76.9M (-2%) in 2019 "due to a unit sales decrease of off-price sales" (UA 2019 10-K p. 37) | **Margin success, growth failure.** GM rose 520 bps from 2018 to 2021, but revenue was flat in 2017 to 2019 |
| **Under Armour**, 2024 to 2026 reset | Planned promotional cuts (eCommerce -20% to -27% a quarter in FY2025), about 25% fewer SKUs, restructuring up to about $305M (under_armour_plank.md, UA 8-Ks) | $958.5M Mar 2024 to $914.8M Mar 2026 (XBRL) | FY2024 46.1%; FY2025 47.9% (+180 bps); FY2026 45.5% (-240 bps, tariffs); Q1 FY2027 54.1% (IEEPA refunds) | Immediate (Q1 FY25 +110 bps), then erased by tariffs | n/a | FY2024 $5.7B to FY2026 $5.0B (-13%); North America down 10 straight quarters; FY2027 guide cut to a mid-single-digit decline | **Failure so far.** Adjusted operating income fell from $310M to $107M |
| **Ralph Lauren**, FY2017 to FY2019 Way Forward Plan | "Strategic reduction of shipments (including within the off-price channel) and points of distribution"; closed about 25% of underperforming U.S. department store doors in FY2018; lower promotions (RL FY18 10-K pp. 40, 45) | $1,124.6M Apr 2016 to $791.5M Apr 2017, -30% (RL FY17 10-K p. F-2) | FY2016 56.5%; FY2017 54.9% (57.9% excluding $197.9M of inventory charges, my arithmetic, RL FY17 10-K p. 47); FY2018 60.7%, adjusted +290 bps (RL FY18 10-K p. 47; Q4 FY18 release); FY2019 61.6%, adjusted +90 bps (RL FY19 10-K p. 46); FY2020 59.3% with COVID charges (RL FY20 10-K p. 45); FY2026 69.9% (XBRL, my arithmetic) | Adjusted GM up "in every quarter" of FY2018, 4 to 7 quarters after the Apr 2016 inventory peak; underlying GM was already rising in FY2017 (my arithmetic) | DTC AUR +4% in FY2018, "with growth in every quarter" (Q4 FY18 release); +8% in FY2019 (Q4 FY19 release); +3% in FY2020 and +8% in Q4 FY2020 (Q4 FY20 release) | $7,405M FY2016 to $6,182M FY2018, -16.5% (my arithmetic; RL FY17 p. 44, FY18 p. 44). North America -15.6% in FY2017 and -14.6% in FY2018 (RL FY18 10-K p. 45). Back to growth in FY2019, +2.1% (RL FY19 10-K p. 44) | **Success on margin and AUR in about 2 years.** But the FY2015 revenue peak ($7,620M, XBRL) was not passed until FY2026 ($8,114.5M) |
| **VF / Vans**, FY2023 to FY2027 | "Deliberate actions taken to right-size inventories in the Americas wholesale channel in the second half of Fiscal 2024" (VF FY25 10-K MD&A); "exiting value-channel wholesale customers and closing unprofitable owned retail stores" (VF FY26 10-K p. 31) | n/a at brand level | VF total: FY2022 54.5%; FY2023 52.5% (VF FY23 10-K p. 27); FY2024 52.0% (VF FY24 p. 29); FY2025 53.5%; FY2026 54.8% (VF FY26 p. 28); Q1 FY2027 54.9% | About 8 quarters from the H2 FY2024 right-sizing back to the FY2022 level (FY2026) | FY2026 GM driven by "higher quality inventory, lower product costs, increased pricing" (VF FY26 10-K p. 28) | Vans $4,161.9M in FY2022 (VF FY23 10-K p. 28) to $2,149.1M in FY2026 (VF FY26 10-K p. 30), -48% (my arithmetic); -12%, -24%, -16%, -9%, then -8% in Q1 FY2027 | **Margin recovered at group level; Vans sales still falling after four years** |
| **Lululemon**, FY2025 to FY2026 (not a completed reset) | Cause of the GM decline not verified in the repo | +18% at Feb 1 2026 (units +6%); -1% at Aug 2 2026 | FY2024 59.2%; FY2025 56.6%; Q1 FY2026 54.2%; Q2 FY2026 60.5% including a 560 bps tariff refund (54.9% excluding it, my arithmetic) | Not recovered | n/a | Americas -3% (Q1 FY26) and -8% (Q2 FY26); FY2026 guide -5% to -7% | **Ongoing.** Inventory has normalized but margin has not (competitor_benchmarks.md) |

**Read across (my inference):**
- Every peer that cut off-price or wholesale doors got gross margin back within **4 to 8 quarters**. Margin is the easy part.
- The cost was revenue: **-16.5% over two years (Ralph Lauren), -13% over two years and still falling (Under Armour 2024 to 2026), -48% over four years (Vans)**. adidas is the only case where revenue grew within a year, and it had a hot franchise and a sellable problem asset.
- Ralph Lauren is the best template for "full price comes back": inventory -30% in one year, a disclosed AUR that rose every quarter, and adjusted margin up about 400 bps in two years (56.8% FY2016 excluding $20.4M of charges, to 60.8% adjusted FY2018; my arithmetic). Nike has not published an AUR-type number. Its nearest equivalent is the ASP line in the gross margin bridge.

---

## D. Indicator dashboard

Full table: `indicator_dashboard.csv`. Readings are as of 2026-10-13.

| Indicator | Today | Recovery threshold | Failure threshold | Next update | Source |
|---|---|---|---|---|---|
| Inventory growth minus revenue growth (y/y) | +1.3 pp in Q1 FY27 (inventory -3%, revenue -4%); +1.1 pp in Q4 FY26; -1.1 to -3.6 pp in Q1 to Q3 FY26 | -3 pp or lower for 2 straight quarters (the precedents ran -6 to -21 pp during their recoveries) | Above +3 pp for 2 quarters, or a sequential build while sales fall | Q2 FY27 results, Dec 2026 | Q1 FY27 release p. 1; Q1 FY27 10-Q p. 3; my arithmetic |
| NIKE Brand ASP line in the GM bridge | -30 bps Q1 FY27; +80 Q3 FY26; -50 Q2 FY26; -250 Q1 FY26 | Positive for 2 straight quarters and at least +50 bps (Q1 FY19 was +100; Q1 FY24 was +300) | Negative again in Q2 FY27 with "higher discounts" cited | Q2 FY27 10-Q, Dec 2026 to Jan 2027 | Q1 FY27 10-Q p. 23; Q1 to Q3 FY26 10-Qs |
| Gross margin excluding one-offs, y/y | +60 bps Q1 FY27 (logistics +90, ASP -30); Q4 FY26 about -10 bps excluding the 900 bps IEEPA benefit (my arithmetic) | Up y/y with ASP as the largest positive driver; a non-Q4 quarter at 44% or more | Flat or down with ASP negative | Q2 FY27, Dec 2026 | Q1 FY27 10-Q p. 23; Q4 FY26 release p. 1 |
| nike.com men's sale shoes as a share of men's shoes | 45.7% (Oct 13); 43% to 46% through 2026 | Below 39%, the top of the 2022 to 2023 range of 26% to 39%, in 2 quarterly reads | Above 46% after holiday 2026, or a new high above 53% | Re-scrape any time; next quarterly read Jan 2027 | `data/marketplace/nike_sale_share_quarterly.csv` |
| nike.com whole-site sale wall item count | 5,102 (Oct 13); 5,131 in Aug 2026, a series high | Below 3,500 (2022 to 2023 ran 2,486 to 4,563) | Above 5,200 | Re-scrape any time; Jan 2027 | marketplace_pricing_and_shelf_share.md, Series 2 |
| Running Warehouse: Nike men's road colorways marked down | 49.0% vs a store average of 23.3%; low of 25.4% in Sep 2025 | About 25% or below (the store average) in 2 reads | Above 45% in 2 reads | Monthly; after holiday clearance (Jan 2027) | `data/marketplace/runningwarehouse_history.csv` |
| Foot Locker: Nike share of sale styles vs share of shoe assortment | 35.1% of sale vs 30.4% of assortment; NIKE, Inc. 49.9% of sale shoes | Sale share at or below assortment share | Sale share above 40% with total sale styles flat | Any time | `data/marketplace/footlocker_brand_sale_mix.csv` |
| Poshmark NWT median ask / retail | Dunk Low 0.90; AF1 1.04; AJ1 Low 1.04; AJ1 High OG 0.68; Vomero 5 0.74 (HOKA 0.83; On 0.87) | Vomero 5 and AJ1 High OG at 0.85 or more; classics at 1.0 or more | Classics below 0.85 | Any time (single snapshot today; asks, not sales) | `data/marketplace/poshmark_summary.csv` |
| GOAT Jordan retro resale premium, 2026 releases | Median -19% | Holiday 2026 retros trade above retail within 60 days | Below retail | Dec 2026 to Feb 2027 | `research_notes/12_jordan_brand_thesis.md` |
| nike.com unpaid review rating (stars) | 4.54 in Q1 FY27; trough 4.47 in Q3 FY26; 4.75 to 4.80 in FY24 | Above 4.60 for 2 quarters | Back below 4.50 | Q2 FY27, complete after Nov 30 2026 | `data/reviews/recent_reviews_quarterly_fiscal.csv` |
| Retailer inventory vs comps (Foot Locker within DICK'S) | Inventory about +17% y/y at Aug 1 2026 vs comps of -3.6% | Inventory growth at or below comps | Inventory growth above comps, plus more Nike-heavy liquidation | DICK'S Q3 results, late Nov 2026 | thesis_tests/retailer_sell_through.md |
| Management timeline and order-book language (*opinion*) | FY26 10-K: done "by the end of December 2026" (p. 30). Q1 FY27 10-Q: Sportswear and Jordan "beyond fiscal 2027" (p. 20). Q4 FY26 call: "sell-through remains challenged, impacting both current discounting and future order books" | Investor Day gives a dated gross margin or full-price target, with no further push-out | A further push-out, or a cut to revenue guidance | Investor Day, Nov 2026 (the Q1 FY27 transcript says "November"; Nov 16 to 17 is snippet-only); Q2 FY27 call, Dec 2026 | FY26 10-K p. 30; Q1 FY27 10-Q p. 20; 12_jordan_brand_thesis.md |
| NIKE Brand footwear units vs ASP | Q1 FY27: units -5%, ASP -1 pt, "primarily due to channel mix and higher discounts" | ASP positive with units flat or better | ASP negative with units falling | Q2 FY27 10-Q | Q1 FY27 10-Q p. 23 |

On wholesale futures: Nike describes a futures ordering program, with orders "five to six months ahead of delivery" (FY26 10-K p. 11), but the FY2026 10-K and the Q1 FY27 10-Q give no futures order numbers. The only read on futures is management commentary, which is *opinion*. Treat Investor Day and the Q2 FY27 call as the update points.

**Why discounting is still high: alternatives tested**
1. *Industry-wide promotions.* DICK'S describes "an increasingly aggressive promotional environment for key athletic brands" (retailer_sell_through.md, DICK'S 10-Q Q2 2026 p. 21), and Gulden blames "heavy discounting at many retailers, especially in Europe" (adidas Q2 2026 release). **Partly survives.** At Foot Locker, Nike's on-sale rate (13.2%) is close to the store's 11.4%, and below HOKA (16.0%), On (15.7%) and New Balance (17.7%).
2. *Nike-specific excess.* At Running Warehouse, 49% of Nike colorways are marked down, against 9.5% for HOKA, 12.5% for On, 19% for ASICS and 23% for the store. Nike's own site has its largest sale wall of the 2022 to 2026 series. **Survives.** The excess sits mainly in Nike's own channel and in specialty running, not in mainstream wholesale.
3. *Dollar inventory overhang.* **Ruled out as the main cause.** Inventory is down 3% y/y (Q1 FY27 release p. 1). The 10-Q puts the 5% rise since May on "shifts in product mix" (Q1 FY27 10-Q p. 19). The filings do not split inventory by age, so how much of it is aged product cannot be measured from them.

---

## E. What it is worth (all of Section E is my arithmetic)

**E0. Where the 170 bps gap to FY2024 comes from** (`nike_gm_gap_fy24_to_fy26_bridge.csv`)

| Driver, FY2025 and FY2026 combined | bps | Source |
|---|---|---|
| NIKE Brand ASP (discounts and channel mix) | -180 (FY25); not listed in FY26 (9M FY26 was -80) | FY25 10-K p. 35; FY26 10-K p. 34; Q3 FY26 10-Q p. 30 |
| Other costs, including obsolescence reserves | -90, then +20 | same |
| Converse | -20, then -20 | same |
| Product costs (FY26 = tariffs net of the $986M IEEPA recovery) | +80, then -20 | same; FY26 10-K p. 30 |
| Warehousing and logistics | +20, then +20 | same |
| FX | -10, then +20 | same |
| Prior-year restructuring | +10 | FY25 10-K p. 35 |
| **Total** | **-170** (44.6% to 42.9%) | my arithmetic |

The ASP line accounts for the whole gap on its own. **But the bridge cannot split discounting from channel mix.** The FY2026 10-K says footwear ASP fell about 1 point, "primarily due to channel mix" (FY26 10-K p. 33), while it names "higher discounts" for apparel. That means part of the lost ASP is the planned move to wholesale, which will not reverse when discounting ends. The same move is cutting logistics costs (+20 bps in FY26 and +90 bps in Q1 FY27), which partly offsets it. Both explanations survive. Nike disclosing ASP by channel, or its full-price share in NIKE Direct, would settle it, and Investor Day is the place to ask. History does not show that a lower Direct share caps gross margin: FY2017 to FY2019 ran at a 28% to 32% Direct share with gross margins of 43.8% to 44.7% (05_channel_split.md; FY19 10-K p. 26). Product costs and FX were different then, though.

**E1. Value of each 100 bps** (`valuation_per_100bps.csv`). Shares: 1,485M (market cap $52,506M / $35.35, peer_multiples.csv; weighted diluted shares were 1,484.2M in Q1 FY27, Q1 FY27 10-Q p. 1). Operating costs are held constant.

| Revenue base | Tax | EBIT per 100 bps | Net income | EPS | % of FY28 consensus $1.646 | Value per share at 15x / 20x / 25x |
|---|---|---|---|---|---|---|
| $43.0B | 21% | $430M | $340M | $0.229 | 13.9% | $3.43 / $4.58 / $5.72 |
| $43.0B | 25% | $430M | $322M | $0.217 | 13.2% | $3.26 / $4.34 / $5.43 |
| $43.6B (FY28 consensus) | 21% | $436M | $345M | $0.232 | 14.1% | $3.48 / $4.64 / $5.80 |
| $43.6B | 25% | $436M | $327M | $0.220 | 13.4% | $3.31 / $4.41 / $5.51 |

**E2. Scenarios** (`valuation_scenarios.csv`). FY2028 revenue is $43,645M (Yahoo consensus, consensus_and_valuation.md). FY2028 SG&A is assumed at $15,630M, which is FY2026's $16,114M (FY26 10-K p. 55) less 3%, matching the -3% SG&A in Q1 FY27 (Q1 FY27 release p. 1). Net interest and other items are taken as zero, and the tax rate as 23%, the middle of the 21% to 25% range; the CSV has 21% and 25% too. For FY2029, revenue is assumed to grow 4% to $45,391M and SG&A 2% to $15,943M.

| Scenario | GM | Year | EBIT margin | EPS (23% tax) | vs FY28 consensus $1.65 | Price at 15x / 20x / 25x / 30x | Change vs $35.35 at 20x | P/E at $35.35 |
|---|---|---|---|---|---|---|---|---|
| No recovery, low | 42.0% | FY28 | 6.2% | $1.40 | -$0.25 | $21 / $28 / $35 / $42 | -21% | 25.2x |
| No recovery, FY26 level | 42.9% | FY28 | 7.1% | $1.60 | -$0.04 | $24 / $32 / $40 / $48 | -9% | 22.0x |
| Partial, low | 43.5% | FY28 | 7.7% | $1.74 | +$0.09 | $26 / $35 / $44 / $52 | -2% | 20.3x |
| Partial, high | 44.0% | FY28 | 8.2% | $1.85 | +$0.21 | $28 / $37 / $46 / $56 | +5% | 19.1x |
| Full, FY24 level in FY28 | 44.6% | FY28 | 8.8% | $1.99 | +$0.34 | $30 / $40 / $50 / $60 | +13% | 17.8x |
| **Full, FY24 level by FY29** | 44.6% | FY29 | 9.5% | $2.23 | n/a (Zacks FY29 mean $2.31) | $33 / $45 / $56 / $67 | +26% (undiscounted) | 15.8x |

For reference: the forward P/E is 21.5x on FY28 consensus today, the ten-year forward P/E proxy averaged 33.1x, and adidas trades at 12.9x its FY2 earnings (consensus_and_valuation.md; peer_multiples.csv).

**E3. What the current price implies** (`valuation_price_implied_gm.csv`, 23% tax). This solves for the FY2028 gross margin at which EPS x P/E = $35.35.

| P/E applied | EPS needed | Implied FY28 GM at SG&A $15.13B / $15.63B / $16.13B |
|---|---|---|
| 18x | $1.96 | 43.3% / 44.5% / 45.6% |
| 20x | $1.77 | 42.5% / 43.6% / 44.8% |
| 21.5x (today, on consensus) | $1.64 | 41.9% / **43.1%** / 44.2% |
| 25x | $1.41 | 40.9% / 42.1% / 43.2% |

- **Consensus already embeds a small recovery.** At SG&A of $15.63B, the FY28 consensus EPS of $1.646 needs a gross margin of about 42.9% to 43.3% (21% to 25% tax), against 42.9% in FY26. The FY27 consensus of $1.29 on revenue down 8% needs about 42.3% to 42.6% (my arithmetic).
- **SG&A matters as much as gross margin.** A $500M change in SG&A moves the implied gross margin by about 115 bps. At $35.35 and 20x, the stock prices in about 43.6% with SG&A held at $15.6B. The Pace program's "approximately $2.5 billion in cumulative savings through fiscal 2031" (Q1 FY27 release p. 1) is the other big lever, and it is not modelled here.

---

## F. Verdict: likelihood, timing, and what would change it

**Likelihood (my judgement, based on the evidence above):**
- **Full recovery to 44.6% by FY2029: about 25%.** It needs the ASP line to turn positive by H2 FY2028 and stay there, *and* the channel-mix drag on ASP to be offset by lower logistics costs or pricing. Two of Nike's three precedents regained less than half the lost margin within two years. Only FY2010, helped by falling freight and raw material costs, overshot.
- **Partial recovery to 43.5% to 44.0% by FY2028 to FY2029: about 45%.** This is the base case. It assumes discounting normalizes once Sportswear and Jordan actions finish beyond FY2027 (Q1 FY27 10-Q p. 20), on Nike's 3 to 4 quarter precedent clock, while channel mix keeps 50 to 100 bps of ASP from coming back.
- **No recovery (42% to 43%): about 30%.** This is the Under Armour and Vans pattern: further push-outs, the nike.com sale share stuck at 43% to 46%, and ASP still negative through FY2028.

**Timing (my inference):** if the actions end in early to mid FY2028, the precedents (3 to 4 quarters from the end of heavy markdowns to a positive gross margin; 4 to 8 quarters at peers) point to a sustained positive ASP line in **H2 FY2028 (Dec 2027 to May 2028) at the earliest**. Full-year gross margin recovery would show up in **FY2029**. Management's December 2026 date for completing the marketplace actions no longer applies.

**Value:** each 100 bps of gross margin is worth about $0.22 to $0.23 of EPS, or about $4.40 to $4.60 per share at 20x. Weighting my three scenarios by the probabilities above (FY28 EPS of $1.50, $1.80 and $2.23 for the no-recovery midpoint, partial midpoint and full FY29 cases) gives an expected EPS of about $1.82 and a value of about $36 at 20x (this mixes FY28 and FY29 EPS and is undiscounted). That is close to today's $35.35, so **the recovery is roughly priced at a 20x multiple. Upside requires either the full scenario or a higher multiple** (my arithmetic).

**What would change the verdict:**
- *More bullish:* (1) the Q2 FY27 bridge shows a positive ASP line of +50 bps or more with "lower discounts" named; (2) Investor Day gives a dated gross margin target of 44% or more, with the full-price share of NIKE Direct disclosed; (3) the nike.com men's sale share falls below 39%, and Running Warehouse markdowns fall below 30%, after holiday 2026; (4) inventory grows at least 3 points slower than sales in Q2 and Q3 FY27.
- *More bearish:* (1) a second push-out of the Sportswear and Jordan timeline (Greater China is already guided to "extend beyond fiscal 2027", Q1 FY27 10-Q p. 20); (2) ASP negative in Q2 and Q3 FY27; (3) DICK'S or Foot Locker inventory growth staying above comps, with Nike-heavy liquidation; (4) new tariff costs showing up in the product cost line, since the IEEPA refund was one-off (FY26 10-K p. 30).

---

## Files

CSVs in `/tmp/claude-0/-home-user-nike-research-case-comp/97c520cc-64e5-53f3-8fe9-898f5b11e054/scratchpad/recovery/`:
- `nike_pb_quarterly_gm_inventory.csv`: PitchBook quarterly revenue, gross profit, GM, inventory and y/y changes, Q3 FY1984 to Q1 FY27 (gross profit from FY1990).
- `nike_pb_annual_gm_inventory.csv`: PitchBook annual history, FY1979 to FY2026.
- `nike_current_episode_quarterly.csv`: filing-fact quarterly GM, bridge lines, and inventory vs sales, Q1 FY23 to Q1 FY27.
- `nike_precedents.csv`: Section B table.
- `nike_gm_gap_fy24_to_fy26_bridge.csv`: Section E0 bridge.
- `peer_cases.csv`: Section C table.
- `indicator_dashboard.csv`: Section D table.
- `valuation_per_100bps.csv`, `valuation_scenarios.csv`, `valuation_price_implied_gm.csv`: Section E.

Scripts are in `scratchpad/rscripts_rec/`. Downloads (untrusted, parsed with `python3 -I`) are in `scratchpad/recovery_dl/`: `peers/` (RL, UA, VF 10-Ks and RL releases from sec.gov), `nke/` (older Nike filings from investors.nike.com) and `xbrl/` (data.sec.gov companyfacts).

Caveats: PitchBook quarterly gross profit for older periods is derived and may differ slightly from Nike's restated figures; the filing-cited values take precedence. Peer figures from repo notes were not re-opened here, except the RL, UA and VF 10-K passages cited by page. The scenario probabilities are judgement, not a model output.
