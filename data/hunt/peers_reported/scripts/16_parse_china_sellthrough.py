"""Parse HKEX quarterly operational updates (Anta brand, FILA, Anta other brands, Li Ning overall platform,
Xtep core brand, Saucony China, Xtep retail discount and channel inventory turnover) into a tidy quarterly table.
Ranges in words are mapped to numeric midpoints (e.g. 'low-single-digit'=2.5, 'mid-teens'=15, '20-25%'=22.5)."""
import re, glob, os, csv
B='/home/user/nike-research-case-comp/data/hunt/peers_reported'
T=B+'/raw/hkex_text'
W={'flat':0,'low single digit':2.5,'mid single digit':5,'high single digit':8,'low teens':12,'low teen':12,'mid teens':15,'mid teen':15,'high teens':18,'high teen':18,
   'low twenties':22,'mid twenties':25,'high twenties':28,'low thirties':32,'mid thirties':35,'mid fifties':55,'mid forties':45,'low forties':42,'high forties':48,'low fifties':52}
def val(s):
    s=s.lower().replace('-',' ').replace('–',' ').replace('\u2014',' ')
    s=re.sub(r'\s+',' ',s)
    neg=bool(re.search(r'declin|decreas|negative|drop',s))
    m=re.search(r'(\d+)\s*%?\s*(?:to|  )\s*(\d+)\s*%',s) or re.search(r'(\d+)%?\s+(\d+)%',s)
    if m: v=(float(m.group(1))+float(m.group(2)))/2
    else:
        m=re.search(r'(?:more than|over|above|around|about)\s+(\d+)\s*%',s) or re.search(r'(\d+)\s*%\s*\+',s)
        if m: v=float(m.group(1))+(2.5 if re.search(r'more than|over|above|\+',s) else 0)
        else:
            v=None
            for k in sorted(W,key=len,reverse=True):
                if k in s: v=W[k]; break
            if v is None: return None,s[:80]
    return (-v if neg else v), s[:80]
def qof(title,txt):
    m=re.search(r'(FIRST|SECOND|THIRD|FOURTH) QUARTER (?:AND [A-Z ]+ )?(?:OF )?(20\d\d)',title.upper())
    if m: return int(m.group(2)),{'FIRST':1,'SECOND':2,'THIRD':3,'FOURTH':4}[m.group(1)]
    m=re.search(r'(?:three months|quarter) ended (\d+) (March|June|September|December) (20\d\d)',txt,re.I)
    if m: return int(m.group(3)),{'march':1,'june':2,'september':3,'december':4}[m.group(2).lower()]
    return None
man={}
for l in open(T+'/_manifest.tsv'):
    p=l.rstrip('\n').split('\t')
    if len(p)>=4: man[p[0][:-4]]=(p[2],p[3])
rows=[]
for fn in sorted(glob.glob(T+'/*.txt')):
    b=os.path.basename(fn)[:-4]
    co,_,fid=b.split('_',2); digits=re.sub(r'\D','',fid)
    url=f'https://www1.hkexnews.hk/listedco/listconews/sehk/{digits[:4]}/{digits[4:8]}/{fid}.pdf'
    title=man.get(b,('',''))[0]
    head=re.sub(r'\s+',' ',open(fn,errors='ignore').read()[:3000]).upper()
    if 'RESULTS ANNOUNCEMENT' in head[:1500] or 'CLARIFICATION' in head[:1500] or 'OPERATIONAL UPDATE' not in head: continue
    t=re.sub(r'\s+',' ',open(fn,errors='ignore').read())
    q=qof(title,t)
    if not q: continue
    y,qq=q
    def add(series,phrase,metric='retail_sellthrough_yoy_pct'):
        v,raw=val(phrase)
        if v is not None: rows.append(dict(series=series,cal_year=y,cal_q=qq,metric=metric,value=v,phrase=raw,source=url))
    if co=='anta':
        for brand,lab in (('ANTA','ANTA brand'),('FILA','FILA brand'),('all other','Anta other brands')):
            m=re.search(r'(?:For|In) the (?:first|second|third|fourth) quarter of 20\d\d,? retail (?:sales|amount)[^.]{0,80}?of '+brand+r'[^.]{0,40}?(?:products|brands?)\*?,? (?:recorded|achieved|registered|was|were)?\s*([^.]{0,90}?)(?:growth|decline|increase|as compared)',t,re.I)
            if m: add(lab,m.group(1)+(' decline' if re.search('decline|negative',m.group(0),re.I) else ''))
    elif co=='lining':
        m=re.search(r'(?:quarter ended|quarter of)[^.]{0,40}?retail sell-through of LI-NING POS[^.]{0,80}?(?:overall platform|whole platform)[^.]{0,10}?(recorded|registered|increased|decreased|declined|remained)([^.;]{0,80})',t,re.I)
        if m: add('Li Ning overall platform',m.group(1)+' '+m.group(2))
    elif co=='xtep':
        seg=t[:t.lower().find('six months ended')] if 'six months ended' in t.lower() else t
        def clean(x): return re.sub(r'\(?including|offline and online channels\)?|\(|\)','',x,flags=re.I)
        m=re.search(r'Retail sell-through growth(.{0,140}?)(?:Retail discount|Same store|SAUCONY|Channel inventory|Retail inventory|For the|The Company)',seg,re.I)
        if m: add('Xtep core brand',clean(m.group(1)))
        m=re.search(r'Retail discount level ([\d%\s–\-to]+|Around \d+%)',seg,re.I)
        if m: add('Xtep core brand','',None) if False else None
        if m:
            v,_=val(m.group(1).replace('Around','about')); 
            if v is not None: rows.append(dict(series='Xtep core brand',cal_year=y,cal_q=qq,metric='retail_discount_pct',value=abs(v),phrase=m.group(1),source=url))
        m=re.search(r'(?:Retail|Channel) inventory turnover (?:Around |About |Below |Approximately )?([\d\.]+)(?: to ([\d\.]+))? months',t,re.I)
        if m:
            v=(float(m.group(1))+float(m.group(2) or m.group(1)))/2
            rows.append(dict(series='Xtep core brand',cal_year=y,cal_q=qq,metric='channel_inventory_turnover_months',value=v,phrase=m.group(0)[:60],source=url))
        m=re.search(r'SAUCONY Retail sell-through growth(.{0,140}?)(?:OPERATIONAL|The Company|For the|–\d)',seg,re.I)
        if m: add('Saucony (China)',clean(m.group(1)))
with open(B+'/china_peers_sellthrough_quarterly.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['series','cal_year','cal_q','metric','value','phrase','source']); w.writeheader(); w.writerows(sorted(rows,key=lambda r:(r['series'],r['metric'],r['cal_year'],r['cal_q'])))
import collections
c=collections.defaultdict(list)
for r in rows: c[(r['series'],r['metric'])].append((r['cal_year'],r['cal_q'],r['value']))
for k,v in sorted(c.items()): print(k,len(v),sorted(v)[-8:])
