"""Clean all raw pulls in ../raw into tidy CSVs in the parent folder.
Run: python3 -I clean_all.py <hunt_dir>
"""
import csv, glob, gzip, json, os, re, sys, datetime
import pandas as pd

H = sys.argv[1] if len(sys.argv) > 1 else ".."
R = os.path.join(H, "raw")

# ---------- Wikipedia: daily -> weekly / monthly ----------
rows = []
for fn in sorted(glob.glob(os.path.join(R, "wiki", "*.json"))):
    d = json.load(open(fn))
    if d.get("missing") or "items" not in d:
        continue
    for it in d["items"]:
        rows.append({"label": d["label"], "project": d["project"], "title": d["title_canonical"],
                     "date": pd.to_datetime(it["timestamp"][:8]), "views": it["views"]})
if rows:
    w = pd.DataFrame(rows)
    w.to_csv(os.path.join(H, "wiki_pageviews_daily_long.csv"), index=False)
    w["week"] = w["date"] - pd.to_timedelta(w["date"].dt.weekday, unit="D")
    wk = w.groupby(["label", "project", "title", "week"], as_index=False).agg(views=("views", "sum"), days=("views", "size"))
    wk = wk[wk["days"] == 7].drop(columns="days")
    wk.to_csv(os.path.join(H, "wiki_pageviews_weekly_long.csv"), index=False)
    w["month"] = w["date"].dt.to_period("M").astype(str)
    mo = w.groupby(["label", "project", "month"], as_index=False).agg(views=("views", "sum"), days=("views", "size"))
    mo.to_csv(os.path.join(H, "wiki_pageviews_monthly_long.csv"), index=False)
    print("wiki", w["label"].nunique(), "articles", len(w), "daily rows")

# ---------- Google Trends ----------
out = []
for fn in sorted(glob.glob(os.path.join(R, "gtrends", "*.csv"))):
    batch = os.path.basename(fn)[:-4]
    df = pd.read_csv(fn)
    if df.empty:
        continue
    part = df.get("isPartial")
    for c in df.columns:
        if c in ("date", "isPartial"):
            continue
        for i, r in df.iterrows():
            out.append({"batch": batch, "term": c, "date": r["date"], "value": r[c],
                        "is_partial": bool(r["isPartial"]) if "isPartial" in df.columns else False})
if out:
    pd.DataFrame(out).to_csv(os.path.join(H, "gtrends_batches_long.csv"), index=False)
    print("gtrends", len(out))

# ---------- Tranco ----------
fn = os.path.join(R, "tranco_hist", "tranco_tracked_domains.csv")
if os.path.exists(fn):
    t = pd.read_csv(fn)
    t.to_csv(os.path.join(H, "tranco_rank_semimonthly_long.csv"), index=False)
    print("tranco", len(t))

