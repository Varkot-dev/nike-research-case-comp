import re,json,sys
s=open(sys.argv[1]).read()
i=s.find('"facetField":"realBrandNameFacet"')
j=s.find('"values":[',i); k=s.find(']',j)
vals=json.loads(s[j+9:k+1])
d={v['name']:v['count'] for v in vals}
tot=re.findall(r'"totalResultCount":"?(\d+)',s)
print('total',tot[:1])
for b in sys.argv[2:]: print(b,d.get(b))
