"""Parse On Holding quarterly 6-K press releases (Ex.99.1 text): regional net sales and growth (first bullet = quarter),
constant-currency growth when printed, gross margin, inventory (NWC table, yoy %). Quarter assigned from filing month."""
import re, glob, os, csv
B='/home/user/nike-research-case-comp/data/hunt/peers_reported'
rows=[]
def num(s): return float(s.replace(',','').rstrip('.'))
def qmap(d):
    y,m=int(d[:4]),int(d[5:7])
    return {2:(y-1,4),3:(y-1,4),4:(y-1,4),5:(y,1),8:(y,2),10:(y,3),11:(y,3)}.get(m)
seen=set()
for fn in sorted(glob.glob(B+'/raw/releases_on/*.txt')):
    t=open(fn).read(); d=os.path.basename(fn)[:10]; qq=qmap(d)
    if not qq or qq in seen: continue
    m=re.search(r'net sales in ([A-Za-z ,\-\(\)"“”]+?) (increased|grew|decreased)( by)? (.+?);',t)
    if not m: continue
    seen.add(qq); y,q=qq; src=t.splitlines()[0].replace('SOURCE ','')
    grp=m.group(1).replace("Europe, Middle East and Africa","EMEA")
    names=[re.sub(r'\s*\(.*?\)|[“”"]','',x).strip() for x in re.split(r',\s*(?:and\s+)?|\s+and\s+',grp) if x.strip()]
    pairs=re.findall(r'(\(?-?[\d\.]+\)?)% to (?:CHF )?([\d,\.]+)',m.group(4))
    m2=re.compile(r'net sales in [^;]*? by ([^;]*?) on a constant currency basis').search(t,m.end(),m.end()+600)
    cc=re.findall(r'(-?[\d\.]+)%',m2.group(1)) if m2 else []
    sign=-1 if m.group(2)=='decreased' else 1
    for i,(g,v) in enumerate(pairs):
        nm=names[i] if i<len(names) else f'r{i}'
        nm={'Europe, Middle East and Africa':'EMEA','Europe':'EMEA (Europe pre-2023)','APAC':'Asia-Pacific'}.get(nm,nm)
        rows.append(dict(company='on',year=y,quarter=q,metric='net_sales_region',region=nm,value=num(v),yoy_reported_pct=sign*float(g.strip('()')),yoy_cn_pct=float(cc[i]) if i<len(cc) else None,unit='CHF m',source=src))
    m=re.search(r'net sales (?:increased|grew)(?: by)? ([\d\.]+)% to (?:a record )?(?:of )?CHF ([\d,\.]+) million',t)
    if m: rows.append(dict(company='on',year=y,quarter=q,metric='net_sales',region='Total',value=num(m.group(2)),yoy_reported_pct=float(m.group(1)),yoy_cn_pct=None,unit='CHF m',source=src))
    m=re.search(r'gross profit margin (?:increased|decreased|was|reached|of|improved)[^\d]{0,30}([\d\.]+)%(?: from| compared to)?[^\d]{0,20}([\d\.]+)%',t)
    if m: rows.append(dict(company='on',year=y,quarter=q,metric='gross_margin_pct',region='Total',value=float(m.group(1)),yoy_reported_pct=float(m.group(2)),yoy_cn_pct=None,unit='% (prior in yoy col)',source=src))
    inv=re.findall(r'Inventories \| \| ([\d,\.]+) \| \| \| ([\d,\.]+) \|[ |]*\(?(-?[\d\.]+)\)? \| %',t)
    if inv:
        a,b_,c=inv[-1]; f=1000 if ',' in a and num(a)>5000 else 1
        rows.append(dict(company='on',year=y,quarter=q,metric='inventory',region='Total',value=num(a)/f,yoy_reported_pct=round((num(a)/num(b_)-1)*100,1),yoy_cn_pct=None,unit='CHF m',source=src))
with open(B+'/on_quarterly_extract.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['company','year','quarter','metric','region','value','yoy_reported_pct','yoy_cn_pct','unit','source']); w.writeheader(); w.writerows(rows)
for r in rows:
    if r['metric']!='net_sales_region' or r['region']=='Americas': print(r['year'],r['quarter'],r['metric'],r['region'],r['value'],r['yoy_reported_pct'],r['yoy_cn_pct'])
