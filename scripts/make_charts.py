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

print("done", sorted(os.listdir(OUT)))
