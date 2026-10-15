import csv,math,datetime,statistics,sys
S0=35.33; r=0.0405; today=datetime.date(2026,10,13)
ch=list(csv.DictReader(open(sys.argv[1])))
N=lambda x:0.5*(1+math.erf(x/math.sqrt(2)))
def b76(F,K,T,v,call):
    d1=(math.log(F/K)+0.5*v*v*T)/(v*math.sqrt(T)); d2=d1-v*math.sqrt(T); D=math.exp(-r*T)
    return D*(F*N(d1)-K*N(d2)) if call else D*(K*N(-d2)-F*N(-d1))
def iv(p,F,K,T,call):
    lo,hi=0.01,3
    if p<=b76(F,K,T,lo,call) or p>=b76(F,K,T,hi,call): return None
    for _ in range(80):
        m=(lo+hi)/2
        if b76(F,K,T,m,call)>p: hi=m
        else: lo=m
    return m
out=[]
for e in sorted(set(x['expiry'] for x in ch)):
    ed=datetime.date.fromisoformat(e); T=((ed-today).days+0.0)/365
    if T<=0.01: continue
    c={float(x['strike']):x for x in ch if x['expiry']==e and x['type']=='C' and x['mid']}; p={float(x['strike']):x for x in ch if x['expiry']==e and x['type']=='P' and x['mid']}
    Fs=[K+(float(c[K]['mid'])-float(p[K]['mid']))*math.exp(r*T) for K in c if K in p and 0.9*S0<=K<=1.1*S0]
    F=statistics.median(Fs)
    # OTM IV curve
    curve={}
    for K in sorted(set(c)|set(p)):
        src=c if K>=F else p
        if K in src:
            v=iv(float(src[K]['mid']),F,K,T,K>=F)
            if v: curve[K]=v
    ks=sorted(curve)
    def at(m):
        x=m*F; lo=[k for k in ks if k<=x]; hi=[k for k in ks if k>=x]
        if not lo or not hi: return None
        a,b=lo[-1],hi[0]
        return curve[a] if a==b else curve[a]+(curve[b]-curve[a])*(x-a)/(b-a)
    atm=at(1.0); p90=at(0.9); c110=at(1.1); p80=at(0.8)
    sd=atm*math.sqrt(T) if atm else None
    prob_below=lambda K: N((math.log(K/F)+0.5*atm*atm*T)/(atm*math.sqrt(T)))
    out.append(dict(expiry=e,days=(ed-today).days,implied_forward=round(F,3),atm_iv_fwd=round(atm,4) if atm else '',iv_90pct=round(p90,4) if p90 else '',iv_110pct=round(c110,4) if c110 else '',iv_80pct=round(p80,4) if p80 else '',
      skew_90_minus_110_pts=round((p90-c110)*100,2) if p90 and c110 else '',
      range_1sd_lo=round(F*math.exp(-sd),2) if sd else '',range_1sd_hi=round(F*math.exp(sd),2) if sd else '',
      rn_prob_below_30=round(prob_below(30),3) if atm else '',rn_prob_above_45=round(1-prob_below(45),3) if atm else '',rn_prob_below_25=round(prob_below(25),3) if atm else ''))
w=csv.DictWriter(open(sys.argv[2],'w',newline=''),fieldnames=list(out[0].keys()));w.writeheader();w.writerows(out)
for o in out: print(o)
# event variance
d={o['expiry']:(o['days']/365,o['atm_iv_fwd']) for o in out}
def ev(a,b,base):
    Ta,va=d[a];Tb,vb=d[b]; m2=vb*vb*Tb-va*va*Ta-base*base*(Tb-Ta); return round(math.sqrt(m2)*100,2) if m2>0 else 'neg'
for a,b in (('2026-11-27','2026-12-18'),('2026-11-27','2027-01-15'),('2026-11-20','2027-01-15')):
    print(a,b,'base=a iv',ev(a,b,d[a][1]),'base=Nov13',ev(a,b,d['2026-11-13'][1]),'fwdvol',round(math.sqrt((d[b][1]**2*d[b][0]-d[a][1]**2*d[a][0])/(d[b][0]-d[a][0]))*100,2))
