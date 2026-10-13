"""Point-in-time fundamentals from SEC companyfacts XBRL at an episode's entry date.
Usage: python3 -I features.py SECDIR PRICEDIR EPISODES_CSV OUT_CSV

Point-in-time rule: a fiscal period counts as known at date D if its period end
is at least 75 days (annual) / 45 days (quarter, balance sheet) before D.
Values for a period are taken from the EARLIEST filing that reports it (closest
to the original report; later comparatives used only when the original was
pre-XBRL). Debt excludes operating leases. All figures USD as filed."""
import sys, os, json, csv, datetime, bisect

SEC, PD, EPCSV, OUT = sys.argv[1:5]

REV = ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet",
       "SalesRevenueGoodsNet", "RevenueFromContractWithCustomerIncludingAssessedTax", "SalesRevenueServicesNet"]
COGS = ["CostOfGoodsAndServicesSold", "CostOfRevenue", "CostOfGoodsSold", "CostOfGoodsSoldExcludingDepreciationDepletionAndAmortization"]
DA = ["DepreciationDepletionAndAmortization", "DepreciationAndAmortization", "DepreciationAmortizationAndAccretionNet", "Depreciation"]
CFO = ["NetCashProvidedByUsedInOperatingActivities", "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"]
CAPEX = ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets"]

def d(s): return datetime.date.fromisoformat(s)

def series(facts, tags, kind):
    """kind 'FY' -> {end: (val, start)} annual durations; 'Q' -> instants; 'SH' -> diluted shares any duration."""
    out = {}
    for t in tags:
        f = facts.get("us-gaap", {}).get(t)
        if not f: continue
        for unit, arr in f["units"].items():
            if unit not in ("USD", "shares"): continue
            for x in sorted(arr, key=lambda z: z["filed"]):
                e = d(x["end"])
                if kind == "FY":
                    if "start" not in x: continue
                    dur = (e - d(x["start"])).days
                    if not 340 <= dur <= 380: continue
                elif kind == "I":
                    if "start" in x: continue
                elif kind == "SH":
                    if "start" not in x: continue
                if e not in out:
                    v = x["val"]
                    if kind == "SH" and 0 < v < 5e6: v = v * 1000  # share counts tagged in thousands
                    out[e] = v
        if kind != "I" and out:  # for flows, prefer first tag that has data, but fill gaps from later tags
            pass
    return out

def merged(facts, tags, kind):
    res = {}
    for t in tags:
        s = series(facts, [t], kind)
        for e, v in s.items():
            res.setdefault(e, v)
    return res

def shares_series(facts):
    """Annual diluted (else basic) weighted shares; per period the MEDIAN across filings
    (guards against filer unit errors such as NUS 2014-15 10-Qs tagged x1000)."""
    import statistics
    res = {}
    for t in ["WeightedAverageNumberOfDilutedSharesOutstanding", "WeightedAverageNumberOfSharesOutstandingBasic"]:
        f = facts.get("us-gaap", {}).get(t)
        if not f: continue
        per = {}
        for unit, arr in f["units"].items():
            for x in arr:
                if "start" not in x: continue
                dur = (d(x["end"]) - d(x["start"])).days
                if not (340 <= dur <= 380 or 80 <= dur <= 100): continue
                v = x["val"]
                if 0 < v < 5e6: v *= 1000
                per.setdefault(d(x["end"]), []).append(v)
        for e, vs in per.items():
            # unit errors show up as x1000 disagreements between filings: keep the plausible (smaller) cluster
            lo = min(vs)
            vs = [v for v in vs if v < lo * 100]
            res.setdefault(e, statistics.median(vs))
    return res

def latest_before(s, D, lag):
    ks = [e for e in s if e + datetime.timedelta(days=lag) <= D]
    if not ks: return None, None
    e = max(ks); return e, s[e]

def prior_year(s, e):
    c = [k for k in s if 330 <= (e - k).days <= 400]
    return s[min(c, key=lambda k: abs((e - k).days - 365))] if c else None

