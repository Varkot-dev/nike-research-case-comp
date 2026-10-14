"""Tests 2-4: China category trend, US shoe-store retail margin, international category vs Nike.
Run: python3 -I scripts/tests_2_to_4.py"""
import pandas as pd, os
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
out = []
# ---- Test 2: China category
c = pd.read_csv('china_nbs_retail_categories_monthly.csv')
p = c.pivot_table(index=['year', 'month'], columns='series', values='month_yoy')
y = c.pivot_table(index=['year', 'month'], columns='series', values='ytd_yoy')
p = p.join(y, rsuffix='_ytd')
for s in ['sports_recreation', 'apparel_footwear', 'total_retail', 'above_size_goods']:
    p[s + '_2yr'] = None
for (yr, mo) in p.index:
    for s in ['sports_recreation', 'apparel_footwear', 'total_retail', 'above_size_goods']:
        if (yr - 1, mo) in p.index and pd.notna(p.loc[(yr, mo), s]) and pd.notna(p.loc[(yr - 1, mo), s]):
            p.loc[(yr, mo), s + '_2yr'] = round(((1 + p.loc[(yr, mo), s] / 100) * (1 + p.loc[(yr - 1, mo), s] / 100) - 1) * 100, 1)
p['sports_minus_total'] = p.sports_recreation - p.total_retail
p.to_csv('test2_china_category_monthly.csv')
def avg(s, months, yr=2026):
    return round(pd.to_numeric(p.loc[[(yr, m) for m in months], s]).mean(), 1)
for s in ['sports_recreation', 'sports_recreation_2yr', 'apparel_footwear', 'apparel_footwear_2yr', 'total_retail', 'sports_minus_total']:
    out.append(('T2', s, 'Mar-May 2026 avg', avg(s, [3, 4, 5]))); out.append(('T2', s, 'Jun-Aug 2026 avg', avg(s, [6, 7, 8])))
    out.append(('T2', s, 'Jun-Aug 2025 avg', avg(s, [6, 7, 8], 2025)))
# ---- Test 3: shoe-store retail margin PPI
u = pd.read_csv('us_category_monthly_long.csv')
m = u[u.series_id.isin(['PCU448210448210', 'PCU451110451110', 'PCU44814481', 'CUUR0000SEAE', 'PCU316210316210'])].pivot(index='date', columns='series_id', values='value')
yo = (m / m.shift(12) - 1) * 100
t3 = m.join(yo, rsuffix='_yoy'); t3.round(2).to_csv('test3_us_retail_margin_ppi_monthly.csv')
full = pd.read_csv('raw/fred_PCU448210448210.csv'); full.columns = ['date', 'v']; full.v = pd.to_numeric(full.v, errors='coerce')
out.append(('T3', 'shoe_store_margin_index', 'Aug 2026 level', round(full.v.iloc[-1], 1)))
out.append(('T3', 'shoe_store_margin_index', 'lowest level before 2026 (since Jun 2002)', round(full[full.date < '2026-01-01'].v.min(), 1)))
out.append(('T3', 'shoe_store_margin_index', 'months below 100 before 2026', int((full[full.date < '2026-01-01'].v < 100).sum())))
out.append(('T3', 'shoe_store_margin_index', 'months below 100 in 2026', int((full[full.date >= '2026-01-01'].v < 100).sum())))
for s in ['PCU448210448210', 'PCU451110451110', 'PCU44814481', 'CUUR0000SEAE', 'PCU316210316210']:
    out.append(('T3', s + '_yoy', 'Jun-Aug 2026 avg', round(yo.loc['2026-06':'2026-08', s].mean(), 1)))
# ---- Test 4: international category
ca = pd.read_csv('canada_retail_by_naics_monthly.csv')
ca = ca[(ca.adjustment == 'Unadjusted') & (ca.sales_type == 'Total retail sales')].pivot(index='ref_date', columns='naics', values='value_cad_thousands')
cy = (ca / ca.shift(12) - 1) * 100
for col in ca.columns:
    if any(k in col for k in ['[4582]', '[459A]', '[4581]']):
        out.append(('T4', 'Canada ' + col, 'Jun-Jul 2026 YoY (sum)', round((ca.loc[['2026-06', '2026-07'], col].sum() / ca.loc[['2025-06', '2025-07'], col].sum() - 1) * 100, 1)))
        out.append(('T4', 'Canada ' + col, 'Jan-Jul 2026 YoY (sum)', round((ca.loc['2026-01':'2026-07', col].sum() / ca.loc['2025-01':'2025-07', col].sum() - 1) * 100, 1)))
uk = pd.read_csv('uk_ons_retail_monthly.csv'); uk = uk[uk.cdid == 'IDOG'].set_index('date').value
out.append(('T4', 'UK textile clothing footwear stores volume YoY (IDOG)', 'Jun-Aug 2026 avg', round(uk.loc['2026-06':'2026-08'].mean(), 1)))
out.append(('T4', 'UK textile clothing footwear stores volume YoY (IDOG)', 'Jan-Aug 2026 avg', round(uk.loc['2026-01':'2026-08'].mean(), 1)))
f = pd.read_csv('raw/repo_nike_filing_facts.csv')
for met in ['revenue_emea', 'revenue_greater_china', 'revenue_north_america']:
    s = f[(f.metric == met)].drop_duplicates('period').set_index('period').value
    out.append(('T4', 'Nike ' + met + ' reported USD YoY', 'Q1FY2027', round((s['Q1FY2027'] / s['Q1FY2026'] - 1) * 100, 1)))
    out.append(('T4', 'Nike ' + met + ' reported USD 2yr', 'Q1FY2027 vs Q1FY2025', round((s['Q1FY2027'] / s['Q1FY2025'] - 1) * 100, 1)))
r = pd.DataFrame(out, columns=['test', 'series', 'window', 'value'])
r.to_csv('tests_2_to_4_results.csv', index=False)
print(r.to_string())
