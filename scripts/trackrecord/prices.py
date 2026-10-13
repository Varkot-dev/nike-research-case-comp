import csv,json,sys,datetime,statistics as st
pf,spxf,out=sys.argv[1:4]
P=[(r['date'],float(r['close_usd'])) for r in csv.DictReader(open(pf))]
dates=[d for d,_ in P]; px=dict(P)
j=json.load(open(spxf))['chart']['result'][0]
spx={datetime.datetime.fromtimestamp(t+j["meta"]["gmtoffset"],datetime.UTC).strftime('%Y-%m-%d'):c for t,c in zip(j['timestamp'],j['indicators']['quote'][0]['close']) if c}
E=[('2019-06-27','Q4 FY19','pre-tracker',''),('2019-09-24','Q1 FY20','pre-tracker',''),('2019-12-19','Q2 FY20','pre-tracker',''),('2020-03-24','Q3 FY20','pre-tracker','Covid'),
('2020-06-25','Q4 FY20','pre-tracker','June 2020 digital 50% vision'),('2020-09-22','Q1 FY21','pre-tracker',''),('2020-12-18','Q2 FY21','pre-tracker',''),('2021-03-18','Q3 FY21','pre-tracker',''),
('2021-06-24','Q4 FY21','pre-tracker','June 2021 targets through FY25'),('2021-09-23','Q1 FY22','pre-tracker','FY22 guide cut'),('2021-12-20','Q2 FY22','pre-tracker',''),('2022-03-21','Q3 FY22','pre-tracker',''),
('2022-06-27','Q4 FY22','initial','FY23 guide: c-n LDD, GM flat to -50'),
('2022-09-29','Q1 FY23','cut','FY23 GM cut to -200/-250'),
('2022-12-20','Q2 FY23','raise','FY23 c-n revenue raised to low teens'),
('2023-03-21','Q3 FY23','raise','FY23 reported revenue raised to HSD; GM to low end'),
('2023-06-29','Q4 FY23','initial','FY24 guide: revenue MSD, GM +140/+160'),
('2023-09-28','Q1 FY24','maintain','FY24 maintained'),
('2023-12-21','Q2 FY24','cut','FY24 revenue cut to ~1%; $2B savings plan'),
('2024-03-21','Q3 FY24','cut','FY25 preview: H1 down LSD'),
('2024-06-27','Q4 FY24','cut','FY25 guide: down MSD'),
('2024-09-19','CEO news','other','Hill named CEO (announced after close Sep 19); not an earnings event'),
('2024-10-01','Q1 FY25','withdraw','FY25 guidance withdrawn; Investor Day postponed'),
('2024-12-19','Q2 FY25','quarterly','Q3 guide: revenue down LDD'),
('2025-03-20','Q3 FY25','quarterly','Q4 guide: revenue down mid-teens'),
('2025-06-26','Q4 FY25','quarterly','Q1 FY26 guide: revenue down MSD; Q4 called largest Win Now impact'),
('2025-09-30','Q1 FY26','quarterly','Q2 guide: revenue down LSD'),
('2025-12-18','Q2 FY26','quarterly','Q3 guide: revenue down LSD'),
('2026-03-31','Q3 FY26','multi-quarter','Q4 FY26 to Q2 FY27 guide; Win Now done by Dec 2026'),
('2026-06-30','Q4 FY26','cut','Q4 FY26 to Q2 FY27 revenue lowered to down LSD-MSD'),
('2026-10-01','Q1 FY27','initial (below consensus)','FY27: revenue down HSD, adj. EPS 1.15 to 1.35; Pace $2.5B savings'),]
def idx(d):
    # index of the release-day close (release after the close); if d not a trading day use prior day
    while d not in px: d=(datetime.date.fromisoformat(d)-datetime.timedelta(days=1)).isoformat()
    return dates.index(d)
rows=[]
for d,lab,cat,note in E:
    i=idx(d); c0=px[dates[i]]
    def r(k):
        if i+k>=len(dates): return None
        return round((px[dates[i+k]]/c0-1)*100,1)
    def m(k):
        if i+k>=len(dates): return None
        a,b=dates[i],dates[i+k]
        if a in spx and b in spx: return round((spx[b]/spx[a]-1)*100,1)
        return None
    r1,r5,r20=r(1),r(5),r(20)
    m1,m5,m20=m(1),m(5),m(20)
    drift = None if r20 is None else round(((1+r20/100)/(1+r1/100)-1)*100,1)
    rel=lambda a,b: None if a is None or b is None else round(a-b,1)
    rows.append(dict(event_date=d,event=lab,guidance_signal=cat,note=note,close_day0=c0,day0_date=dates[i],
      ret_1d_pct=r1,ret_5d_pct=r5,ret_20d_pct=r20,drift_day1_to_day20_pct=drift,spx_1d_pct=m1,spx_5d_pct=m5,spx_20d_pct=m20,
      excess_1d_pct=rel(r1,m1),excess_5d_pct=rel(r5,m5),excess_20d_pct=rel(r20,m20),
      source='market data: data/nke_daily_prices.csv (Yahoo closes); S&P 500 from Yahoo ^GSPC chart API; event dates from 8-K filing dates'))
w=csv.DictWriter(open(out,'w',newline=''),fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
for r in rows: print(r['event'],r['event_date'],r['guidance_signal'],r['close_day0'],r['ret_1d_pct'],r['ret_5d_pct'],r['ret_20d_pct'],'drift',r['drift_day1_to_day20_pct'],'ex1',r['excess_1d_pct'],'ex5',r['excess_5d_pct'],'ex20',r['excess_20d_pct'])
def grp(f,l):
    g=[r for r in rows if f(r) and r['ret_20d_pct'] is not None]
    if not g: return
    print(f"{l}: n={len(g)} mean1d={st.mean(r['ret_1d_pct'] for r in g):.1f} mean5d={st.mean(r['ret_5d_pct'] for r in g):.1f} meandrift={st.mean(r['drift_day1_to_day20_pct'] for r in g):.1f} meanEx1d={st.mean(r['excess_1d_pct'] for r in g):.1f} meanEx20={st.mean(r['excess_20d_pct'] for r in g):.1f} median1d={st.median(r['ret_1d_pct'] for r in g):.1f}")
grp(lambda r:r['guidance_signal'] in('cut','withdraw'),'cut/withdraw')
grp(lambda r:r['guidance_signal'] in('raise','maintain','initial'),'raise/maintain/initial')
grp(lambda r:r['guidance_signal']=='quarterly','Hill quarterly-only')
grp(lambda r:r['guidance_signal']!='pre-tracker' and r['event']!='CEO news','all tracker events')
grp(lambda r:r['guidance_signal']!='other','all earnings since 2019')
grp(lambda r:r['ret_1d_pct'] is not None and r['ret_1d_pct']<=-5 and r['event']!='CEO news','1d <= -5%')
