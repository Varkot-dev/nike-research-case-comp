"""Zappos public pages: (1) running-shoe category listings (all pages) and model searches -> product rows with
review count, rating, price, sale flag; (2) review pages (25 per page) for selected productIds -> review date + stars.
Usage: python3 -I pull_zappos.py listings <rawdir>
       python3 -I pull_zappos.py reviews <rawdir> <productIds comma list> [maxpages]
Sleeps 2.5 s between requests. No login, no cookies kept, no personal data requested."""
import sys, os, json, time, subprocess, re, gzip
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
def get(url):
    for a in range(3):
        cp = subprocess.run(["curl", "-s", "-L", "--compressed", "-A", UA, "-H", "Accept-Language: en-US,en;q=0.9", "--max-time", "60", "-w", "\n%{http_code}", url], capture_output=True, text=True)
        body, _, code = cp.stdout.rpartition("\n")
        time.sleep(2.5)
        if code == "200": return body
        time.sleep(20 * (a + 1))
    return None
def state(h):
    i = h.find("window.__INITIAL_STATE__"); j = h.find("=", i) + 1
    return json.JSONDecoder().raw_decode(h[j:].lstrip())[0]
mode, raw = sys.argv[1], sys.argv[2]
os.makedirs(raw, exist_ok=True)
if mode == "listings":
    out = gzip.open(os.path.join(raw, "zappos_listings.jsonl.gz"), "wt")
    jobs = [("cat", "men-running-shoes"), ("cat", "women-running-shoes")]
    terms = ["nike pegasus", "nike vomero", "nike structure", "nike invincible", "hoka clifton", "hoka bondi", "asics novablast",
             "asics gel nimbus", "asics gel kayano", "brooks ghost", "brooks adrenaline", "on cloudmonster", "on cloudsurfer",
             "saucony ride", "new balance 880", "saucony triumph", "nike pegasus 41", "nike vomero 17", "hoka clifton 9", "asics novablast 4"]
    jobs += [("search", t) for t in terms]
    for kind, key in jobs:
        p = 0
        while True:
            url = (f"https://www.zappos.com/{key}?p={p}" if kind == "cat" else f"https://www.zappos.com/search?term={key.replace(' ', '%20')}&p={p}")
            h = get(url)
            if not h: break
            pr = state(h)["products"]; lst = pr.get("list") or []
            for x in lst:
                x.pop("relatedStyles", None); x.pop("imageMap", None)
                out.write(json.dumps({"job": kind, "key": key, "page": p, "total": pr.get("totalProductCount"), **x}) + "\n")
            print(kind, key, p, len(lst), pr.get("totalProductCount"), flush=True)
            if len(lst) < 100 or (p + 1) * 100 >= (pr.get("totalProductCount") or 0): break
            p += 1
    out.close()
else:
    ids = sys.argv[3].split(","); maxp = int(sys.argv[4]) if len(sys.argv) > 4 else 80
    out = gzip.open(os.path.join(raw, f"zappos_reviews_{int(time.time())}.jsonl.gz"), "wt")
    for pid in ids:
        n = 0
        for page in range(1, maxp + 1):
            url = f"https://www.zappos.com/product/review/{pid}" + (f"/page/{page}/orderBy/newest" if page > 1 else "/page/1/orderBy/newest")
            h = get(url)
            if not h: break
            revs = re.findall(r'"reviewDate":(\d+)', h)
            # pull structured review objects: overall rating near reviewDate
            objs = re.findall(r'\{[^{}]*"reviewDate":\d+[^{}]*\}', h)
            got = 0
            for o in objs:
                d = {k: v for k, v in re.findall(r'"(reviewDate|overallRating|reviewId|id|productId|shoeSize|incentivizedReview|customerRewardReview|premierReview|powerReview|source|comfortRating|hasMedia)":"?([^",}]*)', o)}
                if "reviewDate" in d:
                    d["pid"] = pid; d["page"] = page; out.write(json.dumps(d) + "\n"); got += 1
            tot = re.search(r'"totalReviews":"?(\d+)', h)
            n += got
            print(pid, page, got, tot.group(1) if tot else None, flush=True)
            if got == 0 or (tot and n >= int(tot.group(1))): break
        out.flush()
    out.close()
