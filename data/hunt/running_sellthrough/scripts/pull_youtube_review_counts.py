"""YouTube public search pages: estimatedResults and top-20 video view counts/ages for '<model> review' queries (no login, generic UA).
Output youtube_model_review_search.csv"""
import re, json, subprocess, time, urllib.parse, csv, sys
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
Q = ["nike pegasus 42 review", "nike pegasus 41 review", "nike vomero 18 review", "nike vomero plus review", "nike pegasus premium review", "nike structure 26 review", "nike invincible 3 review",
     "hoka clifton 10 review", "hoka clifton 11 review", "hoka bondi 9 review", "asics novablast 5 review", "asics novablast 6 review", "asics gel nimbus 28 review", "brooks ghost 17 review", "brooks ghost 18 review",
     "brooks glycerin 22 review", "saucony ride 18 review", "saucony triumph 22 review", "new balance 880v15 review", "on cloudmonster 2 review", "adidas adizero evo sl review"]
def num(s):
    s = s.replace(",", "").lower(); m = re.match(r"([\d.]+)\s*([kmb]?)", s)
    return float(m.group(1)) * {"": 1, "k": 1e3, "m": 1e6, "b": 1e9}[m.group(2)] if m else None
rows = []
for q in Q:
    for sp, lab in [("", "all_time"), ("&sp=EgIIBQ%253D%253D", "last_year")]:
        cp = subprocess.run(["curl", "-s", "-L", "--compressed", "-m", "40", "-A", UA, "-H", "Accept-Language: en-US", "https://www.youtube.com/results?search_query=" + urllib.parse.quote_plus(q) + sp], capture_output=True, text=True)
        h = cp.stdout; est = re.search(r'"estimatedResults":"(\d+)"', h)
        views = [num(v) for v in re.findall(r'"viewCountText":\{"simpleText":"([\d,\.KMB]+) views"', h)]
        rows.append({"query": q, "filter": lab, "estimated_results": int(est.group(1)) if est else None, "n_videos_parsed": len(views), "median_views_top": sorted(views)[len(views)//2] if views else None, "sum_views_top": sum(v for v in views if v)})
        print(rows[-1], flush=True); time.sleep(2.5)
w = csv.DictWriter(open("youtube_model_review_search.csv", "w", newline=""), fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
