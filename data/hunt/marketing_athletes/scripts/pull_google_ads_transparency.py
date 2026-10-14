"""Page through all creatives an advertiser showed in a region via Google Ads Transparency Center public RPC
(adstransparency.google.com, no login). Records creative id, format, first/last shown (epoch), days shown.
Usage: python3 -I pull_google_ads_transparency.py <rawdir> <outcsv> [region=2840]"""
import sys, os, json, time, urllib.request, urllib.parse, csv, datetime
RAW, OUT = sys.argv[1], sys.argv[2]; REG = int(sys.argv[3]) if len(sys.argv) > 3 else 2840
os.makedirs(RAW, exist_ok=True)
ADV = {"Nike, Inc.": "AR16735076323512287233", "adidas America, Inc": "AR14017378248766259201",
       "On AG": "AR01173884174826733569", "New Balance Athletic Shoe, Inc.": "AR04323445746671026177",
       "Under Armour, Inc.": "AR16916677161513910273", "Brooks Sports Inc": "AR02322649044444250113",
       "Skechers U.S.A., Inc": "AR10368367437014892545", "Nike Retail Services Inc": "AR04810212910225686529"}
URL = "https://adstransparency.google.com/anji/_/rpc/SearchService/SearchCreatives?authuser=0"
H = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Chrome/120", "Content-Type": "application/x-www-form-urlencoded"}
def call(req):
    body = urllib.parse.urlencode({"f.req": json.dumps(req)}).encode()
    for k in range(6):
        try:
            d = json.load(urllib.request.urlopen(urllib.request.Request(URL, data=body, headers=H), timeout=60))
            if d.get("5") == 429 or (isinstance(d.get("5"), int) and d.get("9")): raise Exception("429 in body")
            return d
        except Exception as e:
            print("retry", e, flush=True); time.sleep(20 * (k + 1))
    return None
rows = []
for name, aid in ADV.items():
    fn = os.path.join(RAW, f"creatives_{aid}_{REG}.jsonl")
    if not os.path.exists(fn):
        tok = None; n = 0
        with open(fn + ".part", "w") as f:
            while True:
                req = {"2": 100, "3": {"8": [REG], "12": {"1": "", "2": True}, "13": {"1": [aid]}}, "7": {"1": 1, "2": 0, "3": REG}}
                if tok: req["4"] = tok
                d = call(req)
                if d is None: print("FAILED", name, n); break
                f.write(json.dumps(d) + "\n"); n += len(d.get("1", []))
                tok = d.get("2")
                if not tok or not d.get("1"): break
                time.sleep(3)
        os.rename(fn + ".part", fn); print("done", name, n, flush=True)
    for line in open(fn):
        d = json.loads(line)
        for c in d.get("1", []):
            fs = int(c["6"]["1"]) if "6" in c else None; ls = int(c["7"]["1"]) if "7" in c else None
            rows.append(dict(advertiser=name, advertiser_id=aid, region=REG, creative_id=c.get("2"), format=c.get("4"),
                             first_shown=datetime.datetime.fromtimestamp(fs, datetime.UTC).date() if fs else None,
                             last_shown=datetime.datetime.fromtimestamp(ls, datetime.UTC).date() if ls else None,
                             days_shown=c.get("13"), total_low=d.get("4"), total_high=d.get("5")))
w = csv.DictWriter(open(OUT, "w"), fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print(len(rows))
