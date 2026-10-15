import json, csv, datetime, statistics, bisect, sys
D = datetime.date.fromisoformat
RAW = '../raw'
PEERS = ['VFC','COLM','DECK','UAA','LULU','CROX','PVH','RL','WWW']
ALL = ['NKE'] + PEERS
ann = {}
for r in csv.DictReader(open('annual.csv')):
    ann.setdefault(r['ticker'], []).append(r)
def f(x):
    return float(x) if x not in ('', None) else None
# prices and splits
px = {}; spl = {}
for t in ALL + ['^GSPC']:
    j = json.load(open(f'{RAW}/px_{t}.json'))['chart']['result'][0]
    ts = j['timestamp']; cl = j['indicators']['quote'][0]['close']
    s = sorted((datetime.date.fromtimestamp(a), b) for a, b in zip(ts, cl) if b)
    px[t] = ([a for a, _ in s], [b for _, b in s])
    spl[t] = sorted((datetime.date.fromtimestamp(v['date']), v['numerator']/v['denominator']) for v in j.get('events', {}).get('splits', {}).values())
def price(t, d):
    ds, cs = px[t]; i = bisect.bisect_right(ds, d) - 1
    return (ds[i], cs[i]) if i >= 0 and (d - ds[i]).days < 8 else (None, None)
def split_adj(t, filed):  # factor to convert per-share value reported at 'filed' into today's split-adjusted basis
    fac = 1.0
    for d, r in spl[t]:
        if d > filed: fac *= r
    return fac
# build fiscal-year records
FY = {}
for t in ALL:
    L = []
    for r in ann[t]:
        fye = D(r['fye']); filed = D(r['filed'])
        fac = split_adj(t, filed)
        eps = f(r['eps']); shs = f(r['shs'])
        rev = f(r['rev']); op = f(r['opinc'])
        if op is None and f(r['pretax']) is not None:
            ni_ = f(r['netint']) or 0
            op = f(r['pretax']) - (ni_ if t == 'NKE' else 0)   # NKE: EBIT = pretax - net interest income (tag is income-positive); others: pretax
        debt = (f(r['ltd']) or 0) + (f(r['ltdc']) or 0) + (f(r['stb']) or 0)
        cash = (f(r['cash']) or 0) + (f(r['sti']) or 0)
        eps_clean = eps/fac if eps is not None else None
        if t == 'NKE' and eps is not None:
            # adjusted EPS per Nike FY2009 10-K reconciliation (OPENED): FY08 3.45, FY09 3.81 (pre 2012/2015 splits, filed 2009 basis -> /4)
            if r['fye'] == '2008-05-31': eps_clean = 3.45/4
            if r['fye'] == '2009-05-31': eps_clean = 3.81/4
            # FY18: add back Tax Act $1,875M + $158M (FY2018 10-K, OPENED) / 1,659.1M diluted shares (DERIVED)
            if r['fye'] == '2018-05-31': eps_clean = eps/fac + 2033/1659.1
        L.append(dict(eps_clean=eps_clean, fye=fye, avail=fye + datetime.timedelta(days=60), eps=eps/fac if eps is not None else None,
                      shs=shs*fac if shs else None, rev=rev, op=op, debt=debt, cash=cash, ni=f(r['ni']), cfo=f(r['cfo']), capex=f(r['capex']), eq=f(r['eq']),
                      has_bs=bool(r['cash']!='' )))
    L.sort(key=lambda x: x['fye'])
    FY[t] = L
