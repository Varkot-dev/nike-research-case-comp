"""W5 China nowcast panel. Inputs are CSVs in data/wave3_w5 plus raw HK C&SD json in scratch (path arg). Run: python3 -I build_panel.py <hk_json_dir>"""
import csv,json,sys,collections,os
D=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HK=sys.argv[1]
def rd(f): return list(csv.DictReader(open(os.path.join(D,f))))
mo={'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
# ---- Nike fiscal quarter of a calendar month: FY label
def nq(y,m):
    # Nike FY ends May. Q1 Jun-Aug, Q2 Sep-Nov, Q3 Dec-Feb, Q4 Mar-May
    if m>=6: fy=y+1
    else: fy=y
    if m in(6,7,8): q=1
    elif m in(9,10,11): q=2
    elif m==12 or m<=2: q=3; fy=y+1 if m==12 else y
    else: q=4
    return f"Q{q}FY{fy}"
# ---- Pou Sheng quarterly on Nike quarters
ps=rd('pousheng_monthly_revenue.csv')
cur=collections.defaultdict(float);pri=collections.defaultdict(float);cnt=collections.Counter()
for r in ps:
    k=nq(int(r['year']),mo[r['month']]); cur[k]+=float(r['rev_rmb_k']);pri[k]+=float(r['prior_yr_rmb_k']);cnt[k]+=1
psq={k:(cur[k]/pri[k]-1)*100 for k in cur if cnt[k]==3}
with open(os.path.join(D,'pousheng_nike_fiscal_quarters.csv'),'w') as f:
    w=csv.writer(f);w.writerow(['nike_fiscal_quarter','rev_rmb_k','prior_rmb_k','yoy_pct','tag'])
    for k in sorted(psq,key=lambda s:(s[-4:],s[:2])): w.writerow([k,int(cur[k]),int(pri[k]),round(psq[k],2),'DERIVED from HKEX monthly revenue announcements (pousheng_monthly_revenue.csv)'])
# ---- NBS
nbs=[ # month label, clothes level (100m yuan), clothes yoy, sports level, sports yoy ; source file
('2025-03',1240,3.6,151,26.2),('2025-04',1088,2.2,132,23.3),('2025-05',1225,4.0,162,28.3),('2025-06',1275,1.9,165,9.5),
('2025-07',961,1.8,127,13.7),('2025-08',1045,3.1,127,16.9),('2025-09',1231,4.7,129,11.9),('2025-10',1471,6.3,157,10.1),
('2025-11',1542,3.5,154,0.4),('2025-12',1661,0.6,152,9.0),('2026-01_02',2831,10.4,265,4.1),('2026-03',1296,7.0,145,-2.0),
('2026-04',1108,3.6,129,-8.0),('2026-05',1251,3.8,157,-8.0),('2026-06',1285,3.9,173,-2.2),('2026-07',922,-1.0,125,-10.6),('2026-08',1013,-0.5,134,-4.8)]
with open(os.path.join(D,'nbs_monthly.csv'),'w') as f:
    w=csv.writer(f);w.writerow(['month','clothes_shoes_hats_textiles_100m_yuan','clothes_yoy_pct','sports_recreational_100m_yuan','sports_yoy_pct','tag'])
    for r in nbs: w.writerow(list(r)+['OPENED stats.gov.cn English monthly release; designated-size enterprises (category rows)'])
def nbs_q(idxs):
    out={}
    for name,months in idxs.items():
        c=sum(r[1] for r in nbs if r[0] in months);cp=sum(r[1]/(1+r[2]/100) for r in nbs if r[0] in months)
        s=sum(r[3] for r in nbs if r[0] in months);sp=sum(r[3]/(1+r[4]/100) for r in nbs if r[0] in months)
        out[name]=((c/cp-1)*100,(s/sp-1)*100)
    return out
nbsq=nbs_q({'Q4FY2026':['2026-03','2026-04','2026-05'],'Q1FY2027':['2026-06','2026-07','2026-08'],'Q1FY2026':['2025-06','2025-07','2025-08'],
 'Q2FY2026':['2025-09','2025-10','2025-11'],'Q3FY2026':['2025-12','2026-01_02']})
# ---- HK C&SD
d=json.load(open(os.path.join(HK,'a_67002.txt')))['dataSet']
want={'Footwear, allied products and other clothing accessories':'footwear','Wearing apparel':'apparel','Clothing, footwear and allied products':'clothing_footwear_total','Total':'all_retail'}
hk=collections.defaultdict(dict)
for x in d:
    if x['freq']!='M': continue
    n=x['OUTLET_TYPEDesc'].strip()
    if n in want:
        if x['sv']=='VAL_RS': hk[x['period']][want[n]+'_hkd_m']=x['figure']
        if x['sv']=='VAL_IDX_RS' and x['svDesc'].startswith('Year'): hk[x['period']][want[n]+'_value_yoy_pct']=x['figure']
v=json.load(open(os.path.join(HK,'a_67003.txt')))['dataSet']
for x in v:
    if x['freq']!='M': continue
    n=x['OUTLET_TYPEDesc'].strip()
    if n in want and x['svDesc'].startswith('Year'): hk[x['period']][want[n]+'_volume_yoy_pct']=x['figure']
cols=sorted({k for p in hk.values() for k in p})
with open(os.path.join(D,'hk_retail_monthly.csv'),'w') as f:
    w=csv.writer(f);w.writerow(['period']+cols+['tag'])
    for p in sorted(hk):
        if p>='202301': w.writerow([p]+[hk[p].get(c,'') for c in cols]+['OPENED censtatd.gov.hk api table 620-67002 and 620-67003 (full_series)'])
def hkq(months,key='footwear_hkd_m'):
    c=sum(hk[m][key] for m in months)
    pm=[str(int(m)-100) for m in months]
    p=sum(hk[m][key] for m in pm)
    return (c/p-1)*100
hkqs={'Q1FY2027':['202606','202607','202608'],'Q4FY2026':['202603','202604','202605'],'Q3FY2026':['202512','202601','202602'],'Q2FY2026':['202509','202510','202511'],'Q1FY2026':['202506','202507','202508']}
hkout={q:(hkq(m,'footwear_hkd_m'),hkq(m,'wearing_apparel_hkd_m') if 'wearing_apparel_hkd_m' in hk[m[0]] else hkq(m,'apparel_hkd_m')) for q,m in hkqs.items()}
json.dump({'nbsq':nbsq,'hkq':hkout,'psq':psq},open('/tmp/w5_interim.json','w'),indent=1)
for q in hkqs: print(q,'NBS clothes/sports',[round(x,1) for x in nbsq.get(q,('',''))] if q in nbsq else '', 'HK footwear/apparel',[round(x,1) for x in hkout[q]])
print({k:round(v,2) for k,v in psq.items() if k[-4:]>='2024'})
