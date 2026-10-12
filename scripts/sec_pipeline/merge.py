"""Merge agent CSV extracts; verify each value appears on the cited sequential page of the cited document."""
import csv, glob, io, json, os, re, sys
S = sys.argv[1]
TEXT = os.path.join(S, "sec/text")
man = {os.path.splitext(m["local"])[0]: m for m in json.load(open(os.path.join(S, "sec/manifest.json")))}
pages = {}
def page(doc, n):
    if doc not in pages:
        t = open(os.path.join(TEXT, doc + ".txt")).read()
        parts = re.split(r"^=== PAGE (\d+) \| printed: ([^ ]+) ===$", t, flags=re.M)
        pages[doc] = {int(parts[i]): (parts[i + 1], parts[i + 2]) for i in range(1, len(parts), 3)}
    return pages[doc].get(n)
def norm_num(v):
    v = v.strip().replace(",", "")
    try: return float(v)
    except: return None
def forms(x):
    out = set()
    if x is None: return out
    a = abs(x)
    for s in (f"{a:,.0f}", f"{a:.0f}", f"{a:,.1f}", f"{a:.1f}", f"{a:.2f}", f"{a:,.2f}", f"{a:.3f}", f"{a:g}", f"{a:,}"):
        out.add(s)
    if a < 1: out |= {f"{a:.2f}".lstrip("0"), f"{a:.3f}".lstrip("0")}
    return out
rows, bad = [], []
for fn in sorted(glob.glob(os.path.join(S, "extract/[A-I]_*.md"))):
    txt = open(fn).read()
    blocks = re.findall(r"```csv\n(.*?)```", txt, flags=re.S)
    if not blocks:
        m = re.search(r"^metric,period,value.*?$(.*?)(?=^#|^```|\Z)", txt, flags=re.S | re.M)
        blocks = [m.group(0)] if m else []
    for block in blocks:
        for r in csv.DictReader(io.StringIO(block)):
            if not r.get("metric") or r["metric"] == "metric": continue
            r["src"] = os.path.basename(fn)[0]
            doc = (r.get("doc") or "").strip()
            try: sp = int(str(r.get("seq_page", "")).strip())
            except: sp = None
            pg = page(doc, sp) if doc in man and sp else None
            val = norm_num(r.get("value", "") or "")
            ok = "nodoc" if doc not in man else "nopage" if not pg else "text"
            if pg and val is not None:
                body = pg[1]
                ok = "OK" if any(re.search(r"(?<![\d.])" + re.escape(f) + r"(?![\d])", body) for f in forms(val)) else "VALUE_NOT_ON_PAGE"
                r["printed_detected"] = pg[0]
            r["check"] = ok
            r["url"] = man.get(doc, {}).get("url", "")
            rows.append(r)
cols = ["metric", "period", "value", "unit", "doc", "seq_page", "printed_page", "printed_detected", "quote", "check", "src", "url"]
with open(os.path.join(S, "extract/master.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore"); w.writeheader(); w.writerows(rows)
from collections import Counter
print(len(rows), Counter(r["check"] for r in rows))
print(Counter((r["src"], r["check"]) for r in rows))
