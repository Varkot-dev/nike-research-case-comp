"""Rule-based episode finder.
Usage: python3 -I find_episodes.py PRICEDIR OUTDIR

Rule (applied to every ticker in universe.py, outcome-blind):
  * Drawdown measured on Yahoo 'close' (split-adjusted, not dividend-adjusted),
    the same basis as "NKE is 80% below its $177.51 record close".
  * Running all-time-high peak; an episode exists when close falls >= 70% below
    the running peak. Trough = lowest close after the peak and before the stock
    regains the peak (or before the end of data). Next episode can start only
    after a new all-time high.
  * Peak must be on/after 1990-01-01 (data before 1990 used only to set the
    running high; an older pre-1990 peak can still be the reference high).
  * Entry points: first close at >= 75% and >= 80% drawdown (E75, E80); also trough.
  * Forward returns use Yahoo 'adjclose' (dividends reinvested) at +252, +504,
    +756 trading days (1, 2, 3 years) and versus the S&P 500 total return index
    (^SP500TR, from 1988), same calendar dates (nearest prior index date).
  * Outcome: max close in 5 calendar years after E75 (or trough) vs peak close.
Data through 2026-10-12 (the NKE reference close date)."""
import sys, os, json, csv, datetime, bisect
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from universe import UNIVERSE

PD, OUT = sys.argv[1], sys.argv[2]
END = datetime.date(2026, 10, 12)

def load(t):
    fn = os.path.join(PD, t.replace("^", "_") + ".json")
    if not os.path.exists(fn): return None
    try: r = json.load(open(fn))["chart"]["result"][0]
    except Exception: return None
    ts = r["timestamp"]; q = r["indicators"]["quote"][0]
    adj = r["indicators"].get("adjclose", [{}])[0].get("adjclose") or q["close"]
    rows = []
    for i, s in enumerate(ts):
        d = datetime.datetime.fromtimestamp(s + r["meta"].get("gmtoffset", 0), datetime.timezone.utc).date()
        c, a = q["close"][i], adj[i]
        if c is None or a is None or c <= 0 or d > END: continue
        rows.append((d, c, a))
    divs = r.get("events", {}).get("dividends", {})
    dv = sorted((datetime.datetime.fromtimestamp(int(k), datetime.timezone.utc).date(), v["amount"]) for k, v in divs.items())
    return rows, dv, r["meta"].get("currency")

bench, _, _ = load("^SP500TR")
bd = [b[0] for b in bench]
def bval(d):
    i = bisect.bisect_right(bd, d) - 1
    return bench[i][2] if i >= 0 else None
gspc, _, _ = load("^GSPC")
gd = [g[0] for g in gspc]
def spx_drawdown(d):
    i = bisect.bisect_right(gd, d) - 1
    pk = max(g[1] for g in gspc[:i + 1])
    return gspc[i][1] / pk - 1

def fwd(rows, i, n):
    if i is None or i + n >= len(rows): return None, None
    r = rows[i + n][2] / rows[i][2] - 1
    b0, b1 = bval(rows[i][0]), bval(rows[i + n][0])
    return r, (r - (b1 / b0 - 1)) if b0 and b1 else None

eps = []
for tk, name, sector, cik in UNIVERSE:
    L = load(tk)
    if not L: print("missing", tk); continue
    rows, divs, ccy = L
    n = len(rows); i = 0; pk_i = 0
    while i < n:
        if rows[i][1] >= rows[pk_i][1]: pk_i = i
        if rows[i][1] <= 0.30 * rows[pk_i][1] and rows[pk_i][0] >= datetime.date(1990, 1, 1):
            # episode: find end = first j>i with close >= peak
            j = i
            while j < n and rows[j][1] < rows[pk_i][1]: j += 1
            seg = range(pk_i, j)
            tr_i = min(seg, key=lambda k: rows[k][1])
            e70 = i
            e75 = next((k for k in seg if rows[k][1] <= 0.25 * rows[pk_i][1]), None)
            e80 = next((k for k in seg if rows[k][1] <= 0.20 * rows[pk_i][1]), None)
            pk = rows[pk_i][1]
            def outcome(k):
                if k is None: return None, None
                d0 = rows[k][0]; lim = d0 + datetime.timedelta(days=int(5 * 365.25))
                window = [r for r in rows[k:] if r[0] <= lim]
                mx = max(r[1] for r in window)
                complete = lim <= END
                return mx / pk, complete
            rec = {"ticker": tk, "name": name, "sector": sector, "cik": cik, "ccy": ccy,
                   "peak_date": rows[pk_i][0], "peak_close": round(pk, 4),
                   "trough_date": rows[tr_i][0], "trough_close": round(rows[tr_i][1], 4),
                   "max_drawdown": round(rows[tr_i][1] / pk - 1, 4),
                   "days_peak_to_trough": (rows[tr_i][0] - rows[pk_i][0]).days,
                   "recovered_peak_date": rows[j][0] if j < n else "",
                   "e70_date": rows[e70][0],
                   "e75_date": rows[e75][0] if e75 is not None else "",
                   "e80_date": rows[e80][0] if e80 is not None else "",
                   "spx_dd_at_e75": round(spx_drawdown(rows[e75][0]), 4) if e75 is not None else "",
                   "spx_dd_at_trough": round(spx_drawdown(rows[tr_i][0]), 4)}
            for lab, k in (("trough", tr_i), ("e75", e75), ("e80", e80)):
                for y, nd in ((1, 252), (2, 504), (3, 756)):
                    r, x = fwd(rows, k, nd)
                    rec[f"{lab}_fwd{y}y"] = "" if r is None else round(r, 4)
                    rec[f"{lab}_xs{y}y"] = "" if x is None else round(x, 4)
                o, c = outcome(k)
                rec[f"{lab}_max5y_vs_peak"] = "" if o is None else round(o, 4)
                rec[f"{lab}_5y_window_complete"] = c
            # dividend cut test: trailing-12m dividends at E75 vs max TTM in the 3 years before
            def ttm(d):
                return sum(a for dd, a in divs if d - datetime.timedelta(days=365) < dd <= d)
            k = e75 if e75 is not None else tr_i
            d0 = rows[k][0]
            prior = max([ttm(rows[pk_i][0] + datetime.timedelta(days=30 * m)) for m in range(0, 37)
                         if rows[pk_i][0] + datetime.timedelta(days=30 * m) <= d0] or [0])
            prior = max(prior, ttm(rows[pk_i][0]))
            now = ttm(d0)
            later = ttm(d0 + datetime.timedelta(days=365))
            rec["div_ttm_peak_max"] = round(prior, 4); rec["div_ttm_at_e75"] = round(now, 4)
            rec["div_ttm_1y_after_e75"] = round(later, 4) if d0 + datetime.timedelta(days=365) <= END else ""
            eps.append(rec)
            # continue after recovery
            if j >= n: break
            i = j; pk_i = j
        i += 1

keys = list(eps[0].keys())
with open(os.path.join(OUT, "episodes_raw.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, keys); w.writeheader(); w.writerows(eps)
print(len(eps), "episodes")
for e in eps:
    print(e["ticker"], e["peak_date"], e["trough_date"], e["max_drawdown"], e["e75_date"], e["e75_fwd1y"], e["e75_fwd3y"], e["e75_max5y_vs_peak"])
