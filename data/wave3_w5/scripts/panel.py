"""Quarterly panel on Nike fiscal quarters. python3 -I panel.py"""
import csv,os,json
D=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R=D+'/../hunt/peers_reported/china_peers_sellthrough_quarterly.csv'
pq=json.load(open('/tmp/w5_interim.json'))
bt={r['q']:r for r in csv.DictReader(open(D+'/backtest_pousheng_implied_vs_nike.csv'))}
dom={}
for r in csv.DictReader(open(R)):
    if r['metric']!='retail_sellthrough_yoy_pct': continue
    nm={'ANTA brand':'anta','FILA brand':'fila','Li Ning overall platform':'lining','Xtep core brand':'xtep'}.get(r['series'])
    if nm: dom[(nm,int(r['cal_year']),int(r['cal_q']))]=float(r['value'])
# 361 core (HKEX business updates, OPENED): Q1'26 +10, Q2'26 +6.5, Q3'26 +5
dom[('361',2026,1)]=10.0;dom[('361',2026,2)]=6.5;dom[('361',2026,3)]=5.0
def cal(nm,y,q): return dom.get((nm,y,q))
def al(nm,a,b):  # a=(y,q) first calendar quarter weight 1/3, b weight 2/3
    x,y=cal(nm,*a),cal(nm,*b)
    return None if x is None or y is None else x/3+2*y/3
M={'Q1FY2026':((2025,2),(2025,3)),'Q2FY2026':((2025,3),(2025,4)),'Q3FY2026':((2025,4),(2026,1)),'Q4FY2026':((2026,1),(2026,2)),'Q1FY2027':((2026,2),(2026,3)),'Q2FY2027':((2026,3),(2026,4))}
# Topsports bands (HKEX quarterly updates; midpoint of band words) mapped by quarter end
ts={'Q1FY2026':(-8,'high-single-digit decline','2025102200844'),'Q2FY2026':(-8,'high-single-digit decline','2025122200868'),'Q3FY2026':(-2.5,'low-single-digit decline','2026052701081'),
    'Q4FY2026':(-12,'low-teens decline (Mar to May 2026)','2026062500529')}
# NOTE Topsports fiscal quarter ending Aug = Nike Q1 etc. Update filed 2025-10-22 covers Jun-Aug 2025 = Nike Q1FY2026.
# the CSV in repo lists 'as_at 31 Aug 2025 high-single-digit', '30 Nov 2025 high-single', '28 Feb 2026 low-single', '31 May 2026 low-teens'
tsmap={'Q1FY2026':(-8,'high-single-digit decline','20251022_2025102200844'),'Q2FY2026':(-8,'high-single-digit decline','20251222_2025122200868'),
       'Q3FY2026':(-2.5,'low-single-digit decline','20260527_2026052701081'),'Q4FY2026':(-12,'low-teens decline','20260625_2026062500529')}
S,A=0.58,0.287; O=1-S-A
def adal(q):
    import importlib.util
    return None
rows=[]
for q in ['Q1FY2026','Q2FY2026','Q3FY2026','Q4FY2026','Q1FY2027']:
    b=bt[q]; n=pq['nbsq'].get(q); h=pq['hkq'].get(q)
    anta,lin,xt=[al(k,*M[q]) for k in('anta','lining','xtep')]
    vals=[v for v in(anta,lin,xt) if v is not None]
    comp=sum(vals)/len(vals) if vals else None
    # Q1FY2027 needs CY Q3 2026 for anta/lining/xtep (not out): None
    tsv=tsmap.get(q)
    ts_imp=None
    if tsv:
        ts_imp=(tsv[0]-A*float(b['adidas_aligned'])-O*0)/S
    rows.append([q,b['nike_gc_cc'],b['nike_gc_rep'],b['wh_cc_est'],b['dir_cc_est'],b['ps_total'],b['ps_implied_nike'],tsv[0] if tsv else '',tsv[1] if tsv else '',round(ts_imp,1) if ts_imp is not None else '',
      round(comp,1) if comp is not None else '',round(al('361',*M[q]),1) if al('361',*M[q]) is not None else '',round(n[0],1) if n else '',round(n[1],1) if n else '',round(h[0],1),round(h[1],1),b['adidas_aligned']])
hdr=['nike_fiscal_quarter','nike_gc_cc_pct','nike_gc_reported_pct','nike_wholesale_cc_est','nike_direct_cc_est','pousheng_total_yoy','pousheng_implied_nike_sellthrough','topsports_total_sales_yoy_midpoint','topsports_band','topsports_implied_nike_sellthrough','domestic_composite_anta_lining_xtep_aligned','361_core_aligned','nbs_clothes_shoes_hats_yoy','nbs_sports_recreational_yoy','hk_footwear_value_yoy','hk_apparel_value_yoy','adidas_gc_cc_aligned']
with open(D+'/panel_nike_fiscal_quarters.csv','w') as f:
    w=csv.writer(f);w.writerow(hdr+['tag']);[w.writerow(r+['DERIVED; sources in W5 note section 2']) for r in rows]
for r in rows: print(r)
# Q1FY27 nike-specific component
b=bt['Q1FY2027']
print('Nike-specific component Q1FY27 = PS implied %s minus NBS sports %s, minus 361 core %s'%(b['ps_implied_nike'],round(pq['nbsq']['Q1FY2027'][1],1),al('361',*M['Q1FY2027'])))
