# Fetch live nike.com target walls and parse with the same parser used for archived captures.
# usage: python3 -I live_target_walls.py targets.txt out.csv
import sys,subprocess,time,csv,datetime,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from wallparse import parse_wall_any
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
w=csv.writer(open(sys.argv[2],"w",newline="")); w.writerow(["coll","ts","wall","count","n_prices","n_disc","share_disc","mean_depth_disc","method","final_url","offset"])
for s in [l.strip() for l in open(sys.argv[1]) if l.strip()]:
    r=subprocess.run(["curl","-sS","-L","-m","60","-A",UA,"-w","\n__URL__%{url_effective}","https://www.nike.com/w/"+s],capture_output=True)
    t=r.stdout.decode("utf8","ignore"); fin=t.rsplit("__URL__",1)[-1]
    n,p,m=parse_wall_any(t); d=[1-b/a for a,b in p if a>0 and b<a-0.01]
    w.writerow(["LIVE-2026-10-14",datetime.datetime.now(datetime.UTC).strftime("%Y%m%d%H%M%S"),s,n,len(p),len(d),round(len(d)/len(p),3) if p else "",round(sum(d)/len(d),3) if d else "",m,fin,""])
    print(s,n,len(p),len(d),fin[-60:],flush=True); time.sleep(2)
