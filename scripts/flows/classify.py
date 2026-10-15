import csv,sys,collections
raw=list(csv.DictReader(open(sys.argv[1]))); f144=list(csv.DictReader(open(sys.argv[2])))
plan144={(r['person'].lower().split()[0],r['approx_sale_date']) :r['plan_adoption'] for r in f144}
dups={'0000320187-26-000051'}  # Hill original Form 4, superseded by 4/A 26-000053
out=[]; seen=set()
for x in raw:
    if x['acc'] in dups: continue
    key=(x['owner'],x['date'],x['code'],x['shares'],x['table'],x['security'])
    if key in seen: continue  # 4/A duplicates
    seen.add(key)
    c=x['code']; fn=x['footnotes']
    d=x['date']; mdY=d[5:7]+'/'+d[8:10]+'/'+d[:4]
    p144=plan144.get((x['owner'].lower().split()[0].strip(','),mdY),'')
    planned = x['aff10b5One'] in ('1','true') or 'trading plan adopted' in fn or bool(p144)
    if c=='P': cat='Open-market purchase (10b5-1 plan)' if planned else 'Open-market purchase (discretionary)'
    elif c=='S':
        if x['table']=='ND' and any(y['acc']==x['acc'] and y['code']=='M' and y['date']==d and y['table']=='ND' and y['shares']==x['shares'] for y in raw): cat='Option exercise and sale (10b5-1 plan)' if planned else 'Option exercise and sale'
        else: cat='Open-market sale (10b5-1 plan)' if planned else 'Open-market sale (discretionary)'
    elif c=='F': cat='Tax withholding (not open market)'
    elif c=='G': cat='Gift or trust transfer'
    elif c=='M': cat='Option exercise'
    elif c=='A': cat='Grant or award'
    elif c=='C': cat='Class A to Class B conversion'
    elif c=='J': cat='Other (distribution, partnership transfer)'
    else: cat=c
    try: val=round(float(x['shares'])*float(x['price']),0) if x['price'] else ''
    except: val=''
    if c in('M','A','G','C','J') or x['table']=='D': val='' if c!='S' else val
    out.append(dict(date=d,owner=x['owner'],role=x['role'],code=c,category=cat,table=x['table'],security=x['security'],shares=x['shares'],price=x['price'],value_usd=val,
        shares_after=x['post'],ownership=('Direct' if x['direct']=='D' else 'Indirect '+x['nature']),plan_adoption_144=p144,accession=x['acc'],
        url='https://www.sec.gov/Archives/edgar/data/320187/'+x['acc'].replace('-','')+'/'))
out.sort(key=lambda r:(r['date'],r['owner']))
w=csv.DictWriter(open(sys.argv[3],'w',newline=''),fieldnames=list(out[0].keys()));w.writeheader();w.writerows(out)
print(collections.Counter(r['category'] for r in out))
tot=collections.defaultdict(lambda:[0,0.0,0])
for r in out:
    if r['value_usd']!='' and r['table']=='ND': t=tot[(r['category'])]; t[0]+=float(r['shares']); t[1]+=float(r['value_usd']); t[2]+=1
for k,v in tot.items(): print(k, round(v[0]), round(v[1]), v[2])
