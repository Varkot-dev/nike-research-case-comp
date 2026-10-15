"""Tests for G6. Run: python3 -I tests.py   (reads files in ..; writes test_*.csv; prints results)"""
import csv, math, os, statistics as st
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..")
H=os.path.join(D,"..")  # data/hunt
def rd(p): return list(csv.DictReader(open(os.path.join(D,p) if not p.startswith("/") else p)))
def corr(x,y):
    mx,my=st.mean(x),st.mean(y); sx=sum((a-mx)**2 for a in x); sy=sum((b-my)**2 for b in y)
    return sum((a-mx)*(b-my) for a,b in zip(x,y))/math.sqrt(sx*sy)
def slope(x,y):
    mx,my=st.mean(x),st.mean(y); return sum((a-mx)*(b-my) for a,b in zip(x,y))/sum((a-mx)**2 for a in x)
# ---- A. Zipf exponent calibration: Semrush Sep-2026 global visits vs Tranco rank 2026-10-01 (cross-section)
sem={}
for r in csv.DictReader(open(os.path.join(H,"apps_digital/web_semrush_history.csv"))):
    if r["metric"]=="visits" and r["month"]=="2026-09-01": sem[r["domain"]]=float(r["value"])
tr={r["domain"]:r for r in rd("raw/tranco_expanded_long.csv") if r["date"]=="2026-10-01" and r["rank"]}
pts=[(d,int(tr[d]["rank"]),sem[d]) for d in sem if d in tr]
x=[math.log(p[1]) for p in pts]; y=[math.log(p[2]) for p in pts]
a=-slope(x,y); r=corr(x,y)
with open(os.path.join(D,"test_alpha_calibration.csv"),"w",newline="") as f:
    w=csv.writer(f); w.writerow(["domain","tranco_rank_2026-10-01","semrush_visits_2026-09"]); w.writerows(pts)
print(f"A. Zipf alpha (OLS slope of log visits on log rank) = {a:.2f}, corr {r:.2f}, n={len(pts)}")
# ---- B. Tranco-implied YoY vs Semrush US trending YoY (Aug 2026)
trend={r["domain"]:float(r["yoy_pct"]) for r in rd("semrush_trending_2026-08_long.csv") if r["country"]=="us" and r["category"]=="sporting-goods" and r["yoy_pct"]!=""}
for r_ in rd("semrush_trending_2026-08_long.csv"):
    if r_["country"]=="us" and r_["domain"] in("lululemon.com","footlocker.com") and r_["yoy_pct"]!="": trend[r_["domain"]]=float(r_["yoy_pct"])
z=rd("tranco_zipf_traffic_index.csv")
rowsB=[]
for dom,sy in trend.items():
    v=[r_ for r_ in z if r_["domain"]==dom and r_["date"] in("2026-08-01","2026-08-15")]
    if len(v)==2:
        raw=st.mean(float(q["raw_traffic_yoy_pct_alpha1.0"]) for q in v)
        adj=st.mean(float(q["adj_vs_listdrift_yoy_pct_alpha1.0"]) for q in v if q.get("adj_vs_listdrift_yoy_pct_alpha1.0"))
        rowsB.append((dom,sy,round(raw,1),round(adj,1)))
with open(os.path.join(D,"test_tranco_vs_semrush_us_yoy_aug2026.csv"),"w",newline="") as f:
    w=csv.writer(f); w.writerow(["domain","semrush_us_yoy_pct_aug2026","tranco_raw_implied_yoy_pct","tranco_listdrift_adj_implied_yoy_pct"]); w.writerows(rowsB)
