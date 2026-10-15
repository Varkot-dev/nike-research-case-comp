"""Parse 13f.info CUSIP summary pages (holders by quarter) for NKE and peers into one tidy CSV.
Usage: python3 -I parse_13finfo_summaries.py OUTDIR"""
import sys, os, re, glob, csv
OUT = sys.argv[1]
def num(s):
    s = s.replace('$', '').replace(',', '').strip(); m = {'k': 1e3, 'M': 1e6, 'B': 1e9}
    return float(s[:-1]) * m[s[-1]] if s and s[-1] in m else float(s)
rows = []
for f in glob.glob(os.path.join(OUT, 'raw/13finfo/*_summary.html')):
    tag = os.path.basename(f).split('_summary')[0]
    t = re.sub(r'<[^>]+>', ' ', open(f).read()); t = re.sub(r'\s+', ' ', t)
    for m in re.finditer(r'(20\d\d) Q([1-4]) ([\d,]+) ([\d.,]+ ?[kMB]?) (\$[\d.,]+ ?[kMB]?) (\$[\d.,]+ ?[kMB]?)', t):
        rows.append(dict(ticker=tag, quarter=f'{m.group(1)}q{m.group(2)}', filings=int(m.group(3).replace(',', '')),
                         shares=num(m.group(4).replace(' ', '')), value_usd=num(m.group(5).replace(' ', '')), options_value_usd=num(m.group(6).replace(' ', ''))))
rows.sort(key=lambda r: (r['ticker'], r['quarter']))
w = csv.DictWriter(open(os.path.join(OUT, 'peer_13f_filings_by_quarter.csv'), 'w', newline=''), fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(len(rows))
