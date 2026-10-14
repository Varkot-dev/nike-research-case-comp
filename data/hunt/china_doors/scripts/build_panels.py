"""Build tidy CSVs for the China Nike-selling door hunt. Run from data/hunt/china_doors:  python3 -I scripts/build_panels.py
Inputs: ../stores/*.csv (HKEX-derived store counts already in repo, re-verified against raw text) and values read by hand from
HKEX/irasia PDFs listed in sources column. Outputs: partner_doors_halfyear.csv, domestic_doors_halfyear.csv, nike_owned_china_doors.csv,
rate_comparison.csv"""
import csv, collections, datetime as dt

# ---- 1. Partner retailers (Nike's two largest China partners). Half label H1 = Pou Sheng Jun / Topsports Aug; H2 = Pou Sheng Dec / Topsports Feb next year
ps = {'2022H1':(4455,'2022-06-30','20220811_2022081101178'),'2022H2':(4093,'2022-12-31','20230315_2023031501229'),
      '2023H1':(3723,'2023-06-30','20230811_2023081101150'),'2023H2':(3523,'2023-12-31','20240313_2024031300835'),
      '2024H1':(3478,'2024-06-30','20240812_2024081201066'),'2024H2':(3448,'2024-12-31','20250311_2025031100653'),
      '2025H1':(3408,'2025-06-30','20250811_2025081100594'),'2025H2':(3310,'2025-12-31','20260311_2026031100658'),
      '2026H1':(3110,'2026-06-30','20260812_2026081200368')}
ts = {'2022H1':(6928,'2022-08-31','20221025_2022102500674'),'2022H2':(6565,'2023-02-28','20230523_2023052300939'),
      '2023H1':(6209,'2023-08-31','20231018_2023101800750'),'2023H2':(6144,'2024-02-29','20240522_2024052201135'),
      '2024H1':(5813,'2024-08-31','20241023_2024102300853'),'2024H2':(5020,'2025-02-28','20250521_2025052101059'),
      '2025H1':(4688,'2025-08-31','20251022_2025102200838'),'2025H2':(4360,'2026-02-28','20260527_2026052701005')}
# Topsports May 2026 (Q1 FY26/27): only gross selling area is disclosed: -2.9% QoQ, -11.2% YoY (20260625_2026062500529).
# Doors estimate: area per store rose +3.9% in FY25/26 (annual report p.9); assume 0 to +3.9% per-store area growth over the quarter.
# stores_qoq = (1-0.029)/(1+g)-1  -> g=0: -2.9% ; g=+1%: -3.9%. Midpoint -3.4% on 4,360 = ~4,212 (range 4,190 to 4,235). ESTIMATE ONLY.
ts_est_2026Q1 = (round(4360*(1-0.034)), '2026-05-31 (estimate)')
per = sorted(ps)
rows=[]; prev_ps=prev_ts=None
for p in per:
    pv,pd,pdoc = ps[p]; tv,td,tdoc = ts.get(p,(None,None,None))
    rows.append(dict(period=p, pousheng_asof=pd, pousheng_doors=pv,
        pousheng_chg=(pv-prev_ps) if prev_ps else '', pousheng_chg_pct=round(100*(pv/prev_ps-1),1) if prev_ps else '',
        topsports_asof=td or '', topsports_doors=tv or '',
        topsports_chg=(tv-prev_ts) if (tv and prev_ts) else '', topsports_chg_pct=round(100*(tv/prev_ts-1),1) if (tv and prev_ts) else '',
        combined_doors=(pv+tv) if tv else '', hkex_docs=f'PS {pdoc}; TS {tdoc}'))
    prev_ps=pv; prev_ts=tv if tv else prev_ts
# combined change
for i,r in enumerate(rows):
    if i and r['combined_doors']!='' and rows[i-1]['combined_doors']!='':
        r['combined_chg_pct']=round(100*(r['combined_doors']/rows[i-1]['combined_doors']-1),1)
    else: r['combined_chg_pct']=''
