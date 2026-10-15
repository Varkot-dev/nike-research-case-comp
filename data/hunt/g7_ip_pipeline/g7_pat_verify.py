"""Verification: recount via independent count queries and compare with pulled rows (printed + written)."""
import json, csv, sys, collections
sys.path.insert(0, ".")
from pplib import *
p = PP()
out = []
def pulled(co, y, kind):
    n = 0
    for l in open(f"pat_raw_{co}.jsonl"):
        r = json.loads(l)
        if r["pub"][:4] == str(y):
            g = r["guid"]
            k = "S" if g.endswith("-S") else ("A" if "-A" in g[-4:] else "B")
            if k == kind: n += 1
    return n
for co, qa in [("Nike", "nike.asn."), ("adidas", "adidas.asn."), ("Puma", "puma.asn."), ("Deckers", "(deckers OR hoka).asn.")]:
    for y in (2013, 2017, 2019, 2024, 2025):
        Y = f'@PD>="{y}0101"<="{y}1231"'
        for kind, kq in [("S", "S.kd."), ("B", "(B1 OR B2).kd."), ("A", "A1.kd.")]:
            try: c = count(p, f"{qa} AND {kq} AND {Y}")
            except Exception as e: c = None
            out.append([co, y, kind, c, pulled(co, y, kind)])
            print(out[-1], flush=True)
csv.writer(open("g7_pat_verify_counts.csv", "w")).writerows([["company","pub_year","kind","independent_count_query","pulled_rows"]] + out)
