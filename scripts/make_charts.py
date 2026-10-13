"""Builds every report chart from data that can be traced to a source.

Financial data: data/nike_filing_facts.csv (one row per metric and period, each with the SEC
filing, printed page, URL and a verbatim quote). Market data: data/nke_daily_prices.csv
(Yahoo Finance chart API, pulled 2026-10-12). People data: data/people_events.csv.
Run: pip install matplotlib && python3 scripts/make_charts.py
"""
import csv
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
OUT = os.path.join(ROOT, "charts")
os.makedirs(OUT, exist_ok=True)

# Reference categorical palette (fixed order) plus text and grid inks
BLUE, ORANGE, AQUA, YELLOW, MAGENTA, GREEN, VIOLET, RED = (
    "#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948")
INK, INK2, MUTED, GRID = "#0b0b0b", "#52514e", "#8a8984", "#e4e3df"
plt.rcParams.update({
    "font.size": 10, "axes.spines.top": False, "axes.spines.right": False,
    "axes.edgecolor": MUTED, "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK2,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6, "axes.axisbelow": True,
    "axes.titleweight": "bold", "axes.titlesize": 11, "axes.titlecolor": INK,
    "figure.dpi": 130, "text.parse_math": False, "savefig.bbox": "tight", "figure.facecolor": "white"})

FACTS = {(r["metric"], r["period"]): r for r in csv.DictReader(open(os.path.join(DATA, "nike_filing_facts.csv")))}


def v(metric, period):
    """Value of a filing fact; raises if missing so no chart silently plots an unsourced number."""
    return float(FACTS[(metric, period)]["value"].replace(",", ""))


def note(fig, text, y=-0.02):
    fig.text(0.01, y, text, fontsize=7, color=INK2, va="top", wrap=True)


def save(name):
    plt.savefig(os.path.join(OUT, name))
    plt.close()


YEARS = list(range(2019, 2027))
FY = [f"FY{y}" for y in YEARS]
FYL = [f"FY{str(y)[2:]}" for y in YEARS]
QTRS = [f"Q{q}FY{y}" for y in (2024, 2025, 2026) for q in (1, 2, 3, 4)] + ["Q1FY2027"]
QL = [f"Q{p[1]} FY{p[-2:]}" for p in QTRS]
K = "Sources: Nike Form 10-K for each fiscal year (income statement, MD&A); see data/nike_filing_facts.csv for page-level citations."

# ---------- 1. Annual revenue and gross margin (two panels, one axis each) ----------
rev = [v("revenues", p) / 1000 for p in FY]
gm = [v("gross_margin_pct", p) for p in FY]
fig, (a1, a2) = plt.subplots(2, 1, figsize=(8, 6.2), sharex=True, gridspec_kw={"height_ratios": [3, 2], "hspace": 0.25})
a1.bar(FYL, rev, color=BLUE, width=0.62)
for x, r in zip(FYL, rev):
    a1.text(x, r + 0.7, f"{r:.1f}", ha="center", fontsize=8.5, color=INK2)
a1.set_ylim(0, 60); a1.set_ylabel("Revenue ($ billions)")
a1.set_title("Revenue peaked at $51.4B in FY24, fell 10% in FY25 and was flat in FY26")
a2.plot(FYL, gm, color=ORANGE, lw=2, marker="o", ms=6)
for x, g in zip(FYL, gm):
    a2.text(x, g + 0.35, f"{g:.1f}%", ha="center", fontsize=8.5, color=INK2)
a2.set_ylim(41, 47.5); a2.set_ylabel("Gross margin (%)")
note(fig, K + " FY26 gross margin includes the Q4 IEEPA tariff recovery benefit (FY26 Q4 earnings release, p. 1).")
save("01_annual_revenue_margin.png")

# ---------- 2. Diluted EPS and FY27 guidance ----------
eps = [v("eps_diluted", p) for p in FY]
fig, ax = plt.subplots(figsize=(8.4, 4.4))
ax.bar(FYL, eps, color=BLUE, width=0.62)
for x, e in zip(FYL, eps):
    ax.text(x, e + 0.08, f"${e:.2f}", ha="center", fontsize=8.5, color=INK2)
ax.bar(["FY27 guide"], [1.35 - 1.15], bottom=1.15, color=ORANGE, width=0.62, alpha=0.85)
ax.text("FY27 guide", 1.42, "$1.15 to $1.35\n(adjusted)", ha="center", fontsize=8.5, color=INK2)
ax.set_ylim(0, 4.3); ax.set_ylabel("Diluted EPS ($)")
ax.set_title("Diluted EPS fell 44% from FY24 to FY26; FY27 guidance points lower again")
note(fig, "FY19 to FY26: diluted EPS from each year's Form 10-K. FY26 includes a $0.52 benefit in Q4 from the expected IEEPA tariff recovery "
          "(Q4 FY26 earnings release, 8-K Ex. 99.1, p. 1). FY27: adjusted diluted EPS outlook of $1.15 to $1.35, excluding about $0.15 of Pace "
          "restructuring expense (Q1 FY27 earnings release, 8-K Ex. 99.1, p. 1). Adjusted EPS is a non-GAAP measure and is not directly comparable to the bars.")
save("02_eps_and_guidance.png")

