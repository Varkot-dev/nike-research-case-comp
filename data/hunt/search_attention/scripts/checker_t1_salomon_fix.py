import pandas as pd, numpy as np, sys
d=pd.read_csv(sys.argv[1]+"/wiki_pageviews_daily_long.csv",parse_dates=["date"])
d=d[d.label!="salomon_oldtitle"]  # identical duplicate of salomon
d["brand"]=d.label.str.replace(r"_oldtitle\d*$","",regex=True)
daily=d.groupby(["brand","date"]).views.sum().unstack(0).fillna(0)
daily=daily[daily.index<="2026-10-12"]
N=["nike_inc","air_jordan"]
R=["adidas","new_balance","asics","puma","skechers","hoka","on_running","brooks","saucony","lululemon","salomon","under_armour","deckers","crocs"]
def sh(a,b,rr=R):
    x=daily.loc[a:b]; n=x[N].sum().sum(); r=x[rr].sum().sum(); return 100*n/(n+r)
for lab,(a1,b1,a0,b0) in {"Jun1-Oct11":("2026-06-01","2026-10-11","2025-06-01","2025-10-11"),"Aug1-Oct11":("2026-08-01","2026-10-11","2025-08-01","2025-10-11"),"Jan1-Oct11":("2026-01-01","2026-10-11","2025-01-01","2025-10-11"),"Sep1-Oct11":("2026-09-01","2026-10-11","2025-09-01","2025-10-11")}.items():
    print(lab, round(sh(a0,b0),2), round(sh(a1,b1),2), round(sh(a1,b1)-sh(a0,b0),2))
rob=[sh("2026-06-01","2026-10-11",[c for c in R if c!=r])-sh("2025-06-01","2025-10-11",[c for c in R if c!=r]) for r in R]
print("drop-one range",round(min(rob),2),round(max(rob),2))
# deckers starts 2023-09, on 2021-06: check coverage of the rival set
print(daily.loc["2025-06-01":"2025-10-11",R].sum().round(0).to_dict())
# Dunk/AF1 monthly
m=daily.resample("MS").sum()
print(m.loc["2022-06":"2026-09",["nike_dunk","air_force_1","air_jordan","nike_inc","adidas_samba"]].iloc[::3].to_string())
