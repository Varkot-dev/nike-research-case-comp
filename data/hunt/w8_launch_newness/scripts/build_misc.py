import sys; sys.path.insert(0,'/tmp/claude-0/scr')
import pandas as pd,re,json
from classify2 import *
OUT='/home/user/nike-research-case-comp/data/hunt/w8_launch_newness/'
# 1 SR vintage
d=pd.read_csv(OUT+'w8_sr_news_release_articles.csv'); d['pub']=pd.to_datetime(d.pub)
def tgt(r):
    if pd.isna(r.target_year): return None
    y=int(r.target_year); m=r.target_month
    if pd.notna(m): return (y,int(m))
    return (y,{'spring':4,'summer':7,'fall':10,'autumn':10,'holiday':11,'winter':1}.get(r.target_season))
d['tg']=d.apply(tgt,axis=1)
def vint(r):
    if r.tg is None or r.tg[1] is None: return None
    y,m=r.tg
    if m>=10: return y
    if m<=6: return y-1
    return None
d['vint']=d.apply(vint,axis=1)
x=d[d.vint.notna()&((d.pub.dt.month*100+d.pub.dt.day)<=1015)&(d.pub.dt.year==d.vint)&(~d.excl)&(~d.kids)&d.b.isin(['Nike','Jordan'])]
t=x.groupby(['vint','cls']).size().unstack(fill_value=0).reset_index()
t['total']=t[[c for c in t.columns if c!='vint']].sum(axis=1)
t['new_AB_share']=((t.get('A_new_model',0)+t.get('B_perf_version',0))/t.total).round(3)
t['retro_C_share']=(t.get('C_retro_classic',0)/t.total).round(3)
t['window']=t.vint.astype(int).astype(str)+'-10 to '+(t.vint+1).astype(int).astype(str)+'-06'
t.to_csv(OUT+'w8_sr_announced_by_oct15_vintage.csv',index=False); print(t.to_string())
# SR articles per publish half-year by brand (coverage drift)
d['hy']=d.pub.dt.year.astype(str)+'H'+((d.pub.dt.month>6)+1).astype(str)
cov=d[d.pub>='2022-07-01'].groupby(['hy','b']).size().unstack(fill_value=0)
cov.to_csv(OUT+'w8_sr_news_release_articles_by_halfyear_brand.csv'); print(cov[['Nike','Jordan','adidas','New Balance','ASICS','Hoka','On','Puma','Other']].to_string())
# 2 SNKRS live snapshot
t=open('/tmp/claude-0/scr/nl.html').read()
m=re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>',t,re.S)
st=json.loads(json.loads(m.group(1))['props']['pageProps']['initialState'])
pr=st['product']['products']['data']['items']
rows=[]
for k,v in pr.items():
    n=v.get('title'); b=brand_of(n) if not re.search('Nike|Jordan',n) else brand_of(n)
    rows.append(dict(title=n,style_color=v.get('styleColor'),launch_utc=v.get('commerceStartDate'),price_usd=v.get('fullPrice'),genders='|'.join(v.get('genders',[])),cls=(nike_class(n) if b in('Nike','Jordan') else 'n/a'),brand=b,tag='OPENED nike.com/launch/upcoming 2026-10-16'))
pd.DataFrame(rows).to_csv(OUT+'w8_snkrs_upcoming_snapshot_2026-10-16.csv',index=False)
print(pd.DataFrame(rows)[['title','launch_utc','cls','brand']].to_string())
# 3 SNKRS feed product threads by publish month
f=json.load(open('/tmp/claude-0/scr/feed_base.json'))
rows=[]
for o in f:
    pc=o['publishedContent']; p=pc['properties']
    rows.append(dict(id=o['id'],title=p.get('title'),threadType=p.get('threadType'),subType=pc.get('subType'),publishStart=pc['publishStartDate'][:10],styles=','.join(x['styleColor'] for x in p.get('products',[]) or [])))
pd.DataFrame(rows).to_csv(OUT+'w8_snkrs_feed_threads_partial.csv',index=False)
