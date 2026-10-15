"""BOL test: holiday-season (Jul-Sep) bill-of-lading counts, 2026 vs 2025, Nike-named consignees vs peers.
Only series whose name is visible in both years are comparable; coverage breaks are flagged."""
import os
import pandas as pd

base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
d = pd.read_csv(os.path.join(base, 'importinfo_monthly_bols.csv'))
d['y'] = d.month.str[:4]; d['m'] = d.month.str[5:].astype(int)
p = d.pivot_table(index='month', columns='slug', values='bols', aggfunc='sum').fillna(0)
groups = {
    'Nike Canada (consignee visible)': ['nike-canada-corp'],
    'Nike USA (consignee, mostly masked since 2022-11)': ['nike-usa-inc'],
    'Nike factories as shippers (VN+ID)': ['feng-tay-enterprises-co-ltd', 'pt-feng-tay-indonesia-enterprises', 'chang-shin-vietnam-co-ltd',
                                           'pt-chang-shin-indonesia', 'freetrend-industrial-a-vietnam-co-ltd', 'pt-pratama-abadi-industri',
                                           'pt-nikomas-gemilang', 'lotus-footwear-enterprises-limited'],
    'APL Logistics VN+ID (Nike forwarder)': ['apl-logistics-vietnam-company-ltd', 'branch-of-apl-logistics-vietnam', 'pt-apl-logistics'],
    'Peer: adidas America': ['adidas-america-inc'],
    'Peer: New Balance': ['new-balance-athletics-inc'],
    'Peer: Vans (VF)': ['vans-a-division-of-vf-outdoor-llc'],
    'Peer: Puma NA': ['puma-north-america-inc'],
    'Peer: Under Armour': ['under-armour-inc'],
}
rows = []
for g, slugs in groups.items():
    s = p.reindex(columns=slugs).fillna(0).sum(axis=1)
    def win(y, a, b):
        return s.loc[f'{y}-{a:02d}':f'{y}-{b:02d}'].sum()
    r = dict(group=g)
    for y in (2023, 2024, 2025, 2026):
        r[f'jul_sep_{y}'] = win(y, 7, 9); r[f'jan_jun_{y}'] = win(y, 1, 6)
    r['jul_sep_yoy_pct'] = round((r['jul_sep_2026'] / r['jul_sep_2025'] - 1) * 100, 1) if r['jul_sep_2025'] else None
    r['jan_jun_yoy_pct'] = round((r['jan_jun_2026'] / r['jan_jun_2025'] - 1) * 100, 1) if r['jan_jun_2025'] else None
    # seasonal loading ratio: Jul-Sep monthly average over Jan-Jun monthly average, same year
    for y in (2024, 2025, 2026):
        r[f'load_ratio_{y}'] = round((r[f'jul_sep_{y}'] / 3) / (r[f'jan_jun_{y}'] / 6), 2) if r[f'jan_jun_{y}'] else None
    # coverage flag: any month with zero in 2024-01..2026-09
    r['months_zero_2024_2026'] = int((s.loc['2024-01':'2026-09'] == 0).sum())
    rows.append(r)
o = pd.DataFrame(rows)
o.to_csv(os.path.join(base, 'test_bol_holiday.csv'), index=False)
pd.set_option('display.width', 250)
print(o[['group', 'jul_sep_2024', 'jul_sep_2025', 'jul_sep_2026', 'jul_sep_yoy_pct', 'jan_jun_yoy_pct', 'load_ratio_2024', 'load_ratio_2025', 'load_ratio_2026', 'months_zero_2024_2026']].to_string())
print(p['nike-canada-corp'].loc['2023-01':].astype(int).to_dict())
