"""Polite cached fetcher. usage: python3 -I fetch.py <outdir> <url> [<url>...]  (or urls from stdin with '-')"""
import sys, os, time, hashlib, json, urllib.parse
import requests
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
STATE="/tmp/claude-0/-home-user-nike-research-case-comp/97c520cc-64e5-53f3-8fe9-898f5b11e054/scratchpad/marketplace/data/fetch_log.jsonl"
last={}
CURL_HOSTS=("web.archive.org","footlocker.com","poshmark.com","runningwarehouse.com","on.com/")
def fname(url):
    return hashlib.sha1(url.encode()).hexdigest()[:16]+".html"
def get(url,outdir,delay=None,retries=4):
    if delay is None: delay=8 if "archive.org" in url else 2.5
    os.makedirs(outdir,exist_ok=True)
    p=os.path.join(outdir,fname(url))
    if os.path.exists(p) and os.path.getsize(p)>500: return p,"cached"
    host=urllib.parse.urlparse(url).netloc
    for a in range(retries+1):
        w=last.get(host,0)+delay-time.time()
        if w>0: time.sleep(w)
        try:
            hd={"User-Agent":UA,"Accept":"text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8","Accept-Language":"en-US,en;q=0.9"}
            if "api.nike.com" in url: hd["nike-api-caller-id"]="com.nike.commerce.nikedotcom.web"
            if any(h in url for h in CURL_HOSTS):
                import subprocess
                cp=subprocess.run(["curl","-s","--compressed","-A",UA,"-H","Accept-Language: en-US,en;q=0.9","-o",p+".part","-w","%{http_code}","--max-time","120",url],capture_output=True,text=True,timeout=90)
                st=int(cp.stdout.strip() or 0)
                class R: pass
                r=R(); r.content=open(p+".part","rb").read() if os.path.exists(p+".part") else b""
                if os.path.exists(p+".part"): os.remove(p+".part")
            else:
                r=requests.get(url,headers=hd,timeout=60)
                st=r.status_code
        except Exception as e:
            st=str(e)[:80]; r=None
        last[host]=time.time()
        with open(STATE,"a") as f: f.write(json.dumps({"t":time.strftime("%Y-%m-%dT%H:%M:%S"),"url":url,"status":st,"file":p})+"\n")
        if r is not None and st==200:
            open(p,"wb").write(r.content); return p,200
        if st in (400,403,404): return None,st
        time.sleep((90 if st==429 else 12)*(a+1))
    return None,st
if __name__=="__main__":
    out=sys.argv[1]; urls=sys.argv[2:]
    if urls==["-"]: urls=[l.strip() for l in sys.stdin if l.strip()]
    for u in urls:
        p,s=get(u,out); print(s,p,u,flush=True)
