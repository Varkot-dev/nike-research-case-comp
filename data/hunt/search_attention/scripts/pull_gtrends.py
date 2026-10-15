"""Google Trends pulls via pytrends (no login). Each batch saved as its own raw CSV.

Re-run: python3 -I pull_gtrends.py <rawdir>
Batches already on disk are skipped. Sleeps 45 s between requests; on any error waits 70 s and retries (max 5).
These batches are NEW versus data/altdata/gtrends_* on branch claude/wonderful-franklin-u31n4e:
weekly 5-year resolution, search intent (sale / outlet / promo), product level running and lifestyle
terms, YouTube and Google Shopping properties, and non-US country geos.
"""
import os, sys, time
from pytrends.request import TrendReq

OUT = sys.argv[1] if len(sys.argv) > 1 else "../raw/gtrends"
os.makedirs(OUT, exist_ok=True)
WEEKLY = "2021-10-17 2026-10-13"  # under 5 years -> weekly points
MONTHLY = "2019-01-01 2026-10-13"

BATCHES = []
# 0. Cross-brand sale intent without the brand term (the brand term dwarfs the sale terms; integer rounding
#    makes within-brand ratios useless, see intent_* batches). Anchored on "nike sale" so values are comparable.
BATCHES.append(("sale_cross", ["nike sale", "adidas sale", "new balance sale", "hoka sale", "nike outlet"], WEEKLY, "US", ""))
BATCHES.append(("sale_cross2", ["nike sale", "asics sale", "on running sale", "nike clearance", "adidas outlet"], WEEKLY, "US", ""))
BATCHES.append(("brands_weekly_US", ["nike", "adidas", "new balance", "hoka", "asics"], WEEKLY, "US", ""))
BATCHES.append(("run_products", ["nike pegasus", "nike vomero", "hoka clifton", "asics novablast", "on cloudmonster"], WEEKLY, "US", ""))
BATCHES.append(("life_products", ["adidas samba", "nike dunk", "air force 1", "onitsuka tiger", "nike air max"], WEEKLY, "US", ""))
# 1. Discount intent within each brand (ratio inside one request is precise)
for b in ["nike", "adidas", "new balance", "hoka", "asics"]:
    BATCHES.append((f"intent_{b.replace(' ', '_')}", [b, f"{b} sale", f"{b} outlet", f"{b} promo code"], WEEKLY, "US", ""))
# 2. Running product level
BATCHES.append(("run_products", ["nike pegasus", "nike vomero", "hoka clifton", "asics novablast", "on cloudmonster"], WEEKLY, "US", ""))
BATCHES.append(("run_generic", ["running shoes", "nike running shoes", "hoka shoes", "asics shoes", "brooks shoes"], WEEKLY, "US", ""))
# 3. Lifestyle product level
BATCHES.append(("life_products", ["adidas samba", "nike dunk", "air force 1", "onitsuka tiger", "nike air max"], WEEKLY, "US", ""))
BATCHES.append(("life_products2", ["adidas samba", "jordan 1", "nike cortez", "new balance 9060", "adidas gazelle"], WEEKLY, "US", ""))
# 4. Other Google properties: YouTube search and Google Shopping search
for prop in ["youtube", "froogle"]:
    BATCHES.append((f"prop_{prop}", ["nike", "adidas", "new balance", "hoka", "asics"], MONTHLY, "US", prop))
# 5. Investor / news attention
BATCHES.append(("investor", ["nike stock", "adidas stock", "lululemon stock", "on holding stock", "deckers stock"], WEEKLY, "US", ""))
# 6. Country geos, brand share, monthly since 2019
for g in ["GB", "DE", "FR", "JP", "KR", "AU", "CA", "IN", "MX", "BR", "TW", "HK"]:
    BATCHES.append((f"geo_{g}", ["nike", "adidas", "new balance", "asics", "puma"], MONTHLY, g, ""))
# 7. Weekly brand share US and world (higher resolution than the existing monthly pull)
for g in ["US", ""]:
    BATCHES.append((f"brands_weekly_{g or 'WORLD'}", ["nike", "adidas", "new balance", "hoka", "asics"], WEEKLY, g, ""))
    BATCHES.append((f"brands2_weekly_{g or 'WORLD'}", ["nike", "on running", "on cloud", "lululemon", "puma"], WEEKLY, g, ""))

done_names = set(f[:-4] for f in os.listdir(OUT))
for name, kw, tf, geo, prop in BATCHES:
    if os.path.exists(os.path.join(OUT, name + ".csv")):
        continue
    for attempt in range(5):
        try:
            p = TrendReq(hl="en-US", tz=0, timeout=(10, 40), requests_args={"verify": "/root/.ccr/ca-bundle.crt"})
            p.build_payload(kw, timeframe=tf, geo=geo, gprop=prop)
            df = p.interest_over_time()
            df.to_csv(os.path.join(OUT, name + ".csv"))
            print("OK", name, len(df), flush=True)
            break
        except Exception as e:
            print("ERR", name, type(e).__name__, str(e)[:120], flush=True)
            time.sleep(70)
    time.sleep(45)
print("DONE", flush=True)
