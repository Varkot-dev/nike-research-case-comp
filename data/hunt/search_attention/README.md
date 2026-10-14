# search_attention: consumer attention data for the Nike LONG or SHORT question

Pulled 2026-10-14 by an automated research agent. Every pull was free, without login or API key.
Scripts are in `scripts/` and can be re-run (each skips files already on disk). Raw pulls are in `raw/`.
Downloads were parsed with `python3 -I`. No personal data was sent in any request (User-Agent is a generic
"NikeCaseCompResearch/1.0 (academic)" string).

This folder ADDS to the existing work on branch `claude/wonderful-franklin-u31n4e`
(`data/altdata/gtrends_*` monthly Google Trends 2019 to Oct 2026 for 10 brands, and
`data/altdata/wikipedia_pageviews_monthly_*` for 10 brand articles). It does not duplicate them: it adds daily
Wikipedia series for 40+ articles including product and old titles, three non-English Wikipedias, Tranco web
traffic ranks since 2019, Reddit post-title mention shares since 2019, deal-subreddit discount posts, Stocktwits,
App Store and YouTube snapshots.

## 1. Sources, method, status

| # | Source | URL / endpoint | Method | Status | Range | Tidy output |
|---|---|---|---|---|---|---|
| 1 | Wikimedia pageviews REST API | `https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/{project}/all-access/user/{title}/daily/2019010100/2026101300` | `scripts/pull_wiki_pageviews.py`, titles resolved through the MediaWiki API, 429 Retry-After honoured (shared egress IP was rate limited all day, about one article per 90 s) | WORKED, 49 article series | 2019-01-01 to 2026-10-12, daily | `wiki_pageviews_daily_long.csv`, `_weekly_long.csv` (Mon-Sun, complete weeks only), `_monthly_long.csv` |
| 2 | Tranco research ranking (Chrome UX Report, Cloudflare Radar, Umbrella, Majestic, Farsight; earlier Alexa, Quantcast) | `https://tranco-list.eu/api/lists/date/{date}` then `https://tranco-list.eu/download/{id}/100000`; also `https://tranco-list.eu/api/ranks/domain/{domain}` (last 37 days only) | `scripts/pull_tranco_history.py`: 1st and 15th of every month, keep only tracked domains | WORKED | 2019-06-01 to 2026-10-01, semi-monthly, 34 domains | `tranco_rank_semimonthly_long.csv` |
| 3 | Reddit post titles via Arctic Shift archive | `https://arctic-shift.photon-reddit.com/api/posts/search` (sort=asc, limit=auto, paged) | `scripts/pull_reddit_titles.py`: first 7 days of every month from 2023-01, Jan/Apr/Jul/Oct only for 2019 to 2022; regex brand and model tagging in `scripts/clean_all.py` | WORKED for r/RunningShoeGeeks, r/Sneakers (complete); partial for r/running, r/malefashionadvice, r/femalefashionadvice, r/Repsneakers, r/sneakermarket (recent months only, not used in tests) | 2019 to 2026-10 | `reddit_title_mentions_monthly_sample.csv` |
| 4 | Reddit deal posts via Arctic Shift | same, FULL calendar months, every month 2019 to 2026 (`full` mode) | `pull_reddit_titles.py ... frugalmalefashion full` and `sneakerdeals full` | see section 4 for coverage at time of writing | 2019 to 2026-10 | `deals_titles_brand_tags.csv`, `test_deals_*.csv` |
| 5 | Reddit subreddit metadata via Arctic Shift | `/api/subreddits/search?subreddit=` | `scripts/pull_subreddit_meta.py` | WORKED but the metadata snapshot is from Feb 2025 (stale) | snapshot | `subreddit_snapshot.csv` |
| 6 | Stocktwits public symbol streams | `https://api.stocktwits.com/api/2/streams/symbol/{SYM}.json?max=` | `scripts/pull_stocktwits.py` | WORKED | NKE: 4,799 messages Oct 1 to Oct 14 2026; peers back further | `stocktwits_messages.csv`, `stocktwits_watchlist_snapshot.csv` |
| 7 | Apple App Store lookup + customer review RSS | `https://itunes.apple.com/lookup?id=&country=`; `https://itunes.apple.com/{cc}/rss/customerreviews/id={id}/xml` | `scripts/pull_appstore_reviews.py` | lookup WORKED (8 storefronts, 10 apps); review RSS returned entries only for the US default feed of some apps (JSON and paged sortby feeds came back empty) | snapshot 2026-10-14 | `appstore_snapshot_2026-10-14.csv`, `appstore_recent_reviews_2026-10-14.csv` |
| 8 | YouTube channel pages | `https://www.youtube.com/@{handle}/videos` (embedded ytInitialData) | `scripts/pull_youtube_channels.py` | WORKED for 12 channels (HOKA, ASICS, On handles not found) | snapshot | `youtube_channel_snapshot_videos.csv` |
| 9 | Google Trends via pytrends 4.9.2 | trends.google.com explore / multiline | `scripts/pull_gtrends.py` (45 s spacing, 70 s backoff) | MOSTLY BLOCKED: 4 batches succeeded early (`intent_*`), every later request returned 429 for hours, including through WebFetch | 2021-10 to 2026-10 weekly | `gtrends_batches_long.csv` (4 batches only; the within-brand sale ratios are useless because "nike sale" rounds to 0 to 1 on a 0 to 100 scale next to "nike") |
| 10 | Published figures (web search) | Piper Sandler teen survey; Confluence Running store share | WebSearch / WebFetch | SNIPPET or OPENED, see section 5 | | cited only |

