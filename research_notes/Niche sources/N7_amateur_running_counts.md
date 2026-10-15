# N7: What everyday and sub-elite runners actually wear (shoe counts, 2018 to 2026)

Prepared 2026-10-15. Data: `N7_amateur_running_counts.csv` (same folder, 73 rows; every row has a URL, tag and note). Extends `research_notes/Long or short cruxes/running_sellthrough.md` (retail and review proxies) and `data/hunt/marketing_athletes` (elite podiums). It does not repeat them.

Tags: OPENED = page fetched and read this session (the fetch tool summarises the page, so numbers are as the summary printed them); SNIPPET = search-result summary only, not opened; DERIVED = my arithmetic, shown; REPO = data already in this repo.

## 1. Verdict

**No smoking gun. The one question asked, "does Nike's 2025 to 2026 running recovery show up in what runners wear?", gets a defensible answer: no, in every dataset that covers the period.** Nike's share of what runners wear fell or was flat in each series that has a post-mid-2025 reading, while Nike reports double-digit running growth for six straight quarters. The two facts can both be true (see section 5), but the wearer data give the LONG case no support, and the biggest series (Hakone) is a falling line that has not turned.

| Series | Last two readings | Nike change | Sample | Tag |
|---|---|---|---|---|
| Hakone Ekiden, collegiate sub-elite runners | Jan 2025 23.3% (49 of 210), Jan 2026 16.7% (35 of 210) | -6.6 pts, -14 runners | 210 runners, 21 teams | OPENED |
| Running USA survey, favorite racing shoe | 2025 15.2% (derived), 2026 11.0% | -4.2 pts (-420 bp, printed) | 11,700 (2026), 12,700 (2025) | OPENED |
| Running USA survey, favorite training shoe | 2025 8.4% (derived), 2026 6.4% | -2.0 pts (-200 bp, printed) | same | OPENED |
| Comrades (South Africa ultra), share of field | 2024 16%, 2025 13% | -3 pts | n not stated | OPENED |
| r/RunningShoeGeeks mention share (REPO) | Jun to Sep 2025 20.9%, Jun to Sep 2026 20.3% | -0.6 pts, flat | tagged posts | REPO |
| Strava logged-shoe rank | 2025: ASICS 1st, Nike 2nd, Hoka 3rd; Pegasus fell from 1st (2024) to 2nd | rank down | Strava global, n not published | OPENED |
| Hakone qualifier (Yosenkai), Oct 2025 | Nike 3rd in top 100 behind ASICS and adidas; Nike share 62.7% to 46.0% in the two earlier qualifiers | falling | 495 to 499 runners (Oct 2025) | OPENED, SNIPPET |

Nothing I could find has Nike up. The one series where Nike is first (Running USA with MarathonFoto race photos: Nike 21.3% of 101,414 finishers; 31.8% of full-marathon finishers) covers races up to November 2024, so it describes the level before the recovery and cannot test it. It is not repeated for 2025 or 2026 in anything free.

## 2. Hakone Ekiden: the longest and best-documented count (OPENED)

Alpen Group counts the shoes of all starters (210 or 230) every January; Nikkei, Bunshun, WWD Japan, PRESIDENT Online and fashionsnap republish it. Sources in the CSV.

| Race (Jan) | n | Nike | adidas | ASICS | Puma | Other |
|---|---|---|---|---|---|---|
| 2018 (94th) | 230 (DERIVED, 23 teams x 10) | 58 = 25.2% | 35 = 15.2% | 54 = 23.5% | n/a | Mizuno 37, NB 26 |
| 2019 | 230 | 95 = 41.3% | 39 = 17.0% | 51 = 22.2% | n/a | Mizuno 24, NB 21 |
| 2020 | n/a | 84.3% | n/a | n/a | n/a | |
| 2021 | 210 | 201 = 95.7% | 4 = 1.9% | 0 | n/a | |
| 2022 | 210 | 73.3% (154, DERIVED) | n/a | 11.4% (24, DERIVED) | n/a | |
| 2023 | 210 | 130 = 61.9% | 38 = 18.1% | 32 = 15.2% | 7 = 3.3% | |
| 2024 | 230 | 98 = 42.6% | 42 = 18.3% | 57 = 24.8% | 20 = 8.7% | Mizuno 5, On 3, HOKA 2 |
| 2025 | 210 | 49 = 23.3% | 76 = 36.2% | 54 = 25.7% | 25 = 11.9% | On 3 |
| 2026 | 210 | 35 = 16.7% | 75 = 35.7% | 60 = 28.6% | 31 = 14.8% | On 3, NB 3, Mizuno 2, HOKA 1 |

