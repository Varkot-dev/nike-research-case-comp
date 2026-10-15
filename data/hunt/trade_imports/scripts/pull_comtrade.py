"""Pull monthly trade from UN Comtrade public preview API (no key; 1 period per call, max 500 rows).
Usage: python pull_comtrade.py <reporter> <flow M|X> <partners csv> <cmds csv> <start YYYYMM> <end YYYYMM> <outprefix>
Saves raw JSON per month into raw/comtrade/<prefix>_<YYYYMM>.json"""
import sys, json, time, os, urllib.request

rep, flow, partners, cmds, start, end, prefix = sys.argv[1:8]
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'raw', 'comtrade')
os.makedirs(out, exist_ok=True)
y, m = int(start[:4]), int(start[4:])
while y * 100 + m <= int(end):
    per = f'{y}{m:02d}'
    fn = os.path.join(out, f'{prefix}_{per}.json')
    if not (os.path.exists(fn) and os.path.getsize(fn) > 200):
        url = (f'https://comtradeapi.un.org/public/v1/preview/C/M/HS?reporterCode={rep}&period={per}'
               f'&partnerCode={partners}&cmdCode={cmds}&flowCode={flow}')
        d = None
        for attempt in range(4):
            try:
                with urllib.request.urlopen(url, timeout=90) as r:
                    d = json.load(r)
                break
            except Exception as e:
                print('retry', per, e, flush=True)
                time.sleep(15)
        if d is not None:
            json.dump(d, open(fn, 'w'))
            print(prefix, per, d.get('count'), d.get('error'), flush=True)
        time.sleep(2)
    m += 1
    if m == 13:
        y, m = y + 1, 1
