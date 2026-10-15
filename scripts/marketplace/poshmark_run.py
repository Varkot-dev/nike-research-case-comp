"""Fetch + parse Poshmark listing searches for iconic models; asking prices vs retail reference."""
import sys, os, re, csv, json, statistics as st, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import get
from poshmark_lib import listings
raw, data = sys.argv[1], sys.argv[2]
# model, query, title regex (must match), exclude regex, retail ref (USD), ref source
MODELS=[("Nike Dunk Low","nike dunk low",r"dunk\s*low",r"\bsb\b|kids|toddler|\bgs\b|\bps\b|\btd\b|youth|big kid|little kid|baby",120,"nike.com 2026-10-13 Dunk Low Retro men's full price $120"),
("Nike Air Force 1","nike air force 1",r"air\s*force\s*(1|one)|\baf1\b",r"kids|toddler|\bgs\b|\bps\b|\btd\b|youth|big kid|little kid|baby|\bmid\b|\bhigh\b|shadow|custom",115,"nike.com 2026-10-13 Air Force 1 '07 full price $115"),
("Air Jordan 1 Low","air jordan 1 low",r"(jordan|aj)\s*1\b.*low|(jordan|aj)\s*1\s*low",r"kids|toddler|\bgs\b|\bps\b|\btd\b|youth|big kid|little kid|baby|\bog\b|travis|fragment",120,"nike.com 2026-10-13 Air Jordan 1 Low full price $120"),
("Air Jordan 1 High OG","air jordan 1 retro high og",r"(jordan|aj)\s*1.*high",r"kids|toddler|\bgs\b|\bps\b|\btd\b|youth|big kid|little kid|baby|travis|fragment|off.?white|dior|union",185,"nike.com 2026-10-13 Air Jordan 1 Retro High OG full price $185 (most colorways)"),
("Nike Zoom Vomero 5","nike vomero 5",r"vomero\s*5",r"kids|toddler|\bgs\b|\bps\b|\btd\b|youth|big kid|little kid|baby",170,"nike.com 2026-10-13 Zoom Vomero 5 full price $170"),
("HOKA Clifton","hoka clifton",r"clifton",r"kids|youth|toddler",155,"Running Warehouse 2026-10-13 Clifton 10 MSRP $155 (older Clifton 8/9 retailed lower)"),
("On Cloud","on cloud 6",r"\bcloud\s*(6|5)\b",r"kids|youth|toddler|waterproof|\bwp\b|versa|geo|push|terry|coast",160,"Foot Locker 2026-10-13 On Cloud 6 $160 (Cloud 5 retailed lower)")]
rows=[]
for model,q,inc,exc,ref,refsrc in MODELS:
    for cond in ["all","nwt"]:
        for pg in [1,2,3]:
            u="https://poshmark.com/search?query="+urllib.parse.quote(q)+"&type=listings&src=dir"+("&condition=nwt" if cond=="nwt" else "")+(f"&max_id={pg}" if pg>1 else "")
            p,s=get(u,os.path.join(raw,"search"))
            if not p: print("FAIL",u,s); continue
            L=listings(open(p,encoding="utf-8",errors="ignore").read()) or []
            for o in L:
                t=o.get("title") or ""; tl=t.lower()
                cat=((o.get("catalog") or {}).get("category_obj") or {}).get("display")
                dept=((o.get("catalog") or {}).get("department_obj") or {}).get("display")
                price=float((o.get("price_amount") or {}).get("val") or 0)
                keep = bool(re.search(inc,tl)) and not re.search(exc,tl) and cat=="Shoes" and dept in("Men","Women") and price>=20
                rows.append({"snapshot_date":"2026-10-13","model":model,"query":q,"condition_filter":cond,"page":pg,"listing_id":o.get("id"),"title":t,"department":dept,"category":cat,
                    "condition":o.get("condition"),"size":o.get("size"),"asking_price":price,"seller_original_price":float((o.get("original_price_amount") or {}).get("val") or 0) or None,
                    "created_at":o.get("created_at"),"retail_ref":ref,"retail_ref_source":refsrc,"included":keep,"ask_to_retail":round(price/ref,3)})
            print(model,cond,pg,s,len(L),flush=True)
# dedupe listing within model+cond
seen=set(); R=[]
for r in rows:
    k=(r["model"],r["condition_filter"],r["listing_id"])
    if k in seen: continue
    seen.add(k); R.append(r)
with open(os.path.join(data,"poshmark_listings.csv"),"w",newline="") as fh:
    wr=csv.DictWriter(fh,fieldnames=list(R[0].keys())); wr.writeheader(); wr.writerows(R)
S=[]
for model,q,inc,exc,ref,refsrc in MODELS:
    for cond in ["all","nwt"]:
        X=[r for r in R if r["model"]==model and r["condition_filter"]==cond and r["included"]]
        if not X: S.append({"model":model,"condition_filter":cond,"n":0}); continue
        rat=sorted(r["ask_to_retail"] for r in X); pr=sorted(r["asking_price"] for r in X)
        S.append({"snapshot_date":"2026-10-13","model":model,"condition_filter":cond,"n_listings_raw":sum(1 for r in R if r["model"]==model and r["condition_filter"]==cond),"n":len(X),"retail_ref":ref,
          "median_ask":st.median(pr),"mean_ask":round(st.mean(pr),1),"median_ask_to_retail":round(st.median(rat),3),
          "p25_ask_to_retail":round(rat[len(rat)//4],3),"p75_ask_to_retail":round(rat[(3*len(rat))//4],3),
          "share_ask_above_retail_pct":round(100*sum(x>1 for x in rat)/len(rat),1),"share_nwt_pct":round(100*sum(r["condition"]=="nwt" for r in X)/len(X),1),"retail_ref_source":refsrc})
with open(os.path.join(data,"poshmark_summary.csv"),"w",newline="") as fh:
    keys=list(next(s for s in S if "median_ask" in s).keys())
    wr=csv.DictWriter(fh,fieldnames=keys); wr.writeheader(); [wr.writerow({k:s.get(k) for k in keys}) for s in S]
for s in S: print({k:s.get(k) for k in ("model","condition_filter","n","median_ask","median_ask_to_retail","p25_ask_to_retail","p75_ask_to_retail","share_ask_above_retail_pct")})
