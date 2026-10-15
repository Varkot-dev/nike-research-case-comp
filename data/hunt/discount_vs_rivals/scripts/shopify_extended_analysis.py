# Same method as pricing_catalog/scripts/shopify_analysis.py, run on the original 16 stores plus the new partner stores pulled in this hunt.
import pandas as pd, numpy as np
old=pd.read_csv("../pricing_catalog/shopify_products_20261014.csv.gz",low_memory=False)
new=pd.read_csv("shopify_new_stores_20261014.csv.gz",low_memory=False)
old['grp']='orig16'; new['grp']='new'
d=pd.concat([old,new]).drop_duplicates(["store","product_id"])
v=d.vendor.astype(str).str.lower().str.strip()
def brand(x):
    if "jordan craig" in x: return None
    if x.startswith("jordan") or x in ("air jordan","nike jordan"): return "Jordan"
    if x.startswith("nike"): return "Nike"
    if x.startswith("adidas") or x=="adidas-y3": return "adidas"
    m={"new balance":"New Balance","asics":"ASICS","hoka":"HOKA","hoka one one":"HOKA","on":"On","on running":"On","on shoes":"On","puma":"Puma","saucony":"Saucony","salomon":"Salomon","brooks":"Brooks","converse":"Converse","vans":"Vans","reebok":"Reebok"}
    return m.get(x)
d["brand"]=v.map(brand)
pt=(d.product_type.fillna("")+" "+d.title.fillna("")).str.lower()
d["footwear"]=pt.str.contains(r"footwear|sneaker|shoe|basketball|lifestyle|running|true retro|casual|quickstrike|boot|sandal|slide|low top|mid top|high top|neutral|stability|flats|trail|clog|mule|cleat")
d["avail"]=d.n_avail>0; d["md10"]=d.disc_pct_max>=10
d["pub"]=pd.to_datetime(d.published_at.fillna(d.created_at),utc=True,errors="coerce")
d["age_days"]=(pd.Timestamp("2026-10-14",tz="UTC")-d.pub).dt.days
d["age_bucket"]=pd.cut(d.age_days,[-1,90,180,365,730,10000],labels=["0-3m","3-6m","6-12m","1-2y","2y+"])
t=d[d.brand.notna()&d.avail&d.footwear&d.store.ne("www.playmakers.com")].copy()
print(t.groupby(['grp','brand']).size().unstack(0).fillna(0).astype(int))
print(t.groupby('store').brand.value_counts().unstack().fillna(0).astype(int).to_string())
def lpm(x,label):
    X=pd.get_dummies(x[["brand","store","age_bucket"]].astype(str)); keep=[c for c in X.columns if c!="brand_adidas" and not c.endswith("_0-3m") and c!=X.columns[[c.startswith("store_") for c in X.columns].index(True)]]
    X=X[keep].astype(float); X.insert(0,"const",1.0); y=x.md10.astype(float).values
    b=np.linalg.lstsq(X.values,y,rcond=None)[0]; r=y-X.values@b
    inv=np.linalg.pinv(X.values.T@X.values); meat=np.zeros((X.shape[1],)*2)
    xr=x.reset_index(drop=True)
    for s,idx in xr.groupby("store").groups.items():
        g=X.values[list(idx)].T@r[list(idx)]; meat+=np.outer(g,g)
    V=inv@meat@inv; se=np.sqrt(np.diag(V))
    o=pd.DataFrame({"coef_vs_adidas":b,"se_cluster_store":se,"set":label},index=X.columns); return o[o.index.str.startswith("brand_")]
res=pd.concat([lpm(t,'all stores'),lpm(t[t.grp=='new'],'new stores only')])
res['n_stores']=np.where(res.set=='all stores',t.store.nunique(),t[t.grp=='new'].store.nunique())
print(res.round(3).to_string()); res.round(4).to_csv("shopify_extended_lpm_brand_effects.csv")
# raw shares for the brands of interest, all and fresh
cmp=t[t.brand.isin(["Nike","Jordan","adidas","HOKA","On","ASICS","New Balance"])]
tab=cmp.groupby("brand").agg(n=("md10","size"),md10=("md10","mean")).round(3)
tab['fresh_le180d_md10']=cmp[cmp.age_days<=180].groupby("brand").md10.mean().round(3); tab['n_fresh']=cmp[cmp.age_days<=180].groupby("brand").size()
print(tab.to_string()); tab.to_csv("shopify_extended_markdown_by_brand.csv")
pv=cmp.pivot_table(index="store",columns="brand",values="md10",aggfunc="mean").round(2); pv.to_csv("shopify_extended_md10_by_store_brand.csv"); print(pv.to_string())
