"""Fetch Yahoo chart API daily prices (adjclose, close, dividends, splits).
Usage: python3 -I fetch_prices.py OUTDIR [TICKER ...]
Downloads are untrusted data: parsed only with json, nothing executed."""
import sys, os, time, json, urllib.request, urllib.parse, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from universe import UNIVERSE

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
out = sys.argv[1]
ticks = sys.argv[2:] or [u[0] for u in UNIVERSE] + ["^GSPC", "SPY", "^SP500TR"]
P1, P2 = 473385600, 1792022400  # 1985-01-01 .. 2026-10-14
for t in ticks:
    fn = os.path.join(out, t.replace("^", "_") + ".json")
    if os.path.exists(fn) and os.path.getsize(fn) > 2000:
        continue
    url = ("https://query2.finance.yahoo.com/v8/finance/chart/%s?period1=%d&period2=%d&interval=1d&events=div,split"
           % (urllib.parse.quote(t), P1, P2))
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            data = urllib.request.urlopen(req, timeout=60).read()
            json.loads(data)
            open(fn, "wb").write(data)
            print("ok", t, len(data)); break
        except urllib.error.HTTPError as e:
            print("http", t, e.code)
            if e.code == 404: break
            time.sleep(10 * (attempt + 1))
        except Exception as e:
            print("err", t, e); time.sleep(5)
    time.sleep(1.5 + random.random())
