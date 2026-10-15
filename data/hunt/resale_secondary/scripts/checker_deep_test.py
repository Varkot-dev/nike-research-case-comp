"""Checker: compare the hunter's top-150 sample with ranks 151-200 (search page 4) for 8 lines.
Usage: python3 -I checker_deep_test.py HUNTDIR
Writes HUNTDIR/checker_deep_rank_compare.csv
"""
import csv, glob, gzip, json, math, os, statistics as st, sys, zlib, datetime as dt
from collections import defaultdict

D = sys.argv[1]
JST = dt.timezone(dt.timedelta(hours=9))
LINES = {'nike dunk low': 'NJ', 'air jordan 1 high': 'NJ', 'nike air force 1': 'NJ', 'air jordan 4': 'NJ',
         'adidas samba': 'RV', 'adidas gazelle': 'RV', 'new balance 2002r': 'RV', 'onitsuka tiger mexico 66': 'RV'}


def madd(m, k):
    y, mo = int(m[:4]), int(m[5:]) + k
    while mo > 12: y += 1; mo -= 12
    while mo < 1: y -= 1; mo += 12
    return '%04d-%02d' % (y, mo)


import re
COLLAB = re.compile(r'×| x |travis|off-white|union|fragment|sacai|supreme|a ma mani|stussy|stüssy|wales bonner|kith|patta|j\.?balvin|bad bunny|tom sachs|clot|cactus|sean wotherspoon|aime leon|joe freshgoods|jjjjound|salehe|stone island|cdg|comme des|undercover|mm6|ambush|bape|kaws|nigel sylvester|stranger things|gucci|prada|bode', re.I)

prods = {}  # code -> dict(kw, band, rel, retail, collab, bym)
# top 150: from hunter tidy files
P = {p['code']: p for p in csv.DictReader(open(os.path.join(D, 'snkrdunk_products.csv')))}
for p in P.values():
    if p['search_kw'] in LINES:
        prods[p['code']] = {'kw': p['search_kw'], 'band': 'top150', 'rel': p['released_jp'][:10], 'retail': float(p['retail_jpy'] or 0),
                            'collab': p['collab'] == '1', 'bym': defaultdict(list)}
for r in csv.DictReader(open(os.path.join(D, 'snkrdunk_product_month.csv'))):
    if r['code'] in prods:
        prods[r['code']]['bym'][r['month']] = (int(r['trade_days']), float(r['median_daily_price_jpy']))
# deep ranks
for f in sorted(glob.glob(os.path.join(D, 'raw', 'checker_deep*.jsonl.gz'))):
    for ln in zlib.decompressobj(31).decompress(open(f, 'rb').read()).decode('utf-8', 'ignore').splitlines():
        try: r = json.loads(ln)
        except Exception: continue
        if not r.get('jp_id') or r['code'] in prods: continue
        name = r.get('name_en') or r.get('name') or ''
        bym = defaultdict(list)
        for ts, pr in r.get('points') or []:
            bym[dt.datetime.fromtimestamp(ts / 1000, JST).strftime('%Y-%m')].append(pr)
        prods[r['code']] = {'kw': r['kw'], 'band': 'rank151_200', 'rel': (r.get('released_jp') or '')[:10], 'retail': float(r.get('retail_jpy') or 0),
                            'collab': bool(COLLAB.search(name)), 'bym': {m: (len(v), st.median(v)) for m, v in bym.items()}}

rows = []
for band in ('top150', 'rank151_200'):
    for grp in ('NJ', 'RV'):
        S = [p for p in prods.values() if p['band'] == band and LINES[p['kw']] == grp]
        # trade days Jan-Sep
        t = {y: sum(v[0] for p in S for m, v in p['bym'].items() if m[:4] == y and m[5:] <= '09') for y in ('2025', '2026')}
        tc = {y: sum(v[0] for p in S if p['rel'] and p['rel'][:7] < '2025-01' for m, v in p['bym'].items() if m[:4] == y and m[5:] <= '09') for y in ('2025', '2026')}
        # Q3 same-product YoY
        q = {}
        for yr in ('2025', '2026'):
            v = []
            for m in [yr + '-07', yr + '-08', yr + '-09']:
                m0 = madd(m, -12)
                for p in S:
                    if p['collab'] or (p['rel'] and p['rel'][:7] > madd(m0, -6)): continue
                    a, b = p['bym'].get(m), p['bym'].get(m0)
                    if a and b and a[0] >= 3 and b[0] >= 3: v.append(math.log(a[1] / b[1]))
            q[yr] = (round(math.exp(st.median(v)) - 1, 3) if v else '', len(v))
        # launch premium
        lp = {}
        for h, (lo, hi) in {'2025': ('2025-01-01', '2025-12-31'), '2026H1': ('2026-01-01', '2026-06-30')}.items():
            v = []
            for p in S:
                if p['collab'] or not p['rel'] or not p['retail'] or not (lo <= p['rel'] <= hi): continue
                ps = [p['bym'][madd(p['rel'][:7], k)][1] for k in (1, 2, 3) if madd(p['rel'][:7], k) in p['bym']]
                if ps: v.append(st.median(ps) / p['retail'] - 1)
            lp[h] = (round(st.median(v), 3) if v else '', len(v), round(sum(x < 0 for x in v) / len(v), 3) if v else '')
        rows.append({'band': band, 'group': grp, 'n_products': len(S), 'td_jan_sep_2025': t['2025'], 'td_jan_sep_2026': t['2026'],
                     'td_yoy': round(t['2026'] / t['2025'] - 1, 3) if t['2025'] else '',
                     'td_yoy_released_pre2025': round(tc['2026'] / tc['2025'] - 1, 3) if tc['2025'] else '',
                     'q3_yoy_2025': q['2025'][0], 'n_q3_2025': q['2025'][1], 'q3_yoy_2026': q['2026'][0], 'n_q3_2026': q['2026'][1],
                     'launch_prem_2025': lp['2025'][0], 'n_launch_2025': lp['2025'][1], 'launch_prem_2026H1': lp['2026H1'][0], 'n_launch_2026H1': lp['2026H1'][1],
                     'below_retail_2025': lp['2025'][2], 'below_retail_2026H1': lp['2026H1'][2]})
with open(os.path.join(D, 'checker_deep_rank_compare.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
for r in rows: print(r)
