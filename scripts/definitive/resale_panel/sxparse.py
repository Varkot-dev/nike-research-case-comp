import re,json,gzip,statistics
def parse(raw):
    r1=_parse(raw); r1.update(ldparse(raw)); return r1
def _parse(raw):
    if raw[:2]==b'\x1f\x8b': raw=gzip.decompress(raw)
    t=raw.decode('utf-8','replace')
    m=re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>',t,re.S)
    if not m: return {'err':'no_next_data','title':(re.search(r'<title>(.*?)</title>',t,re.S) or [None,''])[1][:80]}
    d=json.loads(m.group(1))
    try: qs=d['props']['pageProps']['req']['appContext']['states']['query']['value']['queries']
    except Exception: return {'err':'no_queries'}
    gp=gm=None; cur=None
    for q in qs:
        k=q.get('queryKey') or []
        dd=(q.get('state') or {}).get('data') or {}
        if k and k[0]=='GetProduct' and 'product' in dd: gp=dd['product']; cur=json.dumps(k)
        if k and k[0]=='GetMarketData' and 'product' in dd: gm=dd['product']; cur=cur or json.dumps(k)
    if not gp: return {'err':'no_product'}
    cc=re.search(r'"currencyCode": ?"(\w+)"',cur or ''); 
    tr={x['name']:x['value'] for x in gp.get('traits') or []}
    sizes={v['id']:(v.get('traits') or {}).get('size') for v in gp.get('variants') or []}
    basetype={v['id']:((v.get('sizeChart') or {}).get('baseType')) for v in gp.get('variants') or []}
    src=gm or gp
    var=[]
    for v in src.get('variants') or []:
        st=(v.get('market') or {}).get('state') or {}; si=(v.get('market') or {}).get('salesInformation') or {}
        s=sizes.get(v['id'])
        try: sf=float(re.sub(r'[^0-9.]','',s)) if s else None
        except Exception: sf=None
        var.append({'size':s,'sizef':sf,'basetype':basetype.get(v['id']),'lowestAsk':(st.get('lowestAsk') or {}).get('amount'),'lastSale':si.get('lastSale'),'nAsks':st.get('numberOfAsks'),'nBids':st.get('numberOfBids')})
    pm=(src.get('market') or {}); ps=pm.get('state') or {}; psi=pm.get('salesInformation') or {}
    inr=[v for v in var if v['sizef'] is not None and 7<=v['sizef']<=13 and not re.search(r'[A-Za-z]',(v['size'] or '').replace('W','').replace('.',''))]
    ls=[v['lastSale'] for v in inr if v['lastSale']]; la=[v['lowestAsk'] for v in inr if v['lowestAsk']]
    return {'styleId':gp.get('styleId'),'title':gp.get('title'),'gender':gp.get('gender'),'retail':tr.get('Retail Price'),'release':tr.get('Release Date'),'currency':cc.group(1) if cc else None,
      'prod_lastSale':psi.get('lastSale'),'prod_salesLast72h':psi.get('salesLast72Hours'),'prod_lowestAsk':(ps.get('lowestAsk') or {}).get('amount'),'prod_highestBid':(ps.get('highestBid') or {}).get('amount'),'prod_nAsks':ps.get('numberOfAsks'),'prod_nBids':ps.get('numberOfBids'),
      'n_var':len(var),'n_var_7_13':len(inr),'n_sizes_ask_7_13':len(la),'n_sizes_lastsale_7_13':len(ls),
      'med_lastSale_7_13':statistics.median(ls) if ls else None,'med_lowestAsk_7_13':statistics.median(la) if la else None,
      'sum_nAsks_7_13':sum(v['nAsks'] or 0 for v in inr),'size10_lastSale':next((v['lastSale'] for v in inr if v['sizef']==10),None),'size10_lowestAsk':next((v['lowestAsk'] for v in inr if v['sizef']==10),None)}
def ldparse(raw):
    if raw[:2]==b'\x1f\x8b': raw=gzip.decompress(raw)
    t=raw.decode('utf-8','replace'); out={}
    for m in re.finditer(r'<script type="application/ld\+json"[^>]*>(.*?)</script>',t,re.S):
        try: j=json.loads(m.group(1))
        except Exception: continue
        for o in (j if isinstance(j,list) else [j]):
            if isinstance(o,dict) and o.get('@type')=='Product' and isinstance(o.get('offers'),dict):
                of=o['offers']; offs=of.get('offers') or []
                def sz(d):
                    try: return float(re.sub(r'[^0-9.]','',d))
                    except Exception: return None
                core=[x.get('price') for x in offs if sz(x.get('description') or '') is not None and 7<=sz(x.get('description'))<=13 and x.get('price') and not re.search(r'[A-VX-Za-vx-z]',x.get('description') or '')]
                out={'ld_currency':of.get('priceCurrency'),'ld_offerCount':of.get('offerCount'),'ld_lowPrice':of.get('lowPrice'),'ld_highPrice':of.get('highPrice'),'ld_n_size_offers_7_13':len(core),'ld_med_ask_7_13':statistics.median(core) if core else None,'ld_releaseDate':o.get('releaseDate'),'ld_name':o.get('name'),
                     'ld_size10_ask':next((x.get('price') for x in offs if sz(x.get('description') or '')==10),None),'ld_sizes':[x.get('description') for x in offs][:40]}
    sm=re.search(r'Style\s*(?:<[^>]+>\s*)*([A-Z0-9]{6}-[0-9]{3})',t); 
    if sm: out['visible_style']=sm.group(1)
    rm=re.search(r'Retail Price\s*(?:<[^>]+>\s*)*\$(\d+)',t)
    if rm: out['visible_retail']=rm.group(1)
    return out
if __name__=='__main__':
    import sys; print(json.dumps(parse(open(sys.argv[1],'rb').read()),indent=0))
