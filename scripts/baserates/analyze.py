"""Build the core sample, classify outcomes, compute forward-return statistics and feature splits.
Usage: python3 -I analyze.py OUTDIR   (reads OUTDIR/episodes_features.csv, optional OUTDIR/../manual_features.csv)"""
import sys, os, csv, statistics, datetime

OUT = sys.argv[1]
MAN = sys.argv[2] if len(sys.argv) > 2 else None
rows = list(csv.DictReader(open(os.path.join(OUT, "episodes_features.csv"))))
man = {}
if MAN and os.path.exists(MAN):
    for m in csv.DictReader(open(MAN)):
        man[(m["ticker"], m["peak_date"])] = m

EXCLUDE = {"PARA": "Yahoo ticker PARA now maps to Banzai International (reassigned symbol); not Paramount",
           "GE": "non-consumer; Yahoo history affected by 2023-2024 spin-offs; control only"}
FOREIGN = {"ADS.DE", "PUM.DE", "KER.PA", "BRBY.L", "BOSS.DE", "GIL", "7936.T", "BUD", "NOK", "SONY"}

def f(x):
    try: return float(x)
    except Exception: return None

def q(v, p):
    v = sorted(v); n = len(v)
    if n == 0: return None
    k = (n - 1) * p; lo = int(k); hi = min(lo + 1, n - 1)
    return v[lo] + (v[hi] - v[lo]) * (k - lo)

core = []
for r in rows:
    r["exclusion"] = ""
    if r["ticker"] in EXCLUDE: r["exclusion"] = EXCLUDE[r["ticker"]]
    elif r["sector"] == "control": r["exclusion"] = "non-consumer control"
    pm = f(r["peak_mcap_usd_bn"])
    r["size_basis"] = "computed" if pm is not None else ("not computed (non-SEC filer)" if r["ticker"] in FOREIGN else "not computed")
    if not r["exclusion"]:
        if pm is not None and pm < 3: r["exclusion"] = "peak market cap below $3bn (approx)"
        elif pm is None and r["ticker"] not in FOREIGN: r["exclusion"] = "size unknown"
    if not r["exclusion"] and not r["e75_date"]: r["exclusion"] = "max drawdown 70-75%: never reached 75% entry"
    # outcome from E75
    mx = f(r["e75_max5y_vs_peak"]); f3 = f(r["e75_fwd3y"])
    comp = r["e75_5y_window_complete"] == "True"
    if r["e75_date"]:
        if mx is not None and mx >= 0.75: oc = "recovered"
        elif f3 is not None and f3 <= 0: oc = "value_trap"
        elif f3 is None: oc = "too_recent"
        else: oc = "partial" if comp else "partial_window_open"
    else: oc = ""
    r["outcome_e75"] = oc
    dd = f(r["spx_dd_at_e75"])
    r["regime"] = "" if dd is None else ("market_wide" if dd <= -0.15 else "idiosyncratic")
    # dividends
    pmx, now, later = f(r["div_ttm_peak_max"]), f(r["div_ttm_at_e75"]), f(r["div_ttm_1y_after_e75"])
    if pmx and pmx > 0:
        r["div_payer"] = "yes"
        r["div_cut_by_entry"] = "yes" if now is not None and now < 0.75 * pmx else "no"
        r["div_cut_within_1y_after"] = "" if later is None else ("yes" if later < 0.75 * pmx else "no")
    else:
        r["div_payer"] = "no"; r["div_cut_by_entry"] = "n/a"; r["div_cut_within_1y_after"] = "n/a"
    m = man.get((r["ticker"], r["peak_date"]))
    for k in ("ceo_change_pre", "founder_control", "activist", "manual_source"):
        r[k] = m.get(k, "") if m else ""
    if not r["exclusion"]: core.append(r)

