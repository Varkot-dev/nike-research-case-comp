"""Analyst Q&A: topics per question slot, who asked, answer length, numeric specificity, deflections.

Usage: python3 -I 06_qa_analysis.py <turns.csv> <out_dir>
A 'slot' runs from one operator hand-off to the next: all analyst text in it is the question,
all management text is the answer. Pleasantry turns under 12 words are ignored.
Quantitative tokens are counted after removing time references (fiscal '27, Q2, 2026 ...).
"""
import csv, re, sys, pathlib
from collections import defaultdict
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from pagefind import find_page

TOPICS = {
    "margins_profitability": r"gross margin|\bmargins?\b|profitab|\bebit\b|sg&a|\bcosts?\b|\beps\b|earnings",
    "outlook_guidance": r"guid|outlook|algorithm|next year|fiscal ?'?\d\d|second half|back half|first half|cadence|long[- ]term",
    "recovery_timing": r"when (?:do|will|can|should|could|would)|how long|time ?line|inning|bottom|inflect|trough|normal year|return to growth|back to growth|path to|turn(?:around)?\b",
    "china": r"china|chinese",
    "inventory_marketplace_discount": r"inventor|markdown|promot|discount|clean|liquidat|marketplace|off-price|full[- ]price",
    "wholesale_partners_orderbook": r"wholesale|partners?\b|order ?book|foot locker|dick|sell-in|sell-through|sell through",
    "direct_digital": r"digital|nike direct|\bdirect\b|\bapp\b|snkrs|traffic",
    "product_innovation_franchises": r"innovation|product|franchise|dunk|jordan|air force|classic|running|newness|pipeline|sportswear|basketball|football",
    "tariff_macro_fx": r"tariff|macro|consumer|\bfx\b|currency|inflation|freight",
    "capital_allocation": r"buyback|repurchase|dividend|capital allocation|cash",
    "competition_share": r"competit|market share|\bshare\b|hoka|adidas|\bon\b running|new entrants",
    "org_cost_program": r"restructur|layoff|organization|leadership|\bpace\b|savings|workforce|operating model",
}
TOPICS = {k: re.compile(v, re.I) for k, v in TOPICS.items()}
TIME = re.compile(r"fiscal (?:year )?'?\s?\d{2,4}|\bfy ?'?\d\d\b|\bq[1-4]\b|\b20\d\d\b|'\d\d\b|\b\d{1,2}(?:st|nd|rd|th)\b|\b(?:19|20)\d\d\b", re.I)
QUANT = re.compile(r"\d+(?:\.\d+)?|\b(?:low|mid|high)[- ]?(?:to[- ](?:low|mid|high)[- ]?)?(?:single|double)[- ]digits?\b|\b(?:low|mid|high)[- ]teens\b|\bbasis points?\b|\bpercent\b|\bbillion\b|\bmillion\b|\bflattish\b", re.I)
ASKS_NUM = re.compile(r"how much|quantif|magnitude|\bsize\b|sizing|what percent|how big|range|cadence|basis points|\bbps\b|margin|guid|how should we think|\d|frame|framework|shape", re.I)
DEFLECT = re.compile(r"not going to (?:give|provide|guide|get into|break|comment)|(?:don't|do not|won't|will not) (?:guide|give guidance|provide guidance|break out|get into)|"
                     r"\b(?:share|talk|provide|discuss|outline|dive|come back)\b[^.]{0,80}(?:investor day|in november)|"
                     r"at (?:our )?investor day|hold that question|too early to|not (?:in a position|ready) to|probably not going to provide", re.I)

def order(q): return (int(q[4:]), int(q[1]))

def main(turns_csv, out_dir):
    out_dir = pathlib.Path(out_dir)
    rows = [r for r in csv.DictReader(open(turns_csv)) if r["section"] == "qa"]
    slots, cur = [], None
    for r in rows:
        if r["role"] == "operator":
            cur = None; continue
        if cur is None or (r["role"] == "analyst" and cur["answers"] and r["speaker"] != cur["analyst"]):
            cur = {"quarter": r["quarter"], "era": r["era"], "analyst": None, "q": [], "answers": [],
                   "answerers": [], "page": r["page"]}
            slots.append(cur)
        if r["role"] == "analyst":
            cur["analyst"] = cur["analyst"] or r["speaker"]
            if int(r["words"]) >= 12: cur["q"].append(r["text"])
        elif r["role"] in ("mgmt", "ir"):
            cur["answers"].append(r["text"]); cur["answerers"].append(r["speaker"])
    out = []
    for s in slots:
        if not s["analyst"] or not s["q"]:
            continue
        qt, at = " ".join(s["q"]), " ".join(s["answers"])
        at_nt = TIME.sub(" ", at)
        aw = len(at.split()); qn = len(QUANT.findall(at_nt))
        topics = [k for k, c in TOPICS.items() if c.search(qt)]
        defl = DEFLECT.findall(at)
        out.append({"quarter": s["quarter"], "era": s["era"], "analyst": s["analyst"],
                    "page": find_page(s["quarter"], s["q"][0]) or s["page"],
                    "question_words": len(qt.split()), "topics": ";".join(topics),
                    "asks_for_numbers": int(bool(ASKS_NUM.search(qt))),
                    "answer_words": aw, "answer_quant_tokens": qn,
                    "quant_per_100_words": round(qn / aw * 100, 2) if aw else 0,
                    "answer_has_numbers": int(qn > 0), "deflection": int(bool(defl)),
                    "deflection_text": " | ".join(defl)[:200],
                    "answerers": ";".join(dict.fromkeys(s["answerers"])),
                    "question_text": qt[:600]})
    with open(out_dir / "qa_pairs.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
    # Topic share by quarter
    agg = defaultdict(lambda: defaultdict(int)); nq = defaultdict(int)
    for o in out:
        nq[o["quarter"]] += 1
        for t in o["topics"].split(";"):
            if t: agg[o["quarter"]][t] += 1
    trows = []
    for q in sorted(nq, key=order):
        for t in TOPICS:
            trows.append({"quarter": q, "n_questions": nq[q], "topic": t, "n_asking": agg[q][t],
                          "share": round(agg[q][t] / nq[q], 2)})
    with open(out_dir / "qa_topics_by_quarter.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(trows[0])); w.writeheader(); w.writerows(trows)
    print(len(out), "question slots")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