# ---------- 3. Quarterly revenue and gross margin (two panels) ----------
qrev = [v("revenues", p) / 1000 for p in QTRS]
qgm = [v("gross_margin_pct", p) for p in QTRS]
q4_26_ex = (v("gross_profit", "Q4FY2026") - 986) / v("revenues", "Q4FY2026") * 100
fig, (a1, a2) = plt.subplots(2, 1, figsize=(10.5, 6.4), sharex=True, gridspec_kw={"height_ratios": [3, 2], "hspace": 0.25})
a1.bar(QL, qrev, color=BLUE, width=0.62)
for x, r in zip(QL, qrev):
    a1.text(x, r + 0.2, f"{r:.1f}", ha="center", fontsize=7.5, color=INK2)
a1.set_ylim(0, 15.5); a1.set_ylabel("Revenue ($ billions)")
a1.set_title("Quarterly revenue has held near $11B to $12.5B since FY25; margin is in the low 40s outside the one-time Q4 FY26 benefit")
a2.plot(QL, qgm, color=ORANGE, lw=2, marker="o", ms=6, label="Reported gross margin")
a2.plot([QL[11]], [q4_26_ex], marker="o", ms=7, mfc="white", mec=ORANGE, mew=2, ls="none", label="Q4 FY26 excluding $986M IEEPA benefit (derived)")
a2.annotate(f"49.2% reported\n{q4_26_ex:.1f}% without IEEPA", xy=(11, 49.2), xytext=(8.3, 48.0), fontsize=7.5, color=INK2,
            arrowprops=dict(arrowstyle="-", color=MUTED))
a2.set_ylim(38, 51); a2.set_ylabel("Gross margin (%)")
a2.legend(frameon=False, fontsize=7.5, loc="lower left")
plt.setp(a2.get_xticklabels(), rotation=0, fontsize=8)
note(fig, "Q1 to Q3: each quarter's Form 10-Q (income statement, p. 1). Q4: each year's Q4 earnings release (8-K Ex. 99.1, income statement, p. 2). "
          f"Q4 FY26 ex-IEEPA margin is derived: (gross profit $5,393M minus $986M) / revenue $10,972M = {q4_26_ex:.1f}% (Q4 FY26 release, pp. 1 to 2).", y=-0.0)
save("03_quarterly.png")

# ---------- 4. Revenue by geography (lines, direct-labelled) ----------
geo = [("North America", "revenue_north_america", BLUE), ("EMEA", "revenue_emea", ORANGE),
       ("Greater China", "revenue_greater_china", AQUA), ("APLA", "revenue_apla", YELLOW), ("Converse", "revenue_converse", MAGENTA)]
fig, ax = plt.subplots(figsize=(8.8, 4.8))
for name, m, c in geo:
    ys = [v(m, p) / 1000 for p in FY]
    ax.plot(FYL, ys, color=c, lw=2, marker="o", ms=5, label=name)
    nudge = {"APLA": 0.35, "Greater China": -0.35}.get(name, 0)
    ax.text(len(FYL) - 1 + 0.12, ys[-1] + nudge, f"{name} {ys[-1]:.1f}", va="center", fontsize=8, color=INK2)
ax.set_xlim(-0.3, len(FYL) + 1.1); ax.set_ylim(0, 23); ax.set_ylabel("Revenue ($ billions)")
ax.legend(frameon=False, fontsize=8, ncol=5, loc="upper left")
ax.set_title("Greater China is below its FY19 level and Converse revenue has halved since FY23 (-52%)")
note(fig, "Reported revenues by operating segment. Each year from that year's Form 10-K (Note on operating segments and MD&A tables); "
          "page-level citations in data/nike_filing_facts.csv.")
save("04_geography.png")

# ---------- 5. Share price (daily closes) ----------
px = list(csv.DictReader(open(os.path.join(DATA, "nke_daily_prices.csv"))))
dates = [r["date"] for r in px]
closes = [float(r["close_usd"]) for r in px]
fig, ax = plt.subplots(figsize=(9.6, 4.6))
ax.plot(range(len(dates)), closes, color=BLUE, lw=2)
ticks = [next(i for i, d in enumerate(dates) if d.startswith(str(y))) for y in range(2019, 2027)]
ax.set_xticks(ticks); ax.set_xticklabels([dates[i][:4] for i in ticks])
peak_i = max(range(len(closes)), key=lambda i: closes[i])
ax.annotate("Record close $177.51\n(Nov 5, 2021)", xy=(peak_i, closes[peak_i]), xytext=(peak_i + 120, 176), fontsize=8, color=INK2,
            arrowprops=dict(arrowstyle="-", color=MUTED))
ax.annotate("$35.35 (Oct 12, 2026)", xy=(len(closes) - 1, closes[-1]), xytext=(len(closes) - 420, 18), fontsize=8, color=INK2,
            arrowprops=dict(arrowstyle="-", color=MUTED))
for d, lab in [("2024-09", "Hill named CEO\n(Sep 19, 2024)")]:
    i = next(i for i, x in enumerate(dates) if x.startswith(d))
    ax.axvline(i, color=MUTED, lw=0.8); ax.text(i + 12, 150, lab, fontsize=8, color=INK2)
ax.set_ylim(0, 195); ax.set_ylabel("Share price, daily close ($)")
ax.set_title("NKE closed 80% below its 2021 record on Oct 12, 2026")
note(fig, "Market data, not from SEC filings: daily NYSE closes from the Yahoo Finance chart API (pulled Oct 12, 2026), the last point is the Oct 12, 2026 close. Prices are not adjusted for dividends. Data: data/nke_daily_prices.csv.")
save("05_stock_price.png")

