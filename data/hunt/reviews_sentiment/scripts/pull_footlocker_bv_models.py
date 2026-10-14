"""Foot Locker Bazaarvoice display API (public passkey embedded in footlocker.com pages; same key the repo's
scripts/reviews/bv_footlocker_reviews.py uses). Step 1: product search per running-model keyword, keep products whose
name contains the keyword (stats: total reviews, first/last review). Step 2: for every matched product with >= MINREV
reviews, page all en_US reviews (100 per call) and keep date, rating, syndication source name, incentivized flag.
Usage: python3 -I pull_footlocker_bv_models.py <rawdir> [MINREV]
Sleep 1.5 s per call."""
import sys, os, json, time, csv, gzip, urllib.request, urllib.parse
P = "caRWQpVIWHadvLym6aMyUFt4y13au7s5yi2ZCu0bMOHGY"; API = "https://api.bazaarvoice.com/data/"
raw = sys.argv[1]; MINREV = int(sys.argv[2]) if len(sys.argv) > 2 else 20; os.makedirs(raw, exist_ok=True)
TERMS = ["Pegasus", "Vomero", "Structure", "Invincible", "InfinityRN", "Winflo", "Clifton", "Bondi", "Arahi", "Novablast",
         "Nimbus", "Kayano", "Cumulus", "Ghost", "Adrenaline", "Glycerin", "Cloudmonster", "Cloudsurfer", "Cloudrunner", "Ride", "880", "Triumph"]
def get(ep, params):
    q = urllib.parse.urlencode([("apiversion", "5.4"), ("passkey", P)] + params)
    for a in range(4):
        try:
            with urllib.request.urlopen(API + ep + "?" + q, timeout=60) as r: d = json.load(r)
            time.sleep(1.5); return d
        except Exception: time.sleep(15 * (a + 1))
    return {}
pf = open(os.path.join(raw, "fl_bv_model_products.csv"), "w", newline=""); pw = csv.writer(pf)
pw.writerow(["term", "product_id", "name", "brand", "total_reviews", "avg_rating", "first_review", "last_review"])
prods = {}
for t in TERMS:
    for off in (0, 100, 200):
        d = get("products.json", [("Search", t), ("Limit", 100), ("Offset", off), ("Stats", "Reviews"), ("Sort", "TotalReviewCount:desc")])
        res = d.get("Results") or []
        for p in res:
            if t.lower() not in (p.get("Name") or "").lower(): continue
            s = p.get("ReviewStatistics") or {}
            row = [t, p["Id"], p.get("Name"), (p.get("Brand") or {}).get("Name"), s.get("TotalReviewCount"), s.get("AverageOverallRating"), s.get("FirstSubmissionTime"), s.get("LastSubmissionTime")]
            pw.writerow(row); prods[p["Id"]] = row
        if len(res) < 100 or (res and ((res[-1].get("ReviewStatistics") or {}).get("TotalReviewCount") or 0) < MINREV): break
    pf.flush(); print("term", t, len(prods), flush=True)
pf.close()
rf = gzip.open(os.path.join(raw, "fl_bv_model_reviews.csv.gz"), "wt", newline=""); rw = csv.writer(rf)
rw.writerow(["product_id", "review_id", "submitted", "rating", "is_syndicated", "syndication_source", "incentivized", "recommended", "original_product_name"])
for pid, row in prods.items():
    if (row[4] or 0) < MINREV: continue
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
    rf.flush(); print("reviews", pid, row[2], off, flush=True)
rf.close()
