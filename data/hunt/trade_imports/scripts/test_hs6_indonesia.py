"""Test: is the athletic-footwear supply pipeline into the US (HS 640411 + 640219, 'sports footwear') growing or
shrinking in 2026, and how does Indonesia (Nike 27% of footwear sourcing) export to the world vs Feng Tay?
Run after clean_comtrade.py has produced us_imports_hs6_athletic_monthly.csv and indonesia_exports_footwear_monthly.csv."""
import os
import pandas as pd

base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
pd.set_option('display.width', 220)
h = pd.read_csv(os.path.join(base, 'us_imports_hs6_athletic_monthly.csv')); h['hs'] = h.hs.astype(str)
h['y'] = h.month.str[:4]; h['m'] = h.month.str[5:].astype(int)
ath = {'640411', '640219'}
h['grp'] = h.hs.map(lambda x: 'athletic_640411_640219' if x in ath else 'other_hs6')
out = []
for (a, b) in ((1, 7), (1, 6), (5, 7)):
    w = h[(h.m >= a) & (h.m <= b)]
    for meas in ('value_usd', 'qty'):
        p = w.pivot_table(index=['partner', 'grp'], columns='y', values=meas, aggfunc='sum')
        for idx, r in p.iterrows():
            out.append(dict(window=f'{a:02d}-{b:02d}', measure=meas, partner=idx[0], grp=idx[1],
                            yoy_2026=round((r['2026'] / r['2025'] - 1) * 100, 1), vs_2024=round((r['2026'] / r['2024'] - 1) * 100, 1)))
o = pd.DataFrame(out)
o.to_csv(os.path.join(base, 'test_hs6_athletic_yoy.csv'), index=False)
print(o[o.window.isin(['01-06', '05-07'])].to_string())

# athletic share of US footwear import value, by year (Jan-Jun)
tot = pd.read_csv(os.path.join(base, 'us_imports_footwear_apparel_monthly.csv')); tot['hs'] = tot.hs.astype(str)
tot = tot[(tot.partner == 'World') & tot.hs.isin(['6402', '6403', '6404', '6405'])]
tot['y'] = tot.month.str[:4]; tot['m'] = tot.month.str[5:].astype(int)
t = tot[tot.m <= 6].groupby('y').value_usd.sum()
a = h[(h.partner == 'World') & (h.grp == 'athletic_640411_640219') & (h.m <= 6)].groupby('y').value_usd.sum()
print('Athletic share of US footwear import value, Jan-Jun:', (a / t * 100).round(1).to_dict())

ix = os.path.join(base, 'indonesia_exports_footwear_monthly.csv')
if os.path.exists(ix):
    i = pd.read_csv(ix); i['hs'] = i.hs.astype(str)
    s = i[(i.partner == 'World') & (i.hs == '64')].set_index('month').value_usd / 1e6
    u = i[(i.partner == 'USA') & (i.hs == '64')].set_index('month').value_usd / 1e6
    yy = pd.DataFrame({'id_fw_world_usd_m': s, 'id_fw_us_usd_m': u})
    yy = yy.join(yy.pct_change(12, fill_method=None).mul(100).add_suffix('_yoy'))
    m = pd.read_csv(os.path.join(base, 'nike_vs_industry_monthly.csv'), index_col=0)[['fengtay_yoy']]
    yy = yy.join(m)
    yy.round(2).to_csv(os.path.join(base, 'indonesia_vs_fengtay_monthly.csv'))
    print(yy.loc['2025-01':].round(1).to_string())
    for lab, (a_, b_) in {'Jan-Jun': ('01', '06'), 'Jul-Sep': ('07', '09'), 'Apr-Jun': ('04', '06')}.items():
        c26 = s.loc[f'2026-{a_}':f'2026-{b_}']; c25 = s.loc[f'2025-{a_}':f'2025-{b_}']
        n = min(len(c26), len(c25))
        if n:
            print(lab, 'Indonesia footwear exports to world YoY (months available %d): %.1f%%' % (n, (c26.iloc[:n].sum() / c25.iloc[:n].sum() - 1) * 100))
