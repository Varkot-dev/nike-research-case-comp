"""Pull WARN notice rows from warntracker.com company pages (public, server-rendered __NEXT_DATA__).
Usage: python3 pull_warntracker.py <outdir> slug1 slug2 ..."""
import json, re, sys, time, urllib.request, csv, os
out = sys.argv[1]; rows = []
for slug in sys.argv[2:]:
    url = f"https://www.warntracker.com/company/{slug}"
    try:
        h = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (academic research)"}), timeout=60).read().decode()
    except Exception as e:
        print(slug, "FAIL", e); continue
    open(os.path.join(out, f"{slug}.html"), "w").write(h)
    m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', h, re.S)
    pp = json.loads(m.group(1))["props"]["pageProps"]
    for r in pp.get("data") or []:
        rows.append({"slug": slug, "company": r.get("Company Name"), "raw_name": r.get("Company Name in Raw Data"),
                     "state": r.get("State"), "city": r.get("\U0001F4CD City/Jurisdiction"), "notice_date": r.get("Notice Date"),
                     "layoff_date": r.get("Layoff date"), "workers": r.get("# Laid off")})
    print(slug, len(pp.get("data") or []), json.dumps(pp.get("h1bData"))[:200])
    time.sleep(2)
w = csv.DictWriter(open(os.path.join(out, "warntracker_rows.csv"), "w", newline=""), fieldnames=list(rows[0].keys()))
w.writeheader(); w.writerows(rows)
