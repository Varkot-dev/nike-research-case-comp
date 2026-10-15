"""D6 dividend and cash coverage model. Every input is either a filing figure (cited in D6_dividend_cash.md)
or a labelled assumption below. Run: python3 -I D6_dividend_cash_model.py   (prints all tables used in the note)."""
# ---------- FILING INPUTS (USD millions unless noted) ----------
H = {  # fiscal year: dict. Sources: FY24/FY25/FY26 10-K cash flow statements, income statements, balance sheets
 'FY2019': dict(dps=0.86, eps=2.49, cfo=5903, capex=1119, div=1332, bb=4286, cashsti=None, debt=None),
 'FY2020': dict(dps=0.955, eps=1.60, cfo=2485, capex=1086, div=1452, bb=3067),
 'FY2021': dict(dps=1.07, eps=3.56, cfo=6657, capex=695, div=1638, bb=608),
 'FY2022': dict(dps=1.19, eps=3.75, cfo=5188, capex=758, div=1837, bb=4014),
 'FY2023': dict(dps=1.325, eps=3.23, cfo=5841, capex=969, div=2012, bb=5480, opt=651, cashsti=7441+3234, debt=8927+6),
 'FY2024': dict(dps=1.45, eps=3.73, cfo=7429, capex=812, div=2169, bb=4250, opt=667, cashsti=9860+1722, debt=1000+7903+6),
 'FY2025': dict(dps=1.57, eps=2.16, cfo=3698, capex=430, div=2300, bb=2985, opt=551, cashsti=7464+1687, debt=7961+5),
 'FY2026': dict(dps=1.63, eps=2.10, cfo=2868, capex=684, div=2407, bb=146, opt=354, cashsti=7563+1464, debt=2000+5942),
}
print('== A. History: payout and FCF coverage ==')
for y,d in H.items():
    fcf=d['cfo']-d['capex']; d['fcf']=fcf
    s=f"{y}: DPS {d['dps']:.3f} EPS {d['eps']:.2f} payout(EPS) {d['dps']/d['eps']*100:.0f}% | CFO {d['cfo']} capex {d['capex']} FCF {fcf} div {d['div']} FCF/div {fcf/d['div']:.2f}x div%FCF {d['div']/fcf*100:.0f}% | bb {d['bb']} returns/FCF {(d['div']+d['bb'])/fcf:.2f}x"
    if d.get('cashsti'): s+=f" | cash+STI {d['cashsti']} debt {d['debt']} net cash {d['cashsti']-d['debt']}"
    if d.get('opt'): s+=f" | FCF+option proceeds/div {(fcf+d['opt'])/d['div']:.2f}x"
    print(s)
tot=lambda ys,k:sum(H[y][k] for y in ys)
ys=['FY2023','FY2024','FY2025','FY2026']
print('FY23-26 cumulative: FCF',tot(ys,'fcf'),'div',tot(ys,'div'),'bb',tot(ys,'bb'),'returns',tot(ys,'div')+tot(ys,'bb'),'gap',tot(ys,'div')+tot(ys,'bb')-tot(ys,'fcf'),'option proceeds',tot(ys,'opt'))
print('cash+STI May23 %d -> May26 %d (chg %d); net cash May23 %d -> May26 %d'%(H['FY2023']['cashsti'],H['FY2026']['cashsti'],H['FY2026']['cashsti']-H['FY2023']['cashsti'],H['FY2023']['cashsti']-H['FY2023']['debt'],H['FY2026']['cashsti']-H['FY2026']['debt']))

