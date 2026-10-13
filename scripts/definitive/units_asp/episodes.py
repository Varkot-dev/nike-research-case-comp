"""DERIVED: classify each quarter's units/ASP pattern for the reset episodes.
Usage: python3 -I episodes.py <tidy.csv> <out.csv>
Rule (pre-registered test 5):
  supply_cut_pattern  : units < 0 and ASP >= 0 (ASP stable or rising)
  discount_pattern    : ASP < 0 and stated drivers include 'discount' or 'promotional' or 'off-price'
  units_flat_rev_down : units == 0 and ASP < 0 (disproof condition)
  both_down / volume_up_price_down / growth otherwise
rev_proxy_pct = units + ASP (pp contribution), my arithmetic; Nike states the two add to currency-neutral revenue change approximately.
"""
import sys, csv, re

IN, OUT = sys.argv[1], sys.argv[2]
rows = [r for r in csv.DictReader(open(IN)) if r['source_rank'] == 'primary' and r['period'][:2] in ('Q1', 'Q2', 'Q3', 'FY')]
EP = [('FY2018 reset', 2017, 2019), ('FY2023 inventory glut', 2022, 2024), ('FY2025 to Q1 FY2027 cleanup', 2024, 2027)]
out = []
for r in rows:
    y = int(re.search(r'(\d{4})', r['period']).group(1))
    if r['segment'] not in ('NIKE Brand', 'North America', 'Greater China', 'EMEA', 'APLA', 'Converse'):
        continue
    if r['units_change_pct'] == '' or r['asp_change_pct'] == '':
        continue
    u, a = float(r['units_change_pct']), float(r['asp_change_pct'])
    dtext = (r['asp_drivers_text'] + ' ' + r['quote']).lower()
    disc = bool(re.search(r'discount|promotional|off-price|clearance', dtext))
    lower_disc = 'lower discounts' in dtext
    if u == 0 and a < 0:
        cls = 'units_flat_rev_down'
    elif u < 0 and a >= 0:
        cls = 'supply_cut_pattern'
    elif u < 0 and a < 0:
        cls = 'both_down' + ('_discount' if disc and not lower_disc else '')
    elif u > 0 and a < 0:
        cls = 'volume_up_price_down' + ('_discount' if disc and not lower_disc else '')
    else:
        cls = 'growth_or_flat'
    eps = [n for n, a0, a1 in EP if a0 <= y <= a1]
    out.append(dict(period=r['period'], segment=r['segment'], category=r['category'], units_change_pct=r['units_change_pct'],
                    asp_change_pct=r['asp_change_pct'], asp_measure=r['asp_measure'],
                    rev_proxy_pct_derived=f'{u + a:g}' if r['asp_measure'] in ('pp_contribution', 'flat', 'slightly_up', 'slightly_down') else '',
                    pattern_derived=cls, discount_cited=int(disc), lower_discounts_cited=int(lower_disc), episodes=';'.join(eps),
                    filing=r['filing'], printed_page=r['printed_page']))
with open(OUT, 'w', newline='') as fo:
    w = csv.DictWriter(fo, fieldnames=list(out[0].keys()))
    w.writeheader()
    w.writerows(out)
print(len(out))
