"""Harmonise all sources into tidy panels:
  panel_region_quarterly.csv : company, region_reported, region_std, cal_year, cal_q, period_start, period_end, currency, revenue_local, yoy_reported_pct, yoy_cc_pct, source_type
  panel_company_quarterly.csv: company, cal_year, cal_q, period_end, revenue_local, gross_margin_pct, inventory_local, revenue_yoy_pct, inventory_yoy_pct, gm_yoy_bps, inv_minus_sales_pp
Calendar quarter = quarter containing the fiscal period's midpoint (Nike Jun-Aug -> CQ3; Lululemon May-Jul -> CQ2)."""
import csv, datetime as dt, collections, re
B='/home/user/nike-research-case-comp/data/hunt/peers_reported'
D=dt.date.fromisoformat
def calq(s,e):
    m=D(s)+(D(e)-D(s))/2; return m.year,(m.month-1)//3+1
def qdates(y,q):
    st=dt.date(y,3*q-2,1); en=(dt.date(y+(q==4),(3*q)%12+1,1)-dt.timedelta(days=1)); return str(st),str(en)
STD={ # region_reported -> standard bucket
 'North America':'North America','Americas':'North America','US':'North America','US (domestic)':'North America','Active Americas':'North America','Crocs North America':'North America',
 'EMEA':'Europe/EMEA','Europe':'Europe/EMEA','Active Europe':'Europe/EMEA','EMEA (Europe pre-2023)':'Europe/EMEA',
 'Greater China':'Greater China','China Mainland':'Greater China','China':'Greater China',
 'APLA':'Asia-Pac/LatAm/Other','Asia-Pacific':'Asia-Pac/LatAm/Other','Asia/Pacific':'Asia-Pac/LatAm/Other','Latin America':'Asia-Pac/LatAm/Other','Japan/South Korea':'Asia-Pac/LatAm/Other','Emerging Markets':'Asia-Pac/LatAm/Other','Active Asia-Pacific':'Asia-Pac/LatAm/Other','Asia-Pacific ex China':'Asia-Pac/LatAm/Other','Rest of World':'Asia-Pac/LatAm/Other','Japan':'Japan','Oceania':'Asia-Pac/LatAm/Other','Southeast and South Asia':'Asia-Pac/LatAm/Other','Others':'Asia-Pac/LatAm/Other','International':'International (non-US)',
 'Total':'Total','HOKA':'Brand: HOKA','UGG':'Brand: UGG','Converse':'Brand: Converse','Active':'Segment: VF Active','HEYDUDE':'Brand: HEYDUDE','Crocs International':'International (non-US)','Canada':'North America (Canada)','LAAP':'Asia-Pac/LatAm/Other','Asia-Pacific':'Asia-Pac/LatAm/Other'}
CUR={'nike':'USD','deckers':'USD','lululemon':'USD','vf':'USD','underarmour':'USD','skechers':'USD','crocs':'USD','columbia':'USD','amer':'USD','on':'CHF','birkenstock':'EUR','adidas':'EUR','puma':'EUR','asics':'JPY'}
rows=[]
# 1 SEC regional
for r in csv.DictReader(open(B+'/sec_regional_quarterly.csv')):
    y,q=calq(r['period_start'],r['period_end'])
    rows.append(dict(company=r['company'],region_reported=r['region'],cal_year=y,cal_q=q,period_start=r['period_start'],period_end=r['period_end'],currency=CUR[r['company']],revenue_local=float(r['revenue'])/1e6,yoy_reported_pct=None,yoy_cc_pct=None,source_type='SEC XBRL '+r['how']))
# 2 adidas / puma (levels from current column; prior column fills gaps)
for co in ('adidas','puma'):
    have=set()
    ext=list(csv.DictReader(open(f'{B}/{co}_quarterly_extract.csv')))
    for r in ext:
        if r['metric'] not in ('net_sales_region','net_sales'): continue
        reg=r['region']; y,q=int(r['year']),int(r['quarter'])
        if (reg,y,q) in have: continue
        have.add((reg,y,q)); s,e=qdates(y,q)
        rows.append(dict(company=co,region_reported=reg,cal_year=y,cal_q=q,period_start=s,period_end=e,currency='EUR',revenue_local=float(r['value']),yoy_reported_pct=float(r['yoy_reported_pct']) if r['yoy_reported_pct'] else None,yoy_cc_pct=float(r['yoy_cn_pct']) if r['yoy_cn_pct'] else None,source_type='release '+r['source']))
    for r in ext:
        if r['metric'] not in ('net_sales_region','net_sales') or not r['prior']: continue
        reg=r['region']; y,q=int(r['year'])-1,int(r['quarter'])
        if (reg,y,q) in have: continue
        have.add((reg,y,q)); s,e=qdates(y,q)
        rows.append(dict(company=co,region_reported=reg,cal_year=y,cal_q=q,period_start=s,period_end=e,currency='EUR',revenue_local=float(r['prior']),yoy_reported_pct=None,yoy_cc_pct=None,source_type='release prior-year column '+r['source']))
# adidas Q3 2025: release has no regional table (image); levels and adidas-brand cc growth (ex-Yeezy base) from press coverage (search snippets, worldfootwear / retail-insight-network)
for reg,v,cc in [('Europe',2320.0,12.0),('North America',1290.0,8.0),('Greater China',947.0,10.0)]:
    rows.append(dict(company='adidas',region_reported=reg,cal_year=2025,cal_q=3,period_start='2025-07-01',period_end='2025-09-30',currency='EUR',revenue_local=v,yoy_reported_pct=None,yoy_cc_pct=cc,source_type='press coverage SNIPPET (adidas brand cc, ex-Yeezy prior-year base)'))
