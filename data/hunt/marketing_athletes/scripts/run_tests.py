"""Tests for the marketing and athletes avenue. Reads tidy CSVs in the parent folder, prints results, writes test_*.csv."""
import pandas as pd, numpy as np, os, sys
os.chdir(sys.argv[1] if len(sys.argv) > 1 else ".")
pd.set_option("display.width", 220)
print("=== T1 Spend vs reach ===")
dc = {"FY2024": 4285, "FY2025": 4689, "FY2026": 4754}
print("Nike demand creation $M:", dc, "FY24->FY26 %:", round((4754 / 4285 - 1) * 100, 1), "| Q1 FY27 1252 vs 1188:", round((1252 / 1188 - 1) * 100, 1))
print("adidas marketing EUR M 2024->2025:", 2841, 3079, round((3079 / 2841 - 1) * 100, 1))
yt = pd.read_csv("test_youtube_subscriber_growth.csv"); print(yt.round(3).to_string())
ig = pd.read_csv("instagram_top_accounts_wiki_revisions.csv")
ig["t"] = pd.to_datetime(ig.rev_timestamp)
p = ig[ig.handle.isin(["nike", "cristiano", "leomessi", "realmadrid", "fcbarcelona", "nba", "championsleague", "instagram"])].pivot_table(index="t", columns="handle", values="followers_m")
print(p.to_string())
tt = pd.read_csv("tiktok_brand_snapshot_2026-10-14.csv").sort_values("followers", ascending=False); print(tt.to_string())
print("=== T2 Elite visibility share ===")
ev = pd.read_csv("elite_visibility_share.csv"); print(ev[["arena", "year", "nike_share_pct", "adidas_share_pct", "status"]].to_string())
for a, g in ev.groupby("arena"):
    g = g.dropna(subset=["nike_share_pct"]).sort_values("year")
    if len(g) > 1: print(f"{a[:55]:55s} first {g.year.iloc[0]} {g.nike_share_pct.iloc[0]} -> last {g.year.iloc[-1]} {g.nike_share_pct.iloc[-1]}")
print("=== T3 NBA court share ===")
n = pd.read_csv("nba_shoe_brand_minutes_by_season.csv"); n = n[n.league == "NBA"]
tot = n.groupby("season").minutes.sum(); n["share"] = n.minutes / n.season.map(tot)
pv = n.pivot_table(index="season", columns="brand", values="share").fillna(0)
pv["NikeInc"] = pv["Nike"] + pv["Jordan"] + pv.get("Converse", 0)
out = (pv[["NikeInc", "Nike", "Jordan", "adidas", "Puma", "Anta", "New Balance"]] * 100).round(1); print(out); out.to_csv("test_nba_share.csv")
print("=== T4 Club kits big leagues ===")
k = pd.read_csv("kits_team_season_tidy.csv")
big = ["Premier League", "La Liga", "Serie A", "Bundesliga", "Ligue 1"]
kb = k[k.league.isin(big)]
s = kb.groupby(["season_start", "league"]).brand.apply(lambda x: (x == "Nike").mean()).unstack().round(3); print(s)
s2 = kb.groupby("season_start").brand.value_counts().unstack(fill_value=0); print(s2[["Nike", "adidas", "Puma"]] if "Puma" in s2 else s2)
s2.to_csv("test_big5_kit_counts.csv")
ee = pd.read_csv("endorsement_events.csv"); print(ee.direction_for_nike.str.split().str[0].value_counts())

print("=== T1b Instagram Nike vs top-50 accounts ===")
print(pd.read_csv("test_instagram_nike_vs_top50.csv").to_string())
print("=== T4b Big-5 kits 2019 vs 2025 ===")
print(pd.read_csv("test_big5_kit_2019_vs_2025.csv").to_string())
print("=== YouTube long-form by year ===")
yl = pd.read_csv("test_youtube_longform_by_year.csv"); print(yl[yl.channel.isin(["nike","jordan","nikefootball","adidas","adidasfootball","newbalance","puma"])].to_string())
