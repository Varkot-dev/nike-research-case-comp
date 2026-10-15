"""Flatten raw Comtrade monthly JSON into tidy CSV.
Usage: python clean_comtrade.py <prefix> <out.csv>"""
import sys, os, json, glob, csv

prefix, outname = sys.argv[1:3]
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
PARTNER = {0: 'World', 704: 'Vietnam', 156: 'China', 360: 'Indonesia', 116: 'Cambodia', 699: 'India', 50: 'Bangladesh',
           76: 'Brazil', 380: 'Italy', 484: 'Mexico', 842: 'USA'}
REPORTER = {842: 'USA', 704: 'Vietnam', 360: 'Indonesia', 156: 'China'}
rows = []
for fn in sorted(glob.glob(os.path.join(base, 'raw', 'comtrade', f'{prefix}_*.json'))):
    d = json.load(open(fn))
    for r in d.get('data', []):
        if r.get('motCode', 0) != 0 or r.get('customsCode') not in ('C00', None) or r.get('partner2Code', 0) != 0:
            continue
        rows.append(dict(month=f"{r['refYear']}-{r['refMonth']:02d}", reporter=REPORTER.get(r['reporterCode'], r['reporterCode']),
                         flow=r['flowCode'], partner=PARTNER.get(r['partnerCode'], r['partnerCode']), hs=r['cmdCode'],
                         value_usd=r['primaryValue'], cif_usd=r.get('cifvalue'), fob_usd=r.get('fobvalue'),
                         qty=r.get('qty'), qty_unit_code=r.get('qtyUnitCode'), qty_estimated=r.get('isQtyEstimated'),
                         net_kg=r.get('netWgt')))
rows.sort(key=lambda x: (x['month'], x['partner'], x['hs']))
with open(os.path.join(base, outname), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print(len(rows), rows[0]['month'], rows[-1]['month'])
