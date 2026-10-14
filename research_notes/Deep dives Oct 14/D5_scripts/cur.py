import sys, json, csv, http.cookiejar, urllib.request, datetime
cj = http.cookiejar.CookieJar()
op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
op.addheaders = [("User-Agent", "Mozilla/5.0")]
def get(u): return op.open(u, timeout=30).read().decode()
try: get("https://fc.yahoo.com")
except Exception: pass
crumb = get("https://query1.finance.yahoo.com/v1/test/getcrumb")
T = ["NKE","ADS.DE","PUM.DE","DECK","ONON","LULU","UAA","7936.T","2020.HK","VFC"]
out = {}
for t in T:
    u = f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{t}?modules=price,earningsTrend,financialData,defaultKeyStatistics,summaryDetail&crumb={crumb}"
    r = json.loads(get(u))["quoteSummary"]["result"][0]
    out[t] = r
json.dump(out, open(sys.argv[1], "w"))
def raw(d, k):
    v = d.get(k); return v.get("raw") if isinstance(v, dict) else v
rows = []
for t, r in out.items():
    tr = {x["period"]: x for x in r["earningsTrend"]["trend"]}
    fd = r["financialData"]; ks = r["defaultKeyStatistics"]
    rows.append(dict(ticker=t, price=raw(r["price"], "regularMarketPrice"), ccy=r["price"]["currency"],
        eps0=tr["0y"]["earningsEstimate"]["avg"].get("raw"), eps1=tr["+1y"]["earningsEstimate"]["avg"].get("raw"),
        rev0=tr["0y"]["revenueEstimate"]["avg"].get("raw"), rev1=tr["+1y"]["revenueEstimate"]["avg"].get("raw"),
        rev_growth0=tr["0y"]["revenueEstimate"].get("growth",{}).get("raw"), rev_growth1=tr["+1y"]["revenueEstimate"].get("growth",{}).get("raw"),
        eps_growth1=tr["+1y"]["earningsEstimate"].get("growth",{}).get("raw"),
        roe=raw(fd,"returnOnEquity"), roa=raw(fd,"returnOnAssets"), opm=raw(fd,"operatingMargins"), gm=raw(fd,"grossMargins"),
        fcf=raw(fd,"freeCashflow"), ocf=raw(fd,"operatingCashflow"), totrev=raw(fd,"totalRevenue"), ebitda=raw(fd,"ebitda"),
        ni=raw(ks,"netIncomeToCommon"), ev=raw(ks,"enterpriseValue"), ev_rev=raw(ks,"enterpriseToRevenue"), ev_ebitda=raw(ks,"enterpriseToEbitda"),
        mcap=raw(r["price"],"marketCap"), beta=raw(ks,"beta")))
w = csv.DictWriter(open(sys.argv[2],"w",newline=""), list(rows[0])); w.writeheader(); w.writerows(rows)
for x in rows: print(x)
