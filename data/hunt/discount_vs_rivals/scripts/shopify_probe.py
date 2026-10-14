import urllib.request,json,collections,gzip,time
stores="www.stadiumgoods.com capsuletoronto.com www.nrml.ca www.rbrshoes.com www.laceupnyc.com www.rimeshoes.com www.shoegallerymiami.com www.tintoyshoes.com www.sneakerjunkies.com bodega.shop www.addictmiami.com www.rise45.com www.packershoes.com www.oneness287.com www.footpatrol.com www.runnersneed.com www.sneakerbox.com www.thehundreds.com www.solefly.com www.jimmyjazz.com www.trophyroomstore.com shop.premierstore.com www.sneakercage.com www.footdistrict.com www.sizeer.com".split()
for s in stores:
    try:
        r=urllib.request.Request(f"https://{s}/products.json?limit=250",headers={'User-Agent':'Mozilla/5.0 (compatible; research-bot/1.0)','Accept-Encoding':'gzip'})
        d=urllib.request.urlopen(r,timeout=25).read()
        try:d=gzip.decompress(d)
        except: pass
        j=json.loads(d)['products']
        v=collections.Counter(p['vendor'] for p in j)
        cmp=sum(1 for p in j for x in p['variants'] if x.get('compare_at_price'))
        print(s,len(j),cmp,v.most_common(6),flush=True)
    except Exception as e: print(s,'ERR',str(e)[:40],flush=True)
    time.sleep(1)
