"""Build NKE 13F holder panel 2018Q1-2026Q2 from 13f.info JSON and compute quarterly flow stats.
Outputs: nke_13f_holder_panel_2018_2026.csv (long: quarter,cik,manager,shares,put_sh,call_sh),
nke_13f_quarterly_flows_2018_2026.csv. Usage: python3 -I build_13f_panel.py OUTDIR"""
import sys, os, json, glob, csv, collections, re
OUT = sys.argv[1]
PASSIVE = re.compile(r'VANGUARD|BLACKROCK|STATE STREET|GEODE|NORTHERN TRUST|NORGES|DIMENSIONAL|LEGAL & GENERAL|CHARLES SCHWAB|INVESCO|NUVEEN|TIAA|MELLON|BANK OF NEW YORK|BNY|DEUTSCHE BANK|UBS|MORGAN STANLEY|GOLDMAN|JPMORGAN|JP MORGAN|WELLS FARGO|BANK OF AMERICA|MERRILL|RBC|ROYAL BANK|TD |TORONTO|AMERIPRISE|LPL|RAYMOND JAMES|EDWARD JONES|STIFEL|ALLIANZ|AMUNDI|DZ BANK|HSBC|BARCLAYS|CREDIT SUISSE|NOMURA|MIZUHO|SUMITOMO|MITSUBISHI|PRUDENTIAL|METLIFE|NEW YORK LIFE|FRANKLIN|PRINCIPAL|NATIXIS|SSGA|FIRST TRUST|ALPS|PROSHARES|DIREXION|VANECK|WISDOMTREE|RUSSELL|PARAMETRIC|RHUMBLINE|MANUFACTURERS LIFE|SUN LIFE|CANADA PENSION|ONTARIO|PUBLIC EMPLOYEES|TEACHERS|RETIREMENT SYSTEM|STATE BOARD|PENSION|TREASURER|COMMONWEALTH', re.I)
HEDGE = re.compile(r'CITADEL|MILLENNIUM|POINT72|BALYASNY|TWO SIGMA|RENAISSANCE|D\. ?E\. SHAW|SHAW D E|AQR|BRIDGEWATER|SUSQUEHANNA|JANE STREET|HUDSON BAY|SCHONFELD|EXODUSPOINT|MARSHALL WACE|PERSHING SQUARE|VIKING|TIGER|COATUE|LONE PINE|MAVERICK|D1 CAPITAL|THIRD POINT|SIXTH STREET|ELLIOTT|STARBOARD|JANA|TRIAN|VALUEACT|SOROS|DUQUESNE|APPALOOSA|GREENLIGHT|BAUPOST|ICONIQ|WOLVERINE|IMC|OPTIVER|GROUP ONE|CAPULA|MAN GROUP|WINTON|SCULPTOR|CANYON|ALPINE|TUDOR|KING STREET|ANSON|PALESTRA|WHALE ROCK|LIGHT STREET|GLENVIEW|SAMLYN|TOTE|SIR CAPITAL|DORSAL|CLEARLINE|VERITION|ARROWSTREET|QUBE|DEERFIELD|CABLE CAR|MARSHFIELD|JUPITER TOPCO', re.I)
def cls(n):
    if HEDGE.search(n): return 'hedge_or_trading'
    if PASSIVE.search(n): return 'index_bank_pension'
    return 'other_active_adviser'
panel = {}
for f in sorted(glob.glob(os.path.join(OUT, 'raw/13finfo/NKE_*q*.json'))):
    q = os.path.basename(f)[4:10]
    if q == '2026q3': continue  # Q3 2026 13F deadline is 2026-11-14; only early filers so far
    d = json.load(open(f))['data']
    byc = collections.defaultdict(lambda: collections.defaultdict(lambda: [0, 0, 0]))
    names = {}
    for (name, cik, _), (dt, fid), val, sh, opt in d:
        i = {None: 0, 'put': 1, 'call': 2}[opt]
        byc[cik][fid][i] += sh or 0; names[cik] = name
    for cik, fil in byc.items():
        rest = [k for k in fil if 'restatement' in k]
        keys = [sorted(rest)[-1]] if rest else list(fil)
        tot = [sum(fil[k][i] for k in keys) for i in range(3)]
        panel[(q, cik)] = dict(quarter=q, cik=cik, manager=names[cik], cls=cls(names[cik]), shares=tot[0], put_sh=tot[1], call_sh=tot[2])
