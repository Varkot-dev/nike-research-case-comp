"""Fetch earnings-release exhibits (8-K Item 2.02 Ex.99.1, or 6-K Ex.99.1 for On) since 2019 and save as plain text.
Usage: python3 -I 09_pull_earnings_exhibits.py <company> [<company>...]"""
import json, os, re, sys, time, urllib.request, html
UA='NikeCaseCompResearch research-bot admin@example.org'
B='/home/user/nike-research-case-comp/data/hunt/peers_reported'
CIK={'deckers':910521,'vf':103379,'on':1858985,'skechers':1065837,'underarmour':1336917,'lululemon':1397187,'nike':320187,'amer':1988894,'birkenstock':1977102}
def get(u):
    for k in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=60) as r: return r.read()
        except Exception as e: print('ERR',u,e); time.sleep(2)
def text(b):
    s=b.decode('utf-8','ignore'); s=re.sub(r'(?is)<(script|style).*?</\1>',' ',s)
    s=re.sub(r'(?i)</(p|div|tr|br|li|h\d)>','\n',s); s=re.sub(r'(?i)<br\s*/?>','\n',s); s=re.sub(r'(?i)</t[dh]>',' | ',s)
    s=re.sub(r'<[^>]+>',' ',s); s=html.unescape(s); s=re.sub(r'[ \t\xa0]+',' ',s); s=re.sub(r'\n\s*\n+','\n',s); return s
for co in sys.argv[1:]:
    out=f'{B}/raw/releases_{co}'; os.makedirs(out,exist_ok=True)
    s=json.load(open(f'{B}/raw/sec_companyfacts/{co}_submissions.json'))
    recs=[]
    def add(bl):
        for i in range(len(bl['form'])): recs.append({k:bl[k][i] for k in ('form','filingDate','accessionNumber','items','primaryDocument')})
    add(s['filings']['recent'])
    for f in s['filings'].get('files',[]):
        b=get('https://data.sec.gov/submissions/'+f['name']); time.sleep(0.3)
        if b: add(json.loads(b))
    for r in recs:
        if r['filingDate']<'2019-01-01': continue
        if not ((r['form']=='8-K' and '2.02' in r['items']) or (co in ('on','amer','birkenstock') and r['form']=='6-K')): continue
        acc=r['accessionNumber'].replace('-','')
        dest=f"{out}/{r['filingDate']}_{acc}.txt"
        if os.path.exists(dest): continue
        idx=get(f"https://www.sec.gov/Archives/edgar/data/{CIK[co]}/{acc}/index.json"); time.sleep(0.3)
        if not idx: continue
        items=json.loads(idx)['directory']['item']
        ex=[i['name'] for i in items if re.search(r'(ex|exhibit)[-_ ]?99([-_.]?0?1)?(?![-_.]?[2-9])|ex991|er\.htm|pressrelease|press', i['name'],re.I) and i['name'].endswith(('.htm','.html'))]
        if not ex and co in ('on','amer','birkenstock'): ex=[i['name'] for i in items if i['name'].endswith('.htm') and i['name']!=r['primaryDocument']]
        if not ex: continue
        b=get(f"https://www.sec.gov/Archives/edgar/data/{CIK[co]}/{acc}/{ex[0]}"); time.sleep(0.3)
        if not b: continue
        t=text(b)
        if co in ('on','amer','birkenstock') and not re.search(r'net sales|revenue',t,re.I): continue
        open(dest,'w').write(f"SOURCE https://www.sec.gov/Archives/edgar/data/{CIK[co]}/{acc}/{ex[0]}\n"+t)
        print(co,r['filingDate'],ex[0],len(t))
