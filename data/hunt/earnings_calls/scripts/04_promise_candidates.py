"""Pull every management sentence that pairs a forward-looking verb with a date or period.

Usage: python3 -I 04_promise_candidates.py <turns.csv> <out_csv>
Output is the raw candidate list; promise_tracker.csv is the hand-curated subset with outcomes.
"""
import csv, re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from pagefind import find_page

TIME = re.compile(r"\bby (?:the )?end of\b|\bby (?:fiscal|calendar|holiday|spring|summer|fall|december|the (?:first|second|back|front) half)|"
                  r"\b(?:in|through|into|over|for|beginning in|starting in) (?:fiscal|calendar) ?(?:year )?'?(?:\d\d|20\d\d)\b|"
                  r"\bfiscal ?'?(?:2[2-9]|3[01])\b|\bfiscal (?:year )?20(?:2[2-9]|3[01])\b|\bfy ?'?(?:2[2-9]|3[01])\b|"
                  r"\b(?:first|second|back|front) half\b|\bnext (?:fiscal )?(?:year|quarter|few quarters|several quarters)\b|"
                  r"\b(?:q[1-4]|first quarter|second quarter|third quarter|fourth quarter)\b|\bcalendar year\b|\binvestor day\b|"
                  r"\blong[- ]term (?:financial )?(?:goals?|targets?|outlook|model)\b|\bmultiyear\b", re.I)
FWD = re.compile(r"\b(?:expect\w*|will|plan\w*|on track|target\w*|anticipat\w*|intend\w*|commit\w*|aim\w*|guid\w*|"
                 r"return to|get back to|outlook|forecast\w*|should|believe)\b", re.I)
TOPIC = {
    "revenue_growth": r"\brevenue\w*|\bgrowth\b|\breturn to growth\b|\bgrow\b",
    "gross_margin": r"\bgross margin",
    "ebit_margin": r"\bebit\b|\boperating margin|\bmargins?\b",
    "eps_earnings": r"\bearnings\b|\beps\b|earnings per share",
    "inventory_marketplace": r"\binventor|\bmarketplace\b|\bclean\b|\bliquidat|\bweeks of supply",
    "china": r"\bchina\b",
    "classics": r"\bclassic|\bdunk|\bair force|\bjordan",
    "digital_direct": r"\bdigital\b|\bnike direct\b|\bdirect\b",
    "wholesale": r"\bwholesale\b|\border book|\bpartners?\b",
    "tariff": r"\btariff",
    "cost_program": r"\bsavings\b|\bpace\b|\brestructur|\bcost\b",
    "guidance_policy": r"\bguidance\b|\binvestor day\b",
}
TOPIC = {k: re.compile(v, re.I) for k, v in TOPIC.items()}
SENT = re.compile(r"(?<=[.!?])\s+(?=[A-Z])")

def main(turns_csv, out_csv):
    out = []
    for r in csv.DictReader(open(turns_csv)):
        if r["role"] not in ("mgmt", "ir"):
            continue
        for s in SENT.split(r["text"]):
            if TIME.search(s) and FWD.search(s) and len(s.split()) >= 8:
                topics = [k for k, c in TOPIC.items() if c.search(s)]
                out.append({"quarter": r["quarter"], "call_date": r["call_date"], "era": r["era"],
                            "section": r["section"], "speaker": r["speaker"], "page": find_page(r["quarter"], s.strip()) or r["page"],
                            "topics": ";".join(topics), "sentence": s.strip()})
    with open(out_csv, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
    print(len(out), "candidate sentences")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
