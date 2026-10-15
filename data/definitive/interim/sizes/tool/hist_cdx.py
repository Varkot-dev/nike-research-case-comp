import csv, json, subprocess, sys, time, urllib.parse
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
rows=[r for r in csv.DictReader(open(sys.argv[1])) if r['listed']=='True']
out=open(sys.argv[2],'w')
for r in rows:
    for u,mt in [(f"nike.com/t/{r['slug']}/{r['style_code']}","exact"),(f"nike.com/launch/t/{r['slug'].rsplit('-',1)[0].replace('-mens-shoes','')}","prefix")]:
        q=urllib.parse.urlencode({"url":u,"matchType":mt,"output":"json","from":"2024","to":"2026","filter":"statuscode:200","limit":"500"})
        for a in range(3):
            p=subprocess.run(["curl","-s","--max-time","90","-A",UA,"https://web.archive.org/cdx/search/cdx?"+q],capture_output=True,text=True)
            if p.stdout.strip().startswith("[") or p.stdout.strip()=="" : break
            time.sleep(20)
        try: j=json.loads(p.stdout) if p.stdout.strip() else []
        except Exception: j=None
        n=len(j)-1 if j else 0
        out.write(json.dumps({"style_code":r['style_code'],"query":u,"match":mt,"n":n,"rows":j})+"\n"); out.flush()
        print(r['style_code'],mt,n,[x[1][:8] for x in (j or [])[1:]][:30],flush=True)
        time.sleep(7)
