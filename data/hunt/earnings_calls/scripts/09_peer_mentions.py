"""Nike mentions in retailer earnings calls (Motley Fool transcript pages, downloaded 2026-10-14).

Usage: python3 -I 09_peer_mentions.py <peers_dir> [raw_html_dir]
peers_dir holds peer_urls.txt (ticker|period|call_date|url). If raw_html_dir is given, the Motley Fool
HTML pages there are parsed and clean text is written to peers_dir/text/<ticker>_<period>.txt
(one 'Speaker: text' paragraph per line); otherwise those text files are read.
Outputs peers/peer_calls_summary.csv and peers/peer_nike_mentions.csv. The tone column in
peer_nike_mentions.csv is hand-coded (TONE below, keyed by call and sentence start):
+1 = Nike product/brand described as working or a growth driver, -1 = Nike described as a drag,
excess inventory, promotional, or losing share, 0 = neutral listing.
"""
import csv, re, sys, html, pathlib

BRANDS = {"nike": r"\bnike\b", "jordan": r"\bjordan\b", "adidas": r"\badidas\b", "hoka": r"\bhoka\b",
          "new_balance": r"\bnew balance\b", "asics": r"\basics\b", "on_running": r"\bon running\b|\bon and\b|\band on\b|\bon,\s"}

def body(path):
    s = pathlib.Path(path).read_text(encoding="utf-8", errors="ignore")
    i = s.find('id="article-body-transcript"')
    ends = [k for k in (s.find("article-body-promobox", i), s.find("This article is a transcript", i), s.find("<script", i)) if k > 0]
    j = min(ends) if ends else -1
    if i < 0 or j < 0:
        raise SystemExit(f"no transcript body in {path}")
    paras = re.findall(r"<p>(.*?)</p>", s[i:j], flags=re.S)
    out, spk = [], ""
    for p in paras:
        m = re.match(r"\s*<strong>(.*?)</strong>\s*(.*)", p, flags=re.S)
        if m:
            spk = html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip().rstrip(":")
            p = m.group(2)
        t = html.unescape(re.sub(r"<[^>]+>", " ", p))
        t = re.sub(r"\s+", " ", t).replace("\u2014", " - ").replace("\u2013", "-").strip()
        if t:
            out.append((spk, t))
    return out

TONE_LIST = [  # (call, sentence prefix, tone); unlisted sentences are 0
    ("DKS_FY2025Q1", "So yeah, Nike is a very important", 1), ("DKS_FY2025Q1", "And Nike continues to perform", 1),
    ("DKS_FY2025Q1", "So we feel terrific about the Nike", 1), ("DKS_FY2025Q2", "So you see it in the running construct", 1),
    ("DKS_FY2025Q4", "You can see that already in moments", 1), ("DKS_FY2025Q4", "We are seeing great growth", 1),
    ("DKS_FY2025Q4", "If I could just add on to that", 1),
    ("DKS_FY2026Q2", "There are some things out there", 1), ("DKS_FY2026Q2", "The new product that's out there", 1),
    ("DKS_FY2026Q2", "And like I said, some of the products", 1), ("DKS_FY2026Q2", "The running silhouette", 1),
    ("DKS_FY2026Q2", "What we see coming from our friends", 1), ("DKS_FY2026Q2", "And I think how exciting the NBA", 1),
    ("DKS_FY2026Q2", "But as I said, the brands are starting", 1), ("DKS_FY2026Q2", "You can see that with what Nike", 1),
    ("ASO_FY2023Q4", "We saw growth in work apparel", 1), ("ASO_FY2023Q4", "We continue to see outperformance", 1),
    ("ASO_FY2023Q4", "And I think we're -- you're seeing", 1),
    ("ASO_FY2024Q1", "Athletic footwear had the strongest", 1), ("ASO_FY2024Q1", "We continue to see strong results", 1),
    ("ASO_FY2024Q2", "Kids and athletic footwear outperformed", 1), ("ASO_FY2024Q2", "Across both adult and kids", 1),
    ("ASO_FY2024Q2", "We continue to get expanded access", 1),
    ("ASO_FY2024Q3", "Footwear was our second-best", 1), ("ASO_FY2024Q3", "With that in mind, I'm excited", 1),
    ("ASO_FY2024Q4", "Key national brands such as Nike", 1), ("ASO_FY2024Q4", "We're expanding our partnership", 1),
    ("ASO_FY2024Q4", "In addition to Jordan, we're increasing", 1), ("ASO_FY2024Q4", "That will be supported by Jordan", 1),
    ("ASO_FY2024Q4", "So, it's the launch of Jordan", 1), ("ASO_FY2024Q4", "So, I would tell you, our partnership", 1),
    ("ASO_FY2025Q4", "At the same time, we also will continue", 1), ("ASO_FY2025Q4", "Our gross margin gains", 1),
    ("ASO_FY2025Q4", "That is what is moving against", 1), ("ASO_FY2025Q4", "We are very pleased with the relationship", 1),
    ("ASO_FY2025Q4", "We do not have a last year for Jordan", 1), ("ASO_FY2025Q4", "We are going to continue to expand", 1),
    ("ASO_FY2026Q1", "On the athletic side of the business", 1), ("ASO_FY2026Q1", "We also remain encouraged", 1),
    ("ASO_FY2026Q1", "If you look at the combined Nike", 1), ("ASO_FY2026Q1", "We think Nike is a growth engine", 1),
    ("ASO_FY2026Q1", "The growth we are seeing in terms", 1), ("ASO_FY2026Q2", "The team is focused on moving back", 1),
]

