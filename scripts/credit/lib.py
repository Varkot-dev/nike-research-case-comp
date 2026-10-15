import csv,glob,datetime as dt,math,re,sys
sys.path.insert(0,'/tmp/claude-0/-home-user-nike-research-case-comp/2bf9f309-3096-5c65-b9c3-02b984182743/scratchpad/scripts')
import parse
RAW='/tmp/claude-0/-home-user-nike-research-case-comp/2bf9f309-3096-5c65-b9c3-02b984182743/scratchpad/raw'
TEN={'1 Mo':1/12,'2 Mo':2/12,'3 Mo':.25,'4 Mo':4/12,'6 Mo':.5,'1 Yr':1,'2 Yr':2,'3 Yr':3,'5 Yr':5,'7 Yr':7,'10 Yr':10,'20 Yr':20,'30 Yr':30}
def load_tsy():
    c={}
    for f in glob.glob(RAW+'/tsy20*.csv'):
        for r in csv.DictReader(open(f)):
            m,d,y=r['Date'].split('/')
            try: dd=dt.date(int(y),int(m),int(d))
            except: continue
            cur={}
            for k,v in r.items():
                if k in TEN and v not in('',None): cur[TEN[k]]=float(v)
            c[dd]=cur
    return c
TSY=load_tsy()
def curve_at(d):
    if d<min(TSY): d=min(TSY)
    while d not in TSY: d-=dt.timedelta(days=1)
    return TSY[d]
def interp(cur,t):
    ks=sorted(cur)
    if t<=ks[0]: return cur[ks[0]]
    if t>=ks[-1]: return cur[ks[-1]]
    for a,b in zip(ks,ks[1:]):
        if a<=t<=b: return cur[a]+(cur[b]-cur[a])*(t-a)/(b-a)
def load_oas(sid):
    out={}
    for r in csv.reader(open(f'{RAW}/{sid}.csv')):
        if r[0][:2]!='20': continue
        try: out[dt.date.fromisoformat(r[0])]=float(r[1])*100
        except: pass
    return out
def d360(a,b): return (b.year-a.year)*360+(b.month-a.month)*30+(min(b.day,30)-min(a.day,30))
def add_months(d,n):
    y=d.year+(d.month-1+n)//12; m=(d.month-1+n)%12+1
    import calendar
    return dt.date(y,m,min(d.day,calendar.monthrange(y,m)[1]))
def cashflows(settle,mat,cpn,freq=2):
    # coupon dates stepping back from maturity
    dates=[]; d=mat; k=0
    step=12//freq
    while d>settle:
        dates.append(d); k+=1; d=add_months(mat,-step*k)
    dates=sorted(dates); last=d
    return last,dates
def price_from_y(y,settle,mat,cpn,freq=2):
    last,dates=cashflows(settle,mat,cpn,freq)
    nxt=dates[0]
    step=12//freq
    acc_days=d360(last,settle); per=360/freq
    frac=1-acc_days/per  # fraction of period to next coupon
    pv=0
    for i,dd in enumerate(dates):
        cf=cpn/freq+(100 if i==len(dates)-1 else 0)
        pv+=cf/(1+y/freq)**(frac+i)
    accrued=cpn/freq*acc_days/per
    return pv, accrued   # dirty, accrued
def ytm(clean,settle,mat,cpn,freq=2):
    lo,hi=-0.05,0.5
    for _ in range(100):
        mid=(lo+hi)/2
        dirty,acc=price_from_y(mid,settle,mat,cpn,freq)
        if dirty-acc>clean: lo=mid
        else: hi=mid
    return mid*100
def zero_curve(cur,settle,maxT=31):
    # bootstrap semiannual zero rates (continuous-ish via discount factors) from par curve interpolated at 0.5 steps
    n=int(maxT*2); df=[]; z=[]
    for i in range(1,n+1):
        t=i/2; p=interp(cur,t)/100
        if t<=1.0:  # bills: simple compounding semiannual => df=1/(1+p*t) (bond-equivalent)
            d=1/(1+p*t)
        else:
            d=(1-p/2*sum(df))/(1+p/2)
        df.append(d)
    return df
def zspread(clean,settle,mat,cpn,cur):
    df=zero_curve(cur,settle)
    last,dates=cashflows(settle,mat,cpn)
    acc_days=d360(last,settle); per=180
    frac=1-acc_days/per
    accrued=cpn/2*acc_days/per
    # time of each cashflow in years from settle
    ts=[(frac+i)/2 for i in range(len(dates))]
    zr=[]  # zero yield at t via df interpolation (log-linear on semiannual grid)
    def dfat(t):
        # grid t_k=k/2; df list index k-1; df at 0 =1
        k=t*2
        if k<=0: return 1.0
        lo=int(math.floor(k)); hi=lo+1
        d0=1.0 if lo==0 else df[lo-1]
        if hi>len(df): return df[-1]**(t/(len(df)/2))
        d1=df[hi-1]
        w=k-lo
        return math.exp((1-w)*math.log(d0)+w*math.log(d1))
    def pv(s):
        tot=0
        for i,t in enumerate(ts):
            cf=cpn/2+(100 if i==len(ts)-1 else 0)
            tot+=cf*dfat(t)*math.exp(-s*t)
        return tot
    lo,hi=-0.05,0.3
    for _ in range(80):
        mid=(lo+hi)/2
        if pv(mid)>clean+accrued: lo=mid
        else: hi=mid
    return mid*1e4
