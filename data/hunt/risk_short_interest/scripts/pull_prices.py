"""Daily adjusted closes and volume from the Yahoo chart API (free). Writes raw/px_<T>.json and prices_all.csv."""
import json, subprocess, sys, csv, pathlib, datetime as dt, time
HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
rows = []
for t in sys.argv[1:]:
    out = RAW / f"px_{t}.json"
    if not out.exists():
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?period1=1483228800&period2=1792000000&interval=1d&events=div"
        subprocess.run(["curl", "-sS", "-A", "Mozilla/5.0", url, "-o", str(out)], check=True); time.sleep(0.4)
    try:
        r = json.load(open(out))["chart"]["result"][0]
    except Exception:
        print("fail", t); continue
    ts = r["timestamp"]; q = r["indicators"]["quote"][0]; adj = r["indicators"]["adjclose"][0]["adjclose"]
    n = 0
    for i, s in enumerate(ts):
        if adj[i] is None or q["close"][i] is None: continue
        d = dt.datetime.utcfromtimestamp(s + r["meta"]["gmtoffset"]).date().isoformat()
        rows.append([t, d, round(q["close"][i], 4), round(adj[i], 4), q["volume"][i]]); n += 1
    print(t, n, rows[-1][1])
with open(HERE / "prices_all.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["ticker", "date", "close", "adj_close", "volume"]); w.writerows(rows)
