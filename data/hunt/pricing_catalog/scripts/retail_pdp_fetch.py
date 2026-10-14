# Fetch a random sample of Common Crawl captures of a Shopify retailer's product pages and read vendor, price and compare-at price.
# usage: python3 -I retail_pdp_fetch.py idxdir host N out.csv coll1 coll2 ...
import sys,json,subprocess,gzip,re,random,os,time,csv
from concurrent.futures import ThreadPoolExecutor
idx,host,N,out=sys.argv[1],sys.argv[2],int(sys.argv[3]),sys.argv[4]; colls=sys.argv[5:]
def curl(args):
    for t in range(6):
        r=subprocess.run(["curl","-sS","-m","200"]+args,capture_output=True)
        if r.returncode==0 and r.stdout: return r.stdout
        time.sleep(5+5*t)
    return None
def parse(t):
    v=re.search(r'"vendor":"([^"]+)"',t)
    if not v: return None
    k=t.find('"variants":[')
    seg=t[k:k+60000] if k>0 else t
    pr=[int(x) for x in re.findall(r'"price":([0-9]+)[,}]',seg)]
    ca=[int(x) for x in re.findall(r'"compare_at_price":([0-9]+)[,}]',seg)]
    av=re.findall(r'"available":(true|false)',seg)
    ty=re.search(r'"type":"([^"]*)"',t)
    ti=re.search(r'<title>([^<]+)',t)
    if not pr: return None
    # Shopify product JSON prices are in cents
    return v.group(1),min(pr)/100,(max(ca)/100 if ca else ""),sum(1 for a in av if a=="true"),len(av),(ty.group(1) if ty else ""),(ti.group(1).strip()[:120] if ti else "")
newf=not os.path.exists(out)
w=csv.writer(open(out,"a",newline=""))
if newf: w.writerow(["coll","host","ts","url","vendor","price_min","compare_max","n_avail","n_flags","type","title","status","pool"])
for c in colls:
    fn=os.path.join(idx,f"{host}_{c}.jsonl")
    if not os.path.exists(fn): print("noidx",c); continue
    d={}
    for l in open(fn,errors="ignore"):
        try: j=json.loads(l)
        except Exception: continue
        u=j["url"].split("?")[0]
        if j.get("status")=="200" and "/products/" in u and "/collections/" not in u: d.setdefault(u,j)
    recs=sorted(d.values(),key=lambda j:j["url"]); random.Random(11).shuffle(recs)
    samp=recs[:N]; print(c,"pool",len(recs),"sample",len(samp),flush=True)
    def job(j):
        off=int(j["offset"]); ln=int(j["length"])
        raw=curl(["-r",f"{off}-{off+ln-1}","https://data.commoncrawl.org/"+j["filename"]])
        try: t=gzip.decompress(raw).decode("utf8","ignore")
        except Exception: return [c,host,j["timestamp"],j["url"]]+[""]*7+["fail",len(recs)]
        p=parse(t)
        if not p: return [c,host,j["timestamp"],j["url"]]+[""]*7+["noprice",len(recs)]
        return [c,host,j["timestamp"],j["url"],*p,"ok",len(recs)]
    with ThreadPoolExecutor(4) as ex:
        for r in ex.map(job,samp): w.writerow(r)
    print(c,"done",flush=True)
