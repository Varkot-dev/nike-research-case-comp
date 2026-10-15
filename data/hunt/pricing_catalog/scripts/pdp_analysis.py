# Tidy the Common Crawl PDP panels (nike.com and adidas.com) and compute discount incidence by period, category and product vintage.
import pandas as pd, numpy as np, sys, os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from classify import category
rng=np.random.default_rng(0)
import glob
def load(fn,brand):
    d=pd.concat([pd.read_csv(f) for f in sorted(glob.glob(fn.replace(".csv","*.csv")))],ignore_index=True); d=d[d.status=="ok"].copy()
    d["brand"]=brand
    d[["cat","div"]]=d.url.apply(lambda u: pd.Series(category(u,brand)))
    d["date"]=pd.to_datetime(d.ts.astype(str).str[:8])
    d["disc"]=(d.current<d.full-0.01)
    d["depth"]=np.where(d.disc,1-d.current/d.full,np.nan)
    d=d.drop_duplicates(["coll","url"])
    return d
n=load("cc_pdp_panel_nike.csv","nike"); a=load("cc_pdp_panel_adidas.csv","adidas")
# vintage for Nike: first crawl in which each 2-letter style prefix appears anywhere in the panel
n["pfx"]=n["style"].astype(str).str[:2]
first=n.groupby("pfx").date.min()
n["pfx_first"]=n.pfx.map(first)
n["rel"]=pd.to_datetime(n.release_date,errors="coerce")
n["age_m_release"]=(n.date-n.rel).dt.days/30.4
n["fresh_pfx"]=(n.date-n.pfx_first).dt.days<=365
d=pd.concat([n,a],ignore_index=True)
win={"CC-MAIN-2024-33":"AugSep2024","CC-MAIN-2024-38":"AugSep2024","CC-MAIN-2025-33":"AugSep2025","CC-MAIN-2025-38":"AugSep2025","CC-MAIN-2026-34":"AugSep2026","CC-MAIN-2026-39":"AugSep2026",
     "CC-MAIN-2024-42":"Oct2024","CC-MAIN-2025-43":"Oct2025"}
d["window"]=d.coll.map(win)
d["half"]=d.date.dt.year.astype(str)+np.where(d.date.dt.month<=6,"H1","H2")
d.to_csv("pdp_panel_tidy.csv.gz",index=False)
def boot(s,B=2000):
    s=np.asarray(s,float)
    if len(s)==0: return (np.nan,np.nan)
    m=rng.choice(s,(B,len(s))).mean(1); return np.percentile(m,[2.5,97.5])
rows=[]
for (b,h),g in d.groupby(["brand","half"]):
    lo,hi=boot(g.disc)
    rows.append([b,h,len(g),g.disc.mean(),lo,hi,g.depth.mean()])
T=pd.DataFrame(rows,columns=["brand","half","n","share_disc","ci_lo","ci_hi","mean_depth_disc"]).round(3)
T.to_csv("pdp_share_by_half.csv",index=False); print(T.to_string())
c=d[d.brand=="nike"].pivot_table(index="half",columns="cat",values="disc",aggfunc=["mean","size"]).round(2)
print(c.to_string())
c.to_csv("pdp_nike_share_by_half_category.csv")
# per-crawl series (Nike and adidas), all items and footwear only
S=d.groupby(["brand","coll"]).agg(date=("date","median"),n=("disc","size"),share=("disc","mean"),depth=("depth","mean")); S[["share","depth"]]=S[["share","depth"]].round(3)
Sf=d[d["div"]=="footwear"].groupby(["brand","coll"]).agg(n_fw=("disc","size"),share_fw=("disc","mean")).round(3)
Snf=d[d["cat"]!="fan_gear"].groupby(["brand","coll"]).agg(n_nonfan=("disc","size"),share_nonfan=("disc","mean")).round(3)
S=S.join(Sf).join(Snf); S.to_csv("pdp_share_by_crawl.csv"); print(S.to_string())
# same-calendar-window YoY
w=d[d.window.notna()]
G=w.groupby(["brand","window"]).agg(n=("disc","size"),share=("disc","mean"),depth=("depth","mean")).round(3); print(G)
G.to_csv("pdp_share_by_window.csv")
Gc=w[w.brand=="nike"].pivot_table(index="cat",columns="window",values="disc",aggfunc=["mean","size"]).round(3); print(Gc.to_string())
Gc.to_csv("pdp_nike_window_by_category.csv")
Gf=w[w.brand=="nike"].pivot_table(index="fresh_pfx",columns="window",values="disc",aggfunc=["mean","size"]).round(3); print(Gf.to_string())
Gd=w.pivot_table(index=["brand","div"],columns="window",values="disc",aggfunc=["mean","size"]).round(3); print(Gd.to_string())
# difference in differences AugSep2025 -> AugSep2026, Nike minus adidas, bootstrap
def did(sub):
    x=sub
    def m(b,wd): return x[(x.brand==b)&(x.window==wd)].disc.values.astype(float)
    n25,n26,a25,a26=m("nike","AugSep2025"),m("nike","AugSep2026"),m("adidas","AugSep2025"),m("adidas","AugSep2026")
    est=(n26.mean()-n25.mean())-(a26.mean()-a25.mean())
    bs=[(rng.choice(n26,len(n26)).mean()-rng.choice(n25,len(n25)).mean())-(rng.choice(a26,len(a26)).mean()-rng.choice(a25,len(a25)).mean()) for _ in range(2000)]
    return est,np.percentile(bs,[2.5,97.5]),n26.mean()-n25.mean(),a26.mean()-a25.mean()
# adidas category windows
Ga=w[w.brand=="adidas"].pivot_table(index="cat",columns="window",values="disc",aggfunc=["mean","size"]).round(3); print(Ga.to_string()); Ga.to_csv("pdp_adidas_window_by_category.csv")
print("DiD all:",did(w))
print("DiD footwear:",did(w[w["div"]=="footwear"]))
print("DiD non-fan:",did(w[w["cat"]!="fan_gear"]))

# month-matched YoY (calendar month of crawl), Nike only
nk=d[d.brand=="nike"].copy(); nk["ym"]=nk.date.dt.to_period("M")
M=nk.groupby("ym").agg(n=("disc","size"),share=("disc","mean"),share_fw=("disc",lambda x: x[nk.loc[x.index,"div"]=="footwear"].mean()))
M.index=M.index.astype(str); M=M.round(3); M.to_csv("pdp_nike_monthly.csv"); 
rows=[]
for ym in M.index:
    y,mo=ym.split("-"); prev=f"{int(y)-1}-{mo}"
    if prev in M.index: rows.append([ym,prev,M.loc[ym,"n"],M.loc[prev,"n"],M.loc[ym,"share"],M.loc[prev,"share"],round(M.loc[ym,"share"]-M.loc[prev,"share"],3),M.loc[ym,"share_fw"],M.loc[prev,"share_fw"]])
Y=pd.DataFrame(rows,columns=["month","prior_year_month","n","n_prior","share","share_prior","yoy_pts","share_fw","share_fw_prior"]); print(Y.to_string()); Y.to_csv("pdp_nike_month_yoy.csv",index=False)
