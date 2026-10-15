"""Download XBRL instance documents (extracted *_htm.xml) for every 10-Q/10-K (and XBRL 6-K/20-F for foreign filers)
from 2019-01-01 onward. Instances go to scratchpad (large); parsed extracts are written by 04_parse_segments.py.
Generic User-Agent, no personal data, 0.25s sleep between requests."""
import json, os, sys, time, urllib.request
UA='NikeCaseCompResearch research-bot admin@example.org'
RAW='/home/user/nike-research-case-comp/data/hunt/peers_reported/raw/sec_companyfacts'
OUT=sys.argv[1] if len(sys.argv)>1 else '/tmp/claude-0/-home-user-nike-research-case-comp/2bf9f309-3096-5c65-b9c3-02b984182743/scratchpad/xbrl'
os.makedirs(OUT,exist_ok=True)
CIK={'nike':320187,'deckers':910521,'lululemon':1397187,'vf':103379,'underarmour':1336917,'skechers':1065837,'on':1858985,'crocs':1334036,'amer':1988894,'birkenstock':1977102,'columbia':1050797}
def get(url):
    req=urllib.request.Request(url,headers={'User-Agent':UA})
    for k in range(3):
        try:
            with urllib.request.urlopen(req,timeout=60) as r: return r.read()
        except Exception as e:
            print('ERR',url,e); time.sleep(2)
    return None
only=sys.argv[2:] or list(CIK)
log=open(OUT+'/manifest.tsv','a')
for c in only:
    cik=CIK[c]; s=json.load(open(f'{RAW}/{c}_submissions.json'))
    recs=[]
    def add(block):
        for i in range(len(block['form'])):
            recs.append({k:block[k][i] for k in ('form','filingDate','reportDate','accessionNumber','primaryDocument','isXBRL')})
    add(s['filings']['recent'])
    for f in s['filings'].get('files',[]):
        b=get('https://data.sec.gov/submissions/'+f['name']); time.sleep(0.25)
        if b: add(json.loads(b))
    for r in recs:
        if r['filingDate']<'2019-03-01' or not r['isXBRL']: continue
        if r['form'] not in ('10-Q','10-K','6-K','20-F','10-KT'): continue
        acc=r['accessionNumber'].replace('-','')
        dest=f"{OUT}/{c}_{r['reportDate']}_{r['form']}_{acc}.xml"
        if os.path.exists(dest): continue
        idx=get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{acc}/index.json'); time.sleep(0.25)
        if not idx: continue
        names=[x['name'] for x in json.loads(idx)['directory']['item']]
        inst=[n for n in names if n.endswith('_htm.xml')] or [n for n in names if n.endswith('.xml') and not any(t in n for t in ('_cal','_def','_lab','_pre','FilingSummary','MetaLinks'))]
        if not inst: print('noinst',c,r['form'],r['reportDate']); continue
        b=get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{acc}/{inst[0]}'); time.sleep(0.25)
        if b:
            open(dest,'wb').write(b); log.write(f"{c}\t{r['form']}\t{r['filingDate']}\t{r['reportDate']}\thttps://www.sec.gov/Archives/edgar/data/{cik}/{acc}/{inst[0]}\n"); log.flush()
            print(c,r['form'],r['reportDate'],len(b))
