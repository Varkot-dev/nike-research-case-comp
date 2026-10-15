"""Apple App Store top charts (legacy public iTunes RSS, JSON), by storefront and genre. Snapshot.
URL: https://itunes.apple.com/{cc}/rss/{chart}/limit=200/genre={g}/json  (returns top 100)
Writes raw/appstore_charts/{date}/{cc}_{chart}_{g}.json and appends tidy rows to appstore_charts_snapshot_{date}.csv
"""
import json, os, sys, time, urllib.request, csv, datetime
D = datetime.date.today().isoformat()
BASE = "/home/user/nike-research-case-comp/data/hunt/apps_digital"
RAW = f"{BASE}/raw/appstore_charts/{D}"; os.makedirs(RAW, exist_ok=True)
CCS = "us gb de fr it es nl ca au jp kr cn hk tw mx br in tr pl se ch be at dk no ie nz sg my th ph id vn za ae sa il cl co ar".split()
GENRES = {"6024": "Shopping", "6013": "Health & Fitness", "6012": "Lifestyle", "6004": "Sports", "all": "All"}
CHARTS = ["topfreeapplications", "topgrossingapplications"]
rows = []
for cc in CCS:
    for g in GENRES:
        for ch in CHARTS:
            if g == "all" and ch == "topgrossingapplications":
                continue
            url = f"https://itunes.apple.com/{cc}/rss/{ch}/limit=200/" + ("" if g == "all" else f"genre={g}/") + "json"
            fn = f"{RAW}/{cc}_{ch}_{g}.json"
            if not os.path.exists(fn):
                try:
                    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=60) as r:
                        open(fn, "wb").write(r.read())
                except Exception as e:
                    print("ERR", url, e, flush=True); continue
                time.sleep(0.7)
            try:
                d = json.load(open(fn))
                ents = d["feed"].get("entry", [])
                if isinstance(ents, dict): ents = [ents]
            except Exception as e:
                print("PARSE", fn, e); continue
            for i, x in enumerate(ents):
                rows.append([D, cc, ch, GENRES[g], i + 1, x["id"]["attributes"]["im:id"], x["im:name"]["label"], x.get("im:artist", {}).get("label", "")])
    print(cc, len(rows), flush=True)
with open(f"{BASE}/raw/appstore_charts_all_{D}.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["date", "country", "chart", "genre", "rank", "app_id", "app_name", "developer"]); w.writerows(rows)
