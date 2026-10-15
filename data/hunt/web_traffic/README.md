# web_traffic (G6): nike.com traffic vs Digital revenue

Note with results and route log: `research_notes/Smoking gun hunt/G6_web_traffic.md`. No personal data or email in any request; Tranco/CrUX/Semrush calls used a generic user agent. Raw folder is 1.2 MB.

| File | What |
|---|---|
| raw/tranco_expanded_long.csv | Tranco rank (top 100k) of 50 sportswear/retail domains + 40 control domains, 1st and 15th of each month, 2019-06-01 to 2026-10-01 (blank = outside top 100k) |
| raw/crux_buckets_long.csv | CrUX rank-magnitude bucket by month for brand origins: global 2022-06 to 2026-09, US/DE/GB/JP/CN 2025-01 to 2026-09 |
| semrush_trending_2026-08_long.csv | Semrush trending-websites, 18 countries x 5 categories, top 100 each: Aug 2026 visits, MoM, YoY |
| semrush_trending_global_2026-08_long.csv | Same, global, 5 categories |
| tranco_rank_wide.csv, tranco_control_basket.csv, tranco_listwide_drift.csv, tranco_zipf_traffic_index.csv, tranco_fq_yoy.csv, tranco_zipf_peer_share_by_fq.csv | Derived Tranco series, Zipf-implied YoY (alpha 0.8, 1.0, 1.2) and peer share by Nike fiscal quarter |
| test_alpha_calibration.csv | Zipf exponent fit (alpha 0.79, n=16) |
| test_tranco_vs_semrush_us_yoy_aug2026.csv, test_tranco_nike_vs_reported_digital.csv | Validation of Tranco YoY (fails: correlation -0.31 and -0.10 to -0.32) |
| test_region_semrush_yoy_vs_digital.csv, test_revenue_per_visit_wedge.csv, test_nike_vs_peers_semrush_yoy_aug2026.csv | Main result tables |
| scripts/ | pull_tranco_expanded.py, pull_crux_buckets.py, pull_semrush_trending.py, analyze_tranco.py, zipf_share.py, tests.py, wedge.py (run with `python3 -I`; tests.py needs the top-5000 scratch snapshots only for analyze_tranco.py) |

Caveats: Semrush trending shows only the latest month (Aug 2026); Semrush is a modelled estimate; GB +34% and mainland China numbers look unreliable; the Tranco top-5000 snapshots used for list-wide drift are not stored in the repo (regenerate with pull_tranco_expanded.py).
