# Check: did Nike really close 33 of 73 US in-line stores in July 2026?

Prepared 2026-10-14. Labels: OPENED = I fetched and read the page, record or filing in this session. OPENED (repo) = in this repo from an earlier pull, not re-fetched. SNIPPET = search-result title or summary only. [my arithmetic] = computed by me. [estimate] = my estimate, not from a source.

Files: `data/hunt/stores/closure_verification.csv` (one row per store), built by `data/hunt/stores/scripts/build_closure_verification.py` from `raw/atp_delisted_33_2026-07-18_props.json` and Nike's own store records saved in `raw/nike_api_closures_2026-10-14/`.

## 1. Verdict

**The 33 closures are real. All 33 are confirmed closed, none were relabeled, moved to another category or dropped by a feed change.**

| Status | Stores |
|---|---|
| Confirmed closed | **33** |
| Reclassified (factory, outlet, partner, Style, Unite, other concept) | 0 |
| Still open | 0 |
| Unknown | 0 |

How strong the confirmation is for each store:

| Basis | Stores | Which |
|---|---|---|
| Nike's own store record shows a closing date and no hours, plus an independent news report or listing naming the store | 22 | Pasadena, San Jose (Santana Row), Cary (Fenton), Brooklyn (Williamsburg), Dedham (Legacy Place), Westlake (Crocker Park), Lexington (Fritz Farm), Naperville, Kansas City (Country Club Plaza), Southlake, Carlsbad (La Costa), Louisville (Oxmoor), Bethesda Row, Scarsdale, Colorado Springs (Briargate), Tampa (Hyde Park Village), Manhasset, Long Beach (2nd & PCH), The Woodlands (Market Street), Atlanta (Ponce City Market), Alpharetta (Avalon), Hoboken |
| Nike's record plus the mall directory no longer listing Nike | 5 | Birmingham (The Summit), Chestnut Hill, Tigard (Bridgeport Village), Natick, Minnetonka (Ridgedale) |
| Nike's record only | 6 | Lynnfield, Cranston, South Windsor, El Segundo, Hingham, Glendale WI (Bayshore) |

Every one of the 33 was a **Nike Well Collective** door (the 2023 rebrand of Nike Live), the small neighborhood format of about 4,000 sq ft (CRE Daily, OPENED). Nike's flagships, Rise stores, House of Innovation, Jordan World of Flight and all factory and clearance stores were untouched.

## 2. The decisive evidence: Nike's own store records

The nike.com/retail store pages load their data from `https://api.nike.com/store/store_locations/v1/<store id>`. I fetched that record for each of the 33 ids on 2026-10-14 (OPENED, saved in `raw/nike_api_closures_2026-10-14/`):

- **32 records carry `"closingDate": "2026-07-13"` and one (Avalon, Alpharetta) `"2026-07-14"`.** All 33 have empty regular hours on all seven days.
- All 33 still read `facilityType: NIKE_OWNED_STORE`, `storeConcept: Well Collective`. Nike's system shows them as closed Well Collective stores, not as factory, partner or other-concept doors.
- Control: the 40 US in-line stores still in the feed have **no** closing date. All 15 US in-line doors that left the feed earlier (Jan 2025 to Jun 2026) have a closing date, 14 of them within about two weeks of their last crawl (for example San Ramon 2026-05-03, Berkeley 2026-05-30, Pinecrest 2026-06-14). So the closing-date field tracks real exits. The 33 were still in the 2026-07-18 crawl (collected 2026-07-20) a week after their closing date, so the feed lags by about a week.

## 3. Was it a relabel or a feed change? No.

1. **No category rose.** In the ATP crawls of 2026-07-18 and 2026-07-25 the US Nike Factory Store count stayed at 183 and Clearance at 29 (`nike_locator_weekly_counts.csv`, OPENED (repo)). The whole worldwide feed fell from 4,378 to 4,345, exactly 33, with **zero new ids** that week [my arithmetic].
2. **No reappearance.** None of the 33 ids is in any of the 11 crawls from 2026-07-25 to 2026-10-03, or in Nike's static feed fetched 2026-10-14 (`raw/nike_static_2026-10-14.json.gz`) [my arithmetic].
3. **No replacement nearby.** In the 2026-10-14 feed there is no Nike door of any type (owned, factory, partner) within 3 km of any of the 33 sites, and none of their phone numbers is reused [my arithmetic]. The only Nike in the Natick Mall directory is a shop inside Macy's.
4. **No feed format change on 2026-07-25.** Both ATP runs read the same source (`nslp-directory.nike.com/store-locations-static.json`), carry the same property keys and were collected at normal times (2026-07-20 05:48 and 2026-07-27 03:48 UTC, OPENED). The 2026-10-14 feed has 252 US owned doors: 183 factory, 29 clearance, 19 Well Collective, 11 Rise, 8 Beacon, 1 House of Innovation, 1 World of Flight [my arithmetic].

