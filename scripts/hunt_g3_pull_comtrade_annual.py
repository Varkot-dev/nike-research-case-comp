"""G3: annual footwear (HS 64) exports, World partner, from the UN Comtrade public preview API (no key, no login).
Writes research_notes/Smoking gun hunt/G3_official_footwear_exports_annual.csv. Value only: Comtrade holds no pairs or kg for HS 64 totals."""
import csv, json, os, subprocess, time
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "research_notes", "Smoking gun hunt", "G3_official_footwear_exports_annual.csv")
rows = []
for rep, name in ((704, "Vietnam"), (360, "Indonesia"), (156, "China")):
    for yr in range(2018, 2026):
        url = f"https://comtradeapi.un.org/public/v1/preview/C/A/HS?reporterCode={rep}&period={yr}&partnerCode=0&cmdCode=64&flowCode=X"
        d = None
        for _try in range(4):
            r = subprocess.run(["curl", "-sS", "-m", "30", url], capture_output=True, text=True).stdout
            try: d = json.loads(r)["data"]; break
            except Exception: time.sleep(3)
        if not d: continue
        for x in d:
            rows.append({"reporter": name, "calendar_year": yr, "hs": "64", "flow": "export", "partner": "World",
                         "value_usd_bn": round(x["primaryValue"] / 1e9, 3), "src_url": url, "tag": "OPENED (UN Comtrade preview API); reporter data as submitted"})
        time.sleep(0.5)
prev = {}
for r in rows:
    k = r["reporter"]
    r["yoy_pct"] = round(100 * (r["value_usd_bn"] / prev[k] - 1), 1) if k in prev else ""
    prev[k] = r["value_usd_bn"]
with open(OUT, "w", newline="") as f:
    wr = csv.DictWriter(f, fieldnames=list(rows[0].keys())); wr.writeheader(); wr.writerows(rows)
print(len(rows))
