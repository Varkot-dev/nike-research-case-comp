import pandas as pd, glob, os
D='raw/fred/'
ser=['PCU448210448210','PCU44824482','PCU44814481','PCU451110451110','PCU45114511','PCU451120451120','PCU448310448310','PCU441110441110','PCU445110445110','PCU316210316210']
# also pre-existing macro_category raw
df=None
for s in ser:
    p=D+s+'.csv'
    if not os.path.exists(p): continue
    x=pd.read_csv(p); x.columns=['date',s]; x[s]=pd.to_numeric(x[s],errors='coerce'); x['date']=x['date'].str[:7]
    df=x if df is None else df.merge(x,on='date',how='outer')
df=df.sort_values('date').reset_index(drop=True)
df.to_csv('ppi_margin_indexes_monthly.csv',index=False)
d=df.set_index('date')
rows=[]
for s in d.columns:
    v=d[s].dropna()
    if len(v)<30: continue
    last=v.index[-1]
    # Jun-Aug 2026 mean vs Jun-Aug 2025
    def m(a,b): 
        w=v[(v.index>=a)&(v.index<=b)]; return w.mean() if len(w)==3 else float('nan')
    cur=m('2026-06','2026-08'); prev=m('2025-06','2025-08'); two=m('2024-06','2024-08')
    pre=v[(v.index>='2018-01')&(v.index<='2019-12')].mean()
    pct=(v<v.iloc[-1]).mean()*100
    # 12m rolling mean level vs prior 12m
    l12=v.iloc[-12:].mean(); p12=v.iloc[-24:-12].mean()
    sd=v.pct_change(12).dropna().std()*100
    rows.append(dict(series=s,last=last,last_val=v.iloc[-1],first=v.index[0],JunAug26=cur,JunAug25=prev,JunAug24=two,yoy_JunAug_pct=(cur/prev-1)*100,twoyr_pct=(cur/two-1)*100,L12m_vs_P12m_pct=(l12/p12-1)*100,sd_yoy_pct=sd,pctile_of_last=pct,min_val=v.min(),min_date=v.idxmin()))
r=pd.DataFrame(rows).round(2); r.to_csv('ppi_decomposition_summary.csv',index=False); print(r.to_string())
# monthly detail 2024-2026 for the key ones
print(d.loc['2024-06':,['PCU448210448210','PCU44824482','PCU44814481','PCU451110451110','PCU45114511','PCU316210316210']].to_string())
