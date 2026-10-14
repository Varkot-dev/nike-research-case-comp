# Checker: re-read 3+ Common Crawl wall captures by WARC offset, re-count items with an independent regex.
import sys,subprocess,zlib,re,csv,time
import pandas as pd
d=pd.read_csv(sys.argv[1]); out=sys.argv[2]
pick=d[d.wall.isin(['air-force-1-shoes-5sj3yzy7ok','dunk-shoes-90aohzy7ok','jordan-1-shoes-4fokyzy7ok'])]
pick=pd.concat([pick[pick.coll.str.startswith('CC-MAIN-2024')].head(2),pick[pick.coll.str.startswith('CC-MAIN-2025')].head(2),pick[pick.coll.str.startswith('CC-MAIN-2026')].head(2)])
rows=[]
for _,r in pick.iterrows():
    o=int(r.offset)
    raw=subprocess.run(["curl","-sS","-m","120","-r",f"{o}-{o+4000000}","https://data.commoncrawl.org/"+r.warc],capture_output=True).stdout
    t=zlib.decompressobj(31).decompress(raw).decode("utf8","ignore")
    tr=re.findall(r'"totalResources":([0-9]+)',t); hdr=re.findall(r'wall-header__item_count[^>]*>\(([0-9,]+)\)',t)
    uri=re.search(r'WARC-Target-URI: (\S+)',t).group(1)
    rows.append([r.coll,r.wall,r['count'],uri,tr[:2],hdr[:2]]); print(rows[-1],flush=True); time.sleep(1)
csv.writer(open(out,"w")).writerows([["coll","wall","count_panel","uri","totalResources_recheck","header_recheck"]]+rows)
