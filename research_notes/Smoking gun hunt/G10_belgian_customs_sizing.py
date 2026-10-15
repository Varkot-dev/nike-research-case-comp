"""G10 Belgian customs claim sizing. Regenerates G10_belgian_customs_sizing.csv.
Run: python3 -I "research_notes/Smoking gun hunt/G10_belgian_customs_sizing.py"
Method and inputs are those of G8_tax_scenarios.py (section D); every output is DERIVED arithmetic on a press figure.
"""
import csv, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "G10_belgian_customs_sizing.csv")

SHARES = 1488.0        # D1 FY28 share count, millions (as G8)
CONS_EPS = 1.646       # consensus FY28 EPS (task brief)
EURUSD = 1.15          # ASSUMPTION (as G8)
TOTAL_EUR = 1500.0     # PRESS: De Tijd Sep 2024; Belga 26 Feb 2026 repeats "about 1.5 billion"
TAX = 0.25             # guide "mid-20 percent range" (as G8)
VAT = 0.21             # Belgian standard VAT rate
CASH_STI_B = 9.0       # FY26 10-K: Cash and equivalents and Short-term investments, $ billions (OPENED)
GUAR_B = 1.3           # FY26 10-K p. 88: bank guarantees and letters of credit, about $1.3B (OPENED)
rows = []
def add(group, scenario, pretax_usd_m, aftertax_usd_m, note):
    rows.append(dict(group=group, scenario=scenario,
        pretax_usd_m=round(pretax_usd_m), aftertax_usd_m=round(aftertax_usd_m),
        eps_usd=round(-aftertax_usd_m / SHARES, 3),
        pct_of_fy28_consensus_eps=round(aftertax_usd_m / SHARES / CONS_EPS * 100, 1),
        cash_out_usd_m=round(note.get("cash", 0)), note=note["t"], tag="DERIVED"))

# A. Win: no P&L, no cash
add("A win", "Nike wins on the merits (or settles at zero)", 0, 0, {"cash": 0, "t": "guarantees released; no P&L"})

# B. Lose, duty only expensed, VAT recovered through VAT returns (G8 method)
for r in (0.08, 0.12, 0.17):
    gap = TOTAL_EUR / (r + VAT * (1 + r))          # EUR M undervalued customs value
    duty = gap * r; vat = TOTAL_EUR - duty
    pre = duty * EURUSD
    add("B lose, duty expensed, VAT recovered", f"duty rate {r:.0%}", pre, pre * (1 - TAX),
        {"cash": TOTAL_EUR * EURUSD, "t": f"gap EUR {gap:,.0f}M, duty EUR {duty:,.0f}M, VAT EUR {vat:,.0f}M; cash out is full EUR 1.5B, VAT part comes back with a lag"})

# C. Lose, duty plus VAT not recoverable (G8 method: duty deductible, VAT cost not)
for r in (0.08, 0.12, 0.17):
    gap = TOTAL_EUR / (r + VAT * (1 + r)); duty = gap * r; vat = TOTAL_EUR - duty
    pre = TOTAL_EUR * EURUSD
    add("C lose, VAT not recoverable", f"duty rate {r:.0%}", pre, duty * EURUSD * (1 - TAX) + vat * EURUSD,
        {"cash": pre, "t": "duty taxed at 25% shield; VAT cost no shield"})

# D. Lose and the EUR 1.5B already includes fines and interest: share p of the 1.5B is penalty (non-deductible)
for p in (0.25, 0.50):
    r = 0.12
    base = TOTAL_EUR * (1 - p)
    gap = base / (r + VAT * (1 + r)); duty = gap * r
    pre = (duty + TOTAL_EUR * p) * EURUSD
    add("D lose, penalties inside the 1.5B", f"{p:.0%} of EUR 1.5B is fines/interest, 12% duty, VAT recovered", pre,
        duty * EURUSD * (1 - TAX) + TOTAL_EUR * p * EURUSD,
        {"cash": TOTAL_EUR * EURUSD, "t": f"duty EUR {duty:,.0f}M + penalties EUR {TOTAL_EUR*p:,.0f}M (non-deductible, ASSUMPTION)"})

# E. Ceiling: whole EUR 1.5B expensed, no tax shield
add("E ceiling", "all EUR 1.5B expensed, no tax shield", TOTAL_EUR * EURUSD, TOTAL_EUR * EURUSD,
    {"cash": TOTAL_EUR * EURUSD, "t": "upper bound on one-time P&L"})

# F. Recurring if first-sale valuation must stop (G8 method, 7 fiscal years of claim)
for r in (0.08, 0.12, 0.17):
    gap = TOTAL_EUR / (r + VAT * (1 + r)); annual = gap / 7
    d = annual * r * EURUSD
    add("F recurring per year", f"duty rate {r:.0%} on last-sale value", d, d * (1 - TAX),
        {"cash": d, "t": f"EUR {annual:,.0f}M undervalued per year; only if Nike still uses first-sale values"})

# Checks
print("cash+STI share of $1.725B:", round(TOTAL_EUR * EURUSD / (CASH_STI_B * 1000) * 100, 1), "%")
print("guarantees $1.3B vs claim $", round(TOTAL_EUR * EURUSD), "M:", round(GUAR_B * 1000 / (TOTAL_EUR * EURUSD) * 100), "% covered")
# plausibility: implied undervaluation vs NRBV cost of inventories (Nike Retail BV FY24 accounts, EUR 6,165.8M)
gap12 = TOTAL_EUR / (0.12 + VAT * 1.12)
print("12% case gap EUR M", round(gap12), "per year (7 yrs)", round(gap12 / 7), "= % of NRBV FY24 cost of inventories 6,165.8:", round(gap12 / 7 / 6165.8 * 100, 1))
with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
for r in rows: print(r["group"], "|", r["scenario"], "|", r["pretax_usd_m"], r["aftertax_usd_m"], r["eps_usd"], r["pct_of_fy28_consensus_eps"], r["cash_out_usd_m"])
