"""Adaptive Wayback bisection for first nike.com markdown date per style colour.
usage: python3 -I wb_runner.py <sample.csv> <cdx_glob> <live.csv> <max_fetches>
sample.csv columns: code,release_date (YYYY-MM-DD). live.csv: code,current,full (today's product_feed).
Appends every parsed product price from every page to data/wb_obs.csv. Restartable (raw cache)."""
import sys, os, csv, glob, re, time, json, hashlib, subprocess, datetime as dt, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdp_parse import parse
W=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW=os.path.join(W,"raw","wb"); os.makedirs(RAW,exist_ok=True)
OBS=os.path.join(W,"data","wb_obs.csv"); LOG=os.path.join(W,"data","fetch_log.jsonl")
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
TODAY=dt.date(2026,10,13); THR=(30,60,90,180)
sample=list(csv.DictReader(open(sys.argv[1])))
rel={r["code"]:dt.date.fromisoformat(r["release_date"][:10]) for r in sample}
live={}
if os.path.exists(sys.argv[3]):
    for r in csv.DictReader(open(sys.argv[3])):
        try: live[r["code"]]=(float(r["current"]),float(r["full"]))
        except: pass
CODE=re.compile(r'/([A-Z0-9]{6}-[0-9]{3})(?:[?#/]|$)')
caps={}
for f in glob.glob(sys.argv[2]):
    for l in open(f):
        p=l.split()
        if len(p)<3 or p[2]!="200": continue
        m=CODE.search(p[1])
        if not m or m.group(1) not in rel: continue
        c=m.group(1); d=dt.date(int(p[0][:4]),int(p[0][4:6]),int(p[0][6:8]))
        day=(d-rel[c]).days
        if day<0: continue
        clean="?" not in p[1]
        k=(c,d)
        if k not in caps or (clean and "?" in caps[k][1]): caps[k]=(p[0],p[1])
capd={}
for (c,d),(ts,u) in caps.items(): capd.setdefault(c,[]).append(((d-rel[c]).days,ts,u))
for c in capd: capd[c].sort()
obs={}
def add_obs(c,day,disc):
    obs.setdefault(c,{}); obs[c][day]=obs[c].get(day,False) or disc
if os.path.exists(OBS):
    for r in csv.DictReader(open(OBS)):
        if r["code"] in rel:
            d=dt.date.fromisoformat(r["obs_date"]); add_obs(r["code"],(d-rel[r["code"]]).days,float(r["current"])<float(r["full"])-0.5)
done_urls=set()
if os.path.exists(OBS):
    for r in csv.DictReader(open(OBS)): done_urls.add(r["wayback_url"])
failed=set()
def state(c):
    age=(TODAY-rel[c]).days
    o=obs.get(c,{})
    F=min([d for d,x in o.items() if x and d>=0]+[math.inf])
    if c in live and live[c][0]<live[c][1]-0.5: F=min(F,age)
    lo=max([0]+[d for d,x in o.items() if not x and d<F])
    return lo,F,age
def next_cap(c):
    lo,F,age=state(c)
    cs=[x for x in capd.get(c,[]) if lo<x[0]<min(F,age+1) and wb(x) not in failed and wb(x) not in done_urls]
    if not cs: return None
    if F==math.inf: return cs[-1]
    gap=F-lo
    if gap<=14: return None
    if not any(lo<t<F for t in THR) and gap<=max(30,0.25*lo): return None
    mid=math.sqrt(max(lo,5)*F) if F/max(lo,5)>2 else (lo+F)/2
    return min(cs,key=lambda x:abs(x[0]-mid))
def wb(x): return f"https://web.archive.org/web/{x[1]}id_/{x[2]}"
last=[0.0]
def fetch(url):
    p=os.path.join(RAW,hashlib.sha1(url.encode()).hexdigest()[:16]+".html")
    if os.path.exists(p) and os.path.getsize(p)>5000: return p,"cached"
    for a in range(5):
        w=last[0]+6.5-time.time()
        if w>0: time.sleep(w)
        cp=subprocess.run(["curl","-s","-L","--compressed","-A",UA,"-o",p,"-w","%{http_code}","--max-time","120",url],capture_output=True,text=True)
        last[0]=time.time(); st=cp.stdout.strip()
        open(LOG,"a").write(json.dumps({"t":time.strftime("%Y-%m-%dT%H:%M:%S"),"url":url,"status":st})+"\n")
        if st=="200" and os.path.getsize(p)>5000: return p,200
        if st in ("404","403","400"): return None,st
        time.sleep((60 if st=="429" else 10)*(a+1))
    return None,st
newf=not os.path.exists(OBS)
fo=open(OBS,"a",newline=""); wr=csv.writer(fo)
if newf: wr.writerow(["target_code","code","obs_date","capture_ts","current","full","discount_pct","title","subtitle","wayback_url"])
n=0; maxf=int(sys.argv[4])
while n<maxf:
    progressed=False
    for c in sorted(rel):
        if n>=maxf: break
        x=next_cap(c)
        if x is None: continue
        url=wb(x); p,st=fetch(url); n+=1; progressed=True
        recs=None
        if p:
            recs=parse(open(p,encoding="utf-8",errors="ignore").read())
        if not recs:
            failed.add(url); print(c,x[0],"FAIL",st,flush=True); continue
        d=dt.date(int(x[1][:4]),int(x[1][4:6]),int(x[1][6:8]))
        got=False
        for r in recs:
            disc=round(100*(1-r["current"]/r["full"]),1)
            wr.writerow([c,r["code"],d.isoformat(),x[1],r["current"],r["full"],disc,r["title"],r["subtitle"],url])
            if r["code"] in rel: add_obs(r["code"],(d-rel[r["code"]]).days,r["current"]<r["full"]-0.5)
            if r["code"]==c: got=True
        fo.flush(); done_urls.add(url)
        if not got: failed.add(url)
        lo,F,age=state(c)
        print(c,"day",x[0],"got",got,"lo",lo,"F",F,flush=True)
    if not progressed: break
print("FETCHES",n)
