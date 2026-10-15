"""Semrush 'trending websites' public pages: per country and category, top-100 domains with total_traffic, mom, yoy (embedded window.__PRELOADED_STATE__).
URL: https://www.semrush.com/trending-websites/<cc>/<category>. Page shows only the latest month (no date parameter works).
Run: python3 -I pull_semrush_trending.py <out.csv> <date_tag>
"""
import csv, json, sys, time, urllib.request
OUT=sys.argv[1]; UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
CC=["us","de","gb","jp","cn","fr","it","es","nl","kr","au","ca","br","mx","pl","se","tw","in"]
CAT=["sporting-goods","apparel-and-fashion","retail","e-commerce","consumer-goods"]
w=csv.writer(open(OUT,"w",newline="")); w.writerow(["country","category","data_month","rank_in_page","domain","total_traffic","desktop_pct","mom_pct","yoy_pct","category_total_traffic","category_total_mom"])
for cat in CAT:
  for cc in CC:
    url=f"https://www.semrush.com/trending-websites/{cc}/{cat}"
    h=None
    for i in range(3):
        try:
            h=urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":UA}),timeout=60).read().decode("utf-8","replace"); break
        except Exception as e:
            print("ERR",url,e,flush=True)
            if "404" in str(e): break
            time.sleep(10)
    if not h: continue
    k=h.find("__PRELOADED_STATE__ = ")
    if k<0: print("nostate",url); continue
    d,_=json.JSONDecoder().raw_decode(h[k+22:])
    dd=d["data"]
    for r,x in enumerate(dd["domains"],1):
        w.writerow([cc,cat,dd["date"],r,x["domain_name"],x["total_traffic"],round(x["desktop_percent"],1),round(x["mom"],2) if x.get("mom") is not None else "",round(x["yoy"],2) if x.get("yoy") is not None else "",dd.get("totaltraffic"),round(dd.get("totaltraffic_change") or 0,2)])
    print("OK",cc,cat,len(dd["domains"]),flush=True); time.sleep(2)
