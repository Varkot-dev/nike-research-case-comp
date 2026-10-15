import subprocess,time,json,sys,os,gzip
host,pat=sys.argv[1],sys.argv[2]; crawls=sys.argv[3:]
os.makedirs('cc',exist_ok=True)
def get(u,tries=10):
    for t in range(tries):
        r=subprocess.run(["curl","-sS","-m","200",u],capture_output=True)
        if r.returncode==0: return r.stdout
        time.sleep(6+4*t)
    return None
for c in crawls:
    fn=f'cc/{host}__{c}.jsonl.gz'
    if os.path.exists(fn): continue
    b=get(f"https://index.commoncrawl.org/{c}-index?url={pat}&showNumPages=true&output=json")
    try: n=json.loads(b)['pages']
    except Exception: print('FAILPAGES',host,c,flush=True); continue
    out=b''; ok=True
    for p in range(n):
        d=get(f"https://index.commoncrawl.org/{c}-index?url={pat}&output=json&fl=url,status,timestamp&page={p}")
        if d is None or (d.strip() and not d.lstrip().startswith(b'{')): ok=False; break
        out+=d
    if not ok: print('FAIL',host,c,flush=True); continue
    gzip.open(fn,'wb').write(out); print(host,c,n,out.count(b'\n'),flush=True)
