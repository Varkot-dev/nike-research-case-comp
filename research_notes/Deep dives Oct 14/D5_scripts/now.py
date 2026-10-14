import csv, statistics as st, numpy as np
C={r['ticker']:r for r in csv.DictReader(open('cur.csv'))}
P={r['ticker']:r for r in csv.DictReader(open('/home/user/nike-research-case-comp/research_notes/Thesis decision/dig_5_peer_pe_close_20261013.csv'))}
def f(x):
    try: return float(x)
    except: return None
peers=[t for t in C if t!='NKE']
pe2={t:f(P[t]['pe_fy2']) for t in P}; pe1={t:f(P[t]['pe_fy1']) for t in P}
m2=st.median([v for t,v in pe2.items() if t!='NKE' and v]); m1=st.median([v for t,v in pe1.items() if t!='NKE' and v])
print('Oct13 medians',m1,m2,'prem',pe2['NKE']/m2-1)
# today's intraday refresh
price={t:f(C[t]['price']) for t in C}
fx={'ADS.DE':1,'PUM.DE':1,'ONON':None,'2020.HK':None}
# metrics
rows=[]
for t in C:
    c=C[t]; e0,e1=f(c['eps0']),f(c['eps1']); r0,r1=f(c['rev0']),f(c['rev1'])
    g_rev=r1/r0-1 if r0 and r1 else None
    g_eps=e1/e0-1 if e0 and e1 and e0>0 else None
    fcfc=f(c['fcf'])/f(c['ni']) if f(c['ni']) and f(c['ni'])>0 and f(c['fcf']) else None
    rows.append(dict(ticker=t,pe_fy1=pe1[t],pe_fy2=pe2[t],rev_g_fy2=g_rev,eps_g_fy2=g_eps,peg=(pe2[t]/(g_eps*100) if pe2[t] and g_eps and g_eps>0 else None),opm=f(c['opm']),gm=f(c['gm']),roe=f(c['roe']),roa=f(c['roa']),fcf_conv=fcfc,ev_rev=f(c['ev_rev']),ev_ebitda=f(c['ev_ebitda']),beta=f(c['beta'])))
for r in rows: print({k:(round(v,3) if isinstance(v,float) else v) for k,v in r.items()})
pr=[r for r in rows if r['ticker']!='NKE']
def med(k): 
    v=[r[k] for r in pr if r[k] is not None and not (k=='ev_ebitda' and r[k]<0)]
    return st.median(v)
for k in ['rev_g_fy2','eps_g_fy2','peg','opm','gm','roe','roa','fcf_conv','ev_rev','ev_ebitda']:
    n=[r for r in rows if r['ticker']=='NKE'][0][k]; print(k,'NKE',round(n,3) if n else n,'peer med',round(med(k),3))
# correlations of pe_fy2 with metrics among peers (valid pe)
for k in ['rev_g_fy2','eps_g_fy2','opm','roe','roa','fcf_conv','gm']:
    xs=[(r[k],r['pe_fy2']) for r in pr if r[k] is not None and r['pe_fy2'] and r['ticker'] not in('PUM.DE',)]
    a=np.array(xs); print('corr pe_fy2 vs',k,len(a),round(np.corrcoef(a[:,0],a[:,1])[0,1],2))
# regression pe_fy2 on rev growth, ex PUM (NM)
xs=[(r['rev_g_fy2'],r['pe_fy2']) for r in pr if r['pe_fy2'] and r['ticker']!='PUM.DE' and r['ticker']!='7936.T']
a=np.array(xs); A=np.c_[np.ones(len(a)),a[:,0]]; b=np.linalg.lstsq(A,a[:,1],rcond=None)[0]; print('pe2 = %.1f + %.1f*rev_g ; Nike rev_g %.3f -> %.1f'%(b[0],b[1],rows[0]['rev_g_fy2'],b[0]+b[1]*rows[0]['rev_g_fy2']))
# midcycle
sh=1481.0; ni=50; tax=0.225; rev=43645
def eps(m,rev=rev): return ((rev*m)+ni)*(1-tax)/sh
px=35.33
print('calib 7.2%',eps(0.072),'cons 1.646')
for m in [0.072,0.083,0.10,0.118,0.127]:
    e=eps(m); print(m,round(e,2),'PE',round(px/e,1),'vs peer FY2 med 13.2 prem',round(px/e/13.2-1,3),'vs 15.8',round(px/e/m1-1,3))
rev31=rev*1.03**3
for m in [0.10,0.118,0.127]:
    e=eps(m,rev31); print('FY31 rev',round(rev31),m,round(e,2),'PE',round(px/e,1),'prem',round(px/e/13.2-1,3))
# breakeven margin for premium=0, 25%
for tgt in [0,0.25,0.63]:
    pe=13.2*(1+tgt); e=px/pe; m=((e*sh/(1-tax))-ni)/rev; print('premium',tgt,'needs EPS',round(e,2),'margin',round(m,4))
