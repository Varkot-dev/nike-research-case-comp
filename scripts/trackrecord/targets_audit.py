import csv,sys
facts=sys.argv[1]; T=sys.argv[2]
d={}
for r in csv.DictReader(open(facts)):
    d.setdefault((r['metric'],r['period']),r)
def v(m,p): return float(d[(m,p)]['value'])
def src(m,p): r=d[(m,p)]; return f"{r['filing']} {r['page']}"
cagr=lambda a,b,n: round(((b/a)**(1/n)-1)*100,1)
rows=[]
def add(prog,target,metric,window,actual,verdict,source):
    rows.append(dict(program=prog,target=target,metric=metric,window=window,actual=actual,verdict=verdict,source=source))
# 2017 targets: through FY2023 on average per year (FY2019 10-K p.24); base FY2017
r17,r22,r23=v('revenues','FY2017'),v('revenues','FY2022'),v('revenues','FY2023')
add('Oct 2017 Investor Day','High single-digit revenue growth (avg per year through FY2023)','Revenue CAGR','FY2017 to FY2023',f"{cagr(r17,r23,6)}% (34,350 to 51,217); FY17 to FY22 {cagr(r17,r22,5)}%",'miss (below 7%)','my arithmetic on revenues, FY2019 10-K p. 26 and FY2023 10-K')
g17,g23,g22=v('gross_margin_pct','FY2017'),v('gross_margin_pct','FY2023'),v('gross_margin_pct','FY2022')
add('Oct 2017 Investor Day','Gross margin expansion of as much as 50 bps per year','Gross margin change','FY2017 to FY2023',f"{round((g23-g17)*100)} bps total ({g17}% to {g23}%); peak FY2022 {g22}% = +{round((g22-g17)*100)} bps over 5 yrs = {round((g22-g17)*100/5)} bps/yr",'miss','my arithmetic on gross_margin_pct')
s17=v('total_selling_admin_expense','FY2017')/r17*100; s23=v('total_selling_admin_expense','FY2023')/r23*100
add('Oct 2017 Investor Day','Slight SG&A leverage','SG&A % revenue','FY2017 to FY2023',f"{s17:.1f}% to {s23:.1f}% (deleverage)",'miss','my arithmetic')
e17,e22,e23=v('eps_diluted','FY2017'),v('eps_diluted','FY2022'),v('eps_diluted','FY2023')
add('Oct 2017 Investor Day','Mid-teens EPS growth','Diluted EPS CAGR','FY2017 to FY2023',f"{cagr(e17,e23,6)}% ({e17} to {e23}); FY17 to FY22 {cagr(e17,e22,5)}%",'miss','my arithmetic on eps_diluted')
add('Oct 2017 Investor Day','Low-30s ROIC','ROIC','FY2020 to FY2023',"FY20 21.5%, FY21 48.8%, FY22 46.5%, FY23 31.5% (FY18 and FY19 not in repo)",'mixed (met 3 of 4 years shown)','FY2021 10-K p. 30; FY2022 10-K p. 30; FY2023 10-K p. 30')
na17,na22=v('revenue_north_america','FY2017'),v('revenue_north_america','FY2022')
add('Oct 2017 Investor Day','International to contribute 75% of incremental growth over next five years (Q2 FY18 call p. 7)','Non-North America share of revenue growth','FY2017 to FY2022',f"{round(100*(1-(na22-na17)/(r22-r17)))}% (NIKE Inc. +{r22-r17:.0f}M, North America +{na22-na17:.0f}M)",'met','my arithmetic on revenues and revenue_north_america')
add('Oct 2017 Investor Day','North America mid-single-digit growth (Q2 FY18 call p. 14)','NA revenue CAGR','FY2017 to FY2022',f"{cagr(na17,na22,5)}%",'miss (low end)','my arithmetic')
add('Oct 2017 Investor Day (reported in Q2 FY19 call p. 6)','Owned + partnered digital 30% of business by 2023 (from about 15%)','Digital penetration','FY2021',"Q1 FY21 call: digital across owned and partner 'now represents over 30% of our total business'",'met early (pandemic year)','Q1 FY21 call p. 6 ; management claim, partner digital not audited')
add('2015 Investor Day, reaffirmed Oct 2017','$50B revenue by FY2020, then "within the next five years" (Parker, Oct 2017, secondary)','Revenue level','FY2020 to FY2023',f"FY20 {v('revenues','FY2020'):.0f}, FY22 {r22:.0f}, FY23 {r23:.0f} (first year above $50B)",'late (met in FY2023)','Retail Dive Oct 26 2017 (secondary); revenues from facts')
# June 2020
add('Jun 2020 (Q4 FY20 call p. 3, 6)','Reach 30% digital penetration this coming year; owned + partnered digital to 50% of business','Digital penetration','FY2021 onward',"30% met (Q1 FY21 call). 50% not verifiable: partner digital never disclosed; owned NIKE Brand Digital peaked at 12.6B = 26% of NIKE Brand revenue (FY23)",'30%: met; 50%: not met on owned basis','my arithmetic: 12.6/48.763 (FY2023 10-K p. 33, 36)')
# June 2021 through FY25
r21,r25=v('revenues','FY2021'),v('revenues','FY2025')
add('Jun 2021 (Q4 FY21 call p. 12, 13; IR outlook PDF)','HSD to LDD revenue growth through FY25','Revenue CAGR','FY2021 to FY2025',f"{cagr(r21,r25,4)}%",'miss','my arithmetic')
add('Jun 2021','Gross margin high 40s by FY25','Gross margin','FY2025',f"{v('gross_margin_pct','FY2025')}% (peak {g22}% in FY22)",'miss','FY2025 10-K')
add('Jun 2021','EBIT margin high teens by FY25','EBIT margin','FY2025',f"{v('ebit_margin_pct','FY2025')}% (FY21 {v('ebit_margin_pct','FY2021')}%)",'miss','Q4 FY25 release; FY2021 10-K p. 36')
e21,e25=v('eps_diluted','FY2021'),v('eps_diluted','FY2025')
add('Jun 2021','Mid-to-high-teens EPS growth on average','EPS CAGR','FY2021 to FY2025',f"{cagr(e21,e25,4)}% ({e21} to {e25})",'miss','my arithmetic')
add('Jun 2021','ROIC above low-30% range','ROIC','FY2022 to FY2025',"46.5%, 31.5%, 34.9%, 20.2%",'met FY22, FY24; missed FY23 (borderline), FY25','10-K ROIC tables')
add('Jun 2021','Capex roughly 3% of revenue','Capex % revenue','FY2022 to FY2025',', '.join(f"FY{y[-2:]} {100*v('capex',y)/v('revenues',y):.1f}%" for y in ['FY2022','FY2023','FY2024','FY2025']),'below target (under-spend)','my arithmetic')
add('Jun 2021','NIKE Direct about 60% of NIKE Brand business in FY25','NIKE Direct share','FY2025',f"{v('nike_direct_share_of_nike_brand_pct','FY2025'):.0f}%",'miss','FY2025 10-K p. 29')
dg25=v('revenue_nike_brand_digital','FY2025')*1000/v('revenue_nike_brand','FY2025')*100
add('Jun 2021','NIKE owned Digital 40% of business in FY25; owned + partnered 50%','Owned digital share of NIKE Brand','FY2025',f"{dg25:.1f}% (9.6B / 44.7B)",'miss','my arithmetic, FY2025 10-K p. 34, 37')
w21,w25=v('revenue_wholesale','FY2021'),v('revenue_wholesale','FY2025')
add('Jun 2021','Wholesale roughly flat vs FY21','NIKE Brand wholesale','FY2025',f"{w21:.0f} to {w25:.0f} ({100*(w25/w21-1):.1f}%)",'in line',"FY2021 10-K p. 32; FY2025 10-K p. 33")
add('Jun 2021 (Q4 FY21 call p. 13)','FY22 revenue to grow LDD and surpass $50 billion','FY22 revenue','FY2022',f"{r22:.0f} (+{100*(r22/r21-1):.1f}%)",'miss','FY2022 10-K')
w=csv.DictWriter(open(f'{T}/longterm_targets_vs_actual.csv','w',newline=''),fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
for r in rows: print(r['target'][:60],'|',r['actual'],'|',r['verdict'])
# $2B audit
eci={'FY2024':4.1,'FY2025':3.5,'FY2026':3.1}  # BLS ECI private wages & salaries, 12-mo change, Q2 of calendar year in which FY ends
base=v('operating_overhead_expense','FY2023'); charges={'FY2023':0,'FY2024':379,'FY2025':0,'FY2026':231}
emp={'FY2023':83700,'FY2024':79400,'FY2025':77800,'FY2026':73000}
A=[]; path=base; cum=0
for y in ['FY2023','FY2024','FY2025','FY2026']:
    oh=v('operating_overhead_expense',y); ex=oh-charges[y]; rev=v('revenues',y); dc=v('demand_creation_expense',y); sga=v('total_selling_admin_expense',y)
    if y!='FY2023': path=path*(1+eci[y]/100)
    gap=path-ex if y!='FY2023' else 0; cum+=gap
    revpath=base*rev/v('revenues','FY2023')
    A.append(dict(fiscal_year=y,operating_overhead_reported=oh,charges_in_overhead=charges[y],overhead_ex_charges=ex,overhead_ex_charges_pct_revenue=round(ex/rev*100,2),
      eci_wage_inflation_pct=eci.get(y,''),overhead_if_grown_with_wage_inflation=round(path),gap_vs_inflation_path=round(gap),cumulative_gap=round(cum),
      overhead_if_scaled_to_revenue=round(revpath),gap_vs_revenue_scaled=round(revpath-ex),demand_creation=dc,sga_reported=sga,sga_pct_revenue=round(sga/rev*100,2),
      revenue=rev,employees=emp[y],overhead_ex_charges_per_employee_k=round(ex/emp[y]*1000,1),
      source='operating_overhead_expense, demand_creation_expense, total_selling_admin_expense, revenues: data/nike_filing_facts.csv (10-Ks); charges: FY24 10-K p. 91 (379 opex), FY26 10-K p. 89 (231 in overhead); employees: 10-K p. 6 each year; ECI: BLS series CIU2020000000000A (api.bls.gov); all derived columns my arithmetic'))
w=csv.DictWriter(open(f'{T}/savings_audit_overhead.csv','w',newline=''),fieldnames=list(A[0].keys())); w.writeheader(); w.writerows(A)
for a in A: print({k:a[k] for k in list(a)[:-1]})
