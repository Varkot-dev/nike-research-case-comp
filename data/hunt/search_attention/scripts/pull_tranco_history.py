"""Monthly Tranco ranks (1st and 15th of each month, 2019-06 to 2026-10) for a set of footwear / retail domains.

Source: https://tranco-list.eu/api/lists/date/<date> -> list id; https://tranco-list.eu/download/<id>/100000 (top 100k CSV).
Only rows for the tracked domains are kept (full lists are not stored; each top-100k CSV is ~2 MB).
Domains outside the top 100k are recorded as missing. Provider mix changes over time (Alexa dropped 2023,
Chrome UX Report and Cloudflare Radar added), so read ranks RELATIVE to each other on the same date.
Re-run: python3 -I pull_tranco_history.py <rawdir>
"""
import csv, io, json, os, sys, time, urllib.request, datetime

OUT = sys.argv[1] if len(sys.argv) > 1 else "../raw/tranco_hist"
os.makedirs(OUT, exist_ok=True)
UA = "NikeCaseCompResearch/1.0 (academic)"
DOMAINS = ["nike.com", "adidas.com", "newbalance.com", "hoka.com", "hokaoneone.com", "on.com", "on-running.com",
           "asics.com", "lululemon.com", "puma.com", "skechers.com", "brooksrunning.com", "saucony.com",
           "underarmour.com", "converse.com", "footlocker.com", "dickssportinggoods.com", "finishline.com",
           "jdsports.com", "jdsports.co.uk", "stockx.com", "goat.com", "zappos.com", "hypebeast.com",
           "deckers.com", "crocs.com", "vans.com", "salomon.com", "nike.com.cn", "adidas.co.uk", "adidas.de",
           "amazon.com", "walmart.com", "target.com"]


def fetch(url, binary=False):
    for i in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=180) as r:
                b = r.read()
            return b if binary else json.loads(b)
        except Exception as e:
            print("ERR", url, e, flush=True)
            time.sleep(20 * (i + 1))
    return None


dates = []
d = datetime.date(2019, 6, 1)
while d <= datetime.date(2026, 10, 13):
    dates.append(d)
    dates.append(d.replace(day=15))
    d = (d.replace(day=28) + datetime.timedelta(days=5)).replace(day=1)
dates.append(datetime.date(2026, 10, 13))

outcsv = os.path.join(OUT, "tranco_tracked_domains.csv")
have = set()
if os.path.exists(outcsv):
    for r in csv.DictReader(open(outcsv)):
        have.add(r["date"])
new = not os.path.exists(outcsv)
f = open(outcsv, "a", newline="")
w = csv.writer(f)
if new:
    w.writerow(["date", "list_id", "providers", "domain", "rank"])
for dt in dates:
    ds = dt.isoformat()
    if ds in have or dt > datetime.date(2026, 10, 13):
        continue
    meta = fetch(f"https://tranco-list.eu/api/lists/date/{ds}")
    time.sleep(3)
    if not meta or not meta.get("available"):
        print("no list", ds, flush=True)
        continue
    raw = fetch(f"https://tranco-list.eu/download/{meta['list_id']}/100000", binary=True)
    time.sleep(3)
    if raw is None:
        continue
    ranks = {}
    for line in io.StringIO(raw.decode("utf-8", "replace")):
        parts = line.strip().split(",")
        if len(parts) == 2 and parts[1] in DOMAINS:
            ranks[parts[1]] = parts[0]
    prov = "|".join(meta.get("configuration", {}).get("providers", []))
    for dom in DOMAINS:
        w.writerow([ds, meta["list_id"], prov, dom, ranks.get(dom, "")])
    f.flush()
    print("OK", ds, len(ranks), flush=True)
print("DONE", flush=True)