# ---------- 6 and 7. Senior executive exits (people data) ----------
people = list(csv.DictReader(open(os.path.join(DATA, "people_events.csv"))))
people.sort(key=lambda r: r["month"])
def tx(s):
    y, m = s.split("-"); return int(y) + (int(m) - 1) / 12
HILL = tx("2024-10")
fig, ax = plt.subplots(figsize=(11, 0.36 * len(people) + 1.4))
n = len(people)
for i, r in enumerate(people):
    y = n - 1 - i; xx = tx(r["month"]); c = ORANGE if xx >= HILL else BLUE
    ax.plot(xx, y, "o", color=c, ms=8)
    ax.text(xx + 0.1, y, f"{r['name']}: {r['role']} ({r['type']})", va="center", fontsize=8, color=INK)
ax.axvline(HILL, color=MUTED, lw=0.8)
ax.text(HILL - 0.06, n - 0.3, "Hill becomes CEO (Oct 14, 2024)", ha="right", fontsize=8, color=INK2)
ax.set_yticks([]); ax.grid(axis="y", visible=False)
ax.set_xlim(2019.8, 2030.2); ax.set_ylim(-1, n + 0.4); ax.set_xticks(range(2020, 2028))
ax.spines["left"].set_visible(False)
pre = sum(tx(r["month"]) < HILL for r in people)
ax.set_title(f"Named senior exits since 2020: {pre} before Hill, {n - pre} under Hill")
ax.legend(handles=[plt.Line2D([], [], marker="o", ls="none", color=BLUE, label="Before Hill"),
                   plt.Line2D([], [], marker="o", ls="none", color=ORANGE, label="Hill era")], frameon=False, loc="lower left")
note(fig, "Month is the announcement or effective month shown in data/people_events.csv, where every row carries its source (SEC 8-K, proxy, or "
          "Nike newsroom) and whether it was verified against an opened primary page. Not a complete census of departures.", y=0.0)
save("06_exec_exits_timeline.png")

cnt = {}
for r in people:
    cnt[r["month"][:4]] = cnt.get(r["month"][:4], 0) + 1
yy = sorted(cnt)
fig, ax = plt.subplots(figsize=(7, 3.8))
ax.bar(yy, [cnt[y] for y in yy], color=BLUE, width=0.6)
for y in yy:
    ax.text(y, cnt[y] + 0.1, str(cnt[y]), ha="center", color=INK2)
ax.set_ylabel("Named senior exits"); ax.set_title("Named senior exits by calendar year")
note(fig, "Counts only the people in data/people_events.csv (not a census). 2026 runs through Oct 12. 2024 includes Donahoe (announced Sept 2024).")
save("07_exits_per_year.png")

# ---------- 8. Workforce and restructuring (replaces the unsourced layoff-count chart) ----------
emp = [v("employees_count", f"{y}-05-31") / 1000 for y in YEARS]
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(FYL, emp, color=BLUE, width=0.62)
for x, e in zip(FYL, emp):
    ax.text(x, e + 0.8, f"{e:.1f}k", ha="center", fontsize=8.5, color=INK2)
ax.set_ylim(0, 95); ax.set_ylabel("Employees at May 31 (thousands)")
ax.set_title("Headcount fell from 83,700 (FY23) to about 73,000 (FY26)")
note(fig, "Employees as stated in Item 1 (Human Capital) of each year's Form 10-K, p. 6 of each. Restructuring charges in the same period: "
          "$443M in FY24 (FY24 10-K) and $385M of severance in FY26 (FY26 10-K); Pace adds about $1.0B of further pre-tax charges through FY31 "
          "(8-K filed Oct 1, 2026, Item 2.05). Filings do not state layoff headcounts.")
save("08_workforce.png")

# ---------- 9. Q1 FY27 growth by segment and channel ----------
seg = [("North America", "north_america"), ("EMEA", "emea"), ("Greater China", "greater_china"), ("APLA", "apla"),
       ("Converse", "converse"), ("NIKE Direct", "nike_direct"), ("Wholesale", "wholesale")]
rep = [v(f"growth_{k}_reported_pct", "Q1FY2027") for _, k in seg]
fig, ax = plt.subplots(figsize=(8, 4.2))
ys = list(range(len(seg)))[::-1]
ax.barh(ys, rep, color=[BLUE if x >= 0 else ORANGE for x in rep], height=0.6)
for y, x in zip(ys, rep):
    ax.text(x + (0.6 if x >= 0 else -0.6), y, f"{x:+.0f}%", va="center", ha="left" if x >= 0 else "right", fontsize=9, color=INK2)
ax.set_yticks(ys); ax.set_yticklabels([s for s, _ in seg])
ax.axvline(0, color=INK2, lw=0.8); ax.set_xlim(-35, 8); ax.set_xlabel("Change vs Q1 FY26, reported (%)")
ax.grid(axis="y", visible=False)
ax.set_title("Q1 FY27: North America was the only region that grew")
note(fig, "Reported growth, three months ended Aug 31, 2026. Q1 FY27 Form 10-Q, pp. 22 and 25. Currency-neutral: Greater China -26%, APLA 0%, "
          "EMEA -5%, NIKE Direct -9%. NIKE Direct and wholesale are NIKE Brand only.")
