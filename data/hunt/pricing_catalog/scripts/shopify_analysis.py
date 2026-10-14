# Tidy the Shopify retailer catalogs and test Nike vs peer markdown rates with store and product-age controls.
import pandas as pd, numpy as np, re, sys
d=pd.read_csv("shopify_products_20261014.csv.gz",low_memory=False)
d=d.drop_duplicates(["store","product_id"])
v=d.vendor.astype(str).str.lower().str.strip()
def brand(x):
    if "jordan craig" in x: return None
    if x.startswith("jordan") or x in ("air jordan","nike jordan"): return "Jordan"
    if x.startswith("nike"): return "Nike"
    if x.startswith("adidas"): return "adidas"
    m={"new balance":"New Balance","asics":"ASICS","hoka":"HOKA","hoka one one":"HOKA","on":"On","on running":"On","puma":"Puma","saucony":"Saucony","salomon":"Salomon","brooks":"Brooks","converse":"Converse","vans":"Vans","reebok":"Reebok"}
    return m.get(x)
d["brand"]=v.map(brand)
pt=(d.product_type.fillna("")+" "+d.title.fillna("")).str.lower()
d["footwear"]=pt.str.contains(r"footwear|sneaker|shoe|basketball|lifestyle|running|true retro|casual|quickstrike|boot|sandal|slide|low top|mid top|high top|neutral|stability|flats|trail|clog|mule|cleat")
d["avail"]=d.n_avail>0
d["md10"]=d.disc_pct_max>=10
d["md_any"]=d.n_var_disc>0
d["pub"]=pd.to_datetime(d.published_at.fillna(d.created_at),utc=True,errors="coerce")
d["age_days"]=(pd.Timestamp("2026-10-14",tz="UTC")-d.pub).dt.days
d["age_bucket"]=pd.cut(d.age_days,[-1,90,180,365,730,10000],labels=["0-3m","3-6m","6-12m","1-2y","2y+"])
d["family"]=d.brand.replace({"Jordan":"Nike Inc","Nike":"Nike Inc","Converse":"Nike Inc"})
t=d[d.brand.notna()].copy()
t.to_csv("shopify_tidy_brand_products_20261014.csv.gz",index=False)
x=t[t.avail & t.footwear & t.store.ne("www.playmakers.com")]
print("available footwear rows by brand:"); print(x.brand.value_counts())
print("\nmarkdown>=10% share by brand x age bucket (pooled stores)")
print(x.pivot_table(index="brand",columns="age_bucket",values="md10",aggfunc="mean",observed=False).round(3).to_string())
print(x.pivot_table(index="brand",columns="age_bucket",values="md10",aggfunc="size",observed=False).to_string())
# linear probability model: md10 ~ brand + store FE + age bucket FE
import itertools
X=pd.get_dummies(x[["brand","store","age_bucket"]].astype(str),drop_first=False)
base_cols=[c for c in X.columns if c not in("brand_adidas",) and not c.startswith("store_www.dtlr") and not c.startswith("age_bucket_0-3m")]
X=X[base_cols].astype(float); X.insert(0,"const",1.0)
y=x.md10.astype(float).values
beta,res,rk,sv=np.linalg.lstsq(X.values,y,rcond=None)
resid=y-X.values@beta
# cluster-robust (by store) standard errors
XtX_inv=np.linalg.pinv(X.values.T@X.values)
meat=np.zeros((X.shape[1],X.shape[1]))
for s,idx in x.reset_index().groupby("store").groups.items():
    g=X.values[idx].T@resid[idx]; meat+=np.outer(g,g)
V=XtX_inv@meat@XtX_inv; se=np.sqrt(np.diag(V))
out=pd.DataFrame({"coef_vs_adidas":beta,"se_cluster_store":se},index=X.columns)
print("\nLPM coefficients (brand effects relative to adidas, store and age FE):")
print(out[out.index.str.startswith("brand_")].round(3).to_string())
out.to_csv("shopify_lpm_markdown10_brand_effects.csv")
# fresh product only (<=180 days)
f=x[x.age_days<=180]
print("\nFresh (<=180d) markdown>=10% by brand, pooled and store-avg:")
pv=f.pivot_table(index="store",columns="brand",values="md10",aggfunc="mean")
print(f.groupby("brand").md10.agg(["mean","size"]).round(3).to_string())
sub=f[f.brand.isin(["Nike","Jordan","adidas","New Balance","ASICS"])]
pv=sub.pivot_table(index="store",columns="brand",values="md10",aggfunc="mean").round(2)
print(pv.to_string())
pv.to_csv("shopify_fresh_markdown_by_store_brand.csv")
# running shoes only
pt=(x.product_type.fillna("")+" "+x.title.fillna("")+" "+x.tags.fillna("")).str.lower()
r=x[pt.str.contains("running|pegasus|vomero|structure|invincible|clifton|bondi|ghost|novablast|gel-|kayano|nimbus|1080|880|cloud|adizero|ultraboost|supernova|endorphin|ride|triumph|speedgoat|mach")]
R=r.groupby("brand").agg(n=("md10","size"),md10=("md10","mean"),fresh_md10=("md10",lambda s: s[r.loc[s.index,"age_days"]<=180].mean())).round(3)
print("\nRunning shoes only:"); print(R.to_string()); R.to_csv("shopify_running_markdown_by_brand.csv")
P=r[r.store=="pacersrunning.com"].groupby("brand").md10.agg(["mean","size"]).round(3); print(P.to_string()); P.to_csv("shopify_pacers_running_markdown_by_brand.csv")
