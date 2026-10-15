import sys; sys.path.insert(0,'/tmp/claude-0/-home-user-nike-research-case-comp/2bf9f309-3096-5c65-b9c3-02b984182743/scratchpad/scripts')
from lib import *
import csv,statistics
D=dt.date
# (id, issuer, cpn, maturity, ccy, venue, slug)
B=[
('NKE 2.375 Nov26','Nike',2.375,D(2026,11,1),'USD','BMN','a1875n-nike-anleihe'),
('NKE 2.75 Mar27','Nike',2.75,D(2027,3,27),'USD','BMN','a28vaq-nike-anleihe'),
('NKE 2.85 Mar30','Nike',2.85,D(2030,3,27),'USD','BMN','a28var-nike-anleihe'),
('NKE 3.25 Mar40','Nike',3.25,D(2040,3,27),'USD','BMN','a28vas-nike-anleihe'),
('NKE 3.625 May43','Nike',3.625,D(2043,5,1),'USD','BMN','a1hka3-nike-anleihe'),
('NKE 3.875 Nov45','Nike',3.875,D(2045,11,1),'USD','BMN','a1z9n3-nike-anleihe'),
('NKE 3.375 Nov46','Nike',3.375,D(2046,11,1),'USD','BMN','a1875p-nike-anleihe'),
('NKE 3.375 Mar50','Nike',3.375,D(2050,3,27),'USD','BMN','a28vat-nike-anleihe'),
('RL 2.95 Jun30','Ralph Lauren',2.95,D(2030,6,15),'USD','BMN','a28x7s-ralph-lauren-anleihe'),
('RL 5.0 Jun32','Ralph Lauren',5.0,D(2032,6,15),'USD','BMN','a4eccz-ralph-lauren-anleihe'),
('TPR 4.125 Jul27','Tapestry',4.125,D(2027,7,15),'USD','STU','a19jyd-tapestry-anleihe'),
('TPR 5.1 Mar30','Tapestry',5.1,D(2030,3,11),'USD','STU','a3l63j-tapestry-anleihe'),
('TPR 3.05 Mar32','Tapestry',3.05,D(2032,3,15),'USD','BMN','a3ky06-tapestry-anleihe'),
('TPR 5.5 Mar35','Tapestry',5.5,D(2035,3,11),'USD','STU','a3l63k-tapestry-anleihe'),
('LEVI 3.5 Mar31','Levi Strauss',3.5,D(2031,3,1),'USD','STU','a3klmx-levi-strauss-anleihe'),
('UA 7.25 Jul30','Under Armour',7.25,D(2030,7,15),'USD','FSE','a4edm1-under-armour-anleihe'),
('VFC 6.0 Oct33','VF Corp',6.0,D(2033,10,15),'USD','FSE','a0bdx3-vf-anleihe'),
('PVH 5.5 Jun30','PVH',5.5,D(2030,6,13),'USD','BMN','a4ecp2-pvh-anleihe'),
('ADS 3.125 Nov29 EUR','adidas',3.125,D(2029,11,21),'EUR','BMN','a30v3n-adidas-anleihe'),
('ADS 2.75 Nov30 EUR','adidas',2.75,D(2030,11,6),'EUR','BMN','a460p9-adidas-anleihe'),
('ADS 0.625 Sep35 EUR','adidas',0.625,D(2035,9,10),'EUR','BMN','a3h2x1-adidas-anleihe'),
('VFC 4.25 Mar29 EUR','VF Corp',4.25,D(2029,3,7),'EUR','BMN','a3levn-vf-anleihe'),
('PVH 3.125 Dec27 EUR','PVH',3.125,D(2027,12,15),'EUR','BMN','a19twr-pvh-anleihe'),
('PVH 4.125 Jul29 EUR','PVH',4.125,D(2029,7,16),'EUR','BMN','a3lxd5-pvh-anleihe'),
('LEVI 4.0 Aug30 EUR','Levi Strauss',4.0,D(2030,8,15),'EUR','BMN','a4eeet-levi-strauss-anleihe'),
]
# ECB
ECB={}
for t,y in [('1Y',1),('2Y',2),('3Y',3),('5Y',5),('7Y',7),('10Y',10),('15Y',15),('20Y',20)]:
    for r in csv.DictReader(open(f'{RAW}/ecb_{t}.csv')):
        ECB.setdefault(dt.date.fromisoformat(r['TIME_PERIOD']),{})[y]=(math.exp(float(r['OBS_VALUE'])/100)-1)*100