save("09_q1fy27_segments.png")

# ---------- 10. Illustrative scenario framework ----------
sc = {"Bear": (0.95, 22), "Base": (1.90, 19), "Bull": (2.80, 18)}
last_px = closes[-1]
fig, ax = plt.subplots(figsize=(7, 4))
names = list(sc); prices = [sc[k][0] * sc[k][1] for k in names]
ax.bar(names, prices, color=[MUTED, BLUE, AQUA], width=0.55)
ax.axhline(last_px, color=INK2, lw=1)
ax.text(2.42, last_px + 1, f"Close ${last_px:.2f} (Oct 12, 2026)", ha="right", fontsize=8, color=INK2)
for k, p in zip(names, prices):
    ax.text(k, p + 1, f"${p:.0f}\n({sc[k][0]:.2f} EPS x {sc[k][1]} P/E)", ha="center", fontsize=8, color=INK2)
ax.set_ylim(0, 75); ax.set_ylabel("Implied share price ($)")
ax.set_title("ILLUSTRATIVE scenario method (inputs are placeholders, not forecasts)")
note(fig, "EPS and P/E inputs are placeholder assumptions chosen to show the method; they are not sourced and not forecasts. "
          "Reference point: FY27 adjusted EPS outlook $1.15 to $1.35 (Q1 FY27 release, p. 1).")
save("10_scenarios_illustrative.png")

# ---------- 11. NIKE Direct vs wholesale ----------
nd = [v("revenue_nike_direct", p) / 1000 for p in FY]
wh = [v("revenue_wholesale", p) / 1000 for p in FY]
fig, ax = plt.subplots(figsize=(8.4, 4.4))
ax.plot(FYL, wh, color=BLUE, lw=2, marker="o", ms=5, label="Sales to wholesale customers")
ax.plot(FYL, nd, color=ORANGE, lw=2, marker="o", ms=5, label="NIKE Direct")
for ys, lab in [(wh, "Wholesale"), (nd, "NIKE Direct")]:
    ax.text(len(FYL) - 1 + 0.12, ys[-1], f"{lab} {ys[-1]:.1f}", va="center", fontsize=8, color=INK2)
ax.annotate(f"Direct peak {max(nd):.1f}", xy=(nd.index(max(nd)), max(nd)), xytext=(nd.index(max(nd)) - 1.6, max(nd) + 3), fontsize=8,
            color=INK2, arrowprops=dict(arrowstyle="-", color=MUTED))
ax.set_xlim(-0.3, len(FYL) + 0.9); ax.set_ylim(0, 32); ax.set_ylabel("NIKE Brand revenue ($ billions)")
ax.legend(frameon=False, fontsize=8, loc="lower left")
ax.set_title("NIKE Direct peaked in FY24 and has fallen 18% since; wholesale is recovering")
note(fig, "NIKE Brand revenues by channel from the disaggregation-of-revenue tables in each year's Form 10-K; page-level citations in data/nike_filing_facts.csv.")
save("11_channel_mix.png")

# ---------- 12. Greater China quarterly growth ----------
gq = [f"Q{q}FY{y}" for y in (2023, 2024, 2025, 2026) for q in (1, 2, 3, 4)] + ["Q1FY2027"]
gql = [f"Q{p[1]}\nFY{p[-2:]}" for p in gq]
g = [v("growth_greater_china_reported_pct", p) for p in gq]
fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(gql, g, color=[BLUE if x >= 0 else ORANGE for x in g], width=0.62)
for x, y in zip(gql, g):
    ax.text(x, y + (0.8 if y >= 0 else -0.8), f"{y:+.0f}%", ha="center", va="bottom" if y >= 0 else "top", fontsize=7.5, color=INK2)
ax.axhline(0, color=INK2, lw=0.8); ax.set_ylim(-30, 30); ax.set_ylabel("Change vs prior-year quarter, reported (%)")
ax.set_title("Greater China revenue has declined for nine straight quarters (Q1 FY25 to Q1 FY27)")
plt.setp(ax.get_xticklabels(), fontsize=7.5)
note(fig, "Reported change in Greater China revenues from each quarter's earnings release (8-K Ex. 99.1, divisional revenues table) and Form 10-Q.")
save("12_greater_china_quarterly.png")

# ---------- 13. Dividends vs earnings ----------
dps = [v("dividends_declared_per_share", p) for p in FY]
fig, ax = plt.subplots(figsize=(8.4, 4.4))
ax.plot(FYL, eps, color=BLUE, lw=2, marker="o", ms=5, label="Diluted EPS")
ax.plot(FYL, dps, color=ORANGE, lw=2, marker="o", ms=5, label="Dividends declared per share")
for ys in (eps, dps):
    ax.text(len(FYL) - 1 + 0.12, ys[-1], f"${ys[-1]:.2f}", va="center", fontsize=8, color=INK2)
ax.axhspan(1.15, 1.35, color=ORANGE, alpha=0.12, lw=0)
ax.text(0.0, 1.17, "FY27 adjusted EPS outlook $1.15 to $1.35", fontsize=8, color=INK2)
ax.set_xlim(-0.3, len(FYL) + 0.4); ax.set_ylim(0, 4.2); ax.set_ylabel("$ per share")
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.set_title("The dividend keeps rising while earnings fall: FY26 payout was 78% of diluted EPS")
note(fig, "Diluted EPS and dividends declared per share from each year's Form 10-K. FY27 outlook from the Q1 FY27 earnings release, p. 1. "
          "The current quarterly dividend is $0.41 (Q1 FY27 Form 10-Q, p. 5), or $1.64 a year if held.")
