# List Common Crawl captures of a Shopify retailer's product pages per crawl.
# usage: python3 -I cc_retail_idx.py outdir host coll1 coll2 ...
import sys,subprocess,time,os,json
out=sys.argv[1]; host=sys.argv[2]; os.makedirs(out,exist_ok=True)
pat=f"{host}/products/*"
for c in sys.argv[3:]:
    fn=os.path.join(out,f"{host}_{c}.jsonl")
    if os.path.exists(fn) and os.path.getsize(fn)>1000: continue
    pages=None
    for t in range(12):
        np=subprocess.run(["curl","-sS","-m","200",f"https://index.commoncrawl.org/{c}-index?url={pat}&showNumPages=true"],capture_output=True).stdout
        try: pages=json.loads(np)["pages"]; break
        except Exception: time.sleep(10+5*t)
    if pages is None: print("giveup",c,flush=True); continue
    data=b""
    for p in range(pages):
        for t in range(12):
            r=subprocess.run(["curl","-sS","-m","200",f"https://index.commoncrawl.org/{c}-index?url={pat}&output=json&filter=status:200&fl=url,timestamp,filename,offset,length,mime,status&page={p}"],capture_output=True).stdout
            if r.lstrip().startswith(b'{"url'): data+=r; break
            time.sleep(10+5*t)
    open(fn,"wb").write(data); print(c,pages,data.count(b"\n"),flush=True); time.sleep(2)
