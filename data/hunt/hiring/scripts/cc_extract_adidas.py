"""Extract adidas careers totals (data-count-to) from archived careers.adidas-group.com/jobs pages in Common Crawl.
Usage: python3 cc_extract_adidas.py <ccdir> <outcsv> [max_per_crawl]"""
import gzip, json, glob, os, re, sys, time, csv, urllib.request, urllib.parse
ccdir, outcsv = sys.argv[1], sys.argv[2]; cap = int(sys.argv[3]) if len(sys.argv) > 3 else 12
w = csv.writer(open(outcsv, "w", newline="")); w.writerow(["crawl", "timestamp", "url", "filter", "total"])
for fn in sorted(glob.glob(os.path.join(ccdir, "cdx_*.jsonl.gz"))):
    crawl = os.path.basename(fn)[4:-9]
    R = [json.loads(l) for l in gzip.open(fn, "rt")]
    def filt(u):
        q = urllib.parse.parse_qs(urllib.parse.urlparse(u).query)
        return {k: v for k, v in q.items() if k in ("team", "location", "type", "brand", "search")}
    R.sort(key=lambda r: (len(filt(r["url"])) > 0, r["timestamp"]))
    n = 0
    for r in R:
        if n >= cap: break
        f = filt(r["url"])
        if f and not set(f) <= {"team"}: continue
        off, ln = int(r["offset"]), int(r["length"])
        try:
            b = urllib.request.urlopen(urllib.request.Request("https://data.commoncrawl.org/" + r["filename"], headers={"Range": f"bytes={off}-{off+ln-1}", "User-Agent": "academic-research-cc-client"}), timeout=90).read()
            t = gzip.decompress(b).decode("utf-8", "replace")
        except Exception: continue
        n += 1; time.sleep(0.3)
        m = re.search(r'data-count-to="(\d+)"', t)
        w.writerow([crawl, r["timestamp"], r["url"][:300], json.dumps(f), m.group(1) if m else ""])
    print(crawl, n, flush=True)
