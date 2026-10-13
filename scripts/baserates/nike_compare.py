"""Place Nike in the base-rate framework: valuation percentiles, conditional subsets,
Fisher exact tests on key splits, survivorship sensitivity.
Usage: python3 -I nike_compare.py OUTDIR"""
import sys, os, csv, statistics, math

OUT = sys.argv[1]
core = [r for r in csv.DictReader(open(os.path.join(OUT, "episodes_core.csv"))) if r["ticker"] != "NKE"]
def f(x):
    try: return float(x)
    except Exception: return None
def q(v, p):
    v = sorted(v); n = len(v); k = (n - 1) * p; lo = int(k); hi = min(lo + 1, n - 1)
    return v[lo] + (v[hi] - v[lo]) * (k - lo)
def summ(v):
    v = [x for x in v if x is not None]
    if not v: return "n=0"
    return "n=%d median %+.0f%% p25 %+.0f%% p75 %+.0f%% hit>0 %.0f%%" % (len(v), 100*statistics.median(v), 100*q(v,.25), 100*q(v,.75), 100*sum(x>0 for x in v)/len(v))

def fisher(a, b, c, d):
    """two-sided Fisher exact p for [[a,b],[c,d]]"""
    n = a+b+c+d; r1 = a+b; c1 = a+c
    def p(x): return math.comb(r1, x) * math.comb(n-r1, c1-x) / math.comb(n, c1)
    p0 = p(a); lo = max(0, c1-(n-r1)); hi = min(r1, c1)
    return sum(p(x) for x in range(lo, hi+1) if p(x) <= p0 + 1e-12)

L = []
def emit(s): L.append(s); print(s)

# Nike today (inputs: repo note consensus_and_valuation.md for multiples; XBRL FY2026 for fundamentals)
NIKE = {"regime": "idiosyncratic (S&P 500 within 1% of its high on 2026-10-02, market data)",
        "ev_sales": 1.13, "ev_ebitda": 11.2, "rev_growth_fy26": 0.0019, "gm_chg_fy26_bps": 17.9,
        "net_debt_bn_may26": 0.379, "fcf_fy26_bn": 2.184, "div_cut": "no", "ceo_change": "yes", "founder": "yes",
        "years_peak_to_e75": 4.4}
emit("NIKE inputs: " + str(NIKE))

ev = [f(r["e75_ev_sales"]) for r in core if f(r["e75_ev_sales"]) is not None]
eb = [f(r["e75_ev_ebitda"]) for r in core if f(r["e75_ev_ebitda"]) is not None and f(r["e75_ev_ebitda"]) < 200]
emit("EV/sales at E75 across core sample: n=%d p25 %.2f median %.2f p75 %.2f; share below Nike 1.13x: %.0f%%" % (len(ev), q(ev,.25), statistics.median(ev), q(ev,.75), 100*sum(x < 1.13 for x in ev)/len(ev)))
emit("EV/EBITDA at E75 across core sample: n=%d p25 %.1f median %.1f p75 %.1f; share below Nike 11.2x: %.0f%%" % (len(eb), q(eb,.25), statistics.median(eb), q(eb,.75), 100*sum(x < 11.2 for x in eb)/len(eb)))

def decided(sub): return [r for r in sub if r["outcome_e75"] in ("recovered", "partial", "value_trap")]
def test(name, sub, fn):
    d = decided(sub)
    A = [r for r in d if fn(r) is True]; B = [r for r in d if fn(r) is False]
    a = sum(r["outcome_e75"] == "recovered" for r in A); b = len(A) - a
    c = sum(r["outcome_e75"] == "recovered" for r in B); dd = len(B) - c
    p = fisher(a, b, c, dd) if A and B else float("nan")
    emit("%-60s TRUE rec %d/%d (%.0f%%) | FALSE rec %d/%d (%.0f%%) | Fisher p=%.3f | 3y TRUE %s | 3y FALSE %s" % (
        name, a, len(A), 100*a/len(A) if A else 0, c, len(B), 100*c/len(B) if B else 0, p,
        summ([f(r["e75_fwd3y"]) for r in A]), summ([f(r["e75_fwd3y"]) for r in B])))
    return a, len(A), c, len(B), p

