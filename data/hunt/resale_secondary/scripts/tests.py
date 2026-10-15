"""Run resale tests on tidy CSVs. Usage: python3 -I tests.py OUTDIR
Writes test_*.csv to OUTDIR and prints summaries.
"""
import csv, math, os, statistics as st, sys
from collections import defaultdict

OUT = sys.argv[1]
BR = ['Nike', 'Jordan', 'adidas', 'New Balance', 'ASICS', 'Onitsuka Tiger', 'On', 'Hoka', 'Salomon', 'Puma']
RIVALS = {'adidas', 'New Balance', 'ASICS', 'Onitsuka Tiger', 'On', 'Hoka', 'Salomon', 'Puma'}


def rd(fn):
    return list(csv.DictReader(open(os.path.join(OUT, fn))))


def wr(fn, rows):
    if not rows:
        return
    with open(os.path.join(OUT, fn), 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)


def madd(m, k):
    y, mo = int(m[:4]), int(m[5:7]) + k
    while mo > 12: y += 1; mo -= 12
    while mo < 1: y -= 1; mo += 12
    return '%04d-%02d' % (y, mo)


prods = {p['code']: p for p in rd('snkrdunk_products.csv')}
pm = rd('snkrdunk_product_month.csv')
price = {(r['code'], r['month']): float(r['median_daily_price_jpy']) for r in pm}
tdays = {(r['code'], r['month']): int(r['trade_days']) for r in pm}
months = sorted(set(r['month'] for r in pm))
months = [m for m in months if '2021-06' <= m <= '2026-09']  # Oct 2026 partial, excluded

# ---------- Test A: same-product YoY resale price change (new condition), by brand ----------
rowsA = []
for m in months:
    if m < '2022-06':
        continue
    m0 = madd(m, -12)
    acc = defaultdict(list)
    for code, p in prods.items():
        if p['collab'] == '1':
            continue
        rel = p['released_jp'][:7]
        if rel and rel > madd(m0, -6):   # require product released >= 6 months before base month (skip launch decay)
            continue
        if (code, m) in price and (code, m0) in price and tdays[(code, m)] >= 3 and tdays[(code, m0)] >= 3:
            acc[p['brand_group']].append(math.log(price[(code, m)] / price[(code, m0)]))
            if p['brand_group'] in ('Nike', 'Jordan'):
                acc['Nike+Jordan'].append(acc[p['brand_group']][-1])
            elif p['brand_group'] in RIVALS:
                acc['Rivals'].append(acc[p['brand_group']][-1])
            if p['model_line'] in ('Dunk Low', 'Air Force 1', 'AJ1 High', 'AJ1 Low', 'AJ4'):
                acc['Classics(Dunk,AF1,AJ1,AJ4)'].append(acc[p['brand_group']][-1])
    for b, v in acc.items():
        rowsA.append({'month': m, 'group': b, 'n_products': len(v), 'median_yoy_log_change': round(st.median(v), 4),
                      'median_yoy_pct': round(math.exp(st.median(v)) - 1, 4), 'mean_yoy_log_change': round(st.mean(v), 4)})
wr('test_A_same_product_yoy_price_by_brand.csv', rowsA)

# ---------- Test B: trade-days share and YoY growth by brand ----------
rowsB = []
tot = defaultdict(lambda: defaultdict(int))
for (code, m), d in tdays.items():
    p = prods[code]
    tot[m][p['brand_group']] += d
for m in months:
    T = sum(v for b, v in tot[m].items() if b in BR)
    nj = tot[m]['Nike'] + tot[m]['Jordan']
    row = {'month': m, 'trade_days_all_brands': T, 'nike_jordan_trade_days': nj, 'nike_jordan_share': round(nj / T, 4) if T else ''}
    for b in BR:
        row['td_' + b] = tot[m][b]
    rowsB.append(row)
wr('test_B_trade_days_by_brand_month.csv', rowsB)

