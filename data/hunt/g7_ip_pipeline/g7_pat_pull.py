"""Pull US patent grants (USPAT: utility B1/B2, design S) and published applications (US-PGPUB A1) for Nike and peers
from USPTO Patent Public Search (ppubs.uspto.gov anonymous JSON API). Pub years 2012..2026 YTD.
Outputs pat_raw_<co>.jsonl and pat_fwcpc_<co>.json (guids with footwear CPC A43B/A43C).
No credentials, no email, no API key."""
import json, re, sys, threading
sys.path.insert(0, ".")
from pplib import *
CO = {
 "Nike":       ("nike.asn.",                         r"nike"),
 "adidas":     ("adidas.asn.",                       r"adidas"),
 "On":         ('("on clouds" OR "on holding" OR "on ag").asn.', r"\bon (clouds|holding|ag)"),
 "Deckers":    ("(deckers OR hoka).asn.",            r"deckers|hoka"),
 "NewBalance": ("(new AND balance).asn.",            r"new balance"),
 "ASICS":      ("asics.asn.",                        r"asics"),
 "Puma":       ("puma.asn.",                         r"\bpuma\b"),
 "Lululemon":  ("lululemon.asn.",                    r"lululemon"),
}
def run(co):
    qa, rx = CO[co]
    p = PP(); rows = []; fw = set()
    for y in range(2012, 2027):
        Y = f'@PD>="{y}0101"<="{y}1231"'
        for q, tag in [(f"{qa} AND {Y}", "all"), (f"{qa} AND (A43B* OR A43C*).cpc. AND {Y}", "fw")]:
            st = 0
            while True:
                d = full(p, q, start=st, page=100)
                for r in d["patents"]:
                    if tag == "fw": fw.add(r["guid"]); continue
                    names = (r.get("assigneeName") or []) + (r.get("applicantName") or [])
                    if not any(re.search(rx, n.lower()) for n in names): continue
                    rows.append({"guid": r["guid"], "pub": r["datePublished"][:10], "title": r["inventionTitle"],
                                 "main": r["mainClassificationCode"], "filed": (r.get("applicationFilingDate") or [None])[0],
                                 "asg": r.get("assigneeName"), "app": r.get("applicantName"), "type": r["type"]})
                st += 100
                if st >= d["numFound"] or not d["patents"]: break
        print(co, y, len(rows), flush=True)
    with open(f"pat_raw_{co}.jsonl", "w") as f:
        for r in rows: f.write(json.dumps(r) + "\n")
    json.dump(sorted(fw), open(f"pat_fwcpc_{co}.json", "w"))
ts = [threading.Thread(target=run, args=(c,)) for c in CO]
[t.start() for t in ts]; [t.join() for t in ts]
print("DONE")
