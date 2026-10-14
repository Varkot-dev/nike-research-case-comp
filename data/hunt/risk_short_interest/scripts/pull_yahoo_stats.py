"""Yahoo quoteSummary key stats (shares, float, short % of float, short ratio) for a ticker list. Writes yahoo_keystats_<date>.csv."""
import json, subprocess, sys, csv, pathlib, tempfile, time, datetime as dt
HERE = pathlib.Path(__file__).resolve().parent.parent
jar = tempfile.mkdtemp() + "/c.txt"
subprocess.run(["curl", "-sS", "-c", jar, "-A", "Mozilla/5.0", "https://fc.yahoo.com", "-o", "/dev/null"])
crumb = subprocess.run(["curl", "-sS", "-b", jar, "-A", "Mozilla/5.0", "https://query2.finance.yahoo.com/v1/test/getcrumb"], capture_output=True, text=True).stdout.strip()
F = ["sharesOutstanding", "floatShares", "impliedSharesOutstanding", "sharesShort", "shortRatio", "shortPercentOfFloat", "sharesPercentSharesOut", "dateShortInterest"]
S = ["averageVolume", "dividendYield", "marketCap"]
rows = []
for t in sys.argv[1:]:
    url = f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{t}?modules=defaultKeyStatistics,summaryDetail&crumb={crumb}"
    out = subprocess.run(["curl", "-sS", "-b", jar, "-A", "Mozilla/5.0", url], capture_output=True, text=True).stdout
    try:
        d = json.loads(out)["quoteSummary"]["result"][0]
    except Exception:
        print("fail", t); continue
    k, s = d["defaultKeyStatistics"], d["summaryDetail"]
    g = lambda o, x: (o.get(x) or {}).get("raw") if isinstance(o.get(x), dict) else o.get(x)
    rows.append([t] + [g(k, x) for x in F] + [g(s, x) for x in S]); time.sleep(0.3)
day = dt.date.today().isoformat()
with open(HERE / f"yahoo_keystats_{day}.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["ticker"] + F + S); w.writerows(rows)
print(len(rows))
