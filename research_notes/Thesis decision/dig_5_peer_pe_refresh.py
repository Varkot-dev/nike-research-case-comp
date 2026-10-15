"""Refresh peer forward P/E from ONE source (Yahoo quoteSummary earningsTrend + price) on ONE run date.
Usage: python3 -I peer_pe_refresh.py OUT.csv
P/E FY1 = last close / consensus EPS current FY (0y); FY2 = / next FY (+1y).
Prices for On (USD, reports CHF) and Anta (HKD, reports CNY) converted with Yahoo FX on the same run."""
import sys, json, csv, statistics, http.cookiejar, urllib.request, datetime
cj = http.cookiejar.CookieJar()
op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
op.addheaders = [("User-Agent", "Mozilla/5.0")]
def get(u):
    return op.open(u, timeout=30).read().decode()
try: get("https://fc.yahoo.com")
except Exception: pass
crumb = get("https://query1.finance.yahoo.com/v1/test/getcrumb")
T = [("NKE","Nike",None),("ADS.DE","adidas",None),("PUM.DE","Puma",None),("DECK","Deckers",None),
     ("ONON","On Holding","USDCHF=X"),("LULU","Lululemon",None),("UAA","Under Armour A",None),
     ("7936.T","ASICS",None),("2020.HK","Anta Sports","HKDCNY=X"),("VFC","VF Corp",None)]
def qs(t, mods):
    u = f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{t}?modules={mods}&crumb={crumb}"
    return json.loads(get(u))["quoteSummary"]["result"][0]
rows = []
for t, n, fx in T:
    r = qs(t, "price,earningsTrend")
    p = r["price"]["regularMarketPrice"]["raw"]; ccy = r["price"]["currency"]
    tr = {x["period"]: x for x in r["earningsTrend"]["trend"]}
    e1 = tr["0y"]["earningsEstimate"]["avg"].get("raw"); e2 = tr["+1y"]["earningsEstimate"]["avg"].get("raw")
    n1 = tr["0y"]["earningsEstimate"].get("numberOfAnalysts", {}).get("raw")
    fxr = qs(fx, "price")["price"]["regularMarketPrice"]["raw"] if fx else 1.0
    pc = p * fxr
    pe1 = pc / e1 if e1 and e1 > 0 else None; pe2 = pc / e2 if e2 and e2 > 0 else None
    rows.append(dict(ticker=t, name=n, price=p, ccy=ccy, fx=fxr, fy1_end=tr["0y"]["endDate"], eps_fy1=e1, eps_fy2=e2,
                     pe_fy1=round(pe1,1) if pe1 else "NM", pe_fy2=round(pe2,1) if pe2 else "NM", analysts_fy1=n1,
                     price_time=datetime.datetime.fromtimestamp(r["price"]["regularMarketTime"], datetime.timezone.utc).isoformat()))
peers = [x for x in rows if x["ticker"] != "NKE"]
m1 = statistics.median([x["pe_fy1"] for x in peers if x["pe_fy1"] != "NM"])
m2 = statistics.median([x["pe_fy2"] for x in peers if x["pe_fy2"] != "NM"])
w = csv.DictWriter(open(sys.argv[1], "w", newline=""), fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
for x in rows: print(x)
nke = rows[0]
print(f"peer median FY1 {m1:.1f} FY2 {m2:.1f}; NKE FY1 {nke['pe_fy1']} FY2 {nke['pe_fy2']}; premium FY2 {nke['pe_fy2']/m2-1:.0%}, FY1 {nke['pe_fy1']/m1-1:.0%}")
cy27 = 5/12*nke["eps_fy1"] + 7/12*nke["eps_fy2"]
print(f"NKE calendar-2027 EPS {cy27:.3f}, P/E {nke['price']/cy27:.1f}, premium vs FY2 median {nke['price']/cy27/m2-1:.0%}")
