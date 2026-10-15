"""Weekly per-spider geojson pulls from All The Places for runs since 2025-01 (era with per-spider files).
Saves condensed gzip CSVs (same columns as atp_spider_snapshots.py). Usage: python3 -I atp_weekly_geojson.py <outdir> spider1,spider2"""
import json, sys, os, time, gzip, csv, urllib.request, urllib.error
UA = {"User-Agent": "Mozilla/5.0 (academic research script)"}
OUT, SP = sys.argv[1], sys.argv[2].split(","); os.makedirs(OUT, exist_ok=True)
def get(u): return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=300)
H = json.load(get("https://data.alltheplaces.xyz/runs/history.json"))
FIELDS = ["ref", "owner:type", "type", "brand", "name", "addr:country", "addr:state", "addr:city", "addr:postcode", "lat", "lon"]
for r in H:
    rid = r["run_id"]
    if rid < "2025-01" or not r.get("output_url"): continue
    base = r["output_url"].rsplit("/", 1)[0]
    for s in SP:
        dest = os.path.join(OUT, f"{rid[:10]}_{s}.csv.gz")
        if os.path.exists(dest): continue
        try: feats = json.load(get(f"{base}/output/{s}.geojson"))["features"]
        except urllib.error.HTTPError as e: print("miss", rid, s, e.code); continue
        except Exception as e: print("err", rid, s, e); continue
        with gzip.open(dest, "wt", newline="") as f:
            w = csv.writer(f); w.writerow(FIELDS)
            for ft in feats:
                p = ft.get("properties", {}); g = (ft.get("geometry") or {}).get("coordinates") or [None, None]
                w.writerow([p.get(k) for k in FIELDS[:-2]] + [g[1], g[0]])
        print(rid, s, len(feats), flush=True); time.sleep(0.5)
