"""US App Store rating-count velocity: repo snapshot (data/altdata/appstore_ratings_snapshot_2026-10-13.csv, committed 2026-10-13 20:22 UTC,
used as an upper bound on its pull time) vs iTunes lookup pulls in raw/itunes_lookup/us_*.json."""
import json, glob, pandas as pd
BASE = "/home/user/nike-research-case-comp/data/hunt/apps_digital"
old = pd.read_csv(f"{BASE}/raw/itunes_lookup/repo_snapshot_2026-10-13.csv")
t0 = pd.Timestamp("2026-10-13 20:22:35", tz="UTC")
rows = []
for f in sorted(glob.glob(f"{BASE}/raw/itunes_lookup/us_*.json")):
    ts = pd.Timestamp(f.split("us_")[1][:-5], tz="UTC")
    for x in json.load(open(f))["results"]:
        rows.append([ts, x["trackId"], x["trackName"], x["userRatingCount"]])
d = pd.DataFrame(rows, columns=["ts", "track_id", "app_name", "count"])
last = d[d.ts == d.ts.max()]
m = old[["track_id", "rating_count_all_time"]].merge(last, on="track_id")
hrs = (d.ts.max() - t0).total_seconds() / 3600
m["new_ratings"] = m["count"] - m.rating_count_all_time
m["per_day_upper_bound"] = m.new_ratings / hrs * 24
m["per_day_per_100k_base"] = m.per_day_upper_bound / m.rating_count_all_time * 1e5
m["hours_window_min"] = round(hrs, 1)
m.assign(app_name=m.app_name.str.replace('\u2014', '-')).sort_values("per_day_upper_bound").to_csv(f"{BASE}/ios_rating_velocity_us.csv", index=False)
print(m[["app_name", "rating_count_all_time", "count", "new_ratings", "per_day_upper_bound", "per_day_per_100k_base"]].round(1).to_string())
