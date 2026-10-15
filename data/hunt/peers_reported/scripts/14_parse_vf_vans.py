"""VF releases: Vans brand quarterly growth by region (Americas, EMEA, APAC, Global), reported and constant currency,
from the 'Brand Revenue Growth' supplemental table. Quarter = VF fiscal quarter mapped to calendar quarter by release month."""
import re, glob, os, csv
B='/home/user/nike-research-case-comp/data/hunt/peers_reported'
def cq(d):
    y,m=int(d[:4]),int(d[5:7])
    # VF quarters end ~Jun/Sep/Dec/Mar; releases late Jul/Aug, Oct/Nov, Jan/Feb, May
    return {1:(y-1,4),2:(y-1,4),5:(y,1),7:(y,2),8:(y,2),10:(y,3),11:(y,3)}.get(m)
def n(s):
    s=s.replace(' ','').replace('%','')
    neg='(' in s; s=s.strip('()')
    return -float(s) if neg else float(s)
NUM=r'(\(?\s*-?\d+\s*\)?\s*%\s*\)?|\(\s*\d+\s*%\s*\))'
rows=[]
for fn in sorted(glob.glob(B+'/raw/releases_vf/*.txt')):
    d=os.path.basename(fn)[:10]; q=cq(d)
    if not q: continue
    t=re.sub(r'[\s|]+',' ',open(fn).read())
    m=re.search(r'Vans ?® ?% [Cc]hange ((?:'+NUM+r' ?){4})',t)
    if not m: print('miss',d); continue
    vals=[n(x) for x in re.findall(NUM,m.group(1))]
    m2=re.compile(r'% [Cc]hange [Cc]onstant [Cc]urrency\*? ((?:'+NUM+r' ?){4})').search(t,m.end())
    cc=[n(x) for x in re.findall(NUM,m2.group(1))] if m2 else [None]*4
    for reg,v,c in zip(['Americas','EMEA','APAC','Global'],vals,cc):
        rows.append(dict(company='vf_vans',cal_year=q[0],cal_q=q[1],region=reg,yoy_reported_pct=v,yoy_cc_pct=c,source=d))
# Global-only figures from the slide-format releases (narrative bullets), verified by grep of the release text
for (y,q,v,c,d) in [(2025,2,-14,-15,'2025-07-30 narrative'),(2025,3,-9,-11,'2025-10-28 narrative'),(2025,4,-8,-10,'2026-01-28 narrative')]:
    rows.append(dict(company='vf_vans',cal_year=y,cal_q=q,region='Global',yoy_reported_pct=v,yoy_cc_pct=c,source=d))
rows.sort(key=lambda r:(r['cal_year'],r['cal_q'],r['region']))
with open(B+'/vf_vans_regional_growth.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
for r in rows:
    if r['region'] in ('Americas','Global'): print(r)