Arithmetic [DERIVED]: Nike runners 201 (2021) to 35 (2026) = -166, -82.6%; share -79.0 pts. 2025 to 2026 the 14 Nike runners lost went to ASICS +6, Puma +6, New Balance +2, Mizuno +1, HOKA +1, offset by adidas -1 and Brooks -1 (sums to 14). adidas is flat; the 2026 loser-winner pairs are ASICS and Puma, not adidas.

Significance [DERIVED]: 2025 to 2026 Nike drop is z = -1.7 treating runners as independent (SE 3.9 pts), so on its own not significant. Runners are not independent: shoes are chosen largely by team (21 teams), so the effective sample is closer to 21 than 210. The 2024 to 2026 drop (42.6% to 16.7%, z = -6.2 even before adjustment) and the 2021 to 2026 drop are large enough to survive that. Read the one-year step as direction only.

**Alternatives for the Hakone decline, and what the data say**

| Explanation | Test | Result |
|---|---|---|
| A. Competitors reached product parity, so teams stopped using Nike by default | 2021: ASICS 0 and adidas 1.9% although both sponsor teams, i.e. sponsored teams wore Nike anyway (OPENED, gendai). 2022 to 2026 ASICS 11.4 to 28.6% as Metaspeed shoes arrived | Survives. Fits the timing: the 2021 Nike peak is the high point of a technology gap. |
| B. Sponsor contracts, not shoe choice | Tokai 100% Nike in the Oct 2025 qualifier; Nike has five sponsored advancing schools (OPENED, note.com). Teams switch with contracts | Survives, cannot be separated from A. A switch of a few teams moves 10 to 30 runners. |
| C. Nike supply cut to this segment | No count of Nike allocation to teams in any source | Open. |
| D. Hakone is one race, not the market | Section 3 and 4 give the same sign for the US survey and Comrades | Partly ruled out for direction, not for magnitude. |

What would decide A versus B: the sponsor list per team per year (Nikkei publishes the sponsor table, `xtrend.nikkei.com/atcl/contents/18/00921/00048/`, SNIPPET) joined to the runner counts. Not done here.

## 3. US and global race and survey data

**Race photos (best amateur measure, one vintage).** Running USA with MarathonFoto and Greenfly AI, races up to Nov 2024, 101,414 finishers with bib and shoe read: Nike 21.3%, Brooks 16.5%, Saucony 12.6%, ASICS 12.5%, HOKA 12.1%, New Balance 7.4%, adidas 5.0%, On 3.7%, Mizuno 1.7%, Altra 1.6% (OPENED: Substack and a Thai daily citing the report; the report itself costs $199 and was not bought). Full marathon only: Nike 31.8%, Saucony 17%, Brooks 10.8% (OPENED, Thai daily; secondary). Brooks leads at the shorter distances. Nike skews young. So Nike's share is highest exactly where it sells racing shoes (marathon) and lowest in the everyday 5K to half-marathon field.

**Survey of what runners say they prefer.** Running USA Global Runner Survey, favorite brand (self-selected online panel, about 90% US):

