import pickle,collections,csv,statistics,sys
sys.path.insert(0,'/tmp/claude-0/-home-user-nike-research-case-comp/2bf9f309-3096-5c65-b9c3-02b984182743/scratchpad/scripts')
from lib import *
rows=pickle.load(open('rows.pkl','rb'))
by=collections.defaultdict(dict)
for r in rows: by[r['bond']][r['date']]=r
def sp(r): return float(r['z_spread_bp']) if r['z_spread_bp']!='' else r['i_spread_bp']
def at(b,d):
    ds=[x for x in by[b] if x<=d]; return by[b][max(ds)] if ds else None
OUT='/home/user/nike-research-case-comp/research_notes/Smoking gun hunt/'
# 1 implied rating table Oct 14
tot=oas('BAMLC0A0CM',dt.date(2026,10,14)) if False else None
OASd={k:load_oas(k) for k in ['BAMLC0A0CM']}
allc=OASd['BAMLC0A0CM'][dt.date(2026,10,13)]
snap=[]
print('allcorp OAS Oct13',allc)
for b in by:
    r=by[b].get('2026-10-14')
    if not r or r['ccy']!='USD' or r['years_left']<0.6: continue
    f=r['bucket_oas_bp']/allc
    AA=r['AA_oas_bp']*f; A=r['A_oas_bp']*f; BBB=r['BBB_oas_bp']*f
    z=sp(r); pos=(z-A)/(BBB-A)
    snap.append(dict(bond=b,issuer=r['issuer'],years=r['years_left'],price=r['clean_px'],ytm=r['ytm_pct'],z_bp=z,bucket_oas=r['bucket_oas_bp'],scaleF=round(f,2),AA_scaled=round(AA),A_scaled=round(A),BBB_scaled=round(BBB),pos_A0_BBB1=round(pos,2)))
    print(snap[-1])
with open(OUT+'G5_credit_market_snapshot_oct14.csv','w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=list(snap[0])); w.writeheader(); w.writerows(snap)
# 2 decomposition of yield change for Nike bonds
def dec(b,d0,d1='2026-10-14'):
    a,c=at(b,d0),at(b,d1)
    return round(c['ytm_pct']-a['ytm_pct'],3),round(c['benchmark_pct']-a['benchmark_pct'],3),round(c['i_spread_bp']-a['i_spread_bp'],1),round(sp(c)-sp(a),1),a['clean_px'],c['clean_px']
for b in ['NKE 2.85 Mar30','NKE 3.25 Mar40','NKE 3.875 Nov45','NKE 3.375 Mar50']:
    for d0 in ['2025-12-30','2026-06-30','2026-09-30','2024-09-30']:
        print(b,d0,'dYTM,dTSY,dI,dZ,px0,px1',dec(b,d0))
# 3 event window for all issuers: Sep30->Oct2, Oct2->Oct5, Oct5->Oct14 using I-spread
print('event windows I-spread/bp')
ev=[]
for b in by:
    if by[b].get('2026-10-14') is None or by[b]['2026-10-14']['years_left']<1: continue
    p=[at(b,d) for d in ['2026-09-30','2026-10-02','2026-10-05','2026-10-14']]
    if None in p: continue
    ev.append((b,[sp(x) for x in p]))
    print(b,[round(sp(x),1) for x in p],'tot',round(sp(p[3])-sp(p[0]),1))
with open(OUT+'G5_credit_market_event_window.csv','w',newline='') as fh:
    w=csv.writer(fh); w.writerow(['bond','spread_bp_Sep30','spread_bp_Oct2','spread_bp_Oct5','spread_bp_Oct14','chg_Sep30_Oct2','chg_Oct2_Oct5','chg_Oct5_Oct14','chg_total'])
    for b,s in ev: w.writerow([b]+[round(x,1) for x in s]+[round(s[1]-s[0],1),round(s[2]-s[1],1),round(s[3]-s[2],1),round(s[3]-s[0],1)])
# index changes
for k in ['BAMLC0A3CA','BAMLC0A4CBBB','BAMLC8A0C15PY','BAMLC3A0C57Y','BAMLC2A0C35Y','BAMLH0A1HYBB']:
    s=load_oas(k); print(k,[s.get(dt.date(2026,m,d)) for m,d in [(9,30),(10,2),(10,5),(10,13)]])
# 4 Prior-event placebo: Nike 2050 Z around prior S&P/Moody's actions
for lab,d0,d1 in [('Oct1 2024 guide withdrawal','2024-09-30','2024-10-15'),('Oct 2024 S&P outlook neg','2024-10-17','2024-10-31'),('Jul 2025 S&P A+','2025-07-14','2025-07-31'),('Nov12 2025 Moody A2','2025-11-10','2025-11-28'),('Dec 18 2025 Q2 FY26','2025-12-17','2025-12-30'),('Jun 26 2025 Q4FY25','2025-06-25','2025-07-11')]:
    for b in ['NKE 3.375 Mar50','NKE 2.85 Mar30']:
        a,c=at(b,d0),at(b,d1); print(lab,b,round(sp(a),1),'->',round(sp(c),1),'chg',round(sp(c)-sp(a),1),'bucket',a['bucket_oas_bp'],c['bucket_oas_bp'])
# 5 monthly CSV
with open(OUT+'G5_credit_market_monthly_spreads.csv','w',newline='') as fh:
    w=csv.writer(fh); w.writerow(['month_end_quote_date','bond','issuer','ccy','years_left','clean_px','ytm_pct','benchmark_pct','i_spread_bp','z_spread_bp','ice_bucket_oas_bp','ice_A_oas_bp','ice_BBB_oas_bp','ice_BB_oas_bp'])
    for b in by:
        me={}
        for d in sorted(by[b]): me[d[:7]]=by[b][d]
        for m,r in me.items(): w.writerow([r['date'],b,r['issuer'],r['ccy'],r['years_left'],r['clean_px'],r['ytm_pct'],r['benchmark_pct'],r['i_spread_bp'],r['z_spread_bp'],r['bucket_oas_bp'] if r['bucket_oas_bp'] is not None else '',r['A_oas_bp'] if r['A_oas_bp'] is not None else '',r['BBB_oas_bp'] if r['BBB_oas_bp'] is not None else '',r['BB_oas_bp'] if r['BB_oas_bp'] is not None else ''])
# 6 Nov 2026 note
r=by['NKE 2.375 Nov26']['2026-09-30']; print('Nov26 note', r['clean_px'], r['ytm_pct'])
