"""Build tidy weekly door-count panels from All The Places condensed snapshots.
Outputs:
  nike_locator_weekly_counts.csv  (run_date, region_bucket, owner_type, n)
  partner_doors_weekly_atp.csv    (run_date, spider, n, n_us)
  nike_locator_store_events.csv   (ref, first_seen, last_seen, owner_type, country, brand) for churn tests
Usage: python3 -I build_weekly_panel.py <weekly_dir> <snap_dir> <outdir>"""
import sys, os, glob, re, pandas as pd
wd, sd, out = sys.argv[1], sys.argv[2], sys.argv[3]
files = sorted(glob.glob(os.path.join(wd, "*.csv.gz"))) + sorted(glob.glob(os.path.join(sd, "*.csv.gz")))
nk, pt, ev = [], [], {}
def bucket(c):
    if c == "CN": return "China mainland"
    if c in ("US",): return "US"
    if c in ("CA", "MX"): return "Canada+Mexico"
    if c in ("HK", "TW", "MO"): return "HK/TW/Macau"
    if c in ("KR", "JP"): return "Korea+Japan"
    return "Rest of world"
seen = set()
for f in files:
    b = os.path.basename(f); date, sp = b[:10], b[11:-7]
    if (date, sp) in seen: continue
    seen.add((date, sp))
    try: d = pd.read_csv(f, dtype=str)
    except Exception: continue
    if len(d) == 0: continue
    if sp == "nike":
        if d["owner:type"].isna().all(): continue
        d["bucket"] = d["addr:country"].map(bucket)
        g = d.groupby(["bucket", "owner:type", "brand"]).size().reset_index(name="n"); g.insert(0, "run_date", date); nk.append(g)
        for r in d.itertuples():
            k = r.ref
            if k not in ev: ev[k] = [k, date, date, getattr(r, "_2"), r._6, r.brand, r._8]
            else:
                ev[k][1] = min(ev[k][1], date); ev[k][2] = max(ev[k][2], date)
    else:
        pt.append([date, sp, len(d), int((d["addr:country"].isin(["US", "USA"])).sum())])
pd.concat(nk).to_csv(os.path.join(out, "nike_locator_weekly_counts.csv"), index=False)
pd.DataFrame(pt, columns=["run_date", "spider", "n", "n_us"]).sort_values(["spider", "run_date"]).to_csv(os.path.join(out, "partner_doors_weekly_atp.csv"), index=False)
pd.DataFrame(list(ev.values()), columns=["ref", "first_seen", "last_seen", "owner_type", "country", "brand", "city"]).to_csv(os.path.join(out, "nike_locator_store_events.csv"), index=False)