| Brand | 2024 racing (n=7,400+) | 2025 racing (derived) | 2026 racing (n=11,700) | 2026 training | 2026 YoY racing | 2026 YoY training |
|---|---|---|---|---|---|---|
| Brooks | 19 | 20.2 | 21.9 | 24.7 | +170 bp | +90 bp |
| ASICS | 12 | 13.5 | 15.1 | 17.2 | +160 | +80 |
| Saucony | 12 | n/a | 13.5 | 12.0 | n/a | n/a |
| Nike | 15 | 15.2 | 11.0 | 6.4 | -420 | -200 |
| HOKA | 11 | 11.8 | 10.5 | 11.0 | -130 | -170 |
| adidas | 8 | 4.4 | 5.9 | 5.4 | +150 | +140 |
| On | n/a | 2.4 | 2.1 | 2.2 | -30 | -70 |

(2025 values = 2026 value minus the printed basis-point change [DERIVED]. 2026 article published 2026-10-14, sgbonline, OPENED. adidas 2024 to 2025 is not consistent with the 2024 table because the 2024 table is a different, smaller sample; do not chain 2024 to 2025.) Nike is the largest decliner in both categories and lost more than HOKA, the other decliner. Standard error on 11.0% at n=11,700 is 0.29 pts, so the -4.2 pts is statistically large, but the panel is Running USA's mailing list and social reach, skewed to run-specialty shoppers, and Nike was absent from run specialty until 2026 (REPO, Confluence: Nike 0.00% of run-specialty sales H1 2025, 1.43% 2026 YTD).

Other consumer surveys, for completeness: RunningShoesGuru, Oct 2024, n=794: Nike named favorite by 95 (12.0%), considered by 292, purchased by about 182; stated future-buyer count 71 vs 95 favorites (-25%) (OPENED). Running USA 2022: Nike 24% multi-select, n>5,000 (SNIPPET); 2016: Nike 9% of last purchase, n=10,000 (SNIPPET). These methods differ and are not chained.

**Strava (logged gear, global).** Mid-year 2025: ASICS most-logged brand, then Nike, then HOKA; Brooks first in the US (OPENED, sgbonline, press.strava.com). Year in Sport 2025: ASICS Novablast 1st, Nike Pegasus 2nd, HOKA Clifton 3rd; first time Nike, HOKA or a carbon shoe did not take the top spot (OPENED). No shares published; a "27%" ASICS figure from a stats site is unverified and not used. The 2025 readings predate the revenue recovery; Strava's 2026 mid-year report was not found.

**Comrades Marathon (South Africa, 89 km, Running Mann census of finishers).** Nike 20% (2022), 16% (2024), 13% (2025); adidas 11%, 16%, 22%; ASICS about 33% in 2025; New Balance 11% (OPENED). Basis (finishers vs medallists) is ambiguous in the post; total n not given; Nedbank, a Nike-shod club, inflates Nike at the front. Direction is unambiguous.

**Reddit.** r/RunningShoeGeeks share of brand mentions is flat for Nike (20.0%, 20.9%, 20.3% in Jun to Sep 2024, 2025, 2026) while adidas went 14.9 to 28.7% (REPO, `running_sellthrough`). Mentions measure enthusiasm, not wear.

**Triathlon and trail.** Kona whole-field counts (Shoe Ranger / LAVA) stop at 2018: HOKA 17.7%, ASICS 11.9%, Saucony 11.2%, On 7.9%, adidas 7.4%, Brooks 6.3% (OPENED, podiapaedia). Nike was 14.9% in 2018 per a search summary (SNIPPET). Nothing for 2019 to 2025 at whole-field level, only pro run splits. Western States 2025: Nike 6.3% of the field (SNIPPET). Neither bears on road recovery.

**Elite-adjacent, kept only for contrast.** Atlanta 2020 Trials 404 of 565 pairs Nike (71.5%, SNIPPET); NYC 2023 top 30 Nike 10 (33%) (OPENED); London 2026 championship start zone: Reuters says Adidas and Puma Nitro Elite were common and Nike Alphafly and Vaporfly "few and far between" (observation, not a count; OPENED).

