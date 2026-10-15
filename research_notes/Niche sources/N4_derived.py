"""N4 derived tests from data/niche/N4_subsidiary_accounts.csv -> data/niche/N4_derived_tests.csv (all DERIVED).
APLA reported revenue and currency-neutral growth come from data/nike_filing_facts.csv / 10-K and Q4 releases (typed below).
KRW per USD = simple mean of daily Yahoo Finance KRW=X closes over 1 Jun to 31 May (market data, approximate)."""
import csv
r = list(csv.DictReader(open("data/niche/N4_subsidiary_accounts.csv")))
def S(ent, m):
    out = {}
    for x in r:
        if x["entity"] == ent and x["metric"] == m:
            try: out[x["fiscal_year"]] = float(x["value"])
            except ValueError: pass
    return out
K = "Nike Korea LLC"
rev, cogs, gp, op, sga, inv, ar, rp, ra, pur, tp, ngt = [S(K, m) for m in ("revenue", "cogs", "gross_profit", "operating_profit", "sga", "inventory", "receivables", "returns_provision", "returns_asset", "goods_purchases", "transfer_price_adjustment_in_cogs", "goods_purchases_from_NGT_Singapore")]
pay = S(K, "trade_payables")
fx = {"FY21": 1141.6, "FY22": 1188.6, "FY23": 1320.7, "FY24": 1325.5, "FY25": 1400.2, "FY26": 1434.9}
apla = {"FY21": 5343, "FY22": 5955, "FY23": 6431, "FY24": 6729, "FY25": 6251, "FY26": 6243}
cn = {"FY21": 8, "FY22": 16, "FY23": 17, "FY24": 5, "FY25": -3, "FY26": -1}
fy20_rev = 1293.559
out = []
def put(fy, metric, v, unit, note=""):
    out.append(dict(entity=K, fiscal_year=fy, metric=metric, value=round(v, 3), unit=unit, tag="DERIVED", note=note))
prev = None
for fy in ["FY21", "FY22", "FY23", "FY24", "FY25", "FY26"]:
    g = (rev[fy] / (rev[prev] if prev else fy20_rev) - 1) * 100
    usd = rev[fy] / fx[fy] * 1000
    put(fy, "revenue_growth_krw", g, "%", "KRW, so already currency neutral; FY20 revenue 1,293.559 from FY21 report comparative")
    put(fy, "apla_currency_neutral_growth", cn[fy], "%", "10-K / Q4 release, APLA segment")
    put(fy, "korea_minus_apla_cn_growth", g - cn[fy], "pts")
    put(fy, "revenue_usd_approx", usd, "USD m", "KRW revenue / FY mean KRW per USD (Yahoo KRW=X)")
    put(fy, "share_of_apla_revenue", usd / apla[fy] * 100, "%", "Korea assumed inside APLA")
    put(fy, "gross_margin_reported", gp[fy] / rev[fy] * 100, "%")
    put(fy, "gross_margin_ex_tp_adjustment", (gp[fy] + tp[fy]) / rev[fy] * 100, "%", "removes the transfer price adjustment line in cost of sales")
    put(fy, "operating_margin_reported", op[fy] / rev[fy] * 100, "%")
    put(fy, "operating_margin_ex_tp_adjustment", (op[fy] + tp[fy]) / rev[fy] * 100, "%")
    put(fy, "sga_pct_revenue", sga[fy] / rev[fy] * 100, "%")
    put(fy, "receivable_days", ar[fy] / rev[fy] * 365, "days", "year-end receivables / annual revenue x 365")
    put(fy, "inventory_days", inv[fy] / (cogs[fy] - tp[fy]) * 365, "days", "year-end inventory / cost of sales ex TP adjustment x 365")
    put(fy, "returns_provision_pct_revenue", rp[fy] / rev[fy] * 100, "%")
    put(fy, "returns_provision_less_recovery_asset", rp[fy] - ra[fy], "KRW bn", "provision minus gross returned-goods recovery asset")
    put(fy, "goods_purchases_pct_revenue", pur[fy] / rev[fy] * 100, "%")
    prev = fy
put("FY26", "operating_profit_change_vs_FY25", op["FY26"] - op["FY25"], "KRW bn")
put("FY26", "tp_adjustment_credit", -tp["FY26"], "KRW bn", "share of the operating profit change: %.0f%%" % (-tp["FY26"] / (op["FY26"] - op["FY25"]) * 100))
put("FY26", "ngt_purchases_growth", (ngt["FY26"] / ngt["FY25"] - 1) * 100, "%")
put("FY26", "goods_purchases_growth", (pur["FY26"] / pur["FY25"] - 1) * 100, "%")
put("FY26", "inventory_growth", (inv["FY26"] / inv["FY25"] - 1) * 100, "%")
put("FY26", "returns_provision_growth", (rp["FY26"] / rp["FY25"] - 1) * 100, "%")
put("FY26", "trade_payables_growth", (pay["FY26"] / pay["FY25"] - 1) * 100, "%")
for fy in ("FY23", "FY24", "FY25", "FY26"):
    put(fy, "apla_ex_korea_usd_approx", apla[fy] - rev[fy] / fx[fy] * 1000, "USD m")
N = "Nike Retail B.V. (EMEA)"
def T(m): return S(N, m)
nr, ni, nta, ng = T("revenue"), T("inventory"), T("trade_receivables"), T("trade_revenue")
prev = None
for fy in ("FY22", "FY23", "FY24", "FY25"):
    d = dict(entity=N, fiscal_year=fy, tag="DERIVED", note="")
    out.append({**d, "metric": "trade_receivable_days", "value": round(nta[fy] / ng[fy] * 365, 3), "unit": "days"})
    out.append({**d, "metric": "gross_margin", "value": round(T("gross_profit")[fy] / nr[fy] * 100, 3), "unit": "%"})
    out.append({**d, "metric": "operating_margin", "value": round(T("operating_profit")[fy] / nr[fy] * 100, 3), "unit": "%"})
    if prev:
        out.append({**d, "metric": "revenue_growth_eur", "value": round((nr[fy] / nr[prev] - 1) * 100, 3), "unit": "%"})
        out.append({**d, "metric": "inventory_growth", "value": round((ni[fy] / ni[prev] - 1) * 100, 3), "unit": "%"})
        out.append({**d, "metric": "trade_receivable_growth", "value": round((nta[fy] / nta[prev] - 1) * 100, 3), "unit": "%"})
        out.append({**d, "metric": "rest_of_emea_revenue_growth", "value": round((T("rev_rest_emea")[fy] / T("rev_rest_emea")[prev] - 1) * 100, 3), "unit": "%"})
    prev = fy
with open("data/niche/N4_derived_tests.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["entity", "fiscal_year", "metric", "value", "unit", "tag", "note"])
    w.writeheader(); w.writerows(out)
print(len(out), "rows")
