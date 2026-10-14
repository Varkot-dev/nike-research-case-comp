import json,sys,collections,re
D=json.load(open(sys.argv[1]))
seen={}
for d in D: seen[d['sku.sku']]=d
D=list(seen.values())
def brand(d): return d['product.title'].split('|')[-1].strip().split(' ')[0]
print("unique skus",len(D))
agg=collections.defaultdict(lambda:dict(n=0,disc=0,dep=0.0,inv=0,invdisc=0,full=0))
for d in D:
    inv=d.get('sku.inventory') or 0
    if inv<=0: continue
    b=d['product.title'].split('|')[-1].strip()
    br=None
    for x in ["Nike","HOKA","On ","ASICS","Brooks","Saucony","New Balance","adidas"]:
        if b.startswith(x): br=x.strip()
    if not br: continue
    a=agg[br]; a['n']+=1; a['inv']+=inv
    orig=d.get('computed.originalPrice') or 0; p=d.get('computed.price') or 0
    if d.get('computed.discounted') and orig>p:
        a['disc']+=1; a['dep']+=1-p/orig; a['invdisc']+=inv
print("brand, in-stock colorways, % colorways discounted, avg depth, units in stock, % units on discounted colorways")
for b,a in sorted(agg.items(),key=lambda x:-x[1]['inv']):
    print(f"{b:12s} {a['n']:5d} {100*a['disc']/a['n']:5.1f}% {100*a['dep']/max(a['disc'],1):5.1f}% {a['inv']:7d} {100*a['invdisc']/a['inv']:5.1f}%")
