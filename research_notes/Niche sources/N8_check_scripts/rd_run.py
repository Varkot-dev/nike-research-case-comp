import rd,sys
def px(m,**kw): return (rd.value(m,**kw)+8368-7893)/1487
base=dict(wacc=0.10,g=0.02,cagr=0.03)
print('check price at 14.11%,10/2/3%:',round(px(0.1411,**base),2))
print('\nA. price vs FY31 margin x WACC (g=2%, cagr 3%, tax 22.5%)')
ms=[0.062,0.073,0.083,0.088,0.094,0.10,0.116,0.12,0.14]
print('m%  ',' '.join(f'W{int(w*100):>2}' .rjust(7) for w in (0.08,0.09,0.10,0.11)))
for m in ms: print(f'{m*100:5.1f}',' '.join(f'{px(m,wacc=w,g=0.02,cagr=0.03):7.2f}' for w in (0.08,0.09,0.10,0.11)))
print('\nB. price at 9.4% : g x cagr (WACC 9/10)')
for w in (0.09,0.10):
  for g in (0.01,0.02,0.03):
    print('W',w,'g',g,[round(px(0.094,wacc=w,g=g,cagr=c),2) for c in (0.0,0.01,0.03,0.05)])
print('\nC. tax at 9.4%, wacc 10 g2 cagr3 :',[ (t,round(px(0.094,tax=t,**base),2)) for t in (0.18,0.20,0.225,0.25,0.28)])
print('   NB tax also changes FY27/28 EBIT derived from EPS')
print('\nD. ramp: margin reached 2031 vs 2029/2033 at 9.4%',[(r,round(px(0.094,ramp_end=r,**base),2)) for r in (2029,2031,2033)])
print('\nE. terminal margin: 9.4 to FY31 then continues regress (10y: 10.2; sector 11; own mean 12.4) -- model ends horizon 2036 so set margin m held 2031-2036 and TV on it')
for m in (0.094,0.102,0.11,0.124): print(m, [round(px(m,wacc=w,g=0.02,cagr=0.03),2) for w in (0.09,0.10)])
print('\nF. market-implied margin at price 35.30 (EV 52031), by wacc/g/cagr')
for w in (0.08,0.09,0.10,0.11):
  print(w,[ (g,c,round(rd.solve_m(wacc=w,g=g,cagr=c)*100,1)) for g in (0.02,0.03) for c in (0.01,0.03,0.05)])
print('\nG. exit price at E[m]=9.4% vs 35.30 percentages')
for w in (0.09,0.10):
    p=px(0.094,wacc=w,**{k:v for k,v in base.items() if k!='wacc'}); print(w,round(p,2),round((p/35.30-1)*100,1))
print('\nH. 7.9 (6.2 start, own mean) and 9.4 lumps: 6.2->',round(12.38+.73*(6.2-12.38),2))
