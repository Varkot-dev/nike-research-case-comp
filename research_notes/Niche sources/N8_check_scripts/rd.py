import itertools
EV=52031; SH=1487
R26=46398; R27=43152; R28=43645
def ebit_from_eps(eps,tax): return eps*SH/(1-tax)
def value(m,wacc,g,cagr,tax=0.225,roic=0.20,s2c=2.5,frac=0.63,tv_next=True,neg_reinv=False,ramp_end=2031,end=2036,m28=None):
    revs={2026:R26,2027:R27,2028:R28}
    ebit={2027:ebit_from_eps(1.288,tax),2028:ebit_from_eps(1.646,tax)}
    mm28=ebit[2028]/R28 if m28 is None else m28
    if m28 is not None: ebit[2028]=m28*R28
    for y in range(2029,end+1):
        revs[y]=revs[y-1]*(1+cagr)
        if y<ramp_end: mg=mm28+(m-mm28)*(y-2028)/(ramp_end-2028)
        else: mg=m
        ebit[y]=revs[y]*mg
    pv=0
    for y in range(2027,end+1):
        nopat=ebit[y]*(1-tax); d=revs[y]-revs[y-1]
        reinv=d/s2c if (d>0 or neg_reinv) else 0
        fcf=nopat-reinv
        if y==2027: fcf*=frac; t=frac/2
        else: t=frac+(y-2028)+0.5
        pv+=fcf/(1+wacc)**t
    nop=ebit[end]*(1-tax)*((1+g) if tv_next else 1)
    tv=nop*(1-g/roic)/(wacc-g)
    t_end=frac+(end-2027)  # end of FY end
    pv+=tv/(1+wacc)**t_end
    return pv
def solve_m(target=EV,**kw):
    lo,hi=-0.5,1.0
    for _ in range(80):
        mid=(lo+hi)/2
        if value(mid,**kw)<target: lo=mid
        else: hi=mid
    return mid
if __name__=='__main__':
    for tv_next in (True,False):
        print(tv_next,[round(solve_m(wacc=w,g=g,cagr=0.03,tv_next=tv_next)*100,2) for w,g in [(0.10,0.02),(0.10,0.03),(0.09,0.02),(0.09,0.03),(0.08,0.02),(0.08,0.03)]])
    print('csv: 14.11 13.43 12.15 11.38 10.25 9.38')
