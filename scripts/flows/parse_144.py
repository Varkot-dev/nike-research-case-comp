import sys,glob,os,re,csv
rows=[]
for f in sorted(glob.glob(sys.argv[1]+'/*.xml')):
    s=open(f,encoding='utf-8',errors='replace').read()
    g=lambda tag: (re.search('<%s>([^<]*)</%s>'%(tag,tag),s) or [None,''])[1]
    rel=';'.join(re.findall('<relationshipToIssuer>([^<]*)<',s))
    nat=';'.join(sorted(set(re.findall('<natureOfAcquisitionTransaction>([^<]*)<',s))))
    plan=g('planAdoptionDate') or g('noticeDate')
    rows.append(dict(acc=os.path.basename(f)[:-4],person=g('nameOfPersonForWhoseAccountTheSecuritiesAreToBeSold'),relationship=rel,
      shares=g('noOfUnitsSold'),agg_value=g('aggregateMarketValue'),approx_sale_date=g('approxSaleDate'),broker=g('name'),
      acquired_via=nat,plan_adoption=';'.join(re.findall('<planAdoptionDate>([^<]*)<',s)),
      sold_past_3m=';'.join(re.findall('<amountOfSecuritiesSold>([^<]*)<',s))))
w=csv.DictWriter(open(sys.argv[2],'w',newline=''),fieldnames=list(rows[0].keys()));w.writeheader();w.writerows(rows)
for r in sorted(rows,key=lambda r:r['approx_sale_date'][-4:]+r['approx_sale_date']): print(r)
