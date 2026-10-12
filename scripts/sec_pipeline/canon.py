"""Pick one canonical, cited value per (metric, period) from master.csv; report cross-source conflicts."""
import csv, json, os, re, sys, collections
S = sys.argv[1]; OUTDIR = sys.argv[2]
rows = [r for r in csv.DictReader(open(os.path.join(S, "extract/master.csv"))) if r["check"] in ("OK",)]
OFFSET = {}
for fn in os.listdir(os.path.join(S, "sec/text")):
    t = open(os.path.join(S, "sec/text", fn)).read()
    h = re.findall(r"=== PAGE (\d+) \| printed: ([^ ]+) ===", t)
    d = collections.Counter(int(a) - int(b) for a, b in h if b.isdigit())
    OFFSET[fn[:-4]] = d.most_common(1)[0][0] if d and d.most_common(1)[0][1] >= 5 else None
def qname(doc):
    m = re.search(r"q(\d)fy(\d\d)", doc)
    return f"Q{m.group(1)}FY20{m.group(2)}" if m else None
def fy_of_end(date):
    y, mth = int(date[:4]), int(date[5:7])
    fy = y + 1 if mth >= 6 else y
    q = {8: 1, 11: 2, 2: 3, 5: 4}.get(mth)
    return fy, q
def doc_label(doc):
    form, period, filed = doc.split("_")[:3]
    fy, q = fy_of_end(period)
    if form == "10-K": return f"FY{fy} Form 10-K (filed {filed})"
    if form == "10-Q": return f"Q{q} FY{fy} Form 10-Q (filed {filed})"
    if form == "DEF14A": return f"2026 Proxy Statement, DEF 14A (filed {filed})"
    if "exhibit991er" in doc: return f"{qname(doc).replace('FY', ' FY')} earnings release, 8-K Ex. 99.1 (filed {filed})"
    return f"Form 8-K (filed {filed})"
def page_label(doc, seq):
    off = OFFSET.get(doc)
    if off is not None and not doc.startswith("8-K"):
        p = int(seq) - off
        return f"p. {p}" if p >= 1 else "cover"
    return f"p. {seq} of exhibit" if "exhibit" in doc else f"p. {seq}"
def pref(r):
    doc, per = r["doc"], r["period"]
    form, pend = doc.split("_")[:2]
    fy, q = fy_of_end(pend)
    score = 9
    if re.fullmatch(r"FY\d{4}", per):
        target = int(per[2:])
        if form == "10-K" and fy == target: score = 0
        elif "exhibit991er" in doc and qname(doc) == f"Q4FY{target}": score = 1
        elif form == "10-K": score = 2 + abs(fy - target)
    elif re.fullmatch(r"Q\dFY\d{4}", per):
        if form == "10-Q" and f"Q{q}FY{fy}" == per: score = 0
        elif "exhibit991er" in doc and qname(doc) == per: score = 1
        elif form == "10-K" and per.startswith("Q4") and f"FY{fy}" == per[2:]: score = 2
        else: score = 5
    elif re.fullmatch(r"\d{4}-\d{2}-\d{2}", per):
        if pend == per and form in ("10-K", "10-Q"): score = 0
        elif pend == per: score = 1
        else: score = 4
    elif form == "DEF14A": score = 0
    v = r["value"].replace(",", "")
    if r["unit"] in ("usd_b","usd_bn","usd_billions") or (r["unit"] == "usd_m" and "." in v and abs(float(v or 0)) < 100 and not r["metric"].endswith(("_pct","per_share"))):
        score += 20
    return score
groups = collections.defaultdict(list)
for r in rows: groups[(r["metric"], r["period"])].append(r)
out, conflicts = [], []
for (m, p), rs in sorted(groups.items()):
    rs.sort(key=pref)
    best = rs[0]
    vals = collections.Counter(re.sub(r"[,\s]", "", x["value"]) for x in rs)
    if len(vals) > 1: conflicts.append((m, p, dict(vals), [(x["doc"][:40], x["value"]) for x in rs[:6]]))
    val = best["value"]
    if m in ("dividends_paid","share_repurchases","capex") and val.startswith("-"): val = val[1:]
    out.append({"metric": m, "period": p, "value": val, "unit": best["unit"], "filing": doc_label(best["doc"]),
                "page": page_label(best["doc"], best["seq_page"]), "url": best["url"], "quote": best["quote"],
                "n_sources_agreeing": vals[re.sub(r"[,\s]", "", best["value"])], "n_sources": len(rs)})
os.makedirs(OUTDIR, exist_ok=True)
with open(os.path.join(OUTDIR, "nike_filing_facts.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
json.dump(conflicts, open(os.path.join(S, "extract/conflicts.json"), "w"), indent=1)
print(len(out), "facts;", len(conflicts), "conflicts")
