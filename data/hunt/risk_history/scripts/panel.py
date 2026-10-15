"""Build a quarterly panel (revenue, gross margin, operating margin, yoy changes) from SEC companyfacts.
Logic copied from the Round 3 q2.py (scratchpad/fund2/tool) so results reproduce:
 - current quarter value = first-filed value; prior-year value = version on file as of the current filing
 - Q4 = annual less nine months; GM = GrossProfit/Revenue or (Revenue-COGS)/Revenue
Usage: python3 -I panel.py SECDIR1[,SECDIR2] OUT.csv TICKERS..."""
import json, datetime as dt, sys, collections, csv, os
REV=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet','RevenueFromContractWithCustomerIncludingAssessedTax']
GP=['GrossProfit']
COGS=['CostOfRevenue','CostOfGoodsAndServicesSold','CostOfGoodsSold','CostOfGoodsSoldExcludingDepreciationDepletionAndAmortization','CostOfGoodsAndServiceExcludingDepreciationDepletionAndAmortization']
OI=['OperatingIncomeLoss','IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments']
D=dt.date.fromisoformat
class C:
    def __init__(s,g,nm):
        s.v=collections.defaultdict(list)
        for unit,fs in g[nm]['units'].items():
            if unit!='USD': continue
            for f in fs:
                if 'start' in f: s.v[(D(f['start']),D(f['end']))].append((D(f['filed']),f['val']))
        for k in s.v: s.v[k].sort()
    def find(s,e,lo,hi,start=None):
        return [k for k in s.v if abs((k[1]-e).days)<=6 and lo<=(k[1]-k[0]).days<=hi and (start is None or abs((k[0]-start).days)<=6)]
    def first(s,k): return s.v[k][0]
    def asof(s,k,d):
        x=[v for v in s.v[k] if v[0]<=d]; return x[-1] if x else None
    def q(s,e,mode,d=None):
        pick=(lambda k:s.first(k)) if mode=='first' else (lambda k:s.asof(k,d))
        for k in s.find(e,80,100):
            r=pick(k)
            if r: return r
        for ka in s.find(e,350,380):
            a=pick(ka)
            if not a: continue
            for k9 in s.find(e-dt.timedelta(days=91),260,285,start=ka[0]):
                n=s.asof(k9,a[0])
                if n: return (a[0],a[1]-n[1])
        return None
def quarters(g):
    ends=set()
    for nm in REV:
        for f in g.get(nm,{}).get('units',{}).get('USD',[]):
            if 'start' in f:
                dur=(D(f['end'])-D(f['start'])).days
                if 80<=dur<=100 or 350<=dur<=380: ends.add(D(f['end']))
    out=[]
    for e in sorted(ends):
        if not any(abs((e-x).days)<=6 for x in out): out.append(e)
    return out
def load(path):
    g=json.load(open(path))['facts'].get('us-gaap',{})
    cs={nm:C(g,nm) for nm in REV+GP+COGS+OI if nm in g}
    rows=[]
    for e in quarters(g):
        pe=e-dt.timedelta(days=364)
        cands=[(cs[nm].q(e,'first'),nm) for nm in REV if nm in cs]; cands=[c for c in cands if c[0]]
        if not cands: continue
        cur,nm=min(cands,key=lambda c:c[0][0]); pr=None
        for x in [nm]+[x for x in REV if x!=nm and x in cs]:
            pr=cs[x].q(pe,'asof',cur[0]) or cs[x].q(pe-dt.timedelta(days=7),'asof',cur[0])
            if pr: break
        fd=cur[0]; R=cur[1]; RP=pr[1] if pr else None
        def pair(names):
            cc=[(cs[n].q(e,'first'),n) for n in names if n in cs]; cc=[c for c in cc if c[0]]
            if not cc: return None,None
            cu,n0=min(cc,key=lambda c:c[0][0])
            for x in [n0]+[y for y in names if y!=n0 and y in cs]:
                p=cs[x].q(pe,'asof',max(cu[0],fd)) or cs[x].q(pe-dt.timedelta(days=7),'asof',max(cu[0],fd))
                if p: return cu[1],p[1]
            return cu[1],None
        g_,gp_=pair(GP)
        if g_ is None:
            c,cp=pair(COGS)
            if c is not None: g_=R-c; gp_=None if (cp is None or RP is None) else RP-cp
        o,op=pair(OI)
        r=dict(end=e,filed=fd,rev=R,ry=None,gm=None,gy=None,om=None,oy=None)
        if g_ is not None and R: r['gm']=g_/R
        if o is not None and R: r['om']=o/R
        if RP:
            r['ry']=R/RP-1
            if g_ is not None and gp_ is not None and RP: r['gy']=(g_/R-gp_/RP)*1e4
            if o is not None and op is not None: r['oy']=(o/R-op/RP)*1e4
        rows.append(r)
    return rows
if __name__=='__main__':
    dirs=sys.argv[1].split(','); out=sys.argv[2]; T=sys.argv[3:]
    w=csv.writer(open(out,'w',newline='')); w.writerow(['ticker','qend','filed','revenue_usd','rev_yoy','gross_margin','gm_yoy_bp','op_margin','om_yoy_bp'])
    for t in T:
        p=next((f'{d}/{t}.json' for d in dirs if os.path.exists(f'{d}/{t}.json')),None)
        if not p: print('missing',t); continue
        try: rows=load(p)
        except Exception as ex: print('fail',t,ex); continue
        for r in rows:
            f=lambda v,n: '' if v is None else round(v,n)
            w.writerow([t,r['end'],r['filed'],r['rev'],f(r['ry'],4),f(r['gm'],4),f(r['gy'],0),f(r['om'],4),f(r['oy'],0)])
        print(t,len(rows))
