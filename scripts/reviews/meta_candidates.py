# Stream Amazon 2023 metadata (stdin, decompressed jsonl); keep loose brand candidates.
import sys, json, re, gzip
pat = re.compile(r"\b(nike|jordan|converse|adidas|hoka|on running|on ag|new balance|brooks|asics|skechers|under armour|underarmour|puma)\b", re.I)
out = gzip.open(sys.argv[1], 'wt')
n = 0; k = 0
for line in sys.stdin:
    n += 1
    try: d = json.loads(line)
    except Exception: continue
    store = d.get('store') or ''
    det = d.get('details') or {}
    brand = det.get('Brand') or det.get('brand') or ''
    if not (pat.search(store) or pat.search(str(brand)) or store.strip().lower() == 'on'):
        continue
    k += 1
    out.write(json.dumps({'parent_asin': d.get('parent_asin'), 'store': store, 'brand': brand,
        'title': d.get('title'), 'categories': d.get('categories'), 'main_category': d.get('main_category'),
        'date_first': det.get('Date First Available'), 'rating_number': d.get('rating_number'),
        'average_rating': d.get('average_rating'), 'price': d.get('price')})+'\n')
out.close()
print('meta rows', n, 'candidates', k, file=sys.stderr)
