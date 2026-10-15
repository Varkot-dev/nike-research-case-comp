"""Jordan Brand scenario valuation (illustrative; inputs are labelled assumptions, not forecasts).

Nike does not disclose Jordan profit, units or margin, so Jordan is valued as a scenario: a revenue path
from FY2026 to FY2031, a steady-state EBIT margin reached by FY2031, and a DCF on the same conventions as the
repo's reverse DCF (research_notes/thesis_tests/consensus_and_valuation.md, Section C): tax 22.5%, sales to
capital 2.5, terminal ROIC 20%, valuation date 2026-10-12, FY2027 pro-rated 0.63, mid-period discounting.

Inputs from files:
  data/nike_filing_facts.csv           Jordan FY2026 revenue (revenue_jordan_reported_basis), FY2024 peak,
                                        consolidated EBIT and revenue (for margin anchors)
  data/valuation/peer_multiples.csv     NKE price and diluted share count basis
  data/valuation/peer_ev_ebit_20261013.csv  peer EV/EBIT cross-check (Yahoo market data, Oct 13, 2026)
Output: data/valuation/jordan_scenarios.csv and data/valuation/jordan_sensitivity.csv
Run: python3 scripts/jordan_valuation.py
"""
import csv
import os
import statistics

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
FACTS = {(r["metric"], r["period"]): float(r["value"].replace(",", ""))
         for r in csv.DictReader(open(os.path.join(DATA, "nike_filing_facts.csv")))}

J26 = FACTS[("revenue_jordan_reported_basis", "FY2026")]
J24 = FACTS[("revenue_jordan_reported_basis", "FY2024")]
NKE_MARGIN_FY26 = FACTS[("ebit_total", "FY2026")] / FACTS[("revenues", "FY2026")]
NKE_MARGIN_FY24 = FACTS[("ebit_total", "FY2024")] / FACTS[("revenues", "FY2024")]
NKE = next(r for r in csv.DictReader(open(os.path.join(DATA, "valuation", "peer_multiples.csv"))) if r["ticker"] == "NKE")
PRICE = float(NKE["price"])

# Conventions shared with the repo's reverse DCF (consensus_and_valuation.md Section C)
SHARES_M = 1487.0      # diluted shares used there
TAX = 0.225
SALES_TO_CAPITAL = 2.5
ROIC_TERMINAL = 0.20
WACC = 0.10
M0 = 0.057             # FY2027 consolidated EBIT margin implied by consensus EPS (same note); Jordan starts here
YEARS = ["FY2027", "FY2028", "FY2029", "FY2030", "FY2031"]
T_MID = [0.63 / 2, 0.63 + 0.5, 1.63 + 0.5, 2.63 + 0.5, 3.63 + 0.5]   # years from 2026-10-12, mid-period
T_END = 4.63
FY27_WEIGHT = 0.63

# Scenario assumptions (ASSUMPTIONS, chosen to bracket the evidence in research_notes/12_jordan_brand_thesis.md)
# FY2027 -15% in all three: Q1 FY27 Jordan fell "by mid-teens" (Nike transcript, Oct 1, 2026).
SCEN = {
    "Bear: structural drag": dict(growth=[-0.15, -0.08, 0.00, 0.00, 0.00], margin=0.08, g=0.01),
    "Base: slow repair":     dict(growth=[-0.15, -0.03, 0.05, 0.05, 0.05], margin=0.11, g=0.025),
    "Bull: FY2018 replay":   dict(growth=[-0.15, 0.05, 0.12, 0.12, 0.10], margin=0.14, g=0.03),
}


def path(growth):
    out, r = [], J26
    for gr in growth:
        r *= 1 + gr
        out.append(r)
    return out


def value(revs, target_margin, g):
    margins = [M0 + (target_margin - M0) * i / 4 for i in range(5)]
    pv, prev = 0.0, J26
    for i, (rv, m) in enumerate(zip(revs, margins)):
        nopat = rv * m * (1 - TAX)
        reinv = max(rv - prev, 0) / SALES_TO_CAPITAL
        fcf = (nopat - reinv) * (FY27_WEIGHT if i == 0 else 1)
        pv += fcf / (1 + WACC) ** T_MID[i]
        prev = rv
    nopat_next = revs[-1] * margins[-1] * (1 - TAX) * (1 + g)
    tv = nopat_next * (1 - g / ROIC_TERMINAL) / (WACC - g)
    pv_tv = tv / (1 + WACC) ** T_END
    return pv + pv_tv, margins, pv_tv