### Blocked or unusable (keep trying list)

- Google Trends: 429 for every request after the first four batches (shared egress IP). WebFetch also got 429.
- GDELT DOC 2.0 API (`api.gdeltproject.org`): 429 "limit requests to one every 5 seconds" on the very first call, repeatedly (shared IP). BigQuery GDELT needs a GCP project (none configured).
- web.archive.org (Wayback CDX and snapshots): TCP connection reset on every attempt today (archive.org/wayback/available answers, but snapshots live on web.archive.org). So no archived subreddit-subscriber history and no archived App Store rating-count history.
- reddit.com `about.json`: 403. subredditstats.com: answers but data frozen in Dec 2023.
- Arctic Shift `/aggregate` endpoint with title search: "Timeout. Maybe slow down a bit" (HTTP 422) after a few calls; switched to plain listings.
- Bluesky public search API (`public.api.bsky.app`): connection reset.
- Baidu Index, Weibo, TikTok Creative Center: need login or JS; not attempted beyond a check.
- English Wikipedia has no articles for Nike Pegasus, Vomero or Vaporfly, and de.wikipedia has no On article.

## 2. Known gaps and caveats (read before quoting any number)

- **Wikipedia page moves.** Views are counted per title. When a page is renamed, history stays under the old
  title. Old titles were pulled and summed (`*_oldtitle*` labels): Hoka lived at "Hoka One One" until about
  May 2025, then "Hoka (brand)" until about May 2026, then "Hoka". Missing the middle title made Hoka look
  +900% in an early run; fixed. Nike Dunk, Adidas Gazelle, Air Force 1, Deckers and Converse articles were created
  or moved in 2023 to 2024, so their YoY before mid 2024 is meaningless.
- **Wikipedia traffic is falling for everything** (AI answers, search changes): the median rival brand article
  was down 18% to 30% YoY in 2026. Use SHARES or excess-over-median, never raw YoY.
- **Wikipedia "user" agent still contains some automated traffic**; one-day spikes (On, Sep 18 2026; Converse,
  Sep 19 to 22 2026) are visible in the daily file. Weekly medians were used as a robustness check.
