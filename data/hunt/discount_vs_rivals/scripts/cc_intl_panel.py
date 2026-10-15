# Germany like-for-like: adidas.de vs nike.com/de product pages from Common Crawl, same crawls, random sample per crawl.
# usage: python3 -I cc_intl_panel.py N crawl1 crawl2 ...
import sys,json,subprocess,gzip,re,random,os,time,csv
from concurrent.futures import ThreadPoolExecutor
N=int(sys.argv[1]); colls=sys.argv[2:]; OUT='cc_intl_de_panel.csv'; IDX='raw/cc/intl_idx'; os.makedirs(IDX,exist_ok=True)
SITES={'adidas':('www.adidas.de/*',lambda j: re.search(r'/[A-Z0-9]{6}\.html$',j['url'].split('?')[0]) is not None),
       'nike':('www.nike.com/de/t/*',lambda j: '/de/t/' in j['url'] and '/u/' not in j['url'])}
def curl(args,m=150,tries=6):
    for t in range(tries):
        r=subprocess.run(["curl","-sS","-m",str(m)]+args,capture_output=True)
        if r.returncode==0 and r.stdout: return r.stdout
        time.sleep(5+5*t)
    return None
def money(s):
    m=re.search(r'[0-9]+(?:[.,][0-9]+)?',s.replace('.','').replace(',','.')); return float(m.group()) if m else None
def parse(brand,t):
    if brand=='adidas':
        st=re.search(r'"standard_price":([0-9.]+)',t); sp=re.search(r'"sale_price":([0-9.]+)',t)
        if not st: return None
        f=float(st.group(1)); return f,(float(sp.group(1)) if sp else f),'std_sale'
    c=re.findall(r'data-testid="currentPrice-container"[^>]*>([^<]*)',t)
    if c:
        i=re.findall(r'data-testid="initialPrice-container"[^>]*>([^<]*)',t); cur=money(c[0]); return (money(i[0]) if i else cur),cur,'testid'
    m=re.search(r'"fullPrice":([0-9.]+),"currentPrice":([0-9.]+)',t)
    if m: return float(m.group(1)),float(m.group(2)),'json_first'
    return None
done=set()
if os.path.exists(OUT):
    for x in csv.reader(open(OUT)): done.add((x[0],x[1],x[3]))
newf=not os.path.exists(OUT); w=csv.writer(open(OUT,'a',newline=''))
if newf: w.writerow(['coll','brand','ts','url','full','current','method','status','pool'])
for c in colls:
    for brand,(pat,ok) in SITES.items():
        fn=f'{IDX}/{brand}_{c}.jsonl'
        if not os.path.exists(fn):
            r=None
            for t in range(8):
                np_=curl([f"https://index.commoncrawl.org/{c}-index?url={pat}&showNumPages=true"],tries=1)
                try: pages=json.loads(np_)['pages']; break
                except Exception: pages=None; time.sleep(8+6*t)
            if pages is None: print('idxfail',c,brand,flush=True); continue
            data=b''
            for p in range(min(pages,8)):
                for t in range(8):
                    r=curl([f"https://index.commoncrawl.org/{c}-index?url={pat}&output=json&filter=status:200&page={p}"],tries=1)
                    if r and r.lstrip().startswith(b'{'): data+=r; break
                    time.sleep(8+6*t)
            open(fn,'wb').write(data)
        d={}
        for l in open(fn,errors='ignore'):
            if not l.startswith('{'): continue
            try: j=json.loads(l)
            except Exception: continue
            if j.get('mime','text/html')=='text/html' and ok(j): d.setdefault(j['url'].split('?')[0],j)
        recs=sorted(d.values(),key=lambda j:j['url']); random.Random(11).shuffle(recs)
        samp=[j for j in recs[:N] if (c,brand,j['url']) not in done]
        print(c,brand,'pool',len(recs),'todo',len(samp),flush=True)
        def job(j):
            off=int(j['offset']);ln=int(j['length'])
            raw=curl(["-r",f"{off}-{off+ln-1}","https://data.commoncrawl.org/"+j['filename']],m=120,tries=4)
            if not raw: return [c,brand,j['timestamp'],j['url'],'','','','fetchfail',len(recs)]
            try: t=gzip.decompress(raw).decode('utf8','ignore')
            except Exception: return [c,brand,j['timestamp'],j['url'],'','','','gzfail',len(recs)]
            p=parse(brand,t)
            return [c,brand,j['timestamp'],j['url'],p[0],p[1],p[2],'ok',len(recs)] if p else [c,brand,j['timestamp'],j['url'],'','','','noprice',len(recs)]
        with ThreadPoolExecutor(4) as ex: rows=list(ex.map(job,samp))
        for r in rows: w.writerow(r)
        print(c,brand,'done',sum(r[7]=='ok' for r in rows),flush=True)
