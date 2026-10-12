"""Writes research_notes/04_financial_data_pack.md from data/nike_filing_facts.csv.
Every table row lists the filing and printed pages its numbers come from; the CSV holds
the cell-level citation (filing, page, URL, verbatim quote) for each value."""
import csv
import os
import re
from collections import OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F = OrderedDict(((r["metric"], r["period"]), r) for r in csv.DictReader(open(os.path.join(ROOT, "data", "nike_filing_facts.csv"))))
URLS = OrderedDict()


def cell(metric, period, fmt="{:,.0f}"):
    r = F.get((metric, period))
    if not r:
        return None, None
    raw = r["value"].replace(",", "")
    try:
        txt = fmt.format(float(raw))
    except ValueError:
        txt = r["value"]
    URLS[r["filing"]] = r["url"]
    return txt, (r["filing"], r["page"])


def short(filing):
    m = re.match(r"(FY\d{4}) Form 10-K", filing)
    if m: return f"{m.group(1)} 10-K"
    m = re.match(r"(Q\d FY\d{4}) Form 10-Q", filing)
    if m: return f"{m.group(1)} 10-Q"
    m = re.match(r"(Q\d FY\d{4}) earnings release", filing)
    if m: return f"{m.group(1)} release"
    if filing.startswith("2026 Proxy"): return "2026 proxy"
    return filing


def cite(srcs):
    by = OrderedDict()
    for f, p in srcs:
        by.setdefault(short(f), [])
        n = p.replace("p. ", "").replace(" of exhibit", "")
        if n not in by[short(f)]: by[short(f)].append(n)
    return "; ".join(f"{k} p. {', '.join(sorted(v, key=lambda x: (len(x), x)))}" for k, v in by.items())


def table(title, periods, cols, period_label=None, note=None):
    out = [f"### {title}", "", "| Period | " + " | ".join(c[0] for c in cols) + " | Source (filing, printed page) |",
           "|---|" + "---|" * len(cols) + "---|"]
    for p in periods:
        vals, srcs = [], []
        for _, m, fmt in cols:
            t, s = cell(m, p, fmt)
            vals.append(t if t is not None else "n/a")
            if s: srcs.append(s)
        if not srcs: continue
        out.append(f"| {period_label(p) if period_label else p} | " + " | ".join(vals) + f" | {cite(srcs)} |")
    if note: out += ["", note]
    return "\n".join(out) + "\n"


M0, M1, M2, M3 = "{:,.0f}", "{:.1f}", "{:.2f}", "{:.3f}"
FY = [f"FY{y}" for y in range(2019, 2027)]
FYE = [f"{y}-05-31" for y in range(2019, 2027)]
Q = [f"Q{q}FY{y}" for y in (2024, 2025, 2026) for q in (1, 2, 3, 4)] + ["Q1FY2027"]
QE = ["2023-08-31", "2023-11-30", "2024-02-29", "2024-05-31", "2024-08-31", "2024-11-30", "2025-02-28", "2025-05-31",
      "2025-08-31", "2025-11-30", "2026-02-28", "2026-05-31", "2026-08-31"]
ql = lambda p: f"Q{p[1]} FY{p[-4:]}"

parts = ["""# Nike financial data pack (rebuilt from SEC filings, Oct 12, 2026)

**How this was built.** Every Nike 10-K for FY2019 to FY2026, every 10-Q from Q1 FY2024 to Q1 FY2027, every quarterly
earnings 8-K (Exhibit 99.1) from Q4 FY2019 to Q1 FY2027, the 2026 proxy (DEF 14A) and the 2024 to 2026 leadership and
restructuring 8-Ks were downloaded from sec.gov and read in full. Each number below was extracted with a verbatim quote
and then machine-checked: the value had to appear on the cited page of the cited filing. The complete cell-level record
(filing, printed page, URL, quote) is `data/nike_filing_facts.csv`; this file is generated from it by
`scripts/build_data_pack.py`, so the two cannot drift apart.

**Conventions.** USD millions unless noted. Fiscal year ends May 31. Page numbers are the printed page numbers in the
filing (10-K, 10-Q, proxy). Earnings releases have no printed page numbers, so their pages are counted from the first page
of the Exhibit 99.1 press release. Each table row is drawn from the filing that first reported that period (10-K for the
year, 10-Q for Q1 to Q3, the Q4 earnings release for Q4), so values are as originally reported. Where Nike later
reclassified a figure, the CSV notes the count of sources that agree. "n/a" means the filing does not report it.
"""]

