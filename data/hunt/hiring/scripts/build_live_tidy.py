"""Build tidy CSV of live Nike Workday postings (sites nke = global, nke2 = US retail stores) and Deckers.
Usage: python3 build_live_tidy.py  (run from data/hunt/hiring)"""
import json, re, csv
rows = []
def load(prefix, site, tagfile, company):
    L = json.load(open(f"raw/{prefix}_list.json"))
    det = {}
    try:
        for l in open(f"raw/{prefix}_details.jsonl"):
            d = json.loads(l); det[d["externalPath"]] = d
    except FileNotFoundError: pass
    tags = json.load(open(tagfile)) if tagfile else {}
    for r in L["jobPostings"]:
        p = r["externalPath"]; d = det.get(p, {}); info = d.get("info", {})
        req = (r.get("bulletFields") or [""])[0]
        m = re.search(r"(\d+)", req or "")
        rows.append({"company": company, "site": site, "pulled_utc": L["pulled_utc"][:10], "req_id": req,
            "req_num": int(m.group(1)) if m and req.startswith("R-") else "",
            "title": r["title"], "locations_text": r.get("locationsText"), "country": (info.get("country") or {}).get("descriptor", ""),
            "req_location": (info.get("jobRequisitionLocation") or {}).get("descriptor", ""),
            "time_type": r.get("timeType"), "posted_on": r.get("postedOn"), "start_date": info.get("startDate", ""), "end_date": info.get("endDate", ""),
            "hiring_org": (d.get("hiringOrganization") or {}).get("name", ""),
            "category": ";".join(tags.get(p, ["Retail Stores"] if site == "nke2" else [])), "path": p})
load("nike_nke", "nke", "raw/nike_nke_category_tags.json", "Nike")
load("nike_nke2", "nke2", None, "Nike")
load("deckers_Deckers", "Deckers", "raw/deckers_category_tags.json", "Deckers")
w = csv.DictWriter(open("live_postings_workday_2026-10-14.csv", "w", newline=""), fieldnames=list(rows[0].keys()))
w.writeheader(); w.writerows(rows); print(len(rows))
