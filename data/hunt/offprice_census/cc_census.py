# Brand share of Common Crawl product-page captures per retailer and crawl.
# usage: python3 -I cc_census.py <dir of host__CRAWL.jsonl.gz index files> <out csv>
# Each index file lists url,status,timestamp for a retailer product-URL prefix (see harvest.py).
# Brand = slug prefix; product id = trailing numeric id; unique (brand, id) counted once per crawl.
import gzip, glob, json, re, os, sys, csv, collections
from urllib.parse import unquote
d, out = sys.argv[1], sys.argv[2]
BR = [('air-jordan', 'jordan'), ('jordan', 'jordan'), ('nike', 'nike'), ('adidas', 'adidas'), ('new-balance', 'new_balance'),
      ('hoka', 'hoka'), ('on-running', 'on'), ('asics', 'asics'), ('converse', 'converse'), ('puma', 'puma'),
      ('under-armour', 'under_armour'), ('reebok', 'reebok'), ('skechers', 'skechers'), ('saucony', 'saucony'), ('brooks', 'brooks'), ('vans', 'vans')]
def brand(s):
    s = s.lower()
    for p, b in BR:
        if s.startswith(p):
            return b
    return 'other'
RX = {
    'nordstromrack': r'/s/([^/?]+)/(\d+)',
    'dsw': r'/product/([^/?]+)/(\d+)',
    'academy': r'/p/([^/?]+)-(\d{6,})',
    'famousfootwear': r'/product/([^/?]+)-(\d{5,8})',
    '6pm': r'/p/([^/?]+)/product/(\d+)',
    'saksoff5th': r'/product/(.+)-(\d{10,})\.html',
}
rows = []
for f in sorted(glob.glob(os.path.join(d, '*__CC-MAIN-*.jsonl.gz'))):
    host, crawl = os.path.basename(f)[:-9].split('__')
    if host not in RX:
        continue
    seen = set(); c = collections.Counter(); caps = 0
    for line in gzip.open(f, 'rt'):
        try:
            j = json.loads(line)
        except Exception:
            continue
        caps += 1
        m = re.search(RX[host], unquote(j['url']))
        if not m:
            continue
        key = (m.group(1), m.group(2))
        if key in seen:
            continue
        seen.add(key); c[brand(m.group(1))] += 1
    tot = sum(c.values())
    if tot == 0:
        continue
    for b in ['nike', 'jordan', 'converse', 'adidas', 'new_balance', 'hoka', 'on', 'asics', 'puma', 'other']:
        rows.append([host, crawl, b, c[b], round(100 * c[b] / tot, 3), tot, caps])
with open(out, 'w', newline='') as o:
    w = csv.writer(o); w.writerow(['host', 'crawl', 'brand', 'n_unique_products', 'share_pct', 'total_unique_products', 'index_captures'])
    w.writerows(rows)
print(len(rows))
