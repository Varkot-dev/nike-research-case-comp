"""Does FINRA daily short SALE volume ratio (SVR) nowcast the change in twice-monthly short interest?
Combines raw/finra_short_volume_2019_2025.csv with data/hunt/risk_short_interest/daily_short_volume.csv
and the NKE short-interest history. For each SI period (settlement t-1 to t), SVR = sum short vol / sum total vol
over trading days in (t-1, t]. Regress pct change in SI on SVR. Then apply to 2026-10-01..10-13 (partial
period ending at the Oct 15 settlement). Usage: python3 -I short_volume_nowcast.py OUTDIR"""
import sys, os, csv, collections, statistics as st
OUT = sys.argv[1]; RS = os.path.join(OUT, '../risk_short_interest')
D = collections.defaultdict(dict)
for f in (os.path.join(OUT, 'raw/finra_short_volume_2019_2025.csv'), os.path.join(RS, 'daily_short_volume.csv')):
    for r in csv.DictReader(open(f)):
        d = r['date']; d = f'{d[:4]}-{d[4:6]}-{d[6:]}'
        D[r['symbol']][d] = (float(r['short_volume']), float(r['total_volume_finra_venues']))
w = csv.writer(open(os.path.join(OUT, 'finra_short_volume_daily_2019_2026.csv'), 'w', newline=''))
w.writerow(['date', 'symbol', 'short_volume', 'total_volume_finra_venues', 'short_volume_ratio'])
for s in sorted(D):
    for d in sorted(D[s]): sv, tv = D[s][d]; w.writerow([d, s, int(sv), int(tv), round(sv / tv, 4) if tv else ''])
SI = [(r['settlement_date'], float(r['short_shares'])) for r in csv.DictReader(open(os.path.join(RS, 'nke_short_interest_2017_2026.csv')))]
SI = [x for x in SI if x[0] >= '2019-01-01']
nk = D['NKE']; days = sorted(nk)
rows = []
for (d0, s0), (d1, s1) in zip(SI, SI[1:]):
    win = [d for d in days if d0 < d <= d1]
    if len(win) < 5: continue
    sv = sum(nk[d][0] for d in win); tv = sum(nk[d][1] for d in win)
    rows.append(dict(period_end=d1, si=s1, si_chg_pct=round((s1 / s0 - 1) * 100, 2), svr=round(sv / tv, 4), days=len(win)))
w = csv.DictWriter(open(os.path.join(OUT, 'nke_si_vs_short_volume_ratio.csv'), 'w', newline=''), fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
x = [r['svr'] for r in rows]; y = [r['si_chg_pct'] for r in rows]
mx, my = st.mean(x), st.mean(y)
b = sum((a - mx) * (c - my) for a, c in zip(x, y)) / sum((a - mx) ** 2 for a in x); a0 = my - b * mx
corr = st.correlation(x, y)
print(f'n={len(rows)} corr(SVR, SI%chg)={corr:.2f} slope={b:.1f} per 1.0 SVR, intercept={a0:.1f}')
for lo, hi in ((0, .40), (.40, .45), (.45, .50), (.50, .55), (.55, 1)):
    s = [r['si_chg_pct'] for r in rows if lo <= r['svr'] < hi]
    if s: print(f'  SVR {lo:.2f}-{hi:.2f}: n={len(s):3d} median SI chg {st.median(s):5.1f}% share rising {sum(v > 0 for v in s) / len(s):.2f}')
recent = [r for r in rows if r['period_end'] >= '2026-01-01']
print('2026 periods:', [(r['period_end'], r['svr'], r['si_chg_pct']) for r in recent])
win = [d for d in days if '2026-09-30' < d <= '2026-10-15']
sv = sum(nk[d][0] for d in win); tv = sum(nk[d][1] for d in win)
print(f'Oct 1-13 2026 partial: days={len(win)} SVR={sv / tv:.4f} -> fitted SI chg {a0 + b * sv / tv:.1f}%')
pct = sum(v <= sv / tv for v in x) / len(x)
print(f'percentile of Oct SVR among {len(x)} periods since 2019: {pct:.2f}')
# peers' SVR same window vs their 2025-26 average, as a control for market-wide shorting
for s in ('DECK', 'LULU', 'ONON', 'UAA', 'CROX', 'SPY'):
    if s not in D: continue
    a = [D[s][d] for d in D[s] if '2026-10-01' <= d <= '2026-10-13']; b2 = [D[s][d] for d in D[s] if '2026-01-01' <= d <= '2026-09-30']
    if a and b2: print(f'  {s}: Oct1-13 SVR {sum(v[0] for v in a) / sum(v[1] for v in a):.3f} vs 2026 Jan-Sep {sum(v[0] for v in b2) / sum(v[1] for v in b2):.3f}')
