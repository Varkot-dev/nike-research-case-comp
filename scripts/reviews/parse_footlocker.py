"""Parse Foot Locker category pages (live or Wayback) -> product rows (name, brand, reviews, rating) and brand facet counts.
Usage: python3 -I parse_footlocker.py <fetch_log.jsonl> <items_out.csv> <facets_out.csv>"""
import sys, json, re, csv, os, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brandmatch import brand_of
lg, out_items, out_fac = sys.argv[1:4]
dec = json.JSONDecoder(); items = []; facets = []; seen_fac = set()
def products(s):
    i = s.find('"products":[{')
    if i < 0: return []
    try: return dec.raw_decode(s[i + 11:])[0]
    except Exception: return []
for l in open(lg):
    d = json.loads(l)
    if d["status"] != 200 or not os.path.exists(d["file"]): continue
    url = d["url"]; s = open(d["file"], encoding="utf-8", errors="ignore").read()
    mm = re.search(r"/web/(\d{14})id_/", url)
    date, src = ((mm.group(1)[:4] + "-" + mm.group(1)[4:6] + "-" + mm.group(1)[6:8]), "wayback") if mm else (d["t"][:10], "live")
    gender = "womens" if "/womens/" in url else "mens"
    q = urllib.parse.unquote(url); bm = re.search(r":brand:([^&:]+)", q); qbrand = bm.group(1) if bm else ""
    tr = re.search(r'"totalResults":(\d+)', s)
    for p in products(s):
        rr = p.get("reviewRatings") or {}
        va = [v.get("review", {}) for v in p.get("variantOptions", []) if v.get("review")]
        avg = va[0].get("averageRating") if va else None
        items.append(dict(snapshot_date=date, source=src, gender=gender, query_brand=qbrand, brand=brand_of(p.get("name")),
                          sku=p.get("baseProduct") or p.get("sku"), name=p.get("name"), price=(p.get("price") or {}).get("value"),
                          list_price=(p.get("originalPrice") or {}).get("value"), reviews=rr.get("reviews"), rating=rr.get("rating"),
                          avg_rating_variant=avg, page_total_results=tr.group(1) if tr else None, url=url))
    i = s.find('"name":"Brand"')
    if i >= 0 and (date, gender) not in seen_fac:
        seg = s[i:i + 80000]; j = seg.find('"name":"Under $'); seg = seg[:j] if j > 0 else seg
        for b, c in re.findall(r'"name":"([^"]+)","count":(\d+)', seg):
            facets.append(dict(snapshot_date=date, source=src, gender=gender, brand=b, listing_count=int(c),
                               category_total=tr.group(1) if (tr and not qbrand) else None))
        seen_fac.add((date, gender))
for path, rows in ((out_items, items), (out_fac, facets)):
    if rows:
        with open(path, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print(len(items), "items", len(facets), "facet rows")
