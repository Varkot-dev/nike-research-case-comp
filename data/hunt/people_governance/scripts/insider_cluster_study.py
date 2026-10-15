"""Event study: insider purchase clusters in apparel/footwear/retail peers, 2006-2026.
Cluster = at least 2 distinct non-10%-owner insiders with open-market purchases (code P) within 60 days,
total >= $250k. Event date = filing date of the purchase that completes the cluster. Forward excess return
vs SPY over 126 and 252 trading days (adj_close from data/hunt/risk_short_interest/prices_all.csv, 2017+).
Usage: python3 -I insider_cluster_study.py OUTDIR PRICES_CSV"""
import sys, os, csv, collections, datetime as dt, bisect, statistics as st
OUT, PR = sys.argv[1:3]
P = collections.defaultdict(list)
for r in csv.DictReader(open(PR)):
    if r['adj_close']: P[r['ticker']].append((r['date'], float(r['adj_close'])))
for t in P: P[t].sort()
def ret(t, d0, h):
    s = P.get(t); 
    if not s: return None
    ds = [x[0] for x in s]; i = bisect.bisect_left(ds, d0)
    if i == 0 or i + h >= len(s): return None
    return s[i + h][1] / s[i][1] - 1
def past(t, d0, h=252):
    s = P.get(t) or []; ds = [x[0] for x in s]; i = bisect.bisect_left(ds, d0)
    return s[i][1] / s[i - h][1] - 1 if s and i - h >= 0 and i < len(s) else None
B = collections.defaultdict(list)
for r in csv.DictReader(open(os.path.join(OUT, 'insider_open_market_peers_2006_2026.csv'))):
    if r['ticker'] == 'GPS': r['ticker'] = 'GAP'
    if r['ticker'] == 'UA': r['ticker'] = 'UAA'
    if r['code'] == 'P' and r['ten_pct_owner'] == 'False' and float(r['value_usd']) > 0: B[r['ticker']].append(r)
ev = []
for t, L in B.items():
    L.sort(key=lambda r: r['trans_date']); last = '0000'
    for i, r in enumerate(L):
        d0 = dt.date.fromisoformat(r['trans_date'])
        win = [x for x in L[:i + 1] if (d0 - dt.date.fromisoformat(x['trans_date'])).days <= 60]
        own = set(x['owner'] for x in win); usd = sum(float(x['value_usd']) for x in win)
        if len(own) >= 2 and usd >= 250000 and r['filing_date'] > last:
            fd = r['filing_date']
            e = dict(ticker=t, event_date=fd, insiders=len(own), usd=round(usd), names='; '.join(sorted(own))[:150])
            for h in (126, 252):
                a, m = ret(t, fd, h), ret('SPY', fd, h)
                e[f'xs_{h}d'] = round((a - m) * 100, 1) if a is not None and m is not None else ''
            pp = past(t, fd); e['prior_252d_ret'] = round(pp * 100, 1) if pp is not None else ''
            ev.append(e); last = str(dt.date.fromisoformat(fd) + dt.timedelta(180))  # one event per 6 months per ticker
w = csv.DictWriter(open(os.path.join(OUT, 'insider_cluster_events.csv'), 'w', newline=''), fieldnames=list(ev[0])); w.writeheader(); w.writerows(sorted(ev, key=lambda e: e['event_date']))
def summ(sel, lab):
    for h in (126, 252):
        v = [e[f'xs_{h}d'] for e in sel if e[f'xs_{h}d'] != '']
        if v: print(f'{lab:44s} {h}d n={len(v):3d} median {st.median(v):6.1f}% mean {st.mean(v):6.1f}% win(>0) {sum(x > 0 for x in v)}/{len(v)}')
summ(ev, 'all clusters (priced tickers, 2017+)')
summ([e for e in ev if e['prior_252d_ret'] != '' and e['prior_252d_ret'] < -25], 'clusters after >25% fall')
summ([e for e in ev if e['insiders'] >= 3], 'clusters with 3+ insiders')
print([ (e['event_date'], e['insiders'], e['usd'], e['xs_126d'], e['xs_252d']) for e in ev if e['ticker'] == 'NKE'])
