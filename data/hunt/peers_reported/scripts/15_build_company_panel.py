"""Company-level quarterly panel: revenue, gross margin, inventory (local currency), with yoy changes.
SEC filers from XBRL instances (undimensioned facts); adidas/Puma/On from releases; ASICS from fact sheet + tanshin."""
import csv, re, glob, datetime as dt, collections
B='/home/user/nike-research-case-comp/data/hunt/peers_reported'
D=dt.date.fromisoformat
def calq(s,e):
    m=D(s)+(D(e)-D(s))/2; return m.year,(m.month-1)//3+1
REV=('Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','RevenueFromContractsWithCustomers','Revenue','SalesRevenueNet')
COGS=('CostOfRevenue','CostOfGoodsAndServicesSold','CostOfSales')
INV=('InventoryNet','Inventories','InventoryFinishedGoodsNetOfReserves')
f=collections.defaultdict(dict)
for r in csv.DictReader(open(B+'/raw/sec_xbrl_dimensional_facts.csv')):
    if r['dims']: continue
    co=r['company']; t=r['tag']; key=None
    if t in REV: key='rev'
    elif t=='GrossProfit': key='gp'
    elif t in COGS: key='cogs'
    elif t in INV: key='inv'
    else: continue
    k=(r['start'],r['end'])
    prev=f[(co,key)].get(k)
    if prev is None or r['report_date']>prev[1]: f[(co,key)][k]=(float(r['value']),r['report_date'])
def quarters(d):
    q={}; y={}
    for (s,e),(v,_) in d.items():
        if not s: continue
        n=(D(e)-D(s)).days
        if 80<=n<=100: q[e]=(s,v)
        else: y[(s,e)]=v
    for (s,e),v in y.items():
        if e in q: continue
        pr=[(e2,v2) for (s2,e2),v2 in y.items() if s2==s and 75<=(D(e)-D(e2)).days<=105]
        if pr: e2,v2=max(pr); q[e]=(str(D(e2)+dt.timedelta(days=1)),v-v2)
        else:
            pq=[e2 for e2 in q if q[e2][0]==s and 75<=(D(e)-D(e2)).days<=105]
            if pq and 170<=(D(e)-D(s)).days<=190: q[e]=(str(D(pq[0])+dt.timedelta(days=1)),v-q[pq[0]][1])
    return q
out=[]
for co in sorted({c for c,_ in f}):
    rv=quarters(f[(co,'rev')]); gp=quarters(f[(co,'gp')]); cg=quarters(f[(co,'cogs')])
    inv={e:v for (s,e),(v,_) in f[(co,'inv')].items() if not s}
    for e,(s,v) in rv.items():
        g=gp.get(e,(None,None))[1]
        if g is None and e in cg: g=v-cg[e][1]
        y,q=calq(s,e)
        out.append(dict(company=co,cal_year=y,cal_q=q,period_end=e,currency='USD' if co not in ('on','birkenstock') else ('CHF' if co=='on' else 'EUR'),revenue=v/1e6,gross_profit=(g/1e6 if g is not None else None),inventory=(inv[e]/1e6 if e in inv else None),source='SEC XBRL instance'))
# adidas / puma
def qd(y,q): return str(dt.date(y+(q==4),(3*q)%12+1,1)-dt.timedelta(days=1))
for co in ('adidas','puma'):
    d=collections.defaultdict(dict)
    for r in csv.DictReader(open(f'{B}/{co}_quarterly_extract.csv')):
        if r['region']!='Total': continue
        y,q=int(r['year']),int(r['quarter'])
        d[(y,q)].setdefault(r['metric'],float(r['value']))
        if r['prior']: d[(y-1,q)].setdefault(r['metric']+'_p',float(r['prior']))
    for (y,q),m in d.items():
        rev=m.get('net_sales',m.get('net_sales_p')); gp=m.get('gross_profit',m.get('gross_profit_p')); iv=m.get('inventory',m.get('inventory_p'))
        if rev is None: continue
        if q==4 and all((y,k) in d for k in (1,2,3)):
            q3=d[(y,3)].get('net_sales',d[(y,3)].get('net_sales_p')) or 0
            if rev>2.2*q3:
                parts=[d[(y,k)] for k in (1,2,3)]
                rev=rev-sum(p.get('net_sales',p.get('net_sales_p')) for p in parts)
                gp=gp-sum(p.get('gross_profit',p.get('gross_profit_p')) for p in parts) if gp else None
        out.append(dict(company=co,cal_year=y,cal_q=q,period_end=qd(y,q),currency='EUR',revenue=rev,gross_profit=gp,inventory=iv,source='company release'))
# adidas Q3 2025 from narrative (no table in that release); inventory and GM printed in text
out.append(dict(company='adidas',cal_year=2025,cal_q=3,period_end='2025-09-30',currency='EUR',revenue=6630.0,gross_profit=round(6630.0*0.518,1),inventory=5471.0,source='adidas Q3 2025 release narrative: sales EUR 6.6bn (rounded), GM 51.8%, inventories EUR 5,471m'))
# On
o=collections.defaultdict(dict)
for r in csv.DictReader(open(B+'/on_quarterly_extract.csv')):
    if r['region']=='Total': o[(int(r['year']),int(r['quarter']))][r['metric']]=float(r['value'])