def load_px(t):
    r = json.load(open(os.path.join(PD, t.replace("^", "_") + ".json")))["chart"]["result"][0]
    ts = r["timestamp"]; c = r["indicators"]["quote"][0]["close"]
    rows = [(datetime.datetime.fromtimestamp(s + r["meta"].get("gmtoffset", 0), datetime.timezone.utc).date(), v) for s, v in zip(ts, c) if v]
    spl = [(datetime.datetime.fromtimestamp(int(k), datetime.timezone.utc).date(), v["numerator"] / v["denominator"])
           for k, v in r.get("events", {}).get("splits", {}).items()]
    return rows, spl

def actual_price(rows, spl, D):
    ds = [x[0] for x in rows]; i = bisect.bisect_right(ds, D) - 1
    f = 1.0
    for sd, ratio in spl:
        if sd > rows[i][0]: f *= ratio
    return rows[i][1] * f

def instant_sum(facts, D, combos):
    best = None
    sers = {t: merged(facts, [t], "I") for c in combos for t in c}
    for combo in combos:
        need = combo
        # all components at the same latest instant <= D-45
        ends = None
        for t in need[:1]:
            e, _ = latest_before(sers[t], D, 45)
            ends = e
        if ends is None: continue
        if (D - ends).days > 400: continue
        tot = 0; ok = True
        for k, t in enumerate(need):
            v = sers[t].get(ends)
            if v is None:
                if k == 0: ok = False; break
                v = 0
            tot += v
        if ok and (best is None or tot > best[1]): best = (ends, tot)
    return best

DEBT = [["LongTermDebtNoncurrent", "LongTermDebtCurrent", "ShortTermBorrowings", "CommercialPaper"],
        ["LongTermDebt", "ShortTermBorrowings", "CommercialPaper"],
        ["LongTermDebtNoncurrent", "DebtCurrent"],
        ["DebtLongtermAndShorttermCombinedAmount"],
        ["LongTermDebtAndCapitalLeaseObligations", "LongTermDebtAndCapitalLeaseObligationsCurrent", "ShortTermBorrowings"],
        ["LongTermDebtAndCapitalLeaseObligations", "DebtCurrent"],
        ["SeniorNotes", "ShortTermBorrowings"],
        ["ConvertibleNotesPayable"], ["ConvertibleDebtNoncurrent", "ConvertibleDebtCurrent"],
        ["LineOfCredit", "LongTermDebtNoncurrent"]]
CASH = [["CashAndCashEquivalentsAtCarryingValue", "ShortTermInvestments"],
        ["CashAndCashEquivalentsAtCarryingValue", "MarketableSecuritiesCurrent"],
        ["CashAndCashEquivalentsAtCarryingValue", "AvailableForSaleSecuritiesCurrent"],
        ["CashAndCashEquivalentsAtCarryingValue", "AvailableForSaleSecuritiesDebtSecuritiesCurrent"],
        ["CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents"],
        ["Cash"]]

