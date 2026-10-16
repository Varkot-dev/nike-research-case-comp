"""W5 nowcast model. Run after build_panel.py: python3 -I model.py"""
import csv,os,json
D=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
psq={r['nike_fiscal_quarter']:float(r['yoy_pct']) for r in csv.DictReader(open(D+'/pousheng_nike_fiscal_quarters.csv'))}
# Nike Greater China (10-Q/10-K via data/nike_channel_split.csv; cc from earnings calls, OPENED repo transcripts)
nk={ # total, direct, wholesale USD m ; prior-year same quarter ; cc growth pct
'Q2FY2025':(1711,807,904,1863,836,1027,-11),'Q3FY2025':(1733,738,995,2084,841,1243,-15),'Q4FY2025':(1476,647,829,1863,766,1097,-20),
'Q1FY2026':(1512,619,893,1666,695,971,-10),'Q2FY2026':(1423,656,767,1711,807,904,-16),'Q3FY2026':(1615,727,888,1733,738,995,-10),
'Q4FY2026':(1297,590,707,1476,647,829,-17),'Q1FY2027':(1180,536,644,1512,619,893,-26)}
# adidas Greater China currency-neutral growth, calendar quarters (peers_reported panel; Q2/Q3 2025 from adidas releases, ex-Yeezy)
ad={'2024Q2':9.3,'2024Q3':8.9,'2024Q4':16.1,'2025Q1':12.7,'2025Q2':13,'2025Q3':10,'2025Q4':15,'2026Q1':17,'2026Q2':15}
def adal(q):  # Nike quarter -> months-weighted calendar quarters
    m={'Q1FY2025':('2024Q2','2024Q3'),'Q2FY2025':('2024Q3','2024Q4'),'Q3FY2025':('2024Q4','2025Q1'),'Q4FY2025':('2025Q1','2025Q2'),
       'Q1FY2026':('2025Q2','2025Q3'),'Q2FY2026':('2025Q3','2025Q4'),'Q3FY2026':('2025Q4','2026Q1'),'Q4FY2026':('2026Q1','2026Q2'),
       'Q1FY2027':('2026Q2','2026Q3'),'Q2FY2027':('2026Q3','2026Q4')}[q]
    a,b=m
    if b in ad: return ad[a]/3+2*ad[b]/3
    return ad[a]/3+2*15/3  # Q3/Q4 2026 adidas not yet reported: assume +15 (Q2 2026 level)
S_NIKE,S_ADI=0.52,0.25; G_OTH=3.0   # Pou Sheng revenue shares (assumption), others growth
def implied(gp,q,s=S_NIKE,a=S_ADI,go=G_OTH):
    o=1-s-a; return (gp-a*adal(q)-o*go)/s
rows=[]
for q,(t,d,w,tp,dp,wp,cc) in nk.items():
    rep=(t/tp-1)*100; fx=cc-rep; wrep=(w/wp-1)*100; drep=(d/dp-1)*100
    wcc=wrep+fx; dcc=drep+fx
    g=implied(psq[q],q)
    rows.append(dict(q=q,nike_gc_rep=round(rep,1),nike_gc_cc=cc,fx_pts=round(fx,1),wh_rep=round(wrep,1),wh_cc_est=round(wcc,1),dir_rep=round(drep,1),dir_cc_est=round(dcc,1),
        ps_total=round(psq[q],1),adidas_aligned=round(adal(q),1),ps_implied_nike=round(g,1),gap_wh=round(wcc-g,1),gap_total=round(cc-g,1)))
import statistics as st
gw=[r['gap_wh'] for r in rows]; gt=[r['gap_total'] for r in rows]
print('gap wholesale: mean %.1f sd %.1f min %.1f max %.1f'%(st.mean(gw),st.stdev(gw),min(gw),max(gw)))
print('gap total    : mean %.1f sd %.1f min %.1f max %.1f'%(st.mean(gt),st.stdev(gt),min(gt),max(gt)))
last4=gw[-4:]; print('last4 wholesale gap mean %.1f'%st.mean(last4))
with open(D+'/backtest_pousheng_implied_vs_nike.csv','w') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])+['tag']);w.writeheader()
    for r in rows: r['tag']='DERIVED; Nike inputs OPENED (10-Q/10-K, calls); PS inputs OPENED (HKEX); shares ASSUMED s=0.52 a=0.25 other g=+3'; w.writerow(r)
for r in rows: print(r)
# sensitivity of Q1FY27 implied to shares
print('Q1FY27 implied Nike at PS by share assumption:')
for s in(0.45,0.52,0.58):
    for a in(0.20,0.25,0.30):
        print(s,a,round(implied(psq['Q1FY2027'],'Q1FY2027',s,a),1),end=' | ')
    print()
# ---- Q2 FY27 nowcast
base=dict(total=1423,direct=656,wh=767)
fx_q2=5.5  # pts-equivalent: reported=(1+cc)*(1.055)-1 (Q1FY27 realised 1.054 vs spot 1.061)
def scen(ps,gap,cut,dcc,adi=15.0,s=S_NIKE):
    a=S_ADI; o=1-s-a
    st_=(ps-a*adi-o*G_OTH)/s
    wcc=st_+gap+cut
    tot=(base['wh']*(1+wcc/100)+base['direct']*(1+dcc/100))/base['total']-1
    cc=tot*100
    usd=base['total']*(1+cc/100)*(1+fx_q2/100)
    return dict(ps_total_yoy=ps,implied_nike_sellthrough=round(st_,1),gap=gap,online_cut_pts=cut,wholesale_cc=round(wcc,1),direct_cc=dcc,gc_cc=round(cc,1),gc_usd_m=round(usd),gc_rep_yoy=round((usd/base['total']-1)*100,1))
mg=st.mean(gw[-4:]); sdg=st.stdev(gw[-4:])
sc={
 'A_bull_partner_data_only':scen(-4,0,0,-9),
 'B_base_partner_data_only':scen(-8,round(mg,1),0,-15),
 'C_base_plus_online_cut':scen(-8,round(mg,1),-5,-15),
 'E_central_C_with_direct_at_-22':scen(-8,round(mg,1),-5,-22),
 'D_bear_PS_runrate_plus_cut':scen(-12,round(mg-sdg,1),-10,-22),
}
for k,v in sc.items(): print(k,v)
with open(D+'/nowcast_scenarios_q2fy27.csv','w') as f:
    w=csv.writer(f);cols=list(next(iter(sc.values())));w.writerow(['scenario']+cols+['tag'])
    for k,v in sc.items(): w.writerow([k]+[v[c] for c in cols]+['DERIVED; see W5 note section 6 for every assumption'])
json.dump(sc,open('/tmp/w5_sc.json','w'))
