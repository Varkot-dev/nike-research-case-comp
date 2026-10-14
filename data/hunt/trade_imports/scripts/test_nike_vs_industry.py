"""Test: does Nike-specific shipment volume (Feng Tay USD revenue, ~88-90% Nike) diverge from industry
shipments out of the same origins (US and EU footwear imports from Vietnam/Indonesia/China, weighted by
Nike's FY26 10-K footwear sourcing mix 52/27/16), and from non-Nike shoemakers (Lai Yih, Fulgent Sun)?
Writes nike_vs_industry_monthly.csv and prints window summaries."""
import os, json
import pandas as pd

base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
raw = os.path.join(base, 'raw')

fx = pd.read_csv(os.path.join(raw, 'repo_fx_twd.csv'))[['month', 'twd_per_usd_avg']].set_index('month').twd_per_usd_avg


def tw(t):
    d = pd.DataFrame(json.load(open(os.path.join(raw, 'finmind', f'tw_{t}.json')))['data'])
    d['month'] = d.revenue_year.astype(str) + '-' + d.revenue_month.astype(int).map('{:02d}'.format)
    s = d.set_index('month').revenue.astype(float)
    return s / fx.reindex(s.index) / 1e6  # USD millions


sup = pd.DataFrame({'fengtay_usd_m': tw(9910), 'laiyih_usd_m': tw(6890), 'fulgent_usd_m': tw(9802), 'pouchen_usd_m': tw(9904)})

us = pd.read_csv(os.path.join(base, 'us_imports_footwear_apparel_monthly.csv')); us['hs'] = us.hs.astype(str)
fw = us[us.hs.isin(['6402', '6403', '6404', '6405'])].groupby(['month', 'partner']).value_usd.sum().unstack() / 1e6
W = {'Vietnam': 0.52, 'Indonesia': 0.27, 'China': 0.16}

eu = pd.read_csv(os.path.join(base, 'eu_imports_footwear_monthly.csv'))
eu = eu[(eu.hs.astype(str) == '64') & (eu.indicator == 'VALUE_IN_EUROS')].pivot_table(index='month', columns='partner', values='value') / 1e6

df = pd.DataFrame(index=sorted(set(sup.index) | set(fw.index)))
df = df.join(sup)
for c in ['World', 'Vietnam', 'Indonesia', 'China']:
    df[f'us_fw_{c.lower()}_usd_m'] = fw.get(c)
df['us_fw_nikemix_usd_m'] = sum(fw[c] * w for c, w in W.items()) / sum(W.values())
df['eu_fw_vn_id_cn_eur_m'] = eu[['VN', 'ID', 'CN']].sum(axis=1).reindex(df.index) if all(k in eu for k in ['VN', 'ID', 'CN']) else None
df.index.name = 'month'
yo = df.pct_change(12, fill_method=None) * 100
yo.columns = [c.replace('_usd_m', '_yoy').replace('_eur_m', '_yoy') for c in df.columns]
out = df.join(yo)
# Feng Tay books revenue at factory shipment; goods land in the US about one month later
out['us_nikemix_yoy_lead1'] = out['us_fw_nikemix_yoy'].shift(-1)
out['gap_ft_vs_us_nikemix'] = out['fengtay_yoy'] - out['us_nikemix_yoy_lead1']
out['gap_ft_vs_eu'] = out['fengtay_yoy'] - out['eu_fw_vn_id_cn_yoy']
out['gap_ft_vs_laiyih'] = out['fengtay_yoy'] - out['laiyih_yoy']
out = out[out.index >= '2019-01']
out.round(2).to_csv(os.path.join(base, 'nike_vs_industry_monthly.csv'))

pd.set_option('display.width', 220)
cols = ['fengtay_yoy', 'us_fw_nikemix_yoy', 'us_nikemix_yoy_lead1', 'us_fw_world_yoy', 'eu_fw_vn_id_cn_yoy', 'laiyih_yoy', 'fulgent_yoy', 'gap_ft_vs_us_nikemix', 'gap_ft_vs_eu']
print(out.loc['2024-07':, cols].round(1).to_string())

# windows and history of the gap
g = out['gap_ft_vs_us_nikemix'].dropna()
print('\nGap Feng Tay USD YoY minus US Nike-mix import YoY (t+1), by year:')
print(g.groupby(g.index.str[:4]).agg(['mean', 'std', 'count']).round(1))
recent = g.loc['2026-05':'2026-07']
hist = g.loc['2022-01':'2025-12']
print('recent (May-Jul 2026 FT months):', recent.round(1).to_dict(), 'mean', round(recent.mean(), 1))
print('hist 2022-2025 mean %.1f sd %.1f; share of hist months below recent mean: %.0f%%' % (hist.mean(), hist.std(), (hist < recent.mean()).mean() * 100))
# rolling 3m gap percentile
r3 = g.rolling(3).mean()
print('3m rolling gap, latest:', round(r3.iloc[-1], 1), r3.index[-1], 'percentile vs 2019-2025: %.0f%%' % ((r3.loc[:'2025-12'] < r3.iloc[-1]).mean() * 100))
# level correlation check: does Feng Tay track Nike-mix imports historically?
c = out[['fengtay_yoy', 'us_nikemix_yoy_lead1']].dropna().loc['2019-01':'2025-12']
print('corr FT yoy vs US nikemix yoy (t+1), 2019-2025:', round(c.corr().iloc[0, 1], 2), 'n', len(c))