rows = []
for name, s in SCEN.items():
    revs = path(s["growth"])
    ev, margins, pv_tv = value(revs, s["margin"], s["g"])
    ebit31 = revs[-1] * s["margin"]
    rows.append({
        "scenario": name,
        **{f"revenue_{y}_usd_m": round(r) for y, r in zip(YEARS, revs)},
        "fy2031_vs_fy2024_peak_pct": round((revs[-1] / J24 - 1) * 100, 1),
        "target_ebit_margin_fy2031": s["margin"],
        "terminal_growth": s["g"],
        "fy2031_ebit_usd_m": round(ebit31),
        "fy2031_eps_contribution_usd": round(ebit31 * (1 - TAX) / SHARES_M, 3),
        "dcf_value_usd_m": round(ev),
        "terminal_share_of_value_pct": round(pv_tv / ev * 100, 1),
        "value_per_nke_share_usd": round(ev / SHARES_M, 2),
        "share_of_nke_price_pct": round(ev / SHARES_M / PRICE * 100, 1),
        "basis": "ASSUMPTIONS for growth, margin and g; Jordan FY2026 revenue from FY26 10-K p. 32; DCF conventions from consensus_and_valuation.md Section C",
    })

# Reference points
ev_sales_nke = float(NKE["ev_sales_ttm"])
peers = [r for r in csv.DictReader(open(os.path.join(DATA, "valuation", "peer_ev_ebit_20261013.csv")))
         if r["ticker"] != "NKE" and r["ev_ebit"] not in ("", "nan")]
peer_med = statistics.median(float(r["ev_ebit"]) for r in peers)
rows.append({"scenario": "Reference: Jordan FY2026 revenue at NKE EV/Sales",
             "dcf_value_usd_m": round(J26 * ev_sales_nke),
             "value_per_nke_share_usd": round(J26 * ev_sales_nke / SHARES_M, 2),
             "share_of_nke_price_pct": round(J26 * ev_sales_nke / SHARES_M / PRICE * 100, 1),
             "basis": f"FY2026 Jordan revenue x NKE EV/Sales {ev_sales_nke} (peer_multiples.csv, Oct 13, 2026)"})
rows.append({"scenario": "Reference: peer median EV/EBIT",
             "basis": f"median EV/EBIT of {len(peers)} peers = {peer_med:.1f} (peer_ev_ebit_20261013.csv); NKE 14.6. "
                      f"Margin anchors: NKE EBIT margin FY2026 {NKE_MARGIN_FY26:.1%}, FY2024 {NKE_MARGIN_FY24:.1%} (my arithmetic on FY26 and FY24 10-K p. 31)"})

fields = list(dict.fromkeys(k for r in rows for k in r))
os.makedirs(os.path.join(DATA, "valuation"), exist_ok=True)
with open(os.path.join(DATA, "valuation", "jordan_scenarios.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(rows)

# Sensitivity: value per NKE share by revenue path x steady-state margin (terminal g held at each path's own g)
with open(os.path.join(DATA, "valuation", "jordan_sensitivity.csv"), "w", newline="") as f:
    w = csv.writer(f)
    margins = [0.06, 0.08, 0.11, 0.14, 0.17]
    w.writerow(["revenue_path"] + [f"margin_{int(m * 100)}pct_usd_per_share" for m in margins])
    for name, s in SCEN.items():
        revs = path(s["growth"])
        w.writerow([name] + [round(value(revs, m, s["g"])[0] / SHARES_M, 2) for m in margins])

for r in rows:
    print({k: r.get(k) for k in ("scenario", "revenue_FY2031_usd_m", "fy2031_ebit_usd_m", "fy2031_eps_contribution_usd",
                                 "dcf_value_usd_m", "value_per_nke_share_usd", "share_of_nke_price_pct", "terminal_share_of_value_pct")})
print("NKE EBIT margin FY26 %.3f FY24 %.3f; peer median EV/EBIT %.1f" % (NKE_MARGIN_FY26, NKE_MARGIN_FY24, peer_med))
