import csv,collections,statistics as st,math
rows=list(csv.DictReader(open('../panel.csv')))
P=collections.defaultdict(dict)
for r in rows:
    y=0;m=0
    import datetime as _d; y=(_d.date.fromisoformat(r['fye'])-_d.timedelta(days=75)).year
    k=r['ticker']
    # if duplicate label keep later end date
    if y in P[k] and P[k][y][0]>r['fye']: continue
    P[k][y]=(r['fye'],float(r['margin']))
M={k:{y:v[1] for y,v in d.items()} for k,d in P.items()}
# gaps check
for k,d in M.items():
    ys=sorted(d)
    if ys[-1]-ys[0]+1!=len(ys): print('gap',k,ys)
import pickle; pickle.dump(M,open('../M.pkl','wb'))
def corr(x,y):
    mx,my=st.mean(x),st.mean(y); sx=math.sqrt(sum((a-mx)**2 for a in x)); sy=math.sqrt(sum((b-my)**2 for b in y))
    return sum((a-mx)*(b-my) for a,b in zip(x,y))/(sx*sy)
def slope(x,y):
    mx,my=st.mean(x),st.mean(y); return sum((a-mx)*(b-my) for a,b in zip(x,y))/sum((a-mx)**2 for a in x)
def pairs(keys,h=5):
    x=[];y=[]
    for k in keys:
        d=M[k]
        for t in d:
            if t+h in d: x.append(d[t]); y.append(d[t+h])
    return x,y
def wins(v,lo=2,hi=98):
    s=sorted(v); a=s[int(len(s)*lo/100)]; b=s[min(len(s)-1,int(len(s)*hi/100))]; return [min(max(z,a),b) for z in v]
groups={
'all73':list(M),
'cd_core':['LULU','RL','TPR','UAA','VFC','PVH','COLM','DECK','CROX','WWW','HBI','LEVI','SKX','CPRI','FOSL','CRI','GIII','OXM','PLCE','CHS','SHOO','ANF','AEO','URBN','GPS','LB','FL','KSS','M','BBY','HAS','MAT','HOG','PII','WHR','NWL','LEA','TIF','SBUX','MCD','YUM','DRI','DPZ','CMG','MAR','HLT','NCLH','LZB','TPX','HELE','BC','YETI','SONO','GPRO','PTON','COTY','EL'],
'apparel_footwear_brands':['LULU','RL','TPR','UAA','VFC','PVH','COLM','DECK','CROX','WWW','HBI','LEVI','SKX','CPRI','FOSL','CRI','GIII','OXM','SHOO','TIF'],
'brand_leaders':['LULU','RL','TPR','UAA','VFC','PVH','COLM','DECK','LEVI','SKX','CPRI','TIF','SBUX','EL','HAS','MAT'],
}
for g,ks in groups.items():
    ks=[k for k in ks if k in M]
    for h in (1,3,5):
        x,y=pairs(ks,h)
        xw=wins(x);yw=wins(y)
        print(g,len(ks),'h',h,'n',len(x),'r',round(corr(x,y),3),'r_w',round(corr(xw,yw),3),'slope_w',round(slope(xw,yw),3))
