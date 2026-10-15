import json,numpy as np
rows=[r for r in json.load(open('rows.json')) if r['stance_group']!='EXCLUDE']
rng=np.random.default_rng(1)
def perm(a,b,n=20000):
    a=np.array(a);b=np.array(b); obs=a.mean()-b.mean(); allv=np.concatenate([a,b]); c=0
    for _ in range(n):
        rng.shuffle(allv); c+= abs(allv[:len(a)].mean()-allv[len(a):].mean())>=abs(obs)
    return obs,c/n
def mw(a,b):
    a=np.array(a);b=np.array(b); u=sum((x>y)+0.5*(x==y) for x in a for y in b); return u/(len(a)*len(b))
# objective group: company-document-only
OBJ_DOWN={'E04','E06','E08','E10','E12','E14','E15','E28'}
OBJ_UP={'E01','E03','E07','E19'}
for r in rows:
    r['obj']='CUT_OR_VAGUE' if r['event_id'] in OBJ_DOWN else ('RAISED' if r['event_id'] in OBJ_UP else 'DATED_NO_CUT_OTHER')
    r['dated_nocut']= r['event_id'] not in OBJ_DOWN
out=[]
def P(s): print(s); out.append(s)
for bench in ('vs_sp','vs_sector'):
  for h in (0,1,2,3,5,20):
    k=f'{bench}_d{h}'
    g=lambda f:[r[k] for r in rows if f(r) and r[k] is not None]
    A=g(lambda r:r['dated_nocut']); B=g(lambda r:not r['dated_nocut'])
    U=g(lambda r:r['stance_group']=='UP'); D=g(lambda r:r['stance_group']=='DOWN'); N=g(lambda r:r['stance_group']=='NEUTRAL')
    R=g(lambda r:r['obj']=='RAISED')
    o,p=perm(A,B); o2,p2=perm(U,D)
    P(f"{k}: dated-no-cut n={len(A)} mean={100*np.mean(A):.1f} med={100*np.median(A):.1f} | cut/vague n={len(B)} mean={100*np.mean(B):.1f} med={100*np.median(B):.1f} | diff={100*o:.1f} perm p={p:.4f} P(A>B)={mw(A,B):.2f} || UP n={len(U)} mean={100*np.mean(U):.1f} med={100*np.median(U):.1f} NEUT mean={100*np.mean(N):.1f} DOWN mean={100*np.mean(D):.1f} UPvsDOWN p={p2:.4f} || RAISED(objective) n={len(R)} mean={100*np.mean(R):.1f}")
# investor-day only (exclude earnings-bundled)
EARN={'E03','E04','E06','E12','E28'}
for h in (0,1,5,20):
    k=f'vs_sp_d{h}'
    g=lambda f:[r[k] for r in rows if f(r) and r['event_id'] not in EARN]
    P(f"INVESTOR-DAY-ONLY {k}: UP n={len(g(lambda r:r['stance_group']=='UP'))} mean={100*np.mean(g(lambda r:r['stance_group']=='UP')):.1f} | NEUT n={len(g(lambda r:r['stance_group']=='NEUTRAL'))} mean={100*np.mean(g(lambda r:r['stance_group']=='NEUTRAL')):.1f} | DOWN n={len(g(lambda r:r['stance_group']=='DOWN'))} mean={100*np.mean(g(lambda r:r['stance_group']=='DOWN')):.1f}")
# ex-E03 UP
for h in (0,1,5):
    k=f'vs_sp_d{h}'; U=[r[k] for r in rows if r['stance_group']=='UP' and r['event_id']!='E03']
    P(f"UP ex-E03 {k}: n={len(U)} mean={100*np.mean(U):.1f} med={100*np.median(U):.1f}")
# drawdown test
for lim in (-0.3,-0.4):
    S=[r for r in rows if r['drawdown_from_52w_high']<=lim]
    P(f"drawdown<= {lim}: n={len(S)} "+", ".join(f"{r['event_id']}:{100*r['vs_sp_d1']:.0f}" for r in S)+f" mean vs_sp_d1={100*np.mean([r['vs_sp_d1'] for r in S]):.1f}; others mean={100*np.mean([r['vs_sp_d1'] for r in rows if r['drawdown_from_52w_high']>lim]):.1f}")
# tail counts, all
d0=[r['vs_sp_d0'] for r in rows]; d1=[r['vs_sp_d1'] for r in rows]; d3=[r['vs_sp_d3'] for r in rows]
P(f"All n={len(rows)}: d0 vs SP >= +5%: {sum(x>=.05 for x in d0)}, <= -5%: {sum(x<=-.05 for x in d0)}, <= -10%: {sum(x<=-.10 for x in d0)}, >= +10%: {sum(x>=.10 for x in d0)}")
P(f"All n={len(rows)}: d1 vs SP >= +5%: {sum(x>=.05 for x in d1)}, <= -5%: {sum(x<=-.05 for x in d1)}, <= -10%: {sum(x<=-.10 for x in d1)}, >= +10%: {sum(x>=.10 for x in d1)}")
P(f"All n={len(rows)}: d3 vs SP >= +5%: {sum(x>=.05 for x in d3)}, <= -5%: {sum(x<=-.05 for x in d3)}, <= -10%: {sum(x<=-.10 for x in d3)}")
P(f"abs d1 vs SP: mean {100*np.mean(np.abs(d1)):.1f}, median {100*np.median(np.abs(d1)):.1f}")
# largest-sample: dated_nocut with worst values
A=sorted([(r['vs_sp_d0'],r['event_id']) for r in rows if r['dated_nocut']]); P('dated-no-cut worst d0 vs SP: '+str([(e,round(100*x,1)) for x,e in A[:4]])+' best '+str([(e,round(100*x,1)) for x,e in A[-4:]]))
A=sorted([(r['vs_sp_d5'],r['event_id']) for r in rows if r['dated_nocut']]); P('dated-no-cut worst d5 vs SP: '+str([(e,round(100*x,1)) for x,e in A[:4]]))
open('stats_out.txt','w').write('\n'.join(out))
