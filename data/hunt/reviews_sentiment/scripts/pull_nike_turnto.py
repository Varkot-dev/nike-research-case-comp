"""nike.com reviews via the public TurnTo CDN that nike.com product pages call (site key 'turnToSiteKey' in page source).
Usage: python3 -I pull_nike_turnto.py <styles.csv> <rawdir>
Pages 1000 at a time until 'total' is reached. Keeps only review id, style, catalog title, dates, rating, incentive flags,
syndication source, recommend flag and fit/comfort dimension values. No user fields. Sleep 1.2 s."""
import sys, os, json, time, csv, gzip, urllib.request
KEY = "78GDJmj4zEDYwwHsite"
styles = list(csv.DictReader(open(sys.argv[1]))); raw = sys.argv[2]; os.makedirs(raw, exist_ok=True)
out = gzip.open(os.path.join(raw, "nike_turnto_reviews.csv.gz"), "wt", newline=""); w = csv.writer(out)
w.writerow(["style", "item_title", "review_id", "created_ms", "purchase_date", "rating", "incentivized", "incentivized_type", "syndication", "recommended", "fit", "comfort", "locale", "has_media"])
summ = open(os.path.join(raw, "nike_turnto_style_totals.csv"), "w", newline=""); sw = csv.writer(summ); sw.writerow(["style", "input_title", "turnto_title", "total", "fetched"])
for s in styles:
    st = s["style"]; off = 0; tot = None; got = 0; title = None
    while True:
        url = f"https://cdn-ws.turnto.com/v5/sitedata/{KEY}/{st}/d/review/en_US/{off}/1000/RECENT/false/false/"
        d = None
        for a in range(3):
            try:
                with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=90) as r: d = json.load(r); break
            except Exception as e: time.sleep(10 * (a + 1))
        time.sleep(1.2)
        if not d: break
        tot = d.get("total"); revs = d.get("reviews") or []
        for r in revs:
            dims = {x.get("dimensionLabel"): x.get("value") for x in (r.get("dimensions") or [])}
            title = title or (r.get("catItem") or {}).get("title")
            syn = r.get("syndication"); syn = (syn or {}).get("sourceSiteName") if isinstance(syn, dict) else syn
            w.writerow([st, (r.get("catItem") or {}).get("title"), r.get("id"), r.get("dateCreatedMillis"), r.get("purchaseDateFormatted"), r.get("rating"), r.get("incentivized"),
                        r.get("incentivizedType"), syn, r.get("recommended"), dims.get("How did this product fit?"), dims.get("How comfortable was this product?"), r.get("locale"), bool(r.get("media"))])
        got += len(revs)
        if len(revs) < 1000 or got >= (tot or 0): break
        off += 1000
    sw.writerow([st, s["title"], title, tot, got]); summ.flush(); out.flush()
    print(st, s["title"], title, tot, got, flush=True)
out.close(); summ.close()
