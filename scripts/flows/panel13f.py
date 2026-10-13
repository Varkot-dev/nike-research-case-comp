import csv,sys,collections,datetime
raw=list(csv.DictReader(open(sys.argv[1])))
P=['31-DEC-2024','31-MAR-2025','30-JUN-2025','30-SEP-2025','31-DEC-2025','31-MAR-2026','30-JUN-2026']
fd=lambda s:datetime.datetime.strptime(s,'%d-%b-%Y')
by=collections.defaultdict(list)
for r in raw:
    if r['period'] in P: by[(r['cik'],r['period'])].append(r)
panel={}
names={}
for (cik,p),L in by.items():
    L.sort(key=lambda r:(fd(r['filing_date']),r['accession']))
    base=None; adds=[]
    for r in L:
        if r['amend']!='Y' or (r['amend_type'] or '').upper().startswith('RESTATE'): base=r; adds=[]
        elif 'NEW' in (r['amend_type'] or '').upper(): adds.append(r)
    if base is None: base=L[-1]
    sh=float(base['shares'])+sum(float(a['shares']) for a in adds)
    val=float(base['value'])+sum(float(a['value']) for a in adds)
    CL={'31-DEC-2024':75.67,'31-MAR-2025':63.48,'30-JUN-2025':71.04,'30-SEP-2025':69.73,'31-DEC-2025':63.71,'31-MAR-2026':52.82,'30-JUN-2026':41.05}
    if sh>0 and val>0 and (val/sh/CL[p])<0.1 and not (0.0004<val/sh/CL[p]<0.002):
        print('FIX',base['manager'],p,sh,val,file=sys.stderr); sh=val/CL[p]
    panel[(cik,p)]=dict(shares=sh,value=val,put=float(base['put_shares']),call=float(base['call_shares']))
    names[cik]=base['manager']
ciks=sorted(set(c for c,_ in panel))
out=[]
for c in ciks:
    row=dict(cik=c,manager=names[c])
    for p in P:
        x=panel.get((c,p)); row['sh_'+p]=int(x['shares']) if x else 0
        row['put_'+p]=int(x['put']) if x else 0; row['call_'+p]=int(x['call']) if x else 0
    out.append(row)
out.sort(key=lambda r:-r['sh_30-JUN-2026'])
w=csv.DictWriter(open(sys.argv[2],'w',newline=''),fieldnames=list(out[0].keys()));w.writeheader();w.writerows(out)
# summary
SO=1485308829
for p in P:
    tot=sum(r['sh_'+p] for r in out); n=sum(1 for r in out if r['sh_'+p]>0)
    vals=[panel[(c,p)]['value'] for c in ciks if (c,p) in panel]
    top=sorted([r['sh_'+p] for r in out],reverse=True)
    print(p,'holders',n,'shares',tot,'pctClassB_1203.9m',round(tot/1203921077*100,1),'top10 share of 13F',round(sum(top[:10])/tot*100,1),'top20',round(sum(top[:20])/tot*100,1),'value$bn',round(sum(vals)/1e9,2),'impl px',round(sum(vals)/tot,2),
      'puts',sum(r['put_'+p] for r in out),'calls',sum(r['call_'+p] for r in out))
