"""One careful Google Trends attempt (pytrends) for model-name interest, US, last 12 months weekly. Writes raw/gtrends_models.csv or logs the 429."""
import time, sys
try:
    from pytrends.request import TrendReq
except Exception as e:
    print("pytrends missing", e); sys.exit(0)
groups = [["nike pegasus", "hoka clifton", "brooks ghost", "asics novablast", "nike vomero"], ["on cloudmonster", "saucony ride", "new balance 880", "nike invincible", "adidas adizero"]]
import pandas as pd
out = []
for g in groups:
    try:
        t = TrendReq(hl="en-US", tz=360, timeout=(10, 30)); t.build_payload(g, timeframe="2024-10-01 2026-10-12", geo="US")
        d = t.interest_over_time().reset_index(); d["batch"] = "+".join(g[:2]); out.append(d); print("ok", g, len(d))
    except Exception as e:
        print("fail", g, str(e)[:120])
    time.sleep(60)
if out: pd.concat(out).to_csv("raw/gtrends_models.csv", index=False)
