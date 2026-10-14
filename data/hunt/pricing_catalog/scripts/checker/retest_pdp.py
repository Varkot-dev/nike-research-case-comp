# Checker: independent re-run of T1 and T2 with robustness variants (crawl-equal weights, category reweighting,
# within-URL matched pairs, apparel/footwear split, excluding fan gear, cluster bootstrap by crawl).
import pandas as pd, numpy as np
rng=np.random.default_rng(1)
d=pd.read_csv("pdp_panel_tidy.csv.gz"); d["date"]=pd.to_datetime(d.date); d["m"]=d.date.dt.month; d["y"]=d.date.dt.year
d["disc"]=d.disc.astype(float)
nk=d[d.brand=="nike"]
def boot_diff(a,b,B=4000):
    a=np.asarray(a,float); b=np.asarray(b,float)
    bs=rng.choice(b,(B,len(b))).mean(1)-rng.choice(a,(B,len(a))).mean(1); return np.percentile(bs,[2.5,97.5])
def win(df,y,ms): return df[(df.y==y)&(df.m.isin(ms))]
MS=range(3,10)
print("== T1 page-weighted ==")
for lab,sub in [("all",nk),("footwear",nk[nk["div"]=="footwear"]),("apparel_equip",nk[nk["div"]!="footwear"]),("nonfan",nk[nk.cat!="fan_gear"])]:
    a=win(sub,2025,MS).disc; b=win(sub,2026,MS).disc; lo,hi=boot_diff(a,b)
    print(lab,len(a),round(a.mean(),3),len(b),round(b.mean(),3),"diff",round(b.mean()-a.mean(),3),"CI",round(lo,3),round(hi,3))
print("== T1 crawl-month equal weights + cluster bootstrap over crawl-months ==")
def monthly(sub,y): return sub[(sub.y==y)&(sub.m.isin(MS))].groupby("m").disc.mean()
for lab,sub in [("all",nk),("footwear",nk[nk["div"]=="footwear"])]:
    a=monthly(sub,2025); b=monthly(sub,2026); diff=(b-a)
    print(lab,"2025",round(a.mean(),3),"2026",round(b.mean(),3),"mean month diff",round(diff.mean(),3),"months up",(diff>0).sum(),"of",len(diff), "t-ish SE",round(diff.std()/np.sqrt(len(diff)),3))
print("== T1 category-mix reweighted (2025 Mar-Sep category weights applied to 2026) ==")
a=win(nk,2025,MS); b=win(nk,2026,MS)
w25=a.cat.value_counts(normalize=True); w26=b.cat.value_counts(normalize=True)
print(pd.DataFrame({"w25":w25,"w26":w26}).round(3).to_string())
sh25=a.groupby("cat").disc.mean(); sh26=b.groupby("cat").disc.mean()
print("2026 at 2025 mix",round((sh26*w25).sum(),3),"2025 actual",round((sh25*w25).sum(),3))
print("== T1 within-URL matched (same URL seen in Mar-Sep 2025 and Mar-Sep 2026) ==")
ua=a.groupby("url").disc.mean(); ub=b.groupby("url").disc.mean(); j=pd.concat([ua,ub],axis=1,keys=["y25","y26"]).dropna()
print("n urls",len(j),"2025",round(j.y25.mean(),3),"2026",round(j.y26.mean(),3))
print("== Survivorship: share of pages whose style code first appears in panel >12m before capture ==")
for y in [2025,2026]:
    s=win(nk,y,MS); print(y,"old-prefix share",round((~s.fresh_pfx.astype(bool)).mean(),3),"disc fresh",round(s[s.fresh_pfx.astype(bool)].disc.mean(),3),"disc old",round(s[~s.fresh_pfx.astype(bool)].disc.mean(),3))
print("== Jul-Sep split ==")
for ms in [range(3,7),range(7,10)]:
    a=win(nk,2025,ms).disc;b=win(nk,2026,ms).disc;lo,hi=boot_diff(a,b);print(list(ms),round(a.mean(),3),round(b.mean(),3),round(b.mean()-a.mean(),3),round(lo,3),round(hi,3))
print("== T1 cluster bootstrap by crawl (Mar-Sep) ==")
def cb(sub,B=4000):
    out=[]
    A=[g.disc.values for _,g in win(sub,2025,MS).groupby("coll")]; Bc=[g.disc.values for _,g in win(sub,2026,MS).groupby("coll")]
    for _ in range(B):
        x=np.concatenate([A[i] for i in rng.integers(0,len(A),len(A))]); y=np.concatenate([Bc[i] for i in rng.integers(0,len(Bc),len(Bc))])
        out.append(y.mean()-x.mean())
    return np.percentile(out,[2.5,97.5])
print("all",cb(nk).round(3),"footwear",cb(nk[nk["div"]=="footwear"]).round(3))
print("== T2 DiD Aug-Sep, crawl cluster check ==")
W=d[d.window.isin(["AugSep2025","AugSep2026"])]
for b_ in ["nike","adidas"]:
    print(W[W.brand==b_].groupby(["window","coll"]).disc.agg(["size","mean"]).round(3).to_string())
# category-matched DiD: restrict both brands to footwear+apparel non-fan
for lab,sub in [("all",W),("nonfan",W[W.cat!="fan_gear"]),("footwear",W[W["div"]=="footwear"])]:
    g=sub.groupby(["brand","window"]).disc.mean().unstack(); dd=(g.AugSep2026-g.AugSep2025); print(lab,g.round(3).to_dict(),"DiD",round(dd.nike-dd.adidas,3))
# adidas Jun 2026 vs Aug-Sep 2026 (does adidas peak earlier?)
print(d[d.brand=="adidas"].groupby("coll").disc.mean().round(3).to_string())
