import sys,re
f=sys.argv[1]
for q in sys.argv[2:]:
    pg='?'; hits=[]
    for line in open(f,errors='ignore'):
        m=re.match(r'=== PAGE (\d+) \| printed: (\S+) ===',line)
        if m: pg=m.group(2); continue
        if q in line: hits.append(pg)
    print(repr(q[:60]),'->',hits[:6])
