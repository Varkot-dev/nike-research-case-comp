"""Build control sample: product_feed styleCode colourways with commerceStartDate 2023-2026; release = min(commerceStartDate, first Wayback PDP capture) (DERIVED)."""
import csv, glob, re, datetime as dt, sys, collections
W=sys.argv[1]
L=[r for r in csv.DictReader(open(f"{W}/data/live_productfeed.csv")) if "-" not in r["query"]]
first={}; ncap=collections.Counter()
CODE=re.compile(r'/([A-Z0-9]{6}-[0-9]{3})(?:[?#/]|$)')
for f in glob.glob(f"{W}/raw/cdx_nike_com_t_*_p*.txt"):
    for l in open(f):
        p=l.split()
        if len(p)<3: continue
        m=CODE.search(p[1])
        if not m: continue
        c=m.group(1); d=dt.date(int(p[0][:4]),int(p[0][4:6]),int(p[0][6:8]))
        ncap[c]+=1
        if c not in first or d<first[c]: first[c]=d
def model(r):
    n=r["labelName"].upper()
    if "PEGASUS 40" in n: return "Pegasus 40"
    if "PEGASUS 41" in n: return "Pegasus 41"
    if "PEGASUS 42" in n: return "Pegasus 42"
    if "VOMERO 18" in n: return "Vomero 18"
    if "VOMERO 5" in n: return "Vomero 5"
    if "DUNK LOW" in n: return "Dunk Low"
    return n
w=csv.writer(open(f"{W}/data/sample_control.csv","w",newline=""))
w.writerow(["code","release_date","retail_usd","line","release_year","collab_or_special","gender","name","release_source","commerceStartDate","first_wayback_capture","n_cdx_captures"])
k=0
for r in L:
    cs=dt.date.fromisoformat(r["commerceStartDate"]) if r["commerceStartDate"] else None
    fc=first.get(r["code"])
    cands=[x for x in (cs,fc) if x]
    if not cands: continue
    rd=min(cands)
    if rd.year<2023 or (cs and cs.year<2023): continue
    g="women" if r["subtitle"].startswith("Women") else "men"
    w.writerow([r["code"],rd.isoformat(),r["full"],model(r),rd.year,False,g,r["title"]+" "+r["colorDescription"],"DERIVED min(product_feed commerceStartDate, first Wayback capture)",r["commerceStartDate"],fc.isoformat() if fc else "",ncap[r["code"]]]); k+=1
print(k)
