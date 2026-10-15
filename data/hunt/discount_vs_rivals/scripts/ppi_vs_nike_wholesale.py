import pandas as pd,numpy as np
d=pd.read_csv('ppi_margin_indexes_monthly.csv').set_index('date')
# Nike fiscal quarters: Q1 Jun-Aug, Q2 Sep-Nov, Q3 Dec-Feb, Q4 Mar-May.  Total wholesale growth (reported) from repo note nike_standing.md
q=[('Q1 FY25','2024-06','2024-08',-8),('Q2 FY25','2024-09','2024-11',-3),('Q3 FY25','2024-12','2025-02',-7),('Q4 FY25','2025-03','2025-05',-9),('Q1 FY26','2025-06','2025-08',7),('Q2 FY26','2025-09','2025-11',8),('Q3 FY26','2025-12','2026-02',5),('Q4 FY26','2026-03','2026-05',4),('Q1 FY27','2026-06','2026-08',-1)]
rows=[]
for n,a,b,w in q:
    s=d.loc[a:b]
    rows.append(dict(nike_qtr=n,months=f'{a}..{b}',nike_total_wholesale_growth_pct=w,shoe_stores_margin_idx=s['PCU448210448210'].mean(),clothing_stores_idx=s['PCU44814481'].mean(),sporting_goods_idx=s['PCU451110451110'].mean(),footwear_mfg_ppi=s['PCU316210316210'].mean()))
r=pd.DataFrame(rows)
for c in ['shoe_stores_margin_idx','clothing_stores_idx','sporting_goods_idx']:
    prev=[np.nan]*4+list(r[c][:-4]); r[c+'_yoy_pct']=(r[c]/prev-1)*100
r=r.round(1); r.to_csv('ppi_by_nike_fiscal_quarter.csv',index=False); print(r.to_string())
x=r.dropna(subset=['shoe_stores_margin_idx_yoy_pct'])
print('corr(level shoe idx, wholesale growth) all 9q:',round(np.corrcoef(r.shoe_stores_margin_idx,r.nike_total_wholesale_growth_pct)[0,1],2))
print('corr(level sporting goods idx, wholesale growth):',round(np.corrcoef(r.sporting_goods_idx,r.nike_total_wholesale_growth_pct)[0,1],2))
# z-score of the Jun-Aug 2026 YoY vs history of 3-month-avg YoY
s=d['PCU448210448210'].dropna(); m3=s.rolling(3).mean(); yoy=(m3/m3.shift(12)-1)*100
print('3m avg yoy now',round(yoy.iloc[-1],1),'sd of history',round(yoy.iloc[:-12].std(),1),'z',round(yoy.iloc[-1]/yoy.iloc[:-12].std(),1),'worst previous',round(yoy.iloc[:-12].min(),1),yoy.iloc[:-12].idxmin())
# months in last 3 years with index below prior 24m min
print((s.loc['2026-01':]).round(1).to_dict())