parts.append("## 1. Annual income statement\n")
parts.append(table("Revenue, margin, earnings", FY, [
    ("Revenue", "revenues", M0), ("Gross profit", "gross_profit", M0), ("Gross margin %", "gross_margin_pct", M1),
    ("Demand creation", "demand_creation_expense", M0), ("Operating overhead", "operating_overhead_expense", M0),
    ("EBIT", "ebit_total", M0), ("Tax rate %", "effective_tax_rate_pct", M1), ("Net income", "net_income", M0),
    ("Diluted EPS ($)", "eps_diluted", M2), ("Diluted shares (m)", "weighted_avg_diluted_shares_m", M1)]))

parts.append("## 2. Annual revenue by segment, channel and product\n")
parts.append(table("Operating segments (reported revenues)", FY, [
    ("North America", "revenue_north_america", M0), ("EMEA", "revenue_emea", M0), ("Greater China", "revenue_greater_china", M0),
    ("APLA", "revenue_apla", M0), ("Global Brand Div.", "revenue_global_brand_divisions", M0), ("NIKE Brand", "revenue_nike_brand", M0),
    ("Converse", "revenue_converse", M0), ("Corporate", "revenue_corporate", M0)]))
parts.append(table("NIKE Brand channel and product", FY, [
    ("NIKE Direct", "revenue_nike_direct", M0), ("Wholesale", "revenue_wholesale", M0), ("Footwear", "revenue_footwear", M0),
    ("Apparel", "revenue_apparel", M0), ("Equipment", "revenue_equipment", M0), ("Jordan Brand", "revenue_jordan", M0)],
    note="Jordan Brand revenue is shown as reported in each year's 10-K. Later filings restate some product and Jordan splits "
         "(for example, FY2023 and FY2024 Jordan figures differ between the FY2024 and FY2025 10-Ks); use one year's 10-K for any trend."))
parts.append(table("Segment EBIT", FY, [
    ("North America", "ebit_north_america", M0), ("EMEA", "ebit_emea", M0), ("Greater China", "ebit_greater_china", M0),
    ("APLA", "ebit_apla", M0), ("Converse", "ebit_converse", M0), ("Global Brand Div.", "ebit_global_brand_divisions", M0),
    ("Corporate", "ebit_corporate", M0)]))

parts.append("## 3. Balance sheet at fiscal year end\n")
parts.append(table("May 31 balances", FYE, [
    ("Cash", "cash_and_equivalents", M0), ("ST investments", "short_term_investments", M0), ("Inventories", "inventories", M0),
    ("Total assets", "total_assets", M0), ("Current LTD", "current_portion_long_term_debt", M0), ("Notes payable", "notes_payable", M0),
    ("Long-term debt", "long_term_debt", M0), ("Equity", "shareholders_equity", M0)]))

parts.append("## 4. Cash flow, dividends, buybacks, people\n")
parts.append(table("Cash flow and shareholder returns", FY, [
    ("Cash from operations", "cash_from_operations", M0), ("Capex (PP&E additions)", "capex", M0), ("Dividends paid", "dividends_paid", M0),
    ("Share repurchases", "share_repurchases", M0), ("Dividends declared / share ($)", "dividends_declared_per_share", M3)],
    note="Operating cash flow minus capex is not a Nike-reported measure; compute it from these columns if needed."))
