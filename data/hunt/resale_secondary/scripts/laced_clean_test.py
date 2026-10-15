"""Clean Laced raw pulls into a tidy CSV and run Test D (UK resale units, last 28 days, by brand and release cohort).
Usage: python3 -I laced_clean_test.py OUTDIR
"""
import csv, json, os, re, statistics as st, sys
from collections import defaultdict

OUT = sys.argv[1]; RAW = os.path.join(OUT, 'raw')
coll = {}
for ln in open(os.path.join(RAW, 'laced_collections.jsonl')):
    r = json.loads(ln); coll.setdefault(r['slug'], r)
COLLAB = re.compile(r' x |travis|off-white|union|fragment|sacai|supreme|a ma mani|stussy|wales bonner|kith|patta|balvin|bad bunny|tom sachs|clot|cactus|wotherspoon|aime leon|freshgoods|jjjjound|salehe|stone island|cdg|comme des|undercover|ambush|bape|kaws|nigel sylvester|gucci|prada|bode', re.I)


def bgroup(title, brand):
    t = (title or '').lower()
    if 'jordan' in t: return 'Jordan'
    if (brand or '').lower() == 'nike' or t.startswith('nike'): return 'Nike'
    for b, k in [('adidas', 'adidas'), ('New Balance', 'new balance'), ('ASICS', 'asics'), ('Saucony', 'saucony'), ('Birkenstock', 'birkenstock')]:
        if k in t or (brand or '').lower() == k: return b
    return brand or 'other'


rows = []
seen = set()
for ln in open(os.path.join(RAW, 'laced_products.jsonl')):
    p = json.loads(ln)
    if p['slug'] in seen or p.get('sold_in_last_28_days') is None:
        continue
    seen.add(p['slug'])
    c = coll.get(p['slug'], {})
    rows.append({'slug': p['slug'], 'title': p['title'], 'brand_group': bgroup(p['title'], c.get('brand')), 'collection_line': c.get('line'),
                 'collection_rank': c.get('rank'), 'style_code': p['style_code'], 'release_year': p['release_year'],
                 'collab': int(bool(COLLAB.search(p['title'] or ''))), 'sold_in_last_28_days': p['sold_in_last_28_days'],
                 'min_ask_gbp': c.get('min_ask_gbp'), 'n_sizes_listed': c.get('n_sizes_listed'), 'pulled_utc': p['pulled_utc']})
with open(os.path.join(OUT, 'laced_products_sold28d.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print('laced rows', len(rows))

out = []
agg = defaultdict(list)
for r in rows:
    yr = r['release_year'] or 'na'
    cohort = yr if yr in ('2024', '2025', '2026') else ('pre2024' if yr != 'na' else 'na')
    agg[(r['brand_group'], cohort)].append(r['sold_in_last_28_days'])
    agg[(r['brand_group'], 'all')].append(r['sold_in_last_28_days'])
    agg[(r['collection_line'], 'line_all')].append(r['sold_in_last_28_days'])
total = sum(r['sold_in_last_28_days'] for r in rows)
for (g, c), v in sorted(agg.items(), key=lambda x: (str(x[0][0]), x[0][1])):
    out.append({'group': g, 'cohort': c, 'n_products': len(v), 'units_28d': sum(v), 'share_of_all_units': round(sum(v) / total, 4),
                'median_units_per_product': st.median(v), 'mean_units_per_product': round(st.mean(v), 2),
                'share_products_zero_sales': round(sum(1 for x in v if x == 0) / len(v), 3)})
with open(os.path.join(OUT, 'test_D_laced_units_by_brand_cohort.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
for o in out:
    if o['cohort'] in ('all', '2025', '2026'):
        print(o)
