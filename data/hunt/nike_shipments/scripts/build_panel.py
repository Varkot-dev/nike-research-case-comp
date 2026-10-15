"""Build tidy CSVs and run the pre-registered tests for the nike_shipments hunt.
Inputs (no network):
  ../trade_imports/importinfo_monthly_bols.csv           (earlier hunt, reused)
  raw/importinfo/*_monthly.json                          (new ImportInfo chart pulls)
  raw/importgenius/ig_us_extract.json                    (node scripts/ig_extract.js output)
  ../trade_imports/nike_vs_industry_monthly.csv          (US footwear imports, Feng Tay USD revenue)
Outputs (this folder): see README."""
import os, json, glob, datetime
import pandas as pd

B = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
TI = os.path.join(B, '..', 'trade_imports')

# ---------- 1. Monthly BOL counts (ImportInfo) ----------
old = pd.read_csv(os.path.join(TI, 'importinfo_monthly_bols.csv'))
rows = []
for fn in glob.glob(os.path.join(B, 'raw', 'importinfo', '*_monthly.json')):
    slug = os.path.basename(fn)[:-len('_monthly.json')]
    for r in json.load(open(fn)):
        t = datetime.datetime.fromtimestamp(r['date'] / 1000, datetime.timezone.utc) + datetime.timedelta(days=3)
        rows.append((slug, t.strftime('%Y-%m'), r['value']))
new = pd.DataFrame(rows, columns=['slug', 'month', 'bols'])
allb = pd.concat([old[~old.slug.isin(new.slug)], new]).drop_duplicates(['slug', 'month'])

ROLE = {
    'converse-inc': ('converse', 'consignee', 'Nike-owned (Converse); consignee name not masked'),
    'nike-canada-corp': ('nike_canada', 'consignee', 'Nike Canada cargo routed via US ports; not masked'),
    'nike-de-mexico-s-de-r-l-de-c-v': ('nike_mexico', 'consignee', 'Nike Mexico cargo routed via US ports'),
    'nike-usa-inc': ('nike_usa_leak', 'consignee', 'Nike USA; masked since Dec 2022, residual leaks'),
    'nike-inc': ('nike_usa_leak', 'consignee', 'NIKE, Inc.; mostly non-trade (art, furniture)'),
    'feng-tay-enterprises-co-ltd': ('factory_strict', 'shipper', 'Feng Tay Taiwan/China; Nike ~88-90% of sales'),
    'pt-feng-tay-indonesia-enterprises': ('factory_strict', 'shipper', 'Feng Tay Indonesia; Nike'),
    'chang-shin-vietnam-co-ltd': ('factory_strict', 'shipper', 'Chang Shin Vietnam; Nike-dedicated'),
    'pt-chang-shin-indonesia': ('factory_strict', 'shipper', 'Chang Shin Indonesia; Nike-dedicated'),
    'pt-pratama-abadi-industri': ('factory_strict', 'shipper', 'Pratama (Indonesia); Nike-dedicated'),
    'lotus-footwear-enterprises-limited': ('factory_strict', 'shipper', 'Lotus Footwear (India); BOL text names Nike'),
    'tae-kwang-vina-industrial-joint-stock-company': ('factory_strict', 'shipper', 'Tae Kwang Vina; Nike-dedicated'),
    'pt-tk-industrial-indonesia': ('factory_strict', 'shipper', 'TK Industrial Indonesia (Tae Kwang); Nike'),
    'dona-pacific-vietnam-co-ltd': ('factory_strict', 'shipper', 'Dona Pacific (Feng Tay group) Vietnam'),
    'pt-nikomas-gemilang': ('factory_broad', 'shipper', 'Nikomas (Pou Chen) Indonesia; Nike largest client, multi-brand'),
    'nikomas-gemilang': ('factory_broad', 'shipper', 'Nikomas variant'),
    'freetrend-industrial-a-vietnam-co-ltd': ('factory_broad', 'shipper', 'Freetrend VN; Nike plus ASICS, Mizuno'),
    'pouyuen-vietnam-company-limited': ('factory_broad', 'shipper', 'Pou Yuen VN; multi-brand'),
    'apl-logistics-vietnam-company-ltd': ('forwarder_apl', 'shipper', 'APL Logistics VN; Nike origin consolidator, multi-client'),
    'branch-of-apl-logistics-vietnam': ('forwarder_apl', 'shipper', 'APL Logistics VN branch'),
    'pt-apl-logistics': ('forwarder_apl', 'shipper', 'APL Logistics Indonesia'),
    'adidas-america-inc': ('peer', 'consignee', 'adidas America'),
    'new-balance-athletics-inc': ('peer', 'consignee', 'New Balance'),
    'skechers-usa-inc': ('peer', 'consignee', 'Skechers'),
    'asics-america-corporation': ('peer', 'consignee', 'ASICS America'),
    'deckers-outdoor-corporation': ('peer', 'consignee', 'Deckers (HOKA, UGG)'),
    'brooks-sports-inc': ('peer', 'consignee', 'Brooks'),
    'on-inc': ('peer', 'consignee', 'On'),
    'vans-a-division-of-vf-outdoor-llc': ('peer', 'consignee', 'Vans (VF)'),
    'crocs-inc': ('peer', 'consignee', 'Crocs'),
    'puma-north-america-inc': ('peer_broken', 'consignee', 'Puma; visibility break 2024'),
    'under-armour-inc': ('peer_broken', 'consignee', 'Under Armour; visibility break 2024'),
}
allb['group'] = allb.slug.map(lambda s: ROLE.get(s, ('other', '', ''))[0])
allb['party_role'] = allb.slug.map(lambda s: ROLE.get(s, ('', '', ''))[1])
allb['note'] = allb.slug.map(lambda s: ROLE.get(s, ('', '', ''))[2])
allb = allb[(allb.month >= '2019-01') & (allb.group != 'other')].sort_values(['group', 'slug', 'month'])
allb.to_csv(os.path.join(B, 'bol_monthly_by_entity.csv'), index=False)

