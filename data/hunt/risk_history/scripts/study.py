"""Re-run and stress-test the 'falling revenue but rising gross margin' event study.
Usage: python3 -I study.py PANEL.csv PXDIR1,PXDIR2 OUTDIR
Writes OUTDIR/events_all.csv (every event in every spec with outcomes vs S&P 500, XRT, XLY)."""
import sys, csv, json, bisect, datetime as dt, os, collections
PANEL, PXD, OUT = sys.argv[1], sys.argv[2].split(','), sys.argv[3]
D = dt.date.fromisoformat
APP = "NKE UAA VFC LULU PVH CROX DECK CPRI TPR RL COLM WWW FOSL LEVI CRI GIII OXM VRA SHOO HBI SKX GAP KSS M URBN ANF AEO ZUMZ BBWI BOOT FL GES CHS EXPR".split()
OTH = "SBUX EL PTON PYPL NWL MAT HAS CMG TGT INTC KHC".split()
NEW = "DKS ASO GCO CAL DBI BKE BURL ROST TJX PLCE CATO TLYS FIGS YETI RVLV SFIX WEYS ASNA TLRD DXLG DLTH LAKE LE VNCE JILL KTB ELF COTY".split()
# excluded: SMRT CBK BBBY (Yahoo ticker now a different company); HIBB JWN JCP FRAN PIR SSI DLA VSCO (no Yahoo history)
_px = {}
def S(t):
    if t not in _px:
        p = next((f'{d}/{t}.json' for d in PXD if os.path.exists(f'{d}/{t}.json')), None)
        j = json.load(open(p))['chart']['result'][0]
        q = j['indicators']['quote'][0]['close']; a = j['indicators']['adjclose'][0]['adjclose']
        _px[t] = [(dt.datetime.utcfromtimestamp(ts).date(), c, ac) for ts, c, ac in zip(j['timestamp'], q, a) if c and ac]
    return _px[t]
def at(t, d):
    s = S(t); i = bisect.bisect_left([x[0] for x in s], d)
    return s[i] if i < len(s) else None
def fwd(t, d, m):
    p0 = at(t, d)
    if not p0: return None
    d1 = p0[0] + dt.timedelta(days=int(m * 30.44))
    if d1 > S(t)[-1][0]: return None
    return at(t, d1)[2] / p0[2] - 1
panel = collections.defaultdict(list)
for r in csv.DictReader(open(PANEL)):
    f = lambda k: float(r[k]) if r[k] != '' else None
    panel[r['ticker']].append(dict(end=D(r['qend']), filed=D(r['filed']), rev=float(r['revenue_usd']), ry=f('rev_yoy'), gm=f('gross_margin'), gy=f('gm_yoy_bp'), oy=f('om_yoy_bp')))
def state(t, d):
    rows = panel[t]
    ok = [r for r in rows if r['end'] + dt.timedelta(days=20) <= d and r['filed'] <= d + dt.timedelta(days=30)]
    if len(ok) < 2: return None
    r = ok[-1]; p = ok[-2]
    later = [x for x in rows if x['end'] > r['end'] and x['ry'] is not None]
    if r['ry'] is None or r['gy'] is None or (d - r['end']).days > 150: return None
    n1 = later[0] if later else {}; n2 = later[1] if len(later) > 1 else {}
    return dict(qend=r['end'], ry=r['ry'], gy=r['gy'], oy=r['oy'], ryp=p['ry'], gyp=p['gy'],
                nx=n1.get('ry'), ngy=n1.get('gy'), noy=n1.get('oy'), nqend=n1.get('end'), ngy2=n2.get('gy'), nx2=n2.get('ry'))
def events(T, mode, DD):
    out = []
    for t in T:
        try: s = S(t)
        except Exception: continue
        ds = [x[0] for x in s]; cl = [x[1] for x in s]; ac = [x[2] for x in s]; last = None
        for i in range(1, len(s)):
            d = ds[i]
            if d < dt.date(2010, 6, 1) or d.year == 2020 or d < ds[0] + dt.timedelta(days=5 * 365): continue
            if mode == 'drop':
                if last and (d - last).days < 90: continue
                if ac[i] / ac[i - 1] - 1 > -0.08: continue
            else:
                if ds[i - 1].month == d.month: continue
                if last and (d - last).days < 84: continue
            j = bisect.bisect_left(ds, d - dt.timedelta(days=5 * 365)); dd = cl[i] / max(cl[j:i + 1]) - 1
            if dd > -DD: continue
            k = bisect.bisect_left(ds, d - dt.timedelta(days=365)); it = fwd('^GSPC', ds[k], 12)
            if it is None or it < -0.05: continue
            r12 = fwd(t, d, 12)
            if r12 is None: continue
            st = state(t, d)
            if not st: continue
            e = dict(t=t, d=d, mode=mode, DD=DD, dd=dd, r6=fwd(t, d, 6), r12=r12)
            for b in ['^GSPC', 'XRT', 'XLY']:
                e['x6_' + b] = e['r6'] - fwd(b, d, 6); e['x12_' + b] = r12 - fwd(b, d, 12)
            w = [x for x in s if d <= x[0] <= d + dt.timedelta(days=365)]
            e['min12'] = min(x[2] for x in w) / ac[i] - 1
            e.update(st); out.append(e); last = d
    return out
if __name__ == '__main__':
    ev = []
    for mode in ['drop', 'q']:
        for DD in [0.6, 0.75]:
            ev += events(APP + OTH + NEW, mode, DD)
    keys = list(ev[0].keys())
    with open(f'{OUT}/events_all.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, keys); w.writeheader()
        for e in ev: w.writerow({k: (round(v, 4) if isinstance(v, float) else v) for k, v in e.items()})
    print('events', len(ev))
