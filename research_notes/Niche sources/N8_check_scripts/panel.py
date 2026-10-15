import json,glob,os,sys,csv,datetime
src=sys.argv[1]; out=sys.argv[2]
REV=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet','RevenueFromContractWithCustomerIncludingAssessedTax','SalesRevenueServicesNet']
OPI=['OperatingIncomeLoss']
def series(facts,tags):
    res={}
    for tag in tags:
        f=facts.get('us-gaap',{}).get(tag)
        if not f: continue
        for u in f['units'].get('USD',[]):
            if u.get('form') not in ('10-K','10-K/A','10-KT'): continue
            if not u.get('start'): continue
            s=datetime.date.fromisoformat(u['start']); e=datetime.date.fromisoformat(u['end'])
            d=(e-s).days
            if d<340 or d>380: continue
            k=u['end']
            prev=res.get(k)
            # keep highest priority tag; within tag latest filed
            cand=(tags.index(tag),-int(u['filed'].replace('-','')),u['val'])
            if prev is None or cand[:2]<prev[:2]: res[k]=cand
    return {k:v[2] for k,v in res.items()}
rows=[]
for fn in sorted(glob.glob(src+'/*.json')):
    t=os.path.basename(fn)[:-5]
    if t=='EL2': continue
    d=json.load(open(fn)); fa=d['facts']
    rv=series(fa,REV); op=series(fa,OPI)
    for k in sorted(rv):
        if k in op and rv[k]>0:
            rows.append((t,d['entityName'],k,rv[k],op[k],op[k]/rv[k]*100))
with open(out,'w',newline='') as f:
    w=csv.writer(f); w.writerow(['ticker','name','fye','rev','opinc','margin']); w.writerows(rows)
import collections
c=collections.Counter(r[0] for r in rows); print(len(c)); print(dict(c))
