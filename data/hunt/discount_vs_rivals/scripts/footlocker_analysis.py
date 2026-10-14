import pandas as pd,numpy as np,re
d=pd.read_csv('footlocker_live_listings_20261014.csv')
d['q']=d.url.str.extract(r'/brands/([a-z-]+)\.html|/(?:mens|womens)/([a-z-]+)\.html').bfill(axis=1)[0]
d['disc']=d.price<d.orig-0.005; d['depth']=np.where(d.disc,1-d.price/d.orig,np.nan)
brandmap={'nike':'Nike','jordan':'Jordan','adidas':'adidas','hoka':'HOKA','on':'On','asics':'ASICS','new-balance':'New Balance','brooks':'Brooks','saucony':'Saucony','puma':'Puma','under-armour':'Under Armour','reebok':'Reebok'}
b=d[d.q.isin(brandmap)].drop_duplicates(['q','sku']).copy()
b['brand']=b.q.map(brandmap)
rng=np.random.default_rng(2)
def ci(x):
    x=x.values.astype(float); s=[x[rng.integers(0,len(x),len(x))].mean() for _ in range(2000)]; return np.percentile(s,[2.5,97.5])*100
rows=[]
for br,x in b.groupby('brand'):
    lo,hi=ci(x.disc); rows.append(dict(brand=br,n_skus=len(x),share_discounted=x.disc.mean()*100,ci_lo=lo,ci_hi=hi,mean_depth=x.depth.mean()*100,share_discounts_excluded=x.discExcl.mean()*100,brand_total_results_brandpage=int(d[(d.q==[k for k,v in brandmap.items() if v==br][0])&d.url.str.contains('/brands/')].total.iloc[0])))
r=pd.DataFrame(rows).round(1).sort_values('share_discounted');r.to_csv('footlocker_brand_discount_summary_20261014.csv',index=False);print(r.to_string())
# sale walls: brand mix of listed items
s=d[d.url.str.contains('/sale/')].copy()
def br(n):
    for k in ['Jordan','Nike','adidas','HOKA','On ','ASICS','New Balance','Brooks','Saucony','Puma','Under Armour','Reebok','Converse','Vans']:
        if n.startswith(k): return k.strip()
    return 'other'
s['brand']=s.name.map(br)
print(s.groupby(['url','brand']).size().unstack(0).fillna(0))
print(s.groupby('url').disc.mean())
