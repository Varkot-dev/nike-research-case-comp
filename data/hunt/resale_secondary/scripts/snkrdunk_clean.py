"""Clean SNKRDUNK raw history into tidy CSVs.
Usage: python3 -I snkrdunk_clean.py OUTDIR
Outputs (in OUTDIR):
  snkrdunk_products.csv        one row per product: code, name, brand group, model line, release date, JP retail, n trade days, last-20-trade velocity
  snkrdunk_product_month.csv   product x month: median daily new-condition price (JPY), trade days (days with >=1 new trade), premium vs current JP retail
"""
import csv, glob, gzip, json, os, re, statistics, sys, datetime as dt
from collections import defaultdict

OUT = sys.argv[1]
RAW = os.path.join(OUT, 'raw')
JST = dt.timezone(dt.timedelta(hours=9))

COLLAB = re.compile(r'×| x |travis|off-white|union|fragment|sacai|supreme|a ma mani|stussy|stüssy|wales bonner|kith|patta|j\.?balvin|bad bunny|tom sachs|clot|cactus|sean wotherspoon|aime leon|joe freshgoods|jjjjound|salehe|stone island|cdg|comme des|undercover|mm6|ambush|bape|kaws|nigel sylvester|stranger things|gucci|prada|bode', re.I)


def brand_group(name, brand_id):
    n = name.lower()
    if 'jordan' in n:
        return 'Jordan'
    if n.startswith('nike') or brand_id == 'nike' or ' nike ' in n or '× nike' in n:
        return 'Nike'
    for b, key in [('adidas', 'adidas'), ('New Balance', 'new balance'), ('ASICS', 'asics'), ('Onitsuka Tiger', 'onitsuka'),
                   ('On', 'on cloud'), ('Hoka', 'hoka'), ('Salomon', 'salomon'), ('Puma', 'puma')]:
        if key in n:
            return b
    if (brand_id or '').lower() in ('on', 'on-running'):
        return 'On'
    return (brand_id or 'other')


LINE_RULES = [  # (line, brand group, regex on name)
    ('Dunk Low', 'Nike', r'dunk low'), ('SB Dunk', 'Nike', r'sb dunk'), ('Air Force 1', 'Nike', r'air force 1'),
    ('Pegasus', 'Nike', r'pegasus'), ('Vomero', 'Nike', r'vomero'), ('Air Max 1', 'Nike', r'air max 1\b'),
    ('P-6000', 'Nike', r'p-6000'), ('Cortez', 'Nike', r'cortez'),
    ('AJ1 High', 'Jordan', r'jordan 1 (retro )?high'), ('AJ1 Low', 'Jordan', r'jordan 1 (retro )?low'),
    ('AJ4', 'Jordan', r'jordan 4\b'), ('AJ11', 'Jordan', r'jordan 11\b'),
    ('Samba', 'adidas', r'samba'), ('Gazelle', 'adidas', r'gazelle'), ('Spezial', 'adidas', r'spezial'),
    ('Campus', 'adidas', r'campus'), ('Superstar', 'adidas', r'superstar'), ('Taekwondo', 'adidas', r'taekwondo'),
    ('550', 'New Balance', r'\b(bb)?550\b'), ('2002R', 'New Balance', r'2002r'), ('1906', 'New Balance', r'1906'),
    ('990', 'New Balance', r'\b990'), ('9060', 'New Balance', r'9060'), ('1000', 'New Balance', r'\b1000\b'),
    ('Gel-Kayano 14', 'ASICS', r'kayano 14'), ('Gel-1130', 'ASICS', r'1130'), ('Gel-NYC', 'ASICS', r'gel-nyc'),
    ('Mexico 66', 'Onitsuka Tiger', r'mexico 66'), ('Cloud', 'On', r'cloud'), ('Hoka', 'Hoka', r'hoka'),
    ('XT-6', 'Salomon', r'xt-6'), ('Speedcat', 'Puma', r'speedcat'),
]


def model_line(name, bg):
    n = name.lower()
    for line, b, rx in LINE_RULES:
        if b == bg and re.search(rx, n):
            return line
    return 'other ' + bg


def main():
    prows, mrows = [], []
    seen = set()
    for f in sorted(glob.glob(os.path.join(RAW, 'snkrdunk_history_s*.jsonl.gz'))):
        import zlib
        text = zlib.decompressobj(31).decompress(open(f, 'rb').read()).decode('utf-8', 'ignore')  # tolerant of an unfinished stream
        if True:
            for ln in text.splitlines():
                try:
                    r = json.loads(ln)
                except Exception:
                    continue  # truncated last line
                if r['code'] in seen or not r.get('jp_id'):
                    continue
                seen.add(r['code'])
                name = r.get('name_en') or r.get('name') or ''
                bg = brand_group(name, r.get('brand_id'))
                line = model_line(name, bg)
                rel = (r.get('released_jp') or '')[:10]
                retail = r.get('retail_jpy')
                pts = r.get('points') or []
                bym = defaultdict(list)
                for ts, price in pts:
                    d = dt.datetime.fromtimestamp(ts / 1000, JST).date()
                    bym[d.strftime('%Y-%m')].append(price)
                trades = r.get('trades') or []
                vel = None
                if len(trades) >= 2:
                    t0 = dt.datetime.fromisoformat(trades[0]['soldAt'].replace('Z', '+00:00'))
                    t1 = dt.datetime.fromisoformat(trades[-1]['soldAt'].replace('Z', '+00:00'))
                    days = max((t0 - t1).total_seconds() / 86400, 0.04)
                    vel = round((len(trades) - 1) / days, 3)
                last_trade = trades[0]['soldAt'][:10] if trades else ''
                prows.append({'code': r['code'], 'jp_id': r['jp_id'], 'name': name, 'brand_group': bg, 'model_line': line,
                              'collab': int(bool(COLLAB.search(name))), 'search_kw': r.get('kw'), 'search_rank': r.get('search_rank'),
                              'released_jp': rel, 'retail_jpy': retail, 'n_trade_days_all': len(pts),
                              'first_trade_day': dt.datetime.fromtimestamp(pts[0][0] / 1000, JST).date().isoformat() if pts else '',
                              'last_trade_ts': last_trade, 'trades_per_day_last20': vel, 'pulled_utc': r.get('pulled_utc')})
                for m, ps in sorted(bym.items()):
                    med = statistics.median(ps)
                    mrows.append({'code': r['code'], 'brand_group': bg, 'model_line': line, 'collab': int(bool(COLLAB.search(name))),
                                  'released_jp': rel, 'month': m, 'trade_days': len(ps), 'median_daily_price_jpy': round(med),
                                  'retail_jpy': retail, 'premium_vs_retail': round(med / retail - 1, 4) if retail else ''})
    for fn, rows in [('snkrdunk_products.csv', prows), ('snkrdunk_product_month.csv', mrows)]:
        with open(os.path.join(OUT, fn), 'w', newline='') as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0]))
            w.writeheader(); w.writerows(rows)
        print(fn, len(rows))


if __name__ == '__main__':
    main()
