"""usage: python3 -I cdx_pages.py <outprefix> <urlprefix> <pages comma list>  ; curl with backoff, 7s spacing"""
import sys, subprocess, time, os
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
out, pref, pages = sys.argv[1], sys.argv[2], [int(x) for x in sys.argv[3].split(",")]
for p in pages:
    f=f"{out}_p{p}.txt"
    for a in range(6):
        time.sleep(7)
        cp=subprocess.run(["curl","-s","-A",UA,"-o",f+".part","-w","%{http_code}","--max-time","180",
          f"https://web.archive.org/cdx/search/cdx?url={pref}&matchType=prefix&fl=timestamp,original,statuscode&from=2023&filter=statuscode:200&page={p}"],capture_output=True,text=True)
        st=cp.stdout.strip()
        if st=="200":
            os.replace(f+".part",f); print(p,"ok",sum(1 for _ in open(f)),flush=True); break
        print(p,"status",st,"retry",a,flush=True); time.sleep(30*(a+1))
