"""Pull Laced (UK sneaker resale marketplace) collection listings and per-product
'sold_in_last_28_days' counts (a public field on the product API), plus lowest ask (GBP).

Endpoints (public, no login, robots.txt allows /):
  collection page: https://www.laced.com/<brand>/<collection>  (__NEXT_DATA__ Algolia browse results, 100 hits)
  product api:     https://www.laced.com/api/v1/products/<slug>
Usage: python3 -I laced_pull.py OUTDIR
Writes OUTDIR/raw/laced_collections.jsonl and OUTDIR/raw/laced_products.jsonl (resumable).
"""
import json, os, re, sys, time, urllib.request

OUT = sys.argv[1]
RAW = os.path.join(OUT, 'raw'); os.makedirs(RAW, exist_ok=True)
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'
SLEEP = 0.6
COLL = {
    'nike/dunk-low': 'Nike Dunk Low', 'nike/air-force-1': 'Nike AF1', 'nike/p-6000': 'Nike P-6000',
    'nike/air-max-1': 'Nike Air Max 1', 'nike/air-max-90': 'Nike Air Max 90', 'nike/air-max-95': 'Nike Air Max 95',
    'nike/air-max-tn': 'Nike Air Max TN', 'nike/nike-shox': 'Nike Shox', 'nike/vomero-5': 'Nike Vomero',
    'air-jordan/air-jordan-1-high': 'Jordan AJ1 High', 'air-jordan/air-jordan-1-low': 'Jordan AJ1 Low',
    'air-jordan/air-jordan-1-mid': 'Jordan AJ1 Mid', 'air-jordan/air-jordan-3': 'Jordan AJ3',
    'air-jordan/air-jordan-4': 'Jordan AJ4', 'air-jordan/air-jordan-5': 'Jordan AJ5', 'air-jordan/air-jordan-11': 'Jordan AJ11',
    'adidas/samba': 'adidas Samba', 'adidas/gazelle': 'adidas Gazelle', 'adidas/campus': 'adidas Campus',
    'adidas/spezial': 'adidas Spezial', 'adidas/superstar': 'adidas Superstar',
    'new-balance/new-balance-550': 'NB 550', 'new-balance/new-balance-530': 'NB 530', 'new-balance/new-balance-9060': 'NB 9060',
    'new-balance/new-balance-2002r': 'NB 2002R', 'new-balance/new-balance-990': 'NB 990', 'new-balance/new-balance-1906r': 'NB 1906',
    'asics/asics-gel-kayano-14': 'ASICS Kayano 14', 'asics/gel-1130': 'ASICS Gel-1130', 'asics/asics-gel-nyc': 'ASICS Gel-NYC',
    'saucony/saucony-progrid-omni-9': 'Saucony Omni 9', 'birkenstock/birkenstock-boston': 'Birkenstock Boston',
}


def fetch(url):
    for a in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=40) as r:
                return r.status, r.read().decode('utf-8', 'ignore')
        except urllib.error.HTTPError as e:
            return e.code, ''
        except Exception:
            time.sleep(3 * (a + 1))
    return 0, ''


def main():
    cf = os.path.join(RAW, 'laced_collections.jsonl')
    items = {}
    if os.path.exists(cf):
        for ln in open(cf):
            r = json.loads(ln); items.setdefault(r['slug'], r)
    else:
        with open(cf, 'w') as f:
            for c, line in COLL.items():
                st, html = fetch('https://www.laced.com/' + c); time.sleep(SLEEP)
                m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html)
                if not m:
                    print('no data', c, st, flush=True); continue
                sw = json.loads(m.group(1))['props']['pageProps']['swrServerData']
                k = [k for k in sw if k.startswith('/en/browse')]
                if not k:
                    print('no browse', c, flush=True); continue
                res = sw[k[0]]['results'][0]
                for rank, h in enumerate(res['hits']):
                    loc = h['localisation']['en']
                    prices = [v[0] for v in (h.get('sizePricing') or {}).get('GB', {}).values() if v and v[0]]
                    r = {'collection': c, 'line': line, 'rank': rank, 'nb_hits_collection': res.get('nbHits'),
                         'slug': loc['slug'], 'title': loc['title'], 'brand': loc.get('brand'), 'style_code': h.get('styleCode'),
                         'min_ask_gbp': min(prices) if prices else None, 'n_sizes_listed': len(prices)}
                    f.write(json.dumps(r) + '\n'); items.setdefault(r['slug'], r)
                print('coll', c, res.get('nbHits'), len(res['hits']), flush=True)
    pf = os.path.join(RAW, 'laced_products.jsonl')
    done = set(json.loads(l)['slug'] for l in open(pf)) if os.path.exists(pf) else set()
    with open(pf, 'a') as f:
        for i, (slug, r) in enumerate(items.items()):
            if slug in done:
                continue
            st, body = fetch('https://www.laced.com/api/v1/products/' + slug); time.sleep(SLEEP)
            try:
                d = json.loads(body)
            except Exception:
                d = {}
            f.write(json.dumps({'slug': slug, 'http': st, 'id': d.get('id'), 'brand_id': d.get('brand_id'),
                                'sold_in_last_28_days': d.get('sold_in_last_28_days'), 'release_year': d.get('release_year'),
                                'style_code': d.get('style_code'), 'title': d.get('title'),
                                'pulled_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}) + '\n')
            if i % 100 == 0:
                f.flush(); print('prod', i, flush=True)
    print('done')


if __name__ == '__main__':
    main()