save("13_dividends_vs_eps.png")

# ---------- 14. Cash generation vs shareholder payouts ----------
cfo = [v("cash_from_operations", p) / 1000 for p in FY]
cap = [v("capex", p) / 1000 for p in FY]
div = [v("dividends_paid", p) / 1000 for p in FY]
bb = [v("share_repurchases", p) / 1000 for p in FY]
fcf = [a - b for a, b in zip(cfo, cap)]
import numpy as np
x = np.arange(len(FY)); w = 0.26
fig, ax = plt.subplots(figsize=(9.4, 4.6))
ax.bar(x - w - 0.02, fcf, w, color=BLUE, label="Operating cash flow minus capex (derived)")
ax.bar(x, div, w, color=ORANGE, label="Dividends paid")
ax.bar(x + w + 0.02, bb, w, color=AQUA, label="Share repurchases")
ax.set_xticks(x); ax.set_xticklabels(FYL); ax.set_ylabel("$ billions")
ax.legend(frameon=False, fontsize=8, ncol=3, loc="upper center", bbox_to_anchor=(0.5, 1.0))
ax.set_ylim(0, 7.8)
ax.set_title("In FY26, dividends paid ($2.4B) exceeded operating cash flow minus capex ($2.2B)")
note(fig, "Cash provided by operations, additions to property, plant and equipment, dividends and repurchases from the consolidated statements of "
          "cash flows in each year's Form 10-K. 'Operating cash flow minus capex' is my arithmetic, not a Nike-reported measure.")
save("14_cash_returns.png")

# ---------- 15. EBIT margin by region ----------
regs = [("north_america", "North America", BLUE), ("greater_china", "Greater China", RED), ("apla", "APLA", AQUA),
        ("emea", "EMEA", VIOLET), ("converse", "Converse", MUTED)]
fig, ax = plt.subplots(figsize=(8.8, 4.6))
for key, lab, col in regs:
    m = [100 * v(f"ebit_{key}", p) / v(f"revenue_{key}", p) for p in FY]
    ax.plot(FYL, m, color=col, lw=2, marker="o", ms=4)
    nudge = {"apla": 0.9, "greater_china": -0.9}.get(key, 0)
    ax.text(len(FYL) - 1 + 0.12, m[-1] + nudge, f"{lab} {m[-1]:.1f}%", va="center", fontsize=8, color=INK2)
ax.set_xlim(-0.3, len(FYL) + 1.3); ax.set_ylim(0, 42); ax.set_ylabel("EBIT / segment revenue (%)")
ax.set_title("Greater China fell from Nike's most profitable region (39% in FY21) to 22%; North America now leads")
note(fig, "Segment EBIT divided by segment revenue (my arithmetic) from the segment note in each year's Form 10-K; page-level citations in "
          "data/nike_filing_facts.csv. Segment EBIT excludes Global Brand Divisions and Corporate costs. FY26 North America and Converse include "
          "$965M and $21M of expected IEEPA tariff recovery (FY26 10-K p. 30), which Nike says largely offsets tariffs recognized in FY26.")
save("15_region_ebit_margin.png")
# ---------- 16. FY26 revenue mix: channel, product, region ----------
T = v("revenues", "FY2026")
oth = v("revenue_global_brand_divisions", "FY2026") + v("revenue_corporate", "FY2026")
panels = [
    ("By channel", [("Wholesale (incl. Converse)", v("revenue_total_wholesale_incl_converse", "FY2026")),
                    ("Nike-owned stores", v("revenue_nike_stores", "FY2026") * 1000),
                    ("NIKE Brand Digital", v("revenue_nike_brand_digital", "FY2026") * 1000),
                    ("Converse direct to consumer", v("revenue_converse_dtc", "FY2026")),
                    ("Licensing and other", oth + v("revenue_converse_licensing_other", "FY2026"))]),
    ("By product", [("Footwear", v("revenue_footwear", "FY2026")), ("Apparel", v("revenue_apparel", "FY2026")),
                    ("Equipment", v("revenue_equipment", "FY2026")), ("Converse", v("revenue_converse", "FY2026")),
                    ("Other", oth)]),
    ("By region", [("North America", v("revenue_north_america", "FY2026")), ("EMEA", v("revenue_emea", "FY2026")),
                   ("APLA", v("revenue_apla", "FY2026")), ("Greater China", v("revenue_greater_china", "FY2026")),
                   ("Converse", v("revenue_converse", "FY2026")), ("Other", oth)]),
]
fig, axes = plt.subplots(3, 1, figsize=(8.4, 7.4), gridspec_kw={"hspace": 0.55})
for ax, (ttl, rows) in zip(axes, panels):
    labs = [r[0] for r in rows][::-1]; sh = [r[1] / T * 100 for r in rows][::-1]
    ax.barh(labs, sh, color=BLUE, height=0.6)
    for y, (val, pct) in enumerate(zip([r[1] for r in rows][::-1], sh)):
        ax.text(pct + 0.8, y, f"{pct:.1f}%  (${val / 1000:.1f}B)", va="center", fontsize=8, color=INK2)
    ax.set_xlim(0, 80); ax.grid(axis="y", visible=False); ax.set_title(ttl, loc="left", fontsize=10)
