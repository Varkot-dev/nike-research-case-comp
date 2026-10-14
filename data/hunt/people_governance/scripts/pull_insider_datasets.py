"""Download SEC Insider Transactions Data Sets (Form 3/4/5 structured) quarter by quarter,
keep only rows for a peer list of footwear/apparel issuers, plus market-wide quarterly
aggregates of open-market purchases (P) and sales (S). Zips are deleted after parsing.
Usage: python3 -I pull_insider_datasets.py OUTDIR TMPDIR 2015q1 2026q3"""
import sys, os, io, csv, zipfile, time, re, urllib.request, collections
OUT, TMP, start, end = sys.argv[1:5]
UA = "NikeCaseCompResearch/1.0 research-contact@example.org"
TICK = set("NKE DECK LULU UAA UA SKX VFC CROX COLM FL TPR PVH RL LEVI HBI GPS GAP AEO ANF URBN DKS ASO BOOT WWW SHOO VRA CPRI ADDYY BIRK ONON".split())
idx = open(os.path.join(OUT, 'raw/insider_ds_index.html')).read()
links = dict((m.group(2), m.group(1)) for m in re.finditer(r'href="(/files/[^"]+/(\d{4}q\d)_form345\.zip)"', idx))
def qs():
    y, q = int(start[:4]), int(start[5]); ye, qe = int(end[:4]), int(end[5])
    while (y, q) <= (ye, qe):
        yield f"{y}q{q}"; q += 1
        if q == 5: y, q = y + 1, 1
csv.field_size_limit(10**8)
tx_out = os.path.join(OUT, 'raw/insider_ds_peer_nonderiv.csv')
agg_out = os.path.join(OUT, 'raw/insider_ds_market_agg.csv')
new = not os.path.exists(tx_out)
ftx = open(tx_out, 'a', newline=''); wtx = csv.writer(ftx)
fag = open(agg_out, 'a', newline=''); wag = csv.writer(fag)
if new:
    wtx.writerow(['dataset_q','accession','filing_date','doc_type','issuer_cik','issuer_name','ticker','owner_names','owner_rel','owner_title','trans_date','code','shares','price','acq_disp','shares_after','direct_indirect','equity_swap','trans_form_type'])
    wag.writerow(['dataset_q','n_issuers_P','n_filings_P','usd_P','n_issuers_S','n_filings_S','usd_S'])
done = set()
if not new:
    for r in csv.reader(open(agg_out)): done.add(r[0])
for q in qs():
    if q in done or q not in links: print('skip', q); continue
    url = 'https://www.sec.gov' + links[q]
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            data = urllib.request.urlopen(req, timeout=300).read(); break
        except Exception as e:
            print('retry', q, e); time.sleep(10)
    else:
        continue
    z = zipfile.ZipFile(io.BytesIO(data))
    def rd(name):
        n = [x for x in z.namelist() if x.upper().endswith(name)][0]
        return csv.DictReader(io.TextIOWrapper(z.open(n), encoding='utf-8', errors='replace'), delimiter='\t')
    sub = {}
    for r in rd('SUBMISSION.TSV'):
        sub[r['ACCESSION_NUMBER']] = r
    own = collections.defaultdict(list)
    for r in rd('REPORTINGOWNER.TSV'):
        own[r['ACCESSION_NUMBER']].append(r)
    aggP = collections.defaultdict(float); aggS = collections.defaultdict(float); fP=set(); fS=set()
    for r in rd('NONDERIV_TRANS.TSV'):
        a = r['ACCESSION_NUMBER']; s = sub.get(a)
        if not s: continue
        code = r.get('TRANS_CODE', '')
        try: v = float(r['TRANS_SHARES'] or 0) * float(r['TRANS_PRICEPERSHARE'] or 0)
        except: v = 0
        if code == 'P': aggP[s['ISSUERCIK']] += v; fP.add(a)
        if code == 'S': aggS[s['ISSUERCIK']] += v; fS.add(a)
        t = (s.get('ISSUERTRADINGSYMBOL') or '').upper().strip()
        if t in TICK:
            o = own.get(a, [])
            wtx.writerow([q, a, s['FILING_DATE'], s['DOCUMENT_TYPE'], s['ISSUERCIK'], s['ISSUERNAME'], t,
                          '|'.join(x['RPTOWNERNAME'] for x in o), '|'.join(x.get('RPTOWNER_RELATIONSHIP','') for x in o),
                          '|'.join(x.get('RPTOWNER_TITLE','') for x in o), r['TRANS_DATE'], code, r['TRANS_SHARES'],
                          r['TRANS_PRICEPERSHARE'], r['TRANS_ACQUIRED_DISP_CD'], r.get('SHRS_OWND_FOLWNG_TRANS',''),
                          r.get('DIRECT_INDIRECT_OWNERSHIP',''), r.get('EQUITY_SWAP_INVOLVED',''), r.get('TRANS_FORM_TYPE','')])
    wag.writerow([q, len(aggP), len(fP), round(sum(aggP.values())), len(aggS), len(fS), round(sum(aggS.values()))])
    ftx.flush(); fag.flush(); print(q, len(data)//1e6, 'MB', len(aggP), len(aggS), flush=True)
    time.sleep(1.5)