## 4. What the press and Nike said

| Source | Date | What it says | Label |
|---|---|---|---|
| TheStreet, via Yahoo Finance | 2026-07-18 | Cary (Fenton) and San Jose (Santana Row) closed; Fenton center: store "was originally expected to remain open through July 31 but closed earlier than planned as part of Nike's broader national retail strategy" | OPENED |
| Hoboken Girl | 2026-07-16 | Hoboken store "permanently closed" per Google and Nike's locator | OPENED |
| Community Impact | 2026-07-17 | Market Street officials confirmed July 16 that Nike (Ste. 885) is "no longer operating" | OPENED |
| TheStreet (republished on author's site) | 2026-07-24 | 11 July closures by address: San Jose, Tampa, Atlanta, Alpharetta, Naperville, Louisville, Kansas City, Bethesda, Hoboken, Cary, The Woodlands | OPENED |
| Whatnow Boston | 2026-08-14 | ALO "will take over the former Nike space at 222 Legacy Place" (Dedham) | OPENED |
| Retail Dive | 2026-08-19 | "That location in Melrose, along with at least 14 others, are now permanently closed", across 12 states | OPENED |
| Fast Company | Aug 2026 | At least 24 Well Collective closures in 12 states | SNIPPET (403). Its city list is reproduced by Maquina do Esporte, OPENED |
| Peru Retail | 2026-09-04 | Federal Realty said Santana Row exit was "not a decision specific to this market or property" | OPENED |

**Why the press counts (15, 24) are lower than 33:** the press counted what reporters could see. Fast Company's 24 (as listed by Maquina do Esporte) includes 18 of the 33 plus 6 doors that Nike's records show closed earlier (Berkeley, San Ramon, Marlton, Shrewsbury, Woodcliff Lake, and a New York door). Retail Dive's 15 includes the original Melrose store, which is not among the 33. **Thirteen of the 33 are in none of the national closure lists** (TheStreet, Fast Company, Retail Dive): Lynnfield, Dedham, Chestnut Hill, Natick and Hingham (MA), Cranston (RI), South Windsor (CT), Westlake (OH), Birmingham (AL), Tigard (OR), Minnetonka (MN), Glendale (WI) and El Segundo (CA). Only two of these have their own local evidence (the Dedham re-leasing story and a 'Permanently closed' listing for Westlake).

**What Nike said.** Nike has made no store-specific announcement and gave no count.
- Spokesperson to Retail Dive (OPENED): "Like all retailers, we regularly evaluate our fleet and make adjustments across our marketplace to better align to our strategy for growth, including elevating stores and streamlining our physical retail footprint ... This is part of our work to create Nike's future marketplace." Nike "did not address questions about ... whether this was the extent of the closures."
- Elliott Hill, Q4 FY26 call, 2026-06-30 (transcript in `data/hunt/earnings_calls/transcripts/Q4FY26.txt`, OPENED (repo)): "Over time, we will continue to rezone and elevate our fleet and close the doors that are no longer aligned to our strategy." The closing dates fall 13 days after this call.
- **Q1 FY27 (quarter to 2026-08-31):** the earnings release (8-K Ex. 99.1, filed 2026-10-01), the 10-Q (filed 2026-10-02) and the official call transcript (2026-10-01, Nike IR PDF) do **not** mention US store closures, Well Collective, a store count, lease impairments or exit costs (all OPENED). The 10-Q gives "NIKE store sales were $2.3 billion for the first quarter of fiscal 2027", down 5%.

**WARN notices.** No Nike WARN notice covers these stores. The California WARN report for 2026-07-01 to 2026-10-07 has no Nike row (`data/hunt/hiring/raw/warn_states/ca_warn_current.xlsx`, OPENED (repo)). The repo's WARNTracker pull has no Nike notice after Jan 2026. That fits small stores, which fall below WARN headcount thresholds. Their absence is not evidence the stores stayed open.

## 5. Compared with the 10-K store count

- FY26 10-K (filed 2026-07-15, p. 2): **75** US NIKE Brand in-line stores at 2026-05-31, "including employee-only stores" (`data/nike_filing_facts.csv`, OPENED (repo)). The locator showed 73 in July. The gap of 2 is most likely the employee stores, which are not on the public locator.
- In Nike's Q1 FY27 (Jun 1 to Aug 31, 2026), Nike's records show **34** US in-line closures: Pinecrest (2026-06-14) plus these 33. 34 / 75 = **45%** [my arithmetic]. On the locator base it is 33 / 73 = 45.2% [my arithmetic].
- Implied US in-line count at 2026-08-31: about 41 (75 minus 34), versus 40 on the locator [my arithmetic]. The 10-Q gives no count, so this will be checked only in the FY27 10-K (about July 2027).
- Over a longer window: the locator showed 82 US in-line doors in Dec 2025 and 40 in Oct 2026 (`nike_locator_weekly_counts.csv`). The Well Collective concept went from 52 to 19 US doors in July 2026 alone (-63%) [my arithmetic].
- Against the whole US fleet the cut is much smaller: 33 of 347 US stores in the 10-K (9.5%), or 33 of 287 Nike-brand US stores excluding Converse (11.5%) [my arithmetic].

## 6. Is "Nike cut 45% of its US full-price stores in one quarter" safe?

**The numbers hold, but the wording as written is not safe.** Problems:
1. "Full-price stores" reads as a share of full-price **sales**. These were Nike's smallest US doors, so 45% of doors is far less than 45% of in-line revenue (section 7).
2. It hides that every closed store was a single small format (Well Collective). The flagships, Rise and House of Innovation stores all remain.
3. Nike never announced a number. The count comes from Nike's own store records and locator, not a Nike statement, and press reports give 15 and 24.

**Safe wording (use this):**

> "In July 2026 Nike closed 33 US stores in one week, all small Nike Well Collective neighborhood doors. That cut the US in-line (non-factory) stores on its store locator from 73 to 40, about 45% of the count. Nike's own store records date 32 of the closures to July 13 and one to July 14. Nike called it routine fleet management and did not give a number. Press reports counted at least 15 to 24. Nike's flagships, Rise and House of Innovation stores and its 212 factory and clearance stores were not affected."

Short form for a slide: **"July 2026: Nike closed 33 of its 73 US in-line stores (45% of the count), all small Well Collective doors (Nike store records; locator)."**

Do not say: "45% of US stores" (it is 9.5% of all US stores), "45% of full-price sales", "Nike announced 33 closures", or "in Q1" without saying Nike did not disclose it in Q1 filings.

## 7. What it means financially

No source gives revenue for these doors. Nike does not break out Well Collective, and no article or filing gives sales per door. The numbers below are my bounds, not sourced figures.

- **Upper bound [my arithmetic].** Q1 FY27 NIKE store sales were $2.3B (10-Q), about $9.2B a year, across about 874 Nike-brand owned stores (988 total in the FY26 10-K less 114 Converse). That is about $10.5M per store per year. At that average, 33 doors would be about $350M a year. This overstates, because the average includes flagships and 15,000+ sq ft factory stores.
- **Plausible range [estimate].** At $2M to $5M a year for a 4,000 sq ft door, 33 doors are about **$65M to $165M of annual revenue**: about 0.8% to 1.9% of North America NIKE Direct (Q1 FY27 NA Direct $2,146M, about $8.6B annualized, 10-Q Note 9) and about 0.15% to 0.35% of Nike revenue [my arithmetic].
- **Reading.** This is a small cost cut that also signals strategy: Nike is retreating from the owned neighborhood format it planned to grow to 200 doors in 2020 (Retail Dive) and leaning on wholesale partners (for example the Foot Locker Crenshaw Rec store). It is not a large revenue event. Some sales will move to nearby Nike doors, partners and digital, so the net revenue loss is below the gross figure. The 10-Q discloses no lease impairment or exit cost for the closures. They may sit inside the "Pace" program charges (about $0.3B in FY27, mostly employee costs), but that is not stated.
- **For the pitch.** Use this as evidence of how Nike is managing its channels (owned retail shrinking toward flagships, wholesale rebuilding), not as a sales-collapse signal. It does not move FY27 estimates materially.

## 8. Limits

- web.archive.org was blocked (connection reset), so no archived store pages were checked. Yelp returned 403; the Yelp "CLOSED" titles for Long Beach and Crocker Park are SNIPPET only.
- Mall-directory absence (5 stores) is weaker than a news report; the Nike record carries those rows.
- The ATP diff and Nike API records were pulled 2026-10-14. The API is undocumented and could change.
