import json,http.cookiejar,urllib.request,datetime,sys
cj=http.cookiejar.CookieJar();op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj));op.addheaders=[("User-Agent","Mozilla/5.0")]
def get(u): return op.open(u,timeout=40).read().decode()
try: get("https://fc.yahoo.com")
except Exception: pass
crumb=get("https://query1.finance.yahoo.com/v1/test/getcrumb")
ts=datetime.datetime.utcnow().isoformat()+"Z"
for t in ["NKE","ADS.DE","ADDYY","ONON","DECK","LULU","UAA","PUM.DE"]:
    u=f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{t}?modules=earningsTrend,earningsHistory,upgradeDowngradeHistory,financialData,recommendationTrend,price&crumb={crumb}"
    try:
        d=get(u); open(f"qs_{t}.json","w").write(d); print(t,len(d),ts)
    except Exception as e: print(t,"ERR",e)
