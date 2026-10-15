"""Parse raw statement sentences into tidy unit/ASP rows.
Usage: python3 -I parse.py <raw.csv> <out.csv>
"""
import sys, re, csv

RAW, OUT = sys.argv[1], sys.argv[2]
ORD = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4}


def own_periods(form, pend):
    y, m = int(pend[:4]), int(pend[5:7])
    if form == '10-K':
        return f'FY{y}', None
    if m in (8, 9):
        return f'Q1FY{y+1}', None
    if m in (11, 12):
        return f'Q2FY{y+1}', f'6MFY{y+1}'
    return f'Q3FY{y}', f'9MFY{y}'


def filing_label(form, pend, file):
    y, m = int(pend[:4]), int(pend[5:7])
    if form == '10-K':
        return f'FY{y} Form 10-K'
    q = {8: 1, 9: 1, 11: 2, 12: 2, 2: 3, 3: 3}[m]
    fy = y + 1 if q in (1, 2) else y
    return f'Q{q} FY{fy} Form 10-Q'


NUM = r'(\d+(?:\.\d+)?)'
UP = r'(increased|grew|rose|were up|was up)'
DN = r'(decreased|declined|fell|were down|was down)'


def sgn(word):
    w = word.lower()
    if re.match(UP, w):
        return 1
    if re.match(DN, w):
        return -1
    return 0


ASPT = r'(?:average selling price \(\W?ASP\W?\)|ASPs?)(?:,[^,.]{0,40},)?(?: per (?:pair|unit))?'


def parse_units(s):
    """returns list of numbers (1 or 2) or None"""
    if re.search(r'unit orders|futures orders', s, re.I):
        return None, False
    m = re.search(r'unit sales[^.%;]{0,90}?\b(increased|decreased|grew|declined|rose|fell|contracted|expanded)\s+(?:by\s+)?(?:approximately\s+)?' + NUM +
                  r'%(?:\s+and\s+(?:approximately\s+)?' + NUM + r'%)?', s, re.I)
    if m:
        w = m.group(1).lower()
        sg = -1 if w in ('decreased', 'declined', 'fell', 'contracted') else 1
        vals = [sg * float(m.group(2))]
        if m.group(3):
            vals.append(sg * float(m.group(3)))
        both = bool(re.search(r'both periods', s[m.end():m.end() + 40]))
        return vals, both
    m = re.search(r'unit sales[^.;%]{0,90}?\b(was|were|remained)\s+(?:relatively\s+|approximately\s+)?(flat|unchanged)', s, re.I)
    if m:
        return [0.0], bool(re.search(r'both periods', s))
    return None, False


def parse_asp(s):
    if re.search(r'unit orders|futures orders', s, re.I):
        return None, None, None
    m = re.search(r'\b(higher|lower|increase in|decrease in)?\s*' + ASPT + r'(?:,\s*which)?\s+'
                  r'(contributed|contributing|reduced|reducing|increased|decreased|added|lowered|offset)\s+[^.]*?(?:approximately\s+)?' + NUM +
                  r'(?:\s+and\s+' + NUM + r')?\s+percentage point', s, re.I)
    if m:
        adj = (m.group(1) or '').lower()
        verb = m.group(2).lower()
        sg = -1 if (adj in ('lower', 'decrease in') or verb in ('reduced', 'reducing', 'decreased', 'lowered', 'offset')) else 1
        vals = [sg * float(m.group(3))]
        if m.group(4):
            vals.append(sg * float(m.group(4)))
        return vals, 'pp_contribution', m.start()
    m = re.search(r'approximately ' + NUM + r' percentage points? of (?:\w+ )?(?:revenue )?growth due to (higher|lower) ASP', s)
    if m:
        sg = 1 if m.group(2) == 'higher' else -1
        return [sg * float(m.group(1))], 'pp_contribution', m.start()
    m = re.search(r'\b' + ASPT + r'\s+(increased|decreased|grew|declined)\s+(?:approximately\s+)?' + NUM + r'%(?:\s+and\s+' + NUM + r'%)?', s)
    if m:
        sg = 1 if m.group(1) in ('increased', 'grew') else -1
        vals = [sg * float(m.group(2))]
        if m.group(3):
            vals.append(sg * float(m.group(3)))
        return vals, 'pct', m.start()
    m = re.search(r'ASP (expansion|contraction) of ' + NUM + '%', s)
    if m:
        return [(1 if m.group(1) == 'expansion' else -1) * float(m.group(2))], 'pct', m.start()
    m = re.search(r'(' + ASPT + r'|unit sales of \w+ and ASP per (?:pair|unit))\s+(was|were|remained)\s+(?:relatively\s+|approximately\s+)?(flat|unchanged)', s)
    if m:
        return [0.0], 'flat', m.start()
    m = re.search(ASPT + r'\s+(was|were)\s+slightly\s+(up|down)', s)
    if m:
        return [0.0], 'slightly_' + m.group(2), m.start()
    return None, None, None


