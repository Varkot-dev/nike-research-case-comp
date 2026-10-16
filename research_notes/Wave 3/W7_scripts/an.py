import json,csv,datetime
TS="2026-10-16T16:38Z"
rows=[];acts=[]
def r(d,k):
    v=d.get(k); return v.get("raw") if isinstance(v,dict) else v
for t in ["NKE","ADS.DE","ADDYY","ONON","DECK","LULU","UAA","PUM.DE"]:
    j=json.load(open(f"qs_{t}.json"))["quoteSummary"]["result"][0]
    px=j["price"].get("regularMarketPrice",{}).get("raw")
    for x in j["earningsTrend"]["trend"]:
        e=x["earningsEstimate"];rv=x["revenueEstimate"];tr=x["epsTrend"];rev=x["epsRevisions"]
        rows.append(dict(ticker=t,period=x["period"],endDate=x.get("endDate"),pulled=TS,price=px,
          eps_avg=r(e,"avg"),eps_low=r(e,"low"),eps_high=r(e,"high"),eps_n=r(e,"numberOfAnalysts"),eps_yago=r(e,"yearAgoEps"),
          rev_avg=r(rv,"avg"),rev_low=r(rv,"low"),rev_high=r(rv,"high"),rev_n=r(rv,"numberOfAnalysts"),
          eps_cur=r(tr,"current"),eps_7d=r(tr,"7daysAgo"),eps_30d=r(tr,"30daysAgo"),eps_60d=r(tr,"60daysAgo"),eps_90d=r(tr,"90daysAgo"),
          up7=r(rev,"upLast7days"),up30=r(rev,"upLast30days"),dn7=r(rev,"downLast7Days"),dn30=r(rev,"downLast30days")))
    if t=="NKE":
        for h in j["upgradeDowngradeHistory"]["history"]:
            d=datetime.datetime.fromtimestamp(h["epochGradeDate"],datetime.timezone.utc).date().isoformat()
            acts.append(dict(date=d,firm=h["firm"],from_grade=h.get("fromGrade"),to_grade=h.get("toGrade"),action=h.get("action"),pt_action=h.get("priceTargetAction"),pt=h.get("currentPriceTarget"),prior_pt=h.get("priorPriceTarget"),pulled=TS))
        print("EH",[(x["quarter"]["fmt"],x["epsActual"].get("raw"),x["epsEstimate"].get("raw"),x["surprisePercent"].get("raw")) for x in j["earningsHistory"]["history"]])
        print({k:r(j["financialData"],k) for k in ["currentPrice","targetMeanPrice","targetHighPrice","targetLowPrice","targetMedianPrice","numberOfAnalystOpinions","recommendationMean"]})
        print(j["recommendationTrend"]["trend"])
w=csv.DictWriter(open("snap.csv","w",newline=""),list(rows[0]));w.writeheader();w.writerows(rows)
acts.sort(key=lambda a:a["date"],reverse=True)
w=csv.DictWriter(open("acts.csv","w",newline=""),list(acts[0]));w.writeheader();w.writerows(acts)
print(len(acts),acts[0]["date"],acts[-1]["date"])
for x in rows:
    if x["period"] in("0y","+1y"): print(x["ticker"],x["period"],x["endDate"],x["eps_cur"],x["eps_7d"],x["eps_30d"],x["eps_60d"],x["eps_90d"],x["eps_low"],x["eps_high"],x["eps_n"],x["rev_avg"],x["up7"],x["dn7"],x["up30"],x["dn30"])
