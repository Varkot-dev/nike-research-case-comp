# Checker: re-fetch a random sample of panel rows from Common Crawl WARCs and re-parse price independently.
# usage: python3 -I cc_refetch.py <folder> <n_nike> <n_adidas> <out.csv>
import sys,os,json,gzip,re,random,subprocess,time,csv
import pandas as pd
F=sys.argv[1]; NN=int(sys.argv[2]); NA=int(sys.argv[3]); out=sys.argv[4]
def curl(args):
    for t in range(5):
        r=subprocess.run(["curl","-sS","-m","120"]+args,capture_output=True)
        if r.returncode==0 and r.stdout: return r.stdout
        time.sleep(4+4*t)
    return None
def idx(brand,coll,url,ts):
    fn=f"{F}/raw/cc_pdp_idx/{brand}_{coll}.jsonl.gz"
    for l in gzip.open(fn,"rt",errors="ignore"):
        if not l.startswith("{"): continue
        j=json.loads(l)
        if j["url"].split("?")[0]==url and j["timestamp"]==str(ts): return j
def num(s):
    m=re.search(r'[0-9]+(?:\.[0-9]+)?',s.replace(',','')); return float(m.group()) if m else None
def parse_nike(t,url):
    # independent: rendered price containers first, then any JSON-LD offers price
    code=re.search(r'/([A-Z0-9]{6}-[0-9A-Z]{3})',url); code=code.group(1) if code else None
    cur=re.search(r'currentPrice-container"[^>]*>\s*\$?([0-9.,]+)',t)
    ini=re.search(r'initialPrice-container"[^>]*>\s*\$?([0-9.,]+)',t)
    if cur: return (num(ini.group(1)) if ini else num(cur.group(1)), num(cur.group(1)),"testid")
    if code:
        i=t.find(f'"styleColor":"{code}"')
        if i>=0:
            m=re.search(r'"fullPrice":([0-9.]+),"currentPrice":([0-9.]+)',t[i:i+6000])
            if m: return float(m.group(1)),float(m.group(2)),"json"
    return None
def parse_adidas(t,url):
    s=re.search(r'"standard_price":\s*"?([0-9.]+)',t); p=re.search(r'"sale_price":\s*"?([0-9.]+)',t)
    if s: return float(s.group(1)), float(p.group(1)) if p else float(s.group(1)),"std_sale"
    return None
rows=[]
nk=pd.concat([pd.read_csv(f"{F}/cc_pdp_panel_nike.csv"),pd.read_csv(f"{F}/cc_pdp_panel_nike_part2.csv")]); nk=nk[nk.status=="ok"]
ad=pd.read_csv(f"{F}/cc_pdp_panel_adidas.csv"); ad=ad[ad.status=="ok"]
samp=[("nike",r) for _,r in nk.sample(NN,random_state=int(time.time())%1000).iterrows()]+[("adidas",r) for _,r in ad.sample(NA,random_state=11).iterrows()]
for b,r in samp:
    j=idx(b,r.coll,r.url,r.ts)
    if not j: rows.append([b,r.coll,r.url,r.full,r.current,"","","","noidx"]); continue
    off=int(j["offset"]); ln=int(j["length"])
    raw=curl(["-r",f"{off}-{off+ln-1}","https://data.commoncrawl.org/"+j["filename"]])
    time.sleep(1)
    try: t=gzip.decompress(raw).decode("utf8","ignore")
    except Exception: rows.append([b,r.coll,r.url,r.full,r.current,"","","","fetchfail"]); continue
    p=(parse_nike if b=="nike" else parse_adidas)(t,r.url)
    if not p: rows.append([b,r.coll,r.url,r.full,r.current,"","","","noparse"]); continue
    ok=abs(p[0]-r.full)<0.01 and abs(p[1]-r.current)<0.01
    rows.append([b,r.coll,r.url,r.full,r.current,p[0],p[1],p[2],"match" if ok else "MISMATCH"])
    print(rows[-1],flush=True)
w=csv.writer(open(out,"w",newline="")); w.writerow(["brand","coll","url","full_panel","cur_panel","full_recheck","cur_recheck","method","result"]); w.writerows(rows)
