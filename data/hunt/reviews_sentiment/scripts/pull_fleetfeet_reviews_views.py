"""Fleet Feet public Typesense search index (search-only key embedded in fleetfeet.com browse pages as window.ffTypesense).
Pulls one row per product (grouped by product.slug) for shoes of 8 brands, with review count, average rating, fit rating,
trendScore, views7/30/60, inventory, prices, previousVersion and post/release dates.
Usage: python3 -I pull_fleetfeet_reviews_views.py <keyfile> <out.json>"""
import json, sys, urllib.request, urllib.parse, time
K = open(sys.argv[1]).read().strip(); out = sys.argv[2]
base = "https://8o6idgupvtb1nqksp.a1.typesense.net/collections/fleetfeet_product_variants_v5/documents/search?"
brands = ["Nike", "HOKA", "On", "ASICS", "Brooks", "Saucony", "New Balance", "adidas", "Altra", "Mizuno"]
res = []
for b in brands:
    page = 1
    while True:
        q = {"q": "*", "filter_by": f"product.productType:=Shoes && product.brand:=`{b}`", "group_by": "product.slug", "group_limit": "1", "per_page": "250", "page": str(page)}
        req = urllib.request.Request(base + urllib.parse.urlencode(q), headers={"X-TYPESENSE-API-KEY": K})
        d = json.load(urllib.request.urlopen(req, timeout=60))
        gh = d.get("grouped_hits", [])
        for g in gh:
            doc = g["hits"][0]["document"]; doc["_found_in_group"] = g.get("found"); res.append(doc)
        print(b, page, len(gh), d.get("found"), file=sys.stderr)
        if len(gh) < 250: break
        page += 1; time.sleep(1)
    time.sleep(1)
json.dump(res, open(out, "w"))
print(len(res))
