"""Checker re-run (2026-10-14): balanced-panel and athletic-only versions of T1, plus T2 recompute.
Run: python3 -I scripts/20_checker_robustness.py"""
import pandas as pd
B='/home/user/nike-research-case-comp/data/hunt/peers_reported/'
g=pd.read_csv(B+'panel_growth_comparable.csv')
dom=['ANTA','FILA','Li Ning','Xtep']
for reg,nk in [('North America','Nike NA'),('Europe/EMEA','Nike EMEA'),('Greater China','Nike Greater China')]:
    p=g[g.region==reg].pivot_table(index=['cal_year','cal_q'],columns='series',values='growth_pct').loc[(2025,1):(2026,2)]
    n=p.pop(nk); bal=p.dropna(axis=1); bal=bal[[c for c in bal.columns if not any(k in c for k in dom)]]
    gap=n-bal.median(axis=1)
    print(reg,'balanced peers',list(bal.columns),'gaps',gap.round(1).tolist(),'last2',round(gap.iloc[4:].mean(),2),'prev4',round(gap.iloc[:4].mean(),2))
na=g[g.region=='North America'].pivot_table(index=['cal_year','cal_q'],columns='series',values='growth_pct')
nike=na.pop('Nike NA')
athl=['ASICS NA','Amer Americas','On Americas','adidas NA','Puma Americas','Under Armour NA','Deckers US']
gap=(nike-na[athl].median(axis=1))
print('NA athletic-only gap last2',round(gap.loc[[(2026,1),(2026,2)]].mean(),2),'prev4',round(gap.loc[(2025,1):(2025,4)].mean(),2))
gs=(nike.shift(-1)-na.median(axis=1)).loc[(2025,1):(2026,2)]
print('NA Nike-shifted-one-quarter gap last2',round(gs.iloc[4:].mean(),2),'prev4',round(gs.iloc[:4].mean(),2))
c=pd.read_csv(B+'panel_company_quarterly.csv')
l=c[c.inv_minus_sales_pp.notna()&((c.cal_year*10+c.cal_q)>=20253)].groupby('company').tail(2)
s=l.groupby('company').inv_minus_sales_pp.mean()
print('T2 Nike',round(s['nike'],2),'peer median',round(s.drop('nike').median(),2),'rank from top',int((s>s['nike']).sum())+1,'of',len(s))
