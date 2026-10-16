import pandas as pd,re
OUT='/home/user/nike-research-case-comp/data/hunt/w8_launch_newness/'
d=pd.read_csv('/tmp/claude-0/scr/rr_shoes2.csv',header=None,names=['u','st','rel','pub','mod','title'])
d=d[d.title.str.contains('Review',na=False)].copy()
BR={'nike':'Nike','adidas':'adidas','new-balance':'New Balance','asics':'ASICS','hoka':'Hoka','on':'On','brooks':'Brooks','saucony':'Saucony','puma':'Puma','mizuno':'Mizuno','salomon':'Salomon','altra':'Altra','skechers':'Skechers','under-armour':'Under Armour','topo-athletic':'Topo','reebok':'Reebok','li-ning':'Li-Ning','anta':'Anta'}
def br(u):
    s=u.strip('/')
    for k in sorted(BR,key=len,reverse=True):
        if s.startswith(k+'-'): return BR[k],s[len(k)+1:]
    return 'Other',s
d[['brand','slug']]=d.u.apply(lambda u: pd.Series(br(u)))
def ver(slug):
    m=re.search(r'-(?:v-?)?(\d+)(?:-(?:plus|pro|max|gtx|gore-tex|trail|wide))?$',slug)
    n=int(m.group(1)) if m else None
    stem=re.sub(r'-(?:v-?)?\d+(-(?:plus|pro|max|gtx|gore-tex|trail|wide))?$','',slug)
    return stem,n
d[['stem','num']]=d.slug.apply(lambda s: pd.Series(ver(s)))
def mon(r):
    if isinstance(r.rel,str) and re.match(r'[A-Za-z]{3} \d{4}$',r.rel): return pd.to_datetime(r.rel,format='%b %Y'),'release_date_field'
    if isinstance(r.pub,str) and r.pub: return pd.to_datetime(r.pub),'review_published'
    return pd.NaT,'none'
x=d.apply(mon,axis=1); d['date']=[a for a,b in x]; d['date_basis']=[b for a,b in x]
d=d[d.date.notna()].copy()
# class: numbered >=2 => B (new version), else A (new model/variant name); numbered with num=1 => A
d['cls']=d.num.apply(lambda n:'B_new_version' if (pd.notna(n) and n>=2) else 'A_new_model')
d['ym']=d.date.dt.to_period('M').astype(str); d['hy']=d.date.dt.year.astype(str)+'H'+((d.date.dt.month>6)+1).astype(str)
d.to_csv(OUT+'w8_runrepeat_running_shoes.csv',index=False)
y=d[(d.date>='2023-01-01')&(d.date<='2026-10-16')]
print(len(d),len(y), y.date_basis.value_counts().to_dict())
t=y.groupby(['hy','brand']).size().unstack(fill_value=0)
core=['Nike','adidas','New Balance','ASICS','Hoka','On']
t['six']=t[core].sum(axis=1); t['all']=t.drop(columns=['six']).sum(axis=1)
print(t[core+['Brooks','Saucony','six','all']].to_string())
t2=y.groupby(['hy','brand','cls']).size().unstack(['brand','cls'],fill_value=0)
for b in ['Nike']:
    print(y[y.brand==b].groupby(['hy','cls']).size().unstack(fill_value=0))
y2=y[y.brand.isin(core)]
sh=y2.groupby(['hy']).apply(lambda s: pd.Series(dict(nike=(s.brand=='Nike').sum(),six=len(s),nike_share=round((s.brand=='Nike').mean(),3),nike_A=((s.brand=='Nike')&(s.cls=='A_new_model')).sum(),six_A=(s.cls=='A_new_model').sum(),nike_B=((s.brand=='Nike')&(s.cls=='B_new_version')).sum(),six_B=(s.cls=='B_new_version').sum())))
sh.to_csv(OUT+'w8_runrepeat_nike_share_by_halfyear.csv'); print(sh.to_string())
print(y[(y.brand=='Nike')&(y.date>='2025-01-01')][['u','date','date_basis','cls']].sort_values('date').to_string())
# coverage vs Marathon Handbook 2025
print(y[(y.date.dt.year==2025)].groupby('brand').size().reindex(core))
