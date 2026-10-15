# Today's (2026-10-15) sitemap census of brand shares. usage: python3 -I sitemap_snapshot.py <dir with downloaded sitemaps> <out csv>
import re,glob,gzip,collections,csv,sys,os
d=sys.argv[1]; os.chdir(d)
def rd(f):
    b=open(f,'rb').read()
    try:b=gzip.decompress(b)
    except Exception:pass
    return b.decode('utf8','replace')
def brand(s):
    s=s.lower()
    for p,b in [('air-jordan','jordan'),('jordan','jordan'),('nike','nike'),('adidas','adidas'),('new-balance','new_balance'),('hoka','hoka'),('on-running','on'),('asics','asics'),('converse','converse'),('puma','puma'),('under-armour','under_armour'),('reebok','reebok'),('skechers','skechers'),('saucony','saucony'),('brooks','brooks'),('vans','vans')]:
        if s.startswith(p): return b
    return 'other'
FW=re.compile(r'shoe|sneaker|boot|cleat|slide|sandal|trainer|runner|running|clog|slipper|dunk|air-max|air-force|pegasus|vomero|samba|gazelle|campus|990|530|clifton|cloud|gel-')
sites=[('nordstromrack','nr*.xml',r'/s/([^/]+)/(\d+)$'),('dsw','dsw?.xml',r'/product/([^/?]+)/(\d+)$'),('academy','ac?.gz',r'/p/([^/]+)()$')]
rows=[]
for site,gl,rx in sites:
    seen=set(); c=collections.Counter(); cf=collections.Counter()
    for f in sorted(glob.glob(gl)):
        for m in re.finditer(r'<loc>([^<]*)</loc>',rd(f)):
            u=m.group(1); mm=re.search(rx,u)
            if not mm: continue
            key=(mm.group(1),mm.group(2)) if mm.group(2) else u
            if key in seen: continue
            seen.add(key); b=brand(mm.group(1)); c[b]+=1
            if FW.search(mm.group(1)): cf[b]+=1
    tot=sum(c.values()); totf=sum(cf.values())
    for b in ['nike','jordan','converse','adidas','new_balance','hoka','on','asics','puma','under_armour','reebok','skechers','saucony','brooks','vans','other']:
        rows.append([site,'2026-10-15',b,c[b],round(c[b]/tot*100,3),cf[b],round(cf[b]/totf*100,3) if totf else 0,tot,totf])
with open(sys.argv[2],'w',newline='') as o:
    w=csv.writer(o); w.writerow(['site','date','brand','n_products_all','share_all_pct','n_footwear_slug','share_footwear_slug_pct','site_total_all','site_total_footwear_slug']); w.writerows(rows)
