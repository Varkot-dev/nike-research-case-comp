import pandas as pd
OUT='/home/user/nike-research-case-comp/data/hunt/w8_launch_newness/'
frames=[]
s=pd.read_csv(OUT+'w8_monthly_counts_sbd.csv')
s=s[s.b.isin(['Nike','Jordan','adidas','New Balance','ASICS'])]
frames.append(pd.DataFrame(dict(month=s.month,source='SBD calendar (main+Jordan page)',brand=s.b,class_=s.cls,rows_all=s.rows_all,rows_adult=s.rows_adult,rows_womens=s.rows_wmns,new_model_debuts=s.debuts,basis='release date (announced if >=2026-10)',tag='OPENED')))
r=pd.read_csv(OUT+'w8_runrepeat_running_shoes.csv')
r=r[(r.date>='2023-01-01')&r.brand.isin(['Nike','adidas','New Balance','ASICS','Hoka','On'])]
g=r.groupby(['ym','brand','cls']).size().reset_index(name='n')
frames.append(pd.DataFrame(dict(month=g.ym,source='RunRepeat running catalog',brand=g.brand,class_=g.cls,rows_all=g.n,rows_adult=g.n,rows_womens=0,new_model_debuts=g.n,basis='release-date field if present else review-published date',tag='OPENED')))
a=pd.read_csv(OUT+'w8_sr_news_release_articles.csv'); a['pub']=pd.to_datetime(a.pub)
a=a[(a.pub>='2023-01-01')&a.b.isin(['Nike','Jordan','adidas','New Balance','ASICS','Hoka','On'])&~a.excl&~a.kids]
a['month']=a.pub.dt.to_period('M').astype(str)
g=a.groupby(['month','b','cls']).size().reset_index(name='n')
frames.append(pd.DataFrame(dict(month=g.month,source='SoleRetriever release-date news articles (sitemap slugs)',brand=g.b,class_=g.cls,rows_all=g.n,rows_adult=g.n,rows_womens=0,new_model_debuts=0,basis='article lastmod (announcement month, not release month)',tag='OPENED')))
nk=pd.read_csv(OUT+'w8_release_rows_nicekicks_upcoming.csv'); nk['rdate']=pd.to_datetime(nk.rdate)
nk=nk[nk.b.isin(['Nike','Jordan','adidas','New Balance','ASICS'])&~nk.excl]
nk['month']=nk.rdate.dt.to_period('M').astype(str)
g=nk.groupby(['month','b','cls']).agg(n=('name','size'),ad=('kids',lambda s:(~s).sum())).reset_index()
frames.append(pd.DataFrame(dict(month=g.month,source='Nice Kicks upcoming calendar (snapshot 2026-10-16)',brand=g.b,class_=g.cls,rows_all=g.n,rows_adult=g.ad,rows_womens=0,new_model_debuts=0,basis='announced release date',tag='OPENED')))
out=pd.concat(frames); out=out.sort_values(['source','month','brand','class_'])
out.to_csv(OUT+'W8_launch_monthly_counts.csv',index=False)
out.to_csv('/home/user/nike-research-case-comp/research_notes/Wave 3/W8_launch_monthly_counts.csv',index=False)
print(out.shape, out.source.value_counts().to_dict())
