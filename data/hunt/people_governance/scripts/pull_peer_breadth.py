"""For each ticker with prices in data/hunt/risk_short_interest/prices_all.csv, look up its CUSIP via
13f.info autocomplete and save the CUSIP summary page (13F holders by quarter).
Usage: python3 -I pull_peer_breadth.py OUTDIR PRICES_CSV"""
import sys, os, csv, json, time, urllib.request, urllib.parse
OUT, PR = sys.argv[1:3]
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36'
def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA, 'Referer': 'https://13f.info/'}), timeout=60).read()
ticks = sorted(set(r['ticker'] for r in csv.DictReader(open(PR))) - {'SPY', 'XLP', 'XLY', 'ticker'})
mapf = os.path.join(OUT, 'raw/13finfo/cusip_map.csv'); have = {}
if os.path.exists(mapf): have = {r['ticker']: r for r in csv.DictReader(open(mapf))}
for t in ticks:
    if t in have or os.path.exists(os.path.join(OUT, f'raw/13finfo/{t}_summary.html')): continue
    try:
        j = json.loads(get('https://13f.info/data/autocomplete?q=' + urllib.parse.quote(t)))
        c = [x for x in j.get('cusips', []) if x['name'].split(' - ')[0].strip() == t and ('COM' in x['extra'] or 'CL A' in x['extra'] or 'CL B' in x['extra'] or 'SHS' in x['extra'])]
        if not c: print('nocusip', t, [x['name'] + '|' + x['extra'] for x in j.get('cusips', [])][:3]); time.sleep(2); continue
        have[t] = dict(ticker=t, cusip=c[0]['extra'].split(' - ')[0], label=c[0]['name'] + ' | ' + c[0]['extra'])
        time.sleep(2)
        open(os.path.join(OUT, f'raw/13finfo/{t}_summary.html'), 'wb').write(get('https://13f.info' + c[0]['url']))
        print('ok', t, have[t]['cusip'], flush=True); time.sleep(2.5)
    except Exception as e:
        print('err', t, e, flush=True); time.sleep(5)
w = csv.DictWriter(open(mapf, 'w', newline=''), fieldnames=['ticker', 'cusip', 'label']); w.writeheader(); w.writerows(have.values())
