import re,sys,pathlib
f=pathlib.Path(sys.argv[1]); n=int(sys.argv[2]) if len(sys.argv)>2 else 45
L=f.read_text().split('\n'); page='?'; pg=[]
for l in L:
    m=re.match(r'\[\[page (\d+)\]\]',l)
    if m: page=m.group(1)
    pg.append(page)
# find first line in prepared remarks (before Q&A) matching expectation of revenue
qa=next((i for i,l in enumerate(L) if re.search(r'(?i)question-and-answer|questions? and answers?|operator\]?:? ?(we will now|at this time)',l) and i>150),len(L))
cands=[i for i,l in enumerate(L[:qa]) if re.search(r'(?i)(we|we now|we continue to) (expect|anticipate|are planning)',l) and re.search(r'(?i)revenue|revenues',' '.join(L[i:i+2]))]
cands=[i for i in cands if i>200] or cands
s=cands[0]-3 if cands else 0
for i in range(s,min(s+n,len(L))):
    if L[i].strip() and not L[i].startswith('[[page'): print(pg[i],'|',L[i].strip())
