"""T4 China gap table (Nike GC cc vs foreign peers in China and domestic sell-through) and T2b gross-margin gap (Nike yoy bps minus peer median)."""
import csv, collections, statistics as st
B='/home/user/nike-research-case-comp/data/hunt/peers_reported'
G=collections.defaultdict(list)
for r in csv.DictReader(open(B+'/panel_growth_comparable.csv')): G[(int(r['cal_year']),int(r['cal_q']))].append(r)
X={}
for r in csv.DictReader(open(B+'/china_peers_sellthrough_quarterly.csv')):
    if r['series']=='Xtep core brand' and r['metric']!='retail_sellthrough_yoy_pct': X[(int(r['cal_year']),int(r['cal_q']),r['metric'])]=float(r['value'])
out=[]
for k in sorted(G):
    if k<(2023,1): continue
    nk=[float(r['growth_pct']) for r in G[k] if r['series']=='Nike Greater China']
    fo=[float(r['growth_pct']) for r in G[k] if r['region']=='Greater China' and r['is_nike']=='0']
    do=[float(r['growth_pct']) for r in G[k] if r['region'].startswith('Greater China (')]
    out.append(dict(cal_year=k[0],cal_q=k[1],nike_gc_cc=nk[0] if nk else None,foreign_peer_median=st.median(fo) if fo else None,domestic_sellthrough_median=st.median(do) if do else None,
        gap_vs_foreign=round(nk[0]-st.median(fo),2) if nk and fo else None,gap_vs_domestic=round(nk[0]-st.median(do),2) if nk and do else None,
        xtep_retail_discount_pct=X.get((k[0],k[1],'retail_discount_pct')),xtep_channel_inventory_months=X.get((k[0],k[1],'channel_inventory_turnover_months'))))
with open(B+'/test_T4_china.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
for r in out: print(r)
d=collections.defaultdict(dict)
for r in csv.DictReader(open(B+'/panel_company_quarterly.csv')):
    if r['gm_yoy_bps']: d[(int(r['cal_year']),int(r['cal_q']))][r['company']]=float(r['gm_yoy_bps'])
gm=[]
for k in sorted(d):
    if k<(2023,1): continue
    p=[v for c,v in d[k].items() if c!='nike']
    if 'nike' in d[k] and p: gm.append(dict(cal_year=k[0],cal_q=k[1],nike_gm_yoy_bps=d[k]['nike'],peer_median_gm_yoy_bps=st.median(p),gap_bps=d[k]['nike']-st.median(p),n_peers=len(p),note='CQ2 2026 distorted by IEEPA tariff refunds at Nike and several peers' if k==(2026,2) else ''))
with open(B+'/test_T2b_gm_gap.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(gm[0])); w.writeheader(); w.writerows(gm)
for r in gm: print(r)
