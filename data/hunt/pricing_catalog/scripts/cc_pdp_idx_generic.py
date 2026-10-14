# List Common Crawl captures matching a URL pattern, per crawl.
# usage: python3 -I cc_pdp_idx_generic.py outdir brandlabel "www.adidas.com/us/*" coll1 coll2 ...
import sys,subprocess,time,os,json
out=sys.argv[1]; BR=sys.argv[2]; PAT=sys.argv[3]
for c in sys.argv[4:]:
    fn=os.path.join(out,f"{BR}_{c}.jsonl")
    if os.path.exists(fn) and os.path.getsize(fn)>1000: continue
    for t in range(10):
        np=subprocess.run(["curl","-sS","-m","200",f"https://index.commoncrawl.org/{c}-index?url={PAT}&showNumPages=true"],capture_output=True).stdout
        try: pages=json.loads(np)["pages"]; break
        except Exception: time.sleep(10+5*t); pages=None
    if pages is None: print("giveup",c,flush=True); continue
    data=b""
    for p in range(pages):
        for t in range(10):
            r=subprocess.run(["curl","-sS","-m","200",f"https://index.commoncrawl.org/{c}-index?url={PAT}&output=json&filter=status:200&page={p}"],capture_output=True).stdout
            if r.lstrip().startswith(b'{"urlkey'): data+=r; break
            time.sleep(10+5*t)
    open(fn,"wb").write(data); print(c,pages,data.count(b"\n"),flush=True); time.sleep(2)
