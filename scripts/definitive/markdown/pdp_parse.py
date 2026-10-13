"""Parse a nike.com /t/ product page (live or Wayback id_ capture). Returns list of {code,current,full,title,subtitle,avail}.
Handles 2023 format (flat styleColor/fullPrice/currentPrice) and 2024+ format (prices.currentPrice/initialPrice, pdpUrl.path)."""
import re, json
CODE=re.compile(r'([A-Z0-9]{6}-[0-9]{3})')
def _code(d):
    for k in ("styleColor","productCode"):
        v=d.get(k)
        if isinstance(v,str) and CODE.fullmatch(v): return v
    pu=d.get("pdpUrl")
    if isinstance(pu,dict):
        m=CODE.search(pu.get("path","") or pu.get("url",""))
        if m: return m.group(1)
    return None
def parse(t):
    m=re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',t,re.S)
    if not m: return None
    try: data=json.loads(m.group(1))
    except Exception: return None
    out={}; stack=[data]
    while stack:
        o=stack.pop()
        if isinstance(o,dict):
            cur=full=None
            pr=o.get("prices")
            if isinstance(pr,dict) and "currentPrice" in pr:
                cur=pr.get("currentPrice"); full=pr.get("initialPrice", pr.get("fullPrice"))
            elif "currentPrice" in o and ("fullPrice" in o or "initialPrice" in o):
                cur=o.get("currentPrice"); full=o.get("fullPrice", o.get("initialPrice"))
            c=_code(o) if cur is not None else None
            if c and isinstance(cur,(int,float)) and isinstance(full,(int,float)) and full>0:
                pi=o.get("productInfo") if isinstance(o.get("productInfo"),dict) else {}
                rec={"code":c,"current":cur,"full":full,
                     "title":o.get("title") or pi.get("title") or o.get("fullTitle") or "",
                     "subtitle":o.get("subtitle") or pi.get("subtitle") or "",
                     "avail":o.get("inStock", o.get("isAvailable", o.get("state",""))),
                     "rel":o.get("seoProductReleaseDate") or o.get("releaseDate") or o.get("commerceStartDate") or ""}
                # keep the first record per code, but prefer one with a discount flag consistent
                if c not in out: out[c]=rec
            stack.extend(v for v in o.values() if isinstance(v,(dict,list)))
        elif isinstance(o,list): stack.extend(v for v in o if isinstance(v,(dict,list)))
    return list(out.values())
if __name__=="__main__":
    import sys
    for f in sys.argv[1:]:
        r=parse(open(f,encoding="utf-8",errors="ignore").read())
        print(f, None if r is None else len(r))
        for x in (r or [])[:8]: print("  ",x)
