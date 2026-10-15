# List Common Crawl captures of nike.com product pages (www.nike.com/t/*) per crawl.
# usage: python3 -I cc_pdp_idx.py outdir coll1 coll2 ...
import sys,subprocess,time,os,json
out=sys.argv[1]
for c in sys.argv[2:]:
    fn=os.path.join(out,f"nike_{c}.jsonl")
    if os.path.exists(fn) and os.path.getsize(fn)>1000: continue
    for t in range(10):
        np=subprocess.run(["curl","-sS","-m","200",f"https://index.commoncrawl.org/{c}-index?url=www.nike.com/t/*&showNumPages=true"],capture_output=True).stdout
        try: pages=json.loads(np)["pages"]; break
        except Exception: time.sleep(10+5*t); pages=None
    if pages is None: print("giveup",c,flush=True); continue
    data=b""
    for p in range(pages):
        for t in range(10):
            r=subprocess.run(["curl","-sS","-m","200",f"https://index.commoncrawl.org/{c}-index?url=www.nike.com/t/*&output=json&filter=status:200&page={p}"],capture_output=True).stdout
            if r.lstrip().startswith(b'{"urlkey'): data+=r; break
            time.sleep(10+5*t)
    open(fn,"wb").write(data); print(c,pages,data.count(b"\n"),flush=True); time.sleep(2)
