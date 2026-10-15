"""Download 10-K / 10-Q primary documents (and 8-K EX-99.1 earnings releases) for Nike partners since 2019,
strip to plain text, save gzip. Usage: python3 -I sec_filing_text.py <outdir> TICKER:CIK[:8k] ..."""
import json, sys, os, time, re, gzip, html, urllib.request
UA = {"User-Agent": "Mozilla/5.0 (academic research script)"}
def get(u):
    for i in range(3):
        try: return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=120).read()
        except Exception as e: err = e; time.sleep(3)
    raise err
def text(b):
    s = b.decode("utf8", "ignore")
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?i)</(tr|p|div|br|li|h\d)>", "\n", s)
    s = re.sub(r"(?i)</t[dh]>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s); s = html.unescape(s)
    s = re.sub(r"[ \t\xa0]+", " ", s); s = re.sub(r"\n\s*\n+", "\n", s)
    return s
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
for arg in sys.argv[2:]:
    parts = arg.split(":"); tk, cik = parts[0], int(parts[1]); want8k = len(parts) > 2
    sub = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json"))
    blocks = [sub["filings"]["recent"]] + [json.loads(get("https://data.sec.gov/submissions/" + f["name"])) for f in sub["filings"].get("files", [])]
    for r in blocks:
        for form, date, acc, doc in zip(r["form"], r["filingDate"], r["accessionNumber"], r["primaryDocument"]):
            if date < "2019-01-01": continue
            if form not in ("10-K", "10-Q") and not (want8k and form == "8-K"): continue
            dest = os.path.join(out, f"{tk}_{form}_{date}_{acc}.txt.gz")
            if os.path.exists(dest): continue
            base = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-', '')}"
            try:
                if form == "8-K":
                    idx = json.loads(get(base + "/index.json"))
                    ex = [i["name"] for i in idx["directory"]["item"] if re.search(r"(ex|exhibit)[-_]?99", i["name"], re.I) and i["name"].endswith((".htm", ".html"))]
                    if not ex: continue
                    t = text(get(base + "/" + ex[0]))
                    if not re.search(r"store count|stores? (opened|closed)|number of stores|ending stores", t, re.I): continue
                else:
                    t = text(get(base + "/" + doc))
                with gzip.open(dest, "wt") as f: f.write(t)
                print(dest, flush=True)
            except Exception as e: print("FAIL", tk, form, date, e, flush=True)
            time.sleep(0.3)
