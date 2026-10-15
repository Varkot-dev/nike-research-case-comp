"""Zappos running-shoe listings sorted by recentSalesStyle (Zappos' own best-seller sort), men and women, all pages.
Output: raw/zappos_bestsellers_<tag>.jsonl.gz with rank (1 = top seller), brand, name, price, percentOff, reviews.
Usage: python3 -I pull_zappos_bestsellers.py <rawdir> <tag>   No login, generic UA, 2.5 s sleeps."""
import sys, os, json, time, subprocess, gzip
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
def get(url):
    for a in range(3):
        cp = subprocess.run(["curl","-s","-L","--compressed","-A",UA,"-H","Accept-Language: en-US,en;q=0.9","--max-time","60","-w","\n%{http_code}",url],capture_output=True,text=True)
        body,_,code = cp.stdout.rpartition("\n"); time.sleep(2.5)
        if code=="200": return body
        time.sleep(15*(a+1))
def state(h):
    i=h.find("window.__INITIAL_STATE__"); j=h.find("=",i)+1
    return json.JSONDecoder().raw_decode(h[j:].lstrip())[0]
raw,tag=sys.argv[1],sys.argv[2]; os.makedirs(raw,exist_ok=True)
out=gzip.open(os.path.join(raw,f"zappos_bestsellers_{tag}.jsonl.gz"),"wt")
for cat in ["men-running-shoes","women-running-shoes"]:
    for sortname,s in [("recentSales","recentSalesStyle/desc"),("featured","")]:
        p=0; rank=0
        while p<8:
            url=f"https://www.zappos.com/{cat}?p={p}"+(f"&s={s}" if s else "")
            h=get(url)
            if not h: break
            try: pr=state(h)["products"]
            except Exception as e: print("parse fail",url,e); break
            lst=pr.get("list") or []
            for x in lst:
                rank+=1
                out.write(json.dumps({"cat":cat,"sort":sortname,"page":p,"rank":rank,"total":pr.get("totalProductCount"),
                  **{k:x.get(k) for k in ["productId","brandName","productName","price","originalPrice","percentOff","onSale","reviewCount","productRating","isNew","productUrl"]}})+"\n")
            print(cat,sortname,p,len(lst),pr.get("totalProductCount"),flush=True)
            if len(lst)<100 or (p+1)*100>=(pr.get("totalProductCount") or 0): break
            p+=1
out.close()
