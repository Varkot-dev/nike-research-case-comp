import json,datetime as dt,csv
cos={'1089063':"Dick's Sporting Goods (incl. Foot Locker from Sep 2025)",'850209':'Foot Locker','1817358':'Academy Sports','18498':'Genesco','14707':'Caleres','895447':'Shoe Carnival'}
rows=[]
for c,n in cos.items():
    f=json.load(open(f'raw/sec/cf_{c}.json'))['facts']['us-gaap']
    def get(t):
        o={}
        for x in f.get(t,{}).get('units',{}).get('USD',[]):
            if 'start' not in x: continue
            d=(dt.date.fromisoformat(x['end'])-dt.date.fromisoformat(x['start'])).days
            if 80<=d<=100: o[x['end']]=(x['val'],x['form'],x['accn'],x['filed'])
        return o
    gp=get('GrossProfit'); cg=get('CostOfGoodsAndServicesSold') or get('CostOfGoodsSold')
    cg2=get('CostOfGoodsSold')
    for e in sorted(gp):
        k=cg.get(e) or cg2.get(e)
        if not k: continue
        rv=gp[e][0]+k[0]
        rows.append(dict(company=n,quarter_end=e,sales_proxy=rv,gross_profit=gp[e][0],gross_margin_pct=round(gp[e][0]/rv*100,2),form=gp[e][1],accession=gp[e][2],filed=gp[e][3]))
with open('retailer_gross_margin_quarterly.csv','w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
import collections
by=collections.defaultdict(dict)
for r in rows: by[r['company']][r['quarter_end']]=r['gross_margin_pct']
yo=[]
for n,d in by.items():
    for e,v in sorted(d.items()):
        if e<'2024-06': continue
        y=dt.date.fromisoformat(e); prev=[k for k in d if abs((dt.date.fromisoformat(k)-y.replace(year=y.year-1)).days)<=10]
        if prev: yo.append(dict(company=n,quarter_end=e,gm=v,gm_prior_year=d[prev[0]],yoy_bps=round((v-d[prev[0]])*100)))
pd=__import__('csv')
with open('retailer_gross_margin_yoy_bps.csv','w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=yo[0].keys());w.writeheader();w.writerows(yo)
for r in yo: print(r)
