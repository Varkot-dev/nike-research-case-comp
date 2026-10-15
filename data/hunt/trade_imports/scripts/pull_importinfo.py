"""Pull public ImportInfo.com company pages and their monthly bill-of-lading chart JSON.
Public, no login. robots.txt allows company pages (disallows /search, /manifest, /login).
Usage: python pull_importinfo.py slug1 slug2 ...
Saves raw/importinfo/<slug>.html and raw/importinfo/<slug>_monthly.json"""
import sys, os, time, urllib.request

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'raw', 'importinfo')
os.makedirs(out, exist_ok=True)
UA = {'User-Agent': 'Mozilla/5.0 (academic research; low rate)'}


def get(url):
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception as e:
            print('retry', url, e, flush=True)
            time.sleep(10)
    return None


for slug in sys.argv[1:]:
    for suffix, fn in (('', f'{slug}.html'), ('?monthly_chart', f'{slug}_monthly.json')):
        path = os.path.join(out, fn)
        if os.path.exists(path) and os.path.getsize(path) > 50:
            continue
        b = get(f'https://www.importinfo.com/{slug}{suffix}')
        if b:
            open(path, 'wb').write(b)
            print(slug, suffix or 'page', len(b), flush=True)
        time.sleep(3)
