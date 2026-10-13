import re, json
def listings(t):
    i=t.find("window.__INITIAL_STATE__=")
    if i<0: return None
    d,_=json.JSONDecoder().raw_decode(t[i+len("window.__INITIAL_STATE__="):])
    out=[]; seen=set(); stack=[d]
    while stack:
        o=stack.pop()
        if isinstance(o,dict):
            if "price_amount" in o and "title" in o and "id" in o:
                if o["id"] not in seen:
                    seen.add(o["id"]); out.append(o)
                continue
            stack.extend(o.values())
        elif isinstance(o,list): stack.extend(o)
    return out