axes[-1].set_xlabel("Share of FY26 NIKE, Inc. revenue ($46.4B), %")
axes[1].text(79, 1.2, f"Jordan Brand ${v('revenue_jordan', 'FY2026') / 1000:.1f}B "
             f"({v('revenue_jordan', 'FY2026') / T * 100:.0f}%) sits inside\nNIKE Brand footwear and apparel",
             ha="right", va="center", fontsize=8, color=INK2)
fig.suptitle("FY26: wholesale is 60% of revenue, footwear 64%; licensing and other is 0.3%",
             fontweight="bold", fontsize=11, x=0.01, ha="left", y=0.97)
note(fig, "FY26 Form 10-K: revenues p. 55; product, segment and Jordan p. 32; stores and digital ($9.1B and $8.6B, rounded) p. 33; channel totals "
          "incl. Converse p. 83; Converse DTC and licensing p. 41. 'Other' is Global Brand Divisions ($49M) plus Corporate ($2M). Shares are my arithmetic.")
save("16_revenue_mix_fy26.png")

# ---------- 17. Jordan Brand: like-for-like series and the two resets ----------
# Each year-on-year ratio uses two values from the same filing, so the chain crosses the FY2022
# category change and the FY2025 removal of wholesale equivalent reporting without mixing bases.
jr = {"FY2018": v("revenue_jordan", "FY2018") / v("revenue_jordan", "FY2017"),
      "FY2019": v("revenue_jordan", "FY2019") / v("revenue_jordan", "FY2018"),
      "FY2020": v("revenue_jordan_brand_wholesale_equivalent", "FY2020") / v("revenue_jordan", "FY2019"),
      "FY2021": v("revenue_jordan_wholesale_equiv_recast", "FY2021") / v("revenue_jordan_wholesale_equiv_recast", "FY2020"),
      "FY2022": v("revenue_jordan", "FY2022") / v("revenue_jordan_wholesale_equiv_recast", "FY2021"),
      "FY2023": v("revenue_jordan", "FY2023") / v("revenue_jordan", "FY2022"),
      "FY2024": v("revenue_jordan_reported_basis", "FY2024") / v("revenue_jordan_reported_basis", "FY2023"),
      "FY2025": v("revenue_jordan_reported_basis", "FY2025") / v("revenue_jordan_reported_basis", "FY2024"),
      "FY2026": v("revenue_jordan_reported_basis", "FY2026") / v("revenue_jordan_reported_basis", "FY2025")}
jp = ["FY2017"] + list(jr)
idx = [1.0]
for k in jr:
    idx.append(idx[-1] * jr[k])
lvl = [i / idx[-1] * v("revenue_jordan_reported_basis", "FY2026") / 1000 for i in idx]
fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.4, 4.4), gridspec_kw={"width_ratios": [3, 2], "wspace": 0.28})
a1.bar([f"FY{p[-2:]}" for p in jp], lvl, color=[ORANGE if p in ("FY2018", "FY2025", "FY2026") else BLUE for p in jp], width=0.62)
for i, l in enumerate(lvl):
    a1.text(i, l + 0.12, f"{l:.1f}", ha="center", fontsize=8, color=INK2)
a1.set_ylim(0, 10); a1.set_ylabel("$ billions, FY26 reported basis (back-cast)")
a1.set_title("Jordan revenue, like-for-like (orange = down years)", loc="left", fontsize=10)
pk1 = [0, (idx[1] / idx[0] - 1) * 100, (idx[2] / idx[0] - 1) * 100]
pk2 = [0, (idx[8] / idx[7] - 1) * 100, (idx[9] / idx[7] - 1) * 100]
yrs = ["Peak year", "+1 year", "+2 years"]
a2.plot(yrs, pk1, color=BLUE, lw=2, marker="o", ms=6, label="FY18 reset (peak FY17)")
a2.plot(yrs, pk2, color=ORANGE, lw=2, marker="o", ms=6, label="Current reset (peak FY24)")
for ys, c in ((pk1, BLUE), (pk2, ORANGE)):
    for x, y in zip(yrs[1:], ys[1:]):
        a2.text(x, y + (1.2 if y > -12 else -2.6), f"{y:+.0f}%", ha="center", fontsize=8.5, color=INK2)
a2.axhline(0, color=INK2, lw=0.8); a2.set_ylim(-26, 8); a2.set_ylabel("Change from prior peak (%)")
a2.legend(frameon=False, fontsize=8, loc="lower left")
a2.set_title("Two resets compared", loc="left", fontsize=10)
fig.suptitle("Jordan is 19% below its FY24 peak; the FY18 reset was back above peak within two years",
             fontweight="bold", fontsize=11, x=0.01, ha="left", y=1.02)
note(fig, "Each year's change uses two values from the same filing (FY19, FY20, FY22, FY23, FY25 and FY26 10-Ks), chained and scaled to the FY26 reported "
          "figure ($7,034M, FY26 10-K p. 32). Earlier years were reported on a wholesale equivalent basis and before the FY22 category change, so the "
          "back-cast dollar levels are my arithmetic, not Nike figures. Q1 FY27: Jordan fell by mid-teens (Q1 FY27 call, Oct 1, 2026); not plotted.", y=-0.04)
save("17_jordan_resets.png")