for (y,q),m in o.items():
    rev=m.get('net_sales'); 
    if q==4 and all((y,k) in o for k in (1,2,3)) and rev: rev=rev-sum(o[(y,k)]['net_sales'] for k in (1,2,3))
    gm=m.get('gross_margin_pct') if q!=4 else None
    if not any(x['company']=='on' and x['period_end']==qd(y,q) for x in out):
        out.append(dict(company='on',cal_year=y,cal_q=q,period_end=qd(y,q),currency='CHF',revenue=rev,gross_profit=(rev*gm/100 if (rev and gm) else None),inventory=m.get('inventory'),source='6-K release'))
# ASICS: fact sheet 2023-24 + tanshin YTD 2025-26
for r in csv.DictReader(open(B+'/asics_quarterly_extract.csv')):
    pass
A=collections.defaultdict(dict)
for r in csv.DictReader(open(B+'/asics_quarterly_extract.csv')):
    if r['region']=='Total' and r['metric'] in ('net_sales','gross_profit'): A[(int(r['year']),int(r['quarter']))].setdefault(r['metric'],float(r['value']))
T=B+'/raw/asics_text'; ytd={}
for fn,(y,n) in {'asics_4009.txt':(2025,1),'asics_4047.txt':(2025,2),'asics_4068.txt':(2025,3),'asics_4124.txt':(2025,4),'asics_4158.txt':(2026,1),'asics_4215.txt':(2026,2)}.items():
    t=open(f'{T}/{fn}',errors='ignore').read()
    ns=re.search(r'^\s*Net sales\s+([\d,]+)\s+([\d,]+)\s',t,re.M); gp=re.search(r'^\s*Gross profit\s+([\d,]+)\s+([\d,]+)\s',t,re.M); iv=re.search(r'Merchandise and finished goods\s+([\d,]+)\s+([\d,]+)',t)
    g=lambda m,i: float(m.group(i).replace(',',''))
    ytd[(y,n)]=dict(ns=g(ns,2),gp=g(gp,2),inv=g(iv,2))
ASICS_INV={(2023,4):118411,(2024,4):133922}
for (y,n),v in ytd.items():
    p=ytd.get((y,n-1)) if n>1 else None
    ns=v['ns']-(p['ns'] if p else 0); gp=v['gp']-(p['gp'] if p else 0)
    A[(y,n)].update(net_sales=ns,gross_profit=gp,inventory=v['inv'])
A[(2024,4)]['inventory']=133922; A[(2023,4)]['inventory']=118411
for (y,q),m in A.items():
    if 'net_sales' not in m: continue
    out.append(dict(company='asics',cal_year=y,cal_q=q,period_end=qd(y,q),currency='JPY',revenue=m['net_sales'],gross_profit=m.get('gross_profit'),inventory=m.get('inventory'),source='ASICS fact sheet / tanshin'))
# post-fix: Q4 rows that hold full-year values (adidas FY releases) -> Q4 = FY - Q1..Q3
_ix={(r['company'],r['cal_year'],r['cal_q']):r for r in out}
for r in out:
    if r['cal_q']==4 and r['company'] in ('adidas','puma'):
        parts=[_ix.get((r['company'],r['cal_year'],k)) for k in (1,2,3)]
        if all(parts) and r['revenue']>2.2*parts[2]['revenue']:
            r['revenue']-=sum(p['revenue'] for p in parts)
            r['gross_profit']=(r['gross_profit']-sum(p['gross_profit'] for p in parts)) if r['gross_profit'] and all(p['gross_profit'] for p in parts) else None
            r['source']+=' (Q4 = FY minus Q1-Q3)'
# derived metrics
out.sort(key=lambda r:(r['company'],r['cal_year'],r['cal_q']))
ix={(r['company'],r['cal_year'],r['cal_q']):r for r in out}
for r in out:
    r['gross_margin_pct']=round(100*r['gross_profit']/r['revenue'],2) if (r['gross_profit'] and r['revenue']) else None
for r in out:
    p=ix.get((r['company'],r['cal_year']-1,r['cal_q']))
    r['revenue_yoy_pct']=round(100*(r['revenue']/p['revenue']-1),2) if p and p['revenue'] and r['revenue'] else None
    r['inventory_yoy_pct']=round(100*(r['inventory']/p['inventory']-1),2) if p and p.get('inventory') and r['inventory'] else None
    r['gm_yoy_bps']=round(100*(r['gross_margin_pct']-p['gross_margin_pct'])) if p and p.get('gross_margin_pct') is not None and r['gross_margin_pct'] is not None else None
    r['inv_minus_sales_pp']=round(r['inventory_yoy_pct']-r['revenue_yoy_pct'],2) if (r['inventory_yoy_pct'] is not None and r['revenue_yoy_pct'] is not None) else None
F=['company','cal_year','cal_q','period_end','currency','revenue','gross_profit','gross_margin_pct','inventory','revenue_yoy_pct','inventory_yoy_pct','inv_minus_sales_pp','gm_yoy_bps','source']
with open(B+'/panel_company_quarterly.csv','w',newline='') as fo:
    w=csv.DictWriter(fo,fieldnames=F); w.writeheader(); [w.writerow({k:r.get(k) for k in F}) for r in out if r['cal_year']>=2018]
for r in out:
    if r['cal_year']*10+r['cal_q']>=20253: print(r['company'],r['cal_year'],r['cal_q'],r['revenue_yoy_pct'],r['gross_margin_pct'],r['gm_yoy_bps'],r['inventory_yoy_pct'],r['inv_minus_sales_pp'])