def feats(tk, D):
    fn = os.path.join(SEC, f"{tk}.json")
    if not os.path.exists(fn) or not D: return {}
    facts = json.load(open(fn))["facts"]
    rev = merged(facts, REV, "FY")
    e, R = latest_before(rev, D, 75)
    o = {}
    if R is None: return {"fund_note": "no XBRL FY revenue known at date"}
    o["fy_end"] = e; o["rev"] = R
    R0 = prior_year(rev, e); o["rev_growth"] = R / R0 - 1 if R0 else None
    e3 = [k for k in rev if 1050 <= (e - k).days <= 1130]
    o["rev_3y_cagr"] = (R / rev[e3[0]]) ** (1 / 3) - 1 if e3 and rev[e3[0]] > 0 else None
    gp = merged(facts, ["GrossProfit"], "FY"); cg = merged(facts, COGS, "FY")
    def gm(end):
        rv = rev.get(end)
        if not rv: return None
        if end in gp: return gp[end] / rv
        if end in cg: return 1 - cg[end] / rv
        return None
    o["gm"] = gm(e)
    pe = [k for k in rev if 330 <= (e - k).days <= 400]
    g0 = gm(pe[0]) if pe else None
    o["gm_chg_bps"] = (o["gm"] - g0) * 1e4 if o["gm"] is not None and g0 is not None else None
    oi = merged(facts, ["OperatingIncomeLoss"], "FY")
    o["op_margin"] = oi[e] / R if e in oi else None
    o["op_margin_chg_bps"] = ((oi[e] / R) - oi[pe[0]] / rev[pe[0]]) * 1e4 if e in oi and pe and pe[0] in oi else None
    da = merged(facts, DA, "FY")
    o["ebitda"] = oi[e] + da[e] if e in oi and e in da else None
    cfo = merged(facts, CFO, "FY"); cx = merged(facts, CAPEX, "FY")
    o["fcf"] = cfo[e] - cx.get(e, 0) if e in cfo else None
    debt = instant_sum(facts, D, DEBT); cash = instant_sum(facts, D, CASH)
    o["bs_date"] = cash[0] if cash else None
    o["cash"] = cash[1] if cash else None
    o["debt"] = debt[1] if debt else (0 if cash else None)
    o["net_debt"] = o["debt"] - o["cash"] if o["cash"] is not None and o["debt"] is not None else None
    sh = shares_series(facts)
    es, S = latest_before(sh, D, 75)
    o["shares"] = S
    try:
        rows, spl = load_px(tk)
        P = actual_price(rows, spl, D); o["px_actual"] = P
        if S:
            mc = P * S; o["mcap"] = mc
            if o["net_debt"] is not None:
                ev = mc + o["net_debt"]; o["ev"] = ev
                o["ev_sales"] = ev / R
                o["ev_ebitda"] = ev / o["ebitda"] if o.get("ebitda") and o["ebitda"] > 0 else None
            o["fcf_yield"] = o["fcf"] / mc if o.get("fcf") is not None else None
    except Exception as ex:
        o["fund_note"] = f"price error {ex}"
    return o

def peak_mcap(tk, D):
    fn = os.path.join(SEC, f"{tk}.json")
    if not os.path.exists(fn): return None, "no SEC"
    facts = json.load(open(fn))["facts"]
    sh = shares_series(facts)
    if not sh: return None, "no shares"
    rows, spl = load_px(tk)
    e = min(sh, key=lambda k: abs((k - D).days))
    # convert share count at e into split-adjusted-today units, and price at D into same units
    f_after_e = 1.0
    for sd, ratio in spl:
        if sd > e: f_after_e *= ratio
    ds = [x[0] for x in rows]; i = bisect.bisect_right(ds, D) - 1
    mc = rows[i][1] * sh[e] * f_after_e
    gap = abs((e - D).days)
    return mc, ("xbrl shares %s" % e) + (" (approx, %d days from peak)" % gap if gap > 200 else "")

eps = list(csv.DictReader(open(EPCSV)))
out = []
for ep in eps:
    tk = ep["ticker"]
    row = dict(ep)
    pk = d(ep["peak_date"])
    mc, note = peak_mcap(tk, pk)
    row["peak_mcap_usd_bn"] = round(mc / 1e9, 2) if mc else ""
    row["peak_mcap_note"] = note
    for lab in ("e75", "trough"):
        D = d(ep[f"{lab}_date"]) if ep.get(f"{lab}_date") else None
        f = feats(tk, D) if D else {}
        for k, v in f.items():
            if isinstance(v, float): v = round(v, 4)
            row[f"{lab}_{k}"] = v
    out.append(row)
keys = []
for r in out:
    for k in r:
        if k not in keys: keys.append(k)
with open(OUT, "w", newline="") as fh:
    w = csv.DictWriter(fh, keys); w.writeheader(); w.writerows(out)
print("wrote", len(out))
