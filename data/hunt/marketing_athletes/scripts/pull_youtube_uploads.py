"""Full public upload list per brand YouTube channel via the public web client (innertube browse continuation),
no login, no personal data. Captures title, view count and relative publish age; plus channel subscriber count.
Usage: python3 -I pull_youtube_uploads.py <rawdir> <outcsv> [maxpages]"""
import json, os, re, sys, time, urllib.request, csv
RAW, OUT = sys.argv[1], sys.argv[2]; MAXP = int(sys.argv[3]) if len(sys.argv) > 3 else 40
os.makedirs(RAW, exist_ok=True)
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
H = {"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"}
CH = {"nike": "@nike", "adidas": "@adidas", "puma": "@PUMA", "jordan": "@jordan", "underarmour": "@underarmour",
      "newbalance": "@newbalance", "asics": "@ASICSAmerica", "on": "@onrunning", "hoka": "@HOKA", "lululemon": "@lululemon",
      "nikefootball": "@nikefootball", "adidasfootball": "@adidasfootball", "nikebasketball": "@nikebasketball",
      "nikerunning": "@nikerunning", "adidasoriginals": "@adidasoriginals", "salomon": "@SalomonTV"}
def num(t):
    if not t: return None
    t = t.replace(",", "")
    m = re.search(r"([\d.]+)\s*([KMB])?", t)
    if not m: return None
    mult = {None: 1, "K": 1e3, "M": 1e6, "B": 1e9}[m.group(2)]
    return float(m.group(1)) * mult
def walk(o, out, conts, path=""):
    if isinstance(o, dict):
        if "lockupMetadataViewModel" in o:
            lm = o["lockupMetadataViewModel"]; parts = []
            for row in lm.get("metadata", {}).get("contentMetadataViewModel", {}).get("metadataRows", []):
                for p in row.get("metadataParts", []): parts.append(p.get("accessibilityLabel") or p.get("text", {}).get("content", ""))
            out.append((lm.get("title", {}).get("content"), parts))
        if "videoRenderer" in o:
            v = o["videoRenderer"]
            out.append((v.get("title", {}).get("runs", [{}])[0].get("text"),
                        [v.get("viewCountText", {}).get("simpleText", ""), v.get("publishedTimeText", {}).get("simpleText", "")]))
        if "continuationCommand" in o and "continuationItemRenderer" in path and "engagementPanel" not in path and "chip" not in path:
            conts.append(o["continuationCommand"]["token"])
        for k, v in o.items(): walk(v, out, conts, path + "/" + k)
    elif isinstance(o, list):
        for v in o: walk(v, out, conts, path)
rows = []
for name, h in CH.items():
    try:
        s = urllib.request.urlopen(urllib.request.Request(f"https://www.youtube.com/{h}/videos", headers=H), timeout=60).read().decode("utf-8", "replace")
    except Exception as e:
        print("ERR", name, e); continue
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", s)
    if not m: print("nodata", name); continue
    key = re.search(r'"INNERTUBE_API_KEY":"([^"]+)"', s).group(1)
    ver = re.search(r'"INNERTUBE_CLIENT_VERSION":"([^"]+)"', s).group(1)
    subs = re.search(r'"content":"([\d.,]+[KMB]?) subscribers"', m.group(1))
    subs = num(subs.group(1)) if subs else None
    cid = re.search(r'"externalId":"(UC[^"]+)"', s); cid = cid.group(1) if cid else None
    vids, conts = [], []; walk(json.loads(m.group(1)), vids, conts)
    pages = 0
    while conts and pages < MAXP:
        tok = conts[-1]; conts = []
        body = json.dumps({"context": {"client": {"clientName": "WEB", "clientVersion": ver, "hl": "en", "gl": "US"}}, "continuation": tok}).encode()
        d = None
        for k in range(4):
            try:
                d = json.load(urllib.request.urlopen(urllib.request.Request(f"https://www.youtube.com/youtubei/v1/browse?key={key}&prettyPrint=false", data=body, headers={**H, "Content-Type": "application/json"}), timeout=60)); break
            except Exception as e:
                print("ERRc", name, e); time.sleep(20 * (k + 1))
        if d is None: break
        walk(d, vids, conts); pages += 1; time.sleep(1.5)
    for t, parts in vids:
        views = next((p for p in parts if "view" in p.lower()), None)
        age = next((p for p in parts if "ago" in p), None)
        rows.append(dict(channel=name, handle=h, channel_id=cid, subscribers=subs, title=t, views_text=views, views=num(views), age_text=age, pulled="2026-10-14"))
    print("OK", name, cid, subs, len(vids), pages, flush=True)
    time.sleep(3)
with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
