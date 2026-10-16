import sys; sys.path.insert(0,'/tmp/claude-0/scr')
import pandas as pd,re,csv,json
from classify2 import *
OUT='/home/user/nike-research-case-comp/data/hunt/w8_launch_newness/'
d=pd.read_csv('/tmp/claude-0/scr/sbd_raw.csv').drop_duplicates(['name','style','date'])
d['date']=d.date.astype(str)
d['rdate']=pd.to_datetime(d.date,errors='coerce')
def prec(r):
    if pd.notna(r.rdate): return 'day'
    if re.match(r'^[A-Za-z]+ 20\d\d$',str(r.date)): return 'month'
    if re.match(r'^20\d\d$',str(r.date)): return 'year'
    return 'unk'
d['prec']=d.apply(prec,axis=1)
d.loc[d.prec=='month','rdate']=pd.to_datetime(d.loc[d.prec=='month','date'],format='%B %Y',errors='coerce')
d['src']=d.file.map(lambda f:'SBD_jordan' if '_j_' in f else 'SBD_main')
d['yr_undated']=d.apply(lambda r: int(r.date) if r.prec=='year' else None,axis=1)
d['b']=d.name.map(brand_of)
d['cls']=[nike_class(n) if b in('Nike','Jordan') else peer_class(n,b) for n,b in zip(d.name,d.b)]
d['excl']=d.name.map(lambda n: bool(EXCL.search(n)))
d['kids']=d.name.map(lambda n: bool(KIDS.search(n)))
d['wmns']=d.name.map(lambda n: bool(WMNS.search(n)))
d['key']=d.name.map(model_key)
# drop out-of-window day-dated rows
bad=d[(d.prec!='year')&((d.rdate<'2023-01-01')|(d.rdate>'2027-06-30'))]
print('out of window',len(bad)); d=d.drop(bad.index)
d['ym']=d.rdate.dt.to_period('M').astype(str)
d.loc[d.prec=='year','ym']='undated-'+d.loc[d.prec=='year','date'].astype(str)
# collab base type
d['collab_base']=''
# debut flags (colorway rows, adult, non-excluded), burn-in: first seen on/after 2023-04
core=d[(~d.excl)&(~d.kids)&(d.prec!='year')].sort_values('rdate')
first=core[core.cls.isin(['A_new_model','B_perf_version'])].groupby(['b','key']).rdate.min()
d['debut']=False
for (b,k),dt in first.items():
    idx=core[(core.b==b)&(core.key==k)&(core.rdate==dt)].index[0]
    d.loc[idx,'debut']=True
d['burnin']=d.debut&(d.rdate<'2023-04-01')
d['debut_counted']=d.debut&~d.burnin
d.to_csv(OUT+'w8_release_rows_sbd.csv',index=False)
print(d.shape)
