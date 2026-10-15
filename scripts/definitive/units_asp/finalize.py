"""Finalize tidy CSV: overrides, dedupe preference, value-in-quote check.
Usage: python3 -I finalize.py <parsed.csv> <out_tidy.csv>
"""
import sys, csv, re, collections

IN, OUT = sys.argv[1], sys.argv[2]
rows = list(csv.DictReader(open(IN)))
# Manual fixes after reading each quote (mixed verbs, per-period ASP sentences, 'higher ASP reduced the impact of lower revenues')
FIX = {
    ('6MFY2017', 'Central & Eastern Europe', 'apparel'): ('units_change_pct', '2', None),
    ('9MFY2017', 'Central & Eastern Europe', 'apparel'): ('asp_change_pct', '1', None),
    ('9MFY2017', 'Converse', 'comparable_direct_distribution_total'): ('units_change_pct', '2', None),
    ('6MFY2019', 'Converse', 'comparable_direct_distribution_total'): ('units_change_pct', '0', None),
    ('6MFY2018', 'Greater China', 'footwear'): ('asp_change_pct', '-1', None),
    ('Q3FY2018', 'EMEA', 'footwear'): ('asp_change_pct', '1', None),
    ('Q2FY2018', 'North America', 'footwear'): ('asp_change_pct', '4', None),
    ('Q3FY2018', 'North America', 'footwear'): ('asp_change_pct', '1', None),
    ('9MFY2018', 'North America', 'footwear'): ('asp_change_pct', '1', None),
}
out = []
for r in rows:
    if r['period'].endswith('2016'):
        continue
    if r['category'] == 'UNKNOWN':
        continue  # Q2 FY2026 NA "ASP was flat" sits inside a gross margin bullet, not a units/ASP revenue statement
    if r['period'] == '9MFY2021' and r['segment'] == 'Greater China' and r['category'] == 'apparel':
        r['asp_change_pct'] = '-4'
        r['asp_measure'] = 'pp_contribution'
        r['printed_page'] = '36-37'
        r['quote'] += ' percentage points. Lower ASP was driven by lower NIKE Direct ASP and unfavorable full-price mix, partially offset by higher off-price ASP.'
        r['asp_drivers_text'] = 'Lower ASP was driven by lower NIKE Direct ASP and unfavorable full-price mix, partially offset by higher off-price ASP.'
        r['flags'] = 'quote_spans_page_break'
    if r['printed_page'] == 'n/a' and r['file'].startswith('10-K_2019-05-31'):
        r['printed_page'] = str(int(r['seq_page']) - 2)  # footer missing on this page; FY19 10-K offset is constant 2 (seq 31 = p. 29, seq 33 = p. 31)
        r['flags'] = (r['flags'] + ';printed_page_from_offset').strip(';')
    fx = FIX.get((r['period'], r['segment'], r['category']))
    if fx and (fx[2] is None or r['filing'] == fx[2]):
        col, val = fx[0], fx[1]
        r[col] = val
        r['flags'] = (r['flags'] + ';manual_fix_' + col).strip(';')
    out.append(r)


def own(r):
    f = r['filing']
    m = re.match(r'(FY|Q(\d) FY)(\d{4})', f)
    if f.startswith('FY'):
        return r['period'] == 'FY' + m.group(3)
    return r['period'].endswith('FY' + m.group(3))


groups = collections.defaultdict(list)
for r in out:
    groups[(r['period'], r['segment'], r['category'])].append(r)
for k, g in groups.items():
    prim = [r for r in g if own(r)] or g[:1]
    for r in g:
        r['source_rank'] = 'primary' if r is prim[0] else 'repeat_in_later_filing'
    vals = {(r['units_change_pct'], r['asp_change_pct']) for r in g}
    if len(vals) > 1:
        for r in g:
            r['flags'] = (r['flags'] + ';conflict_across_filings').strip(';')

# value-in-quote check
for r in out:
    q = r['quote']
    for col in ('units_change_pct', 'asp_change_pct'):
        v = r[col]
        if v == '':
            continue
        n = str(abs(float(v))).rstrip('0').rstrip('.')
        ok = (n == '0' and re.search(r'flat|unchanged|slightly', q)) or re.search(r'\b' + re.escape(n) + r'(%| percentage| and \d)', q) or re.search(r'and ' + re.escape(n) + r'(%| percentage)', q)
        if not ok:
            r['flags'] = (r['flags'] + f';{col}_not_in_quote').strip(';')

for r in out:
    for c in r:
        if isinstance(r[c], str):
            r[c] = r[c].replace(chr(8212), '-').replace(chr(8211), '-')

order = lambda r: (int(re.search(r'(\d{4})', r['period']).group(1)), {'Q1': 1, 'Q2': 2, '6M': 2.5, 'Q3': 3, '9M': 3.5, 'FY': 5}[r['period'][:2]], r['segment'], r['category'])
out.sort(key=order)
cols = ['period', 'period_type', 'segment', 'category', 'units_change_pct', 'asp_change_pct', 'asp_measure', 'asp_drivers_text',
        'filing', 'printed_page', 'quote', 'source_rank', 'flags', 'file', 'seq_page']
for r in out:
    r['period_type'] = {'Q': 'quarter', '6': 'ytd_6m', '9': 'ytd_9m', 'F': 'fiscal_year'}[r['period'][0]]
with open(OUT, 'w', newline='') as fo:
    w = csv.DictWriter(fo, fieldnames=cols, extrasaction='ignore')
    w.writeheader()
    w.writerows(out)
print(len(out), 'rows;', collections.Counter(r['flags'] for r in out))
