import csv,json,re,glob,sys
P='/tmp/claude-0/-home-user-nike-research-case-comp/c6360f77-8844-5e04-9011-d8ceb3c498c8/scratchpad/dt/resale_panel'
rows=list(csv.DictReader(open('/home/user/nike-research-case-comp/data/jordan_resale_goat_20261013.csv')))
slugs=set()
for f in glob.glob(P+'/dl/cdx/*.json'):
    try:
        for o,t in json.load(open(f))[1:]:
            s=o.split('stockx.com/')[1].split('?')[0].lower().rstrip('/')
            slugs.add(s)
    except Exception: pass
pref={'AJ1 High OG':['air-jordan-1-retro-high','air-jordan-1-high'],'AJ3':['air-jordan-3-retro'],'AJ4':['air-jordan-4-retro'],'AJ5':['air-jordan-5-retro'],'AJ11':['air-jordan-11-retro']}
def sl(x): return re.sub(r'[^a-z0-9]+','-',x.lower().replace("'",'').replace('&','')).strip('-')
out=[]
for r in rows:
    if r['line'] not in pref or r['collab_or_special']=='True': continue
    m=re.findall(r"'([^']+)'",r['name']); nick=sl(m[-1]) if m else ''
    yr=re.search(r"' (\d{4})$",r['name'])
    w=r['gender']!='men'
    cands=[s for s in slugs if any(s.startswith(p) for p in pref[r['line']]) and nick and nick in s]
    if r['line'].startswith('AJ1'): cands=[s for s in cands if 'low' not in s and 'mid' not in s and '85' not in s]
    if r['line'] in('AJ3','AJ4','AJ5','AJ11'): cands=[s for s in cands if '-low' not in s and '-gs' not in s and '-ps' not in s and '-td' not in s]
    cands=[s for s in cands if ('-w' in s.split(nick)[-1] or 'womens' in s)==w]
    out.append({'goat_id':r['goat_id'],'line':r['line'],'name':r['name'],'style_code':r['style_code'],'release_date':r['release_date'],'gender':r['gender'],'cands':sorted(cands,key=len)})
json.dump(out,open(P+'/match_cands.json','w'),indent=0)
n0=sum(1 for o in out if not o['cands']); print(len(out),'no cand',n0)
for o in out: print(o['line'],o['release_date'],o['name'][:55],'|',o['cands'][:4])
