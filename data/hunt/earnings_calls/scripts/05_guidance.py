"""Guidance specificity by call and next-quarter guidance vs actual.

Usage: python3 -I 05_guidance.py <turns.csv> <nike_filing_facts.csv> <out_dir>

1) guidance_specificity.csv: hand-coded from the CFO outlook section of each call (read in full).
   Scale per field: 3 = numeric (%, bps, $ or numeric range), 2 = size bucket (low single digits,
   flat, mid-teens), 1 = direction only (up, down, pressure), 0 = not given.
   nq_* = next quarter, fy_* = full fiscal year (or the multi-quarter window Nike gave instead in
   Q3 FY26 and Q4 FY26), seg_items = count of forward geography, channel or category items (capped at 3),
   multi_year = 2 full multi-year algorithm, 1 a partial multi-year number or promise, 0 none.
   Also computed automatically: numeric tokens in CFO prepared sentences that contain 'expect'.
2) guidance_scorecard.csv: next-quarter revenue growth and gross margin change guides, mapped to
   numeric ranges (bucket mapping in BUCKETS below), against reported actuals from the facts CSV.
   Each guide quote is checked against the transcript text (raises if not found).
"""
import csv, re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from pagefind import find_page

F = ["nq_rev", "nq_gm", "nq_sga", "nq_oie_tax", "fy_rev", "fy_gm", "fy_sga", "fy_eps", "fy_oie_tax", "seg_items", "multi_year"]
SPEC = {  # quarter: values in F order
    "Q1FY21": [0, 1, 0, 0, 2, 2, 3, 0, 0, 0, 0], "Q2FY21": [0, 2, 0, 0, 2, 3, 2, 0, 2, 0, 0],
    "Q3FY21": [3, 0, 0, 0, 2, 3, 1, 0, 2, 0, 0], "Q4FY21": [1, 0, 0, 0, 3, 3, 1, 0, 2, 3, 2],
    "Q1FY22": [2, 1, 0, 0, 2, 3, 2, 0, 0, 1, 1], "Q2FY22": [2, 0, 0, 0, 2, 3, 2, 0, 2, 0, 1],
    "Q3FY22": [1, 0, 0, 0, 2, 3, 2, 0, 2, 2, 1], "Q4FY22": [2, 3, 0, 0, 2, 3, 2, 0, 2, 1, 0],
    "Q1FY23": [2, 3, 0, 0, 2, 3, 2, 0, 2, 0, 1], "Q2FY23": [1, 2, 2, 0, 2, 3, 2, 0, 2, 0, 0],
    "Q3FY23": [2, 0, 0, 0, 2, 3, 3, 0, 2, 1, 0], "Q4FY23": [2, 3, 2, 0, 2, 3, 1, 0, 3, 1, 0],
    "Q1FY24": [1, 3, 2, 2, 2, 3, 2, 0, 3, 0, 0], "Q2FY24": [1, 3, 1, 0, 3, 3, 3, 1, 3, 1, 0],
    "Q3FY24": [1, 3, 1, 0, 3, 3, 2, 1, 2, 0, 1], "Q4FY24": [3, 2, 2, 0, 2, 3, 1, 0, 3, 1, 1],
    "Q1FY25": [3, 3, 2, 3, 1, 1, 0, 0, 0, 2, 0], "Q2FY25": [2, 3, 1, 3, 0, 0, 0, 0, 0, 1, 0],
    "Q3FY25": [2, 3, 2, 3, 0, 0, 0, 0, 2, 3, 0], "Q4FY25": [2, 3, 2, 3, 0, 3, 2, 0, 3, 3, 0],
    "Q1FY26": [2, 3, 2, 3, 1, 3, 2, 0, 2, 3, 0], "Q2FY26": [2, 3, 2, 3, 0, 0, 0, 0, 0, 2, 0],
    "Q3FY26": [3, 3, 2, 3, 2, 1, 0, 1, 2, 3, 1], "Q4FY26": [2, 2, 2, 0, 2, 1, 0, 1, 2, 1, 0],
    "Q1FY27": [1, 0, 0, 0, 2, 1, 1, 3, 0, 1, 1],
}
# Next-quarter guides: (call, target quarter, metric, low, high, quote that must exist in the call)
BUCKETS = "flat=0; slightly=0 to 2; low single digits=1 to 3; mid single digits=4 to 6; low double digits=10 to 13 (or -13 to -10)"
GUIDES = [
    ("Q4FY22", "Q1FY2023", "rev", 0, 2, "we expect real-dollar Revenue growth to be flat to slightly up"),
    ("Q4FY22", "Q1FY2023", "gm", -400, -100, "We expect gross margin pressure to exceed 100 basis points in the first quarter"),
    ("Q1FY23", "Q2FY2023", "rev", 10, 13, "For the second quarter specifically, we expect reported revenue to grow low double-digits"),
    ("Q1FY23", "Q2FY2023", "gm", -400, -350, "We expect second quarter gross margins to decline approximately 350 to 400 basis points"),
    ("Q2FY23", "Q3FY2023", "gm", -350, -250, "We expect the third quarter gross margin will decline at a similar rate as the second quarter"),
    ("Q3FY23", "Q4FY2023", "rev", 0, 3, "For the fourth quarter, this translates into flat to low single-digit revenue growth"),
    ("Q4FY23", "Q1FY2024", "rev", 0, 3, "We expect first-quarter revenue growth to be flat to up low single-digits"),
    ("Q4FY23", "Q1FY2024", "gm", -75, -50, "down 50-75 basis points on a reported basis"),
    ("Q1FY24", "Q2FY2024", "rev", 0, 2, "We expect second quarter reported revenue growth to be up slightly versus the prior year"),
    ("Q1FY24", "Q2FY2024", "gm", 75, 125, "We expect second-quarter gross margins to expand approximately 100 basis points"),
    ("Q2FY24", "Q3FY2024", "rev", -2, 0, "we expect Q3 reported revenue to be slightly negative"),
    ("Q2FY24", "Q3FY2024", "gm", 160, 180, "with Q3 margins expanding 160 to 180 basis points"),
    ("Q3FY24", "Q4FY2024", "rev", 0, 2, "We now expect Q4 revenue to be up slightly"),
    ("Q3FY24", "Q4FY2024", "gm", 160, 180, "We expect Q4 gross margins to expand approximately 160-180 basis points"),
    ("Q4FY24", "Q1FY2025", "rev", -11, -9, "We expect first-quarter revenue to be down approximately 10%"),
    ("Q4FY24", "Q1FY2025", "gm", 10, 30, "We expect first-quarter gross margins to be in line with the full year guidance"),
    ("Q1FY25", "Q2FY2025", "rev", -10, -8, "We expect Q2 revenues to be down in the 8% to 10% range"),
    ("Q1FY25", "Q2FY2025", "gm", -175, -125, "We expect Q2 gross margins to be down approximately 150 basis points"),
    ("Q2FY25", "Q3FY2025", "rev", -13, -10, "We expect Q3 revenues to be down low double digits"),
    ("Q2FY25", "Q3FY2025", "gm", -350, -300, "We expect Q3 gross margins to be down approximately 300 to 350 basis points"),
    ("Q3FY25", "Q4FY2025", "rev", -15, -13, "We expect Q4 revenues to be down in the mid-teens range, albeit at the low end"),
    ("Q3FY25", "Q4FY2025", "gm", -500, -400, "We expect Q4 gross margins to be down approximately 400-500 basis points"),
    ("Q4FY25", "Q1FY2026", "rev", -6, -4, "We expect Q1 revenues to be down mid-single digits"),
    ("Q4FY25", "Q1FY2026", "gm", -425, -350, "We expect Q1 gross margins to be down approximately 350 to 425 basis points"),
    ("Q1FY26", "Q2FY2026", "rev", -3, -1, "We expect Q2 revenues to be down low single digits"),
    ("Q1FY26", "Q2FY2026", "gm", -375, -300, "We expect Q2 gross margins to be down approximately 300 to 375 basis points"),
    ("Q2FY26", "Q3FY2026", "rev", -3, -1, "We expect Q3 revenues to be down low single digits"),
    ("Q2FY26", "Q3FY2026", "gm", -225, -175, "We expect Q3 gross margins to be down approximately 175 to 225 basis points"),
    ("Q3FY26", "Q4FY2026", "rev", -4, -2, "We expect revenues in Q4 to be down 2% to 4%"),
    ("Q3FY26", "Q4FY2026", "gm", -75, -25, "with Q4 down approximately 25 to 75 basis points"),
    ("Q4FY26", "Q1FY2027", "rev", -6, -1, "we expect reported revenues to be down low to mid-single digits"),
    ("Q4FY26", "Q1FY2027", "gm", 0, 50, "We expect gross margin in Q1 to be slightly positive"),
]
# Q4 FY26 reported gross margin includes a 900 bp IEEPA tariff refund (Q4 FY26 call p. 8); the
# guide excluded it, so the scorecard uses the ex-refund change management reported (-10 bp, Q4 FY26 call p. 22).
GM_OVERRIDE = {"Q4FY2026": (-10, "ex IEEPA refund, as stated on Q4 FY26 call p. 22")}

