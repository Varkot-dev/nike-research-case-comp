"""Robustness checks run after tests.py. Usage: python3 -I robustness.py OUTDIR
1) same-product YoY price change by model line and brand, Q3 2024/2025/2026 (Jul-Sep), thresholds 3 and 1 trade-days
2) trade-days Jan-Sep by brand, YoY (writes test_B3_trade_days_jan_sep_yoy_by_brand.csv)
3) launch premium bootstrap CIs, diff-in-diff vs rivals, and within-model-line (mix-adjusted) change
"""
import csv, math, os, random, statistics as st, sys, collections
from collections import defaultdict
OUT = sys.argv[1]; os.chdir(OUT)
P = {p['code']: p for p in csv.DictReader(open('snkrdunk_products.csv'))}
pm = list(csv.DictReader(open('snkrdunk_product_month.csv')))
pr = {(r['code'], r['month']): float(r['median_daily_price_jpy']) for r in pm}
td = {(r['code'], r['month']): int(r['trade_days']) for r in pm}
NJB = ('Nike', 'Jordan'); RVB = ('adidas', 'New Balance', 'ASICS', 'Onitsuka Tiger', 'On', 'Hoka', 'Salomon', 'Puma')


def madd(m, k):
    y, mo = int(m[:4]), int(m[5:]) + k
    while mo > 12: y += 1; mo -= 12
    while mo < 1: y -= 1; mo += 12
    return '%04d-%02d' % (y, mo)


def yoy(f, months, thr=3):
    v = []
    for m in months:
        m0 = madd(m, -12)
        for c, p in P.items():
            if p['collab'] == '1' or not f(p): continue
            rel = p['released_jp'][:7]
            if rel and rel > madd(m0, -6): continue
            if (c, m) in pr and (c, m0) in pr and td[(c, m)] >= thr and td[(c, m0)] >= thr:
                v.append(math.log(pr[(c, m)] / pr[(c, m0)]))
    return (round(math.exp(st.median(v)) - 1, 3), len(v)) if v else None


Q = {y: ['%s-07' % y, '%s-08' % y, '%s-09' % y] for y in ('2024', '2025', '2026')}
rows = []
lines = sorted(set(p['model_line'] for p in P.values()))
for kind, keys, fn in [('line', lines, lambda k: (lambda p: p['model_line'] == k)),
                       ('brand', ['Nike', 'Jordan', 'adidas', 'New Balance', 'ASICS', 'Onitsuka Tiger'], lambda k: (lambda p: p['brand_group'] == k)),
                       ('group', ['Nike+Jordan', 'Rivals'], lambda k: (lambda p: p['brand_group'] in (NJB if k == 'Nike+Jordan' else RVB)))]:
    for k in keys:
        row = {'kind': kind, 'key': k}
        for y in Q:
            r = yoy(fn(k), Q[y]); row['yoy_q3_%s' % y] = r[0] if r else ''; row['n_q3_%s' % y] = r[1] if r else 0
        r1 = yoy(fn(k), Q['2026'], 1); row['yoy_q3_2026_thr1'] = r1[0] if r1 else ''
        rows.append(row)
with open('test_A2_q3_yoy_by_line_brand.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
for r in rows:
    if r['n_q3_2026'] >= 10: print(r)

s = defaultdict(lambda: defaultdict(int))
for r in pm:
    if r['month'][5:] <= '09': s[r['brand_group']][r['month'][:4]] += int(r['trade_days'])
out = []
for b in ['Nike', 'Jordan', 'adidas', 'New Balance', 'ASICS', 'Onitsuka Tiger', 'Puma', 'Salomon', 'Hoka', 'On']:
    d = s[b]
    out.append({'brand': b, 'td_jan_sep_2024': d['2024'], 'td_jan_sep_2025': d['2025'], 'td_jan_sep_2026': d['2026'],
                'yoy_2025': round(d['2025'] / d['2024'] - 1, 3) if d['2024'] else '', 'yoy_2026': round(d['2026'] / d['2025'] - 1, 3) if d['2025'] else ''})
with open('test_B3_trade_days_jan_sep_yoy_by_brand.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
NJ = [sum(s[b][y] for b in NJB) for y in ('2024', '2025', '2026')]; RV = [sum(s[b][y] for b in s if b not in NJB) for y in ('2024', '2025', '2026')]
print('trade-days Jan-Sep NJ', NJ, 'RV', RV, 'NJ share', [round(NJ[i] / (NJ[i] + RV[i]), 3) for i in range(3)])

r = list(csv.DictReader(open('test_C_launch_premium_products.csv')))
g = lambda bs, hs: [float(x['premium_m1_m3']) for x in r if x['brand_group'] in bs and x['release_half'] in hs]
a, b, c, d = g(NJB, ['2026H1']), g(NJB, ['2025H1', '2025H2']), g(RVB, ['2026H1']), g(RVB, ['2025H1', '2025H2'])
random.seed(2); ds = []
for _ in range(5000):
    rs = lambda x: st.median(random.choices(x, k=len(x)))
    ds.append((rs(a) - rs(b)) - (rs(c) - rs(d)))
ds.sort()
print('launch premium NJ 2026H1 %.3f (n=%d) vs 2025 %.3f (n=%d); RV %.3f (n=%d) vs %.3f (n=%d); DiD %.3f CI95 (%.3f, %.3f)' % (
    st.median(a), len(a), st.median(b), len(b), st.median(c), len(c), st.median(d), len(d),
    (st.median(a) - st.median(b)) - (st.median(c) - st.median(d)), ds[125], ds[4875]))
for nm, bs in [('NJ', NJB), ('RV', RVB)]:
    A = defaultdict(list); B = defaultdict(list)
    for x in r:
        if x['brand_group'] in bs and x['release_half'] in ('2025H1', '2025H2'): A[x['model_line']].append(float(x['premium_m1_m3']))
        if x['brand_group'] in bs and x['release_half'] == '2026H1': B[x['model_line']].append(float(x['premium_m1_m3']))
    common = [l for l in A if l in B and len(A[l]) >= 2 and len(B[l]) >= 2]
    diffs = [st.median(B[l]) - st.median(A[l]) for l in common]; wts = [len(B[l]) for l in common]
    print(nm, 'within-line change mean %.3f weighted %.3f lines %d' % (st.mean(diffs), sum(x * y for x, y in zip(diffs, wts)) / sum(wts), len(common)))
