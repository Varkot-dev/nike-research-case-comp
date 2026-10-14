# Marketing and athletes data hunt (key: marketing_athletes)

Pulled 2026-10-14. Question: is Nike's marketing reach growing relative to rivals while it spends more (demand creation about 10% to 11% of revenue), or is reach stalling?

Status tags: OPENED (we fetched the page or API ourselves), SNIPPET (search summary only), DERIVED (our arithmetic).

## Tidy files

| File | What it is | Rows / span | Source | Method |
|---|---|---|---|---|
| `nba_shoe_brand_minutes_by_season.csv` | On-court NBA minutes, times worn, players, points by shoe brand, top 20 brands per season (plus a second league id 4, probably EuroLeague) | 2019-20 to 2025-26 | https://www.colendri.com/stats/ (formerly KixStats; robots.txt allows /stats/) | `scripts/pull_colendri_nba_brands.py`, league_ids=3 verified as NBA. OPENED |
| `test_nba_share.csv` | Minute shares (Nike Inc = Nike + Jordan + Converse) | 7 seasons | DERIVED | `scripts/run_tests.py` |
| `elite_visibility_share.csv` | Nike and adidas share of podiums or players in elite arenas: World Marathon Majors podiums (2018, 2019, 2024, 2025, 2026), World Athletics podiums (2022, 2023, 2024 Olympics, 2025), World Cup boots (2018, 2022, 2026), World Cup kits (2022, 2026) | 14 rows | runpack.fr, therunningchannel.com, runningshoesguru.com, footyheadlines.com, nss-sports.com, logos-pres.md (Footpack data) | hand-entered from opened pages; URL and status per row |
| `endorsement_events.csv` | Ledger of athlete, club, federation and college wins and losses for Nike, 2023 to Sep 2026 | 20 events | news pages, URL per row | hand-entered; status per row |
| `followers_wikidata_brands_long.csv` | Follower history stored on Wikidata (property P8687 with point-in-time qualifiers): YouTube, X/Twitter, Instagram, for 17 brands | 88 rows, 2017 to 2026 | https://www.wikidata.org/wiki/Special:EntityData/Q483915.json etc. | `scripts/wikidata_followers.py` (entity JSON, not the query service, which was rate limited) |
| `youtube_subscribers_history.csv`, `test_youtube_subscriber_growth.csv` | Wikidata YouTube subscriber points plus today's count from the channel page; interpolated Jul 2021, Oct 2024, Oct 2025, Oct 2026 and growth rates | 9 brands | Wikidata + youtube.com | DERIVED (linear interpolation between dated points) |
| `youtube_uploads_tidy.csv`, `test_youtube_longform_by_year.csv`, `test_youtube_views_by_age.csv` | Every long-form upload on 16 brand channels with view count and relative age ("4 months ago") | 4,450 videos | youtube.com/@handle/videos and the public web client continuation (no key, no login) | `scripts/pull_youtube_uploads.py`, `scripts/tidy_youtube.py` |
| `tiktok_brand_snapshot_2026-10-14.csv` | Followers, total likes, video count for 23 brand TikTok handles | snapshot | https://www.tiktok.com/@handle (embedded JSON) | `scripts/pull_tiktok.sh` |
| `instagram_top_accounts_wiki_revisions.csv` | Follower counts (millions) of the top 50 Instagram accounts, including @nike, read from quarterly revisions of the Wikipedia page "List of most-followed Instagram accounts" | 2016 to 2026 (see gaps) | MediaWiki revisions API | `scripts/wiki_revision_series.py`, `scripts/tidy_instagram_list.py` |
| `social_followers_snapshots_manual.csv` | Instagram follower snapshots for Nike (2025, Feb 2026, Oct 2026) and rivals (Feb 2026) | 9 rows | qualtrics, revistamercado.do, qoruz.com | hand-entered |
| `kits_team_season_tidy.csv`, `kits_league_season_brand_counts.csv`, `test_big5_kit_counts.csv` | Kit manufacturer of every club in a league season, from Wikipedia season pages | 2014-15 to 2026-27, patchy (see gaps) | en.wikipedia.org REST HTML | `scripts/pull_wiki_kits.py`, `scripts/fetch_wiki_pages.py`, `scripts/tidy_kits.py` |
| `google_ads_*` | Not produced: see blocked list | | | `scripts/pull_google_ads_transparency.py`, `scripts/pull_google_ads_monthly_counts.py` kept for re-runs |

