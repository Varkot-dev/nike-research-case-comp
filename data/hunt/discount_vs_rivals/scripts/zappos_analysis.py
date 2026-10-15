import pandas as pd,numpy as np
d=pd.read_csv('zappos_live_listings_20261014.csv')
num=lambda s: pd.to_numeric(s.astype(str).str.replace(r'[$,%]','',regex=True),errors='coerce')
d['price_n']=num(d.price);d['orig_n']=num(d.originalPrice);d['pct']=num(d.percentOff)
d=d[d.productType.eq('Shoes')|d.productType.isna()]
d['disc']=(d.pct>0)|(d.orig_n>d.price_n+0.005)
d['depth']=np.where(d.disc,1-d.price_n/d.orig_n,np.nan)
d['dedupe']=d.brand+'|'+d.productId.astype(str)+'|'+d.styleId.astype(str)
u=d.drop_duplicates('dedupe')
keep=['Nike','adidas','HOKA','On','ASICS','New Balance','Brooks','Saucony','PUMA','Under Armour','SKECHERS','Reebok']
u=u[u.brand.isin(keep)].copy()
u['cat']=u['dedupe'].map(d.groupby('dedupe')['query'].first()).str.split('-',n=1).str[1] if False else None
q=d.drop_duplicates('dedupe').set_index('dedupe')['query']
u['cat']=u.dedupe.map(q).str.replace(r'^(new-balance|under-armour|[a-z]+)-','',regex=True)
rng=np.random.default_rng(1)
def boot(x,B=2000):
    x=x.values.astype(float); s=[x[rng.integers(0,len(x),len(x))].mean() for _ in range(B)]; return np.percentile(s,[2.5,97.5])
rows=[]
for b in keep:
    x=u[u.brand==b]
    lo,hi=boot(x.disc)
    rows.append(dict(brand=b,n_styles=len(x),share_discounted=x.disc.mean()*100,ci_lo=lo*100,ci_hi=hi*100,mean_depth_pct=x.depth.mean()*100,median_depth_pct=x.depth.median()*100,avg_list_price=x.orig_n.mean(),price_weighted_disc_pct=(1-x.price_n.sum()/x.orig_n.sum())*100))
r=pd.DataFrame(rows).round(1); r.to_csv('zappos_brand_discount_summary_20261014.csv',index=False); print(r.to_string())
# running-shoes only
rr=u[u.cat.eq('running-shoes')]
rows=[]
for b in keep:
    x=rr[rr.brand==b]
    if len(x)<20: continue
    lo,hi=boot(x.disc)
    rows.append(dict(brand=b,n=len(x),share_discounted=x.disc.mean()*100,ci_lo=lo*100,ci_hi=hi*100,mean_depth=x.depth.mean()*100))
r2=pd.DataFrame(rows).round(1);r2.to_csv('zappos_running_discount_summary_20261014.csv',index=False);print(r2.to_string())
# Nike minus rival difference with bootstrap
for rival in ['adidas','HOKA','On','ASICS','New Balance','Brooks','Saucony']:
    a=u[u.brand=='Nike'].disc.values.astype(float);b=u[u.brand==rival].disc.values.astype(float)
    diff=[a[rng.integers(0,len(a),len(a))].mean()-b[rng.integers(0,len(b),len(b))].mean() for _ in range(2000)]
    print('Nike minus',rival,round((a.mean()-b.mean())*100,1),np.percentile(diff,[2.5,97.5]).round(3)*100)
u.to_csv('zappos_tidy_deduped_20261014.csv',index=False)
