"""N2: Nike NA footwear sell-in vs Circana-based market sell-through proxy.
Inputs hard-coded below with source tags. Run: python3 -I scripts/niche/n2_sellin_vs_sellthrough.py
Outputs: data/niche/N2_nike_sellin_vs_sellthrough.csv, data/niche/N2_scenarios.csv
"""
import csv, os
root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
# NA footwear revenue $M by Nike fiscal quarter (10-Q segment tables, OPENED 2026-10-15; Q4 = 10-K annual less 9M, DERIVED)
NAF = {'Q1FY23':3805,'Q2FY23':3963,'Q3FY23':3322,'Q4FY23':14897-3805-3963-3322,
       'Q1FY24':3733,'Q2FY24':3757,'Q3FY24':3460,'Q4FY24':14537-3733-3757-3460,
       'Q1FY25':3212,'Q2FY25':3236,'Q3FY25':3132,'Q4FY25':12684-3212-3236-3132,
       'Q1FY26':3219,'Q2FY26':3542,'Q3FY26':3326,'Q4FY26':13317-3219-3542-3326,
       'Q1FY27':3259}
# NA channel split (data/nike_channel_split.csv)
rows = list(csv.DictReader(open(os.path.join(root,'data','nike_channel_split.csv'))))
CH = {}
for r in rows:
    if r['segment']=='north_america' and r['period'].startswith('Q'):
        CH.setdefault(r['period'].replace('FY20','FY'),{})[r['channel']] = float(r['value_usd_m'])
# NA footwear unit change YoY % (10-Q NA MD&A bullets, OPENED); Q4 not disclosed quarterly
UNITS = {'Q1FY24':-10,'Q2FY24':-17,'Q3FY24':7,'Q1FY25':-15,'Q2FY25':-6,'Q3FY25':-8,
         'Q1FY26':5,'Q2FY26':14,'Q3FY26':4,'Q1FY27':2}
fq = sorted(NAF, key=lambda q:(int(q[4:]),q[:2]))
def prior(q): return q[:4]+str(int(q[4:])-1)
out=[]
for q in fq:
    c = CH[q]; tot=c['total']; f = NAF[q]/tot
    out.append(dict(q=q, na_foot=NAF[q], na_total=tot, na_wh=c['wholesale'], na_dir=c['direct'],
        foot_share=round(f,4), wh_foot=round(f*c['wholesale'],1), dir_foot=round(f*c['direct'],1)))
D = {o['q']:o for o in out}
# Market proxy by calendar quarter (Circana, dollars, YoY %). Nike FQn maps to calendar quarter n+2 (2 of 3 months overlap).
# total: reported or derived; SL = sport lifestyle; P = performance. Tags in note.
CQ = {  # cq: (total, SL, P, tag)
 'CQ1_24':(0,1,1,'reported: Q1 24 total flat, leisure +1, performance +1 (SGI/SGB)'),
 'CQ2_24':(-2,0,3,'reported: Q2 24 total -2, leisure flat, performance +3 (FN via Yahoo)'),
 'CQ3_24':(-1,None,0,'reported: Q3 24 total -1, performance flat; SL not given'),
 'CQ4_24':(3,None,None,'DERIVED: FY24 flat with Q1-Q3 at 0,-2,-1 implies Q4 about +3; holiday +3 reported'),
 'CQ1_25':(-4,1,4,'reported: Q1 25 total -4 (universe differs, see note), SL almost +1, performance +4'),
 'CQ2_25':(2,5,7,'DERIVED total/SL from H1 (-1, SL +3) less Q1; performance +7 per rrm.com (Circana POS, SNIPPET-grade)'),
 'CQ3_25':(3,5,None,'reported: Q3 25 total +3, SL +5, fashion -1, ASP +4, units -1'),
 'CQ4_25':(2,None,None,'reported: Q4 25 total +2, ASP +8, units down; performance FY +6, SL FY +4'),
 'CQ1_26':(1,None,5,'reported: Q1 26 total +1, performance +5; SL decline not quantified'),
 'CQ2_26':(1,None,7,'DERIVED: H1 26 total +1, performance +6, SL decline not quantified'),
}
# Athletic proxy = 0.71*SL + 0.29*P (weights from Q1 24 Circana $: leisure 4.4B, performance 1.8B). Fill gaps with annual reported:
SL_FILL = {'CQ3_24':5.5,'CQ4_24':5.5,'CQ4_25':5.0,'CQ1_26':-1.0,'CQ2_26':-2.0}   # ASSUMED, see note (SL annual +3 / +4, 2026 sign negative)
P_FILL  = {'CQ4_24':3.0,'CQ3_25':7.0,'CQ4_25':6.0}                             # ASSUMED from FY performance +6 and neighbours
W_SL, W_P = 0.71, 0.29
def ath(cq):
    t,sl,p,_=CQ[cq]
    sl = sl if sl is not None else SL_FILL[cq]; p = p if p is not None else P_FILL[cq]
    return W_SL*sl+W_P*p