def category(seg, s):
    if seg == 'Converse':
        return 'comparable_direct_distribution_total' if 'direct distribution' in s.lower() else 'total'
    sl = s.lower()
    fw = 'footwear' in sl or 'per pair' in sl
    ap = 'apparel' in sl or ('per unit' in sl and not fw)
    if fw and not ap:
        return 'footwear'
    if ap and not fw:
        return 'apparel'
    if fw and ap:
        # pick the one tied to unit sales phrase
        m = re.search(r'unit sales of (footwear|apparel)', sl)
        if m:
            return m.group(1)
        return 'AMBIG'
    return 'UNKNOWN'


def drivers(s, drv):
    txt = ''
    m = re.search(r'ASP[^.]*?\b(due to|driven by|reflecting|attributable to|as a result of|result of|as higher|as lower|as)\b(.*)$', s)
    if m:
        txt = (m.group(1) + m.group(2)).strip()
    if drv:
        txt = (txt + ' | ' + drv).strip(' |')
    return txt


def main():
    rows = list(csv.DictReader(open(RAW)))
    out = []
    for r in rows:
        s = r['sentence']
        para = r['paragraph']
        qp, yp = own_periods(r['form'], r['period_end'])
        u, uboth = parse_units(s)
        a, ameas, apos = parse_asp(s)
        if u is None and a is None:
            continue
        cat = category(r['seg'], s)
        flags = []
        # period resolution
        if r['head_period']:
            periods = [r['head_period']]
        else:
            # sentence-level or paragraph-level hints
            sm = re.search(r'(first|second|third|fourth) quarter and first (six|nine) months', s.split('. ')[0], re.I)
            if r['form'] == '10-K':
                ys = re.findall(r'fiscal (\d{4})', s)
                if not ys:
                    before = para[:para.find(s[:40])] if s[:40] in para else para
                    ys = re.findall(r'fiscal (\d{4})', before)
                periods = [f'FY{ys[-1] if ys and not re.findall(r"fiscal (\d{4})", s) else (ys[0] if ys else qp[2:])}']
            elif yp is None:
                periods = [qp]
            else:
                s0 = s.split('. ')[0]
                has_q = re.search(r'(first|second|third|fourth) quarter', s0, re.I)
                has_y = re.search(r'first (six|nine) months|year-to-date', s0, re.I)
                nums = max(len(u or []), len(a or []))
                if (u and len(u) == 2) or (a and len(a) == 2) or uboth or 'both periods' in s.split('. ')[0] or sm:
                    periods = [qp, yp]
                elif has_q and not has_y:
                    periods = [qp]
                elif has_y and not has_q:
                    periods = [yp]
                else:
                    # look back in paragraph for the latest explicit period phrase
                    idx = para.find(s[:40])
                    before = para[:idx] if idx > 0 else ''
                    lq = [mm for mm in re.finditer(r'(quarter|first (six|nine) months)', before, re.I)]
                    if lq and 'months' in lq[-1].group(0).lower() and 'quarter' not in before[lq[-1].start()-60:lq[-1].start()].lower():
                        periods = [yp]; flags.append('period_from_context_ytd')
                    elif lq:
                        periods = [qp]; flags.append('period_from_context_q')
                    else:
                        periods = [qp]; flags.append('period_assumed_q')
        for i, p in enumerate(periods):
            def pick(v):
                if v is None:
                    return ''
                if len(v) == 1:
                    return v[0]
                return v[i] if i < len(v) else v[-1]
            uu = pick(u)
            aa = pick(a)
            out.append(dict(period=p, segment=r['seg'], category=cat,
                            units_change_pct='' if uu == '' else f'{uu:g}',
                            asp_change_pct='' if aa == '' else f'{aa:g}',
                            asp_measure=ameas or '',
                            asp_drivers_text=drivers(s, r['driver_sents']),
                            filing=filing_label(r['form'], r['period_end'], r['file']),
                            file=r['file'], seq_page=r['seq_page'], printed_page=r['printed_page'],
                            quote=s + ((' ' + r['driver_sents']) if r['driver_sents'] else ''),
                            flags=';'.join(flags)))
    with open(OUT, 'w', newline='') as fo:
        w = csv.DictWriter(fo, fieldnames=list(out[0].keys()))
        w.writeheader()
        w.writerows(out)
    print(len(out), 'rows')


main()