# ---------- Reddit titles: brand mention shares ----------
TERMS = {
    "nike": r"\bnike'?s?\b", "jordan": r"\b(jordan|aj ?1|aj ?4|aj ?11|jumpman)\b", "dunk": r"\bdunks?\b",
    "af1": r"\b(af ?1|air force)\b", "air_max": r"\bair ?max\b", "pegasus": r"\bpegasus\b",
    "vomero": r"\bvomero\b", "vaporfly": r"\bvaporfly\b", "alphafly": r"\balphafly\b",
    "nike_run_any": r"\b(pegasus|vomero|vaporfly|alphafly|invincible|zoomfly|zoom fly|streakfly|structure)\b",
    "adidas": r"\badidas\b", "samba": r"\bsambas?\b", "gazelle": r"\bgazelles?\b", "adizero": r"\badizero|adios|evo sl\b",
    "new_balance": r"\b(new balance|nb ?\d{3,4})\b", "asics": r"\basics\b|\bnovablast|superblast|gel[- ]kayano|nimbus\b",
    "hoka": r"\bhoka\b|\bclifton|bondi\b", "on": r"\bon (running|cloud)|\bcloud(monster|surfer|boom|tilt)\b",
    "saucony": r"\bsaucony\b|\bendorphin\b", "brooks": r"\bbrooks\b|\bghost \d|glycerin\b",
    "puma": r"\bpuma\b", "salomon": r"\bsalomon\b", "onitsuka": r"\bonitsuka\b", "converse": r"\bconverse\b|\bchuck",
    "yeezy": r"\byeezy\b",
}
CRX = {k: re.compile(v, re.I) for k, v in TERMS.items()}
rows = []
for fn in sorted(glob.glob(os.path.join(R, "reddit_titles", "*", "*.csv.gz"))):
    sub = fn.split(os.sep)[-2]
    month = os.path.basename(fn)[:7]
    n, cnt, eng = 0, {k: 0 for k in TERMS}, {k: 0 for k in TERMS}
    with gzip.open(fn, "rt") as f:
        for r in csv.DictReader(f):
            title = r["title"] or ""
            if title.startswith("[ Removed") or title in ("[deleted]", "[removed]"):
                continue
            n += 1
            nc = int(r["num_comments"] or 0)
            for k, rx in CRX.items():
                if rx.search(title):
                    cnt[k] += 1
                    eng[k] += nc
    for k in TERMS:
        rows.append({"subreddit": sub, "month": month, "term": k, "posts_total": n, "posts_mentioning": cnt[k],
                     "share_pct": round(100 * cnt[k] / n, 3) if n else None, "comments_on_mentioning": eng[k]})
if rows:
    pd.DataFrame(rows).to_csv(os.path.join(H, "reddit_title_mentions_monthly_sample.csv"), index=False)
    print("reddit", len(rows))

# ---------- App Store ----------
rows, rev = [], []
for fn in sorted(glob.glob(os.path.join(R, "appstore", "*.json"))):
    d = json.load(open(fn))
    rs = d["reviews"]
    dates = sorted(pd.to_datetime([x["updated"] for x in rs], utc=True)) if rs else []
    span = (dates[-1] - dates[0]).total_seconds() / 86400 if len(dates) > 1 else None
    rows.append({"app": d["app"], "country": d["country"], "pulled": d["pulled"], "userRatingCount": d["userRatingCount"],
                 "averageUserRating": d["averageUserRating"],
                 "userRatingCountForCurrentVersion": d.get("userRatingCountForCurrentVersion"),
                 "n_recent_reviews": len(rs), "recent_reviews_span_days": round(span, 2) if span else None,
                 "reviews_per_day": round(len(rs) / span, 2) if span else None,
                 "recent_avg_stars": round(sum(x["rating"] for x in rs) / len(rs), 2) if rs else None,
                 "recent_share_1star_pct": round(100 * sum(x["rating"] == 1 for x in rs) / len(rs), 1) if rs else None})
    for x in rs:
        rev.append({"app": d["app"], "country": d["country"], **x})
if rows:
    pd.DataFrame(rows).to_csv(os.path.join(H, "appstore_snapshot_2026-10-14.csv"), index=False)
    pd.DataFrame(rev).to_csv(os.path.join(H, "appstore_recent_reviews_2026-10-14.csv"), index=False)
    print("appstore", len(rows))

# ---------- Stocktwits ----------
rows, meta = [], []
for fn in sorted(glob.glob(os.path.join(R, "stocktwits", "*.json"))):
    d = json.load(open(fn))
    meta.append({"symbol": d["symbol"], "watchlist_count": (d.get("meta") or {}).get("watchlist_count"),
                 "pulled": d["pulled"], "messages_pulled": len(d["messages"])})
    for m in d["messages"]:
        rows.append({"symbol": d["symbol"], **m})
if rows:
    pd.DataFrame(rows).to_csv(os.path.join(H, "stocktwits_messages.csv"), index=False)
    pd.DataFrame(meta).to_csv(os.path.join(H, "stocktwits_watchlist_snapshot.csv"), index=False)
    print("stocktwits", len(rows))
