"""Builds derived CSVs from raw/tranco_expanded_long.csv.
Outputs (in ..): tranco_rank_wide.csv (date x domain), tranco_control_basket.csv, tranco_listwide_drift.csv (from scratch top5000 files),
tranco_zipf_traffic_index.csv (traffic index vs same month prior year, alpha=1 and 0.8/1.2), tranco_fq_yoy.csv (Nike fiscal quarters).
Run: python3 -I analyze_tranco.py <top5000_dir>
"""
import csv, gzip, json, math, os, sys, statistics as st, glob, datetime
TOP=sys.argv[1]; D=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..")
rows=list(csv.DictReader(open(os.path.join(D,"raw/tranco_expanded_long.csv"))))
R={}
for r in rows:
    if r["rank"]!="": R.setdefault(r["date"],{})[r["domain"]]=int(r["rank"])
dates=sorted(R)
doms=sorted({r["domain"] for r in rows})
with open(os.path.join(D,"tranco_rank_wide.csv"),"w",newline="") as f:
    w=csv.writer(f); w.writerow(["date"]+doms)
    for d in dates: w.writerow([d]+[R[d].get(x,"") for x in doms])
CONTROL=["amazon.com","walmart.com","target.com","bestbuy.com","homedepot.com","lowes.com","ebay.com","etsy.com","macys.com","kohls.com","wayfair.com","costco.com","ikea.com","zara.com","hm.com","uniqlo.com","sephora.com","nordstrom.com","gap.com","ulta.com","chewy.com","apple.com","netflix.com","spotify.com","wikipedia.org","linkedin.com","paypal.com","cvs.com","walgreens.com","kroger.com"]
def prior(ds):
    d=datetime.date.fromisoformat(ds)
    try: return d.replace(year=d.year-1).isoformat()
    except ValueError: return d.replace(year=d.year-1,day=28).isoformat()
# list-wide drift: median over domains ranked 100..3000 on BOTH dates of rank_t/rank_{t-1y}; also rank-weighted
drift={}
for d in dates:
    p=prior(d); a=os.path.join(TOP,f"top5000_{d}.json.gz"); b=os.path.join(TOP,f"top5000_{p}.json.gz")
    if not (os.path.exists(a) and os.path.exists(b)): continue
    A=json.load(gzip.open(a,"rt")); B=json.load(gzip.open(b,"rt"))
    lr=[math.log(A[x]/B[x]) for x in A if x in B and 150<=B[x]<=1500]
    if len(lr)>=50: drift[d]=(st.median(lr),len(lr))
with open(os.path.join(D,"tranco_listwide_drift.csv"),"w",newline="") as f:
    w=csv.writer(f); w.writerow(["date","median_log_rank_ratio_vs_1y_ago_for_domains_ranked_150_1500_1y_ago","n_domains"])
    for d,(m,n) in drift.items(): w.writerow([d,round(m,4),n])
def ctrl(d):
    p=prior(d)
    lr=[math.log(R[d][x]/R[p][x]) for x in CONTROL if d in R and p in R and x in R[d] and x in R[p]]
    return (st.median(lr),len(lr)) if len(lr)>=8 else (None,0)
with open(os.path.join(D,"tranco_control_basket.csv"),"w",newline="") as f:
    w=csv.writer(f); w.writerow(["date","median_log_rank_ratio_vs_1y_ago_retail_media_basket","n"])
    for d in dates:
        m,n=ctrl(d)
        if m is not None: w.writerow([d,round(m,4),n])
BR=["nike.com","adidas.com","on.com","on-running.com","hoka.com","newbalance.com","asics.com","lululemon.com","dickssportinggoods.com","footlocker.com","nike.com.cn","adidas.de","adidas.co.uk","adidas.co.jp","puma.com","underarmour.com","jdsports.co.uk","zalando.de"]
out=[]
for d in dates:
    p=prior(d)
    if p not in R: continue
    c,_=ctrl(d); l=drift.get(d,(None,0))[0]
    for x in BR:
        if x in R[d] and x in R[p]:
            lr=math.log(R[d][x]/R[p][x])  # >0 means rank number rose = worse
            row={"date":d,"domain":x,"rank_now":R[d][x],"rank_1y_ago":R[p][x],"log_rank_ratio":round(lr,4)}
            for a in (0.8,1.0,1.2):
                row[f"raw_traffic_yoy_pct_alpha{a}"]=round((math.exp(-a*lr)-1)*100,1)
                if c is not None: row[f"adj_vs_basket_yoy_pct_alpha{a}"]=round((math.exp(-a*(lr-c))-1)*100,1)
                if l is not None: row[f"adj_vs_listdrift_yoy_pct_alpha{a}"]=round((math.exp(-a*(lr-l))-1)*100,1)
            row["basket_log_ratio"]=round(c,4) if c is not None else ""
            row["listdrift_log_ratio"]=round(l,4) if l is not None else ""
            out.append(row)
keys=["date","domain","rank_now","rank_1y_ago","log_rank_ratio","basket_log_ratio","listdrift_log_ratio"]+sorted({k for r in out for k in r if k not in ("date","domain","rank_now","rank_1y_ago","log_rank_ratio","basket_log_ratio","listdrift_log_ratio")})
with open(os.path.join(D,"tranco_zipf_traffic_index.csv"),"w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=keys); w.writeheader(); w.writerows(out)
# Nike fiscal quarter windows: Q1 Jun-Aug, Q2 Sep-Nov, Q3 Dec-Feb, Q4 Mar-May
def fq(ds):
    y,m=int(ds[:4]),int(ds[5:7])
    if m>=6: fy=y+1; q=1 if m<=8 else (2 if m<=11 else 3)
    else: fy=y; q=3 if m<=2 else 4
    return f"FY{fy}Q{q}"
agg={}
for r in out:
    agg.setdefault((fq(r["date"]),r["domain"]),[]).append(r)
with open(os.path.join(D,"tranco_fq_yoy.csv"),"w",newline="") as f:
    w=csv.writer(f); w.writerow(["fq","domain","n_dates","raw_yoy_pct_a1","adj_basket_yoy_pct_a1","adj_listdrift_yoy_pct_a1","adj_listdrift_yoy_pct_a0.8","adj_listdrift_yoy_pct_a1.2"])
    for (q,x),v in sorted(agg.items()):
        def m(k):
            vals=[r[k] for r in v if k in r]
            return round(st.mean(vals),1) if vals else ""
        w.writerow([q,x,len(v),m("raw_traffic_yoy_pct_alpha1.0"),m("adj_vs_basket_yoy_pct_alpha1.0"),m("adj_vs_listdrift_yoy_pct_alpha1.0"),m("adj_vs_listdrift_yoy_pct_alpha0.8"),m("adj_vs_listdrift_yoy_pct_alpha1.2")])
print("done",len(dates),"dates",len(drift),"drift dates")
