"""Tag Reddit post titles (Arctic Shift pull) with running-shoe brands and model families; monthly tidy counts.
Usage: python3 -I clean_reddit.py <raw/reddit dir> <outdir>"""
import sys, os, re, pandas as pd
raw, out = sys.argv[1], sys.argv[2]
BRANDS = {
 "Nike": r"\bnike\b|pegasus|vomero|invincible|alphafly|vaporfly|zoom ?fly|streakfly|structure 2\d|infinity ?rn|winflo|\bpeg\s?\d\d|\bpeg plus|ja fly|victory 2",
 "HOKA": r"\bhoka\b|clifton|bondi|\bmach\s?[x\d]|rocket ?x|cielo|speedgoat|arahi|skyward|rincon|transport",
 "ASICS": r"\basics\b|novablast|nimbus|kayano|superblast|metaspeed|megablast|cumulus|gt-?2000|sonicblast",
 "adidas": r"\badidas\b|adizero|\bboston 1\d|evo ?sl|adios pro|takumi|supernova|\bsl2\b",
 "Brooks": r"\bbrooks\b|\bghost 1\d|ghost max|glycerin|adrenaline|hyperion",
 "On": r"\bon running\b|cloudmonster|cloudsurfer|cloudboom|cloudeclipse|cloudflow|cloudrunner|\bon cloud",
 "Saucony": r"\bsaucony\b|endorphin|\bride 1\d|triumph|kinvara|guide 1\d",
 "New Balance": r"new balance|\bnb\b|1080|\b880\b|rebel v\d|sc elite|sc trainer|fuelcell",
 "PUMA": r"\bpuma\b|deviate|magnify|velocity nitro|fast-r",
}
MODELS = {"Pegasus": r"pegasus(?! trail)|\bpeg\s?4\d|\bpeg plus", "Vomero": r"vomero(?! 5)", "Alphafly/Vaporfly": r"alphafly|vaporfly", "Invincible": r"invincible",
          "Clifton": r"clifton", "Bondi": r"bondi", "Mach": r"\bmach\s?[x\d]", "Novablast": r"novablast", "Superblast": r"superblast", "Nimbus": r"nimbus",
          "Ghost": r"\bghost\b", "Cloudmonster": r"cloudmonster", "Endorphin": r"endorphin", "Adizero Evo SL": r"evo ?sl", "Adios Pro": r"adios pro"}
frames = []
for f in sorted(os.listdir(raw)):
    if not f.endswith(".csv.gz"): continue
    d = pd.read_csv(os.path.join(raw, f)); d["subreddit"] = f.split(".")[0]; frames.append(d)
d = pd.concat(frames); d["date"] = pd.to_datetime(d.created_utc, unit="s"); d["month"] = d.date.dt.to_period("M").astype(str)
t = d.title.fillna("").str.lower(); d["flair"] = d.link_flair_text.fillna("").str.lower()
for b, rx in BRANDS.items(): d["b_" + b] = t.str.contains(rx, regex=True)
for m, rx in MODELS.items(): d["m_" + m] = t.str.contains(rx, regex=True)
d.drop(columns=["title"]).to_csv(os.path.join(out, "reddit_posts_tagged.csv.gz"), index=False, compression="gzip")
rows = []
for (sub, month), g in d.groupby(["subreddit", "month"]):
    base = dict(subreddit=sub, month=month, posts=len(g), comments=int(g.num_comments.sum()))
    for k in [c for c in d.columns if c.startswith("b_") or c.startswith("m_")]:
        gg = g[g[k]]
        rows.append({**base, "tag": k[2:], "kind": "brand" if k.startswith("b_") else "model", "mentions": len(gg), "mention_comments": int(gg.num_comments.sum()),
                     "deal_posts": int(gg.flair.str.contains("deal").sum()), "review_posts": int(gg.flair.str.contains("review").sum())})
pd.DataFrame(rows).to_csv(os.path.join(out, "reddit_monthly_mentions.csv"), index=False)
print(len(d), "posts;", len(rows), "rows")
