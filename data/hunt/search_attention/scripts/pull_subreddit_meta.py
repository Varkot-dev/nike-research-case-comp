"""Subreddit metadata snapshot (subscribers, created date, archive post/comment totals) from Arctic Shift.
Source: https://arctic-shift.photon-reddit.com/api/subreddits/search?subreddit=<name>
Re-run: python3 -I pull_subreddit_meta.py <rawdir> <outcsv>"""
import csv, json, os, sys, time, urllib.request
OUT, CSV = sys.argv[1], sys.argv[2]
SUBS = ["Nike", "adidas", "Hoka", "NewBalance", "asics", "OnRunning", "Brooksrunning", "Saucony", "Jordans",
        "Sneakers", "RunningShoeGeeks", "running", "Repsneakers", "sneakermarket", "malefashionadvice",
        "femalefashionadvice", "lululemon", "Puma"]
rows = []
for s in SUBS:
    fn = os.path.join(OUT, s + ".json")
    if not os.path.exists(fn):
        try:
            with urllib.request.urlopen(urllib.request.Request(
                    f"https://arctic-shift.photon-reddit.com/api/subreddits/search?subreddit={s}",
                    headers={"User-Agent": "NikeCaseCompResearch/1.0"}), timeout=60) as r:
                open(fn, "wb").write(r.read())
        except Exception as e:
            print("ERR", s, e); continue
        time.sleep(3)
    d = json.load(open(fn)).get("data") or []
    if not d:
        print("none", s); continue
    x = d[0]; m = x.get("_meta", {})
    rows.append({"subreddit": x.get("display_name"), "subscribers": x.get("subscribers"),
                 "created_utc": x.get("created_utc"), "archive_num_posts": m.get("num_posts"),
                 "archive_num_comments": m.get("num_comments"), "retrieved_utc": x.get("retrieved_on") or x.get("_meta", {}).get("num_posts_updated_at")})
    print(rows[-1])
with open(CSV, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
