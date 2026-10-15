import csv,collections,statistics as st,datetime
rows=list(csv.DictReader(open('../panel.csv')))
P=collections.defaultdict(dict)
for r in rows:
    y=(datetime.date.fromisoformat(r['fye'])-datetime.timedelta(days=75)).year
    P[r['ticker']][y]=(float(r['rev']),float(r['opinc']))
cd=['LULU','RL','TPR','UAA','VFC','PVH','COLM','DECK','CROX','WWW','HBI','LEVI','SKX','CPRI','FOSL','CRI','GIII','OXM','PLCE','CHS','SHOO','ANF','AEO','URBN','GPS','LB','FL','KSS','M','BBY','HAS','MAT','HOG','PII','WHR','NWL','LEA','TIF','SBUX','MCD','YUM','DRI','DPZ','CMG','MAR','HLT','NCLH','LZB','TPX','HELE','BC','YETI','SONO','GPRO','PTON','COTY','EL']
for h in (2,3):
  out=[]
  for k in cd:
    d=P.get(k,{})
    for t in d:
        if t+h in d:
            dr=d[t+h][0]-d[t][0]; do=d[t+h][1]-d[t][1]
            if dr/d[t][0]<=-0.05 and d[t][1]>0: out.append((k,t,dr/d[t][0],-do/-dr))
  v=sorted(x[3] for x in out)
  print(f'h={h}: n={len(v)} windows with revenue fall>=5%; EBIT lost per $ lost: p25 {v[len(v)//4]:.2f} median {st.median(v):.2f} p75 {v[3*len(v)//4]:.2f}; share with ratio>=0.54: {sum(x>=0.54 for x in v)/len(v):.0%}; >=0.74: {sum(x>=0.74 for x in v)/len(v):.0%}')
  # excluding covid windows (spanning 2019->2020/2021)
  v2=sorted(x[3] for x in out if not (x[1]<=2020<=x[1]+h))
  print(f'   ex-2020-spanning: n={len(v2)} median {st.median(v2):.2f} p25 {v2[len(v2)//4]:.2f} p75 {v2[3*len(v2)//4]:.2f}; >=0.54: {sum(x>=0.54 for x in v2)/len(v2):.0%}')
  big=[x for x in out if x[2]<=-0.08 and not (x[1]<=2020<=x[1]+h)]
  vb=sorted(x[3] for x in big); print(f'   fall>=8% ex-covid n={len(vb)} median {st.median(vb):.2f}')
# pooled regression slope 3y change in $ (all sign), consumer disc
xs=[];ys=[]
for k in cd:
    d=P.get(k,{})
    for t in d:
        if t+3 in d: xs.append(d[t+3][0]-d[t][0]); ys.append(d[t+3][1]-d[t][1])
mx,my=st.mean(xs),st.mean(ys); b=sum((a-mx)*(c-my) for a,c in zip(xs,ys))/sum((a-mx)**2 for a in xs)
print('pooled 3y slope dOpInc on dSales (this panel, nominal $, unwinsorized):',round(b,3),'n',len(xs))
neg=[(a,c) for a,c in zip(xs,ys) if a<0]
mx,my=st.mean(a for a,_ in neg),st.mean(c for _,c in neg); b=sum((a-mx)*(c-my) for a,c in neg)/sum((a-mx)**2 for a,_ in neg)
print('slope using only sales-decline observations:',round(b,3),'n',len(neg))