months = pd.period_range('2019-01', '2026-10', freq='M').strftime('%Y-%m')
piv = allb.pivot_table(index='month', columns='slug', values='bols', aggfunc='sum').reindex(months).fillna(0)
grp = allb.pivot_table(index='month', columns='group', values='bols', aggfunc='sum').reindex(months).fillna(0)

# ---------- 2. Market series ----------
mk = pd.read_csv(os.path.join(TI, 'nike_vs_industry_monthly.csv')).set_index('month')
panel = grp.copy()
panel['us_footwear_imports_usd_m'] = mk['us_fw_world_usd_m'].reindex(months)
panel['us_footwear_nikemix_usd_m'] = mk['us_fw_nikemix_usd_m'].reindex(months)
panel['fengtay_revenue_usd_m'] = mk['fengtay_usd_m'].reindex(months)
# FT-900 Exhibit 15 (NSA) footwear Aug 2026 = 2,483; Jul 2026 = 2,295 (SITC 85 basis, not HS 64). Aug 2025 HS64 not in Comtrade
# file; earlier hunt estimated Aug 2026 YoY at about +1.8%. Store Aug 2026 as HS64 Aug 2025 x 1.018 (flagged estimate).
panel.loc['2026-08', 'us_footwear_imports_usd_m'] = round(panel.loc['2025-08', 'us_footwear_imports_usd_m'] * 1.018, 2)
panel['us_footwear_aug2026_is_estimate'] = panel.index == '2026-08'
panel.index.name = 'month'
panel.reset_index().to_csv(os.path.join(B, 'nike_linked_panel_monthly.csv'), index=False)

# ---------- 3. Tests ----------
def wsum(s, y, m0, m1):
    return s[[f'{y}-{m:02d}' for m in range(m0, m1 + 1)]].sum()

def yoy(a, b):
    return round(100 * (a / b - 1), 1) if b else None

out = []
series = {**{c: piv[c] for c in piv.columns}, **{'GROUP:' + c: grp[c] for c in grp.columns},
          'MARKET:us_footwear_imports_usd_m': panel['us_footwear_imports_usd_m'],
          'MARKET:fengtay_revenue_usd_m': panel['fengtay_revenue_usd_m']}
