"""Flatten Nike's public store-locator static JSON (https://nslp-directory.nike.com/store-locations-static.json)
into one row per store. Usage: python3 -I flatten_nike_locator.py <json> <out_csv>"""
import json, sys, csv
d = json.load(open(sys.argv[1])); S = d["stores"]
cols = ["id", "storeNumber", "name", "facilityType", "businessConcept", "storeConcept", "company", "region", "iso2Country",
        "state", "city", "postalCode", "latitude", "longitude", "openingDate", "n_closures", "closures", "n_offerings", "n_services", "nikeAppStoreMode"]
with open(sys.argv[2], "w", newline="") as f:
    w = csv.writer(f); w.writerow(cols + ["file_created"])
    for s in S.values():
        a = s.get("address", {}); od = s.get("operationalDetails", {}) or {}; c = s.get("coordinates", {}) or {}
        w.writerow([s.get("id"), s.get("storeNumber"), s.get("name"), s.get("facilityType"), s.get("businessConcept"), s.get("storeConcept"),
                    s.get("company"), s.get("region"), a.get("iso2Country"), a.get("state"), a.get("city"), a.get("postalCode"),
                    c.get("latitude"), c.get("longitude"), od.get("openingDate"), len(od.get("closures") or []), json.dumps(od.get("closures") or [])[:300],
                    len(s.get("offerings") or []), len(s.get("storeServices") or []), s.get("nikeAppStoreMode"), d.get("fileCreatedTime")])
print(len(S))
