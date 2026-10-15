"""Fetch Foot Locker sale-shoes listings per brand (pageSize=200), Nike split by price band."""
import sys, os, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import get
out=sys.argv[1]
BR=["Nike","Jordan","adidas","New Balance","ASICS®","HOKA","On","PUMA","Saucony","Brooks","Converse"]
BANDS=['%22-inf%22-%2225%22','%2225%22-%2250%22','%2250%22-%2275%22','%2275%22-%22100%22','%22100%22-%22150%22','%22150%22-%22inf%22']
for b in BR:
    q="%3Arelevance%3Acollection_id%3Asale-shoes%3Abrand%3A"+urllib.parse.quote(b)
    qs=[q+"%3Aprice%3A"+x for x in BANDS] if b=="Nike" else [q]
    for qq in qs:
        u="https://www.footlocker.com/category/sale/shoes.html?query="+qq+"&pageSize=200"
        p,s=get(u,out); print(b,s,p,flush=True)
