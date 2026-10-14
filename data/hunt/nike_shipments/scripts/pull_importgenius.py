"""Pull public ImportGenius company pages (US customs BOL data, and Vietnam/India pages).
robots.txt (checked 2026-10-14) allows all paths except /search. No login, no cookies, no personal data sent.
Usage: python -I pull_importgenius.py <outdir> path1 path2 ...   (path like importers/nike-usa-inc or suppliers/feng-tay-enterprises-co-ltd)
Saves <outdir>/<path with / -> __>.html ; 4 s sleep between requests."""
import sys, os, time, urllib.request, urllib.error
out = sys.argv[1]
os.makedirs(out, exist_ok=True)
UA = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'}
for p in sys.argv[2:]:
    fn = os.path.join(out, p.replace('/', '__') + '.html')
    if os.path.exists(fn) and os.path.getsize(fn) > 1000:
        continue
    url = 'https://www.importgenius.com/' + p
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90) as r:
            b = r.read(); code = r.status
    except urllib.error.HTTPError as e:
        b = b''; code = e.code
    except Exception as e:
        b = b''; code = str(e)
    if b:
        open(fn, 'wb').write(b)
    print(p, code, len(b), flush=True)
    time.sleep(4)
