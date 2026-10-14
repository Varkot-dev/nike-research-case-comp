import json,sys,collections,re
D=list({d['sku.sku']:d for d in json.load(open(sys.argv[1]))}.values())
pat=sys.argv[2] if len(sys.argv)>2 else None
m=collections.defaultdict(lambda:dict(n=0,disc=0,inv=0,invd=0,views=set(),price=[],orig=[]))
for d in D:
    inv=d.get('sku.inventory') or 0
    if inv<=0: continue
    t=re.sub(r"^(Men's|Women's|Unisex|Kids'|Big Kids'|Little Kids')\s*\|\s*","",d['product.title']).strip()
    a=m[t]; a['n']+=1; a['inv']+=inv
    a['views'].add((d['product.slug'],d.get('product.views30') or 0))
    o=d.get('computed.originalPrice') or 0;p=d.get('computed.price') or 0
    a['price'].append(p)
    if d.get('computed.discounted') and o>p: a['disc']+=1;a['invd']+=inv;a['orig'].append(o)
rows=sorted(m.items(),key=lambda x:-x[1]['inv'])
for t,a in rows:
    if pat and not re.search(pat,t,re.I): continue
    v=sum(x[1] for x in a['views'])
    print(f"{t[:42]:42s} cw={a['n']:4d} disc={100*a['disc']/a['n']:5.1f}% units={a['inv']:6d} unitsdisc={100*a['invd']/max(a['inv'],1):5.1f}% views30={v:7d} medprice={sorted(a['price'])[len(a['price'])//2]}")
