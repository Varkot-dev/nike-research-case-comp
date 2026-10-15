# Summarise the live nike.com product-wall API pulls (2026-10-14) by wall: groupings, colourways, share discounted, depth.
import pandas as pd, glob
rows=[]
for f in sorted(glob.glob("raw/api_live_20261014/api_w*.csv*")):
    d=pd.read_csv(f); d=d[d.initialPrice>0]
    d=d.drop_duplicates("productCode")
    g=d.drop_duplicates("groupKey",keep="first")
    disc=d.currentPrice<d.initialPrice-0.01
    gd=g.currentPrice<g.initialPrice-0.01
    bs=d.featured.fillna("").str.contains("BEST_SELLER")
    nfl=d.subTitle.fillna("").str.contains("NFL|MLB|NBA|WNBA|College",regex=True)
    rows.append(dict(wall=(f.split("api_")[-1].replace(".csv.gz","").replace(".csv","").replace("w_","",1) if "api_w_" in f else "w"),groupings=len(g),colourways=len(d),
        share_colourways_disc=round(disc.mean(),3),share_lead_colourway_disc=round(gd.mean(),3),
        mean_depth_disc=round((1-d.currentPrice/d.initialPrice)[disc].mean(),3),
        listprice_weighted_disc_all=round((d.initialPrice-d.currentPrice).sum()/d.initialPrice.sum(),3),
        best_seller_colourways=int(bs.sum()),share_best_seller_disc=round(disc[bs].mean(),3),
        share_league_fan_colourways=round(nfl.mean(),3),share_nonfan_disc=round(disc[~nfl].mean(),3),
        mean_list_price=round(d.initialPrice.mean(),2)))
T=pd.DataFrame(rows); T.to_csv("live_nikecom_wall_summary_20261014.csv",index=False); print(T.to_string())
