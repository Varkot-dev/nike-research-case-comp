"""Clean SEC insider data set rows into tidy tables.
Outputs: insider_open_market_peers_2006_2026.csv (code P and S only, deduplicated),
nke_insider_yearly_2006_2026.csv, insider_market_wide_quarterly.csv. Usage: python3 -I clean_insider.py OUTDIR"""
import sys, os, csv, collections, datetime as dt
OUT = sys.argv[1]
def d(s): return dt.datetime.strptime(s, '%d-%b-%Y').date()
seen = set(); rows = []
for r in csv.DictReader(open(os.path.join(OUT, 'raw/insider_ds_peer_nonderiv.csv'))):
    if r['code'] not in ('P', 'S') or r['doc_type'] not in ('4', '4/A', '5'): continue
    try: sh = float(r['shares'] or 0); px = float(r['price'] or 0)
    except: continue
    k = (r['ticker'], r['owner_names'], r['trans_date'], r['code'], round(sh), round(px, 2))
    if k in seen: continue
    seen.add(k)
    rel = r['owner_rel'].lower()
    rows.append(dict(ticker=r['ticker'], trans_date=str(d(r['trans_date'])), filing_date=str(d(r['filing_date'])), owner=r['owner_names'], rel=r['owner_rel'],
                     title=r['owner_title'], code=r['code'], shares=round(sh), price=round(px, 4), value_usd=round(sh * px),
                     ten_pct_owner='tenpercent' in rel.replace(' ', '').replace('%', 'percent'), accession=r['accession']))
rows.sort(key=lambda r: (r['ticker'], r['trans_date']))
w = csv.DictWriter(open(os.path.join(OUT, 'insider_open_market_peers_2006_2026.csv'), 'w', newline=''), fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
Y = collections.defaultdict(lambda: dict(buyers=set(), buy_usd=0, n_buy=0, sellers=set(), sell_usd=0, n_sell=0))
for r in rows:
    if r['ticker'] != 'NKE': continue
    y = Y[r['trans_date'][:4]]
    if r['code'] == 'P': y['buyers'].add(r['owner']); y['buy_usd'] += r['value_usd']; y['n_buy'] += 1
    else: y['sellers'].add(r['owner']); y['sell_usd'] += r['value_usd']; y['n_sell'] += 1
w = csv.writer(open(os.path.join(OUT, 'nke_insider_yearly_2006_2026.csv'), 'w', newline=''))
w.writerow(['year', 'distinct_buyers', 'n_buy_tx', 'buy_usd', 'distinct_sellers', 'n_sell_tx', 'sell_usd', 'buyer_names'])
for k in sorted(Y):
    y = Y[k]; w.writerow([k, len(y['buyers']), y['n_buy'], y['buy_usd'], len(y['sellers']), y['n_sell'], y['sell_usd'], '; '.join(sorted(y['buyers']))])
    print(k, len(y['buyers']), y['n_buy'], f"{y['buy_usd']/1e6:.2f}M", len(y['sellers']), f"{y['sell_usd']/1e6:.1f}M", '; '.join(sorted(y['buyers']))[:120])
