"""Compare live Amazon Best Seller listed (lowest shown) price of Nike items with nike.com full price for the same model name."""
import sys, os, csv, re, collections
data=sys.argv[1]
full=collections.defaultdict(collections.Counter)
for r in csv.DictReader(open(os.path.join(data,"nike_current_products.csv"))):
    if r["full"]: full[(r["title"] or "").strip()][float(r["full"])]+=1
MAP={"Run Defy":"Nike Run Defy","Revolution 8":"Nike Revolution 8","Run Swift 3":"Nike Run Swift 3","Air Monarch IV":"Nike Air Monarch IV","Court Vision Lo":"Nike Court Vision Low","Air Max Excee":"Nike Air Max Excee","Downshifter 14":"Nike Downshifter 14","Pegasus 42":"Nike Pegasus 42"}
out=[]
for r in csv.DictReader(open(os.path.join(data,"amazon_bestsellers_items.csv"))):
    if r["brand"]!="Nike" or r["source"]!="live": continue
    key=next((v for k,v in MAP.items() if k.lower() in r["title"].lower()),None)
    fp=full[key].most_common(1)[0][0] if key and full[key] else None
    p=float(r["price_low"]) if r["price_low"] else None
    out.append({"snapshot_date":r["snapshot_date"],"category":r["category"],"rank":r["rank"],"title":r["title"],"asin":r["asin"],"amazon_price_shown":p,"nike_com_model":key,"nike_com_full_price":fp,
        "amazon_vs_full_pct":round(100*(p/fp-1),1) if p and fp else None})
with open(os.path.join(data,"amazon_nike_price_vs_nikecom.csv"),"w",newline="") as fh:
    wr=csv.DictWriter(fh,fieldnames=list(out[0].keys())); wr.writeheader(); wr.writerows(out)
for o in out: print(o["category"],o["rank"],o["title"][:40],o["amazon_price_shown"],o["nike_com_full_price"],o["amazon_vs_full_pct"])
