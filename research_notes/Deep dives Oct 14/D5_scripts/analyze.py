import csv, statistics as st, math
R=list(csv.DictReader(open('monthly.csv')))
def fl(x): return float(x) if x not in('',None) else None
import hist
FY=hist.FY['NKE']
print('NKE FY: fye eps clean opm growth')
prev=None
for r in FY:
    opm=r['op']/r['rev']; g=(r['rev']/prev-1) if prev else None; prev=r['rev']
    print(r['fye'],round(r['eps'],3),round(r['eps_clean'],3),round(opm,4),None if g is None else round(g,3))
def stats(rows,k):
    v=[fl(r[k]) for r in rows if fl(r[k]) is not None]
    return (len(v),round(st.median(v),3),round(min(v),3),round(max(v),3)) if v else None
keys=['prem_pe_trail','prem_pe_ntm_clean','prem_pe_ntm','prem_evs_trail','prem_evs_ntm','prem_eve_ntm','prem_eve_trail']
wins={'all 2009-07..2026-06':('2009-07-01','2026-06-30'),'GFC trough 2008-10..2009-06':('2008-10-01','2009-06-30'),'2010-2012':('2010-01-01','2012-12-31'),'2013':('2013-01-01','2013-12-31'),'2014-2016':('2014-01-01','2016-12-31'),'FY17-FY19 margin trough 2017-06..2019-06':('2017-06-01','2019-06-30'),'COVID 2020-03..2020-12':('2020-03-01','2020-12-31'),'2022-07..2023-12':('2022-07-01','2023-12-31'),'2024-07..2025-12':('2024-07-01','2025-12-31')}
for w,(a,b) in wins.items():
    rr=[r for r in R if a<=r['date']<=b]
    print(w,{k:stats(rr,k) for k in keys})
import numpy as np
ye=[r for r in R if r['date'][5:7] in('12','06')]
X=[];Y=[]
for r in ye:
    if fl(r['prem_pe_ntm_clean']) is not None and r['nke_opm_last'] and r['peer_med_opm_last'] and r['nke_rev_growth_last']:
        X.append([1,fl(r['nke_opm_last'])-fl(r['peer_med_opm_last']),fl(r['nke_rev_growth_last'])]);Y.append(fl(r['prem_pe_ntm_clean']))
X=np.array(X);Y=np.array(Y)
b=np.linalg.lstsq(X,Y,rcond=None)[0]; res=Y-X@b; print('regress prem_ntm_clean on opm gap, growth: n',len(Y),b,1-res.var()/Y.var())
Xe=[];Ye=[]
for r in ye:
    if fl(r['prem_evs_trail']) is not None and r['nke_opm_last']:
        Xe.append([1,fl(r['nke_opm_last'])-fl(r['peer_med_opm_last'])]);Ye.append(fl(r['prem_evs_trail']))
Xe=np.array(Xe);Ye=np.array(Ye);be=np.linalg.lstsq(Xe,Ye,rcond=None)[0];print('EVS prem on opm gap',len(Ye),be,'corr',np.corrcoef(Xe[:,1],Ye)[0,1])
for a,b_ in [('2010-01-01','2019-12-31'),('2009-07-01','2026-06-30')]:
    v=[fl(r['peer_med_pe_ntm_clean']) for r in R if a<=r['date']<=b_ and fl(r['peer_med_pe_ntm_clean'])]
    n=[fl(r['nke_pe_ntm_clean']) for r in R if a<=r['date']<=b_ and fl(r['nke_pe_ntm_clean'])]
    print(a,b_,'peer med NTM',round(st.median(v),1),'nke NTM',round(st.median(n),1))
for d in ['2008-12-31','2009-03-31','2009-06-30','2010-06-30','2010-09-30','2013-06-30','2013-12-31','2017-06-30','2018-03-31','2018-06-30','2019-06-30','2020-03-31','2020-06-30','2022-09-30','2023-12-31','2024-06-30','2025-06-30','2026-06-30']:
    r=[x for x in R if x['date']==d]
    if r:
        r=r[0]; print(d,{k:r[k] for k in ['nke_price','nke_pe_trail','peer_med_pe_trail','prem_pe_trail','nke_pe_ntm_clean','peer_med_pe_ntm_clean','prem_pe_ntm_clean','nke_pe_ntm','prem_pe_ntm','nke_evs_trail','peer_med_evs_trail','prem_evs_trail','prem_eve_ntm','nke_opm_last','nke_roic_last','peer_med_roic_last','nke_fcf_conv','peer_med_fcf_conv']})
