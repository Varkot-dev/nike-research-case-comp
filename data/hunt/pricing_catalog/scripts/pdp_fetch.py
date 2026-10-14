# Fetch a random sample of Common Crawl captures of nike.com product pages per crawl and read price, list price, style code.
# usage: python3 -I pdp_fetch.py idxdir N out.csv coll1 coll2 ...
import sys,json,subprocess,gzip,re,random,os,time,csv
from concurrent.futures import ThreadPoolExecutor
idx=sys.argv[1]; N=int(sys.argv[2]); out=sys.argv[3]; colls=sys.argv[4:]
def curl(args):
    for t in range(6):
        r=subprocess.run(["curl","-sS","-m","200"]+args,capture_output=True)
        if r.returncode==0 and r.stdout: return r.stdout
        time.sleep(5+5*t)
    return None
def money(s):
    m=re.search(r'[0-9]+(?:\.[0-9]+)?',s.replace(',','')); return float(m.group()) if m else None
def json_objects(t):
    """Map styleColor -> (release_date, fullPrice, currentPrice) from the PDP's embedded product JSON.
    Each colourway object lists styleColor, then seoProductReleaseDate, then fullPrice/currentPrice."""
    ev=[(m.start(),"S",m.group(1)) for m in re.finditer(r'"styleColor":"([A-Z0-9]{6}-[0-9A-Z]{3})"',t)]
    ev+=[(m.start(),"R",m.group(1)[:10]) for m in re.finditer(r'"seoProductReleaseDate":"([^"]+)"',t)]
    ev+=[(m.start(),"P",(float(m.group(1)),float(m.group(2)))) for m in re.finditer(r'"fullPrice":([0-9.]+),"currentPrice":([0-9.]+)',t)]
    ev.sort(); out={}
    for i,(pos,k,v) in enumerate(ev):
        if k!="S": continue
        rel=None; pr=None
        for pos2,k2,v2 in ev[i+1:i+4]:
            if k2=="S": break
            if k2=="R": rel=v2
            if k2=="P": pr=v2; break
        if pr and v not in out: out[v]=(rel,pr[0],pr[1])
    return out
def parse(t,url):
    code=re.search(r'/([A-Z0-9]{6}-[0-9A-Z]{3})(?:$|[/?])',url)
    code=code.group(1) if code else None
    objs=json_objects(t)
    if code is None:
        m=re.search(r'Style: ?(?:<[^>]+>)*\s*([A-Z0-9]{6}-[0-9A-Z]{3})',t) or re.search(r'"styleColor":"([A-Z0-9]{6}-[0-9A-Z]{3})"',t)
        code=m.group(1) if m else None
    rel=objs.get(code,(None,))[0] if code else None
    c=re.findall(r'data-testid="currentPrice-container"[^>]*>([^<]*)',t)
    if c:
        i=re.findall(r'data-testid="initialPrice-container"[^>]*>([^<]*)',t)
        cur=money(c[0]); full=money(i[0]) if i else cur
        return full,cur,code,"testid",rel
    if code in objs:
        r,f,cp=objs[code]; return f,cp,code,"json_obj",r
    red=re.findall(r'data-test="product-price-reduced"[^>]*>([^<]+)',t); fp=re.findall(r'data-test="product-price"[^>]*>([^<]+)',t)
    if red or fp:
        cur=money(red[0]) if red else money(fp[0]); full=money(fp[0]) if fp else cur
        return full,cur,code,"datatest",rel
    return None
newf=not os.path.exists(out)
done=set()
if os.path.exists(out):
    for x in csv.reader(open(out)): done.add((x[0],x[3]))
w=csv.writer(open(out,"a",newline=""))
if newf: w.writerow(["coll","brand","ts","url","full","current","style","method","release_date","status","pool"])
for c in colls:
    fn=os.path.join(idx,f"nike_{c}.jsonl")
    if not os.path.exists(fn): print("noidx",c); continue
    d={}
    for l in open(fn,errors="ignore"):
        if not l.startswith("{"): continue
        try: j=json.loads(l)
        except Exception: continue
        if j.get("status")=="200" and j.get("mime","text/html")=="text/html" and "/t/" in j["url"] and "/u/" not in j["url"]:
            d.setdefault(j["url"].split("?")[0],j)
    recs=sorted(d.values(),key=lambda j:j["url"]); random.Random(7).shuffle(recs)
    samp=[j for j in recs[:N] if (c,j["url"]) not in done]
    print(c,"pool",len(recs),"todo",len(samp),flush=True)
    def job(j):
        off=int(j["offset"]); ln=int(j["length"])
        raw=curl(["-r",f"{off}-{off+ln-1}","https://data.commoncrawl.org/"+j["filename"]])
        if not raw: return [c,"nike",j["timestamp"],j["url"],"","","","","","fetchfail",len(recs)]
        try: t=gzip.decompress(raw).decode("utf8","ignore")
        except Exception: return [c,"nike",j["timestamp"],j["url"],"","","","","","gzfail",len(recs)]
        p=parse(t,j["url"])
        if not p: return [c,"nike",j["timestamp"],j["url"],"","","","","","noprice",len(recs)]
        return [c,"nike",j["timestamp"],j["url"],p[0],p[1],p[2],p[3],p[4],"ok",len(recs)]
    with ThreadPoolExecutor(4) as ex:
        for r in ex.map(job,samp): w.writerow(r)
    print(c,"done",flush=True)
