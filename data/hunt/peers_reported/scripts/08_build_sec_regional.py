"""Build discrete-quarter regional revenue series for SEC filers from the dimensional facts.
Q4 (or any missing quarter) derived as annual minus 9-month YTD when needed. Output: sec_regional_quarterly.csv"""
import csv, re, datetime as dt, collections
B='/home/user/nike-research-case-comp/data/hunt/peers_reported'
D=lambda s: dt.date.fromisoformat(s)
REVTAGS=('Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','RevenueFromContractsWithCustomers','Revenue','SalesRevenueNet')
BAD=('ProductOrService','SalesChannel','ProductsAndServices','SalesChannels','Restatement','Concentration','Adjustments','Derivative','BusinessAcquisition','NatureOfExpense','InitialApplication','Error')
RULES={ # company: [(region, regex on dims)]
 'nike':[('North America',r'SubsegmentsAxis=NorthAmerica|BusinessSegmentsAxis=NorthAmerica'),('EMEA',r'SubsegmentsAxis=EuropeMiddleEastAndAfrica|BusinessSegmentsAxis=EuropeMiddleEastAndAfrica'),
         ('Greater China',r'SubsegmentsAxis=GreaterChina|BusinessSegmentsAxis=GreaterChina'),('APLA',r'SubsegmentsAxis=AsiaPacificAndLatinAmerica|BusinessSegmentsAxis=AsiaPacificAndLatinAmerica'),('Converse',r'BusinessSegmentsAxis=ConverseSegmentMember$|BusinessSegmentsAxis=ConverseSegmentMember;|^StatementBusinessSegmentsAxis=ConverseMember$')],
 'underarmour':[('North America',r'(Geographical|BusinessSegments)Axis=NorthAmericaMember$'),('EMEA',r'(Geographical|BusinessSegments)Axis=EMEAMember$'),('Asia-Pacific',r'(Geographical|BusinessSegments)Axis=AsiaPacificMember$'),('Latin America',r'(Geographical|BusinessSegments)Axis=LatinAmericaMember$')],
 'vf':[('Active Americas',r'ActiveMember;StatementGeographicalAxis=AmericasMember$'),('Active Europe',r'ActiveMember;StatementGeographicalAxis=EuropeMember$'),('Active Asia-Pacific',r'ActiveMember;StatementGeographicalAxis=AsiaPacificMember$'),('Active',r'^StatementBusinessSegmentsAxis=ActiveMember$')],
 'lululemon':[('Americas',r'^StatementGeographicalAxis=AmericasMember$|^StatementBusinessSegmentsAxis=AmericasSegmentMember$'),('US',r'^StatementGeographicalAxis=US$'),('Canada',r'^StatementGeographicalAxis=CA$'),('China Mainland',r'^StatementGeographicalAxis=ChinaMainlandMember$|^StatementGeographicalAxis=CN$|ChinaMainlands?SegmentMember$'),('Rest of World',r'^StatementGeographicalAxis=RestOfWorldMember$|OtherCountrySegmentMember$')],
 'deckers':[('HOKA',r'HokaBrand|HokaMember'),('UGG',r'UGGBrand|UGGMember'),('US',r'^StatementGeographicalAxis=US$'),('International',r'^StatementGeographicalAxis=NonUsMember$')],
 'skechers':[('Americas',r'^StatementGeographicalAxis=AmericasMember$'),('EMEA',r'^StatementGeographicalAxis=EuropeMiddleEastAndAfricaMember$'),('Asia-Pacific',r'^StatementGeographicalAxis=AsiaPacificMember$'),('China',r'^StatementGeographicalAxis=CN$'),('US',r'^StatementGeographicalAxis=US$'),('International',r'^StatementGeographicalAxis=NonUsMember$')],
 'crocs':[('Crocs North America',r'CrocsBrandSegmentMember;StatementGeographicalAxis=NorthAmericaMember$'),('Crocs International',r'CrocsBrandSegmentMember;StatementGeographicalAxis=InternationalMember$'),('HEYDUDE',r'^StatementBusinessSegmentsAxis=HEYDUDEBrandSegmentMember$')],
 'columbia':[('US',r'StatementGeographicalAxis=US$|BusinessSegmentsAxis=UnitedStatesMember$'),('EMEA',r'StatementGeographicalAxis=EMEAMember$|BusinessSegmentsAxis=EuropeMiddleEastAndAfricaMember$'),('LAAP',r'LatinAmericaAndAsiaPacificMember$'),('Canada',r'StatementGeographicalAxis=CA$|BusinessSegmentsAxis=CanadaMember$')],
 'on':[('Americas',r'GeographicalAreasAxis=AmericasMember$'),('EMEA',r'GeographicalAreasAxis=EuropeMiddleEastAndAfricaMember$'),('Asia-Pacific',r'GeographicalAreasAxis=AsiaPacificMember$')],
 'amer':[('Americas',r'GeographicalAreasAxis=AmericasMember$'),('EMEA',r'GeographicalAreasAxis=(IFRS)?EMEAMember$'),('Greater China',r'GeographicalAreasAxis=GreaterChinaMember$'),('Asia-Pacific ex China',r'GeographicalAreasAxis=AsiaPacificExcludingGreaterChinaMember$')],
 'birkenstock':[('Americas',r'GeographicalAreasAxis=AmericasMember$'),('EMEA',r'GeographicalAreasAxis=EuropeMiddleEastAndAfricaMember$'),('Asia-Pacific',r'GeographicalAreasAxis=AsiaPacificMember$')],
}
facts=collections.defaultdict(dict)  # (co,region) -> {(start,end): (value, accn, dims, tag)}
for r in csv.DictReader(open(B+'/raw/sec_xbrl_dimensional_facts.csv')):
    if r['tag'] not in REVTAGS or not r['start']: continue
    co=r['company']; dims=r['dims']
    core=';'.join(d for d in dims.split(';') if not d.startswith('ConsolidationItemsAxis'))
    if dims=='' : reg='Total'
    else:
        if any(b in core for b in BAD) and not (co=='vf' and 'ActiveMember' in core and 'Product' not in core): continue
        reg=None
        for name,rx in RULES.get(co,[]):
            if re.search(rx,core): reg=name; break
        if not reg: continue
    k=(r['start'],r['end']); prev=facts[(co,reg)].get(k)
    # prefer the shortest dims (true total) and the latest report
    cand=(len(core),-int(r['report_date'].replace('-','')))
    if prev is None or cand<prev[4]:
        facts[(co,reg)][k]=(float(r['value']),r['accn'],core,r['tag'],cand,r['unit'],r['report_date'])