print('\n== B. Why FY24->FY26 CFO fell (4,561) ==')
ni24,ni26=5700,3108; nc24=796-497+804+48-138; nc26=747-96+715+50+22; wc24=-329+908-260+397; wc26=-1207-31+519-959
print('NI',ni26-ni24,'noncash',nc26-nc24,'WC',wc26-wc24,'sum',ni26-ni24+nc26-nc24+wc26-wc24,'(nc24',nc24,'nc26',nc26,'wc24',wc24,'wc26',wc26,')')
print('WC share of CFO decline %.0f%%'%((wc26-wc24)/(2868-7429)*100))
rev24,rev26,gp24,gp26=51362,46398,22887,19911
print('GP bridge FY24->FY26: volume(revenue) %.0f, GM rate %.0f, total %d; S&A saving %d; interest %d; other %d'%((rev26-rev24)*gp24/rev24,(gp26/rev26-gp24/rev24)*rev26,gp26-gp24,16576-16114,-50+161 and (-(-50)+(-161))*-1 if False else (161-50)*-1,(53-228)))
print('Pretax FY24 6700 -> FY26 3900 (-2800); ex-IEEPA 986 -> 2914 (-3786)')

print('\n== C. FY27E build (guide) ==')
SH=1485.0; DIV=613*4   # Q1 FY27 dividends declared 613 x4
print('Dividend run-rate declared 613x4 =',DIV,' ; $1.64 x 1,483 shares =',round(1.64*1483))
NONCASH=193*4+158*4  # D&A + SBC at Q1 run-rate (assumption)
CAPEX=199*4          # Q1 run-rate (assumption)
IEEPA=684-0.23*986   # receivable collected less tax at 23% (assumption)
PACE=300             # after-tax cash drag vs adjusted NI (assumption, range 190-420)
print('assumptions: noncash',NONCASH,'capex',CAPEX,'IEEPA net',round(IEEPA),'Pace',PACE)
print('Adj EPS | adj NI | FCF @ otherWC -1000 / -500 / 0 / +500 | coverage')
for eps in (1.15,1.25,1.35):
    ni=eps*SH
    row=[]
    for wc in (-1000,-500,0,500):
        fcf=ni+NONCASH+IEEPA-PACE+wc-CAPEX
        row.append(f"{fcf:.0f} ({fcf/DIV:.2f}x)")
    print(f"{eps:.2f} | {ni:.0f} | "+' | '.join(row))
print('Payout of adj EPS: ',[round(1.64/e*100) for e in (1.15,1.25,1.35)],' GAAP EPS (less 0.15 Pace):',[round(1.64/(e-0.15)*100) for e in (1.15,1.25,1.35)])
print('Q1 FY27 FCF -64 ; ex IEEPA net %.0f -> %.0f ; ex severance paid 243 too -> %.0f'%(IEEPA,-64-IEEPA,-64-IEEPA+243))
print('Q1 other WC (ex IEEPA net, ex severance) = %.0f vs Q1 FY26 total WC -897'%(-846-IEEPA+243))

print('\n== D. FY28E grid (adjusted EPS, ex Pace; Pace cash after tax 230) ==')
SH28=1490.0
print('EPS | NI | payout | FCF(WC0) cov | FCF(WC-500) cov | FCF(WC+500) cov')
for eps in (1.00,1.15,1.25,1.40,1.50,1.65):
    ni=eps*SH28; base=ni+NONCASH-230-CAPEX
    print(f"{eps:.2f} | {ni:.0f} | {1.64/eps*100:.0f}% | {base:.0f} {base/DIV:.2f}x | {base-500:.0f} {(base-500)/DIV:.2f}x | {base+500:.0f} {(base+500)/DIV:.2f}x")
be=(DIV-NONCASH+230+CAPEX)/SH28
print('Break-even FY28 adj EPS for FCF=dividend (WC0): %.2f ; with SBC treated as cash cost (noncash=D&A only): %.2f ; with WC -500: %.2f'%(be,(DIV-772+230+CAPEX)/SH28,be+500/SH28))
print('EBIT sensitivity: each $0.10 of EPS = %.0f NI = %.0f pretax at 25%% tax'%(0.10*SH28,0.10*SH28/0.75))
print('Hold FY24 margin: FY24 EBIT margin 12.7%% x FY27E rev 42.7B = %.0f vs FY27E adj pretax ~2,475'%(0.127*42700))

