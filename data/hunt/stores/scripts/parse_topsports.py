"""Parse Topsports (6110.HK) operational updates and results texts into tidy CSVs.
Usage: python3 -I parse_topsports.py <hkex_topsports_dir> <out_dir>"""
import re, os, sys, glob, csv
d, out = sys.argv[1], sys.argv[2]
qa, stores = [], []
for t in sorted(glob.glob(os.path.join(d, "*.txt"))):
    title = open(t[:-4] + ".title").read().strip()
    s = re.sub(r"\s+", " ", open(t, errors="ignore").read())
    fid = os.path.basename(t)[:-4]
    if "OPERATIONAL UPDATE" in title.upper():
        m = re.search(r"As at (\d+ \w+ \d{4}), the gross selling area of directly-operated stores (.{0,200}?(?:quarter|year-on-year|year)[^.]*?(?:\d\.\d%[^.]*)?)\.(?= [A-Z])", s)
        g = re.search(r"retail and wholesale operations? registered an? ([\w\- ]+?) (decline|increase|growth)", s)
        pct = re.findall(r"(declined|increased|raised|decreased) by (\d+\.\d)%", m.group(2)) if m else []
        qoq = None
        if m:
            if "largely flat" in m.group(2) and not pct: qoq = 0.0
            elif pct: qoq = float(pct[0][1]) * (-1 if pct[0][0] in ("declined", "decreased") else 1)
            if "largely flat" in m.group(2).split(",")[0]: qoq = 0.0
        yoy = None
        if m:
            y = re.search(r"(declined|increased|decreased|raised)? ?(?:by )?(\d+\.\d)% (?:on a )?year-on-year", m.group(2))
            if y: yoy = float(y.group(2)) * (-1 if (y.group(1) or (pct[0][0] if pct else "")) in ("declined", "decreased") else 1)
        qa.append([fid, title, m.group(1) if m else "", qoq, yoy, m.group(2)[:220] if m else "", (g.group(1) + " " + g.group(2)) if g else ""])
    for m in re.finditer(r"(?:As (?:of|at)|By) (\d+ \w+ \d{4}),? (?:we|the Group)[^.]{0,40}?(\d,\d{3}) directly-? ?(?:operated|managed) stores", s):
        stores.append([fid, title, m.group(1), int(m.group(2).replace(",", ""))])
    for m in re.finditer(r"(?:We|we) directly operated? (\d,\d{3}) stores[^.]{0,120}?as (?:of|at) (\d+ \w+ \d{4})", s):
        stores.append([fid, title, m.group(2), int(m.group(1).replace(",", ""))])
with open(os.path.join(out, "topsports_quarterly_updates.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["hkex_doc", "title", "as_at", "selling_area_qoq_pct", "selling_area_yoy_pct", "selling_area_sentence", "retail_wholesale_sales_yoy_band"]); w.writerows(qa)
seen = {}
for r in stores: seen.setdefault(r[2], r)
with open(os.path.join(out, "topsports_store_counts.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["hkex_doc", "title", "as_at", "directly_operated_stores"]); w.writerows(seen.values())
