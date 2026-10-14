"""Pull SNKRDUNK (Japan's largest sneaker resale marketplace) product universe and
daily new-condition trade price history for Nike/Jordan models and rival models.

Endpoints (public, no login, allowed by robots.txt which only disallows /en/v1/*):
  search:   https://snkrdunk.com/en/v2/search?keyword=..&categoryIds=1&perPage=50&page=N
  product:  https://snkrdunk.com/v2/products/{code}?type=sneaker      (JP id, release date, JP retail yen)
  history:  https://snkrdunk.com/v3/products/{id}/trading-history?range=all&condition_code=new_unused
Usage: python3 -I snkrdunk_pull.py OUTDIR [pages_per_keyword] [shard] [nshards]
Writes OUTDIR/raw/snkrdunk_search_<kw>.json, OUTDIR/raw/snkrdunk_products.jsonl,
OUTDIR/raw/snkrdunk_history.jsonl.gz (chart points + last 20 trades per product).
Resumable: skips products already in the history file.
"""
import gzip, json, os, sys, time, urllib.error, urllib.parse, urllib.request

OUT = sys.argv[1]
PAGES = int(sys.argv[2]) if len(sys.argv) > 2 else 3
SHARD = int(sys.argv[3]) if len(sys.argv) > 3 else 0
NSHARD = int(sys.argv[4]) if len(sys.argv) > 4 else 1
RAW = os.path.join(OUT, 'raw')
os.makedirs(RAW, exist_ok=True)
UA = 'Mozilla/5.0 (research; low-rate)'
SLEEP = 0.6

KEYWORDS = {
    # Nike / Jordan
    'nike dunk low': 'Nike Dunk Low', 'nike air force 1': 'Nike AF1',
    'air jordan 1 high': 'Jordan AJ1 High', 'air jordan 1 low': 'Jordan AJ1 Low',
    'air jordan 4': 'Jordan AJ4', 'air jordan 11': 'Jordan AJ11',
    'nike pegasus': 'Nike Pegasus', 'nike vomero': 'Nike Vomero',
    'nike air max 1': 'Nike Air Max 1', 'nike p-6000': 'Nike P-6000',
    'nike cortez': 'Nike Cortez', 'nike sb dunk': 'Nike SB Dunk',
    # rivals
    'adidas samba': 'adidas Samba', 'adidas gazelle': 'adidas Gazelle',
    'adidas spezial': 'adidas Spezial', 'adidas campus': 'adidas Campus',
    'adidas superstar': 'adidas Superstar', 'adidas taekwondo': 'adidas Taekwondo',
    'new balance 550': 'NB 550', 'new balance 2002r': 'NB 2002R',
    'new balance 1906': 'NB 1906', 'new balance 990': 'NB 990',
    'new balance 9060': 'NB 9060', 'new balance 1000': 'NB 1000',
    'asics gel-kayano 14': 'ASICS Kayano 14', 'asics gel-1130': 'ASICS Gel-1130',
    'asics gel-nyc': 'ASICS Gel-NYC', 'onitsuka tiger mexico 66': 'Onitsuka Mexico 66',
    'on cloud': 'On Cloud', 'hoka': 'Hoka', 'salomon xt-6': 'Salomon XT-6',
    'puma speedcat': 'Puma Speedcat',
}


def get(url):
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': 'application/json'})
            with urllib.request.urlopen(req, timeout=40) as r:
                return json.loads(r.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            try:
                return {'_error': 'HTTP %s %s' % (e.code, e.read()[:200].decode('utf-8', 'ignore'))}
            except Exception:
                return {'_error': 'HTTP %s' % e.code}
        except Exception as e:  # noqa
            err = e
            time.sleep(3 * (attempt + 1))
    return {'_error': str(err)}


def search():
    prods = {}
    for kw, line in KEYWORDS.items():
        pages = []
        for p in range(1, PAGES + 1):
            q = urllib.parse.urlencode({'keyword': kw, 'categoryIds': 1, 'perPage': 50, 'page': p})
            d = get('https://snkrdunk.com/en/v2/search?' + q)
            time.sleep(SLEEP)
            pages.append(d)
            items = (d.get('search') or {}).get('products') or []
            for rank, it in enumerate(items):
                code = it.get('productCode')
                if not code or it.get('productTypeGB') != 'sneaker':
                    continue
                prods.setdefault(code, {'code': code, 'name': it.get('name'), 'line_kw': line, 'kw': kw,
                                        'brand_id': (it.get('supershipLog') or {}).get('brandId'),
                                        'search_rank': (p - 1) * 50 + rank, 'en_price_usd': (it.get('price') or {}).get('value')})
            if len(items) < 50:
                break
        json.dump(pages, open(os.path.join(RAW, 'snkrdunk_search_%s.json' % kw.replace(' ', '_')), 'w'))
        print('search', kw, len(prods), flush=True)
    return prods


def main():
    pf = os.path.join(RAW, 'snkrdunk_universe.json')
    if os.path.exists(pf):
        prods = json.load(open(pf))
    else:
        prods = search()
        json.dump(prods, open(pf, 'w'))
    hf = os.path.join(RAW, 'snkrdunk_history_s%d.jsonl.gz' % SHARD)
    done = set()
    if os.path.exists(hf):
        with gzip.open(hf, 'rt') as f:
            for ln in f:
                done.add(json.loads(ln)['code'])
    out = gzip.open(hf, 'at')
    n = 0
    for i, (code, meta) in enumerate(sorted(prods.items())):
        if i % NSHARD != SHARD or code in done:
            continue
        pj = get('https://snkrdunk.com/v2/products/' + urllib.parse.quote(code) + '?type=sneaker')
        time.sleep(SLEEP)
        rec = dict(meta)
        rec.update({'jp_id': pj.get('id'), 'released_jp': pj.get('releasedAtJP'), 'retail_jpy': pj.get('regularPriceJP'),
                    'name_en': pj.get('nameEN'), 'pulled_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())})
        if pj.get('id'):
            th = get('https://snkrdunk.com/v3/products/%s/trading-history?range=all&condition_code=new_unused' % pj['id'])
            time.sleep(SLEEP)
            lines = (th.get('chart') or {}).get('lines') or []
            rec['points'] = [[p['timestamp'], p['price']] for l in lines for p in l['points']]
            rec['trades'] = th.get('trades')
            rec['err'] = th.get('_error') or th.get('code')
        out.write(json.dumps(rec, ensure_ascii=False) + '\n')
        n += 1
        if n % 50 == 0:
            out.flush()
            print('history', n, flush=True)
    out.close()
    print('done', n)


if __name__ == '__main__':
    main()
