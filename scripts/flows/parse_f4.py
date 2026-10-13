import sys,glob,os,csv,xml.etree.ElementTree as ET
d=sys.argv[1]; out=sys.argv[2]
rows=[]
def t(e,p):
    x=e.find(p); 
    return (x.text or '').strip() if x is not None and x.text else ''
for f in sorted(glob.glob(d+'/*.xml')):
    acc=os.path.basename(f)[:-4]
    try: r=ET.parse(f).getroot()
    except Exception as ex: print('ERR',f,ex); continue
    owners=[]; roles=[]
    for o in r.findall('reportingOwner'):
        owners.append(t(o,'reportingOwnerId/rptOwnerName'))
        rel=o.find('reportingOwnerRelationship'); rr=[]
        if rel is not None:
            if t(rel,'isDirector') in ('1','true'): rr.append('Director')
            if t(rel,'isOfficer') in ('1','true'): rr.append(t(rel,'officerTitle') or 'Officer')
            if t(rel,'isTenPercentOwner') in ('1','true'): rr.append('10% owner')
            if t(rel,'isOther') in ('1','true'): rr.append('Other:'+t(rel,'otherText'))
        roles.append('/'.join(rr))
    a10=t(r,'aff10b5One')
    fn={x.get('id'):(x.text or '').strip() for x in r.iter('footnote')}
    allfn=' | '.join(fn.values())
    for kind,tag in (('ND','nonDerivativeTable/nonDerivativeTransaction'),('D','derivativeTable/derivativeTransaction')):
        for tx in r.findall(tag):
            code=t(tx,'transactionCoding/transactionCode')
            sh=t(tx,'transactionAmounts/transactionShares/value')
            pr=t(tx,'transactionAmounts/transactionPricePerShare/value')
            ad=t(tx,'transactionAmounts/transactionAcquiredDisposedCode/value')
            post=t(tx,'postTransactionAmounts/sharesOwnedFollowingTransaction/value')
            di=t(tx,'ownershipNature/directOrIndirectOwnership/value')
            nat=t(tx,'ownershipNature/natureOfOwnership/value')
            fids=[x.get('id') for x in tx.iter('footnoteId')]
            ftxt=' | '.join(fn.get(i,'') for i in fids)
            plan='10b5-1' if ('10b5-1' in ftxt or '10b5-1' in allfn and code=='S') else ''
            if a10 in ('1','true'): plan='10b5-1'
            rows.append(dict(acc=acc,period=t(r,'periodOfReport'),owner='; '.join(owners),role='; '.join(roles),table=kind,
              security=t(tx,'securityTitle/value'),date=t(tx,'transactionDate/value'),code=code,ad=ad,shares=sh,price=pr,
              post=post,direct=di,nature=nat,plan=plan,aff10b5One=a10,footnotes=ftxt[:400].replace('\n',' ')))
with open(out,'w',newline='') as fo:
    w=csv.DictWriter(fo,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print(len(rows))
