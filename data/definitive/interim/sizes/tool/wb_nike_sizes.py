"""usage: python3 -I wb_nike_sizes.py <html>... -> prints size statuses from a Wayback nike.com PDP capture"""
import re, json, sys
dec=json.JSONDecoder()
for f in sys.argv[1:]:
    t=open(f,encoding='utf-8',errors='ignore').read()
    out=None
    for m in re.finditer(r'"sizes":\[',t):
        try: arr,_=dec.raw_decode(t[m.end()-1:])
        except Exception: continue
        if arr and isinstance(arr[0],dict) and 'status' in arr[0]:
            out=[(s.get('label'),s.get('status')) for s in arr]; break
    pm=re.search(r'"prices":\{"currency":"USD","currentPrice":([\d.]+),"initialPrice":([\d.]+)',t)
    print(f, pm.groups() if pm else None, out)
