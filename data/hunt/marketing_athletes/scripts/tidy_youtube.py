import pandas as pd, re, numpy as np, sys
d=pd.read_csv(sys.argv[1])
def vnum(t):
    if not isinstance(t,str): return np.nan
    t=t.replace(',','').lower()
    if 'no views' in t: return 0.0
    m=re.search(r'([\d.]+)\s*(k|m|b|thousand|million|billion)?',t)
    if not m: return np.nan
    mult={'k':1e3,'thousand':1e3,'m':1e6,'million':1e6,'b':1e9,'billion':1e9,None:1}[m.group(2)]
    return float(m.group(1))*mult
d['views']=d.views_text.map(vnum)
def age_years(t):
    if not isinstance(t,str): return np.nan
    m=re.search(r'(\d+)\s*(seconds?|minutes?|hours?|days?|weeks?|months?|years?|mo|w|d|h|y)\b',t)
    if not m: return np.nan
    n=int(m.group(1)); u=m.group(2)
    if u.startswith('mo'): f=1/12
    elif u.startswith('y'): return n+0.5
    elif u.startswith('w'): f=7/365
    elif u.startswith('d'): f=1/365
    else: f=0
    return n*f
d['age_years_mid']=d.age_text.map(age_years)
d['age_bucket']=pd.cut(d.age_years_mid,[-0.01,1,2,3,4,6,100],labels=['<1y','1-2y','2-3y','3-4y','4-6y','6y+'])
d.to_csv(sys.argv[2],index=False)
print(d.groupby('channel').agg(n=('title','size'),views_ok=('views','count'),age_ok=('age_years_mid','count')))
g=d.groupby(['channel','age_bucket'],observed=False).views.agg(['count','median']).unstack()
pd.set_option('display.width',250); print(g)
g.to_csv(sys.argv[3])
