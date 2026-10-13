"""usage: python3 -I cdx.py <url> [matchType]  -> prints quarterly snapshot list (timestamp original) 2022-2026"""
import sys, json, time, requests
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
def cdx(url, match="exact", frm="2022", to="2026"):
    p={"url":url,"output":"json","from":frm,"to":to,"filter":"statuscode:200","collapse":"timestamp:6","matchType":match,"limit":"5000"}
    for a in range(4):
        try:
            r=requests.get("https://web.archive.org/cdx/search/cdx",params=p,headers={"User-Agent":UA},timeout=90)
            if r.status_code==200:
                j=r.json() if r.text.strip() else []
                return [dict(zip(j[0],row)) for row in j[1:]] if j else []
        except Exception as e: pass
        time.sleep(6*(a+1))
    return None
def quarterly(rows):
    best={}
    for r in rows:
        ts=r["timestamp"]; y=int(ts[:4]); m=int(ts[4:6]); q=(m-1)//3+1
        key=(y,q); mid=(q-1)*3+2
        score=abs(m-mid)
        if key not in best or score<best[key][0]: best[key]=(score,r)
    return [best[k][1] for k in sorted(best)]
if __name__=="__main__":
    rows=cdx(sys.argv[1], sys.argv[2] if len(sys.argv)>2 else "exact")
    if rows is None: print("CDX_FAIL"); sys.exit(1)
    print("# monthly rows:",len(rows))
    for r in quarterly(rows): print(r["timestamp"], r["original"], r.get("length"))
