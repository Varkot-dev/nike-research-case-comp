import json, os, re, sys, time, urllib.request
SEC = sys.argv[1]
# Download from Nike's investor-site mirror of EDGAR, not www.sec.gov: no contact header (and never an email) is sent.
UA = {"User-Agent": "Mozilla/5.0"}
MIRROR = "https://investors.nike.com/sec-filings/all-sec-filings/content/{acc}/"
CANON = "https://www.sec.gov/Archives/edgar/data/320187/{acc}/"  # cited URL only; never fetched
def linked_htm(html):
    """Exhibit file names linked from a filing's cover page on the mirror."""
    return sorted({h.rsplit("/", 1)[-1] for h in re.findall(r'href="([^"]+\.html?)"', html.decode("utf-8", "ignore"), re.I)})
OUT = os.path.join(SEC, "filings"); os.makedirs(OUT, exist_ok=True)
def get(url):
    for i in range(5):
        try:
            req = urllib.request.Request(url, headers=UA)
            return urllib.request.urlopen(req, timeout=60).read()
        except Exception as e:
            print("retry", url, e); time.sleep(2 ** i)
    raise SystemExit("failed " + url)
d = json.load(open(os.path.join(SEC, "sub.json")))["filings"]["recent"]
rows = [dict(zip(d.keys(), v)) for v in zip(*d.values())]
want = []
for r in rows:
    f, fd, rd = r["form"], r["filingDate"], r["reportDate"]
    if f == "10-K" and "2019-05-31" <= rd <= "2026-05-31": want.append(r)
    elif f == "10-Q" and rd >= "2023-08-31": want.append(r)
    elif f == "8-K" and "2.02" in r["items"] and fd >= "2019-06-01": want.append(r)
    elif f == "DEF 14A" and fd.startswith("2026"): want.append(r)
manifest = []
for r in want:
    base = MIRROR.format(acc=r["accessionNumber"])
    canon = CANON.format(acc=r["accessionNumber"].replace("-", ""))
    files = [r["primaryDocument"]]
    if r["form"] == "8-K":
        names = linked_htm(get(base + r["primaryDocument"]))
        files += [n for n in names if ("99" in n.lower() or "er" in n.lower()) and n != r["primaryDocument"]]
    for fn in files:
        tag = f'{r["form"].replace(" ","")}_{r["reportDate"]}_{r["filingDate"]}_{fn}'
        p = os.path.join(OUT, tag)
        if not os.path.exists(p):
            open(p, "wb").write(get(base + fn)); time.sleep(0.15)
        manifest.append({"form": r["form"], "filed": r["filingDate"], "period": r["reportDate"], "accession": r["accessionNumber"], "file": fn, "local": tag, "url": canon + fn, "items": r["items"]})
        print(tag, os.path.getsize(p))
json.dump(manifest, open(os.path.join(SEC, "manifest.json"), "w"), indent=1)