## 4. Comparison with reported running growth (company data)

Running growth in the latest quarter, from REPO `evidence_summary.csv` and the earnings notes: Nike Running double digits (sixth straight quarter, Q1 FY27 call); ASICS North America +33.8%; adidas running +28%; Brooks H1 +14% (Americas +9%); Saucony +9.9%; HOKA +7.7%; On Americas +13.0% constant currency. Circana US running H1 2026: category +13% dollars and units; YipitData: 2025 running footwear +8.9% with Nike share down in store and online (OPENED).

The wearer series line up with the peer growth ranking, not with Nike's: the brands gaining wearers (ASICS +160 bp racing, adidas +150 bp, Brooks +170 bp in the survey; ASICS and adidas to 64% of Hakone) are the brands reporting the fastest running growth (ASICS +33.8% NA, adidas +28%). Brooks at +9% Americas is gaining survey share, so the survey tracks preference, not the same quarter's sales.

## 5. Can both be true? Alternatives tested

Nike running revenue up about $1B over five quarters while Nike's share among racing-minded runners fell 4.2 points. Explanations, with what the data say:

| Explanation | Evidence | Status |
|---|---|---|
| Growth comes from new distribution, not wearer share (Fleet Feet from April 2026; Nike run-specialty share 0.00% to 1.43%) | REPO Confluence and Fleet Feet notes; survey panel is run-specialty skewed so it cannot see doors Nike just entered | Survives |
| Growth is in non-racing and running-inspired lifestyle (Vomero, P-6000, V5 Runner "strong double digits") | Nike call quotes (REPO); wearers in races and surveys would not move | Survives |
| Growth is price (discounted Pegasus 42, 25% of Fleet Feet units at about 25% off; 43.5% of nike.com colourways discounted) | REPO `running_sellthrough` | Partly; the ASP line in the gross-margin bridge was only -30 bp in Q1 FY27 per REPO, so price is not the whole $1B |
| Growth is outside the US (EMEA, China running) while the survey is about 90% US | Nike China Running up six quarters (call, REPO); survey sample about 90% US | Survives; not testable with these data |
| The survey is biased against Nike (membership of a trade group, specialty shoppers) | Level bias is likely; a year-on-year change within one panel is less exposed, though panel composition can move | Weakens the size of the signal, not the sign |
| Hakone is team-contract driven | Section 2 | Survives for Hakone only; does not explain the US survey or Comrades |

The data cannot separate the first four. Deciding data: Circana or NPD Nike running units and ASP by channel (specialty, sporting goods, DTC); MarathonFoto 2025 and 2026 reports with Nike share by distance; Nike disclosing running units. Nike's own running figures are revenue, with no unit or price split.

Ruled out: that the Nike drop is a photo or sampling artifact. Hakone is a complete count (all starters, not photos), the survey is a self-report, Comrades is a finisher census, and Strava is app data; four different methods, same sign. Elite versus amateur: elite podium share (REPO, 86% to 19% at Majors podiums) is marketing and sponsorship; the amateur series fall in the same direction but by much less in the latest year (Hakone -6.6 pts, survey -4.2 pts versus the multi-year podium drop of 67 pts), so elite podiums are a poor guide to the size of the amateur loss (periods differ, so this is a rough comparison).

## 6. Routes tried (never accept "inconclusive")

