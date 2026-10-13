import re, json
def _iter_price_products(obj):
    """yield dicts that look like product records with price info, from any nested JSON"""
    stack=[obj]
    while stack:
        o=stack.pop()
        if isinstance(o,dict):
            pr=o.get("prices") or o.get("price")
            if isinstance(pr,dict) and ("currentPrice" in pr) and ("initialPrice" in pr or "fullPrice" in pr):
                yield o
                continue
            stack.extend(o.values())
        elif isinstance(o,list): stack.extend(o)
def parse_html(t):
    """returns dict(total, products=[{title,subtitle,code,current,full}])"""
    res={"total":None,"products":[],"format":None}
    m=re.search(r'"totalResources":(\d+)',t)
    if m: res["total"]=int(m.group(1))
    data=None
    m=re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',t,re.S)
    if m:
        data=json.loads(m.group(1)); res["format"]="__NEXT_DATA__"
    else:
        m=re.search(r'window\.INITIAL_REDUX_STATE\s*=\s*(\{.*?\});?\s*</script>',t,re.S)
        if m:
            try: data=json.loads(m.group(1)); res["format"]="INITIAL_REDUX_STATE"
            except Exception: data=None
    if data is None:
        res["format"]="none"; return res
    if res["total"] is None:
        m=re.search(r'"totalResources":(\d+)',json.dumps(data))
        if m: res["total"]=int(m.group(1))
    wall=None
    try: wall=data["props"]["pageProps"]["initialState"]["Wall"]
    except Exception: wall=data.get("Wall") if isinstance(data,dict) else None
    if wall is None:
        res["format"]+="(no Wall)"; return res
    res["wall_keys"]=list(wall.keys())[:30]
    if wall.get("pageData",{}).get("totalResources") is not None: res["total"]=wall["pageData"]["totalResources"]
    if "productGroupings" in wall:
        res["products"],_=parse_api(wall); return res
    seen=set()
    for o in _iter_price_products(wall.get("products",wall)):
        pr=o.get("prices") or o.get("price")
        cur=pr.get("currentPrice"); full=pr.get("initialPrice", pr.get("fullPrice"))
        copy=o.get("copy") or {}
        title=copy.get("title") or o.get("title"); sub=copy.get("subTitle") or o.get("subtitle")
        code=o.get("productCode") or o.get("cloudProductId") or o.get("id") or o.get("pid")
        key=(code,title,cur)
        if key in seen: continue
        seen.add(key)
        res["products"].append({"title":title,"subtitle":sub,"code":code,"current":cur,"full":full})
    return res
def parse_api(j):
    out=[]
    for g in (j.get("productGroupings") or []):
        for i,o in enumerate(g.get("products") or []):
            pr=o.get("prices") or {}
            out.append({"group":g.get("groupKey") or o.get("groupKey"),"is_first":i==0,"title":(o.get("copy") or {}).get("title"),"subtitle":(o.get("copy") or {}).get("subTitle"),"code":o.get("productCode"),"current":pr.get("currentPrice"),"full":pr.get("initialPrice")})
    return out, j.get("pages",{}).get("totalResources")
