# Research map: who owns what (check before starting any research)

**Purpose.** Several Claude sessions research this repo in parallel. This file is the single register of what has been researched, what is in progress, and who owns each topic, so that no two sessions investigate the same question. It acts as the project's chief of staff.

**Last updated:** October 13, 2026, by the "Nike SEC filings research" session (branch `claude/eloquent-feynman-cnpk76`).

## Protocol (every session, every time)

1. **Before researching anything**, read this file. If the question is listed under *Done* or *In progress*, do not research it again. Build on the existing note instead, and say which note you are extending.
2. **To start new research**, add a row under *In progress* (topic, the exact question, your session and branch, planned output path) and get that row onto the default branch (`claude/wonderful-franklin-u31n4e`) in a small PR **before** launching agents. If another session already claimed the topic, pick something else or coordinate.
3. **When you finish**, move the row to *Done*, add the output file paths and a one-line result, and merge through a PR.
4. **Boundaries matter.** If your question touches a topic another session owns, state the overlap in your note and cite their file rather than redoing it.
5. Keep entries short. The notes hold the detail.

## Sessions and their lanes

| Session (title in Claude Code) | Branch | Lane |
|---|---|---|
| Nike SEC filings research | `claude/eloquent-feynman-cnpk76` | Filing dataset and citations; channel split data; thesis tests (retailers, competitors, valuation, marketing, say vs do, consumer alt data, marketplace pricing, review tone); discounting causes and recovery; insiders and flows; capital and dividend; management track record; base rates |
| Academic research on consumer shoe preferences | `claude/stoic-shannon-dmkmyu` | Root-cause analysis of the decline (17 hypotheses with contribution estimates); execution vs structural report; adidas and Under Armour turnaround cases; academic literature |
| Nike DTC/Retail analysis | `claude/zealous-mccarthy-rj0t2h` | Region and channel profitability; channel margin test; Converse; new products; investigations 01 to 08 (sell-in vs sell-through, Greater China collapse, NIKE Direct decline, markdown depth, segment gross margins, customer concentration, footwear vs apparel) |
| Nike revenue streams research | `claude/gallant-ride-0plbb9` | Revenue streams; Jordan Brand thesis and valuation; definitive tests (supplier factory output, time to markdown, size runs, resale panel, units vs price) |
| Excel/Sheets modeling skill | `claude/beautiful-archimedes-6cjphp` | Excel modeling skill; Jordan valuation workbook and tornado (merged in PR #9) |

## Done (on the default branch unless noted)

### Foundations
| Topic | Files | Owner |
|---|---|---|
| Filing-cited fact base (6,270 facts, FY2019 to Q1 FY2027) and data pack | `data/nike_filing_facts.csv`, `research_notes/04_financial_data_pack.md`, `scripts/sec_pipeline/` | SEC filings session |
| Main report and charts | `REPORT.md`, `charts/`, `scripts/make_charts.py` | Shared (edit through PRs) |
| Leadership, board, departures, Denton and Ewing | `research_notes/01` to `03`, `DEEP_DIVE_DENTON_EWING.md`, `data/people_events.csv` | SEC filings session |
| Channel split by region and quarter | `data/nike_channel_split.csv`, `research_notes/05_channel_split.md` | SEC filings session |
| Region margin, products, Converse, channel margins | `research_notes/06` to `10`, `data/nike_region_profitability.csv` | DTC/Retail session |
| Revenue streams; Jordan thesis and valuation | `research_notes/11` to `13`, `research_notes/jordan_extracts/` | Revenue streams session |
| Profit bridge and thesis scorecard | `research_notes/14_profit_bridge_and_thesis_scorecard.md` | SEC filings session |
| Excel modeling skill; Jordan valuation workbook | `.claude/skills/excel-modeling/`, `data/valuation/jordan_valuation.xlsx`, `scripts/jordan_valuation_xlsx.py` | Excel session |

### Thesis tests (`research_notes/thesis_tests/`)
| Question | File | One-line result | Owner |
|---|---|---|---|
| Is NA wholesale growth sell-through or sell-in (retailer filings)? | `retailer_sell_through.md` | Mostly sell-in except DICK'S own stores | SEC filings session |
| Nike vs 13 peers | `competitor_benchmarks.md` | About two-thirds company-specific | SEC filings session |
| Consensus, short interest snapshot, multiples, reverse DCF | `consensus_and_valuation.md` | Price implies 11 to 14% steady-state EBIT margin | SEC filings session |
| Does the marketing step-up pay off? | `marketing_payoff.md` | Unlikely without product | SEC filings session |
| Say vs do on the wholesale turnaround | `say_vs_do_execution.md` | Real action; December 2026 deadline slipped | SEC filings session |
| Consumer interest (search, pageviews, apps) | `consumer_interest_altdata.md` | U.S. bottoming; global still losing to adidas | SEC filings session |
| Marketplace pricing and shelf share | `marketplace_pricing_and_shelf_share.md` | Discounting elevated; running markdowns 49% | SEC filings session |
| Review tone (Jin 2023) | `review_tone_jin2023.md` | Not a reliable predictor for Nike | SEC filings session |

### Discounting
| Question | File | Owner |
|---|---|---|
| Why Nike discounts (quarterly bridge, inventory, reserves) | `research_notes/15_why_nike_discounts.md`, `data/discount/` | SEC filings session |
| Will full price recover (precedents, peers, dashboard, value) | `research_notes/16_full_price_recovery.md`, `data/recovery/` | SEC filings session |

### Root causes and turnarounds (`research_notes/Nike decline root cause analysis/`, `Nike decline execution vs structural/`, `Gulden and Plank turnarounds vs Nike/`, `reports/`)
On the default branch: franchise oversupply, DTC and wholesale, the execution vs structural report and its six supporting notes, adidas and Under Armour turnarounds. **On `claude/stoic-shannon-dmkmyu`, not yet merged:** apparel and women, challengers and taste, China, culture and demographics, digital and tech, EMEA/Converse/Jordan, governance and incentives, innovation drought, macro and COVID cycle, marketing shift, org and talent, peer differential, pricing and discounting, tariffs and costs, timeline forensics, valuation vs business. Owner: Academic research session.

### Investigations (`research_notes/investigations/`, on `claude/zealous-mccarthy-rj0t2h`, not yet merged)
01 NA sell-in vs sell-through; 02 Greater China collapse; 03 NIKE Direct decline; 04 Direct markdown depth; 05 NA gross margin; 06 U.S. customer concentration; 07 segment gross margins (in revision); 08 footwear vs apparel. Owner: DTC/Retail session.

### Capital, flows and management
| Question | Files | One-line result | Owner |
|---|---|---|---|
| Is the dividend covered; debt, ratings, buybacks, cut precedents | `research_notes/18_capital_and_dividend.md`, `data/capital/`, `scripts/capital/` | FCF covered 0.91x of dividends in FY2026 and is negative in Q1 FY2027; net cash only about $0.5B; streak language dropped from the last two releases | SEC filings session |
| Insiders, Knight/Swoosh, 13F, short interest, options | `research_notes/17_insider_and_institutional_flows.md`, `data/flows/`, `scripts/flows/` | Mixed: $9.1M of director buys (all under water), no Knight sales; short interest 14.5M (Dec 2023) to 99.2M shares (Sep 30, 2026); options imply about 7% earnings move | SEC filings session |
| Management track record and savings audit | `research_notes/19_management_track_record.md`, `data/trackrecord/`, `scripts/trackrecord/` | Every 2017 and 2021 profit target missed; Hill beat 22 of 22 quarterly guides but both dated milestones slipped; the $2B savings plan was never scored and leaves the 10-Ks after FY2024 | SEC filings session |
| Base rates after 70%+ drawdowns in large consumer brands | `research_notes/20_base_rates.md`, `data/baserates/`, `scripts/baserates/` | Nike-like episodes bought at -80%: median +69% at 3 years but only +10% vs S&P 500; full recovery 10 of 27; entry EV/sales <= 1.0x separated recoveries (6 of 11 vs 0 of 9); survivorship bias inflates all figures | SEC filings session |

## In progress

| Topic and exact question | Owner session (branch) | Planned output | Started |
|---|---|---|---|
| Definitive tests: supplier monthly output, time to markdown, size runs, resale panel, units vs price | Revenue streams (`claude/gallant-ride-0plbb9`) | `DEEP_DIVE_DEFINITIVE_TESTS.md` | Oct 13 |
| Consistency audit across the repo | Revenue streams (`claude/gallant-ride-0plbb9`) | (per that session) | Oct 13 |

## Open topics nobody owns yet (claim one before starting)
Leads from the Oct 13 scan of every branch are listed in `research_notes/21_leads_scan_oct13.md` (section 3):
- Q2 FY2027 footwear nowcast from Feng Tay and Pou Chen monthly revenue.
- FY2027 channel-fill unwind at the top three U.S. accounts.
- Exit multiple if the sector de-rating is permanent (peer multiple history).
- Catalyst playbook for Nov 1 to Nov 19 (supplier October revenue, dividend declaration, Investor Day).
- The pitch itself: thesis decision memo, 10-page report, 15-slide deck (needs every lane's results).
- The full three-statement Excel model for the submission (use the merged skill in `.claude/skills/excel-modeling/`).
- Sum-of-the-parts and strategic options (Converse sale, Jordan) beyond the existing Jordan valuation.
- University database pulls (Euromonitor brand shares, Mintel consumer surveys, Bloomberg, I/B/E/S): waiting on the user.
