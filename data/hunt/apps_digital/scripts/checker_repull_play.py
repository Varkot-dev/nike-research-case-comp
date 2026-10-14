"""Checker: re-pull Google Play reviews (newest first) back to a stop date for a sample of app-locales, to verify the original pull.
Writes raw/checker/<app>__<lang>_<cc>__repull.csv.gz (at, score only)."""
import csv, gzip, sys, time, datetime
from google_play_scraper import reviews, Sort
OUT = "/home/user/nike-research-case-comp/data/hunt/apps_digital/raw/checker"
STOP = datetime.datetime(2025, 3, 1)
JOBS = [("nike_app","com.nike.omega","en","us"),("adidas_app","com.adidas.app","en","us"),
        ("nike_app","com.nike.omega","de","de"),("adidas_app","com.adidas.app","fr","fr"),
        ("adidas_app","com.adidas.app","de","de"),("nike_app","com.nike.omega","fr","fr"),
        ("stockx","com.stockx.stockx","en","us"),("footlocker","com.footlocker.approved","en","us")]
for name,pid,lang,cc in JOBS:
    rows, token = [], None
    while True:
        res, token = reviews(pid, lang=lang, country=cc, sort=Sort.NEWEST, count=200, continuation_token=token)
        if not res: break
        rows += [(r["at"].strftime("%Y-%m-%d %H:%M:%S"), r["score"]) for r in res]
        if res[-1]["at"] < STOP or token is None or getattr(token,"token",1) is None: break
        time.sleep(0.8)
    with gzip.open(f"{OUT}/{name}__{lang}_{cc}__repull.csv.gz","wt",newline="") as f:
        w=csv.writer(f); w.writerow(["at","score"]); w.writerows(rows)
    print(name,lang,cc,len(rows),rows[-1][0] if rows else None, flush=True)
