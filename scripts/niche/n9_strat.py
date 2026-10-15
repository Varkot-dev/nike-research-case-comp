"""N9 step 4: event-window implied moves, D7 mixture vs market, and expected value of put / put spread / put spread financed by a call.
Run: python3 -I n9_strat.py <scratch_dir> <out_dir>   (needs n9_chain.py and n9_term.py outputs)"""
import sys, datetime as dt, json
import numpy as np, pandas as pd
from math import sqrt, exp, log

SCR, OUT = sys.argv[1], sys.argv[2]
R = 0.0405; VAL = dt.date(2026, 10, 14); S0 = 35.30
rng = np.random.default_rng(20261015)
N = 400000
ts = pd.read_csv(f'{OUT}/N9_term_structure_2026-10-14.csv', parse_dates=['expiry']).set_index('expiry')
ch = pd.read_csv(f'{OUT}/N9_nke_chain_2026-10-14.csv', parse_dates=['expiry'])

# ---------- 1. event windows by variance differencing ----------
W = ts.W
wk = {  # forward variance of one calendar week (5 trading days) between consecutive weekly expiries
    'Oct23': W['2026-10-23'] - W['2026-10-16'] if False else ts.loc['2026-10-23', 'dW'],
    'Oct30': ts.loc['2026-10-30', 'dW'], 'Nov06_election': ts.loc['2026-11-06', 'dW'], 'Nov13': ts.loc['2026-11-13', 'dW'],
    'Nov20_event': ts.loc['2026-11-20', 'dW'], 'Nov27_4d': ts.loc['2026-11-27', 'dW']}
base_clean = np.mean([wk['Oct23'], wk['Oct30'], wk['Nov13']])           # three clean weeks
base_alts = {'clean_3wk_mean': base_clean, 'Nov06_wk(election)': wk['Nov06_election'], 'Nov27_wk_scaled_5d': wk['Nov27_4d'] * 5 / 4,
             'max_of_all': max(wk['Oct23'], wk['Oct30'], wk['Nov06_election'], wk['Nov13'], wk['Nov27_4d'] * 5 / 4)}
res = {'weekly_fwd_var': {k: float(v) for k, v in wk.items()}}
tot = wk['Nov20_event']
res['id_window'] = {'total_var': float(tot), 'total_sigma_pct': 100 * sqrt(tot)}
for k, b in base_alts.items():
    ev = tot - b
    res['id_window'][k] = dict(base_var=float(b), event_var=float(ev), event_sigma_pct=100 * sqrt(max(ev, 0)),
                              exp_abs_move_pct=100 * sqrt(max(ev, 0)) * sqrt(2 / np.pi))
res['id_window']['straddle_method'] = dict(nov20_straddle_pct=float(ts.loc['2026-11-20', 'straddle_pct_spot'] * 100),
                                           nov13_straddle_pct=float(ts.loc['2026-11-13', 'straddle_pct_spot'] * 100))
# Q2 window: Dec 18 expiry vs Nov 27 expiry (no weekly listed between them)
tdq = ts.loc['2026-12-18', 'tdays'] - ts.loc['2026-11-27', 'tdays']
dWq = ts.loc['2026-12-18', 'dW']
perday = {'clean_3wk_per_td': base_clean / 5, 'Nov27_wk_per_td': wk['Nov27_4d'] / 4, 'Nov06_per_td': wk['Nov06_election'] / 5}
res['q2_window'] = {'trading_days': int(tdq), 'total_var': float(dWq)}
for k, b in perday.items():
    ev = dWq - b * tdq
    res['q2_window'][k] = dict(event_var=float(ev), event_sigma_pct=100 * sqrt(max(ev, 0)), exp_abs_pct=100 * sqrt(max(ev, 0)) * sqrt(2 / np.pi))
# Jan 15 version in case the print is Jan or the Dec 18 does not capture it
tdj = ts.loc['2027-01-15', 'tdays'] - ts.loc['2026-11-27', 'tdays']
dWj = ts.loc['2027-01-15', 'W'] - ts.loc['2026-11-27', 'W']
res['q2_window']['jan15_vs_nov27'] = {k: dict(event_sigma_pct=100 * sqrt(max(dWj - b * tdj, 0))) for k, b in perday.items()}

# earnings history (repo)
hist = pd.read_csv('/home/user/nike-research-case-comp/data/flows/earnings_day_moves.csv').move_pct.values
res['earn_hist'] = dict(n=len(hist), mean=float(hist.mean()), mean_abs=float(np.abs(hist).mean()), median_abs=float(np.median(np.abs(hist))), std=float(hist.std(ddof=1)),
                        neg=int((hist < 0).sum()))

