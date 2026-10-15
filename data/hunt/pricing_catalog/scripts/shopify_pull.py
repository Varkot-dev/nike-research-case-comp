# Pull full public Shopify catalogs (/products.json) of US sneaker and running retailers.
# usage: python3 -I shopify_pull.py rawdir tidy.csv host1 host2 ...
import sys, json, time, subprocess, os, gzip, csv, datetime
raw=sys.argv[1]; tidy=sys.argv[2]; hosts=sys.argv[3:]; os.makedirs(raw,exist_ok=True)
UA="Mozilla/5.0 (compatible; research-bot; price-study)"
newf=not os.path.exists(tidy)
w=csv.writer(open(tidy,"a",newline=""))
if newf: w.writerow(["store","fetched_utc","product_id","vendor","product_type","title","handle","created_at","published_at","updated_at","n_variants","n_avail","price_min","price_max","compare_max","n_var_disc","disc_pct_max","tags"])
for h in hosts:
    now=datetime.datetime.now(datetime.UTC).isoformat(timespec="seconds"); allp=[]
    for page in range(1,81):
        for t in range(4):
            r=subprocess.run(["curl","-sS","-L","-m","60","-A",UA,f"https://{h}/products.json?limit=250&page={page}"],capture_output=True)
            try: d=json.loads(r.stdout); break
            except Exception: time.sleep(8+8*t); d=None
        if not d or not d.get("products"): break
        allp+=d["products"]; time.sleep(1.5)
    with gzip.open(os.path.join(raw,f"{h}_{now[:10]}.json.gz"),"wt") as f:
        # slim raw: drop images/body to keep files small
        json.dump([{k:v for k,v in p.items() if k not in("images","body_html","image","options")} for p in allp],f)
    for p in allp:
        vs=p.get("variants") or []
        pr=[float(v["price"]) for v in vs if v.get("price")]
        ca=[float(v["compare_at_price"]) for v in vs if v.get("compare_at_price")]
        nd=sum(1 for v in vs if v.get("compare_at_price") and float(v["compare_at_price"])>float(v["price"])+0.01)
        dp=max([1-float(v["price"])/float(v["compare_at_price"]) for v in vs if v.get("compare_at_price") and float(v["compare_at_price"])>0]+[0])
        w.writerow([h,now,p["id"],p.get("vendor"),p.get("product_type"),p.get("title"),p.get("handle"),p.get("created_at"),p.get("published_at"),p.get("updated_at"),len(vs),sum(1 for v in vs if v.get("available")),min(pr) if pr else "",max(pr) if pr else "",max(ca) if ca else "",nd,round(100*dp,1),"|".join((p.get("tags") or [])[:25]) if isinstance(p.get("tags"),list) else p.get("tags")])
    print(h,len(allp),flush=True)
