"""Pull monthly trade from UN Comtrade public preview API (no key).
Usage: python pull_comtrade.py <reporter> <flow M|X> <partners csv> <cmds csv> <years csv> <outprefix>
Saves raw JSON per (cmd, year) into raw/comtrade/."""
import sys, json, time, os, urllib.request
rep, flow, partners, cmds, years, prefix = sys.argv[1:7]
out = os.path.join(os.path.dirname(__file__), '..', 'raw', 'comtrade'); os.makedirs(out, exist_ok=True)
for cmd in cmds.split(','):
    for y in years.split(','):
        fn = os.path.join(out, f'{prefix}_{cmd}_{y}.json')
        if os.path.exists(fn) and os.path.getsize(fn) > 200: continue
        per = ','.join(f'{y}{m:02d}' for m in range(1, 13))
        url = (f'https://comtradeapi.un.org/public/v1/preview/C/M/HS?reporterCode={rep}&period={per}'
               f'&partnerCode={partners}&cmdCode={cmd}&flowCode={flow}')
        for attempt in range(4):
            try:
                with urllib.request.urlopen(url, timeout=90) as r: d = json.load(r)
                break
            except Exception as e:
                print('retry', cmd, y, e); time.sleep(10)
        else:
            continue
        json.dump(d, open(fn, 'w'))
        print(prefix, cmd, y, d.get('count'), d.get('error'))
        time.sleep(3)