| # | Target | Route | Result |
|---|---|---|---|
| 1 | Hakone 2018 to 2026 | Japanese search, Nikkei xtrend, Bunshun, WWD Japan, fashionsnap, PRESIDENT, Business Insider JP | WORKED (full series, counts for 2018, 2019, 2021, 2023 to 2026; 2020 and 2022 shares only) |
| 2 | Hakone from source | alpen-group.jp pages | BLOCKED (HTTP 403 on fetch); got counts via republishers |
| 3 | Hakone archived copy | web.archive.org | BLOCKED (fetch tool refuses the host) |
| 4 | Hakone qualifier and Izumo, Zenjitsu | Japanese search, note.com (Fujiwara), gendai.media | PARTIAL (Nike share 2024 and 2025, Izumo and Zenjitsu 2021, Oct 2025 top-100 order; no full-field Oct 2025 Nike count, Pia report seen only as a search snippet) |
| 5 | Japanese citizen marathons (Tokyo) | Japanese search for Tokyo Marathon and citizen runner counts, PRESIDENT, gendai, WWD | FAILED (no published amateur count found) |
| 6 | RunRepeat brand share at marathons | English search; RunRepeat studies are participation (State of Running 2019), review ratings and a 2025 US marathon report; none has brand shares | FAILED (does not exist as far as found) |
| 7 | Race photos US | Running USA, Substack, Thai daily, endurancesportswire | WORKED for 2024 vintage; no 2025 or 2026 edition found; full report paywalled ($199) and not bought |
| 8 | Boston, Chicago, NYC, London, Berlin, Tokyo, Valencia field counts | English, German (Berlin), Spanish (Valencia), Japanese (Tokyo) searches; Marathon Handbook, Outside, Runner's World mirrors | FAILED for full fields; only podium or top-30 lists. A claim of "Nike 27.4% of Chicago 2025 finishers" came from a scraped spam page and the Marathon Handbook article it cites contains only podium shoes; not used |
| 9 | Believe in the Run, Running Warehouse, Doctors of Running, Kevin Goldberg | Site and name searches; DOR London mailbag fetch returned 404 | FAILED (no shoe-count posts found) |
| 10 | YouTube descriptions, Instagram captions, Substack, podcasts | Searches including "shoe count", "shoe spotting"; DOR podcast pages | FAILED (no counts; Substack worked only for the Running USA report) |
| 11 | Strava shares | T3, Tom's Guide, sgbonline, press.strava.com pages | PARTIAL (rankings only; Strava does not publish shares) |
| 12 | Reddit annual surveys | Search; old.reddit.com fetch | BLOCKED (fetch tool refuses reddit); used REPO mention-share series instead |
| 13 | NCAA and high school cross-country spikes | Search | FAILED (no published count) |
| 14 | Comrades and other race censuses | Running Mann, News24 | PARTIAL (2025 post only; 2022 and 2024 are quoted inside it; no 2023 or 2026 post) |
| 15 | Kona whole-field after 2018 | Slowtwitch, Triathlete (paywalled redirect), podiapaedia | PARTIAL (to 2018 only) |

More than five different routes failed for the mass-marathon field counts and the NCAA spike counts, so these are reported as not published in free sources. What would settle them: (a) Running USA 2025 and 2026 MarathonFoto reports (paid, or free via a Running USA membership; a person needs to request it); (b) race-day clicker counts that brands keep internally (Nike, adidas and ASICS field staff count at finish lines; request via a sell-side channel check); (c) a photo-labelling pass on public finish-line galleries (MarathonFoto, Brightroom) for Chicago, Boston, London, Berlin 2024 versus 2025 versus 2026, roughly 1,000 runners per race to give a 3 point margin; (d) Alpen Group's own Magazine pages, which the 403 blocked.

## 7. What this note does and does not say

- It supports "Nike's share of what runners wear is lower in the latest reading than a year earlier" in four independent series. It does not support "Nike running revenue growth is fake," because the revenue and wearer measures cover different populations (section 5).
- It does not give a smoking gun. Ranked by weight: Running USA 2026 survey (-420 bp racing, n=11,700, biased panel) and Hakone (full count, team-driven) are the two strongest; Strava and Reddit are weak.
- Suggested scoreboard wording (not edited into REPORT.md): "Wearer data (Hakone 23.3% to 16.7%, Running USA racing-shoe favorite 15.2% to 11.0%, Comrades 16% to 13%) show no Nike recovery in what runners wear through mid-2026; Nike's running growth is therefore likely distribution, lifestyle or non-US, which the data cannot separate."
