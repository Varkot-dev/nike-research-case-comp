"""Pull EU monthly imports of footwear from Eurostat Comext API (DS-045409, free, no key).
Saves raw JSON-stat to raw/eurostat/ and a tidy CSV eu_imports_footwear_monthly.csv."""
import os, json, time, urllib.request, itertools, csv
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
raw = os.path.join(base, 'raw', 'eurostat'); os.makedirs(raw, exist_ok=True)
partners = ['VN', 'ID', 'CN', 'KH', 'IN', 'BD', 'EXT_EU27_2020']
products = ['64', '6402', '6403', '6404']
indicators = ['VALUE_IN_EUROS', 'SUPPLEMENTARY_QUANTITY']
rows = []
for p in partners:
    fn = os.path.join(raw, f'eu_imp_{p}.json')
    if not os.path.exists(fn):
        q = '&'.join([f'product={x}' for x in products] + [f'indicators={x}' for x in indicators])
        url = ('https://ec.europa.eu/eurostat/api/comext/dissemination/statistics/1.0/data/DS-045409?format=JSON&lang=EN'
               f'&freq=M&reporter=EU&partner={p}&flow=1&{q}&sinceTimePeriod=2019-01')
        with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=120) as r:
            open(fn, 'wb').write(r.read())
        time.sleep(3)
    d = json.load(open(fn))
    dims = d['id']; size = d['size']
    cats = [sorted(d['dimension'][k]['category']['index'].items(), key=lambda kv: kv[1]) for k in dims]
    for combo in itertools.product(*[range(s) for s in size]):
        idx = 0
        for k, c in enumerate(combo):
            idx = idx * size[k] + c
        v = d['value'].get(str(idx))
        if v is None:
            continue
        rec = {dims[k]: cats[k][combo[k]][0] for k in range(len(dims))}
        rows.append(dict(month=rec['time'], partner=p, hs=rec['product'], indicator=rec['indicators'], value=v))
    print(p, len(rows), flush=True)
with open(os.path.join(base, 'eu_imports_footwear_monthly.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['month', 'partner', 'hs', 'indicator', 'value']); w.writeheader(); w.writerows(rows)
