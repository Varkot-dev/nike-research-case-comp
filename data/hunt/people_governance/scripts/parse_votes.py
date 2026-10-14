"""Parse Nike annual meeting 8-K (Item 5.07) texts into tidy vote tables.
Class A is held about 77% to 79% by Swoosh LLC (Knight family), which always votes For,
so Class B-only support for say-on-pay = (For - ClassA votes) / (For - ClassA + Against).
Usage: python3 -I parse_votes.py OUTDIR"""
import sys, os, re, glob, csv
OUT = sys.argv[1]
num = r'([\d,]{5,})'
dirs, sop = [], []
for f in sorted(glob.glob(os.path.join(OUT, 'raw/nke_8k/*.txt'))):
    if '2016-10-14' in f: continue  # 8-K/A repeating the 2016 results
    t = open(f).read()
    if 'Election of Directors' not in t or 'Executive Compensation' not in t: continue
    flat = re.sub(r'[\s|]+', ' ', t).replace('\u2014', '0').replace('\u2013', '0')
    date = os.path.basename(f)[:10]
    a0 = flat.find('Class A Common Stock:'); b0 = flat.find('Class B Common Stock:', a0 + 1); p2 = flat.find('Proposal 2', b0)
    classA = 0
    for sec, cls in ((flat[a0:b0], 'A'), (flat[b0:p2], 'B')):
        for m in re.finditer(r'([A-Z][A-Za-zÀ-ÿ\.\' ,-]+?) ' + num + r' ([\d,]+) ([\d,]+)', sec):
            name = m.group(1).replace('Votes Cast For Votes Withheld Broker Non-Votes', '').strip()
            fo, wi, bn = (int(m.group(i).replace(',', '')) for i in (2, 3, 4))
            if cls == 'A': classA = max(classA, fo + wi)
            dirs.append(dict(meeting_8k_filed=date, director=name, elected_by='Class ' + cls, votes_for=fo, withheld=wi, broker_nonvotes=bn, withhold_pct=round(wi / (fo + wi) * 100, 1)))
    s = flat.find('Advisory Vote on Executive Compensation')
    m = re.search(num + ' ' + num + ' ' + num + ' ' + num, flat[s:s + 600])
    fo, ag, ab, bn = (int(m.group(i).replace(',', '')) for i in (1, 2, 3, 4))
    sop.append(dict(meeting_8k_filed=date, sop_for=fo, sop_against=ag, sop_abstain=ab, broker_nonvotes=bn, classA_votes=classA,
                    support_pct_all=round(fo / (fo + ag) * 100, 1),
                    support_pct_classB_only=(round((fo - classA) / (fo - classA + ag) * 100, 1) if classA else None)))
for name, rows in (('nke_say_on_pay_2015_2026.csv', sop), ('nke_director_votes_2015_2026.csv', dirs)):
    w = csv.DictWriter(open(os.path.join(OUT, name), 'w', newline=''), fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
for r in sop: print(r)
