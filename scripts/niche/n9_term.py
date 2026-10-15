"""N9 step 2: ATM IV term structure, forward variances, event-window implied moves, skew, OI tables.
Run: python3 -I n9_term.py <scratch_dir> <out_dir>"""
import sys, datetime as dt
import numpy as np, pandas as pd
from math import sqrt, exp, log
from scipy.stats import norm

SCR, OUT = sys.argv[1], sys.argv[2]
R = 0.0405; VAL = dt.date(2026, 10, 14); S0 = 35.30
df = pd.read_pickle(f'{SCR}/chain.pkl')
HOL = {dt.date(2026, 11, 26), dt.date(2026, 12, 25), dt.date(2027, 1, 1), dt.date(2027, 1, 18), dt.date(2027, 2, 15), dt.date(2027, 3, 26)}


def tdays(a, b):  # trading days in (a, b]
    n = 0; d = a
    while d < b:
        d += dt.timedelta(days=1)
        if d.weekday() < 5 and d not in HOL: n += 1
    return n


def otm_iv_curve(g, F):
    pts = []
    for r in g.itertuples():
        if np.isnan(r.iv_b76): continue
        if (r.cp == 'P' and r.strike <= F) or (r.cp == 'C' and r.strike >= F):
            sp = (r.ask - r.bid) if (r.ask == r.ask and r.bid == r.bid) else 9
            if sp > max(0.20, 0.25 * r.mid): continue
            pts.append((r.strike, r.iv_b76, r.cp))
    pts.sort()
    return pts


def atm_iv(g, F):
    pts = otm_iv_curve(g, F)
    ks = np.array([p[0] for p in pts]); vs = np.array([p[1] for p in pts])
    return float(np.interp(F, ks, vs)) if len(ks) >= 2 else np.nan


def iv_at(g, F, K):
    pts = otm_iv_curve(g, F)
    ks = np.array([p[0] for p in pts]); vs = np.array([p[1] for p in pts])
    if len(ks) < 2 or K < ks.min() or K > ks.max(): return np.nan
    return float(np.interp(K, ks, vs))


exps = sorted(df.expiry.unique())
rows = []
for e in exps:
    g = df[df.expiry == e]; F = g.F.iloc[0]; T = (e - VAL).days / 365
    a = atm_iv(g, F)
    # straddle at nearest strike to F (mids)
    ks = sorted(set(g.strike), key=lambda k: abs(k - F))
    st = np.nan; k0 = np.nan
    for k in ks:
        c = g[(g.strike == k) & (g.cp == 'C')].mid; p = g[(g.strike == k) & (g.cp == 'P')].mid
        if len(c) and len(p) and not np.isnan(c.iloc[0]) and not np.isnan(p.iloc[0]):
            st = c.iloc[0] + p.iloc[0]; k0 = k; break
    # skew: IV at 90% and 110% of forward and 25-delta style (K = F*exp(-+0.674*s*sqrtT))
    s = a
    kp = F * exp(-0.674 * s * sqrt(T)); kc = F * exp(0.674 * s * sqrt(T))
    ivp = iv_at(g, F, kp); ivc = iv_at(g, F, kc)
    ivp90 = iv_at(g, F, 0.9 * F); ivc110 = iv_at(g, F, 1.1 * F)
    ivp80 = iv_at(g, F, 0.8 * F)
    gp = g[g.cp == 'P']; gc = g[g.cp == 'C']
    rows.append(dict(expiry=e, dte=(e - VAL).days, tdays=tdays(VAL, e), F=F, atm_iv=a, W=a * a * T, strad_k=k0, straddle=st,
                     straddle_pct_spot=st / S0 if st == st else np.nan, iv_25dP=ivp, iv_25dC=ivc, rr25=(ivp - ivc) if ivp == ivp and ivc == ivc else np.nan,
                     iv90P=ivp90, iv110C=ivc110, skew90_110=(ivp90 - ivc110) if ivp90 == ivp90 and ivc110 == ivc110 else np.nan, iv80P=ivp80,
                     oi_put=gp.oi.sum(), oi_call=gc.oi.sum(), pc_oi=gp.oi.sum() / gc.oi.sum(), vol_put=gp.volume.sum(), vol_call=gc.volume.sum(),
                     pc_vol=gp.volume.sum() / max(gc.volume.sum(), 1)))
ts = pd.DataFrame(rows)
ts.to_csv(f'{OUT}/N9_term_structure_2026-10-14.csv', index=False)
pd.set_option('display.width', 250); pd.set_option('display.max_columns', 40)
print(ts[['expiry', 'dte', 'tdays', 'F', 'atm_iv', 'straddle', 'straddle_pct_spot', 'iv_25dP', 'iv_25dC', 'rr25', 'iv90P', 'iv110C', 'skew90_110', 'pc_oi', 'pc_vol', 'oi_put', 'oi_call']].round(4).to_string())

# forward (interval) variances between listed expiries
ts['dW'] = ts.W.diff(); ts['ddays'] = ts.dte.diff(); ts['dtd'] = ts.tdays.diff()
ts['fwd_vol_cal'] = np.sqrt(ts.dW / (ts.ddays / 365))
ts['fwd_vol_per_tradingday_pct'] = 100 * np.sqrt(ts.dW / ts.dtd)  # std of one trading day move implied, % (variance spread evenly)
print(ts[['expiry', 'ddays', 'dtd', 'dW', 'fwd_vol_cal', 'fwd_vol_per_tradingday_pct']].round(4).to_string())
ts.to_csv(f'{OUT}/N9_term_structure_2026-10-14.csv', index=False)
