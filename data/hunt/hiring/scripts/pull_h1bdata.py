"""Pull H-1B LCA rows (DOL disclosure data as republished by h1bdata.info) per employer search term and year.
Usage: python3 pull_h1bdata.py <rawdir> <outcsv>"""
import sys, time, os, urllib.request, urllib.parse, io
import pandas as pd
raw, outcsv = sys.argv[1], sys.argv[2]
terms = {"nike": "nike", "nike_inc": "nike inc", "nike_usa": "nike usa", "nike_retail": "nike retail services", "nike_ihm": "nike ihm", "converse": "converse inc", "adidas": "adidas", "deckers": "deckers", "lululemon": "lululemon",
         "under_armour": "under armour", "on_running": "on running", "vf": "vf corporation", "skechers": "skechers", "new_balance": "new balance athletics", "foot_locker": "foot locker"}
frames = []
for key, term in terms.items():
    for yr in range(2019, 2027):
        fn = os.path.join(raw, f"h1b_{key}_{yr}.html")
        if not os.path.exists(fn):
            url = "https://h1bdata.info/index.php?" + urllib.parse.urlencode({"em": term, "job": "", "city": "", "year": yr})
            try:
                h = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (academic research)"}), timeout=90).read().decode("utf-8", "replace")
            except Exception as e:
                print("FAIL", key, yr, e); continue
            open(fn, "w").write(h); time.sleep(2)
        h = open(fn).read()
        try:
            t = pd.read_html(io.StringIO(h))[0]
        except Exception:
            print(key, yr, 0); continue
        t = t[t["EMPLOYER"].astype(str).str.len() < 80]
        t["search_key"] = key; t["search_year"] = yr
        frames.append(t); print(key, yr, len(t), flush=True)
df = pd.concat(frames, ignore_index=True)
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
df = df.loc[:, ~df.columns.str.startswith("unnamed")]
df.to_csv(outcsv, index=False)
