"""Fetch all pages of selected nike.com walls via the public product_wall JSON endpoint the wall page itself calls."""
import sys, re, json, os, html as H
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import get, fname
raw=sys.argv[1]
WALLS=sys.argv[2:]
for w in WALLS:
    p=os.path.join(raw,fname("https://www.nike.com/w/"+w))
    t=open(p,encoding="utf-8",errors="ignore").read()
    m=re.search(r'"pageData":\{"next":"([^"]+)".*?"totalPages":(\d+),"totalResources":(\d+)',t)
    nxt=json.loads('"'+m.group(1)+'"'); tp=int(m.group(2))
    base=re.sub(r'anchor=\d+','anchor={a}',nxt)
    for i in range(1,tp):
        url="https://api.nike.com"+base.format(a=24*i)
        f,s=get(url,os.path.join(raw,"api"))
        print(w,i,s,flush=True)
