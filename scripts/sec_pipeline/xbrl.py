import json, sys, datetime as dt
f = json.load(open(sys.argv[1]))["facts"]
def series(tag, ns="us-gaap", unit=None):
    t = f[ns].get(tag)
    if not t: return []
    u = unit or list(t["units"])[0]
    return [x for x in t["units"][u]]
def dur(x):
    if "start" not in x: return None
    return (dt.date.fromisoformat(x["end"]) - dt.date.fromisoformat(x["start"])).days
out = {}
def pick(tag, kind):
    res = {}
    for x in series(tag):
        d = dur(x)
        if kind == "FY" and d and 360 <= d <= 370: k = ("FY", x["end"])
        elif kind == "Q" and d and 85 <= d <= 95: k = ("Q", x["end"])
        elif kind == "I" and d is None: k = ("I", x["end"])
        else: continue
        # keep the value from the earliest filing (as originally reported), record later restatements
        res.setdefault(k, []).append((x["filed"], x["val"], x["form"], x["accn"]))
    return {k: sorted(v) for k, v in res.items()}
REV = ["RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet", "RevenueFromContractWithCustomerIncludingAssessedTax"]
tags = {"revenue": REV, "gross_profit": ["GrossProfit"], "net_income": ["NetIncomeLoss"], "eps_diluted": ["EarningsPerShareDiluted"],
        "diluted_shares": ["WeightedAverageNumberOfDilutedSharesOutstanding"], "sga": ["SellingGeneralAndAdministrativeExpense"],
        "dps_declared": ["CommonStockDividendsPerShareDeclared"], "cfo": ["NetCashProvidedByUsedInOperatingActivities"],
        "capex": ["PaymentsToAcquirePropertyPlantAndEquipment"], "buybacks": ["PaymentsForRepurchaseOfCommonStock"],
        "dividends_paid": ["PaymentsOfDividends", "PaymentsOfDividendsCommonStock"]}
itags = {"inventory": ["InventoryNet"], "cash": ["CashAndCashEquivalentsAtCarryingValue"], "st_inv": ["ShortTermInvestments"],
         "ltd_noncurrent": ["LongTermDebtNoncurrent"], "ltd_current": ["LongTermDebtCurrent"], "equity": ["StockholdersEquity"]}
rows = []
for name, tl in tags.items():
    for kind in ("FY", "Q"):
        merged = {}
        for t in tl:
            for k, v in pick(t, kind).items(): merged.setdefault(k, v)
        for (kk, end), v in merged.items():
            vals = sorted(set(x[1] for x in v))
            rows.append((name, kk, end, v[0][1], v[0][2], v[0][3], "RESTATED:" + str(vals) if len(vals) > 1 else ""))
for name, tl in itags.items():
    merged = {}
    for t in tl:
        for k, v in pick(t, "I").items(): merged.setdefault(k, v)
    for (kk, end), v in merged.items():
        vals = sorted(set(x[1] for x in v))
        rows.append((name, kk, end, v[0][1], v[0][2], v[0][3], "RESTATED:" + str(vals) if len(vals) > 1 else ""))
for x in series("EntityCommonStockSharesOutstanding", "dei", "shares"):
    rows.append(("shares_outstanding_cover", "I", x["end"], x["val"], x["form"], x["accn"], x.get("frame","") ))
rows = [r for r in rows if r[2] >= "2018-05-31"]
rows.sort(key=lambda r: (r[0], r[1], r[2]))
import csv
w = csv.writer(open(sys.argv[2], "w")); w.writerow(["metric", "kind", "period_end", "value_as_first_reported", "form", "accession", "note"]); w.writerows(rows)
print(len(rows))
