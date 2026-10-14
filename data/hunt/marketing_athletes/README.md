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
