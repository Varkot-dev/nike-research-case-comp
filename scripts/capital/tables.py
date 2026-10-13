import csv,sys
D=sys.argv[1]
def W(name,hdr,rows):
    with open(f'{D}/{name}','w',newline='') as f:
        w=csv.writer(f); w.writerow(hdr); w.writerows(rows)
# cash flow
P=['FY2019','FY2020','FY2021','FY2022','FY2023','FY2024','FY2025','FY2026','Q1FY2026','Q1FY2027']
cfo=[5903,2485,6657,5188,5841,7429,3698,2868,222,135]
capex=[1119,1086,695,758,969,812,430,684,207,199]
div=[1332,1452,1638,1837,2012,2169,2300,2407,591,610]
bb=[4286,3067,608,4014,5480,4250,2985,146,126,0]
ar=[-270,1239,-1606,-504,489,-329,-257,-1207,-215,695]
inv=[-490,-1854,507,-1676,-133,908,120,-31,-610,-312]
pre=[-203,-654,-182,-845,-644,-260,-224,519,-165,-10]
ap=[1525,24,1326,1365,-225,397,-426,-959,93,-1219]
sbc=[325,429,611,638,755,804,709,715,185,158]
ni=[4029,2539,5727,6046,5070,5700,3219,3108,727,712]
rcash=['n/d','n/d','n/d (FY21 charges 294)','n/d','n/d',123,247,142,'n/d','about 243 (accrual "substantially all" paid)']
intpaid=[153,140,293,290,347,381,389,323,'n/d','n/d']
src=['FY21 10-K p. 60','FY21 10-K p. 60','FY23 10-K p. 58; FY21 10-K p. 60','FY23 10-K p. 58','FY23 10-K p. 58','FY26 10-K p. 58','FY26 10-K p. 58','FY26 10-K p. 58','Q1 FY27 10-Q p. 4','Q1 FY27 10-Q p. 4']
rows=[]
for i,p in enumerate(P):
    fcf=cfo[i]-capex[i]; wc=ar[i]+inv[i]+pre[i]+ap[i]
    rows.append([p,ni[i],cfo[i],capex[i],fcf,div[i],bb[i],(round(100*div[i]/fcf) if fcf>0 and p.startswith('FY') else 'n/m (quarter or FCF<0)'),fcf-div[i]-bb[i],ar[i],inv[i],pre[i],ap[i],wc,sbc[i],rcash[i],intpaid[i],src[i]])
W('cashflow_fy2019_q1fy2027.csv',['period','net_income','cash_from_operations','capex','fcf_cfo_minus_capex_my_arithmetic','dividends_paid','share_repurchases','dividends_pct_of_fcf','fcf_after_div_and_buybacks','wc_accounts_receivable','wc_inventories','wc_prepaid_and_other_assets','wc_payables_accrued_and_other_liabs','wc_total','stock_based_comp','restructuring_severance_cash','interest_paid','source'],rows)
# dividends
dps=[0.86,0.955,1.07,1.19,1.325,1.45,1.57,1.63]
eps=[2.49,1.60,3.56,3.75,3.23,3.73,2.16,2.10]
raise_=[('Nov 2018 (release not opened)','0.20 to 0.22 (inferred: 0.86 = 0.20 + 3 x 0.22)','n/d'),('2019-11-14','0.22 to 0.245','11%'),('2020-11-19','0.245 to 0.275','12%'),('2021-11-18','0.275 to 0.305','11%'),('2022-11-15','0.305 to 0.340','11%'),('2023-11-14','0.340 to 0.370','9%'),('2024-11-14','0.37 to 0.40','8%'),('2025-11-20','0.40 to 0.41','3%')]
streak=[17,18,19,20,21,22,23,24]
rows=[]
for i,p in enumerate(P[:8]):
    fcf=cfo[i]-capex[i]
    rows.append([p,dps[i],eps[i],round(100*dps[i]/eps[i]),round(100*div[i]/fcf),raise_[i][0],raise_[i][1],raise_[i][2],streak[i]])
