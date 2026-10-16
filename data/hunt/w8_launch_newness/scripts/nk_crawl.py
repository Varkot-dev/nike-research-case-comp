import requests,re,json,time,csv,html
from bs4 import BeautifulSoup
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
rows=[]
for p in range(1,60):
    u='https://www.nicekicks.com/sneaker-release-dates/'+('' if p==1 else f'page/{p}/')
    r=requests.get(u,headers={'User-Agent':UA},timeout=40)
    s=BeautifulSoup(r.text,'lxml'); arts=s.select('article.ccard')
    print(p,r.status_code,len(arts),flush=True)
    if not arts: break
    for a in arts:
        el=a.select_one('[data-nk-buy]')
        try: d=json.loads(el['data-nk-buy'])
        except: continue
        rows.append((a.get('data-brand'),a.get('data-model'),d.get('n'),d.get('d'),d.get('ts'),d.get('rp'),d.get('url')))
    time.sleep(1)
csv.writer(open('nk_upcoming.csv','w')).writerows(rows)
print(len(rows))
