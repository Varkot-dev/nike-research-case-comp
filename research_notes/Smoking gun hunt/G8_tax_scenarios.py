"""G8 tax and contingency scenarios. Regenerates G8_tax_scenarios.csv.
Run: python3 -I "research_notes/Smoking gun hunt/G8_tax_scenarios.py"
Inputs are typed in below with their source; every output row is DERIVED arithmetic.
"""
import csv, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "G8_tax_scenarios.csv")

# ---- FY28 reference cases (D1_fy28_bridge.md) ----
SHARES = 1488.0                      # D1 FY28 share count, millions
CONS_PRETAX = 3179.0 + 55.0          # D1: consensus FY28 EBIT 3,179 + net interest 55
BASE_PRETAX = 1.171 * SHARES / 0.75  # D1 Base EPS 1.171 at 25% tax -> pretax (DERIVED)
GUIDE_TAX = 0.25                     # "mid-20 percent range" (Q1 FY27 8-K Ex. 99.1)

# ---- Tax history (10-K income tax notes) ----
HIST = {  # fy: (pretax, tax)
    2019: (4801, 772), 2020: (2887, 348), 2021: (6661, 934),
    2022: (6651, 605), 2023: (6201, 1131), 2024: (6700, 1000),
    2025: (3885, 666), 2026: (3900, 792)}
rows = []

def add(group, scenario, driver, case, d_eps, note):
    rows.append(dict(group=group, scenario=scenario, driver=driver, case=case,
                     delta_eps_usd=round(d_eps, 3), note=note, tag="DERIVED"))

def eps_per_pt(pretax):  # 1 point of tax rate, $/share
    return pretax * 0.01 / SHARES

# ---- A. Tax-rate ladder vs the 25% guide ----
simple = sum(t / p for p, t in (HIST[y] for y in range(2019, 2025))) / 6 * 100
weighted = sum(HIST[y][1] for y in range(2019, 2025)) / sum(HIST[y][0] for y in range(2019, 2025)) * 100
for label, rate in [("FY2019-FY2024 simple mean", simple), ("FY2019-FY2024 pretax-weighted", weighted),
                    ("FY2025 actual 17.1", 17.1), ("FY2026 actual 20.3", 20.3),
                    ("Q1 FY2027 actual 22.7", 22.7), ("guide minus 1 point", 24.0),
                    ("guide plus 1 point", 26.0), ("guide plus 3 points", 28.0)]:
    for case, pt in (("consensus pretax", CONS_PRETAX), ("Base pretax", BASE_PRETAX)):
        add("A tax rate ladder", f"ETR {rate:.1f}% ({label})", "rate vs 25%", case,
            (GUIDE_TAX * 100 - rate) * eps_per_pt(pt),
            f"(25 - {rate:.1f}) pts x pretax {pt:,.0f} / 100 / {SHARES:,.0f}M shares; positive = EPS higher")

# ---- B. Pillar Two add-on ----
for pts in (1, 2, 3):
    for case, pt in (("consensus pretax", CONS_PRETAX), ("Base pretax", BASE_PRETAX)):
        add("B Pillar Two", f"+{pts} pt ETR", "top-up tax", case, -pts * eps_per_pt(pt),
            f"{pts} pt x pretax {pt:,.0f} = ${pts*pt/100:,.0f}M of extra tax")
print("Pillar Two 3 pts as share of FY26 tax-holiday benefit ($254M):", round(3 * CONS_PRETAX / 100 / 254, 2))

# ---- C. State aid (Netherlands) ----
NEON_EUR_B = [3.536, 3.735, 3.902, 3.686, 3.907, 4.394, 4.736, 5.528, 7.257, 8.401]  # FY07..FY16, opening decision Table 1
EURUSD_HIST = 1.30                               # ASSUMPTION, FY07-FY16 average
EMEA = {2017: 7970, 2018: 9242, 2019: 9812, 2020: 9347, 2021: 11456, 2022: 12479,
        2023: 13418, 2024: 13607, 2025: 12257, 2026: 12572}  # repo facts, revenue_emea, USD M