# ---------- 2. window-return distributions: market vs D7 vs D4 ----------
sig_base_win = sqrt(base_clean); sigE = sqrt(tot - base_clean)
sig_win = sqrt(tot)
def mkt_window(fat):
    z = rng.standard_normal(N)
    if fat:   # event leg Student t(4), variance matched
        t = rng.standard_t(4, N) / sqrt(2.0)
    else:
        t = rng.standard_normal(N)
    lr = sig_base_win * z + sigE * t
    lr = lr - np.log(np.mean(np.exp(lr)))      # martingale (risk neutral)
    return np.exp(lr) - 1
D7 = {'UP': (0.25, 7.9, 4.6, 3.9, 8.7), 'NEUTRAL': (13 / 28, -0.2, 2.9, -1.3, 9.5), 'DOWN': (8 / 28, -15.0, 6.7, -19.2, 12.9)}
D7['UP'] = (7 / 28,) + D7['UP'][1:]
D4P = {'UP': 0.08, 'NEUTRAL': 0.42, 'DOWN': 0.50}
MKT_NOISE_D3 = 0.02; MKT_NOISE_D20 = 0.045   # S&P 500 noise over 4 and 20 trading days, assumption (about 1%/day)

def scen_window(probs, down_mean=None, horizon=3):
    names = list(probs); p = np.array([probs[n] for n in names])
    idx = rng.choice(len(names), size=N, p=p / p.sum())
    r = np.zeros(N)
    for i, n in enumerate(names):
        m3, s3, m20, s20 = D7[n][1:]
        if horizon == 3:
            mean, sd, noise = m3, s3, MKT_NOISE_D3
            if n == 'DOWN' and down_mean is not None: mean = down_mean
        else:
            mean, sd, noise = m20, s20, MKT_NOISE_D20
            if n == 'DOWN' and down_mean is not None: mean = down_mean * (m20 / m3)
        k = idx == i
        a = rng.normal(mean, sd, k.sum()) / 100 + rng.normal(0, noise, k.sum())
        r[k] = a
    return r, idx

def tail_stats(r):
    return dict(P_gt6=float((r > 0.06).mean()), P_lt_m10=float((r < -0.10).mean()), P_lt_m15=float((r < -0.15).mean()),
                mean_pct=float(100 * r.mean()), sd_pct=float(100 * r.std()), P_abs_gt_10=float((np.abs(r) > 0.10).mean()))

D7P = {k: v[0] for k, v in D7.items()}
win = {'market_normal': tail_stats(mkt_window(False)), 'market_fat_event_t4': tail_stats(mkt_window(True)),
       'D7_base_rates': tail_stats(scen_window(D7P)[0]), 'D4_probs_D7_means': tail_stats(scen_window(D4P)[0]),
       'D4_probs_down_-8': tail_stats(scen_window(D4P, down_mean=-8.0)[0]),
       'neutral_only': tail_stats(scen_window({'NEUTRAL': 1.0})[0])}
res['window_prob'] = win

# ---------- 3. structures ----------
def q(expiry, strike, cp):
    r = ch[(ch.expiry == expiry) & (ch.strike == strike) & (ch.cp == cp)].iloc[0]
    return dict(bid=float(r.bid), ask=float(r.ask), mid=float((r.bid + r.ask) / 2), oi=float(r.oi), vol=float(r.volume))

STRUCT = {
    'A1 long 35P': [(+1, 35.0, 'P')],
    'A2 long 32.5P': [(+1, 32.5, 'P')],
    'B1 put spread 35/30': [(+1, 35.0, 'P'), (-1, 30.0, 'P')],
    'B2 put spread 32.5/27.5': [(+1, 32.5, 'P'), (-1, 27.5, 'P')],
    'C1 35/30 put spread, short 40C': [(+1, 35.0, 'P'), (-1, 30.0, 'P'), (-1, 40.0, 'C')],
    'C2 35/30 put spread, short 37.5C': [(+1, 35.0, 'P'), (-1, 30.0, 'P'), (-1, 37.5, 'C')],
}

def cost(legs, expiry, mode):
    c = 0.0
    for sgn, k, cp in legs:
        x = q(expiry, k, cp)
        px = x['mid'] if mode == 'mid' else (x['ask'] if sgn > 0 else x['bid'])
        c += sgn * px
    return c

def payoff(legs, S):
    p = np.zeros_like(S)
    for sgn, k, cp in legs:
        p += sgn * (np.maximum(k - S, 0) if cp == 'P' else np.maximum(S - k, 0))
    return p

