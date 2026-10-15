"""usage: python3 -I cdx_all.py <outprefix> <urlprefix> : fetch CDX pages 0.. until empty/400"""
import sys, subprocess, time, os
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
out, pref = sys.argv[1], sys.argv[2]
p=0
while p<60:
    f=f"{out}_p{p}.txt"; ok=False
    for a in range(5):
        time.sleep(7)
        cp=subprocess.run(["curl","-s","-A",UA,"-o",f,"-w","%{http_code}","--max-time","180",
          f"https://web.archive.org/cdx/search/cdx?url={pref}&matchType=prefix&fl=timestamp,original,statuscode&from=2023&filter=statuscode:200&page={p}"],capture_output=True,text=True)
        st=cp.stdout.strip()
        if st=="200": ok=True; break
        if st=="400": break
        time.sleep(30*(a+1))
    n=sum(1 for _ in open(f)) if ok else -1
    print(pref,p,st,n,flush=True)
    if not ok or n==0:
        if os.path.exists(f) and not ok: os.remove(f)
        break
    p+=1
