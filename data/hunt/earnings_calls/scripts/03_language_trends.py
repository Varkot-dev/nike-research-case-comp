"""Term frequency per 10,000 words by quarter and section.

Usage: python3 -I 03_language_trends.py <turns.csv> <out_dir>
Sections: prepared (management + IR prepared remarks), qa_answer (management answers),
qa_question (analyst questions), mgmt_all, ceo_only (Donahoe or Hill), cfo_only (Friend or Denton).
The CEO/CFO split tests whether a trend is just one speaker's vocabulary. Operator text is excluded.
Robustness: hedges and recovery words are also counted after dropping every sentence that
mentions tariffs, and a leave-one-term-out net index is computed.
"""
import csv, re, sys, pathlib
from collections import defaultdict

TERMS = {
    "discount_promo": r"\bdiscount\w*|\bpromotion\w*|\bpromotional\w*|\bmarkdown\w*|\bliquidat\w*|\bclearance\b|\bcloseout\w*",
    "full_price": r"\bfull[- ]price\b",
    "clean_healthy_marketplace": r"\b(?:clean|cleaner|healthy|healthier)\s+(?:the\s+|a\s+)?marketplace|\bmarketplace\s+(?:health|is (?:clean|healthy))|\bclean(?:ing)?\s+up\s+(?:the\s+)?marketplace|\bhealthy\s+(?:inventory|marketplace)",
    "inventory": r"\binventor(?:y|ies)\b",
    "china": r"\bchina\b|\bchinese\b",
    "jordan": r"\bjordan\b",
    "classics_franchises": r"\bdunks?\b|\bair force 1\b|\baf1\b|\bclassics?\b|\bpanda\b|\blifestyle franchises\b|\bkey franchises\b|\bicons?\b|\bretro\b",
    "sportswear": r"\bsportswear\b",
    "running": r"\brunning\b|\bpegasus\b|\bvomero\b|\bvaporfly\b|\balphafly\b",
    "wholesale_partners": r"\bwholesale\b|\bpartners?\b|\bfoot locker\b|\bdick'?s\b|\bjd\b",
    "direct_digital": r"\bdigital\b|\bnike direct\b|\bsnkrs\b",
    "tariff": r"\btariffs?\b",
    "fy28_beyond": r"\bfiscal\s*'?\s*(?:28|29|30)\b|\bfiscal (?:year )?20(?:28|29|30)\b|\bfy\s*'?(?:28|29|30)\b",
    "growth": r"\bgrowth\b|\bgrow(?:s|ing|n)?\b",
    "recovery": r"\brecover\w*|\bcomeback\b|\bturnaround\b|\bturn around\b|\bmomentum\b|\breturn(?:ing)? to growth\b|\binflect\w*|\bstabiliz\w*|\bimprov\w*",
    "recovery_ex_improve": r"\brecover\w*|\bcomeback\b|\bturnaround\b|\bturn around\b|\bmomentum\b|\breturn(?:ing)? to growth\b|\binflect\w*|\bstabiliz\w*",
    "hedge_headwind": r"\bheadwinds?\b",
    "hedge_challenging": r"\bchalleng\w*|\bdifficult\w*|\btough\b",
    "hedge_uncertainty": r"\buncertain\w*|\bvolatil\w*|\bdynamic environment\b",
    "hedge_pressure": r"\bpressur\w*",
    "confident": r"\bconfident\b|\bconfidence\b",
    "not_yet": r"\bnot (?:there|where we want) yet\b|\bnot yet\b|\bmore work to do\b|\bwork to do\b",
}
HEDGES = ["hedge_headwind", "hedge_challenging", "hedge_uncertainty", "hedge_pressure"]
UPBEAT = ["recovery", "confident"]
COMP = {k: re.compile(v, re.I) for k, v in TERMS.items()}
SENT = re.compile(r"(?<=[.!?])\s+")

def order(q): return (int(q[4:]), int(q[1]))

def main(turns_csv, out_dir):
    out_dir = pathlib.Path(out_dir)
    text = defaultdict(list)
    era = {}
    for r in csv.DictReader(open(turns_csv)):
        era[r["quarter"]] = r["era"]
        if r["role"] in ("mgmt", "ir"):
            sec = "prepared" if r["section"] == "prepared" else "qa_answer"
        elif r["role"] == "analyst":
            sec = "qa_question"
        else:
            continue
        text[(r["quarter"], sec)].append(r["text"])
        if sec != "qa_question":
            text[(r["quarter"], "mgmt_all")].append(r["text"])
        if r["speaker"] in ("John Donahoe", "Elliott Hill"):
            text[(r["quarter"], "ceo_only")].append(r["text"])
        if r["speaker"] in ("Matt Friend", "Dave Denton"):
            text[(r["quarter"], "cfo_only")].append(r["text"])
    rows = []
    for (q, sec), parts in text.items():
        t = " ".join(parts)
        words = len(t.split())
        no_tariff = " ".join(s for s in SENT.split(t) if not re.search(r"tariff", s, re.I))
        words_nt = len(no_tariff.split())
        for k, c in COMP.items():
            n = len(c.findall(t))
            n_nt = len(c.findall(no_tariff))
            rows.append({"quarter": q, "era": era[q], "section": sec, "words": words, "term": k,
                         "count": n, "per10k": round(n / words * 1e4, 2),
                         "count_excl_tariff_sentences": n_nt,
                         "per10k_excl_tariff_sentences": round(n_nt / max(words_nt, 1) * 1e4, 2)})
    rows.sort(key=lambda r: (order(r["quarter"]), r["section"], r["term"]))
    with open(out_dir / "language_trends.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    # Net tone index per quarter and section: (recovery + confident) minus hedges, per 10k words
    idx = defaultdict(dict)
    for r in rows:
        idx[(r["quarter"], r["section"])][r["term"]] = r
    out = []
    for (q, sec), d in sorted(idx.items(), key=lambda x: (order(x[0][0]), x[0][1])):
        up = sum(d[k]["per10k"] for k in UPBEAT); hd = sum(d[k]["per10k"] for k in HEDGES)
        up_nt = sum(d[k]["per10k_excl_tariff_sentences"] for k in UPBEAT)
        hd_nt = sum(d[k]["per10k_excl_tariff_sentences"] for k in HEDGES)
        loo = {f"net_wo_{k}": round(up - hd - (d[k]["per10k"] if k in UPBEAT else -d[k]["per10k"]), 1)
               for k in UPBEAT + HEDGES}
        out.append({"quarter": q, "era": era[q], "section": sec, "upbeat_per10k": round(up, 1),
                    "hedge_per10k": round(hd, 1), "net_tone": round(up - hd, 1),
                    "net_tone_excl_tariff_sentences": round(up_nt - hd_nt, 1), **loo})
    with open(out_dir / "tone_index.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
    print(len(rows), "term rows;", len(out), "tone rows")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