parts.append(table("Employees", FYE, [("Employees (approx.)", "employees_count", M0)]))

parts.append("## 5. Quarterly results (Q1 FY2024 to Q1 FY2027)\n")
parts.append(table("Quarterly income statement", Q, [
    ("Revenue", "revenues", M0), ("Gross margin %", "gross_margin_pct", M1), ("Net income", "net_income", M0),
    ("Diluted EPS ($)", "eps_diluted", M2), ("Reported growth %", "growth_revenues_reported_pct", M0),
    ("Currency-neutral growth %", "growth_revenues_cn_pct", M0)], period_label=ql))
parts.append(table("Quarterly segments and channels", Q, [
    ("North America", "revenue_north_america", M0), ("EMEA", "revenue_emea", M0), ("Greater China", "revenue_greater_china", M0),
    ("APLA", "revenue_apla", M0), ("Converse", "revenue_converse", M0), ("NIKE Direct", "revenue_nike_direct", M0),
    ("Wholesale", "revenue_wholesale", M0)], period_label=ql,
    note="Q4 NIKE Direct and wholesale appear in the Q4 releases only rounded to $ billions (for example 4.1 = $4.1 billion)."))
parts.append(table("Greater China growth by quarter (%)", [f"Q{q}FY{y}" for y in (2023, 2024, 2025, 2026) for q in (1, 2, 3, 4)] + ["Q1FY2027"], [
    ("Reported", "growth_greater_china_reported_pct", M0), ("Currency-neutral", "growth_greater_china_cn_pct", M0)], period_label=ql))
parts.append(table("Quarter-end balances", QE, [
    ("Cash", "cash_and_equivalents", M0), ("ST investments", "short_term_investments", M0), ("Inventories", "inventories", M0),
    ("Current LTD", "current_portion_long_term_debt", M0), ("Long-term debt", "long_term_debt", M0), ("Equity", "shareholders_equity", M0)]))

