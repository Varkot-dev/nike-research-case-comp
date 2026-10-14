"""Snapshot of public YouTube channel pages (no login, no API key): subscriber count and the ~30 most recent
long-form videos with view counts and relative publish age, for Nike and rival brand channels.

Source: https://www.youtube.com/@<handle>/videos  (embedded ytInitialData JSON)
Snapshot only (no history). Re-run: python3 -I pull_youtube_channels.py <rawdir> <outcsv>
"""
import json, os, re, sys, time, urllib.request, csv

RAW = sys.argv[1] if len(sys.argv) > 1 else "../raw/youtube"
OUTCSV = sys.argv[2] if len(sys.argv) > 2 else "../youtube_channel_snapshot_videos.csv"
os.makedirs(RAW, exist_ok=True)
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
HANDLES = ["nike", "nikerunning", "jordan", "nikebasketball", "nikefootball", "adidas",
           "adidasoriginals", "newbalance", "HOKAOneOne", "OnRunning", "asics", "PUMA", "lululemon", "BrooksRunning", "saucony"]


def parse_num(t):
    t = t.replace(",", "").strip()
    m = re.match(r"([\d.]+)\s*([KMB]?)", t)
    if not m:
        return None
    mult = {"": 1, "K": 1e3, "M": 1e6, "B": 1e9}[m.group(2)]
    for word, mu in (("thousand", 1e3), ("million", 1e6), ("billion", 1e9)):
        if word in t:
            mult = mu
    return float(m.group(1)) * mult


rows = []
for h in HANDLES:
    fn = os.path.join(RAW, f"{h}.html")
    if not os.path.exists(fn):
        req = urllib.request.Request(f"https://www.youtube.com/@{h}/videos",
                                     headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                open(fn, "wb").write(r.read())
        except Exception as e:
            print("ERR", h, e, flush=True)
            continue
        time.sleep(4)
    s = open(fn, encoding="utf-8", errors="replace").read()
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", s)
    if not m:
        print("no data", h)
        continue
    txt = m.group(1)
    subs = re.search(r'"content":"([\d.,]+[KMB]?) subscribers"', txt)
    subs = parse_num(subs.group(1)) if subs else None
    d = json.loads(txt)
    vids = []

    def walk(o):
        if isinstance(o, dict):
            if "lockupMetadataViewModel" in o:
                lm = o["lockupMetadataViewModel"]
                title = lm.get("title", {}).get("content")
                parts = []
                for row in lm.get("metadata", {}).get("contentMetadataViewModel", {}).get("metadataRows", []):
                    for p in row.get("metadataParts", []):
                        parts.append(p.get("accessibilityLabel") or p.get("text", {}).get("content", ""))
                vids.append((title, parts))
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(d)
    for title, parts in vids:
        views = next((p for p in parts if "view" in p.lower()), None)
        age = next((p for p in parts if "ago" in p), None)
        rows.append({"handle": h, "subscribers": subs, "title": title, "views_text": views,
                     "views": parse_num(views) if views else None, "age_text": age})
    print("OK", h, subs, len(vids), flush=True)

with open(OUTCSV, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["handle", "subscribers", "title", "views_text", "views", "age_text"])
    w.writeheader()
    w.writerows(rows)
