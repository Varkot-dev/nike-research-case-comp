"""Checker: pull deeper SNKRDUNK search ranks (151 to 200 by default, page 4; pages are a CLI option) for selected lines, to test whether
the hunter's top-150-by-relevance universe is selected on current popularity.
Usage: python3 -I checker_deep_pull.py OUTFILE.jsonl.gz SHARD NSHARD [PAGES, default 4]
Products are interleaved across lines and sharded by position; codes already in any
raw/checker_deep_*.jsonl.gz file are skipped (resumable).
Same public endpoints and user agent as snkrdunk_pull.py, 0.8 s between requests.
"""
import gzip, json, os, sys, time, urllib.parse, urllib.request

OUTF, SHARD, NSHARD = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
PAGES = [int(x) for x in (sys.argv[4] if len(sys.argv) > 4 else '4').split(',')]
UA = 'Mozilla/5.0 (research; low-rate)'
SLEEP = 0.8
KWS = ['nike dunk low', 'air jordan 1 high', 'nike air force 1', 'air jordan 4',
       'adidas samba', 'adidas gazelle', 'new balance 2002r', 'onitsuka tiger mexico 66']


def get(url):
    for a in range(3):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': 'application/json'})
            with urllib.request.urlopen(req, timeout=40) as r:
                return json.loads(r.read().decode('utf-8'))
        except Exception as e:  # noqa
            err = str(e); time.sleep(3 * (a + 1))
    return {'_error': err}


import glob, zlib
done = set()
for f in glob.glob(os.path.join(os.path.dirname(OUTF), 'checker_deep_*.jsonl.gz')):
    for ln in zlib.decompressobj(31).decompress(open(f, 'rb').read()).decode('utf-8', 'ignore').splitlines():
        try: done.add(json.loads(ln)['code'])
        except Exception: pass
per_kw = {}
for kw in KWS:
    per_kw[kw] = []
    for p in PAGES:
        d = get('https://snkrdunk.com/en/v2/search?' + urllib.parse.urlencode({'keyword': kw, 'categoryIds': 1, 'perPage': 50, 'page': p}))
        time.sleep(SLEEP)
        for rank, it in enumerate((d.get('search') or {}).get('products') or []):
            if it.get('productTypeGB') == 'sneaker':
                per_kw[kw].append({'code': it['productCode'], 'name': it.get('name'), 'kw': kw,
                                   'brand_id': (it.get('supershipLog') or {}).get('brandId'), 'search_rank': (p - 1) * 50 + rank})
inter = [x for i in range(max(len(v) for v in per_kw.values())) for x in [v[i] for v in per_kw.values() if i < len(v)]]
prods = [m for j, m in enumerate(inter) if j % NSHARD == SHARD and m['code'] not in done]
out = gzip.open(OUTF, 'at')
for m in prods:
    pj = get('https://snkrdunk.com/v2/products/' + urllib.parse.quote(m['code']) + '?type=sneaker'); time.sleep(SLEEP)
    m.update({'jp_id': pj.get('id'), 'released_jp': pj.get('releasedAtJP'), 'retail_jpy': pj.get('regularPriceJP'), 'name_en': pj.get('nameEN')})
    if pj.get('id'):
        th = get('https://snkrdunk.com/v3/products/%s/trading-history?range=all&condition_code=new_unused' % pj['id']); time.sleep(SLEEP)
        m['points'] = [[q['timestamp'], q['price']] for l in ((th.get('chart') or {}).get('lines') or []) for q in l['points']]
    out.write(json.dumps(m, ensure_ascii=False) + '\n'); out.flush()
out.close()
print('done', len(prods))
