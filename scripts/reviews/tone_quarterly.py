"""Part 1: Jin (2023) style tone measures on Amazon Reviews 2023 (McAuley Lab) for Nike Inc and competitors.
Inputs: data/matched_products.csv, data/amazon_reviews_filtered.csv.gz. Outputs: tone-scored reviews (parquet) and quarterly CSVs."""
import pandas as pd, numpy as np, re, json, sys, os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
D = sys.argv[1]
prod = pd.read_csv(f"{D}/matched_products.csv.gz", usecols=["parent_asin", "brand", "firm", "footwear"])
rv = pd.read_csv(f"{D}/amazon_reviews_filtered.csv.gz")
rv = rv.merge(prod, on="parent_asin", how="inner")
n0 = len(rv)
rv["title"] = rv["title"].fillna("").astype(str).str.strip(); rv["text"] = rv["text"].fillna("").astype(str)
# duplicates: same user+product+time, and identical (summary,text) pairs with substantive text (paper drops duplicate reviews even across users)
rv = rv.drop_duplicates(["user_id", "parent_asin", "timestamp"])
long = rv["text"].str.len() > 40
rv = pd.concat([rv[~long], rv[long].drop_duplicates(["title", "text"])])
rv["date"] = pd.to_datetime(rv["timestamp"], unit="ms")
rv = rv[(rv.date >= "2005-01-01") & (rv.date < "2023-10-01")]
print("reviews matched", n0, "after dedupe/date", len(rv))
rv["label"] = np.select([rv.rating >= 4, rv.rating <= 2], ["pos", "neg"], "neu")
has = rv["title"].str.len() > 0
# --- Naive Bayes per Appendix C: 15,000 random summaries, 80/20 split; labels from stars (deviation: paper used two human coders)
rng = 20231910
def fit_nb(n):
    s = rv[has].sample(n=n, random_state=rng)
    tr, te = train_test_split(s, test_size=0.2, random_state=rng)
    vec = CountVectorizer(ngram_range=(1, 2), min_df=2, lowercase=True)
    Xtr = vec.fit_transform(tr["title"]); nb = MultinomialNB(alpha=1.0).fit(Xtr, tr["label"])
    pred = nb.predict(vec.transform(te["title"]))
    acc = float((pred == te["label"]).mean()); base = float((te["label"] == "pos").mean())
    return vec, nb, acc, base
def score(vec, nb, texts):
    P = nb.predict_proba(vec.transform(texts)); cls = list(nb.classes_)
    return P[:, cls.index("pos")] - P[:, cls.index("neg")], np.array(cls)[P.argmax(1)]
vec, nb, acc, base = fit_nb(15000)
vec2, nb2, acc2, base2 = fit_nb(200000)
import pickle; pickle.dump((vec, nb), open(f"{D}/nb_model_15k.pkl", "wb"))
rv["tone_nb"] = np.nan; rv["tone_nb_big"] = np.nan; rv["nb_class"] = ""
t, c = score(vec, nb, rv.loc[has, "title"]); rv.loc[has, "tone_nb"] = t; rv.loc[has, "nb_class"] = c
rv.loc[has, "tone_nb_big"] = score(vec2, nb2, rv.loc[has, "title"])[0]
# class-based score as literally described in the paper text: positive in (0,1], negative in [-1,0), neutral = 0
pp = nb.predict_proba(vec.transform(rv.loc[has, "title"])); cls = list(nb.classes_)
rv.loc[has, "tone_nb_class"] = np.select([rv.loc[has, "nb_class"] == "pos", rv.loc[has, "nb_class"] == "neg"],
                                        [pp[:, cls.index("pos")], -pp[:, cls.index("neg")]], 0.0)
sia = SentimentIntensityAnalyzer()
rv["tone_vader"] = [sia.polarity_scores(x)["compound"] if x else np.nan for x in rv["title"]]
meta = dict(nb15k_test_accuracy=acc, nb15k_test_majority_baseline=base, nb200k_test_accuracy=acc2, nb200k_majority_baseline=base2,
            reviews_after_dedupe=int(len(rv)), reviews_with_summary=int(has.sum()), reviews_raw_matched=int(n0),
            top_pos_words=[w for w, _ in sorted(zip(vec.get_feature_names_out(), nb.feature_log_prob_[cls.index("pos")] - nb.feature_log_prob_[cls.index("neg")]), key=lambda x: -x[1])[:25]],
            top_neg_words=[w for w, _ in sorted(zip(vec.get_feature_names_out(), nb.feature_log_prob_[cls.index("neg")] - nb.feature_log_prob_[cls.index("pos")]), key=lambda x: -x[1])[:25]])
