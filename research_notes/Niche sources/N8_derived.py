"""N8 derived numbers. Inputs are typed from opened sources (cited in N8_literature_base_rates.md) and repo files.
Run: python3 -I N8_derived.py   (prints the tables used in the note; writes N8_derived_numbers.csv)"""
import math, csv, os
out=[]
def rec(k,v,src): out.append((k,v,src)); print(f"{k}: {v}   [{src}]")
# ---- Nike inputs (data/nike_filing_facts.csv via research_notes/04_financial_data_pack.md)
rev={'FY23':51217,'FY24':51362,'FY25':46309,'FY26':46398}; ebit={'FY23':6195,'FY24':6539,'FY25':3778,'FY26':3850}
# ---- Base Rate Book Exhibit 4, sales >$25,000 Mn, REAL CAGR, % of observations (printed p. 25)
lo=[-99,-25,-20,-15,-10,-5,0,5,10,15,20,25,30,35,40,45]
H3=[1.6,0.8,2.0,3.8,9.0,19.8,26.9,18.2,9.1,4.3,2.2,1.1,0.4,0.4,0.2,0.3]
H5=[1.0,0.6,1.5,3.0,8.2,21.3,32.6,18.1,8.5,3.2,1.2,0.4,0.2,0.1,0.1,0.0]
ge=lambda h,t: sum(p for p,l in zip(h,lo) if l>=t)
for n,h in (('3y',H3),('5y',H5)):
    rec(f'BRB >$25B real {n} P(CAGR<0)',round(100-ge(h,0),1),'BRB Exh.4 p.25')
    rec(f'BRB >$25B real {n} P(CAGR>=5)',round(ge(h,5),1),'BRB Exh.4 p.25')
    rec(f'BRB >$25B real {n} P(CAGR>=10)',round(ge(h,10),1),'BRB Exh.4 p.25')
# Nike growth history
cagr=lambda a,b,n:(b/a)**(1/n)-1
rec('Nike revenue FY23->FY26 3y nominal CAGR %',round(cagr(rev['FY23'],rev['FY26'],3)*100,2),'DERIVED')
rec('Nike revenue FY21->FY26 5y nominal CAGR %',round(cagr(44538,46398,5)*100,2),'DERIVED')
rec('Nike FY28 consensus revenue vs FY26: 2y CAGR %',round(cagr(46398,43600,2)*100,2),'D5 FY28 rev 43.6B')
# ---- Operating leverage (BRB Exh.11/12 consumer discretionary 3y: dOpInc = 0.074*dSales + 17.436 ($M))
b,a=0.074,17.436
for s,e in (('FY23','FY26'),('FY24','FY26')):
    dS=rev[e]-rev[s]; dE=ebit[e]-ebit[s]; pred=b*dS+a
    rec(f'Op leverage {s}->{e}: dSales',dS,'filings'); rec(f'  actual dEBIT',dE,'filings'); rec(f'  BRB-predicted dEBIT',round(pred),'BRB Exh.12')
    rec(f'  share of EBIT fall NOT explained by sector volume leverage %',round((1-pred/dE)*100,1),'DERIVED')
need_ebit=0.116*43600; cons_ebit=0.072*43600
rec('FY28 EBIT at consensus 7.2% ($M)',round(cons_ebit),'D5'); rec('FY28 EBIT at 11.6% ($M)',round(need_ebit),'D5')
# Nike's own observed incremental margin on the way down (EBIT lost per $ of sales lost)
gp={'FY23':22292,'FY24':22887,'FY25':19790,'FY26':19911}; opx={'FY23':4060+12317,'FY24':4285+12291,'FY26':4754+11360}
for s,e in (('FY23','FY26'),('FY24','FY26')):
    rec(f'Nike EBIT lost per $ of sales lost {s}->{e}',round((ebit[s]-ebit[e])/(rev[s]-rev[e]),3),'DERIVED from filings; sector BRB beta 0.074')
dS=rev['FY24']-rev['FY26']; gm24=gp['FY24']/rev['FY24']
rec('FY24->FY26 gross profit change ($M)',gp['FY26']-gp['FY24'],'filings')
rec('  of which volume at FY24 gross margin ($M)',round(-dS*gm24),'DERIVED'); rec('  of which rate (GM change x FY26 sales) ($M)',round((gp['FY26']/rev['FY26']-gm24)*rev['FY26']),'DERIVED')
rec('  opex (demand creation + overhead) change FY24->FY26 ($M)',opx['FY26']-opx['FY24'],'filings'); rec('  opex flex per $ of sales lost',round(-(opx['FY26']-opx['FY24'])/dS,3),'DERIVED vs sector 1-0.074=0.926')
# Symmetric-recovery arithmetic on the consensus revenue path
rev31=43600*1.03**3; dS31=rev31-43600
rec('FY31 revenue at +3%/yr from FY28 consensus ($M)',round(rev31),'DERIVED')
gm26=gp['FY26']/rev['FY26']
vol_gp=dS31*gm26
rec('Volume-only EBIT gain if opex flat in $ (flow-through at FY26 GM 42.9%) ($M)',round(vol_gp),'DERIVED, assumption: FY28 GM = FY26 GM')
for tgt in (0.116,0.14):
    need=tgt*rev31-cons_ebit; rate=need-vol_gp
    rec(f'To reach {tgt*100:.1f}% of FY31 revenue: EBIT gain needed ($M) / left for rate ($M) / = gross margin points',(round(need),round(rate),round(rate/rev31*100,1)),'DERIVED')
