"""Parse cached Wikipedia league-season pages into tidy team-season kit supplier rows and league-season brand shares."""
import sys, os, re, glob
import pandas as pd
RAW, OUT1, OUT2 = sys.argv[1], sys.argv[2], sys.argv[3]
rows = []
for fn in sorted(glob.glob(os.path.join(RAW, "*.html"))):
    base = os.path.basename(fn)[:-5]
    m = re.match(r"(\d{4})_(\d{2})_(.+)$", base) or re.match(r"(\d{4})_(.+)$", base)
    if not m: continue
    if len(m.groups()) == 3: season = f"{m.group(1)}-{m.group(2)}"; league = m.group(3).replace("_", " "); start = int(m.group(1))
    else: season = m.group(1); league = m.group(2).replace("_", " "); start = int(m.group(1))
    try: tabs = pd.read_html(fn)
    except Exception: continue
    for t in tabs:
        if isinstance(t.columns, pd.MultiIndex): t.columns = [" ".join(map(str, c)) for c in t.columns]
        cols = [str(c) for c in t.columns]
        kc = [c for c in cols if re.search(r"kit (manufacturer|supplier|maker)|^kit$|manufacturer", c, re.I)]
        tc = [c for c in cols if re.search(r"^(team|club)", c, re.I)]
        if kc and tc and len(t) >= 8:
            for _, r in t.iterrows():
                k = re.sub(r"\[.*?\]|\(.*?\)", "", str(r[kc[0]])).strip()
                k = k.replace("Νike", "Nike")
                rows.append(dict(league=league, season=season, season_start=start, team=re.sub(r"\[.*?\]", "", str(r[tc[0]])).strip(), kit_supplier=k))
            break
d = pd.DataFrame(rows).drop_duplicates(["league", "season", "team"])
d = d[~d.team.str.contains("Source|Note|nan", case=False)]
def norm(k):
    kl = k.lower()
    for b in ["nike", "adidas", "puma", "new balance", "under armour", "castore", "macron", "umbro", "hummel", "kappa", "joma", "jordan"]:
        if kl.startswith(b): return "Nike" if b in ("nike", "jordan") else b.title() if b != "adidas" else "adidas"
    return "Other"
d["brand"] = d.kit_supplier.map(norm)
d.to_csv(OUT1, index=False)
s = d.groupby(["league", "season_start", "brand"]).size().unstack(fill_value=0)
s["n_teams"] = s.sum(axis=1)
for b in ["Nike", "adidas", "Puma"]:
    if b in s: s[b + "_share"] = (s[b] / s["n_teams"]).round(3)
s.reset_index().to_csv(OUT2, index=False)
print(s[["n_teams", "Nike", "adidas", "Puma"]].to_string())
