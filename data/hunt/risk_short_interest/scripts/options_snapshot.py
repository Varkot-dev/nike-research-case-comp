"""Yahoo v7 options snapshot for NKE: per expiry ATM IV, straddle-implied move, OI and volume put/call, 90% put vs 110% call IV (Yahoo IV).
Writes options_snapshot_<date>.csv."""
import json, subprocess, tempfile, csv, pathlib, datetime as dt
H = pathlib.Path(__file__).resolve().parent.parent
jar = tempfile.mkdtemp() + "/c.txt"
subprocess.run(["curl", "-sS", "-c", jar, "-A", "Mozilla/5.0", "https://fc.yahoo.com", "-o", "/dev/null"])
cr = subprocess.run(["curl", "-sS", "-b", jar, "-A", "Mozilla/5.0", "https://query2.finance.yahoo.com/v1/test/getcrumb"], capture_output=True, text=True).stdout.strip()
g = lambda u: json.loads(subprocess.run(["curl", "-sS", "-b", jar, "-A", "Mozilla/5.0", u + f"&crumb={cr}"], capture_output=True, text=True).stdout)
base = "https://query2.finance.yahoo.com/v7/finance/options/NKE?"
r0 = g(base + "x=1")["optionChain"]["result"][0]
S = r0["quote"]["regularMarketPrice"]; rows = []
tot = dict(poi=0, coi=0, pv=0, cv=0)
for e in r0["expirationDates"]:
    r = g(base + f"date={e}")["optionChain"]["result"][0]["options"][0]
    C, P = r["calls"], r["puts"]
    near = lambda L, k: min(L, key=lambda o: abs(o["strike"] - k)) if L else None
    c, p = near(C, S), near(P, S)
    mid = lambda o: (o.get("bid", 0) + o.get("ask", 0)) / 2 if o and o.get("ask") else (o or {}).get("lastPrice", 0)
    strad = mid(c) + mid(p)
    poi = sum(o.get("openInterest", 0) for o in P); coi = sum(o.get("openInterest", 0) for o in C)
    pv = sum(o.get("volume", 0) or 0 for o in P); cv = sum(o.get("volume", 0) or 0 for o in C)
    for k, v in (("poi", poi), ("coi", coi), ("pv", pv), ("cv", cv)): tot[k] += v
    p90, c110 = near(P, 0.9 * S), near(C, 1.1 * S)
    rows.append(dict(expiry=dt.datetime.utcfromtimestamp(e).date().isoformat(), spot=S, atm_strike=c["strike"] if c else None,
        atm_iv_call=round(100 * c["impliedVolatility"], 1) if c else None, atm_iv_put=round(100 * p["impliedVolatility"], 1) if p else None,
        straddle=round(strad, 2), straddle_pct=round(100 * strad / S, 1), put_oi=poi, call_oi=coi, pc_oi=round(poi / coi, 2) if coi else None,
        put_vol=pv, call_vol=cv, put90_iv=round(100 * p90["impliedVolatility"], 1) if p90 else None, call110_iv=round(100 * c110["impliedVolatility"], 1) if c110 else None))
day = dt.date.today().isoformat()
with open(H / f"options_snapshot_{day}.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
for x in rows[:10]: print(x)
print("spot", S, "total P/C OI", round(tot["poi"] / tot["coi"], 2), "vol P/C", round(tot["pv"] / max(tot["cv"], 1), 2), tot)
