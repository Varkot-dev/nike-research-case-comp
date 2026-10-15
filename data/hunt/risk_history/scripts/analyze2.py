"""Extra cuts: base rates, cost-relief windows, magnitude match, list of GM-up cases.
Usage: python3 -I analyze2.py events_all.csv"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.argv = [sys.argv[0], sys.argv[1], 'none']
from analyze import ev, dedupe, line, nk, ngp, ngm, NONCONS
import datetime as dt
C = [r for r in ev if r['t'] not in NONCONS]
base = dedupe([r for r in C if nk(r)])
allev = dedupe(C)
print('== C1. base rates, all drawdown events (deduped), consumer universe ==')
for k in ['x6_^GSPC', 'x12_^GSPC', 'x12_XRT']: print(' ', line('all events ' + k, allev, k))
# cost relief windows: the NEXT quarter (the one whose GM rose) ends inside a known input-cost deflation window
COT = (dt.date(2012, 3, 1), dt.date(2013, 12, 31))   # cotton fell from 2011 peak; apparel GM rebound 2012-13
FRT = (dt.date(2022, 12, 1), dt.date(2024, 9, 30))   # ocean freight and air freight normalised after 2021-22 spike
inw = lambda r, w: r['nqend'] is not None and w[0] <= r['nqend'] <= w[1]
cost = lambda r: inw(r, COT) or inw(r, FRT)
print('\n== C2. Nike path & next GM up, split by cost-relief window (cotton 2012-13, freight 2023-24) ==')
gu = [r for r in base if ngp(r)]
for k in ['x6_^GSPC', 'x12_^GSPC', 'x6_XRT', 'x12_XRT']:
    print(' ', line('GM up in cost-relief window ' + k, [r for r in gu if cost(r)], k))
    print(' ', line('GM up outside windows ' + k, [r for r in gu if not cost(r)], k))
print('\n== C3. magnitude match: next-Q revenue between -14% and -5% (Nike guide about -8% to -11%) ==')
mm = [r for r in base if -0.14 <= r['nx'] <= -0.05]
for k in ['x6_^GSPC', 'x12_^GSPC', 'x12_XRT']:
    print(' ', line('mag match all ' + k, mm, k))
    print(' ', line('mag match next GM up ' + k, [r for r in mm if ngp(r)], k))
    print(' ', line('mag match next GM down ' + k, [r for r in mm if ngm(r)], k))
print('\n== C4. two-quarter persistence: next GM up AND second-next GM up ==')
for k in ['x6_^GSPC', 'x12_^GSPC']:
    print(' ', line('nGM+ & n2GM+ ' + k, [r for r in base if ngp(r) and r['ngy2'] is not None and r['ngy2'] > 0], k))
    print(' ', line('nGM+ & n2GM- ' + k, [r for r in base if ngp(r) and r['ngy2'] is not None and r['ngy2'] <= 0], k))
print('\n== C5. how often did current GM direction persist into the next quarter (Nike path)? ==')
a = [r for r in base if r['gy'] > 0 and r['ngy'] is not None]
print(f'  current GM up -> next GM up: {sum(r["ngy"]>0 for r in a)}/{len(a)}')
b = [r for r in base if r['gy'] <= 0 and r['ngy'] is not None]
print(f'  current GM down -> next GM up: {sum(r["ngy"]>0 for r in b)}/{len(b)}')
print('\n== C6. every Nike-path GM-up-next case (deduped), sorted ==')
for r in sorted(gu, key=lambda r: (r['t'], r['d'])):
    print(f"  {r['t']:5s} {r['d']} dd {r['dd']*100:+4.0f} rev {r['ry']*100:+5.1f} next {r['nx']*100:+5.1f} GMnow {r['gy']:+5.0f} GMnext {r['ngy']:+5.0f} OMnext {(r['noy'] or 0):+6.0f} cost={'Y' if cost(r) else 'n'} x6 {r['x6_^GSPC']*100:+4.0f} x12 {r['x12_^GSPC']*100:+4.0f} x12xrt {r['x12_XRT']*100:+4.0f} min12 {r['min12']*100:+4.0f}")
print('\n== C7. every Nike-path GM-down-next case ==')
for r in sorted([r for r in base if ngm(r)], key=lambda r: (r['t'], r['d'])):
    print(f"  {r['t']:5s} {r['d']} rev {r['ry']*100:+5.1f} next {r['nx']*100:+5.1f} GMnow {r['gy']:+5.0f} GMnext {r['ngy']:+5.0f} x6 {r['x6_^GSPC']*100:+4.0f} x12 {r['x12_^GSPC']*100:+4.0f}")
