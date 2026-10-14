import sys, json, time, subprocess, csv
path, attr, out = sys.argv[1], sys.argv[2], sys.argv[3]
sort=sys.argv[4] if len(sys.argv)>4 else ""
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
base="https://api.nike.com/discover/product_wall/v1/marketplace/US/language/en/consumerChannelId/d9a5bc42-4b9c-4976-858a-f159cf99c647"
anchor=0; rows=[]; total=None
while True:
    q=f"?path={path}"+(f"&attributeIds={attr}" if attr!="-" else "")+f"&queryType=PRODUCTS&anchor={anchor}&count=100"+(f"&sortBy={sort}" if sort else "")
    for t in range(4):
        r=subprocess.run(["curl","-sS","-m","60","-A",UA,"-H","nike-api-caller-id: com.nike.commerce.nikedotcom.web",base+q],capture_output=True,text=True)
        try: d=json.loads(r.stdout); break
        except Exception: time.sleep(5)
    else: print("fail",anchor); break
    if "pages" not in d: print("stop",anchor,str(d)[:200]); break
    total=d["pages"]["totalResources"]
    for g in d.get("productGroupings") or []:
        for p in g.get("products") or []:
            pr=p.get("prices") or {}
            rows.append([g.get("products")[0].get("groupKey"),p.get("productCode"),p.get("productType"),(p.get("copy") or {}).get("title"),(p.get("copy") or {}).get("subTitle"),pr.get("initialPrice"),pr.get("currentPrice"),pr.get("discountPercentage"),json.dumps(p.get("promotions")) if p.get("promotions") else ""])
    anchor+=100
    print(anchor,total,len(rows),flush=True)
    if anchor>=total or anchor>=10000 or not d.get("productGroupings"): break
    time.sleep(1)
with open(out,"w",newline="") as f:
    w=csv.writer(f); w.writerow(["groupKey","productCode","productType","title","subTitle","initialPrice","currentPrice","discountPct","promotions"]); w.writerows(rows)
print("done",total,len(rows))