Raw pulls are in `raw/` (HTML, JSON). All under 20 MB.

## Re-run

```
python3 -I scripts/pull_colendri_nba_brands.py raw/colendri nba_shoe_brand_minutes_by_season.csv
python3 -I scripts/wikidata_followers.py raw/wikidata followers_wikidata_brands_long.csv "Nike, Inc.|Adidas|..."
python3 -I scripts/pull_youtube_uploads.py raw/youtube raw/youtube_uploads_raw.csv 60
python3 -I scripts/tidy_youtube.py raw/youtube_uploads_raw.csv youtube_uploads_tidy.csv test_youtube_views_by_age.csv
bash scripts/pull_tiktok.sh raw/tiktok
python3 -I scripts/wiki_revision_series.py "List of most-followed Instagram accounts" raw/wiki_rev_instagram 2019-01 2026-10 3
python3 -I scripts/tidy_instagram_list.py raw/wiki_rev_instagram instagram_top_accounts_wiki_revisions.csv
python3 -I scripts/tidy_kits.py raw/wiki_league_pages kits_team_season_tidy.csv kits_league_season_brand_counts.csv
python3 -I scripts/run_tests.py .
```

## Blocked or unusable sources

- Meta Ad Library: web page returns 403 without login; Graph API `ads_archive` needs an access token. Not attempted further (no login rule).
- Google Ads Transparency Center: the public `SearchSuggestions` RPC worked (advertiser ids saved in `raw/google_ads/suggest_*.json`; Nike, Inc. US shows a 9,000 to 10,000 lifetime creative bucket, adidas America 2,000 to 3,000, On AG 2,000 to 3,000, Under Armour 7,000 to 8,000) and one `SearchCreatives` call returned Sep 2026 Nike US creatives in a 1,000 to 2,000 bucket. Every later `SearchCreatives` call returned HTTP 429 for over an hour, so no monthly series.
- web.archive.org (CDX, id_ snapshots), archive.org availability API, archive.ph, mementoweb: connection reset, 429 or 502 through the proxy, and WebFetch refuses web.archive.org. So no archived Social Blade or Instagram pages.
- Wikidata Query Service (SPARQL): "rate-limiting to 1 req/min during outage". Used entity JSON instead.
- Instagram profile pages: no follower meta without login.
- Social Blade live pages: not attempted after archive block (live pages need JS and show only recent history).
- Wikipedia REST and API: heavy 429s (shared IP with other agents), so league pages and Instagram revisions are patchy.
- WWD (tollbit paywall redirect), Graphic News (subscriber only).
- KixStats now redirects to Colendri (worked).

## Known gaps and caveats

- Elite visibility rows mix sources with different counting rules (podium places vs medals, top 3 vs all finishers). Compare within an arena, not across arenas. World Marathon Majors 2026 covers 6 of 7 races (New York on Nov 1 pending).
- 2018 Marathon Majors and the World Cup boot shares for 2018 and 2022 are SNIPPET only. 2023 Marathon Majors brand totals were not published in full (Nike Alphafly 7, adidas at least 13 of 36), so 2023 is left out.
- YouTube long-form views include paid TrueView views, so they measure spend as much as organic interest. Relative upload ages are coarse ("2 years ago" means 2.0 to 2.99 years). Shorts are not included.
- Wikidata follower points are entered by volunteers at irregular dates; growth rates use linear interpolation between them.
- TikTok is one snapshot; no history could be retrieved.
- Colendri shows only the top 20 brands per query; the tail (under 1% each) is missing from denominators, which inflates all shares slightly and equally.
- Endorsement ledger is not exhaustive; it lists high-profile moves found in searches.

