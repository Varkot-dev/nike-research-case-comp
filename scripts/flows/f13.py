import zipfile,csv,io,sys,glob,os,collections,datetime
CUSIP='654106103'
recs=[]  # per accession
sub={};cov={};hold=collections.defaultdict(lambda:collections.Counter())
for z in sorted(glob.glob(sys.argv[1]+'/*.zip')):
    zf=zipfile.ZipFile(z)
    def rd(name):
        n=[x for x in zf.namelist() if x.endswith(name)][0]
        return csv.DictReader(io.TextIOWrapper(zf.open(n),encoding='utf-8',errors='replace'),delimiter='\t',quoting=csv.QUOTE_NONE)
    for r in rd('SUBMISSION.tsv'): sub[r['ACCESSION_NUMBER']]=r
    for r in rd('COVERPAGE.tsv'): cov[r['ACCESSION_NUMBER']]=r
    n=0
    for r in rd('INFOTABLE.tsv'):
        if r['CUSIP'].strip().upper()==CUSIP:
            a=r['ACCESSION_NUMBER']; pc=(r['PUTCALL'] or '').strip().upper()
            k='sh' if not pc else pc.lower()
            try: sh=float(r['SSHPRNAMT']); v=float(r['VALUE'])
            except: continue
            if r['SSHPRNAMTTYPE'].strip()!='SH' and not pc: continue
            hold[a][k+'_shares']+=sh; hold[a][k+'_value']+=v
            n+=1
    print(z,n,file=sys.stderr)
rows=[]
for a,h in hold.items():
    s=sub.get(a,{}); c=cov.get(a,{})
    rows.append(dict(accession=a,cik=s.get('CIK',''),manager=c.get('FILINGMANAGER_NAME',''),period=s.get('PERIODOFREPORT',''),cover_period=c.get('REPORTCALENDARORQUARTER',''),filing_date=s.get('FILING_DATE',''),form=s.get('SUBMISSIONTYPE',''),
      amend=c.get('ISAMENDMENT',''),amend_type=c.get('AMENDMENTTYPE',''),shares=h['sh_shares'],value=h['sh_value'],put_shares=h['put_shares'],call_shares=h['call_shares']))
w=csv.DictWriter(open(sys.argv[2],'w',newline=''),fieldnames=list(rows[0].keys()));w.writeheader();w.writerows(rows)
print(len(rows))
