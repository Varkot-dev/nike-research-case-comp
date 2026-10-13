import csv,sys
OUT=sys.argv[1]
START_CASH=9027  # cash 7,563 + STI 1,464 at May 31, 2026 (FY26 10-K p. 57)
FLOOR=4663       # cash 4,466 + STI 197 at May 31, 2019 (FY19 10-K p. 52): period low-water mark
LEASES=3179      # operating lease liabilities 473 + 2,706 at Aug 31, 2026 (Q1 FY27 10-Q p. 3)
TAX=0.25
years=['FY2027','FY2028','FY2029','FY2030x','FY2031x']
maturities={'FY2027':2000,'FY2028':0,'FY2029':0,'FY2030x':1500,'FY2031x':0}  # FY26 10-K p. 70
sc={
 'base':dict(eps=[1.25,1.65,2.30,2.30,2.30],shares=[1485,1492,1500,1507,1515],da=760,sbc=650,oth=-100,
             wc=[-300,-200,-300,-200,-200],capex=[750,750,800,800,800],pace=[300,250,150,150,150],
             dps=[1.66,1.70,1.74,1.78,1.82],refi=False,refi_rate=None),
 'stress':dict(eps=[1.00,1.00,1.00,1.00,1.00],shares=[1485,1492,1500,1507,1515],da=760,sbc=650,oth=-100,
             wc=[-300,0,0,0,0],capex=[800,800,800,800,800],pace=[350,350,300,0,0],
             dps=[1.64]*5,refi=True,refi_rate=0.055),
 'stress_repay_from_cash':dict(eps=[1.00]*5,shares=[1485,1492,1500,1507,1515],da=760,sbc=650,oth=-100,
             wc=[-300,0,0,0,0],capex=[800]*5,pace=[350,350,300,0,0],dps=[1.64]*5,refi=False,refi_rate=None),
}
rows=[]
for name,a in sc.items():
    cash=START_CASH; debt=8000; refi_bal=0
    for i,y in enumerate(years):
        ni=a['eps'][i]*a['shares'][i]
        pace_at=a['pace'][i]*(1-TAX)
        refi_cost=0
        if a['refi']:
            # refinance maturities with new notes; incremental coupon vs old (2.38%/2.75%) ~2.56% avg on the FY27 $2.0B
            if y=='FY2027': refi_cost=2000*(a['refi_rate']-0.0256)*(1-TAX)*0.5   # half-year effect
            elif y=='FY2030x': refi_cost=2000*(a['refi_rate']-0.0256)*(1-TAX)+1500*(a['refi_rate']-0.0285)*(1-TAX)*0.2
            else: refi_cost=2000*(a['refi_rate']-0.0256)*(1-TAX)
            if y=='FY2031x': refi_cost=2000*(a['refi_rate']-0.0256)*(1-TAX)+1500*(a['refi_rate']-0.0285)*(1-TAX)
        cfo=ni+a['da']+a['sbc']+a['oth']+a['wc'][i]-pace_at-refi_cost
        fcf=cfo-a['capex'][i]
        div=a['dps'][i]*a['shares'][i]
        mat=maturities[y]
        repay=0 if a['refi'] else mat
        debt-=repay
        cash=cash+fcf-div-repay
        ebitda=ni/(1-TAX)+a['da']
        rows.append(dict(scenario=name,year=y,adj_eps=a['eps'][i],shares_m=a['shares'][i],adj_net_income=round(ni),
          d_and_a=a['da'],sbc=a['sbc'],other_noncash=a['oth'],working_capital=a['wc'][i],pace_cash_after_tax=round(-pace_at),
          incr_refi_interest_after_tax=round(-refi_cost),cfo=round(cfo),capex=a['capex'][i],fcf=round(fcf),dps=a['dps'][i],
          dividends=round(div),fcf_div_coverage=round(fcf/div,2),fcf_minus_div=round(fcf-div),debt_repaid_from_cash=repay,
          debt_face_end=debt,cash_sti_end=round(cash),net_cash_end=round(cash-debt),cash_minus_floor=round(cash-FLOOR),
          ebitda_approx=round(ebitda),debt_to_ebitda=round(debt/ebitda,2),lease_adj_debt_to_ebitda=round((debt+LEASES)/ebitda,2),
          fcf_to_lease_adj_debt_pct=round(100*fcf/(debt+LEASES),1),
          dividend_payout_of_adj_eps_pct=round(100*a['dps'][i]/a['eps'][i]),
          label='my arithmetic; FY2030x and FY2031x are extrapolations holding FY2029 assumptions'))
w=csv.DictWriter(open(OUT,'w',newline=''),fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
for r in rows: print(r['scenario'],r['year'],'CFO',r['cfo'],'FCF',r['fcf'],'div',r['dividends'],'cov',r['fcf_div_coverage'],'gap',r['fcf_minus_div'],'cash',r['cash_sti_end'],'debt',r['debt_face_end'],'net',r['net_cash_end'],'D/E',r['debt_to_ebitda'],'FOCF/adjdebt',r['fcf_to_lease_adj_debt_pct'],'payout',r['dividend_payout_of_adj_eps_pct'])
# severe: S&P burn ~1.2B/yr after dividends (secondary), debt repaid from cash
cash=START_CASH; debt=8000; sev=[]
for y in years:
    cash=cash-1200-maturities[y]; debt-=maturities[y]
    sev.append((y,cash,debt,cash-debt,cash-FLOOR))
print('severe S&P-implied',sev)
with open(OUT.replace('.csv','_severe_sp_burn.csv'),'w',newline='') as f:
    ww=csv.writer(f); ww.writerow(['year','cash_sti_end','debt_face_end','net_cash_end','cash_minus_floor','label'])
    for r in sev: ww.writerow(list(r)+['my arithmetic on S&P burn of about $1.2B a year after dividends (secondary: Reuters via capital.com, Oct 5, 2026)'])
