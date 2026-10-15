"""Annual US trademark application counts, Nike vs peers, plus abandonments/cancellations. Input tm_raw_<co>.jsonl (g7_tm_pull.py)."""
import json, re, collections, csv
COS = ["Nike","adidas","On","Deckers","NewBalance","ASICS","Puma","Lululemon"]
PEERS = COS[1:]; FOOT = ["adidas","On","Deckers","NewBalance","ASICS","Puma"]
YRS = list(range(2012, 2027))
FW = re.compile(r"footwear|shoe|sneaker|boot|sandal|slipper|cleat|insole|sole\b|socks?\b|clog|flip.flop", re.I)
OWN_RX = {"Nike": r"^(nike,? inc\b|nike usa|nike innovate|brs, inc)"}
def prim_ok(co, r):
    on = r["ownerName"] if isinstance(r["ownerName"], list) else [r["ownerName"]]
    return co != "Nike" or re.match(OWN_RX["Nike"], on[0].lower().strip())
def classes(r):
    ic = r["internationalClass"] or []
    return {int(x.split()[-1]) for x in ic}
data = {}
for co in COS:
    rows = [json.loads(l) for l in open(f"tm_raw_{co}.jsonl")]
    data[co] = [r for r in rows if prim_ok(co, r)]
def goods_text(r): return " ".join(r["goodsAndServices"] or [])
def is_fw25(r):
    # footwear goods inside class 25 (text of goods list)
    g = goods_text(r)
    return 25 in classes(r) and bool(FW.search(g.split("IC 025")[-1][:2500])) if "IC 025" in g else False
def basis(r, k):
    b = r.get(k) or []
    return b if isinstance(b, list) else [b]
rows_out = []; seen_names = {co: set() for co in COS}
per = collections.defaultdict(lambda: collections.Counter())
for co in COS:
    for r in sorted(data[co], key=lambda x: x["filedDate"]):
        y = int(r["filedDate"][:4]); cl = classes(r)
        c = per[(co, y)]
        c["apps"] += 1
        if 25 in cl: c["cl25"] += 1
        if is_fw25(r): c["cl25_footwear_goods"] += 1
        if 9 in cl: c["cl9"] += 1
        if 42 in cl: c["cl42"] += 1
        if 9 in cl or 42 in cl: c["cl9_42"] += 1
        if cl and cl <= {35, 41, 38, 45}: c["services_only"] += 1
        if 18 in cl: c["cl18"] += 1
        if 28 in cl: c["cl28"] += 1
        if "1b" in basis(r, "originalBasis"): c["itu_1b"] += 1
        if any(b in ("44e", "66a", "44d") for b in basis(r, "originalBasis") + basis(r, "currentBasis")): c["foreign_44_66"] += 1
        wm = (r.get("wordmark") or "").strip().lower()
        if not wm: c["design_only_no_wordmark"] += 1
        elif wm not in seen_names[co]:
            c["new_wordmarks"] += 1; seen_names[co].add(wm)
        if (25 in cl) and wm and wm not in {x for x in []}:
            pass
# also new wordmarks in class 25 specifically
seen25 = {co: set() for co in COS}
for co in COS:
    for r in sorted(data[co], key=lambda x: x["filedDate"]):
        if 25 in classes(r):
            wm = (r.get("wordmark") or "").strip().lower()
            y = int(r["filedDate"][:4])
            if wm and wm not in seen25[co]:
                per[(co, y)]["new_wordmarks_cl25"] += 1; seen25[co].add(wm)
CORE = {"Nike": {"nike","swoosh","just do it","jumpman","jordan","acg","air","converse","nike air"},
        "adidas": {"adidas","trefoil","three stripes"}, "On": {"on","on running","cloudtec"}, "Deckers": {"ugg","hoka","teva","deckers","hoka one one"},
        "NewBalance": {"new balance","nb"}, "ASICS": {"asics","onitsuka tiger"}, "Puma": {"puma"}, "Lululemon": {"lululemon","lululemon athletica"}}
