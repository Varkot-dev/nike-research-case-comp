"""Monthly count buckets of creatives shown in the US per advertiser, Google Ads Transparency Center public RPC.
The RPC returns only a bucketed total ('4' low, '5' high, e.g. 1000-2000). One request per advertiser-month, 45 s apart.
Usage: python3 -I pull_google_ads_monthly_counts.py <rawdir> <outcsv>"""
import sys, os, json, time, urllib.request, urllib.parse, csv, calendar
RAW, OUT = sys.argv[1], sys.argv[2]; os.makedirs(RAW, exist_ok=True)
ADV = {"Nike, Inc.": "AR16735076323512287233", "adidas America, Inc": "AR14017378248766259201", "On AG": "AR01173884174826733569",
       "New Balance Athletic Shoe, Inc.": "AR04323445746671026177"}
MONTHS = ["2024-01", "2024-10", "2025-04", "2025-10", "2026-04", "2026-09"]
URL = "https://adstransparency.google.com/anji/_/rpc/SearchService/SearchCreatives?authuser=0"
H = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Chrome/120", "Content-Type": "application/x-www-form-urlencoded"}
rows = []
for ym in MONTHS:
    y, m = map(int, ym.split("-")); last = calendar.monthrange(y, m)[1]
    for name, aid in ADV.items():
        fn = os.path.join(RAW, f"count_{aid}_{ym}.json")
        if not os.path.exists(fn):
            req = {"2": 40, "3": {"6": int(f"{y}{m:02d}01"), "7": int(f"{y}{m:02d}{last}"), "8": [2840], "12": {"1": "", "2": True}, "13": {"1": [aid]}}, "7": {"1": 1, "2": 0, "3": 2840}}
            body = urllib.parse.urlencode({"f.req": json.dumps(req)}).encode()
            try:
                d = json.load(urllib.request.urlopen(urllib.request.Request(URL, data=body, headers=H), timeout=60))
            except Exception as e:
                d = {"error": str(e)}
            if "error" not in d and d.get("5") != 429: json.dump(d, open(fn, "w"))
            else: print("fail", name, ym, d, flush=True)
            time.sleep(45)
        if os.path.exists(fn):
            d = json.load(open(fn))
            rows.append(dict(month=ym, advertiser=name, advertiser_id=aid, creatives_low=d.get("4"), creatives_high=d.get("5"), n_first_page=len(d.get("1", []))))
            print(rows[-1], flush=True)
w = csv.DictWriter(open(OUT, "w"), fieldnames=["month", "advertiser", "advertiser_id", "creatives_low", "creatives_high", "n_first_page"]); w.writeheader(); w.writerows(rows)
