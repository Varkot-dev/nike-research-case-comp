import pickle,statistics as st,math,csv,sys
M=pickle.load(open('../M.pkl','rb'))
brand=['LULU','RL','TPR','UAA','VFC','PVH','COLM','DECK','CROX','WWW','HBI','LEVI','SKX','CPRI','FOSL','CRI','GIII','OXM','SHOO','TIF','SBUX','EL','HAS','MAT','COTY','YETI','HOG']
leaders=['LULU','RL','TPR','UAA','VFC','PVH','COLM','DECK','LEVI','SKX','CPRI','TIF','SBUX','EL','HAS','MAT']
def episodes(keys,drop=3.0,pers=2,minm=0.0,h=5):
    out=[]
    for k in keys:
        d=M.get(k,{}); ys=sorted(d)
        last_entry=-99
        for t in ys:
            win=[d[s] for s in range(t-5,t) if s in d]
            if len(win)<3: continue
            pk=max(win)
            ok=all((s in d) and d[s]<=pk-drop and d[s]>minm for s in range(t-pers+1,t+1))
            if not ok: continue
            if t-last_entry<=h: continue   # one episode per spell
            last_entry=t
            fut=d.get(t+h)
            out.append(dict(k=k,t=t,m0=d[t],peak=pk,gap=pk-d[t],m5=fut,chg=None if fut is None else fut-d[t],closed=None if fut is None else (fut-d[t])/(pk-d[t])))
    return out
def summ(eps,label,thr=3.3):
    c=[e for e in eps if e['m5'] is not None]
    if not c: print(label,'none'); return
    chg=sorted(e['chg'] for e in c)
    n=len(c); k33=sum(e['chg']>=thr for e in c); k57=sum(e['chg']>=5.7 for e in c); kneg=sum(e['chg']<0 for e in c)
    print(f"{label}: n={n} (+{len(eps)-n} open) median chg {st.median(chg):.1f} mean {st.mean(chg):.1f} | >=+3.3: {k33}/{n} | >=+5.7: {k57}/{n} | chg<0: {kneg}/{n} | median gap closed {st.median([e['closed'] for e in c]):.2f}")
if __name__=='__main__':
    for drop,pers in ((3,2),(4,1),(4,2),(5,2)):
        for lab,ks in (('brand',brand),('leaders',leaders),('all',list(M))):
            summ(episodes(ks,drop,pers),f'drop>={drop} pers{pers} {lab}')
    print()
    for e in episodes(brand,3,2): print(e['k'],e['t'],round(e['m0'],1),'peak',round(e['peak'],1),'m5',None if e['m5'] is None else round(e['m5'],1),'chg',None if e['chg'] is None else round(e['chg'],1))
