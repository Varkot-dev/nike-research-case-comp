"""Extract Rule 10b5-1 trading-arrangement disclosures (Reg S-K Item 408) from Nike 10-Q/10-K filings
since mid-2023 ("Other Information" item). Usage: python3 -I pull_10b51_disclosures.py OUTDIR"""
import sys, os, json, re, time, html, urllib.request
OUT = sys.argv[1]; UA = "NikeCaseCompResearch/1.0 research-contact@example.org"
d = json.load(open(os.path.join(OUT, 'raw/sec_submissions_NKE.json')))['filings']['recent']
for i in range(len(d['form'])):
    if d['form'][i] in ('10-Q', '10-K') and d['filingDate'][i] >= '2023-09-01':
        p = os.path.join(OUT, f"raw/nke_10q/{d['filingDate'][i]}_{d['form'][i]}_10b51.txt")
        if os.path.exists(p): continue
        url = f"https://www.sec.gov/Archives/edgar/data/320187/{d['accessionNumber'][i].replace('-','')}/{d['primaryDocument'][i]}"
        h = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=120).read().decode('utf-8', 'replace')
        t = html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h)))
        segs = [m.start() for m in re.finditer(r'10b5-1', t)]
        keep = []
        for s in segs:
            seg = t[max(0, s - 200): s + 1200]
            if 'adopted' in seg or 'terminated' in seg or 'trading arrangement' in seg: keep.append(seg)
        open(p, 'w').write(url + '\n' + '\n----\n'.join(keep[-4:])); print(p, len(keep), flush=True); time.sleep(0.5)
