import sys,json,subprocess,gzip,re,random,os,time,csv
from concurrent.futures import ThreadPoolExecutor
colls=sys.argv[1].split(','); N=int(sys.argv[2]); out=sys.argv[3]
def curl(args):
    for t in range(6):
        r=subprocess.run(["curl","-sS","-m","200"]+args,capture_output=True)
        if r.returncode==0 and r.stdout: return r.stdout
        time.sleep(5+5*t)
    return None
def money(s):
    m=re.search(r'[0-9]+(?:\.[0-9]+)?',s.replace(',','')); return float(m.group()) if m else None
def parse_nike(t):
    c=re.findall(r'data-testid="currentPrice-container"[^>]*>([^<]*)',t)
    i=re.findall(r'data-testid="initialPrice-container"[^>]*>([^<]*)',t)
    if not c: return None
    cur=money(c[0]); full=money(i[0]) if i else cur
    return full,cur
def parse_adidas(t):
    s=re.search(r'"standard_price":([0-9.]+)',t); p=re.search(r'"sale_price":([0-9.]+)',t)
    if not s: return None
    full=float(s.group(1)); cur=float(p.group(1)) if p else full
    return full,cur
brands={"nike":("www.nike.com/t/*",lambda u: "/t/" in u, parse_nike),
        "adidas":("www.adidas.com/us/*",lambda u: re.search(r'/us/[^/]+/[A-Z0-9]{6}\.html$',u) is not None, parse_adidas)}
done_pairs=set((x[0],x[1]) for x in csv.reader(open(out)) if len(x)>1)
rows=[]; w=csv.writer(open(out,"a",newline=""))
random.seed(42)
for c in colls:
    for b,(pat,ok,parse) in brands.items():
        fn=f"idx/{b}_{c}.jsonl"
        if (c,b) in done_pairs: continue
        tries=0
        while (not os.path.exists(fn) or os.path.getsize(fn)<1000) and tries<10:
            r=curl([f"https://index.commoncrawl.org/{c}-index?url={pat}&output=json&filter=status:200"])
            if r and r.lstrip().startswith(b'{"urlkey'): open(fn,"wb").write(r)
            else: print("idx retry",c,b,(r or b"")[:60],flush=True); time.sleep(30)
            tries+=1
        if not os.path.exists(fn): print("idx giveup",c,b,flush=True); continue
        recs=[]
        for l in open(fn):
            if not l.startswith("{"): continue
            try: j=json.loads(l)
            except Exception: continue
            if j.get("mime")=="text/html" and ok(j["url"]): recs.append(j)
        # dedupe by url
        d={}
        for j in recs: d.setdefault(j["urlkey"],j)
        recs=list(d.values())
        samp=random.sample(recs,min(N,len(recs)))
        print(c,b,"pool",len(recs),"sample",len(samp),flush=True)
        def job(j):
            off=int(j["offset"]); ln=int(j["length"])
            raw=curl(["-r",f"{off}-{off+ln-1}","https://data.commoncrawl.org/"+j["filename"]])
            if not raw: return [c,b,j["timestamp"],j["url"],"","","fetchfail",len(recs)]
            try: t=gzip.decompress(raw).decode("utf8","ignore")
            except Exception: return [c,b,j["timestamp"],j["url"],"","","gzfail",len(recs)]
            p=parse(t)
            if not p: return [c,b,j["timestamp"],j["url"],"","","noprice",len(recs)]
            return [c,b,j["timestamp"],j["url"],p[0],p[1],"ok",len(recs)]
        with ThreadPoolExecutor(4) as ex:
            for row in ex.map(job,samp): w.writerow(row)
        print(c,b,"done",flush=True)
