"""Cross-sectional web traffic test on Semrush 6-month histories, Similarweb Sep MoM and HypeStat MoM snapshots."""
import pandas as pd, numpy as np
BASE = "/home/user/nike-research-case-comp/data/hunt/apps_digital"
d = pd.read_csv(f"{BASE}/web_semrush_history.csv")
BRANDS = ["nike.com", "adidas.com", "hoka.com", "on.com", "newbalance.com", "puma.com", "underarmour.com", "skechers.com", "converse.com", "asics.com", "lululemon.com", "vans.com", "brooksrunning.com"]
out = []
for met, a, b in [("visits", "2026-04-01", "2026-09-01"), ("visits", "2026-07-01", "2026-09-01"), ("visits", "2026-06-01", "2026-08-01"),
                  ("search_organic", "2026-04-15", "2026-09-15"), ("search_organic", "2026-06-15", "2026-08-15"), ("mobile_visits", "2026-04-01", "2026-09-01")]:
    x = d[d.metric == met].pivot_table(index="domain", columns="month", values="value")
    if a not in x or b not in x: continue
    ch = ((x[b] / x[a] - 1) * 100).dropna()
    br = ch[ch.index.isin(BRANDS)]
    peers = br.drop("nike.com", errors="ignore")
    rank = (br.rank(ascending=False)["nike.com"] if "nike.com" in br else np.nan)
    out.append([met, a, b, round(br.get("nike.com", np.nan), 1), round(peers.median(), 1), len(peers), int(rank) if rank == rank else None, len(br), round((peers < br.get("nike.com", np.nan)).mean() * 100, 0)])
    print(met, a, "->", b); print(br.sort_values().round(1).to_string())
o = pd.DataFrame(out, columns=["metric", "from", "to", "nike_change_pct", "peer_median_change_pct", "n_peers", "nike_rank_best_is_1", "n_brands", "pct_peers_worse_than_nike"])
o.to_csv(f"{BASE}/test_web_traffic_cross_section.csv", index=False)
print(o.to_string())
s = pd.read_csv(f"{BASE}/web_similarweb_snapshot_2026-10-14.csv")
print(s[["domain", "mom_change_pct"]].sort_values("mom_change_pct").to_string())
