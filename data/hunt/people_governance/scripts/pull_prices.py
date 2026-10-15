"""Daily close and adjusted close, 2006-01-03 to today, from the Yahoo chart API (free, no login).
Usage: python3 -I pull_prices.py OUTDIR T1 T2 ..."""
import sys, os, json, csv, time, datetime as dt, urllib.request
OUT = sys.argv[1]; rows = []
for t in sys.argv[2:]:
    p = os.path.join(OUT, f'raw/px/{t}.json')
    if not os.path.exists(p):
        u = f'https://query1.finance.yahoo.com/v8/finance/chart/{t}?period1=1136073600&period2=1792000000&interval=1d&events=div'
        try: open(p, 'wb').write(urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60).read())
        except Exception as e: print('fail', t, e); continue
        time.sleep(0.8)
    try: r = json.load(open(p))['chart']['result'][0]
    except Exception: print('bad', t); continue
    q = r['indicators']['quote'][0]; adj = r['indicators']['adjclose'][0]['adjclose']
    for i, s in enumerate(r['timestamp']):
        if adj[i] is None or q['close'][i] is None: continue
        rows.append([t, dt.datetime.utcfromtimestamp(s + r['meta']['gmtoffset']).date().isoformat(), round(q['close'][i], 4), round(adj[i], 4)])
    print(t, rows[-1][1])
w = csv.writer(open(os.path.join(OUT, 'prices_peers_2006_2026.csv'), 'w', newline='')); w.writerow(['ticker', 'date', 'close', 'adj_close']); w.writerows(rows)