print('\n== E. Balance sheet runway (Aug 31 2026) ==')
cash=6903+1465; debt=2000+5893+0
print('cash+STI',cash,'debt',debt,'net cash',cash-debt)
leases=473+2706
print('lease liabilities',leases,'; net debt incl leases',debt+leases-cash)
ebitda26=3850+747; ebitdar26=ebitda26+693
print('FY26 EBITDA',ebitda26,'EBITDAR',ebitdar26,'debt/EBITDA %.2f'%(7942/ebitda26),'(debt+leases 3091)/EBITDAR %.2f'%((7942+3091)/ebitdar26),'net (debt+leases-cash)/EBITDAR %.2f'%((7942+3091-9027)/ebitdar26))
coupon=1000*.0238+1000*.0275+1500*.0285+1000*.0325+500*.0363+1000*.0388+500*.0338+1500*.0338
print('Annual coupon run-rate',round(coupon,1),'; FY26 interest paid 323; FY26 EBIT/coupon %.1fx'%(3850/coupon),'; avg coupon %.2f%%'%(coupon/8000*100))
print('After both 2027 notes repaid: coupon',round(coupon-23.8-27.5,1))
print('Portfolio yield FY26: 278 / avg(9151,9027) = %.2f%%'%(278/((9151+9027)/2)*100))
print('Refi 2.0B at 5.49%% vs 2.56%% avg old coupon: +%.0f pretax = $%.3f EPS (at 25%% tax, 1485 sh)'%(2000*(0.0549-0.0256),2000*(0.0549-0.0256)*.75/1485))
print('\nQuarters of cover (cash+STI 8,368 less 2,000 notes due by Mar 27 2027 = 6,368)')
avail=cash-2000
for floor in (0,3000,4000):
    for lab,q in (('dividend only',DIV/4),('dividend + $1.5B/yr buyback',DIV/4+375),('dividend + $3.0B/yr buyback (FY25 pace)',DIV/4+750)):
        print(f" floor {floor}: {lab}: gross-cash quarters {(avail-floor)/q:.1f}")
print('Net of operating FCF: S&P burn 1.2B/yr after dividends -> years to exhaust 6,368: %.1f ; with min cash 4,000: %.1f'%(avail/1200,(avail-4000)/1200))
for eps in (1.00,1.25):
    gap=DIV-(eps*SH28+NONCASH-230-CAPEX)
    print(f"FY28 EPS {eps}: annual shortfall vs dividend {gap:.0f}; years of 6,368 cash {avail/gap:.1f}")

print('\n== F. What a cut/freeze is worth ==')
mcap=35.35*1483
for lab,newdps in (('token raise +$0.01/qtr',1.68),('freeze',1.64),('cut 25%',1.23),('cut 50%',0.82),('suspend',0.0)):
    sav=(1.64-newdps)*1483
    print(f"{lab}: dps {newdps} annual cash vs $1.64 {sav:+.0f} ($/sh {1.64-newdps:+.2f}); yield on 35.35 {newdps/35.35*100:.1f}%; = {sav/mcap*100:.2f}% of mkt cap")
for sv in (59,613,1230):
    pass
print('Buyback at 35.35 of 1,230: shares retired %.1fM = %.2f%% ; EPS accretion on FY28 1.25: +$%.3f'%(1230/35.35,1230/mcap*100,1.25*(1230/mcap)))
print('Interest: use 2,000 saved to avoid refi at 5.49%%: net of 3.06%% lost portfolio yield: %.0f pretax'%(2000*(0.0549-0.0306)))
print('Swoosh LLC: 221.75M Class A x 1.64 = %.0f (share count from 2026 proxy per REPO note 18, unverified here)'%(221.75*1.64))
