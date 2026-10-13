"""Live Excel version of the Jordan Brand scenario valuation (scripts/jordan_valuation.py).

Same inputs, same conventions, but every number is a formula a reader can audit or flex in
Excel: pick Bear/Base/Bull on the Inputs sheet and the whole model follows. Built with the
excel-modeling skill (.claude/skills/excel-modeling), which recalculates the workbook with
LibreOffice, caches the values and runs the checks. The test at the bottom proves each
scenario reproduces data/valuation/jordan_scenarios.csv and jordan_sensitivity.csv.

Inputs from files: data/nike_filing_facts.csv (Jordan FY2026 and FY2024 revenue, FY26 10-K
p. 32) and data/valuation/peer_multiples.csv (NKE price, market data, Oct 13, 2026).
Output: data/valuation/jordan_valuation.xlsx
Run: python3 scripts/jordan_valuation_xlsx.py
"""
import csv
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, ".claude", "skills", "excel-modeling", "scripts"))
from model_builder import Model  # noqa: E402
import xlcore  # noqa: E402

DATA = os.path.join(ROOT, "data")
OUT = os.path.join(DATA, "valuation", "jordan_valuation.xlsx")
FACTS = {(r["metric"], r["period"]): r for r in csv.DictReader(open(os.path.join(DATA, "nike_filing_facts.csv")))}
NKE = next(r for r in csv.DictReader(open(os.path.join(DATA, "valuation", "peer_multiples.csv"))) if r["ticker"] == "NKE")


def fact(metric, period):
    r = FACTS[(metric, period)]
    return float(r["value"].replace(",", "")), f"{r['filing']} {r['page']}"


J26, J26_SRC = fact("revenue_jordan_reported_basis", "FY2026")
J24, J24_SRC = fact("revenue_jordan_reported_basis", "FY2024")
CONV = "Convention shared with the reverse DCF (research_notes/thesis_tests/consensus_and_valuation.md Section C)"
CASES = ["Bear", "Base", "Bull"]
YEARS = ["FY2027E", "FY2028E", "FY2029E", "FY2030E", "FY2031E"]

m = Model(OUT, "Jordan Brand scenario valuation (illustrative)", YEARS,
          description="Assumption-driven DCF of Jordan Brand; growth, margin and terminal growth are labelled ASSUMPTIONS, not forecasts. "
                      "Mirror of scripts/jordan_valuation.py.")

inp = m.list_sheet("Inputs").describe("Scenario switch, filing facts, market data and DCF conventions")
inp.section("Scenario")
inp.switch("case", "Active scenario", CASES, "Base")
inp.section("Filing facts ($m)")
inp.scalar("j26", "Jordan revenue FY2026", J26, "$m", J26_SRC)
inp.scalar("j24", "Jordan revenue FY2024 (peak)", J24, "$m", J24_SRC)
inp.section("Market data")
inp.scalar("price", "NKE share price", float(NKE["price"]), "$", "market data, data/valuation/peer_multiples.csv (Oct 13, 2026)")
inp.scalar("shares", "NKE diluted shares (m)", 1487.0, "#", CONV)
inp.section("DCF conventions")
inp.scalar("tax", "Tax rate", 0.225, "%", CONV)
inp.scalar("s2c", "Sales to capital", 2.5, "x", CONV)
inp.scalar("roic", "Terminal ROIC", 0.20, "%", CONV)
inp.scalar("wacc", "WACC", 0.10, "%", CONV)
inp.scalar("m0", "FY2027 starting EBIT margin", 0.057, "%", "FY2027 consolidated margin implied by consensus EPS; " + CONV)
inp.scalar("w27", "FY2027 weight (valuation date 2026-10-12)", 0.63, "yrs", CONV)
inp.section("Scenario assumptions (ASSUMPTIONS)")
inp.scenario("target_margin", "Steady-state EBIT margin, reached FY2031", "%", {"Bear": 0.08, "Base": 0.11, "Bull": 0.14},
             "ASSUMPTION; see research_notes/12_jordan_brand_thesis.md")
inp.scenario("g", "Terminal growth", "%", {"Bear": 0.01, "Base": 0.025, "Bull": 0.03}, "ASSUMPTION")

md = m.timeline_sheet("Model").describe("Revenue path, margin ramp, free cash flow and discounting by fiscal year")
md.section("Timing")
md.row("t", "Period number", "#", "={t[-1]}+1", first="=1")
md.row("w", "Year weight (FY2027 pro-rated)", "yrs", "=1", first="={Inputs.w27}")
md.row("t_end", "Years from valuation date, period end", "yrs", "={t_end[-1]}+{w}", first="={w}")
md.row("t_mid", "Discount timing, mid-period", "yrs", "={t_end}-{w}/2")
md.section("Revenue")
md.scenario_rows("growth", "Revenue growth", "%",
                 {"Bear": [-0.15, -0.08, 0.00, 0.00, 0.00], "Base": [-0.15, -0.03, 0.05, 0.05, 0.05],
                  "Bull": [-0.15, 0.05, 0.12, 0.12, 0.10]},
                 source="ASSUMPTION; FY2027 -15% from Q1 FY27 'mid-teens' decline (Nike transcript, Oct 1, 2026)")
