"""For a set of All The Places runs (roughly quarterly 2019-2026), extract per-store rows for selected
spiders and save a condensed gzip CSV per run+spider. Handles three archive eras:
 - 2018..2022-11: output.tar.gz (download whole, ~35-85 MB, stream extract)
 - 2022-11..2024: output.zip (HTTP Range extraction of members only)
 - 2025+: per-spider output/<spider>.geojson
Usage: python3 -I atp_spider_snapshots.py <outdir>"""
import json, sys, os, time, tarfile, gzip, csv, io, re, urllib.request, urllib.error
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from remote_zip import HttpFile
import zipfile
UA = {"User-Agent": "Mozilla/5.0 (academic research script)"}
SPIDERS = ["nike", "converse", "adidas", "foot_locker", "dicks_sporting_goods", "academy_us", "academy",
           "hibbett_sports", "jd_sports_us", "finish_line", "dsw", "champs_sports", "skechers", "puma", "new_balance"]
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
def get(u): return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=600)
H = json.load(get("https://data.alltheplaces.xyz/runs/history.json"))
# pick first run in each Jan/Apr/Jul/Oct from 2019
picked, seen = [], set()
for r in H:
    y, m = r['run_id'][:4], int(r['run_id'][5:7])
    if y < '2019' or not r.get('output_url'): continue
    if m in (1, 4, 7, 10) and (y, m) not in seen:
        seen.add((y, m)); picked.append(r)
picked.append(H[-1])
FIELDS = ["ref", "owner:type", "type", "brand", "name", "addr:country", "addr:state", "addr:city", "addr:postcode", "lat", "lon"]
def condense(rid, spider, raw):
    try: feats = json.loads(raw)["features"]
    except Exception:
        feats = [json.loads(l) for l in raw.decode("utf8", "ignore").splitlines() if l.strip().startswith("{")]
    path = os.path.join(OUT, f"{rid[:10]}_{spider}.csv.gz")
    with gzip.open(path, "wt", newline="") as f:
        w = csv.writer(f); w.writerow(FIELDS)
        for ft in feats:
            p = ft.get("properties", {}); g = (ft.get("geometry") or {}).get("coordinates") or [None, None]
            w.writerow([p.get(k) for k in FIELDS[:-2]] + [g[1], g[0]])
    return len(feats)
log = open(os.path.join(OUT, "_snapshot_log.csv"), "a")
for r in picked:
    rid, url = r['run_id'], r['output_url']
    done = [s for s in SPIDERS if os.path.exists(os.path.join(OUT, f"{rid[:10]}_{s}.csv.gz"))]
    if len(done) > 0: continue
    try:
        if url.endswith(".tar.gz"):
            data = get(url).read()
            with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as t:
                for m in t.getmembers():
                    b = os.path.basename(m.name).rsplit(".", 1)[0]
                    if b in SPIDERS and m.isfile():
                        n = condense(rid, b, t.extractfile(m).read()); log.write(f"{rid},{b},{n},tar\n")
        elif rid < "2025-01":
            z = zipfile.ZipFile(io.BufferedReader(HttpFile(url), buffer_size=1 << 20))
            for nm in z.namelist():
                b = os.path.basename(nm).rsplit(".", 1)[0]
                if b in SPIDERS:
                    n = condense(rid, b, z.open(nm).read()); log.write(f"{rid},{b},{n},zip\n")
        else:
            base = url.rsplit("/", 1)[0]
            for s in SPIDERS:
                try:
                    n = condense(rid, s, get(f"{base}/output/{s}.geojson").read()); log.write(f"{rid},{s},{n},geojson\n")
                except urllib.error.HTTPError: pass
                time.sleep(0.5)
    except Exception as e:
        print("FAIL", rid, e, flush=True); log.write(f"{rid},ERROR,{e!r},\n")
    log.flush(); print("done", rid, flush=True); time.sleep(1)
