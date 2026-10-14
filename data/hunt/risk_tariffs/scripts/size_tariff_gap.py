"""Size the gap between Nike's planned tariff rate (15% from Aug 2026) and the rate
actually in force (Section 301 forced-labor action: 10% / 12.5% from Jul 24, 2026).

Simple arithmetic only. Every input is labelled with where it came from.
Run: python3 -I size_tariff_gap.py  (writes ../tariff_gap_sizing.csv)
"""
import csv
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tariff_gap_sizing.csv")

# ---------- Inputs ----------
# Dutiable US-bound import value (FOB/customs value), USD bn per year.
# Method A: $1.5B annualized gross tariff (Q1 FY26 call, 2025-09-30) / ~20% blended IEEPA rate
#           (Vietnam 20, Indonesia 19, Cambodia 19, China ~20 after Nov 2025) = ~$7.5B.
# Method B: Q3 FY26 NA "nearly 650 basis points of gross impact from new U.S. tariffs"
#           (Q3 FY26 call, 2026-03-31) x NA Q3 FY26 revenue $5,026M = ~$327M/qtr = ~$1.31B/yr
#           / ~20% = ~$6.5B.
# FY27 volumes lower (revenue guided down high-single digits; NA buys tightened), so use a range.
base_low, base_mid, base_high = 6.0, 6.5, 7.5

# Blended incremental rate actually in force (USTR FRN 2026-15181; HTS 2026 Rev 21):
#   Vietnam 12.5 (9903.05.84), China 12.5 (9903.05.31, on top of legacy 301),
#   Indonesia 10 (9903.05.45), Cambodia 10 (9903.05.28), India/Bangladesh/Sri Lanka/Pakistan 10.
# US-bound mix assumption (FY26 10-K global mix, China cut for US footwear to high single digits):
footwear = {"Vietnam": (0.55, 12.5), "Indonesia": (0.30, 10.0), "China": (0.08, 12.5), "Other_10pct": (0.07, 10.0)}
apparel = {"Vietnam": (0.40, 12.5), "China": (0.08, 12.5), "Cambodia": (0.15, 10.0), "Other_10pct": (0.37, 10.0)}
fw_share = 0.65  # footwear share of US-bound import value (assumption; footwear ~2/3 of NIKE Brand revenue)


def blend(mix):
    return sum(w * r for w, r in mix.values()) / sum(w for w, _ in mix.values())


rate_fw = blend(footwear)
rate_ap = blend(apparel)
rate_actual = fw_share * rate_fw + (1 - fw_share) * rate_ap
rate_plan = 15.0  # Q4 FY26 call 2026-06-30: "10% ... through the end of July and then increasing to 15% thereafter"
gap_pts = rate_plan - rate_actual

# Pass-through: share of the duty saving Nike keeps in gross margin (some cost-sharing with
# factories / retail price actions may unwind). 70% to 100%.
keep_low, keep_high = 0.7, 1.0

# Timing. Plan and reality are identical through Jul 31 (10%). Gap applies to entries from Aug 1.
# Inventory: $7,846M at 2026-08-31 vs Q1 FY27 COGS $6,415M -> ~112 days on hand (~3.7 months).
dio_days = 7846 / (6415 * 4) * 365
lag_months = dio_days / 30.4
# FY27 ends May 31, 2027. Entries Aug 2026 onward reach COGS ~lag months later.
months_in_fy27_cogs = max(0.0, 10 - lag_months)  # Aug..May = 10 months of entries, minus lag

fy27_rev = 46.398 * (1 - 0.07)  # FY26 revenue $46,398M; guide "down high-single digits" -> ~-7%
fy28_rev = fy27_rev * 1.011     # consensus FY28 revenue ~+1.1% (expectations_gap.md)
tax = 0.215                     # "low 20% range" (Q4 FY26 call); Q1 FY27 ETR 22.7%
shares = 1.4842                 # bn diluted, Q1 FY27 10-Q

rows = []