md.row("rev", "Jordan revenue", "$m", "={rev[-1]}*(1+{growth})", first="={Inputs.j26}*(1+{growth})", bold=True)
md.section("Profit and cash flow")
md.row("margin", "EBIT margin (linear ramp to target)", "%",
       "={Inputs.m0}+({Inputs.target_margin}-{Inputs.m0})*({t}-1)/(MAX({t@all})-1)")
md.row("ebit", "EBIT", "$m", "={rev}*{margin}")
md.row("nopat", "NOPAT", "$m", "={ebit}*(1-{Inputs.tax})")
md.row("reinv", "Reinvestment (revenue growth / sales to capital, floored at 0)", "$m",
       "=MAX({rev}-{rev[-1]},0)/{Inputs.s2c}", first="=MAX({rev}-{Inputs.j26},0)/{Inputs.s2c}")
md.row("fcf", "Free cash flow, period-weighted", "$m", "=({nopat}-{reinv})*{w}", bold=True)
md.row("df", "Discount factor", "x", "=1/(1+{Inputs.wacc})^{t_mid}")
md.row("pv", "PV of free cash flow", "$m", "={fcf}*{df}")

val = m.list_sheet("Valuation").describe("DCF value, per-share value and terminal share for the active scenario")
val.section("Terminal value")
val.calc("nopat_next", "NOPAT FY2032 (FY2031 x (1+g))", "$m",
           "={Model.rev@FY2031E}*{Model.margin@FY2031E}*(1-{Inputs.tax})*(1+{Inputs.g})")
val.calc("tv", "Terminal value at FY2031 (value driver formula)", "$m",
           "={nopat_next}*(1-{Inputs.g}/{Inputs.roic})/({Inputs.wacc}-{Inputs.g})")
val.calc("pv_tv", "PV of terminal value", "$m", "={tv}/(1+{Inputs.wacc})^{Model.t_end@FY2031E}")
val.section("Value")
val.calc("pv_fcf", "PV of FY2027-FY2031 free cash flow", "$m", "=SUM({Model.pv@all})")
val.calc("ev", "DCF value of Jordan", "$m", "={pv_fcf}+{pv_tv}")
val.calc("per_share", "Value per NKE share", "$", "={ev}/{Inputs.shares}")
val.calc("pct_price", "Share of NKE price", "%", "={per_share}/{Inputs.price}")
val.calc("tv_share", "Terminal value share of DCF value", "%", "={pv_tv}/{ev}")
val.section("FY2031 snapshot")
val.calc("ebit31", "EBIT FY2031", "$m", "={Model.ebit@FY2031E}")
val.calc("eps31", "EPS contribution FY2031", "$", "={ebit31}*(1-{Inputs.tax})/{Inputs.shares}")
val.calc("vs_peak", "FY2031 revenue vs FY2024 peak", "%", "={Model.rev@FY2031E}/{Inputs.j24}-1")

SC = {r["scenario"].split(":")[0]: r for r in csv.DictReader(open(os.path.join(DATA, "valuation", "jordan_scenarios.csv")))}
SE = {r["revenue_path"].split(":")[0]: r for r in csv.DictReader(open(os.path.join(DATA, "valuation", "jordan_sensitivity.csv")))}
ev_sales = next(r for r in csv.DictReader(open(os.path.join(DATA, "valuation", "jordan_scenarios.csv")))
                if r["scenario"] == "Reference: Jordan FY2026 revenue at NKE EV/Sales")
ch = m.chart_sheet("Charts").describe("Value bridge for the active scenario and the per-share football field")
ch.waterfall("Jordan DCF value, active scenario ($m)", ("PV FY2027 FCF", "={Model.pv@FY2027E}"),
             [("PV FY2028 FCF", "={Model.pv@FY2028E}"), ("PV FY2029 FCF", "={Model.pv@FY2029E}"),
              ("PV FY2030 FCF", "={Model.pv@FY2030E}"), ("PV FY2031 FCF", "={Model.pv@FY2031E}"),
              ("PV terminal value", "={Valuation.pv_tv}")],
             note="Live: follows the scenario switch on Inputs. End bar equals Valuation 'DCF value of Jordan'.")
ch.football_field("Jordan value per NKE share ($)", [
    ("DCF, Bear to Bull scenarios", float(SC["Bear"]["value_per_nke_share_usd"]), float(SC["Bull"]["value_per_nke_share_usd"]),
     "data/valuation/jordan_scenarios.csv (scripts/jordan_valuation.py)"),
    ("DCF, Base path, margin 6% to 17%", float(SE["Base"]["margin_6pct_usd_per_share"]), float(SE["Base"]["margin_17pct_usd_per_share"]),
     "data/valuation/jordan_sensitivity.csv"),
    ("DCF, Bear path, margin 6% to 17%", float(SE["Bear"]["margin_6pct_usd_per_share"]), float(SE["Bear"]["margin_17pct_usd_per_share"]),
     "data/valuation/jordan_sensitivity.csv"),
    ("Jordan FY2026 revenue x NKE EV/Sales", float(ev_sales["value_per_nke_share_usd"]), float(ev_sales["value_per_nke_share_usd"]) + 0.02,
     "jordan_scenarios.csv reference row (point estimate)"),
], unit="$", marker=("Live scenario value per share", "={Valuation.per_share}"),
   note="Static ranges are outputs of scripts/jordan_valuation.py; the marker is live.")

