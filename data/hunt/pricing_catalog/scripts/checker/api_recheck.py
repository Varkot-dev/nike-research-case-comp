# Checker: re-pull page 1 of three nike.com product_wall API walls and compare prices with the hunter's union catalog.
import subprocess,json,sys,time,pandas as pd
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
base="https://api.nike.com/discover/product_wall/v1/marketplace/US/language/en/consumerChannelId/d9a5bc42-4b9c-4976-858a-f159cf99c647"
u=pd.read_csv(sys.argv[1]).set_index('productCode'); rows=[]
for path in ["/w/running-shoes-37v7jzy7ok","/w/dunk-shoes-90aohzy7ok","/w/jordan-shoes-37eefzy7ok"]:
    r=subprocess.run(["curl","-sS","-m","60","-A",UA,"-H","nike-api-caller-id: com.nike.commerce.nikedotcom.web",base+f"?path={path}&queryType=PRODUCTS&anchor=0&count=24"],capture_output=True,text=True)
    d=json.loads(r.stdout); print(path,"totalResources",d["pages"]["totalResources"])
    for g in d.get("productGroupings",[])[:24]:
        for p in g.get("products") or []:
            c=p["productCode"]; pr=p.get("prices") or {}
            if c in u.index:
                h=u.loc[c]; rows.append([path,c,h.initialPrice,h.currentPrice,pr.get("initialPrice"),pr.get("currentPrice")])
            else: rows.append([path,c,None,None,pr.get("initialPrice"),pr.get("currentPrice")])
    time.sleep(2)
R=pd.DataFrame(rows,columns=["wall","code","init_hunter","cur_hunter","init_now","cur_now"])
R["match"]=(R.init_hunter==R.init_now)&(R.cur_hunter==R.cur_now)
R.to_csv(sys.argv[2],index=False)
print(R.groupby("wall").agg(n=("code","size"),in_hunter=("init_hunter",lambda x:x.notna().sum()),match=("match","sum")))
print(R[~R.match & R.init_hunter.notna()].head(10).to_string())
