"""Nike SNKRS public product feed (the JSON behind nike.com/launch). No login.
https://api.nike.com/product_feed/threads/v3/?anchor={a}&count=50&filter=marketplace({M})&filter=language({L})&filter=channelId(010794e5-35fe-4e32-aaff-cd2c74f89d61)&filter=exclusiveAccess(true,false)
Keeps per-thread, per-product fields: thread publish/view dates, product style-color, launch method and dates, full and current price, availability, merch status.
Raw pages saved gzipped to raw/snkrs/{M}/page_{n}.json.gz. Tidy: snkrs_threads_{M}.csv
Usage: python3 pull_snkrs_feed.py US en
"""
import json, gzip, os, sys, time, csv, urllib.request, urllib.parse
M = sys.argv[1] if len(sys.argv) > 1 else "US"; L = sys.argv[2] if len(sys.argv) > 2 else "en"
BASE = "/home/user/nike-research-case-comp/data/hunt/apps_digital"
RAW = f"{BASE}/raw/snkrs/{M}"; os.makedirs(RAW, exist_ok=True)
CH = "010794e5-35fe-4e32-aaff-cd2c74f89d61"
rows = []; a = 0; n = 0
while True:
    fn = f"{RAW}/page_{n:04d}.json.gz"
    if os.path.exists(fn):
        d = json.load(gzip.open(fn))
    else:
        q = f"anchor={a}&count=50&filter=marketplace({M})&filter=language({L})&filter=channelId({CH})&filter=exclusiveAccess(true,false)"
        url = "https://api.nike.com/product_feed/threads/v3/?" + urllib.parse.quote(q, safe="=&")
        d = None
        for i in range(4):
            try:
                with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=60) as r:
                    d = json.load(r); break
            except Exception as e:
                print("ERR", n, e, flush=True); time.sleep(10 * (i + 1))
        if d is None: break
        json.dump(d, gzip.open(fn, "wt")); time.sleep(1.0)
    objs = d.get("objects", [])
    if not objs: break
    for o in objs:
        pc = o.get("publishedContent", {}) or {}
        props = pc.get("properties", {}) or {}
        for p in o.get("productInfo", []) or []:
            mp = p.get("merchProduct", {}) or {}; pr = p.get("merchPrice", {}) or {}; lv = p.get("launchView", {}) or {}
            av = p.get("availability", {}) or {}
            sk = p.get("skus", []) or []
            avs = p.get("availableSkus", []) or []
            rows.append([M, o.get("id"), pc.get("createdDateTime"), pc.get("viewStartDate"), o.get("lastFetchTime"),
                         mp.get("styleColor"), mp.get("productType"), mp.get("status"), mp.get("commerceStartDate"), mp.get("publishType"),
                         (mp.get("genders") or [None])[0], (mp.get("brand") or ""), mp.get("exclusiveAccess"),
                         lv.get("method"), lv.get("startEntryDate"), lv.get("stopEntryDate"),
                         pr.get("fullPrice"), pr.get("currentPrice"), pr.get("discounted"), pr.get("currency"),
                         av.get("available"), len(sk), sum(1 for x in avs if x.get("available")), (p.get("productContent", {}) or {}).get("fullTitle") or (p.get("productContent", {}) or {}).get("title")])
    n += 1; a += 50
    nxt = d.get("pages", {}).get("next")
    if n % 20 == 0: print(M, n, len(rows), flush=True)
    if not nxt: break
cols = ["marketplace", "thread_id", "thread_created", "view_start", "fetched", "style_color", "product_type", "merch_status", "commerce_start", "publish_type",
        "gender", "brand", "exclusive_access", "launch_method", "launch_start", "launch_stop", "full_price", "current_price", "discounted", "currency",
        "available", "n_skus", "n_skus_available", "title"]
with open(f"{BASE}/snkrs_threads_{M}.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(cols); w.writerows(rows)
print("done", M, n, len(rows))
