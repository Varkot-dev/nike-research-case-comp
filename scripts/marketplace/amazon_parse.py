"""Parse Amazon Best Sellers pages (current + Wayback) -> item-level and brand-share CSVs."""
import sys, os, json, csv, re, html
from bs4 import BeautifulSoup
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brands import brand_of, FOCUS
data=sys.argv[1]
NODES={"679286011":"mens_running","679360011":"womens_running","679312011":"mens_fashion_sneakers","679394011":"womens_fashion_sneakers","6127770011":"mens_athletic","6127771011":"womens_athletic"}
log=[json.loads(l) for l in open(os.path.join(data,"fetch_log.jsonl"))]
pages={}
for d in log:
    if d["status"]!=200 or "amazon.com" not in d["url"]: continue
    m=re.search(r'/(\d{9,11})(?:/|$|\?)',d["url"]+"/")
    node=m.group(1) if m else None
    if node not in NODES: continue
    if "web.archive.org" in d["url"]:
        ts=re.search(r'/web/(\d{14})id_',d["url"]).group(1); date=f"{ts[:4]}-{ts[4:6]}-{ts[6:8]}"; src="wayback"
    else: date=d["t"][:10]; src="live"
    pages[(NODES[node],date)]=(d["file"],d["url"],src)
items=[]; summ=[]; fails=[]
for (cat,date),(f,url,src) in sorted(pages.items()):
    soup=BeautifulSoup(open(f,encoding="utf-8",errors="ignore").read(),"html.parser")
    title=soup.title.get_text(strip=True) if soup.title else ""
    cards=soup.select("#gridItemRoot") or soup.select("li.zg-item-immersion")
    got=[]
    for c in cards:
        r=c.select_one(".zg-bdg-text, .zg-badge-text")
        rank=int(re.sub(r"\D","",r.get_text())) if r else None
        tdiv=c.find(lambda tag: tag.name in("div","span") and tag.get("class") and any("line-clamp" in x or "p13n-sc-truncate" in x for x in tag["class"]))
        name=tdiv.get_text(" ",strip=True) if tdiv else None
        if not name:
            img=c.find("img"); name=img.get("alt") if img else None
        pe=c.find(lambda tag: tag.name=="span" and tag.get("class") and any("p13n-sc-price" in x for x in tag["class"]))
        price=pe.get_text(strip=True) if pe else ""
        mm=re.search(r"\$([\d,]+\.\d\d)",price); price=float(mm.group(1).replace(",","")) if mm else None
        asin=None
        a=c.find("a",href=re.compile(r"/dp/"))
        if a: asin=re.search(r"/dp/([A-Z0-9]{10})",a["href"]).group(1)
        if name: got.append((rank,name,price,asin))
    if not got:
        fails.append((cat,date,src,title[:60])); continue
    for rank,name,price,asin in got:
        items.append({"category":cat,"snapshot_date":date,"source":src,"rank":rank,"title":name,"brand":brand_of(name),"price_low":price,"asin":asin,"url":url})
    got=[(g[0],g[1]) for g in got]
    n=len(got); top30=[x for x in got if x[0] and x[0]<=30]
    row={"category":cat,"snapshot_date":date,"source":src,"items_parsed":n,"top30_n":len(top30)}
    for b in FOCUS:
        k=sum(1 for _,nm in top30 if brand_of(nm)==b); row[f"{b}_count_top30"]=k; row[f"{b}_share_top30_pct"]=round(100*k/len(top30),1) if top30 else None
    nk=sum(1 for _,nm in top30 if brand_of(nm) in("Nike","Jordan"))
    row["NikeInc_ex_Converse_count_top30"]=nk; row["NikeInc_ex_Converse_share_top30_pct"]=round(100*nk/len(top30),1) if top30 else None
    row["Nike_best_rank"]=min([r for r,nm in got if brand_of(nm)=="Nike" and r] or [None], key=lambda x: x if x else 999)
    summ.append(row)
def w(path,rows):
    with open(path,"w",newline="") as fh:
        wr=csv.DictWriter(fh,fieldnames=list(rows[0].keys())); wr.writeheader(); wr.writerows(rows)
w(os.path.join(data,"amazon_bestsellers_items.csv"),items)
w(os.path.join(data,"amazon_bestsellers_brand_share.csv"),summ)
for s in summ: print(s["category"],s["snapshot_date"],s["source"],s["items_parsed"],"Nike",s["Nike_count_top30"],"HOKA",s["HOKA_count_top30"],"On",s["On_count_top30"],"Brooks",s["Brooks_count_top30"],"ASICS",s["ASICS_count_top30"],"NB",s["New Balance_count_top30"],"adi",s["adidas_count_top30"],"Sk",s["Skechers_count_top30"])
print("FAILS",fails)
