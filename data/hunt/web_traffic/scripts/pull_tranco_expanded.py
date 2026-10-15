"""Tranco ranks (1st and 15th of every month, 2019-06 to 2026-10) for sportswear peers, regional TLDs and a control basket.
Source: https://tranco-list.eu/api/lists/date/<date> -> list id; https://tranco-list.eu/download/<id>/100000 (top 100k).
Writes raw/tranco_expanded_long.csv (tracked + basket domains only) and, to a scratch dir (arg 2), the full top-5000 per date
(used only to compute list-wide drift; not stored in the repo).
Run: python3 -I pull_tranco_expanded.py <rawdir> <scratchdir>
"""
import csv, io, json, os, sys, time, urllib.request, datetime, gzip
OUT, SCR = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True); os.makedirs(SCR, exist_ok=True)
UA = "NikeCaseCompResearch/1.0 (academic)"
PEERS = ["nike.com","nike.com.cn","nike.net","adidas.com","adidas.de","adidas.co.uk","adidas.co.jp","adidas.com.cn","adidas.fr",
 "on.com","on-running.com","hoka.com","hokaoneone.com","newbalance.com","newbalance.co.uk","newbalance.de","asics.com","asics.co.jp",
 "lululemon.com","puma.com","skechers.com","underarmour.com","brooksrunning.com","saucony.com","converse.com","vans.com",
 "dickssportinggoods.com","footlocker.com","footlocker.co.uk","footlocker.de","finishline.com","jdsports.com","jdsports.co.uk",
 "hibbett.com","academy.com","rei.com","zappos.com","stockx.com","goat.com","zalando.de","zalando.co.uk","zalando.com","sportscheck.com",
 "tmall.com","jd.com","taobao.com","rakuten.co.jp","zozo.jp","asos.com","shein.com","temu.com"]
CONTROL = ["amazon.com","walmart.com","target.com","bestbuy.com","homedepot.com","lowes.com","ebay.com","etsy.com","macys.com","kohls.com",
 "wayfair.com","costco.com","ikea.com","zara.com","hm.com","uniqlo.com","sephora.com","nordstrom.com","gap.com","ulta.com","chewy.com",
 "apple.com","netflix.com","spotify.com","wikipedia.org","linkedin.com","paypal.com","bestbuy.com","cvs.com","walgreens.com","kroger.com",
 "aliexpress.com","amazon.de","amazon.co.uk","amazon.co.jp","ebay.de","ebay.co.uk","otto.de","argos.co.uk","next.co.uk"]
DOMS = list(dict.fromkeys(PEERS + CONTROL))
def fetch(url, binary=False):
    for i in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=180) as r:
                b = r.read()
            return b if binary else json.loads(b)
        except Exception as e:
            print("ERR", url, e, flush=True); time.sleep(15*(i+1))
dates=[]; d=datetime.date(2019,6,1)
while d <= datetime.date(2026,10,15):
    for dd in (d, d.replace(day=15)):
        if dd <= datetime.date(2026,10,15): dates.append(dd)
    d=(d.replace(day=28)+datetime.timedelta(days=5)).replace(day=1)
outcsv=os.path.join(OUT,"tranco_expanded_long.csv"); have=set()
if os.path.exists(outcsv): have={r["date"] for r in csv.DictReader(open(outcsv))}
new=not os.path.exists(outcsv); f=open(outcsv,"a",newline=""); w=csv.writer(f)
if new: w.writerow(["date","list_id","providers","domain","rank"])
for dt in dates:
    ds=dt.isoformat()
    if ds in have: continue
    meta=fetch(f"https://tranco-list.eu/api/lists/date/{ds}"); time.sleep(2)
    if not meta or not meta.get("available"): print("no list",ds,flush=True); continue
    raw=fetch(f"https://tranco-list.eu/download/{meta['list_id']}/100000",binary=True); time.sleep(2)
    if raw is None: continue
    ranks={}; top={}
    for line in io.StringIO(raw.decode("utf-8","replace")):
        p=line.strip().split(",")
        if len(p)==2:
            r=int(p[0])
            if r<=5000: top[p[1]]=r
            if p[1] in DOMS: ranks[p[1]]=r
    prov="|".join(meta.get("configuration",{}).get("providers",[]))
    for dom in DOMS: w.writerow([ds,meta["list_id"],prov,dom,ranks.get(dom,"")])
    f.flush()
    with gzip.open(os.path.join(SCR,f"top5000_{ds}.json.gz"),"wt") as g: json.dump(top,g)
    print("OK",ds,len(ranks),flush=True)
print("DONE",flush=True)
