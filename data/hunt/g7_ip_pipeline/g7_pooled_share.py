"""Pooled Nike share of (Nike + peers), 2017-19 vs 2024-26 (2026 = same partial period for Nike and peers, so no annualisation needed)."""
import csv
P7=["adidas","On","Deckers","NewBalance","ASICS","Puma","Lululemon"]; P6=P7[:-1]
out=[]
sp=list(csv.DictReader(open("g7_tm_same_period_jan_sep.csv")))
def tm(co,y,k): return int(next(r[k] for r in sp if r["company"]==co and r["year_jan_sep"]==str(y)))
pp=list(csv.DictReader(open("g7_pat_annual_by_pub_year.csv")))
def pt(co,y,k): return int(next(r[k] for r in pp if r["company"]==co and r["pub_year"]==str(y)))
def row(src,metric,fn,keyname):
    for peers,label in [(P7,"vs_7_peers"),(P6,"vs_6_footwear_peers")]:
        a=[sum(fn(c,y,metric) for y in ys) for ys,c in [((2017,2018,2019),"Nike")]][0]
        b=sum(fn("Nike",y,metric) for y in (2024,2025,2026))
        pa=sum(fn(c,y,metric) for y in (2017,2018,2019) for c in peers); pb=sum(fn(c,y,metric) for y in (2024,2025,2026) for c in peers)
        out.append([src,metric,label,a,pa,round(100*a/(a+pa),1),b,pb,round(100*b/(b+pb),1),round(100*b/(b+pb)-100*a/(a+pa),1)])
for m in ["apps","cl25","itu_1b_cl25","itu_new_product_names_cl25"]: row("TM (Jan-Sep each year)",m,tm,"")
for m in ["design_grants","design_grants_footwear","util_grants","util_grants_footwear_cpc","util_pubs","util_pubs_footwear_cpc"]: row("Patents (pub-year, 2026 to Oct 13)",m,pt,"")
w=csv.writer(open("g7_pooled_share_2017_19_vs_2024_26.csv","w",newline=""))
w.writerow(["source","metric","peer_set","nike_2017_19","peers_2017_19","nike_share_pct_2017_19","nike_2024_26","peers_2024_26","nike_share_pct_2024_26","change_pp"]); w.writerows(out)
for r in out: print(r)
