"""EDGAR full-text search: other companies' 8-K filings (Item 5.02, officer/director appointments)
that mention a person's background "at <Company>". Counts distinct filings per year, excluding the
company's own filings, as a measure of how often that company's alumni are appointed elsewhere.
Usage: python3 -I pull_efts_talent.py OUTDIR"""
import sys, os, json, time, csv, urllib.request, urllib.parse
OUT = sys.argv[1]; UA = "NikeCaseCompResearch/1.0 research-contact@example.org"
TERMS = {'Nike': ('"at Nike"', '0000320187'), 'adidas': ('"at adidas"', None), 'Lululemon': ('"at lululemon"', '0001397187'),
         'Under Armour': ('"at Under Armour"', '0001336917'), 'Procter & Gamble': ('"at Procter & Gamble"', '0000080424'),
         'PepsiCo': ('"at PepsiCo"', '0000077476'), 'Starbucks': ('"at Starbucks"', '0000829224')}
hits_out = []; counts = []
for name, (q, owncik) in TERMS.items():
    for y in range(2015, 2027):
        end = f'{y}-12-31' if y < 2026 else '2026-10-14'
        seen = {}; frm = 0
        while True:
            url = 'https://efts.sec.gov/LATEST/search-index?' + urllib.parse.urlencode({'q': q, 'forms': '8-K', 'dateRange': 'custom', 'startdt': f'{y}-01-01', 'enddt': end, 'from': frm})
            for a in range(3):
                try: j = json.loads(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=60).read()); break
                except Exception as e: print('err', e); time.sleep(5)
            hs = j['hits']['hits']
            for h in hs:
                s = h['_source']
                if '5.02' not in (s.get('items') or []): continue
                if owncik and owncik in s['ciks']: continue
                seen.setdefault(s['adsh'], s)
            frm += len(hs); time.sleep(0.25)
            if not hs or frm >= j['hits']['total']['value'] or frm >= 1000: break
        counts.append(dict(term=name, year=y, filings_502=len(seen), total_hits_any_8k=j['hits']['total']['value']))
        if name == 'Nike':
            for a, s in seen.items(): hits_out.append(dict(year=y, file_date=s['file_date'], company=s['display_names'][0], adsh=a, items=','.join(s['items'])))
        print(name, y, len(seen), flush=True)
w = csv.DictWriter(open(os.path.join(OUT, 'efts_alumni_appointments_by_year.csv'), 'w', newline=''), fieldnames=list(counts[0])); w.writeheader(); w.writerows(counts)
w = csv.DictWriter(open(os.path.join(OUT, 'efts_nike_alumni_8k_hits.csv'), 'w', newline=''), fieldnames=list(hits_out[0])); w.writeheader(); w.writerows(sorted(hits_out, key=lambda r: r['file_date']))
