# Checker: for random panel pages in Aug-Sep 2025 and Aug-Sep 2026, re-read the archived HTML and flag
# hidden promotions ("See Price in Bag"), sold-out / unavailable pages, and member-price badges.
import sys,json,gzip,subprocess,time,re,csv
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
N=int(sys.argv[1]); out=sys.argv[2]
d=pd.read_csv("pdp_panel_tidy.csv.gz"); d=d[d.brand=="nike"]; d["m"]=pd.to_datetime(d.date).dt.month; d["window"]=None; d.loc[d.m.between(3,6)&d.date.str.startswith("2025"),"window"]="MarJun2025"; d.loc[d.m.between(3,6)&d.date.str.startswith("2026"),"window"]="MarJun2026"; d.loc[d.coll.isin(["CC-MAIN-2024-33","CC-MAIN-2024-38"]),"window"]="AugSep2024"; d=d[d.window.notna()]
samp=pd.concat([d[d.window==w].sample(N,random_state=3) for w in ["AugSep2024","MarJun2025","MarJun2026"]])
idx={}
for c in samp.coll.unique():
    want=set(samp[samp.coll==c].url)
    for l in gzip.open(f"raw/cc_pdp_idx/nike_{c}.jsonl.gz","rt",errors="ignore"):
        if l.startswith("{"):
            try: j=json.loads(l)
            except Exception: continue
            u=j["url"].split("?")[0]
            if u in want and j.get("status")=="200": idx[(c,u,j["timestamp"])]=j
def job(r):
    j=idx.get((r.coll,r.url,str(r.ts)))
    if not j: return None
    o=int(j["offset"]); n=int(j["length"])
    for t in range(4):
        x=subprocess.run(["curl","-sS","-m","90","-r",f"{o}-{o+n-1}","https://data.commoncrawl.org/"+j["filename"]],capture_output=True).stdout
        try: h=gzip.decompress(x).decode("utf8","ignore"); break
        except Exception: time.sleep(5)
    else: return None
    time.sleep(0.5)
    return [r.window,r.coll,r.url,r.disc,r["cat"],
        bool(re.search(r'promo-message">See Price in Bag',h)),
        bool(re.search(r'>\s*Sold Out\s*<|"soldOut":true|Sold Out',h)),
        bool(re.search(r'Coming Soon|Notify Me',h,re.I)),
        bool(re.search(r'"available":false|OutOfStock',h)),
        bool(re.search(r'InStock',h)),
        bool(re.search(r'Member (?:Price|Exclusive)|member price',h,re.I))]
with ThreadPoolExecutor(3) as ex: rows=[x for x in ex.map(job,[r for _,r in samp.iterrows()]) if x]
cols=["window","coll","url","disc","cat","price_in_bag","sold_out_text","coming_soon_notify","schema_outofstock","schema_instock","member_price"]
R=pd.DataFrame(rows,columns=cols); R.to_csv(out,index=False)
print(R.groupby("window")[cols[3:4]+cols[5:]].mean().round(3).T); print(R.groupby("window").size())
print(R.groupby(["window","schema_outofstock"]).disc.agg(["size","mean"]).round(3))