# fixed-cohort version: only products released before 2024-01 (removes new-product entry)
rowsB2 = []
for m in months:
    acc = defaultdict(int)
    for code, p in prods.items():
        if p['released_jp'] and p['released_jp'][:7] < '2024-01' and (code, m) in tdays:
            acc[p['brand_group']] += tdays[(code, m)]
    T = sum(v for b, v in acc.items() if b in BR)
    rowsB2.append({'month': m, 'cohort': 'released_before_2024', 'total': T, 'nike_jordan_share': round((acc['Nike'] + acc['Jordan']) / T, 4) if T else '',
                   **{'td_' + b: acc[b] for b in BR}})
wr('test_B2_trade_days_fixed_cohort.csv', rowsB2)

# ---------- Test C: launch reception, premium vs JP retail 30-120 days after release ----------
import datetime as dt
rowsC = []
cell = defaultdict(list)
for code, p in prods.items():
    if p['collab'] == '1' or not p['released_jp'] or not p['retail_jpy']:
        continue
    rel = dt.date.fromisoformat(p['released_jp'][:10])
    if rel < dt.date(2021, 7, 1) or rel > dt.date(2026, 6, 30):
        continue
    ms = [madd(rel.strftime('%Y-%m'), k) for k in (1, 2, 3)]
    ps = [price[(code, m)] for m in ms if (code, m) in price]
    if not ps:
        continue
    prem = st.median(ps) / float(p['retail_jpy']) - 1
    half = '%dH%d' % (rel.year, 1 if rel.month <= 6 else 2)
    bg = p['brand_group']
    grp = 'Nike+Jordan' if bg in ('Nike', 'Jordan') else ('Rivals' if bg in RIVALS else None)
    for g in [bg, grp]:
        if g:
            cell[(g, half)].append(prem)
    rowsC.append({'code': code, 'name': p['name'], 'brand_group': bg, 'model_line': p['model_line'], 'released_jp': p['released_jp'][:10],
                  'retail_jpy': p['retail_jpy'], 'median_price_m1_m3_jpy': round(st.median(ps)), 'premium_m1_m3': round(prem, 4), 'release_half': half})
wr('test_C_launch_premium_products.csv', rowsC)
rowsC2 = []
for (g, h), v in sorted(cell.items(), key=lambda x: (x[0][0], x[0][1])):
    rowsC2.append({'group': g, 'release_half': h, 'n_releases': len(v), 'median_premium_m1_m3': round(st.median(v), 4),
                   'share_below_retail': round(sum(1 for x in v if x < 0) / len(v), 4)})
wr('test_C_launch_premium_by_brand_half.csv', rowsC2)

# ---------- print summaries ----------
def show(rows, keys, flt):
    for r in rows:
        if flt(r):
            print({k: r[k] for k in keys})

print('\n== Test A: same-product YoY price change (median), selected months')
for g in ['Nike', 'Jordan', 'Nike+Jordan', 'Classics(Dunk,AF1,AJ1,AJ4)', 'adidas', 'New Balance', 'ASICS', 'Onitsuka Tiger', 'Rivals']:
    s = [(r['month'], r['median_yoy_pct'], r['n_products']) for r in rowsA if r['group'] == g and r['month'][5:] in ('03', '06', '09')]
    print(g, s)
print('\n== Test B: Nike+Jordan share of trade-days (all products), Sep each year; fixed cohort')
print([(r['month'], r['nike_jordan_share'], r['trade_days_all_brands']) for r in rowsB if r['month'][5:] in ('03', '09')])
print([(r['month'], r['nike_jordan_share'], r['total']) for r in rowsB2 if r['month'][5:] in ('03', '09')])
print('\n== Test C: launch premium by brand and release half')
for g in ['Nike', 'Jordan', 'Nike+Jordan', 'adidas', 'New Balance', 'ASICS', 'Onitsuka Tiger', 'On', 'Rivals']:
    print(g, [(r['release_half'], r['median_premium_m1_m3'], r['share_below_retail'], r['n_releases']) for r in rowsC2 if r['group'] == g])
