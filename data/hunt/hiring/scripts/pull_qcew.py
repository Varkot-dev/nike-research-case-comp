"""BLS QCEW open-data area files: Washington County, OR (FIPS 41067), where Nike World HQ (Beaverton) sits.
Keeps private-sector rows for NAICS 551114 (corporate/managing offices; Nike WHQ dominates) plus comparison rows.
Usage: python3 pull_qcew.py <rawdir> <outcsv>"""
import sys, time, urllib.request, csv, io, os
raw, out = sys.argv[1], sys.argv[2]
keep = {"10", "55", "551114", "5415", "334", "424340", "4482", "315"}
rows = []
for y in range(2018, 2027):
    for q in range(1, 5):
        fn = os.path.join(raw, f"qcew_41067_{y}q{q}.csv")
        if not os.path.exists(fn):
            try:
                t = urllib.request.urlopen(urllib.request.Request(f"https://data.bls.gov/cew/data/api/{y}/{q}/area/41067.csv", headers={"User-Agent": "Mozilla/5.0 (academic research)"}), timeout=90).read().decode()
            except Exception as e:
                print(y, q, "n/a", e); continue
            # keep only needed rows to stay small
            r = list(csv.DictReader(io.StringIO(t)))
            sub = [x for x in r if x["industry_code"] in keep and x["own_code"] in ("0", "5")]
            with open(fn, "w", newline="") as fh:
                w = csv.DictWriter(fh, fieldnames=list(r[0].keys())); w.writeheader(); w.writerows(sub)
            time.sleep(1)
        for x in csv.DictReader(open(fn)):
            rows.append({k: x[k] for k in ["year", "qtr", "own_code", "industry_code", "disclosure_code", "qtrly_estabs", "month1_emplvl", "month2_emplvl", "month3_emplvl", "total_qtrly_wages", "avg_wkly_wage", "oty_month3_emplvl_pct_chg"]})
        print(y, q, flush=True)
w = csv.DictWriter(open(out, "w", newline=""), fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
