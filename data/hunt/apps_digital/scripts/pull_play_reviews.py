"""Google Play: page newest-first through public reviews (google-play-scraper, no login) for Nike and rival apps.
Stops at 2019-01-01 or a cap. Writes raw/play_reviews/<app>__<lang>_<cc>.csv.gz (date, score, thumbs, appVersion; no text, no user names).
Re-run: python3 pull_play_reviews.py [lang] [country]
"""
import csv, gzip, os, sys, time, datetime
from google_play_scraper import reviews, Sort
LANG = sys.argv[1] if len(sys.argv) > 1 else "en"
CC = sys.argv[2] if len(sys.argv) > 2 else "us"
OUT = "/home/user/nike-research-case-comp/data/hunt/apps_digital/raw/play_reviews"
os.makedirs(OUT, exist_ok=True)
APPS = {"nike_app": "com.nike.omega", "nike_snkrs": "com.nike.snkrs", "nike_run_club": "com.nike.plusgps",
        "nike_training_club": "com.nike.ntc", "adidas_app": "com.adidas.app", "adidas_confirmed": "com.adidas.confirmed.app",
        "adidas_running": "com.runtastic.android", "stockx": "com.stockx.stockx", "goat": "com.airgoat.goat",
        "footlocker": "com.footlocker.approved", "dicks": "dsgui.android", "strava": "com.strava",
        "zappos": "com.zappos.android", "champs": "com.champssports.champssports", "asics_runkeeper": "com.fitnesskeeper.runkeeper.pro"}
STOP = datetime.datetime(2019, 1, 1)
CAP = int(os.environ.get("CAP", "150000"))
only = os.environ.get("ONLY")
for name, pid in APPS.items():
    if only and name not in only.split(","):
        continue
    fn = f"{OUT}/{name}__{LANG}_{CC}.csv.gz"
    if os.path.exists(fn):
        continue
    rows, token, err = [], None, 0
    while len(rows) < CAP:
        try:
            res, token = reviews(pid, lang=LANG, country=CC, sort=Sort.NEWEST, count=200, continuation_token=token)
        except Exception as e:
            err += 1; print("ERR", name, e, flush=True); time.sleep(15 * err)
            if err > 5: break
            continue
        if not res:
            break
        for r in res:
            rows.append((r["at"].strftime("%Y-%m-%d %H:%M:%S"), r["score"], r.get("thumbsUpCount"), r.get("appVersion") or r.get("reviewCreatedVersion"), 1 if r.get("replyContent") else 0))
        if res[-1]["at"] < STOP or token is None or getattr(token, "token", 1) is None:
            break
        time.sleep(0.6)
    with gzip.open(fn, "wt", newline="") as f:
        w = csv.writer(f); w.writerow(["at", "score", "thumbs", "app_version", "dev_replied"]); w.writerows(rows)
    print(name, LANG, CC, len(rows), rows[-1][0] if rows else None, flush=True)
