"""Pull ImportInfo.com monthly bill-of-lading chart JSON (public company pages; robots.txt allows company pages).
Only the ?monthly_chart endpoint is requested (HTML company pages returned HTTP 401 bot challenge on 2026-10-14).
Usage: python -I pull_importinfo_monthly.py <outdir> slug1 slug2 ...   ; 4 s sleep, skips existing files."""
import sys, os, time, urllib.request, urllib.error
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
UA = {'User-Agent': 'Mozilla/5.0 (academic research; low rate)'}
for slug in sys.argv[2:]:
    fn = os.path.join(out, slug + '_monthly.json')
    if os.path.exists(fn) and os.path.getsize(fn) > 20:
        continue
    try:
        with urllib.request.urlopen(urllib.request.Request(f'https://www.importinfo.com/{slug}?monthly_chart', headers=UA), timeout=60) as r:
            b = r.read(); code = r.status
    except urllib.error.HTTPError as e:
        b = b''; code = e.code
    except Exception as e:
        b = b''; code = str(e)
    if b and b.lstrip()[:1] == b'[':
        open(fn, 'wb').write(b)
    print(slug, code, len(b), flush=True)
    time.sleep(int(os.environ.get("SLEEP","4")))