json.dump(meta, open(f"{D}/tone_model_info.json", "w"), indent=1); print(meta)
# --- quarters
rv["cal_q"] = rv.date.dt.to_period("Q").astype(str)
fy = rv.date.dt.year + (rv.date.dt.month >= 6).astype(int)
fq = ((rv.date.dt.month - 6) % 12) // 3 + 1
rv["fis_q"] = "Q" + fq.astype(str) + "FY" + fy.astype(str)
rv["fis_sort"] = fy * 10 + fq
keep = ["parent_asin", "brand", "firm", "footwear", "rating", "title", "date", "verified_purchase", "helpful_vote", "tone_nb", "tone_nb_big", "tone_nb_class", "tone_vader", "cal_q", "fis_q"]
rv[keep].to_parquet(f"{D}/amazon_reviews_scored.parquet", index=False)
def agg(df, qcol, unit):
    g = df.groupby([unit, qcol])
    out = g.agg(listings_proxy=("parent_asin", "nunique"), review_cnt=("rating", "size"), avg_rating=("rating", "mean"),
                share_1_2_star=("rating", lambda x: (x <= 2).mean()), avg_tone_nb=("tone_nb", "mean"), sd_tone_nb=("tone_nb", "std"),
                avg_tone_nb_big=("tone_nb_big", "mean"), avg_tone_nb_class=("tone_nb_class", "mean"), avg_tone_vader=("tone_vader", "mean"),
                sd_rating=("rating", "std"), share_verified=("verified_purchase", "mean")).reset_index()
    out = out.rename(columns={unit: "unit", qcol: "quarter"})
    out["qsort"] = out["quarter"].map(lambda q: int(q[4:8]) * 10 + int(q[1]) if q.startswith("Q") else int(q[:4]) * 10 + int(q[-1]))
    out = out.sort_values(["unit", "qsort"])
    res = []
    for u, x in out.groupby("unit"):
        x = x.set_index("qsort").reindex(range(x.qsort.min(), x.qsort.max() + 1)).dropna(subset=["quarter"]) if False else x.copy()
        # previous four quarters by position in a complete quarter grid
        full = pd.Series(sorted(set(out.qsort)))
        x = x.set_index("qsort")
        def prev4(col):
            vals = []
            for q in x.index:
                y, k = divmod(q, 10); prevs = []
                for j in range(1, 5):
                    kk = k - j; yy = y
                    while kk <= 0: kk += 4; yy -= 1
                    prevs.append(yy * 10 + kk)
                v = x[col].reindex(prevs)
                vals.append(v.mean() if v.notna().sum() == 4 else np.nan)
            return np.array(vals)
        x["AbnormalTone"] = x["avg_tone_nb"] - prev4("avg_tone_nb")
        x["AbnormalTone_big"] = x["avg_tone_nb_big"] - prev4("avg_tone_nb_big")
        x["AbnormalTone_vader"] = x["avg_tone_vader"] - prev4("avg_tone_vader")
        x["AbnormalRating"] = x["avg_rating"] - prev4("avg_rating")
        x["AbnormalReviewCnt"] = (x["review_cnt"] - prev4("review_cnt")) / 100.0
        x["StdDevTone"] = x["sd_tone_nb"] / x["avg_tone_nb"].abs()
        x["StdDevRating"] = x["sd_rating"] / x["avg_rating"]
        x["Negative_AbnormalTone"] = x["AbnormalTone"].clip(upper=0)
        x["Positive_AbnormalTone"] = x["AbnormalTone"].clip(lower=0)
        res.append(x.reset_index())
    return pd.concat(res)
for qcol, name in (("cal_q", "calendar"), ("fis_q", "nike_fiscal")):
    a = pd.concat([agg(rv, qcol, "firm").assign(level="firm"), agg(rv, qcol, "brand").assign(level="brand")])
    a = a[~((a.level == "brand") & a.unit.isin(a[a.level == "firm"].unit) & ~a.unit.isin(["Nike", "Jordan", "Converse"]))]
    fw = agg(rv[rv.footwear == 1], qcol, "firm").assign(level="firm_footwear_only")
    a = pd.concat([a, fw]); a.to_csv(f"{D}/amazon_quarterly_{name}.csv", index=False, float_format="%.4f")
    print(name, a.shape)
