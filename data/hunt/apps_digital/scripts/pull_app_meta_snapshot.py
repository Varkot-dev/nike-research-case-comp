"""Snapshot of app metadata.
Google Play (google-play-scraper app()): realInstalls (exact global installs), installs band, ratings, written reviews, score, histogram.
Apple (apps.apple.com/{cc}/app/id{id} HTML): ratingCount, ratingAverage, ratingCounts histogram (5..1 stars).
"""
import csv, json, re, time, os, datetime, urllib.request
from google_play_scraper import app
D = datetime.date.today().isoformat()
BASE = "/home/user/nike-research-case-comp/data/hunt/apps_digital"
RAW = f"{BASE}/raw/app_meta/{D}"; os.makedirs(RAW, exist_ok=True)
PLAY = {"nike_app": "com.nike.omega", "nike_snkrs": "com.nike.snkrs", "nike_run_club": "com.nike.plusgps", "nike_training_club": "com.nike.ntc",
        "adidas_app": "com.adidas.app", "adidas_confirmed": "com.adidas.confirmed.app", "adidas_running": "com.runtastic.android",
        "stockx": "com.stockx.stockx", "goat": "com.airgoat.goat", "footlocker": "com.footlocker.approved", "dicks": "dsgui.android",
        "strava": "com.strava", "zappos": "com.zappos.android", "champs": "com.champssports.champssports", "asics_runkeeper": "com.fitnesskeeper.runkeeper.pro",
        "poizon_intl": "com.shizhuang.poizon.hk", "skechers": "com.skechers.android", "jdsports": "com.jdsports.app"}
IOS = {"nike_app": 1095459556, "nike_snkrs": 911130812, "nike_run_club": 387771637, "nike_training_club": 301521403, "adidas_app": 1266591536,
       "adidas_confirmed": 1508115448, "adidas_running": 336599882, "on_app": 6449706677, "stockx": 881599819, "dicks": 556653197,
       "strava": 426826309, "lululemon": 920098546, "puma": 1563024677, "asics_runkeeper": 300235330, "goat": 966758561}
rows = []
for k, pid in PLAY.items():
    try:
        d = app(pid, lang="en", country="us")
        json.dump({x: d.get(x) for x in ["installs", "minInstalls", "realInstalls", "score", "ratings", "reviews", "histogram", "released", "updated", "version", "title", "developer"]}, open(f"{RAW}/play_{k}.json", "w"))
        rows.append([D, "google_play", k, pid, "global", d.get("realInstalls"), d.get("installs"), d.get("ratings"), d.get("reviews"), d.get("score"), json.dumps(d.get("histogram"))])
    except Exception as e:
        print("ERR play", k, e)
    time.sleep(1)
for k, aid in IOS.items():
    for cc in ["us", "gb", "de", "fr", "jp", "kr", "cn", "au", "ca", "it", "es", "mx", "br"]:
        try:
            with urllib.request.urlopen(urllib.request.Request(f"https://apps.apple.com/{cc}/app/id{aid}", headers={"User-Agent": "Mozilla/5.0"}), timeout=60) as r:
                s = r.read().decode("utf8", "ignore")
        except Exception as e:
            print("ERR ios", k, cc, e); continue
        rc = re.search(r'"ratingCount":(\d+)', s); ra = re.search(r'"ratingAverage":([0-9.]+)', s); h = re.search(r'"ratingCounts":\[([0-9.,]+)\]', s)
        rows.append([D, "app_store", k, aid, cc, "", "", rc.group(1) if rc else "", "", ra.group(1) if ra else "", "[" + h.group(1) + "]" if h else ""])
        time.sleep(0.8)
    print(k, flush=True)
with open(f"{BASE}/app_meta_snapshot_{D}.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["pulled", "store", "app", "app_id", "storefront", "real_installs", "installs_band", "ratings", "written_reviews", "score", "histogram"]); w.writerows(rows)