# 3 ASICS
seen=set()
for r in csv.DictReader(open(B+'/asics_quarterly_extract.csv')):
    if r['metric'] not in ('net_sales_region','net_sales'): continue
    k=(r['region'],r['year'],r['quarter'])
    if k in seen: continue
    seen.add(k); y,q=int(r['year']),int(r['quarter']); s,e=qdates(y,q)
    rows.append(dict(company='asics',region_reported=r['region'],cal_year=y,cal_q=q,period_start=s,period_end=e,currency='JPY',revenue_local=float(r['value']),yoy_reported_pct=None,yoy_cc_pct=None,source_type='IR '+r['source']))
# ASICS prior-restated for yoy of 2025-26 kept separately
asics_prior={(r['region'],int(r['year']),int(r['quarter'])):float(r['value']) for r in csv.DictReader(open(B+'/asics_quarterly_extract.csv')) if r['metric']=='net_sales_region_prior_restated'}
# 4 On: quarters; Q4 rows in releases are FY -> derive
on=[r for r in csv.DictReader(open(B+'/on_quarterly_extract.csv')) if r['metric'] in ('net_sales_region','net_sales')]
onv={(r['region'],int(r['year']),int(r['quarter'])):r for r in on}
for (reg,y,q),r in onv.items():
    v=float(r['value']); cc=float(r['yoy_cn_pct']) if r['yoy_cn_pct'] else None; g=float(r['yoy_reported_pct'])
    if q==4:
        parts=[onv.get((reg,y,k)) for k in (1,2,3)]
        if not all(parts): continue
        v=v-sum(float(p['value']) for p in parts); cc=None; g=None
    s,e=qdates(y,q)
    rows.append(dict(company='on',region_reported=reg,cal_year=y,cal_q=q,period_start=s,period_end=e,currency='CHF',revenue_local=v,yoy_reported_pct=g,yoy_cc_pct=cc,source_type='6-K release'+(' (Q4=FY-9M)' if q==4 else '')))
# 5 Deckers release HOKA etc. (only where XBRL missing)
xb={(r['company'],r['region_reported'],r['period_end']) for r in rows}
for r in csv.DictReader(open(B+'/deckers_release_extract.csv')):
    reg=r['segment']
    if reg in ('DTC','Wholesale'): continue
    e=r['period_end']; s=str(D(e)-dt.timedelta(days=91))
    if ('deckers',reg,e) in xb or ('deckers','US' if reg=='US (domestic)' else reg,e) in xb: continue
    if float(r['value'])>2*float(r['prior'])+1e9: continue
    if e.endswith('03-31') and float(r['value'])>1500 and reg=='HOKA': continue  # FY figure captured, skip
    y,q=calq(s,e)
    rows.append(dict(company='deckers',region_reported=reg,cal_year=y,cal_q=q,period_start=s,period_end=e,currency='USD',revenue_local=float(r['value']),yoy_reported_pct=float(r['yoy_reported_pct']),yoy_cc_pct=None,source_type='8-K release'))
# reported yoy from levels where missing
idx={(r['company'],r['region_reported'],r['cal_year'],r['cal_q']):r for r in rows}
for r in rows:
    r['region_std']=STD.get(r['region_reported'],r['region_reported'])
    if r['yoy_reported_pct'] is None:
        p=idx.get((r['company'],r['region_reported'],r['cal_year']-1,r['cal_q']))
        if r['company']=='asics' and r['cal_year']>=2025: 
            pv=asics_prior.get((r['region_reported'],r['cal_year']-1,r['cal_q']))
            if pv: r['yoy_reported_pct']=round((r['revenue_local']/pv-1)*100,2); r['source_type']+=' ; yoy vs same-vintage restated prior'
        elif p and p['revenue_local']:
            r['yoy_reported_pct']=round((r['revenue_local']/p['revenue_local']-1)*100,2)
# Nike constant-currency growth from repo filing facts
NMAP={'growth_north_america_cn_pct':'North America','growth_emea_cn_pct':'EMEA','growth_greater_china_cn_pct':'Greater China','growth_apla_cn_pct':'APLA','growth_revenues_cn_pct':'Total','growth_converse_cn_pct':'Converse'}
FQEND={1:'08-31',2:'11-30',3:'02-28',4:'05-31'}
try:
    for f in csv.DictReader(open('/home/user/nike-research-case-comp/data/nike_filing_facts.csv')):
        if f['metric'] in NMAP and re.match(r'Q\dFY\d{4}$',f['period']):
            q=int(f['period'][1]); fy=int(f['period'][4:]); y=fy-1 if q in (1,2) else fy
            e=f'{y}-{FQEND[q]}'
            for r in rows:
                if r['company']=='nike' and r['region_reported']==NMAP[f['metric']] and r['period_end'][:7]==e[:7]:
                    r['yoy_cc_pct']=float(f['value'])
except FileNotFoundError: pass
rows.sort(key=lambda r:(r['company'],r['region_reported'],r['cal_year'],r['cal_q']))
F=['company','region_reported','region_std','cal_year','cal_q','period_start','period_end','currency','revenue_local','yoy_reported_pct','yoy_cc_pct','source_type']
with open(B+'/panel_region_quarterly.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=F); w.writeheader(); [w.writerow({k:r[k] for k in F}) for r in rows]
c=collections.Counter((r['company']) for r in rows if r['cal_year']>=2019)
print(c)
