"""Fetch SEC companyfacts XBRL JSON for universe CIKs.
Usage: python3 -I fetch_sec.py OUTDIR
User-Agent comes from the SEC_USER_AGENT environment variable; sent only to data.sec.gov."""
import sys, os, time, json, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from universe import UNIVERSE
UA = os.environ["SEC_USER_AGENT"]
out = sys.argv[1]
for tk, name, sec, cik in UNIVERSE:
    if not cik: continue
    fn = os.path.join(out, f"{tk}.json")
    if os.path.exists(fn) and os.path.getsize(fn) > 5000: continue
    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
        d = urllib.request.urlopen(req, timeout=60).read()
        j = json.loads(d)
        open(fn, "wb").write(d)
        print("ok", tk, cik, j.get("entityName"))
    except Exception as e:
        print("err", tk, cik, e)
    time.sleep(0.4)