def cq_of(q):
    n=int(q[1]); fy=int(q[4:]); cqn=n+2; yr=2000+fy-1  # Q1FY25 (Jun-Aug 2024) -> CQ3_24
    if cqn>4: cqn-=4; yr+=1
    return 'CQ%d_%d'%(cqn,yr-2000)
SCEN = {'S0 no share change':0.0,'S1 Euromonitor avg -2.7%/yr':-2.7,'S2 -5%/yr':-5.0}
qrows=[]
for q in fq:
    p=prior(q)
    if p not in D: continue
    o=D[q]; wf_g = (o['wh_foot']/D[p]['wh_foot']-1)*100; df_g=(o['dir_foot']/D[p]['dir_foot']-1)*100
    nf_g=(o['na_foot']/D[p]['na_foot']-1)*100
    cq=cq_of(q); m = ath(cq) if cq in CQ else None
    r=dict(quarter=q,na_footwear_usd_m=o['na_foot'],na_footwear_yoy_pct=round(nf_g,1),
           na_wholesale_footwear_est_usd_m=o['wh_foot'],wholesale_footwear_yoy_pct=round(wf_g,1),
           nike_direct_footwear_est_yoy_pct=round(df_g,1),
           na_footwear_units_yoy_pct=UNITS.get(q,''),
           calendar_quarter_mapped=cq if cq in CQ else '', circana_total_yoy_pct=CQ[cq][0] if cq in CQ else '',
           athletic_proxy_yoy_pct=round(m,1) if m is not None else '')
    if m is not None:
        for k,s in SCEN.items():
            st=(1+m/100)*(1+s/100)-1
            ex=wf_g-st*100
            r['excess_wholesale_sellin_vs_sellthrough_pts_'+k[:2]]=round(ex,1)
            r['excess_usd_m_'+k[:2]]=round(D[p]['wh_foot']*ex/100,0)
    qrows.append(r)
keys=[]
for r in qrows:
    for k in r:
        if k not in keys: keys.append(k)
with open(os.path.join(root,'data','niche','N2_nike_sellin_vs_sellthrough.csv'),'w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=keys); w.writeheader(); [w.writerow(r) for r in qrows]
# Annual calendar windows (Jul-Jun style: CQ3..CQ2 = Nike FY Q1..Q4 is shifted; use calendar year = Q3FYn..Q2FYn+1)
def win(qs,field): return sum(D[q][field] for q in qs)
CY = {'CY23':['Q3FY23','Q4FY23','Q1FY24','Q2FY24'],'CY24':['Q3FY24','Q4FY24','Q1FY25','Q2FY25'],
      'CY25':['Q3FY25','Q4FY25','Q1FY26','Q2FY26']}
ANN={'CY24':(0.71*3+0.29*2, 'SL +3 (FY24), P ~+2 (Q1-Q3 avg)'),'CY25':(0.71*4+0.29*6,'SL +4, P +6 (FY25)')}
BAND={'CY24':(-1.0,2.7,4.0),'CY25':(2.5,4.6,6.0)}   # low/mid/high athletic dollar growth, subjective band
sc=[]
for s_name,s in SCEN.items():
    for bi,bn in enumerate(['low','mid','high']):
        base_wh=win(CY['CY23'],'wh_foot'); st=base_wh; row={'scenario':s_name,'market_band':bn}
        cum_gap=0
        for y,prev in (('CY24','CY23'),('CY25','CY24')):
            g=BAND[y][bi]
            st=st*(1+g/100)*(1+s/100)
            wh=win(CY[y],'wh_foot'); gap=wh-st
            row[y+'_wh_sellin_usd_m']=round(wh); row[y+'_implied_partner_sellthrough_usd_m']=round(st)
            row[y+'_cum_sellin_minus_sellthrough_usd_m']=round(gap)
            row[y+'_gap_pct_of_sellin']=round(100*gap/wh,1)
        sc.append(row)
with open(os.path.join(root,'data','niche','N2_scenarios.csv'),'w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(sc[0].keys())); w.writeheader(); [w.writerow(r) for r in sc]
for r in qrows: print(r)
print()
for r in sc: print(r)
print({y:(round(win(CY[y],'wh_foot')),round(win(CY[y],'dir_foot')),round(win(CY[y],'na_foot'))) for y in CY})
