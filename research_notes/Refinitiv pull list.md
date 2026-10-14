# What to pull from Refinitiv (LSEG Workspace) in the morning

**Why this list exists.** The free-data hunt hit walls on a few facts that matter for the long vs short decision. A university terminal can usually get past those walls. Pull what you can, save each file as CSV or Excel into `data/university/` in the repo (or just drop them in the chat), and the next step is to test them against the eight long vs short questions.

**One caution.** I cannot see which Refinitiv modules Penn's license includes, and menu names change between Workspace versions. Treat the "where to look" hints as starting points. If a function is not in your license, skip it and tell me which one, and I will find another route.

**Rules for copying.** Keep dates as full dates. Keep the units the screen shows (USD, local currency, millions). Do not clean anything up. Raw is better.

---

## Priority 1: pulls that could change the call

### 1. Analyst estimate history for NKE (the FY28 question)
- **Why it matters:** The whole short rests on FY28 EPS of $1.65 being too high. We need to see how that number has moved and who is cutting.
- **Pull:** Consensus mean, median, high, low and number of analysts for NKE, for FY27, FY28 and FY29: EPS, revenue, gross margin, EBIT and EBIT margin. Include the history of the mean (weekly or monthly) back to Jan 2025, and the list of individual broker estimates with the date each was last changed.
- **Where to look:** Search "NKE" then Estimates (I/B/E/S). Look for "Consensus Estimates" and "Estimate Revisions" or "Broker Detail". Export to Excel.
- **Also:** StarMine SmartEstimate vs mean for NKE, if available (it weights recent and accurate analysts).

### 2. Supplier and customer map for Nike (the factory and shelf questions)
- **Why it matters:** We found that Nike's own shipments are hidden in public records. A supply-chain map shows which companies sell to Nike and how much of their sales depend on it, so we can find more suppliers to track (like Feng Tay) and more customers to read.
- **Pull:** Supply Chain relationships for NKE: suppliers and customers, with the revenue share where shown (Feng Tay, Pou Chen, Yue Yuen, Eclat, Shenzhou and others), plus each supplier's latest monthly or quarterly revenue.
- **Where to look:** Search "NKE" then Supply Chain (also called SPLC or Value Chain). Export the supplier and customer tables.

### 3. Monthly US footwear imports by country (the hard demand check)
- **Why it matters:** The Census website needs registration with an email, which I will not do on your behalf. Datastream or Economic Indicators often carry the same monthly series.
- **Pull:** US imports of footwear (HS 6402, 6403, 6404 if split out, otherwise total footwear) by value and, if available, quantity, monthly from Jan 2019 to Aug or Sep 2026. By origin: Vietnam, Indonesia, China, Cambodia, India. Also total US apparel imports.
- **Where to look:** Datastream (Excel add-in) or Economic Indicators. Search "US imports footwear" or "imports of footwear Vietnam". If neither has it, say so and I will try the USITC route.

### 4. Short interest and securities lending for NKE (the crowded short)
- **Why it matters:** We have FINRA twice-monthly short interest. Lending data shows borrow cost and how much stock is on loan, which tells us whether a squeeze is possible.
- **Pull:** NKE short interest history (shares and % of float), securities lending utilization, indicative borrow fee, shares on loan and available to lend, daily or weekly back to Jan 2025.
- **Where to look:** Search "NKE" then Short Interest or Securities Lending (sometimes under Ownership or Equity Research). Export.

---

## Priority 2: strengthens existing evidence

### 5. Peer panel in one download
- **Why it matters:** Peers are the control group for "is this Nike-specific." We built a panel by hand from filings. A clean pull lets us verify it.
- **Pull:** Quarterly revenue (reported and, if shown, currency-neutral), gross margin, inventory and EPS for ADS (adidas), PUM (Puma), ONON, DECK, 7936 (ASICS), 2020.HK (Anta), 2331.HK (Li-Ning), 1368.HK (Xtep), LULU, VFC, UAA, SKX if still listed, from Q1 2022 to the latest.
- **Where to look:** Datastream or the Excel add-in with the Worldscope or Fundamentals fields. Or Company screener then Financial Statements, export quarterly.

### 6. Forward multiples for the same peers
- **Pull:** Forward P/E (FY1, FY2), EV/EBITDA and EV/Sales for NKE and the same peers above, today and monthly for the last 3 years.
- **Where to look:** Datastream, or Estimates then Valuation, or the Excel add-in. This tests whether Nike's premium (21.5x FY28 vs about 13x) is normal or unusual.

### 7. Ownership changes
- **Pull:** NKE top 50 holders with latest and prior-quarter share counts (13F data), holder type, and any funds that exited or entered in the last 4 quarters.
- **Where to look:** Search "NKE" then Ownership (Holdings). Export.

### 8. Earnings call transcripts for retailers and peers
- **Why it matters:** We read Nike's calls and Dick's and Academy. Missing: Foot Locker (2024 to 2025), JD Sports, Hibbett, Genesco, Caleres, On, Deckers, Skechers, ASICS.
- **Pull:** Transcripts from Jan 2024 to now where Nike is mentioned. Save as text or PDF.
- **Where to look:** StreetEvents or Transcripts.

---

## Priority 3: nice to have

### 9. China sporting goods demand
- **Pull:** China NBS retail sales of sports and entertainment goods, monthly, with year-on-year growth, Jan 2023 to latest (Datastream or Economic Indicators).

### 10. News and event timeline
- **Pull:** A Nike news feed export (Jan 2026 to now) filtered for "store closures", "layoffs", "guidance", "downgrade". This helps date events precisely.

---

## Things Refinitiv will NOT solve (and who might)

- **Nike's own US shipment volumes by month.** Nike hid its name in public shipping records. Refinitiv is not the right tool. The paid shipping databases are Panjiva (S&P Global), Datamyne and Descartes. Ask Penn Libraries which of these Penn subscribes to. The exact text patterns to search for are in `data/hunt/nike_shipments/README.md` ("FOOTWEAR DIVISION OF GOODS", "OCM-CTP", notify party Expeditors, Portland).
- **Brand-share data (Euromonitor) and consumer surveys (Mintel).** Those are separate Penn Library databases, not Refinitiv. Euromonitor Passport is the one to try first: athletic footwear brand shares by country, 2019 to 2025.
- **Credit card spending by brand.** Not in Refinitiv. Skip unless Penn has an alternative-data subscription (some business schools do through Wharton Research Data Services).

---

## How to send it back
Drop the files in the chat, or save them under `data/university/` with names like `ibes_nke_estimates.xlsx`, `splc_nke.xlsx`, `short_interest_nke.xlsx`. Tell me anything you could not find. The next step is to test each against the eight questions and update the scoreboard.
