import json,csv,statistics as S,datetime as dt,collections,os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from sxparse import parse
P='/tmp/claude-0/-home-user-nike-research-case-comp/c6360f77-8844-5e04-9011-d8ceb3c498c8/scratchpad/dt/resale_panel'
base={r['goat_id']:r for r in csv.DictReader(open('/home/user/nike-research-case-comp/data/jordan_resale_goat_20261013.csv'))}
caps=json.load(open(P+'/caps_parsed.json'))
rows=[]
for gid,c in caps.items():
    if not c.get('slug'): continue
    b=base[gid]; rel=dt.date.fromisoformat(b['release_date']); ret=float(b['retail_usd'])
    seen={}
    for x in c['caps']:
        if x['ts'] in seen: seen[x['ts']]['targets'].append(x['target']); continue
        if not os.path.exists(x['file']): continue
        p=parse(open(x['file'],'rb').read())
        ask=p.get('ld_med_ask_7_13') or p.get('med_lowestAsk_7_13'); cur=p.get('ld_currency') or p.get('currency')
        if not ask or cur not in ('USD',None): continue
        d=dt.date(int(x['ts'][:4]),int(x['ts'][4:6]),int(x['ts'][6:8]))
        r=dict(goat_id=gid,line=b['line'],name=b['name'],gender=b['gender'],style_code=b['style_code'],stockx_style=p.get('styleId') or p.get('visible_style'),stockx_slug=c['slug'],release_date=b['release_date'],
          retail_usd=ret,stockx_retail=p.get('retail') or p.get('visible_retail'),targets=[x['target']],capture_date=d.isoformat(),capture_ts=x['ts'],age_days=(d-rel).days,
          sx_med_ask_7_13=ask,ask_basis='ld+json offers' if p.get('ld_med_ask_7_13') else 'GetMarketData lowestAsk',sx_med_lastSale_7_13=p.get('med_lastSale_7_13'),sx_size10_ask=p.get('ld_size10_ask') or p.get('size10_lowestAsk'),
          sx_total_asks=p.get('ld_offerCount') or p.get('prod_nAsks'),sx_total_bids=p.get('prod_nBids'),sx_salesLast72h=p.get('prod_salesLast72h'),n_sizes_ask_7_13=p.get('ld_n_size_offers_7_13') or p.get('n_sizes_ask_7_13'),
          premium_ask_DERIVED=round(ask/ret-1,4),premium_lastSale_DERIVED=round(p['med_lastSale_7_13']/ret-1,4) if p.get('med_lastSale_7_13') else None,
          source='StockX product page via Wayback capture (ld+json AggregateOffer or __NEXT_DATA__ GetMarketData)',wayback_url=x['url'],size_basis='median per-size lowest ask, StockX default size label 7-13 (men US M; women US W)',label='VERIFIED (archived page opened); premium DERIVED')
        seen[x['ts']]=r; rows.append(r)
for r in rows: r['targets']='|'.join(r['targets'])
rows.sort(key=lambda r:(r['line'],r['release_date'],r['capture_date']))
w=csv.DictWriter(open(P+'/resale_panel_stockx_wayback.csv','w',newline=''),fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print('shoes',len({r['goat_id'] for r in rows}),'points',len(rows))
print(collections.Counter(r['line'] for r in {r['goat_id']:r for r in rows}.values()))
json.dump(rows,open(P+'/panel_rows.json','w'))
