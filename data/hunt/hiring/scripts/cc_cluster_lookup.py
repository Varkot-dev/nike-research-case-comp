"""Look up Common Crawl CDX records for SURT prefixes WITHOUT the index server:
binary-search each crawl's cluster.idx on data.commoncrawl.org with HTTP Range requests,
then range-fetch only the matching compressed cdx blocks.
Usage: python3 cc_cluster_lookup.py <outdir> <since YYYY-MM> surt_prefix1 [surt_prefix2 ...]
  e.g. "com,nike,jobs)/" "com,nike,careers)/"
Output: <outdir>/cdx_<crawl>.jsonl.gz, status-200 captures only."""
import json, os, sys, time, gzip, urllib.request
out, since = sys.argv[1], sys.argv[2]; prefixes = sys.argv[3:]
BASE = "https://data.commoncrawl.org/"
def rng(path, a, b):
    for i in range(6):
        try:
            req = urllib.request.Request(BASE + path, headers={"Range": f"bytes={a}-{b}", "User-Agent": "academic-research-cc-client"})
            return urllib.request.urlopen(req, timeout=120).read()
        except Exception as e:
            time.sleep(4 * (i + 1))
    raise RuntimeError("range fail " + path)
def size(path):
    for i in range(6):
        try:
            req = urllib.request.Request(BASE + path, method="HEAD", headers={"User-Agent": "academic-research-cc-client"})
            return int(urllib.request.urlopen(req, timeout=60).headers["Content-Length"])
        except Exception: time.sleep(4 * (i + 1))
    raise RuntimeError("head fail")
def line_at(path, pos, total):
    """first complete line starting at or after pos -> (line_start, line)"""
    chunk = rng(path, pos, min(pos + 8191, total - 1))
    if pos == 0: s = 0
    else:
        s = chunk.find(b"\n") + 1
    e = chunk.find(b"\n", s)
    while e == -1:
        chunk += rng(path, pos + len(chunk), min(pos + len(chunk) + 8191, total - 1)); e = chunk.find(b"\n", s)
    return pos + s, chunk[s:e].decode("utf-8", "replace")
coll = json.load(open(os.path.join(out, "collinfo.json")))
for c in coll:
    if c["from"][:7] < since: continue
    fn = os.path.join(out, f"cdx_{c['id']}.jsonl.gz")
    if os.path.exists(fn): continue
    path = f"cc-index/collections/{c['id']}/indexes/cluster.idx"
    try:
        total = size(path)
        recs = []
        for pre in prefixes:
            lo, hi = 0, total
            while hi - lo > 9000:
                mid = (lo + hi) // 2
                st, ln = line_at(path, mid, total)
                if ln.split(" ")[0] < pre: lo = mid
                else: hi = mid
            # scan forward from lo collecting cluster lines; the block containing prefix starts at the last line < pre
            buf = rng(path, lo, min(lo + 200000, total - 1)).decode("utf-8", "replace").split("\n")[1:-1]
            blocks, prev = [], None
            for ln in buf:
                parts = ln.split("\t"); key = parts[0].split(" ")[0]
                if key < pre: prev = parts; continue
                if prev is not None and not blocks: blocks.append(prev)
                if key.startswith(pre) or (key < pre + "￿" and key.startswith(pre[:-1])): blocks.append(parts); continue
                if not blocks: blocks.append(parts) if prev is None else None
                break
            seen = set()
            for b in blocks:
                cdxfile, off, ln_ = b[1], int(b[2]), int(b[3])
                if (cdxfile, off) in seen: continue
                seen.add((cdxfile, off))
                data = gzip.decompress(rng(f"cc-index/collections/{c['id']}/indexes/{cdxfile}", off, off + ln_ - 1)).decode("utf-8", "replace")
                for l in data.split("\n"):
                    if l.startswith(pre):
                        surt, ts, js = l.split(" ", 2)
                        r = json.loads(js)
                        if r.get("status") != "200": continue
                        recs.append({"crawl": c["id"], "timestamp": ts, "url": r["url"], "length": r["length"], "offset": r["offset"], "filename": r["filename"], "digest": r.get("digest")})
                time.sleep(0.3)
        with gzip.open(fn, "wt") as f:
            for r in recs: f.write(json.dumps(r) + "\n")
        print(c["id"], len(recs), flush=True)
    except Exception as e:
        print("FAIL", c["id"], e, flush=True)
    time.sleep(0.5)
