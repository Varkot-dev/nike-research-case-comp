"""Hand-curated tracker of dated forward-looking promises, built from promise_candidates.csv and the
CFO outlook sections. Every quote is verified word for word against the transcript (raises if absent).

Usage: python3 -I 08_promise_tracker.py <out_dir>
Outputs promise_tracker.csv (one row per promise) and promise_events.csv (every restatement).
event kinds: made, reaffirmed, cut (target lowered), raised, pushed (date moved later),
declared_done, reversed (later call contradicts a 'done'), dropped (no longer mentioned or withdrawn).
score: kept, kept_late, beat, missed, partly, pending, pending_at_risk.
Only promises that management controlled the wording of are scored (negative guides such as
'Direct will not grow' are tracked but flagged as negative_guide=1).
"""
import csv, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from pagefind import find_page_strict

P = [
 dict(id="D01", era="Donahoe", topic="inventory", target="end of Q2 FY21 (Nov 2020)", neg=0,
      ev=[("Q1FY21","made","our top priority is to normalize inventory by the end of the second quarter"),
          ("Q2FY21","declared_done","marketplace health has been restored across all geographies")],
      outcome="Achieved on time per Q2 FY21 call.", score="kept"),
 dict(id="D02", era="Donahoe", topic="revenue", target="FY22 revenue growth low double digits, above $50B", neg=0,
      ev=[("Q4FY21","made","In Fiscal 22, we expect Revenue to grow low double-digits and surpass $50 billion"),
          ("Q1FY22","cut","We now expect fiscal 2022 revenue to grow mid-single-digits versus the prior year")],
      outcome="FY22 revenue $46,710M, +5% (FY22 10-K p. 56). Cut was blamed on Vietnam factory closures.", score="missed"),
 dict(id="D03", era="Donahoe", topic="gross_margin", target="FY22 gross margin +125 to 150 bp", neg=0,
      ev=[("Q4FY21","made","We expect Gross Margin to expand 125 to 150 basis points"),
          ("Q2FY22","raised","We are raising our Gross Margin guidance to expand 150 basis points versus the prior year"),
          ("Q3FY22","raised","We now expect gross margin to expand by at least 150 basis points versus the prior year")],
      outcome="FY22 gross margin 46.0% vs 44.8%, +120 bp (FY22 10-K p. 31; FY21 10-K p. 31): below the raised 'at least 150 bp'.", score="missed"),
 dict(id="D04", era="Donahoe", topic="long_term_revenue", target="FY22 to FY25 revenue growth high single to low double digits on average", neg=0,
      ev=[("Q4FY21","made","we expect Revenue growth to inflect upwards to a range of high single digit to low double digit growth on average"),
          ("Q1FY22","reaffirmed","transforming our financial model toward the long-term fiscal 2025 financial outlook I shared last quarter"),
          ("Q3FY22","reaffirmed","we remain confident we are on track towards our long-term financial goals"),
          ("Q1FY23","reaffirmed","we are optimistic as we continue to make progress towards our long-term financial goals"),
          ("Q2FY23","reaffirmed","we remain on a path toward our long-term goals as well"),
          ("Q1FY24","reaffirmed","And we still believe those long-term goals of profitability are achievable"),
          ("Q1FY25","dropped","we have also decided to postpone our Investor Day")],
      outcome="FY21 to FY25 revenue CAGR +1.0% ($44,538M to $46,309M; FY21 10-K p. 57, FY25 10-K p. 32; my arithmetic).", score="missed"),
 dict(id="D05", era="Donahoe", topic="long_term_gross_margin", target="gross margin in the high 40s by FY25", neg=0,
      ev=[("Q4FY21","made","We now see Gross Margin rate reaching the high 40s by fiscal 25"),
          ("Q2FY22","reaffirmed","and on what is required to deliver on our Fiscal '25 financial outlook")],
      outcome="FY25 gross margin 42.7% (FY25 10-K p. 32).", score="missed"),
 dict(id="D06", era="Donahoe", topic="long_term_ebit", target="EBIT margin high teens by FY25", neg=0,
      ev=[("Q4FY21","made","we see our EBIT margin reaching high-teens by fiscal 25"),
          ("Q3FY22","reaffirmed","which will enable us to hit that high teens operating profit over the multiyear period"),
          ("Q1FY24","reaffirmed","And we still believe those long-term goals of profitability are achievable")],
      outcome="FY25 EBIT margin 8.2% (Q4 FY25 release p. 6).", score="missed"),
 dict(id="D07", era="Donahoe", topic="china", target="Greater China low-to-mid-teens growth over the long term", neg=0,
      ev=[("Q4FY21","made","we are optimistic that we can continue to grow low-to-mid-teens over the long-term")],
      outcome="Greater China revenue $8,290M (FY21) to $5,847M (FY26), about -7% a year (FY21 10-K p. 36, FY26 10-K p. 36; my arithmetic).", score="missed"),
 dict(id="D08", era="Donahoe", topic="gross_margin", target="FY23 gross margin flat to -50 bp", neg=0,
      ev=[("Q4FY22","made","We expect gross margins to be in the range of flat to declining by 50 basis points versus the prior year"),
          ("Q1FY23","cut","We now expect gross margin to decline between 200 to 250 basis points versus the prior year"),
          ("Q3FY23","cut","We expect Fiscal '23 gross margin to decline approximately 250 basis points, at the low end of our previous guidance range")],
      outcome="FY23 gross margin 43.5% vs 46.0%, -250 bp (FY23 10-K p. 31).", score="missed"),
 dict(id="D09", era="Donahoe", topic="revenue", target="FY23 revenue growth low double digits currency-neutral", neg=0,
      ev=[("Q4FY22","made","We expect Revenue for the full year to grow low double-digits on a currency-neutral basis"),
          ("Q2FY23","raised","we now expect full year revenue to grow low teens on a currency-neutral basis")],
      outcome="FY23 currency-neutral revenue +16% (Q4 FY23 release p. 4).", score="beat"),
 dict(id="D10", era="Donahoe", topic="inventory", target="healthy pull market by end of Q2 FY23 (Nov 2022)", neg=0,
      ev=[("Q4FY22","made","our focus is on getting to a healthy pull market by the end of the second quarter"),
          ("Q1FY23","reaffirmed","we're increasingly confident that our inventory will be normalized by the end of this coming quarter"),
          ("Q2FY23","pushed","prioritizing our brand getting to a healthy inventory position by the end of this fiscal year"),
          ("Q3FY23","reaffirmed","we are on track to hit our FY23 priorities of getting inventory in a healthy position"),
          ("Q4FY23","declared_done","a robust product innovation pipeline, healthy inventory, and a normalized flow of supply")],
      outcome="Reached about two quarters late (end of FY23 instead of end of Q2 FY23).", score="kept_late"),
 dict(id="D11", era="Donahoe", topic="revenue", target="FY24 revenue growth mid single digits", neg=0,
      ev=[("Q4FY23","made","For the full year we expect Fiscal '24 reported revenue to grow mid-single digits, led by Nike Direct"),
          ("Q1FY24","reaffirmed","For the full year we continue to expect reported revenue to grow mid-single digits"),
          ("Q2FY24","cut","with full year reported revenue now growing approximately 1%")],
      outcome="FY24 revenue $51,362M vs $51,217M, +0.3% (FY24 10-K p. 57; FY23 10-K p. 31).", score="missed"),
 dict(id="D12", era="Donahoe", topic="gross_margin", target="FY24 gross margin +140 to 160 bp", neg=0,
      ev=[("Q4FY23","made","We expect gross margins to expand 140 to 160 basis points on a reported basis"),
          ("Q2FY24","reaffirmed","We continue to expect full year gross margins to expand 140 to 160 basis points"),
          ("Q3FY24","cut","this translates into gross margins expanding approximately 120 basis points")],
      outcome="FY24 gross margin 44.6% vs 43.5%, +110 bp (FY24 10-K p. 33).", score="missed"),
 dict(id="D13", era="Donahoe", topic="revenue", target="FY25 revenue and earnings growth, margins expanding", neg=0,
      ev=[("Q3FY24","made","We expect revenue and earnings to grow versus the prior year, with operating margins expanding"),
          ("Q3FY24","made","But we believe we will inflect in the second half and grow next year on the top line"),
          ("Q4FY24","cut","we now expect Fiscal 25 reported revenue to be down mid-single-digits, with the first half down high single-digits"),
          ("Q1FY25","dropped","we are withdrawing our full year guidance")],
      outcome="FY25 revenue -10% (Q4 FY25 release p. 1); diluted EPS $2.16 vs $3.73 (FY25 10-K p. 56; FY24 10-K p. 57); EBIT margin 8.2% vs 12.7%.", score="missed"),
 dict(id="X01", era="Donahoe", topic="investor_day", target="Investor Day with 5-year algorithm, late 2024", neg=0,
      ev=[("Q3FY24","made","And we look forward to sharing our plans in-depth at an Investor Day later this year"),
          ("Q4FY24","reaffirmed","At Investor Day in November, we will provide an updated outlook on growth and profitability"),
          ("Q1FY25","dropped","we have also decided to postpone our Investor Day"),
          ("Q3FY26","pushed","we will return to providing full year and long-term guidance at our Investor Day in the fall"),
          ("Q1FY27","reaffirmed","in November, we're going to give you a financial algorithm")],
      outcome="Postponed about two years; now scheduled Nov 16 to 17, 2026.", score="pending"),
 dict(id="H01", era="Hill", topic="trough", target="Q4 FY25 is the worst quarter; headwinds moderate after", neg=0,
      ev=[("Q3FY25","made","we believe that the fourth quarter will reflect the largest impact from our Win Now actions, and that the headwinds to revenue and gross margin will begin to moderate from there")],
      outcome="Q4 FY25 revenue -12%, gross margin -440 bp; then Q1 FY26 +1%/-320 bp, Q2 FY26 +1%/-300 bp, Q3 FY26 0%/-130 bp (10-Qs and releases; my arithmetic).", score="kept"),
 dict(id="H02", era="Hill", topic="clean_marketplace", target="healthy and clean marketplace by end of 1H FY26 (Nov 2025)", neg=0,
      ev=[("Q3FY25","made","We expect these actions will continue through the first half of Fiscal 2026"),
          ("Q4FY25","reaffirmed","We remain on track for a healthy and clean market by the end of the first half of fiscal '26"),
          ("Q1FY26","reaffirmed","we have made steady progress on our plans for a healthy marketplace by the end of the first half of fiscal '26"),
          ("Q2FY26","declared_done","In North America and EMEA, which represent almost 3/4 of our business, we have returned to a healthy marketplace"),
          ("Q3FY26","reversed","while we expect to exit the fourth quarter with elevated inventory in EMEA"),
          ("Q3FY26","pushed","we have a clear set of plans in place to complete our Win Now actions by the end of the calendar year"),
          ("Q4FY26","reversed","EMEA continues to work through heightened inventory and promotional levels"),
          ("Q1FY27","pushed","we proactively work with our wholesale partners to work through excess inventory to create a healthy marketplace"),
          ("Q1FY27","pushed","We expect those actions will create pressure on reported revenues for the remainder of fiscal '27 and into '28")],
      outcome="Declared done for North America and EMEA in Dec 2025, reversed for EMEA three months later and for North America sportswear in Oct 2026; supply cuts now run into FY28.", score="missed"),
 dict(id="H03", era="Hill", topic="win_now_completion", target="Win Now actions finished by end of calendar 2026", neg=0,
      ev=[("Q3FY26","made","By the end of the calendar year, we expect to have finished our Win Now actions"),
          ("Q4FY26","reaffirmed","And we do remain on track to sunset the Win Now actions by the end of this calendar year"),
          ("Q1FY27","dropped","through a program we're calling Pace")],
      outcome="'Win Now' is not mentioned once in the Q1 FY27 call (0 vs 16 to 24 mentions a call before); replaced by the Pace program with savings mostly in FY29 to FY30.", score="pending_at_risk"),
 dict(id="H04", era="Hill", topic="wholesale", target="wholesale returns to modest growth in FY26", neg=0,
      ev=[("Q1FY26","made","we expect wholesale revenue to return to modest growth for fiscal '26")],
      outcome="FY26 wholesale $27,453M vs $25,883M, +6.1% (FY26 10-K p. 32; FY25 10-K p. 33; my arithmetic).", score="beat"),
 dict(id="H05", era="Hill", topic="direct", target="NIKE Direct does not return to growth in FY26", neg=1,
      ev=[("Q1FY26","made","we do not expect NIKE Direct to return to growth for fiscal '26")],
      outcome="FY26 NIKE Direct $17,720M vs $18,783M, -5.7% (FY26 10-K p. 32; FY25 10-K p. 33).", score="kept"),
 dict(id="H06", era="Hill", topic="revenue", target="Q4 FY26 to Q2 FY27 revenue down low single digits", neg=0,
      ev=[("Q3FY26","made","We expect revenues to be down low single digits versus the prior year with gains in North America offset by declines in Greater China"),
          ("Q4FY26","cut","We now expect revenue to be down low to midsingle digits"),
          ("Q1FY27","cut","For fiscal '27, we currently expect revenues to decline in the high single-digit range")],
      outcome="Q4 FY26 -1%, Q1 FY27 -4% so far; window cut once, then full-year FY27 set at a high single digit decline, which implies a weaker second half.", score="missed"),
 dict(id="H07", era="Hill", topic="gross_margin", target="gross margin expansion from Q2 FY27", neg=0,
      ev=[("Q3FY26","made","We expect gross margin expansion to begin in the second quarter"),
          ("Q4FY26","raised","We now expect gross margin expansion earlier beginning in Q1"),
          ("Q1FY27","cut","This outlook reflects continued pressure on gross margin")],
      outcome="Q1 FY27 gross margin 42.8% vs 42.2%, +60 bp (Q1 FY27 10-Q p. 22). FY27 gross margin no longer guided.", score="partly"),
 dict(id="H08", era="Hill", topic="earnings", target="earnings flattish Q4 FY26 to Q2 FY27", neg=0,
      ev=[("Q3FY26","made","We expect earnings to be flattish with gross margins beginning to inflect"),
          ("Q4FY26","reaffirmed","We reiterate our expectation for earnings to be flattish over that time period, excluding the benefit from tariff recovery")],
      outcome="Q1 FY27 diluted EPS $0.48 vs $0.49 (Q1 FY27 10-Q p. 1); Q2 FY27 reported about Dec 17, 2026.", score="pending"),
 dict(id="H09", era="Hill", topic="tariff", target="Q1 FY27 last quarter of material tariff headwind", neg=0,
      ev=[("Q3FY26","made","we expect the first quarter of fiscal '27 to be the final quarter where higher tariffs continue to be a material year-over-year headwind to gross margin")],
      outcome="The word 'tariff' does not appear in the Q1 FY27 call; Q1 gross margin rose 60 bp.", score="pending"),
 dict(id="H10", era="Hill", topic="fy28_benefits", target="restructuring benefits start FY27 and build through FY28", neg=0,
      ev=[("Q3FY26","made","We expect benefits from these actions to begin in fiscal '27 and continue to build through fiscal '28"),
          ("Q1FY27","pushed","expect the majority of the program savings to be realized in fiscal years '29 and '30")],
      outcome="The new Pace program puts most of its $2.5B savings in FY29 to FY30; the FY27 to FY28 benefit language was not repeated.", score="pending_at_risk"),
 dict(id="H11", era="Hill", topic="margin_ambition", target="return to double-digit EBIT margins (no date)", neg=0,
      ev=[("Q4FY25","made","And over time, we absolutely have the ambition to get back to double-digit operating margins"),
          ("Q1FY26","reaffirmed","As I look longer term, I think that we continue to believe that double-digit margins are something that are achievable"),
          ("Q2FY26","reaffirmed","While it will take time, we see the path back to double-digit EBIT margins for NIKE, Inc"),
          ("Q3FY26","reaffirmed","it is a critical step in our return to double-digit EBIT margins"),
          ("Q4FY26","reaffirmed","contribute to this trajectory to get back to double-digit margins as you referenced"),
          ("Q1FY27","cut","We currently expect EBIT to decline by a greater percentage than revenue")],
      outcome="Never dated in six calls. FY26 EBIT margin 8.3% (FY26 10-K p. 31); FY27 guided lower.", score="pending"),
 dict(id="H12", era="Hill", topic="classics", target="classics down more than $4B from peak by end of FY26", neg=1,
      ev=[("Q2FY26","made","The Classics footwear franchises are on track to decline from peak levels by more than $4 billion by fiscal year-end"),
          ("Q3FY26","reaffirmed","by the end of this fiscal year, we will have intentionally reduced over $4 billion of revenue from the peak levels of classic footwear franchises")],
      outcome="Management-reported; not separately disclosed in filings.", score="kept"),
 dict(id="H13", era="Hill", topic="china", target="China recovery (never dated)", neg=1,
      ev=[("Q4FY25","made","China will take longer due to the unique characteristics of the marketplace"),
          ("Q1FY26","reaffirmed","we expect revenue and gross margin headwinds from Greater China and Converse to continue throughout fiscal '26"),
          ("Q2FY26","reaffirmed","that's where it gets tough to put an exact date on it"),
          ("Q1FY27","cut","assumes that China actually gets worse from a revenue perspective for the balance of this year")],
      outcome="Greater China revenue $1,180M in Q1 FY27, -22% vs $1,512M (Q1 FY27 10-Q p. 25; Q1 FY26 release p. 4; my arithmetic). No recovery date has ever been given.", score="missed"),
]

