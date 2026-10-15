"""nike.com wall history from Wayback snapshots + current live first page (same first-page method) -> tidy CSVs."""
import sys, os, json, csv, statistics as st
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from nike_parse_lib import parse_html
from fetch import fname
data, rawcur = sys.argv[1], sys.argv[2]
recs=[]
def summarize(wall,date,src,f):
    try: r=parse_html(open(f,encoding="utf-8",errors="ignore").read())
    except Exception as e: r={"format":"error:"+str(e)[:40],"total":None,"products":[]}
    P=r["products"]; F=[p for p in P if p.get("is_first",True) and p["full"]]
    d=[100*(1-p["current"]/p["full"]) for p in F]; dd=[x for x in d if x>0.5]
    cw=[100*(1-p["current"]/p["full"]) for p in P if p["full"]]
    return {"wall":wall,"snapshot_date":date,"source":src,"parse_format":r["format"],"total_reported":r["total"],"first_page_products":len(F),"first_page_colorways":len(P),
      "fp_share_products_discounted_pct":round(100*len(dd)/len(d),1) if d else None,"fp_avg_discount_all_pct":round(st.mean(d),1) if d else None,
      "fp_avg_discount_discounted_pct":round(st.mean(dd),1) if dd else None,"fp_share_colorways_discounted_pct":round(100*sum(x>0.5 for x in cw)/len(cw),1) if cw else None,
      "fp_avg_discount_colorways_pct":round(st.mean(cw),1) if cw else None,"file":f}
seen=set()
for l in open(os.path.join(data,"wayback_manifest.jsonl")):
    d=json.loads(l)
    if d["src"]!="nike" or d["status"] not in (200,"cached") or not d["file"]: continue
    wall=d["original"].split("/w/")[1].split("?")[0]; ts=d["timestamp"]
    if (wall,ts) in seen: continue
    seen.add((wall,ts))
    recs.append(summarize(wall,f"{ts[:4]}-{ts[4:6]}-{ts[6:8]}","wayback",d["file"]))
for w in ["sale-3yaep","mens-shoes-nik1zy7ok","womens-shoes-5e1x6zy7ok","mens-sale-shoes-3yaepznik1zy7ok","womens-sale-shoes-3yaepz5e1x6zy7ok","sale-shoes-3yaepzy7ok","shoes-y7ok"]:
    recs.append(summarize(w,"2026-10-13","live",os.path.join(rawcur,fname("https://www.nike.com/w/"+w))))
recs.sort(key=lambda r:(r["wall"],r["snapshot_date"]))
with open(os.path.join(data,"nike_wall_history.csv"),"w",newline="") as fh:
    wr=csv.DictWriter(fh,fieldnames=list(recs[0].keys())); wr.writeheader(); wr.writerows(recs)
# sale ratio: mens-sale-shoes / mens-shoes by quarter
def q(dt): y,m=int(dt[:4]),int(dt[5:7]); return f"{y}Q{(m-1)//3+1}"
byq={}
for r in recs:
    if r["total_reported"] is None: continue
    byq.setdefault((q(r["snapshot_date"]),r["wall"]),r)
out=[]
for qq in sorted({k[0] for k in byq}):
    g=lambda w: byq.get((qq,w),{}).get("total_reported")
    ms,mt,sa=g("mens-sale-shoes-3yaepznik1zy7ok"),g("mens-shoes-nik1zy7ok"),g("sale-3yaep")
    out.append({"quarter":qq,"mens_sale_shoes_count":ms,"mens_shoes_count":mt,"mens_sale_share_pct":round(100*ms/mt,1) if ms and mt else None,
      "womens_shoes_count":g("womens-shoes-5e1x6zy7ok"),"womens_sale_shoes_count":g("womens-sale-shoes-3yaepz5e1x6zy7ok"),"all_sale_count":sa,
      "mens_shoes_fp_share_discounted_pct":byq.get((qq,"mens-shoes-nik1zy7ok"),{}).get("fp_share_products_discounted_pct"),
      "womens_shoes_fp_share_discounted_pct":byq.get((qq,"womens-shoes-5e1x6zy7ok"),{}).get("fp_share_products_discounted_pct"),
      "sale_wall_fp_avg_discount_discounted_pct":byq.get((qq,"sale-3yaep"),{}).get("fp_avg_discount_discounted_pct"),
      "mens_sale_fp_avg_discount_discounted_pct":byq.get((qq,"mens-sale-shoes-3yaepznik1zy7ok"),{}).get("fp_avg_discount_discounted_pct"),
      "snapshot_dates":";".join(sorted({byq[k]["snapshot_date"] for k in byq if k[0]==qq}))})
with open(os.path.join(data,"nike_sale_share_quarterly.csv"),"w",newline="") as fh:
    wr=csv.DictWriter(fh,fieldnames=list(out[0].keys())); wr.writeheader(); wr.writerows(out)
for o in out: print(o)
print("PARSE FAILS:",[(r["wall"],r["snapshot_date"],r["parse_format"]) for r in recs if not r["first_page_products"]])
