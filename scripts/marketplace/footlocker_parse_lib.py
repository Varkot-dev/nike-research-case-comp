import re, json
def blocks(t):
    """return (pagination, facets, products) from first embedded search result JSON"""
    out={}
    m=re.search(r'"pagination":\{"currentPage":(\d+),"pageSize":(\d+),"sort":"([^"]*)","totalPages":(\d+),"totalResults":(\d+)\}',t)
    if m: out["pagination"]=dict(currentPage=int(m.group(1)),pageSize=int(m.group(2)),totalPages=int(m.group(4)),totalResults=int(m.group(5)))
    # products array after pagination
    prods=[]
    if m:
        i=m.end()
        if t[i:i+12]==',"products":':
            dec=json.JSONDecoder(); arr,_=dec.raw_decode(t[i+12:].replace('\\u002F','/'))
            prods=arr
    out["products"]=prods
    # brand facet
    fb={}
    j=t.find('"code":"brand","selectedCount')
    if j>0:
        # facet object values precede the code key; search backwards for '"values":['
        k=t.rfind('"values":[',0,j)
        seg=t[k:j]
        for mm in re.finditer(r'\{"name":"([^"]+)","count":(\d+)',seg): fb[mm.group(1)]=int(mm.group(2))
    out["brand_facet"]=fb
    return out
