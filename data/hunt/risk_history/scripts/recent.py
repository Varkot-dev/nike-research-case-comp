"""Recent Nike-path setups (2024-07 onward) scored at 6 months only, since 12-month outcomes are not yet known.
Usage: python3 -I recent.py PANEL.csv PXDIR1,PXDIR2 OUTDIR (same args as study.py)"""
import sys, os, datetime as dt, bisect
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import study
from study import S, fwd, state, APP, OTH, NEW
for t in APP + NEW + ['EL', 'HAS', 'MAT', 'NWL']:
    try: s = S(t)
    except Exception: continue
    ds = [x[0] for x in s]; cl = [x[1] for x in s]; last = None
    for i in range(1, len(s)):
        d = ds[i]
        if d < dt.date(2024, 7, 1) or ds[i - 1].month == d.month or (last and (d - last).days < 84): continue
        j = bisect.bisect_left(ds, d - dt.timedelta(days=5 * 365)); dd = cl[i] / max(cl[j:i + 1]) - 1
        if dd > -0.6: continue
        st = state(t, d)
        if not st or not (st['ry'] < 0 and st['nx'] is not None and st['nx'] < st['ry'] - 0.02): continue
        r6 = fwd(t, d, 6); i6 = fwd('^GSPC', d, 6)
        x6 = None if r6 is None or i6 is None else r6 - i6
        print(f"{t:5s} {d} dd {dd*100:+.0f} rev {st['ry']*100:+.1f} next {st['nx']*100:+.1f} GMnow {st['gy']:+.0f} GMnext {st['ngy'] if st['ngy'] is None else round(st['ngy'])} x6 {'na' if x6 is None else round(x6*100)}")
        last = d
