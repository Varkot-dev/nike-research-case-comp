import json,csv,statistics as S,datetime as dt,random,collections
import numpy as np
P='/tmp/claude-0/-home-user-nike-research-case-comp/c6360f77-8844-5e04-9011-d8ceb3c498c8/scratchpad/dt/resale_panel'
rows=json.load(open(P+'/panel_rows.json'))
base={r['goat_id']:r for r in csv.DictReader(open('/home/user/nike-research-case-comp/data/jordan_resale_goat_20261013.csv'))}
T='AJ1 High OG'; C={'AJ3','AJ4'}
def grp(l): return 'AJ1H' if l==T else ('AJ3/4' if l in C else l)
VAR='premium_ask_DERIVED'
out=[]
def boot(f,shoes,n=2000):
    random.seed(1); v=[]
    for _ in range(n):
        s=[random.choice(shoes) for _ in shoes]
        try: v.append(f(s))
        except Exception: pass
    v.sort(); return (round(v[int(.025*len(v))],3),round(v[int(.975*len(v))],3)) if v else None
# A: early premium (first capture age 14-200d) by cohort
early={}
for r in sorted(rows,key=lambda r:r['age_days']):
    if 14<=r['age_days']<=200 and r['goat_id'] not in early: early[r['goat_id']]=r
print('\n== A. Early premium (StockX median lowest ask US7-13, first capture 14-200 days after release) ==')
def cell(g,coh): return [r[VAR] for r in early.values() if grp(r['line'])==g and coh(r['release_date'])]
cohorts={'2023':lambda d:d[:4]=='2023','2024':lambda d:d[:4]=='2024','2025':lambda d:d[:4]=='2025','2026':lambda d:d[:4]=='2026','post2024-26':lambda d:d>='2024'}
tabA=[]
for g in ['AJ1H','AJ3/4','AJ3','AJ4','AJ5','AJ11']:
    line=[]
    for k,f in cohorts.items():
        v=[r[VAR] for r in early.values() if (grp(r['line'])==g or r['line']==g) and f(r['release_date'])]
        line.append(f"{k}: n={len(v)} med={S.median(v):+.0%} mean={S.mean(v):+.0%}" if v else f"{k}: n=0")
        tabA.append(dict(design='A_early_premium',group=g,cohort=k,n=len(v),median=round(S.median(v),4) if v else None,mean=round(S.mean(v),4) if v else None))
    print(g,' | '.join(line))
def didA(sample,stat=S.mean):
    a1=[r[VAR] for r in sample if grp(r['line'])=='AJ1H' and r['release_date']<'2024']; a2=[r[VAR] for r in sample if grp(r['line'])=='AJ1H' and r['release_date']>='2024']
    c1=[r[VAR] for r in sample if grp(r['line'])=='AJ3/4' and r['release_date']<'2024']; c2=[r[VAR] for r in sample if grp(r['line'])=='AJ3/4' and r['release_date']>='2024']
    return (stat(a2)-stat(a1))-(stat(c2)-stat(c1))
E=[r for r in early.values() if grp(r['line']) in('AJ1H','AJ3/4')]
cn={k:sum(1 for r in E if grp(r['line'])==k[0] and (r['release_date']>='2024')==k[1]) for k in [('AJ1H',False),('AJ1H',True),('AJ3/4',False),('AJ3/4',True)]}
print('A cell n (group, post):',cn)
try:
    dA=didA(E); dAm=didA(E,S.median); ci=boot(lambda s:didA(s),E)
    print(f"DiD A (mean) = {dA:+.3f}  95% bootstrap CI {ci}; DiD A (median) = {dAm:+.3f}")
    out.append(dict(design='A_early_premium_cohort',estimate_mean=round(dA,4),ci95=str(ci),estimate_median=round(dAm,4),n=str(cn)))
except Exception as e: print('DiD A not estimable',e)
# C: half-year two-way FE panel
def hy(d): return d[:4]+('H1' if d[5:7]<='06' else 'H2')
cellv=collections.defaultdict(list)
for r in rows:
    if grp(r['line']) in ('AJ1H','AJ3/4') and r['age_days']>=14: cellv[(r['goat_id'],hy(r['capture_date']))].append(r[VAR])
pan=[(g,p,S.median(v)) for (g,p),v in cellv.items()]
lineof={r['goat_id']:grp(r['line']) for r in rows}
periods=sorted({p for _,p,_ in pan})
print('\n== C. Within-shoe half-year panel (shoe FE + period FE), treat = AJ1H x period >= 2024H1 ==')
tabC=[]
for p in periods:
    a=[v for g,pp,v in pan if pp==p and lineof[g]=='AJ1H']; c=[v for g,pp,v in pan if pp==p and lineof[g]=='AJ3/4']
    print(p,f"AJ1H n={len(a)} mean={S.mean(a):+.0%}" if a else 'AJ1H n=0',f"| AJ3/4 n={len(c)} mean={S.mean(c):+.0%}" if c else '| AJ3/4 n=0')
    tabC.append(dict(design='C_halfyear_means',period=p,n_AJ1H=len(a),mean_AJ1H=round(S.mean(a),4) if a else None,n_AJ34=len(c),mean_AJ34=round(S.mean(c),4) if c else None))
