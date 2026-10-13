import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import wbrate
import json,re,subprocess,time,urllib.parse,os
P='/tmp/claude-0/-home-user-nike-research-case-comp/c6360f77-8844-5e04-9011-d8ceb3c498c8/scratchpad/dt/resale_panel'
shoes=json.load(open(P+'/match_cands.json'))
outf=P+'/cdx_by_shoe.json'
res=json.load(open(outf)) if os.path.exists(outf) else {}
base={'AJ1 High OG':'air-jordan-1-retro-high-og-','AJ3':'air-jordan-3-retro-','AJ4':'air-jordan-4-retro-','AJ5':'air-jordan-5-retro-','AJ11':'air-jordan-11-retro-'}
def sl(x): return re.sub(r'[^a-z0-9]+','-',x.lower().replace("'",'').replace('&','').replace('’','')).strip('-')
def cdx(prefix):
    q="https://web.archive.org/cdx/search/cdx?"+urllib.parse.urlencode({'url':'stockx.com/'+prefix,'matchType':'prefix','output':'json','fl':'original,timestamp,statuscode,mimetype','from':'2023','limit':'5000'})
    for att in range(5):
        wbrate.wait()
        r=subprocess.run(['curl','-sS','-m','40','-A','Mozilla/5.0','-w','\n%{http_code}',q],capture_output=True,text=True)
        body,code=(r.stdout.rsplit('\n',1)+['0'])[:2]
        if code=='200':
            try: return json.loads(body)[1:] if body.strip() else []
            except Exception: return []
        print('retry',prefix,code,flush=True); time.sleep(30*(att+1))
    return None
kid=re.compile(r'-(gs|ps|td|td9|td9a|bt|bp)$')

def prio(s):
    l=s['line']; y=s['release_date'][:4]
    if l in('AJ4','AJ3') and y<='2025': return (0, 0 if l=='AJ4' else 1, s['release_date'])
    if l=='AJ1 High OG' and y>='2024': return (1,0,s['release_date'])
    if l in('AJ4','AJ3'): return (2,0,s['release_date'])
    return (3,0,s['release_date'])
for s in sorted(shoes,key=prio):
    k=s['goat_id']
    if k in res: continue
    m=re.findall(r"'([^']+)'",s['name']); nick=sl(m[-1]) if m else ''
    nick=re.sub(r'-(19|20)\d\d$','',nick)
    prefixes=[base[s['line']]+nick]
    for c in s['cands'][:3]:
        if not kid.search(c) and not any(c.startswith(p) for p in prefixes): prefixes.append(c)
    rows=[]
    for p in prefixes:
        r=cdx(p)
        if r: rows+= [x for x in r if x[2]=='200']
    res[k]={'prefixes':prefixes,'rows':rows}
    print(k,s['line'],s['name'][:40],prefixes,len(rows),flush=True)
    json.dump(res,open(outf,'w'))
