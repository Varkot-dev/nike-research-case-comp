import re,glob,csv
from bs4 import BeautifulSoup
rows=[]
for f in sorted(glob.glob('sbd_*.html')):
    s=BeautifulSoup(open(f).read(),'lxml')
    t=[x for x in s.get_text('\n',strip=True).split('\n')]
    for i,l in enumerate(t):
        if l.startswith('Release Date:') and i>=3:
            # find name: go back to line before 'Color:' 
            j=i-1
            while j>0 and not t[j].startswith('Style Code:'): j-=1
            sc=t[j].replace('Style Code:','').strip()
            k=j-1
            while k>0 and not t[k].startswith('Color:'): k-=1
            name=t[k-1]
            price=''
            if i+1<len(t) and t[i+1].startswith('Price:'): price=t[i+1][6:].strip()
            rows.append((name,sc,l[13:].strip(),price,f))
print(len(rows))
w=csv.writer(open('sbd_raw.csv','w'));w.writerow(['name','style','date','price','file']);w.writerows(rows)
