import json,sys,urllib.request,urllib.parse,time,os
K=sys.argv[1]; out=sys.argv[2]
base="https://8o6idgupvtb1nqksp.a1.typesense.net/collections/fleetfeet_product_variants_v5/documents/search?"
brands=["Nike","HOKA","On","ASICS","Brooks","Saucony","New Balance","adidas"]
fields="sku.sku,sku.skuName,sku.inventory,product.title,product.slug,product.primaryBrandSlug,product.gender,product.views30,product.views7,product.inventory,product.postDate,product.releaseDate,product.previousVersion,product.surface,product.shoeStyle,computed.discounted,computed.price,computed.originalPrice,product.actualPrice,product.minPrice,product.maxPrice,product.inStock,product.productCta"
res=[]
for b in brands:
    page=1
    while True:
        q={"q":"*","filter_by":f"product.productType:=Shoes && product.brand:=`{b}`","group_by":"sku.sku","group_limit":"1","per_page":"250","page":str(page),"include_fields":fields}
        req=urllib.request.Request(base+urllib.parse.urlencode(q),headers={"X-TYPESENSE-API-KEY":K})
        d=json.load(urllib.request.urlopen(req,timeout=60))
        gh=d.get("grouped_hits",[])
        for g in gh: res.append(g["hits"][0]["document"])
        print(b,page,len(gh),d.get("found"),file=sys.stderr)
        if len(gh)<250: break
        page+=1; time.sleep(0.5)
json.dump(res,open(out,"w"))
print(len(res))
