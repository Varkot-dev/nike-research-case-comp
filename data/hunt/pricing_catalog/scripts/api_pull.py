# Pull every product on a nike.com US wall via the public product_wall API the site itself calls.
# usage: python3 -I api_pull.py outdir path1 [path2 ...]   (path like /w/running-shoes-37v7jzy7ok)
# IMPORTANT: attributeIds from the first response must be passed on every page, otherwise the API ignores path after page 1.
# Walls >10000 items are pulled twice (price asc and desc) and de-duplicated downstream.
import sys, json, time, subprocess, csv, os, datetime
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
base="https://api.nike.com/discover/product_wall/v1/marketplace/US/language/en/consumerChannelId/d9a5bc42-4b9c-4976-858a-f159cf99c647"
out=sys.argv[1]; os.makedirs(out,exist_ok=True)
cols=["wall","fetched_utc","groupKey","productCode","productType","productSubType","title","subTitle","color","initialPrice","currentPrice","employeePrice","discountPct","badge","featured","isNewUntil","promotions","pdp"]
def get(q):
    for t in range(5):
        r=subprocess.run(["curl","-sS","-m","60","-A",UA,"-H","nike-api-caller-id: com.nike.commerce.nikedotcom.web",base+q],capture_output=True,text=True)
        try: return json.loads(r.stdout)
        except Exception: time.sleep(5+5*t)
    return None
for path in sys.argv[2:]:
    sorts=[""]
    d=get(f"?path={path}&queryType=PRODUCTS&anchor=0&count=24")
    if not d or "pages" not in d: print("fail",path); continue
    tot=d["pages"]["totalResources"]
    attrs=d.get("attributeIds") or []
    if isinstance(attrs,list): attrs=",".join(attrs)
    aq=f"&attributeIds={attrs}" if attrs else ""
    if tot>10000: sorts=["priceAsc","priceDesc"]
    fn=os.path.join(out,"api_"+path.strip("/").replace("/","_")+".csv")
    f=open(fn,"w",newline=""); w=csv.writer(f); w.writerow(cols); n=0
    now=datetime.datetime.now(datetime.UTC).isoformat(timespec="seconds")
    for s in sorts:
        anchor=0
        while anchor<min(tot,10000):
            d=get(f"?path={path}{aq}&queryType=PRODUCTS&anchor={anchor}&count=100"+(f"&sortBy={s}" if s else ""))
            if not d or "pages" not in d: print("stop",path,anchor); break
            gs=d.get("productGroupings") or []
            for g in gs:
                for p in g.get("products") or []:
                    pr=p.get("prices") or {}; c=p.get("copy") or {}
                    w.writerow([path,now,p.get("groupKey"),p.get("productCode"),p.get("productType"),p.get("productSubType"),c.get("title"),c.get("subTitle"),((p.get("displayColors") or {}).get("colorDescription")),pr.get("initialPrice"),pr.get("currentPrice"),pr.get("employeePrice"),pr.get("discountPercentage"),p.get("badgeLabel"),"|".join(p.get("featuredAttributes") or []),p.get("isNewUntil"),json.dumps(p.get("promotions")) if p.get("promotions") else "",(p.get("pdpUrl") or {}).get("path")]); n+=1
            if not gs: break
            anchor+=100; time.sleep(1.2)
    f.close(); print(path,tot,n,flush=True)
