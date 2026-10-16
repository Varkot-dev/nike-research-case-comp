import sys; sys.path.insert(0,'/tmp/claude-0/scr')
import pandas as pd,re
from classify2 import *
d=pd.read_csv('/tmp/claude-0/scr/sr_news_release.csv')
d['txt']=d.slug.str.replace('-',' ')
d['txt']=d.txt.str.replace(r'\brelease dates?\b.*$','',regex=True)
d['txt']=d.txt.str.replace(r'^(where to buy|official look|first look) ','',regex=True)
def br(t):
    if re.search(r'\bair jordan\b|\bjordan\b|\baj ?\d',t): return 'Jordan'
    if re.search(r'\bnike\b|\bnocta\b',t): return 'Nike'
    if re.search(r'\badidas\b',t): return 'adidas'
    if re.search(r'new balance',t): return 'New Balance'
    if re.search(r'\basics\b',t): return 'ASICS'
    if re.search(r'\bhoka\b',t): return 'Hoka'
    if re.search(r'(^| )on (cloud|running)|cloudtilt|cloudmonster|cloudsurfer|cloudboom|cloudnova|cloudeclipse',t): return 'On'
    if re.search(r'\bpuma\b',t): return 'Puma'
    return 'Other'
d['b']=d.txt.map(br)
def cl(r):
    t=r.txt
    if r.b in('Nike','Jordan'):
        t2=('nike '+t) if r.b=='Nike' and 'nike' not in t else t
        return nike_class(t2)
    if r.b in('adidas','New Balance','ASICS'): return peer_class(t,r.b)
    return 'n/a'
d['cls']=d.apply(cl,axis=1)
d['excl']=d.txt.map(lambda n: bool(EXCL.search(n)))
d['kids']=d.txt.map(lambda n: bool(re.search(r'\bgs\b|\bps\b|\btd\b|\bkids\b',n)))
d.to_csv('/home/user/nike-research-case-comp/data/hunt/w8_launch_newness/w8_sr_news_release_articles.csv',index=False)
d['pub']=pd.to_datetime(d.pub)
# target window: Oct Y .. Jun Y+1
def tgt(r):
    y=r.target_year; m=r.target_month; s=r.target_season
    if pd.isna(y): return None
    y=int(y)
    if pd.notna(m): return (y,int(m))
    return (y,{'spring':4,'summer':7,'fall':10,'autumn':10,'holiday':11,'winter':1}.get(s,None))
d['tg']=d.apply(tgt,axis=1)
def vintage(r):
    if r.tg is None or r.tg[1] is None: return None
    y,m=r.tg
    # holiday vintage V covers Oct V .. Jun V+1
    if m>=10: V=y
    elif m<=6: V=y-1
    else: return None
    return V
d['vint']=d.apply(vintage,axis=1)
x=d[(d.vint.notna())&(d.pub.dt.month*100+d.pub.dt.day<=1015)&(d.pub.dt.year==d.vint)&(~d.excl)&(~d.kids)&d.b.isin(['Nike','Jordan'])]
print(x.groupby(['vint','b','cls']).size().unstack(fill_value=0).to_string())
t=x.groupby(['vint','cls']).size().unstack(fill_value=0); t['tot']=t.sum(axis=1); t['A+B']=((t.A_new_model+t.B_perf_version)/t.tot).round(3); t['C']=(t.C_retro_classic/t.tot).round(3);t['D']=(t.D_collab/t.tot).round(3)
print(t.to_string())
# overall pub-month counts
y=d[(~d.excl)&d.b.isin(['Nike','Jordan'])]
y['hy']=y.pub.dt.year.astype(str)+'H'+((y.pub.dt.month>6)+1).astype(str)
tt=y.groupby(['hy','cls']).size().unstack(fill_value=0); tt['tot']=tt.sum(axis=1); print(tt.to_string())
