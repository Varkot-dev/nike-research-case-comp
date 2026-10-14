"""Fleet Feet UPC-level (colour x size x width) inventory from the public Typesense index (search-only key read from the
fleetfeet.com browse page at run time; never stored). For selected current models, pulls every UPC doc and records total inventory,
size, colour (sku) and stores-with-stock. Output raw/fleetfeet_upc_<date>.csv.gz
Usage: python3 -I pull_fleetfeet_sizeruns.py <outfile> <slug1,slug2,...>"""
import sys, re, json, gzip, csv, time, subprocess, urllib.request, urllib.parse
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
h = subprocess.run(["curl","-s","-L","-m","60","-A",UA,"https://www.fleetfeet.com/browse/mens/running-shoes"],capture_output=True,text=True).stdout
K = re.search(r'ffTypesense\s*=\s*\{[^}]*"apiKey":"([^"]+)"', h).group(1)
base = "https://8o6idgupvtb1nqksp.a1.typesense.net/collections/fleetfeet_product_variants_v5/documents/search?"
rows = []
for slug in sys.argv[2].split(","):
    page = 1
    while True:
        q = {"q": "*", "filter_by": f"product.slug:=`{slug}`", "per_page": "250", "page": str(page),
             "include_fields": "product.slug,product.brand,product.title,sku.sku,sku.inventory,upc.upc,upc.shoeSize,upc.totalInventory,upc.inventory,product.inventory,computed.price,computed.originalPrice,computed.discounted,product.inStock"}
        req = urllib.request.Request(base + urllib.parse.urlencode(q), headers={"X-TYPESENSE-API-KEY": K})
        d = json.load(urllib.request.urlopen(req, timeout=60))
        hits = d.get("hits", [])
        for x in hits:
            doc = x["document"]
            rows.append({"slug": slug, "brand": doc.get("product.brand"), "sku": doc.get("sku.sku"), "size": doc.get("upc.shoeSize"),
                         "upc_inventory": doc.get("upc.totalInventory", 0), "price": doc.get("computed.price"), "orig": doc.get("computed.originalPrice")})
        if len(hits) < 250: break
        page += 1; time.sleep(1)
    print(slug, len([r for r in rows if r["slug"] == slug]), flush=True); time.sleep(0.8)
with gzip.open(sys.argv[1], "wt", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
