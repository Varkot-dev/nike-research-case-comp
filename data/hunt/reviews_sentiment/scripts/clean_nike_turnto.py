"""Tidy nike.com TurnTo reviews: model name from TurnTo catalog title, launch cohorts and monthly counts.
Outputs: nike_reviews_tidy.csv.gz (one row per review, no text/user), nike_reviews_monthly_by_model.csv, nike_launch_cohorts.csv"""
import sys, re, pandas as pd, numpy as np
raw = sys.argv[1]
r = pd.read_csv(raw + "/nike_turnto_reviews.csv.gz").drop_duplicates("review_id")
r["date"] = pd.to_datetime(r.created_ms, unit="ms"); r["month"] = r.date.dt.to_period("M").astype(str)
def model(t):
    t = str(t).replace("Nike ", "").replace("Air Zoom ", "")
    t = re.split(r" (Men's|Women's|Women’s|Men’s|Big Kids'|Older Kids'|Road|Shoes)", t)[0]
    t = re.sub(r"\s+(SE|Premium|Electric|By You)$", lambda m: " " + m.group(1), t).strip()
    return t
r["model"] = r.item_title.map(model)
r["gender"] = np.where(r.item_title.str.contains("Women", na=False), "W", np.where(r.item_title.str.contains("Men", na=False), "M", "U"))
r["family"] = r.model.str.extract(r"^(Pegasus Trail|Pegasus Plus|Pegasus Premium|Pegasus|Vomero Plus|Vomero Premium|Vomero|Structure Plus|Structure|Invincible|InfinityRN|Revolution|Downshifter|Winflo|Vaporfly|Alphafly|Zoom Fly|Journey Run|Quest|Air Force 1|Dunk Low|Air Jordan 1|Zoom Vomero 5|Air Max 90|Cortez)", expand=False)
r["gen"] = r.model.str.extract(r"(\d+)\s*$", expand=False)
r["incentivized"] = r.incentivized.astype(str).str.lower().eq("true")
r["us"] = r.locale.eq("en_US")
keep = ["review_id", "style", "item_title", "model", "family", "gen", "gender", "date", "month", "rating", "incentivized", "incentivized_type", "recommended", "fit", "comfort", "locale", "us", "has_media", "purchase_date"]
r[keep].to_csv("nike_reviews_tidy.csv.gz", index=False, compression="gzip")
m = r.groupby(["family", "model", "month"]).agg(reviews=("review_id", "size"), us_reviews=("us", "sum"), organic=("incentivized", lambda s: int((~s).sum())),
                                                avg_rating=("rating", "mean"), share_1_2=("rating", lambda s: float((s <= 2).mean()))).reset_index()
m.to_csv("nike_reviews_monthly_by_model.csv", index=False)
# launch cohorts: per model (M+W pooled), first review date = launch proxy; counts within 90/180/365 days
rows = []
for (fam, mod), g in r.groupby(["family", "model"]):
    t0 = g.date.min()
    t0r = g.date.quantile(0.02)  # robust launch: 2nd percentile (drops stray early reviews)
    row = dict(family=fam, model=mod, gen=g.gen.iloc[0], first_review=t0.date(), launch_proxy=t0r.date(), total=len(g), last_review=g.date.max().date())
    age = (pd.Timestamp("2026-10-13") - t0r).days; row["age_days"] = age
    for D in (90, 180, 270, 365):
        w = g[(g.date >= t0r) & (g.date < t0r + pd.Timedelta(days=D))]
        row[f"n{D}"] = len(w) if age >= D else np.nan
        row[f"organic_us_n{D}"] = int((w.us & ~w.incentivized).sum()) if age >= D else np.nan
        row[f"rating{D}"] = w.rating.mean() if age >= D and len(w) else np.nan
        row[f"organic_rating{D}"] = w[~w.incentivized].rating.mean() if age >= D and len(w) else np.nan
        row[f"incent_share{D}"] = w.incentivized.mean() if age >= D and len(w) else np.nan
    rows.append(row)
pd.DataFrame(rows).sort_values(["family", "launch_proxy"]).to_csv("nike_launch_cohorts.csv", index=False)
print(len(r))
