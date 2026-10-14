"""Fetch Nike 8-K primary docs with items 5.02 or 5.07 (2015-2026) and save plain text. Usage: python3 -I pull_nke_8k_text.py OUTDIR"""
import sys, os, csv, re, time, html, urllib.request
OUT = sys.argv[1]; UA = "NikeCaseCompResearch/1.0 research-contact@example.org"
for r in csv.DictReader(open(os.path.join(OUT, 'raw/8k_filings_peers.csv'))):
    if r['ticker'] != 'NKE' or not ('5.02' in r['items'] or '5.07' in r['items']): continue
    p = os.path.join(OUT, f"raw/nke_8k/{r['filing_date']}_{r['accession']}.txt")
    if os.path.exists(p): continue
    url = f"https://www.sec.gov/Archives/edgar/data/320187/{r['accession'].replace('-','')}/{r['primary_doc']}"
    h = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=60).read().decode('utf-8', 'replace')
    t = re.sub(r'<(br|/p|/div|/tr)[^>]*>', '\n', h, flags=re.I); t = re.sub(r'<td[^>]*>', ' | ', t, flags=re.I)
    t = html.unescape(re.sub(r'<[^>]+>', ' ', t)); t = re.sub(r'[ \t\xa0]+', ' ', t); t = re.sub(r'\n\s*\n+', '\n', t)
    open(p, 'w').write(url + '\n' + r['items'] + '\n' + t); print(p, flush=True); time.sleep(0.4)
