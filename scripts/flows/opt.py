import json,glob,sys,math,datetime,csv
d=sys.argv[1]; S0=float(sys.argv[2]); r=0.04; q=0.0464
now=datetime.datetime(2026,10,13,20,0,tzinfo=datetime.timezone.utc)
def N(x): return 0.5*(1+math.erf(x/math.sqrt(2)))
def bs(S,K,T,v,call):
    if v<=0 or T<=0: return max(0,(S-K) if call else (K-S))
    d1=(math.log(S/K)+(r-q+0.5*v*v)*T)/(v*math.sqrt(T)); d2=d1-v*math.sqrt(T)
    return S*math.exp(-q*T)*N(d1)-K*math.exp(-r*T)*N(d2) if call else K*math.exp(-r*T)*N(-d2)-S*math.exp(-q*T)*N(-d1)
def iv(p,S,K,T,call):
    lo,hi=0.01,4
    if p<=bs(S,K,T,lo,call): return None
    for _ in range(100):
        m=(lo+hi)/2
        if bs(S,K,T,m,call)>p: hi=m
        else: lo=m
    return m
rows=[];chain=[]
for f in sorted(glob.glob(d+'/e_*.json')):
    res=json.load(open(f))['optionChain']['result'][0]; o=res['options'][0]
    exp=datetime.datetime.fromtimestamp(o['expirationDate'],datetime.timezone.utc)
    T=((exp-now).total_seconds()+20*3600)/(365*86400)  # expiry at 4pm ET close approx
    calls={c['strike']:c for c in o['calls']}; puts={p['strike']:p for p in o['puts']}
    coi=sum(c.get('openInterest',0) or 0 for c in o['calls']); poi=sum(p.get('openInterest',0) or 0 for p in o['puts'])
    cv=sum(c.get('volume',0) or 0 for c in o['calls']); pv=sum(p.get('volume',0) or 0 for p in o['puts'])
    def mid(c):
        b,a=c.get('bid',0) or 0,c.get('ask',0) or 0
        return (b+a)/2 if a>0 and b>0 else None
    ivs={}
    for K in sorted(set(calls)|set(puts)):
        for typ,src in (('C',calls),('P',puts)):
            c=src.get(K)
            if not c: continue
            m=mid(c); v=iv(m,S0,K,T,typ=='C') if m else None
            chain.append(dict(expiry=exp.date().isoformat(),type=typ,strike=K,bid=c.get('bid'),ask=c.get('ask'),last=c.get('lastPrice'),volume=c.get('volume'),open_interest=c.get('openInterest'),yahoo_iv=round(c.get('impliedVolatility',0),4),mid=m,my_iv=round(v,4) if v else ''))
            if v: ivs[(typ,K)]=v
    # ATM: OTM-side IVs averaged at strikes bracketing spot
    ks=sorted(set(k for _,k in ivs))
    below=max([k for k in ks if k<=S0],default=None); above=min([k for k in ks if k>=S0],default=None)
    def avgiv(K):
        v=[ivs[x] for x in (('C',K),('P',K)) if x in ivs]; return sum(v)/len(v) if v else None
    a,b=avgiv(below),avgiv(above)
    atm=a if below==above else (a+(b-a)*(S0-below)/(above-below) if a and b else a or b)
    # straddle at nearest strike
    Kn=min(ks,key=lambda k:abs(k-S0)); st=None
    if Kn in calls and Kn in puts and mid(calls[Kn]) and mid(puts[Kn]): st=mid(calls[Kn])+mid(puts[Kn])
    # skew: IV of ~10% OTM put minus ~10% OTM call
    kp=min(ks,key=lambda k:abs(k-0.9*S0)); kc=min(ks,key=lambda k:abs(k-1.1*S0))
    pivv=ivs.get(('P',kp)); civv=ivs.get(('C',kc))
    rows.append(dict(expiry=exp.date().isoformat(),days=round(T*365,1),atm_iv=round(atm,4) if atm else '',straddle_strike=Kn,straddle_mid=round(st,3) if st else '',straddle_pct_spot=round(st/S0*100,2) if st else '',
        one_sd_move_pct=round(atm*math.sqrt(T)*100,2) if atm else '',lo_1sd=round(S0*math.exp(-atm*math.sqrt(T)),2) if atm else '',hi_1sd=round(S0*math.exp(atm*math.sqrt(T)),2) if atm else '',
        put90_strike=kp,put90_iv=round(pivv,4) if pivv else '',call110_strike=kc,call110_iv=round(civv,4) if civv else '',skew_pts=round((pivv-civv)*100,2) if pivv and civv else '',
        call_oi=coi,put_oi=poi,pc_oi=round(poi/coi,3) if coi else '',call_vol=cv,put_vol=pv,pc_vol=round(pv/cv,3) if cv else ''))
w=csv.DictWriter(open(sys.argv[3],'w',newline=''),fieldnames=list(rows[0].keys()));w.writeheader();w.writerows(rows)
w=csv.DictWriter(open(sys.argv[4],'w',newline=''),fieldnames=list(chain[0].keys()));w.writeheader();w.writerows(chain)
for x in rows: print(x)
print('TOTAL call OI',sum(x['call_oi'] for x in rows),'put OI',sum(x['put_oi'] for x in rows))
