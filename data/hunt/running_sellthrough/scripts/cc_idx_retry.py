"""List Common Crawl captures for URL patterns with retries (the index server is slow and often resets through the proxy).
usage: python3 -I cc_idx_retry.py <outdir> "<pattern>" crawl1 crawl2 ...   Output: <outdir>/<safe pattern>__<crawl>.jsonl (status 200 captures)."""
import sys, subprocess, time, os, json, re
out, PAT = sys.argv[1], sys.argv[2]
safe = re.sub(r"[^A-Za-z0-9]+", "_", PAT)
for c in sys.argv[3:]:
    fn = os.path.join(out, f"{safe}__{c}.jsonl")
    if os.path.exists(fn): continue
    pages = None
    for t in range(8):
        r = subprocess.run(["curl", "-sS", "-m", "120", f"https://index.commoncrawl.org/{c}-index?url={PAT}&showNumPages=true"], capture_output=True).stdout
        try: pages = json.loads(r)["pages"]; break
        except Exception: time.sleep(6 + 4 * t)
    if pages is None: print("giveup", PAT, c, flush=True); continue
    data = b""; ok = True
    for p in range(min(pages, 6)):
        got = False
        for t in range(8):
            r = subprocess.run(["curl", "-sS", "-m", "120", f"https://index.commoncrawl.org/{c}-index?url={PAT}&output=json&filter=status:200&page={p}"], capture_output=True).stdout
            if r.lstrip().startswith(b'{"urlkey') or r.strip() == b"": data += r; got = True; break
            if b"No Captures" in r: got = True; break
            time.sleep(6 + 4 * t)
        ok &= got
    open(fn, "wb").write(data); print(c, PAT, pages, data.count(b"\n"), "ok" if ok else "partial", flush=True)
