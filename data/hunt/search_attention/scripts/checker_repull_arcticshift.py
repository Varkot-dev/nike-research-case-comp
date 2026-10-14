import urllib.request,urllib.parse,json,time,sys,datetime as dt
def cnt(sub,y,m,days=7):
    s=int(dt.datetime(y,m,1,tzinfo=dt.timezone.utc).timestamp()); e=s+days*86400
    after=s; n=0; titles=[]
    for _ in range(100):
        u="https://arctic-shift.photon-reddit.com/api/posts/search?"+urllib.parse.urlencode({"subreddit":sub,"after":after,"before":e,"sort":"asc","limit":"auto","fields":"created_utc,title"})
        r=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"NikeCaseCompChecker/1.0"}),timeout=60))["data"]
        time.sleep(4)
        if not r: break
        n+=len(r); titles+= [x["title"] for x in r]
        after=int(r[-1]["created_utc"])+1
        if len(r)<90: break
    return n,titles
for sub,y,m in [("RunningShoeGeeks",2024,4),("RunningShoeGeeks",2025,9),("RunningShoeGeeks",2026,9),("Sneakers",2026,9)]:
    n,t=cnt(sub,y,m); import re
    print(sub,y,m,n,"nike",sum(bool(re.search(r"\bnike\b",x,re.I)) for x in t),"vomero",sum(bool(re.search(r"vomero",x,re.I)) for x in t))
