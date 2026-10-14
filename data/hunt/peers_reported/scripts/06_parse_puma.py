"""Parse Puma quarterly releases/statements (pdftotext -layout). First regional table = quarter.
Columns: current, prior, reported change, currency-adjusted change."""
import re, glob, os, csv
T='/home/user/nike-research-case-comp/data/hunt/peers_reported/raw/puma_text'
REG=['EMEA','Americas','Asia/Pacific']
def pnum(s):
    s=s.replace(',','').replace('%','').strip(); neg=s.startswith('-') or s.startswith('('); s=s.strip('()-')
    try: return -float(s) if neg else float(s)
    except: return None
def qid(b):
    if '2025-1-22' in b: return None  # preliminary FY2024, duplicate of full Q4 release
    y=re.search(r'(20\d\d)',b.replace('2019-07-31','2019')).group(1)
    m=re.search(r'q([1-4])',b); return int(y),int(m.group(1))
rows=[]
for fn in sorted(glob.glob(T+'/*.txt')):
    b=os.path.basename(fn); q=qid(b)
    if not q: continue
    y,qq=q; L=open(fn,errors='ignore').read().splitlines(); txt='\n'.join(L); seen=set()
    for i,l in enumerate(L):
        m=re.match(r'^\s*(EMEA|Americas|Asia/Pacific)\s{2,}(.*)$',l)
        if not m or m.group(1) in seen: continue
        toks=re.findall(r'-?[\d,]+\.\d+%?|-?\d+\.\d%',m.group(2))
        if len(toks)<4: continue
        seen.add(m.group(1))
        rows.append(dict(company='puma',year=y,quarter=qq,metric='net_sales_region',region=m.group(1),value=pnum(toks[0]),prior=pnum(toks[1]),yoy_reported_pct=pnum(toks[2]),yoy_cn_pct=pnum(toks[3]),unit='EUR m',source=b,line=i+1))
    m=re.search(r'^\s*Sales\s{2,}([\d,]+\.\d)\s+([\d,]+\.\d)\s+(-?[\d\.]+)%',txt,re.M)
    if m: rows.append(dict(company='puma',year=y,quarter=qq,metric='net_sales',region='Total',value=pnum(m.group(1)),prior=pnum(m.group(2)),yoy_reported_pct=pnum(m.group(3)),yoy_cn_pct=None,unit='EUR m',source=b,line=txt[:m.start()].count('\n')+1))
    m=re.search(r'^\s*Gross profit\s{2,}([\d,]+\.\d)\s+([\d,]+\.\d)',txt,re.M)
    if m: rows.append(dict(company='puma',year=y,quarter=qq,metric='gross_profit',region='Total',value=pnum(m.group(1)),prior=pnum(m.group(2)),yoy_reported_pct=None,yoy_cn_pct=None,unit='EUR m',source=b,line=txt[:m.start()].count('\n')+1))
    m=re.search(r'^\s*Inventories\s*\*?\s{2,}([\d,]+\.\d)\s+([\d,]+\.\d)\s+(-?[\d\.]+)%',txt,re.M)
    if m: rows.append(dict(company='puma',year=y,quarter=qq,metric='inventory',region='Total',value=pnum(m.group(1)),prior=pnum(m.group(2)),yoy_reported_pct=pnum(m.group(3)),yoy_cn_pct=None,unit='EUR m',source=b,line=txt[:m.start()].count('\n')+1))
with open('/home/user/nike-research-case-comp/data/hunt/peers_reported/puma_quarterly_extract.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
import collections; c=collections.defaultdict(list)
for r in rows: c[(r['year'],r['quarter'])].append(r['metric'][:5]+(r['region'][:3] if r['region']!='Total' else ''))
for k in sorted(c): print(k,c[k])
