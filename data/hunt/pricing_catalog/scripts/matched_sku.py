# Match style codes seen on nike.com product pages in Common Crawl (2024-2025) to today's live nike.com price list.
import pandas as pd, glob, numpy as np
live=pd.concat([pd.read_csv(f) for f in glob.glob("raw/api_live_20261014/api_w_*.csv")])
live=live[live.initialPrice>0].drop_duplicates("productCode")
live.to_csv("live_nikecom_union_catalog_20261014.csv.gz",index=False,compression="gzip")
p=pd.read_csv("pdp_panel_tidy.csv",low_memory=False); p=p[p.brand=="nike"]
p=p.dropna(subset=["style"]).sort_values("date").drop_duplicates(["coll","style"])
m=p.merge(live[["productCode","initialPrice","currentPrice","title","subTitle"]],left_on="style",right_on="productCode",how="left")
m["still_listed"]=m.productCode.notna()
m["live_disc"]=m.currentPrice<m.initialPrice-0.01
m["list_change_pct"]=100*(m.initialPrice/m.full-1)
out=[]
for w,g in m.groupby("window"):
    s=g[g.still_listed]
    out.append([w,len(g),g.still_listed.mean(),len(s),s.list_change_pct.median(),(s.list_change_pct>0.5).mean(),(s.list_change_pct<-0.5).mean(),g[~g.disc].shape[0],s[~s.disc].live_disc.mean(),s[s.disc].live_disc.mean()])
R=pd.DataFrame(out,columns=["window","n_seen","share_still_listed","n_matched","median_list_change_pct","share_list_up","share_list_down","n_fullprice_then","share_fullprice_then_now_disc","share_disc_then_now_disc"]).round(3)
print(R.to_string()); R.to_csv("matched_sku_then_vs_now.csv",index=False)
m.to_csv("matched_sku_rows.csv",index=False)
# list-price change by category for SKUs seen in Aug-Oct 2025
s=m[m.window.isin(["AugSep2025","Oct2025"])&m.still_listed]
print(s.groupby("cat").agg(n=("style","size"),med_list_change=("list_change_pct","median"),share_up=("list_change_pct",lambda x:(x>0.5).mean()),now_disc=("live_disc","mean")).round(3))
