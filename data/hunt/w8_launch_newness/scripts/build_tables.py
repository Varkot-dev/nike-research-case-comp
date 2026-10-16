import sys; sys.path.insert(0,'/tmp/claude-0/scr')
import pandas as pd,re
from classify2 import *
OUT='/home/user/nike-research-case-comp/data/hunt/w8_launch_newness/'
d=pd.read_csv(OUT+'w8_release_rows_sbd.csv'); d['rdate']=pd.to_datetime(d.rdate)
# collab base class
def base(n):
    t=re.split(r'\s+x\s+',n,flags=re.I)[-1]
    t2=t if re.search(r'nike|jordan',t,re.I) else 'Nike '+t
    return nike_class(t2) if not COLLAB.search(t2) else 'U_unmatched'
d['collab_base']=''
m=(d.cls=='D_collab')&d.b.isin(['Nike','Jordan'])
d.loc[m,'collab_base']=d.loc[m,'name'].map(base)
d['segment']=''
bb=r'lebron|\bkd\b|\bja \d|book|sabrina|gt (cut|jump|hustle|future)|giannis|freak|luka|tatum|zion|air jordan (3[6-9]|4\d)|a.one|a.two|caitlin|kobe nxt|\bwemb'
d.loc[d.b.isin(['Nike','Jordan']),'segment']=d.loc[d.b.isin(['Nike','Jordan']),'name'].map(lambda n:'basketball_signature' if re.search(bb,n.lower().replace('’',"'")) else ('running_training' if re.search(r'pegasus|vomero (?!5)|alphafly|vaporfly|structure|invincible|zoom fly|infinity|winflo|metcon|streakfly|ultrafly|zegama|kiger|journey|rival',n.lower()) else 'lifestyle_other'))
d['ym_str']=d.ym
d.to_csv(OUT+'w8_release_rows_sbd.csv',index=False)
# monthly counts (SBD)
x=d[(d.prec!='year')&(d.rdate>='2023-01-01')&(d.rdate<='2027-06-30')&~d.excl].copy()
x['month']=x.rdate.dt.to_period('M').astype(str)
g=x.groupby(['month','src','b','cls']).agg(rows_all=('name','size'),rows_adult=('kids',lambda s:(~s).sum()),rows_wmns=('wmns','sum'),debuts=('debut_counted','sum')).reset_index()
g['source']='SBD'; g['status']=g.month.map(lambda m:'announced_forward' if m>='2026-10' else 'realized_or_scheduled')
g.to_csv(OUT+'w8_monthly_counts_sbd.csv',index=False)
# half-year
x['hy']=x.rdate.dt.year.astype(str)+'H'+((x.rdate.dt.month>6)+1).astype(str)
x['ret_eq']=(x.cls=='C_retro_classic')|((x.cls=='D_collab')&(x.collab_base=='C_retro_classic'))
x['new_eq']=x.cls.isin(['A_new_model','B_perf_version'])|((x.cls=='D_collab')&x.collab_base.isin(['A_new_model','B_perf_version']))
ad=x[~x.kids&x.b.isin(['Nike','Jordan'])&(x.rdate<='2026-12-31')]
rows=[]
for (hy,b),s in ad.groupby(['hy','b']):
    rows.append(dict(half_year=hy,brand=b,rows=len(s),A_new_model=(s.cls=='A_new_model').sum(),B_perf_version=(s.cls=='B_perf_version').sum(),C_retro_classic=(s.cls=='C_retro_classic').sum(),D_collab=(s.cls=='D_collab').sum(),U_unmatched=(s.cls=='U_unmatched').sum(),collab_on_retro_base=((s.cls=='D_collab')&(s.collab_base=='C_retro_classic')).sum(),A_debuts=((s.cls=='A_new_model')&s.debut_counted).sum(),B_version_debuts=((s.cls=='B_perf_version')&s.debut_counted).sum(),new_eq_share=round(s.new_eq.mean(),3),retro_eq_share=round(s.ret_eq.mean(),3),new_to_retro_ratio=round(s.new_eq.sum()/max(s.ret_eq.sum(),1),3)))
h=pd.DataFrame(rows); h.to_csv(OUT+'w8_halfyear_nike_jordan_sbd.csv',index=False)
print(h.to_string())
nj=ad.groupby('hy').agg(rows=('name','size'),new_eq=('new_eq','sum'),ret_eq=('ret_eq','sum'))
nj['new_eq_share']=(nj.new_eq/nj.rows).round(3); nj['ratio']=(nj.new_eq/nj.ret_eq).round(3); print(nj)
# segment split of B for Nike
print(ad[ad.cls=='B_perf_version'].groupby(['hy','segment']).size().unstack(fill_value=0))
print(ad[ad.b=='Nike'].groupby(['hy','segment']).size().unstack(fill_value=0))
