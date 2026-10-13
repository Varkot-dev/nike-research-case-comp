"""Extract NIKE footwear/apparel unit and ASP statements from paged 10-K/10-Q text.
Usage: python3 -I extract.py <textdir> <out_raw_csv>
Emits one row per (filing, segment, statement sentence) with parsed fields and a parse flag.
"""
import sys, re, csv, os, glob

TEXT, OUT = sys.argv[1], sys.argv[2]

SEG = {
    'north america': 'North America', 'europe, middle east & africa': 'EMEA',
    'greater china': 'Greater China', 'asia pacific & latin america': 'APLA',
    'converse': 'Converse', 'western europe': 'Western Europe',
    'central & eastern europe': 'Central & Eastern Europe', 'japan': 'Japan',
    'emerging markets': 'Emerging Markets',
    'consolidated operating results': 'NIKE Brand', 'results of operations': 'NIKE Brand',
    'global brand divisions': None, 'corporate': None,
    'foreign currency exposures and hedging practices': 'STOP',
}
ORD = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4}
NUMW = {'six': '6M', 'nine': '9M'}


def fy_period(fy, q=None, ytd=None):
    if q:
        return f'Q{q}FY{fy}'
    if ytd:
        return f'{ytd}FY{fy}'
    return f'FY{fy}'


def head_period(line):
    m = re.match(r'^(first|second|third|fourth) quarter of fiscal (\d{4}) compared', line, re.I)
    if m:
        return fy_period(m.group(2), q=ORD[m.group(1).lower()])
    m = re.match(r'^first (six|nine) months of fiscal (\d{4}) compared', line, re.I)
    if m:
        return fy_period(m.group(2), ytd=NUMW[m.group(1).lower()])
    m = re.match(r'^fiscal (\d{4}) compared to fiscal', line, re.I)
    if m:
        return fy_period(m.group(1))
    return None


def split_sents(p):
    p = p.lstrip('•• |').strip()
    parts = re.split(r'(?<=[A-Za-z0-9%)])\.\s+(?=[A-Z])', p)
    return [s.strip() for s in parts if s.strip()]


STATE = re.compile(r'unit sales|ASP per (pair|unit)|\bASP (increased|decreased|was|were|contributed|reduced)|higher ASP contributed|lower ASP reduced|ASPs? (per|was|were)', re.I)


def main():
    rows = []
    for f in sorted(glob.glob(os.path.join(TEXT, '10-[KQ]_*.txt'))):
        base = os.path.basename(f)
        form, pend = base.split('_')[0], base.split('_')[1]
        page = printed = None
        seg = None
        hp = None  # heading period
        in_mdna = False
        for line in open(f, encoding='utf-8', errors='replace'):
            line = line.rstrip('\n')
            m = re.match(r'^=== PAGE (\d+) \| printed: (\S+) ===', line)
            if m:
                page, printed = int(m.group(1)), m.group(2)
                continue
            s = line.strip()
            low = s.lower()
            if low in ('results of operations',):
                in_mdna = True
            if not in_mdna:
                continue
            if low in SEG:
                if SEG[low] == 'STOP':
                    in_mdna = False
                    continue
                seg = SEG[low]
                hp = None
                continue
            h = head_period(s)
            if h:
                hp = h
                continue
            if seg is None or len(s) < 40:
                continue
            sents = split_sents(s)
            used = set()
            for i, se in enumerate(sents):
                if i in used or not STATE.search(se):
                    continue
                if re.search(r'gross margin|basis points', se, re.I):
                    continue
                grp = [se]
                if re.search(r'unit sales', se, re.I):
                    for j in range(i + 1, len(sents)):
                        nx = sents[j]
                        if re.search(r'unit sales', nx, re.I):
                            break
                        if re.search(r'\bASPs?\b', nx) and not re.search(r'gross margin|basis points', nx, re.I):
                            grp.append(nx); used.add(j)
                        else:
                            break
                rows.append(dict(form=form, period_end=pend, file=base, seg=seg, head_period=hp or '',
                                 seq_page=page, printed_page=printed, sentence='. '.join(grp), driver_sents='',
                                 paragraph=s))
    with open(OUT, 'w', newline='') as fo:
        w = csv.DictWriter(fo, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(len(rows), 'statement sentences')


main()