- **zh.wikipedia is blocked in mainland China**, so it measures Taiwan, Hong Kong and overseas Chinese readers.
- **Reddit archive coverage drops in Oct 2025**: posts per sampled week in r/RunningShoeGeeks fell from about
  300 to about 70, and r/running from about 600 to about 60 (recovering mid 2026). This looks like archive
  ingestion or moderation removal, not a real 75% fall in activity. Shares (Nike mentions over all brand
  mentions) are robust to this, but sample sizes and confidence intervals widen.
- **Reddit regex tagging** is title-only and imperfect ("on" is only counted as "on running / on cloud / cloudmonster"
  etc.; "jordan" can be a person). A post naming two brands counts for both.
- **Tranco** ranks blend several providers and the provider mix changed (Alexa removed in 2023, Chrome UX
  Report and Cloudflare added). Compare Nike with peers on the same date, not across years.
- **Stocktwits** sentiment is self-tagged by a minority of posters and is retail chatter, not positioning data.
- **App Store** written-review feeds skew to complaints and cover only the latest 50; rating counts are cumulative
  since launch. Snapshot only, so no test is built on them.

## 3. Tests (rules written before running; full output in `test_output_2026-10-14.txt`)

**T1. Is Nike's share of consumer attention rising or falling in 2026? (questions 1 and 7)**
Rule: LONG if Nike + Air Jordan share of en.wikipedia views versus 14 rival brand articles is up 1 pp or more
YoY over Jun 1 to Oct 11 2026; SHORT if down 1 pp or more; otherwise flat.
Result: 20.46% (2025) to 20.75% (2026), +0.29 pp. Dropping any one rival: -0.15 to +1.16 pp. Weekly medians 20.83%
vs 20.88%; 10 of 19 weeks above last year's median. Aug 1 to Oct 11 only (after the World Cup): +0.28 pp.
Trajectory of the YoY gap: about -15 pp a month in 2024, -2 to -4 pp in 2025, about 0 in 2026 (`test_wiki_monthly_nike_share.csv`).
Validation: across 20 fiscal quarters (FY21 to FY27Q1, ex COVID base), corr(Nike revenue YoY, wiki share YoY) = 0.41.
Reading: the attention slide stopped in mid 2025; there is no rebound. Agrees with the repo's Google Trends work (US
share up 0.7 to 4.5 pp YoY Jun to Oct 2026, world flat). Flat attention next to +9% NA wholesale shipments fits the
channel-fill reading of question 1 rather than a demand surge. Verdict: NEUTRAL on level, mildly SHORT for question 1.

**T2. Running: is Nike gaining share of enthusiast conversation? (question 6)**
Rule: LONG if Nike's share of brand mentions in r/RunningShoeGeeks titles is up significantly in 2026 vs 2025;
SHORT if down. Result: 17.7% (74 of 418) in 2026 vs 15.0% (243 of 1,622) in 2025, +2.7 pp, z = 1.37, p = 0.17;
2023 to 2024 baseline 16.3%. Vomero mentions per 1,000 titles: 3.9 (2023), 5.1 (2024), 11.6 (2025H1), 44.6 (2025H2),
41.2 (2026H1), 36.9 (2026H2). Pegasus 21 to 22 in 2023 to 2025, 14.8 in 2026H2; Vaporfly 17 to 21 falling to 3.7.
Hoka fell from 46 to 33. Verdict: weak LONG. Vomero created real organic enthusiasm (8x), Nike's share edged up
but not significantly; Pegasus attention is fading, which fits the discounted Pegasus 42 finding.