base07_16 = sum(NEON_EUR_B) * 1000 * EURUSD_HIST
thru22 = base07_16 + sum(EMEA[y] for y in range(2017, 2023))
thru26 = base07_16 + sum(EMEA.values())
print("revenue base FY07-FY16 $M", round(base07_16), "through FY22", round(thru22), "through FY26", round(thru26))
NL_RATE = 0.25
for cover, base in (("rulings through FY22", thru22), ("rulings through FY26", thru26)):
    for pts in (0.5, 1, 2, 3, 5):
        for us_off in (0.0, 0.5):
            gross = base * pts / 100 * NL_RATE
            with_int = gross * 1.30  # ASSUMPTION: recovery interest adds 30% of principal
            net = with_int * (1 - us_off)
            add("C state aid one-time", f"excess margin {pts} pt, {cover}, US offset {int(us_off*100)}%",
                "one-time charge in year booked", "FY28 if booked in FY28", -net / SHARES,
                f"base ${base:,.0f}M x {pts}% x {NL_RATE:.0%} NL rate = ${gross:,.0f}M, +30% interest = ${with_int:,.0f}M, x(1-{us_off:.0%})")
# prospective (annual) effect if rulings are withdrawn: FY28 EMEA revenue approx FY26
for pts in (1, 2, 3):
    gross = 12572 * pts / 100 * NL_RATE
    add("C state aid recurring", f"+{pts} pt Dutch margin on EMEA revenue", "annual tax", "FY28 recurring, no US offset",
        -gross / SHARES, f"$12,572M x {pts}% x 25% = ${gross:,.0f}M per year")

# ---- D. Belgian customs claim (press: EUR 1.5B total duties + VAT, De Tijd Sep 2024) ----
EURUSD = 1.15  # ASSUMPTION
total_eur = 1500.0
for duty_rate in (0.08, 0.12, 0.17):
    vat = 0.21
    value_gap = total_eur / (duty_rate + vat * (1 + duty_rate))   # EUR M undervalued, VAT on value + duty
    duty = value_gap * duty_rate
    vat_amt = total_eur - duty
    for vat_case, vat_cost in (("VAT fully recoverable", 0.0), ("VAT not recoverable (non-deductible)", vat_amt)):
        pre = (duty + vat_cost) * EURUSD
        after = duty * EURUSD * (1 - 0.25) + vat_cost * EURUSD  # duty deductible at 25%; VAT cost treated as non-deductible
        add("D Belgian customs one-time", f"duty rate {duty_rate:.0%}, {vat_case}", "one-time, excl. interest/penalties",
            "year booked", -after / SHARES,
            f"gap EUR {value_gap:,.0f}M; duty EUR {duty:,.0f}M, VAT EUR {vat_amt:,.0f}M; pretax ${pre:,.0f}M at {EURUSD}")
    annual_gap = value_gap / 7   # ASSUMPTION: claim spans about 7 fiscal years (FY18-FY24)
    add("D Belgian customs recurring", f"duty rate {duty_rate:.0%} on last-sale value", "annual duty if first-sale valuation must stop",
        "FY28 recurring", -(annual_gap * duty_rate * EURUSD * 0.75) / SHARES,
        f"EUR {annual_gap:,.0f}M undervalued per year x {duty_rate:.0%}, after 25% tax")

# ---- E. IEEPA ----
rec = 986.0
for tr in (0.21, 0.234):
    print(f"IEEPA benefit tax at {tr:.1%}: ${rec*tr:,.0f}M; after-tax per share ${rec*(1-tr)/1481:.3f}")
print("FY26 ex-IEEPA ETR at 23.4% on benefit:", round((792 - rec * 0.234) / (3900 - rec) * 100, 1))
print("simple mean", round(simple, 2), "weighted", round(weighted, 2))
print("eps per pt consensus", round(eps_per_pt(CONS_PRETAX), 4), "base", round(eps_per_pt(BASE_PRETAX), 4), "base pretax", round(BASE_PRETAX))

with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)
print("rows", len(rows), "->", OUT)
