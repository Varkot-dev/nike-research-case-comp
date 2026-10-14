"""HKEXnews title search (public JSON endpoint behind the search page) for Chinese sportswear peers.
Downloads quarterly operational updates and interim/annual results announcements (PDF) to scratchpad, text to raw/hkex_text."""
import json, os, re, sys, time, urllib.request, urllib.parse, subprocess
UA='Mozilla/5.0 (research script)'
B='/home/user/nike-research-case-comp/data/hunt/peers_reported'
PDF=sys.argv[1]; os.makedirs(PDF,exist_ok=True); TXT=B+'/raw/hkex_text'; os.makedirs(TXT,exist_ok=True)
IDS={'anta':16111,'lining':7647,'xtep':23896,'361':34919,'topsports':1000010460,'pousheng':23491}
QUERIES={'anta':['operational update','results announcement'],'lining':['operational update','retail','results announcement'],'xtep':['operational update','results announcement'],'361':['operational update','retail operation','results announcement'],'topsports':['operational update','results announcement'],'pousheng':['results announcement']}
def get(u):
    with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=60) as r: return r.read()
man=open(TXT+'/_manifest.tsv','a')
for co,sid in IDS.items():
    for q in QUERIES[co]:
        p=dict(sortDir=0,sortByOptions='DateTime',category=0,market='SEHK',stockId=sid,documentType=-1,fromDate='20180101',toDate='20261014',title=q,searchType=0,t1code=-2,t2Gcode=-2,t2code=-2,rowRange=300,lang='E')
        try: res=json.loads(json.loads(get('https://www1.hkexnews.hk/search/titleSearchServlet.do?'+urllib.parse.urlencode(p)))['result'])
        except Exception as e: print('ERR',co,q,e); continue
        time.sleep(1)
        for r in res:
            t=r['TITLE'].upper()
            if 'RESULTS ANNOUNCEMENT' in q.upper() and not re.search(r'(INTERIM|ANNUAL) RESULTS ANNOUNCEMENT|RESULTS ANNOUNCEMENT FOR THE (YEAR|SIX MONTHS)',t): continue
            if 'RESULTS' in q.upper() and ('DATE' in t or 'BOARD MEETING' in t): continue
            link=r['FILE_LINK']
            if not link.lower().endswith('.pdf'): continue
            d=r['DATE_TIME'][6:10]+r['DATE_TIME'][3:5]+r['DATE_TIME'][0:2]
            name=f"{co}_{d}_{os.path.basename(link)}"
            if os.path.exists(f'{TXT}/{name[:-4]}.txt'): continue
            try: b=get('https://www1.hkexnews.hk'+link)
            except Exception as e: print('ERR',link,e); continue
            open(f'{PDF}/{name}','wb').write(b); time.sleep(1)
            subprocess.run(['pdftotext','-layout',f'{PDF}/{name}',f'{TXT}/{name[:-4]}.txt'],stderr=subprocess.DEVNULL)
            man.write(f"{name}\t{r['DATE_TIME']}\t{r['TITLE']}\thttps://www1.hkexnews.hk{link}\n"); man.flush()
            print(co,d,r['TITLE'][:90])