rows[-1]['topsports_asof']='2026-05-31 (estimate from area; Aug 2026 not yet published, due 2026-10-28)'
rows[-1]['topsports_doors']=ts_est_2026Q1[0]
rows[-1]['combined_doors']=rows[-1]['pousheng_doors']+ts_est_2026Q1[0]
rows[-1]['topsports_chg']=ts_est_2026Q1[0]-4360; rows[-1]['topsports_chg_pct']=round(100*(ts_est_2026Q1[0]/4360-1),1)
rows[-1]['combined_chg_pct']=round(100*(rows[-1]['combined_doors']/rows[-2]['combined_doors']-1),1)
rows[-1]['hkex_docs']='PS 20260812_2026081200368; TS Q1 area 20260625_2026062500529 (estimate)'
flds=['period','pousheng_asof','pousheng_doors','pousheng_chg','pousheng_chg_pct','topsports_asof','topsports_doors','topsports_chg','topsports_chg_pct','combined_doors','combined_chg_pct','hkex_docs']
w=csv.DictWriter(open('partner_doors_halfyear.csv','w'),fieldnames=flds,extrasaction='ignore'); w.writeheader(); w.writerows(rows)

# ---- 2. Domestic brands. period uses same H1=Jun, H2=Dec labels
dom=[]
def add(brand,series): 
    for p,(v,src) in series.items(): dom.append(dict(brand=brand,period=p,doors=v,source=src))
add('ANTA (brand, Mainland+overseas)',{'2022H1':(6660,'ANTA interim 2022 20220823_2022082300202'),'2022H2':(6924,'ANTA results 20230321_2023032100283'),
 '2023H1':(6941,'20230822_2023082200404'),'2023H2':(7053,'20240827_2024082700407'),'2024H1':(7073,'20240827_2024082700407'),'2024H2':(7135,'20250319_2025031900218'),
 '2025H1':(7187,'20250827_2025082700307'),'2025H2':(7203,'20260325_2026032500245'),'2026H1':(7122,'20260826_2026082600213')})
add('ANTA KIDS',{'2022H1':(2563,'20220823_2022082300202'),'2022H2':(2679,'20230321_2023032100283'),'2023H1':(2692,'20230822_2023082200404'),'2023H2':(2778,'20240827_2024082700407'),
 '2024H1':(2831,'20240827_2024082700407'),'2024H2':(2784,'20250319_2025031900218'),'2025H1':(2722,'20250827_2025082700307'),'2025H2':(2652,'20260325_2026032500245'),'2026H1':(2560,'20260826_2026082600213')})
add('Li Ning core POS (China)',{'2022H1':(5937,'20220812_2022081200015'),'2022H2':(6295,'20230317_2023031700007'),'2023H1':(6167,'20230811_2023081100017'),'2023H2':(6240,'20240320_2024032000035'),
 '2024H1':(6239,'20240816_2024081600001'),'2024H2':(6117,'20250328_2025032800019'),'2025H1':(6099,'20250714_2025071400364'),'2025H2':(6091,'20260115_2026011500147'),'2026H1':(6063,'20260715_2026071500286')})
add('Xtep Adult',{'2022H2':(6313,'Xtep AR2023 p.19 (prior-year figure)'),'2023H1':(6443,'Xtep interim 2023 irasia int.pdf'),'2023H2':(6571,'Xtep AR2023'),'2024H1':(6578,'Xtep interim 2024'),
 '2024H2':(6382,'Xtep AR2024'),'2025H1':(6360,'Xtep interim 2025'),'2025H2':(6357,'Xtep AR2025 / interim 2026'),'2026H1':(6308,'Xtep interim 2026 (irasia int.pdf)')})
add('Xtep Kids / X Young',{'2022H2':(1520,'Xtep interim 2023 (31 Dec 2022 comparison)'),'2023H1':(1588,'Xtep interim 2023'),'2023H2':(1703,'Xtep interim 2024 comparison'),'2024H1':(1706,'Xtep interim 2024'),
 '2024H2':(1584,'Xtep interim 2025 comparison'),'2025H1':(1564,'Xtep interim 2025'),'2025H2':(1488,'Xtep interim 2026 comparison'),'2026H1':(1455,'Xtep interim 2026')})
