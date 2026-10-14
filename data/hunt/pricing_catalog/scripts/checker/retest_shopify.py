# Checker: re-run T4 with (a) created_at instead of published_at for age, (b) 0-3m vs 0-6m fresh windows,
# (c) stricter running classifier (word-boundary model names, no colour words like 'Cloud White'),
# (d) excluding unreleased (future-dated / not_released) items, (e) brand-level LPM with store FE, store-clustered SE.
import pandas as pd, numpy as np, re
t=pd.read_csv("shopify_tidy_brand_products_20261014.csv.gz",low_memory=False)
x=t[t.avail & t.footwear & t.store.ne("www.playmakers.com")].copy()
x["created"]=pd.to_datetime(x.created_at,utc=True,errors="coerce")
x["age_c"]=(pd.Timestamp("2026-10-14",tz="UTC")-x.created).dt.days
x["unrel"]=x.tags.fillna("").str.contains("not_released")|(x.age_days<0)
print("unreleased rows",x.unrel.sum(),"of",len(x)); print("published vs created gap>30d share",((x.age_c-x.age_days)>30).mean().round(3))
for lab,col,hi in [("pub 0-3m",'age_days',90),("pub 0-6m",'age_days',180),("created 0-3m",'age_c',90),("created 0-6m",'age_c',180)]:
    f=x[(x[col]>=0)&(x[col]<=hi)&~x.unrel]
    g=f.groupby("brand").md10.agg(["mean","size"]).round(3)
    print(lab, g.loc[["Nike","Jordan","adidas","New Balance","On","HOKA","ASICS"]].to_dict("index"))
def lpm(x,agecol):
    x=x[(x[agecol]>=0)&~x.unrel].copy()
    x["ab"]=pd.cut(x[agecol],[-1,90,180,365,730,100000]).astype(str)
    X=pd.get_dummies(x[["brand","store","ab"]].astype(str)).astype(float)
    X=X.drop(columns=["brand_adidas",[c for c in X if c.startswith("store_")][0],[c for c in X if c.startswith("ab_")][0]]); X.insert(0,"const",1.0)
    y=x.md10.astype(float).values; A=X.values; b=np.linalg.lstsq(A,y,rcond=None)[0]; e=y-A@b
    Xi=np.linalg.pinv(A.T@A); M=np.zeros((A.shape[1],)*2)
    for _,ix in x.reset_index().groupby("store").groups.items(): g=A[ix].T@e[ix]; M+=np.outer(g,g)
    G=x.store.nunique(); N,K=A.shape; c=G/(G-1)*(N-1)/(N-K)
    se=np.sqrt(np.diag(c*Xi@M@Xi)); o=pd.Series(b,X.columns); s=pd.Series(se,X.columns)
    return {k:(round(o[k],3),round(s[k],3)) for k in ["brand_Nike","brand_Jordan","brand_On","brand_HOKA","brand_New Balance"]}
print("LPM pub-age, small-sample corrected:",lpm(x,"age_days"))
print("LPM created-age:",lpm(x,"age_c"))
# within-store Nike minus adidas for fresh created 0-6m, stores with >=20 of each
f=x[(x.age_c<=180)&(x.age_c>=0)&~x.unrel]
pv=f[f.brand.isin(["Nike","adidas"])].groupby(["store","brand"]).md10.agg(["mean","size"]).unstack()
ok=pv[(pv["size"]["Nike"]>=20)&(pv["size"]["adidas"]>=20)]
diff=(ok["mean"]["Nike"]-ok["mean"]["adidas"]); print("within-store fresh Nike-adidas:",diff.round(3).to_dict(),"stores Nike higher",(diff>0).sum(),"of",len(diff))
# running classifier check
txt=(x.product_type.fillna("")+" "+x.title.fillna("")+" "+x.tags.fillna("")).str.lower()
old=txt.str.contains("running|pegasus|vomero|structure|invincible|clifton|bondi|ghost|novablast|gel-|kayano|nimbus|1080|880|cloud|adizero|ultraboost|supernova|endorphin|ride|triumph|speedgoat|mach")
tl=x.title.fillna("").str.lower(); ty=x.product_type.fillna("").str.lower()
new=ty.str.contains(r"\brunning\b")|tl.str.contains(r"\b(?:pegasus|vomero|structure|invincible|zoomx|alphafly|vaporfly|clifton|bondi|mach \d|speedgoat|arahi|novablast|gel-kayano|gel-nimbus|kayano|nimbus|gt-2000|fresh foam|1080|880|rebel v|fuelcell|cloudmonster|cloudsurfer|cloudrunner|cloudflow|cloudboom|cloudeclipse|cloudswift|cloud 6|adizero|ultraboost|supernova|endorphin|ride 1\d|triumph|guide 1\d|ghost 1\d|glycerin|adrenaline|hyperion|running)\b")
x["run_old"]=old; x["run_new"]=new
print("classified running old vs new by brand:"); print(x.groupby("brand")[["run_old","run_new"]].sum().to_string())
print("adidas old-running titles with 'cloud' but not new:",x[(x.brand=="adidas")&old&~new].title.head(8).tolist())
print("Nike old-running not new:",x[(x.brand=="Nike")&old&~new].title.head(8).tolist())
R=x[new].groupby("brand").md10.agg(["mean","size"]).round(3); print("running (strict):"); print(R.to_string())
R2=x[new&~x.store.isin(["pacersrunning.com"])].groupby("brand").md10.agg(["mean","size"]).round(3); print("running strict ex Pacers:");print(R2.to_string())
print("running strict by store, Nike vs others:"); print(x[new&x.brand.isin(["Nike","HOKA","On","ASICS","Brooks","adidas","New Balance"])].pivot_table(index="store",columns="brand",values="md10",aggfunc="mean").round(2).to_string())
