"""Running Warehouse brand summary from Wayback snapshots + live (men's road catalog and men's clearance)."""
import sys, os, json, csv, re, collections, statistics as st
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rw_parse import parse
from fetch import fname
data, rawlive = sys.argv[1], sys.argv[2]
srcs=[]
for d in (json.loads(l) for l in open(os.path.join(data,"fetch_log.jsonl"))):
    if d["status"]==200 and "runningwarehouse.com/catpage-" in d["url"]:
        page="mens_road" if "MBESTUSE" in d["url"] else "mens_clearance" if "SALEMS" in d["url"] else None
        if not page: continue
        if "web.archive.org" in d["url"]:
            ts=re.search(r"/web/(\d{14})",d["url"]).group(1); date=f"{ts[:4]}-{ts[4:6]}-{ts[6:8]}"
        else: date=d["t"][:10]
        srcs.append((page,date,d["file"]))
FOC=["Nike","Hoka","On Running","Brooks","ASICS","New Balance","adidas","Saucony","Skechers Performance","PUMA","Mizuno","Altra Run Natural"]
out=[]
for page,date,f in sorted(set(srcs)):
    R=parse(open(f,encoding="utf-8",errors="ignore").read())
    if not R:
        out.append({"page":page,"snapshot_date":date,"brand":"PARSE_FAIL","colorways":0}); continue
    for b in FOC+["ALL"]:
        L=R if b=="ALL" else [r for r in R if r["brand"]==b]
        sale=[r for r in L if r["on_sale"]]
        out.append({"page":page,"snapshot_date":date,"brand":b,"colorways":len(L),"colorway_share_pct":round(100*len(L)/len(R),1),"models":len({r["model"] for r in L}),
          "colorways_on_sale":len(sale),"share_on_sale_pct":round(100*len(sale)/len(L),1) if L else None,"avg_discount_on_sale_pct":round(st.mean(r["discount_pct"] for r in sale),1) if sale else None})
with open(os.path.join(data,"runningwarehouse_history.csv"),"w",newline="") as fh:
    wr=csv.DictWriter(fh,fieldnames=["page","snapshot_date","brand","colorways","colorway_share_pct","models","colorways_on_sale","share_on_sale_pct","avg_discount_on_sale_pct"]); wr.writeheader(); wr.writerows(out)
for o in out:
    if o["brand"] in ("Nike","Hoka","On Running","Brooks","ASICS","ALL","PARSE_FAIL"): print(o)
