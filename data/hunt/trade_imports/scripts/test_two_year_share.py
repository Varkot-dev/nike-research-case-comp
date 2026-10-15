"""Two-year stack test: Nike's main shoemaker (Feng Tay, USD) vs the athletic footwear supply pipeline,
H1 2026 vs H1 2024 and vs H1 2025, plus Jul-Sep windows. Removes the 2025 base effect (tariff front-loading by
other brands in H1 2025 and Nike's own H2 2025 strength). Writes test_two_year_share.csv."""
import os
import pandas as pd

base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
m = pd.read_csv(os.path.join(base, 'nike_vs_industry_monthly.csv'), index_col=0)
h = pd.read_csv(os.path.join(base, 'us_imports_hs6_athletic_monthly.csv')); h['hs'] = h.hs.astype(str)
ath = h[(h.partner == 'World') & h.hs.isin(['640411', '640219'])].groupby('month')[['value_usd', 'qty']].sum()
eu = pd.read_csv(os.path.join(base, 'eu_imports_footwear_monthly.csv'))
eu6404 = eu[(eu.hs.astype(str) == '6404') & (eu.indicator == 'VALUE_IN_EUROS') & eu.partner.isin(['VN', 'ID', 'CN'])].groupby('month').value.sum()
eu64 = eu[(eu.hs.astype(str) == '64') & (eu.indicator == 'VALUE_IN_EUROS') & eu.partner.isin(['VN', 'ID', 'CN'])].groupby('month').value.sum()
ind = pd.read_csv(os.path.join(base, 'indonesia_exports_footwear_monthly.csv')); ind['hs'] = ind.hs.astype(str)
idw = ind[(ind.partner == 'World') & (ind.hs == '64')].set_index('month').value_usd

series = {
    'Feng Tay revenue USD (Nike ~88%)': m.fengtay_usd_m,
    'Pou Chen revenue USD (multi-brand)': m.pouchen_usd_m,
    'Fulgent Sun revenue USD (On, others)': m.fulgent_usd_m,
    'US imports footwear 6402-6405, World, USD': m.us_fw_world_usd_m,
    'US imports footwear, Nike sourcing mix VN52/ID27/CN16, USD': m.us_fw_nikemix_usd_m,
    'US imports sports footwear 640411+640219, World, USD': ath.value_usd,
    'US imports sports footwear 640411+640219, World, pairs': ath.qty,
    'EU imports 6404 from VN+ID+CN, EUR': eu6404,
    'EU imports 64 from VN+ID+CN, EUR': eu64,
    'Indonesia footwear exports to world, USD': idw,
}


def ratio(s, a, b, pa, pb):
    x, y = s.loc[a:b], s.loc[pa:pb]
    if x.count() != y.count() or x.count() == 0:
        return None
    return round((x.sum() / y.sum() - 1) * 100, 1)


rows = []
for name, s in series.items():
    rows.append(dict(series=name,
                     h1_26_vs_h1_25=ratio(s, '2026-01', '2026-06', '2025-01', '2025-06'),
                     h1_26_vs_h1_24=ratio(s, '2026-01', '2026-06', '2024-01', '2024-06'),
                     h2_25_vs_h2_24=ratio(s, '2025-07', '2025-12', '2024-07', '2024-12'),
                     jul_26_vs_jul_24=ratio(s, '2026-07', '2026-07', '2024-07', '2024-07')))
o = pd.DataFrame(rows)
o.to_csv(os.path.join(base, 'test_two_year_share.csv'), index=False)
pd.set_option('display.width', 220)
print(o.to_string())
ft = o.set_index('series').loc['Feng Tay revenue USD (Nike ~88%)', 'h1_26_vs_h1_24']
others = o[~o.series.str.contains('Feng Tay|Pou Chen|Fulgent')].set_index('series')['h1_26_vs_h1_24']
print('\nFeng Tay H1 two-year minus each industry series (pts):')
print((ft - others).round(1).to_string())
