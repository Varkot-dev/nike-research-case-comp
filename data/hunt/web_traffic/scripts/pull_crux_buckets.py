"""CrUX top-list rank-magnitude buckets by country (cached monthly by zakird/crux-top-lists on raw.githubusercontent.com).
Buckets are 1000/5000/10000/50000/100000/500000/1000000 (order of magnitude only). Keeps origins whose host matches tracked brand domains.
Run: python3 -I pull_crux_buckets.py <out.csv>
"""
import csv, gzip, io, re, sys, time, urllib.request
OUT=sys.argv[1]; UA="NikeCaseCompResearch/1.0 (academic)"
B="https://raw.githubusercontent.com/zakird/crux-top-lists/main/data/"
PAT=re.compile(r"^https?://([^/]*\.)?(nike\.com|nike\.com\.cn|adidas\.[a-z.]+|on\.com|on-running\.com|hoka\.com|newbalance\.[a-z.]+|asics\.[a-z.]+|lululemon\.com|dickssportinggoods\.com|footlocker\.[a-z.]+|puma\.com|amazon\.[a-z.]+|walmart\.com|target\.com|zalando\.[a-z.]+|jdsports\.[a-z.]+|zappos\.com|stockx\.com)$")
locs=["global","country/us","country/de","country/gb","country/jp","country/cn"]
months=[f"{y}{m:02d}" for y in range(2022,2027) for m in range(1,13) if "202205"<f"{y}{m:02d}"<="202609"]
w=csv.writer(open(OUT,"w",newline="")); w.writerow(["month","loc","origin","bucket"])
for loc in locs:
    for m in months:
        for i in range(3):
            try:
                with urllib.request.urlopen(urllib.request.Request(B+f"{loc}/{m}.csv.gz",headers={"User-Agent":UA}),timeout=120) as r: b=r.read()
                break
            except Exception as e:
                b=None
                if "404" in str(e): break
                time.sleep(10)
        if not b: print("MISSING",loc,m,flush=True); continue
        n=0
        for line in io.TextIOWrapper(gzip.GzipFile(fileobj=io.BytesIO(b)),encoding="utf-8",errors="replace"):
            o,_,rk=line.rstrip("\n").rpartition(",")
            if PAT.match(o): w.writerow([m,loc,o,rk]); n+=1
        print("OK",loc,m,n,flush=True); time.sleep(1)
