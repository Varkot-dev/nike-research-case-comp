"""Build tidy CSVs from raw/ pulls. Run: python3 -I scripts/build_tidy.py"""
import csv, json, glob, os, re
import pandas as pd
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
rows = []
FRED_DESC = {
 'MRTSSM4482USS': ('US', 'Census MRTS shoe stores NAICS 4482 sales, SA, $mn'),
 'MRTSSM4482USN': ('US', 'Census MRTS shoe stores NAICS 4482 sales, NSA, $mn'),
 'MRTSSM45111USN': ('US', 'Census MRTS sporting goods stores NAICS 45111 sales, NSA, $mn'),
 'MRTSSM451USN': ('US', 'Census MRTS sporting goods, hobby, musical instrument, book stores NAICS 451, NSA, $mn'),
 'MRTSSM448USN': ('US', 'Census MRTS clothing and accessories stores NAICS 448, NSA, $mn'),
 'MRTSSM4481USS': ('US', 'Census MRTS clothing stores NAICS 4481, SA, $mn'),
 'MRTSSM44812USN': ('US', "Census MRTS women's clothing stores, NSA, $mn"),
 'MRTSSM454USS': ('US', 'Census MRTS nonstore retailers NAICS 454, SA, $mn'),
 'MRTSSM4541USS': ('US', 'Census MRTS electronic shopping and mail order NAICS 4541, SA, $mn'),
 'RSCCAS': ('US', 'Advance retail sales clothing and accessory stores, SA, $mn'),
 'RSCCASN': ('US', 'Advance retail sales clothing and accessory stores, NSA, $mn'),
 'RSSGHBMS': ('US', 'Advance retail sales sporting goods, hobby, musical instrument, book stores, SA, $mn'),
 'RSXFS': ('US', 'Advance retail sales ex food services, SA, $mn'),
 'RSAFS': ('US', 'Advance retail and food services sales, SA, $mn'),
 'RSNSR': ('US', 'Advance retail sales nonstore retailers, SA, $mn'),
 'CUSR0000SEAE': ('US', 'CPI-U footwear, SA, index 1982-84=100'),
 'CUUR0000SEAE': ('US', 'CPI-U footwear, NSA, index 1982-84=100'),
 'CUUR0000SERE01': ('US', 'CPI-U toys, NSA'),
 'CPIAUCSL': ('US', 'CPI-U all items, SA'),
 'PCU316210316210': ('US', 'PPI footwear manufacturing NAICS 316210'),
 'PCU316210316210P': ('US', 'PPI footwear manufacturing primary products'),
 'PCU3162131621': ('US', 'PPI footwear manufacturing NAICS 31621 (2003=100)'),
 'WPU0431': ('US', 'PPI commodity: footwear (ends 2025-12)'),
 'WPU0432': ('US', 'PPI commodity: other leather and related products'),
 'IR10000': ('US', 'BLS import price index all imports (FRED IR10000)'),
 'CES4244800001': ('US', 'CES employees, clothing and clothing accessories retailers, thousands, SA'),
 'CES4245100001': ('US', 'CES employees, sporting goods, hobby, musical instrument and book retailers, thousands, SA'),
 'ECOMSA': ('US', 'Census quarterly e-commerce retail sales, SA, $mn'),
 'PCU44824482': ('US', 'PPI retail trade margin: shoe stores (NAICS 4482), Dec 2003=100'),
 'PCU448210448210': ('US', 'PPI retail trade margin: shoe stores 448210, Jun 2002=100'),
 'PCU45114511': ('US', 'PPI retail trade margin: sporting goods stores (4511), Dec 2003=100'),
 'PCU451110451110': ('US', 'PPI retail trade margin: sporting goods stores 451110'),
 'PCU4511104511101': ('US', 'PPI retail margin: sporting goods stores, sporting goods/athletic apparel/footwear line'),
 'PCU44814481': ('US', 'PPI retail trade margin: clothing stores (4481)'),
}
for f in glob.glob('raw/fred_*.csv'):
    sid = f[9:-4]
    if sid not in FRED_DESC: continue
    d = pd.read_csv(f)
    d.columns = ['date', 'value']
    d['value'] = pd.to_numeric(d['value'], errors='coerce')
    for _, r in d.dropna().iterrows():
        rows.append(dict(geo=FRED_DESC[sid][0], source='FRED', series_id=sid, description=FRED_DESC[sid][1], date=r['date'][:7], value=r['value'],
                         url=f'https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}'))
