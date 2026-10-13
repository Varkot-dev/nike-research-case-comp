"""Extract the revenue disaggregation tables (segment x channel) from Nike 10-K and 10-Q notes.
Usage: python3 -I channel_split.py <text_dir> <manifest.json> <out.csv>"""
import csv, json, os, re, sys, collections
TEXT, MAN, OUT = sys.argv[1:4]
man = {os.path.splitext(m["local"])[0]: m for m in json.load(open(MAN))}
COLS = ["north_america", "emea", "greater_china", "apla", "global_brand_divisions", "nike_brand", "converse", "corporate", "nike_inc"]
ROWS = {"Sales to Wholesale Customers": "wholesale", "Sales through NIKE Direct": "direct",
        "Sales through Direct to Consumer": "direct", "Other": "other", "TOTAL REVENUES": "total"}
MONTHS = {"MAY": 5, "AUGUST": 8, "NOVEMBER": 11, "FEBRUARY": 2}
def num(c):
    c = c.strip().replace(",", "").replace(" ", "")
    if c in ("—", "-", ""): return 0.0
    neg = c.startswith("(")
    c = c.strip("()")
    return -float(c) if neg else float(c)
def period(header, doc):
    m = re.search(r"(YEAR|THREE MONTHS|SIX MONTHS|NINE MONTHS) ENDED (MAY|AUGUST|NOVEMBER|FEBRUARY) (\d{1,2},? )?(\d{4})", header.upper())
    if not m: return None
    kind, mon, yr = m.group(1), MONTHS[m.group(2)], int(m.group(4))
    fy = yr + 1 if mon >= 6 else yr
    q = {8: 1, 11: 2, 2: 3, 5: 4}[mon]
    return {"YEAR": f"FY{fy}", "THREE MONTHS": f"Q{q}FY{fy}", "SIX MONTHS": f"6MFY{fy}", "NINE MONTHS": f"9MFY{fy}"}[kind]
out = []
for fn in sorted(os.listdir(TEXT)):
    if not fn.startswith(("10-K", "10-Q")): continue
    doc = fn[:-4]; t = open(os.path.join(TEXT, fn)).read()
    h = re.findall(r"=== PAGE (\d+) \| printed: ([^ ]+) ===", t)
    off = collections.Counter(int(a) - int(b) for a, b in h if b.isdigit()).most_common(1)[0][0]
    lines = t.split("\n"); page = 0; header = ""
    for i, line in enumerate(lines):
        mp = re.match(r"=== PAGE (\d+) \|", line)
        if mp: page = int(mp.group(1)); continue
        if re.search(r"(YEAR|THREE MONTHS|SIX MONTHS|NINE MONTHS) ENDED", line.upper()) and len(line) < 120: header = line
        parts = [p.strip() for p in line.split("|")]
        lab = re.sub(r"\s*\(\d\)$", "", parts[0])
        if lab in ROWS and len(parts) == 10 and "NORTH AMERICA" in " ".join(lines[max(0, i - 14):i]).upper():
            per = period(header, doc)
            if not per: continue
            vals = [num(c) for c in parts[1:]]
            for col, val in zip(COLS, vals):
                out.append({"period": per, "segment": col, "channel": ROWS[lab], "value_usd_m": f"{val:.0f}", "doc": doc,
                            "printed_page": page - off, "url": man[doc]["url"], "row": line[:150]})
# keep each (period, segment, channel) from the filing that first reported it (earliest filing date)
best = {}
for r in out:
    k = (r["period"], r["segment"], r["channel"])
    filed = r["doc"].split("_")[2]
    if k not in best or filed < best[k]["doc"].split("_")[2]: best[k] = r
rows = sorted(best.values(), key=lambda r: (r["period"], r["segment"], r["channel"]))
with open(OUT, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(len(out), "rows parsed;", len(rows), "kept;", sorted({r["period"] for r in rows}))