def add(label, value, unit, note):
    rows.append({"item": label, "value": round(value, 4) if isinstance(value, float) else value, "unit": unit, "note": note})


add("blended_rate_footwear_actual", rate_fw, "pct", "US-bound mix assumption x FRN rates")
add("blended_rate_apparel_actual", rate_ap, "pct", "US-bound mix assumption x FRN rates")
add("blended_rate_actual", rate_actual, "pct", "65/35 footwear/apparel")
add("rate_plan", rate_plan, "pct", "Nike Q4 FY26 call 2026-06-30")
add("gap_pts", gap_pts, "pct pts", "plan minus actual")
add("dio_days", dio_days, "days", "inventory 2026-08-31 / annualized Q1 FY27 COGS")
add("lag_months", lag_months, "months", "entry to COGS")
add("fy27_months_of_benefit_in_cogs", months_in_fy27_cogs, "months", "Aug-May entries minus lag")

for name, base in (("low", base_low), ("mid", base_mid), ("high", base_high)):
    annual = base * gap_pts / 100  # $bn per year, gross
    for keep_name, keep in (("keep70", keep_low), ("keep100", keep_high)):
        fy27 = annual * keep * months_in_fy27_cogs / 12
        fy28 = annual * keep
        add(f"annual_gap_{name}_{keep_name}", annual * keep, "usd_bn", f"base {base}bn")
        add(f"fy27_gm_bps_{name}_{keep_name}", fy27 / fy27_rev * 1e4, "bps", "")
        add(f"fy27_eps_{name}_{keep_name}", fy27 * (1 - tax) / shares, "usd/share", "")
        add(f"fy28_gm_bps_{name}_{keep_name}", fy28 / fy28_rev * 1e4, "bps", "")
        add(f"fy28_eps_{name}_{keep_name}", fy28 * (1 - tax) / shares, "usd/share", "")

# Tail scenarios (one-off or regime changes), mid base, 100% kept
# 1) Section 122 refund: 10% on entries Feb 24 - Jul 23, 2026 (~5 months), only if CAFC affirms
#    AND relief reaches Nike (CIT judgment covers 3 named plaintiffs only).
s122 = base_mid * 0.10 * 5 / 12
add("tail_s122_refund_gross", s122, "usd_bn", "one-time; CIT 2026-05-07 ruling stayed by CAFC 2026-06-11")
add("tail_s122_refund_eps", s122 * (1 - tax) / shares, "usd/share", "one-time, likely excluded from adjusted EPS by market")
# 2) FLIP 301 struck down with no replacement: rate falls from ~11.5% to 0 incremental
flip = base_mid * rate_actual / 100
add("tail_flip301_vacated_annual", flip, "usd_bn", "annual, if no replacement")
add("tail_flip301_vacated_eps", flip * (1 - tax) / shares, "usd/share", "annual")
# 3) Excess-capacity 301 adds +7.5 pts (back to ~19-20%, the old IEEPA level) on all 4 countries
exc = base_mid * 0.075
add("tail_excess_capacity_plus7p5_annual", exc, "usd_bn", "annual cost, before mitigation")
add("tail_excess_capacity_plus7p5_eps", -exc * (1 - tax) / shares, "usd/share", "annual")
# 4) Y/Y tariff relief already in guidance: FY26 ex-refund gross tariffs ~$1.07-1.14B (tariffs_costs.md)
#    vs FY27 at ~11.5% on ~$6.5B = ~$0.75B -> y/y saving
fy27_cost = base_mid * rate_actual / 100
add("fy27_tariff_cost_at_actual", fy27_cost, "usd_bn", "full-year run rate at actual rates")
add("yoy_saving_vs_fy26_gross", 1.1 - fy27_cost, "usd_bn", "already embedded in Oct 1 guide if built on actual rates")

with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["item", "value", "unit", "note"])
    w.writeheader()
    w.writerows(rows)

for r in rows:
    print(f"{r['item']:40s} {r['value']:>10} {r['unit']:10s} {r['note']}")
