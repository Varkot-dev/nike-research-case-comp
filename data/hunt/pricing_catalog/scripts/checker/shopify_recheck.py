# Checker: re-pull page 1 of products.json for 3 stores and compare price, compare-at and created_at with the hunter's file.
import subprocess,json,sys,time,pandas as pd
h=pd.read_csv(sys.argv[1],dtype={"product_id":str}); rows=[]
for s in ["www.dtlr.com","pacersrunning.com","sneakerpolitics.com"]:
    r=subprocess.run(["curl","-sS","-m","60","-A","Mozilla/5.0 (research checker)",f"https://{s}/products.json?limit=250&page=2"],capture_output=True,text=True)
    for p in json.loads(r.stdout)["products"]:
        v=p["variants"]; pr=max(float(x["price"]) for x in v); ca=max(float(x["compare_at_price"] or 0) for x in v)
        m=h[(h.store==s)&(h.product_id==str(p["id"]))]
        rows.append([s,p["id"],p["vendor"],p["created_at"],pr,ca,len(m), m.price_max.iloc[0] if len(m) else None, m.compare_max.iloc[0] if len(m) else None, m.created_at.iloc[0] if len(m) else None])
    time.sleep(2)
R=pd.DataFrame(rows,columns=["store","id","vendor","created_now","price_now","compare_now","n_hunter","price_hunter","compare_hunter","created_hunter"])
R["price_match"]=R.price_now==R.price_hunter; R["created_match"]=R.created_now==R.created_hunter
R.to_csv(sys.argv[2],index=False)
print(R.groupby("store").agg(n=("id","size"),found=("n_hunter",lambda x:(x>0).sum()),dups=("n_hunter",lambda x:(x>1).sum()),price_match=("price_match","sum"),created_match=("created_match","sum")))
print(R[(R.n_hunter>0)&~R.price_match].head(8).to_string())
