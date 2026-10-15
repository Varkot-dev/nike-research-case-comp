# Foot Locker brand pages, first page only (48 products, relevance sort). robots.txt disallows currentPage= and sort= so no paging.
import re,json,time,csv,urllib.request,datetime as dt
UA="Mozilla/5.0 (compatible; research-bot/1.0)"
brands=['nike','jordan','adidas','hoka','on','asics','new-balance','brooks','saucony','puma','under-armour','reebok','converse','vans','salomon','mizuno']
urls=[]
for b in brands:
    urls+= [f"https://www.footlocker.com/category/brands/{b}.html",f"https://www.footlocker.com/category/mens/{b}.html",f"https://www.footlocker.com/category/womens/{b}.html"]
urls+=["https://www.footlocker.com/category/mens/shoes.html","https://www.footlocker.com/category/womens/shoes.html","https://www.footlocker.com/category/sale/mens/shoes.html","https://www.footlocker.com/category/sale/womens/shoes.html"]
out=[];log=[];today=dt.date.today().isoformat()
dec=json.JSONDecoder()
for u in urls:
    try: s=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=40).read().decode('utf8','ignore')
    except Exception as e: log.append((u,'ERR',str(e)[:50])); continue
    i=s.find('"products":[{"badges"')
    if i<0: log.append((u,'noproducts')); continue
    lst,_=dec.raw_decode(s[i+len('"products":'):])
    tot=re.search(r'"totalResults":(\d+)',s)
    for it in lst:
        out.append(dict(pulled=today,url=u,name=it.get('name'),sku=it.get('baseProduct') or it.get('sku'),price=it['price']['value'],orig=it['originalPrice']['value'],isSale=it.get('isSaleProduct'),discExcl=it.get('badges',{}).get('isDiscountsExcluded'),isNew=it.get('isNewProduct'),total=tot.group(1) if tot else ''))
    log.append((u,'ok',len(lst),tot.group(1) if tot else ''))
    time.sleep(2)
with open('footlocker_live_listings_20261014.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=out[0].keys());w.writeheader();w.writerows(out)
open('raw/footlocker_pull_log.txt','w').write('\n'.join(map(str,log)));print(len(out))
