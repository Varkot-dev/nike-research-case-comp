import json,datetime,bisect,statistics,csv,sys,os
P='px2/'
cache={}
def load(t):
    if t in cache: return cache[t]
    f=P+t.replace('^','_')+'.json'
    try:
        r=json.load(open(f))['chart']['result'][0]
    except Exception: cache[t]=None; return None
    ts=r['timestamp']; q=r['indicators']['quote'][0]
    ac=r['indicators'].get('adjclose',[{}])[0].get('adjclose') or q['close']
    gm=r['meta'].get('gmtoffset',0)
    out={}
    for t_,c in zip(ts,ac):
        if c is None: continue
        d=(datetime.datetime.utcfromtimestamp(t_+gm)).date()
        out[d]=c
    ds=sorted(out); cache[t]=(ds,[out[d] for d in ds]); return cache[t]
def rets(t,day0,hs=(0,1,5,20)):
    L=load(t)
    if not L: return None
    ds,cl=L
    d0=datetime.date.fromisoformat(day0)
    i=bisect.bisect_left(ds,d0)
    if i>=len(ds) or i==0: return None
    if ds[i]!=d0 and (ds[i]-d0).days>4: return None
    base=cl[i-1]
    res={}
    for h in hs:
        j=i+h
        res[h]=cl[j]/base-1 if j<len(cl) else None
    res['d0actual']=ds[i].isoformat()
    return res
BASKET=['NKE','LULU','VFC','UAA','PVH','RL','TPR','COLM','CROX','DECK','WWW','LEVI','KTB','GIL','CPRI','GIII']
def basket(day0,exclude,hs=(0,1,5,20)):
    rs=[]
    for t in BASKET:
        if t in exclude: continue
        r=rets(t,day0,hs)
        if r and all(r[h] is not None for h in hs): rs.append(r)
    if len(rs)<5: return None
    return {h:statistics.mean(r[h] for r in rs) for h in hs}|{'n':len(rs)}