rows.append(['FY2027 guide','1.64 run-rate (0.41 x 4)','1.15 to 1.35 adjusted','121 to 143 (adjusted)','see forward model','Nov 2026 window (not yet declared)','0.41 to ?','?','25 if raised'])
W('dividend_history.csv',['fiscal_year','dps_declared','diluted_eps_gaap','payout_of_eps_pct_my_arithmetic','dividends_pct_of_fcf_my_arithmetic','raise_declared_date','quarterly_rate_change','raise_pct','consecutive_years_of_increase_after_raise'],rows)
# debt
W('debt_schedule.csv',['maturity','fiscal_year_due','coupon_pct','principal_usd_m','book_value_may31_2026','swapped_to_floating','indicative_yield_oct13_2026_secondary','source'],[
 ['2026-11-01','FY2027',2.38,1000,1000,'no','n/a (matures in 19 days)','FY26 10-K p. 70'],
 ['2027-03-27','FY2027',2.75,1000,1000,'no','4.81% at 99.1 clean (finanzen.net, quote time stale)','FY26 10-K p. 70'],
 ['2030-03-27','FY2030',2.85,1500,1495,'no','5.49% at 91.9 (finanzen.net, gettex, Oct 13, 2026)','FY26 10-K p. 70'],
 ['2040-03-27','FY2040',3.25,1000,986,'yes','n/d','FY26 10-K p. 70'],
 ['2043-05-01','FY2043',3.63,500,497,'yes','n/d','FY26 10-K p. 70'],
 ['2045-11-01','FY2046',3.88,1000,987,'yes','6.43% at 72.4 (finanzen.net, gettex, Oct 13, 2026)','FY26 10-K p. 70'],
 ['2046-11-01','FY2047',3.38,500,493,'no','n/d','FY26 10-K p. 70'],
 ['2050-03-27','FY2050',3.38,1500,1484,'no','6.47% at 63.2 (finanzen.net, gettex, Oct 13, 2026)','FY26 10-K p. 70'],
 ['TOTAL','',round((1000*2.38+1000*2.75+1500*2.85+1000*3.25+500*3.63+1000*3.88+500*3.38+1500*3.38)/8000,2),8000,7942,'2.4B notional','','FY26 10-K p. 70; weighted coupon my arithmetic'],
 ['Revolver 5-year $2.0B (to $3.0B), matures 2030-03-07','','Term SOFR + 0.725%; fee 0.05%',0,'','','undrawn','FY26 10-K p. 69'],
 ['Revolver 364-day $1.0B (to $1.5B), matures 2027-03-05','','Term SOFR + 0.625%; fee 0.03%',0,'','','undrawn','FY26 10-K p. 69'],
 ['Commercial paper program $3.0B','','',0,'','','none outstanding Aug 31, 2026','Q1 FY27 10-Q p. 34'],
])
W('ratings_history.csv',['date','agency','action','rating_after','outlook','source'],[
 ['FY2019 to FY2024 10-Ks','S&P / Moody\'s','held','AA- / A1','','FY19 10-K p. 39 through FY24 10-K p. 47'],
 ['2024-10 (article Oct 20, 2024)','S&P','outlook to negative, AA- affirmed','AA-','negative','secondary: SGB Media, opened'],
 ['2025-07 (article Jul 16, 2025)','S&P','downgrade one notch','A+','stable','secondary: SGB Media, opened; FY25 10-K p. 46 shows A+ and A1'],
 ['2025-11-12','Moody\'s','downgrade one notch','A2','stable (from negative)','secondary: Reuters via MarketScreener Nov 13, 2025, opened; Q2 FY26 10-Q p. 40 shows A2'],
 ['2026-10-05','S&P','downgrade one notch','A','negative','secondary: Reuters via capital.com and Tradingpedia, Oct 5, 2026, opened; Q1 FY27 10-Q p. 34 (filed Oct 2) still shows A+'],
])
W('buyback_and_shares.csv',['date_or_period','item','value','source'],[
 ['2022-06','$18B four-year program approved','18,000','Q1 FY27 10-Q p. 39'],
 ['2023-05-31','remaining under program','13,200','FY23 10-K p. 25'],
 ['2024-05-31','remaining under program','8,945','FY24 10-K p. 27'],
 ['2025-05-31','remaining under program','5,990','FY25 10-K p. 26'],
 ['FY2026','repurchased under program','1.8m shares, $122.4m, avg $67.63','FY26 10-K p. 45'],
 ['Q1 FY2026','repurchases paused','','FY26 10-K p. 45'],
 ['2026-06','program reapproved with no fixed expiration, no increase','','Q1 FY27 10-Q p. 33'],
 ['2026-08-31','cumulative under program','124.4m shares, about $12.1B, avg $97.57','Q1 FY27 10-Q p. 33'],
 ['2026-08-31','remaining (my arithmetic: 18.0 - 12.1)','about 5.9B','FY26 10-K p. 26 (5.9)'],
 ['Q1 FY2027','shares repurchased','0','Q1 FY27 10-Q p. 39'],
 ['FY2019','shares repurchased (m)','54.3','FY19 10-K p. 38'],['FY2020','shares repurchased (m)','33.5','FY20 10-K p. 44'],['FY2021','shares repurchased (m)','4.9','FY21 10-K p. 45'],['FY2022','shares repurchased (m)','27.3','FY22 10-K p. 45'],['FY2023','shares repurchased (m)','50.0','FY23 10-K p. 45'],['FY2024','shares repurchased (m)','41.4','FY24 10-K p. 47'],['FY2025','shares repurchased (m)','37.6','FY25 10-K p. 46'],['FY2026','shares repurchased (m)','1.8','FY26 10-K p. 45'],
 ['2019-07-19','shares outstanding','1,566,888,373','FY19 10-K cover'],['2021-07-09','shares outstanding','1,581,801,224','FY21 10-K cover'],['2023-07-12','shares outstanding','1,529,971,608','FY23 10-K cover'],['2024-07-10','shares outstanding','1,499,358,944','FY24 10-K cover'],['2025-03-28','shares outstanding (low point)','1,475,990,487','Q3 FY25 10-Q cover'],['2025-07-09','shares outstanding','1,476,903,492','FY25 10-K cover'],['2026-07-08','shares outstanding','1,483,498,703','FY26 10-K cover'],['2026-09-28','shares outstanding','1,485,308,829','Q1 FY27 10-Q cover'],
])
