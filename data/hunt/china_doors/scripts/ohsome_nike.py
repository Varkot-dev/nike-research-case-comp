"""OSM history via ohsome API (no login). Counts Nike-tagged shop features in city bounding boxes
(whole-country polygon requests returned HTTP 500). Quarterly 2022-01-01..2026-07-01.
OSM completeness changes over time, so this only shows mapping coverage plus any large closure waves."""
import requests, sys, csv, time
UA={'User-Agent':'research-bot/1.0'}
CITIES={ # tier, name: lon_min,lat_min,lon_max,lat_max
 ('T1','Beijing'):(116.1,39.7,116.8,40.2),('T1','Shanghai'):(121.0,30.9,121.9,31.6),
 ('T1','Guangzhou'):(113.1,22.9,113.6,23.4),('T1','Shenzhen'):(113.8,22.45,114.4,22.85),
 ('NT1','Chengdu'):(103.9,30.5,104.3,30.8),('NT1','Hangzhou'):(120.0,30.1,120.4,30.4),
 ('NT1','Chongqing'):(106.4,29.4,106.7,29.8),('NT1','Wuhan'):(114.1,30.4,114.5,30.7),
 ('NT1','Nanjing'):(118.6,31.9,118.95,32.2),('NT1','Xian'):(108.8,34.1,109.1,34.4),
 ('T2','Suzhou'):(120.5,31.2,120.8,31.4),('T2','Tianjin'):(117.0,38.9,117.5,39.3),
 ('T2','Changsha'):(112.85,28.1,113.1,28.3),('T2','Zhengzhou'):(113.5,34.65,113.85,34.9),
 ('T2','Qingdao'):(120.2,36.0,120.5,36.2),('T2','Shenyang'):(123.3,41.7,123.6,41.9),
 ('T2','Ningbo'):(121.4,29.75,121.7,29.95),('T2','Xiamen'):(118.0,24.4,118.2,24.6),
 ('T2','Kunming'):(102.6,24.9,102.85,25.15),('T2','Hefei'):(117.15,31.7,117.4,31.95),
 ('T3','Nanning'):(108.2,22.7,108.5,22.9),('T3','Lanzhou'):(103.6,35.95,103.95,36.15),
 ('T3','Guiyang'):(106.6,26.5,106.8,26.7),('T3','Taiyuan'):(112.4,37.75,112.7,38.0),
}
NIKE='(brand in (Nike,NIKE,"耐克") or brand:wikidata=Q483915 or name in (Nike,NIKE,"耐克")) and shop=*'
FILTERS={'nike':NIKE,
 'adidas':'(brand in (adidas,Adidas,"阿迪达斯") or brand:wikidata=Q3895 or name in (adidas,Adidas,ADIDAS,"阿迪达斯")) and shop=*',
 'anta':'(brand in (ANTA,Anta,"安踏") or brand:wikidata=Q4766688 or name in (ANTA,Anta,"安踏")) and shop=*',
 'lining':'(brand in (Li-Ning,"李宁") or brand:wikidata=Q1466155 or name in (Li-Ning,"李宁")) and shop=*'}
rows=[]
import itertools
for k,f in FILTERS.items():
  for (t0,n0),b0 in CITIES.items():
    bb=f'{n0}:{",".join(map(str,b0))}'
    for attempt in range(3):
        try: r=requests.post('https://api.ohsome.org/v1/elements/count/groupBy/boundary',data={'bboxes':bb,'filter':f,'time':'2022-01-01/2026-07-01/P3M'},headers=UA,timeout=600)
        except Exception as e: print(k,n0,'ERR',e,file=sys.stderr); time.sleep(5); continue
        if r.status_code==200: break
        print(k,r.status_code,r.text[:200],file=sys.stderr); time.sleep(5)
    else: continue
    for g in r.json()['groupByResult']:
        tier=[t for (t,n) in CITIES if n==g['groupByObject']][0]
        for x in g['result']: rows.append((k,tier,g['groupByObject'],x['timestamp'][:10],int(x['value'])))
    time.sleep(0.5)
w=csv.writer(open('osm_ohsome_city_counts_quarterly.csv','w')); w.writerow(['series','tier','city','date','count']); w.writerows(rows)
print(len(rows))
