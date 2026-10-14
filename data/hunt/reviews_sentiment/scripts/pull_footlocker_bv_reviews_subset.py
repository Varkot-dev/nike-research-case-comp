"""Second worker for the Foot Locker BV pull: reads fl_bv_model_products.csv and pages reviews only for products whose
search term is in TERMS (argv[3], comma list). Same fields/rate as pull_footlocker_bv_models.py.
Usage: python3 -I pull_footlocker_bv_reviews_subset.py <rawdir> <outname.csv.gz> <terms> [MINREV]"""
import sys, os, csv, gzip, json, time, urllib.request, urllib.parse
P = "caRWQpVIWHadvLym6aMyUFt4y13au7s5yi2ZCu0bMOHGY"; API = "https://api.bazaarvoice.com/data/"
raw, outn, terms = sys.argv[1], sys.argv[2], set(sys.argv[3].split(",")); MINREV = int(sys.argv[4]) if len(sys.argv) > 4 else 20
def get(ep, params):
    q = urllib.parse.urlencode([("apiversion", "5.4"), ("passkey", P)] + params)
    for a in range(4):
        try:
            with urllib.request.urlopen(API + ep + "?" + q, timeout=60) as r: d = json.load(r)
            time.sleep(1.5); return d
        except Exception: time.sleep(15 * (a + 1))
    return {}
prods = {}
for row in csv.DictReader(open(os.path.join(raw, "fl_bv_model_products.csv"))):
    if row["term"] in terms and int(float(row["total_reviews"] or 0)) >= MINREV: prods[row["product_id"]] = row
rf = gzip.open(os.path.join(raw, outn), "wt", newline=""); rw = csv.writer(rf)
rw.writerow(["product_id", "review_id", "submitted", "rating", "is_syndicated", "syndication_source", "incentivized", "recommended", "original_product_name"])
for pid, row in prods.items():
    off = 0
    while True:
        d = get("reviews.json", [("Filter", "ProductId:" + pid), ("Filter", "ContentLocale:en_US"), ("Sort", "SubmissionTime:desc"), ("Limit", 100), ("Offset", off)])
        res = d.get("Results") or []
        for r in res:
            ctx = r.get("ContextDataValues") or {}
            rw.writerow([pid, r.get("Id"), r.get("SubmissionTime"), r.get("Rating"), r.get("IsSyndicated"), (r.get("SyndicationSource") or {}).get("Name"),
                         (ctx.get("IncentivizedReview") or {}).get("Value"), r.get("IsRecommended"), r.get("OriginalProductName")])
        off += 100
        if len(res) < 100 or off >= 10000: break
    rf.flush(); print("reviews", pid, row["name"], off, flush=True)
rf.close()
