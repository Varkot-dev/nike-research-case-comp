"""Foot Locker: brand facet counts (sale vs total shoes) and per-brand discount depth on sale shoes. Also parses Wayback snapshots of sale pages."""
import sys, os, re, json, csv, statistics as st, urllib.parse, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from footlocker_parse_lib import blocks
from fetch import fname
raw, data = sys.argv[1], sys.argv[2]
FOCUS=["Nike","Jordan","adidas","New Balance","ASICS","HOKA","On","PUMA","Saucony","Brooks","Converse","Skechers"]
def load(u): 
    p=os.path.join(raw,fname(u)); return blocks(open(p,encoding="utf-8",errors="ignore").read())
pages={"sale_shoes":"https://www.footlocker.com/category/sale/shoes.html","all_shoes":"https://www.footlocker.com/category/shoes.html",
"sale_mens_shoes":"https://www.footlocker.com/category/sale/mens/shoes.html","all_mens_shoes":"https://www.footlocker.com/category/mens/shoes.html",
"sale_womens_shoes":"https://www.footlocker.com/category/sale/womens/shoes.html","all_womens_shoes":"https://www.footlocker.com/category/womens/shoes.html",
"sale_all":"https://www.footlocker.com/category/sale.html"}
B={k:load(u) for k,u in pages.items()}
rows=[]
for seg in ["shoes","mens_shoes","womens_shoes"]:
    s=B["sale_"+seg]; a=B["all_"+seg]
    st_tot=s["pagination"]["totalResults"]; a_tot=a["pagination"]["totalResults"]
    brands=sorted(set(s["brand_facet"])|set(a["brand_facet"]),key=lambda b:-a["brand_facet"].get(b,0))
    for b in brands:
        sc=s["brand_facet"].get(b,0); ac=a["brand_facet"].get(b,0)
        if ac<10 and b not in FOCUS: continue
        rows.append({"snapshot_date":"2026-10-13","segment":seg,"brand":b,"sale_styles":sc,"all_styles":ac,"share_of_brand_on_sale_pct":round(100*sc/ac,1) if ac else None,
            "brand_share_of_sale_pct":round(100*sc/st_tot,1),"brand_share_of_assortment_pct":round(100*ac/a_tot,1),"segment_sale_total":st_tot,"segment_all_total":a_tot})
    rows.append({"snapshot_date":"2026-10-13","segment":seg,"brand":"ALL","sale_styles":st_tot,"all_styles":a_tot,"share_of_brand_on_sale_pct":round(100*st_tot/a_tot,1),"brand_share_of_sale_pct":100,"brand_share_of_assortment_pct":100,"segment_sale_total":st_tot,"segment_all_total":a_tot})
with open(os.path.join(data,"footlocker_brand_sale_mix.csv"),"w",newline="") as fh:
    wr=csv.DictWriter(fh,fieldnames=list(rows[0].keys())); wr.writeheader(); wr.writerows(rows)
# per brand discount depth
items=[]
log=[json.loads(l) for l in open(os.path.join(data,"fetch_log.jsonl"))]
for d in log:
    if d["status"]!=200 or "footlocker.com/category/sale/shoes.html?query=" not in d["url"]: continue
    q=urllib.parse.unquote(d["url"].split("query=")[1].split("&")[0])
    m=re.search(r":brand:([^:]+)",q); brand=m.group(1).replace("®","")
    b=blocks(open(d["file"],encoding="utf-8",errors="ignore").read())
    for p in b["products"]:
        op=(p.get("originalPrice") or {}).get("value"); pr=(p.get("price") or {}).get("value")
        items.append({"snapshot_date":"2026-10-13","brand_filter":brand,"query":q,"sku":p.get("sku"),"name":p.get("name"),"original_price":op,"price":pr,
            "discount_pct":round(100*(1-pr/op),1) if op and pr else None,"result_total":b["pagination"]["totalResults"]})
seen=set(); I=[]
for r in items:
    if r["sku"] in seen: continue
    seen.add(r["sku"]); I.append(r)
with open(os.path.join(data,"footlocker_sale_items.csv"),"w",newline="") as fh:
    wr=csv.DictWriter(fh,fieldnames=list(I[0].keys())); wr.writeheader(); wr.writerows(I)
S=[]
for b in sorted({r["brand_filter"] for r in I}):
    X=[r for r in I if r["brand_filter"]==b and r["discount_pct"] is not None]
    adult=[r for r in X if re.search(r"- (Men's|Women's)$",r["name"] or "")]
    exp=B["sale_shoes"]["brand_facet"].get(b)
    S.append({"snapshot_date":"2026-10-13","brand":b,"sale_styles_facet":exp,"items_parsed":len(X),"avg_discount_pct":round(st.mean(r["discount_pct"] for r in X),1),
      "median_discount_pct":st.median(r["discount_pct"] for r in X),"avg_original_price":round(st.mean(r["original_price"] for r in X),1),
      "share_disc_ge_30_pct":round(100*sum(r["discount_pct"]>=30 for r in X)/len(X),1),"adult_items":len(adult),
      "adult_avg_discount_pct":round(st.mean(r["discount_pct"] for r in adult),1) if adult else None})
with open(os.path.join(data,"footlocker_discount_by_brand.csv"),"w",newline="") as fh:
    wr=csv.DictWriter(fh,fieldnames=list(S[0].keys())); wr.writeheader(); wr.writerows(S)
for r in rows:
    if r["brand"] in FOCUS+["ALL"]: print(r["segment"],r["brand"],r["sale_styles"],r["all_styles"],r["share_of_brand_on_sale_pct"],r["brand_share_of_sale_pct"],r["brand_share_of_assortment_pct"])
for s in S: print(s)
