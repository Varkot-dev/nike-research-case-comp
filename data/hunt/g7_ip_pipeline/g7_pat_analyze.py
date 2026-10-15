"""Annual US design/utility patent grants and published applications, Nike vs peers. Input pat_raw_<co>.jsonl, pat_fwcpc_<co>.json."""
import json, re, csv, collections, statistics as st
from datetime import date
COS = ["Nike","adidas","On","Deckers","NewBalance","ASICS","Puma","Lululemon"]
PEERS = COS[1:]; FOOT = ["adidas","On","Deckers","NewBalance","ASICS","Puma"]
FWT = re.compile(r"\b(shoe|shoes|footwear|boot|boots|sandal|sneaker|cleat|cleats|sole|midsole|outsole|insole|slipper|upper|lace|shoelace|heel)\b", re.I)
SOCK = re.compile(r"sock|hosiery|legwear", re.I)
def kind(g):
    if g.endswith("-S"): return "design_grant"
    if re.search(r"-A\d$", g): return "util_pub"
    if re.search(r"-B\d$", g): return "util_grant"
    return "other"
def is_fw_design(r):
    m = r["main"] or ""; t = r["title"] or ""
    cls = bool(re.match(r"D2/(8[9]\d|9\d\d)$", m)) and not SOCK.search(t)
    ttl = bool(FWT.search(t)) and not SOCK.search(t) and not re.search(r"display|icon|interface|screen", t, re.I)
    return cls, ttl
data = {}; fw = {}
for co in COS:
    rows = {}
    for l in open(f"pat_raw_{co}.jsonl"):
        r = json.loads(l); rows[r["guid"]] = r
    data[co] = list(rows.values()); fw[co] = set(json.load(open(f"pat_fwcpc_{co}.json")))
allpub = [r["pub"] for co in COS for r in data[co]]
LAST = max(allpub); LASTD = date.fromisoformat(LAST)
FRAC26 = (LASTD - date(2025, 12, 31)).days / 365.0
print("latest publication date in data", LAST, "fraction of 2026", round(FRAC26, 3))
per = collections.defaultdict(collections.Counter)
perF = collections.defaultdict(collections.Counter)   # by filing year
lags = collections.defaultdict(list)
for co in COS:
    for r in data[co]:
        k = kind(r["guid"]); 
        if k == "other": continue
        y = int(r["pub"][:4]); c = per[(co, y)]
        fy = int(r["filed"][:4]) if r["filed"] else None
        if k == "design_grant":
            cls, ttl = is_fw_design(r); f = cls or ttl
            c["design_grants"] += 1
            if f: c["design_grants_footwear"] += 1
            if cls != ttl: c["design_fw_class_vs_title_disagree"] += 1
            if (r["main"] or "").startswith("D14"): c["design_grants_display_icon_D14"] += 1
            if fy: perF[(co, fy)]["design_grants_by_filing_year"] += 1; perF[(co, fy)]["design_grants_footwear_by_filing_year"] += int(f)
        elif k == "util_grant":
            c["util_grants"] += 1; f = r["guid"] in fw[co]
            if f: c["util_grants_footwear_cpc"] += 1
            if fy: perF[(co, fy)]["util_grants_by_filing_year"] += 1; perF[(co, fy)]["util_grants_fw_by_filing_year"] += int(f)
        elif k == "util_pub":
            c["util_pubs"] += 1; f = r["guid"] in fw[co]
            if f: c["util_pubs_footwear_cpc"] += 1
            if fy: perF[(co, fy)]["util_pubs_by_filing_year"] += 1; perF[(co, fy)]["util_pubs_fw_by_filing_year"] += int(f)
        if r["filed"]:
            lag = (date.fromisoformat(r["pub"]) - date.fromisoformat(r["filed"][:10])).days / 30.44
            lags[(co, k, y)].append(lag)
cols = ["design_grants","design_grants_footwear","design_grants_display_icon_D14","util_grants","util_grants_footwear_cpc","util_pubs","util_pubs_footwear_cpc","design_fw_class_vs_title_disagree"]
YRS = list(range(2012, 2027))
with open("g7_pat_annual_by_pub_year.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["company","pub_year","note"] + cols)
    for co in COS:
        for y in YRS: w.writerow([co, y, f"YTD to {LAST}" if y == 2026 else ""] + [per[(co, y)][k] for k in cols])
fcols = ["design_grants_by_filing_year","design_grants_footwear_by_filing_year","util_grants_by_filing_year","util_grants_fw_by_filing_year","util_pubs_by_filing_year","util_pubs_fw_by_filing_year"]
with open("g7_pat_annual_by_filing_year.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["company","filing_year","note"] + fcols)
    for co in COS:
        for y in range(2012, 2027): w.writerow([co, y, "right-censored: designs take ~2y to grant, utility apps publish at 18m" if y >= 2024 else ""] + [perF[(co, y)][k] for k in fcols])
with open("g7_pat_lags_months.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["company","kind","pub_year","n","median_months_filing_to_pub"])
    for (co, k, y), v in sorted(lags.items()):
        if co in ("Nike","adidas") and y >= 2017: w.writerow([co, k, y, len(v), round(st.median(v), 1)])
def tot(cos, y, k): return sum(per[(c, y)][k] for c in cos)
SHARE = [("design_grants",), ("design_grants_footwear",), ("util_grants",), ("util_grants_footwear_cpc",), ("util_pubs",), ("util_pubs_footwear_cpc",)]
with open("g7_pat_nike_share.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["pub_year","metric","nike","peers7_total","nike_share_of_nike_plus_peers7","peers6_footwear_total","nike_share_vs_footwear6"])
    for y in YRS:
        for (k,) in SHARE:
            n = per[("Nike", y)][k]; p7 = tot(PEERS, y, k); p6 = tot(FOOT, y, k)
            w.writerow([y, k, n, p7, round(n/(n+p7), 4) if n+p7 else "", p6, round(n/(n+p6), 4) if n+p6 else ""])
with open("g7_pat_change_2024_26_vs_2017_19.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["entity","metric","avg_2017_19","2024","2025","2026_ytd","2026_annualized","avg_2024_26_annualized","change_pct_vs_2017_19"])
    for ent, cl in [(c, [c]) for c in COS] + [("Peers7", PEERS), ("Peers6_footwear", FOOT)]:
        for (k,) in SHARE:
            a = sum(tot(cl, y, k) for y in (2017, 2018, 2019)) / 3
            y24, y25, y26 = tot(cl, 2024, k), tot(cl, 2025, k), tot(cl, 2026, k)
            ann = y26 / FRAC26; avg = (y24 + y25 + ann) / 3
            w.writerow([ent, k, round(a, 1), y24, y25, y26, round(ann, 1), round(avg, 1), round(100*(avg/a-1), 1) if a else ""])
print("ok")
