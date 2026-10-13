"""Foot Locker reviews via the public Bazaarvoice display API (passkey embedded in footlocker.com product pages).
Per brand: top NPROD products by review count, then each product's en_US reviews since START (newest first, capped at MAXPAGES x 100).
The API allows one ProductId per review query. Reviews syndicated from brand sites (e.g. nike.com) are kept and flagged.
Output: gzip CSV of reviews + CSV of products. 2.5 s between requests."""
import requests, time, json, csv, gzip, sys
P = "caRWQpVIWHadvLym6aMyUFt4y13au7s5yi2ZCu0bMOHGY"; API = "https://api.bazaarvoice.com/data/"
START = "2021-06-01"; MAXPAGES = 10; NPROD = 25
ids = json.load(open(sys.argv[1])); outdir = sys.argv[2]
EXTRA = {"ASICS": ["992vd8i5zfp4nyzofumuwk61c", "BBF6CB53", "F99F7C1C"], "adidas": ["66F5009A", "dkaciv3ngm7qtews5m96gi79t"]}
def get(ep, **p):
    for a in range(4):
        try:
            q = dict(apiversion="5.4", passkey=P, **p)
            r = requests.get(API + ep, params=q, timeout=60)
            if r.status_code == 200: time.sleep(2.0); return r.json()
        except Exception: pass
        time.sleep(15 * (a + 1))
    return {}
pw = csv.writer(open(outdir + "/footlocker_bv_products.csv", "w", newline=""))
pw.writerow(["brand", "product_id", "name", "category_id", "total_reviews", "avg_rating", "first_review", "last_review"])
rf = gzip.open(outdir + "/footlocker_bv_reviews.csv.gz", "wt", newline=""); rw = csv.writer(rf)
rw.writerow(["brand", "product_id", "review_id", "submitted", "rating", "title", "text", "is_syndicated", "incentivized", "recommended"])
for brand, lst in ids.items():
    bids = sorted(set([x[0] for x in lst] + EXTRA.get(brand, [])))
    prods = []
    for off in (0, 100):
        d = get("products.json", Filter="BrandId:" + ",".join(bids), Sort="TotalReviewCount:desc", Limit=100, Offset=off, Stats="Reviews")
        prods += d.get("Results", [])
    prods = [p for p in prods if (p.get("ReviewStatistics") or {}).get("TotalReviewCount", 0) > 0]
    for p in prods:
        s = p.get("ReviewStatistics") or {}
        pw.writerow([brand, p["Id"], p.get("Name"), p.get("CategoryId"), s.get("TotalReviewCount"), s.get("AverageOverallRating"),
                     s.get("FirstSubmissionTime"), s.get("LastSubmissionTime")])
    n = 0; oldest = None
    for p in prods[:NPROD]:
        for page in range(MAXPAGES):
            d = get("reviews.json", Filter=["ProductId:" + p["Id"], "ContentLocale:en_US"], Sort="SubmissionTime:desc", Limit=100, Offset=page * 100)
            res = d.get("Results", [])
            for r in res:
                ctx = r.get("ContextDataValues") or {}
                rw.writerow([brand, r.get("ProductId"), r.get("Id"), r.get("SubmissionTime"), r.get("Rating"), r.get("Title"),
                             (r.get("ReviewText") or "")[:2000], r.get("IsSyndicated"), (ctx.get("IncentivizedReview") or {}).get("Value"),
                             r.get("IsRecommended")])
            n += len(res)
            if res: oldest = res[-1].get("SubmissionTime")
            if len(res) < 100 or (res and res[-1].get("SubmissionTime", "")[:10] < START): break
    rf.flush()
    print(brand, "products", len(prods), "reviews", n, "oldest", oldest, flush=True)
rf.close()
