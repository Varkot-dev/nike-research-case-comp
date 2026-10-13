import sys, json
sys.path.insert(0, sys.argv[1])
from cdx import quarterly
from fetch import get
idx=json.load(open(sys.argv[2])); outdir=sys.argv[3]; man=[]
for cat,rows in idx.items():
    # dedupe by timestamp, prefer quarterly pick
    for r in quarterly(rows):
        url=f"https://web.archive.org/web/{r['timestamp']}id_/{r['original']}"
        p,s=get(url,outdir)
        man.append({"cat":cat,"timestamp":r["timestamp"],"original":r["original"],"file":p,"status":s})
        print(cat,r["timestamp"],s,flush=True)
json.dump(man,open(sys.argv[4],"w"),indent=0)
