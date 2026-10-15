"""N9 step 3: risk-neutral density (SVI smoothing + Breeden-Litzenberger) for chosen expiries and event-window probabilities.
Run: python3 -I n9_density.py <scratch_dir> <out_dir>"""
import sys, datetime as dt, json
import numpy as np, pandas as pd
from math import sqrt, exp, log
from scipy.stats import norm
from scipy.optimize import least_squares

SCR, OUT = sys.argv[1], sys.argv[2]
R = 0.0405; VAL = dt.date(2026, 10, 14); S0 = 35.30
df = pd.read_pickle(f'{SCR}/chain.pkl')


def b76(F, K, T, sig, cp):
    sig = np.maximum(sig, 1e-4)
    d1 = (np.log(F / K) + 0.5 * sig ** 2 * T) / (sig * np.sqrt(T)); d2 = d1 - sig * np.sqrt(T); df_ = exp(-R * T)
    return df_ * (F * norm.cdf(d1) - K * norm.cdf(d2)) if cp == 'C' else df_ * (K * norm.cdf(-d2) - F * norm.cdf(-d1))


def svi_w(p, k):
    a, b, rho, m, s = p
    return a + b * (rho * (k - m) + np.sqrt((k - m) ** 2 + s ** 2))


def fit_svi(e, kmax=0.45):
    g = df[df.expiry == e]; F = g.F.iloc[0]; T = (e - VAL).days / 365
    pts = []
    for r in g.itertuples():
        if np.isnan(r.iv_b76): continue
        if not ((r.cp == 'P' and r.strike <= F) or (r.cp == 'C' and r.strike >= F)): continue
        sp = r.ask - r.bid
        if sp > max(0.20, 0.25 * r.mid): continue
        k = log(r.strike / F)
        if abs(k) > kmax: continue
        pts.append((k, r.iv_b76 ** 2 * T, 1.0 / max(sp, 0.02)))   # weight by 1 / quoted spread
    pts = np.array(pts)
    k, w, wt = pts[:, 0], pts[:, 1], pts[:, 2]
    wt = wt / wt.max()
    best = None
    for rho0 in (-0.5, 0.0, 0.5):
        x0 = [w.min() * 0.8, 0.1, rho0, 0.0, 0.1]
        res = least_squares(lambda p: (svi_w(p, k) - w) * wt ** 0.5 * 100, x0,
                            bounds=([-0.05, 1e-4, -0.99, -0.5, 0.01], [1.0, 5.0, 0.99, 0.5, 1.0]))
        if best is None or res.cost < best.cost: best = res
    return best.x, pts, F, T


def fit_quad(e, kmax=0.30):
    """Weighted quadratic smile in log-moneyness on IV; flat extrapolation outside the fitted range."""
    g = df[df.expiry == e]; F = g.F.iloc[0]; T = (e - VAL).days / 365
    pts = []
    for r in g.itertuples():
        if np.isnan(r.iv_b76): continue
        if not ((r.cp == 'P' and r.strike <= F) or (r.cp == 'C' and r.strike >= F)): continue
        sp = r.ask - r.bid
        if sp > max(0.20, 0.25 * r.mid): continue
        k = log(r.strike / F)
        if abs(k) > kmax: continue
        pts.append((k, r.iv_b76, 1.0 / max(sp, 0.02)))
    pts = np.array(pts)
    c = np.polyfit(pts[:, 0], pts[:, 1], 2, w=np.sqrt(pts[:, 2] / pts[:, 2].max()))
    return c, pts, F, T, (pts[:, 0].min(), pts[:, 0].max())