print("B. n=",len(rowsB),"corr(Semrush US YoY, Tranco adj implied YoY)=",round(corr([q[1] for q in rowsB],[q[3] for q in rowsB]),2), "corr raw",round(corr([q[1] for q in rowsB],[q[2] for q in rowsB]),2))
for q in rowsB: print("   ",q)
# ---- C. Tranco nike.com adj YoY vs reported NIKE Brand Digital growth by fiscal quarter
rep={"FY2025Q1":-20,"FY2025Q2":-21,"FY2025Q3":-15,"FY2025Q4":-26,"FY2026Q1":-12,"FY2026Q2":-14,"FY2026Q3":-9,"FY2026Q4":-12,"FY2027Q1":-13}
fq={(r_["fq"],r_["domain"]):r_ for r_ in rd("tranco_fq_yoy.csv")}
rowsC=[]
for q,g in rep.items():
    t=fq.get((q,"nike.com")); rowsC.append((q,g,t["raw_yoy_pct_a1"],t["adj_basket_yoy_pct_a1"],t["adj_listdrift_yoy_pct_a1"]))
with open(os.path.join(D,"test_tranco_nike_vs_reported_digital.csv"),"w",newline="") as f:
    w=csv.writer(f); w.writerow(["fiscal_quarter","reported_nike_brand_digital_growth_pct","tranco_nike_raw_yoy_pct_a1","tranco_nike_adj_basket_yoy_pct_a1","tranco_nike_adj_listdrift_yoy_pct_a1"]); w.writerows(rowsC)
for k in (2,3,4):
    xs=[float(q[k]) for q in rowsC]; ys=[q[1] for q in rowsC]
    print(f"C. corr(reported digital growth, tranco col {k}) = {corr(xs,ys):.2f}  (n={len(xs)}); mean tranco {st.mean(xs):.1f} vs mean reported {st.mean(ys):.1f}")
# ---- D. Semrush Aug-2026 country YoY, nike.com vs reported regional digital growth
REG={"NA (digital -6% cc)":["us","ca"],"EMEA (digital -26% cc)":["de","gb","fr","it","es","nl","pl","se"],"APLA (digital -10% cc)":["jp","kr","au","mx","tw","in"]}
sw=[r_ for r_ in rd("semrush_trending_2026-08_long.csv") if r_["category"]=="sporting-goods"]
def lvl(cc,dom):
    for r_ in sw:
        if r_["country"]==cc and r_["domain"]==dom and r_["yoy_pct"]!="": return float(r_["total_traffic"]),float(r_["yoy_pct"])
outD=[]
for reg,ccs in REG.items():
    for excl in (None,"gb"):
        n=p=0; used=[]
        for cc in ccs:
            if cc==excl: continue
            v=lvl(cc,"nike.com")
            if v: n+=v[0]; p+=v[0]/(1+v[1]/100); used.append(cc)
        if n: outD.append((reg,"all" if excl is None else "ex-GB",",".join(used),round(n/1e6,2),round((n/p-1)*100,1)))
with open(os.path.join(D,"test_region_semrush_yoy_vs_digital.csv"),"w",newline="") as f:
    w=csv.writer(f); w.writerow(["region_and_reported_digital","set","countries","aug2026_visits_m","traffic_weighted_yoy_pct"]); w.writerows(outD)
for o in outD: print("D.",o)
# peers same countries
peers={"us":["adidas.com","newbalance.com","asics.com","puma.com","dickssportinggoods.com","jdsports.com"],"de":["adidas.de","newbalance.de","puma.com","jdsports.de"],"gb":["adidas.co.uk","newbalance.co.uk","jdsports.co.uk","sportsdirect.com","puma.com"],"fr":["adidas.fr","jdsports.fr","decathlon.com","puma.com"],"jp":["newbalance.jp","asics.com","puma.com"]}
with open(os.path.join(D,"test_nike_vs_peers_semrush_yoy_aug2026.csv"),"w",newline="") as f:
    w=csv.writer(f); w.writerow(["country","domain","aug2026_visits","yoy_pct","nike_yoy_pct","nike_minus_peer_pts"])
    for cc,ds in peers.items():
        nv=lvl(cc,"nike.com")
        for d in ds:
            v=lvl(cc,d)
            if v and nv: w.writerow([cc,d,int(v[0]),v[1],nv[1],round(nv[1]-v[1],1)])
