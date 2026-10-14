import sys, json, subprocess, time, os, gzip, urllib.parse
# usage: cc.py outdir coll1,coll2 url1 url2 ...
out=sys.argv[1]; colls=sys.argv[2].split(','); urls=sys.argv[3:]
os.makedirs(out,exist_ok=True)
def curl(args,binary=False):
    for t in range(5):
        r=subprocess.run(["curl","-sS","-m","120"]+args,capture_output=True)
        if r.returncode==0: return r.stdout
        time.sleep(4+4*t)
    return None
man=open(os.path.join(out,"manifest.jsonl"),"a")
for c in colls:
    for u in urls:
        q=f"https://index.commoncrawl.org/{c}-index?url={urllib.parse.quote(u,safe='')}&output=json&filter=status:200"
        r=curl([q])
        if not r: print("idxfail",c,u,flush=True); continue
        recs=[json.loads(l) for l in r.decode().splitlines() if l.startswith('{')]
        if not recs: print("none",c,u,flush=True); continue
        recs=[x for x in recs if "offset" in x]
        for rec in recs[:2]:
            off=int(rec["offset"]); ln=int(rec["length"])
            b=curl(["-r",f"{off}-{off+ln-1}","https://data.commoncrawl.org/"+rec["filename"]])
            if not b: print("fetchfail",c,u,flush=True); continue
            try: txt=gzip.decompress(b)
            except Exception as e: print("gz",e); continue
            fn=os.path.join(out,f"{c}_{rec['timestamp']}_{abs(hash(u))%10**8}.warc")
            open(fn,"wb").write(txt)
            man.write(json.dumps({"coll":c,"url":u,"ts":rec["timestamp"],"file":fn,"warc":rec["filename"],"offset":off,"length":ln})+"\n"); man.flush()
            print("ok",c,rec["timestamp"],u,len(txt),flush=True)
        time.sleep(1)
