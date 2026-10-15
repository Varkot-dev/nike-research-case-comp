"""Fetch SEC companyfacts and Yahoo daily prices for the expanded universe.
Usage: python3 -I fetch.py OUTDIR
Writes OUTDIR/sec/<T>.json and OUTDIR/px/<T>.json. Generic User-Agent, no personal data."""
import sys, json, time, urllib.request, os
OUT = sys.argv[1]
UA = 'nike-case-research-bot research@example.org'
CIK = dict(DKS=1089063, ASO=1817358, HIBB=1017480, GCO=18498, CAL=14707, DBI=1319947, BKE=885245,
  JWN=72333, BURL=1579298, ROST=745732, TJX=109198, PLCE=1041859, CATO=18255, TLYS=1524025,
  FIGS=1846576, YETI=1670592, RVLV=1746618, SFIX=1576942, VSCO=1856437, WEYS=106532,
  ASNA=1498301, TLRD=884217, JCP=1166126, FRAN=1399935, PIR=278130, SMRT=884940, DXLG=813298,
  CBK=883943, SSI=6885, BBBY=886158, DLTH=1649744, LAKE=798081, DLA=1101396, LE=799288,
  VNCE=1579157, JILL=1687932, KTB=1760965, ONON=1858985, BIRK=1977102, ELF=1600033, COTY=1024305)
EXTRA_PX = ['XRT', 'XLY', 'RTH', '^GSPC']
def get(url, ua):
    req = urllib.request.Request(url, headers={'User-Agent': ua})
    with urllib.request.urlopen(req, timeout=60) as r: return r.read()
os.makedirs(OUT + '/sec', exist_ok=True); os.makedirs(OUT + '/px', exist_ok=True)
for t, c in CIK.items():
    p = f'{OUT}/sec/{t}.json'
    if not os.path.exists(p):
        try:
            b = get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{c:010d}.json', UA)
            open(p, 'wb').write(b); print('sec', t, json.loads(b).get('entityName'))
        except Exception as e: print('sec FAIL', t, e)
        time.sleep(0.2)
for t in list(CIK) + EXTRA_PX:
    p = f'{OUT}/px/{t}.json'
    if os.path.exists(p): continue
    try:
        b = get(f'https://query1.finance.yahoo.com/v8/finance/chart/{t}?period1=0&period2=1792000000&interval=1d&events=div,split', 'Mozilla/5.0')
        j = json.loads(b)['chart']['result'][0]; open(p, 'wb').write(b); print('px', t, len(j.get('timestamp', [])))
    except Exception as e: print('px FAIL', t, e)
    time.sleep(0.3)
