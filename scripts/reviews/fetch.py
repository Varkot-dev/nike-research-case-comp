"""Polite cached fetcher (curl). Usage: python3 -I fetch.py <outdir> <delay_s> < urls.txt
Writes <outdir>/<sha1[:16]>.html, appends <outdir>/fetch_log.jsonl. Backs off 90s+ on 429."""
import sys, os, json, time, hashlib, subprocess
out, delay = sys.argv[1], float(sys.argv[2])
os.makedirs(out, exist_ok=True)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
log = open(os.path.join(out, "fetch_log.jsonl"), "a")
for url in [l.strip() for l in sys.stdin if l.strip()]:
    fn = os.path.join(out, hashlib.sha1(url.encode()).hexdigest()[:16] + ".html")
    if os.path.exists(fn) and os.path.getsize(fn) > 2000:
        continue
    st = 0
    for attempt in range(4):
        try:
            cp = subprocess.run(["curl", "-s", "-L", "--compressed", "-A", UA, "-H", "Accept-Language: en-US,en;q=0.9",
                                 "-o", fn + ".part", "-w", "%{http_code}", "--max-time", "120", url],
                                capture_output=True, text=True, timeout=150)
            st = int(cp.stdout.strip() or 0)
        except Exception as e:
            st = -1
        if st == 200 and os.path.exists(fn + ".part"):
            os.replace(fn + ".part", fn); break
        if os.path.exists(fn + ".part"): os.remove(fn + ".part")
        if st in (400, 403, 404, 405): break
        time.sleep(90 * (attempt + 1) if st == 429 else delay * 4)
    log.write(json.dumps({"t": time.strftime("%Y-%m-%dT%H:%M:%S"), "url": url, "status": st, "file": fn}) + "\n"); log.flush()
    print(st, url, flush=True)
    time.sleep(delay)
