"""Shares outstanding history from SEC XBRL companyfacts (dei:EntityCommonStockSharesOutstanding, cover-page counts).
Multi-class issuers report one value per class; we sum all classes on the same date (total shares) and keep the list.
Writes shares_all.csv (ticker, date, shares_total, n_classes)."""
import json, subprocess, sys, csv, pathlib, time, collections
HERE = pathlib.Path(__file__).resolve().parent.parent; RAW = HERE / "raw"
UA = "NKE case research bot research@example.com"
tk = RAW / "company_tickers.json"
if not tk.exists():
    subprocess.run(["curl", "-sS", "-A", UA, "https://www.sec.gov/files/company_tickers.json", "-o", str(tk)], check=True)
m = {v["ticker"]: v["cik_str"] for v in json.load(open(tk)).values()}
m.setdefault("GAP", m.get("GAP")); 
rows = []
for t in sys.argv[1:]:
    cik = m.get(t)
    if cik is None: print("nocik", t); continue
    out = RAW / f"cf_{t}.json"
    if not out.exists():
        subprocess.run(["curl", "-sS", "-A", UA, f"https://data.sec.gov/api/xbrl/companyconcept/CIK{cik:010d}/dei/EntityCommonStockSharesOutstanding.json", "-o", str(out)], check=True); time.sleep(0.15)
    try: d = json.load(open(out))
    except Exception: print("fail", t); continue
    by = collections.defaultdict(dict)
    for u in d["units"].get("shares", []):
        by[u["end"]][u.get("accn", "") + str(u["val"])] = u["val"]
    for end in sorted(by):
        # same date, de-duplicate filings: take distinct values per accession; sum classes within latest accession
        per_acc = collections.defaultdict(list)
        for u in d["units"]["shares"]:
            if u["end"] == end: per_acc[u["accn"]].append(u["val"])
        acc = sorted(per_acc)[0]
        vals = per_acc[acc]
        rows.append([t, end, sum(vals), len(vals)])
    print(t, len(by))
with open(HERE / "shares_all.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["ticker", "date", "shares_total", "n_classes"]); w.writerows(rows)