def terminal(horizon, scenario_kind, q2mode=None, down_mean=None, probs=None):  # scenario_kind kept for clarity
    sig13 = sqrt(ts.loc['2026-11-13', 'W'])
    lr = rng.normal(0, sig13, N); lr = lr - np.log(np.mean(np.exp(lr)))
    S13 = S0 * 1.0025 * np.exp(lr)   # 1.0025 = Nov 13 forward / spot (parity)
    r, idx = scen_window(probs, down_mean=down_mean, horizon=3 if horizon == 'nov' else 20)
    S = S13 * np.exp(np.log1p(np.clip(r, -0.95, 5)))
    if horizon == 'dec':
        if q2mode == 'hist_raw':
            q2 = rng.choice(hist, N) / 100
        elif q2mode == 'implied_zero_mean':
            sg = res['q2_window']['clean_3wk_per_td']['event_sigma_pct'] / 100
            q2 = rng.normal(0, sg, N)
        S = S * (1 + q2)
    return S

DISTS = {
    'D7 base rates (25/46/29)': dict(probs=D7P),
    'D4 probs (8/42/50), D7 means': dict(probs=D4P),
    'D4 probs, DOWN mean -8% d3': dict(probs=D4P, down_mean=-8.0),
    'Neutral only (no news)': dict(probs={'NEUTRAL': 1.0}),
}
rows = []
for horizon, expiry, exp_s in (('nov', dt.datetime(2026, 11, 20), 'Nov 20'), ('dec', dt.datetime(2026, 12, 18), 'Dec 18')):
    T = (expiry.date() - VAL).days / 365; dfac = exp(-R * T)
    # density-implied fair values
    for dname, kw in DISTS.items():
        for q2mode in ([None] if horizon == 'nov' else ['hist_raw', 'implied_zero_mean']):
            S = terminal(horizon, 'scen', q2mode=q2mode, **kw)
            for sname, legs in STRUCT.items():
                pay = payoff(legs, S) * dfac
                for mode in ('natural', 'mid'):
                    c = cost(legs, pd.Timestamp(expiry), mode)
                    pnl = pay - c
                    up_legs = [l for l in legs if l[2] == 'C']
                    be = legs[0][1] - c   # long-put strike minus net debit (downside breakeven at expiry)
                    rows.append(dict(expiry=exp_s, dist=dname, q2=q2mode or '', structure=sname, price_mode=mode, cost_per_share=round(c, 3),
                                     cost_pct_spot=round(100 * c / S0, 2), ev_per_share=round(float(pnl.mean()), 3),
                                     ev_pct_of_debit=round(100 * float(pnl.mean()) / abs(c), 1) if abs(c) > 0.05 else np.nan,
                                     p_profit=round(float((pnl > 0).mean()), 3), p5_pnl=round(float(np.percentile(pnl, 5)), 2),
                                     p95_pnl=round(float(np.percentile(pnl, 95)), 2), breakeven_S=round(float(be), 2), be_pct=round(100 * (float(be) / S0 - 1), 1),
                                     max_gain=round(float(payoff(legs, np.array([0.0]))[0] - c), 2),
                                     loss_if_S_is_43_5=round(float(payoff(legs, np.array([43.5]))[0] - c), 2),
                                     pnl_if_S_is_38=round(float(payoff(legs, np.array([38.0]))[0] - c), 2), pnl_if_S_is_30=round(float(payoff(legs, np.array([30.0]))[0] - c), 2)))
out = pd.DataFrame(rows)
# sensitivity: EV of Nov 20 structures at natural prices vs p_DOWN and DOWN mean (p_UP fixed), D7 std per group
sens = []
for pu in (0.08, 0.25):
    for pd_ in (0.10, 0.20, 0.29, 0.40, 0.50, 0.60):
        for dm in (-15.0, -10.0, -5.0):
            pn = 1 - pu - pd_
            if pn < 0: continue
            S = terminal('nov', 'scen', probs={'UP': pu, 'NEUTRAL': pn, 'DOWN': pd_}, down_mean=dm)
            dfac = exp(-R * 37 / 365)
            for sname in ('A1 long 35P', 'B1 put spread 35/30', 'C1 35/30 put spread, short 40C'):
                legs = STRUCT[sname]; c = cost(legs, pd.Timestamp('2026-11-20'), 'natural')
                sens.append(dict(p_up=pu, p_down=pd_, down_mean_d3=dm, structure=sname, ev_per_share=round(float((payoff(legs, S) * dfac - c).mean()), 3)))
pd.DataFrame(sens).to_csv(f'{OUT}/N9_sensitivity_nov20.csv', index=False)
out.to_csv(f'{OUT}/N9_strategy_ev_2026-10-14.csv', index=False)
json.dump(res, open(f'{OUT}/N9_event_windows.json', 'w'), indent=1, default=float)
print(json.dumps(res, indent=1, default=float))
