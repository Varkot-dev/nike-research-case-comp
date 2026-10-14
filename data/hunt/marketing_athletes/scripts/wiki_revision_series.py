"""Monthly snapshots of a Wikipedia page via the MediaWiki revisions API (first revision on/after the 1st of each month).
Usage: python3 -I wiki_revision_series.py "<title>" <rawdir> <start YYYY-MM> <end YYYY-MM>"""
import sys, json, os, time, urllib.request, urllib.parse, re
UA={"User-Agent":"nike-research-casecomp/1.0 (student research)"}
title, RAW, start, end = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]; STEP=int(sys.argv[5]) if len(sys.argv)>5 else 1
os.makedirs(RAW, exist_ok=True)
y,m=map(int,start.split("-")); ye,me=map(int,end.split("-"))
while (y,m)<=(ye,me):
    ts=f"{y:04d}-{m:02d}-01T00:00:00Z"
    fn=os.path.join(RAW, re.sub(r'\W+','_',title)+f"_{y:04d}{m:02d}.json")
    if not os.path.exists(fn):
        url="https://en.wikipedia.org/w/api.php?"+urllib.parse.urlencode(dict(action="query",prop="revisions",titles=title,rvlimit=1,rvdir="older",rvstart=ts,rvprop="timestamp|ids|content",rvslots="main",format="json",redirects=1))
        d=None
        for k in range(5):
            try: d=json.load(urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60)); break
            except Exception as e: print("retry",ts,e); time.sleep(15*(k+1))
        if d: json.dump(d,open(fn,"w"))
        time.sleep(2.5)
    m+=STEP
    if m>12: y+=1; m-=12
print("done")