keys = list(rows[0].keys())
with open(os.path.join(OUT, "episodes_all.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, keys); w.writeheader(); w.writerows(rows)
core_nn = [r for r in core if r["ticker"] != "NKE"]
with open(os.path.join(OUT, "episodes_core.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, keys); w.writeheader(); w.writerows(core)

def stats(sub, col):
    v = [f(r[col]) for r in sub if f(r[col]) is not None]
    if not v: return {"n": 0}
    return {"n": len(v), "median": statistics.median(v), "p25": q(v, .25), "p75": q(v, .75),
            "mean": statistics.mean(v), "hit_pos": sum(x > 0 for x in v) / len(v),
            "gt50": sum(x > 0.5 for x in v) / len(v), "lt_m25": sum(x < -0.25 for x in v) / len(v)}

lines = []
def emit(s): lines.append(s); print(s)
def fmt(st):
    if st["n"] == 0: return "n=0"
    return "n=%d median %+.0f%% IQR %+.0f%% to %+.0f%% mean %+.0f%% hit>0 %.0f%% >+50%% %.0f%% <-25%% %.0f%%" % (
        st["n"], 100 * st["median"], 100 * st["p25"], 100 * st["p75"], 100 * st["mean"], 100 * st["hit_pos"], 100 * st["gt50"], 100 * st["lt_m25"])

stat_rows = []
groups = {"all_core": core_nn,
          "idiosyncratic": [r for r in core_nn if r["regime"] == "idiosyncratic"],
          "market_wide": [r for r in core_nn if r["regime"] == "market_wide"],
          "us_sec_filers": [r for r in core_nn if r["ticker"] not in FOREIGN],
          "peak_mcap_ge_10bn": [r for r in core_nn if (f(r["peak_mcap_usd_bn"]) or 0) >= 10],
          "ex_2000_tech": [r for r in core_nn if not (r["sector"] in ("consumer_tech", "retail") and "1999" <= r["peak_date"][:4] <= "2000")],
          "post_2009_entries": [r for r in core_nn if r["e75_date"] >= "2009-07-01"],
          "idio_post_2009": [r for r in core_nn if r["regime"] == "idiosyncratic" and r["e75_date"] >= "2009-07-01"]}
for g, sub in groups.items():
    for ent in ("e75", "e80", "trough"):
        for y in (1, 2, 3):
            for kind in ("fwd", "xs"):
                col = f"{ent}_{kind}{y}y"
                st = stats([r for r in sub if r.get(f"{ent}_date")], col)
                st.update({"group": g, "entry": ent, "horizon_y": y, "measure": "absolute_TR" if kind == "fwd" else "excess_vs_SP500TR"})
                stat_rows.append(st)
                if g in ("all_core", "idiosyncratic", "market_wide", "idio_post_2009") or (ent == "e75" and kind == "fwd"):
                    emit(f"{g:18s} {ent:6s} {y}y {kind:3s} " + fmt(st))
with open(os.path.join(OUT, "forward_return_stats.csv"), "w", newline="") as fh:
    ks = ["group", "entry", "horizon_y", "measure", "n", "median", "p25", "p75", "mean", "hit_pos", "gt50", "lt_m25"]
    w = csv.DictWriter(fh, ks); w.writeheader()
    for s in stat_rows: w.writerow({k: (round(s[k], 4) if isinstance(s.get(k), float) else s.get(k, "")) for k in ks})

# outcome counts
emit("")
for g in ("all_core", "idiosyncratic", "market_wide"):
    sub = groups[g]
    c = {}
    for r in sub: c[r["outcome_e75"]] = c.get(r["outcome_e75"], 0) + 1
    emit(f"outcomes {g}: {c}")

# feature splits (E75 entry)
def split(sub, name, fn):
    out = []
    buckets = {}
    for r in sub:
        k = fn(r)
        if k is None: continue
        buckets.setdefault(k, []).append(r)
    for k, b in sorted(buckets.items()):
        dec = [r for r in b if r["outcome_e75"] in ("recovered", "partial", "value_trap")]
        rec = sum(r["outcome_e75"] == "recovered" for r in dec); trap = sum(r["outcome_e75"] == "value_trap" for r in dec)
        s3 = stats(b, "e75_fwd3y"); s1 = stats(b, "e75_fwd1y"); x3 = stats(b, "e75_xs3y")
        out.append({"feature": name, "bucket": k, "n": len(b), "n_decided": len(dec), "recovered": rec, "value_trap": trap,
                    "recovery_rate": round(rec / len(dec), 3) if dec else "", "trap_rate": round(trap / len(dec), 3) if dec else "",
                    "median_1y": round(s1["median"], 4) if s1["n"] else "", "n_3y": s3["n"],
                    "median_3y": round(s3["median"], 4) if s3["n"] else "", "median_xs_3y": round(x3["median"], 4) if x3["n"] else "",
                    "hit_3y": round(s3["hit_pos"], 3) if s3["n"] else "",
                    "tickers": " ".join(f'{r["ticker"]}:{r["peak_date"][:4]}:{r["outcome_e75"][:3]}' for r in b)})
    return out

def yn(col, thr=0.0):
    def g(r):
        v = f(r.get(col))
        return None if v is None else ("above_%g" % thr if v > thr else "at_or_below_%g" % thr)
    return g

FEATS = [("regime (S&P 500 drawdown at entry)", lambda r: r["regime"] or None),
         ("revenue growth latest FY", yn("e75_rev_growth")),
         ("revenue 3y CAGR", yn("e75_rev_3y_cagr")),
         ("gross margin change latest FY (bps)", yn("e75_gm_chg_bps")),
         ("operating margin latest FY", yn("e75_op_margin", 0.08)),
         ("operating margin change (bps)", yn("e75_op_margin_chg_bps")),
         ("net debt (positive = net debt)", yn("e75_net_debt")),
         ("net debt / revenue", yn_nd := (lambda r: None if f(r.get("e75_net_debt")) is None or not f(r.get("e75_rev")) else ("net_debt_gt_25pct_rev" if f(r["e75_net_debt"]) / f(r["e75_rev"]) > 0.25 else "net_debt_le_25pct_rev"))),
         ("free cash flow latest FY", yn("e75_fcf")),
         ("EV/sales at entry", yn("e75_ev_sales", 1.0)),
         ("EV/EBITDA at entry", lambda r: None if f(r.get("e75_ev_ebitda")) is None else ("le_8x" if f(r["e75_ev_ebitda"]) <= 8 else "gt_8x")),
         ("dividend payer at peak", lambda r: r["div_payer"]),
         ("dividend cut by entry (payers)", lambda r: None if r["div_cut_by_entry"] == "n/a" else r["div_cut_by_entry"]),
         ("dividend cut within 1y after entry (payers; not observable at entry)", lambda r: None if r["div_cut_within_1y_after"] in ("n/a", "") else r["div_cut_within_1y_after"]),
         ("time peak to E75 (years)", lambda r: None if not r["e75_date"] else ("le_2y" if (datetime.date.fromisoformat(r["e75_date"]) - datetime.date.fromisoformat(r["peak_date"])).days <= 730 else "gt_2y")),
         ("CEO change in 24m before entry [manual]", lambda r: r["ceo_change_pre"] or None),
         ("founder or family control [manual]", lambda r: r["founder_control"] or None),
         ("activist stake disclosed by entry +12m [manual]", lambda r: r["activist"] or None),
         ("sector", lambda r: r["sector"])]
frows = []
for gname in ("all_core", "idiosyncratic"):
    for name, fn in FEATS:
        for s in split(groups[gname], name, fn):
            s["group"] = gname; frows.append(s)
with open(os.path.join(OUT, "feature_splits.csv"), "w", newline="") as fh:
    ks = ["group", "feature", "bucket", "n", "n_decided", "recovered", "value_trap", "recovery_rate", "trap_rate", "median_1y", "n_3y", "median_3y", "median_xs_3y", "hit_3y", "tickers"]
    w = csv.DictWriter(fh, ks); w.writeheader(); w.writerows(frows)
emit("")
for s in frows:
    emit(f'{s["group"]:14s} {s["feature"][:45]:45s} {str(s["bucket"]):24s} n={s["n"]:3d} dec={s["n_decided"]:3d} rec={s["recovery_rate"]} trap={s["trap_rate"]} med1y={s["median_1y"]} med3y={s["median_3y"]} (n3={s["n_3y"]}) xs3y={s["median_xs_3y"]}')
open(os.path.join(OUT, "analysis_log.txt"), "w").write("\n".join(lines))
