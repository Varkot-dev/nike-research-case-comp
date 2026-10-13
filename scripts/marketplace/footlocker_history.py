"""Foot Locker sale-page brand facet counts over time (Wayback + live)."""
import sys, os, json, csv
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from footlocker_parse_lib import blocks
from fetch import fname
data, rawlive = sys.argv[1], sys.argv[2]
BR=["Nike","Jordan","Converse","adidas","New Balance","ASICS","HOKA","On","PUMA","Saucony","Brooks"]
src=[]
for l in open(os.path.join(data,"wayback_manifest.jsonl")):
    d=json.loads(l)
    if d["src"]=="footlocker" and d["file"]:
        ts=d["timestamp"]; src.append(("sale_shoes" if "sale/shoes" in d["original"] else "sale_all",f"{ts[:4]}-{ts[4:6]}-{ts[6:8]}","wayback",d["file"]))
src.append(("sale_all","2026-10-13","live",os.path.join(rawlive,fname("https://www.footlocker.com/category/sale.html"))))
src.append(("sale_shoes","2026-10-13","live",os.path.join(rawlive,fname("https://www.footlocker.com/category/sale/shoes.html"))))
rows=[]; seen=set()
for page,date,s,f in sorted(src,key=lambda x:(x[0],x[1])):
    if (page,date) in seen: continue
    seen.add((page,date))
    b=blocks(open(f,encoding="utf-8",errors="ignore").read()); fb=b["brand_facet"]; tot=(b.get("pagination") or {}).get("totalResults")
    if not fb or not tot:
        rows.append({"page":page,"snapshot_date":date,"source":s,"total_sale_items":None,"brand":"PARSE_FAIL"}); continue
    for br in BR+["NikeInc(Nike+Jordan+Converse)"]:
        c=sum(fb.get(x,0) for x in ["Nike","Jordan","Converse"]) if br.startswith("NikeInc") else fb.get(br,0)
        rows.append({"page":page,"snapshot_date":date,"source":s,"total_sale_items":tot,"brand":br,"sale_items":c,"share_of_sale_pct":round(100*c/tot,1)})
with open(os.path.join(data,"footlocker_sale_brand_history.csv"),"w",newline="") as fh:
    wr=csv.DictWriter(fh,fieldnames=["page","snapshot_date","source","total_sale_items","brand","sale_items","share_of_sale_pct"]); wr.writeheader(); wr.writerows(rows)
for r in rows:
    if r["brand"] in ("Nike","NikeInc(Nike+Jordan+Converse)","PARSE_FAIL","HOKA","On","New Balance"): print(r)