qs = sorted(set(k[0] for k in panel))
w = csv.DictWriter(open(os.path.join(OUT, 'nke_13f_holder_panel_2018_2026.csv'), 'w', newline=''), fieldnames=['quarter', 'cik', 'manager', 'cls', 'shares', 'put_sh', 'call_sh'])
w.writeheader(); [w.writerow(panel[k]) for k in sorted(panel)]
rows = []
for i, q in enumerate(qs):
    cur = {c: v for (qq, c), v in panel.items() if qq == q and v['shares'] > 0}
    r = dict(quarter=q, holders=len(cur), shares_m=round(sum(v['shares'] for v in cur.values()) / 1e6, 1),
             put_sh_m=round(sum(v['put_sh'] for (qq, c), v in panel.items() if qq == q) / 1e6, 1),
             call_sh_m=round(sum(v['call_sh'] for (qq, c), v in panel.items() if qq == q) / 1e6, 1))
    r['put_call_ratio'] = round(r['put_sh_m'] / r['call_sh_m'], 2) if r['call_sh_m'] else None
    for k in ('hedge_or_trading', 'index_bank_pension', 'other_active_adviser'):
        r['shares_m_' + k] = round(sum(v['shares'] for v in cur.values() if v['cls'] == k) / 1e6, 1)
    if i:
        prev = {c: v for (qq, c), v in panel.items() if qq == qs[i - 1] and v['shares'] > 0}
        new = [c for c in cur if c not in prev]; ex = [c for c in prev if c not in cur]
        both = [c for c in cur if c in prev]
        r.update(new_positions=len(new), exits=len(ex), increased=sum(cur[c]['shares'] > prev[c]['shares'] * 1.02 for c in both),
                 decreased=sum(cur[c]['shares'] < prev[c]['shares'] * 0.98 for c in both),
                 new_sh_m=round(sum(cur[c]['shares'] for c in new) / 1e6, 1), exit_sh_m=round(sum(prev[c]['shares'] for c in ex) / 1e6, 1))
        r['net_entries'] = r['new_positions'] - r['exits']
        r['buyer_ratio'] = round((r['new_positions'] + r['increased']) / max(1, r['new_positions'] + r['increased'] + r['exits'] + r['decreased']), 3)
        # Hedge fund active flows (exclude pure options market makers by using equity shares only)
        hk = set(c for c in list(cur) + list(prev) if (cur.get(c) or prev.get(c))['cls'] == 'hedge_or_trading')
        r['hedge_net_sh_m'] = round(sum((cur.get(c, {}).get('shares', 0) - prev.get(c, {}).get('shares', 0)) for c in hk) / 1e6, 1)
        ok = set(c for c in list(cur) + list(prev) if (cur.get(c) or prev.get(c))['cls'] == 'other_active_adviser')
        r['active_adviser_net_sh_m'] = round(sum((cur.get(c, {}).get('shares', 0) - prev.get(c, {}).get('shares', 0)) for c in ok) / 1e6, 1)
    rows.append(r)
fields = list(rows[-1].keys())
w = csv.DictWriter(open(os.path.join(OUT, 'nke_13f_quarterly_flows_2018_2026.csv'), 'w', newline=''), fieldnames=fields); w.writeheader(); w.writerows(rows)
for r in rows: print({k: r.get(k) for k in ('quarter', 'holders', 'shares_m', 'new_positions', 'exits', 'net_entries', 'buyer_ratio', 'put_call_ratio', 'hedge_net_sh_m', 'active_adviser_net_sh_m')})
