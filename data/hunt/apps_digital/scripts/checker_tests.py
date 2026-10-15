"""Checker re-run of the Play review tests (does not overwrite the hunter's outputs)."""
import pandas as pd, numpy as np
B="/home/user/nike-research-case-comp/data/hunt/apps_digital"
q=pd.read_csv(f"{B}/play_reviews_fq.csv"); cal=pd.read_csv(f"{B}/test_play_calibration.csv")
# 1 calibration
c=cal.dropna(subset=["nike_app_us_yoy"])
print("r all",round(c.nike_brand_digital_yoy_pct.corr(c.nike_app_us_yoy),3),"n",len(c))
p=c[c.fq>="FY2023Q1"]; print("r FY23+ incl FY27Q1",round(p.nike_brand_digital_yoy_pct.corr(p.nike_app_us_yoy),3),"n",len(p))
p2=p[p.fq!="FY2027Q1"]; b,a=np.polyfit(p2.nike_app_us_yoy,p2.nike_brand_digital_yoy_pct,1)
res=p2.nike_brand_digital_yoy_pct-(a+b*p2.nike_app_us_yoy)
print("fit FY23Q1-FY26Q4: a=%.2f b=%.3f sd=%.2f n=%d r=%.3f"%(a,b,res.std(ddof=1),len(p2),p2.nike_brand_digital_yoy_pct.corr(p2.nike_app_us_yoy)))
for v,lab in [(-37.25,"Q1FY27"),(-32.8,"Q2td"),(-25.0,"Sep")]: print(lab,"implied",round(a+b*v,1))
# leave-one-out on FY23+ : how often does the review model call direction of QoQ change in digital?
d=c[["fq","nike_brand_digital_yoy_pct","nike_app_us_yoy"]].set_index("fq").diff().dropna()
print("same-direction QoQ all:",round((np.sign(d.iloc[:,0])==np.sign(d.iloc[:,1])).mean(),2),"n",len(d))
# FY25+ only (post-decline regime)
p3=c[c.fq>="FY2025Q1"]; print("r FY25+",round(p3.nike_brand_digital_yoy_pct.corr(p3.nike_app_us_yoy),3),"n",len(p3))
# 2 peer pool with and without dicks
for peers,lab in [(["adidas_app","stockx","goat","footlocker","dicks","zappos","champs"],"with dicks (as in script)"),
                  (["adidas_app","stockx","goat","footlocker","zappos","champs"],"without dicks (as in summary)")]:
    pe=q[q.app.isin(peers)&(q.locale=="en_us")&q.fq.isin(["FY2026Q2","FY2026Q3","FY2026Q4","FY2027Q1"])].groupby("fq")[["n_reviews","n_prev"]].sum()
    pe["yoy"]=(pe.n_reviews/pe.n_prev-1)*100; print(lab); print(pe.round(1).to_string())
# 3 volatility of the Nike-minus-peers gap (peers ex Dick's), and long-run decay of review volume
peers=["adidas_app","stockx","goat","footlocker","zappos","champs"]
pe=q[q.app.isin(peers)&(q.locale=="en_us")].groupby("fq")[["n_reviews","n_prev"]].sum()
pe["peer"]=(pe.n_reviews/pe.n_prev-1)*100
nk=q[(q.app=="nike_app")&(q.locale=="en_us")].set_index("fq")
g=(nk.yoy_pct-pe.peer).dropna(); g=g[g.index>="FY2022Q1"]
print("gap Nike-peers exDicks FY22+:"); print(g.round(1).to_string())
print("gap mean %.1f sd %.1f; QoQ change sd %.1f"%(g.mean(),g.std(),g.diff().std()))
ann=q[(q.locale=="en_us")&q.fq.str.endswith("Q1")].pivot(index="fq",columns="app",values="n_reviews")
print(ann[["nike_app","adidas_app","stockx","goat","footlocker","zappos","champs","nike_run_club"]].to_string())
for loc in ["de_de","fr_fr","ja_jp"]:
    t=q[(q.locale==loc)&q.fq.isin(["FY2026Q1","FY2027Q1","FY2026Q4","FY2025Q1"])][["app","fq","n_reviews","n_prev","yoy_pct"]]
    print(t.round(1).to_string())
