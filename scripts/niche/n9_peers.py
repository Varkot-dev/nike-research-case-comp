"""N9 step 5: skew for NKE and peers from the same CBOE delayed-quote source, same day, same method.
Run: python3 -I n9_peers.py <scratch_dir> <out_dir>"""
import sys, json, re, datetime as dt
import numpy as np, pandas as pd
from math import log, sqrt, exp
from scipy.stats import norm
from scipy.optimize import brentq

SCR, OUT = sys.argv[1], sys.argv[2]
R = 0.0405; VAL = dt.date(2026, 10, 14)


def b76(F, K, T, sig, cp):
    d1 = (log(F / K) + 0.5 * sig * sig * T) / (sig * sqrt(T)); d2 = d1 - sig * sqrt(T); df = exp(-R * T)
    return df * (F * norm.cdf(d1) - K * norm.cdf(d2)) if cp == 'C' else df * (K * norm.cdf(-d2) - F * norm.cdf(-d1))


def iv(price, F, K, T, cp):
    df = exp(-R * T)
    if price <= df * max((F - K) if cp == 'C' else (K - F), 0) + 1e-4: return np.nan
    try: return brentq(lambda s: b76(F, K, T, s, cp) - price, 0.01, 5)
    except Exception: return np.nan


def load(path):
    d = json.load(open(path)); spot = d['data']['current_price']; rows = []
    for o in d['data']['options']:
        m = re.match(r'([A-Z]+)(\d{6})([CP])(\d{8})', o['option'])
        rows.append(dict(expiry=dt.datetime.strptime(m.group(2), '%y%m%d').date(), cp=m.group(3), strike=int(m.group(4)) / 1000,
                         bid=o['bid'], ask=o['ask'], oi=o['open_interest'], volume=o['volume']))
    return pd.DataFrame(rows), spot, d['timestamp']


def analyse(sym, path, target_dte):
    df, spot, ts = load(path)
    exps = sorted(set(df.expiry)); e = min(exps, key=lambda x: abs((x - VAL).days - target_dte))
    g = df[df.expiry == e].copy(); T = (e - VAL).days / 365
    g['mid'] = np.where((g.bid > 0) & (g.ask > g.bid), (g.bid + g.ask) / 2, np.nan)
    cc = g[g.cp == 'C'].set_index('strike').mid; pp = g[g.cp == 'P'].set_index('strike').mid
    ks = sorted([k for k in cc.index.intersection(pp.index) if abs(k / spot - 1) < 0.1 and cc[k] == cc[k] and pp[k] == pp[k]], key=lambda k: abs(k - spot))[:6]
    if len(ks) < 2: return None
    F = float(np.median([k + exp(R * T) * (cc[k] - pp[k]) for k in ks]))
    pts = []
    for r in g.itertuples():
        if r.mid != r.mid: continue
        if not ((r.cp == 'P' and r.strike <= F) or (r.cp == 'C' and r.strike >= F)): continue
        if (r.ask - r.bid) > max(0.2, 0.25 * r.mid) * max(1, spot / 50): continue
        v = iv(r.mid, F, r.strike, T, r.cp)
        if v == v: pts.append((r.strike, v))
    pts.sort(); K = np.array([p[0] for p in pts]); V = np.array([p[1] for p in pts])
    f = lambda k: float(np.interp(k, K, V)) if K.min() <= k <= K.max() else np.nan
    a = f(F); s = a * sqrt(T)
    out = dict(sym=sym, expiry=str(e), dte=(e - VAL).days, spot=spot, F=round(F, 2), atm_iv=a,
               iv_p25=f(F * exp(-0.674 * s)), iv_c25=f(F * exp(0.674 * s)), iv_p90=f(0.9 * F), iv_c110=f(1.1 * F), iv_p80=f(0.8 * F), iv_c120=f(1.2 * F),
               pc_oi=g[g.cp == 'P'].oi.sum() / max(g[g.cp == 'C'].oi.sum(), 1), cboe_ts=ts)
    out['rr25'] = out['iv_p25'] - out['iv_c25']; out['skew90_110'] = out['iv_p90'] - out['iv_c110']; out['skew80_120'] = out['iv_p80'] - out['iv_c120']
    out['rr25_over_atm'] = out['rr25'] / a if a == a else np.nan
    return out


rows = []
for sym in ('NKE', 'LULU', 'DECK', 'ONON', 'UAA', 'VFC', 'CROX', 'SPY'):
    path = f'{SCR}/cboe.json' if sym == 'NKE' else f'{SCR}/peers/{sym}.json'
    for t in (37, 65):
        try:
            r = analyse(sym, path, t)
            if r: rows.append(r)
        except Exception as ex:
            print(sym, t, 'ERR', ex)
o = pd.DataFrame(rows)
o.to_csv(f'{OUT}/N9_peer_skew_2026-10-14.csv', index=False)
pd.set_option('display.width', 250)
print(o.drop(columns=['cboe_ts']).round(4).to_string())
