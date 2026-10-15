"""NBA on-court shoe brand usage by season from Colendri (formerly KixStats) public /stats/ page (robots: Allow).
league_ids=3 is NBA (verified: 414 Nike players 2025-26). Parses brand, minutes, times worn, players, points.
Usage: python3 -I pull_colendri_nba_brands.py <rawdir> <outcsv>"""
import sys, os, re, html, time, urllib.request, csv
RAW, OUT = sys.argv[1], sys.argv[2]; os.makedirs(RAW, exist_ok=True)
H = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Chrome/120"}
SEASONS = {"2019-20": ("2019-10-01", "2020-10-15"), "2020-21": ("2020-12-01", "2021-07-25"), "2021-22": ("2021-10-01", "2022-06-30"),
           "2022-23": ("2022-10-01", "2023-06-30"), "2023-24": ("2023-10-01", "2024-06-30"), "2024-25": ("2024-10-01", "2025-06-30"),
           "2025-26": ("2025-10-01", "2026-06-30")}
LEAGUES = {"NBA": 3, "Euroleague?": 4}
rows = []
for lg, lid in LEAGUES.items():
    for s, (a, b) in SEASONS.items():
        fn = os.path.join(RAW, f"brand_minutes_l{lid}_{s}.html")
        if not os.path.exists(fn):
            url = f"https://www.colendri.com/stats/?group_by=brand&metric=minutes&league_ids={lid}&date_from={a}&date_to={b}"
            open(fn, "wb").write(urllib.request.urlopen(urllib.request.Request(url, headers=H), timeout=90).read()); time.sleep(5)
        t = open(fn, encoding="utf-8").read()
        t = re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S); t = re.sub(r"<[^>]+>", " ", t); t = html.unescape(re.sub(r"\s+", " ", t))
        for m in re.finditer(r"#(\d+) (.+?) (\d+):(\d+) Minutes on court (\d+) worn (\d+) players \d+:\d+ (\d+) pts", t):
            rows.append(dict(league=lg, league_id=lid, season=s, date_from=a, date_to=b, rank=int(m.group(1)), brand=m.group(2),
                             minutes=int(m.group(3)) + int(m.group(4)) / 60, times_worn=int(m.group(5)), players=int(m.group(6)), points=int(m.group(7))))
        print(lg, s, sum(1 for r in rows if r["season"] == s and r["league"] == lg), flush=True)
w = csv.DictWriter(open(OUT, "w"), fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
