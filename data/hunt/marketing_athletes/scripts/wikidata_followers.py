"""Social-media follower history (Wikidata P8687 with P580/P585 point in time, P6552/P2002/P2003/P2397 qualifiers) for brands and athletes.
Uses en.wikipedia pageprops to map titles -> QIDs, then wikidata Special:EntityData JSON (not WDQS)."""
import sys, json, time, urllib.request, urllib.parse, csv, os
UA={"User-Agent":"nike-research-casecomp/1.0 (student research)"}
def get(url):
    for k in range(4):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60))
        except Exception as e:
            print("retry",url[:90],e); time.sleep(10*(k+1))
    return None
titles=sys.argv[3].split("|")
RAW=sys.argv[1]; OUT=sys.argv[2]
props=get("https://en.wikipedia.org/w/api.php?action=query&prop=pageprops&ppprop=wikibase_item&redirects=1&format=json&titles="+urllib.parse.quote("|".join(titles)))
qmap={p["title"]:p.get("pageprops",{}).get("wikibase_item") for p in props["query"]["pages"].values()}
print(qmap)
QUAL={"P6552":"twitter_id","P2002":"twitter","P2003":"instagram","P2397":"youtube_channel","P7085":"tiktok","P4033":"mastodon","P2013":"facebook","P11892":"threads"}
rows=[]
for t,q in qmap.items():
    if not q: continue
    fn=os.path.join(RAW,f"wikidata_{q}.json")
    if not os.path.exists(fn):
        d=get(f"https://www.wikidata.org/wiki/Special:EntityData/{q}.json"); time.sleep(3)
        if d is None: continue
        json.dump(d,open(fn,"w"))
    d=json.load(open(fn))
    ent=d["entities"][q]
    for st in ent["claims"].get("P8687",[]):
        try: v=float(st["mainsnak"]["datavalue"]["value"]["amount"])
        except: continue
        qual=st.get("qualifiers",{})
        date=None
        for p in ("P585","P580"):
            if p in qual: date=qual[p][0]["datavalue"]["value"]["time"][1:11]; break
        platform=None; handle=None
        for p,name in QUAL.items():
            if p in qual:
                platform=name; dv=qual[p][0].get("datavalue",{}).get("value"); handle=dv if isinstance(dv,str) else None; break
        rows.append(dict(entity=t,qid=q,platform=platform,handle=handle,date=date,followers=v,rank=st.get("rank")))
w=csv.DictWriter(open(OUT,"w"),fieldnames=["entity","qid","platform","handle","date","followers","rank"]); w.writeheader(); w.writerows(rows)
print(len(rows))
