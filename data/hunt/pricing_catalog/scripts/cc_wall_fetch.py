# Fetch every Common Crawl capture (latest per crawl) of the target nike.com walls; parse item count and first-page prices.
# usage: python3 -I cc_wall_fetch.py indexdir targets.txt out.csv
import sys,json,glob,subprocess,gzip,os,time,csv
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from wallparse import parse_wall_any
idx,tg,out=sys.argv[1:4]
T=set("/w/"+l.strip() for l in open(tg) if l.strip())
done=set()
if os.path.exists(out):
    for r in csv.DictReader(open(out)): done.add((r["coll"],r["wall"]))
newf=not os.path.exists(out)
w=csv.writer(open(out,"a",newline=""))
if newf: w.writerow(["coll","ts","wall","count","n_prices","n_disc","share_disc","mean_depth_disc","method","warc","offset"])
for fn in sorted(glob.glob(os.path.join(idx,"*_nike_w.jsonl"))):
    c=os.path.basename(fn)[:15]
    best={}
    for l in open(fn,errors="ignore"):
        try: j=json.loads(l)
        except Exception: continue
        if j.get("status")!="200": continue
        u=j["url"].replace("https://www.nike.com","").replace("http://www.nike.com","")
        if "?" in u: continue
        if u in T and (u not in best or j["timestamp"]>best[u]["timestamp"]): best[u]=j
    for u,j in best.items():
        if (c,u[3:]) in done: continue
        off=int(j["offset"]); ln=int(j["length"]); t=None
        for k in range(5):
            r=subprocess.run(["curl","-sS","-m","120","-r",f"{off}-{off+ln-1}","https://data.commoncrawl.org/"+j["filename"]],capture_output=True)
            try: t=gzip.decompress(r.stdout).decode("utf8","ignore"); break
            except Exception: time.sleep(5)
        if t is None: continue
        n,p,m=parse_wall_any(t)
        d=[1-b/a for a,b in p if a>0 and b<a-0.01]
        w.writerow([c,j["timestamp"],u[3:],n,len(p),len(d),round(len(d)/len(p),3) if p else "",round(sum(d)/len(d),3) if d else "",m,j["filename"],off])
        print(c,u,n,len(p),len(d),flush=True)
