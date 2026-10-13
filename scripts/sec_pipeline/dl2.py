import json, os, re, sys, time, urllib.request
SEC = sys.argv[1]
# Download from Nike's investor-site mirror of EDGAR, not www.sec.gov: no contact header (and never an email) is sent.
UA = {"User-Agent": "Mozilla/5.0"}
MIRROR = "https://investors.nike.com/sec-filings/all-sec-filings/content/{acc}/"
CANON = "https://www.sec.gov/Archives/edgar/data/320187/{acc}/"  # cited URL only; never fetched
def linked_htm(html):
    """Exhibit file names linked from a filing's cover page on the mirror."""
    return sorted({h.rsplit("/", 1)[-1] for h in re.findall(r'href="([^"]+\.html?)"', html.decode("utf-8", "ignore"), re.I)})
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
    base = MIRROR.format(acc=r["accessionNumber"])
    canon = CANON.format(acc=r["accessionNumber"].replace("-", ""))
    names = [r["primaryDocument"]] + [n for n in linked_htm(get(base + r["primaryDocument"])) if n != r["primaryDocument"]]
    for fn in names:
        tag = f'8-K_{r["reportDate"]}_{r["filingDate"]}_{fn}'
        p = os.path.join(OUT, tag)
        if not os.path.exists(p): open(p,"wb").write(get(base+fn)); time.sleep(0.15)
        man.append({"form":"8-K","filed":r["filingDate"],"period":r["reportDate"],"accession":r["accessionNumber"],"file":fn,"local":tag,"url":canon+fn,"items":r["items"]})
        print(tag, os.path.getsize(p), r["items"])
man = [m for m in man if os.path.exists(os.path.join(OUT, m["local"]))]
json.dump(man, open(os.path.join(SEC,"manifest.json"),"w"), indent=1)
print(len(man))
