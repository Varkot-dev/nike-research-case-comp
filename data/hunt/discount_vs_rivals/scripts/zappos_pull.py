import re,json,time,sys,csv,gzip,urllib.request,datetime as dt
UA="Mozilla/5.0 (compatible; research-bot/1.0)"
brands=['nike','adidas','hoka','on','asics','new-balance','brooks','saucony','puma','jordan','under-armour','skechers','reebok']
cats=['running-shoes','sneakers','basketball-shoes','athletic-shoes']
out=[];log=[]
def get(u):
    r=urllib.request.Request(u,headers={'User-Agent':UA})
    return urllib.request.urlopen(r,timeout=40).read().decode('utf8','ignore')
def extract(s):
    i=s.find('"list":[{"sizing"')
    if i<0: return None,0
    m=re.search(r'"totalProductCount":(\d+)',s)
    j=i+len('"list":'); dec=json.JSONDecoder()
    lst,_=dec.raw_decode(s[j:])
    return lst,int(m.group(1)) if m else 0
today=dt.date.today().isoformat()
for b in brands:
  for c in cats:
    for p in range(0,3):
        u=f"https://www.zappos.com/{b}-{c}"+(f"?p={p}" if p else "")
        try: s=get(u)
        except Exception as e:
            log.append((u,'ERR',str(e)[:60])); break
        lst,tot=extract(s)
        if not lst: log.append((u,'nolist',0)); break
        n=0
        for it in lst:
            out.append(dict(pulled=today,query=f"{b}-{c}",page=p,brand=it.get('brandName'),productId=it.get('productId'),styleId=it.get('styleId'),name=it.get('productName'),gender='|'.join(it.get('txAttrFacet_Gender') or []),price=it.get('price'),originalPrice=it.get('originalPrice'),percentOff=it.get('percentOff'),onSale=it.get('onSale'),productType=it.get('productType'),total=tot)); n+=1
        log.append((u,'ok',n,tot))
        time.sleep(1.5)
        if len(lst)<100: break
with open('zappos_live_listings_20261014.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=out[0].keys());w.writeheader();w.writerows(out)
open('raw/zappos_pull_log.txt','w').write('\n'.join(map(str,log)))
print(len(out)); print('\n'.join(map(str,log)))
