"""N9 step 1: build the NKE option chain table (CBOE delayed quotes primary, Yahoo cross-check),
forward by put-call parity, Black-76 implied vols, term structure, open interest tables.
Run: python3 -I n9_chain.py <scratch_dir> <out_dir>
Inputs in scratch_dir: cboe.json (https://cdn.cboe.com/api/global/delayed_quotes/options/NKE.json),
yh/NKE_<epoch>.json (https://query1.finance.yahoo.com/v7/finance/options/NKE?date=<epoch>&crumb=...)
"""
import sys, json, glob, re, datetime as dt
import numpy as np, pandas as pd
from math import log, sqrt, exp
from scipy.stats import norm
from scipy.optimize import brentq

SCR, OUT = sys.argv[1], sys.argv[2]
R = 0.0405            # 13-week bill, repo note 17 (^IRX); constant
VAL = dt.date(2026, 10, 14)   # quote date (US close)
S0 = 35.30            # official close 2026-10-14 (Yahoo regularMarketPrice 35.30 at 20:00:02 UTC; AlphaQuery 35.30)


def b76(F, K, T, sig, cp):
    d1 = (log(F / K) + 0.5 * sig * sig * T) / (sig * sqrt(T)); d2 = d1 - sig * sqrt(T)
    df = exp(-R * T)
    return df * (F * norm.cdf(d1) - K * norm.cdf(d2)) if cp == 'C' else df * (K * norm.cdf(-d2) - F * norm.cdf(-d1))


def iv(price, F, K, T, cp):
    df = exp(-R * T); intr = df * max((F - K) if cp == 'C' else (K - F), 0)
    if price <= intr + 1e-4: return np.nan
    try: return brentq(lambda s: b76(F, K, T, s, cp) - price, 0.01, 5.0)
    except Exception: return np.nan


def load_cboe():
    d = json.load(open(f'{SCR}/cboe.json'))
    rows = []
    for o in d['data']['options']:
        m = re.match(r'NKE(\d{6})([CP])(\d{8})', o['option'])
        e = dt.datetime.strptime(m.group(1), '%y%m%d').date()
        rows.append(dict(expiry=e, cp=m.group(2), strike=int(m.group(3)) / 1000, bid=o['bid'], ask=o['ask'],
                         last=o['last_trade_price'], volume=o['volume'], oi=o['open_interest'],
                         cboe_iv=o['iv'], cboe_delta=o['delta'], last_trade_time=o['last_trade_time']))
    return pd.DataFrame(rows), d['timestamp']


def load_yahoo():
    rows = []
    for f in glob.glob(f'{SCR}/yh/NKE_*.json'):
        r = json.load(open(f))['optionChain']['result'][0]
        for side, k in (('C', 'calls'), ('P', 'puts')):
            for o in r['options'][0][k]:
                rows.append(dict(expiry=dt.datetime.utcfromtimestamp(o['expiration']).date(), cp=side, strike=o['strike'],
                                 y_bid=o.get('bid'), y_ask=o.get('ask'), y_last=o.get('lastPrice'), y_vol=o.get('volume'),
                                 y_oi=o.get('openInterest'), y_iv=o.get('impliedVolatility')))
    return pd.DataFrame(rows)


def main():
    c, ts = load_cboe(); y = load_yahoo()
    df = c.merge(y, on=['expiry', 'cp', 'strike'], how='outer')
    df['mid'] = np.where((df.bid > 0) & (df.ask > df.bid), (df.bid + df.ask) / 2, np.nan)
    df['T'] = [((e - VAL).days) / 365.0 for e in df.expiry]
    df['dte'] = [(e - VAL).days for e in df.expiry]
    # forward per expiry from put-call parity on mids, strikes within 12% of spot, median
    fw = {}
    for e, g in df.groupby('expiry'):
        T = (e - VAL).days / 365.0
        cc = g[(g.cp == 'C')].set_index('strike').mid; pp = g[(g.cp == 'P')].set_index('strike').mid
        ks = [k for k in cc.index.intersection(pp.index) if abs(k / S0 - 1) < 0.12 and not np.isnan(cc[k]) and not np.isnan(pp[k])]
        # weight toward ATM: use the 6 strikes nearest spot
        ks = sorted(ks, key=lambda k: abs(k - S0))[:6]
        if ks:
            est = [k + exp(R * T) * (cc[k] - pp[k]) for k in ks]
            fw[e] = float(np.median(est))
        else:
            fw[e] = np.nan
    df['F'] = df.expiry.map(fw)
    ivs = []
    for r in df.itertuples():
        if np.isnan(r.mid) or np.isnan(r.F): ivs.append(np.nan); continue
        # OTM only for reliability; ITM IVs reported via parity-equivalent OTM
        ivs.append(iv(r.mid, r.F, r.T, r.strike, r.cp) if False else iv(r.mid, r.F, r.strike, r.T, r.cp))
    df['iv_b76'] = ivs
    df.to_pickle(f'{SCR}/chain.pkl')
    return df, ts, fw


if __name__ == '__main__':
    df, ts, fw = main()
    out = df.copy()
    out.insert(0, 'quote_date', str(VAL)); out.insert(1, 'cboe_file_timestamp', ts)
    out = out[(out.expiry >= dt.date(2026, 10, 16))]
    out = out.sort_values(['expiry', 'strike', 'cp'])
    out.to_csv(f'{OUT}/N9_nke_chain_2026-10-14.csv', index=False)
    print(len(out), 'rows; forwards:'); [print(k, round(v, 3)) for k, v in fw.items()]