# BEA PCE monthly
BEA = {'DSHURC': 'PCE shoes and other footwear, current $mn SAAR', 'DSHURA': 'PCE shoes and other footwear, real quantity index 2017=100',
       'DSHURG': 'PCE shoes and other footwear, price index 2017=100', 'DSHURX': 'PCE shoes and other footwear, chained 2017 $mn SAAR',
       'DSPGRC': 'PCE sporting equipment, supplies, guns and ammunition, current $mn SAAR', 'DSPGRA': 'PCE sporting equipment quantity index',
       'DCLORC': 'PCE clothing and footwear, current $mn SAAR', 'DCLORA': 'PCE clothing and footwear quantity index', 'DCLORG': 'PCE clothing and footwear price index',
       'DGARRC': 'PCE garments, current $mn SAAR', 'DPCERC': 'PCE total, current $mn SAAR', 'DGDSRC': 'PCE goods, current $mn SAAR', 'DPCERG': 'PCE price index total'}
for line in open('raw/bea_nipa_monthly_subset.txt'):
    p = next(csv.reader([line]))
    sid = p[0].strip('"')
    if sid in BEA:
        y, m = p[1].split('M')
        rows.append(dict(geo='US', source='BEA NIPA (NipaDataM.txt)', series_id=sid, description=BEA[sid], date=f'{y}-{m}', value=float(p[2].replace(',', '')),
                         url='https://apps.bea.gov/national/Release/TXT/NipaDataM.txt'))
us = pd.DataFrame(rows)
us = us[us.date >= '2015-01']
us.to_csv('us_category_monthly_long.csv', index=False)
# Eurostat
er = []
for f in glob.glob('raw/eurostat/*.json'):
    d = json.load(open(f))
    dims = d['id']; sizes = d['size']
    cats = {k: {v: kk for kk, v in d['dimension'][k]['category']['index'].items()} for k in dims}
    for idx, val in d['value'].items():
        idx = int(idx); coords = {}
        for k, s in zip(reversed(dims), reversed(sizes)):
            coords[k] = cats[k][idx % s]; idx //= s
        er.append(dict(dataset=os.path.basename(f).split('_')[0] if 'hicp' in f else 'sts_trtu_m', nace_or_coicop=coords.get('nace_r2', coords.get('coicop')),
                       indic=coords.get('indic_bt', 'HICP'), s_adj=coords.get('s_adj', ''), unit=coords.get('unit'), geo=coords['geo'], date=coords['time'], value=val))
pd.DataFrame(er).sort_values(['dataset', 'nace_or_coicop', 'indic', 'geo', 'date']).to_csv('europe_retail_hicp_monthly_long.csv', index=False)
# StatCan
sc = pd.read_csv('raw/statcan_20100056_canada_subset.csv'); sc.to_csv('canada_retail_by_naics_monthly.csv', index=False)
# ONS
on = []
for f in glob.glob('raw/ons_*.csv'):
    lines = list(csv.reader(open(f)))
    title = lines[0][1]; cdid = lines[1][1]
    for l in lines:
        if len(l) == 2 and re.match(r'^\d{4} [A-Z]{3}$', l[0]) and l[1] != '':
            on.append(dict(cdid=cdid, title=title, date=pd.to_datetime(l[0], format='%Y %b').strftime('%Y-%m'), value=float(l[1])))
pd.DataFrame(on).to_csv('uk_ons_retail_monthly.csv', index=False)
print(len(us), len(er), len(sc), len(on))
