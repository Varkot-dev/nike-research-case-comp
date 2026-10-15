"""Find Foot Locker Bazaarvoice brand ids by searching each brand name (public display passkey from footlocker.com page source)."""
import requests, time, json, collections, sys
P = "caRWQpVIWHadvLym6aMyUFt4y13au7s5yi2ZCu0bMOHGY"
B = {"Nike": "nike", "Jordan": "jordan", "Converse": "converse", "adidas": "adidas", "HOKA": "hoka", "On": "on cloud",
     "New Balance": "new balance", "Brooks": "brooks", "ASICS": "asics", "PUMA": "puma", "Under Armour": "under armour", "Skechers": "skechers"}
out = {}
for b, q in B.items():
    r = requests.get("https://api.bazaarvoice.com/data/products.json", params=dict(apiversion="5.4", passkey=P, Search=q, Limit=100, Stats="Reviews"), timeout=60).json()
    c = collections.Counter((x["Brand"]["Id"], x["Brand"]["Name"]) for x in r.get("Results", []) if x.get("Brand"))
    print(b, c.most_common(4), flush=True)
    out[b] = [k for k, v in c.most_common(6) if k[1].lower().replace("®", "").strip() in (b.lower(), q, "hoka one one", "on running", "on")]
    time.sleep(3)
json.dump(out, open(sys.argv[1], "w"), indent=1)
