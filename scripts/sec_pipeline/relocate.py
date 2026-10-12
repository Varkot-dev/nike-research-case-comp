"""For annual/balance facts not cited to the period's own 10-K/10-Q, find the same table row and value in that filing."""
import csv, json, os, re, sys
S = sys.argv[1]; FN = sys.argv[2]
man = {os.path.splitext(m["local"])[0]: m for m in json.load(open(os.path.join(S, "sec/manifest.json")))}
docs = [d for d in man if d.startswith(("10-K", "10-Q"))]
def own_doc(period):
    if re.fullmatch(r"FY\d{4}", period): end = f"{period[2:]}-05-31"; form = "10-K"
    elif re.fullmatch(r"\d{4}-\d{2}-\d{2}", period): end = period; form = None
    elif re.fullmatch(r"Q[123]FY\d{4}", period):
        q, fy = int(period[1]), int(period[4:]); end = {1: f"{fy-1}-08-31", 2: f"{fy-1}-11-30", 3: f"{fy}-02-2"}[q]; form = "10-Q"
    else: return None
    c = [d for d in docs if d.split("_")[1].startswith(end) and (form is None or d.startswith(form))]
    return c[0] if c else None
cache = {}
def pages(doc):
    if doc not in cache:
        t = open(os.path.join(S, "sec/text", doc + ".txt")).read()
        p = re.split(r"^=== PAGE (\d+) \| printed: [^ ]+ ===$", t, flags=re.M)
        cache[doc] = [(int(p[i]), p[i + 1]) for i in range(1, len(p), 2)]
    return cache[doc]
OFF = {}
def offset(doc):
    if doc not in OFF:
        t = open(os.path.join(S, "sec/text", doc + ".txt")).read()
        import collections
        h = re.findall(r"=== PAGE (\d+) \| printed: ([^ ]+) ===", t)
        OFF[doc] = collections.Counter(int(a) - int(b) for a, b in h if b.isdigit()).most_common(1)[0][0]
    return OFF[doc]
def label(doc):
    form, period, filed = doc.split("_")[:3]
    y, m = int(period[:4]), int(period[5:7]); fy = y + 1 if m >= 6 else y; q = {8: 1, 11: 2, 2: 3, 5: 4}[m]
    return f"FY{fy} Form 10-K (filed {filed})" if form == "10-K" else f"Q{q} FY{fy} Form 10-Q (filed {filed})"
rows = list(csv.DictReader(open(FN))); moved = 0
for r in rows:
    od = own_doc(r["period"])
    if not od or label(od) == r["filing"]: continue
    q = r["quote"].strip('"')
    lab = q.split("|")[0].strip()
    if not lab or len(lab) < 4: continue
    try: val = float(r["value"].replace(",", ""))
    except: continue
    vs = {f"{abs(val):,.0f}", f"{abs(val):,.1f}", f"{abs(val):.2f}", f"{abs(val):,.2f}", f"{abs(val):.3f}"}
    hits = []
    for n, body in pages(od):
        for line in body.split("\n"):
            if line.startswith(lab + " |") or line.startswith(lab + "|"):
                cells = [c.strip().strip("()$% ") for c in line.split("|")[1:3]]   # current-year columns come first
                if cells and cells[0] in vs: hits.append((n, line))
    if len({h[0] for h in hits}) >= 1:
        n, line = hits[0]
        r["filing"] = label(od); r["page"] = f"p. {n - offset(od)}"; r["url"] = man[od]["url"]; r["quote"] = line[:160]; moved += 1
with open(FN, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print("re-cited to original filing:", moved)
