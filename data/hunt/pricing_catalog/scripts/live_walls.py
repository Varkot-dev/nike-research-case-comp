# Fetch live nike.com category walls (full and sale) and read totalResources + canonical URL.
# usage: python3 -I live_walls.py slugs.txt out.csv
import sys, subprocess, re, time, csv, datetime
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
slugs=[l.split() for l in open(sys.argv[1]) if l.strip() and not l.startswith('#')]
w=csv.writer(open(sys.argv[2],"w",newline="")); w.writerow(["fetched_utc","category","kind","slug","final_url","canonical","totalResources","title"])
for cat,kind,slug in slugs:
    u="https://www.nike.com/w/"+slug
    for t in range(3):
        r=subprocess.run(["curl","-sS","-L","-m","60","-A",UA,"-w","\n__URL__%{url_effective}",u],capture_output=True)
        txt=r.stdout.decode("utf8","ignore")
        if "__URL__" in txt and len(txt)>5000: break
        time.sleep(5)
    fin=txt.rsplit("__URL__",1)[-1]
    tr=re.findall(r'"totalResources":([0-9]+)',txt)
    can=re.findall(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"',txt) or re.findall(r'href="([^"]+)"[^>]*rel="canonical"',txt)
    ti=re.findall(r'<title[^>]*>([^<]+)</title>',txt)
    w.writerow([datetime.datetime.now(datetime.UTC).isoformat(timespec="seconds"),cat,kind,slug,fin,can[0] if can else "",tr[0] if tr else "",ti[0] if ti else ""])
    print(cat,kind,slug,tr[:1],can[:1],flush=True)
    time.sleep(2)
