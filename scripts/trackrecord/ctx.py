import re,sys
f,pat=sys.argv[1],sys.argv[2]; B=int(sys.argv[3]) if len(sys.argv)>3 else 3; A=int(sys.argv[4]) if len(sys.argv)>4 else 8
L=open(f).read().split('\n'); pg=[];p='?'
for l in L:
    m=re.match(r'\[\[page (\d+)\]\]',l)
    if m:p=m.group(1)
    pg.append(p)
last=-1
for i,l in enumerate(L):
    if re.search(pat,l,re.I) and i>last:
        s=max(0,i-B); e=min(len(L),i+A); print('---')
        for j in range(s,e):
            if L[j].strip() and not L[j].startswith('[[page'): print(f'p{pg[j]} | {L[j].strip()}')
        last=e