**T3. Lifestyle classics: still falling faster than the market? (question 5)**
Rule: LONG if Dunk, AF1 and Jordan Wikipedia views beat the median rival brand article YoY in the latest window and
Nike's r/Sneakers share is stable or rising; SHORT if they trail and the share falls.
Result (excess YoY vs rival median, pp): Dunk -14.6 (Jun to Aug 2026), -20.7 (Sep 1 to Oct 11); AF1 +18.2 then -3.2;
Air Jordan +5.9 then -8.0; Air Max +6.4 then -7.7. Adidas Samba -26.3 and Gazelle -33.8 in Sep to Oct (the
terrace fad is fading faster). r/Sneakers Nike share of brand mentions: 66.0% (2023), 59.6% (2024), 57.9% (2025),
54.8% (2026 Jan to Oct; z = -1.41 vs 2025, p = 0.16; p < 0.001 vs 2023), 50.2% in Jul to Oct 2026.
Verdict: SHORT, moderate. Dunk has not found a floor; AF1 and Jordan improved in summer then relapsed in Sep to Oct.

**T4. International attention vs adidas, controlling for the World Cup (questions 3 and 7)**
Rule: SHORT if Nike/adidas view ratio on zh, de and ja Wikipedia is down YoY after removing the Jun to Jul 2026 World
Cup window; LONG if up. Result: Jun to Jul 2026 ratio fell 28% (zh), 28% (de), 55% (ja), 30% (en): an adidas World
Cup spike. Aug 1 to Oct 11: zh +17%, de +16%, ja -3%, en +2%. Verdict: weak LONG for brand heat abroad, and a
warning that any Jun to Jul 2026 comparison against adidas is distorted. zh.wikipedia is blocked in mainland China, so
this says nothing about the China floor.

**Supporting, not tests**
- Tranco: nike.com averaged rank 595 (Jun to Oct 2025) and 639 (Jun to Oct 2026); peer domains fell further
  (adidas 2,164 to 3,000; newbalance 14,779 to 22,369; asics 6,114 to 8,697; lululemon 4,233 to 6,077; on.com flat).
  Log rank gap vs peers -2.21 to -2.44. But big-retail controls moved like Nike (target 538 to 588; walmart 442 to 424)
  and most mid-tier domains drifted down, so this is a list-composition effect as much as a Nike effect. INCONCLUSIVE.
- r/sneakerdeals [Retailer]-tagged posts: Nike share of branded deals 11.3% (2025) to 14.3% (2026 Jan to Oct), and 50%
  in Jul to Oct 2026 (35 of 70), many "[Nike] ... 25% off with code DAYONE" posts. Driven by a few prolific posters,
  so INCONCLUSIVE, but it shows Nike.com running an extra-25%-off member code in Aug to Sep 2026.
- Stocktwits NKE, Oct 1 to 14 2026: 4,799 messages, 61% of tagged messages Bullish (DECK 90%, ONON 66%, LULU 59%);
  bullish share went from 39% on Oct 1 (earnings day) to 70% to 80% on Oct 5 to 9. Retail is buying the dip while
  short interest is at a record: crowded on both sides.

## 5. Published figures found (not machine-pulled)

- Piper Sandler Taking Stock With Teens: Nike favourite footwear brand 61% (Fall 2023), 57% (Fall 2024),
  "49% vs 60% average 2022 to 2023" (Spring 2025), 46% (Fall 2025, "mindshare starting to stabilize sequentially";
  On No. 4 overtook HOKA No. 5). The survey moved to once a year; the Fall 2026 edition had not been found as of
  2026-10-14 and may land before Nov 19 (a catalyst). Sources: pipersandler.com/teens (OPENED), sgbonline.com and
  finance.yahoo.com articles (SNIPPET).
- Confluence Running (one US run-specialty store) brand share, post dated 2026-02-18 (OPENED,
  confluencerunning.com): Nike 0.00% (Q1 to Q2 2025), 0.31% (Q4 2025), 1.43% (2026 YTD); HOKA 19.17%,
  Brooks 17.05%, Saucony 12.46%, Topo 10.87%, New Balance 9.68%, Asics 8.43%, On 5.05%. One store, no
  methodology: anecdote of Nike re-entering run specialty from zero, not a market share.
