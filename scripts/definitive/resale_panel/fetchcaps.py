import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import wbrate
import json,re,subprocess,time,os,sys,datetime as dt
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from sxparse import parse
P='/tmp/claude-0/-home-user-nike-research-case-comp/c6360f77-8844-5e04-9011-d8ceb3c498c8/scratchpad/dt/resale_panel'
shoes={s['goat_id']:s for s in json.load(open(P+'/match_cands.json'))}
outf=P+'/caps_parsed.json'
res=json.load(open(outf)) if os.path.exists(outf) else {}
RAW=P+'/dl/wb'; os.makedirs(RAW,exist_ok=True)
kid=re.compile(r'-(gs|ps|td|td9|td9a|bt|bp|golf)(-|$)|golf')
def D(s): return dt.date(int(s[:4]),int(s[4:6]),int(s[6:8])) if len(s)>=8 and s[4]!='-' else dt.date.fromisoformat(s[:10])
targets_rel=[('d90',90,14,200),('d365',365,271,500)]
cal=['2024-10-15','2025-10-15']
def fetch(ts,orig):
    u=f"https://web.archive.org/web/{ts}id_/{orig}"
    fn=f"{RAW}/{re.sub(r'[^A-Za-z0-9]+','_',orig.split('stockx.com/')[1])[:80]}_{ts}.html"
    if os.path.exists(fn) and os.path.getsize(fn)>1000: return u,fn,open(fn,'rb').read()
    for att in range(4):
        wbrate.wait()
        r=subprocess.run(['curl','-sS','-m','60','-A','Mozilla/5.0','-o',fn,'-w','%{http_code}',u],capture_output=True,text=True)
        if r.stdout=='200': return u,fn,open(fn,'rb').read()
        print('  http',r.stdout,r.stderr[:80],flush=True); time.sleep(30*(att+1) if r.stdout in('429','000','503') else 6)
        if r.stdout in('404','403'): return u,fn,None
    return u,fn,None

def prio(s):
    l=s['line']; y=s['release_date'][:4]
    if l in('AJ4','AJ3') and y<='2025': return (0, 0 if l=='AJ4' else 1, s['release_date'])
    if l=='AJ1 High OG' and y>='2024': return (1,0,s['release_date'])
    if l in('AJ4','AJ3'): return (2,0,s['release_date'])
    return (3,0,s['release_date'])
def run(cdxf):
    cdx=json.load(open(cdxf))
    for gid,c in sorted(cdx.items(),key=lambda kv:prio(shoes[kv[0]])):
        if gid in res or prio(shoes[gid])[0]>=3: continue
        s=shoes[gid]; rel=D(s['release_date'])
        rows=[(o,t) for o,t,st,mt in c['rows'] if 'html' in mt]
        if not rows: res[gid]={'slug':None,'caps':[]}; continue
        bases={}
        for o,t in rows:
            b=o.split('stockx.com/')[1].split('?')[0].rstrip('/').lower()
            if kid.search(b): continue
            bases.setdefault(b,[]).append((o,t))
        if not bases: res[gid]={'slug':None,'caps':[]}; continue
        # verify slug: try bases ordered by capture count, check styleId
        good=None; caps=[]
        for b in sorted(bases,key=lambda b:-len(bases[b]))[:3]:
            o,t=sorted(bases[b],key=lambda x:x[1])[-1]
            u,fn,raw=fetch(t,o)
            p=parse(raw) if raw else {'err':'fetch'}
            sid=(p.get('styleId') or '').upper()
            print(gid,s['name'][:40],b,t,sid,s['style_code'],p.get('err'),flush=True)
            if sid and (sid==s['style_code'].upper() or sid.replace(' ','') in s['style_code'].upper() or s['style_code'].upper() in sid):
                good=b; caps.append(dict(target='latest',ts=t,url=u,file=fn,**p)); break
        if not good: res[gid]={'slug':None,'tried':list(bases)[:3],'caps':[]}; json.dump(res,open(outf,'w')); continue
        avail=sorted(bases[good],key=lambda x:x[1])
        want=[]
        for name,c0,lo,hi in targets_rel:
            tgt=rel+dt.timedelta(days=c0)
            cand=[(abs((D(t)-tgt).days),o,t) for o,t in avail if lo<=(D(t)-rel).days<=hi]
            if cand: want.append((name,)+min(cand)[1:])
        for cd in cal:
            tgt=dt.date.fromisoformat(cd)
            if tgt<rel+dt.timedelta(days=14): continue
            cand=[(abs((D(t)-tgt).days),o,t) for o,t in avail if abs((D(t)-tgt).days)<=45 and (D(t)-rel).days>=14]
            if cand: want.append(('cal'+cd[:7],)+min(cand)[1:])
        done={caps[0]['ts']:caps[0]}
        for name,o,t in want:
            if t in done: caps.append(dict(done[t],target=name)); continue
            u,fn,raw=fetch(t,o)
            p=parse(raw) if raw else {'err':'fetch'}
            rec=dict(target=name,ts=t,url=u,file=fn,**p); caps.append(rec); done[t]=rec
            print('   ',name,t,p.get('med_lastSale_7_13'),p.get('prod_nAsks'),p.get('err'),flush=True)
        res[gid]={'slug':good,'caps':caps}
        json.dump(res,open(outf,'w'))
import shutil
while True:
    try:
        shutil.copy(P+'/cdx_by_shoe.json',P+'/cdx_snap.json'); n=len(json.load(open(P+'/cdx_snap.json')))
    except Exception: time.sleep(20); continue
    run(P+'/cdx_snap.json')
    if n>=len(shoes): break
    time.sleep(60)
print('ALLDONE',flush=True)
