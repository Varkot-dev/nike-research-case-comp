"""Pull all postings from a public Workday CXS job board (no login).
Usage: python3 pull_workday.py <tenant> <wdN> <site> <outprefix> [--details]
Example: python3 pull_workday.py nike wd1 nke raw/nike_nke --details
Writes <outprefix>_list.json (all list rows + facets) and optional _details.jsonl."""
import json, sys, time, urllib.request
tenant, wd, site, out = sys.argv[1:5]
details = '--details' in sys.argv
base = f"https://{tenant}.{wd}.myworkdayjobs.com/wday/cxs/{tenant}/{site}"
def post(offset, facets=None):
    body = json.dumps({"appliedFacets": facets or {}, "limit": 20, "offset": offset, "searchText": ""}).encode()
    req = urllib.request.Request(base + "/jobs", data=body, headers={"Content-Type": "application/json", "Accept": "application/json", "User-Agent": "Mozilla/5.0 (academic research)"})
    for i in range(4):
        try:
            return json.load(urllib.request.urlopen(req, timeout=60))
        except Exception as e:
            print("retry", offset, e, file=sys.stderr); time.sleep(3 * (i + 1))
    raise SystemExit("failed")
first = post(0)
total = first["total"]; rows = list(first["jobPostings"]); facets = first["facets"]
off = 20
while off < total:
    d = post(off); rows += d["jobPostings"]; off += 20; time.sleep(0.6)
    if not d["jobPostings"]: break
json.dump({"pulled_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "base": base, "total": total, "facets": facets, "jobPostings": rows}, open(out + "_list.json", "w"))
print(site, "total", total, "rows", len(rows))
if details:
    seen = set()
    with open(out + "_details.jsonl", "w") as f:
        for r in rows:
            p = r.get("externalPath")
            if not p or p in seen: continue
            seen.add(p)
            req = urllib.request.Request(base + p, headers={"Accept": "application/json", "User-Agent": "Mozilla/5.0 (academic research)"})
            try:
                d = json.load(urllib.request.urlopen(req, timeout=60))
                ji = d.get("jobPostingInfo", {})
                ji.pop("jobDescription", None)  # keep file small
                f.write(json.dumps({"externalPath": p, "info": ji, "hiringOrganization": d.get("hiringOrganization")}) + "\n")
            except Exception as e:
                print("detail fail", p, e, file=sys.stderr)
            time.sleep(0.4)
