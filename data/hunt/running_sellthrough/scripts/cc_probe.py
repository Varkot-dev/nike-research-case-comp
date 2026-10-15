"""Probe Common Crawl index for pages of running-shoe retailers. Usage: python3 -I cc_probe.py <outcsv>"""
import sys, json, subprocess, time, csv
crawls = [c for c in ["CC-MAIN-2024-33","CC-MAIN-2024-42","CC-MAIN-2024-51","CC-MAIN-2025-13","CC-MAIN-2025-26","CC-MAIN-2025-38","CC-MAIN-2025-51","CC-MAIN-2026-12","CC-MAIN-2026-25","CC-MAIN-2026-34","CC-MAIN-2026-39"]]
pats = ["www.amazon.com/Best-Sellers-Clothing-Shoes-Jewelry-Mens-Running-Shoes*","www.amazon.com/gp/bestsellers/fashion/679286011*","www.amazon.com/*Nike-Pegasus*",
        "www.runningwarehouse.com/*Pegasus*","www.runningwarehouse.com/Nike_*","www.zappos.com/p/nike-pegasus*","www.fleetfeet.com/products/*pegasus*","www.roadrunnersports.com/*Pegasus*","www.jackrabbit.com/*pegasus*"]
def q(c,p):
    for a in range(3):
        cp = subprocess.run(["curl","-s","-m","60",f"https://index.commoncrawl.org/{c}-index?url={p}&output=json&limit=200"],capture_output=True,text=True)
        if cp.stdout.strip(): return cp.stdout
        time.sleep(3)
    return ""
w = csv.writer(open(sys.argv[1],"w",newline="")); w.writerow(["crawl","pattern","n_captures","sample_url"])
for p in pats:
    for c in crawls:
        t = q(c,p); L=[l for l in t.splitlines() if l.startswith("{") and "\"url\"" in l]
        s = json.loads(L[0])["url"] if L else ""
        w.writerow([c,p,len(L),s]); print(c,p,len(L),s,flush=True); time.sleep(1)
