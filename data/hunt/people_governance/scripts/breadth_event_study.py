"""Ownership-breadth test (Chen, Hong and Stein 2002 style) on ~59 US consumer stocks, 2017-2026.
Breadth change = 13F filings holding the stock at quarter Q / filings at Q-4 - 1, minus the cross-sectional
median that quarter (removes growth in the number of 13F filers). Signal date = Q end + 46 days (after the
13F deadline). Forward excess return vs SPY over 63/126/252 trading days, from adj_close.
Usage: python3 -I breadth_event_study.py OUTDIR PRICES_CSV"""
import sys, os, csv, collections, statistics as st, datetime as dt, bisect
OUT, PR = sys.argv[1:3]
F = collections.defaultdict(dict)
for r in csv.DictReader(open(os.path.join(OUT, 'peer_13f_filings_by_quarter.csv'))):
    F[r['ticker']][r['quarter']] = int(r['filings'])
P = collections.defaultdict(list)
for r in csv.DictReader(open(PR)):
    if r['adj_close']: P[r['ticker']].append((r['date'], float(r['adj_close'])))
for t in P: P[t].sort()
def qend(q):
    y, n = int(q[:4]), int(q[5]); return dt.date(y, 3 * n, 31 if n in (1, 4) else 30)
def prevq(q, k=4): return f'{int(q[:4]) - 1}q{q[5]}' if k == 4 else None
def fwd(t, d0, h):
    s = P[t]; ds = [x[0] for x in s]; i = bisect.bisect_left(ds, d0)
    if i + h >= len(s): return None
    return s[i + h][1] / s[i][1] - 1
qs = sorted(set(q for t in F for q in F[t]))
rows = []
for q in qs:
    if q < '2017q1' or q > '2026q2': continue
    ch = {}
    for t in F:
        a, b = F[t].get(q), F[t].get(prevq(q))
        if a and b and b >= 100: ch[t] = a / b - 1
    if len(ch) < 20: continue
    med = st.median(ch.values())
    d0 = str(qend(q) + dt.timedelta(46))
    for t, c in ch.items():
        if t not in P: continue
        r = dict(ticker=t, quarter=q, signal_date=d0, breadth_yoy=round(c * 100, 1), rel_breadth=round((c - med) * 100, 1))
        for h in (63, 126, 252):
            x, m = fwd(t, d0, h), fwd('SPY', d0, h)
            r[f'xs_{h}d'] = round((x - m) * 100, 1) if x is not None and m is not None else ''
        rows.append(r)
w = csv.DictWriter(open(os.path.join(OUT, 'breadth_event_panel.csv'), 'w', newline=''), fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
nk = [r for r in rows if r['ticker'] == 'NKE' and r['quarter'] >= '2025q1']
print('NKE recent:', [(r['quarter'], r['breadth_yoy'], r['rel_breadth']) for r in nk])
def summ(sel, lab):
    for h in (63, 126, 252):
        v = [r[f'xs_{h}d'] for r in sel if r[f'xs_{h}d'] != '']
        if v: print(f'  {lab:38s} {h}d n={len(v):4d} median {st.median(v):6.1f}% mean {st.mean(v):6.1f}% share<0 {sum(x < 0 for x in v) / len(v):.2f}')
summ(rows, 'all')
summ([r for r in rows if r['rel_breadth'] <= -10], 'rel_breadth <= -10pp')
summ([r for r in rows if r['rel_breadth'] <= -14], 'rel_breadth <= -14pp')
summ([r for r in rows if r['rel_breadth'] >= 5], 'rel_breadth >= +5pp')
# also: after a drawdown (stock down >30% over prior 252d), so the comparison is like for like
def past(t, d0, h=252):
    s = P[t]; ds = [x[0] for x in s]; i = bisect.bisect_left(ds, d0)
    return s[i][1] / s[i - h][1] - 1 if i - h >= 0 and i < len(s) else None
dd = [r for r in rows if (past(r['ticker'], r['signal_date']) or 0) < -0.25]
summ([r for r in dd if r['rel_breadth'] <= -10], 'fell>25% & rel_breadth <= -10pp')
summ([r for r in dd if r['rel_breadth'] > -10], 'fell>25% & rel_breadth > -10pp')
# decile sort
v = sorted([r for r in rows if r['xs_126d'] != ''], key=lambda r: r['rel_breadth'])
n = len(v)
for k in range(5):
    sel = v[k * n // 5:(k + 1) * n // 5]
    print(f'  quintile {k + 1} rel_breadth {sel[0]["rel_breadth"]:6.1f}..{sel[-1]["rel_breadth"]:6.1f} 126d median {st.median([r["xs_126d"] for r in sel]):6.1f} mean {st.mean([r["xs_126d"] for r in sel]):6.1f} n={len(sel)}')