m.check("Margin reaches target in FY2031", "={Model.margin@FY2031E}-{Inputs.target_margin}")
m.check_less("Terminal growth below WACC", "{Inputs.g}", "{Inputs.wacc}")
m.check_rows_nonneg("Revenue never negative", "Model.rev")
m.check("Value = PV(FCF) + PV(TV)", "={Valuation.ev}-SUM({Model.pv@all})-{Valuation.pv_tv}")
m.check("Discount timing: final period ends at stub + (periods - 1) years",
        "={Model.t_end@FY2031E}-({Inputs.w27}+MAX({Model.t@all})-1)")

if __name__ == "__main__":
    rep = m.save()
    print(rep)
    # Proof: each case reproduces the Python model's published CSVs
    want = {r["scenario"].split(":")[0]: r for r in csv.DictReader(open(os.path.join(DATA, "valuation", "jordan_scenarios.csv")))}
    sens = {r["revenue_path"].split(":")[0]: r for r in csv.DictReader(open(os.path.join(DATA, "valuation", "jordan_sensitivity.csv")))}
    from openpyxl import load_workbook
    names = {n: d.attr_text for n, d in load_workbook(OUT).defined_names.items()}

    def at(sheet, key, col="C"):
        """Cell of a keyed row (the builder names every row k_<Sheet>_<key>)."""
        return f"{sheet}!{col}{names[f'k_{sheet}_{key}'].split('$')[-1]}"

    bad = 0
    with xlcore.LOSession(OUT) as lo:
        for case in CASES:
            lo.set(at("Inputs", "case"), case)
            lo.recalc()
            got = {"dcf_value_usd_m": round(lo.get(at("Valuation", "ev"))), "value_per_nke_share_usd": round(lo.get(at("Valuation", "per_share")), 2),
                   "terminal_share_of_value_pct": round(lo.get(at("Valuation", "tv_share")) * 100, 1),
                   "fy2031_ebit_usd_m": round(lo.get(at("Valuation", "ebit31"))), "revenue_FY2031_usd_m": round(lo.get(at("Model", "rev", "G")))}
            for k, v in got.items():
                ok = abs(float(want[case][k]) - v) < 1e-9
                bad += not ok
                print(f"{'OK ' if ok else 'BAD'} {case} {k}: xlsx {v} vs csv {want[case][k]}")
            assert lo.get(names["MasterCheck"]) == 1, "master check failed"
            for mg in (0.06, 0.08, 0.11, 0.14, 0.17):
                lo.set(at("Inputs", "target_margin", "DEF"[CASES.index(case)]), mg)
                lo.recalc()
                v = round(lo.get(at("Valuation", "per_share")), 2)
                ok = abs(float(sens[case][f"margin_{int(round(mg * 100))}pct_usd_per_share"]) - v) < 1e-9
                bad += not ok
                print(f"{'OK ' if ok else 'BAD'} {case} margin {mg}: xlsx {v} vs csv {sens[case][f'margin_{int(round(mg * 100))}pct_usd_per_share']}")
    # Driver ranking for the pitch: one-at-a-time flex around the Base case (my arithmetic on the model)
    import xl
    flex = [("target_margin", "E", 0.08, 0.14), ("wacc", "C", 0.09, 0.11), ("g", "E", 0.01, 0.03),
            ("tax", "C", 0.20, 0.25), ("s2c", "C", 2.0, 3.0), ("roic", "C", 0.15, 0.25), ("m0", "C", 0.047, 0.067)]
    t = xl.tornado(OUT, at("Valuation", "per_share"), [(at("Inputs", k, c), lo, hi) for k, c, lo, hi in flex])
    labels = {at("Inputs", k, c): k for k, c, _, _ in flex}
    with open(os.path.join(DATA, "valuation", "jordan_tornado.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["input", "low", "high", "value_per_share_at_low_usd", "value_per_share_at_high_usd", "swing_usd",
                    "base_value_per_share_usd", "basis"])
        for r in t["ranked"]:
            w.writerow([labels[r["input"]], r["low"], r["high"], round(r["output_at_low"], 2), round(r["output_at_high"], 2),
                        round(r["swing"], 2), round(t["base_output"], 2),
                        "my arithmetic: Base case of data/valuation/jordan_valuation.xlsx, one input flexed at a time"])
    print("tornado:", [(labels[r["input"]], round(r["swing"], 2)) for r in t["ranked"]])
    sys.exit(1 if bad else 0)
