"""Zipf rank->traffic share inside the peer set. Assumption: visits ~ rank^-alpha, alpha 0.79 (cross-section fit, tests.py A), also 1.0.
Peer set (global domains): nike, adidas, on (on.com), hoka, newbalance, asics, lululemon. Domains not in top 100k are dropped (set to 0).
Quarter windows are Nike fiscal quarters. Run: python3 -I zipf_share.py"""
import csv, os, statistics as st
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..")
W=list(csv.DictReader(open(os.path.join(D,"tranco_rank_wide.csv"))))
SET=["nike.com","adidas.com","on.com","hoka.com","newbalance.com","asics.com","lululemon.com"]
def fq(ds):
    y,m=int(ds[:4]),int(ds[5:7])
    if m>=6: fy=y+1; q=1 if m<=8 else (2 if m<=11 else 3)
    else: fy=y; q=3 if m<=2 else 4
    return f"FY{fy}Q{q}"
out={}
for a in (0.79,1.0):
    for r in W:
        v={d:(int(r[d])**-a if r[d] else 0.0) for d in SET}
        t=sum(v.values())
        out.setdefault((fq(r["date"]),a),[]).append({d:v[d]/t for d in SET})
with open(os.path.join(D,"tranco_zipf_peer_share_by_fq.csv"),"w",newline="") as f:
    w=csv.writer(f); w.writerow(["fq","alpha"]+[d+"_share_pct" for d in SET])
    for (q,a),L in sorted(out.items()):
        w.writerow([q,a]+[round(100*st.mean(x[d] for x in L),1) for d in SET])
