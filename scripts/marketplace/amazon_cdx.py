import sys, json, time
sys.path.insert(0, sys.argv[1])
from cdx import cdx
CATS={"mens_running":("Mens-Running-Shoes","679286011"),"womens_running":("Womens-Running-Shoes","679360011"),
"mens_fashion_sneakers":("Mens-Fashion-Sneakers","679312011"),"womens_fashion_sneakers":("Womens-Fashion-Sneakers","679394011"),
"mens_athletic":("Mens-Athletic-Shoes","6127770011"),"womens_athletic":("Womens-Athletic-Shoes","6127771011")}
out={}
for cat,(slug,node) in CATS.items():
    rows=[]
    for u in [f"amazon.com/Best-Sellers-Clothing-Shoes-Jewelry-{slug}/zgbs/fashion/{node}",f"amazon.com/gp/bestsellers/fashion/{node}",f"amazon.com/Best-Sellers-{slug}/zgbs/fashion/{node}",f"amazon.com/zgbs/fashion/{node}"]:
        r=cdx(u,"prefix"); time.sleep(3)
        if r: rows+= [x for x in r if "pg=2" not in x["original"] and int(x.get("length") or 0)>20000]
    rows.sort(key=lambda x:x["timestamp"])
    out[cat]=rows
    print(cat,len(rows),[x["timestamp"][:8] for x in rows],flush=True)
json.dump(out,open(sys.argv[2],"w"),indent=0)
