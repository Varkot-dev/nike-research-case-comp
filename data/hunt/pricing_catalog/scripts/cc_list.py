# List all Common Crawl captures of www.nike.com/w/* (category walls) for every crawl 2023-2026.
# usage: python3 -I cc_list.py outdir [coll ...]
import sys, json, subprocess, time, os
out=sys.argv[1]; os.makedirs(out,exist_ok=True)
def curl(url,tries=8):
    for t in range(tries):
        r=subprocess.run(["curl","-sS","-m","180",url],capture_output=True)
        if r.returncode==0 and r.stdout and not r.stdout.startswith(b"<"): return r.stdout
        time.sleep(3+3*t)
    return None
colls=sys.argv[2:] if len(sys.argv)>2 else [c["id"] for c in json.loads(curl("https://index.commoncrawl.org/collinfo.json")) if c["id"]>="CC-MAIN-2023"]
for c in colls:
    fn=os.path.join(out,f"{c}_nike_w.jsonl")
    if os.path.exists(fn) and os.path.getsize(fn)>0: continue
    for pfx in ["www.nike.com/w/"]:
        np=curl(f"https://index.commoncrawl.org/{c}-index?url={pfx}&matchType=prefix&showNumPages=true")
        pages=json.loads(np)["pages"] if np else 0
        data=b""
        for p in range(pages):
            d=curl(f"https://index.commoncrawl.org/{c}-index?url={pfx}&matchType=prefix&output=json&fl=url,timestamp,status,filename,offset,length,mime&page={p}")
            if d: data+=d
            time.sleep(1)
        open(fn,"wb").write(data)
        print(c,pages,data.count(b"\n"),flush=True)
    time.sleep(1)
