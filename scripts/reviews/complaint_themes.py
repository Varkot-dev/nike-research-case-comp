"""Share of Amazon reviews (summary + text) mentioning counterfeit, used-item, quality-failure and sizing themes, by firm and Nike fiscal year."""
import sys, pandas as pd
D = sys.argv[1]
r = pd.read_csv(f"{D}/amazon_reviews_filtered.csv.gz", usecols=["parent_asin", "rating", "title", "text", "timestamp"])
r = r.merge(pd.read_csv(f"{D}/matched_products.csv.gz", usecols=["parent_asin", "firm"]), on="parent_asin")
r["date"] = pd.to_datetime(r.timestamp, unit="ms"); r["fy"] = r.date.dt.year + (r.date.dt.month >= 6)
r = r[(r.fy >= 2017) & (r.fy <= 2023)]
s = (r.title.fillna("") + " " + r.text.fillna("")).str.lower()
r["fake"] = s.str.contains(r"\bfake\b|counterfeit|not authentic|not genuine|knock ?off|replica")
r["used"] = s.str.contains(r"\bused\b.{0,20}(?:shoe|pair|item)|worn before|been worn|dirty|scuff")
r["size"] = s.str.contains(r"runs? (?:small|big|large)|too (?:small|big|tight)|size (?:up|down)")
r["quality"] = s.str.contains(r"fell apart|fall apart|came apart|ripped|tore|broke|falling apart|cheap(?:ly)? made|poor quality|sole (?:came|separat)")
r.groupby(["firm", "fy"])[["fake", "used", "quality", "size"]].mean().reset_index().to_csv(f"{D}/amazon_complaint_themes_by_fy.csv", index=False, float_format="%.4f")
