import zipfile,csv,io,sys,collections
z=zipfile.ZipFile(sys.argv[1]); c=collections.Counter(); ex={}
n=[x for x in z.namelist() if x.endswith('INFOTABLE.tsv')][0]
sub={}
for r in csv.DictReader(io.TextIOWrapper(z.open([x for x in z.namelist() if x.endswith('SUBMISSION.tsv')][0]),encoding='utf-8',errors='replace'),delimiter='\t',quoting=csv.QUOTE_NONE): sub[r['ACCESSION_NUMBER']]=r['CIK']
for r in csv.DictReader(io.TextIOWrapper(z.open(n),encoding='utf-8',errors='replace'),delimiter='\t',quoting=csv.QUOTE_NONE):
    nm=(r['NAMEOFISSUER'] or '').upper()
    if nm.startswith('NIKE') and r['CUSIP'].strip().upper()!='654106103':
        c[r['CUSIP']]+=1; 
        if sub.get(r['ACCESSION_NUMBER'])=='0001374170': print('NORGES',r)
print(c.most_common(10))
print('norges accs',[a for a,k in sub.items() if k=='0001374170'])
