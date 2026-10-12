import json, os, sys, time, urllib.request
SEC = sys.argv[1]
UA = {"User-Agent": os.environ.get("SEC_USER_AGENT", "Your Name your.email@example.com")}  # SEC requires a contact in the User-Agent
OUT = os.path.join(SEC, "filings")
def get(url):
    for i in range(5):
        try: return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
        except Exception as e: print("retry", e); time.sleep(2**i)
    raise SystemExit("fail "+url)
d = json.load(open(os.path.join(SEC, "sub.json")))["filings"]["recent"]
rows = [dict(zip(d.keys(), v)) for v in zip(*d.values())]
man = json.load(open(os.path.join(SEC, "manifest.json")))
have = {m["accession"] for m in man}
for r in rows:
    if r["form"] != "8-K" or r["filingDate"] < "2023-12-01" or r["accessionNumber"] in have: continue
    if not any(i in r["items"] for i in ("5.02","2.05","8.01","7.01")): continue
    acc = r["accessionNumber"].replace("-", "")
    base = f"https://www.sec.gov/Archives/edgar/data/320187/{acc}/"
    names = [i["name"] for i in json.loads(get(base+"index.json"))["directory"]["item"]]
    for fn in [n for n in names if n.lower().endswith((".htm",".html")) and "index" not in n.lower()]:
        tag = f'8-K_{r["reportDate"]}_{r["filingDate"]}_{fn}'
        p = os.path.join(OUT, tag)
        if not os.path.exists(p): open(p,"wb").write(get(base+fn)); time.sleep(0.15)
        man.append({"form":"8-K","filed":r["filingDate"],"period":r["reportDate"],"accession":r["accessionNumber"],"file":fn,"local":tag,"url":base+fn,"items":r["items"]})
        print(tag, os.path.getsize(p), r["items"])
man = [m for m in man if os.path.exists(os.path.join(OUT, m["local"]))]
json.dump(man, open(os.path.join(SEC,"manifest.json"),"w"), indent=1)
print(len(man))