rec('Opex growth room: if opex grows 1%/yr FY28-31 on $16.1B-ish base, cost ($M)',round(16114*(1.01**3-1)),'DERIVED illustration')
# ---- Margin persistence (BRB Exh.1 p.59, Exh.4-5 p.62: consumer discretionary 5y r=0.73, median 10%, avg 11%)
nike_m={2008:13.4,2009:10.2,2010:13.3,2011:13.7,2012:12.4,2013:12.9,2014:12.9,2015:13.8,2016:14.3,2017:14.4,2018:12.0,2019:12.4,2020:8.0,2021:15.5,2022:14.7,2023:12.1,2024:12.7,2025:8.2,2026:8.3}
mu_own=sum(nike_m.values())/len(nike_m); mu10=sum(nike_m[y] for y in range(2017,2027))/10
rec('Nike mean EBIT margin FY08-FY26 %',round(mu_own,2),'D5_valuation_annual_xbrl.csv'); rec('Nike 10y mean FY17-FY26 %',round(mu10,2),'same')
r5=0.73; m0=8.3
for lab,mu in (('Nike own mean',mu_own),('Nike 10y mean',mu10),('sector avg 11%',11.0),('sector median 10%',10.0)):
    rec(f'E[FY31 margin | FY26=8.3, r5=0.73, mean={lab}] %',round(mu+r5*(m0-mu),2),'DERIVED from BRB p.59,62')
r4=0.76
rec('E[FY31 margin | FY27 consensus 5.7%, r4~0.76, Nike own mean] %',round(mu_own+r4*(5.7-mu_own),2),'DERIVED (r4 interpolated between BRB 3y 0.79 and 5y 0.73/0.72)')
E_m=mu_own+r5*(m0-mu_own)
def Pge(x,mean,sd): return 0.5*math.erfc((x-mean)/(sd*math.sqrt(2)))
print('Normal grid around E[m]=%.2f'%E_m)
for sd in (2.2,3.5,5.0,8.2):
    row={x:round(100*Pge(x,E_m,sd),1) for x in (11.0,11.6,12.0,14.0)}
    rec(f'P(FY31 margin >= x | sd={sd})',row,'DERIVED (sd 2.2 = Nike own FY08-26; 8.2 = pooled 10-firm 5y residual)')
# ---- analog episodes from D5 XBRL 10-firm set (computed in the note's section 6; counts typed here)
n_ep=13; k33=3; k57=2
def wilson(k,n,z=1.96):
    p=k/n; d=1+z*z/n; c=p+z*z/(2*n); w=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n)); return round(100*(c-w)/d,0),round(100*(c+w)/d,0)
rec('Analog episodes: >=+3.3pp (to 11.6%) in 5y',f'{k33}/{n_ep} = {100*k33/n_ep:.0f}%  Wilson95 {wilson(k33,n_ep)}','D5 XBRL 10 firms, DERIVED')
rec('Analog episodes: >=+5.7pp (to 14%) in 5y',f'{k57}/{n_ep} = {100*k57/n_ep:.0f}%  Wilson95 {wilson(k57,n_ep)}','same')
# ---- value mapping from consensus_and_valuation.md reverse DCF cross-check (10% WACC: 8%->$20.8, 10%->$25.4, 15%->$36.7 midpoints)
price=lambda m: 20.8+2.27*(m-8)
rec('Reverse-DCF price at E[m]=9.4% (10% WACC) $',round(price(E_m),1),'consensus_and_valuation.md l.239 midpoints, linear')
rec('  vs $35.30 %',round((price(E_m)/35.30-1)*100,0),'DERIVED')
rec('Reverse-DCF price at E[m]=9.4% (9% WACC; $23 at 8%, $30 at 10%) $',round(23+3.5*(E_m-8),1),'consensus_and_valuation.md l.247')
# ---- CMR announcement return CI
se=4.8/2.31; rec('CMR 3-day CAR -4.8%: SE / 95% CI (pp)',f'{se:.2f} / {-4.8-1.96*se:.1f} to {-4.8+1.96*se:.1f}','CMR preprint Table 3 p.48 (t=-2.31, N=73)')
# ---- Nike first-below-midpoint reaction (data/nke_daily_prices.csv, ^GSPC Yahoo chart API)
rec('NKE Oct 2 2026 close-to-close %',round((33.87/35.15-1)*100,2),'nke_daily_prices.csv'); rec('S&P 500 same day %',round((7722.72/7666.45-1)*100,2),'Yahoo ^GSPC')
rec('NKE abnormal vs S&P (simple difference) pp',round((33.87/35.15-1)*100-(7722.72/7666.45-1)*100,2),'DERIVED')
# ---- HLT dispersion/error effect in dollars
rec('HLT Stop coefficient on ChgError x $35.30 ($ per share EPS forecast error)',round(0.0003*35.30,4),'HLT Table 9 p.49 (deflated by price)')
rec('HLT FutureEPS gap stoppers - maintainers (mean, price-deflated) x $35.30 ($)',round((-0.001-0.006)*35.30,3),'HLT Table 3 p.41 (t=-1.11, NOT significant; Wilcoxon z=-3.13)')
# ---- convexity (Reibstein and Farris 1994 WP p.10: exponent a in share ~ distribution^a ranged 1.80 to 4.68 across 12 categories)
for dl in (0.05,0.10,0.20):
    rec(f'Share ratio after {int(dl*100)}% fall in weighted distribution, a=1.80 / 4.68 %',(round((1-dl)**1.8*100-100,1),round((1-dl)**4.68*100-100,1)),'DERIVED, cross-sectional CPG exponent, illustrative only')
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'N8_derived_numbers.csv'),'w',newline='') as f:
    w=csv.writer(f); w.writerow(['item','value','source']); w.writerows(out)
