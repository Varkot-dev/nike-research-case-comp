import pandas as pd,numpy as np,re
d=pd.read_csv('cc_intl_de_panel.csv'); d=d[d.status=='ok'].copy()
d['full']=d.full.astype(float);d['current']=d.current.astype(float)
d['date']=pd.to_datetime(d.ts.astype(str).str[:8]); d['ym']=d.date.dt.strftime('%Y-%m')
d['disc']=d.current<d.full-0.005; d['depth']=np.where(d.disc,1-d.current/d.full,np.nan)
foot=r'schuh|sneaker|stiefel|sandale|slides|badelatschen|latschen|boots|shoe|cleat|stollen|hallenschuh|pantolette|clog|trainer|runner|samba|gazelle|campus|spezial|ultraboost|adizero|pegasus|vomero|air-max|air-force|dunk|cortez|blazer|jordan-\d'
d['foot']=d.url.str.lower().str.contains(foot)&~d.url.str.lower().str.contains(r'socken|jacke|hose|shirt|short|top-|hoodie|trikot|tasche|rucksack|jersey|mütze|cap|bra')
rng=np.random.default_rng(3)
def bs(x,B=2000):
    x=x.values.astype(float); s=np.array([x[rng.integers(0,len(x),len(x))].mean() for _ in range(B)]); return s
rows=[]
for (c,b),g in d.groupby(['coll','brand']):
    for lab,gg in [('all',g),('footwear',g[g.foot])]:
        if len(gg)<30: continue
        s=bs(gg.disc); rows.append(dict(coll=c,month=gg.ym.mode()[0],brand=b,subset=lab,n=len(gg),share_disc=gg.disc.mean()*100,ci_lo=np.percentile(s,2.5)*100,ci_hi=np.percentile(s,97.5)*100,mean_depth=gg.depth.mean()*100))
r=pd.DataFrame(rows).round(1).sort_values(['subset','month','brand']); r.to_csv('intl_de_discount_by_crawl.csv',index=False); print(r.to_string())
# YoY difference-in-differences on matched months where all present
for lab,sub in [('all',d),('footwear',d[d.foot])]:
    for yrs in [(2025,2026),(2024,2026),(2024,2025)]:
        m=sub[sub.date.dt.month.isin([8,9])]
        a={b:{y:m[(m.brand==b)&(m.date.dt.year==y)].disc for y in yrs} for b in ['nike','adidas']}
        if any(len(a[b][y])<30 for b in a for y in yrs): continue
        dn=[bs(a['nike'][yrs[1]],1)[0]-bs(a['nike'][yrs[0]],1)[0]]
        res=[]
        for _ in range(2000):
            f=lambda s: s.values[rng.integers(0,len(s),len(s))].mean()
            res.append((f(a['nike'][yrs[1]])-f(a['nike'][yrs[0]]))-(f(a['adidas'][yrs[1]])-f(a['adidas'][yrs[0]])))
        dnk=a['nike'][yrs[1]].mean()-a['nike'][yrs[0]].mean(); dad=a['adidas'][yrs[1]].mean()-a['adidas'][yrs[0]].mean()
        print(lab,yrs,'Aug-Sep: Nike chg %.1f pts, adidas chg %.1f pts, DiD (Nike-adidas) %.1f pts CI %s'%(dnk*100,dad*100,(dnk-dad)*100,np.percentile(res,[2.5,97.5]).round(3)*100),'n',[len(a[b][y]) for b in a for y in yrs])
