"""SEC submissions JSON for issuers: list every 8-K with item codes (2015-2026).
Usage: python3 -I pull_8k_items.py OUTDIR"""
import sys, os, json, time, urllib.request, csv
OUT = sys.argv[1]
UA = "NikeCaseCompResearch/1.0 research-contact@example.org"
CIK = {'NKE':320187,'DECK':910521,'LULU':1397187,'UAA':1336917,'SKX':1065837,'VFC':103379,'CROX':1334036,'COLM':1050797,'TPR':1116132,'RL':1037038,'PVH':78239,'LEVI':94845,'DKS':1089063,'FL':850209,'ADDYY_none':0}
def get(url):
    for a in range(3):
        try: return json.loads(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=60).read())
        except Exception as e: print('err', url, e); time.sleep(5)
rows = []
for t, c in CIK.items():
    if not c: continue
    d = get(f'https://data.sec.gov/submissions/CIK{c:010d}.json'); time.sleep(0.3)
    json.dump(d, open(os.path.join(OUT, f'raw/sec_submissions/{t}.json'), 'w'))
    blocks = [d['filings']['recent']]
    for f in d['filings'].get('files', []):
        if f['filingTo'] >= '2015-01-01':
            blocks.append(get('https://data.sec.gov/submissions/' + f['name'])); time.sleep(0.3)
    for b in blocks:
        for i in range(len(b['form'])):
            if b['form'][i] in ('8-K', '8-K/A') and b['filingDate'][i] >= '2015-01-01':
                rows.append([t, b['filingDate'][i], b['form'][i], b['accessionNumber'][i], b['items'][i], b['primaryDocument'][i]])
    print(t, len(rows), flush=True)
w = csv.writer(open(os.path.join(OUT, 'raw/8k_filings_peers.csv'), 'w', newline=''))
w.writerow(['ticker', 'filing_date', 'form', 'accession', 'items', 'primary_doc']); w.writerows(rows)
