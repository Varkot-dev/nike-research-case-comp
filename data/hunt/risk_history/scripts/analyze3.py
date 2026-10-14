"""Robustness: drop distressed repeaters, brand-only subset, ex-ante combos closest to Nike.
Usage: python3 -I analyze3.py events_all.csv"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.argv = [sys.argv[0], sys.argv[1], 'none']
from analyze import ev, dedupe, line, nk, ngp, ngm, NONCONS
BRANDS = set("UAA VFC LULU PVH CROX DECK CPRI TPR RL COLM LEVI HBI SKX EL HAS MAT GAP KTB YETI ELF COTY WWW SHOO FOSL OXM GIII CRI VRA".split())
C = [r for r in ev if r['t'] not in NONCONS]
base = dedupe([r for r in C if nk(r)])
K = ['x6_^GSPC', 'x12_^GSPC', 'x12_XRT']
def show(name, rs):
    for k in K: print(' ', line(f'{name} {k}', rs, k))
print('== R1. drop FOSL and PTON ==')
b2 = [r for r in base if r['t'] not in ('FOSL', 'PTON')]
show('nGM+', [r for r in b2 if ngp(r)]); show('nGM-', [r for r in b2 if ngm(r)])
print('== R2. brand owners only (no pure retailers) ==')
b3 = [r for r in base if r['t'] in BRANDS]
show('brands nGM+', [r for r in b3 if ngp(r)]); show('brands nGM-', [r for r in b3 if ngm(r)])
print('== R3. ex-ante: current GM up AND next OM down (Nike Q1 FY27 +61bp, guide says EBIT falls faster than revenue) ==')
show('curGM+ & nOM-', [r for r in base if r['gy'] > 0 and r['noy'] is not None and r['noy'] <= 0])
show('curGM+ & nGM+ & nOM-', [r for r in base if r['gy'] > 0 and ngp(r) and r['noy'] is not None and r['noy'] <= 0])
print('== R4. drawdown >= 75% only (Nike about 80% below its 2021 high) ==')
b4 = [r for r in base if r['dd'] <= -0.75]
show('dd75 nGM+', [r for r in b4 if ngp(r)]); show('dd75 nGM-', [r for r in b4 if ngm(r)])
print('== R5. worst point within 12 months, nGM+ bucket ==')
import statistics as st
g = [r for r in base if ngp(r)]
print('  median min12', round(st.median(r['min12'] for r in g) * 100), ' share with min12 <= -25%:', sum(r['min12'] <= -0.25 for r in g), '/', len(g))
