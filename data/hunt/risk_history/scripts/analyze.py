"""Bucket analysis with Wilson and company-cluster bootstrap intervals.
Usage: python3 -I analyze.py events_all.csv [section]"""
import sys, csv, random, statistics as st, math, datetime as dt
D = dt.date.fromisoformat
APP = set("NKE UAA VFC LULU PVH CROX DECK CPRI TPR RL COLM WWW FOSL LEVI CRI GIII OXM VRA SHOO HBI SKX GAP KSS M URBN ANF AEO ZUMZ BBWI BOOT FL GES CHS EXPR".split())
OTH = set("SBUX EL PTON PYPL NWL MAT HAS CMG TGT INTC KHC".split())
ORIG = APP | OTH
NONCONS = set("PYPL INTC KHC CMG SBUX".split())
ev = []
for r in csv.DictReader(open(sys.argv[1])):
    for k, v in list(r.items()):
        if k in ('t', 'mode'): continue
        if k in ('d', 'qend', 'nqend'): r[k] = D(v) if v else None
        else: r[k] = float(v) if v not in ('', 'None') else None
    ev.append(r)
def wilson(k, n, z=1.96):
    if n == 0: return (0, 0)
    p = k / n; den = 1 + z * z / n; c = (p + z * z / (2 * n)) / den; h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return (c - h, c + h)
def boot(rs, key, B=2000, seed=1):
    cos = sorted(set(r['t'] for r in rs)); by = {c: [r for r in rs if r['t'] == c] for c in cos}
    rnd = random.Random(seed); hs = []; ms = []
    for _ in range(B):
        s = [x for c in (rnd.choice(cos) for _ in cos) for x in by[c]]
        v = [r[key] for r in s if r[key] is not None]
        if v: hs.append(sum(x > 0 for x in v) / len(v)); ms.append(st.median(v))
    hs.sort(); ms.sort()
    return (hs[int(.025 * len(hs))], hs[int(.975 * len(hs))]), (ms[int(.025 * len(ms))], ms[int(.975 * len(ms))])
def line(name, rs, key):
    v = [r[key] for r in rs if r[key] is not None]
    if not v: return f'{name:44s} N=0'
    k = sum(x > 0 for x in v); n = len(v); w = wilson(k, n)
    (bl, bh), (ml, mh) = boot([r for r in rs if r[key] is not None], key) if len(set(r['t'] for r in rs)) > 2 else ((0, 0), (0, 0))
    return f'{name:44s} N={n:3d} cos={len(set(r["t"] for r in rs)):2d} pos={k:3d}/{n:<3d} {k/n*100:3.0f}% wilson[{w[0]*100:3.0f},{w[1]*100:3.0f}] clusterboot[{bl*100:3.0f},{bh*100:3.0f}] med={st.median(v)*100:+4.0f} medCI[{ml*100:+4.0f},{mh*100:+4.0f}]'
def dedupe(rs, gap=180):
    """one event per company episode: drop any event within `gap` days after a kept event of the same company, across all specs"""
    out = []
    for r in sorted(rs, key=lambda r: (r['t'], r['d'])):
        if out and out[-1]['t'] == r['t'] and (r['d'] - out[-1]['d']).days < gap: continue
        out.append(r)
    return out
nk = lambda r: r['ry'] < 0 and r['nx'] is not None and r['nx'] < r['ry'] - 0.02
ngp = lambda r: r['ngy'] is not None and r['ngy'] > 0
ngm = lambda r: r['ngy'] is not None and r['ngy'] <= 0
def spec(rs, m, d): return [r for r in rs if r['mode'] == m and r['DD'] == d]
SPECS = [('drop', .6), ('drop', .75), ('q', .6), ('q', .75)]
sec = sys.argv[2] if len(sys.argv) > 2 else 'all'
U = {'orig45': [r for r in ev if r['t'] in ORIG], 'expanded': ev, 'expanded_consumer': [r for r in ev if r['t'] not in NONCONS], 'apparel_footwear_retail': [r for r in ev if r['t'] in APP or r['t'] in set("DKS ASO GCO CAL DBI BKE BURL ROST TJX PLCE CATO TLYS FIGS RVLV WEYS ASNA TLRD DXLG DLTH LAKE LE VNCE JILL KTB".split())]}
if sec in ('all', 'repro'):
    print('== A. Reproduce Round 3 (orig 45, per spec, 6m vs S&P) ==')
    for m, d in SPECS:
        rs = [r for r in spec(U['orig45'], m, d) if nk(r)]
        print(m, d, 'nikepath', len(rs), 'GM+ next', sum(r['x6_^GSPC'] > 0 for r in rs if ngp(r)), '/', sum(1 for r in rs if ngp(r)), ' GM- next', sum(r['x6_^GSPC'] > 0 for r in rs if ngm(r)), '/', sum(1 for r in rs if ngm(r)))
if sec in ('all', 'main'):
    for uname, rs0 in U.items():
        print(f'\n== B. {uname}: Nike path, deduped across all 4 specs (one event per company per 180 days) ==')
        base = dedupe([r for r in rs0 if nk(r)])
        for key in ['x6_^GSPC', 'x12_^GSPC', 'x6_XRT', 'x12_XRT', 'x6_XLY', 'x12_XLY']:
            print(' ', key)
            print('   ' + line('Nike path, all', base, key))
            print('   ' + line('  next-Q GM up (realized, look-ahead)', [r for r in base if ngp(r)], key))
            print('   ' + line('  next-Q GM down (realized, look-ahead)', [r for r in base if ngm(r)], key))
            print('   ' + line('  current GM up (known at event)', [r for r in base if r['gy'] > 0], key))
            print('   ' + line('  current GM down (known at event)', [r for r in base if r['gy'] <= 0], key))
            print('   ' + line('  next GM up >= +50bp', [r for r in base if r['ngy'] is not None and r['ngy'] >= 50], key))
            print('   ' + line('  next GM up 0..+50bp', [r for r in base if r['ngy'] is not None and 0 < r['ngy'] < 50], key))
            print('   ' + line('  next GM up & next OM down (Nike guide)', [r for r in base if ngp(r) and r['noy'] is not None and r['noy'] <= 0], key))
            print('   ' + line('  next GM up & next OM up', [r for r in base if ngp(r) and r['noy'] is not None and r['noy'] > 0], key))