## Test results (2026-10-14, full output in `test_output_2026-10-14.txt`)

Spend context: Nike demand creation $4,285M (FY24) to $4,754M (FY26), +10.9%; Q1 FY27 $1,252M vs $1,188M, +5.4% while revenue fell. adidas marketing EUR 2,841M to 3,079M (2024 to 2025), +8.4%.

1. **Reach vs spend (social).** Set in advance: LONG if Nike's follower growth keeps pace with rivals and peers; SHORT if Nike's reach stalls while spend rises.
   - Instagram (Wikipedia revision series): @nike grew 60.5% from Dec 2021 to Sep 2023 (faster than 98% of the other top-50 accounts), then peaked at 307M (Mar 2024) and fell to 291M (Sep 2026), -5.2%, against a median of -2.2% for the other top-50 accounts (77% did better). Last 12 months: Nike -2.7% vs median -2.0% (roughly in line; a platform-wide clean-out in mid-2026 hit everyone).
   - YouTube subscribers: Nike +7.2% (Oct 24 to Oct 25) then +3.6% (Oct 25 to Oct 26); adidas +44% then +43%, passing Nike (adidas 3.28M vs Nike 2.28M; in Jul 2021 it was 0.93M vs 1.64M).
   - TikTok snapshot: adidas 12.3M followers and 152M likes vs Nike 9.3M and 50M.
   - Paid reach is a different story: Nike's football channel pulled 95M long-form views on uploads from the last 12 months (one World Cup film "Rip The Script" has 81M), vs 2.6M the year before. Spend buys views; organic following is not growing.
2. **Elite visibility share (proof of product on the biggest stages).** LONG if Nike's share stabilises or rebounds in 2025 to 2026; SHORT if it keeps falling.
   - World Marathon Majors podiums: 86% (2019) to 26% (2024), 24% (2025), 19% (2026, 6 of 7 races). adidas 56% in 2026.
   - World Athletics podiums: 57.0% (2022), 46% (2023), 45.8% (Paris 2024), 37.6% (Tokyo 2025).
   - World Cup boots: 62.8% (2018), about 50% (2022), 42.8% (2026); adidas 33% to 40%.
   - World Cup kits: 13 of 32 (2022) to 12 of 48 (2026); adidas 14, Puma 11.