def tone_of(call, s):
    for c, pre, t in TONE_LIST:
        if c == call and s.startswith(pre):
            return t
    return 0

def main(pdir, raw=None):
    pdir = pathlib.Path(pdir)
    summ, ment = [], []
    for line in (pdir / "peer_urls.txt").read_text().splitlines():
        tk, per, date, url = line.split("|")
        tpath = pdir / "text" / f"{tk}_{per}.txt"
        if raw:
            paras = body(pathlib.Path(raw) / f"{tk}_{per}.html")
            tpath.parent.mkdir(exist_ok=True)
            tpath.write_text("# Source: " + url + " (Motley Fool transcript page, downloaded 2026-10-14)\n" + "\n".join(f"{a}: {b}" for a, b in paras) + "\n")
        else:
            paras = [tuple(l.split(": ", 1)) if ": " in l else ("", l) for l in tpath.read_text().splitlines()[1:]]
        text = " ".join(t for _, t in paras)
        words = len(text.split())
        row = {"ticker": tk, "period": per, "call_date": date, "source_url": url, "words": words}
        for b, pat in BRANDS.items():
            row[f"{b}_mentions"] = len(re.findall(pat, text, flags=re.I))
        row["nike_per_10k"] = round(row["nike_mentions"] / words * 1e4, 2)
        tones = []
        for spk, t in paras:
            for s in re.split(r"(?<=[.!?])\s+", t):
                if re.search(r"\bnike\b", s, re.I):
                    tone = tone_of(f"{tk}_{per}", s)
                    tones.append(tone)
                    ment.append({"ticker": tk, "period": per, "call_date": date, "speaker": spk,
                                 "speaker_is_analyst": int(bool(re.search(r"analyst", spk, re.I))),
                                 "tone": tone, "sentence": s})
        coded = [x for x in tones if x is not None]
        row["nike_sentences"] = len(tones)
        row["nike_positive"] = sum(1 for x in coded if x > 0)
        row["nike_negative"] = sum(1 for x in coded if x < 0)
        row["nike_net_tone"] = row["nike_positive"] - row["nike_negative"]
        summ.append(row)
    for name, data in (("peer_calls_summary.csv", summ), ("peer_nike_mentions.csv", ment)):
        with open(pdir / name, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(data[0])); w.writeheader(); w.writerows(data)
    print(len(summ), "calls,", len(ment), "Nike sentences")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