out=[]
for (co,reg),d in facts.items():
    q={}; ytd={}
    for (s,e),v in d.items():
        n=(D(e)-D(s)).days
        if 80<=n<=100: q[e]=(s,v,'reported')
        else: ytd[(s,e)]=(n,v)
    # derive missing quarters: YTD(e) - YTD(prev) with same start
    for (s,e),(n,v) in ytd.items():
        if e in q: continue
        prevs=[(s2,e2,v2) for (s2,e2),(n2,v2) in ytd.items() if s2==s and D(e2)<D(e) and 75<=(D(e)-D(e2)).days<=105]
        if prevs:
            s2,e2,v2=max(prevs,key=lambda x:x[1]); q[e]=(str(D(e2)+dt.timedelta(days=1)),(v[0]-v2[0],)+v[1:],'derived_ytd_diff')
        elif 170<=n<=190 and any(D(qe)<D(e) and D(q[qe][0])==D(s) for qe in q):
            qe=[qe for qe in q if D(q[qe][0])==D(s)][0]; q[e]=(str(D(qe)+dt.timedelta(days=1)),(v[0]-q[qe][1][0],)+v[1:],'derived_h1_minus_q1')
    for e,(s,v,how) in sorted(q.items()):
        out.append(dict(company=co,region=reg,period_start=s,period_end=e,revenue=v[0],unit=v[5],how=how,dims=v[2],accn=v[1]))
out.sort(key=lambda r:(r['company'],r['region'],r['period_end']))
with open(B+'/sec_regional_quarterly.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
c=collections.defaultdict(list)
for r in out: c[(r['company'],r['region'])].append(r['period_end'])
for k in sorted(c): print(k,len(c[k]),c[k][0],c[k][-1])