idio = [r for r in core if r["regime"] == "idiosyncratic"]
emit("\n== recovery-rate tests (E75 entry; decided episodes only) ==")
tests = [
    ("market-wide regime (S&P 500 down >=15% at entry)", core, lambda r: r["regime"] == "market_wide"),
    ("EV/sales <= 1.0x [all]", core, lambda r: None if f(r["e75_ev_sales"]) is None else f(r["e75_ev_sales"]) <= 1.0),
    ("EV/sales <= 1.0x [idiosyncratic]", idio, lambda r: None if f(r["e75_ev_sales"]) is None else f(r["e75_ev_sales"]) <= 1.0),
    ("EV/EBITDA <= 8x [all]", core, lambda r: None if f(r["e75_ev_ebitda"]) is None else f(r["e75_ev_ebitda"]) <= 8),
    ("EV/EBITDA <= 8x [idiosyncratic]", idio, lambda r: None if f(r["e75_ev_ebitda"]) is None else f(r["e75_ev_ebitda"]) <= 8),
    ("revenue growth > 0 [all]", core, lambda r: None if f(r["e75_rev_growth"]) is None else f(r["e75_rev_growth"]) > 0),
    ("gross margin up y/y [all]", core, lambda r: None if f(r["e75_gm_chg_bps"]) is None else f(r["e75_gm_chg_bps"]) > 0),
    ("net cash [all]", core, lambda r: None if f(r["e75_net_debt"]) is None else f(r["e75_net_debt"]) <= 0),
    ("net cash [idiosyncratic]", idio, lambda r: None if f(r["e75_net_debt"]) is None else f(r["e75_net_debt"]) <= 0),
    ("positive FCF [all]", core, lambda r: None if f(r["e75_fcf"]) is None else f(r["e75_fcf"]) > 0),
    ("dividend cut by entry (payers) [all]", core, lambda r: None if r["div_cut_by_entry"] == "n/a" else r["div_cut_by_entry"] == "yes"),
    ("peak to E75 within 2 years [all]", core, lambda r: (__import__("datetime").date.fromisoformat(r["e75_date"]) - __import__("datetime").date.fromisoformat(r["peak_date"])).days <= 730),
    ("peak to E75 within 2 years [idiosyncratic]", idio, lambda r: (__import__("datetime").date.fromisoformat(r["e75_date"]) - __import__("datetime").date.fromisoformat(r["peak_date"])).days <= 730),
    ("CEO change in 24m before entry [manual, idiosyncratic]", idio, lambda r: None if r["ceo_change_pre"] not in ("yes", "no") else r["ceo_change_pre"] == "yes"),
    ("founder/family/sponsor control [manual, idiosyncratic]", idio, lambda r: None if r["founder_control"] not in ("yes", "no") else r["founder_control"] == "yes"),
    ("activist by entry+12m [manual, idiosyncratic]", idio, lambda r: None if r["activist"] not in ("yes", "no") else r["activist"] == "yes"),
]
trow = []
for name, sub, fn in tests:
    a, na, c, nb, p = test(name, sub, fn)
    trow.append({"test": name, "true_recovered": a, "true_n": na, "false_recovered": c, "false_n": nb, "fisher_p": round(p, 4)})
with open(os.path.join(OUT, "feature_tests_fisher.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, list(trow[0].keys())); w.writeheader(); w.writerows(trow)

# Nike-like conditional subsets
emit("\n== Nike-like subsets: forward total return from E75 and E80 ==")
import datetime as dt
def yrs(r): return (dt.date.fromisoformat(r["e75_date"]) - dt.date.fromisoformat(r["peak_date"])).days / 365.25
subsets = {
    "S1 idiosyncratic": idio,
    "S2 idiosyncratic + EV/sales > 0.8x": [r for r in idio if (f(r["e75_ev_sales"]) or 0) > 0.8],
    "S3 idiosyncratic + EV/EBITDA > 8x": [r for r in idio if (f(r["e75_ev_ebitda"]) or 0) > 8],
    "S4 idiosyncratic + slow decline (>2y peak to E75)": [r for r in idio if yrs(r) > 2],
    "S5 idiosyncratic + no dividend cut by entry + positive FCF": [r for r in idio if r["div_cut_by_entry"] != "yes" and (f(r["e75_fcf"]) or -1) > 0],
    "S6 idiosyncratic + founder/family control": [r for r in idio if r["founder_control"] == "yes"],
    "S7 apparel/footwear/luxury, any regime": [r for r in core if r["sector"] == "apparel_footwear"],
    "S8 apparel/footwear/luxury, idiosyncratic": [r for r in core if r["sector"] == "apparel_footwear" and r["regime"] == "idiosyncratic"],
}
srows = []
for nm, sub in subsets.items():
    for ent in ("e75", "e80"):
        for y in (1, 2, 3):
            v = [f(r[f"{ent}_fwd{y}y"]) for r in sub if f(r[f"{ent}_fwd{y}y"]) is not None]
            x = [f(r[f"{ent}_xs{y}y"]) for r in sub if f(r[f"{ent}_xs{y}y"]) is not None]
            emit(f"{nm:58s} {ent} {y}y abs {summ(v)} | xs {summ(x)}")
            srows.append({"subset": nm, "entry": ent, "horizon_y": y, "n": len(v),
                          "median": round(statistics.median(v), 4) if v else "", "p25": round(q(v, .25), 4) if v else "",
                          "p75": round(q(v, .75), 4) if v else "", "hit_pos": round(sum(z > 0 for z in v) / len(v), 3) if v else "",
                          "xs_median": round(statistics.median(x), 4) if x else "", "xs_hit_pos": round(sum(z > 0 for z in x) / len(x), 3) if x else ""})
    emit("   members: " + ", ".join(f'{r["ticker"]} {r["peak_date"][:4]} ({r["outcome_e75"]})' for r in sub))
with open(os.path.join(OUT, "nike_like_subsets.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, list(srows[0].keys())); w.writeheader(); w.writerows(srows)

# Survivorship sensitivity: add K synthetic failures at -90% to the idiosyncratic 3y E75 distribution
emit("\n== survivorship sensitivity (idiosyncratic, E75, 3y absolute) ==")
base = [f(r["e75_fwd3y"]) for r in idio if f(r["e75_fwd3y"]) is not None]
for K in (0, 5, 10, 15):
    v = base + [-0.9] * K
    emit("add %2d failures at -90%%: %s" % (K, summ(v)))
open(os.path.join(OUT, "nike_compare_log.txt"), "w").write("\n".join(L))
