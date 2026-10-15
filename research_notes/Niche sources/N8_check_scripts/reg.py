import pickle,statistics as st,math
import numpy as np
M=pickle.load(open('../M.pkl','rb'))
from epis import brand,leaders
cd_core=['LULU','RL','TPR','UAA','VFC','PVH','COLM','DECK','CROX','WWW','HBI','LEVI','SKX','CPRI','FOSL','CRI','GIII','OXM','PLCE','CHS','SHOO','ANF','AEO','URBN','GPS','LB','FL','KSS','M','BBY','HAS','MAT','HOG','PII','WHR','NWL','LEA','TIF','SBUX','MCD','YUM','DRI','DPZ','CMG','MAR','HLT','NCLH','LZB','TPX','HELE','BC','YETI','SONO','GPRO','PTON','COTY','EL']
def build(keys,h=5,minhist=5):
    X=[];Y=[];G=[]
    for k in keys:
        d=M.get(k,{})
        for t in d:
            if t+h not in d: continue
            hist=[d[s] for s in range(t-minhist+1,t+1) if s in d]
            if len(hist)<minhist: continue
            allh=[d[s] for s in d if s<=t]
            X.append((d[t],st.mean(allh)));Y.append(d[t+h]);G.append(k)
    return np.array(X),np.array(Y),G
def wins(v,lo=2,hi=98):
    a,b=np.percentile(v,[lo,hi]); return np.clip(v,a,b)
for lab,ks in (('brand',brand),('cd_core',cd_core),('leaders',leaders)):
    X,Y,G=build([k for k in ks if k in M])
    Xw=np.column_stack([wins(X[:,0]),wins(X[:,1])]); Yw=wins(Y)
    A=np.column_stack([np.ones(len(Yw)),Xw]); coef,res,_,_=np.linalg.lstsq(A,Yw,rcond=None)
    pred=A@coef; resid=Yw-pred
    print(lab,'n',len(Yw),'firms',len(set(G)),'| m5 = %.2f + %.2f*m0 + %.2f*ownmean(to t)'%tuple(coef),'| resid sd %.2f'%resid.std(ddof=3))
    # Nike prediction
    for m0,mu in ((8.3,12.38),(6.2,12.38),(8.3,11.83)):
        print('   Nike m0=%.1f own mean=%.2f -> E[m5]=%.2f'%(m0,mu,coef@np.array([1,m0,mu])), ' 80%% interval %.1f to %.1f'%tuple(coef@np.array([1,m0,mu])+np.percentile(resid,[10,90])))
    # pooled m0 only
    A1=np.column_stack([np.ones(len(Yw)),Xw[:,0]]); c1=np.linalg.lstsq(A1,Yw,rcond=None)[0]; r1=Yw-A1@c1
    print('   m0-only: m5=%.2f+%.2f*m0 resid sd %.2f; at 8.3 -> %.2f'%(c1[0],c1[1],r1.std(ddof=2),c1[0]+c1[1]*8.3))
