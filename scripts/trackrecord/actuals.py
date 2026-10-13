import csv,sys,collections
facts=sys.argv[1]; out=sys.argv[2]
d=collections.defaultdict(dict)
for r in csv.DictReader(open(facts)):
    k=(r['metric'],r['period'])
    if r['period'] not in d[r['metric']]: d[r['metric']][r['period']]=r
def v(m,p):
    r=d[m].get(p); return (float(r['value']),r['filing'],r['page']) if r else (None,'','')
periods=[f'Q{q}FY{y}' for y in range(2022,2028) for q in range(1,5)]+[f'FY{y}' for y in range(2017,2027)]
rows=[]
def prior(p):
    if p.startswith('FY'): return f'FY{int(p[2:])-1}'
    return p[:4]+str(int(p[4:])-1)
for p in periods:
    rev=v('revenues',p)
    if rev[0] is None: continue
    pr=prior(p); rp=v('revenues',pr); sga=v('total_selling_admin_expense',p); sgap=v('total_selling_admin_expense',pr)
    oh=v('operating_overhead_expense',p); ohp=v('operating_overhead_expense',pr)
    dc=v('demand_creation_expense',p); gm=v('gross_margin_pct',p); gmp=v('gross_margin_pct',pr)
    gmc=v('gross_margin_change_bps',p); tax=v('effective_tax_rate_pct',p); eps=v('eps_diluted',p)
    g=lambda a,b: round((a/b-1)*100,1) if a is not None and b is not None else ''
    cn=v('growth_revenues_cn_pct',p)
    rows.append(dict(period=p,revenue_usd_m=rev[0],revenue_growth_reported_pct_calc=g(rev[0],rp[0]),
      revenue_growth_cn_pct=cn[0] if cn[0] is not None else '',
      gross_margin_pct=gm[0],gm_change_bps_reported=gmc[0] if gmc[0] is not None else '',
      gm_change_bps_calc=round((gm[0]-gmp[0])*100) if gm[0] is not None and gmp[0] is not None else '',
      sga_usd_m=sga[0],sga_growth_pct_calc=g(sga[0],sgap[0]),overhead_usd_m=oh[0],overhead_growth_pct_calc=g(oh[0],ohp[0]),
      demand_creation_usd_m=dc[0],tax_rate_pct=tax[0],eps_diluted=eps[0],
      source_revenue=f"{rev[1]} {rev[2]}",source_sga=f"{sga[1]} {sga[2]}",source_tax_eps=f"{tax[1]} {tax[2]} / {eps[1]} {eps[2]}"))
w=csv.DictWriter(open(out,'w',newline=''),fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
for r in rows: print(r['period'],r['revenue_usd_m'],r['revenue_growth_reported_pct_calc'],r['revenue_growth_cn_pct'],r['gross_margin_pct'],r['gm_change_bps_reported'],r['gm_change_bps_calc'],r['sga_usd_m'],r['sga_growth_pct_calc'],r['overhead_usd_m'],r['overhead_growth_pct_calc'],r['demand_creation_usd_m'],r['tax_rate_pct'],r['eps_diluted'])
