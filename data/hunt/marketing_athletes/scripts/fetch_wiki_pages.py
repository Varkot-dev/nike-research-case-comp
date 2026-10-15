"""Fetch a list of Wikipedia pages (REST HTML) into rawdir with polite backoff. Usage: fetch_wiki_pages.py <rawdir> <title>..."""
import sys, os, re, time, urllib.request, urllib.parse
UA = {"User-Agent": "nike-research-casecomp/1.0 (student research)"}
RAW = sys.argv[1]
for title in sys.argv[2:]:
    fn = os.path.join(RAW, re.sub(r'[^A-Za-z0-9]+', '_', title) + ".html")
    if os.path.exists(fn): continue
    url = "https://en.wikipedia.org/api/rest_v1/page/html/" + urllib.parse.quote(title.replace(" ", "_"))
    for k in range(6):
        try:
            open(fn, "wb").write(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()); print("ok", title, flush=True); break
        except Exception as e:
            if "404" in str(e): print("404", title, flush=True); break
            time.sleep(20 * (k + 1))
    time.sleep(4)
