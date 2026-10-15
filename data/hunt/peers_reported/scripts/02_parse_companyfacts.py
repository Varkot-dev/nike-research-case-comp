"""Parse SEC companyfacts into a quarterly panel: revenue, gross profit, inventory.
Discrete quarters: use ~3-month duration facts; if a fiscal Q4 is missing, derive annual minus the three prior discrete quarters.
Run: python3 -I 02_parse_companyfacts.py"""
import json, csv, os, datetime as dt
BASE='/home/user/nike-research-case-comp/data/hunt/peers_reported'
RAW=BASE+'/raw/sec_companyfacts'
COS=['nike','deckers','lululemon','vf','underarmour','skechers','on','crocs','amer','birkenstock','columbia','dicks']
REV=['RevenueFromContractWithCustomerExcludingAssessedTax','Revenues','SalesRevenueNet','SalesRevenueGoodsNet','RevenueFromContractWithCustomerIncludingAssessedTax','Revenue']
GP=['GrossProfit']
COGS=['CostOfGoodsAndServicesSold','CostOfRevenue','CostOfGoodsSold','CostOfSales']
INV=['InventoryNet','InventoryFinishedGoodsNetOfReserves','Inventories','InventoryFinishedGoods']
def D(s): return dt.date.fromisoformat(s)
def facts(j,tags):
    out={}
    for tax in ('us-gaap','ifrs-full'):
        for t in tags:
            node=j.get('facts',{}).get(tax,{}).get(t)
            if not node: continue
            for unit,arr in node['units'].items():
                for f in arr:
                    key=(f.get('start'),f['end'])
                    # prefer latest filed value (restatements) -> keep latest 'filed'
                    prev=out.get(key)
                    if prev is None or (f['filed']>prev['filed']):
                        out[key]=dict(val=f['val'],filed=f['filed'],form=f['form'],tag=t,unit=unit,accn=f['accn'])
    return out
def quarters(fs):
    q={}; ann={}
    for (s,e),f in fs.items():
        if s is None: continue
        d=(D(e)-D(s)).days
        if 80<=d<=100: q[e]=dict(f,start=s)
        elif 350<=d<=380: ann[e]=dict(f,start=s)
        elif 170<=d<=190 or 260<=d<=285: pass
    # derive missing Q4s
    for e,a in ann.items():
        if e in q: continue
        st=D(a['start']); inside=[k for k in q if D(q[k]['start'])>=st-dt.timedelta(days=5) and D(k)<D(e)]
        if len(inside)==3:
            q[e]=dict(a,val=a['val']-sum(q[k]['val'] for k in inside),start=str(D(sorted(inside)[-1])+dt.timedelta(days=1)),derived='annual_minus_3q')
    return q
def inst(fs):
    return {e:f for (s,e),f in fs.items() if s is None}
rows=[]
for c in COS:
    j=json.load(open(f'{RAW}/{c}.json'))
    # merge revenue across tags: prefer tag giving most quarters per date
    best={}
    for t in REV:
        qq=quarters(facts(j,[t]))
        for e,v in qq.items():
            if e not in best: best[e]=v
    gp=quarters(facts(j,GP)); cg={}
    for t in COGS:
        for e,v in quarters(facts(j,[t])).items(): cg.setdefault(e,v)
    iv={}
    for t in INV:
        for e,v in inst(facts(j,[t])).items(): iv.setdefault(e,v)
    for e in sorted(best):
        if e<'2017-01-01': continue
        r=best[e]; g=gp.get(e,{}).get('val')
        if g is None and e in cg: g=r['val']-cg[e]['val']
        rows.append(dict(company=c,period_start=r['start'],period_end=e,revenue=r['val'],gross_profit=g,
            inventory=iv.get(e,{}).get('val'),unit=r['unit'],rev_tag=r['tag'],derived=r.get('derived',''),form=r['form'],accn=r['accn']))
with open(BASE+'/sec_quarterly_financials_raw.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
import collections
cnt=collections.Counter(r['company'] for r in rows)
for c in COS:
    rr=[r for r in rows if r['company']==c]
    print(c,cnt[c], rr[0]['period_end'] if rr else '', rr[-1]['period_end'] if rr else '', sum(1 for r in rr if r['gross_profit'] is None), sum(1 for r in rr if r['inventory'] is None))
