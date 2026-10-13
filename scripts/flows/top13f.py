import csv,sys,collections
r=list(csv.DictReader(open(sys.argv[1])))
P=['31-DEC-2024','31-MAR-2025','30-JUN-2025','30-SEP-2025','31-DEC-2025','31-MAR-2026','30-JUN-2026']
G={'0000102909':'Vanguard (all entities)','0002100119':'Vanguard (all entities)','0002100121':'Vanguard (all entities)','0000933478':'Vanguard (all entities)','0001680208':'Vanguard (all entities)','0001811242':'Vanguard (all entities)',
   '0001422849':'Capital Group (CWI+CII+CRGI)','0001562230':'Capital Group (CWI+CII+CRGI)','0001422848':'Capital Group (CWI+CII+CRGI)'}
agg=collections.defaultdict(lambda:collections.Counter()); nm={}
for x in r:
    k=G.get(x['cik'],x['cik']); nm[k]=G.get(x['cik'],x['manager'].strip())
    for p in P: agg[k][p]+=int(x['sh_'+p]); agg[k]['put'+p]+=int(x['put_'+p]); agg[k]['call'+p]+=int(x['call_'+p])
L=sorted(agg,key=lambda k:-agg[k]['30-JUN-2026'])
CLB=1203921077
rows=[]
for i,k in enumerate(L[:25]):
    a=agg[k]
    rows.append(dict(rank=i+1,holder=nm[k],key=k,**{p:a[p] for p in P},pct_classB_jun26=round(a['30-JUN-2026']/CLB*100,2),chg_q2_26=a['30-JUN-2026']-a['31-MAR-2026'],chg_q1_26=a['31-MAR-2026']-a['31-DEC-2025'],chg_since_dec24=a['30-JUN-2026']-a['31-DEC-2024']))
w=csv.DictWriter(open(sys.argv[2],'w',newline=''),fieldnames=list(rows[0].keys()));w.writeheader();w.writerows(rows)
for x in rows: print(x['rank'],x['holder'][:36],round(x['30-JUN-2026']/1e6,2),x['pct_classB_jun26'],'q2',round(x['chg_q2_26']/1e6,2),'q1',round(x['chg_q1_26']/1e6,2),'vsDec24',round(x['chg_since_dec24']/1e6,2))
# flows per quarter
fl=[]
for j in range(1,len(P)):
    a,b=P[j-1],P[j]
    ch=[(agg[k][b]-agg[k][a],k) for k in agg]
    for d,k in ch:
        if abs(d)>=1_500_000:
            kind='new' if agg[k][a]==0 else ('exit' if agg[k][b]==0 else ('add' if d>0 else 'cut'))
            fl.append(dict(quarter=b,holder=nm[k],key=k,prev=agg[k][a],now=agg[k][b],change=d,kind=kind))
fl.sort(key=lambda x:(x['quarter'],-x['change']))
w=csv.DictWriter(open(sys.argv[3],'w',newline=''),fieldnames=list(fl[0].keys()));w.writeheader();w.writerows(fl)
for q in ('31-DEC-2025','31-MAR-2026','30-JUN-2026','31-MAR-2025','30-JUN-2025','30-SEP-2025'):
    print('==',q)
    for x in fl:
        if x['quarter']==q and x['key'] not in ('0001374170',): print('  ',x['kind'],x['holder'][:40],round(x['prev']/1e6,2),'->',round(x['now']/1e6,2))
# HHI and puts/calls by top option holders Jun 26
for p in P:
    tot=sum(agg[k][p] for k in agg); hhi=sum((agg[k][p]/tot*100)**2 for k in agg)
    print(p,'13F holders(grouped)',sum(1 for k in agg if agg[k][p]>0),'HHI',round(hhi),'top5',round(sum(sorted([agg[k][p] for k in agg],reverse=True)[:5])/CLB*100,1),'% of class B')
print('top put holders Jun26',[(nm[k][:25],agg[k]['put30-JUN-2026']) for k in sorted(agg,key=lambda k:-agg[k]['put30-JUN-2026'])[:8]])
print('top call holders Jun26',[(nm[k][:25],agg[k]['call30-JUN-2026']) for k in sorted(agg,key=lambda k:-agg[k]['call30-JUN-2026'])[:8]])
