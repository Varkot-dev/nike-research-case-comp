"""Google Trends (pytrends, no login): app and site navigation searches. Sleeps 45 s between requests.
Raw: raw/gtrends_apps/<batch>.csv
"""
import os, time
from pytrends.request import TrendReq
OUT = "/home/user/nike-research-case-comp/data/hunt/apps_digital/raw/gtrends_apps"; os.makedirs(OUT, exist_ok=True)
M = "2019-01-01 2026-10-13"; W = "2021-10-17 2026-10-13"
B = [("apps_monthly_US", ["snkrs", "nike app", "nike run club", "adidas app", "stockx"], M, "US", ""),
     ("apps_weekly_US", ["snkrs", "nike app", "nike run club", "adidas app", "stockx"], W, "US", ""),
     ("nav_monthly_US", ["nike.com", "adidas.com", "hoka.com", "nike app", "snkrs"], M, "US", ""),
     ("apps_monthly_WORLD", ["snkrs", "nike app", "nike run club", "adidas app", "stockx"], M, "", ""),
     ("snkrs_vs_resale_US", ["snkrs", "stockx", "goat app", "confirmed app", "nike launch"], M, "US", ""),
     ("apps_monthly_GB", ["snkrs", "nike app", "nike run club", "adidas app", "stockx"], M, "GB", ""),
     ("apps_monthly_JP", ["snkrs", "nike app", "nike run club", "adidas app", "stockx"], M, "JP", "")]
for name, kw, tf, geo, prop in B:
    fn = os.path.join(OUT, name + ".csv")
    if os.path.exists(fn): continue
    for a in range(5):
        try:
            p = TrendReq(hl="en-US", tz=0, timeout=(10, 40), requests_args={"verify": "/root/.ccr/ca-bundle.crt"})
            p.build_payload(kw, timeframe=tf, geo=geo, gprop=prop)
            df = p.interest_over_time(); df.to_csv(fn); print("OK", name, len(df), flush=True); break
        except Exception as e:
            print("ERR", name, type(e).__name__, str(e)[:120], flush=True); time.sleep(70)
    time.sleep(45)
