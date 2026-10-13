"""usage: python3 -I pf_parse.py <out.csv> <fetchlog>... ; logs have lines 'code status path'"""
import sys, json, csv
rows={}
for lg in sys.argv[2:]:
    for l in open(lg):
        p=l.split()
        if len(p)<3 or p[1] not in ("200","cached"): continue
        q=p[0]
        try: d=json.load(open(p[2]))
        except Exception: continue
        for o in d.get("objects",[]):
            vs=o.get("publishedContent",{}).get("viewStartDate","")
            for pi in o.get("productInfo",[]):
                mp=pi.get("merchProduct",{}); pr=pi.get("merchPrice",{}); pc=pi.get("productContent",{})
                c=mp.get("styleColor")
                if not c: continue
                if "-" in q and c!=q: continue
                rows[c]={"query":q,"code":c,"labelName":mp.get("labelName",""),"title":pc.get("title",""),"subtitle":pc.get("subtitle",""),
                  "colorDescription":pc.get("colorDescription",""),"full":pr.get("fullPrice"),"current":pr.get("currentPrice"),
                  "discounted":pr.get("discounted"),"available":pi.get("availability",{}).get("available"),"status":mp.get("status"),
                  "commerceStartDate":(mp.get("commerceStartDate") or "")[:10],"viewStartDate":vs[:10],
                  "slug":pc.get("slug",""),"pdp_url":f"https://www.nike.com/t/{pc.get('slug','')}/{c}",
                  "api_lastFetchTime":o.get("lastFetchTime",""),"fetched":"2026-10-13"}
w=csv.DictWriter(open(sys.argv[1],"w",newline=""),fieldnames=list(next(iter(rows.values())).keys()))
w.writeheader(); [w.writerow(r) for r in rows.values()]
print(len(rows))