def snap(t, d):
    L = FY[t]; p = price(t, d)[1]
    if p is None: return None
    rep = [x for x in L if x['avail'] <= d]
    last = rep[-1] if rep else dict(fye=D('1900-01-01'), avail=D('1900-01-01'), eps=None, eps_clean=None, shs=None, rev=None, op=None, debt=0, cash=0, ni=None, cfo=None, capex=None, eq=None, has_bs=False)
    fut = [x for x in L if x['fye'] >= d]
    out = dict(price=p, last=last, have_last=bool(rep))
    out['pe_trail'] = p / last['eps'] if last['eps'] and last['eps'] > 0 else None
    out['pe_trail_clean'] = p / last['eps_clean'] if last['eps_clean'] and last['eps_clean'] > 0 else None
    # NTM perfect foresight
    ntm_eps = None; ntm_rev = None; ntm_clean = None; ntm_op = None
    if len(fut) >= 2:
        a, b = fut[0], fut[1]
        if 330 < (b['fye'] - a['fye']).days < 400 and (a['fye'] - d).days <= 400:
            w = min(1.0, (a['fye'] - d).days / 365.0)
            if a['eps'] is not None and b['eps'] is not None: ntm_eps = w*a['eps'] + (1-w)*b['eps']
            if a['eps_clean'] is not None and b['eps_clean'] is not None: ntm_clean = w*a['eps_clean'] + (1-w)*b['eps_clean']
            if a['op'] is not None and b['op'] is not None: ntm_op = w*a['op'] + (1-w)*b['op']
            if a['rev'] and b['rev']: ntm_rev = w*a['rev'] + (1-w)*b['rev']
            out['fy2_eps'] = b['eps']; out['fy1_eps'] = a['eps']
    out['pe_ntm'] = p / ntm_eps if ntm_eps and ntm_eps > 0 else None
    out['pe_ntm_clean'] = p / ntm_clean if ntm_clean and ntm_clean > 0 else None
    # EV/Sales trailing and NTM
    if last['shs'] and last['rev'] and last['has_bs']:
        mc = p * last['shs']
        ev = mc + last['debt'] - last['cash']
        out['evs_trail'] = ev / last['rev']
        out['evs_ntm'] = ev / ntm_rev if ntm_rev else None
        out['eve_trail'] = ev / last['op'] if last['op'] and last['op'] > 0 else None
        out['eve_ntm'] = ev / ntm_op if ntm_op and ntm_op > 0 else None
        ic = (last['eq'] or 0) + last['debt'] - last['cash']
        out['roic'] = last['op'] * 0.75 / ic if last['op'] and ic > 0 else None
        out['fcf_conv'] = (last['cfo'] - (last['capex'] or 0)) / last['ni'] if last['cfo'] and last['ni'] and last['ni'] > 0 else None
        out['mcap'] = mc
    else:
        out['evs_trail'] = out['evs_ntm'] = out['eve_trail'] = out['eve_ntm'] = out['roic'] = out['fcf_conv'] = None
    out['opm'] = last['op'] / last['rev'] if last['op'] is not None and last['rev'] else None
    return out
def med(v):
    v = [x for x in v if x is not None]
    return (statistics.median(v), len(v)) if v else (None, 0)
def month_ends(a, b):
    d = a; out = []
    while d <= b:
        nxt = datetime.date(d.year + (d.month == 12), d.month % 12 + 1, 1)
        out.append(nxt - datetime.timedelta(days=1)); d = nxt
    return out
rows = []
def one(d):
    n = snap('NKE', d)
    if not n: return None
    ps = {t: snap(t, d) for t in PEERS}
    r = dict(date=d.isoformat(), nke_price=round(n['price'], 2))
    pk = {'pe_trail_clean': 'pe_trail', 'pe_ntm_clean': 'pe_ntm'}
    for k in ['pe_trail', 'pe_ntm', 'pe_trail_clean', 'pe_ntm_clean', 'evs_trail', 'evs_ntm', 'eve_trail', 'eve_ntm']:
        pm, pn = med([ps[t][pk.get(k, k)] for t in PEERS if ps[t]])
        r['nke_' + k] = round(n[k], 2) if n[k] else None
        r['peer_med_' + k] = round(pm, 2) if pm else None
        r['peer_n_' + k] = pn
        r['prem_' + k] = round(n[k] / pm - 1, 3) if n[k] and pm and pn >= 4 else None
    r['nke_roic_last'] = round(n['roic'], 4) if n.get('roic') else None
    r['peer_med_roic_last'] = round(med([ps[t].get('roic') for t in PEERS if ps[t]])[0] or 0, 4)
    r['nke_fcf_conv'] = round(n['fcf_conv'], 3) if n.get('fcf_conv') else None
    r['peer_med_fcf_conv'] = round(med([ps[t].get('fcf_conv') for t in PEERS if ps[t]])[0] or 0, 3)
    r['nke_last_fy'] = n['last']['fye'].isoformat(); r['nke_last_eps'] = round(n['last']['eps'], 3)
    r['nke_opm_last'] = round(n['opm'], 4) if n['opm'] else None
    r['peer_med_opm_last'] = round(med([ps[t]['opm'] for t in PEERS if ps[t]])[0] or 0, 4)
    lastrev = [x for x in FY['NKE'] if x['fye'] < n['last']['fye']]
    r['nke_rev_growth_last'] = round(n['last']['rev'] / lastrev[-1]['rev'] - 1, 4) if lastrev and lastrev[-1]['rev'] else None
    return r
if __name__ == '__main__':
    for d in month_ends(D('2008-08-01'), D('2026-09-30')):
        r = one(d)
        if r: rows.append(r)
    w = csv.DictWriter(open('monthly.csv', 'w', newline=''), list(rows[0])); w.writeheader(); w.writerows(rows)
    print(len(rows))
    for r in rows[::6]:
        print(r['date'], r['nke_pe_trail'], r['peer_med_pe_trail'], r['prem_pe_trail'], '|', r['nke_pe_ntm'], r['peer_med_pe_ntm'], r['prem_pe_ntm'], '|', r['nke_evs_trail'], r['peer_med_evs_trail'], r['prem_evs_trail'], r['peer_n_pe_ntm'])
