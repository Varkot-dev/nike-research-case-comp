"""Test 1: US footwear category vs Nike North America footwear, by Nike fiscal quarter.
Nike FQ1=Jun-Aug, FQ2=Sep-Nov, FQ3=Dec-Feb, FQ4=Mar-May; FY named by year of May end."""
import pandas as pd, os
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
us = pd.read_csv('us_category_monthly_long.csv')
def fq(date):
    y, m = int(date[:4]), int(date[5:7])
    fy = y + 1 if m >= 6 else y
    q = {6:1,7:1,8:1,9:2,10:2,11:2,12:3,1:3,2:3,3:4,4:4,5:4}[m]
    return f'Q{q}FY{fy}'
us['fq'] = us.date.map(fq)
series = {'DSHURC':'pce_shoes_nominal','DSHURX':'pce_shoes_real','DSHURG':'pce_shoes_price','MRTSSM4482USN':'shoe_stores_nsa',
          'MRTSSM45111USN':'sporting_goods_stores_nsa','CUUR0000SEAE':'cpi_footwear_nsa','RSXFS':'retail_ex_food_sa','PCU448210448210':'ppi_shoe_store_margin','PCU451110451110':'ppi_sporting_goods_margin'}
out = []
for sid, name in series.items():
    s = us[us.series_id == sid].copy()
    agg = 'mean' if sid in ('DSHURG','CUUR0000SEAE','PCU448210448210','PCU451110451110','DSHURC','DSHURX') else 'sum'
    g = s.groupby('fq').agg(v=('value', agg), n=('value', 'size')).reset_index()
    g['series'] = name
    out.append(g)
q = pd.concat(out)
q['fy'] = q.fq.str[-4:].astype(int); q['qn'] = q.fq.str[1].astype(int)
q = q.sort_values(['series', 'fy', 'qn'])
q['prev'] = q.groupby(['series', 'qn']).v.shift(1)
q['prev_n'] = q.groupby(['series', 'qn']).n.shift(1)
q['yoy_pct'] = (q.v / q.prev - 1) * 100
q.loc[q.n != q.prev_n, 'yoy_pct'] = None  # partial quarter guard
# partial quarter handling: recompute same-months YoY for the latest partial quarter
wide = q.pivot_table(index='fq', columns='series', values='yoy_pct')
# Nike
u = pd.read_csv('raw/repo_nike_units_asp_tidy.csv')
u = u[(u.period_type == 'quarter') & (u.segment == 'North America') & (u.category == 'footwear')][['period', 'units_change_pct', 'asp_change_pct']]
u['nike_na_fw_rev_pct_approx'] = u.units_change_pct + u.asp_change_pct
u = u.rename(columns={'period': 'fq', 'units_change_pct': 'nike_na_fw_units_pct', 'asp_change_pct': 'nike_na_fw_asp_pp'})
f = pd.read_csv('raw/repo_nike_filing_facts.csv')
na = f[(f.metric == 'revenue_north_america') & f.period.str.match(r'^Q[1-4]FY20\d\d$')].drop_duplicates('period')[['period', 'value']]
na['fy'] = na.period.str[-4:].astype(int); na['qn'] = na.period.str[1].astype(int)
na = na.sort_values(['qn', 'fy']); na['nike_na_rev_yoy_pct'] = na.groupby('qn').value.pct_change() * 100
t = wide.join(u.set_index('fq'), how='left').join(na.set_index('period')[['nike_na_rev_yoy_pct']], how='left')
t['fy'] = t.index.str[-4:].astype(int); t['qn'] = t.index.str[1].astype(int)
t = t.sort_values(['fy', 'qn']); t = t[t.fy >= 2019]
t['units_gap_vs_pce_real'] = t.nike_na_fw_units_pct - t.pce_shoes_real
t['rev_gap_vs_pce_nominal'] = t.nike_na_fw_rev_pct_approx - t.pce_shoes_nominal
t['asp_gap_vs_pce_price'] = t.nike_na_fw_asp_pp - t.pce_shoes_price
t.round(2).to_csv('test1_us_category_vs_nike_na_quarterly.csv')
print(t.round(1)[t.fy >= 2023].to_string())
# cumulative since FY2024 (Q1FY24 .. Q1FY27) chain-linked
c = t[(t.fy >= 2024)].copy()
def chain(col):
    return ((1 + c[col] / 100).prod() - 1) * 100
print('\nCumulative 13 quarters Q1FY24..Q1FY27 (chain of YoY, rough):')
for col in ['nike_na_fw_units_pct', 'pce_shoes_real', 'nike_na_fw_rev_pct_approx', 'pce_shoes_nominal']:
    print(col, round(chain(col), 1))
