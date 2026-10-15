"""Tests on the peer panel.
T1 regional growth gap (Nike minus peer median), latest two calendar quarters with peer data (2026Q1-Q2) vs the four before (2025Q1-Q4).
T2 inventory cleanliness: inventory growth minus sales growth, and gross-margin change, Nike vs peers.
T3 Nike share of combined peer-set revenue in USD, by region; yoy change in share.
T4 China: Nike Greater China vs foreign peers in China and domestic brands' retail sell-through.
Growth basis: constant currency where the company prints it; otherwise reported growth translated into the region's home
currency with ECB monthly averages (USD for North America, EUR for Europe/EMEA, CNY for Greater China)."""
import csv, collections, statistics as st, json
B='/home/user/nike-research-case-comp/data/hunt/peers_reported'
# FX: quarterly average units per EUR
fxm=collections.defaultdict(dict)
for r in csv.DictReader(open(B+'/raw/fx/ecb_monthly_eur_rates.csv')):
    y,m=int(r['TIME_PERIOD'][:4]),int(r['TIME_PERIOD'][5:7]); fxm[r['CURRENCY']][(y,(m-1)//3+1,m)]=float(r['OBS_VALUE'])
def fxq(cur,y,q):
    if cur=='EUR': return 1.0
    v=[val for (yy,qq,m),val in fxm[cur].items() if yy==y and qq==q]
    return sum(v)/len(v) if v else None
def conv(val,cur,home,y,q):
    a,b=fxq(cur,y,q),fxq(home,y,q)
    return None if (a is None or b is None) else val/a*b
P=list(csv.DictReader(open(B+'/panel_region_quarterly.csv')))
lv={(r['company'],r['region_reported'],int(r['cal_year']),int(r['cal_q'])):r for r in P}
HOME={'North America':'USD','Europe/EMEA':'EUR','Greater China':'CNY'}
SERIES={ # region -> list of (label, company, region_reported)
 'North America':[('Nike NA','nike','North America'),('adidas NA','adidas','North America'),('Puma Americas','puma','Americas'),('ASICS NA','asics','North America'),('On Americas','on','Americas'),
    ('Lululemon Americas','lululemon','Americas'),('Under Armour NA','underarmour','North America'),('Deckers US','deckers','US'),('Amer Americas','amer','Americas'),('Columbia US','columbia','US'),
    ('Crocs brand NA','crocs','Crocs North America'),('Skechers Americas','skechers','Americas')],
 'Europe/EMEA':[('Nike EMEA','nike','EMEA'),('adidas Europe','adidas','Europe'),('Puma EMEA','puma','EMEA'),('ASICS EMEA','asics','EMEA'),('On EMEA','on','EMEA'),('Under Armour EMEA','underarmour','EMEA'),
    ('Amer EMEA','amer','EMEA'),('Columbia EMEA','columbia','EMEA'),('Skechers EMEA','skechers','EMEA')],
 'Greater China':[('Nike Greater China','nike','Greater China'),('adidas Greater China','adidas','Greater China'),('ASICS Greater China','asics','Greater China'),('Lululemon China Mainland','lululemon','China Mainland'),
    ('Amer Greater China','amer','Greater China'),('Skechers China','skechers','China')]}
def growth(co,reg,y,q,home):
    r=lv.get((co,reg,y,q))
    if not r: return None,None
    if r['yoy_cc_pct'] not in ('',None): return float(r['yoy_cc_pct']),'cc'
    p=lv.get((co,reg,y-1,q))
    if co=='asics' and y>=2025:
        # use same-vintage prior (already in yoy_reported) translated
        if r['yoy_reported_pct'] in ('',None): return None,None
        g=float(r['yoy_reported_pct']); a=fxq('JPY',y,q)/fxq(home,y,q); b=fxq('JPY',y-1,q)/fxq(home,y-1,q)
        return round(((1+g/100)*b/a-1)*100,2),'fx-translated'
    if not p: return (float(r['yoy_reported_pct']) if r['yoy_reported_pct'] else None),'reported'
    if r['currency']==home: return round((float(r['revenue_local'])/float(p['revenue_local'])-1)*100,2),'reported(home ccy)'
    c=conv(float(r['revenue_local']),r['currency'],home,y,q); pc=conv(float(p['revenue_local']),r['currency'],home,y-1,q)
    if c is None or pc is None: return None,None
    return round((c/pc-1)*100,2),'fx-translated'
# Vans (growth only)
vans={(int(r['cal_year']),int(r['cal_q']),r['region']):r for r in csv.DictReader(open(B+'/vf_vans_regional_growth.csv'))}
VMAP={'North America':'Americas','Europe/EMEA':'EMEA'}
QS=[(y,q) for y in range(2019,2027) for q in range(1,5) if (y,q)<=(2026,3)]
out=[]
for reg,ser in SERIES.items():
    for (y,q) in QS:
        for lab,co,rr in ser:
            g,b=growth(co,rr,y,q,HOME[reg])
            if g is not None: out.append(dict(region=reg,cal_year=y,cal_q=q,series=lab,is_nike=int(co=='nike'),growth_pct=g,basis=b))
        if reg in VMAP:
            v=vans.get((y,q,VMAP[reg]))
            if v and v['yoy_cc_pct']: out.append(dict(region=reg,cal_year=y,cal_q=q,series='Vans '+VMAP[reg],is_nike=0,growth_pct=float(v['yoy_cc_pct']),basis='cc'))
# China domestic retail sell-through (separate group)
for r in csv.DictReader(open(B+'/china_peers_sellthrough_quarterly.csv')):
    if r['metric']=='retail_sellthrough_yoy_pct' and r['series'] in ('ANTA brand','FILA brand','Li Ning overall platform','Xtep core brand'):
        out.append(dict(region='Greater China (domestic sell-through)',cal_year=int(r['cal_year']),cal_q=int(r['cal_q']),series=r['series'],is_nike=0,growth_pct=float(r['value']),basis='retail sell-through, range midpoint'))
with open(B+'/panel_growth_comparable.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
# gap table
gap=[]
G=collections.defaultdict(list)
for r in out: G[(r['region'],r['cal_year'],r['cal_q'])].append(r)
for (reg,y,q),rs in sorted(G.items()):
    if reg.startswith('Greater China ('): continue
    n=[r['growth_pct'] for r in rs if r['is_nike']]; p=[r['growth_pct'] for r in rs if not r['is_nike']]
    dom=[r['growth_pct'] for r in G.get(('Greater China (domestic sell-through)',y,q),[])] if reg=='Greater China' else []
    if not n or len(p)<3: continue
    gap.append(dict(region=reg,cal_year=y,cal_q=q,nike=n[0],peer_median=st.median(p),peer_mean=round(st.mean(p),2),n_peers=len(p),gap_vs_median=round(n[0]-st.median(p),2),share_of_peers_beating_nike=round(sum(x>n[0] for x in p)/len(p),2),
        domestic_median=(st.median(dom) if dom else None),gap_vs_domestic=(round(n[0]-st.median(dom),2) if dom else None)))
with open(B+'/test_gap_by_region_quarter.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(gap[0])); w.writeheader(); w.writerows(gap)
print('T1 gap Nike minus peer median (pp)')
res={}
for reg in SERIES:
    g={(r['cal_year'],r['cal_q']):r for r in gap if r['region']==reg}
    last2=[g[k]['gap_vs_median'] for k in [(2026,1),(2026,2)] if k in g]; prev4=[g[k]['gap_vs_median'] for k in [(2025,1),(2025,2),(2025,3),(2025,4)] if k in g]
    prev8=[g[k]['gap_vs_median'] for k in [(2024,1),(2024,2),(2024,3),(2024,4)] if k in g]
    res[reg]=dict(last2=last2,prev4=prev4,prev_2024=prev8,mean_last2=round(st.mean(last2),2),mean_prev4=round(st.mean(prev4),2),mean_2024=round(st.mean(prev8),2) if prev8 else None)
    print(reg,res[reg])
    for k in sorted(g)[-10:]: print('   ',k,g[k]['nike'],g[k]['peer_median'],g[k]['gap_vs_median'],g[k]['n_peers'],g[k]['share_of_peers_beating_nike'],g[k]['domestic_median'])
json.dump(res,open(B+'/test_T1_summary.json','w'),indent=1)
