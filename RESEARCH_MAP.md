# Research map: who owns what (check before starting any research)

**Purpose.** Several Claude sessions research this repo in parallel. This file is the single register of what has been researched, what is in progress, and who owns each topic, so that no two sessions investigate the same question. It acts as the project's chief of staff.

**Last updated:** October 15, 2026, by the "Academic research" session (branch `claude/stoic-shannon-dmkmyu`), merging its lane into the default branch.

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


### Long vs short decision lane (merged Oct 15, 2026 from `claude/stoic-shannon-dmkmyu`)
| Topic | Files | One-line result | Owner |
|---|---|---|---|
| Root cause analysis, 17 hypotheses with contribution estimates | `research_notes/Nike decline root cause analysis/` (00_root_cause_synthesis.md plus about 23 notes) | Franchise oversupply, DTC overreach and China are the largest; see synthesis | Academic research session |
| Eight long vs short cruxes, scoreboard and skeptic checks | `research_notes/Long or short cruxes/00_SCOREBOARD.md` and 17 notes | Lean SHORT, low to moderate confidence; China strong, five cruxes moderate short, none long | Academic research session |
| Free-data hunt, 20 datasets with scripts and READMEs | `data/hunt/*/README.md` | Factory orders flat at about -6%, nike.com discount share flat YoY with hidden promos rising, 33 of 73 US full-price stores delisted in one week, Nike hides its name in US customs data | Academic research session |
| Thesis decision: five advocates, judges, five digs, ruling | `research_notes/Thesis decision/` | SHORT on FY28 expectations; Investor Day (Nov 16 to 17) is the decider | Academic research session |
| Deep dives D1 to D7: FY28 bridge, NA demand, EMEA and Converse, long steelman, valuation premium, dividend, Investor Day event study | `research_notes/Deep dives Oct 14/` (00_SYNTHESIS.md first) | Filing-based FY28 EPS gap only $0.09 to $0.19; premium is trough-earnings; NA is channel mix not stuffing; dividend covered by balance sheet; raised targets rally +6% day 1 | Academic research session |
| Refinitiv pull list for the user | `research_notes/Refinitiv pull list.md` | Priority 1: I/B/E/S estimate history, supply chain map, footwear imports, short interest | Academic research session |
| Decks | `slides/pptx/Nike Short Thesis.pptx` (editable), `slides/` HTML | 13-slide short deck; needs margin-first rewrite per D1, D4, D5 | Academic research session |

**Known contradictions to resolve before submission:** guidance beats (note 19 says 22 of 22 items; deck says 14 of 14 quarters; D4 says Q1 FY27 fell below the guide midpoint); NA wholesale wording (thesis_tests says mostly sell-in, D2 says channel mix plus one-quarter pulse); dividend-cut angle (note 18 and D6 agree on 0.91x cover, D6 adds years of balance-sheet runway).


### Smoking-gun hunt results (Oct 15, 2026, Academic research session)
| # | Question | Files | One-line result |
|---|---|---|---|
| G1 | Forward demand from Nike's own filings: product purchase obligations, inventory purchase commitments, endorsement obligations, FY19 to Q1 FY27 | `research_notes/Smoking gun hunt/G1_purchase_obligations.md` | Not predictive; FY25 $7.9B was a filing error (about $5B) |
| G2 | Receivables forensics: DSO, allowance for doubtful accounts, sales returns and markdown reserves vs wholesale growth, by quarter | `research_notes/Smoking gun hunt/G2_receivables_reserves.md` | No credit fingerprint in push quarters; wholesale DSO +4.5 to +9.7 days from Q3 FY26; segment AR and returns rollforward disclosures withdrawn |
| G3 | Unit volumes from Nike Impact Reports and the Nike Manufacturing Map: footwear units, factory and worker counts by country, FY15 to latest | `research_notes/Smoking gun hunt/G3_units_factories.md` | Footwear units flat vs FY19; all growth was price; ASP now falling |
| G4 | Securities class action complaints against Nike (2024 onward): confidential witness accounts on inventory, discounting and DTC, from court dockets | `research_notes/Smoking gun hunt/G4_litigation_witnesses.md` | Court dismissed 78 of 79 statements; 2022 allegations only |
| G5 | Credit market read: Nike bond yields and spreads vs peers (TRACE), CDS if available, rating agency reports | `research_notes/Smoking gun hunt/G5_credit_market.md` | Bonds price single-A, tightest in peer group; no stress |
| G6 | Web traffic and digital demand: Cloudflare Radar and Tranco domain ranks for nike.com and peers by country; app store ranks | `research_notes/Smoking gun hunt/G6_web_traffic.md` | nike.com visits -11% YoY vs peers flat to up; digital decline is demand outside EMEA |
| G7 | Innovation pipeline: USPTO and EUIPO trademark and patent filings by Nike vs adidas, On, Deckers, 2015 to 2026 | `research_notes/Smoking gun hunt/G7_ip_pipeline.md` | 2026 trademark filings at a 15-year high; supports the long case product rebuild |
| G8 | Tax and contingencies: EU state aid case on Nike's Dutch rulings, IRS and other disputes, unrecognized tax benefits, FY28 EPS exposure | `research_notes/Smoking gun hunt/G8_tax_contingencies.md` | No tax gap; Belgian customs claim (press EUR 1.5B) is the largest unmodeled item |
| G9 | Resolve the guidance-beat contradiction (22 of 22 items vs 14 of 14 quarters vs Q1 FY27 below midpoint) against the releases | `research_notes/Smoking gun hunt/G9_guidance_record.md` | 16 of 16 inside guided range; Q1 FY27 first below midpoint |
| G12 | Do sales-related reserve releases explain the FY26 beats? | `research_notes/Smoking gun hunt/G12_reserve_release.md`, `G12_check.md` | Balances and EPS arithmetic survive; "explains the beats" rejected by the skeptic (pre-announced base effect; provision vs usage not separable) |
| G10 | Belgian customs case outcome | `research_notes/Smoking gun hunt/G10_belgian_customs.md` | No judgment; merits hearing listed Nov 30, 2026 (press); EUR 1.5B unreserved; one-time EPS $0.23 to $1.16 |
| G11 | Disclosure withdrawal audit | `research_notes/Smoking gun hunt/G11_disclosure_withdrawal.md` | 16 KPI families withdrawn in 9 quarters vs about 5 in prior 24; 11 of 12 directional were deteriorating |
| Hunt | Synthesis | `research_notes/Smoking gun hunt/00_HUNT_SYNTHESIS.md` | No smoking gun; mosaic pitch, margin first; deck and REPORT.md section 11A updated |

