"""Pull every submission (metadata + title only) from a subreddit via the public Arctic Shift archive API.
Usage: python3 -I pull_reddit_arcticshift.py <subreddit> <after YYYY-MM-DD> <out.csv.gz>
Pages forward by created_utc with limit=auto. Sleeps 1.5 s between calls; backs off on errors. No auth, no personal data
requested beyond public post metadata (author field is NOT requested)."""
import sys, json, time, gzip, csv, os, urllib.request, urllib.parse, datetime
sub, after, out = sys.argv[1], sys.argv[2], sys.argv[3]
API = "https://arctic-shift.photon-reddit.com/api/posts/search"
FIELDS = "id,created_utc,title,num_comments,score,link_flair_text"
cur = int(datetime.datetime.strptime(after, "%Y-%m-%d").replace(tzinfo=datetime.timezone.utc).timestamp())
seen = set(); mode = "wt"
if os.path.exists(out):
    with gzip.open(out, "rt") as f:
        rows = list(csv.DictReader(f))
    if rows:
        cur = max(int(r["created_utc"]) for r in rows); seen = {r["id"] for r in rows}; mode = "at"
f = gzip.open(out, mode, newline=""); w = csv.writer(f)
if mode == "wt": w.writerow(FIELDS.split(","))
n = 0; fails = 0
while True:
    q = urllib.parse.urlencode(dict(subreddit=sub, after=cur, limit="auto", sort="asc", fields=FIELDS))
    try:
        with urllib.request.urlopen(urllib.request.Request(API + "?" + q, headers={"User-Agent": "research-script/1.0"}), timeout=120) as r:
            d = json.load(r)
    except Exception as e:
        d = {"error": str(e)}
    if d.get("error") or d.get("data") is None:
        fails += 1; print("err", d.get("error"), flush=True)
        if fails > 8: break
        time.sleep(10 * fails); continue
    fails = 0; data = d["data"]
    new = [x for x in data if x["id"] not in seen]
    for x in new:
        seen.add(x["id"]); w.writerow([x.get(k) for k in FIELDS.split(",")])
    n += len(new)
    if not data or not new: break
    cur = max(int(x["created_utc"]) for x in data)
    print(sub, datetime.datetime.utcfromtimestamp(cur).date(), n, flush=True)
    f.flush(); time.sleep(1.5)
f.close(); print("done", sub, n)
