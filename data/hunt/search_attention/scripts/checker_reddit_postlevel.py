import gzip,csv,glob,os,re,sys,math
import pandas as pd
R=sys.argv[1]
T={"nike":r"\bnike'?s?\b","jordan":r"\b(jordan|aj ?1|aj ?4|aj ?11|jumpman)\b","dunk":r"\bdunks?\b","af1":r"\b(af ?1|air force)\b","air_max":r"\bair ?max\b",
"nike_run_any":r"\b(pegasus|vomero|vaporfly|alphafly|invincible|zoomfly|zoom fly|streakfly|structure)\b",
"adidas":r"\badidas\b","samba":r"\bsambas?\b","gazelle":r"\bgazelles?\b","adizero":r"\badizero|adios|evo sl\b",
"new_balance":r"\b(new balance|nb ?\d{3,4})\b","asics":r"\basics\b|\bnovablast|superblast|gel[- ]kayano|nimbus\b",
"hoka":r"\bhoka\b|\bclifton|bondi\b","on":r"\bon (running|cloud)|\bcloud(monster|surfer|boom|tilt)\b",
"saucony":r"\bsaucony\b|\bendorphin\b","brooks":r"\bbrooks\b|\bghost \d|glycerin\b","puma":r"\bpuma\b","salomon":r"\bsalomon\b","onitsuka":r"\bonitsuka\b","converse":r"\bconverse\b|\bchuck"}
C={k:re.compile(v,re.I) for k,v in T.items()}
SETS={"RunningShoeGeeks":(["nike","nike_run_any"],["hoka","asics","on","saucony","brooks","adidas","adizero","new_balance","puma"]),
"Sneakers":(["nike","jordan","dunk","af1","air_max"],["adidas","samba","gazelle","new_balance","asics","onitsuka","salomon","puma","converse"])}
rows=[]
for sub,(nk,rv) in SETS.items():
  for fn in sorted(glob.glob(os.path.join(R,"reddit_titles",sub,"*.csv.gz"))):
    m=os.path.basename(fn)[:7]; n=nn=rr=both=0; sumN=sumR=0
    for r in csv.DictReader(gzip.open(fn,"rt")):
      t=r["title"] or ""
      if t.startswith("[ Removed") or t in("[deleted]","[removed]"): continue
      n+=1; a=any(C[k].search(t) for k in nk); b=any(C[k].search(t) for k in rv)
      nn+=a; rr+=b; both+=a and b
    rows.append((sub,m,n,nn,rr,both))
d=pd.DataFrame(rows,columns=["sub","month","posts","nike_posts","rival_posts","both"])
def per(m):
  y=int(m[:4]); mo=int(m[5:])
  return str(y) if y<2025 else f"{y}H{1 if mo<=6 else 2}"
d["period"]=d.month.map(per)
d.to_csv("postlevel_monthly.csv",index=False)
for sub in SETS:
  g=d[d["sub"]==sub].groupby("period")[["posts","nike_posts","rival_posts"]].sum()
  g["share"]=100*g.nike_posts/(g.nike_posts+g.rival_posts); print(sub); print(g.loc["2023":].round(2).to_string())
def z(sub,a,b):
  x=d[(d["sub"]==sub)]
  A=x[x.month.str[:4].isin(a)];B=x[x.month.str[:4].isin(b)]
  if isinstance(a,tuple):pass
  n1,k1=A.nike_posts.sum()+A.rival_posts.sum(),A.nike_posts.sum(); n2,k2=B.nike_posts.sum()+B.rival_posts.sum(),B.nike_posts.sum()
  p1,p2=k1/n1,k2/n2;p=(k1+k2)/(n1+n2);zz=(p2-p1)/math.sqrt(p*(1-p)*(1/n1+1/n2))
  print(sub,a,"->",b,f"{100*p1:.1f}% (n={n1}) -> {100*p2:.1f}% (n={n2}) z={zz:.2f} p={math.erfc(abs(zz)/2**.5):.3f}")
for sub in SETS:
  z(sub,["2025"],["2026"]); z(sub,["2023"],["2026"])
# post-break only (Oct2025 onwards): Oct-Dec2025 vs Jul-Oct 2026
x=d[d["sub"]=="Sneakers"]
for lab,ms in [("2025-10..2026-03",[m for m in x.month if "2025-10"<=m<="2026-03"]),("2026-04..2026-10",[m for m in x.month if "2026-04"<=m<="2026-10"]),("2025-01..2025-09",[m for m in x.month if "2025-01"<=m<="2025-09"])]:
  y=x[x.month.isin(ms)];print("Sneakers",lab,round(100*y.nike_posts.sum()/(y.nike_posts.sum()+y.rival_posts.sum()),1),y.nike_posts.sum()+y.rival_posts.sum())