# ---------- 18. Jordan: resale premiums and search interest against revenue ----------
import statistics
rs = [r for r in csv.DictReader(open(os.path.join(DATA, "jordan_resale_goat_20261013.csv")))
      if r["collab_or_special"] == "False" and r["premium_primary_DERIVED"]]
ry = ["2023", "2024", "2025", "2026"]
def med_prem(f):
    return [statistics.median(float(r["premium_primary_DERIVED"]) for r in rs if r["release_year"] == y and f(r)) * 100 for y in ry]
series = [("All retro general releases", med_prem(lambda r: True), INK2),
          ("Air Jordan 1 High OG", med_prem(lambda r: r["line"] == "AJ1 High OG"), BLUE),
          ("Air Jordan 4", med_prem(lambda r: r["line"] == "AJ4"), ORANGE),
          ("Air Jordan 3", med_prem(lambda r: r["line"] == "AJ3"), AQUA)]
gt = {(r["dt"], r["geo"]): r for r in csv.DictReader(open(os.path.join(DATA, "google_trends_jordan_julsep.csv")))}
# Jul to Sep of calendar year Y falls in Nike fiscal year Y+1; index both to FY2022 = 100
fyl = ["FY22", "FY23", "FY24", "FY25", "FY26"]
cal = ["2021", "2022", "2023", "2024", "2025"]
def gidx(term):
    b = float(gt[("2021", "US")][term])
    return [float(gt[(c, "US")][term]) / b * 100 for c in cal]
rev_i = [l / lvl[5] * 100 for l in lvl[5:10]]
fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.6, 4.5), gridspec_kw={"wspace": 0.3})
for lab, ys, c in series:
    a1.plot(ry, ys, color=c, lw=2, marker="o", ms=5, label=lab)
a1.text(3.1, series[1][1][-1], f"{series[1][1][-1]:+.0f}%", va="center", fontsize=8, color=INK2)
a1.axhline(0, color=INK2, lw=0.8); a1.set_xlim(-0.3, 3.6); a1.set_ylim(-45, 35)
a1.set_xlabel("Release year"); a1.set_ylabel("Median resale vs retail (%)")
a1.legend(frameon=False, fontsize=7.5, loc="lower left")
a1.set_title("Resale premium by release year (GOAT, Oct 13, 2026)", loc="left", fontsize=10)
for lab, ys, c in [("Jordan revenue (like-for-like)", rev_i, BLUE), ('Search: "Air Jordan"', gidx("Air Jordan"), ORANGE),
                   ('Search: "Jordan 1"', gidx("Jordan 1"), AQUA)]:
    a2.plot(fyl, ys, color=c, lw=2, marker="o", ms=5, label=lab)
    a2.text(4.12, ys[-1], f"{ys[-1]:.0f}", va="center", fontsize=8, color=INK2)
a2.axhline(100, color=MUTED, lw=0.8); a2.set_xlim(-0.3, 4.6); a2.set_ylim(0, 150)
a2.set_ylabel("Index, FY22 = 100"); a2.legend(frameon=False, fontsize=7.5, loc="lower left")
a2.set_title("US search interest fell while revenue rose", loc="left", fontsize=10)
fig.suptitle("Interest in retro Jordans fell before the supply cuts, and resale prices have not recovered since",
             fontweight="bold", fontsize=11, x=0.01, ha="left", y=1.02)
note(fig, "Left: median of per-size last sales (US 7 to 13) on GOAT divided by retail, general releases only, 247 shoes, observed Oct 13, 2026 "
          "(data/jordan_resale_goat_20261013.csv); one snapshot, so older releases have had longer to drift; my arithmetic. Right: Google Trends US, "
          "July to September average of each calendar year, mapped to the Nike fiscal year it falls in (data/google_trends_jordan_julsep.csv); revenue "
          "index from chart 17. Search indices are scaled to each term's own peak and are not a measure of units.", y=-0.04)
save("18_jordan_demand_tests.png")

# ---------- 19. Jordan scenario valuation (illustrative) ----------
jv = list(csv.DictReader(open(os.path.join(DATA, "valuation", "jordan_scenarios.csv"))))
sc_rows = [r for r in jv if not r["scenario"].startswith("Reference")]
ref = next(r for r in jv if r["scenario"].startswith("Reference: Jordan FY2026"))
yrs = ["FY24", "FY25", "FY26", "FY27", "FY28", "FY29", "FY30", "FY31"]
hist = [v("revenue_jordan_reported_basis", p) / 1000 for p in ("FY2024", "FY2025", "FY2026")]
cols = [MUTED, BLUE, AQUA]
fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.6, 4.5), gridspec_kw={"width_ratios": [3, 2], "wspace": 0.3})
a1.plot(yrs[:3], hist, color=INK, lw=2, marker="o", ms=5, label="Reported")
for r, c in zip(sc_rows, cols):
    ys = [hist[-1]] + [float(r[f"revenue_FY{y}_usd_m"]) / 1000 for y in range(2027, 2032)]
    a1.plot(yrs[2:], ys, color=c, lw=2, marker="o", ms=4, ls="--", label=r["scenario"])
    a1.text(7.15, ys[-1], f"{ys[-1]:.1f}", va="center", fontsize=8, color=INK2)
