import pickle,statistics as st,numpy as np
M=pickle.load(open('../M.pkl','rb'))
from reg import cd_core,brand,leaders
def obs(keys,h=5):
    out=[]
    for k in keys:
        d=M.get(k,{})
        for t in d:
            if t+h not in d: continue
            hist=[d[s] for s in d if t-9<=s<=t]
            if len(hist)<5: continue
            out.append((k,t,d[t],np.mean(hist),max(d[s] for s in d if t-5<=s<=t),d[t+h]))
    return out
for lab,ks in (('cd_core',cd_core),('brand',brand),('leaders',leaders)):
    O=obs([k for k in ks if k in M])
    for cov in ('all windows','ex 2020-spanning'):
        S=[o for o in O if 5.5<=o[2]<=11.5 and o[3]-o[2]>=2.0 and (cov=='all windows' or not(o[1]<=2020<=o[1]+5))]
        if not S: continue
        ch=np.array([o[5]-o[2] for o in S]); m5=np.array([o[5] for o in S])
        print(f"{lab} {cov}: n={len(S)} firms={len({o[0] for o in S})} | m0 5.5-11.5 and >=2pt below own 10y mean | m5 mean {m5.mean():.1f} median {np.median(m5):.1f} | chg median {np.median(ch):.1f} p10 {np.percentile(ch,10):.1f} p90 {np.percentile(ch,90):.1f} | P(chg>=3.3) {np.mean(ch>=3.3):.0%} P(>=5.7) {np.mean(ch>=5.7):.0%} P(chg<0) {np.mean(ch<0):.0%} | MAD-sd {1.4826*np.median(abs(ch-np.median(ch))):.1f}")
