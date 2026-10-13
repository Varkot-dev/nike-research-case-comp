# Leads scan across every branch (Oct 13, 2026)

**Purpose.** A read of every branch on GitHub at the end of Oct 13, 2026 to list what is new, what it changes in the pitch, and which follow-ups nobody owns yet. Numbers are quoted from the notes named in each row, which carry the filing and page citations; nothing here is new research.

## 1. Where the work sits

| Branch | Status vs default | New since the last scan |
|---|---|---|
| `claude/wonderful-franklin-u31n4e` (default) | | `DEEP_DIVE_DEFINITIVE_TESTS.md` (Tests 1 to 5, PRs #14 and #15); notes 17 to 20 |
| `claude/gallant-ride-0plbb9` | Merges cleanly | Size-run tracker data for Oct 13 (`data/definitive/sizes/`) |
| `claude/stoic-shannon-dmkmyu` | 18 commits ahead; **conflicts** in 7 files under `research_notes/Nike decline execution vs structural/`, `reports/` and `dtc_wholesale.md` | Root-cause synthesis with 23 hypothesis notes (new: effective tax rate drift, Hispanic consumer pullback, Middle East conflict 2026, U.S. wholesale partner destocking, World Cup 2026 event shift); a slide deck in `slides/` |
| `claude/zealous-mccarthy-rj0t2h` | 20 commits ahead; **conflicts** in `CLAUDE.md`, `REPORT.md`, notes 06 and 08, `scripts/make_charts.py` | Investigations 01 to 09 including a cross-note critic review; REPORT.md 5.7 and 5.8 corrections; a mirror-only `dl.py` |

The two conflicting branches belong to other sessions and are not merged here.

## 2. New findings that change the pitch

| # | Finding | Source note | Direction |
|---|---|---|---|
| 1 | Nike's main shoe factory (Feng Tay, 83% to 86% one customer) cut in 2023, four quarters before Nike footwear fell, and leads Nike footwear growth by about one quarter (correlation 0.68 excluding COVID years). Its Q1 FY2027 revenue was -8.8%, pointing to continued weakness in Q2 FY2027. | `DEEP_DIVE_DEFINITIVE_TESTS.md` Test 1 | Short |
| 2 | The supply-cut signature (units down, price held) appears only in Greater China (units -26%) and Converse (units -34%). North America sold 2% more footwear pairs at lower ASP in Q1 FY2027. | Test 5 | Short (weakens "scarcity will restore full price") |
| 3 | Jordan retros: 2 of 113 colourways discounted on nike.com, yet Foot Locker has 2026 AJ3 and AJ4 releases 18% to 23% off, resale trades 26% to 35% below retail, and the AJ4 Rare Air has all 13 sizes in stock on day 38. | Tests 2 to 4 | Short (markdowns sit in wholesale and resale) |
| 4 | North America wholesale growth is part sell-in: about a third to a half of FY2026 growth restores FY2025 holdbacks; Foot Locker inventory +14% to +16% against sales -6.5%; channel shift is 22% of FY2026 NA wholesale growth at wholesale value. | Investigations 01 and 09 | Short |
| 5 | North America FY2026 gross margin +120 bps depends on the IEEPA refund; excluding it, -350 bps. Excluding the refund, NA EBIT margin fell 5.7 pts, the same as EMEA and APLA. | Investigations 05 and 09 | Corrects REPORT.md 5.7 |
| 6 | NIKE Direct fell $3.8B FY2024 to FY2026, about 92% NIKE Brand Digital, on traffic; store closures negligible. | Investigation 03 | Neutral (diagnosis) |
| 7 | Top-3 U.S. customer share 21% to 29%: about 3.1 pts from Direct shrinking, about 4.5 pts from JD buying Hibbett; Dick's and Foot Locker under 1 pt. | Investigation 06 | Corrects note 01 |
| 8 | Root cause ledger: Nike's own decisions explain about 65% to 75% of gross headwinds (mostly fixable), but about 45% of the log share-price fall is a sector de-rating (adidas P/E fell by about the same 52%). | stoic-shannon `00_root_cause_synthesis.md` | Long on the business, but caps the re-rating |
| 9 | Tax rate drift: 14.9% (FY2024) to a guided mid-20s for FY2027 costs about $0.14 to $0.17 of EPS. | stoic-shannon `effective_tax_rate_drift.md` | Minor short |
| 10 | Dividend not covered by FCF (0.91x FY2026, negative in Q1 FY2027); every 2017 and 2021 profit target missed; base rates show no full recovery at Nike-like valuations. | Notes 18 to 20 | Short |

## 3. Open leads nobody owns (claim in `RESEARCH_MAP.md` first)

1. **Q2 FY2027 nowcast from supplier data.** Feng Tay and Pou Chen publish monthly revenue on Taiwan's MOPS around the 10th of each month. Build a Q2 FY2027 Nike footwear revenue nowcast from September to November supplier revenue and compare it with guidance and consensus. This is a "why we differ from the market" number. Inputs exist in `data/definitive/suppliers/`.
2. **Size-run re-runs before the deadline.** The tracker re-run on the AJ1 Royal is scheduled around Oct 24 and Nov 7 (Test 3); only the Oct 24 run lands before the Nov 1 submission. Owner: Revenue streams session; confirm it is scheduled.
3. **Channel-fill unwind in FY2027.** Size the inventory placed in the top three U.S. accounts that must be worked down (Foot Locker inventory +14% to +16% vs sales -6.5%) and its revenue and margin effect on FY2027, before Dick's Q3 results (early December).
4. **What multiple to pay if the sector de-rating is permanent.** Lead 8 implies the bull case cannot assume Nike's historical multiple. Peer P/E and EV/EBIT history (adidas, Puma, Deckers, On, Lululemon) to set the exit multiple in the model.
5. **Catalyst calendar between submission (Nov 1) and finals (Nov 19).** Feng Tay October revenue (about Nov 10), dividend declaration (usually Nov 14 to 20), Investor Day (Nov 16 to 17). Prepare how the thesis updates under each outcome.
6. **REPORT.md corrections waiting on unmerged work.** Sections 5.7 (NA margin bases) and 5.8 (markdown break-even) per investigations 04 and 05, and note 01's concentration line per 06. These sit on `claude/zealous-mccarthy-rj0t2h`, which conflicts with the default branch.
