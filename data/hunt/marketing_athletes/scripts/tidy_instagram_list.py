"""Parse revisions of Wikipedia 'List of most-followed Instagram accounts' into handle x date follower counts (millions)."""
import sys, json, glob, re, os, csv
RAW, OUT = sys.argv[1], sys.argv[2]
rows = []
for f in sorted(glob.glob(os.path.join(RAW, "*.json"))):
    d = json.load(open(f)); pg = list(d["query"]["pages"].values())[0]
    if "revisions" not in pg: continue
    r = pg["revisions"][0]; txt = r["slots"]["main"]["*"]
    # first wikitable only (main ranking)
    tabs = []; pos = 0
    while True:
        i = txt.find("{|", pos)
        if i < 0: break
        j = txt.find("\n|}", i); tabs.append(txt[i:j]); pos = j + 1 if j > 0 else len(txt)
    tab = max(tabs, key=lambda x: x.count("instagram.com/")) if tabs else ""
    for blk in tab.split("\n|-")[1:]:
        h = re.search(r"instagram\.com/([A-Za-z0-9_.]+)", blk)
        if not h: continue
        rk = None; fol = None
        for ln in blk.strip().split("\n"):
            last = ln.split("|")[-1].strip()
            if not re.fullmatch(r"\d{1,3}(?:\.\d+)?", last): continue
            if ln.startswith("!") or (rk is None and fol is None and "instagram.com" not in blk.split(ln)[0]):
                rk = int(float(last))
            elif fol is None:
                fol = float(last)
        if fol is not None:
            rows.append(dict(snapshot_file=os.path.basename(f), rev_timestamp=r["timestamp"], revid=r["revid"], handle=h.group(1).lower(), rank=rk, followers_m=fol))
w = csv.DictWriter(open(OUT, "w"), fieldnames=["snapshot_file", "rev_timestamp", "revid", "handle", "rank", "followers_m"]); w.writeheader(); w.writerows(rows)
print(len(rows))
