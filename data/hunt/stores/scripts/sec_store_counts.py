"""Pull SEC XBRL companyfacts for Nike partners and extract store-count style facts
(us-gaap:NumberOfStores and any custom tag containing 'Store' with unit 'store'/pure counts).
Usage: python3 -I sec_store_counts.py <rawdir> <out_csv>"""
import json, sys, os, time, csv, urllib.request
UA = {"User-Agent": "Mozilla/5.0 (academic research script)"}
CIKS = {"DKS": 1089063, "FL": 850209, "ASO": 1817358, "HIBB": 1017480, "DBI": 1319947, "M": 794367,
        "GCO": 18498, "SCVL": 895447, "BGFV": 1156388, "KSS": 885639, "JWN": 72333, "NKE": 320187, "BOOT": 1610250}
raw, out = sys.argv[1], sys.argv[2]; os.makedirs(raw, exist_ok=True)
rows = []
for tk, cik in CIKS.items():
    p = os.path.join(raw, f"companyfacts_{tk}.json")
    if not os.path.exists(p):
        d = urllib.request.urlopen(urllib.request.Request(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json", headers=UA), timeout=120).read()
        open(p, "wb").write(d); time.sleep(0.5)
    d = json.load(open(p))
    for ns, tags in d.get("facts", {}).items():
        for tag, v in tags.items():
            if "store" not in tag.lower() and "location" not in tag.lower(): continue
            for unit, facts in v.get("units", {}).items():
                if unit.lower() in ("usd", "usd/shares", "shares"): continue
                for f in facts:
                    rows.append([tk, ns, tag, unit, f.get("start"), f.get("end"), f.get("val"), f.get("fy"), f.get("fp"), f.get("form"), f.get("filed"), f.get("accn"), f.get("frame")])
with open(out, "w", newline="") as f:
    w = csv.writer(f); w.writerow(["ticker", "ns", "tag", "unit", "start", "end", "val", "fy", "fp", "form", "filed", "accn", "frame"]); w.writerows(rows)
print(len(rows))
