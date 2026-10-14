"""Query Common Crawl CDX indexes for given URL patterns across crawls (2019 onward).
Usage: python3 cc_index.py <outdir> <since YYYY-MM> pattern1 [pattern2 ...]
Writes <outdir>/idx_<crawl>_<slug>.jsonl ; skips files that already exist. Retries on the flaky proxy."""
import json, os, sys, time, urllib.request, urllib.parse
out, since = sys.argv[1], sys.argv[2]; pats = sys.argv[3:]
coll = json.load(open(os.path.join(out, "collinfo.json")))
def get(url, tries=6):
    for i in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "academic-research-cc-client"}), timeout=120).read().decode()
        except urllib.error.HTTPError as e:
            if e.code == 404: return ""
            time.sleep(5 * (i + 1))
        except Exception as e:
            time.sleep(5 * (i + 1))
    return None
for c in coll:
    if c["from"][:7] < since: continue
    for p in pats:
        slug = p.replace("/", "_").replace("*", "").replace(".", "-").strip("_")
        fn = os.path.join(out, f"idx_{c['id']}_{slug}.jsonl")
        if os.path.exists(fn): continue
        base = c["cdx-api"] + "?url=" + urllib.parse.quote(p, safe="*/:") + "&output=json&fl=timestamp,url,status,length,offset,filename,mime"
        np = get(base + "&showNumPages=true")
        if np is None: print("FAIL", c["id"], p); continue
        try: pages = json.loads(np)["pages"] if np.strip() else 0
        except Exception: pages = 1
        txt = ""
        ok = True
        for pg in range(pages):
            t = get(base + f"&page={pg}")
            if t is None: ok = False; break
            txt += t
            time.sleep(1.5)
        if not ok: print("FAIL", c["id"], p); continue
        open(fn, "w").write(txt)
        print(c["id"], p, pages, txt.count("\n"), flush=True)
        time.sleep(1.5)