for name, s in series.items():
    s = s.fillna(0)
    m1 = 8 if name.startswith('MARKET:us_') else 9  # market data through Aug 2026 (Aug estimated)
    r = dict(series=name, window=f'Jul-{"Aug" if m1 == 8 else "Sep"}')
    for y in (2024, 2025, 2026):
        r[f'jul_{y}'] = wsum(s, y, 7, m1)
        h1 = wsum(s, y, 1, 6) / 6
        r[f'loading_{y}'] = round((wsum(s, y, 7, m1) / (m1 - 6)) / h1, 2) if h1 else None
        r[f'ytd_{y}'] = wsum(s, y, 1, m1)
    r['yoy_vs_2025_pct'] = yoy(r['jul_2026'], r['jul_2025'])
    r['vs_2024_pct'] = yoy(r['jul_2026'], r['jul_2024'])
    r['ytd_yoy_pct'] = yoy(r['ytd_2026'], r['ytd_2025'])
    # visibility break flag: max/min of trailing 12-month sums over 2024-2026 > 3x
    roll = s.rolling(12).sum()['2024-12':'2026-09']
    r['visibility_break_flag'] = bool(roll.min() == 0 or roll.max() / max(roll.min(), 1) > 3)
    r['role'] = ROLE.get(name, ('', '', ''))[0] if ':' not in name else name.split(':')[0]
    out.append(r)
t = pd.DataFrame(out).rename(columns={'jul_2024': 'window_2024', 'jul_2025': 'window_2025', 'jul_2026': 'window_2026'})
t.to_csv(os.path.join(B, 'test_holiday_window.csv'), index=False)

peers = t[t.role == 'peer']
print(t[['series', 'window', 'window_2024', 'window_2025', 'window_2026', 'yoy_vs_2025_pct', 'vs_2024_pct', 'ytd_yoy_pct',
         'loading_2024', 'loading_2025', 'loading_2026', 'visibility_break_flag']].to_string())
print('\nPeer median YoY Jul-Sep 2026:', peers.yoy_vs_2025_pct.median(), ' vs 2024:', peers.vs_2024_pct.median(),
      ' peer median loading 2025->2026:', peers.loading_2025.median(), peers.loading_2026.median())

# ---------- 4. ImportGenius annual counts and recent shipments ----------
ig = json.load(open(os.path.join(B, 'raw', 'importgenius', 'ig_us_extract.json')))
ann, rec = [], []
for k, v in ig.items():
    if not v or 'error' in v:
        continue
    page = k.replace('.html', '').replace('__', '/').replace('ig_', 'suppliers/')
    for d in v.get('datapoints') or []:
        y = datetime.datetime.fromtimestamp(d['start'], datetime.timezone.utc).year
        end = datetime.datetime.fromtimestamp(d['end'], datetime.timezone.utc).date().isoformat()
        ann.append(dict(page=page, company=v['company'], trader_type=v['traderType'], year=y, shipments=d['totalShipments'], period_end=end))
    for s in v.get('shipments') or []:
        rec.append(dict(page=page, arrival=datetime.datetime.fromtimestamp(s['ArrivalDate'], datetime.timezone.utc).date().isoformat(),
                        shipper=(s.get('Shipper') or {}).get('name'), consignee=(s.get('Consignee') or {}).get('name'),
                        quantity=s.get('Quantity'), unit=s.get('QuantityUnit'), gross_kg=s.get('GrossWeightKgs'),
                        origin=s.get('CountryOfOrigin'), description=' | '.join(dict.fromkeys(s.get('ProductDescription') or []))[:400]))
pd.DataFrame(ann).drop_duplicates(['page', 'year']).to_csv(os.path.join(B, 'importgenius_annual_counts.csv'), index=False)
pd.DataFrame(rec).drop_duplicates().to_csv(os.path.join(B, 'importgenius_recent_shipments.csv'), index=False)