3. **NBA court share (Nike's strongest arena).** LONG if stable; SHORT if eroding. Nike Inc (Nike + Jordan + Converse) minute share 74.8% (2019-20) to 69.1% (2024-25), then 70.8% (2025-26). Chinese brands 2.2% to 6.9%. Largely stable: NEUTRAL.
4. **Sponsorship roster (clubs and athletes).** LONG if wins outnumber losses; SHORT if losses dominate. Big-5 European leagues: Nike clubs 18 of 97 (2019-20) to 13 of 95 (2025-26), adidas 13 to 23. Ledger of headline moves 2023 to Sep 2026: 15 losses (Mbappe, Kane, Dembele, Liverpool, Portugal, Penn State, Tennessee, Tiger Woods...) vs 5 wins (DFB from 2027, Caitlin Clark, Cade Cunningham extension, Alysa Liu, South Carolina). Not exhaustive; Nike says it is concentrating on fewer elite assets, which explains part of the drop.

## Checker review

Checked 2026-10-14 by a second agent. Re-pulls are saved in `raw/checker/` (script: `scripts/checker_repull.sh`). `scripts/run_tests.py` was re-run and its output matches `test_output_2026-10-14.txt` exactly.

### Re-pulls against the original sources

| Dataset | Points re-pulled | Result |
|---|---|---|
| Colendri NBA brand minutes | 2025-26, 2023-24, 2019-20 (league_ids=3) | Exact match (Nike 388,696 min and 414 players in 2025-26; 397,064 min in 2023-24; 101,279 min in 2019-20) |
| Marathon Majors podiums | therunningchannel 2026 and 2025, runpack 2019 | Match: 2026 adidas 20, Nike 7, ASICS 5, UA 2, On 1, Xtep 1 (36); 2025 adidas 18, Nike 10 of 42; 2019 Nike 14 of 18 women and 17 of 18 men (31 of 36) |
| World Athletics podiums | runpack 2025 | Match: Nike 50 medals (37.6%), vs 57.02% (2022) and 46% (2023); adidas 28.6% |
| World Cup boots 2026 | footyheadlines | Article says Nike 42.6% and adidas 40.3%. The CSV has 42.8% from counts (534 of 1,248) whose source the article does not show. Small gap, no effect on the conclusion |
| Instagram (Wikipedia revisions) | revids 1063018789, 1216568016, 1376216022 via `action=raw` | Match: @nike 190M, 307M and 291M |
| Wikidata P8687 (Q483915) | entity JSON | All 14 Nike follower statements match the CSV |
| YouTube subscribers | @nike, @adidas pages | Match: 2.28M and 3.28M |
| TikTok | @nike, @adidas, @puma | Match: 9.3M followers and 49.9M likes; 12.3M and 152.1M; 6.2M and 73.1M |
| Club kits | current 2025-26 Bundesliga page | All 18 suppliers match the tidy CSV |

### Cleaning checks

- No duplicate rows in the NBA, Instagram (revid by handle), Wikidata, kits (league by team by season) or YouTube files (video by views). The 73 repeated channel and title pairs in the YouTube file are reposts with different view counts, not duplicates.
- **NBA 2019-20 is a partial sample.** The 2019-20 season has only 156,829 player-minutes and 6,594 wears. Every season from 2021-22 has about 635,000 minutes and 28,000 wears. A re-pull for Oct 2019 to Mar 2020 gives only 64,434 Nike minutes, so Colendri's coverage that season is thin, and it is not just the bubble. 2020-21 (564,827 min) is the first near-complete season. Its Nike Inc share (74.8%) matches the 2019-20 figure, so the trend still holds: 74.8% (2020-21) to 70.8% (2025-26). The baseline should be cited as 2020-21. The README row count of 163 is slightly off: the file has 128 NBA rows and 43 league-4 rows.
- Instagram survivorship: only 2 of the Mar 2024 top-50 accounts are missing in Sep 2026, and both are renames (justinbieber to lilbieber, mileycyrus to miley), so there is no real survivorship bias. Only 1 or 2 accounts show unchanged (stale) values between revisions. The result is not sensitive to the start date: Nike's change to Sep 2026 vs the top-50 median was -4.6% vs -0.6% from Sep 2023, -4.9% vs -1.8% from Dec 2023, and -4.3% vs -2.2% from Sep 2024. Among brand or institution accounts in the list, Nike (-5.2%) is close to natgeo (-5.6%), while nba (+0.7%), championsleague (+5.3%), realmadrid (+17.5%) and fcbarcelona (+17.5%) grew.
- Kits denominators: Ligue 1 went from 20 to 18 clubs, and one club is missing in each of 2019 and 2025 (19 of 20 and 17 of 18). Nike share is 18.6% (18 of 97) in 2019-20 vs 13.7% (13 of 95) in 2025-26. The 2015, 2016, 2021 and 2026 seasons cover only 3 or 4 leagues, so do not plot them next to full seasons.
- The TikTok snapshot includes non-official accounts that should be dropped: adidasoriginals (53 followers), anta (771), lining (8) and nikebasketball (7).
- Elite visibility rows mix race sets: 2019 has 6 majors, 2024 has 6 majors plus the Paris Olympic marathon, and 2025 and 2026 include Sydney. The 2018 and 2022 boot shares come from different databases (Footpack and Football Boots DB) and are SNIPPET only.

### What holds and what does not

1. **Elite visibility (SHORT, strong): HOLDS for running, weaker for football.** The Marathon Majors and World Athletics numbers were re-pulled from the original pages and match. The 2026 Majors result does not depend on New York: even if Nike took all 6 NYC podium places, it would reach only 13 of 42 (31%), still below 2024. In football, the 2018 to 2026 boot trend joins numbers from different databases, and kit counts reflect commercial choices. So football is moderate. Running is strong.
2. **Social reach vs spend (SHORT, moderate): PARTLY HOLDS.** The Instagram result reproduces and is robust to the start date and to survivorship. The claim that "adidas passed Nike on YouTube" is true only for the flagship channels. Nike splits its audience across channels. The Nike family re-pulled today totals about 6.45M subscribers (nike 2.28M, nikefootball 3.0M, jordan 440K, nikebasketball 413K, nikewomen 219K, nikerunning 85K, nikesportswear 17K). The adidas family found totals about 5.34M (adidas 3.28M, adidasfootball 1.68M, adidasoriginals 378K; the adidasbasketball page showed no count, and adidasrunning and adidaswomen return 404). So Nike still leads on total YouTube reach. The adidas flagship's growth (+43% a year) is real, but flagship counts alone overstate the shift. TikTok is one snapshot and cannot show a trend. Keep this at moderate SHORT, and let Instagram carry it.
3. **NBA court share (NEUTRAL, moderate): HOLDS** once the baseline is moved to 2020-21 (74.8% to 70.8%). Chinese brands rose from 2.2% to 6.9%, but that start figure is the 2019-20 partial sample; use 2020-21 instead.
4. **Sponsorship roster (SHORT, moderate): WEAKER than stated, closer to weak.**
   - The ledger leaves out at least three major Nike retentions or wins that the checker verified. FC Barcelona renewed to 2038 (approved Dec 21, 2024; reported at about EUR 1.7B over 14 years; [beIN](https://www.beinsports.com/en-us/soccer/articles-video/fc-barcelona-and-nike-extend-partnership-until-2038-2024-12-21)). The NFL uniform deal was extended to 2038 (Dec 2024; [BNN Bloomberg](https://bnnbloomberg.ca/business/2024/12/11/nike-extends-football-uniform-deal-with-nfl-through-2038), [Sportcal](https://www.sportcal.com/sponsorship/nike-ties-down-nfl-uniform-supply-rights-through-2038/)). Giannis Antetokounmpo's re-signing appears in the ledger's own Cade Cunningham source URL but not as a row.
   - Two of the 15 "losses" are contested prospects Nike never had under a senior deal (Yamal, Flagg). The Bekele "two decades with Nike" row is an unverified snippet. So the 15 vs 5 count overstates the imbalance. Corrected, it is about 13 losses vs 8 wins, and the wins include two of the largest contracts in the sport.
   - The big-5 kit decline is a long-running trend, not a new one: Nike share was 26.8% (2014-15), 18.6% (2019-20), 14.7% (2023-24) and 13.7% (2025-26). Most of the drop came before the 2023 to 2026 problems. That supports the "deliberate concentration on elite assets" explanation.
   - What does stand is that adidas went from 13 to 23 clubs, and Liverpool, Penn State and Tennessee moved to adidas.
   - Mbappe leaving Nike is corroborated (Le Parisien via [footyheadlines](https://www.footyheadlines.com/2026/03/mbappe-leaves-nike.html)), and the move to On by [Sole Retriever](https://www.soleretriever.com/news/articles/kylian-mbappe-leaves-nike-and-joins-on-football) in addition to ESPN.

**Net:** the hunter's best finding (losing the performance-chosen stages in running) is reproducible and strong. The reach-vs-spend claim should be presented with the YouTube channel-family caveat. The roster test should be downgraded to weak or moderate SHORT.
