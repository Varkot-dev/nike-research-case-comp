"""Deckers earnings releases: first-quarter-section bullets for HOKA, UGG, domestic, international, DTC, wholesale net sales."""
import re, glob, os, csv
B='/home/user/nike-research-case-comp/data/hunt/peers_reported'
def qend(d):
    y,m=int(d[:4]),int(d[5:7])
    return {1:f'{y-1}-12-31',2:f'{y-1}-12-31',5:f'{y}-03-31',7:f'{y}-06-30',10:f'{y}-09-30'}.get(m)
rows=[]
PAT={'HOKA':r'HOKA®? brand (?:net )?sales','UGG':r'UGG®? brand (?:net )?sales','US (domestic)':r'Domestic net sales','International':r'International net sales','DTC':r'(?:Direct-to-Consumer|DTC)(?: \(DTC\))? net sales','Wholesale':r'Wholesale net sales','Total':r'Net sales (?:increased|decreased)'}
for fn in sorted(glob.glob(B+'/raw/releases_deckers/*.txt')):
    d=os.path.basename(fn)[:10]; e=qend(d)
    if not e: continue
    t=open(fn).read(); src=t.splitlines()[0].replace('SOURCE ','')
    for k,p in PAT.items():
        m=re.search(p+r'[^.$]{0,60}?(increased|decreased)\s+([\d\.]+)%\s+to\s+\$([\d,\.]+)\s+(million|billion)\s+compared\s+to\s+\$([\d,\.]+)\s+(million|billion)',t)
        if not m: continue
        f=lambda v,u: float(v.replace(',',''))*(1000 if u=='billion' else 1)
        g=float(m.group(2))*(-1 if m.group(1)=='decreased' else 1)
        rows.append(dict(company='deckers',period_end=e,metric='net_sales',segment=k,value=f(m.group(3),m.group(4)),prior=f(m.group(5),m.group(6)),yoy_reported_pct=g,unit='USD m',source=src))
with open(B+'/deckers_release_extract.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
for r in rows:
    if r['segment'] in ('HOKA','International','US (domestic)'): print(r['period_end'],r['segment'],r['value'],r['yoy_reported_pct'])
