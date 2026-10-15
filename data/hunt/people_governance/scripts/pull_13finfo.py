"""Pull 13f.info per-quarter holder JSON for a CUSIP, and the CUSIP summary page.
Usage: python3 -I pull_13finfo.py OUTDIR CUSIP TAG 2019 1 2026 2 [summary_only]"""
import sys, os, time, urllib.request
OUT, CUSIP, TAG = sys.argv[1:4]; y0, q0, y1, q1 = map(int, sys.argv[4:8])
only_summary = len(sys.argv) > 8
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36'
def get(url, path, ref):
    if os.path.exists(path) and os.path.getsize(path) > 1000: return
    for a in range(3):
        try:
            r = urllib.request.Request(url, headers={'User-Agent': UA, 'Referer': ref})
            open(path, 'wb').write(urllib.request.urlopen(r, timeout=90).read()); print('ok', url, flush=True); return
        except Exception as e:
            print('err', url, e, flush=True); time.sleep(8)
base = 'https://13f.info/cusip/' + CUSIP
get(base, os.path.join(OUT, f'raw/13finfo/{TAG}_summary.html'), 'https://13f.info/')
time.sleep(2)
if only_summary: sys.exit()
y, q = y0, q0
while (y, q) <= (y1, q1):
    get(f'https://13f.info/data/cusip/{CUSIP}/{y}/{q}', os.path.join(OUT, f'raw/13finfo/{TAG}_{y}q{q}.json'), f'{base}/{y}/{q}')
    time.sleep(2.5); q += 1
    if q == 5: y, q = y + 1, 1
