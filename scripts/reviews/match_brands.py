"""Apply exact store-name brand rules to metadata candidates -> matched_products.csv.
Rules: normalise store (strip 'Brand: ', 'Visit the ... Store', '(Designer)'), match an exact allow-list per brand,
require the brand token in the title (drops miscategorised items, e.g. a phone screen protector under 'AIR JORDAN'),
drop third-party accessory phrasing ('for Nike', 'compatible with', 'replacement')."""
import sys, json, gzip, re, csv
STORES = {
 "Nike": ["nike", "nike golf", "nike sb", "nike acg"],
 "Jordan": ["jordan", "air jordan", "nike jordan"],
 "Converse": ["converse"],
 "adidas": ["adidas", "adidas originals", "adidas outdoor", "adidas by stella mccartney", "adidas golf", "adidas performance"],
 "HOKA": ["hoka one one", "hoka"],
 "On": ["on", "on running", "on ag"],
 "New Balance": ["new balance"],
 "Brooks": ["brooks", "brooks heritage"],
 "ASICS": ["asics", "asics tiger"],
 "Skechers": ["skechers", "concept 3 by skechers", "skechers sport women's", "skechers usa men's", "skechers cali women's",
              "skechers modern comfort women's", "skechers golf", "skechers performance", "skechers kids", "skechers work"],
 "Under Armour": ["under armour"],
 "PUMA": ["puma", "puma golf"],
}
TOKEN = {"Nike": r"nike|air max|air force|jordan", "Jordan": r"jordan", "Converse": r"converse|chuck taylor", "adidas": r"adidas",
         "HOKA": r"hoka", "On": r"\bon\b|cloud", "New Balance": r"new balance|\bnb\b", "Brooks": r"brooks", "ASICS": r"asics|tiger|onitsuka",
         "Skechers": r"skechers", "Under Armour": r"under armour|\bua\b", "PUMA": r"puma"}
BAD = re.compile(r"\bfor nike\b|\bfor adidas\b|compatible with|\breplacement\b|\bfits nike\b|\bfor (air )?jordan\b|\bfor converse\b|\bshoelaces? for\b", re.I)
lookup = {s: b for b, ss in STORES.items() for s in ss}
def norm(s):
    s = (s or "").strip()
    s = re.sub(r"^Brand:\s*", "", s); s = re.sub(r"^Visit the (.*) Store$", r"\1", s); s = re.sub(r"\s*\(Designer\)$", "", s)
    return s.strip().lower()
rows = []; drop = {"token": 0, "bad": 0}
for l in gzip.open(sys.argv[1], "rt"):
    try: d = json.loads(l)
    except Exception: continue
    b = lookup.get(norm(d["store"]))
    if not b: continue
    t = d.get("title") or ""
    if not re.search(TOKEN[b], t, re.I): drop["token"] += 1; continue
    if BAD.search(t): drop["bad"] += 1; continue
    cats = d.get("categories") or []
    rows.append(dict(parent_asin=d["parent_asin"], brand=b, firm="Nike Inc" if b in ("Nike", "Jordan", "Converse") else b,
                     store=d["store"], title=t[:200], category=" > ".join(cats), footwear=int(any(("Shoes" in c or "Sneakers" in c) and c != "Clothing, Shoes & Jewelry" for c in cats[1:])),
                     main_category=d.get("main_category"), date_first=d.get("date_first"), price=d.get("price")))
with (gzip.open(sys.argv[2], "wt", newline="") if sys.argv[2].endswith(".gz") else open(sys.argv[2], "w", newline="")) as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
import collections
print(len(rows), "matched; dropped", drop); print(collections.Counter(r["brand"] for r in rows))
