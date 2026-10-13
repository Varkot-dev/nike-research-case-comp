"""Join segment revenue, channel split, EBIT and gross margin into one region-by-year table.
Inputs: data/nike_filing_facts.csv and data/nike_channel_split.csv (both cited to filing pages).
Output: data/nike_region_profitability.csv. Every computed column is derived (my arithmetic).
Usage: python3 scripts/build_region_channel.py"""
import csv, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
FACTS = {(r["metric"], r["period"]): r for r in csv.DictReader(open(ROOT / "data/nike_filing_facts.csv"))}
SPLIT = {(r["period"], r["segment"], r["channel"]): r for r in csv.DictReader(open(ROOT / "data/nike_channel_split.csv"))}
REGIONS = ["north_america", "emea", "greater_china", "apla", "converse"]
YEARS = [f"FY{y}" for y in range(2019, 2027)]


def fact(metric, period):
    r = FACTS.get((metric, period))
    return (float(r["value"]), f'{r["filing"]} {r["page"]}') if r else (None, "")


rows = []
for fy in YEARS:
    for seg in REGIONS:
        total = SPLIT.get((fy, seg, "total"))
        direct = SPLIT.get((fy, seg, "direct"))
        wholesale = SPLIT.get((fy, seg, "wholesale"))
        if not (total and direct and wholesale):
            continue
        rev, d, w = (float(x["value_usd_m"]) for x in (total, direct, wholesale))
        ebit, ebit_src = fact(f"ebit_{seg}", fy)
        gm, gm_src = fact(f"gross_margin_{seg}_pct", fy)
        rows.append({
            "period": fy, "segment": seg,
            "revenue_usd_m": round(rev), "direct_usd_m": round(d), "wholesale_usd_m": round(w),
            "direct_share_pct": round(100 * d / (d + w), 1),
            "ebit_usd_m": ebit, "ebit_margin_pct": round(100 * ebit / rev, 1) if ebit is not None else "",
            "gross_margin_pct": gm if gm is not None else "",
            "channel_source": f'{total["doc"]} p. {total["printed_page"]}',
            "ebit_source": ebit_src, "gross_margin_source": gm_src,
            "basis": "revenue, channel, EBIT and gross margin as reported; shares and EBIT margin derived (my arithmetic)",
        })

out = ROOT / "data/nike_region_profitability.csv"
with open(out, "w", newline="") as f:
    wr = csv.DictWriter(f, fieldnames=list(rows[0]))
    wr.writeheader()
    wr.writerows(rows)
print(f"wrote {len(rows)} rows to {out.relative_to(ROOT)}")
