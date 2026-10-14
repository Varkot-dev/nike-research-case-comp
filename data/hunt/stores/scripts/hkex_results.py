"""Download HKEX results announcements / operational updates for Topsports (6110) and Pou Sheng (3813)
since 2019 and convert to text. Usage: python3 -I hkex_results.py <rawdir>"""
import json, os, sys, time, re, subprocess, urllib.request, html
UA = {"User-Agent": "Mozilla/5.0 (academic research script)"}
raw = sys.argv[1]
KEEP = re.compile(r"(RESULTS FOR|INTERIM RESULTS|ANNUAL RESULTS|OPERATIONAL UPDATE|THREE MONTHS ENDED|NINE MONTHS ENDED|FINAL RESULTS)", re.I)
for name in ("topsports", "pousheng"):
    d = json.loads(json.load(open(os.path.join(raw, f"list_{name}.json")))["result"])
    od = os.path.join(raw, name); os.makedirs(od, exist_ok=True)
    for x in d:
        t = html.unescape(x["TITLE"])
        if not KEEP.search(t) or "POLL" in t.upper() or not x["FILE_LINK"].endswith(".pdf"): continue
        dd = x["DATE_TIME"][6:10] + x["DATE_TIME"][3:5] + x["DATE_TIME"][0:2]
        base = os.path.join(od, f"{dd}_{os.path.basename(x['FILE_LINK'])[:-4]}")
        if os.path.exists(base + ".txt"): continue
        b = urllib.request.urlopen(urllib.request.Request("https://www1.hkexnews.hk" + x["FILE_LINK"], headers=UA), timeout=120).read()
        open(base + ".pdf", "wb").write(b)
        subprocess.run(["pdftotext", "-layout", base + ".pdf", base + ".txt"])
        os.remove(base + ".pdf")
        open(base + ".title", "w").write(t)
        print(dd, t[:80], flush=True); time.sleep(1)
