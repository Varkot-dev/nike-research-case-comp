"""T3 Nike share of peer-set revenue by region (home currency, ECB FX); T2 inventory and gross margin vs peers."""
import csv, collections, statistics as st, json
B='/home/user/nike-research-case-comp/data/hunt/peers_reported'
exec(open(B+'/scripts/17_tests.py').read().split("P=list(")[0])  # reuse fx helpers
P=list(csv.DictReader(open(B+'/panel_region_quarterly.csv')))
lv=collections.defaultdict(float); have=set()
for r in P:
    lv[(r['company'],r['region_reported'],int(r['cal_year']),int(r['cal_q']))]=float(r['revenue_local']); have.add((r['company'],r['region_reported'],int(r['cal_year']),int(r['cal_q'])))
CUR={'nike':'USD','deckers':'USD','lululemon':'USD','vf':'USD','underarmour':'USD','skechers':'USD','crocs':'USD','columbia':'USD','amer':'USD','on':'CHF','adidas':'EUR','puma':'EUR','asics':'JPY'}
SETS={
 'North America':dict(home='USD',start=(2019,1),members=[('nike',['North America']),('adidas',['North America']),('puma',['Americas']),('asics',['North America']),('underarmour',['North America']),
     ('columbia',['US']),('deckers',['US','US (domestic)']),('on',['Americas','North America'])]),
 'North America (2023Q2+ incl. Amer, Crocs)':dict(home='USD',start=(2023,2),members=[('nike',['North America']),('adidas',['North America']),('puma',['Americas']),('asics',['North America']),('underarmour',['North America']),
     ('columbia',['US']),('deckers',['US','US (domestic)']),('lululemon',['US','Canada']),('on',['Americas','North America']),('amer',['Americas']),('crocs',['Crocs North America'])]),
 'Europe/EMEA':dict(home='EUR',start=(2019,1),members=[('nike',['EMEA']),('adidas',['Europe','EMEA']),('puma',['EMEA']),('asics',['EMEA']),('underarmour',['EMEA']),('columbia',['EMEA']),('on',['EMEA','EMEA (Europe pre-2023)'])]),
 'Greater China':dict(home='CNY',start=(2019,1),members=[('nike',['Greater China']),('adidas',['Greater China']),('asics',['Greater China'])]),
 'Greater China (2023Q2+ incl. Amer, Lululemon)':dict(home='CNY',start=(2023,2),members=[('nike',['Greater China']),('adidas',['Greater China']),('asics',['Greater China']),('amer',['Greater China']),('lululemon',['China Mainland'])]),
}
QS=[(y,q) for y in range(2019,2027) for q in range(1,5) if (y,q)<=(2026,2)]
rows=[]
for name,S in SETS.items():
    for (y,q) in QS:
        if (y,q)<S['start']: continue
        tot=0; nike=None; missing=[]
        for co,regs in S['members']:
            # adidas Europe vs EMEA naming: take whichever exists, not both
            v=None
            for rg in regs:
                if (co,rg,y,q) in have:
                    v=(v or 0)+lv[(co,rg,y,q)]
                    if co=='adidas': break
            if v is None:
                if co=='on' and y<2022: v=0.0  # On pre-IPO regional data not available; small base
                else: missing.append(co); continue
            c=conv(v,CUR[co],S['home'],y,q)
            if c is None: missing.append(co); continue
            tot+=c
            if co=='nike': nike=c
        if nike is None or missing: rows.append(dict(set=name,cal_year=y,cal_q=q,nike_share_pct=None,missing=';'.join(missing))); continue
        rows.append(dict(set=name,cal_year=y,cal_q=q,nike_share_pct=round(100*nike/tot,2),peer_total_home_ccy_m=round(tot-nike,1),nike_home_ccy_m=round(nike,1),missing=''))
ix={(r['set'],r['cal_year'],r['cal_q']):r for r in rows}
for r in rows:
    p=ix.get((r['set'],r['cal_year']-1,r['cal_q']))
    r['share_change_yoy_pp']=round(r['nike_share_pct']-p['nike_share_pct'],2) if (p and p.get('nike_share_pct') is not None and r['nike_share_pct'] is not None) else None
F=['set','cal_year','cal_q','nike_share_pct','share_change_yoy_pp','nike_home_ccy_m','peer_total_home_ccy_m','missing']
with open(B+'/test_T3_nike_share_by_region.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=F); w.writeheader(); [w.writerow({k:r.get(k) for k in F}) for r in rows]
print('T3 Nike share of peer-set revenue (home ccy) and yoy change')
summ={}
for name in SETS:
    rs=[r for r in rows if r['set']==name]
    print(name); 
    for r in rs[-10:]: print('   ',r['cal_year'],r['cal_q'],r['nike_share_pct'],r['share_change_yoy_pp'],r['missing'])
    g={(r['cal_year'],r['cal_q']):r['share_change_yoy_pp'] for r in rs}
    l2=[g.get(k) for k in [(2026,1),(2026,2)]]; p4=[g.get(k) for k in [(2025,1),(2025,2),(2025,3),(2025,4)]]
    summ[name]=dict(last2=l2,prev4=p4,mean_last2=round(st.mean([x for x in l2 if x is not None]),2) if any(x is not None for x in l2) else None,mean_prev4=round(st.mean([x for x in p4 if x is not None]),2) if any(x is not None for x in p4) else None,
        share_2019Q2=ix.get((name,2019,2),{}).get('nike_share_pct'),share_latest=ix.get((name,2026,2),{}).get('nike_share_pct'))
    print('  ',summ[name])
json.dump(summ,open(B+'/test_T3_summary.json','w'),indent=1)
# ---- T2 inventory and GM
C=list(csv.DictReader(open(B+'/panel_company_quarterly.csv')))
cix={(r['company'],int(r['cal_year']),int(r['cal_q'])):r for r in C}
print('\nT2 inventory growth minus sales growth (pp), GM yoy (bps)')
t2=[]
for co in sorted({r['company'] for r in C}):
    for (y,q) in [(2025,3),(2025,4),(2026,1),(2026,2),(2026,3)]:
        r=cix.get((co,y,q))
        if r: t2.append(dict(company=co,cal_year=y,cal_q=q,revenue_yoy_pct=r['revenue_yoy_pct'],inventory_yoy_pct=r['inventory_yoy_pct'],inv_minus_sales_pp=r['inv_minus_sales_pp'],gross_margin_pct=r['gross_margin_pct'],gm_yoy_bps=r['gm_yoy_bps']))
with open(B+'/test_T2_inventory_gm_latest.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(t2[0])); w.writeheader(); w.writerows(t2)
def latest2(co):
    rs=[r for r in t2 if r['company']==co and r['inv_minus_sales_pp'] not in ('',None)]
    return rs[-2:]
peers=[]; 
for co in sorted({r['company'] for r in t2}):
    l=latest2(co)
    if not l: continue
    m=st.mean(float(x['inv_minus_sales_pp']) for x in l); iy=st.mean(float(x['inventory_yoy_pct']) for x in l)
    print(f"  {co:12s} quarters={[ (x['cal_year'],x['cal_q']) for x in l]} inv_minus_sales_mean={m:6.2f} inv_yoy_mean={iy:6.2f}")
    if co!='nike': peers.append((co,m,iy))
pm=st.median(p[1] for p in peers); print('  peer median inv-minus-sales',round(pm,2),' peers with gap>5pp:',[p[0] for p in peers if p[1]>5])
json.dump(dict(peer_median_inv_minus_sales=pm,peers=peers),open(B+'/test_T2_summary.json','w'),indent=1)
