"""Re-grade test for positioning_valuation_history (2026-10-14).
Conditions the hunt's insider-cluster and 13F-breadth event studies on depth of drawdown,
to see whether positioning signals separate outcomes for deeply fallen stocks like Nike.
Run from data/hunt/people_governance/: python3 scripts/regrade_positioning_conditional.py"""
import pandas as pd
c=pd.read_csv('insider_cluster_events.csv',parse_dates=['event_date'])
print('Insider clusters by prior 252d return threshold: n, med126, pos126, med252, pos252')
for th in [-30,-40,-50]:
    s=c[c.prior_252d_ret<=th]
    print(th,len(s),s.xs_126d.median(),f"{(s.xs_126d>0).sum()}/{s.xs_126d.count()}",s.xs_252d.median(),f"{(s.xs_252d>0).sum()}/{s.xs_252d.count()}")
b=pd.read_csv('breadth_event_panel.csv',parse_dates=['signal_date'])
p=pd.read_csv('prices_peers_2006_2026.csv',parse_dates=['date'])
dd={}
for t,g in p.groupby('ticker'):
    g=g.set_index('date').sort_index().close
    d=g/g.rolling(1260,min_periods=250).max()-1
    for i,r in b[b.ticker==t].iterrows():
        x=d[:r.signal_date]
        if len(x): dd[i]=x.iloc[-1]
b['dd']=pd.Series(dd); b=b.dropna(subset=['dd'])
print('Breadth panel rows with prices:',len(b))
for th in [-0.5,-0.6]:
    for rb in [None,-10]:
        x=b[b.dd<=th]
        if rb is not None: x=x[x.rel_breadth<=rb]
        for h in ['xs_126d','xs_252d']:
            y=x[h].dropna(); print(th,rb,h,len(y),round(y.median(),1),f"{(y>0).sum()}/{len(y)}",'cos',x.ticker.nunique())
