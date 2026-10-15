# Pool Common Crawl product captures by host and calendar window; unique (brand,id) per host-window.
# usage: python3 -I cc_yearly.py <dir with host__CRAWL.jsonl.gz> <out csv>
import gzip,glob,json,re,os,sys,csv,collections
from urllib.parse import unquote
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
d,out=sys.argv[1],sys.argv[2]
BR=[('air-jordan','jordan'),('jordan','jordan'),('nike','nike'),('adidas','adidas'),('new-balance','new_balance'),('hoka','hoka'),('on-running','on'),('asics','asics'),('converse','converse'),('puma','puma')]
def brand(s):
    s=s.lower()
    for p,b in BR:
        if s.startswith(p): return b
    return 'other'
RX={'nordstromrack':r'/s/([^/?]+)/(\d+)','dsw':r'/product/([^/?]+)/(\d+)','academy':r'/p/([^/?]+)-(\d{6,})','famousfootwear':r'/product/([^/?]+)-(\d{5,8})','6pm':r'/p/([^/?]+)/product/(\d+)','saksoff5th':r'/product/(.+)-(\d{10,})\.html'}
def window(c):
    y=int(c[8:12]); w=int(c[13:])
    if 33<=w<=44: return f'{y} Aug-Oct (wk33-44)'
    return None
seen=collections.defaultdict(set); per=collections.defaultdict(list)
for f in sorted(glob.glob(os.path.join(d,'*__CC-MAIN-*.jsonl.gz'))):
    host,crawl=os.path.basename(f)[:-9].split('__')
    if host not in RX: continue
    wn=window(crawl)
    if not wn: continue
    for line in gzip.open(f,'rt'):
        try:j=json.loads(line)
        except Exception: continue
        m=re.search(RX[host],unquote(j['url']))
        if not m: continue
        seen[(host,wn)].add((brand(m.group(1)),m.group(1),m.group(2)))
    per[(host,wn)].append(crawl)
rows=[]
for (host,wn),S in sorted(seen.items()):
    c=collections.Counter(b for b,_,_ in S); tot=sum(c.values())
    r=[host,wn,'+'.join(x[8:] for x in per[(host,wn)]),tot]
    for b in ['nike','jordan','adidas','new_balance','hoka','on','asics']: r+= [c[b],round(100*c[b]/tot,3)]
    r.append(round(c['nike']/c['adidas'],3) if c['adidas'] else '')
    rows.append(r)
with open(out,'w',newline='') as o:
    w=csv.writer(o); w.writerow(['host','window','crawls','total_unique','nike_n','nike_pct','jordan_n','jordan_pct','adidas_n','adidas_pct','nb_n','nb_pct','hoka_n','hoka_pct','on_n','on_pct','asics_n','asics_pct','nike_over_adidas'])
    w.writerows(rows)
for r in rows: print(r)
