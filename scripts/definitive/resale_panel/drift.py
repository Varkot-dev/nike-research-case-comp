import json,csv,statistics as S
P='/tmp/claude-0/-home-user-nike-research-case-comp/c6360f77-8844-5e04-9011-d8ceb3c498c8/scratchpad/dt/resale_panel'
base={r['goat_id']:r for r in csv.DictReader(open('/home/user/nike-research-case-comp/data/jordan_resale_goat_20261013.csv'))}
old=json.load(open('/tmp/claude-0/-home-user-nike-research-case-comp/c6360f77-8844-5e04-9011-d8ceb3c498c8/scratchpad/rh/resale/raw/buybar.json'))
new=json.load(open(P+'/dl/goat/recheck.json'))
def metr(data):
    good=[x for x in data if x.get('shoeCondition')=='new_no_defects' and x.get('boxCondition')=='good_condition']
    amt=lambda x,k:((x.get(k) or {}).get('amount') or 0)/100 or None
    bysz={x['sizeOption']['value']:x for x in good}; core=[x for s,x in bysz.items() if 7<=s<=13]
    a=[amt(x,'lowestPriceCents') for x in core if amt(x,'lowestPriceCents')]; l=[amt(x,'lastSoldPriceCents') for x in core if amt(x,'lastSoldPriceCents')]
    ch=sum(1 for s,x in bysz.items() if 7<=s<=13)
    return (S.median(l) if l else None, S.median(a) if a else None, {s:(amt(x,'lowestPriceCents'),amt(x,'lastSoldPriceCents')) for s,x in bysz.items() if 7<=s<=13})
out=[]
for gid,v in new.items():
    if gid.startswith('_'): continue
    b=base[gid]; ret=float(b['retail_usd'])
    ml0,ma0,s0=metr(old[gid]['data']); ml1,ma1,s1=metr(v['data'])
    nchg_last=sum(1 for s in s1 if s in s0 and s0[s][1]!=s1[s][1]); nchg_ask=sum(1 for s in s1 if s in s0 and s0[s][0]!=s1[s][0])
    out.append(dict(goat_id=gid,line=b['line'],name=b['name'],retail_usd=ret,obs0_utc=old[gid]['observed_utc'],obs1_utc=v['observed_utc'],
      med_last_0=ml0,med_last_1=ml1,med_ask_0=ma0,med_ask_1=ma1,
      drift_last_pct_DERIVED=round(ml1/ml0-1,4) if ml0 and ml1 else None,drift_ask_pct_DERIVED=round(ma1/ma0-1,4) if ma0 and ma1 else None,
      prem_last_0_DERIVED=round(ml0/ret-1,4) if ml0 else None,prem_last_1_DERIVED=round(ml1/ret-1,4) if ml1 else None,
      n_sizes_last_changed=nchg_last,n_sizes_ask_changed=nchg_ask,api_url=v['url']))
w=csv.DictWriter(open(P+'/goat_drift_recheck_20261013.csv','w',newline=''),fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
dl=[o['drift_last_pct_DERIVED'] for o in out if o['drift_last_pct_DERIVED'] is not None]; da=[o['drift_ask_pct_DERIVED'] for o in out if o['drift_ask_pct_DERIVED'] is not None]
print('n',len(out),'median drift last',S.median(dl),'mean',round(S.mean(dl),4),'max abs',max(map(abs,dl)),'n nonzero',sum(1 for x in dl if x))
print('median drift ask',S.median(da),'mean',round(S.mean(da),4),'max abs',max(map(abs,da)),'n nonzero',sum(1 for x in da if x))
print('sizes last changed total',sum(o['n_sizes_last_changed'] for o in out),'ask changed',sum(o['n_sizes_ask_changed'] for o in out))
print('obs range',min(o['obs1_utc'] for o in out),max(o['obs1_utc'] for o in out))
for line in ['AJ1 High OG','AJ3','AJ4','AJ5','AJ11']:
    g=[o for o in out if o['line']==line and o['drift_last_pct_DERIVED'] is not None]; print(line,len(g),S.median(o['drift_last_pct_DERIVED'] for o in g) if g else None)
