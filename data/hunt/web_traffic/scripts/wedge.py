"""Revenue-per-visit wedge: (1+digital revenue growth)/(1+Semrush visit growth)-1, by region. Run: python3 -I wedge.py"""
import csv, os
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..")
rows=[
 ("Global NIKE Brand Digital (Q1 FY27, Jun-Aug 2026, reported USD)",-13,"Semrush global nike.com Aug 2026 YoY",-11.39,"q1fy27 8-K Ex.99.1 (OPENED via repo facts); semrush_trending_global_2026-08_long.csv (OPENED raw)"),
 ("North America digital (cc)",-6,"Semrush US+CA nike.com Aug 2026, traffic-weighted",-11.4,"10-Q p.~23 (OPENED 2026-10-15); semrush_trending_2026-08_long.csv"),
 ("EMEA digital (cc), all 8 countries",-26,"Semrush DE,GB,FR,IT,ES,NL,PL,SE traffic-weighted",2.2,"10-Q p.27 (OPENED); includes GB +34.4%"),
 ("EMEA digital (cc), ex-GB",-26,"Semrush DE,FR,IT,ES,NL,PL,SE traffic-weighted",-6.8,"10-Q p.27 (OPENED)"),
 ("APLA digital (cc)",-10,"Semrush JP,KR,AU,MX,TW,IN traffic-weighted (BR, CL, AR omitted)",-24.5,"10-Q (OPENED)"),
 ("Greater China digital (cc)",-28,"not measurable (Semrush has no nike.com.cn; nike.com CN page is 133k visits, desktop-only)",None,"10-Q p.28 (OPENED)"),
]
with open(os.path.join(D,"test_revenue_per_visit_wedge.csv"),"w",newline="") as f:
    w=csv.writer(f); w.writerow(["segment","reported_digital_revenue_growth_pct","traffic_measure","traffic_yoy_pct","implied_revenue_per_visit_change_pct","source_tag"])
    for s,g,m,t,src in rows:
        w.writerow([s,g,m,t,"" if t is None else round(((1+g/100)/(1+t/100)-1)*100,1),src])
        print(s,g,t,"" if t is None else round(((1+g/100)/(1+t/100)-1)*100,1))
