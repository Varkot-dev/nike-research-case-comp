"""Tag each posting on a Workday board with its jobFamilyGroup by re-querying with each facet applied.
Usage: python3 tag_workday_categories.py <tenant> <wdN> <site> <list_json> <out_json>"""
import json, sys, time, urllib.request
tenant, wd, site, lj, out = sys.argv[1:6]
base = f"https://{tenant}.{wd}.myworkdayjobs.com/wday/cxs/{tenant}/{site}/jobs"
L = json.load(open(lj))
fam = [f for f in L["facets"] if f["facetParameter"] in ("jobFamilyGroup", "jobFamily")]
tags = {}
for f in fam:
    for v in f["values"]:
        off = 0
        while True:
            body = json.dumps({"appliedFacets": {f["facetParameter"]: [v["id"]]}, "limit": 20, "offset": off, "searchText": ""}).encode()
            d = json.load(urllib.request.urlopen(urllib.request.Request(base, data=body, headers={"Content-Type": "application/json", "Accept": "application/json", "User-Agent": "Mozilla/5.0 (academic research)"}), timeout=60))
            for r in d["jobPostings"]: tags.setdefault(r["externalPath"], []).append(v["descriptor"])
            off += 20; time.sleep(0.5)
            if off >= d["total"] or not d["jobPostings"]: break
        print(v["descriptor"], v["count"], flush=True)
json.dump(tags, open(out, "w"))
