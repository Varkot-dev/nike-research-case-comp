import sys, os, json, re, csv, statistics as st
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from nike_parse_lib import parse_html, parse_api
from fetch import fname
raw, data = sys.argv[1], sys.argv[2]
WALLS=["sale-3yaep","shoes-y7ok","sale-shoes-3yaepzy7ok","mens-shoes-nik1zy7ok","womens-shoes-5e1x6zy7ok","mens-sale-shoes-3yaepznik1zy7ok","womens-sale-shoes-3yaepz5e1x6zy7ok","mens-running-shoes-37v7jznik1zy7ok","womens-running-shoes-37v7jz5e1x6zy7ok"]
log=[json.loads(l) for l in open(os.path.join(data,"fetch_log.jsonl"))]
apif={}
for d in log:
    if "api.nike.com" in d["url"] and d["status"]==200:
        m=re.search(r'path=/w/([^&]+)',d["url"]); a=int(re.search(r'anchor=(\d+)',d["url"]).group(1))
        apif.setdefault(m.group(1),{})[a]=d["file"]
rows=[]; summ=[]
for w in WALLS:
    h=parse_html(open(os.path.join(raw,fname("https://www.nike.com/w/"+w)),encoding="utf-8",errors="ignore").read())
    prods=list(h["products"]); pages=1
    for a,f in sorted(apif.get(w,{}).items()):
        p,_=parse_api(json.load(open(f))); prods+=p; pages+=1
    seen=set(); P=[]
    for p in prods:
        k=(p["group"],p["code"])
        if k in seen: continue
        seen.add(k); P.append(p)
    for p in P:
        disc=None
        if p["current"] is not None and p["full"]: disc=round(100*(1-p["current"]/p["full"]),2)
        rows.append({"snapshot_date":"2026-10-13","wall":w,**p,"discount_pct":disc})
    firsts=[p for p in P if p["is_first"] and p["full"]]
    disc=[100*(1-p["current"]/p["full"]) for p in firsts]
    cw=[100*(1-p["current"]/p["full"]) for p in P if p["full"]]
    dd=[x for x in disc if x>0.5]
    summ.append({"snapshot_date":"2026-10-13","wall":w,"total_reported":h["total"],"pages_fetched":pages,"products_parsed":len(firsts),"colorways_parsed":len(P),
      "share_products_discounted_pct":round(100*len(dd)/len(disc),1) if disc else None,
      "avg_discount_all_products_pct":round(st.mean(disc),1) if disc else None,
      "avg_discount_discounted_products_pct":round(st.mean(dd),1) if dd else None,
      "median_discount_discounted_pct":round(st.median(dd),1) if dd else None,
      "avg_discount_all_colorways_pct":round(st.mean(cw),1) if cw else None,
      "share_colorways_discounted_pct":round(100*sum(x>0.5 for x in cw)/len(cw),1) if cw else None})
with open(os.path.join(data,"nike_current_products.csv"),"w",newline="") as f:
    wr=csv.DictWriter(f,fieldnames=list(rows[0].keys())); wr.writeheader(); wr.writerows(rows)
with open(os.path.join(data,"nike_current_summary.csv"),"w",newline="") as f:
    wr=csv.DictWriter(f,fieldnames=list(summ[0].keys())); wr.writeheader(); wr.writerows(summ)
for s in summ: print(s)
