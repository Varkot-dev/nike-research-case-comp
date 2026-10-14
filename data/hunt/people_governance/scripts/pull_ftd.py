"""SEC fails-to-deliver half-month files: keep rows for a symbol list. Usage: python3 -I pull_ftd.py OUTDIR 201901"""
import sys, io, re, zipfile, time, urllib.request, csv, os
OUT, start = sys.argv[1], sys.argv[2]
UA = "NikeCaseCompResearch/1.0 research-contact@example.org"
SYM = set("NKE DECK LULU UAA SKX VFC CROX ONON BIRK ADDYY FL".split())
idx = open(os.path.join(OUT, 'raw/ftd_index.html')).read()
links = sorted(set(re.findall(r'href="(/files/data/fails-deliver-data/cnsfails(\d{6})([ab])\.zip)"', idx)), key=lambda x: (x[1], x[2]))
outp = os.path.join(OUT, 'raw/ftd_peers_raw.csv')
have = set()
if os.path.exists(outp):
    have = set(r[0] for r in csv.reader(open(outp)))
f = open(outp, 'a', newline=''); w = csv.writer(f)
if not have: w.writerow(['file', 'settlement_date', 'cusip', 'symbol', 'quantity_fails', 'description', 'price'])
for path, ym, half in links:
    if ym < start: continue
    tag = ym + half
    if tag in have: continue
    try:
        data = urllib.request.urlopen(urllib.request.Request('https://www.sec.gov' + path, headers={'User-Agent': UA}), timeout=120).read()
    except Exception as e:
        print('fail', tag, e); time.sleep(5); continue
    z = zipfile.ZipFile(io.BytesIO(data))
    txt = z.open(z.namelist()[0]).read().decode('latin-1')
    n = 0
    for line in txt.splitlines()[1:]:
        p = line.split('|')
        if len(p) >= 6 and p[2].strip() in SYM:
            w.writerow([tag, p[0], p[1], p[2], p[3], p[4], p[5]]); n += 1
    f.flush(); print(tag, n, flush=True); time.sleep(1.0)
