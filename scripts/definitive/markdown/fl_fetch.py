"""Foot Locker product pages: https://www.footlocker.com/product/~/<code w/o dash and first char>.html ; 3 s spacing, curl."""
import sys, csv, re, subprocess, time, os, json
W=sys.argv[1]; UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
S=list(csv.DictReader(open(f"{W}/data/sample_priority.csv")))
out=csv.writer(open(f"{W}/data/footlocker_priority_20261013.csv","w",newline=""))
out.writerow(["code","line","release_year","retail_usd","fl_url","http","fl_name","fl_listPrice","fl_salePrice","fl_disc_pct_DERIVED","sizes_listed","sizes_available","fetched_utc","label"])
for r in S:
    sku=r["code"].replace("-","")[1:]; url=f"https://www.footlocker.com/product/~/{sku}.html"
    p=f"{W}/raw/fl/{sku}.html"
    cp=subprocess.run(["curl","-s","-L","--compressed","-A",UA,"-o",p,"-w","%{http_code}","--max-time","60",url],capture_output=True,text=True)
    st=cp.stdout.strip(); ts=time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime())
    t=open(p,encoding="utf-8",errors="ignore").read() if os.path.exists(p) else ""
    m=re.search(r'"newArrivalDate":"[^"]*","ageBuckets":\[[^\]]*\],"price":\{"currencyIso":null,"listPrice":([\d.]+),"salePrice":([\d.]+)',t) or re.search(r'"listPrice":([\d.]+),"salePrice":([\d.]+)',t)
    sk=re.search(rf'"sku":"{sku}"',t)
    nm=re.search(r'"name":"([^"]{3,80})"',t)
    if m and sk:
        lp,sp=float(m.group(1)),float(m.group(2))
        nsz=len(re.findall(r'"strippedSize":',t)); nav=len(re.findall(r'"inventoryAvailable":true',t))
        out.writerow([r["code"],r["line"],r["release_year"],r["retail_usd"],url,st,nm.group(1) if nm else "",lp,sp,round(100*(1-sp/lp),1),nsz,nav,ts,"VERIFIED (footlocker.com page opened); disc DERIVED"])
    else:
        out.writerow([r["code"],r["line"],r["release_year"],r["retail_usd"],url,st,"","","","","","",ts,"not listed / no price"])
    print(r["code"],st,bool(m and sk),flush=True); time.sleep(3)