def twfe(pan,cut='2024H1'):
    shoes=sorted({g for g,_,_ in pan}); per=sorted({p for _,p,_ in pan}); si={s:i for i,s in enumerate(shoes)}; pi={p:i for i,p in enumerate(per)}
    X=np.zeros((len(pan),len(shoes)+len(per)-1+1)); y=np.zeros(len(pan))
    for k,(g,p,v) in enumerate(pan):
        X[k,si[g]]=1
        if pi[p]>0: X[k,len(shoes)+pi[p]-1]=1
        X[k,-1]=1.0 if (lineof[g]=='AJ1H' and p>=cut) else 0.0
        y[k]=v
    b=np.linalg.lstsq(X,y,rcond=None)[0]; return b[-1]
# identification needs AJ1H shoes observed both pre and post: count
pre_post=collections.Counter()
for g in {g for g,_,_ in pan}:
    ps=[p for gg,p,_ in pan if gg==g]
    if min(ps)<'2024H1' and max(ps)>='2024H1': pre_post[lineof[g]]+=1
print('shoes observed both pre (<2024) and post:',dict(pre_post))
est=twfe(pan)
print('obs by group x post:',dict(collections.Counter((lineof[g],p>='2024H1') for g,p,_ in pan)))
shoes=sorted({g for g,_,_ in pan}); random.seed(2); bs=[]
for _ in range(1000):
    s=[random.choice(shoes) for _ in shoes]; pp=[]
    for j,g in enumerate(s): pp+=[(g+'#'+str(j),p,v) for gg,p,v in pan if gg==g]
    for g in s: pass
    lo2={}
    for (g,p,v) in pp: lo2[g]=lineof[g.split('#')[0]]
    old=dict(lineof); lineof.update(lo2)
    try: bs.append(twfe(pp))
    except Exception: pass
bs.sort(); ci=(round(bs[25],3),round(bs[975],3))
print(f"TWFE DiD (AJ1H x post-2024) = {est:+.3f}, shoe-cluster bootstrap 95% CI {ci}; n obs={len(pan)}, shoes={len(shoes)}")
out.append(dict(design='C_twfe_halfyear',estimate_mean=round(est,4),ci95=str(ci),n=len(pan),shoes=len(shoes),pre_post_shoes=str(dict(pre_post))))
# C2 using 2025H1 cut
est2=twfe(pan,'2025H1'); print(f"TWFE with cut at 2025H1 = {est2:+.3f}")
out.append(dict(design='C_twfe_halfyear_cut2025H1',estimate_mean=round(est2,4),n=len(pan)))
# B: within-shoe change for pre-cut cohort shoes (released 2023): pre point (<2024) vs latest StockX point (>=2025H2)
print('\n== B. 2023-release shoes: within-shoe change from last pre-2024 capture to latest capture ==')
chg=collections.defaultdict(list)
for g in {g for g,_,_ in pan}:
    pts=sorted([(p,v) for gg,p,v in pan if gg==g])
    pre=[v for p,v in pts if p<'2024H1']; post=[v for p,v in pts if p>='2025H2']
    if pre and post: chg[lineof[g]].append(post[-1]-pre[-1])
for k,v in chg.items(): print(k,'n',len(v),'mean change',f"{S.mean(v):+.3f}",'median',f"{S.median(v):+.3f}")
if chg.get('AJ1H') and chg.get('AJ3/4'):
    d=S.mean(chg['AJ1H'])-S.mean(chg['AJ3/4']); print('DiD B (mean) =',round(d,3)); out.append(dict(design='B_within_shoe_2023cohort',estimate_mean=round(d,4),n=f"AJ1H {len(chg['AJ1H'])}, AJ3/4 {len(chg['AJ3/4'])}"))
# Overhang: total asks by group/period
print('\n== Overhang: StockX total asks (offerCount) per shoe, median by group and half-year ==')
ov=collections.defaultdict(list)
for r in rows:
    if r.get('sx_total_asks') and grp(r['line']) in('AJ1H','AJ3/4','AJ4','AJ3'): ov[(grp(r['line']),hy(r['capture_date']))].append(r['sx_total_asks'])
for k in sorted(ov): print(k,len(ov[k]),S.median(ov[k]))
lat={}
for r in sorted(rows,key=lambda r:r['capture_date']):
    if r['capture_date']>='2025-07-01' and r.get('sx_total_asks'): lat[r['goat_id']]=r
for g in ['AJ1H','AJ3/4']:
    v=[r for r in lat.values() if grp(r['line'])==g]
    if v: print('latest (>=2025H2)',g,'n',len(v),'median asks',S.median(r['sx_total_asks'] for r in v),'median asks/sizes', S.median(r['sx_total_asks'] for r in v))
for r in out: print(r)
csv.DictWriter(open(P+'/did_results.csv','w',newline=''),fieldnames=sorted({k for r in out for k in r})).writeheader()
with open(P+'/did_results.csv','a',newline='') as f:
    w=csv.DictWriter(f,fieldnames=sorted({k for r in out for k in r})); w.writerows(out)
with open(P+'/did_cells.csv','w',newline='') as f:
    ks=sorted({k for r in tabA+tabC for k in r}); w=csv.DictWriter(f,fieldnames=ks); w.writeheader(); w.writerows(tabA+tabC)
