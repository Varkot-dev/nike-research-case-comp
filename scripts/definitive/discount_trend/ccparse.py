import json,re,sys,statistics as st
rows=[]
for l in open(sys.argv[1]):
    m=json.loads(l); t=open(m['file'],'rb').read().decode('utf8','ignore')
    c=re.findall(r'wall-header__item_count[^>]*>\(([0-9,]+)\)',t)
    tr=re.findall(r'"totalResources":([0-9]+)',t)
    n=int(c[0].replace(',','')) if c else (int(tr[0]) if tr else None)
    # card prices
    cards=t.split('data-testid="product-card"')[1:]
    disc=[]; nd=0
    for cd in cards:
        cd=cd[:6000]
        cur=re.findall(r'data-testid="product-price-reduced"[^>]*>\$([0-9.,]+)',cd)
        full=re.findall(r'data-testid="product-price"[^>]*>\$([0-9.,]+)',cd)
        if cur and full:
            a=float(cur[0].replace(',','')); b=float(full[0].replace(',',''))
            if b>0: disc.append(100*(1-a/b))
        elif full: nd+=1
    rows.append((m['url'].replace('https://www.nike.com',''),m['ts'][:8],n,len(cards),len(disc),nd,round(st.mean(disc),1) if disc else None))
for r in sorted(set(rows)): print(*r)