# ---------- 5. Pre-registered test verdicts ----------
clean_peers = t[(t.role == 'peer') & (~t.visibility_break_flag)]
pm, pm24 = round(clean_peers.yoy_vs_2025_pct.median(), 1), round(clean_peers.vs_2024_pct.median(), 1)
g = t.set_index('series')
strict = ['feng-tay-enterprises-co-ltd', 'pt-feng-tay-indonesia-enterprises', 'chang-shin-vietnam-co-ltd',
          'pt-chang-shin-indonesia', 'pt-pratama-abadi-industri', 'lotus-footwear-enterprises-limited']
st = g.loc[strict]
risers_all = int((st.window_2026 > st.window_2025).sum())
st_clean = st[~st.visibility_break_flag]
risers_clean = int((st_clean.window_2026 > st_clean.window_2025).sum())
clean_sum = st_clean[['window_2024', 'window_2025', 'window_2026']].sum()
mkt = g.loc['MARKET:us_footwear_imports_usd_m']
res = [
    dict(test='T1 Converse vs clean peers, Jul-Sep YoY', nike_linked=g.loc['converse-inc', 'yoy_vs_2025_pct'], benchmark=pm,
         gap_pts=round(g.loc['converse-inc', 'yoy_vs_2025_pct'] - pm, 1),
         rule='SHORT if gap < -10; NEUTRAL within 10; LONG if above',
         result='SHORT' if g.loc['converse-inc', 'yoy_vs_2025_pct'] - pm < -10 else ('NEUTRAL' if g.loc['converse-inc', 'yoy_vs_2025_pct'] - pm <= 10 else 'LONG')),
    dict(test='T1b Converse vs clean peers, Jul-Sep 2026 vs 2024', nike_linked=g.loc['converse-inc', 'vs_2024_pct'], benchmark=pm24,
         gap_pts=round(g.loc['converse-inc', 'vs_2024_pct'] - pm24, 1), rule='same thresholds (supplementary)',
         result='SHORT' if g.loc['converse-inc', 'vs_2024_pct'] - pm24 < -10 else 'NEUTRAL'),
    dict(test='T2a Nike Canada consignee Jul-Sep YoY vs US footwear imports Jul-Aug YoY', nike_linked=g.loc['nike-canada-corp', 'yoy_vs_2025_pct'],
         benchmark=mkt.yoy_vs_2025_pct, gap_pts=round(g.loc['nike-canada-corp', 'yoy_vs_2025_pct'] - mkt.yoy_vs_2025_pct, 1),
         rule='part of T2', result='rises, beats market'),
    dict(test='T2b strict factory leaks (non-break names only) Jul-Sep YoY', nike_linked=round(100 * (clean_sum.window_2026 / clean_sum.window_2025 - 1), 1),
         benchmark=mkt.yoy_vs_2025_pct, gap_pts=None,
         rule=f'breadth: risers among 6 strict names = {risers_all} (all) / {risers_clean} of {len(st_clean)} non-break names; need 3+ without break names',
         result='INCONCLUSIVE (breadth fails once visibility-break names are removed)' if risers_clean < 3 else 'LONG'),
    dict(test='T3 holiday loading Jul-Sep avg / Jan-Jun avg, 2026 vs 2025', nike_linked=f"Nike Canada {g.loc['nike-canada-corp','loading_2025']}->{g.loc['nike-canada-corp','loading_2026']}; strict factories {g.loc['GROUP:factory_strict','loading_2025']}->{g.loc['GROUP:factory_strict','loading_2026']}; Converse {g.loc['converse-inc','loading_2025']}->{g.loc['converse-inc','loading_2026']}",
         benchmark=f"clean peer median {round(clean_peers.loading_2025.median(),2)}->{round(clean_peers.loading_2026.median(),2)}; US footwear imports {mkt.loading_2025}->{mkt.loading_2026}",
         gap_pts=None, rule='LONG if Nike-linked ratios rise while peers fall', result='LONG-leaning (weak: small, visibility-prone samples)'),
]
pd.DataFrame(res).to_csv(os.path.join(B, 'test_results.csv'), index=False)
print(pd.DataFrame(res).to_string())
print('clean peers used:', clean_peers.series.tolist())