seenp = {co: set() for co in COS}
for co in COS:
    for r in sorted(data[co], key=lambda x: x["filedDate"]):
        wm = (r.get("wordmark") or "").strip().lower(); y = int(r["filedDate"][:4])
        if not wm or wm in CORE[co]: continue
        if wm in seenp[co]: continue
        seenp[co].add(wm)
        if 25 in classes(r): per[(co, y)]["new_product_names_cl25_ex_house"] += 1
cols = ["apps","cl25","cl25_footwear_goods","cl9","cl42","cl9_42","cl18","cl28","services_only","itu_1b","foreign_44_66","new_wordmarks","new_wordmarks_cl25","new_product_names_cl25_ex_house","design_only_no_wordmark"]
with open("g7_tm_annual_counts.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["company","filed_year","ytd_note"] + cols)
    for co in COS:
        for y in YRS:
            c = per[(co, y)]
            w.writerow([co, y, "Jan1-Sep30 only (data load 2026-10-02)" if y == 2026 else ""] + [c[k] for k in cols])
# share and change
def tot(cos, y, k): return sum(per[(c, y)][k] for c in cos)
with open("g7_tm_nike_share.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["filed_year","metric","nike","peers7_total","nike_share_of_peers7_plus_nike","peers6_footwear_total","nike_share_vs_footwear6"])
    for y in YRS:
        for k in ["apps","cl25","cl9_42","itu_1b","new_wordmarks","new_wordmarks_cl25","new_product_names_cl25_ex_house"]:
            n = per[("Nike", y)][k]; p7 = tot(PEERS, y, k); p6 = tot(FOOT, y, k)
            w.writerow([y, k, n, p7, round(n/(n+p7), 4) if n+p7 else "", p6, round(n/(n+p6), 4) if n+p6 else ""])
def avg(co_list, ys, k, scale=None):
    return sum(tot(co_list, y, k) * (scale if (scale and y == 2026) else 1) for y in ys) / len(ys)
ANN = 365/273  # Jan1-Sep30 = 273 days
with open("g7_tm_change_2024_26_vs_2017_19.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["entity","metric","avg_2017_19","avg_2024_25_full_years","2026_ytd_sep30","2026_annualized","avg_2024_26_annualized","change_pct_2024_26_vs_2017_19","change_pct_2024_25_vs_2017_19"])
    for ent, cl in [("Nike", ["Nike"]), ("adidas",["adidas"]), ("On",["On"]), ("Deckers",["Deckers"]), ("NewBalance",["NewBalance"]), ("ASICS",["ASICS"]), ("Puma",["Puma"]), ("Lululemon",["Lululemon"]), ("Peers7", PEERS), ("Peers6_footwear", FOOT)]:
        for k in ["apps","cl25","cl9_42","itu_1b","new_wordmarks","new_wordmarks_cl25","new_product_names_cl25_ex_house"]:
            a1719 = sum(tot(cl, y, k) for y in (2017, 2018, 2019)) / 3
            a2425 = sum(tot(cl, y, k) for y in (2024, 2025)) / 2
            ytd = tot(cl, 2026, k); ann = ytd * ANN
            a2426 = (tot(cl, 2024, k) + tot(cl, 2025, k) + ann) / 3
            w.writerow([ent, k, round(a1719, 2), round(a2425, 2), ytd, round(ann, 1), round(a2426, 2),
                        round(100*(a2426/a1719-1), 1) if a1719 else "", round(100*(a2425/a1719-1), 1) if a1719 else ""])
# abandonments and cancellations by event year
ab = collections.defaultdict(collections.Counter)
det = []
for co in COS:
    for r in data[co]:
        if r["abandonDate"]:
            y = int(r["abandonDate"][:4]); ab[(co, y)]["abandoned"] += 1
            if "1b" in basis(r, "originalBasis"): ab[(co, y)]["abandoned_itu_1b"] += 1
            if "NO STATEMENT OF USE" in (r["statusDescription"] or "").upper(): ab[(co, y)]["abandoned_no_SOU"] += 1
            if "FAILURE TO RESPOND" in (r["statusDescription"] or "").upper(): ab[(co, y)]["abandoned_failure_respond"] += 1
            if 25 in classes(r): ab[(co, y)]["abandoned_cl25"] += 1
            if co == "Nike" and y >= 2024:
                det.append([r["id"], r["wordmark"], r["filedDate"][:10], r["abandonDate"][:10], r["statusDescription"], ",".join(basis(r,"originalBasis")), ";".join(r["internationalClass"] or []), r["drawingCode"]])
        if r["cancelDate"]:
            y = int(r["cancelDate"][:4]); ab[(co, y)]["cancelled_registrations"] += 1
            if 25 in classes(r): ab[(co, y)]["cancelled_cl25"] += 1
acols = ["abandoned","abandoned_itu_1b","abandoned_no_SOU","abandoned_failure_respond","abandoned_cl25","cancelled_registrations","cancelled_cl25"]
with open("g7_tm_abandon_cancel.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["company","event_year"] + acols)
    for co in COS:
        for y in YRS: w.writerow([co, y] + [ab[(co, y)][k] for k in acols])
with open("g7_nike_tm_abandoned_2024_26_detail.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["serial","wordmark","filed","abandoned","status","original_basis","classes","drawing_code"]); w.writerows(sorted(det, key=lambda x: x[3]))
# cohort: share of applications filed in year Y now abandoned
with open("g7_tm_cohort_abandon_rate.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["company","filed_year","apps","now_abandoned","pct_abandoned","itu_1b_apps","itu_1b_now_abandoned"])
    for co in COS:
        for y in range(2012, 2027):
            rs = [r for r in data[co] if int(r["filedDate"][:4]) == y]
            a = sum(1 for r in rs if r["abandonDate"]); i = [r for r in rs if "1b" in basis(r, "originalBasis")]
            ia = sum(1 for r in i if r["abandonDate"])
            w.writerow([co, y, len(rs), a, round(100*a/len(rs), 1) if rs else "", len(i), ia])
print("ok")

# ---- extra: ITU new product names and lead-lag (filing date vs first use) ----
from datetime import date
def d(s):
    try: return date.fromisoformat(s[:10])
    except Exception: return None
seen2 = {co: set() for co in COS}; itu_new = collections.Counter()
for co in COS:
    for r in sorted(data[co], key=lambda x: x["filedDate"]):
        wm = (r.get("wordmark") or "").strip().lower(); y = int(r["filedDate"][:4])
        if wm and wm not in CORE[co] and wm not in seen2[co]:
            seen2[co].add(wm)
            if "1b" in basis(r, "originalBasis") and 25 in classes(r): itu_new[(co, y)] += 1
with open("g7_tm_itu_new_names_cl25.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["company","filed_year","itu_1b_new_product_names_cl25_ex_house"])
    for co in COS:
        for y in YRS: w.writerow([co, y, itu_new[(co, y)]])
ll = collections.defaultdict(list)
for co in COS:
    for r in data[co]:
        fu = d(r.get("firstUseCommerceDate") or r.get("firstUseAnyDate") or ""); fd = d(r["filedDate"])
        if fu and fd and 25 in classes(r):
            ll[(co, int(r["filedDate"][:4]), "1b" if "1b" in basis(r, "originalBasis") else ("1a" if "1a" in basis(r, "originalBasis") else "other"))].append((fu - fd).days)
import statistics as st
with open("g7_tm_leadlag_first_use.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["company","filed_year","original_basis","n_class25_with_first_use_date","median_days_first_use_minus_filed","pct_filed_before_first_use"])
    for k in sorted(ll):
        v = ll[k]; w.writerow(list(k) + [len(v), st.median(v), round(100*sum(1 for x in v if x > 0)/len(v), 1)])
print("extra ok")
