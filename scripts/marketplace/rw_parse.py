"""Parse Running Warehouse catpage listings (colorway cells) -> item CSV + brand summary CSV."""
import sys, os, re, csv, html, json, collections, statistics as st
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
def parse(t):
    out=[]
    for c in re.split(r'<div class="cattable-wrap-cell gtm_impression"',t)[1:]:
        g=lambda a: (re.search(a+r'="([^"]*)"',c) or [None,None])[1]
        name=html.unescape(g("data-gtm_impression_name") or ""); brand=html.unescape(g("data-gtm_impression_brand") or "")
        price=g("data-gtm_impression_price"); code=g("data-code")
        model=re.search(r'cattable-wrap-cell-info-name">([^<]*)<',c)
        msrp=re.search(r'is-crossout">\$([\d,.]+)',c)
        flag=re.search(r'cattable-wrap-cell-info-flag[^"]*">([^<]*)<',c)
        p=float(price) if price else None; m=float(msrp.group(1).replace(",","")) if msrp else p
        out.append({"code":code,"brand":brand,"model":html.unescape(model.group(1)).strip() if model else None,"name":name,"price":p,"msrp":m,
            "on_sale":bool(msrp and m and p and p<m-0.01),"discount_pct":round(100*(1-p/m),1) if (p and m) else None,"flag":(flag.group(1).strip() if flag else "")})
    return out
if __name__=="__main__":
    data=sys.argv[1]; snap=sys.argv[2]; pages=sys.argv[3:]  # label=file
    items=[]
    for lp in pages:
        label,f=lp.split("=",1)
        rows=parse(open(f,encoding="utf-8",errors="ignore").read())
        for i,r in enumerate(rows): items.append({"snapshot_date":snap,"page":label,"position":i+1,**r})
    with open(os.path.join(data,"runningwarehouse_items.csv"),"w",newline="") as fh:
        wr=csv.DictWriter(fh,fieldnames=list(items[0].keys())); wr.writeheader(); wr.writerows(items)
    summ=[]
    for label in [lp.split("=")[0] for lp in pages]:
        R=[r for r in items if r["page"]==label]
        byb=collections.defaultdict(list)
        for r in R: byb[r["brand"]].append(r)
        for b,L in sorted(byb.items(),key=lambda x:-len(x[1])):
            models={r["model"] for r in L}; sale=[r for r in L if r["on_sale"]]
            top100=sum(1 for r in L if r["position"]<=100)
            summ.append({"snapshot_date":snap,"page":label,"brand":b,"colorways":len(L),"colorway_share_pct":round(100*len(L)/len(R),1),"models":len(models),
              "colorways_in_first100":top100,"colorways_on_sale":len(sale),"share_on_sale_pct":round(100*len(sale)/len(L),1),
              "avg_discount_on_sale_pct":round(st.mean(r["discount_pct"] for r in sale),1) if sale else None,"median_price":st.median(r["price"] for r in L)})
    with open(os.path.join(data,"runningwarehouse_brand_summary.csv"),"w",newline="") as fh:
        wr=csv.DictWriter(fh,fieldnames=list(summ[0].keys())); wr.writeheader(); wr.writerows(summ)
    for s in summ:
        if s["colorways"]>=10: print(s)
