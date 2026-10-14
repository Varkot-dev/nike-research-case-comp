"""Parse adidas quarterly results releases (pdftotext -layout) into tidy rows.
First regional table in each release = the quarter (Q4 for FY releases). Columns: current, prior, reported change, currency-neutral change."""
import re, glob, os, csv, sys
T='/home/user/nike-research-case-comp/data/hunt/peers_reported/raw/adidas_text'
REG=['EMEA','Europe','North America','Asia-Pacific','Greater China','Russia/CIS','Latin America','Emerging Markets','Japan/South Korea','Other Businesses']
NUM=r'\(?-?[\d,\.]+\s*%?\)?'
def pnum(s):
    s=s.replace(',','').replace(' ','').replace('%','')
    neg=s.startswith('(') or s.startswith('-'); s=s.strip('()-')
    try: v=float(s)
    except: return None
    return -v if neg else v
def qid(fn):
    f=fn.lower()
    m=re.search(r'(20\d\d)_?q([1-3])|q([1-3])_?(20\d\d)',f)
    if m: y=m.group(1) or m.group(4); q=m.group(2) or m.group(3); return int(y),int(q)
    m=re.search(r'fy_?(20\d\d)|(20\d\d)_?fy',f)
    if m: return int(m.group(1) or m.group(2)),4
    return None
rows=[]
for fn in sorted(glob.glob(T+'/*.txt')):
    b=os.path.basename(fn).lower()
    if 'supplement' in b or 'preliminary' in b: continue
    q=qid(b)
    if not q: print('skip',b); continue
    y,qq=q; L=open(fn,encoding='utf-8',errors='ignore').read().splitlines()
    blocks=[]; cur=[]; last=-5
    for i,l in enumerate(L):
        m=re.match(r'^\s*('+'|'.join(re.escape(r) for r in REG)+r')\s{2,}(.*)$',l)
        if not m: continue
        toks=re.findall(r'\([\d,\.]+\s*%?\)|-?[\d,\.]+\s*%?',m.group(2))
        if len(toks)<4: continue
        if i-last>3 and cur: blocks.append(cur); cur=[]
        cur.append((i,m.group(1),toks)); last=i
    if cur: blocks.append(cur)
    blocks=[b for b in blocks if len(b)>=3]
    if not blocks: continue
    if qq==4:
        blk=min(blocks,key=lambda b: sum(pnum(t[2][0]) or 0 for t in b))
    else: blk=blocks[0]
    seen=set()
    for i,reg,toks in blk:
        if reg in seen: continue
        seen.add(reg)
        rows.append(dict(company='adidas',year=y,quarter=qq,metric='net_sales_region',region=reg,value=pnum(toks[0]),prior=pnum(toks[1]),
             yoy_reported_pct=pnum(toks[2]),yoy_cn_pct=pnum(toks[3]),unit='EUR m',source=os.path.basename(fn),line=i+1))
    # group sales, gm, inventory
    txt='\n'.join(L)
    m=re.search(r'^\s*Net sales\s{2,}([\d,]+)\s+([\d,]+)\s+(\(?-?[\d\.]+\s*%?\)?)',txt,re.M)
    if m: rows.append(dict(company='adidas',year=y,quarter=qq,metric='net_sales',region='Total',value=pnum(m.group(1)),prior=pnum(m.group(2)),yoy_reported_pct=pnum(m.group(3)),yoy_cn_pct=None,unit='EUR m',source=os.path.basename(fn),line=txt[:m.start()].count('\n')+1))
    m=re.search(r'^\s*Gross profit\s{2,}([\d,]+)\s+([\d,]+)\s+(\(?-?[\d\.]+\s*%?\)?)',txt,re.M)
    if m: rows.append(dict(company='adidas',year=y,quarter=qq,metric='gross_profit',region='Total',value=pnum(m.group(1)),prior=pnum(m.group(2)),yoy_reported_pct=pnum(m.group(3)),yoy_cn_pct=None,unit='EUR m',source=os.path.basename(fn),line=txt[:m.start()].count('\n')+1))
    m=re.search(r'^\s*Inventories\s{2,}([\d,]+)\s+([\d,]+)\s+(\(?-?[\d\.]+\)?)',txt,re.M)
    if m: rows.append(dict(company='adidas',year=y,quarter=qq,metric='inventory',region='Total',value=pnum(m.group(1)),prior=pnum(m.group(2)),yoy_reported_pct=pnum(m.group(3)),yoy_cn_pct=None,unit='EUR m',source=os.path.basename(fn),line=txt[:m.start()].count('\n')+1))
out='/home/user/nike-research-case-comp/data/hunt/peers_reported/adidas_quarterly_extract.csv'
with open(out,'w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
import collections
c=collections.defaultdict(list)
for r in rows: c[(r['year'],r['quarter'])].append(r['metric'][:3]+':'+r['region'][:5])
for k in sorted(c): print(k,len(c[k]),c[k])
