import json,http.cookiejar,urllib.request,datetime,csv,time
from concurrent.futures import ThreadPoolExecutor
T="""NKE ADDYY ONON DECK LULU UAA VFC PVH RL TPR CPRI HBI GIII OXM COLM CROX SKX BIRD WWW FL DKS ASO BOOT SHOO CAL LEVI KTB PLCE AEO ANF URBN GPS BURL ROST TJX KSS M JWN DDS AMZN EBAY ETSY W CHWY WSM RH ARHS BBWI VSCO HAS MAT FUN PTON YETI SONO GRMN FOSL SN LEG LZB PII HOG BC THO WGO F GM TSLA HD LOW FND TSCO ORLY AZO GPC LKQ KMX CVNA LAD AN PAG SAH ABG GPI DRI CMG SBUX MCD YUM DPZ QSR WING SHAK CAKE TXRT BLMN EAT BROS CAVA KDP PEP KO MNST CELH STZ TAP MDLZ HSY GIS CPB CAG SJM HRL TSN KHC MKC CL KMB PG CLX CHD EL COTY ELF HELE NWL SPB WMT COST TGT DG DLTR BJ KR ACI SFM PM MO NCLH CCL RCL LVS WYNN MGM CZR DKNG PLNT MTN SIX CHDN LYV TTWO EA SCVL GCO DBI VRA LE JILL CATO ZUMZ APTV BWA LEA ALV GT GNTX ADNT AAL DAL UAL LUV JBLU AAPL MSFT NVDA INTC AMD CRM ADBE ORCL CSCO TXN QCOM PFE MRK JNJ ABBV BMY LLY AMGN GILD UNH CVS CI HUM ELV BA GE CAT DE MMM HON UPS FDX UNP CSX NSC LMT RTX GD NOC XOM CVX COP OXY SLB DOW LYB DD NUE FCX NEM LIN APD SHW PPG ECL JPM BAC WFC C GS MS SCHW AXP COF DFS V MA PYPL T VZ TMUS CMCSA DIS NFLX WBD PARA""".split()
T=list(dict.fromkeys(T))
cj=http.cookiejar.CookieJar();op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj));op.addheaders=[("User-Agent","Mozilla/5.0")]
def get(u): return op.open(u,timeout=40).read().decode()
try: get("https://fc.yahoo.com")
except Exception: pass
crumb=get("https://query1.finance.yahoo.com/v1/test/getcrumb")
def g(x,k):
    v=x["epsTrend"].get(k)
    return v.get("raw") if isinstance(v,dict) else v
def one(t):
    for k in range(2):
        try:
            d=json.loads(get(f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{t}?modules=earningsTrend&crumb={crumb}"))
            out=[]
            for x in d["quoteSummary"]["result"][0]["earningsTrend"]["trend"]:
                if x["period"] in("0y","+1y"):
                    out.append(dict(ticker=t,period=x["period"],end=x.get("endDate"),cur=g(x,"current"),d7=g(x,"7daysAgo"),d30=g(x,"30daysAgo"),d60=g(x,"60daysAgo"),d90=g(x,"90daysAgo"),n=(x["earningsEstimate"].get("numberOfAnalysts") or {}).get("raw")))
            return out
        except Exception as e:
            time.sleep(1)
    return []
with ThreadPoolExecutor(6) as ex: res=list(ex.map(one,T))
rows=[r for x in res for r in x]
ts=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
for r in rows: r["pulled"]=ts
w=csv.DictWriter(open("universe.csv","w",newline=""),list(rows[0]));w.writeheader();w.writerows(rows)
print(len(T),len(rows),ts)
