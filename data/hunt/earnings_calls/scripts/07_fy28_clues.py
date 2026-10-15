"""Every sentence (management or analyst) that refers to fiscal 2028 or later, the long-term algorithm,
double-digit margins, or the Investor Day, from Q3 FY24 onward.

Usage: python3 -I 07_fy28_clues.py <turns.csv> <out_csv>
"""
import csv, re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from pagefind import find_page

PAT = re.compile(r"fiscal\s*(?:year\s*)?'?\s*(?:28|29|30|31)\b|fiscal (?:year )?20(?:28|29|30|31)|\bfy\s*'?(?:28|29|30)\b|'(?:28|29|30)\b|"
                 r"algorithm|double[- ]digit (?:ebit |operating )?margins?|long[- ]term (?:growth|guidance|view|financial|objectives|targets?)|"
                 r"investor day|next 5 years|5-year|five[- ]year|normal year|first .normal.", re.I)

def order(q): return (int(q[4:]), int(q[1]))

def main(turns_csv, out_csv):
    out = []
    for r in csv.DictReader(open(turns_csv)):
        if order(r["quarter"]) < (24, 3) or r["role"] == "operator":
            continue
        for s in re.split(r"(?<=[.!?])\s+(?=[A-Z\"])", r["text"]):
            if PAT.search(s):
                out.append({"quarter": r["quarter"], "call_date": r["call_date"], "section": r["section"],
                            "speaker": r["speaker"], "role": r["role"], "page": find_page(r["quarter"], s) or r["page"],
                            "match": "; ".join(sorted(set(m.lower() for m in PAT.findall(s)))), "sentence": s.strip()})
    with open(out_csv, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
    print(len(out), "FY28 and long-term sentences")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
