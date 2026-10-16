import requests,re,time,csv,json
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
urls=json.load(open('rr_urls.json'))
out=[]
for i,u in enumerate(urls):
    try:
        r=requests.get('https://runrepeat.com'+u,headers={'User-Agent':UA},timeout=40)
        m=re.search(r'release-date-value[^>]*>.*?<span>(?:<!---->)? ?(?:<!--\[-->)?<span>([A-Za-z]{3} \d{4}|\d{4})</span>',r.text,re.S)
        dp=re.search(r'"datePublished":"([^"]+)"',r.text); dm=re.search(r'"dateModified":"([^"]+)"',r.text)
        t=re.search(r'<title>(.*?)</title>',r.text)
        pr=re.search(r'"(?:msrp|price)":\s*"?(\d+(?:\.\d+)?)',r.text)
        out.append((u,r.status_code,m.group(1) if m else '',dp.group(1)[:10] if dp else '',dm.group(1)[:10] if dm else '',t.group(1) if t else ''))
    except Exception as e: out.append((u,0,'','','',str(e)))
    time.sleep(0.3)
csv.writer(open('rr_shoes2.csv','w')).writerows(out)
print('done')
