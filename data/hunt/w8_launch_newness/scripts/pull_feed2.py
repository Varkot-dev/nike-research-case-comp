import requests,json,time,sys
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
base="https://api.nike.com/product_feed/threads/v3/"
name=sys.argv[1]; extra=sys.argv[2:]
out={}
for a in range(0,1500,50):
    params=[('anchor',a),('count',50),('filter','marketplace(US)'),('filter','language(en)'),('filter','channelId(010794e5-35fe-4e32-aaff-cd2c74f89d61)'),('filter','exclusiveAccess(true,false)')]+[('filter',e) for e in extra]
    r=requests.get(base,params=params,headers={'User-Agent':UA},timeout=60)
    if r.status_code!=200: print(a,r.status_code); break
    ob=r.json()['objects']
    if not ob: break
    for o in ob: out[o['id']]=o
    time.sleep(0.4)
json.dump(list(out.values()),open(f'feed_{name}.json','w'))
print(name,len(out))
