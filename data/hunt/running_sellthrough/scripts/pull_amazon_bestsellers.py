"""Amazon US Best Sellers (public zgbs pages, no login) for running shoes. Parses rank, ASIN, title, rating, review count, price.
Usage: python3 -I pull_amazon_bestsellers.py <rawdir> <tag>"""
import sys, os, re, html, json, subprocess, time, csv
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
raw, tag = sys.argv[1], sys.argv[2]
NODES = {"mens_running": ("Best-Sellers-Clothing-Shoes-Jewelry-Mens-Running-Shoes", "679286011"),
         "womens_running": ("Best-Sellers-Clothing-Shoes-Jewelry-Womens-Running-Shoes", "679360011")}
if len(sys.argv) > 3: NODES["womens_running"] = ("Best-Sellers-Clothing-Shoes-Jewelry-Womens-Running-Shoes", sys.argv[3])
def get(u):
    for a in range(3):
        cp = subprocess.run(["curl","-s","-L","--compressed","-A",UA,"-H","Accept-Language: en-US,en;q=0.9","--max-time","60","-w","\n%{http_code}",u],capture_output=True,text=True)
        b,_,c = cp.stdout.rpartition("\n"); time.sleep(3)
        if c == "200": return b
        time.sleep(15)
rows = []
for key,(slug,node) in NODES.items():
    for pg in (1,2):
        h = get(f"https://www.amazon.com/{slug}/zgbs/fashion/{node}?_encoding=UTF8&pg={pg}")
        if not h: continue
        open(os.path.join(raw,f"amz_{key}_pg{pg}_{tag}.html"),"w").write(h)
        t = re.findall(r"<title>(.*?)</title>",h)
        parts = re.split(r'zg-bdg-text">#?(\d+)</span>', h)
        for k in range(1, len(parts)-1, 2):
            rkv, b = parts[k], parts[k+1][:6000]
            rk = [rkv]; asin = re.findall(r'/dp/(B[0-9A-Z]{9})',b)
            ti = re.findall(r'alt="([^"]+)"',b)
            rt = re.findall(r'(\d\.\d) out of 5 stars',b)
            rc = re.findall(r'aria-label="[\d.]+ out of 5 stars, ([\d,]+) rating',b) or re.findall(r'class="a-size-small">\s*([\d,]+)\s*<',b)
            pr = re.findall(r'a-offscreen">\$([\d.,]+)',b)
            rows.append({"node":key,"page":pg,"rank":rk[0] if rk else "","asin":asin[0] if asin else "","title":html.unescape(ti[0]) if ti else "",
                         "rating":rt[0] if rt else "","ratings_count":rc[0].replace(",","") if rc else "","price":pr[0] if pr else "","page_title":html.unescape(t[0]) if t else "","tag":tag})
        print(key,pg,len(rows),t[:1],flush=True)
w = csv.DictWriter(open(os.path.join(raw,f"amazon_bestsellers_{tag}.csv"),"w",newline=""),fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