## In progress

### Wave 3 hunt (DONE Oct 16, 2026, Academic research session; outputs in `research_notes/Wave 3/`, start with `00_WAVE3_SYNTHESIS.md`; no smoking gun; Street FY28 now near our bear case, margin argument leads)
| # | Question | Planned output |
|---|---|---|
| W1 | Management's own internal targets: 2026 proxy PSU and PSP goals (FY27 to FY29 revenue, EPS, EBIT), retention award terms, the Mar 2026 $1B 364-day facility terms and covenants | `W1_internal_targets.md` |
| W2 | CFO Denton's investor-day playbook at Lowe's and CVS: targets set, dated or not, met or missed, stock reaction | `W2_denton_playbook.md` |
| W3 | Supplier order-book guidance for 2027: Feng Tay, Pou Chen, Yue Yuen, Lai Yih, Eclat, Makalot, Shenzhou, Changshin investor conferences (Chinese, Korean) | `W3_supplier_order_guidance.md` |
| W4 | Supplier labor cuts in local-language press: Vietnam, Indonesia, Cambodia, India Nike-supplier layoffs and hiring 2025 to 2026 | `W4_supplier_labor.md` |
| W5 | China real-time nowcast: Pou Sheng monthly revenue and Topsports quarterly operational updates through Sep 2026 into Nike Q2 FY27 | `W5_china_nowcast.md` |
| W6 | Wholesale customers' Nike purchase share over time: Foot Locker, DICK'S, JD Sports, Academy, Hibbett, Genesco, Snipes, Zalando, Intersport | `W6_customer_purchase_share.md` |
| W7 | Consensus revision dynamics: FY27 and FY28 EPS revision path and breadth since Jun 2026, per-broker actions, price targets | `W7_revision_dynamics.md` |
| W8 | Product newness count: Nike, Jordan and peer launch calendars 2023 to 2026 by franchise; share of new vs retro | `W8_launch_newness.md` |
| W9 | Demand creation spend from ad transparency: Google Ads Transparency Center, Meta Ad Library, YouTube, TV ad trackers for Nike vs peers | `W9_ad_spend.md` |


### Niche-source hunt (DONE Oct 15, 2026, Academic research session; outputs in `research_notes/Niche sources/`, start with `00_NICHE_SYNTHESIS.md`; no smoking gun, base-rate margin argument is the lead)
| # | Question | Planned output |
|---|---|---|
| N1 | Brand health panel: Piper Sandler teens Fall 2025 to Fall 2026 (extends the Spring 2022 to Spring 2025 work), ACSI athletic shoes, Axios Harris Poll 100, Interbrand, Kantar BrandZ, Brand Finance, Lyst Index | `N1_brand_health_panel.md` |
| N2 | Industry experts with sell-through data: Circana public releases, Matt Powell (Spurwink), Running USA, Running Insight, SGB, Footwear News analyst columns | `N2_expert_sellthrough.md` |
| N3 | Nike's own history from books and old 10-Ks: Reebok 1986 to 1988, 1998 to 2001, 2017; time to margin and unit recovery, stock path | `N3_nike_history_analogs.md` |
| N4 | Nike subsidiary statutory accounts: Nike Korea (DART), Nike (UK) and Nike Retail (Companies House), Nike Japan (kanpo), others | `N4_subsidiary_accounts.md` |
| N5 | China e-commerce event rankings: 11.11 and 618 sportswear brand rankings on Tmall, JD, Douyin 2019 to 2026 | `N5_china_ecommerce_rankings.md` |
| N6 | Off-price channel census: Nike SKUs at TJX, Ross, Burlington, Nordstrom Rack, Saks Off 5th, Shoe Carnival, Famous Footwear via Common Crawl and call transcripts | `N6_offprice_census.md` |
| N7 | Amateur running adoption: shoe counts at major marathons and races (RunRepeat, Running Warehouse, Believe in the Run), Strava and race photo studies | `N7_amateur_running_counts.md` |
| N8 | Academic literature applied: disclosure withdrawal, guidance cessation, investor days, Mauboussin Base Rate Book; turn G9, G11 and D7 into return predictions | `N8_literature_base_rates.md` |
| N9 | Options market: implied distribution through Investor Day and finals vs D7 base rates; cost of a put or put spread | `N9_options_investor_day.md` |




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
