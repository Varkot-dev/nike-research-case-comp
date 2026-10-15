"""Parse nike.com review JSON (TurnTo public CDN, site key from nike.com product page source) -> one row per unique review.
Usage: python3 -I parse_nike_turnto.py <dl/nike_turnto> <data/nike_styles_queried.csv> <out.csv.gz> <style_summary.csv>"""
import sys, json, re, os, csv, gzip
import pandas as pd
dl, styles, out, summ = sys.argv[1:5]
st = pd.read_csv(styles).set_index("style")
rows = {}; sm = []
for l in open(os.path.join(dl, "fetch_log.jsonl")):
    d = json.loads(l)
    if d["status"] != 200 or not os.path.exists(d["file"]): continue
    style = re.search(r"/sitedata/[^/]+/([^/]+)/d/review", d["url"]).group(1)
    try: j = json.load(open(d["file"]))
    except Exception: continue
    revs = j.get("reviews") or []
    sm.append(dict(style=style, model=st.loc[style, "title"] if style in st.index else None, total_reviews=j.get("total"), fetched=len(revs),
                   avg_rating_fetched=(sum(float(r["rating"]) for r in revs) / len(revs)) if revs else None))
    for r in revs:
        rid = r.get("id")
        if rid in rows: continue
        rows[rid] = dict(review_id=rid, style=style, model=sm[-1]["model"], date=pd.to_datetime(int(r["dateCreatedMillis"]), unit="ms").date().isoformat(),
                         rating=r.get("rating"), title=r.get("title") or "", text=(r.get("text") or "")[:2000],
                         incentivized=r.get("incentivized"), locale=r.get("locale"))
pd.DataFrame(list(rows.values())).to_csv(out, index=False, compression="gzip")
pd.DataFrame(sm).to_csv(summ, index=False)
print(len(rows), "unique reviews from", len(sm), "styles")
