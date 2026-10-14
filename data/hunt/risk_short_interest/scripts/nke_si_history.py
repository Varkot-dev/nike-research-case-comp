"""NKE short interest, Dec 2017 to Sep 2026: % of Class B (the only traded class), % of all shares, FINRA days to cover,
days to cover on Yahoo consolidated 20-day volume, and short dollar value. Share counts are 10-K / 10-Q cover values from
data/nike_filing_facts.csv (class A + class B), held constant until the next filing; before Jul 2019 we use FY18 balance
sheet counts (Class B 1,272M, FY19 10-K p. 52; Class A 315M)."""
import csv, pathlib, bisect, collections
H = pathlib.Path(__file__).resolve().parent.parent
F = H.parent.parent / "nike_filing_facts.csv"
B, A = [("2017-01-01", 1272e6)], [("2017-01-01", 315e6)]
for r in csv.DictReader(open(F)):
    if r["metric"] == "class_b_shares_outstanding": B.append((r["period"], float(r["value"])))
    if r["metric"] == "class_a_shares_outstanding": A.append((r["period"], float(r["value"])))
B.sort(); A.sort()
asof = lambda L, d: L[bisect.bisect_right([x[0] for x in L], d) - 1][1]
px = [r for r in csv.DictReader(open(H / "prices_all.csv")) if r["ticker"] == "NKE"]
D = [r["date"] for r in px]; C = [float(r["close"]) for r in px]; V = [int(r["volume"]) for r in px]
out = []
for r in csv.DictReader(open(H / "si_all.csv")):
    if r["ticker"] != "NKE": continue
    d = r["settlement_date"]; s = int(r["short_shares"]); i = bisect.bisect_right(D, d) - 1
    adv20 = sum(V[i - 19:i + 1]) / 20
    b, a = asof(B, d), asof(A, d)
    out.append(dict(settlement_date=d, short_shares=s, pct_classB=round(100 * s / b, 2), pct_all_shares=round(100 * s / (a + b), 2),
                    finra_adv=r["finra_adv"], finra_dtc=r["finra_days_to_cover"], yahoo_adv20=round(adv20), dtc_yahoo20=round(s / adv20, 2),
                    nke_close=C[i], short_value_usd_bn=round(s * C[i] / 1e9, 2)))
with open(H / "nke_short_interest_2017_2026.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
mx = max(out, key=lambda r: r["pct_classB"]); print("max", mx)
print("max dtc_yahoo20", max(out, key=lambda r: r["dtc_yahoo20"]))
print("max finra dtc", max(out, key=lambda r: float(r["finra_dtc"])))
for y in range(2018, 2027):
    L = [r for r in out if r["settlement_date"].startswith(str(y))]
    print(y, "pctB range", min(r["pct_classB"] for r in L), max(r["pct_classB"] for r in L), "median dtc20", sorted(r["dtc_yahoo20"] for r in L)[len(L) // 2])
for r in out[-8:]: print(r)
