# Cross-branch scan, Oct 13, 2026 (evening)

**Purpose.** A full read of every Nike research source at the end of Oct 13, 2026, to find contradictions between lanes and the leads for a unique thesis. Nothing here is new research; each number is quoted from the file named, which carries its own citation. Written by the "Academic research on consumer shoe preferences" session (`claude/stoic-shannon-dmkmyu`).

## 1. What exists

| Source | Where | Merged into default (`claude/wonderful-franklin-u31n4e`)? |
|---|---|---|
| Nike SEC filings research | `claude/eloquent-feynman-cnpk76`: REPORT.md, notes 01 to 05, 14 to 21, `thesis_tests/`, `RESEARCH_MAP.md` | Yes |
| Nike revenue streams research | `claude/gallant-ride-0plbb9`: notes 11 to 13, `jordan_extracts/`, `DEEP_DIVE_DEFINITIVE_TESTS.md` | Yes, except REPORT.md Section 5.13 (10 commits) |
| Excel/Sheets modeling skill | `claude/beautiful-archimedes-6cjphp`: skill and Jordan valuation workbook | Yes |
| Nike DTC/Retail analysis | `claude/zealous-mccarthy-rj0t2h`: notes 06 to 10, `investigations/01` to `09`, CLAUDE.md rules | No (20 commits; conflicts) |
| Academic research (this session) | `claude/stoic-shannon-dmkmyu`: international research, 23-hypothesis root cause analysis, adidas and Under Armour cases, integrated report, slide deck | Partly (18 commits; conflicts) |
| "Nike's Channel Shift: Research Brief" | Claude Docs page dated Oct 12, 2026 (https://claude.ai/code/artifact/0ed37e13-86ad-44af-9383-b61dabe934b3), not in the repo | n/a |

No other Nike sessions, repositories or Google Drive files were found (cloud session list, artifact list and Drive search checked Oct 13).

## 2. Contradictions this session's work must answer

| # | This session said | Other lanes found | Source |
|---|---|---|---|
| 1 | North America "fixed": five growth quarters, record NA wholesale | NA wholesale growth is partly sell-in: 35% of FY26 growth only restores FY24 volume; Foot Locker inventory +14.1% to +15.5% vs sales -6.5% (Aug 1, 2026); top-3 accounts took $772M to $1,173M of FY26 NA wholesale growth | `investigations/01`, `09`; `thesis_tests/retailer_sell_through.md` |
| 2 | Quoted Hill: Foot Locker comps "positive for the first time in 4 years" | Foot Locker comps -4.7%, -3.4%, +0.6%, -3.6%; about $260M liquidation charges | `thesis_tests/retailer_sell_through.md` |
| 3 | Classics drag fading; supply cuts worked for AF1 and AJ1 | Units-vs-price test: the supply-cut signature appears only in Greater China and Converse; NA sells 2% more pairs at lower ASP; AJ1 resale did 22.7 pts worse than AJ3 after its cut (interval includes zero); 2026 Jordan retros sit in full size runs 4 to 10 weeks after launch | `DEEP_DIVE_DEFINITIVE_TESTS.md` Tests 3 to 5 |
| 4 | NA gross margin recovery | NA FY26 gross margin is -350 bps excluding the $965M IEEPA refund; +100 to +190 bps on a no-new-tariff basis | `investigations/05` |
| 5 | Fixable, recovery from H2 FY28 | Every 2017 and 2021 profit target missed; FCF covered 0.91x of the dividend in FY26 and was negative in Q1 FY27; EV/sales above 1.0x: 0 of 9 base-rate recoveries (Nike 1.13x) | notes 18, 19, 20 |
| 6 | Greater China mostly Nike execution | Agrees: Nike lost sell-through share while adidas GC grew +20.3% over FY25 to FY26; domestic brands ruled out as share-takers | `investigations/02` |

Rows 1 to 4 do not overturn the root-cause ranking (the Consumer Direct strategy is still the root), but they do weaken the claim that North America proves the fix is working.

## 3. Leads for a unique thesis (none claimed in RESEARCH_MAP.md yet)

1. **"Where the markdowns went."** nike.com holds Jordan prices (2 of 113 retro colourways discounted) while Foot Locker sells 2026 retros 18% to 24% off and resale trades below retail. Test whether Nike moved discounting off its own P&L into partners' inventory, which flatters Nike's reported recovery and must reverse in FY27. Data: Dick's Q3 2026 (early Dec), Foot Locker inventory vs $1,822M to $1,850M, Q2 FY27 NA wholesale vs about $3,550M.
2. **Factory nowcast.** Feng Tay (83% to 86% Nike) leads Nike footwear by about one quarter (correlation 0.68); Q1 FY27 was -8.8%. Build a Q2 FY27 forecast from Sept to Nov monthly revenue on MOPS. Inputs: `data/definitive/suppliers/`.
3. **Dividend as the catalyst.** Payout 121% to 143% of guided EPS; S&P cut to A, negative outlook (Oct 5); "consecutive years" streak language dropped. The declaration (Nov 14 to 20) falls between submission (Nov 1) and finals (Nov 19).
4. **Reconcile "fixable" with "priced in."** The business is about two-thirds Nike-specific and fixable (this session; `competitor_benchmarks.md`), yet the price implies a 12% to 14% FY31 EBIT margin and about 45% of the stock fall is a sector de-rating. A thesis that the fix is real but already in the price is distinct from both the bull and bear readings.
5. **Jordan as the hidden downside.** Demand fell before the supply cut (search -76% since 2021); valuation puts Jordan at $2.32 to $5.96 a share against about $5.68 priced in.

## 4. Housekeeping needed before the pitch

- Merge `claude/stoic-shannon-dmkmyu` and `claude/zealous-mccarthy-rj0t2h` into the default branch (both conflict; owners must resolve).
- Correct this session's report and deck for rows 1, 2 and 4 above.
- Fix the Jordan FY24 figure in the data ($8,701M per `investigations/08` and the default branch).