parts.append("""## 6. Key disclosures quoted from the filings

| Topic | What the filing says | Source |
|---|---|---|
| IEEPA tariff recovery | Q4 FY2026 gross margin "increased 890 basis points to 49.2 percent ... The expected recovery of the IEEPA tariffs of $986 million increased gross margin by approximately 900 basis points." Q4 diluted EPS of $0.72 included "a $0.52 benefit related to the expected recovery of the IEEPA tariffs." $965M was booked in North America and $21M in Converse. | Q4 FY2026 release p. 1 and divisional revenues footnote; FY2026 10-K |
| IEEPA cash | FY2026 cash from operations "includes approximately $0.3 billion of cash received from IEEPA tariff recoveries." | Q4 FY2026 release p. 1 |
| FY2027 outlook | "Revenues are expected to decline high-single digits in fiscal 2027." Effective tax rate "expected to be in the mid-20 percent range." "Adjusted Diluted earnings per share is expected to be in the range of $1.15 to $1.35, which excludes approximately $0.15 of restructuring expenses related to Pace." | Q1 FY2027 release p. 1 |
| Pace program | "approximately $2.5 billion in cumulative savings through fiscal 2031, with approximately $1.0 billion of pre-tax charges, primarily consisting of employee-related costs, through fiscal 2031, in addition to approximately $0.3 billion of severance costs recognized in fiscal 2026." Includes "a new campus in India." Builds on "the previous cost realignment plan announced in March 2026." | Q1 FY2027 release p. 1; 8-K filed Oct 1, 2026 (Item 2.05) p. 2 |
| Geography change | "NIKE plans to organize into three geographies in fiscal 2028." | Q1 FY2027 10-Q |
| March 2026 plan | About $300M of pre-tax charges, primarily severance, substantially all in Q3 FY2026; no headcount stated. | 8-K filed Mar 5, 2026 (Item 2.05) p. 2 |
| FY2024 restructuring | $443M of restructuring charges in FY2024 ($392M severance); no savings target or headcount stated. | FY2024 10-K |
| FY2020 charges | $200M to $250M employee termination costs; $405M impairment on moving Brazil, Argentina, Chile and Uruguay to distributors. | FY2020 10-K |
| Q1 FY2027 margin | Gross margin rose 60 bps to 42.8%; lower warehousing and logistics costs added about 90 bps. | Q1 FY2027 10-Q p. 19 |
| Dividend | Quarterly dividend raised to $0.41 from $0.40 in Q2 FY2026; $0.41 declared in Q1 FY2027. | Q2 FY2026 10-Q; Q1 FY2027 10-Q p. 5 |
| Tariff cost estimate | "As a result of new tariffs, we expect a gross incremental cost of approximately $1.5 billion on an annualized basis." Not repeated in the Q3 FY2026 or Q1 FY2027 10-Qs. | Q1 FY2026 10-Q p. 19; Q2 FY2026 10-Q p. 23 |
| IEEPA before Q4 | As of April 1, 2026, "Total IEEPA tariffs paid ... is approximately $1.0 billion" and recovery was judged "not probable"; the receivable was collected in Q1 FY2027 (amount not stated in the 10-Q). | Q3 FY2026 10-Q p. 26; Q1 FY2027 10-Q |
| China and Converse outlook | "The actions related to Converse are expected to continue throughout fiscal 2027 and for Greater China to extend beyond fiscal 2027." | Q1 FY2027 10-Q p. 20 |
| Campion separation | "one-time cash compensation amount of $2,750,000 under a Separation and Release Agreement." | Q2 FY2024 10-Q p. 47 |
| Shares outstanding | 1,483,498,703 (281,387,752 Class A and 1,202,110,951 Class B) at July 8, 2026; 1,485,308,829 on the Q1 FY2027 10-Q cover. | FY2026 10-K cover; 2026 proxy p. 76; Q1 FY2027 10-Q cover |

## 7. Items checked against the full text of every filing

Confirmed in filings (previously unverified):
- Dec 2023 plan: Nike was "identifying opportunities to deliver up to $2 billion in cumulative cost savings over the next three years" and expected "pre-tax restructuring charges of approximately $400 million to $450 million primarily associated with employee severance" (8-K filed Dec 21, 2023, Item 2.05, p. 2; Q2 FY2024 10-Q p. 22).
- Tariffs: "we expect a gross incremental cost of approximately $1.5 billion on an annualized basis" (Q1 FY2026 10-Q p. 19; Q2 FY2026 10-Q p. 23).
- Geography change: Nike's "four Geographies" (Dec 2025 leadership announcement, 8-K Ex. 99.1 filed Dec 2, 2025) become "three geographies in fiscal 2028" (Q1 FY2027 10-Q; Oct 1, 2026 8-K).

Not in any filing (a text search of all 102 documents found nothing), so the report sources them to opened Nike, WARN or news pages or drops them:
- Layoff headcounts (Feb 2024 "more than 1,500", Jan 2026 "around 775", Apr 2026 "about 1,400"). Filings describe "a net reduction in the Company's global workforce" and the charges, never a count.
- The Q2 FY2027 "400 bps Cyber Week" headwind (likely from the earnings call; dropped).
- "Bengaluru" (filings say "a new campus in India"; Nike's Oct 1, 2026 employee memo names Bengaluru).
- Stock prices, index membership and analyst targets are market data, not filing data; see `data/nke_daily_prices.csv` (Yahoo Finance) and the report's labelling.

## 8. Filing URLs
""")
parts.append("\n".join(f"- {k}: {u}" for k, u in URLS.items()) + "\n")
open(os.path.join(ROOT, "research_notes", "04_financial_data_pack.md"), "w").write("\n".join(parts))
print("ok", len(URLS), "filings cited")
