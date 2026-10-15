import csv, sys, math, statistics as st, datetime as dt, collections
W=sys.argv[1]; TODAY=dt.date(2026,10,13)
S={r["code"]:r for r in csv.DictReader(open(f"{W}/data/sample_priority.csv"))}
L={r["code"]:r for r in csv.DictReader(open(f"{W}/data/live_productfeed.csv"))}
obs=collections.defaultdict(list)
for r in csv.DictReader(open(f"{W}/data/wb_obs.csv")):
    c=r["code"]
    if c not in S: continue
    d=(dt.date.fromisoformat(r["obs_date"])-dt.date.fromisoformat(S[c]["release_date"])).days
    if d<0: continue
    obs[c].append((d,float(r["current"])<float(r["full"])-0.5,float(r["discount_pct"]),r["wayback_url"]))
rows=[]
for c,s in S.items():
    age=(TODAY-dt.date.fromisoformat(s["release_date"])).days
    o=sorted(obs[c]); dis=[x for x in o if x[1]]
    F=dis[0][0] if dis else math.inf; Fsrc=dis[0][3] if dis else ""; depth=dis[0][2] if dis else ""
    l=L.get(c); live_disc=bool(l and float(l["current"])<float(l["full"])-0.5)
    if live_disc and age<F: F=age; Fsrc="live product_feed 2026-10-13"; depth=round(100*(1-float(l["current"])/float(l["full"])),1)
    lo=max([0]+[x[0] for x in o if not x[1] and x[0]<F])
    lourl=next((x[3] for x in o if not x[1] and x[0]==lo),"")
    st_={}
    for T in (30,60,90,180):
        if T>age: st_[T]="too_young"
        elif F<=T: st_[T]="yes"
        elif lo>=T: st_[T]="no"
        else: st_[T]="unknown"
    rows.append(dict(code=c,line=s["line"],release_year=s["release_year"],release_date=s["release_date"],retail=s["retail_usd"],age_days=age,n_wayback_obs=len(o),
        last_full_day=lo,first_disc_day=("" if F==math.inf else F),first_disc_window=("" if F==math.inf else f"{lo}-{F}"),first_disc_depth_pct=depth,
        censored_full_through_day=(lo if F==math.inf else ""),live_available=(l or {}).get("available",""),live_current=(l or {}).get("current",""),live_full=(l or {}).get("full",""),
        within30=st_[30],within60=st_[60],within90=st_[90],within180=st_[180],last_full_source=lourl,first_disc_source=Fsrc))
w=csv.DictWriter(open(f"{W}/data/time_to_markdown_by_colorway.csv","w",newline=""),fieldnames=list(rows[0].keys())); w.writeheader(); [w.writerow(r) for r in rows]
g=collections.defaultdict(list)
for r in rows: g[(r["line"],r["release_year"])].append(r)
out=csv.writer(open(f"{W}/data/time_to_markdown_cohort_table.csv","w",newline=""))
hdr=["line","release_year","n","n_with_wayback_obs"]+[f"disc_within_{T}d_yes/known" for T in (30,60,90,180)]+["n_discounted_ever_observed","median_first_disc_day_upper_bound","n_censored_full","median_censor_day","median_depth_pct"]
out.writerow(hdr); print(hdr)
for k in sorted(g):
    v=g[k]; cells=[]
    for T in (30,60,90,180):
        y=sum(r[f"within{T}"]=="yes" for r in v); n=sum(r[f"within{T}"] in("yes","no") for r in v); cells.append(f"{y}/{n}")
    d=[r for r in v if r["first_disc_day"]!=""]; cz=[r for r in v if r["censored_full_through_day"]!="" and r["n_wayback_obs"]>0]
    row=[*k,len(v),sum(r["n_wayback_obs"]>0 for r in v),*cells,len(d),st.median([r["first_disc_day"] for r in d]) if d else "",len(cz),st.median([r["censored_full_through_day"] for r in cz]) if cz else "",st.median([r["first_disc_depth_pct"] for r in d]) if d else ""]
    out.writerow(row); print(row)
