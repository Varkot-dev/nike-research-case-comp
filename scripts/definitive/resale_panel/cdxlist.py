import sys,subprocess,time,json,urllib.parse
out=sys.argv[1]
for pref in sys.argv[2:]:
    q="https://web.archive.org/cdx/search/cdx?"+urllib.parse.urlencode({'url':pref,'matchType':'prefix','output':'json','fl':'original,timestamp','collapse':'urlkey','filter':'statuscode:200','from':'2023'})
    for att in range(4):
        r=subprocess.run(['curl','-sS','-m','120','-A','Mozilla/5.0','-w','\n%{http_code}',q],capture_output=True,text=True)
        body,code=r.stdout.rsplit('\n',1) if '\n' in r.stdout else (r.stdout,'0')
        if code=='200': break
        print('retry',pref,code,r.stderr[:100],flush=True); time.sleep(30*(att+1))
    fn=out+'/'+pref.replace('/','_').replace('*','')+'.json'
    open(fn,'w').write(body)
    try: print(pref,len(json.loads(body)),flush=True)
    except Exception: print(pref,'bad',body[:200])
    time.sleep(7)