a1.set_xlim(-0.3, 7.7); a1.set_ylim(0, 10); a1.set_ylabel("Jordan revenue ($ billions)")
a1.legend(frameon=False, fontsize=7.5, loc="lower left")
a1.set_title("Revenue paths (scenario assumptions)", loc="left", fontsize=10)
names = [r["scenario"].split(":")[0] for r in sc_rows]
vals = [float(r["value_per_nke_share_usd"]) for r in sc_rows]
a2.bar(names, vals, color=cols, width=0.55)
for i, (val, r) in enumerate(zip(vals, sc_rows)):
    a2.text(i, val + 0.15, f"${val:.2f}\n({float(r['share_of_nke_price_pct']):.0f}% of price)", ha="center", fontsize=8, color=INK2)
refv = float(ref["value_per_nke_share_usd"])
a2.axhline(refv, color=INK2, lw=1, ls=":")
a2.text(-0.35, refv - 0.4, f"Reference: FY26 revenue at\nNKE EV/Sales = ${refv:.2f}", ha="left", va="top", fontsize=7.5, color=INK2)
a2.set_ylim(0, 8.5); a2.set_ylabel("Jordan value per NKE share ($)"); a2.grid(axis="x", visible=False)
a2.set_title("DCF value per NKE share", loc="left", fontsize=10)
fig.suptitle("ILLUSTRATIVE: Jordan is worth about $2 to $6 of NKE's $35 share price across scenarios",
             fontweight="bold", fontsize=11, x=0.01, ha="left", y=1.02)
note(fig, "Scenario growth rates, FY2031 EBIT margins (8%, 11%, 14%) and terminal growth (1%, 2.5%, 3%) are assumptions, not forecasts; all start from "
          "FY2026 Jordan revenue of $7,034M (FY26 10-K p. 32) and a mid-teens FY2027 decline (Q1 FY27 call). DCF conventions follow the repo's reverse DCF: "
          "10% WACC, 22.5% tax, sales to capital 2.5, 1,487M shares, NKE $35.35 (Oct 12, 2026). Built by scripts/jordan_valuation.py "
          "(data/valuation/jordan_scenarios.csv).", y=-0.04)
save("19_jordan_valuation.png")

# ---------- 20. Factory orders vs Nike footwear revenue (Test 1) ----------
fa = [r for r in csv.DictReader(open(os.path.join(DATA, "definitive", "suppliers", "nike_fiscal_quarter_alignment.csv")))
      if r["nike_footwear_yoy_pct_DERIVED"] and r["fengtay_yoy_usd_pct_DERIVED"]]
xl = [f"Q{r['nike_fq'][1]}\nFY{r['nike_fq'][-2:]}" if r["nike_fq"][1] == "1" else "" for r in fa]
ft = [float(r["fengtay_yoy_usd_pct_DERIVED"]) for r in fa]
nf = [float(r["nike_footwear_yoy_pct_DERIVED"]) for r in fa]
fig, ax = plt.subplots(figsize=(10.4, 4.6))
xs = list(range(len(fa)))
ax.plot(xs, ft, color=BLUE, lw=2, marker="o", ms=3.5, label="Feng Tay revenue in USD (factory, about 85% one customer)")
ax.plot(xs, nf, color=ORANGE, lw=2, marker="o", ms=3.5, label="Nike Brand footwear revenue")
ax.axhline(0, color=INK2, lw=0.8)
lo, hi = -40, 60
for x, a, b in zip(xs, ft, nf):
    for val, c in ((a, BLUE), (b, ORANGE)):
        if val > hi:
            ax.text(x, hi - 3, f"{val:.0f}%", ha="center", fontsize=7, color=INK2)
ax.set_ylim(lo, hi); ax.set_xticks(xs); ax.set_xticklabels(xl, fontsize=8)
i0 = [r["nike_fq"] for r in fa].index("Q3FY2023"); i1 = [r["nike_fq"] for r in fa].index("Q2FY2024")
ax.axvspan(i0 - 0.4, i1 + 0.4, color=GRID, alpha=0.6, lw=0)
ax.text((i0 + i1) / 2, 48, "Factory cut while\nNike footwear grew", ha="center", fontsize=8, color=INK2)
j0 = [r["nike_fq"] for r in fa].index("Q1FY2025")
ax.annotate("FY25: Nike footwear -11.7%,\nFeng Tay only -4.7%", xy=(j0 + 1, -12), xytext=(j0 - 6, -33), fontsize=8, color=INK2,
            arrowprops=dict(arrowstyle="-", color=MUTED))
ax.set_ylabel("Change vs same quarter a year earlier (%)")
ax.legend(frameon=False, fontsize=8, loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=2)
ax.set_title("Nike's main shoe factory's revenue fell in 2023, four quarters before Nike's footwear revenue did", loc="left")
note(fig, "Feng Tay (9910.TW) monthly revenue from MOPS via the FinMind mirror (287 of 296 checked values match MOPS; all Feng Tay months 2018 to 2026 match "
          "Feng Tay's IR page), summed into Nike fiscal quarters and converted at monthly TWD/USD averages (my arithmetic). Feng Tay's largest customer, "
          "83% to 86% of revenue, is unnamed; that it is Nike is my inference from Feng Tay's own site. Nike footwear: earnings releases and 10-Qs "
          "(data/definitive/suppliers/nike_fiscal_quarter_alignment.csv). Values above 60% are printed at the top edge.", y=-0.1)
save("20_factory_vs_nike_footwear.png")

print("done", sorted(os.listdir(OUT)))
