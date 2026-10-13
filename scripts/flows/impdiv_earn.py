import csv,json,math,datetime,statistics,sys
S0=35.33; r=0.0405
ch=list(csv.DictReader(open(sys.argv[1])))
exdates=[datetime.date(2026,12,1),datetime.date(2027,3,1),datetime.date(2027,6,1),datetime.date(2027,9,1),datetime.date(2027,12,1),datetime.date(2028,3,1),datetime.date(2028,6,1),datetime.date(2028,9,1),datetime.date(2028,12,1)]
today=datetime.date(2026,10,13)
out=[]
for e in sorted(set(x['expiry'] for x in ch)):
    ed=datetime.date.fromisoformat(e); T=(ed-today).days/365
    c={float(x['strike']):x for x in ch if x['expiry']==e and x['type']=='C'}; p={float(x['strike']):x for x in ch if x['expiry']==e and x['type']=='P'}
    vals=[]
    for K in c:
        if K in p and 0.9*S0<=K<=1.1*S0 and c[K]['mid'] and p[K]['mid']:
            vals.append(S0-(float(c[K]['mid'])-float(p[K]['mid']))-K*math.exp(-r*T))
    sched=sum(0.41*math.exp(-r*(d-today).days/365) for d in exdates if d<ed)
    n=sum(1 for d in exdates if d<ed)
    if vals: out.append(dict(expiry=e,days=(ed-today).days,implied_pv_div=round(statistics.median(vals),3),scheduled_pv_div_at_041=round(sched,3),ex_dates_before_expiry=n,implied_vs_sched_pct=round((statistics.median(vals)/sched-1)*100,1) if sched else '',n_strikes=len(vals)))
w=csv.DictWriter(open(sys.argv[3],'w',newline=''),fieldnames=list(out[0].keys()));w.writeheader();w.writerows(out)
for o in out: print(o)
# earnings reactions
d=json.load(open(sys.argv[2]))['chart']['result'][0]
ts=[datetime.datetime.fromtimestamp(t,datetime.timezone.utc).date() for t in d['timestamp']]; cl=d['indicators']['quote'][0]['close']
er=[]
for s in sys.argv[4].split(','):
    dt=datetime.date.fromisoformat(s)
    i=max(k for k,t in enumerate(ts) if t<=dt)
    er.append(dict(release_date=s,close_before=round(cl[i],2),next_close=round(cl[i+1],2),move_pct=round((cl[i+1]/cl[i]-1)*100,2)))
w=csv.DictWriter(open(sys.argv[5],'w',newline=''),fieldnames=list(er[0].keys()));w.writeheader();w.writerows(er)
for x in er: print(x)
a=[abs(x['move_pct']) for x in er]; print('mean abs',round(sum(a)/len(a),2),'median',statistics.median(a),'last8 mean',round(sum(a[:8])/8,2))