def main(out_dir):
    out_dir = pathlib.Path(out_dir)
    events, rows = [], []
    for p in P:
        pushes = cuts = reaff = 0
        for q, kind, quote in p["ev"]:
            pg = find_page_strict(q, quote)
            if pg is None:
                raise SystemExit(f"{p['id']}: quote not found in {q}: {quote}")
            events.append({"promise_id": p["id"], "quarter": q, "kind": kind, "page": pg, "quote": quote})
            pushes += kind == "pushed"; cuts += kind == "cut"; reaff += kind == "reaffirmed"
        first = p["ev"][0]
        rows.append({"promise_id": p["id"], "era": p["era"], "topic": p["topic"], "target": p["target"],
                     "negative_guide": p["neg"], "made_in": first[0], "made_page": events[-len(p["ev"])]["page"],
                     "first_quote": first[2], "n_statements": len(p["ev"]), "times_reaffirmed": reaff,
                     "times_pushed": pushes, "times_cut": cuts,
                     "times_pushed_or_cut": pushes + cuts, "outcome": p["outcome"], "score": p["score"]})
    for name, data in (("promise_tracker.csv", rows), ("promise_events.csv", events)):
        with open(out_dir / name, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(data[0])); w.writeheader(); w.writerows(data)
    print(len(rows), "promises,", len(events), "statements, all quotes verified")

if __name__ == "__main__":
    main(sys.argv[1])
