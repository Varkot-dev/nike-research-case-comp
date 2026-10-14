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
def parse(t,url):
    code=re.search(r'/([A-Z0-9]{6}-[0-9]{3})(?:$|[/?])',url)
    code=code.group(1) if code else None
    # 1) 2024+ markup
    c=re.findall(r'data-testid="currentPrice-container"[^>]*>([^<]*)',t)
    if c:
        i=re.findall(r'data-testid="initialPrice-container"[^>]*>([^<]*)',t)
        cur=money(c[0]); full=money(i[0]) if i else cur
        if code is None:
            m=re.search(r'Style: ?</?[^>]*>?\s*([A-Z0-9]{6}-[0-9]{3})',t) or re.search(r'"styleColor":"([A-Z0-9]{6}-[0-9]{3})"',t)
            code=m.group(1) if m else None
        return full,cur,code,"testid"
    # 2) JSON state keyed by styleColor (2019-2023 PDPs)
    if code:
        k=t.find(f'"styleColor":"{code}"')
        if k>0:
            win=t[max(0,k-3000):k+3000]
            f=re.search(r'"fullPrice":([0-9.]+)',win); cp=re.search(r'"currentPrice":([0-9.]+)',win)
            if f and cp: return float(f.group(1)),float(cp.group(1)),code,"json_style"
    f=re.search(r'"fullPrice":([0-9.]+)',t); cp=re.search(r'"currentPrice":([0-9.]+)',t)
    if f and cp:
        m=re.search(r'"styleColor":"([A-Z0-9]{6}-[0-9]{3})"',t)
        return float(f.group(1)),float(cp.group(1)),code or (m.group(1) if m else None),"json_first"
    # 3) old css classes
    cur=re.findall(r'is--current-price[^>]*>\$?([0-9.,]+)',t); st=re.findall(r'is--striked-out[^>]*>\$?([0-9.,]+)',t)
    if cur: return (money(st[0]) if st else money(cur[0])),money(cur[0]),code,"css"
    return None
done=set()
if os.path.exists(out):
    for x in csv.reader(open(out)): done.add((x[0],x[3]))
w=csv.writer(open(out,"a",newline=""))
if not os.path.exists(out) or os.path.getsize(out)==0: w.writerow(["coll","brand","ts","url","full","current","style","method","status","pool"])
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
        if not raw: return [c,"nike",j["timestamp"],j["url"],"","","","","fetchfail",len(recs)]
        try: t=gzip.decompress(raw).decode("utf8","ignore")
        except Exception: return [c,"nike",j["timestamp"],j["url"],"","","","","gzfail",len(recs)]
        p=parse(t,j["url"])
        if not p: return [c,"nike",j["timestamp"],j["url"],"","","","","noprice",len(recs)]
        return [c,"nike",j["timestamp"],j["url"],p[0],p[1],p[2],p[3],"ok",len(recs)]
    with ThreadPoolExecutor(4) as ex:
        for r in ex.map(job,samp): w.writerow(r)
    print(c,"done",flush=True)