add('361 core (Chinese mainland)',{'2022H2':(5480,'361 results 20230316_2023031600320'),'2023H1':(5642,'20230815_2023081500175'),'2023H2':(5734,'20240313_2024031300227'),'2024H1':(5740,'20240812_2024081200163'),
 '2024H2':(5750,'20250312_2025031200235'),'2025H1':(5669,'20250812_2025081200135'),'2025H2':(5394,'20260324_2026032400135'),'2026H1':(5076,'20260818_2026081800247')})
add('361 Kids (Chinese mainland POS)',{'2022H2':(2288,'20230316_2023031600320'),'2023H1':(2448,'20230815_2023081500175'),'2023H2':(2545,'20240313_2024031300227'),'2024H1':(2550,'20240812_2024081200163'),
 '2024H2':(2548,'20250312_2025031200235'),'2025H1':(2494,'20250812_2025081200135'),'2025H2':(2364,'20260324_2026032400135'),'2026H1':(2202,'20260818_2026081800247')})
add('Pou Sheng (Nike-heavy partner)',{p:(v[0],'HKEX '+v[2]) for p,v in ps.items()})
add('Topsports (Nike-heavy partner)',{p:(v[0],'HKEX '+v[2]) for p,v in ts.items()})
w=csv.DictWriter(open('domestic_doors_halfyear.csv','w'),fieldnames=['brand','period','doors','source']); w.writeheader(); w.writerows(dom)

# ---- 3. rate comparison: change over windows
d=collections.defaultdict(dict)
for r in dom: d[r['brand']][r['period']]=r['doors']
d['Topsports (Nike-heavy partner)']['2026H1']=ts_est_2026Q1[0]
d['Partners combined (PS+TS)']={p:ps[p][0]+ts[p][0] for p in ts}
d['Partners combined (PS+TS)']['2026H1']=ps['2026H1'][0]+ts_est_2026Q1[0]
out=[]
for b,s in d.items():
    for a,z,lab in [('2023H1','2026H1','Jun/Aug 2023 to Jun 2026 (3y)'),('2025H1','2026H1','Jun/Aug 2025 to Jun 2026 (1y)'),('2025H2','2026H1','last half-year')]:
        if a in s and z in s: out.append(dict(brand=b,window=lab,start=s[a],end=s[z],change_pct=round(100*(s[z]/s[a]-1),1)))
w=csv.DictWriter(open('rate_comparison.csv','w'),fieldnames=['brand','window','start','end','change_pct']); w.writeheader(); w.writerows(out)

# ---- 4. Nike-owned China mainland doors (locator; owned records are maintained weekly)
loc={r['id']:r for r in csv.DictReader(open('../stores/nike_locator_2026-10-14.csv'))}
ev=[e for e in csv.DictReader(open('../stores/nike_locator_store_events.csv')) if e['country']=='CN' and e['owner_type']=='NIKE_OWNED_STORE']
fut=[(r['id'],r['openingDate']) for r in loc.values() if r['iso2Country']=='CN' and r['facilityType']=='NIKE_OWNED_STORE' and r['openingDate']>'2026-10-14']
wk=collections.defaultdict(int)
for r in csv.DictReader(open('../stores/nike_locator_weekly_counts.csv')):
    if r['bucket']=='China mainland' and r['owner:type']=='NIKE_OWNED_STORE': wk[r['run_date']]+=int(r['n'])
res=[]
for dte,n in sorted(wk.items()):
    # stores listed on that date but with a future opening date (pre-listed). Only knowable for stores still listed today.
    pre=[i for i,o in fut if o>dte and any(e['ref']==i and e['first_seen']<=dte for e in ev)]
    res.append(dict(run_date=dte,listed=n,prelisted_future_opening=len(pre),operating_est=n-len(pre),
        window_note='source changed 2023-10..2024-10 (about 130 records; unusable)' if '2023-10'<=dte<'2025-01' else 'consistent static-JSON source'))
w=csv.DictWriter(open('nike_owned_china_doors.csv','w'),fieldnames=list(res[0])); w.writeheader(); w.writerows(res)
print('future-dated owned CN:',len(fut)); print(res[-1])
