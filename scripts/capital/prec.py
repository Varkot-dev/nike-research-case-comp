import json,sys,datetime,csv
D=sys.argv[1]; OUT=sys.argv[2]
def load(t):
    j=json.load(open(f'{D}/{t}.json'))['chart']['result'][0]
    ts=j['timestamp']; c=j['indicators']['quote'][0]['close']; ac=j['indicators']['adjclose'][0]['adjclose']
    rows=[(datetime.datetime.utcfromtimestamp(a).date().isoformat(),b,d) for a,b,d in zip(ts,c,ac) if b is not None]
    return rows
spy=load('SPY'); spyd={r[0]:r for r in spy}
ev=[('KHC','2019-02-21','after close','cut 36% (0.625 to 0.40)'),
    ('VFC','2023-02-07','pre-market','cut 41% (0.51 to 0.30)'),
    ('VFC','2023-10-30','after close','cut 70% (0.30 to 0.09)'),
    ('INTC','2023-02-22','see note','cut 66% (0.365 to 0.125)'),
    ('INTC','2024-08-01','after close','suspended (0.125 to 0)'),
    ('EL','2024-10-31','pre-market','cut 47% (0.66 to 0.35)')]
w=csv.writer(open(OUT,'w')); w.writerow(['ticker','announce_date','timing','action','pre_close_date','pre_close','reaction_day','reaction_close','reaction_pct','two_day_pct','pct_6m_from_pre','pct_12m_from_pre','spy_6m_pct','spy_12m_pct','rel_12m_pts_vs_spy','low_within_12m','low_date','low_vs_reaction_close_pct','close_12m_vs_reaction_close_pct','source'])
for t,a,tim,act in ev:
    r=load(t); dates=[x[0] for x in r]
    i=next(k for k,d in enumerate(dates) if d>=a)  # announce day index
    pre=i-1 if tim!='after close' else i
    rx=pre+1
    p0=r[pre]; p1=r[rx]; p2=r[min(pre+2,len(r)-1)]
    def at(n): return r[min(pre+n,len(r)-1)]
    s0=spyd[p0[0]]
    def sp(n):
        d=at(n)[0]; return (spyd[d][2]/s0[2]-1)*100
    win=r[rx:pre+253]; lo=min(win,key=lambda x:x[1])
    # adj close returns (dividend-inclusive) for horizons; price close for reaction
    w.writerow([t,a,tim,act,p0[0],round(p0[1],2),p1[0],round(p1[1],2),round((p1[1]/p0[1]-1)*100,1),round((p2[1]/p0[1]-1)*100,1),
      round((at(126)[2]/p0[2]-1)*100,1),round((at(252)[2]/p0[2]-1)*100,1),round(sp(126),1),round(sp(252),1),
      round((at(252)[2]/p0[2]-1)*100-sp(252),1),round(lo[1],2),lo[0],round((lo[1]/p1[1]-1)*100,1),round((at(252)[1]/p1[1]-1)*100,1),
      'market data: Yahoo Finance chart API, downloaded 2026-10-13'])
print(open(OUT).read())