def ecb_at(d):
    if d<min(ECB): d=min(ECB)
    while d not in ECB: d-=dt.timedelta(days=1)
    return ECB[d]
OAS={k:load_oas(k) for k in ['BAMLC0A1CAAA','BAMLC0A2CAA','BAMLC0A3CA','BAMLC0A4CBBB','BAMLH0A1HYBB','BAMLC0A0CM','BAMLC1A0C13Y','BAMLC2A0C35Y','BAMLC3A0C57Y','BAMLC4A0C710Y','BAMLC7A0C1015Y','BAMLC8A0C15PY']}
def oas(k,d):
    s=OAS[k]; 
    for i in range(10):
        if d in s: return s[d]
        d-=dt.timedelta(days=1)
    return None
def bucket(T):
    if T<3: return 'BAMLC1A0C13Y'
    if T<5: return 'BAMLC2A0C35Y'
    if T<7: return 'BAMLC3A0C57Y'
    if T<10: return 'BAMLC4A0C710Y'
    if T<15: return 'BAMLC7A0C1015Y'
    return 'BAMLC8A0C15PY'
rows=[]
for bid,iss,cpn,mat,ccy,mk,slug in B:
    h=parse.load(slug,mk)
    for d in sorted(h):
        dd=D.fromisoformat(d); s=dd+dt.timedelta(days=1)
        if mat<=s+dt.timedelta(days=30) or dd<D(2023,1,1): continue
        T=(mat-s).days/365.25; px=h[d]['close']
        if ccy=='USD':
            cur=curve_at(dd); y=ytm(px,s,mat,cpn); tb=interp(cur,T); isp=(y-tb)*100
            try: zs=zspread(px,s,mat,cpn,cur)
            except Exception: zs=None
            b=bucket(T)
            rows.append(dict(date=d,bond=bid,issuer=iss,ccy=ccy,coupon=cpn,maturity=mat.isoformat(),years_left=round(T,2),clean_px=px,ytm_pct=round(y,3),benchmark_pct=round(tb,3),i_spread_bp=round(isp,1),z_spread_bp=round(zs,1) if zs is not None else '',bucket_oas_bp=oas(b,dd),A_oas_bp=oas('BAMLC0A3CA',dd),BBB_oas_bp=oas('BAMLC0A4CBBB',dd),BB_oas_bp=oas('BAMLH0A1HYBB',dd),AA_oas_bp=oas('BAMLC0A2CAA',dd)))
        else:
            e=ecb_at(dd); ks=sorted(e); 
            tb=interp(e,T)
            # annual pay
            lo,hi=-0.05,0.5
            # annual-coupon YTM
            def pv(y):
                n=math.ceil(T-1e-9); tot=0
                for k in range(n):
                    t=T-(n-1-k) # approx time to each coupon
                    # years to coupon k from settle: T-(n-1-k)
                    tot+=cpn/(1+y)**t
                tot+=100/(1+y)**T
                frac=T-(n-1)  # time to next coupon
                acc=cpn*(1-frac)
                return tot-acc
            for _ in range(100):
                mid=(lo+hi)/2
                if pv(mid)>px: lo=mid
                else: hi=mid
            y=mid*100
            rows.append(dict(date=d,bond=bid,issuer=iss,ccy=ccy,coupon=cpn,maturity=mat.isoformat(),years_left=round(T,2),clean_px=px,ytm_pct=round(y,3),benchmark_pct=round(tb,3),i_spread_bp=round((y-tb)*100,1),z_spread_bp='',bucket_oas_bp='',A_oas_bp='',BBB_oas_bp='',BB_oas_bp='',AA_oas_bp=''))
import os
out='/home/user/nike-research-case-comp/data/credit'
os.makedirs(out,exist_ok=True)
cols=list(rows[0].keys())
with open(out+'/g5_bond_daily_spreads.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=cols); w.writeheader(); w.writerows(rows)
print(len(rows))
import pickle; pickle.dump(rows,open('rows.pkl','wb'))