def density(e, method='svi'):
    if method == 'svi':
        p, pts, F, T = fit_svi(e)
    else:
        p, pts, F, T, (klo, khi) = fit_quad(e)
    K = np.linspace(0.5 * F, 2.5 * F, 4001)
    k = np.log(K / F)
    if method == 'svi':
        iv = np.sqrt(np.maximum(svi_w(p, k), 1e-8) / T)
    else:
        iv = np.polyval(p, np.clip(k, klo, khi))
    C = b76(F, K, T, iv, 'C')
    dK = K[1] - K[0]
    d2 = np.gradient(np.gradient(C, dK), dK) * exp(R * T)
    sl = -np.gradient(C, dK) * exp(R * T)          # P(S > K)
    return dict(p=p, pts=pts, F=F, T=T, K=K, iv=iv, pdf=d2, surv=sl, C=C)


def prob_above(D, x):   # P(S_T > x)
    return float(np.interp(x, D['K'], D['surv']))


def adj_threshold(D, x, shrink):
    """P(S_{T-1d} > x) under log-return scaling by `shrink` around F."""
    F = D['F']; y = F * (x / F) ** (1 / shrink)
    return prob_above(D, y)


if __name__ == '__main__':
    out = {}
    METHOD = sys.argv[3] if len(sys.argv) > 3 else 'svi'
    for e in (dt.date(2026, 11, 13), dt.date(2026, 11, 20), dt.date(2026, 12, 18)):
        D = density(e, METHOD)
        p = D['p']
        area = np.trapezoid(D['pdf'], D['K'])
        neg = float((D['pdf'] < -1e-6).sum())
        mean = np.trapezoid(D['K'] * D['pdf'], D['K'])
        ts = pd.read_csv(f'{OUT}/N9_term_structure_2026-10-14.csv', parse_dates=['expiry'])
        W = float(ts[ts.expiry == pd.Timestamp(e)].W.iloc[0])
        # shrink for one fewer trading day (base daily variance 0.00042 from ordinary weeks)
        shrink = sqrt(max(1 - 0.00042 / W, 0.5)) if e == dt.date(2026, 11, 20) else 1.0
        r = dict(svi=[round(float(x), 5) for x in p], area=round(float(area), 4), mean_F=round(float(mean), 3), F=round(D['F'], 3),
                 neg_pdf_points=neg)
        for lab, ret in (('up6', 0.06), ('dn10', -0.10), ('dn15', -0.15), ('up10', 0.10), ('dn5', -0.05), ('dn20', -0.20), ('up15', 0.15)):
            x = S0 * (1 + ret)
            pr = prob_above(D, x) if ret > 0 else 1 - prob_above(D, x)
            r[lab + '_nov20exp' if e.month == 11 else lab] = round(float(pr), 4)
            if e == dt.date(2026, 11, 20):
                r[lab + '_adj_nov19'] = round(float(adj_threshold(D, x, shrink) if ret > 0 else 1 - adj_threshold(D, x, shrink)), 4)
        # model-free check from raw market prices: butterfly-free digital via call spread around x (strikes available)
        g = df[(df.expiry == e)]
        out[str(e)] = r
        print(e, r)
        # sanity: re-price market options with density (RN expectation of payoff)
        chk = []
        for row in g[g.strike.between(27, 45)].itertuples():
            if np.isnan(row.mid): continue
            pay = np.maximum(D['K'] - row.strike, 0) if row.cp == 'C' else np.maximum(row.strike - D['K'], 0)
            val = exp(-R * D['T']) * np.trapezoid(pay * D['pdf'], D['K'])
            chk.append(dict(expiry=str(e), cp=row.cp, strike=row.strike, mid=row.mid, svi_price=round(float(val), 3)))
        pd.DataFrame(chk).to_csv(f'{OUT}/N9_{METHOD}_repricing_{e}.csv', index=False)
        pd.DataFrame(dict(K=D['K'][::20], pdf=D['pdf'][::20], surv=D['surv'][::20])).to_csv(f'{OUT}/N9_rn_density_{METHOD}_{e}.csv', index=False)
    json.dump(out, open(f'{OUT}/N9_density_summary_{METHOD}.json', 'w'), indent=1)
