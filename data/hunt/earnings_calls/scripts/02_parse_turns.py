"""Split each transcript into speaker turns, tagged prepared remarks vs Q&A, with PDF page.

Usage: python3 -I 02_parse_turns.py <transcripts_dir> <out_csv>
Handles the four label styles Nike used: 'Name, Title:' (FY21-22), '<Q - Name>:' (FY21-22),
'Q: Name' (Q2 FY22), '[NAME]' (FY23 on).
"""
import csv, re, sys, pathlib

CALL_DATES = {
    "Q1FY21": "2020-09-22", "Q2FY21": "2020-12-18", "Q3FY21": "2021-03-18", "Q4FY21": "2021-06-24",
    "Q1FY22": "2021-09-23", "Q2FY22": "2021-12-20", "Q3FY22": "2022-03-21", "Q4FY22": "2022-06-27",
    "Q1FY23": "2022-09-29", "Q2FY23": "2022-12-20", "Q3FY23": "2023-03-21", "Q4FY23": "2023-06-29",
    "Q1FY24": "2023-09-28", "Q2FY24": "2023-12-21", "Q3FY24": "2024-03-21", "Q4FY24": "2024-06-27",
    "Q1FY25": "2024-10-01", "Q2FY25": "2024-12-19", "Q3FY25": "2025-03-20", "Q4FY25": "2025-06-26",
    "Q1FY26": "2025-09-30", "Q2FY26": "2025-12-18", "Q3FY26": "2026-03-31", "Q4FY26": "2026-06-30",
    "Q1FY27": "2026-10-01",
}
MGMT = {"donahoe": "John Donahoe", "friend": "Matt Friend", "hill": "Elliott Hill",
        "denton": "Dave Denton", "parker": "Mark Parker"}
IR = {"muir": "Andy Muir", "trussell": "Paul Trussell"}

def order(q):
    return (int(q[4:]), int(q[1]))

def era(q):
    # Elliott Hill became CEO Oct 14, 2024; Q2 FY25 (Dec 2024) is his first call as CEO.
    return "Hill" if order(q) >= (25, 2) else "Donahoe"

PAT_BRACKET = re.compile(r"^\s*\[([^\]]+)\]\s*(.*)$")
PAT_QA = re.compile(r"^\s*<\s*([QA])\s*[-\u2013]\s*([^>]+?)\s*>\s*:?\s*(.*)$")
PAT_QCOLON = re.compile(r"^\s*([QA]):\s*([A-Z][A-Za-z.'\- ]+?)\s*$")
PAT_OPER = re.compile(r"^\s*Operator\s*[:;]?\s*(.*)$", re.I)
PAT_COLON = re.compile(r"^\s*([A-Z][A-Za-z.'\-]+(?: [A-Z][A-Za-z.'\-]+){1,3})\s*(?:,[^:]{0,100})?[:;]\s*(.*)$")

ALIASES = {"Matthew Friend": "Matt Friend", "Robert Drbul": "Bob Drbul", "Bob Drubul": "Bob Drbul",
           "Aneesha Serman": "Aneesha Sherman", "Brooke Siler Roach": "Brooke Roach",
           "Gabby Carbone": "Gabriella Carbone", "Jon Komp": "Jonathan Komp",
           "Kimberly Greenburger": "Kimberly Greenberger", "Matt Boss": "Matthew Boss",
           "Matthew R. Boss": "Matthew Boss", "Micheal Binetti": "Michael Binetti",
           "Simeon Siegal": "Simeon Siegel", "Indiscernible": "Unidentified Analyst"}

def norm_name(n):
    n = re.sub(r"\s+", " ", n.strip()).title()
    return ALIASES.get(n, n)

def role(name):
    if name.lower() == "operator":
        return "operator"
    last = name.split()[-1].lower()
    if last in MGMT: return "mgmt"
    if last in IR: return "ir"
    return "analyst"

def known_surnames(files):
    s = set(MGMT) | set(IR)
    for f in files:
        for line in f.read_text().splitlines():
            for pat in (PAT_BRACKET, PAT_QA):
                m = pat.match(line)
                if m:
                    nm = m.group(2) if pat is PAT_QA else m.group(1)
                    if "instruction" not in nm.lower():
                        s.add(nm.split()[-1].lower())
            m = re.search(r"(?:line of|question (?:is |comes )?from|from the line of)\s+([A-Z][A-Za-z.'\-]+ [A-Z][A-Za-z.'\-]+)", line)
            if m: s.add(m.group(1).split()[-1].lower())
    return s

def parse(path, surnames):
    q = path.stem
    turns, page, cur = [], 1, None
    def start(name, first):
        nonlocal cur
        cur = {"speaker": norm_name(name), "page": page, "lines": [first] if first else []}
        turns.append(cur)
    for line in path.read_text().splitlines():
        pm = re.match(r"^=== PAGE (\d+) ===$", line)
        if pm:
            page = int(pm.group(1)); continue
        if line.startswith("# NIKE, Inc."):
            continue
        m = PAT_BRACKET.match(line)
        if m and "instruction" not in m.group(1).lower() and len(m.group(1)) < 40 and not m.group(1).strip().isdigit():
            start(m.group(1), m.group(2)); continue
        m = PAT_QA.match(line)
        if m: start(m.group(2), m.group(3)); continue
        m = PAT_QCOLON.match(line)
        if m: start(m.group(2), ""); continue
        m = PAT_OPER.match(line)
        if m and len(line.strip()) < 200 and (line.strip().lower().startswith("operator:") or line.strip().lower().startswith("operator;") or line.strip().lower() == "operator"):
            start("Operator", m.group(1)); continue
        m = PAT_COLON.match(line)
        if m and m.group(1).split()[-1].lower() in surnames and len(m.group(1).split()) <= 3:
            start(m.group(1), m.group(2)); continue
        if cur is not None:
            cur["lines"].append(line)
    rows, in_qa = [], False
    for i, t in enumerate(turns):
        r = role(t["speaker"])
        if r == "analyst" and not in_qa:
            in_qa = True
            if rows and rows[-1]["role"] == "operator":
                rows[-1]["section"] = "qa"
        text = re.sub(r"\s+", " ", " ".join(t["lines"])).strip()
        rows.append({"quarter": q, "call_date": CALL_DATES[q], "era": era(q), "turn": i,
                     "section": "qa" if in_qa else "prepared", "speaker": t["speaker"], "role": r,
                     "page": t["page"], "words": len(text.split()), "text": text})
    return rows

def main(tdir, out):
    files = sorted(pathlib.Path(tdir).glob("Q*FY*.txt"), key=lambda p: order(p.stem))
    sn = known_surnames(files)
    rows = [r for f in files for r in parse(f, sn)]
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)
    print(len(rows), "turns")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