def era(call): return "Hill" if (int(call[4:]), int(call[1])) >= (25, 2) else "Donahoe"

def prior(q):  # Q1FY2027 -> Q1FY2026
    return q[:4] + str(int(q[4:]) - 1)

def main(turns_csv, facts_csv, out_dir):
    out_dir = pathlib.Path(out_dir)
    facts = {}
    for r in csv.DictReader(open(facts_csv)):
        if r["metric"] in ("revenues", "gross_margin_pct") and (r["metric"], r["period"]) not in facts:
            facts[(r["metric"], r["period"])] = (float(r["value"]), f'{r["filing"].split("(")[0].strip()} {r["page"]}')
    # automated count
    auto = {}
    num = re.compile(r"\d+(?:\.\d+)?\s*(?:%|percent|basis points|billion|million)|\$\s?\d|\b(?:low|mid|high)[- ](?:to[- ](?:low|mid|high)[- ])?(?:single|double)[- ]digits?|\b(?:low|mid|high)[- ]teens|\bflat(?:tish)?\b", re.I)
    for r in csv.DictReader(open(turns_csv)):
        if r["section"] == "prepared" and r["speaker"] in ("Matt Friend", "Dave Denton"):
            for s in re.split(r"(?<=[.!?])\s+", r["text"]):
                if re.search(r"\bexpect", s, re.I):
                    a = auto.setdefault(r["quarter"], [0, 0])
                    a[0] += 1; a[1] += len(num.findall(s))
    rows = []
    for q, v in SPEC.items():
        d = dict(zip(F, v))
        score = sum(d[k] for k in F[:9]) + min(d["seg_items"], 3) + d["multi_year"]
        rows.append({"quarter": q, "era": era(q), **d, "spec_score": score,
                     "n_numeric_fields": sum(1 for k in F[:9] if d[k] == 3),
                     "next_quarter_fields_given": sum(1 for k in F[:4] if d[k] > 0),
                     "auto_expect_sentences": auto.get(q, [0, 0])[0],
                     "auto_quant_tokens_in_expect_sentences": auto.get(q, [0, 0])[1]})
    with open(out_dir / "guidance_specificity.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    sc = []
    for call, tq, m, lo, hi, quote in GUIDES:
        pg = find_page(call, quote)
        if pg is None:
            raise SystemExit(f"quote not found in {call}: {quote}")
        if m == "rev":
            a, src = facts[("revenues", tq)]; b, _ = facts[("revenues", prior(tq))]
            act = round((a / b - 1) * 100, 1); src = f"{src}; prior year {prior(tq)}"
        else:
            if tq in GM_OVERRIDE:
                act, src = GM_OVERRIDE[tq]
            else:
                a, src = facts[("gross_margin_pct", tq)]; b, _ = facts[("gross_margin_pct", prior(tq))]
                act = round((a - b) * 100); src = f"{src}; prior year {prior(tq)}"
        res = "beat" if act > hi else ("miss" if act < lo else "in range")
        sc.append({"call": call, "era": era(call), "target_quarter": tq, "metric": "revenue_growth_pct" if m == "rev" else "gross_margin_change_bps",
                   "guide_low": lo, "guide_high": hi, "actual": act, "result": res,
                   "distance_from_midpoint": round(act - (lo + hi) / 2, 1),
                   "guide_quote": quote, "guide_page": pg, "actual_source": src})
    with open(out_dir / "guidance_scorecard.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(sc[0])); w.writeheader(); w.writerows(sc)
    print(len(rows), "specificity rows;", len(sc), "scorecard rows")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
