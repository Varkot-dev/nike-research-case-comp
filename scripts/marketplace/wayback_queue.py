"""Build one prioritized Wayback fetch queue across series and fetch sequentially (single host, slow)."""
import sys, os, json, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cdx import quarterly
import fetch
fetch_delay=float(os.environ.get("WB_DELAY","15"))
data=sys.argv[1]; raw=sys.argv[2]
items=[]
idx=json.load(open(os.path.join(data,"amazon_cdx_index.json")))
for cat,rows in idx.items():
    for r in quarterly(rows): items.append(("amazon",cat,r["timestamp"],r["original"]))
for f in glob.glob(os.path.join(data,"cdx_*.txt")):
    series=os.path.basename(f)[4:-4]
    for l in open(f):
        if l.startswith("#") or not l.strip(): continue
        ts,orig,_=l.split()
        items.append(("nike" if "nike" in series else "footlocker",series,ts,orig))
def prio(it):
    src,cat,ts,_=it; y=int(ts[:4]); m=int(ts[4:6]); q=(m-1)//3+1
    tier=0 if y>=2025 else (1 if q in (1,3) else 2)
    # within tier: nike first, then amazon running, then rest
    order={"nike":0,"amazon":1,"footlocker":2}[src]
    if src=="amazon" and "running" not in cat: order=3
    return (tier,order,ts)
items.sort(key=prio)
man_path=os.path.join(data,"wayback_manifest.jsonl")
done={json.loads(l)["url"] for l in open(man_path)} if os.path.exists(man_path) else set()
print(len(items),"items",flush=True)
for src,cat,ts,orig in items:
    url=f"https://web.archive.org/web/{ts}id_/{orig}"
    p,s=fetch.get(url,os.path.join(raw,f"{src}_wayback"),delay=fetch_delay,retries=3)
    with open(man_path,"a") as f: f.write(json.dumps({"src":src,"cat":cat,"timestamp":ts,"original":orig,"url":url,"file":p,"status":s})+"\n")
    print(src,cat,ts,s,flush=True)
