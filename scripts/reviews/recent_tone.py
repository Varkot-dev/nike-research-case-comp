"""Part 2: apply the Amazon-trained Naive Bayes (15k summaries) and VADER to recent review titles from nike.com (TurnTo)
and Foot Locker (Bazaarvoice), then quarterly metrics and AbnormalTone per brand.
Usage: python3 -I recent_tone.py <data_dir>"""
import sys, pickle, numpy as np, pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
D = sys.argv[1]; vec, nb = pickle.load(open(f"{D}/nb_model_15k.pkl", "rb")); cls = list(nb.classes_); sia = SentimentIntensityAnalyzer()
def tone(titles):
    P = nb.predict_proba(vec.transform(titles)); return P[:, cls.index("pos")] - P[:, cls.index("neg")]
frames = []
nk = pd.read_csv(f"{D}/nike_com_reviews.csv.gz"); nk["source"] = "nike.com"; nk["brand"] = "Nike (nike.com)"; frames.append(nk)
try:
    fl = pd.read_csv(f"{D}/footlocker_bv_reviews.csv.gz"); fl["date"] = fl["submitted"].str[:10]; fl["source"] = "footlocker"
    fl["syndicated"] = fl["is_syndicated"].astype(str) == "True"; frames.append(fl)
except FileNotFoundError: pass
df = pd.concat(frames, ignore_index=True)
df["title"] = df["title"].fillna("").astype(str).replace({"None": ""}).str.strip()
df["date"] = pd.to_datetime(df["date"]); df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
df = df[(df.date >= "2021-06-01") & (df.date < "2026-10-01")]
h = df.title.str.len() > 0
df.loc[h, "tone_nb"] = tone(df.loc[h, "title"]); df.loc[h, "tone_vader"] = [sia.polarity_scores(t)["compound"] for t in df.loc[h, "title"]]
fy = df.date.dt.year + (df.date.dt.month >= 6).astype(int); fq = ((df.date.dt.month - 6) % 12) // 3 + 1
df["fis_q"] = "Q" + fq.astype(str) + "FY" + fy.astype(str); df["qsort"] = fy * 10 + fq
df["unit"] = np.where(df.source == "nike.com", "Nike (nike.com)", "FL: " + df["brand"].astype(str))
df.loc[(df.source == "footlocker") & df.brand.isin(["Nike", "Jordan", "Converse"]), "firm"] = "FL: Nike Inc"
rows = []
def q(x, unit):
    g = x.groupby(["qsort", "fis_q"]).agg(review_cnt=("rating", "size"), products=("product_id" if "product_id" in x and x["product_id"].notna().any() else "style", "nunique"),
        avg_rating=("rating", "mean"), share_1_2_star=("rating", lambda r: (r <= 2).mean()), titles=("tone_nb", "count"),
        avg_tone_nb=("tone_nb", "mean"), avg_tone_vader=("tone_vader", "mean"),
        share_incentivized=("incentivized", lambda r: (r.astype(str) == "True").mean())).reset_index()
    g["unit"] = unit; return g
for u, x in df.groupby("unit"): rows.append(q(x, u))
fln = df[df.firm == "FL: Nike Inc"]
if len(fln): rows.append(q(fln, "FL: Nike Inc (Nike+Jordan+Converse)"))
fl_native = df[(df.source == "footlocker") & (~df.get("syndicated", pd.Series(False, index=df.index)).fillna(False).astype(bool))]
for u, x in fl_native.groupby("unit"): rows.append(q(x, u + " [native FL only]"))
nki = df[(df.source == "nike.com") & (df["incentivized"].astype(str) != "True")]
rows.append(q(nki, "Nike (nike.com) [non-incentivized only]"))
out = pd.concat(rows).sort_values(["unit", "qsort"])
def prev4(s):
    return s.shift(1).rolling(4, min_periods=4).mean()
res = []
for u, x in out.groupby("unit"):
    x = x.set_index("qsort").reindex(range(x.qsort.min(), x.qsort.max() + 1))
    x = x[x.index % 10 <= 4].copy(); x = x[x.index % 10 >= 1]
    x["unit"] = u
    for c, a in (("avg_tone_nb", "AbnormalTone"), ("avg_tone_vader", "AbnormalTone_vader"), ("avg_rating", "AbnormalRating")):
        x[a] = x[c] - prev4(x[c])
    x["AbnormalReviewCnt"] = (x["review_cnt"] - prev4(x["review_cnt"])) / 100
    x["Negative_AbnormalTone"] = x["AbnormalTone"].clip(upper=0)
    res.append(x.reset_index())
out = pd.concat(res); out = out[out.fis_q.notna()]
out.to_csv(f"{D}/recent_reviews_quarterly_fiscal.csv", index=False, float_format="%.4f")
df.drop(columns=["text"], errors="ignore").to_csv(f"{D}/recent_reviews_scored.csv.gz", index=False, compression="gzip")
print(out.groupby("unit").size())
