"""Apple App Store: current rating counts (lookup API) and the 50 most recent written reviews (RSS XML)
for Nike and rival apps across storefronts. Snapshot, pulled 2026-10-14.

Sources:
  https://itunes.apple.com/lookup?id={id}&country={cc}          -> userRatingCount, averageUserRating
  https://itunes.apple.com/{cc}/rss/customerreviews/id={id}/xml -> latest 50 reviews (the JSON and the paged
     sortby=mostrecent variants returned empty feeds on 2026-10-14; the plain XML feed works)
Review velocity = 50 / (days spanned by the 50 newest reviews).
Re-run: python3 -I pull_appstore_reviews.py <rawdir>
"""
import json, os, re, sys, time, urllib.request
import xml.etree.ElementTree as ET

OUT = sys.argv[1] if len(sys.argv) > 1 else "../raw/appstore"
os.makedirs(OUT, exist_ok=True)
UA = "NikeCaseCompResearch/1.0 (academic)"
APPS = {
    "nike_app": 1095459556, "nike_snkrs": 911130812, "nike_run_club": 387771637,
    "adidas_app": 1266591536, "adidas_confirmed": 1508115448, "adidas_running": 336599882,
    "on_app": 6449706677, "stockx": 881599819, "dicks": 556653197, "strava": 426826309,
}
COUNTRIES = ["us", "gb", "de", "fr", "jp", "kr", "au", "ca"]
NS = {"a": "http://www.w3.org/2005/Atom", "im": "http://itunes.apple.com/rss"}


def get(url):
    for i in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=60) as r:
                return r.read()
        except Exception as e:
            print("ERR", url, e, flush=True)
            time.sleep(10 * (i + 1))
    return None


for app, aid in APPS.items():
    for cc in COUNTRIES:
        fn = os.path.join(OUT, f"{app}__{cc}.json")
        if os.path.exists(fn):
            continue
        meta = json.loads(get(f"https://itunes.apple.com/lookup?id={aid}&country={cc}") or b"{}")
        time.sleep(2)
        m = (meta.get("results") or [{}])[0]
        raw = get(f"https://itunes.apple.com/{cc}/rss/customerreviews/id={aid}/xml")
        time.sleep(2)
        reviews = []
        if raw:
            try:
                root = ET.fromstring(raw)
                for e in root.findall("a:entry", NS):
                    r = e.find("im:rating", NS)
                    if r is None:
                        continue
                    reviews.append({"updated": e.findtext("a:updated", default="", namespaces=NS),
                                    "rating": int(r.text),
                                    "version": e.findtext("im:version", default="", namespaces=NS),
                                    "title": e.findtext("a:title", default="", namespaces=NS)})
            except ET.ParseError as ex:
                print("parse", app, cc, ex)
        json.dump({"app": app, "id": aid, "country": cc, "pulled": time.strftime("%Y-%m-%d"),
                   "userRatingCount": m.get("userRatingCount"), "averageUserRating": m.get("averageUserRating"),
                   "userRatingCountForCurrentVersion": m.get("userRatingCountForCurrentVersion"),
                   "currentVersionReleaseDate": m.get("currentVersionReleaseDate"),
                   "reviews": reviews}, open(fn, "w"), ensure_ascii=False)
        print("OK", app, cc, len(reviews), m.get("userRatingCount"), flush=True)
print("DONE", flush=True)
