# Zappos product pages from Common Crawl, brand from URL slug, price = schema.org offer price, list = MSRP PriceSpecification if present (matches the rendered "(NN% off)").
import sys,json,subprocess,gzip,re,random,os,time,csv,html
from concurrent.futures import ThreadPoolExecutor
OUT='cc_zappos_panel.csv'; IDX='raw/cc/zappos_idx'; os.makedirs(IDX,exist_ok=True)
crawls=sys.argv[1:]
brands=['nike','adidas','hoka','on','asics','new-balance','brooks','saucony']
N=80
def curl(args,m=150,tries=6):
    for t in range(tries):
        r=subprocess.run(["curl","-sS","-m",str(m)]+args,capture_output=True)
        if r.returncode==0 and r.stdout: return r.stdout
        time.sleep(4+4*t)
    return None
done=set()
if os.path.exists(OUT):
    for x in csv.reader(open(OUT)): done.add((x[0],x[1]))
newfile=not os.path.exists(OUT)
w=csv.writer(open(OUT,'a',newline=''))
if newfile: w.writerow(['coll','brand_q','ts','url','brand','category','price','msrp','status'])
def parse(t):
    b=re.search(r'"brand":\{"@type":"Brand","name":"([^"]*)"',t); c=re.search(r'"category":"([^"]*)"',t)
    p=re.search(r'"offers":\{[^}]*?"price":"([0-9.]+)"',t)
    m=re.search(r'"priceSpecification":\{[^}]*?"price":"([0-9.]+)"[^}]*MSRP',t) or re.search(r'"price":"([0-9.]+)","priceCurrency":"USD","priceType":"https://schema.org/MSRP"',t)
    if not p: return None
    return (html.unescape(b.group(1)) if b else '',html.unescape(c.group(1)) if c else '',float(p.group(1)),float(m.group(1)) if m else float(p.group(1)))
for c in crawls:
    for b in brands:
        if (c,b) in done: continue
        fn=f'{IDX}/{c}_{b}.jsonl'
        if not os.path.exists(fn):
            r=curl([f"https://index.commoncrawl.org/{c}-index?url=www.zappos.com/p/{b}-*&output=json&filter=status:200&limit=2500"],tries=5)
            if not r or not r.lstrip().startswith(b'{'): print('idxfail',c,b,flush=True); continue
            open(fn,'wb').write(r)
        recs=[json.loads(l) for l in open(fn,errors='ignore') if l.startswith('{')]
        d={}
        for j in recs: d.setdefault(j['url'].split('/color/')[0],j)
        recs=sorted(d.values(),key=lambda j:j['url']); random.Random(5).shuffle(recs); samp=recs[:N]
        def job(j):
            off=int(j['offset']);ln=int(j['length'])
            raw=curl(["-r",f"{off}-{off+ln-1}","https://data.commoncrawl.org/"+j['filename']],m=100,tries=3)
            if not raw: return [c,b,j['timestamp'],j['url'],'','','','','fetchfail']
            try: t=gzip.decompress(raw).decode('utf8','ignore')
            except Exception: return [c,b,j['timestamp'],j['url'],'','','','','gzfail']
            p=parse(t)
            return [c,b,j['timestamp'],j['url'],p[0],p[1],p[2],p[3],'ok'] if p else [c,b,j['timestamp'],j['url'],'','','','','noprice']
        with ThreadPoolExecutor(6) as ex:
            rows=list(ex.map(job,samp))
        for r in rows: w.writerow(r)
        print(c,b,len(recs),len(rows),sum(r[-1]=='ok' for r in rows),flush=True)
