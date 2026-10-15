"""Industry baseline: US footwear imports YoY by origin, value and pairs, windows Jan-Jul and May-Jul."""
import pandas as pd, os
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
d = pd.read_csv(os.path.join(base, 'us_imports_footwear_apparel_monthly.csv')); d['hs'] = d.hs.astype(str)
d['y'] = d.month.str[:4]; d['m'] = d.month.str[5:].astype(int)
out = []
for hsset, lab in ((['6402', '6403', '6404', '6405'], 'footwear_6402-6405'), (['6404'], '6404_textile_upper'), (['6402'], '6402_rubber_plastic'), (['61', '62'], 'apparel_61_62')):
    x = d[d.hs.isin(hsset)]
    for (a, b) in ((1, 7), (5, 7), (7, 7)):
        w = x[(x.m >= a) & (x.m <= b)]
        for meas in ('value_usd', 'qty'):
            if meas == 'qty' and lab == 'apparel_61_62':
                continue
            p = w.pivot_table(index='partner', columns='y', values=meas, aggfunc='sum')
            for partner in p.index:
                r = p.loc[partner]
                if meas == 'qty' and partner == 'World':
                    continue  # World qty missing for Jul 2026 in Comtrade
                out.append(dict(series=lab, window=f'{a:02d}-{b:02d}', measure=meas, partner=partner,
                                v2024=r.get('2024'), v2025=r.get('2025'), v2026=r.get('2026'),
                                yoy_2026_pct=round((r.get('2026') / r.get('2025') - 1) * 100, 1),
                                vs2024_pct=round((r.get('2026') / r.get('2024') - 1) * 100, 1)))
o = pd.DataFrame(out); o.to_csv(os.path.join(base, 'test_industry_yoy.csv'), index=False)
pd.set_option('display.width', 200)
print(o[(o.series == 'footwear_6402-6405')].drop(columns=['v2024', 'v2025', 'v2026']).to_string())
print(o[(o.series.isin(['6404_textile_upper', 'apparel_61_62'])) & (o.window == '01-07')].drop(columns=['v2024', 'v2025', 'v2026']).to_string())
