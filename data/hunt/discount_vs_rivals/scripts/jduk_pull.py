# JD Sports UK brand footwear listing pages (server-embedded product JSON: price, wasPrice). robots.txt: sort/search/comma params disallowed; brand pages and ?from= paging are not.
import re,json,time,csv,urllib.request,datetime as dt
UA="Mozilla/5.0 (compatible; research-bot/1.0)"
import gzip
brands={'adidas':'adidas','nike':'nike','jordan':'jordan','hoka':'hoka','on':'on-running','asics':'asics','new-balance':'new-balance','puma':'puma','brooks':'brooks','saucony':'saucony','under-armour':'under-armour','reebok':'reebok'}
out={};log=[];today=dt.date.today().isoformat()
def get(u):
    r=urllib.request.Request(u,headers={'User-Agent':UA,'Accept-Encoding':'gzip'})
    d=urllib.request.urlopen(r,timeout=60).read()
    try: d=gzip.decompress(d)
    except Exception: pass
    return d.decode('utf8','ignore')
pat=re.compile(r'\{"objectID":"(\d+)","name":"([^"]*)"(.*?)"price":(\d+(?:\.\d+)?)(?:,"priceFormatted":"[^"]*")?(?:,"wasPrice":(\d+(?:\.\d+)?))?',re.S)
for gen in ['men/mens-footwear','women/womens-footwear']:
  for b,slug in brands.items():
    hits=None
    for p in range(0,8):
        u=f"https://www.jdsports.co.uk/{gen}/brand/{slug}/"+(f"?from={72*p}" if p else "")
        s=None
        for att in range(4):
            try: s=get(u); break
            except Exception as e:
                log.append((u,'ERR',str(e)[:50],att)); time.sleep(20*(att+1))
        if s is None: break
        m=re.search(r'"nbHits":(\d+)',s); hits=int(m.group(1)) if m else None
        n=0
        for m in pat.finditer(s):
            oid,name,mid,price,was=m.groups()
            if len(mid)>400: continue
            key=(gen,oid)
            if key not in out:
                out[key]=dict(pulled=today,gender=gen.split('/')[0],brand_query=b,objectID=oid,name=name,price_gbp=float(price),was_gbp=float(was) if was else '',nbHits=hits); n+=1
        log.append((u,'ok',n,hits)); time.sleep(6)
        if n==0 or (hits and 72*(p+1)>=hits): break
rows=list(out.values())
with open('jduk_live_listings_20261014.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
open('raw/jduk_pull_log.txt','w').write('\n'.join(map(str,log)));print(len(rows))
