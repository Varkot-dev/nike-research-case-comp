"""Reddit post titles, sampled: the first 7 days of every month, Jan 2019 to Oct 2026, for selected subreddits.

Source: Arctic Shift public Reddit archive (https://arctic-shift.photon-reddit.com/api/posts/search), no login/key.
Why titles and not the /aggregate endpoint: the aggregate+title queries hit the server's query-time throttle
("Timeout. Maybe slow down a bit", HTTP 422) on 2026-10-14; plain listings are cheap.
Paging: sort=asc, limit=auto, next 'after' = last created_utc + 1.
Output: raw/reddit_titles/<sub>/<YYYY-MM>.csv.gz with created_utc,score,num_comments,title
Re-run: python3 -I pull_reddit_titles.py <rawdir>
"""
import csv, gzip, json, os, sys, time, urllib.parse, urllib.request, datetime

OUT = sys.argv[1] if len(sys.argv) > 1 else "../raw/reddit_titles"
UA = "NikeCaseCompResearch/1.0 (academic)"
SUBS = ["RunningShoeGeeks", "Sneakers", "malefashionadvice", "femalefashionadvice", "running"]
if len(sys.argv) > 2:
    SUBS = sys.argv[2].split(",")
# Optional 3rd arg "full": take whole calendar months and every month 2019-2026 (used for the low-volume deal subs)
FULL = len(sys.argv) > 3 and sys.argv[3] == "full"
# Throughput is about one file per minute, so months are thinned: every month from 2023-01,
# and Jan / Apr / Jul / Oct only for 2019 to 2022.
BASE = "https://arctic-shift.photon-reddit.com/api/posts/search"


def get(params):
    url = BASE + "?" + urllib.parse.urlencode(params)
    for i in range(6):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=180) as r:
                d = json.load(r)
            if d.get("data") is not None:
                return d["data"]
            print("server:", d.get("error"), flush=True)
        except Exception as e:
            print("ERR", e, flush=True)
        time.sleep(20 * (i + 1))
    return None


months = []
d = datetime.date(2019, 1, 1)
while d <= datetime.date(2026, 10, 1):
    if FULL or d.year >= 2023 or d.month in (1, 4, 7, 10):
        months.append(d)
    d =(d.replace(day=28) + datetime.timedelta(days=5)).replace(day=1)

for m in reversed(months):  # newest first so the most relevant period lands first
    for sub in SUBS:
        os.makedirs(os.path.join(OUT, sub), exist_ok=True)
        fn = os.path.join(OUT, sub, f"{m:%Y-%m}.csv.gz")
        if os.path.exists(fn):
            continue
        start = int(datetime.datetime(m.year, m.month, 1, tzinfo=datetime.timezone.utc).timestamp())
        if FULL:
            nxt = (m.replace(day=28) + datetime.timedelta(days=5)).replace(day=1)
            end = int(datetime.datetime(nxt.year, nxt.month, 1, tzinfo=datetime.timezone.utc).timestamp())
        else:
            end = start + 7 * 86400
        after, rows, ok = start, [], True
        for _ in range(200):
            data = get({"subreddit": sub, "after": after, "before": end, "sort": "asc", "limit": "auto",
                        "fields": "created_utc,score,num_comments,title"})
            time.sleep(1.5)
            if data is None:
                ok = False
                break
            if not data:
                break
            rows.extend(data)
            after = int(data[-1]["created_utc"]) + 1
            if len(data) < 90:
                break
        if not ok:
            print("FAILED", sub, m, flush=True)
            continue
        with gzip.open(fn, "wt", newline="") as f:
            w = csv.writer(f)
            w.writerow(["created_utc", "score", "num_comments", "title"])
            for r in rows:
                w.writerow([r.get("created_utc"), r.get("score"), r.get("num_comments"), r.get("title")])
        print("OK", sub, f"{m:%Y-%m}", len(rows), flush=True)
print("DONE", flush=True)
