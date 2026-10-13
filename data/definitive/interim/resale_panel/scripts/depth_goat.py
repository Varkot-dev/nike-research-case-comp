import json,csv,statistics,collections
P='/tmp/claude-0/-home-user-nike-research-case-comp/c6360f77-8844-5e04-9011-d8ceb3c498c8/scratchpad/dt/resale_panel'
bb=json.load(open('/tmp/claude-0/-home-user-nike-research-case-comp/c6360f77-8844-5e04-9011-d8ceb3c498c8/scratchpad/rh/resale/raw/buybar.json'))
rows=list(csv.DictReader(open('/home/user/nike-research-case-comp/data/jordan_resale_goat_20261013.csv')))
out=[]
for r in rows:
    d=bb.get(r['goat_id'])
    if not d: continue
    sz=collections.defaultdict(dict)
    for v in d['data']:
        if v['shoeCondition']!='new_no_defects' or v['boxCondition']!='good_condition': continue
        s=v['sizeOption']['value']
        sz[s]=v
    allsz=[s for s in sz]; in7=[s for s in sz if 7<=s<=13]
    st=collections.Counter(sz[s]['stockStatus'] for s in in7)
    ask=[s for s in in7 if sz[s].get('lowestPriceCents',{}).get('amount')]
    askall=[s for s in allsz if sz[s].get('lowestPriceCents',{}).get('amount')]
    ret=float(r['retail_usd']) if r['retail_usd'] else None
    below=[s for s in ask if ret and sz[s]['lowestPriceCents']['amount']/100<ret]
    out.append({'goat_id':r['goat_id'],'line':r['line'],'name':r['name'],'release_year':r['release_year'],'gender':r['gender'],'collab_or_special':r['collab_or_special'],
      'n_sizes_listed_all':len(allsz),'n_sizes_7_13':len(in7),'n_sizes_with_ask_7_13':len(ask),'n_sizes_with_ask_all':len(askall),'n_sizes_ask_below_retail_7_13':len(below),'share_sizes_ask_below_retail_DERIVED':round(len(below)/len(ask),3) if ask else None,'n_multiple_in_stock_7_13':st.get('multiple_in_stock',0),'n_single_in_stock_7_13':st.get('single_in_stock',0),'n_not_in_stock_7_13':st.get('not_in_stock',0),
      'share_multiple_DERIVED':round(st.get('multiple_in_stock',0)/len(in7),3) if in7 else None,'premium_primary_DERIVED':r['premium_primary_DERIVED'],'source_url':d['url'],'observed_utc':d['observed_utc']})
w=csv.DictWriter(open(P+'/goat_depth_20261013.csv','w',newline=''),fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
print('statuses seen',collections.Counter(v['stockStatus'] for d in bb.values() if isinstance(d,dict) and 'data' in d for v in d['data']))
for line in ['AJ1 High OG','AJ3','AJ4','AJ5','AJ11']:
  for yr in ['2023','2024','2025','2026','all']:
    g=[o for o in out if o['line']==line and o['collab_or_special']=='False' and (yr=='all' or o['release_year']==yr)]
    if not g: continue
    print(line,yr,len(g),'askall med',statistics.median(o['n_sizes_with_ask_all'] for o in g),'ask7-13 med',statistics.median(o['n_sizes_with_ask_7_13'] for o in g),'share below retail',round(statistics.mean(o['share_sizes_ask_below_retail_DERIVED'] for o in g if o['share_sizes_ask_below_retail_DERIVED'] is not None),2))
