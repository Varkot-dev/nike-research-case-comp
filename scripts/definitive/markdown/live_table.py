import csv, sys, statistics as st, datetime as dt, collections
W=sys.argv[1]
L={r["code"]:r for r in csv.DictReader(open(f"{W}/data/live_productfeed.csv"))}
rows=[]
for fn,grp in (("sample_jordan.csv","Jordan"),("sample_control.csv","Control")):
    for r in csv.DictReader(open(f"{W}/data/{fn}")):
        l=L.get(r["code"])
        if not l: continue
        age=(dt.date(2026,10,13)-dt.date.fromisoformat(r["release_date"])).days
        cur,full=float(l["current"]),float(l["full"])
        rows.append(dict(group=grp,line=r["line"],year=r["release_year"],code=r["code"],release_date=r["release_date"],age_days=age,
            collab=r["collab_or_special"],available=l["available"],full=full,current=cur,disc_today=cur<full-0.5,depth_pct=round(100*(1-cur/full),1),pdp_url=l["pdp_url"]))
w=csv.DictWriter(open(f"{W}/data/live_status_by_colorway_20261013.csv","w",newline=""),fieldnames=list(rows[0].keys())+["label"])
w.writeheader()
for r in rows: r["label"]="VERIFIED (api.nike.com product_feed opened 2026-10-13); disc/depth DERIVED"; w.writerow(r)
g=collections.defaultdict(list)
for r in rows:
    if r["available"]!="True" or r["collab"]=="True": continue
    key=(r["group"],r["line"] if r["group"]=="Control" or r["line"] in ("AJ1 High OG","AJ1 Low OG","AJ3","AJ4","AJ5","AJ11","AJ12") else "Other Jordan",r["year"])
    g[key].append(r)
out=csv.writer(open(f"{W}/data/live_cohort_table_20261013.csv","w",newline=""))
out.writerow(["group","line","release_year","n_available_colorways","n_discounted_today","share_discounted_today_pct_DERIVED","median_depth_of_discounted_pct_DERIVED"])
for k in sorted(g):
    v=g[k]; d=[x for x in v if x["disc_today"]]
    row=[*k,len(v),len(d),round(100*len(d)/len(v),1),st.median([x["depth_pct"] for x in d]) if d else ""]
    out.writerow(row); print(row)
